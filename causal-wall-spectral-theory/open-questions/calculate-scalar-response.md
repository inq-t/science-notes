# Calculate the Scalar Response

CWST becomes a scalar-spectrum theory only when a microscopic wall member independently calculates its positive spin-zero or equivalent response function, including amplitude and scale dependence. Inferring that function from the measured \(A_s\), \(n_s\), or \(\alpha_s\) is calibration, not completion.

## Required calculation

A completed member should return

$$
\mathcal K^{\mathrm{calc}}_\zeta(k)
$$

on the physical quotient. In the optional holographic realization this may be expressed as

$$
c_{\mathrm{calc}}^{(0)}(k),
\qquad
\mathcal K^{\mathrm{calc}}_\zeta(k)
=\frac{\pi^2}{8}c_{\mathrm{calc}}^{(0)}(k)k^3.
$$

The member must calculate the normalization, not merely the degree-three factor. Near-critical language must be backed by a flow equation, operator mixing, and a controlled distance from a fixed point. The strict trace-fixed-point obstruction in [[critical-scale-kernels/trace-fixed-point-null-no-go|the null no-go]] must be addressed by a deformation, double scaling, or different operator rather than by inverting a zero response.

## Upgrade test

An upgrade requires a declared algebra and state, renormalized source, response calculation, physical continuation, and predictions for at least one observable not used to select the member. A robust amplitude plus a derived relation among tilt, running, and another response channel would be materially stronger than a fitted power law.

## Failure

The member fails if its calculated response is negative on a required physical mode, singular without a justified quotient, dependent on arbitrary counterterm data that enter observables, or incompatible with the scalar likelihood. An unrestricted positive-function interface survives such a member failure but remains nonpredictive by [[critical-scale-kernels/unrestricted-response-no-go|the unrestricted-response no-go]].

