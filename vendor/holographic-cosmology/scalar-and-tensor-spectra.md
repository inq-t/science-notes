# Scalar and Tensor Spectra

Within a declared domain-wall/cosmology member, the primordial scalar and tensor powers are inverse continued stress responses. The normalization identities are exact after the response convention is fixed, but a response inferred from observed power is only a target; a prediction requires the same quantity to be calculated independently from the dual QFT.

## Cosmological conventions

For the gauge-invariant curvature perturbation \(\zeta\), define

$$
\langle\zeta_{\mathbf k}\zeta_{\mathbf k'}\rangle
=(2\pi)^3\delta^{(3)}(\mathbf k+\mathbf k')P_\zeta(k),
\qquad
\Delta_\zeta^2(k)
:=\frac{k^3}{2\pi^2}P_\zeta(k).
$$

On the physical nonzero-mode subspace,

$$
\boxed{
\mathcal K_\zeta(k)
:=P_\zeta(k)^{-1}
=\frac{k^3}{2\pi^2\Delta_\zeta^2(k)}.}
$$

This is the exact inverse-covariance definition. In a non-Gaussian theory it is the two-point probability-1PI kernel, not necessarily the raw quadratic coefficient of an arbitrarily chosen probability density.

## Continued QFT response

Let \(A_{\mathrm{calc}}\) and \(B_{\mathrm{calc}}\) be independently computed in a Euclidean QFT member and continued according to [[vendor/holographic-cosmology/analytic-continuation-and-state|the registered prescription]]. Define the positive cosmological responses

$$
\rho_{B,\mathrm{calc}}^{\mathrm{cos}}(k)
:=-\operatorname{Im}B_{\mathrm{cont}}(-ik)>0,
$$

$$
\rho_{A,\mathrm{calc}}^{\mathrm{cos}}(k)
:=-\operatorname{Im}A_{\mathrm{cont}}(-ik)>0.
$$

Then the McFadden--Skenderis dictionary is

$$
\boxed{
\Delta_\zeta^2(k)
=\frac{k^3}
{16\pi^2\rho_{B,\mathrm{calc}}^{\mathrm{cos}}(k)},
\qquad
\Delta_T^2(k)
=\frac{2k^3}
{\pi^2\rho_{A,\mathrm{calc}}^{\mathrm{cos}}(k)}.}
$$

Equivalently,

$$
\boxed{
\mathcal K_\zeta(k)
=8\rho_{B,\mathrm{calc}}^{\mathrm{cos}}(k).}
$$

These are **[CONDITIONAL THEOREM]** statements: applicability requires the declared holographic member and continuation, while the displayed normalization algebra is exact.

## Spectral-function convention

Define dimensionless spin-zero and spin-two spectral responses by

$$
\rho_B^{\mathrm{cos}}(k)
:=\frac{\pi^2}{64}c^{(0)}(k)k^3,
\qquad
\rho_A^{\mathrm{cos}}(k)
:=\frac{\pi^2}{16}c^{(2)}(k)k^3.
$$

It follows that

$$
\boxed{
\Delta_\zeta^2(k)
=\frac{4}{\pi^4c^{(0)}(k)},
\qquad
\Delta_T^2(k)
=\frac{32}{\pi^4c^{(2)}(k)},}
$$

and

$$
\boxed{
r(k):=\frac{\Delta_T^2}{\Delta_\zeta^2}
=8\frac{c^{(0)}(k)}{c^{(2)}(k)}.}
$$

These coefficients are translated into the current programme by [[causal-wall-spectral-theory/holographic-spectral-adapter|the optional CWST holographic adapter]] and agree with the spectral representation in [[library/on-the-power-spectrum-of-inflationary-cosmologies-dual-to-a-deformed-cft/entry|McFadden's deformed-CFT calculation]]. The quantity \(c^{(0)}\) is a spin-zero trace response. It is not automatically a fixed-point central charge or a microscopic degree-of-freedom count.

## Target is not return value

**[DEFINITION]** Data can be translated into target functions,

$$
\rho_{B,\mathrm{targ}}^{\mathrm{cos}}(k)
:=\frac{k^3}{16\pi^2\Delta_{\zeta,\mathrm{obs}}^2(k)},
\qquad
\rho_{A,\mathrm{targ}}^{\mathrm{cos}}(k)
:=\frac{2k^3}{\pi^2\Delta_{T,\mathrm{obs}}^2(k)}.
$$

A holographic member becomes predictive only when it independently calculates return values satisfying the empirical comparison

$$
\rho_{B,\mathrm{calc}}^{\mathrm{cos}}
\stackrel{\mathrm{test}}{=}
\rho_{B,\mathrm{targ}}^{\mathrm{cos}},
\qquad
\rho_{A,\mathrm{calc}}^{\mathrm{cos}}
\stackrel{\mathrm{test}}{=}
\rho_{A,\mathrm{targ}}^{\mathrm{cos}}.
$$

Defining \(c^{(0)}\) from the measured scalar amplitude and substituting it back into the spectrum verifies normalization only. It does not calculate the QFT response.

## Tilt and running

Where the dictionary applies,

$$
n_s-1
=-\frac{\mathrm d\ln c^{(0)}}{\mathrm d\ln k},
\qquad
\alpha_s
=-\frac{\mathrm d^2\ln c^{(0)}}
{\mathrm d(\ln k)^2}.
$$

These are logarithmic identities, not a beta function for an unspecified theory. A power-law ansatz for \(c^{(0)}\) gives zero running by assumption. A microscopic prediction of tilt or running requires an independently calculated QFT flow, such as the deformed-CFT example in the local primary source above.
