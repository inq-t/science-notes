# Entropic Stiffness, Not Entropic Force

The useful inheritance from entropic gravity is not that entropy is a substance which pushes matter. It is that a universal family of state--boundary response laws can reconstruct geometric dynamics, and that the second variation of relative entropy can sometimes coincide with a canonical energy on the same perturbation. For the mass-gap programme this suggests an all-cut stability principle: causal cuts select a complete, dimensionless distinction frame; a separately reconstructed Poincare Casimir charges that frame; and an independent yardstick supplies units. Jacobson provides the universality pattern, holographic canonical energy provides one controlled existence proof for the information-to-energy solder, and Verlinde and Padmanabhan provide useful boundary-first intuitions. None supplies the Yang--Mills carrier, uniform coercivity, or scale.

**Status: [EXACT VARIATIONAL AND NORMALIZATION DISTINCTIONS; CONTROLLED HOLOGRAPHIC PRECEDENT; CONDITIONAL ALL-CUT GAP THEOREM; OPEN YANG--MILLS REALIZATION].** This note imports no stochastic ontology and does not infer a Yang--Mills scale from \(G\), horizon area, Unruh temperature, or cosmic acceleration.

## Four entropic equations with different types

The phrase “entropic gravity” covers several inequivalent constructions:

| Formula | Varies | Output | What it is not |
|---|---|---|---|
| \(\delta Q=T\,\delta S\) | flux through a causal boundary | equilibrium balance | a particle force law |
| \(F\cdot\delta x=T\,\delta S\) | a configuration displacement | virtual work | a state-space metric |
| \(\delta S_{\mathrm{tot}}|_V=0\) | geometry and state at fixed volume | first-order stationarity | a stability modulus or gap |
| \(D''(\rho_t\Vert\rho_0)|_0=g^{\mathrm{BKM}}(X,X)\) | a faithful state tangent \(X=\dot\rho_0\) | dimensionless quadratic distinguishability | physical energy before a solder |

Entropy is therefore not one ontological fluid appearing in four disguises. Each formula has its own carrier, tangent, and codomain. The last row is the one naturally aligned with a spectral-gap inequality because both are quadratic forms, but alignment is not identity.

For a faithful reference state \(\rho_0\), put \(K_0=-\log\rho_0\). Along a normalized differentiable state path,

$$
\left.\frac{\mathrm d}{\mathrm dt}S(\rho_t)\right|_0
=
\left.\frac{\mathrm d}{\mathrm dt}
\langle K_0\rangle_{\rho_t}\right|_0,
\tag{E1}
$$

whereas

$$
D(\rho_t\Vert\rho_0)
=
\frac{t^2}{2}
g^{\mathrm{BKM}}_{\rho_0}(X,X)
+o(t^2).
\tag{E2}
$$

Equation (E1) is the entanglement first law. Equation (E2) is the first nonvanishing relative-entropy remainder after that linear law cancels. A field equation can follow from universal first-order stationarity; a gap requires a positive *uniform second-order modulus*. This is the central upgrade from entropic equilibrium to entropic stiffness.

The global Yang--Mills vacuum is pure, so (E2) is not finite on the full matrix algebra in transverse pure-state directions. [[regional-relative-entropy-frames]] gives the correctly typed repair: first restrict through observable channels to faithful regional output states, then pull their BKM Hessians back to the projective vacuum tangent.

## Jacobson's real contribution is causal tomography

[[vendor/entropic-gravity/jacobson-local-horizon-thermodynamics|Jacobson's local-horizon argument]] imposes the Clausius law at every point and for every local null direction. Raychaudhuri focusing and the assumed entropy-area density give

$$
\left(
R_{ab}
-\frac{2\pi}{\hbar\eta}T_{ab}
\right)k^ak^b=0
\tag{E3}
$$

for every null \(k^a\). Null-direction universality upgrades these scalar contractions to a tensor equation modulo a metric term; Bianchi identity and stress conservation then fix that term up to \(\Lambda\). The power lies neither in the word *entropy* nor in a stochastic microscopic story. It lies in the completeness of the causal test family.

This supplies a direct analogue for the distinction programme:

$$
\{\text{all admissible causal cuts and orientations}\}
\longrightarrow
\{J_W\}_{W\in\mathfrak W}
\longrightarrow
\bigcap_{W\in\mathfrak W}\ker J_W.
\tag{E4}
$$

Point separation, \(\bigcap_W\ker J_W=\{0\}\), is the informational analogue of tensor tomography. A mass-gap proof needs the stronger quantitative statement that the joint map has closed range with a uniform lower bound. Jacobson therefore suggests a principled way to choose the atlas—every admissible causal cut—not the value of that bound.

## The local Unruh law removes a normalization; it does not create a yardstick

In Jacobson's construction the approximate boost field is normalized by an arbitrary \(\kappa\). The matter heat flux and Unruh temperature scale together:

$$
\delta Q_\kappa
=
\kappa\,\delta Q_1,
\qquad
k_BT_\kappa
=
\frac{\hbar\kappa}{2\pi c},
\qquad
\frac{\delta Q_\kappa}{k_BT_\kappa}
=
\frac{\delta Q_1}{k_BT_1}.
\tag{E5}
$$

The cancellation is exactly why an arbitrary local boost normalization can yield a geometric equation. It also proves a no-yardstick result: the dimensionless entropy response determines no absolute \(\kappa\), temperature, energy, or mass scale. The universal \(2\pi\) fixes a dimensionless conversion convention; it cannot by itself produce \(E_*\).

The entropy-area coefficient is likewise supplied:

$$
\eta
=
\frac{k_Bc^3}{4G\hbar}.
\tag{E6}
$$

Jacobson proves that one universal \(\eta\) entails one universal gravitational coupling. He does not calculate \(\eta\) independently of \(G\). For pure Yang--Mills, whose defining problem contains no \(G\), (E6) cannot be the mass yardstick without a separate gravity-decoupling theorem.

## Entanglement equilibrium stops one derivative too early for a gap

[[vendor/entropic-gravity/jacobson-entanglement-equilibrium|Entanglement equilibrium]] uses

$$
\delta S_{\mathrm{tot}}|_V
=
\eta\,\delta A|_V
+\delta S_{\mathrm{IR}}
=0
\tag{E7}
$$

for small balls. For conformal matter, the ball modular Hamiltonian is a local weighted stress-tensor integral, and all-ball stationarity gives the semiclassical Einstein equation at leading order under the stated scale hierarchy. But first-order stationarity says only that the linear term vanishes. It neither proves that the stationary point is a strict maximum nor supplies a norm-uniform Hessian bound.

The mass-gap analogue is not (E7), but a quantitative second-variation statement on every nonvacuum physical tangent. In schematic generalized-entropy language it would be

$$
-\delta^2S_{\mathrm{tot},W}[\Psi]
\geq
\kappa_W\lVert J_W\Psi\rVert_W^2,
\tag{E8}
$$

after gauge directions, edge data, domains, and the sign convention have been fixed. Relative entropy is the safer positive object because its first variation vanishes identically at coincidence and its Hessian is BKM. Equation (E8) is therefore motivation, not a proposed universal identity.

## A same-tangent energy solder really exists in one controlled regime

[[library/canonical-energy-is-quantum-fisher-information/inq|Lashkari and Van Raamsdonk]] show that, for perturbations of a holographic CFT vacuum reduced to a ball and admitting the stated semiclassical AdS Rindler-wedge dual, the regional quantum Fisher form equals bulk gravitational canonical energy in the authors' normalization:

$$
g^{\mathrm{QF}}_B(\dot\rho_B,\dot\rho_B)
\longleftrightarrow
\mathcal E^{\mathrm{grav}}_{R_B}(\delta g,\delta g).
\tag{E9}
$$

This is the most useful entropic-gravity precedent for the mass-gap programme. It proves that “information geometry solders to energetic geometry” can be an actual same-tangent theorem, not merely metaphor. It also teaches three restrictions:

1. the information is retained regional distinguishability, not automatically information erased by a wall;
2. canonical-energy positivity is not a norm-uniform spectral gap; and
3. the AdS/CFT carrier, gravitational normalization, and reconstruction dictionary are essential hypotheses, not consequences of BKM positivity.

The target is therefore to construct a Yang--Mills analogue of the *type* of (E9), not to transplant its gravitational member.

## What Verlinde and Padmanabhan contribute

[[vendor/entropic-gravity/verlinde-entropic-force|Verlinde's screen construction]] contains a philosophically important reversal: a screen separates a region already represented as space from one not yet spatially represented, and gravitational potential is read as a coarse-graining coordinate. This is close to treating space as the presentation of distinctions rather than a container.

Its equations do not yet ground that picture. The probe entropy gradient already contains the test mass,

$$
\Delta S
=
2\pi k_B\frac{mc}{\hbar}\Delta x,
\tag{E10}
$$

the screen count already contains \(G\),

$$
N
=
\frac{Ac^3}{G\hbar},
\tag{E11}
$$

and the equipotential surfaces of the desired potential define the screen family. Moreover, a conservative force admits infinitely many formal \((T,S)\) representations; [[library/conservative-entropic-forces/inq|Visser's analysis]] makes this underdetermination explicit. The useful import is the register—geometry as response of an information-bearing boundary—not the claim that an entropy gradient has independently explained force.

[[library/thermodynamical-aspects-of-gravity-new-insights/inq|Padmanabhan's programme]] contributes a different insight: horizon entropy is naturally a boundary Noether quantity, and gravitational field equations can be recast as thermodynamic or extremal identities for null directions. This reinforces the reversal “boundary balance before bulk geometry.” But the relevant gravitational entropy density and diffeomorphism-invariant dynamics are already supplied. It is a variational architecture, not a derivation of the microscopic ledger or its conversion coefficient.

## Stochastic descriptions provide covariances, not ontology or a gap

Stochasticity is not a common premise of the strongest entropic arguments above. Jacobson's implication is an equilibrium universality argument, and (E9) is a deterministic equality of quadratic forms. In [[library/stochastic-gravity-theory-and-applications/inq|stochastic gravity]], a classical stochastic source is introduced so that its covariance reproduces the stress-tensor noise kernel in the Einstein--Langevin description. The noise kernel is a positive two-point covariance acting on test-tensor perturbations; it is not a selection of one actual history and does not assert that chance is fundamental.

Such a kernel may still be useful. It supplies a principled quadratic form measuring fluctuations visible to geometry, and an influence functional can relate its symmetric noise part to a dissipative response kernel under suitable state and stationarity assumptions. But covariance is not inverse covariance, dissipation is not Lorentzian Hamiltonian evolution, and fluctuation--dissipation does not supply an absolute clock normalization. A noise kernel can become one response fiber in an atlas only after a carrier map, domain, quotient by gauge directions, and energy solder are proved.

## The all-cut entropic-stiffness theorem target

Let \(\mathfrak W_r\) be a regulator-level family of causal cuts, boundary readouts, or gauge-invariant flux contexts fixed independently of the low spectrum. Let \(\mathcal R_{r,W}\) send the physical vacuum state to a faithful output state \(\sigma_{r,W}\), and let \(J_{r,W}\) be its derivative on projective vacuum tangents. Define

$$
\mathfrak d_r[\Psi]
:=
\int_{\mathfrak W_r}
w_r(\mathrm dW)\,
g^{\mathrm{BKM}}_{\sigma_{r,W}}
(J_{r,W}\Psi,J_{r,W}\Psi).
\tag{E12}
$$

The entropic-gravity import is the universality demand: the cut site and normalization are fixed by one causal rule and cover every admissible orientation, rather than being tuned to selected excitations. The two estimates that would matter are

$$
\mathfrak d_r[\Psi]
\geq
\kappa_r\lVert(1-P_{0,r})\Psi\rVert^2,
\qquad
\langle\Psi,\mathcal C_r\Psi\rangle
\geq
\eta_{C,r}E_{*,r}^2\mathfrak d_r[\Psi],
\tag{E13}
$$

where

$$
\mathcal C_r
=
H_r^2-c^2\mathbf P_r^2
\tag{E14}
$$

is the energy-squared Poincare Casimir on the reconstructed physical carrier. By [[joint-causal-generators-and-the-mass-casimir]], (E13) implies

$$
\boxed{
\Delta_{E,r}
\geq
E_{*,r}\sqrt{\eta_{C,r}\kappa_r}.}
\tag{E15}
$$

A continuum theorem requires a positive lower limit of the right-hand side together with carrier, form, vacuum-projection, observable-net, and Poincare reconstruction. The three factors have distinct explanatory roles:

| Factor | Meaning | Forbidden source |
|---|---|---|
| \(\kappa_r\) | completeness/stiffness of the causal distinction atlas | the desired spectrum or fitted correlator |
| \(\eta_{C,r}\) | same-tangent conversion from distinction to invariant clock cost | defining \(\mathfrak d_r\) from \(\mathcal C_r\) |
| \(E_{*,r}\) | common dimensional normalization | measured glueball mass, \(G\), or chosen Unruh acceleration |

This is what survives the entropic-gravity audit. Equilibrium can select equations of state; all-cut second-order stability can, in principle, select a spectral floor. Entropy does not cause mass. Rather, a complete causal algebra may make every realizable nonvacuum distinction carry a positive invariant clock cost, with spatial and gravitational geometry reconstructed as downstream presentations of that response.
