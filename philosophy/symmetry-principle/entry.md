# The Invariance Axiom

The second of the three principles. It asserts that a theory is unchanged under the action of a group, and it is a schema rather than a proposition: the content lies entirely in which group and, just as much, in which object is left invariant. A configuration, a solution set, an action, and a functional measure are different targets with different consequences, and the third module needs the action specifically. The axiom is independent of the variational one, though it constrains actions sharply once an action is granted.

## The axiom

For a group $G$ acting on the objects of a theory,

$$
\boxed{\ \text{the theory is unchanged under }G\ }
$$

— which is under-specified twice over, and both gaps are load-bearing.

## Invariance of what

[[invariance-of-what]] separates the five targets and shows the nesting

$$
\text{strict}\subseteq\text{variational}\subseteq\text{dynamical}
$$

to be strict. Kepler's rescaling $\boldsymbol r\mapsto\lambda^2\boldsymbol r$, $t\mapsto\lambda^3t$ sends $S\mapsto\lambda S$: it maps solutions to solutions, so it is a symmetry of the laws, and it preserves neither the action nor the action up to a divergence, so it produces no conserved quantity. A symmetry can be real, famous, and Noether-inert.

This is the hinge of the section. The invariance axiom is naturally stated about laws, and Noether's theorem requires it about the action. The synthesis is therefore not the plain conjunction of the two axioms but a *re-typing* of the second onto the object the first introduces, and that upgrade can fail.

Invariance of the functional measure is a further and separate hypothesis, whose failure is an anomaly.

## Which group

[[which-group]] treats the other gap. The axiom is properly $\mathrm{Inv}(G)$ and antitone in its index, exactly as the razor of [[philosophy/indiscernibility-of-identicals/two-directions|the indiscernibility module]] is properly $\mathrm{PII}(\mathcal F)$; announced without $G$ it announces nothing. The index may be read off a structure, in which case invariance and automorphism are the two coordinates of one declaration, or imposed in order to build a theory, in which case it is a construction.

Left unqualified the schema nearly trivializes, since general covariance can be arranged for almost any local theory. A symmetry claim earns content only against a declaration of what is held fixed, the standard repair being a prohibition on absolute objects — a proposal with known difficulties in its precise formulation, and better cited as the shape of the repair than as a definition. Whether a group is gauge or physical is likewise not a fact about the group but about the declared observables, and it decides which of Noether's two theorems applies.

## Law and state

[[law-symmetry-and-state-symmetry]] disposes of the inference from symmetric laws to symmetric outcomes. A symmetric law requires only that the solution *set* be closed under the group, so Curie's principle is true of orbits and false of individual solutions. The consequence that matters downstream is the separation of explicit from spontaneous breaking: spontaneous breaking leaves the action invariant, so the Noether current remains conserved and only the charge may become ill defined in infinite volume, whereas explicit breaking removes the hypothesis and the conservation law with it.

## Independence

[[independence-from-the-variational-axiom]] argues that neither axiom entails the other. A generic potential is variational with no symmetry. In the other direction, invariance of a system of expressions does not imply the self-adjointness that variationality requires, since the two conditions constrain independent features — though the stronger claim, that some symmetric *dynamics* admits no action under any multiplier, is left unverified here and should not be asserted.

What symmetry does do, once an action is granted, is select among actions: with locality, field content, and a derivative bound, invariance can fix one nearly uniquely. Selection within the variational class is not establishment of membership in it.

## Claim levels

| Status                        | Content                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                    |                                                                                                         |                      |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------- |
| Exact                         | the five targets are distinct claims; strict $\subseteq$ variational $\subseteq$ dynamical; strictness of the second inclusion, witnessed by Kepler rescaling $S\mapsto\lambda S$; a divergence added to $L$ leaves the Euler--Lagrange expressions unchanged; the solution set of an invariant law is a union of orbits; invariance of a presentation does not imply its self-adjointness |                                                                                                    |                                                                                                         |                      |
| Exact, hypotheses named       | conservation of the Noether current under spontaneous breaking, with the charge possibly ill defined in infinite volume; near-unique selection of an action from invariance given locality, field content, and a derivative bound                                                                                                                                                          |                                                                                                    |                                                                                                         |                      |
| Proposal, contested in detail | the absolute-object criterion as the repair for Kretschmann's objection                                                                                                                                                                                                                                                                                                                    |                                                                                                    |                                                                                                         |                      |
| Open                          | whether a symmetric dynamics exists that admits no action under any multiplier; what grounds the invariance axiom itself, no reconstruction being offered here; which group, in any given case                                                                                                                                                                                             |                                                                                                    |                                                                                                         |                      |
| Outside this module           | the existence of an action — see [[philosophy/principle-of-least-action/entry                                                                                                                                                                                                                                                                                                              | the variational axiom]]; the conservation law itself — see [[philosophy/noether-conservation/entry | the Noether synthesis]]; the selection of the internal gauge group — see [[symmetry-groups-select/entry | symmetry selection]] |
