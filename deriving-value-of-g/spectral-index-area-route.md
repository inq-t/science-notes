# The Spectral Index--Area Route to \(G\)

The finite-index route derives \(G\) only if a central edge-entropy measure produced by the gravitational correspondence has a universal Radon--Nikodym density with respect to an independently normalized spectral area measure, and the physical scale tangent has the same local BKM density. This replaces a verbal information--gravity identification by an all-patch operator identity. The algebraic entropy per cell is calculable in finite models; the dimensional spectral area and the equality of the three measures remain open.

## Three measures, not one renamed quantity

For every admissible patch \(U\) of a codimension-two causal cut, construct independently:

1. a horizontal response measure

   $$
   \mu_{\mathrm{BKM}}^\perp(U)
   :=G_{NN,\mathrm{ren}}^\perp[U];
   $$

2. a central edge-entropy measure from the finite-index gravitational correspondence

   $$
   \mu_{\mathrm{edge}}(U)
   :=\mathcal L_{E,U};
   $$

3. a physical spectral area measure

   $$
   \mu_{A,D}(U)
   :=\mathcal A_{D,U}.
   $$

The desired theorem is

$$
\boxed{
\frac{\mathrm d\mu_{\mathrm{BKM}}^\perp}
{\mathrm d\mu_{A,D}}
=
\frac{\mathrm d\mu_{\mathrm{edge}}}
{\mathrm d\mu_{A,D}}
=:\eta_*,}
$$

with one finite positive constant \(\eta_*\) throughout the stated Einstein regime. In operator form, before choosing a central character,

$$
\boxed{
\mathcal L_{E,U}
=\eta_*\mathcal A_{D,U}
\qquad
\text{for every admissible }U.}
$$

The second equation is stronger than matching the total area of one horizon. It tests locality, additivity, and sector independence.

Strictly, \(\mu_{\mathrm{edge}}\) is central-operator-valued before a sector or normal central state is chosen. The Radon--Nikodym equation is therefore to be read sectorwise, or as an equality of central positive operator-valued measures once that theory is supplied. It must not silently treat a stack of sectors as one scalar measure.

If the edge state is also a genuine unit escort thermal channel, [[deriving-value-of-g/noether-capacity-theorem|the Noether--capacity theorem]] can supply

$$
\mu_{\mathrm{BKM}}^\perp(U)
=\mu_{\mathrm{edge}}(U).
$$

That tangent alignment is additional. The finite-index identity by itself relates edge entropy to maximum algebraic capacity and wall defect; it does not identify edge entropy with horizontal BKM capacity.

## Spectral area on a smooth cut

For a closed two-dimensional spin cut with ordinary Dirac spectral triple

$$
(C^\infty(\Sigma),L^2(\Sigma,S),D_\Sigma),
$$

Connes' trace theorem gives, in the standard spinor normalization,

$$
\boxed{
A_D(U)
=2\pi\operatorname{Tr}_\omega
\left(
\pi(1_U)|D_\Sigma|^{-2}
\right).}
$$

For nonsmooth patches, \(1_U\) and the spectral measure require an approximation or measurable-functional-calculus prescription. In a genuinely noncommutative cut, \(\pi(1_U)\) must be replaced by the positive element or projection that defines the context patch.

This formula supplies an area once \(D_\Sigma\) is fixed. It does not fix the absolute length scale of \(D_\Sigma\): under

$$
D_\Sigma\longmapsto\lambda D_\Sigma,
$$

one has

$$
A_D\longmapsto\lambda^{-2}A_D.
$$

The scale of the Dirac operator is therefore precisely where a dimensionful prediction must enter.

## The exact cell model

In one type-I factor cell of [[spectral-wall-descent/finite-index-area-weld|the finite-index area weld]], let

$$
s_*:=S(\chi_*)
$$

be the distinguished edge entropy and let

$$
a_*:=A_D(\text{cell})
$$

be its independently calculated spectral area. For \(K\) mutually independent identical cells,

$$
\mu_{\mathrm{edge}}=Ks_*,
\qquad
\mu_{A,D}=Ka_*.
$$

Hence

$$
\boxed{
\eta_*=\frac{s_*}{a_*},
\qquad
G_{\mathrm{pred}}
=\frac{c^3a_*}{4\hbar s_*}.}
$$

The number of cells cancels. The model is noncircular if \(s_*\) and \(a_*\) are derived without the Bekenstein--Hawking formula, measured \(G\), Planck units, or a fitted cosmological history.

If the edge state is maximally mixed on \(\mathbb C^d\), then

$$
s_*=\log d
=\frac12\log\operatorname{Ind}(E_\tau).
$$

For a nonmaximal edge state,

$$
s_*
=\frac12\log\operatorname{Ind}(E_\tau)
-D(\chi_*\Vert\tau_d).
$$

Thus index determines only a maximum in this model. The unit condition \(s_*=1\) nat would give \(d=e\) under maximal mixing, which is impossible for the literal finite type-I cell because its Hilbert dimension \(d\) is an integer. Interpreting the equation through a continuous categorical index would be a different model and would still require a saturation theorem. No universal \(d=e\) conclusion follows from the Ruble principle.

## A relative prediction from a singlet scale

Pure dimensionless algebra cannot fix \(a_*\). If an independently selected singlet mass \(m_\sigma\) fixes the cut Dirac scale so that

$$
a_*
=C_\sigma
\left(
\frac{\hbar}{m_\sigma c}
\right)^2,
$$

then the genuine prediction is the dimensionless relation

$$
\boxed{
\frac{Gm_\sigma^2}{\hbar c}
=\frac{C_\sigma}{4s_*}.}
$$

This derives \(G\) relative to a separately constructed spectral mass. It does not create a dimensionful constant from dimensionless structure. The singlet mass must itself be selected without using the desired gravitational value.

## Relation to the observable spectral action

The Einstein--Hilbert action can be written

$$
\frac{S_{\mathrm{EH}}}{\hbar}
=\frac{\eta_{\mathrm E}}{4\pi}
\int R\,\mathrm dV.
$$

Therefore the central density theorem predicts the dimensionless curvature stiffness

$$
Z_g=\frac{\eta_*}{4\pi}.
$$

The observable noncommutative Standard Model instead returns

$$
Z_{\mathrm{spec}}
=\frac{96f_2\Lambda^2-f_0c}{24\pi^2}
$$

in its natural-unit convention. Closure requires the independently derived equation

$$
\boxed{
\frac{\eta_*}{4\pi}
=Z_{\mathrm{spec}}.}
$$

This is a testable weld between the correspondence/area construction and the observable spectral action. Using the spectral coefficient to define \(\eta_*\) would reverse the dependency and would not derive \(G\).

## What Connes' volume quantization contributes

[[library/quanta-of-geometry/entry|Quanta of Geometry]] relates a higher Heisenberg relation, an index pairing, and quantized volume. It demonstrates that a Dirac-algebra relation can normalize geometric measure through topology rather than by a classical coordinate lattice.

It does not yet close the present problem. The paper's displayed area and volume quanta are expressed in gravitational or Planck-normalized units, and the construction begins with a manifold and Dirac operator. It can supply a spectral cycle and discreteness grammar; it cannot be imported as a numerical derivation of \(G\) without independently fixing the Dirac scale.

## The noncircular theorem target

A successful proof must establish, in this order:

1. a finite-index noncommutative gravitational expectation \(E_g\) or a controlled type-II analogue;
2. its central relative-commutant edge states \(\chi_{U,\alpha}\);
3. locality and fusion compatibility of \(\mathcal L_{E,U}\);
4. a cut spectral triple and physical normalization of \(D_\Sigma\);
5. the all-patch identity \(\mathcal L_{E,U}=\eta_*\mathcal A_{D,U}\);
6. the same-tangent identity \(\mu_{\mathrm{BKM}}^\perp=\mu_{\mathrm{edge}}\);
7. universality across scalar, tensor, local Newtonian, wave, and horizon sectors; and
8. only then \(G_{\mathrm{pred}}=c^3/(4\hbar\eta_*)\).

Failure is informative. A central density varying by sector predicts non-Einstein coupling; a scale-dependent density predicts a running or scalar--tensor response; a nonlocal measure predicts nonlocal gravity; and absence of a canonical Dirac normalization blocks any numerical value of \(G\).

Primary sources: [the holographic central area operator](https://arxiv.org/abs/2008.04810), [relative entropy and index](https://arxiv.org/abs/1909.01906), [functorial matrix dimension](https://arxiv.org/abs/1805.09234), and [spectral volume quantization](https://arxiv.org/abs/1409.2471).
