# The Second Theorem and Gauge

When the invariance group depends on arbitrary functions rather than finitely many parameters, the first theorem does not produce new conserved quantities. It produces differential identities among the equations of motion, holding off shell, which express that the equations are not independent. Physical charges then relocate to the boundary, and they exist only for the transformations that act nontrivially there. This is the structural reason that energy in general relativity is not the Noether charge of a time translation.

## Finite parameters versus arbitrary functions

Noether's first theorem takes an $r$-parameter Lie group and returns $r$ currents. A gauge symmetry is parameterized instead by functions $\varepsilon(x)$ ranging over an infinite-dimensional space, and the second theorem applies. Its output is a set of identities

$$
\boxed{
\mathcal D_a\bigl(E^a\bigr)\equiv0
}
$$

satisfied identically, off shell, for differential operators $\mathcal D_a$ determined by the gauge generators. Nothing here is a conservation law. The identities say that the Euler--Lagrange expressions are functionally dependent, hence that the evolution problem is underdetermined and part of the system is constraint rather than dynamics.

The canonical instance is already recorded in [[philosophy/principle-of-least-action/einstein-hilbert-action|the Einstein--Hilbert action]]: diffeomorphism invariance yields the contracted Bianchi identity

$$
\nabla^\mu G_{\mu\nu}\equiv0 ,
$$

which holds for every metric whatever, solution or not. Covariant stress-energy conservation $\nabla^\mu T_{\mu\nu}=0$ then follows *given* the matter equations, and is a consequence of the identity rather than an independent Noether conservation law.

Applying the first theorem to a gauge symmetry does not fail loudly. It returns a current that is identically conserved for trivial reasons — a so-called improper or trivial conservation law, typically the divergence of an antisymmetric superpotential — and mistaking one of these for physical content is a standard error. Which theorem applies is settled by whether the parameters are constants or functions, which is the classification drawn in [[philosophy/symmetry-principle/which-group|which group]].

## Where the charges go

Gauge charges are not absent; they are relocated. The transformations that fall away as trivial are those approaching the identity at the boundary; those with nontrivial asymptotic or corner behavior — improper gauge transformations — carry genuine charges, expressed as surface integrals rather than volume integrals. The ADM energy and momentum of an asymptotically flat spacetime are of this kind, and so are the corner charges that appear in covariant phase space treatments.

Two consequences follow for the larger programme.

Energy in general relativity is not the Noether charge of a global time translation, because there is no global time translation to be a symmetry — diffeomorphism invariance is local. A conserved integral energy requires additional structure, a timelike Killing vector being the standard sufficient condition, and generic cosmological spacetimes have none. Statements about energy conservation in cosmology must therefore name the structure they are using.

And the vault's conservation programme inherits exactly this shape. [[conservation-of-causal-charge/indiscernibility-and-the-noether-gap|Indiscernibility and the Noether Gap]] classifies four distinct outputs of the word *symmetry* and records that a gauge symmetry generally produces a constraint with charges at boundaries; [[conservation-of-causal-charge/causal-individuation-balance|Causal-Individuation Balance]] then conjectures a diagonal causal charge whose gravitational contribution is precisely of the boundary type. The present note supplies the general reason those charges must be sought at boundaries rather than in the bulk.

## Degeneracy is the common cause

The second theorem and the failure of the converse in [[variational-versus-dynamical-symmetry]] have one source. A gauge theory's Euler--Lagrange system is degenerate: the identities above are exactly the failure of the maximal-rank condition that normality requires. So a gauge theory is a system in which conservation laws are not in bijection with symmetries, the first theorem is not the right instrument, and the honest accounting runs through constraints, boundary terms, and a quotient by the redundancy — which is where this section rejoins [[philosophy/indiscernibility-of-identicals/rigidity-and-surplus-structure|surplus structure]] and the question of what a quotient is entitled to forget.
