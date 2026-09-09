# The Four-Face Gap Softens While Its Source Response Hardens

On the fixed \(2\times2\) planar \(SU(2)\) patch, the first nonlinear physical-gap correction is negative. The original compact scalar source nevertheless has a smaller normalized susceptibility than its harmonic value, because it acquires weight in higher physical excitations. Exact direct and virtual contributions establish both signs. This decides the shared-patch test: a favorable response of that one source does not demonstrate a strengthened gap. A separately constructed oriented probe removes the leading source mixing without changing the Hamiltonian.

**Status: proved first nonlinear coefficients of the actual fixed-patch theory.** [[planar-patch-confinement-and-the-spatial-soft-mode|PP]] owns the twelve-edge square patch with Gauss law at all nine vertices. [[compact-source-normalization-and-the-nonlinear-return|CS1–14]] realizes the expansion in its actual vacuum. [[comb-face-transport-and-the-first-nonlinear-jet|FJ]] fixes the comb coordinates, comparison paths and raw-edge jets. This is distinct from the earlier nine-edge three-face corner.

## The retained physical experiment

Fix \(\kappa>0\), put \(h=(\kappa/g)^{1/4}\), \(E=\sqrt{\kappa g}\), and write
\[
\widehat H_h=H_g/E=\mathcal O+hV_1+h^2V_2+\cdots .
\tag{FF1}
\]
Order the faces as \(a=(1,1),b=(2,1),c=(1,2),d=(2,2)\). The real orthogonal normal-mode matrix has columns
\[
v_0=\tfrac12(1,1,1,1),\quad
v_1=\tfrac12(1,-1,1,-1),\quad
v_2=\tfrac12(1,1,-1,-1),\quad
v_3=\tfrac12(1,-1,-1,1).
\]
The corresponding oscillator frequencies are
\(\omega=(\sqrt2,2,2,\sqrt6)\).
Let \(\Omega\) be the normalized oscillator vacuum and
\[
\phi=f\Omega,\qquad
f=\frac{|Y_0|^2/\sqrt2-3}{\sqrt6},\qquad
c_0=2\sqrt2 .
\tag{FF2}
\]
This is the normalized first physical scalar excitation. All inverses below act within the simultaneous-conjugation-invariant oscillator carrier.

Keep the actual compact multiplication source
\[
B=|Q_0|^2,\qquad Q_m=\sum_pv_m(p)\mathbf q_p,
\qquad P_p=q_{0,p}I-i\mathbf q_p\cdot\sigma ,
\tag{FF3}
\]
with the fixed comb-based plaquettes \(P_p\). Let \(\mathcal X_g\) be its actual centered reduced-resolvent susceptibility and \(N_g\) its actual vacuum variance. The quantities computed below are
\[
\frac{\Delta_g}{E}=c_0+h^2d+O(h^4),\qquad
\mathcal S_g=E\frac{\mathcal X_g}{N_g}
=c_0^{-1}+h^2s+O(h^4).
\tag{FF4}
\]
The scale, source and vacuum conventions are the same in both expressions.

## Direct electric hardening is reversed by the complete virtual response

For \(K=\mathcal O-\omega_{\rm vac}\), define
\[
W_\Omega=\langle V_1\Omega,K^{-1}_{\perp}V_1\Omega\rangle,\qquad
W_\phi=\langle V_1\phi,(K-c_0)^{-1}_{\phi^\perp}V_1\phi\rangle .
\]
The second inverse is well defined on the physical carrier. Its arguments are odd scalar states above the first excitation. The complete gap coefficient is
\[
d=\langle\phi,V_2\phi\rangle-\langle\Omega,V_2\Omega\rangle
-(W_\phi-W_\Omega).
\tag{FF5}
\]

[[four-face-direct-kinetic-and-potential-correction|The direct-form calculation]] and [[four-face-cubic-response-and-source-leakage|the cubic resolvent calculation]] give the following ordinary coefficients of \(h^2\):

| Contribution to the excitation-minus-vacuum coefficient | Exact value |
| --- | --- |
| Electric metric terms | \(19\sqrt2/12+\sqrt3/6\) |
| Haar half-density term | \(0\) |
| Magnetic quartic term | \(-5/32-5\sqrt2/24-5\sqrt3/48\) |
| Virtual cubic response \(W_\Omega-W_\phi\) | \(-37\sqrt2/28-\sqrt3/6\) |

The density term is \(-4\) in each absolute energy; it cancels only after retaining both energies. The direct gap correction is positive, but the virtual correction is larger in magnitude and negative. Adding every row gives
\[
\boxed{d=-\frac5{32}+\frac{3\sqrt2}{56}-\frac{5\sqrt3}{48}
\approx-0.2609105183<0.}
\tag{FF6}
\]
For example, \(\sqrt2<3/2\) already bounds the first two terms by \(-17/224\), before the negative \(\sqrt3\) term.

The separate actual second-order energies are
\[
\begin{aligned}
e_{\Omega,2}
&=-\frac{1065}{224}+\frac{9\sqrt2}{224}
-\frac{5\sqrt3}{64}-\frac{\sqrt6}{32},\\
e_{\phi,2}
&=-\frac{275}{56}+\frac{3\sqrt2}{32}
-\frac{35\sqrt3}{192}-\frac{\sqrt6}{32}.
\end{aligned}
\tag{FF7}
\]
Their difference is (FF6). Thus the complete physical gap is
\(\Delta_g=2\sqrt{2\kappa g}+\kappa d+O(\kappa\sqrt{\kappa/g})\).
The sign refers to the correction relative to the harmonic value, not a claim that the absolute gap decreases as \(g\) increases.

## Two higher-energy source channels reverse the susceptibility verdict

Write \(T_{ijk}=Y_i\cdot(Y_j\times Y_k)\). The exact source leakage vector from the cubic owner is
\[
\ell=\left(\frac{\sqrt3}{42}T_{012}
+\frac{\sqrt3}{12}T_{013}\right)\Omega .
\]
Its two nonzero spectral weights and excitation energies are
\[
\begin{array}{c|c|c}
\text{channel}&\text{coefficient of escaped weight }h^2&\text{energy}\\ \hline
012&w_1=2\sqrt2/49&\nu_1=4+\sqrt2\\
013&w_2=\sqrt3/2&\nu_2=2+\sqrt2+\sqrt6 .
\end{array}
\tag{FF8}
\]
All five-quantum leakage cancels. The five-quantum states still contribute to the virtual excited energy in (FF5); the two calculations must not be conflated.

[[nonlinear-scalar-source-and-the-vacuum-response-coefficient|NV11–13]] now yields
\[
\begin{aligned}
\mathcal L
&=\sum_{i=1}^2w_i\left(\frac1{\nu_i}-\frac1{c_0}\right)
=-\frac{1101}{2744}+\frac{4\sqrt2}{343}+\frac{\sqrt3}{8},\\
s&=-\frac d8+\mathcal L
=-\frac{33517}{87808}+\frac{109\sqrt2}{21952}
+\frac{53\sqrt3}{384}
\approx-0.1356266149<0.
\end{aligned}
\tag{FF9}
\]
The rational bounds \(\sqrt2<3/2\), \(\sqrt3<7/4\) give
\(s<-69925/526848<0\).
The true gap softens, so its inverse rises at this order; the higher-channel weights instead make this particular normalized susceptibility fall.

An energy proxy extracted from that single susceptibility therefore has the opposite correction:
\[
\frac{N_g}{\mathcal X_g}
=c_0E-8\kappa s+O(\kappa h^2),
\qquad -8s\approx1.085012919>0.
\tag{FF10}
\]
This is a source-dependent proxy, not a second definition of the physical gap. The exact spectral inequality \(N_g/\mathcal X_g\ge\Delta_g\) is respected.

At each fixed scaled duration \(\tau>0\), put \(r_\alpha=1-e^{-2\tau\alpha}\). The source's innovation quotient also separates its gap and leakage pieces:
\[
\mathfrak q_g(\tau)
=1-e^{-2\tau(c_0+h^2d)}
+h^2\sum_{i=1}^2w_i\,
\frac{r_{\nu_i}(r_{\nu_i}-r_{c_0})}{r_{c_0}}
+o(h^2).
\tag{FF11}
\]
Every displayed leakage contribution is positive. The sign of the total correction relative to the harmonic quotient depends on the duration as well as the gap term; it cannot be inferred from the leakage sign alone.

For these exact coefficients, the sign actually changes. Write
\(\mathfrak q_g(\tau)=1-e^{-2\tau c_0}+h^2q_2(\tau)+o(h^2)\).
Factoring (FF11) gives
\[
q_2(\tau)=e^{-2\tau c_0}\left[
2\tau d+\sum_iw_i
\frac{(1-e^{-2\tau\nu_i})(1-e^{-2\tau(\nu_i-c_0)})}
{1-e^{-2\tau c_0}}\right].
\]
The two short-duration leakage coefficients satisfy
\[
\frac{w_1\nu_1(\nu_1-c_0)}{c_0}=\frac27,\qquad
\frac{w_2\nu_2(\nu_2-c_0)}{c_0}=3+\sqrt6 .
\]
Consequently
\[
q_2(\tau)=2\tau\left[
\frac{701}{224}+\frac{3\sqrt2}{56}
-\frac{5\sqrt3}{48}+\sqrt6\right]+O(\tau^2)>0
\quad\text{for sufficiently small }\tau>0 .
\]
The bracket is positive already from
\(\sqrt6-5\sqrt3/48=\sqrt3(\sqrt2-5/48)>0\).
Since both \(\nu_i>c_0\), at long duration
\[
q_2(\tau)=e^{-2\tau c_0}
\left[2\tau d+\frac{2\sqrt2}{49}+\frac{\sqrt3}{2}+o(1)\right]<0
\quad\text{for sufficiently large }\tau .
\]
Continuity therefore gives at least one positive duration where this coefficient vanishes. These are duration limits of the already extracted \(h^2\) coefficient. They assert no uniform expansion when \(\tau\) and \(h^{-1}\) grow together.

## An oriented physical probe removes the leading source mixing

[[four-face-oriented-source-and-the-gap-following-probe|The corrected source construction]] uses the same Hamiltonian and comparison paths:
\[
\boxed{
B^\sharp=|Q_0|^2-\frac27Q_0\cdot(Q_1\times Q_2)
-Q_0\cdot(Q_1\times Q_3).}
\tag{FF12}
\]
It is bounded, real and gauge invariant, with coefficients independent of \(g\). Its two cubic terms exactly cancel the leading leakage (FF8). Its normalized susceptibility coefficient is consequently \(-d/8>0\), and its innovation coefficient at this order is just the negative gap-shift contribution \(2\tau d\,e^{-2\tau c_0}\). This is a distinct observable in the same complete physical source algebra. It does not alter the original experiment or add a mass term.

The finite test therefore requires the elementary law to control the complete source carrier, including the oriented cubic comparisons. [[four-face-optimal-quadratic-response-and-parity|The full quadratic optimization]] strengthens the conclusion: even its minimum has exactly the coefficient (FF11), because mixed first-order corrections vanish by parity. [[four-face-oriented-source-extension-and-the-schur-surplus|The extended Gram pencil]] then subtracts the two leakage weights and attains the physical-gap coefficient. A criterion restricted to the quadratic carrier would draw the wrong short-duration conclusion about this correction.

The [independent Hermite receipt](receipts/four_face_nonlinear_receipt.py) reconstructs every raw row and uses exact arithmetic in \(\mathbb Q(\sqrt2,\sqrt3)\). It checks the one-plaquette calibration, both density constants, the direct and virtual contributions, the cancellation of higher-degree leakage, and agreement of the two normalized-susceptibility formulas and source-energy moments. The direct and cubic owners use independent Gaussian and triple contractions. No sampled dynamics or numerical spectral cutoff is used.

The calculation proves a fixed-patch nonlinear response. Its negative gap coefficient rejects reading the first shared-patch correction as an automatically positive mass contribution. It supplies no bound on the full spatial remainder, no exchange of the confinement and large-volume limits, and no continuum or infinite-volume Yang–Mills gap.
