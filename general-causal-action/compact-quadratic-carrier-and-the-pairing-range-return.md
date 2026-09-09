# The Compact Quadratic Carrier Retains the Pairing-Range Response

Every real symmetric quadratic source kernel has a uniform return from the actual compact planar vacuum to its harmonic source, even when its signed coefficients, support and pairing range vary with the patch. Centering before estimating removes the extensive mean; the small harmonic variance is retained explicitly. The resulting comparison controls all mixed quadratic covariance forms and transfers a harmonic pairing-range bound to the actual OI quotient on the same clock. It does not return arbitrary radial chaoses or the complete compact observable space.

**Status: proved uniform quadratic-source and chronological return on the confinement window; quantitative pairing-range consequence.** [[fixed-regional-sources-and-the-compact-vacuum-return|FR]] fixes the exact global chart and source convention, [[weighted-compact-source-return-on-growing-patches|WS]] supplies Gaussian and compact graph bounds, and [[compact-chronology-on-finite-hermite-sources|HC]] supplies finite-degree chronology. [[uniform-nonlinear-planar-gap-and-marked-response|UN]] selects the actual sixth-order vacuum quasimode. [[finite-pairing-range-and-the-harmonic-innovation-floor|The harmonic range theorem]] supplies the range-dependent innovation bound.

## Keep the kernel, vacuum and scale explicit

Use the full Gauss carrier and common-root comb faces of [[comb-face-transport-and-the-first-nonlinear-jet|FJ]]. Put
\[
N=L^2,\qquad n=L+1,\qquad C=\sqrt{A_L},\qquad
0<\epsilon=hn^{10}\le\eta,\qquad \theta=hn^{11/2}.
\]
Let \(B=B^{\mathsf T}\ne0\) be any real \(N\times N\) matrix, with no sign, support or range assumption. Define
\[
\beta_B=\|B\|_{\mathrm F},\quad
m_{B,0}=3\operatorname{Tr}(BC),\quad
F_B(X)=\sum_{\alpha=1}^3X_\alpha^{\mathsf T}BX_\alpha-m_{B,0},
\]
\[
u_B=F_B\Omega_L,\qquad
\sigma_B=\|u_B\|
=\sqrt6\,\|C^{1/2}BC^{1/2}\|_{\mathrm F}.
\]
The covariance eigenvalues obey \(4/n\le\lambda_{\min}(C)\le\|C\|\le\sqrt8\). Since \(\operatorname{Tr}C^2=4L^2\),
\[
\boxed{
\frac{4\sqrt6}{n}\beta_B\le\sigma_B\le\sqrt{48}\,\beta_B,
\qquad |m_{B,0}|\le6L\beta_B.}
\tag{QK1}
\]
Thus a normalized quadratic may have a variance of order \(n^{-2}\) relative to its coefficient norm. This cost is not assumed away.

For the same matrix in the compact theory retain
\[
\mathcal Q_B=\sum_{p,q}B_{pq}\mathbf q_p\cdot\mathbf q_q,\qquad
S_{B,h}=\frac4{h^2}\mathcal Q_B,\qquad
m_{B,h}=\langle\psi_h,S_{B,h}\psi_h\rangle,
\]
\[
F_{B,h}=S_{B,h}-m_{B,h},\qquad
\sigma_{B,h}=\|F_{B,h}\psi_h\|,\qquad
\zeta_{B,h}=F_{B,h}\psi_h/\sigma_{B,h}.
\tag{QK2}
\]
Here \(\psi_h\) is the actual positive normalized vacuum. All quaternion vectors use the stipulated common based color frame. Both the diagonal and the signed off-diagonal terms remain in the source.

## Center before estimating Gaussian multiplication

Let \(P_{\le m}\) be a fixed total Hermite-degree projector. A centered Gaussian quadratic divided by its own standard deviation has dimension-independent fixed moments. Hölder and the fixed-chaos moment bound used in WS therefore give
\[
\boxed{\|F_BP_{\le m}\|\le C_m\sigma_B.}
\tag{QK3}
\]
This is a bound on multiplication by the centered function, not the uncentered quadratic with mean \(m_{B,0}\).

The exact scaled chart expression is
\[
S_{B,h}(X)=
\sum_\alpha Y_{h,\alpha}^{\mathsf T}BY_{h,\alpha},\qquad
(Y_h)_p=\operatorname{sinc}(h|X_p|/2)X_p.
\]
Diagonalize \(B=\sum_j\lambda_j v_jv_j^{\mathsf T}\) with \(\|v_j\|_2=1\). WS's odd-sum estimate applies to every such vector, regardless of its support. The uniform upper covariance bound gives a rank-one source error at most \(C_mh^2\). Hence, for \(0<h\le1\),
\[
\boxed{
\|(S_{B,h}-S_{B,0})P_{\le m}\|
\le C_mh^2\sum_j|\lambda_j|
\le C_mh^2L\beta_B,}
\tag{QK4}
\]
where \(S_{B,0}=F_B+m_{B,0}\). The last inequality is the trace-norm/Frobenius inequality for \(N=L^2\). No positivity of \(B\) is used.

Put \(\overline S_{B,h}=S_{B,h}-m_{B,0}\). Equations (QK1), (QK3) and (QK4) imply
\(\|\overline S_{B,h}P_{\le m}\|
\le C_m\sigma_B(1+h^2n^2)\).
Subtracting the known scalar \(m_{B,0}\) changes neither the actual centered vector nor its variance.

On the exact compact carrier, with \(V=h^{-2}W\),
\[
|S_{B,h}|\le4\|B\|_{\mathrm{op}}V,\qquad
\|S_{B,h}v\|
\le4\|B\|_{\mathrm{op}}
  \bigl(\|\widehat Hv\|+\sqrt6L\|v\|\bigr).
\tag{QK5}
\]
Indeed \(|\mathcal Q_B|\le\|B\|_{\mathrm{op}}\sum_p|\mathbf q_p|^2
\le\|B\|_{\mathrm{op}}W\), and WS11 applies. The centered graph estimate additionally has the explicitly bounded term \(|m_{B,0}|\|v\|\).

## Pay the cutoff and vacuum errors in the same source norm

Use CQ's magnetic cutoff \(\chi_h\), map \(\mathcal J_h\), and FR's global flattening \(\mathcal U_h\), so
\(\mathcal U_h\mathcal J_hu=\chi_hu\). Set
\(\tau_h=(hn^{3/2})^8\). Uniform eighth moments give
\[
\boxed{
\|(1-\chi_h)u\|\le C_m\tau_h\|u\|,\qquad
\|(1-\chi_h)\overline S_{B,h}u\|
\le C_m\tau_h(\sigma_B+h^2n\beta_B)\|u\|,
\quad u\in P_{\le m}.}
\tag{QK6}
\]
For the second estimate first multiply by \(|X|^8\), use Hölder with (QK3), and use the same rank-one decomposition for the Taylor difference in (QK4). Its weighted norm is at most
\(C_mn^8(\sigma_B+h^2n\beta_B)\).
The cutoff radius is comparable to \((h\sqrt n)^{-1}\), yielding (QK6). These are estimates on constructed Gaussian vectors.

UN supplies a normalized compact vacuum quasimode \(v_h\), with its actual ground branch selected, such that
\[
\rho_h=\|(\widehat H-\lambda_h)v_h\|\le Ch^7n^{75/2},
\qquad
\|\psi_h-v_h\|\le Cn\rho_h.
\tag{QK7}
\]
Its uncut polynomial lies in degree eighteen and differs from \(\Omega_L\) by \(O(\theta)\). Normalization after cutoff contributes \(O(\tau_h)\). It follows from (QK3)–(QK6) that
\[
\|\overline S_{B,h}v_h-\mathcal J_hu_B\|
\le C\sigma_B(\theta+h^2n^2+\tau_h),
\]
\[
|\langle v_h,\overline S_{B,h}v_h\rangle|
\le C\sigma_B(\theta+h^2n^2+\tau_h).
\tag{QK8}
\]
The second estimate uses \(\langle\Omega_L,F_B\Omega_L\rangle=0\), with its cutoff inner-product defect retained. In particular, the factor \(m_{B,0}=O(n\beta_B)\) has not multiplied the polynomial vacuum error.

UP gives \(E_0\le Cn^2\) and a gap at least \(c/n\). The selected residual obeys
\(\|\widehat H(\psi_h-v_h)\|\le E_0\|\psi_h-v_h\|+2\rho_h\).
Using (QK5), \(\|B\|_{\mathrm{op}}\le\beta_B\), and the mean bound in (QK1),
\[
\boxed{
\|\overline S_{B,h}(\psi_h-v_h)\|
\le C\beta_Bn^3\rho_h
\le C\sigma_Bn^4\rho_h.}
\tag{QK9}
\]
This is the explicit small-variance cost of transferring the actual vacuum.

## The complete quadratic source map returns uniformly

Define
\[
d_{L,h}=\theta+h^2n^2+n^4\rho_h+\tau_h.
\]
Apply WS12's direct centering identity to the multiplier
\(\overline S_{B,h}\), then use (QK8)–(QK9). The result is
\[
\boxed{
|m_{B,h}-m_{B,0}|\le C\sigma_Bd_{L,h},\qquad
\left|\frac{\sigma_{B,h}^2}{\sigma_B^2}-1\right|
\le Cd_{L,h},}
\]
\[
\boxed{
\|\mathcal U_h(F_{B,h}\psi_h)-u_B\|
\le C\sigma_Bd_{L,h},\qquad
\|\mathcal U_h\zeta_{B,h}-u_B/\sigma_B\|
\le Cd_{L,h}.}
\tag{QK10}
\]
The cutoff source tail is included in the comparison with the uncut \(u_B\). Taking the fixed window sufficiently small gives a positive actual variance for every \(B\ne0\), uniformly; no actual lower variance is assumed as a separate hypothesis.

The error is of the same order as the vacuum correction:
\[
\boxed{d_{L,h}\le C\theta.}
\tag{QK11}
\]
Indeed
\[
\frac{h^2n^2}{\theta}=\epsilon n^{-27/2},\qquad
\frac{n^4\rho_h}{\theta}\le C\epsilon^6n^{-24},\qquad
\frac{\tau_h}{\theta}=\epsilon^7n^{-127/2}.
\]
Every constant in (QK10)–(QK11) is independent of \(B\), its range and its support.

The map
\(\mathcal A_h:u_B\mapsto F_{B,h}\psi_h\)
is linear: the actual mean is linear in \(B\). Equation (QK10) therefore proves an operator-norm source comparison on the entire physical second-chaos carrier, equipped with its harmonic covariance norm. Its dimension may grow with \(L\). This is stronger than separate bounds on a fixed list of source entries, but is still a fixed-degree statement.

## All mixed quadratic chronological forms return

Let \(K_h=\widehat H-E_0\) and \(D_t=Ce^{-tC}\). HC applies uniformly to every centered degree-two unit vector. Combining its all-time Duhamel bound with (QK10) gives
\[
\boxed{
\sup_{t\ge0}
\left|
\langle F_{B,h}\psi_h,e^{-tK_h}F_{N,h}\psi_h\rangle
-6\operatorname{Tr}(BD_tND_t)
\right|
\le C\theta\,\sigma_B\sigma_N,}
\tag{QK12}
\]
for all real symmetric \(B,N\). If both are nonzero, division by their actual standard deviations gives the analogous bound
\[
\sup_{t\ge0}
\left|
\langle\zeta_{B,h},e^{-tK_h}\zeta_{N,h}\rangle
-\frac{6\operatorname{Tr}(BD_tND_t)}{\sigma_B\sigma_N}
\right|\le C\theta .
\]
No diagonal or positivity assumption is made on either source. Because (QK12) is a bound in the harmonic source norm for every pair of vectors, arbitrary growing linear combinations are controlled without an extra number-of-marks factor. This does not estimate conditional projections on the complete compact radial space.

For the original unscaled observable \(\mathcal Q_B\), the same proof gives
\[
\mathbb E_{\psi_h}\mathcal Q_B
=\frac{h^2}{4}m_{B,0}+O(h^2\sigma_B\theta),\qquad
\operatorname{Var}_{\psi_h}\mathcal Q_B
=\frac{h^4}{16}\sigma_B^2(1+O(\theta)).
\]
The factors \(4/h^2\) cancel from normalized source vectors and OI quotients.

## A finite pairing range supplies the quotient denominator

Suppose \(B_{pq}=0\) for \(|p-q|_\infty>R\). The harmonic range theorem proves, for the normalized source \(u_B/\sigma_B\),
\[
\boxed{
G_{B,0}(t):=
1-\frac{\langle u_B,e^{-2tK_0}u_B\rangle}{\sigma_B^2}
\ge g_R(t),\qquad
\mathfrak q_{B,0}(t)\ge g_R(t),}
\]
\[
g_R(t)=\frac56(1-e^{-2t\delta_R}),\qquad
\delta_R=\frac1{\sqrt{\pi e}(2R+1)} .
\tag{QK13}
\]
Both the innovation and quotient bounds are needed for the following comparison; a positive quotient alone would not supply a nonvanishing denominator.

For the actual normalized source put
\[
G_{B,h}(t)=1-\langle\zeta_{B,h},e^{-2tK_h}\zeta_{B,h}\rangle,
\]
\[
N_{B,h}(t)=
1-2\langle\zeta_{B,h},e^{-2tK_h}\zeta_{B,h}\rangle
+\langle\zeta_{B,h},e^{-4tK_h}\zeta_{B,h}\rangle,
\qquad
\mathfrak q_{B,h}(t)=N_{B,h}(t)/G_{B,h}(t).
\]
These are the full OI response and surplus at the original duration. Equation (QK12) gives errors \(C\theta\) for both numerator and denominator. Since \(0\le N_{B,0}\le G_{B,0}\), whenever \(C\theta\le g_R(t)/2\),
\[
\boxed{
|\mathfrak q_{B,h}(t)-\mathfrak q_{B,0}(t)|
\le\frac{C\theta}{g_R(t)}
\le\frac{C'\theta}{1-e^{-2t\delta_R}}.}
\tag{QK14}
\]
In particular the error at every \(t\ge t_0>0\) is at most
\(C_{t_0}(R+1)\theta\), provided the displayed denominator condition holds.

The harmonic lower bound survives relatively when the error is smaller than that bound. A sufficient condition is \(C\theta\le g_R(t)^2/2\), giving
\[
\boxed{
\mathfrak q_{B,h}(t)\ge\tfrac12g_R(t).}
\tag{QK15}
\]
For \(t\ge t_0>0\), it suffices that
\(C_{t_0}(R+1)^2\theta\) be small. Every effective range satisfies \(R\le L-1\), so
\[
(R+1)^2\theta\le n^2\theta=\epsilon n^{-5/2}.
\]
Thus a size-independent sufficiently small subwindow, depending on \(t_0\), transfers the range lower bound simultaneously over all effective ranges. The bound itself deteriorates as the range grows; this statement does not replace it by a positive full-carrier constant.

Without a range estimate, the known harmonic gap still gives
\(G_{B,0}(t)\ge1-e^{-2tc_L}\), with \(c_L\ge8/n\). Hence (QK12) also yields a fallback quotient error \(C_{t_0}n\theta\), uniformly over all quadratic kernels and \(t\ge t_0\), when the corresponding denominator error is small. No relative estimate at arbitrarily short time follows from a constant covariance error.

## The complete quadratic range floor has the same order in every containing patch

For each finite \(L\) and integer \(0\le R\le L-1\), define
\[
c^h_{R,L}(t)=
\inf_{\substack{B=B^{\mathsf T}\ne0\\
B_{pq}=0\ \text{when }|p-q|_\infty>R}}
\mathfrak q_{B,h}(t).
\]
Every source in this infimum uses its actual mean and variance from (QK2), the same compact vacuum, and the same full chronological operator.

For every \(t_0>0\), there is a size-independent \(\eta(t_0)>0\) such that
\[
\boxed{
c_*\min\!\left\{1,\frac{t}{R+1}\right\}
\le c^h_{R,L}(t)
\le C_*\min\!\left\{1,\frac{t}{R+1}\right\}}
\tag{QK16}
\]
simultaneously for all \(L\ge1\), \(0\le R\le L-1\), \(t\ge t_0\), and
\(0<\epsilon=hn^{10}\le\eta(t_0)\). The positive constants \(c_*,C_*\) may be chosen numerical; the allowed window depends on \(t_0\).

To prove this, \(g_R(t)\) is bounded above and below by positive numerical multiples of \(\min\{1,t/(R+1)\}\). For \(t\ge t_0\), the bound
\((R+1)^2\theta\le\epsilon n^{-5/2}\)
allows the window to be chosen so that the error in (QK14) is at most \(g_R(t)/2\), uniformly in every parameter in (QK16). The lower inequality follows from (QK15).

For the upper inequality, [[localized-relational-sources-in-the-inherited-vacuum]] constructs a normalized sine-squared profile \(b\) supported on an \((R+1)\)-square inside every containing \(L\)-square. Its rank-one kernel \(B=bb^{\mathsf T}\) has pairing range at most \(R\), and its harmonic response in that containing vacuum satisfies
\[
\mathfrak q_{B,0}(t)
\le1-\exp\!\left[-\frac{16\pi^2t}{\sqrt3(R+2)}\right]
\le C\min\!\left\{1,\frac{t}{R+1}\right\}.
\]
Applying (QK14) to this same matrix gives the upper inequality in (QK16). The inherited covariance is the covariance of the full containing patch; no smaller independent vacuum is substituted. The uniform source-norm comparison in (QK10)–(QK12) justifies taking the infimum over the growing matrix family, rather than only following one fixed source.

All times above are scaled; physical duration is \(t/\sqrt{\kappa g}\). The compact source carrier returned here includes every invariant quadratic in the declared based face vectors, not every compact radial observable or arbitrary-degree marked history. The pairing-range theorem is a response bound on that source carrier, not a four-dimensional or fixed-coupling infinite-volume mass-gap theorem.
