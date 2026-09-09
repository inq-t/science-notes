# Conditional Replica Cumulants Are Stable Under Amplitude Approximation

An integrated conditional fourth cumulant can be written as one bounded expectation over four conditionally independent replicas. The replica law is Lipschitz in the original joint probability law, without a lower bound on its retained marginal. More strongly, the cumulant is a continuously differentiable functional of the vacuum amplitude with globally Lipschitz derivative. This controls true parameter derivatives of the actual statistic even when an approximate marginal has zero fibers.

**Status: exact measure and Hilbert-space estimates.** [[character-memory-in-the-local-conditional-fourth-cumulant|LCM]] fixes the local physical statistic and its preparation contrast. The present estimates transfer amplitude and amplitude-derivative errors to that statistic. They do not derive those approximation errors or interchange spatial and confinement limits.

## Replica laws do not require a marginal lower bound

Let \(P,Q\) be probability laws on standard Borel spaces \(\mathcal A\times\mathcal Z\). Regular conditional laws define
\[
R_k(P)(da,dz_1\cdots dz_k)
=P_A(da)\prod_{j=1}^kP(dz_j\mid a).
\]
Their values on zero-marginal fibers do not affect \(R_k\). Use
\(d_{\rm TV}(P,Q)=\sup_B|P(B)-Q(B)|\), one half the variation norm. Then
\[
\boxed{
d_{\rm TV}(R_k(P),R_k(Q))
\le k\,d_{\rm TV}(P,Q)+(k-1)d_{\rm TV}(P_A,Q_A)
\le(2k-1)d_{\rm TV}(P,Q).}
\tag{CRA1}
\]

For a proof, dominate both laws by \(M=(P+Q)/2\), disintegrated as
\(M_A(da)K_a(dz)\). Write their densities as \(p,q\), their marginal densities as \(p_A,q_A\), and interpolate \(p_t=(1-t)p+tq\). Relative to \(M_A\prod_jK_a\), the replica density is
\[
r_{k,t}(a,\mathbf z)
=\frac{\prod_jp_t(a,z_j)}{p_{A,t}(a)^{k-1}},
\qquad 0<t<1.
\tag{CRA2}
\]
Both \(p+q=2\) and \(p_A+q_A=2\) almost everywhere on their respective dominating spaces, so the interior denominators are positive. Differentiating CRA2, taking absolute values and integrating gives
\[
\|\dot r_{k,t}\|_1
\le k\|q-p\|_{L^1(M)}
+(k-1)\|q_A-p_A\|_{L^1(M_A)}.
\]
In each numerator term, integration of the other \(k-1\) replicas cancels the denominator. In the marginal derivative term, all \(k\) numerator integrals cancel it. This is an integrated cancellation, not a bound on an inverse marginal. Integrate in \(t\). At either endpoint the replica densities converge pointwise, with zero density where the corresponding marginal vanishes; their integrals are one. Scheffé's lemma gives endpoint \(L^1\) convergence and proves CRA1.

The constant \(2k-1\) is optimal. On two binary coordinates, let
\[
\begin{array}{c|ccc}
& (0,0)&(1,0)&(1,1)\\ \hline
P&1/2&1/2-\delta&\delta
\end{array},
\quad
Q(0,0)=1/2,\quad Q(0,1)=\delta,\quad Q(1,0)=1/2-\delta,
\]
with \(0<\delta<1/2\) and all other masses zero. Here \(d_{\rm TV}(P,Q)=\delta\), whereas
\[
d_{\rm TV}(R_k(P),R_k(Q))
=1-\tfrac12(1+2\delta)^{-(k-1)}
-\tfrac12(1-2\delta)^k
=(2k-1)\delta+O(\delta^2).
\tag{CRA3}
\]

## Four replicas contain the actual centered invariant statistic

Let \(X=X(a,z)\) be a real vector in a fixed inner-product space, with \(|X|\le B_X\). Use the identical source function in every law. On four replicas put \(X_j=X(a,z_j)\), \(D_{12}=X_1-X_2\), \(D_{34}=X_3-X_4\), and
\[
\boxed{
\Xi(a,\mathbf z)
=\tfrac12|D_{12}|^4
-\tfrac12|D_{12}|^2|D_{34}|^2
-(D_{12}\cdot D_{34})^2,\qquad
|\Xi|\le32B_X^4.}
\tag{CRA4}
\]
The bound follows from \(|D_{ij}|\le2B_X\). The kernel is translation invariant in the four vectors and invariant under simultaneous orthogonal transformations.

In each conditional law, let \(m=\mathbb E[X\mid a]\), \(V=\mathbb E[(X-m)\otimes(X-m)\mid a]\), and \(\mu_4=\mathbb E[|X-m|^4\mid a]\). Conditional independence and centering give
\[
\tfrac12\mathbb E[|D_{12}|^4\mid a]
=\mu_4+(\operatorname{Tr}V)^2+2\operatorname{Tr}(V^2),
\]
\[
\tfrac12\mathbb E[|D_{12}|^2|D_{34}|^2\mid a]
=2(\operatorname{Tr}V)^2,\qquad
\mathbb E[(D_{12}\cdot D_{34})^2\mid a]=4\operatorname{Tr}(V^2).
\]
Thus the integrated invariant conditional fourth cumulant is exactly
\[
\boxed{
\mathcal K(P)=
\mathbb E_{P_A}\{\mu_4-(\operatorname{Tr}V)^2-2\operatorname{Tr}(V^2)\}
=\mathbb E_{R_4(P)}\Xi.}
\tag{CRA5}
\]
Actual conditional centering and the actual retained marginal are included, with no Gaussian approximation. In LCM the vectors transform in the adjoint representation, so this closed scalar is a physical invariant.

CRA1 and CRA4 imply the useful safe estimate
\[
\boxed{|\mathcal K(P)-\mathcal K(Q)|
\le448B_X^4\,d_{\rm TV}(P,Q).}
\tag{CRA6}
\]
No positivity condition is imposed on the observable. More generally, an integrated product of \(k\) conditional expectations of bounded signed or complex marks is a marked expectation under \(R_k\). The ordinary cumulant partition formula represents a conditional cumulant of order \(k\) with at most \(k\) replicas; conjugated marks can be included as individual arguments. Positivity is required of the underlying probability laws, not of their source factors.

## The amplitude functional has a bounded Hessian away from zero

Consider a real Hilbert space \(\mathcal H\) and a bounded self-adjoint operator \(\Xi\) on its fourth Hilbert tensor power, with \(\|\Xi\|\le B\). Define
\[
F(p)=
\begin{cases}
\|p\|^{-6}\langle p^{\otimes4},\Xi p^{\otimes4}\rangle,&p\ne0,\\
0,&p=0.
\end{cases}
\tag{CRA7}
\]
It is homogeneous of degree two and satisfies \(|F(p)|\le B\|p\|^2\). In the application \(\Xi\) is multiplication by CRA4 on the conditional four-replica fiber; it need not preserve the symmetric tensor subspace.

Here are explicit dimension-independent derivative bounds. For \(r=\|p\|>0\) and \(Q(p)=\langle p^{\otimes4},\Xi p^{\otimes4}\rangle\),
\[
|Q(p)|\le Br^8,\qquad
\|DQ(p)\|\le8Br^7,\qquad
\|D^2Q(p)\|\le56Br^6.
\]
Indeed the first tensor derivative has norm at most \(4r^3\), the second at most \(12r^2\), on unit directions. Also
\[
\|D(r^{-6})\|\le6r^{-7},\qquad
D^2(r^{-6})[u,v]
=48r^{-10}\langle p,u\rangle\langle p,v\rangle
-6r^{-8}\langle u,v\rangle,
\]
so its Hessian norm is at most \(54r^{-8}\). Applying the product rule gives
\[
\boxed{
\|DF(p)\|\le14B\|p\|,\qquad
\|D^2F(p)\|\le206B\quad(p\ne0).}
\tag{CRA8}
\]
The constants are convenient upper bounds, not optimal ones.

The quadratic bound proves differentiability at zero with \(DF(0)=0\), and the gradient bound makes that derivative continuous. Integrate the Hessian along a segment between two vectors. If the segment passes through zero, split it there and use gradient continuity. Therefore
\[
\boxed{\|DF(p)-DF(q)\|\le206B\|p-q\|.}
\tag{CRA9}
\]
Thus \(F\) is globally \(C^{1,1}\). A second derivative at zero is not asserted.

## Integrate over retained fibers before comparing derivatives

Let a fixed reference joint measure disintegrate as \(\nu(da)K_a(dz)\), and let \(p_a\in L^2(K_a;\mathbb R)\) be a measurable amplitude field. Allow a measurable kernel \(\Xi_a\) with a common operator bound \(B\). On the direct-integral amplitude Hilbert space define
\[
\mathfrak F(p)=\int F_a(p_a)\,\nu(da).
\tag{CRA10}
\]
The bound \(|F_a(p_a)|\le B\|p_a\|^2\) makes this well-defined. CRA8–9 give
\[
\|D\mathfrak F(p)\|\le14B\|p\|,\qquad
\|D\mathfrak F(p)-D\mathfrak F(q)\|\le206B\|p-q\|.
\]
One can verify Fréchet differentiability directly by integrating the Taylor remainder bounded by \(103B\|u_a\|^2\). No fiberwise marginal lower bound or inverse-integrability assumption enters.

For a globally normalized amplitude \(p\), its joint probability law has marginal \(\|p_a\|^2\nu(da)\) and conditional density \(|p_a(z)|^2/\|p_a\|^2\). Therefore CRA7 supplies exactly the four-replica density after the marginal is included:
\[
\boxed{\mathfrak F(p)=\mathcal K(|p|^2)\quad\text{when }\|p\|=1.}
\tag{CRA11}
\]
Zero fibers contribute zero. An amplitude may change sign; its squared law remains positive. For an unnormalized nonzero amplitude the probability statistic is \(\mathfrak F(p)/\|p\|^2\), so normalization and its derivative must first be retained.

For differentiable amplitude families \(v,q\), the chain rule and CRA9 yield the true derivative comparison
\[
\boxed{
|D\mathfrak F(v)[v']-D\mathfrak F(q)[q']|
\le14B\|v\|\|v'-q'\|
+206B\|v-q\|\|q'\|.}
\tag{CRA12}
\]
Here the common reference fibers and source kernel are held fixed under differentiation. A parameter-dependent source would contribute its own kernel derivative.

In the physical application, use the common Haar face fibers and the same original scaled compact mark \(\widehat X_h=2q_\rho/h\). Its uniform bound is \(B_X\le C_\rho/h\); hence \(B\le32B_X^4=O(h^{-4})\). Normalized actual and approximate vacuum amplitudes satisfy
\(d_{\rm TV}(|v|^2,|q|^2)\le\|v-q\|_2\), so CRA6 already transfers their statistic values. CRA12 additionally transfers parameter derivatives once both amplitude and amplitude-derivative errors are proved. Arbitrarily accurate positive squared-quasimode laws are therefore sufficient even if their retained marginal vanishes on some fibers. The analytic accuracy, spatial dependence and choice of confinement window remain obligations of the compact approximation theorem.
