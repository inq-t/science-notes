# Spectral Wall Descent

Spectral wall descent is the proposed algebraic passage from a homogeneous noncommutative spectral datum to a symmetry-broken observable geometry. The construction now has three distinct ledgers: conditional expectation splits retained from erased distinguishability; a finite-index correspondence plus extra expectation and fixed-edge-state data can define a candidate central entropy operator; and a later, generally infinite-index readout produces commutative facts and records. AdS holography calibrates retained Fisher response against canonical energy in a controlled vacuum-ball regime, while direct semiclassical de Sitter type-II constructions supply candidate observable carriers. The spectral action and least-action equations remain downstream. The open theorem is an all-patch equality between central edge entropy, horizontal BKM capacity, and independently normalized spectral area—not a conservation of unitary information or a renaming of loss as gravity.

## The revised order of construction

The proposed order is

$$
\boxed{
\begin{aligned}
&\text{homogeneous pre-observable spectral datum}\\
&\longrightarrow
\text{finite-index noncommutative gravitational descent}\\
&\longrightarrow
\text{observable geometry and spectral action}\\
&\longrightarrow
\text{generally infinite-index factual descent and record}.
\end{aligned}}
$$

Write the upstream datum schematically as

$$
\Sigma_-=(\mathcal A_-,\mathcal H_-,D_-,J_-,\gamma_-,\omega_-).
$$

No principle of least action and no information-conserving unitarity is imposed on this register. A wall chooses an observable algebra or context \(\mathcal B\), together with a genuinely noninvertible comparison such as a conditional expectation

$$
E:\mathcal A_-\longrightarrow\mathcal B.
$$

Only after a represented observable spectral geometry \(\Sigma_+\) has been constructed does the spectral action

$$
S_{\mathrm{spec}}[D_{+,A}]
=\operatorname{Tr}f(D_{+,A}/\Lambda)
$$

have its ordinary variational meaning. [[spectral-wall-descent/observable-spectral-action|The observable spectral-action note]] fixes that register boundary.

## The exact loss--gain theorem

For a finite tracial inclusion \(\mathcal B\subseteq\mathcal A\), let \(E\) be the trace-preserving conditional expectation and let \(\bar\rho=E(\rho)\). Then

$$
\boxed{
S(\bar\rho)-S(\rho)
=D(\rho\Vert\bar\rho)
\geq0.}
$$

Relative to the tracial reference \(\tau=\mathbf1/n\), this becomes

$$
\boxed{
D(\rho\Vert\tau)
=D(\bar\rho\Vert\tau)
+D(\rho\Vert\bar\rho).}
$$

Thus pre-observable negentropy or distinguishability is divided into retained observable distinguishability and wall-produced entropy. Nothing in this equation is a conserved energy, an ontological count of bits, or a unitary flow. [[spectral-wall-descent/conditional-expectation-balance|The conditional-expectation balance]] proves the result, states its modular existence gate, and distinguishes the entropy of an unconditioned observable law from an actual character.

At coincidence, the same theorem gives an orthogonal BKM response split

$$
\boxed{
\mathbb G^{\mathrm{pre}}
=\mathbb G^{\mathrm{obs}}
+\mathbb G^{\mathrm{wall}}.}
$$

The original direct proposal

$$
\mathbb G^{\mathrm{wall}}
\stackrel{?}{=}
Z_g\,\mathfrak S^*\mathbb G^{\mathrm{grav}}
$$

is now too strong. For physical perturbations with classical asymptotically AdS duals, to second order about a vacuum CFT ball and in its AdS Rindler wedge, controlled results identify **retained** regional quantum Fisher information with gravitational canonical energy. In exact complementary-recovery codes, the fixed central edge term cancels from relative entropy. The revised weld has two independent parts:

$$
\boxed{
\mathbb G^{\mathrm{ret}}
\stackrel{\mathrm{AdS\ calibration}}{=}
\mathfrak S^*\mathcal E_{\mathrm{can}}^{\mathrm{grav}},}
$$

$$
\boxed{
\mathcal L_\chi(U)
\stackrel{?}{=}
\eta_*\mathcal A_D^Z(U)
\qquad\text{for every admissible patch }U.}
$$

Here \(\mathcal L_\chi\) is a candidate central operator built from algebraically selected fixed edge states, and \(\mathcal A_D^Z\) is a compatible central spectral-area assignment with normalization independent of measured gravity. In a type-I product cell, the exact debugging identity for the auxiliary tracial expectation is

$$
\boxed{
S(\chi)+D(\chi\Vert\tau)
=\frac12\log\operatorname{Ind}_{W}(E_\tau).}
$$

Thus a chosen product input edge entropy and its distinction from the tracial state partition the erased factor's log-dimension in one matched finite model; this is not the full index capacity, and the code expectation selecting \(\chi\) need not be the tracial expectation. Identifying the fixed code edge operator with gravity remains the independent spectral-area weld. [[spectral-wall-descent/finite-index-area-weld|The finite-index area weld]] proves the scoped identity, and [[spectral-wall-descent/ads-calibration-and-ds-carrier|AdS calibration and the de Sitter carrier]] fixes the holographic typing.

## What persists through symmetry breaking

Inner fluctuations can change gauge fields, Higgs data, masses, and the observable spectral action while leaving the \(K\)-homology class of the spectral triple fixed under the usual bounded-perturbation hypotheses. Its cyclic Chern character changes only by transgression. Consequently, index pairings remain invariant while local representatives and curvature densities change.

This is a non-Noether meaning of symmetry through symmetry breaking:

$$
\boxed{
\text{the representative and its stabilizer change;
the algebraic pairing class persists}.}
$$

[[spectral-wall-descent/index-and-curvature-transgression|Index and curvature transgression]] develops this class-level conservation and the relative \(K\)-theory of an observable context. It also states the separate Cartan-geometric possibility that local \(G\to H\) reductions acquire a connection whose curvature becomes spacetime gravity only after genuine soldering.

## Why entropy is close to anti-information

For a finite \(n\)-level tracial register,

$$
D(\rho\Vert\tau_n)=\ln n-S(\rho).
$$

Entropy is therefore the complement of distinguishability from the maximally uninformative reference. A wall expectation raises \(S\) by exactly the coherence or relative distinction it removes. This statement is reference- and algebra-dependent. Local type-III algebras generally have no density-matrix trace or absolute von Neumann entropy, so the continuum theory must begin with Araki relative entropy and modularly admissible expectations rather than an absolute entropy stock.

Nor is the actual fact itself entropic in the same way. A character of a finite commutative algebra is a pure state with zero Shannon entropy. The entropy above belongs to the unconditioned law of possible observable characters. Factive selection and persistent record formation remain the later construction in [[conservation-of-causal-charge/factive-descent-and-records|factive descent and records]].

## Calculated consequences

The finite and spectral calculations establish the following useful facts.

1. For the diagonal context \(\mathbb C^n\subset M_n(\mathbb C)\), relative \(K\)-theory contains the exact zero-sum lattice

   $$
   \ker\!\left(\mathbb Z^n\xrightarrow{\sum}\mathbb Z\right)
   \cong A_{n-1}.
   $$

   Its real span is the decomposition into the homogeneous direction and mean-zero observational distinctions used by [[program-core/common-response-matrix|the common response matrix]].

2. A two-level finite spectral triple makes the wall BKM cost a positive norm of a Dirac commutator. Its bulk spectral action remains constant along conjugacy orbits while its fixed-context entropy defect changes. [[spectral-wall-descent/finite-spectral-wall|The finite spectral wall]] gives the formulas and reproducible receipt.

3. A three-level exponential family has

   $$
   G_{N\zeta}=0,
   \qquad
   \mathcal C_{N\zeta\zeta}=\frac{1}{2\sqrt2}.
   $$

   [[spectral-wall-descent/mixed-response-jet|The mixed-response jet]] is an exact realization of a vanishing quadratic cross block with a nonzero first scale variation of observational response.

4. Normalized heat-kernel entropy cancels the term linear in \(a_2\) containing the Einstein--Hilbert action; \(a_2\) re-enters only quadratically at the next order. [[spectral-wall-descent/heat-entropy-no-go|The heat-entropy no-go]] proves that ordinary spectral entropy cannot simply be called gravity. A different, explicitly unnormalized defect functional retains \(a_2\) linearly, but its physical status remains conjectural.

5. Eliminating one positive hidden block produces the exact correction \(-BL^{-1}B^*\). [[spectral-wall-descent/hidden-resolvent-and-seesaw|One hidden resolvent]] shows how its zero mode can shift homogeneous response, its nonzero modes can generate a scale-dependent observational kernel, and its finite internal block can produce a seesaw mass. These are algebraically unified openings for dark-energy, dark-matter, and neutrino questions, not physical identifications.

6. The twisted grand-symmetry involution gives the exact expectation \(E_\rho=(1+\rho)/2\) onto its fixed algebra. The Majorana singlet is twist odd, and its positive two-level normalization reproduces the binary BKM profile. [[spectral-wall-descent/twist-fixed-point-wall|The twisted fixed-point wall]] states the additional state-selection postulate.

7. One positive singlet repairs a target response matrix if and only if the mismatch is positive semidefinite of rank at most one. [[program-core/singlet-response-completion|The singlet response-completion test]] replaces the claim that an extra scalar “fixes the coupling” by a generalized-eigenvalue and rank test.

8. One background-dependent positive Gaussian hidden operator can produce both the Schur correction and a central log determinant. The negative log determinant has the positive classical Fisher or commutative-BKM Hessian, while the real bosonic effective action uses the opposite sign. [[spectral-wall-descent/response-determinant|The response--determinant bridge]] is a finite same-operator relation between response and downstream action, not a general quantum-BKM theorem.

9. The Majorana cosmological coefficient completes into a positive square plus an \(R\)-independent residual. The source's fixed-ray minimum is generally anisotropic; a broader project-chosen traceless hyperbolic orbit keeps the spectral Newton coefficient constant while producing an exact \(\operatorname{sech}^2\) deficit. [[spectral-wall-descent/majorana-square-and-cosmic-pulse|The Majorana square and cosmic pulse]] proves the scoped identities and exposes the remaining amplitude hierarchy.

The finite Majorana block in Connes' Standard Model geometry supplies an additional downstream calculation. [[spectral-wall-descent/majorana-response-jacobian|The Majorana response Jacobian]] shows that one matrix \(M_R\) simultaneously changes the Einstein coefficient, cosmological coefficient, Higgs mass parameter, and seesaw spectrum. This is a genuine shared observable source, not yet the pre-observable common response.

## Relation to postquantum gravity

[[vendor/postquantum-gravity/entry|Postquantum gravity]] begins from a fundamental classical--quantum split and asks which completely positive stochastic dynamics can preserve it. Its decoherence--diffusion trade-off and Onsager--Machlup history weight are therefore downstream of the question posed here. At trade-off saturation, purity conditioned on a classical trajectory is an exact result in that theory; it does not imply unitarity of this wall, because the classical trajectory and the action over histories have already been assumed.

The transferable idea is narrower. An equation-of-motion-squared functional can be a positive cost or probability weight rather than a deterministic higher-derivative action. That supplies a useful observable model for a descent residue and motivates the positive cost realization in [[program-core/common-response-matrix#A positive descent-cost realization|the common response construction]]. It does not derive the noninvertible context map, identify diffusion with \(\Sigma_E\), or explain why a classical spacetime carrier exists. Importing that carrier would assume the descent that this module is meant to construct.

## Present construction boundary

The current result does not derive spacetime from a spectral triple, identify entropy with curvature, or prove that the wall expectation exists for a local QFT algebra. It does identify the correct objects and the first decisive obstructions:

- a generic commutative context need not admit a state-preserving expectation;
- a final type-III-to-commutative wall cannot be a finite-index subfactor step;
- a unitary or invertible wall map cannot realize genuine loss, while Morita equivalence alone supplies no loss mechanism;
- the bulk spectral action cannot recover context-dependent wall entropy;
- a scalar index is too coarse in the presence of centers, where the matrix dimension or full correspondence must be retained;
- AdS canonical energy calibrates retained rather than erased response;
- a central edge entropy has no physical inverse-area value until the cut Dirac operator is independently normalized; and
- a curvature interpretation requires a constructed connection, transgression, and soldering to tangent geometry.

The research target is therefore [[spectral-wall-descent/scale-correspondence-stack|a scale-indexed correspondence prestack]] with effective descent still to prove, Q-system or equivalent data for a finite-index candidate gravitational expectation, an algebraically selected central edge-state cocycle, and independently normalized spectral area. It must prove the equality of edge, BKM, and area densities, realize de Sitter causal geometry, and only later supply a commutative character and one-sided record algebra without importing any of them from the desired cosmology.
