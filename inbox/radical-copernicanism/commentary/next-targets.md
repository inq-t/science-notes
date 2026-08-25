# Next Targets and Guardrails

The theorem-shaped work that falls out of this folder, ordered by leverage.

## T1 — The gating question: is the wall family a chain of half-sided modular inclusions?

Every module this folder touches converges on this single structural question.

- `../modular-theory-inventory.md` (Employment Risk 1.5): operator-valued weights along inclusions exist iff some weight's modular flow preserves the subalgebra — generically false for type III₁ local inclusions, *except* in the half-sided modular case, where Wiesbrock/Araki–Zsidó supply a canonical compression semigroup and a genuine operator-valued weight.
- `../algebra-of-causality.md`: a totally ordered nested family of horizon algebras is exactly a chain of half-sided modular inclusions / one-dimensional Borchers triples, and that is where the causal content (positive semigroup + modular positivity) survives while the lattice trivializes.
- [[sufficient-reason/theorem-programme|Target C4]]: the half-sided modular inclusion is the named rigorous candidate for the arrow bridge.
- `../stack-of-weight-groupoids.md` (benchmark ii): proving the inclusions half-sided restores core-functoriality and hence the descent lemma on the chain.

One yes/no question gates cross-fiber transport for [[wall-construction-interface/entry|the wall interface]], the arrow bridge, the causal semigroup, and the costack lemma restricted to the chain. The diagnostic is already written: check whether $\Delta^{it}_{M_{N'}} M_N \Delta^{-it}_{M_{N'}} \subseteq M_N$ for one sign of $t$. Attack this before the grand descent theorem.

## T2 — The telescoping flux-balance along the chain

Formulate and prove the cosmological Clausius identity: the relative-entropy decrements $S(\omega_N \Vert \sigma_N)$ against the reference weight telescope along inclusions of the wall chain. Machinery on hand: Uhlmann monotonicity (data processing) plus, given T1, the h.s.m.i. transport. This would be the first *equality-shaped* global ledger statement (the GSL only gives the inequality), and it uses the inventory's own workhorse recommendation.

## T3 — Recast synchronization as a fixed point

The balanced reference ρ₀ = 𝟙/2 is the normalized trace of the binary channel, so the crossing is the cut where the channel coincides with its own trace (see `retyped-conservation.md`). Restate [[causal-scale-theory/conjectures/self-dual-synchronization|the synchronization conjecture]]'s first gate as: *the wall moduli object has a unique cut at which the physical channel sits at its own tracial state, and the capacity, density, and w = −1 loci are consequences of that coincidence.* This turns a coordination of seven events into one fixed-point statement plus derivations — a cleaner theorem target and a cleaner failure mode.

## T4 — The ε ≠ 0 dominant-weight GAP as an external contribution

The 2022–2026 crossed-product literature (Witten; CLPW; Chen–Penington; KFLS; Speranza; De Vuyst–Eccles–Höhn–Kirklin) is a live mainstream frontier, and CST's ε ≠ 0 case sits exactly on its declared gap: no exact KMS/dominant weight off equilibrium, only the physical-clock workaround. An "approximately dominant weights with error bounds" theorem is simultaneously the inventory's GAP, a publishable external result, and CST's ε-flow in their language. The wall programme is no longer isolated on this front; this is the natural point of contact.

## T5 — The costack ligament, only when the base widens

The genuinely new theorem in `../stack-of-weight-groupoids.md` — descent for O ↦ core(M(O)) over the causal site with modular coefficients — pays off only beyond the chain, on genuine covers with spacelike overlaps, where Casini's lattice and Haag duality reactivate. On the chain, base cohomology is trivial and all invariant content is fibre-direction. Decide explicitly whether the programme needs the 2+ dimensional site now; do not pay for it earlier. Read Elliott (2021) in full before any novelty claim.

## Audit item — the vertical/horizontal solder

The inventory's dictionary entry mapping CST's capacity flow dC/dN = 2εC to the trace-scaling module is the one ungraded cross-type identification in an otherwise fastidious document. Per GR5/GR6 discipline it is a GLOSS requiring its own soldering theorem, and the escort-tangent no-go is the precedent for how such identifications fail when made by terminology. Recommend writing it up as a CST-style conjecture note with explicit upgrade and failure criteria before it hardens into an assumption.

## Guardrails

- **Closed-universe triviality.** The Harlow–Usatyuk–Zhao / Chen–Penington / Maldacena line — that a closed universe's Hilbert space may be one-dimensional absent special observer rules — sits directly under the II₁ branch. Any use of "the nothing is an attainable state" must carry this controversy as a live threat.
- **The GSL is an inequality.** Second-law-shaped, not first-law-shaped. The equality candidates are the Hamiltonian constraint and flux-balance; keep the types separate.
- **Perturbative scope.** The type assignments and the compact/noncompact asymmetry are semiclassical (G → 0, large N). Whether they survive non-perturbatively is OPEN, and the covariance note marks it as the central open problem.
- **Hegel as compass, not citation.** The being/nothing register earned its keep (it surfaced the trace-as-nothing reading and T3), but it stays in commentary. Nothing in this folder goes to the library without the standard citation audit — the research notes self-flag their weak spots.
- **Revocations from the audit** (`audit-findings.md`): no base cohomological obstruction on the chain; "the class = the flow of weights" is imprecise (the datum is the trace-scaling module). Do not re-import.
