# Duplication Audit

This ledger records where each statement collected in this module is currently also stated elsewhere, so that a later consolidation can be reviewed statement by statement rather than performed on impression. Nothing in the existing modules has been altered. Until a trim is separately reviewed and applied, this module **restates** rather than replaces, and the existing modules remain the operative text for their own programmes.

## Provenance of the extracted statements

| Statement | Canonical location here | Currently also stated in |
|---|---|---|
| The scale-indexed package as a tuple of regions, algebras, states, modular data, transport, scale law, cocycle, and generator | [[entry]] | `causal-wall-spectral-theory/causal-scale-interface.md` (7-tuple, fullest); `causal-scale-master-v8/wall-state-construction.md` (5-tuple with modular data); `scale-as-modular-observable/observable-map.md` ($\Phi$ alone) |
| A derivative of the state family is undefined before transport | [[cross-fiber-transport]] | `causal-scale-master-v8/wall-state-construction.md`; `causal-wall-spectral-theory/causal-scale-interface.md` (as the "common-algebra clause") |
| The four transport strategies | [[cross-fiber-transport]] | `causal-scale-master-v8/wall-state-construction.md` |
| Vertical/horizontal type distinction | *not extracted* — canonical in `causal-scale-master/modular-flow.md` | recapped in `causal-scale-master-v8/wall-state-construction.md`, `causal-wall-spectral-theory/causal-scale-interface.md`, `scale-as-modular-observable/observable-map.md` |
| Three-term decomposition of the modular change, only the middle term load-bearing | [[cross-fiber-transport]] (as an obligation) | derivation in `causal-scale-master/modular-flow.md`; restated in `causal-scale-master-v8/wall-state-construction.md` |
| Geometric reflection is not Tomita conjugation; factoriality obstruction; doubled $Q_L,Q_R$ realization | [[binary-channel]] | `causal-scale-master-v8/wall-state-construction.md` (full); `causal-scale-master-v8/entry.md` (one line) |
| The channel $\mathcal E_N$ and its non-interchangeable readings | [[binary-channel]] | `causal-scale-master-v8/wall-state-construction.md` |
| Balance is an additional premise, not a normalization | [[binary-channel]] | `causal-scale-master-v8/wall-state-construction.md`; `causal-scale-master-v8/entry.md` |
| Cocycle form, multiplicative Cauchy equation, affinity without slope | [[cross-fiber-transport]] (as an obligation) | theorem in `causal-scale-master/scale-soldering.md`; restated in `causal-scale-master-v8/wall-state-construction.md`, `causal-scale-master-v8/entry.md`, `scale-as-modular-observable/observable-map.md` |
| Cocycle failure modes | [[cross-fiber-transport]] | `causal-scale-master-v8/wall-state-construction.md` |
| State selection is substantive; no covariantly preferred state | [[cross-fiber-transport]] | `causal-wall-spectral-theory/causal-scale-interface.md`; `causal-wall-spectral-theory/open-problems.md` (CW–T1b) |
| Independence / anti-circularity test | [[elimination-test]] | `causal-scale-master-v8/entry.md`; `causal-scale-master-v8/wall-state-construction.md` (with the region trap); `causal-wall-spectral-theory/causal-scale-interface.md`; `scale-as-modular-observable/observable-map.md`; `causal-wall-spectral-theory/open-problems.md` (CW–T1c) |
| Conservative-restriction test | [[elimination-test]] | `causal-wall-spectral-theory/causal-scale-interface.md`; `causal-scale-master-v8/perturbation-and-qft-interface.md`; `causal-wall-spectral-theory/open-problems.md` (CW–T6) |
| Two completion levels | [[entry]] | `causal-wall-spectral-theory/causal-scale-interface.md`; comparable three-level version in `causal-wall-spectral-theory/open-problems.md` |
| The five-rung ladder | [[construction-ladder]] | `causal-scale-master-v8/wall-state-construction.md` |
| Literature precedents for individual slots | [[construction-ladder]], [[cross-fiber-transport]] | `causal-wall-spectral-theory/causal-scale-interface.md` |

## Findings worth acting on separately

**The ladder and its citations are in different modules.** `causal-scale-master-v8/wall-state-construction.md` states the five rungs with no literature anchors; `causal-wall-spectral-theory/causal-scale-interface.md` supplies exactly the precedents those rungs need, with no ladder. Neither cross-references the other. Of everything in this audit, this is the clearest case where the duplication is actively costing content rather than merely repeating it: the v8 programme is missing five relevant constructions that the sibling module already has on disk.

**A sharp regularity point is stranded.** The observation that sigma-weak continuity of $u_t$ in the cocycle parameter does not establish measurability with respect to the external scale ratio appears only in `scale-as-modular-observable/observable-map.md` — the module whose status is least settled. It is preserved in [[cross-fiber-transport]] so that it does not depend on that module's fate.

**A known divergence between v7 and v8, left in place.** `causal-scale-master/binary-geometry.md` writes the reflection relation with a modular conjugation, $J_{\rm mod}QJ_{\rm mod}=-Q$, while `causal-scale-master-v8/wall-state-construction.md` argues that this identification is incompatible with factoriality for a single noncentral $Q$ and that the operator must be a geometric reflection $J_{\rm refl}$. The two statements are in tension. **No edit has been made.** Resolving it touches an exact-algebra leaf note and should be a deliberate, separately reviewed change; [[binary-channel]] records the argument and the two available realizations without asserting which the v7 leaf intended.

**CWST duplicates itself.** The "three rank-one claims" table in `causal-wall-spectral-theory/causal-scale-interface.md` and the "rank one is under-specified" section of `causal-wall-spectral-theory/claim-audit.md` state the same content. Only the first of the three claims is an obligation of this interface; the other two are consumer-side. This is internal to CWST and outside the scope of the present extraction.

**A live cross-dependency on an unsettled module.** `causal-scale-master-v8/wall-state-construction.md` links to `scale-as-modular-observable/observable-map.md` for its general observable-map requirements. Whatever is eventually decided about the status of `scale-as-modular-observable`, that decision now has a consumer and cannot be treated as purely cosmetic.

## Open architectural question

Two notes in this module cite primary sources by paths inside `causal-wall-spectral-theory/sources/papers/`. A shared dependency reaching into one particular consumer's source library is backwards: if the library is vault-wide infrastructure, it belongs at top level; if it is CWST's own working bibliography, this module should carry its own provenance ledger instead. The links are correct as written today and are left that way. Given the size of what lives under that directory, moving it is a decision on its own, not a side effect of this extraction.

## What a later trim would do

For the record, and not as an instruction: the trim would replace each duplicated section listed above with a single link, leaving `causal-scale-master-v8/wall-state-construction.md` holding only the two return values and its own upgrade criteria, and `causal-wall-spectral-theory/causal-scale-interface.md` holding only the three-objects table, the consumer-side rank-one claims, and its claim-status verdict. Neither file would lose a statement that is not preserved here. That change is deferred pending review of this module.
