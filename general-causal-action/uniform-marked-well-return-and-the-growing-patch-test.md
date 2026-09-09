# A Uniform Growing-Patch Test for the Actual Source

The actual planar gap and one prescribed compact-source response satisfy uniform fourth-order remainder bounds in a quantified confinement window. The proved powers are stronger than the original test required. Their joint limit retains the harmonic spatial softening in scaled energy, while the stipulated absolute confinement scale grows. This decides the marked-well test within oriented innovation transport.

**Status: proved uniform estimates and their marked consequences.** [[uniform-nonlinear-planar-gap-and-marked-response|UN]] owns the nonlinear spectral proof and synthesis; [[uniform-centered-poisson-return-and-the-planar-source|PO]] owns the centered-source proof. [[uniform-planar-localization-and-the-first-physical-levels|UP]] supplies actual low-level isolation. [[determinant-response-sewing-and-relational-rigidity#Active candidate: oriented innovation transport|Oriented innovation transport]] remains the active foundation.

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
[[compact-source-normalization-and-the-nonlinear-return|CS]] supplies the actual fixed-\(L\) coefficients \(d_L,S_{2,L}\). The sharper [[comb-chart-ellipticity-and-uniform-local-comparison|UC15–17]] estimates give
\[
|d_L|\le C_d n^{10},\qquad |S_{2,L}|\le C_s n^{12}.
\]
They retain the Haar contribution, virtual transitions, moving vacuum and source leakage. The negative four-face gap correction in [[four-face-gap-shift-and-the-complete-source-response|FF]] does not determine either coefficient's large-\(L\) behavior.

## The uniform remainder test is resolved

There exist \(C,\eta>0\), independent of \(L,h\), such that for every \(L\ge1\) and \(0<hn^{10}\le\eta\),
\[
\boxed{
\left|\widehat\Delta_L-c_L-h^2d_L\right|
\le Ch^4n^{21},}
\tag{GW3}
\]
\[
\boxed{
\left|\mathcal S_L-c_L^{-1}-h^2S_{2,L}\right|
\le Ch^4n^{23}.}
\tag{GW4}
\]
The original proposed envelopes were \(Ch^4n^{39}\) and \(Ch^4n^{41}\). UN proves these stronger estimates with one onset window for all sizes.

The proof has three distinct inputs: the [[compact-operator-taylor-remainder-on-planar-wells|actual differential remainder]], the [[compact-cutoffs-and-uniform-polynomial-quasimodes|compact cutoff and quasimodes]], and the [[uniform-centered-poisson-return-and-the-planar-source|moving centered Poisson equation]]. Finite-degree coefficient bounds alone would not establish (GW3)–(GW4).

The marked quantity is the centered and variance-normalized response of this specified probe family. Equation (GW4) does not assert an estimate for arbitrary increasing collections of marks or an operator-norm return on every observable.

## Relative errors vanish throughout the bounded window

Dividing (GW3) by \(c_L\), and multiplying (GW4) by \(c_L\), gives
\[
\boxed{
\left|\frac{\Delta_L(g)}{Ec_L}-1\right|
+|c_L\mathcal S_L-1|
\le C(\epsilon^2n^{-9}+\epsilon^4n^{-18}).}
\tag{GW5}
\]
The first relative correction is \(O(h^2n^{11})\); the relative remainder is \(O(h^4n^{22})\). A smaller size-independent \(\eta\) makes these errors less than \(1/2\). Along every sequence \(L\to\infty\), \(0<\epsilon_L\le\eta\),
\[
\boxed{
\widehat\Delta_L\sim\frac{2\sqrt2\pi}{n}\longrightarrow0,\qquad
\mathcal S_L\sim\frac{n}{2\sqrt2\pi}\longrightarrow\infty.}
\tag{GW6}
\]
There is no requirement that \(\epsilon_L\to0\). No sign assumption on \(d_L\) or \(S_{2,L}\) is used. The controlled nonlinear terms cannot remove the harmonic spatial softening in this window.

## The absolute physical scale has a different limit

At the stipulated fixed \(\kappa>0\), \(h=\epsilon n^{-10}\) gives
\[
\boxed{
\Delta_L(g)\sim
2\sqrt2\pi\,\kappa\,\frac{n^{19}}{\epsilon_L^2}
\longrightarrow\infty,\qquad
\frac{\mathcal X_L}{\operatorname{Var}(\mathcal B_L)}
\sim\frac{\epsilon_L^2}{2\sqrt2\pi\,\kappa\,n^{19}}
\longrightarrow0.}
\tag{GW7}
\]
The confinement energy grows faster than the normalized gap coefficient falls. This trajectory changes \(g=\kappa h^{-4}\) rapidly with volume. It is not a fixed-coupling infinite-volume limit or a specified four-dimensional continuum scaling. The isolated patch vacuum is not automatically an inherited state of a larger region.

## Compare innovation floors at the stated duration

For the actual physical operator \(K_{L,g}=H_{L,g}-E_0(L,g)\), define
\(A_t=e^{-tK_{L,g}}\), \(R_t=I-A_t^2\). Its exact optimal floor on the vacuum complement is
\[
\gamma_{L,g}(t)
=\inf_{\xi\perp\psi,\ \xi\ne0}
\frac{\langle\xi,R_t^2\xi\rangle}{\langle\xi,R_t\xi\rangle}
=1-e^{-2t\Delta_L(g)}.
\tag{GW8}
\]
This follows by spectral calculus and the attained first physical excitation. It is the complete-carrier floor of [[oriented-innovation-and-finite-temporal-repair|OI]]; the chosen probe need not attain it.

At fixed scaled duration \(\tau>0\), \(t=\tau/E\),
\(\gamma_{L,g}(\tau/E)\sim4\sqrt2\pi\tau/n\to0\).
At fixed physical duration \(t=\ell>0\),
\(\gamma_{L,g}(\ell)\to1\).
The first comparison uses shrinking physical times, so it does not refute the active conjecture at a fixed positive physical slab.

## Spatial assembly remains the next discriminating test

The uniform remainder resolves this isolated planar test. [[compact-regional-covariance-and-susceptibility-return|The fixed-profile compact return]] preserves inherited regional covariance and susceptibility, while [[vacuum-hellinger-return-and-regional-conditional-projections|the conditional-operator theorem]] proves actual one-face memory. [[regional-innovation-and-exterior-information-balance|The regional balance]] retains the exterior channel in the same oriented response. [[uniform-collar-capture-and-the-local-gap-limitation|The collar comparison]] now controls this omission and proves a stronger discriminator: complete one-face radial harmonic coercivity coexists with the closing global harmonic floor. [[compact-quadratic-carrier-and-the-pairing-range-return|The complete quadratic source return]] now controls those growing mixed marks. Their optimal floor remains of order \(\min\{1,t/(R+1)\}\), so [[spatial-block-sewing-and-the-vacuum-cap-response|the same sewing law]] must constrain further new-range surplus to obtain a range-independent physical bound.

A gap mechanism beyond the present window requires controlled crossover and the complete mixed-source obligations of [[conditional-vacuum-rigidity-and-the-physical-gap|CV]]. The four-face counterprobe remains a control against inferring reinforcement from one favorable readout.
