# Algebra and Coalgebra as Forms of Ground

Initial algebras formalize construction from generators, while final coalgebras formalize behavior through indefinite observation. They provide a precise candidate language for necessitating and sufficing reason, respectively, but the correspondence remains a proposed representation until a quantum readout functor and an operational equivalence theorem are constructed.

## The dual fixed-point forms

Let $F:\mathcal C\to\mathcal C$ be an endofunctor.

An $F$-algebra is a pair $(X,\alpha)$ with

$$
\alpha:F(X)\to X.
$$

When an initial $F$-algebra exists, it is the least fixed point in the relevant sense. It supports construction, well-founded recursion, and induction.

An $F$-coalgebra is a pair $(X,\gamma)$ with

$$
\gamma:X\to F(X).
$$

When a final $F$-coalgebra exists, it represents complete observable behavior. It supports unfolding, coinduction, and behavioral identity by bisimulation.

| | Initial algebra | Final coalgebra |
|---|---|---|
| Structural map | $F(X)\to X$ | $X\to F(X)$ |
| Governing idea | construction | observation |
| Proof principle | induction | coinduction |
| Equality | generated structural equality | bisimulation |
| Typical foundedness | well-founded | permits non-well-founded behavior |

Group versus semigroup does not follow from this table. An algebra can encode irreversible operations, and a coalgebraic transition can be reversible. Any identification of construction with group action or observation with one-sided action needs a separate bridge.

## Lambek's lemma

If $(Z,\zeta)$ is an initial algebra or final coalgebra, its structure map is an isomorphism. For a final coalgebra,

$$
\zeta:Z\xrightarrow{\sim}F(Z).
$$

This says that the carrier of final behavior is isomorphic to one layer of its own unfolding. It does not say that every coalgebra map $\gamma:X\to F(X)$ is invertible, nor that a physical transition is irreversible while the universe as a whole is reversible. That reading is a suggestive interpretation requiring a specified $F$ and a physical meaning for one unfolding step.

## Bisimulation and the identity of indiscernibles

For a coalgebra, bisimulation identifies states whose observable unfoldings cannot be distinguished. This resembles Leibniz's identity of indiscernibles, but the resemblance becomes a physical result only if

$$
x\sim_{\mathrm{bisim}}y
\quad\Longleftrightarrow\quad
x\sim_{\mathrm{operational}}y.
$$

The right side must quantify over the measurements physically available at a wall or readout context. Proving this equivalence is the core identity test in [[theorem-programme]].

## The missing behavior functor

The intended coalgebra should encode at least:

1. selection or availability of a commutative context $\mathcal D\subseteq\mathcal M$;
2. restriction of a state to that context;
3. the resulting probability law on $\operatorname{Spec}(\mathcal D)$; and
4. repeated observation or state update.

A schematic candidate is a context-indexed composite involving a probability construction and the spectrum functor. The variance, covariance, and naturality of those components matter: spectrum is contravariant, state restriction reverses inclusions, and quantum state update is not determined by a probability law alone. Until these types are made exact, “sufficing reason is a final coalgebra” is a programme conjecture.
