---
inq.module: "auxiliary-response-localization"
inq.include:
  - "**/*.md"
inq.ambient:
  - "**/*.py"
keywords: [auxiliary dynamics, covariance decay, Witten Laplacian, exact one-forms, locality, Yang–Mills]
---
# Auxiliary Response Localization

A local proof dynamics on a Euclidean law can certify static response decay without representing physical time. Its forgetting rate and influence speed together determine a spatial exponent that is unchanged by rescaling the auxiliary clock. A complementary Witten formulation localizes the susceptibility induced by an exact local score. Physical energy enters only after the resulting Euclidean estimates pass through a reconstruction and scale comparison.

[[auxiliary-clock-elimination|Auxiliary clock elimination]] combines centered contraction with a two-observable influence bound. The product-defect identity separates local influence from the remaining covariance, and balancing their decay rates removes the auxiliary parameter. Reversibility is unnecessary once those estimates hold. A scalar Poincare floor without spatial influence control cannot perform this step, and different samplers can yield different nonoptimal certificates for the same law.

[[witten-covariance-and-local-response|Witten covariance and local response]] writes the same covariance as the pairing of one local score with the reduced inverse one-form response to another. Its operator acts on configuration-space exact one-forms. A global weighted response bound is sufficient for exponential covariance decay; [[exact-source-locality-without-a-full-form-gap|exact-source locality]] provides a distinct direct off-support estimate using a gap only on the exact sector and weighted growth on the full nonnegative operator. That argument reaches covariance decay without asserting the stronger global weighted norm at the same exponent.

The downstream spectral statement has a different owner and carrier. [[positive-semigroup-decay/total-family-spectral-gap|One common exponent on a total family]] excludes low spectrum of a positive self-adjoint semigroup. With [[positive-semigroup-decay/physical-reconstruction-and-units|full OS translation reconstruction and physical units]], it applies to a gauge-invariant local family whose linear span is Hilbert-norm dense in the vacuum complement. Observable-dependent constants and onset lengths are allowed; the exponent must be common. Equal-time spatial clustering requires a further comparison to the OS translation direction, and reflection positivity alone does not construct that translation semigroup.

[[conditional-correlation-tensorization/inq|Conditional correlation tensorization]] asks a stronger question: can estimates surviving every required pinning bound a complete boundary-response angle? Its matrix norm must be uniformly below one; entrywise decay alone is insufficient. This route controls more than the total-family spectral argument and has separate boundary, sector, and summability hypotheses.

[[yang-mills-response-calibration|Yang–Mills response calibration]] locates the remaining physical construction. Microscopic strong-coupling estimates are established precedents. A regulator-uniform passage from the asymptotically free law to a fixed physical scale, control of transported source prefactors, a nontrivial continuum theory, and OS/Poincare realization are still required. The primitive certificate is localization per declared cut distance; a calibrated physical comparison gives energy and invariant mass.
