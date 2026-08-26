# A Falsifiable Causal-Scale Template for the CMB

The clean first observable is a small modulation of the primordial curvature state, periodic in logarithmic scale and propagated through otherwise standard photon--baryon transfer. This realizes the grain as a scale unit rather than confusing it with the acoustic ruler. An optional (A_2) branch order parameter predicts when the fundamental modulation cancels and when a third-harmonic higher-point signal may survive. A stronger material route could derive the photon--baryon sound cone from causal dwell and transport, but it must return baryon loading, opacity, and hot-history scaling rather than merely redescribe them.

## Choose the causal location of the new physics

A grain proposal must first choose which part of the forward model changes.

### Initial-state route

The causal carrier fixes primordial gauge-invariant data,

$$
q_A(\mathbf k)
\xrightarrow{\mathfrak S_{\mathrm{prim}}}
I(\mathbf k)
=
\{\zeta,S_i,h_\lambda,\ldots\},
$$

with covariance

$$
\mathcal P_{IJ}(k)
=
\mathcal M_{IA}(k)
\mathcal P^q_{AB}(k)
\mathcal M^\dagger_{BJ}(k).
$$

Standard Einstein--Boltzmann transfer then gives

$$
C_\ell^{XY}
=
4\pi\int\mathrm d\ln k
\sum_{IJ}
\mathcal P_{IJ}(k)
\Delta_{\ell,I}^{X}(k)
\Delta_{\ell,J}^{Y}(k).
$$

This is the preferred minimal test because it does not disturb the already successful recombination and acoustic dynamics.

### Material/dynamical route

The grain instead constructs or modifies the effective photon--baryon characteristic geometry,

$$
(\mu_{\mathrm{sc}},\omega_{\mathrm{hot}})
\xrightarrow{\mathfrak W_{\gamma b}}
(R,c_s,\dot\kappa,\Phi,\Psi).
$$

Then it must derive or perturb

$$
c_s^2=\frac{1}{3(1+R)}
$$

and predict correlated changes to acoustic phase, baryon loading, gravitational driving, diffusion damping, recombination, neutrino phase shifts, and lensing. One illustrative deformation is

$$
\omega_\gamma^2(k,\eta)
=
c_s^2k^2
\left[1+\alpha_gF(k/k_g,\eta)\right],
$$

which produces

$$
\delta\varphi_g(k)
=
\int^{\eta_*}
\left[
\omega_\gamma(k,\eta)-c_sk
\right]\mathrm d\eta.
$$

This equation is only a parameterization. An actual explanation of the relational geometry must derive (F), (R), and the opacity from the causal response, not fit them independently.

The two routes should not be mixed in a first search. A primordial feature and a modified sound speed can mimic one another over a limited range but predict different polarization, damping, lensing, and matter-transfer signatures.

## The UV/IR solder is indispensable

The canonical diagnostic grain has

$$
\lambda_*=4.264\,\mathrm{fm}.
$$

The Planck best-fit comoving distance to last scattering is

$$
D_M(z_*)=13.86955\,\mathrm{Gpc}.
$$

If (lambda_*) were naively treated as a present comoving wavelength, its angular projection would be of order

$$
\ell_g\sim\frac{D_M}{\lambda_*}
\simeq10^{41}
$$

before the optional (2\pi) wavenumber convention. If it were a physical length at recombination, converting it to a comoving length would still give (ell_g\sim10^{38}). Primary CMB measurements end around a few thousand. The (4.3\,\mathrm{fm}) ruler therefore cannot directly be an acoustic wavelength.

Likewise,

$$
\ln\frac{r_s(z_*)}{\lambda_*}
\simeq89.8.
$$

This is a bare comparison of the sound horizon with the microscopic ruler, not an inflation prediction; the epoch and comoving convention are absent. It exposes the missing object: an approximately ninety-e-fold UV/IR history or some nonlocal correspondence must relate the grain ruler to CMB scales.

If the grain is created as a physical correlation length at scale factor (a_g), a minimal comoving anchor would be

$$
k_g
=
\chi_g\frac{a_g}{\lambda_*},
\qquad
\chi_g\in\{1,2\pi\},
$$

followed by whatever transfer or freeze-out law the theory derives. The values of (a_g), (chi_g), reheating history, and any anomalous scaling must be frozen before the CMB is inspected.

## A scale unit predicts a logarithmic phase

Let

$$
\sigma(k):=\ln\frac{k}{k_g}.
$$

If one realized scale grain has width (delta\sigma_g), its phase is

$$
\theta_g(k)
=
\frac{2\pi}{\delta\sigma_g}\sigma(k)+\phi_g.
$$

The minimal positive scalar template is

$$
\boxed{
\mathcal P_\zeta(k)
=
\mathcal P_\zeta^{(0)}(k)
\exp\!\left[
A_gW(k)\cos\theta_g(k)
\right].
}
$$

The exponential prevents a negative power spectrum. (W(k)) is a fixed envelope determined by the proposed transition or resonance width. A free spline envelope would erase the content of the grain hypothesis.

The literal unit choice (delta\sigma_g=1) gives one cycle per unit (ln k), or a wavelength ratio (e). Across the approximate Planck feature-sensitive interval (0.005\lesssim k\lesssim0.2\,\mathrm{Mpc}^{-1}), it would produce about

$$
\ln(0.2/0.005)\simeq3.69
$$

cycles. This makes the unit claim directly falsifiable once (k_g), (A_g), (W), and (phi_g) are independently fixed.

A single sharp event at conformal time (eta_g) would instead suggest

$$
\theta_g(k)\propto k\eta_g,
$$

which is linear in (k). The theory must choose the dilation/unit mechanism or the sharp-event mechanism; searching both and reporting the better one incurs a larger trials penalty.

## The (A_2) branch selection rule

Let

$$
\omega_3:=e^{2\pi i/3}
$$

and let (w_a\ge0), (sum_aw_a=1), be the realized weights of three branches. Define the first branch moment

$$
\Xi_1
:=
\sum_{a=0}^{2}w_a\omega_3^a.
$$

The branch-sensitive version of the scale template is

$$
\ln\mathcal P_\zeta(k)
=
\ln\mathcal P_\zeta^{(0)}(k)
+A_gW(k)
\operatorname{Re}
\left[
\Xi_1e^{i\theta_g(k)}
\right].
$$

For the completely symmetric state (w_0=w_1=w_2=1/3),

$$
\Xi_1
=
\frac13(1+\omega_3+\omega_3^2)
=0.
$$

Thus an unbroken three-branch completion has no fundamental two-point ripple in this template. The exact trigonometric identities

$$
\sum_{a=0}^{2}
\cos\left(\theta+\frac{2\pi a}{3}\right)
=0,
$$

$$
\sum_{a=0}^{2}
\cos^2\left(\theta+\frac{2\pi a}{3}\right)
=\frac32,
$$

and

$$
\sum_{a=0}^{2}
\cos^3\left(\theta+\frac{2\pi a}{3}\right)
=\frac34\cos(3\theta)
$$

show a potentially valuable selection rule. Symmetric branch averaging can hide the fundamental in the power spectrum while allowing a third harmonic in a cubic statistic. Turning that identity into a bispectrum prediction still requires a nonlinear curvature map; the trigonometry alone does not generate non-Gaussianity.

If a descended associative operator supplies three genuine energy levels, an independent refinement is an additive gap multiplet,

$$
\delta\ln\mathcal P_\zeta(k)
=
\sum_{i<j}
A_{ij}W_{ij}(k)
\cos\!\left[
\Omega_{ij}\ln\frac{k}{k_0}
+\phi_{ij}
\right],
$$

with

$$
\Omega_{13}=\Omega_{12}+\Omega_{23}.
$$

This is more restrictive than one arbitrary oscillation, but it is licensed only after the same operator derives the centers, widths, residues, and clock-to-(ln k) solder. A Jordan cubic by itself does not do so.

## Propagation into TT, TE, and EE

For a small primordial modulation,

$$
\delta C_\ell^{XY}
=
4\pi\int\mathrm d\ln k\,
\delta\mathcal P_\zeta(k)
\Delta_\ell^X(k)\Delta_\ell^Y(k).
$$

The same ((k_g,\delta\sigma_g,\phi_g,W)) must be used in every spectrum. The residuals will not look identical because the transfer kernels differ and TE can change sign. “Same phase” means one common primordial source after forward projection, not peak-by-peak alignment in (ell).

If the descent also predicts tensors, isocurvature, parity violation, or a preferred direction, the data vector must be enlarged rather than silently absorbing those effects into the scalar template. For example, a selected spatial direction would produce off-diagonal or bipolar-spherical-harmonic covariance, while a parity-odd photon coupling could produce TB/EB. Octonionic nonassociativity alone predicts neither.

## Likelihood contract

For bandpowers,

$$
m_b^{XY}(\Theta)
=
\sum_\ell W_{b\ell}^{XY}
D_\ell^{XY}(\Theta)
+F_b^{XY}(\eta_{\mathrm{fg}}),
$$

where (W_{b\ell}) is the experiment’s window matrix and (F_b) is its foreground model. A high-(ell) Gaussian approximation has

$$
-2\ln\mathcal L
=
(\mathbf d-\mathbf m)^T
\mathbf C^{-1}
(\mathbf d-\mathbf m)
+\ln|\mathbf C|
+\text{const},
$$

but low-(ell) Planck data require the collaboration likelihood or an explicitly validated replacement.

Before a search, freeze:

- whether the phase is logarithmic or linear in (k);
- the relation between (lambda_*), (k_g), and the generation epoch;
- (delta\sigma_g), or a prior fixed by the wall theory;
- the envelope and linewidth;
- the (A_2) branch weights or gap ratios;
- which scalar, tensor, isocurvature, anisotropic, or parity channels are present;
- the foreground and lensing treatment; and
- the holdout observable.

A credible detection requires

1. a common causal parameter set across TT, TE, and EE;
2. agreement between Planck and ACT with overlap covariance handled;
3. observing-frequency independence after foreground marginalization;
4. global significance from simulations over the entire searched parameter volume;
5. Bayesian evidence with declared priors, not only a local (Delta\chi^2);
6. correct propagation through diffusion damping and lensing; and
7. a predicted bispectrum, trispectrum, lensing, matter-spectrum, or held-out multipole signature.

## Null result and kill conditions

The current null is the six-parameter adiabatic (Lambda)CDM spectrum. Planck found no significant primordial feature after accounting for search freedom, and ACT DR6 independently finds TT, TE, and EE well described by (Lambda)CDM plus foregrounds. The grain model is therefore viable only as a constrained residual hypothesis unless it first derives the standard acoustic geometry itself.

The CMB version of the proposal fails if

- the (4.3\,\mathrm{fm})-to-cosmological-scale map is chosen after seeing the residual;
- TT prefers a pattern that its fixed primordial model fails to reproduce in TE and EE;
- the feature follows observing frequency or foreground masks;
- a dynamical model shifts peaks without the required damping, polarization, or lensing consequences;
- equal (A_2) weights are claimed while a fundamental two-point ripple is retained;
- the local improvement disappears under a global trials calculation; or
- the CMB-conditioned grain value is reused as supposedly independent CMB evidence.
