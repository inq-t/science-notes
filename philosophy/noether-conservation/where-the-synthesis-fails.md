# Where the Synthesis Fails

Conservation is expensive. The theorem needs an action, a continuous group, invariance at the level of that action, finitely many parameters, an invariant measure if the theory is quantized, and boundary control before a current becomes a number. Each requirement has a characteristic failure, and each failure is a way of possessing a symmetry and no conservation law. The register below is the checklist any proposed conservation law in this project must survive.

## Register

**No action.** If the dynamics is not variational there is no decomposition to run the argument through and no theorem at all. Whether a given dynamics is variational is the multiplier problem of [[philosophy/principle-of-least-action/variational-is-a-restriction|variationality is a restriction]], settled in low dimension and open in general.

**Symmetry of the equations only.** No $K^\mu$ exists, so no current is produced. Kepler rescaling is the witness: it maps solutions to solutions and rescales the action.

**Discrete symmetry.** There is no infinitesimal generator and hence no current. What a discrete symmetry gives instead is a grading, a selection rule, or a topological sector — the third entry in the four-way classification of [[conservation-of-causal-charge/indiscernibility-and-the-noether-gap|Indiscernibility and the Noether Gap]].

**Gauge symmetry.** The first theorem returns identically conserved trivialities; the real output is the Noether identities of [[second-theorem-and-gauge]], with physical charges at boundaries.

**Explicit time dependence.** A Lagrangian depending explicitly on $t$ has no time-translation symmetry and no conserved energy. The damped oscillator is the clean case, and it is variational, so the failure is squarely the second axiom's and not the first's.

**Non-invariant measure.** A symmetry of the classical action need not survive quantization. When the functional measure fails to be invariant the classical conservation law acquires an anomalous divergence, and the fifth row of [[philosophy/symmetry-principle/invariance-of-what|invariance of what]] is the hypothesis that was silently assumed. [[philosophy/principle-of-least-action/quantum-action|Quantum Action]] records that this is one of several ways two classically equivalent actions can differ quantum mechanically.

**Boundary and fall-off failure.** A conserved current gives a conserved charge only with control of the flux. In infinite volume the integral may diverge — the standard case being spontaneous symmetry breaking, where the current remains conserved and the charge does not exist, noted in [[philosophy/symmetry-principle/law-symmetry-and-state-symmetry|law symmetry and state symmetry]]. In a bounded region the flux-inclusive form of [[conservation-of-causal-charge/diagonal-charge-balance|Diagonal Charge Balance]] is the only correct statement.

**Degeneracy.** For systems failing the normality condition the converse correspondence breaks, so the absence of an obvious symmetry no longer implies the absence of a conservation law, nor the reverse.

## What this costs the programme

The register is not a list of curiosities. Nearly every item is live in the setting this project actually works in. A cosmological spacetime has no timelike Killing vector, gravity is a gauge theory whose charges live at boundaries, the causal-scale sector's candidate symmetries include a discrete reflection and a one-sided semigroup, and the wall construction has not yet supplied an action. Under those conditions the correct default is that there is no conservation law until each line above has been answered.

That is the same conclusion [[conservation-of-causal-charge/theorem-programme|the causal-charge theorem programme]] reaches from the other side, and it is why the programme's construction axiom CA7 in [[program-core/axioms-and-principles|the axiom and principle ledger]] demands the whole list at once rather than a symmetry alone. The present module supplies its general form:

$$
\boxed{
\text{a symmetry is evidence of a conservation law only after the action, the arity, the measure, and the boundary have been named}.
}
$$

## The positive residue

Stated as a negative register this can read as discouragement, which would be the wrong lesson. The synthesis remains the strongest instance in physics of a structure being *derived* rather than posited: given the two axioms in their exact forms, conservation is not an additional assumption but a theorem, and by the converse of [[variational-versus-dynamical-symmetry]] it is the *only* source of conservation in a regular variational theory. The expense catalogued here is the price of that strength. A principle that yielded conservation laws under weaker hypotheses would yield them where they do not hold.
