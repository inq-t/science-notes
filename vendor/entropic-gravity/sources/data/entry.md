# SPARC and Radial-Acceleration Data

Four official machine-readable tables are vendored locally because they are the compact observational data most directly connected to finite-galaxy tests of Verlinde’s apparent-gravity relation. They preserve the SPARC galaxy sample, resolved baryonic mass models, the 2,693-point radial-acceleration relation, and its 14 plotted bins.

## Local tables

| File | Content | Records |
|---|---|---:|
| [[vendor/entropic-gravity/sources/data/SPARC_Lelli2016c.mrt|SPARC_Lelli2016c.mrt]] | galaxy-level distances, inclinations, luminosities, scale lengths, surface brightnesses, H I masses, rotation velocities, quality flags | 175 galaxies |
| [[vendor/entropic-gravity/sources/data/MassModels_Lelli2016c.mrt|MassModels_Lelli2016c.mrt]] | resolved radius, observed velocity, uncertainty, gas/disk/bulge velocity contributions, and surface brightness | 3,391 radial measurements |
| [[vendor/entropic-gravity/sources/data/RAR.mrt|RAR.mrt]] | \(\log_{10}g_{\mathrm{bar}}\), its uncertainty, \(\log_{10}g_{\mathrm{obs}}\), and its uncertainty | 2,693 measurements from 153 galaxies |
| [[vendor/entropic-gravity/sources/data/RARbins.mrt|RARbins.mrt]] | mean baryonic and observed accelerations, scatter, and population count behind the binned RAR figure | 14 bins |

Each file is a CDS-style machine-readable table with a byte-by-byte schema in its header. Acceleration columns labeled [m/s2] contain base-ten logarithms of accelerations measured in \(\mathrm{m\,s^{-2}}\), as the file descriptions state.

## Relation to the theory

For a baryonic mass profile \(M_B(r)\), Verlinde’s spherical saturated relation predicts

$$
M_D^2(r)
=\frac{a_0r^2}{6G}
\frac{d}{dr}\!\left[rM_B(r)\right].
$$

The mass-model table supplies the resolved observed and baryonic velocity components from which one can reconstruct accelerations. The RAR table supplies the already reduced pair \((g_{\mathrm{bar}},g_{\mathrm{obs}})\) used for a direct relation-level comparison.

The tables do not themselves provide a unique test of the original theory:

- SPARC galaxies are disks, while Verlinde’s controlled formula is spherical;
- stellar mass-to-light ratios and gas corrections enter \(g_{\mathrm{bar}}\);
- distances and inclinations propagate into both axes;
- the reduced RAR points are not independent of the SPARC modeling choices; and
- fitting an acceleration relation does not test cosmology, lensing, or the proposed de Sitter microphysics.

The correct use is to reproduce a declared finite-galaxy extension and audit its residuals, not to treat the table as native data from a closed emergent-gravity field theory.

## Provenance

The four files were downloaded from the official SPARC data site on 2026-08-23. Their exact upstream URLs are recorded in [[vendor/entropic-gravity/sources/origins|origins]] and their hashes in [[vendor/entropic-gravity/sources/checksums|checksums]].

The files do not carry an explicit standalone license statement in their headers. Scholarly reuse should cite the corresponding SPARC and radial-acceleration papers and follow the source site’s attribution expectations.
