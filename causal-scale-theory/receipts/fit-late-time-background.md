# Direct Late-Time Background Receipt

This receipt performs an equal-footing background-only comparison between the frozen unit CST-B2 member and flat \(\Lambda\)CDM. It reads the archived DESI DR2, Pantheon+, and Planck PR3 products; verifies their hashes; profiles the shared distance calibrations analytically; fits one ordinary-sector shape parameter \(\Omega_{m0}\) in each model; and writes the complete result to [[causal-scale-theory/receipts/late-time-background-fit.json|the machine-readable fit ledger]]. The Planck product is used only for explicitly qualified acoustic-distance stress tests, not as a substitute for a primary-CMB likelihood.

Run from the repository root with the bundled or any Python 3 interpreter carrying NumPy:

```powershell
python causal-scale-theory/receipts/fit-late-time-background.py `
  --data-dir causal-scale-theory/sources/late-time-background `
  --planck-chain-dir causal-wall-spectral-theory/sources/data/planck-2018/base-plikHM-TTTEEE-lowl-lowE/base/plikHM_TTTEEE_lowl_lowE `
  --output causal-scale-theory/receipts/late-time-background-fit.json
```

The supernova nuisance offset is profiled from

$$
\chi^2_{\mathrm{SN}}(\mathcal M)
=(r-\mathcal M\mathbf1)^TC^{-1}(r-\mathcal M\mathbf1),
$$

where \(r=m_b-5\log_{10}[(1+z_{\mathrm{hel}})\chi(z_{\mathrm{HD}})]\). The BAO prediction has the common form \(A g(E,\chi)\), where

$$
A=\frac{c}{H_0r_d},
$$

so \(A\) is profiled by the same quadratic projection. Thus neither \(H_0\), \(r_d\), nor the supernova absolute magnitude is smuggled into the shape comparison.

The receipt validates its likelihood construction by recovering three published flat-\(\Lambda\)CDM results: the Pantheon+-only \(\Omega_m\), the 2025 DESI-BAO-only \(\Omega_m\), and the 2026 DESI galaxy-BAO plus Ly\(\alpha\)-full-shape \(\Omega_m\). The last comparison is a provisional Gaussian reconstruction of the published two-distance block with zero cross-covariance to the released lower-redshift blocks, not a released 2026 likelihood. The receipt uses the Pantheon+ selection \(z_{\mathrm{HD}}>0.01\) with calibrators removed, leaving 1,580 supernova rows, and the full selected covariance submatrix. Radiation is frozen at \(\Omega_{r0}=9.15\times10^{-5}\).

For the early-distance audit it also evaluates

$$
Q_*=1000\frac{D_{M,*}[\mathrm{Gpc}]}{r_d[\mathrm{Mpc}]}
$$

over all four weighted Planck PR3 base-\(\Lambda\)CDM chains, reproducing \(Q_*=94.31404\pm0.03458\) from 24,497 rows. It appends each of two separately labeled cases to the fully released 2025 DESI vector: the undocumented historical project anchor \(94.32\pm0.28\) and the tight chain-derived posterior. The former is not a Planck-published measurement and its archived uncertainty construction is unknown; the latter is not model-neutral because the chain assumes base \(\Lambda\)CDM. Neither is counted as a full CMB fit. Doubling the logarithmic integration grid changes the unit-member distance to last scattering by only \(8.3\times10^{-12}\) relative.

This is a likelihood receipt, not evidence for the microscopic wall construction. Its scope stops at the flat homogeneous distance law; it contains no primary-CMB anisotropy, growth, lensing, or response-perturbation likelihood.
