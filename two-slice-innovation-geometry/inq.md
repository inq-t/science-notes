---
inq.module: "two-slice-innovation-geometry"
inq.include:
  - "./"
inq.ambient:
  - "**"
---
# Two-Slice Innovation Geometry

A stationary two-slice law has a canonical dimensionless distinction coefficient: its Hirschfeld--Gebelein--Renyi maximal correlation, equivalently the norm of conditional transport on centered \(L^2\). The coefficient is also the Friedrichs cosine of the two endpoint subspaces, the optimal two-block variance-factorization constant is its reciprocal defect, and a complete orthogonal innovation decomposition bounds it by the norm of a scalar influence matrix. This gives a non-density-based local-to-global route to a transfer gap and an exact warning: perfect decorrelation of every proper marginal can still miss an almost conserved global parity mode. The theorem concerns the actual two-slice law; a sampler with the same one-slice state is a different operator.

**Status: [EXACT] for the two-slice norm, round-trip variance, two-block factorization, innovation-matrix theorem, and parity counterexample; [EXACT UNDER THE STATED TRANSFER IDENTIFICATION] for the logarithmic energy edge; [OPEN CONSTRUCTION] for a volume-uniform innovation estimate on the interacting Wilson vacuum law and its continuum transport.**

## A relation comes before its endpoint operator

Let \(\mathsf J\) be a probability law on \(X\times Y\), with marginals
\(\nu_X,\nu_Y\). Its conditional transport is the contraction

$$
(Kf)(x)
:=
\mathbb E_{\mathsf J}[f(Y)\mid X=x],
\qquad
K:L^2(\nu_Y)\longrightarrow L^2(\nu_X).
\tag{TSI1}
$$

Write \(L_0^2\) for the mean-zero subspace. The maximal correlation of the
**whole pair law** is

$$
\boxed{
\rho(\mathsf J)
:=
\sup_{\substack{f\in L_0^2(\nu_Y),\ g\in L_0^2(\nu_X)\\
\|f\|_2=\|g\|_2=1}}
\left|\mathbb E_{\mathsf J}[g(X)f(Y)]\right|
=
\|K|_{L_0^2}\|.}
\tag{TSI2}
$$

No density, diagonal support, reversibility, or stochastic ontology is
assumed. A probability law is one representation of a positive relation
between two presentations; (TSI2) only records how well a centered
distinction in one presentation can survive conditional descent to the
other.

If \(X=Y\), both marginals equal \(\nu\), and \(\mathsf J\) is the stationary
edge law of a Markov operator \(P\), then \(K=P\). Let \(\Pi\) project onto
constants. The canonical return determined by the pair is \(P^*P\), and for
every \(f\perp1\),

$$
\begin{aligned}
\langle f,(I-P^*P)f\rangle_\nu
&=
\|f\|_2^2-\|Pf\|_2^2\\
&=
\mathbb E_{\mathsf J}
\!\left[\operatorname{Var}(f(Y)\mid X)\right].
\end{aligned}
\tag{TSI3}
$$

Consequently,

$$
\boxed{
1-\rho(\mathsf J)^2
=
\inf_{f\perp1}
\frac{\mathbb E[\operatorname{Var}(f(Y)\mid X)]}
{\operatorname{Var}_\nu(f)}.}
\tag{TSI4}
$$

The square belongs to the alternating whole-slice return. It must not be
silently substituted for the one-way defect \(1-\rho\).

The whole pair carrier also factors this defect exactly. Let
$J_X:L^2(\nu_X)\to L^2(\mathsf J)$ and
$J_Y:L^2(\nu_Y)\to L^2(\mathsf J)$ be the endpoint pullback isometries.
Then $K=J_X^*J_Y$, and the residual analysis

$$
L_{Y\mid X}:=(I-J_XJ_X^*)J_Y
\tag{TSI4a}
$$

obeys

$$
\boxed{I-K^*K=L_{Y\mid X}^*L_{Y\mid X}.}
\tag{TSI4b}
$$

Thus conditional variance is literally the squared component of the
$Y$-presentation orthogonal to the $X$-presentation inside the joint whole.
[[transported-response-observability-solder/inq|The transported-response
theorem]] composes these exact residuals, or geometry-derived lower bounds
on them, across changing stages.

There is a stricter three-slice refinement. In a stationary path with
endpoints \(X_0,X_{2n}\),
[[bridge-score-fusion-geometry/inq|the bridge-score analysis]] inserts a
middle observable \(f(X_n)\) and removes everything predictable from both
endpoints:

$$
L_n^{\mathrm{br}}f
=
(I-\mathbb E[\,\cdot\mid X_0,X_{2n}])f(X_n).
$$

Its Gramian is average conditional bridge variance and, reversibly,

$$
0\leq (L_n^{\mathrm{br}})^*L_n^{\mathrm{br}}
\leq I-P^{2n}.
$$

The extra endpoint can only improve prediction, so this fusion-residue
response is generally smaller than the one-ended transfer defect. A uniform
lower frame for it is sufficient for a transfer gap but is not equivalent to
one without further hypotheses.
[[bridge-data-augmentation-solder/inq|Bridge Data-Augmentation Solder]]
identifies its complement as the positive marginal chain \(K_n^*K_n\) of
the middle--endpoint-pair joint law. This makes the bridge lower frame an
ordinary two-component data-augmentation spectral gap with an exact
same-carrier order below physical transfer defect. It also imports the
tensorization theorem correctly: independent link bridges retain the worst
one-link maximal correlation rather than multiplying density-minorization
constants.

If \(P=P^*\), \(0<P\leq I\), and an independently justified transfer
identification gives

$$
P=e^{-\ell(H-E_0)/(\hbar c)},
\tag{TSI5}
$$

then positivity removes the absolute-spectrum ambiguity and

$$
\boxed{
\Delta_E
=
-\frac{\hbar c}{\ell}\log\rho(\mathsf J).}
\tag{TSI6}
$$

Without Hilbert positivity, maximal correlation controls a singular norm;
a negative near-\(-1\) eigenvalue can make \(\rho\) large without approaching
the upper spectral edge of \(P\).

## The angle is exactly a two-block variance constant

Embed endpoint functions isometrically in \(L^2(\mathsf J)\), and let
\(e_X,e_Y\) be conditional expectation onto the two endpoint
sigma-algebras. Let \(R=e_X\wedge e_Y\) project onto their common retained
information and define the reduced Friedrichs cosine

$$
c_F
:=
\|(e_X-R)(e_Y-R)\|.
\tag{TSI7}
$$

On the complement of \(R\), the two-projection theorem gives the sharp pair
edge

$$
2I-e_X-e_Y
\geq
(1-c_F)(I-R).
\tag{TSI8}
$$

Since an orthogonal expectation satisfies

$$
\langle F,(I-e_X)F\rangle
=
\|F-e_XF\|^2,
\tag{TSI9}
$$

(TSI8) is equivalently the two-block variance-factorization inequality

$$
\boxed{
\|F-RF\|^2
\leq
\frac{1}{1-c_F}
\left(
\|F-e_XF\|^2+\|F-e_YF\|^2
\right).}
\tag{TSI10}
$$

In the classical case the two terms on the right are expected conditional
variances. Provided at least one reduced endpoint range
\(\operatorname{Ran}(e_X-R)\) or \(\operatorname{Ran}(e_Y-R)\) is nonzero,
the optimal constant is

$$
C_{\mathrm{var}}^*
=
\frac{1}{1-c_F}.
\tag{TSI11}
$$

For a stationary positive transfer with only constants fixed,
\(c_F=\rho(\mathsf J)\). Therefore the same information can be written

$$
\boxed{
\Delta_E
=
\frac{\hbar c}{\ell}
\log\frac{C_{\mathrm{var}}^*}{C_{\mathrm{var}}^*-1}.}
\tag{TSI12}
$$

At fixed physical \(\ell>0\), a volume-uniform finite factorization constant
is a gap certificate. For adjacent slices with
\(\ell=a_\tau\downarrow0\), an ordinary finite gap instead gives

$$
C_{\mathrm{var}}^*(a_\tau)
\sim
\frac{\hbar c}{a_\tau\Delta_E}.
\tag{TSI13}
$$

Thus demanding a regulator-uniform adjacent-slice constant would impose the
wrong continuum scaling. The invariant is the logarithm per calibrated slab
thickness.

A nontrivial common factor makes the unreduced maximal correlation equal to
one. It must be represented by \(R\) and removed before a vacuum-complement
bound is stated; declaring it absent does not remove a conserved,
topological, gauge, or superselection direction.

## Entropy can certify the angle but is not identical to it

For normalized densities \(h\), suppose the actual joint law obeys a
two-block entropy quasi-factorization

$$
\operatorname{Ent}_{\mathsf J}(h)
-\operatorname{Ent}_{\mathsf J}(Rh)
\leq
C_{\mathrm{ent}}
\sum_{Z\in\{X,Y\}}
\left[
\operatorname{Ent}_{\mathsf J}(h)
-\operatorname{Ent}_{\mathsf J}(e_Zh)
\right].
\tag{TSI14}
$$

Linearizing at \(h=1+\varepsilon F\) gives (TSI10), hence

$$
C_{\mathrm{var}}^*\leq C_{\mathrm{ent}},
\qquad
c_F\leq1-\frac1{C_{\mathrm{ent}}}.
\tag{TSI15}
$$

This is one-way. The Hessian coefficient of a channel-relative-entropy
contraction is \(\rho^2\), but the optimal global relative-entropy
contraction can be strictly larger. Local information geometry, global
convexity, the pair-frame defect \(1-\rho\), and the round-trip defect
\(1-\rho^2\) are four related but distinct quantities. See
[[library/on-maximal-correlation-hypercontractivity-and-the-data-processing-inequality-studied-by-erkip-and-cover/inq|Anantharam--Gohari--Kamath--Nair]] and
[[library/strong-data-processing-inequalities-for-channels-and-bayesian-networks/inq|Polyanskiy--Wu]].

Classical block-factorization theorems provide a serious route when their
hypotheses can be independently verified. In particular,
[[library/block-factorization-of-the-relative-entropy-via-spatial-mixing/inq|Caputo--Parisi]] derive volume-uniform block entropy factorization from
strong spatial mixing for their spin-system class. Applied to the whole path
law with an open interior and overlapping boundary collars, its linearized
inequality leaves exactly the bridge variance on a midpoint observable.
[[three-block-bridge-factorization/inq|Three-Block Bridge Factorization]]
records this direct same-law implication and proves why the superficially
simpler disjoint full-carrier constant must diverge during temporal
refinement. The cited theorem does not cover the Wilson plaquette model or
derive the required scale-aware collared estimate; the associated block
resampling chain remains auxiliary rather than physical time.

## Complete orthogonal innovations give a local-to-global theorem

Choose finite nested endpoint filtrations

$$
\mathbb C1=\mathcal A_0^X\subset\cdots\subset\mathcal A_m^X,
\qquad
\mathbb C1=\mathcal A_0^Y\subset\cdots\subset\mathcal A_n^Y,
\tag{TSI16}
$$

ending in the full endpoint sigma-algebras. Their martingale innovations are

$$
D_i^X
:=
E_{\mathcal A_i^X}-E_{\mathcal A_{i-1}^X},
\qquad
D_j^Y
:=
E_{\mathcal A_j^Y}-E_{\mathcal A_{j-1}^Y}.
\tag{TSI17}
$$

They are orthogonal projections within each endpoint and resolve the
centered carriers:

$$
I-\Pi_X=\sum_iD_i^X,
\qquad
I-\Pi_Y=\sum_jD_j^Y.
\tag{TSI18}
$$

Suppose \(c_{ij}\geq0\) satisfy

$$
\|D_i^XKD_j^Y\|\leq c_{ij},
\qquad
C=(c_{ij}).
\tag{TSI19}
$$

Then the **innovation-matrix theorem** is

$$
\boxed{
\rho(\mathsf J)\leq\|C\|_{\ell^2\to\ell^2}.}
\tag{TSI20}
$$

Indeed, writing \(f=\sum_jf_j\) with \(f_j=D_j^Yf\), orthogonality gives

$$
\begin{aligned}
\|Kf\|^2
&=
\sum_i
\left\|\sum_jD_i^XKD_j^Yf_j\right\|^2\\
&\leq
\sum_i\left(\sum_jc_{ij}\|f_j\|\right)^2\\
&\leq
\|C\|_{2\to2}^2\sum_j\|f_j\|^2.
\end{aligned}
\tag{TSI21}
$$

The bound is optimal given only the scalar block norms: arbitrary Hilbert
block matrices can saturate the norm of their scalar majorant. The Schur
estimate supplies the usable local criterion

$$
\|C\|_2
\leq
\sqrt{
\left(\max_i\sum_jc_{ij}\right)
\left(\max_j\sum_ic_{ij}\right)}.
\tag{TSI22}
$$

If \(c_{ij}\leq r_i\delta_{ij}+d_{ij}\), then

$$
\rho(\mathsf J)
\leq
\max_i r_i+\|D\|_2.
\tag{TSI23}
$$

For at most \(z\) nonzero off-diagonal influences of size \(\delta\) in each
row and column, \(r+z\delta<1\) is sufficient. The diagonal local
contraction \(r<1\) alone is not.

The entries in (TSI19) are correlations of **innovations**, not raw spatial
marginals. A conditional local estimate controls such an entry only when
both innovations are centered relative to the conditioning boundary. In
general,

$$
\mathbb E[uv]
=
\mathbb E[\operatorname{Cov}(u,v\mid\mathcal C)]
+
\operatorname{Cov}
\!\left(\mathbb E[u\mid\mathcal C],\mathbb E[v\mid\mathcal C]\right),
\tag{TSI24}
$$

and the second term is an additional influence channel.

When a two-block decomposition comes with the stronger full-space inequality \(B\ge bQ\), [[projection-conditioned-coercivity|projection-conditioned coercivity]] gives a sharp alternative to estimating a scalar matrix of all cross blocks: \(PBP\ge aP\) and \(0\le B\le I\) imply \(B\ge abI\). [[bridge-data-augmentation-solder/coarse-boundary-leakage-and-response-lifting|Conditional fine-to-coarse bridge lifting]] constructs this hypothesis from the actual discarded-core law and explicitly accounts for fine-boundary predictors omitted by coarsening.

## The hidden-parity obstruction is exact

Let

$$
\Omega_n=\{-1,+1\}^n,
\qquad
\nu_n=\text{uniform},
\qquad
\chi(x)=\prod_{k=1}^nx_k.
\tag{TSI25}
$$

For \(0<\varepsilon<1\), define

$$
P_\varepsilon
=
\Pi+(1-\varepsilon)|\chi\rangle\langle\chi|.
\tag{TSI26}
$$

Its transition density relative to \(\nu_n\) is

$$
p_\varepsilon(x,y)
=
1+(1-\varepsilon)\chi(x)\chi(y)
\geq\varepsilon.
\tag{TSI27}
$$

Thus the kernel has full support, is reversible and Hilbert-positive, and
has only constants fixed. Nevertheless,

$$
\rho(P_\varepsilon)=1-\varepsilon.
\tag{TSI28}
$$

If \(B\subsetneq\{1,\ldots,n\}\) and \(g\) depends only on \(Y_B\), then an
omitted coordinate averages \(\chi\) to zero, so

$$
P_\varepsilon g=\Pi g.
\tag{TSI29}
$$

Every proper output block is therefore independent of the entire input
slice, while the full parity retains correlation \(1-\varepsilon\). Taking
\(\varepsilon_n\downarrow0\) gives perfect proper-block decorrelation and a
vanishing global transfer edge. Strict kernel positivity does not help.

The missing mode reappears when both exteriors are conditioned. Given
\(X_{-i},Y_{-i}\), the conditional pair law is proportional to

$$
1+(1-\varepsilon)
\left(\prod_{k\neq i}X_k\right)
\left(\prod_{k\neq i}Y_k\right)x_iy_i,
\tag{TSI30}
$$

whose conditional correlation has magnitude \(1-\varepsilon\). The
counterexample therefore does not defeat the innovation theorem; it proves
why the filtration must be complete and its boundary influence retained.

The zero eigenvalues of \(P_\varepsilon\) are inessential. Let \(K_r\) be the
injective product binary-noise channel with Walsh eigenvalue \(r^{|S|}\) on
the character indexed by \(S\), where \(0<r<1\), and set

$$
\widetilde P_{\varepsilon,\delta}
:=
(1-\delta)P_\varepsilon+\delta K_r,
\qquad
0<\delta<1.
\tag{TSI30a}
$$

All of its finite-dimensional eigenvalues are strictly positive. Every
proper-block correlation is at most \(\delta r\), while its parity
eigenvalue is

$$
(1-\delta)(1-\varepsilon)+\delta r^n.
\tag{TSI30b}
$$

Taking \(\delta_n,\varepsilon_n\downarrow0\) therefore preserves the
obstruction with an injective strictly Hilbert-positive transfer: local
proper-block correlations vanish while the global contraction tends to one.

It also separates state mixing from transfer contraction. The stationary
one-slice law \(\nu_n\) is a product measure whose ordinary heat-bath sampler
has optimal mixing, even while \(P_\varepsilon\) has an arbitrarily small
edge. A valid comparison needs an additional same-carrier inequality such
as

$$
I-P^*P\geq\eta(I-Q),
\tag{TSI31}
$$

where \(Q\) is the explicitly chosen sampler or auxiliary response. If
\(Q\leq\Pi+(1-\gamma)(I-\Pi)\), then

$$
\rho(P)^2\leq1-\eta\gamma.
\tag{TSI32}
$$

Without (TSI31), sampler mixing and clock transport belong to different
categories.

## The Wilson two-slice target

For a finite Wilson sandwich

$$
T=M_aKM_a,
\qquad
(Kf)(U)=\int k(U,V)f(V)\,\mathrm d\mu(V),
\tag{TSI33}
$$

let \(T\psi=\lambda_0\psi\), \(\psi>0\), and put \(b=a\psi\). The exact Doob
kernel and stationary pair law are

$$
\boxed{
P_T(U,\mathrm dV)
=
\frac{k(U,V)b(V)}{(Kb)(U)}\,\mathrm d\mu(V),}
\tag{TSI34}
$$

$$
\boxed{
\mathrm d\mathsf J_T(U,V)
=
\lambda_0^{-1}b(U)k(U,V)b(V)
\,\mathrm d\mu(U)\mathrm d\mu(V).}
\tag{TSI35}
$$

If \(k(U,V)=\prod_e k_e(U_e,V_e)\), then, conditional on both exteriors,
the pair law in a spatial block \(B\) is proportional to

$$
b(U_B,U_{B^c})b(V_B,V_{B^c})
\prod_{e\in B}k_e(U_e,V_e)
\,\mathrm d\mu_B(U_B)\mathrm d\mu_B(V_B).
\tag{TSI36}
$$

The kinetic cross-slice factors are explicit. The unresolved factor is the
Perron dressing \(b=a\psi\), which can transmit nonlocal vacuum dependence.
This is why a product-kernel estimate, isolated block marginal, or global
minimum-to-maximum density ratio does not settle the interacting problem.

The sharp direct program is to use a complete gauge-invariant innovation
filtration for the **actual** law (TSI35) and prove

$$
\|C_{a,L}(\ell_*)\|_2\leq q_*<1
\tag{TSI37}
$$

uniformly in volume and admissible boundary or flux sector at a fixed
positive physical thickness \(\ell_*\). For adjacent slices the correctly
scaled stopping condition is

$$
\boxed{
\liminf_{a\downarrow0}\inf_L
\frac{\hbar c}
{a_{\tau,a}\Lambda_{\mathrm{YM}}^{(\mathsf s)}}
\,\bigl[-\log\|C_{a,L}(a_{\tau,a})\|_2\bigr]
>0.}
\tag{TSI38}
$$

Gauge invariance is not decorative, but the finite-regulator kinematic step
is now closed. [[gauge-cycle-innovation-filtration/inq|Gauge-Cycle Innovation
Filtration]] proves that conditional expectation onto any edge-subgraph
sigma-algebra commutes with the gauge action. Ordering a spanning tree first
makes all tree-stage physical innovations vanish; the subsequent chord
innovations resolve the complete gauge-invariant carrier. In maximal-tree
coordinates they are the joint cycle-holonomy filtration modulo residual
simultaneous conjugation. What remains open is the estimate in (TSI37), not
the existence of a physical filtration. Boundary frames and edge modes may
still be needed to make that estimate local, and common superselection data
must be retained in \(R\) rather than averaged away.

An alternative theorem route uses a scale-aware block variance
factorization, uniform conditional block edges, and a genuine physical
same-carrier form comparison. If

$$
\gamma(\alpha)\operatorname{Var}_\nu f
\leq
C_r\sum_A\alpha_A\,\nu[\operatorname{Var}_A f],
\tag{TSI39}
$$

each conditional block response has centered norm at most \(r_r<1\), and

$$
\langle f,(I-P_T)f\rangle
\geq
\theta_r\sum_A\alpha_A\,
\nu\!\left[\langle f,(I-K_{A\mid A^c})f\rangle_A\right],
\tag{TSI40}
$$

then

$$
1-\|P_T|_{L_0^2}\|
\geq
\frac{\theta_r(1-r_r)\gamma(\alpha)}{C_r}.
\tag{TSI41}
$$

The normalization of the weights must be included if they define a random
block update. Equation (TSI40), not the existence of a good auxiliary
sampler, is the missing physical solder.

## Copernican reading

The primitive object in this module is the whole relation \(\mathsf J\), not
a mass placed inside a pre-existing spatial box. The endpoint algebras are
two presentations of that relation. Conditional expectation is genuinely
noninvertible on the joint carrier, and conditional variance measures what
each presentation forgets. Their relative angle determines how much of a
noncommon distinction can survive both descents.

That does **not** mean a nonunitary whole time evolution produces a unitary
local evolution by restriction. The arrows have different types:

$$
\begin{gathered}
\text{whole two-slice relation}
\longrightarrow
\text{noninvertible endpoint expectations},\\
\text{supported positive transfer}
\longrightarrow
\text{Euclidean attenuation generator},\\
\text{OS/Poincare reconstruction}
\longrightarrow
\text{local Lorentzian unitary clock group}.
\end{gathered}
\tag{TSI42}
$$

Something is forgotten in the first arrow; no finite-depth kernel is needed
in the second; reversible clock grammar appears only in the third. This is a
precise form of the proposed reversal. It remains a mass-gap theorem only
after (TSI37) or (TSI40) is proved from Yang--Mills data, the carriers and
vacua converge, and the reconstructed generator is identified with the
physical Poincare energy--mass spectrum.

## Sources and dependencies

- [[library/on-measures-of-dependence/inq|Renyi]] introduces maximal correlation.
- [[library/on-sequences-of-pairs-of-dependent-random-variables/inq|Witsenhausen]] proves exact tensorization for independent pairs.
- [[library/on-maximal-correlation-hypercontractivity-and-the-data-processing-inequality-studied-by-erkip-and-cover/inq|Anantharam--Gohari--Kamath--Nair]] identify the local information-geometric coefficient and refute its unqualified promotion to a global information contraction.
- [[library/strong-data-processing-inequalities-for-channels-and-bayesian-networks/inq|Polyanskiy--Wu]] compare fixed-input \(\chi^2\), maximal-correlation, and relative-entropy contraction coefficients.
- [[library/approximate-tensorization-of-entropy-at-high-temperature/inq|Caputo--Menz--Tetali]] and [[library/block-factorization-of-the-relative-entropy-via-spatial-mixing/inq|Caputo--Parisi]] supply classical conditional-to-global entropy precedents.
- [[past-future-angle-and-the-transfer-gap]] supplies the stationary path-space and logarithmic-transfer realization.
- [[reverse-prediction-residue-archive/inq|Reverse-Prediction Residue Archive]] resolves the two-slice defect into the orthogonal innovations of a nested future filtration and states the finite-slab stopping condition.
- [[bridge-data-augmentation-solder/inq|Bridge Data-Augmentation Solder]] identifies the bridge form with the positive marginal chain of the middle--boundary-pair Gibbs update and proves its product and gauge-restriction laws.
- [[three-block-bridge-factorization/inq|Three-Block Bridge Factorization]] turns collared whole-spacetime block factorization into a bridge floor and proves that the disjoint full-carrier constant has the wrong continuum scaling.
- [[gaussian-bridge-gap-calibration/inq|Gaussian Bridge-Gap Calibration]] proves the exact free-field identity \(\kappa_{\rm br}(\ell)=\tanh(\omega\ell)\).
- [[markov-edge-measure-solder/inq|Markov Edge-Measure Solder]] supplies a complementary two-slice form-comparison route.
- [[gauge-cycle-innovation-filtration/inq|Gauge-Cycle Innovation Filtration]] supplies the exact finite Wilson physical filtration and its pure-kinetic calibration.

[[two-slice-innovation-geometry/receipts/two_slice_innovation_receipt.py|The finite receipt]]
checks the sharp pair factor, a saturated product-channel innovation bound,
and the hidden-parity obstruction. It is an identity check, not evidence for
the Wilson continuum estimate.
[[two-slice-innovation-geometry/receipts/two-slice-innovation-receipt-output.txt|The stored output]]
records the checked values.
