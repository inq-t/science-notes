# Passive Adiabatic Transfer

A common local clock makes relative density isocurvature vanish at linear order, but conservation of the total curvature mode and coherent late-time transfer require further dynamical and matching hypotheses. This note states that conditional theorem once so that whole-state, boundary, and early-universe proposals can import it without treating “rank one” or one scalar covariance as a complete perturbation theory.

## Common-clock lemma

Let every relevant material background quantity be evaluated on one local clock displacement \(\delta N(x)\):

$$
\rho_i(x)=\bar\rho_i\bigl(N+\delta N(x)\bigr).
$$

At first order,

$$
\delta\rho_i=\bar\rho_i'\,\delta N.
$$

Using the convention

$$
\zeta_i:=-\psi-\frac{\delta\rho_i}{\bar\rho_i'},
$$

all species have the same curvature perturbation,

$$
\zeta_i=-\psi-\delta N,
\qquad
S_{ij}:=3(\zeta_i-\zeta_j)=0.
$$

This is **[EXACT — AFTER REDUCTION]**: it follows algebraically from the granted common-clock ansatz and the stated linear convention. It does not show that a proposed wall theory has only one material clock, that its scalar is the metric curvature mode, or that interactions preserve the reduction.

## Relative adiabaticity is not the whole condition

The equality \(S_{ij}=0\) removes relative density isocurvature. It does not by itself imply that the total nonadiabatic pressure vanishes. That stronger statement requires control of

- intrinsic entropy perturbations within each component;
- non-barotropic pressures and non-attractor modes;
- energy exchange among components;
- relative velocities and anisotropic stress;
- constrained or additional gravitational degrees of freedom; and
- any transition between the proposed primordial description and the hot universe.

Under the usual conservation and regularity hypotheses, the long-wavelength evolution is

$$
\frac{\mathrm d\zeta_{\mathrm{ud}}}{\mathrm dN}
=-\frac{\delta p_{\mathrm{nad}}}{\rho+p}
+\mathcal O\!\left(\frac{k^2}{a^2H^2}\right).
$$

Hence \(\delta p_{\mathrm{nad}}=0\) gives a conserved physical curvature mode outside the horizon. This is **[STANDARD — UNDER THE DECLARED HYPOTHESES]**, as developed by [[library/a-new-approach-to-the-evolution-of-cosmological-perturbations-on-large-scales/inq|Wands, Malik, Lyth, and Liddle]]. [[library/adiabatic-modes-in-cosmology/inq|Weinberg's adiabatic-mode theorem]] separately requires the long-wavelength solution and gauge transformation to be regular; it does not say that every formal zero-momentum gauge mode is the physical growing mode.

## Passive and coherent initial data

The standard transfer functions apply to passive initial data: the primordial mechanism fixes the mode before the subsequent plasma evolution, and no continuing incoherent source repeatedly resets its phase. The growing solution and its conjugate momentum must be selected so that an uncontrolled decaying mode is absent or bounded. A wall-to-metric or reheating transition must preserve the induced metric, constraints, and whatever matching data the chosen dynamics requires.

Once those conditions are met, ordinary Einstein--Boltzmann evolution gives, at linear order,

$$
C_\ell^{XY}
=4\pi\int \mathrm d\ln k\,
\Delta_\zeta^2(k)
\Theta_\ell^X(k)\Theta_\ell^Y(k).
$$

The transfer kernels \(\Theta_\ell^X\) are inherited from the imported local gravitational, plasma, and kinetic theory. The equation is a deterministic linear propagation of correlation data; it does not decide whether the primordial covariance represents ontic indeterminacy, an ensemble, a whole-state expectation, or inaccessible determining reason.

Acoustic coherence therefore tests more than the scalar power amplitude. A model that specifies only \(\Delta_\zeta^2(k)\) but leaves the momentum, decaying mode, or ongoing source arbitrary has not earned the standard coherent peaks.

## Nonlinear boundary

At higher order, one common clock can support the familiar separate-universe and soft-limit reasoning only under additional locality, attractor, state, and Ward-identity assumptions. It does not force the full bispectrum or trispectrum, and it does not identify derivatives of a state divergence with cosmological 1PI vertices. Those distinctions are owned by [[basic-concepts/hessians/higher-relative-entropy-is-not-cumulants|the higher-Hessian no-go]] and [[compatible-with-existing-physics/primordial-observable-interface|the primordial observable interface]].

## Upgrade and failure tests

A new primordial proposal may import passive adiabatic transfer after it provides:

1. a gauge-invariant physical scalar and its canonical normalization;
2. the common-clock or other proof that relative entropy modes are absent;
3. a proof that intrinsic nonadiabatic pressure is absent or sufficiently suppressed;
4. passive growing-mode state and momentum data;
5. controlled matching into the standard thermal history; and
6. the tensors and higher correlations required by the claimed observables.

The imported route fails if a surviving entropy mode sources curvature, a transition excites an uncontrolled decaying or incoherent component, the standard constraints are not preserved, or the late-time records cannot be calculated from the proposed primordial data.

