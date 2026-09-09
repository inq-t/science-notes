# The Centered Poisson Equation Returns the Uniform Planar Source

A sixth-order vacuum approximation and a finite centered Poisson construction give a uniform nonlinear susceptibility bound on the growing planar patch. The calculation retains the changing source mean, variance and vacuum projection. Its explicit error ledger gives a remainder \(Ch^4(L+1)^{23}\), stronger than the original target. The proof uses the actual compact operator and cutoff estimates, alongside the finite oscillator calculation.

**Status: proved uniform susceptibility remainder on the stated growing-patch window.** [[compact-source-normalization-and-the-nonlinear-return|CS]] and [[comb-chart-ellipticity-and-uniform-local-comparison|UC19–20]] supply the finite coefficients. [[uniform-planar-localization-and-the-first-physical-levels|UP]] supplies actual spectral isolation; [[weighted-compact-source-return-on-growing-patches|WS]] supplies weighted source transfer. [[compact-operator-taylor-remainder-on-planar-wells|The operator remainder]] and [[compact-cutoffs-and-uniform-polynomial-quasimodes|the compact cutoff construction]] establish (PO1) on the actual carrier. The source is the original fixed comb probe throughout.

## The actual comparison needed from the local construction

Put \(n=L+1\), \(h=(\kappa/g)^{1/4}\), \(\epsilon=hn^{10}\), and restrict \(0<\epsilon\le\eta\), with \(\eta\) sufficiently small and independent of \(L\). Let \(\widehat H=H_{L,g}/\sqrt{\kappa g}\).

Use CQ's even invariant magnetic cutoff, whose support and unit region have radii comparable to \(\delta_*n^{-1/2}\), and its Haar half-density map \(\mathcal J_h\). The actual operator comparison is
\[
\boxed{
\left\|\widehat H\mathcal J_hu
-\mathcal J_h\sum_{r=0}^{6}h^rV_ru\right\|
\le C h^7n^{29/2}\|u\|,
\qquad u\in P_{\le20}.}
\tag{PO1}
\]
OT8 at order six gives the interior \(h^7n^{29/2}\) term. CQ9, for example with \(q=4\), bounds the cutoff commutator by \(Ch^9n^{14}\), which is smaller on this window. This proves (PO1) in norm on the actual compact operator; a local quadratic-form Taylor bound would not suffice.

For the same finite-degree space, Gaussian moments give the uniform cutoff estimates
\[
t_h=C(hn^{3/2})^8=Ch^8n^{12},\qquad
\|(1-\chi_h)u\|
+\omega^{-1}\|(1-\chi_h)B_hu\|
\le t_h\|u\|,
\tag{PO2}
\]
where \(\omega=\sqrt{\lambda_{\min}(A_L)}\asymp n^{-1}\) and \(B_h=4\mathcal B_L/h^2\) has its exact sinc expression in the chart. Indeed the scaled cutoff radius is comparable to \((h\sqrt n)^{-1}\); use eighth moments of total radius and the weighted Gaussian bounds in WS. Hölder's inequality gives
\(\||X|^8B_hu\|\le Cn^8\omega\|u\|\) in this window. Equation (PO2) also bounds the defect of inner products under \(\mathcal J_h\).

## Construct the normalized source coefficients

Let \(\Omega\) be the normalized oscillator vacuum, \(e_0\) its energy, \(K_0=V_0-e_0\), and \(R_0=K_0^{-1}\) off \(\Omega\). The known physical bound is \(\|R_0\|\le Cn\).

Use the ordinary formal coefficients
\[
\psi^{[6]}(h)=\sum_{r=0}^6h^r\psi_r,\qquad
\lambda^{[6]}(h)=\sum_{r=0}^6h^re_r,\qquad \psi_0=\Omega .
\]
They solve the vacuum eigen-equation and normalization through order six. UC gives
\[
\|\psi_r\|\le C_rn^{11r/2},\qquad
|e_r|\le C_rn^{11r/2-1}\quad(r\ge1),\qquad
\|V_rP_{\le m}\|\le C_{m,r}n^{3r/2+3}.
\tag{PO3}
\]
Their parity is the parity of \(r\); odd energy coefficients vanish. Each \(\psi_r\) has Hermite degree at most \(3r\).

The source jets are explicit. Set
\[
Z_{2j+1}=\sum_pv_{11}(p)|X_p|^{2j}X_p,\qquad
a_j=\frac{(-1)^j}{2^{2j}(2j+1)!}.
\]
Then
\[
B_{2k}=\sum_{j=0}^ka_ja_{k-j}
Z_{2j+1}\cdot Z_{2(k-j)+1},\qquad B_{2k+1}=0.
\tag{PO4}
\]
In particular \(B_0=|Y|^2\) and \(B_2=-Y\cdot Z_3/12\). The odd-sum argument in WS applies at every fixed polynomial degree, giving
\[
\|B_0P_{\le m}\|\le C_m\omega,\quad
\|B_2P_{\le m}\|\le C_m\sqrt\omega,\quad
\|B_{2k}P_{\le m}\|\le C_{m,k}\quad(k\ge2).
\]
The Taylor remainder through \(B_6\) is bounded by \(C_mh^8\) on these spaces.

Form the mean \(m(h)\), centered vector \(F(h)\), variance \(N(h)\), and normalized source \(z(h)\) as formal series:
\[
m=\langle\psi,B\psi\rangle,\qquad
F=(B-m)\psi,\qquad N=\langle F,F\rangle,\qquad
z=F/\sqrt N .
\tag{PO5}
\]
The vacuum series is normalized before these operations. Since
\(N_0=6\omega^2\), finite multiplication and the binomial series for
\((N/N_0)^{-1/2}\) give
\[
\|F_r\|\le C_rn^{11r/2-1},\quad
|N_r|\le C_rn^{11r/2-2},\quad
\boxed{\|z_r\|\le C_rn^{11r/2}.}
\tag{PO6}
\]
All coefficients through order six are finite Gaussian contractions. The vector \(z_r\) has parity \(r\) and degree at most \(3r+2\). Its leading term is the normalized scalar excitation \(\phi\), with \(K_0\phi=c_L\phi\). Higher coefficients retain its complete source leakage.

## Solve the moving centered Poisson equation

Write \(A_s=V_s-e_sI\), and seek \(y(h)\) with
\((V(h)-e(h))y(h)=z(h)\) and \(\langle\psi(h),y(h)\rangle=0\). Set \(y_0=R_0\phi\). For \(r\ge1\), the explicit recursion is
\[
\boxed{
y_r=
R_0\left(z_r-\sum_{s=1}^r A_sy_{r-s}\right)
-\left(\sum_{s=1}^r\langle\psi_s,y_{r-s}\rangle\right)\Omega .}
\tag{PO7}
\]
The scalar is the moving-vacuum orthogonality correction. Compatibility of the equation follows from the formal vacuum eigen-equation and \(\langle\psi,z\rangle=0\): after the lower orders vanish, the remaining right side is orthogonal to \(\Omega\).

Induction using (PO3), (PO6) and \(\|R_0\|\le Cn\) gives
\[
\boxed{\|y_r\|\le C_rn^{11r/2+1},\qquad
\deg_{\rm Hermite}y_r\le3r+2.}
\tag{PO8}
\]
For example the \(V_1y_{r-1}\) term costs
\(n\cdot n^{9/2}\cdot n^{11(r-1)/2+1}=n^{11r/2+1}\).
The energy coefficients and the scalar in (PO7) obey the same bound. Thus degree twenty suffices through order six.

The formal susceptibility coefficients are
\[
s_r=\sum_{i+j=r}\langle z_i,y_j\rangle,\qquad
|s_r|\le C_rn^{11r/2+1}.
\tag{PO9}
\]
Parity gives \(s_r=0\) for odd \(r\). The first terms are \(s_0=1/c_L\) and the complete \(s_2=S_{2,L}\) of NV, including virtual transitions and leakage. The next scalar coefficient is bounded by \(Cn^{23}\).

## Transfer the source to the actual vacuum

Set \(v_h=\mathcal J_h\psi^{[6]}/\|\mathcal J_h\psi^{[6]}\|\), with approximate energy \(\lambda^{[6]}\). The first omitted formal eigen-equation terms have order \(h^7n^{75/2}\). Equations (PO1)–(PO3) therefore give
\[
\rho_h=\|(\widehat H-\lambda^{[6]})v_h\|
\le Ch^7n^{75/2}.
\tag{PO10}
\]
UP's ordered eigenvalue comparison selects the ground branch: the formal energy shift from \(e_0\) is \(O(h^2n^{10})\), while UP's absolute comparison error is \(O(\epsilon^{2/3}n^{-4})\). Both fit inside its isolated ground interval when \(\eta\) is sufficiently small. Spectral projection then gives
\(|E_0(h)-\lambda^{[6]}|\le\rho_h\).

Let \(\zeta_h\) be the actual centered and normalized compact-source vector. The normalized polynomial approximation differs from \(\Omega\) by \(O(hn^{11/2})\). WS's Gaussian bounds therefore verify its source norm and variance conditions uniformly. Applying its exact compact graph-norm transfer gives
\[
\boxed{
\|\zeta_h-\zeta(v_h)\|\le Cn^4\rho_h
\le Ch^7n^{83/2}.}
\tag{PO11}
\]
The mean and variance in this statement are evaluated in their respective actual and approximating states.

Let \(Z_h=\mathcal J_h\sum_{r=0}^6h^rz_r\).
The finite source expansion, its exact normalization, and (PO2) give
\[
\|\zeta(v_h)-Z_h\|
\le C\bigl(h^7n^{77/2}+t_h\bigr).
\tag{PO12}
\]
One can see uniformity by rescaling the finite coefficients with
\(\theta=hn^{11/2}\). The state and relative variance stay in fixed neighborhoods of their nonzero leading values, so the norm and inverse-square-root operations have uniform finite-order remainders. The extra sinc remainder contributes only \(Ch^8/\omega\le Ch^8n\). Both it and \(t_h\) are smaller than the right side of (PO12).

## The actual reduced inverse closes the error ledger

Put \(Y_h=\mathcal J_h\sum_{r=0}^6h^ry_r\); then \(\|Y_h\|\le Cn\). The first omitted products in (PO7) cost \(h^7n^{77/2}\). Including the actual operator comparison gives
\[
\|(\widehat H-\lambda^{[6]})Y_h-Z_h\|
\le Ch^7n^{77/2}.
\]
Combining the ground-energy error, (PO11) and (PO12), for
\(K_h=\widehat H-E_0(h)\),
\[
\boxed{\|K_hY_h-\zeta_h\|\le Ch^7n^{83/2}.}
\tag{PO13}
\]
The actual vacuum-subtracted inverse has norm at most \(Cn\). Although \(Y_h\) need not be exactly orthogonal to the actual vacuum, its vacuum component drops from the susceptibility because \(\zeta_h\) is exactly centered. More explicitly,
\[
Q_hY_h-K_h^{-1}\zeta_h
=K_h^{-1}(K_hY_h-\zeta_h),
\qquad Q_h=I-|\psi_h\rangle\langle\psi_h|.
\]
Consequently the actual normalized scaled susceptibility satisfies
\[
\left|\mathcal S_L(h)-\langle Z_h,Y_h\rangle\right|
\le Ch^7n^{85/2}.
\tag{PO14}
\]
This is a source-vector and Poisson-residual argument. It assumes neither that the source remains in its first excitation nor a global norm-resolvent identification with the oscillator.

The full Gaussian inner product of the two finite series has only even powers. Terms of order four and higher are bounded by \(Ch^4n^{23}\), because \(\theta=hn^{11/2}\) is uniformly small. Its cutoff error is at most \(Cnt_h\le Ch^8n^{13}\). Thus
\[
\boxed{
\left|\mathcal S_L(h)-\frac1{c_L}-h^2S_{2,L}\right|
\le C\left(h^4n^{23}+h^7n^{85/2}+h^8n^{13}\right)
\le Ch^4n^{23}.}
\tag{PO15}
\]
For the last inequality,
\(h^3n^{39/2}=\epsilon^3n^{-21/2}\) bounds the ratio of the second term to the first. The third is smaller as well. This establishes GW4 with a stronger power on the same window; it does not widen that window.

The operator and cutoff estimates are essential to the actual return; formal coefficients alone would leave it unproved. The result concerns the original marked source in the isolated planar theory. It supplies no fixed-coupling infinite-volume limit, inherited regional vacuum, or four-dimensional Yang–Mills gap.
