---
inq.module: "bicep2-keck-planck-2015-joint-likelihood"
inq.include:
  - "./"
inq.ambient:
  - ".gitignore"
---
# BICEP2/Keck–Planck 2015 Joint Likelihood

The January 2015 BICEP2/Keck Array and Planck joint-analysis release packages the bandpowers, noise estimates, window functions, bandpasses, foreground model, and CosmoMC configuration needed to reproduce the collaboration's joint likelihood. It is a likelihood-ready reduction of the observations, not raw map data.

## Metadata

- **Dataset:** BICEP2/Keck Array and Planck Joint Analysis Data Products.
- **Creators:** BICEP2/Keck and Planck collaborations.
- **Release:** January 2015; the packaged README is dated 2015-01-30.
- **Distribution:** BICEP/Keck public products and NASA LAMBDA.
- **Retrieved locally:** 2026-08-22.
- **Local cache:** `data/bicep2-keck-planck-2015-joint-likelihood/local/`.
- **Git status:** `local/` is intentionally ignored and excluded from the module inventory; this note and its cache policy remain available in a blob-free clone.

## Contents

The canonical download is `BKP_likelihood_cosmomc_20150131.tgz` (318,962 bytes; SHA-256 `64d8c1b0cd90eff9ea702907365260d88f1c7227dd2a88b1464f8bbc21c51802`). Its 58-file extracted tree is stored locally as `bkp-likelihood/` and contains:

- the preferred detector-set bandpowers, noise, and ancillary likelihood inputs;
- an alternate year-split data selection;
- bandpower window functions and instrument bandpasses;
- CosmoMC and GetDist configurations for the paper's fiducial and alternative analyses; and
- the Fortran implementation of the CMB-plus-foreground model.

The 318 KB archive and approximately 4.1 MB extracted tree are two representations of the same release. Both are retained because the archive is the immutable fetch artifact while CosmoMC consumes the extracted relative layout. Files inside that layout must not be deduplicated or moved independently.

## Fetch

Download the release archive from [NASA LAMBDA](https://lambda.gsfc.nasa.gov/data/suborbital/BICEP2KP/BKP_likelihood_cosmomc_20150131.tgz). Extract it without flattening directories, then place the resulting tree under the local-cache path above.

The likelihood was tested by its authors against the January 2015 CosmoMC release. Reproducing it with current software may require a compatible legacy environment in addition to these data products.
