# Observational Data Cache

This ignored directory is a local working cache for large, reproducible observational downloads and their extracted runtime trees. Canonical descriptions, metadata, and fetch instructions now live in dataset modules under `data/`, so a Git clone retains the research graph without downloading the roughly 5.34 GiB cache.

## Canonical dataset modules

- [[data/act-dr6-cosmology-products/inq|ACT DR6 cosmology products]]
- [[data/bicep-keck-2018-data-products/inq|BICEP/Keck 2018 data products]]
- [[data/planck-2018-release-3-cosmology-products/inq|Planck 2018 Release-3 cosmology products]]
- [[data/planck-2015-release-2-cosmology-products/inq|Planck 2015 Release-2 cosmology products]]
- [[data/bicep2-keck-planck-2015-joint-likelihood/inq|BICEP2/Keck–Planck 2015 joint likelihood]]
- [[data/wmap-seven-year-power-spectra/inq|WMAP seven-year power spectra]]

## Storage policy

The root `.gitignore` excludes every payload below this directory while retaining this note. Download archives are immutable retrieval artifacts; extracted directories are derivative working copies retained where legacy likelihoods require fixed relative paths. Exact repeated files inside Planck and BK18 layouts are package components, not safe deletion targets.

No active data or receipt was moved during the wrapper refactor. In particular, the Planck 2018 posterior archive and extracted chain tree retain the relative geometry expected by the late-time background receipt.

## Deliberately absent products

The cache does not mirror the 66.72 GB BK18 full chains, the 11 GB Planck Release-3 all-model grid, the Planck SMICA maps and FFP10 simulation ensemble, the roughly 988 MB WMAP7 full likelihood, the roughly 300 MB Planck Release-2 baseline likelihood, or ACT map-level simulations. These are size and reproducibility boundaries: none is needed for the claims currently audited in the workspace.

[[causal-wall-spectral-theory/sources/origins|Source origins]] records the upstream release locations, and [[causal-wall-spectral-theory/sources/checksums|download integrity]] freezes the locally mirrored archives and compact products.
