---
inq.module: physical-response-coercivity
inq.include:
  - './'
inq.ambient:
  - 'receipts/*.py'
  - 'receipts/*.txt'
keywords:
  - physical response
  - coercivity
  - causal frames
  - relative entropy
  - BKM metric
  - energy comparison
  - form cores
  - vacuum complement
---
# Physical Response Coercivity

A response can detect a physical distinction without measuring its energy. A gap argument therefore needs two independent estimates on the same complete physical carrier: a lower frame that detects every nonvacuum direction, and a calibrated comparison that bounds the response by physical energy. This module develops causal, regional and entropy-based realizations of those estimates, including their blind directions and domain obstructions. The comparison implications are exact under their stated hypotheses; no complete, regulator-uniform Yang–Mills realization is supplied.

## Detect every physical direction

[[physical-response-coercivity/physical-distinction-coercivity|Physical distinction coercivity]] identifies the centered GNS carrier with the vacuum complement. An event projection, a gauge quotient, a state tangent and an obtained outcome have different roles. A projection's two values do not determine an energy threshold, and a bound for one observable channel need not cover the full physical carrier.

[[physical-response-coercivity/causal-frame-coercivity|Causal frames]] assemble distinction maps into a closed analysis form. On a common complex physical energy-form core in \(\Omega^\perp\), the required estimates have the shape

\[
\mathfrak d[\psi]\geq\kappa_{\mathrm{fr}}\|\psi\|^2,
\qquad
\mathfrak h_{\mathrm{phys}}[\psi]
\geq\eta_{\mathrm{sol}}E_*\mathfrak d[\psi].
\]

The first is quantitative coverage, not merely a trivial common kernel. The second compares with the physical Hamiltonian form, not an auxiliary relaxation operator. [[measured-response-carriers/response-to-energy-comparison|The generic response-to-energy theorem]] owns the implication
\(\Delta_E\geq\eta_{\mathrm{sol}}E_*\kappa_{\mathrm{fr}}\), including analysis-map coverage, response kernels and closure on a complex form core. The frame, its normalization and the energy yardstick must be fixed independently of the target spectrum.

## Complete source susceptibility is a direct spectral test

[[physical-response-coercivity/conditional-vacuum-rigidity-and-the-physical-gap|Conditional vacuum rigidity]] uses the actual interacting vacuum and its centered generator \(L\). For centered bounded physical sources \(f_i\), the covariance and reduced-resolvent response are
\[
\mathsf C_{ij}=\langle f_i,f_j\rangle,\qquad
\mathsf X_{ij}=\langle f_i,L^{-1}f_j\rangle.
\]
On its fixed compact gauge carrier, the inequality \(\mathsf X\leq\Delta^{-1}\mathsf C\) for every finite family from a dense physical source algebra is equivalent to \(L\geq\Delta\) on the vacuum complement. The same response is the negative half-Hessian of the ground energy for linear source perturbations. Sewn finite-duration curvature approaches it with a triangular time weight.

This criterion already uses the physical generator. Its source norm-density condition differs from the complex energy-form core needed by an independently defined response-to-energy comparison above. [[general-causal-action/prepared-readout-algebra-and-physical-source-completeness|Prepared readout completeness]] constructs that source algebra for the finite preparation models. Conditional innovations split the susceptibility into blocks, but their mixed response still requires control; bounds on a few chosen statistics or diagonal blocks do not establish the complete inequality. [[two-slice-innovation-geometry/chronological-cyclic-sources-and-the-innovation-floor|The cyclic-source analysis]] supplies the corresponding distinction for the actual chronology.

## Regional access repairs one problem, not all of them

The global pure vacuum has no finite relative-entropy Hessian in transverse pure-state directions. [[physical-response-coercivity/regional-relative-entropy-frames|Regional relative-entropy frames]] instead pull faithful output-state metrics back through declared access channels. Their two-qubit witness shows that faithful local marginals can detect amplitude while missing relative phase; an additional joint readout repairs that finite example. In infinite dimension, separation still does not give a uniform lower frame.

A preserving expectation is not automatically such a repair. [[channel-loss-and-recovery/preserving-expectation-loss|The preserving-expectation theorem]] distinguishes incoming information loss from a form on retained directions: the minimum loss over lifts of any retained tangent is zero for one adapted preserving expectation. Likewise, the [[physical-response-coercivity/causal-frame-coercivity#Conditional-expectation shells|local-expectation obstruction]] rules out proper vacuum-preserving expectations between ordinary nested local algebras under the stated cyclicity and separatingness hypotheses. A regulator or comparison filtration needs its own construction; orthogonal shells do not automatically diagonalize the energy form.

## A localized energy comparison has precise hypotheses

[[physical-response-coercivity/localized-relative-entropy-and-the-energy-solder|Localized relative entropy]] specializes Longo's finite-width bound to differentiable local-unitary paths. With the half-Hessian convention, the real path forms satisfy

\[
0\leq q^{\mathrm{loss}}\leq q_B
\leq\frac{2\pi R}{\hbar c}\mathfrak h_{\mathrm{phys}}.
\]

This is an established energy comparison for that localized setting, not for arbitrary information channels. A spectral conclusion still requires a positive Hermitian extension with the same upper bound on a complex energy-form core, together with an independently proved lower frame. The local-unitary state map can have centralizer blind directions; Reeh–Schlieder norm density supplies neither their removal nor the form-core condition. The finite real-core counterexample in that note makes the complexification requirement explicit.

## Retained responses and paired walls have different inputs

[[physical-response-coercivity/retained-output-casimir-bound|A retained-output response]] first minimizes over hidden lifts, then needs a complex physical carrier map and a lower frame on the full reconstructed vacuum complement. A general channel can genuinely contract its declared BKM metrics and leave a positive output form; the zero-output-loss obstruction concerns one adapted preserving expectation. Comparing the resulting response with the full energy-squared Casimir gives \(\Delta_E\geq E_*\sqrt{\eta\kappa}\). At a finite lattice regulator, the available Hamiltonian comparison instead gives the linear bound \(\Delta_H\geq\eta E_*\kappa\).

[[physical-response-coercivity/paired-wall-casimir-comparison|The paired-wall construction]] supplies a more specific possible response: the joint spectral product of two strongly commuting dimensionless operators on one complete carrier. Reciprocal scaling can make that product invariant while its marginals remain gapless. Its paired completeness estimate and calibrated Casimir comparison are independent hypotheses; neither follows from two wall labels or one-parameter invariance. This product is also distinct from adding two losses before minimizing over hidden lifts.

## Stability and scale remain separate

[[physical-response-coercivity/entropic-stiffness-not-entropic-force|Entropic stiffness]] distinguishes first-order equilibrium from the uniform second-order modulus needed for a gap. Its holographic information–energy correspondence is a controlled precedent with its own carrier and normalization, not a Yang–Mills construction. Causal-cut completeness may organize the response family; entropy positivity alone supplies neither its lower bound nor its clock rate.

[[physical-response-coercivity/quotient-to-qft-realization|Quotient-to-QFT realization]] separates the pre-observable quotient from its accessible state channel and the effective theory reconstructed from it. Exact QFT recovery may hold for that effective image even when the full source is not recoverable. To pass a proved regulator estimate to a continuum theory, the constants must survive along declared carrier comparisons, the energy forms and vacuum projections must converge with sufficient recovery control, and the Euclidean states or correlations must separately converge to data satisfying the reconstruction conditions. [[mass-scale-calibration/inq|Mass and scale calibration]] then separates the Hamiltonian threshold from its Poincare-invariant mass interpretation. These are additional construction obligations, not consequences of calling a response causal or entropic.
