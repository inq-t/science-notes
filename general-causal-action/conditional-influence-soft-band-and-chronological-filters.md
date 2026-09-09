# The Conditional Influence Has an Actual Soft Band and Explicit Chronological Filters

For a face in the central portion of a growing planar patch, the actual conditional-cumulant influence has at least \(c(L+1)^{-4}\) spectral weight in an energy band of width \(O((L+1)^{-1})\). A normalized filter formed from the original chronological semigroup then has an innovation quotient of order \((L+1)^{-1}\). Both its norm and innovation denominator have explicit polynomial lower bounds. This constructs the soft witnesses in the actual compact theory, without inferring them from weak convergence of spectral measures.

**Status: proved actual soft-band weight and filtered-source bounds for the fixed three-block \(SU(2)\) family.** Use [[uniform-weighted-character-return-and-the-soft-gap|UW's]] confinement window, [[conditional-influence-vectors-and-the-original-source-carrier|IV's]] complete influence vector, and [[centered-compact-chronology-and-integrable-source-return|CC's]] centered generator comparison. The innovation duration in the construction is fixed in scaled units. The physical-time distinction is given below.

## A fourth-Hermite harmonic witness

Put \(n=L+1\), \(0<h n^{10}\le\eta_I\), and fix the preparation parameter in a compact interval \(I\subset(-1/14,1/16)\). Let
\[
K=\widehat H_{\varepsilon,L,h}-\lambda_{\varepsilon,L,h},\qquad
Q=1-|v\rangle\langle v|,\qquad
K|_{\operatorname{ran}Q}\ge c_I/n .
\]
All vectors are in the full physical Gauss carrier. Write \(f_h\) for IV1's centered actual conditional influence, retaining the original bounded mark and every exterior face. Its harmonic comparison is
\[
f_0=\mathcal H_{4,\sigma}(\eta)\Omega_L,\qquad
\mathcal H_{4,\sigma}(x)=|x|^4-10\sigma|x|^2+15\sigma^2,
\]
\[
\eta=\sigma(C_L^{-1}X)_r,\qquad
C_L=\sqrt{4I-\operatorname{Adj}_L},\qquad
\sigma=((C_L^{-1})_{rr})^{-1}.
\tag{SF1}
\]
Killed-kernel comparison from [[character-memory-in-the-local-conditional-fourth-cumulant|LCM]] gives
\((C_L^{-1})_{rr}\le(C_\infty^{-1})_{00}\), hence
\(\sigma\ge\sigma_\infty>0\), uniformly in \(L,r\).
Also \(\sigma\le2\).

Choose the explicit central face
\[
r_L=(\lfloor n/2\rfloor,\lfloor n/2\rfloor).
\]
The normalized lowest sine mode and its frequency are
\[
s_L(i,j)=\frac2n\sin\frac{\pi i}{n}\sin\frac{\pi j}{n},
\qquad
\omega_L=2\sqrt2\sin\frac{\pi}{2n}.
\]
For this face, \(s_L(r_L)\ge3/(2n)\), including \(n=2\). Define the three-color mode \(Y=\sum_p s_L(p)X_p\), of covariance \(\omega_LI_3\), and
\[
\boxed{
\chi_L=\frac{\mathcal H_{4,\omega_L}(Y)}
{\sqrt{120}\,\omega_L^2}\Omega_L,\qquad
\|\chi_L\|=1,\qquad
K_0\chi_L=4\omega_L\chi_L.}
\tag{SF2}
\]
It is an invariant fourth-Hermite vector. No simplicity or isolation of its harmonic eigenvalue is required.

The component covariance between \(\eta\) and \(Y\) is
\(\sigma s_L(r_L)\). Wick contraction therefore gives the exact overlap
\[
\boxed{
\langle f_0,\chi_L\rangle
=\frac{\sqrt{120}\,\sigma^4s_L(r_L)^4}{\omega_L^2}
\ge c\,n^{-2}.}
\tag{SF3}
\]
Indeed \(\omega_L^2\le2\pi^2/n^2\) and \(\sigma\ge\sigma_\infty\). The same estimate holds for any placement satisfying \(s_L(r_L)\ge c_*/n\), with constants depending on \(c_*>0\). It is not claimed for every face whose boundary distance merely tends to infinity.

## Return the low-energy weight without isolating a spectral cluster

Let \(\mathcal I=Q\mathcal JQ_0\) be CC's centered cutoff embedding. Put \(\theta=hn^{11/2}\). Its generator and Gram estimates, together with IV, give
\[
\begin{gathered}
\|(K-4\omega_L)\mathcal I\chi_L\|
\le C_Ihn^{9/2},\qquad
\|f_h-\mathcal If_0\|\le C_I\theta,\qquad
\|f_h\|\le C_I,\\
|\langle\mathcal If_0,\mathcal I\chi_L\rangle
-\langle f_0,\chi_L\rangle|\le C_I\theta^2.
\end{gathered}
\tag{SF4}
\]
The smaller cutoff Gram term is included in the last bound on this window.

Use the actual spectral projection
\[
P_{\rm lo}=\mathbf1_{(0,20/n]}(K).
\]
Since \(4\omega_L\le4\sqrt2\pi/n<20/n\), the spectral theorem and exact actual centering imply
\[
\|(1-P_{\rm lo})\mathcal I\chi_L\|
\le\frac{n}{20-4\sqrt2\pi}
\|(K-4\omega_L)\mathcal I\chi_L\|
\le C_I\theta.
\]
There need not be a spectral gap at \(20/n\). The estimate only uses the distance from the trial energy to the part above the cutoff.

Subtract this high-energy component in the pairing with \(f_h\). Since \(\mathcal I\) is a contraction, SF3–4 imply
\[
\|P_{\rm lo}f_h\|
\ge|\langle P_{\rm lo}f_h,\mathcal I\chi_L\rangle|
\ge c n^{-2}-C_I\theta.
\]
After reducing the fixed upper window bound \(\eta_I\), if necessary, the last error is at most half the first term for all \(n\ge2\). Thus
\[
\boxed{\|P_{\rm lo}f_h\|^2\ge c_I n^{-4}.}
\tag{SF5}
\]
This is spectral weight of the actual source under the actual Hamiltonian. It does not use a weak-measure limit or identify the lowest eigenvalue in the influence's cyclic sector.

## Filter the original source and retain its denominator

Fix a scaled innovation duration \(a>0\), and set
\[
R_a=1-e^{-2aK},\qquad
z_T=e^{-TK}f_h,\qquad
u_T=z_T/\|z_T\| .
\]
SF5 makes \(z_T\ne0\) for every finite \(T\). All filters use the original chronological semigroup and remain centered. In its stationary ground transform, the filtered observable is the evolution of the same bounded influence observable; normalization changes its size, not its source carrier.

Let \(d_h(s)=\langle f_h,e^{-sK}f_h\rangle\). The normalized quotient is exactly
\[
\boxed{
q_T(a)=
\frac{\langle u_T,R_a^2u_T\rangle}
{\langle u_T,R_au_T\rangle}
=\frac{d_h(2T)-2d_h(2T+2a)+d_h(2T+4a)}
{d_h(2T)-d_h(2T+2a)}.}
\tag{SF6}
\]
The denominator below is controlled directly, rather than by subtracting approximations to its three time arguments.

Let \(\mu_h\) be the spectral measure of \(f_h\), so
\(\mu_h((0,20/n])\ge c_In^{-4}\) and \(\mu_h(\mathbb R)\le C_I\).
For \(r_a(\lambda)=1-e^{-2a\lambda}\), the actual gap gives
\[
r_a(\lambda)\ge1-e^{-2ac_I/n}
\ge\frac{1-e^{-2ac_I}}n
\quad\text{on the support of }\mu_h.
\]
Consequently, with constants allowed to depend on \(a\),
\[
\boxed{\begin{aligned}
\|z_T\|^2
&\ge c_In^{-4}e^{-40T/n},\\
D_T:=\langle z_T,R_az_T\rangle
&\ge c_{I,a}n^{-5}e^{-40T/n}.
\end{aligned}}
\tag{SF7}
\]
The second inequality uses concavity of \(1-e^{-x}\). It retains both the source weight and the shrinking innovation factor.

Split the numerator at \(24/n\). Below that cutoff,
\(r_a(\lambda)^2\le r_a(24/n)r_a(\lambda)\).
Above it, \(r_a^2\le1\), so the contribution is at most
\(C_Ie^{-48T/n}\). Dividing by SF7 proves
\[
\boxed{
q_T(a)\le r_a(24/n)+C_{I,a}n^5e^{-8T/n}.}
\tag{SF8}
\]

Take the explicit actual filter time
\[
\boxed{T_n=\tfrac34 n\log n.}
\]
Then
\[
\boxed{
\|z_{T_n}\|^2\ge c_In^{-34},\qquad
D_{T_n}\ge c_{I,a}n^{-35},\qquad
q_{T_n}(a)\le\frac{48a+C_{I,a}}n.}
\tag{SF9}
\]
Since \(\|z_{T_n}\|^2\le C_I\), even the normalized innovation denominator is bounded below by \(c'_{I,a}n^{-35}\). Thus these are explicitly defined normalized returned vectors, with a nonzero denominator at every regulator.

## The actual cyclic floor has the same order

Let \(\mathcal C_h\) be the closed span of \(\{e^{-tK}f_h:t\ge0\}\), the [[two-slice-innovation-geometry/chronological-cyclic-sources-and-the-innovation-floor|chronological cyclic carrier]], and take the infimum of the innovation quotient over its nonzero vectors. This subspace is centered and contains every \(u_{T_n}\). The physical-gap lower bound gives \(R_a^2\ge r_a(c_I/n)R_a\) on the entire physical vacuum complement. Combining it with SF9 yields
\[
\boxed{
\frac{c_{I,a}}n
\le
\inf_{0\ne u\in\mathcal C_h}
\frac{\langle u,R_a^2u\rangle}{\langle u,R_au\rangle}
\le\frac{C_{I,a}}n.}
\tag{SF10}
\]
The explicit heat-filter family has the same two-sided order. A single influence source therefore generates soft chronological tests on these growing patches, even though its unfiltered susceptibility can have a finite bulk limit. The exact bottom of its actual cyclic spectrum remains unspecified.

This statement uses fixed scaled \(a\). At fixed physical duration \(\ell>0\), the scaled duration is \(a=E\ell\), with \(E=\kappa h^{-2}\). The same original gap gives, for every nonzero centered physical vector,
\[
1-\exp\!\left(-\frac{2c_I\kappa\ell}{h^2n}\right)
\le q(E\ell)\le1.
\]
On \(hn^{10}\le\eta_I\), the lower bound tends to one. Meanwhile the physical duration of the filter itself obeys
\[
T_n/E
\le\frac{3\eta_I^2}{4\kappa}\,n^{-19}\log n
\longrightarrow0.
\]
No clock has been changed: these are different duration scalings on the same rapidly confining family. The construction supplies neither a counterexample to fixed-physical-duration OI nor a fixed-coupling thermodynamic or four-dimensional limit.
