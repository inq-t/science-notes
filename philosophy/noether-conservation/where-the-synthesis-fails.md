# Where the Synthesis Fails

Conservation is expensive. The theorem needs an action, a continuous group with finitely many parameters, invariance of that action locally, an invariant measure if the theory is quantized, and boundary control before a current becomes a number. Each requirement has a characteristic failure, and each failure is a way of possessing a symmetry and no conservation law.

## Register

**No action.** If the dynamics is not variational there is no decomposition to run the argument through and no theorem at all. Whether a given dynamics is variational is the multiplier problem of [[philosophy/principle-of-least-action/variational-is-a-restriction|variationality is a restriction]], settled in low dimension and open in general.

**Symmetry of the equations only.** No $K^\mu_k$ exists, so no current is produced. Kepler rescaling is the witness — see [[philosophy/symmetry-principle/invariance-of-what|invariance of what]].

**Discrete symmetry.** There is no infinitesimal generator and hence no current. What a discrete symmetry gives instead is a grading, a selection rule, or a topological sector — the third entry in the four-way classification of [[conservation-of-causal-charge/indiscernibility-and-the-noether-gap|Indiscernibility and the Noether Gap]].

**One-sided semigroup.** The obstruction is not the absence of a generator — a strongly continuous one-parameter semigroup has one — but that non-invertible maps need not carry the solution set onto itself, so its elements are not symmetries in the sense the theorem requires. Where a differentiable generator does exist and satisfies the divergence condition the construction applies to it; otherwise the semigroup encodes irreversible accessibility or record preservation without yielding a current — the fourth entry of that classification, and a live candidate in this programme.

**Gauge symmetry.** The first theorem returns currents that are trivial on shell; the real output is the Noether identities of [[second-theorem-and-gauge]], with physical charges at boundaries.

**No time-translation symmetry of the action.** The criterion is not whether $\mathcal L$ displays $t$ but whether $\partial\mathcal L/\partial t$ is a total derivative, which is to say whether time translation is a divergence symmetry. A Lagrangian can depend explicitly on $t$ and still conserve energy. For the damped oscillator it does not: there $\partial L/\partial t=\gamma L$ is not a total derivative, and no conserved energy exists although the system is perfectly variational.

**Non-invariant measure.** A symmetry of the classical action need not survive quantization. When the functional measure fails to be invariant the classical conservation law acquires an anomalous divergence, and the fifth row of [[philosophy/symmetry-principle/invariance-of-what|invariance of what]] is the hypothesis that was silently assumed.

**Boundary and fall-off failure.** A conserved current gives a conserved charge only with control of the flux. In infinite volume the integral may diverge — the standard case being spontaneous symmetry breaking, where the current remains conserved and the charge does not exist, noted in [[philosophy/symmetry-principle/law-symmetry-and-state-symmetry|law symmetry and state symmetry]]. In a bounded region the flux-inclusive form of [[conservation-of-causal-charge/diagonal-charge-balance|Diagonal Charge Balance]] is the only complete statement.

**Degeneracy.** For systems failing normality the converse correspondence breaks, so a conservation law no longer certifies a variational symmetry. The forward direction survives: a variational symmetry still yields a current. For the *gauge* symmetries that current is trivial on shell, while the system's non-gauge variational symmetries — spacetime translations in Maxwell theory, for instance — still yield nontrivial ones.

## What this costs the programme

Nearly every item is live in the setting this project works in. A cosmological spacetime has no timelike Killing vector, gravity is a gauge theory whose charges live at boundaries, the causal-scale sector's candidate symmetries include a discrete reflection and a one-sided semigroup, and the wall construction has not yet supplied an action. Under those conditions the correct default is that there is no conservation law until each line above has been answered.

That is the conclusion [[conservation-of-causal-charge/theorem-programme|the causal-charge theorem programme]] reaches from the other side, and why construction axiom CA7 in [[program-core/axioms-and-principles|the axiom and principle ledger]] demands the whole list at once rather than a symmetry alone.

$$
\boxed{
\text{a symmetry is evidence of a conservation law only after the action, the parameter count, the measure, and the boundary have been named}.
}
$$

The synthesis remains the strongest instance in physics of a structure derived rather than posited: given the two axioms in their exact forms, conservation is a theorem, and by the converse of [[variational-versus-dynamical-symmetry]] it is the only source of conservation in a normal, totally nondegenerate variational theory. The expense catalogued here is the price of that strength. A principle yielding conservation laws under weaker hypotheses would yield them where they do not hold.
