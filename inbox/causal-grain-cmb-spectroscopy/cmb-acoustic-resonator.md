# The CMB Acoustic Resonator and Its Phase Readouts

The CMB acoustic pattern is a classical, phase-coherent normal-mode spectrum of the pre-recombination photon--baryon plasma. Temperature and E-polarization read approximately conjugate quadratures: compression/rarefaction and velocity-generated quadrupole. Their correlated TT, TE, and EE structure makes the CMB an unusually strict analyser of primordial phase, but the same structure is already explained by linear Einstein--Boltzmann physics and does not by itself imply a quantum of spacetime.

## The oscillator

In conformal Newtonian gauge, write

$$
\mathrm ds^2
=a^2(\eta)
\left[-(1+2\Psi)\mathrm d\eta^2
+(1-2\Phi)\mathrm d\mathbf x^2\right].
$$

For one scalar Fourier mode, define

$$
R(\eta):=\frac{3\rho_b}{4\rho_\gamma},
\qquad
c_s^2=\frac{1}{3(1+R)},
\qquad
D:=\Theta_0+\Psi,
$$

where (Theta_0=delta_\gamma/4) is the photon-temperature monopole. In tight coupling, after photon shear is neglected, the photon continuity and Euler equations combine schematically as

$$
D''
+\frac{R'}{1+R}D'
+c_s^2k^2D
=S_{\Phi,\Psi}(k,\eta).
$$

The source contains the gravitational potentials and their time evolution. In the ideal limit of constant (R,Phi,Psi) and negligible initial velocity,

$$
D(\eta)
=
[D_i+R\Psi]\cos[k r_s(\eta)]-R\Psi,
$$

with

$$
r_s(\eta)
:=
\int_0^\eta c_s(\tilde\eta)\,\mathrm d\tilde\eta.
$$

This elementary solution exposes three established effects:

- the cosine produces the harmonic acoustic series;
- baryons shift the equilibrium and preferentially enhance compression peaks for adiabatic initial data; and
- decaying potentials drive modes that enter during radiation domination.

The full equations and gauge conventions are treated by [Ma and Bertschinger](https://doi.org/10.1086/176550); the analytic acoustic treatment is developed by [Hu and Sugiyama](https://doi.org/10.1086/177989).

## The photon--baryon relational geometry

The tight-coupled plasma has a precise geometry of **propagation relative to dwell**. Its relevant inertial densities are the enthalpies

$$
h_\gamma=\rho_\gamma+p_\gamma=\frac43\rho_\gamma,
\qquad
h_b\simeq\rho_b,
$$

so the baryon-loading parameter is exactly the ratio

$$
\boxed{
R=\frac{h_b}{h_\gamma}
=\frac{3\rho_b}{4\rho_\gamma}.
}
$$

Photons supply almost all of the pressure restoring force; baryons add inertia while contributing negligible pressure. For tightly locked adiabatic perturbations,

$$
\delta_b=\frac34\delta_\gamma,
$$

and hence

$$
\delta\rho_b
=R\,\delta\rho_\gamma,
\qquad
\delta p
=\frac13\delta\rho_\gamma,
\qquad
\delta\rho
=(1+R)\delta\rho_\gamma.
$$

It follows that

$$
\boxed{
c_s^2
=\frac{\delta p}{\delta\rho}
=\frac{1}{3(1+R)}.
}
$$

This is the exact standard core of the user’s intuition. Radiation is the propagation/stiffness register; baryonic mass is the storage, inertia, or **dwell-loading** register. Their relation fixes the sound cone. Up to a conformal factor, one may display that cone by

$$
\mathrm d\widehat s_{\mathrm{ac}}^2
=-c_s^2(\eta)\,\mathrm d\eta^2
+\mathrm d\mathbf x^2,
$$

whose null curves obey (|\mathrm d\mathbf x/\mathrm d\eta|=c_s). This acoustic metric is an effective characteristic geometry on the already supplied FLRW spacetime; it is not a replacement for the gravitational metric.

The scale-grain hypothesis can now be stated without metaphor. If the hot-history realization supplies a comoving scale ruler (lambda_{g,\mathrm{com}}(\eta)), define the accumulated acoustic-grain count by

$$
\mathrm dn_{\mathrm{ac}}
:=
\frac{c_s(\eta)\,\mathrm d\eta}
{\lambda_{g,\mathrm{com}}(\eta)}.
$$

Then

$$
r_s(\eta_*)
=
\int^{\eta_*}
\lambda_{g,\mathrm{com}}(\eta)
\,\mathrm dn_{\mathrm{ac}},
$$

and the standing-wave condition becomes

$$
k_m
\int^{\eta_*}
\lambda_{g,\mathrm{com}}\,\mathrm dn_{\mathrm{ac}}
\simeq m\pi.
$$

Thus a peak is a relation among a very large number of scale units, not one grain. The grain would explain the relational acoustic geometry only if a material/hot-history solder derives

$$
\mathfrak W_{\gamma b}:
(\mu_{\mathrm{sc}},\omega_{\mathrm{hot}})
\longmapsto
(h_\gamma,h_b,\dot\kappa,
\lambda_{g,\mathrm{com}})
$$

and thereby returns (R(eta)), (c_s(eta)), and Thomson locking. At present the repository imports those quantities from standard particle, plasma, and gravitational physics. The grain therefore supplies a promising **common-unit interpretation** of the acoustic geometry, but not yet its derivation.

## Sound horizon and angular projection

At photon decoupling,

$$
\theta_*
=
\frac{r_s(z_*)}{D_M(z_*)},
\qquad
\ell_A
=
\frac{\pi}{\theta_*}.
$$

Ideal extrema satisfy

$$
k_mr_s(z_*)\simeq m\pi,
\qquad
\ell_m\simeq k_mD_M(z_*).
$$

The repository’s local Planck best-fit product gives

$$
z_*=1089.914,
\quad
r_s(z_*)=144.3938\,\mathrm{Mpc},
\quad
D_M(z_*)=13.86955\,\mathrm{Gpc},
\quad
100\theta_*=1.041085,
$$

and therefore

$$
\ell_A=301.76.
$$

The first TT peak is nevertheless near (ell=220.6), not (301.8). Potential evolution, baryon loading, neutrino free streaming, Doppler projection, the thickness of last scattering, and lensing shift or reshape actual extrema. Reading the plotted peak numbers as a literal integer spectrum is therefore already falsified by the first peak. Planck reports the first three TT maxima at

$$
\ell=220.6\pm0.6,
\qquad
538.1\pm1.3,
\qquad
809.8\pm1.0.
$$

The full table of measured TT, TE, and EE extrema is in the [Planck 2018 overview](https://doi.org/10.1051/0004-6361/201833880).

## Temperature and polarization are quadrature measurements

For the passive growing adiabatic mode, the idealized phases are

$$
\Theta_0+\Psi\sim\cos(k r_s),
\qquad
v_{\gamma b}\sim\sin(k r_s).
$$

Thomson scattering generates linear polarization from a local radiation quadrupole. Near recombination that quadrupole is sourced approximately by the velocity/dipole through the finite photon mean free path,

$$
\Pi_\gamma
\sim
\frac{k}{\dot\kappa}v_{\gamma b},
\qquad
\dot\kappa=a n_e\sigma_T.
$$

Consequently, in the simple phase picture,

$$
TT\sim\cos^2(k r_s),
\qquad
EE\sim\sin^2(k r_s),
\qquad
TE\sim\tfrac12\sin(2k r_s).
$$

Thus recombination-era EE maxima lie roughly between TT maxima, while TE alternates sign. Planck’s first clear EE maxima are near

$$
\ell=398.3\pm1.0,
\qquad
690.4\pm1.2,
\qquad
993.1\pm1.8.
$$

These formulae are phase mnemonics, not precision spectra. A Boltzmann solver integrates a finite visibility function with metric, plasma, neutrino, and projection sources. The E/B decomposition and full-sky polarization transfer are developed by [Zaldarriaga and Seljak](https://doi.org/10.1103/PhysRevD.55.1830); the acoustic/polarization logic is reviewed by [Hu and White](https://arxiv.org/abs/astro-ph/9706147).

The phase relation carries more information than TT peak spacing alone. A continuing stochastic source generally loses the sharply synchronized growing-mode phase. [[compatible-with-existing-physics/passive-adiabatic-transfer|Passive adiabatic transfer]] therefore requires a proposal to control the curvature mode, its conjugate momentum, decaying modes, and any active source before it inherits the standard peaks.

## The transfer, damping, and lensing filters

The line-of-sight solution has the form

$$
\Delta_\ell^X(k)
=
\int_0^{\eta_0}
\mathrm d\eta\,
S_X(k,\eta)
j_\ell[k(\eta_0-\eta)],
$$

and a statistically isotropic scalar curvature spectrum produces

$$
C_\ell^{XY}
=
4\pi\int\mathrm d\ln k\,
\mathcal P_\zeta(k)
\Delta_\ell^X(k)
\Delta_\ell^Y(k).
$$

This is the actual spectrometer response: a feature at one (k) is broadened and projected into a range of multipoles, differently for each (XY). The line-of-sight method was introduced by [Seljak and Zaldarriaga](https://doi.org/10.1086/177793).

Photon diffusion further suppresses small scales approximately as

$$
D(k,\eta_*)
\longmapsto
D(k,\eta_*)e^{-k^2/k_D^2},
$$

while the finite width of the visibility function adds smoothing. Weak gravitational lensing remaps the primary sky,

$$
\widetilde X(\hat{\mathbf n})
=
X\!\left(\hat{\mathbf n}+\nabla\phi\right),
$$

smoothing peaks, correlating modes, and converting some E into B. Any primordial grain template has to pass through these filters; fitting a sinusoid directly to the already-lensed (D_\ell) curve is not a forward model.

## What “dwell” contributes

A classical oscillator with coordinate (Q=A\cos\theta) and uniform phase spends a fraction

$$
p(Q)\,\mathrm dQ
=
\frac{\mathrm dQ}{\pi\sqrt{A^2-Q^2}}
$$

near (Q). The density is largest at the turning points (Q=\pm A), where the velocity vanishes. This gives a legitimate local meaning to the phrase **acoustic dwell**:

- TT preferentially sees modes at displacement/compression extrema;
- EE preferentially sees the velocity quadrature; and
- TE says which quadrant of phase space is being sampled.

But the observed (C_\ell) is not (p(Q)). It is a spatial ensemble covariance at one last-scattering epoch, integrated over a continuum of (k), then projected and lensed. Acoustic dwell is an interpretation of the phase geometry. Born dwell for a cosmic wavefunction is a different measure that still needs a map into (mathcal P_\zeta).

## The observed baseline

Planck determines the angular acoustic scale to about (0.03\%) in base (Lambda)CDM and finds its temperature, polarization, and lensing spectra mutually consistent with that model; see [Planck 2018 VI](https://doi.org/10.1051/0004-6361/201833910). Its dedicated searches find no significant primordial feature after accounting for the search freedom; see [Planck 2018 X](https://doi.org/10.1051/0004-6361/201833887).

ACT DR6 independently measures TT, TE, and EE to arcminute scales and reports that its spectra are well fit by CMB plus foregrounds with a (Lambda)CDM CMB component. The joint Planck--ACT acoustic scale reaches roughly (0.02\%) precision; see the [ACT DR6 power-spectrum analysis](https://arxiv.org/abs/2503.14452).

The repository’s P-ACT best-fit theory file contains the expected harmonic comb. A simple local-extremum receipt finds, for example,

$$
\ell_{\mathrm{TT,max}}
=
(221,537,813,1127,1422,1726,2010),
$$

and the recombination branch of

$$
\ell_{\mathrm{EE,max}}
=
(395,688,990,1299,1608,1920,2230,2537,2832).
$$

Those numbers come from a best-fit theoretical product, not from a new data reduction and not from a causal-grain fit. Their role is to verify the standard phase scaffold against which a residual model must be tested.

## What a causal explanation must add

Matching a mean peak spacing does not explain this resonator. A causal-scale model must choose one of two routes:

1. **Initial-state route:** derive (mathcal P_{IJ}(k)), the growing-mode phase, and any higher-point functions, then use the established transfer kernels.
2. **Dynamical route:** alter the metric/plasma equations and jointly predict the scale-dependent phase shift, baryon response, driving, damping, recombination, lensing, and polarization.

A credible signal must be common across TT, TE, and EE after their different kernels are applied, survive foreground-frequency tests, agree between Planck and ACT without double-counting overlapping sky, pay the global look-elsewhere penalty, and predict at least one held-out statistic. A TT-only numerical rhyme is not cosmic spectroscopy.

## Why the Planck comparison is methodological

Max Planck’s quantum entered through the blackbody energy law. Atomic line spectroscopy was a related later arena, but it was not the evidence from which he originally inferred (E=h\nu). The CMB also has two different spectra that must not be conflated:

- its photon-frequency spectrum is an extraordinarily accurate (2.725\,mathrm K) blackbody; and
- its anisotropy spectrum is angular covariance versus multipole (ell).

The useful analogy is inverse response: infer hidden structure from a calibrated spectrum. The causal grain, if real, would be the source of an additional correlated residual, not the explanation for why a classical fluid in a finite sound horizon has harmonics.
