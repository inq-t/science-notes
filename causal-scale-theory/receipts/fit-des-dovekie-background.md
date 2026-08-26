# DES-Dovekie Background Robustness Receipt

This receipt replaces Pantheon+ by the separately recalibrated DES-Dovekie Hubble diagram and treats the fully released 2025 DESI likelihood as its canonical BAO row. It reproduces the collaboration's flat-\(\Lambda\)CDM supernova fit, resolves the apparent absolute-\(\chi^2\) discrepancy as the published analytic-marginalization constant, and finds that the frozen unit CST-B2 curve remains competitive. This is a calibration-and-compilation robustness test, not statistically independent evidence and not a perturbation or primary-CMB fit.

## Meaning

Pantheon+ and DES-Dovekie are materially different reductions of supernova information. Agreement of the CST background result under that replacement asks a sharper question than merely re-running the same file: does the conclusion survive a new calibration, light-curve model, bias-correction pipeline, contamination treatment, and systematic covariance?

It does. With the fully released 2025 DESI DR2 BAO likelihood, replacing Pantheon+ by DES-Dovekie changes the direct equal-footing comparison from \(\Delta\chi^2=-3.31\) to

$$
\Delta\chi^2
:=\chi^2_{\mathrm{CST}}-\chi^2_{\Lambda\mathrm{CDM}}
=-6.7052.
$$

Replacing the old Ly\(\alpha\) block by the bivariate Gaussian published in August 2026 gives \(-6.6096\). That update is provisional because its full likelihood and cross-covariances have not yet been released. The sign is robust to both updates and to the supernova likelihood's normalization convention. The evidential weight is not additive to the Pantheon+ result: the two compilations share some low-redshift supernova material, and both comparisons reuse the same DESI likelihood.

## Exact released interface

The release supplies 1,820 rows in the order required by its packed precision matrix. The compact Hubble-diagram columns are

$$
(\mathrm{CID},\mathrm{IDSURVEY},z_{\mathrm{HD}},z_{\mathrm{HEL}},
\mu,\sigma_\mu,\sigma_{\mathrm{VPEC}},\sigma_{\mathrm{sys}},P_{\mathrm{Ia}}).
$$

The likelihood keeps rows with \(z_{\mathrm{HD}}>0\). Every released row passes; the upstream BBC production already imposed \(z>0.025\), and the actual range is

$$
0.02509\le z_{\mathrm{HD}}\le1.14418.
$$

The theory vector must use the two redshifts in different places:

$$
D_L=(1+z_{\mathrm{HEL}})\,D_M(z_{\mathrm{HD}}),
\qquad
\mu_{\mathrm{th}}=5\log_{10}D_L+\text{constant}.
$$

Thus \(z_{\mathrm{HD}}\) supplies the CMB-frame, peculiar-velocity-corrected integration limit, while \(z_{\mathrm{HEL}}\) supplies the observed-redshift factor. Replacing both by one redshift is not the released likelihood.

`DES-Dovekie_STAT+SYS.npz` contains `nsn = 1820` and the 1,657,110 entries of the upper triangle of the total **inverse covariance** \(P\). The triangle is reflected to make \(P\) symmetric. The `MUERR` and `MUERR_SYS` columns are diagnostics, not extra covariance terms: after inversion,

$$
\sqrt{\operatorname{diag}P^{-1}}
=\sqrt{\mathrm{MUERR}^2+\mathrm{MUERR\_SYS}^2}
$$

to a maximum absolute difference of \(8.14\times10^{-6}\) mag. Adding either diagonal again would double-count released uncertainty. The Hubble-diagram ordering must be retained; the collaboration warns that its metadata table is differently ordered.

The [Cobaya compact mirror](https://github.com/CobayaSampler/sn_data/tree/master/DES-Dovekie) calls the same binary product `covtot_inv_000.npz`; it is byte-for-byte identical to the collaboration's `STAT+SYS.npz` at SHA-256 `ffd3124b...95463b`. Its comma-normalized Hubble diagram removes `CID` and adds an index, so its file hash differs, but all eight retained numerical columns are exactly equal row by row. The exploratory compact fit therefore used the correct measurements and precision matrix.

The 1,820-row Gaussian vector should not be confused with the paper's stated effective count of 1,684. That effective count is not reproducible by simply summing the compact release's `PROBIA_BEAMS` column, which gives 1,714.22; its internal construction is therefore not inferred here. The official compact likelihood nevertheless uses all 1,820 rows and does not multiply the final quadratic form by `PROBIA_BEAMS`. Contamination and BEAMS treatment have already been propagated into the released distances and statistical errors.

## Offset marginalization and the missing 8.85

Let \(r=\mu_{\mathrm{obs}}-\mu_{\mathrm{th}}\), \(\mathbf 1\) be the constant-offset direction, and

$$
A=r^TPr,
\qquad
B=\mathbf1^TPr,
\qquad
C=\mathbf1^TP\mathbf1.
$$

Profiling the common magnitude--\(H_0\) offset gives

$$
Q=A-\frac{B^2}{C}.
$$

The released DES likelihood instead records the analytically marginalized convention used by Goliath et al.:

$$
\chi^2_{\mathrm{DES}}=Q+\ln\!\left(\frac{C}{2\pi}\right).
$$

For this release,

$$
C=43938.33706138445,
\qquad
\ln\!\left(\frac{C}{2\pi}\right)=8.85266543315.
$$

That constant exactly resolves the apparent mismatch:

| Flat \(\Lambda\)CDM SN-only quantity | Reproduced value | Popovic et al. |
|---|---:|---:|
| best \(\Omega_m\), radiation neglected | \(0.330317\) | \(0.330\pm0.015\) |
| profiled quadratic \(Q\) | \(1631.420536\) | not tabulated |
| \(Q+\ln(C/2\pi)\) | \(1640.273201\) | \(1640.3\) |

Because the data mask and covariance are identical for CST and \(\Lambda\)CDM, the logarithmic term is model-independent and cancels exactly in \(\Delta\chi^2\). Absolute numbers should use the DES convention when compared with Table 10; model differences may use either convention if they are declared consistently.

## Distance results

The robustness comparison uses \(\Omega_{r0}=9.15\times10^{-5}\), fits the same single shape parameter \(\Omega_{m0}\) in both models, and profiles the same supernova offset and DESI amplitude \(c/(H_0r_d)\). The provisional 2026 DESI Ly\(\alpha\) full-shape pair replaces, rather than supplements, the older \(z=2.33\) BAO pair and assumes zero cross-covariance with the lower-redshift blocks pending a full product.

| DESI + DES-Dovekie row | Flat \(\Lambda\)CDM \(\Omega_{m0}\) | Unit CST-B2 \(\Omega_{m0}\) | Flat \(\Lambda\)CDM \(\chi^2\) | Unit CST-B2 \(\chi^2\) | \(\Delta\chi^2\) |
|---|---:|---:|---:|---:|---:|
| Fully released 2025 BAO | \(0.305769\) | \(0.322253\) | \(1645.328740\) | \(1638.623522\) | \(-6.705219\) |
| Provisional 2026 published-Gaussian update | \(0.307616\) | \(0.325335\) | \(1647.011221\) | \(1640.401595\) | \(-6.609626\) |

For the fully released row, both covariance blocks are positive definite and the 1,833-element vector has 1,830 nominal degrees of freedom after the three fitted quantities. The reduced \(\chi^2\) values are \(0.89909\) and \(0.89542\), with maximum absolute Cholesky-whitened residuals \(3.83\) and \(3.70\). There is no conventional goodness-of-fit rejection. The result is a stronger late-time preference than the Pantheon+ run, but it remains a non-nested maximum-likelihood comparison developed after the broad observational pattern was known. No Gaussian significance or discovery claim follows from \(-6.71\).

## Corrections already upstream

The compact likelihood begins after the observational pipeline has produced corrected distances and a total covariance.

- **Peculiar velocities.** The released `zHD` is already in the CMB frame with the nominal peculiar-velocity correction. Popovic et al. use updated low-redshift redshifts, Peterson et al. corrections with a uniform \(250\ \mathrm{km\,s^{-1}}\) uncertainty, and a nominal 2M++ flow correction. Alternative line-of-sight 2M++ and 2MRS treatments enter the systematic covariance. `MUERR_VPEC` is diagnostic and must not be added again.
- **Weak-lensing scatter.** The released BBC configuration sets `lensing_zpar=0.055`, i.e. the production-stage redshift-dependent lensing-scatter prescription. Simulations also use the released lensing probability map. The compact cosmology likelihood adds no further \(0.055z\) term; its statistical covariance already reproduces the released `MUERR` diagonal.
- **Light-curve and population nuisances.** The released \(\alpha=0.169\), \(\beta=3.14\), and host step \(\gamma=0.033\), together with calibration, dust, contamination, and bias-correction variations, have already been condensed into \(\mu\) and \(P\). They are not new free parameters in this compact background fit. Only the common absolute offset is marginalized at this stage.

## Reproduction

Run

```powershell
python causal-scale-theory/receipts/fit-des-dovekie-background.py `
  --data-dir causal-scale-theory/sources/late-time-background `
  --output causal-scale-theory/receipts/des-dovekie-background-fit.json
```

The script verifies the four source hashes, unpacks the precision matrix, checks its diagonal against the released uncertainty diagnostics, reproduces the published flat-\(\Lambda\)CDM fit, and writes [[causal-scale-theory/receipts/des-dovekie-background-fit|the machine-readable ledger]]. Its shared expansion and distance functions are imported from [[causal-scale-theory/receipts/fit-late-time-background|the primary late-time receipt]], so the alternate-supernova test does not fork a second implementation of CST-B2.

## Primary sources

- [[library/dark-energy-survey-supernova-program-reanalysis/entry|Popovic et al., DES supernova reanalysis]]: sample construction, corrections, systematics, cosmological results, and Table 10.
- [DES-SN5YR distance and covariance release](https://github.com/des-science/DES-SN5YR/tree/main/4_DISTANCES_COVMAT): ordered Hubble diagram, packed inverse covariance, column definitions, and production products.
- [DES-Dovekie CosmoSIS likelihood](https://github.com/des-science/DES-SN5YR/blob/main/5_COSMOLOGY/Dovekie_cosmosis_likelihood.py): exact row mask, two-redshift luminosity distance, matrix unpacking, and analytic offset marginalization.
- [Cobaya supernova-data mirror](https://github.com/CobayaSampler/sn_data/tree/master/DES-Dovekie): the compact `covtot_inv_000.npz` and numerically identical normalized distance table used in the exploratory run.
- [DES-Dovekie BBC production configuration](https://github.com/des-science/DES-SN5YR/blob/main/7_PIPPIN_FILES/base_files/bbc/BBC_des5yr.input): \(z\) range and lensing-scatter parameter.
- [Goliath et al., *Supernovae and the Nature of the Dark Energy*](https://doi.org/10.1051/0004-6361:20011398): analytic constant-offset marginalization used by the released likelihood.

The appropriate promotion is **[REPRODUCED BACKGROUND ROBUSTNESS TEST]**. It strengthens the empirical case that the frozen expansion curve is not an accident of the Pantheon+ reduction. It does not promote CST-B2 into a full cosmology, prove the response ontology, or supply statistically independent evidence that may be multiplied with the Pantheon+ likelihood ratio.
