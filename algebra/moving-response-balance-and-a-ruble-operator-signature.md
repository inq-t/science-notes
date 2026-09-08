# Moving Response Balance and a Ruble Operator Signature

A whole-to-local process can change both a distinction and the response by which that distinction is measured. Its intrinsic loss is therefore not the dissipative part of a matrix in a fixed norm: it is the defect of transport relative to the moving response. This gives an exact compositional balance and a covariant infinitesimal operator on distinction tangents, before any parameter is identified with spacetime clock time. A proposed Ruble operator is a comparison of this defect with a second response on the same carrier. The construction supplies a type signature and a finite information-geometric member, not an arena-making law or a Yang--Mills mass gap.

## The input is a comparison of presentations

Let a category of admissible processes assign a finite-dimensional real or complex vector space \(V_c\) to each context \(c\), a positive-definite response form \(G_c\) on it, and a linear map \(F_a:V_c\to V_d\) to an arrow \(a:c\to d\). Require \(F_{ba}=F_bF_a\) and \(F_{\mathrm{id}_c}=I_{V_c}\), and assume
\[
F_a^*G_dF_a\le G_c.
\tag{MR1}
\]
Here \(G_c\) is initially a form on distinctions, not a spacetime metric or Newton's constant. The star in coordinates is the ordinary transpose or conjugate transpose used to pull a form back. It does not assert that the process has a physically admissible reverse.

The finite-dimensional assumptions make all formulas below ordinary matrix identities. Degenerate forms require a justified radical quotient; changes of rank require separate charts. Closed unbounded forms and Type-III tangent domains require additional hypotheses, not the substitution of infinite matrices into these formulas.

Define the arrow defect as a form on the **incoming** carrier:
\[
\boxed{D_a:=G_c-F_a^*G_dF_a\ge0.}
\tag{MR2}
\]
For \(b:d\to e\), direct cancellation gives
\[
\boxed{D_{ba}=D_a+F_a^*D_bF_a.}
\tag{MR3}
\]
The second loss must be pulled back through the first process. Adding two untransported numbers called entropy would miss this structure.

For \(x\in V_c\), the same law reads
\[
G_c[x]=G_d[F_ax]+D_a[x].
\tag{MR4}
\]
It is a response balance between retained and unretained distinctions. It is not a claim that information is a conserved physical substance. One may package (MR4) into an isometry into a direct sum of retained and defect spaces, but that bookkeeping neither constructs a unitary whole nor supplies an observed record. The separate [[program-core/record-scale-soldering|record--scale construction]] addresses persistent facts and their ordering.

An invertible arrow with an admissible inverse has \(D_a=0\): apply (MR3) to its identity composite, whose two positive summands must vanish. Conversely, an isometry need not have an admissible inverse unless surjectivity and membership in the process category are established. These are the moving-form counterparts of [[quotient-unitarity-and-kernel-stabilization|quotient unitarity]].

## The infinitesimal balance includes motion of the response

On a positive, constant-rank smooth path, choose coordinates and an increasing parameter \(u\). This parameter only labels the path; it is not yet proper time, modular time, or a fourth spacetime coordinate. Suppose the evolution family satisfies
\[
T(u+du,u)=I+K_u\,du+o(du),\qquad G_{u+du}=G_u+\dot G_u\,du+o(du).
\]
The derivative of (MR2) is
\[
\boxed{R_u:=-\dot G_u-K_u^*G_u-G_uK_u\ge0.}
\tag{MR5}
\]
Its type is a positive form per unit \(u\): a map from distinction tangents into their duals with a process-density weight. It is not an endomorphism, a probability amplitude, or an energy until further comparisons are supplied.

For \(x_u=T(u,u_0)x_0\),
\[
\frac d{du}G_u[x_u]=-R_u[x_u],
\]
and hence
\[
G_{u_0}[x_0]-G_{u_1}[T(u_1,u_0)x_0]
=\int_{u_0}^{u_1}R_u[T(u,u_0)x_0]\,du.
\tag{MR6}
\]
Thus (MR5) is the differential version of the exact cocycle, not a separate assertion of stationary action. It can be written as a balance law
\[
\dot G+K^*G+GK+R=0.
\tag{MR7}
\]
The response-preserving special case is \(R=0\). A fixed response then gives \(K^*G+GK=0\), the infinitesimal isometry condition. A clock, a symplectic realization and an action still require the separate constructions in [[quotient-clock-and-stationary-action]] and [[cauchy-response-and-local-action]].

For a bounded smooth finite-dimensional evolution, finite-step transport is linearly invertible. A positive defect therefore does not mean that its underlying matrix lacks an inverse. Rather, that inverse cannot be an admissible response contraction on the affected directions. Genuinely noninjective jumps remain possible in the arrow formulation (MR1)--(MR3); they are not produced merely by calling a smooth contraction irreversible.

## An apparent loss can be a changing yardstick

Take \(G_u=e^{2u}I\) and \(K_u=-I\). Coordinate components decay, \(x_u=e^{-u}x_0\), but
\[
R_u=-2G_u+2G_u=0,\qquad G_u[x_u]=\|x_0\|^2.
\tag{MR8}
\]
Calling \(-K\) an intrinsic forgetting rate would be wrong. In normalized coordinates \(y_u=e^ux_u\), both the response and the vector are stationary.

Conversely, \(K_u=0\) with \(G_u=e^{-2u}I\) gives \(R_u=2G_u\): the transported coordinate is unchanged but the specified response to it decreases. This is a genuinely different pair \((T,G)\), not a coordinate rewriting of the lossless example. Neither example identifies \(G\) with cosmic expansion. Their lesson is that the process and its arena of comparison must be typed together.

## The balance is independent of a chosen presentation

Under a differentiable invertible frame change \(x=S_uy\), the same process has
\[
\widetilde G=S^*GS,\qquad
\widetilde K=S^{-1}KS-S^{-1}\dot S,
\qquad
\boxed{\widetilde R=S^*RS.}
\tag{MR9}
\]
Substitution in (MR5) cancels all derivatives of \(S\). Consequently the relative eigenvalues of \(R\) against \(G\) do not depend on this moving frame. By contrast, the eigenvalues of the coordinate matrix \(-K\) can change.

There is a second covariance. Under \(u=f(v)\), \(f'>0\),
\[
R^{(v)}=f'R^{(u)},\qquad G^{(v)}=G^{(u)}.
\tag{MR10}
\]
The relative operator \(G^{-1/2}RG^{-1/2}\) is therefore a **rate**, not a parameter-independent scalar. An ordering alone does not fix that rate.

Suppose the same construction supplies a positive-definite comparison form \(C_u\) with the same process-density weight, so \(C^{(v)}=f'C^{(u)}\). Then the proposed **Ruble response pencil** is
\[
(R_u,C_u),\qquad
\mathfrak R_u=C_u^{-1/2}R_uC_u^{-1/2},\qquad
\lambda_*=
\inf_{x\ne0}\frac{R_u[x]}{C_u[x]}.
\tag{MR11}
\]
The generalized spectrum is invariant under both changes of frame and increasing reparameterizations. Indeed, frame changes take the pencil by congruence; whitening with \(C\) turns that congruence into unitary similarity. The common factor \(f'\) cancels under reparameterization.

Equation (MR11) is a provisional operator signature, not a new value of the existing [[program-core/ruble-equations|Ruble matching field]]. It specifies what an exchange ratio must operate on: two responses to the same distinction, transported by one process. The [[mass-scale-calibration/internal-yardstick-as-a-generalized-rate-edge|generalized-rate-edge theorem]] owns the further closed-form and physical-comparison requirements. No clock is derived by arbitrarily choosing \(C\).

The method parallels [[deriving-g-v2/the-g-free-first-law|the G-free first law]]: identify the common ledger and its separate presentations before composing their exchange rates. Here the comparison is quadratic and tangent-valued. The [[mass-scale-calibration/mass-and-g-as-dual-exchange-rates|dual-rate analysis]] explains why an ordinary entropy differential cannot simply be substituted into that slot.

For example, \(C_u=\ell_uG_u\) with a positive one-form \(d\tau=\ell_u\,du\) makes (MR11) a response rate per \(\tau\). Whether \(\tau\) is a physical clock must be proved by its realization. An intrinsic normalization on a nonzero-loss path is
\[
\ell_u=\frac1r\operatorname{Tr}(G_u^{-1}R_u),\qquad r=\dim V_u,
\tag{MR12}
\]
where it is nonzero. It gives unit mean relative rate. It does not give a positive least rate uniformly: with \(G=I\) in two dimensions, \(R=\operatorname{diag}(2-\epsilon,\epsilon)\) has \(\ell=1\) but minimum \(\epsilon\to0\). Deriving a mean exchange rate and excluding almost-invisible directions remain different tasks.

This trace normalization has an exact arrow-level meaning. For invertible transport between equal-rank carriers with \(r>0\), define
\[
\boxed{\tau(a):=-\frac1r\log\det\!\left(G_c^{-1}F_a^*G_dF_a\right).}
\tag{MR12a}
\]
The matrix inside the determinant is similar to a positive contraction, so \(0<\det\le1\) and \(\tau(a)\ge0\). Determinant multiplication gives
\[
\tau(ba)=\tau(a)+\tau(b).
\]
Along the smooth evolution, Jacobi's determinant formula and (MR5) give
\[
\boxed{\tau\!\left(T(u_1,u_0)\right)
=\int_{u_0}^{u_1}\frac1r\operatorname{Tr}(G_u^{-1}R_u)\,du.}
\tag{MR12b}
\]
It is minus the logarithm of the product of squared response singular values, divided by \(r\). On a real rank-\(r\) carrier the determinant is the square of the metric-volume ratio. On a complex rank-\(r\) carrier it equals the real metric-volume ratio in real dimension \(2r\); determinants and ranks in (MR12a) are taken over the declared base field. Both formulas are invariant under endpoint frame changes. This cocycle belongs to processes, not necessarily to objects: different paths between the same contexts can have different values.

The scalar therefore need not be put in by a human clock. But neither should its scope be concealed. It is finite here because rank is fixed and the maps are invertible. A singular same-rank arrow has infinite log cost, and a rank-changing arrow is outside this determinant formula.

[[finite-entropy-cost-and-rank-changing-readout|Finite entropy readout]] supplies a distinct finite-cost construction for an actual sphere-to-ball quotient. Its cost depends on the incoming density and composes with the processed state; repeating an already-applied expectation costs zero. Its \(L^2\) density carriers are infinite dimensional, despite the finite geometric dimensions. This is not a continuation of (MR12a): a rank-one projection-pair witness proves that simply deleting zero singular values destroys determinant-cost additivity.

The [[qubit-cone-interiorization-and-the-clock-gap|qubit cone test]] also keeps the entire state space and its entropy capacity fixed while a genuine CP process develops an arbitrarily slow direction. Capacity, accumulated cost, and the smallest relative rate therefore occupy different slots even within finite information geometry.

There is one exact rigidity route. If the retained context symmetries preserve \(G\) and \(R\) and act irreducibly on \(V\), the self-adjoint relative operator \(G^{-1/2}RG^{-1/2}\) has invariant eigenspaces and must be scalar. Thus \(R=\ell G\), and its nonzero trace-normalized pencil is \(I\). This is a finite same-carrier result; irreducibility and response invariance on the complete physical field carrier have not been derived. Neither its dimension \(r\) nor its normalized scalar is a spatial dimension or a physical mass.

## Information geometry supplies an exact member

Take faithful finite-dimensional reference states \(\rho_c\), state-tangent spaces of traceless self-adjoint matrices, and \(G_c=g^{\mathrm{BKM}}_{\rho_c}\). For a CPTP map \(\Phi_a\), set \(\rho_d=\Phi_a\rho_c\) and \(F_aX=\Phi_aX\), restricting to the output support when required. The [[contemporary-puzzles/yang-mills-mass-gap/descent-loss-cocycle-and-recovery-fork|descent-loss theorem, D4--D5c]] proves (MR1)--(MR3) by differentiating data processing:
\[
D(\rho_c+\epsilon X\Vert\rho_c)
-D(\rho_d+\epsilon F_aX\Vert\rho_d)
=\frac{\epsilon^2}{2}D_a[X]+o(\epsilon^2).
\tag{MR13}
\]
The derivative in \(\epsilon\) measures a state distinction. The derivative in \(u\) in (MR5) measures transport of such distinctions. They are not interchangeable derivatives of one quantity called time or entropy.

For a same-dimension unital channel and the tracial reference, the full relative-entropy deficit equals the entropy increase. More generally it is lost relative distinguishability, not automatically thermodynamic entropy production. At a maximally mixed stationary state, entropy production can vanish while its tangent defect is strictly positive: it describes how perturbations would be forgotten, not a continuing creation of facts at that state.

The [[peirce-context-averaging-and-the-emergent-qubit-process|Peirce context member]] gives a useful exact calibration. On its three-dimensional traceless qubit tangent space the retained map is multiplication by \(1/3\), so
\[
D_\Phi=\frac89G.
\tag{MR14}
\]
Under its declared unit-rate Poisson interpolation, \(T_s=e^{-2s/3}I\) and \(R_s=\frac43G\). Under the distinct logarithmic interpolation \(T_s=3^{-s}I\), the rate is \(R_s=2\log3\,G\). They reach the one-step map at \(s=\frac32\log3\) and \(s=1\), respectively. Its intrinsic volume cost (MR12a) is \(2\log3\) in both cases. The geometry fixes the one-step comparison; these interpolations do not assign it the same external process duration. No physical duration or mass follows merely from the dimensionless cost.

## What the balance does not select

Choose a normalized frame with \(G=I\). Equation (MR5) becomes
\[
K+K^*=-R,
\qquad
K=Q-\frac12R,\qquad Q^*=-Q.
\tag{MR15}
\]
The positive defect fixes the symmetric part but leaves the skew part \(Q\) undetermined. Along one open path a moving unitary frame can remove \(Q\); interpreting it as physical reversible dynamics therefore requires retained endpoint, observable, localization or holonomy data. Moreover, an arbitrary response-isometric rotation need not be an automorphism of a local observable algebra. Thus the balance has not yet selected observable clock dynamics, even when its loss is known exactly.

For example, \(G=I\), \(R=\rho I\), \(\rho>0\), and any constant skew-adjoint \(Q\) give
\[
T_s=e^{-\rho s/2}e^{sQ},\qquad D_{T_s}=(1-e^{-\rho s})I.
\tag{MR16}
\]
Even the complete finite loss cocycle can therefore be identical for different transports in a held frame. The missing data cannot be recovered from that scalar contraction history.

[[oriented-projection-cycles-and-joint-response|Oriented projection cycles]] supply one explicit geometric completion of this missing skew part. A fixed graph polygon and ordered projection protocol compute both \(S\) and \(H\) in the returned contraction generator \(S+iH\), with the sharp form bound \(-\cot(\pi/m)S\le H\le\cot(\pi/m)S\). The bound does not transfer a loss floor to a phase floor. Every pair in the triangle's sectorial cone can be realized by choosing its graph maps, and smooth refinement can keep phase while eliminating loss. Thus fixed-primitive joint selection and a law restricting the admissible primitives are separate achievements.

The required new law must constrain \(G\), \(F\), the comparison \(C\), and the local realization together. In particular it must determine which incoming distinctions become physical nonvacuum excitations; completely erased directions have no nonzero output tangent, while exactly recoverable directions have zero defect. The recovery fork cannot be bypassed by renaming an incoming loss as mass.

[[sphere-to-ball-descent-and-the-jacobi-response|The spherical readout member]] now constrains several outputs together: its projection pushes forward the round law and spherical generator, while [[jordan-covariance-and-the-entropy-weighted-ball|Jordan covariance and fiber volume]] determine the retained co-metric and weighted drift. A hidden rotational drift can disappear under that same readout without changing the local detailed-balanced process. This is a concrete common realization, not a derivation of its round geometry, whole generator or physical clock. The conditional loss and retained diffusion remain different operators on different distinctions.

This is the precise place for the proposed arena-making interpretation. The object to construct is a response-valued process law, with its own realization and composition rules, whose physical representations return space, clock, scale and the appropriate invariant excitation bound. The continuum transport example in [[refining-holonomy-and-a-finite-continuum-threshold]] is a diagnostic of those return obligations, not the primitive of this programme. Its supplied background can force a probe threshold without being a source-free gauge vacuum, as [[joint-transport-variance-and-the-source-free-obstruction|the joint-variance test]] proves.

For a Clay claim, the resulting observable representation must still be the stipulated nontrivial four-dimensional Yang--Mills theory, with a uniform vacuum-complement bound in the required limits and the correct joint translation spectrum. A Born-like rule assigning weights to already specified outcomes would not alone determine their spectral support. The ambitious step is to construct that support and its arena from the same law, not merely to rename the gap.

[[directed-analytic-realization/moving_response_receipt.py|The moving-response receipt]] checks finite arrow composition, moving frames, response pencils, determinant costs and the Peirce calibration. [[directed-analytic-realization/moving-response-receipt-output.txt|Its output]] separates exact rational identities from numerical exponential and logarithmic checks; neither constitutes the open physical realization.
