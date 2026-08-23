# Principle of Least Action

The principle of least action says that a physical history makes an **action** functional stationary among nearby admissible histories. “Least” is historical shorthand: the history may be a minimum, maximum, or saddle, so **principle of stationary action** is the more accurate name.

The principle is less a claim that nature performs an optimization than a compact way of encoding dynamics. Once an action, its variables, its admissible histories, and its boundary conditions have been specified, the stationarity condition produces local equations of motion. The same framework makes symmetries and conservation laws transparent, extends naturally from particles to fields and spacetime geometry, and supplies the phase that organizes quantum amplitudes.

> [!important] The word “least”
> In most fundamental applications the mathematical condition is
> $$
> \delta S=0,
> $$
> not “$S$ is globally smallest.” Determining whether a stationary history is a minimum requires a separate second-variation analysis.

## The basic construction

Let a system be described by generalized coordinates $q^i(t)$. A **history** is an entire curve $q^i(t)$ between prescribed endpoints, not merely the system's state at one instant. A functional assigns a number to each history:

$$
S[q]=\int_{t_1}^{t_2}L(q,\dot q,t)\,\mathrm dt.
$$

Here $L$ is the Lagrangian and $S$ is the action. Compare the candidate history with nearby histories

$$
q^i_\varepsilon(t)=q^i(t)+\varepsilon\eta^i(t),
\qquad
\eta^i(t_1)=\eta^i(t_2)=0.
$$

The first variation measures the action's linear response to $\varepsilon$. With fixed endpoints, integration by parts turns $\delta S=0$ into the Euler--Lagrange equations

$$
\frac{\mathrm d}{\mathrm dt}\frac{\partial L}{\partial\dot q^i}
-\frac{\partial L}{\partial q^i}=0.
$$

Thus a statement about a whole history becomes a differential equation that can be evolved locally from initial data. There is no need to interpret the variational form as the system looking ahead or knowing its destination.

## What must be specified

A variational principle is not defined by an extremum slogan alone. It requires all of the following:

| Ingredient | Question it answers |
|---|---|
| Variables | What is allowed to change: particle paths, fields, metrics, density matrices, fluxes? |
| Functional | What number is assigned to each candidate: action, entropy, free energy, effective action? |
| Domain | Which histories or configurations are admissible? |
| Constraints | What is held fixed, and which conservation laws are imposed? |
| Boundary data | Are endpoints, boundary values, momenta, or asymptotic states fixed? |
| Extremality condition | Is the first variation zero, or is a genuine minimum/maximum required? |
| Interpretation | Is the extremum an equation of motion, an equilibrium condition, a saddle approximation, or a probability statement? |

Changing any one of these can change the physical content. In particular, “maximize entropy” at fixed energy and “minimize free energy” at fixed temperature describe the same equilibrium physics in different environments, whereas maximizing entropy with no stated constraints is not a usable principle.

## Why the action formulation is powerful

### One object encodes many equations

A field theory with many coupled components can often be specified by one action. Varying each field gives its equation of motion, while boundary terms reveal what data must be fixed and may carry physical charges.

### Symmetry becomes structural

Continuous transformations that leave the action invariant generate conserved currents through Noether's theorem. Time translation gives energy conservation, spatial translation gives momentum conservation, rotation gives angular momentum conservation, and gauge or diffeomorphism invariance generates identities and constraints.

### Coordinates become secondary

An action can be written from geometric scalars, making covariance manifest. This is central in relativity, where the dynamical variable is the spacetime metric itself.

### Classical and quantum descriptions meet

In quantum mechanics a history contributes a phase $e^{iS/\hbar}$. When $S$ changes rapidly compared with $\hbar$, neighboring nonstationary histories tend to cancel by destructive interference, leaving stationary histories as the centers of semiclassical contributions. Classical mechanics is therefore related to a stationary-phase limit, not to quantum particles literally selecting one minimum-action path.

## Domain-specific meanings

These uses share variational mathematics but do not all assert the same physical principle.

| Flavor | Object varied | Functional or weight | Meaning of the condition |
|---|---|---|---|
| [[classical-action|Classical action]] | Particle or classical-field histories | $S=\int L\,dt$ or $S=\int\mathcal L\,d^dx$ | The realized classical history satisfies $\delta S=0$ |
| [[einstein-hilbert-action|Einstein--Hilbert action]] | Spacetime metric, plus matter fields | $S_{\mathrm{EH}}+S_{\mathrm m}$ with necessary boundary terms | Metric stationarity yields Einstein's field equation |
| [[quantum-action|Quantum action]] | All histories, quantum states, or mean fields depending on formulation | Phase $e^{iS/\hbar}$, state action, or effective action $\Gamma$ | Histories interfere; classical saddles and quantum-corrected stationarity arise in different limits |
| [[thermodynamic-entropy|Thermodynamic and entropic principles]] | Macrostates, fluxes, or stochastic histories | $S_{\mathrm{th}}$, thermodynamic potentials, dissipation functionals, or path entropy | Equilibrium extrema are exact under stated constraints; dynamical principles require additional, regime-specific assumptions |

## The limits of the analogy

The shared variational pattern is not by itself a derived physical equivalence. Writing an entropy, Euclidean action, or information measure as an extremized functional does not identify it with mechanical action. Such an identification requires an explicit map between variables, constraints, dynamics, dimensions, measures, and limiting regimes. Variational principles are unified securely at the level of mathematical architecture; their physical meanings remain domain-dependent.

## Compact glossary

- **Action:** a functional of an entire history, conventionally with dimensions of energy times time.
- **Functional:** a map from a function, field, curve, or history to a number.
- **Variation:** an infinitesimal comparison of a candidate with nearby admissible candidates.
- **Stationary point:** a configuration whose first variation vanishes.
- **Extremum:** a local or global minimum or maximum; every differentiable interior extremum is stationary, but not every stationary point is an extremum.
- **On shell:** evaluated on a history satisfying the equations of motion.
- **Off shell:** evaluated on an admissible history that need not satisfy the equations of motion.
- **Boundary term:** a contribution supported at the boundary; it may leave bulk equations unchanged while changing the admissible boundary-value problem and physical charges.
