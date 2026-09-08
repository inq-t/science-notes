---
inq.module: exceptional-state-comparison
inq.include:
  - './'
inq.ambient:
  - 'receipts/*.py'
keywords: [exceptional contexts, Albert algebra, Peirce readouts, entropy loss, finite matrix coverage, qubit return]
---
# Exceptional State Comparison

Exceptional Jordan contexts determine finite positive comparisons, but their coverage depends on the carrier and the family of readouts. Cyclic retractions separate trace-free Albert observables while missing directions in their larger matrix realization. Primitive Peirce readouts cover that full matrix carrier. A different average, keeping a rank-two corner fixed, yields a qubit process. The invariant measures and process conventions are declared inputs; none of these finite bounds supplies a field-theoretic mass gap.

## Context loss and its matrix realization

Starting from the [[albert-algebra/inq|Albert algebra]], Yokota’s chosen order-three automorphism selects its complex fixed context. [[exceptional-state-comparison/cyclic-context-retraction-and-response|Cyclic context retraction]] is positive and has an exact variance residue. Averaging the discarded projections over the full compact \(F_4\) orbit gives \((9/13)I\) on the trace-free Jordan carrier, hence a bounded reconstruction map. Regular multiplication realizes the same retraction through a completely positive matrix expectation, with a calculable relative-entropy-loss Hessian.

That regular realization enlarges the carrier from Jordan observables to all matrices on \(J_{\mathbb C}\). A nonzero balance between the unit line and its trace-free complement is invisible to every cyclic matrix expectation. [[exceptional-state-comparison/primitive-peirce-response|Primitive Peirce response]] adds the readouts determined by all primitive idempotents. An exact integer certificate for the regular-multiplier response supplies a lower bound for their averaged loss on every traceless matrix, including the balance direction, and yields a global finite-state entropy contraction. This is additional coverage, not a quotient that discards the counterexample.

## Fixing a corner changes the comparison

[[exceptional-state-comparison/peirce-context-averaging-and-the-emergent-qubit-process|Peirce context averaging]] fixes a rank-two unit and moves its complex contexts under \(\operatorname{Spin}(9)\). The retained three-plane inside nine trace-free corner directions gives a qubit depolarizer with centered eigenvalue \(1/3\). Its Poisson and logarithmic interpolations have different normalized rates. Individual Jordan comparisons can fail complete positivity even though this particular averaged return is completely positive.

The orbit, measure and carrier must stay attached to each coefficient. In particular, [[primitive-state-diffusion/inq|primitive-state diffusion]] instead compares functions on an entire primitive orbit. Its overlap moment shares a number with the finite matrix construction but acts on an infinite-dimensional function space and requires its own refinement and domain argument.

## Finite coverage leaves a field question

A fiberwise unital map fixes \(f(U)I\) for every scalar configuration function \(f\). Complete finite matrix coverage therefore says nothing by itself about nonconstant Wilson observables. [[global-local-response-reconstruction/exceptional-context-analysis-of-gauge-gradients|Differentiated context analysis]] applies the finite frame to genuine gauge-representation gradients under a specified field law. It supplies a field-sensitive analysis map; uniform coercivity for that law and comparison with the physical transfer spectrum remain additional obligations.
