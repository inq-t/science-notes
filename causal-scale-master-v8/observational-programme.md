# Observational Programme and Receipts

The background ansatz is testable now, but the microscopic wall theory and its perturbations are not. Evidence must therefore be divided into algebraic identities, numerical consequences of the assumed closure, phenomenological background fits, and first-principles wall calculations; success in one layer cannot validate the layers beneath it.

## Four evidential layers

1. **Symbolic identity:** verifies algebra after definitions, such as the binary invariant or Witten factorization.
2. **Background receipt:** verifies numerical roots, cosmographic derivatives, and chronology for declared inputs and branch choices.
3. **Phenomenological fit:** evaluates a documented likelihood against released data, with priors, nuisance parameters, covariance, and branch selection.
4. **Microscopic test:** computes $\nu$ and $\mathfrak R_c$ from an independently constructed FLRW wall state.

The first two establish internal consistency. The third establishes empirical viability of an effective background. Only the fourth tests the proposed modular origin directly.

## Structural prediction ledger

| Claim | Required assumptions | Clean failure condition |
|---|---|---|
| $9(1+w_X)^2+6w_X'=4\nu^2$ | binary profile, affine soldering, separate conservation | reconstructed response history cannot satisfy any constant right-hand side |
| $w_a=\frac32(1+w_0)^2-\frac23\nu^2$ | same assumptions plus local CPL tangent convention | measured tangent lies off the width locus |
| one density maximum and one $w=-1$ crossing | balanced binary single channel and monotone affine $\theta(N)$ | multiple genuine maxima or crossings in the response sector |
| self-duality coincides with the maximum | reflection-balanced binary channel | independently constructed wall self-duality occurs elsewhere or is absent |
| $\Omega_{X,c}=1/2$ and dark–ordinary equality | $\mathfrak R_c=1$, flat $3+1$ background, zero residual at crossing | crossing fraction differs from one half after assumptions are controlled |
| $\nu=1$ | width principle in canonical $Q^2=1$ normalization | direct cocycle calculation gives another slope |
| $\mathfrak R_c=1$ | scale–capacity principle | direct wall BKM calculation gives another entropy-normalized peak |
| finite acceleration followed by coasting | unit width, zero residual, declared matter content | a positive residual or another future component dominates; this rejects the sector, not necessarily the pulse |
| unit-branch cosmography | benchmark ordinary abundances and late flatness root | distances or background derivatives exclude the fixed history |

The invariant and CPL locus test the **effective shape**. They do not distinguish a modular derivation from another mechanism engineered to produce the same $w(N)$.

## The phrase “measuring the unit laws” needs care

A background fit in which $\nu$ and $\mathfrak R_c$ are allowed to vary estimates the parameters of the generalized effective profile. It does not directly measure modular capacity or a Connes-cocycle character while the wall map is unconstructed.

The disciplined wording is:

> A phenomenological fit estimates the effective width and crossing amplitude; the modular interpretation predicts that the corresponding microscopic quantities equal one.

Calling such a fit a direct quantum-information measurement would reverse the direction of inference.

## Audit of the supplied receipt

The raw AI revision and its added receipt remain in

`inbox/causal-scale-dynamics-proposed-v8/`.

The file `receipts_revision2.py` checks:

- the unit-branch flatness root and benchmark values;
- two numerical routes to the corrected jerk;
- a local $q$ derivative and an $\Omega_m$ sweep;
- acceleration entry, exit, and selected exit-state quantities;
- a normalized density-history table;
- the unit-width CPL tangent and crossings inferred from three quoted CPL pairs;
- direct substitution into the unit-width differential invariant;
- a hybrid dust-form fold approximation near $\nu=1.8141$, dropping radiation from the evolving density while retaining it in the present closure target.

The unit benchmark, exact matter-plus-radiation folds, representative root atlas, strict-dust fold, and hybrid fold are independently recomputed by [the reviewed background receipt](receipts/background.py). It uses only the Python standard library, can emit JSON, and exits nonzero on failure.

The receipt is helpful but partial:

- it does not test the full matter-plus-radiation root atlas or the radiation-driven branch;
- its “existence ceiling” check uses the hybrid dust-form fold and therefore cannot establish an absolute ceiling;
- the invariant test evaluates an analytic identity using the same formula on both sides, so it is a regression check rather than independent evidence;
- it does not check the generalized $\mathfrak R_c$ closure, the reported effective fit $\nu\approx0.800$, the reported amplitude fit $\mathfrak R_c\approx1.025$, any $\chi^2$/AIC table, neutrino claims, the perturbative profile, or wall-state physics;
- it prints a failure list but does not return a nonzero process exit code when comparisons fail, so automation can mistake a failed run for success.

The proposed-v8 document refers to a larger `receipts_v8.py` and a `P1/` analysis package. Neither is present in the supplied inbox directory. Consequently its quantitative likelihood, posterior, AIC, and perturbation-profile claims are not reproducible from the delivered materials and should remain outside the master synthesis.

## Requirements for authoritative background receipts

An adopted receipt suite should:

- state the exact equation and assumptions checked by each test;
- distinguish symbolic identities from numerical evaluations;
- make the root branch an explicit input and enumerate all roots in diagnostic mode;
- cover the full matter-plus-radiation closure and recompute folds when parameters change;
- test generalized $(\nu,\mathfrak R_c)$ values, not only the unit branch;
- use independent formulations where possible, rather than substituting an identity into itself;
- emit machine-readable results and return nonzero on failure;
- record dependency versions and numerical tolerances;
- avoid language implying that arithmetic validates a physical principle.

The historical receipt should remain attached to the inbox proposal. A future authoritative suite should be written from the reviewed equations rather than silently promoted from the AI draft.

## Requirements for an empirical analysis

Every dated observational analysis should preserve:

- dataset release identifiers, download locations, and hashes;
- sample selections, redshift cuts, covariance treatment, and calibrations;
- the exact likelihood, nuisance model, and any compressed-data assumptions;
- parameter definitions, priors, branch priors, and residual-sector choice;
- treatment of radiation, neutrino masses, curvature, and external anchors;
- code revision, environment, random seeds, and machine-readable outputs;
- explicit inclusions and exclusions, especially primary CMB, lensing, growth, and perturbation observables.

A background-only comparison may establish that the rigid history is not immediately excluded. It cannot establish perturbative consistency or replace a Boltzmann likelihood. AIC statements are meaningful only when the likelihoods, data vectors, nuisance counts, and parameter accounting are genuinely comparable.

## Highest-value tests in order

1. Reconstruct $w(N)$ nonparametrically and test whether the inferred invariant is approximately constant.
2. Fit the generalized background with explicit branch control and publish the full likelihood package.
3. Test the unit point $(\nu,\mathfrak R_c)=(1,1)$ without converting posterior proximity into a derivation.
4. Construct the covariant response and calculate growth, lensing, and CMB signatures.
5. Compute $(\nu,\mathfrak R_c)$ directly from wall modular data.

The fifth test is conceptually strongest even if it is technically hardest: it interrogates the proposed cause rather than only its homogeneous effect.
