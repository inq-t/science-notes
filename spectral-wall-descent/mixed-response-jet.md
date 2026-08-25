# A Finite Mixed-Response Jet

A three-level exponential family exactly realizes the symmetry pattern proposed for the common response form: the homogeneous and observational directions are orthogonal at the symmetric reference, so \(G_{N\zeta}=0\), while the first scale derivative of observational response is nonzero. The resulting value \(\mathcal C_{N\zeta\zeta}=1/(2\sqrt2)\) is a nonseparable coupling witness within this declared one-potential model, calculated rather than fitted sector by sector.

## The family

Let

$$
\tau:=\frac{\mathbf1_3}{3},
$$

and define Hermitian generators

$$
Q_N
:=\frac{1}{\sqrt2}
\operatorname{diag}(1,1,-2),
$$

$$
Q_\zeta
:=\sqrt{\frac32}
\left(E_{13}+E_{31}\right).
$$

They satisfy

$$
\tau(Q_N)=\tau(Q_\zeta)=0,
$$

$$
\tau(Q_N^2)=\tau(Q_\zeta^2)=1,
\qquad
\tau(Q_NQ_\zeta)=0.
$$

Let \(H=U(2)\times U(1)\subset U(3)\) act block diagonally. The generator \(Q_N\) is an \(H\)-singlet, while \(Q_\zeta\) is one real component of the nontrivial off-diagonal \(i3\) representation. Since the tracial reference and its BKM form are \(U(3)\)-invariant, their vanishing quadratic pairing is both an explicit trace calculation and a representation-orthogonality statement.

Define

$$
K(N,\zeta)
:=NQ_N+\zeta Q_\zeta,
$$

$$
\rho_{N,\zeta}
:=\frac{e^{-K(N,\zeta)}}{Z(N,\zeta)},
\qquad
\Psi(N,\zeta):=\log Z(N,\zeta).
$$

At the reference \((N,\zeta)=(0,0)\), the BKM score metric is the tracial covariance. Therefore

$$
\boxed{
G_{NN}=1,
\qquad
G_{\zeta\zeta}=1,
\qquad
G_{N\zeta}=0.}
$$

## The cubic calculation

Because the generators are centered,

$$
\Psi(N,\zeta)
=\log3
+\frac12\tau(K^2)
-\frac16\tau(K^3)
+O(4).
$$

The mixed cubic tensor is

$$
\mathcal C_{N\zeta\zeta}
:=\left.
\partial_N\partial_\zeta^2\Psi
\right|_{(0,0)}
=-\tau(Q_NQ_\zeta^2).
$$

Now

$$
Q_\zeta^2
=\frac32(E_{11}+E_{33}),
$$

so

$$
\tau(Q_NQ_\zeta^2)
=-\frac{1}{2\sqrt2}.
$$

Hence the **[EXACT FINITE RESULT]** is

$$
\boxed{
\mathcal C_{N\zeta\zeta}
=\partial_NG_{\zeta\zeta}
=\frac{1}{2\sqrt2}
\simeq0.353553390593.}
$$

The quadratic mixed block vanishes, but the homogeneous coordinate changes the response geometry of the observational coordinate. This is precisely the higher-jet effect predicted in [[program-core/common-response-form|the common response construction]].

## What the model proves

It proves that

- one positive Hessian potential can generate both sectors;
- symmetry orthogonality can force the quadratic cross term to vanish;
- a nonseparable coupling within the declared one-potential model survives at cubic order; and
- its value is constrained by one algebraic multiplication table.

It does not prove that \(Q_N\) is cosmological scale, that \(Q_\zeta\) is curvature perturbation, or that the three-level family is a wall algebra. Those identifications require the consumer maps in CST and CWST.

The generators also illustrate why the cubic jet is more informative than a hand-assembled block matrix. If \(G_{NN}\) and \(G_{\zeta\zeta}\) were chosen independently, no multiplication law would force the value \(1/(2\sqrt2)\) or the equality of mixed derivatives.

## Verification

[[spectral-wall-descent/receipts/verify-spectral-wall.py|The finite receipt]] evaluates the log-partition function by matrix diagonalization. A centered finite difference with step \(10^{-3}\) returns

$$
\mathcal C_{N\zeta\zeta}^{\mathrm{FD}}
\simeq0.35355319,
$$

in agreement with the exact value.

## Upgrade path

The next model should replace the assigned generators by

- a scale singlet derived from a spectral or modular deformation;
- a mean-zero context deformation derived from \(E\) or \([D,\mathcal B]\); and
- a hidden finite-Dirac sector such as \(M_R\).

It should then calculate the full \((N,\zeta,h)\) Hessian, its wall-loss split, and the corresponding observable spectral-action Jacobian on one independently normalized carrier.
