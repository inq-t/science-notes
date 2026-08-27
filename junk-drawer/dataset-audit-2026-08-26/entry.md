# Dataset Audit — 2026-08-26

This audit inventories external datasets outside `inbox/`, separates true duplication from related scientific products, and records the wrapper-only refactor that made the workspace clone-friendly without moving any payload consumed by experiments or receipts.

## Scope

The scan included tracked, untracked, hidden, and Git-ignored files throughout the workspace, excluding `.git/`, `inbox/`, article payloads already owned by `library/`, and generated receipt ledgers as primary-dataset candidates. Vendored likelihood and reproduction-code trees were inspected for data dependencies and duplicate payloads but were not treated as freely rearrangeable storage.

## Inventory

| Collection | Payload files | Bytes | Git policy |
|---|---:|---:|---|
| CWST observational cache | 1,566 ignored payloads plus its tracked cache note | 5,733,165,306 | large, reproducible downloads ignored |
| Late-time background inputs | 6 | 40,260,215 | tracked |
| SPARC and RAR tables | 4 | 367,115 | tracked |
| CODATA ASCII table | 1 | 40,801 | tracked |

The CWST cache comprises ACT DR6, Planck 2018, BK18, Planck 2015/BKP, and WMAP7 release products. A tracked 5,391,360-byte FITS file inside the ACT code snapshot is a simulated test fixture, not the released ACT CMB-only observational product.

## Exact duplicates

The byte-saving duplicate tally used a conservative payload filter: it excluded both Planck `clik` source-code trees, seven empty ACT `.locked` sentinels, and three groups of repeated Planck `.properties.ini` configuration files. Those files were still inspected for dependency risk, but were not counted as removable scientific payload. Within that declared filter, hashing found 77 SHA-256 groups involving 230 files and 13,867,952 redundant bytes. These repeats are almost entirely fixed-layout components inside Planck and BK18 likelihood packages:

- Planck TT and TTTEEE layouts repeat matrices, templates, and metadata;
- Planck's top-level best-fit parameter and theory files repeat official convenience copies inside the extracted posterior tree;
- BK18 `dust` and `dust_incEE` layouts repeat bandpasses and parameter names while differing in their scientific data, covariance, windows, and configuration; and
- the ACT 20-bin and 50-bin packages repeat one `dataset_trace.pkl` while their other 214 matched paths differ.

None is a safe file-level deletion. The likelihoods resolve fixed relative paths, and deleting an internal copy would damage the released package interface. No exact duplicate occurs among the six late-time inputs, the three WMAP spectra, the CODATA table, the downloaded archives, or the locally retained SPARC/RAR tables.

## Near duplicates and derived products

Twenty-three downloaded archives have matching extracted working trees. The archives occupy about 0.935 GiB compressed and the trees about 4.403 GiB extracted. Their path inventories match without unexplained extras. Both representations were retained: the archive freezes the retrievable artifact and hash, while legacy software consumes the extracted relative layout.

Scientifically related products were not collapsed:

- ACT full multifrequency SACC and CMB-only SACC are distinct $6840\times6840$ and $135\times135$ interfaces;
- ACT 20-bin and 50-bin products are alternate binnings, not duplicate tables;
- ACT, Planck, and joint chains are posterior outputs from different likelihood combinations;
- BK18 public bandpasses add an E-mode response column not present in the likelihood serialization;
- Planck `clik` 2 and 3 are versioned software releases, with both identical and changed files;
- Pantheon+SH0ES and DES-Dovekie are distinct calibrations and reductions;
- SPARC mass models, resolved RAR points, and RAR bins form a source-to-reduction-to-aggregation lineage; and
- the CODATA PDF and ASCII table are human- and machine-readable presentations of one adjustment.

## Changes made

Twelve canonical modules were created under `data/`, each with a searchable `entry.md`, a module manifest, provenance, direct fetch URLs, structure information, and local Git/storage status:

- [[data/act-dr6-cosmology-products/entry|ACT DR6 cosmology products]]
- [[data/bicep-keck-2018-data-products/entry|BICEP/Keck 2018 data products]]
- [[data/bicep2-keck-planck-2015-joint-likelihood/entry|BICEP2/Keck–Planck 2015 joint likelihood]]
- [[data/codata-2022-fundamental-physical-constants/entry|CODATA 2022 constants]]
- [[data/des-dovekie-distance-likelihood/entry|DES-Dovekie distance likelihood]]
- [[data/desi-dr2-bao-gaussian-likelihood/entry|DESI DR2 BAO Gaussian likelihood]]
- [[data/pantheon-plus-shoes-distance-likelihood/entry|Pantheon+SH0ES distance likelihood]]
- [[data/planck-2015-release-2-cosmology-products/entry|Planck 2015 Release-2 products]]
- [[data/planck-2018-release-3-cosmology-products/entry|Planck 2018 Release-3 products]]
- [[data/radial-acceleration-relation-data/entry|radial-acceleration-relation data]]
- [[data/sparc-galaxy-sample-and-mass-models/entry|SPARC sample and mass models]]
- [[data/wmap-seven-year-power-spectra/entry|WMAP seven-year power spectra]]

Conceptual notes now link to these wrappers. Direct payload URLs remain in provenance and checksum ledgers where they belong. The old CWST and entropic-gravity data notes remain as short local-cache bridges so historical links do not break.

No data file was moved, renamed, rewritten, or deleted. Consequently, no Python path or generated receipt changed. A scoped `/data/*/local/` ignore rule was added for future large per-module caches; small datasets placed beside a module's `entry.md` remain trackable.

## Verification

Each module was registered and linted before the next was created. The final checks verify workspace membership, wrapper links, H1-plus-summary openings, trackability of Markdown/manifests, continued ignoring of the large CWST cache, hashes of all active late-time inputs, and the unchanged behavior of the four background-fit receipts.
