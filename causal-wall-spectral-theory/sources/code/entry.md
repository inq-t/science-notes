# Reproduction Code

This directory holds commit-pinned local snapshots of the public ACT DR6 likelihood and run-configuration repositories. The archives preserve exact upstream revisions, while the unpacked trees expose their readmes, YAML combinations, priors, and likelihood implementations to local search.

## ACT DR6 CMB-only likelihood

- Revision: `627aeafb88ae5ad1aa66b406bea2d65cfa66a27d`
- [[causal-wall-spectral-theory/sources/code/act-dr6-cmbonly-627aeafb/DR6-ACT-lite-627aeafb88ae5ad1aa66b406bea2d65cfa66a27d/README.md|Local readme]]
- [[causal-wall-spectral-theory/sources/code/act-dr6-cmbonly-627aeafb/DR6-ACT-lite-627aeafb88ae5ad1aa66b406bea2d65cfa66a27d/yamls/parameters/nrun.yaml|Running parameter definition]]
- [[causal-wall-spectral-theory/sources/code/act-dr6-cmbonly-627aeafb/DR6-ACT-lite-627aeafb88ae5ad1aa66b406bea2d65cfa66a27d/yamls/p-act-lb-lcdm.yaml|P--ACT--lensing--BAO example]]
- [[causal-wall-spectral-theory/sources/code/act-dr6-cmbonly-627aeafb.zip|Commit archive]]

The package evaluates the foreground-marginalized CMB-only SACC interface documented by [[data/act-dr6-cosmology-products/entry|the ACT DR6 dataset module]].

## ACT DR6 multifrequency likelihood

- Revision: `4220e14efb3a995f47c9f54cb687479e558c6138`
- [[causal-wall-spectral-theory/sources/code/act-dr6-mflike-4220e14e/act_dr6_mflike-4220e14efb3a995f47c9f54cb687479e558c6138/README.rst|Local readme]]
- [[causal-wall-spectral-theory/sources/code/act-dr6-mflike-4220e14e/act_dr6_mflike-4220e14efb3a995f47c9f54cb687479e558c6138/examples/act_dr6_example.yml|Example likelihood configuration]]
- [[causal-wall-spectral-theory/sources/code/act-dr6-mflike-4220e14e.zip|Commit archive]]

This package consumes the full multifrequency SACC interface documented by [[data/act-dr6-cosmology-products/entry|the ACT DR6 dataset module]] and introduces the foreground and nuisance model absent from the CMB-only product.

## ACT DR6 run definitions

- Revision: `fad1d4c97cd56a40955be4e7ba16c0307200b9bb`
- [[causal-wall-spectral-theory/sources/code/act-dr6-parameters-fad1d4c9/ACT-DR6-parameters-fad1d4c97cd56a40955be4e7ba16c0307200b9bb/README.md|Local readme]]
- [[causal-wall-spectral-theory/sources/code/act-dr6-parameters-fad1d4c9/ACT-DR6-parameters-fad1d4c97cd56a40955be4e7ba16c0307200b9bb/likelihoods/act_dr6_extended.yaml|Extended-model likelihood definition]]
- [[causal-wall-spectral-theory/sources/code/act-dr6-parameters-fad1d4c9/ACT-DR6-parameters-fad1d4c97cd56a40955be4e7ba16c0307200b9bb/runs/dr6_camb.yaml|Baseline CAMB run]]
- [[causal-wall-spectral-theory/sources/code/act-dr6-parameters-fad1d4c9.zip|Commit archive]]

## Other local released code

- [[data/planck-2018-release-3-cosmology-products/entry|Planck Release-3]] includes the legacy `clik` 3.01 C, Fortran, and Python likelihood stack supplied with its data products.
- [[data/planck-2015-release-2-cosmology-products/entry|Planck Release-2]] includes `clik` 2.0, while [[data/bicep2-keck-planck-2015-joint-likelihood/entry|the 2015 BKP module]] owns the associated joint likelihood package.
- [[data/bicep-keck-2018-data-products/entry|The BK18 module]] owns the CosmoMC likelihood and released $r$--$n_s$ companion package.

These packages were mirrored and archive-checked, not installed or rerun. A genuine CWST likelihood test additionally requires a theory-to-spectrum implementation; none of the released packages supplies one.
