# DESI DR2 BAO Gaussian Likelihood

The DESI Data Release 2 compact BAO likelihood consists of a 13-element distance vector and its $13\times13$ covariance. It records isotropic $D_V/r_s$ and anisotropic $D_M/r_s$, $D_H/r_s$ measurements from $z=0.295$ to $z=2.33$ and is the released Gaussian interface used by the workspace's late-time background receipts.

## Metadata

- **Dataset:** DESI DR2 Gaussian BAO likelihood, all combined galaxy and Ly$\alpha$ measurements.
- **Creator:** DESI Collaboration.
- **Release:** 2025 Data Release 2 cosmology products.
- **Associated article:** [[library/desi-dr2-results-ii/entry|DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints]].
- **Official release context:** [DESI DR2 BAO cosmology results](https://data.desi.lbl.gov/public/papers/y3/bao-cosmo-params/README.html).
- **Local storage:** `causal-scale-theory/sources/late-time-background/`.
- **Git status:** both compact text files are tracked.

## Structure

`desi_dr2_bao_mean.txt` has 13 rows with columns `z`, `value`, and `quantity`: one $D_V/r_s$, six $D_M/r_s$, and six $D_H/r_s$ entries. Its SHA-256 is `9ac154ab583ce759c0f7eef3c978c7c70a6ead2d18774caceadf1a350a640585`.

`desi_dr2_bao_cov.txt` is the matching symmetric $13\times13$ covariance matrix. Its SHA-256 is `252a143274c8a07c78694c119617d36594f6d7965d00319ca611c6ffb886e509`.

The two files form one dataset and must retain their shared ordering. They have no exact duplicate elsewhere in the workspace. A provisional 2026 Ly$\alpha$ published-Gaussian substitution in some receipts is a transcription from a paper, not a second released likelihood file.

## Fetch

Download the exact compact files from the CobayaSampler likelihood-data repository:

- [mean vector](https://raw.githubusercontent.com/CobayaSampler/bao_data/master/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_mean.txt)
- [covariance matrix](https://raw.githubusercontent.com/CobayaSampler/bao_data/master/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt)

Place both files together under the local-storage path above to use the existing receipt defaults. The fit scripts also accept a replacement directory through `--data-dir`, but that directory must contain the other paired late-time inputs expected by the selected receipt.

