# Connection and Generator Conventions

The transport-intertwining defect is the covariant derivative induced on maps between two bundles. Its signs depend on whether transport is written as an evolution equation or a parallel-section equation. A metric connection is a stronger datum than a general Banach evolution, and a statistical score identity on one reference section does not automatically define a differentiable operator family on every tangent.

## The induced derivative on maps

Let \(\mathcal H_\pm\to I\) be differentiable Hilbert bundles. In fixed unitary trivializations, write supplied metric connections as
\[
\nabla_\pm=\partial_N+\Gamma_\pm(N),\qquad \Gamma_\pm^*=-\Gamma_\pm.
\]
One sufficient setting is bounded norm-continuous connection coefficients and a norm-\(C^1\) map family \(J_N\). For unbounded coefficients or weaker map regularity, declare common section domains preserved by every composition and prove the product rule there. Local triviality already requires locally constant fiber type; a dimension-changing blocking map does not by itself supply such a bundle.

For an admissible source section \(x\), define
\[
(\nabla^{\mathrm{Hom}}J)x:=\nabla_+(Jx)-J\nabla_-x.
\]
The derivatives of \(x\) cancel, leaving
\[
\nabla^{\mathrm{Hom}}J=J'+\Gamma_+J-J\Gamma_-.
\]
If \(V_\pm(s,t)\) are the corresponding parallel transports, vanishing of this derivative is equivalent, under the stated transport regularity, to
\[
J_sV_-(s,t)=V_+(s,t)J_t.
\]
The equivalence concerns transport compatibility, and does not require \(J\) to be invertible.

## Evolution uses the opposite connection sign

An evolution equation \(x'=A x\) says that \((\partial_N-A)x=0\). Thus its connection coefficient is \(\Gamma=-A\), and
\[
\nabla^{\mathrm{Hom}}J=J'+JA_--A_+J.
\]
This is exactly [[transport-intertwining-defect/propagator-intertwining-and-placement#The exact wall-defect identity|the propagator defect (WD5)]]. The plus sign in \(\partial+\Gamma\) must not be transferred to an evolution generator without this conversion.

For bounded coefficients on fixed Hilbert spaces, metric parallel transport is unitary and the evolution generator is skew-adjoint. A dissipative semigroup, a smoothing contraction and a general Banach evolution need not satisfy that metric condition. The propagator product rule can apply to them without asserting a metric Hilbert-bundle connection.

## Source and target frames transform independently

Under differentiable unitary frames \(W_\pm\),
\[
\widetilde\Gamma_\pm=W_\pm\Gamma_\pm W_\pm^{-1}-W_\pm'W_\pm^{-1},\qquad
\widetilde J=W_+JW_-^{-1}.
\]
Consequently
\[
\widetilde{\nabla^{\mathrm{Hom}}J}
=W_+(\nabla^{\mathrm{Hom}}J)W_-^{-1}.
\]
The two frames are independent; this is ordinary conjugation only when source and target have been identified and their frame changes agree. General bounded isomorphisms obey the same algebraic law with transported metrics, as in (WD7a)--(WD7b).

For a moving statistical channel, existence of a differentiated output density can give a score identity on a reference section without giving an operator-norm derivative of the full conditional-prediction map. Applying the complete map-level calculus requires its own differentiability and domain hypotheses, especially when score multiplication is unbounded.
