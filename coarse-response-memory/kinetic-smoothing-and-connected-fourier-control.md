# Kinetic Smoothing Controls Connected Preparation

The connected logarithmic preparation equation closes in a volume-uniform local norm when kinetic damping is retained before estimating its quadratic response. Representation Casimirs pay for the derivative cost; a trace-class Fourier norm keeps the nonabelian product channels together. At an explicit small interaction-to-kinetic ratio this constructs the actual connected preparation with exponentially weighted local derivative bounds for all times. The graph, group, kinetic operator and interaction remain supplied, and the estimate does not extend automatically to the Yang--Mills continuum trajectory.

**Status: constructive small-interaction theorem on finite compact-group
products, uniform in volume and preparation time under the stated
local source bound.** No novelty claim is made. The gain over a
small-perturbation gap alone is control of connected spatial
derivatives of the actual prepared logarithm.

## Retain kinetic response before taking its norm

Use the carrier, product kinetic operator and interaction subsets
in [[connected-preparation-and-local-normalization|connected preparation]]
(CP1)--(CP8). The factors are copies of a fixed compact connected
nontrivial Lie group \(G\), with a specified bi-invariant metric.
Write
\[
0<\kappa_{\min}\le\kappa_e\le\kappa_{\max},\qquad
c_*=\min_{\pi\ne\mathbf1}c_\pi>0,
\tag{KF1}
\]
where \(c_\pi\) is the positive Laplacian Casimir on an irreducible
representation. This is the supplied one-link kinetic scale,
not an interacting mass gap inferred from the construction.

The instantaneous quadratic term need not be bounded in a
fixed local derivative norm. Its relevant replacement is
\[
\mathcal B(U,V)_C(t)
=\int_0^t e^{-(t-s)K}Q
\sum_{\substack{A,D\subseteq C\\A\cup D=C}}
\Gamma_K(U_A(s),V_D(s))\,ds,
\tag{KF2}
\]
where \(Q\) removes the global Haar constant of each function.
Constant connected coefficients have no derivatives and are
restored below. All comparisons keep the same padded kinetic
operator, including when interactions are removed.

## A norm indexed by actual representation activity

For a product irreducible \(\boldsymbol\pi=(\pi_e)_{e\in E}\), put
\[
h_e(\boldsymbol\pi)=\sqrt{c_{\pi_e}},\qquad
h(\boldsymbol\pi)=\sum_eh_e(\boldsymbol\pi),\qquad
E_{\boldsymbol\pi}=\sum_e\kappa_ec_{\pi_e}.
\tag{KF3}
\]
Expand a mean-zero connected coefficient as
\[
U_C(t,x)=
\sum_{\boldsymbol\pi\ne\mathbf1}
\operatorname{Tr}\!\left(A_{C,\boldsymbol\pi}(t)
\boldsymbol\pi(x)\right).
\tag{KF4}
\]
The usual Fourier dimension factor is absorbed in \(A\);
its coefficient norm is the matrix trace norm \(\|A\|_1\).
Require \(\pi_e=\mathbf1\) off \(E(C)\). An interaction
label may be large even when its surviving representation
depends on few links; these are not interchangeable supports.

There is a time-norm subtlety for matrices. Let
\(\mathcal T=C_b([0,\infty),\mathbb C)\), and use
\[
\|A\|_{\mathcal T,1}
=\inf_{A(t)=\sum_j a_j(t)B_j}
\sum_j\|a_j\|_\infty\|B_j\|_1.
\tag{KF5}
\]
This is the completed projective tensor norm
\(\mathcal T\widehat\otimes_\pi S_1(V_{\boldsymbol\pi})\).
The matrices \(B_j\) are time independent. Taking only
\(\sup_t\|A(t)\|_1\) would not justify summing the separate
output-channel time suprema in the proof below.

Let \(C\) range over nonempty connected interaction sets and
give it weight \(w_\mu(C)=e^{\mu\operatorname{diam}C}\), \(\mu>0\),
using the induced overlap graph and diameter zero for a singleton.
Define
\[
\boxed{
\mathcal N_\mu(U)=
\sup_e\sum_{\substack{C\ {\rm connected}\\
                         \boldsymbol\pi\ne\mathbf1}}
w_\mu(C)h_e(\boldsymbol\pi)h(\boldsymbol\pi)
\|A_{C,\boldsymbol\pi}\|_{\mathcal T,1}.
}
\tag{KF6}
\]
Take real-valued fields, zero initial values and no constant
mode. These are closed conditions. For a finite graph this
is a Banach space after completion; every nonconstant mode
is detected by at least one anchor.

This norm controls the derivatives actually requested in
(CP13). In the supplied product connection,
\[
\begin{aligned}
\sup_{t,e}\sum_C w_\mu(C)\|\nabla_eU_C(t)\|_\infty
&\le c_*^{-1/2}\mathcal N_\mu(U),\\
\sup_{t,e}\sum_C w_\mu(C)
\sum_f\|\nabla_f\nabla_eU_C(t)\|_\infty
&\le\mathcal N_\mu(U).
\end{aligned}
\tag{KF7}
\]
The second norm can be the Hilbert--Schmidt norm of each
Hessian block. To verify it, first take a rank-one matrix
coefficient. The identity
\(\sum_a d\pi(X_a)^*d\pi(X_a)=c_\pi I\) bounds its gradient
by \(h_e\|A\|_1\) and its ordered second derivatives by
\(h_eh_f\|A\|_1\). On the same group factor, the covariant
Hessian is the symmetrized pair of invariant derivatives,
because the metric is bi-invariant; the same bound holds.
Sum a nuclear decomposition and then the Fourier series.
Finally use \(h(\boldsymbol\pi)\ge\sqrt{c_*}\).

In particular the norm implies absolute convergence through
two spatial derivatives on every finite product. Its constants
in (KF7) do not count that product's volume.

## Nonabelian multiplication does not lose matrix dimension

For one product-representation pair \(\boldsymbol\pi,\boldsymbol\sigma\),
decompose their tensor product into irreducibles
\(\boldsymbol\tau\) and multiplicity spaces. If the input
matrices are \(A,B\), the product coefficient
\(C_{\boldsymbol\tau}(A,B)\) is obtained by compressing
\(A\otimes B\) to that isotypic block and tracing its multiplicity
space. Pinching and partial trace give
\[
\sum_{\boldsymbol\tau}
\|C_{\boldsymbol\tau}(A,B)\|_1
\le\|A\|_1\|B\|_1.
\tag{KF8}
\]
This holds for non-Hermitian matrices as well: the adjoint
of the compression-and-trace map is a unital star homomorphism
on the block-diagonal output algebra, hence an operator-norm
contraction; duality gives the trace-norm contraction.
No representation-dimension factor is discarded.

On this output channel, the coefficient of \(\Gamma_K\) is
\[
\gamma_{\boldsymbol\pi,\boldsymbol\sigma}^{\boldsymbol\tau}
=\frac12\sum_f\kappa_f
(c_{\pi_f}+c_{\sigma_f}-c_{\tau_f}).
\tag{KF9}
\]
The cross Casimir is scalar on each irreducible channel,
including all its multiplicities. Row--column Cauchy--Schwarz
for the Lie generators, and the triangle inequality for
their tensor-product row operator, give respectively
\[
\begin{aligned}
|\gamma_{\boldsymbol\pi,\boldsymbol\sigma}^{\boldsymbol\tau}|
&\le\kappa_{\max}\sum_fh_f(\boldsymbol\pi)h_f(\boldsymbol\sigma),\\
h_e(\boldsymbol\tau)&\le
h_e(\boldsymbol\pi)+h_e(\boldsymbol\sigma).
\end{aligned}
\tag{KF10}
\]
For example, the cross operator is a sum of
\(d\pi(X_a)\otimes d\sigma(X_a)\); the two squared row norms
are the scalar Casimirs. The identities do not require
commuting Lie generators.

For any nonconstant output,
\[
\frac{h(\boldsymbol\tau)}{E_{\boldsymbol\tau}}
\le\frac1{\kappa_{\min}\sqrt{c_*}},
\tag{KF11}
\]
since each nonzero \(h_e\) is at least \(\sqrt{c_*}\).
This is the kinetic compensation that a support-only estimate
misses.

## The anchored bilinear estimate closes

If a shared-link term in (KF10) is nonzero, both input
interaction sets contain that link in their support. Their
union is connected, and
\[
w_\mu(A\cup D)\le e^\mu w_\mu(A)w_\mu(D).
\tag{KF12}
\]
The factor \(e^\mu\) allows one connecting adjacency even when
\(A,D\) have no interaction label in common.

For elementary time coefficients \(a(t)A,b(t)B\), each output
matrix in (KF8) is fixed. Its scalar time convolution obeys
\[
\left\|\int_0^t e^{-E_{\boldsymbol\tau}(t-s)}
a(s)b(s)\,ds\right\|_\infty
\le\frac{\|a\|_\infty\|b\|_\infty}{E_{\boldsymbol\tau}}.
\]
Thus (KF8) remains available before the projective infimum
in (KF5). Remove the constant output before dividing.

Combining (KF8)--(KF12), split the anchor into
\(h_e(\boldsymbol\pi)+h_e(\boldsymbol\sigma)\).
For the first branch the remaining input sum at a shared
link \(f\) is bounded by
\[
\sum_{D,\boldsymbol\sigma}
w_\mu(D)h_f(\boldsymbol\sigma)
\|B_{D,\boldsymbol\sigma}\|_{\mathcal T,1}
\le c_*^{-1/2}\mathcal N_\mu(V).
\]
The sum over \(f\) then leaves precisely
\(h_e(\boldsymbol\pi)h(\boldsymbol\pi)\) for the first
input. The other branch is identical. Therefore
\[
\boxed{
\mathcal N_\mu(\mathcal B(U,V))
\le C_\mu\mathcal N_\mu(U)\mathcal N_\mu(V),
\qquad
C_\mu=\frac{2e^\mu\kappa_{\max}}{\kappa_{\min}c_*}.
}
\tag{KF13}
\]
The same proof gives the static inverse bound for
\(K^{-1}Q\sum_{A\cup D=C}\Gamma_K(U_A,V_D)\).
The estimate uses active derivatives and kinetic damping,
not a lower bound proportional to the number of interaction
labels in \(C\).

## Why the kinetic denominator cannot be discarded

There is an exact counterexample in the static version of
(KF6), already on unit circle links. Take a cycle of \(N\ge4\)
links, interaction supports \(E(p_j)=\{j,j+1\}\), the full
connected family \(C_N\), and \(W=w_\mu(C_N)\). Set
\[
U_{C_N}=\frac{\cos(\sum_j\theta_j)}{NW},\qquad
V_{\{p_j\}}=\frac{\cos\theta_j+\cos\theta_{j+1}}2,
\]
with all other coefficients zero. Both anchored Fourier
norms are exactly one. The union response has only the
label \(C_N\), and its frequencies are
\(\pm(\mathbf1-e_j)\) and \(\pm(\mathbf1+e_j)\).
Their kinetic energies are \(N-1\) and \(N+3\), respectively.
Directly summing the anchor weights gives
\[
\begin{aligned}
\mathcal N_\mu\!\left(\sum_{A\cup D=C}\Gamma(U_A,V_D)\right)
&=\frac{N^2+1}{N},\\
\mathcal N_\mu\!\left(K^{-1}Q
\sum_{A\cup D=C}\Gamma(U_A,V_D)\right)
&=\frac{N^2+2N-1}{N(N+3)}<1.
\end{aligned}
\tag{KF13a}
\]
For example, the negative-frequency shift contributes
\((N-1)^2/(2N)\) to the first norm and the positive shift
contributes \((N+1)^2/(2N)\); divide these by their
respective energies for the second norm. The cluster weight
cancels between input and output. Thus the instantaneous
bilinear map is unbounded in this same norm, while its
kinetic inverse has the proved uniform bound. No large
frequency on any one link was needed.

These are test functions in the comparison space, not an
asserted Haar-prepared Wilson trajectory. The
[[receipts/connected_kinetic_majorant_receipt.py|focused verification receipt]]
checks (KF13a) with exact Fourier dictionaries, the scalar
weight inequalities and zero-mode removal. Separate finite
\(SU(2)\) tensor tests check cross Casimirs, non-Hermitian
trace contraction and a genuine multiplicity-two channel.
They also reject using a normalized multiplicity trace.
The finite controls do not prove the infinite representation
sum, projective time completion or fixed-point theorem;
those are the analytic arguments above and below.

## Construct the actual logarithm, rather than assume its bound

Let each \(q_p\) be a real trigonometric polynomial on its
fixed support. More general smooth sources are allowed when the
following Fourier sum is finite. Write \(q_{p,\boldsymbol\pi}\)
for the absorbed-dimension coefficient in (KF4), and set
\[
s=
\sup_e\sum_{p,\boldsymbol\pi\ne\mathbf1}
\frac{h_e(\boldsymbol\pi)h(\boldsymbol\pi)}
     {E_{\boldsymbol\pi}}
\|\lambda_pq_{p,\boldsymbol\pi}\|_1.
\tag{KF14}
\]
The singleton source trajectory
\[
S_{\{p\}}(t)=\int_0^t e^{-(t-r)K}Q(\lambda_pq_p)\,dr
\]
has \(\mathcal N_\mu(S)\le s\). If
\[
\boxed{4C_\mu s<1,}
\tag{KF15}
\]
the map \(U\mapsto S+\mathcal B(U,U)\) preserves the ball
\(\mathcal N_\mu(U)\le2s\) and contracts there with constant
at most \(4C_\mu s\). At \(s=0\) its zero solution is immediate.
Banach iteration constructs a unique solution in this ball
for all \(t\ge0\), with no volume-dependent constant.

This alone would not justify assuming the actual preparation
belongs to the ball. Instead, restore each scalar connected
coefficient by integrating the Haar-constant part of (CP8),
initially zero. Derivatives and \(\Gamma_K\) ignore these
constants, so this restoration does not change the fixed point.
For every \(B\subseteq\Lambda\), sum the restored coefficients
over \(C\subseteq B\). The resulting \(w_B\) satisfies (CP7)
and \(w_B(0)=0\).

On each finite graph, (KF7) gives convergent second derivatives;
the mild equation consequently gives the classical logarithmic
heat equation. Exponentiating gives the positive solution of
the original linear equation with initial value one. Uniqueness
identifies it with \(P_B\) in (CP2). Finite-time parabolic
regularity recovers further smoothness. Reality and, when
applicable, gauge invariance are preserved at every iteration.
No interacting gap or small norm of the unknown exact
trajectory was assumed.

The connected derivative target is therefore proved in this
regime:
\[
\boxed{\text{the left side of (CP13)}
\le2s(1+c_*^{-1/2}).}
\tag{KF16}
\]
For a fixed finite graph, smooth convergence of normalized
heat preparation to its positive ground vector transfers
these derivative bounds to the connected ground logarithms.
That convergence uses compact spectral isolation only at
the fixed graph; no volume-uniform rate is needed to pass
the already uniform derivative estimate.

There is also a direct locality consequence. Compare
\(\Lambda_0\subseteq\Lambda\) on the same padded kinetic
carrier. Suppose every removed interaction has overlap-graph
distance at least \(R\) from every interaction incident to
an anchored edge \(e\). The difference of local scores is
the sum over \(C\subseteq\Lambda\) not contained in
\(\Lambda_0\). Every contributing \(C\) joins that edge
to a removed interaction, so its diameter is at least \(R\).
Hence
\[
\begin{aligned}
\|\nabla_e(w_\Lambda-w_{\Lambda_0})\|_\infty
&\le2s\,c_*^{-1/2}e^{-\mu R},\\
\sum_f\|\nabla_f\nabla_e(w_\Lambda-w_{\Lambda_0})\|_\infty
&\le2s\,e^{-\mu R}.
\end{aligned}
\tag{KF18}
\]
The bounds hold uniformly in preparation time and pass to
the fixed-finite-graph ground logarithms. They concern
removing distant interactions, not arbitrary changes of
boundary conditions or conditioning prescriptions. No
thermodynamic quantum state is constructed by this statement
alone.

## An explicit Wilson sufficient regime

For \(SU(2)\), \(Q=-2\operatorname{Tr}\), common \(\kappa\)
and elementary plaquettes with four distinct links,
\[
c_*=\frac34,\qquad C_\mu=\frac83e^\mu.
\]
Each link in the fundamental plaquette function has Casimir
\(3/4\). Expanding its normalized trace into matrix entries
gives at most \(2^4\) rank-one coefficient terms, each of
trace norm \(1/2\), so
\(\|q_{p,\boldsymbol\pi}\|_1\le8\). Inverted links use the
contragredient representation and do not alter that bound.
No optimal Fourier norm is asserted. Since
\(h_eh/E_{\boldsymbol\pi}=1/\kappa\) for an incident link,
if \(d=\max_e n_e\) and \(|\lambda_p|\le\lambda\),
\[
s\le\frac{8\lambda d}{\kappa},\qquad
\boxed{\frac{\lambda d}{\kappa}
<\frac{3}{256e^\mu}}
\tag{KF17}
\]
is an explicit sufficient condition for (KF16).
The constants count local incidence, not total volume.

This is stronger local information than an unquantified
product-vacuum stability statement, not a claim that
strong-coupling stability was previously unknown.
[[strong-coupling-gap-and-continuum-crossover/hamiltonian-product-vacuum-stability|The existing stability application]]
owns that established spectral result and its distinct
thermodynamic hypotheses. The bound above concerns the
connected preparation and its spatial derivatives.

## The relation constrained, and the relation still missing

The same multiplication channels that generate the quadratic
joined response also determine the Casimir damping used to
bound it. Replacing either by an independently chosen matrix
or support count would lose (KF13). This is a compatibility
constraint on the supplied operator and its state construction.

[[kinetic-hessian-bootstrap-and-uniform-response|The direct Hessian bootstrap]]
gives a complementary, larger sufficient \(SU(2)\) regime and
turns actual conditional score control into a response bound.
It does not resolve connected tails, whereas the Fourier
estimate does. Neither estimate covers the equal-unit
two-plaquette benchmark or the weak-bare-coupling continuum
trajectory merely by continuity. The threshold is a sufficient
analytic condition, not a physical transition.

[[interacting-reference-and-spectral-product-control|Changing to interacting reference blocks]]
preserves the product rule but changes the spectral multiplication
channels. A reference-drift bound gives a sufficient extension of
this construction. A positive block gap alone does not: an explicit
gapped compact reference violates the square-root energy triangle
after its eigenfunctions replace representation coefficients.
The block support, centering law and boundary-charge carrier must
also change coherently.

The Fourier-algebra background is standard; see
[[library/beurling-fourier-algebras-on-compact-groups/inq|Ludwig, Spronk and Turowska]]
for compact-group representation weights. Ground-state
fixed-point expansions likewise have established precedents,
including
[[library/expansions-for-one-quasiparticle-states-in-spin-half-systems/inq|Datta and Kennedy]].
These sources are background and attribution, not substitutes
for the particular anchored estimate proved here. Its novelty
has not been established.
