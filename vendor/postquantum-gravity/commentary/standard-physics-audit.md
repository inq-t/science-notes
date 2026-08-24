# Standard-Physics Audit

What the vendored work has established, what it has established conditionally, and what remains open. The purpose is to fix the confidence at which each item may be cited elsewhere in the vault, following the discipline of [[program-core/claim-and-failure-contract|the claim and failure contract]].

## Established

The classical-quantum path integral is a consistent construction: complete positivity is proved directly rather than inferred from a master equation, and the resulting theory of classical gravity coupled to quantum matter is diffeomorphism invariant. It is the first example of diffeomorphism-invariant collapse dynamics in which loss of coherence is derived from the interaction rather than postulated.

**Local** CQ dynamics cannot generate entanglement. This is a theorem, and the locality hypothesis is load-bearing: it requires a sufficiently local noise kernel and that direct quantum interactions be negligible or screened, and nonlocal noise kernels can generate entanglement. What the classical field can do is establish ordinary classical correlation; what it cannot do is entangle. This is what makes the theory falsifiable by entanglement experiments.

The Ostrogradsky objection does not apply. An Onsager--Machlup weight with a real coefficient is a probability density over paths, not a higher-derivative Lagrangian, and the deterministic equation of motion remains the global extremum. The provenance argument — that a $i\ddot q^2$ term comes from integrating out a negative-energy field while $-\ddot q^2/2D_2$ comes from integrating out a positive-energy noise source — is sound.

The scalar-vector-tensor analysis establishes that the dynamical stochastic modes are one spin-0 and two spin-2 polarisations, and that the Newtonian potential and the vector are fixed by constraints. That the indefinite sector is the non-dynamical one is established only *relatively*: the vector action ceases to be indefinite once the path integral is restricted to continuous geometries, and the published paper reports the sector positive semidefinite on shell while the off-shell tachyonic modes are not yet understood.

The Itô drift result is clean: a constraint convex in a variable that receives noise acquires a strictly positive drift, with no tuning.

## Established conditionally

Renormalisability is *formal*: power counting plus a mapping onto quadratic gravity. It is conditional on pole prescriptions in loops preserving both renormalisability and complete positivity, which is unresolved and which the authors name as the key remaining question.

Positivity of the two-point function has been shown for the scalar mode and, sector by sector, for the dynamical modes. It has not been shown for the whole theory, and the published construction explicitly does not prove normalisability.

Ultraviolet growth of the diffusion follows from an expected sign flip in the beta functions, argued by analogy with quadratic gravity rather than computed, and even there the direction of running depends on initial couplings. Asymptotic freedom is a different matter: it is a cited property of scale-invariant quadratic gravity, inherited through the mapping rather than derived here, and should not be filed as a consequence of the sign flip.

Selection of the scale-invariant theory by positivity is stated with the qualification that the matter couplings differ from quadratic gravity's and the condition may be relaxable.

## Open, and named as such by the authors

The Lorentzian deWitt kernel is not positive semidefinite. Its negative eigenvalues are argued to be benign, but the effect of the normalisation on the magnetic part of the Weyl curvature is not understood and could cost covariance.

Boundary terms in a stochastic theory, including the Gauss--Bonnet term routinely dropped in higher-derivative gravity, are not worked out.

An infrared divergence appears when linearising about Minkowski rather than a spacetime with a horizon.

How constraints are imposed in the path integral beyond linear order, where vector--scalar mixing becomes dynamically relevant, is unresolved.

Whether the path-integral theory is equivalent to the master-equation theory is not known; the published paper says it may be inequivalent.

The renormalisation-group map from laboratory to cosmological scales cannot currently be performed, so the cosmological applications import laboratory bounds by assumption.

The quoted bounds on the dimensionless coupling do not agree across the sources: the renormalisation paper's window and the newest sector-resolved one are disjoint, as recorded in [[empirical-status]]. Until that is reconciled, no single number should be cited as *the* bound.

## Weaknesses the audit adds

Two methodological points deserve recording beyond what the sources emphasise.

**Order of operations.** Reducing the phase space by solving constraints and then adding noise gives different physics from letting noise act on the full metric and recovering constraints from the path integral. The sources identify this and note the parallel to Dirac versus reduced-phase-space quantisation. Any downstream use must state which order it assumes.

**Free parameters fixed by the consistency they establish.** In the rotation-curve work an undetermined time scale $\epsilon$ is bounded by requiring agreement between astrophysical and tabletop results, and that agreement is then reported as a result. The phantom-dark-matter work is better than this: its Hubble-volume averaging scheme is defended on causal-contact grounds and does satisfy the constraint that rules out the alternative — but the authors still state that they have no rigorous procedure for the renormalisation, so the scaling is argued rather than forced. Neither is dishonest, both are flagged by the authors, and neither may be cited as a prediction. This is the same failure mode recorded for the previous vendor in [[vendor/entropic-gravity/commentary/methodological-lessons|the methodological lessons]]: a coefficient that enters the derivation cannot be counted among its outputs.
