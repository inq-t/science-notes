# Symmetry as the Dual Presentation of Discernment

A symmetry group is the kernel of a discernment relation: the transformations that no declared observable registers. Invariance and automorphism form a Galois connection, so declaring which differences make a difference and declaring a group are one act in two coordinates — but the duality is faithful only when the declared family includes relations of every finite arity. At arity one the group records nothing beyond a partition, which is the same fact about grades that governs [[grades-of-discernment]], seen from the side of the group. Whether a group counts as gauge or as physical is a fact about which family it is the automorphism group of. Discernment is moreover local data, and local indiscernibility need not glue.

## The Galois connection

For a set $X$ let the declared data be relations rather than maps, so that the poset is a set. Write $\operatorname{Inv}_n(G)$ for the $G$-invariant subsets of $X^n$ under the diagonal action, $\operatorname{Inv}(G)=\bigcup_{n\geq1}\operatorname{Inv}_n(G)$, and

$$
\operatorname{Aut}(\mathcal R)
=\{g\in\operatorname{Sym}(X): g\ \text{preserves every}\ R\in\mathcal R\}.
$$

Both maps are order-reversing, and

$$
\mathcal R\subseteq\operatorname{Inv}\operatorname{Aut}(\mathcal R),
\qquad
G\subseteq\operatorname{Aut}\operatorname{Inv}(G),
$$

so the composites are closure operators and the connection restricts to a bijection between closed families and closed groups. This is the precise content of the practice it explains. To declare which differences make a difference is to declare $\mathcal R$; the group $\operatorname{Aut}(\mathcal R)$ is the same declaration written as its kernel, and it is usually the more tractable of the two, which is why the study of symmetry groups is the study of discernment carried out in the efficient coordinate.

## Arity is the grade of discernment

The duality is worthless at arity one. Since each orbit is itself an invariant subset, a permutation preserving every member of $\operatorname{Inv}_1(G)$ is exactly one preserving every orbit setwise, so

$$
\operatorname{Aut}\operatorname{Inv}_1(G)=\prod_{\mathcal O}\operatorname{Sym}(\mathcal O),
$$

the product over $G$-orbits. The closed groups at that arity are precisely the products of full symmetric groups on the blocks of a partition; the group records the partition $X/\!\equiv$ and nothing else. For $G=\langle(123)\rangle$ on three points the recovered group is $S_3$, not $\mathbb Z/3$.

Admitting all finite arities repairs this. The orbit of a tuple is then itself an invariant relation, which forces any recovered permutation to agree with some element of $G$ on each tuple, and Krasner's theorem gives

$$
\boxed{
\operatorname{Aut}\operatorname{Inv}(G)=\overline G ,
}
$$

the closure of $G$ in the topology of pointwise convergence, which for finite $X$ is $G$ itself. The moral is not technical. A group carries more information than a partition exactly because discernment is *relational*. The step from arity one to arity two is the same step as the one from absolute to relational discernment in [[grades-of-discernment]]; the two relational grades are then separated by a condition on the formula rather than by a further rise in arity. Absolute discernment sees only blocks, and the structure of a symmetry lives at arity two and above.

Even so, the connection is a bijection only between closed objects, so two families with the same automorphism group have the same closure and need not be the same family. The group records what is indiscernible, never which relations were primitive.

The correspondence also weakens outside the plain set-theoretic setting, and the weakening is not a technicality. For a *reductive* group acting on an affine variety over an algebraically closed field, the invariant ring is finitely generated and the affine quotient separates disjoint closed invariant subsets — so invariants separate closed orbits, and orbits whose closures meet are identified by every invariant. That last identification holds for any group whatever, and without reductivity even distinct closed orbits can fail to be separated, as they do for the additive group acting on the plane by $t\cdot(x,y)=(x,y+tx)$. Any transfer of the connection to smooth, measurable, operator-algebraic, or scheme-theoretic settings must state its hypotheses rather than inherit them.

## Gauge and physical symmetry differ by index, not by kind

A transformation is gauge when it lies in $\operatorname{Aut}(\mathcal R)$ for the declared family, and physical when it does not. The same abstract group can occupy either role in different theories, and no inspection of the group settles the question. This is [[two-directions|the suppressed index]] in its physical form: an assertion that some symmetry is merely a redescription is an assertion about the family.

The four-way classification of what a symmetry yields — continuous global, gauge, discrete, one-sided — and the reason that none of it follows from indiscernibility alone are given in [[conservation-of-causal-charge/indiscernibility-and-the-noether-gap|Indiscernibility and the Noether Gap]].

The role assignment is also unstable under change of scope. In the causal-scale programme the horizontal transport and the internal gauge fibers occupy different registers, and [[symmetry-groups-select/reconstruction-versus-selection|gauge reconstruction is not gauge selection]] records what would be required to derive the internal group rather than import it. Reconstruction theorems traverse the Galois connection; they do not choose the family it starts from.

## Discernment is local data

For a theory with regions, the declared family is not one family but an assignment $U\mapsto\mathcal R(U)$ with restriction maps, and therefore a presheaf of discernment relations rather than a single relation. Two configurations may then be indiscernible on every member of a cover and discernible globally.

This is not a pathology; it is where some of the most secure physics lives. A connection that is locally pure gauge can have nontrivial holonomy around a cycle that no local observable sees, and the difference is registered by a cohomology class rather than by any element of $\mathcal R(U)$. The obstruction is exactly the datum of [[basic-concepts/gluing/inq|gluing]] and [[basic-concepts/sheafs/inq|sheaves]], and its coherent form over a cover is [[basic-concepts/descent/inq|descent]].

The consequence for the razor is sharp:

$$
\boxed{
\text{indiscernible on each }U_i
\;\not\Longrightarrow\;
\text{indiscernible on }X .
}
$$

A razor applied region by region can therefore delete a global fact. Applying it correctly requires knowing whether the discernment presheaf satisfies descent, which is a theorem to be proved about a specific theory and never a default.
