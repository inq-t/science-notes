# A Positive Spectral Modulus Need Not Integrate to a Response

Taking the absolute value of a signed linear response produces a positive operator. For a response varying with configuration, the same operation can destroy the differential compatibility required of a Hessian. This happens already for the cubic determinant in the homogeneous gauge construction, away from every zero eigenvalue. A positive quantum realization therefore requires a compatible response law, not merely a pointwise choice of positive eigenvalues.

## Positivity and integrability are different requirements

Work on a convex open set \(U\subset\mathbb R^n\) with its declared flat metric. A gradient response is \(N=\nabla W\), with \(W\in C^3(U)\), and its linearization is the symmetric field
\[
H(q)=DN(q)=\operatorname{Hess}W(q).
\tag{AH1}
\]
For a constant symmetric invertible matrix \(H\), the modulus
\(|H|=(H^2)^{1/2}\) is the Hessian of
\(\tfrac12 q^T|H|q\). This is the linear signed-to-positive construction used in the free boundary member.

For a \(C^1\) symmetric matrix field \(B(q)\), there is a local \(C^3\) function \(W_+\) with \(\operatorname{Hess}W_+=B\) if and only if
\[
\boxed{\partial_k B_{ij}=\partial_j B_{ik}\quad
\text{for every }i,j,k.}
\tag{AH2}
\]
On the convex set this condition also suffices globally. Indeed, each row one-form \(\sum_j B_{ij}\,dq_j\) is closed, so it integrates to a component \(N_{+,i}\). Symmetry of \(B=DN_+\) then makes \(\sum_i N_{+,i}\,dq_i\) closed, and a second integration gives \(W_+\). The function is determined up to an affine term.

Positive definiteness of \(B\) adds strict convexity after this construction; it does not establish (AH2). Nor does existence of a local convex function prove that its exponential is globally normalizable. These are separate conditions on the response and its carrier.

This theorem concerns ordinary Hessians in a fixed affine carrier. A curved configuration metric requires the corresponding covariant compatibility equations and is not covered by silently replacing partial derivatives.

## The obstruction occurs in the determinant gauge member

On the diagonal homogeneous \(SU(2)\) carrier, the normalized transgression is
\[
W(x,y,z)=xyz,\qquad
N=(yz,xz,xy),\qquad
H=
\begin{pmatrix}
0&z&y\\ z&0&x\\ y&x&0
\end{pmatrix}.
\tag{AH3}
\]
The normalization and its connection to the magnetic action are derived in
[[directed-analytic-realization/chern-simons-response-and-gauge-action|the gauge-response construction]].

At \(a=(q,q,q)\), \(q>0\), let \(\mathbf 1=(1,1,1)^T\) and \(P=\mathbf1\mathbf1^T/3\). Then
\[
H(a)=q(3P-I),\qquad
|H(a)|=q(I+P).
\tag{AH4}
\]
The eigenvalues of \(H(a)\) are \(2q,-q,-q\). Thus \(B=|H|\) is smooth and strictly positive in a neighborhood of \(a\); no eigenvalue crossing or singular spectral cut is involved.

For a symmetric perturbation \(E\), differentiation of the spectral modulus at this matrix gives
\[
\begin{aligned}
D|H|[E]
&=PEP-(I-P)E(I-P)\\
&\quad+\frac13\big(PE(I-P)+(I-P)EP\big)\\
&=-E+\frac43(PE+EP)-\frac23PEP.
\end{aligned}
\tag{AH5}
\]
The coefficients are the derivative \(+1\) on the positive block, \(-1\) on the negative block, and the divided difference
\((|2q|-|-q|)/(2q+q)=1/3\) on the mixed blocks. Degeneracy within the negative block causes no ambiguity because the modulus is smooth there.

Write \(E_y=\partial_yH\), with entries \(13,31\) equal to one, and \(E_x=\partial_xH\), with entries \(23,32\) equal to one. Substitution in (AH5) yields
\[
\left.\partial_y B_{11}\right|_a=\frac{20}{27},
\qquad
\left.\partial_x B_{12}\right|_a=\frac8{27}.
\tag{AH6}
\]
Their difference is \(4/9\), contradicting (AH2). Therefore
\[
\boxed{|\,\operatorname{Hess}(xyz)\,|
\text{ is not the Hessian of any local potential near }a.}
\tag{AH7}
\]

This is also an obstruction on the full nine-dimensional matrix carrier. At every diagonal matrix, the diagonal subspace reduces the self-adjoint derivative of the cofactor map. Functional calculus preserves that reducing subspace, so restricting the full modulus gives exactly (AH3)–(AH7). If the full modulus were a Hessian, its restriction would be one too.

The constant volume factor in the transgression is canceled by the same factor in the configuration metric. It does not repair the incompatible derivatives. At \(qI\), diagonal variations are also Gauss-horizontal: the obstruction is not obtained by inserting a pure gauge tangent.

## Preserving the squared response is not enough either

Another attempted completion rotates the response itself:
\[
\widetilde N(q)=\operatorname{sgn}(H(q))\,N(q).
\tag{AH8}
\]
Where \(H\) is invertible this preserves \(\|\widetilde N\|=\|N\|\), hence the classical squared-response potential. But the configuration-dependent rotation need not preserve closedness.

For an elementary explicit check, take \(W(x,y)=x^2y\) on \(x>0\). Set \(r=(y^2+4x^2)^{1/2}\). Its Hessian has one positive and one negative eigenvalue, and
\[
\operatorname{sgn}(H)=\frac1r
\begin{pmatrix}y&2x\\2x&-y\end{pmatrix},
\qquad
\widetilde N=\frac1r
\begin{pmatrix}2x(y^2+x^2)\\3x^2y\end{pmatrix}.
\tag{AH9}
\]
Direct differentiation gives
\[
\partial_x\widetilde N_2-\partial_y\widetilde N_1
=\frac{2xy(2y^2-x^2)}{(y^2+4x^2)^{3/2}}.
\tag{AH10}
\]
At \((1,1)\) this equals \(2/(5\sqrt5)\ne0\). The rotated field preserves the magnetic-style potential exactly, but it is not the gradient of a local scalar response. Integrating it along different paths gives different answers.

The two attempted prescriptions differ: \(D\widetilde N\) contains the derivative of \(\operatorname{sgn}(H)\), so it need not equal \(|H|\). Both failures must be checked independently.

## What a positive completion must actually construct

The [[algebra/nonlinear-response-and-clock-realization|nonlinear response theorem]] needs a closed response to connect its graphs, normal continuation and squared-response clock. The
[[algebra/response-factorization-and-the-vacuum|factored quantum realization]] additionally needs a measure, domain and normalizable state, with a divergence correction to the classical squared-response potential.

A proposed completion must therefore construct the response as a compatible field over configurations, not select its spectrum independently in each tangent fiber. If it is meant to preserve a given classical action, it must also prove its squared-response identity; if it is meant to select the quantum vacuum, it must satisfy the appropriate quantum equation and global state conditions.

Neither (AH7) nor (AH10) excludes a different positive boundary-state construction. A [[algebra/positive-boundary-response-from-decaying-extensions|decaying-extension theorem]] constructs a compatible positive local response from analytic nondegenerate finite-dimensional data without prescribing its Hessian pointwise. At a quartic degenerate origin, [[directed-analytic-realization/quantum-response-regularity-at-the-gauge-origin|the regularity test]] instead distinguishes an obstructed smooth classical minimum from the actual quantum vacuum's smooth positive local response. No theorem here requires that vacuum's logarithm to have a positive Hessian everywhere. What fails is the claim that the linear absolute-value prescription automatically supplies the nonlinear construction.

[[directed-analytic-realization/nonlinear_response_receipt.py|The finite receipt]] checks the exact rational mismatch in (AH6), an independent spectral finite difference, and the norm-preserving but nonclosed field in (AH9). The compatibility proof above, not numerical sampling, establishes the obstruction.
