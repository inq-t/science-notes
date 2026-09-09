# Weighted Source Return Avoids the Global Multiplication Loss

The growing-patch compact source has uniform Gaussian multiplication bounds and an exact graph-norm bound on the original physical carrier. The latter replaces its crude \(L^2h^{-2}\) operator norm by one power of the actual Hamiltonian and a term proportional to \(L\). These estimates give a sufficient, quantitative transfer from a selected ground-state quasimode to the actual centered and normalized source. They do not assume that an arbitrary quasimode represents the vacuum, or establish the full uniform susceptibility remainder.

**Status: proved Gaussian bounds, exact compact operator estimate, and a conditional ground-state residual corollary.** [[planar-patch-confinement-and-the-spatial-soft-mode|PP]] fixes the patch and source. [[comb-face-transport-and-the-first-nonlinear-jet|FJ]] fixes its comb chart. [[compact-source-normalization-and-the-nonlinear-return|CS]] supplies the fixed-patch realization; [[uniform-centered-poisson-return-and-the-planar-source|PO]] verifies the residual corollary's hypotheses and proves the uniform susceptibility remainder.

## Normalize by the soft source scale

Put \(n=L+1\), \(h=(\kappa/g)^{1/4}\), \(N=L^2\), and write
\[
C=A_L^{1/2},\qquad \omega=\sqrt{\lambda_{\min}(A_L)}\asymp n^{-1}.
\]
The oscillator vacuum law \(\mu\) on face vectors \(X_p\in\mathbb R^3\) has covariance \(C\otimes I_3\), with \(\|C\|\le\sqrt8\). Let \(v=v_{11}\), \(\sum_pv_p^2=1\), and \(Y=\sum_pv_pX_p\). Each component of \(Y\) has variance \(\omega\).

For the same fixed compact probe as GW, its exact scaled chart expression is
\[
B_h=\frac4{h^2}\mathcal B_L=|Y_h|^2,\qquad
Y_h=\sum_pv_p\operatorname{sinc}(h|X_p|/2)X_p.
\tag{WS1}
\]
Thus \(B_0=|Y|^2\), \(m_0=3\omega\), and the harmonic centered-source norm is
\[
\sigma_0=\sqrt{\operatorname{Var}_\mu B_0}=\sqrt6\,\omega .
\tag{WS2}
\]
These definitions apply to the full simultaneous-color invariant carrier, without taking a separate quotient at each face.

## Odd local sums have dimension-independent Gaussian moments

Let \(F=\sum_pv_pf_p(X_p)\), where the scalar \(f_p\) are odd differentiable functions. For every fixed \(q\ge2\),
\[
\|F\|_{L^q(\mu)}
\le c_q\|C\|^{1/2}
\left(\sum_pv_p^2\|\nabla f_p(X_p)\|_{L^q(\mu)}^2\right)^{1/2}.
\tag{WS3}
\]
The constant is independent of the number of faces. The same estimate holds componentwise for a three-vector.

For a direct proof, whiten the Gaussian and join two independent standard Gaussian vectors by the rotation \(Z_\theta=Z\cos\theta+Z'\sin\theta\), \(0\le\theta\le\pi/2\). Its derivative is an independent standard Gaussian at each \(\theta\). Integrating the derivative of \(F(Z_\theta)\), using its zero mean and conditional Gaussian moments, bounds \(\|F\|_q\) by a constant times its Gaussian gradient norm. That gradient satisfies
\[
|\nabla_Z F|^2
\le\|C\|\sum_pv_p^2|\nabla f_p(X_p)|^2.
\]
Minkowski's inequality gives (WS3). No independence between different faces is assumed.

Define \(Z_3=\sum_pv_p|X_p|^2X_p\). Taylor's theorem gives
\[
Y_h=Y-\frac{h^2}{24}Z_3+h^4R_{5,h},
\qquad
\|Z_3\|_q+\|R_{5,h}\|_q\le C_q,
\qquad
\|Y\|_q\le C_q\sqrt\omega .
\tag{WS4}
\]
To check uniformity of the remainder, its single-face vector is
\[
r_{5,h}(x)=h^{-4}
\left[\operatorname{sinc}(h|x|/2)-1+\frac{h^2|x|^2}{24}\right]x.
\]
It is odd, with \(|r_{5,h}(x)|\le C|x|^5\) and
\(|\nabla r_{5,h}(x)|\le C|x|^4\), uniformly for \(h>0\). These follow, including at \(x=0\), from
\(\operatorname{sinc}z=\int_0^1\cos(tz)\,dt\) and the cosine and sine Taylor remainders. Since the local variances are bounded, (WS3) applies. The analogous first remainder gives \(\|Y_h-Y\|_q\le C_qh^2\).

## Source multiplication on finite Hermite spaces

Let \(P_{\le m}\) project onto total oscillator Hermite degree at most a fixed \(m\). Under the Gaussian identification, such vectors are \(p\Omega\), and
\(\|p\|_q\le C_{m,q}\|p\|_2\) for every fixed even \(q\). A finite Wick expansion proves this dimension-independent inequality: contractions between normalized chaos tensors are bounded by their tensor norms, with a number of contraction patterns depending only on \(m,q\).

Apply Hölder's inequality to (WS4), and use \(0<h\le1\). With the actual source curvature \(B_2=-Y\cdot Z_3/12\),
\[
\boxed{
\|B_2P_{\le m}\|\le C_m\sqrt\omega,\qquad
\|(B_h-B_0-h^2B_2)P_{\le m}\|\le C_mh^4,}
\tag{WS5}
\]
\[
\boxed{
\|B_hP_{\le m}\|
\le C_m(\omega+h^2\sqrt\omega+h^4).}
\tag{WS6}
\]
For example the fourth-order source remainder contains \(Z_3^2/576+2Y\cdot R_{5,h}\), followed by terms of orders \(h^6,h^8\); their Gaussian moments are uniformly bounded. The small variance of \(Y\), rather than the global supremum of the compact source, controls the direct \(B_2\) term.

After dividing by \(\sigma_0\), the first source change costs at most
\[
C_m\left(\frac{h^2}{\sqrt\omega}+\frac{h^4}{\omega}\right)
\le C_m(h^2\sqrt n+h^4n),
\tag{WS7}
\]
and the second-order Taylor remainder costs at most \(C_mh^4n\). Multiplication by \((B_0-m_0)/\sigma_0\) itself is bounded on each finite-degree space independently of \(L\).

These estimates also hold after applying CS's chart cutoff and Haar half-density map: source multiplication commutes with the density factor, and the cutoff has absolute value at most one. The omitted Gaussian chart tail is controlled independently of any actual vacuum. For a cutoff equal to one when every \(|hX_p|\le r\), a Gaussian union bound gives
\[
\mu\{\max_p|hX_p|>r\}\le C_rL^2e^{-c_r/h^2}.
\]
Hölder's inequality and the same finite-degree moment bounds make the unweighted tail at most \(C_m n^{1/2}e^{-c/h^2}\), and the source-weighted tail at most that factor times the right side of (WS6), after adjusting constants. These are bounds on the constructed Gaussian vectors, not a localization theorem for the actual vacuum.

## An exact graph-norm estimate on the compact carrier

Return to raw Haar coordinates. Let
\[
\mathsf C=\sum_{\text{raw edges }e}C_e,\qquad
W=\sum_{\text{faces }p}(2-\chi_{1/2}(P_p)),\qquad
\widehat H=h^2\mathsf C+h^{-2}W,\qquad V=h^{-2}W .
\tag{WS8}
\]
The same scaled source obeys the pointwise inequality
\[
0\le B_h\le4V .
\tag{WS9}
\]
Indeed \(|\sum_pv_p\mathbf q_p|^2\le\sum_p|\mathbf q_p|^2\) and
\(|\mathbf q_p|^2=1-q_{0,p}^2\le2(1-q_{0,p})=2-\chi_{1/2}(P_p)\).

Each plaquette contains four distinct raw edges. Each fundamental character receives Casimir \(3/4\) from each of them, giving the exact identity
\[
\mathsf C W=3W-6N .
\tag{WS10}
\]
For a smooth physical vector \(u\), integrate the cross term in
\(\|\widehat H u\|^2\). If \(Z_{e,a}\) are the skew raw derivatives,
\[
\begin{aligned}
\|\widehat H u\|^2
={}&\|h^2\mathsf C u\|^2+\|Vu\|^2
+2h^2\sum_{e,a}\int V|Z_{e,a}u|^2\\
&+3\langle u,Wu\rangle-6N\|u\|^2 .
\end{aligned}
\]
All terms except the last are nonnegative. Consequently
\[
\boxed{
\|Vu\|^2\le\|\widehat H u\|^2+6L^2\|u\|^2,\qquad
\|B_hu\|\le4\bigl(\|\widehat H u\|+\sqrt6\,L\|u\|\bigr).}
\tag{WS11}
\]
The inequality extends to the graph domain of \(\widehat H\). It is exact at every finite \(L,h>0\), before any localization or oscillator approximation. It therefore supplies actual weighted control without the factor \(h^{-2}\) from the crude global multiplication norm.

## Centering and normalization preserve a weighted approximation

Let \(\psi,v\) be normalized vectors, with \(\psi\) the actual vacuum and \(v\) a proposed approximation. For the self-adjoint source \(B_h\), put
\[
\delta_0=\|\psi-v\|,\qquad
\delta_B=\|B_h(\psi-v)\|,\qquad M=\|B_hv\|.
\]
Let \(m_\psi,m_v\) be their means and
\(F_\psi=(B_h-m_\psi)\psi\), \(F_v=(B_h-m_v)v\). Direct subtraction gives
\[
\boxed{
|m_\psi-m_v|\le M\delta_0+\delta_B,\qquad
\|F_\psi-F_v\|\le(2+\delta_0)(\delta_B+M\delta_0).}
\tag{WS12}
\]
For the first bound write the mean difference as
\(\langle\psi-v,B_hv\rangle+\langle\psi,B_h(\psi-v)\rangle\). The second follows by subtracting the two centered vectors and retaining this mean difference.

Suppose the verified approximation satisfies
\[
M\le M_0\omega,\qquad \|F_v\|\ge a\omega
\tag{WS13}
\]
with \(a,M_0>0\) independent of \(L,h\). If
\(\delta_0+\delta_B/\omega\) is sufficiently small, (WS12) gives an actual centered norm at least \(a\omega/2\), and
\[
\boxed{
\left\|\frac{F_\psi}{\|F_\psi\|}-\frac{F_v}{\|F_v\|}\right\|
\le C_{a,M_0}\left(\delta_0+\frac{\delta_B}{\omega}\right).}
\tag{WS14}
\]
The same error controls the mean in units of \(\omega\) and the variance in units of \(\omega^2\). Thus no unknown actual variance lower bound is being assumed.

Conditions (WS13) are checkable on Gaussian quasimodes. If their normalized polynomial part lies in a fixed degree and is sufficiently close to \(\Omega\), (WS5)–(WS7) give \(M=O(\omega)\) and \(\|F_v\|/\omega\) close to \(\sqrt6\), provided \(h^2/\sqrt\omega\) and the Gaussian cutoff tail are small.

## A selected ground residual is sufficient

The remaining spectral input can be stated precisely. Suppose the actual ground energy and first gap in scaled units satisfy
\[
E_0\le C_E n^2,\qquad \gamma\ge c_\gamma/n,
\]
and a normalized quasimode \(v\) has real approximate energy \(\lambda\), with
\[
|\lambda-E_0|\le\gamma/2,\qquad
\rho=\|(\widehat H-\lambda)v\|\le\gamma/4 .
\]
The spectral location condition selects the ground branch; a small residual for an arbitrary excited quasimode does not suffice. After aligning its phase with the ground state, spectral projection gives
\(\delta_0\le C\rho/\gamma\), and \(|\lambda-E_0|\le\rho\). Hence
\[
\|\widehat H(\psi-v)\|\le E_0\delta_0+2\rho.
\]
Using (WS11), \(\omega\asymp n^{-1}\), and (WS13), the result is
\[
\boxed{
\delta_0\le Cn\rho,\qquad
\delta_B\le Cn^3\rho,\qquad
\|\zeta_\psi-\zeta_v\|\le Cn^4\rho,}
\tag{WS15}
\]
when \(n^4\rho\) is sufficiently small. Here \(\zeta\) denotes the centered normalized source vector. These are sufficient estimates with explicit hypotheses, not a proof of compact spectral localization.

[[uniform-planar-localization-and-the-first-physical-levels|UP]] supplies the displayed actual \(E_0\) and gap bounds in its \(\epsilon=hn^{10}\) window. The approximate energy's ground-branch location, residual quality and source conditions (WS13) must still be verified for the quasimode being used.

For any bounded operator \(T\), the corresponding source quadratic forms differ by at most \(2\|T\|\|\zeta_\psi-\zeta_v\|\). The source-vector part of a covariance error is therefore \(O(n^4\rho)\). For the actual reduced inverse, \(\|R\|\le Cn\), that part of the susceptibility error is \(O(n^5\rho)\). Controlling the operator or Poisson approximation is a separate obligation.

## The actual residual supplies the uniform source return

The graph bound closes a real missing bridge: it removes the compact source's global \(h^{-2}\) multiplication loss. It does not by itself establish GW4. For example, a residual bounded only by
\(\rho\le C\epsilon^M/n\), with \(\epsilon=hn^{10}\), would give \(Cn^3\epsilon^M\) in (WS15). No fixed \(M\) makes this uniform in \(n\) on an entire window \(0<\epsilon\le\eta\).

[[comb-chart-ellipticity-and-uniform-local-comparison|UC18–20]] gives the stronger fixed-degree coefficient bounds. [[compact-operator-taylor-remainder-on-planar-wells|The actual operator remainder]] and [[compact-cutoffs-and-uniform-polynomial-quasimodes|the cutoff construction]] now turn the sixth-order vacuum series into a compact quasimode with \(\rho\le Ch^7n^{75/2}\). [[uniform-centered-poisson-return-and-the-planar-source|PO]] checks its spectral location, mean and variance conditions, applies (WS15), and controls the actual centered Poisson residual. The resulting susceptibility remainder is \(Ch^4n^{23}\) on the same window. This conclusion uses the quantitative operator residual in addition to the formal coefficients.
