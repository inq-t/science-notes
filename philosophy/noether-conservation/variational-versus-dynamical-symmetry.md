# Variational Versus Dynamical Symmetry

The gap between symmetries of the action and symmetries of the equations runs in both directions. Read forward, a famous symmetry can yield nothing. Read backward, there is a converse: for variational systems satisfying two regularity hypotheses, every conservation law comes from a variational symmetry, so conservation has no brute instances. The converse holds only when *symmetry* is read broadly enough to include transformations acting on velocities, and that breadth is a real extension of the geometric notion.

## Forward: the upgrade can fail

The strict inclusion $\text{variational}\subseteq\text{dynamical}$ and its Kepler witness belong to [[philosophy/symmetry-principle/invariance-of-what|invariance of what]]. The consequence here is that a theory can be rich in symmetries of its equations and poor in conserved quantities, and that inspecting the solution set is the wrong way to look for conservation laws. Only the action knows.

## Backward: conservation is not brute

For a variational system that is **normal** — possessing a noncharacteristic direction, so that the system can be put in Cauchy--Kovalevskaya form — and **totally nondegenerate** — satisfying a maximal-rank condition together with local solvability, for the system and all its prolongations — there is a one-to-one correspondence

$$
\boxed{
\Bigl\{\substack{\text{equivalence classes of}\\ \text{conservation laws}}\Bigr\}
\;\longleftrightarrow\;
\Bigl\{\substack{\text{equivalence classes of}\\ \text{variational symmetries}}\Bigr\},
}
$$

with trivial conservation laws and trivial symmetries quotiented out on each side. The two hypotheses are distinct and are both required: normality concerns the existence of a well-posed evolution direction, total nondegeneracy an algebraic rank condition plus local solvability. This is the converse of Noether's first theorem, and it makes the synthesis tight rather than merely productive.

In a normal, totally nondegenerate variational theory there are then no unexplained conservation laws: every conserved quantity has a symmetry as its reason, exactly rather than heuristically. That is a local instance of the demand in [[sufficient-reason/entry|Sufficing and Necessitating Reason]] that structure have grounds, met by a theorem.

Gauge systems are under-determined and therefore fail normality, which is why they need the separate treatment in [[second-theorem-and-gauge]].

## The breadth the converse needs

The correspondence fails if *symmetry* is restricted to point transformations of the fields and coordinates. The witness is again Kepler. With $\boldsymbol L=m\,\boldsymbol r\times\dot{\boldsymbol r}$, the Laplace--Runge--Lenz vector

$$
\boldsymbol A=\dot{\boldsymbol r}\times\boldsymbol L-\frac{\alpha\,\boldsymbol r}{|\boldsymbol r|}
$$

is conserved, and it is the Noether charge of no point symmetry of the action. It corresponds instead to a generalized symmetry, whose generator depends on velocities as well as positions and so does not act on configuration space at all. Admitting generalized symmetries restores the correspondence; refusing them leaves conserved quantities without symmetries and makes Noether's theorem look merely sufficient.

The second axiom should therefore not be silently restricted to groups acting geometrically on spacetime or on an internal bundle. Requiring that is an additional assumption, frequently reasonable, and not part of the axiom.

## What the two directions establish jointly

| Direction | Statement | Status |
|---|---|---|
| forward | variational symmetry $\Rightarrow$ conserved current | exact, and the hypothesis is about the action |
| forward, negative | dynamical symmetry alone $\Rightarrow$ nothing | exact, witnessed by Kepler rescaling |
| backward | conserved current $\Rightarrow$ variational symmetry | exact for normal, totally nondegenerate systems, generalized symmetries admitted |
| backward, negative | the correspondence fails for point symmetries alone | exact, witnessed by the Runge--Lenz vector |

For normal, totally nondegenerate variational theories, symmetry and conservation are two presentations of one thing. The correspondence lapses at exactly the degenerate systems that gravity and gauge theory are.
