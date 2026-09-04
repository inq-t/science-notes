---
inq.module: "markov-edge-measure-solder"
inq.include:
  - "./"
inq.ambient:
  - "**"
---
# Markov Edge-Measure Solder

A bounded comparison between two reversible Markov defects can be proved before taking either spectrum by comparing their stationary two-slice measures. The comparison survives finite tensor products without multiplying one loss factor per component, restricts safely to a gauge-invariant carrier, and descends through a deterministic block map as a one-step kernel inequality. For a ground-state-transformed Osterwalder--Schrader transfer, the same theorem gives an explicit Radon--Nikodym certificate for soldering an independently constructed cylinder response to clock energy. The unresolved Yang--Mills problem is to prove that certificate for the interacting transfer kernel uniformly in volume and along continuum RG removal.

**Status: [EXACT] for the edge-measure comparison, tensor no-loss theorem, gauge restriction, deterministic pushforward, Doob edge formula, and transfer-energy implication under the stated hypotheses; [CONDITIONAL PHYSICAL IDENTIFICATION] for the Osterwalder--Schrader application; [OPEN] for a volume- and regulator-uniform interacting Wilson certificate.**

## A reversible defect is a two-slice form

Let \((X,\mathcal B,\nu)\) be a standard Borel probability space and let \(P\) be a self-adjoint Markov operator on \(L^2(\nu)\), represented by a transition kernel \(P(x,\mathrm dy)\). Its stationary edge measure is

\[
\mathrm d\mathsf J_P(x,y)
:=
\nu(\mathrm dx)P(x,\mathrm dy).
\tag{ME1}
\]

Reversibility is exactly symmetry of \(\mathsf J_P\). For every \(f\in L^2(\nu)\),

\[
\boxed{
\langle f,(I-P)f\rangle_\nu
=
\frac12\int_{X\times X}|f(x)-f(y)|^2
\,\mathrm d\mathsf J_P(x,y).}
\tag{ME2}
\]

Thus \(I-P\) operates on the difference between two consecutive presentations, not on either endpoint in isolation.

Let \(Q\) be another reversible Markov operator with the same invariant law. Restrict both edge measures to the off-diagonal and write the Lebesgue decomposition

\[
\mathsf J_P^\circ
=r\,\mathsf J_Q^\circ+\mathsf J_P^\perp,
\qquad
\mathsf J_P^\perp\perp\mathsf J_Q^\circ.
\tag{ME3}
\]

If

\[
\eta_{P\mid Q}
:=
\operatorname*{ess\,inf}_{\mathsf J_Q^\circ}r
>0,
\tag{ME4}
\]

then (ME2) gives the **edge-measure comparison theorem**

\[
\boxed{
I-P\geq\eta_{P\mid Q}(I-Q).}
\tag{ME5}
\]

This is a sufficient kernel certificate, not an equivalence: an operator-form comparison can hold even when no pointwise Radon--Nikodym lower bound does. Diagonal holding mass is irrelevant because it contributes zero to (ME2).

## Tensor products do not multiply the defect loss

The direct density ratio between product edge measures can deteriorate exponentially even when the operator comparison does not. Let \(P_i,Q_i\) be positive self-adjoint Markov contractions on \(L^2(\nu_i)\), for \(1\leq i\leq n\), and suppose

\[
I-P_i\geq\eta_i(I-Q_i),
\qquad
\eta:=\min\{1,\eta_1,\ldots,\eta_n\}>0.
\tag{ME6}
\]

Put \(P^{\otimes}=\bigotimes_iP_i\) and \(Q^{\otimes}=\bigotimes_iQ_i\). Then

\[
\boxed{
I-P^{\otimes}\geq\eta(I-Q^{\otimes}).}
\tag{ME7}
\]

**Proof.** Equation (ME6) gives

\[
0\leq P_i
\leq
R_i:=(1-\eta)I+\eta Q_i.
\tag{ME8}
\]

Positivity and monotonicity of finite tensor products imply

\[
P^{\otimes}\leq\bigotimes_iR_i.
\tag{ME9}
\]

For \(r_\eta(s)=1-\eta+\eta s\) and \(s,t\in[0,1]\),

\[
r_\eta(st)-r_\eta(s)r_\eta(t)
=
\eta(1-\eta)(1-s)(1-t)
\geq0.
\tag{ME10}
\]

Induction and joint spectral calculus for the operators on distinct tensor factors therefore give

\[
\bigotimes_iR_i
\leq
(1-\eta)I+\eta Q^{\otimes}.
\tag{ME11}
\]

Combining (ME9) and (ME11) proves (ME7). \(\square\)

In particular, if \(Q_i=e^{-\tau D_i}\), then

\[
Q^{\otimes}
=e^{-\tau\sum_iD_i}
\tag{ME12}
\]

on the product carrier. A local bounded solder therefore reaches the product flux generator with the worst local coefficient, not its \(n\)-th power. This exact fact explains why a globally multiplied density-ratio estimate can be far weaker than the true product coercivity. The [[contemporary-puzzles/yang-mills-mass-gap/finite-spacing-transfer-and-bounded-flux-solder#The pure product-Wilson bounded edge|pure product-Wilson theorem]] gives a sharper gauge-invariant instance by diagonalizing the spin-network carrier directly.

## Gauge restriction and deterministic blocking preserve the order

Suppose a compact gauge group acts unitarily on \(L^2(\nu)\), with averaging projection \(E_{\mathcal G}\), and both \(P\) and \(Q\) commute with that action. Their self-adjoint defects reduce the invariant subspace, so (ME5) restricts to

\[
I_{\mathrm{GI}}-P_{\mathrm{GI}}
\geq
\eta_{P\mid Q}
(I_{\mathrm{GI}}-Q_{\mathrm{GI}}).
\tag{ME13}
\]

Gauge averaging constructs the carrier on which this inequality is tested. Its own defect \(I-E_{\mathcal G}\) vanishes on every gauge-invariant excitation and is not the coercive operator in (ME13), as emphasized by [[contemporary-puzzles/yang-mills-mass-gap/gauge-dirichlet-trace-carrier#Gauge averaging is a projection to the carrier, not its defect|the gauge-carrier firewall]].

Now let \(B:X\to Y\) be a measurable block map, \(\bar\nu=B_*\nu\), and

\[
J_B:L^2(\bar\nu)\longrightarrow L^2(\nu),
\qquad
J_Bf=f\circ B.
\tag{ME14}
\]

The pushed stationary pair law

\[
\mathsf J_{\bar P}
:=(B\times B)_*\mathsf J_P
\tag{ME15}
\]

has both marginals \(\bar\nu\), is symmetric, and disintegrates to the reversible one-step Markov operator

\[
\bar P=J_B^*PJ_B.
\tag{ME16}
\]

If \(I-P\geq\eta(I-Q)\), then

\[
\boxed{
I-\bar P
=J_B^*(I-P)J_B
\geq
\eta J_B^*(I-Q)J_B
=\eta(I-\bar Q).}
\tag{ME17}
\]

Equivalently, edge-measure domination survives the pushforward because positive measure order survives \(B\times B\). This is the one-step kernel counterpart of the multiplicative observable-pullback form in [[trace-dirichlet-descent/inq#The variance-correct safe branch pulls observables back|Trace Dirichlet Descent]].

Equation (ME16) does not assert lumpability. In general

\[
\bar P^{\,n}
\neq
J_B^*P^nJ_B,
\tag{ME18}
\]

and a family \(J_B^*P_tJ_B\) need not obey the semigroup law unless \(\operatorname{Ran}J_B\) is invariant. Nor can (ME17) be run backward: a coarse gap leaves every forgotten fiber uncontrolled. The fiber inequalities, induced horizontal metric, and macro--micro coupling required for that lift are the content of [[contemporary-puzzles/yang-mills-mass-gap/two-scale-rg-descent-and-the-crossover-lemma|the two-scale RG problem]].

## The transfer Doob transform gives the physical certificate

Let \(T\) be a bounded self-adjoint positive operator on \(L^2(\mu)\) with symmetric nonnegative kernel \(K_T(x,y)\). Suppose its top eigenvalue \(\lambda_0>0\) is simple and has a strictly positive normalized eigenfunction \(\psi\). Put

\[
\mathrm d\nu=\psi^2\,\mathrm d\mu,
\qquad
P=M_\psi^{-1}\frac{T}{\lambda_0}M_\psi.
\tag{ME19}
\]

Then \(P\) is a reversible Markov operator on \(L^2(\nu)\), and its edge measure has the exact density

\[
\boxed{
\mathrm d\mathsf J_P(x,y)
=
\frac{\psi(x)K_T(x,y)\psi(y)}{\lambda_0}
\,\mathrm d\mu(x)\mathrm d\mu(y).}
\tag{ME20}
\]

Let \(D\geq0\) independently generate a conservative reversible Markov semigroup on the same vacuum carrier, and put \(Q_\tau=e^{-\tau D}\). If \(Q_\tau\) has a symmetric density \(q_\tau(x,y)\) relative to \(\nu\), then the pointwise two-slice estimate

\[
\boxed{
K_T(x,y)
\geq
\eta\lambda_0\psi(x)\psi(y)q_\tau(x,y)}
\tag{ME21}
\]

for \(\mu\otimes\mu\)-almost every off-diagonal pair is sufficient for

\[
I-P\geq\eta(I-e^{-\tau D}).
\tag{ME22}
\]

This is the kernel-level return type of the bounded solder in [[contemporary-puzzles/yang-mills-mass-gap/finite-spacing-transfer-and-bounded-flux-solder#The bounded-solder theorem|the finite-spacing transfer theorem]]. It compares stationary two-slice conductance, not merely the one-slice density \(\psi^2\). Bounds on \(\psi\) and \(\lambda_0\) are noncircular only when obtained from the action or vacuum construction without using the unknown nonvacuum transfer edge.

The same comparison also feeds a nonstationary theorem. For a positive
stage $P_k$, $I-P_k^2\geq I-P_k$, so, writing the comparison generator as
$G_k$, (ME22) supplies the explicit analysis map

\[
L_k=\sqrt{\eta_k}
\left(I-e^{-\tau_kG_k}\right)^{1/2}.
\]

[[transported-response-observability-solder/inq|Transported Response
Observability Solder]] proves that a uniform lower frame for the pulled-back
$L_k$ forces the whole ordered slab product to contract. Thus one local
kernel need not see every direction at one stage; complementary responses
may become complete only after transport. The edge-measure inequality is
the action-derived solder, while the transported Gramian is the separate
coverage theorem.

Assume \(P\) is injective, \(P\) and \(D\) have the same fixed-space projection \(P_0\), and

\[
D\geq\lambda_D(I-P_0),
\qquad
\lambda_D>0.
\tag{ME23}
\]

Then (ME22) gives, with

\[
\delta:=\eta(1-e^{-\tau\lambda_D}),
\tag{ME24}
\]

the contraction bound \(P|_{(I-P_0)L^2}\leq(1-\delta)I\). For \(0<\delta<1\), spectral calculus therefore yields the sharper logarithmic rate

\[
\boxed{
-\log P
\geq
-\log(1-\delta)(I-P_0)
\geq
\delta(I-P_0).}
\tag{ME25}
\]

If \(T/\lambda_0=e^{-a_\tau(H_T-E_0)/(\hbar c)}\) is the vacuum-normalized Osterwalder--Schrader transfer through Euclidean length \(a_\tau\), the ground-state unitary turns (ME25) into

\[
\boxed{
H_T-E_0
\geq
\frac{\hbar c}{a_\tau}
\log\!\bigl((1-\delta)^{-1}\bigr)(I-P_0).}
\tag{ME26}
\]

This last interpretation requires the reflection-positive transfer construction and the exact carrier identification developed in [[contemporary-puzzles/yang-mills-mass-gap/vacuum-boundary-gluing-and-wall-response|vacuum boundary gluing]]. A stochastic sampler kernel with the same invariant measure is not thereby physical clock transport.

## The interacting obligation is now a local two-slice estimate

For the pure product kinetic kernel, local comparisons and (ME7) avoid an exponential volume loss. The full Wilson transfer instead contains spatial-plaquette multipliers around the kinetic kernel, and its vacuum density is interacting. Neither its Doob kernel nor the reference vacuum-weighted heat kernel factorizes over links. A global minimum-to-maximum bound on \(\psi^2\) can therefore deteriorate exponentially with volume even when the true edge stays positive; [[contemporary-puzzles/yang-mills-mass-gap/mass-gap-no-gos#NG9 — A global vacuum-density ratio is not local mixing|the vacuum-density no-go]] already rules out treating that estimate as continuum evidence.

[[two-slice-innovation-geometry/inq|Two-Slice Innovation Geometry]] supplies
a complementary route that needs no density domination. It decomposes the
actual stationary pair law into complete orthogonal endpoint innovations and
bounds its maximal correlation by a scalar influence-matrix norm. Its exact
parity counterexample shows why isolated block marginals are insufficient:
every proper output block can be independent of the entire input slice while
one global mode retains correlation arbitrarily close to one.
Boundary-conditioned innovations or a genuine form comparison such as
(ME22) must
control that collective channel.

The remaining noncircular target is to derive, from the action or independently normalized block-RG data, either (ME21) or a weaker path-flow/form comparison implying (ME22). Write

\[
\delta_{a,L}
:=
\eta_{a,L}\left(1-e^{-\tau_a\lambda_{D,a,L}}\right).
\]

Strict positivity of the transfer forces \(0<\delta_{a,L}<1\) whenever the vacuum complement is nonzero. The coefficients must satisfy

\[
\boxed{
\liminf_{\substack{a\downarrow0\\L\uparrow\infty}}
\frac{\hbar c}{a_{\tau,a}\Lambda_{\mathrm{YM}}^{(\mathsf s)}}
\log\!\left((1-\delta_{a,L})^{-1}\right)
>0.}
\tag{ME27}
\]

This is the exact logarithmic stopping quantity. Its linearization with \(\delta_{a,L}\) is a weaker sufficient bound and is asymptotically equivalent only when that one-step defect tends uniformly to zero. The estimate must cover every nonvacuum gauge-invariant direction, remain uniform in spatial volume and the required boundary family, and coexist with convergence of carriers and vacuum projections. Gauge restriction and RG pushforward preserve a comparison already proved; they do not create it or lift it through forgotten fibers. Only after Osterwalder--Schrader reconstruction, continuum existence, and Poincare covariance does the resulting clock-energy floor become a Yang--Mills mass gap.
