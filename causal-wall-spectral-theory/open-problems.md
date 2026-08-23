# Open Problems

The programme becomes a physical causal-wall theory only when the scale residue, state geometry, spectral representation, and spacetime evolution are constructed as one compatible system. The original CW--T1--T4 list is useful but too compressed; the dependencies below expose the additional kinematic, analytic, stability, and local-preservation obligations.

## CW--T0: identify the physical scalar

Following [[cosmological-descent|the descent problem]], construct the spacetime meaning of

$$
-\delta\ln\sigma=\delta N+\zeta_{\mathrm{wall}}
$$

and prove the inhomogeneous residue's relation to a gauge-invariant cosmological curvature perturbation. This requires the perturbed physical metric, gauge transformations, lapse/shift constraints, physical phase space, zero-mode treatment, quadratic action or symplectic form, and long-wavelength relation to $\zeta_{\mathrm{cos}}$ or $\mathcal R$.

**Success:** the wall variable has the same normalized two-point observable and causal evolution as the curvature mode used in the CMB transfer equations.

**Failure:** it is pure gauge, an additional propagating scalar with excluded couplings, a constrained variable with a different covariance, or cannot be matched to a conserved curvature mode.

## CW--T1a: construct the scale-indexed observer net

Implement [[causal-scale-interface|the interface data]] by choosing the observer-relative causal regions $D_N$, horizons $\mathcal H_N$, and cuts $\Sigma_N$. Construct

$$
O\longmapsto\mathcal A_N(O)
$$

with isotony, locality, covariance, and an appropriate time-slice property. If the regions or algebras change with $N$, specify inclusions, isomorphisms, or a common standard form.

**Success:** every state comparison used later is defined on one algebra after explicit transport.

**Failure:** no canonical comparison survives changing regions, or the construction violates locality or causal propagation.

## CW--T1b: select the state family

Construct faithful normal states $\omega_N$ with the required microlocal or Hadamard regularity and a physical selection principle. State clearly whether exact KMS behavior, a horizon equilibrium approximation, an adiabatic vacuum, or another condition is used.

**Success:** the family is defined independently of the observed expansion and primordial spectrum, is sufficiently regular for relative modular theory, and admits controlled renormalized stress responses.

**Failure:** the state is selected only by fitting $H(z)$ or $\Delta_\zeta^2(k)$, is nonfaithful on the needed algebra, or has unacceptable ultraviolet behavior.

## CW--T1c: construct horizontal scale comparison

Define the scale-to-state map and its relative modular data,

$$
\Phi:\sigma\longmapsto\omega_\sigma,
\qquad
u_{2:1}(s)=[D\omega_2:D\omega_1]_s.
$$

If a local Weyl perturbation is implemented through relative Cauchy evolution or an Araki perturbation, state its support, domain, and relation to a homogeneous FLRW scale change. Prove or falsify ratio dependence, regularity, and absence of noncentral holonomy.

**Success:** the horizontal tangent is obtained without reconstructing it from the desired cosmological response.

**Failure:** the cocycle is path-dependent in an uncontrolled way, depends on more than the scale ratio, or no global scale action exists.

## CW--T1d: derive any reduced scalar sector

Determine whether the physical horizontal tangent has one generator $Q$, whether $Q^2=1$, and whether other tangents decouple, are constrained, or create observable isocurvature. This is separate from deriving a single cosmological curvature clock and from selecting the spin-zero stress channel.

**Success:** the reduction follows from the full algebra and state rather than being imposed, with controlled errors and a clear infrared regime.

**Failure:** several light noncentral modes survive, the response is nonbinary, or the BKM profile differs from the assumed reduced geometry.

## CW--T1e: identify the state-geometric response

Starting from [[information-geometric-weld|the information-geometric construction]], establish the controlled part of the chain

$$
\operatorname{Hess}\mathscr J_{\mathrm{wall}}
\longrightarrow
G^{\mathrm{BKM}}_{TT}
\longrightarrow
\text{a declared renormalized response object}.
$$

The proof must control type-III algebraic definitions, the operator called $T$, modular/KMS kernels, contact terms, and positivity on the physical quotient. It must state whether the endpoint is a modular susceptibility, Euclidean response, Wightman function, or physical precision; these objects are not interchangeable.

**Success:** the wall Hessian and its response endpoint are well defined and their equality is proved with one declared normalization and domain. If the autonomous interface takes $\mathcal K_\zeta$ as primitive instead, this obligation is replaced by an independent law for that precision and its coupling to GR.

**Failure:** an uncontrolled frequency kernel remains, symmetrized relative entropy is mistaken for a 1PI object, or the response is reconstructed from the target spectrum.

## CW--T1f: build the Lorentzian-to-spectral representation

If the holographic branch is used, relate the observer/horizon structure to the three-dimensional Euclidean QFT used by [[spectral-dictionary]]. Supply the domain-wall/cosmology duality, state, renormalization, simultaneous continuation of momentum and theory parameters, `Disc` orientation, and Lorentzian unitarity or reconstruction conditions. Together with CW--T1e, this must establish

$$
\operatorname{Hess}\mathscr J_{\mathrm{wall,spec}}
=\Gamma_\zeta^{(2)}(k)
=\mathcal K_\zeta(k)
=8\rho_B^{\mathrm{cos}}(k)
$$

with one consistent set of conventions.

**Success:** the scalar and tensor spectral functions are derived representations of the same wall state, and the continued scalar kernel is positive and invertible after the correct physical quotient.

**Failure:** the Euclidean QFT is only an unrelated model with a fitted spectrum, or the continuation violates positivity, reality, causality, or Ward identities.

## CW--T2: compute the scalar response

Calculate $c^{(0)}(k)$ rather than inserting it. The result must explain the leading $|k|^3$ shape classified in [[critical-kernel]], the normalization, the red tilt, and any running or features in a declared range. On curved walls it must specify filling data, operator domain, positivity, and a covariant meaning of running.

At the v3 pivot, the target is

$$
c^{(0)}(k_*)=1.956447\times10^7,
\qquad
k_*=0.05\,\mathrm{Mpc}^{-1},
$$

with the observed slow variation.

**Failure:** a computed microscopic member misses the normalization or shape beyond registered scheme ambiguities, produces an inadmissible fixed-point limit, or retains a freely fitted function.

## CW--T3: compute the tensor response

Calculate $c^{(2)}(k)$ from the same structure, including its normalization, tensor tilt, polarizations, and relation to the physical metric tensor mode. This should predict $r$ rather than merely accommodate its bound.

**Failure:** the tensor mode has a wrong sign or normalization, violates the observed bound, or cannot be embedded in a stable two-polarization Lorentzian metric sector.

## CW--T4: compute higher response

Calculate continued $\langle TTT\rangle$ and higher stress correlators, including semilocal terms and Ward identities. Map them into 1PI probability vertices and then into bispectrum and trispectrum shapes, including exchange terms.

**Failure:** higher correlators violate reflection/spectral positivity, unitarity, locality, factorization, or observational non-Gaussianity bounds. No universal kill threshold should be declared before a microscopic member predicts the relevant shapes.

## CW--T5: construct covariant dynamics and transfer

Complete [[cosmological-descent|the spacetime descent]] by supplying a conserved response tensor or equivalent constrained dynamics that:

- reproduces the proposed scalar covariance and any associated background sector;
- has a regular gauge-invariant scalar, two tensor polarizations, and any declared vector sector;
- is hyperbolic and free of ghosts and gradient instabilities;
- identifies intrinsic and relative entropy perturbations;
- selects the passive growing mode and its initial conjugate momentum;
- matches through any early transition or reheating surface; and
- feeds a standard or explicitly modified Boltzmann system.

Only after this step can the theory claim CMB, lensing, growth, or neutrino-cosmology predictions rather than a primordial spectral ansatz.

## CW--T6: preserve imported local GR plus QFT

Apply [[causal-scale-interface|the conservative-restriction test]]: if local QFT is an imported fiber, prove that the new horizontal structure does not spoil its tested regime. Required checks include:

- microcausality and local covariance;
- conservation of the renormalized stress tensor;
- gauge and BRST Ward identities;
- Standard Model anomaly cancellation and curved-spacetime trace terms;
- constancy of physical masses and dimensionless couplings in local units;
- absence or suppression of Lorentz violation, fifth forces, and equivalence-principle violations; and
- quantitative bounds or a decoupling limit for wall-induced corrections to accessible local correlators.

This is not a demand that the interface derive the Standard Model. It is the minimum proof that “QFT supplies the fibers” defines a consistent conservative extension rather than a slogan. A genuine recovery theorem becomes necessary only if the fiber itself is later claimed to emerge from causal-wall primitives.

## CW--T7: perform reproducible empirical tests

- Declare data releases, likelihoods, nuisance parameters, priors, covariances, and pivot conventions.
- Compare a calculated wall member with a power law and with published holographic-QFT alternatives.
- Test running through one joint extended-model likelihood rather than differences between best-fit tilts.
- Implement the full scalar/tensor dynamics in CLASS, CAMB, or an equivalent solver.
- Publish code and receipts that reproduce theory-to-observable predictions, not only algebraic conversions of measured inputs.

## Scope-indexed falsifiers

| Scope | Falsifier |
|---|---|
| Flat critical member | Leading kernel is not positive and homogeneous of degree three under the stated exact symmetries |
| Chosen curved member | No admissible filling/domain gives the required positive operator |
| Constant-exponent member | Robust nonzero running or resolved primordial features |
| Rank-one passive member | Independent primordial isocurvature, intrinsic entropy, or a continuously active incoherent source |
| Causal-wall weld | The constructed wall Hessian does not yield the continued physical precision |
| Microscopic wall member | Calculated scalar, tensor, or higher responses miss observations or consistency conditions |
| Einstein single-clock member | A measured tensor sector violates its leading consistency relations within their accuracy regime |

An arbitrary positive $c^{(0)}(k)$ is not falsified by a different positive spectrum; it can simply be redefined. Predictive force begins only when the response functions are independently calculated or restricted.

## Completion criterion

Three levels should not be conflated:

1. **Spectral formulation:** define inverse covariance and a conditional holographic representation. Version 3 substantially reaches this level, subject to the sign and domain qualifications in the audit.
2. **Causal-scale interface theory:** complete CW--T0, CW--T1a--T1d, CW--T5, and CW--T6, and give an independent physical law for the precision functional and its coupling to GR. Complete CW--T1e as well if the state geometry is claimed to derive that precision; CW--T1f is not mandatory when a three-dimensional QFT is only an optional representation.
3. **Microscopic response completion:** additionally complete CW--T2--T4 and calculate the observed hierarchy from the wall structure with no freely inserted spectral functions. A holographic member must also complete both CW--T1e and CW--T1f.

The current programme is at level 1. Calling it complete at level 2 or 3 would conceal the very theorem targets that make the proposal scientifically testable.
