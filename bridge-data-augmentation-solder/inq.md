---
inq.module: "bridge-data-augmentation-solder"
inq.include:
  - "./"
inq.ambient:
  - "**"
---
# Bridge Data-Augmentation Solder

The conditional bridge Gramian is exactly the Dirichlet form of a canonical
positive Markov operator obtained by alternating between a middle slice and
its two boundary slices. This auxiliary data-augmentation chain is not the
physical clock transfer, but its defect is bounded above by the physical
round-trip transfer defect on the same slice carrier. Its spectral gap
therefore gives a valid sufficient transfer-gap certificate. Unlike a global
density minorization, its maximal-correlation coefficient tensorizes by a
maximum, so a product of link bridges retains the worst one-link angle rather
than multiplying one small constant per link. Complete gauge innovations
then turn the interacting problem into a subunit block-matrix estimate for
the actual Wilson bridge law.

**Status: [EXACT] for the data-augmentation factorization, fixed-space
criterion, physical upper solder, product tensorization, gauge restriction,
and complete-innovation bound; [EXACT AT FINITE REGULATOR] for the
pure-product link application; [OPEN] for the volume-, sector-, and
regulator-uniform interacting Wilson innovation estimate and its continuum
reconstruction.**

## The boundary pair is a second component

Let \((X_j)_{j\in\mathbb Z}\) be a stationary Markov path with invariant law
\(\nu\). Fix \(n\geq1\), put

$$
Y:=X_n,
\qquad
Z:=(X_0,X_{2n}),
\tag{DA1}
$$

and let \(\mathsf R_n\) be the joint law of \((Y,Z)\). Its marginals are
\(\nu\) and the endpoint-pair law \(\mathsf J_{0,2n}\). The conditional
transport from middle observables to endpoint observables is

$$
\begin{aligned}
K_n &:L^2(\nu)\longrightarrow L^2(\mathsf J_{0,2n}),\\
(K_nf)(x,z)
&:=
\mathbb E[f(X_n)\mid X_0=x,X_{2n}=z].
\end{aligned}
\tag{DA2}
$$

If \(J_Y\) and \(J_Z\) embed the two component carriers into
\(L^2(\mathsf R_n)\), then

$$
K_n=J_Z^*J_Y.
\tag{DA3}
$$

Consequently the bridge-score Gramian from
[[bridge-score-fusion-geometry/inq|Bridge-Score Fusion Geometry]] is

$$
\boxed{
B_n^{\mathrm{br}}
=
I-K_n^*K_n.}
\tag{DA4}
$$

This identity retypes the lower-frame problem. It asks whether the two
boundaries can almost perfectly reconstruct a nonfixed middle distinction.
It does not ask whether a bridge fiber has nonzero dimension or whether its
density is pointwise positive.

## Alternating conditional presentation gives a positive chain

Disintegrate the same joint law in both directions:

$$
\mathsf R_n(\mathrm dy,\mathrm dz)
=
\nu(\mathrm dy)\,\alpha_y(\mathrm dz)
=
\mathsf J_{0,2n}(\mathrm dz)\,\beta_z(\mathrm dy).
\tag{DA5}
$$

Here \(\alpha_y\) is the conditional endpoint-pair law given the middle and
\(\beta_z\) is the conditional bridge law. Define

$$
S_n:=K_n^*K_n.
\tag{DA6}
$$

Then \(S_n\) is a self-adjoint Hilbert-positive Markov contraction on
\(L^2(\nu)\), with transition kernel

$$
\boxed{
S_n(y,\mathrm dy')
=
\int
\alpha_y(\mathrm dz)\,
\beta_z(\mathrm dy').}
\tag{DA7}
$$

Operationally, one samples a boundary pair compatible with \(y\), then a
new middle value compatible with that boundary pair. This is the marginal
chain of a two-component Gibbs or data-augmentation update. The terminology
describes an exact factorization of conditional expectations; it makes no
claim that stochastic sampling is fundamental ontology.

For every \(f\in L^2(\nu)\),

$$
\boxed{
\langle f,(I-S_n)f\rangle_\nu
=
\mathbb E\!\left[
\operatorname{Var}(f(Y)\mid Z)
\right].}
\tag{DA8}
$$

Thus

$$
B_n^{\mathrm{br}}=I-S_n.
\tag{DA9}
$$

The fixed space is also exact:

$$
\boxed{
\ker(I-S_n)
=
\left\{
f\in L^2(\nu):
f(Y)=g(Z)\ \mathsf R_n\text{-a.s. for some }g
\right\}.}
\tag{DA10}
$$

Indeed, equality \(\|K_nf\|=\|f\|\) holds exactly when the orthogonal
projection of \(J_Yf\) onto the endpoint subspace loses no norm, which is
equivalent to \(J_Yf\in\operatorname{Ran}J_Z\). A nonconstant element of
(DA10) is a perfectly boundary-recoverable middle \(L^2\)-distinction and is an exact
obstruction to a bridge lower frame.

In finite dimension, or whenever the centered conditional transport is
compact, absence of such a common factor implies a strict finite-system
angle. It does not imply a uniform angle along a thermodynamic or continuum
sequence: the top centered singular value may approach one without ever
attaining one.

The exact quantitative condition is

$$
\boxed{
\|K_nQ\|<1,}
\tag{DA10a}
$$

or a regulator-uniform version of it. A transfer gap and the qualitative
identity \(\ker(I-S_n)=\operatorname{Ran}\Pi_{\rm fix}\) still do not imply
(DA10a): positive reversible high-girth expander chains can mix strongly
one-endedly while two endpoints recover the middle with probability tending
to one. [[three-block-bridge-factorization/inq|Three-Block Bridge
Factorization]] records this no-go and the relative quasi-factorization that
measures the missing two-ended synergy.

## Why this auxiliary chain can constrain physical transfer

For a general stationary path, projection order gives

$$
S_n
\geq
(P^*)^nP^n,
\qquad
S_n
\geq
P^n(P^*)^n.
\tag{DA11}
$$

When \(P=P^*\),

$$
\boxed{P^{2n}\leq S_n\leq I.}
\tag{DA12}
$$

The auxiliary chain retains at least as much middle information as either
one-ended \(n\)-step prediction, because it is allowed to inspect both
endpoints. Equivalently,

$$
0\leq I-S_n\leq I-P^{2n}.
\tag{DA13}
$$

This same-carrier order is what distinguishes \(S_n\) from an arbitrary
sampler having invariant law \(\nu\). If

$$
I-S_n\geq\kappa Q,
\qquad
Q:=I-\Pi_{\operatorname{Fix}(P)},
\tag{DA14}
$$

then

$$
\|P^nQ\|\leq\sqrt{1-\kappa}.
\tag{DA15}
$$

For

$$
P=e^{-a_\tau(H-E_0)/(\hbar c)},
\qquad
n(a)a_{\tau,a}\longrightarrow\ell_*>0,
\tag{DA16}
$$

a regulator-uniform \(\kappa_*>0\) yields

$$
\Delta_E
\geq
-\frac{\hbar c}{2\ell_*}\log(1-\kappa_*).
\tag{DA17}
$$

The data-augmentation chain does not replace physical transfer. Its
Dirichlet form is a rigorously dominated response whose independently proved
coercivity would force transfer coercivity.

## An edge-measure comparison isolates the temporal solder

The stationary edge measure of \(S_n\) is determined entirely by the bridge
family:

$$
\boxed{
\mathsf M_n(\mathrm dy,\mathrm dy')
:=
\int
\beta_z(\mathrm dy)\beta_z(\mathrm dy')
\,\mathsf J_{0,2n}(\mathrm dz).}
\tag{DA17a}
$$

It is symmetric, has both marginals equal to \(\nu\), and represents (DA7).
Let \(D\geq0\) independently generate a conservative reversible Markov
semigroup on the same \(L^2(\nu)\) carrier, put

$$
Q_\tau:=e^{-\tau D},
\tag{DA17b}
$$

and let \(\mathsf J_{Q_\tau}\) be its stationary edge measure. If their
off-diagonal parts obey the measure order

$$
\mathsf M_n^\circ
\geq
\eta\,\mathsf J_{Q_\tau}^\circ,
\qquad
\eta>0,
\tag{DA17c}
$$

then the
[[markov-edge-measure-solder/inq|Markov Edge-Measure Solder]] gives

$$
\boxed{
I-S_n
\geq
\eta(I-e^{-\tau D}).}
\tag{DA17d}
$$

If \(D\) has the same fixed projection and

$$
D\geq\lambda_DQ,
\qquad
\lambda_D>0,
\tag{DA17e}
$$

then the bridge floor is

$$
\boxed{
\kappa_n
\geq
\eta\left(1-e^{-\tau\lambda_D}\right).}
\tag{DA17f}
$$

This factorization separates two obligations that must not be conflated.
Conditional Poincare plus subcritical Dobrushin influence for the actual
vacuum law can provide a lower bound for \(\lambda_D\). It cannot provide
the temporal comparison coefficient \(\eta\), which must come from the
actual bridge edge \(\mathsf M_n\), raw transfer kernels, or independently
normalized RG data.

The separation is necessary. On a uniform product bit space, the one-slice
heat-bath sampler has perfect tensorization. Yet the positive parity
transfer with density

$$
p_a(x,y)=1+a\chi(x)\chi(y),
\qquad
0<a<1,
\tag{DA17g}
$$

has bridge floor on the parity mode

$$
\frac{1-a^2}{1+a^2}
\longrightarrow0
\qquad
(a\uparrow1).
\tag{DA17h}
$$

One-slice geometry alone therefore cannot imply (DA17c). The bridge
edge-measure order, or an equivalent same-carrier form comparison, is the
load-bearing temporal solder.

## Product bridges tensorize by a maximum

Let \(\mathsf R_i\) be independent middle--boundary joint laws, with
conditional transports \(K_i\), centered maximal correlations

$$
\rho_i:=\|K_i|_{L_0^2}\|<1,
\tag{DA18}
$$

and bridge floors \(\kappa_i:=1-\rho_i^2\). For their finite product,

$$
K=\bigotimes_iK_i.
\tag{DA19}
$$

Maximal correlation tensorization gives

$$
\boxed{
\rho\!\left(\bigotimes_i\mathsf R_i\right)
=
\max_i\rho_i,
\qquad
\kappa\!\left(\bigotimes_i\mathsf R_i\right)
=
\min_i\kappa_i.}
\tag{DA20}
$$

This is the decisive improvement over multiplying pointwise density
minorization constants. If each bridge fiber obeys

$$
\beta_{i,z_i}\geq\varepsilon_i\nu_i,
\tag{DA21}
$$

then \(\kappa_i\geq\varepsilon_i\), and therefore

$$
\kappa_{\mathrm{product}}\geq\min_i\varepsilon_i.
\tag{DA22}
$$

The direct product minorization would retain only
\(\prod_i\varepsilon_i\). Its exponential volume deterioration is a defect
of that certificate, not of the Hilbert angle.

For identical links,

$$
\rho_{\mathrm{product}}=\rho_{\mathrm{link}},
\qquad
\kappa_{\mathrm{product}}=\kappa_{\mathrm{link}},
\tag{DA23}
$$

at every finite volume.

## Gauge restriction cannot worsen a proved raw-link floor

Suppose compact gauge groups act on the middle and endpoint carriers,
preserve \(\mathsf R_n\), and the two actions make \(K_n\) equivariant. Then
\(S_n=K_n^*K_n\) preserves the gauge-invariant middle carrier. Restricting a
quadratic-form inequality to a closed invariant subspace gives

$$
(I-S_n)\big|_{\mathcal H_{\mathrm{GI}}}
\geq
\kappa
\left(I-\Pi_{\mathbf1}\right)\big|_{\mathcal H_{\mathrm{GI}}}
\tag{DA24}
$$

whenever the raw carrier has the same lower bound. Thus a product-link
bridge floor survives Gauss projection. It may improve because open charged
one-link modes are removed and the first physical excitation may require a
closed spin-network support.

For a pure kinetic Wilson transfer, the link path laws are independent
before gauge restriction. A strictly positive continuous one-link kernel on
a compact group gives a compact conditional transport with no nonconstant
common factor, hence a positive finite-regulator \(\kappa_{\mathrm{link}}\).
Equations (DA20) and (DA24) make this floor volume independent. This is a
finite-regulator calibration, not a continuum result: the one-link angle
may close along the weak-bare-coupling trajectory, and its logarithmic rate
still requires physical scaling.

## Complete innovations localize the interacting target

For the interacting Wilson/Perron path law, product tensorization is no
longer available. Choose complete orthogonal innovation resolutions

$$
Q_M=\sum_iD_i^M,
\qquad
Q_\partial=\sum_jD_j^\partial
\tag{DA25}
$$

on the middle and endpoint-pair carriers after retaining any common
superselection algebra explicitly. Suppose

$$
\|D_j^\partial K_nD_i^M\|\leq c_{ji},
\qquad
C=(c_{ji}).
\tag{DA26}
$$

The complete innovation-matrix theorem gives

$$
\|K_nQ_M\|\leq\|C\|_{2\to2}.
\tag{DA27}
$$

Consequently,

$$
\boxed{
I-S_n
\geq
\left(1-\|C\|_{2\to2}^2\right)Q_M.}
\tag{DA28}
$$

If row and column sums are easier to estimate,

$$
\|C\|_2
\leq
\sqrt{
\left(\sup_j\sum_i c_{ji}\right)
\left(\sup_i\sum_j c_{ji}\right)}.
\tag{DA29}
$$

The correct Yang--Mills blocks are not independently gauge-closed spatial
regions. [[gauge-boundary-frame-gluing/inq|Gauge Boundary Frames and Gauss
Gluing]] requires open regional charge sectors to be paired before global
closure, while
[[vacuum-aligned-innovation-completion/inq|Vacuum-Aligned Innovation
Completion]] adds the balance sector omitted by internal block centering.
[[gauge-cycle-innovation-filtration/inq|Gauge-Cycle Innovation Filtration]]
supplies a complete finite-slice resolution by relational cycle closure.

Let \(C_{a,L,\mathsf s}^{\mathrm{br}}(\ell_*)\) be the resulting complete
middle-to-boundary bridge matrix for the actual vacuum-prepared Wilson path
in sector \(\mathsf s\). The sharpened stopping condition is

$$
\boxed{
\sup_{\substack{a<a_0,\ L,\ \mathsf s}}
\left\|
C_{a,L,\mathsf s}^{\mathrm{br}}(\ell_*)
\right\|_2
\leq
q_*<1.}
\tag{DA30}
$$

It implies

$$
\kappa_*\geq1-q_*^2,
\qquad
\Delta_E
\geq
-\frac{\hbar c}{\ell_*}\log q_*.
\tag{DA31}
$$

This target is localizable without becoming local in the naive sense:
every row and column belongs to a piece of a complete whole-carrier
resolution, and boundary-charge plus balance channels are mandatory.

## What has and has not been reduced

The bridge lower-frame problem has become the spectral-gap problem of a
canonical auxiliary chain determined by the actual three-slice path law.
That statement is useful because:

1. the chain is automatically positive and self-adjoint;
2. its defect is exactly the fusion/bridge response;
3. its defect is already soldered below the physical transfer defect;
4. its maximal correlation tensorizes on independent links; and
5. complete innovations provide a non-global comparison target when
   interactions break the product.

It has not become easy. Proving (DA30) still requires control of the Perron
vacuum dressing at a fixed physical block scale. Alternatively one may
prove (DA17c) and a uniform auxiliary-generator edge, or prove a block
factorization on the full spacetime law using overlapping boundary collars
of fixed physical width.
A one-slice heat-bath gap, strict positivity at each finite volume, an
unconditioned local marginal, or assumed exponential clustering cannot
replace these temporal estimates. The continuum proof must also construct
the limiting carrier and OS/Poincare representation.

The Copernican content is typed rather than metaphorical. The whole
middle--boundary relation comes first. Its two conditional-expectation
projections on the joint carrier are noninvertible when their orthogonal
residues are nonzero; the induced maps \(K_n\) and \(S_n=K_n^*K_n\) need not
themselves have kernels. The positive operator \(S_n\) measures boundary
recoverability of middle distinctions. Under full OS reconstruction, a later
strongly continuous unitary group acts on the physical Hilbert carrier and
its adjoint action implements observable automorphisms; it is not the inverse
of either conditional presentation.

[[algebra/os-descent-naturality-and-clock-no-go|The idempotent-clock no-go]]
sharpens this: only the joint-carrier conditional projections are
idempotent, and any literal unitary factor of either projection is the
identity. The positive recovery operator \(S_n\) could itself be unitary only
if \(S_n=I\), equivalently if the bridge residue vanished. Nontrivial clock
unitarity must therefore belong to the distinct reconstructed action.

## Sources and dependencies

- [[library/covariance-structure-of-the-gibbs-sampler-with-applications-to-the-comparisons-of-estimators-and-augmentation-schemes/inq|Liu--Wong--Kong]] identify the marginal data-augmentation convergence operator with the square of maximal correlation and compare a component with grouped conditioning data.
- [[library/on-sequences-of-pairs-of-dependent-random-variables/inq|Witsenhausen]] supplies maximal-correlation tensorization for independent pairs.
- [[two-slice-innovation-geometry/inq|Two-Slice Innovation Geometry]] supplies the complete innovation-matrix theorem and the hidden-parity warning.
- [[bridge-score-fusion-geometry/inq|Bridge-Score Fusion Geometry]] supplies the bridge score, Fisher Gramian, and physical transfer upper solder.
- [[markov-edge-measure-solder/inq|Markov Edge-Measure Solder]] turns a bridge-resampling edge-measure comparison into a bounded same-carrier form inequality without taking the unknown spectrum first.
- [[three-block-bridge-factorization/inq|Three-Block Bridge Factorization]] shows that collared whole-slab block variance or entropy factorization leaves exactly the bridge variance on a midpoint observable, while the disjoint full-carrier constant is forced to diverge under temporal refinement.
- [[gaussian-bridge-gap-calibration/inq|Gaussian Bridge-Gap Calibration]] computes the optimal bridge floor as \(\tanh(\omega\ell)\) and recovers the inverse-length gap exactly in the free Gaussian sector.

[[bridge-data-augmentation-solder/receipts/bridge_data_augmentation_receipt.py|The finite receipt]]
checks the positive marginal chain, its squared-maximal-correlation spectrum,
physical domination, product tensorization, global-minorization failure, and
improvement under a three-link \(\mathbb Z_2\) gauge-cycle restriction.
[[bridge-data-augmentation-solder/receipts/bridge-data-augmentation-receipt-output.txt|The stored output]]
records the checked values.
