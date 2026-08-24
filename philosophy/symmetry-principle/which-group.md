# Which Group

The symmetry principle is a schema, not a proposition. "The laws are invariant under $G$" says nothing until $G$ is named, and all of the content sits in the choice. The schema also has a degenerate solution — general covariance can be arranged for almost any theory — so a symmetry claim earns content only by fixing what is *not* allowed to vary along with it. Whether a given transformation is gauge or physical is likewise not a fact about the group alone but about the declared observables and about its behavior at the boundary.

## The index problem

As with the indexed principle $\mathrm{PII}(\mathcal F)$ of [[philosophy/indiscernibility-of-identicals/two-directions|the indiscernibility module]], the invariance axiom is properly written $\mathrm{Inv}(G)$ and is antitone in its index: the larger the group, the stronger the claim and the smaller the class of theories satisfying it. Announcing "the symmetry principle" without $G$ announces nothing.

The two indices are dual rather than identical. Commitment PC2 in [[program-core/axioms-and-principles|the axiom and principle ledger]] indexes the *discernment* side by a declared family of possible factual consequences, with the sharpening that indirect geometric, charge, or record consequences count as discernment even when nothing can be read directly across a wall; $\mathrm{Inv}(G)$ is that family's Galois dual, related to it by the connection in [[philosophy/indiscernibility-of-identicals/symmetry-as-dual-of-discernment|symmetry as the dual presentation of discernment]] and faithful only above arity one. [[program-core/physical-quotient|The physical quotient]] carries the construction.

There are two very different ways to supply the index.

**Read off.** Given a structure, $G=\operatorname{Aut}(X)$ is determined. This is the direction of that Galois connection, where invariance and automorphism are two coordinates on one declaration.

**Imposed.** Given a group, demand that the theory be built from its invariants. This is the working method of gauge theory and effective field theory, and it is a construction rather than a discovery. What it cannot do is establish that the theory has an action at all — see [[independence-from-the-variational-axiom]].

## The degenerate solution

Left unqualified the schema is nearly vacuous. Kretschmann's objection is that any local theory can be rewritten in generally covariant form by promoting its background structures to fields or writing everything in tensors, so general covariance by itself excludes almost nothing. Invariance becomes contentful only when accompanied by a statement of what remains fixed — which structures are given as background rather than solved for.

The standard repair is to require that the theory contain no *absolute objects*: no field that is the same, up to diffeomorphism, in every solution. Anderson's criterion is a proposal with known difficulties in the precise formulation of sameness, and should be cited as the shape of the repair rather than as a settled definition. The durable moral survives either way:

$$
\boxed{
\text{a symmetry claim has content only relative to a declaration of what is held fixed}.
}
$$

This is the structure the indiscernibility module found in the razor. A principle stated over an unrestricted domain trivializes; the work is done by the restriction.

## Global, local, and the boundary

A global symmetry acts by one group element throughout and relates situations the theory distinguishes. A local symmetry acts by an arbitrary function of position, and whether it relates descriptions or situations depends on its behavior at the boundary: transformations approaching the identity there are redundancies of the formalism, while those with nontrivial asymptotic or corner behavior relate physically distinct states and carry genuine charges, as [[philosophy/noether-conservation/second-theorem-and-gauge|the second theorem and gauge]] sets out.

Which transformations count as redundant is in any case a fact about the declared observables, since a transformation is gauge exactly when it lies in the kernel of the declared family — the point made in [[philosophy/indiscernibility-of-identicals/symmetry-as-dual-of-discernment|symmetry as the dual presentation of discernment]]. The same abstract group can occupy either role in different theories.

The consequence for the third module is a fork in which theorem applies. Noether's first theorem takes a group with *finitely many parameters* and returns conserved currents; a symmetry parameterized by *arbitrary functions* falls under the second theorem and returns identities among the equations of motion. The criterion is the parameter count, not the geometry of the action: the generators need not act on spacetime or on an internal bundle at all, and admitting ones that do not is what makes the converse in [[philosophy/noether-conservation/variational-versus-dynamical-symmetry|variational versus dynamical symmetry]] hold. Misclassifying produces either a phantom conservation law or a missing one.
