# Observational Data and Likelihoods

This directory contains local copies of the observational products that bear directly on the numerical calibration and falsification statements in the CWST notes. Posterior chains can verify a published constraint under its stated likelihood combination; they cannot test a new CWST spectrum until the theory supplies a calculable spectrum and the likelihood is rerun with that spectrum.

## Planck 2018

The scalar calibration in [[spectral-dictionary]] uses the Planck 2018 inflation analysis, mirrored as [[causal-wall-spectral-theory/sources/papers/1807.06211-planck-2018-inflation.pdf|Planck 2018 results X]]. The local [[causal-wall-spectral-theory/sources/snapshots/planck-pr3-cosmoparams-index.html|cosmological-parameter release index]] and [[causal-wall-spectral-theory/sources/snapshots/planck-pr3-software-index.html|likelihood-software index]] record the official release context.

- [[causal-wall-spectral-theory/sources/data/planck-2018/COM_CosmoParams_base-plikHM-TTTEEE-lowl-lowE_R3.00.zip|Baseline TTTEEE + low-l/lowE posterior archive]] and its extracted `base-plikHM-TTTEEE-lowl-lowE/` tree contain the baseline and lensing-chain products used to audit quoted $A_s$ and $n_s$ values.
- [[causal-wall-spectral-theory/sources/data/planck-2018/result_table_2018_68pcp120.pdf|Published 68% parameter table]] is the compact human-readable parameter summary.
- [[causal-wall-spectral-theory/sources/data/planck-2018/COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum-theory_R3.01.txt|Best-fit theory spectrum]] and [[causal-wall-spectral-theory/sources/data/planck-2018/COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum_R3.01.txt|best-fit parameter vector]] expose the baseline fit without requiring the full likelihood stack.
- [[causal-wall-spectral-theory/sources/data/planck-2018/COM_PowerSpect_CMB-TT-binned_R3.01.txt|TT]], [[causal-wall-spectral-theory/sources/data/planck-2018/COM_PowerSpect_CMB-TE-binned_R3.02.txt|TE]], and [[causal-wall-spectral-theory/sources/data/planck-2018/COM_PowerSpect_CMB-EE-binned_R3.02.txt|EE]] are compact plotting and audit spectra, not independent likelihoods.
- [[causal-wall-spectral-theory/sources/data/planck-2018/COM_Likelihood_Code-v3.0_R3.01.tar.gz|clik 3.01 source]], [[causal-wall-spectral-theory/sources/data/planck-2018/COM_Likelihood_Data-baseline_R3.00.tar.gz|baseline likelihood data]], and [[causal-wall-spectral-theory/sources/data/planck-2018/COM_Likelihood_Data-extra-lensing-ext_R3.00.tar.gz|extended lensing data]] are mirrored and unpacked. The local [[causal-wall-spectral-theory/sources/data/planck-2018/clik-data-baseline-r3/baseline/readme_baseline.md|baseline readme]] and [[causal-wall-spectral-theory/sources/data/planck-2018/clik-code-v3/code/plc_3.0/plc-3.01/readme.md|code readme]] describe the legacy compiled interface.

These products are enough to inspect the published scalar calibration and to assemble a conventional custom-spectrum refit. They do not contain a CWST forward model.

## ACT DR6

The relevant analyses are [[causal-wall-spectral-theory/sources/papers/2503.14452-act-dr6-power-spectra-likelihoods-lcdm.pdf|the DR6 spectra and baseline-parameter paper]] and [[causal-wall-spectral-theory/sources/papers/2503.14454-act-dr6-extended-cosmological-models.pdf|the extended-model paper]]. The [[causal-wall-spectral-theory/sources/snapshots/act-dr6.02-release.html|local DR6.02 release page]] records the official product structure.

- [[causal-wall-spectral-theory/sources/data/act-dr6/dr6_data_cmbonly/v1.0/dr6_data_cmbonly.fits|Foreground-marginalized CMB-only SACC data]] is the compact likelihood input; its archive is [[causal-wall-spectral-theory/sources/data/act-dr6/dr6_data_cmbonly.tar.gz|retained here]].
- [[causal-wall-spectral-theory/sources/data/act-dr6/dr6_data/v1.0/dr6_data.fits|Full multifrequency SACC data]] and its [[causal-wall-spectral-theory/sources/data/act-dr6/dr6_data.tar.gz|original archive]] support nuisance-parameter and foreground reanalysis.
- [[causal-wall-spectral-theory/sources/data/act-dr6/act_dr6.02_spectra_and_cov_binning_50.tar.gz|Likelihood-binned spectra and covariance]], the finer [[causal-wall-spectral-theory/sources/data/act-dr6/act_dr6.02_spectra_and_cov_binning_20.tar.gz|20-bin product]], and the [[causal-wall-spectral-theory/sources/data/act-dr6/act_dr6.02_best_fits_dr6_lcdm.tar.gz|ACT]] and [[causal-wall-spectral-theory/sources/data/act-dr6/act_dr6.02_best_fits_pact_lcdm.tar.gz|P--ACT]] best-fit archives preserve the spectra-level release.
- [[causal-wall-spectral-theory/sources/data/act-dr6/p-actlite-l-b_nrun_camb/p-actlite-l-b_nrun_camb/p-actlite-l-b_nrun_camb.input.yaml|P--ACT-lite--lensing--BAO running configuration]], [[causal-wall-spectral-theory/sources/data/act-dr6/p-actlite-l-b_nrun_camb/p-actlite-l-b_nrun_camb/p-actlite-l-b_nrun_camb.minimum.txt|best-fit point]], and [[causal-wall-spectral-theory/sources/data/act-dr6/p-actlite-l-b_nrun_camb.tar.gz|posterior archive]] are the exact compact artifacts behind the quoted $\alpha_s=0.0062\pm0.0052$ combination. This is a joint combination, not an ACT-only measurement.
- [[causal-wall-spectral-theory/sources/data/act-dr6/p-actlite-bk-l-b_r_camb/p-actlite-bk-l-b_r_camb/p-actlite-bk-l-b_r_camb.input.yaml|ACT + BK + lensing + BAO tensor configuration]] and its [[causal-wall-spectral-theory/sources/data/act-dr6/p-actlite-bk-l-b_r_camb.tar.gz|posterior archive]] preserve the extended analysis's compact tensor run.
- [[causal-wall-spectral-theory/sources/data/act-dr6/ACT_dr6_likelihood_v1.2/v1.2/README|DR6 lensing likelihood readme]] and [[causal-wall-spectral-theory/sources/data/act-dr6/ACT_dr6_likelihood_v1.2.tgz|likelihood archive]] supply the lensing component. The other ACT-only, Planck-only, and joint running chains are also mirrored and unpacked for comparison.

The commit-pinned likelihood implementations and run definitions are indexed in [[causal-wall-spectral-theory/sources/code/entry|Reproduction Code]].

## BICEP/Keck BK18

The tensor bound in [[spectral-dictionary]] comes from [[causal-wall-spectral-theory/sources/papers/2110.00483-bicep-keck-2018-primordial-gravitational-waves.pdf|the BK18 analysis]]. The official release has DOI `10.71662/5etq-eh39`; the [[causal-wall-spectral-theory/sources/snapshots/bicep-keck-products.html|local product page]] records file descriptions and release sizes.

- [[causal-wall-spectral-theory/sources/data/bicep-keck-2018/BK18_bandpowers_20210607.txt|BB bandpowers]], [[causal-wall-spectral-theory/sources/data/bicep-keck-2018/BK18_r_likelihood_20210607.txt|marginalized $r$ likelihood]], [[causal-wall-spectral-theory/sources/data/bicep-keck-2018/BK18_components_20210607.txt|component decomposition]], and [[causal-wall-spectral-theory/sources/data/bicep-keck-2018/BK18_Nl_fsky_20210607.txt|noise and effective sky fraction]] are directly inspectable text products.
- The [[causal-wall-spectral-theory/sources/data/bicep-keck-2018/BK18_B95_bandpass_20210607.txt|BICEP3 95]], [[causal-wall-spectral-theory/sources/data/bicep-keck-2018/BK18_K95_bandpass_20210607.txt|Keck 95]], [[causal-wall-spectral-theory/sources/data/bicep-keck-2018/BK18_150_bandpass_20210607.txt|150]], and [[causal-wall-spectral-theory/sources/data/bicep-keck-2018/BK18_220_bandpass_20210607.txt|220 GHz]] tables record the released frequency responses.
- [[causal-wall-spectral-theory/sources/data/bicep-keck-2018/BK18_cosmomc/BK18_cosmomc/BK18_README.txt|BK18 CosmoMC readme]], [[causal-wall-spectral-theory/sources/data/bicep-keck-2018/BK18_cosmomc.tgz|likelihood/data archive]], and [[causal-wall-spectral-theory/sources/data/bicep-keck-2018/rns_code/rns_code/BK18_rns.py|the $r$--$n_s$ reproduction script]] preserve the released calculation inputs.

The tabulated $r$ likelihood is adequate for auditing the bound cited by CWST. The full joint chains are unnecessary for that check.

## Historical holographic fits

Two papers in the v3 bibliography fit particular holographic-QFT models to older releases. Their conclusions concern those calculated model families and datasets, not the unrestricted CWST response function.

- For [[causal-wall-spectral-theory/sources/papers/1104.2040-easther-flauger-mcfadden-skenderis-holographic-inflation-wmap.pdf|the WMAP7 fit]], the local [[causal-wall-spectral-theory/sources/data/wmap7/wmap_tt_spectrum_7yr_v4p1.txt|TT]], [[causal-wall-spectral-theory/sources/data/wmap7/wmap_te_spectrum_7yr_v4p1.txt|TE]], and [[causal-wall-spectral-theory/sources/data/wmap7/wmap_ee_spectrum_7yr_v4p1.txt|EE]] spectra preserve the compact official release. They are not the full WMAP likelihood.
- For [[causal-wall-spectral-theory/sources/papers/1703.05385-afshordi-gould-skenderis-holographic-cosmology-planck.pdf|the Planck-2015 fit]], the [[causal-wall-spectral-theory/sources/data/planck-2015-bkp/COM_Likelihood_Code-v2.0.R2.00.tar.bz2|PR2 clik code]], [[causal-wall-spectral-theory/sources/data/planck-2015-bkp/COM_Likelihood_Data-extra-lensing-ext.R2.00.tar.gz|extended lensing product]], [[causal-wall-spectral-theory/sources/data/planck-2015-bkp/COM_PowerSpect_CMB_R2.02.fits|CMB spectra]], and [[causal-wall-spectral-theory/sources/data/planck-2015-bkp/bkp-likelihood/BKPlanck_README.txt|BKP likelihood package]] preserve the compact reproducibility inputs. The paper's competitive fit applies after removing Planck multipoles $\ell<30$; it is not an all-scale confirmation of holographic cosmology.

## Products deliberately not mirrored

| Product | Reported size or access | Reason |
|---|---:|---|
| BK18 full CosmoMC chains | 66.72 GB; 2.71 GB without `.data` files | The tabulated likelihood, released code, and compact joint artifacts contain the evidence used here. |
| Planck PR3 all-model posterior grid | 11 GB | The 62 MB baseline archive contains the scalar calibration actually cited. |
| Planck PR3 SMICA I/Q/U map and FFP10 simulations | 1.9 GB map plus hundreds of simulation realizations on NERSC storage | No standalone official primordial-non-Gaussianity likelihood exists; a reproducible estimator project would need the maps, masks, pipeline, and simulation ensemble together. |
| WMAP7 full likelihood | about 988 MB compressed | It is a legacy Fortran stack and still does not reproduce the holographic paper without the authors' model patch and historical auxiliary likelihoods. |
| Planck PR2 baseline likelihood | about 300 MB | The historical fit is not turnkey; compact spectra, lensing data, BKP likelihood, and the paper preserve the relevant claim and qualifications. |
| ACT DR6 maps, NILC maps, and map-level simulations | many gigabytes | The cited parameter claims are carried by the locally mirrored spectra, likelihoods, covariances, and chains; map-making is outside the present audit. |

These omissions are size and reproducibility boundaries, not hidden evidentiary gaps. Origins, local archive hashes, and download provenance are recorded in [[causal-wall-spectral-theory/sources/origins]] and [[causal-wall-spectral-theory/sources/checksums]].
