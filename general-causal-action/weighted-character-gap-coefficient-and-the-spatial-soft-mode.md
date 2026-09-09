# The Character-Dependent Gap Coefficient Follows the Spatial Soft Mode

The preparation contrast that changes the four-face gap also has an exact coefficient on every open square patch. Its magnitude decreases as \(1/(L+1)\), at the same rate as the harmonic physical gap. Their ratio tends to a nonzero constant fixed by the bulk lattice covariance. The nonlinear character data remain observable, but this contrast contributes no size-independent scaled energy at second order. Turning these coefficient statements into a simultaneous compact and spatial limit requires a separate uniform remainder.

**Status: exact coefficient and spatial asymptotic, with actual return at each fixed patch.** [[equal-character-hessians-and-the-nonlinear-source-discriminator|EH]] fixes the \(SU(2)\) representation, positive weight family and common scale. [[planar-patch-confinement-and-the-spatial-soft-mode|PP]] fixes the full Gauss carrier and soft mode. The full preparation weight changes; its trace, character Hessian and complete first-order data remain fixed.

## The same preparation contrast on every patch

Use EH's fixed representation
\(\rho=\rho_{1/2}\oplus\rho_1\oplus\rho_{3/2}\) and
\[
A_\varepsilon=(1+14\varepsilon)I_2
\oplus(1-16\varepsilon)I_3
\oplus(1+5\varepsilon)I_4,\qquad
-1/14<\varepsilon<1/16.
\]
On the open \(L\times L\) face patch, gauge every vertex and retain the actual based face words. Put
\[
H_{\varepsilon,L}
=\kappa\mathsf C_{\mathrm{raw},Q}
+g\sum_p W_{A_\varepsilon}(P_p),\qquad
h=(\kappa/(15g))^{1/4},\quad E=\kappa/h^2.
\tag{WS1}
\]
The electric operator and scale are common to the family. Write
\(\Delta_{\varepsilon,L}(h)\) for the first physical gap of \(H_{\varepsilon,L}/E\).
In the face chart \(P_p=e^{hX_p}\), EH's exact character moments give
\[
\partial_\varepsilon(H_{\varepsilon,L}/E)
=-\frac7{120}h^2\sum_p|X_p|^4+O_L(h^4)
\tag{WS2}
\]
as a local weighted operator jet. This is not a global operator-norm expansion.

Let \(n=L+1\), \(A_L=4I-\operatorname{Adj}_L\), and \(C_L=\sqrt{A_L}\). The normalized lowest sine mode and its frequency are
\[
u(i,j)=\frac2n\sin\frac{\pi i}{n}\sin\frac{\pi j}{n},
\qquad
\omega_L=2\sqrt2\sin\frac{\pi}{2n}.
\tag{WS3}
\]
For \(Y=\sum_pu(p)X_p\), the normalized first physical harmonic state is
\[
\phi_L=\frac{|Y|^2-3\omega_L}{\sqrt6\,\omega_L}\Omega_L.
\]
Its energy above the vacuum is \(2\omega_L\). The lowest spatial mode and its invariant quadratic are unique; no invariant one-quantum state lies below it.

## The vacuum-subtracted quartic moment

Write \(c_p=(C_L)_{pp}\) and
\[
S_L=\sum_pu(p)^2c_p,\qquad I_L=\sum_pu(p)^4.
\]
The Gaussian decomposition \(X_p=u(p)Y+\eta_p\) has \(\eta_p\) independent of \(Y\), with component variance \(c_p-u(p)^2\omega_L\). No independence between distinct residual faces is assumed.

For \(R=|Y|^2\), the scalar two-quantum state in \(d\) colors has
\[
\langle R\rangle_\phi-\langle R\rangle_\Omega=4\omega_L,\qquad
\langle R^2\rangle_\phi-\langle R^2\rangle_\Omega
=12(d+2)\omega_L^2.
\]
Expanding the conditional Gaussian fourth moment therefore gives
\[
\begin{aligned}
\langle |X_p|^4\rangle_\phi-\langle |X_p|^4\rangle_\Omega
&=(d+2)\bigl[8u(p)^2c_p\omega_L
+4u(p)^4\omega_L^2\bigr].
\end{aligned}
\]
At \(d=3\), summing over faces and applying WS2 proves the exact coefficient
\[
\boxed{
k_L=-\frac76\,\omega_L(2S_L+\omega_L I_L)<0.}
\tag{WS4}
\]

For each fixed \(L\), the actual simple vacuum and first physical level return to \(\Omega_L,\phi_L\). The weighted quasimode and Feynman–Hellmann proof used in EH applies uniformly on every compact parameter interval \(J\subset(-1/14,1/16)\): positivity of the cost and its unique well are uniform there. It yields
\[
\boxed{
\Delta_{\varepsilon_2,L}(h)-\Delta_{\varepsilon_1,L}(h)
=(\varepsilon_2-\varepsilon_1)h^2k_L
+O_{L,J}(|\varepsilon_2-\varepsilon_1|h^3).}
\tag{WS5}
\]
Arbitrarily accurate eigenvector quasimodes are taken before multiplying the globally growing compact perturbation. The unknown common second-order gap contribution cancels in this parameter difference. WS5 alone gives no bound uniform in \(L\).

For \(L=1\), \(\omega_1=c_1=2\), \(S_1=2\), \(I_1=1\), so \(k_1=-14\). For \(L=2\), \(u(p)=1/2\),
\[
S_2=\frac{4+\sqrt2+\sqrt6}{4},\qquad I_2=\frac14,
\]
and
\[
\boxed{k_2=-\frac7{24}(8\sqrt2+6+4\sqrt3),}
\tag{WS6}
\]
exactly EH14.

## The weighted diagonal is an explicit bulk quadrature

For \(n\ge3\), the elementary sine sums give
\[
\sum_{i=1}^{n-1}\sin^4\frac{\pi i}{n}=\frac{3n}{8},
\qquad
\boxed{I_L=\frac9{4n^2}.}
\tag{WS7}
\]
To compute \(S_L\), insert the complete sine spectral resolution of \(C_L\). The one-dimensional overlaps are
\[
w_r=\frac4{n^2}\sum_{i=1}^{n-1}
\sin^2\frac{\pi i}{n}\sin^2\frac{r\pi i}{n}
=
\begin{cases}
3/(2n),&r=1\text{ or }r=n-1,\\
1/n,&2\le r\le n-2.
\end{cases}
\]
These identities follow by expanding into cosines and using
\(\sum_{i=1}^{n-1}\cos(2k\pi i/n)=-1\) unless \(n\) divides \(k\).
Consequently
\[
\boxed{
S_L=\sum_{r,s=1}^{n-1}w_rw_s\,
\varpi(r\pi/n,s\pi/n),\qquad
\varpi(x,y)=\sqrt{4-2\cos x-2\cos y}.}
\tag{WS8}
\]
The weights sum to one. This is the mode-weighted diagonal of the containing patch covariance, not the covariance of an independently prepared block.

Define
\[
c_\infty=\frac1{\pi^2}\int_0^\pi\int_0^\pi
\varpi(x,y)\,dx\,dy.
\]
The dispersion is \(1\)-Lipschitz, since
\(\varpi(x,y)=2|(\sin(x/2),\sin(y/2))|\).
The weights \(w_r\) are exactly the uniform masses of a partition with first cell \([0,3\pi/(2n)]\), last cell \([(n-3/2)\pi/n,\pi]\), and the usual centered cells between them. Every point of a cell is within \(\pi/n\) of its assigned node \(r\pi/n\). Coupling the product uniform measure to these nodes therefore proves
\[
\boxed{|S_L-c_\infty|\le\frac{\sqrt2\pi}{n},\qquad n\ge3.}
\tag{WS9}
\]
This proves the required bulk limit directly, including the boundary weighting of the lowest sine mode.

## Compare with the harmonic physical gap

Since \(\omega_L=\sqrt2\pi/n+O(n^{-3})\), WS4 and WS7–9 give
\[
\boxed{
k_L=-\frac{7\sqrt2\pi c_\infty}{3n}+O(n^{-2}),\qquad
\frac{k_L}{2\omega_L}
=-\frac76c_\infty+O(n^{-1}).}
\tag{WS10}
\]
The term involving \(I_L\) contributes only \(O(n^{-4})\) to \(k_L\).

There are also size-independent coefficient bounds. The spectral inequality
\(\sqrt{A_L}\ge A_L/\sqrt8\) and diagonal Cauchy–Schwarz give
\(\sqrt2\le c_p\le2\). Thus \(\sqrt2\le S_L\le2\); moreover
\(\omega_L I_L\le2\). Hence, for every \(L\ge1\),
\[
\boxed{
\frac{7\sqrt2}{6}
\le-\frac{k_L}{2\omega_L}\le\frac72.}
\tag{WS11}
\]
The bulk constant satisfies \(\sqrt2<c_\infty<2\).

For fixed distinct preparation parameters, the sequential limit is therefore
\[
\boxed{
\lim_{L\to\infty}\lim_{h\to0}
\frac{\Delta_{\varepsilon_2,L}(h)-\Delta_{\varepsilon_1,L}(h)}
{(\varepsilon_2-\varepsilon_1)h^2(2\omega_L)}
=-\frac76c_\infty.}
\tag{WS12}
\]
The character contrast scales with the harmonic closing rather than adding a nonzero scaled edge. This does not determine the complete second-order gap coefficient or a fixed-coupling thermodynamic limit. [[uniform-weighted-character-return-and-the-soft-gap|The weighted-family return]] now proves the required simultaneous comparison: its parameter-contrast remainder is \(O_I(|\varepsilon_2-\varepsilon_1|h^4n^{13})\), resolving WS12 throughout \(hn^{10}\le\eta_I\). That theorem separately accounts for the common physical scale and the actual absolute contrast. [[character-response-and-the-bulk-vacuum-normalization|The same character tangent]] also fixes an extensive vacuum response. The four-dimensional and complete-source physical-limit obligations remain unchanged.
