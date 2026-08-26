# Covariance Within, Realization Across

The promising “groupoid over a monoid” slogan should be retyped as a two-level architecture: reversible covariance compares presentations within a fixed carrier, while potentially noninvertible realization or transport relates distinct carriers. The slogan is a programme signature until its base, total category, projection, lifts, and composition laws have been constructed.

## Reversible core

Let $\mathcal C$ be a category of presentations and physical processes. Its maximal subgroupoid

$$
\mathcal C^{\simeq}\subseteq\mathcal C
$$

contains the invertible changes of coordinates, gauge, trivialization, or equivalent representation. On a fixed von Neumann algebra, Connes cocycles relating faithful normal semifinite weights provide an important theorem-grade example of such comparison data.

This establishes covariance of modular presentations. It does not establish that all states are physically equivalent, that no physical law may select a state, or that two different physical algebras are merely different weights on one carrier.

## Process direction

Carrier-changing operations may instead lie in

$$
\mathcal C\setminus\mathcal C^{\simeq}.
$$

Examples include proper inclusions, conditional expectations, instruments, record extensions, and some correspondences. Such arrows may supply the one-sided carrier required for orientation; noninvertibility alone does not establish one. The orientation still needs a presentation-independent order and factual persistence.

The safest abstract package is presently one of:

- a category equipped with a wide subgroupoid of presentation equivalences;
- a bicategory of von Neumann algebras and $W^*$-correspondences;
- a double category with equivalences in one direction and processes in the other;
- a pseudofunctor from a directed scale category into a category of context-indexed correspondence prestacks.

Which package is correct depends on the actual wall and descent maps. Calling the base a monoid is justified only if there is one object whose endomorphisms form the relevant scale action. A scale-indexing category or preorder is more general and presently safer.

## The Copernican comparison law

The envisioned architecture is:

$$
\begin{array}{c}
\text{presentation changes inside a carrier}
\quad\leadsto\quad
\text{groupoid covariance},\\[4pt]
\text{transport between carriers}
\quad\leadsto\quad
\text{correspondence or directed process},\\[4pt]
\text{fact and record formation}
\quad\leadsto\quad
\text{additional observational descent}.
\end{array}
$$

The first line has established realizations. The second and third are open in the programme. PC1 and [[program-core/operation-registers|Operations Between Registers]] own the category split; [[spectral-wall-descent/scale-correspondence-stack|the Scale-Correspondence Prestack]] owns the proposed pseudofunctor; and [[algebra/local-global-individuation|Local--Global Individuation]] owns the orientation and record criterion.

The philosophical payoff is exact: objective one-sidedness need not be a failure of covariance. But it becomes physics only when a concrete process arrow, its invariant content, and its relation to records are constructed. [[library/linearization-instabilities-and-crossed-products|Linearization (In)stabilities and Crossed Products]] is especially important here because it shows that compact and boundary-bearing regimes can have genuinely different constraint justifications; a Copernican law must preserve that asymmetry rather than rename it a frame change.
