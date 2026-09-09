# A Fixed Oriented Probe Tracks the Four-Face Gap

Two bounded oriented triple products cancel the leading spectral leakage of the four-face scalar probe. Their coefficients are fixed by the actual cubic response, and do not depend on the confinement strength. The resulting physical observable tracks the inverse gap and its innovation quotient through the first nonlinear order. Comparing it with the original probe separates the negative gap shift from a redistribution of source weight, within the same Hamiltonian and vacuum.

**Status: proved first nonlinear source response at the fixed four-face patch.** [[four-face-cubic-response-and-source-leakage|FC1–14]] supplies the exact leakage channels. [[four-face-gap-shift-and-the-complete-source-response|The complete four-face calculation]] supplies the gap coefficient. [[compact-source-normalization-and-the-nonlinear-return|CS]] supplies the compact realization and remainder estimates. This is a second physical probe in the complete observable algebra, not a change of the original probe or of the dynamics.

## Fix the compact observable before changing the strength

Keep the comb-based face holonomies and mode orientation of FC1. Write
\[
P_p=q_{0,p}I-i\mathbf q_p\cdot\sigma,\qquad
\mathbf Q_m=\sum_p O_{pm}\mathbf q_p,\qquad m=0,1,2,3.
\tag{OS1}
\]
The original compact source is \(\mathcal B=|\mathbf Q_0|^2\). Define the distinct source
\[
\boxed{
\mathcal B^\sharp=
|\mathbf Q_0|^2
-\frac27\mathbf Q_0\cdot(\mathbf Q_1\times\mathbf Q_2)
-\mathbf Q_0\cdot(\mathbf Q_1\times\mathbf Q_3).}
\tag{OS2}
\]
The face words, matrix \(O\), orientations and coefficients in (OS2) are fixed once. In particular the source has no dependence on \(g\), the exact vacuum, or a spectral projector.

Each \(\mathbf Q_m\) transforms by the same proper color rotation under residual \(SU(2)\) conjugation. Dot and oriented triple products are therefore gauge invariant. Compactness makes (OS2) a bounded real multiplication observable on the full physical carrier. Positivity of its values is not required for a self-adjoint source.

## The actual cubic correction cancels both leakage channels

Put \(h=(\kappa/g)^{1/4}\). In the same face chart as FC,
\[
\mathbf Q_m=\frac h2Y_m+O(h^3).
\]
Use \(T_{ijk}=Y_i\cdot(Y_j\times Y_k)\), and let \(B_h=4\mathcal B/h^2\). Equation (OS2) gives
\[
\boxed{
B_h^\sharp:=\frac4{h^2}\mathcal B^\sharp
=B_0+hD+h^2B_2+O(h^3),\qquad
D=-\frac17T_{012}-\frac12T_{013}.}
\tag{OS3}
\]
Here \(B_0=|Y_0|^2\), and \(B_2\) is the original source curvature from NV2. The triple products first contribute at order \(h\) and then at order \(h^3\) after this scaling.

The harmonic mean and variance remain \(m_0=3\sqrt2\) and \(N_0=12\). Let \(\Omega\) be the normalized vacuum, \(u\) its first correction, \(\phi=f\Omega\) the normalized first scalar excitation, and \(\eta_1\) that excitation's first correction. FC10 proves
\[
\ell=fu-\eta_1
=\left(\frac{\sqrt3}{42}T_{012}
+\frac{\sqrt3}{12}T_{013}\right)\Omega .
\tag{OS4}
\]
Consequently
\[
D\Omega=-\sqrt{N_0}\,\ell .
\]
The odd polynomial \(D\) has zero harmonic mean. The order-\(h\) mean and variance coefficients also vanish by normal parity. The first normalized centered-source vector is therefore
\[
\frac{F_1^\sharp}{\sqrt{N_0}}
=fu+\frac{D\Omega}{\sqrt{N_0}}
=\eta_1 .
\tag{OS5}
\]
It agrees with the changing excitation vector to this order: \(\ell^\sharp=0\).

For a general correction \(-a\,\mathbf Q_0\cdot(\mathbf Q_1\times\mathbf Q_2)-b\,\mathbf Q_0\cdot(\mathbf Q_1\times\mathbf Q_3)\), its scaled linear jet is \(-aT_{012}/2-bT_{013}/2\). The two cubic states are independent, so cancellation forces \(a=2/7\), \(b=1\) within this specified correction space. This does not claim uniqueness among all bounded physical observables or among additions invisible at this order.

## Center and normalize in the same actual vacuum

Let \(E=\sqrt{\kappa g}\), \(\widehat K_h=(H_{2,g}-E_0(g))/E\), and let \(\psi_h\) be the same actual vacuum used for the original probe. Define
\[
\zeta_h^\sharp=
\frac{(\mathcal B^\sharp-\langle\mathcal B^\sharp\rangle_h)\psi_h}
{\sqrt{\operatorname{Var}_h(\mathcal B^\sharp)}} .
\]
The leading variance is \(3h^4/4\), so the denominator is nonzero for sufficiently small \(h\). If \(P_{1,h}\) is the actual first physical excitation projection, (OS5) and the higher-order compact source expansion imply
\[
\boxed{\|(I-P_{1,h})\zeta_h^\sharp\|^2=O(h^4).}
\tag{OS6}
\]
CS's argument applies because (OS2) is a fixed smooth bounded source. Its rescaled operator norm remains \(O(h^{-2})\), and arbitrarily accurate vacuum quasimodes control multiplication by it. Its source jets have the same graded parity, including the odd jet \(D\). No eigenprojector is used to define the observable; \(P_{1,h}\) only states the resulting spectral estimate.

The original probe instead has escaped weight
\(h^2(2\sqrt2/49+\sqrt3/2)+O(h^4)\).
Equation (OS6) removes that leading term. It does not make the corrected source an exact eigenvector at every strength.

## The susceptibility now follows the true gap shift

Write \(c_h=\Delta_2(g)/E\). The complete energy calculation gives
\[
c_h=c+h^2d_2+O(h^4),\qquad c=2\sqrt2,\qquad
d_2=-\frac5{32}+\frac{3\sqrt2}{56}-\frac{5\sqrt3}{48}<0 .
\]
The normalized scaled susceptibility of (OS2) is
\[
\mathcal S^\sharp(h)=
\langle\zeta_h^\sharp,\widehat K_h^{-1}\zeta_h^\sharp\rangle .
\]
The fixed-patch reduced gap and (OS6) give
\[
\boxed{
\mathcal S^\sharp(h)=\frac1{c_h}+O(h^4)
=\frac1{2\sqrt2}
+h^2\left(\frac5{256}-\frac{3\sqrt2}{448}
+\frac{5\sqrt3}{384}\right)+O(h^4).}
\tag{OS7}
\]
The displayed coefficient is \(-d_2/c^2>0\). The exact spectral inequality \(\mathcal S^\sharp(h)\le1/c_h\) still holds; their first possible separation has moved to a higher order.

For comparison, the original source has
\[
\mathcal S(h)=\frac1c+h^2\left[
-\frac{d_2}{c^2}
-\frac{1101}{2744}+\frac{4\sqrt2}{343}+\frac{\sqrt3}{8}
\right]+O(h^4).
\]
Its full coefficient is negative, as the complete four-face calculation verifies. Thus the two fixed observables have opposite first susceptibility corrections in the same vacuum. The physical gap has the same negative correction relative to its harmonic value in both comparisons; their differing response comes from the source weights.

## The chronological comparison uses the same clock

Fix a scaled duration \(\tau>0\), corresponding to physical duration \(\tau/E\), and put
\[
A_{\tau,h}=e^{-\tau\widehat K_h},\qquad
R_{\tau,h}=I-A_{\tau,h}^2,\qquad
q^\sharp_\tau(h)=
\frac{\langle\zeta_h^\sharp,R_{\tau,h}^2\zeta_h^\sharp\rangle}
{\langle\zeta_h^\sharp,R_{\tau,h}\zeta_h^\sharp\rangle}.
\]
The same spectral estimate gives
\[
\boxed{
q^\sharp_\tau(h)=1-e^{-2\tau c_h}+O_\tau(h^4)
=1-e^{-2\tau c}
+2\tau d_2e^{-2\tau c}h^2+O_\tau(h^4).}
\tag{OS8}
\]
Its first nonlinear coefficient is negative. The leading denominator is nonzero, and the remainder is uniform on fixed compact duration intervals contained in \((0,\infty)\).

The original probe's positive order-\(h^2\) leakage contribution is instead
\[
\boxed{
q_\tau(h)-(1-e^{-2\tau c_h})
=h^2\sum_{i=1}^2w_i
\frac{r_i(r_i-r_c)}{r_c}+O_\tau(h^4),}
\tag{OS9}
\]
where
\[
(w_1,w_2)=\left(\frac{2\sqrt2}{49},\frac{\sqrt3}{2}\right),\quad
(\nu_1,\nu_2)=(4+\sqrt2,\,2+\sqrt2+\sqrt6),\quad
r_i=1-e^{-2\tau\nu_i},\quad r_c=1-e^{-2\tau c}.
\]
Every summand is positive because \(\nu_i>c\). This is the contribution relative to the changing gap benchmark; it is not a claim that the original quotient's total correction has the same sign at every duration.

Both probes belong to the same complete physical source algebra. A uniform innovation inequality must apply to the corrected probe as well as the original one. The cancellation exposes a negative gap correction that source redistribution can obscure, but it constructs no mass mechanism and supplies no volume-uniform conclusion. The Hamiltonian, actual vacuum, comparison paths and clock have remained the same throughout.
