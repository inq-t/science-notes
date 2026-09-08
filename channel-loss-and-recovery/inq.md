---
inq.module: channel-loss-and-recovery
inq.include:
  - './'
inq.ambient:
  - 'receipts/*.py'
keywords:
  - relative entropy
  - channel loss
  - Petz recovery
  - BKM tangents
  - conditional expectations
  - minimum-lift metrics
  - retained output
---
# Channel Loss and Recovery

A channel can erase distinguishability from an input state pair without assigning any stiffness to its retained output. Relative-entropy loss, its tangent Hessian and the minimum loss needed to realize an output change answer different questions. This module constructs those comparisons, characterizes exact recovery, and separates the zero-output result for adapted preserving expectations from genuine contraction by more general channels. The constructions use declared states and metrics; a physical energy scale requires further data.

## Loss composes with the state pair

[[channel-loss-and-recovery/relative-entropy-loss-and-sufficiency|Relative-entropy loss]] is a nonnegative difference of input and output distinguishability. Under successive channels it adds with transported arguments:
\[
\mathcal L_{\Psi\Phi}(\rho;\sigma)
=\mathcal L_\Phi(\rho;\sigma)
+\mathcal L_\Psi(\Phi\rho;\Phi\sigma).
\]
Its zero set is exact recoverability of the declared pair. A statistical family requires a common recovery map. For faithful normal states with finite Araki relative entropy, restriction loss vanishes exactly when the subalgebra retains their Connes cocycle. This does not automatically provide an ordinary preserving expectation onto that entire subalgebra.

These channels encode accessible state transformations and need not be ontological dynamics. [[measured-response-carriers/descent-and-clock-arrows|Descent and clock arrows]] distinguishes channel loss from strict effective descent, which glues compatible data and does not itself create residue or chance.

## The tangent defect remains on the input

[[channel-loss-and-recovery/bkm-loss-operators|BKM loss operators]] differentiate the channel comparison on a declared tangent domain. The input-metric defect is
\[
L_\Phi^\sigma=I-\Phi^{\sharp_\sigma}\Phi,
\qquad 0\leq_{g_\sigma}L_\Phi^\sigma\leq_{g_\sigma}I.
\]
Its positivity refers to the BKM tangent metric, not matrix-algebra complete positivity. Its composition law pulls the later defect back through the earlier tangent map. In Type III, regular curves must define a common quadratic Hessian; obtaining a self-adjoint operator additionally requires a specified Hilbert carrier and a closed form.

[[channel-loss-and-recovery/preserving-expectation-loss|A preserving expectation]] gives a stronger result. Its recovered tangents form an orthogonal BKM subspace, and the loss Hessian is the squared norm of the forgotten component. Every retained tangent has a recovered lift with zero quadratic loss. The unit bound on the incoming vertical quotient therefore supplies no retained-output stiffness. Holding an expectation's index fixed while varying noninvariant reference states also supplies no state-uniform lower bound.

## Output cost is a separate minimization

For a surjective contraction \(A:V\to W\) between finite-dimensional inner-product spaces, [[channel-loss-and-recovery/minimum-lift-output-forms|the minimum-lift construction]] gives
\[
\tau_A(y)=\inf_{Ax=y}
\bigl(\|x\|_V^2-\|Ax\|_W^2\bigr).
\]
Every input loss splits into this minimum output cost and an additional vertical norm. Output costs compose by infimizing over the intermediate carrier, rather than by ordinary addition. This is a specific metric comparison within the broader [[trace-dirichlet-descent/inq|least-cost trace construction]].

For an adapted preserving expectation, \(\tau_A=0\). For a genuinely contracting general channel it can be positive with the ordinary information metrics. [[channel-loss-and-recovery/binary-channel-witness|The binary witness]] has positive cost for \(0<\lambda<1\) and nonzero output tangents, even though its linear tangent map is invertible. Thus loss of metric distinguishability, failure of an admissible inverse, and nontrivial fibers must remain distinct. The linked calculation checks the carrier split and composition identities.

## Neither a kernel nor a metric chooses physical energy

[[channel-loss-and-recovery/normalization-and-coercivity-limits|Normalization and coercivity limits]] exhibits arbitrary positive relaxation rates on one fixed expectation's forgotten subspace. Pointwise invertibility likewise supplies no uniform global lower bound. A derived rate needs quantitative coverage of the complete intended carrier and an independent scale.

[[physical-response-coercivity/localized-relative-entropy-and-the-energy-solder#A descent-loss Hessian also fits|Localized relative entropy]] supplies a physical energy upper comparison in its specified QFT setting. The separate [[physical-response-coercivity/retained-output-casimir-bound|retained-output Casimir bound]] needs a nonzero output response, a complex physical carrier map, a lower frame and an independently normalized Casimir comparison. [[physical-response-coercivity/paired-wall-casimir-comparison|Paired-wall comparison]] instead uses a strongly commuting product on a common carrier. Neither physical construction follows from channel positivity or Petz recovery.
