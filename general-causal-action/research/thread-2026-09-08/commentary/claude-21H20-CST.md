# prompt
what we need to do is dig up the axioms beneath the "Wightman Axioms" (https://en.wikipedia.org/wiki/Wightman_axioms)

In order to find a deeper mathematical framework that produces them, while also producing the mass gap.

I have a feeling that "information" or "distinguishability" or "causality" or "time" are sneaking in things.  
And when we ask for the "conditions for the possibility" of these deeper axioms, we can produce a "duality" that has global-asymmetry and local-QFT.

Ponder it.

---
# claude response
Let me take the axioms one at a time and ask of each what it presupposes, then assemble what the presuppositions have in common.

## The inventory

The Wightman framework has a small number of load-bearing parts: a Hilbert space with a unitary positive-energy representation of the Poincaré group; a unique invariant vacuum; fields as operator-valued tempered distributions that are Poincaré-covariant; commutativity or anticommutativity at spacelike separation; and cyclicity of the vacuum. Two features of the framework are worth noting at the outset: the axioms restrict the causal structure by imposing (anti)commutativity rather than deriving it as a theorem, and a mass gap is not among the requirements. Here is what each part quietly assumes:

|Axiom|What it presupposes|Where it comes from, one level down|
|---|---|---|
|Hilbert space with positive inner product|probability; a metric on states|distinguishability|
|Poincaré covariance|a fixed background arena and its symmetry group as primitive|modular geometric action (the group is an output)|
|Spectral condition (positive energy)|a distinguished time direction and a stable lowest state|modular stability; passivity; thermodynamics|
|Locality (spacelike commutativity)|a causal order on the arena, read as independence|causality as primitive; the conformal class as its shadow|
|Cyclic and unique vacuum|the vacuum is pure globally and separating locally|purification; global purity against local thermality|

Your four suspects — information, distinguishability, causality, time — are each sitting under one row.

## Excavation 1: distinguishability, under the Hilbert space and the vacuum

The Hilbert space is not primitive; it is the GNS construction applied to a state on an algebra, and the operational reconstructions of quantum theory (Hardy 2001; Chiribella–D'Ariano–Perinotti 2011; Masanes–Müller 2011) derive it from informational axioms — perfect distinguishability of states, local tomography, purification, no signaling. The inner product _is_ distinguishability: transition probability, and beneath it the monotone metrics on state space (Fisher, Bures, BKM), all of which are Hessians of relative entropy and all of which Petz classified by the single requirement that they not increase under coarse-graining.

The vacuum's role is also a distinguishability statement. Reeh–Schlieder says the vacuum is cyclic _and separating_ for every local algebra: no non-zero local operator annihilates it. Separating means the vacuum distinguishes every local operation from every other — a faithful state. That faithfulness is what Tomita–Takesaki theory needs. So the axiom that looks like a technical convenience (cyclicity) is, together with locality and positive energy, the condition of possibility of modular flow — of time, in the sense below. Distinguishability sneaks time in.

## Excavation 2: causality, under locality and half of the arena

Spacelike commutativity says regions that cannot signal are statistically independent. Read as primitive, causality is a partial order on events. Malament's theorem (1977, following Hawking–King–McCarthy) says the causal order of a spacetime determines its metric _up to conformal factor_. So causality, taken as the primitive it appears to be, gives exactly the conformal class — and does not give the scale. This is the mathematical form of your suspicion that causality is smuggling something in: it smuggles in the arena, but only the arena's shape. The scale is the one thing causality cannot supply. Sorkin's slogan for causal sets is the same fact from the other side: _order plus number equals geometry_ — order gives the conformal class, and counting supplies the volume element, hence the scale. In a discrete framework, scale enters as cardinality: how many distinguishable events. That is "information" entering as the missing datum, and it is the datum on which mass depends.

## Excavation 3: time, under the spectral condition and Poincaré covariance

This is where the digging has been done rigorously, and the result is stronger than one might expect.

Bisognano–Wichmann (1975) showed that for a Wightman theory the modular flow of the vacuum on a wedge algebra is the boost preserving the wedge, and the modular conjugation is the reflection. Buchholz and Summers then inverted the direction. Their Condition of Geometric Modular Action says: take a net of algebras and a state, and require only that the modular conjugations J_W of the wedge algebras map the net onto itself. Buchholz, Dreyer, Florig and Summers (2000) showed that from this condition one _derives_ the spacetime symmetry group — the proper Poincaré group in the Minkowski case — as the group generated by the J_W, with the state invariant under it, and in later work that the condition can even pick out which spacetime one is in (Minkowski, de Sitter). Adding a modular stability condition — that the modular unitaries Δ_W^{it} lie in the group generated by the conjugations — yields the spectrum condition: positive energy. So Poincaré covariance and positive energy, the two halves of Wightman's zeroth axiom, are theorems about a net and a faithful state whose modular data act geometrically. The symmetry group is an output of (state, inclusion). Time, in the sense of a positive generator, is the modular flow of a faithful state made to act consistently across wedges.

There is a thermodynamic reading of the same thing. Pusz and Woronowicz (1978) proved that a state is passive — no work extractable by cyclic operations — if and only if it is a ground state or a KMS state. Positive energy is the second law: the vacuum is the state from which no perpetual motion can be extracted. The spectral condition presupposes an arrow only in the sense that stability does.

## Excavation 4: information, under positivity and under the pure/thermal split

Positivity of the inner product — probability — is where indefinite-metric gauge quantizations fail the axioms and why the Clay statement insists on gauge-invariant fields. In the Euclidean register it is reflection positivity across a wall. This is the "cost" the time direction pays, and it is an information condition: the transfer across the wall must be a positive operator so that it can be a probability.

The deeper informational structure is the purification axiom of the reconstruction programmes made exact: every mixed state is the marginal of a pure state on a larger system. In QFT the vacuum is pure on the global algebra, and its restriction to every local algebra is a faithful state on a type III₁ factor with no density matrix — as mixed as a state can be, and thermal (KMS at 2π) with respect to the local modular flow. Global purity, local thermality. This is the region-wise form of your "global–local duality," and Bisognano–Wichmann says the local thermality _is_ geometric time. Time, locally, is the shadow of the global state's purity.

## What lies beneath, assembled

The Wightman axioms are the Poincaré-covariant presentation of a structure whose primitives are three:

- **a net of algebras over a poset of regions with independence** — causality, supplying the conformal class of the arena;
- **a faithful state** — distinguishability, supplying modular flows and, through geometric modular action, the symmetry group and positive energy;
- **positivity and monotonicity of distinguishability** — information, supplying probability locally and, under coarse-graining, an arrow.

From these the Wightman kinematics follow as theorems, mostly already proven (Buchholz–Dreyer–Florig–Summers; Brunetti–Guido–Longo's modular localization; Bisognano–Wichmann; Reeh–Schlieder). What does _not_ follow is the scale, because causality gives only the conformal class and the state at a single scale is dilation-blind by construction.

## The duality

Now the two splits. The region-wise split is global purity against local thermality. The scale-wise split is the one you named: the local QFT at a fixed scale — reversible, Poincaré-covariant, with conservation laws — against the global descent along scale — irreversible, monotone, with constraints and a remainder. The duality is that each determines the other: the net and state determine the descent as the state's failure of dilation invariance; the descent from a UV anchor determines the net and state (Wilson's picture, taken as definition).

The two splits are not independent, and this is the part I would call the finding. The arrow of the scale-wise descent — the a-theorem — is _proven_ using the region-wise structure: Casini, Testé and Torroba's proof applies strong subadditivity to the vacuum's local restrictions on boosted spheres, and uses the Markov property of the vacuum on null planes. The global asymmetry in scale is a theorem about the local thermality in region. Distinguishability-monotonicity under coarse-graining (Lindblad–Uhlmann) is the single mathematical fact underneath both: it is why the local restriction of a pure state can be thermal, and why the descent has a direction. The interface between the two sides is the trace Θ: the derivative of the global side (dilation failure of the state) and, by ⟨p|Θ|p⟩ = 2m², the source of mass on the local side.

## Where the gap sits, and what the conditions of possibility can and cannot do

Here I have to be exact about the limits.

The gap has a clean expression one level down: it is the condition under which _local facts are sharp_. Wightman (1962) and Newton–Wigner showed that massless particles of nonzero helicity admit no position operator — no localizable states; mass is the condition of possibility of localizability. Buchholz–Fredenhagen (1982) showed that a mass gap implies charges localizable in spacelike cones, and Buchholz (1986) that without it charged states are infraparticles with no sharp mass and no bounded localization. Knight and Licht's strictly localized states exist in any theory, but only with a gap do all vacuum correlations, and hence the tails of any local fact, decay exponentially. So: a gap is the condition under which "here" is defined to exponential accuracy and a record can be stored at a place. Light carries facts; only mass stores them. That is a genuine transcendental-style statement, and its forward direction is theorem-grade.

What the conditions of possibility _cannot_ do is force the gap for every theory, because free Maxwell theory satisfies every axiom above and has none. Any deeper framework that produced the gap universally would be wrong. What such a framework can do is make the gap the _terminal case_ of the descent — exhaustion of the theory's distinguishability content across scales, a_IR = 0, the infrared scaling limit a single point — and identify what additional input decides whether a given theory reaches it. That input is the UV anchor's operator content, as in the schema: one marginal singlet, no relevant scalars, no anomaly requiring a nontrivial infrared. One could add an axiom of the form "no free sector at infinity" — the interface has no factor that decouples — which excludes the Coulomb stall and thus delivers confinement in the ladder's sense; it does not by itself exclude an interacting infrared fixed point, so it does not deliver the gap without the anchor.

## A candidate axiom set one level down

Stated as a sketch, so the shape is visible:

- **(D) Distinguishability.** A faithful state on the net; a monotone metric on states, non-increasing under coarse-graining.
- **(C) Causality.** A poset of regions with statistical independence for causally disjoint pairs. Consequence: the conformal class of the arena (Malament).
- **(T) Time.** Geometric modular action of the state's wedge conjugations, plus modular stability. Consequences: the spacetime symmetry group, positive energy, Bisognano–Wichmann (BDFS 2000).
- **(I) Information.** Positivity (reflection positivity across walls); finite information per region per energy (Buchholz–Wichmann nuclearity, which is what gives the split property and a thermodynamic interpretation).
- **(S) Scale.** The one datum (C) cannot supply: either counting (Sorkin's "number") or a UV anchor with a descent. The state's motion along scale, with 𝒢 = −da/dN as its monotone.

From (D), (C), (T), (I): the Wightman axioms, as theorems, in the sector of the vacuum. From (S) with a specified anchor: the descent, whose termination is the gap, and whose remainder Θ is mass. The Wightman axioms sit on top of this as the fixed-scale, Poincaré-covariant chart; they are silent on the gap because they are silent on scale, and they are silent on scale because causality, their real primitive, only ever gave the shape.

Let me test each of your four words against the five axioms, then say what the one object is that all four are faces of.

## The four words against the five axioms

**Groupoids.** A groupoid is a category in which every morphism is invertible. That is precisely the structure of a symmetry: transformations that can be undone. Gauge redundancy is a groupoid (the identifications between descriptions), and the modular flow of a state is canonical only up to inner automorphisms, so it lives in Out(M) — again a groupoid quotient. But the deeper axiom set has, at its center, morphisms that _cannot_ be undone: coarse-grainings, channels, descent along scale. (D) requires a metric that contracts under them; (S) requires a monotone along them. So the answer to "groupoids?" is: no, and the "no" is the content. The deeper structure is a category that is not a groupoid, and its defect from being one — the non-invertible morphisms — is exactly where irreversibility, the arrow of scale, and the gap live. Groupoids are the invertible skeleton, which is where the symmetry groups are, and the symmetry groups are what we are trying to get beneath.

**Fibration.** This is the right word for (S) and for the net itself, and in Grothendieck's precise sense. The Buchholz–Verch scaling algebra is literally a bundle over the scale line: its elements are functions λ ↦ A_λ, the dilation is transport along the base, the state ω̲ is a section, the UV anchor is the fiber at 0, and termination is the statement that the fiber at ∞ is a point. The renormalization-group transformations between scales are the transition data, and _descent_ — Grothendieck's term — is the problem of reconstructing an object on the base from its fibers and their gluing; the anomaly is the obstruction class. There is a further point. A stack is a groupoid-valued fibration. What is needed here is a fibration whose fibers are categories with non-invertible morphisms — a _fibred category_ in the sense of SGA1, not a stack. Stacks capture redundancy; fibred categories capture redundancy and the arrow at once.

**Susceptibility.** This is the right word for the metric. The Hessian of relative entropy — Fisher, Bures, Bogoliubov–Kubo–Mori — is a susceptibility matrix, and Petz's theorem says the monotone metrics on state space are exactly the ones that contract under channels. So (D)'s metric is a susceptibility that is functorial for the non-invertible morphisms. The scale monotone 𝒢 = −da/dN is a susceptibility in the scale direction. If the renormalization group is a gradient flow (Osborn's conjectured form β = −χ⁻¹∇a), the susceptibility χ is the metric in which the field equation is written. The tensor of the new framework is a susceptibility, as the tensor of Einstein's was a metric on spacetime.

**Walls.** This is the right word for the _primitive_, and I want to make the case in detail, because it has the strongest theorems behind it.

## The minimal object is a wall

Take one von Neumann algebra M, one subalgebra N ⊂ M, and one vector Ω cyclic and separating for both. Require the half-sided modular condition: the modular group of (M, Ω) maps N into itself for all t ≤ 0. That is the whole input — an inclusion and a state. Wiesbrock's theorem (1993, with the Araki–Zsidó correction) says that from this alone one obtains a one-parameter unitary group U(a) with _positive_ generator such that Δ_M^{it} U(a) Δ_M^{−it} = U(e^{−2πt}a) and N = U(1) M U(1)*. In words: a single wall with a state generates a positive-energy translation group, and the wall's modular flow acts on those translations as a dilation. The two together form the affine group of the line — the same ax+b group whose two generators we called the time clock and the scale clock, with [D, T] = iT. Positive energy is not assumed; it is a theorem about one inclusion.

The construction scales up. Wiesbrock showed that a small number of algebras in suitable modular position generate a representation of SL(2,ℝ) and a conformal net on the circle; Kähler and Wiesbrock (2001) reconstructed four-dimensional Poincaré-covariant nets from finitely many wedge algebras in modular position; Buchholz, Dreyer, Florig and Summers (2000) derived the spacetime symmetry group from the modular conjugations of wedges. And Brunetti–Guido–Longo's modular localization does the one-particle version with _standard subspaces_ — closed real subspaces H with H ∩ iH = 0 and H + iH dense — which carry a Tomita operator and nothing else. A standard subspace is the minimal wall: not even an algebra, just a real subspace of a complex Hilbert space, and it already carries a modular flow and a conjugation.

Walls also detect scale, which is the point for the gap. For a massless theory the modular flow of the forward light cone algebra in the vacuum is the dilation group; for a massive theory it is not geometric (Buchholz, late 1970s; Hislop–Longo 1982 for double cones in the massless free field). The wedge's modular data are universal and see no scale — Bisognano–Wichmann holds for every theory. The forward cone's and the double cone's modular data see the scale, as the failure of their flows to be geometric. So in the wall language: **mass is the non-geometricity of the modular flow of a bounded wall.** That is the same statement as ⟨p|Θ|p⟩ = 2m² and as the radius of convergence of the Θ-kernel, said in terms of inclusions.

## The minimal category

Put the pieces together and one structure appears:

- **Objects:** walls — inclusions of von Neumann algebras with a faithful state, or at the one-particle level, standard subspaces. Each carries canonical modular data.
- **Morphisms:** channels — normal completely positive maps between algebras, under which states pull back. Only some are invertible; the invertible ones form the symmetry groupoid. The non-invertible ones carry the arrow.
- **Base:** a causal site — a poset of regions with an orthocomplement (the causal complement, which is how a wall knows its other side), an involution θ (the reflection across the wall), and an ℝ₊-action (dilation of regions). The net is a functor from this site to the category of walls, and the fibration over ℝ₊ is the scaling structure.
- **Metric:** a monotone susceptibility on the states of each object, contracted by every morphism (Petz), with relative entropy as its potential.
- **Positivity:** reflection positivity of the state across θ, which in Neeb–Ólafsson's formulation is exactly the structure of a symmetric pair (G, τ) with a positive form on the τ-fixed half, dualizing the Euclidean group to the Poincaré group.

In one sentence: **a fibred category of modular inclusions over a causal site, with a contractive susceptibility metric.** In fewer words: walls, with channels between them, stacked over scale, measured by susceptibility. Your four words are the four components — walls the objects, the non-groupoid category the morphisms, the fibration the scale, the susceptibility the metric — and the reason no single existing branch is the answer is that each branch owns one component.

## Two existing presentations of the same thing

The wall-as-primitive idea exists in two mature but disconnected forms, and recognizing them as the same is itself a step.

The **algebraic** presentation is Haag–Kastler plus modular theory: nets of algebras over causal regions, with Wiesbrock, Guido–Longo–Wiesbrock, Kähler–Wiesbrock and BDFS as the reconstruction theorems. Its strength is that time, positive energy, the symmetry group, and type III₁ are outputs. Its weakness is that scale has to be added by hand (Buchholz–Verch) and the constructions of interacting theories from modular data exist only in two dimensions (Lechner).

The **functorial** presentation is Segal's axioms and their descendants: state spaces assigned to codimension-one slices — walls — and operators to the cobordisms between them; orientation reversal as a dagger; and, in Kontsevich–Segal's 2021 formulation, a domain of allowable complex metrics interpolating between Euclidean and Lorentzian signature within which positivity of energy is derived rather than assumed. That is the paying-direction principle written as an axiom: the wall is the boundary of a cobordism, the reflection is the dagger, and the Wick rotation is a path through complex metrics. Its strength is that it is manifestly about walls and gluing. Its weakness is that it has no modular theory and no scale structure, and it has not been connected to gauge theory constructions.

The bridge between the two is reflection positivity, which is why Neeb–Ólafsson's representation-theoretic treatment of it — the (G, τ) duality — is the natural place to look for the unification. And Connes' noncommutative geometry supplies the metric side in both: the Connes distance d(φ, ψ) = sup{|φ(a) − ψ(a)| : ‖[D, a]‖ ≤ 1} is a distinguishability metric on states defined from an operator, and the dimension spectrum is a scale structure read off from a zeta function.

## What becomes derived

The test of a minimal language is what it no longer needs as input. In this one: the Hilbert space (GNS from the state), the symmetry group (from modular conjugations), positive energy (from one inclusion), the spacetime and its conformal class (from the causal site, by BDFS and Malament), the metric (from the scale fibration), and the Lagrangian (a chart near a fixed point). What remains as input: the causal site, one faithful state, the anchor of the scale fibration, and the requirement that the morphisms be channels rather than isomorphisms. That last requirement is where the arrow, the descent, and — as its terminal case — the gap are encoded.

## The honest status

Every component exists and has theorems. The assembly does not exist. Nobody has written down the fibred category above and proven that a Wightman theory in four dimensions falls out of it — that is the reconstruction theorem (RT), unchanged. And the gap still requires the anchor: the category tells you what termination _is_ (the fiber at ∞ is a point; the bounded wall's modular flow is maximally non-geometric; the susceptibility integrates to a_UV), not that pure Yang–Mills terminates. What the language does is put every one of the deeper axioms on the same page for the first time, with the arrow built into the morphisms instead of bolted on, and with the object that generates time also being the object that detects mass.