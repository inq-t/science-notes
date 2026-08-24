# Local--Global Individuation

Local equivalence explains why several presentations can count as one object, while global individuation asks whether that object admits a coherent labeling, section, or point. Descent can succeed even when global trivialization fails, and monodromy can record that failure without selecting an actuality or orienting time. A fact-bearing cosmos therefore needs an ambient process category whose reversible core handles presentation and whose genuinely noninvertible arrows extend persistent records.

## Descent is not individuation

Let $p:U\to S$ be a cover and let $x$ be an object over $U$. A descent datum is an isomorphism

$$
\theta:p_1^*x\xrightarrow{\sim}p_2^*x
$$

over $U\times_SU$ satisfying the cocycle condition over the triple fiber product. If the datum is effective, it reconstructs an object over $S$. It does not choose a point of that object, a trivialization, a branch, or an outcome.

For a local system with fiber $F$, monodromy is a representation

$$
\rho:\pi_1(S,s)\longrightarrow\operatorname{Aut}(F).
$$

Nontrivial $\rho$ can obstruct a global labeling of $F$ while the local system itself is a perfectly good global object. Thus:

$$
\boxed{
\text{effective descent}
\not\Longrightarrow
\text{global triviality or canonical pointing}.}
$$

Conversely, trivial monodromy is not required for descent. [[basic-concepts/descent/entry|The descent module]] owns the exact cocycle and effectivity conditions; [[basic-concepts/stacks/entry|stacks]] own the symmetry-sensitive global object.

## A fact is additional structure

Depending on the carrier, factual pointing may be modeled as:

- a section of a bundle or sheaf;
- a lift through a covering map;
- a character of a declared commutative unital $C^*$-algebra \(A\), namely a unital *-homomorphism \(\chi:A\to\mathbb C\);
- an outcome component of an instrument;
- a selected object in a fiber together with its compatibility data.

These models are not equivalent without maps between them. In particular, a probability measure on the character space is not a character, and a descended global object is not a selected section. The term **actualization** should be used only after its source, target, and selection rule have been typed.

## The reversible core and the process category

Let $\mathcal C$ be a category of admissible presentations and processes. Its maximal subgroupoid

$$
\mathcal C^{\simeq}\subseteq\mathcal C
$$

contains every object and only the invertible arrows. Changes of coordinates, gauge, local trivialization, and equivalent representation belong here when they are genuinely reversible. A groupoid-valued stack can organize their descent.

Causal precedence, a proper inclusion of record algebras, a non-automorphic endomorphism, an instrument, or a conditional expectation generally lies in $\mathcal C\setminus\mathcal C^{\simeq}$. This two-tier structure is the minimum correction to treating “category, groupoid, or stack” as interchangeable presentation options. One may package it as a category with a chosen class of presentation equivalences, a category-valued stack, or a double category whose vertical arrows are equivalences and horizontal arrows are processes. The choice must be made before theorems are imported.

## A theorem-shaped criterion for orientation

Let \(W\subseteq\mathcal C^{\simeq}\) be the declared wide subgroupoid of presentation equivalences and let \(P\subseteq\mathcal C\) be a wide subcategory of physically admissible processes containing \(W\). Equivalently, one could require a chosen process class to contain identities and be closed under composition and under pre- and post-composition by \(W\). After identifying objects along \(W\), define reachability by

$$
[x]\preceq[y]
\quad\Longleftrightarrow\quad
\text{there exists }p:x'\to y'\text{ in }P
\text{ with }x'\simeq_Wx, y'\simeq_Wy.
$$

This is a preorder because \(P\) contains identities, composites, and the presentation equivalences needed to join representatives. It becomes a partial order after quotienting its cycles if every two-way reachable pair is physically equivalent. A proposed objective orientation must therefore prove at least:

1. reachability is independent of presentation;
2. nontrivial cycles disappear only by declared physical equivalence;
3. observers induce compatible orders; and
4. some admissible arrows are not invertible on the physical register.

To make the order factual, add a record functor

$$
\mathcal R:P\longrightarrow\mathsf{Rec},
$$

where $\mathsf{Rec}$ has persistent record objects and monomorphisms. Require \(\mathcal R\) to send \(W\) to record isomorphisms. For a fact-producing arrow $p:x\to y$, require

$$
\mathcal R(p):\mathcal R(x)\hookrightarrow\mathcal R(y)
$$

to be a proper extension and to preserve earlier factual values. This does not yet construct such a functor. It states what the phrase “time is the orientation of facts” must return mathematically. [[sufficient-reason/algebraic-arrow-of-time|The algebraic arrow of time]] supplies rigorous operator-algebraic candidates such as one-sided endomorphism semigroups and half-sided modular inclusions, while [[conservation-of-causal-charge/unitarity-and-ontological-time|ontological time]] owns the record-inclusion interpretation.

## Modular flow and monodromy do not supply the arrow

Both ordinary monodromy and Tomita--Takesaki modular evolution are invertible:

$$
\rho(\gamma)^{-1}=\rho(\gamma^{-1}),
\qquad
\sigma_t^\omega{}^{-1}=\sigma_{-t}^\omega.
$$

Modular flow additionally depends on a faithful state or weight, can be trivial for a trace, and is a two-sided \(\mathbb R\)-action. Although \(\Delta_\omega^{it}\) implements it in the standard Hilbert-space representation, \(\sigma_t^\omega\) need not be inner in \(\mathcal M\); under the appropriate hypotheses, change of faithful weight alters the flow by a Connes cocycle and leaves the corresponding outer class invariant. Interpreting that flow as physical time requires a thermal-time or related bridge. Finite-order $A_2$ monodromy is not KMS flow, RG flow, or cosmic time. [[causal-wall-spectral-theory/sources/legacy/calc-chats/a2-wall-rejection|The earlier $A_2$ wall rejection]] records this no-go.

A conditional expectation

$$
E:\mathcal M\to\mathcal N,
\qquad E^2=E,
$$

is noninvertible when \(\mathcal N\subsetneq\mathcal M\) and the chosen expectation genuinely erases distinctions; the identity expectation is the trivial exception. In the nontrivial case it can quantify lost distinguishability relative to the chosen subalgebra. It still does not choose an outcome or create a persistent record. An instrument and a record-extension law are additional data.

## Here, now, and metric realization

The phrase “facts happen here and now” contains two different pointings. **Here** selects a contextual or spatial locus relative to a realized carrier. **Now** selects a stage in the preorder of compatible record extension. Neither is supplied by a bare global object, and they need not be coordinates of the same type before a Lorentzian realization is constructed.

Writing \(x^0=ct\) converts a temporal coordinate to units of length. The constant \(c\) is not a quotient that identifies space with time: Lorentzian signature, causal cones, and the distinction between spacelike and timelike directions remain. A soldering map between record order and Lorentzian time is an additional physical weld.

Likewise, mass-energy and gravity are related but not generally identical or dual. In an imported Einstein branch, stress-energy sources geometry through field equations; the metric also has source-free degrees of freedom. Calling gravity the “cost of descent” requires a covariant map from a typed loss or response functional to gravitational canonical energy, curvature, and independently normalized area. It does not follow from forgetting, and it does not by itself explain cosmic expansion or acceleration.

## There is no untyped residue of forgetting

The word *residue* is meaningful only after a construction specifies its type. Possible return values include:

| Construction | Legitimate remainder |
|---|---|
| failed lifting or gluing problem | obstruction or cohomology class |
| covering with nontrivial transport | monodromy representation |
| quotient or complex | kernel, cokernel, fiber, cofiber, or derived functor |
| conditional expectation | relative-entropy or response defect |
| coarse moduli map | forgotten stabilizer data |
| factual process | proper increment of a record object |

A generic forgetful functor has no canonical curvature, entropy, time, or gravity attached to it. If forgetting is expressed by an adjunction $F\dashv U$, the unit, counit, monad or comonad, and the proposed invariant of their failure must be stated. Only then can a “tax” be calculated.

## Sufficient reason is not past-state recoverability

If the whole fact-bearing structure uniquely determines a history, later facts may be necessitated without being encoded as recoverable variables in an earlier observable algebra. The distinction is

$$
\text{global grounding}
\ne
\text{invertible evolution from an earlier accessible state}.
$$

This leaves room for genuine becoming without ontic chance: the sufficing reason can be global or inaccessible, while the record order is one-sided. It also supplies a sharp failure test. If every later record is already isomorphic to an earlier record under the physical equivalence, no factual extension—and hence no ontological orientation—has been constructed.
