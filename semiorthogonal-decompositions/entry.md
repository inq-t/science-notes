# Semiorthogonal Decompositions as Categorical Walls

A semiorthogonal decomposition separates a category into sectors that are orthogonal in one direction but may still extend one another in the reverse direction. This is exact mathematics for an asymmetric presentation of a richer whole: after admissibility is proved, an idempotent projection can retain one sector and annihilate another, while the ambient category still records both. For the foundational programme this is worth exploring as a **categorical first stage** of a wall, not yet as a quantum channel, entropy law, or physical measurement.

## The meaning

An orthogonal direct sum says that two sectors cannot see one another in either direction. A semiorthogonal decomposition is subtler. It says that one direction of derived morphism vanishes while the reverse direction may carry extensions:

$$
\mathcal T=\langle\mathcal A,\mathcal B\rangle,
\qquad
\operatorname{RHom}_{\mathcal T}(B,A)\simeq0,
\qquad
\operatorname{RHom}_{\mathcal T}(A,B)
\text{ need not vanish}.
$$

Thus the whole is ordered without being split into unrelated pieces. The order is an **asymmetry of composability**. It is not temporal order by itself, but it is the kind of prior structure from which a directed presentation or selection rule could be constructed.

When the components are admissible, every object \(X\in\mathcal T\) has a functorial projection triangle

$$
B_X\longrightarrow X\longrightarrow A_X\longrightarrow B_X[1],
\qquad
A_X\in\mathcal A,
\quad
B_X\in\mathcal B.
$$

Write \(\pi_{\mathcal A}:\mathcal T\to\mathcal A\) for \(X\mapsto A_X\) and \(P_{\mathcal A}:=i_{\mathcal A}\pi_{\mathcal A}\) for the associated endofunctor of \(\mathcal T\). Then \(P_{\mathcal A}\) is exact and idempotent. It is genuinely noninvertible if \(\mathcal B\ne0\), because it sends every object of \(\mathcal B\) to zero. The exact hypotheses and variance conventions are recorded in [[semiorthogonal-decompositions/definitions-and-projections|definitions and projections]].

## Three structures that must not be conflated

| Structure | What it says | Reversible? |
|---|---|---|
| Semiorthogonality | \(\operatorname{RHom}(\mathcal B,\mathcal A)=0\) | It is a property, not an evolution |
| Admissible projection or Verdier quotient | A functor retains one component and kills the other | Generally no |
| Mutation | The ordered decomposition is changed by an adjoint-cone construction | Reversible on the mutated components under the standard hypotheses |

The distinction is decisive. Semiorthogonality alone is not forgetting. A mutation is normally a re-presentation of categorical data, not its destruction. Noninvertibility enters through a specified projection or quotient.

## Why this is worth exploring

The project presently asks one construction to do two different jobs:

1. identify which distinctions belong to the presented sector; and
2. realize their loss by a positive, state-preserving analytic map.

Semiorthogonal decomposition can make the first job exact before the second is solved. It offers:

- a rigorous one-sided selection law rather than a symmetric block decomposition;
- an idempotent categorical projector when admissibility holds;
- mutation and recollement as controlled ways to compare neighboring presentations;
- natural contact with \(A_2\) quivers, vanishing cycles, braid phenomena, and exceptional collections; and
- additive splittings of invariants such as algebraic \(K\)-theory and Hochschild homology under the appropriate enhanced hypotheses.

The elementary [[semiorthogonal-decompositions/mutations-recollement-and-a2|\(A_2\)-quiver example]] shows the asymmetry explicitly: one derived morphism direction vanishes while a nontrivial extension survives in the other direction.

## The proposed place in the wall architecture

The honest programme has two distinct arrows:

$$
\underbrace{
\mathcal T\xrightarrow{\ \pi_{\mathcal A}\ }\mathcal A
}_{\text{categorical selection}}
\quad\dashrightarrow\quad
\underbrace{
(\mathcal M,\varphi)
\xrightarrow{\ E\ }
(\mathcal N,\varphi|_{\mathcal N})
}_{\text{analytic realization}}.
$$

The first arrow may be an admissible projection or a dg/Verdier quotient. The second must be a normal completely positive map, preferably a \(\varphi\)-preserving conditional expectation when the modular hypotheses allow one. The dashed arrow is the missing realization theorem.

Accordingly, a semiorthogonal decomposition does **not** bypass the Takesaki gate in [[spectral-wall-descent/conditional-expectation-balance|conditional expectation balance]]. It can instead explain why a particular observable subcategory should be selected before asking whether that selection has a completely positive operator-algebraic realization. The complete obligation ledger is in [[semiorthogonal-decompositions/categorical-wall-interface|the categorical wall interface]].

## Relation to the present source corpus

[[library/hodge-atoms-spectral-triples-bps/entry|Raugas]] places a Kuznetsov semiorthogonal component, a proposed dynamical selection rule, and JLO/index language in one discussion. The categorical decomposition is standard; the promotion of its one-sided \(\operatorname{RHom}\)-vanishing to a physical tunnelling prohibition is explicitly conjectural. Moreover, a semiorthogonal decomposition of a dg category does not by itself produce a spectral triple or JLO cocycle.

The safe synthesis with [[spectral-wall-descent/index-and-curvature-transgression|index and curvature transgression]] is therefore conditional: first realize the categorical components in analytic \(K\)-homology or spectral data, then ask whether the JLO character and index pairings split or transgress compatibly. Additivity of an abstract invariant is not yet a physical conservation law.

## Claim status

- **[STANDARD MATHEMATICS]** Semiorthogonal decompositions, admissibility, projection triangles, mutations, Verdier quotients, and recollement under the stated hypotheses.
- **[EXACT EXAMPLE]** The directed \(A_2\)-quiver calculation.
- **[PROPOSED PROJECT ROLE]** A semiorthogonal projection as the categorical first stage of a causal or observational wall.
- **[OPEN CONSTRUCTION]** A functorial realization by \(C^*\)- or von Neumann algebra data carrying a faithful state, completely positive expectation, BKM metric, and modular covariance.
- **[NOT DERIVED]** Physical time, irreversible dynamics, entropy production, spacetime curvature, or quantum measurement from semiorthogonality alone.

The foundational and authoritative literature used here is classified in [[semiorthogonal-decompositions/sources-and-status|sources and status]].
