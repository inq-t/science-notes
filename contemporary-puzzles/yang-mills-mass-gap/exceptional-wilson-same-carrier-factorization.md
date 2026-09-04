# Exceptional Wilson Same-Carrier Factorization

The exceptional color construction does not require a linear map from its finite normal representation into the Yang--Mills wavefunction space. On the holonomy branch, the normal representation is a probe: its Hilbert--Schmidt response becomes a scalar plaquette function and its trace form becomes a metric on the link group. Both then act on the ordinary gauge-invariant configuration carrier. The resulting finite-regulator Hamiltonian is exactly a reparameterized Wilson--Kogut--Susskind Hamiltonian; the trace-metric factor \(8\) and character factor \(288\) are absorbed by the electric and magnetic coefficients. What remains is not a representation-carrier mismatch but the interacting-vacuum Poincare estimate, its regulator-uniform physical normalization, and continuum reconstruction.

**Status: [EXACT] for the finite-graph carrier factorization, coefficient conversion, ground-state-form scaling, and normalization-free relative-coercivity quotient; [EXACT CONDITIONAL] for the OS identification under the stated reflection and transfer hypotheses; [OPEN] for selection of the color member and couplings, construction and uniform control of the interacting vacuum, continuum OS/Poincare reconstruction, and a dimensional yardstick.**

## Two uses of the exceptional normal must be separated

The 149-dimensional real representation \(N_{\mathrm{def}}\) in
[[exceptional-normal-holonomy-and-the-residual-gauge-form]] enters two
different proposals.

The **normal-Hessian route** tries to use a positive form on deformations of
the exceptional flag itself. That form acts on a finite normal space. To
compare it with physical Yang--Mills excitations, one really does need a
field-valued analysis map from the physical vacuum complement into a bundle
of such response spaces, together with lower coverage and an energy-form
solder.

The **holonomy route** does something else. A link comparison acts on the
normal fibre, but the fibre response is immediately contracted to the class
function

\[
Q_N(U)
=
\sum_p\left\|\sigma_N(U_p)-I\right\|_{\mathrm{HS}}^2.
\tag{EW1}
\]

The corresponding trace form

\[
b_N(X,Y)
=
\operatorname{Tr}_{N_{\mathrm{def}}}
\bigl(\mathrm d\sigma_N(X)^*\mathrm d\sigma_N(Y)\bigr)
\tag{EW2}
\]

is an invariant metric on the link group. After these two contractions, the
operators of interest act on functions of link configurations, not on
\(N_{\mathrm{def}}\).

This is the decisive type correction. The normal is a **response probe** in
the holonomy construction, not the physical state carrier.

## The graph carrier is already the Wilson carrier

The quotient-stack equivalence

\[
[S^6/G_2]\simeq\mathbf B SU(3)
\tag{EW3}
\]

and free-path transgression in
[[octonionic-slice-groupoid-and-orientation-torsor]] give, for a finite
oriented graph \(\Gamma\), taken below as the one-skeleton of a finite
two-complex,

\[
\operatorname{Fun}(\mathcal P_\Gamma,G_2\ltimes S^6)
\simeq
SU(3)^{E(\Gamma)}\mathbin{/\mkern-6mu/}SU(3)^{V(\Gamma)}.
\tag{EW4}
\]

Thus the exceptional presentation data and ordinary color link variables are
two presentations of the same finite connection groupoid. The stack
equivalence by itself transports no measure. After moving to the
\(SU(3)^E\)-presentation and separately choosing normalized product Haar
measure, the construction lands on the standard gauge-invariant Hilbert
carrier

\[
\mathcal H_\Gamma
:=
L^2\!\left(SU(3)^{E(\Gamma)},\mu_{\mathrm H}^{E(\Gamma)}\right)^{SU(3)^{V(\Gamma)}}.
\tag{EW5}
\]

The transporter convention in (EW4) writes
\(U_e\mapsto k_{t(e)}^{-1}U_ek_{s(e)}\), whereas another common convention
writes \(U_e\mapsto g_{s(e)}U_eg_{t(e)}^{-1}\). Edgewise inversion, reversal
of the path-composition convention, and \(g_v=k_v^{-1}\) identify them.
Inversion preserves Haar measure and the bi-invariant Casimir, and sends a
plaquette holonomy to its inverse, leaving
\(\operatorname{Re}\operatorname{tr}_{\mathbf3}U_p\) unchanged.

The word *same* is literal here. No injection
\(N_{\mathrm{def}}\to\mathcal H_\Gamma\) is part of the construction.

## Exact coefficient-conversion theorem

Put

\[
K:=-B_{\mathfrak{su}(3)}.
\tag{EW6}
\]

On the structurally distinguished color subgroup, the exceptional normal
calculation gives the two exact identities

\[
\boxed{
b_N=8K,
\qquad
Q_N=288Q_W,}
\tag{EW7}
\]

where

\[
Q_W(U)
=
\sum_p\left(1-\frac13\operatorname{Re}\operatorname{tr}_{\mathbf3}U_p\right).
\tag{EW8}
\]

Let \(\Delta_{\Gamma,b}\) be the positive link Laplacian defined using the
inverse metric \(b^{-1}\), restricted to the gauge-invariant smooth core, and
let \(M_Q\) denote multiplication by \(Q\). Define

\[
\begin{aligned}
H_N(\kappa_N,\lambda_N)
&:=
\kappa_N\Delta_{\Gamma,b_N}+\lambda_NM_{Q_N},\\
H_W(\kappa_W,\lambda_W)
&:=
\kappa_W\Delta_{\Gamma,K}+\lambda_WM_{Q_W}.
\end{aligned}
\tag{EW9}
\]

**Finite-regulator same-carrier theorem.** On the common carrier
\(\mathcal H_\Gamma\),

\[
\boxed{
H_N(\kappa_N,\lambda_N)
=
H_W\!\left(\frac{\kappa_N}{8},288\lambda_N\right).}
\tag{EW10}
\]

In particular,

\[
\kappa_N=8\kappa_W,
\qquad
\lambda_N=\frac{\lambda_W}{288}
\tag{EW11}
\]

makes the two Hamiltonians identical, not merely isospectral or members of a
common universality class.

**Proof.** Since the Laplacian contracts two derivatives with the inverse
metric, \(b_N=8K\) gives

\[
\Delta_{\Gamma,b_N}
=
\frac18\Delta_{\Gamma,K}.
\tag{EW12}
\]

The second identity in (EW7) gives

\[
M_{Q_N}=288M_{Q_W}.
\tag{EW13}
\]

Substitution proves (EW10) on the common smooth core. Compactness of the
finite link group gives essential self-adjointness of the invariant
Laplacian, while the plaquette functions are bounded. The equality therefore
passes to the self-adjoint closures and to their gauge-invariant
restrictions. \(\square\)

The factors \(8\) and \(288\) are exact geometric normalization data. They
are not independent spectral enhancements. Unless an upstream theory fixes
the dimensional coefficients against an independently normalized clock,
they are removed by the coordinate conversion (EW10).

## The plaquette multiplier cannot be the gap operator

The exact Wilson recovery also closes a tempting but incorrect shortcut.
The nonnegative continuous function \(Q_N\) vanishes at every flat
configuration. Hence every sublevel set

\[
\mathcal U_\varepsilon
:=
\{U:Q_N(U)<\varepsilon\}
\tag{EW13a}
\]

contains an open neighborhood of the flat locus and has positive Haar
measure. On a graph with at least one physical cycle, the gauge-invariant
\(L^2\)-space supported in \(\mathcal U_\varepsilon\) is
infinite-dimensional. For any declared unit vector
\(\Omega\in\mathcal H_\Gamma\), one may therefore choose a unit
gauge-invariant \(f_\varepsilon\perp\Omega\) supported in that sublevel set.
Then

\[
\left\langle
f_\varepsilon,M_{Q_N}f_\varepsilon
\right\rangle
<\varepsilon.
\tag{EW13b}
\]

Consequently

\[
\boxed{
\inf_{\substack{
f\perp\Omega\\
\|f\|=1
}}
\langle f,M_{Q_N}f\rangle
=0.}
\tag{EW13c}
\]

Thus the exceptional plaquette response is a potential on configuration
space, but multiplication by that potential has no positive
vacuum-complement floor. The gap can arise only from the complete operator,
in which the electric form and the interacting vacuum couple configuration
directions. A finite normal Hessian or a positive curvature penalty cannot
replace that joint analysis.

## The ground-state transform preserves the cancellation

Assume the matched operator has a unique strictly positive normalized ground
state \(\psi_{0,\Gamma}\), with ground energy \(E_{0,\Gamma}\), and set

\[
\mathrm d\nu_\Gamma
=
\psi_{0,\Gamma}^2\,\mathrm d\mu_{\mathrm H}^{E(\Gamma)}.
\tag{EW14}
\]

For an invariant metric \(b\), define the vacuum-weighted electric form

\[
\mathcal E_{b,\nu_\Gamma}(f)
:=
\sum_e
\int
b^{-1}(\mathrm d_ef,\mathrm d_e\bar f)
\,\mathrm d\nu_\Gamma.
\tag{EW15}
\]

Then

\[
\mathcal E_{b_N,\nu_\Gamma}
=
\frac18\mathcal E_{K,\nu_\Gamma}.
\tag{EW16}
\]

Writing \(\lambda_{\mathrm P}^{\mathrm{GI}}(\nu;b)\) for the optimal
Poincare constant on the mean-zero gauge-invariant carrier, one obtains

\[
\lambda_{\mathrm P}^{\mathrm{GI}}(\nu_\Gamma;b_N)
=
\frac18
\lambda_{\mathrm P}^{\mathrm{GI}}(\nu_\Gamma;K).
\tag{EW17}
\]

The ground-state-transform theorem in
[[gauge-descent-flux-fisher-coercivity]] therefore gives the same physical
gap in either convention:

\[
\boxed{
\Delta_\Gamma
=
\kappa_N\lambda_{\mathrm P}^{\mathrm{GI}}(\nu_\Gamma;b_N)
=
\kappa_W\lambda_{\mathrm P}^{\mathrm{GI}}(\nu_\Gamma;K).}
\tag{EW18}
\]

The trace-metric eight lowers the dimensionless Poincare constant by eight
and raises the matched kinetic coefficient by eight. It cancels exactly in
the energy product.

## A normalization-free location of the unknown

For a connected graph containing a cycle, the exact Haar constants are

\[
\lambda_{\mathrm P}^{\mathrm{GI}}(\mu_{\mathrm H};K)
=
\frac{4g(\Gamma)}9,
\qquad
\lambda_{\mathrm P}^{\mathrm{GI}}(\mu_{\mathrm H};b_N)
=
\frac{g(\Gamma)}{18}.
\tag{EW19}
\]

This makes it useful to isolate the dimensionless **relative vacuum
coercivity**

\[
\boxed{
\Theta_\Gamma
:=
\frac{
\lambda_{\mathrm P}^{\mathrm{GI}}(\nu_\Gamma;b_N)
}{g(\Gamma)/18}
=
\frac{
\lambda_{\mathrm P}^{\mathrm{GI}}(\nu_\Gamma;K)
}{4g(\Gamma)/9}.}
\tag{EW20}
\]

This quotient is invariant under a common rescaling of the link metric.
It satisfies \(\Theta_\Gamma=1\) for product Haar measure. It is positive at a
fixed regular elliptic finite regulator, but need not be at most one and need
not have a positive volume- or continuum-uniform lower bound.

Equation (EW18) becomes

\[
\boxed{
\Delta_\Gamma
=
\kappa_N\frac{g(\Gamma)}{18}\Theta_\Gamma
=
\kappa_W\frac{4g(\Gamma)}9\Theta_\Gamma.}
\tag{EW21}
\]

If \(W_\Gamma=-2\log\psi_{0,\Gamma}\), the elementary global
density comparison gives the exact but generally volume-poor estimate

\[
\Theta_\Gamma
\geq
e^{-\operatorname{osc}W_\Gamma}.
\tag{EW21a}
\]

In the normal metric convention, a uniform conditional Poincare constant
\(\lambda_{\mathrm{loc},\Gamma}^{(N)}\) and a Wasserstein--Dobrushin
influence matrix \(C_\Gamma\) with spectral radius below one instead give

\[
\Theta_\Gamma
\geq
\frac{
\lambda_{\mathrm{loc},\Gamma}^{(N)}
\bigl[1-r_{\mathrm{sp}}(C_\Gamma)\bigr]
}{
g(\Gamma)/18
}.
\tag{EW21b}
\]

Both are consequences of already stated comparison theorems. The first
normally decays exponentially with volume; the second becomes useful only
after its conditional laws and constants are derived from the physical
vacuum rather than from a presumed gap or clustering length.

This is the sharp finite-regulator separation:

- \(g(\Gamma)\) is incidence data;
- \(4/9\), or equivalently \(1/18\), is compact-group geometry in a declared
  metric convention;
- \(\Theta_\Gamma\) is the distortion of kinematic coercivity by the
  interacting vacuum;
- \(\kappa_W\), or equivalently \(\kappa_N\), is the dimensional clock-energy
  coefficient; and
- only their product is the Hamiltonian gap.

The local conditional-Poincare and Dobrushin theorem supplies one sufficient
route to a lower estimate for \(\Theta_\Gamma\). It does not construct the
vacuum specification or prove that the estimate survives the continuum
trajectory.

## Euclidean Wilson recovery uses the same factorization

The exact color character identity also gives

\[
\frac\beta2Q_N
=
\beta_WQ_W,
\qquad
\beta_W=144\beta.
\tag{EW22}
\]

With the same product Haar reference measure, the finite Euclidean Gibbs
measures are therefore identical. Using the same reflection and transfer
normalizations, their OS pre-Hilbert forms, null spaces, completed carriers,
and transfer operators agree. Under the reflection-Markov and vacuum
preparation hypotheses in
[[vacuum-boundary-gluing-and-wall-response]], the resulting OS-to-interface
unitary lands in

\[
L^2(\nu_{T,I})^{\mathrm{GI}}.
\tag{EW22a}
\]

Only when the reflection interface \(I\) is the canonical transfer slice
\(\Sigma\) may one identify

\[
\nu_{T,I}
=
\nu_{T,\Gamma},
\qquad
\mathrm d\nu_{T,\Gamma}
=
\psi_{0,T,\Gamma}^2\,\mathrm d\mu_{\mathrm H}^{E(\Gamma)},
\tag{EW22b}
\]

where \(\psi_{0,T,\Gamma}\) is the positive ground state of the transfer
Hamiltonian. A thick interface requires the separately constructed
domain-compatible map to the canonical slice described in the boundary
gluing note.

This statement retains the temporal-regulator firewall. Writing \(a_\tau\)
for Euclidean temporal length, an isotropic Wilson
transfer generator

\[
H_T=-\frac{\hbar c}{a_\tau}\log T
\tag{EW23}
\]

is not automatically the canonical Kogut--Susskind Hamiltonian at finite
\(a_\tau\). Accordingly, \(\nu_{T,\Gamma}\) equals the Hamiltonian vacuum law
\(\nu_\Gamma\) in (EW14) only when \(T=e^{-a_\tau H_N/(\hbar c)}\), with the
matched operator of (EW10), or after a controlled temporal-continuum and
form-identification theorem. The exceptional factorization does not remove
this standard obligation.

There is nevertheless an exact conditional composition theorem. Suppose the
reflection interface is the canonical transfer slice, the OS map

\[
B_\Gamma^{\mathrm{OS}}:
\mathcal H_{\mathrm{OS},\Gamma}
\overset{\sim}{\longrightarrow}
L^2(\nu_{T,\Gamma})^{\mathrm{GI}}
\tag{EW23a}
\]

is unitary and carries the unique transfer vacuum to \(1\), and the invariant
\(b_N\)-gradient \(D_{b_N}\) is closed. Require the form-domain inclusion

\[
B_\Gamma^{\mathrm{OS}}
\bigl(\operatorname{Dom}h_{T,\Gamma}^{\mathrm{OS}}\bigr)
\subseteq
\operatorname{Dom}D_{b_N}.
\tag{EW23a-domain}
\]

If \(\lambda_{T,\Gamma}^{(N)}>0\) and

\[
\|D_{b_N}f\|^2
\geq
\lambda_{T,\Gamma}^{(N)}
\|f\|^2,
\qquad
\int f\,\mathrm d\nu_{T,\Gamma}=0,
\tag{EW23b}
\]

and the centered transfer-Hamiltonian form obeys the independently proved
solder with \(\kappa_{N,\Gamma}>0\) and
\(c_{\mathrm{form},\Gamma}>0\),

\[
h_{T,\Gamma}^{\mathrm{OS}}[\Psi]
\geq
\kappa_{N,\Gamma}c_{\mathrm{form},\Gamma}
\left\|
D_{b_N}B_\Gamma^{\mathrm{OS}}\Psi
\right\|^2,
\tag{EW23c}
\]

then

\[
\boxed{
H_{T,\Gamma}^{\mathrm{OS}}-E_{0,T,\Gamma}
\geq
\kappa_{N,\Gamma}c_{\mathrm{form},\Gamma}
\lambda_{T,\Gamma}^{(N)}
(1-P_{0,T,\Gamma})}
\tag{EW23d}
\]

in quadratic-form sense. The proof is only the unitary identification of the
vacuum complement followed by (EW23b) and (EW23c); all physical content lies
in constructing those hypotheses. For an exactly matched Kogut--Susskind
semigroup, \(c_{\mathrm{form},\Gamma}=1\). A genuinely thick interface needs
an additional domain-compatible interface-to-slice map and its own lower
coverage constant.

## What each operator operates on

The complete finite-regulator type chain is

\[
\begin{array}{ccl}
\sigma_N(U_p)-I
&:&N_{\mathrm{def}}\longrightarrow N_{\mathrm{def}},\\[2pt]
\|\sigma_N(U_p)-I\|_{\mathrm{HS}}^2
&:&SU(3)\longrightarrow\mathbb R_{\geq0},\\[2pt]
M_{Q_N}
&:&\mathcal H_\Gamma\longrightarrow\mathcal H_\Gamma,\\[2pt]
\Delta_{\Gamma,b_N}
&:&\operatorname{Dom}\Delta_{\Gamma,b_N}
\subset\mathcal H_\Gamma\longrightarrow\mathcal H_\Gamma,\\[2pt]
D_{b_N}
&:&\operatorname{Dom}D_{b_N}\subset L^2(\nu_\Gamma)^{\mathrm{GI}}
\longrightarrow\mathcal K_{\mathrm{flux}},\\[2pt]
H_\Gamma-E_{0,\Gamma}
&:&\operatorname{Dom}H_\Gamma\subset\mathcal H_\Gamma
\longrightarrow\mathcal H_\Gamma.
\end{array}
\tag{EW24}
\]

The Hilbert--Schmidt contraction is the bridge from the finite probe fibre to
a scalar potential on configuration space. The trace metric is the bridge
from the same probe to the electric cometric. These operations are explicit
once \(N_{\mathrm{def}}\) has been selected as the response probe. The later ground-state multiplication
\(f\mapsto\psi_0f\) and the OS interface map are the relevant Hilbert-carrier
unitaries.

A field-valued map into \(N_{\mathrm{def}}\)-responses is necessary only if
the finite idempotency or flag-normal Hessian itself is proposed as the gap
form. It is not necessary to recover the Wilson holonomy theory.

## The revised stopping condition

Let \(r=(a,L)\) range along a tuned sequence of finite regulators and let
\(\widehat\Lambda_{\mathrm{YM},r}^{(\mathsf s)}\) be an independently defined
energy-valued scale representative in a declared scheme. On the exceptional
metric convention, the remaining quantitative target is

\[
\boxed{
\liminf_{r\to\mathrm{cont}}
\frac{
\kappa_{N,r}\,g(\Gamma_r)\Theta_r/18
}{
\widehat\Lambda_{\mathrm{YM},r}^{(\mathsf s)}
}
>0.}
\tag{EW25}
\]

It must be accompanied by generalized Mosco convergence of the physical
forms, convergence of the complete vacuum projections, and a nontrivial OS
and Poincare reconstruction. A fixed positive \(\Theta_r\) at each finite
regulator is insufficient; low-cost states may appear with growing volume or
regulator removal.

The exceptional construction has therefore moved the frontier, but in a
specific way. It derives the color connection groupoid, a faithful response
probe, the Wilson plaquette function, and an invariant electric metric from a
prior geometry. It does not need to force a finite normal space to *become*
the QFT Hilbert space. Its remaining Copernican burden is deeper: construct or
constrain the whole-to-slice vacuum law strongly enough that
\(\Theta_r\) cannot collapse, and fix the clock-energy coefficient without
reading either quantity back from the desired spectrum.
