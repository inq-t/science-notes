# Retirement Audit of the Causal Scale Masters

The versioned `causal-scale-master` and `causal-scale-master-v8` modules are retired from active ownership after a claim-by-claim comparison with the versionless CST graph. Their exact trees remain local immutable sources. Retirement therefore means that new claims and links belong in `causal-scale-theory`, not that the historical arguments, artifacts, or receipts have been deleted.

## Verdict

The versionless graph is the canonical owner of Causal Scale Theory. It preserves the exact and conditionally useful content of both masters, rejects claims that exceeded their derivations, and delegates interfaces that belong to other modules. The old trees are evidence of intellectual provenance rather than parallel versions of the theory.

## Salvaged into the canonical graph

| Legacy contribution | Canonical disposition |
|---|---|
| The separation of causal order from metric calibration and the tractor transport reformulation | [[causal-scale-theory/causal-order]] and [[causal-scale-theory/scale-tractor]] |
| Balanced binary geometry, its Casimir balance, and the heteroclinic state-space flow | [[causal-scale-theory/balanced-channel-premise]] and [[causal-scale-theory/binary-geometry]] |
| The generalized $(\nu,\mathfrak R_c)$ response, past- and future-crossing branches, fold structure, and future classes | [[causal-scale-theory/response-law]], [[causal-scale-theory/flatness-branches]], and [[causal-scale-theory/future-asymptotics]] |
| The $d$-dimensional crossing law | [[causal-scale-theory/dimensional-horizon-closure]] |
| The past/future threshold $\mathfrak R_c=2(1-\Omega_{m0}-\Omega_{r0})$ on the continuous unit-width branch | [[causal-scale-theory/flatness-branches]] |
| The signed horizon index, temperature distinction, and conditional Hawking--Friedmann conversion | [[causal-scale-theory/horizon-clock]], [[causal-scale-theory/horizontal-temperature]], and [[causal-scale-theory/hawking-friedmann]] |
| The collective, constitutive typing of the state coordinate and the limited role of the relative-entropy Hessian | [[causal-scale-theory/state-variable-typing]], [[causal-scale-theory/relative-entropy-hessian]], and [[causal-scale-theory/free-energy-source]] |
| The exact internal Witten--Darboux factorization, including its zero mode and scattering data, with a guarded covariant-lift conjecture | [[causal-scale-theory/witten-pair]] and [[causal-scale-theory/conjectures/covariant-response-sector]] |
| Local trace-free vacuum blindness together with the missing global scalar completion and counterterm problem | [[causal-scale-theory/vacuum-residual-sector]] and [[causal-scale-theory/conjectures/local-global-vacuum-completion]] |
| Reproducibility requirements, branch declaration, and separation of arithmetic receipts from empirical evidence | [[causal-scale-theory/empirical-status]], [[causal-scale-theory/observables]], and `causal-scale-theory/receipts/` |

## Claims not admitted to the canon

| Legacy claim or inference | Disposition |
|---|---|
| A universal width ceiling near $\nu\simeq1.814$ or at $\nu=2$ | Rejected. The first is a late-branch fold for particular abundances; the second is an asymptotic tail threshold. Finite roots require the full branch equation. |
| Conformal-weight integrality fixes unit width | Rejected by [[causal-scale-theory/no-gos/character-theory-does-not-fix-unit-width]]. Unit width remains a principle unless an independent representation calculation derives it. |
| A two-dimensional normal plane supplies a Cardy or CFT derivation of capacity | Rejected by [[causal-scale-theory/no-gos/normal-plane-is-not-automatically-a-cft]]. The stronger near-horizon algebraic route remains conjectural. |
| Fixed-reference free energy derives the all-history pulse | Rejected by [[causal-scale-theory/no-gos/fixed-reference-free-energy-does-not-give-the-pulse]]. Only the local Hessian is exact; the source law is constitutive. |
| The Witten pair is already the cosmological perturbation operator, fixes signal speed, or fixes a kinetic sign | Rejected. The factorization is internal state-space mathematics until a conserved hyperbolic spacetime lift is constructed. |
| Local central blindness solves the cosmological-constant problem | Rejected. It neither determines the scalar residual nor controls effective-action counterterms or radiative stability. |
| Background agreement constitutes recovery of GR, QFT, or the Standard Model | Rejected. Local physics is imported wherever the descriptions overlap; recovery or reconstruction requires independent results. |
| The proposal's likelihood, posterior, AIC, and perturbation-profile numbers are established results | Withheld because the cited data and analysis package were not present in the reviewed source tree. |

Rejected arguments remain visible in [[causal-scale-theory/no-go-register|the no-go register]] or in their exact legacy context. A rejected derivation does not forbid a stronger construction from reaching a related conclusion.

## Delegated ownership

| Question | Owning module |
|---|---|
| Cross-fiber wall algebra, states, transport, binary reduction, and anti-circularity | [[wall-construction-interface/entry]] |
| Coexistence with, conservative restriction of, recovery of, or derivation of local GR and QFT | [[compatible-with-existing-physics/entry]] |
| Primordial spectral descent and the wall-state/perturbation interface | [[causal-wall-spectral-theory/entry]] |
| Philosophical and group-theoretic interpretation of causal charge | [[conservation-of-causal-charge/entry]] |
| Meaning and possible determination of Newton's constant | [[deriving-value-of-g/entry]] |
| Any reconstruction or selection of gauge and matter symmetry | [[symmetry-groups-select/entry]] |

Delegation is not evidence that these interfaces have been completed. It prevents the CST background module from claiming results whose construction lives elsewhere.

## Receipt disposition

[[causal-scale-theory/sources/legacy/causal-scale-master-v8/receipts/background.py|The historical v8 background receipt]] is retained intact with its source tree. Its 27 checks recompute benchmark algebra and arithmetic: the exact matter-plus-radiation folds, strict-dust and hybrid folds, representative root branches, generalized-amplitude past/future cases, and the unit benchmark. They do not test the physical principles, wall construction, covariant perturbations, likelihoods, or QFT recovery.

The active receipt suite under `causal-scale-theory/receipts/` is written from the reviewed canonical equations. At retirement, `algebra.py` passes 17/17 declared checks and `background.py` passes 41/41. Machine agreement promotes unchecked arithmetic to checked arithmetic only; it does not promote a premise, identification, or constitutive law to a theorem.

## Exact-tree preservation

The complete pre-retirement trees are preserved at [[causal-scale-theory/sources/legacy/causal-scale-master/entry|the v7 legacy root]] and [[causal-scale-theory/sources/legacy/causal-scale-master-v8/entry|the v8 legacy root]]. They preserve every file that was present rather than a curated subset. The original v7 ZIP remains provenance; `causal-scale-theory/sources/legacy/unpacked-v7-package/` is a convenience mirror of its 65 locally reviewable entries. No chats were observed in that ZIP.

[[causal-scale-theory/archive|The source archive]] records SHA-256 fingerprints for selected reviewed files. Those hashes verify that a present file matches the reviewed bytes; they cannot reconstruct an absent tree. Git commit `8eef728d80704f6529150afab6e086c5ce58212c` identifies the repository immediately before retirement and supplies the independent version-control provenance for the exact old layout.

Retirement is active: the two versioned modules are no longer workspace members, historical references in this planning packet point into `causal-scale-theory/sources/legacy/`, and new work belongs in the versionless graph.
