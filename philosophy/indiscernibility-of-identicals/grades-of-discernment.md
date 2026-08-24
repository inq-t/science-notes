# Grades of Discernment

Discernment by a monadic property, by an asymmetric relation, and by an irreflexive relation form a strictly increasing hierarchy, and the identity of indiscernibles has a different truth value at each grade. Automorphism orbits are contained in the indiscernibility classes of the invariant *monadic* family, which is why symmetric structures are the standard counterexamples at the strongest grade and not at the weakest. The weakest grade grounds identity only in a language from which identity has been excluded; otherwise it is circular.

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

Let $G=\operatorname{Aut}(X)$ and let $\mathcal F$ be the family of $G$-invariant monadic maps — the maps definable by one-place formulas of the language, so that $F\circ g=F$ for all $g\in G$. Then for every $x$ we have $x\equiv_{\mathcal F}g\,x$, hence

$$
\boxed{
G\text{-orbits}\ \subseteq\ \text{classes of absolute indiscernibility}.
}
$$

This inclusion is the source of every standard counterexample at the absolute grade: a structure with a nontrivial automorphism has distinct elements that no invariant monadic property separates. Two points exchanged by a symmetry are absolutely indiscernible, by a one-line argument and with no metaphysics involved. The inclusion says nothing about the relational grades, and the strictness examples above show that it must not be read as if it did.

The converse inclusion is not general. Elements may share every definable property and still lie in different orbits — in $(\alpha,<)$ for an ordinal $\alpha>2^{\aleph_0}$ every element is fixed by every automorphism, yet a countable language admits at most $2^{\aleph_0}$ complete types, so some two ordinals satisfy exactly the same formulas. Equality of orbits with indiscernibility classes holds under additional hypotheses: for a structure that is $\omega$-categorical in a countable first-order language, the Ryll-Nardzewski characterization makes the orbits of $\operatorname{Aut}(X)$ on $X^n$ coincide with the sets defined by complete $n$-types over $\varnothing$. Both hypotheses are load-bearing and must be checked rather than assumed.

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

The governing caution is that a symmetry defeats the principle at the grade of properties while leaving the grade of relations untouched, and an argument that moves between the two without saying so has changed its subject.
