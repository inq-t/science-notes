# Variational Versus Dynamical Symmetry

The gap between symmetries of the action and symmetries of the equations runs in both directions and is the reason the synthesis is neither automatic nor merely sufficient. Read forward, the gap means a famous symmetry can yield nothing. Read backward, there is a converse: for suitably regular variational systems every conservation law comes from a variational symmetry, so conservation has no brute instances. The converse holds only when *symmetry* is read broadly enough to include transformations that act on velocities, and that breadth is a real extension of the geometric notion.

## Forward: the upgrade can fail

The strict inclusion $\text{variational}\subseteq\text{dynamical}$ and its Kepler witness belong to [[philosophy/symmetry-principle/invariance-of-what|invariance of what]]. The consequence here is that a theory can be rich in symmetries of its equations and poor in conserved quantities, and that inspecting the solution set is the wrong way to look for conservation laws. Only the action knows.

## Backward: conservation is not brute

The more interesting direction is whether Noether's theorem is exhaustive. It is, under hypotheses. For a variational system that is *normal* — totally nondegenerate, in the sense that its equations and their differential consequences satisfy a maximal-rank condition — there is a one-to-one correspondence

$$
\boxed{
\Bigl\{\substack{\text{equivalence classes of}\\ \text{conservation laws}}\Bigr\}
\;\longleftrightarrow\;
\Bigl\{\substack{\text{equivalence classes of}\\ \text{variational symmetries}}\Bigr\},
}
$$

with trivial conservation laws and trivial symmetries quotiented out on each side. This is the converse of Noether's first theorem, and it is the statement that makes the synthesis tight rather than merely productive.

Its philosophical weight for this project is worth naming. In a normal variational theory there are no unexplained conservation laws: every conserved quantity has a symmetry as its reason, and the correspondence is exact rather than heuristic. That is a local instance of the demand in [[sufficient-reason/entry|Sufficing and Necessitating Reason]] that structure have grounds — one of the few places in physics where the demand is met by a theorem rather than by a programme.

The hypotheses are not decoration. Gauge systems are degenerate and fall outside normality, which is precisely why they need a separate treatment in [[second-theorem-and-gauge]].

## The breadth the converse needs

The correspondence fails if *symmetry* is restricted to point transformations of the fields and coordinates. The standard witness is again Kepler. The Laplace--Runge--Lenz vector

$$
\boldsymbol A=\dot{\boldsymbol r}\times\boldsymbol L-\frac{k\,\boldsymbol r}{|\boldsymbol r|}
$$

is conserved, and it is not the Noether charge of any point symmetry of the action. It corresponds instead to a generalized symmetry, whose generator depends on velocities as well as positions and so does not act on configuration space at all. Admitting generalized symmetries restores the correspondence; refusing them leaves conserved quantities without symmetries and makes Noether's theorem look merely sufficient.

This has a consequence for how the second axiom should be understood in the section. The relevant $G$ need not act geometrically on spacetime or on an internal bundle. Requiring it to do so is an additional assumption, frequently a reasonable one, and not part of the axiom.

## What the two directions establish jointly

| Direction | Statement | Status |
|---|---|---|
| forward | variational symmetry $\Rightarrow$ conserved current | exact, and the hypothesis is about the action |
| forward, negative | dynamical symmetry alone $\Rightarrow$ nothing | exact, witnessed by Kepler rescaling |
| backward | conserved current $\Rightarrow$ variational symmetry | exact for normal systems, generalized symmetries admitted |
| backward, negative | the correspondence fails for point symmetries alone | exact, witnessed by the Runge--Lenz vector |

Taken together these say that for regular variational theories, symmetry and conservation are two presentations of one thing — which is a considerably stronger claim than the textbook one-way slogan, and which fails exactly at the degenerate systems that gravity and gauge theory are.
