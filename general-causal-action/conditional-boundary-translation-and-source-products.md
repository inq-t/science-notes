# Conditional Boundary Translation and Source Products

Eliminating one face from the actual four-face vacuum has a determined first correction: translate its inherited conditional Gaussian mean by a quadratic Lie-bracket field. The same conditional covariance fixes all polynomial source products. Retaining this message on a three-face boundary makes the two elimination orders return the original joint readout; passing only a pair mean discards information already at Gaussian order.

**Status: exact conditional first-score identities, a nonlinear-extension obstruction, and actual fixed-patch polynomial-source jets.** [[regional-vacuum-score-and-the-three-face-orientation|VS]] fixes the actual vacuum score. [[regional-conditional-projection-and-the-vacuum-score|VP]] controls the changing conditional projections and finite words on fixed polynomial sources. [[four-face-covariant-route-response|The four-face route calculation]] evaluates the direct and unrepaired pair routes. No conditional update is identified with physical time.

## One omitted face has a translated conditional law

Use the inherited four-face Gaussian covariance \(C\otimes I_{\mathfrak g}\), the positive invariant metric \(Q\), and the actual amplitude score
\[
\alpha=\beta_1T(a,b,c)+\beta_2T(a,b,d)
+\beta_3T(a,c,d)+\beta_4T(b,c,d),
\qquad T(x,y,z)=Q(x,[y,z]).
\tag{BM1}
\]
Here \(a,b,c,d\) denote the face vectors, and the \(\beta_i\) are the full face-score coefficients, not the coefficients of separately marginalized triples. They are fixed in the linked route calculation by VS's mode score and FC's face transformation.

Retain three faces \(S\) and omit \(r\). In the containing Gaussian law put
\[
m_r=C_{rS}C_{SS}^{-1}X_S,\qquad
\sigma_r=C_{rr}-C_{rS}C_{SS}^{-1}C_{Sr}>0,\qquad
X_r=m_r+\eta_r.
\]
The residual covariance is \(\sigma_r I_{\mathfrak g}\). Since each alternating triple is linear in every face it contains,
\[
L_r(X_S):=\nabla_{X_r}\alpha,\qquad
\boxed{\alpha-\alpha_S=Q(L_r,\eta_r),\quad
\alpha_S=\mathbb E_0[\alpha\mid X_S]=\alpha(X_S,m_r).}
\tag{BM2}
\]
In particular,
\[
L_d=\beta_2[a,b]+\beta_3[a,c]+\beta_4[b,c],
\qquad
L_c=\beta_1[a,b]+\beta_3[d,a]+\beta_4[d,b].
\tag{BM3}
\]
The probability score is twice the amplitude score. The conditional probability's tangent therefore is
\[
2(\alpha-\alpha_S)=2Q(L_r,\eta_r).
\]
This is exactly the tangent of a Gaussian with the same covariance and shifted mean
\[
\boxed{m_{r,h}=m_r+2h\sigma_r L_r.}
\tag{BM4}
\]
Indeed differentiating the Gaussian density with respect to its mean gives
\(Q(\partial_hm_{r,h},\eta_r)/\sigma_r\). The marginal normalization has removed \(\alpha_S\); omitting that subtraction would add a spurious scalar weight. Equation (BM4) is an equality of first jets, not an assertion that the complete interacting conditional law is Gaussian.

For a polynomial mark \(F(X_S,X_r)\), define the finite heat polynomial
\[
H_{\sigma_r}F(X_S,m)
=\left.e^{(\sigma_r/2)\Delta_{X_r}}F(X_S,X_r)\right|_{X_r=m}.
\]
Then the entire conditional source first jet is
\[
\boxed{\mathcal M_{S,h}F
=H_{\sigma_r}F(X_S,m_r)
+2h\sigma_r Q\!\left(L_r,\nabla_mH_{\sigma_r}F(X_S,m_r)\right)
+O(h^2).}
\tag{BM5}
\]
On the actual compact carrier the remainder is interpreted after multiplication by the actual vacuum amplitude, in VP's norm. It is \(O(h^2)\) for every specified fixed polynomial source and its GM compact realization. Take weighted vacuum accuracy before multiplying the scaled marks. This is a compatible family of finite-source statements, not a uniform estimate over all polynomial degrees.

## The message retains source products

For two polynomials in the omitted vector, with retained variables held fixed, Gaussian Wick contraction gives
\[
\begin{aligned}
H_\sigma(FG)(m)
=\sum_{n\ge0}\frac{\sigma^n}{n!}
\sum_{i_1,\ldots,i_n}
&\bigl(\partial_{i_1}\cdots\partial_{i_n}H_\sigma F\bigr)(m)\\
{}\times&
\bigl(\partial_{i_1}\cdots\partial_{i_n}H_\sigma G\bigr)(m).
\end{aligned}
\tag{BM6}
\]
The sum is finite; the indices refer to a \(Q\)-orthonormal basis. The formula follows by applying the heat operator to a product in two independent variables and retaining its cross derivative. For the first jet, evaluate the right side at \(m=m_r+2h\sigma_rL_r\) and retain terms through degree one in \(h\). In these derivatives \(L_r\) and the retained variables are fixed.

The term \(n=0\) is the product of the separate conditional means. All \(n\ge1\) terms are additional source contractions fixed by the same conditional covariance. Thus BM5 together with BM6 carries the complete product of any prescribed polynomial marks without fitting another response.

For \(S=\{a,b,c\}\), let \(J=[c,d]\) and \(T=Q(a,J)\). Set
\[
\overline J_h=[c,m_d]+2h\sigma_d[c,L_d],
\qquad
\overline T_h=Q(a,\overline J_h).
\]
Then
\[
\mathcal M_{S,h}J=\overline J_h+O(h^2),
\qquad
\mathcal M_{S,h}T=\overline T_h+O(h^2),
\]
\[
\boxed{
\mathcal M_{S,h}(T^2)
=\overline T_h^{\,2}+\sigma_d\|[a,c]\|_Q^2+O(h^2),}
\tag{BM7}
\]
where the square is expanded through first order. For the translated Gaussian proxy in BM4, the centered adjoint covariance is exactly
\[
\operatorname{Cov}_{\rm shift}(J\mid X_S)
=-\sigma_d\,\operatorname{ad}_c^2.
\]
Its corresponding actual raw second-moment return is
\[
\boxed{
\mathcal M_{S,h}\|J\|_Q^2
=\|\overline J_h\|_Q^2+\sigma_d\chi_Q\|c\|_Q^2+O(h^2),
\qquad \chi_Q=\mathfrak F_Q/\dim\mathfrak g.}
\tag{BM8}
\]
The simple-algebra assumption makes the adjoint Casimir scalar. Since \(\operatorname{ad}_c\) is skew for \(Q\), the proxy covariance is positive and independent of its shifted mean. This supplies the covariance's formal polynomial-moment first jet. No additional \(L^2\) estimate for the product of the true conditional means is asserted. Each actual raw moment is justified as its own polynomial-source return, rather than by multiplying an uncontrolled remainder.

Equivalently, the Gaussian conditional characteristic expression for \(J\), through first order, is
\[
\begin{aligned}
\exp\!\left(iQ(u,[c,m_d])
-\frac{\sigma_d}{2}\|[u,c]\|_Q^2\right)
\bigl(1+2ih\sigma_dQ(L_d,[u,c])\bigr).
\end{aligned}
\tag{BM9}
\]
Here it serves as a generator of fixed polynomial moment identities at \(u=0\). No uniform compact return for an unrestricted source parameter is asserted. Substituting \(u=sa\) retains the original scalar \(T\) and its products. The negative quadratic exponent records information absent from the mean.

## Complete the two routes by retaining their boundary

Let \(A=\{a,b\}\), \(B=\{b,c\}\), and \(D=\{a,d\}\). Passing \(J\) only through \(B\) loses its correlation with the omitted face \(a\). The determined repair retains \(a\) in the intermediate message:
\[
S_B=A\cup B=\{a,b,c\},\qquad
S_D=A\cup D=\{a,b,d\}.
\]
Their respective messages are
\[
\boxed{
\begin{aligned}
\mathcal M_{S_B,h}J
&=[c,m_d]+2h\sigma_d[c,L_d]+O(h^2),\\
\mathcal M_{S_D,h}J
&=[m_c,d]+2h\sigma_c[L_c,d]+O(h^2).
\end{aligned}}
\tag{BM10}
\]
Each \(m_r,\sigma_r\) is conditioned on its displayed retained triple. They must not be replaced by the pair-conditioned values used in the unrepaired route.

Let \(E_{R,h}\) be actual conditional expectation given the complete prepared face variables in \(R\). For the full source \(F\),
\[
\boxed{
E_{A,h}E_{S_B,h}F
=E_{A,h}F
=E_{A,h}E_{S_D,h}F.}
\tag{BM11}
\]
These are nested towers. They do not assert \(E_{A,h}E_{B,h}=E_{A,h}\) or equality of the unrepaired nonnested routes. Their strong compact versions follow from VP's finite projection words.

The two first-order integrations can also be verified before returning to the compact model. Since \(\alpha_A=0\),
\[
\begin{aligned}
\partial_h(E_{A,h}E_{S,h}F)\big|_0
={}&2E_A\!\left[(\alpha_S-\alpha_A)E_SF\right]\\
&+2E_AE_S\!\left[(\alpha-\alpha_S)F\right]\\
={}&2E_A[(\alpha-\alpha_A)F].
\end{aligned}
\tag{BM12}
\]
The cancellation uses \(E_A(\alpha_SE_SF)=E_A(\alpha_SF)\). The two terms are respectively the changing triple marginal and the omitted-face translation. Dropping either one changes the law. In each route the remaining integration from \(S\) to \(A\) is itself a one-face Gaussian translation driven by the marginal triple score, with its inherited Schur covariance.

Because \(a\) is retained throughout both repaired routes, BM11 holds for \(Q(a,J)\), \(Q(a,J)^2\), and every other prescribed joint polynomial product. BM7 makes the product test explicit. Closing an adjoint index after a pair-only forgetting step is a different readout; repairing just the vector mean does not repair its squared scalar response.

There is a direct positive witness at the target pair. Write
\(m_c=u a+v b\), \(m_d=w a+z b\), and
\(\Sigma=C_{\{c,d\}\mid\{a,b\}}\). For \(F=T(a,c,d)\), conditional Gaussian contraction gives
\[
E_AF=0,\qquad
\boxed{
E_A(F^2)=
\bigl(v^2\Sigma_{dd}+z^2\Sigma_{cc}-2vz\Sigma_{cd}\bigr)
\|[a,b]\|_Q^2+\chi_Q\det\Sigma\,\|a\|_Q^2.}
\tag{BM13}
\]
Indeed
\(F=Q([a,b],v\eta_d-z\eta_c)+Q(a,[\eta_c,\eta_d])\).
The linear and quadratic residual terms are orthogonal. Their variances give BM13 by the same Casimir contraction as CB10. Since \(\Sigma>0\), the last term is strictly positive for \(a\ne0\). A message containing only the closed Gaussian mean would erase this entire original squared-source response.

## Exact Gaussian promotion fails the joint normalization test

For each omitted face separately, the Gaussian in BM4 is a positive normalized conditional kernel at every \(h\). This does not make all four such kernels the full conditionals of one normalized joint law.

Suppose that, at fixed \(h\ne0\), a strictly positive \(C^1\) probability density \(p_h\) on the entire harmonic carrier \(\mathfrak g^4\) had all four exact conditionals
\[
X_r\mid X_{r^c}\sim
\mathcal N\bigl(m_r+2h\sigma_r\nabla_r\alpha,\sigma_r I\bigr).
\]
Since \(m_r\) and \(\nabla_r\alpha\) are independent of \(X_r\), differentiating these conditional densities gives
\[
\nabla_r\log p_h
=-\frac{X_r-m_r}{\sigma_r}+2h\nabla_r\alpha
=-(C^{-1}X)_r+2h\nabla_r\alpha.
\]
The full gradient is thus determined, so connectedness forces
\[
\boxed{
p_h(X)=Z_h^{-1}
\exp\!\left[-\tfrac12 Q(X,C^{-1}X)+2h\alpha(X)\right].}
\tag{BM14}
\]
Here \(Q(X,C^{-1}X)=\sum_{r,s}(C^{-1})_{rs}Q(X_r,X_s)\).

The actual score \(\alpha\) is a nonzero homogeneous cubic. For either sign of \(h\ne0\), there is an open cone of unit vectors on which \(h\alpha\) is bounded below by a positive constant. Along \(X=R\omega\) in that cone, the exponent in BM14 grows at least as \(cR^3-CR^2\). Consequently
\[
\boxed{Z_h=\infty\quad(h\ne0).}
\tag{BM15}
\]
Thus the four exact translated-Gaussian conditionals admit no joint density in this class. Their local score equations are compatible as gradients, but the resulting weight has no finite normalization.

This rejects an exact nonlinear closure by BM4 alone. It does not reject BM5's first jet, the repaired first-order towers, or the actual compact vacuum. Their higher-order conditional corrections and non-Gaussian tails were never removed. A further construction must obtain those terms from the inherited law; repeated first-order translation cannot stand in for them. This is a normalization obstruction on the unbounded harmonic carrier, not a nonexistence theorem for the original compact model.

## What has become determined

The actual four-face covariance and vacuum score fix the two boundary messages, their quadratic drifts, their residual product contractions and their elimination-order identity. There is no adjustable message coefficient, reset regional preparation, or new clock. This establishes a local composition rule for the conditional first jet of the inherited law, while BM15 rules out treating that jet as its complete nonlinear extension.

[[logarithmic-vacuum-curvature-and-conditional-cumulants|The second conditional correction]] now follows from the actual logarithmic vacuum equation. Its degree-four term forces a fourth conditional cumulant; correcting only the Gaussian mean and covariance cannot return it. Cutoff-log sources have a strictly positive leading coefficient, while the original bounded marks add a cubic coordinate contact and have a negative coefficient when \(A=I\). The proof controls conditional moment products in every fixed finite \(L^p\). [[equal-character-hessians-and-the-nonlinear-source-discriminator|The equal-Hessian family]] detects dependence on the full preparation even when the scale, source map and all first-order data agree.

It does not show that this finite message remains closed under arbitrary spatial refinement, or that its static positive covariance controls a physical energy. [[covariant-source-memory-and-the-first-chronological-response|The first chronological comparison]] now transports the source and projection jets through the original transfer and detects a nonzero mixed exterior response on physical scalar sources. [[two-slice-innovation-geometry/regional-innovation-and-exterior-information-balance|RI]] places that channel in the full innovation forms. [[spatial-block-sewing-and-the-vacuum-cap-response|SB]] additionally retains the actual vacuum caps, source exchange and changed-history lag. Iterating the static conditional translation would select a different evolution unless an independent equality were proved.
