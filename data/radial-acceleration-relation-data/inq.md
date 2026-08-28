---
inq.module: "radial-acceleration-relation-data"
inq.include:
  - "./"
inq.ambient:
  - "**"
---
# Radial-Acceleration Relation Data

The machine-readable radial-acceleration-relation release contains 2,693 resolved pairs of baryonic and observed acceleration from 153 disk galaxies, plus the 14-bin aggregation used in the published figure. The binned table is a derived summary of the resolved relation, not a second independent sample.

## Metadata

- **Dataset:** Radial Acceleration Relation resolved measurements and plotted bins.
- **Creators:** Federico Lelli, Stacy S. McGaugh, James M. Schombert, and Marcel S. Pawlowski.
- **Publication:** 2017; the associated preprint appeared in 2016.
- **Publisher:** SPARC data site, Case Western Reserve University.
- **Associated article:** [“One Law to Rule Them All: The Radial Acceleration Relation of Galaxies”](https://arxiv.org/abs/1610.08981), *The Astrophysical Journal* 836 (2017), 152.
- **Retrieved locally:** 2026-08-23.
- **Local storage:** `vendor/entropic-gravity/sources/data/`.
- **Git status:** both compact tables are tracked.

## Structure

`RAR.mrt` is a CDS-style table with a byte-by-byte schema in its header. Its 2,693 records give $\log_{10}g_{\mathrm{bar}}$, its uncertainty, $\log_{10}g_{\mathrm{obs}}$, and its uncertainty for 153 galaxies. Acceleration columns marked $\mathrm{m\,s^{-2}}$ contain base-ten logarithms in those units.

`RARbins.mrt` contains 14 bins with mean baryonic and observed accelerations, scatter, and the number of contributing measurements. Its `N` column sums to 2,630, so it is an aggregation/subset of the resolved table rather than a lossless alternate serialization.

| File | Records | Bytes | SHA-256 |
|---|---:|---:|---|
| `RAR.mrt` | 2,693 | 68,136 | `24aa7059dab7fa44787f7c11191052489899819370f6508621674769f3b72833` |
| `RARbins.mrt` | 14 | 1,202 | `d543cab7b720a4f14152ccc8158f7823072ce65a9c5b403d7c401b3f039a79d7` |

The resolved accelerations descend from SPARC rotation curves and baryonic mass models. They therefore inherit distance, inclination, stellar mass-to-light, gas, and selection assumptions; the RAR files are not statistically independent of the SPARC source data.

## Fetch

Download the official tables from the SPARC site:

- [resolved RAR measurements](https://astroweb.case.edu/SPARC/RAR.mrt)
- [binned RAR summary](https://astroweb.case.edu/SPARC/RARbins.mrt)

The files contain no explicit standalone license statement in their headers. Scholarly reuse should cite the associated article and follow the source site's attribution expectations.
