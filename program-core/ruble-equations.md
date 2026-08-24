# The Ruble Equations

The Ruble equations are a typed dependency stack from causal scale through horizontal state response to a conjectural state–geometry equivalence and its homogeneous cosmological projection. Only the balanced-binary identities and the stated geometric or thermodynamic identities are exact; the wall construction, modulus localization, unit principles, source law, and covariant response remain open or constitutive.

Use

$$
x:=N-N_c
$$

for logarithmic scale displacement from the distinguished crossing. A prime on a homogeneous quantity denotes \(\mathrm d/\mathrm dN\).

## Canonical symbol policy

Several legacy notes use one symbol for different types. The core fixes:

| Core symbol | Meaning | Legacy usage to audit |
|---|---|---|
| \(m=\langle Q\rangle\) | binary polarization | often written \(\eta\); the core reserves \(\eta\) for an areal gravitational modulus |
| \(\boldsymbol\chi\) | local bilinear descent-modulus field | richer object than a homogeneous scalar |
| \(\chi_N(p)\) | local contraction on the physical scale tangent at \(p\in\Sigma_N\) | legacy \(\chi_\downarrow\) may mean this or a cut average |
| \(\overline\chi_{\Sigma,N}\) | integrated cut norm divided by area | should not be silently identified with \(\chi_N(p)\) |
| \(\mathfrak r_{\Sigma,N}(p)\) | local state–gravity matching field | some notes use \(\mathfrak R_\Sigma\) without distinguishing local and integrated scope |
| \(\mathfrak R_\Sigma(N)\) | integrated matching ratio on a general cut | not a pointwise field or automatically a constant along the path |
| \(\mathfrak R_c=\mathfrak R_{\Sigma_c}(N_c)\) | integrated crossing capacity number | retained for the historical homogeneous amplitude |
| \(R_c^{\mathrm{hor}}\) | horizon radius at the crossing | never abbreviated to \(\mathfrak R_c\) |

This policy is intentionally more explicit than the historical notation. Later module audits should translate symbols by type, not perform blind textual replacement.

## RE0 — Causal scale

**[STANDARD / DEFINITION]**

$$
\boxed{
g_{\mathrm{phys}}
=\sigma^{-2}\boldsymbol g,
\qquad
N=-\ln\frac{\sigma}{\sigma_c}.}
$$

The conformal metric \(\boldsymbol g\) fixes causal cones; the positive scale section \(\sigma\) fixes physical calibration. On a homogeneous FLRW specialization with \(\sigma\propto a^{-1}\),

$$
N=\ln\frac{a}{a_c}.
$$

The first definition is generic scale data; the second is its FLRW realization. Neither makes \(N\) proper time or modular time.

The reusable conformal distinction and its invariance proof live in [[conformal-scale-geometry/causal-order-and-metric-scale|causal order and metric scale]].

## RE1 — Physical horizontal state deformation

**[PRINCIPLE + OPEN CONSTRUCTION]**

$$
\boxed{
N\longmapsto
(\Sigma_N,\mathcal A_N,\omega_N,\mathcal T_{N_2N_1}),
\qquad
v_N=D^{\mathrm{hor}}\Phi(\partial_N).}
$$

The comparison maps \(\mathcal T\), physical quotient, and tangent normalization must be specified before \(v_N\) exists. The scale-to-state principle asserts that realized scale displacement has such an invariant horizontal image.

## RE2 — Distinguishability response and localization

**[EXACT UNDER REGULARITY, THEN OPEN LOCALIZATION]**

Let

$$
\widetilde\omega_{N+\delta N}^{(N)}
:=\mathcal T_{N\leftarrow N+\delta N}
(\omega_{N+\delta N})
$$

denote the neighboring state after transport to the carrier at \(N\). If \(\mathcal T\) is specified on observables, this notation means the induced dual transport on states. Under the regularity and comparability hypotheses,

$$
\boxed{
D(\widetilde\omega_{N+\delta N}^{(N)}\Vert\omega_N)
=\frac12G^{\perp}_{NN}(N)\,\delta N^2
+o(\delta N^2),}
$$

with

$$
G^{\perp}_{NN}
:=g^{\mathrm{BKM}}(v_N,v_N)\geq0.
$$

The localization target is a symmetric bilinear finite signed-measure-valued form \(\mu^{\mathrm{desc}}_{v,w}\) on measurable cut patches, with positive diagonal and a common area measure \(\mu_A\), such that

$$
\mu^{\mathrm{desc}}_{v,w}\ll\mu_A
$$

for the physical tangent sector under consideration, with full-cut normalization

$$
\boxed{
\mu^{\mathrm{desc}}_{v,w}(\Sigma_N)
=g^{\mathrm{BKM}}_{\omega_N}(v,w).}
$$

Its Radon--Nikodym density is

$$
\boxed{
\boldsymbol\chi(v,w;p)
:=\frac{\mathrm d\mu^{\mathrm{desc}}_{v,w}}
{\mathrm d\mu_A}(p),
\qquad
\chi_N(p):=\boldsymbol\chi(v_N,v_N;p),
\qquad
\mathfrak a_N(p):=\chi_N(p)^{-1}.}
$$

The corresponding cut average is

$$
\overline\chi_{\Sigma,N}
:=\frac{\mu^{\mathrm{desc}}_{v_N,v_N}(\Sigma_N)}
{\mu_A(\Sigma_N)}.
$$

Here \(p\in\Sigma_N\), \([\chi_N]=[\overline\chi_{\Sigma,N}]=L^{-2}\), and \([\mathfrak a_N]=L^2\) for the dimensionless normalized scale tangent. The first object is a local bilinear modulus; the scalar and its inverse are contractions on a pointwise nondegenerate physical direction. The average need not equal the local density. Cross-term densities require absolute continuity of the signed measures themselves, obtained directly or by a justified polarization and measure Cauchy--Schwarz argument.

The coincidence-Hessian theorem is owned by [[basic-concepts/hessians/entry#Log-partition Hessians and Fisher geometry|the Hessian module]]; [[basic-concepts/hessians/gibbs-free-energy-relative-entropy|the Gibbs--relative-entropy identity]] records the fixed-Hamiltonian thermodynamic specialization. Neither theorem supplies the open localization map.

## RE3 — State–geometry equivalence

**[FULL-WELD CONJECTURE + NORMALIZED-CHANNEL PRINCIPLE]**

The full structural target is a covariant same-tangent map

$$
\mathfrak S_\Sigma:
H^{\mathrm{state}}_\Sigma
\longrightarrow
H^{\mathrm{grav}}_\Sigma
$$

such that, for all physical tangents \(v,w\), the localized response geometries obey the measure-valued weld

$$
\boxed{
\mu^{\mathrm{desc}}_{v,w}
=Z_g\,
\mu^{\mathrm{grav,resp}}_{\mathfrak S_\Sigma v,
\mathfrak S_\Sigma w}.}
$$

Here \(\mu^{\mathrm{grav,resp}}\) is the tangent-indexed gravitational response measure computed from a unit-normalized kinetic term and \(Z_g\) remains symbolic. Its full-cut integral may be written

$$
g^{\mathrm{BKM}}(v,w)
=Z_g\,
\mathcal E^{(1)}_{\mathrm{can}}
(\mathfrak S_\Sigma v,\mathfrak S_\Sigma w),
$$

with \([Z_g\mathcal E^{(1)}_{\mathrm{can}}]=1\). Before the normalization is absorbed into the target response form, this is a prospective equivariant homothety; it becomes an isometry only after the common normalization is fixed.

The full response weld does not by itself identify a quadratic response with background entropy. Separately suppose the gravitational theory supplies a positive entropy measure \(\mu^{S,\mathrm{grav}}\) on the same cut in the same prescription. When

$$
\mu^{S,\mathrm{grav}}\ll\mu_A,
$$

define

$$
\eta_{\mathrm{grav}}(p)
:=\frac{\mathrm d\mu^{S,\mathrm{grav}}}
{\mathrm d\mu_A}(p).
$$

The additional horizon or canonical-energy bridge for the canonically normalized scale tangent is

$$
\boxed{
Z_g\,
\mu^{\mathrm{grav,resp}}_{\mathfrak S_\Sigma v_N,
\mathfrak S_\Sigma v_N}
=\mu^{S,\mathrm{grav}}.}
$$

This is a distinct physical principle. Together with the full weld it gives \(\mu^{\mathrm{desc}}_{v_N,v_N}=\mu^{S,\mathrm{grav}}\). To define the corresponding local comparison, require

$$
\mu^{\mathrm{desc}}_{v_N,v_N}
\ll\mu^{S,\mathrm{grav}}.
$$

The local Ruble matching field is then

$$
\boxed{
\mathfrak r_{\Sigma,N}(p)
:=\frac{\mathrm d\mu^{\mathrm{desc}}_{v_N,v_N}}
{\mathrm d\mu^{S,\mathrm{grav}}}(p)
=\frac{\chi_N(p)}
{\eta_{\mathrm{grav}}(p)}.}
$$

The density quotient is understood on the support of \(\mu^{S,\mathrm{grav}}\), where \(\eta_{\mathrm{grav}}>0\), and all pointwise statements retain their almost-everywhere measure-theoretic scope unless additional regularity is proved.

The strong causal-capacity equivalence principle for this normalized scale channel is

$$
\boxed{
\mathfrak r_{\Sigma,N}(p)=1
\quad\mu^{S,\mathrm{grav}}\text{-a.e.}
\quad\Longleftrightarrow\quad
\mu^{\mathrm{desc}}_{v_N,v_N}
=\mu^{S,\mathrm{grav}}.}
$$

This contraction-level equality throughout a declared universality class is stronger than crossing equality on one cut, but it does not by itself construct the full tangent-space weld above.

In a two-derivative Einstein universality class,

$$
\mu^{S,\mathrm E}(U)
=\eta_{\mathrm E}\mu_A(U),
\qquad
\eta_{\mathrm E}
=\frac{c^3}{4\hbar G},
$$

so an independently calculated universal state-side modulus \(\chi_*\), together with the Einstein-class equivalence, gives

$$
\boxed{
G_{\mathrm{pred}}
=\frac{c^3}{4\hbar\chi_*}.}
$$

This is noncircular only if \(\chi_*\) and area were constructed without measured \(G\), Bekenstein--Hawking normalization containing \(G\), or the target cosmological history.

## RE4 — Balanced binary specialization

**[IDENTIFICATION, BALANCE ASSUMPTION, THEN EXACT]**

Suppose the relevant reflection-odd horizontal response factors through a normalized binary generator

$$
Q^*=Q,
\qquad
Q^2=\mathbf1.
$$

Let

$$
P_\pm:=\frac{\mathbf1\pm Q}{2},
$$

and suppose a faithful reference state \(\rho_0\) commutes with \(Q\) and has balanced total weights

$$
\operatorname{Tr}(\rho_0P_+)
=\operatorname{Tr}(\rho_0P_-)
=\frac12.
$$

A geometric reflection may satisfy

$$
J_{\mathrm{refl}}QJ_{\mathrm{refl}}^{-1}=-Q,
$$

but \(J_{\mathrm{refl}}\) is not automatically Tomita conjugation. Balance is not a consequence of \(Q^2=\mathbf1\).

Define the balanced exponential family by

$$
\rho_\theta
=\frac{e^{\theta Q/2}\rho_0e^{\theta Q/2}}
{Z_{\rho_0}(\theta)},
\qquad
Z_{\rho_0}(\theta)
:=\operatorname{Tr}(\rho_0e^{\theta Q})
=\cosh\theta,
\qquad
\psi(\theta):=\ln Z_{\rho_0}(\theta).
$$

For this family, one obtains

$$
\boxed{
m(\theta):=\langle Q\rangle_{\rho_\theta}
=\tanh\theta,
\qquad
g^{\mathrm{bin}}_{\theta\theta}
=\operatorname{sech}^2\theta,
\qquad
m^2+g^{\mathrm{bin}}_{\theta\theta}=1.}
$$

These equations fix a normalized shape and Casimir allocation. They do not construct the full wall, its channel multiplicity, a fact, a charge, or gravity.

The exact reduction is proved once in [[binary-information-geometry/balanced-exponential-family|the balanced exponential-family theorem]]. The claim that a physical wall admits this reduction belongs instead to [[wall-construction-interface/binary-channel|the binary-channel interface]].

## RE5 — Scale soldering, width, and extensive norm

**[CONDITIONAL THEOREM + SEPARATE PRINCIPLE + ASSUMPTION]**

Under rank-one ratio dependence, cocycle composition, controlled holonomy, and regularity,

$$
\boxed{
\theta=\varrho_\perp x,
\qquad
\nu:=|\varrho_\perp|.}
$$

The unit-width principle separately proposes

$$
\boxed{\nu=1.}
$$

With a physical extensive factor \(C_\perp(N)\),

$$
\boxed{
G^{\perp}_{NN}(N)
=C_\perp(N)\nu^2
\operatorname{sech}^2(\nu x).}
$$

The rigid homogeneous pulse assumes

$$
C_\perp(N)=C_{\perp,c}.
$$

Neither the binary Casimir nor affine soldering determines \(C_{\perp,c}\).

The affine conclusion and its hypotheses are isolated in [[basic-concepts/soldering/affine-scale-state|affine scale--state soldering]]. [[basic-concepts/soldering/continuous-character-no-go|The continuous-character no-go]] explains why the slope is not fixed by the additive and multiplicative group structures alone.

## RE6 — Integrated crossing capacity

**[DEFINITION + WEAK PRINCIPLE]**

For a general cut with nonzero total gravitational entropy measure, define the integrated Ruble ratio

$$
\boxed{
\mathfrak R_\Sigma(N)
:=\frac{
\mu^{\mathrm{desc}}_{v_N,v_N}(\Sigma_N)}
{\mu^{S,\mathrm{grav}}(\Sigma_N)}.}
$$

When the local matching field exists,

$$
\mathfrak R_\Sigma(N)
=\frac{
\displaystyle\int_{\Sigma_N}
\mathfrak r_{\Sigma,N}(p)\,
\mathrm d\mu^{S,\mathrm{grav}}(p)}
{\mu^{S,\mathrm{grav}}(\Sigma_N)}.
$$

It is therefore an entropy-measure-weighted average of the local field. It becomes an area average only in a constant-\(\eta_{\mathrm{grav}}\) regime.

At the distinguished crossing, set

$$
\frac{S_c}{k_B}
:=\mu^{S,\mathrm{grav}}(\Sigma_c),
\qquad
G^{\perp}_{NN}(N_c)
:=\mu^{\mathrm{desc}}_{v_{N_c},v_{N_c}}(\Sigma_c),
$$

and define the cosmological crossing number

$$
\boxed{
\mathfrak R_c
:=\mathfrak R_{\Sigma_c}(N_c)
=\frac{k_B}{S_c}
G^{\perp}_{NN}(N_c)
=\frac{k_BC_{\perp,c}\nu^2}{S_c}.}
$$

The weak Ruble principle is

$$
\boxed{\mathfrak R_c=1.}
$$

Under constant \(C_\perp\),

$$
\boxed{
G^{\perp}_{NN}(N)
=\frac{S_c}{k_B}\mathfrak R_c
\operatorname{sech}^2(\nu x).}
$$

\(\mathfrak R_c\) is an integrated amplitude at one cut. It is not the local field \(\mathfrak r_{\Sigma,N}(p)\), a pathwise constant, or an RG fixed point. Unit integrated matching does not imply pointwise unit matching; it fixes only the weighted average above unless a local constancy theorem is supplied.

The extensive normalization required at the crossing is

$$
\boxed{
C_{\perp,c}
=\frac{S_c}{k_B}\frac{\mathfrak R_c}{\nu^2}.}
$$

For the current unit-branch benchmark this is approximately \(1.50\times10^{122}\). That number is a full-cut target in the benchmark scheme, not a per-channel coefficient or a fundamental pure constant.

## RE7 — Anchored source and horizon conversion

**[CONSTITUTIVE]**

The homogeneous source law is

$$
\boxed{
\rho_X(N)
:=\frac{k_BT_c}{2V_c}
G^{\perp}_{NN}(N).}
$$

**[IDENTIFICATION — OPEN CONSTRUCTION]** The temperature anchoring the horizontal source is identified with the canonical apparent-horizon temperature at the crossing:

$$
T_c:=T_{\mathrm{hor},c}.
$$

The semiclassical horizon temperature does not by itself prove that the horizontal state deformation uses this temperature.

**[STANDARD / EXACT GIVEN THE IDENTIFICATION]** For a flat \(3+1\)-dimensional FLRW apparent horizon,

$$
R_c^{\mathrm{hor}}=\frac{c}{H_c},
\qquad
k_BT_{\mathrm{hor},c}
=\frac{\hbar c}{2\pi R_c^{\mathrm{hor}}},
\qquad
\frac{S_c}{k_B}
=\frac{\pi c^3(R_c^{\mathrm{hor}})^2}{G\hbar},
$$

and

$$
\boxed{
k_BT_c\frac{S_c}{k_B}
=E_{\mathrm{MS},c}
=\rho_{\mathrm{crit},c}V_c.}
$$

This identity contains \(G\). It closes the homogeneous source after the horizon assumptions; it does not derive \(G\).

The geometric conversion is proved independently in [[conformal-scale-geometry/hawking-friedmann-identity|the Hawking--Friedmann identity]].

## RE8 — Generalized homogeneous Ruble response

**[CONDITIONAL OUTPUT]**

Combining RE5–RE7 gives

$$
\boxed{
\rho_X(N)
=\frac{\mathfrak R_c}{2}
\rho_{\mathrm{crit},c}
\operatorname{sech}^2(\nu x).}
$$

At the crossing,

$$
\boxed{
\Omega_{X,c}
=\frac{\mathfrak R_c}{2}.}
$$

Any interval such as \(0<\mathfrak R_c<2\) is downstream of this source law together with flatness and positivity of the complementary density. It is not a kinematic or information-geometric bound. Likewise, equal partition at \(\mathfrak R_c=1\) follows from the linear relation above plus the weak unit principle; the midpoint of a linear interval is not an independent explanation of unity.

On a spatially flat crossing, \(\mathfrak R_c=1\) makes the response equal the total non-\(X\) complement. If the declared complement contains only ordinary matter and radiation, with zero residual vacuum and no additional sector, then

$$
\rho_{X,c}=\rho_{m,c}+\rho_{r,c}.
$$

It equals dustlike matter alone only when radiation and every other component are negligible.

The unit branch is

$$
(\nu,\mathfrak R_c)=(1,1).
$$

It is selected by two independent principles.

## RE9 — Equation of state and shape invariant

**[CONDITIONAL OUTPUT GIVEN SEPARATE CONSERVATION]**

If the response obeys

$$
\rho_X'=-3(1+w_X)\rho_X,
$$

then

$$
\boxed{
w_X(N)
=-1+\frac{2\nu}{3}\tanh(\nu x),}
$$

and

$$
\boxed{
9(1+w_X)^2+6w_X'=4\nu^2.}
$$

These are rigid consequences of the generalized pulse and separate conservation. They are not independent evidence for the microscopic wall or the equivalence principles.

The calculation is isolated in [[causal-scale-theory/theorems/rigid-sech-response-identities|the rigid-response theorem]].

## RE10 — Prospective causal charge extension

**[CONJECTURE — NOT IN THE HOMOGENEOUS DERIVATION]**

If a common continuous causal symmetry and covariant phase space exist,

$$
\boxed{
\boldsymbol\mu^{\mathrm{causal}}_\Sigma
=\boldsymbol\mu^{\mathrm{state+matter}}_\Sigma
+\boldsymbol\mu^{\mathrm{grav}}_\Sigma
+\boldsymbol\mu^{\mathrm{record}}_\Sigma
\in\mathfrak g_c^*,}
$$

and, for \(\xi\in\mathfrak g_c\),

$$
Q_\xi[\Sigma]
:=\left\langle
\boldsymbol\mu^{\mathrm{causal}}_\Sigma,\xi
\right\rangle.
$$

The conjectured flux balance is

$$
\boxed{
Q_\xi[\Sigma_2]
-Q_\xi[\Sigma_1]
+\mathcal F_\xi[W]=0.}
$$

The \(\mathrm{state+matter}\) contribution includes the complete nongravitational sector: bulk matter and the relevant wall or observer-state degrees of freedom. A further split into wall-state and bulk-matter charges requires a gauge-compatible factorization and must not count matter twice.

This is the prospective conservation law. It does not follow from \(\mathfrak r_{\Sigma,N}(p)=1\), \(\mathfrak R_c=1\), or the binary Casimir. The hoped-for bridge is a common variational structure relating BKM capacity to gravitational canonical energy while retaining the distinction between a quadratic capacity and linear charge.

## The several appearances of one

| Equation | Meaning of \(1\) |
|---|---|
| \(c=1\) | unit convention for a dimensionful conversion |
| \(Q^2=\mathbf1\) | representation normalization |
| \(\operatorname{sech}^2(0)=1\) | normalized binary peak identity |
| \(m^2+g_{\theta\theta}^{\mathrm{bin}}=1\) | binary second-moment Casimir |
| \(\nu=1\) | proposed width law after canonical normalization |
| \(\mathfrak R_c=1\) | proposed integrated crossing equivalence |
| \(\mathfrak r_{\Sigma,N}(p)=1\) | proposed local equality in the normalized scale channel |
| \(C_E/(S/k_B)=1\) | conditional \(n=1\) conformal thermal result |

No row proves another.

## Constitutional no-go at the crossing

For the literal two-state specialization

$$
\rho_0=\frac{\mathbf1}{2},
\qquad
\rho_\theta=\frac{e^{\theta Q}}{2\cosh\theta},
$$

the modular variance is

$$
\operatorname{Var}_{\rho_\theta}(-\ln\rho_\theta)
=\theta^2\operatorname{sech}^2\theta.
$$

Hence at \(\theta=0\),

$$
g^{\mathrm{BKM}}_{\theta\theta}(0)=1,
\qquad
\operatorname{Var}_{\rho_0}(-\ln\rho_0)=0.
$$

The binary translation tangent is therefore not the escort-temperature tangent of the same reduced state; [[binary-information-geometry/escort-tangent-no-go|the exact no-go]] owns this calculation. [[deriving-value-of-g/noether-capacity-theorem|The Noether--capacity theorem]] gives the conditional result \(C_E/(S/k_B)=n\) for a conformal thermal sector. It can explain a unit ratio here only if a larger physical wall sector is shown to be effectively \(1+1\)-dimensional and its sufficient reduction preserves the relevant tangent norm in one common scheme. Calling unity a *saturation* is licensed only inside a class with a proved inequality and an identified attaining sector; outside that class, \(\mathfrak R_c=1\) remains a matching principle.

This is why **Ruble's Equations** is the appropriate name for the system, while **Ruble's Constant** is not currently a canonical object.
