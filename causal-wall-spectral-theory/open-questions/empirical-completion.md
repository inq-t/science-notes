# Perform an Independent Empirical Test

CWST needs a reproducible likelihood for a response calculated independently of the data used to select it. Arithmetic identities and backward calibration are receipts; empirical completion begins only when a restricted member returns amplitude, shape, tensors, or higher correlations before comparison with released observations.

## Minimum reproducibility package

A test should record:

- the member's independently derived parameter set and priors;
- the map from its wall quantities to gauge-invariant primordial variables;
- the Boltzmann or alternative observable implementation;
- released data, likelihood versions, nuisance treatment, and covariance;
- baseline model and model-comparison statistic;
- posterior chains or sufficient reproducible outputs; and
- tests on data not used to design the member.

The local source archive already contains Planck, BICEP/Keck, and ACT papers, likelihood material, chains, and run definitions. [[causal-wall-spectral-theory/receipts/README|The normalization receipt]] checks only algebra and explicitly does not satisfy this empirical package.

## Order of operations

The clean order is

$$
\text{construct member}
\longrightarrow
\text{calculate response}
\longrightarrow
\text{derive observable map}
\longrightarrow
\text{freeze prediction}
\longrightarrow
\text{evaluate likelihood}.
$$

Choosing a discrete exponent because it lies close to a published central value and then calling the proximity a prediction reverses that order. [[no-gos/singularity-invariants-do-not-select-a-wall-member|The rejected \(A_2\) attempt]] is retained as a concrete warning.

## Completion and failure

Empirical completion requires at least one nontrivial calculated quantity not used as input and an end-to-end likelihood. A member fails when that frozen return is excluded or when its observable implementation cannot be made consistent. The broad interface remains unfalsifiably flexible until microscopic structure restricts its response functions; that flexibility is a programme gap, not empirical success.

