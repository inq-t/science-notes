# The Finite-Index Area Weld

A matched type-I factor model has an exact algebraic budget: the log dimension of the tracial inclusion splits into a chosen edge state's entropy and its distinguishability from the tracial edge state. Holographic error-correcting codes independently identify fixed relative-commutant edge entropy with a central area operator. Welding these structures, while keeping their expectations distinct, yields a precise finite-index candidate for gravitational descent; the final passage to a commutative fact remains a separate, generally infinite-index step.

## Why the wall has two stages

The type obstruction in [[spectral-wall-descent/conditional-expectation-balance#The modular existence gate|the modular existence gate]] rules out a finite-index final wall from a type-III factor to a commutative record algebra. The gravitational step must therefore occur earlier:

$$
\boxed{
\mathcal A_-
\xrightarrow{\ E_g\ }
\mathcal A_{\mathrm{geo}}
\xrightarrow{\ E_f\ }
\mathcal B_{\mathrm{fact}}.}
$$

Here \(E_g\) is allowed to be a finite-index expectation between noncommutative algebras. The map \(E_f\) is the later observational or record-producing descent and need not have finite index.

When both expectations exist in a finite tracial debugging model and \(E_fE_g=E_f\), the nested Pythagorean identity gives

$$
\boxed{
D(\rho\Vert E_f\rho)
=D(\rho\Vert E_g\rho)
+D(E_g\rho\Vert E_f\rho).}
$$

At coincidence, the pre-observable BKM norm decomposes into geometric-wall loss, factual-wall loss, and retained factual response. No unitary environment or conserved bit count is required.

## Exact one-sector calculation

Let

$$
\mathcal N
=B(\mathcal H_a)\otimes\mathbf1_b
\subset
\mathcal M
=B(\mathcal H_a\otimes\mathbb C^d),
$$

and let the reference tracial expectation be

$$
E_\tau=\operatorname{id}\otimes\tau_d,
\qquad
\tau_d:=\frac{\mathbf1_d}{d}.
$$

For matrix units \(e_{ij}\) on \(\mathbb C^d\), a quasi-basis is

$$
u_{ij}=\sqrt d\,(\mathbf1_a\otimes e_{ij}).
$$

Hence the Watatani index is

$$
\boxed{
\operatorname{Ind}(E_\tau)
=\sum_{i,j}u_{ij}u_{ij}^*
=d^2\mathbf1.}
$$

Take a product state

$$
\rho=\rho_a\otimes\chi,
$$

where \(\chi\) is a faithful edge state. The predual coarse graining sends

$$
E_{\tau *}(\rho)=\rho_a\otimes\tau_d.
$$

Therefore

$$
S(E_{\tau *}\rho)-S(\rho)
=\log d-S(\chi)
=D(\chi\Vert\tau_d).
$$

Equivalently,

$$
\boxed{
S(\chi)
+D(\chi\Vert\tau_d)
=\log d
=\frac12\log\operatorname{Ind}(E_\tau).}
$$

This is the finite **index--entropy--defect theorem** used by the construction. If an exact code on the same relative-commutant factor uses \(\chi\) as its fixed edge state, its central area contribution is \(\mathcal L_\chi=S(\chi)\). The expectation determined by that code state need not be the tracial expectation \(E_\tau\), and its Pimsner--Popa index need not equal \(d^2\). The equation compares the code's edge state with the tracial capacity reference on the same factor; it must not conflate the two expectations.

Its three terms have different types:

- \(\tfrac12\log\operatorname{Ind}(E_\tau)\) is the maximum dimensionless capacity of the tracial factor inclusion;
- \(S(\chi)\) is entropy carried by its distinguished edge state; and
- \(D(\chi\Vert\tau_d)\) is the distinction erased when that state is replaced by the tracial edge state.

The equation is a balance internal to one algebraic cell. It is not conservation of energy, and it does not say that entropy and information are substances that change into each other.

## Central geometry in several sectors

For a finite observable algebra with center,

$$
\mathcal M_R
=\bigoplus_\alpha
\left(
B(\mathcal H_{a_\alpha})\otimes\mathbf1
\right),
\qquad
Z(\mathcal M_R)
=\bigoplus_\alpha\mathbb CP_\alpha,
$$

the algebraic Ryu--Takayanagi theorem and the conditional-expectation formulation of exact holographic codes place the area term in the center:

$$
\boxed{
\mathcal L_{\mathrm{code}}
=\sum_\alpha S(\chi_\alpha)P_\alpha
\in Z(\mathcal M_R).}
$$

The center records which sector is presented; the matrix factor inside a sector remains noncommutative. Apparent points or lumps are therefore characters of

$$
\operatorname{Spec}Z(\mathcal M_R),
$$

not primitive atoms in the upstream algebra. This is a controlled model of [[program-core/contextual-descent-from-homogeneity|contextual descent from homogeneity]].

In an index-saturated type-I sector, \(\chi_\alpha=\tau_{d_\alpha}\), and

$$
\mathcal L_{\mathrm{code}}|_\alpha
=\frac12\log\operatorname{Ind}(E_{\tau,\alpha}).
$$

In general,

$$
\boxed{
\mathcal L_{\mathrm{code}}|_\alpha
=\frac12\log\operatorname{Ind}(E_{\tau,\alpha})
-D(\chi_\alpha\Vert\tau_{d_\alpha}).}
$$

Thus index is a ceiling, not automatically the physical area entropy. Translating a unit entropy cell into a numerical Jones index requires a saturation theorem. In particular, no universal conclusion such as \(d=e\) follows from the unit Ruble law.

## The candidate non-Noether symmetry

The data that compose under scale change are finite-index correspondences, not scalar entropy numbers. In a factor sector, a dualizable correspondence \(X\) has categorical dimension \(d(X)\), and Connes fusion obeys

$$
d(X_{32}\boxtimes X_{21})
=d(X_{32})d(X_{21}).
$$

Consequently

$$
\Lambda(X):=\log d(X)
$$

is additive under fusion. If the distinguished edge states also factor under that fusion, their entropies and relative defects add separately, so the one-cell identity extends to a cocycle balance.

This is the strongest present answer to “what remains symmetric during symmetry breaking”:

$$
\boxed{
\text{the correspondence composes coherently;
matched edge and tracial data obey an exact capacity partition}.}
$$

The assertion about categorical dimension is standard in the factor or simple-sector setting. With nontrivial centers, scalar minimal index is generally only submultiplicative. The functorial datum is a matrix dimension or the full bimodule, so the theory must retain sectorwise information rather than collapse it prematurely to one number.

## Relation to gravity and to lost response

Holographic relative entropy gives an important no-go. At fixed code subspace, the central area term cancels from relative entropy, while the retained regional quantum Fisher metric maps to bulk canonical energy. Therefore

$$
G^{\mathrm{ret}}
\longleftrightarrow
\mathcal E_{\mathrm{can}}
$$

is the calibrated AdS relation; it is not generally

$$
G^{\mathrm{lost}}
\longleftrightarrow
\mathcal E_{\mathrm{can}}.
$$

The gravitational coefficient belongs instead to the independent central weld

$$
\mathcal L_{\mathrm{code}}
\stackrel{?}{=}
\eta_*\mathcal A_D,
$$

where \(\mathcal A_D\) is an independently normalized spectral area operator. [[deriving-value-of-g/spectral-index-area-route|The spectral index--area route]] states this density theorem and its anti-circularity test.

The result refines the phrase “gravity balances what observation loses.” In the matched factor cell, geometric edge entropy and distinction from the tracial capacity state are complementary summands. If the physical wall is tracial, that defect is its exact BKM loss; for a nontracial code expectation this further identification must be proved. Gravity is not simply renamed BKM loss.

## Scope

This construction is **[EXACT FINITE ALGEBRA]** for the displayed type-I inclusion and **[CONJECTURAL WELD]** when extended to physical gravitational cuts.

- Correlated states need not have the product edge form; algebraic conditional entropy can be negative.
- Exact holographic codes are controlled models, not a derivation of the causal wall.
- Finite index is dimensionless and locally rigid; a physical area density requires a scale-indexed tower and a separately normalized Dirac operator.
- The final character and persistent record are still supplied only by [[conservation-of-causal-charge/factive-descent-and-records|factive descent and records]].

Primary sources: [operator-algebra quantum error correction and the central area operator](https://arxiv.org/abs/1607.03901), [the holographic map as a conditional expectation](https://arxiv.org/abs/2008.04810), [relative entropy and subalgebra index](https://arxiv.org/abs/1909.01906), and [matrix dimension for finite-center correspondences](https://arxiv.org/abs/1805.09234).
