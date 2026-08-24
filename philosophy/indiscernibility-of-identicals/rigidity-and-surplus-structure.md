# Rigidity and Surplus Structure

Rigidity — the triviality of the automorphism group — is what the orbit inclusion identifies as the obstruction to the identity of indiscernibles at the grade of properties. Against the full family of invariants it *is* the principle; against the family a language can define it is necessary and not sufficient. Where a group acts freely and properly the quotient loses nothing an invariant could have registered; where the action is not proper the quotient can fail to be a space at all, and where stabilizers are present it can fail to be smooth. The honest repair in either case is to keep the arrows. Surplus structure in a physical formalism is the same phenomenon seen from the other side, and it is a defect only when the extra distinctions are also idle for locality and well-posedness.

## Rigidity is necessary, not sufficient

For a structure $X$ whose automorphisms are determined by their action on points,

$$
\operatorname{Aut}(X)=1
\iff
\text{every }\operatorname{Aut}(X)\text{-orbit is a singleton}.
$$

By the boxed statement of [[grades-of-discernment]], the orbits are exactly the indiscernibility classes of the full invariant family, so against that family rigidity and the principle coincide. Against the definable family only one direction survives: a nontrivial automorphism is a witness against the principle, so rigidity is required, but it does not secure it — the ordinal example in that note is rigid and still contains elements no formula separates.

| Discernment | Structural name | What must be retained |
|---|---|---|
| definable properties separate points | rigid, and enough types | the set of points |
| action free and proper, some orbit nontrivial | no isotropy | the space together with its difference structure; no preferred origin |
| some point has nontrivial stabilizer | non-rigid, isotropy present | the arrows: a groupoid or stack, not a set |

## What the quotient costs, geometrically

Let a Lie group $G$ act smoothly on a configuration space $C$, with the observables the invariant functions. If the action is free and proper, $C/G$ is a manifold and no information is lost that the invariants could have registered. Properness is not a formality: the irrational flow on the torus is free, every orbit is dense, and the quotient carries the indiscrete topology on an uncountable set.

If the action is not free, the quotient is stratified by orbit type and may fail to be smooth; where it is singular, the singularities lie on strata at which the stabilizer jumps. The converse fails, and usefully so — $\mathbb Z/2$ acting on $\mathbb C$ by $z\mapsto-z$ has a jump at the origin and the smooth quotient $\operatorname{Spec}\mathbb C[z^2]$ — so singularity is a sufficient sign of retained isotropy and not a necessary one. The same failure appears globally as the non-existence of a gauge slice: a principal bundle with no global section admits no consistent choice of representative, and a formalism that assumes one has assumed away a cocycle.

The clean intermediate case is a $G$-torsor over a point: a nonempty set with a free and transitive action. Every invariant function on it is constant, so no point is discernible from any other, while the difference map $\delta:P\times P\to G$ of [[basic-concepts/torsors/entry|torsors]] is canonical, so every difference is. A torsor is therefore the sharpest available statement of this project's governing intuition, that the discernible content is entirely relational. Over a base the statement must be relativized — invariant functions are the functions on the base and the difference map lives on $P\times_SP$ — and the cautions in that note on specifying the group, freeness, transitivity, and local topology apply before the analogy may be used at all.

When stabilizers are present the torsor picture is not enough and the arrows must be retained explicitly: [[basic-concepts/groupoids/entry|groupoids]] for the arrows themselves, [[basic-concepts/descent/entry|descent]] for their coherence over a cover, and [[basic-concepts/stacks/entry|stacks]] for the resulting local-to-global object that remembers symmetry. Moduli theory shows the stakes. Rigidity is necessary for a fine moduli space, since a nontrivial automorphism permits a family that is locally trivial and globally not; it is not sufficient, because representability additionally demands descent, boundedness, and Artin's conditions, and can still land on an algebraic space rather than a scheme. When rigidity fails one may either rigidify by imposing extra structure — level structures on elliptic curves are the standard case — or pass to a stack. This apparatus is best understood as the disciplined way of living with the failure of the present principle.

## Surplus structure

Call a formalism **surplus** with respect to a declared observable family when its configuration space carries distinctions the family cannot register. Which of the three readings in [[the-razor]] applies — diagnostic, constitutive, or illegitimate — is a decision about the formalism and not a finding about nature.

Surplus is not automatically a defect. Redundant descriptions are often what makes a theory local, linear, or variationally well-posed, and eliminating them can cost more structure than it saves. The correct question is never whether a formalism has more distinctions than its observables, but whether those extra distinctions are doing work that the quotient cannot do.

The governing distinction is that a symmetry which leaves no trace in the invariants may still leave one in the arrows, and only the second kind of trace tells you what the quotient was entitled to forget.
