# Torsors

A torsor is a space on which a group acts freely and transitively: it has all the relative structure of the group but no preferred identity element. In algebraic geometry, a $G$-torsor over a base $X$ is a family that becomes isomorphic to $G$ after passing to a chosen notion of local cover, although it may admit no global trivialization. Torsors therefore give a precise language for locally available choices—frames, phases, coordinates, solutions—whose differences are canonical even when none of the choices is.

## A group with its origin forgotten

Let $G$ be a group. A **right $G$-torsor** is a nonempty set $P$ with a right action

$$
P\times G\longrightarrow P,
\qquad
(p,g)\longmapsto p\cdot g,
$$

such that for every $p,q\in P$ there is a unique $g\in G$ satisfying

$$
q=p\cdot g.
$$

Equivalently, the map

$$
P\times G\longrightarrow P\times P,
\qquad
(p,g)\longmapsto (p,p\cdot g)
$$

is a bijection. Freeness gives uniqueness; transitivity gives existence.

This condition defines a canonical **difference map**

$$
\delta:P\times P\longrightarrow G,
\qquad
q=p\cdot\delta(p,q).
$$

Thus two points of $P$ have a well-defined relative displacement even though no point is intrinsically zero. Choosing $p_0\in P$ creates an isomorphism

$$
G\overset{\sim}{\longrightarrow}P,
\qquad
g\longmapsto p_0\cdot g,
$$

but this isomorphism depends on $p_0$. If $p_1=p_0\cdot h$ is chosen instead, the coordinate of a point changes from $g$ to $h^{-1}g$. A torsor is consequently not just “a group without an identity”: the acting group and its action remain specified, while multiplication of two points of $P$ is not canonical.

The phrase **principal homogeneous space** is often synonymous with torsor, especially over a field. “Homogeneous” records transitivity; “principal” records the absence of stabilizers.

## Torsors over a scheme

Let $X$ be a scheme, let $G\to X$ be a group scheme, and choose a Grothendieck topology $\tau$, such as the Zariski, étale, fppf, or fpqc topology. A right $G$-torsor $P\to X$ is a [[basic-concepts/sheafs/entry|sheaf]] with a right $G$-action such that

1. $P$ has sections locally for $\tau$; and
2. the canonical map

   $$
   P\times_XG\longrightarrow P\times_XP,
   \qquad
   (p,g)\longmapsto(p,p\cdot g),
   $$

   is an isomorphism of sheaves.

When $P$ is representable, this is the usual geometric object also called a principal $G$-bundle. The topology is part of the assertion. A family may be trivial étale-locally but not Zariski-locally, so “locally a copy of $G$” is incomplete until *locally* has been specified.

Each geometric fiber is a simply transitive $G$-space, but fiberwise nonemptiness does not supply a global section. A section $s:X\to P$ does much more: it gives the equivariant trivialization

$$
G\overset{\sim}{\longrightarrow}P,
\qquad
g\longmapsto s\cdot g.
$$

Conversely, a trivialization sends the identity section of $G$ to a section of $P$. Hence

$$
P\text{ is globally trivial}
\quad\Longleftrightarrow\quad
P\text{ has a global section}.
$$

Over $X=\operatorname{Spec}k$, this becomes the sharp statement that a representable $G$-torsor is trivial precisely when it has a $k$-rational point. It may have points over an algebraic closure, or over every member of a chosen local cover, without having a point over $k$.

## Transition functions and $H^1$

Choose a cover $\{U_i\to X\}$ on which $P$ has sections $s_i$. On an overlap $U_{ij}$ there is a unique

$$
g_{ij}\in G(U_{ij})
$$

such that

$$
s_j=s_i\cdot g_{ij}.
$$

Uniqueness forces the cocycle equation

$$
g_{ij}g_{jk}=g_{ik}
$$

on triple overlaps. If the local origins are changed to $s_i'=s_i\cdot h_i$, then

$$
g'_{ij}=h_i^{-1}g_{ij}h_j.
$$

The transition functions are therefore not intrinsic one by one; their equivalence class is. This is the basic mechanism relating torsors to [[basic-concepts/gluing/entry|gluing]] and [[basic-concepts/descent/entry|descent]]: local trivial objects are identified on overlaps, the cocycle equation makes those identifications coherent, and descent asks whether the coherent local data come from a global object.

Isomorphism classes of $G$-torsors are classified by nonabelian cohomology

$$
H^1_\tau(X,G).
$$

For a general noncommutative $G$, this $H^1$ is a **pointed set**, not a group; its distinguished point is the trivial torsor. If $G$ is abelian, $H^1$ inherits a group law. A chosen trivializing cover gives Čech cocycles as above, but a computation on one cover should not be silently identified with the full sheaf-cohomological $H^1$ unless the relevant comparison hypotheses are known.

The cohomology class does not measure the size of a torsor. It records the obstruction to choosing compatible local origins globally.

## Line bundles as $\mathbf G_m$-torsors

Let $L$ be a line bundle on $X$. Its bundle of frames is

$$
L^\times:=\operatorname{Isom}_X(\mathcal O_X,L).
$$

A frame can be multiplied by an invertible function, so $L^\times$ is a $\mathbf G_m$-torsor. A nowhere-vanishing global section of $L$ is exactly a global frame and therefore exactly a trivialization. An arbitrary section, which may vanish, does not trivialize $L$.

Conversely, a $\mathbf G_m$-torsor $P$ produces a line bundle through the associated-bundle construction

$$
L=P\times^{\mathbf G_m}\mathbf A^1.
$$

If local frames $e_i$ satisfy $e_j=e_i g_{ij}$, their invertible transition functions $g_{ij}\in\mathcal O_X^\times(U_{ij})$ form a cocycle. Tensor product supplies the group law, yielding

$$
\operatorname{Pic}(X)
\simeq
H^1(X,\mathbf G_m).
$$

This example captures the point of the notion: every sufficiently small region has a generator of the line, but the geometry lies in whether those generators can be made into one global choice.

For a rank-$n$ vector bundle $E$, the same construction with ordered bases gives its frame torsor

$$
\operatorname{Fr}(E)=\operatorname{Isom}_X(\mathcal O_X^n,E),
$$

a $\operatorname{GL}_n$-torsor. The [[basic-concepts/soldering/entry|solder form]] becomes possible when such an internal frame bundle is identified with the frame geometry of tangent directions.

## Arithmetic examples

### Galois extensions

If $L/k$ is a finite Galois extension with group $\Gamma$, then

$$
\operatorname{Spec}L\longrightarrow\operatorname{Spec}k
$$

is an étale torsor under the constant group scheme $\Gamma_k$. After an étale base change it becomes a disjoint union of copies of the base, just like the trivial torsor. For a nontrivial extension it has no $k$-point and hence no global choice of one Galois-conjugate embedding as an origin.

A Kummer equation gives a smaller model. If $n$ is invertible in $k$ and $a\in k^\times$, then

$$
\operatorname{Spec}k[t]/(t^n-a)
$$

is a finite étale $\boldsymbol\mu_n$-torsor. It is trivial exactly when $a$ is an $n$th power in $k$. The roots are related transitively by multiplication by $n$th roots of unity, but no root need be defined over $k$.

### Genus-one curves

A smooth projective genus-one curve $C/k$ has a Jacobian elliptic curve

$$
E=\operatorname{Pic}^0(C).
$$

The curve $C$ is naturally a torsor under $E$. Its class lies in

$$
H^1(k,E).
$$

If $C(k)\neq\varnothing$, choosing a rational point turns $C$ into an elliptic curve by declaring that point to be zero, and the torsor becomes trivial. Without such a point, $C$ retains the relative addition supplied by $E$ but has no $k$-rational origin. This is one of the clearest cases in which “no preferred origin” is an arithmetic fact rather than a matter of taste.

Local solubility need not imply global solubility. A torsor can have points over all completions of a number field and still have no rational point; such failures of a local-to-global principle are detected by further arithmetic obstructions. The bare word *local* must therefore be kept distinct among scheme-theoretic covers, field extensions, and completions at places.

## Spaces of choices in geometry and physics

Torsors recur whenever differences are meaningful before absolute values are.

- The set of affine origins on an affine space is a torsor under its translation vector space. Likewise, when nonempty, the space of connections on a fixed smooth principal bundle is an affine torsor under $\Omega^1(M,\operatorname{ad}P)$: the difference of two connections is a well-defined adjoint-valued one-form, although a connection is not itself such a form canonically.
- The set of frames of a vector-space fiber is a $\operatorname{GL}_n$-torsor. Choosing a frame gives components; changing the frame acts by the structure group. The components are choice-dependent while the geometric object is not.
- The normalized vectors representing a fixed ray in complex Hilbert space form a $U(1)$-torsor. Relative phase is defined, but a quantum ray supplies no preferred phase representative.
- Given a conformal class $[g]$ on a smooth manifold, its metric representatives form a torsor under positive smooth functions acting by $g\mapsto\Omega^2g$. Choosing a conformal scale selects a representative; the causal order alone does not select one. This is the choice isolated in [[causal-scale-master/causal-order|causal order and metric scale]].

For this project, torsor language is most valuable as a discipline of **relative determination**. It separates an invariant relation between two choices from a chosen basepoint, gauge, phase, frame, or scale. A physical principle that selects one member of a torsor is extra data: the mere existence of the torsor neither supplies the selection nor proves that nature makes one.

[[sufficient-reason/facticity-and-pointing|Facticity and pointing]] uses this distinction to separate nonemptiness from the existence of a distinguished or globally compatible point. The torsor example makes that distinction exact, but it remains an analogy for a quantum state or spectral presheaf unless an acting group, a free transitive action, and the relevant local trivializations are actually constructed.

## Boundaries of the concept

- A transitive $G$-space $G/H$ is not a $G$-torsor unless the stabilizer $H$ is trivial.
- A bundle whose fibers happen to look like $G$ is not yet a torsor; it needs a specified action and the local triviality condition in a specified topology.
- Choosing a section trivializes a torsor but does not make that section canonical.
- Trivial geometric fibers do not imply a trivial global family.
- For nonabelian $G$, $H^1(X,G)$ has no natural addition in general. Treating torsor classes as an abelian obstruction group loses essential ordering information.
- Calling a collection of possibilities “torsor-like” is only justified after identifying the acting group and proving freeness and transitivity. Metaphorical absence of an origin is not enough.

The governing distinction is simple: a torsor contains no absolute point, but it contains exact laws for how any point is related to every other one.
