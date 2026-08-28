---
inq.module: "sparc-galaxy-sample-and-mass-models"
inq.include:
  - "./"
inq.ambient:
  - "**"
---
# SPARC Galaxy Sample and Mass Models

SPARC—the Spitzer Photometry and Accurate Rotation Curves compilation—provides galaxy-level properties for 175 disk galaxies and 3,391 resolved rotation-curve mass-model rows. These are the source observational tables from which the workspace's reduced radial-acceleration relation descends.

## Metadata

- **Dataset:** SPARC galaxy sample and resolved baryonic mass models.
- **Creators:** Federico Lelli, Stacy S. McGaugh, and James M. Schombert.
- **Release:** 2016.
- **Publisher:** SPARC data site, Case Western Reserve University.
- **Associated article:** [[library/sparc-mass-models-for-175-disk-galaxies/inq|SPARC: Mass Models for 175 Disk Galaxies]].
- **Retrieved locally:** 2026-08-23.
- **Local storage:** `vendor/entropic-gravity/sources/data/`.
- **Git status:** both compact tables are tracked.

## Structure

`SPARC_Lelli2016c.mrt` has one row per galaxy and records distance, inclination, luminosity, scale lengths, surface brightness, H I mass, characteristic rotation velocity, and quality flags.

`MassModels_Lelli2016c.mrt` has one row per resolved radius and records the observed rotation velocity and uncertainty together with gas, stellar-disk, and bulge velocity contributions and surface-brightness information. Galaxy name plus radius is the natural record key; galaxy name alone is intentionally repeated across a rotation curve.

| File | Records | Bytes | SHA-256 |
|---|---:|---:|---|
| `SPARC_Lelli2016c.mrt` | 175 galaxies | 28,259 | `5aa0501f6b0d881fa579030e315e7b5b6ef561a5bd3a07472f9929c7e5728243` |
| `MassModels_Lelli2016c.mrt` | 3,391 radii | 269,518 | `9108994b12cc401b94a1768beca61c53ec354779385c9c9cc571049f3043244c` |

Both are CDS-style machine-readable tables with byte-by-byte schemas in their headers. [[data/radial-acceleration-relation-data/inq|The radial-acceleration dataset]] is a reduction of this observational lineage, not a duplicate local copy or an independent sample.

## Fetch

Download the official tables from the SPARC site:

- [galaxy-level sample](https://astroweb.case.edu/SPARC/SPARC_Lelli2016c.mrt)
- [resolved mass models](https://astroweb.case.edu/SPARC/MassModels_Lelli2016c.mrt)

The files contain no explicit standalone license statement in their headers. Scholarly reuse should cite the associated SPARC article and follow the source site's attribution expectations.

