# Two Directions of Leibniz's Law

The indiscernibility of identicals and the identity of indiscernibles are converse implications of unequal standing. The first is a well-definedness condition on the declared property family and cannot fail. The second is a claim about the *pair* consisting of a domain and a family, and it fails whenever the family consists of invariants of a nontrivial automorphism. It becomes vacuous when the family is allowed to contain identity properties. Every use of the principle in this project is therefore indexed by a declared family, and the index must be stated before the principle is invoked.

## The two implications

Fix a domain $X$ — of presentations, configurations, states, points, or histories — and a family

$$
\mathcal F=\{F:X\to Y_F\}
$$

of declared properties, observables, or accessible maps. Write

$$
a\equiv_{\mathcal F}b
\quad:\Longleftrightarrow\quad
F(a)=F(b)\ \text{for every }F\in\mathcal F .
$$

**Indiscernibility of identicals.**

$$
a=b\;\Longrightarrow\;a\equiv_{\mathcal F}b .
$$

This holds for every $\mathcal F$ whatsoever, because each $F$ is a function of its argument. It is single-valuedness restated, and its working corollary is the substitution rule: equals may be exchanged inside any declared context. The direction is a constraint on the presentation of $\mathcal F$, not information about $X$. To deny it is not to describe a different world but to have written down maps that are not functions on the domain claimed for them.

**Identity of indiscernibles.**

$$
a\equiv_{\mathcal F}b\;\Longrightarrow\;a=b .
$$

Nothing about identity secures this. It says that $\mathcal F$ is rich enough to tell the elements of $X$ apart, which is a fact about the *choice* of $\mathcal F$ relative to $X$. Write the indexed claim as $\mathrm{PII}(\mathcal F)$. Its exact equivalent is stated in [[separation-and-quotient]], and the condition under which a symmetry defeats it — that $\mathcal F$ consist of invariants of that symmetry — in [[grades-of-discernment]].

## The index cannot be suppressed

The relation $\equiv_{\mathcal F}$ is antitone in the family. If $\mathcal F\subseteq\mathcal F'$ then agreeing on all of $\mathcal F'$ implies agreeing on all of $\mathcal F$, so

$$
\mathcal F\subseteq\mathcal F'
\;\Longrightarrow\;
\bigl(\equiv_{\mathcal F'}\bigr)\subseteq\bigl(\equiv_{\mathcal F}\bigr)
\;\Longrightarrow\;
\bigl(\mathrm{PII}(\mathcal F)\Rightarrow\mathrm{PII}(\mathcal F')\bigr).
$$

The strong form of the principle is thus the one quantifying over the *smallest* family. A claim that two situations are indiscernible is only as strong as the meagreness of the family it ranges over, and a claim that the principle holds is only as strong as the richness of that family. Announcing either without the index states nothing. A symmetric structure is a counterexample to the principle only relative to an invariant family: on $X=\{1,2\}$ with $\mathcal F=\{\mathrm{id}_X\}$ the automorphism group is $S_2$ and the principle nevertheless holds, because $\mathrm{id}_X$ is not invariant.

Where $\mathcal F$ is a family of physical observables, this is the family written $\mathcal O$ in [[conservation-of-causal-charge/indiscernibility-and-the-noether-gap|Indiscernibility and the Noether Gap]], and $\equiv_{\mathcal F}$ is the relation written $\sim_{\mathcal O}$ there.

## Trivialization by identity properties

Under unrestricted second-order comprehension the family contains the haecceities

$$
F_a=\lambda x.\,(x=a),
$$

for which $a\equiv b$ immediately yields $F_a(a)=F_a(b)$, hence $b=a$. So the unrestricted principle is a theorem of the logic and licenses nothing whatever about nature. It becomes a razor only under a *qualitative* restriction: $\mathcal F$ must be closed under the transformations the theory declines to regard as physical, which is to say $\mathcal F$ must consist of invariants of a declared group or groupoid. That restriction is the subject of [[symmetry-as-dual-of-discernment]], and the ways it is evaded in practice are registered in [[the-razor]].

## Two conclusions to distinguish from identity

Even a separating family need not deliver equality as its conclusion. In a categorical setting the honest output is canonical isomorphism, and in a relational setting it may be discernibility by a relation rather than by any property. These are not weakenings of the principle but different conclusions with different consequences, treated in [[separation-and-quotient]] and [[grades-of-discernment]].

The exegetical question of what Leibniz himself asserted, and the derivation of the principle from a demand for grounds, is out of scope here and belongs to [[philosophy/leibniz/entry|the Leibniz module]]. The typed form of that demand in this project is [[sufficient-reason/entry|Sufficing and Necessitating Reason]]. The structural relation used here is only this: a distinction that no reason could fix is not yet a distinction, so the principle of individuation and the principle of ground constrain each other.
