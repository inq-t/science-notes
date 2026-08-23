# Cosmological Descent

Cosmological descent is the map from wall correlation data to the gauge-invariant scalar, tensor, and higher-point observables evolved through the hot universe. Version 3 imports several correct formulas from standard cosmology, but it has not yet shown that its scale residue is the curvature mode entering those formulas or supplied the covariant action, constraints, state matching, and passive initial data needed for the import.

## Kinematic identification comes first

Separate the homogeneous displacement from the wall variable by

$$
-\delta\ln\sigma(x)
=\delta N+\zeta_{\mathrm{wall}}(x)
$$

with the homogeneous mode removed from $\zeta_{\mathrm{wall}}$. The observed scalar power is conventionally assigned to a gauge-invariant curvature perturbation, such as the comoving curvature $\mathcal R$ or the uniform-density curvature $\zeta_{\mathrm{cos}}$.

Equality of symbols is not a derivation:

$$
\boxed{
\zeta_{\mathrm{wall}}
\stackrel{?}{=}
\zeta_{\mathrm{cos}}.}
$$

A proof must specify:

- the perturbed physical metric $g_\sigma$ and how $\delta\sigma$ transforms under spacetime gauge transformations;
- the lapse and shift constraints and the slicing on which $\zeta_{\mathrm{wall}}$ is evaluated;
- the physical scalar degree of freedom after constraints and zero modes are removed;
- its quadratic action or symplectic form, including normalization and causal evolution;
- its relation to the conserved curvature variable in the long-wavelength limit; and
- matching across any non-geometric, reheating, or other transition into standard hot-big-bang evolution.

Without this theorem, the match to the measured $\Delta_\zeta^2$ is a proposed identification rather than a derived observable.

The benchmark is an explicit reduced action after the gravitational constraints have been solved, as in [[causal-wall-spectral-theory/sources/papers/1988-mukhanov-gauge-invariant-cosmological-perturbations.pdf|Mukhanov's gauge-invariant construction]]. A positive wall covariance by itself supplies neither that constrained phase space nor its Lorentzian kinetic term.

## Tensor sector

The three-dimensional stress response has an independent spin-two coefficient $c^{(2)}(k)$. With the conventions in [[spectral-dictionary]],

$$
\Delta_T^2(k)=\frac{32}{\pi^4c^{(2)}(k)},
\qquad
r=8\frac{c^{(0)}}{c^{(2)}}.
$$

The general wall formulation leaves $c^{(2)}(k)$ free. It therefore predicts neither $r$ nor a tensor tilt until one microscopic structure computes that function.

### Einstein single-clock member

In a leading semiclassical Einstein reconstruction with one canonical clock, define

$$
\mathfrak S
:=\frac{8\pi^2M_{\mathrm P}^2}{H^2}
=\frac{\pi}{GH^2},
\qquad
M_{\mathrm P}^{-2}=8\pi G.
$$

The standard leading spectra are

$$
\Delta_\zeta^2=\frac1{\epsilon\mathfrak S},
\qquad
\Delta_T^2=\frac{16}{\mathfrak S}.
$$

Comparison with the registered spectral coefficients gives

$$
\boxed{
c^{(0)}=\frac{4\epsilon\mathfrak S}{\pi^4},
\qquad
c^{(2)}=\frac{2\mathfrak S}{\pi^4},
\qquad
\mathcal I_\zeta=\epsilon\mathfrak S.}
$$

At this order,

$$
r=16\epsilon,
\qquad
n_t=-2\epsilon=-\frac r8.
$$

These are standard member-specific consistency relations. They check the normalization of the spectral dictionary; they do not derive Einstein single-clock inflation from the wall and are not identities of the general class.

## Rank-one descent

Version 3 assumes that every material sector is evaluated at one local clock reading,

$$
\rho_i(x)=\bar\rho_i(N+\zeta(x)).
$$

At linear order,

$$
\delta\rho_i=\bar\rho_i'\zeta.
$$

With a consistent curvature convention, all species then share the same clock displacement and their relative entropy modes vanish:

$$
S_{ij}=3(\zeta_i-\zeta_j)=0.
$$

This is a conditional common-clock result. It is not derived from the one-generator binary quotient or from the existence of the spin-zero stress channel.

Vanishing relative isocurvature also does not alone prove vanishing total nonadiabatic pressure. One additionally needs each relevant sector to be barotropic or on an attractor, no surviving intrinsic entropy perturbation, and a specified treatment of interactions, anisotropic stress, and relative velocities. Under those conditions,

$$
\delta p_{\mathrm{nad}}=0.
$$

Stress-energy conservation then gives the standard long-wavelength relation

$$
\frac{\mathrm d\zeta_{\mathrm{cos}}}{\mathrm dN}
=-\frac{\delta p_{\mathrm{nad}}}{\rho+p}
+\mathcal O\!\left(\frac{k^2}{a^2H^2}\right),
$$

so the physical curvature mode is conserved outside the horizon. This is the familiar theorem of standard cosmological perturbation theory, as in [[causal-wall-spectral-theory/sources/papers/0003278-wands-malik-lyth-liddle-cosmological-perturbations-large-scales.pdf|Wands et al.]], once its hypotheses are satisfied. [[causal-wall-spectral-theory/sources/papers/0302326-weinberg-adiabatic-modes-cosmology.pdf|Weinberg's adiabatic-mode theorem]] separately records the long-wavelength regularity and gauge assumptions needed to identify the physical mode.

## Passive coherent transfer

For a conserved primordial curvature covariance, standard Einstein--Boltzmann evolution gives

$$
C_\ell^{XY}
=4\pi\int\mathrm d\ln k\,
\Delta_\zeta^2(k)
\Theta_\ell^X(k)\Theta_\ell^Y(k).
$$

Acoustic phase coherence requires more than a two-point spectrum. The initial perturbation must be the passive growing mode with the appropriate conjugate momentum or decaying mode suppressed, and there must be no continuously active incoherent source. Reheating or any wall-to-metric transition must preserve the matching conditions. The photon, baryon, neutrino, and dark-matter transfer functions are then inherited from ordinary GR plus local QFT/kinetic theory.

Thus the framework may legitimately leave standard transfer untouched, but only after it supplies the initial gauge-invariant mode and proves the interface conditions. A full Boltzmann implementation cannot be replaced by inserting a measured power law into the usual transfer integral.

## Higher-point descent

Three different derivative hierarchies must remain distinct:

1. source derivatives of $W[\zeta]=\log Z[\zeta]$, which generate connected stress correlators;
2. higher derivatives of relative entropy, which are Bregman combinations and do not equal source cumulants beyond quadratic order; and
3. vertices of the probability 1PI effective action, whose propagator contractions generate connected cosmological correlators.

Write

$$
\Gamma[\zeta]
=\frac12\zeta\mathcal K_\zeta\zeta
+\frac1{3!}\Gamma_3[\zeta^3]
+\frac1{4!}\Gamma_4[\zeta^4]+\cdots.
$$

Cosmological expectation values require a Lorentzian state and an in-in prescription; [[causal-wall-spectral-theory/sources/papers/0506236-weinberg-quantum-contributions-cosmological-correlations.pdf|Weinberg's in-in construction]] is the relevant standard benchmark. A Euclidean Hessian does not select that contour or state by itself. The holographic three-point dictionary and its semilocal terms are worked out by [[causal-wall-spectral-theory/sources/papers/1104.3894-mcfadden-skenderis-cosmological-three-point-correlators.pdf|McFadden and Skenderis]], with a controlled near-CFT realization in [[causal-wall-spectral-theory/sources/papers/1211.4550-bzowski-mcfadden-skenderis-holography-inflation-cpt.pdf|Bzowski, McFadden, and Skenderis]]. Those results do not supply CWST's missing state-to-vertex weld. At leading order in nonquadratic vertices,

$$
\boxed{
\langle\zeta_1\zeta_2\zeta_3\rangle_c
=-\mathcal C_1\mathcal C_2\mathcal C_3
\Gamma_3(1,2,3)+\cdots,}
$$

where $\mathcal C=\mathcal K^{-1}$ on the physical subspace. The four-point function contains both a dressed $\Gamma_4$ term and exchange contributions with two $\Gamma_3$ vertices. A holographic calculation of $\Gamma_3$ requires the continued $\langle TTT\rangle$ response and the necessary semilocal terms; it is not the third derivative of symmetrized relative entropy.

The large numerical value of $c^{(0)}$ does not establish large-$N$ factorization because $c^{(0)}$ is a beta-weighted spin-zero response, not automatically the central charge that controls all normalized correlators. Consequently neither a universal $1/\sqrt{c^{(0)}}$ non-Gaussianity floor nor a universal $|f_{\mathrm{NL}}|\gtrsim1$ exclusion follows.

If the standard local single-clock attractor, adiabatic vacuum, locality, and dilation Ward identity are separately assumed, the squeezed relation is

$$
f_{\mathrm{NL}}^{\mathrm{sq}}
=\frac5{12}(1-n_s).
$$

This is a conditional single-clock member result, familiar from the single-field consistency relation of [[causal-wall-spectral-theory/sources/papers/0210603-maldacena-non-gaussian-features-single-field-inflation.pdf|Maldacena]], not a theorem of positive spectral typing. The broader soft relations require the adiabatic-mode Ward identities and their assumptions, as organized by [[causal-wall-spectral-theory/sources/papers/1304.5527-hinterbichler-hui-khoury-ward-identities-adiabatic-modes.pdf|Hinterbichler, Hui, and Khoury]].

## What remains to descend

| Layer | Present status |
|---|---|
| Wall residue $\to$ gauge-invariant scalar | Open spacetime and constraint theorem |
| Scalar two-point normalization and tilt | Imported observational target until $c^{(0)}(k)$ is computed |
| Tensor spectrum | Open function $c^{(2)}(k)$ outside the Einstein member |
| Adiabaticity | Common-clock ansatz plus additional intrinsic-entropy assumptions |
| Conservation and coherence | Standard conditional theorems after passive-mode and matching data are supplied |
| Higher points | Correct mathematical slots identified; stress vertices uncomputed |
| Stability and causality | No covariant quadratic action, kinetic matrix, sound cones, or hyperbolicity proof |

The descent is complete only when these layers are derived from one compatible wall/metric state rather than assembled from measured initial data and standard downstream evolution.
