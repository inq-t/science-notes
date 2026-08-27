# Pantheon+SH0ES Distance Likelihood

The Pantheon+SH0ES distance release pairs a 1,701-row Type Ia supernova table with its full statistical-plus-systematic covariance. The same files support both a Hubble-diagram shape analysis and an absolute-distance analysis that retains Cepheid-host calibrators; those are selections from one ordered likelihood dataset, not separate copies.

## Metadata

- **Dataset:** Pantheon+SH0ES Hubble diagram and statistical-plus-systematic covariance.
- **Creators:** Pantheon+ and SH0ES collaborations.
- **Release:** 2022 public data release.
- **Associated articles:** [[library/pantheon-plus-analysis-cosmological-constraints/entry|The Pantheon+ Analysis: Cosmological Constraints]] and [[library/comprehensive-local-hubble-constant-measurement/entry|A Comprehensive Measurement of the Local Value of the Hubble Constant]].
- **Local storage:** `causal-scale-theory/sources/late-time-background/`.
- **Git status:** both files are tracked; together they occupy about 32.3 MiB.

## Structure

`Pantheon+SH0ES.dat` contains 1,701 rows and 47 columns, including multiple redshift frames, corrected apparent magnitude, SH0ES distance modulus, calibrator flags, light-curve parameters, host properties, and uncertainty diagnostics. It covers $0.00122\leq z_{\mathrm{HD}}\leq2.26137$, contains 1,543 distinct `CID` values, and marks 77 rows as calibrators. Repeated `CID` values are distinct ordered observations, not duplicate rows.

`Pantheon+SH0ES_STAT+SYS.cov` begins with the dimension 1,701 followed by $1701^2$ flattened covariance entries. Its ordering is exactly the table's row ordering. Slice the table and both covariance axes with the same mask.

| File | Bytes | SHA-256 |
|---|---:|---|
| `Pantheon+SH0ES.dat` | 579,283 | `1cb0fc379ef066afdc2ffd1857681cc478024570d8a3eba284fb645775198cf8` |
| `Pantheon+SH0ES_STAT+SYS.cov` | 33,284,960 | `abf806d966485e64afdb359c87bffc0ecc00d05eff0a31ced66f247385df0fdc` |

The workspace's shape-only receipt selects $z_{\mathrm{HD}}>0.01$ and removes calibrators, leaving 1,580 rows. The calibrated receipt instead keeps rows satisfying $(z_{\mathrm{HD}}>0.01)\lor\mathtt{IS\_CALIBRATOR}$ and uses the released `CEPH_DIST` values. Pantheon+SH0ES overlaps scientifically with DES-Dovekie, but the two are materially different supernova reductions and must remain separate dataset identities.

## Fetch

Download both files from the official Pantheon+SH0ES DataRelease repository:

- [Hubble-diagram table](https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/Pantheon%2BSH0ES.dat)
- [statistical-plus-systematic covariance](https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/Pantheon%2BSH0ES_STAT%2BSYS.cov)

Place the pair together under the local-storage path above to use the existing receipt defaults. The scripts verify both hashes before fitting.

