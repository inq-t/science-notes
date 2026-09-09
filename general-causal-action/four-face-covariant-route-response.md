# Four-Face Covariant Returns Depend on the Conditional Route

The inherited four-face law fixes the direct conditional return of an adjoint pair mark and both returns through the opposite pair contexts. The direct expression contains a Gaussian bracket, two first-order double brackets and a linear Casimir contraction of the full vacuum score. The composed routes retain both score insertions. They need not agree: the contexts are nonnested, and forgetting an exterior source changes the experiment. All coefficients below belong to the same prepared words, covariance and actual compact vacuum.

**Status: exact Gaussian and first-score formulas, with proved actual fixed-group strong-source return.** [[regional-vacuum-score-and-the-three-face-orientation|VS]] fixes the full oriented score, [[covariant-boundary-source-and-the-oriented-return|CB]] fixes the covariant three-face response, and [[regional-conditional-projection-and-the-vacuum-score|VP]] supplies the actual finite-source projection words. Keep [[weighted-character-scale-and-bounded-lie-sources|GM's weighted cost and scale]]. No new comparison parameter, detached vacuum or clock is introduced.

## The direct return uses both exterior residuals

Let \(x=X_a,y=X_b,z=X_c,w=X_d\), with a positive face covariance \(C\otimes I_{\mathfrak g}\). The compact connected simple group, invariant metric \(Q\) and prepared common-root face transports are fixed. Put
\[
K=[x,y],\qquad
T(x,y,z)=Q(x,[y,z]),\qquad
\chi_Q=\frac{\mathfrak F_Q}{d},\qquad
\mathfrak F_Q=\sum_{\alpha\beta\gamma}f_{\alpha\beta\gamma}^2,
\quad d=\dim\mathfrak g.
\]
Retain the boundary mark \(J_{cd}=[z,w]\), with its adjoint index open. It is not an invariant scalar source by itself.

Write the complete first amplitude score as
\[
\alpha=\beta_1T(x,y,z)+\beta_2T(x,y,w)
+\beta_3T(x,z,w)+\beta_4T(y,z,w).
\tag{DR1}
\]
In particular these \(\beta\)'s are full four-face coefficients, not the marginal coefficients of three-face scores. Conditional on \(A=\{a,b\}\),
\[
\binom zw
=M\binom xy+\binom\xi\zeta,\qquad
M=C_{\{c,d\},A}C_{AA}^{-1},
\qquad
\Sigma=C_{\{c,d\},\{c,d\}}-MC_{A,\{c,d\}}.
\tag{DR2}
\]
Use
\(m_c=M_{11}x+M_{12}y\),
\(m_d=M_{21}x+M_{22}y\), and
\(\mathbb E[\xi^\alpha\zeta^\beta]=\Sigma_{cd}\delta_{\alpha\beta}\).

Define
\[
\ell=\beta_1-M_{22}\beta_3+M_{21}\beta_4,\qquad
m=\beta_2+M_{12}\beta_3-M_{11}\beta_4,\qquad
Z=\beta_3x+\beta_4y.
\]
Alternating multilinearity gives the exact conditional score decomposition
\[
\boxed{\alpha=Q(K,\ell\xi+m\zeta)+Q(Z,[\xi,\zeta]).}
\tag{DR3}
\]
It has zero conditional mean. The first density score is \(2\alpha\), with no marginal subtraction left on this two-face set.

Set
\[
\eta_c=\Sigma_{cc}\ell+\Sigma_{cd}m,\qquad
\eta_d=\Sigma_{cd}\ell+\Sigma_{dd}m,
\]
\[
b_x=M_{11}\eta_d-M_{21}\eta_c,\qquad
b_y=M_{12}\eta_d-M_{22}\eta_c .
\]
Then the complete direct return is
\[
\boxed{
\mathbb E_{A,h}J_{cd}
=(\det M)K
+2h\left\{
b_x[x,K]+b_y[y,K]+\chi_Q\det\Sigma\,Z
\right\}+O(h^2).}
\tag{DR4}
\]
The meaning of the actual compact remainder is specified below.

For a direct derivation, expand
\[
J_{cd}=[m_c,m_d]+[m_c,\zeta]+[\xi,m_d]+[\xi,\zeta].
\]
Its Gaussian mean is \((\det M)K\). The linear-residual part of (DR3) paired with the two linear-residual terms of \(J\) gives
\[
\eta_d[m_c,K]+\eta_c[K,m_d].
\]
The quadratic-residual part paired with \([\xi,\zeta]\) gives
\[
\mathbb E\bigl(Q(Z,[\xi,\zeta])[\xi,\zeta]\mid x,y\bigr)
=\chi_Q\det\Sigma\,Z.
\]
Indeed
\(\mathbb E([\xi,\zeta]\otimes[\xi,\zeta])
=\chi_Q\det\Sigma\,I_{\mathfrak g}\).
All remaining contributions have odd residual degree or an alternating contraction with the color identity and vanish. This explains why no fifth-degree term survives. It also separates the linear Casimir channel from the two cubic double-bracket channels.

## The existing four-face covariance and score fix every coefficient

For the face ordering of the comb owner, set
\[
d_0=\frac{4+\sqrt2+\sqrt6}{4},\qquad
n_0=\frac{\sqrt2-\sqrt6}{4},\qquad
o_0=\frac{\sqrt2+\sqrt6-4}{4}.
\]
The actual harmonic covariance is
\[
\boxed{
C=\begin{pmatrix}
d_0&n_0&n_0&o_0\\
n_0&d_0&o_0&n_0\\
n_0&o_0&d_0&n_0\\
o_0&n_0&n_0&d_0
\end{pmatrix}.}
\tag{DR5}
\]
It is the same \(C=O\operatorname{diag}(\sqrt2,2,2,\sqrt6)O^{\mathsf T}\) as VS. The weighted representation cost has already been absorbed through its declared Hessian scale; its higher-order coefficients are not reset.

Transforming VS16's four mode-score coefficients by the exterior cube of its Hadamard matrix gives
\[
\boxed{
\begin{aligned}
\beta_1&=\frac{27\sqrt2+14\sqrt6-66}{672},&
\beta_2&=\frac{6-5\sqrt2}{224},\\
\beta_3&=\frac{14\sqrt6-27\sqrt2-18}{672},&
\beta_4&=-\beta_2 .
\end{aligned}}
\tag{DR6}
\]
For clarity, that transformation from the coefficient order
\((012,013,023,123)\) to \((abc,abd,acd,bcd)\) is
\[
\frac12
\begin{pmatrix}
1&1&-1&-1\\
1&-1&-1&1\\
-1&-1&-1&-1\\
-1&1&-1&1
\end{pmatrix}.
\]
This retains every term of the full score before conditioning.

For \(A=\{a,b\}\), the regression and residual covariance reduce to
\[
M=\begin{pmatrix}r&s\\s&r\end{pmatrix},\qquad
r=\sqrt2+\sqrt6-4,\quad s=\sqrt2-\sqrt6+1,
\]
\[
\Sigma=\begin{pmatrix}\sigma&\upsilon\\\upsilon&\sigma\end{pmatrix},
\qquad
\sigma=2(\sqrt2-\sqrt6+2),\quad
\upsilon=2r,\quad
\det\Sigma=16(\sqrt2-1)(3-\sqrt6).
\tag{DR7}
\]
For example, the two eigenvalues of \(M\) are \(2\sqrt2-3\) and \(2\sqrt6-5\); those of \(\Sigma\) are \(4(\sqrt2-1)\) and \(4(3-\sqrt6)\). This verifies the regression without a numerical matrix inversion.

Thus (DR4) is an exact finite radical formula: insert
\[
\ell=\beta_1-r\beta_3+s\beta_4,\qquad
m=\beta_2+s\beta_3-r\beta_4,
\]
\[
\eta_c=\sigma\ell+\upsilon m,\qquad
\eta_d=\upsilon\ell+\sigma m,\qquad
b_x=r\eta_d-s\eta_c,\quad b_y=s\eta_d-r\eta_c.
\]
No fitted coefficient remains in the direct response.

## Both composed routes retain their outer score insertion

Let \(B=\{b,c\}\) and \(D=\{a,d\}\). These opposite-face pairs are not nested with \(A\). Put
\[
\lambda=\frac{n_0}{d_0+o_0}=\frac{\sqrt3-2}{2},\qquad
\tau=d_0-\frac{2n_0^2}{d_0+o_0}
=1+\frac{3\sqrt2-\sqrt6}{2}.
\tag{DR8}
\]
Here \(\tau=\operatorname{Var}_0(w^\alpha\mid y,z)
=\operatorname{Var}_0(z^\alpha\mid x,w)\).

The marginal three-face coefficients are also fixed by (DR5)–(DR6). With
\(\mathcal D_3=\sqrt2+2\sqrt3+\sqrt6\), they are:

| Union | Coefficient \(\gamma\) of its alphabetically oriented Cartan triple |
| --- | --- |
| \(abc\) | \((9+3\sqrt2-7\sqrt3)/(28\mathcal D_3)\) |
| \(abd\) | \((3\sqrt2-5)/(28\mathcal D_3)\) |
| \(acd\) | \((5+4\sqrt2-7\sqrt6)/(28\mathcal D_3)\) |
| \(bcd\) | \((4\sqrt2+7\sqrt6-7\sqrt3-9)/(28\mathcal D_3)\) |

Each equals \(\langle\alpha,T(X_U)\rangle_0/
(\mathfrak F_Q\det C_{UU})\); all four determinants are \(\mathcal D_3\).
Their signs are respectively \(+,-,-,+\).

Write \(A_1=[x,K]\), \(B_1=[y,K]\). The inner returns from CB are
\[
\mathbb E_{B,h}J_{cd}
=-\lambda[y,z]+2h\gamma_{bcd}\tau[z,[y,z]]+O(h^2),
\]
\[
\mathbb E_{D,h}J_{cd}
=\lambda[x,w]+2h\gamma_{acd}\tau[w,[x,w]]+O(h^2).
\]
Applying the actual outer conditional law as well gives
\[
\boxed{\begin{aligned}
\mathbb E_{A,h}\mathbb E_{B,h}J_{cd}
={}&\lambda rK\\
+h\{&
-2\gamma_{bcd}\tau r^2A_1
-2(\lambda\gamma_{abc}\sigma+\gamma_{bcd}\tau rs)B_1
+2\chi_Q\gamma_{bcd}\tau\sigma\,y\}
+O(h^2),
\end{aligned}}
\tag{DR9}
\]
\[
\boxed{\begin{aligned}
\mathbb E_{A,h}\mathbb E_{D,h}J_{cd}
={}&\lambda rK\\
+h\{&
2(\lambda\gamma_{abd}\sigma+\gamma_{acd}\tau rs)A_1
+2\gamma_{acd}\tau r^2B_1
+2\chi_Q\gamma_{acd}\tau\sigma\,x\}
+O(h^2).
\end{aligned}}
\tag{DR10}
\]
For example, the outer first score acting on \(-\lambda[y,z]\) contributes
\(-2\lambda\gamma_{abc}\sigma B_1\). It cannot be omitted merely because the pair marginal score is zero.

The remaining contractions are ordinary conditional Gaussian identities:
\[
\begin{aligned}
\mathbb E_0\!\left([z,[y,z]]\mid x,y\right)
&=-r^2A_1-rsB_1+\chi_Q\sigma y,\\
\mathbb E_0\!\left([w,[x,w]]\mid x,y\right)
&=rsA_1+r^2B_1+\chi_Q\sigma x.
\end{aligned}
\]
The Casimir terms are the residual contractions
\(\sum_\alpha[e_\alpha,[y,e_\alpha]]=\chi_Q y\) and its \(x\) counterpart. In these displays the left side denotes the expectation of the complete indicated double bracket.

## The discrepancies are fixed exterior-information responses

The direct Gaussian coefficient is \(r^2-s^2\); both composed coefficients are \(\lambda r\). Their difference has the useful exact form
\[
\boxed{
r^2-s^2-\lambda r
=\frac{o_0(2-\tau)}{d_0^2-n_0^2}<0.}
\tag{DR11}
\]
Indeed \(d_0-o_0=2\), \(o_0<0\), and \(\tau<2\). Equivalently the difference is
\(11+10\sqrt3-(21\sqrt2+11\sqrt6)/2\).
The directions lost by the two nonnested projections already matter in the Gaussian law.

The composed routes agree at that order, but their first coefficients in (DR9)–(DR10) differ. Their linear parts are respectively
\(2\chi_Q\gamma_{bcd}\tau\sigma y\) and
\(2\chi_Q\gamma_{acd}\tau\sigma x\). They are nonzero with opposite coefficient signs; terms of cubic polynomial degree cannot cancel that linear polynomial difference. Hence the complete first-order route discrepancy is a nonzero covariant polynomial. This does not assume that every individual invariant contraction detects it.

The closing source must be specified. For example \(Q(x,K)=0\), so closing the adjoint index with \(x\) hides the Gaussian difference. Closing with the retained \(A\)-source \(K\) instead gives
\[
\langle K,(\mathbb E_{A,0}
-\mathbb E_{A,0}\mathbb E_{B,0})J_{cd}\rangle_0
=\mathfrak F_Q\,o_0(2-\tau)\ne0,
\tag{DR12}
\]
and the same value through \(D\). This uses
\(\mathbb E_0|K|_Q^2=\mathfrak F_Q(d_0^2-n_0^2)\).
The result compares two specified conditional experiments with the closing source retained at \(A\). It does not license commuting that source through an intermediate forgetting operation.

## These are actual compact finite-source comparisons

Set
\[
\widehat X_{p,h}=\frac2h q_\rho(P_p),\qquad
\widehat J_{cd,h}=[\widehat X_{c,h},\widehat X_{d,h}],
\]
using GM's bounded equivariant mark. Its local jet is \(X_p+O(h^2)\). In each displayed route polynomial replace \(x,y\) by the corresponding compact marks. If
\(\mathcal R_h=\mathcal R_0+h\mathcal R_1\) denotes one of (DR4), (DR9), (DR10), VP proves
\[
\boxed{
\mathsf P_{A,h}\mathsf P_{B,h}
(\Phi_h\widehat J_{cd,h})
=\Phi_h\,\mathcal R_h(\widehat X_{a,h},\widehat X_{b,h})
+O_{L^2\otimes\mathfrak g}(h^2)}
\tag{DR13}
\]
for the \(B\)-route, with the analogous statements for the direct and \(D\)-routes. The projections belong to the actual common vacuum and complete prepared face algebras. The adjoint index is treated componentwise on the framed cover; no extra scalar physical state is introduced.

The proof applies the weighted source return and finite ordered projection-word expansion before truncating. It does not multiply an uncontrolled \(O(h^2)\) remainder by an unbounded rescaled mark. The compact bracket has norm \(O(h^{-2})\), while each output polynomial has fixed degree; arbitrary vacuum accuracy pays these fixed losses as in VP and CB.

The scalar witness (DR12) also returns without that multiplication problem: take the Hilbert-space pairing of the separately returned vector
\(\Phi_h[\widehat X_{a,h},\widehat X_{b,h}]\) with the difference of the conditional output vectors. Its actual value is
\(\mathfrak F_Qo_0(2-\tau)+O(h^2)\). The first coefficient vanishes by Gaussian parity: the bracket sources are even and the first score and first response polynomials are odd. This is a closed invariant comparison, with the closing source explicitly fixed.

The differences are expected for nonnested conditional projections. Recovering the original joint readout along another route requires retaining its exterior message and any source used to close the boundary index. [[conditional-boundary-translation-and-source-products|The conditional boundary translation]] constructs that three-face message, retaining the inherited covariance and the complete polynomial product. These formulas determine what it must restore; they do not supply a new vacuum, a tunable Casimir coefficient or a mass term. All estimates concern the fixed four-face geometry, fixed group and finite source family. Chronological exterior response and the vacuum-cap and lag terms of [[two-slice-innovation-geometry/regional-innovation-and-exterior-information-balance|RI]] and [[spatial-block-sewing-and-the-vacuum-cap-response|SB]] remain separate from this static first-order test.
