# Causal-Capacity Equivalence

The keystone physical conjecture is that horizontal state distinguishability and gravitational area response are two representations of one local modulus. Its unit scalar form is an equivalence law only when the state and gravitational measures, tangents, areas, and renormalization prescriptions have been fixed independently.

## The gravitational modulus

For a gravitational theory with a well-defined horizon or Wald entropy functional, first construct a positive dimensionless gravitational entropy measure \(\mu^{S,\mathrm{grav}}\) on the cut. If

$$
\mu^{S,\mathrm{grav}}\ll\mu_A,
$$

define

$$
\eta_{\mathrm{grav}}(p)
:=\frac{\mathrm d\mu^{S,\mathrm{grav}}}
{\mathrm d\mu_A}(p).
$$

Generic Wald or higher-curvature entropy need not be a functional of area alone, so this absolute-continuity statement is a hypothesis rather than notation. In two-derivative Einstein gravity,

$$
\mu^{S,\mathrm E}(U)
:=\eta_{\mathrm E}A(U),
$$

with the constant

$$
\boxed{
\eta_{\mathrm E}
=\frac{c^3}{4\hbar G}
=\frac{1}{4\ell_P^2}.}
$$

Its inverse is the Einstein areal compliance

$$
\mathfrak a_{\mathrm E}
=\eta_{\mathrm E}^{-1}
=\frac{4\hbar G}{c^3}.
$$

Strictly, \(\mathfrak a_{\mathrm E}\), not \(G\) alone, has the units and literal interpretation of area per unit dimensionless entropy or distinguishability curvature. \(G\) is that compliance expressed in mechanical units through \(c\) and \(\hbar\). [[deriving-value-of-g/areal-information-modulus|The areal information modulus]] gives the established Einstein identities.

## The structural weld precedes the scalar ratio

Let

$$
\mathfrak S_\Sigma:
H^{\mathrm{state}}_\Sigma
\longrightarrow
H^{\mathrm{grav}}_\Sigma
$$

be a covariant same-tangent map. Suppose the gravitational theory also supplies a localized bilinear response measure

$$
\mu^{\mathrm{grav,resp}}_{\mathfrak S_\Sigma v,\mathfrak S_\Sigma w}(U)
$$

whose total is the appropriately normalized canonical-energy form. The strongest response-level target is then the measure-valued homothety

$$
\boxed{
\mathrm d\mu^{\mathrm{desc}}_{v,w}
=Z_g\,
\mathrm d\mu^{\mathrm{grav,resp}}_{\mathfrak S_\Sigma v,\mathfrak S_\Sigma w}}
\qquad
\text{for all physical }v,w.
$$

After integration over the cut, this entails the bilinear form

$$
\boxed{
g^{\mathrm{BKM}}(v,w)
=Z_g\,
\mathcal E^{(1)}_{\mathrm{can}}
(\mathfrak S_\Sigma v,\mathfrak S_\Sigma w)}
\qquad
\text{for all physical }v,w.
$$

Here \(\mathcal E^{(1)}_{\mathrm{can}}\) is computed with a unit-normalized gravitational kinetic term and \(Z_g\) is kept symbolic, with \([Z_g\mathcal E^{(1)}_{\mathrm{can}}]=1\) in the displayed normalization. This is a prospective equivariant homothety; it becomes an isometry only after the target normalization is fixed. It must preserve the same physical tangents, not merely return equal scalar norms for unrelated vectors.

The weaker **Einstein scale-direction matching** concerns only the canonically normalized tangent \(v_N\). It additionally requires a horizon or canonical-energy bridge identifying the selected gravitational response measure with the Einstein entropy-area measure:

$$
\mathrm d\mu^{\mathrm{desc}}_{v_N,v_N}
\stackrel{?}{=}
\mathrm d\mu^{S,\mathrm E}
=\eta_{\mathrm E}\,\mathrm dA.
$$

Universality of this rank-one contraction across cuts does not by itself prove the full bilinear homothety. Conversely, the abstract homothety does not fix the Einstein entropy normalization until the bridge is supplied.

A strict extended use of *soldering* requires a declared source, target, base, symmetry action, covariance law, rank, and preservation property. [[basic-concepts/soldering/entry|Soldering]] owns those conditions.

## The local matching field

When both localized measures exist on one physical cut with one compatible trace and renormalization prescription, require

$$
\mu^{\mathrm{desc}}_{v_N,v_N}\ll\mu^{S,\mathrm{grav}},
\qquad
\eta_{\mathrm{grav}}(p)>0
\quad\text{almost everywhere}.
$$

Then define

$$
\boxed{
\mathfrak r_{\Sigma,N}(p)
:=
\frac{\mathrm d\mu^{\mathrm{desc}}_{v_N,v_N}}
{\mathrm d\mu^{S,\mathrm{grav}}}(p)
=\frac{\chi_N(p)}{\eta_{\mathrm{grav}}(p)}.}
$$

This is the **Ruble matching field**. It is a diagnostic of mismatch, not the fundamental response object. In a rank-one, homogeneous, constant-density reduction it becomes a number.

The local Einstein-class principle is

$$
\boxed{
\mathfrak r_{\Sigma,N}=1
\quad\mu^{S,\mathrm E}\text{-a.e. on }\Sigma.}
$$

It is equivalent to the measure equality

$$
\boxed{
\mathrm d\mu^{\mathrm{desc}}_{v_N,v_N}
=\mathrm d\mu^{S,\mathrm E}
=\eta_{\mathrm E}\,\mathrm dA.}
$$

Unity here is invariant under changes of physical units. Its content is that an independently constructed state measure and gravitational measure agree on the selected physical scale direction after the declared soldering.

## Cut ratio, weak crossing law, and strong universality

For any cut on which the denominator is positive and finite, define the integrated cut ratio

$$
\boxed{
\mathfrak R_\Sigma(N)
:=
\frac{\mu^{\mathrm{desc}}_{v_N,v_N}(\Sigma_N)}
{\mu^{S,\mathrm{grav}}(\Sigma_N)}.}
$$

Under the absolute-continuity hypotheses,

$$
\mathfrak R_\Sigma(N)
=
\frac{\int_{\Sigma_N}
\mathfrak r_{\Sigma,N}(p)\,
\mathrm d\mu^{S,\mathrm{grav}}(p)}
{\mu^{S,\mathrm{grav}}(\Sigma_N)}.
$$

It is therefore a gravitational-entropy-measure-weighted average of the local matching field. It is an ordinary area average only when \(\eta_{\mathrm{grav}}\) is constant on the cut.

At a self-dual cosmological cut, define the integrated crossing ratio

$$
\mathfrak R_c
:=\mathfrak R_{\Sigma_c}(N_c).
$$

When \(\mu^{S,\mathrm{grav}}(\Sigma_c)=S_c/k_B\), it can be written

$$
\mathfrak R_c
=\frac{\mu^{\mathrm{desc}}_{v_{N_c},v_{N_c}}(\Sigma_c)}
{S_c/k_B}
=\frac{k_B}{S_c}G^{\perp}_{NN}(N_c).
$$

The **weak Ruble principle** is

$$
\boxed{\mathfrak R_c=1.}
$$

$$
\mathfrak R_c
=\frac{\int_{\Sigma_c}
\mathfrak r_{\Sigma_c,N_c}(p)\,
\mathrm d\mu^{S,\mathrm{grav}}}
{\mu^{S,\mathrm{grav}}(\Sigma_c)}.
$$

Thus it is a gravitational-measure-weighted average of the local matching field. It becomes an area-weighted average only in an Einstein or other constant-\(\eta_{\mathrm{grav}}\) regime. It selects the weak-unit homogeneous branch at one cut after the common-carrier, localization, entropy-extensivity, and compatible-scheme hypotheses are supplied.

The **strong causal-capacity equivalence principle** is the local measure equality throughout a declared Einstein universality class. It is the stronger statement needed if one coefficient is to govern local focusing, weak-field gravity, lensing, waves, cosmology, and horizon entropy.

Thus

$$
\mathfrak R_c=1
\not\Longrightarrow
\mathfrak r_{\Sigma,N}(p)=1
\text{ universally}.
$$

## What can be meant by a new constant

The programme has one missing dimensionful **modulus slot**. Its status has three possibilities.

1. **Primitive matched \(\chi_*\).** If a universal \(\chi_*\) is postulated and the unit Einstein matching principle additionally identifies \(\chi_*=\eta_{\mathrm E}\), the basis

   $$
   \{c,\hbar,k_B,G\}
   \longleftrightarrow
   \{c,\hbar,k_B,\chi_*\}
   $$

   has changed, but the number of independent dimensionful inputs has not. Without that matching principle, primitive \(\chi_*\) and \(G\) are two independent dimensionful inputs and \(\mathfrak r_*\) compares them.

2. **Derived \(\chi_*\).** If a wall construction calculates \(\chi_*\) using an independently normalized area or spectral scale and no measured gravitational coefficient, then

   $$
   \boxed{
   G_{\mathrm{pred}}
   =\frac{c^3}{4\hbar\chi_*}}
   $$

   is a physical prediction.

3. **Nonuniversal \(\boldsymbol\chi\).** If the response remains a field or tensor, Einstein gravity is not the universal scalar specialization. The result may describe varying coupling, equivalence-principle violation, higher-curvature response, anisotropy, or nonlocality.

No new dimensionless constant appears if the independently derived matching field is identically one. A universal irreducible value \(\mathfrak r_*\ne1\) would introduce a dimensionless coefficient requiring its own reason. A cut-, state-, or scale-dependent value is a constitutive field, not a constant. It is not an RG-running coupling without an operator basis, subtraction prescription, probe scale, and beta function.

## Capacity-generated unit family

Any positive inverse-area modulus defines a convenient family of units:

$$
\ell_\chi:=\frac{1}{2\sqrt{\chi_*}},
\qquad
t_\chi:=\frac{\ell_\chi}{c},
$$

$$
m_\chi:=\frac{\hbar}{c\ell_\chi},
\qquad
E_\chi:=\frac{\hbar c}{\ell_\chi},
\qquad
T_\chi:=\frac{\hbar c}{k_B\ell_\chi}.
$$

If \(\chi_*=\eta_{\mathrm E}=1/(4\ell_P^2)\), then \(\ell_\chi=\ell_P\) and the remaining quantities become the corresponding Planck units. These are exact definitions after a positive \(\chi_*\) is supplied. They show that the Planck family can be read as several unit translations of one areal modulus; they do not independently calculate that modulus.

## Weak gravity means high stiffness

On the unit Einstein branch,

$$
G
=\frac{c^3}{4\hbar}\mathfrak a_*
=\frac{c^3}{4\hbar\chi_*}.
$$

Therefore smaller \(G\) means smaller compliance and larger areal modulus:

$$
\boxed{
\text{weak gravitational coupling}
\quad\Longleftrightarrow\quad
\text{high areal causal stiffness}.}
$$

This is the precise content of the proposed retyping. It should not be reversed into the claim that weak gravity means more area per unit distinguishability curvature.

## The role of \(c\)

The speed \(c\) and the modulus \(\chi\) occupy different layers. The former calibrates the Lorentzian causal cone and bounds causal propagation. The latter measures a constitutive response of state distinguishability per area. Setting \(c=1\) hides a conversion between length and time; it cannot force \(\mathfrak r_{\Sigma,N}=1\) or determine \(\chi_*\).

The causal speed limit motivates a finite arena of becoming, but it is not itself the susceptibility of factive descent.
