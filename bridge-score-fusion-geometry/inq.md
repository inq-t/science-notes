---
inq.module: "bridge-score-fusion-geometry"
inq.include:
  - "./"
inq.ambient:
  - "**"
---
# Bridge-Score Fusion Geometry

A two-step Markov path disintegrates over its endpoints into conditional
bridge fibers. In the commutative pointed-GNS fusion, the composite cyclic
line is the constant direction in each bridge fiber and the fusion residue
is exactly its conditional-mean-zero complement. Bridge scores and
half-density derivatives therefore give canonical residue vectors. More
strongly, insertion of a complete middle-slice observable gives a bounded
history-sensitive analysis on the full slice \(L^2\) carrier whose Gramian
is dominated by the physical transfer defect. Perron factors cancel from
each conditional bridge but not from the endpoint law or global Hilbert
norm, and a transfer gap still requires a uniform lower frame for the
middle-insertion Gramian.

**Status: [EXACT] for the dominated-kernel bridge disintegration,
commutative fusion-residue identification, score/Fisher and half-density
normalizations, marginal-Hessian sign, Doob invariance, middle-insertion
operator, and transfer-defect upper bound; [EXACT UNDER THE STATED
FINITE-WILSON HYPOTHESES] for the Perron-cancellation formula; [OPEN
ANALYTIC ESTIMATE] for a volume- and regulator-uniform bridge lower frame on
the complete gauge-invariant vacuum complement.**

## A composite kernel disintegrates into bridge fibers

Let \(X,Y,Z\) be standard Borel spaces, let \(\nu\) be a probability measure
on \(X\), and let \(k_s(x,y)\) and \(k_t(y,z)\) be nonnegative Markov
densities relative to fixed sigma-finite measures \(\mu_Y,\mu_Z\). Put

$$
k_{s+t}(x,z)
:=
\int_Y
k_s(x,y)k_t(y,z)
\,\mathrm d\mu_Y(y).
\tag{BSF1}
$$

The two-step path law and its endpoint marginal are

$$
\begin{aligned}
\mathrm d\Pi_{s,t}(x,y,z)
&:=
\nu(\mathrm dx)
k_s(x,y)\,\mathrm d\mu_Y(y)
k_t(y,z)\,\mathrm d\mu_Z(z),\\
\mathrm d\mathsf J_{s+t}(x,z)
&:=
\nu(\mathrm dx)
k_{s+t}(x,z)\,\mathrm d\mu_Z(z).
\end{aligned}
\tag{BSF2}
$$

On the endpoint support where \(k_{s+t}(x,z)>0\), conditioning on both
endpoints gives the Markov bridge

$$
\boxed{
\beta_{s,t}^{x,z}(\mathrm dy)
:=
\frac{
k_s(x,y)k_t(y,z)
}{
k_{s+t}(x,z)
}
\,\mathrm d\mu_Y(y),}
\qquad
\mathrm d\Pi_{s,t}
=
\mathrm d\mathsf J_{s+t}\,
\beta_{s,t}^{x,z}.
\tag{BSF3}
$$

Consequently,

$$
L^2(\Pi_{s,t})
\cong
\int_{X\times Z}^{\oplus}
L^2(\beta_{s,t}^{x,z})
\,\mathrm d\mathsf J_{s+t}(x,z).
\tag{BSF4}
$$

This is the scalar Hilbert realization of the commutative specialization of
[[pointed-cp-fusion-residue/inq#Composition is a cyclic inclusion|pointed
GNS fusion]]. The scalarized cyclic inclusion is

$$
\mathsf V:
L^2(\mathsf J_{s+t})
\longrightarrow
L^2(\Pi_{s,t}),
\qquad
(\mathsf VF)(x,y,z):=F(x,z),
\tag{BSF5}
$$

and its adjoint is endpoint conditioning:

$$
(\mathsf V^*G)(x,z)
:=
\mathbb E_{\beta_{s,t}^{x,z}}
[G(x,\cdot,z)].
\tag{BSF6}
$$

The scalarized fusion residue is therefore

$$
\boxed{
\mathcal R_{s,t}^{\mathrm{sc}}
:=
\ker\mathsf V^*
=
\left\{
G:
\mathbb E[G\mid X,Z]=0
\right\}
\cong
\int_{X\times Z}^{\oplus}
L_0^2(\beta_{s,t}^{x,z})
\,\mathrm d\mathsf J_{s+t}(x,z).}
\tag{BSF7}
$$

In the fixed fiber \(L^2(\mu_Y)\), the normalized cyclic vector over
\((x,z)\) is the bridge half-density

$$
\xi_{s,t}^{x,z}(y)
:=
\left(
\frac{\mathrm d\beta_{s,t}^{x,z}}
{\mathrm d\mu_Y}(y)
\right)^{1/2}.
\tag{BSF8}
$$

Multiplication by \(\xi_{s,t}^{x,z}\) identifies
\(\mathbb C1\subset L^2(\beta_{s,t}^{x,z})\) with the cyclic line and
\(L_0^2(\beta_{s,t}^{x,z})\) with its orthogonal complement. The bridge law
defines the whole intermediate-path fiber; only its centered \(L^2\)
subspace is the fusion residue. No strict-positivity premise is needed for
this projection statement. With zeros, the displayed density and all score
derivatives are understood \(\mathsf J_{s+t}\)-almost everywhere on their
possibly varying supports; differentiable score families additionally need
fixed support, or an explicit treatment of support motion.

## Bridge scores are residue tangents

Let \(q\) collect exterior endpoint, kernel, or time-splitting parameters.
Relative to the fixed measure \(\mu_Y\), write

$$
\mathscr V_q(y)
:=
-\log\!\left[
k_s^q(x,y)k_t^q(y,z)
\right],
\qquad
\mathscr A(q)
:=
-\log
\int_Ye^{-\mathscr V_q(y)}
\,\mathrm d\mu_Y(y).
\tag{BSF9}
$$

Assume fixed support, twice differentiable kernels, differentiation under
the integral, and square-integrable scores. For \(u\in T_qQ\), define

$$
\boxed{
\mathcal S_q(u)
:=
\mathrm d_q
\log\!\left(
\frac{\mathrm d\beta_q}
{\mathrm d\mu_Y}
\right)[u]
=
-\left(
\mathrm d\mathscr V_q[u]
-\mathbb E_{\beta_q}
[\mathrm d\mathscr V_q[u]]
\right).}
\tag{BSF10}
$$

Normalization gives

$$
\mathbb E_{\beta_q}[\mathcal S_q(u)]=0,
\qquad
\mathcal S_q(u)\in L_0^2(\beta_q).
\tag{BSF11}
$$

For example, endpoint derivatives are

$$
\begin{aligned}
\mathcal S_x(u;y)
&=
\mathrm d_x\log k_s(x,y)[u]
-\mathrm d_x\log k_{s+t}(x,z)[u],\\
\mathcal S_z(v;y)
&=
\mathrm d_z\log k_t(y,z)[v]
-\mathrm d_z\log k_{s+t}(x,z)[v].
\end{aligned}
\tag{BSF12}
$$

The score Gramian is the bridge Fisher form

$$
\boxed{
\mathcal I_q(u,v)
:=
\left\langle
\mathcal S_q(u),\mathcal S_q(v)
\right\rangle_{L^2(\beta_q)}
=
\operatorname{Cov}_{\beta_q}
\!\left(
\mathrm d\mathscr V_q[u],
\mathrm d\mathscr V_q[v]
\right).}
\tag{BSF13}
$$

The GNS half-density carries a different normalization. In the common
\(L^2(\mu_Y)\) trivialization,

$$
\boxed{
\mathrm d\xi_q[u]
=
\frac12\mathcal S_q(u)\xi_q,
\qquad
\mathrm d\xi_q[u]\perp\xi_q,
\qquad
\left\langle
\mathrm d\xi_q[u],
\mathrm d\xi_q[v]
\right\rangle
=
\frac14\mathcal I_q(u,v).}
\tag{BSF14}
$$

Thus a differentiated cyclic bridge line supplies a genuine
fusion-residue vector, but its Gramian is one quarter of the score Fisher
form. The score family need not span the full residue, and infinite Fisher
norm means that the declared direction does not define a Hilbert
half-density tangent.

With a fixed affine connection on \(Q\), the same differentiation gives

$$
\boxed{
\nabla^2\mathscr A(u,v)
=
\mathbb E_{\beta_q}
\!\left[
\nabla^2\mathscr V_q(u,v)
\right]
-\mathcal I_q(u,v).}
\tag{BSF15}
$$

The Fisher Gramian is the positive covariance term **subtracted** from the
Hessian of \(-\log Z\), not generally the effective Hessian itself.
[[contemporary-puzzles/yang-mills-mass-gap/vacuum-boundary-gluing-and-wall-response#The nonlinear residue has a fixed sign|The nonlinear marginal theorem]]
owns the corresponding curved-fiber, Witten-operator, and form-domain
statements. If the reference measure varies with \(q\), its log-density must
be absorbed into \(\mathscr V_q\), or its score and geometric
volume-variation terms must be added explicitly.

## Doob transforms preserve the bridge fiber

Let \(\kappa_r(x,y)\) be composable positive kernels with
\(\kappa_{s+t}=\kappa_s\kappa_t\), and let \(h>0\) satisfy

$$
K_rh=\lambda_rh,
\qquad
\lambda_{s+t}=\lambda_s\lambda_t,
$$

and define their common Doob transform by

$$
p_r^h(x,y)
:=
\frac{
\kappa_r(x,y)h(y)
}{
\lambda_rh(x)
}.
\tag{BSF16}
$$

Then the conditional bridge density obeys the exact cancellation

$$
\boxed{
\frac{
p_s^h(x,y)p_t^h(y,z)
}{
p_{s+t}^h(x,z)
}
=
\frac{
\kappa_s(x,y)\kappa_t(y,z)
}{
\kappa_{s+t}(x,z)
}.}
\tag{BSF17}
$$

The \(h\)- and eigenvalue factors, including their parameter derivatives,
cancel fiberwise. They do not disappear from the endpoint law used to
scalarize the fibers. In a stationary ground-state transform,
\(\nu_h=h^2\mu\) and
\(\mathsf J_{s+t}=\nu_hP_{s+t}^h\) still determine the global
direct-integral norm.

For the finite regulated Wilson sandwich, assume \(a>0\), \(k>0\), and a
strictly positive Perron pair for

$$
T
=
c\,M_aKM_a,
\qquad
K_T(U,V)
=
c\,a(U)k(U,V)a(V),
\tag{BSF18}
$$

the conditional middle-slice bridge of two Doob steps is

$$
\boxed{
\beta_T^{U,Z}(\mathrm dY)
=
\frac{
k(U,Y)a(Y)^2k(Y,Z)
}{
\displaystyle
\int
k(U,Y')a(Y')^2k(Y',Z)
\,\mathrm d\mu_{\mathrm H}(Y')
}
\,\mathrm d\mu_{\mathrm H}(Y).}
\tag{BSF19}
$$

The Perron vector, maximal eigenvalue, scalar \(c\), and endpoint factors
\(a(U),a(Z)\) cancel. The middle action weight \(a(Y)^2\) does not.
Likewise, a perturbation that multiplies the unnormalized two-step path
weight by a factor depending only on the fixed endpoints \((U,Z)\) leaves
the normalized bridge unchanged and has zero bridge score. Bridge geometry
therefore has a reciprocal or endpoint-coboundary radical.

This cancellation is useful but limited. The actual Wilson stationary edge
law and the orthogonal structure of the physical slice carrier remain
Perron weighted, as recorded by
[[gauge-cycle-innovation-filtration/inq#The actual Wilson pair has a complete physical matrix|the Wilson innovation matrix]].

## A middle insertion analyzes the complete slice carrier

The finite-parameter score construction does not by itself cover an
infinite-dimensional physical carrier. A stationary Markov path supplies a
canonical infinite family. Let \((X_j)_{j\in\mathbb Z}\) have invariant law
\(\nu\), and use the forward convention

$$
(Pf)(x)
:=
\mathbb E[f(X_1)\mid X_0=x]
\tag{BSF20}
$$

on \(\mathcal H=L^2(\nu)\). Let

$$
J_n:\mathcal H\longrightarrow L^2(\Omega,\mathbb P),
\qquad
J_nf:=f(X_n),
$$

and let

$$
\mathsf E_{0,2n}
:=
\mathbb E[
\,\cdot\mid\sigma(X_0,X_{2n})
].
$$

Write \(\mathsf J_{2n}:=\operatorname{Law}(X_0,X_{2n})\) and choose the
regular conditional bridge
\(\beta_n^{x,z}:=\operatorname{Law}(X_n\mid X_0=x,X_{2n}=z)\).

Define the bridge analysis and its slice Gramian by

$$
\boxed{
L_n^{\mathrm{br}}
:=
(I-\mathsf E_{0,2n})J_n,
\qquad
B_n^{\mathrm{br}}
:=
(L_n^{\mathrm{br}})^*L_n^{\mathrm{br}}
=
J_n^*(I-\mathsf E_{0,2n})J_n.}
\tag{BSF21}
$$

The range of \(L_n^{\mathrm{br}}\) is contained in the centered bridge
fusion residue, and

$$
\boxed{
\left\langle
f,B_n^{\mathrm{br}}g
\right\rangle_\nu
=
\mathbb E\!\left[
\operatorname{Cov}
\!\left(
\overline{f(X_n)},g(X_n)
\mid X_0,X_{2n}
\right)
\right].}
\tag{BSF22}
$$

In particular, with all equalities understood in \(L^2(\mathbb P)\),

$$
\boxed{
\ker L_n^{\mathrm{br}}
=
\left\{
f\in L^2(\nu):
f(X_n)\text{ is }\sigma(X_0,X_{2n})\text{-measurable}
\right\}.}
\tag{BSF22a}
$$

If the bridge law is equivalent to \(\nu\) for almost every endpoint pair,
this kernel consists only of constants. Without such a support-connecting
hypothesis, endpoint-determined middle observables can remain in the kernel.

No reversibility is needed for this identity. To compare with transfer,
write \(\mathsf E_0\) and \(\mathsf E_{2n}\) for conditioning on the
corresponding single-time sigma-algebras. Nested projection order gives

$$
\mathsf E_0
\leq
\mathsf E_{0,2n},
\qquad
\mathsf E_{2n}
\leq
\mathsf E_{0,2n}.
$$

Moreover,

$$
\mathsf E_0J_n=J_0P^n,
\qquad
\mathsf E_{2n}J_n=J_{2n}(P^*)^n.
$$

Therefore

$$
\boxed{
0
\leq
B_n^{\mathrm{br}}
\leq
I-(P^*)^nP^n,
\qquad
B_n^{\mathrm{br}}
\leq
I-P^n(P^*)^n.}
\tag{BSF23}
$$

For a reversible chain, \(P=P^*\), and both upper bounds become

$$
\boxed{
0
\leq
B_n^{\mathrm{br}}
\leq
I-P^{2n}.}
\tag{BSF24}
$$

This is a canonical history-sensitive same-carrier solder. It differs from
the canonical endpoint lift of the composite GNS carrier, which lies
entirely in the cyclic range and is annihilated by the fusion-residue
projection.

The bridge analysis is also an infinite-dimensional score map. For bounded
real \(f\), set \(\beta^{x,z}=\beta_n^{x,z}\) and tilt each conditional
bridge by

$$
\frac{
\mathrm d\beta_{\theta,f}^{x,z}
}{
\mathrm d\beta^{x,z}
}(y)
:=
\frac{
e^{\theta f(y)}
}{
\int e^{\theta f}\,\mathrm d\beta^{x,z}
}.
\tag{BSF25}
$$

At \(\theta=0\),

$$
\boxed{
\left.
\partial_\theta
\log
\frac{
\mathrm d\beta_{\theta,f}^{X_0,X_{2n}}
}{
\mathrm d\beta^{X_0,X_{2n}}
}(X_n)
\right|_{\theta=0}
=
f(X_n)
-\mathbb E[f(X_n)\mid X_0,X_{2n}]
=
L_n^{\mathrm{br}}f.}
\tag{BSF26}
$$

Thus the global Fisher Gramian of the middle-insertion family is
\(B_n^{\mathrm{br}}\), while its normalized half-density derivative has
Gramian \(B_n^{\mathrm{br}}/4\). The probability tilts are initially
defined for bounded real directions. Since \(L_n^{\mathrm{br}}\) is a
bounded complex-linear operator, the analysis and its Hermitian Gramian
extend to all of \(L^2(\nu)\); an unbounded exponential tilt separately
requires exponential integrability or differentiability in quadratic mean.

The normalization in (BSF25) is endpointwise. A single unnormalized path
tilt \(e^{\theta f(X_n)}\), followed by conditioning on the endpoints, gives
exactly (BSF25). Equivalently, one may multiply each half-kernel by
\(e^{\theta f/2}\). Multiplying **both** half-kernels by
\(e^{\theta f}\) instead gives score \(2L_n^{\mathrm{br}}f\). By contrast,
normalizing the tilted path law only once globally gives score
\(f(X_n)-\mathbb E f(X_n)\): its endpoint marginal also moves, so that
global score is not \(L_n^{\mathrm{br}}f\).

For this affine tilt,

$$
\left.
\partial_\theta^2
\log
\int e^{\theta f}\,\mathrm d\beta^{x,z}
\right|_{\theta=0}
=
\operatorname{Var}_{\beta^{x,z}}(f),
$$

whereas the Hessian of the negative log normalization is its negative. This
is the one-parameter specialization of (BSF15).

## The bridge floor is a subspace angle

Let $Q$ be any orthogonal projection on the slice carrier and set

$$
\rho_n^{\mathrm{br}}(Q)
:=
\left\|
\mathsf E_{0,2n}J_nQ
\right\|.
\tag{BSF26a}
$$

Because $J_n$ is an isometry and $\mathsf E_{0,2n}$ is an orthogonal
projection,

$$
\boxed{
\inf_{\substack{f\in\operatorname{Ran}Q\\\|f\|=1}}
\langle f,B_n^{\mathrm{br}}f\rangle
=
1-\rho_n^{\mathrm{br}}(Q)^2.}
\tag{BSF26b}
$$

Thus the bridge lower frame is exactly a positive angle between the chosen
middle-slice subspace and the joint endpoint-measurable subspace.
Equivalently, it is a ceiling on how accurately the two boundary
presentations can jointly recover any normalized middle distinction. This
is a maximal-correlation statement for $X_n$ and $(X_0,X_{2n})$; it is
not the ordinary one-ended maximal correlation of $X_0$ and $X_n$.

## The remaining theorem is a lower frame

Let $\Pi_{\mathrm{fix}}$ be the fixed-space projection of a Hilbert-positive
self-adjoint Markov transfer $P$, and put
$Q:=I-\Pi_{\mathrm{fix}}$. Equations (BSF21)--(BSF24) already supply the upper
same-carrier comparison needed by the fusion-response theorem. The new
analytic premise is

$$
\boxed{
B_n^{\mathrm{br}}
\geq
\kappa_nQ,
\qquad
\kappa_n>0,}
\tag{BSF27}
$$

equivalently,

$$
\mathbb E\!\left[
\operatorname{Var}
\!\left(
f(X_n)\mid X_0,X_{2n}
\right)
\right]
\geq
\kappa_n\|Qf\|_2^2
\tag{BSF28}
$$

for every \(f\in L^2(\nu)\). A useful sufficient condition is a bridge
minorization. If, for \(\mathsf J_{2n}\)-almost every \((x,z)\),

$$
\beta_n^{x,z}\geq\varepsilon\nu
\qquad
\text{as measures},
\tag{BSF28a}
$$

then

$$
\operatorname{Var}_{\beta_n^{x,z}}(f)
=
\inf_{c\in\mathbb C}
\int|f-c|^2\,\mathrm d\beta_n^{x,z}
\geq
\varepsilon\operatorname{Var}_{\nu}(f),
$$

and hence \(B_n^{\mathrm{br}}\geq
\varepsilon(I-\Pi_{\mathbf1})\). This gives (BSF27) when the fixed space is
the constant line. At a fixed finite regulator, entrywise positivity often
produces some minorization constant; it says nothing by itself about a
constant uniform in volume or regulator removal.

If (BSF27) holds, then

$$
\|P^nQ\|
\leq
\sqrt{1-\kappa_n}.
\tag{BSF29}
$$

If

$$
P
=
e^{-a_\tau(H-E_0)/(\hbar c)},
\qquad
n(a)a_{\tau,a}\longrightarrow\ell_*>0,
$$

and \(\kappa_{n(a)}\geq\kappa_*>0\) uniformly in spatial volume, admissible
boundary or flux sector, and regulator removal, then

$$
\boxed{
\Delta_E
\geq
-\frac{\hbar c}{2\ell_*}
\log(1-\kappa_*).}
\tag{BSF30}
$$

The factor \(1/2\) comes from the squared transfer norm. The endpoint
separation is \(2n\) steps, while \(\ell_*\) is the limiting length from
either endpoint to the middle insertion.

The upper comparison (BSF24) is exact; the lower frame (BSF27) is a
one-way sufficient condition and is not derived by fusion, conditioning,
positivity, or the existence of bridge scores. Even when one separately
proves the qualitative identity
\(\ker B_n^{\mathrm{br}}=\operatorname{Ran}\Pi_{\mathrm{fix}}\), it gives no
volume-uniform or continuum-uniform constant. A nonzero fusion residue can
retain fixed rank while a Markov generator edge tends to zero, as
[[contemporary-puzzles/yang-mills-mass-gap/fusion-residue-is-not-transfer-defect|the fusion/transfer firewall]]
shows.

[[bridge-data-augmentation-solder/inq|Bridge Data-Augmentation Solder]]
identifies \(I-B_n^{\mathrm{br}}=K_n^*K_n\) as the positive marginal chain
of the two-component middle--boundary joint law. This does not prove
(BSF27), but it supplies two non-global routes to it: exact
maximal-correlation tensorization for product link bridges and a complete
innovation-matrix bound for the interacting bridge law.

There is no converse from transfer mixing to a bridge lower frame. For the
nonreversible shift register

$$
X_k=(\xi_k,\xi_{k+1}),
$$

with iid bits \(\xi_k\), one has \(P^2=\Pi_{\mathbf1}\), but \(X_1\) is
determined by \((X_0,X_2)\). Thus \(L_1^{\mathrm{br}}=0\) despite complete
two-step mixing. Likewise, the reversible deterministic flip on two points
has \(L_1^{\mathrm{br}}=0\) and period two. It also warns that reversibility
alone does not make \(P\) a positive Hilbert-space transfer admitting the
Hamiltonian logarithm used in (BSF30).

The obstruction persists even after both defects are removed. Positive
reversible high-girth expander chains can have a centered transfer norm
tending to zero and no nonconstant exactly recoverable midpoint function,
while their bridge floors still tend to zero because two endpoints recover
the middle with probability tending to one. Thus the missing condition is
uniform exclusion of **approximate** two-ended recovery, not merely transfer
mixing plus a kernel identity. The construction and its relative
quasi-factorization reformulation are in
[[three-block-bridge-factorization/inq|Three-Block Bridge Factorization]].

For comparison, [[gaussian-bridge-gap-calibration/inq|Gaussian Bridge-Gap
Calibration]] proves that a stationary Gaussian mode has the sharp floor
\(\tanh(\omega\ell)\). This is the exact free-theory relation between the
bridge angle and inverse Compton rate, not a generic interacting formula.

For lattice gauge theory, the safest construction is on the gauge-reduced
slice path space. Working upstairs instead requires the path law and
\(\mathsf E_{0,2n}\) to commute with the residual gauge action before
restricting (BSF21) to invariant functions. Fiberwise Doob cancellation
does not remove the Perron weight from the global norm in (BSF22). A bridge
Fisher form is also dimensionless and changes with tangent normalization.
It becomes a physical transfer rate only through (BSF23), a fixed
Euclidean thickness, and the independently proved lower frame.

Finally, the Markov path carrier is a representation of a positive
relation, not a stochastic ontology. Its endpoint conditioning is not by
itself an Osterwalder--Schrader interface map, and the resulting Euclidean
contraction is not Lorentzian local unitarity. Gauge reduction, OS
reconstruction, continuum carrier convergence, and the Poincare
energy--mass identification remain separate.

[[bridge-score-fusion-geometry/receipts/bridge_score_fusion_receipt.py|The
finite two-state receipt]] checks the bridge projection, centered score,
half-density factor, Doob cancellation, and the transfer-defect order.
[[bridge-score-fusion-geometry/receipts/bridge-score-fusion-receipt-output.txt|Its
stored output]] records the errors and the strict inequality.
