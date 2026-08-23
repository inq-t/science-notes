# The Theorem Programme

The proposal becomes a theory only if it constructs a natural coalgebra of contextual readout, proves that coalgebraic and operational identity coincide, and connects repeated observation to a physically instantiated one-sided algebraic action. Each target below has an explicit failure condition so that a suggestive analogy cannot masquerade as a result.

## Construct the observation coalgebra

**Target C1 — behavior functor.** Define a category of wall or observer systems and an endofunctor $F$ for which a coalgebra $\gamma:X\to F(X)$ encodes the selection of a commutative context and the induced probability law on its spectrum. Variance under context inclusion, the contravariance of spectrum, and state update must all type-check.

Abramsky's coalgebraic and Chu-space representations of physical systems and probabilistic coalgebra are natural starting points. The physical object should be compatible with the algebra-and-state package demanded by [[causal-wall-spectral-theory/causal-scale-interface|the causal-scale interface]].

**Failure K1.** No such $F$ is natural under the admissible maps of observer systems while reproducing quantum probabilities. Then the coalgebraic language is at the wrong level.

## Prove nonemptiness

**Target C2 — terminal behavior.** Construct the terminal sequence for $F$ and prove that its limit exists and is nonempty, perhaps through compact-Hausdorff preservation.

**Failure K2.** The terminal sequence has an empty limit or fails to converge in the required category. Then the fixed-point argument supplies no necessity of behavior.

## Identify physical sameness

**Target C3 — operational bisimulation.** Prove

$$
\sim_{\mathrm{bisim}};=\;\sim_{\mathrm{operational}}
$$

for the physically allowed observations. Probabilistic bisimulation gives a classical template, not the quantum result.

**Failure K3.** Bisimilar states are physically distinguishable, or operationally indistinguishable states fail to be bisimilar. Then coinduction gives the wrong identity criterion.

## Build the semigroup bridge

**Target C4 — one-sided dynamics.** Relate iterated coalgebraic observation to a half-sided modular inclusion or an $E_0$-semigroup on the identified observable algebra. Specify the parameter, the accessible subalgebra, and the record-forming operation.

**Failure K4.** No natural bridge exists. Then the coalgebraic and operator-algebraic accounts are two analogies rather than one structure.

## Globalize orientation

**Target C5 — compatible arrows.** Treat local orientations as local data and prove that they glue to a coherent global orientation across interacting walls or observers.

**Failure K5.** The orientation cocycle is obstructed or permits incompatible arrows with no account of shared records. Then the proposal yields local arrows but no common past.

## Resolve normality and actuality

**Target C6 — physical outcomes.** Determine whether readout facts can be represented by normal or otherwise operationally realizable states, or construct a precise theory in which singular characters can nevertheless be outcomes of normal-state processes.

**Failure K6.** Characters remain algebraically existent but physically unrealizable, with no limiting or instrument-based account of their occurrence. Then the necessity claim concerns only formal points.

## Framework-wide stress tests

The construction must also survive four independent tests:

- A noncircular derivation of outcome probability and the Born rule from reversible dynamics alone would weaken the need for a second species of reason.
- A local noncontextual hidden-variable completion reproducing quantum predictions would overturn the no-go basis of the distinction. Existing Bell and Kochen--Specker results exclude the usual target packages of assumptions.
- The dimension-two exception to projection-valued Gleason must be handled explicitly, either as a domain restriction or through a justified generalized measurement theorem.
- If decoherence plus a complete outcome theory exhausts both context and fact selection, the present account must show what additional explanatory work its two-reason vocabulary performs.

Local Friendliness results add a fifth stress test for relative-fact versions: the abandoned assumption and the resulting cross-observer consistency law must be explicit.

## Dependency order

C1 is logically prior to C2 and C3. C4 depends on a repeated-observation structure from C1. C5 depends on local orientations supplied by C4. C6 is partly independent: even a perfect behavioral and temporal construction does not by itself turn a measure into an actual point.
