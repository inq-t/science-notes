# Kinetic and Stochastic Variational Principles

Out of equilibrium the variational picture survives only with additional constitutive, stochastic, or near-equilibrium assumptions. Linear irreversible thermodynamics yields a least-dissipation structure over instantaneous rates; stochastic dynamics assigns weights to whole histories and yields a most-probable path relative to a declared noise model. Neither is Hamilton's principle with entropy substituted for action, and the exponential weights they share with [[quantum-action|the quantum flavor]] are a formal resemblance until a map is constructed.

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
