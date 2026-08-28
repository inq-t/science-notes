---
inq.module: "codata-2022-fundamental-physical-constants"
inq.include:
  - "./"
inq.ambient:
  - "**"
---
# CODATA 2022 Fundamental Physical Constants

The NIST ASCII table for the 2022 CODATA adjustment lists 355 fundamental-constant records with their adjusted values, standard uncertainties, and units. It is the machine-readable comparison source used by the workspace's Newton-constant and Planck-scale calculations; the accompanying NIST PDF is a human-readable presentation of the same release, not an independent dataset.

## Metadata

- **Dataset:** Fundamental Physical Constants — Complete Listing, 2022 CODATA adjustment.
- **Producer:** CODATA Task Group on Fundamental Constants.
- **Publisher:** National Institute of Standards and Technology (NIST).
- **Adjustment year:** 2022.
- **Retrieved locally:** 2026-08-23.
- **Local file:** `deriving-value-of-g/sources/data/nist-2022-codata-all-constants.txt`.
- **Git status:** the 40,801-byte table is tracked.
- **SHA-256:** `77fb90e66c40db3e6eb16630bc9c88e4c7c8beddbe5e71be406f2f26e3f67e67`.

## Structure

The fixed-width table has 355 records and four logical fields: quantity name, adjusted value, standard uncertainty, and unit. Spaces embedded in the value and uncertainty fields group digits and are not field separators. Some dimensionless constants have a blank unit.

The neighboring `nist-2022-codata-recommended-values.pdf` is NIST's extensive human-readable listing for the same adjustment. It can clarify typography and definitions, but parsers should use the ASCII table and verify the hash above.

## Fetch

Download the current NIST ASCII alias from [NIST's complete constants table](https://physics.nist.gov/cuu/Constants/Table/allascii.txt). The companion [NIST PDF listing](https://physics.nist.gov/cuu/pdf/all.pdf) is available separately.

These NIST URLs are mutable aliases and may later point to a newer CODATA adjustment. To reproduce the workspace calculations, confirm that the downloaded table identifies itself as the **2022 CODATA adjustment** and matches the frozen SHA-256 digest above.

