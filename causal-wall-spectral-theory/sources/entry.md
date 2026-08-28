# CWST Source Index

This index organizes the evidence corpus for the canonical CWST notes: 45 primary papers, official observational products, released likelihood code, and provenance snapshots. Each article and its primary payloads are owned by one module under `library/`; CWST retains the observational products, code, and provenance records that belong specifically to its audit. Inclusion means “relevant to this proof obligation,” not “support for CWST as a completed theory.”

The v3 bibliography contains 18 works but no inline citation commands. This index retains all 18, links every primary citation used in the canonical notes to its library owner, and adds focused sources for the obligations exposed by [[causal-wall-spectral-theory/realization-map|the realization map]] and [[causal-wall-spectral-theory/open-problems|construction programme]]. Observational products and their inference limits are treated separately in [[causal-wall-spectral-theory/sources/data/entry|Observational Data and Likelihoods]]; commit-pinned repositories are in [[causal-wall-spectral-theory/sources/code/entry|Reproduction Code]].

## Relative entropy and information geometry

- [[library/relative-entropy-of-states-of-von-neumann-algebras/inq|Araki, “Relative Entropy of States of von Neumann Algebras”]] and [[library/relative-entropy-for-states-of-von-neumann-algebras-ii/inq|Part II]] give the type-III/general von Neumann algebra definition, monotonicity, support treatment, and lower-semicontinuity needed beyond density matrices.
- [[library/relative-hamiltonian-for-faithful-normal-states/inq|Araki, “Relative Hamiltonian for Faithful Normal States of a von Neumann Algebra”]] is the closest operator-algebraic starting point for lifting the finite exponential-family deformation in [[causal-wall-spectral-theory/conjectures/bkm-to-spatial-precision|the state-to-spatial-precision conjecture]].
- [[library/monotone-riemannian-metrics-and-relative-entropy/inq|Lesniewski and Ruskai, “Monotone Riemannian Metrics and Relative Entropy on Noncommutative Probability Spaces”]] relates relative-entropy Hessians to monotone quantum metrics in the regular setting.
- [[library/geometries-of-quantum-states/inq|Petz and Sudár, “Geometries of Quantum States”]] proves the operator-monotone characterization of monotone metrics. This is a primary preprint substitute for the closed Petz 1996 article, DOI `10.1016/0024-3795(94)00211-8`, not a copy of that article.

## Local covariance, renormalized response, and state selection

- [[library/the-generally-covariant-locality-principle-a-new-paradigm-for-local-quantum-physics/inq|Brunetti, Fredenhagen, and Verch, “The Generally Covariant Locality Principle”]] supplies the functorial locally covariant framework used in [[wall-construction-interface/inq|the wall-construction interface]].
- [[library/microlocal-analysis-and-interacting-qft/inq|Brunetti and Fredenhagen, “Microlocal Analysis and Interacting Quantum Field Theories”]] constructs perturbative renormalization on curved backgrounds.
- [[library/local-wick-polynomials-and-time-ordered-products/inq|Hollands and Wald, “Local Wick Polynomials and Time Ordered Products”]] classifies locality, covariance, scaling, and metric-dependent renormalization ambiguities; [[library/existence-of-local-covariant-time-ordered-products/inq|their existence paper]] completes the construction.
- [[library/dynamical-locality-and-covariance/inq|Fewster and Verch, “Dynamical Locality and Covariance”]] makes the state-selection burden sharp: under broad locally covariant hypotheses there is no universal preferred-state prescription of the kind CWST would otherwise be tempted to assume.

## Observer, horizon, and gravitational algebras

- [[library/cosmological-horizons-and-reconstruction-of-quantum-field-theories/inq|Dappiaggi, Moretti, and Pinamonti, “Cosmological Horizons and Reconstruction of Quantum Field Theories”]] embeds a bulk Klein–Gordon algebra into a cosmological-horizon algebra for a restricted expanding class.
- [[library/modular-hamiltonians-on-the-null-plane-and-the-markov-property-of-the-vacuum-state/inq|Casini, Teste, and Torroba, “Modular Hamiltonians on the Null Plane and the Markov Property of the Vacuum State”]] gives a controlled null-surface example with local stress-tensor modular Hamiltonians.
- [[library/generalized-entropy-for-general-subregions-in-quantum-gravity/inq|Jensen, Sorce, and Speranza, “Generalized Entropy for General Subregions in Quantum Gravity”]] constructs observer-dependent type-II subregion algebras in a semiclassical limit.
- [[library/algebraic-observational-cosmology/inq|Kudler-Flam, Leutheusser, and Satishchandran, “Algebraic Observational Cosmology”]] constructs gravitationally dressed observables accessible to a comoving observer in a class of FLRW cosmologies.
- [[library/subregion-algebras-in-classical-and-quantum-gravity/inq|Chandrasekaran and Flanagan, “Subregion Algebras in Classical and Quantum Gravity”]] develops horizon-cut algebras, edge modes, crossed products, and half-sided modular structure in perturbative gravity.

These are constructibility precedents. None derives CWST’s scale-indexed state family, binary quotient, or spectral weld.

## Critical conformal operators

- [[library/scattering-matrix-in-conformal-geometry/inq|Graham and Zworski, “Scattering Matrix in Conformal Geometry”]] constructs conformally covariant fractional operators from Poincaré–Einstein scattering data.
- [[library/fractional-laplacian-in-conformal-geometry/inq|Chang and González, “Fractional Laplacian in Conformal Geometry”]] supplies the extension formulation behind fractional conformal Laplacians.
- [[library/fractional-conformal-laplacians-and-fractional-yamabe-problems/inq|González and Qing, “Fractional Conformal Laplacians and Fractional Yamabe Problems”]] records filling, maximum-principle, and positivity hypotheses that cannot be omitted from a curved $P_3$ claim.
- [[library/on-fractional-gjms-operators/inq|Case and Chang, “On Fractional GJMS Operators”]] includes extension and energy identities relevant to the three-dimensional critical endpoint.
- [[library/conformally-invariant-powers-of-the-laplacian-q-curvature-and-tractor-calculus/inq|Gover and Peterson, “Conformally Invariant Powers of the Laplacian, Q-Curvature, and Tractor Calculus”]] is a primary substitute for the closed 1992 Graham–Jenne–Mason–Sparling article, DOI `10.1112/jlms/s2-46.3.557`. It is not the original paper.

## Holographic response and analytic continuation

- [[library/holographic-renormalization/inq|de Haro, Solodukhin, and Skenderis, “Holographic Reconstruction of Spacetime and Renormalization in the AdS/CFT Correspondence”]] supplies the counterterm and renormalized source/response machinery.
- [[library/correlation-functions-in-holographic-rg-flows/inq|Papadimitriou and Skenderis, “Correlation Functions in Holographic RG Flows”]] treats response functions, scheme terms, and contact contributions along flows.
- [[library/pseudo-supersymmetry-and-the-domain-wall-cosmology-correspondence/inq|Skenderis and Townsend, “Pseudo-Supersymmetry and the Domain-Wall/Cosmology Correspondence”]] states the restricted domain-wall/cosmology relation that precedes the spectral continuation.
- [[library/holography-for-cosmology/inq|McFadden and Skenderis, “Holography for Cosmology”]] gives the scalar and tensor two-point dictionary presented in [[vendor/holographic-cosmology/scalar-and-tensor-spectra|the vendored spectrum note]].
- [[library/operator-dictionaries-and-wave-functions-in-ads-cft-and-ds-cft/inq|Harlow and Stanford, “Operator Dictionaries and Wave Functions in AdS/CFT and dS/CFT”]] distinguishes a continued wavefunction dictionary from an expectation-value/operator dictionary. That distinction bears directly on the unproved Euclidean-response $\to\Psi\to|\Psi|^2$ step.
- [[library/on-the-power-spectrum-of-inflationary-cosmologies-dual-to-a-deformed-cft/inq|McFadden, “On the Power Spectrum of Inflationary Cosmologies Dual to a Deformed CFT”]] is the closest direct source for the inverse stress-trace spectral-density formula used by v3.
- [[library/holography-for-inflation-using-conformal-perturbation-theory/inq|Bzowski, McFadden, and Skenderis, “Holography for Inflation Using Conformal Perturbation Theory”]] develops a controlled near-CFT scalar spectrum and bispectrum.
- [[library/cosmological-3-point-correlators-from-holography/inq|McFadden and Skenderis, “Cosmological 3-Point Correlators from Holography”]] makes semilocal terms and the higher-point continuation explicit.

## Cosmological perturbations and descent

- [[library/quantum-theory-of-gauge-invariant-cosmological-perturbations/inq|Mukhanov, “Quantum Theory of Gauge-Invariant Cosmological Perturbations”]] derives the reduced quadratic action after the gravitational constraints; it is the benchmark for CWST’s missing wall-mode descent.
- [[library/a-new-approach-to-the-evolution-of-cosmological-perturbations-on-large-scales/inq|Wands, Malik, Lyth, and Liddle, “A New Approach to the Evolution of Cosmological Perturbations on Large Scales”]] states the conservation theorem and its nonadiabatic-pressure hypothesis.
- [[library/adiabatic-modes-in-cosmology/inq|Weinberg, “Adiabatic Modes in Cosmology”]] isolates the assumptions behind physical adiabatic modes at long wavelength.
- [[library/an-infinite-set-of-ward-identities-for-adiabatic-modes-in-cosmology/inq|Hinterbichler, Hui, and Khoury, “An Infinite Set of Ward Identities for Adiabatic Modes in Cosmology”]] supplies the symmetry and soft-limit conditions needed before higher-point consistency relations may be imported.
- [[library/non-gaussian-features-of-primordial-fluctuations-in-single-field-inflationary-models/inq|Maldacena, “Non-Gaussian Features of Primordial Fluctuations in Single Field Inflationary Models”]] is the source for the conditional single-clock squeezed relation.
- [[library/quantum-contributions-to-cosmological-correlations/inq|Weinberg, “Quantum Contributions to Cosmological Correlations”]] gives the Lorentzian in-in framework and is a direct check against treating a Euclidean Hessian as a cosmological probability kernel without further work.

## Observational papers and worked holographic models

- [[library/constraining-holographic-inflation-with-wmap/inq|Easther, Flauger, McFadden, and Skenderis, “Constraining Holographic Inflation with WMAP”]] fits a particular perturbative holographic model to WMAP7.
- [[library/constraining-holographic-cosmology-using-planck-data/inq|Afshordi, Gould, and Skenderis, “Constraining Holographic Cosmology Using Planck Data”]] fits a particular model to Planck 2015; its competitive result is conditional on removing $\ell<30$.
- [[library/planck-2018-results-x-constraints-on-inflation/inq|Planck 2018 results X: Constraints on Inflation]] supplies the scalar amplitude and tilt calibration used by v3.
- [[library/planck-2018-results-ix-constraints-on-primordial-non-gaussianity/inq|Planck 2018 results IX: Constraints on Primordial Non-Gaussianity]] supplies shape-dependent bounds, not a universal CWST non-Gaussianity threshold.
- [[library/act-dr6-power-spectra-likelihoods-lambda-cdm/inq|ACT DR6 Power Spectra, Likelihoods and $\Lambda$CDM Parameters]] gives the baseline DR6 likelihood and parameter analysis.
- [[library/the-atacama-cosmology-telescope-dr6-constraints-on-extended-cosmological-models/inq|ACT DR6 Constraints on Extended Cosmological Models]] gives the joint running result discussed in [[causal-wall-spectral-theory/empirical-targets|the empirical-target ledger]].
- [[library/bicep-keck-2018-primordial-gravitational-waves/inq|BICEP/Keck 2018-Season Primordial-Gravitational-Wave Analysis]] supplies the tensor bound used as a calibration target.

The matching observational products are owned by [[data/wmap-seven-year-power-spectra/inq|WMAP7]], [[data/planck-2015-release-2-cosmology-products/inq|Planck Release-2]], [[data/bicep2-keck-planck-2015-joint-likelihood/inq|the 2015 BKP likelihood]], [[data/planck-2018-release-3-cosmology-products/inq|Planck Release-3]], [[data/bicep-keck-2018-data-products/inq|BK18]], and [[data/act-dr6-cosmology-products/inq|ACT DR6]] dataset modules.

## Adjacent vacuum and gravitational-information sources

These four papers are cited only in the historical vacuum/gravity conversation. They are mirrored for completeness but are not premises of the canonical CWST spectral construction.

- [[library/relative-entropy-and-the-bekenstein-bound/inq|Casini, “Relative Entropy and the Bekenstein Bound”]] gives the QFT-relative-entropy form of the bound.
- [[library/entanglement-equilibrium-and-the-einstein-equation/inq|Jacobson, “Entanglement Equilibrium and the Einstein Equation”]] derives an Einstein-equation relation under a finite universal entropy-density hypothesis.
- [[library/canonical-energy-is-quantum-fisher-information/inq|Lashkari and Van Raamsdonk, “Canonical Energy Is Quantum Fisher Information”]] identifies a holographic relative-entropy quadratic form with bulk canonical energy in its stated regime.
- [[library/a-manifestly-local-theory-of-vacuum-energy-sequestering/inq|Kaloper and Padilla, “A Manifestly Local Theory of Vacuum Energy Sequestering”]] demonstrates a separate constructible global/top-form mechanism; it is not already contained in CWST.

## Integrity and provenance

All 46 non-legacy reference PDFs—the 45 library-owned papers above plus the CWST-owned Planck parameter table—open without encryption and were rendered for visual identity checks. The two historical CWST monographs are tracked separately by [[causal-wall-spectral-theory/sources/legacy/README|the legacy ledger]]. All downloaded archives pass a full member-list read, and each extracted FITS file begins with a valid `SIMPLE` card. [[causal-wall-spectral-theory/sources/checksums|The checksum ledger]] covers the immutable downloaded artifacts at their present canonical paths; extracted trees are derivative copies of those checked archives. [[causal-wall-spectral-theory/sources/origins|The origin ledger]] records the exact upstream locations and the two access-limited substitutions.
