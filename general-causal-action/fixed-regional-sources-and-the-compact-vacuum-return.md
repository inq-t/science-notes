# Fixed Regional Sources Return with the Actual Compact Vacuum

A finite family of fixed face profiles has a uniform, nonzero harmonic source variance as the planar patch grows. This removes the extra normalization loss of the lowest spatial mode. The actual compact vacuum and its centered, variance-normalized source vectors return to their harmonic counterparts with error \(O(h(L+1)^{11/2})\) on the proved confinement window. The source profiles and comb connectors remain fixed; the result does not replace the inherited regional vacuum by an independently prepared block.

**Status: proved uniform source-vector and equal-time normalization return for finitely many prescribed profiles.** [[planar-patch-confinement-and-the-spatial-soft-mode|PP]] fixes the physical planar carrier and [[comb-face-transport-and-the-first-nonlinear-jet|FJ]] fixes the common-root comb faces. [[compact-cutoffs-and-uniform-polynomial-quasimodes|CQ]] and [[compact-operator-taylor-remainder-on-planar-wells|OT]] construct the actual quasimode; [[uniform-planar-localization-and-the-first-physical-levels|UP]] selects its ground branch. The weighted transfer uses [[weighted-compact-source-return-on-growing-patches|WS]]. [[inherited-planar-vacuum-and-the-regional-time-law|The inherited harmonic law]] supplies the regional interpretation.

## A fixed profile retains a positive source scale

Let \(\Lambda_L=\{1,\ldots,L\}^2\), \(n=L+1\), \(A_L=4I-\operatorname{Adj}_{\Lambda_L}\), and \(C_L=A_L^{1/2}\). Put
\[
h=(\kappa/g)^{1/4},\qquad
\epsilon=hn^{10},\qquad \theta=hn^{11/2}.
\tag{FR1}
\]
The actual scaled Hamiltonian is \(\widehat H=H_{L,g}/\sqrt{\kappa g}\). Every vertex, including the boundary vertices, carries Gauss law.

Choose a nonzero, real, finitely supported profile \(b\) on \(\mathbb Z^2\). Translate its complete support into \(\Lambda_L\), retaining its coefficients, and write \(\beta_b=\|b\|_2\). Constants may depend on a fixed finite collection of these profiles, but not on \(L,h\), or the allowed translations. No distance from the exterior boundary is required for the estimates below.

Extend the translated vector by zero to \(\mathbb Z^2\). Its discrete energy is
\[
\mathcal E(b)=
\sum_{\{p,q\}:\,|p-q|_1=1}(b_p-b_q)^2
=b^{\mathsf T}A_Lb>0 .
\tag{FR2}
\]
Each unordered lattice edge is counted once. The expression is translation invariant and independent of the containing patch: the boundary diagonal remains four. If this energy vanished, the zero extension would be constant on the connected infinite lattice, and finite support would force \(b=0\).

The spectrum of \(A_L\) is contained in \((0,8)\), so \(\sqrt{A_L}\ge A_L/\sqrt8\). Consequently
\[
\boxed{
0<\frac{\mathcal E(b)}{\sqrt8}
\le c_{b,L}:=b^{\mathsf T}C_Lb
\le \sqrt8\,\beta_b^2 .}
\tag{FR3}
\]
In particular, \(a_b=\mathcal E(b)/(\sqrt8\,\beta_b^2)>0\) is a size-independent lower bound for \(c_{b,L}/\beta_b^2\).

Let \(\Omega_L\) be the normalized harmonic vacuum. Its three color components are independent Gaussians with face covariance \(C_L\). For \(Y_b=\sum_p b_pX_p\), define
\[
B_{b,0}=|Y_b|^2,\quad
F_{b,0}=(|Y_b|^2-3c_{b,L})\Omega_L,\quad
\sigma_{b,0}=\sqrt6\,c_{b,L},\quad
\zeta_{b,0}=F_{b,0}/\sigma_{b,0}.
\tag{FR4}
\]
This is a normalized, physical Hermite-degree-two vector. In general it contains many oscillator energies; it is not a single-mode replacement for the regional source.

## The compact probe has uniform Gaussian and graph bounds

Write the common-root face quaternion as \(P_p=q_{0,p}I-i\mathbf q_p\cdot\sigma\). The fixed compact observable and its scaled form are
\[
\mathcal B_b=\left|\sum_p b_p\mathbf q_p\right|^2,\qquad
B_{b,h}=\frac4{h^2}\mathcal B_b.
\tag{FR5}
\]
All quaternion vectors rotate together under the residual root action, so the observable is physical. “Regional” here refers to the selected comb-face profiles. Their specified transport paths remain part of the observable; they are not removed by imposing separate facewise gauge quotients.

In the exact scaled logarithmic chart,
\[
B_{b,h}=|Y_{b,h}|^2,\qquad
Y_{b,h}=\sum_p b_p\operatorname{sinc}(h|X_p|/2)X_p.
\]
WS's odd-sum estimate is homogeneous in the coefficient vector. For every fixed Gaussian moment order \(q\) and finite Hermite degree \(m\),
\[
\|Y_{b,h}-Y_b\|_q\le C_q\beta_bh^2,\qquad
\|Y_b\|_q+\|Y_{b,h}\|_q\le C_q\beta_b,
\]
\[
\boxed{
\|B_{b,h}P_{\le m}\|\le C_m\beta_b^2,\qquad
\|(B_{b,h}-B_{b,0})P_{\le m}\|
\le C_m\beta_b^2h^2,\quad 0<h\le1 .}
\tag{FR6}
\]
The proof is WS3 followed by Hölder and the dimension-independent fixed-chaos moment bound. Correlation between faces is retained; independence of those faces is unnecessary.

On the actual compact carrier, let \(V=h^{-2}W\), where \(W\) is the sum of plaquette magnetic costs. Cauchy–Schwarz gives
\[
0\le B_{b,h}\le4\beta_b^2V.
\]
Using WS's exact identity \(\mathsf C_{\rm raw}W=3W-6L^2\) therefore gives
\[
\boxed{
\|B_{b,h}u\|
\le4\beta_b^2\bigl(\|\widehat Hu\|
+\sqrt6\,L\|u\|\bigr),\qquad
u\in D(\widehat H).}
\tag{FR7}
\]
This bound holds before localization. It avoids using the growing global multiplication norm of \(B_{b,h}\).

## The constructed vacuum carries the source and its normalization

Use CQ's single magnetic cutoff and Haar half-density map \(\mathcal J_h\), without renormalizing the map on each input. On any fixed Hermite-degree space, set
\[
t_h=(hn^{3/2})^8.
\]
The cutoff radius is comparable to \((h\sqrt n)^{-1}\). Eighth moments and (FR6), with Hölder before truncating the tail, give
\[
\|(1-\chi_h)u\|
\le C_mt_h\|u\|,\qquad
\|(1-\chi_h)B_{b,h}u\|
\le C_m\beta_b^2t_h\|u\|.
\tag{FR8}
\]
For example,
\(\||X|^8B_{b,h}u\|\le C_m n^8\beta_b^2\|u\|\).
The same bounds hold with \(B_{b,0}\). All are Gaussian trial-vector estimates; none assumes localization of the unknown actual vacuum.

The sixth-order construction in [[uniform-nonlinear-planar-gap-and-marked-response|UN4–5]] gives a normalized physical vector \(v_h\), approximate energy \(\lambda_h\), and actual normalized vacuum \(\psi_h\), with
\[
\rho_h=\|(\widehat H-\lambda_h)v_h\|
\le Ch^7n^{75/2},\qquad
\|\psi_h-v_h\|\le Cn\rho_h.
\tag{FR9}
\]
The phase is aligned with the actual positive vacuum. UP supplies its energy bound \(E_0\le Cn^2\) and gap at least \(c/n\); it also selects the ground eigenline. Thus (FR9) does not use a generic unselected quasimode.

The uncut polynomial part of \(v_h\) lies in degree at most eighteen and differs from \(\Omega_L\) by \(O(\theta)\). This follows from the fixed-order coefficients \(\|\psi_r\|\le C_rn^{11r/2}\). Equations (FR6) and (FR8), including the normalization of the cutoff vector, imply
\[
\|v_h-\mathcal J_h\Omega_L\|\le C(\theta+t_h),
\]
\[
\|B_{b,h}v_h-\mathcal J_hB_{b,0}\Omega_L\|
\le C\beta_b^2(\theta+h^2+t_h).
\tag{FR10}
\]
In particular its source mean approaches \(3c_{b,L}\), its centered norm approaches \(\sqrt6c_{b,L}\), and its source norm is at most \(C\beta_b^2\). The nonzero lower bound in (FR3) verifies these normalization conditions uniformly.

The weighted error from \(v_h\) to the actual vacuum follows directly from (FR7):
\[
\|B_{b,h}(\psi_h-v_h)\|
\le C\beta_b^2n^3\rho_h.
\tag{FR11}
\]
Indeed
\(\|\widehat H(\psi_h-v_h)\|\le E_0\|\psi_h-v_h\|+2\rho_h\).
Here the factor \(n^3\) retains the extensive vacuum energy and the \(1/n\) spectral separation. There is no additional factor from a vanishing regional variance.

## The actual centered source returns uniformly

Let \(m_{b,h}\) and \(\sigma_{b,h}^2\) be the mean and variance of \(B_{b,h}\) in \(\psi_h\), and put
\[
\zeta_{b,h}=(B_{b,h}-m_{b,h})\psi_h/\sigma_{b,h},\qquad
\delta_{L,h}=\theta+h^2+n^3\rho_h+t_h.
\]
After choosing the fixed \(\epsilon\)-window sufficiently small for the prescribed finite family,
\[
\boxed{
|m_{b,h}-3c_{b,L}|\le C_b\beta_b^2\delta_{L,h},\qquad
|\sigma_{b,h}^2-6c_{b,L}^2|
\le C_b\beta_b^4\delta_{L,h},}
\tag{FR12}
\]
\[
\boxed{
\|\zeta_{b,h}-\mathcal J_h\zeta_{b,0}\|
\le C_b\delta_{L,h}
\le C_bhn^{11/2}.}
\tag{FR13}
\]
The constants may depend on \(a_b^{-1}\); no arbitrary lower bound on the actual variance is posited.

For completeness, (FR10) first compares the approximating mean and centered vector with their harmonic values. Equations (FR9), (FR11) and the direct centering identity WS12 then compare the two normalized compact states. The resulting centered-vector error is \(O(\beta_b^2\delta_{L,h})\). Taking squared norms gives (FR12), while (FR3) bounds the harmonic denominator away from zero in units of \(\beta_b^2\). The cutoff norm defect in (FR8) is included before dividing by that denominator. This proves (FR13) even though \(\mathcal J_h\) itself is only a contraction.

To check the last bound in (FR13),
\[
\frac{n^3\rho_h}{\theta}
\le Ch^6n^{35}=C\epsilon^6n^{-25},\qquad
\frac{t_h}{\theta}=h^7n^{13/2}
=\epsilon^7n^{-127/2}.
\]
The term \(h^2/\theta\) is smaller as well. Thus one \(L\)-independent window suffices. Returning to the original bounded observable, its leading mean and variance are
\[
\mathbb E_{\psi_h}\mathcal B_b
=\frac{3h^2}{4}c_{b,L}+O_b(h^2\beta_b^2\theta),\qquad
\operatorname{Var}_{\psi_h}\mathcal B_b
=\frac{3h^4}{8}c_{b,L}^2
+O_b(h^4\beta_b^4\theta).
\tag{FR14}
\]
The small physical variance is paid for explicitly; multiplying the source by \(4/h^2\) does not change its normalized vector.

## A finite set of cross marks uses the same return

For two fixed nonzero profiles \(b,c\), the signed compact bilinear mark is
\[
B_{b,c,h}=\frac4{h^2}
\left(\sum_p b_p\mathbf q_p\right)\cdot
\left(\sum_p c_p\mathbf q_p\right)
=\frac{B_{b+c,h}-B_{b-c,h}}4.
\]
Its harmonic centered vector is
\((Y_b\cdot Y_c-3k_{bc})\Omega_L\), where
\(k_{bc}=b^{\mathsf T}C_Lc\), and its variance is
\[
\boxed{\operatorname{Var}(Y_b\cdot Y_c)
=3(c_{b,L}c_{c,L}+k_{bc}^2)>0.}
\tag{FR15}
\]
Wick contraction proves the formula. The graph bound has factor \(4\beta_b\beta_c\), and the Gaussian bounds have factor \(\beta_b\beta_c\). Hence the same centering and normalized-vector proof applies to any prescribed finite collection of these cross marks. Zero profiles appearing in the polarization identity contribute the zero observable and require no normalization.

## The global principal chart identifies both vacuum densities

FJ1 is an exact product-Haar coordinate map. Each face then has a unique principal logarithm in \(|y_p|<2\pi\), except at the Haar-null point \(-I\). Put \(N=L^2\),
\[
D_h=\{x\in\mathbb R^{3N}:|x_p|<2\pi/h\text{ for all }p\},
\]
and let \(\rho_L(y)\,dy\) be the complete normalized product Haar density in these logarithms. Define
\[
(\mathcal U_hf)(x)=
\mathbf1_{D_h}(x)\,h^{3N/2}\rho_L(hx)^{1/2}
f(P(hx)).
\]
This is unitary from the framed compact Haar space onto \(L^2(D_h,dx)\). After zero extension it is an isometry into \(L^2(\mathbb R^{3N})\), with
\(\mathcal U_h^*\mathcal U_h=I\) and
\(\mathcal U_h\mathcal U_h^*=\mathbf1_{D_h}\).
It intertwines simultaneous conjugation with common color rotation and therefore restricts to the physical invariant spaces. No onto identification with the entire oscillator Hilbert space is asserted.

The same cutoff map used above is exactly
\(\mathcal J_h=\mathcal U_h^*\chi_h\), so
\(\mathcal U_h\mathcal J_hu=\chi_hu\). Equations (FR8)–(FR13) give
\[
\boxed{
\|\mathcal U_h\psi_h-\Omega_L\|\le C\theta,\qquad
\|\mathcal U_h\zeta_{b,h}-\zeta_{b,0}\|
\le C_b\theta.}
\tag{FR16}
\]
The first bound uses \(Cn\rho_h+C(\theta+t_h)\); the second uses (FR13) and the degree-two cutoff tail. The flattened vacuum and \(\Omega_L\) are nonnegative normalized vectors on the same full Euclidean measure space. Thus the first inequality is also a bound on the \(L^2\) distance of the square roots of their probability densities. This comparison retains the complete global vacuum before any regional conditional expectation is taken.

This theorem returns source vectors and their actual equal-time normalizations. Propagating them requires a separate semigroup estimate; a fixed-support source is not automatically confined to one energy. A bulk limit additionally requires a boundary-distance prescription. The result supplies neither arbitrary growing families of marks nor fixed-physical-time infinite-volume dynamics, and it does not identify the inherited state with an independently prepared regional vacuum.
