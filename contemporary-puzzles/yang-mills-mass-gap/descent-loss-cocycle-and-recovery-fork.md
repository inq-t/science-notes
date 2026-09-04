# The Descent-Loss Cocycle and the Recovery Fork

Relative entropy supplies an exact state-pair-indexed data-processing deficit whose values add with transported arguments under channel composition, but a carrier audit exposes a decisive fork. On directions that the channel can exactly recover, the loss vanishes; on directions it completely erases, the loss remains upstream and has no nonzero output tangent on which a mass could act. The restriction-loss construction and its Connes-cocycle zero set extend exactly to faithful normal states on arbitrary von Neumann algebras, including Type III; on any declared smooth tangent class, its Hessian is the difference between upstream and restricted information metrics. For a state-preserving conditional expectation this Hessian is exactly the squared BKM norm of the forgotten vertical component, while its minimum over lifts of every retained tangent is zero. Thus the one-channel quotient already has a trivial unit lower edge in the wrong place: it supplies neither retained physical stiffness nor its normalization. A Yang--Mills gap would follow only after a physically normalized, jointly transverse family of pullbacks, an independently normalized Poincare-Casimir solder, a dimensional yardstick, and a continuum theorem are constructed.

**Status: [EXACT FINITE-DIMENSIONAL CHANNEL THEOREMS; EXACT TYPE-III-COMPATIBLE RESTRICTION LOSS AND SUFFICIENCY CRITERION; EXACT PRESERVING-EXPECTATION VERTICAL HESSIAN SPLIT; CONDITIONAL HESSIAN-OPERATOR CONSTRUCTION ON A DECLARED TANGENT DOMAIN; EXACT QUOTIENT-METRIC CONSTRUCTION; NO INDEX-ONLY PHYSICAL FLOOR; CONDITIONAL MASS-GAP IMPLICATION; OPEN YANG--MILLS AND CONTINUUM REALIZATION].** The construction is compatible with a deterministic pre-observable ground. Channels encode accessible state transformation and need not be ontological dynamics. Here *descent loss* always means loss under a separately declared nonfaithful realization or channel after gluing; strict effective descent itself is equivalence-level bookkeeping and creates neither residue nor chance.

## Relative-entropy loss is an arrow cost

For faithful finite-dimensional states $\rho$ and $\sigma$ and a completely positive trace-preserving channel $\Phi$, define

$$
\boxed{
\mathcal L_\Phi(\rho;\sigma)
:=
D(\rho\Vert\sigma)
-D(\Phi\rho\Vert\Phi\sigma).}
\tag{D1}
$$

Data processing gives

$$
\mathcal L_\Phi(\rho;\sigma)\geq0.
$$

For composable channels $\Phi$ and $\Psi$, direct cancellation gives the **[EXACT COCYCLE LAW]**

$$
\boxed{
\mathcal L_{\Psi\circ\Phi}(\rho;\sigma)
=
\mathcal L_\Phi(\rho;\sigma)
+
\mathcal L_\Psi(\Phi\rho;\Phi\sigma).}
\tag{D2}
$$

This is a state-pair-indexed additive valuation on channel arrows. It is not a single number attached to $\Phi$, a Noether charge, or a substance stored behind the wall. [[spectral-wall-descent/conditional-expectation-balance|Conditional-expectation balance]] gives a stronger orthogonal Pythagorean identity when the channel is an admissible state-preserving expectation. Equation (D2) applies to arbitrary finite-dimensional channels but supplies no orthogonal decomposition.

[[library/sufficiency-of-channels-over-von-neumann-algebras/inq|Petz sufficiency]] determines the zero set. Let $\Phi^\dagger$ denote the Hilbert--Schmidt adjoint. With inverses taken on supports, the finite-dimensional recovery map associated with $\sigma$ is

$$
\mathcal R_{\sigma,\Phi}(Y)
=
\sigma^{1/2}
\Phi^\dagger\!\left(
(\Phi\sigma)^{-1/2}
Y
(\Phi\sigma)^{-1/2}
\right)
\sigma^{1/2}.
\tag{D3}
$$

It recovers $\sigma$. On $\operatorname{supp}\Phi(\sigma)$ it is trace preserving; if that support is not the entire output space, it can be extended on the orthogonal complement to a CPTP recovery channel. Moreover,

$$
\mathcal L_\Phi(\rho;\sigma)=0
$$

if and only if the pair is recoverable under the standard finite-dimensional hypotheses. Zero residue means sufficiency for the declared state pair; positive residue means failure of exact recovery relative to that channel and pair. Sufficiency for a whole statistical family requires one common recovery channel, not a different reference-dependent recovery chosen pair by pair. Neither statement decides whether the underlying reality is determinate.

## The infinitesimal cocycle is a BKM defect

Let

$$
\rho_t=\sigma+tX+O(t^2),
\qquad
X=X^*,
\qquad
\operatorname{Tr}X=0.
$$

Put $P:=\operatorname{supp}\Phi(\sigma)$. If $P$ is not the output identity, replace the output algebra $\mathcal B$ by the corner $P\mathcal BP$ and regard $\Phi$ as a channel into that corner; in finite dimension, faithfulness of $\sigma$ ensures that all channel outputs lie in this support. For a later channel $\Psi$, make the analogous restriction to $\operatorname{supp}\Psi\Phi(\sigma)$. All output adjoints and BKM inverses below are taken on these declared support algebras. The coincidence expansion is

$$
D(\rho_t\Vert\sigma)
=
\frac{t^2}{2}
g_\sigma^{\mathrm{BKM}}(X,X)
+o(t^2).
$$

Consequently

$$
\boxed{
\ell_\Phi^\sigma[X]
:=
g_\sigma^{\mathrm{BKM}}(X,X)
-
g_{\Phi\sigma}^{\mathrm{BKM}}(\Phi X,\Phi X)
\geq0,}
\tag{D4}
$$

and differentiation of (D2) gives

$$
\boxed{
\ell_{\Psi\circ\Phi}^\sigma[X]
=
\ell_\Phi^\sigma[X]
+
\ell_\Psi^{\Phi\sigma}[\Phi X].}
\tag{D5}
$$

This is the rigorous quadratic meaning of a residue paid across a wall. The form operates on the incoming state tangent $X$. It must not be silently retyped as an output energy.

The defect operator itself can be displayed. Write

$$
\Omega_\sigma(Z)
:=
\int_0^1\sigma^sZ\sigma^{1-s}\,\mathrm ds,
\qquad
g_\sigma^{\mathrm{BKM}}(X,Y)
=
\operatorname{Tr}\!\left[X\Omega_\sigma^{-1}(Y)\right].
\tag{D5a}
$$

The BKM adjoint of the state-tangent map is

$$
\Phi^{\sharp_\sigma}
:=
\Omega_\sigma\circ\Phi^\dagger\circ\Omega_{\Phi\sigma}^{-1},
$$

characterized by

$$
g_\sigma^{\mathrm{BKM}}(X,\Phi^{\sharp_\sigma}Y)
=
g_{\Phi\sigma}^{\mathrm{BKM}}(\Phi X,Y).
$$

Therefore

$$
\boxed{
L_\Phi^\sigma
:=
I-\Phi^{\sharp_\sigma}\Phi
,
\qquad
(L_\Phi^\sigma)^{*_{g_\sigma}}=L_\Phi^\sigma,
\qquad
0\leq_{g_\sigma}L_\Phi^\sigma\leq_{g_\sigma}I,
\qquad
\ell_\Phi^\sigma[X]
=
g_\sigma^{\mathrm{BKM}}(X,L_\Phi^\sigma X).}
\tag{D5b}
$$

For $\Psi$ after $\Phi$, the scalar cocycle (D5) is the quadratic form of the exact operator-valued identity

$$
\boxed{
L_{\Psi\Phi}^{\sigma}
=
L_\Phi^\sigma
+
\Phi^{\sharp_\sigma}
L_\Psi^{\Phi\sigma}
\Phi.}
\tag{D5c}
$$

Here positivity and self-adjointness are with respect to the input BKM tangent metric, not Hilbert--Schmidt Loewner order or complete positivity on the matrix algebra; $\Phi^{\sharp_\sigma}$ need not itself be a channel. This answers the operator question without changing carriers: $L_\Phi^\sigma$ operates on incoming BKM tangents. It is not a spacetime operator, a clock generator, or a mass Casimir.

## Type III lift: the exact loss and the conditional response operator

The density-matrix notation above is not essential to the wall idea. Let

$$
\mathcal N\subseteq\mathcal M
$$

be an inclusion of von Neumann algebras and let \(\varphi,\sigma\) be faithful normal states for which the relevant Araki relative entropies are finite. Define the restriction loss

$$
\boxed{
\mathcal L_{\sigma,\mathcal N}(\varphi)
:=
S_{\mathcal M}(\varphi\Vert\sigma)
-
S_{\mathcal N}(\varphi|_{\mathcal N}\Vert
\sigma|_{\mathcal N})
\geq0.}
\tag{D5d}
$$

This uses no trace and is therefore compatible with Type III local algebras. [[library/sufficient-subalgebras-and-relative-entropy/inq|Petz's theorem]] gives the exact zero semantics under its stated faithful and finite-entropy hypotheses:

$$
\boxed{
\mathcal L_{\sigma,\mathcal N}(\varphi)=0
\quad\Longleftrightarrow\quad
[D\varphi:D\sigma]_t\in\mathcal N
\ \text{for every }t\in\mathbb R,}
\tag{D5e}
$$

equivalently to the corresponding sufficiency/generalized-expectation conditions. The local algebra loses no distinction relevant to the pair exactly when it retains their Connes cocycle. This gives a rigorous meaning to “something is forgotten in descent” without turning forgetting into ontological randomness.

An ordinary \(\sigma\)-preserving conditional expectation exists only under the Takesaki modular-invariance condition. When that condition fails, [[library/conditional-expectations-and-a-theorem-of-takesaki/inq|the Accardi--Cecchini generalized expectation]] still supplies a state-dependent standard-form contraction. Thus the carrier map is available more generally than an idempotent expectation, but its existence alone contributes no stiffness.

Now choose a class of sufficiently regular faithful state curves \(\varphi_s\) through \(\sigma\), with tangent \(\xi=\dot\varphi_0\), on which both second variations exist. Define

$$
q_{\sigma,\mathcal N}[\xi]
:=
\left.
\frac{\mathrm d^2}{\mathrm ds^2}
\mathcal L_{\sigma,\mathcal N}(\varphi_s)
\right|_{s=0}
=
g_{\sigma}^{\mathcal M}(\xi,\xi)
-
g_{\sigma|_{\mathcal N}}^{\mathcal N}
(\xi|_{\mathcal N},\xi|_{\mathcal N})
\geq0.
\tag{D5f}
$$

The form operates on incoming normal-state tangents. Its kernel consists of directions with zero **quadratic** restriction loss. That infinitesimal statement is weaker than exact recoverability of an entire finite curve; equation (D5e) remains the exact state-pair criterion.

If a physical construction provides a Hilbert tangent carrier \(\mathcal T_{\sigma,\mathcal N}\) on which \(q_{\sigma,\mathcal N}\) is densely defined and closed, the representation theorem returns a unique positive self-adjoint operator \(R_{\sigma,\mathcal N}\) satisfying

$$
\boxed{
q_{\sigma,\mathcal N}[\xi]
=
\|R_{\sigma,\mathcal N}^{1/2}\xi\|^2.}
\tag{D5g}
$$

This is an exact implication from the declared analytic hypotheses, not a theorem that every physically desired tangent completion has those properties. At this level one can ask the recognizable lower-frame question

$$
q_{\sigma,\mathcal N}[\xi]
\stackrel{?}{\geq}
\kappa^2
\operatorname{dist}
(\xi,\ker q_{\sigma,\mathcal N})^2.
\tag{D5h}
$$

For a general restriction and reference state, pointwise positivity gives no such uniform \(\kappa>0\). For a state-preserving ordinary expectation, however, (D5h) holds tautologically with \(\kappa=1\) on the incoming BKM quotient. The next theorem shows why that exact estimate is still not a mass-gap form.

## A localized loss has an established energy upper solder

When \(\mathcal M=\mathcal A(B)\) is a local QFT algebra for a region of width \(2R\), the reference is the vacuum restriction, and the state path is implemented by localized unitaries \(e^{isA}\Omega\), Longo's finite-width theorem adds a physical comparison that is absent for a generic inclusion. Under the differentiability and domain hypotheses stated in [[localized-relative-entropy-and-the-energy-solder]], the convention in (D5f), which uses the full second derivative, gives

$$
0\leq
q_{\omega,\mathcal N}[A]
\leq
\frac{4\pi R}{\hbar c}
\langle A\Omega,HA\Omega\rangle.
\tag{D5h.0}
$$

Therefore a noncircular lower bound

$$
q_{\omega,\mathcal N}[A]
\geq
\kappa\|(1-P_0)A\Omega\|^2
$$

on a Hamiltonian form core would imply

$$
\Delta_E
\geq
\frac{\hbar c}{4\pi R}\kappa.
$$

Equivalently, using half-Hessians removes both factors of two. The physical advance is that the right-hand inequality comes from locality and positive-energy translation covariance rather than a freely normalized Markov clock. The remaining obstruction is the left-hand lower frame and the form-core theorem. The preserving-expectation result below explains why one vertical loss cannot supply them on retained neutral directions.

## The preserving-expectation Hessian is vertical

Suppose \(E:\mathcal M\to\mathcal N\) is a faithful normal conditional expectation and the faithful normal reference state obeys \(\sigma\circ E=\sigma\). Let

$$
\operatorname{res}:\mathcal M_*\to\mathcal N_*,
\qquad
\operatorname{res}\rho=\rho|_{\mathcal N},
\qquad
j_E:\mathcal N_*\to\mathcal M_*,
\qquad
j_E\eta=\eta\circ E.
\tag{D5h.1}
$$

Then \(\operatorname{res}j_E=1\). [[library/approximate-recoverability-and-relative-entropy-ii/inq|Faulkner--Hollands]] give, in this specialization, the general-von-Neumann chain rule

$$
\boxed{
S_{\mathcal M}(\rho\Vert\sigma)
-
S_{\mathcal N}(\operatorname{res}\rho\Vert\operatorname{res}\sigma)
=
S_{\mathcal M}(\rho\Vert\rho\circ E).}
\tag{D5h.2}
$$

Every output curve \(\eta_s\) therefore has a recovered lift \(\rho_s=j_E\eta_s\) whose loss vanishes identically. On any common smooth Araki/BKM tangent domain,

$$
P_E:=j_E\operatorname{res}
\tag{D5h.3}
$$

is the BKM-orthogonal projection onto the recovered tangents and

$$
\boxed{
q_{\sigma,\mathcal N}[\xi]
=
\|(1-P_E)\xi\|_{\mathrm{BKM},\sigma}^2
=
\operatorname{dist}_{\mathrm{BKM}}
(\xi,\operatorname{ran}P_E)^2.}
\tag{D5h.4}
$$

Thus the incoming quotient estimate is exact, with sharp constant one, and needs no finite-index hypothesis. But its output transgression is

$$
\boxed{
\tau_{\operatorname{res}}(y)
:=
\inf_{\operatorname{res}\xi=y}q_{\sigma,\mathcal N}[\xi]
=0}
\tag{D5h.5}
$$

for every retained tangent \(y\). The form measures only the **vertical distinction forgotten by this one expectation**. It gives no stiffness to what survives.

Nor can finite index repair this by itself. For the index-\(4\) factor inclusion

$$
M_2\otimes1
\subset
M_2\otimes M_2,
\qquad
E=\operatorname{id}\otimes\tau_2,
\tag{D5h.6}
$$

write \(I_2\) for the identity and \(X,Z\) for the Pauli matrices, and take

$$
\sigma_t
=
\frac{I_2\otimes I_2+tX\otimes X}{4},
\qquad
0<t<1,
\qquad
\xi=\frac{Z\otimes I_2}{4}.
$$

Relative to the upstairs BKM norm of this tangent, the transverse loss ratio is

$$
1-\frac{t}{\operatorname{artanh}t}
=
\frac{t^2}{3}+O(t^4)
\longrightarrow0.
\tag{D5h.7}
$$

Tensoring this example with any \(\sigma\)-finite Type III factor preserves both index and ratio. Hence there is no state-uniform positive Hessian floor depending only on the index. [[gauge-index-no-go-and-four-dimensional-center-square]] gives the gauge-theoretic consequence: index is a capacity or sector-count datum, whereas physical coercivity needs normalized pullbacks and transverse relative position among a family of descents.

## The normalization no-go

The descent structure cannot choose its own physical rate. Suppose a \(\sigma\)-preserving ordinary conditional expectation \(E:\mathcal M\to\mathcal N\) exists, and let \(E_2\) be its orthogonal \(L^2(\mathcal M,\sigma)\) implementation. For every freely chosen \(\gamma>0\),

$$
T_t^{(\gamma)}
:=
E+e^{-\gamma t}(I-E)
=
(1-e^{-\gamma t})E+e^{-\gamma t}I
\tag{D5i}
$$

is a normal unital completely positive \(\sigma\)-preserving semigroup. Its positive \(L^2\) generator is

$$
\boxed{
L_2^{(\gamma)}
=
\gamma(I-E_2),}
\tag{D5j}
$$

whose lower edge on \(L^2(\mathcal N)^\perp\) is exactly \(\gamma\). The same inclusion, expectation, state, kernel, and distinction split therefore admit every positive relaxation gap merely by changing an external number.

This gives the decisive **[EXACT NORMALIZATION NO-GO]**:

$$
\boxed{
\text{descent plus positivity determines a kernel decomposition, not a physical mass scale}.}
\tag{D5k}
$$

For an independently selected KMS-symmetric quantum Markov semigroup on an arbitrary von Neumann algebra, [[library/derivations-and-kms-symmetric-quantum-markov-semigroups/inq|Vernooij and Wirth]] prove the first-order factorization

$$
L_2=\delta^*\delta,
\qquad
\mathcal E(\xi)=\|\delta\xi\|^2.
\tag{D5l}
$$

This supplies the correct operator shape and remains valid without a trace. It starts with the semigroup and does not select it, its rate, or a gap. A physical realization must derive a Yang--Mills-specific \(\delta\), construct a physically normalized pullback from retained Yang--Mills directions into one or several forms like (D5f), prove a regulator-uniform joint frame estimate there, and then compare that same-carrier form with reconstructed energy or the Poincare Casimir. Establishing (D5h) merely on the incoming quotient of one preserving expectation is already automatic and does not meet that obligation.

The causal grain can therefore do only a sharply typed job here. A Fredholm or Q-system transition may select which descent carrier exists; a logarithmic scale character may normalize its dimensionless response; cosmological data may later calibrate or test a dimensional realization. None of those steps permits setting \(\gamma=46.27\,\mathrm{MeV}\) by unit conversion. The grain must determine the normalization through an independent scale/geometry theorem if it is to contribute more than the topology of forgetting.

## The sufficiency--carrier fork

Two exact observations block the most tempting identification.

First, suppose a smooth state family $\rho_\theta$ is exactly recoverable by one channel $\mathcal R$:

$$
\mathcal R\Phi(\rho_\theta)=\rho_\theta.
$$

Data processing through $\Phi$ and then $\mathcal R$ forces equality throughout, so

$$
\ell_\Phi^{\rho_0}[\dot\rho_0]=0.
\tag{D6}
$$

Thus the relative-entropy residue cannot positively charge a tangent whose entire statistical model is exactly sufficient through the wall.

Second, if

$$
\Phi X=0,
$$

then

$$
\ell_\Phi^\sigma[X]
=
g_\sigma^{\mathrm{BKM}}(X,X),
$$

but the output tangent is zero. This is real lost distinction on the input carrier, not a mass form on an observable excitation.

Hence the **[EXACT RECOVERY FORK]** is

$$
\boxed{
\begin{array}{ccl}
\text{recoverable direction}&\Longrightarrow&\text{zero residue},\\[2mm]
\text{erased direction}&\Longrightarrow&\text{positive upstream residue but zero output}.
\end{array}}
\tag{D7}
$$

This sharpens the range--kernel no-go in [[causal-patch-boundary-and-two-times]]. If a wall is to contribute to a mass-gap form, it needs a further construction that acts on retained physical directions.

## Minimal-lift transgression puts a form on the output

Let $(V,g_V)$ and $(W,g_W)$ be finite-dimensional real inner-product spaces, and let

$$
A:V\longrightarrow W
$$

be a surjective contraction:

$$
g_W(Ax,Ax)\leq g_V(x,x).
$$

For a channel derivative, take $V$ to be the input BKM tangent space and restrict $W$ to the reachable output tangent $\operatorname{im}A$. Define the minimal-lift metric

$$
\boxed{
g_A^\uparrow(y,y)
:=
\inf_{Ax=y}g_V(x,x).}
\tag{D8}
$$

Contraction implies

$$
g_A^\uparrow(y,y)\geq g_W(y,y).
$$

The **output transgression** is therefore

$$
\boxed{
\tau_A(y)
:=
g_A^\uparrow(y,y)-g_W(y,y)
=
\inf_{Ax=y}\ell_A[x]
\geq0,}
\tag{D9}
$$

where $\ell_A[x]:=g_V(x,x)-g_W(Ax,Ax)$. Unlike $\ell_A$, the form $\tau_A$ operates on retained output tangents. It is the least upstream distinction lost among all realizations of the same output change, not the total information forgotten by the fiber. For the derivative of a preserving expectation with its adapted BKM metrics, the recovery section is isometric and (D5h.5) gives \(\tau_A\equiv0\). Positive output transgression therefore requires a non-adapted metric comparison or a jointly transverse family; it is not generated by forgetfulness alone.

Indeed, let

$$
V=(\ker A)^{\perp_{g_V}}\oplus\ker A
$$

and let $s_A:W\to(\ker A)^{\perp_{g_V}}$ be the unique minimum-norm lift. Every $x\in V$ decomposes as

$$
x=s_A(Ax)+k,
\qquad
k\in\ker A,
$$

and Pythagoras gives the sharper **[EXACT CARRIER SPLIT]**

$$
\boxed{
\ell_A[x]
=
\tau_A(Ax)
+g_V(k,k).}
\tag{D9a}
$$

The first term is the minimum-output shadow of metric contraction. The second is inaccessible vertical residue and remains entirely on the incoming carrier.

In coordinates, let $G_V$ and $G_W$ be the positive metric matrices and let $A$ have full row rank. Lagrange minimization gives

$$
\boxed{
g_A^\uparrow(y,y)
=
y^{\mathsf T}
\left(AG_V^{-1}A^{\mathsf T}\right)^{-1}
y,}
\tag{D10}
$$

so

$$
\tau_A(y)
=
y^{\mathsf T}
\left[
\left(AG_V^{-1}A^{\mathsf T}\right)^{-1}
-G_W
\right]y.
\tag{D11}
$$

The bracket is positive semidefinite. Relative to $g_W$, it defines a positive semidefinite self-adjoint operator

$$
T_A
=
G_W^{-1}
\left[
\left(AG_V^{-1}A^{\mathsf T}\right)^{-1}
-G_W
\right].
\tag{D12}
$$

For another surjective contraction $B:W\to Z$, minimization by the intermediate value yields the exact dynamic-programming law

$$
g_{BA}^\uparrow(z,z)
=
\inf_{By=z}g_A^\uparrow(y,y),
\tag{D13}
$$

and hence

$$
\boxed{
\tau_{BA}(z)
=
\inf_{By=z}
\left\{
\tau_A(y)
+g_W(y,y)-g_Z(z,z)
\right\}.}
\tag{D14}
$$

The incoming defects add exactly along a chosen lift by (D5); their output transgressions compose by infimizing over the forgotten intermediate carrier. In general $\tau_{BA}$ is not $\tau_A+\tau_B$. This infimal law, rather than ordinary addition, is the appropriate noninvertible analogue of path-cost composition.

In the BKM application both metrics are dimensionless, so $T_A$ is dimensionless. For arbitrary abstract inner-product spaces that typing is not automatic. The construction is canonical only relative to the supplied channel and two supplied metrics. It does not choose them, fix their normalization, or turn $T_A$ into a Hamiltonian. Two counterexamples fix its interpretation:

- for the Euclidean projection $A(x_1,x_2)=x_1$, the entire $x_2$ fiber is forgotten while $\tau_A=0$; all loss is the vertical term in (D9a);
- for the binary channel below with $\lambda\ne0$, the tangent map is invertible and has no nontrivial fiber, yet $\tau_\lambda>0$ because its inverse is not a stochastic contraction.

Thus $\tau_A$ measures minimum metric distortion of retained directions. It is not fiber multiplicity, branch count, or all forgotten distinction.

## Binary channel witness

Let

$$
p_t=\left(\frac12+t,\frac12-t\right)
$$

and let a binary symmetric channel have contraction parameter

$$
0<\lambda\leq1,
\qquad
t\longmapsto\lambda t.
$$

At $t=0$ the Fisher/BKM tangent metric is

$$
g(t,t)=4t^2.
$$

Equations (D4) and (D9) become

$$
\ell_\lambda(t)
=
4(1-\lambda^2)t^2,
\tag{D15}
$$

$$
g_\lambda^\uparrow(s,s)
=
\frac{4s^2}{\lambda^2},
\qquad
\boxed{
\tau_\lambda(s)
=
4s^2(\lambda^{-2}-1).}
\tag{D16}
$$

For two channels,

$$
\ell_{\lambda_2\lambda_1}(t)
=
\ell_{\lambda_1}(t)
+
\ell_{\lambda_2}(\lambda_1t).
\tag{D17}
$$

[[contemporary-puzzles/yang-mills-mass-gap/receipts/descent_loss_cocycle_receipt.py|The descent-loss receipt]] checks the carrier split, weighted quotient metric, general two-arrow infimal composition, and binary identities (D15)--(D17) numerically. The positive coefficient is a dimensionless contraction cost. No energy or time parameter occurs.

## Local invertibility still does not give global coercivity

The Jacobian counterexamples supply the complementary warning. A polynomial map can have an invertible differential at every point and still be globally many-to-one and nonproper. Pulling back a positive target metric then produces a pointwise positive source metric, but this does not give a global inverse, a uniform least singular value, compact resolvent, or a Poincare constant.

That distinction is exactly the one the mass-gap programme needs:

$$
\boxed{
\text{pointwise nondegenerate Hessian or Jacobian}
\not\Longrightarrow
\text{global spectral coercivity}.}
\tag{D18}
$$

[[sufficient-reason/noninvertible-presentation-and-apparent-chance|Noninvertible presentation and apparent chance]] gives the deterministic reading and the groupoid/torsor firewall. Here its analytic lesson is that the stopping condition must control the full carrier and its behavior at infinity, not merely every local chart.

## QFT compatibility belongs after the nonfaithful quotient

A genuinely forgetful realization cannot itself be an equivalence. To avoid an untyped quotient, first use the algebraic-net version. For every declared Euclidean region $O$, let

$$
q_{r,O}:\mathcal A^{\mathrm{pre}}_{r,G}(O)
\longrightarrow
\mathcal Q_{r,G}(O)
$$

be a surjective $*$-homomorphism with closed two-sided $*$-ideal $I_r(O):=\ker q_{r,O}$. Require these ideals to respect the regional inclusions, so that $q_r$ is a natural quotient map and

$$
\mathcal Q_{r,G}(O)
\cong
\mathcal A^{\mathrm{pre}}_{r,G}(O)/I_r(O).
$$

Let $\mathcal R_r$ be a declared state-preserving Euclidean-net morphism or localization/reconstruction functor into a reflection-positive Euclidean data package. The **[CONDITIONAL ARCHITECTURE]** is then

$$
\boxed{
(\mathcal A^{\mathrm{pre}}_{r,G}(-),F_t^r)
\xrightarrow[\mathrm{nonfaithful}]{q_r}
\mathcal Q_{r,G}(-)
\xrightarrow{\mathcal R_r}
\mathfrak B^{\mathrm E}_{r,G}
\xrightarrow[\text{directed regulator limit}]
{\text{Mosco plus Euclidean state/correlation convergence}}
\mathfrak B^{\mathrm E}_G
\xrightarrow{\mathrm{OS}}
\mathfrak A_G^{\mathrm{YM}}.}
\tag{D19}
$$

Here $r$ denotes the directed regulator data, including $a\to0$ and $L\to\infty$ when a lattice is used. The symbols $\mathfrak B^{\mathrm E}_{r,G}$ and $\mathfrak B^{\mathrm E}_G$ denote full Euclidean state/correlation/form packages, not bare $C^*$-algebras. Mosco convergence governs their forms and operators on changing Hilbert spaces; convergence of the Euclidean states or Schwinger functions is additional; OS reconstruction applies only after the OS axioms hold and is the later passage to the Lorentzian physical carrier. Thus (D19) is a typed construction target, not one theorem supplied by the quotient. At finite lattice regulator $\mathfrak B^{\mathrm E}_{r,G}$ has only the declared lattice symmetries and reflection structure. Continuous Poincare covariance is a continuum reconstruction target, not a finite-lattice property.

Only the effective image $\mathcal Q_{r,G}(-)$, after carrier reconstruction, is required to recover the Yang--Mills net. The full pre-observable net is not. If $F_t^r(I_r(O))\subseteq I_r(O)$ compatibly for every region, the deterministic preflow descends to the quotient net. If the primitive object is instead a category and $q_r$ is a functor, then $\mathcal Q_{r,G}$ must be defined as the coequalizer of a declared object-and-arrow kernel-pair congruence, when that coequalizer exists; the bare notation $\mathcal C/\ker q$ is not sufficient.

The continuum target must be a pointed Poincare-covariant net, including its inclusions, vacuum state, translation representation, energy form, spectrum condition, and renormalized scale. Recovering one Type-III factor is not enough. An exact state- and Poincare-covariance-preserving natural isomorphism with $\mathfrak A_G^{\mathrm{YM}}$ induces a GNS unitary intertwining translations, and therefore preserves the Poincare Casimir and the mass gap.

The BKM wall is a separate typed datum. Let $\Phi_r$ be a state channel with faithful reference state $\sigma_r$, and set

$$
A_r:=(\mathrm d\Phi_r)_{\sigma_r}.
$$

No formal identity equates the algebraic quotient $q_r$ with the tangent contraction $A_r$. A realization theorem must show that $\Phi_r$ implements the declared accessible quotient and that its reachable BKM tangents belong to the reconstructed physical package.

Approximate low-energy compatibility is weaker. It should compare the full net on energy-bounded states or smeared observables with explicit regulator, volume, heavy-sector, and background errors; a sharp spectral subspace should not be misnamed a local subalgebra. [[causal-frame-coercivity#Recovery of observed QFT below a UV threshold|The compatibility ledger]] states the exact extension, effective-recovery, and strong-emergence contracts separately.

This factorization resolves an apparent contradiction in (D7). The wall may forget distinctions that do not survive into $\mathcal Q_{r,G}$ while the reconstructed effective image exactly realizes QFT. Petz recovery of the *full source* is neither required nor desired. What must be recovered is the observable net from the effective quotient. Conversely, if a proposed positive residue is evaluated on a family claimed to be Petz-recoverable through the same wall, it vanishes and cannot explain a gap.

## Why the solder must target the joint invariant

One causal translation generator is the wrong place to demand the gap. The clean two-direction witness is exact in $1+1$ dimensions, or on a declared zero-transverse-momentum sector of a higher-dimensional representation. If a nonzero positive generator $P_+$ obeys exact same-carrier scaling

$$
U_sP_+U_s^*=e^sP_+,
$$

then its spectrum is forced down to zero. A complementary strongly commuting generator can scale oppositely,

$$
U_sP_-U_s^*=e^{-s}P_-,
$$

so the product $P_+P_-$ is invariant under this reciprocal one-parameter action even though each marginal spectrum is $[0,\infty)$. In natural units define

$$
H=\frac{P_++P_-}{2},
\qquad
M^2=P_+P_-.
$$

Joint functional calculus and the arithmetic--geometric mean give $H\geq M$. Hence

$$
M^2\geq m_*^2(1-P_0)
\quad\Longrightarrow\quad
H\geq m_*(1-P_0).
\tag{D19a}
$$

[[joint-causal-generators-and-the-mass-casimir|The joint-causal-generator theorem]] proves this exact reversal and gives a massive rapidity-space witness in which both null generators are gapless while their product is fixed. The quotient transgression must therefore be compared with the joint Casimir of a completed translation representation, not with one modular logarithm or one null generator. The “gapless causal directions, gapped mass” pattern is not an evasion of the mass-gap problem; it identifies the invariant on which its coercivity theorem belongs.

In $3+1$ dimensions, $P_\pm=H\pm cP_z$ give $P_+P_-=H^2-c^2P_z^2=\mathcal C+c^2\mathbf P_\perp^2$, not the full mass Casimir. This forbids identifying the directional product itself with mass. It does **not** make a full-carrier directional floor insufficient: after positive-energy Poincare reconstruction, a lower bound for one fixed physical null-pair product on the entire vacuum complement gives the Hamiltonian gap by the arithmetic--geometric mean, and Lorentz-orbit covariance then gives the full Casimir floor. An abstract distinction product still requires a noncircular same-carrier solder to that physical pair, to an all-direction family, or directly to $\mathcal C$.

## The paired-wall operator signature

The same reversal can be stated one level before energy. Suppose two complementary wall constructions yield quotient-transgression forms that have been pulled back to one common physical vacuum-tangent carrier. Assume their closed forms are represented there by strongly commuting positive self-adjoint **dimensionless** operators $K_+$ and $K_-$, each annihilating the vacuum. Their product is then the positive self-adjoint operator defined by joint spectral calculus. Only after this common-carrier theorem does $K_+K_-$ have a meaning.

If a scale or boost action satisfies

$$
U_sK_+U_s^*=e^sK_+,
\qquad
U_sK_-U_s^*=e^{-s}K_-,
\tag{D19b}
$$

then either directional operator may have spectrum down to zero, while

$$
U_s(K_+K_-)U_s^*=K_+K_-.
$$

Let $P_0$ reduce $H$, the full Poincare Casimir $\mathcal C$, and $K_+K_-$. On the common form domain

$$
\mathcal D_{\leftrightarrow}
:=
\operatorname{Dom}\!\left((K_+K_-)^{1/2}\right)
\cap
\operatorname{Dom}(\mathcal C^{1/2}),
$$

assume the **paired completeness** estimate

$$
\left\|(K_+K_-)^{1/2}\Psi\right\|^2
\geq
\kappa_{\leftrightarrow}^2
\left\|(1-P_0)\Psi\right\|^2
\tag{D19c}
$$

and a separately normalized same-carrier Casimir solder

$$
\left\|\mathcal C^{1/2}\Psi\right\|^2
\geq
\eta_{\leftrightarrow}E_*^2
\left\|(K_+K_-)^{1/2}\Psi\right\|^2.
\tag{D19d}
$$

for every $\Psi\in\mathcal D_{\leftrightarrow}$, with $\kappa_{\leftrightarrow},\eta_{\leftrightarrow},E_*>0$. If this domain is a form core for $\mathcal C$, positivity of the translation spectrum gives the **[CONDITIONAL EXACT IMPLICATION]**

$$
H
\geq
E_*\sqrt{\eta_{\leftrightarrow}}\,
\kappa_{\leftrightarrow}(1-P_0).
\tag{D19e}
$$

This is the most literal current formulation of the upside-down proposal. The directional $K_\pm$ operate on physical distinction tangents, not on spacetime; $P_\pm$ operate on the physical Hilbert space as translation generators; and $\mathcal C$ is their joint Poincare invariant. Invariance of $K_+K_-$ under (D19b) alone does not make it a full Poincare scalar. Equations (D19c) and (D19d) do not identify these layers. They state the two missing theorems: complementary walls must leave no jointly soft nonvacuum direction, and their invariant distinction product must be controlled by the physical mass Casimir without using the desired spectrum to normalize it.

## The conditional Casimir stopping theorem on reconstructed members

In this subsection, $r$ ranges only over Lorentzian members for which a positive-energy Poincare representation has actually been reconstructed; it does not range over arbitrary finite lattice regulators from (D19). Let $\mathcal H_r$ be such a reconstructed physical carrier, with vacuum projection $P_{0,r}$ reducing the translation generators and with positive Poincare Casimir operator

$$
\mathcal C_r=H_r^2-c^2\mathbf P_r^2.
$$

Its closed quadratic form is

$$
\mathfrak c_r[\Psi]
:=
\left\|\mathcal C_r^{1/2}\Psi\right\|^2,
\qquad
\Psi\in\mathcal D_r:=\operatorname{Dom}(\mathcal C_r^{1/2}).
$$

Assume $P_{0,r}\mathcal D_r\subseteq\mathcal D_r$. The finite-dimensional construction (D8)--(D14) is not silently imported. Instead declare real BKM tangent Hilbert spaces $V_r,W_r$ and a bounded contraction

$$
A_r:V_r\longrightarrow W_r
$$

with closed reachable range \(W_r^{\mathrm{reach}}:=\operatorname{Ran}A_r\). The quotient/minimum-lift norm is then

$$
g_{A_r}^{\uparrow}(y,y)
:=
\inf_{A_rx=y}\|x\|_{V_r}^2,
\qquad
y\in W_r^{\mathrm{reach}},
$$

and the closed-range theorem gives a unique minimum lift in $(\ker A_r)^\perp$. Require

$$
\tau_{A_r}(y)
:=
g_{A_r}^{\uparrow}(y,y)-\|y\|_{W_r}^2
$$

to be the resulting nonnegative closed quadratic form on the reachable output carrier, and extend it to the complexification by Hermitian polarization. If $A_r$ is unbounded or its range is not closed, these conclusions are not automatic: one must instead construct the quotient completion, prove that the output metric extends there, and prove closability of the difference form before proceeding.

Let a complex-linear map $\mathcal J_r$ send $\mathcal D_r$ into the form domain of that complexified retained-output form, with $\mathcal J_rP_{0,r}=0$. Such a map is a substantive carrier bridge: BKM tangents are density perturbations, not Hilbert excitations by definition. By (D5h.5), \(A_r\) cannot here be merely one preserving expectation equipped with its adapted BKM metrics, because then \(\tau_{A_r}=0\). A live realization must use a non-adapted comparison or replace \(\tau_{A_r}\) by a jointly transverse sum of independently normalized closed channel forms. Assume the pullback below is closable and define

$$
\mathfrak t_r[\Psi]
:=
\tau_{A_r}(\mathcal J_r\Psi).
\tag{D20}
$$

Assume, without using the desired spectrum to define any term, that for every $\Psi\in\mathcal D_r$,

$$
\mathfrak t_r[\Psi]
\geq
\kappa_r
\lVert(1-P_{0,r})\Psi\rVert^2
\tag{D21}
$$

and

$$
\mathfrak c_r[\Psi]
\geq
\eta_rE_{*,r}^2
\mathfrak t_r[\Psi].
\tag{D22}
$$

where $\kappa_r,\eta_r,E_{*,r}>0$. Because the estimates hold on the full Casimir form domain, the joint-Casimir theorem gives the **[CONDITIONAL EXACT IMPLICATION]**

$$
\boxed{
\Delta_{E,r}
\geq
E_{*,r}\sqrt{\eta_r\kappa_r}.}
\tag{D23}
$$

The factors have distinct meanings:

| Factor | Type or carrier | Required origin |
|---|---|---|
| $\tau_{A_r}$ | retained output tangents | non-adapted minimum BKM contraction loss, or a jointly transverse sum; one adapted preserving expectation gives zero |
| pulled-back form $\mathfrak t_r$ | physical vacuum-complement | uniform coercivity, possibly certified by a separately typed closed-range theorem |
| $\kappa_r$ | scalar | dimensionless lower-frame constant for $\mathfrak t_r$ |
| $\eta_r$ | scalar | dimensionless comparison with the reconstructed Poincare Casimir |
| $E_{*,r}$ | unit line | independent RG or cross-sector scale calibration |

For a continuum theorem, the product must retain a positive lower limit under changing-carrier form convergence, the vacuum projections must converge, and the effective nets must satisfy OS or direct positive-energy reconstruction. A mixing gap of the channel, a local Hessian, or a finite-regulator singular value is not a substitute.

At a finite lattice regulator, where continuous Poincare covariance and \(\mathcal C_r\) are unavailable, the legitimate stopping theorem uses the centered lattice Hamiltonian form

$$
\mathfrak h_r[\Psi]
:=
\left\|(H_r-E_{0,r})^{1/2}\Psi\right\|^2,
\qquad
\Psi\in\operatorname{Dom}\!\left((H_r-E_{0,r})^{1/2}\right).
$$

If on its form domain

$$
\mathfrak t_r[\Psi]
\geq
\kappa_r\|(1-P_{0,r})\Psi\|^2,
\qquad
\mathfrak h_r[\Psi]
\geq
\eta_rE_{*,r}\mathfrak t_r[\Psi],
$$

then the regulated Hamiltonian gap obeys

$$
\Delta_{H,r}
\geq
\eta_rE_{*,r}\kappa_r.
\tag{D23a}
$$

This is a finite-regulator spectral statement, not yet a mass-Casimir theorem. Uniform transport through regulator removal and Poincare reconstruction is still required before (D23) can be invoked.

## The concrete Yang--Mills research question

The new construction does not solve the crossover. It makes the missing object more precise:

1. construct a gauge-invariant scale-indexed source carrier and deterministic or algebraic preflow;
2. construct the accessible algebraic quotient $q_r$, a compatible state channel $\Phi_r$, its reference state and BKM metrics, and the derivative $A_r=(\mathrm d\Phi_r)_{\sigma_r}$ without spectral input;
3. prove that a physically normalized non-adapted or jointly transverse pulled-back form is uniformly coercive, or has the required uniform closed range, on the reconstructed nonvacuum tangent;
4. prove a same-carrier Casimir solder and calibrate $E_{*,r}$ from the renormalization trajectory rather than the observed glueball mass;
5. show that ultraviolet block descent enters an infrared coercive basin and transports its physical bound across all remaining scales with controlled loss; and
6. prove that the resulting effective quotient recovers the local Yang--Mills net, state, covariance, and clock dynamics.

This is the precise sense in which “the cause is there but cannot be worked backward toward” may contribute to the mass-gap problem. A declared channel makes an exact incoming distinction residue; noninvertibility can place part of it in inaccessible vertical fibers. The vertical residue alone is not mass. Only a separately nonzero, physically normalized joint form on retained directions, after carrier reconstruction and energy soldering, could enter a mass-gap theorem.
