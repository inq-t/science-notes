# CWST Empirical Targets

Current observations provide target scalar and tensor correlation functions against which a calculated CWST member can be tested. The archived v3 numbers are useful normalization receipts, but none is a prediction when the measured amplitude, tilt, or tensor bound is inserted to define the response coefficient.

## Data-inferred targets

Fix the Fourier convention

$$
\langle\zeta_{\mathbf k}\zeta_{\mathbf k'}\rangle
=(2\pi)^3\delta^{(3)}(\mathbf k+\mathbf k')P_\zeta(k),
\qquad
\Delta_\zeta^2(k)=\frac{k^3}{2\pi^2}P_\zeta(k).
$$

The measured scalar power defines

$$
\mathcal K^{\mathrm{target}}_\zeta(k)
=\frac{k^3}{2\pi^2\Delta_{\zeta,\mathrm{obs}}^2(k)}.
$$

Within the optional holographic normalization, it also defines the target coefficient

$$
c_{\mathrm{target}}^{(0)}(k)
=\frac{4}{\pi^4\Delta_{\zeta,\mathrm{obs}}^2(k)}.
$$

These are **[DEFINITION]** values inferred from data. A wall member must instead calculate \(\mathcal K^{\mathrm{calc}}_\zeta\) or \(c_{\mathrm{calc}}^{(0)}\) from its independently selected algebra, state, transport, and response law.

## Archived v3 calibration

At \(k_*=0.05\,\mathrm{Mpc}^{-1}\), v3 used

$$
\ln(10^{10}A_s)=3.044,
\qquad
A_s=2.098903\times10^{-9}.
$$

The registered algebra then gives

$$
\mathcal I_{\zeta,\mathrm{target}}(k_*)
=A_s^{-1}
=4.764393\times10^8,
$$

$$
c_{\mathrm{target}}^{(0)}(k_*)
=\frac{4}{\pi^4A_s}
=1.956447\times10^7.
$$

Using the archived BK18 bound \(r_{0.05}<0.036\) gives, in the same conventions,

$$
\frac{c_{\mathrm{target}}^{(2)}}
{c_{\mathrm{target}}^{(0)}}>222.2,
\qquad
\frac{\mathcal K_{\gamma,\mathrm{target}}}
{\mathcal K_{\zeta,\mathrm{target}}}>55.6
$$

for one tensor polarization in the second ratio. These are **[RECEIPT]** consequences of reported inputs. The local [[library/planck-2018-results-x-constraints-on-inflation/entry|Planck inflation analysis]], [[library/bicep-keck-2018-primordial-gravitational-waves/entry|BK18 analysis]], [[data/planck-2018-release-3-cosmology-products/entry|Planck data products]], and [[data/bicep-keck-2018-data-products/entry|BK18 data products]] document that calibration. They should not be described as current universal constants or as independent CWST successes.

## Shape targets

The exact logarithmic identities in [[critical-scale-kernels/tilt-and-running-identities|the tilt note]] translate a calculated response into

$$
n_s-1
=-\frac{\mathrm d\ln c_{\mathrm{calc}}^{(0)}}
{\mathrm d\ln k},
\qquad
\alpha_s
=-\frac{\mathrm d^2\ln c_{\mathrm{calc}}^{(0)}}
{\mathrm d(\ln k)^2}
$$

inside the holographic scalar member. [[members/constant-exponent-response|The constant-exponent member]] sets \(\alpha_s=0\) by definition; it does not derive the observed exponent. The ACT DR6 extended-model result mirrored locally is consistent with zero, but differences between best-fit tilts from overlapping likelihood combinations are not an estimator of running.

## What would count as prediction

A predictive member must independently restrict or calculate enough of

$$
\bigl{
c_{\mathrm{calc}}^{(0)}(k),
c_{\mathrm{calc}}^{(2)}(k),
\Gamma_{3,\mathrm{calc}},
\Gamma_{4,\mathrm{calc}},\ldots
\bigr}
$$

to produce overdetermined observables. Strong milestones are:

- amplitude from a microscopic normalization rather than from \(A_s\);
- tilt and running from a derived flow law;
- a tensor amplitude and tilt from an independent spin-two response;
- bispectrum and trispectrum shapes with the required semilocal and Ward-identity terms;
- passive matching into the thermal history; and
- a reproducible likelihood using released data and nuisance treatment.

An unrestricted positive function \(c^{(0)}(k)\) can encode any positive scalar spectrum. [[critical-scale-kernels/unrestricted-response-no-go|The nonprediction no-go]] therefore makes microscopic restriction of the function the empirical turning point.

## Scope-indexed falsifiers

- A calculated member is rejected if its scalar, tensor, or higher response disagrees with the declared likelihood.
- The constant-exponent member is rejected by established nonzero running, while the unrestricted response class survives.
- The exact flat critical member is rejected if its physical field genuinely satisfies the declared flat symmetries but its leading precision is not homogeneous of degree three.
- The holographic member is rejected if the required continuation, state, or stress representation fails; CWST could still seek a different representation.
- The causal-wall realization is rejected if its constructed state response does not produce the required positive cosmological precision or cannot transfer to the measured observable statistics and data products. Actual record formation is a separate factive obligation.
