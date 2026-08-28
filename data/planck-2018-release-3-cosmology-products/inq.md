---
inq.module: "planck-2018-release-3-cosmology-products"
inq.include:
  - "./"
inq.ambient:
  - ".gitignore"
---
# Planck 2018 Release-3 Cosmology Products

This Planck 2018 subset preserves the baseline TT, TE, EE, low-$\ell$, lowE posterior package, selected best-fit and binned spectra, and the Release-3 `clik` likelihood software and data. It is sufficient for the workspace's scalar-calibration receipts and conventional likelihood setup, but it is not the complete 11 GB Planck posterior grid or the map-and-simulation archive.

## Metadata

- **Dataset:** Planck Public Data Release 3 cosmology products.
- **Creator:** Planck Collaboration.
- **Publisher:** ESA Planck Legacy Archive, mirrored by NASA/IPAC IRSA.
- **Release:** 2018 products; posterior and likelihood data R3.00, likelihood code and selected spectra R3.01/R3.02.
- **Associated article:** [[library/planck-2018-cosmological-parameters/inq|Planck 2018 Results VI: Cosmological Parameters]].
- **Retrieved locally:** 2026-08-22.
- **Local cache:** `data/planck-2018-release-3-cosmology-products/local/` (historically 642 files and 456,370,511 bytes including extracted working trees).
- **Git status:** `local/` is intentionally ignored and excluded from the module inventory; this note and its cache policy remain available in a blob-free clone.

## Posterior and compact spectra

`COM_CosmoParams_base-plikHM-TTTEEE-lowl-lowE_R3.00.zip` is the canonical baseline posterior archive (65,362,284 bytes; SHA-256 `52cf6793f14e250ffc1436ce7f6fe6d92f6a066c433ec9efc66e4178f3d45a1f`). Its 169 archive entries exactly match the 169-file extracted `base-plikHM-TTTEEE-lowl-lowE/` tree, which occupies approximately 216 MB.

The local cache also retains:

- a best-fit parameter vector and its theory spectrum;
- compact TT, TE, and EE binned spectra; and
- the published 68% parameter table.

The top-level best-fit parameter and theory files are byte-identical to convenience copies inside the extracted posterior tree. They are left in place because the official release exposes both paths and existing receipts refer to the top-level archive geometry.

## Likelihood products

| Product | Archive bytes | SHA-256 | Extracted working tree |
|---|---:|---|---|
| Baseline likelihood data R3.00 | 60,323,470 | `0b73171e3acc671c28184466a45485a2d1c1d93676b832abdfe688c7b04024e6` | `clik-data-baseline-r3/` |
| Extra lensing data R3.00 | 815,162 | `b38ca13efeb5cb57e53edba01a7ea64aee5bf13983be553adbf0375ed7703e8c` | `clik-data-extra-lensing-r3/` |
| `clik` code R3.01 | 2,395,386 | `ea641f7ba6a1cdc6b6271079b2bb70613944260e7de57d53fee2516b77d68c8d` | `clik-code-v3/` |

Repeated matrices, templates, and metadata inside the Planck likelihood tree are part of fixed TT and TTTEEE package layouts. Removing those exact copies would break runtime-relative lookups. Likewise, files shared byte-for-byte with the older `clik` 2 tree are software-version overlap rather than duplicate observational records.

The active late-time background receipt reads selected extracted chains and locates the posterior ZIP through their relative ancestry. Preserve the archive/extraction geometry unless that receipt and its recorded provenance are deliberately updated and rerun.

## Fetch

Direct IRSA downloads are:

- [baseline posterior archive](https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/cosmoparams/COM_CosmoParams_base-plikHM-TTTEEE-lowl-lowE_R3.00.zip)
- [baseline likelihood data](https://irsa.ipac.caltech.edu/data/Planck/release_3/software/COM_Likelihood_Data-baseline_R3.00.tar.gz)
- [extra lensing likelihood data](https://irsa.ipac.caltech.edu/data/Planck/release_3/software/COM_Likelihood_Data-extra-lensing-ext_R3.00.tar.gz)
- [`clik` code](https://irsa.ipac.caltech.edu/data/Planck/release_3/software/COM_Likelihood_Code-v3.0_R3.01.tar.gz)
- [best-fit parameter vector](https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/cosmoparams/COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum_R3.01.txt)
- [best-fit theory spectrum](https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/cosmoparams/COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum-theory_R3.01.txt)
- [TT binned spectrum](https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/cosmoparams/COM_PowerSpect_CMB-TT-binned_R3.01.txt)
- [TE binned spectrum](https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/cosmoparams/COM_PowerSpect_CMB-TE-binned_R3.02.txt)
- [EE binned spectrum](https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/cosmoparams/COM_PowerSpect_CMB-EE-binned_R3.02.txt)
- [68% parameter table](https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/cosmoparams/result_table_2018_68pcp120.pdf)

The [Release-3 cosmological-parameter index](https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/cosmoparams/) and [likelihood-software index](https://irsa.ipac.caltech.edu/data/Planck/release_3/software/index.html) list additional products. Restore required files under the local-cache path and pass their extracted chain directory explicitly to receipts that use it.
