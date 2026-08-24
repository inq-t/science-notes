# The Construction Ladder

The dynamical cosmological case makes every slot of the interface hard at once, so a direct attempt cannot distinguish a wrong identification from a merely difficult calculation. The ladder orders five settings by which slot first becomes nontrivial. Its purpose is diagnostic: agreement across successive rungs would establish a universality pattern, while disagreement localizes the failure to one ingredient instead of to the programme.

## The invariant at every rung

Before computing anything at a given rung, six data must be fixed in order:

1. the region and its selected cut;
2. the algebra;
3. the state, and the rule selecting it;
4. the transport between neighbouring fibers;
5. the reflection-odd channel and its reference balance;
6. the entropy or capacity normalization.

Only then are the return values well posed. Computing a ratio while any of the six is implicit produces a number whose meaning is not fixed, and such a number cannot falsify anything.

## Rung 1 — Rindler wedge

**Newly nontrivial:** nothing. This is the calibration rung.

Geometric modular flow is known exactly: the modular Hamiltonian generates boosts, and the state and algebra are standard. There is no scale family here, so $\Phi$ must be introduced by hand as a chosen one-parameter deformation.

**What it tests.** Whether the reflection-odd channel and the entropy normalization can be exhibited *at all* in a setting where nothing else is in doubt. A construction that cannot produce a balanced binary channel with a well-defined normalization in the wedge has a problem in the channel, not in the cosmology.

## Rung 2 — CFT ball or causal diamond

**Newly nontrivial:** the region has finite extent, so the cut is a genuine choice and the modular Hamiltonian is no longer a global boost.

Local stress-tensor modular Hamiltonians and a Markov property for vacuum regions on a null plane, or a null cone in a conformal theory, are available from [[causal-wall-spectral-theory/sources/papers/1703.10656-casini-teste-torroba-null-plane-modular-hamiltonians.pdf|Casini, Teste, and Torroba]]. The setting is still static and vacuum, so transport between nearby regions is a controlled deformation rather than an evolution.

**What it tests.** Whether the channel and normalization survive localization, and whether a one-parameter family of nested regions produces an affine state coordinate.

## Rung 3 — controlled gravitational or crossed-product degrees of freedom

**Newly nontrivial:** the algebra type changes, and observables must be dressed.

Observer-dependent type-II subregion algebras in the $G_N\to0$ limit are constructed by [[causal-wall-spectral-theory/sources/papers/2306.01837-jensen-sorce-speranza-generalized-entropy-subregions.pdf|Jensen, Sorce, and Speranza]], using states whose instantaneously geometric modular flow is itself conjectural. Horizon-cut algebras with edge modes and half-sided modular structure in perturbative gravity about black-hole backgrounds are constructed by [[causal-wall-spectral-theory/sources/papers/2601.07915-chandrasekaran-flanagan-subregion-algebras-gravity.pdf|Chandrasekaran and Flanagan]].

**What it tests.** Whether the entropy normalization retains its meaning once a density matrix and a trace become available in the crossed product — and whether the edge or corner degrees of freedom introduce additional reflection-odd modes that the channel obligation must then suppress. This is the first rung where the discarded-mode bound in [[binary-channel|the binary channel obligation]] has real content.

## Rung 4 — slowly evolving or perturbative horizons

**Newly nontrivial:** transport becomes a genuine evolution, and the region moves.

Gravitationally dressed observables for a comoving observer in a past-asymptotically-de Sitter cosmology are constructed by [[causal-wall-spectral-theory/sources/papers/2406.01669-kudler-flam-leutheusser-satishchandran-algebraic-observational-cosmology.pdf|Kudler-Flam, Leutheusser, and Satishchandran]].

**What it tests.** Whether the horizontal noncentral term of the comparison is nonzero and frame-independent once the fibers genuinely differ, and whether holonomy is negligible over a finite stretch of the family. This is the first rung at which the affine soldering hypothesis can be checked rather than assumed.

## Rung 5 — dynamical apparent-horizon cut

**Newly nontrivial:** everything, and additionally the region is located by the solution.

This is the intended physical setting and the only rung at which the region trap of [[elimination-test|Test I]] bites. A construction here must either supply an off-shell functional for arbitrary admissible backgrounds and solve the coupled system, or fix the state family from independent initial and matter data.

**What it tests.** The programme's actual claim. A returned width or peak ratio differing from a postulated value falsifies that postulate.

## Reading the ladder

None of the cited constructions supplies the scale-indexed state law, the binary reduction, or the cosmological weld required here. They are controlled precedents for individual slots — a preferred state in a restricted class, a geometric modular Hamiltonian, a dressed observable, a type-II normalization — and their value is that each isolates one ingredient in a setting where the others are known.

Two failure signatures are worth distinguishing in advance:

- **Failure that propagates upward.** If the channel cannot be exhibited at rung 1 or 2, no amount of work at rung 5 will help; the identification is wrong, not merely unproved.
- **Failure that appears only at the top.** If rungs 1–4 agree and rung 5 disagrees, the discrepancy is informative about the dynamical setting specifically — a temperature normalization, a moving region, or holonomy over long stretches — rather than about the reduction.

The second signature is the more valuable outcome, and it is only available if the lower rungs were actually done.

## Interface position

The ladder is a strategy, not an obligation of the interface: a construction that jumps straight to rung 5 and succeeds owes nothing to this note. Its use is that partial results become interpretable. The data that must be fixed at each rung are the slots enumerated in [[wall-construction-interface/entry|the interface package]]; whether a completed rung explains anything is decided by [[elimination-test|the elimination tests]].
