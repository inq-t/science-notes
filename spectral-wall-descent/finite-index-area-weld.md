# The Finite-Index Area Weld

A matched type-I product-cell model has an exact algebraic budget: the log dimension of an erased edge factor splits into a chosen input edge state's entropy and its distinguishability from the tracial edge state. Exact complementary-recovery codes independently identify fixed relative-commutant edge entropy with a central area operator. Welding these two data, while keeping their expectations distinct, yields a finite-index candidate for gravitational descent rather than a general index--area theorem; the final passage to a commutative fact remains a separate, generally infinite-index step.

## Why the wall has two stages

The type obstruction in [[spectral-wall-descent/conditional-expectation-balance#The modular existence gate|the modular existence gate]] rules out a finite-index final wall from a type-III factor to a commutative record algebra. The gravitational step must therefore occur earlier:

$$
\boxed{
\mathcal A_-
\xrightarrow{\ E_g\ }
\mathcal A_{\mathrm{geo}}
\xrightarrow{\ F\ }
\mathcal B_{\mathrm{fact}},
\qquad
E_{\mathrm{tot}}:=F\circ E_g.}
$$

Here \(E_g\) is allowed to be a finite-index expectation between noncommutative algebras. The map \(F\) is the later observational or record-producing descent and need not have finite index.

In a finite tracial debugging model, let \(P_g\) and \(P_{\mathrm{tot}}\) be the trace-adjoint density projections induced by these nested expectations. Under faithfulness and support compatibility, the nested Pythagorean identity gives

$$
\boxed{
D(\rho\Vert P_{\mathrm{tot}}\rho)
=D(\rho\Vert P_g\rho)
+D(P_g\rho\Vert P_{\mathrm{tot}}\rho).}
$$

At a faithful reference fixed by both stages, the coincidence Hessian decomposes the pre-observable BKM norm into geometric-wall loss, factual-wall loss, and retained factual response. No unitary environment or conserved bit count is required.

## Exact one-sector calculation

Let

$$
\mathcal N
=B(\mathcal H_a)\otimes\mathbf1_b
\subset
\mathcal M
=B(\mathcal H_a\otimes\mathbb C^d),
$$

Write separately the normalized trace functional and its density,

$$
\operatorname{tr}_d(b):=\frac{\operatorname{Tr}(b)}d,
\qquad
\tau_d:=\frac{\mathbf1_d}{d}.
$$

The reference tracial expectation is

$$
E_\tau(a\otimes b)
:=a\operatorname{tr}_d(b)\otimes\mathbf1_d.
$$

For matrix units \(e_{ij}\) on \(\mathbb C^d\), a quasi-basis is

$$
u_{ij}=\sqrt d\,(\mathbf1_a\otimes e_{ij}).
$$

Hence the Watatani index is

$$
\boxed{
\operatorname{Ind}_{W}(E_\tau)
=\sum_{i,j}u_{ij}u_{ij}^*
=d^2\mathbf1.}
$$

Take a product state

$$
\rho=\rho_a\otimes\chi,
$$

where \(\chi\) is a faithful edge state. Using trace self-adjointness to identify functionals with density matrices, let \(P_\tau\) denote restriction to \(\mathcal N\) followed by the tracial extension back to \(\mathcal M\). On the displayed product density it sends

$$
P_\tau(\rho)=\rho_a\otimes\tau_d.
$$

Therefore

$$
S(P_\tau\rho)-S(\rho)
=\log d-S(\chi)
=D(\chi\Vert\tau_d).
$$

Equivalently,

$$
\boxed{
S(\chi)
+D(\chi\Vert\tau_d)
=\log d
=\frac12\log\operatorname{Ind}_{W}(E_\tau).}
$$

This is the finite **[EXACT TYPE-I PRODUCT-EDGE IDENTITY]**. It uses two data: the tracial coarse-grainer \(E_\tau\) and an arbitrary product input edge state \(\chi\). It is not an invariant of \(E_\tau\) alone and does not say that \(E_\tau\) selects an area eigenvalue \(S(\chi)\).

If an exact complementary-recovery code on the same relative-commutant factor instead selects \(\chi\) as a fixed edge state, its commutant expectation is

$$
E_\chi(a\otimes b)
=a\operatorname{Tr}(\chi b)\otimes\mathbf1_d.
$$

For faithful \(\chi\),

$$
\operatorname{Ind}_{W}(E_\chi)
=\operatorname{Tr}(\chi^{-1})\mathbf1,
$$

and \(E_\chi\) is trace preserving only when \(\chi=\tau_d\). Thus no single expectation presently supplies both the arbitrary-edge entropy formula and the tracial index formula.

Its three terms have different types:

- \(\tfrac12\log\operatorname{Ind}_{W}(E_\tau)=\log d\) is the log-dimension of the distinguished erased edge factor, equivalently the logarithm of its categorical dimension in this minimal factor model;
- \(S(\chi)\) is entropy carried by its distinguished edge state; and
- \(D(\chi\Vert\tau_d)\) is the distinction erased when that state is replaced by the tracial edge state.

The equation is a product-state balance internal to one algebraic cell. It is not conservation of energy, and it does not say that entropy and information are substances that change into each other.

The index conventions must not be collapsed. Here

$$
\operatorname{Ind}_{W}(E_\tau)=d^2,
\qquad
d_{\mathrm{cat}}=d,
\qquad
C_{\mathrm{edge}}=\log d,
$$

while the matrix-amplified subalgebra relative-entropy capacity is \(\log\operatorname{Ind}_{W}(E_\tau)=2\log d\). If \(n=\dim\mathcal H_a\), the ordinary unamplified supremum in this concrete model is \(\log\!\left(d\min\{n,d\}\right)\). The half-index term is therefore not the unrestricted information capacity of the inclusion.

## Central geometry in several sectors

For the sector-preserving type-I toy inclusion,

$$
\bigoplus_\alpha
\left(
B(\mathcal H_{a_\alpha})\otimes\mathbf1_{b_\alpha}
\right)
\subset
\bigoplus_\alpha
\left(
B(\mathcal H_{a_\alpha})\otimes B(\mathcal H_{b_\alpha})
\right),
$$

write the retained algebra and its center as

$$
\mathcal N_R
=\bigoplus_\alpha
\left(
B(\mathcal H_{a_\alpha})\otimes\mathbf1_{b_\alpha}
\right),
\qquad
Z(\mathcal N_R)
=\bigoplus_\alpha\mathbb CP_\alpha,
$$

the algebraic Ryu--Takayanagi theorem and the conditional-expectation formulation of exact complementary-recovery codes place the area term in the center, provided each \(\chi_\alpha\) is fixed for all logical states in its sector:

$$
\boxed{
\mathcal L_{\mathrm{code}}
=\sum_\alpha S(\chi_\alpha)P_\alpha
\in Z(\mathcal N_R).}
$$

The center records which sector is presented; the matrix factor inside a sector remains noncommutative. Points of

$$
\operatorname{Spec}Z(\mathcal N_R)
$$

are characters of that center and hence superselection labels, not primitive atoms in the upstream algebra. Calling such labels spatial “lumps” additionally requires a localized net, support map, and gluing construction. This is a controlled precursor to [[program-core/contextual-descent-from-homogeneity|contextual descent from homogeneity]].

In an edge-entropy-saturated type-I sector, \(\chi_\alpha=\tau_{d_\alpha}\), and the auxiliary tracial reference gives

$$
\mathcal L_{\chi}|_\alpha
=\frac12\log\operatorname{Ind}_{W}(E_{\tau,\alpha}).
$$

In general,

$$
\boxed{
\mathcal L_{\chi}|_\alpha
=\frac12\log\operatorname{Ind}_{W}(E_{\tau,\alpha})
-D(\chi_\alpha\Vert\tau_{d_\alpha}).}
$$

This last formula is a two-datum comparison: \(E_{\tau,\alpha}\) is an auxiliary trace expectation, not generally the code expectation \(E_{\chi_\alpha}\) that selects the area state. Translating a unit entropy cell into a numerical Jones index therefore requires both an algebraic state-selection theorem and an entropy-saturation theorem. In particular, no universal conclusion such as \(d=e\) follows from the unit Ruble law.

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

is additive under fusion. If the distinguished edge factors and states form a no-sector-mixing tensor product compatible with that fusion, their entropies and relative defects add separately, so the one-cell identity extends to a product cocycle balance.

This is the strongest present answer to “what remains symmetric during symmetry breaking”:

$$
\boxed{
\text{the correspondence composes coherently;
matched product-edge and tracial data obey an exact local identity}.}
$$

The assertion about categorical dimension is standard in the factor or simple-sector setting. With nontrivial centers, fusion uses matrix dimensions and sums over intermediate sectors, and entropy can acquire classical mixing terms; scalar minimal index is generally only submultiplicative. The theory must therefore retain the dimension matrix or full bimodule rather than collapse it prematurely to one number.

## Relation to gravity and to lost response

Holographic relative entropy gives an important no-go. In exact complementary-recovery code models the central area term cancels from relative entropy. For perturbations of the vacuum CFT ball with a leading semiclassical AdS Rindler-wedge dual, the retained regional quantum Fisher metric pulls back to bulk canonical energy. Therefore

$$
G^{\mathrm{ret}}
\longleftrightarrow
\mathcal E_{\mathrm{can}}
$$

is the calibrated AdS relation in that regime; it is not generally

$$
G^{\mathrm{lost}}
\longleftrightarrow
\mathcal E_{\mathrm{can}}.
$$

In exact algebraic code models, a candidate gravitational coefficient belongs instead to the independent central weld

$$
\mathcal L_{\mathrm{code}}
\stackrel{?}{=}
\eta_*\mathcal A_D,
$$

where \(\mathcal A_D\) is an independently normalized central spectral area assignment. [[deriving-value-of-g/spectral-index-area-route|The spectral index--area route]] states this theorem target and its anti-circularity test.

The result refines the phrase “gravity balances what observation loses.” In the type-I product cell, edge entropy and distinction from the tracial edge state are complementary summands. In an exact code, the fixed edge entropy can separately define a central area datum. Proving that one physical wall selects both structures is precisely the missing weld. Gravity is not simply renamed BKM loss.

## Scope

This construction is **[EXACT TYPE-I PRODUCT CELL]** for the displayed identity and **[CONJECTURAL WELD]** when extended to physical gravitational cuts.

- Correlated states do not obey the constant product-edge budget; algebraic conditional entropy can be negative and the full index capacity belongs to a different theorem.
- Exact holographic codes are controlled models, not a derivation of the causal wall.
- Finite index is dimensionless and locally rigid; a physical area density requires a scale-indexed tower and a separately normalized Dirac operator.
- The final character and persistent record are still supplied only by [[conservation-of-causal-charge/factive-descent-and-records|factive descent and records]].

Primary sources: [operator-algebra quantum error correction and the central area operator](https://arxiv.org/abs/1607.03901), [the holographic map as a conditional expectation](https://arxiv.org/abs/2008.04810), [relative entropy and subalgebra index](https://arxiv.org/abs/1909.01906), and [matrix dimension for finite-center correspondences](https://arxiv.org/abs/1805.09234).
