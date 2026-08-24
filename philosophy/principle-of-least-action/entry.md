# The Variational Axiom

The first of the three principles this section treats as axioms. It asserts that a dynamical law has the type of a stationarity condition on a functional of whole histories rather than of a propagation rule for states. "Least" is historical shorthand: the condition is $\delta S=0$, and the history may be a minimum, maximum, or saddle. The assertion has content, since not every dynamics admits an action and the obstruction is exact. It is silent about symmetry and supplies no conservation law. Its partial ground is a composition law on histories, of which the action is the logarithm up to $-i\hbar$.

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

[[why-an-action-at-all]] reconstructs the form of the principle from a composition law: weights that multiply under concatenation in an *abelian* group have an additive logarithm, which under absolute continuity is an integral along the history, and stationarity then follows by stationary phase rather than by postulate. What the reconstruction delivers is circle-valued, so the real-valued $S$ the axiom posits needs a further lift. This inverts the order of grounding and leaves the composition law, locality, and the Lagrangian itself underived.

## Flavors

These share variational mathematics and do not all assert the same physical principle.

| Flavor | Object varied | Functional or weight | Meaning of the condition |
|---|---|---|---|
| [[classical-action\|Classical]] | particle or classical-field histories | $S=\int L\,\mathrm dt$ or $\int\mathcal L\,\mathrm d^dx$ | the realized history satisfies $\delta S=0$ |
| [[einstein-hilbert-action\|Einstein--Hilbert]] | spacetime metric, plus matter | $S_{\mathrm{EH}}+S_{\mathrm m}$ with boundary terms | metric stationarity yields Einstein's field equation |
| [[quantum-action\|Quantum]] | all histories, states, or mean fields | phase $e^{iS/\hbar}$, state action, or effective action $\Gamma$ | histories interfere; classical saddles and quantum-corrected stationarity arise in different limits |
| [[thermodynamic-equilibrium\|Thermodynamic]] | macrostates | $S_{\mathrm{th}}$ or a thermodynamic potential | equilibrium extrema, exact under stated constraints |
| [[kinetic-and-stochastic\|Kinetic and stochastic]] | instantaneous rates, or whole stochastic histories | dissipation functionals, Onsager--Machlup path weight, path entropy | least dissipation near equilibrium; most-probable path relative to a noise model |

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
| **[CONDITIONAL THEOREM]** | the action as the logarithm of a multiplicative composition law, given an abelian weight group, absolute continuity in the endpoints, and unimodularity — yielding a circle-valued action, with the lift to $\mathbb R$ a further hypothesis |
| **[PROGRAMME COMMITMENT]** | reading $\delta S=0$ as characterizing the solution set rather than producing it |
| **[OPEN CONSTRUCTION]** | whether physics is variational as a classification rather than a commitment; the multiplier problem for three or more degrees of freedom; grounds for the composition law, for locality, and for the specific Lagrangian |
| Outside this module | which symmetries an action has, and any conservation law — see [[philosophy/symmetry-principle/entry\|the invariance axiom]] and [[philosophy/noether-conservation/entry\|the Noether synthesis]] |
