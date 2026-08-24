# Nonfaithful Realization and the Limit of Unitarity

A realization that genuinely forgets distinctions cannot be a unitary equivalence between its source and target categories. This is an exact categorical obstruction, not an interpretation of a wave function: equivalences are faithful, whereas a physical quotient or observational wall is nonfaithful precisely when distinct source arrows acquire one observable image. Unitarity may still govern reversible transport within a realized register, but it cannot be the law of a cross-register map whose work is to identify distinctions.

## Realization is a map between mathematical realities

Let

$$
\Pi:\mathcal C_{\mathrm{int}}
\longrightarrow
\mathcal C_{\mathrm{obs}}
$$

be a proposed realization or presentation functor from an internal mathematical regime to an observable one. Neither category is ontologically downgraded by this notation. The functor states how the second structure is borne by the first.

For each pair of objects \(x,y\), \(\Pi\) induces

$$
\Pi_{x,y}:
\operatorname{Hom}_{\mathcal C_{\mathrm{int}}}(x,y)
\longrightarrow
\operatorname{Hom}_{\mathcal C_{\mathrm{obs}}}(\Pi x,\Pi y).
$$

The realization is **faithful** when every \(\Pi_{x,y}\) is injective. It is genuinely forgetful at the arrow level when there are \(f\ne g\) with

$$
\Pi(f)=\Pi(g).
$$

This defines a congruence on source arrows. If objects rather than arrows are identified, the corresponding kernel pair or essential-image relation must be stated separately. “Information loss” without one of these typed identifications is not yet a mathematical claim.

## Exact nonfaithfulness obstruction

**Proposition.** If \(\Pi\) is an equivalence of categories, then \(\Pi\) is full and faithful. Consequently, a nonfaithful realization cannot possess a quasi-inverse and cannot be a unitary equivalence of represented categories.

**Proof.** Let \(G\) be a quasi-inverse with a natural isomorphism

$$
\eta:\operatorname{id}_{\mathcal C_{\mathrm{int}}}
\xRightarrow{\sim}
G\Pi.
$$

If \(\Pi(f)=\Pi(g)\) for \(f,g:x\to y\), then naturality gives

$$
\eta_y\circ f
=G\Pi(f)\circ\eta_x
=G\Pi(g)\circ\eta_x
=\eta_y\circ g.
$$

Since \(\eta_y\) is invertible, \(f=g\). Thus \(\Pi\) is faithful. Fullness follows by transporting a target arrow through the unit and counit of the equivalence. \(\square\)

The contrapositive is the relevant theorem:

$$
\boxed{
\text{genuine categorical forgetting}
\Longrightarrow
\text{no equivalence across that realization}.}
$$

An equivalence is also conservative and injective on isomorphism classes: if \(\Pi(f)\) is an isomorphism, fullness supplies a candidate inverse and faithfulness proves the inverse identities; if \(\Pi x\simeq\Pi y\), fullness lifts that isomorphism and conservativity shows \(x\simeq y\). Hence either of the following also obstructs equivalence:

$$
f\text{ noninvertible but }\Pi(f)\text{ invertible},
$$

$$
x\not\simeq y
\quad\text{but}\quad
\Pi x\simeq\Pi y.
$$

If the categories are concretely represented on Hilbert spaces and the proposed cross-register map is conjugation by a unitary, it is invertible and hence faithful. It therefore cannot perform a nontrivial quotient. This does not disprove unitary dynamics of a closed observable subsystem inside \(\mathcal C_{\mathrm{obs}}\); it localizes the domain on which a unitarity claim can be true.

## A dilation is a factorization, not an inverse

A completely positive map may admit a Stinespring representation

$$
\Phi(a)=V^*\pi(a)V.
$$

The representation embeds the formula into a larger carrier. It does not supply an inverse to \(\Phi\), prove that \(\Phi\) is faithful on physical distinctions, or establish that the dilation space is the ontology from which the apparent loss can be recovered. Treating every mathematical dilation as a physically instantiated environment would add an ontological postulate that is absent from the representation theorem.

For a state-preserving conditional expectation

$$
E:\mathcal M\to\mathcal N,
\qquad
E^2=E,
$$

with \(\mathcal N\subsetneq\mathcal M\), noninvertibility is part of the construction. Under the finite tracial hypotheses, [[spectral-wall-descent/conditional-expectation-balance|the conditional-expectation theorem]] gives the exact identities

$$
D(\rho\Vert\tau)
=D(E\rho\Vert\tau)
+D(\rho\Vert E\rho)
$$

and

$$
G^{\mathrm{pre}}
=G^{\mathrm{ret}}
+G^{\mathrm{lost}}.
$$

These quantify a selected nonfaithful passage. They do not reverse it.

## Strict descent is not the forgetting map

Strict descent glues compatible local presentations into a global object. Its comparison arrows are ordinarily equivalences satisfying cocycle coherence. Effective descent can retain all stabilizers and local data in a stack. It therefore does not, by itself, erase information or generate entropy.

Genuine forgetting may instead be implemented by:

- an effective quotient or coequalizer of a declared kernel pair;
- a coarse-moduli map that discards stabilizers;
- a localization that inverts a chosen class of arrows;
- decategorification;
- restriction to a subalgebra;
- a conditional expectation or instrument; or
- a nonconservative realization functor that sends a nonisomorphism to an isomorphism.

Each operation forgets a different type of structure. [[algebra/local-global-individuation|Local--global individuation]] owns the further distinction between this loss, factual selection, and persistent record extension.

## What can be conserved

Nonfaithfulness does not imply that “information” moves into another reservoir. A balance among erased distinction, entropy, geometry, and records becomes meaningful only after all terms map to a common additive carrier.

One precise target is a commutative monoid \(A\), together with additive process valuations

$$
\lambda_i:\mathsf P\longrightarrow BA,
$$

where \(BA\) is the one-object category whose composition is addition in \(A\). For composable processes \(p,q\), each valuation must satisfy

$$
\lambda_i(q\circ p)
=\lambda_i(q)+\lambda_i(p).
$$

Only after natural comparison maps place loss, record growth, scale growth, and geometric response in \(A\) can one propose an identity such as

$$
\lambda_{\mathrm{total}}
=\lambda_{\mathrm{loss}}
+\lambda_{\mathrm{record}}
+\lambda_{\mathrm{geom}}.
$$

The equation would still need a derivation from a symmetry, universal property, or exact factorization. Without those maps, it is an addition of unlike types. [[program-core/record-scale-soldering|Record--scale soldering]] states the more specific conditions under which record order, cosmic scale, entropy, and horizon area could become aspects of one process law.

## Consequences

The proposition closes one conceptual question and leaves the constructive physics visible:

- global cross-register unitarity is incompatible with genuine nonfaithful realization;
- local unitarity inside a reversible observable sector may remain exact;
- loss of accessible distinction is genuine without being annihilation of the source mathematics;
- persistent algebraic or \(K\)-theoretic classes may survive even when the realization is nonfaithful;
- an actual fact still requires a pointing or instrument outcome; and
- time still requires an oriented, persistent record order.

Thus the correct replacement for unrestricted information conservation is not arbitrary destruction. It is **compositional exactness with explicitly typed loss**.
