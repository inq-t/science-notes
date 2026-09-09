---
inq.module: "quantitative-descent"
inq.include:
  - "**/*.md"
keywords: [descent, rigidity, closed-range, finite-word-certificate, bounded-repair, soft-escape]
---
# Quantitative Descent

Quantitative descent asks whether every nontrivial distinction can be reconstructed from its comparison defects with a bound independent of the number of contexts or refinement steps. Exact gluing identifies which distinctions have zero defect; rigidity additionally excludes normalized distinctions whose defects approach zero. The comparison, its norm and its admissible representations must be fixed before seeking that bound.

The constructive alternatives are an explicit finite-polynomial certificate and an independently assembled bounded repair. [[rigidity-certificates-and-soft-escape|Rigidity certificates and soft escape]] proves their lower bounds and gives three controls that retain exact algebraic structure while losing uniform rigidity. The repair estimate allows a dense, potentially unbounded analysis domain; a self-adjoint response operator requires its own closure theorem.

A change of access can discard part of the comparison and part of its repair. [[scale-bearing-descent/variance-completed-rigidity|Variance-completed descent]] records those channels, derives their exact compression formula and states a cumulative error budget. Keeping every loss is an identity; proving that the total loss leaves a strict repair margin is the substantive estimate.

For an observable realization, the response must descend through the actual state-null quotient and detect the complete intended complement. [[measured-response-carriers/response-to-energy-comparison|The physical energy comparison]] then explains which normalization and form-core conditions turn rigidity into an energy bound. [[scale-bearing-descent/inq|Scale-bearing descent]] places this construction within a proposed law of comparison, while [[global-local-response-reconstruction/inq|global–local reconstruction]] specifies its physical return.
