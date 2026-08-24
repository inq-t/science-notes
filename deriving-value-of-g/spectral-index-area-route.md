# The Spectral Index--Area Route to \(G\)

The finite-index route derives \(G\) only if algebraically selected, correspondence-compatible edge states define a central assignment with a universal density relative to independently normalized spectral area, and the independently normalized physical scale tangent has the same local BKM density. This replaces a verbal information--gravity identification by an all-patch operator identity. The product-edge entropy per cell is calculable in finite models; state selection, additivity, dimensional spectral area, and the equality of the three assignments remain open.

## Three candidate assignments, not one renamed quantity

For every admissible patch \(U\) of a codimension-two causal cut, construct independently:

1. a horizontal response measure

   $$
   \mu_{\mathrm{BKM}}^\perp(U)
   :=G_{NN,\mathrm{ren}}^\perp[U];
   $$

2. a central edge-entropy assignment from fixed edge states supplied separately with the exact code, Q-system, or expectation data and proved compatible with the correspondence

   $$
   \mu_{\mathrm{edge}}(U)
   :=\mathcal L_{\chi,U};
   $$

3. a physical spectral area measure

   $$
   \mu_{A,D}(U)
   :=\mathcal A_{D,U}.
   $$

Before countable additivity and compatible restriction maps are proved, these are candidate assignments rather than measures. The desired theorem is

$$
\boxed{
\frac{\mathrm d\mu_{\mathrm{BKM}}^\perp}
{\mathrm d\mu_{A,D}}
=
\frac{\mathrm d\mu_{\mathrm{edge}}}
{\mathrm d\mu_{A,D}}
=:\eta_*,}
$$

with one finite positive constant \(\eta_*\) throughout the stated Einstein regime. For the operator form, one must first place all patch centers in a fixed central algebra or provide compatible maps among them. With sector projections \(P_\alpha\), define

$$
\mathcal A_D^Z(U)
:=\sum_\alpha A_{D,\alpha}(U)P_\alpha.
$$

Then, before choosing a central character, the theorem target is

$$
\boxed{
\mathcal L_{\chi,U}
=\eta_*\mathcal A_D^Z(U)
\qquad
\text{for every admissible }U.}
$$

The second equation is stronger than matching the total area of one horizon. It tests locality, additivity, compatible center transport, and sector independence.

Strictly, \(\mu_{\mathrm{edge}}\) is central-operator-valued before a sector or normal central state is chosen. The Radon--Nikodym equation is therefore to be read sectorwise, or as an equality of central positive operator-valued measures only after additivity and center compatibility are supplied. It must not silently treat a prestack of sectors as one scalar measure.

If the edge state is also a genuine unit escort thermal channel, [[deriving-value-of-g/noether-capacity-theorem|the Noether--capacity theorem]] can supply

$$
\mu_{\mathrm{BKM}}^\perp(U)
=\mu_{\mathrm{edge}}(U).
$$

That tangent alignment is additional. The type-I product-edge identity by itself relates a chosen input edge entropy to the log-dimension of its erased factor and its tracial defect; it neither selects the code edge state nor identifies edge entropy with horizontal BKM capacity.

## Spectral area on a smooth cut

For a closed two-dimensional spin cut with ordinary Dirac spectral triple

$$
(C^\infty(\Sigma),L^2(\Sigma,S),D_\Sigma),
$$

Declare \([D_\Sigma]=L^{-1}\), let \(P_0\) project onto its zero modes, and write

$$
|D_\Sigma|^{-2}_0
:=(1-P_0)|D_\Sigma|^{-2}.
$$

For a smooth patch surrogate \(a_U\), Connes' trace theorem gives, in the irreducible standard spinor normalization,

$$
\boxed{
A_D(U)
=\frac{2\pi}{m_{\mathrm{sp}}}\operatorname{Tr}_\omega
\left(
\pi(a_U)|D_\Sigma|^{-2}_0
\right).}
$$

Here \(m_{\mathrm{sp}}\) removes only identical spectator copies relative to the irreducible geometric triple; it equals one when no such amplification is present. The operator must be Dixmier measurable so that the value is independent of the generalized limit. For a sharp nonsmooth patch, \(1_U\) requires a declared approximation or measurable-functional-calculus prescription. In a genuinely noncommutative cut, \(a_U\) must be the positive element or projection that defines the context patch.

This formula supplies an area once \(D_\Sigma\) is fixed. It does not fix the absolute length scale of \(D_\Sigma\): under

$$
D_\Sigma\longmapsto\lambda D_\Sigma,
$$

one has

$$
A_D\longmapsto\lambda^{-2}A_D.
$$

The scale of the Dirac operator is therefore precisely where a dimensionful prediction must enter. Spectator or Morita-equivalent amplification is another normalization gate: \(D^{\oplus m}\) preserves Connes distance but multiplies the raw Dixmier trace by \(m\), so the area prescription must be amplification invariant or prove that the multiplicity is physical.

## The exact cell model

In one type-I factor cell of [[spectral-wall-descent/finite-index-area-weld|the finite-index area weld]], let

$$
s_*:=S(\chi_*)
$$

be the entropy of an edge state selected algebraically before any area matching, and let

$$
a_*:=A_D(\text{cell})
$$

be the independently calculated spectral area of the cell assigned to it by a canonical correspondence-to-patch map. For \(K\) mutually independent identical product cells with no sector mixing,

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

The number of cells cancels. The model is noncircular only if \(s_*\), the cell decomposition, the scale-tangent normalization, and \(a_*\) are derived without the Bekenstein--Hawking formula, measured \(G\), Planck units, or a fitted cosmological history.

If the edge state is maximally mixed on \(\mathbb C^d\), then

$$
s_*=\log d
=\frac12\log\operatorname{Ind}_{W}(E_\tau).
$$

For a nonmaximal edge state,

$$
s_*
=\frac12\log\operatorname{Ind}_{W}(E_\tau)
-D(\chi_*\Vert\tau_d).
$$

These formulas compare \(\chi_*\) with the auxiliary tracial expectation on the same product edge factor; the code expectation selecting \(\chi_*\) is generally different. The half-index fixes the upper bound \(\log d\) on edge-state entropy in this model, not the full subalgebra relative-entropy capacity.

The unit condition \(s_*=1\) nat would give \(d=e\) only under maximal mixing, which is impossible for a literal finite type-I cell because \(d\) is an integer. A nonmaximally mixed state can have one nat of entropy when \(d\geq3\), so the condition can constrain \(\chi_*\) without fixing \(d\). A finite fusion-category dimension is algebraic and likewise cannot equal the transcendental number \(e\). An unrestricted infinite-depth \(\mathrm{II}_1\) subfactor may have Jones index \(e^2>4\), but that alone supplies no equality between edge entropy and log categorical dimension. No universal \(d=e\) conclusion follows from the Ruble principle.

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

The observable noncommutative Standard Model instead returns, in natural units with \(\Lambda\) and Majorana entries treated as inverse lengths,

$$
Z_{\mathrm{spec}}
=\frac{96f_2\Lambda^2-f_0c_{\mathrm{NCG}}}{24\pi^2},
\qquad
c_{\mathrm{NCG}}
:=\operatorname{Tr}(M_R^*M_R),
$$

where \(c_{\mathrm{NCG}}\) is not the speed of light. If \(\Lambda\) and \(M_R\) are expressed as energies instead, the right-hand side must be divided by \((\hbar c)^2\) to have units \(L^{-2}\). Closure requires the independently derived equation

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

1. a finite-index noncommutative gravitational expectation \(E_g\) or a controlled type-II analogue, including the Q-system or standard-solution data that determine it;
2. algebraically selected relative-commutant edge states \(\chi_{U,\alpha}\), fixed throughout each exact-code sector before any area matching;
3. locality, additivity, center transport, and fusion or Markov compatibility of \(\mathcal L_{\chi,U}\);
4. a canonical assignment from each correspondence cell to a spectral patch, preventing arbitrary refinement or fitted cell size;
5. a cut spectral triple and physical normalization of \(D_\Sigma\), including zero modes and spectator multiplicity;
6. invariance of the area density under spectator amplification and Morita-equivalent presentation, unless the multiplicity is independently proved physical;
7. the all-patch identity \(\mathcal L_{\chi,U}=\eta_*\mathcal A_D^Z(U)\);
8. an independently normalized physical scale tangent and the same-tangent identity \(\mu_{\mathrm{BKM}}^\perp=\mu_{\mathrm{edge}}\);
9. universality across scalar, tensor, local Newtonian, wave, and horizon sectors; and
10. only then \(G_{\mathrm{pred}}=c^3/(4\hbar\eta_*)\).

Failure is informative. A central density varying by sector predicts non-Einstein coupling; a scale-dependent density predicts a running or scalar--tensor response; a nonlocal measure predicts nonlocal gravity; and absence of a canonical Dirac normalization blocks any numerical value of \(G\).

Primary sources: [the holographic central area operator](https://arxiv.org/abs/2008.04810), [relative entropy and index](https://arxiv.org/abs/1909.01906), [functorial matrix dimension](https://arxiv.org/abs/1805.09234), and [spectral volume quantization](https://arxiv.org/abs/1409.2471).
