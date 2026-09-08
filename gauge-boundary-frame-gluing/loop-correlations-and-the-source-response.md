# Loop Correlations Change the Source Response

A smooth gauge-invariant loop weight changes both the state and the Fisher geometry of the retained heat source. Conjugation symmetry makes this change unusually explicit: the full path-shift entropy is its original kinetic cost plus an averaged endpoint potential difference. Its Hessian reduces the complete response calculation to a finite endpoint-control matrix. This gives a closed interacting finite-graph response and an exact \(SU(2)\) state-to-mobility relation. It does not select the loop potential, identify the response clock with physical translation, or supply a volume-uniform Yang--Mills estimate.

**Status: [EXACT FINITE-SOURCE THEOREM] for real smooth gauge-invariant endpoint weights, finite real coupling, and the source actions specified below; [EXACT OBSTRUCTION] to preserving the returned response under ordinary subdivision after a loop tilt.** The interaction function is an input. Consistency of the weighted states does not repair the proved response mismatch.

## Keep the source and its allowed transformations

Use [[haar-vertex-source-and-joint-gauge-response|the Haar-vertex source]]
on a finite graph. Its independent factors have speeds
\(c_e^U=a_e\theta_e\), \(c_e^V=a_e(1-\theta_e)\), terminal horizon \(T\),
and \(Y_e=U_e(T)V_e(T)^{-1}\). Vertex frames give
\(x_e=B_{s(e)}Y_eB_{t(e)}^{-1}\).
The group is compact and connected, with semisimple Lie algebra and
positive bi-invariant metric \(Q\).

Let \(V\in C^\infty(G^{\mathcal E},\mathbb R)^{G^{\mathcal V}}\)
and \(\lambda\in\mathbb R\) be specified. Define
\[
d\nu_\lambda=\rho_\lambda\,d\nu,\qquad
\rho_\lambda=Z_\lambda^{-1}e^{-\lambda V(Y)},\qquad
Z_\lambda=\mathbb E_\nu e^{-\lambda V(Y)}.
\tag{LT1}
\]
Gauge invariance gives \(V(x)=V(Y)\), so the Haar frames remain
independent and cost-free. The endpoint density is
\[
w_\lambda(x)=Z_\lambda^{-1}e^{-\lambda V(x)}w_0(x).
\tag{LT2}
\]
Every density here is smooth, positive and bounded above and below
on the finite compact endpoint product.

Retain the original deterministic based path actions
\(U_e\mapsto k_eU_e\), \(V_e\mapsto l_eV_e\), together with the
vertex-frame actions. No new Hamiltonian or mobility is specified.
The source tilt, however, is a genuine new functional input.

## The actual score includes the interaction derivative

Let \(\mathsf H\) be the real Hilbert space of based absolutely
continuous factor controls \(h=(h^U,h^V)\), with metric
\[
g_0(h,h)=\frac12\sum_e\int_0^T
 \left(\frac{|\dot h_e^U|_Q^2}{c_e^U}
       +\frac{|\dot h_e^V|_Q^2}{c_e^V}\right)ds.
\tag{LT3}
\]
Denote their pointwise source derivative by \(D_h\).
The scaled [[path-shift-fisher-geometry-before-gauge-projection|path-shift likelihood]]
has baseline score
\[
S_0(h)=\sum_{e,A\in\{U,V\}}\frac1{\sqrt{2c_e^A}}
       \int_0^T Q(\dot h_e^A,dC_e^A),
\tag{LT4}
\]
where the \(C_e^A\) are independent right stochastic logarithms,
standard Brownian motions under \(\nu\).
For nonzero \(h\), \(S_0(h)/\sqrt{g_0(h,h)}\) is standard Gaussian.

The score of the **pushed tilted law relative to itself** is
\[
\boxed{S_\lambda(h)=S_0(h)+\lambda D_hV(Y),\qquad
g_\lambda(h,j)=\mathbb E_{\nu_\lambda}S_\lambda(h)S_\lambda(j).}
\tag{LT5}
\]
The plus sign comes from differentiating
\(\rho_\lambda(\mathcal T_\epsilon^{-1}z)/\rho_\lambda(z)\).
In particular this is not merely \(g_0\) evaluated in a different
endpoint norm. Direct differentiation gives the useful check
\[
\left.\partial_\lambda g_\lambda(h,j)\right|_0
=-\operatorname{Cov}_\nu(V,S_0(h)S_0(j))
+\mathbb E_\nu\!\left[S_0(h)D_jV+S_0(j)D_hV\right].
\tag{LT6}
\]

## Conjugation reduces the whole entropy correction to endpoints

The stronger simplification uses the actual source symmetry.
Simultaneously conjugating all factor paths preserves \(\nu_\lambda\).
Every \(C_e^A\) transforms by the adjoint action. Semisimplicity
therefore implies
\[
\mathbb E_{\nu_\lambda}\int_0^T Q(v_s,dC_e^A(s))=0
\tag{LT7}
\]
for every deterministic square-integrable \(v\).
Boundedness of \(\rho_\lambda\) justifies integrability and
approximation by step functions. This is a symmetry consequence;
it does not assert that the tilted logarithms remain Brownian.

Evaluate the baseline Radon--Nikodym logarithm at a shifted sample.
For one factor of speed \(c\), it is
\[
\log\frac{d(\mathcal T_k)_*\nu}{d\nu}(\mathcal T_k z)
=\frac1{\sqrt{2c}}\int Q(k^{-1}\dot k,dC)
 +\frac1{4c}\int|k^{-1}\dot k|_Q^2ds.
\]
The velocity is in the displayed stochastic frame.
Using (LT7) and the tilt ratio proves, for arbitrary finite-energy
based \(k,l\),
\[
\boxed{\begin{aligned}
D((\mathcal T_{k,l})_*\nu_\lambda\Vert\nu_\lambda)
={}&\frac14\sum_e\int_0^T
 \left(\frac{|k_e^{-1}\dot k_e|_Q^2}{c_e^U}
      +\frac{|l_e^{-1}\dot l_e|_Q^2}{c_e^V}\right)ds\\
&+\lambda\mathbb E_{\nu_\lambda}
  \left[V((k_e(T)Y_el_e(T)^{-1})_e)-V(Y)\right].
\end{aligned}}
\tag{LT8}
\]
All path dependence outside the endpoints remains in the original
kinetic cost. The second line is not necessarily positive separately.
Their sum is actual relative entropy.

## A finite stiffness matrix determines the full endpoint response

Let \(E:\mathsf H\to\mathfrak g^{2|\mathcal E|}\) evaluate the
factor controls at \(T\), and put
\[
D_0=EE^*
=\operatorname{diag}_e(2Tc_e^U,2Tc_e^V)\otimes I_{\mathfrak g},
\tag{LT9}
\]
where the adjoint uses \(g_0\) and the endpoint \(Q\)-pairing.
Define the real symmetric matrix
\[
\mathsf H_\lambda
=\left.\operatorname{Hess}_{(\xi,\eta)}\right|_0
\mathbb E_{\nu_\lambda}
 V((e^{\xi_e}Y_e e^{-\eta_e})_e).
\tag{LT10}
\]
The first derivative is zero by the same adjoint invariance.
Thus this Hessian does not depend on second-order coordinate choices.

Taking the Hessian of (LT8) yields
\[
\boxed{g_\lambda(h,j)=g_0(h,j)
+\lambda\langle Eh,\mathsf H_\lambda Ej\rangle.}
\tag{LT11}
\]
This identity holds for all controls, not just linear ramps.
Controls with zero endpoint are \(g_0\)-orthogonal to the linear
ramps \(h(s)=s\,h(T)/T\); (LT11) preserves that orthogonality.
Minimizing at fixed endpoint therefore gives the stiffness and
its full dual
\[
\boxed{\mathsf M_\lambda=D_0^{-1}+\lambda\mathsf H_\lambda,\qquad
\mathsf C_\lambda=\mathsf M_\lambda^{-1}.}
\tag{LT12}
\]
Strict positivity is proved below, not imposed on the Hessian.
The matrix is the minimized **retained-path parameter Fisher**.
It is not the Fisher matrix of the endpoint marginal experiment:
discarding the source paths also projects scores, a different operation
in [[trace-dirichlet-descent/conditional-score-shorting-and-observable-lifts|conditional score shorting]].

The source cometric need not descend pointwise through \(x\).
For invariant smooth real \(f\), its framed endpoint cotangent is
\[
p_f(x,B)_e=
 \left(\operatorname{Ad}_{B_{s(e)}}^{-1}\nabla_{L,e}f(x),
      -\operatorname{Ad}_{B_{t(e)}}^{-1}\nabla_{R,e}f(x)\right).
\]
The conditional frame law is unchanged by the endpoint tilt:
\[
d\beta_x(B)=
\frac{\prod_e p_{a_eT}(B_{s(e)}^{-1}x_eB_{t(e)})}{w_0(x)}\,dB.
\tag{LT13}
\]
The actual returned endpoint tensor is
\[
\boxed{\Gamma_\lambda(f,g)(x)
=\int\langle p_f(x,B),\mathsf C_\lambda p_g(x,B)\rangle\,d\beta_x(B).}
\tag{LT14}
\]
Thus the mean interaction Hessian fixes a finite source cometric,
while conditional frame averaging represents it on the endpoint.
Hidden frame dependence must not be silently removed before this step.

## Coercivity survives every finite smooth tilt

Set
\[
r_-=\inf\rho_\lambda,\quad r_+=\sup\rho_\lambda,\quad
M_V^2=\sup_x\Gamma_0(V,V)(x),\quad b=|\lambda|M_V.
\]
Baseline source duality gives
\(|D_hV|\le M_V\sqrt{g_0(h,h)}\) pointwise.
The bounded correction in (LT5) cannot cancel the unbounded Gaussian
tails of \(S_0(h)\). Hence
\[
\ell_\lambda g_0\le g_\lambda\le u_\lambda g_0,\qquad
\ell_\lambda=r_-c(b)>0,\quad u_\lambda=r_+(1+b)^2,
\tag{LT15}
\]
where
\[
c(b)=\mathbb E[(|Z|-b)_+^2]
=2[(1+b^2)\overline\Phi(b)-b\phi(b)]>0,\qquad Z\sim N(0,1).
\tag{LT16}
\]
For the lower bound use
\(|S_0+\lambda D_hV|\ge(|S_0|-b\sqrt{g_0})_+\)
and \(\rho_\lambda\ge r_-\).
For the upper bound use \(\rho_\lambda\le r_+\) and the \(L^2\)
triangle inequality. Bounded density alone would not control a
changed Fisher score; the Gaussian-tail argument is essential.

There are consequently no new based-factor zero-score directions.
Vertex directions still have exactly zero score, so finite smooth
response again selects precisely the full Gauss-invariant algebra.
Inverting (LT15) and averaging gives
\[
u_\lambda^{-1}\Gamma_0\le\Gamma_\lambda
\le\ell_\lambda^{-1}\Gamma_0.
\tag{LT17}
\]
The tensor (LT14) is smooth and gauge covariant: its frame integral
has smooth positive compact kernel and a fixed finite positive matrix.
On invariant observables the form
\[
\mathcal E_\lambda(f,g)=\int\Gamma_\lambda(\bar f,g)w_\lambda\,dx
\tag{LT18}
\]
therefore closes with inherited invariant \(H^1(G^{\mathcal E})\)
domain. Its weighted elliptic generator has invariant \(H^2\)
domain, compact resolvent and unique constant vacuum. Extending
(LT14) to a raw elliptic tensor for this argument is not a declaration
that noninvariant raw observables have finite response under the
zero-score vertex actions.

The parent auxiliary inequality and density comparison also yield
\[
\mathcal E_\lambda(f)\ge
\frac{2r_-}{r_+u_\lambda}\operatorname{Var}_{w_\lambda}(f).
\tag{LT19}
\]
This follows by comparing energies to \(\mathcal E_0\) and using
\(\operatorname{Var}_{w_\lambda}(f)\le r_+\operatorname{Var}_{w_0}(f)\).
It does not transfer the old OU clock to the tilted source.
For extensive loop sums, \(\operatorname{osc}V\) and \(M_V\)
generally grow with graph size; this bound supplies no required
uniform interacting thermodynamic or continuum rate.

[[local-interaction-cocycle-and-global-source-response|The local conditional-law construction]]
now avoids a global bounded-density comparison. It derives the actual
finite-support likelihood from an interacting specification, including
boundary terms, and completes the source Fisher operator under a
uniform weighted-Hessian smallness bound. Its inverse has controlled
exterior corrections. This is an interacting fixed-graph response
construction, not a uniform physical gap or a repair of the subdivision
obstruction below.

[[physical-vacuum-lift-and-fisher-comparison|Supplying the actual physical vacuum]]
is a different finite-source calibration. The preparing potential
need only be common-conjugation invariant for the entropy identity.
Haar one-link marginals cancel its heat-prior Hessian, leaving
the positive endpoint score covariance of the physical density.
The resulting clock is not identical to physical evolution, but
its calibrated form lies below the physical form with a
volume-uniform reverse comparison at fixed coupling ratio.

## An exact \(SU(2)\) mobility is fixed by the same state

Take one self-loop edge, \(Q=-2\operatorname{Tr}\),
\(t=aT>0\), and
\[
q(Y)=\tfrac12\operatorname{Tr}Y,\qquad V(Y)=1-q(Y),\qquad
m_\lambda=\mathbb E_{\nu_\lambda}q(Y).
\]
Its tilted central endpoint law gives \(\mathbb E_{\nu_\lambda}Y=m_\lambda I\).
For arbitrary controls (LT8) becomes
\[
D=\text{baseline path cost}
+\lambda m_\lambda[1-q(k(T)l(T)^{-1})].
\tag{LT20}
\]
In particular
\[
\mathsf H_\lambda=\frac{m_\lambda}{4}
\begin{pmatrix}I&-I\\-I&I\end{pmatrix}.
\]
Inverting the full matrix in (LT12), not merely a selected score
submatrix, gives for smooth class functions
\[
\boxed{\Gamma_\lambda(f,g)
=\frac{2t}{1+\lambda m_\lambda t/2}
       Q(\nabla f,\nabla g).}
\tag{LT21}
\]
The retained factor split cancels. The denominator is positive for
every finite real \(\lambda\) by (LT15).
For \(\lambda\ge0\), \(m_\lambda\ge m_0=e^{-3t/4}>0\), since
\(\partial_\lambda m_\lambda=\operatorname{Var}_\lambda(q)>0\).

This is an exact state-to-response relation: the same tilted state
determines \(m_\lambda\), hence the mobility.
At zero coupling,
\[
\left.\partial_\lambda\Gamma_\lambda(f,g)\right|_0
=-t^2e^{-3t/4}Q(\nabla f,\nabla g).
\tag{LT22}
\]
For \(f=q\), the heat moments
\[
\mathbb E_0q=e^{-3t/4},\qquad
\mathbb E_0q^2=\tfrac14(1+3e^{-2t}),\qquad
|\nabla q|_Q^2=\tfrac14(1-q^2)
\]
give the decisive comparison with the frozen old response:
\[
\left.\partial_\lambda\right|_0
\left[\mathcal E_\lambda(q)
-\int\Gamma_0(q,q)w_\lambda\,dx\right]
=-\frac{3t^2}{16}e^{-3t/4}(1-e^{-2t})<0.
\tag{LT23}
\]
The common state-density derivative cancels in this difference.
Changing the state while retaining the old electric tensor is
therefore a demonstrably different construction.

## Ordinary subdivision preserves the state but changes this response

Replace the one-edge self-loop by the two-edge cycle obtained by
inserting a new bivalent vertex, with \(t_1+t_2=t\), where
\(t_i=a_iT>0\). This is not an open chain.
Use the same potential \(V=1-q(Y_1Y_2)\) and identify the physical
loop with \(W=Y_1Y_2\). The two weighted physical states agree
exactly for every \(\lambda\): vertex frames cancel, heat times
convolve, and multiplication by the same function of \(W\)
commutes with that pushforward.

Nevertheless their response forms differ. Set
\[
m=e^{-3t/4},\qquad
A=t_1\theta_1+t_2(1-\theta_2),\quad
B=t_1(1-\theta_1)+t_2\theta_2,\quad A+B=t.
\tag{LT25}
\]
At zero coupling, independence and the central heat means give
\[
\mathbb E_0q(k_1Y_1l_1^{-1}k_2Y_2l_2^{-1})
=m\,q(k_1l_1^{-1}k_2l_2^{-1}).
\]
Hence the first Fisher correction is \(m/4\) times the squared norm
of \(\xi_1-\eta_1+\xi_2-\eta_2\).
For \(F=q(W)\), write
\[
w=\nabla_Lq(W)=\nabla_Rq(W),\qquad
z=\operatorname{Ad}_{Y_1}^{-1}w.
\]
Its factor cotangents are \((w,-z,z,-w)\).
Weighting by the unperturbed endpoint cometric makes the displayed
sum of Riesz-control endpoints \(2(Aw+Bz)\).
Differentiating the **complete** inverse in (LT12) therefore gives
\[
\dot\Gamma_{\mathrm{fine},0}(F)=-m|Aw+Bz|_Q^2,\qquad
\dot\Gamma_{\mathrm{coarse},0}(q)=-mt^2|w|_Q^2.
\tag{LT26}
\]
The first expression is in the retained source presentation.
Its conditional frame average supplies the endpoint tensor;
it must not be declared a basic function before that average.
Because \(|w|=|z|\), their source difference is
\[
mAB|w-z|_Q^2.
\]
Writing \(Y_i=(q_i,v_i)\) as unit quaternions gives
\(|w-z|_Q^2=|v_1\times v_2|^2\).
The independent heat factors obey
\[
\mathbb E_0 v_iv_i^T=\tfrac14(1-e^{-2t_i})I_3,
\]
so the exact integrated discrepancy is
\[
\boxed{\left.\partial_\lambda\right|_0
\left[\mathcal E_{\mathrm{fine},\lambda}(F)
      -\mathcal E_{\mathrm{coarse},\lambda}(q)\right]
=\frac38mAB(1-e^{-2t_1})(1-e^{-2t_2})>0.}
\tag{LT27}
\]
The common state-density derivative cancels: at zero coupling the
baseline response already intertwines under subdivision.
Smooth dependence then proves unequal forms for sufficiently small
positive \(\lambda\), not only unequal formal coefficients.
Even \(\theta_1=\theta_2=1/2\) gives \(A=B=t/2\), leaving a strictly
positive discrepancy. It is not repaired by handed symmetry.

Thus this source construction is well-defined on each finite graph
but is not a subdivision-covariant interacting law. Conditional
averaging the hidden frames does not remove the integrated defect.
Repair would have to constrain the interaction and the admissible
source comparisons together, not just copy the same scalar
potential into each equivalent graph presentation.

## What remains a freely supplied action

For any smooth strictly positive gauge-invariant target density
\(w_*\), normalized relative to product Haar, and \(\lambda\ne0\),
the choice
\[
V=-\lambda^{-1}\log(w_*/w_0)
\tag{LT24}
\]
makes (LT2) exactly \(w_*\).
Thus the construction passes fixed-input retuning for the response,
but **fails to select the state if arbitrary \(V\) is permitted**.
This is the [[general-causal-action/research-schema#The next construction: joint selection with restricted primitives|disguised-input test]]
in an actual interacting source family.

A chosen loop weight is not a derivation of an action from nothing.
What has been derived is a joint rule tying that weight to a response
through its averaged geometric Hessian, instead of appending an
independent generator. The meaningful next constraint is whether
one upstream composition or refinement law restricts \(V\) and
preserves the returned state **and** response across presentations.
Equation (LT27) makes this an operative obstruction, not merely an
unperformed consistency check. Neither finite ellipticity nor a
positive auxiliary gap answers it.

The actual conditional cut law is already available. In the
two-edge source, given \(W=Y_1Y_2\),
\[
d\beta_W(Y_1)
=\frac{p_{t_1}(Y_1)p_{t_2}(Y_1^{-1}W)}{p_t(W)}\,dY_1.
\tag{LT28}
\]
The loop tilt cancels from this normalized conditional law.
[[conditional-fisher-coercivity/measure-preserving-horizontal-lifts#A law-preserving lift has the marginal likelihood|The likelihood of a law-preserving horizontal lift]]
is now computed: it equals the endpoint marginal likelihood.
It therefore discards retained-path score information and changes
this source experiment even before a tilt. That endpoint-only
repair is ruled out, not an outstanding test.

[[source-action-transport-through-ordered-cuts|Transporting the complete source]]
does preserve its actual interacting likelihood and response
through ordered cuts, with explicitly derived prefix-dependent
actions. The same work realizes the unweighted ordered law as
a paired-edge-chain response. But independently assigning new
edge actions changes the tilted response by another strictly
positive first-order defect, even on that realized chain.
Thus the unresolved obligation is selection of a compatible
interaction-and-comparison law, not existence of an arbitrary
conditional lift or equality of the unweighted tensors.

[[receipts/two_sided_fisher_receipt.py|The source-response receipt]]
checks the \(SU(2)\) heat moments, shifted matrix characters,
finite entropy Hessian, inverse-matrix identities and the positive
subdivision discrepancy by independent heat moments. These finite
checks do not prove the path likelihood theorem, form domains,
refinement compatibility or a Yang--Mills realization.
