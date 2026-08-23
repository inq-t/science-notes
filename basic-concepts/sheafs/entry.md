# Sheaves

A sheaf is a rule for assigning data to every local context so that the data can be restricted to smaller contexts and so that compatible local observations determine exactly one global observation. Its meaning lies in this discipline of locality: a section over a whole contains mutually consistent sections over all of its parts, while a compatible family over a cover is not merely evidence for a whole but a complete presentation of one. In algebraic geometry, sheaves make functions, equations, modules, and geometric structures vary over a space without presupposing global coordinates.

## Data organized by restriction

Let $X$ be a topological space, and let $\operatorname{Open}(X)$ be the category whose objects are open subsets of $X$ and whose arrows are inclusions. A **presheaf** $\mathcal F$ of sets on $X$ is a contravariant functor

$$
\mathcal F:\operatorname{Open}(X)^{\mathrm{op}}\longrightarrow\mathbf{Set}.
$$

Thus every open set $U$ has a set $\mathcal F(U)$ of **sections over $U$**, and every inclusion $V\subseteq U$ has a restriction map

$$
\rho^U_V:\mathcal F(U)\longrightarrow\mathcal F(V),
\qquad
s\longmapsto s|_V.
$$

The functor laws say

$$
\rho^U_U=\operatorname{id}_{\mathcal F(U)},
\qquad
\rho^V_W\circ\rho^U_V=\rho^U_W
\quad(W\subseteq V\subseteq U).
$$

The same definition works with values in groups, rings, modules, chain complexes, or another category with the required limits. Contravariance expresses a basic asymmetry: data already defined on a larger region can always be inspected on a smaller one, but data on a smaller region need not extend to a larger one.

A presheaf is not just a family $U\mapsto\mathcal F(U)$. Its restriction maps say when observations made at different resolutions or on different regions are appearances of the same datum. A list of values with no restriction law is only an indexed inventory.

## The sheaf axiom

Suppose $U=\bigcup_iU_i$. A family $s_i\in\mathcal F(U_i)$ is a **matching family** when

$$
s_i|_{U_i\cap U_j}=s_j|_{U_i\cap U_j}
$$

for every $i,j$. The presheaf $\mathcal F$ is a **sheaf** when every matching family is the family of restrictions of a unique $s\in\mathcal F(U)$.

For set-valued sheaves, this says that the diagram

$$
\mathcal F(U)
\longrightarrow
\prod_i\mathcal F(U_i)
\rightrightarrows
\prod_{i,j}\mathcal F(U_i\cap U_j)
$$

is an equalizer. The two parallel arrows restrict $s_i$ and $s_j$ to the same pairwise overlap. The axiom contains two different assertions:

- **locality, or separatedness:** if two sections over $U$ have the same restriction to every $U_i$, they are equal;
- **gluing:** if sections over the $U_i$ agree on all overlaps, a section over $U$ realizing them exists.

Separatedness here is a property of a presheaf's restriction law; it is not the separatedness condition on a scheme's diagonal.

This is the elementary law developed more generally in [[basic-concepts/gluing/entry|gluing]]. It does not say that arbitrary local data make a whole. They must agree after being brought into a common context, and the resulting whole is unique because sections are compared by equality. Objects that are compared only up to isomorphism require [[basic-concepts/descent/entry|descent]] and usually a [[basic-concepts/stacks/entry|stack]].

The axiom also explains why sections over regions, rather than values at points, are primary. Locality is a relation among extended domains and their overlaps. Points become useful through germs, but a point alone has no overlap geometry.

## Germs and stalks

Two sections may be indistinguishable near a point even when they are defined on different neighborhoods. For $x\in X$, a **germ at $x$** is an equivalence class of pairs $(U,s)$ with $x\in U$ and $s\in\mathcal F(U)$, where

$$
(U,s)\sim(V,t)
$$

if there is a neighborhood $W\subseteq U\cap V$ of $x$ on which $s|_W=t|_W$. The set of germs is the **stalk**

$$
\mathcal F_x
=
\varinjlim_{x\in U}\mathcal F(U).
$$

A stalk therefore records every datum visible sufficiently near $x$, modulo how far its original representative happened to be defined. It is not normally the value of a field at $x$. For the sheaf of smooth functions, for example, $\mathcal C^\infty_{X,x}$ contains full smooth germs; evaluation at $x$ forgets most of that information.

For an $\mathcal O_X$-module $\mathcal F$ on a scheme, the distinction from a [[basic-concepts/fibers/entry|fiber]] is exact:

$$
\text{stalk: }\mathcal F_x,
\qquad
\text{fiber: }\mathcal F(x)
:=\mathcal F_x\otimes_{\mathcal O_{X,x}}\kappa(x).
$$

The stalk is a module over the local ring $\mathcal O_{X,x}$ and retains behavior in a neighborhood of $x$. Tensoring with the residue field $\kappa(x)$ kills the maximal-ideal directions and leaves the value in the geometric fiber. Confusing these loses precisely the infinitesimal information that algebraic geometry encodes locally.

On an ordinary topological space, a morphism of sheaves is an isomorphism if and only if it induces an isomorphism on every stalk. A bare family of stalks still does not determine a sheaf: one must also know which germs assemble into sections and how they vary. On a general site there may be no adequate family of ordinary points, so the covering-based sheaf axiom remains more fundamental than a stalkwise test.

## The structure sheaf makes a space algebraic

A scheme is not its topological space alone. It is a locally ringed space

$$
(|X|,\mathcal O_X)
$$

locally isomorphic to the spectrum of a ring with its **structure sheaf**. If $X=\operatorname{Spec}A$, then on a principal open $D(f)$,

$$
\mathcal O_X(D(f))\cong A_f,
$$

and at the prime $\mathfrak p$,

$$
\mathcal O_{X,\mathfrak p}\cong A_{\mathfrak p}.
$$

The localization $A_f$ permits precisely the denominators that are nonvanishing on $D(f)$. Thus a regular function is not defined by one global polynomial formula in every presentation. It is locally a quotient with an invertible denominator, and the sheaf axiom identifies local formulas that agree wherever both are meaningful.

The requirement that each stalk $\mathcal O_{X,x}$ be a local ring marks one value as the value at $x$: its maximal ideal consists of germs vanishing at $x$, and the quotient

$$
\kappa(x)=\mathcal O_{X,x}/\mathfrak m_x
$$

is the residue field. Topology says which points specialize to which; the structure sheaf says which functions and infinitesimal relations exist around them. The scheme is the conjunction, not either constituent separately.

## Modules made local

If $M$ is an $A$-module and $X=\operatorname{Spec}A$, the associated sheaf $\widetilde M$ is characterized on principal opens by

$$
\widetilde M(D(f))=M_f.
$$

An $\mathcal O_X$-module $\mathcal F$ is **quasi-coherent** when it is locally of this form. Quasi-coherence means that the module data vary by the same localization law as regular functions; it is not a generic regularity condition on an arbitrary sheaf. Quasi-coherent sheaves are the natural carriers of ideals, differentials, equations, and linear families in algebraic geometry.

A finite locally free $\mathcal O_X$-module is locally isomorphic to $\mathcal O_X^n$ and corresponds, under the usual algebraic-geometric convention, to a rank-$n$ vector bundle. The associated sheaf assigns to $U$ the sections of the bundle over $U$. The two viewpoints are closely related but typed differently:

$$
E\longrightarrow X
\quad\text{is a geometric object over }X,
\qquad
U\longmapsto\Gamma(U,E)
\quad\text{is its sheaf of sections}.
$$

Not every sheaf is the section sheaf of an ordinary bundle, and a stalk of the section sheaf consists of germs of local sections rather than points of the bundle fiber. Frame choices form [[basic-concepts/torsors/entry|torsors]]; their transition functions describe how locally free sheaves become globally twisted.

## Examples that expose the definition

The assignments of continuous, smooth, holomorphic, or regular functions to open sets are sheaves. Agreement on overlaps permits the formulas to be pasted, and pointwise equality makes the pasted function unique. Differential forms and sections of a fixed bundle form sheaves for the same reason.

For a set or group $A$, the **constant presheaf** informally assigns $A$ to every nonempty open set with identity restriction maps. It usually is not a sheaf. If

$$
U=U_1\sqcup U_2
$$

is disconnected, one may choose $a_1\ne a_2$ on the two components. The choices agree vacuously on the empty overlap, but no single constant element of $A$ restricts to both. Its sheafification is the **constant sheaf** $\underline A$, whose sections are locally constant $A$-valued functions. The correction is meaningful: locality permits a value to be constant near every point without forcing one value on disconnected components.

More generally, a **locally constant sheaf**, or local system in a standard topological setting, is locally isomorphic to a constant sheaf but can have nontrivial monodromy around loops. It records data that can be transported locally even though returning around a loop may act by an automorphism. Once a basepoint and suitable hypotheses are chosen, such systems can be described by representations of the fundamental group.

For a closed point $i:\{x\}\hookrightarrow X$ and an abelian group $A$, the **skyscraper sheaf** $i_*A$ has

$$
(i_*A)(U)=
\begin{cases}
A,&x\in U,\\
0,&x\notin U.
\end{cases}
$$

It concentrates data at one closed location. Skyscraper sheaves are useful for describing point-supported conditions, residues, defects, and quotients. They also show that a sheaf need not describe a continuously spread field.

## Sheafification

Every presheaf $\mathcal F$ of sets or standard algebraic objects has an associated sheaf $a\mathcal F$ and a morphism

$$
\eta:\mathcal F\longrightarrow a\mathcal F
$$

universal among morphisms from $\mathcal F$ to sheaves:

$$
\operatorname{Hom}_{\mathbf{Sh}(X)}(a\mathcal F,\mathcal G)
\cong
\operatorname{Hom}_{\mathbf{PSh}(X)}(\mathcal F,\mathcal G)
$$

for every sheaf $\mathcal G$. Sheafification identifies sections that are locally equal and adds sections represented by compatible local families. On topological spaces it does not change the stalks. What changes is the law by which those germs are admitted as sections over larger opens.

Sheafification is therefore a localization of descriptions, not a proof that arbitrary geometric objects descend. It repairs equality-valued local data. If local objects have nontrivial automorphisms, passing prematurely to isomorphism classes can destroy the coherence needed to glue them; the appropriate completion is stackification rather than ordinary sheafification.

## Sites: locality without open subsets

Algebraic geometry needs notions of locality finer than the Zariski open sets. A **site** $(\mathcal C,J)$ is a category $\mathcal C$ equipped with a Grothendieck topology $J$, which specifies which families

$$
\{U_i\longrightarrow U\}
$$

count as covers. Covers include identities, remain covers after base change, and compose transitively. A presheaf on the site is a functor $\mathcal C^{\mathrm{op}}\to\mathbf{Set}$; it is a sheaf when matching families for every declared cover glue uniquely. When the relevant fiber products exist, the overlap $U_i\cap U_j$ is replaced by

$$
U_i\times_UU_j.
$$

The Zariski, étale, fppf, and fpqc topologies declare different morphisms to be local covers. The same assignment may be a sheaf for one topology and fail for a finer one because the finer topology demands effective gluing across more presentations. This is why claims that an object exists “locally” are incomplete until the topology is named; [[basic-concepts/descent/entry|descent]] develops that dependence in detail.

On a subcanonical site, every representable presheaf

$$
h_X(T)=\operatorname{Hom}(T,X)
$$

is a sheaf. This connects the functor-of-points view of a geometric object to locality: maps into $X$ can be recognized after passing to a cover. The category $\mathbf{Sh}(\mathcal C,J)$ is a **topos**. Different sites can present equivalent topoi, so the chosen charts are not always intrinsic to the resulting universe of sheaves.

## Cohomology records global failure beyond the sheaf axiom

For a sheaf of abelian groups, global sections define a left-exact functor

$$
\Gamma(X,-):\mathbf{Sh}(X,\mathbf{Ab})\longrightarrow\mathbf{Ab}.
$$

Its right-derived functors are sheaf cohomology:

$$
H^q(X,\mathcal F)=R^q\Gamma(X,\mathcal F),
\qquad
H^0(X,\mathcal F)=\Gamma(X,\mathcal F).
$$

The sheaf axiom already guarantees that matching **sections of $\mathcal F$** glue. Higher cohomology does not measure a failure of that axiom. It measures failures of other constructions involving local choices to become globally exact.

For example, from a short exact sequence

$$
0\longrightarrow\mathcal F
\longrightarrow\mathcal G
\longrightarrow\mathcal H
\longrightarrow0
$$

comes a connecting map

$$
\delta:H^0(X,\mathcal H)\longrightarrow H^1(X,\mathcal F).
$$

A global section $h$ of $\mathcal H$ can be lifted locally to $\mathcal G$. The class $\delta(h)$ is the obstruction to choosing those local lifts compatibly as one global lift. Similarly,

$$
\operatorname{Pic}(X)\cong H^1(X,\mathcal O_X^\times)
$$

classifies line bundles by the transition cocycles of local frames. For a nonabelian group sheaf $G$, $H^1(X,G)$ classifies $G$-torsors only as a pointed set in general, not as a derived abelian group.

Čech cocycles make many such classes concrete, but Čech cohomology for one cover is not automatically identical to derived sheaf cohomology without additional hypotheses. Nor is every cohomology class generically “an obstruction”; the relevant class and degree must arise from the particular extension, lifting, deformation, or classification problem. A central benchmark is that, for Zariski cohomology of a quasi-coherent sheaf $\mathcal F$ on an affine scheme,

$$
H^q(X,\mathcal F)=0
\qquad(q>0),
$$

so affine localization has no higher quasi-coherent cohomological obstruction of this kind.

## Neighboring notions are not synonyms

| Notion | Variance and local law | What it describes |
|---|---|---|
| Presheaf | contravariant restrictions | local data, without a guarantee of local-to-global reconstruction |
| Sheaf | contravariant restrictions plus unique gluing | sections determined by compatible local sections |
| Cosheaf | covariant extension maps plus a colimit gluing law | data assembled outward from parts rather than inspected by restriction |
| Bundle $E\to X$ | a geometric map locally resembling a product | fibers varying over a base; its sections may form a sheaf |
| [[basic-concepts/stacks/entry|Stack]] | category- or [[basic-concepts/groupoids/entry|groupoid]]-valued descent | objects and their automorphisms glued up to coherent isomorphism |

A covariant functor on regions is not automatically a cosheaf: it must satisfy the appropriate colimit law. Likewise, a contravariant functor is only a presheaf until its equalizer law is proved. A sheaf can be regarded as a stack with discrete fibers, where every morphism is an identity; a genuine stack retains automorphisms and the higher coherence they force.

The distinction becomes visible for line bundles. Their local **sections** form a sheaf, but line bundles themselves glue through isomorphisms of local bundles. The presheaf of isomorphism classes forgets those isomorphisms and can fail to encode descent correctly. The stack of line bundles keeps them.

## Quantum contexts and the spectral presheaf

Let $\mathcal A$ be a noncommutative observable algebra, and let $\mathcal V(\mathcal A)$ be a poset of unital commutative subalgebras ordered by inclusion. The **spectral presheaf** assigns

$$
C\longmapsto\Sigma(C),
$$

the Gelfand spectrum of each commutative context. An inclusion $C'\subseteq C$ induces the restriction

$$
\Sigma(C)\longrightarrow\Sigma(C'),
\qquad
\lambda\longmapsto\lambda|_{C'}.
$$

A global element would be a choice of character in every context, compatible under every restriction. In the standard Hilbert-space setting of dimension at least three, the Kochen--Specker theorem rules out such a noncontextual global valuation. Rephrasing the theorem as absence of a global element is illuminating, but several cautions are essential:

- the spectral object is, first of all, a **presheaf** on the context category; calling it a sheaf requires a specified topology and a verified sheaf condition;
- absence of a global element is not failure of the sheaf axiom;
- the theorem does not say that individual commutative contexts lack characters;
- it does not select a contextual outcome, derive the Born rule, or supply a dynamics of fact formation.

The distinction in [[sufficient-reason/quantum-interpretations|quantum interpretation and the type change]] therefore remains: restricting a state to a commutative context yields a probability measure on its spectrum, not a selected spectral point. [[sufficient-reason/facticity-and-pointing|Facticity and pointing]] asks for the further structure by which a contextual value becomes a fact.

## Local quantum physics has mixed variance

In algebraic quantum field theory, an inclusion of causal regions usually gives an inclusion of observable algebras,

$$
O_1\subseteq O_2
\quad\Longrightarrow\quad
\mathcal A(O_1)\hookrightarrow\mathcal A(O_2).
$$

The net $O\mapsto\mathcal A(O)$ is therefore covariant, whereas an ordinary sheaf on regions is contravariant. A state on the larger algebra restricts by precomposition to the smaller algebra,

$$
\omega_{O_2}\longmapsto
\omega_{O_2}|_{\mathcal A(O_1)},
$$

so state assignment runs contravariantly relative to the algebra inclusions. Neither fact makes the corresponding assignment automatically a cosheaf or a sheaf. Additivity and Einstein causality for a net are different axioms from a cosheaf colimit law, and compatible local states need not have a unique—or any admissible—global extension.

This variance is decisive for the proposed local package

$$
O\longmapsto(g_O,\mathcal A_O,\omega_O).
$$

The metric, algebra, and state components cannot be called one sheaf until their common base category, covers, arrows, and compatibility maps are specified. The local-to-global obligation in [[cosmodynamics/construction-programme|the cosmodynamics construction programme]] must say whether algebras are included, states are restricted, metrics are pulled back, and facts or records agree by equality, isomorphism, or a higher comparison. [[compatible-with-existing-physics/local-physics-interface|The local-physics interface]] adds the requirement that these maps preserve the imported QFT and GR structures. [[cosmodynamics/fact-record-history|A common history]] adds a still stronger demand: observer-relative records must remain consistent whenever they become jointly comparable.

Sheaf language does not solve these problems by naming them. It makes their hidden premises explicit. One must identify what counts as a context, what counts as a cover, what restriction forgets, what overlap comparison means, and which theorem turns compatible local descriptions into one global structure. That is precisely why sheaves belong near the foundation of this project: they convert an intuition of “many local perspectives, one cosmos” into a list of mathematical obligations that can succeed or fail.
