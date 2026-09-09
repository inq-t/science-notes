# Regional Vacuum Scores and Three-Face Orientation

The first oriented vacuum correction is invisible in every one- and two-face marginal of the inherited Gaussian law. A three-face marginal can retain it. There is a further cancellation: two overlapping invariant two-face readouts have no first-order conditional exchange from this score, even when their union carries a nonzero orientation. The amplitude projections still move outside their old ranges. Marginal invisibility therefore does not identify a fixed regional embedding with a transported one.

**Status: exact Gaussian conditional identities and proved fixed-patch polynomial-source jets.** [[vacuum-hellinger-return-and-regional-conditional-projections|VH]] fixes the amplitude projection and inherited regional law. [[four-face-cubic-response-and-source-leakage|FC]] and [[all-group-oriented-kinetic-jet-and-source-lift|AJ]] supply the actual first vacuum score at four faces; [[fixed-group-compact-vacuum-and-oriented-source-return|GV]] supplies its fixed-group compact realization. [[regional-conditional-projection-and-the-vacuum-score|VP]] proves the weighted actual amplitude and conditional-projection jets on fixed polynomial source families. No operator-norm differentiability is inferred from VH's Hellinger bound.

## Condition the score in the inherited covariance

Let \(\mathfrak g\) have dimension \(d\), positive invariant metric \(Q\), and Cartan tensor
\[
T(x,y,z)=Q(x,[y,z]),\qquad
\mathcal F_Q=\sum_{a,b,c}Q(e_a,[e_b,e_c])^2.
\tag{VS1}
\]
Use a \(Q\)-orthonormal basis. On a fixed face-labelled cover let
\[
\mu_0=\Omega^2dX,\qquad
\mathbb E_0[X_p^aX_q^b]=C_{pq}\delta_{ab},\qquad C>0,
\qquad
\alpha(X)=\sum_{i<j<k}\beta_{ijk}T(X_i,X_j,X_k).
\tag{VS2}
\]
For the planar harmonic vacuum \(C=\sqrt{4I-\mathrm{Adj}}\), with the full containing patch retained. The score is \(\alpha=u/\Omega\), where \(u\) is the actual first vacuum-vector correction. No regional covariance is reset.

For a retained face set \(B\), write \(P_B=\mathbb E_0[\,\cdot\,|X_B]\). The conditional law is
\[
X=M_BX_B+\eta,\qquad
M_B=C_{:B}C_{BB}^{-1},\qquad
\mathbb E[\eta_i^a\eta_j^b|X_B]=(\Sigma_B)_{ij}\delta_{ab},
\quad
\Sigma_B=C-C_{:B}C_{BB}^{-1}C_{B:}.
\tag{VS3}
\]
Every contraction of two color slots of \(T\) vanishes. Consequently,
\[
\boxed{\alpha_B:=P_B\alpha=\alpha(M_BX_B).}
\tag{VS4}
\]
In particular, if \(J\) runs over increasing triples in \(B\), its coefficient is
\[
\alpha_B=\sum_{J\subset B,\ |J|=3}
\left[\sum_{I,\ |I|=3}\beta_I\det M_B[I,J]\right]T(X_J).
\tag{VS5}
\]
This follows by alternating multilinearity, after the residual Gaussian pair contractions have vanished. Thus \(\alpha_B=0\) for every \(|B|\le2\). For nested sets the same formula obeys \(P_A\alpha_B=\alpha_A\); forgetting data does not introduce an independently chosen preparation.

The complete conditional variance also has a finite formula. At \(m=M_BX_B\), put \(L_{ia}=\partial_{ia}\alpha(m)\) and \(H_{ia,jb}=\partial_{ia}\partial_{jb}\alpha(m)\), and abbreviate \(\Sigma=\Sigma_B\). Then
\[
\begin{aligned}
\operatorname{Var}_0(\alpha|X_B)
={}&\sum_{i,j,a}\Sigma_{ij}L_{ia}L_{ja}\\
&+\frac12\sum_{i,j,k,l,a,b}
\Sigma_{ik}\Sigma_{jl}H_{ia,jb}H_{ka,lb}\\
&+\mathcal F_Q\sum_{I,J}\beta_I\beta_J\det\Sigma[I,J].
\end{aligned}
\tag{VS6}
\]
Indeed, \(\alpha(m+\eta)-\alpha(m)\) splits into its degree-one, degree-two and degree-three residual Hermite parts. All internal contractions vanish, so these three parts are orthogonal. Wick's formula gives (VS6). Each displayed contribution is nonnegative as a whole, including when \(\Sigma\) is singular. Polarization gives the corresponding conditional covariance of two Cartan-cubic scores.

## Two representations of a changing conditional law

Use VP's complete facewise measurable chart and its weighted first expansion
\[
\Phi_h=\Omega(1+h\alpha)+O(h^2).
\tag{VS7}
\]
The remainder is \(O(h^2)\) after multiplication by any specified fixed polynomial weight. VP8 justifies the differentiated fiber projection without an inverse marginal-density bound. Merely using an unweighted \(O(h^2)\) error in VH3 would not establish this derivative.

The probability density has first score \(2\alpha\). Differentiating the conditional-function ratio gives
\[
\left.\partial_h P_{B,h}f\right|_0
=2\{P_B(\alpha f)-\alpha_BP_Bf\}.
\tag{VS8}
\]
For the actual compact law, interpret this as a fixed-polynomial source jet in the moving vacuum norm: multiply the difference between \(P_{B,h}f\) and the displayed first-order expansion by \(\Phi_h\). Its norm is \(O(h^2)\). Indeed apply VP9 to \(\Phi_h f=\Omega f+h\Omega\alpha f+O(h^2)\), then subtract the moving amplitude multiplying \(P_Bf\). This avoids taking an uncontrolled quotient in a fixed unweighted norm.
The common amplitude projection is different. Conjugate VH1 by multiplication by \(\Omega\), so its unperturbed action is \(P_B\) on \(L^2(\mu_0)\). Its first jet is
\[
\mathsf E_{B,h}=P_B+hJ_B+O(h^2),\qquad
\boxed{J_B=M_{\alpha-\alpha_B}P_B+P_BM_{\alpha-\alpha_B}.}
\tag{VS9}
\]
Here \(M_f\) denotes multiplication. The factor two in (VS8) and the two distinct terms in (VS9) express the same density change in different carriers. In particular,
\[
J_Bf_B=(\alpha-\alpha_B)f_B,\qquad
P_BJ_BP_B=0
\tag{VS10}
\]
for regional polynomial \(f_B\). A zero marginal score does not make the projection stationary. For the explicit polynomial amplitude model \((1+h\alpha)\Omega\) and \(|B|\le2\), its conditional denominator is exactly \(1+h^2P_B\alpha^2\ge1\); (VS9) then holds on fixed polynomial probes directly, without an inverse marginal-density bound.

## An overlapping-pair Ward cancellation

Take \(B=\{p,q\}\), \(D=\{q,r\}\), and \(U=B\cup D\), with three distinct faces. Formula (VS5) gives
\[
\alpha_U=\gamma_U T(X_p,X_q,X_r).
\tag{VS11}
\]
For every simultaneously Ad-invariant polynomial \(f(X_q,X_r)\),
\[
\boxed{P_B(\alpha f)=P_B(\alpha_Uf)=0.}
\tag{VS12}
\]
To prove it, condition on \(X_p=x,X_q=y\). Then \(X_r=m+\zeta\), with \(m=ax+by\) and isotropic residual covariance \(\sigma I\). Gaussian integration by parts gives
\[
\mathbb E[T(x,y,X_r)f(y,X_r)|x,y]
=\sigma Q\!\left([x,y],\nabla_m
 \mathbb E[f(y,m+\zeta)]\right).
\tag{VS13}
\]
The conditional mean term vanishes because \(m\in\operatorname{span}(x,y)\). The averaged polynomial on the right is invariant under \(m\mapsto\operatorname{Ad}_{\exp(sy)}m\), since this conjugation fixes \(y\) and preserves the isotropic Gaussian. For \(a\ne0\), \([y,m]=-a[x,y]\), so its derivative is zero. For \(a=0\) the same conclusion follows by polynomial continuity in \(a\). This proves (VS12) for every compact group with invariant \(Q\), without classifying its two-vector invariant polynomials.

Thus (VS8) vanishes for the conditional exchange from the invariant \(D\)-source core to \(B\). In the common amplitude carrier,
\[
P_BM_\alpha P_D=0,\qquad
\left.\partial_h(\mathsf E_{B,h}\mathsf E_{D,h})\right|_0
=M_\alpha P_BP_D+P_BP_DM_\alpha .
\tag{VS14}
\]
The general product derivative contains the additional middle term \(2P_BM_\alpha P_D\); (VS12) removes it here. The exterior vacuum-amplitude terms remain. Neither \(P_BP_D=P_B\) nor a physical factorization across these overlapping sets has been assumed.

The orientation can still be present in their union. From the same conditional law,
\[
\mathbb E_0[\alpha_U|X_p,X_q]=0,\qquad
\operatorname{Var}_0(\alpha_U|X_p,X_q)
=\gamma_U^2\sigma\,\|[X_p,X_q]\|_Q^2,
\qquad
\|\alpha_U\|_2^2=\gamma_U^2\mathcal F_Q\det C_{UU}.
\tag{VS15}
\]
This positive commutator-square is a conditional score-variance budget. It is not an additional Hamiltonian potential or an innovation lower bound.

## A nonzero three-face score in the actual four-face comb

Use the mode and face orientation of FC1, with faces \(a,b,c,d\) and frequencies \((\sqrt2,2,2,\sqrt6)\). FC9, equivalently AJ's \(S_G\Omega\), gives
\[
\alpha=
\frac{2\sqrt2-1}{112}T_{012}
+\frac{\sqrt2-1}{16}T_{013}
+\frac{3-\sqrt6}{48}(T_{023}+T_{123}).
\tag{VS16}
\]
These coefficients use the inherited vacuum in the specified comb chart. They apply to the Cartan tensor with the metric normalization of [[weighted-character-scale-and-bounded-lie-sources|GM]]; no nonlinear \(SU(2)\) energy coefficient is being imported.

For \(U=\{a,b,c\}\),
\[
T(X_a,X_b,X_c)=\frac12(T_{012}+T_{013}-T_{023}-T_{123}),
\qquad
\det C_{UU}=\sqrt2+2\sqrt3+\sqrt6.
\]
The mode triples are orthogonal and have norm squared
\(\mathcal F_Q\omega_i\omega_j\omega_k\). Applying (VS4), or taking their exact pairing with the retained triple, yields
\[
\boxed{
\alpha_U=\gamma_{abc}T(X_a,X_b,X_c),\qquad
\gamma_{abc}=
\frac{9+3\sqrt2-7\sqrt3}
{28(\sqrt2+2\sqrt3+\sqrt6)}>0.}
\tag{VS17}
\]
Positivity follows from \(9+3\sqrt2>7\sqrt3\). A retained scaled orientation mark therefore has the first density response
\[
\mathbb E_h[T(X_a,X_b,X_c)]
=2h\,\gamma_{abc}\mathcal F_Q\det C_{UU}+O(h^2)
\tag{VS18}
\]
whenever the fixed-patch compact source return realizes this polynomial mark, as in GV. Its one- and two-face marginal score tests all vanish at this order, and so does the invariant overlapping-pair conditional exchange (VS12).

Source composition must therefore distinguish fixed face access, the moving amplitude projection, and the oriented three-face union. [[covariant-boundary-source-and-the-oriented-return|The covariant boundary return]] retains an adjoint pair index and derives a nonzero nested response from this same \(\gamma_{abc}\). [[four-face-covariant-route-response|The full four-face calculation]] transforms VS16 to the complete face score and compares the nonnested conditional routes. [[conditional-boundary-translation-and-source-products|Its boundary message]] uses the residual score \(\alpha-\alpha_S\) to recover the original products and elimination orders. [[resonant-source-transport-and-fixed-regional-access|RG]] concerns a different freedom: changing a normal-form source lift while retaining its clock. The cancellations here do not identify fixed regional access with that transported embedding.
