"""Build a reproducible manifest for the 2026-08-26 source-library audit.

This script is intentionally limited to article corpora already present in the
workspace plus a short list of repeatedly cited articles that have no local
payload.  It does not modify canonical notes or move artifacts.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import time
import unicodedata
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
AUDIT_DIR = Path(__file__).resolve().parent

ARTICLE_GLOBS = (
    "causal-wall-spectral-theory/sources/papers/*.pdf",
    "compatible-with-existing-physics/sources/papers/*.pdf",
    "conformal-time/sources/*.pdf",
    "deriving-value-of-g/sources/papers/*.pdf",
    "deriving-value-of-g/sources/arxiv-source/*",
    "misner-log-time/sources/*.pdf",
    "misner-log-time/sources/*source.tar.gz",
    "misner-log-time/sources/*source/*",
    "symmetry-groups-select/sources/papers/*.pdf",
    "vendor/entropic-gravity/sources/papers/*.pdf",
    "vendor/entropic-gravity/sources/arxiv-source/*",
    "_inq/arxiv-2002-03318/paper.tex",
    "_inq/arxiv-2002-03318/source/*",
)

# These are repeatedly cited in mutable canonical notes but have no local paper
# payload and no current root-library owner.
REPEATED_URL_ONLY_IDS = (
    "math-ph/0006030",
    "1805.09234",
    "2008.04810",
    "2503.14738",
    "2102.04486",
    "2607.27410",
    "1607.03901",
    "1909.01906",
    "1512.06431",
    "2504.15336",
    "1807.06209",
    "1908.10824",
    "2608.00222",
)

EXISTING_MODULE_BY_ID = {
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
    "2411.19931": "linearization-instabilities-and-crossed-products",
    "2603.16639": "hodge-atoms-spectral-triples-bps",
    "2605.05375": "stochastic-modes-in-postquantum-gravity",
    "hep-th/0608226": "ncg-standard-model-neutrino-mixing",
    "math/0412061": "extension-of-borchers-structure-theorem",
}

MODULE_OVERRIDE_BY_ID = {
    **EXISTING_MODULE_BY_ID,
    "doi:10.1093/mnras/116.6.662": "visual-horizons-in-world-models",
    "doi:10.1103/PhysRevLett.10.66": "asymptotic-properties-of-fields-and-spacetimes",
    "doi:10.1103/PhysRev.183.1057": "quantized-fields-and-particle-creation-i",
    "doi:10.1103/PhysRev.186.1319": "quantum-cosmology-i",
    "doi:10.1103/PhysRevLett.22.1071": "mixmaster-universe",
    "doi:10.2139/ssrn.6093146": "fine-structure-constant-from-first-principles",
    "doi:10.2977/prims/1195192744": "relative-hamiltonian-for-faithful-normal-states",
    "doi:10.2977/prims/1195191148": "relative-entropy-of-states-of-von-neumann-algebras",
    "doi:10.2977/prims/1195190105": "relative-entropy-for-states-of-von-neumann-algebras-ii",
    "journal:mukhanov-1988-gauge-invariant-perturbations": "quantum-theory-of-gauge-invariant-cosmological-perturbations",
    "preprint:esi-204": "geometries-of-quantum-states",
    "2002.03318": "l0-regularized-high-dimensional-aft-model",
    "0706.3690": "standard-model-algebra",
    "1106.4785": "dynamical-locality-and-covariance",
    "1109.2794": "entropic-gravity-entropy-postulate-screens-quantum-mechanics",
    "1512.06431": "relative-entropy-equals-bulk-relative-entropy",
    "1602.01380": "entanglement-entropy-excited-states-einstein-equation",
    "1606.09251": "sparc-mass-models-for-175-disk-galaxies",
    "1607.03901": "operator-algebra-quantum-error-correction",
    "1612.03034": "first-weak-lensing-test-of-emergent-gravity",
    "1805.09234": "minimal-index-and-matrix-dimension-finite-centers",
    "1807.06209": "planck-2018-cosmological-parameters",
    "1908.10824": "almost-hermitian-structures-on-tangent-bundles",
    "1909.01906": "relative-entropy-and-subalgebra-index",
    "1910.12106": "ehlers-newtonian-limit",
    "2008.04810": "holographic-map-as-conditional-expectation",
    "2102.04486": "globular-cluster-age",
    "2106.11677": "kids-1000-weak-lensing-radial-acceleration-relation",
    "2110.00483": "bicep-keck-2018-primordial-gravitational-waves",
    "2401.00707": "smacs-j0723-test-of-emergent-gravity",
    "2503.14738": "desi-dr2-results-ii",
    "2504.15336": "on-desi-dr2-exclusion-of-lambda-cdm",
    "2607.27410": "desi-dr2-results-iv",
    "2608.00222": "counterexamples-to-the-jacobian-conjecture",
    "2503.14452": "act-dr6-power-spectra-likelihoods-lambda-cdm",
    "gr-qc/0103074": "local-wick-polynomials-and-time-ordered-products",
    "gr-qc/0111108": "existence-of-local-covariant-time-ordered-products",
    "hep-th/0002230": "holographic-renormalization",
    "math-ph/0006030": "uniqueness-of-chentsov-metric-quantum-information-geometry",
    "math-ph/9808016": "monotone-riemannian-metrics-and-relative-entropy",
    "math-ph/9903028": "microlocal-analysis-and-interacting-qft",
}

MANUAL_ID_BY_PATH = {
    "conformal-time/sources/1995-ma-bertschinger-cosmological-perturbation-theory.pdf": "astro-ph/9506072",
    "misner-log-time/sources/1994-misner-mixmaster-cosmological-metrics-arxiv-source.tar.gz": "gr-qc/9405068",
    "misner-log-time/sources/1994-misner-mixmaster-cosmological-metrics-arxiv-source/9405068.tex": "gr-qc/9405068",
    "misner-log-time/sources/2017-agostini-cianfrani-montani-bianchi-i-internal-time.pdf": "1704.08502",
    "_inq/arxiv-2002-03318/paper.tex": "2002.03318",
}

# Local articles without arXiv identifiers.  Abstracts and exact metadata are
# supplied separately during wrapper generation after source-page verification.
MANUAL_KEY_BY_PATH = {
    "causal-wall-spectral-theory/sources/papers/1973-araki-relative-hamiltonian-faithful-normal-states.pdf": "doi:10.2977/prims/1195192744",
    "causal-wall-spectral-theory/sources/papers/1976-araki-relative-entropy-von-neumann-algebras-i.pdf": "doi:10.2977/prims/1195191148",
    "causal-wall-spectral-theory/sources/papers/1977-araki-relative-entropy-von-neumann-algebras-ii.pdf": "doi:10.2977/prims/1195190105",
    "causal-wall-spectral-theory/sources/papers/1988-mukhanov-gauge-invariant-cosmological-perturbations.pdf": "journal:mukhanov-1988-gauge-invariant-perturbations",
    "causal-wall-spectral-theory/sources/papers/1995-petz-sudar-geometries-quantum-states-substitute.pdf": "preprint:esi-204",
    "conformal-time/sources/1956-rindler-visual-horizons-in-world-models.pdf": "doi:10.1093/mnras/116.6.662",
    "conformal-time/sources/1963-penrose-asymptotic-properties-fields-spacetimes.pdf": "doi:10.1103/PhysRevLett.10.66",
    "conformal-time/sources/1969-parker-quantized-fields-particle-creation-i.pdf": "doi:10.1103/PhysRev.183.1057",
    "deriving-value-of-g/sources/papers/ssrn-6093146-paquet-fine-structure-constant-first-principles.pdf": "doi:10.2139/ssrn.6093146",
    "misner-log-time/sources/1969-misner-mixmaster-universe.pdf": "doi:10.1103/PhysRevLett.22.1071",
    "misner-log-time/sources/1969-misner-quantum-cosmology-i.pdf": "doi:10.1103/PhysRev.186.1319",
}

ARXIV_URL_RE = re.compile(
    r"https?://(?:export\.)?arxiv\.org/(?:abs|pdf|e-print)/"
    r"(?P<id>(?:[a-z-]+/)?\d{4}\.\d{4,5}(?:v\d+)?|(?:[a-z-]+/)?\d{7}(?:v\d+)?)",
    re.IGNORECASE,
)
NEW_ID_RE = re.compile(r"^(?P<id>\d{4}\.\d{4,5})(?P<version>v\d+)?(?:-|$)")
OLD_ID_RE = re.compile(
    r"^(?P<category>astro-ph|gr-qc|hep-th|hep-lat|math-ph|funct-an|dg-ga|math)-"
    r"(?P<number>\d{7})(?P<version>v\d+)?(?:-|$)"
)
COMPACT_OLD_RE = re.compile(r"^(?P<number>\d{7})(?:-|$)")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_arxiv_id(identifier: str) -> tuple[str, str | None]:
    identifier = identifier.removesuffix(".pdf")
    match = re.fullmatch(r"(.+?)(v\d+)?", identifier)
    assert match
    return match.group(1), match.group(2)


def url_id_index() -> dict[str, set[str]]:
    by_compact: dict[str, set[str]] = defaultdict(set)
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for match in ARXIV_URL_RE.finditer(text):
            identifier, _ = normalize_arxiv_id(match.group("id"))
            by_compact[identifier.rsplit("/", 1)[-1]].add(identifier)
    return by_compact


def identify(path: Path, compact_index: dict[str, set[str]]) -> tuple[str, str | None]:
    relative = rel(path)
    if relative.startswith("_inq/arxiv-2002-03318/source/"):
        return "2002.03318", None
    if relative.startswith("misner-log-time/sources/1994-misner-mixmaster-cosmological-metrics-arxiv-source/"):
        return "gr-qc/9405068", None
    if relative in MANUAL_ID_BY_PATH:
        return MANUAL_ID_BY_PATH[relative], None
    if relative in MANUAL_KEY_BY_PATH:
        return MANUAL_KEY_BY_PATH[relative], None

    name = path.name
    match = NEW_ID_RE.match(name)
    if match:
        return match.group("id"), match.group("version")
    match = OLD_ID_RE.match(name)
    if match:
        return f"{match.group('category')}/{match.group('number')}", match.group("version")
    match = COMPACT_OLD_RE.match(name)
    if match:
        candidates = compact_index.get(match.group("number"), set())
        if len(candidates) == 1:
            return next(iter(candidates)), None
        raise ValueError(f"Ambiguous old-style arXiv identity for {relative}: {sorted(candidates)}")
    raise ValueError(f"No article identity rule for {relative}")


def collect_assets() -> list[dict[str, object]]:
    compact_index = url_id_index()
    paths: set[Path] = set()
    for pattern in ARTICLE_GLOBS:
        paths.update(ROOT.glob(pattern))
    records: list[dict[str, object]] = []
    for path in sorted(p for p in paths if p.is_file()):
        identity, version = identify(path, compact_index)
        records.append(
            {
                "identity": identity,
                "version": version,
                "path": rel(path),
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
                "managed_dependency": "arxiv-2002-03318" in path.parts,
            }
        )
    return records


def parse_atom(content: bytes) -> dict[str, dict[str, object]]:
    root = ET.fromstring(content)
    atom = "{http://www.w3.org/2005/Atom}"
    arxiv = "{http://arxiv.org/schemas/atom}"
    result: dict[str, dict[str, object]] = {}
    for entry in root.findall(f"{atom}entry"):
        entry_id = entry.findtext(f"{atom}id") or ""
        raw_id = entry_id.split("/abs/", 1)[-1]
        if raw_id == "Error" or "api/errors" in (entry.findtext(f"{atom}id") or ""):
            continue
        identity, version = normalize_arxiv_id(raw_id)
        authors = [
            author.findtext(f"{atom}name") or ""
            for author in entry.findall(f"{atom}author")
        ]
        categories = [category.attrib.get("term", "") for category in entry.findall(f"{atom}category")]
        result[identity] = {
            "identity": identity,
            "version": version,
            "title": " ".join((entry.findtext(f"{atom}title") or "").split()),
            "abstract": " ".join((entry.findtext(f"{atom}summary") or "").split()),
            "authors": authors,
            "published": entry.findtext(f"{atom}published"),
            "updated": entry.findtext(f"{atom}updated"),
            "categories": categories,
            "primary_category": (
                entry.find(f"{arxiv}primary_category").attrib.get("term")
                if entry.find(f"{arxiv}primary_category") is not None
                else None
            ),
            "doi": entry.findtext(f"{arxiv}doi"),
            "journal_reference": entry.findtext(f"{arxiv}journal_ref"),
            "comment": entry.findtext(f"{arxiv}comment"),
            "record_url": f"https://arxiv.org/abs/{identity}",
        }
    return result


def fetch_arxiv(identities: list[str]) -> dict[str, dict[str, object]]:
    result: dict[str, dict[str, object]] = {}
    for start in range(0, len(identities), 25):
        batch = identities[start : start + 25]
        query = urllib.parse.urlencode({"id_list": ",".join(batch), "max_results": len(batch)})
        url = f"https://export.arxiv.org/api/query?{query}"
        request = urllib.request.Request(url, headers={"User-Agent": "physics-source-library-audit/1.0"})
        with urllib.request.urlopen(request, timeout=60) as response:
            result.update(parse_atom(response.read()))
        if start + 25 < len(identities):
            time.sleep(3.2)
    return result


def slugify(title: str) -> str:
    text = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode("ascii")
    text = text.replace("&", " and ")
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text


def build_manifest(fetch: bool) -> dict[str, object]:
    assets = collect_assets()
    identities = sorted(
        {
            str(record["identity"])
            for record in assets
            if not str(record["identity"]).startswith(("doi:", "journal:", "preprint:"))
        }
        | set(REPEATED_URL_ONLY_IDS)
    )

    metadata_path = AUDIT_DIR / "arxiv-metadata.json"
    if fetch:
        metadata = fetch_arxiv(identities)
        metadata_path.write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    elif metadata_path.exists():
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    else:
        metadata = {}

    by_identity: dict[str, list[dict[str, object]]] = defaultdict(list)
    for record in assets:
        by_identity[str(record["identity"])].append(record)
    for identity in REPEATED_URL_ONLY_IDS:
        by_identity.setdefault(identity, [])

    articles: list[dict[str, object]] = []
    for identity in sorted(by_identity):
        meta = metadata.get(identity, {})
        module = MODULE_OVERRIDE_BY_ID.get(identity)
        if not module and meta.get("title"):
            module = slugify(str(meta["title"]))
        assets_for_article = by_identity[identity]
        for asset in assets_for_article:
            if asset.get("version"):
                asset["asset_role"] = f"historical_{asset['version']}"
            elif meta.get("version"):
                asset["asset_role"] = f"current_{meta['version']}"
            else:
                asset["asset_role"] = "canonical_local_artifact"
        articles.append(
            {
                "identity": identity,
                "module": module,
                "existing_module": identity in EXISTING_MODULE_BY_ID,
                "metadata": meta,
                "assets": assets_for_article,
            }
        )

    hashes: dict[str, list[str]] = defaultdict(list)
    for record in assets:
        hashes[str(record["sha256"])].append(str(record["path"]))
    duplicate_hashes = {
        digest: paths for digest, paths in sorted(hashes.items()) if len(paths) > 1
    }
    missing_metadata = [
        identity
        for identity in identities
        if identity not in metadata
    ]
    return {
        "generated_for": "2026-08-26 source-library audit",
        "article_count": len(articles),
        "asset_count": len(assets),
        "duplicate_hash_groups": duplicate_hashes,
        "missing_arxiv_metadata": missing_metadata,
        "manual_metadata_required": [
            article["identity"] for article in articles if not article["metadata"]
        ],
        "existing_library_overlaps": {
            "arxiv": EXISTING_MODULE_BY_ID,
        },
        "articles": articles,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fetch", action="store_true", help="refresh metadata from the official arXiv API")
    args = parser.parse_args()
    manifest = build_manifest(fetch=args.fetch)
    path = AUDIT_DIR / "manifest.json"
    path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(
        json.dumps(
            {
                "article_count": manifest["article_count"],
                "asset_count": manifest["asset_count"],
                "duplicate_hash_group_count": len(manifest["duplicate_hash_groups"]),
                "missing_arxiv_metadata": manifest["missing_arxiv_metadata"],
                "manifest": rel(path),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
