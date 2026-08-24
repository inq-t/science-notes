# Selecting the Class

The standing complaint is that Connes chose the KO-dimension of the finite geometry to be $6$ because it made the fermion doubling problem go away, and never derived it. The complaint is aimed at the wrong variable. Requiring that the fermionic action be a nonvanishing antisymmetric form on the chiral subspace forces $\varepsilon''=-1$ and $\varepsilon\varepsilon'=-1$, which among the four even classes holds only at $n=2$; with a four-dimensional spin manifold the class of $F$ then follows as $6=2-4$ in $\mathbb Z/8$. What was not derived is the metric dimension $4$, the demand for a Pfaffian, the algebra, and the three generations. The KO-dimension is the dependent variable in that list, not a free one.

## The two conditions

On a real spectral triple write $\mathcal H^\pm=\{\xi:\gamma\xi=\pm\xi\}$ and

$$
A_D(\xi',\xi)=\langle J\xi',D\xi\rangle,\qquad \xi,\xi'\in\mathcal H^+ .
$$

**Non-vanishing requires $\varepsilon''=-1$.** Since $D$ anticommutes with $\gamma$, $D$ maps $\mathcal H^+$ into $\mathcal H^-$. For $\xi\in\mathcal H^+$,

$$
\gamma(J\xi)=\varepsilon''J\gamma\xi=\varepsilon''\,J\xi ,
$$

so $J$ carries $\mathcal H^+$ into $\mathcal H^{\varepsilon''}$. If $\varepsilon''=+1$ then $J\xi'\in\mathcal H^+$ while $D\xi\in\mathcal H^-$, the two subspaces are orthogonal, and $A_D$ vanishes identically. Only $\varepsilon''=-1$ leaves a form at all.

**Antisymmetry requires $\varepsilon\varepsilon'=-1$.** Antilinearity and isometry give, by polarization, $\langle J\alpha,J\beta\rangle=\langle\beta,\alpha\rangle$, and $J^{-1}=\varepsilon J$. Then

$$
A_D(\xi',\xi)=\langle J\xi',J(J^{-1}D\xi)\rangle
=\langle J^{-1}D\xi,\xi'\rangle
=\varepsilon\,\langle JD\xi,\xi'\rangle
=\varepsilon\varepsilon'\,\langle DJ\xi,\xi'\rangle
=\varepsilon\varepsilon'\,A_D(\xi,\xi'),
$$

on a $J$-invariant domain and using self-adjointness of $D$ in the last step. So the form is antisymmetric exactly when $\varepsilon\varepsilon'=-1$ and symmetric exactly when $\varepsilon\varepsilon'=+1$.

## The two conditions pick one class

Chirality demands a grading, so $n$ is even, and for even $n$ the table gives $\varepsilon'=+1$ throughout. The condition reduces to $\varepsilon=-1$ together with $\varepsilon''=-1$:

| $n$ | $\varepsilon$ | $\varepsilon''$ | $A_D$ on $\mathcal H^+$ |
|---|---|---|---|
| 0 | $+$ | $+$ | vanishes |
| 2 | $-$ | $-$ | antisymmetric |
| 4 | $-$ | $+$ | vanishes |
| 6 | $+$ | $-$ | symmetric |

The pair $(-,-)$ occurs once. The KO-dimension of the total geometry is therefore **forced** to $2\in\mathbb Z/8$ by the demand for a Pfaffian, and $n=6$ is disqualified as the total class for the same reason it is required as the finite one — it gives a symmetric form.

Given a Riemannian spin $4$-manifold, whose KO-dimension is $4$, additivity leaves

$$
n_F=2-4=-2\equiv 6 \pmod 8 .
$$

[[library/why-the-standard-model/entry|Chamseddine and Connes]] state the same derivation backwards — "the raison d'être for $F$ is to correct the K-theoretic dimension from four to ten (modulo eight)" — which makes the dependency explicit: $2$ is the target, $4$ is given, $6$ is solved for.

## Why a Pfaffian

The condition is not free, but it is not arbitrary either. In the Euclidean spectral formalism the naive fermionic term over the full $\mathcal H$ counts each physical degree of freedom several times over; this is the fermion doubling problem. The Pfaffian is the square root of the determinant, and expressing the fermionic integral as

$$
\mathrm{Pf}(A)=\int e^{-\frac12 A(\xi)}\,D[\xi]
$$

over anticommuting classical fermions restricted to $\mathcal H^+$ restores the correct count. So the demand is a *counting* demand about physical matter, imported from experience, and the class $n=2$ is what an algebra must be to satisfy it.

## The ledger

| Input | Status |
|---|---|
| metric dimension $4$ | empirical, not derived |
| evenness of the triple, i.e. that matter is chiral | empirical, not derived |
| the fermionic action is a Pfaffian on $\mathcal H^+$ | a counting constraint imported from the observed fermion content |
| KO-dimension $2$ of $M\times F$ | **derived** from the three above |
| KO-dimension $6$ of $F$ | **derived**, given the above and additivity |
| the algebra $\mathcal A_{LR}$ and its representation | constrained afterwards, not before — see below |
| three generations | put in by hand, and said to be so in the source |

Two later results narrow the sixth line without closing it. [[library/why-the-standard-model/entry|Why the Standard Model]] classifies the irreducible finite geometries *of KO-dimension six*, finds the dimension per generation to be a square $k^2$, and singles out the standard model under an added hypothesis of quaternion linearity, giving $k=4$ and so $2k^2=32$ per generation — matching the count assembled by Schur in [[what-commutes-with-everything]]. [[library/quanta-of-geometry/entry|Quanta of Geometry]] obtains $M_2(\mathbb H)$ and $M_4(\mathbb C)$ from a higher-degree Heisenberg relation. Both take the class as given and work inside it.

## What this does and does not settle

It settles that the KO-dimension is not an adjustable parameter. Wall's classification makes the option set a finite set of ten, [[the-eightfold-in-the-sign-table|four of which are even]], and the Pfaffian condition is a discrete algebraic test that eliminates three of the four. That is selection within a classified set, which is the only shape a structural derivation can have.

It does not settle why the arena has metric dimension four, why its matter is chiral, or why the fermion count is what it is. Those are the genuine inputs, and moving the complaint onto them is the point of the exercise. By the standard already adopted for the finite algebra in [[symmetry-groups-select/finite-algebra-filters|the filters note]] — that a condition applied to an assumed candidate is a consistency check and not an explanation — the Pfaffian argument is a filter of unusual sharpness, sharp enough to leave exactly one survivor, and still a filter. Nothing here generates the geometry it selects.
