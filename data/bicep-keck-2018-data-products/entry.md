# BICEP/Keck 2018 Data Products

The BK18 public release supplies compact bandpower, foreground-component, noise, bandpass, and marginalized tensor-likelihood tables together with a CosmoMC likelihood package. These are reduced products from BICEP2, Keck Array, and BICEP3 observations through the 2018 season; they support the published $r$ analysis but are not the underlying sky maps or full posterior-chain release.

## Metadata

- **Dataset:** BICEP/Keck 2018 Data Products (BK18).
- **Creator:** BICEP/Keck Collaboration.
- **Product date:** 2021-06-07.
- **Release DOI:** [10.71662/5etq-eh39](https://doi.org/10.71662/5etq-eh39).
- **Associated article:** [[library/bicep-keck-2018-primordial-gravitational-waves/entry|Improved Constraints on Primordial Gravitational Waves using Planck, WMAP, and BICEP/Keck Observations through the 2018 Observing Season]].
- **Retrieved locally:** 2026-08-22.
- **Local cache:** `causal-wall-spectral-theory/sources/data/bicep-keck-2018/` (100 files; 76,344,761 bytes including extracted working trees).
- **Git status:** the local cache is intentionally ignored; this wrapper remains available in a blob-free clone.

## Compact tables

| Product | Shape | Local filename | SHA-256 |
|---|---:|---|---|
| BB bandpowers and cross-spectra | $9\times134$ | `BK18_bandpowers_20210607.txt` | `d62ee72c800c16a3c9434ad0e343e8fa445400d464c0ba82118062c8e99bf80e` |
| Foreground/CMB component decomposition | $9\times28$ | `BK18_components_20210607.txt` | `96cf5ed546f20fa7efba08a9effa8e8211b94e553209eb58f43c409a6c9eb0e4` |
| Noise and effective sky fraction | $9\times12$ | `BK18_Nl_fsky_20210607.txt` | `9fc6749ff0b19e2ec4feb0d7c6268551cfc012bfcb3c8669be66b40ae5ff0e01` |
| Marginalized $r$ likelihood | $100\times2$ | `BK18_r_likelihood_20210607.txt` | `b3320d2d5b739cbf04d23c2dc2f5275e706b861cc3a5eafa7e626121d0657889` |

Four three-column bandpass tables cover BICEP3 95 GHz, Keck 95 GHz, 150 GHz, and 220 GHz responses. Their filenames and hashes remain frozen in the local checksum ledger.

## Likelihood package and related representations

`BK18_cosmomc.tgz` is the canonical executable release archive (10,410,429 bytes; SHA-256 `ca1555ae52ec6780c3575a97a7ef5a14817997767ddd0b2908af059bf62dee7a`). Its 83-file, approximately 61 MB extracted tree is retained because CosmoMC expects its internal paths. The `rns_code.tgz` companion archive (1,364,730 bytes; SHA-256 `0612f8b5c630bbb5ce0e5586f244334152f236b4605ac0934131a5cf9f142641`) contains the released $r$--$n_s$ calculation and contour inputs.

Several files are deliberately related without being redundant:

- the top-level bandpass tables add an E-mode response column, whereas the CosmoMC copies retain the likelihood's B-mode response representation;
- `BK18lf_dust` and `BK18lf_dust_incEE` share some bandpasses and parameter names, but the latter has different E-inclusive data, covariance, windows, and configuration; and
- archive files and extracted trees are immutable downloads and executable working copies, respectively.

Preserve these layouts rather than deleting their repeated internal files.

## Fetch

The [BICEP/Keck product page](https://lambda.gsfc.nasa.gov/product/bicepkeck/bicep2_prod_table.html) is the release index. Direct downloads are:

- [bandpowers](https://lambda.gsfc.nasa.gov/data/suborbital/BICEPK_2021/BK18_bandpowers_20210607.txt)
- [$r$ likelihood](https://lambda.gsfc.nasa.gov/data/suborbital/BICEPK_2021/BK18_r_likelihood_20210607.txt)
- [components](https://lambda.gsfc.nasa.gov/data/suborbital/BICEPK_2021/BK18_components_20210607.txt)
- [noise and sky fraction](https://lambda.gsfc.nasa.gov/data/suborbital/BICEPK_2021/BK18_Nl_fsky_20210607.txt)
- [BICEP3 95 GHz bandpass](https://lambda.gsfc.nasa.gov/data/suborbital/BICEPK_2021/BK18_B95_bandpass_20210607.txt)
- [Keck 95 GHz bandpass](https://lambda.gsfc.nasa.gov/data/suborbital/BICEPK_2021/BK18_K95_bandpass_20210607.txt)
- [150 GHz bandpass](https://lambda.gsfc.nasa.gov/data/suborbital/BICEPK_2021/BK18_150_bandpass_20210607.txt)
- [220 GHz bandpass](https://lambda.gsfc.nasa.gov/data/suborbital/BICEPK_2021/BK18_220_bandpass_20210607.txt)
- [CosmoMC likelihood archive](https://lambda.gsfc.nasa.gov/data/suborbital/BICEPK_2021/BK18_cosmomc.tgz)
- [$r$--$n_s$ companion archive](https://lambda.gsfc.nasa.gov/data/suborbital/BICEPK_2021/rns_code.tgz)

Restore files to the local-cache path above when an old workspace command requires that layout. The much larger full chain release is intentionally not mirrored.

