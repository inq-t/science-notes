---
inq.module: "wmap-seven-year-power-spectra"
inq.include:
  - "./"
inq.ambient:
  - ".gitignore"
---
# WMAP Seven-Year Power Spectra

The WMAP seven-year version 4.1 release provides combined temperature and polarization angular-power-spectrum estimates as three compact text tables: TT, TE, and EE. These tables are useful for plotting and limited spectrum-level audits, but they are not a substitute for the full WMAP likelihood because neighboring multipoles are coupled and the low-multipole likelihood is not generally Gaussian.

## Metadata

- **Dataset:** WMAP Seven-Year Combined Power Spectra.
- **Publisher:** NASA Legacy Archive for Microwave Background Data Analysis (LAMBDA), for the WMAP Science Team.
- **Release:** version 4.1; TT and TE dated June 2010, EE dated October 2010.
- **Retrieved locally:** 2026-08-22.
- **Local cache:** `data/wmap-seven-year-power-spectra/local/`.
- **Git status:** `local/` is intentionally ignored and excluded from the module inventory; this note and its cache policy remain available in a blob-free clone.

## Contents

Each whitespace-delimited table has five columns: multipole $\ell$, the corresponding $\ell(\ell+1)C_\ell/(2\pi)$ estimate in $\mu\mathrm K^2$, a diagonal-error estimate, its measurement-error contribution, and its cosmic-variance contribution.

| Product | Rows | Multipoles | Local filename | SHA-256 |
|---|---:|---:|---|---|
| TT | 1,199 | $2\ldots1200$ | `wmap_tt_spectrum_7yr_v4p1.txt` | `8732f59dadf860f93a24d3e445d1628a8e40c039199e24c084dc39732a828cea` |
| TE | 799 | $2\ldots800$ | `wmap_te_spectrum_7yr_v4p1.txt` | `4b3fd1c182a744e99c5351e872dcfab500fabcadcd71dae579846d1d8167c918` |
| EE | 1,023 | $2\ldots1024$ | `wmap_ee_spectrum_7yr_v4p1.txt` | `82842c8072dc0fb2517df34100624b85cbce77c7d568325080234a356b479ea9` |

The quoted error column is only a scale estimate. Use the release's full Fisher information or likelihood code for statistical inference.

## Fetch

Download the files directly from NASA LAMBDA:

- [TT spectrum](https://lambda.gsfc.nasa.gov/data/map/dr4/dcp/spectra/wmap_tt_spectrum_7yr_v4p1.txt)
- [TE spectrum](https://lambda.gsfc.nasa.gov/data/map/dr4/dcp/spectra/wmap_te_spectrum_7yr_v4p1.txt)
- [EE spectrum](https://lambda.gsfc.nasa.gov/data/map/dr4/dcp/spectra/wmap_ee_spectrum_7yr_v4p1.txt)

Place downloaded files under the local-cache path above when needed.
