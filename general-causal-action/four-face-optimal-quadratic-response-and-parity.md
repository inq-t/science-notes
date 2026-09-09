# The Optimal Four-Face Quadratic Response Retains Cubic Leakage

Optimizing over every quadratic comparison on the four-face patch leaves the first nonlinear innovation coefficient unchanged from the original soft-mode probe. The complete mixed response matrices have no linear term in the confinement parameter, and their harmonic minimum is simple. The optimizing quadratic therefore moves only at second order and cannot cancel the odd first-order cubic leakage. The optimal quadratic response rises at short scaled durations even though the true gap has a negative correction; at sufficiently long fixed durations its first correction is negative.

**Status: proved first nonlinear coefficient of the actual fixed-patch quadratic variational minimum.** [[four-face-gap-shift-and-the-complete-source-response|FF]] owns the exact energy and leakage coefficients. [[compact-source-normalization-and-the-nonlinear-return|CS]] supplies the actual vacuum and source expansions. [[compact-quadratic-carrier-and-the-pairing-range-return|QK]] fixes the complete quadratic source space and its normalization. The patch, comb comparison paths, Hamiltonian and clock remain fixed.

## The variational space contains all ten quadratic comparisons

Use the twelve-edge \(2\times2\) patch with Gauss law at all nine vertices and the face orientation of [[comb-face-transport-and-the-first-nonlinear-jet|FJ]]. Put
\[
h=(\kappa/g)^{1/4},\qquad E=\sqrt{\kappa g},\qquad
K_h=(H_g-E_{\rm vac}(g))/E .
\]
For \(B\in\mathcal V=\operatorname{Sym}_4(\mathbb R)\), define
\[
\mathcal Q_B=\sum_{p,q}B_{pq}\mathbf q_p\cdot\mathbf q_q,\qquad
S_h(B)=4\mathcal Q_B/h^2,
\]
\[
m_h(B)=\langle\psi_h,S_h(B)\psi_h\rangle,\qquad
F_h(B)=(S_h(B)-m_h(B))\psi_h .
\tag{OQ1}
\]
Here \(\psi_h\) is the actual normalized positive vacuum. Both the mean and the centered-vector map are linear in \(B\). The space has dimension ten; antisymmetric coefficient matrices give the zero source and are excluded. For small \(h\), its centered Gram form is positive definite by its harmonic limit.

For scaled \(t>0\), set
\[
M_h(s)[B,N]=\langle F_h(B),e^{-sK_h}F_h(N)\rangle,
\]
\[
D_h(t)=M_h(0)-M_h(2t),\qquad
A_h(t)=M_h(0)-2M_h(2t)+M_h(4t),
\]
\[
q_h(B;t)=\frac{A_h(t)[B,B]}{D_h(t)[B,B]},\qquad
q_{\rm quad}(h;t)=\min_{B\ne0}q_h(B;t).
\tag{OQ2}
\]
The actual source variance cancels between numerator and denominator. Thus (OQ2) is exactly the quotient formed with the actual variance-normalized source, not a substitution of its harmonic normalization. These are full chronological forms, without a regional reset.

## Mixed forms inherit the parity of the actual jets

In the fixed face chart and Haar half-density representation, let \(\Pi u(X)=u(-X)\). CS gives
\[
\widehat H_h\sim\mathcal O+\sum_{r\ge1}h^rV_r,\qquad
\Pi V_r\Pi=(-1)^rV_r .
\]
Every compact quadratic mark has only even multiplication jets:
\[
S_h(B)=S_0(B)+h^2S_2(B)+\cdots .
\]
The normalized vacuum has coefficient parity
\(\Pi\psi_r=(-1)^r\psi_r\). Its scalar energy and each source mean have vanishing odd coefficients. Consequently
\[
F_h(B)=\mathcal J_h\bigl(F_0(B)+hF_1(B)+h^2F_2(B)\bigr)+o(h^2),
\qquad
\Pi F_r(B)=(-1)^rF_r(B).
\tag{OQ3}
\]
The remainder is a vector norm bound uniform on bounded subsets of this fixed ten-dimensional coefficient space. It uses CS's higher-order vacuum quasimodes before multiplying by \(S_h(B)\), whose compact operator norm is \(O(h^{-2})\). The moving mean and the vacuum normalization are retained in every \(F_r\).

For completeness, the same realization controls all mixed finite-time entries, including those whose leading source occupies several oscillator energies. Write
\[
K_0=\mathcal O-e_0,\qquad K_1=V_1,\qquad K_2=V_2-e_2 .
\]
For each source \(N\), solve the finite polynomial-Gaussian evolution equations
\[
\begin{aligned}
\dot u_0&=-K_0u_0,&u_0(0)&=F_0(N),\\
\dot u_1&=-K_0u_1-K_1u_0,&u_1(0)&=F_1(N),\\
\dot u_2&=-K_0u_2-K_1u_1-K_2u_0,&u_2(0)&=F_2(N).
\end{aligned}
\tag{OQ4}
\]
Each curve lies in a fixed finite Hermite-degree space on a bounded duration interval. CS's local operator remainder applies uniformly to these curves. Duhamel with the exact contraction \(e^{-sK_h}\) then compares the actual evolution with
\(\mathcal J_h(u_0+hu_1+h^2u_2)\) up to \(o(h^2)\), uniformly for \(0\le s\le T<\infty\). This does not exponentiate a truncated polynomial Hamiltonian.

Since \(\Pi u_r=(-1)^ru_r\), the linear mixed coefficient vanishes. The actual matrix expansion is
\[
\boxed{
M_h(s)=M_0(s)+h^2M_2(s)+o_T(h^2),}
\]
\[
M_2(s)[B,N]
=\langle F_2(B),u_0(s;N)\rangle
+\langle F_1(B),u_1(s;N)\rangle
+\langle F_0(B),u_2(s;N)\rangle .
\tag{OQ5}
\]
It holds in matrix norm, and hence uniformly over all quadratic directions after fixing a coefficient norm. The same even expansion holds for \(D_h,A_h\). This is asymptotic normal-coordinate parity. No exact global symmetry under inversion of all compact holonomies is assumed.

## The harmonic generalized minimum is isolated

In the normal coordinates \(Y_i=\sum_pv_i(p)X_p\) of FF2, the four frequencies are
\[
(\omega_0,\omega_1,\omega_2,\omega_3)
=(\sqrt2,2,2,\sqrt6).
\]
An orthonormal basis of the physical quadratic oscillator carrier is
\[
\phi_{ii}=\frac{|Y_i|^2-3\omega_i}{\sqrt6\,\omega_i}\Omega,\qquad
\phi_{ij}=\frac{Y_i\cdot Y_j}{\sqrt{3\omega_i\omega_j}}\Omega
\quad(i<j).
\]
Each is an exact eigenvector with energy
\(\nu_{ij}=\omega_i+\omega_j\). Put \(r_\nu(t)=1-e^{-2t\nu}\). In these source coordinates,
\[
D_0(t)=\operatorname{diag}(r_{\nu_{ij}}),\qquad
A_0(t)=\operatorname{diag}(r_{\nu_{ij}}^2).
\tag{OQ6}
\]
The generalized eigenvalues are \(r_{\nu_{ij}}\). Their minimum is
\[
\boxed{
q_{\rm quad}(0;t)=r_c(t),\qquad c=2\sqrt2,}
\]
\[
r_{\sqrt2+2}(t)-r_c(t)
=e^{-2tc}-e^{-2t(\sqrt2+2)}>0 .
\tag{OQ7}
\]
The minimizing source line is uniquely
\(B_*=v_0v_0^{\mathsf T}\), the original \(|\mathbf Q_0|^2\) probe. The degeneracy of the two frequency-\(2\) normal modes does not affect this simple lowest root.

For each fixed \(t>0\), \(D_h(t)\) stays positive definite. Whitening by its positive square root converts (OQ2) into a real symmetric matrix eigenvalue problem. Equation (OQ5) and the isolated minimum imply
\[
\boxed{
q_{\rm quad}(h;t)=r_c(t)+h^2q_2(t)+o_t(h^2),\qquad
[B_{\rm opt}(h;t)]=[B_*+O_t(h^2)].}
\tag{OQ8}
\]
Brackets denote a projective source direction. A fixed nonzero leading coefficient along \(B_*\) fixes its representative. The minimizing line is unique for sufficiently small \(h\), although its representative has a sign and scale freedom.

The coefficient is the generalized Rayleigh derivative at that leading line:
\[
q_2(t)=
\frac{A_2(t)[B_*,B_*]-r_c(t)D_2(t)[B_*,B_*]}
{D_0(t)[B_*,B_*]},
\qquad D_0(t)[B_*,B_*]=12r_c(t).
\tag{OQ9}
\]
The change in the optimizer does not contribute at this order because the leading Rayleigh quotient is stationary at its simple minimum. Thus (OQ9) is exactly the fixed-probe coefficient already evaluated in FF11.

## The optimal coefficient keeps both the gap shift and leakage

The actual first physical gap and the two leaked source channels are
\[
c_h=c+h^2d+O(h^4),\qquad
d=-\frac5{32}+\frac{3\sqrt2}{56}-\frac{5\sqrt3}{48}<0,
\]
\[
(w_1,w_2)=\left(\frac{2\sqrt2}{49},\frac{\sqrt3}{2}\right),\qquad
(\nu_1,\nu_2)=(4+\sqrt2,\ 2+\sqrt2+\sqrt6).
\]
Equations (OQ9) and FF11 give
\[
\boxed{
q_2(t)=2td\,e^{-2tc}
+\sum_{i=1}^2w_i
\frac{r_{\nu_i}(t)\bigl(r_{\nu_i}(t)-r_c(t)\bigr)}{r_c(t)}.}
\tag{OQ10}
\]
The sum is strictly positive at every fixed \(t>0\). In particular,
\[
q_{\rm quad}(h;t)-(1-e^{-2tc_h})
=h^2\sum_iw_i
\frac{r_{\nu_i}(r_{\nu_i}-r_c)}{r_c}
+o_t(h^2)>0
\]
for sufficiently small \(h\) at that duration. Optimizing every quadratic direction leaves a positive difference at order \(h^2\) from the true gap benchmark.

The exact sign limits are
\[
\frac{q_2(t)}{2t}\longrightarrow
\frac{701}{224}+\frac{3\sqrt2}{56}
-\frac{5\sqrt3}{48}+\sqrt6>0
\qquad(t\downarrow0),
\]
\[
e^{2tc}q_2(t)=
2td+\frac{2\sqrt2}{49}+\frac{\sqrt3}{2}+o(1)
\qquad(t\to\infty).
\tag{OQ11}
\]
Therefore the optimal quadratic quotient has a positive first nonlinear correction for sufficiently short fixed durations and a negative one for sufficiently long fixed durations. These are limits of the extracted coefficient. The remainder is uniform on fixed compact intervals inside \((0,\infty)\); no joint limit of duration with \(h^{-1}\) follows.

## Quadratic optimization cannot supply the missing odd correction

Let \(\phi=\phi_{00}\), let \(\eta_1\) be the first correction to the actual first-excitation vector, and let \(f=\phi/\Omega\). The exact leakage from [[four-face-cubic-response-and-source-leakage|FC]] is
\[
\ell=f\psi_1-\eta_1
=\left(\frac{\sqrt3}{42}Y_0\cdot(Y_1\times Y_2)
+\frac{\sqrt3}{12}Y_0\cdot(Y_1\times Y_3)\right)\Omega .
\tag{OQ12}
\]
The normalized source vector at the optimum still has first correction \(f\psi_1\), because its coefficient matrix moves only by \(O(h^2)\). With the sign chosen to approach \(\phi\), and \(P_{1,h}\) the actual first-excitation projection, this gives
\[
\boxed{
\|(I-P_{1,h})\zeta_{B_{\rm opt},h}\|^2
=h^2\left(\frac{2\sqrt2}{49}+\frac{\sqrt3}{2}\right)+o_t(h^2).}
\tag{OQ13}
\]
The source is exactly centered against the moving vacuum, so the displayed escaped weight has no vacuum component.

Even an imposed order-\(h\) change \(B_*+hC\) would add an even leading quadratic vector. It cannot cancel the odd vector \(\ell\). Its contribution to the second quotient coefficient is instead
\[
\frac{(A_0-r_cD_0)[C,C]}{D_0[B_*,B_*]}\ge0,
\]
strictly positive for a nonzero transverse direction. This also explains directly why the optimum has no transverse order-\(h\) displacement.

The bounded oriented source in [[four-face-oriented-source-and-the-gap-following-probe|OS2]] adds precisely the odd cubic jets needed to cancel (OQ12). It belongs to a larger physical comparison space than the ten quadratics. The distinction is therefore observable within one fixed Hamiltonian: completing the quadratic pairing range does not complete the physical source algebra. The present theorem concerns only this fixed four-face variational problem and its confinement expansion; it supplies no spatially uniform or continuum Yang–Mills gap.
