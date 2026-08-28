---
inq.module: "indiscernibility-of-identicals"
inq.include:
  - "**/*.md"
---
# Identity and Indiscernibility

Leibniz's law has two directions of unequal standing. That identicals are indiscernible is a well-definedness condition on whatever counts as a property, and cannot fail. Its converse — that indiscernibles are identical — is substantive, exactly equivalent to the claim that the declared properties separate points, and defeated wherever those properties are invariants of a nontrivial symmetry. Physics does not discover the converse but imposes it, and a symmetry group is that imposition written as a kernel.

## The two directions

For a domain $X$ and a declared family $\mathcal F$ of properties, observables, or accessible maps, write $a\equiv_{\mathcal F}b$ when every member of $\mathcal F$ agrees on $a$ and $b$. The two implications are

$$
a=b\Longrightarrow a\equiv_{\mathcal F}b
\qquad\text{and}\qquad
a\equiv_{\mathcal F}b\Longrightarrow a=b .
$$

The first holds for every $\mathcal F$ whatsoever, because the members of $\mathcal F$ are functions of their argument; it constrains the presentation and says nothing about $X$. The second is a property of the pair $(X,\mathcal F)$, antitone in $\mathcal F$, and equivalent to a condition that can be checked:

$$
\boxed{
\mathrm{PII}(\mathcal F)\ \text{on}\ X
\iff
\mathcal F\ \text{separates the points of}\ X .
}
$$

Failure admits a canonical repair — pass to $X/\!\equiv_{\mathcal F}$, through which every declared map factors uniquely — so the principle is never evidence for anything, since it can always be arranged. What carries information is the quotient map and what it discards.

## Argument

[[two-directions]] fixes the asymmetry and shows that the converse collapses into a theorem of logic if the family may contain identity properties, so that the principle is always the indexed claim $\mathrm{PII}(\mathcal F)$ over a qualitative family.

[[separation-and-quotient]] proves the separation equivalence and follows the same repair through the Kolmogorov quotient, the Gelfand spectrum, and almost-everywhere equality, ending at the Yoneda embedding, where indiscernibles are returned canonically isomorphic rather than equal — and at the price univalence pays for adopting that conclusion as an identity, namely that equality acquires the structure of a groupoid.

[[grades-of-discernment]] separates discernment by a property, by an asymmetric relation, and by an irreflexive one, proves the hierarchy strict, and locates the standard counterexamples: automorphism orbits are exactly the classes of the full invariant family and sit inside those of the definable family, while a transitive action leaves only constants invariant. The weakest grade is circular in a language that already contains identity.

[[rigidity-and-surplus-structure]] follows that obstruction: against the full family of invariants rigidity *is* the principle, while against what a language can define it is necessary and not sufficient. Geometrically a free and proper action costs nothing, non-properness can cost the quotient its existence as a space, and retained isotropy can cost it its smoothness. A $G$-torsor over a point states this project's governing intuition without remainder: no invariant function distinguishes two of its points, while the difference map $\delta:P\times P\to G$ distinguishes every pair of them. [[basic-concepts/groupoids/inq|Groupoids]], [[basic-concepts/torsors/inq|torsors]], [[basic-concepts/descent/inq|descent]], and [[basic-concepts/stacks/inq|stacks]] are the disciplined way of living with the failure of this principle rather than quotienting it away.

[[symmetry-as-dual-of-discernment]] gives the Galois connection between invariance and automorphism, and the reason it is faithful only above arity one: at the grade of properties the recovered group is a product of symmetric groups on the blocks of a partition, and a symmetry carries more than a partition exactly because discernment is relational. It also records that gauge and physical symmetry differ by index rather than by kind, and that discernment is a presheaf — indiscernibility on every patch does not imply it globally, so a razor applied region by region can delete a holonomy.

[[the-razor]] states the rule in two-sided form, over-cutting and under-cutting being the same error in opposite signs, and registers the ways it is applied without its index, its category, or its scope.

[[why-there-is-difference]] runs the razor backwards. If every declared observable is constant the readout context is $\mathbb C$, which has one state and one character: such an arena exists and has a fact, and the fact carries no information, so a demand for a reason that there is something rather than nothing under-specifies its target. The sharpened question is why the readout context has more than one character. Its second half receives an answer of the right type — within a commutative context everything is valued at once, so *at once* names commutativity rather than a temporal notion, while by Kochen--Specker the spectral presheaf over the contexts has no global section — and the proposed reading is that this non-totalizability is where succession has to live. That a poset of contexts is not an order, an order not an orientation, and a claim about valuations not a claim about processes are the three gaps, carried by [[sufficient-reason/algebraic-arrow-of-time|the algebraic arrow programme]] and [[cosmodynamics/fact-record-history|Fact, Record, and History]].

## Claim levels

| Status | Content |
|---|---|
| Exact | the asymmetry of the two directions; $\mathrm{PII}(\mathcal F)$ iff $\mathcal F$ separates points; the universal quotient; antitonicity in $\mathcal F$; the three grades, their implications, and the strictness of both; orbits equal to the classes of the full invariant family and contained in those of the definable family; transitive action gives constant invariants; the invariance/automorphism Galois connection, its closure operators, and its collapse at arity one |
| Exact, hypotheses named | rigidity as triviality of the orbit structure, for automorphisms determined by their action on points; Krasner closure under pointwise convergence, over invariants of all finite arities; the Ryll-Nardzewski converse, for a countable structure $\omega$-categorical in a countable language; separation of closed orbits only, for a reductive group in the algebraic setting; joint spectral resolution, for bounded or strongly commuting operators; Kochen--Specker for dimension at least three |
| Adopted convention | the diagnostic reading of the razor; the constitutive reading is available but not applicable where the observable family is still under construction |
| Axiom in the setting adopted | univalence as the strongest form of the converse — added in book type theory, a theorem in cubical type theory — paid for by identity acquiring groupoid structure |
| Proposed reading | non-totalizability of contexts as the residence of succession; a homogeneous ground whose facts are sections rather than invariants |
| Contested | weak discernibility of fermions in an antisymmetric state |
| Open | why the readout context has more than one character; the passage from a poset of contexts to an order on facts; orientation of that order; whether the staging is arena-side or observer-side |
| Outside this module | actuality of an outcome; any conservation law; the derivation of an internal symmetry group |
