# From Internal Spectrum to Spacetime Physics

The binary information potential generates a beautiful and exactly solvable Witten–Darboux pair, but this is not yet a cosmological perturbation theory. A legitimate lift must construct a conserved covariant response with spatial propagation and constraints; ordinary QFT or the Standard Model can meanwhile be imported as external matter, but that coexistence must not be described as their derivation or recovery.

## Exact internal operator geometry

Take

$$
\mathcal H=L^2(\mathbb R,\mathrm d\theta)
$$

with suitable Sobolev domains, and define

$$
\mathcal A=\partial_\theta+\tanh\theta,
\qquad
\mathcal A^\dagger=-\partial_\theta+\tanh\theta.
$$

Then

$$
\mathcal H_-=\mathcal A^\dagger\mathcal A
=-\partial_\theta^2+1-2\operatorname{sech}^2\theta,
$$

$$
\mathcal H_+=\mathcal A\mathcal A^\dagger
=-\partial_\theta^2+1.
$$

The normalized zero mode is

$$
\psi_0(\theta)=\frac1{\sqrt2}\operatorname{sech}\theta,
$$

so

$$
2|\psi_0|^2
=G^{\rm BKM}_{\theta\theta}.
$$

The continuum begins at $E=1$ and is reflectionless. A convenient scattering solution is

$$
\psi_k(\theta)
=(-ik+\tanh\theta)e^{ik\theta},
\qquad R(k)=0.
$$

There is also a non-normalizable threshold solution proportional to $\tanh\theta$ at $E=1$. Any Levinson-theorem count must state the parity and phase conventions and how this threshold resonance is treated.

These facts are **[ALGEBRA]** after the binary reduction. Their common $\operatorname{sech}^2$ profile is one factorization viewed in several registers, not several independent confirmations.

## The categorical boundary

The variable $\theta$ is an internal coordinate on a family of states. It is not cosmic time, conformal time, a spatial coordinate, or a field amplitude unless an additional map is constructed. Likewise:

- the scattering label $k$ is not comoving momentum;
- reflectionlessness is not causal propagation through spacetime;
- positivity of $\mathcal H_-=\mathcal A^\dagger\mathcal A$ is not absence of spacetime ghosts;
- the Witten index is not four-dimensional chirality, a Weyl fermion, or physical supersymmetry;
- a single internal bound state does not count scalar cosmological degrees of freedom.

These are type errors, not merely missing numerical factors.

## The response map to be constructed

The missing object may be written schematically as

$$
\delta T^X_{ab}
=\mathcal R_{\Sigma,ab}
[\delta\omega,\delta g,\delta\Sigma;\omega,g].
$$

Whether $\mathcal R_\Sigma$ is derived from an action, an influence functional, a Ward identity, an algebraic response theorem, or a natural-operator classification should remain open. An action is not mandatory in principle, but refusing action-based completions in advance would be an unnecessary restriction.

At minimum, the lift must provide:

1. a covariantly conserved $T^X_{ab}$ and its background limit;
2. gauge-invariant scalar, vector, and tensor perturbation variables;
3. lapse/shift constraints or the equivalent covariant constraint algebra;
4. spatial-gradient operators and characteristic cones;
5. hyperbolicity and a well-posed initial-value problem;
6. absence of negative-kinetic-energy and gradient instabilities;
7. regular evolution through $w_X=-1$;
8. coupling to matter, radiation, and metric perturbations;
9. initial-state prescriptions and an arrow of time;
10. CMB, lensing, growth, and other transfer functions.

The background pressure inferred from

$$
\rho_X'=-3(1+w_X)\rho_X
$$

does not supply these data. In particular, a crossing of $w=-1$ is harmless as a smooth prescribed background function but can be singular in simple single-field or barotropic completions. The lift must specify entropy perturbations, extra degrees of freedom, a nonlocal response, or another mechanism that keeps the physical variables regular.

## Useful no-go results

Several negative results prevent the internal pair from being attached to the first available perturbation equation:

- the standard smooth-dark-energy matter-growth equation contains Hubble friction and matter terms and is not the Pöschl–Teller operator;
- the response density itself is not a wave potential until a spacetime kinetic operator is defined;
- a reflectionless one-dimensional potential does not determine retarded support or signal speed;
- factorization in $\theta$ does not determine the sign of a Lorentzian kinetic term.

These failures are productive. They say that the spacetime lift, if it exists, must be a genuinely new response map rather than a relabeling of standard growth.

## The strongest plausible lift conjecture

**[CONJECTURAL ROUTE — covariant Witten lift]** The horizontal modular Hessian may be the radial or normal part of a covariant causal-response operator whose constraints remove one partner sector, leaving a single protected collective mode and transparent internal transport.

For this to be more than spectral resemblance, one must derive:

$$
\mathcal D_{\rm spacetime}
\longrightarrow
\mathcal H_-
$$

under a controlled symmetry reduction, with the same inner product, boundary conditions, and degree-of-freedom count. The internal zero mode should then map to a gauge-invariant spacetime observable, and the continuum label should acquire a physical relation to frequency or momentum.

**Upgrade condition:** a conserved Lorentzian system satisfying the ten requirements above reduces to the displayed pair in a declared sector.

**Failure condition:** no natural conserved response map exists, or every lift is unstable or acausal.

## QFT as input versus QFT as output

There are two legitimate programme choices.

### External-fiber route

Take renormalized GR plus the Standard Model as established local physics and add a wall response that decouples in tested local regimes:

$$
\Gamma_{\rm eff}[g,\Psi;\mu]
=\Gamma_{\rm GR+SM}^{\rm ren}[g,\Psi;\mu]
+\Delta\Gamma_{\rm wall},
$$

with

$$
\Delta\Gamma_{\rm wall}\longrightarrow0
$$

for local laboratory processes, or with an algebraic analogue stating convergence of local nets, states, and correlators. This would establish **compatibility and decoupling**, not derive the Standard Model.

### Reconstruction route

Claiming that QFT or the Standard Model emerges requires much more. A recovery theorem must address:

- locality or microcausality;
- unitarity, or reflection positivity in a Euclidean construction;
- a conserved stress tensor and gravitational Ward identities;
- gauge and BRST structure;
- the $SU(3)\times SU(2)\times U(1)$ algebra and its representations;
- chiral fermions and Yukawa couplings;
- gauge, gravitational, and relevant global anomaly cancellation;
- renormalization, counterterms, and scale dependence;
- convergence of accessible correlators and scattering amplitudes to the Standard Model regime.

No such recovery currently exists. The optional programme in [[symmetry-groups-select/entry|symmetry groups select]] may suggest routes through algebraic reconstruction or finite spectral geometry, but a possible route is not a derivation.

The weaker external-fiber interface and its exact-versus-conjectural boundary are developed in [[causal-wall-spectral-theory/causal-scale-interface|the causal-scale interface]] and [[compatible-with-existing-physics/entry|compatibility with existing physics]].

## A sensible near-term boundary

The minimal credible completion does not need to explain all particle physics. It may instead:

1. import GR+SM as the tested local sector;
2. derive a covariant, stable wall response;
3. show that the response decouples locally and couples consistently to the renormalized stress tensor;
4. calculate growth, lensing, and CMB observables.

That would make Causal Scale Dynamics a physical cosmological extension. A deeper QFT/SM reconstruction could remain a separate, more ambitious module rather than a prerequisite smuggled into the background claim.
