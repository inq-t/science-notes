# Synthesis Plan

The target is one versionless module whose leaves have a single owner per statement, carrying the generalized $(\nu,\mathfrak R_c)$ family as canon and the unit values as a named branch. This note gives the target map, the note-by-note resolution of the places where v7 and v8 disagree, the three abstractions worth lifting that exist nowhere today, and a staged migration in which nothing irreversible happens before the target shape is legible.

## Target module map

```
causal-scale-theory/
  entry.md                     master synthesis, versionless, ordered
  closure-stack.md             the load-bearing sequence and its failure localization
  causal-order.md              ─┐
  scale-tractor.md              │
  flrw-kinematics.md            │  exact / standard leaves,
  modular-flow.md               │  migrated unchanged in content
  binary-geometry.md            │  from causal-scale-master
  scale-soldering.md            │
  witten-pair.md               ─┘
  scale-capacity.md            the amplitude principle, stated generally
  free-energy-source.md        the constitutive law, with the counterexample
  horizon-and-residual.md      horizon clock + two temperatures + residual sectors
  generalized-background.md    the (ν, 𝔯_c) family, root atlas, branch declaration
  unit-branch.md               the ν = 𝔯_c = 1 evaluation and its benchmark
  no-go-register.md            computed negatives                          ← new
  observables.md               tests, with the statistical power of each   ← new
  conjecture-ledger.md         bold routes with upgrade and kill criteria
  archive.md                   pointers and hashes to the five generations ← new
  receipts/                    suite, contract, machine-readable outputs
  quarantine.md                live tensions
```

Three structural decisions are embedded there.

**`self-dual-response` and `generalized-background` are one note at two specializations.** [[causal-scale-master/self-dual-response|v7's note]] is precisely [[causal-scale-master-v8/generalized-background|v8's note]] evaluated at $\nu=\mathfrak R_c=1$. Keeping both is keeping a function and one of its values as sibling definitions. The general note is canon; `unit-branch.md` holds the evaluation, the benchmark table, and the crossing date — which is solution data fixed by present flatness, not a constant of the theory.

**`horizon-clock` and `horizon-and-vacuum` merge.** [[causal-scale-master/horizon-clock|v7's]] allocation identity and [[causal-scale-master-v8/horizon-and-vacuum|v8's]] signed-index and two-temperature discussion are the same subject, and the v8 note currently re-derives the allocation to get to its new content. One note, with the allocation stated once.

**`wall-state-construction` mostly evaporates.** Its general content is now [[wall-construction-interface/entry|the shared interface]]. What remains theory-side is the two return values the construction must produce and the upgrade criteria for promoting the binary sector; that fits in `closure-stack.md` and does not need a note.

## Harmonization: where v7 and v8 disagree

Resolutions below are per statement. "v8" as a resolution means the v8 statement is correct and the v7 leaf needs amending, which for exact-algebra leaves is flagged as requiring explicit approval.

| Statement | v7 leaf | v8 note | Resolution |
|---|---|---|---|
| Reflection operator on $Q$ | $J_{\mathrm{mod}}QJ_{\mathrm{mod}}=-Q$ in [[causal-scale-master/binary-geometry]] | geometric $J_{\rm refl}$; Tomita identification incompatible with factoriality for noncentral $Q$ | **v8.** Edit to an exact-algebra leaf — needs approval. The argument and the two available realizations are in [[wall-construction-interface/binary-channel]]; the unresolved choice between them is [[quarantine]]. |
| Soldering slope | $\varrho_\perp=1$ hardwired | $\nu:=\lvert\varrho_\perp\rvert$, orientation-independent | **v8.** The canon carries $\nu$; orientation reversal sends $Q\mapsto-Q$ and $\varrho_\perp\mapsto-\varrho_\perp$, so only the magnitude is physical. |
| Amplitude | $\mathfrak R_c=1$ | family $0<\mathfrak R_c<2$, with $\mathfrak R_c=1$ the equal-partition point | **v8.** |
| Shape invariant | $=4$ | $=4\nu^2$ | **v8**, with the unit value in `unit-branch.md`. |
| Riccati flow | "limiting fixed points" | hyperbolic; $\tanh$ is a heteroclinic orbit modulo translation | **consistent already**; v8's wording is more precise. Both are right that G4's saddle-node branding is wrong. |
| Horizon index | signed-vs-magnitude distinction present in [[causal-scale-master/flrw-kinematics]] and [[causal-scale-master/horizon-clock]] | same distinction | **consistent**; consolidate into one statement rather than three. |
| Horizontal temperature | [[causal-scale-master/hawking-friedmann]] warns against interchanging | $T_{\rm KH}=\mu_Ak_BT_{\rm hor}$, tagged open | **consistent**; v8 supplies the relation. *Why* the horizontal channel uses $T_{\rm hor}$ is [[quarantine]]. |
| Density maximum and $w=-1$ | equality stated | notes $\rho_X'=0\Leftrightarrow w_X=-1$ is generic for any positive separately conserved component | **v8's sharpening enters the canon.** The non-trivial content is coincidence with self-duality and, at $\mathfrak R_c=1$, with equal partition. |
| Acceleration exit | competition of dilution rates | ordinary active mass overtakes a decaying negative response; $1+3w_X<0$ at every finite $x$ | **consistent**; v8 and G4's Komar account agree and are more mechanical. |
| Flatness root structure | absent | full atlas: radiation double root at $\nu\simeq1.5584$, three roots up to $\simeq1.8147$, high-redshift root to $\nu<2$ | **v8 only.** Independently reconfirmed; the true existence bound is $\nu=2$, set by the radiation exponent and independent of $\Omega_m$. |
| Free-energy step | constitutive definition | "physical choice" | **neither — the autopsy layer wins.** See below. |

Two statements where [[scale-as-modular-observable/claim-audit|the claim audit]] is stronger than both:

**The free-energy substitution is an identified error, not a labelled choice.** The monograph replaces the fixed-reference difference $F_c(\omega_{N+\mathrm dN})-F_c(\omega_N)$ with the neighbouring-state expansion $\tfrac12G_{NN}\mathrm dN^2$. The former generically carries a term linear in $\mathrm dN$, and the audit exhibits it: in the balanced binary family with $\omega_c=\omega_0$,

$$
S(\omega_\theta\Vert\omega_0)=\theta\tanh\theta-\ln\cosh\theta,
\qquad
\frac{\mathrm d}{\mathrm d\theta}S(\omega_\theta\Vert\omega_0)=\theta\operatorname{sech}^2\theta\neq0 .
$$

That belongs in `free-energy-source.md`, replacing the weaker framing.

**The modular-rescaling direction is demonstrably not the $Q$ direction.** In the same family,

$$
\operatorname{Var}_{\omega_\theta}(-\ln\omega_\theta)=\theta^2\operatorname{sech}^2\theta,
\qquad\text{whereas}\qquad
G^{\rm BKM}_{\theta\theta}=\operatorname{sech}^2\theta,
$$

so at $\theta=0$ the first vanishes and the second is one. This is the crispest available refutation of identifying the scale tangent with a temperature rescaling, and v8 has no equivalent. It belongs in [[wall-construction-interface/cross-fiber-transport|cross-fiber transport]], since it constrains what the horizontal tangent can be.

## Three abstractions worth lifting

**A no-go register.** Computed negative results are the archive's least-decaying content and its most scattered: four in G4, four generic ones in [[causal-scale-master-v8/perturbation-and-qft-interface|v8's perturbation note]], and one live only inside a receipt script. They are the regression tests of the theory — each permanently closes a design direction — and they deserve a note that states, per entry, the claim excluded, the computation, and the scope of the exclusion. [[salvage-ledger|The salvage ledger]] lists the recoverable ones.

**Observables with their power.** The present tests ledger states what each test would falsify but not whether it can be performed. At least one cannot: the shape invariant is unmeasurable with background data for structural reasons, since the data span less than one transition width and the shape exponent controls the tails where the response is subdominant. A test ledger that omits power invites exactly the misordering [[causal-scale-master-v8/observational-programme|the observational programme]] currently commits by ranking that test first. Every row should carry an assumption set, a failure condition, *and* a power statement.

**The claim-label vocabulary belongs outside this module.** Fourteen labels with a dash-qualifier convention are defined inside v8's entry note, while [[causal-wall-spectral-theory/claim-audit|the spectral programme]], [[scale-as-modular-observable/entry|the autopsy layer]], and [[least-action/entry|least-action]] each maintain a compatible-but-different informal vocabulary. My recommendation is a small top-level `epistemic-labels` module rather than a note under [[cosmodynamics/entry|cosmodynamics]]: the taxonomy is vault infrastructure, and cosmodynamics is a content module that should consume it like everything else. [[cosmodynamics/registers-and-type-discipline|Type discipline]] is the closest existing relative and should link to it rather than absorb it.

## Migration stages

Ordered so that reversibility decreases monotonically. Do not begin a stage before the previous one has been read.

**Stage 0 — this plan.** No file outside this module changes.

**Stage 1 — additive only.** Write `no-go-register.md`, `observables.md`, and `archive.md` here, from the sources in [[salvage-ledger|the salvage ledger]]. These duplicate nothing, because none of them exists anywhere. Also write the receipt contract from [[receipts-plan|the receipts plan]]. Nothing moves; nothing is deleted; every existing module still reads exactly as it does now.

**Stage 2 — adopt the shared interface.** Execute the trim already specified in [[wall-construction-interface/duplication-audit|the duplication audit]], replacing the duplicated interface preamble in [[causal-scale-master-v8/wall-state-construction|wall-state-construction]] and [[causal-wall-spectral-theory/causal-scale-interface|the spectral interface note]] with links. This is the first stage that edits other modules, and it only removes text that is preserved verbatim elsewhere.

**Stage 3 — move the leaves.** Migrate the seven exact/standard leaves of [[causal-scale-master/entry|causal-scale-master]] into this module with their content unchanged, merge `self-dual-response` into `unit-branch.md`, and merge `horizon-clock` with v8's `horizon-and-vacuum` into `horizon-and-residual.md`. Rewrite `entry.md` as the ordered synthesis. Use `git mv` so history follows the files. `causal-scale-master/` retains only `latest/` — the raw v7 artifacts — and becomes an archive folder referenced from `archive.md`.

**Stage 4 — retire the v8 module.** Fold `closure-stack`, `generalized-background`, and `conjecture-ledger` into the canon; distribute `observational-programme` between `observables.md` and the receipt contract; keep [[causal-scale-master-v8/revision-audit|revision-audit]] as a permanent provenance record and move it to `archive.md`'s neighbourhood rather than deleting it. The inbox proposal stays untouched in the inbox, as it is the hashed object the audit refers to.

**Stage 5 — the receipt suite.** Build one suite under `receipts/` against the contract, porting the checks worth porting and marking every check independent or regression. Add `"**/*.py"` to this module's `inq.toml` include list when it lands.

The one edit outside this sequence is the reflection-operator amendment to [[causal-scale-master/binary-geometry|binary-geometry]]. It is small, it is a correction rather than a reorganization, and it touches a note whose whole value is that its algebra is exact — so it should be done deliberately and on its own, at whatever point you want it, not folded into a stage.

## What I would not do

Do not write a sixth synthesis document to supersede the five. The archive's characteristic failure is that each generation restated its predecessor's premises to stand alone, and the restatements drifted apart; another self-contained monograph would be the sixth instance of the disease rather than its cure.

Do not delete the autopsy layer, and do not delete `chats/`. The first is upstream of the repair and the second is the only record of when each claim was promoted, which is what made the promotions findable.

Do not resolve the quarantined tensions as a side effect of the migration. Each one is a research question with a real answer, and consolidating a note is not the occasion to guess at it.
