# Local Interaction Cocycle and Global Source Response

Compatible interacting conditional laws determine finite-support likelihoods and a global Fisher stiffness without an infinite-product density. Boundary-crossing interactions contribute to every local source change. Under a uniform small-interaction bound, completing and then inverting that stiffness yields controlled exterior corrections and a closed gauge-invariant cylinder response. The interaction, chosen Gibbs state and physical realization remain separate inputs.

**Status: exact local likelihood and Fisher identities; conditional countable completion and inverse-assembly theorem under the displayed bounds.** The parameter indexing the retained heat paths is not identified with physical time. Probability describes the chosen state, without a claim about ontic randomness.

## Specify local laws without a global density

Let the oriented graph be countable and locally finite. Fix a compact
connected group \(G\) with nonzero semisimple Lie algebra, a positive
bi-invariant metric \(Q\), and \(T>0\). On edge \(e\), the reference
source consists of independent based heat paths \(U_e,V_e\) of speeds
\(c_e^U,c_e^V\). For the countable operator statements assume
\(0<c_-\le c_e^A\le c_+<\infty\). The reference endpoint law is
\[
Y_e=U_e(T)V_e(T)^{-1},\qquad
r_e(dy)=p_{(c_e^U+c_e^V)T}(y)\,dy.
\tag{IC1}
\]
The source actions and readout are those of
[[gauge-graph-source-response/haar-vertex-source-and-joint-gauge-response|the Haar-vertex construction]].

Supply smooth real gauge-invariant interactions \(\Phi_X\), supported
on finite edge sets \(X\). Require local finiteness of the interaction
family: every finite edge set meets only finitely many nonzero terms.
The later propagation estimate additionally requires a uniform bound
on their diameters. For finite \(S\), define
\[
H_S(y)=\sum_{X:X\cap S\ne\varnothing}\Phi_X(y),\qquad
\gamma_S(dy_S\mid y_{S^c})
=\frac{e^{-\lambda H_S(y)}}{Z_S(y_{S^c})}
\prod_{e\in S}r_e(dy_e).
\tag{IC2}
\]
An interaction touching both \(S\) and its exterior belongs in \(H_S\).
Terms confined to the exterior cancel from a conditional normalizer.
This makes the specifications compatible under nested conditioning:
\(\gamma_\Lambda\gamma_S=\gamma_\Lambda\) for \(S\subset\Lambda\),
as kernels acting on functions. Arbitrary overlapping updates need
not commute.
No infinite sum \(H(y)\), or global density \(Z^{-1}e^{-\lambda H}\),
is asserted.

There exists a state \(m\) with these conditional laws. To see this,
exhaust the edges by finite sets and use (IC2) with identity exterior.
The compact metrizable product \(G^{\mathcal E}\) gives a weakly
convergent subsequence of endpoint laws. Each fixed conditional
kernel maps continuous cylinders to continuous cylinders and depends
on only finitely many exterior coordinates. The finite-volume
conditional identity therefore passes to the limit, first for
continuous cylinders and then by the monotone-class argument.
Centrality of the heat priors and gauge invariance of each interaction
make these approximants, and the limit, invariant under common
conjugation.

Fix one such common-conjugation-invariant state \(m\). Existence does
not establish uniqueness, extremality, or independence of exterior
preparation. A different Gibbs phase is not automatically the same
primitive state.

## Lift the endpoints with the actual paired bridges

Given \(Y_e=y\), sample \(v=V_e(T)\) with density
\[
\frac{p_{c_e^UT}(yv)p_{c_e^VT}(v)}
     {p_{(c_e^U+c_e^V)T}(y)}\,dv,
\qquad u=U_e(T)=yv.
\tag{IC3}
\]
Then sample independent heat bridges from the identity to \(u\) and
\(v\). These *paired* conditional kernels are independent across
edges given \(y\sim m\); the two paths are not independent conditional
on \(Y_e\) alone. Let \(\nu\) be the resulting countable path law.
This lift is equivariant under common conjugation.

Conditioning on all exterior paths gives exactly
\[
\nu(dz_S\mid z_{S^c})
=\frac{e^{-\lambda H_S(Y(z))}}{Z_S(Y_{S^c})}
\prod_{e\in S}\nu_e^0(dz_e),
\tag{IC4}
\]
where \(\nu_e^0\) is the original paired heat-path law. This follows by
disintegrating the product endpoint prior using (IC3). For each fixed
finite \(S\), the conditional density and its reciprocal have bounds
uniform in the exterior: \(H_S\) is a smooth function on a finite
compact product. Those bounds may grow with \(S\).

## A local likelihood is an exact composition cocycle

Let \(\mathcal T_k\) act by \(U_e\mapsto k_e^UU_e\) and
\(V_e\mapsto k_e^VV_e\), where all controls are deterministic, based,
absolutely continuous and of finite logarithmic energy. Only
finitely many edges \(S\) are changed. Write \(J_0(k;z)\) for the
product of the actual
[[gauge-path-fisher-response/path-shift-fisher-geometry-before-gauge-projection|heat-path likelihoods]].
Then
\[
\boxed{
R_k(z):=\frac{d(\mathcal T_k)_*\nu}{d\nu}(z)
=J_0(k;z)
\exp\{-\lambda[H_S(Y(\mathcal T_k^{-1}z))-H_S(Y(z))]\}.
}
\tag{IC5}
\]
Indeed the exterior is fixed, so the conditional \(Z_S\) in (IC4)
cancels. The conditional change-of-variables theorem proves
normalization before integrating over the exterior. Enlarging \(S\)
does not change the likelihood, because all added unaffected terms
cancel. Inverse controls prove equivalence of the two laws.

For \(\mathcal T_{k\ell}=\mathcal T_k\mathcal T_\ell\),
\[
R_{k\ell}(z)=R_k(z)R_\ell(\mathcal T_k^{-1}z).
\tag{IC6}
\]
The logarithm is thus additive with its argument transported; it is
not generally a sum of independent regional costs. Omitting a
boundary interaction changes this cocycle, not just a convenient
normalization.

All stochastic integrals here involve a fixed finite block.
The uniform-in-exterior bounds for that block transfer Gaussian
moments and justify differentiating the finite-parameter likelihood.
This proves the local theorem without proving quasi-invariance of
arbitrary infinite-support transformations.

## The same state determines the Fisher stiffness

Let \(h=(h_e^U,h_e^V)\) be a finitely supported based Lie-algebra
control, and use the baseline norm
\[
g_0(h,h)=\frac12\sum_{e,A}\int_0^T
\frac{|\dot h_e^A|_Q^2}{c_e^A}\,dt.
\tag{IC7}
\]
The scaled right stochastic logarithms \(C_e^A\) are Brownian under
the reference law, not under \(\nu\). Common conjugation rotates
them by the adjoint action. Their deterministic integrals have
finite expectation by (IC4); semisimplicity forces that expectation
to vanish in the invariant state \(\nu\).

Evaluating (IC5) at the transformed sample therefore gives
\[
\begin{aligned}
D((\mathcal T_k)_*\nu\Vert\nu)
={}&\frac14\sum_{e,A}\int_0^T
\frac{|(k_e^A)^{-1}\dot k_e^A|_Q^2}{c_e^A}\,dt\\
&+\lambda\,\mathbb E_m
\left[H_S((k_e^U(T)Y_e k_e^V(T)^{-1})_e)-H_S(Y)\right].
\end{aligned}
\tag{IC8}
\]
This is the local, infinite-system version of
[[gauge-graph-source-response/loop-correlations-and-the-source-response|the finite-source entropy identity]].
The interaction term need not be positive separately. A
non-conjugation-invariant phase need not obey this simplified formula.

Differentiation at \(k_e^A(t)=e^{\epsilon h_e^A(t)}\) gives
\[
S_\nu(h)=S_0(h)+\lambda D_hH_S,\qquad
S_0(h)=\sum_{e,A}\frac1{\sqrt{2c_e^A}}
\int_0^T Q(\dot h_e^A,dC_e^A),
\tag{IC9}
\]
and
\[
\boxed{g_\nu(h,j):=\mathbb E_\nu[S_\nu(h)S_\nu(j)]
=g_0(h,j)+\lambda\langle Eh,\mathsf H_m Ej\rangle.}
\tag{IC10}
\]
Here \(Eh=h(T)\). The symmetric block matrix \(\mathsf H_m\) is the
averaged Hessian at zero of the endpoint action
\(\Phi_X((e^{\xi_e^U}Y_e e^{-\xi_e^V})_e)\), summed over terms
touching the varied slots. For any finite pair of controls the sum
is finite. Its mean first derivative vanishes by common conjugation,
so the averaged Hessian is independent of second-order coordinate
choices.

Equation (IC10) is a locality statement about *scores*: separated
controls have no Fisher cross term if no interaction meets both.
It does not say that their endpoint observables are independent.
It is not the reverse-conditional Fisher tensor or the
[[rg-covariance-residue/joint-fisher-response-of-normalized-gauge-blocking|covariance subtraction in an effective potential]].

## Complete the control space before inverting

Index the endpoint factor slots by \(i=(e,A)\). On
\(\mathscr K=\ell^2(\{(e,A)\};\mathfrak g,Q)\), put
\[
D_0=\operatorname{diag}_i d_i,\quad d_i=2Tc_i,\qquad
\mathsf B=D_0^{1/2}\mathsf H_m D_0^{1/2}.
\tag{IC11}
\]
A sufficient bound, uniform in the chosen phase, is
\[
C:=\sup_i\sum_j\sqrt{d_i d_j}
\sum_X\sup_y\|\operatorname{Hess}_{ij}\Phi_X(y)\|<\infty.
\tag{IC12}
\]
Only terms involving both slots contribute. Symmetry and the Schur
test give \(\|\mathsf B\|\le C\). The Hessians in (IC12) use the
two-sided action just specified, not an unspecified coordinate norm.
For Wilson words, reuse
[[rg-covariance-residue/nonlinear-conditional-gauge-response|length-weighted path incidence]]:
bounded counts of arbitrarily long words do not suffice. That note's
metric \(-r^{-1}\operatorname{ReTr}\) differs from \(Q=-2\operatorname{Tr}\)
by a factor four for \(SU(2)\).

Assume \(q:=|\lambda|C<1\). Decompose a control into its zero-endpoint
part and its linear ramp \(h(t)=t\,Eh/T\). These parts are orthogonal
for both \(g_0\) and (IC10). On the ramps the normalized stiffness is
\[
\boxed{
\mathsf A=I+\lambda\mathsf B,\qquad
(1-q)I\le\mathsf A\le(1+q)I,\qquad
\mathsf C=D_0^{1/2}\mathsf A^{-1}D_0^{1/2}.
}
\tag{IC13}
\]
The full control norms obey the same comparison with \(g_0\).
Thus the score map extends by continuity to the countable
Cameron--Martin completion, with no new based radical.
This is a completion of infinitesimal scores and observable
cotangents, not an assertion that every completed control integrates
to a quasi-invariant transformation.

## The exterior changes the local inverse

Let \(P\) select a finite set of factor slots and \(P^\perp=I-P\).
The positive operator (IC13) gives the exact Schur identity
\[
\boxed{
P\mathsf A^{-1}P
=\left[
P\mathsf AP-
P\mathsf AP^\perp(P^\perp\mathsf AP^\perp)^{-1}
P^\perp\mathsf AP
\right]^{-1}
}
\tag{IC14}
\]
as an operator on \(P\mathscr K\). The exterior correction is
positive semidefinite. Allowing an exterior control to relax
therefore lowers the least Fisher cost at fixed retained control.
Inverting \(P\mathsf AP\) alone instead freezes that exterior.
This is actual
[[trace-dirichlet-descent/inq#The finite block is a Dirichlet-to-Neumann operator|Fisher shorting]],
not independent resetting of regional experiments.

For an exhaustion \(P_n\uparrow I\), the extended principal-section
inverses
\[
\mathsf C_n=P_n(P_n\mathsf AP_n)^{-1}P_n
\]
increase in quadratic-form order and converge strongly to
\(\mathsf A^{-1}\). One proof maximizes
\(2\operatorname{Re}\langle v,u\rangle-\langle u,\mathsf Au\rangle\)
over \(u\in P_n\mathscr K\). These nested spaces are dense and
\(\mathsf A\) is uniformly coercive. This is Galerkin convergence
for one global state and stiffness, not convergence of independently
chosen free-boundary Gibbs states.

These sections use the unconditional Fisher stiffness of that state.
Conditional Fisher matrices cannot be inverted first and then
averaged to obtain its inverse. A fixed exterior can also break the
conjugation invariance used in (IC8)--(IC10).

Suppose \(\mathsf B\) has propagation at most \(R>0\) in a declared
factor-slot distance. For separated slot sets \(S,F\), the Neumann
series gives
\[
\|P_S\mathsf A^{-1}P_F\|
\le \frac{q^{\lceil\operatorname{dist}(S,F)/R\rceil}}{1-q}.
\tag{IC15}
\]
At \(\lambda=0\), the inverse is exactly the identity. For \(0<q<1\),
let \(S\subset\Lambda\) and
\(N=\lceil\operatorname{dist}(S,\Lambda^c)/R\rceil\). The buffered
local error has the stronger quadratic bound
\[
0\le
P_S\left[\mathsf A^{-1}
-P_\Lambda(P_\Lambda\mathsf AP_\Lambda)^{-1}P_\Lambda\right]P_S
\le \frac{(1+q)q^{2N}}{(1-q)^2}I_S.
\tag{IC16}
\]
Indeed for \(v\) supported in \(S\), let \(x=\mathsf A^{-1}v\) and
let \(x_\Lambda\) be its Galerkin approximation. The quadratic
difference equals \(\|x-x_\Lambda\|_{\mathsf A}^2\), at most
\((1+q)\|P_{\Lambda^c}x\|^2\); apply (IC15).
Bounds for unnormalized cometrics include the explicit
\(D_0^{1/2}\) factors.

This controls inverse tails under the stated smallness assumption.
It does not contradict
[[rg-covariance-residue/conditioned-source-transport|the sparse-precision counterexample]]:
locality without a uniform inverse bound need not survive inversion.

## The complete Gauss cylinder form closes

Add independent Haar frames \(B_v\) and form
\(x_e=B_{s(e)}Y_eB_{t(e)}^{-1}\). Their zero-score actions remain
unchanged. The endpoint output law \(\widehat m\) is gauge invariant.
For a smooth invariant cylinder \(f\), the pullback is exactly \(f(Y)\).
Define its finite-support cotangent by
\[
p_f(Y)_e=(\nabla_{L,e}f(Y),-\nabla_{R,e}f(Y)),\qquad
q_f=D_0^{1/2}p_f,
\]
and the form
\[
\boxed{
\mathcal E_m(f,g)
=\int\langle q_f(Y),\mathsf A^{-1}q_g(Y)\rangle\,m(dY).
}
\tag{IC17}
\]
Use the Hermitian extension for complex observables. This form is on
the full smooth Gauss-invariant cylinder algebra, not on separately
neutralized regional algebras. Its norm is the norm in
\(L^2(\widehat m)^{G^{\mathcal V}}\).

For each fixed edge, (IC2) gives a smooth positive conditional
density relative to Haar whose logarithmic derivative is bounded
uniformly in the exterior. It consists of the heat-density
derivative and finitely many interaction derivatives. Integration
by parts against cylinder tests therefore makes the coordinate
gradient closable in \(L^2(m)\). Testing one edge at a time proves
closability of the square-summed gradient. Moreover
\[
\|q_f(Y)\|^2
=2T\sum_e(c_e^U+c_e^V)|\nabla_e f(Y)|_Q^2.
\]
Uniform equivalence in (IC13) now proves closability of (IC17).
Take its own invariant-cylinder closure. Gauge averaging on
\(\widehat m\) proves density of that core; the chain rule proves
the Markov contraction property, and the constant core vector
makes the form conservative. Its nonnegative self-adjoint generator
is consequently defined by the closed form, not prescribed separately.

The source cotangent need not be basic before conditional averaging
over the endpoint readout. Formula (IC17) defines the integrated
form without postulating an infinite-product version of the finite
frame-density formula. No maximal Sobolev domain, unique vacuum,
or commutation of the source semigroup with readout is asserted.
In particular, the product-OU gap cannot be imported into this
possibly mixed interacting state.

## An interacting local probe detects the omitted exterior

For a finite calibration, take two self-loops at one vertex,
\(G=SU(2)\), \(Q=-2\operatorname{Tr}\), and
\(\Phi=1-q(Y_1Y_2^{-1})\), where \(q(Y)=\tfrac12\operatorname{Tr}Y\).
Write \(Y_i=q_iI-i\,v_i\cdot\sigma\), and in the actual tilted
two-loop state put
\[
\alpha=\mathbb E(q_1q_2),\quad
\beta=\mathbb E(v_1\cdot v_2),\quad
\bar q=\alpha+\beta,\quad \chi=\alpha-\beta/3.
\]
Common conjugation gives
\(\mathbb E(v_{1a}v_{2b})=\delta_{ab}\beta/3\) and zero scalar-vector
cross moments. The Pauli identity
\(\sum_a\sigma_a B\sigma_a=2\operatorname{Tr}(B)I-B\) therefore yields
\[
\mathbb E\,q(A Y_1 B Y_2^{-1})
=\chi q(AB)+\tfrac{4\beta}{3}q(A)q(B).
\tag{IC18}
\]
The actual shifted word has \(A=(k_2^U)^{-1}k_1^U\) and
\(B=(k_1^V)^{-1}k_2^V\). Differentiating (IC18) gives the full
averaged endpoint Hessian
\[
\langle\xi,\mathsf H_m\xi\rangle
=\tfrac14\left[\bar q(|u|^2+|v|^2)-2\chi\,u\cdot v\right],
\quad
u=\xi_1^U-\xi_2^U,\quad v=\xi_1^V-\xi_2^V.
\tag{IC19}
\]
For the genuine local class observable \(f=q(Y_1)\), its source
cotangent is \((w,-w,0,0)\), \(w=\nabla q(Y_1)\).
Thus (IC14) can be tested on an actual invariant derivative rather
than an arbitrary selected matrix vector.

[[gauge-graph-source-response/receipts/local_interaction_assembly_receipt.py|The interaction-assembly receipt]]
evaluates the tilted Haar/heat integrals, checks (IC18)--(IC19)
against actual shifted Pauli words, and compares the full inverse
with the prematurely restricted inverse. These are finite
calibrations, not a simulation of an infinite Gibbs state.

At heat ages \(t_1=0.7,t_2=1.1\), splits
\(\theta_1=0.3,\theta_2=0.6\), and \(\lambda=1\), the computed
moments are \(\bar q=0.437481402048\) and
\(\chi=0.290955602719\). For the local probe at
\(Y_1=0.6I-i(0.48\sigma_1+0.64\sigma_2)\), its response is
\(0.201667584168\) using the restricted *global inverse*, versus
\(0.197968578702\) when the local stiffness is inverted first.
The corresponding integrated form values are \(0.169118538911\)
and \(0.166016551041\). Three positive product quadratures agree;
an independent relative-word heat convolution checks the partition
function and mean. These numbers discriminate two constructions
with the same state, not two candidate mass values.

## What this changes in the programme

The construction removes a global bounded-density assumption and
an independent choice of regional mobility. Once the source
specification, chosen invariant Gibbs state and shift action are
fixed, its likelihood cocycle, Fisher stiffness and full dual
response are tied together. Exterior relaxation is quantitatively
controlled, rather than silently omitted.

It does not select the interaction, graph, heat geometry, phase or
Fisher-dual prescription. Finite-support likelihoods alone do not
select tail/phase data. Nor does this exhaustion of a fixed graph
repair the separate
[[gauge-graph-source-response/loop-correlations-and-the-source-response#Ordinary subdivision preserves the state but changes this response|interacting subdivision obstruction]].
The smallness condition bounds a parameter Fisher operator; it is
not a Poincare inequality for physical states and is not the
weak-bare-coupling Yang--Mills continuum trajectory. The required
vacuum, translation representation, nontrivial four-dimensional
limit and mass gap remain unconstructed.

[[prepared-vacuum-fisher-comparison/physical-vacuum-lift-and-fisher-comparison|The actual-vacuum recovery test]]
supplies a separate finite-regulator bridge to the physical form.
When the exact vacuum is supplied through the paired bridges,
the source Fisher correction is positive and a calibrated
two-sided physical comparison is uniform over spatial boxes at
fixed coupling ratio. The clocks are nonetheless different.
That prepared vacuum is not the finite-range Gibbs state assumed
in (IC2), and its existence and dynamics have not been derived
from the source construction.
