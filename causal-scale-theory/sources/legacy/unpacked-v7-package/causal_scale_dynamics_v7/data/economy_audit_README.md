# Modular–Weyl economy and uniqueness audit: null lensing ensemble

This diagnostic tests whether the previously reported anti-alignment between the rigid pulse's approximate CMB-lensing response and CAMB's positive-neutrino-mass response is unique.

It samples 250 smooth, positive transient histories

\[
\rho_X(N)\propto \operatorname{sech}^{p}[\beta(N-N_t)]
\]

with broad ranges in \(p\), \(\beta\), and \(N_t\). Each accepted model is matched to the same early physical matter density and comoving distance to \(z=20\) as the rigid pulse, and is required to contribute less than 2% of the total density at \(z=20\). The same transfer-weighted linear-growth Limber approximation used in the direct-response report is applied.

## Result

225 histories were accepted. Of these:

- 92.9% had weighted cosine below -0.90 relative to CAMB's positive-neutrino response;
- 76.9% had cosine below -0.95;
- the median cosine was -0.969;
- the rigid pulse's cosine was -0.972;
- 98.2% generated a negative equivalent signed neutrino response;
- the median equivalent response was -0.0435 eV, versus -0.0488 eV for the rigid pulse under the same weighting.

## Interpretation

The lensing anti-alignment is a meaningful necessary-condition success, but it is not unique to the modular–Weyl pulse. It is common among smooth transient histories selected to preserve the early universe and alter intermediate-redshift growth. The more discriminating tests are the rigid pulse's fixed exponent, branch-folded conic, amplitude-width relation, perturbation kernel, and independent modular derivation.

## Reproduce

```bash
python null_lensing_ensemble.py
```

Outputs are written to `null_ensemble_results.json`.
