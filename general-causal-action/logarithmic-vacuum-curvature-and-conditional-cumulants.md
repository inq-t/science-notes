# Logarithmic Vacuum Curvature Forces a Conditional Fourth Cumulant

The actual second vacuum coefficient determines the next conditional message. Its logarithm has degree at most four: the apparent sixth-degree amplitude term is exactly the square of the first cubic score. On the four-face patch, the quartic logarithmic coefficient is strictly positive along every nonzero common Lie-algebra direction. It therefore produces a nonzero conditional fourth cumulant for a bounded realization of the logarithmic face coordinate. A Gaussian message with corrected mean and covariance still misses this coefficient. The conclusion uses the actual metric and weighted character cost, and makes no claim that a truncated logarithmic weight is globally normalizable.

**Status: proved fixed-group, fixed-patch second-score and conditional-moment return.** [[conditional-boundary-translation-and-source-products|BM]] owns the first translated conditional Gaussian and its exact nonlinear normalization obstruction. [[all-group-oriented-kinetic-jet-and-source-lift|AJ]] fixes the raw edge rows and first score; [[weighted-character-scale-and-bounded-lie-sources|GM]] keeps the cost and source normalizations distinct. [[fixed-group-compact-vacuum-and-oriented-source-return|GV]] and [[regional-conditional-projection-and-the-vacuum-score|VP]] supply arbitrary finite vacuum accuracy and exact regional algebras. The differential calculation follows the density convention of [[compact-operator-taylor-remainder-on-planar-wells|OT]], without importing its group-specific coefficient values or uniform spatial estimates.

## The second logarithmic coefficient has degree four

Fix GM's compact connected group with simple Lie algebra, invariant metric \(Q\), faithful unitary representation \(\rho\), and positive preparation matrix \(A\) commuting with \(\rho(G)\). All faces use that same declared cost. Keep the four-face comb coordinates \(P_p=\exp(hX_p)\), and put
\[
h=(\kappa/(2I_Ag))^{1/4},\qquad E=\kappa h^{-2}.
\]
After Haar half-density transport, write the local actual operator, before subtracting its vacuum energy, as
\[
\widehat H_h=-\operatorname{div}(\mathsf A_h\nabla)+\mathcal U_h,\qquad
\mathsf A_h=\mathsf A_0+h\mathsf A_1+h^2\mathsf A_2+\cdots,
\quad \mathsf A_0=C^2\otimes I_{\mathfrak g},
\quad C=\sqrt{A_2}.
\tag{LCV1}
\]
Here \(A_2=4I-\operatorname{Adj}_{2\times2}\) is the face incidence matrix; the different symbol \(\mathsf A_2\) denotes the second metric Taylor coefficient. Each \(\mathsf A_r(X)\) is homogeneous of degree \(r\). All divergences and gradients use Euclidean coordinates from \(Q\).

The total scalar term has expansion
\[
\mathcal U_h=\frac14|X|^2+h^2\mathcal U_2+O(h^3),\qquad
\mathcal U_2=U_{\mathrm{Haar},2}+W_4,
\]
\[
W_4(X)=-\frac1{48I_A}\sum_p
\operatorname{Re}\operatorname{Tr}\!\left[A\,d\rho(X_p)^4\right].
\tag{LCV2}
\]
The Haar contribution \(U_{\mathrm{Haar},2}\) is constant. Indeed the scaled logarithmic Haar gradient begins with \(h^2\ell_2(X)\), where \(\ell_2\) is linear, and the exact density scalar is
\(\tfrac12\operatorname{div}(\mathsf A_h\ell_h)+\tfrac14\ell_h^{\mathsf T}\mathsf A_h\ell_h\).
The quartic character form need not be a multiple of \(|X|^4\); its higher representation invariants remain part of the input.

Let \(\Omega\) be the normalized harmonic vacuum, \(s_0=\log\Omega\), and
\[
q=\nabla s_0=-\tfrac12(C^{-1}\otimes I)X,\qquad
\mathcal L_0=-\operatorname{div}(\mathsf A_0\nabla)+(CX)\cdot\nabla .
\]
Use the normalized actual vacuum expansion
\[
\Phi_h=\Omega(1+h\alpha+h^2a_2)+O_{\mathrm{weighted}}(h^3),
\qquad
b=a_2-\frac{\alpha^2}{2}.
\tag{LCV3}
\]
Thus \(h\alpha+h^2b\) is the logarithmic *coefficient* of the amplitude. No norm estimate for the actual logarithm, or global expansion of its pointwise ratio, is being asserted. GV's arbitrarily accurate quasimodes justify (LCV3) with every specified polynomial weight before truncation.

The first score \(\alpha\) is AJ's homogeneous Cartan cubic. Substitution of \(s=s_0+h\alpha+h^2b\) into
\[
e^{-s}\widehat H_he^s
=-\operatorname{div}(\mathsf A_h\nabla s)
-(\nabla s)^{\mathsf T}\mathsf A_h\nabla s+\mathcal U_h
\]
gives
\[
\boxed{\mathcal L_0b=e_2+\mathcal F,}
\]
\[
\begin{aligned}
\mathcal F={}&(\nabla\alpha)^{\mathsf T}\mathsf A_0\nabla\alpha
+\operatorname{div}(\mathsf A_1\nabla\alpha)
+2q^{\mathsf T}\mathsf A_1\nabla\alpha\\
&+\operatorname{div}(\mathsf A_2q)
+q^{\mathsf T}\mathsf A_2q-\mathcal U_2 .
\end{aligned}
\tag{LCV4}
\]
The scalar solvability condition is \(e_2=-\mathbb E_0\mathcal F\). The remaining additive constant of \(b\) is fixed by vacuum normalization:
\[
\boxed{\mathbb E_0b=-\mathbb E_0\alpha^2.}
\tag{LCV5}
\]

Every term of \(\mathcal F\) is even and has degree at most four. The Gaussian Ornstein–Uhlenbeck operator preserves finite polynomial degree and is invertible off constants. Hence \(b\) has degrees \(0,2,4\). In particular
\[
a_2=\frac{\alpha^2}{2}+b
\]
identifies and cancels the entire degree-six part before forming a conditional logarithmic score. This is a finite polynomial Poisson equation, not an inverse of an unknown interacting gap.

## The second conditional message includes connected moments

Retain three complete faces \(S=r^c\). Under the inherited Gaussian law write
\[
X_r=m_r+\eta,\qquad
\eta\sim\mathcal N(0,\sigma_r I_{\mathfrak g}),\qquad
\alpha-\alpha_S=Q(L_r,\eta),
\]
using BM's \(m_r,\sigma_r,L_r\). For a polynomial \(F\), let
\[
\mathcal H_\sigma F(m)=
\left.e^{(\sigma/2)\Delta_r}F\right|_{X_r=m},
\qquad \sigma=\sigma_r,\quad m=m_r.
\]
Conditional normalization of the density coefficient
\(\exp(2h\alpha+2h^2b)\) gives
\[
\begin{aligned}
\log\frac{d\mu_{r|S,h}}{d\mu_{r|S,0}}
={}&2hQ(L_r,\eta)\\
&+2h^2\{b-\mathbb E_0[b\mid S]-\sigma|L_r|^2\}
+O(h^3),
\end{aligned}
\tag{LCV6}
\]
as a normalized moment jet. The last scalar is the normalizer of the first mean translation; it is not a freely chosen potential.

Equivalently, for the conditional cumulant generator with a formal vector source \(t\),
\[
\boxed{\begin{aligned}
\mathcal K_h(t)
={}&Q(t,m)+\frac{\sigma}{2}|t|^2+2h\sigma Q(t,L_r)\\
&+2h^2\{\mathcal H_\sigma b(m+\sigma t)
-\mathcal H_\sigma b(m)\}+O(h^3).
\end{aligned}}
\tag{LCV7}
\]
This formula means its fixed derivatives at \(t=0\); it does not require a moment-generating function for a globally truncated cubic or quartic density.

The mean and covariance coefficients are therefore
\[
\begin{aligned}
\mathbb E_h[X_r\mid S]
&=m+2h\sigma L_r+2h^2\sigma\,\mathbb E_0[\nabla_rb\mid S]+O(h^3),\\
\operatorname{Cov}_h(X_r\mid S)
&=\sigma I+2h^2\sigma^2\,\mathbb E_0[\nabla_r^2b\mid S]+O(h^3).
\end{aligned}
\]
For \(k=3,4\),
\[
\boxed{\operatorname{Cum}_{k,h}(X_r\mid S)
=2h^2\sigma^k\mathbb E_0[\nabla_r^kb\mid S]+O(h^3).}
\tag{LCV8}
\]
Every \(k\ge5\) has zero coefficient through this order. No sign is implied for the covariance correction, or for the third cumulant.

The corresponding source-product rule is explicit:
\[
\begin{aligned}
\mathbb E_h[F\mid S]
={}&\mathcal H_\sigma F(m)
+2h\sigma(L_r\cdot\nabla_m)\mathcal H_\sigma F(m)\\
&+2h^2\sigma^2(L_r\cdot\nabla_m)^2\mathcal H_\sigma F(m)
+2h^2\operatorname{Cov}_0(F,b\mid S)+O(h^3).
\end{aligned}
\tag{LCV9}
\]
The first three terms are BM's translated Gaussian through second order. The final connected contraction is determined by the actual second vacuum equation. Applying (LCV9) to a product retains its own contraction; multiplying separate conditional means would discard it.

## A common Cartan direction isolates a strictly positive quartic

Let \(b_4,\mathcal F_4\) be homogeneous degree-four parts. The degree-four equation from (LCV4) is
\[
(CX)\cdot\nabla b_4=\mathcal F_4,\qquad
b_4(X)=\int_0^\infty\mathcal F_4(e^{-sC}X)\,ds .
\]
Fix \(0\ne H\in\mathfrak g\), and set \(X_p=t_pH\). All brackets between these face vectors vanish, so \(\nabla\alpha=0\). Also, for the exact raw-row matrix \(\mathsf B_h\),
\[
\mathsf B_hq=\mathsf B_0q\quad\text{on }X_p=t_pH .
\]
To verify this last identity, each component \(q_p\) is a scalar multiple of \(H\). The dual logarithmic left/right Jacobian fixes \(H\), as does every connector adjoint built from \(\exp(ht_pH)\). Conjugation tails pair to zero. Applying each actual row to the covector \(q\) therefore gives its constant-row value, at every local \(h\). Since \(\mathsf A_h=\mathsf B_h^{\mathsf T}\mathsf B_h\), it follows that \(q^{\mathsf T}\mathsf A_2q=0\) there. The two divergence terms in (LCV4) have degree two and do not enter this calculation.

Consequently only the magnetic quartic survives on this aligned subspace:
\[
\boxed{
b_4((t_pH)_p)=
\frac{\operatorname{Re}\operatorname{Tr}[A\,d\rho(H)^4]}{48I_A}
\int_0^\infty\sum_p[(e^{-sC}t)_p]^4\,ds.}
\tag{LCV10}
\]
The matrix \(C\) is positive, so the integral is finite and positive for \(t\ne0\). The trace is strictly positive for \(H\ne0\): \(d\rho(H)\) is a nonzero skew-Hermitian matrix, \(A>0\), and \(A\) commutes with it.

Define the fixed geometric number
\[
J_r=\int_0^\infty\sum_p(e^{-sC})_{pr}^{\,4}\,ds>0.
\]
Taking four derivatives only in the omitted face direction \(H\) gives the conditional scalar cumulant
\[
\boxed{
\operatorname{Cum}_{4,h}\bigl(Q(H,X_r)\mid S\bigr)
=h^2\,\sigma_r^4
\frac{\operatorname{Re}\operatorname{Tr}[A\,d\rho(H)^4]}{I_A}
J_r+O(h^3).}
\tag{LCV11}
\]
The coefficient is constant in the retained variables and strictly positive. A Gaussian conditional law, even one whose mean and covariance change at order \(h^2\), has identically zero fourth cumulant and cannot match it. This tests the actual conditional law in the logarithmic coordinate convention used by BM. The positive quartic coefficient does not stabilize an exponential density at infinity; truncation would again require a separate normalization check.

## Actual compact conditional cumulants and source curvature

There is a bounded, smooth, equivariant source realizing this coordinate: choose an \(\operatorname{Ad}G\)-invariant cutoff inside an injective exponential neighborhood, equal to one near the identity, and set
\[
\lambda(P)=\chi(P)\log P
\]
inside that chart, extended by zero. Its scaled mark \(\lambda(P_r)/h\) has exactly the logarithmic jet near the vacuum well. The regional conditioning still uses the *complete face words*, through VP's injective completed chart; it is not conditioning on the possibly noninjective cutoff mark. Fixed components are framed covariant sources. Contracting the fourth tensor with the invariant metric, or averaging its positive directional coefficient over the unit sphere of \(Q\), gives a scalar physical readout.

For every specified finite moment family, the errors in (LCV8)–(LCV11) are actual conditional-function errors in each fixed finite \(L^p\) norm of the moving retained marginal. Here is the additional estimate needed for products of conditional means.

First extend VP's fiber-line Taylor proof to any fixed order \(M\), using the degree-finite vacuum polynomial through that order. On fibers where its perturbation relative to \(\Omega\) is at most \(1/4\), Taylor's formula for the normalized rank-one line has a polynomially weighted \(O(h^{M+1})\) remainder. The complement has Gaussian tails smaller than every fixed power. Arbitrarily accurate weighted vacuum approximation bounds the actual-to-polynomial line error by the same method as VP8. Matching the moving source and output amplitude then gives the conditional-moment expansion through order \(M\) in moving \(L^2\), with error \(O(h^{M+1})\).

Second, every fixed conditional moment has bounded moving \(L^q\) norm for every fixed \(q<\infty\): conditional Jensen reduces this to a full polynomial moment, which the weighted vacuum estimates bound. The polynomial Taylor coefficients have the same bounds. Interpolating a sufficiently high-order \(L^2\) remainder with such a bounded higher \(L^q\) norm gives the desired \(L^p\) accuracy. Truncating afterward at order two leaves \(O(h^3)\). Hölder's inequality now controls the finite products of conditional moments defining the centered covariance and cumulants. Thus (LCV11) has actual moment meaning; it is not deduced by multiplying first-order \(L^2\) remainders.

The original GM mark is a different specified observable at this order:
\[
\widehat X_{\rho,h}=2q_\rho(P)/h
=X+h^2R_\rho(X)+O(h^4),\qquad
R_\rho(X)=\tfrac16(d\rho)^{-1}\Pi_\rho(d\rho(X)^3).
\]
Its fourth cumulant includes the cubic source-curvature contact. Gaussian integration by parts gives
\[
\boxed{\begin{aligned}
\operatorname{Cum}_{4,h}\bigl(Q(H,\widehat X_{\rho,r,h})\mid S\bigr)
=h^2\bigg\{&
\sigma_r^4\frac{\operatorname{Re}\operatorname{Tr}[A\,d\rho(H)^4]}{I_A}J_r\\
&-4\sigma_r^3
\frac{\operatorname{Re}\operatorname{Tr}[d\rho(H)^4]}{I_\rho}
\bigg\}+O(h^3).
\end{aligned}}
\tag{LCV12}
\]
Indeed the additional coefficient is
\(4\sigma_r^3\partial_H^3Q(H,R_\rho)\), and that derivative equals
\(-\operatorname{Re}\operatorname{Tr}[d\rho(H)^4]/I_\rho\).
This term is unrelated to the cost weight \(A\). For \(A=I\), the coefficient in (LCV12) is strictly negative: \(\sigma_r\le\sqrt6\) and \(J_r\le1/(4\sqrt2)\), so \(\sigma_rJ_r<4\). For general weighted \(A\), no common sign is asserted. Both readouts retain the same Hamiltonian and conditioning algebra; the source curvature is stated explicitly rather than absorbed into a vacuum score.

The next conditional message is therefore fixed by \((\alpha,b)\), with metric curvature, Haar normalization and the declared quartic character all retained. Its third and fourth connected moments are additional channels beyond a Gaussian mean and covariance. This is a fixed four-face statement; it supplies no uniform spatial estimate, positive logarithmic global model, replacement evolution, or physical gap bound.

[[equal-character-hessians-and-the-nonlinear-source-discriminator|The equal-Hessian preparation family]] keeps the representation, total weight, quadratic index and original GM source fixed while changing the quartic cost. Its invariant conditional cumulant separates the actual preparations at order \(h^2\), although their first-order data agree.
