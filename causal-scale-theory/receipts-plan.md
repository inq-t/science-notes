# Receipts and Data Plan

The archive contains five receipt scripts of widely differing quality, one of which verifies its headline result with a hard-coded literal. The plan is one suite under a written contract, every check labelled by what it actually establishes, and a standing ledger of the quantitative claims that cannot presently be reproduced at all.

The contract already exists in prose: the requirements listed in [[causal-scale-master-v8/observational-programme|the observational programme]] are the right nine, and [[causal-scale-master-v8/receipts/README|the v8 receipt README]] is the right shape for a per-suite statement of scope. Both should be lifted rather than rewritten.

## The contract

A receipt in this module must:

- state the exact equation and the assumptions each test checks;
- declare each check **independent** or **regression** — see below;
- take the root branch as an explicit input, and enumerate all roots in diagnostic mode;
- cover the full matter-plus-radiation closure, and recompute folds when parameters change;
- exercise generalized $(\nu,\mathfrak R_c)$ values, not only the unit branch;
- use the standard library only;
- emit machine-readable output and **return nonzero on failure**;
- record dependency versions and numerical tolerances;
- avoid any wording implying that arithmetic validates a physical principle.

The independent-versus-regression distinction is the one I would enforce hardest, because it is where the existing scripts fail. A check that substitutes an analytic identity into itself confirms that the algebra was transcribed correctly and nothing else. That is worth having — it catches typos and drift — but labelling it as verification of a result is how a suite comes to look like evidence. Every check gets one of two words in its header, and the JSON carries the same field.

## Existing scripts, by what they establish

| Script | Establishes | Defects |
|---|---|---|
| [[causal-scale-master-v8/receipts/background.py]] | the exact matter-plus-radiation folds, the strict-dust and hybrid distinction, the root atlas, generalized-amplitude cases, the unit benchmark | none material — this is the model to build on. Stdlib, JSON, nonzero exit. |
| [[causal-scale-master/latest/receipts_v7.py]] | selected symbolic residuals of the v7 unit branch | its aggregate flag checks residual *strings*; validates no physical principle; writes output beside itself |
| `inbox/causal-scale-dynamics-proposed-v8/receipts_revision2.py` | unit-branch benchmark, two routes to the jerk, chronology, CPL tangent | ceiling check uses the hybrid dust form; the invariant check substitutes one formula into both sides; prints failures but **exits zero** |
| [[scale-as-modular-observable/chats/02/outputs/receipts_closure.py]] | a classical exponential-family cumulant identity, to ~$10^{-6}$ | the capacity check prints $C/S$ as the literal `1.0` and never computes $C=T\,\mathrm dS/\mathrm dT$; one check evaluates no numbers at all; three benchmark "exact" values are tautologies that return identically for arbitrary fake roots; requires numpy and scipy; exits zero always |
| [[scale-as-modular-observable/chats/03/outputs/receipts_transparency_fold.py]] | twenty-one identities including the tractor identity, the Levinson phase density, and the two live no-gos | ceiling computed in the hybrid dust form; single root bracket, so it cannot see three roots where three exist; requires numpy and scipy; exits zero always |

The last row is the awkward one: the weakest-engineered script carries the most unique physics, including [[salvage-ledger|two salvageable no-gos and the tractor-parallel split]]. Port the content, discard the harness.

## What the suite should check

**Port from v8's background.py unchanged in substance.** The fold values, the root atlas, the strict-dust versus hybrid distinction, past- and future-crossing generalized-amplitude cases, and the unit benchmark. Mark the benchmark cosmography independent (it solves the closure) and the invariant check regression (it substitutes the analytic $w_X$ into the analytic invariant).

**Add the asymptotic existence bound.** Newly established and currently receipted nowhere. With $F_\nu(x)=M(x)\operatorname{sech}^2(\nu x)$ and $M=\Omega_{m0}e^{3x}+\Omega_{r0}e^{4x}$,

$$
F_\nu\sim4\Omega_{r0}e^{(4-2\nu)x},
$$

so a positive root exists for every $\nu<2$ and none at $\nu\ge2$, and that bound requires only $\Omega_{r0}>0$ — it is independent of $\Omega_{m0}$. Dropping radiation from $M$ moves the threshold to $\nu<3/2$ and manufactures the artifact ceiling near $1.814$. The check should assert root existence across a $\nu$ grid straddling $2$, assert non-existence above it, and assert that the dust-form variant reproduces the historical $\simeq1.8141$ — pinning the artifact as a *known wrong answer* so it cannot quietly return. Recorded in [[scale-as-modular-observable/claim-audit|the claim audit]].

**Add root-count assertions, not just root values.** The failure that produced the artifact was a single bracket returning one root where three exist. Asserting the count at chosen widths — one below $\simeq1.5584$, three between there and $\simeq1.8147$, one above — is the regression test for that class of bug.

**Port the independent identities worth keeping.** The tractor norm identity $I^2=-\widehat\mu_AH^2$; the e-fold allocation $\mathrm dN=\mathrm d\widehat\eta_A+\tfrac14\mathrm d\ln\mathcal S_A$; the binary moment identity and Fisher length; the Witten factorization and its zero mode; the Gudermannian relations in both position and momentum. All independent, all cheap, all currently spread across three scripts.

**Do not port the capacity check.** It cannot be repaired, because there is no computation there to fix — the quantity was never computed. If a capacity check is wanted it has to be written from scratch against an actual regulated model, and that is a research task, not a receipt.

## The withheld-claims ledger

These quantitative claims appear in the master documents and cannot be reproduced from anything in the vault. [[causal-scale-master-v8/revision-audit|The revision audit]] already withholds the v8 set correctly; this consolidates them and says what would be needed.

| Claim | Source | What is missing |
|---|---|---|
| fitted width $\nu\approx0.800$ with interval | proposed v8 | the `P1/` package and `receipts_v8.py`, both absent from the inbox snapshot |
| fitted amplitude $\mathfrak R_c\approx1.025$ with interval | proposed v8 | same |
| $\Delta\chi^2$ and AIC model rankings | proposed v8, Revision 2 | likelihood code, data manifest, covariance treatment, priors, nuisance parameters, branch handling |
| v7's background comparison, $\chi^2\approx1398$ versus $1402$ | v7 master | reproduction paths in the README describe the archive layout, not the flattened snapshot |
| the shape-exponent profile likelihood | the P1 result | its code and data package |
| neutrino-mass release discussion | Revision 2 | a Boltzmann posterior; the perturbation sector is open, so this cannot exist yet |
| CMB-lensing response direction | Revision 2 | superseded by its own negative control, which disqualified it |

The discipline that keeps this honest: a claim leaves the ledger only when code and data that regenerate it are in the vault, not when it is restated in a newer document. Two of the rows above moved between generations without ever acquiring support.

## Data provenance

Do not copy data into this module. [[causal-wall-spectral-theory/sources/entry|The spectral programme's source library]] already mirrors the primary literature, official likelihoods, released chains, and reproducibility code, with a checksum ledger. The background tests this module needs are arithmetic on declared abundances and require no dataset at all; anything that needs real data needs that library.

There is an unresolved architectural question here, already flagged in [[wall-construction-interface/duplication-audit|the duplication audit]]: a vault-wide source library living inside one consumer module is backwards. Two modules now reach into it from outside. My recommendation is to promote it to a top-level `sources` module when convenient, and until then to reference it by path and accept the oddity — moving several hundred megabytes is a decision on its own, and it should not be made as a side effect of either refactor.

For anything this module does eventually fit against, the empirical-hygiene requirements in [[causal-scale-master-v8/observational-programme|the observational programme]] — release identifiers, hashes, cuts, covariance treatment, priors, branch priors, residual sector, seeds, machine-readable outputs, explicit inclusions and exclusions — should be adopted verbatim rather than paraphrased. They are already correct, and [[cosmodynamics/empirical-boundaries|the empirical boundaries note]] states the surrounding scope discipline.
