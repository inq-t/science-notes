# The Elimination Tests

Two tests separate a wall construction that explains from one that redescribes. The independence test forbids obtaining the horizontal law by solving backward from the history or spectrum it is meant to predict. The restriction test requires that adding the interface leave the local physics it claims to import intact. They are logically independent — a candidate can pass either while failing the other — so they must be checked separately and neither may be cited as evidence for the other.

## Test I — independent construction

**Statement.** The scale-to-state law $\Phi$, its transport, and its response must be obtainable without inferring them from the observable they are meant to explain.

The two outcomes are:

$$
\text{independently constructed state deformation}
\Longrightarrow
\text{new physical structure},
$$

$$
\text{state coordinate reconstructed only from the target observable}
\Longrightarrow
\text{effective description in modular notation}.
$$

The target observable is whichever quantity the calling programme means to derive — an expansion history, a fitted equation of state, a primordial power spectrum. Failing this test does not make a construction *wrong*; it makes it a change of variables. That is a real cost, because a change of variables cannot be confirmed by the agreement it was built to reproduce.

### The region trap

There is a stronger requirement peculiar to cosmological applications: the region family $\{D_N,\Sigma_N\}$ may itself be defined by the solution. An apparent-horizon cut is located by the expansion history, so evaluating modular data only on an already-fitted background silently imports the answer into the domain of integration. Passing the test at the level of the *state* while failing it at the level of the *region* is a real and easy mistake.

A construction escapes this by supplying one of:

- an **off-shell functional** of the wall response for arbitrary admissible backgrounds, followed by a coupled solution of the gravitational and wall equations together; or
- a **state family fixed by independently specified initial and matter data**, from which the background is then predicted rather than assumed.

Using the target background to define both the wall path and its supposed source fails Test I even if every modular calculation along the way is exact.

### What counts as passing

| Passes | Fails |
|---|---|
| the response is a functional of the background, solved simultaneously with it | the response is evaluated only on the fitted background |
| the state family follows from declared initial and matter data | the state family is chosen to reproduce a measured curve |
| the reduced generator and its normalization come from the algebra | the normalization is fixed by matching an amplitude downstream |
| a returned number disagrees with a postulated law, and the law is treated as falsified | a returned number is adjusted until it matches the postulated law |

The last row is the operative discipline. If a construction returns a scale-state rate or a peak ratio different from its postulated value, that is a falsification of the postulate, not a technical discrepancy to be renormalized away.

## Test II — conservative restriction

**Statement.** If local quantum field theory supplies the fibers, the added horizontal structure must not disturb that theory in its tested regime.

An action-level version of the requirement reads

$$
\Gamma_{\rm eff}[g,\Psi;\mu]
=\Gamma_{\rm GR+SM}^{\rm ren}[g,\Psi;\mu]
+\Delta\Gamma_{\rm wall},
\qquad
\Delta\Gamma_{\rm wall}\longrightarrow0
$$

for local laboratory processes, where $\Gamma_{\rm GR+SM}^{\rm ren}$ is the ordinary renormalized low-energy effective action including the cosmological, curvature, and matter counterterms allowed in its regime. An algebraic version — convergence of the relevant local nets, states, and accessible correlators — would discharge the same obligation without writing a single ordinary action, and refusing action-based completions in advance would be an unnecessary restriction.

The checks the statement abbreviates:

- microcausality and local covariance;
- conservation of the renormalized stress tensor;
- gauge and BRST Ward identities;
- Standard Model anomaly cancellation, and curved-spacetime trace terms;
- constancy of physical masses and dimensionless couplings in local units;
- absence or suppression of Lorentz violation, fifth forces, and equivalence-principle violation;
- quantitative bounds, or an explicit decoupling limit, for wall-induced corrections to accessible local correlators.

**This is not a demand that the interface derive the Standard Model.** Importing local physics as a fiber theory is a legitimate scope choice. What the choice owes is a proof that it defines a consistent conservative extension rather than a slogan. A recovery theorem becomes necessary only if the fiber itself is later claimed to *emerge* from wall primitives, which is a different and much larger obligation.

## Why the tests are independent

The failure modes are genuinely orthogonal, which is why a single combined "consistency check" would be a weaker instrument than two:

- **Passes II, fails I.** The added structure decouples cleanly in every laboratory regime and disturbs nothing — but its horizontal law was read off the target curve. Nothing is broken and nothing is explained.
- **Passes I, fails II.** The state family is constructed independently and genuinely predicts the target — but the same structure induces a fifth force, breaks a Ward identity, or drifts a dimensionless coupling. The prediction is real and the theory is excluded.
- **Fails both.** A fitted response that also disturbs local physics: excluded, and uninformative about why.

Only passing both licenses the claim that a construction is a predictive extension of the imported theory.

## Scope note

These tests apply to the *interface*. They do not adjudicate the further obligations a consumer incurs after the interface is granted — a covariantly conserved response tensor, hyperbolicity, regular perturbation crossing, or an end-to-end likelihood. Those are consumer-side gates, and passing both tests here does not anticipate them.
