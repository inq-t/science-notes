# The Noether Synthesis

The third principle is not an axiom but a theorem, and it is what the first two are for. Given an action and a continuous group that leaves that action invariant, every generator yields a current conserved along solutions. The two hypotheses enter at two different places in one identity, so neither can be dropped and neither can substitute for the other. The synthesis also requires more than the plain conjunction of the axioms as ordinarily stated, because the invariance must be of the action rather than of the laws — an upgrade that famous symmetries fail.

## The identity

For a local action $S[\phi]=\int\mathcal L\,\mathrm d^dx$ with Euler--Lagrange expressions $E_a$, the variational axiom supplies an off-shell decomposition of any variation, and the invariance axiom makes the symmetry variation a pure divergence:

$$
\underbrace{\int\partial_\mu K^\mu_k}_{\text{invariance of }S}
\;=\;\delta_kS\;=\;
\int\Bigl(
\underbrace{E_a\,\delta_k\phi^a}_{\text{vanishes on shell}}
+\;\partial_\mu\underbrace{\Theta^\mu[\delta_k\phi]}_{\text{variational structure}}
\Bigr).
$$

With $j^\mu_k:=\Theta^\mu[\delta_k\phi]-K^\mu_k$ this gives $\partial_\mu j^\mu_k=-E_a\,\delta_k\phi^a$ identically, hence

$$
\boxed{
\partial_\mu j^\mu_k=0
\quad\text{on shell},
\qquad k=1,\dots,r .
}
$$

[[what-the-synthesis-requires]] sets out the hypotheses and the two registers the theorem connects: invariance is a property of $S$ over all histories and is off shell, conservation holds along solutions and is on shell, and the transfer runs only in that direction. It also records that a current becomes a number only with boundary control, the honest form being the flux-inclusive balance of [[conservation-of-causal-charge/diagonal-charge-balance|Diagonal Charge Balance]].

## The synthesis is not a plain conjunction

The invariance axiom is naturally stated about laws; the theorem needs it about the action. Kepler's rescaling $\boldsymbol r\mapsto\lambda^2\boldsymbol r$, $t\mapsto\lambda^3t$ maps solutions to solutions and sends $S\mapsto\lambda S$, so it is a symmetry of the laws and yields nothing. The general nesting and its strictness belong to [[philosophy/symmetry-principle/invariance-of-what|invariance of what]]; the consequence here is that the second axiom must be re-typed onto the object the first introduces before the two can be combined at all. That is why the three modules are ordered as they are.

## The converse, and why it matters more than the theorem

[[variational-versus-dynamical-symmetry]] gives the direction usually omitted. For a *normal* variational system there is a one-to-one correspondence between equivalence classes of conservation laws and equivalence classes of variational symmetries. Conservation therefore has no brute instances: in a regular variational theory every conserved quantity has a symmetry as its reason, which is a rare case of the demand in [[sufficient-reason/entry|Sufficing and Necessitating Reason]] being met by a theorem rather than by a programme.

The correspondence needs *symmetry* read broadly. The Runge--Lenz vector is conserved and is the charge of no point symmetry; admitting generalized symmetries, whose generators depend on velocities, restores the bijection. So the second axiom should not be silently restricted to groups acting geometrically.

## Where it stops

[[second-theorem-and-gauge]] handles the case that matters most for this project. A symmetry parameterized by arbitrary functions falls under the second theorem, whose output is off-shell identities among the equations of motion — the contracted Bianchi identity being the gravitational instance — rather than new conserved quantities. Physical charges relocate to boundaries and belong to the transformations acting nontrivially there. Energy in general relativity is consequently not the Noether charge of a time translation, and a conserved integral energy needs extra structure such as a timelike Killing vector, which generic cosmological spacetimes lack.

Degeneracy is the common cause: a gauge system fails the normality condition, so the converse correspondence lapses in exactly the theories where the first theorem was already the wrong instrument.

[[where-the-synthesis-fails]] collects the full register — no action, symmetry of the equations only, discrete symmetry, gauge symmetry, explicit time dependence, non-invariant measure, boundary and fall-off failure, degeneracy. Nearly every entry is live in the setting this project works in, so the correct default is that there is no conservation law until each has been answered.

## Relation to the programme ledger

This module states the general theorem and its hypotheses. The programme's own application of it is owned elsewhere and should not be restated here. [[program-core/symmetry-conservation-and-action|Symmetry, conservation, and action]] keeps Casimir, capacity, charge, and action apart as four types and gives the requirement list in presymplectic rather than Lagrangian form; the two presentations are the same content in different registers, the identity above being the Lagrangian side of it. [[program-core/axioms-and-principles|The axiom and principle ledger]] then records the programme's commitment as construction axiom CA7, which demands precisely a continuous action, a presymplectic or Lagrangian structure, a normalized generator, a moment map or current, and a boundary-flux law before any causal conservation may be claimed. The register in [[where-the-synthesis-fails]] is the general reason that list has the entries it does.

## Claim levels

| Status | Content |
|---|---|
| Exact | the off-shell decomposition $\delta S=\int(E_a\delta\phi^a+\partial_\mu\Theta^\mu)$; the first theorem for a finite-parameter Lie group of variational symmetries, giving on-shell conserved currents; that a symmetry of the equations alone yields none, witnessed by Kepler; the second theorem's off-shell identities for function-parameterized groups; $\nabla^\mu G_{\mu\nu}\equiv0$ as the diffeomorphism Noether identity |
| Exact, hypotheses named | the converse correspondence between conservation laws and variational symmetries, for normal systems with generalized symmetries admitted and trivial classes quotiented; conservation of a charge given flux control; a conserved integral energy given a timelike Killing vector |
| Established but easy to misapply | the first theorem applied to a gauge symmetry returns identically conserved trivialities, not physical charges; improper gauge transformations do carry boundary charges |
| Not delivered by the synthesis | which group; which action; the value of any charge; actuality of an outcome; any conservation law in a theory whose action has not been constructed |
| Open, in this project | whether the causal-wall sector admits an action at all; whether its candidate symmetries are continuous, discrete, or one-sided; the boundary accounting for a causal horizon — see [[conservation-of-causal-charge/theorem-programme|the causal-charge theorem programme]] |
