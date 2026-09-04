---
inq.module: "hessian-response-geometry"
inq.include:
  - "**/*.md"
---
# Hessian Structure on a Common Response Form

After a declared scalar evaluation, or within one normalized sector, a common response form becomes a Hessian geometry when one flat affine response manifold and one potential generate all of its homogeneous, observational, hidden, and mixed blocks. Calling the center-valued density itself Hessian would require a separately defined center-valued affine structure. In a finite quantum exponential family the scalar Hessian is the pullback of the Bogoliubov--Kubo--Mori metric, but neither Hessianity nor BKM uniqueness follows from the word *response*. The tangent bundle of a real Hessian manifold then has a natural complexification with a canonical conjugation, providing a rigorous response-space model of \(6\to3\) without deriving physical three-space.

## The scalar or sectorwise input

[[program-core/center-valued-response|Center-valued response and scalarization]] owns the W1 package, its central-score Fisher term, its internal sector metrics, and the distinction among normal evaluation, sectorwise reasoning, and character evaluation. An ordinary real Hessian manifold begins only after one scalar policy \(G^{\mathsf p}\) has been declared or one normalized sector metric \(G^{(\alpha),\mathrm{int}}\) has been selected for a conditional theorem. Calling \(\mathbf G^Z\) itself a Hessian metric requires a separately defined center-valued affine connection and potential.

Fix one sector \(\alpha\), let \(U\subset\mathfrak D_{\mathrm{phys}}^{(\alpha)}\) be a finite-dimensional smooth affine neighborhood with flat torsion-free connection \(\nabla\), and suppose a strictly convex potential

$$
\Psi_\alpha:U\longrightarrow\mathbb R
$$

obeys

$$
\boxed{
G^{(\alpha),\mathrm{int}}=\nabla\mathrm d\Psi_\alpha.}
$$

Then \((U,\nabla,G^{(\alpha),\mathrm{int}})\) is a Hessian manifold. In affine coordinates \(\lambda^I=(N,\zeta,h)\),

$$
G^{(\alpha),\mathrm{int}}_{IJ}
=\partial_I\partial_J\Psi_\alpha,
\qquad
\mathcal C^{(\alpha),\mathrm{int}}_{IJK}
:=(\nabla_I G^{(\alpha),\mathrm{int}})_{JK}
=\partial_I\partial_J\partial_K\Psi_\alpha.
$$

With fixed central weights and one affine identification, averaging the sector potentials gives the scalar Hessian \(\nabla\mathrm d(\sum_\alpha q_\alpha\Psi_\alpha)\). When the weights vary, the normal whole-state response is instead

$$
G^{\mathrm{whole}}
=I^{\mathrm F}[q]
+\sum_\alpha q_\alpha G^{(\alpha),\mathrm{int}},
$$

and it cannot be replaced by the weighted internal sum. Showing that this full joint metric is Hessian requires a common affine model for the central law and the conditional states, not merely sectorwise potentials.

[[vacuum-balance-fisher-geometry/inq|Vacuum-Balance Fisher Geometry]]
supplies the corresponding pointed-Hilbert decomposition for an atomic block
law: the real between-block vacuum directions carry exactly the Fisher score
metric, the internally centered blocks carry the conditional directions, and
the total Hilbert norm obeys the associated total-variance split. Its
imaginary balance directions remain phase rather than classical Fisher
tangents, so the Hilbert theorem does not by itself construct a joint Hessian
state manifold.

Thus the mixed response relation already used by [[program-core/common-response-form|the common response form]],

$$
\mathcal C^{(\alpha),\mathrm{int}}_{N\zeta\zeta}
=\partial_NG^{(\alpha),\mathrm{int}}_{\zeta\zeta},
$$

is one component of the Hessian cubic form. Equality of its permutations is an integrability test: response blocks independently chosen for CST and CWST need not arise from one \(\Psi_\alpha\).

[[affine-hessian-structure|The affine Hessian structure]] states the local theorem and the global obstructions. The tensor \(\nabla g\) is the Amari--Chentsov tensor only when the Hessian manifold is supplied by the relevant statistical model; a generic Hessian cubic should not inherit that physical interpretation by name alone.

[[relative-response-spectrum|A response spectrum is relative to a metric]] supplies the numerical gate: eigenvalues of a raw coordinate Hessian are not intrinsic. A generalized response spectrum is coordinate invariant only when response and reference metric are pulled back together, and its relative normalization remains part of the data.

## When the Hessian is BKM

Suppose one fixed finite algebra in one central sector carries a faithful affine exponential family

$$
\rho_\lambda
=
\exp\!\left(
\log\rho_0+\lambda^IA_I-\psi(\lambda)
\right),
\qquad
\psi(\lambda)=\log\operatorname{Tr}
e^{\log\rho_0+\lambda^IA_I}.
$$

Then

$$
\partial_I\partial_J\psi
=g^{\mathrm{BKM}}_{\rho_\lambda}
(\dot\rho_I,\dot\rho_J)
$$

in the declared affine chart. Pulling this state geometry back along the CRF readout map gives that sector's response form. By [[measured-response-carriers/inq#Parameter Hessians are pullbacks, not new carriers|the pullback-radical theorem]],

$$
\operatorname{rad}G_\lambda
=
\ker D\rho_\lambda.
$$

It is a metric only after parameter directions that induce no state tangent
have been quotiented. Equivalently, the centered generators must be linearly
independent modulo the scalar identity. Central averaging or factive
evaluation is a later operation.

This is an **[EXACT FINITE-DIMENSIONAL MODEL]**. It does not prove that every CRF realization is Hessian or that its continuum response is finite. More generally, set

$$
\rho_\lambda
=\frac{e^{-K(\lambda)}}{Z(\lambda)},
\qquad
Z(\lambda)=\operatorname{Tr}e^{-K(\lambda)},
$$

and center an operator by \(\widetilde A=A-\operatorname{Tr}(\rho_\lambda A)\mathbf1\). In the observable-score convention,

$$
\partial_I\partial_J\log Z
=g^{\mathrm{BKM}}_{\rho_\lambda}
\left(
\widetilde{\partial_IK},
\widetilde{\partial_JK}
\right)
-\operatorname{Tr}
\left(
\rho_\lambda\,\partial_I\partial_JK
\right).
$$

Thus a nonlinear modular Hamiltonian contributes an acceleration term, and the raw log-partition Hessian need not be the positive BKM pullback in those coordinates.

[[bridge-score-fusion-geometry/inq|Bridge-Score Fusion Geometry]] gives a
carrier-level instance of the same sign. After a two-step kernel is
conditioned on both endpoints, the centered logarithmic derivative of its
middle bridge lies in the scalarized fusion residue. Its Fisher Gramian is
the conditional score covariance, while the differentiated normalized GNS
half-density has one quarter of that Gramian. For
\(\mathscr A=-\log\int e^{-\mathscr V}\),

$$
\nabla^2\mathscr A
=
\mathbb E[\nabla^2\mathscr V]
-\operatorname{Cov}(\mathrm d\mathscr V,\mathrm d\mathscr V).
$$

An arbitrary middle-slice source \(f\), rather than a finite parameter list,
then yields the bounded analysis
\((I-\mathbb E[\,\cdot\mid X_0,X_{2n}])f(X_n)\). Its Gramian is an operator on
the full slice \(L^2\) carrier. This is a genuine response operator; a
uniform lower frame for it remains an additional analytic theorem.

A programme-specific **[OPEN ANSATZ]** is one represented modular or Dirac-derived family

$$
K(N,\zeta,h)
=K_0+NQ_N+\sum_a\zeta^aQ_a^{\mathrm{obs}}+Q_F(h)
$$

whose faithful Gibbs states and readout maps supply all CRF blocks at once. Inner fluctuations can provide algebraic metric deformations while preserving an underlying representation class, but a completely positive readout, transport, quotient, and continuum normalization still have to be built. The spectral-action Hessian must not be identified with the positive BKM pullback merely because both depend on the same Dirac family.

There is a genuine BKM selection theorem, but it has stronger hypotheses than “dually flat plus monotone.” [[bkm-selection-theorem|The qualified Grasselli--Streater theorem]] explains that on the full finite-dimensional faithful-state manifold, a monotone metric for which the particular exponential and mixture connections are mutually dual is a constant multiple of BKM. A selected CRF submanifold or quotient does not inherit this uniqueness automatically.

## What Hessian geometry buys

Once the construction is genuine, the programme gains more than a name.

- Every sector's response matrix is generated by one scalar potential rather than several fitted positive kernels; a common potential across sectors becomes a further test.
- The cubic tensor gives coordinate-invariant obstruction data after the affine connection is declared.
- Natural and expectation coordinates are related by a Legendre transform on the response manifold.
- Hidden-mode elimination can be tested for compatibility with the Hessian structure rather than performed block by block.
- The global existence question becomes a problem about affine holonomy, convexity, and the patching of local potentials.

The Hessian form canonically lowers an index,

$$
g^\flat:T_\lambda U\longrightarrow T_\lambda^*U.
$$

It is not a response endomorphism until a separately normalized source norm
or Riesz map identifies tangent and cotangent carriers. Consequently, matrix
eigenvalues of \(G_{IJ}\) are not intrinsic spectral gaps: they depend on
the tangent normalization and coordinates. The reusable carrier distinction
is developed in [[measured-response-carriers/inq]].

Legendre duality does **not** perform the Fourier covariance-to-precision map. The former relates dual affine coordinates on one statistical manifold; [[basic-concepts/hessians/fourier-covariance-and-precision|the latter]] inverts an operator after a carrier, measure, and Fourier convention have been supplied. W2 still needs its carrier-changing realization.

## Tangent-bundle complexification

For a real Hessian manifold \((M,\nabla,g)\), the connection splits \(T(TM)\) into horizontal and vertical copies of \(TM\). The Dombrowski construction defines a natural complex structure and compatible metric on \(TM\); flatness makes the almost-complex structure integrable, and the Hessian condition makes the resulting Hermitian structure Kähler.

In affine coordinates,

$$
z^i=x^i+iy^i,
$$

and fiber inversion is complex conjugation:

$$
\tau(x,y)=(x,-y),
\qquad
\tau(z)=\bar z,
\qquad
\operatorname{Fix}(\tau)=M.
$$

Consequently,

$$
\dim_{\mathbb R}M=n
\quad\Longrightarrow\quad
\dim_{\mathbb C}TM=n,
\qquad
\dim_{\mathbb R}TM=2n.
$$

For \(n=3\), this is an exact six-real-dimensional complexification with a three-real-dimensional fixed locus. [[tangent-bundle-complexification|The tangent-bundle note]] explains why this is an important debugging model but not a derivation of space: the real three-manifold \(M\) is input, and in the CRF it initially parametrizes responses rather than spatial points.

Nor does the Dombrowski complex structure on \(TM\) supply the positive
Hermitian extension of a real response form to a complex physical Hilbert
or Hamiltonian-form carrier. Those are different complexifications and
require an explicit comparison map.

## Impact on the larger programme

The Hessian reading sharpens four existing obligations.

### Common origin

CST's homogeneous response and CWST's spectral response have one origin only if they are pullbacks or reductions of one \(g=\nabla\mathrm d\Psi\). Agreement of separately fitted diagonal blocks is insufficient. The first nontrivial mixed jet is a falsifiable integrability condition.

### Reduction

Gauge quotient, constraint elimination, and Hessian formation need not commute. For genuine radical directions they may descend compatibly; for hidden physical modes, a Schur complement can change the effective Hessian and generate a determinant term. [[spectral-wall-descent/hidden-resolvent-and-seesaw|The hidden-resolvent module]] owns that algebra.

### Complex response space

The tangent bundle \(T\mathfrak D_{\mathrm{phys}}\) is a natural complex space of response base points and tangent displacements. Its conjugation can model a real slice of response data and may clarify what an antiholomorphic factive selection would have to preserve. It is generally noncompact and is not the compact integrable \(S^6\) geometry. The two constructions may occupy different layers; they are not automatically rivals or identical carriers.

### Consumer maps

Even a perfect Hessian/BKM construction returns state-space response. It does not by itself return

$$
\text{spatial precision},
\quad
\text{stress tensor},
\quad
\text{Lorentzian curvature},
\quad
\text{mass matrix},
\quad\text{or}\quad
G.
$$

Those are typed consumer maps. The BKM-to-spatial map remains W2, while the state-to-geometry and areal-normalization welds remain separate.

## Construction gates

1. Specify the response manifold or stack and its physical tangent quotient.
2. State whether the Hessian claim concerns the internal conditional metric, the whole-state normal evaluation, or the full center-valued density. Keep algebraic character evaluation distinct from both conditionalization and an instrumentally realized fact, and prove any common cross-sector normalization.
3. Construct a flat torsion-free connection rather than assuming preferred coordinates.
4. Exhibit potentials \(\Psi_\alpha\) whose Hessians give every claimed block.
5. Prove positivity and control the radical after gauge reduction.
6. If Grasselli--Streater uniqueness is invoked, construct the metric on the full finite faithful-state manifold, verify the source theorem's full monotonicity class and specified e/m duality, and only then pull back to the CRF; otherwise prove a new restricted uniqueness theorem.
7. Test whether the Hessian structure globalizes across charts and scale fibers.
8. Keep tangent-bundle complexification distinct from the spatial carrier and prove any realization map between them.
9. Construct the independent spatial, gravitational, mass, and factual consumers.

The primary references and their precise roles are recorded in [[sources|the source ledger]].
