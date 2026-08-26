# Primary-Source Library Audit, 2026-08-26

This audit centralizes article ownership under `library/`, removes verified duplicate payloads, and redirects mutable canonical notes to one Markdown wrapper per primary source while preserving immutable research history and upstream provenance.

## Scope and identity rules

The audit covered article holdings in the CWST, compatible-physics, conformal-time, deriving-$G$, Misner-time, symmetry-selection, and entropic-gravity source corpora, the generated arXiv dependency for `2002.03318`, and repeatedly cited primary sources that previously had no library owner.

Source identity was resolved in this order:

1. DOI;
2. base arXiv identifier, with versions retained as artifacts of one article module;
3. official repository or preprint identifier;
4. title, authors, year, and payload hash when no stronger identifier exists.

Chats, inbox material, junk drawers, legacy snapshots, and vendored code/data trees were not rewritten. Remote URLs remain in provenance and checksum ledgers; canonical prose now links to the local wrapper. No authored or historical source text was polished in place.

## Results

- 133 primary-source identities were normalized in this pass.
- 131 new article modules were created; 2 existing wrappers were updated because their locally held artifacts moved under their ownership.
- The root library now contains 167 registered modules, including the 36 that predated this audit.
- 181 tracked artifact paths represented 171 unique payloads.
- 9 exact duplicate-hash groups contained 10 redundant copies, all removed only after SHA-256 verification.
- 72 mutable Markdown files were rewritten to use library wrappers or, in provenance contexts, the new canonical artifact paths.
- `library/identities.json` records normalized identities and hashes for all 167 library modules.

The exact duplicate groups were:

| source identity | duplicated payload | redundant copies removed |
|---|---|---:|
| arXiv:1505.04753 | current article PDF in three corpora | 2 |
| arXiv:1505.04753 | current arXiv source archive in two corpora | 1 |
| arXiv:1508.00897 | article PDF in two corpora | 1 |
| arXiv:1505.01492 | article PDF in two corpora | 1 |
| arXiv:0804.2182 | article PDF in two corpora | 1 |
| arXiv:2601.07915 | article PDF in two corpora | 1 |
| arXiv:gr-qc/9504004 | article PDF in two corpora | 1 |
| arXiv:gr-qc/9504004 | arXiv source archive in two corpora | 1 |
| arXiv:2002.03318 | generated `paper.tex` duplicating the source package's main TeX file | 1 |

The distinct v1 PDF and source archive for arXiv:1505.04753 were retained in the same article module as historical-version artifacts; they are not byte duplicates of the current version.

## Wrapper contract

Every wrapper written in this pass has:

- an H1 title followed immediately by the article abstract or a concise editorial synopsis;
- explicit authors and publication year;
- a publication date or first-submission date;
- a journal or other publication record when available;
- DOI, arXiv, or primary-record links;
- the names of locally held primary artifacts, or an explicit statement that none is held.

When an original source has no formal abstract, the wrapper labels its opening paragraph as an editorial synopsis. This applies, for example, to Fisher, Kullback--Leibler, and Dombrowski. Bibliographic distinctions that could otherwise merge separate works were retained: Petz's solo *Monotone Metrics on Matrix Spaces* is not Petz and Sudár's *Geometries of Quantum States*; Satoh's arXiv:1908.10824 is not Dombrowski's 1962 article; and the unattributed singular-titled Ulam.ai Jacobian manuscript is not Gao's plural-titled arXiv:2608.00222.

The pre-existing `algebraic-backgrounds` module remains one wrapper because the held primary object is one arXiv deposit, arXiv:1902.09387, even though its journal reference points to two separately titled published parts. No consumer currently cites either DOI independently; splitting that composite deposit would therefore invent two local payload owners for one held source rather than remove a duplicate.

## Verification

- All 133 migrated wrappers and all 181 original asset references resolve to the expected destination hash.
- All 167 library modules have an H1, an immediate summary paragraph, and a valid broad resource manifest.
- All 152 library PDFs open with a nonempty page tree.
- All 45 local source archives either read as archives or are recognized legacy single-stream arXiv deposits.
- A fresh workspace scan found no remaining exact duplicate PDFs or `.tar.gz` archives among 229 such files.
- Mutable Markdown contains no stale full path to a migrated artifact and no known repeated arXiv/DOI URL without its wrapper outside the dedicated provenance ledgers.
- A changed-note wiki-link scan found no unresolved target introduced by the migration; the remaining reports are pre-existing links or valid extensionless/raw-resource targets outside this audit.
- `inq sync` completed, `inq lint --warn --no-color` is clean, and `git diff --check` is clean.

## Audit receipts

- `manifest.json` is the artifact-and-identity inventory.
- `arxiv-metadata.json` is the cached official arXiv metadata used for wrapper generation.
- `manual-metadata.json` records verified non-arXiv metadata and clearly marked editorial synopses.
- `scan_sources.py` produced the frozen pre-migration inventory; it is retained to document the discovery rules used before the old corpora were emptied.
- `migrate_library.py` records the ownership move, wrapper generation, citation rewrite, registration, and identity-registry procedure and is idempotent against the migrated state.
- `verify_migration.py` reruns the post-migration structural, hash, duplicate-payload, link-target, PDF, archive, and registry checks.
