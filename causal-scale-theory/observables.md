# Observables and Discriminating Tests

CST should be tested through member-specific signatures and through completion tests that can falsify its microscopic interpretation. The executable background tests below belong to CST-B2, the present rigid balanced-binary member; another member of [[causal-scale-theory/response-family-interface|the response family]] must publish its own profile and failure conditions. Every CST-B2 test must preserve the core types: \(\nu\) is the scale-state rate and inverse profile width, \(\mathfrak R_c\) is an integrated reference ratio, \(m\) is binary polarization, and the signed \(\widehat\zeta_A\) is horizon rapidity rather than another state coordinate.

## Test hierarchy

| Test | Required inputs | Failure condition | Present power |
|---|---|---|---|
| Direct CST-B2 background forward fit | \((\nu,\mathfrak R_c)\), root branch, ordinary abundances, residual sector; SNe, BAO, clocks, and distance data | No allowed branch fits the joint expansion data competitively | Executable now; moderate member discrimination because flexible dark-energy histories can imitate the transition |
| Closure and branch atlas | Present flatness and declared abundances | No root, or only roots incompatible with the declared branch prior | Strong internal admissibility test; not independent evidence because flatness supplies the closure |
| Linked \(w_0\)--\(w_a\) tangent | A separately identified response component and direct forward model | Posterior excludes the theorem relation for all allowed rates | Potentially useful, but a generic CPL posterior need not estimate the local CST tangent |
| CST-B2 rigid shape invariant | Reconstruction of \(w_X\) and \(w_X'\) with covariance | No constant \(\nu\) satisfies the response identity | Exact conditional member signature, but differentiation is noisy and finite redshift coverage gives weak tail leverage |
| Finite acceleration and future class | Amplitude, branch, contents, separate conservation, and residual choice | Reconstructed history has an incompatible sign pattern or asymptotic class | Sharp model statement; current data constrain acceleration entry more directly than the remote future |
| Horizon reconstruction diagnostic | Reconstructed \(H(N)\) and \(q(N)\) | No independent failure condition when every term is reconstructed from the same history; an independent area or rapidity determination would be required | Exact implementation diagnostic with no present independent CST discrimination |
| Growth, lensing, and primary CMB | Covariant \(T^X_{ab}\), characteristic and constraint structure, initial conditions, Boltzmann implementation | Instability or unacceptable joint spectra and growth | Potentially decisive, but not honestly executable until [[causal-scale-theory/conjectures/covariant-response-sector|the response sector]] is constructed |
| Microscopic return values | Independent wall algebra, state family, transport, renormalized BKM measure, and area comparison | The construction fails to yield the binary channel, or calculated \(\nu\) and \(\mathfrak R_c\) disagree with the unit principles | Highest explanatory discrimination; no dynamical FLRW wall construction exists yet |

## Background interface

For a selected CST-B2 root \(x_c\), [[causal-scale-theory/future-asymptotics|the expansion function]] determines

$$
H(z),
\qquad
D_M(z),
\qquad
D_L(z),
\qquad
t(z),
\qquad
q(z),
$$

after the usual nuisance and calibration parameters are supplied. A credible analysis should fit this forward model directly rather than reconstruct a generic \(w(z)\) and then reinterpret that reconstruction as a wall measurement.

In flat FLRW with an area-law apparent horizon, the same history also reconstructs \(R_A=c/H\) and the signed horizon rapidity, up to an additive constant, through

$$
\mathrm d\widehat\zeta_A
=\frac{1-q}{2}\,\mathrm dN.
$$

[[conformal-scale-geometry/horizon-allocation|The conformal-scale theorem]] owns this kinematic identity and its limitations. When \(H\), \(q\), \(S_A\), and \(\widehat\zeta_A\) are all reconstructed from one history, the relation is an internal diagnostic rather than an independent empirical test. Independent discriminating power would require an operational area or rapidity determination not defined through that same reconstruction. The identity does not identify \(\widehat\zeta_A\) with modular time or with the binary polarization \(m\).

## CST-B2 rigid response signatures

[[causal-scale-theory/theorems/rigid-sech-response-identities|The CST-B2 rigid-sech theorem]] proves, under its positive constant-rate pulse and separate conservation,

$$
9(1+w_X)^2+6w_X'=4\nu^2,
$$

and the local CPL tangent relation

$$
w_a
=\frac32(1+w_0)^2
-\frac{2\nu^2}{3}.
$$

Their limitation is inferential rather than algebraic. The \(X\) sector must be separated from matter, radiation, curvature, residual vacuum, and interactions, while derivatives amplify reconstruction error. With data spanning less than a full effective transition width, the crossing placement and amplitude can be constrained while nearby rates remain difficult to distinguish. These relations should therefore be posterior consistency checks after direct fitting, not the first advertised observables.

The inherited analysis also compared favorable-looking statistics with a matched ensemble of smooth positive transients. Many null histories reproduced the same broad CMB-lensing response direction, so the apparent agreement was correctly treated as model-class membership rather than distinctive confirmation. The pipeline is not preserved in the canonical evidence, but the methodological rule remains: every attractive statistic needs a comparator ensemble capable of showing whether it is generic to the wider class.

## Perturbative boundary

Growth rate \(f\sigma_8\), weak lensing, ISW correlations, and primary CMB spectra are not determined by \(H(z)\). They require pressure perturbations, anisotropic stress, characteristic speeds, constraints, and initial conditions. Borrowing a smooth-fluid prescription would test that borrowed completion, not CST as such.

The programme need not derive the Standard Model or all of QFT to study the global arena of facthood. Under [[program-core/claim-and-failure-contract|the conservative local-interface rule]], however, its added response must preserve the successful local sector and avoid forbidden degrees of freedom or uncontrolled corrections.

## Reporting discipline

Every empirical result should state:

- dataset releases, local source locations, and file hashes;
- selections, redshift cuts, covariance treatment, and calibrations;
- likelihood, nuisance model, and compressed-data assumptions;
- parameter definitions and priors, including branch and residual-sector priors;
- treatment of radiation, neutrino masses, curvature, interactions, and external anchors;
- whether perturbations were derived, imported, or omitted, with explicit observable inclusions and exclusions;
- comparison model, likelihood parity, nuisance accounting, and equalized parameter count; and
- code revision, environment, seeds, tolerances, and machine-readable outputs.

A background-only result must say so in its title or opening claim. Likelihood or information-criterion improvements are interpretable only when data vectors, likelihoods, nuisances, and parameter accounting genuinely match. [[causal-scale-theory/empirical-status|The empirical-status note]] records what the inherited material presently supports.
