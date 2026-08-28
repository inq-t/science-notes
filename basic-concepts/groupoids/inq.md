---
inq.module: "groupoids"
inq.include:
  - "**/*.md"
---
# Groupoids

A groupoid is a category in which every arrow is invertible. Its objects name presentations, positions, frames, or configurations, while its arrows name reversible identifications or transformations between them. A groupoid therefore remembers both which objects are equivalent and *how* they are equivalent, including the symmetries that leave each object fixed. This is why groupoids are the natural grammar of [[basic-concepts/descent/inq|descent]], quotient constructions, and moduli problems: an orbit set remembers equivalence classes, but a groupoid also remembers the identifications and automorphisms that make those classes.

## Reversible arrows with many objects

A category \(\mathcal G\) consists of objects, sets of arrows

$$
\operatorname{Hom}_{\mathcal G}(x,y),
$$

identity arrows \(\operatorname{id}_x\), and associative composition. It is a **groupoid** when every arrow

$$
g:x\longrightarrow y
$$

has an inverse \(g^{-1}:y\to x\) satisfying

$$
g^{-1}g=\operatorname{id}_x,
\qquad
gg^{-1}=\operatorname{id}_y.
$$

The arrows should not automatically be read as physical processes. They may be changes of coordinates, gauge transformations, isomorphisms of bundles, paths up to a reversible equivalence, or alternate local presentations of one object. What unifies these examples is that an arrow can be undone without loss inside the structure being modeled.

Several familiar notions sit at the edges of this definition.

- A **set** becomes a discrete groupoid by giving each element only its identity arrow.
- A **group** is a groupoid with one object. Its elements are the automorphisms of that object.
- An **equivalence relation** on a set gives a groupoid with at most one arrow between any ordered pair of objects: there is one precisely when the objects are equivalent.
- A general groupoid can have many arrows between the same objects and nontrivial arrows from an object to itself.

Thus a groupoid is not merely a group with several objects, and it is not merely an equivalence relation. It combines the partition into equivalence classes with the symmetry carried inside each class.

## Orbits and isotropy

Two objects are in the same **orbit**, or connected component, when at least one arrow joins them. The set of components is often written

$$
\pi_0(\mathcal G)
=\operatorname{Ob}(\mathcal G)/{\cong}.
$$

This is the equivalence-relation shadow of the groupoid. Passing to \(\pi_0(\mathcal G)\) forgets how many identifications exist and which symmetries survive at each object.

The **isotropy group** or automorphism group at \(x\) is

$$
\mathcal G_x
=\operatorname{Aut}_{\mathcal G}(x)
=\operatorname{Hom}_{\mathcal G}(x,x).
$$

If \(h:x\to y\), conjugation gives an isomorphism

$$
\mathcal G_x\longrightarrow\mathcal G_y,
\qquad
a\longmapsto hah^{-1}.
$$

The isomorphism depends on the chosen arrow \(h\). Consequently, all isotropy groups in one connected component are isomorphic, but generally not canonically isomorphic. Choosing an object in a connected groupoid makes that groupoid equivalent to its isotropy group viewed as a one-object groupoid. The choice is precisely what suppresses the other objects; the equivalence does not say that the original groupoid was literally a group.

This distinction is decisive in moduli theory. Two curves can represent the same isomorphism class while possessing different visible presentations, and one curve can have several self-isomorphisms. The orbit set records only the class; the groupoid records the curve together with its automorphisms.

## Basic examples

### The pair groupoid

For a set or space \(X\), the **pair groupoid** has object space \(X\) and exactly one arrow from every \(x\) to every \(y\). Its arrows can be written

$$
X\times X\rightrightarrows X,
$$

with \((y,x)\) the arrow \(x\to y\), and composition

$$
(z,y)\circ(y,x)=(z,x).
$$

If \(X\) is nonempty, the pair groupoid has one orbit and trivial isotropy. It says that all objects are uniquely comparable; it does not say that they are literally the same object.

For a finite set of \(n\) points, the convolution algebra of the pair groupoid has basis \(e_{ij}\) with

$$
e_{ij}e_{kl}=\delta_{jk}e_{il},
$$

and is therefore \(M_n(k)\) over a coefficient field \(k\). This is a useful bridge from arrows to matrix algebra, but it is not automatic quantization. For a general topological or measured groupoid, forming a convolution algebra requires choices of function class, topology, measure or Haar system, and completion.

### The action groupoid

If a group \(G\) acts on \(X\), the **action groupoid** is

$$
G\times X\rightrightarrows X,
$$

where

$$
s(g,x)=x,
\qquad
t(g,x)=g\cdot x.
$$

An arrow from \(x\) to \(y\) is a group element carrying \(x\) to \(y\). The orbit of \(x\) is its ordinary \(G\)-orbit, while its isotropy group is the stabilizer

$$
G_x=\{g\in G:g\cdot x=x\}.
$$

The orbit set \(X/G\) forgets every stabilizer. The action groupoid retains them, including the fact that an object can be equivalent to itself in several nontrivial ways. This is the prototype of a quotient groupoid and, after imposing descent, of the quotient [[basic-concepts/stacks/inq|stack]] \([X/G]\).

### The Čech groupoid of a cover

Let \(p:U\to X\) be a cover. Its **Čech groupoid** is

$$
U\times_XU\rightrightarrows U,
$$

with source and target the two projections. A point of \(U\times_XU\) is a pair of presentations in \(U\) that lie over the same point of \(X\); it is therefore an arrow identifying those presentations. Composition is induced on

$$
U\times_XU\times_XU
$$

by forgetting the middle presentation.

This groupoid does not primarily encode a symmetry acting on \(X\). It encodes the redundancy introduced by the cover. Under the hypotheses that make \(U\to X\) an effective cover, quotienting this redundancy recovers \(X\). The double and triple fiber products that appear here are exactly the domains on which [[basic-concepts/gluing/inq|overlap maps]] and cocycle equations live.

The pair groupoid is the Čech groupoid of the map \(X\to *\). The two examples express the same pattern at different levels: arrows certify that two presentations have a common image.

### The fundamental groupoid

For a topological space \(X\), the **fundamental groupoid** \(\Pi_1(X)\) has points of \(X\) as objects and endpoint-preserving homotopy classes of paths as arrows. Reversing a path supplies the inverse. Its isotropy group at \(x\) is the fundamental group

$$
\operatorname{Aut}_{\Pi_1(X)}(x)=\pi_1(X,x).
$$

Using all basepoints avoids selecting one privileged point. A connected space gives a connected fundamental groupoid, but identifications between the groups \(\pi_1(X,x)\) at different basepoints depend on paths and are canonical only up to conjugation. The groupoid records exactly that dependence.

A flat connection determines holonomy that factors through \(\Pi_1(X)\). A connection with curvature generally depends on more than ordinary endpoint-fixed homotopy; its parallel transport is naturally formulated on a path groupoid or a thin-homotopy groupoid instead. The distinction prevents the word *holonomy* from silently imposing flatness.

### Gauge groupoids

Let \(P\to M\) be a principal right \(G\)-bundle. Its **gauge groupoid** has points of \(M\) as objects and arrows

$$
\operatorname{Hom}_G(P_x,P_y)
$$

from \(x\) to \(y\): equivariant bijections between the two \(G\)-[[basic-concepts/torsors/inq|torsor]] fibers. Equivalently, its arrow bundle is

$$
(P\times P)/G\rightrightarrows M,
$$

where \(G\) acts diagonally. Its isotropy at \(x\) is noncanonically isomorphic to \(G\); intrinsically these isotropy groups form the adjoint group bundle \(P\times^G G\), with \(G\) acting on itself by conjugation.

A related but different construction takes fields or connections as objects and gauge transformations as arrows. That action groupoid expresses “configuration modulo gauge” without collapsing gauge-equivalent configurations to a bare orbit set. The first gauge groupoid belongs to the geometry of one principal bundle; the second belongs to the moduli of its fields. They should not be conflated.

## Groupoid objects in geometry

The definition of groupoid can be made **internal** to any category with the required fiber products. A groupoid object in schemes consists of an object scheme \(U\), an arrow scheme \(R\), and structure maps

$$
R\mathrel{\substack{\xrightarrow{\ t\ }\\[-0.5ex]\xrightarrow[\ s\ ]{}}}U,
\qquad
e:U\to R,
\qquad
i:R\to R,
$$

together with composition

$$
m:R\times_{s,U,t}R\longrightarrow R.
$$

These maps satisfy the ordinary source, target, identity, associativity, and inverse equations as equalities of morphisms of schemes. Writing the laws internally is stronger than declaring that the sets of rational points happen to form groupoids: it makes the construction compatible with arbitrary test schemes and retains nilpotent and arithmetic structure.

Two standard internal groupoids are immediate:

- an action of a group scheme \(G\) on a scheme \(X\) gives \(G\times X\rightrightarrows X\);
- a morphism \(U\to X\) gives the Čech groupoid \(U\times_XU\rightrightarrows U\).

For smooth manifolds, a **Lie groupoid** is an internal groupoid with smooth object and arrow manifolds and suitable submersion conditions on source and target. For schemes or algebraic spaces, the geometric properties of \(s\), \(t\), and the diagonal control whether the resulting quotient has the desired algebraic behavior. The word *groupoid* alone supplies the composition laws; it does not supply smoothness, separatedness, finiteness, or representability.

## Quotients: what is retained and what is lost

Given \(R\rightrightarrows U\), one can form several different notions of quotient.

The **orbit set** identifies objects joined by an arrow. A sheaf quotient improves its behavior under localization. A **quotient stack** \([U/R]\) goes further: over every test scheme it retains families of objects, their local presentations, and their isomorphisms. These outputs can agree only in favorable cases.

The loss from passing directly to orbits is already visible for an action groupoid. A fixed point and a free orbit can both become single points of \(X/G\), although the first has a nontrivial stabilizer and the second does not. The quotient stack remembers that distinction through isotropy. It also remembers twisting: a map into \([X/G]\) may be represented by a nontrivial \(G\)-torsor with an equivariant map to \(X\), not merely by a global point of \(X\).

Conversely, an internal groupoid need not have a quotient representable by a scheme. It may be represented only by an algebraic space, by an algebraic stack, or by no algebraic object of the desired kind. A presentation \(R\rightrightarrows U\) and the quotient it presents are also different levels of description: distinct groupoids can present equivalent stacks. The relevant invariance is often **Morita equivalence**, not isomorphism of the chosen presentations.

## Groupoids are the grammar of descent

Suppose an object \(x\) is given over a cover \(U\to X\). Its two pullbacks to \(U\times_XU\) need not be equal; they are compared by an isomorphism

$$
\theta:p_1^*x\xrightarrow{\sim}p_2^*x.
$$

On \(U\times_XU\times_XU\), the cocycle equation says that two composites of these reversible comparisons are the same arrow. Objects, isomorphisms, and compositions therefore form a groupoid before one asks whether the descent datum is effective.

This is why a moduli problem is naturally organized as a groupoid for every test scheme \(T\):

$$
\mathcal M(T)
=\{\text{families over }T\text{ and their isomorphisms}\}.
$$

Pullback along \(T'\to T\) gives a functor between groupoids. When these groupoids satisfy descent, they form a [[basic-concepts/stacks/inq|stack]]. Replacing each \(\mathcal M(T)\) by its set of isomorphism classes too early can destroy the gluing information, because locally chosen isomorphisms can differ by automorphisms on overlaps.

## Use in algebraic geometry and physics

Groupoids are used to organize:

- equivalence relations and quotient presentations;
- atlases of algebraic spaces and stacks;
- moduli of curves, bundles, sheaves, maps, and connections;
- monodromy and transport with more than one basepoint;
- orbifolds and quotient singularities, where stabilizer data are geometrically significant;
- gauge configurations and gauge transformations; and
- convolution algebras associated with reversible relational data.

Their physical meaning depends on what the arrows denote. Gauge transformations are redundancies or symmetries of description; paths are possible transports; isomorphisms of local models are changes of presentation. None of these is automatically an irreversible event. A groupoid can describe which descriptions count as the same physical configuration while saying nothing about which configuration becomes actual or which transition occurs in time.

## Use in the cosmodynamics programme

Groupoids offer a disciplined language for the project's local descriptions. If a causal region, observer context, scale presentation, or local model can be represented in several reversible ways, those presentations may be objects and their admissible equivalences may be arrows. Isotropy would then record transformations that preserve one local presentation, and a quotient stack could retain that symmetry while organizing compatible families.

This possibility sharpens the local-to-global obligation in [[cosmodynamics/construction-programme|the cosmodynamics construction programme]]. A construction would have to specify:

1. what the objects are—regions, frames, algebra-state pairs, facts, or models;
2. which comparisons are invertible and therefore belong in a groupoid;
3. what the isotropy groups mean physically;
4. how objects and arrows pull back along refinements or changes of context; and
5. whether their descent data are effective.

The type distinctions in [[cosmodynamics/registers-and-type-discipline|register and type discipline]] matter here. Causal precedence \(x\preceq y\) is generally not invertible, so the causal order is a category or poset, not a groupoid. Formation of a record and growth of a history are likewise intended to be one-sided in [[cosmodynamics/fact-record-history|facts, records, and common history]]. Encoding them solely by reversible arrows would erase the very orientation the theory seeks to explain. The difference mirrors [[sufficient-reason/algebraic-and-statistical-arrows|the distinction between reversible algebraic flow and a statistical arrow]].

Nor does a pair groupoid on a collection of branches, sheets, or outcomes by itself prove that the associated matrix algebra is the physical observable algebra. One must justify why those arrows exist, why convolution is the appropriate algebraic operation, which representation is physical, and how established quantum structure is recovered. The matrix multiplication is exact once the pair groupoid algebra is chosen; the choice of that groupoid algebra is a separate construction.

## Boundaries of the concept

- Groupoid arrows are invertible. A genuinely lossy process, inclusion, causal precedence, or measurement update is not an arrow of a groupoid unless only its reversible change-of-presentation aspect is being modeled.
- Two objects in one orbit need not be equal, and an equivalence of groupoids need not be an isomorphism of their chosen presentations.
- Taking isomorphism classes discards isotropy and can break descent in families.
- An action groupoid remembers stabilizers; the orbit set does not.
- An internal groupoid in schemes does not automatically have a scheme quotient, an algebraic stack quotient, or good separation properties.
- A groupoid presentation is not intrinsic. Claims about the quotient should be invariant under the appropriate equivalence of presentations.
- A convolution algebra is additional analytic or algebraic structure built from a groupoid, not part of the bare definition.

The governing insight is that identity can have structure. A groupoid replaces the blunt assertion “these objects are the same” with reversible arrows that state exactly how they are identified and which symmetries remain after the identification.
