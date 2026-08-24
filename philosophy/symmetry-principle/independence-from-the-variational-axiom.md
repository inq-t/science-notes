# Independence from the Variational Axiom

Neither axiom entails the other. The variational axiom constrains the derivative structure of the equations, through self-adjointness; the invariance axiom constrains their behavior under a group. These are conditions on different features, and neither implies the other as a matter of logic. The easy direction has a trivial witness. The hard direction is established as a claim about presentations of dynamics and is left open here in its strongest form, which is a limitation worth stating rather than hiding.

## Variational without symmetry

Take

$$
L=\tfrac12m\dot{\boldsymbol x}^{\,2}-V(\boldsymbol x)
$$

for a potential with no continuous invariance — generic, with no level-set symmetry and no periodicity. The system is variational by construction and possesses no continuous variational symmetry, hence no Noether current. The damped oscillator of [[philosophy/principle-of-least-action/variational-is-a-restriction|variationality is a restriction]] makes the same point with time translation specifically: an action exists, and its explicit time dependence leaves no conserved energy.

So the first axiom does not deliver the second, and a world could satisfy it completely while exhibiting no conservation laws at all.

## Symmetry without variational structure

The converse requires care, and the honest answer comes in two strengths.

**Exact, about presentations.** Invariance of a system of expressions does not imply self-adjointness of that system. The pair

$$
E_1=\ddot q^{\,1}+\ddot q^{\,2},
\qquad
E_2=\ddot q^{\,2}
$$

is invariant under time translation and under translation in each $q^i$, and fails the first Helmholtz condition, since $\partial E_1/\partial\ddot q^{\,2}=1$ while $\partial E_2/\partial\ddot q^{\,1}=0$. Symmetry conditions and self-adjointness conditions therefore constrain independent features of the equations, and no amount of the former supplies the latter.

**Open, about dynamics.** The witness above is a badly written free particle: a multiplier repairs it, so it shows independence of the two conditions without exhibiting a symmetric *dynamics* that admits no action whatever. Establishing that stronger claim requires a system with a continuous symmetry lying in one of the classes Douglas showed to admit no multiplier, and this note does not supply one. The strong independence claim is therefore plausible and not verified here.

The weaker result is nevertheless enough for the section's purpose. Nothing in the invariance axiom mentions an action, and a theory must be shown variational before its symmetries can be asked to produce conservation laws.

## The partial dependence that does exist

Independence should not be overstated in the other direction either, because symmetry does real work on actions once an action is granted.

$$
\boxed{
\text{invariance can select an action within the variational class; it cannot establish membership in the class}.
}
$$

Given locality, a field content, and a bound on derivative order, invariance can determine an action nearly uniquely — the four-dimensional metric case in [[philosophy/principle-of-least-action/einstein-hilbert-action|the Einstein--Hilbert action]] is the standard demonstration, and the whole method of effective field theory is the general one. This is selection among variational theories, which presupposes variationality rather than deriving it. The distinction is the same one drawn for internal symmetry in [[symmetry-groups-select/reconstruction-versus-selection|gauge reconstruction is not gauge selection]]: a theorem that operates on supplied data does not supply the data.

## Neither is prior in the order of grounding

The two axioms are also independent in their justifications. The reconstruction in [[philosophy/principle-of-least-action/why-an-action-at-all|why there is an action]] derives the form of the action from a composition law on histories and never mentions a group. Whatever grounds the invariance axiom — and this section does not claim to have grounded it — will not be that argument.

The section therefore rests on two axioms rather than one, and the third module is where their conjunction earns its keep.
