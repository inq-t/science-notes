# Compact Heat-Bridge Fusion Tail

For the Haar heat bridge on \(SU(2)\), the complete two-ended prediction operator is scalar on each Peter--Weyl block. Its numerator is a Casimir-weighted fusion sum, while its denominator is the actual endpoint heat density. This yields an explicit vanishing high-spin prediction tail at fixed heat time. It is a non-Abelian calibration of the required estimate, not a uniform four-dimensional Yang--Mills result.

**Status: [EXACT] Haar heat-bridge identities and analytic tail bound; [NOT ESTABLISHED] after interacting Wilson/Perron dressing or a continuum trajectory.** [[two-boundary-multiplication-and-predictive-tails|The multiplication and insertion theorem]] owns the general operator type and the actual-law normalization.

## Fix the carrier and the heat convention

Use Haar probability on \(G=SU(2)\), spins \(j\in\frac12\mathbb N_0\), and
\[
d_j=2j+1,\qquad c_j=j(j+1),\qquad
h_t(g)=\sum_j d_j e^{-tc_j}\chi_j(g),\qquad t>0.
\tag{HF1}
\]
This declares the Laplacian normalization. The heat time \(t\) is not yet a physical slab length or a cosmic age. The positive smooth central kernel defines \(P_tf(x)=\int h_t(x^{-1}y)f(y)\,dy\).

[[library/spin-network-states-in-gauge-theory/inq|Baez's spin-network construction]] records the \(G\times G\) Peter--Weyl decomposition underlying the complete carrier; its gauge-invariant graph construction requires vertex intertwiners as well as edge representations. Here the full carrier is \(L^2(G)\). Its class-function restriction can model a closed holonomy. It is not a nonconstant gauge-invariant observable on an isolated open tree edge.

Let \(Y\) be the midpoint, \(X,Z\) its independent heat endpoints conditional on \(Y\), and \(K_t f=\mathbb E[f(Y)\mid X,Z]\). In coordinates \(x=X\), \(g=X^{-1}Z\), their joint law is
\[
J(dx,dg)=dx\,h_{2t}(g)\,dg.
\tag{HF2}
\]
Set
\[
A_j(g)=\int h_t(v)h_t(v^{-1}g)D^j(v)\,dv.
\]
The insertion formula gives
\[
K_tD^j_{ab}(x,xg)=
\frac{[D^j(x)A_j(g)]_{ab}}{h_{2t}(g)}.
\tag{HF3}
\]
The law is equivariant under simultaneous left and right translation. Consequently \(S_t=K_t^*K_t\) acts as a scalar on each irreducible \(G\times G\) block \(V_j\otimes V_j^*\). Schur orthogonality fixes that scalar:
\[
\boxed{\gamma_j(t)=
\frac1{d_j}\int_G
\frac{\|A_j(g)\|_{\mathrm{HS}}^2}{h_{2t}(g)}\,dg.}
\tag{HF4}
\]
There are \(d_j^2\) matrix coefficients in this block, but no extra \(d_j^2\) factor in its operator norm. The character \(\chi_j\), of norm one, has the same scalar response.

This character test retains the group-valued endpoints. Passing each endpoint separately to its conjugacy class is a further quotient. [[gauge-quotients-of-midpoint-bridges|The quotient theorem]] proves that this can strictly reduce prediction and need not preserve the diagonalization in (HF4), although the upper operator bounds descend.

## Fusion computes the unweighted numerator

Put
\[
m_{2t}=\min_G h_{2t}>0,\qquad M_{2t}=\max_G h_{2t},\qquad
C_j(t)=\frac1{d_j}\int_G\|A_j(g)\|_{\mathrm{HS}}^2\,dg.
\]
Then
\[
\frac{C_j}{M_{2t}}\le\gamma_j\le
\min\{1,C_j/m_{2t}\}.
\tag{HF5}
\]
These constants are fixed-carrier quantities, not automatically bounds uniform in a growing system.

The numerator has the exact expansion
\[
\boxed{C_j(t)=\frac1{d_j}
\sum_{a,b}d_a d_b N_{ab}^{\,j}
e^{-2t(c_a+c_b)}.}
\tag{HF6}
\]
One proof avoids manipulating matrix-index products. The kernel norm identity is
\[
\|P_tM_fP_t\|_{\mathrm{HS}}^2
=\int f(y)\overline{f(y')}h_{2t}(y^{-1}y')^2\,dy\,dy'.
\tag{HF7}
\]
It follows by integrating over both outer insertion variables. Thus the numerator quadratic form is convolution by \(h_{2t}^2\). Expand this central function into characters and use Schur orthogonality to obtain (HF6).

For \(SU(2)\), the elementary character formula
\(\chi_j(\theta)=\sin((2j+1)\theta)/\sin\theta\) gives
\[
\chi_a\chi_b=\sum_{\substack{j=|a-b|\\\text{step }1}}^{a+b}\chi_j.
\]
Therefore \(N_{ab}^{\,j}=1\) precisely when
\[
|a-b|\le j\le a+b,\qquad a+b+j\in\mathbb Z,
\tag{HF8}
\]
and is zero otherwise. The parity condition is essential. No gap conclusion is supplied by this discrete incidence relation alone.

## A computable complete tail

Parametrize the admissible pairs bijectively by
\[
n=a+b-j\in\mathbb N_0,\qquad
m=a-b\in\{-j,-j+1,\ldots,j\}.
\]
Since \(d_ad_b=(j+n+1)^2-m^2\) and
\(2(c_a+c_b)=(j+n+1)^2+m^2-1\), (HF6) becomes
\[
\boxed{C_j(t)=\frac{e^t}{d_j}
\sum_{n\ge0}e^{-t(j+n+1)^2}
\sum_{m=-j}^{j}\bigl[(j+n+1)^2-m^2\bigr]e^{-tm^2}.}
\tag{HF9}
\]
The inner sum has step one and exactly \(d_j\) terms, also for half-integral \(j\). In particular \(C_0=h_{4t}(e)\); the leading \(j=\tfrac12\) term is \(2e^{-3t/2}\).

Bounding each inner term by \((j+n+1)^2\) yields
\[
C_j(t)\le e^t\sum_{n\ge0}(j+n+1)^2e^{-t(j+n+1)^2}.
\]
For \(R\ge t^{-1/2}\), the summand is decreasing. Its first term plus its integral gives the explicit bound
\[
\mathcal F_t(R)=e^t\left[
\left(R^2+\frac{R}{2t}\right)e^{-tR^2}
+\frac{\sqrt\pi}{4t^{3/2}}\operatorname{erfc}(\sqrt tR)
\right].
\tag{HF10}
\]
The remainder of (HF9) from \(n=N\) onward is at most \(\mathcal F_t(j+N+1)\), once its argument meets the condition. For a half-integer cutoff \(J\), let \(Q_{>J}\) be the complete higher-spin projection. If \(J+\tfrac32\ge t^{-1/2}\), then
\[
\boxed{\delta_{>J}(t)=\|K_tQ_{>J}\|^2
=\sup_{j>J}\gamma_j(t)
\le\min\left\{1,\frac{\mathcal F_t(J+3/2)}{m_{2t}}\right\}
\longrightarrow0.}
\tag{HF11}
\]
This is an actual two-ended tail, including all fusion channels and multiplicities. A numerical use of \(m_{2t}\) needs a certified lower bound; a sampled minimum is not one. At sufficiently large \(t\), the elementary uniform estimate
\[
m_{2t}\ge 1-\sum_{j>0}d_j^2e^{-2tc_j}
\tag{HF12}
\]
is already positive and can be certified by a Gaussian-series tail. At smaller \(t\), positivity of the true minimum remains exact, but (HF12) may be useless.

## A low-spin product exposes the issue

Take \(f(Y)=\chi_1(Y)\) and \(H(X,Z)=\chi_{1/2}(X)\chi_{1/2}(Z)\). Then
\[
K_t^*H=e^{-3t/2}(1+\chi_1),\qquad
\mathbb E_J H=e^{-3t/2},\qquad
\operatorname{Var}_J H=1+e^{-4t}-e^{-3t}.
\]
Testing the centered \(H\) proves
\[
\gamma_1(t)\ge
\frac{e^{-3t}}{1+e^{-4t}-e^{-3t}},
\tag{HF13}
\]
whereas one-ended squared prediction of \(f\) is \(e^{-4t}\). Two fundamental endpoint characters therefore probe a spin-one midpoint channel. This is why a low-spin span cannot silently be called an observable subalgebra.

## What remains after the tail is known

The high-spin projection in (HF11) is a linear approximation tool, not an exact sufficient statistic. In this exactly block-diagonal model, put \(a_J=\min_{0<j\le J}(1-\gamma_j)\). The complete centered floor is exactly \(\min\{a_J,1-\delta_{>J}\}\); it does not require \(a_J>\delta_{>J}\). Strictly positive bridge densities force each nonconstant retained mode to have positive residual, and the tail tends to zero. Together these give a qualitative fixed-\(t\) floor. Its heat normalization and compact carrier were supplied, not derived.

Without such a reducing projection in an interacting comparison, the general-purpose sufficient estimate remains \(a_J-\delta_{>J}\). The stronger condition belongs to that lifting strategy, not to every possible gap proof.

The four-dimensional target is harder: construct a corresponding estimate on the actual gauge-reduced, Perron-weighted midpoint law at fixed physical separation, uniformly in volume, coupling trajectory and cutoff. A Haar heat replacement has no right to inherit that uniformity. Nor does a finite-group or finite-graph calibration prove nontrivial continuum existence. [[gaussian-bridge-gap-calibration/two-boundary-half-smoothing|The Gaussian comparison]] and (HF11) show two concrete shapes such an estimate can take.

[[volume-uniform-fusion-envelopes|Volume-uniform fusion envelopes]] removes the prefactor before taking independent products and extends the heat result to arbitrary compact connected Lie groups. Its general criterion uses the supplied transfer's logarithmic representation weights. [[vacuum-aligned-innovation-completion/heat-envelopes-and-the-vacuum-vector|The vacuum-vector obstruction]] explains why this Haar result cannot simply be dressed into an interacting comparison.

[[receipts/two_boundary_prediction_receipt.py|The receipt]] checks the parity-sensitive fusion enumeration, the reindexed series against class-function quadrature, tail inequalities and the low-spin product moments. Numerical quadrature is a calibration; the infinite tail is established by (HF9)--(HF10), not by truncating a graph of eigenvalues.
