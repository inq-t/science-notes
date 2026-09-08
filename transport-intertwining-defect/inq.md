---
inq.module: transport-intertwining-defect
inq.include:
  - './'
keywords: [intertwining, propagators, covariant derivative, changing carriers, observation, closed range]
---
# Transport Intertwining Defect

A comparison map between two evolving carriers can depend on where it is inserted. Its covariant derivative measures that dependence: the map's own change, followed by the difference between evolving before and after comparison. This module separates the exact transport identity from two further operations: observing the defect through a finite readout, and assigning it a positive metric response. Neither a nonzero defect nor a positive response alone supplies a physical interpretation or a spectral gap.

## Compare transport across the map

For evolution generators \(A_\pm\) and a differentiable map \(J_\sigma:X_-\to X_+\), [[transport-intertwining-defect/propagator-intertwining-and-placement|propagator intertwining]] defines
\[
\mathfrak D_\sigma=J_\sigma'+J_\sigma A_-(\sigma)-A_+(\sigma)J_\sigma.
\]
On the declared domains, inserting this operator between the incoming and outgoing propagators gives the derivative of the terminal state with respect to insertion address. Zero defect makes that address invisible within this composite. A noninvertible comparison can nevertheless have zero defect.

[[transport-intertwining-defect/connection-and-generator-conventions|Connection and generator conventions]] identifies the same operator as an induced derivative on maps. Evolution \(x'=Ax\) uses the connection \(\nabla=\partial-A\). A metric connection in a unitary frame is often written \(\partial+\Gamma\); the relation is \(A=-\Gamma\). General dissipative evolution does not automatically define a metric connection.

## A readout retains only part of the defect

[[transport-intertwining-defect/observation-of-a-transport-defect|Observation of a transport defect]] applies a frozen observation derivative and removes specified nuisance directions. A nonzero residual derivative is exactly first-order sensitivity to one insertion parameter in that model. It is weaker than finite-noise detectability and does not reconstruct the full defect operator. A finite experiment returns only its response class modulo the kernel of the chosen readout.

## Positivity requires a metric and a domain

The defect is generally rectangular and has no positivity order. [[transport-intertwining-defect/metric-response-of-an-intertwining-defect|Its metric response]] requires a target metric and a source Hilbert carrier. The squared norm of the weighted defect becomes a closed quadratic form only after a closable operator realization is supplied. Closed range then characterizes a positive lower bound modulo that realization's kernel; full physical coverage and energy normalization are further data.
