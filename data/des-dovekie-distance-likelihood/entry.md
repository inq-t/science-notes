# DES-Dovekie Distance Likelihood

The DES-Dovekie supernova release pairs an ordered 1,820-row Hubble diagram with a packed statistical-plus-systematic precision matrix. It is a recalibrated DES five-year distance reduction used here as a robustness test of the late-time background fit, not a duplicate or interchangeable serialization of Pantheon+.

## Metadata

- **Dataset:** DES-Dovekie Hubble diagram and statistical-plus-systematic precision matrix.
- **Creator:** Dark Energy Survey Supernova Program.
- **Release:** DES-SN5YR public reduction current at commit `c9a4fcafc4cbd19bd750dee47fc76194a45c181f`.
- **Associated article:** [[library/dark-energy-survey-supernova-program-reanalysis/entry|Dark Energy Survey Supernova Program: Reanalysis of DES-SN5YR with DES-Dovekie]].
- **Local storage:** `causal-scale-theory/sources/late-time-background/`.
- **Git status:** both compact files are tracked.

## Structure

`DES-Dovekie_HD.csv` is a SNANA-style whitespace table despite its `.csv` suffix. It contains 1,820 uniquely identified supernova rows and nine declared fields: `CID`, `IDSURVEY`, `zHD`, `zHEL`, `MU`, `MUERR`, `MUERR_VPEC`, `MUERR_SYS`, and `PROBIA_BEAMS`. The sample spans $0.02509\leq z_{\mathrm{HD}}\leq1.14418$.

`DES-Dovekie_STAT+SYS.npz` contains `nsn = 1820` and 1,657,110 packed `float32` values, exactly $1820\cdot1821/2$. Those values are the upper triangle of the **inverse covariance** in the Hubble-diagram row order. They must be mirrored to form the symmetric precision matrix; treating them as covariance entries reverses the likelihood.

| File | Bytes | SHA-256 |
|---|---:|---|
| `DES-Dovekie_HD.csv` | 148,002 | `2f57019d783eaa976df80a41b0054171a2d994ee9808d715ce850c2df5720aaf` |
| `DES-Dovekie_STAT+SYS.npz` | 6,244,951 | `ffd3124b32148b1372bd95fda9299269f0352a9f8eee02d416c610e38495463b` |

The CobayaSampler mirror renames the precision file `covtot_inv_000.npz`; that remote file is byte-identical. Its normalized distance table retains the same eight numerical columns and row order while replacing `CID` with a row index. No second local copy is present, so there is nothing to delete or move.

## Fetch

Download the primary collaboration products directly from DES-SN5YR:

- [Hubble diagram](https://raw.githubusercontent.com/des-science/DES-SN5YR/main/4_DISTANCES_COVMAT/DES-Dovekie_HD.csv)
- [packed precision matrix](https://raw.githubusercontent.com/des-science/DES-SN5YR/main/4_DISTANCES_COVMAT/STAT%2BSYS.npz)

The collaboration's [CosmoSIS likelihood implementation](https://github.com/des-science/DES-SN5YR/blob/main/5_COSMOLOGY/Dovekie_cosmosis_likelihood.py) defines the row mask, two-redshift luminosity distance, unpacking convention, and analytic nuisance treatment. Place both files under the local-storage path above, together with the DESI pair, to use the existing robustness-receipt defaults.

