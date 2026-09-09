# A Uniform Growing-Patch Test for the Actual Source

The remaining spatial test asks whether the actual planar gap and one specified compact-source response admit uniform fourth-order remainder bounds in a quantified confinement window. A coarse spectral return is now proved throughout that window. The sharper powers below remain conjectural targets. Their marked consequence would also control the normalized susceptibility as the patch grows. Keeping normalized energy separate from the absolute confinement scale places this test inside the existing fixed-physical-time innovation programme.

**Status: conjectural fourth-order uniform estimates, with proved conditional consequences.** [[compact-source-normalization-and-the-nonlinear-return|CS1–14]] proves fixed-patch expansions and coefficient envelopes. [[uniform-planar-localization-and-the-first-physical-levels|UP1–12]] now proves a coarse actual spectral return and low-level isolation on the displayed window, without assuming the fourth-order estimates below. It already establishes the gap and innovation-floor limits; the susceptibility limit remains conditional. [[determinant-response-sewing-and-relational-rigidity#Active candidate: oriented innovation transport|Oriented innovation transport]] remains the active foundation.

## Keep the same law, source and boundaries as the patch grows

Use the isolated open \(L\times L\) planar \(SU(2)\) patch of [[planar-patch-confinement-and-the-spatial-soft-mode|PP]], with Gauss law at every vertex, including its boundary. Fix the comb connectors of [[comb-face-transport-and-the-first-nonlinear-jet|FJ]]. At each size use the prescribed lowest-mode probe
\[
\mathcal B_L=\left|\sum_pv_{11}(p)\mathbf q_p\right|^2
\]
and its actual vacuum mean, variance and reduced susceptibility \(\mathcal X_L\). No source coefficient, interaction or clock is fitted after evaluating the response.

Fix \(\kappa>0\), and put
\[
n=L+1,\qquad h=(\kappa/g)^{1/4},\qquad
E=\sqrt{\kappa g}=\kappa h^{-2},\qquad
\epsilon=h n^{10}.
\tag{GW1}
\]
Let \(\widehat\Delta_L=\Delta_L(g)/E\), and let
\(\mathcal S_L=E\mathcal X_L/\operatorname{Var}(\mathcal B_L)\).
The known harmonic coefficient is
\[
c_L=4\sqrt2\sin\frac{\pi}{2n}
\sim\frac{2\sqrt2\pi}{n},\qquad
\frac{4\sqrt2}{n}\le c_L\le\frac{2\sqrt2\pi}{n}.
\tag{GW2}
\]
CS supplies the actual fixed-\(L\) coefficients \(d_L,S_{2,L}\). The sharper [[comb-chart-ellipticity-and-uniform-local-comparison|UC15–17]] estimates give
\[
|d_L|\le C_d n^{10},\qquad |S_{2,L}|\le C_s n^{12}.
\]
They retain the Haar contribution, virtual transitions, moving vacuum and source leakage. The negative four-face gap correction in [[four-face-gap-shift-and-the-complete-source-response|FF]] does not determine either coefficient's large-\(L\) behavior.

## The proposed uniform remainder test

**Conjectural estimate.** There exist \(C,\eta>0\), independent of \(L\) and \(h\), such that for every \(L\ge1\) and \(0<h n^{10}\le\eta\),
\[
\boxed{
\left|\widehat\Delta_L-c_L-h^2d_L\right|
\le C h^4 n^{39},}
\tag{GW3}
\]
\[
\boxed{
\left|\mathcal S_L-c_L^{-1}-h^2S_{2,L}\right|
\le C h^4 n^{41}.}
\tag{GW4}
\]
The same \(\eta\) must cover all patch sizes; allowing an additional unknown \(L\)-dependent onset threshold would not establish this test.

The exponents \(39,41\) are conservative proposed envelopes. The sharper local jet bounds reduce the known coefficient costs, but an exact compact remainder is not determined by finite-degree coefficient estimates. A sharper valid uniform remainder would also resolve the test.

Here the marked quantity is the actual centered and variance-normalized response of this specified probe family. Equation (GW4) is not a uniform theorem for arbitrary increasing collections of marks, a full spectral reconstruction, or an operator-norm return on every observable.

## Conditional relative-error control

Assume (GW3)–(GW4). Dividing (GW3) by \(c_L\), and multiplying (GW4) by \(c_L\), gives constants independent of \(L,h\) such that
\[
\boxed{
\left|\frac{\Delta_L(g)}{E c_L}-1\right|
\le C_\Delta(\epsilon^2n^{-9}+\epsilon^4),\qquad
\left|c_L\mathcal S_L-1\right|
\le C_{\mathcal S}(\epsilon^2n^{-9}+\epsilon^4).}
\tag{GW5}
\]
For example, the gap's first relative correction is bounded by
\(C_d h^2n^{10}/c_L=O(h^2n^{11})=O(\epsilon^2n^{-9})\); its relative remainder is \(O(h^4n^{40})=O(\epsilon^4)\). The susceptibility has the same two powers after normalization by \(1/c_L\).

Shrinking \(\eta\) if necessary makes both relative errors less than \(1/2\). Thus throughout that smaller window the scaled gap is comparable to \(c_L\), and the scaled susceptibility is comparable to \(1/c_L\). Along any sequence \(L\to\infty\), \(\epsilon\to0\),
\[
\boxed{
\widehat\Delta_L\sim\frac{2\sqrt2\pi}{n}\longrightarrow0,\qquad
\mathcal S_L\sim\frac{n}{2\sqrt2\pi}\longrightarrow\infty.}
\tag{GW6}
\]
No sign assumption on \(d_L\) or \(S_{2,L}\) is used. In this window the controlled nonlinear terms cannot remove the harmonic spatial softening of the normalized gap coefficient.

## The absolute physical scale has a different limit

Equation (GW6) is not an absolute-gap collapse. With the stipulated fixed \(\kappa>0\), \(h=\epsilon n^{-10}\) gives, conditionally,
\[
\boxed{
\Delta_L(g)\sim
2\sqrt2\pi\,\kappa\,\frac{n^{19}}{\epsilon^2}
\longrightarrow\infty,\qquad
\frac{\mathcal X_L}{\operatorname{Var}(\mathcal B_L)}
\sim\frac{\epsilon^2}{2\sqrt2\pi\,\kappa\,n^{19}}
\longrightarrow0 .}
\tag{GW7}
\]
The confinement energy \(E=\kappa h^{-2}\) grows faster than the normalized coefficient falls. Even with \(\epsilon\) merely bounded by the sufficiently small fixed window, the conditional lower bound for the physical gap grows at least as a constant times \(\kappa n^{19}/\eta^2\).

This trajectory changes \(g=\kappa h^{-4}\) very rapidly with volume. It is not a fixed-coupling infinite-volume limit or a specified four-dimensional continuum scaling. Nor is the isolated patch vacuum an automatically inherited marginal of a larger physical region.

## Compare innovation floors at the stated duration

For the actual physical operator \(K_{L,g}=H_{L,g}-E_0(L,g)\), define
\(A_t=e^{-tK_{L,g}}\), \(R_t=I-A_t^2\). The exact optimal floor on its vacuum complement is
\[
\gamma_{L,g}(t)
=\inf_{\xi\perp\psi,\ \xi\ne0}
\frac{\langle\xi,R_t^2\xi\rangle}{\langle\xi,R_t\xi\rangle}
=1-e^{-2t\Delta_L(g)}.
\tag{GW8}
\]
The equality follows by spectral calculus and the attained first physical excitation. It is the complete-carrier floor of [[oriented-innovation-and-finite-temporal-repair|OI]], not a claim that the chosen probe alone attains it.

At a fixed scaled duration \(\tau\), \(t=\tau/E\), equations (GW6) and (GW8) give
\(\gamma_{L,g}(\tau/E)\sim4\sqrt2\pi\tau/n\to0\).
At a fixed physical duration \(t=\ell>0\), equation (GW7) instead gives
\(\gamma_{L,g}(\ell)\to1\).
The first comparison uses shrinking physical times. It therefore does not refute the active innovation conjecture at a fixed positive physical slab.

## The remaining estimate is a nonlinear operator residual

[[uniform-planar-localization-and-the-first-physical-levels|The uniform localization theorem]] now supplies actual low-level separation with explicit size dependence. [[weighted-compact-source-return-on-growing-patches|The exact compact graph-norm estimate]] controls source multiplication through that same Hamiltonian. The next step is to propagate sufficiently accurate nonlinear quasimodes and the centered Poisson solution with quantitative operator residuals. Fixed-degree coefficient arithmetic alone is insufficient.

The source loss itself has a size factor:
\[
\|\mathcal B_L\|\le L^2,\qquad
\|4\mathcal B_L/h^2\|\le4L^2h^{-2},
\]
by \(\sum_pv_{11}(p)^2=1\), \(|\mathbf q_p|\le1\), and Cauchy–Schwarz. Its leading scaled variance is \(6\lambda_{\min}(A_L)\asymp n^{-2}\). The weighted source theorem now replaces this crude multiplication loss: a correctly selected ground-quasimode residual \(\rho\), with the specified normalization checks, gives source-vector error at most \(Cn^4\rho\). The variance scale is retained in this bound. It does not by itself prove the susceptibility remainder.

A proof of (GW3)–(GW4), or a rigorously identified failure of the proposed window, would determine where the current nonlinear calculation can be used as spatial evidence. A gap mechanism beyond that window would still require a controlled crossover and the complete mixed-source obligations of [[conditional-vacuum-rigidity-and-the-physical-gap|CV]]. An unevaluated positive mass correction or a different source chosen to hide leakage would not resolve this test.
