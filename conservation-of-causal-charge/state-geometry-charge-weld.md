# The State--Geometry Charge Weld

Causal capacity is a positive quadratic response, whereas causal charge is a signed linear moment-map or boundary quantity. This note interprets the canonical state--geometry response weld as a possible second-variation layer of one causal symmetry; it imports the response objects and matching notation from the programme core and does not turn their equality into a conservation law by itself.

## The canonical capacity side

[[program-core/localized-areal-response-geometry|Localized areal response geometry]] owns the state-side construction. A scale-indexed family first requires a common carrier, cross-fiber transport, a physical horizontal quotient, and a canonically normalized scale tangent

$$
v_N:=D^{\mathrm{hor}}\Phi(\partial_N).
$$

Its cut-integrated BKM capacity is

$$
G^\perp_{NN}
:=g^{\mathrm{BKM}}_{\omega_N}(v_N,v_N).
$$

Localization is an additional theorem target: for physical tangents \(v,w\), construct a symmetric bilinear measure \(\mu^{\mathrm{desc}}_{v,w}\) on cut patches such that

$$
\mu^{\mathrm{desc}}_{v,w}(\Sigma)
=g^{\mathrm{BKM}}_\omega(v,w).
$$

If this measure is absolutely continuous with respect to an independently normalized area measure \(\mu_A\), its Radon--Nikodym derivative is the local bilinear areal modulus

$$
\boldsymbol\chi(v,w;p)
:=\frac{\mathrm d\mu^{\mathrm{desc}}_{v,w}}
{\mathrm d\mu_A}(p).
$$

The physical scale contraction is

$$
\chi_N(p):=\boldsymbol\chi(v_N,v_N;p).
$$

These objects are quadratic capacities. They are not modular charges, entropy measures, or outcome counts. A normalized binary metric can supply a profile for one reduced tangent, but it cannot construct the local measure or its extensive normalization.

## The same-tangent response weld

Let

$$
\mathfrak S_\Sigma:
H^{\mathrm{state}}_\Sigma
\longrightarrow
H^{\mathrm{grav}}_\Sigma
$$

be a covariant map between the physical state and gravitational tangent sectors. [[program-core/causal-capacity-equivalence|Causal-capacity equivalence]] owns the strongest response-level target:

$$
\boxed{
\mathrm d\mu^{\mathrm{desc}}_{v,w}
=Z_g\,
\mathrm d\mu^{\mathrm{grav,resp}}_{\mathfrak S_\Sigma v,
\mathfrak S_\Sigma w}}
\qquad
\text{for all physical }v,w.
$$

After integration over a cut, this entails

$$
g^{\mathrm{BKM}}(v,w)
=Z_g\,
\mathcal E^{(1)}_{\mathrm{can}}
(\mathfrak S_\Sigma v,\mathfrak S_\Sigma w).
$$

The gravitational form is computed with a unit-normalized kinetic term and \(Z_g\) remains symbolic until a common normalization is derived. Before that normalization is fixed, the proposed map is a homothety, not an isometry. Equal numbers obtained from different tangents, carriers, or prescriptions do not establish the weld.

## Local matching and the Einstein branch

Suppose the gravitational theory independently supplies a positive entropy measure \(\mu^{S,\mathrm{grav}}\) with

$$
\eta_{\mathrm{grav}}(p)
:=\frac{\mathrm d\mu^{S,\mathrm{grav}}}
{\mathrm d\mu_A}(p)>0
$$

almost everywhere. The core then defines the local Ruble matching field

$$
\boxed{
\mathfrak r_{\Sigma,N}(p)
:=\frac{\mathrm d\mu^{\mathrm{desc}}_{v_N,v_N}}
{\mathrm d\mu^{S,\mathrm{grav}}}(p)
=\frac{\chi_N(p)}{\eta_{\mathrm{grav}}(p)}.}
$$

In a two-derivative Einstein universality class,

$$
\eta_{\mathrm E}
=\frac{c^3}{4\hbar G}.
$$

The strong scale-channel principle is

$$
\boxed{
\mathfrak r_{\Sigma,N}(p)=1
\quad\Longleftrightarrow\quad
\mathrm d\mu^{\mathrm{desc}}_{v_N,v_N}
=\mathrm d\mu^{S,\mathrm E}}
$$

almost everywhere throughout a declared class. If the state-side construction independently returns one universal scalar \(\chi_*\), this equality gives

$$
\chi_*=\eta_{\mathrm E},
\qquad
G_{\mathrm{pred}}
=\frac{c^3}{4\hbar\chi_*}.
$$

The calculation is circular if measured \(G\), Einstein area entropy containing \(G\), or the target cosmological history fixes \(\chi_*\) on the state side.

## Integrated crossing equality is weaker

On a cut with nonzero gravitational entropy, define

$$
\mathfrak R_\Sigma(N)
:=\frac{
\mu^{\mathrm{desc}}_{v_N,v_N}(\Sigma_N)}
{\mu^{S,\mathrm{grav}}(\Sigma_N)}.
$$

At the distinguished crossing,

$$
\mathfrak R_c
:=\mathfrak R_{\Sigma_c}(N_c)
=\frac{k_B}{S_c}G^\perp_{NN}(N_c).
$$

The weak principle \(\mathfrak R_c=1\) fixes one gravitational-measure-weighted average. It does not imply \(\mathfrak r_{\Sigma,N}(p)=1\) locally, along the full history, or in other gravitational regimes.

## How a quadratic weld could participate in charge

The causal moment map proposed in [[causal-individuation-balance]] is linear in its normalized generator. The BKM form and gravitational canonical energy are quadratic in perturbations. They can belong to one structure only if a common variational construction shows that the quadratic response is a Hessian, second variation, or polarization of the same Hamiltonian or boundary-charge system.

Thus the response weld would not add “capacity” as another term in the charge sum. It would explain how the susceptibility of the state sector and the canonical response of geometry arise from one generator after differentiation. The combined action, first-variation charge, second-variation form, gauge reduction, edge terms, and flux law must all be compatible.

## Failure conditions

The proposal fails or changes universality class if the descent measure is not finite, local, positive on physical diagonals, additive, or regulator controlled; if the compared forms use different tangents or carriers; if the same-tangent map is noncovariant or rank deficient beyond declared gauge directions; if \(\boldsymbol\chi\) is species-, state-, direction-, or curvature-dependent without a controlled law; or if the normalization imports the gravitational coefficient it claims to return.

Such a result can leave a useful response geometry while defeating universal Einstein matching or its causal-charge interpretation. [[program-core/claim-and-failure-contract|The claim-and-failure contract]] governs those return values, and [[basic-concepts/soldering/entry|soldering discipline]] governs the proposed cross-register map.
