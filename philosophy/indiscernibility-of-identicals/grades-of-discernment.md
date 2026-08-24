# Grades of Discernment

Discernment by a monadic property, by an asymmetric relation, and by an irreflexive relation form a strictly increasing hierarchy, and the identity of indiscernibles has a different truth value at each grade. Automorphism orbits are exactly the classes of the invariant monadic family and are contained in those of the definable one, which is why symmetric structures are the standard counterexamples at the strongest grade; the weaker grades survive some symmetries and not others, and must be checked one at a time. The weakest grade grounds identity only in a language from which identity has been excluded; otherwise it is circular.

## Three grades

Let $X$ carry a structure and let the admissible formulas be those of its language. Distinct $a,b\in X$ are:

- **absolutely discernible** when some one-place $\varphi$ satisfies $\varphi(a)\wedge\neg\varphi(b)$;
- **relatively discernible** when some two-place $\varphi$ satisfies $\varphi(a,b)\wedge\neg\varphi(b,a)$;
- **weakly discernible** when some two-place $\varphi$ is irreflexive and satisfies $\varphi(a,b)$.

The implications

$$
\text{absolute}\Longrightarrow\text{relative}\Longrightarrow\text{weak}
$$

are immediate. From an absolute $\varphi$ set $\psi(x,y)=\varphi(x)\wedge\neg\varphi(y)$; from a relative $\varphi$ set $\psi(x,y)=\varphi(x,y)\wedge\neg\varphi(y,x)$. In each case $\psi$ is irreflexive and holds of the pair. Irreflexivity is what does the work at the last grade: from $\neg\psi(a,a)$ and $\psi(a,b)$ it follows that $b\neq a$, so weak discernibility entails numerical distinctness without exhibiting any property that one has and the other lacks.

Both implications are strict. In $(\mathbb Z,<)$ the translations act transitively, so no invariant monadic formula separates any two integers, while $<$ orders every pair: relative but not absolute. On $X=\{a,b\}$ with the single relation $R=\{(a,b),(b,a)\}$ the transposition is an automorphism, so no formula can hold of $(a,b)$ and fail of $(b,a)$, while $R$ itself is irreflexive and holds of the pair: weak but not relative.

Each grade indexes its own version of the principle. A structure may satisfy the identity of indiscernibles weakly and violate it absolutely, and this is the ordinary situation for symmetric configurations.

## The circularity trap at the weakest grade

If the language contains identity, then $x\neq y$ is itself irreflexive, and any two distinct elements are weakly discernible by it. The weakest grade is then a tautology and grounds nothing. Weak discernibility is informative only when identity is *excluded* from the primitive vocabulary — that is, only when the point of the exercise is to construct identity from structure rather than to presuppose it. Any appeal to it must therefore declare the primitive relations and show that the witnessing relation is among them rather than definable from equality.

## Orbits and invariants

Two monadic families are in play at the absolute grade and they must not be run together. Let $G=\operatorname{Aut}(X)$, let $\mathcal F_{\mathrm{inv}}$ be *all* $G$-invariant maps $X\to\mathbb C$, and let $\mathcal F_{\mathrm{def}}$ be the indicators $1_{\varphi(X)}$ of the subsets defined by a one-place formula over $\varnothing$, so that $x\equiv_{\mathcal F_{\mathrm{def}}}y$ says exactly that $x$ and $y$ have the same complete $1$-type. Every definable map is invariant, so $\mathcal F_{\mathrm{def}}\subseteq\mathcal F_{\mathrm{inv}}$ and the induced relations run the other way. Since each orbit indicator $1_{Gx}$ is itself invariant,

$$
\boxed{
\{(x,gx):x\in X,\ g\in G\}
\;=\;\bigl(\equiv_{\mathcal F_{\mathrm{inv}}}\bigr)
\;\subseteq\;\bigl(\equiv_{\mathcal F_{\mathrm{def}}}\bigr)
\;\subseteq\;X\times X .
}
$$

The inclusion is the source of every standard counterexample at the absolute grade: two points exchanged by a symmetry lie in one orbit, hence in one class of $\equiv_{\mathcal F_{\mathrm{def}}}$, so no one-place formula separates them — a one-line argument with no metaphysics in it. The equality says something else, that against the full invariant family the principle is exactly rigidity. The inclusion is strict in general, and the gap between the two families is the gap between a symmetry and what a language can say about it.

The difference is not idle, because the principle has different truth conditions on the two sides. Against $\mathcal F_{\mathrm{inv}}$ it holds precisely when the orbits are singletons. Against $\mathcal F_{\mathrm{def}}$ that is necessary and not sufficient: elements may share every definable property and lie in different orbits. In $(\alpha,<)$ for an ordinal with $|\alpha|>2^{\aleph_0}$ — say $\alpha=(2^{\aleph_0})^{+}$ — every element is fixed by every automorphism, since a well-order is rigid, yet a countable language admits at most $2^{\aleph_0}$ complete $1$-types, so some two ordinals satisfy exactly the same formulas. Equality of the two sides holds under additional hypotheses: for a *countable* structure that is $\omega$-categorical in a countable first-order language, the Ryll-Nardzewski characterization makes the orbits of $\operatorname{Aut}(X)$ on $X^n$ coincide with the sets defined by complete $n$-types over $\varnothing$. Countability of the structure is load-bearing — an uncountable model of the same theory can have automorphisms constrained by class cardinalities — and must be checked rather than assumed.

A limiting case deserves its own name. If $G$ acts transitively on a nonempty $X$ then every $G$-invariant function is constant:

$$
\boxed{
G\ \text{transitive on}\ X\neq\varnothing
\;\Longrightarrow\;
\operatorname{Fun}(X,\mathbb C)^{G}=\mathbb C\cdot 1_X .
}
$$

A homogeneous arena has a trivial invariant readout. Its content cannot lie in invariants and must lie in sections, differences, and cocycles instead — which is why facthood is retyped as pointing in [[conservation-of-causal-charge/facthood-and-symmetry-breaking|Facthood and Symmetry Breaking]], and why [[why-there-is-difference]] treats homogeneity as a constraint on where facts can live rather than as an absence of them.

## Identical particles

Permutation invariance of a many-body theory declares that particle labels are not observables. The formalism then quotients the labels; in three or more spatial dimensions the symmetrization postulate leaves a state in a symmetrized or antisymmetrized space, while in two dimensions braid statistics permit more. Whether the residue is one object or several weakly discernible ones is not settled by the principle; it is settled by the state space the theory writes down, and the readings are compatible with the same predictions.

The narrower observation — that fermions in an antisymmetric state stand in irreflexive relations to one another and are therefore weakly discernible, while no invariant monadic property separates them — is a proposed reading and is contested, not a safe result. It depends on reading a relation off the expectation value of a symmetric projector in the given state, and both the irreflexivity of the resulting relation and the identification of its relata have been disputed. What is safe is only the structural point it illustrates: the grades come apart, and a configuration can be discernible at one grade and not at another.

The governing caution is that the grades must be checked one at a time. A symmetry defeats the principle at the grade of properties for any two points sharing an orbit, and at the relative grade whenever some automorphism *swaps* them, as the two-element example above shows; what a swapping symmetry can leave standing is at most weak discernibility, and even that only if the structure supplies an irreflexive relation. An argument that moves between grades without saying so has changed its subject.
