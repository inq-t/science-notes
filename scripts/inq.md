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

The [[scripts/audit-module-links.py|module-graph audit]] checks resolvable local links, immediate summaries, balanced math delimiters, and transitive resource reachability from each named entrypoint. It treats frozen records as opaque leaves and checks paths rather than claiming mathematical correctness. Use it alongside `inq lint`, because neither a file inventory nor an entrypoint-only check proves that supporting resources are actually reachable.

The earlier [[scripts/migrate-inq-md.py|Inq entrypoint migration]] converted the retired `entry.md` plus module-manifest format to `inq.md`. It is retained for reproducibility of that separate migration, not part of the current relocation operation.
