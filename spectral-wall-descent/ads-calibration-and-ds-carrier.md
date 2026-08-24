# AdS Calibration and the de Sitter Carrier

AdS is not identified with the pre-observable side of the wall. Its controlled role is to geometrize scale and to calibrate retained regional Fisher response against gravitational canonical energy. Observable cosmology may remain de Sitter: AdS and dS are different real forms of one complex homogeneous model, and direct gravitational-observable constructions already place de Sitter subregion entropy in type-II algebras. The common object is therefore modular and correspondence algebra, not a hidden claim that our cosmos is AdS.

## Full AdS/CFT is not the wall

An exact AdS/CFT encoding or exact code isometry preserves inner products. It is therefore not the genuinely noninvertible step sought by the wall construction. Noninvertibility enters when one restricts to a boundary region or applies the conditional expectation onto its reconstructable algebra.

Let

$$
E_R:\mathcal A_-\longrightarrow\mathcal M_R
$$

be such an expectation, let \(V\) be an exact code isometry, and let the reference \(\sigma\) lie in the reconstructable algebra. Conditional-expectation Pythagoras and exact operator-algebra quantum error correction give the controlled finite grammar

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

For perturbations of a vacuum CFT ball with a classical AdS dual, the retained term is dual, with the stated Hessian convention, to AdS canonical energy:

$$
\boxed{
G_R^{\mathrm{ret}}
=\mathcal E^{\mathrm{AdS}}_{\mathrm{can},R}.}
$$

This is the key correction to a direct wall-loss weld. Canonical energy calibrates what the region can reconstruct, not automatically what the expectation erases.

The central area term appears in the modular Hamiltonian, but it cancels from relative entropy at fixed code subspace. It must therefore be carried by the separate central entropy operator in [[spectral-wall-descent/finite-index-area-weld|the finite-index area weld]].

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

Normalize \(N=2\pi t\). The affine group admits the left-invariant metric

$$
\mathrm ds^2
=\ell^2
\left(
\mathrm dN^2+e^{-2N}\mathrm dx^2
\right).
$$

With \(z=e^N\),

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

The horizontal BKM line element of the binary state family is

$$
\operatorname{sech}^2N\,\mathrm dN^2,
$$

not \(\mathrm dN^2\). Identifying the affine radial direction with the physical state tangent therefore remains an alignment theorem, not a change of notation.

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

AdS and dS are different real forms of this complex homogeneous variety. This gives a clean algebraic possibility: the upstream complex object can remain homogeneous and signature-neutral, while an antilinear real structure selects the descended signature and curvature sign.

The statement does not select the de Sitter real form, its radius, the Bunch--Davies state, or an arrow of time. Those require additional state, positivity, boundary, and record data.

The [[vendor/holographic-cosmology/domain-wall-cosmology-correspondence|domain-wall/cosmology correspondence]] supplies a controlled physical continuation for a restricted class of gravity--scalar solutions. It continues couplings, potential signs, momenta, and states as well as coordinates. It does not license the claim that every AdS operator dictionary continues unchanged to cosmology.

## Direct de Sitter algebras

The observable carrier need not be secretly AdS. Existing gravitational algebra constructions provide:

- a type-\(\mathrm{II}_1\) algebra for an observer's de Sitter static patch, with entropy equal up to a state-independent constant to generalized entropy;
- type-II algebras for more general compact or asymptotic gravitational subregions in a controlled \(G_N\to0\) regime; and
- type-\(\mathrm{II}_\infty\) algebras for horizon cuts, built as crossed products with edge modes, whose entropy is generalized entropy and whose nesting supports generalized second-law and focusing statements.

This motivates the architecture

$$
\boxed{
\text{scale-indexed }W^*\text{-correspondence stack}
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
4. A dS observable theory can be built directly from gravitational subregion algebras; analytic continuation is a comparison tool, not its ontology.
5. Importing the Ryu--Takayanagi coefficient imports \(G\) and therefore cannot derive its value.

Primary sources: [canonical energy as quantum Fisher information](https://arxiv.org/abs/1508.00897), [JLMS relative entropy](https://arxiv.org/abs/1512.06431), [operator-algebra quantum error correction](https://arxiv.org/abs/1607.03901), [the domain-wall/cosmology correspondence](https://arxiv.org/abs/hep-th/0610253), [holography for cosmology](https://arxiv.org/abs/0907.5542), [the de Sitter static-patch algebra](https://arxiv.org/abs/2206.10780), [general gravitational subregion entropy](https://arxiv.org/abs/2306.01837), and [horizon subregion algebras](https://arxiv.org/abs/2601.07915).
