# Entropic-Gravity Source Index

This index describes a frozen, locally reviewable corpus for the Jacobson and Verlinde lineages: 34 PDF versions, their 34 arXiv source payloads, one local arXiv metadata record, and four official SPARC/RAR machine-readable tables. Each article and its source payloads are now owned by one module under `library/`; this vendor module retains the shared metadata, bounded datasets, provenance, and interpretive organization. The corpus includes primary proposals, immediate mathematical qualifications, covariant completions, and representative galaxy, Solar-System, lensing, dwarf, and cluster tests through the 2026 dwarf-spheroidal comparison.

## Foundational papers

### Jacobson lineage

- [[library/thermodynamics-of-spacetime-the-einstein-equation-of-state/inq|Thermodynamics of Spacetime: The Einstein Equation of State]]
- [[library/non-equilibrium-thermodynamics-of-spacetime/inq|Non-equilibrium Thermodynamics of Spacetime]]
- [[library/gravitation-and-vacuum-entanglement-entropy/inq|Gravitation and Vacuum Entanglement Entropy]]
- [[library/entanglement-equilibrium-and-the-einstein-equation/inq|Entanglement Equilibrium and the Einstein Equation — current v4]]
- [[library/entanglement-equilibrium-and-the-einstein-equation/inq|Entanglement Equilibrium and the Einstein Equation — historical v1]]
- [[library/equilibrium-to-einstein-entanglement-thermodynamics-and-gravity/inq|Equilibrium to Einstein: Entanglement, Thermodynamics, and Gravity]]
- [[library/gravitational-thermodynamics-of-causal-diamonds-in-a-ds/inq|Gravitational Thermodynamics of Causal Diamonds in (A)dS]]

### Verlinde lineage

- [[library/on-the-origin-of-gravity-and-the-laws-of-newton/inq|On the Origin of Gravity and the Laws of Newton]]
- [[library/emergent-gravity-and-the-dark-universe/inq|Emergent Gravity and the Dark Universe]]

## Mathematical qualifications and theory development

- [[library/conservative-entropic-forces/inq|Conservative Entropic Forces]]
- [[library/gravity-is-not-an-entropic-force/inq|Gravity Is Not an Entropic Force]]
- [[library/entropic-gravity-entropy-postulate-screens-quantum-mechanics/inq|On Entropic Gravity: The Entropy Postulate, Screens, and Quantum Mechanics]]
- [[library/comments-on-jacobson-s-entanglement-equilibrium-and-the-einstein-equation/inq|Comments on Jacobson’s Entanglement Equilibrium]]
- [[library/entanglement-entropy-excited-states-einstein-equation/inq|Entanglement Entropy of Excited States and the Einstein Equation]]
- [[library/entanglement-equilibrium-for-higher-order-gravity/inq|Entanglement Equilibrium for Higher-Order Gravity]]
- [[library/a-covariant-version-of-verlinde-s-emergent-gravity/inq|A Covariant Version of Verlinde’s Emergent Gravity]]
- [[library/a-note-on-a-covariant-version-of-verlinde-s-emergent-gravity/inq|A Note on a Covariant Version of Verlinde’s Emergent Gravity]]
- [[library/field-equations-and-particle-motion-in-covariant-emergent-gravity/inq|Field Equations and Particle Motion in Covariant Emergent Gravity]]
- [[library/inconsistencies-in-verlinde-s-emergent-gravity/inq|Inconsistencies in Verlinde’s Emergent Gravity]]
- [[library/comment-on-inconsistencies-in-verlinde-s-emergent-gravity/inq|Comment on “Inconsistencies in Verlinde’s Emergent Gravity”]]
- [[library/a-critique-of-covariant-emergent-gravity/inq|A Critique of Covariant Emergent Gravity]]

## Empirical papers

- [[library/sparc-mass-models-for-175-disk-galaxies/inq|SPARC: Mass Models for 175 Disk Galaxies]]
- [[library/the-radial-acceleration-relation-in-rotationally-supported-galaxies/inq|The Radial Acceleration Relation in Rotationally Supported Galaxies]]
- [[library/first-weak-lensing-test-of-emergent-gravity/inq|First Weak-Lensing Test of Verlinde’s Emergent Gravity]]
- [[library/verlinde-s-emergent-gravity-versus-mond-and-the-case-of-dwarf-spheroidals/inq|Verlinde’s Emergent Gravity versus MOND and Dwarf Spheroidals]]
- [[library/testing-verlinde-s-emergent-gravity-with-the-radial-acceleration-relation/inq|Testing Verlinde’s Emergent Gravity with the Radial Acceleration Relation]]
- [[library/emergent-gravity-in-galaxies-and-in-the-solar-system/inq|Emergent Gravity in Galaxies and in the Solar System]]
- [[library/testing-verlinde-s-emergent-gravity-in-early-type-galaxies/inq|Testing Verlinde’s Emergent Gravity in Early-Type Galaxies]]
- [[library/testing-emergent-gravity-with-isolated-dwarf-galaxies/inq|Testing Emergent Gravity with Isolated Dwarf Galaxies]]
- [[library/testing-emergent-gravity-with-mass-densities-of-galaxy-clusters/inq|Testing Emergent Gravity with Galaxy-Cluster Mass Densities]]
- [[library/testing-emergent-gravity-on-galaxy-cluster-scales/inq|Testing Emergent Gravity on Galaxy-Cluster Scales]]
- [[library/kids-1000-weak-lensing-radial-acceleration-relation/inq|The KiDS-1000 Weak-Lensing Radial Acceleration Relation]]
- [[library/smacs-j0723-test-of-emergent-gravity/inq|A Test with SMACS J0723.3-7327]]
- [[library/comparison-of-mond-and-verlinde-s-emergent-gravity-in-dwarf-spheroidals/inq|Comparison of MOND and Verlinde’s Emergent Gravity in Dwarf Spheroidals]]

The bounded local galaxy products are documented by [[data/sparc-galaxy-sample-and-mass-models/inq|the SPARC dataset module]] and [[data/radial-acceleration-relation-data/inq|the radial-acceleration dataset module]]. Large KiDS, GAMA, X-ray, and cluster survey products were not mirrored: reproducing the published selections would require much larger survey archives and analysis pipelines, not one stable source table.

## Source payloads and metadata

Every library-owned PDF from this corpus has a matching source payload in the same article module. Some old arXiv submissions are a single gzip-compressed TeX file rather than a tar archive; the `.tar.gz` filenames preserve one uniform local convention.

[[vendor/entropic-gravity/sources/arxiv-metadata.xml|The local arXiv Atom record]] preserves the 33 unique identifiers, current version labels, authors, titles, abstracts, categories, and update dates returned on 2026-08-23. The historical Jacobson v1 is a second frozen version of identifier 1505.04753.

[[vendor/entropic-gravity/sources/origins|Origins]] records upstream locations and retrieval policy. [[vendor/entropic-gravity/sources/checksums|Checksums]] freezes every archived source artifact.

## Verification

All 34 library-owned PDFs were opened with an independent PDF parser, had at least one page, and yielded nonempty first-page text; together they contain 612 pages. The first page of every PDF was also rendered and reviewed as one contact sheet. All 34 colocated arXiv source payloads were successfully decompressed; 28 are tar archives and six are gzip-compressed single files. The four vendor-owned data tables are nonempty, include their machine-readable schemas, and have the expected record counts.

This verifies archive integrity and visual readability. It does not certify the truth of the papers’ claims.
