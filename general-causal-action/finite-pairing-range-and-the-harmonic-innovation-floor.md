# Finite Pairing Range Forces a Harmonic Innovation Floor

Every neutral quadratic source with pairing range at most \(R\) has a positive full-innovation floor, uniformly in the size of the planar patch and in its signed coefficients. The optimal range-restricted OI quotient is comparable to \(\min\{1,t/(R+1)\}\). The proof bounds the source's actual covariance-weighted low-frequency mass; it does not assume that banded quadratic sources form an invariant dynamical subspace. Soft quadratic response therefore requires pairings across increasing distances.

**Status: proved sharp-order range and duration bounds in the harmonic quadratic carrier.** [[additive-neutral-sources-and-the-pairing-range-test|AR1–5]] defines the source and quotient, [[lattice-poisson-tails-and-collar-localization|LP]] supplies the killed-walk comparison, and [[planar-patch-confinement-and-the-spatial-soft-mode|PP]] supplies the full physical harmonic spectrum. The same common Gauss color frame, inherited covariance and chronological time are retained.

## The source spectrum carries two covariance weights

On an open \(L\times L\) face box \(\Lambda\), let
\[
A=4I-\operatorname{Adj}_\Lambda,\qquad C=\sqrt A,\qquad
F_B=\sum_{\alpha=1}^3X_\alpha^{\mathsf T}BX_\alpha
       -3\operatorname{Tr}(BC),
\]
where the colors have independent Gaussian laws with face covariance \(C\), and \(B=B^{\mathsf T}\ne0\) is real. Assume
\[
B_{pq}=0\quad\text{when }|p-q|_\infty>R,\qquad
R\in\{0,1,2,\ldots\}.
\tag{PR1}
\]
All these sources are invariant under the common color rotation. Their covariance and mean are those of the full containing patch. The complete based transport words remain part of each observable; \(R\) measures the separation of its face labels in this fixed comb chart.

In a real orthonormal eigenbasis of \(C\), with frequencies \(\omega_i>0\), write \(\widetilde B\) for the matrix of \(B\). Set
\[
D_B=\operatorname{Tr}(BCBC)
=\|C^{1/2}BC^{1/2}\|_{\mathrm{HS}}^2
=\sum_{i,j}\omega_i\omega_j|\widetilde B_{ij}|^2>0.
\]
AR's mixed Gaussian formula gives the exact normalized spectral measure
\[
\boxed{
\nu_B=\frac1{D_B}\sum_{i,j}
\omega_i\omega_j|\widetilde B_{ij}|^2
\,\delta_{\omega_i+\omega_j},\qquad
\|F_B\|^2=6D_B.}
\tag{PR2}
\]
Thus the relevant mass is weighted by both frequencies. A bound only on the unweighted matrix entries would not suffice.

## A local support bound controls the low-frequency projector

For \(u>0\), the killed-walk comparison and positive subordination in LP give
\[
(e^{-uC})_{pp}\le
\int_{[-\pi,\pi]^2}e^{-u\omega(k)}\frac{d^2k}{(2\pi)^2},
\qquad
\omega(k)=\sqrt{4-2\cos k_1-2\cos k_2}.
\]
Since \(\omega(k)\ge2|k|/\pi\) on this square, extending the radial integral to the plane proves the explicit bound
\[
\boxed{(e^{-uC})_{pp}\le\frac{\pi}{8u^2}.}
\tag{PR3}
\]
The comparison includes boundary killing, so its constant is independent of the box and the site.

For \(\delta>0\), let \(E_\delta=1_{[0,\delta]}(C)\). Scalar functional calculus gives
\(E_\delta\le e\,e^{-C/\delta}\), hence
\[
(E_\delta)_{pp}\le K\delta^2,\qquad K=\frac{\pi e}{8}.
\]
If \(b\) has support \(T\), the positive compression of \(E_\delta\) to \(T\) has norm at most its trace. Therefore
\[
\|E_\delta b\|^2
=\langle b,E_\delta b\rangle
\le K\delta^2|T|\,\|b\|^2.
\]
Every column and row of \(B\) has at most \(N_R=(2R+1)^2\) nonzero entries, giving
\[
\boxed{
\|E_\delta B\|_{\mathrm{HS}}^2,\quad
\|BE_\delta\|_{\mathrm{HS}}^2
\le K N_R\delta^2\|B\|_{\mathrm{HS}}^2.}
\tag{PR4}
\]
No sign constraint on the entries is used.

## The weighted low-low block cannot dominate

Choose
\[
\boxed{\delta_R=\frac1{\sqrt{\pi e}(2R+1)},\qquad
E=E_{\delta_R},\quad J=I-E.}
\tag{PR5}
\]
Then \(KN_R\delta_R^2=1/8\). The four row/column spectral blocks are orthogonal in Hilbert–Schmidt norm, so
\[
\|JBJ\|_{\mathrm{HS}}^2
\ge\|B\|_{\mathrm{HS}}^2-\|EB\|_{\mathrm{HS}}^2
                         -\|BE\|_{\mathrm{HS}}^2
\ge\frac34\|B\|_{\mathrm{HS}}^2.
\]
Because \(C\) commutes with \(E,J\), the blocks remain orthogonal after multiplication by \(C^{1/2}\) on both sides. The high-high block then gives
\[
D_B\ge\delta_R^2\|JBJ\|_{\mathrm{HS}}^2
\ge\frac34\delta_R^2\|B\|_{\mathrm{HS}}^2.
\]
The low-low block instead satisfies
\[
D_{\mathrm{low}}
:=\|C^{1/2}EBEC^{1/2}\|_{\mathrm{HS}}^2
\le\delta_R^2\|EBE\|_{\mathrm{HS}}^2
\le\frac18\delta_R^2\|B\|_{\mathrm{HS}}^2.
\]
Consequently
\[
\boxed{\frac{D_{\mathrm{low}}}{D_B}\le\frac16,\qquad
\nu_B([\delta_R,\infty))\ge\frac56.}
\tag{PR6}
\]
Outside the low-low block at least one frequency exceeds \(\delta_R\), so their sum exceeds it. Any additional low-low mass above that threshold only strengthens the last inequality.

## Full innovation and OI retain the range floor

Let \(P_t=e^{-tK_0}\) be the full harmonic ground-transformed chronology. The original full-predictor innovation is
\[
G_B(t)=\|F_B\|^2-\langle F_B,P_{2t}F_B\rangle
=\|\delta_tF_B\|^2.
\]
With \(r_t(\lambda)=1-e^{-2t\lambda}\), equations (PR2), (PR6) imply
\[
\boxed{
\frac{G_B(t)}{\|F_B\|^2}
=\int r_t\,d\nu_B
\ge\frac56(1-e^{-2t\delta_R}),\qquad t>0.}
\tag{PR7}
\]
The unchanged OI quotient has numerator
\(\langle F_B,(I-P_{2t})^2F_B\rangle\). Cauchy–Schwarz in the probability measure \(\nu_B\) gives
\[
\boxed{
\mathfrak q_t(F_B)
=\frac{\int r_t^2\,d\nu_B}{\int r_t\,d\nu_B}
\ge\int r_t\,d\nu_B
\ge\frac56(1-e^{-2t\delta_R}).}
\tag{PR8}
\]
The denominator is strictly positive for every admitted nonzero source. These are spectral-measure estimates on its complete evolution, not a restriction of the generator to the banded source subspace.

## The lowest mode supplies the matching range scale

For the infimum \(c_R(t)\) in AR5, choose \(L=R+1\). Every pair in that box is permitted by (PR1). Let \(v_{\min}\) be the normalized lowest spatial mode and \(B=v_{\min}v_{\min}^{\mathsf T}\). Its centered quadratic is the physical two-quantum scalar of energy
\[
2\sqrt{\lambda_{\min}(A)}
=4\sqrt2\sin\frac{\pi}{2(R+2)}.
\]
Its spectral measure is a point mass, so together with (PR8),
\[
\boxed{
\frac56\left(1-e^{-2t/[\sqrt{\pi e}(2R+1)]}\right)
\le c_R(t)
\le1-e^{-8\sqrt2\,t\sin[\pi/(2(R+2))]}.}
\tag{PR9}
\]
In particular universal positive constants \(c_*,C_*\) satisfy
\[
\boxed{
c_*\min\!\left\{1,\frac{t}{R+1}\right\}
\le c_R(t)\le
C_*\min\!\left\{1,\frac{t}{R+1}\right\},
\qquad t>0,\ R\ge0.}
\tag{PR10}
\]
For example one may take
\(c_*=\frac56(1-e^{-1/\sqrt{\pi e}})\) and \(C_*=4\sqrt2\pi\).
Use \(2R+1\le2(R+1)\), \(\sin x\le x\), and the elementary chord bounds for \(1-e^{-x}\). At \(R=0\), AR4 supplies a stronger constant than this uniform-range proof.

The upper witness in (PR9) uses the actual vacuum of its chosen containing box; it does not identify a regional vacuum inside a larger patch with that box's independent vacuum. [[localized-relational-sources-in-the-inherited-vacuum|The localized relational source]] supplies a complementary upper witness in an inherited larger vacuum.

The theorem covers arbitrary signed symmetric pairing matrices and arbitrarily many faces in the harmonic quadratic source carrier. It proves that fixed pairing range cannot approach the known soft quadratic response at fixed duration. [[compact-quadratic-carrier-and-the-pairing-range-return|The separate compact quadratic return]] transfers this declared source carrier with its actual normalization and explicit range-dependent denominator errors. Higher-degree regional observables and the four-dimensional physical mass gap remain outside these results. The original global/local source and chronological constraints remain those of [[regional-innovation-and-exterior-information-balance|RI]] and [[spatial-block-sewing-and-the-vacuum-cap-response|SB]].
