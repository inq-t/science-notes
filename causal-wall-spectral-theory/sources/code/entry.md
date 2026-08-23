# Reproduction Code

This directory holds commit-pinned local snapshots of the public ACT DR6 likelihood and run-configuration repositories. The archives preserve exact upstream revisions, while the unpacked trees expose their readmes, YAML combinations, priors, and likelihood implementations to local search.

## ACT DR6 CMB-only likelihood

- Revision: `627aeafb88ae5ad1aa66b406bea2d65cfa66a27d`
- [[causal-wall-spectral-theory/sources/code/act-dr6-cmbonly-627aeafb/DR6-ACT-lite-627aeafb88ae5ad1aa66b406bea2d65cfa66a27d/README.md|Local readme]]
- [[causal-wall-spectral-theory/sources/code/act-dr6-cmbonly-627aeafb/DR6-ACT-lite-627aeafb88ae5ad1aa66b406bea2d65cfa66a27d/yamls/parameters/nrun.yaml|Running parameter definition]]
- [[causal-wall-spectral-theory/sources/code/act-dr6-cmbonly-627aeafb/DR6-ACT-lite-627aeafb88ae5ad1aa66b406bea2d65cfa66a27d/yamls/p-act-lb-lcdm.yaml|P--ACT--lensing--BAO example]]
- [[causal-wall-spectral-theory/sources/code/act-dr6-cmbonly-627aeafb.zip|Commit archive]]

The package evaluates the foreground-marginalized CMB-only SACC likelihood mirrored under [[causal-wall-spectral-theory/sources/data/act-dr6/dr6_data_cmbonly/v1.0/dr6_data_cmbonly.fits|data/act-dr6]].

## ACT DR6 multifrequency likelihood

- Revision: `4220e14efb3a995f47c9f54cb687479e558c6138`
- [[causal-wall-spectral-theory/sources/code/act-dr6-mflike-4220e14e/act_dr6_mflike-4220e14efb3a995f47c9f54cb687479e558c6138/README.rst|Local readme]]
- [[causal-wall-spectral-theory/sources/code/act-dr6-mflike-4220e14e/act_dr6_mflike-4220e14efb3a995f47c9f54cb687479e558c6138/examples/act_dr6_example.yml|Example likelihood configuration]]
- [[causal-wall-spectral-theory/sources/code/act-dr6-mflike-4220e14e.zip|Commit archive]]

This package consumes the full local [[causal-wall-spectral-theory/sources/data/act-dr6/dr6_data/v1.0/dr6_data.fits|multifrequency SACC file]] and introduces the foreground and nuisance model absent from the CMB-only product.

## ACT DR6 run definitions

- Revision: `fad1d4c97cd56a40955be4e7ba16c0307200b9bb`
- [[causal-wall-spectral-theory/sources/code/act-dr6-parameters-fad1d4c9/ACT-DR6-parameters-fad1d4c97cd56a40955be4e7ba16c0307200b9bb/README.md|Local readme]]
- [[causal-wall-spectral-theory/sources/code/act-dr6-parameters-fad1d4c9/ACT-DR6-parameters-fad1d4c97cd56a40955be4e7ba16c0307200b9bb/likelihoods/act_dr6_extended.yaml|Extended-model likelihood definition]]
- [[causal-wall-spectral-theory/sources/code/act-dr6-parameters-fad1d4c9/ACT-DR6-parameters-fad1d4c97cd56a40955be4e7ba16c0307200b9bb/runs/dr6_camb.yaml|Baseline CAMB run]]
- [[causal-wall-spectral-theory/sources/code/act-dr6-parameters-fad1d4c9.zip|Commit archive]]

## Other local released code

- [[causal-wall-spectral-theory/sources/data/planck-2018/clik-code-v3/code/plc_3.0/plc-3.01/readme.md|Planck PR3 clik 3.01]] is a legacy C, Fortran, and Python likelihood stack supplied with the matching local data release.
- [[causal-wall-spectral-theory/sources/data/planck-2015-bkp/clik-code-v2/plc-2.0/readme.md|Planck PR2 clik 2.0]] and [[causal-wall-spectral-theory/sources/data/planck-2015-bkp/bkp-likelihood/BKPlanck_README.txt|the BKP likelihood]] preserve the older analysis inputs.
- [[causal-wall-spectral-theory/sources/data/bicep-keck-2018/BK18_cosmomc/BK18_cosmomc/BK18_README.txt|BK18 CosmoMC]] and [[causal-wall-spectral-theory/sources/data/bicep-keck-2018/rns_code/rns_code/BK18_rns.py|the released $r$--$n_s$ script]] accompany the BK18 data.

These packages were mirrored and archive-checked, not installed or rerun. A genuine CWST likelihood test additionally requires a theory-to-spectrum implementation; none of the released packages supplies one.
