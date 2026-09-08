---
inq.module: holonomy-state-refinement
inq.include:
  - './'
inq.ambient:
  - 'receipts/*.py'
keywords:
  - holonomy
  - heat-kernel state
  - face refinement
  - boundary amplitudes
  - clock compatibility
  - weighted girth
  - response closability
---
# Holonomy state refinement

A gauge refinement must preserve the state, the observable embedding, and the response needed to define a clock. These requirements are distinct. Exact face integration can produce a consistent heat state while a proposed response fails to close; a closed compatible refinement clock can instead exist with zero spectral gap. This module develops explicit compact-group examples that identify which additional structure each step requires.

[[holonomy-state-refinement/overlap-kernels-and-face-refinement|Overlap kernels and face refinement]] begins with a declared faithful matrix representation and an anchored trace comparison. Sharpening its density and convolving the resulting increments gives a heat kernel. Interior integration on regular disks and face carpets then yields an exact coarse boundary law and fixed-box convergence. Full mesh elimination exposes several representation channels, requiring boundary amplitudes beyond one scalar face weight. The coincident boundary-star Hessian computes their relative response, while leaving propagation to a separate construction.

Temporal sewing makes that separation explicit. On a fixed spatial graph, a declared anisotropic scaling of temporal comparisons and spatial potentials yields a complete compact-rotor clock. Applying the same sharpening power to both kinds of face instead gives a singular fixed-carrier limit, even after vacuum normalization. Neither result identifies face subdivision with physical duration or supplies simultaneous spatial refinement.

[[holonomy-state-refinement/holonomy-refinement-and-clock-compatibility|Holonomy refinement and clock compatibility]] tests the spatial step. Independent-link diffusion weights must add along each coarse edge; faithful vacuum reweighting preserves this principal-response condition. General mixed responses obey a conditional tensor pullback, but matching that form alone need not make a compressed clock autonomous. For a compatible countable Haar refinement, the full physical threshold is the least nontrivial Casimir times the infimum of weighted cycle lengths. New arbitrarily cheap loops therefore close the gap although the vacuum remains unique. A different natural mixed cometric can instead miss closed-loop distinctions entirely.

[[holonomy-state-refinement/heat-state-continuity-and-response-closability|Heat-state continuity and response closability]] changes the state to the area-additive planar heat law. Its small-loop behavior escapes the bounded-density Haar comparison, yet the additive perimeter response fails a stronger test: nearby loop characters converge in the state's Hilbert norm while remaining response-orthogonal. Their averages prove nonclosability. The [[gauge-path-fisher-response/inq|path-source constructions]] supply mixed responses compatible with this convergence on the nested-holonomy sector. Extending such a response to the full graph carrier, selecting its physical clock, and constructing a four-dimensional Yang–Mills vacuum remain further requirements.
