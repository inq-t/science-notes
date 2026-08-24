# The Second Theorem and Gauge

When the invariance group depends on arbitrary functions rather than finitely many parameters, the first theorem does not produce new conserved quantities. It produces differential identities among the equations of motion, holding off shell, which express that the equations are not independent. Physical charges then relocate to the boundary, and belong only to the transformations acting nontrivially there.

## Finitely many parameters versus arbitrary functions

Noether's first theorem takes a group with $r$ parameters and returns $r$ currents. A gauge symmetry is parameterized instead by functions $\varepsilon^r(x)$ ranging over an infinite-dimensional space, and the second theorem applies. Its output is one identity per gauge parameter,

$$
\boxed{
\mathcal D^a_r\bigl(E_a\bigr)\equiv0 ,
}
$$

with $r$ indexing the gauge generators and $\mathcal D^a_r$ differential operators determined by them. These hold identically, off shell, for every field configuration whatever. Nothing here is a conservation law. The identities say that the Euler--Lagrange expressions are differentially dependent — the count of identities is the count of dependencies — so the system is under-determined and part of it is constraint rather than evolution.

The canonical instance is recorded in [[philosophy/principle-of-least-action/einstein-hilbert-action|the Einstein--Hilbert action]]: diffeomorphism invariance yields the contracted Bianchi identity $\nabla^\mu G_{\mu\nu}\equiv0$, which holds for every metric, solution or not. The covariant stress-energy conservation noted there is therefore a consequence of an identity and not an independent Noether law. Two routes reach it and should not be crossed: from the Bianchi identity together with the *gravitational* field equations, or, independently of whether those hold, from the diffeomorphism Noether identity of the *matter* action alone once the matter equations are satisfied.

Applying the first theorem to a gauge symmetry does not fail loudly. It returns a current that is conserved on shell for trivial reasons — on shell it is the divergence of an antisymmetric superpotential, and for Maxwell with $\delta A_\mu=\partial_\mu\varepsilon$ one finds $j^\mu=-F^{\mu\nu}\partial_\nu\varepsilon\approx\partial_\nu(\varepsilon F^{\nu\mu})$. The triviality is on-shell, not an off-shell identity, and mistaking such a current for physical content is a standard error. Which theorem applies is settled by the parameter count, as classified in [[philosophy/symmetry-principle/which-group|which group]].

## Where the charges go

Gauge charges are not absent; they are relocated. Transformations approaching the identity at the boundary fall away as trivial; those with nontrivial asymptotic or corner behavior — improper gauge transformations — carry genuine charges, expressed as surface integrals rather than volume integrals. The ADM energy and momentum of an asymptotically flat spacetime are of this kind, and so are the corner charges of covariant phase space treatments.

Hence the precise statement about energy in general relativity. It is not a *bulk* first-theorem Noether charge, because diffeomorphism invariance is local. Where boundary conditions supply an asymptotic time translation it is the corresponding *surface* charge, which is what ADM energy is. A conserved *volume* integral requires further structure, a timelike Killing vector being the standard sufficient condition, and generic cosmological spacetimes have none — so statements about energy conservation in cosmology must name the structure they use.

The vault's conservation programme inherits this shape. [[conservation-of-causal-charge/indiscernibility-and-the-noether-gap|Indiscernibility and the Noether Gap]] classifies four distinct outputs of the word *symmetry* and records that a gauge symmetry generally produces a constraint with charges at boundaries; [[conservation-of-causal-charge/causal-individuation-balance|Causal-Individuation Balance]] then conjectures a diagonal causal charge whose gravitational contribution is precisely of the boundary type.

## Degeneracy is the common cause

The second theorem and the failure of the converse in [[variational-versus-dynamical-symmetry]] have one source. The identities above are exactly the under-determinacy that defeats normality: a gauge system cannot be put in Cauchy--Kovalevskaya form, so the hypothesis the converse needs is absent. A gauge theory is thus a system in which conservation laws are not in bijection with symmetries, the first theorem is the wrong instrument, and the accounting runs through constraints, boundary terms, and a quotient by the redundancy — where this section rejoins [[philosophy/indiscernibility-of-identicals/rigidity-and-surplus-structure|surplus structure]] and the question of what a quotient is entitled to forget.
