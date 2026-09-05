# Accumulated Readout Noise Has a Local Covariance

In the regular soft Gaussian gauge chain, all added readout noise admits an exact nearest-neighbor covariance on the final unprojected bond carrier, at every blocking depth. Intermediate gauge projections cancel after the final quotient projection. The actual potential covariance can still be nonlocal, and its transverse inverse must be taken on the correct carrier. This isolates the inherited massless Maxwell covariance, rather than spreading of the added noise, as the remaining source of difficulty in Gaussian localization.

## The operator acts on retained bond potentials

Use [[soft-gaussian-gauge-blocking|the normalized soft chain]] with factor \(L\ge2\), meshes \(b_i=L^ia\), and physical \(L^2\) metrics. Write \(Q_n\) for the raw parallel-path average through factor \(n\), and \(\Pi_i\) for projection onto the harmonic-free Coulomb space \(H_i\). The chain map is \(\mathsf Q_i=\Pi_{i+1}Q_L|_{H_i}\).

Gradients map to gradients, and spatial means are preserved. Therefore

$$
\Pi_kQ_n\Pi_i=\Pi_kQ_n,\qquad
T_{i:k}=\Pi_kQ_{L^{k-i}}|_{H_i},
\tag{AN1}
$$

where \(T_{i:k}\) is the actual composite quotient map. The equality uses aligned blocks and \(Q_mQ_n=Q_{mn}\), not an assumption that Coulomb projections are local. It implies
\(T_{i:k}T_{i:k}^*=\Pi_kQ_{L^{k-i}}Q_{L^{k-i}}^*\Pi_k|_{H_k}\).

## Exact overlap counting

Let \(S_\mu\) shift one final coarse cell in direction \(\mu\). The physical adjoint of the average satisfies the componentwise identity

$$
\boxed{
(Q_nQ_n^*)_\mu
=\frac{2+n^{-2}}3I+
\frac{1-n^{-2}}6(S_\mu+S_\mu^*).}
\tag{AN2}
$$

There are no cross-component terms. To derive it, the longitudinal kernel in the fine lattice is the triangular weight

$$
t_n(r)=n^{-2}\#\{(x,j):0\le x,j<n,\ x+j=r\}.
$$

Only coarse shifts \(0,\pm1\) overlap. Summing the triangular squares and adjacent overlaps gives

$$
n\sum_rt_n(r)^2=\frac{2+n^{-2}}3,\qquad
n\sum_rt_n(r)t_n(r-n)=\frac{1-n^{-2}}6.
$$

The other \(d-1\) directions have disjoint uniform cell averages; their factors cancel against the physical adjoint normalization. Thus (AN2) is dimension-independent. It also holds at \(n=1\); periodic shifts are understood with multiplicity on short tori.

## The whole accumulated noise

At final mesh \(b=b_k\), define

$$
U_k=\frac{1-L^{-2k}}{1-L^{-2}},\qquad
V_k=\frac{1-L^{-4k}}{1-L^{-4}}.
$$

The noise term in the actual covariance (SG4) is \(N_k=\Pi_k\widetilde N_k\Pi_k|_{H_k}\), where

$$
\boxed{
\widetilde N_{k,\mu}
=\eta b^2\left[
\frac{2U_k+V_k}{3}I+
\frac{U_k-V_k}{6}(S_\mu+S_\mu^*)\right].}
\tag{AN3}
$$

Indeed each upstream contribution has weight \(\eta b^2L^{-2j}\) and average factor \(n=L^j\), for \(j=0,\ldots,k-1\). Formula (AN2) sums those two geometric series exactly. The symbol is

$$
\widetilde N_{k,\mu}(p)
=\eta b^2\left[U_k-\frac23(U_k-V_k)\sin^2(p_\mu/2)\right].
\tag{AN4}
$$

For \(k\ge1\),

$$
\eta b^2I
\le \eta b^2\frac{U_k+2V_k}{3}I
\le\widetilde N_k
\le\eta b^2U_kI
\le\frac{\eta b^2}{1-L^{-2}}I.
\tag{AN5}
$$

At fixed final \(b\), letting the initial cutoff recede gives a norm-convergent nearest-neighbor covariance: replace \(U_k,V_k\) by their infinite sums. The error is at most \(\eta b^2L^{-2k}/(1-L^{-2})\). This is a noise-only ultraviolet limit, not continuum Yang--Mills existence.

The raw positive \(\widetilde N_k\) has a uniformly exponentially decaying inverse by the finite-range inverse expansion in [[local-completion-of-soft-gauge-conditioning|the one-step completion]]. But this inverse is **not** the inverse of the compressed covariance \(N_k\). Even at \(k=1\), the full-matrix presentation of \(N_1=\eta b_1^2\Pi_1\) is generally nonlocal.

Curl \(\mathcal C_k\) kills both gradients and harmonic one-forms. Thus

$$
\mathcal C_kN_k\mathcal C_k^*
=\mathcal C_k\widetilde N_k\mathcal C_k^*.
\tag{AN6}
$$

The noise contribution to curvature covariance is finite-range too. At \(k\ge2\) it is not obtained by repeatedly adding one scalar white covariance at the final scale; the directional neighbor term is nonzero.

## The remaining covariance and the correct inverse

The [[endpoint-averages-and-quadratic-ultraviolet-control|Fourier alias convention (EA8d)]] gives a complete finite-depth expression. Put \(n=L^k\), \(q_\ell=(p+2\pi\ell)/n\), and \(\widehat q^2=4\sum_\nu\sin^2(q_\nu/2)\). For nonzero final momentum \(p\), define

$$
F_{k,\mu}(p)=
n^{-2}\sum_{\ell\in\{0,\ldots,n-1\}^d}
\frac{|\Omega_n(q_\ell)_{\mu\mu}|^2}{\widehat q_\ell^2}
+\eta\left[U_k-\frac23(U_k-V_k)\sin^2(p_\mu/2)\right].
\tag{AN7}
$$

Then, on the transverse space at that momentum,

$$
\operatorname{Cov}(X_k)(p)
=b^2\Pi(p)\mathcal D_k(p)\Pi(p),\qquad
\mathcal D_k(p)=\operatorname{diag}(F_{k,\mu}(p)).
\tag{AN8}
$$

The factor \(n^{-2}=a^2/b^2\) comes from the Maxwell inverse's dimension. It is not an alias-count normalization. At \(p=0\) the physical harmonic sector is removed separately; (AN7) must not be evaluated by retaining its singular zero alias.

Let \(v_\mu=e^{ip_\mu}-1\), so \(\Pi=I-v(v^*v)^{-1}v^*\). The gauge-flat extension of the actual inverse in (AN8) is

$$
\boxed{
\widehat P_k(p)=b^{-2}\left[
\mathcal D_k^{-1}
-\mathcal D_k^{-1}v
(v^*\mathcal D_k^{-1}v)^{-1}
v^*\mathcal D_k^{-1}\right].}
\tag{AN9}
$$

The bracket annihilates \(v\), has transverse range, and multiplying it by \(\Pi\mathcal D_k\Pi\) returns \(\Pi\). This verifies the inverse on the declared carrier. In general it is not \(\Pi\mathcal D_k^{-1}\Pi\): for \(\mathcal D=\operatorname{diag}(1,2)\), \(v=(1,1)\), the transverse inverse is \(2/3\), whereas inverse-then-project gives \(3/4\).

[[library/the-classically-perfect-fixed-point-action-for-su3-gauge-theory/inq|DeGrand et al., Appendix A]] supplies a closely related covariance-iteration and transverse-inversion precedent, equations (A6)--(A10) and (A14)--(A19). Their averaging kernel and field normalizations differ. Equations (AN1)--(AN9) are derived for the specific regular average here, not imported fixed-point estimates.

[[uniform-gaussian-conditional-locality|Uniform Gaussian conditional locality]] controls (AN9) in a common complex momentum strip: gradient compatibility cancels its apparent principal pole, and a summable high-alias bound is uniform in depth. Exponential precision coefficients and the [[multilevel-local-gauge-completion|terminal Schur floor]] then give a weighted inverse estimate. Real-momentum positivity alone would not suffice. This closes the declared Gaussian localization step, not the nonlinear conditional estimate or the retained infrared mass gap.
