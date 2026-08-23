# Claim Audit

Version 3 has a sound exact core and substantially better epistemic discipline than versions 2.0--2.1, but it still promotes several conditional bridges to “exact” status too early. The safest verdict is: exact Fourier and scaling identities; an exact regularized BKM lemma; a conditional holographic representation; and an unconstructed causal-wall, spacetime, and local-QFT interface.

## Direct compatibility verdict

The proposal is **not flagrantly at odds with prevailing physics** when read as a global state/interface programme that imports ordinary QFT, GR constraints, and Einstein--Boltzmann transfer. Most of its current technical content either reformulates an inverse covariance, uses standard information geometry, or selects a known holographic cosmology representation.

It **does not recover QFT or the Standard Model as a limit**. No action, algebraic functor, or correlator theorem shows that the complete framework reduces to

$$
SU(3)_c\times SU(2)_L\times U(1)_Y
$$

with the Standard Model's chiral representations, Yukawa sector, gauge and BRST Ward identities, anomaly cancellation, renormalization, scattering amplitudes, and curved-spacetime stress tensor. If the intended theory is only an interface around QFT, it need not derive those structures, but it must define the interface and prove their local recovery and decoupling. That weaker burden also remains open.

## Exact or standard pieces

The following statements survive the audit in their stated domains:

- On the physical invertible subspace,

  $$
  \mathcal K_\zeta=P_\zeta^{-1}
  =\frac{k^3}{2\pi^2\Delta_\zeta^2}
  $$

  is an exact definition of inverse covariance. Its identification with the quadratic coefficient of a raw probability density is exact for a Gaussian and with a 1PI Hessian in general.
- For a regular finite or controlled exponential family, each orientation of relative entropy has BKM Hessian, and the symmetrized divergence has Hessian $2G^{\mathrm{BKM}}$.
- In the three-dimensional stress decomposition used by v3, trace contraction gives $\langle TT\rangle=4B$.
- Local counterterms polynomial in momentum have zero discontinuity across a spectral cut.
- With the holographic response coefficients defined as in [[spectral-dictionary]], all conversions among $\Delta_\zeta^2$, $\mathcal K_\zeta$, $\mathcal I_\zeta$, $c^{(0)}$, $c^{(2)}$, and $r$ are algebraically correct.
- Homogeneity, isotropy, positivity, weight zero, and exact dilation covariance force $\mathcal K_\zeta=C|k|^3$ in flat three-dimensional space.
- For the standard critical fractional operator on a round $S^3$ with the stated filling,

  $$
  P_3Y_{\ell mn}=R^{-3}\ell(\ell+1)(\ell+2)Y_{\ell mn}.
  $$
- The tilt and running identities follow by logarithmic differentiation, and $\alpha_s=0$ follows exactly inside the constant-exponent member because that member assumes a constant exponent.
- The scalar calibration, tensor ratios, Einstein-member relations, and numerical receipts in v3 reproduce.
- The leading relation between a cubic 1PI vertex and a connected three-point function is correct at the order stated.

These results validate internal normalization and mathematical typing. They do not validate the physical premises that select the kernels.

## Conditional established frameworks

Several pieces are established in the literature only after substantive hypotheses are supplied:

| Claim | Required domain |
|---|---|
| McFadden--Skenderis scalar and tensor formulas | A domain-wall/cosmology dual, gauge/gravity dictionary, simultaneous continuation of momentum and theory parameters, renormalization, and a state/vacuum prescription |
| [[critical-kernel|Curved $P_3$ precision]] | A suitable conformal filling or scattering construction, a self-adjoint domain, a controlled kernel, and positivity on the selected physical subspace |
| Trace response vanishes at a fixed point | An improved conformal stress tensor, no relevant anomaly/boundary/virial contribution, and regular operator mixing and correlators |
| Superhorizon conservation | A gauge-invariant curvature variable, covariant stress conservation, negligible gradients, and vanishing total nonadiabatic pressure |
| Acoustic coherence | A passive growing mode, suitable initial conjugate momentum, no active incoherent source, and consistent matching to ordinary transfer |
| Squeezed $f_{\mathrm{NL}}$ relation | A local adiabatic single-clock attractor, the appropriate state, and its dilation Ward identity |

These are legitimate member constructions, not universal consequences of positivity or causal-scale language.

## Load-bearing unproved identifications

### The wall variable is not yet cosmological curvature

As detailed in [[cosmological-descent]], the decomposition $-\delta\ln\sigma=\delta N+\zeta_{\mathrm{wall}}$ does not supply the inhomogeneous residue's gauge transformation, constraints, kinetic term, physical slicing, or equality with the conserved curvature perturbation. All use of the observed scalar spectrum and transfer functions depends on this missing spacetime lift.

### BKM, Euclidean, spectral, and probability kernels differ

The exact proposition proves

$$
\operatorname{Hess}\mathscr J=2G^{\mathrm{BKM}}
$$

for the selected state family. It does not prove

$$
G^{\mathrm{BKM}}_{TT}
=\text{Euclidean }\langle TT\rangle
=\text{continued spectral kernel}
=\tfrac12\mathcal K_\zeta.
$$

Generic BKM, Euclidean, Wightman, retarded, and spectral correlators differ by state-dependent modular or KMS kernels. Symmetrizing relative entropy matches the desired factor of two numerically; reverse relative entropy is not thereby the complex-conjugate wavefunctional. [[information-geometric-weld|The BKM-to-wavefunctional map]] and the probability/1PI identification remain the central theorem target.

### The holographic dictionary is not universal

The pure algebra in [[spectral-dictionary|the spectral dictionary]] is exact. Applicability of the dictionary is conditional on the holographic cosmology class. Version 3's $+\operatorname{Im}B(-k^2-i0)$ convention also needs an explicit relation to the published continuation, which is commonly written with $-\operatorname{Im}B(-ik)$ after other parameters are continued. A branch label alone does not construct that relation.

### “The wall” still changes type

The observer-region algebra, a codimension-two cut or null horizon sector, and a three-dimensional Euclidean QFT are different objects. Their dimensions, signatures, observables, and state notions differ. [[causal-scale-interface|The interface]] must provide the maps among them, and states at different scales must be transported to a common algebra before a Connes cocycle or relative entropy is defined.

### Rank one is under-specified

One binary generator, one common material clock, and one spin-zero stress channel are three separate rank-one statements. Even the common-clock ansatz removes relative isocurvature only; eliminating intrinsic nonadiabatic pressure and fixing coherent initial phases requires further dynamical assumptions.

### Positivity of one two-point kernel is insufficient

A positive $\mathcal K_\zeta$ does not prove reflection positivity of a Euclidean theory, unitarity or locality of its Lorentzian reconstruction, consistent Ward identities, higher-point factorization, causal propagation, or stability. No covariant perturbation action or constraint algebra currently supplies those tests.

## Claims that need narrower wording

| v3 wording or implication | Corrected status |
|---|---|
| “Exact holographic spectral dictionary” | Established only within a specified domain-wall/cosmology member and its full continuation; the subsequent normalization algebra is exact. |
| Symmetrized relative entropy is “the correct normalization” | It is a consistent proposed normalization that repairs the coefficient; correctness as a cosmological probability kernel awaits the weld. |
| The discontinuity is “precisely” the quotient by contacts | Local polynomials lie in its kernel; equality of the whole kernel with local contacts needs dispersion, analyticity, and growth assumptions. |
| $P_3$ is the curved critical precision | It is a natural filling-dependent conformal representative; positivity, domain, kernel, and running need construction. |
| Rank one yields $\delta p_{\mathrm{nad}}=0$ | A common clock eliminates relative entropy modes; intrinsic entropy and matter dynamics require additional assumptions. |
| Rank one yields coherent transfer | Coherence also needs the passive growing mode, initial-momentum selection, no active source, and consistent matching. |
| The general formulation is falsifiable | Only a specified member, microscopic weld, or calculated response is falsifiable; arbitrary positive response functions can fit arbitrary positive spectra. |
| The scalar target is “exactly” a stress spectral response | It is exactly an inverse covariance; stress-spectral typing is conditional on the holographic representation. |
| “Non-stochastic” is a physical completion | It is an ontological reinterpretation unless it supplies a distinct state construction and measurement theory. |
| QFT is left alone | This is a scope choice, not a local-QFT recovery or decoupling theorem. |

## Corrections retained from v3

Version 3 correctly rejects or repairs the following v2/v2.1 claims, which should not be revived:

- first Weyl variation does not prove an exponential state family;
- abelianization does not make every BKM, Euclidean, and Lorentzian correlator coincide;
- $c^{(0)}$ is not automatically a central charge or a large-$N$ count;
- there is no derived universal $1/\sqrt{c^{(0)}}$ non-Gaussianity floor or $|f_{\mathrm{NL}}|\gtrsim1$ exclusion;
- no universal $n_t=\mathcal O(\delta^2)$ follows for the general wall class;
- no universal $|\alpha_s|\lesssim\delta^2$ follows without a microscopic flow;
- comparing Planck and ACT best-fit tilts does not estimate running;
- higher derivatives of relative entropy are not cosmological cumulants;
- quotienting constants does not by itself prove metric block diagonality;
- the fixed-point null precision must be quotiented before inversion.

The v3 referee disposition accurately records most of these improvements and explicitly acknowledges that the wall map and weld remain unproved. Its residual overreach is narrower: it asserts that the continued BKM trace kernel contributes $4\rho_B$ without deriving the selected BKM-to-Euclidean/wavefunctional map, and it describes the holographic formula mainly as a matter of conventions rather than a substantive model class.

## Material not promoted from the conversations

- The “grammar of facts” and horizontal-collapse ideas in `convo/04` remain philosophical programme statements; no definition of fact, record, outcome, or irreversible dynamics has been constructed.
- The vacuum/gravity exercise in `convo/05` belongs to an adjacent module. The compactness identity $\mathcal I_B/\mathcal C_A=r_s/R$ is an algebraic comparison of standard bounds, but it does not derive $G$. Central shifts of a fixed-background Hamiltonian are state-invisible, while $C\int\sqrt{-g}$ has nonzero metric variation; trace-free or null projection does not solve the global or radiatively stable vacuum-energy problem.
- Claims about neutrino mass concern possible cosmological inference under a different background. This module derives neither neutrino masses nor a neutrino perturbation likelihood.

## Source and evidence status

- The v3 bibliography contains no inline `\cite` commands. Its references are therefore not tied to individual theorem, dictionary, or data claims in the source. The canonical notes now link the main joints to [[causal-wall-spectral-theory/sources/entry|local primary sources]], while the library records the further references needed to test the open obligations.
- The old JSON receipts and reproduced arithmetic check formulas and numbers only. They cannot validate the wall state, the weld, the duality, or a cosmological likelihood.
- `old-versions/` is superseded technical history. `convo/` records how the interpretation changed; later philosophical agreement is not evidence for a mathematical claim.
- The unrestricted theory still contains the functions $c^{(0)}(k)$, $c^{(2)}(k)$, and all higher vertices. Observational values are calibration targets until those functions are computed independently.

## Repaired statement

The strongest defensible summary is:

> Causal-Wall Spectral Theory identifies inverse scalar covariance as the exact observable target, exhibits a conditional holographic stress-response representation with consistent normalizations, and derives a flat critical $|k|^3$ universality class. A physical causal-wall model exists only after one constructs the common algebra and state family, proves the BKM/continuation/probability weld, identifies the gauge-invariant spacetime mode, computes the scalar, tensor, and higher responses, and recovers local GR plus QFT in their tested regime.
