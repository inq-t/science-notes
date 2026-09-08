---
inq.module: finite-index-distinction
inq.include:
  - './'
inq.ambient:
  - 'receipts/*.py'
  - 'receipts/*.txt'
keywords:
  - finite index
  - conditional expectation
  - statistical dimension
  - Connes fusion
  - relative entropy capacity
  - center symmetry
  - cosmic capacity weld
---
# Finite-Index Distinction

Finite-index inclusions quantify algebraic size, duality normalization and maximum information loss. They do not by themselves quantify the minimum response of every nonvacuum physical direction. This module develops that distinction through the conjugate square, the entropy capacity and the gauge-center tests, then states the additional law that would relate categorical capacity to a cosmological scale family.

## A square normalization becomes intrinsic only with standard data

[[finite-index-distinction/finite-index-duality-and-the-square-response|Finite-index duality]] starts with a chosen normal faithful finite-index expectation \(E\) between properly infinite von Neumann algebras. Its conjugate data contain an intertwiner obeying

\[
\widetilde v_E^*\widetilde v_E=\operatorname{Ind}(E),
\qquad
V_E=\widetilde v_E\operatorname{Ind}(E)^{-1/2},
\qquad V_E^*V_E=1.
\]

In a factor with chosen index greater than one, \(V_E\) is a proper isometry. It differs from the projection-like implementation of the expectation, and its norm preservation distinguishes no vacuum. Only a minimal expectation and standard conjugate solution identify the index with intrinsic squared statistical dimension \(d(X)^2\). For standard factor sectors, \(d\) multiplies under Connes fusion, so \(\log d\) supplies an additive address. [[spectral-wall-descent/scale-correspondence-stack|The correspondence construction]] retains the fuller dimension data needed when centers are nontrivial.

This square suggests an algebraic input to [[scale-incidence-response/compensated-incidence-response-and-four-dimensional-balance|compensated scale response]]. A fixed scalar normalization does not supply that theorem's nontrivial scale family, geometric character or lower physical response. Those require separately constructed comparison maps.

## Entropy capacity is a maximum, coercivity is a minimum

[[finite-index-distinction/two-sided-index-capacity-and-the-cosmic-weld|Two-sided index capacity]] records the established infinite-factor result

\[
\mathfrak C(E)
=\sup_\varphi S(\varphi\Vert\varphi\circ E)
=\log\operatorname{Ind}(E).
\]

With the stated standard-form hypotheses, losses for an expectation and its normalized commutant dual also share a statewise log-index budget. A standard minimal sector realized over infinite-dimensional factors gives \(\mathfrak C(X)=2\log d(X)\), additive under fusion. Finite-dimensional unamplified examples can have smaller capacity: retained side information and matrix amplification matter. [[spectral-wall-descent/finite-index-area-weld|The selected edge-entropy weld]] is therefore a different comparison from this full operational capacity.

The supremum describes how much distinction can be erased. A coercivity estimate asks how little response any nonvacuum direction can have. [[trace-dirichlet-descent/subfactor-angle-coercivity-and-the-index-firewall|The fixed-index angle counterexample]] holds the relevant indices fixed while the response edge collapses. [[categorical-gauge-response/quantum-g2-categorical-rigidity-and-the-carrier-firewall|Categorical rigidity]] investigates an additional invariant capable of constraining a minimum; it is not recovered from the sector capacity alone.

## Gauge topology supplies a finite remnant with limited coverage

[[finite-index-distinction/gauge-index-no-go-and-four-dimensional-center-square|The gauge-index audit]] separates local Gauss-law reduction, compact global fixed points, finite charged extensions and ring additivity--duality inclusions. For a faithful minimal compact-group action on a factor with separable predual, the global fixed-point inclusion has finite index exactly when the effective group is finite. A faithful global \(SU(N)\) action therefore cannot provide the desired finite-index inclusion.

Under the stated pure-gauge net hypotheses in four dimensions, electric and magnetic center classes instead give a ring index \(|Z(G)|^2\) and certainty budget \(2\log|Z(G)|\). That topological plateau is trivial for centerless groups and cannot be the universal cause of a Yang--Mills gap. The note's fixed-index BKM counterexample further separates categorical size from a normalized tangent-response edge.

## A cosmic comparison must choose its composition law

The two-sided capacity note distinguishes an additive identification

\[
\iota_n-\iota_b=2n\log d(X)
\]

from the stronger multiplicative effective-cell law

\[
\log(\iota_n/\iota_b)=2n\log d(X).
\]

Here \(\iota=S_A/k_B\) is the dimensionless horizon ledger supplied by [[cosmological-scale-selection/cosmic-geon-hypothesis-and-horizon-rate-ledger|the cosmic-geon calculation]]. The second law, together with its Einstein apparent-horizon assumptions, gives \(H_n/H_b=d(X)^{-n}\); the first does not. Neither law follows from the entropy theorem. A composition-preserving physical comparison, a selected rung and an independent absolute normalization are still needed before [[cosmological-scale-selection/cosmological-selection-of-the-yang-mills-yardstick|the common-count construction]] can select a dimensional member.

The gauge-index and two-sided capacity notes link their finite receipts and retained outputs. These check matrix counterexamples, ancillary-carrier dependence and conditional scalar arithmetic. The physical capacity weld, full-carrier coercivity, energy comparison and gravity-decoupled Yang--Mills limit remain independent obligations.
