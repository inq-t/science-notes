# Empirical Status

The empirically testable object in Verlinde’s 2016 programme is chiefly its saturated, static, spherical apparent-mass relation, not a complete relativistic gravity theory. Galaxy data exhibit the low-acceleration regularities that motivated the proposal, but finite-disc, dwarf, Solar-System, lensing, and cluster tests give mixed results and often require auxiliary GR or \(\Lambda\)CDM assumptions outside the theory’s own supplied dynamics. This review includes the literature archived here through the January 2026 dwarf-spheroidal comparison.

Jacobson’s equilibrium constructions are not rival galaxy-force laws. Under their premises they return the Einstein equation, so their empirical burden is carried by the validity and universality of those premises and by GR in the resulting regime.

## What is actually predicted

For isolated, static, approximately spherical systems, the saturated four-dimensional Verlinde relation is

$$
\int_0^r
\frac{GM_D^2(r')}{r'^2}\,dr'
=\frac{a_0}{6}M_B(r)r.
$$

Equivalently,

$$
M_D^2(r)
=\frac{a_0r^2}{6G}
\frac{d}{dr}\!\left[rM_B(r)\right].
$$

For a point mass,

$$
g_D^2=\frac{a_0}{6}g_B.
$$

These formulas predict an effective mass or acceleration after the baryonic profile and \(a_0\) are supplied. The original paper does not independently provide

- a nonspherical field equation;
- cosmological distances and growth;
- a relativistic lensing map;
- the time evolution of \(a_0\); or
- a theory of non-equilibrium clusters and colliding systems.

Consequently, many observations test the spherical formula embedded in an auxiliary gravitational and cosmological framework.

## Galaxy regularities and local data

The SPARC compilation contains high-quality rotation curves and baryonic mass models for 175 disk galaxies. The radial-acceleration-relation compilation contains 2,693 resolved measurements from 153 galaxies and displays a tight relation between observed acceleration \(g_{\mathrm{obs}}\) and the acceleration \(g_{\mathrm{bar}}\) predicted from baryons.

The source papers are archived as [[library/sparc-mass-models-for-175-disk-galaxies/inq|SPARC]] and [[library/the-radial-acceleration-relation-in-rotationally-supported-galaxies/inq|the radial acceleration relation]]. Their machine-readable tables are owned by [[data/sparc-galaxy-sample-and-mass-models/inq|the SPARC dataset module]] and [[data/radial-acceleration-relation-data/inq|the RAR dataset module]].

The existence of these regularities is the principal empirical motivation for a baryon-linked law. It does not by itself identify Verlinde’s microscopic explanation: MOND interpolation laws, dark-matter galaxy formation, and other baryon–halo relations can also be compared with the same data.

## Direct tests and later implementations

| Test | Reported result | Decisive qualification |
|---|---|---|
| [[library/testing-verlinde-s-emergent-gravity-with-the-radial-acceleration-relation/inq|Lelli, McGaugh, and Schombert 2017]] | The point-mass asymptote is correct, but finite disks predict too much inner discrepancy for fiducial stellar mass-to-light ratios and a radius-correlated residual not seen in the data. | Disk galaxies lie outside the original spherical derivation; nevertheless, a usable general theory must eventually describe them. |
| [[library/emergent-gravity-in-galaxies-and-in-the-solar-system/inq|Hees, Famaey, and Bertone 2017]] | Galaxy rotation-curve fits preferred an anomalously low \(H_0\), systematically low distances, and low stellar mass-to-light ratios. Applied in its stated spherical exterior regime, the same weak-field formula overpredicts anomalous Solar-System perihelion advances by roughly seven orders of magnitude. | This directly rules out universal use of the published weak-field formula, not every possible screened or otherwise modified completion of emergent gravity. The original proposal supplies no such completion. |
| [[library/testing-verlinde-s-emergent-gravity-in-early-type-galaxies/inq|Tortora et al. 2018]] | Central velocity dispersions for 4,260 early-type galaxies can be reproduced by emergent gravity, MOND, or dark-halo models once the stellar mass-to-light ratio is allowed to vary; none is selected by these data. | Central dynamics is strongly degenerate with the stellar initial-mass function. The analysis also assumes maximal strain, so the equality provides a lower bound on the required stellar mass-to-light ratio. |
| [[library/verlinde-s-emergent-gravity-versus-mond-and-the-case-of-dwarf-spheroidals/inq|Diez-Tejedor, Gonzalez-Morales, and Niz 2018]] | The line-of-sight dispersions of eight classical dwarf spheroidals can be fitted, but the maximal-strain prescription tends to require stellar mass-to-light ratios marginally above population-synthesis expectations. | The galaxies are Milky-Way satellites rather than isolated systems, and anisotropy, environmental response, and the saturation assumption enter the inference. |
| [[library/testing-emergent-gravity-with-isolated-dwarf-galaxies/inq|Pardo 2018]] | In 452 isolated dwarfs, modeled maximum velocities agree around \(100\,\mathrm{km\,s^{-1}}\), are overpredicted below it, and underpredicted above it. | The axisymmetric extension and baryonic profile normalizations are additional modeling choices; resolved rotation curves were not available. |
| [[library/comparison-of-mond-and-verlinde-s-emergent-gravity-in-dwarf-spheroidals/inq|Yoon, Han, and Hwang 2026]] | Using the later Yoon prescription \(g_{\mathrm{Ver}}=\sqrt{g_{\mathrm{bar}}^2+g_D^2}\) with fixed quasi-de Sitter \(a_0=5.41\times10^{-10}\,\mathrm{m\,s^{-2}}\), the authors report that 21 of 23 within-galaxy trends lie closer to their emergent-gravity line than to the MOND line. Their custom regression-slope-angle statistic combines to \(5.2\sigma\) by Stouffer’s method, \(4.5\sigma\) by Fisher’s method, and \(4.0\sigma\) by a binomial count. | This is not Verlinde’s original linear addition \(g_{\mathrm{tot}}=g_B+g_D\), nor an absolute-fit or likelihood significance. It is a relative comparison of two chosen prescriptions; dwarf mass inference and stellar-dynamical modeling remain inputs. |
| [[library/first-weak-lensing-test-of-emergent-gravity/inq|Brouwer et al. 2017]] | Galaxy–galaxy lensing around 33,613 isolated centrals agreed well with the no-fitted-parameter apparent-mass estimate in four stellar-mass bins. | The analysis supplied a \(\Lambda\)CDM background and the usual relation between effective mass and lensing because the emergent-gravity paper lacked both. |
| [[library/kids-1000-weak-lensing-radial-acceleration-relation/inq|Brouwer et al. 2021]] | KiDS-1000 lensing extended the acceleration relation two decades lower and broadly agreed with the low-acceleration modified-gravity curves. | Early- and late-type galaxies of the same stellar mass differed by at least \(6\sigma\); a universal modification independent of galaxy history cannot explain this without additional baryonic structure. |
| [[library/testing-emergent-gravity-with-mass-densities-of-galaxy-clusters/inq|Halenka and Miller 2020]] | Nominal X-ray and lensing profiles for 23 clusters disagree in cores and outskirts at more than \(5\sigma\), while allowed profile systematics can restore agreement over \(0.3\lesssim r/R_{200}\lesssim1\). | The result is limited by systematic uncertainty in both mass-profile shapes and by flexibility in applying the emergent relation. |
| [[library/testing-emergent-gravity-on-galaxy-cluster-scales/inq|Tamosiunas et al. 2019]] | Joint X-ray and lensing fits to Coma and 58 stacked clusters are significantly worse than GR with cold dark matter; agreement occurs only over limited radial ranges. | The original formula is not a general cluster-dynamics theory, but the scale-dependent failures are requirements any completion must address. |
| [[library/smacs-j0723-test-of-emergent-gravity/inq|Govind and Desai 2024]] | The abstract emphasizes inner-region agreement, while the main analysis and conclusion report agreement between the inferred emergent-gravity and dynamical masses within \(1\sigma\) at all analyzed radii out to \(r_{500}\). | This is one relaxed cluster; central uncertainties are very large, and parameter covariances were omitted, which the authors note may overestimate the errors. It does not resolve the wider cluster-profile tensions. |

## What the lensing tests assume

Weak lensing measures shear and requires a relativistic relation among matter, metric potentials, photon trajectories, distances, and the background expansion. Verlinde’s 2016 paper supplies none of these as a closed system. The early lensing analyses therefore interpret \(M_B+M_D\) as an effective GR lensing mass and use standard cosmological distances.

This is a reasonable phenomenological test of the apparent-mass profile, but not a direct test of a native emergent-gravity lensing equation. [[covariant-completions]] shows that different completions can assign different effective metrics and light couplings.

## Present assessment

The low-acceleration baryon–gravity relation is real and theoretically important. Verlinde’s point-mass scaling captures its asymptotic form with the cosmological acceleration scale \(a_0/6\). The stronger claim that the 2016 microscopic picture supplies a complete alternative to dark matter is not established:

- the main equality is conditional on saturation of a more general inequality;
- finite galaxies expose shape and residual tests not fixed by the point-mass relation;
- the published weak-field formula fails a direct Solar-System exterior test unless new domain restrictions or dynamics are added;
- cluster agreement is radial-range and systematics dependent;
- lensing tests import missing relativistic structure; and
- there is no CMB, structure-formation, or full cosmological likelihood from the original theory.

The favorable 2026 dwarf comparison and the severe Solar-System failure can both be true because they test related but nonidentical phenomenological prescriptions, in very different regimes and against different alternatives. The fair verdict is **interesting restricted phenomenology with an incomplete fundamental theory**, not either empirical confirmation of the microscopic ontology or a universal observational refutation of every entropic-gravity idea.
