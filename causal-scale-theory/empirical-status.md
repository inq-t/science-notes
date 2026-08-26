# Empirical Status

The canonical reproduced empirical result is the frozen unit CST-B2 comparison against the fully released 2025 DESI DR2 Gaussian BAO likelihood and Pantheon+. On that homogeneous-background test the unit curve is viable and has a lower maximum-likelihood \(\chi^2\) than flat \(\Lambda\)CDM at equal parameter count; replacing Pantheon+ with the fully released DES-Dovekie reduction gives the same qualitative verdict. A generalized CST-B2 profile is also reproducible and leaves the unit point compatible but unselected, while information criteria favor retaining the frozen unit member. Retaining the Pantheon+ Cepheid calibrators preserves late-time viability but exposes a smaller-sound-horizon requirement and conditional low-age pressure under extrapolation of the late-time ansatz. These are background results only, not evidence for the wall construction, an \(A_2\) cosmology, either unity principle, or a covariant perturbation completion.

## Reproducible local evidence

[[causal-scale-theory/receipts/README|The canonical formula receipt suite]] recomputes the CST-B2 theorem consequences used by the phenomenology notes: exact reduced identities, unit-branch cosmography, matter-plus-radiation folds, strict-dust and historical hybrid folds, representative roots, amplitude-dependent past and future branches, and counterexamples to treating \(\nu=2\) as a universal existence bound. Its machine-readable outputs are [[causal-scale-theory/receipts/algebra.json|the algebra receipt]] and [[causal-scale-theory/receipts/background.json|the background receipt]].

The separate [[causal-scale-theory/receipts/fit-late-time-background|late-time likelihood receipt]] verifies hashes of the archived primary data, applies the declared Pantheon+ selection and full covariance, profiles both calibration nuisances analytically, fits the same \(\Omega_{m0}\) parameter in CST-B2 and flat \(\Lambda\)CDM, and writes [[causal-scale-theory/receipts/late-time-background-fit|a machine-readable result]]. Its fully released 2025 DESI-plus-Pantheon+ row is the canonical reproduced primary comparison.

[[causal-scale-theory/receipts/fit-des-dovekie-background|The DES-Dovekie robustness receipt]] replaces Pantheon+ with the released recalibrated supernova vector and precision matrix. Its 2025 DESI row is likewise assembled entirely from released products and preserves the unit member's relative advantage. This is a **[REPRODUCED BACKGROUND ROBUSTNESS TEST]**, not independent evidence to multiply with the Pantheon+ result: the supernova releases overlap and the DESI likelihood is reused.

[[causal-scale-theory/receipts/fit-calibrated-background|The Cepheid-calibrated receipt]] restores the 77 calibrator rows that the shape-only test intentionally removes. It validates the official flat-\(\Lambda\)CDM Pantheon+SH0ES interface and finds unit CST-B2 competitive after the released 2025 DESI vector is added. The same fit requires \(r_d\simeq136\ \mathrm{Mpc}\) on the local-\(H_0\) branch and gives a conditionally low age when the late-time ansatz is extrapolated to the radiation era. This is a **[REPRODUCED ABSOLUTE-SCALE STRESS TEST]**: it shows that the late response does not by itself solve the Hubble tension, and it identifies the early ruler and extrapolated age as obligations for a completion. It is not an independent likelihood multiplier: it reuses the 1,580 Hubble-flow supernovae and the DESI vector, adding only the 77-row absolute calibration.

The 2026 Ly\(\alpha\) update has a different claim type. It replaces the released 2025 Ly\(\alpha\) block by the bivariate distance mean, uncertainties, and correlation published in DESI Results IV, while taking its cross-covariances with lower-redshift DESI distances to vanish. Until the collaboration releases the full likelihood product, this row is a **[PROVISIONAL PUBLISHED-GAUSSIAN UPDATE]**, not a released or direct 2026 likelihood. Its agreement with the published flat-\(\Lambda\)CDM summary validates the reconstruction without changing that status.

The legacy schema name `crossing_ratio` denotes \(\mathfrak R_c\), the integrated reference matching ratio. The name becomes literal only when the selected member constructs a physical crossing at the reference cut. A passing receipt establishes that quoted values follow from the declared equations and inputs. It does not establish the constitutive source, the weak unit principle \(\mathfrak R_c=1\), the rate principle \(\nu=1\), or their truth in nature.

## Generalized member profile

[[causal-scale-theory/receipts/fit-generalized-background|The generalized CST-B2 receipt]] releases \(\nu\) and \(\mathfrak R_c\), uses the reference location as a branch coordinate, and profiles the admitted positive-reference backgrounds. Its canonical ledger uses the fully released 2025 DESI mean vector and covariance; a separate ledger carries the provisional 2026 Gaussian update. Its result is

$$
\boxed{
\text{unit point compatible with the generalized profile}
\ne
\text{data-derived unity principles}.}
$$

On the released data, \(\nu=1\) sits just outside two one-dimensional \(\Delta\chi^2=1\) profiles but remains inside the wider contours, and the full unit point lies inside the nominal joint two-parameter 68-percent contour. Releasing one or both response parameters improves the maximum likelihood slightly, but not enough to repay their parameter cost: AIC and BIC prefer the frozen unit member. The jointly free \(\mathfrak R_c\) profile is open toward zero, so the data do not identify the fitted maximum as a measured constant. This supports using the unit point as an economical phenomenological member; it does not show that observation selects \(\nu=\mathfrak R_c=1\), still less that the microscopic meanings assigned to those parameters have been measured.

[[causal-scale-theory/data-consistency|The data-consistency audit]] owns the numerical comparisons and their interpretation. The receipt ledgers own the decimals, nuisance conventions, profile intervals, and branch diagnostics, so they are not duplicated here.

## Conditional early-distance stress tests

The fixed-member receipt also derives a last-scattering distance compression from official Planck PR3 base-\(\Lambda\)CDM chains. Appending it to the released 2025 distance vector narrows the CST--\(\Lambda\)CDM likelihood advantage to \(\Delta\chi^2=-1.49\) without exposing a gross distance conflict. That posterior is carrier-conditional rather than model-neutral; the repository's broader historical acoustic anchor has an undocumented uncertainty construction. Both are **[CONDITIONAL EARLY-DISTANCE STRESS TESTS]**, not primary-CMB fits or independent Planck-published one-point likelihoods.

The empirical status is therefore **[REPRODUCED FIT — BACKGROUND ONLY]** for the released 2025 rows, **[REPRODUCED ABSOLUTE-SCALE STRESS TEST]** for the retained Cepheid calibration, **[PROVISIONAL PUBLISHED-GAUSSIAN UPDATE]** for the 2026 Ly\(\alpha\) replacement, and **[CONDITIONAL STRESS TEST]** for the acoustic compressions. None includes primary CMB anisotropies, a derived response-perturbation likelihood, CMB or weak lensing, growth, ISW correlations, BBN, or neutrino-mass inference.

The missing historical `P1/` package still matters for provenance. The new generalized calculation replaces its reported parameter profiles as the canonical current calculation; it does not reproduce the absent historical pipeline or retroactively verify every archived table.

## Withheld claims

The historical shape-exponent and neutrino exercises remain model-class or negative-control comparisons rather than distinctive support for CST. No current background fit measures a BKM metric, horizon capacity, modular flow, wall quotient, or microscopic source map. Nor does the generalized CST-B2 calculation test another member of [[causal-scale-theory/response-family-interface|the wider response-family interface]].

## Promotion path

The next background promotion is to rerun the frozen and generalized profiles against the fully released 2026 DESI likelihood, including collaboration-supplied cross-covariances, and current released supernova reductions. The next physical promotion is a covariant perturbation completion followed by a joint primary-CMB--lensing--growth analysis. A different response member requires its own frozen profile and calculation. The evidence layers must remain separate:

$$
\boxed{
\text{theorem}
\ne
\text{receipt}
\ne
\text{background fit}
\ne
\text{microscopic evidence}.}
$$

[[causal-scale-theory/observables|The observable hierarchy]] specifies the failure conditions and reporting requirements for each promotion step.
