# Conformal Time

Conformal time is the cosmological time coordinate $\eta$ defined by $\mathrm d\eta=\mathrm dt/a(t)$, where $t$ is cosmic proper time and $a(t)$ is the scale factor. In this coordinate an FLRW metric takes the form $g=a^2(\eta)\widetilde g$, with all explicit expansion carried by one overall conformal factor. Radial light rays then satisfy $\mathrm d\chi=\pm c\,\mathrm d\eta$, so conformal-time intervals directly measure comoving light-travel distances. This makes causal horizons, cosmological distances, perturbation equations, and quantum fields in an expanding universe much easier to analyze. Conformal time is not the elapsed time on a physical clock, and a finite conformal-time boundary need not occur at finite proper time.

## Definition

Write the FLRW line element as

$$
\mathrm ds^2
=-c^2\mathrm dt^2+a^2(t)\,\mathrm d\Sigma_K^2,
$$

where $\mathrm d\Sigma_K^2$ is a time-independent metric of constant spatial curvature. Define

$$
\eta(t)-\eta_*
=\int_{t_*}^{t}\frac{\mathrm dt'}{a(t')},
\qquad
\mathrm d\eta=\frac{\mathrm dt}{a(t)}.
$$

Then

$$
\mathrm ds^2
=a^2(\eta)
\left[-c^2\mathrm d\eta^2+\mathrm d\Sigma_K^2\right].
$$

This convention takes $a$ to be dimensionless, so $t$ and $\eta$ both have units of time. Authors who give $a$ dimensions of length may instead give $\eta$ dimensions of inverse velocity or set $c=1$ from the start. The defining integral, rather than dimensional shorthand, fixes the convention.

The additive constant $\eta_*$ is arbitrary. Common choices put the big bang at $\eta=0$, the present at $\eta=0$, or the future boundary of an inflationary patch at $\eta=0^-$. Only differences of conformal time have direct coordinate significance.

## Coordinate change versus conformal rescaling

Two operations are often displayed in the same equation:

1. Replacing $t$ with $\eta$ is a coordinate change on the same physical spacetime.
2. Replacing $g$ with $\widetilde g=a^{-2}g$ is a conformal rescaling to a different metric representative.

The first operation does not change the metric geometry; it only relabels events. The second changes lengths and clock rates but preserves null cones and unparametrized null geodesics. This preservation of causal directions is the standard geometric content of [[causal-order|conformal structure and metric scale]].

For spatially flat FLRW,

$$
\widetilde g
=-c^2\mathrm d\eta^2+\mathrm d\mathbf x^2
$$

is the Minkowski metric. The physical spacetime is therefore conformal to Minkowski space even though it is generally curved. Factoring out $a^2$ does not eliminate expansion, redshift, curvature, or gravitational dynamics; those reappear through the scale factor and its derivatives.

## Relation to physical clocks

For an observer comoving with the cosmological fluid, $\mathrm d\mathbf x=0$, and the observer's proper time is

$$
\mathrm d\tau=\mathrm dt=a(\eta)\,\mathrm d\eta.
$$

Thus one unit of $\eta$ represents different amounts of proper time at different epochs. For a noncomoving timelike worldline, spatial motion contributes as well:

$$
c^2\mathrm d\tau^2
=a^2(\eta)
\left(c^2\mathrm d\eta^2-\mathrm d\ell_{\rm com}^2\right).
$$

Conformal time is consequently a coordinate adapted to causal propagation, not the reading of a universal physical clock.

## Derivative dictionary

Let overdots denote $\mathrm d/\mathrm dt$ and primes denote $\mathrm d/\mathrm d\eta$. For any homogeneous quantity $X$,

$$
X'=a\dot X.
$$

The conformal Hubble parameter is

$$
\mathcal H:=\frac{a'}a=aH,
\qquad
H:=\frac{\dot a}{a}.
$$

With the deceleration parameter $q=-a\ddot a/\dot a^2$,

$$
\mathcal H'=-q\mathcal H^2,
\qquad
\frac{a''}{a}=(1-q)\mathcal H^2.
$$

These identities are kinematic. They do not require Einstein's field equation or a particular matter model. Further identities using the inverse scale $\sigma=1/a$ are collected in [[flrw-kinematics|FLRW scale-section kinematics]].

Conformal time and [[misner-log-time|Misner logarithmic time]] emphasize different aspects of expansion. If $\Omega=-\ln(a/a_*)$, then

$$
\frac{\mathrm d\Omega}{\mathrm d\eta}=-\mathcal H,
\qquad
\mathrm d\eta=-\frac{\mathrm d\Omega}{\mathcal H}.
$$

Equal increments of $\Omega$ are equal scale-factor ratios; equal increments of $\eta$ are equal comoving light-travel times.

## Why light propagation becomes simple

For a radial path, write the spatial line element as $\mathrm d\Sigma_K^2=\mathrm d\chi^2$. A null ray has $\mathrm ds^2=0$, hence

$$
\frac{\mathrm d\chi}{\mathrm d\eta}=\pm c.
$$

In a diagram with axes $(\eta,\chi/c)$, radial light rays therefore run at $45^\circ$. Their paths have the same coordinate form as in Minkowski space. The conformal factor changes physical wavelengths, energies, distances, and affine parametrization, but not the null curves themselves.

Light emitted at $\eta_e$ and received at $\eta_0$ travels the comoving radial distance

$$
\chi=c(\eta_0-\eta_e)
=c\int_{t_e}^{t_0}\frac{\mathrm dt}{a(t)}.
$$

This integral is the starting point for cosmological distance-redshift relations. Spatial curvature and factors of $a$ then convert $\chi$ into angular-diameter, luminosity, or proper distance.

## Horizons and causal structure

Suppose the FLRW solution has an initial conformal endpoint $\eta_i$ and a future endpoint $\eta_f$. At time $\eta$, the comoving particle-horizon radius is

$$
\chi_{\rm particle}(\eta)=c(\eta-\eta_i),
$$

provided the past integral converges. The comoving event-horizon radius is

$$
\chi_{\rm event}(\eta)=c(\eta_f-\eta),
$$

provided the future integral converges. A particle horizon asks which events could already have influenced the observer; an event horizon asks which events can ever influence the observer. Their existence is controlled by the convergence of $\int \mathrm dt/a(t)$ at the relevant endpoint.

Neither horizon should be confused with the comoving Hubble radius

$$
r_{H,{\rm com}}=\frac{c}{aH}=\frac{c}{\mathcal H}.
$$

The Hubble radius is a local expansion scale, not generally a causal boundary. Its conformal-time derivative is

$$
r_{H,{\rm com}}'=cq.
$$

It shrinks during accelerated expansion ($q<0$), which is why inflation can move Fourier modes from $k\gg\mathcal H$ to $k\ll\mathcal H$. The phrase “horizon crossing” often means $k=\mathcal H$, or crossing the comoving Hubble radius, rather than crossing a particle or event horizon.

## Standard expansion histories

For a power-law universe $a(t)\propto t^p$,

$$
\eta\propto
\begin{cases}
t^{1-p}, & p\ne1,\\
\ln t, & p=1.
\end{cases}
$$

After choosing origins and normalizations, familiar cases become

| Background | Cosmic-time form | Conformal-time form |
|---|---|---|
| Radiation domination | $a\propto t^{1/2}$ | $a\propto\eta$ |
| Matter domination | $a\propto t^{2/3}$ | $a\propto\eta^2$ |
| de Sitter expansion | $a\propto e^{Ht}$ | $a=-1/(H\eta)$, with $\eta<0$ |

In radiation- and matter-dominated big-bang models, it is conventional to put the singularity at $\eta=0^+$. In the expanding flat patch of de Sitter spacetime, infinite future proper time corresponds to the finite limit $\eta\to0^-$. This is the simplest demonstration that a finite conformal-time endpoint need not be a physical singularity or an event inside spacetime.

## How conformal time is used

### Causal and conformal diagrams

Because null lines are simple, one can identify which regions communicate by inspecting intervals in $\eta$. Penrose diagrams add further compactifying coordinate transformations so that infinite coordinate ranges fit in a finite diagram. Conformal time prepares an FLRW metric for this analysis, but conformal time by itself is not a compactification.

### Cosmological perturbation theory

Perturbed metrics are commonly written with the scale factor outside the entire line element. In conformal Newtonian gauge, for example,

$$
\mathrm ds^2=a^2(\eta)
\left[-(1+2\Psi)c^2\mathrm d\eta^2
+(1-2\Phi)\mathrm d\mathbf x^2\right].
$$

Fourier modes then compare naturally with the conformal expansion rate $\mathcal H$. In units $c=1$, the canonically normalized scalar perturbation often obeys the Mukhanov--Sasaki equation

$$
v_k''+
\left(c_s^2k^2-\frac{z''}{z}\right)v_k=0,
$$

while a canonically normalized tensor mode has the schematic form

$$
\mu_k''+
\left(k^2-\frac{a''}{a}\right)\mu_k=0.
$$

These look like flat-space oscillator equations with time-dependent effective potentials. This form makes the sub-Hubble oscillatory regime, amplification near Hubble crossing, and super-Hubble evolution comparatively transparent.

### Relativistic kinetic theory and the cosmic microwave background

Photon and neutrino trajectories are naturally evolved per unit $\eta$, and the Boltzmann, Einstein, and fluid equations share the same conformal-time coordinate. Modern CMB calculations inherit this organization: comoving wave numbers are compared with $\mathcal H$, while photon travel distances are differences in $\eta$.

### Quantum fields in expanding spacetime

For a scalar field in spatially flat FLRW, rescaling a Fourier mode by the scale factor turns its equation into an oscillator equation. In units $c=\hbar=1$, a mode $u_k=a\phi_k$ with mass $m$ and curvature coupling $\xi$ satisfies

$$
u_k''+
\left[
k^2+a^2m^2+(6\xi-1)\frac{a''}{a}
\right]u_k=0.
$$

For a massless conformally coupled scalar, $m=0$ and $\xi=1/6$, the explicit expansion term cancels. For minimally coupled or massive fields it does not. Conformal flatness therefore simplifies field theory, but it does not make every field conformally invariant or eliminate cosmological particle creation.

## Limitations and common mistakes

- **Conformal time is not proper time.** For comoving clocks, $\Delta t=\int a\,\mathrm d\eta$, not simply $\Delta\eta$.
- **The zero and sign of $\eta$ are conventional.** Inflationary calculations often use negative $\eta$ increasing toward zero; late-time calculations often use positive $\eta$ measured from the big bang.
- **A finite conformal boundary is not necessarily a spacetime event.** It may represent infinite proper time, as in de Sitter future infinity.
- **The transformation can fail at $a=0$.** Writing the singular surface at a finite or infinite $\eta$ does not extend the physical metric through it.
- **Straight null lines do not mean no redshift.** The conformal factor leaves the path unchanged while changing physical frequency and wavelength.
- **Null geodesics are not generally affinely parametrized by $\eta$.** Conformal transformations preserve their unparametrized trajectories, not their affine parameters.
- **The Hubble radius is not automatically a horizon.** Causal horizons depend on integrals over the full expansion history.
- **Scale-factor normalization affects coordinate conventions.** Rescaling $a$ and the comoving spatial coordinates changes the numerical normalization of $\eta$ while leaving physical observables invariant.

## Sources

- W. Rindler, [“Visual Horizons in World Models”](sources/1956-rindler-visual-horizons-in-world-models.pdf) (1956; [publisher record](https://doi.org/10.1093/mnras/116.6.662)): the foundational distinction between particle and event horizons in Robertson--Walker cosmology.
- Roger Penrose, [“Asymptotic Properties of Fields and Space-Times”](sources/1963-penrose-asymptotic-properties-fields-spacetimes.pdf) (1963; [publisher record](https://doi.org/10.1103/PhysRevLett.10.66)): the conformal treatment of causal infinity underlying conformal diagrams.
- Leonard Parker, [“Quantized Fields and Particle Creation in Expanding Universes. I”](sources/1969-parker-quantized-fields-particle-creation-i.pdf) (1969; [publisher record](https://doi.org/10.1103/PhysRev.183.1057)): quantum fields and particle creation in a spatially flat expanding universe.
- Chung-Pei Ma and Edmund Bertschinger, [“Cosmological Perturbation Theory in the Synchronous and Conformal Newtonian Gauges”](sources/1995-ma-bertschinger-cosmological-perturbation-theory.pdf) (1995; [repository record](https://arxiv.org/abs/astro-ph/9506072)): conformal-time Einstein--Boltzmann perturbation equations used in CMB and structure calculations.
