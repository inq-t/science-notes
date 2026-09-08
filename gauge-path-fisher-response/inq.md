---
inq.module: gauge-path-fisher-response
inq.include:
  - './'
inq.ambient:
  - 'receipts/*.py'
  - 'receipts/*.txt'
keywords:
  - heat paths
  - Fisher response
  - gauge projection
  - source retention
  - Ornstein–Uhlenbeck clock
  - annular restart
  - compression defect
---
# Gauge path Fisher response

A compact-group heat-path state supports several inequivalent response geometries. Choosing the transformations whose state costs are measured, deciding which source variables remain available, and dualizing before or after gauge projection can change both the finite-response carrier and its closed clock. These explicit constructions separate those choices: they derive complete auxiliary thresholds and gluing laws without identifying the supplied heat-area coordinate or the resulting response duration with physical time.

The [[gauge-path-fisher-response/shared-driver-response-and-the-nested-holonomy-clock|shared-driver construction]] couples nested holonomies through one driving path. Its mixed response repairs the nearby-loop nonclosability of an edge-diagonal perimeter form. The full continuous path retains its stochastic logarithm, so Wiener calculus supplies a closed form with a cylinder core and an Ornstein–Uhlenbeck clock. On simultaneous-conjugation invariants of a nontrivial compact connected semisimple group, the unit clock has an attained threshold two. The same state also admits positive, nonuniform driver rates with zero threshold. A common restart law forces constant intensity within that family, while leaving its overall calibration free.

[[gauge-path-fisher-response/path-shift-fisher-geometry-before-gauge-projection|Path-shift Fisher geometry]] supplies a different selection condition: declare deterministic left path multiplication, compute its actual relative entropy, and dualize the resulting Fisher metric on pointwise observable variations. This fixes the shared-driver response. Projecting the perturbation scores to gauge invariants first erases their first-order metric; it does not erase the response already defined on invariant observables. Choosing right multiplication instead gives an inversion-related clock whose response differs on suitable three-holonomy invariants.

For a compact connected group with nonabelian simple Lie algebra, retaining both actions produces [[gauge-path-fisher-response/two-sided-fisher-completion-and-the-neutral-carrier|the joint two-sided response]]. Its cross-score covariance and singular behavior near the path origin force finite smooth cylinders to be jointly neutral. The closed cylinder form has unique constant vacuum and threshold two, now without an excited eigenvector at that threshold. It respects terminal enlargement and heat-time reparametrization, but fails the same-clock annular restart law. Conditioning on the retained prefix before dualization changes the response again and excludes some globally neutral observables; copying this metric independently onto graph edges imposes the wrong gauge carrier.

[[gauge-path-fisher-response/heat-factor-response-and-the-compression-defect|Retaining two independent heat-factor sources]] gives the same output heat law with a different Fisher experiment. Its restricted source response is a weighted combination of the handed forms. The invariant-cylinder closure admits neutral annular restart and charged ordered cuts with an endpoint frame correction; its threshold two is also not attained. Yet the original product source clock does not descend through the readout: a source-chaos component varies along a fiber invisible to every output observable. This realizes the distinction between [[trace-dirichlet-descent/standard-form-pullback-and-reducing-wall|closing a pulled-back response and compressing a source semigroup]].

The analytic inputs concern complete compact-group path carriers, finite heat horizons, and declared source actions. An ordered path cut does not establish an order-independent spatial graph law; [[gauge-source-action-transport/inq|source-action transport]] and [[gauge-graph-source-response/inq|graph source response]] formulate those further compatibility tests. A spacetime-local observable net, a four-dimensional continuum state, and a physical Hamiltonian remain separate constructions. In particular, an auxiliary threshold alone does not supply [[mass-scale-calibration/inq|an invariant mass or its calibration]].
