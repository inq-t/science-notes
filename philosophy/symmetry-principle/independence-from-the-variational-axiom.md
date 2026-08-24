# Independence from the Variational Axiom

Neither axiom entails the other as a condition on presentations of dynamics; the stronger claim about dynamics is left open below. The variational axiom constrains the derivative structure of the equations, through self-adjointness; the invariance axiom constrains their behavior under a group. These are conditions on different features. Independence should not be overstated in the other direction either, since invariance does real work on actions once an action is granted.

## Variational without a given symmetry

A variational system need not possess any *particular* symmetry, and so need not possess the conservation law that symmetry would supply. For

$$
L=\tfrac12m\dot{\boldsymbol x}^{\,2}-V(t,\boldsymbol x)
$$

with $V$ generic in both arguments, there is no spatial invariance and no time-translation invariance, hence neither momentum nor energy is conserved. The explicit $t$-dependence is essential to the example: the autonomous $L=\tfrac12m\dot{\boldsymbol x}^2-V(\boldsymbol x)$ is time-translation invariant for *every* $V$ whatsoever, and its energy is conserved however irregular the potential.

The claim must be stated at the right strength, and it differs between ordinary and partial differential equations. A regular variational system of *ordinary* differential equations cannot lack conservation laws altogether: away from equilibria the flow-box theorem supplies $2n-1$ independent local first integrals, and by the converse in [[philosophy/noether-conservation/variational-versus-dynamical-symmetry|variational versus dynamical symmetry]] each is the charge of some generalized variational symmetry, so what is absent is only any *named* symmetry and its particular charge. No such guarantee holds in field theory, where there is no flow-box theorem: a generic $\mathcal L=\tfrac12\eta^{\mu\nu}\partial_\mu\phi\,\partial_\nu\phi-V(x,\phi)$ is normal and totally nondegenerate, has no variational symmetry, and therefore by that same converse has no nontrivial conservation law at all.

So the first axiom does not deliver the second.

## Symmetry without variational structure

The converse comes in two strengths.

**Exact, about presentations.** Invariance of a system of expressions does not imply self-adjointness of that system. The pair displayed in [[philosophy/principle-of-least-action/variational-is-a-restriction|variationality is a restriction]] is invariant under time translation and under translation in each $q^i$, and fails the first Helmholtz condition. Symmetry conditions and self-adjointness conditions therefore constrain independent features of the equations, and no amount of the former supplies the latter.

**Open, about dynamics.** That witness is a badly written free particle: a multiplier repairs it, so it shows independence of the two *conditions* without exhibiting a symmetric dynamics that admits no action whatever. Establishing the stronger claim requires a system with a continuous symmetry lying in one of the classes Douglas showed to admit no multiplier, and this note does not supply one. The strong independence claim is plausible and unverified.

The weaker result suffices for the section's purpose. Nothing in the invariance axiom mentions an action, and a theory must be shown variational before its symmetries can be asked to produce conservation laws.

## The partial dependence that does exist

$$
\boxed{
\text{invariance can select an action within the variational class; it cannot establish membership in the class}.
}
$$

Given locality, a field content, and a bound on derivative order, invariance can determine an action nearly uniquely — the four-dimensional metric case in [[philosophy/principle-of-least-action/einstein-hilbert-action|the Einstein--Hilbert action]] is the standard demonstration, and effective field theory the general method. This is selection among variational theories, which presupposes variationality rather than deriving it. The distinction is the one drawn for internal symmetry in [[symmetry-groups-select/reconstruction-versus-selection|gauge reconstruction is not gauge selection]]: a theorem that operates on supplied data does not supply the data.

## Neither grounds the other

The two axioms are independent in their justifications. The reconstruction in [[philosophy/principle-of-least-action/why-an-action-at-all|why there is an action]] derives the form of the action from a composition law on histories and never mentions a group; whatever grounds the invariance axiom — and this section does not claim to have grounded it — will not be that argument.

This is independence in the order of justification, and it does not conflict with the order of *statement*, in which the variational axiom is prior: the invariance the synthesis needs is invariance of an object that only the first axiom supplies.
