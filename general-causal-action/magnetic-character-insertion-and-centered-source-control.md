# The Centered Character Insertion Has Only a Square-Root Volume Cost

The global magnetic parameter insertion has a centered harmonic norm proportional to the patch width, although its mean is proportional to the patch area. Subtracting that mean before comparing vacuum amplitudes preserves this improvement in the actual compact theory. The resulting source-vector error is \(C_Ih(L+1)^{13/2}\), with the original insertion, actual mean and full physical carrier retained.

**Status: proved uniform centered source-vector return for the fixed three-block \(SU(2)\) preparation family.** [[uniform-weighted-character-return-and-the-soft-gap|UW]] fixes the family and its compact spectral construction. [[uniform-local-conditional-character-return|UL]] supplies the common complete-face chart and normalized polynomial vacuum. This module controls the global insertion paired with [[conditional-cumulant-influence-and-the-original-chronology|CI's conditional influence]]; it does not replace the inherited dynamics.

## Center the same magnetic derivative

Use UW's scales and parameter interval:
\[
n=L+1,\qquad h=(\kappa/(15g))^{1/4},\qquad
\delta=hn^{10},\qquad \theta=hn^{11/2},\qquad
\varepsilon\in I\Subset(-1/14,1/16).
\]
Let \(v_\varepsilon\) be the actual normalized positive vacuum of the scaled Hamiltonian \(\widehat H_\varepsilon\), and let
\[
Q_\varepsilon=1-|v_\varepsilon\rangle\langle v_\varepsilon|,
\qquad
B_\varepsilon=\partial_\varepsilon\widehat H_\varepsilon,
\qquad D_h=h^{-2}B_\varepsilon.
\]
The derivative holds the electric operator, \(L,h\), source maps and Haar carrier fixed. In this affine preparation family, the multiplication function \(B_\varepsilon\) itself is independent of \(\varepsilon\), although its vacuum law is not. Define
\[
g_{\varepsilon,L,h}
=Q_\varepsilon D_hv_\varepsilon
=(D_h-\mathbb E_\varepsilon D_h)v_\varepsilon.
\tag{MI1}
\]
Thus the mixed kernel with this vector is precisely CI's original covariance divided by \(h^2\).

In the harmonic space, write
\[
C_L=\sqrt{4I-\operatorname{Adj}_L},\qquad
\mu_0=\Omega_L^2dX,\qquad
B_2(X)=-\frac7{120}\sum_p|X_p|^4,
\]
\[
a_0=\mathbb E_0B_2,\qquad
b_0=(B_2-a_0)\Omega_L,\qquad
Q_0=1-|\Omega_L\rangle\langle\Omega_L|.
\tag{MI2}
\]
The three color components have covariance \(C_L\). The invariant vector \(b_0\) has Hermite degrees two and four, with no vacuum component.

## The centered fourth-power sum costs only \(n\)

For two three-component centered isotropic Gaussian vectors with component variances \(c_p,c_q\) and component cross covariance \(c_{pq}\), radial Wick contraction gives
\[
\operatorname{Cov}(|X_p|^4,|X_q|^4)
=120c_{pq}^4+600c_pc_qc_{pq}^2.
\tag{MI3}
\]
To check the constants, decompose
\[
|X_p|^4
=\mathcal H_{4,c_p}(X_p)
+10c_p(|X_p|^2-3c_p)+15c_p^2.
\]
The fourth-chaos pairing is \(120c_{pq}^4\); the second-chaos pairing is
\(100c_pc_q\,6c_{pq}^2\). Different chaoses are orthogonal.

Here \(c_p=(C_L)_{pp}\le2\), \(|c_{pq}|\le2\), and
\[
\sum_{p,q}(C_L)_{pq}^2
=\operatorname{Tr}(C_L^2)=4L^2.
\]
Consequently
\[
\boxed{
\|b_0\|_2\le Cn,\qquad
\|B_2-a_0\|_{L^q(\mu_0)}\le C_qn
\quad\text{for every fixed }q<\infty.}
\tag{MI4}
\]
The second estimate uses the fixed-chaos norm comparison proved by Wick contractions in UL. Its constants do not grow with the number of faces. In contrast, \(|a_0|\le Cn^2\). On any fixed-degree polynomial amplitude \(p\), Hölder therefore gives
\[
\|(B_2-a_0)p\|_2
\le Cn\|p\|_4.
\tag{MI5}
\]
All norms in (MI4)–(MI5), except the amplitude norm of \(b_0\), use \(\mu_0\). No independent-face approximation is made: the full off-diagonal covariance enters (MI3).

## The exact insertion admits a global comparison function

Use UL's parameter-independent principal chart and exact Haar half-density, followed by zero extension. Write all amplitudes on the common flat space \(L^2(dX)\). With
\[
v_h(X_p)=2\bigl(1-\cos(h|X_p|/2)\bigr),
\]
the same insertion has the extension
\[
D_h(X)=h^{-4}\sum_p\frac{v_h(X_p)^2(5v_h(X_p)-14)}{15}.
\tag{MI6}
\]
It agrees with the original compact multiplication operator on the supported actual amplitude. Its values elsewhere serve only to compare Gaussian vectors.

For every real \(X\),
\[
\boxed{
\|D_h\|_\infty\le Ch^{-4}n^2,\qquad
|D_h(X)|\le C\sum_p|X_p|^4,\qquad
|D_h(X)-B_2(X)|\le Ch^2\sum_p|X_p|^6.}
\tag{MI7}
\]
The first uses \(0\le v_h\le4\); the second also uses \(v_h\le h^2|X_p|^2/4\). For the third, put \(t=h|X_p|\). The even trigonometric polynomial
\[
d(t)=\frac{[2(1-\cos(t/2))]^2[10(1-\cos(t/2))-14]}{15}
\]
has fourth Taylor term \(-7t^4/120\), and its sixth derivative is bounded globally. Its terms of orders zero and two vanish. Taylor's integral remainder therefore bounds
\(|d(t)+7t^4/120|\) by \(C|t|^6\) for every \(t\). This is an estimate for the identical character insertion, including outside the local well.

## Approximate the vacuum only after subtracting the common scalar

Use order \(M=18\) in UL and [[magnetic-parameter-tangents-and-uniform-vacuum-control|MVT]], and set
\[
u=U_{18}/\|U_{18}\|,\qquad
q=\chi_{L,h}U_{18}/\|\chi_{L,h}U_{18}\|,\qquad
p=u/\Omega_L,\qquad \tau=hn^{3/2}.
\]
These actual, cut and uncut vectors are normalized in the same flat carrier. Their established estimates are
\[
\|v_\varepsilon-q\|\le C_In\rho_{18},\qquad
\rho_{18}=C_Ih^{19}n^{207/2},\qquad
\|q-u\|\le C_I\tau^8,\qquad
\|p-1\|_4\le C_I\theta,\quad \|p\|_4\le C_I.
\tag{MI8}
\]
No parameter derivative is needed here. The fixed window may be reduced by a constant to accommodate this fixed approximation order.

Every fixed moment of one face is bounded uniformly, since its three-component Gaussian covariance is at most \(2I_3\). Hence
\[
\left\|\sum_p|X_p|^6\right\|_{L^4(\mu_0)}
\le Cn^2.
\]
Combining this with (MI5) and (MI7) gives
\[
\begin{aligned}
\|(D_h-a_0)u-b_0\|
&\le \|(D_h-B_2)p\|_{L^2(\mu_0)}
+\|(B_2-a_0)(p-1)\|_{L^2(\mu_0)}\\
&\le C_I(h^2n^2+n\theta).
\end{aligned}
\tag{MI9}
\]
Using \(\|D_h-a_0\|_\infty\le Ch^{-4}n^2\) on the two preceding amplitude differences then proves
\[
\begin{aligned}
\|(D_h-a_0)v_\varepsilon-b_0\|
&\le C_I\{h^{-4}n^3\rho_{18}
+h^{-4}n^2\tau^8+h^2n^2+n\theta\}\\
&\le\boxed{C_In\theta=C_Ih n^{13/2}.}
\end{aligned}
\tag{MI10}
\]
For clarity, the first two losses are \(h^{15}n^{213/2}\) and \(h^4n^{14}\). Dividing them by \(n\theta\) gives respectively
\(\delta^{14}n^{-40}\) and \(\delta^3n^{-45/2}\); the source Taylor loss has ratio \(hn^{-9/2}\). They are uniformly harmless on \(0<\delta\le\eta_I\).

Subtracting the actual expectation only after bounding an uncentered product would obscure (MI4). The fixed scalar \(a_0\) cancels exactly under \(Q_\varepsilon\), so subtracting it before the comparison changes neither the actual vector nor its observable.

## Return to the actual centered embedding

Let \(\mathcal J\) be CQ's exact compact density transform with cutoff, and define the centered comparison map
\[
\mathcal I_{\varepsilon,L,h}=Q_\varepsilon\mathcal JQ_0.
\]
In the common flat coordinates, \(\mathcal Jb_0=\chi_{L,h}b_0\). Since \(b_0\) has fixed degree, CQ's tail estimate and (MI4) give
\[
\|(1-\chi_{L,h})b_0\|\le Cn\tau^8.
\]
Applying the contraction \(Q_\varepsilon\) to (MI10) therefore yields
\[
\boxed{
\|g_{\varepsilon,L,h}-\mathcal I_{\varepsilon,L,h}b_0\|
\le C_Ih n^{13/2},\qquad
\|g_{\varepsilon,L,h}\|\le C_In.}
\tag{MI11}
\]
The last estimate also uses \(\|\mathcal I\|\le1\) and \(\theta\le\eta_I\). The original source vector and its actual centering are retained exactly; \(\mathcal I\) only compares carriers.

The source is global, with a square-root volume norm after centering. It is not a single-face observable or an independently prepared regional source. Combining this estimate with a returned conditional influence and a centered chronological comparison is a separate step. It can control one mixed response throughout the strong-confinement window; it does not establish a positive floor for the complete physical source algebra.
