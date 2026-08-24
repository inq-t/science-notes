# Identity and Indiscernibility

Leibniz's law has two directions of unequal standing. That identicals are indiscernible is a well-definedness condition on whatever counts as a property, and cannot fail. Its converse — that indiscernibles are identical — is substantive, false of any structure with a nontrivial automorphism, and exactly equivalent to the statement that the declared properties separate points. Physics does not discover the converse; it imposes it, and a symmetry group is that imposition written as a kernel. This module states the razor the imposition licenses, the grades of discernment it must respect, the structures that survive its failure, and the sense in which the possibility of a cosmos is the non-triviality of a discernment relation.

## The asymmetry

For a domain $X$ and a declared family $\mathcal F$ of properties, observables, or accessible maps, [[two-directions]] separates

$$
a=b\Longrightarrow a\equiv_{\mathcal F}b
\qquad\text{from}\qquad
a\equiv_{\mathcal F}b\Longrightarrow a=b .
$$

The first says only that the members of $\mathcal F$ are functions of their argument, and constrains the presentation rather than the world. The second is a property of the pair $(X,\mathcal F)$, is antitone in $\mathcal F$, and collapses into a theorem of logic if $\mathcal F$ is permitted to contain identity properties. It is therefore an indexed claim $\mathrm{PII}(\mathcal F)$, and the index is not decoration.

## What the converse says exactly

[[separation-and-quotient]] reduces it to a checkable condition,

$$
\boxed{
\mathrm{PII}(\mathcal F)\ \text{on}\ X
\iff
\mathcal F\ \text{separates the points of}\ X ,
}
$$

and observes that failure always admits the same repair: pass to $X/\!\equiv_{\mathcal F}$, through which every declared map factors uniquely. The principle is consequently never evidence, since it can always be arranged; what carries information is the quotient map and what it discards. The same repair appears as the Kolmogorov quotient, the Gelfand spectrum, and almost-everywhere equality, and appears in its most exacting form as the Yoneda embedding, where indiscernibles are returned not equal but canonically isomorphic — the isomorphism being the datum that the set-level quotient throws away.

## Discernment has grades

The conclusion also depends on how the discriminating formula is allowed to look. [[grades-of-discernment]] fixes the strict hierarchy of absolute, relative, and weak discernibility, and records the two facts that govern all standard counterexamples: automorphism orbits lie inside the indiscernibility classes of the invariant language, and a transitive action leaves only constants invariant. The weakest grade is informative only in a language from which identity has been excluded, and is otherwise circular.

## Failure has a structural name

Non-rigidity is failure of the converse, measured exactly. [[rigidity-and-surplus-structure]] follows the consequence into geometry: where the action is free the quotient loses nothing an invariant could have seen, and where stabilizers are present the quotient is singular along precisely the strata that the discarded automorphisms occupied. The honest repair is to keep the arrows. [[basic-concepts/groupoids/entry|Groupoids]], [[basic-concepts/torsors/entry|torsors]], [[basic-concepts/descent/entry|descent]], and [[basic-concepts/stacks/entry|stacks]] are best read as the mathematics of living with the failure of this principle rather than quotienting it away, and a moduli problem needs a stack instead of a space for exactly this reason.

The torsor is the sharpest case and states this project's governing intuition without remainder: every invariant function is constant, so no point is discernible from any other, while the difference map $P\times P\to G$ is canonical, so every difference is. The content is entirely relational.

## Symmetry is the dual presentation

Invariance and automorphism form a Galois connection, so declaring which differences make a difference and declaring a symmetry group are one act performed in two coordinates. [[symmetry-as-dual-of-discernment]] gives the connection, the closure operators that make it a bijection only between closed objects, and the settings — algebraic quotients above all — where invariants over-cut without anyone's assistance. It also records that gauge and physical symmetry differ by index rather than by kind, and that discernment is a presheaf: indiscernibility on every patch does not imply indiscernibility globally, so a razor applied region by region can delete a holonomy.

That the connection carries no dynamics is the standing limit. It says which transformations are undetectable and therefore nothing about what is conserved; the additional hypotheses are enumerated in [[conservation-of-causal-charge/indiscernibility-and-the-noether-gap|Indiscernibility and the Noether Gap]].

## The razor

[[the-razor]] states the rule in its two-sided form — the formalism's distinctions should match the observables' discriminations, with over-cutting and under-cutting the same error in opposite signs — and registers the ways it is applied without its index, its category, or its scope. Its boundary is worth naming here: the razor governs what could be a fact and never which fact obtains. A separating family delivers a spectrum, not a point of it, and the gap between them is the whole subject of [[sufficient-reason/entry|Sufficing and Necessitating Reason]].

## Why there is difference

Run backwards, the razor is a condition on the possibility of a cosmos, and [[why-there-is-difference]] draws the consequence. If every declared observable is constant, the readout algebra is $\mathbb C$: nonzero, unital, possessed of exactly one state and one character. Such an arena exists and has a fact, and the fact carries no information. The demand for a reason that there is something rather than nothing therefore under-specifies its own target, since non-emptiness is satisfied by $\mathbb C$. The sharpened question is why the readout algebra exceeds $\mathbb C$ — why there is more than one fact, not why there is one.

The second half of the question receives an answer of the right type. Within a commutative context every quantity is valued at once, so *at once* is the algebraic notion of commutativity rather than a temporal one; and by Kochen--Specker the totality of contexts admits no joint character while each context admits its own. Difference exists and cannot be totalized. The proposed reading is that this non-totalizability is where succession has to live. The gaps are that a poset of contexts is not an order on facts, an order is not an orientation, and a claim about valuations is not yet a claim about processes; those are carried by [[sufficient-reason/algebraic-arrow-of-time|the algebraic arrow programme]] and [[cosmodynamics/fact-record-history|Fact, Record, and History]].

## Claim levels

| Status | Content |
|---|---|
| Exact | the asymmetry of the two directions; $\mathrm{PII}(\mathcal F)$ iff $\mathcal F$ separates points; the universal quotient; antitonicity in $\mathcal F$; the three grades and their strict implications; orbits contained in invariant-indiscernibility classes; transitive action gives constant invariants; rigidity as triviality of the orbit structure; the invariance/automorphism Galois connection and its closure operators |
| Exact, hypotheses named | the Ryll-Nardzewski converse for $\omega$-categorical structures; closure of a permutation group under pointwise convergence; separation of closed orbits only, in the algebraic setting; Kochen--Specker for dimension at least three |
| Adopted convention | the constitutive reading of the razor, under which the physical state is the equivalence class |
| Axiom, not theorem | univalence, as the strongest available form of the converse, paid for by identity acquiring groupoid structure |
| Proposed reading | non-totalizability of contexts as the residence of succession; homogeneity of the ground with facts as sections rather than invariants |
| Open | why the readout algebra exceeds $\mathbb C$; the passage from a poset of contexts to an order on facts; orientation of that order; whether the staging is arena-side or observer-side |
| Outside this module | actuality of an outcome; any conservation law; the derivation of an internal symmetry group |
