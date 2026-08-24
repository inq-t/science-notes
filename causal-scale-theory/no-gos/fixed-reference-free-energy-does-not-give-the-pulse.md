# Fixed-Reference Free Energy Does Not Derive the Pulse

The local BKM Hessian cannot be substituted for a finite fixed-reference free-energy difference along the whole binary path. The exclusion is exact for the declared balanced family and blocks one derivation of the CST source; it does not block the source from being proposed constitutively.

For the balanced binary state $\rho_\theta$ and reference $\rho_0$,

$$
S(\rho_\theta\Vert\rho_0)
=\theta\tanh\theta-\ln\cosh\theta.
$$

Its derivative is

$$
\frac{\mathrm d}{\mathrm d\theta}
S(\rho_\theta\Vert\rho_0)
=\theta\operatorname{sech}^2\theta,
$$

which is nonzero for $\theta\ne0$.

By contrast, neighboring-state relative entropy has the coincidence expansion

$$
S(\rho_{\theta+\delta\theta}\Vert\rho_\theta)
=\frac12\operatorname{sech}^2\theta
(\delta\theta)^2+O((\delta\theta)^3).
$$

These expressions answer different questions. The first compares every state with one fixed reference; the second compares infinitesimally neighboring states. Replacing the first by the second discards its linear variation.

The no-go conclusion is

$$
\boxed{
\text{fixed-reference free-energy identity}
\not\vdash
\rho_X\propto G^{\mathrm{BKM}}_{NN}
\text{ for all }N.}
$$

[[causal-scale-theory/free-energy-source|The anchored source law]] therefore remains explicitly constitutive.
