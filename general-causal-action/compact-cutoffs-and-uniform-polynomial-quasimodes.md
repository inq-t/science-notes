# Compact Cutoffs for Uniform Polynomial Quasimodes

A fixed magnetic cutoff prescription converts finite-degree oscillator vectors into smooth vectors of the actual compact planar theory, with uniform control of tails and commutators. Its physical radius decreases only as \((L+1)^{-1/2}\); in the stated confinement window its Gaussian radius is much larger than the typical field size. Exact magnetic identities control the cutoff derivatives without differentiating the entire comb metric. Combined with the interior operator remainder, this gives an arbitrary fixed-order compact quasimode residual with explicit spatial powers.

**Status: proved uniform cutoff and residual-combination estimates.** [[comb-chart-ellipticity-and-uniform-local-comparison|UC]] supplies the exact flat rows and finite-order coefficients. [[uniform-planar-localization-and-the-first-physical-levels|UP]] supplies the global magnetic estimate. [[compact-operator-taylor-remainder-on-planar-wells|The interior operator remainder]] controls the uncut operator Taylor error. Selecting the resulting quasimode as an actual vacuum or first excitation uses the separate ordered spectral comparison in [[planar-physical-cluster-separation-and-the-uniform-window|PS]].

## One cutoff remains inside the uniform local chart

Put \(n=L+1\), \(N=L^2\), and keep
\[
\widehat H=h^2\mathsf C+h^{-2}W,\qquad
\mathsf C=\sum_{\rm raw\ edges}C_e,\qquad
W=\sum_p(2-\chi_{1/2}(P_p)),\qquad
\epsilon=hn^{10}.
\]
Fix \(0<\delta_*<(2\pi\sqrt2)^{-1}\). Choose a smooth function \(\chi_*\), with values in \([0,1]\), equal to one on \((-\infty,1]\) and zero on \([2,\infty)\). Define
\[
\delta_n=\frac{\delta_*}{\sqrt n},\qquad
\chi_{L,h}(x)=\chi_*\!\left(\frac{W(P(hx))}{\delta_n^2}\right),
\qquad
R=\frac{\delta_n}{h}=\frac{\delta_*}{h\sqrt n}.
\tag{CQ1}
\]
Here \(P_p(y)=\exp(-iy_p\cdot\sigma/2)\) are the principal comb face logarithms. The global cutoff is a function of \(W\), so it is physical and smooth independently of the chart.

UP6 gives
\[
\operatorname{supp}\chi_{L,h}
\subset\{|x|\le\pi\sqrt2R\},\qquad
\operatorname{supp}(1-\chi_{L,h})
\subset\{|x|\ge2R\}
\quad\text{within the scaled chart}.
\tag{CQ2}
\]
Extend the scaled cutoff by zero outside that chart; the second inclusion remains valid. On its support,
\[
h\sqrt L\,|x|\le\pi\sqrt2\,\delta_*\sqrt{L/n}<1 .
\]
Thus the interior operator estimates apply on the entire support. For \(0<\epsilon\le\eta_0\), a fixed sufficiently small \(\eta_0\) also makes \(R\ge1\) for all \(n\ge2\). All constants below may depend on \(\delta_*\), the fixed cutoff, degree and expansion order, but not on patch size or confinement strength.

If the actual product Haar density in the \(y\)-chart is \(\rho_L(y)\,dy\), define
\[
(\mathcal J_{L,h}u)(P(y))
=h^{-3N/2}\rho_L(y)^{-1/2}
\chi_*\!\left(W(P(y))/\delta_n^2\right)u(y/h),
\tag{CQ3}
\]
extended by zero. For an invariant polynomial-Gaussian vector this is a smooth physical compact vector. The full density normalization is retained, even when it depends on \(N\). Exactly,
\[
\|\mathcal J_{L,h}u\|^2
=\int|\chi_{L,h}u|^2\,dx .
\]
The local density transform is an isometry on supported vectors; the cutoff makes \(\mathcal J_{L,h}\) a contraction, not an isometry on the entire oscillator space.

## Polynomial moments suffice for every fixed tail order

Let \(P_{\le m,L}\) project onto total oscillator Hermite degree at most fixed \(m\), on the full colored cover. The covariance eigenvalues are bounded above by \(\sqrt8\). Creation and annihilation operators therefore give
\[
\||x|^kP_{\le m,L}\|\le C_{m,k}n^k,\qquad
\sum_i\|\partial_i u\|^2\le C_m n^3\|u\|^2 .
\tag{CQ4}
\]
For even \(k=2q\), the first estimate follows by successively multiplying by \(|x|^2=\sum_{i=1}^{3N}x_i^2\): each coordinate square is bounded on finite degree, the sum costs \(O(n^2)\), and each multiplication increases degree by at most two. The odd powers follow by Cauchy–Schwarz from even moments. Each derivative vector has degree at most \(m+1\), so the same moment argument applies after differentiation.

Consequently, for every nonnegative integer \(q\), with
\(\tau=hn^{3/2}\), one has
\[
\begin{aligned}
\|\mathbf1_{\{|x|\ge R\}}u\|
&\le C_{m,q}\tau^{2q}\|u\|,\\
\|\mathbf1_{\{|x|\ge R\}}\nabla u\|
&\le C_{m,q}n^{3/2}\tau^{2q}\|u\|,\\
\|\mathbf1_{\{|x|\ge R\}}|x|u\|
&\le C_{m,q}n\,\tau^{2q}\|u\| .
\end{aligned}
\tag{CQ5}
\]
The fixed powers of \(\delta_*^{-1}\) are included in \(C_{m,q}\).
These are dimension-dependent polynomial estimates with explicitly retained powers of \(n\). Arbitrarily high fixed moments are available; no dimension-independent Gaussian tail constant is assumed.

## The exact magnetic identities control the commutator

Each plaquette trace is a spin-\(1/2\) eigenfunction of each of its four incident edge Casimirs. Hence, on the original compact carrier,
\[
\boxed{\mathsf C W=3W-6N,\qquad \Gamma(W)\le8W,}
\tag{CQ6}
\]
where \(\Gamma(F)=\sum_{e,a}|Z_{e,a}F|^2\). The first identity is also the one used in [[weighted-compact-source-return-on-growing-patches|WS]]; the second is UP4. Applying the exact chain rule for \(\mathsf C=-\sum Z_{e,a}^2\) gives, on the cutoff transition region,
\[
h^2\Gamma(\chi_*)\le C h^2n,\qquad
|h^2\mathsf C(\chi_*)|\le C h^2n^3.
\tag{CQ7}
\]
Here \(\chi_*\) means its composed compact multiplier in (CQ1). Indeed,
\[
\mathsf C\chi_*(W/\delta_n^2)
=\frac{\chi_*'(W/\delta_n^2)}{\delta_n^2}(3W-6N)
-\frac{\chi_*''(W/\delta_n^2)}{\delta_n^4}\Gamma(W),
\]
and the derivatives are supported where
\(\delta_n^2\le W\le2\delta_n^2\).

Let \(D_{e,h}=hZ_e\) denote the derivative part after dilation, and let
\(\mathsf E_{e,h}=D_{e,h}-\tfrac12D_{e,h}\log\rho_h\)
be its exact flat-density row. Haar divergence-freeness gives
\(\widetilde H_h=-\sum_e\mathsf E_{e,h}^2+h^{-2}W\).
The product rule, including the row's zero-order term, gives the exact identity
\[
\boxed{
[\widetilde H_h,\chi]u
=(h^2\mathsf C\chi)u
-2\sum_e(D_{e,h}\chi)\,\mathsf E_{e,h}u .}
\tag{CQ8}
\]
All raw color components are included in the sum. This identity avoids a separate estimate for derivatives of the full metric.

On the support of the cutoff, UC4 and UC8 imply
\[
\left(\sum_e|\mathsf E_{e,h}u|^2\right)^{1/2}
\le C\bigl(|\nabla u|+h^2|x|\,|u|\bigr).
\]
Every coefficient in (CQ8) is supported in the tail region of (CQ5). By pointwise Cauchy–Schwarz over the raw rows, followed by (CQ5)–(CQ7),
\[
\begin{aligned}
\|[\widetilde H_h,\chi]u\|
&\le C_{m,q}
\bigl(h^2n^3+hn^2+h^3n^{3/2}\bigr)\tau^{2q}\|u\|\\
&\le\boxed{C_{m,q}hn^2\tau^{2q}\|u\|},
\qquad 0<\epsilon\le\min\{\eta_0,1\}.
\end{aligned}
\tag{CQ9}
\]
The last inequality uses \(hn\le1\). Both the derivative and half-density terms have been retained.

## Combine an interior error with a polynomial residual

For an integer \(M\ge1\), put \(T_M(h)=\sum_{r=0}^M h^rV_r\).
The interior operator theorem gives
\[
\|\mathbf1_{\{|x|\le\pi\sqrt2R\}}
(\widetilde H_h-T_M(h))P_{\le m,L}\|
\le C_{m,M}h^{M+1}n^{3(M+1)/2+4}.
\tag{CQ10}
\]
Let \(u_h,f_h\) belong to a fixed Hermite-degree space, and let \(z_h\) be a scalar. The supported density isometry and (CQ8) give
\[
\begin{aligned}
&\|(\widehat H-z_h)\mathcal J_{L,h}u_h-\mathcal J_{L,h}f_h\|\\
&\quad\le
\|(T_M(h)-z_h)u_h-f_h\|
+C_{m,M}h^{M+1}n^{3(M+1)/2+4}\|u_h\|\\
&\qquad\quad
+C_{m,q}hn^2(hn^{3/2})^{2q}\|u_h\|.
\end{aligned}
\tag{CQ11}
\]
This is also a forced-equation estimate: it does not require \(f_h=0\).
It assumes neither that \(u_h\) approximates the vacuum nor that a polynomial forcing already equals the actual centered compact source.

Choose \(q=M+1\). For \(M\ge1\),
\[
\frac32(M+1)+4\le\frac{11}{2}(M+1)-1.
\]
The commutator term is smaller than that same target throughout the stipulated window. Thus if, for a fixed exponent \(b\ge0\),
\[
\|u_h\|\le Cn^b,\qquad
\|(T_M(h)-z_h)u_h-f_h\|
\le C h^{M+1}n^{11(M+1)/2-1+b},
\]
then
\[
\boxed{
\|(\widehat H-z_h)\mathcal J_{L,h}u_h-\mathcal J_{L,h}f_h\|
\le C h^{M+1}n^{11(M+1)/2-1+b}.}
\tag{CQ12}
\]
The dependence on input size is linear. In particular a Poisson trial of norm \(O(n)\) costs exactly one additional power of \(n\) here, provided its polynomial residual obeys the correspondingly stated bound. Its forcing and centering errors must still be estimated separately.

## Formal eigenpairs give normalized compact quasimodes

Take either the harmonic vacuum or first physical scalar branch. Use the normalized formal coefficients of UC20 and set
\[
U_M(h)=\sum_{j=0}^M h^j\psi_j,\qquad
z_M(h)=e_0+\sum_{j=1}^M h^je_j,\qquad
\theta=hn^{11/2}.
\]
For each fixed \(M\), the vectors have degree at most \(d_0+3M\).
Their coefficient bounds give
\(\|U_M(h)\|\le C_M\) when \(\theta\le1\).
The formal eigen-equation cancels every power through \(M\) in
\((T_M-z_M)U_M\). Every remaining coefficient of order \(r>M\) costs at most \(C_Mn^{11r/2-1}\): for \(s\ge1\),
\[
\|V_s\psi_{r-s}\|
\le C_M n^{3s/2+3+11(r-s)/2}
\le C_M n^{11r/2-1},
\]
and \(e_s\psi_{r-s}\) has the same envelope. Only finitely many powers, through \(2M\), occur. Therefore
\[
\|(T_M-z_M)U_M\|\le C_M n^{-1}\theta^{M+1}.
\]
Formal normalization likewise gives
\(\|U_M\|^2=1+O_M(\theta^{M+1})\).
Equation (CQ5), with \(q=M+1\), bounds the cutoff loss by a smaller power. Shrinking the fixed \(\epsilon\)-window if necessary, independently of \(L\), makes the cut norm bounded away from zero. Thus
\[
\Psi_{M,L,h}
=\frac{\mathcal J_{L,h}U_M(h)}
{\|\mathcal J_{L,h}U_M(h)\|}
\]
is a normalized physical compact vector with
\[
\boxed{
\|(\widehat H-z_M)\Psi_{M,L,h}\|
\le C_M h^{M+1}n^{11(M+1)/2-1},
\qquad M\ge1.}
\tag{CQ13}
\]
The constants and allowed window may depend on the fixed order \(M\); no uniformity as \(M\to\infty\) or convergence of the formal series is asserted.

At sixth order the eigenpair residual is \(O(h^7n^{75/2})\).
The forced estimate (CQ12), for an input of norm \(O(n)\), gives
\(O(h^7n^{77/2})\) when its polynomial defect has that size.
These are residual bounds in the original compact operator and its exact Haar norm. Identifying the eigenline, replacing a forcing by the actual centered source, and obtaining a marked susceptibility remainder require the spectral and weighted-source steps in PS and WS; they do not follow from a residual alone.
