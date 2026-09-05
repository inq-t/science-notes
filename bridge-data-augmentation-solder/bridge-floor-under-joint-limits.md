# A Bridge Floor Survives Joint Limits

A uniform conditional-variance floor passes to a limiting joint law without convergence of conditional expectations, conditional densities, Fisher tensors, or auxiliary generators. The useful formulation bounds the error of every boundary predictor before taking the limit. This preserves an already proved global--local response estimate; it neither constructs the limiting law nor establishes its nontriviality or physical reconstruction.

**Status: [EXACT CONDITIONAL LIMIT THEOREM].** The core and boundary observables, their limiting joint law, and a uniform positive constant are hypotheses. Centering is by constants; changing physical-sector projections requires additional comparison data.

## Keep both the observable and its possible predictors

Let \(\mu_n\) be joint laws of a core \(C\) and retained boundary \(D\), with a limiting law \(\mu\). The regulators may have different raw carriers, but require specified identifications of their bounded continuous cylinder observables with those of the limit, preserving constants, products and complex conjugation. Assume joint cylinder convergence and that the core and boundary test algebras are dense in their respective limiting marginal \(L^2\) spaces.

Suppose a constant \(0<\kappa\le1\), independent of \(n\), satisfies
\[
\mathbb E_{\mu_n}\operatorname{Var}_{\mu_n}(f(C)\mid D)
\ge\kappa\operatorname{Var}_{\mu_n}(f(C))
\tag{JL1}
\]
for the identified core tests. Consequently, for every core test \(f\) and every bounded continuous boundary cylinder predictor \(g\),
\[
\boxed{
\mathbb E_{\mu_n}|f(C)-g(D)|^2
\ge\kappa\operatorname{Var}_{\mu_n}(f(C)).}
\tag{JL2}
\]
The implication from (JL1) is immediate from the least-squares property of conditional expectation. Conversely, equivalence at a given regulator uses density of its boundary predictor class.

For fixed \(f,g\), joint cylinder convergence passes each bounded continuous integral in (JL2), including the mean used in the variance. Thus
\[
\mathbb E_\mu|f(C)-g(D)|^2
\ge\kappa\operatorname{Var}_\mu(f(C)).
\tag{JL3}
\]
Marginal \(L^2\) density and continuity of both sides extend this inequality to all square-integrable \(f\) and \(g\). Only now minimize over \(g\). Orthogonal projection onto the boundary subspace gives
\[
\boxed{
\mathbb E_\mu\operatorname{Var}_\mu(f(C)\mid D)
\ge\kappa\operatorname{Var}_\mu(f(C)).}
\tag{JL4}
\]
In the notation of [[inq|the data-augmentation construction]], the limiting operator therefore satisfies \(I-K^*K\ge\kappa Q_C\).

The order of quantifiers matters: preserve the inequality for every predictor and then optimize in the limiting law. Interchanging an infimum with a limit, or assuming that the finite conditional expectations converge, is unnecessary.

## What this permits and what it does not

[[conditional-fisher-coercivity/inq|Conditional Fisher coercivity]] can prove the finite-regulator constant. Once the response floor is established, its certificate may be discarded for this limiting step: even a singular limiting Fisher geometry is harmless if (JL2) survives on the complete identified test classes.

For unbounded cylinder fields, weak convergence alone does not pass the quadratic terms. One must either start with bounded tests and extend in the limiting \(L^2\) spaces as above, or establish the required uniform integrability. Separate convergence of the core and boundary marginals is also insufficient; their joint coupling determines recovery.

Fixed physical slab widths, vacuum preparation, and outer boundary conditions must be included in the family for which \(\kappa\) is uniform. A positive constant that closes with the cutoff does not meet (JL1). Nor does the theorem prevent all nonconstant observables from disappearing in a trivial limit: then the inequality holds vacuously.

Nontriviality, gauge identities, reflection positivity, the limiting transfer, locality and Poincare covariance remain independent obligations of the physical reconstruction. The theorem preserves the bridge estimate once those carriers and joint limits exist; it does not provide a Yang--Mills continuum construction.
