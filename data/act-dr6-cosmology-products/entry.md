# ACT DR6 Cosmology Products

The Atacama Cosmology Telescope Data Release 6 cosmology suite contains multifrequency and foreground-marginalized CMB spectra, covariances, best-fit spectra, posterior chains, and the DR6 lensing likelihood. These products share one observational release but expose distinct analysis interfaces; they must not be collapsed merely because some are reductions, alternate binnings, or different likelihood combinations of the same sky observations.

## Metadata

- **Dataset:** ACT DR6 public cosmology products.
- **Creator:** Atacama Cosmology Telescope Collaboration.
- **Distribution:** NASA LAMBDA.
- **Release families:** DR6.02 power-spectrum products and DR6 lensing likelihood version 1.2.
- **Associated articles:** [[library/act-dr6-power-spectra-likelihoods-lambda-cdm/entry|The Atacama Cosmology Telescope: DR6 Power Spectra, Likelihoods and ΛCDM Parameters]] and [[library/the-atacama-cosmology-telescope-dr6-constraints-on-extended-cosmological-models/entry|The Atacama Cosmology Telescope: DR6 Constraints on Extended Cosmological Models]].
- **Retrieved locally:** 2026-08-22.
- **Local cache:** `causal-wall-spectral-theory/sources/data/act-dr6/` (597 files; 5,181,144,163 bytes including extracted working trees).
- **Git status:** the local cache is intentionally ignored; this wrapper remains available in a blob-free clone.

## Spectra and covariance products

The full multifrequency SACC archive `dr6_data.tar.gz` is 413,203,437 bytes with SHA-256 `5f5a68b76e0bb074bb0333e7c1b5ba9b556ccd29e58eb66f4cb4251805825383`; its extracted FITS file has a $6840\times6840$ covariance and retains tracer, bandpass, and beam information. The much smaller `dr6_data_cmbonly.tar.gz` is 286,990 bytes with SHA-256 `3f057c2569211ada03759530b74848b322edc3d68d66b6b8c2db0679547dbbd8`; its extracted FITS file is a foreground-marginalized $135\times135$ TT/TE/EE interface. The CMB-only product is a scientific reduction, not a duplicate of the multifrequency data.

The released spectra-and-covariance archives provide 20-bin and 50-bin views plus an extra product. Their corresponding sampled covariance arrays are $138\times138$ and $39\times39$. The two main trees have the same 215 relative filenames, but 214 payloads differ; their single identical `dataset_trace.pkl` belongs to the official package layout and should not be removed.

ACT-only and P--ACT best-fit trees share filenames and schemas but differ numerically throughout. They encode different fitted likelihood combinations, not duplicate measurements.

## Chains and lensing likelihood

Six compact chain archives retain ACT-only, Planck-only, and joint running or tensor analyses: `actlite_nrun_camb.tar.gz`, `p-actlite_nrun_camb.tar.gz`, `p-actlite-l-b_nrun_camb.tar.gz`, `planck_nrun_camb.tar.gz`, `planck-l-b_nrun_camb.tar.gz`, and `p-actlite-bk-l-b_r_camb.tar.gz`. Each has a matching extracted working tree. Their parameter columns are related, but their likelihood combinations and posterior samples are different datasets.

`ACT_dr6_likelihood_v1.2.tgz` is the canonical DR6 lensing-likelihood archive (361,306,879 bytes; SHA-256 `bbcde3bcacd7c9a97138c4873c8a1217635a18504d15c4f86b1fba39d3601085`). Its extracted version-1.2 working tree occupies approximately 2.93 GB. The archive and tree are intentionally both present: one freezes the download, while the other supplies the runtime-relative files.

The tracked FITS file inside the commit-pinned `DR6-ACT-lite` code snapshot is a smaller simulated test fixture. It is not an alternate copy of the released CMB-only SACC product and remains owned by the code package.

## Fetch

The [ACT DR6.02 release page](https://lambda.gsfc.nasa.gov/product/act/act_dr6.02/index.html) describes the power-spectrum products. Direct downloads are:

- [full multifrequency SACC](https://lambda.gsfc.nasa.gov/data/act/pspipe/sacc_files/dr6_data.tar.gz)
- [foreground-marginalized CMB-only SACC](https://lambda.gsfc.nasa.gov/data/act/pspipe/sacc_files/dr6_data_cmbonly.tar.gz)
- [20-bin spectra and covariance](https://lambda.gsfc.nasa.gov/data/act/pspipe/spectra_and_cov/act_dr6.02_spectra_and_cov_binning_20.tar.gz)
- [50-bin spectra and covariance](https://lambda.gsfc.nasa.gov/data/act/pspipe/spectra_and_cov/act_dr6.02_spectra_and_cov_binning_50.tar.gz)
- [extra spectra product](https://lambda.gsfc.nasa.gov/data/act/pspipe/spectra_and_cov/act_dr6.02_spectra_and_cov_xtra.tar.gz)
- [ACT best fits](https://lambda.gsfc.nasa.gov/data/act/pspipe/best_fits/act_dr6.02_best_fits_dr6_lcdm.tar.gz)
- [P--ACT best fits](https://lambda.gsfc.nasa.gov/data/act/pspipe/best_fits/act_dr6.02_best_fits_pact_lcdm.tar.gz)
- [ACT-lite running chain](https://lambda.gsfc.nasa.gov/data/act/chains/nrun/actlite_nrun_camb.tar.gz)
- [P--ACT-lite running chain](https://lambda.gsfc.nasa.gov/data/act/chains/nrun/p-actlite_nrun_camb.tar.gz)
- [P--ACT-lite, lensing, and BAO running chain](https://lambda.gsfc.nasa.gov/data/act/chains/nrun/p-actlite-l-b_nrun_camb.tar.gz)
- [Planck running chain](https://lambda.gsfc.nasa.gov/data/act/chains/nrun/planck_nrun_camb.tar.gz)
- [Planck, lensing, and BAO running chain](https://lambda.gsfc.nasa.gov/data/act/chains/nrun/planck-l-b_nrun_camb.tar.gz)
- [P--ACT-lite, BK, lensing, and BAO tensor chain](https://lambda.gsfc.nasa.gov/data/act/chains/r/p-actlite-bk-l-b_r_camb.tar.gz)
- [DR6 lensing likelihood 1.2](https://lambda.gsfc.nasa.gov/data/suborbital/ACT/ACT_dr6/likelihood/data/ACT_dr6_likelihood_v1.2.tgz)

Download only the product family required by an analysis. When extracting an archive, preserve its directory structure and restore it under the local-cache path above if an existing command expects the historical workspace layout.

