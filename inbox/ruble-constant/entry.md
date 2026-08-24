# The Ruble Quotient and Causal Individuation

This provisional packet asks what the proposed Ruble quantity measures and where the surrounding programme bottoms out. Its working answer is that the theory does not presently require a new constant of nature: it proposes a physical quotient of scale--state presentations equipped with a distinguishability metric, an inverse-area modulus obtained by localizing that metric on causal cuts, and a dimensionless Ruble quotient testing whether the state-side modulus equals the gravitational entropy--area modulus.

These notes are staging material. They reorganize ideas from [[causal-scale-theory/entry|Causal Scale Theory]], [[causal-wall-spectral-theory/entry|Causal-Wall Spectral Theory]], [[conservation-of-causal-charge/entry|Conservation of Causal Charge]], [[deriving-value-of-g/entry|Deriving the Value of $G$]], and [[cosmodynamics/entry|Cosmodynamics]] without changing the claim status of any source result.

## Working thesis

The proposed structure has three levels:

$$
\boxed{
\text{causal individuation geometry}
\longrightarrow
\text{capacity per causal area}
\longrightarrow
\text{geometric compliance and }G.}
$$

The first level is a still-unconstructed quotient of physically redundant presentations together with a positive quadratic form measuring distinguishable deformation. The second level is the localization of that form as a measure on a causal cut. The third level is the conjectural identification of its areal density with the entropy--area coefficient that governs Einstein focusing.

The proposed fundamental concept is therefore **causal individuation**: the structured capacity for a distinction to survive the quotient by indiscernibility, acquire causal and metric placement, and persist as a record. Its quantitative form is **causal capacity**. Its local intensive form is a **causal-capacity modulus**. Its possible linear symmetry invariant is **causal charge**. These are related roles, not synonyms.

[[terminology-and-type-discipline]] fixes this vocabulary and the distinctions among a parameter, invariant, universal coefficient, running coupling, capacity, Casimir, and charge.

## The candidate mathematical bottom

Let $\mathfrak P$ denote a presentation space containing scale sections, observer cuts, algebras, states, and comparison data. After declaring the admissible observables and presentation arrows, the programme seeks a physical quotient or groupoid schematically written

$$
\mathfrak P_{\mathrm{phys}}
=
\frac{\mathfrak P}
{\text{indiscernible, vertical, central, and gauge directions}}.
$$

A scale-to-state map

$$
\Phi:\mathfrak P_{\mathrm{phys}}\longrightarrow\mathfrak S
$$

would pull the BKM geometry of admissible states back to a causal-scale geometry,

$$
\boxed{
\mathcal G_{\mathrm{CI}}
:=\Phi^*G_{\mathrm{BKM}}.}
$$

This **causal-individuation metric** is a construction target, not an existing global object. [[causal-individuation-geometry]] states its proposed domain, components, and failure conditions.

At a homogeneous reference, its anticipated decomposition is

$$
\mathcal G_{\mathrm{CI}}
\sim
\begin{pmatrix}
G^\perp_{NN} & G_{N\zeta}\\
G_{\zeta N} & \mathcal K_\zeta
\end{pmatrix}
$$

on a tangent space of the schematic form

$$
\mathbb R\oplus C^\infty(\Sigma)/\mathbb R.
$$

Causal Scale Theory studies the homogeneous $N$ block. Causal-Wall Spectral Theory proposes a representation of the inhomogeneous $\zeta$ block. The mixed blocks and the common carrier have not been constructed.

## The dimensional content

Relative entropy, logarithmic scale $N$, and the integrated BKM quadratic form are dimensionless. If the horizontal norm localizes additively on a codimension-two causal cut, its Radon--Nikodym density with respect to area has units $L^{-2}$:

$$
\chi_{\downarrow}
:=
\frac{\mathrm d\mu^\perp_{\mathrm{BKM}}}
{\mathrm d\mu_A},
\qquad
[\chi_{\downarrow}]=L^{-2}.
$$

Its inverse

$$
\mathfrak a_{\downarrow}:=\chi_{\downarrow}^{-1}
$$

has units $L^2$ and can be read as causal area per unit natural-log distinguishability curvature. [[units-and-planck-rebasing]] explains why this is the programme's plausible Planck-like dimensional primitive and why dimensionless binary geometry cannot calculate its magnitude.

## The Ruble quotient

Einstein gravity supplies a separately defined entropy--area modulus

$$
\eta_{\mathrm E}
:=
\frac{\mathrm d(S_{\mathrm{hor}}/k_B)}{\mathrm dA}
=\frac{c^3}{4\hbar G}
=\frac{1}{4\ell_P^2}.
$$

Whenever the state-side and gravitational coefficients are independently defined on the same cut, define

$$
\boxed{
\mathfrak R_\Sigma
:=
\frac{\chi_{\downarrow}}{\eta_{\mathrm E}}.}
$$

Under a linear area law and the required extensivity, the value at the self-dual cut is

$$
\mathfrak R_c
=\frac{k_B}{S_c}G^\perp_{NN}(N_c).
$$

Thus $\mathfrak R$ is best typed as a **state--geometry equivalence quotient**. The unit law

$$
\mathfrak R_\Sigma=1
$$

asserts that two independently constructed moduli coincide. The physical content is the equivalence, not the numeral one. [[ruble-quotient-and-flow]] distinguishes this matching law from constancy along a path, a fixed point, a universal functional, and renormalization-group running.

## Symmetry does not collapse the types

The exact binary identity

$$
1=\eta^2+G^{\mathrm{BKM}}_{\theta\theta}
$$

is a quadratic Casimir allocation. The proposed causal charge is instead a linear moment-map or boundary charge. A least-action principle would require an action whose variations produce the physical dynamics. [[symmetry-charge-and-action]] records why none of these statements currently implies the others.

## Present claim boundary

| Status | Content |
|---|---|
| Exact after stated reduction | binary mean--variance Casimir; regular relative-entropy Hessian; flat critical $|k|^3$ scaling; Einstein area-law rearrangements |
| Defined after a valid wall state is supplied | horizontal BKM norm and its localized measure |
| Conditional theorem | unit escort tangent in a genuine $1+1$ conformal thermal sector gives capacity equal to entropy |
| Central physical conjecture | the wall BKM areal modulus equals the Einstein entropy--area modulus |
| Prospective conservation law | one diagonal causal charge across state, geometry, flux, and records |
| Not established | the common quotient, scale-indexed wall state, universal areal density, state--geometry weld, common action, or numerical derivation of $G$ |

[[theorem-and-failure-ledger]] gives the promotion tests that would turn this vocabulary into physics and the outcomes that would falsify or modify it.
