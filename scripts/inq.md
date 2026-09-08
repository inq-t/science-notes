---
inq.module: workspace-note-maintenance
inq.include:
  - './'
inq.ambient:
  - '*.py'
  - 'refactors/*.json'
keywords: [wikilinks, provenance, refactoring, knowledge-graph]
---
# Maintaining the Modular Research Workspace

Explicit file relocations can preserve the research graph without rewriting its mathematical content. The maintenance tools separate a reviewed ownership map, mechanical link updates, and verification of frozen historical records; module boundaries and synthesis prose remain editorial decisions.

The [[scripts/relocate-notes.py|relocation tool]] consumes an explicit old-to-new path manifest. Its default is a dry run; `--apply` moves only the named files, rebases resolvable links in active Markdown, and records hashes. Inbox, chat, research-run and junk-drawer records remain unchanged. Protected working-tree files cause a refusal if a necessary rewrite would touch them. [[scripts/test-relocate-notes.py|The tests]] exercise source-relative links, incoming references, anchors, multiline labels and ambiguity. This tool is not a complete Markdown parser or a replacement for inspecting the resulting diff and running Inq's own checks.

The [[scripts/refactors/2026-09-08-yang-mills.json|Yang–Mills extraction ledger]] records the ownership decisions for the first refactoring batch. Its [[scripts/refactors/2026-09-08-yang-mills.receipt.json|execution receipt]] records original and resulting hashes; changed Markdown hashes reflect rebased links, while script and stored-output hashes should remain equal. Old paths inside frozen records can be located through this ledger without rewriting the historical text.

The [[scripts/refactors/2026-09-08-yang-mills-response.json|response extraction ledger]] separates shared projection mathematics, physical coercivity and cosmological scale-selection hypotheses. Its [[scripts/refactors/2026-09-08-yang-mills-response.receipt.json|execution receipt]] verifies the mechanical moves and frozen records. Two incoming links in a pre-edited file are handled separately from the relocation pass so that unrelated wording edits can remain unstaged. These ledgers record moves; later synthesis or proof-deduplication edits are reviewed in the corresponding Git diff.

The [[scripts/audit-module-links.py|module-graph audit]] checks entrypoint existence and keyword hints, resolvable local links, immediate summaries, balanced math delimiters and code fences, and transitive resource reachability from each named entrypoint. It treats frozen records as opaque leaves, excludes code examples from link and math checks, and excludes formulas from link checks. Its [[scripts/test-audit-module-links.py|fixture tests]] cover missing entrypoints, internal closure, resource links and Markdown boundaries. The check establishes paths, not mathematical correctness; title agreement with filenames remains an editorial check. Use it alongside `inq lint`, because neither a file inventory nor an entrypoint-only check proves that supporting resources are actually reachable.

The [[scripts/refactors/2026-09-08-yang-mills-scale-continuum.json|scale and continuum extraction ledger]] separates logistic geometry, incidence response, finite-index distinction and continuum reconstruction, and places the numerical rhyme sweep with its causal-grain diagnostics. Its [[scripts/refactors/2026-09-08-yang-mills-scale-continuum.receipt.json|execution receipt]] records 25 file moves and verifies the frozen Markdown records. Scripts and stored calculations move without content changes; subsequent editorial reductions are visible in Git.

The [[scripts/refactors/2026-09-08-scale-sections.json|scale section map]] extracts the wall-to-Casimir comparison and codimension-two balance. The [[scripts/refactors/2026-09-08-causal-grain-sections.json|causal-grain section map]] separates genealogy, local rulers, acoustic calibration, exceptional descent and the recovery contract. Both retain old heading destinations and identify shared mathematical owners. Their [[scripts/refactors/2026-09-08-section-links.receipt.json|section-link receipt]] records incoming-link repairs and verifies the frozen files, including the original combined-note snapshots.

The earlier [[scripts/migrate-inq-md.py|Inq entrypoint migration]] converted the retired `entry.md` plus module-manifest format to `inq.md`. It is retained for reproducibility of that separate migration, not part of the current relocation operation.

The [[scripts/refactors/2026-09-08-causal-grain-sources.json|causal-grain source ledger]] packages eleven cited inbox records as opaque resources after checking that no byte-identical admitted copies exist. It records the original and packaged paths, byte counts and SHA-256 hashes. The original records remain unchanged; this source packaging does not create additional active accounts of their claims.

The [[scripts/refactors/2026-09-08-yang-mills-neighbor-audit.json|Yang–Mills neighbor audit]] records a bounded traversal from the eleven extracted research modules, with concrete shared-construction and ownership findings. Its line references locate the inspected evidence; its unreviewed frontier identifies work still to examine. A keyword match or this inventory alone does not certify a mathematical claim or justify merging different physical carriers.

The [[scripts/refactors/2026-09-08-measured-response-sections.json|measured-response section map]] assigns the long carrier entry's constructions to focused notes and identifies their earlier headings at the recorded source commit. Its [[scripts/refactors/2026-09-08-measured-response-links.receipt.json|link-repair receipt]] records active heading redirects, frozen-record checks and preservation of equation labels. The associated Git diff records clarification and proof deduplication; neither the map nor label preservation certifies those arguments.
