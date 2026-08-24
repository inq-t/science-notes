# Terminology and Type Discipline for the Ruble Programme

The Ruble discussion uses several words—constant, invariant, capacity, charge, information, quotient, and running—that name different mathematical types. This provisional vocabulary prevents a true statement about one type from being promoted into a false statement about another.

## Core vocabulary

| Term | Strict mathematical type | Proposed role here |
|---|---|---|
| Presentation | representative description before physical equivalences are imposed | a scale section, observer cut, algebra--state fiber, or coordinate description |
| Observational quotient | equivalence classes under equality of all declared accessible observables | removes differences with no operational bearing |
| Presentation groupoid | objects together with explicit reversible arrows between presentations | retains stabilizers and comparison data erased by an orbit set |
| Causal individuation | not yet one standard mathematical object | capacity for a distinction to become causally placed, metrically comparable, and recordable |
| Distinguishability | relative comparison of states on a declared algebra | measured locally by relative entropy or another controlled divergence |
| Causal capacity | positive quadratic response or measure | amount of distinguishability curvature available along a physical causal-scale tangent |
| Modulus | intensive response coefficient | capacity per causal area |
| Compliance | inverse modulus | causal area per unit capacity |
| Casimir | invariant polynomial of a representation | fixed algebraic norm redistributed between mean order and covariance |
| Charge | linear moment-map, Noether, or boundary quantity | candidate conserved value of a common causal generator |
| Entropy | state-, algebra-, and prescription-dependent accounting quantity | horizon entropy is one geometric capacity measure, not every BKM norm |
| Fact | selected contextual value or character | determinate pointing, not an expectation or probability measure |
| Record | dynamically stable physical encoding | persistence of a fact within a common history |

The canonical distinctions among capacity, charge, entropy, fact, and record are developed in [[conservation-of-causal-charge/causal-charge-meaning|The Meaning of Causal Charge]].

## Constant, invariant, and universal

A **constant along a flow** is a function $I$ satisfying

$$
\frac{\mathrm dI}{\mathrm d\lambda}=0
$$

for a declared evolution parameter $\lambda$.

A **coordinate invariant** has the same value after an allowed reparameterization. This does not imply that it is constant from state to state.

A **model parameter** is held fixed inside one effective family. It need not have the same value in another solution or microscopic realization.

A **universal coefficient** has the same value throughout a stated universality class after physical normalization and renormalization are fixed.

A **fundamental constant of nature** is a universal empirical coefficient entering physical laws. For a dimensionful constant, its invariant content lies in the conversion law or in dimensionless comparisons, not in its unit-dependent decimal representation.

The current $\mathfrak R_c$ is a coordinate-invariant dimensionless peak ratio and a parameter of the generalized homogeneous model. It has not been proved universal across states, cuts, species, regulators, or gravitational sectors.

## State function, horizontal flow, and RG running

A universal state functional has a fixed rule but state-dependent output:

$$
\mathfrak R:\mathfrak S_{\mathrm{adm}}\longrightarrow\mathbb R_+,
\qquad
\omega\longmapsto\mathfrak R[\omega].
$$

Along a physical scale path $N\mapsto\omega_N$, a horizontal flow law would have the form

$$
\frac{D\mathfrak R}{\mathrm dN}
=\beta^{\mathrm{hor}}_{\mathfrak R}
(\mathfrak R,\nu,\lambda_I,\ldots).
$$

This is not automatically renormalization-group running. A genuine running coupling requires a coarse-graining or renormalization scale $\mu$, an effective operator basis, a regulator and subtraction prescription, and an equation such as

$$
\mu\frac{\mathrm d\mathfrak R}{\mathrm d\mu}
=\beta_{\mathfrak R}.
$$

The logarithmic cosmological coordinate $N$, a modular parameter, and an RG scale are differently typed. Their numerical similarity or additive composition does not identify them.

## Matching point, fixed point, and pathwise identity

The following claims are inequivalent:

$$
\mathfrak R(N_c)=1
$$

states unit matching at one distinguished cut;

$$
\beta_{\mathfrak R}(1)=0
$$

states that one is a fixed point of a declared flow; and

$$
\mathfrak R(N)=1\quad\text{for every }N
$$

states exact equality throughout a path or domain.

The present unit-amplitude principle asserts the first. It does not establish the second or third.

## Information, precision, and capacity

The word *information* is too broad to carry an equation without further typing. In this programme:

- relative entropy compares two states on a declared algebra;
- a BKM metric is a second-order tangent response;
- covariance describes fluctuations or correlations;
- precision is inverse covariance on a physical quotient;
- entropy is an accounting functional of a state or horizon prescription;
- channel number or density supplies extensive normalization; and
- causal capacity is the proposed physical interpretation of an appropriately localized positive response.

None is an ontological substance. In particular,

$$
\text{lost distinguishability}
\ne
\text{gravity}
$$

without an equivariant construction of the state--geometry map.

## Recommended provisional names

| Symbol or statement | Provisional name |
|---|---|
| $\mathcal G_{\mathrm{CI}}$ | causal-individuation metric or causal distinguishability geometry |
| $\mu^\perp_{\mathrm{BKM}}$ | horizontal causal-capacity measure |
| $\chi_{\downarrow}$ | causal-capacity modulus or areal descent modulus |
| $\mathfrak a_{\downarrow}=\chi_{\downarrow}^{-1}$ | causal compliance |
| $\mathfrak R_\Sigma$ | Ruble quotient or state--geometry equivalence quotient |
| $\mathfrak R_\Sigma=1$ | unit Ruble matching or causal-capacity equivalence principle |
| $Q_\xi$ | causal charge, only after the generator and moment map exist |

“Ruble's Constant” should remain a historical or informal name until a domain, flow, normalization, and universality theorem establish what is constant.
