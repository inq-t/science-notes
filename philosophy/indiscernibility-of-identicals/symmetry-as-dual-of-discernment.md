# Symmetry as the Dual Presentation of Discernment

A symmetry group is the kernel of a discernment relation: the transformations that no declared observable registers. Invariance and automorphism form a Galois connection, so a family of observables and a group of symmetries are two presentations of one datum — but the group presents only the *closed* part of the family, and the correspondence is exact for permutation groups and relations on a set, not automatically in continuous or algebraic settings. Whether a given group counts as gauge or as physical is a fact about which family it is the automorphism group of, not about the group. Discernment is moreover local data, and local indiscernibility need not glue.

## The Galois connection

For a set $X$ write

$$
\operatorname{Aut}(\mathcal F)
=\{g\in\operatorname{Sym}(X):F\circ g=F\ \text{for all}\ F\in\mathcal F\},
\qquad
\operatorname{Inv}(G)
=\{F:F\circ g=F\ \text{for all}\ g\in G\}.
$$

Both maps are order-reversing, and

$$
\mathcal F\subseteq\operatorname{Inv}\operatorname{Aut}(\mathcal F),
\qquad
G\subseteq\operatorname{Aut}\operatorname{Inv}(G),
$$

so the composites are closure operators and the connection restricts to a bijection between closed families and closed groups. This is the precise content of the practice it explains. To declare which differences make a difference is to declare $\mathcal F$; the group $\operatorname{Aut}(\mathcal F)$ is the same declaration written as its kernel, and it is usually the more tractable of the two — finitely presented, classifiable, representable — which is why the study of symmetry groups is the study of discernment carried out in the efficient coordinate.

## What the group forgets

The connection is a bijection only between *closed* objects. For permutation groups on a set, the closure is the topological one:

$$
\operatorname{Aut}\operatorname{Inv}(G)=\overline G,
$$

the closure of $G$ in the topology of pointwise convergence, which for finite $X$ is $G$ itself. Two observable families with the same automorphism group therefore have the same closure and need not be the same family. The group records what is indiscernible; it does not record which observables were primitive.

The correspondence also weakens outside the plain set-theoretic setting, and the weakening is not a technicality. For an algebraic group acting on an affine variety, invariant regular functions separate *closed* orbits only: orbits whose closures meet are identified by every invariant, so the invariant-theoretic quotient is coarser than the orbit set. There the razor over-cuts on its own, without anyone applying it. Any transfer of the connection to smooth, measurable, operator-algebraic, or scheme-theoretic settings must state its hypotheses rather than inherit them.

## Gauge and physical symmetry differ by index, not by kind

A transformation is gauge when it lies in $\operatorname{Aut}(\mathcal F)$ for the declared $\mathcal F$, and physical when it does not. The same abstract group can occupy either role in different theories, and no inspection of the group settles the question. This is [[two-directions|the suppressed index]] appearing in its physical form: an assertion that some symmetry is "merely a redescription" is an assertion about $\mathcal F$.

The two roles have different mathematical consequences, and the four-way classification — continuous global, gauge, discrete, and one-sided — is set out in [[conservation-of-causal-charge/indiscernibility-and-the-noether-gap|Indiscernibility and the Noether Gap]] together with the reason that none of them follows from indiscernibility alone. The gap is worth restating in the present vocabulary: the Galois connection is a statement about *which* transformations are undetectable, and contains no dynamics, no phase space, no action functional, and therefore no current. A theory of what makes no difference is not yet a theory of what is conserved.

The role assignment is also unstable under change of scope. In the causal-scale programme the horizontal transport $\Phi$ and the internal gauge fibers occupy different registers, and [[symmetry-groups-select/reconstruction-versus-selection|gauge reconstruction is not gauge selection]] records what would be required to derive the internal group rather than import it. Reconstruction theorems traverse the Galois connection; they do not choose the family it starts from.

## Discernment is local data

For a theory with regions, the declared family is not one family but an assignment $U\mapsto\mathcal F(U)$ with restriction maps, and therefore a presheaf of discernment relations rather than a single relation. Two configurations may then be indiscernible on every member of a cover and discernible globally.

This is not a pathology; it is where some of the most secure physics lives. A connection that is locally pure gauge can have nontrivial holonomy around a cycle that no local observable sees, and the difference is registered by a cohomology class rather than by any element of $\mathcal F(U)$. The obstruction is exactly the gluing datum of [[basic-concepts/gluing/entry|gluing]] and [[basic-concepts/sheafs/entry|sheaves]], and its coherent form over a cover is [[basic-concepts/descent/entry|descent]].

The consequence for the razor is sharp and easy to state:

$$
\boxed{
\text{indiscernible on each }U_i
\;\not\Longrightarrow\;
\text{indiscernible on }X .
}
$$

A razor applied region by region can therefore delete a global fact. Applying it correctly requires knowing whether the discernment presheaf satisfies descent, which is a theorem to be proved about a specific theory and never a default.
