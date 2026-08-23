# Descent

Descent is the theory of recognizing when an object seen after base change really comes from an object on the base. Given a cover $p:U\to S$, an object over $U$ appears twice over $U\times_SU$; a descent datum identifies those two appearances and requires the identifications to compose coherently over $U\times_SU\times_SU$. Descent is **effective** when this coherent upstairs object is the pullback of a downstairs object. It is the relative, isomorphism-sensitive form of [[basic-concepts/gluing/entry|gluing]].

## Recovering what base change has duplicated

Let $\mathcal F$ assign a category of objects $\mathcal F(T)$ to each scheme or space $T$, with pullback along maps. Fix a covering morphism

$$
p:U\longrightarrow S.
$$

The fiber product

$$
R=U\times_SU
$$

records pairs of points or generalized points of $U$ that represent the same point of $S$. Its two projections

$$
p_1,p_2:R\rightrightarrows U
$$

give two pullbacks of any $x\in\mathcal F(U)$. If $x$ came from $y\in\mathcal F(S)$, then $p_1^*x$ and $p_2^*x$ would be canonically isomorphic, because $p\circ p_1=p\circ p_2$.

A **descent datum** on $x$ is an isomorphism

$$
\theta:p_1^*x\xrightarrow{\sim}p_2^*x
$$

that is the identity along the diagonal $U\to U\times_SU$ and satisfies the cocycle equation on the triple fiber product $U^{[3]}=U\times_SU\times_SU$:

$$
p_{23}^*\theta\circ p_{12}^*\theta
=p_{13}^*\theta.
$$

Here $p_{ij}:U^{[3]}\to U\times_SU$ retains the $i$th and $j$th factors. The equation says that identifying the first presentation with the third directly gives the same result as identifying first with second and then second with third. It is a path-independence law for changes of presentation, not a dynamical evolution law.

The datum $(x,\theta)$ is **effective** if there are an object $y\in\mathcal F(S)$ and an isomorphism

$$
\alpha:p^*y\xrightarrow{\sim}x
$$

whose induced overlap comparison is $\theta$. Thus descent separates three questions:

1. can morphisms between downstairs objects be recovered from their pullbacks;
2. can one write coherent comparison data upstairs; and
3. does that datum actually arise from an object downstairs?

When $\mathcal F$ is organized as a category fibered in groupoids, the pullback construction gives a functor

$$
\mathcal F(S)\longrightarrow\operatorname{Desc}_{\mathcal F}(U/S).
$$

Its full faithfulness is descent for morphisms; its essential surjectivity is effective descent for objects. The assignment is a **stack** for a topology when this functor is an equivalence for every cover in that topology. For a set-valued assignment, the statement reduces to the ordinary sheaf condition.

## How descent differs from gluing

In elementary gluing, the $U_i$ are open subobjects already sitting inside $S$. In descent, $U\to S$ need not be an inclusion. It may be étale, faithfully flat, or a field extension, so its points and functions can be a redundant or enlarged presentation of the base.

An open cover is nevertheless a special case. Set

$$
U=\coprod_iU_i\longrightarrow S.
$$

Then

$$
U\times_SU=\coprod_{i,j}(U_i\cap U_j),
$$

and the descent isomorphism is precisely the family of transition maps on pairwise overlaps. The triple fiber product gives the usual triple-overlap cocycle. Thus gluing emphasizes assembly from subdomains; descent emphasizes invariance under changing the presentation of a base.

This distinction matters conceptually. A thing downstairs is not one more independent object added to all of its local appearances. It is what those appearances, together with their coherent identifications, jointly present.

## The topology specifies what “local” means

Descent is always relative to a class of covers. Different Grothendieck topologies expose different kinds of local triviality.

| Topology | Typical covers | What they make locally visible |
|---|---|---|
| Zariski | jointly surjective open immersions | ordinary affine charts, regular functions, vector-bundle trivializations |
| Étale | jointly surjective étale maps | unramified local coordinates, finite étale objects, many arithmetic forms |
| fppf | jointly surjective maps that are flat and locally of finite presentation | torsors for flat group schemes, including phenomena invisible étale-locally in positive characteristic |
| fpqc | faithfully flat quasi-compact covers, or the corresponding covering families | broad faithfully flat descent, especially for modules and quasi-coherent sheaves |

A statement that something exists “locally” is incomplete until the topology is named. An object may admit no Zariski-local trivialization yet become trivial on an étale or fppf cover. Conversely, making the cover class broader increases the burden on a purported sheaf or stack: it must make more descent data effective.

Taking a [[basic-concepts/fibers/entry|fiber]] is itself base change along $\operatorname{Spec}\kappa(s)\to S$. Descent asks the reverse kind of question: after restricting or extending the base, what comparison data prove that the resulting object still comes from $S$?

## Faithfully flat descent for modules

Let $A\to B$ be faithfully flat. An $A$-module $M$ pulls back to the $B$-module

$$
N=B\otimes_AM.
$$

Over $B\otimes_AB$, the two scalar extensions of $N$ are canonically identified, and that identification satisfies the cocycle condition over $B\otimes_AB\otimes_AB$. Faithfully flat descent says the converse as well: a $B$-module equipped with such a datum comes from an $A$-module, uniquely up to the appropriate isomorphism.

The recovery mechanism is visible in the exact beginning of the Amitsur complex:

$$
0\longrightarrow M
\longrightarrow B\otimes_AM
\rightrightarrows B\otimes_AB\otimes_AM.
$$

The two arrows insert the two copies of $B$. Their equalizer consists precisely of the elements whose two upstairs presentations agree. Flatness preserves the relations needed for this comparison; faithfulness ensures that base change detects rather than erases information.

Faithfulness is essential. The flat map $\mathbf Z\to\mathbf Q$ kills every torsion module after tensoring. For example,

$$
\mathbf Q\otimes_{\mathbf Z}\mathbf Z/n\mathbf Z=0.
$$

From the rationalized object alone one cannot recover whether the original module was zero or contained torsion. A change of base that forgets an entire region of algebraic information cannot support effective recovery.

The same principle extends from modules to quasi-coherent sheaves: they satisfy fpqc descent. This theorem is one reason faithfully flat covers are fundamental in algebraic geometry—they permit calculations after a convenient enlargement without changing which quasi-coherent object is being studied.

## Galois descent

Let $L/K$ be a finite Galois extension with group $G$. If a $K$-vector space $W$ is extended to $L$, then

$$
V=L\otimes_KW
$$

carries a semilinear $G$-action:

$$
g(\lambda v)=g(\lambda)g(v).
$$

Galois descent says conversely that an $L$-vector space with a compatible semilinear $G$-action has a $K$-form,

$$
W=V^G,
\qquad
L\otimes_KV^G\xrightarrow{\sim}V.
$$

For $\mathbf C/\mathbf R$, the datum is a conjugate-linear involution. Its fixed vectors form the real vector space from which the complex vector space descends. The complex object alone does not specify a preferred real form; the semilinear comparison is the additional descent datum.

This pattern is used for varieties, representations, algebras, and bundles over non-algebraically closed fields. Distinct descent data on the same object after base extension can yield distinct **forms** downstairs. Descent therefore explains both recoverability and twisting: local sameness need not imply global isomorphism.

## Line bundles and torsors

Suppose a line bundle becomes trivial after a cover $U\to S$. Its descent datum is then an invertible function on the double overlap,

$$
g\in\mathbb G_m(U\times_SU),
$$

whose pullbacks satisfy

$$
g_{12}g_{23}=g_{13}
$$

on $U^{[3]}$. Changing the chosen trivialization modifies $g$ by a coboundary. The resulting equivalence classes give the first cohomology class of the bundle; in familiar notation,

$$
\operatorname{Pic}(S)\cong H^1(S,\mathbb G_m).
$$

Replace $\mathbb G_m$ by a group object $G$ and the same construction gives a $G$-valued cocycle. Under the appropriate hypotheses it descends the trivial $G$-bundle on $U$ to a [[basic-concepts/torsors/entry|$G$-torsor]] on $S$. For noncommutative $G$, this is nonabelian $H^1$: it is naturally a pointed set rather than a group.

This is the geometric meaning of a torsor's “twist.” Locally it looks like the group acting on itself, but the descent datum says how the locally chosen origins differ. A global origin exists exactly when the cocycle is trivial up to a change of local trivializations.

## Effectivity and obstruction

Coherence is necessary but not universally sufficient. The following distinctions must be kept explicit.

- **The cover must detect information.** Nonfaithful base change can identify genuinely different downstairs objects.
- **The target category must admit effective descent.** Modules, quasi-coherent sheaves, schemes, and standard torsor categories satisfy strong descent theorems for appropriate topologies; an arbitrary presheaf of categories need not.
- **Objects and morphisms are separate tests.** Local morphisms can glue uniquely even when an object-level descent datum is not effective.
- **A property needs its own locality theorem.** Descending an object does not automatically show that every extra condition imposed upstairs survives downstairs.
- **Automorphisms change the logic.** Global forms are classified by cocycles modulo changes of trivialization, not by simply taking an equalizer of underlying sets.
- **Pairwise equivalence need not supply a cocycle.** Chosen pairwise isomorphisms can disagree on triple overlaps. In suitable lifting problems that mismatch defines a degree-two obstruction, but the relevant cohomology and even its being abelian depend on the automorphism structure.
- **A coherent quotient need not be representable in the desired category.** One may obtain a sheaf or algebraic space when one had demanded a scheme. Representability is an additional conclusion, not part of the word *descent*.

Descent also does not select a point, a physical outcome, a direction of time, or a preferred trivialization. It reconstructs an object from redundant presentations under stated hypotheses. Any stronger metaphysical or physical conclusion needs an additional argument.

## Use in algebraic geometry and physics

Descent is used to:

- define schemes, sheaves, bundles, and morphisms independently of coordinates;
- construct objects over a field from objects over a splitting field;
- classify twisted forms and principal bundles;
- treat moduli as stacks when automorphisms prevent a set-valued moduli space from carrying the right gluing law;
- pass to flat or étale covers where calculations become simple and then prove that the result is intrinsic; and
- formulate gauge fields and local frames without mistaking a choice of gauge for global structure.

For the cosmodynamics programme, descent offers a precise model of one possible meaning of “many local descriptions constitute one cosmos.” One would first need a base category or site of causal regions, observer contexts, or scale presentations; a declared class of covers; objects such as local algebras, states, metrics, facts, or records; and pullback or restriction maps of the correct variance. A candidate common object would then require overlap identifications and triple-overlap coherence, followed by an **effectivity theorem**. This sharpens the local-to-global requirement in [[cosmodynamics/construction-programme|the construction programme]] and the intrinsic-whole idea in [[cosmodynamics/cosmos-as-structure-of-facts|a cosmos as the structure of facts]]. It does not prove either one by analogy.

The project also uses *descent* in [[causal-wall-spectral-theory/cosmological-descent|cosmological descent]] for the map from wall correlation data to gauge-invariant cosmological observables and their later transfer. That is presently a representation-and-dynamics problem, not Grothendieck descent. The two meanings could meet only if the wall and spacetime descriptions were formulated as objects related by base change, equipped with comparison data on fiber products, and shown to be effective. Reusing the word does not supply those structures.

Finally, descent must remain distinct from [[basic-concepts/soldering/entry|soldering]]. Descent asks whether several presentations are one object; soldering asks how different kinds of structure—such as an internal bundle and the tangent geometry, or scale and state registers—are connected. A soldering map may itself have to descend, but its cross-type identification is extra data.

The durable questions for later scholia are: What information has base change duplicated or forgotten? Which comparisons are canonical and which are choices? What topology expresses physical locality? Is the datum effective, and in what category? What twists remain after local trivialization? Those questions turn “the local descriptions agree” from a metaphor into a theorem-shaped claim.
