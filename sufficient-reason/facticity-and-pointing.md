# Facticity and Pointing

A fact in a commutative context is a character, hence a multiplicative evaluation at one point of the context's spectrum. This is stronger than the existence of elements, stronger than the existence of a state, and different from purity: a pure state of a noncommutative algebra can be extremal without assigning multiplicative values to all observables.

## Characters are points

For a commutative unital C\*-algebra $\mathcal D$, Gelfand duality gives

$$
\mathcal D\cong C(X),
\qquad
X=\operatorname{Hom}_{*}(\mathcal D,\mathbb C).
$$

Each $x\in X$ defines the character

$$
\chi_x(d)=\widehat d(x),
\qquad
\chi_x(d_1d_2)=\chi_x(d_1)\chi_x(d_2).
$$

Within the context $\mathcal D$, a character is a simultaneous value assignment compatible with the algebraic relations. The equation “a fact is a character” is therefore context-relative: it concerns the commuting quantities in $\mathcal D$, not a global valuation of every element of a noncommutative $\mathcal M$.

## Purity is not multiplicativity

For $\mathcal M=M_n(\mathbb C)$, a unit vector $\psi$ defines the pure state

$$
\omega_\psi(A)=\langle\psi,A\psi\rangle.
$$

Purity means that $\omega_\psi$ is extremal in the convex state space. It does not imply

$$
\omega_\psi(AB)=\omega_\psi(A)\omega_\psi(B).
$$

Indeed,

$$
\omega_\psi(A^2)-\omega_\psi(A)^2
=\operatorname{Var}_\psi(A)
$$

is generally nonzero. When $n\ge2$, $M_n(\mathbb C)$ has no characters: a nonzero homomorphism to $\mathbb C$ would have a two-sided kernel, but simplicity makes it injective, which is impossible into a one-dimensional algebra.

Thus three notions must remain separate:

| Notion | Formal expression | What it provides |
|---|---|---|
| State | positive normalized linear functional | expectations |
| Pure state | extremal state | no nontrivial convex decomposition |
| Character | multiplicative state | a point-valued assignment in a commutative algebra |

A pure quantum state is maximally extremal but not a global classical point.

## Non-emptiness is not pointing

A set may have many elements without possessing a distinguished element. A $G$-torsor makes this exact: it is locally indistinguishable from $G$ acting on itself, but it has no preferred identity until a point or section is chosen. In geometric settings, the obstruction to a global section is measured by an $H^1$-class.

This supplies an analogy, not an identification, for contextual quantum valuations. In the spectral-presheaf formulation of Kochen--Specker, spectra exist in individual commutative contexts while no compatible global section exists. The relevant failure is therefore not emptiness in each context but global pointing across contexts.

The analogy must not be overextended. A torsor, a sheaf obstruction, and a quantum state are different structures; an exact comparison would require a functor preserving their respective notions of section and compatibility.

## Atomlessness in local quantum field theory

Local algebras in algebraic QFT are often modeled by type III factors. Such algebras have no minimal projections, no normal pure states, and no faithful normal trace. This strengthens the separation between a normal physical state and an atomic point description. It does not eliminate commutative subalgebras or their characters; that separate fact is treated in [[necessity-and-nonemptiness]].
