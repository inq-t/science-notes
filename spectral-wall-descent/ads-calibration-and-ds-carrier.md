# AdS Calibration and the de Sitter Carrier

AdS is not identified with the pre-observable side of the wall. Its controlled role is to geometrize scale and to calibrate retained regional Fisher response against gravitational canonical energy in the vacuum-ball semiclassical regime. Observable cosmology may remain de Sitter: the standard AdS and dS quadrics are different real forms of one complex homogeneous model, and direct semiclassical constructions place selected de Sitter subregion entropies in type-II algebras. The common object is therefore modular and correspondence algebra, not a hidden claim that our cosmos is AdS.

## Full AdS/CFT is not the wall

An exact AdS/CFT encoding or exact code isometry preserves inner products. It is therefore not the genuinely noninvertible step sought by the wall construction. Noninvertibility enters when one restricts to a boundary region or applies the conditional expectation onto its reconstructable algebra.

In a finite exact complementary-recovery model, let

$$
E_R:\mathcal A_-\longrightarrow\mathcal M_R
$$

be the trace-preserving logical expectation under the finite density identification, let \(V\) be an exact code isometry with complementary recovery for the logical algebra and its commutant, and let \(\sigma\) be faithful with \(E_R\sigma=\sigma\). Conditional-expectation Pythagoras and exact operator-algebra quantum error correction then give the controlled finite grammar

$$
\boxed{
\begin{aligned}
D_{\mathcal A_-}(\rho\Vert\sigma)
={}&D_{\mathcal A(R)}
\left(
(V\rho V^*)_R
\middle\Vert
(V\sigma V^*)_R
\right)\\
&+D_{\mathcal A_-}(\rho\Vert E_R\rho).
\end{aligned}}
$$

At coincidence,

$$
\boxed{
G_-=G_R^{\mathrm{ret}}+G_R^{\mathrm{lost}}.}
$$

For a family of physical perturbations with classical asymptotically AdS duals, to second order about the vacuum density matrix of a CFT ball and in the corresponding AdS Rindler wedge, let \(\mathfrak S_R\) be the linearized bulk reconstruction map. With the convention that the relative-entropy Hessian has no extra factor of \(1/2\), the retained metric is the pullback of AdS canonical energy:

$$
\boxed{
G_R^{\mathrm{ret}}(X,Y)
=\mathcal E^{\mathrm{AdS}}_{\mathrm{can},R}
\left(
\mathrm d\mathfrak S_R X,
\mathrm d\mathfrak S_R Y
\right).}
$$

This is the key correction to a direct wall-loss weld. Canonical energy calibrates what the region can reconstruct, not automatically what the expectation erases.

In JLMS, for nearby states with a bulk effective description and to leading order in the bulk gravitational coupling, the surface-area term in the modular Hamiltonian cancels from relative entropy. In the separate exact complementary-recovery code model, its analogue is carried by a central edge-entropy operator. Identifying that operator with gravitational area is the additional weld studied in [[spectral-wall-descent/finite-index-area-weld|the finite-index area weld]], not a consequence of cancellation alone.

## AdS as a geometric atlas of scale

Fefferman--Graham form makes the scale reading explicit:

$$
g_+
=\frac{L^2}{z^2}
\left(
\mathrm dz^2+g_z
\right).
$$

A change of defining function changes the representative of the boundary conformal class. Radial Hamilton--Jacobi evolution consequently geometrizes renormalization scale. But it is already a geometric, action-based observable description; it cannot be used as the ontologically prior cause of the wall if least action belongs downstream.

There is also a small pure-algebra model. A half-sided modular inclusion carries an affine relation of the form

$$
\Delta^{it}U(a)\Delta^{-it}
=U(e^{-2\pi t}a).
$$

Normalize \(N=2\pi t\) and order the group coordinates as \(U(x)\Delta_N\). The group law is

$$
(N,x)(N',x')
=\left(N+N',x+e^{-N}x'\right).
$$

The associated left-invariant metric is

$$
\mathrm ds^2
=\ell^2
\left(
\mathrm dN^2+e^{2N}\mathrm dx^2
\right).
$$

With \(z=e^{-N}\),

$$
\boxed{
\mathrm ds^2
=\ell^2\frac{\mathrm dz^2+\mathrm dx^2}{z^2},}
$$

so its Gaussian and scalar curvatures are

$$
K=-\ell^{-2},
\qquad
R=-2\ell^{-2}.
$$

Thus the algebra of modular dilation and translation already has a hyperbolic, Euclidean-AdS\(_2\) resolution geometry. This is an auxiliary geometry of scale comparison, not a derivation of physical AdS spacetime. Higher dimensions require additional translation and conformal structure; a two-dimensional normal plane is not a \(1+1\) CFT.

The horizontal BKM line element of the binary state family in its own statistical coordinate \(\theta\) is

$$
\operatorname{sech}^2\theta\,\mathrm d\theta^2,
$$

not \(\mathrm dN^2\). Only after a soldering \(\theta=\varrho_\perp(N-N_c)\) does its pullback become

$$
\varrho_\perp^2
\operatorname{sech}^2\!\left(\varrho_\perp(N-N_c)\right)
\mathrm dN^2.
$$

Identifying the affine radial direction with the physical state tangent therefore remains an alignment theorem, not a change of notation.

## One complex homogeneous model, two real forms

In spacetime dimension \(D\),

$$
\mathrm{AdS}_D
=SO(2,D-1)/SO(1,D-1),
$$

$$
\mathrm{dS}_D
=SO(1,D)/SO(1,D-1).
$$

Both complexify to

$$
\boxed{
X_{\mathbb C}
=SO(D+1,\mathbb C)/SO(D,\mathbb C).}
$$

The standard AdS and dS quadrics, before choosing connected components and before passing to the physical universal cover of AdS, are real forms of this complex homogeneous variety. This gives a clean algebraic possibility: the upstream complex object can remain homogeneous and signature-neutral, while an antilinear real structure together with an invariant real bilinear form selects a real slice and signature. The physical AdS universal cover is not literally the displayed algebraic quotient.

The complex quotient alone does not select curvature normalization, causal orientation, the de Sitter real form, its radius, the Bunch--Davies state, or an arrow of time. Those require additional real, state, positivity, boundary, and record data.

The [[vendor/holographic-cosmology/domain-wall-cosmology-correspondence|domain-wall/cosmology correspondence]] supplies a controlled physical continuation for a restricted class of gravity--scalar solutions. It continues couplings, potential signs, momenta, and states as well as coordinates. It does not license the claim that every AdS operator dictionary continues unchanged to cosmology.

## Direct de Sitter algebras

The observable carrier need not be secretly AdS. Existing gravitational algebra constructions provide:

- an observer-dressed type-\(\mathrm{II}_1\) algebra for a de Sitter static patch in the \(G_N\to0\) observer-clock construction, whose entropy agrees up to a state-independent constant with generalized entropy for the semiclassical states under study;
- type-II algebras for bounded regions or regions containing a complete asymptotic boundary in Einstein gravity coupled to matter in the \(G_N\to0\) regime, with the bounded-region construction relying on a supplied observer and conjectural instantaneously geometric modular states; this result explicitly excludes regions that divide an asymptotic boundary, including ordinary AdS entanglement wedges, whose boundary algebras remain type \(\mathrm{III}_1\); and
- a recent perturbative construction of type-\(\mathrm{II}_\infty\) crossed-product algebras for cuts of a stationary black hole with bifurcate Killing horizon. Their entropy agrees with generalized entropy only up to a state-independent constant and a small averaging over fluctuations of the cut location. The generalized-second-law and focusing results are perturbative null-horizon comparisons, not a direct de Sitter carrier.

This motivates the architecture

$$
\boxed{
\text{candidate scale-indexed }W^*\text{-correspondence prestack}
\longrightarrow
\begin{cases}
\text{AdS code atlas for retained-response calibration},\\
\text{dS type-II atlas for observable cosmic geometry}.
\end{cases}}
$$

The shared invariant is modular and categorical structure. Spacetime signature belongs to a realization.

## Construction consequences

1. The previous direct conjecture \(G^{\mathrm{lost}}\propto G^{\mathrm{grav}}\) is too strong. The controlled holographic equality uses \(G^{\mathrm{ret}}\).
2. The coefficient of gravity should be sought in a central area-density weld, not extracted from the fixed-code relative entropy in which the area term cancels.
3. AdS radial flow can model scale transport but does not produce irreversibility or ontological time.
4. These constructions show that a candidate dS observable carrier need not be obtained by analytic continuation from AdS; they do not yet construct a general de Sitter cosmology.
5. Importing the Ryu--Takayanagi coefficient imports \(G\) and therefore cannot derive its value.

Primary sources: [canonical energy as quantum Fisher information](https://arxiv.org/abs/1508.00897), [JLMS relative entropy](https://arxiv.org/abs/1512.06431), [operator-algebra quantum error correction](https://arxiv.org/abs/1607.03901), [half-sided modular inclusions](https://arxiv.org/abs/math/0412061), [the domain-wall/cosmology correspondence](https://arxiv.org/abs/hep-th/0610253), [holography for cosmology](https://arxiv.org/abs/0907.5542), [the de Sitter static-patch algebra](https://arxiv.org/abs/2206.10780), [general gravitational subregion entropy](https://arxiv.org/abs/2306.01837), and [horizon subregion algebras](https://arxiv.org/abs/2601.07915).
