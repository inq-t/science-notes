---
inq.module: "gluing"
inq.include:
  - "**/*.md"
---
# Gluing

Gluing is the passage from compatible local presentations to one global object. Its essential datum is not merely a collection of pieces, but an identification of the pieces wherever they overlap, coherent on every triple overlap. For sections of a [[basic-concepts/sheafs/inq|sheaf]] those identifications reduce to equality; for schemes, bundles, and [[basic-concepts/torsors/inq|torsors]] they are isomorphisms. A gluing theorem says exactly when such local data determine a whole, and in what sense that whole is unique.

## The local-to-global pattern

Let $X$ be a topological space, scheme, or more general site, and let

$$
X=\bigcup_i U_i
$$

be a cover. Suppose an object $E_i$ is given over each $U_i$. Write

$$
U_{ij}=U_i\times_XU_j,
\qquad
U_{ijk}=U_i\times_XU_j\times_XU_k.
$$

To say that the $E_i$ are presentations of one object requires isomorphisms on overlaps,

$$
\varphi_{ij}:E_j|_{U_{ij}}\xrightarrow{\sim}E_i|_{U_{ij}}.
$$

After all terms are restricted to a triple overlap, the direct comparison must agree with the comparison through an intermediate chart:

$$
\varphi_{ij}\circ\varphi_{jk}=\varphi_{ik}
\qquad\text{on }U_{ijk}.
$$

One also normalizes $\varphi_{ii}=\mathrm{id}$ and $\varphi_{ji}=\varphi_{ij}^{-1}$. These are not decorative equations. Without them, going from chart $k$ to chart $i$ can give different answers depending on the route. The **cocycle condition** is the assertion that the local changes of presentation contain no such ambiguity.

A global object $E$ automatically produces this data by restriction: choose identifications $E|_{U_i}\simeq E_i$ and compare them on overlaps. Gluing asks for the converse:

> Does every coherent family $(E_i,\varphi_{ij})$ arise from an object $E$ over $X$?

When it does, $E$ is generally unique up to a unique isomorphism compatible with the chosen local identifications. “Up to isomorphism” matters whenever the local objects have automorphisms.

Gluing concerns neighborhoods, not isolated points. The individual [[basic-concepts/fibers/inq|fibers]] $E_x$ may describe what lies over each $x\in X$, but a bare list of fibers contains no information about which nearby elements vary together, which local sections exist, or how transport around a loop acts. The overlap maps carry that missing relational structure.

## The sheaf axiom is the basic gluing law

For a presheaf $\mathcal F$ of sets, local sections already live in one fixed kind of object, so compatibility means equality after restriction. The sheaf axiom says that

$$
\mathcal F(U)
\longrightarrow
\prod_i\mathcal F(U_i)
\rightrightarrows
\prod_{i,j}\mathcal F(U_{ij})
$$

is an equalizer. Concretely, if $s_i\in\mathcal F(U_i)$ and

$$
s_i|_{U_{ij}}=s_j|_{U_{ij}}
$$

for every $i,j$, then there is a unique $s\in\mathcal F(U)$ with $s|_{U_i}=s_i$.

This has two logically separate parts:

- **locality, or separatedness:** two global sections that agree on every member of a cover are equal;
- **existence, or gluing:** every compatible family of local sections comes from a global section.

This is *separatedness of a presheaf*, not separatedness of a scheme. The former is uniqueness of glued sections; the latter is a condition on the diagonal morphism of a scheme.

Continuous functions, smooth functions, and regular functions are standard examples. Functions can be compared by equality on overlaps. Bundles and other objects cannot: two locally trivial bundles may be isomorphic without being literally equal. Their local-to-global theory therefore belongs naturally to [[basic-concepts/descent/inq|descent]] and [[basic-concepts/stacks/inq|stacks]] rather than only to set-valued sheaves.

## Gluing affine schemes

Schemes are built by gluing affine schemes, just as manifolds are built from coordinate charts. Let

$$
X_i=\operatorname{Spec}A_i
$$

and choose open subschemes $X_{ij}\subseteq X_i$ together with isomorphisms

$$
\varphi_{ij}:X_{ji}\xrightarrow{\sim}X_{ij}.
$$

If the overlap isomorphisms satisfy the identity, inverse, and cocycle conditions—including compatibility of the specified overlap opens on triple intersections—there is a scheme $X$ covered by open copies of the $X_i$ that realizes those identifications. The topology and the structure sheaf must be glued together; gluing the underlying point sets alone would forget the regular functions and hence would not determine a scheme.

The projective line is the decisive elementary example. Take

$$
U_0=\operatorname{Spec}k[t],
\qquad
U_1=\operatorname{Spec}k[s],
$$

and identify the principal opens

$$
D(t)=\operatorname{Spec}k[t,t^{-1}]
\quad\text{and}\quad
D(s)=\operatorname{Spec}k[s,s^{-1}]
$$

by $s=t^{-1}$. The result is $\mathbf P^1_k$. Neither affine chart contains the whole object; the reciprocal change of coordinate says how their descriptions are two views of the same points.

Gluing can succeed without producing every desirable global property. If two copies of $\mathbf A^1_k$ are glued by the identity on $\mathbf A^1_k\setminus\{0\}$, the result is the affine line with doubled origin. It is a legitimate scheme, but it is not separated. Thus the cocycle condition makes the assembly coherent; it does not by itself impose a Hausdorff-like separation condition.

## A line bundle is transition data made geometric

A line bundle $L\to X$ is locally $U_i\times\mathbf A^1$. Once local frames are chosen, an overlap identification is multiplication by an invertible regular function

$$
g_{ij}\in\mathcal O_X^\times(U_{ij}).
$$

The equations

$$
g_{ii}=1,
\qquad
g_{ji}=g_{ij}^{-1},
\qquad
g_{ij}g_{jk}=g_{ik}
$$

say that the local trivial bundles glue to a line bundle. Changing the frame on $U_i$ by $h_i\in\mathcal O_X^\times(U_i)$ changes the transition functions by a coboundary,

$$
g_{ij}\longmapsto h_i g_{ij}h_j^{-1}.
$$

The bundle is globally trivial precisely when its transition cocycle can be removed in this way. This is the meaning behind the classification of line bundles by

$$
\operatorname{Pic}(X)\cong H^1(X,\mathcal O_X^\times)
$$

in the relevant sheaf topology.

On $\mathbf P^1$, the tautological bundle $\mathcal O(-1)$ has local frames

$$
e_0=(1,t),
\qquad
e_1=(s,1),
$$

with $e_0=t e_1$ on $t\ne0$. The function $t$ is not an incidental coordinate formula: it is the rule by which two trivial local line bundles become one globally nontrivial line bundle. Principal bundles, gauge fields, and [[basic-concepts/torsors/inq|torsors]] use the same architecture with a group-valued transition cocycle.

## What can fail

Several different failures are often compressed into “the pieces do not glue.”

- The local data may disagree even on pairwise overlaps.
- Pairwise isomorphisms may exist, but their product around a triple overlap may be a nonidentity automorphism. Then the proposed identifications are not coherent.
- A coherent descent datum may fail to be effective because the chosen category of objects is not a stack for the chosen notion of cover.
- The global object may exist but lack an additional desired property, as the doubled-origin example lacks separatedness.
- A global object may exist without being globally trivial. A line bundle can be glued perfectly even though it has no global frame.
- Local sections may glue while locally presented **objects** require isomorphism-valued or higher coherence data that a set-valued sheaf cannot express.

In abelian situations, Čech or sheaf cohomology often records these distinctions. A degree-one class can record a nontrivial object assembled from local trivializations; in lifting problems, a degree-two class can obstruct the existence of coherent transition data. The degree and coefficient object depend on the problem—there is no universal “gluing obstruction” with one fixed cohomology group.

## Gluing, descent, and soldering answer different questions

| Structure | Question |
|---|---|
| Restriction | What does a global object look like on a smaller domain? |
| Gluing | Do compatible local pieces form one global object? |
| [[basic-concepts/descent/inq|Descent]] | Can an object pulled to a cover be recognized as coming from the base? |
| [[basic-concepts/soldering/inq|Soldering]] | How are objects of different geometric or physical kinds identified or calibrated? |

An open-cover gluing problem can be reformulated as descent along $\coprod_iU_i\to X$, so the first two notions are closely related. Soldering is not another name for either one. A soldering form can itself be given locally and glued, but what it *does* is connect different structures, not merely assemble copies of one structure.

## Use in geometry and physics

Gluing is used whenever a global object has no preferred global coordinates:

- schemes and varieties from affine charts;
- manifolds from coordinate patches;
- sheaves from compatible local sections;
- vector bundles and principal bundles from transition functions;
- gauge potentials, whose local representatives are related by gauge transformations;
- moduli problems, where families that are locally isomorphic must be compared together with their automorphisms; and
- local models of singular or compact spaces.

For this project, the intended architecture

$$
O\longmapsto (g_O,\mathcal A_O,\omega_O)
$$

cannot become a global theory merely by calling its values “local fibers.” One must say what the domains $O$ are, what counts as a cover, which data restrict covariantly or contravariantly, and what agreement means on a common refinement. Observable algebras in algebraic QFT are usually covariant under inclusions, while states restrict in the opposite direction; the combined object is therefore not automatically an ordinary sheaf.

The local-to-global obligation in [[cosmodynamics/construction-programme|the cosmodynamics construction programme]] is a genuine gluing problem only after those types and maps have been supplied. [[cosmodynamics/cosmos-as-structure-of-facts|A cosmos as the structure of facts]] motivates coherent overlap records, but pairwise agreement alone does not produce a shared history, an irreversible arrow, or physically realizable facts. Likewise, the surrounding architecture in [[compatible-with-existing-physics/relations-among-theories|relations among theories]] must prove that its global comparison laws preserve the imported local theories; the word *gluing* does not perform that proof.

The questions to retain for later scholia are therefore exact ones: What is local? What is the cover? Are overlaps literal intersections or fiber products? Are local data compared by equality, isomorphism, or a higher morphism? What enforces the triple-overlap law? Which global properties survive assembly? Those choices determine what “one whole” can mean.
