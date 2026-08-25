# The Common Response Matrix as Hessian Geometry

After central evaluation, or sector by sector before it, the common response matrix becomes a Hessian geometry when one flat affine response manifold and one potential generate all of its homogeneous, observational, hidden, and mixed blocks. In a finite quantum exponential family that Hessian is the pullback of the Bogoliubov--Kubo--Mori metric, but neither Hessianity nor BKM uniqueness follows from the word *response*: the affine connection, state family, monotonicity class, and dual connections must be constructed. The tangent bundle of a real Hessian manifold then has a natural complexification with a canonical conjugation, providing a rigorous response-space model of \(6\to3\) without deriving physical three-space.

## The sectorwise identification

The canonical W1 datum is generally the package

$$
\mathfrak G^Z
=
(Z,\mathbf G^Z,\omega^Z),
$$

where [[program-core/center-valued-response|center-valued response and scalarization]] owns the split

$$
\mathbf G^Z
=
\mathbf F^Z
+\mathbf G^{Z,\mathrm{int}}
$$

between central-score Fisher density and internal sector BKM density. Normal evaluation by the central law \(\omega^Z=\varphi|_Z\) inherited from the whole state gives the unconditioned numerical metric; it does not select a fact. A conditional sector theorem instead uses the normalized internal metric \(G^{(\alpha),\mathrm{int}}\). Evaluating the joint density by a character also retains the sector's central-score term, so it is not the same operation, and neither operation makes \(\alpha\) actual without an instrument and outcome.

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

Averaging the sectors with fixed central weights gives another scalar metric, but it is Hessian with potential \(\sum_\alpha q_\alpha\Psi_\alpha\) only when those weights and the affine identification do not vary. A single potential and common normalization across all sectors are therefore additional cross-sector laws.

Thus the mixed response relation already used by [[program-core/common-response-matrix|the common response matrix]],

$$
\mathcal C^{(\alpha),\mathrm{int}}_{N\zeta\zeta}
=\partial_NG^{(\alpha),\mathrm{int}}_{\zeta\zeta},
$$

is one component of the Hessian cubic form. Equality of its permutations is an integrability test: response blocks independently chosen for CST and CWST need not arise from one \(\Psi_\alpha\).

[[affine-hessian-structure|The affine Hessian structure]] states the local theorem and the global obstructions. The tensor \(\nabla g\) is the Amari--Chentsov tensor only when the Hessian manifold is supplied by the relevant statistical model; a generic Hessian cubic should not inherit that physical interpretation by name alone.

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

in the declared affine chart. Pulling this state geometry back along the CRM readout map gives that sector's response matrix. Central averaging or factive evaluation is a later operation.

This is an **[EXACT FINITE-DIMENSIONAL MODEL]**. It does not prove that every CRM realization is Hessian or that its continuum response is finite. More generally, set

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

There is a genuine BKM selection theorem, but it has stronger hypotheses than “dually flat plus monotone.” [[bkm-selection-theorem|The qualified Grasselli--Streater theorem]] explains that on the full finite-dimensional faithful-state manifold, a monotone metric for which the particular exponential and mixture connections are mutually dual is a constant multiple of BKM. A selected CRM submanifold or quotient does not inherit this uniqueness automatically.

## What Hessian geometry buys

Once the construction is genuine, the programme gains more than a name.

- Every sector's response matrix is generated by one scalar potential rather than several fitted positive kernels; a common potential across sectors becomes a further test.
- The cubic tensor gives coordinate-invariant obstruction data after the affine connection is declared.
- Natural and expectation coordinates are related by a Legendre transform on the response manifold.
- Hidden-mode elimination can be tested for compatibility with the Hessian structure rather than performed block by block.
- The global existence question becomes a problem about affine holonomy, convexity, and the patching of local potentials.

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

For \(n=3\), this is an exact six-real-dimensional complexification with a three-real-dimensional fixed locus. [[tangent-bundle-complexification|The tangent-bundle note]] explains why this is an important debugging model but not a derivation of space: the real three-manifold \(M\) is input, and in CRM it initially parametrizes responses rather than spatial points.

## Impact on the larger programme

The Hessian reading sharpens four existing obligations.

### Common origin

CST's homogeneous response and CWST's spectral response have one origin only if they are pullbacks or reductions of one \(g=\nabla\mathrm d\Psi\). Agreement of separately fitted diagonal blocks is insufficient. The first nontrivial mixed jet is a falsifiable integrability condition.

### Reduction

Gauge quotient, constraint elimination, and Hessian formation need not commute. For genuine radical directions they may descend compatibly; for hidden physical modes, a Schur complement can change the effective Hessian and generate a determinant term. [[spectral-wall-descent/hidden-resolvent-and-seesaw|The hidden-resolvent module]] owns that algebra.

### Complex response space

The tangent bundle \(T\mathfrak D_{\mathrm{phys}}\) is a natural complex space of response base points and tangent displacements. Its conjugation can model a real slice of response data and may clarify what an antiholomorphic factive selection would have to preserve. It is generally noncompact and is not the compact conditional \(S^6\) geometry. The two constructions may occupy different layers; they are not automatically rivals or identical carriers.

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
6. If Grasselli--Streater uniqueness is invoked, construct the metric on the full finite faithful-state manifold, verify the source theorem's full monotonicity class and specified e/m duality, and only then pull back to CRM; otherwise prove a new restricted uniqueness theorem.
7. Test whether the Hessian structure globalizes across charts and scale fibers.
8. Keep tangent-bundle complexification distinct from the spatial carrier and prove any realization map between them.
9. Construct the independent spatial, gravitational, mass, and factual consumers.

The primary references and their precise roles are recorded in [[sources|the source ledger]].
