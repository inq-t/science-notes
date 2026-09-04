# From Collared Surface Response to the Clay Gap

A uniform middle-to-boundary maximal-correlation bound on the complete regulated Yang--Mills vacuum complement is sufficient to produce a fixed-physical-slab Hamiltonian gap. If that bound and the pointed transfer forms survive the continuum and infinite-volume limits with Osterwalder--Schrader reconstruction, the limiting spectral exclusion is exactly the gap clause of the Clay problem. This note isolates that implication so the search for a pre-QFT carrier has one unambiguous analytic return type.

**Status: [EXACT -- FINITE REGULATOR] for the bridge-to-transfer implication; [CONDITIONAL CONTINUUM THEOREM] for passage to the Clay carrier; [OPEN] for the regulator-uniform Wilson surface-response bound, continuum existence, and nontrivial Yang--Mills identification.**

## Finite-regulator theorem

Let \(\mathcal H_r\) be a finite-regulator, gauge-invariant time-slice carrier with normalized vacuum \(\Omega_r\), vacuum projection \(P_{0,r}\), and positive self-adjoint vacuum-normalized transfer step

$$
P_r
=
\exp\!\left[-\frac{a_{\tau,r}}{\hbar c}(H_r-E_{0,r})\right],
\qquad
0<P_r\leq I.
\tag{C1}
$$

Let \(Q_r:=I-P_{0,r}\), and assume \(Q_r\) reduces \(P_r\). Choose an integer half-depth \(n_r\geq1\). Let

$$
K_{n_r}:Q_r\mathcal H_r
\longrightarrow
L^2_0(\text{two boundary slices})
\tag{C2}
$$

be centered conditional transport from the midpoint to the two boundaries under the stationary Euclidean path law. Define

$$
S_{n_r}:=K_{n_r}^*K_{n_r},
\qquad
B_{n_r}^{\mathrm{br}}:=I-S_{n_r}.
\tag{C3}
$$

Suppose the path law is reversible, so that the exact data-augmentation order holds,

$$
P_r^{2n_r}Q_r\leq S_{n_r}Q_r,
\tag{C4}
$$

and suppose its complete middle--boundary maximal correlation obeys

$$
c_{F,r}:=\|K_{n_r}Q_r\|\leq\rho_*<1
\tag{C5}
$$

with \(\rho_*\) independent of every component of the regulator \(r\). Then

$$
S_{n_r}Q_r\leq\rho_*^2Q_r,
\qquad
B_{n_r}^{\mathrm{br}}Q_r
\geq(1-\rho_*^2)Q_r.
\tag{C6}
$$

Combining (C4) and (C6) gives

$$
P_r^{2n_r}Q_r\leq\rho_*^2Q_r.
\tag{C7}
$$

Positivity and self-adjointness of \(P_r\) therefore imply

$$
\|P_r^{n_r}Q_r\|\leq\rho_*.
\tag{C8}
$$

Spectral calculus converts this dimensionless slab attenuation into the form bound

$$
\boxed{
H_r-E_{0,r}
\geq
\frac{\hbar c}{n_ra_{\tau,r}}
\log(\rho_*^{-1})\,Q_r.}
\tag{C9}
$$

Thus the object that must be bounded is neither a local action Hessian nor the rank of a descent map. It is the norm of conditional prediction from a complete physical midpoint distinction to both Euclidean boundaries.

## Fixed physical thickness

For a continuum limit, require

$$
n_ra_{\tau,r}\longrightarrow\ell_*>0.
\tag{C10}
$$

An adjacent-slice bound with fixed \(n_r\) is wrongly scaled: every finite physical excitation makes its one-step contraction approach one as \(a_{\tau,r}\to0\). At fixed physical thickness, (C9) instead gives the regulator-independent candidate

$$
\Delta_*
=
\frac{\hbar c}{\ell_*}\log(\rho_*^{-1})>0.
\tag{C11}
$$

The Gaussian calibration sharpens the dictionary but is not used in the theorem: for a Gaussian mode, \(1-c_F^2=\tanh(\omega\ell_*)\). An interacting proof needs only the inequality (C5), not a Gaussian inverse formula.

## What “complete” means

The projection \(Q_r\) must contain the entire gauge-invariant vacuum complement in the claimed sector. It cannot omit:

- vacuum-balance directions created by a nonproduct interacting density;
- independent gauge-cycle and crossing-loop distinctions;
- diagonally paired boundary-charge sectors; or
- topological sectors included in the claimed physical theory.

A lower frame on one glueball operator, one collection of local marginals, one charged twist sector, or one finite parameter Hessian does not imply (C5). [[gauge-cycle-innovation-filtration/inq|Gauge-cycle innovations]] and [[vacuum-aligned-innovation-completion/inq|vacuum-aligned completion]] construct finite-regulator completeness ledgers; they do not prove the subunit norm.

## One action-derived route to the missing bound

[[collared-quasi-factorization-and-surface-response/inq|Collared quasi-factorization]] shows that a two-block variance or entropy inequality on the **whole** Euclidean cylinder forces the midpoint bridge floor when the two end collars are treated as one disconnected block. Wilson plaquettes can be typed as bounded finite-range interactions of compact cell spins at fixed regulator. The published complete-analyticity certificate, however, pays for transverse boundary cardinality and is not automatically uniform under continuum refinement.

[[nonlinear-whole-law-surface-response/inq|Nonlinear whole-law surface response]] makes the next comparison noncircular. The flat Wilson two-jet is a Maxwell cochain Hessian and has a gauge-invariant soft mode, so it cannot prove (C5). The candidate response must be constructed after the full nonlinear Wilson law is integrated and glued. A sufficient result would compare the actual bridge defect with an independently normalized whole-law Dirichlet response and prove that both inequalities have regulator-uniform constants.

## Continuum reconstruction theorem target

Assume a sequence satisfying (C1)--(C10) also has:

1. a common dense observable core whose pointed Euclidean forms converge in a generalized Mosco or comparably strong sense;
2. convergence of the vacuum projections and preservation of the one-dimensional vacuum kernel;
3. reflection positivity and the remaining Osterwalder--Schrader hypotheses in the limit;
4. reconstruction of a local, Poincare-covariant observable net on \(\mathbb R^4\) with the spectrum condition;
5. the prescribed short-distance Yang--Mills behavior, including the required gauge-invariant local fields and asymptotic-freedom/OPE identification; and
6. nontriviality of the limiting theory.

Then lower semicontinuity of the closed forms carries (C9) to

$$
H_{\mathrm{YM}}
\geq
\Delta_*(I-P_0),
\tag{C12}
$$

and hence

$$
\sigma(H_{\mathrm{YM}})\cap(0,\Delta_*)=\varnothing.
\tag{C13}
$$

After the Poincare representation has been reconstructed, [[joint-causal-generators-and-the-mass-casimir]] identifies the corresponding invariant-mass statement. Before that reconstruction, (C9) is a transfer-Hamiltonian estimate, not yet a mass Casimir.

## The fresh stopping condition

The whole research programme can now stop searching for new metaphors when it returns one concrete estimate:

$$
\boxed{
\sup_r
\left\|K_{n_r}Q_r\right\|
<1
\quad\text{at one fixed physical half-thickness }\ell_*,}
\tag{C14}
$$

on the complete Perron-dressed Wilson carrier, with the independent continuum and reconstruction hypotheses above. Every proposed wall, Hessian, entropy, knot, exceptional geometry, or global--local invariant should be evaluated by whether it constructs or bounds the operator in (C14) without reading the desired transfer spectrum backward into its definition.

