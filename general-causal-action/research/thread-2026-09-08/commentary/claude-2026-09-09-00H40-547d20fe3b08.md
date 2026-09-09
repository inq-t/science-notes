check the "./wall-return-channel"

# Prompt

Work with this idea for turning the problem upside down.
In one sentence: **a fibred category of modular inclusions over a causal site, with a contractive susceptibility metric.** In fewer words: walls, with channels between them, stacked over scale, measured by susceptibility. Your four words are the four components — walls the objects, the non-groupoid category the morphisms, the fibration the scale, the susceptibility the metric — and the reason no single existing branch is the answer is that each branch owns one component.

Think deeply about how this construction can be used to turn the problem upside down.

Something like “stop trying to find a mass gap in gauge theory, but instead derive Yang Mills from a deeper ontological/mathematical asymmetry”.

And give a suggestive schema for the research program’s direction

---
# Response 1

The text is mostly right about the mathematics, wrong about one type, and wrong that the assembly does not exist, in a way that helps: two pieces of it exist under names the text does not use, and the third piece has a small theorem sitting in it that nobody has stated in this vocabulary. Let me check the claims, then build the object, then run the one computation that shows the mechanism.Sympy mangled the nested radical, so I finished the algebra by hand. Let me verify both closed forms numerically before I rely on them.Both closed forms check numerically, and the Takesaki criterion behaves exactly as predicted. Now the assessment and the assembly.

## Merits of the text

The mathematics it cites is right: Wiesbrock with the Araki–Zsidó repair, Guido–Longo–Wiesbrock, Kähler–Wiesbrock, BDFS, Brunetti–Guido–Longo's standard subspaces, Petz's classification of monotone metrics, Neeb–Ólafsson's representation-theoretic reflection positivity, Kontsevich–Segal. The diagnosis that groupoids are the invertible skeleton and that the content lives in the non-invertible morphisms is correct and is your own arrow criterion. Two things are mistyped and one is overstated. "A fibred category, not a stack" conflates stacks with stacks _in groupoids_; a fibred category in categories that satisfies descent is a stack in categories, and that is exactly what a net with isotony and gluing is, so the object wanted is a stack after all, just not a groupoid-valued one. "For a massive theory the modular flow is not geometric" is expected but not a theorem for double cones; what is known is that it cannot be the dilation, and Bostelmann–Cadamuro–Minz have numerics, not a proof. And the assembly-does-not-exist claim is false in a way that helps.

Three of the four components exist under names the text does not use. The "net as functor on a causal site" is Brunetti–Fredenhagen–Verch's locally covariant QFT (2003), a functor from a category of spacetimes to algebras, twenty years old. The "wall net at the one-particle level" is the Neeb–Morinelli–Ólafsson programme: nets of standard subspaces on causal symmetric spaces built from Euler elements, with the causal structure, modular flow and spectrum condition derived from Lie theory; your radical-copernicanism audit already cites it. And "susceptibility as a functor on the non-groupoid" has a theorem behind it that is stronger than Petz monotonicity: Baez, Fritz and Leinster (2011) proved that Shannon entropy is, up to scale, the _unique_ functor measuring information loss along measure-preserving maps of finite probability spaces, Baez–Fritz (2014) did the same for relative entropy, and Parzygnat extended both to the quantum case. Information loss along a non-invertible morphism is not a metaphor with a metric attached; it is a characterized functor. The text's "susceptibility" is that functor's Hessian.

What does not exist, and what I think is the actual object, is the fourth component: a canonical morphism _back_ across the wall and the invariant it carries. That is what I will build.

## The assembly

Take a wall to be a pointed inclusion (M, N, Ω): von Neumann algebras N ⊂ M with Ω cyclic and separating for both, state ω = ⟨Ω, · Ω⟩. Morphisms between walls are normal unital completely positive maps compatible with the inclusions and pulling the states back; the invertible ones form the symmetry groupoid. Over this sit four structures, three of them theorems.

The modular functor is Wiesbrock: on the half-sided subcategory, a wall returns a positive-energy representation of the ax+b group, with the modular flow of M acting as dilation on the translations. Time and positivity are outputs of one inclusion.

The return functor is the piece nobody has named in this setting, and it comes from two old theorems. Accardi and Cecchini (1982) showed that for any inclusion ι: N → M and faithful normal state ω there is a canonical normal unital completely positive map E_ω: M → N with ω_N ∘ E_ω = ω, the ω-dual of the inclusion; Petz later identified it as his recovery map. Compose it with the inclusion:

D := E_ω ∘ ι : N → N.

D is a unital, ω_N-preserving channel on the small algebra; it is what a distinction made inside the wall looks like after being carried out and canonically brought back. Takesaki's 1972 theorem says E_ω is a conditional expectation, equivalently D = id, if and only if σ^ω_t(N) = N for all t. So for every proper half-sided modular inclusion D ≠ id, and for the wall between a factor A and its environment, N = A ⊗ 1, D = id if and only if ω is a product state, since a ω-preserving conditional expectation onto A ⊗ 1 must have the form a ⊗ b ↦ a φ(b). The arrow, the non-invertibility of the wall's morphism, is a theorem about the state, not an axiom about the category. And D = id exactly when a reference measure is available: for a trace, or for a modularly aligned wall, there is no return defect. That is your §5 against Boltzmann made into one line.

The monotone is the relative-entropy loss across the wall, S_M(ω‖φ) − S_N(ω‖φ) ≥ 0, with equality if and only if Petz recovery is exact; your channel-loss-and-recovery module already owns this cocycle, and Petz's sufficiency theorem is its recovery fork. Its Hessian is a Petz monotone metric, contracted by every channel, and the contraction along the wall is governed by the spectral gap of D. So the susceptibility of the wall is the gap of its return channel.

The fibration is the scale family: for nested regions, the walls (𝔄(λO_r) ⊂ 𝔄(λO_R), Ω) over λ ∈ ℝ₊ with dilation as transport, and the return functor along it, λ ↦ D_λ. This is where Q* lands. In a conformal vacuum the dilations implement ω-preserving isomorphisms between the walls at different λ, so D_λ are all unitarily equivalent and the gap of D_λ is a function of r/R alone; the scale rate is zero. In a massive theory the gap depends on (r/R, mR), and the conjecture that gives Q* its object is that its behavior in λ at fixed r/R is the mass. I am not asserting the direction; I am asserting that this is a single number, intrinsic to the pointed inclusion, that quantifies the non-invariance of N under the modular flow of (M, Ω) _without knowing what that flow is_. That matters because the modular flow of a massive double cone is unknown and the return channel's gap does not need it.

## The receipts

Two walls small enough to compute exactly, to show the mechanism is real and not a name.

Take M = M₂(ℂ), N the diagonal algebra, and ω the state with density (I + r n·σ)/2 where n makes angle θ with the axis the diagonal algebra defines. Then D is a 2×2 stochastic matrix on functions of two points and its return-defect gap is

g(r, θ) = (1 − √(1 − r²)) sin²θ / (1 − r² cos²θ) = (1 − 2√det ρ) · sin²θ / (4 det ρ_N).

It vanishes when θ = 0, the wall aligned with the modular flow, and when r = 0, the tracial state; it tends to 1 for a pure state at θ = π/2, where D becomes projection onto constants and nothing is returned. The three factors are the state's distance from the trace, the misalignment of the wall with the state's eigenbasis, and the spread of the marginal. Sympy botched the nested radical; I did the algebra by hand and the formula matches the numerics to eight digits.

Take M = M₂ ⊗ M₂, N = M₂ ⊗ 1, and ω the isotropic state (1−p) I/4 + p|Φ⁺⟩⟨Φ⁺|. By SU(2) covariance D is depolarizing, and its gap is

q(p) = [1 + p − √((1 + 3p)(1 − p))] / 2,

zero at p = 0 (product state, Takesaki holds, no arrow), one at p = 1 (a pure entangled state; the return channel is the trace). Random correlated states give D ≠ id with ‖D − id‖ tracking the distance from the product state, and a product state gives ‖D − id‖ at machine zero.

These are finite and compact, and I will say what I said about the sewn overlaps: they prove the mechanism, not anything about Yang–Mills. Their value is that the same definition, unchanged, applies to (𝔄(O_r) ⊂ 𝔄(O_R), Ω) in a quantum field theory, where the only thing that changes is that the computation gets hard.

## Where this puts the four words

Wall: the pointed inclusion. Non-groupoid: D ≠ id, by Takesaki, whenever the state is not a trace and the wall is not aligned with its flow. Susceptibility: the gap of D, which is the contraction of the Petz metric across the wall and the Hessian of the relative-entropy loss cocycle. Fibration: λ ↦ D_λ over the scale line, with the conformal case as the control where the rate is zero. And the "one object" the text asked for is not the category, which is an assembly of BFV, Neeb–Morinelli–Ólafsson, and Baez–Fritz–Leinster. It is the return functor and its scale rate. That is the piece with no owner.

It also gives your metaphysics a precise carrier. What is "there but inaccessible" across a wall is exactly what D fails to return; the reason exists in M and its image in N is degraded by a canonical, state-determined channel whose deviation from the identity is measured by a single number. Descent into facthood, at linear order, is D.

## What to do next, and what not to claim

The next computation is well posed and I would do it before writing another word of philosophy about it: the return channel of a quasi-free state across an inclusion of CCR algebras. For Gaussian states the Petz recovery map is Gaussian (Lami–Das–Wilde 2018), so D is a Gaussian channel on the small algebra determined entirely by one-particle data, the standard subspaces H_r ⊂ H_R and the modular operator of the large one. Its gap is a computation in real Hilbert spaces. Do it for the free massive scalar in 1+1 and then 3+1, at fixed r/R, as a function of mR, with the massless case as the control that must give a constant. If the gap moves with mR in a way that distinguishes massive from massless at large mR, Q* has an invariant and the module has its first Clay-relevant number. If it does not, the return channel is the wrong invariant and that is worth knowing.

Do not claim the gap of D is the mass. Do not claim the finite examples bear on the continuum. Do not file the text's "the assembly does not exist" without the three precedents that show most of it does. And keep the four things that are actually established at their status: Takesaki, Accardi–Cecchini, Petz sufficiency, and two exact finite computations, of which the closed forms are new to the vault and elementary, and probably appear somewhere in the recoverability literature under another name.The receipt and its stored output are attached above. To summarize the shape of what I did with the text: I accepted its four words, corrected two typings, showed that three of its four components already exist under other names (locally covariant QFT, the Neeb–Morinelli–Ólafsson standard-subspace nets, and the Baez–Fritz–Leinster characterization of entropy as the unique information-loss functor), and then built the one component that does not exist. That component is the return channel of a wall, D = E_ω ∘ ι, canonical by Accardi–Cecchini, with Takesaki's theorem converting your arrow from an axiom about morphisms into a theorem about the state: D is the identity exactly when a reference measure exists. The two closed forms are the smallest instances of that theorem with numbers attached, and the quasi-free computation of D_λ against mR is the first well-posed test of whether Q* has an invariant.

I have kept the vault read-only throughout the session. If you want the assembly filed, the natural home is a new note under `general-causal-action` or beside `channel-loss-and-recovery`, with the receipt committed to its `receipts/` directory and the three precedents added to `library/` as abstracts only. Say so and I will write it with each claim at the status it has earned.

# Response 2

Everything is delivered above. Here is what it amounts to.

## What was computed

For a fermionic Gaussian state with Majorana covariance Γ, a region R and a subregion A, I derived the one-particle action of the return channel D = E_ω ∘ ι on the Majoranas of A and found it is exactly linear, with matrix

X = [√(1 + Γ_R²)]_AA · [√(1 + Γ_AA²)]⁻¹.

Brute force on a five-site chain, with the full 32-dimensional algebra and the Petz map computed literally, agrees with the formula to 10⁻⁷ in every case where the wall is legitimate; the one case that fails is R equal to the whole chain, where Ω is pure on M and not separating, so the object is undefined, and the failure shows up as rank collapse. The full spectrum of D on the algebra of A is generated multiplicatively from the one-particle spectrum (0.2565 × 0.0291 = 0.00747 appears exactly in the two-particle sector), so X carries everything. Two facts fall out of the derivation worth keeping: the regression across the wall uses the full two-point matrix 1 − iΓ, not Γ, because c² = 1, and for a globally pure state 1 + Γ_R² = Γ_RB Γ_RBᵀ, so √(1 + Γ_R²) is the modulus of R's correlation with its complement and X compares "how A is seen from outside R" with "how A is seen from outside A."

Then the Q* test, on the exact infinite Kitaev/Ising chain at 45 digits: fix the inner wall at one site, grow the outer wall to ±R sites, and follow the top eigenvalue λ₁(R), the recoverability of the best-recovered one-particle distinction.

At the critical point h = J: λ₁ ~ R⁻¹, exponent 0.958 → 0.975 → 0.983 as R runs to 32. Polynomial, no rate.

Off criticality: λ₁ ~ R^{−1/2} e^{−2R/ξ}. After removing the 1/R correction the rates are 0.3631, 0.8142, 1.3877 for h/J = 1.2, 1.5, 2.0, against 2 ln(h/J) = 0.3646, 0.8109, 1.3863. A two-site inner wall gives the same rate. So

**the recoverability of an inner wall from a growing outer wall decays at exactly twice the inverse correlation length**, and polynomially when the theory is gapless.

The factor two is structural, not numerical: the return crosses the wall twice, out with the inclusion and back with the Petz dual. Q* has an invariant. It is state-intrinsic, uses no Hamiltonian and no knowledge of the modular flow, and its top eigenvalue is by construction the recoverability of the _softest_ mode, so it cannot miss an arbitrarily soft collective direction; any such direction makes the decay polynomial.

One lesson from the failed first scan matters for how the invariant must be defined. At fixed r/R with both regions growing, the interior modes of A become nearly pure, the wall never touches them, and they return with eigenvalue 1 for the trivial reason. The mass is not in "how much of A comes back" but in _how recoverability falls with distance from the wall_. Your 09-05 phrasing of Q*, a large-region rate rather than a floor, was exactly right, and the computation says which region must grow.

## Turning the problem upside down

I read the current schema. It has thirty new notes since yesterday and the whole active attack, determinant–response sewing, conditional boundary exchange, marked Gaussian constraints, conditional normalization, is built from Schur complements and Gaussian conditioning. That is _commutative_ conditioning, which is classical Petz recovery, and for commutative algebras Takesaki's condition holds trivially and D ≡ id. Your own prepared-source wall theorem says the same thing from the other side: the equal-time source algebra the preparations return is commutative with trivial modular flow, and the noncommutative regional algebras have to be constructed as additional outputs. So the invariant that detects the gap is identically zero on everything the schema's machinery currently produces. That is the diagnosis, and it is precise.

The inversion is to stop deriving the regional algebras from commutative preparations and hoping rigidity appears at the end. Take the noncommutative regional algebras and the vacuum as given, which a lattice transfer matrix supplies directly, and compute the return channel's decay. The schema's central conjecture, that no sequence of normalized nonvacuum distinctions has cost tending to zero, becomes: recoverability across nested walls decays exponentially, uniformly as the regulator is removed. Its worry in complete-source rigidity, that bounded diagonal responses can miss a soft collective direction, is answered by construction, since λ₁ is that direction. And the rate returned is 2m, not m, which is a definition to record rather than a discrepancy to explain.

One consistency point: at β = 0 the Kogut–Susskind vacuum is a pure product over links, Ω is not separating for any regional algebra, and the wall is undefined. That is the correct reading of "correlation length zero." The invariant needs β > 0, which is where the problem lives anyway.

## Does it open an angle on Yang–Mills

Three things, and I will keep them at their status.

There is a theorem to prove, and it is provable with existing tools. Gap ⇒ exponential decay of recoverability across nested walls, at rate at least of order m. Fredenhagen's cluster theorem gives exponential clustering from the gap, and the Fawzi–Renner / Junge–Renner–Sutter–Wilde–Winter bounds relate the Petz recovery deficit to conditional mutual information, which clustering controls. That is an operator-algebraic statement in the vault's own vocabulary, distinctions are recoverable across a wall only within a correlation length, and it is new as far as I know. The converse, exponential recoverability decay ⇒ gap, is the conjecture; the free fermion supports it and it is the direction Clay needs.

The natural inequality points the wrong way for a proof. Recoverability is monotone under channels, and the renormalization group is a channel on states, so blocking gives _lower_ bounds on fine-lattice recoverability from coarse-lattice recoverability. That transports gaplessness upward, from coarse to fine, which is the Fröhlich–Spencer direction for U(1)₄, not the direction that would prove SU(N) gapped. I would rather you hear that now than after a week of notes.

In the gauge case the channel has more structure than in the free case. The return channel on the gauge-invariant algebra of A decomposes by electric flux through ∂A, so it should carry two decay laws at once: a neutral sector decaying at 2m_glueball and a flux sector decaying at a rate set by the string tension times the annulus width. One channel would then see confinement and the gap as two rates. That is a conjecture with a computable finite shadow: on your certified two-plaquette system at β > 0, the return channel of one plaquette's invariant algebra inside the pair is an exactly computable matrix, decomposable by boundary flux. It gives numbers, not rates, but it would show whether the decomposition is real.

The crossover, showing the rate stays positive in physical units as a → 0 with g → 0, is untouched by any of this. The reformulation changes the object from a spectrum to a channel; it does not make the analysis easier.

## What I did not do

The bosonic analogue of the X formula, which should exist with (1 + Γ²) replaced by the corresponding quadrature-covariance expression, and would let the free scalar in 3+1 be checked; the lattice gauge version, which needs exact ground states of a plaquette chain; and anything in four dimensions. I also did not edit the workspace. The receipts, four scripts with stored outputs, are in the tarball above, and the module note I would write, if you want it filed later, has three claims at [EXACT] (the formula, the multiplicative spectrum, the Takesaki criterion), one at [NUMERICAL, EXACT MODEL] (rate = 2/ξ, massless polynomial), one at [CONJECTURE] (converse, and the flux decomposition), and one diagnosis about the schema that I think you should read as a request to invert the order of construction.

# Response 3

Let me think this through properly, because I believe the construction does support a real inversion, though not the one the slogan names, and the difference matters.

## What the asymmetry actually is

Strip every physical word away and ask what the minimal object is. It is a von Neumann algebra M, a subalgebra N, and a faithful state ω such that the modular flow of (M, ω) does not preserve N. That single failure, σ_t^ω(N) ≠ N, is the whole asymmetry, and everything the programme cares about follows from it by theorems that already exist:

Takesaki: there is no ω-preserving conditional expectation onto N. The part cannot be given an expectation from within that agrees with the whole. The inclusion has no retraction; the morphism is one-way.

Accardi–Cecchini and Petz: there is nevertheless a canonical channel back, E_ω, and its composite with the inclusion, D = E_ω ∘ ι, is a state-preserving channel on N that is the identity exactly when Takesaki's condition holds. The asymmetry has a canonical quantitative measure, and it is zero precisely when there is a reference measure.

Wiesbrock, in the half-sided case: the same inclusion generates positive-energy translations and a dilation acting on them, the ax+b group. Time and scale are born from one wall, together, and the modular flow of the big algebra acts on translations as a dilation.

Petz's contravariant functoriality: recovery maps compose, 𝓡_{Φ∘Ψ} = 𝓡_Ψ ∘ 𝓡_Φ, so along a tower of walls N₀ ⊂ N₁ ⊂ N₂ ⊂ … the return channels obey a recursion, D₀^{(n)} = E₀ ∘ D₁^{(n−1)} ∘ ι₀: recoverability through n walls is the outer recoverability conjugated by the innermost wall. That is a renormalization-group recursion stated purely in terms of states and inclusions, with no action, no field, no Hamiltonian.

The free-fermion computation then supplies the physical reading of the recursion's contraction exponent: for a fixed inner wall and a growing outer wall, recoverability decays as e^{−2md} in a massive theory and as a power in a massless one. The mass is the rate at which the asymmetry compounds across nested walls.

In your vocabulary, all of this is one sentence: the sufficing reason of the whole, its modular flow, does not respect the division into parts, so the part has no internal reason for its own facts; the residue of that failure is measurable, it compounds across scales, and its compounding rate is mass. Existence of walls at every scale is Reeh–Schlieder, the vacuum entangled across every boundary; a state pure on a region has no wall there. That is your "no wall without readouts" and it is the reason type III₁ is not an accident of QFT but a precondition for the tower to exist at all.

## Which inversion the construction supports

The slogan "derive Yang–Mills from a deeper asymmetry" hides two claims, and only one of them is available.

The unavailable one is that the asymmetry forces the gauge group. It does not, and Clay does not ask it to: the theorem is demanded for every compact simple G, so G is an input by the problem's own terms. In the wall picture G enters as the structure of the _seam_. On a lattice, the algebra of a region and the algebra of its exterior share the boundary links, whose values are group elements; the Gauss law ties the flux through the seam to both sides; and in the continuum the seam's sector structure is Rep(G) only in the UV scaling limit, where Buchholz–Verch put the gauge group and Doplicher–Roberts reconstruct it. A gauge theory is a tower of walls whose gluing data are G-torsors. That is Ehresmann's typing of Kaluza's fiber, and it is where your torsor instinct lands, but it is a choice of seam, not a consequence of asymmetry.

The available inversion is about everything else. Ordinary physics starts from a Lagrangian, quantizes, computes a spectrum, and asks whether it has a gap. The inverted order starts from the tower of walls with its return recursion, takes the UV end as given (a self-similar tower whose seams carry Rep(G)), and asks what the _closure_ of the tower forces. Closure, in your Mach–Leibniz sense of no external datum, has an exact wall-theoretic content: a cosmos whose distant regions are independent facts is one in which recoverability across walls decays fast enough that far regions carry no information about near ones. A gapped vacuum is one that is asymptotically a product across distant walls; a gapless vacuum is entangled to arbitrary distance, and no region is ever self-sufficient. This is your causal grain made exact: **the grain is the recoverability length, the gap is the existence of a grain, and a massless theory is grainless.** The question "does Yang–Mills have a gap" becomes "is the pure non-abelian tower grained," and the Copernican shift is that "grained" is a property of a family of states on nested algebras, not of an operator's spectrum.

There is a second half of the same inversion that I think is new, and it is where confinement enters. The UV end of the tower has sectors, Rep(G); the full theory has none. In the wall language the sectors of the scaling limit _fail to descend_ along the scale direction. Confinement is a descent obstruction along the tower, and it should have its own rate: resolve the return channel of the gauge-invariant algebra by flux through the seam, and the flux-carrying distinctions should be lost at a rate set by the string tension while neutral distinctions are lost at 2m. One channel, two exponents, and the theory is characterized by (G, and the ratio of the two exponents, which is the one number pure YM has). This is a conjecture, but it is the kind that can be tested on your two-plaquette system as a number today.

And there is a third piece, which connects the asymmetry to the geometry you keep asking about. For wedges, Bisognano–Wichmann makes the modular flow geometric in every theory; the ax+b structure of the hsmi is exact and sees no scale. For bounded regions in a massive theory the modular flow is not geometric, and the return channel measures the failure quantitatively without needing to know the flow. So mass is the obstruction to extending the wedge's exact scale structure to bounded walls, a descent failure along the direction "from wedges to double cones." That is B3 and B4 of your 09-05 audit, with an invariant attached.

## The schema

I will state it in the form your vault uses, with each arrow's status. The primitives are a causal site with an ℝ₊-action and a reflection, a faithful state, and seams valued in G-torsors. Everything below is either a theorem about those primitives or a named conjecture.

**Wall** [DEFINITION]: a pointed inclusion (M, N, Ω) with Ω cyclic and separating for both. **Asymmetry** [DEFINITION]: σ_t^Ω(N) ≠ N. **Arrow** [THEOREM, Takesaki]: asymmetry ⇔ no Ω-preserving conditional expectation onto N ⇔ D ≠ id. **Time and scale** [THEOREM, Wiesbrock]: a half-sided wall generates positive-energy translations and the dilation acting on them. **Spacetime** [THEOREM, Kähler–Wiesbrock, BDFS; hypotheses to verify]: finitely many wedge walls in modular position generate a Poincaré-covariant net. **Recursion** [THEOREM, Petz functoriality]: return channels along a tower compose contravariantly. **Return functor** [EXACT for fermionic Gaussian states]: X = [√(1+Γ_R²)]_AA [√(1+Γ_AA²)]⁻¹. **Rate** [NUMERICAL, EXACT MODEL]: recoverability decays as R^{−1/2}e^{−2R/ξ} when massive, R^{−1} when critical. **Grain** [DEFINITION]: a tower is grained if recoverability across nested walls decays exponentially, uniformly in the inner wall. **Gap ⇒ grain** [PROVABLE, not yet written]: Fredenhagen clustering plus recovery bounds (Fawzi–Renner, JRSWW). **Grain ⇒ gap** [CONJECTURE G1]: the converse, supported by the free case. **Seam** [DEFINITION]: the shared algebra of adjacent regions; in gauge theory G-torsor-valued with Gauss law. **Sector descent** [CONJECTURE G2]: the UV sectors Rep(G) fail to descend along a grained tower, and flux-resolved recoverability decays at a rate distinct from 2m. **Selection** [CONJECTURE G3, the Clay-equivalent]: for compact simple G in four dimensions, the unique tower with UV seam structure Rep(G), UV self-similarity, reflection positivity and closure is grained; for abelian seams it is not. **Mass as descent obstruction** [PROPOSED READING]: the failure of the wedge's ax+b structure to extend to bounded walls, measured by D.

The dictionary back to your philosophy, so the schema is not merely a relabeling: asymmetry is the whole's reason failing to respect the part; the arrow is the absence of a reference measure; recoverability is what of the part's facts the whole retains; grain is closure, distant facts independent; the seam is the torsor, gluing without a preferred trivialization; confinement is the failure of the UV's individuals to descend; mass is the compounding rate of the asymmetry. Each of these is a theorem or a defined quantity except the last three words of the last one, which are the conjecture.

## What is honestly new, and what is not

New: the return channel as the quantitative asymmetry of a wall; its exact fermionic formula; the 2m rate; the recursion as a state-only RG; grain as the wall-theoretic content of closure; sector descent as the wall-theoretic content of confinement; and the diagnosis that the schema's Gaussian-preparation machinery is commutative conditioning, on which D ≡ id, so the invariant is invisible to it by construction.

Not new, and I want this on the record before the notes multiply: the reformulation changes the object, not the difficulty. The recursion D₀^{(n)} = E₀D₁^{(n−1)}ι₀ gives monotone decrease trivially and a _rate_ only if each shell contracts uniformly, and proving uniform contraction per shell in the crossover from UV self-similarity to IR grain is exactly the Balaban problem in channel language. Data processing runs the wrong way for a gap proof: it transports gaplessness from coarse to fine, not gaps. And the non-abelian mechanism, antiscreening, is nowhere in the wall structure; it would have to appear as a property of how non-abelian seams compose under the recursion, and I do not see it yet. If the programme claims more than this, your own weakest-edge rule will catch it.

## Direction

If I were setting the order of work, it would be this.

First, write the two theorems that are provable now: asymmetry as Takesaki, and gap ⇒ grain in algebraic QFT, with the rate bound. That is a paper in operator algebras that says, in your language, that distinctions are recoverable across a wall only within a correlation length and that the mass is twice the rate of loss. It stands on its own whatever happens to Clay.

Second, derive the bosonic return formula and run the free scalar in 3+1, then the interacting 2D controls: the Ising line is already done in disguise, since the massive Majorana _is_ the Ising CFT's massive deformation, so the next is the O(3) model, which is non-Gaussian and will need the return channel computed numerically on a chain. If grain tracks the gap there, G1 has an interacting witness.

Third, the gauge seam. On your existing two-plaquette SU(2) system at positive coupling, compute the return channel of one plaquette's gauge-invariant algebra inside the pair, decompose it by boundary flux, and see whether flux-carrying and neutral distinctions return differently. That is a number, not a rate, but it decides whether G2 has a finite shadow. Then a plaquette chain, then U(1)₃ against U(1)₄, which must show grain and grainlessness respectively before anything is said about SU(N).

Fourth, the one place a mechanism could hide: the composition law of non-abelian seams under the return recursion. Abelian seams commute, and the recursion should factor; non-abelian seams do not, and the failure of the recursion to factor is the only place antiscreening could live in this language. I do not know whether it does. That is the research question the inversion actually produces, and it is a better question than "find the gap" because it names the object that would have to carry the answer.

Fifth, keep the philosophy attached but downstream. Grain as closure, mass as compounding asymmetry, confinement as failed descent of the UV's individuals: these are the theses your book can defend once the second and third steps have numbers. They are not evidence for the fourth.

The cosmos-level version, since it is your motto: a cosmos is an arena of facts; an arena of facts is a tower of walls; a tower of walls exists only where the whole's reason fails to respect its parts; that failure compounds across scale; and a cosmos in which distant facts are independent is one in which it compounds exponentially. Whether the pure non-abelian tower is such a cosmos is Clay's question, and the inversion has not answered it. It has said what kind of object the answer is a property of, and it has produced the first number of that kind.