# Semiorthogonality, Admissibility, and Projection Triangles

A semiorthogonal decomposition is a directed generation statement in an enhanced stable setting. Admissibility supplies adjoints and therefore functorial projection triangles; without admissibility, a vanishing condition and generation do not automatically provide a canonical projector.

## The enhanced setting

Let \(\mathcal T\) be one of the following:

- an idempotent-complete \(k\)-linear stable \(\infty\)-category;
- a pretriangulated dg category, interpreted through its homotopy category \(H^0(\mathcal T)\); or
- an enhanced triangulated category in which the derived mapping objects and required adjoints exist.

For full stable subcategories \(\mathcal A,\mathcal B\subseteq\mathcal T\), write

$$
\operatorname{RHom}_{\mathcal T}(B,A)\simeq0
$$

to mean that the dg mapping complex is acyclic. Equivalently, in the stable \(\infty\)-categorical formulation the mapping spectrum \(\operatorname{Map}_{\mathcal T}(B,A)\) is contractible. On the homotopy category this implies

$$
\operatorname{Hom}_{H^0(\mathcal T)}(B,A[n])=0
\qquad
\text{for every }n\in\mathbb Z.
$$

Vanishing only \(\operatorname{Hom}(B,A)\) in degree zero is not enough.

## Definition and convention

This module uses the convention

$$
\boxed{
\mathcal T=\langle\mathcal A_1,\ldots,\mathcal A_n\rangle
\quad\Longrightarrow\quad
\operatorname{RHom}(\mathcal A_j,\mathcal A_i)\simeq0
\text{ for }j>i.}
$$

In addition, the smallest thick stable subcategory containing every \(\mathcal A_i\) must be all of \(\mathcal T\). Here *thick* means stable and closed under retracts. Some authors reverse the ordering convention, so every imported formula must be checked against its author's direction of vanishing.

For two components, semiorthogonality is one-sided:

$$
\operatorname{RHom}(\mathcal B,\mathcal A)\simeq0,
\qquad
\operatorname{RHom}(\mathcal A,\mathcal B)
\text{ may be nonzero}.
$$

If both directions vanish, the result is an orthogonal decomposition and, under the usual completeness hypotheses, behaves like a categorical direct sum. The possible reverse extension data are precisely what makes the semiorthogonal case richer.

## Admissibility

For a full inclusion

$$
i_{\mathcal A}:\mathcal A\hookrightarrow\mathcal T,
$$

the subcategory \(\mathcal A\) is:

- **left admissible** if \(i_{\mathcal A}\) has a left adjoint \(i_{\mathcal A}^*\);
- **right admissible** if it has a right adjoint \(i_{\mathcal A}^!\); and
- **admissible** if it has both.

Admissibility is extra structure. In smooth proper or saturated geometric settings it is often available for exceptional components, but it must not be assumed in an arbitrary triangulated or stable category.

Define the left and right orthogonals by

$$
{}^\perp\mathcal A
:=\{X:\operatorname{RHom}(X,A)\simeq0\ \forall A\in\mathcal A\},
$$

$$
\mathcal A^\perp
:=\{X:\operatorname{RHom}(A,X)\simeq0\ \forall A\in\mathcal A\}.
$$

A left-admissible \(\mathcal A\) gives

$$
\mathcal T=\langle\mathcal A,{}^\perp\mathcal A\rangle,
$$

while a right-admissible \(\mathcal A\) gives

$$
\mathcal T=\langle\mathcal A^\perp,\mathcal A\rangle.
$$

## The projection triangle

Suppose

$$
\mathcal T=\langle\mathcal A,\mathcal B\rangle
$$

with the adjoints needed for the decomposition. Every \(X\in\mathcal T\) then sits functorially in a distinguished triangle

$$
\boxed{
B_X\longrightarrow X\longrightarrow A_X\longrightarrow B_X[1],
\qquad
A_X\in\mathcal A,
\quad
B_X\in\mathcal B.}
$$

The arrow \(X\to A_X\) is universal among arrows from \(X\) to \(\mathcal A\), whereas \(B_X\to X\) is universal among arrows from \(\mathcal B\) to \(X\). In adjoint notation,

$$
A_X=i_{\mathcal A}i_{\mathcal A}^*X,
\qquad
B_X=i_{\mathcal B}i_{\mathcal B}^!X.
$$

Write

$$
\pi_{\mathcal A}:=i_{\mathcal A}^*:\mathcal T\longrightarrow\mathcal A,
\qquad
\pi_{\mathcal B}:=i_{\mathcal B}^!:\mathcal T\longrightarrow\mathcal B
$$

for the component-valued projection functors. The associated endofunctors

$$
P_{\mathcal A}:=i_{\mathcal A}\pi_{\mathcal A},
\qquad
P_{\mathcal B}:=i_{\mathcal B}\pi_{\mathcal B}
$$

are exact and idempotent up to canonical equivalence. They obey

$$
P_{\mathcal A}|_{\mathcal A}\simeq\operatorname{id}_{\mathcal A},
\qquad
P_{\mathcal A}|_{\mathcal B}\simeq0,
$$

and analogously for \(P_{\mathcal B}\). Thus \(P_{\mathcal A}\) is noninvertible when \(\mathcal B\ne0\).

This triangle is not generally a direct-sum decomposition \(X\simeq A_X\oplus B_X\). Its connecting morphism records how the components are glued.

## Verdier and dg quotients

For an admissible component \(\mathcal B\), the projection to the complementary component factors through the Verdier quotient and yields an equivalence

$$
\mathcal T/\mathcal B\simeq\mathcal A.
$$

At the dg level one uses a dg quotient, retaining the higher mapping information that can be lost by working only with a bare triangulated category. The quotient is an exact categorical localization: the objects of \(\mathcal B\) become zero.

This is not the same operation as a conditional expectation of operator algebras. A quotient kills a thick subcategory. A conditional expectation is typically not a \(*\)-homomorphism and its linear kernel is generally not a two-sided ideal.

## Filtrations for more than two components

For

$$
\mathcal T=\langle\mathcal A_1,\ldots,\mathcal A_n\rangle,
$$

each object admits a functorial filtration by exact triangles whose successive factors lie in the ordered components. This is the categorical analogue of an upper-triangular rather than diagonal decomposition. The order matters because morphisms from later to earlier factors vanish while morphisms in the reverse direction may encode their extensions.

## Additive invariants

For enhanced semiorthogonal decompositions satisfying the hypotheses of an additive invariant \(E\), one obtains a split formula

$$
E(\mathcal T)
\simeq
\bigoplus_i E(\mathcal A_i).
$$

Examples include algebraic \(K\)-theory spectra and Hochschild homology in the appropriate dg setting. The statement is invariant-specific: a metric, entropy, state, or spectral action does not split merely because Hochschild homology does.

In particular, JLO entire cyclic cohomology belongs to a specified theta-summable analytic cycle. It is not automatically attached to an abstract dg category. That realization boundary is developed in [[semiorthogonal-decompositions/categorical-wall-interface|the categorical wall interface]].
