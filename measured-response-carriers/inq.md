---
inq.module: "measured-response-carriers"
inq.include:
  - './'
inq.ambient:
  - 'receipts/*.py'
keywords:
  - measured response
  - GNS representation
  - state tangents
  - BKM metric
  - completely positive maps
  - information loss
  - recovery
  - energy comparison
---
# Measured Response Carriers

A state-preserving completely positive operation acts on observables, contracts GNS vectors, and transforms state tangents. The resulting defects have different meanings: an observable or GNS gap is a spectral estimate, while the state-tangent loss is a relative-entropy Hessian. This module constructs those carriers and the maps between them, then isolates the additional conditions needed for parameter geometry, categorical rigidity and physical energy. Exact algebraic and finite-dimensional bridges coexist with source theorems for general von Neumann algebras; physical carrier realization and clock calibration remain separate construction problems.

## Three carriers of one operation

[[measured-response-carriers/measured-operations-and-gns-defects|The measured-operation contract]] declares a von Neumann algebra \(\mathcal A\), faithful normal state \(\omega\), a normal state-preserving UCP map \(\Phi\), and an appropriate adjoint when GNS symmetry is needed.

| Carrier | Object being transformed | Response and its meaning |
|---|---|---|
| Observable algebra | \(a\mapsto\Phi(a)\) | Multiplicative structure, positivity, locality and fixed observables |
| GNS Hilbert space | \(a\Omega_\omega\mapsto\Phi(a)\Omega_\omega\) | For a symmetric map, \(I-V_\Phi\) is a positive dimensionless defect |
| Faithful state tangents | \(X\mapsto\Phi_*X\) | The difference of BKM metrics measures lost infinitesimal distinguishability |

A weighted family of symmetric operations has defect kernel equal to the intersection of its fixed-vector spaces. Vacuum ergodicity removes fixed nonvacuum directions; a positive uniform edge is a further estimate. Even an easily engineered order-one edge does not provide a Hamiltonian.

## The reusable carrier stack

The constructions have the following order:

\[
\boxed{
\begin{aligned}
(\mathcal A,\omega,\Phi)
&\longrightarrow
(\mathcal H_\omega,\Omega_\omega,V_\Phi,D_\Phi),\\
(\mathcal A,\omega,\Phi)
&\longrightarrow
(T_\omega\mathcal S,\mathcal Q_{\Phi,\omega}^{\mathrm{BKM}}),\\
T_\lambda M
&\xrightarrow{\,J_\lambda\,}
T_{\rho_\lambda}\mathcal S,\\
\mathcal K_{\mathrm{phys}}
&\xrightarrow{\,J_{\mathrm{phys}}\,}
\mathcal H_\omega\ \text{or}\ T_\omega\mathcal S,\\
\text{response defect}
&\xrightarrow{\text{same-core comparison}}
\text{clock-energy form}.
\end{aligned}}
\tag{MC25}
\]

Each arrow needs its own domain, kernel and comparison theorem. The state and map select a response; they do not supply the physical analysis \(J_{\mathrm{phys}}\), its coverage or a dimensional yardstick.

## Observable gaps and state-tangent losses

[[measured-response-carriers/observable-bkm-gap-transfer|Operator-monotone gap transfer]] carries a GNS Markov gap to the observable BKM norm under the source theorem's faithful invariant-state and exponential-contraction hypotheses; GNS symmetry is not required. This addresses the observable score. [[measured-response-carriers/state-tangent-bkm-bridge|The state-tangent bridge]] separately uses the inverse BKM metric on density perturbations. In finite dimensions, its modular factor gives a canonical GNS realization; a Type-III score map still needs a tangent domain, intertwining and adequate range.

[[measured-response-carriers/descent-loss-cocycle-and-recovery-fork|The descent-loss cocycle]] makes this distinction consequential. Data-processing losses add with transported arguments, but a preserving expectation's loss is vertical: it vanishes on recovered directions and has zero minimum over lifts of a retained tangent. That loss therefore cannot become retained stiffness merely by quotienting. Jointly transverse comparisons require their own lower frame.

## Pullbacks determine what a model can see

[[measured-response-carriers/response-pullbacks-and-radicals|Response pullbacks]] explain parameter Hessians: a readout derivative \(J_\lambda\) pulls a positive target metric back to the parameter space, with radical \(\ker J_\lambda\). Metric descent to a quotient and preservation of a Hessian structure impose different geometric conditions. A finite collection of finite-dimensional readouts cannot frame an infinite-dimensional physical vacuum complement; a suitably complete family must instead be constructed.

[[binary-information-geometry/inq|Binary information geometry]] supplies a commutative one-parameter example. Its Witten--Darboux operator appears after a separate half-density unitary changes the weighted logistic probability carrier. [[hessian-response-geometry/inq|Hessian response geometry]] supplies the affine and integrability conditions under which parameter responses share a Hessian potential. Neither construction determines an energy interpretation from coordinate entries of a Hessian.

## Symmetry and positive transport require explicit maps

[[measured-response-carriers/descent-and-clock-arrows|Descent and clock arrows]] separates nonfaithful realization across registers from reversible evolution within a realized algebra. Categorical gluing, a CP dilation and an isometric defect completion have different effects on what is retained. [[measured-response-carriers/closed-form-carrier-transport|Closed-form carrier transport]] specifies when a positive form crosses an invertible carrier map, which spectrum is preserved by a unitary map, and when lower bounds survive a more general comparison.

[[measured-response-carriers/normalized-fusion-actions|Normalized fusion actions]] add an algebraic representation on the GNS carrier. Tube admissibility is an additional hypothesis before categorical property \((T)\) applies; identifying the invariant subspace with the vacuum line is another. [[categorical-gauge-response/inq|Categorical gauge response]] must realize these data on the neutral gauge-observable carrier. The abstract fusion identity supplies neither that realization nor the physical clock.

[[measured-response-carriers/lazification-and-clock-calibration|Lazification]] replaces a self-adjoint contraction by a positive contraction and halves its defect. An injective result has a logarithmic generator, possibly unbounded. To call it physical energy requires a proved transfer or direct energy realization and an independently calibrated duration.

## From response to physical energy

[[measured-response-carriers/response-to-energy-comparison|The response-to-energy theorem]] chains three independent estimates on a complex form core of the full physical vacuum complement: response coercivity \(\kappa\), a physical analysis lower frame \(b_J\), and a normalized energy comparison \(\eta_{\mathrm{sol}}E_*\). It gives
\[
\Delta_E\ge\eta_{\mathrm{sol}}E_*\kappa b_J.
\]
A response gap modulo a kernel requires a lower frame modulo that same kernel. The coefficient \(E_*\) must be selected without fitting the desired gap.

[[physical-response-coercivity/inq|Regional and causal response constructions]] address complete physical coverage and the independent energy comparison. [[general-causal-action/carrier-first-reversal|The carrier-first reversal]] asks for these estimates on the full vacuum carrier. [[transported-response-observability-solder/inq|Transported response observability]] constructs bounded analyses \(\sqrt\eta(I-e^{-\tau G})^{1/2}\) from a closed response and studies when their transported lower frame forces a physical transfer product to contract. [[causal-wall-spectral-theory/inq|Causal-wall spectral theory]] instead asks for a change from state response to spatial precision and then a separate Lorentzian field realization. These are distinct construction routes; their localization, coverage, clock and continuum hypotheses cannot be supplied by identifying symbols across carriers.
