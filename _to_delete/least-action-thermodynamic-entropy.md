# Thermodynamic and Entropic Variational Principles

Thermodynamics contains powerful extremum principles, but there is no single unrestricted “least thermodynamic action.” At equilibrium, entropy is maximized or an appropriate thermodynamic potential is minimized under clearly stated environmental constraints. Out of equilibrium, variational descriptions exist only with additional constitutive, stochastic, or near-equilibrium assumptions.

## Equilibrium: entropy maximum

For an isolated system with fixed internal energy $U$, volume $V$, and particle numbers $N_a$, stable equilibrium maximizes thermodynamic entropy:

$$
\delta S_{\mathrm{th}}=0,
\qquad
\delta^2S_{\mathrm{th}}<0
$$

for permitted nontrivial variations near a strict stable equilibrium. The first condition identifies a candidate equilibrium; the concavity or second-variation condition supplies stability.

For example, let two subsystems exchange energy while their total energy is fixed. With $U_2=U-U_1$,

$$
S_{\mathrm{tot}}(U_1)
=S_1(U_1)+S_2(U-U_1).
$$

Stationarity gives

$$
\frac{\partial S_1}{\partial U_1}
=\frac{\partial S_2}{\partial U_2},
$$

and because $1/T=\partial S/\partial U$, the equilibrium condition is $T_1=T_2$. Entropy maximization is therefore a compact way to derive the equality of intensive variables subject to conservation constraints.

## The environment selects the potential

Legendre transforms replace constrained entropy maximization by minimization of the potential natural to the quantities controlled by the environment.

| Controlled variables | Stable-equilibrium principle | Potential |
|---|---|---|
| $U,V,N_a$ | Maximize entropy | $S_{\mathrm{th}}$ |
| $S_{\mathrm{th}},V,N_a$ | Minimize internal energy | $U$ |
| $T,V,N_a$ | Minimize Helmholtz free energy | $F=U-TS_{\mathrm{th}}$ |
| $T,P,N_a$ | Minimize Gibbs free energy | $G=U-TS_{\mathrm{th}}+PV$ |
| $T,V,\mu_a$ | Minimize grand potential | $\Omega=U-TS_{\mathrm{th}}-\sum_a\mu_aN_a$ |

These statements apply to the appropriate stable equilibrium and admissible variations. Phase coexistence, metastability, long-range forces, nonconcave entropy, and finite-size effects can complicate the global-extremum picture.

## Statistical-mechanical origin

In equilibrium statistical mechanics, entropy is a functional of a probability distribution. For discrete microstates,

$$
S[p]=-k_B\sum_i p_i\ln p_i.
$$

Maximizing $S[p]$ subject to normalization and a fixed mean energy gives the canonical distribution,

$$
p_i=\frac{1}{Z}e^{-\beta E_i},
\qquad
Z=\sum_i e^{-\beta E_i}.
$$

The Lagrange multipliers encode the imposed constraints. Without the mean-energy constraint, maximum entropy would instead produce the uniform distribution over the allowed states. “Maximum entropy” is therefore an inference or equilibrium rule only after the state space, measure, and constraints are supplied.

Equivalently, for fixed temperature the canonical distribution minimizes the nonequilibrium free-energy functional

$$
\mathcal F[p]
=\sum_i p_iE_i
+k_BT\sum_i p_i\ln p_i.
$$

The difference from the equilibrium value is

$$
\mathcal F[p]-F_{\mathrm{eq}}
=k_BT\,D(p\|p_{\mathrm{eq}})\ge0,
$$

where $D$ is relative entropy. This is a precise minimum principle, not merely an analogy.

## The second law is not a least-action law

For an isolated macroscopic system, the second law states

$$
\Delta S_{\mathrm{th}}\ge0
$$

for an allowed process, or $\dot S_{\mathrm{tot}}\ge0$ in a suitable local description. It supplies an arrow and an inequality. It does **not** generally say that the realized irreversible history maximizes total entropy production, minimizes entropy production, or extremizes the time integral of entropy.

Those stronger claims require a separately derived regime and functional. Far-from-equilibrium systems may form patterns, sustain currents, and depend on kinetic details not fixed by state-function thermodynamics alone.

## Near-equilibrium dissipation principles

In linear irreversible thermodynamics, fluxes $J_a$ are linearly related to thermodynamic forces $X_b$:

$$
J_a=\sum_bL_{ab}X_b.
$$

Under microscopic reversibility and suitable variable parities, the kinetic coefficients satisfy Onsager reciprocity. When the symmetric dissipative matrix is positive, the linear constitutive law can often be expressed as a local variational problem.

For overdamped variables $x$, one common form minimizes the **Rayleighian** over instantaneous rates:

$$
\mathcal R(\dot x)
=\frac12\dot x^{\mathsf T}\zeta\dot x
+\nabla F\cdot\dot x.
$$

Stationarity gives

$$
\zeta\dot x=-\nabla F.
$$

This is a least-dissipation or Onsager variational structure under specific linear-response assumptions. It is local in time and depends on the friction operator $\zeta$; it is not [[classical-action|Hamilton's principle]] with entropy substituted for mechanical action.

Prigogine's minimum-entropy-production theorem is narrower still: it applies to certain steady states in the linear near-equilibrium regime with specified forces and constraints. It is not a universal theorem for biological organization, turbulence, cosmology, or arbitrary driven matter.

## Stochastic histories and maximum caliber

Stochastic dynamics can assign probabilities to whole histories. In favorable diffusion processes, a path probability takes a schematic form

$$
\mathbb P[x(\cdot)]
\propto e^{-\mathcal A_{\mathrm{OM}}[x]},
$$

where $\mathcal A_{\mathrm{OM}}$ is an Onsager--Machlup functional determined by the drift, noise covariance, discretization, and boundary conditions. Its minimizer is a most-probable path only relative to that stochastic model and with care about the path measure. It is not a deterministic law that all thermal systems follow.

Maximum caliber applies maximum-entropy reasoning to a distribution over paths rather than states. Constraints on path observables determine a least-biased path ensemble. Again, the output is a probability distribution over histories, not normally a single mechanical trajectory.

## Entropy, Euclidean action, and information

Several formulas invite a deeper comparison:

$$
e^{-\beta E},
\qquad
e^{-S_E/\hbar},
\qquad
e^{-\mathcal A_{\mathrm{OM}}}.
$$

They share exponential weighting and can sometimes be mapped into one another. But the meanings differ:

- $E$ weights equilibrium microstates in a specified ensemble.
- $S_E$ weights Euclidean field configurations in a quantum or statistical functional integral.
- $\mathcal A_{\mathrm{OM}}$ weights stochastic histories for a specified noise model.
- Thermodynamic entropy counts or quantifies a distribution over compatible microscopic descriptions.

A valid identification requires an explicit derivation of the variables, measure, constraints, units, and limiting procedure. Formal similarity alone does not show that entropy is literally the action of nature. The Euclidean correspondence in [[quantum-action]] is one case where the relationship can be made precise under stated conditions.
