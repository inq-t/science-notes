# Planck 2015 Release-2 Cosmology Products

This local subset of the Planck 2015 public release preserves the compact CMB power-spectrum product, the extended lensing likelihood data, and the matching `clik` 2.0 software needed to interpret that likelihood. It is a reproducibility subset rather than the complete Planck Release-2 likelihood or posterior archive.

## Metadata

- **Dataset:** Planck Public Data Release 2 cosmology products.
- **Publisher:** ESA Planck Legacy Archive, mirrored by NASA/IPAC IRSA.
- **Release:** 2015; likelihood software/data version R2.00 and power spectra version R2.02.
- **Retrieved locally:** 2026-08-22.
- **Local cache:** `causal-wall-spectral-theory/sources/data/planck-2015-bkp/`.
- **Git status:** the local cache is intentionally ignored; this wrapper remains available in a blob-free clone.

## Retained products

| Product | Local filename | Bytes | SHA-256 |
|---|---|---:|---|
| CMB power spectra in FITS form | `COM_PowerSpect_CMB_R2.02.fits` | 164,160 | `473b986216037e13587b1684a2bf5bc9c56332f711a40a93c10d859f254b8f24` |
| Extended lensing likelihood data | `COM_Likelihood_Data-extra-lensing-ext.R2.00.tar.gz` | 1,296,809 | `0c017984bfd12315b94958f48f8e61e625361a84066838976f676fb5c2e76dbc` |
| `clik` likelihood software | `COM_Likelihood_Code-v2.0.R2.00.tar.bz2` | 1,614,281 | `c1efa208175b2751e75b2ad1c026dae744a7dd279eb74baa5db3098bc9c971bb` |

The unpacked `clik-code-v2/` and `clik-data-extra-lensing-r2/` trees are derivative working copies of the checked archives. They remain beside the archives because the legacy likelihood resolves many files by their internal relative paths. The overlapping files shared with `clik` 3 are versioned software components, not duplicate observational records, and must not be deduplicated individually.

The approximately 300 MB Release-2 baseline likelihood is not mirrored locally. Consequently, this subset alone does not reconstruct the full historical Planck likelihood used by every 2015 analysis.

## Fetch

The retained artifacts can be downloaded directly from IRSA:

- [CMB power spectra R2.02](https://irsa.ipac.caltech.edu/data/Planck/release_2/ancillary-data/cosmoparams/COM_PowerSpect_CMB_R2.02.fits)
- [Extended lensing likelihood R2.00](https://irsa.ipac.caltech.edu/data/Planck/release_2/software/COM_Likelihood_Data-extra-lensing-ext.R2.00.tar.gz)
- [`clik` likelihood code R2.00](https://irsa.ipac.caltech.edu/data/Planck/release_2/software/COM_Likelihood_Code-v2.0.R2.00.tar.bz2)

For a complete reconstruction, consult the [Planck Release-2 software index](https://irsa.ipac.caltech.edu/data/Planck/release_2/software/) and fetch the additional likelihood products required by the intended analysis. Preserve the archive filenames and internal directory layouts when restoring the historical local cache.

