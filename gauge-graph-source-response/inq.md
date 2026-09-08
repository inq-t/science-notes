---
inq.module: "gauge-graph-source-response"
inq.include:
  - "./"
inq.ambient:
  - "**"
keywords: [gauge frames, heat paths, Fisher response, loop interactions, Gibbs specifications, exterior relaxation]
---
# Gauge Graph Source Response

A declared graph source can determine its gauge constraint, state and mixed response together. Haar vertex frames supply zero-cost gauge motions, while retained edge heat paths supply finite-cost variations. Their entropy Hessian fixes the observable cometric and a closed auxiliary clock. Interactions change this response through the same source likelihood; constructing it still leaves the graph, interaction, comparison actions and physical realization to be selected.

The [[gauge-graph-source-response/haar-vertex-source-and-joint-gauge-response|Haar-vertex construction]] makes finite response equivalent to the complete Gauss constraint. Shared edge factors produce the mixed derivatives needed by [[gauge-boundary-frame-gluing/oriented-context-gluing-and-mixed-response|charged context gluing]]. On a finite graph the independent heat source returns a smooth positive endpoint density and an electric-type weighted diffusion. Its own invariant-cylinder closure extends to a countable fixed graph and inherits an auxiliary lower bound of two from the absence of invariant first Wiener chaos. The source Ornstein--Uhlenbeck semigroup nevertheless fails to preserve the endpoint readout in the explicit two-edge example.

[[gauge-graph-source-response/loop-correlations-and-the-source-response|A loop interaction]] changes both the state and the retained-path Fisher metric. Conjugation symmetry reduces the entropy correction to an averaged endpoint Hessian, and a Gaussian-tail argument proves coercivity at every fixed finite smooth coupling. Completing the full source comparison before dualizing gives the returned response; averaging or marginalizing first can give a different experiment. Ordinary subdivision preserves the tilted state but changes this response, even at first order.

[[gauge-graph-source-response/local-interaction-cocycle-and-global-source-response|Local interacting specifications]] replace a global bounded-density hypothesis by compatible conditional laws and a chosen invariant Gibbs state. Every finite-support likelihood includes the interactions crossing its boundary. A uniform weighted-Hessian smallness bound permits completion of the global Fisher stiffness, controls its inverse tails, and closes the full invariant-cylinder response. The exterior contributes a Schur correction to a local inverse; independently inverting regional blocks omits it. This is an infinitesimal response construction on one fixed graph and state, without a claim about infinite-support quasi-invariance or a physical spectral gap.

The finite and countable constructions therefore answer how a supplied experiment returns a response. They do not select its vacuum: an arbitrary positive finite-graph density can be installed by a loop weight. A Yang--Mills realization additionally needs its physical carrier, translations, continuum limit and independently calibrated comparison.
