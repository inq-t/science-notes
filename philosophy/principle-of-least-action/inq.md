---
inq.module: "principle-of-least-action"
inq.include:
  - "**/*.md"
---
# The Variational Axiom

The first of the three principles this section studies as candidate axioms: a dynamical law may be represented by stationarity of a functional of histories rather than specified only as a state-propagation rule. "Least" is historical shorthand for $\delta S=0$, which permits a minimum, maximum or saddle. Whether an action exists is a separate question from its symmetry and conservation laws. Composition of history phases and realization of a quotient clock provide two conditional routes to action; neither establishes stationary action as a primitive law of the whole.

## The axiom

For a set $\mathcal H$ of admissible histories,

$$
S:\mathcal H\longrightarrow\mathbb R,
\qquad
\boxed{\ \text{physical histories are those with }\delta S=0\ }
$$

over a declared class of variations. [[what-the-axiom-asserts]] fixes what this does and does not claim: that the passage to local Euler--Lagrange equations is a theorem with hypotheses rather than a definition, that the global form is the weaker one because the two-point problem it poses can have no solution or many where the initial-value problem has exactly one, and that the axiom therefore characterizes the solution set rather than producing it.

## What a variational principle must specify

An extremum slogan is not a principle. Each of the following is a separate choice, and changing any one changes the physical content.

| Ingredient | Question it answers |
|---|---|
| Variables | What is allowed to change: particle paths, fields, metrics, density matrices, fluxes? |
| Functional | What number is assigned to each candidate: action, entropy, free energy, effective action? |
| Domain | Which histories or configurations are admissible? |
| Constraints | What is held fixed, and which conservation laws are imposed? |
| Boundary data | Are endpoints, boundary values, momenta, or asymptotic states fixed? |
| Extremality condition | Is the first variation zero, or is a genuine minimum or maximum required? |
| Interpretation | Is the extremum an equation of motion, an equilibrium condition, a saddle approximation, or a probability statement? |

"Maximize entropy" at fixed energy and "minimize free energy" at fixed temperature describe the same equilibrium in different environments, whereas maximizing entropy with no stated constraints is not a usable principle at all.

## The axiom has content

[[variational-is-a-restriction]] shows that variationality excludes dynamics: a system is variational exactly when its Fréchet derivative is self-adjoint, whose coordinate form is the Helmholtz conditions. The criterion tests a presentation rather than a dynamics, so the invariant question is the multiplier problem — vacuous for one degree of freedom, classified by Douglas for two, open beyond.

That note also disposes of the standard illustration. The damped oscillator *is* variational. What dissipation costs is not an action but a symmetry of one, which is the first indication that the second axiom is independent and the third genuinely needs both.

## The axiom has a partial ground

[[why-an-action-at-all]] reconstructs part of the form from a composition law: nonzero complex scalar weights have additive logarithms modulo branch ambiguity. A compatible absolutely continuous lift gives an integral density along a history, not automatically a finite-jet local Lagrangian. Phase-only weights initially give a circle-valued action. Stationary-phase conclusions require a defined oscillatory integration problem and controlled asymptotics.

[[algebra/quotient-clock-and-stationary-action|The quotient-clock route]]
instead derives an exact stationary state action from a one-sided process
and its complex positive realization. The
[[directed-analytic-realization/inq|analytic-tail member]] calculates its
Hilbert quotient and generator from the same translation rule. This is a
worked state-space variational representation, not yet a spacetime-local QFT
action or a physical mass-gap construction.

[[algebra/cauchy-response-and-local-action|The opposed-boundary theorem]]
now returns an actual local scalar action in \(3+1\) coordinates from
that state action, using a supplied three-dimensional response geometry.
The exact relation is an endpoint correction followed by elimination of
the normal-response variable. It does not derive the chosen arena or
an interacting gauge theory.

## Flavors

These share variational mathematics and do not all assert the same physical principle.

Their detailed owners are [[classical-action|classical action]], [[einstein-hilbert-action|Einstein--Hilbert action]], [[quantum-action|quantum action]], [[thermodynamic-equilibrium|thermodynamic equilibrium]], and [[kinetic-and-stochastic|kinetic and stochastic principles]].

| Flavor | Object varied | Functional or weight | Meaning of the condition |
|---|---|---|---|
| Classical | particle or classical-field histories | $S=\int L\,\mathrm dt$ or $\int\mathcal L\,\mathrm d^dx$ | the realized history satisfies $\delta S=0$ |
| Einstein--Hilbert | spacetime metric, plus matter | $S_{\mathrm{EH}}+S_{\mathrm m}$ with boundary terms | metric stationarity yields Einstein's field equation |
| Quantum | all histories, states, or mean fields | phase $e^{iS/\hbar}$, state action, or effective action $\Gamma$ | histories interfere; classical saddles and quantum-corrected stationarity arise in different limits |
| Thermodynamic | macrostates | $S_{\mathrm{th}}$ or a thermodynamic potential | equilibrium extrema, exact under stated constraints |
| Kinetic and stochastic | instantaneous rates, or whole stochastic histories | dissipation functionals, Onsager--Machlup path weight, path entropy | least dissipation near equilibrium; most-probable path relative to a noise model |

The first three vary histories or fields; the fourth varies macrostates and is not a history principle at all; the fifth varies rates or histories but weights them probabilistically. Only the first two assert $\delta S=0$ for a mechanical action in the sense of this axiom.

Shared variational form is not a derived physical equivalence. Writing an entropy, a Euclidean action, or an information measure as an extremized functional does not identify it with mechanical action; that requires an explicit map among variables, constraints, dynamics, dimensions, measures, and limiting regimes. These principles are unified securely at the level of mathematical architecture and remain domain-dependent in meaning.

## Glossary

- **Action:** a functional of an entire history, conventionally with dimensions of energy times time.
- **Functional:** a map from a function, field, curve, or history to a number.
- **Variation:** an infinitesimal comparison of a candidate with nearby admissible candidates.
- **Stationary point:** a configuration whose first variation vanishes.
- **Extremum:** a local or global minimum or maximum; every differentiable interior extremum is stationary, but not every stationary point is an extremum.
- **On shell:** evaluated on a history satisfying the equations of motion.
- **Off shell:** evaluated on an admissible history that need not satisfy them.
- **Boundary term:** a contribution supported at the boundary; it may leave bulk equations unchanged while changing the admissible boundary-value problem and the physical charges.

## Claim levels

| Status | Content |
|---|---|
| **[STANDARD]** | the Euler--Lagrange equivalence, for a first-order Lagrangian with fixed endpoints and regularity; self-adjointness of the Fréchet derivative as the criterion for variationality, locally on a star-shaped domain; local solvability of the inverse problem for one degree of freedom, after Darboux; Douglas's classification of the two-degree-of-freedom multiplier problem; non-uniqueness of the two-point problem at conjugate points; the equilibrium and near-equilibrium extremum principles of the thermodynamic and kinetic flavors, under their stated constraints |
| **[EXACT]** | failure of the first Helmholtz condition for a non-symmetric acceleration matrix; the Caldirola--Kanai Lagrangian for the damped oscillator |
| **[CONDITIONAL THEOREM]** | a circle-valued additive action from multiplicative $U(1)$ weights; a compatible real lift and absolute continuity give a density along a history; finite-jet locality and stationary-phase control remain additional hypotheses; a quotient unitary process admits an exact stationary state action on its declared domain |
| **[PROGRAMME COMMITMENT]** | reading $\delta S=0$ as characterizing the solution set rather than producing it |
| **[OPEN CONSTRUCTION]** | whether physics is variational as a classification rather than a commitment; the multiplier problem for three or more degrees of freedom; grounds for the composition law, for locality, and for the specific Lagrangian |
| Outside this module | which symmetries an action has, and any conservation law |

Those neighboring claims belong to [[philosophy/symmetry-principle/inq|the invariance axiom]] and [[philosophy/noether-conservation/inq|the Noether synthesis]].
