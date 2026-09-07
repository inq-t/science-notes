# Purification Descent and the Matrix Response

A unit sphere of complex matrices descends, by taking its Gram matrix, to the full body of finite-dimensional density matrices. The same quotient pushes forward round measure to a determinant-weighted law and the normalized spherical Laplacian to a differential operator whose quadratic response is exactly Jordan covariance. Its inherited self-adjoint realization has a complete polynomial spectrum and a computable positive threshold. For a two-level system with four purification columns, the law, operator and realization coincide with the octonionic-corner ball construction. This is a finite matrix-state response, not yet a spacetime field theory; the round law, matrix dimensions and rate normalization remain declared inputs.

## The quotient and its carrier

Fix integers \(K\ge d\ge2\). Give
\[
\mathcal Z=\mathbb C^{d\times K}
\]
the real Euclidean metric \(\operatorname{Re}\operatorname{Tr}(V^*W)\), and let
\[
\mathbb S=S^{2dK-1}=\{\Psi:\operatorname{Tr}\Psi\Psi^*=1\}
\]
carry normalized round measure \(\sigma\). Define
\[
Q:\mathbb S\longrightarrow\mathcal D_d,\qquad
Q(\Psi)=\rho=\Psi\Psi^*,
\qquad
\mathcal D_d=\{\rho=\rho^*\ge0:\operatorname{Tr}\rho=1\}.
\tag{PM1}
\]
The assumption \(K\ge d\) makes \(Q\) onto the entire state body, including its boundary. Its interior has real dimension \(r=d^2-1\).

The right action \(\Psi\mapsto\Psi V\), \(V\in U(K)\), preserves \(Q\), the round metric and \(\sigma\). Conversely, equal Gram matrices give purifications related by such a unitary: use singular-value decompositions, then extend the resulting partial isometry on the column space to \(\mathbb C^K\). Thus each fiber is exactly one \(U(K)\) orbit. At rank \(s\) the orbit is \(U(K)/U(K-s)\); it need not be a free group orbit or a torsor.

Left multiplication by \(W\in U(d)\) instead gives \(Q(W\Psi)=W\rho W^*\). The measure and returned generator below are equivariant under this visible change of matrix frame.

Set \(\nu=Q_*\sigma\). Pullback is an isometry
\[
\mathsf U:L^2(\mathcal D_d,\nu)\longrightarrow L^2(\mathbb S,\sigma),
\qquad \mathsf Uf=f\circ Q,
\tag{PM2}
\]
whose image is the closed subspace of right-\(U(K)\)-invariant functions. Its adjoint \(\mathsf U^*\) averages over the conditional fiber law. The projection \(\mathsf U\mathsf U^*\) is Haar averaging over \(U(K)\), and has a genuine kernel: for example, a nonzero linear coordinate of \(\Psi\) has zero fiber average. Pullback itself is injective. These are different operations and different claims about forgetting.

The operator below acts on functions of matrix states \(\rho\), not on vectors in \(\mathbb C^d\), spatial positions, or a presumed mass phase space. The earlier [[sphere-to-ball-descent-and-the-jacobi-response|sphere-to-ball construction]] is the corresponding coordinate-projection model.

## The determinant law follows from the same map

Relative to the Euclidean Hilbert--Schmidt volume \(d\rho_{\mathrm{HS}}\) on the affine hyperplane \(\operatorname{Tr}\rho=1\), the pushforward law is
\[
\boxed{
d\nu(\rho)=c_{d,K}(\det\rho)^{K-d}\,d\rho_{\mathrm{HS}},
\qquad \rho>0,
}
\tag{PM3}
\]
where \(c_{d,K}>0\) normalizes total mass to one. There is no boundary atom; rank-deficient states remain in the support. In particular, \(K=d\) gives the flat Hilbert--Schmidt law.

Here is a derivation that does not posit a second physical law. Introduce an auxiliary complex matrix \(Z\) with independent standard complex Gaussian entries. Its direction \(\Psi=Z/\|Z\|_{\mathrm{HS}}\) has exactly round law, independently of its radius. This is a device for integrating round measure, not an assertion of stochastic ontology.

Put \(W=ZZ^*\). For every positive semidefinite Hermitian \(T\), the elementary columnwise Gaussian integral gives
\[
\mathbb E e^{-\operatorname{Tr}TW}=\det(I+T)^{-K}.
\tag{PM4}
\]
To identify its density, consider
\[
I(S)=\int_{W>0}e^{-\operatorname{Tr}SW}
(\det W)^{K-d}\,dW_{\mathrm{HS}},\qquad S>0.
\]
The congruence substitution \(W=S^{-1/2}XS^{-1/2}\) has real Hermitian Jacobian \((\det S)^{-d}\). To check the exponent, diagonalize the positive congruence matrix: a diagonal Hermitian coordinate scales by \(c_i^2\), while the two real coordinates of each off-diagonal entry contribute \((c_ic_j)^2\). Their product is \(|\det C|^{2d}\).

The determinant power supplies the remaining factor, so
\[
I(S)=(\det S)^{-K}I(I).
\tag{PM5}
\]
The integral \(I(I)\) is finite: \(K-d\ge0\), the determinant power is bounded by a power of the trace, and the exponential controls infinity. The normalized candidate density \(e^{-\operatorname{Tr}W}(\det W)^{K-d}/I(I)\) therefore has Laplace transform (PM4). Uniqueness of the finite-dimensional Laplace transform identifies the law of \(W\).

The column count \(K\) is an integer here. Extending the inverse
determinant to arbitrary real exponents requires a separate positivity
test: [[determinant-preparation-positivity-and-the-rank-threshold|the rank-threshold theorem]]
proves the full classification for complex two-by-two matrices, including
its singular rank-one endpoint. A locally positive log-determinant
Hessian does not license every exponent as a whole-cone overlap.

Now write \(W=t\rho\), with \(t=\operatorname{Tr}W>0\). The volume element is
\[
dW_{\mathrm{HS}}=\frac{t^{d^2-1}}{\sqrt d}\,dt\,d\rho_{\mathrm{HS}}.
\tag{PM6}
\]
Indeed, the coordinate along the trace direction is \(t/\sqrt d\); each of the \(d^2-1\) tangent coordinates scales by \(t\). Since \(\det(t\rho)=t^d\det\rho\), the joint density factors as
\[
e^{-t}t^{dK-1}\,dt\;\cdot\;
(\det\rho)^{K-d}\,d\rho_{\mathrm{HS}}.
\]
The normalized Gram matrix of \(Z\) is also \(Q(\Psi)\), proving (PM3).

This derivation determines a measure on the matrix-state carrier. It does not interpret \(-\log\det\rho\) as a unique entropy, and it does not replace the logarithmic Hessian by a diffusion covariance without checking their types.

## The induced quadratic response is Jordan covariance

Choose the nonpositive whole generator
\[
\mathcal G=\frac14\Delta_{\mathbb S}.
\tag{PM7}
\]
For Hermitian \(A\), define the affine matrix-state function and its pullback by
\[
f_A(\rho)=\operatorname{Tr}\rho A,\qquad
F_A(\Psi)=\mathsf Uf_A=\operatorname{Tr}\Psi^*A\Psi.
\]
The real ambient gradient is \(2A\Psi\), so the spherical gradient is
\[
\nabla_{\mathbb S}F_A=2(A\Psi-F_A\Psi).
\tag{PM8}
\]
Using
\[
\Gamma_{\mathcal G}(F,G)
=\tfrac12\bigl(\mathcal G(FG)-F\mathcal GG-G\mathcal GF\bigr)
=\tfrac14\langle\nabla_{\mathbb S}F,\nabla_{\mathbb S}G\rangle,
\]
one obtains
\[
\boxed{
\Gamma(f_A,f_B)
=\operatorname{Tr}\rho(A\circ B)
-\operatorname{Tr}\rho A\,\operatorname{Tr}\rho B,
\qquad A\circ B=\tfrac12(AB+BA).
}
\tag{PM9}
\]
The factor \(1/4\) in (PM7) is precisely the normalization making this equality hold with no extra coefficient.

For the drift, \(F_A\) is homogeneous of real degree two in ambient dimension \(N=2dK\), and
\[
\Delta_{\mathbb R^N}F_A=4K\operatorname{Tr}A.
\]
Restricting a quadratic polynomial to the sphere gives
\[
\Delta_{\mathbb S}F_A
=4K\operatorname{Tr}A-4dK F_A.
\]
Consequently,
\[
Lf_A=K\operatorname{Tr}A-dKf_A.
\tag{PM10}
\]
Constants are fixed: \(A=I\) gives \(Lf_I=0\). The same map \(Q\) has supplied both (PM3) and (PM9)--(PM10), rather than fitting a state law to an unrelated operator afterward.

Take a traceless Hermitian Hilbert--Schmidt orthonormal basis \(T_1,\ldots,T_r\). With
\[
x_i=\operatorname{Tr}\rho T_i,\qquad
\rho=\frac Id+\sum_{i=1}^r x_iT_i,
\]
the returned differential expression is
\[
\boxed{
L_{d,K}
=\sum_{i,j=1}^r a_{ij}(\rho)\partial_i\partial_j
-dK\sum_{i=1}^r x_i\partial_i,
\qquad
a_{ij}(\rho)
=\operatorname{Tr}\rho(T_i\circ T_j)-x_ix_j.
}
\tag{PM11}
\]
The matrix \(a\) is positive definite in the interior. For a nonzero traceless Hermitian \(A\), its quadratic form is
\[
\operatorname{Tr}\rho\bigl(A-\operatorname{Tr}(\rho A)I\bigr)^2>0
\qquad(\rho>0).
\]
It can degenerate at the boundary. Its first term in (PM11) is affine in the coordinates, and its homogeneous quadratic term is \(-x_ix_j\).

The covariance's operator type is more precise than a matrix in a chosen chart. At an interior state it is the isomorphism
\[
\boxed{
\mathsf C_\rho:\operatorname{Herm}_d/\mathbb RI
\longrightarrow\{X=X^*:\operatorname{Tr}X=0\},\qquad
\mathsf C_\rho[A]=\frac{\rho A+A\rho}{2}-\rho\,\operatorname{Tr}(\rho A).}
\tag{PM11a}
\]
The trace pairing makes observable classes the cotangents to the trace-one state space. Its positive form is exactly (PM9), and its kernel before quotienting is the scalar identity. For a state tangent \(X\), solve the Sylvester equation \(X=(\rho\ell_X+\ell_X\rho)/2\). Positivity of \(\rho\) makes this solution unique, and tracing the equation gives \(\operatorname{Tr}(\rho\ell_X)=0\). Thus \(\mathsf C_\rho[\ell_X]=X\), and the inverse metric is
\[
g_\rho^{\mathrm{SLD}}(X,Y)
=\operatorname{Tr}(X\ell_Y)
=\operatorname{Tr}\rho(\ell_X\circ\ell_Y).
\]
The diffusion covariance acts on observable cotangents; the inverse Fisher metric acts on state tangents. They are dual forms, not two endomorphisms on an unidentified common carrier.

The coordinate formula also proves the exact intertwining on polynomials:
\[
\mathcal G\mathsf U=\mathsf U L_{d,K}.
\tag{PM12}
\]
The [[jordan-covariance-and-the-entropy-weighted-ball|qubit covariance and Fisher analysis]] identifies the inverse covariance metric in the two-level case and distinguishes it from the Hessian of a determinant barrier. Those metrics are not interchangeable just because the same determinant appears in a stationary density.

## The realization is inherited, not a boundary guess

Right-\(U(K)\) averaging commutes with the round heat semigroup. Hence the image of \(\mathsf U\) is a reducing subspace for the self-adjoint spherical Laplacian. Define
\[
e^{tL_{d,K}}=\mathsf U^*e^{t\Delta_{\mathbb S}/4}\mathsf U,
\qquad H_{d,K}=-L_{d,K}.
\tag{PM13}
\]
This is a conservative, symmetric Markov semigroup on \(L^2(\nu)\); its generator is the self-adjoint return of the spherical generator. Its closed quadratic form is
\[
\begin{aligned}
\operatorname{Dom}\mathcal E
&=\{f\in L^2(\nu):\mathsf Uf\in H^1(\mathbb S)\},\\
\mathcal E(f,f)
&=\frac14\int_{\mathbb S}|\nabla_{\mathbb S}\mathsf Uf|^2\,d\sigma\\
&=\int_{\mathcal D_d}\sum_{i,j}
\overline{\partial_i f}\,a_{ij}\partial_j f\,d\nu
\quad\text{for polynomial }f.
\end{aligned}
\tag{PM14}
\]
The operator domain is the preimage of the spherical Laplacian domain in the reducing subspace. Constants belong to it. No absorbing condition at \(\det\rho=0\) has been appended to the interior expression (PM11).

The fiber quotient is many-to-one, but the heat semigroup at every finite positive time is injective on \(L^2(\nu)\), as its spectrum below makes explicit. A contractive Markov evolution is not by itself exact finite-time erasure. Its parameter is a chosen response duration; the associated Hilbert unitary group \(e^{-itH_{d,K}}\) is not automatically an automorphism group of the matrix observable algebra or a spacetime clock.

## Exact polynomial spectrum

Let \(\mathcal P_\ell\) be the restrictions to \(\mathcal D_d\) of polynomials of degree at most \(\ell\) in the \(r\) coordinates, and let
\[
\mathcal V_\ell=\mathcal P_\ell\ominus_{L^2(\nu)}\mathcal P_{\ell-1},
\qquad \mathcal P_{-1}=\{0\}.
\]
Because the state body has nonempty interior, there are no nonzero polynomial identities among these affine coordinates. Thus
\[
\dim\mathcal V_\ell=\binom{r+\ell-1}{\ell}.
\tag{PM15}
\]

The operator \(L_{d,K}\) preserves \(\mathcal P_\ell\). On a homogeneous polynomial \(p_\ell\) of degree \(\ell\), its degree-\(\ell\) part is
\[
-\sum_{i,j}x_ix_j\partial_i\partial_jp_\ell
-dK\sum_i x_i\partial_i p_\ell
=-\ell(\ell+dK-1)p_\ell.
\tag{PM16}
\]
The affine part of the covariance lowers polynomial degree. Symmetry of the inherited generator makes \(\mathcal V_\ell\) invariant: its image is orthogonal to \(\mathcal P_{\ell-1}\). Equation (PM16) then implies that
\[
\bigl(L_{d,K}+\ell(\ell+dK-1)\bigr)\mathcal V_\ell
\subseteq\mathcal P_{\ell-1}\cap\mathcal V_\ell=\{0\}.
\]
Therefore
\[
\boxed{
\operatorname{spec}H_{d,K}
=\{\ell(\ell+dK-1):\ell=0,1,2,\ldots\},
\quad
\operatorname{mult}\bigl(\ell(\ell+dK-1)\bigr)
=\binom{d^2+\ell-2}{\ell}.
}
\tag{PM17}
\]

Polynomials separate points of the compact state body and contain constants, so they are uniformly dense in continuous functions and dense in \(L^2(\nu)\). The finite-dimensional spaces \(\mathcal V_\ell\) consequently form a complete orthogonal eigenbasis. If \(f=\sum_{\ell\ge0}f_\ell\), \(f_\ell\in\mathcal V_\ell\), and \(\lambda_\ell=\ell(\ell+dK-1)\), then
\[
\begin{aligned}
f\in\operatorname{Dom}\mathcal E
&\Longleftrightarrow\sum_{\ell\ge0}\lambda_\ell\|f_\ell\|_2^2<\infty,\\
f\in\operatorname{Dom}H_{d,K}
&\Longleftrightarrow\sum_{\ell\ge0}\lambda_\ell^2\|f_\ell\|_2^2<\infty.
\end{aligned}
\tag{PM18}
\]
Spectral truncation proves that polynomials are both a form core and an operator core. This also fixes the relevant closed realization without relying on a formal boundary integration by parts.

The constants are the unique ground eigenspace, and
\[
\mathcal E(f,f)\ge dK\,\|f-\nu(f)\|_2^2,
\qquad \operatorname{gap}H_{d,K}=dK.
\tag{PM19}
\]
The bound is sharp on nonconstant affine coordinates.

This is a restriction of an already-gapped whole. The first nonconstant eigenvalue of \(-\Delta_{\mathbb S}/4\) on all spherical functions is \((2dK-1)/4\), attained by linear functions of \(\Psi\). Such functions are not right-\(U(K)\)-invariant; in particular they change sign under \(\Psi\mapsto-\Psi\). The first nonconstant retained functions are quadratic and have eigenvalue \(dK\). More generally, (PM17) agrees with the spherical degree-\(2\ell\) eigenvalue
\[
\frac14(2\ell)(2\ell+2dK-2).
\]
The quotient raises the first visible threshold by excluding modes; it has not produced a positive threshold from a gapless spherical source.

## The two-level, four-column return

For \(d=2\), use Pauli coordinates rather than the orthonormal coordinates of (PM11):
\[
\rho_x=\frac12(I+x\cdot\sigma),\qquad |x|\le1.
\]
Since \(\sigma_i\circ\sigma_j=\delta_{ij}I\), equations (PM9)--(PM10), at \(K=4\), become
\[
L_{2,4}
=\sum_{i,j=1}^3(\delta_{ij}-x_ix_j)\partial_i\partial_j
-8x\cdot\nabla.
\tag{PM20}
\]
Also \(\det\rho_x=(1-|x|^2)/4\), and Hilbert--Schmidt volume differs from \(dx\) only by a constant. Normalizing (PM3) gives
\[
d\nu(x)=\frac{105}{32\pi}(1-|x|^2)^2\,dx.
\tag{PM21}
\]
The exact spectrum is \(\ell(\ell+7)\), with multiplicity \(\binom{\ell+2}{\ell}\) and gap \(8\).

These are exactly the law and differential expression of the [[sphere-to-ball-descent-and-the-jacobi-response|projection \(S^8\to\overline B^3\)]]. They are also the same self-adjoint realization: both inherit the same complete polynomial eigenspaces with the same spectral domains (PM18). Equality is therefore stronger than a match of interior coefficients or first eigenvalues.

There is an exact common-parent factorization, not only an equality of returned coefficients. [[octonionic-hopf-descent-and-the-complex-purification|Octonionic Hopf descent]] identifies the normalized amplitudes \(\mathbb C^{2\times4}\cong\mathbb O^2\), after selecting a complex unit, and proves \(Q=q_e\circ h\) with \(h:S^{15}\to S^8\). The normalized whole generator \(\Delta_{15}/4\) returns \(\Delta_8\), which then returns (PM20). This diagram starts at the amplitude sphere; it does not assert that the intermediate octonionic Hopf map factors through the selected complex projective phase quotient merely because the final Gram map does.

The full carrier \(L^2(\nu)\) has all polynomial degrees. Its affine subspace models matrix expectations, but it is not the finite-dimensional qubit observable algebra itself. A finite qubit channel obtained from the affine return and the complete differential response are related constructions, not the same operator on the same carrier.

## What the construction fixes

Once \(d\), \(K\), the normalized round geometry and (PM7) are selected, the Gram quotient jointly fixes the visible state body, determinant law, covariance, drift and closed spectrum. This extends the qubit example to every full complex matrix-state body; it does not independently prescribe a density and then search for a compatible gap.

What remains supplied is substantial. The construction does not select the complex matrix algebra, the purification dimension \(K\), the round whole law, or a physical rate unit. Multiplying (PM7) by a positive constant multiplies its entire returned spectrum by that constant. The integers \(d\) and \(K\) here count matrix and purification dimensions, not spacetime dimensions. The assumption \(K\ge d\) is essential to the full-dimensional polynomial argument; rank-constrained images for \(K<d\) require a separate analysis.

The exact result is a whole-to-local response realization with a classified finite-state-space spectrum. An interpretation as causal action, an interacting local field theory, or a Yang--Mills mass gap would require additional structure on this declared carrier and a justified passage to the relevant physical one.

[[partial-trace-clock-consistency-and-the-fluctuation-limit|Partial-trace consistency]]
supplies one exact test of that passage: regrouping the same parent
preserves \(dK\) and its response duration. Growing the environment is a
different operation; the reference law concentrates, while explicitly
rescaled fluctuations retain a Gaussian limit.
[[matrix-symbol-realization-and-the-clock-algebra|The matrix-symbol realization]]
uses those fluctuations for an exact quantum Hilbert isometry and a
faithful positive operator representation. It is not pointwise
multiplication, and its chosen global clock does not preserve the
represented algebra.

[[directed-analytic-realization/purification_descent_receipt.py|The shared purification receipt]]
checks exact finite drift, covariance, polynomial and marginalization
identities. [[directed-analytic-realization/purification-descent-receipt-output.txt|Its output]]
does not replace the density, domain and completeness proofs above.
