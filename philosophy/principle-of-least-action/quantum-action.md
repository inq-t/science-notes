# Quantum Action

Quantum theory changes the meaning of action. In the path-integral formulation, nature does not select one least-action history. Every allowed history contributes an amplitude whose phase is set by [[classical-action|classical action]]. Stationary action reappears as a semiclassical interference effect, while distinct quantum variational principles govern state evolution and quantum-corrected mean fields.

## Sum over histories

For a particle propagating from $(q_i,t_i)$ to $(q_f,t_f)$, the formal path integral is

$$
K(q_f,t_f;q_i,t_i)
=\int_{q(t_i)=q_i}^{q(t_f)=q_f}
\mathcal Dq\;
e^{\tfrac{i}{\hbar}S[q]}.
$$

The integrand has unit-magnitude phase in this schematic Lorentzian expression. Paths are not assigned ordinary classical probabilities and then optimized. Their complex amplitudes add, and probabilities are obtained only after amplitudes have been combined and the appropriate measurement rule applied.

For quantum fields the corresponding generating functional has the schematic form

$$
Z
=\int\mathcal D\phi\;
e^{\tfrac{i}{\hbar}S[\phi]}.
$$

Sources, boundary or initial states, normalization, gauge fixing, and regularization must be added for a usable theory.

## How classical action emerges

Expand around a stationary history $q_{\mathrm{cl}}$:

$$
q=q_{\mathrm{cl}}+\eta,
\qquad
S[q]
=S[q_{\mathrm{cl}}]
+\frac12\delta^2S[\eta,\eta]
+\cdots,
$$

because

$$
\delta S[q_{\mathrm{cl}}]=0.
$$

When action differences among nearby macroscopic histories are large compared with $\hbar$, the phase oscillates rapidly. Contributions far from stationary histories tend to cancel, whereas neighborhoods of stationary histories add coherently enough to dominate an asymptotic stationary-phase expansion.

This is the core relation between quantum and classical action, with qualifications:

- More than one classical saddle may contribute and interfere.
- A stationary path can be a saddle rather than a minimum.
- Tunneling and instanton effects have no ordinary real-time classical trajectory connecting the relevant regions.
- Decoherence and coarse graining are usually needed to explain why a particular quasiclassical history can be treated probabilistically.
- The classical limit is not captured by the slogan “set $\hbar$ to zero” without specifying scales, states, and observables.

## Euclidean action

After a justified Wick rotation $t=-i\tau$, a Lorentzian integral may become schematically

$$
Z_E
=\int\mathcal D\phi\;
e^{-S_E[\phi]/\hbar}.
$$

The exponential resembles a Boltzmann weight, so minima of a positive Euclidean action can dominate a semiclassical approximation. This is one bridge from quantum field theory to the ensembles and potentials underlying [[thermodynamic-equilibrium|thermodynamic variational principles]].

It is not a universal least-action theorem. Wick rotation may be obstructed, the Euclidean action may be unbounded or complex, the measure and contour matter, and relevant saddles can have negative modes. Euclidean gravity's conformal-factor problem is a prominent warning.

## A variational principle for the quantum state

Schrödinger evolution itself can be written as a stationary-action condition. A common form is

$$
S_\psi
=\int_{t_1}^{t_2}
\left\langle\psi(t)\left|
i\hbar\frac{\mathrm d}{\mathrm dt}-\hat H
\right|\psi(t)\right\rangle\mathrm dt,
$$

with suitable endpoint, normalization, and reality conventions. Independent allowed variations of the bra and ket yield the Schrödinger equation and its adjoint.

If $|\psi(t)\rangle$ is restricted to a trial family, the same idea gives time-dependent variational approximations. The resulting motion is the best within that chosen manifold according to the selected variational rule; it is not exact unless the family is dynamically closed.

This state-space action is conceptually different from summing over configuration-space histories, even when the formulations are mathematically equivalent in an appropriate regime.

[[algebra/quotient-clock-and-stationary-action|A quotient-clock construction]]
reverses the order within this register: a declared one-sided process and
complex positive realization determine the unitary quotient and its
generator, from which a real state action and its stationary equation
follow. The [[directed-analytic-realization/inq|analytic-tail member]] works
this out without an independently appended Hamiltonian. It does not derive
the four-dimensional configuration-space action or its integration measure.

## The quantum effective action

The effective action $\Gamma[\bar\phi]$ is a functional of a mean or classical field $\bar\phi$, obtained from the generating functional by a Legendre transform. Its stationarity equation,

$$
\frac{\delta\Gamma}{\delta\bar\phi}=0,
$$

is the quantum-corrected field equation for the specified states and boundary conditions. In a loop expansion,

$$
\Gamma[\bar\phi]
=S[\bar\phi]
+\hbar\,\Gamma_1[\bar\phi]
+\hbar^2\Gamma_2[\bar\phi]
+\cdots.
$$

Unlike a simple classical action, $\Gamma$ generally contains nonlocal terms and scale-dependent couplings. An in--out effective action is tailored to scattering amplitudes and can yield complex or acausal-looking equations if misused for real-time expectation values. Nonequilibrium evolution usually calls for an in--in, or closed-time-path, effective action.

## The action is not the whole quantum theory

Specifying a classical-looking action is necessary in many quantum field theories but not sufficient to define them. One must also specify or control:

- the field content and state or boundary conditions,
- the functional measure and integration contour,
- gauge fixing and ghost determinants for redundant variables,
- regularization and renormalization,
- unitarity, locality, and stability,
- possible anomalies that spoil a classical symmetry of the action,
- and the observables whose amplitudes or expectation values are being computed.

Two classically equivalent actions can also differ quantum mechanically if a field redefinition changes the measure, a boundary term changes a topological sector or phase, or an anomaly is present.
