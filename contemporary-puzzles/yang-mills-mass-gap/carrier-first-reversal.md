# The Carrier-First Reversal

An operator has no physical meaning apart from the carrier, domain, state, and clock on which it acts. The useful reversal is therefore not merely to calculate mass from a chosen geometry, but to start from the physical observable carrier and its energetic quadratic form, construct the operator by representation theory, and only then read off the intrinsic geometry encoded by that form. At finite Yang--Mills regulator this reversal is exact. In the continuum it becomes a concrete construction programme, while spectrum-to-geometry by itself remains nonunique and cannot prove a gap already assumed in the input.

**Status: [EXACT FUNCTIONAL-ANALYTIC REVERSAL; OPEN YANG--MILLS CONTINUUM CONSTRUCTION].** The representation theorem for closed forms, semigroup reconstruction, carré du champ, and finite-regulator carrier identifications are exact under their stated hypotheses. The continuum vacuum measure, closability, Osterwalder--Schrader identification, and uniform Poincare bound remain open.

## The Copernican criterion: change the primitives

A genuine reversal does not merely solve the old equations for a different variable. It replaces what is assumed with what can be reconstructed. To honor the question “what does the operator operate on?”, the proposed primitive package is more precisely

$$
\mathfrak P
=
(\mathfrak A,\omega,\mathsf C,\mathcal K_\partial,\partial),
$$

where \(\mathfrak A\) is an algebra or higher algebra of distinctions, \(\omega\) is a state or consistency functional, \(\mathsf C\) is a directed relation on a declared category of contexts, \(\mathcal K_\partial\) is a response Hilbert space or correspondence, and

$$
\partial:
\mathfrak A_0
\longrightarrow
\mathcal K_\partial
$$

is a canonically normalized distinction map on a dense test algebra. The state first constructs the GNS carrier \((\pi_\omega,\mathcal H_\omega,\Omega)\). Writing

$$
\mathcal N_\omega
:=
\{a\in\mathfrak A_0:\omega(a^*a)=0\},
$$

the response becomes a form on what the theory can physically distinguish only if it descends through the state-null ideal, for example through \(\partial n=0\) for \(n\in\mathcal N_\omega\):

$$
\mathfrak d_\partial([a],[b])
:=
\langle\partial a,\partial b\rangle_{\mathcal K_\partial},
\qquad
[a]=\pi_\omega(a)\Omega.
\tag{C0a}
$$

Closability is then a theorem to prove, not a word hidden inside “operator.” None of these data is yet “matter moving in spacetime,” and the response generator obtained from the closed form is not yet the physical clock Hamiltonian. A successful reconstruction must produce

$$
\boxed{
\mathfrak P
\xrightarrow{\ \mathsf{Rec}\ }
(M,[g],\sigma,\mathcal O\mapsto\mathfrak A(\mathcal O),U,P_\mu,H,M^2),}
\tag{C0}
$$

with event localization, causal cones, metric scale, an observable net, Poincare action, clock Hamiltonian, and invariant mass operator satisfying their required compatibility laws.

| Conventional primitive | Carrier-first reconstruction target |
|---|---|
| things located at spacetime points | states, characters, sectors, or records individuated by an algebra |
| pre-given spatial distance | distance reconstructed from a Dirichlet form, commutator seminorm, or correlation response |
| locality as microscopic ontology | isotony, commutation, causal factorization, and finite propagation of the observable net |
| one undifferentiated time variable | directed record order, reversible clock automorphisms, Euclidean preparation, and modular flow, compared but not identified |
| mass as stuff or a field coefficient | Poincare Casimir and a positive lower edge of the reconstructed translation spectrum |
| a black hole as an object enclosing an assumed interior | an exterior equivalence class, with sector status and any interior ontology owed by reconstruction |
| entropy as substance | unresolved distinguishability relative to a state, algebra, boundary, or channel |

This is the programme's Copernican test. If \(\mathsf{Rec}\) recovers the QFT observables and symmetries and makes the gap follow from a simpler coercive principle, the reversal has explanatory force. If it merely renames energy “distinction,” assumes the desired response form, or fails to recover locality and Poincare covariance, it has redrawn the epicycle.

## Explanatory order is not algebraic rearrangement

An equation may be solved in either direction without either direction becoming an explanation. The proposed order is instead a dependency graph:

$$
\boxed{
\mathfrak P
\longrightarrow
(\mathcal H_\omega,\overline{\mathfrak d}_\partial)
\xrightarrow{\text{clock and energy solder}}
(\mathcal H_{\mathrm{phys}},\mathfrak h)
\longrightarrow
H
\longrightarrow
\Delta_E.}
\tag{C0b}
$$

Geometry is reconstructed from the algebra and closed response form along a second downstream branch; it is not inserted into the first arrow as a pre-given container. The mass gap becomes explanatory only if no construction arrow secretly points backward from \(H\), \(\Delta_E\), a fitted correlator, or the observed glueball spectrum into \(\mathfrak P\). In particular,

$$
\mathfrak d_\partial
:=
E_*^{-1}\mathfrak h
$$

would make the desired comparison true by definition and explain nothing.

A proposed Copernican replacement therefore has five non-circularity tests:

1. **Upstream definability:** the algebra, state, directed relation, response carrier, and distinction map are defined without a background metric, the Yang--Mills Hamiltonian, or its low spectrum.
2. **Fixed normalization:** rescaling \(\partial\), its fiber metric, the wall measure, or the clock is forbidden after spectral data are consulted.
3. **Typed realization:** explicit maps carry the response form to the physical carrier and separately reconstruct localization, Poincare covariance, and clock evolution.
4. **Uniform coercivity:** the lower bound covers the entire nonvacuum carrier and survives volume, cutoff, and continuum limits.
5. **Empirical recovery:** the reconstructed net, state, scattering or correlators, and gauge identities recover ordinary Yang--Mills in a declared regime.

This is how the Copernican claim becomes falsifiable. GR and QFT may remain exact or effective calculational descriptions of the reconstructed observable arena while ceasing to dictate the ontology from which that arena is built.

For Yang--Mills, the reversed question is therefore

$$
\boxed{
\text{Why can no nonvacuum gauge-invariant distinction be made at arbitrarily small clock cost?}}
\tag{C1}
$$

The word *clock* is load-bearing: a dimensionless algebraic obstruction becomes a mass gap only after the reconstruction identifies the physical time-translation generator and proves a uniform form comparison on its full vacuum complement. [[horizon-saturation-and-entropic-distinction]] develops the entropy and localization-boundary version of the same reversal; [[mass-as-casimir-and-realization]] supplies its representation-theoretic mass type.

## The operator-carrier ledger

The recurring operators in this programme do not act on the same thing:

| Operator | Carrier | What its spectrum can mean |
|---|---|---|
| \(H_{\mathrm{phys}}\) | the vacuum GNS Hilbert space \(\mathcal H_\omega\) of gauge-invariant observables | physical energy and mass gap |
| \(e^{-\tau H_{\mathrm{phys}}/\hbar}\) | the same physical carrier, or OS equivalence classes after reconstruction | Euclidean-time correlation decay |
| \(K_\Gamma=-\sum_{e,A}(X_e^A)^2\) | gauge-invariant link wavefunctions in \(L^2(SU(3)^{E(\Gamma)})\) | regulated electric-flux energy |
| \(\mathscr L_\Gamma\) | functions in \(L^2(\nu_\Gamma)\) after the vacuum ground-state transform | the same regulated gap as a weighted Poincare constant |
| \(-\Delta_{SU(3)}^{\mathrm{rad}}\) | one-link class functions, equivalently a Weyl-anti-invariant torus subspace | one-link Casimir spectrum |
| \(L_w=-\partial_N^2+w^2\) | amplitudes on a declared half-line domain | the auxiliary Witten threshold \(w^2\) |
| \(\bar\partial\), a complex Dirac operator, or a Laplacian on \(S^6\) | forms, spinors, or sections on the chosen complex sphere | complex-geometric cohomology or metric spectrum |
| a Connes operator \(D\) | a Hilbert-space representation of an algebra | a commutator seminorm and, under additional axioms, spectral geometry |

Equal eigenvalues across rows do not identify the operators. A physical bridge must supply an intertwiner that preserves the relevant state, quadratic form, domain, and time normalization.

## The acceptance test for a proposed geometry

Let a candidate metric-measure construction supply \(L^2(X,\nu)\), vacuum \(1\), and closed form \(\mathcal E_{\mathrm{cand}}\). Normalize the physical vacuum energy so that \(H_{\mathrm{phys}}\Omega=0\), and let its Hamiltonian form be

$$
\mathfrak h(\Psi,\Phi)
:=
\langle H_{\mathrm{phys}}^{1/2}\Psi,
H_{\mathrm{phys}}^{1/2}\Phi\rangle.
$$

The candidate is physically realized only if there is a vacuum-preserving unitary

$$
W:L^2(X,\nu)\longrightarrow\mathcal H_{\mathrm{phys}},
\qquad
W1=\Omega,
$$

such that, with one declared dimensional normalization, on a form core,

$$
\boxed{
\mathcal E_{\mathrm{cand}}(f,g)
=
\mathfrak h(Wf,Wg).
}
$$

The representation theorem then forces unitary equivalence of the generators. For a lower bound, equality can be weakened to a one-sided form comparison covering the whole physical vacuum complement:

$$
\mathfrak h(Wf,Wf)
\geq
c\,\mathcal E_{\mathrm{cand}}(f,f),
\qquad
c>0.
$$

Matching an eigenvalue, determinant degree, heat coefficient, or dimension does not pass this test. This is the common admission rule for \(S^6\), \(A_2\), wall, and Connes-inspired candidates. [[measured-response-carriers/response-to-energy-comparison|The generic response-to-energy theorem]] gives the lower-bound version with an analysis map rather than a unitary equivalence; in the present unitary case its map is \(J=W^{-1}\) on the physical form core.

## Begin with the form, not a differential expression

Let \(\mathcal H\) be a declared Hilbert carrier and let

$$
\mathcal E:
D(\mathcal E)\times D(\mathcal E)
\longrightarrow
\mathbb C
$$

be a densely defined, closed, nonnegative quadratic form. The first representation theorem supplies a unique nonnegative self-adjoint operator \(L\) such that

$$
D(\mathcal E)=D(L^{1/2}),
\qquad
\mathcal E(f,g)
=
\langle L^{1/2}f,L^{1/2}g\rangle.
$$

If the form is Markovian, \(P_t=e^{-tL}\) is a symmetric Markov semigroup. Conversely,

$$
\boxed{
\mathcal E(f,g)
=
\lim_{t\downarrow0}
\frac1t
\langle f,(1-P_t)g\rangle
}
$$

on the form domain. Thus the following three presentations determine one another under the declared hypotheses:

$$
\text{closed energy form}
\longleftrightarrow
\text{positive generator}
\longleftrightarrow
\text{symmetric semigroup}.
$$

For a physically normalized positive, self-adjoint, injective transfer step

$$
\widetilde T_\tau
=
e^{-\tau H_{\mathrm{phys}}/\hbar},
$$

spectral calculus gives

$$
\boxed{
H_{\mathrm{phys}}
=
-\frac{\hbar}{\tau}\log\widetilde T_\tau.
}
$$

The factors \(\tau\) and \(\hbar\) are the clock solder. If a proposed transfer map has a kernel, negative spectrum, or lacks self-adjointness, this logarithm does not produce the claimed positive Hamiltonian without additional choices.

This is the rigorous reversal tactic. The differential formula for \(L\) is secondary; the form already says which variations cost energy.

A Hilbert-space contraction semigroup is not automatically geometric. To obtain a classical Dirichlet form, one must also choose a represented commutative configuration algebra \(\mathcal D\simeq L^\infty(X,\nu)\) with \(\Omega\leftrightarrow1\), and prove that the transformed semigroup is positivity preserving, \(L^\infty\)-contractive, and conservative. Without this Markov gate, a positive generator supplies dynamics but not a configuration-space metric.

[[contemporary-puzzles/yang-mills-mass-gap/receipts/carrier_reversal_receipt.py|The finite-dimensional reversal receipt]] reconstructs a generator, form, carré du champ, and Poincare gap from one semigroup. It then exhibits two symmetric three-state generators with the same vacuum and spectrum \(\{0,1,10\}\), while only one is Markov in the declared coordinate cone; [[contemporary-puzzles/yang-mills-mass-gap/receipts/carrier-reversal-receipt-output.txt|the stored output]] records the passing run. The example isolates why spectral data do not choose a configuration geometry.

## The gap is the coercivity of the form

Suppose \(1\in\ker L\) and the vacuum line is the whole kernel. Then

$$
\Delta_L
=
\inf_{\substack{f\in D(\mathcal E)\\
\langle1,f\rangle=0\\
f\neq0}}
\frac{\mathcal E(f,f)}{\lVert f\rVert^2}.
$$

Equivalently,

$$
\operatorname{Var}_\nu(f)
\leq
\frac1{\Delta_L}\mathcal E(f,f).
$$

The gap is therefore not attached to an operator symbol in isolation. It belongs to the tuple

$$
\boxed{
(\text{carrier},\text{vacuum state},\text{closed form},\text{clock normalization}).
}
$$

Changing any entry can change the physical meaning or numerical value while leaving a superficially similar differential expression.

## Geometry can be reconstructed from energetic distinguishability

For a strongly local diffusion generator written with the positive convention \(P_t=e^{-tL}\), define the carré du champ for real \(f,g\) in a suitable algebra by

$$
\Gamma_L(f,g)
:=
\frac12
\left(
fLg+gLf-L(fg)
\right).
$$

For an ordinary weighted Laplacian this is

$$
\Gamma_L(f,g)
=
\langle\nabla f,\nabla g\rangle_{G^{-1}},
\qquad
\mathcal E(f,g)
=
\int\Gamma_L(f,g)\,\mathrm d\nu.
$$

The cometric is therefore recoverable by asking how much energy local coordinate functions cost:

$$
G^{ij}
=
\Gamma_L(x^i,x^j).
$$

Under the regularity hypotheses of strongly local Dirichlet-form geometry, the associated intrinsic distance is

$$
d_{\mathcal E}(x,y)
:=
\sup
\left\{
f(x)-f(y):
\Gamma_L(f,f)\leq1
\right\}.
$$

This is the precise sense in which spatial or configuration-space measure can be downstream of energetic relations. One does not first need points moving through a pre-given container; one can reconstruct a notion of separation from which distinctions can be made at bounded flux cost.

Strong locality is itself an output to test. If the form has jump or killing parts, the Beurling--Deny decomposition reconstructs a nonlocal kernel or loss term rather than an ordinary Riemannian metric. On a noncommutative observable algebra, the analogous exact object is a gradient correspondence and derivation

$$
\partial:\mathfrak A\longrightarrow\mathcal H_\partial,
\qquad
\mathcal E(a,b)
=
\langle\partial a,\partial b\rangle_{\mathcal H_\partial}.
$$

A Dirac-type block built from \(\partial+\partial^*\) is then a further proposal. Bounded commutators, compact resolvent, summability, orientation, and reconstruction remain separate theorems.

The Connes formula has the same carrier-first grammar:

$$
d_D(\varphi,\psi)
=
\sup_{\substack{a=a^*\\\lVert[D,\pi(a)]\rVert\leq1}}
|\varphi(a)-\psi(a)|.
$$

Here \(D\) acts on the Hilbert representation, \(a\) belongs to the represented algebra, and the distance is reconstructed on states. Merely naming a Dirac operator without these types supplies no geometry.

## The Yang--Mills reversal

The forward route is

$$
\text{guessed orbit geometry}
\longrightarrow
\text{Laplacian}
\longrightarrow
\text{spectrum}
\longrightarrow
\text{mass}.
$$

The carrier-first route is

$$
\boxed{
\begin{aligned}
\text{gauge-invariant local algebra and vacuum}
&\longrightarrow
\text{physical }L^2\text{ carrier},\\
\text{electric-flux derivations and vacuum state}
&\longrightarrow
\text{closed Dirichlet form},\\
\text{closed form}
&\longrightarrow
\text{self-adjoint generator and semigroup},\\
\text{uniform Poincare inequality}
&\longrightarrow
\text{mass gap},\\
\Gamma_L
&\longrightarrow
\text{effective orbit-space cometric and distance}.
\end{aligned}
}
$$

At finite regulator, [[contemporary-puzzles/yang-mills-mass-gap/gauge-descent-flux-fisher-coercivity|the flux-coercivity theorem]] executes these arrows after the vacuum is known. The continuum construction target is to:

1. construct a reflection-positive vacuum measure \(\nu\) on gauge-invariant cylinder data or another precise observable carrier;
2. define renormalized electric derivations and prove that their quadratic form is closable;
3. prove that constants are the whole kernel;
4. establish a Poincare constant positive in physical \(\Lambda_{\mathrm{YM}}^{(\mathsf s)}\) units, uniformly in volume and regulator removal;
5. identify the resulting semigroup with physical Euclidean time by OS reconstruction or a direct positive-energy construction; and
6. derive the intrinsic configuration geometry from \(\Gamma_L\) afterward.

This order can bypass the demand for a globally smooth orbit manifold. Singular quotient strata are carried by the measure and form domain before any coordinate geometry is imposed. The coarse invariant algebra may nevertheless forget stabilizer groups, orbit-type incidence, Gribov data, and topological or \(\theta\)-sectors. If those are physical, the transformation groupoid, stack, or crossed-product data must be retained alongside the invariant spectrum.

For regulator removal, a precise target is generalized Mosco convergence of the physical-unit forms on appropriately identified varying Hilbert spaces. Write

$$
\widehat{\mathfrak h}_{a,L}
:=
\frac{\mathfrak h_{a,L}}
{\Lambda_{\mathrm{YM}}^{(\mathsf s)}}.
$$

The desired convergence and bound are

$$
\widehat{\mathfrak h}_{a,L}
\xrightarrow[\ L\to\infty,\ a\to0\ ]{\mathrm{Mosco}}
\widehat{\mathfrak h},
$$

and

$$
\boxed{
\widehat{\mathfrak h}_{a,L}[\Psi]
\geq
\gamma_{\mathsf s}
\lVert(1-P_{0,a,L})\Psi\rVert^2,
\qquad
\gamma_{\mathsf s}>0.
}
$$

Together with convergence of the vacuum projections, this can pass the coercive inequality to the limiting form. Strong resolvent or semigroup convergence alone does not prevent low-energy states from escaping to infinite volume.

## What the reversal does not license

The Einstein equation permits an analogous inverse reading: once a metric and the gravitational field equation are fixed, its Einstein tensor defines an effective stress tensor. That does not make curvature and matter the same concept, nor does it make the inverse initial-boundary problem unique. The equation is the solder.

The same firewalls apply here:

- A spectrum alone does not determine a unique geometry; isospectral nonisometric spaces exist.
- A closed form can determine an intrinsic metric only under locality, regularity, and nondegeneracy hypotheses.
- An abstract Hamiltonian does not choose a unique coordinate algebra or positivity cone; different choices can present unitarily equivalent dynamics as different geometries.
- Reconstructing \(L\) from an already observed semigroup is diagnostic, not a proof that the gap is positive.
- The exact ground-state weight contains information about the same Hamiltonian. Estimating its curvature from assumed correlation decay is circular.
- A carré du champ recovers a principal energetic symbol, not a unique split into base volume, orbit Jacobian, and vacuum potential.
- Boundary conditions and self-adjoint extensions remain part of the operator even when the formal differential expression is unchanged.
- A configuration-space metric is not physical spacetime curvature.
- An \(S^6\) operator, a one-link radial operator, and the Yang--Mills Hamiltonian remain different until a form-preserving carrier map is constructed.

The reversal is consequently methodological rather than magical: prove the energetic relation on the correct carrier first, allow its geometry to emerge second, and attach the word *mass* only after physical time translation has been identified.
