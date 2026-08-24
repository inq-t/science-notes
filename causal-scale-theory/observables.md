# Observables and Discriminating Tests

CST should be tested through observables that distinguish its rigid response from flexible background reconstructions and through completion tests that can falsify its microscopic interpretation. Algebraic elegance does not determine test priority: each proposed test must state its assumptions, present executability, and discriminating power.

## Test hierarchy

| Test | Required inputs | Failure condition | Present power |
|---|---|---|---|
| Direct background forward fit | $(\nu,\mathfrak R_c)$, root branch, ordinary abundances, residual sector; SNe, BAO, clock and distance data | No allowed branch fits the joint expansion data competitively | Executable now; moderate theory discrimination because flexible dark-energy histories can imitate the transition |
| Closure and branch atlas | Present flatness and declared abundances | No positive root, or only roots incompatible with the intended late branch | Strong as an internal admissibility test; not independent evidence because flatness is used in the closure |
| Linked $w_0$--$w_a$ tangent | A separately identified response component and direct forward model | Posterior excludes $w_a=\tfrac32(1+w_0)^2-\tfrac{2\nu^2}{3}$ | Potentially useful, but generic CPL posteriors need not equal the local CST tangent |
| Shape invariant | Reconstruction of $w_X$ and $w_X'$ with covariance | $9(1+w_X)^2+6w_X'\ne4\nu^2$ | Structurally weak with present background coverage: differentiation is noisy and the tails carry most width leverage |
| Finite acceleration and future class | Amplitude, branch, contents, separate conservation, residual choice | Reconstructed history has an incompatible sign pattern or asymptotic class | Sharp model statement but the remote future is not directly observable; current acceleration history still constrains entry |
| Growth, lensing, and primary CMB | Covariant $T^X_{ab}$, sound/constraint structure, initial conditions, Boltzmann implementation | Instability or unacceptable joint spectra and growth | Potentially decisive, but not executable honestly until [[conjectures/covariant-response-sector|the response sector]] is constructed |
| Microscopic return values | Independent wall algebra, states, transport, and renormalized BKM form | Calculated $\nu$ or $\mathfrak R_c$ disagrees with the proposed unit laws, or the binary channel fails | Highest explanatory discrimination; no dynamical FLRW construction exists yet |

## Background observables

For a selected closure root $x_c$, [[future-asymptotics|the expansion function]] determines the background observables

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

once the usual nuisance and calibration parameters are supplied. A credible analysis should fit this forward model rather than first reconstructing $w(z)$ and then interpreting the reconstruction as a wall measurement.

## Characteristic background relations

The response-sector relations

$$
9(1+w_X)^2+6w_X'=4\nu^2
$$

and

$$
w_a=\frac32(1+w_0)^2-\frac{2\nu^2}{3}
$$

are exact conditional shape constraints. Their weakness is not algebraic but inferential: $w_X$ must be separated from matter, radiation, curvature, residual vacuum, and any interactions, and $w_X'$ amplifies reconstruction error.

When usable background data cover less than a full effective transition width, they can constrain the crossing combination and amplitude while retaining little leverage on the tails that distinguish nearby $\nu$. The inherited work reports this weak-leverage regime but does not preserve a complete power pipeline. The invariant should therefore be a consistency check after direct fitting, not the first advertised observable.

The inherited analysis also used a matched null ensemble of smooth positive transient histories. Many members reproduced the same broad CMB-lensing response direction, so that apparent agreement was rejected as class membership rather than distinctive confirmation. The numerical pipeline is not part of the canonical evidence, but the methodological lesson is: every favorable-looking statistic needs a comparator ensemble capable of revealing whether it is generic to the model class.

## Perturbative observables

Growth rate $f\sigma_8$, weak lensing, ISW correlations, and primary CMB spectra are not determined by $H(z)$ alone. They require pressure perturbations, anisotropic stress, characteristic speeds, and initial conditions. Borrowing a smooth-fluid prescription would test that borrowed completion, not CST as such.

This is also where compatibility with existing physics becomes more demanding. The model need not derive the Standard Model or all of QFT to count as a cosmology of the arena, but its new response must preserve the empirically successful local sector and must not introduce forbidden degrees of freedom.

## Reporting discipline

Every empirical result should state:

- dataset release identifiers, local source locations, and file hashes;
- sample selections, redshift cuts, covariance treatment, and calibrations;
- the exact likelihood, nuisance model, and compressed-data assumptions;
- parameter definitions and priors, including root-branch priors and the residual-sector choice;
- treatment of radiation, neutrino masses, curvature, and external anchors;
- whether perturbations were derived, imported, or omitted, with explicit observable inclusions and exclusions;
- the comparison model, likelihood parity, nuisance accounting, and equalized parameter count;
- code revision, environment, computational seeds, tolerances, and machine-readable outputs.

A background-only result must say so in its title or opening claim. AIC or likelihood improvements are interpretable only when the compared data vectors, likelihoods, nuisance counts, and parameter accounting genuinely match.

[[causal-scale-theory/empirical-status]] records what the inherited masters actually establish today.
