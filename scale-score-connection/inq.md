---
inq.module: "scale-score-connection"
inq.include:
  - "**/*.md"
---
# The Scale-Score Connection

A derivative with respect to scale is not intrinsic when the probability carriers or Hilbert spaces change with scale. After the carriers have first been placed in a common bundle, the correctly typed derivative uses a metric connection; a pure-state scale score is then a projective tangent, while a changing observation channel contributes a separate conditional channel score. This makes Fisher response covariant after transport is supplied and proves a decisive nonuniqueness result: no nonzero score is invariant under all metric connections, because on a scale interval one can always make the chosen state section parallel.

**Status: [EXACT] for regular fixed-carrier classical Fisher realization, pure-state projective geometry, unitary frame covariance, connection dependence, and the dominated moving-channel score identity; [CONSTRUCTION TARGET] for a natural RG connection on blocked Yang--Mills carriers; [OPEN] for a mixed-state quantum extension, a scheme-covariant balanced grain, and continuum response.**

## Scale differentiation needs transport

Let \(I\) be a scale interval with coordinate \(N\), and let

$$
\mathcal H
\longrightarrow
I,
\qquad
N\longmapsto\mathcal H_N,
\tag{SC1}
$$

be a differentiable Hilbert bundle. This already restricts the problem: an ordinary locally trivial bundle has locally constant fiber type. RG blockings whose finite carriers genuinely change dimension require a prior common embedding, inductive or projective limit, continuous field, or correspondence construction before (SC1) applies. A normalized section \(\Omega_N\in\mathcal H_N\) represents a pure state at scale \(N\). The expression \(\partial_N\Omega_N\) is meaningless until neighboring fibers have been identified. Supply a metric connection \(\nabla_N\) and define

$$
Q_N:=I-|\Omega_N\rangle\langle\Omega_N|,
\qquad
v_N^{\nabla}:=2Q_N\nabla_N\Omega_N,
\qquad
\mathcal I_N^{\nabla}:=\|v_N^{\nabla}\|^2.
\tag{SC2}
$$

The projection removes the entire normalized complex reference line. Since metricity and normalization make the parallel component of \(\nabla_N\Omega_N\) purely imaginary, \(v_N^{\nabla}\) is the projective or Fubini--Study tangent after the \(U(1)\) phase direction has been removed; it is not the horizontal tangent of the supplied bundle connection and not a velocity through spacetime. For a mixed state represented by a purification, phase is not the full gauge: one must quotient the purification or commutant orbit, or choose a canonical standard-form representative. Equation (SC2) is therefore not yet a general quantum Fisher construction.

On one fixed classical carrier with dominating measure \(m\), assume \(p_N>0\) on common support, quadratic-mean differentiability, and enough domination to differentiate normalization under the integral. Put \(\Omega_N=\sqrt{p_N}\in L^2(m)\) and use the trivial connection. Then the DQM score agrees almost everywhere with \(s_N=\partial_N\log p_N\), and

$$
2\partial_N\Omega_N
=
s_N\Omega_N,
\qquad
4\|Q_N\partial_N\Omega_N\|^2
=
\int s_N^2p_N\,\mathrm dm.
\tag{SC3}
$$

Equation (SC3) is the ordinary Fisher information of the scale path. Here \(Q_N\) is redundant because normalization gives \(\langle\sqrt{p_N},\partial_N\sqrt{p_N}\rangle=0\). Moving support can add boundary or distributional terms and lies outside these hypotheses. Equation (SC2) is the corresponding pure-projective bundle construction, not a universal mixed-state identification.

## Frame covariance is not connection uniqueness

Choose a local trivialization in which

$$
\nabla_N=\partial_N+A_N,
\qquad
A_N^*=-A_N.
\tag{SC4}
$$

Under a differentiable unitary change of frame \(W_N\), set

$$
\Omega_N'=W_N\Omega_N,
\qquad
A_N'
=
W_NA_NW_N^{-1}
-(\partial_NW_N)W_N^{-1}.
\tag{SC5}
$$

Then

$$
\nabla_N'=W_N\nabla_NW_N^{-1},
\qquad
Q_N'=W_NQ_NW_N^{-1},
\qquad
v_N^{\nabla'}=W_Nv_N^{\nabla},
\tag{SC6}
$$

and therefore

$$
\boxed{
\mathcal I_N^{\nabla'}
=
\mathcal I_N^{\nabla}.}
\tag{SC7}
$$

This is covariance of a supplied connection. It does not say that the family \(\Omega_N\) selects one.

Indeed, over an interval every differentiable normalized section of a locally trivial Hilbert bundle admits a metric connection \(\nabla^{\parallel}\) satisfying

$$
\nabla_N^{\parallel}\Omega_N=0.
\tag{SC8}
$$

One construction uses a global unitary trivialization over the interval. Equivalently, split \(\mathcal H=\mathbb C\Omega\oplus\Omega^\perp\), declare \(\nabla(f\Omega)=\mathrm df\otimes\Omega\), and choose any metric connection on the complement. For this connection,

$$
v_N^{\nabla^{\parallel}}=0,
\qquad
\mathcal I_N^{\nabla^{\parallel}}=0.
\tag{SC9}
$$

This **connection-dependence no-go** is exact: no nonzero Fisher scale speed is invariant under all metric connections, and the state section does not determine transport on its orthogonal complement. The statement does not by itself forbid every possible functorial selection rule; such a categorical no-go would require a declared naturality category and admissible automorphisms. It does prove that a nonzero balanced-Fisher root needs additional composition, locality, symmetry, endpoint, or physical-observable data fixed before the desired grain is inspected.

Because the base \(I\) is one-dimensional, the curvature two-form of every ordinary connection is identically zero. Over an interval every connection is gauge-trivial and every closed-loop holonomy is trivial. A Wilson line between two endpoints becomes meaningful only after endpoint framings or identifications are fixed. Curvature can become informative on a multiparameter space of scales, couplings, cuts, or schemes; flat holonomy can be nontrivial on \(S^1\) or an isotropy loop of a parameter groupoid. An open groupoid arrow carries parallel transport, not gauge-invariant holonomy by itself.

## A moving channel has its own score

Let the input density be \(p_N(x)\) and let an observation or blocking channel have density \(c_N(z\mid x)\) relative to \(N\)-independent reference measures. Assume common positive supports and joint DQM or dominated differentiability sufficient to pass \(\partial_N\) through both normalizing integrals. Define

$$
s_N^X(x):=\partial_N\log p_N(x),
\qquad
u_N(x,z):=\partial_N\log c_N(z\mid x).
\tag{SC10}
$$

If \(q_N(z)=\int p_N(x)c_N(z\mid x)\,\mathrm dx\), direct differentiation gives

$$
\boxed{
s_N^Z(z)
=
\mathbb E_N[s_N^X(X)+u_N(X,Z)\mid Z=z]
=
K_Ns_N^X(z)+\chi_N(z),}
\tag{SC11}
$$

where

$$
K_Nf:=\mathbb E_N[f(X)\mid Z],
\qquad
\chi_N:=\mathbb E_N[u_N(X,Z)\mid Z].
\tag{SC12}
$$

Differentiating \(\int c_N(z\mid x)\,\mathrm dz=1\) gives \(\mathbb E[u_N\mid X]=0\), but it does not force \(\chi_N=0\). Thus \(K_Ns_N^X\) is the full output score only for a fixed channel or after a theorem proves that its conditional channel-score term vanishes. Moving support and singular deterministic channels require a separate pushforward or DQM formulation. [[library/a-note-on-insufficiency-and-the-preservation-of-fisher-information/inq|Pollard's DQM theorem]] owns the fixed-statistic score projection; equation (SC11) is the elementary dominated moving-channel extension.

[[conditional-fisher-coercivity/coarse-graining-and-moving-context|The conditional-Fisher transport theorem]] derives the associated tensor balance: input Fisher information plus channel Fisher information equals output information plus the missing conditional score covariance. It explains why fixed-channel monotonicity cannot be reused when the readout depends on the context being varied, even if every kernel remains normalized.

In bundle language, a family of contractions \(K_N:\mathcal H_N^X\to\mathcal H_N^Z\) has covariant derivative

$$
(\nabla K)_N
:=
\nabla_N^ZK_N-K_N\nabla_N^X.
\tag{SC13}
$$

The vanishing condition \(\nabla K=0\) says that the channel intertwines the two scale transports. Under independent unitary frame changes on the source and target,

$$
(\nabla K)'_N
=
W_N^Z(\nabla K)_N(W_N^X)^{-1},
\tag{SC13a}
$$

so its vanishing is frame-independent. This is bi-unitary covariance, not literal conjugation when source and target differ.

There is an exact classical solder. Take

$$
\mathcal H_N^X=L^2(p_N\,\mathrm dm_X),
\qquad
\mathcal H_N^Z=L^2(q_N\,\mathrm dm_Z),
\tag{SC13b}
$$

with unit reference sections \(1_X,1_Z\) and square-root-induced metric connections

$$
\nabla_N^Xf=\partial_Nf+\frac12s_N^Xf,
\qquad
\nabla_N^Zg=\partial_Ng+\frac12s_N^Zg.
\tag{SC13c}
$$

Since \(K_N1_X=1_Z\), equations (SC11)--(SC13) give

$$
\boxed{
2(\nabla K)_N1_X
=
s_N^Z-K_Ns_N^X
=
\chi_N.}
\tag{SC13d}
$$

Thus \(\chi_N\) is exactly one component of \(\nabla K\), evaluated on the reference section. Full horizontality implies \(\chi_N=0\); the converse need not hold.

For an already declared joint product-gradient form, this metric connection is not the same operation as its inherited derivative at fixed hidden coordinate. [[conditional-fisher-coercivity/moving-fiber-connection|The moving-fiber calculation]] proves that the latter becomes \(\partial_N-s_N/2\) after square-root transport, and annihilates the transported conditional vacuum. A Fisher term from the bare derivative of that vacuum cannot be inserted into the same generator without the compensating score term.

## A moving frame can erase an apparent scale

Let

$$
X_N\sim\mathcal N(0,e^{2N}).
\tag{SC14}
$$

On the fixed real-line carrier,

$$
s_N^X(x)=-1+e^{-2N}x^2,
\qquad
\mathcal I_N^X=2.
\tag{SC15}
$$

The scale-dependent bijection \(Y=e^{-N}X_N\) transports every member to \(\mathcal N(0,1)\), so the transported score and Fisher information are zero. The missing value has not been physically destroyed; the moving identification absorbed it. Because this is a singular deterministic, moving pushforward, it is a frame-change witness of (SC8)--(SC9), not literally an instance of the density hypotheses in (SC10).

[[library/exact-scheme-independence/inq|Exact renormalization-group kernels can be formulated as field connections]], while [[library/the-classically-perfect-fixed-point-action-for-su3-gauge-theory/inq|exact \(SU(3)\) blocking transformations contain free choices]]. Consequently, “exact blocking” and “canonical scale derivative” are different predicates.

## What each operator operates on

The construction separates four operators that are easily conflated:

- \(\nabla_N\) acts on sections of the scale-indexed state carrier and defines horizontal change of presentation;
- \(K_N\) acts on a tangent or distinction in one input fiber and returns its conditional prediction from the retained output;
- \(Q_N^X(I-K_N^*K_N)Q_N^X\) acts on the declared physical input-tangent fiber and measures its \(L^2\) contraction defect; and
- the transfer generator \(H-E_0\) acts on the reconstructed physical Hilbert space after a clock and Osterwalder--Schrader structure have been supplied.

For a contraction \(K_N\), the third quadratic form is exactly

$$
\left\langle f,Q_N^X(I-K_N^*K_N)Q_N^Xf\right\rangle
=
\|Q_N^Xf\|^2-\|K_NQ_N^Xf\|^2
\geq0.
\tag{SC16}
$$

Calling this defect *irrecoverable* requires a separate sufficiency or recovery theorem. The first operator can define a scale tangent. The third can carry a uniform dimensionless edge. Only the fourth has energy units. A theorem must construct and intertwine these carriers; notation alone cannot identify them.

## Admission test for a scale-derived grain

A scale-score grain is intrinsic to the proposed physical construction only after it provides:

1. the scale torsor or parameter base and its allowed changes of chart;
2. the bundle of state or response carriers over that base;
3. a metric RG connection selected independently of the target root;
4. the covariant channel term in (SC11), or a proof that it vanishes;
5. naturality under inequivalent admissible blocking schemes and field redefinitions;
6. a derived map from scale depth to physical collar length; and
7. a separate uniform response bound on the complete vacuum complement.

[[global-local-response-reconstruction/yang-mills-balanced-fisher-grain|The balanced-Fisher Yang--Mills proposal]] currently has a fixed-carrier score and response decomposition but not clauses 3--6. [[vacuum-aligned-transfer-cocycle/inq|The changing-carrier transfer cocycle]] supplies exact composition and defect ledgers for already declared carrier maps; it does not select the RG connection. The connection problem is therefore upstream of the gap theorem, not a new name for it.
