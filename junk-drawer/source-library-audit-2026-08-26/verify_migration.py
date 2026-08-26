"""Verify the completed 2026-08-26 primary-source library migration."""

from __future__ import annotations

import gzip
import importlib.util
import json
import re
import sys
import tarfile
from collections import defaultdict
from pathlib import Path

from pypdf import PdfReader


sys.dont_write_bytecode = True


AUDIT_DIR = Path(__file__).resolve().parent
ROOT = AUDIT_DIR.parents[1]


def load_migration_module():
    path = AUDIT_DIR / "migrate_library.py"
    spec = importlib.util.spec_from_file_location("source_library_migration", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def should_check_markdown(path: Path, migration) -> bool:
    relative = migration.rel(path)
    parts = path.relative_to(ROOT).parts
    if any(part in {"chats", "inbox", "junk-drawer", "_inq"} for part in parts):
        return False
    if relative.startswith("causal-scale-theory/sources/legacy/"):
        return False
    padded = f"/{relative}"
    if any(segment in padded for segment in ("/sources/code/", "/sources/data/", "/sources/snapshots/")):
        return path.name == "entry.md"
    return True


def main() -> None:
    migration = load_migration_module()
    articles = migration.load_articles()
    path_plan, _ = migration.plan_assets(articles)
    errors: list[str] = []

    # Wrapper and asset ownership contract.
    for article in articles:
        identity = str(article["identity"])
        module = str(article["module"])
        entry = ROOT / "library" / module / "entry.md"
        manifest = ROOT / "library" / module / "inq.toml"
        if not entry.exists():
            errors.append(f"{module}: missing entry.md")
            continue
        text = entry.read_text(encoding="utf-8")
        lines = text.splitlines()
        if not lines or not lines[0].startswith("# "):
            errors.append(f"{module}: entry does not start with an H1")
        if len(lines) < 3 or lines[1].strip() or not lines[2].strip():
            errors.append(f"{module}: H1 is not followed by an immediate summary paragraph")
        for field in ("## Metadata", "- **Authors:**", "- **Year:**", "- **Local artifacts:**"):
            if field not in text:
                errors.append(f"{module}: missing {field}")
        if not any(field in text for field in ("- **Published:**", "- **First submitted:**")):
            errors.append(f"{module}: missing publication or submission date")
        if not manifest.exists() or 'include = ["**"]' not in manifest.read_text(encoding="utf-8"):
            errors.append(f"{module}: invalid library manifest")
        if not identity:
            errors.append(f"{module}: empty source identity")

    for old, record in path_plan.items():
        destination = ROOT / record["destination"]
        if not destination.exists():
            errors.append(f"{record['destination']}: destination missing")
        elif migration.sha256(destination) != record["sha256"]:
            errors.append(f"{record['destination']}: destination hash mismatch")
        if (ROOT / old).exists():
            errors.append(f"{old}: original artifact path still exists")

    # All library modules, including modules that predate this audit.
    library_modules = []
    for entry in sorted((ROOT / "library").glob("*/entry.md")):
        if entry.parent.name == "inbox":
            continue
        library_modules.append(entry.parent.name)
        text = entry.read_text(encoding="utf-8")
        lines = text.splitlines()
        if not lines or not lines[0].startswith("# "):
            errors.append(f"{entry.parent.name}: library H1 missing")
        if len(lines) < 3 or lines[1].strip() or not lines[2].strip():
            errors.append(f"{entry.parent.name}: library opening summary missing")
        manifest = entry.parent / "inq.toml"
        if not manifest.exists() or 'include = ["**"]' not in manifest.read_text(encoding="utf-8"):
            errors.append(f"{entry.parent.name}: library manifest is not normalized")

    workspace_manifest = (ROOT / "inq.toml").read_text(encoding="utf-8")
    for module in library_modules:
        if f'"library/{module}"' not in workspace_manifest:
            errors.append(f"library/{module}: not registered in root workspace")

    # Local link migration: old paths must disappear from mutable prose and all
    # library wiki targets must resolve.
    stale_paths = []
    unresolved_library_links = []
    library_link_count = 0
    library_wiki = re.compile(r"\[\[(library/[^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts or not should_check_markdown(path, migration):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        normalized = text.replace("\\", "/")
        for old in path_plan:
            if old in normalized:
                stale_paths.append(f"{migration.rel(path)} -> {old}")
        for match in library_wiki.finditer(text):
            library_link_count += 1
            target = match.group(1)
            if target.startswith("library/inbox/"):
                continue
            target_path = ROOT / target
            if target_path.suffix:
                resolved = target_path.exists()
            else:
                resolved = target_path.with_suffix(".md").exists() or (target_path / "entry.md").exists()
            if not resolved:
                unresolved_library_links.append(f"{migration.rel(path)} -> {target}")
    errors.extend(f"stale artifact path: {item}" for item in stale_paths)
    errors.extend(f"unresolved library link: {item}" for item in unresolved_library_links)

    # No exact duplicate article PDFs or source archives may remain anywhere in
    # the workspace, including immutable areas. Audit receipts are excluded.
    by_hash: dict[tuple[str, int], list[str]] = defaultdict(list)
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "junk-drawer" in path.parts:
            continue
        lower = path.name.lower()
        if not (lower.endswith(".pdf") or lower.endswith(".tar.gz")):
            continue
        key = (migration.sha256(path), path.stat().st_size)
        by_hash[key].append(migration.rel(path))
    duplicate_groups = [paths for paths in by_hash.values() if len(paths) > 1]
    for group in duplicate_groups:
        errors.append(f"duplicate payload remains: {group}")

    pdfs = list((ROOT / "library").rglob("*.pdf"))
    for path in pdfs:
        try:
            if not PdfReader(path).pages:
                errors.append(f"{migration.rel(path)}: PDF has no pages")
        except Exception as exc:  # pragma: no cover - diagnostic path
            errors.append(f"{migration.rel(path)}: PDF open failed: {exc}")

    archives = list((ROOT / "library").rglob("*.tar.gz"))
    archive_count = 0
    legacy_stream_count = 0
    for path in archives:
        try:
            with tarfile.open(path, "r:*") as stream:
                stream.getmembers()
            archive_count += 1
        except tarfile.ReadError:
            try:
                with gzip.open(path, "rb") as stream:
                    if not stream.read(512):
                        raise ValueError("empty gzip stream")
                legacy_stream_count += 1
            except Exception as exc:  # pragma: no cover - diagnostic path
                errors.append(f"{migration.rel(path)}: source payload unreadable: {exc}")

    registry = json.loads((ROOT / "library" / "identities.json").read_text(encoding="utf-8"))
    registry_modules = [record["module"] for record in registry["modules"]]
    if len(registry_modules) != len(set(registry_modules)):
        errors.append("library/identities.json contains duplicate module records")
    if set(registry_modules) != set(library_modules):
        errors.append("library/identities.json does not match the registered library modules")

    result = {
        "migrated_wrappers_checked": len(articles),
        "all_library_modules_checked": len(library_modules),
        "original_asset_references_checked": len(path_plan),
        "unique_migrated_payloads": len({record["destination"] for record in path_plan.values()}),
        "library_wiki_links_checked": library_link_count,
        "workspace_pdf_and_archive_files_hashed": sum(len(paths) for paths in by_hash.values()),
        "duplicate_pdf_or_archive_groups_remaining": len(duplicate_groups),
        "library_pdfs_opened": len(pdfs),
        "source_tar_archives_read": archive_count,
        "legacy_gzip_source_streams_read": legacy_stream_count,
        "errors": len(errors),
    }
    print(json.dumps(result, indent=2))
    if errors:
        print("\n".join(errors))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
