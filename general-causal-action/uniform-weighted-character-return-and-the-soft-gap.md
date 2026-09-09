# Weighted Character Contrast Returns Uniformly to the Spatial Soft Gap

The three-block character family has a uniform actual compact return on the same growing-patch confinement window as the fundamental planar model. Its changing part is a sum of single-face multiplication operators, which gives a sharper parameter derivative than subtracting two general remainder bounds. The resulting gap contrast has error \(C|\Delta\varepsilon|h^4(L+1)^{13}\). This resolves its order-\(h^2/(L+1)\) spatial coefficient throughout \(h(L+1)^{10}\le\eta\), with the same physical scale and full Gauss carrier.

**Status: proved uniform weighted-family spectral return and parameter-contrast estimate.** [[equal-character-hessians-and-the-nonlinear-source-discriminator|EH]] fixes the representation and preparation family. [[uniform-planar-localization-and-the-first-physical-levels|UP]], [[compact-operator-taylor-remainder-on-planar-wells|OT]], [[compact-cutoffs-and-uniform-polynomial-quasimodes|CQ]] and [[uniform-nonlinear-planar-gap-and-marked-response|UN]] supply the localization and finite-order proof structure; the changes needed for this family are proved below. [[weighted-character-gap-coefficient-and-the-spatial-soft-mode|The spatial coefficient calculation]] owns the exact \(k_L\) and its sine-mode limit. No parameter derivative is inferred by differentiating an unspecified remainder.

## The exact potential keeps a uniform global well

Use EH's fixed faithful representation
\(\rho=\rho_{1/2}\oplus\rho_1\oplus\rho_{3/2}\) of \(SU(2)\), and
\[
A_\varepsilon=(1+14\varepsilon)I_2
\oplus(1-16\varepsilon)I_3
\oplus(1+5\varepsilon)I_4.
\]
Fix a compact interval \(I\subset(-1/14,1/16)\) for the preparation parameter \(\varepsilon\). Its quadratic index is \(I_A=15/2\), independently of \(\varepsilon\). On the open \(L\times L\) patch, with every vertex gauged, put
\[
n=L+1,\qquad h=(\kappa/(15g))^{1/4},\qquad
E=\kappa h^{-2},\qquad
\delta=hn^{10},\qquad \theta=hn^{11/2}.
\tag{UW1}
\]
The symbols \(\varepsilon\) and \(\delta\) denote the preparation parameter and confinement window parameter, respectively. The exact physical scale \(E\) is common to the family.

For a single face let \(u=\chi_{1/2}(P)/2\) and \(v=2(1-u)\). The elementary character identities give
\[
\boxed{
w_\varepsilon(P):=\frac{W_{A_\varepsilon}(P)}{15}
=v-\frac{7+14\varepsilon}{15}v^2
+\frac{1+5\varepsilon}{15}v^3.}
\tag{UW2}
\]
In particular \(0\le v\le4\). Every irreducible character cost
\(d_j-\chi_j(P)\) is nonnegative. The positive fundamental block gives
\[
\boxed{m_Iv\le w_\varepsilon(P)\le M_Iv
\quad(\varepsilon\in I,\ P\in SU(2)),}
\tag{UW3}
\]
with \(m_I>0\) and finite \(M_I\) independent of \(L\). One may take
\(m_I=\min_I(1+14\varepsilon)/15\); the upper bound follows either from (UW2) or the bounded character ratios. Thus the identity remains the unique common minimum.

The parameter derivative is
\[
\partial_\varepsilon w_\varepsilon
=\frac{v^2(5v-14)}{15}.
\]
It changes sign away from the well. No global operator monotonicity is used. Near \(P=\exp y\),
\[
w_\varepsilon(\exp y)=|y|^2/4+O_I(|y|^4),
\qquad
\partial_\varepsilon\!\left[h^{-2}w_\varepsilon(e^{hX})\right]
=-\frac7{120}h^2|X|^4+O_I(h^4|X|^6).
\tag{UW4}
\]
All fixed local derivatives have constants uniform on \(I\).

## The original cutoff works for the new Hamiltonians

Write \(W_0=\sum_pv(P_p)\). The actual scaled operator is
\[
\widehat H_{\varepsilon,L,h}
=h^2\mathsf C_{\rm raw}+h^{-2}\sum_pw_\varepsilon(P_p).
\]
Keep UP and CQ's cutoff as a function of \(W_0\), rather than replacing it by the new potential. Its exact identities are unchanged:
\[
\mathsf C_{\rm raw}W_0=3W_0-6L^2,\qquad
\Gamma(W_0)\le8W_0.
\tag{UW5}
\]
All multiplication potentials commute with this cutoff. Consequently CQ's exact cutoff commutator, density factors, polynomial tail estimates and spatial powers hold verbatim. This use of \(W_0\) is an auxiliary localization choice, not a substitution in the Hamiltonian.

For UP's lower min–max bound, (UW3) changes the exterior threshold from \(\delta_{\rm chart}^2/h^2\) to \(m_I\delta_{\rm chart}^2/h^2\). Inside, (UW4) has the same quadratic oscillator and a relative \(O_I(\delta_{\rm chart}^2)\) magnetic error. The comb metric and product Haar density do not depend on \(\varepsilon\). Enlarging UP's fixed radius constant and shrinking the window by constants depending on \(I\) therefore proves
\[
|\widehat E_{j,\varepsilon,L,h}-e_{j,L}^{(0)}|
\le C_I\delta^{2/3}n^{-4},\qquad j=0,1,2,
\quad 0<\delta\le\eta_I .
\tag{UW6}
\]
The extensive oscillator vacuum energy is retained in this estimate. PS's harmonic separation then gives the actual simple vacuum and first physical scalar branches, each separated from the other physical spectrum by at least \(c_I/n\). This holds uniformly in \(L\) and \(\varepsilon\in I\).

## Uniform finite-order expansions retain parity

The electric and Haar operator jets are unchanged. The new magnetic Taylor coefficients are finite sums of the same single-face even powers, with uniformly bounded coefficients on \(I\). Thus OT's actual interior norm remainder and UC's fixed-order jet bounds remain
\[
\|V_{r,\varepsilon}P_{\le m,L}\|
\le C_{I,m,r}n^{3r/2+3},\qquad r\ge1.
\]
The local potential Taylor remainder is bounded by a constant times
\(h^{M+1}\sum_p|X_p|^{M+3}\), on the same uniform chart. It fits OT's stated, larger envelope. No estimate for the new potential is inferred merely from its value comparison (UW3).

For either selected harmonic seed, the normalized formal recursion and the harmonic inverse bound \(C n\) give
\[
\|\psi_{r,\varepsilon}\|\le C_{I,r}n^{11r/2},
\qquad
|e_{r,\varepsilon}|\le C_{I,r}n^{11r/2-1}.
\]
The common jets have parity \((-1)^r\), and the two seeds are even. Hence all odd energy coefficients vanish. CQ yields, at every fixed order \(M\ge1\), normalized actual compact quasimodes \(\Psi_{M,\varepsilon}\) of approximate energy \(z_{M,\varepsilon}\), with
\[
\boxed{\|(\widehat H_\varepsilon-z_{M,\varepsilon})\Psi_{M,\varepsilon}\|
\le \rho_M,\qquad
\rho_M=C_{I,M}h^{M+1}n^{11(M+1)/2-1}.}
\tag{UW7}
\]
Constants may depend on \(I,M\); only finitely many orders are used below.

Let \(\Delta_{\varepsilon,L}(h)\) denote the actual first physical gap in scaled units. The sixth-order argument of UN now gives, uniformly on the stated window,
\[
\Delta_{\varepsilon,L}(h)
=c_L+h^2d_L(\varepsilon)+O_I(h^4n^{21}),
\qquad c_L=2\omega_L,
\quad \omega_L=\sqrt{\lambda_{11}(A_L)} .
\tag{UW8}
\]
The bound \(|d_L(\varepsilon)|\le C_In^{10}\) is unchanged. This already proves
\[
\frac{\Delta_{\varepsilon,L}(h)}{c_L}
=1+O_I(\theta^2+\theta^4)\longrightarrow1
\]
as \(L\to\infty\), uniformly for \(0<\delta\le\eta_I\) and \(\varepsilon\in I\).

Subtracting two instances of (UW8) alone is insufficient to resolve a contrast of size \(h^2/n\) throughout this window: the corresponding relative error is \(h^2n^{22}=\delta^2n^2\). A sharper parameter estimate is needed.

## The changing operator has a smaller spatial envelope

At fixed \(\varepsilon\), denote its parameter derivative by a prime. Since the kinetic operator and quadratic character term are fixed,
\[
V'_{0,\varepsilon}=V'_{1,\varepsilon}=0.
\]
Every nonzero \(V'_{r,\varepsilon}\), \(r\ge2\), is multiplication by a sum of fixed-degree single-face polynomials. On each finite total Hermite-degree space, every coordinate of one face has bounded creation/annihilation coefficients because the oscillator covariance is bounded by \(\sqrt8\). Therefore a fixed polynomial of that face has bounded norm, independently of the total number of faces. Summing over \(L^2\) faces gives the sharper estimate
\[
\boxed{\|V'_{r,\varepsilon}P_{\le m,L}\|
\le C_{I,m,r}n^2,\qquad r\ge2.}
\tag{UW9}
\]

The normalized formal eigen-equation has an exact coefficientwise Feynman–Hellmann identity:
\[
e'_\varepsilon(h)
=\langle\psi_\varepsilon(h),
\widehat H'_\varepsilon(h)\psi_\varepsilon(h)\rangle .
\]
Differentiate the formal eigen-equation and its norm \(1\); the two terms containing \(\psi'_\varepsilon\) cancel. This is an identity of finite coefficients and assumes no convergence of the series. Combining (UW9) with the vector bounds gives
\[
\boxed{|e'_{r,\varepsilon}|
\le C_{I,r}n^{11(r-2)/2+2}
=C_{I,r}n^{11r/2-9},\qquad r\ge2.}
\tag{UW10}
\]
Indeed each term has \(i+j+k=r\), \(j\ge2\), and is bounded by
\(C n^{11(i+k)/2+2}\). Odd coefficients again vanish. In particular the fourth-order derivative costs \(n^{13}\), rather than \(n^{21}\).

## Differentiate actual quasimodes before applying Feynman–Hellmann

The needed derivative remainder follows from the construction, not by differentiating (UW7) as an inequality. Each fixed formal coefficient is a smooth function of \(\varepsilon\), obtained from a finite recursion whose harmonic inverse is independent of \(\varepsilon\). Differentiate that recursion explicitly. The same induction gives
\[
\|\psi'_{r,\varepsilon}\|\le C_{I,r}n^{11r/2}.
\]
The differentiated local operator remainder obeys the same bound as OT: its only new term is the parameter derivative of the magnetic Taylor remainder. The cutoff and density transform are independent of \(\varepsilon\). Differentiating their explicit product residual consequently gives
\[
\|\Psi'_{M,\varepsilon}\|\le C_{I,M},
\qquad
\|r'_{M,\varepsilon}\|\le C_{I,M}\rho_M,
\quad
r_{M,\varepsilon}=(\widehat H_\varepsilon-z_{M,\varepsilon})
\Psi_{M,\varepsilon}.
\]
Normalization and its derivative have bounded denominators in the same window.

Choose \(M=10\). The actual eigenvector \(v_\varepsilon\), with its phase fixed by positive overlap, satisfies
\(\|v_\varepsilon-\Psi_{10,\varepsilon}\|\le C_In\rho_{10}\) by (UW6). On the compact carrier the exact global bound is
\[
\|\widehat H'_\varepsilon\|\le C_Ih^{-2}n^2.
\]
This multiplier bound pays for the tails before any local polynomial substitution. Differentiating the residual identity and using normalized vectors gives
\[
\langle\Psi_{10},\widehat H'_\varepsilon\Psi_{10}\rangle
-z'_{10}
=\operatorname{Re}\{\langle\Psi_{10},r'_{10}\rangle
-\langle r_{10},\Psi'_{10}\rangle\}
=O_I(\rho_{10}).
\]
The actual eigenbranches are simple on \(I\), so ordinary Feynman–Hellmann applies. Together these estimates imply
\[
\boxed{|\widehat E'_{\varepsilon,L,h}-z'_{10,\varepsilon}|
\le C_I\{\rho_{10}+h^{-2}n^3\rho_{10}\}
\le C_Ih^9n^{125/2}.}
\tag{UW11}
\]
Here \(\rho_{10}=C_Ih^{11}n^{119/2}\).

After the second coefficient, (UW10) bounds the even formal remainder by
\[
C_Ih^4n^{13}(1+\theta^2+\theta^4+\theta^6).
\]
The actual error in (UW11) fits the same envelope, since
\[
\frac{h^9n^{125/2}}{h^4n^{13}}
=h^5n^{99/2}=\delta^5n^{-1/2}.
\]
This proves the sharper estimate for both physical branches and their difference:
\[
\boxed{
\left|\partial_\varepsilon\Delta_{\varepsilon,L}(h)
-h^2k_L\right|\le C_Ih^4n^{13}.}
\tag{UW12}
\]
The coefficient \(k_L=d'_L(\varepsilon)\) is independent of \(\varepsilon\): the only second-operator variation is
\(-7\sum_p|X_p|^4/120\), while \(V_1\) and the first vector corrections are unchanged.

## The contrast follows the spatial soft frequency

Integrating (UW12) between any two parameters in \(I\) gives the actual contrast, with its full dependence on the contrast size:
\[
\boxed{\left|
\Delta_{\varepsilon_2,L}(h)-\Delta_{\varepsilon_1,L}(h)
-(\varepsilon_2-\varepsilon_1)h^2k_L
\right|
\le C_I|\varepsilon_2-\varepsilon_1|h^4n^{13}.}
\tag{UW13}
\]
The [[weighted-character-gap-coefficient-and-the-spatial-soft-mode|independent spatial coefficient calculation]] gives
\[
k_L=-\frac76\omega_L(2S_L+\omega_L I_L),
\qquad
\frac{k_L}{2\omega_L}\longrightarrow-\frac76c_\infty .
\]
Here \(S_L\) is the soft-profile weighted diagonal covariance, \(I_L\) its fourth power sum, and \(c_\infty\) the bulk square-lattice mean dispersion. That calculation also gives \(|k_L|\asymp1/n\); its coefficient derivation is not needed for the uniform remainder above.

For distinct parameters, since \(c_L=2\omega_L\asymp1/n\),
\[
\boxed{
\frac{\Delta_{\varepsilon_2,L}(h)-\Delta_{\varepsilon_1,L}(h)}
{(\varepsilon_2-\varepsilon_1)h^2c_L}
=\frac{k_L}{c_L}+O_I(h^2n^{14})
\longrightarrow-\frac76c_\infty.}
\tag{UW14}
\]
The error is at most \(C_I\delta^2n^{-6}\), so this holds throughout the original confinement window, even when \(\delta\) does not tend to zero. Shrinking its fixed upper bound if needed also makes the actual gap strictly decreasing in \(\varepsilon\), uniformly in \(L\) on this window, despite the sign-changing global potential derivative.

The nonlinear contrast follows the same soft frequency. It does not remove its closing behavior in scaled units: (UW8) still gives \(\Delta_{\varepsilon,L}/c_L\to1\). Restoring physical units multiplies both gaps by the common \(E\); at fixed \(\kappa\), their absolute contrast is asymptotic to
\(\kappa(\varepsilon_2-\varepsilon_1)k_L\), which tends to zero, while the absolute gaps themselves grow on the strong-confinement window. [[uniform-local-conditional-character-return|The conditional source return]] separately proves that a local fourth-cumulant parameter coefficient stays nonzero in the bulk, with full exterior conditioning. These statements concern the isolated planar carrier and specified parameter interval. They do not supply a fixed-coupling thermodynamic limit, a four-dimensional continuum trajectory, or invariance of every nonlinear source statistic under this preparation change.
