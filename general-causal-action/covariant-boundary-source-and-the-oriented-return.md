# Covariant Boundary Sources Retain the Oriented Return

The first oriented vacuum score has a nonzero conditional response when its boundary index is retained until the regions are sewn. An adjoint-valued pair mark returns a double Lie bracket; eliminating the shared face then gives a linear Casimir response. Direct and nested conditioning fix the same coefficient from the actual vacuum and inherited covariance. This channel is absent from the exchange of already neutral scalar pair marks. Its compact realization uses the original prepared face words and is independent of resonant normal-form choices.

**Status: exact Gaussian conditional response and actual fixed-patch strong-source first jet.** [[regional-vacuum-score-and-the-three-face-orientation|VS]] supplies the three-face marginal score and the neutral-pair cancellation. [[regional-conditional-projection-and-the-vacuum-score|VP]] proves the actual weighted source and conditional-projection return. [[weighted-character-scale-and-bounded-lie-sources|GM]] supplies globally bounded equivariant compact marks. This is a response of the specified law, not a new Hamiltonian term or a physical gap bound.

## Keep the shared adjoint index until contraction

Let \(p,q,r\) be three distinct based faces, with the common-root transports kept fixed. Write
\[
x=X_p,\qquad y=X_q,\qquad z=X_r,\qquad
T(x,y,z)=Q(x,[y,z]).
\]
The inherited harmonic covariance is \(C\otimes I_{\mathfrak g}\). Suppose its actual marginal amplitude score on this union is
\[
\alpha_{\{p,q,r\}}=\gamma\,T(x,y,z).
\tag{CB1}
\]
The coefficient \(\gamma\) is fixed by conditional projection of the actual vacuum correction. It can vanish and its sign depends on the declared ordering. VS gives both the general regression formula and an explicit nonzero four-face example.

Given \(x,y\), write
\[
z=\lambda_p x+\lambda_q y+\eta,\qquad
\mathbb E_0[\eta^a\eta^b\mid x,y]=\sigma\delta_{ab},
\]
\[
(\lambda_p,\lambda_q)=C_{rB}C_{BB}^{-1},\qquad
\sigma=C_{rr}-C_{rB}C_{BB}^{-1}C_{Br}>0,\qquad B=\{p,q\}.
\tag{CB2}
\]
Since \(T(x,y,\lambda_p x+\lambda_q y)=0\), the conditional density's first score is \(2\gamma Q([x,y],\eta)\).

Retain the covariant pair mark
\[
J_{qr}=[y,z]\in\mathfrak g .
\]
It transforms by the adjoint action, rather than being a scalar physical source by itself. The joint contraction \(Q(x,J_{qr})=T(x,y,z)\) is a physical invariant. On the framed cover, conditional expectation acts componentwise on this finite-dimensional boundary index. [[gauge-boundary-frame-gluing/inq|Boundary gluing]] uses the same distinction between a covariant regional presentation and its closed invariant contraction.

The Gaussian conditional mean is
\[
\mathbb E_0[J_{qr}\mid x,y]=\lambda_p[y,x].
\]
The first conditional response is forced:
\[
\boxed{\left.\partial_h\mathbb E_h[J_{qr}\mid x,y]\right|_0
=2\gamma\sigma\,[y,[x,y]].}
\tag{CB3}
\]
Indeed the marginal score on \(B\) is zero. In the product of the joint score with \(J_{qr}\), only the two residual factors contribute, and
\[
\mathbb E_0\!\left[
Q([x,y],\eta)[y,\eta]\mid x,y\right]
=\sigma[y,[x,y]].
\]
This proves the sign and normalization in (CB3), without a color-dimension approximation.

## Closing the boundary channel gives an invariant response

Contracting (CB3) with \(x\) uses invariance of \(Q\):
\[
Q(x,[y,[x,y]])=Q([x,y],[x,y]).
\]
Thus
\[
\boxed{\left.\partial_h\mathbb E_h[T(x,y,z)\mid x,y]\right|_0
=2\gamma\sigma\,\|[x,y]\|_Q^2.}
\tag{CB4}
\]
The conditional Gaussian mean of \(T\) is zero. The sign of the response is the sign of \(\gamma\); the nonnegative squared bracket is not by itself a positive energy.

Let \(\mathfrak F_Q=\sum_{abc}f_{abc}^2\). Two-vector Gaussian contraction gives
\[
\mathbb E_0\|[x,y]\|_Q^2
=\mathfrak F_Q\det C_{BB},\qquad
\sigma\det C_{BB}=\det C_{\{p,q,r\},\{p,q,r\}}.
\]
Integrating (CB4) therefore gives
\[
\boxed{\left.\partial_h\mathbb E_hT\right|_0
=2\gamma\mathfrak F_Q\det C_{\{p,q,r\},\{p,q,r\}}.}
\tag{CB5}
\]
This agrees with direct pairing against the actual three-face score.

The squared norm of its conditional density tangent is also fixed:
\[
\mathbb E_0[(2\gamma T)^2\mid x,y]
=4\gamma^2\sigma\,\|[x,y]\|_Q^2.
\tag{CB6}
\]
This is the conditional score's information coefficient. No equality with a transfer energy, the normal-form multiplier contact, or the full OI surplus is inferred from it.

VS's Ward cancellation applies to an invariant scalar \(f(y,z)\). The map \(J_{qr}\) retains an adjoint index, so that cancellation does not apply. Closing the index only after coupling to \(x\) supplies the missing invariant three-face source. This identifies the source information lost by neutralizing each pair before sewing.

## The original compact marks realize the response

For the faithful representation and actual weighted scale of GM, set
\[
\widehat X_{s,h}=\frac2h\,q_\rho(P_s),\qquad
\widehat J_{qr,h}=[\widehat X_{q,h},\widehat X_{r,h}],
\]
\[
\widehat T_h
=Q(\widehat X_{p,h},
[\widehat X_{q,h},\widehat X_{r,h}]).
\tag{CB7}
\]
Each underlying unscaled mark is globally bounded and equivariant. In the common logarithm neighborhood,
\(\widehat X_{s,h}=X_s+O(h^2)\), so the marks have no independent first-order coordinate correction. Their scaled norms grow as \(h^{-1},h^{-2},h^{-3}\), respectively; VP's weighted vacuum accuracy is taken before source multiplication.

Let \(\Phi_h\) be the actual vacuum in VP's complete common chart and let \(\mathsf P_{B,h}\) be its actual conditional amplitude projection. The following statements are \(L^2\) vector expansions, with the finite adjoint index retained in the first:
\[
\begin{aligned}
\mathsf P_{B,h}(\Phi_h\widehat J_{qr,h})
=\Phi_h\bigl(&\lambda_p[\widehat X_{q,h},\widehat X_{p,h}]\\
&+2h\gamma\sigma
[\widehat X_{q,h},[\widehat X_{p,h},\widehat X_{q,h}]]
\bigr)+O(h^2),
\end{aligned}
\]
\[
\boxed{
\mathsf P_{B,h}(\Phi_h\widehat T_h)
=2h\gamma\sigma\,\Phi_h
\|[\widehat X_{p,h},\widehat X_{q,h}]\|_Q^2
+O(h^2).}
\tag{CB8}
\]
Apply VP's moving-source formula separately to the quadratic covariant and cubic invariant marks. This avoids multiplying an uncontrolled projection remainder by an unbounded rescaled source. Polynomial-weight estimates and cutoff tails transfer the local formulas to the displayed global compact marks. Outside the local chart, use the exactly transported Gauss action.

Actual centering is explicit as well. If \(m_h=\langle\widehat T_h\rangle_{\psi_h}\), then
\[
\begin{aligned}
\mathsf P_{B,h}\bigl(\Phi_h(\widehat T_h-m_h)\bigr)
=2h\gamma\sigma\,\Phi_h\bigl(
\|[\widehat X_{p,h},\widehat X_{q,h}]\|_Q^2
-\mathfrak F_Q\det C_{BB}\bigr)+O(h^2).
\end{aligned}
\tag{CB9}
\]
The Gaussian constant suffices to this order because the two-face marginal has zero first score. Dividing by the positive leading standard deviation gives the corresponding normalized source return.

## Eliminating the shared face fixes a linear Casimir response

In the fixed simple-algebra setting, retain only \(x=X_p\), and put
\[
\Sigma_{qr\mid p}
=C_{\{q,r\},\{q,r\}}
-C_{\{q,r\},p}C_{pp}^{-1}C_{p,\{q,r\}},
\qquad \chi_Q=\frac{\mathfrak F_Q}{d}.
\]
The conditional means of \(y,z\) are multiples of \(x\). Write their residuals as \(\eta_y,\eta_z\). Then
\[
T(x,y,z)=Q(x,[\eta_y,\eta_z]),\qquad
\mathbb E_0[J_{qr}\mid x]=0.
\]
The linear-residual terms in \(J_{qr}\), multiplied by this quadratic score, have zero Gaussian mean. The remaining contraction is
\[
\mathbb E_0\!\left[
[\eta_y,\eta_z]\otimes[\eta_y,\eta_z]\mid x\right]
=\chi_Q\det\Sigma_{qr\mid p}\,I_{\mathfrak g}.
\]
It follows that
\[
\boxed{\left.\partial_h\mathbb E_h[J_{qr}\mid x]\right|_0
=\rho_{p;qr}\,x,\qquad
\rho_{p;qr}=2\gamma\chi_Q\det\Sigma_{qr\mid p}.}
\tag{CB10}
\]
The linear response is forced by contracting the same two structure tensors that supplied the squared-bracket response.

The nested route through \(\{p,q\}\) gives exactly the same answer. Its outer conditional law has zero first score because the entire pair marginal has zero first score. Also
\[
\mathbb E_0\!\left([y,[x,y]]\mid x\right)
=\chi_Q\,\operatorname{Var}_0(y^\alpha\mid x)\,x,
\]
\[
\operatorname{Var}_0(y^\alpha\mid x)\,
\operatorname{Var}_0(z^\alpha\mid x,y)
=\det\Sigma_{qr\mid p}.
\tag{CB11}
\]
Here the first expectation denotes
\(\mathbb E_0([y,[x,y]]\mid x)\); each scalar variance is the same for every orthonormal component \(\alpha\). The bracket identity follows from
\(\sum_a[e_a,[x,e_a]]=\chi_Qx\). The variance identity is the two-by-two Schur determinant formula. Applying (CB3) and then conditioning on \(x\) therefore recovers (CB10), with no new normalization or independent comparison parameter.

VP's finite-word return makes this a comparison of actual compact conditional projections. In the common amplitude carrier,
\[
\mathsf P_{p,h}(\Phi_h\widehat J_{qr,h})
=h\rho_{p;qr}\Phi_h\widehat X_{p,h}+O(h^2),
\]
\[
\boxed{
\mathsf P_{p,h}\bigl(\Phi_h(\widehat T_h-m_h)\bigr)
=h\rho_{p;qr}\Phi_h
\bigl(Q(\widehat X_{p,h},\widehat X_{p,h})-dC_{pp}\bigr)
+O(h^2).}
\tag{CB12}
\]
The actual nested identity
\(\mathsf P_{p,h}\mathsf P_{\{p,q\},h}=\mathsf P_{p,h}\)
retains the common vacuum. Both expressions also follow directly by applying VP to the corresponding covariant or scalar source; no rescaled multiplier is applied to a previously uncontrolled remainder.

For VS's explicit four-face union \(p=a,q=b,r=c\),
\(C_{aa}=(4+\sqrt2+\sqrt6)/4\). Substituting its actual \(\gamma_{abc}\) gives the nonzero coefficient
\[
\boxed{\rho_{a;bc}
=\frac{2\mathfrak F_Q}{7d}
\frac{9+3\sqrt2-7\sqrt3}{4+\sqrt2+\sqrt6}>0.}
\tag{CB13}
\]
This is a dimensionless coefficient of conditional source return in the declared normalization. A linear adjoint response is not thereby a mass term. Its significance here is that the actual three-face orientation determines both a nonlinear intermediate channel and its linear contraction, while the neutral scalar pair exchanges miss that first-order information.

All these estimates concern a fixed patch, group and finite source family in the declared units. The value of \(\gamma\) comes from \(u/\Omega\), so adding a resonant source generator with \(N\Omega=0\) cannot retune it. [[two-face-source-access-and-the-normal-form-obstruction|The normal-form access obstruction]] accordingly directs source sewing toward the actual covariant conditional channel, with its embedding and products retained. A further spatial composition must preserve that channel and the [[spatial-block-sewing-and-the-vacuum-cap-response|vacuum-cap, source-exchange and changed-history terms]]; their control through the required physical limits remains open.
