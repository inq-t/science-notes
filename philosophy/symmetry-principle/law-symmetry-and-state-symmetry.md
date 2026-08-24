# Law Symmetry and State Symmetry

A symmetric law does not require symmetric solutions; it requires that the *set* of solutions be symmetric. Individual solutions may carry none of the group, and the orbit structure of the solution set is where the invariance survives. This separates two things routinely conflated under the phrase "symmetry breaking": explicit breaking, in which the action is not invariant, and spontaneous breaking, in which it is and the realized state is not. Only the first destroys a conservation law.

## Curie's principle, stated so that it is true

The slogan that the symmetries of a cause reappear among its effects is false of individual effects and true of the effect *set*. If $G$ preserves the equations, then $g$ maps solutions to solutions, so

$$
\phi\ \text{a solution}
\;\Longrightarrow\;
\Phi_g\phi\ \text{a solution},
$$

and the solution set is a union of $G$-orbits. Nothing forces any orbit to be a fixed point. A rotationally invariant equation admits solutions that single out a direction, provided the rotated versions are solutions too.

The correct statement is therefore about closure under the group, not about the invariance of what obtains. Read as a claim about individual outcomes, Curie's principle is simply false, and the buckling of a symmetric column is enough to refute it.

## Explicit and spontaneous breaking are different phenomena

| | Action invariant | Realized state invariant | Noether current |
|---|---|---|---|
| unbroken | yes | yes | conserved |
| spontaneously broken | yes | no | still conserved |
| explicitly broken | no | not required | not conserved |

The middle row is the one that matters and the one the vocabulary obscures. When breaking is spontaneous the action retains its full invariance, so the hypothesis of Noether's theorem is untouched and the current remains conserved; what fails is that the ground state is not a fixed point of the group, and the degenerate vacua form an orbit. In infinite volume the *charge* — the spatial integral of the conserved density — may fail to be well defined even though the current's divergence still vanishes. For a spontaneously broken continuous **global** symmetry in three or more spacetime dimensions there are in addition Goldstone modes along the orbit; a broken gauge symmetry produces none in the spectrum, and in two dimensions the phenomenon is forbidden outright.

Only explicit breaking touches the conservation law, because only explicit breaking touches the action. It does not follow that the realized state is then asymmetric: the damped oscillator's rest solution $x\equiv0$ is time-translation invariant while its action is not, so the third row's middle entry records what is typical rather than what is entailed. The time-dependent Lagrangian of the damped oscillator in [[philosophy/principle-of-least-action/variational-is-a-restriction|variationality is a restriction]] is explicit breaking of time-translation invariance, and that is exactly why the energy is not conserved there.

## Invariance survives as orbit structure, not as fixed points

The general pattern is the one this section has already met. An unpointed object can be fully $G$-symmetric while every choice of point on it is not, and choosing a point reduces the manifest symmetry to a stabilizer without removing the group. That is the torsor picture of [[philosophy/indiscernibility-of-identicals/rigidity-and-surplus-structure|rigidity and surplus structure]], where invariant functions are constant while every difference is canonical, and it is the retyping of facthood as pointing developed in [[conservation-of-causal-charge/facthood-and-symmetry-breaking|Facthood and Symmetry Breaking]].

Two consequences follow for how a symmetry claim should be read.

A symmetry claim is not refuted by an asymmetric observation. The observation is a section; the claim is about the bundle. Refuting it requires showing that the rotated situation is *not* available, which is a much stronger finding than that it is not the one at hand.

A symmetry claim is also not confirmed by a symmetric observation, since a symmetric configuration is compatible with laws having no symmetry at all — the first row of [[invariance-of-what]]. Neither direction of naive inference from states to laws is valid, and both are common.

## What this leaves for the synthesis

For the third module the relevant residue is narrow and clean. Noether's hypothesis concerns the action and is untouched by whether the state realizes the symmetry, so the theorem applies unchanged to a spontaneously broken theory. The question of which fact obtains within a symmetric orbit is not a question this axiom answers, and it is not one the conservation law answers either; it is the pointing problem of [[sufficient-reason/facticity-and-pointing|Facticity and Pointing]], and the programme's statement of the same retyping is the closing section of [[program-core/symmetry-conservation-and-action|Symmetry, conservation, and action]].
