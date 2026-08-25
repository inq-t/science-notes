# Fixed-Reference Relative Entropy Cannot Be the Full Source

A finite relative entropy from one fixed reference and the coincidence BKM Hessian along a state path are different functions. For the balanced binary family this distinction is exact, so a fixed-reference free-energy identity cannot derive the all-history CST-B2 pulse by replacing its finite difference with the instantaneous quadratic capacity.

[[basic-concepts/hessians/gibbs-free-energy-relative-entropy|The Gibbs free-energy theorem]] owns the general fixed-data identity and its coincidence boundary. For the present reduced family, [[binary-information-geometry/reflected-divergence|the exact binary divergence]] gives

$$
D(\rho_\theta\Vert\rho_0)
=\theta\tanh\theta-\ln\cosh\theta,
\qquad
\frac{\mathrm d}{\mathrm d\theta}
D(\rho_\theta\Vert\rho_0)
=\theta\operatorname{sech}^2\theta.
$$

The derivative is nonzero away from \(\theta=0\). By contrast, neighboring-state relative entropy begins quadratically with local coefficient

$$
g^{\mathrm{bin}}_{\theta\theta}
=\operatorname{sech}^2\theta.
$$

Consequently,

$$
\boxed{
\text{fixed-reference free-energy identity}
\not\vdash
\rho_X(N)\propto G^{\perp}_{NN}(N)
\text{ for an entire history}.}
$$

The anchored source in [[program-core/ruble-equations|the Ruble equations]] therefore remains **[CONSTITUTIVE]**. The no-go does not refute that law; it excludes one attempted derivation of it.
