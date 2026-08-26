# Late-Time Background Data

This directory freezes the public inputs used by the direct CST-B2 background receipts: the official 2025 DESI DR2 Gaussian BAO vector and covariance, the official Pantheon+ Hubble diagram with its full statistical-plus-systematic covariance, and the 2026 DES-Dovekie Hubble diagram with its released packed precision matrix. The 2026 DESI Ly\(\alpha\) full-shape update is not yet a released data product; its two distances and correlation are transcribed in the receipt from equation (26) of the primary paper and replace, rather than supplement, the 2025 Ly\(\alpha\) BAO pair.

## Files and provenance

| Local file | Upstream source | SHA-256 |
|---|---|---|
| `desi_dr2_bao_mean.txt` | [CobayaSampler official DESI DR2 likelihood data](https://github.com/CobayaSampler/bao_data/blob/master/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_mean.txt) | `9ac154ab583ce759c0f7eef3c978c7c70a6ead2d18774caceadf1a350a640585` |
| `desi_dr2_bao_cov.txt` | [CobayaSampler official DESI DR2 likelihood data](https://github.com/CobayaSampler/bao_data/blob/master/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt) | `252a143274c8a07c78694c119617d36594f6d7965d00319ca611c6ffb886e509` |
| `Pantheon+SH0ES.dat` | [Pantheon+SH0ES DataRelease](https://github.com/PantheonPlusSH0ES/DataRelease/blob/main/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/Pantheon%2BSH0ES.dat) | `1cb0fc379ef066afdc2ffd1857681cc478024570d8a3eba284fb645775198cf8` |
| `Pantheon+SH0ES_STAT+SYS.cov` | [Pantheon+SH0ES DataRelease](https://github.com/PantheonPlusSH0ES/DataRelease/blob/main/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/Pantheon%2BSH0ES_STAT%2BSYS.cov) | `abf806d966485e64afdb359c87bffc0ecc00d05eff0a31ced66f247385df0fdc` |
| `DES-Dovekie_HD.csv` | [DES-SN5YR DES-Dovekie release](https://github.com/des-science/DES-SN5YR/blob/main/4_DISTANCES_COVMAT/DES-Dovekie_HD.csv) | `2f57019d783eaa976df80a41b0054171a2d994ee9808d715ce850c2df5720aaf` |
| `DES-Dovekie_STAT+SYS.npz` | [DES-SN5YR DES-Dovekie release](https://github.com/des-science/DES-SN5YR/blob/main/4_DISTANCES_COVMAT/STAT%2BSYS.npz) | `ffd3124b32148b1372bd95fda9299269f0352a9f8eee02d416c610e38495463b` |

The DESI collaboration identifies the Gaussian BAO files as the likelihood products used for its DR2 cosmology analysis: [DESI DR2 BAO cosmology results](https://data.desi.lbl.gov/public/papers/y3/bao-cosmo-params/README.html). The measurements and cosmological analysis are in [[library/desi-dr2-results-ii/entry|DESI DR2 Results II]]. Pantheon+ sample and cosmology methods are described by [Scolnic et al.](https://doi.org/10.3847/1538-4357/ac8b7a) and [[library/pantheon-plus-analysis-cosmological-constraints/entry|Brout et al.]].

The Pantheon+ table contains both Hubble-flow and Cepheid-host rows. The shape-only receipt selects \(z_{\mathrm{HD}}>0.01\) and removes calibrators, leaving 1,580 rows. [[causal-scale-theory/receipts/fit-calibrated-background|The calibrated receipt]] instead applies the collaboration's \((z_{\mathrm{HD}}>0.01)\lor\mathtt{IS\_CALIBRATOR}\) selection, retains 77 calibrator rows, and uses their released `CEPH_DIST` values. Both receipts slice the same full covariance after defining their selection.

The DES-Dovekie files are the unmodified products at DES-SN5YR commit `c9a4fcafc4cbd19bd750dee47fc76194a45c181f`. The `.npz` product contains an upper-triangular **inverse** covariance, not a covariance. Its ordering matches `DES-Dovekie_HD.csv`; the release warns that the larger metadata table has a different ordering. [[library/dark-energy-survey-supernova-program-reanalysis/entry|Popovic et al.]] own the recalibration and cosmology analysis, while the collaboration's [likelihood implementation](https://github.com/des-science/DES-SN5YR/blob/main/5_COSMOLOGY/Dovekie_cosmosis_likelihood.py) owns the compact data interface and nuisance convention.

The [CobayaSampler compact mirror](https://github.com/CobayaSampler/sn_data/tree/master/DES-Dovekie) renames the same precision product `covtot_inv_000.npz`; its SHA-256 is identical. Its comma-normalized distance table retains exactly the same eight numerical columns and row order while replacing `CID` with a row index. The collaboration products are archived here because they remain the primary source.

## 2026 Ly\(\alpha\) replacement

[[library/desi-dr2-results-iv/entry|DESI DR2 Results IV, version 3]] reports at \(z_{\mathrm{eff}}=2.33\)

$$
\frac{D_M}{r_d}=39.32\pm0.33,
\qquad
\frac{D_H}{r_d}=8.600\pm0.066,
\qquad
\rho=0.225.
$$

The receipt replaces the last two entries and their covariance block with these values. It does not add them to the older Ly\(\alpha\) BAO likelihood, because the new result combines the broadband Alcock--Paczyński and BAO information from the same forest sample. Cross-covariances with the lower-redshift galaxy and quasar blocks are taken to vanish, following the block structure of the released DESI Gaussian likelihood and the collaboration's stated combination of the measurements. This assumption should be replaced by the collaboration's full released likelihood when DESI publishes it.

These are raw source products. Project interpretation belongs in [[causal-scale-theory/data-consistency|the data-consistency audit]].

## Reused early-distance source

The optional acoustic-distance stress tests do not duplicate the already archived Planck products in this directory. They read the four baseline chains from [[causal-wall-spectral-theory/sources/data/entry|the observational-data archive]] and verify the SHA-256 of `COM_CosmoParams_base-plikHM-TTTEEE-lowl-lowE_R3.00.zip` against [[causal-wall-spectral-theory/sources/checksums|the source checksum ledger]]. The receipt derives its tight compression from the `DAstar`, `rdrag`, and `zstar` columns; it does not attribute the project's broader \(94.32\pm0.28\) sensitivity width to the Planck collaboration. Both compressions are appended to the fully released 2025 DESI vector, not to the provisional 2026 Gaussian substitution.
