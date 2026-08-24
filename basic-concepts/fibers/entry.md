# Fibers

A fiber is what a varying object becomes when the parameter beneath it is held fixed. For a morphism of schemes $f:X\to S$, the fiber over $s\in S$ is not merely the inverse image of a point but the base change $X_s=X\times_S\operatorname{Spec}\kappa(s)$, which retains the functions, residue field, multiplicities, and infinitesimal structure present at that parameter value. Fibers expose the *vertical* content of a family; they do not by themselves say how different parameter values are identified, transported, or assembled into one global object.

## What lies over a point

For a map of sets

$$
f:X\longrightarrow S,
$$

the fiber over $s\in S$ is the inverse image

$$
f^{-1}(s)=\{x\in X:f(x)=s\}.
$$

This elementary definition already contains the governing idea. The base $S$ records a mode of variation, and the fiber records the possibilities compatible with one fixed base value. The base might represent position, time, scale, a coupling, a moduli parameter, or an arithmetic prime. What a fiber *means* therefore depends on what the map means.

In geometry, however, a set of points is generally too poor. It forgets which functions exist on those points, over which field they are defined, whether points occur with multiplicity, and whether infinitesimal directions survive after the parameter is fixed. Algebraic geometry replaces inverse image by pullback.

## The scheme-theoretic fiber

Let $f:X\to S$ be a morphism of schemes and let $s\in S$. The point $s$ has a residue field

$$
\kappa(s)=\mathcal O_{S,s}/\mathfrak m_s
$$

and hence a canonical morphism $\operatorname{Spec}\kappa(s)\to S$. The fiber of $f$ at $s$ is

$$
\boxed{X_s:=X\times_S\operatorname{Spec}\kappa(s).}
$$

Thus taking a fiber is a special case of base change: it is the universal way to impose the condition “the base is $s$.” The underlying points lie over $s$, while the structure sheaf records the algebra that remains after localization at $s$ and specialization to its residue field.

In the affine case, a morphism

$$
\operatorname{Spec}B\longrightarrow\operatorname{Spec}A
$$

comes from a ring map $A\to B$. If $s$ corresponds to $\mathfrak p\subset A$, then

$$
X_s
=\operatorname{Spec}\bigl(B\otimes_A\kappa(\mathfrak p)\bigr)
\cong
\operatorname{Spec}\bigl((A\setminus\mathfrak p)^{-1}B/\mathfrak p(A\setminus\mathfrak p)^{-1}B\bigr).
$$

The two operations have distinct meanings: localization discards behavior away from $s$, and quotienting by $\mathfrak p$ fixes the base parameters at their values at $s$.

### Multiplicity invisible to sets

Let $k$ be algebraically closed of characteristic different from $2$, and consider

$$
f:\mathbb A^1_x\longrightarrow\mathbb A^1_t,
\qquad t=x^2.
$$

Algebraically, $k[t]\to k[x]$ sends $t$ to $x^2$. For $a\ne0$, the fiber is

$$
X_a=\operatorname{Spec}k[x]/(x^2-a),
$$

which consists of two reduced points. At $a=0$,

$$
X_0=\operatorname{Spec}k[x]/(x^2).
$$

Its underlying set has one point, but its coordinate ring contains the nonzero nilpotent class of $x$. The scheme-theoretic fiber therefore remembers that two points have coalesced with multiplicity. The set-theoretic fiber sees only one point and loses precisely the structure that distinguishes a transverse intersection from a ramified one.

A fiber removes directions along the base. It may retain nilpotent structure created by the way the total space meets that base value, but one fiber does not retain the full law of variation normal to itself. For first-order and higher deformation data one needs additional structures such as relative differentials, a normal complex, or the cotangent complex.

## Ordinary and geometric fibers

The residue field $\kappa(s)$ need not be algebraically closed. This can make arithmetic and geometry appear together in the ordinary fiber. Choose an algebraically closed extension $\Omega/\kappa(s)$ and a geometric point

$$
\bar s:\operatorname{Spec}\Omega\longrightarrow S
$$

lying over $s$. The corresponding geometric fiber is

$$
X_{\bar s}:=X\times_S\operatorname{Spec}\Omega
\cong X_s\times_{\operatorname{Spec}\kappa(s)}\operatorname{Spec}\Omega.
$$

Geometric fibers ask what the fiber looks like after scalar obstructions have been removed. For example, $\operatorname{Spec}\mathbb C\to\operatorname{Spec}\mathbb R$ has an ordinary fiber with one point, whereas after extension to $\mathbb C$,

$$
\operatorname{Spec}\bigl(\mathbb C\otimes_{\mathbb R}\mathbb C\bigr)
\cong
\operatorname{Spec}(\mathbb C\times\mathbb C)
$$

has two components. The geometric fiber reveals the two conjugate embeddings that the real fiber packages together.

This is why algebraic geometers distinguish *reduced* from *geometrically reduced*, *connected* from *geometrically connected*, and *irreducible* from *geometrically irreducible*. A $\kappa(s)$-rational point is also stronger than a geometric point: the former is a section $\operatorname{Spec}\kappa(s)\to X_s$, while the latter may exist only after extending scalars.

## A family is more than its fibers

A morphism $f:X\to S$ presents $X$ as a family parametrized by $S$. Its fibers are members of that family, but the total space contains relations among them that no isolated member possesses.

Three distinctions are essential:

- A **fiber** is the object at one base value.
- A **section** $\sigma:S\to X$ with $f\circ\sigma=\operatorname{id}_S$ chooses one point $\sigma(s)\in X_s$ coherently for every $s$.
- A **transport law** or connection says how data in different fibers may be compared along motion in the base.

Neither a section nor a transport law is supplied by the bare existence of $f$. There is generally no canonical equality between $X_s$ and $X_{s'}$, even when the two fibers happen to be isomorphic. Indeed, every fiber can be isomorphic to the same model while the family remains globally nontrivial because its local identifications have monodromy or twisting. That global obstruction is expressed through [[basic-concepts/gluing/entry|gluing]], [[basic-concepts/descent/entry|descent]], and [[basic-concepts/torsors/entry|torsors]].

If $S$ is integral with generic point $\eta$, the generic fiber $X_\eta$ describes behavior over the function field $\kappa(\eta)$—often the behavior valid for a general parameter value. Closed or otherwise distinguished points can have special fibers with extra components, singularities, automorphisms, or nilpotents. The contrast between generic and special fibers is one of algebraic geometry's principal ways of studying degeneration.

## Flatness and smoothness govern different questions

Calling something a family does not make its fibers vary uniformly. Two conditions separate different senses of regular variation.

A morphism $f:X\to S$ is **flat** when each local ring $\mathcal O_{X,x}$ is a flat $\mathcal O_{S,f(x)}$-module. Equivalently at the module level, tensoring with the varying algebra preserves finite relations instead of destroying exactness. Flatness thereby rules out many torsion-driven jumps under specialization. In a projective flat family, the Hilbert polynomial of the fibers is locally constant. Flatness is consequently a strong algebraic notion of continuity, but it does not say that all fibers are smooth, reduced, irreducible, or mutually isomorphic. The map $t=x^2$ above is finite flat of rank two, although its fiber at $0$ is nonreduced.

A morphism is **smooth** when it is locally of finite presentation, flat, and has geometrically regular fibers. Smoothness therefore adds the absence of fiberwise singularities. It is a condition on the map, not merely on the total and base schemes separately: both copies of $\mathbb A^1$ in $t=x^2$ are smooth over $k$, while the morphism between them is ramified and not smooth at $x=0$.

These conditions answer different questions:

$$
\begin{aligned}
\text{flatness}&:\quad\text{does algebraic size behave continuously under specialization?}\\
\text{smoothness}&:\quad\text{is that variation also free of geometric singularities?}
\end{aligned}
$$

Properness, by contrast, controls a relative analogue of compactness. Flat, smooth, and proper morphisms are all stable under base change, but none should be substituted for another.

## Vector bundles: linear fibers with coherent coordinates

Let $\mathcal E$ be a locally free $\mathcal O_S$-module of rank $n$. Its associated geometric vector bundle can be written

$$
\mathbb V(\mathcal E)
=\underline{\operatorname{Spec}}_S\operatorname{Sym}(\mathcal E^\vee)
\longrightarrow S.
$$

The fiber at $s$ is the affine space associated with the vector space

$$
\mathcal E_s:=\mathcal E\otimes_{\mathcal O_S}\kappa(s).
$$

Locally on $S$, the bundle is $\mathbb A^n\times S$, and changes of trivialization are maps into $\mathrm{GL}_n$ satisfying cocycle identities. A vector bundle is therefore not merely a vector space assigned to every point. It is a family whose local bases are related coherently on overlaps. A section is a varying vector—a classical field when the base is spacetime—not a fiber.

## Principal bundles: fibers without a preferred origin

Let $G\to S$ be a group scheme. A principal $G$-bundle, or $G$-torsor, is a space $P\to S$ with a right $G$-action such that $P\to S$ is a cover in the chosen topology and

$$
P\times_S G\longrightarrow P\times_S P,
\qquad (p,g)\longmapsto(p,pg)
$$

is an isomorphism. The relevant meaning of “locally” may be Zariski, étale, fppf, or another Grothendieck topology.

Each geometric fiber is acted on freely and transitively by the corresponding group fiber. It looks like $G$ only after one of its points has been chosen; that choice supplies an origin and hence a trivialization. A fiber can have geometric points while having no $\kappa(s)$-rational point, which is the arithmetic form of nontriviality. [[basic-concepts/torsors/entry|Torsors]] isolate this idea of a space of choices, while [[basic-concepts/descent/entry|descent]] explains how locally trivial fibers and their transition data determine a global bundle.

## Elliptic curves and degeneration

Let $k$ have characteristic different from $2$, and consider the projective cubic family

$$
E_t:\qquad y^2z=x(x-z)(x-tz)
$$

over the $t$-line. For $t\ne0,1$, the fiber is a smooth genus-one curve with the section $[0:1:0]$, hence an elliptic curve. At $t=0$ the equation becomes

$$
y^2z=x^2(x-z),
$$

and the geometric fiber is a nodal cubic. The family is flat: all fibers remain plane cubics with the same Hilbert polynomial and arithmetic genus. It is not smooth at the nodal fiber. The normalization of that special fiber has geometric genus zero, while the node accounts for the missing unit of arithmetic genus.

This example shows why degeneration is structure rather than mere failure. A singular fiber records how a smooth family reaches the boundary of its moduli space. Singular fibers are central in elliptic surfaces, compactifications of moduli, stable reduction, and arithmetic geometry. In mathematical physics, singular elliptic fibers and their resolutions also organize gauge data in F-theory; that application uses considerably more structure than the bare statement that a fiber is singular.

## Base change changes the observer, not the rule

Given any map $g:T\to S$, the pulled-back family is

$$
X_T:=X\times_S T\longrightarrow T.
$$

For $t\in T$ mapping to $s=g(t)$, its fiber satisfies

$$
(X_T)_t
\cong
X_s\times_{\operatorname{Spec}\kappa(s)}\operatorname{Spec}\kappa(t).
$$

Base change can mean restricting to an open part of parameter space, extending the ground field, passing to a cover, or reparametrizing the same family. It can split components, expose geometric points, or make a bundle locally trivial. Because the construction is a fiber product, it preserves the defining compatibility with the original base.

The reverse problem is descent: if an object is constructed after passing to a cover $T\to S$, when does it come from an object over $S$? Base change and [[basic-concepts/descent/entry|descent]] are therefore opposite movements. Base change localizes or enlarges the viewpoint; descent proves that compatible local viewpoints constitute one global object.

## Fibers in geometry and physics

Several standard physical constructions are genuinely fibered:

- A tangent bundle $TM\to M$ has tangent space $T_xM$ as its fiber at $x$. A vector field is a section $x\mapsto v_x$, not a collection of canonically identical tangent vectors.
- A principal gauge bundle $P\to M$ has gauge-group torsors over spacetime points. Matter fields are sections of associated vector bundles, while a gauge potential is a connection specifying comparison between neighboring fibers.
- A parameter-dependent eigenspace can form a vector or line bundle over parameter space. Its Berry connection and holonomy contain information absent from each eigenspace separately.
- In a family of elliptic curves, K3 surfaces, or Calabi--Yau varieties, special fibers and monodromy can control new massless sectors, dualities, or gauge enhancement. Those conclusions depend on the total family, singularity type, and physical compactification, not on the word “fiber” alone.

[[basic-concepts/soldering/entry|Soldering]] addresses a different operation: it relates fibers of different kinds over the same base—for example, an internal vector bundle to the tangent bundle. Sharing a base does not itself provide such an identification.

## Use in the cosmodynamics programme

The project proposes that established local QFT and GR may be imported as the local fibers of a larger cosmodynamic structure. The intended schema is

$$
O\longmapsto(g_O,\mathcal A_O,\omega_O),
$$

with $O$ a causal region. At present, “fiber” here names an architectural role, not a constructed morphism of schemes. In algebraic QFT, $O\mapsto\mathcal A(O)$ is ordinarily a net of algebras with inclusion maps; depending on variance and context, [[basic-concepts/sheafs/entry|sheaves]], cosheaves, bundles, [[basic-concepts/stacks/entry|stacks]], or fibrations may be better formal models than scheme fibers. A precise theory must specify the base category, the category in which the fibers live, their restriction or transport maps, and the compatibility law on overlaps. [[compatible-with-existing-physics/entry|Compatibility with existing physics]] states the preservation burden, and [[cosmodynamics/construction-programme|the cosmodynamic construction programme]] states the unresolved local-to-global burden.

The scale-indexed proposal similarly considers a family

$$
N\longmapsto(\mathcal A_N,\omega_N).
$$

An individual $N$ gives only one vertical algebra-state pair. If the algebras vary, expressions comparing $\omega_N$ with $\omega_{N'}$ require explicit identifications, inclusions, a connection, a cocycle, or relative data. Even if all $\mathcal A_N$ are one fixed algebra, the path of states and its physical interpretation remain additional structure. In particular, modular flow within one algebra-state fiber is not automatically horizontal motion through the family. This distinction is maintained in [[cosmodynamics/registers-and-type-discipline|register and type discipline]] and [[scale-as-modular-observable/entry|Scale as a Modular Observable]]; [[wall-construction-interface/cross-fiber-transport|cross-fiber transport and state selection]] states the missing comparison data explicitly.

The vocabulary becomes fruitful only when it exposes these obligations:

$$
\begin{aligned}
\text{local fiber data}&\ne\text{a global cosmos},\\
\text{isomorphic fibers}&\ne\text{canonical cross-fiber identity},\\
\text{a parameterized list of states}&\ne\text{a transport law},\\
\text{compatibility with local QFT}&\ne\text{recovery or derivation of QFT}.
\end{aligned}
$$

The deeper question is therefore not simply “what is in each fiber?” It is “what must the base, the fibers, and the relations among them be so that their totality is one object rather than an indexed inventory?” Fibers make that question precise by showing exactly what remains after a context is fixed—and, just as importantly, what has been lost by fixing it.
