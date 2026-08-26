"""Centralize audited article artifacts and rewrite citations to library wrappers.

The input manifest is produced by ``scan_sources.py``.  The migration is
deterministic: exact duplicate payloads are verified by SHA-256 before removal,
one canonical copy is moved into the article module, and immutable/raw areas are
excluded from citation rewrites.
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
AUDIT_DIR = Path(__file__).resolve().parent
LIBRARY = ROOT / "library"

MANIFEST_PATH = AUDIT_DIR / "manifest.json"
MANUAL_METADATA_PATH = AUDIT_DIR / "manual-metadata.json"

EXISTING_DOI_MODULES = {
    "10.1006/jfan.2000.3718": "noncommutative-flow-of-weights",
    "10.1016/0370-2693(89)91251-3": "cosmological-constant-and-general-covariance",
    "10.1088/1751-8121/ac8fc5": "from-ncg-to-random-matrix-theory",
    "10.1103/7whh-9j22": "phantom-cold-dark-matter",
    "10.1103/physrevd.61.084027": "wald-zoupas-conserved-quantities",
    "10.20944/preprints202506.0446.v2": "lorentzian-kernel-epistemic-envelope",
}

EXISTING_ARXIV_MODULES = {
    "0706.3688": "why-the-standard-model",
    "1409.2471": "quanta-of-geometry",
    "1411.1320": "twisted-spectral-triple-standard-model",
    "2011.14234": "the-tenfold-way",
    "2111.04488": "planar-algebraic-conditional-expectations",
    "2112.12828": "gravity-and-the-crossed-product",
    "2206.10780": "de-sitter-observables-algebra",
    "2402.17844": "renormalisation-of-postquantum-gravity",
    "2402.19459": "anomalous-galactic-rotation-curves",
    "2403.11973": "quantum-reference-frames-local-algebra-types",
    "2411.19931": "linearization-instabilities-and-cross-products",
    "2603.16639": "hodge-atoms-spectral-triples-bps",
    "2605.05375": "stochastic-modes-in-postquantum-gravity",
    "hep-th/0608226": "ncg-standard-model-neutrino-mixing",
    "math/0412061": "extension-of-borchers-structure-theorem",
}

# Correct the single spelling in the static table above from the actual module.
EXISTING_ARXIV_MODULES["2411.19931"] = "linearization-instabilities-and-crossed-products"

RAW_PARTS = {"chats", "inbox", "junk-drawer", "_inq"}
RAW_PREFIXES = (
    "causal-scale-theory/sources/legacy/",
)
RAW_SOURCE_SEGMENTS = (
    "/sources/code/",
    "/sources/data/",
    "/sources/snapshots/",
)

WIKI_RE = re.compile(r"\[\[(?P<target>[^\]|#]+)(?P<anchor>#[^\]|]+)?(?:\|(?P<label>[^\]]+))?\]\]")
MARKDOWN_LINK_RE = re.compile(
    r"\[(?P<label>[^\]]+)\]\((?P<target>https?://(?:[^()\s]|\([^)]*\))+|[^)]+)\)"
)
ARXIV_URL_RE = re.compile(
    r"https?://(?:export\.)?arxiv\.org/(?:abs|pdf|e-print)/"
    r"(?P<id>(?:[a-z-]+/)?\d{4}\.\d{4,5}(?:v\d+)?|(?:[a-z-]+/)?\d{7}(?:v\d+)?)",
    re.IGNORECASE,
)
DOI_URL_RE = re.compile(r"https?://(?:dx\.)?doi\.org/(?P<doi>10\.\d{4,9}/.+)", re.IGNORECASE)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_arxiv(identifier: str) -> str:
    identifier = identifier.removesuffix(".pdf")
    return re.sub(r"v\d+$", "", identifier)


def normalize_doi(doi: str) -> str:
    return doi.strip().rstrip(".,;").lower()


def join_authors(authors: list[str]) -> str:
    authors = [author.strip() for author in authors if author.strip()]
    if not authors:
        return "Not stated"
    if len(authors) > 20:
        if "collaboration" in authors[0].lower():
            return f"{authors[0]} ({len(authors)} author entries in the source record)"
        return f"{', '.join(authors[:8])}, et al. ({len(authors)} author entries in the source record)"
    if len(authors) == 1:
        return authors[0]
    if len(authors) == 2:
        return f"{authors[0]} and {authors[1]}"
    return f"{', '.join(authors[:-1])}, and {authors[-1]}"


def date_only(value: str | None) -> str | None:
    return value[:10] if value else None


def load_articles() -> list[dict[str, object]]:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    manual = json.loads(MANUAL_METADATA_PATH.read_text(encoding="utf-8"))
    articles = manifest["articles"]
    known = {article["identity"] for article in articles}
    for article in articles:
        if article["identity"] in manual:
            supplied = manual[article["identity"]]
            article["metadata"] = supplied["metadata"]
            article["module"] = supplied.get("module", article["module"])
    for identity, supplied in manual.items():
        if identity in known:
            continue
        articles.append(
            {
                "identity": identity,
                "module": supplied["module"],
                "existing_module": False,
                "metadata": supplied["metadata"],
                "assets": [],
            }
        )
    articles.sort(key=lambda article: str(article["module"]))
    missing = [article["identity"] for article in articles if not article.get("metadata")]
    if missing:
        raise ValueError(f"Missing metadata for: {missing}")
    return articles


def asset_score(record: dict[str, object]) -> tuple[int, int, str]:
    name = Path(str(record["path"])).name
    generic_penalty = -1000 if name.lower() in {"paper.tex", "main.pdf"} else 0
    return (generic_penalty + len(name), -len(Path(str(record["path"])).parts), str(record["path"]))


def plan_assets(articles: list[dict[str, object]]) -> tuple[dict[str, dict[str, str]], dict[str, list[str]]]:
    path_plan: dict[str, dict[str, str]] = {}
    files_by_identity: dict[str, list[str]] = defaultdict(list)
    for article in articles:
        identity = str(article["identity"])
        module = str(article["module"])
        by_hash: dict[str, list[dict[str, object]]] = defaultdict(list)
        for record in article.get("assets", []):
            by_hash[str(record["sha256"])].append(record)
        used_names: dict[str, str] = {}
        for digest, group in sorted(by_hash.items()):
            canonical = max(group, key=asset_score)
            name = Path(str(canonical["path"])).name
            if name in used_names and used_names[name] != digest:
                stem = Path(name).stem
                suffixes = "".join(Path(name).suffixes)
                name = f"{stem}-{digest[:8]}{suffixes}"
            used_names[name] = digest
            destination = f"library/{module}/{name}"
            files_by_identity[identity].append(name)
            for record in group:
                path_plan[str(record["path"])] = {
                    "identity": identity,
                    "module": module,
                    "destination": destination,
                    "sha256": digest,
                    "canonical_source": str(canonical["path"]),
                }
    return path_plan, files_by_identity


def is_raw(path: Path) -> bool:
    relative = rel(path)
    if any(part in RAW_PARTS for part in path.relative_to(ROOT).parts):
        return True
    if relative.startswith(RAW_PREFIXES):
        return True
    if path.name == "entry.md" and path.parent.name in {"code", "data"} and path.parent.parent.name == "sources":
        return False
    padded = f"/{relative}"
    return any(segment in padded for segment in RAW_SOURCE_SEGMENTS)


def module_root(path: Path) -> Path:
    current = path.parent
    while current != ROOT:
        if (current / "inq.toml").exists():
            return current
        current = current.parent
    return path.parent


def resolve_artifact_target(current_file: Path, target: str, path_plan: dict[str, dict[str, str]]) -> str | None:
    normalized = target.replace("\\", "/").removeprefix("./")
    if normalized in path_plan:
        return normalized
    candidates = []
    for base in (current_file.parent, module_root(current_file), ROOT):
        try:
            candidate = (base / normalized).resolve().relative_to(ROOT.resolve()).as_posix()
        except (ValueError, OSError):
            continue
        candidates.append(candidate)
    for candidate in candidates:
        if candidate in path_plan:
            return candidate
    suffix_matches = [old for old in path_plan if old.endswith(f"/{normalized}")]
    if len(suffix_matches) == 1:
        return suffix_matches[0]
    return None


def wrapper_target(module: str) -> str:
    return f"library/{module}/entry"


def rewrite_artifact_literals(text: str, path_plan: dict[str, dict[str, str]]) -> str:
    destinations_by_literal: dict[str, set[str]] = defaultdict(set)
    for old, plan in path_plan.items():
        old_path = Path(old)
        candidates = {old, old_path.name}
        if len(old_path.parts) >= 2:
            candidates.add("/".join(old_path.parts[-2:]))
        for candidate in candidates:
            destinations_by_literal[candidate].add(plan["destination"])
    replacements = {
        literal: next(iter(destinations))
        for literal, destinations in destinations_by_literal.items()
        if len(destinations) == 1 and literal != next(iter(destinations))
    }
    for literal in sorted(replacements, key=len, reverse=True):
        pattern = rf"(?<![A-Za-z0-9_./-]){re.escape(literal)}(?![A-Za-z0-9_./-])"
        text = re.sub(pattern, replacements[literal], text)
    return text


def rewrite_markdown(
    path: Path,
    path_plan: dict[str, dict[str, str]],
    arxiv_modules: dict[str, str],
    doi_modules: dict[str, str],
    title_by_identity: dict[str, str],
) -> bool:
    if is_raw(path) or "library" in path.relative_to(ROOT).parts or path.parts[0:1] == ("_inq",):
        return False
    original = path.read_text(encoding="utf-8")
    relative_parts = path.relative_to(ROOT).parts
    artifact_context = path.name in {"origins.md", "checksums.md"} or (
        path.name == "README.md" and "sources" in relative_parts
    )

    def replace_wiki(match: re.Match[str]) -> str:
        old = resolve_artifact_target(path, match.group("target"), path_plan)
        if not old:
            return match.group(0)
        plan = path_plan[old]
        label = match.group("label")
        old_suffix = Path(old).suffix.lower()
        if artifact_context or old_suffix != ".pdf":
            target = plan["destination"]
            display = f"|{label}" if label else ""
            return f"[[{target}{display}]]"
        identity = plan["identity"]
        display = label or title_by_identity.get(identity) or Path(old).stem
        return f"[[{wrapper_target(plan['module'])}|{display}]]"

    text = WIKI_RE.sub(replace_wiki, original)

    # Work line-by-line so a line that already cites the wrapper does not gain a
    # second link merely because it also carried an upstream record URL.
    output_lines: list[str] = []
    for line in text.splitlines(keepends=True):
        def replace_link(match: re.Match[str]) -> str:
            label = match.group("label")
            target = match.group("target")
            old = resolve_artifact_target(path, target, path_plan)
            if old:
                plan = path_plan[old]
                if artifact_context or Path(old).suffix.lower() != ".pdf":
                    return f"[[{plan['destination']}|{label}]]"
                canonical = wrapper_target(plan["module"])
                return f"[[{canonical}|{label}]]"
            if artifact_context:
                return match.group(0)
            arxiv_match = ARXIV_URL_RE.fullmatch(target)
            module = None
            if arxiv_match:
                module = arxiv_modules.get(normalize_arxiv(arxiv_match.group("id")))
            doi_match = DOI_URL_RE.fullmatch(target)
            if doi_match:
                module = doi_modules.get(normalize_doi(doi_match.group("doi")))
            if target.startswith("https://www.ulam.ai/research/jacobian.pdf"):
                module = "counterexample-to-the-jacobian-conjecture"
            if not module:
                return match.group(0)
            canonical = wrapper_target(module)
            if f"[[{canonical}|" in line or f"[[{canonical}]]" in line:
                return label
            return f"[[{canonical}|{label}]]"

        output_lines.append(MARKDOWN_LINK_RE.sub(replace_link, line))
    text = "".join(output_lines)
    if artifact_context:
        text = rewrite_artifact_literals(text, path_plan)
    if text != original:
        path.write_text(text, encoding="utf-8", newline="\n")
        return True
    return False


def publication_year(meta: dict[str, object]) -> str:
    if meta.get("year"):
        return str(meta["year"])
    journal_reference = str(meta.get("journal_reference") or "")
    years = re.findall(r"(?<!\d)(?:18|19|20)\d{2}(?!\d)", journal_reference)
    if years:
        return years[-1]
    published = date_only(meta.get("published"))
    return published[:4] if published else "Not recorded"


def source_block(meta: dict[str, object], files: list[str], identity: str, module: str) -> str:
    lines = [
        "## Metadata",
        "",
        f"- **Authors:** {join_authors(list(meta.get('authors') or []))}.",
        f"- **Year:** {publication_year(meta)}.",
    ]
    arxiv_id = meta.get("identity") if str(meta.get("identity", "")).count(":") == 0 else None
    if meta.get("record_url") and arxiv_id:
        version = meta.get("version") or ""
        if date_only(meta.get("published")):
            lines.append(f"- **First submitted:** {date_only(meta.get('published'))}.")
        if date_only(meta.get("updated")) and date_only(meta.get("updated")) != date_only(meta.get("published")):
            lines.append(f"- **Last revised:** {date_only(meta.get('updated'))}.")
        category = meta.get("primary_category")
        if category:
            lines.append(f"- **Primary category:** `{category}`.")
        lines.append(f"- **arXiv:** [{arxiv_id}{version}]({meta['record_url']}).")
    elif meta.get("record_url"):
        if date_only(meta.get("published")):
            lines.append(f"- **Published:** {date_only(meta.get('published'))}.")
        lines.append(f"- **Primary record:** [source page]({meta['record_url']}).")
    if meta.get("journal_reference"):
        lines.append(f"- **Publication:** {str(meta['journal_reference']).rstrip('.')}.")
    if meta.get("doi"):
        lines.append(f"- **DOI:** [{meta['doi']}](https://doi.org/{meta['doi']}).")
    if files:
        rendered = ", ".join(f"`{name}`" for name in sorted(files))
        lines.append(f"- **Local artifacts:** {rendered}.")
    else:
        lines.append("- **Local artifacts:** None held in this workspace.")
    note = meta.get("abstract_note")
    if note:
        lines.extend(["", str(note)])
    return "\n".join(lines)


def write_wrappers(articles: list[dict[str, object]], files_by_identity: dict[str, list[str]]) -> None:
    for article in articles:
        identity = str(article["identity"])
        module = str(article["module"])
        meta = dict(article["metadata"])
        title = str(meta["title"]).strip()
        abstract = str(meta["abstract"]).strip()
        module_dir = LIBRARY / module
        module_dir.mkdir(parents=True, exist_ok=True)
        entry = f"# {title}\n\n{abstract}\n\n{source_block(meta, files_by_identity.get(identity, []), identity, module)}\n"
        (module_dir / "entry.md").write_text(entry, encoding="utf-8", newline="\n")
        (module_dir / "inq.toml").write_text(
            f'[module]\nname = "{module}"\nentry = "entry.md"\ninclude = ["**"]\n',
            encoding="utf-8",
            newline="\n",
        )


def move_assets(path_plan: dict[str, dict[str, str]]) -> tuple[int, int]:
    moved = 0
    removed_duplicates = 0
    by_destination: dict[str, list[tuple[str, dict[str, str]]]] = defaultdict(list)
    for old, plan in path_plan.items():
        by_destination[plan["destination"]].append((old, plan))
    for destination_rel, group in sorted(by_destination.items()):
        plan = group[0][1]
        digest = plan["sha256"]
        canonical_rel = plan["canonical_source"]
        destination = ROOT / destination_rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        canonical = ROOT / canonical_rel
        if destination.exists():
            if sha256(destination) != digest:
                raise ValueError(f"Destination collision: {destination_rel}")
        else:
            if not canonical.exists() or sha256(canonical) != digest:
                raise ValueError(f"Canonical source missing or changed: {canonical_rel}")
            shutil.move(str(canonical), str(destination))
            moved += 1
        for old_rel, _ in group:
            old = ROOT / old_rel
            if old.exists():
                if sha256(old) != digest:
                    raise ValueError(f"Duplicate changed before removal: {old_rel}")
                old.unlink()
                removed_duplicates += 1
    return moved, removed_duplicates


def register_library_modules() -> int:
    workspace_path = ROOT / "inq.toml"
    original = workspace_path.read_text(encoding="utf-8")
    match = re.search(r"(?ms)(members\s*=\s*\[)(.*?)(\n\])", original)
    if not match:
        raise ValueError("Could not locate workspace members array")
    existing = set(re.findall(r'"([^"]+)"', match.group(2)))
    modules = sorted(
        rel(path.parent)
        for path in LIBRARY.glob("*/inq.toml")
        if path.parent.name != "inbox"
    )
    missing = [module for module in modules if module not in existing]
    if not missing:
        return 0
    insertion = "".join(f'\n  "{module}",' for module in missing)
    updated = original[: match.end(2)] + insertion + original[match.end(2) :]
    workspace_path.write_text(updated, encoding="utf-8", newline="\n")
    return len(missing)


def normalize_library_manifests() -> int:
    changed = 0
    for module_dir in sorted(path.parent for path in LIBRARY.glob("*/entry.md")):
        if module_dir.name == "inbox":
            continue
        manifest = module_dir / "inq.toml"
        desired = (
            "[module]\n"
            f'name = "{module_dir.name}"\n'
            'entry = "entry.md"\n'
            'include = ["**"]\n'
        )
        if not manifest.exists() or manifest.read_text(encoding="utf-8") != desired:
            manifest.write_text(desired, encoding="utf-8", newline="\n")
            changed += 1
    return changed


def write_registry(articles: list[dict[str, object]]) -> None:
    migrated = {str(article["module"]): article for article in articles}
    records = []
    for entry in sorted(LIBRARY.glob("*/entry.md")):
        module = entry.parent.name
        text = entry.read_text(encoding="utf-8")
        title = text.splitlines()[0].removeprefix("# ") if text else module
        article = migrated.get(module)
        if article:
            identity = article["identity"]
            meta = article["metadata"]
            arxiv = meta.get("identity") if "arxiv.org/abs/" in str(meta.get("record_url", "")) else None
            doi = meta.get("doi")
        else:
            arxiv_match = re.search(r"arxiv\.org/abs/([^/)]+(?:/[^/)]+)?)", text, re.IGNORECASE)
            doi_match = re.search(r"doi\.org/(10\.\d{4,9}/[^)\s]+)", text, re.IGNORECASE)
            arxiv = normalize_arxiv(arxiv_match.group(1)) if arxiv_match else None
            doi = doi_match.group(1).rstrip(".,") if doi_match else None
            identity = f"arxiv:{arxiv}" if arxiv else (f"doi:{doi}" if doi else None)
        artifacts = []
        for path in sorted(entry.parent.rglob("*")):
            if not path.is_file() or path.name in {"entry.md", "inq.toml"}:
                continue
            artifacts.append({"path": path.relative_to(entry.parent).as_posix(), "bytes": path.stat().st_size, "sha256": sha256(path)})
        records.append(
            {
                "module": module,
                "title": title,
                "identity": identity,
                "arxiv": arxiv,
                "doi": doi,
                "artifacts": artifacts,
            }
        )
    payload = {
        "generated": "2026-08-26",
        "identity_priority": ["doi", "arxiv_base_id", "official_repository_id", "title_authors_year_and_sha256"],
        "modules": records,
    }
    (LIBRARY / "identities.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def main() -> None:
    articles = load_articles()
    path_plan, files_by_identity = plan_assets(articles)
    arxiv_modules = dict(EXISTING_ARXIV_MODULES)
    doi_modules = {normalize_doi(doi): module for doi, module in EXISTING_DOI_MODULES.items()}
    title_by_identity = {}
    for article in articles:
        identity = str(article["identity"])
        module = str(article["module"])
        meta = article["metadata"]
        title_by_identity[identity] = str(meta["title"])
        if not identity.startswith(("doi:", "journal:", "preprint:", "url:")):
            arxiv_modules[normalize_arxiv(identity)] = module
            doi_modules[f"10.48550/arxiv.{normalize_arxiv(identity).lower()}"] = module
        if meta.get("doi"):
            doi_modules[normalize_doi(str(meta["doi"]))] = module

    changed_markdown = 0
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        if rewrite_markdown(path, path_plan, arxiv_modules, doi_modules, title_by_identity):
            changed_markdown += 1

    write_wrappers(articles, files_by_identity)
    moved, removed = move_assets(path_plan)
    normalized_manifests = normalize_library_manifests()
    registered = register_library_modules()
    write_registry(articles)
    print(
        json.dumps(
            {
                "article_wrappers_written": len(articles),
                "article_payloads_moved": moved,
                "duplicate_payload_copies_removed": removed,
                "markdown_files_rewritten": changed_markdown,
                "library_manifests_normalized": normalized_manifests,
                "library_modules_registered": registered,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
