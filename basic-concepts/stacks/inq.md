---
inq.module: "stacks"
inq.include:
  - "**/*.md"
---
# Stacks

A stack is a local-to-global object that remembers symmetry. Over every test space it assigns a [[basic-concepts/groupoids/inq|groupoid]] of families and their isomorphisms; pullback changes the test space, and the stack condition says that compatible local families and compatible arrows satisfy effective [[basic-concepts/descent/inq|descent]]. A stack is therefore a categorified [[basic-concepts/sheafs/inq|sheaf]]: equality of local sections is replaced by coherent isomorphism of local objects. Algebraic stacks add representability conditions that make this symmetry-sensitive moduli object accessible to algebraic geometry.

## Which meaning of “stack”

This entry concerns **Grothendieck stacks**, especially stacks in groupoids on schemes, and then **algebraic stacks**. It does not concern a software call stack, a technology stack, or an informal pile of assumptions.

In particular, [[causal-scale-theory/realization-map|the CST realization map]] is an ordinary dependency stack: a layered ledger of premises and closure laws. That phrase is useful, but it does not assert the existence of a site, a groupoid-valued functor, descent data, a representable diagonal, or an atlas. Nothing in the algebraic-geometric theory of stacks follows merely from arranging dependencies in layers.

The term **geometric stack** is also convention-dependent. It can mean an algebraic stack, or it can belong to an inductive theory of \(n\)-geometric or derived stacks. Any use of that phrase should state its convention. Here the precise standard term will be *algebraic stack*.

## Why a sheaf of sets is sometimes too small

Suppose a moduli problem asks for vector bundles, elliptic curves, or principal bundles varying over a scheme \(T\). A set-valued assignment might send \(T\) to the set of isomorphism classes of such objects. That assignment has forgotten information too early.

On an open or faithfully flat cover \(\{T_i\to T\}\), local objects \(x_i\) are not normally equal on overlaps. They are related by chosen isomorphisms

$$
\varphi_{ij}:x_j|_{T_{ij}}\xrightarrow{\sim}x_i|_{T_{ij}},
\qquad
T_{ij}=T_i\times_TT_j.
$$

On a triple overlap these choices must satisfy

$$
\varphi_{ij}\circ\varphi_{jk}=\varphi_{ik}.
$$

If the objects have automorphisms, different choices of \(\varphi_{ij}\) can produce inequivalent global objects even when every local isomorphism class is the same. The set of local isomorphism classes cannot express that difference. A groupoid can: its objects are the families, and its arrows are their isomorphisms.

This gives the central meaning of a stack:

> A sheaf remembers which local values are equal. A stack remembers which local objects are isomorphic, the isomorphisms themselves, and the coherence required for those isomorphisms to constitute one global object.

Stacks do not weaken rigor by replacing equality with a vague notion of sameness. They make the relevant sameness into explicit arrows with identities, inverses, and composition.

## The groupoid-valued viewpoint

Let \((\mathcal C,\tau)\) be a **site**: a category \(\mathcal C\) equipped with a declared class of covering families. In algebraic geometry, \(\mathcal C\) is often the category of schemes over a base \(S\), and \(\tau\) may be the Zariski, étale, smooth, fppf, or fpqc topology.

The intuitive form of a stack begins with a contravariant assignment

$$
\mathcal X:\mathcal C^{\mathrm{op}}\longrightarrow\mathbf{Grpd}.
$$

For every \(T\), \(\mathcal X(T)\) is a groupoid of objects over \(T\). A map \(f:T'\to T\) gives a pullback functor

$$
f^*:\mathcal X(T)\longrightarrow\mathcal X(T').
$$

For moduli of families, \(f^*x\) is the family obtained by base change. Pullback is often associative and unital only up to specified canonical isomorphisms,

$$
(f\circ g)^*\cong g^*f^*,
\qquad
\operatorname{id}_T^*\cong\operatorname{id}_{\mathcal X(T)},
$$

and those isomorphisms themselves obey coherence laws. Thus the technically honest assignment is usually a **pseudofunctor**, not a strict functor.

The equivalent geometric packaging is a **category fibered in groupoids**

$$
p:\mathcal X\longrightarrow\mathcal C.
$$

An object of the total category lies over some \(T\), and a map \(T'\to T\) admits a cartesian lift expressing pullback. The fiber \(\mathcal X_T\) over \(T\) is a groupoid. The pseudofunctor and fibered-category pictures encode the same intuition through the Grothendieck construction; the latter avoids making arbitrary strict choices of pullbacks.

This use of *fiber* is categorical. It is related in spirit to [[basic-concepts/fibers/inq|scheme-theoretic fibers]] but is not the same construction as \(X\times_S\operatorname{Spec}\kappa(s)\).

## The stack condition

Fix a cover \(\{T_i\to T\}\). A **descent datum** consists of

1. objects \(x_i\in\mathcal X(T_i)\);
2. isomorphisms \(\varphi_{ij}:x_j|_{T_{ij}}\to x_i|_{T_{ij}}\); and
3. the cocycle equation \(\varphi_{ij}\varphi_{jk}=\varphi_{ik}\) on \(T_{ijk}\).

These data and their compatible morphisms form a descent groupoid, denoted schematically by

$$
\operatorname{Desc}_{\mathcal X}(\{T_i\to T\}).
$$

Restriction gives a functor

$$
\mathcal X(T)\longrightarrow
\operatorname{Desc}_{\mathcal X}(\{T_i\to T\}).
$$

The assignment \(\mathcal X\) is a **stack** for \(\tau\) when this functor is an equivalence of groupoids for every \(\tau\)-cover. The two parts of that equivalence have different meanings:

- **descent for arrows:** morphisms between global objects are determined by compatible local morphisms;
- **effective descent for objects:** every coherent local object is isomorphic to the restriction of a global object.

Equivalently, the presheaf

$$
U\longmapsto\operatorname{Isom}_U(x|_U,y|_U)
$$

must be a sheaf for every pair \(x,y\), and every object-level descent datum must be effective. The descended object is not literally unique as a chosen object. It is unique up to a unique isomorphism compatible with the descent identifications—the correct categorical analogue of the uniqueness clause in the sheaf axiom.

Terminology for **prestack** varies. A common convention calls a category fibered in groupoids a prestack once descent for arrows holds, and reserves *stack* for the additional effectiveness of object descent. Other authors call any groupoid-valued pseudofunctor a prestack. The convention must be checked before using a theorem.

**Stackification** is the analogue of sheafification: it universally replaces a prestack by a stack. It can supply the objects needed to make descent effective, but it does not make the result algebraic, representable, separated, finite-dimensional, or physically realized.

## Every scheme is a stack, but not every stack is a scheme

A scheme \(X\) over \(S\) defines its functor of points

$$
h_X(T)=\operatorname{Hom}_S(T,X).
$$

Regard each set \(h_X(T)\) as a discrete groupoid, containing only identity automorphisms. For the standard subcanonical topologies, morphisms into \(X\) satisfy descent, so \(h_X\) is a stack. A stack equivalent to some \(h_X\) is **representable by the scheme \(X\)**.

This embeds schemes into stacks without changing their ordinary geometry. The enlargement becomes visible when \(\mathcal X(T)\) has nontrivial automorphisms or contains twisted families that no single global coordinate presentation can display. Such a stack cannot be represented by a scheme in a way that preserves those groupoids, because a representable stack is discrete over every test scheme.

The same idea embeds algebraic spaces as stacks. Algebraic stacks enlarge that world again while retaining enough representability to do geometry.

## The classifying stack \(BG\)

Let \(G\to S\) be a group scheme. Its **classifying stack** \(BG\), also written \([S/G]\) for the trivial action, assigns to each \(T\to S\) the groupoid

$$
BG(T)=\{G_T\text{-torsors on }T\text{ and their equivariant isomorphisms}\}.
$$

A morphism \(T\to BG\) therefore *is* a family of \(G\)-torsors over \(T\). The [[basic-concepts/torsors/inq|torsor]] need not be globally trivial; allowing all such torsors is exactly what makes the construction satisfy descent.

The trivial torsor has automorphism group \(G(T)\) in the elementary case. Thus \(BG\) can have only one geometric isomorphism class of objects while still carrying the entire group \(G\) as isotropy. Replacing \(BG\) by a one-point set would erase its defining content.

For \(G=\operatorname{GL}_n\), a \(G\)-torsor is a frame torsor and hence determines a rank-\(n\) vector bundle. Accordingly,

$$
B\operatorname{GL}_n(T)
\simeq
\{\text{rank-}n\text{ vector bundles on }T\text{ and their isomorphisms}\}.
$$

This is a compact example of the progression

$$
\text{local frames}
\longrightarrow
\text{transition isomorphisms}
\longrightarrow
\text{torsor}
\longrightarrow
\text{classifying stack}.
$$

## Quotient stacks \([X/G]\)

Let \(G\) act on a scheme or algebraic space \(X\), and write \(\mathcal X=[X/G]\) for the quotient stack rather than the orbit set \(X/G\). Over a test scheme \(T\), an object of the groupoid \(\mathcal X(T)\) is a pair

$$
(P\to T,\;P\to X),
$$

where \(P\to T\) is a \(G\)-torsor and \(P\to X\) is equivariant; arrows are equivariant isomorphisms compatible with the maps to \(X\). Locally, after trivializing \(P\), this looks like a map \(T\to X\). Changing the trivialization acts by \(G\), and globally the torsor may remain nontrivial.

For a geometric point \(x\in X\), the automorphism group of the corresponding object in \([X/G]\) is its stabilizer

$$
G_x=\{g\in G:g\cdot x=x\}.
$$

The quotient stack therefore retains both the orbit and its isotropy. If the action is free and an appropriate geometric quotient exists, \([X/G]\) may be representable by that quotient. With fixed points, quotient singularities, or nontrivial torsors, the stack and the coarse orbit space carry different information.

The action [[basic-concepts/groupoids/inq|groupoid]]

$$
G\times X\rightrightarrows X
$$

is a presentation of \([X/G]\). More generally, a groupoid object \(R\rightrightarrows U\) can present a quotient stack \([U/R]\). Different presentations can define equivalent stacks, so the atlas and groupoid are coordinates on the stack rather than the stack's absolute identity.

## Moduli means families, not merely points

The stack of elliptic curves \(\mathcal M_{1,1}\) assigns to \(T\) the groupoid of elliptic curves

$$
E\longrightarrow T
$$

with zero section, together with their isomorphisms over \(T\). A morphism \(T'\to T\) pulls the entire family back. The definition therefore records base change, twisting over the base, and automorphisms fiber by fiber; it is not just the set of complex isomorphism classes of individual elliptic curves. Singular degenerations lie on an appropriate compactification, not inside the stack of smooth elliptic curves itself.

The \(j\)-invariant gives a coarse parameter, but it forgets automorphisms. Away from exceptional characteristics and loci, an elliptic curve already has the automorphisms \(\{\pm1\}\), and at special \(j\)-values its automorphism group is larger. The stack remembers these stabilizers. The coarse \(j\)-line does not, and it does not carry a universal elliptic curve in the fine-moduli sense.

The same pattern occurs for moduli of curves, vector bundles, coherent sheaves, stable maps, and principal bundles. A **fine moduli space** represents the full set-valued moduli functor and carries a universal family. Such a space often cannot exist because objects have automorphisms. A moduli stack retains the automorphisms instead of treating them as an inconvenience to be discarded.

## Algebraic and Deligne--Mumford stacks

A stack in groupoids on schemes can be far too large or irregular for ordinary algebraic geometry. Under the standard convention used here, one begins with a stack in groupoids on \((\mathrm{Sch}/S)_{\mathrm{fppf}}\). An **algebraic stack** over \(S\) then imposes two additional geometric conditions:

1. the diagonal

   $$
   \Delta_{\mathcal X}:\mathcal X\longrightarrow
   \mathcal X\times_S\mathcal X
   $$

   is representable by algebraic spaces; and
2. there is a scheme \(U\) and a smooth surjective morphism

   $$
   U\longrightarrow\mathcal X.
   $$

The map \(U\to\mathcal X\) is an **atlas**. It says that the stack can be covered smoothly by ordinary algebraic geometry. The diagonal condition says, roughly, that the isomorphisms between two families are themselves represented by algebraic spaces: after maps \(T\to\mathcal X\) corresponding to \(x,y\in\mathcal X(T)\), the relevant fiber of the diagonal represents \(\operatorname{Isom}_T(x,y)\). The diagonal therefore controls stabilizers, separation properties, and the geometry of comparison.

Many authors call this an **Artin stack**, with finiteness conventions varying by source. A **Deligne--Mumford stack** is an algebraic stack admitting an étale surjective atlas

$$
U\longrightarrow\mathcal X.
$$

The étale condition is stronger than smoothness. Under the usual finiteness hypotheses it corresponds to geometrically discrete, unramified stabilizers, but it does not require those stabilizers to be trivial. Orbifolds and moduli of stable curves are central examples.

For a smooth algebraic group \(G\) acting on a scheme \(X\), the map \(X\to[X/G]\) is a smooth surjective atlas under standard hypotheses, so the quotient is algebraic. If \(G\) is finite étale, the same atlas is étale and the quotient is Deligne--Mumford. These are examples, not a license to assume that every group action or every groupoid has an algebraic quotient stack.

Algebraicity is an extra theorem-shaped claim. One must prove descent, representability of the diagonal, and existence of the required atlas; none is contained in the word *moduli*.

## Coarse moduli spaces lose symmetry

A **coarse moduli space** for a stack \(\mathcal X\) is, roughly, an algebraic space \(M\) receiving a map

$$
\pi:\mathcal X\longrightarrow M
$$

that is universal for maps from \(\mathcal X\) to algebraic spaces and matches geometric isomorphism classes under appropriate hypotheses. It is designed to retain orbit-level geometry, not the full groupoid of families.

Consequently, \(M\) generally forgets:

- automorphism and stabilizer groups;
- how those groups vary in families;
- nontrivial torsors or gerbes over a point of \(M\);
- some deformation information on which stabilizers act; and
- the universal family that exists naturally over the stack.

This loss is sometimes exactly what is wanted: a coarse space may be easier to plot, compactify, or compare with classical invariants. But it cannot be used interchangeably with the stack when symmetry matters. The map \(BG\to *\) is the limiting example: the coarse target can be one point while the source remembers the whole group \(G\).

## The two-dimensional logic of stacks

Stacks naturally form a \((2,1)\)-category:

- stacks are objects;
- functors compatible with pullback are \(1\)-morphisms; and
- natural isomorphisms between those functors are \(2\)-morphisms.

The \(2\)-morphisms are invertible. As a result, constructions are often canonical up to a specified isomorphism rather than by literal equality. A fiber product of stacks is a **2-fiber product**: an object includes not only objects from the two factors, but an isomorphism between their images in the base stack.

This is not dispensable formalism. It is what keeps track of the witness that two families agree. Suppressing the \(2\)-isomorphism can turn a correct universal property into a false set-theoretic one.

Ordinary stacks in groupoids are nevertheless only one level of higher geometry. If objects have nontrivial morphisms between morphisms, and then transformations between those, one needs higher groupoids and higher stacks. Derived stacks add homological and infinitesimal information. Neither extension is implied by the bare word *stack*.

## Use in algebraic geometry and physics

Stacks are used wherever objects vary in families and possess automorphisms:

- moduli of curves, abelian varieties, bundles, sheaves, and maps;
- quotients by group actions, especially with fixed points;
- orbifolds and quotient singularities;
- deformation theory, where stabilizers act on infinitesimal deformations;
- intersection theory on moduli spaces with symmetry; and
- classification of [[basic-concepts/torsors/inq|torsors]] and forms by descent.

In physics, stack-like structures arise in quotients of field configurations by gauge transformations, moduli of gauge fields and connections, orbifolds, and parameter spaces carrying anomaly or determinant line bundles. The stack retains residual gauge symmetry at configurations with stabilizers, where a naive orbit space may be singular or misleading.

These physical examples are not automatically algebraic stacks. Spaces of smooth fields are often infinite-dimensional; gauge equivalences may call for differentiable, topological, derived, or higher stacks; and path integrals require analytic and measure-theoretic structure absent from the definition of a stack. Writing \([\mathcal F/\mathcal G]\) organizes the quotient problem but does not construct the measure, action, quantum theory, or renormalization.

## Use in the cosmodynamics programme

A stack could formalize one possible meaning of “compatible local descriptions form one cosmos,” but only after the project's data have been assigned exact types. One possible schematic fiber over a causal or observer region \(O\) might be a groupoid

$$
\mathcal X(O)
=\{(g_O,\mathcal A_O,\omega_O,\ldots)
\text{ and their admissible isomorphisms}\}.
$$

For this to be a stack rather than an analogy, the construction must provide:

1. a base category or site of regions, contexts, or scale presentations;
2. a declared topology saying which families cover a context;
3. a groupoid of local objects and a physical meaning for every automorphism;
4. pullback or restriction functors with coherent composition laws;
5. sheaf descent for isomorphisms and effective descent for objects; and
6. if *algebraic stack* is claimed, a scheme-theoretic functor of points, representable diagonal, and smooth atlas.

The mixed variance noted in [[basic-concepts/fibers/inq|the local-fiber architecture]] is a real obstacle: observable algebras in algebraic QFT are usually covariant under inclusions of regions, while states restrict contravariantly. Placing \((\mathcal A_O,\omega_O)\) in one tuple does not automatically create a contravariant groupoid-valued pseudofunctor. A fibration, opfibration, net, sheaf, cosheaf, or coupled construction may be the correct object; its variance has to be derived from the operations actually available.

The same restraint applies to [[basic-concepts/soldering/inq|soldering]] maps among causal, metric, quantum, and thermodynamic registers. Such maps can be included as structure on objects of a stack only after their source, target, equivariance, and pullback laws are defined. They must then themselves satisfy descent.

Even a successful stack would solve a local-to-global **presentation** problem, not every problem in [[cosmodynamics/construction-programme|the cosmodynamics construction programme]]. It would not by itself select a quantum outcome, make a fact, stabilize a record, choose a metric scale, produce an irreversible arrow, or recover QFT and GR. [[cosmodynamics/fact-record-history|Fact, record, and history]] contain one-sided and realizability claims that cannot be obtained solely from invertible isomorphisms in fiber groupoids.

The useful promise is narrower and exact: a stack can state when local models with symmetry are genuinely the local presentations of one global object. It can also reveal the obstruction when they are not.

## Boundaries of the concept

- A stack is not a layered list of assumptions or a software architecture.
- A groupoid-valued assignment is not a stack until the topology, pullbacks, and descent theorem are supplied.
- Taking isomorphism classes before descent can erase the cocycles and automorphisms needed for gluing.
- A quotient stack \([X/G]\) is not the orbit space \(X/G\).
- A stack need not be representable, algebraic, Deligne--Mumford, finite-dimensional, separated, or proper.
- Stackification enforces descent; it does not establish algebraicity or physical correctness.
- A coarse moduli space deliberately forgets stabilizers and should not be substituted for the stack in symmetry-sensitive arguments.
- An atlas is a presentation, not a preferred global coordinate system, and different atlases may present equivalent stacks.
- Descent provides a global object up to coherent isomorphism; it does not choose a preferred representative or trivialization.
- A physical gauge quotient may require differentiable, derived, or higher structures beyond algebraic stacks.

The governing idea is that a whole can be locally present without being locally rigid. A stack makes the whole recoverable while preserving the transformations by which its local presentations are the same.
