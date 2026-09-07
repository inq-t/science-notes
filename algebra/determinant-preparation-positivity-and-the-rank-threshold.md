# Determinant Preparation Positivity and the Rank Threshold

A smooth positive determinant Hessian need not exponentiate to a positive preparation kernel. On the full cone of positive complex two-by-two matrices, the inverse-determinant sum kernel is positive exactly at exponent zero or at exponents at least one. An elementary differential obstruction and positive integral representations prove this. Restricting to one commuting context or to fixed-trace qubits removes the obstruction. This constrains a whole-to-local preparation geometry; it is not a lower bound on excitation energy.

## The overlap compares two positive presentations

Let \(\Omega=\operatorname{Herm}_2(\mathbb C)_{++}\), with its ordinary
matrix determinant. For real \(\beta\), consider
\[
K_\beta(A,B)=\det(A+B)^{-\beta},\qquad A,B\in\Omega.
\tag{DK1}
\]
Positivity means that every finite matrix \([K_\beta(A_i,A_j)]\) is
positive semidefinite. The sum, not the difference, of presentations
appears. Compare [[lorentzian-spectral-envelope/positive-kernels-and-reflection-positivity|the two kernel tests]].

Normalize the diagonal:
\[
\begin{aligned}
k_\beta(A,B)
&=\frac{\det(2A)^{\beta/2}\det(2B)^{\beta/2}}
{\det(A+B)^\beta}
=e^{-\beta C(A,B)},\\
C(A,B)&=\log\det\frac{A+B}{2}
-\frac12\log\det A-\frac12\log\det B.
\end{aligned}
\tag{DK2}
\]
Positive diagonal congruence makes positivity of \(k_\beta\) equivalent
to that of \(K_\beta\). Concavity of log determinant gives \(C\ge0\),
with equality exactly when \(A=B\). This is a symmetric comparison
cost, not an additive directed entropy-production law.

Simultaneous invertible congruence leaves \(C\) and \(k_\beta\)
unchanged; in particular common scaling cancels. Independent rescaling
of the two presentations generally does not cancel. Thus the overlap
is dimensionless without discarding their relative scale.

## A positive local Hessian is not enough

For Hermitian variations, expansion at \(A>0\) gives
\[
C(A,A+\epsilon X)
=\frac{\epsilon^2}{8}
\operatorname{Tr}(A^{-1}XA^{-1}X)+O(\epsilon^3).
\tag{DK3}
\]
This quadratic form is positive for every \(\beta>0\) after multiplication
by \(\beta\). If normalized feature vectors \(e_A\) realizing (DK2)
exist, their induced real metric is
\[
g_A^{\mathrm{prep}}(X,Y)
=\frac\beta4\operatorname{Tr}(A^{-1}XA^{-1}Y)
=\frac\beta2h_A(X,Y),
\tag{DK4}
\]
where \(h\) is the [[positive-cone-processes-and-the-complex-corner|complex-corner determinant Hessian]].
The equality of quadratic responses does not establish existence of the
feature vectors. Neither is this Hessian the
[[jordan-covariance-and-the-entropy-weighted-ball|SLD or BKM state metric]].

## The exact complex rank-two classification

The claim is
\[
\boxed{K_\beta\text{ is positive on }\Omega
\quad\Longleftrightarrow\quad\beta=0\text{ or }\beta\ge1.}
\tag{DK5}
\]
Here is a direct proof, rather than an inference from positive curvature.

For \(\beta<0\), \(k_\beta(I,2I)=(8/9)^\beta>1\), so the
two-by-two unit-diagonal Gram matrix is not positive.

Write \(A=\left(\begin{smallmatrix}a&z\\\bar z&b\end{smallmatrix}\right)\)
and introduce the constant-coefficient differential operator
\[
\mathcal D=\partial_a\partial_b-\partial_z\partial_{\bar z}
=\partial_a\partial_b-\tfrac14
(\partial_{\operatorname{Re}z}^2+\partial_{\operatorname{Im}z}^2).
\tag{DK6}
\]
Differentiating \((ab-|z|^2)^s\) gives
\(\mathcal D\det(A)^s=s(s+1)\det(A)^{s-1}\). Applying this twice,
\[
\boxed{
\mathcal D_A\mathcal D_BK_\beta(A,B)
=\beta^2(\beta^2-1)\det(A+B)^{-\beta-2}.
}
\tag{DK7}
\]
For a smooth positive kernel, applying the same real differential
functional to its two arguments at the same point must give a
nonnegative number. Indeed its finite-difference approximants are Gram
quadratic forms, and the positive cone is open. At \(A=B\), (DK7) is
negative for \(0<\beta<1\), excluding this entire interval.

At \(\beta=0\), the kernel is the constant one. At \(\beta=1\), the
ordinary complex Gaussian integral supplies
\[
\det C^{-1}=\pi^{-2}\int_{\mathbb C^2}e^{-z^*Cz}\,d^4z,
\qquad C>0.
\tag{DK8}
\]
Substituting \(C=A+B\) realizes the kernel as the Gram pairing of
\(z\mapsto e^{-z^*Az}\). Products give positive integer powers, as in
[[purification-descent-and-the-matrix-response|the complex Gram-law construction]].

For every \(\beta>1\), use coordinate Lebesgue measure
\(dX=da\,db\,d\operatorname{Re}z\,d\operatorname{Im}z\) on
\(\operatorname{Herm}_2(\mathbb C)\). Then
\[
\det C^{-\beta}
=\frac1{\pi\Gamma(\beta)\Gamma(\beta-1)}
\int_{X>0}e^{-\operatorname{Tr}(CX)}
(\det X)^{\beta-2}\,dX.
\tag{DK9}
\]
At \(C=I\), set \(b=t+|z|^2/a\), with \(a,t>0\).
The determinant is \(at\), and the \(z\)-integral is \(\pi a\).
The remaining integrals are \(\Gamma(\beta)\Gamma(\beta-1)\).
Congruence \(X=C^{-1/2}YC^{-1/2}\) contributes Jacobian
\((\det C)^{-2}\), proving (DK9) and positivity. This completes (DK5).

The base field is load-bearing. A real Gaussian contributes a half
power of a real symmetric precision determinant; a complex Gaussian
column contributes a full power here. The half-logdet coefficient of a
positive Hessian cannot be copied into (DK1) as a positive complex-cone
kernel without this test.

## A finite witness uses both scale and noncommuting directions

Let \(h=1/4\), and take six positive matrices
\[
A_\pm=(1\pm h)I,\qquad
B_j=I+h\,v_j\cdot\sigma,
\tag{DK10}
\]
where \(v_j\) are the four tetrahedral vectors
\((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)\).
The \(B_j\) have eigenvalues \(1\pm\sqrt3/4>0\).
For coefficients \((2,2,-1,-1,-1,-1)\), the \(K_{1/2}\) Gram form is
\[
Q=\frac{124}{15}-\frac{64}{\sqrt{78}}-\frac{64}{\sqrt{46}}
+\frac8{\sqrt{13}}+\frac{24}{\sqrt{15}}<0.
\tag{DK11}
\]
The sign can be certified rationally: use lower bounds
\(3.6055<\sqrt{13}\), \(3.8729<\sqrt{15}\) and upper bounds
\(\sqrt{78}<8.8318\), \(\sqrt{46}<6.7824\).
They give
\(Q<-84420832374148/261387268239424095<0\).
Each root bound is verified by squaring. This is a finite negative
Gram witness, not an ill-conditioned floating-point eigenvalue test.

## A restricted local carrier can admit the forbidden exponents

On one fixed commuting diagonal context,
\(K_\beta(A,B)=\prod_{j=1}^2(a_j+b_j)^{-\beta}\) is positive for
every \(\beta>0\), by two scalar Gamma integrals.

More strongly, fix \(t>0\) and restrict to qubit presentations
\(A=tI+x\cdot\sigma\), \(|x|<t\), without varying their trace.
For every \(\beta>0\),
\[
K_\beta(A,B)=\frac1{\Gamma(\beta)}\int_0^\infty
s^{\beta-1}e^{-4t^2s}e^{s|x|^2}e^{s|y|^2}
e^{2s x\cdot y}\,ds.
\tag{DK12}
\]
The last factor is positive definite by its tensor-power expansion.
Multiplication by the separate positive endpoint factors and integration
preserve positivity; convergence follows from \(|x+y|<2t\).
Thus **every positive exponent is admissible on the fixed-trace ball**,
even though that ball contains noncommuting matrices.

On the full cone, \(k_\beta k_\gamma=k_{\beta+\gamma}\), but arbitrary
positive roots fail (DK5). The family is not infinitely divisible.
On the fixed-trace ball it is. The same comparison law can therefore be
locally admissible on a reduced carrier but fail when scale variation
is restored. This is an exact whole-to-local distinction, not yet a
spacetime-locality theorem or an irreversible quotient.

The exponent \(\beta\) is a parameter of the overlap geometry, not the
duration of its preparation process. Failure to take arbitrary kernel
roots does not forbid the genuine positive preparation semigroup
constructed in [[directed-analytic-realization/determinant-cone-preparation-and-the-gapless-return|the cone return]].

## The exceptional generalization has a different threshold

For a simple Euclidean Jordan algebra of rank \(r\) and Peirce dimension
\(d\), the corresponding inverse-determinant sum kernel is positive
exactly for
\[
\beta\in\{0,d/2,\ldots,(r-1)d/2\}\cup((r-1)d/2,\infty).
\tag{DK13}
\]
This is the semigroup-kernel classification in
[[library/complete-monotonicity-for-inverse-powers/inq|Scott–Sokal, Theorem 6.5]],
not merely a statement about scalar Hessians. It gives
\(\{0,4\}\cup[8,\infty)\) for the Albert algebra, with \(r=3,d=8\).
These are admissible representation parameters, not particle masses.

A bare rank-two corner has zero cubic Albert determinant. Inside a
selected complex flag \(B\simeq\operatorname{Herm}_3(\mathbb C)\), let
\(p\) be the rank-two idempotent defining the
[[positive-cone-processes-and-the-complex-corner|corner]]
\(pBp\simeq\operatorname{Herm}_2(\mathbb C)\). A comparison there uses
\(A\mapsto A+c(1-p)\), \(c>0\). The determinant of the sum is
\(2c\det_2(A+B)\); the fixed complement cancels in normalized overlaps.
The positive retraction onto the corner does not in general preserve
determinants. The full Albert positivity condition is stronger than this
particular corner test, and neither selects the physical flag.

[[directed-analytic-realization/determinant_kernel_receipt.py|The determinant-kernel receipt]]
and [[directed-analytic-realization/determinant-kernel-receipt-output.txt|its output]]
check finite identities and the explicit obstruction. The classification
and the fixed-trace exception are proved above or attributed explicitly;
finite sampling does not establish them.
