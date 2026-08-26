# The Primordial Observable Interface

Any proposed origin of cosmic correlations must eventually return gauge-invariant scalar and tensor observables with a Lorentzian state, constrained dynamics, matching data, and a calculable correlation hierarchy. This is an observable-representation obligation: a whole-state or boundary account need not repeat the usual microscopic story, but a positive spatial covariance alone is not yet a cosmological perturbation theory.

## What has to be represented

Write a scalar perturbation of a spatially flat FLRW metric, in one common convention, as

$$
\mathrm ds^2
=-(1+2A)\,\mathrm dt^2
+2a\,\partial_iB\,\mathrm dt\,\mathrm dx^i
+a^2\left[(1-2\psi)\delta_{ij}
+2\partial_i\partial_jE\right]\mathrm dx^i\mathrm dx^j.
$$

The four displayed functions are not four propagating scalar degrees of freedom. A time shift and scalar spatial diffeomorphism change them, while the lapse and shift impose constraints. A candidate primordial variable must therefore be related to a declared gauge-invariant quantity after those redundancies and constraints have been handled. Typical curvature variables are

$$
\zeta_{\mathrm{ud}}
:=-\psi-H\frac{\delta\rho}{\dot\rho},
\qquad
\mathcal R
:=\psi-H\frac{\delta q}{\rho+p},
$$

with signs depending on the metric convention. Agreement of a proposed symbol with the letter \(\zeta\) does not provide this relation.

The standard benchmark is the gauge-invariant constrained construction represented by [[library/quantum-theory-of-gauge-invariant-cosmological-perturbations/entry|Mukhanov, Feldman, and Brandenberger]]. In a single-clock realization it can reduce to an action of the schematic form

$$
S^{(2)}
=\frac12\int \mathrm d\eta\,\mathrm d^3x\,
z^2\left[(\zeta')^2-c_s^2(\nabla\zeta)^2\right].
$$

This display is a benchmark, not a universal premise. A multi-field, constrained, nonlocal, modified-gravity, or boundary realization may have a different reduced phase space and kinetic operator. It must nevertheless state enough Lorentzian structure to decide which modes propagate, which are constrained, whether the initial-value problem is well posed, and which equal-time field is observed.

## Minimal return type

A complete interface should return at least

$$
\mathfrak P
=\bigl(
\mathcal P_{\mathrm{red}},
\Omega_{\mathrm{red}},
\mathcal E_{\mathrm L},
\omega_{\mathrm L},
\mathcal M_{\mathrm{hot}},
\mathcal O_{\mathrm{late}}
\bigr),
$$

where:

| Slot | Required content |
|---|---|
| \(\mathcal P_{\mathrm{red}}\) | the gauge-reduced scalar and tensor phase space, including treatment of zero modes |
| \(\Omega_{\mathrm{red}}\) | symplectic form or equivalent canonical normalization |
| \(\mathcal E_{\mathrm L}\) | Lorentzian equations, constraints, causal characteristics, and stability conditions |
| \(\omega_{\mathrm L}\) | the state or boundary prescription that fixes the correlation functions |
| \(\mathcal M_{\mathrm{hot}}\) | matching through reheating or any wall-to-geometric transition into the hot universe |
| \(\mathcal O_{\mathrm{late}}\) | the map to CMB, lensing, structure, or gravitational-wave observables |

This package is **[CONSTRUCTION AXIOM]** for any programme that claims primordial observable adequacy. Established cosmology supplies realizations of it under familiar field-content and background assumptions. A new theory may import such a realization or replace it, but it cannot omit the slots while claiming the same observables.

## A spatial precision is only one slot

An equal-time connected covariance and its inverse satisfy

$$
\mathcal K_\zeta
=\mathcal C_\zeta^{-1}
$$

on a declared nondegenerate physical subspace. This is useful data about the state. It does not by itself supply

- a Lorentzian kinetic term or symplectic structure;
- lapse and shift constraints;
- hyperbolicity, sound cones, or absence of ghosts;
- reflection positivity or unitarity;
- the decaying-mode or conjugate-momentum initial condition;
- tensors and their coupling to the scalar sector; or
- higher-point Ward identities and a consistent in-in contour.

The distinction is especially important for boundary and whole-state formulations. A boundary functional may encode a late-time wavefunctional, but the map from that object to expectation values depends on the state, analytic continuation, contour, and contact or semilocal terms. [[library/operator-dictionaries-and-wave-functions-in-ads-cft-and-ds-cft/entry|Harlow and Stanford]] exhibit this distinction in a controlled holographic setting, while [[library/quantum-contributions-to-cosmological-correlations/entry|Weinberg's in-in construction]] gives the standard Lorentzian benchmark.

## Scalar, tensor, and higher-point obligations

The scalar interface must prove which wall, boundary, or state-space direction becomes \(\zeta_{\mathrm{ud}}\) or \(\mathcal R\), and with what normalization. The tensor interface must independently return the transverse-traceless modes, their state, and their power; a scalar response coefficient does not determine them.

Beyond quadratic order, connected source derivatives, higher derivatives of relative entropy, wavefunctional coefficients, probability 1PI vertices, and Lorentzian correlators are differently typed objects. Their maps must be supplied. The standard single-clock squeezed relation is conditional on an adiabatic mode, locality, an appropriate state, and the relevant Ward identity; [[library/non-gaussian-features-of-primordial-fluctuations-in-single-field-inflationary-models/entry|Maldacena]] and [[library/an-infinite-set-of-ward-identities-for-adiabatic-modes-in-cosmology/entry|Hinterbichler, Hui, and Khoury]] state controlled versions of these assumptions.

## Two legitimate completion routes

**Imported-transfer route.** The new theory identifies and normalizes a passive gauge-invariant primordial mode, then proves matching into ordinary GR plus local QFT or kinetic theory. Standard Einstein--Boltzmann transfer can then be reused. This is conservative local restriction, not derivation of the local fibers.

**End-to-end alternative.** The new theory supplies its own causal evolution and calculates the same measured records. It need not use the standard variables internally, but it must exhibit an empirically equivalent observable map in the overlap regime.

Either route is stronger than fitting a positive function to an observed power spectrum. [[passive-adiabatic-transfer|Passive adiabatic transfer]] isolates the additional conditions under which the imported route is valid.

## Failure conditions

The interface fails if the proposed primordial data cannot be assigned to a gauge-invariant physical mode, if the Lorentzian system has an ill-posed or unstable initial-value problem, if state or matching data leave arbitrary observable phases, if scalar and tensor constraints are inconsistent, or if the resulting correlation hierarchy violates the local conservation, analyticity, unitarity, or gauge conditions of the claimed observational regime.

