# Descent Instead of Diffusion

The theory's stochasticity cannot be removed: complete positivity together with a genuine classical-quantum split forces the metric to diffuse and the matter to decohere. But what the probability measure *means* is not fixed by that mathematics, and the theory itself supplies the fact that makes a second reading available. At saturation of the decoherence--diffusion trade-off the quantum state remains pure conditioned on the classical trajectory. The mixedness of the unconditioned state is then marginalisation over a fact the observer does not possess, not destruction of information. That is the reading this project wants, it is an interpretation of the same measure rather than a weaker theory, and turning it into a descent in the technical sense remains a construction.

## What cannot be given up, and what can

The objection that gravity "being stochastic" is the wrong picture cannot be met by weakening the mathematics. Diffusion is not an assumption bolted onto the postquantum theory; it is forced. Given that classical and quantum degrees of freedom both persist and that the dynamics preserves the hybrid state space, the evolution must be completely positive, and complete positivity buys the classical sector's noise with the quantum sector's coherence at a fixed exchange rate. Any theory that keeps spacetime classical pays it.

What is not forced is the reading of the measure. The mathematics fixes a probability law over histories. It does not say whether that law is nature's own indeterminacy or the shape of a ground whose determination is inaccessible.

## The fact the theory supplies

From [[vendor/postquantum-gravity/cq-construction]]: when the trade-off is saturated,

$$
\text{trade-off saturated}
\qquad\Longrightarrow\qquad
\boxed{\ \hat\sigma(z,t)\ \text{is pure, for each classical history }z.\ }
$$

The published paper proves this by the factorisation of the $\phi^\pm$ integrals and notes that it was independently established by master-equation methods. Its own framing of CQ dynamics in general is that the quantum state decoheres while purity is preserved on the quantum system, so that **"there is no loss of quantum information"** — qualified there as holding "under certain natural conditions" and credited to prior work, so the phrase should be carried with its qualifier rather than read as a theorem about the saturated case.

Nothing is lost *along* a history. The unconditioned state

$$
\varrho(t)=\int dz\;p(z,t)\,\hat\sigma(z,t)
$$

is mixed only because it averages over which history obtains. The information that appears destroyed is the answer to *which one* — and that is a fact, not a fluid. Read this way the theory does not violate unitarity so much as decline to condition on something no observer has.

Two consequences follow that are not available to a generic collapse model. Local CQ dynamics cannot generate entanglement — acting on a product state it returns a separable one, so the classical field can carry ordinary correlation but not entanglement, by the standard argument that local operations with classical communication cannot entangle. Calling the classical sector a **record** rather than a channel is this module's gloss, not the sources' language, and it is offered as a reading of that theorem rather than as its content. And the decoherence is derived rather than postulated: there is no external collapse mechanism, and classicalisation is mediated by spacetime itself.

## Why this is the project's sufficing reason

The correspondence with [[sufficient-reason/inq|Sufficing and Necessitating Reason]] is not an analogy. That module distinguishes a necessitating reason, which terminates in a character — a point of a spectrum — from a sufficing reason, which terminates in a measure on that spectrum. Here:

| Vendor object | Project type |
|---|---|
| a classical history $z$ | a **character**: a point of a classical configuration space is a character of its commutative algebra of functions |
| the Onsager--Machlup weight over histories | a **measure** on that spectrum |
| conditional purity given $z$ | determinateness *given* the pointing |
| the mixed unconditioned state | what remains when the pointing is not available |

The signature is visible in the coefficient itself. An amplitude carries $e^{iS/\hbar}$ and determines a history; a probability weight carries $e^{-\mathcal I/2D_2}$ and determines only a law over histories. The switch from imaginary to real is, in this project's vocabulary, the switch from a necessitating to a sufficing ground — and it is the same switch that removes the ghost in [[vendor/postquantum-gravity/no-ghosts-and-real-couplings]]. One change of coefficient does both jobs, which is the strongest structural hint the vendor offers.

The programme already holds this position for its own sector, in [[causal-wall-spectral-theory/whole-state-correlation-reading|the whole-state correlation reading]]. The vendor is the first place it meets a fully worked covariant theory.

## Information destroyed, or never accessible: the precise question

Every completely positive trace-preserving map admits a Stinespring dilation, so "information destroyed" and "information moved beyond access" are never distinguished by the channel alone. What distinguishes them is what plays the part of the environment.

- If the dilating environment is a quantum system entangled with the metric, then the metric is not classical, and the theory is a different one.
- If the dilating sector is the classical trajectory itself, the reading holds — and conditional purity says it does, at saturation.

That is why this vendor matters to the project more than a generic open-system model would. It exhibits a dilation whose environment is a *fact* rather than a quantum system, which is the closest current physics comes to the claim that the inaccessible reason is inaccessible in principle rather than merely unmeasured.

The caveat must travel with the claim. Conditional purity is established at saturation for the fundamental dynamics — proved in the published paper and independently in the trajectories literature. Whether it survives integrating out mediating gravitational modes is not settled here, and [[vendor/postquantum-gravity/stochastic-modes]] leaves related questions open about constraints at higher order and non-Markovianity. If it fails there, the descent reading fails with it, and that is the single most important thing to check before building on this.

## Residue and cost

An Onsager--Machlup action is an equation of motion squared. It is therefore literally a cost functional: it measures the price of deviating from the deterministic law, and assigns exponentially less weight the higher the price. In gravity that cost is carried by the curvature-squared sector,

$$
\mathcal I[g]\;\propto\;-\int d^4x\sqrt{-g}\,
\bigl(R^{\mu\nu}R_{\mu\nu}-\beta R^2\bigr),
$$

so within this vendor,

$$
\boxed{\text{the higher-curvature sector }is\text{ the cost of deviating from Einstein's equations.}}
$$

That is a concrete candidate for the functional form of what this project calls the residue of a descent. It also converts a slogan into a theorem target: **derive an equation-of-motion-squared weight from a descent, rather than postulating it.** If the programme's descent produces a cost functional of that shape, the two frameworks are computing the same object; if it produces something else, the analogy was verbal.

## What "descent" would still have to add

A conditional probability is not a descent. The programme's own machinery in [[program-core/physical-quotient|the physical quotient]] and [[basic-concepts/descent/inq|descent]] requires more than a measure over global histories:

1. **Contexts.** A cover — causal cuts, commutative readout contexts, or scale-indexed algebras — over which local data live. The vendor has one global path integral, not a site.
2. **Transport.** Comparison maps between contexts. The vendor's classical trajectory is a global object; nothing yet plays the role of a cocycle.
3. **Effectivity.** A statement that coherent local data descend to one global object, and an obstruction class when they do not.
4. **Derivation of the cost.** The $(\text{EOM})^2$ weight must come *out* of the descent rather than being imported alongside it.

Until these exist, the correct description is that the vendor supplies a physically realised instance of the *interpretive* move — measure rather than amplitude, record rather than channel, conditional purity rather than destruction — and does not yet supply the *mathematical* structure the programme means by a descent across a stack.

## Two things the reframing must not do

**It must not remove empirical content.** The diffusion is predicted, and it is bounded from both sides by the experiments in [[vendor/postquantum-gravity/empirical-status|empirical status]]. A descent reading that predicted no noise would not be a reinterpretation but a different and already-constrained theory. The reframing changes the ground of the measure, not the measure.

**It must not smuggle determinism back in.** Conditional purity says that *given* the trajectory nothing further is lost. It does not supply a reason for the trajectory. Supplying that reason is the actuality problem, and it remains exactly as open here as in [[sufficient-reason/necessity-and-nonemptiness|Necessity, Nonemptiness, and Realizability]]: the availability of a pointing is not the realisation of one.
