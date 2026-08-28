---
inq.module: "coalgebras"
inq.include:
  - "**/*.md"
---
# Coalgebras

A coalgebra presents structure by **decomposition or observation** rather than by combination. The word has two standard meanings. A linear coalgebra has maps $C\to C\otimes C$ and $C\to k$ dual in direction to multiplication and unit; it is fundamental to affine group schemes and their representations. An $F$-coalgebra is a state space equipped with a map $X\to F(X)$ that exposes one step of behavior; it is fundamental to transition systems, bisimulation, and coinduction. The two meanings share an arrow-reversal pattern, but they belong to different theories and must not be silently identified.

## Structure read outward

An algebra is usually specified by operations that take pieces **inward** to a result. For example, an associative $k$-algebra has multiplication

$$
m:A\otimes_k A\longrightarrow A
$$

and a unit $u:k\to A$. A linear coalgebra reverses these arrows: it sends one element outward toward two components and toward a scalar. A categorical $F$-coalgebra likewise sends a state outward to its immediately observable shape.

This common orientation is suggestive, but it is not a universal definition of “coalgebra.” The tensor product in the first theory and the endofunctor $F$ in the second perform different jobs. Whenever the word appears, the first question should therefore be:

> Coalgebra for which monoidal product or for which endofunctor?

Without that datum, the term does not yet determine a mathematical object.

## Linear coalgebras

Let $k$ be a field. A **coalgebra over $k$** is a $k$-vector space $C$ with a comultiplication and counit

$$
\Delta:C\longrightarrow C\otimes_k C,
\qquad
\varepsilon:C\longrightarrow k,
$$

satisfying coassociativity

$$
(\Delta\otimes \operatorname{id}_C)\circ\Delta
=
(\operatorname{id}_C\otimes\Delta)\circ\Delta
$$

and the counit identities

$$
(\varepsilon\otimes\operatorname{id}_C)\circ\Delta
=
\operatorname{id}_C
=
(\operatorname{id}_C\otimes\varepsilon)\circ\Delta,
$$

using the canonical identifications $k\otimes C\cong C\cong C\otimes k$.

Conceptually, $Delta(c)$ records all the correlated left and right components into which $c$ decomposes. It need not be a simple tensor $c_1\otimes c_2$; Sweedler notation

$$
\Delta(c)=\sum c_{(1)}\otimes c_{(2)}
$$

suppresses what may be a genuine sum. The counit is not an inverse to $\Delta$. It says that discarding either component in the prescribed way leaves the original element.

More generally, a coalgebra object is a **comonoid object** in a monoidal category. This formulation exposes exactly what has been dualized: a monoid object has arrows $A\otimes A\to A$ and $\mathbb{1}\to A$, whereas a comonoid object has arrows $C\to C\otimes C$ and $C\to\mathbb{1}$.

### Affine groups become Hopf algebras

The most important algebraic-geometric example comes from reversing geometric maps by pulling back functions. If $G$ is an affine group scheme over $k$, its coordinate ring $\mathcal O(G)$ is a commutative algebra. The group multiplication, identity, and inverse

$$
G\times G\longrightarrow G,
\qquad
\operatorname{Spec}k\longrightarrow G,
\qquad
G\longrightarrow G
$$

induce maps in the opposite direction

$$
\Delta:\mathcal O(G)\longrightarrow
\mathcal O(G)\otimes_k\mathcal O(G),
\qquad
\varepsilon:\mathcal O(G)\longrightarrow k,
\qquad
S:\mathcal O(G)\longrightarrow\mathcal O(G).
$$

Together with the ordinary algebra structure, these make $\mathcal O(G)$ a commutative **Hopf algebra**. The coalgebra structure remembers how a function evaluates on a product of group elements:

$$
(\Delta f)(g,h)=f(gh).
$$

For the multiplicative group $\mathbb G_m$,

$$
\mathcal O(\mathbb G_m)=k[t,t^{-1}],
\qquad
\Delta(t)=t\otimes t,
\qquad
\varepsilon(t)=1,
\qquad
S(t)=t^{-1}.
$$

For the additive group $\mathbb G_a$,

$$
\mathcal O(\mathbb G_a)=k[x],
\qquad
\Delta(x)=x\otimes 1+1\otimes x,
\qquad
\varepsilon(x)=0,
\qquad
S(x)=-x.
$$

These formulas distinguish two useful kinds of elements in a Hopf algebra: $t$ is **group-like**, with $\Delta(t)=t\otimes t$, while $x$ is **primitive**, with $\Delta(x)=x\otimes1+1\otimes x$.

A right **comodule** over $C$ is a vector space $V$ with a coaction

$$
\rho:V\longrightarrow V\otimes C
$$

obeying analogues of coassociativity and the counit law. Representations of an affine group scheme $G$ are encoded by comodules over $\mathcal O(G)$. Thus the coalgebra is not decorative extra structure on the coordinate ring: it is what lets algebraic functions carry the group action. This connects coalgebras to [[basic-concepts/torsors/inq|torsors]], [[basic-concepts/groupoids/inq|groupoids]], and quotient constructions.

### Duality has a finiteness boundary

If $A$ is a finite-dimensional $k$-algebra, the linear dual $A^*=\operatorname{Hom}_k(A,k)$ is naturally a coalgebra: the transpose of multiplication lands in

$$
(A\otimes A)^*\cong A^*\otimes A^*.
$$

For infinite-dimensional $A$, the displayed identification generally fails. The transpose of multiplication lands in $(A\otimes A)^*$, which is usually larger than $A^*\otimes A^*$. One may need a finite dual, a restricted dual, or a topology and completed tensor product. “Coalgebra is the dual of algebra” is therefore a reliable guide to the axioms, not an unrestricted construction theorem.

## Coalgebras for an endofunctor

Let $F:\mathcal C\to\mathcal C$ be an endofunctor. An **$F$-coalgebra** is an object $X$ with a structure map

$$
\gamma:X\longrightarrow F(X).
$$

Here $X$ is a space of states and $\gamma$ reveals one layer of observable behavior. The choice of $F$ determines what one observation contains. It may expose an output and a successor, a family of labelled successors, a probability distribution, or some other prescribed shape.

A morphism of $F$-coalgebras

$$
h:(X,\gamma)\longrightarrow(Y,\delta)
$$

is a map $h:X\to Y$ satisfying

$$
F(h)\circ\gamma=\delta\circ h.
$$

This equation says that translating a state and then observing it gives the same result as observing it first and translating the exposed successors. Coalgebra morphisms preserve behavior, not merely the underlying set or space.

### Streams

Fix an alphabet $A$ and take

$$
F(X)=A\times X.
$$

An $F$-coalgebra assigns to every state an output in $A$ and a next state. The set of infinite streams $A^{\mathbb N}$, equipped with head and tail,

$$
A^{\mathbb N}\longrightarrow A\times A^{\mathbb N},
$$

is the canonical space of complete behaviors. Every machine $\gamma:X\to A\times X$ determines a stream from each initial state by repeated observation.

### Automata and transition systems

For deterministic automata with input alphabet $A$ and Boolean acceptance output, one uses

$$
F(X)=2\times X^A.
$$

The structure map says whether a state accepts the empty word and gives one successor for each input symbol. Its complete behavior is the language accepted from that state.

A labelled nondeterministic transition system can instead be modeled, subject to size choices, by

$$
F(X)=\mathcal P(A\times X),
$$

where $\mathcal P$ is a power-set functor. Probabilistic systems use an appropriate distribution functor. These examples show why $F$ cannot be omitted: determinism, nondeterminism, labels, and probabilities are different behavioral signatures.

## Final coalgebras and complete behavior

A **final $F$-coalgebra** is a terminal object $(\nu F,\zeta)$ in the category of $F$-coalgebras. For every $(X,\gamma)$ there is a unique coalgebra morphism

$$
\operatorname{beh}_\gamma:X\longrightarrow\nu F.
$$

This map sends a state to its complete observable behavior. Two states are behaviorally equivalent when they have the same image under it. For the stream functor $A\times-$, the final coalgebra is $A^{\mathbb N}$; the behavior map unfolds a machine into the stream it produces.

If a final coalgebra exists, **Lambek's lemma** implies that its structure map

$$
\zeta:\nu F\overset{\sim}{\longrightarrow}F(\nu F)
$$

is an isomorphism. This expresses self-similarity: a complete behavior consists of one observable layer together with complete successor behavior. It does **not** say that every transition in every $F$-coalgebra is reversible.

Final coalgebras do not exist for every endofunctor on every category. Their existence is a theorem requiring hypotheses, a construction, or both. Large branching functors can also create size obstructions; for example, the unrestricted covariant power-set functor on sets has no final coalgebra as an ordinary set. One should never infer existence merely from writing the symbol $\nu F$.

## Bisimulation and coinduction

A **bisimulation** relates states whose observations can continue to match step by step. For a deterministic stream system, a relation $R\subseteq X\times X$ is a bisimulation when related states have the same output and their successors are again related. The **coinduction principle** then permits a global equality of behaviors to be proved from this locally self-renewing relation.

The slogan is useful:

$$
\text{induction proves properties of constructed objects,}
$$

$$
\text{coinduction proves equivalence of observed behaviors.}
$$

But the general relation between bisimilarity and equality in a final coalgebra depends on properties of $F$ and on which notion of relation lifting is used. Weak-pullback preservation is one common sufficient hypothesis in set-based accounts. “Bisimilar” and “behaviorally equivalent” should not be declared synonymous without checking the setting.

## Initial algebras and final coalgebras

For the same endofunctor $F$, an $F$-algebra has the opposite orientation

$$
\alpha:F(A)\longrightarrow A.
$$

An **initial algebra** admits a unique homomorphism *out* to every other $F$-algebra; it supports folds and structural induction. A **final coalgebra** admits a unique homomorphism *in* from every other $F$-coalgebra; it supports unfolds and coinduction. In favorable examples, the former captures finite, well-founded constructions while the latter captures potentially infinite behavior.

This contrast is structural, not automatically metaphysical. “Initial” and “final” refer to universal mapping properties in specified categories. Neither word by itself means temporally first, causally ultimate, necessary, nonempty, or physically real.

## Nearby notions that are not coalgebras

- A **comonad** is an endofunctor equipped with natural transformations $G\to G^2$ and $G\to\operatorname{Id}$. One can speak of coalgebras *for* a comonad, but the comonad and each of its coalgebras are different data.
- A **$C^*$-algebra**, von Neumann algebra, or algebra of observables is an algebra in the operator-algebraic sense. It is not a coalgebra merely because it describes a dynamical system.
- A flow or semigroup action $X\to X$ may be packaged coalgebraically only after an appropriate endofunctor and observation type have been chosen.
- A [[basic-concepts/sheafs/inq|sheaf]] organizes compatible local data over varying regions. A coalgebra organizes decomposition or behavior. A sheaf may take values in coalgebras, but neither notion entails the other.
- A [[basic-concepts/stacks/inq|stack]] records objects with automorphisms satisfying descent. The “coalgebra of behaviors” and the “stack of locally gluable objects” solve different structural problems.

## Why coalgebras matter here

The project uses coalgebra primarily in the endofunctorial, behavioral sense. The proposal in [[sufficient-reason/algebra-and-coalgebra|Algebra and coalgebra]] is that a completed account of sufficing reason should be final among systems that expose the same observable structure. On that reading, the idea is not simply that the cosmos evolves. It is that every admissible presentation of the relevant behavior should have a unique behavior-preserving map into one universal semantic object.

That proposal becomes mathematically definite only after supplying at least:

1. a category $\mathcal C$ of candidate systems;
2. an endofunctor $F$ specifying exactly what one observable layer contains;
3. the intended morphisms and their physical or logical meaning;
4. an existence proof for a final $F$-coalgebra;
5. a proof that the resulting behavioral equivalence matches the intended operational indistinguishability.

The present project explicitly records these as open obligations in [[sufficient-reason/theorem-programme|Theorem programme]]. In particular, context selection, outcomes, and probabilities cannot be gestured at as “the behavior functor”; they have to be typed as actual components of $F$. Likewise, [[sufficient-reason/necessity-and-nonemptiness|Necessity and nonemptiness]] distinguishes a finality theorem from the further claims that the final object exists, is nonempty, is unique in the intended physical category, or is metaphysically necessary.

Coalgebra is valuable here because it sharpens a genuine distinction:

$$
\text{what a system is made from}
\quad\neq\quad
\text{how its behavior can be observed indefinitely}.
$$

It does not by itself close the gap between those descriptions. Its contribution is to state exactly what a behavioral closure claim would have to prove.
