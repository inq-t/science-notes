# Balanced Binary Information Geometry

Once a balanced two-outcome channel with normalized generator $Q^2=\mathbf1$ is granted, its polarization, BKM metric, Casimir balance, finite Fisher length, and reflected divergences follow exactly. The reduction and its realization in a local operator algebra remain separate physical obligations.

## Reduction premises

Let

$$
Q=Q^*,
\qquad
Q^2=\mathbf1,
\qquad
P_\pm:=\frac{\mathbf1\pm Q}{2}.
$$

The normalization fixes the two eigenvalues, but it does **not** fix their degeneracies or reference weights. [[balanced-channel-premise|Balance is an independent premise]]. In a concrete faithful finite realization, let $\rho_0$ commute with $Q$ and impose

$$
\operatorname{Tr}(\rho_0P_+)
=\operatorname{Tr}(\rho_0P_-)
=\frac12.
$$

An abstract geometric reflection may be represented in the reduced model by an involution $J_{\mathrm{refl}}$ satisfying

$$
J_{\mathrm{refl}}QJ_{\mathrm{refl}}^{-1}=-Q.
$$

$J_{\mathrm{refl}}$ is not to be identified with Tomita conjugation $J^{\mathrm{TT}}$. [[open-questions/binary-reflection-realization|The full-algebra obstruction and the two live realizations]] are owned separately; the shared construction obligation remains in [[wall-construction-interface/binary-channel|the binary-channel interface]].

## Exponential family

Define the balanced exponential tilt

$$
\rho_\theta
=\frac{e^{\theta Q/2}\rho_0e^{\theta Q/2}}
{Z_{\rho_0}(\theta)},
\qquad
Z_{\rho_0}(\theta)
:=\operatorname{Tr}(\rho_0e^{\theta Q})
=\cosh\theta,
\qquad
\psi(\theta):=\ln Z_{\rho_0}(\theta).
$$

For the literal two-dimensional maximally mixed reference $\rho_0=\mathbf1/2$, this reduces to $\rho_\theta=e^{\theta Q}/(2\cosh\theta)$. The balanced-reference form above also permits equal total weights with nontrivial degeneracies inside the two blocks.

Then

$$
\eta(\theta)
:=\omega_\theta(Q)
=\psi'(\theta)
=\tanh\theta,
$$

and the BKM metric along the exponential coordinate is

$$
G^{\mathrm{BKM}}_{\theta\theta}
=\psi''(\theta)
=\operatorname{Var}_{\omega_\theta}(Q)
=\operatorname{sech}^2\theta.
$$

These are **[EXACT — AFTER REDUCTION]**. They do not establish that the full wall theory possesses only this channel or that its extensive norm is finite.

Čencov's theorem fixes the classical Fisher metric up to scale under its statistical-morphism hypotheses. Quantum monotonicity is less selective: Petz's classification contains a family of monotone metrics. CST uses the BKM member because it is the coincidence Hessian of Umegaki relative entropy and the covariance metric of this commuting exponential family, not because monotonicity alone uniquely selects it. None of these classification theorems converts a dimensionless state metric into energy density.

## Casimir balance

Because $Q^2=\mathbf1$,

$$
\omega_\theta(Q^2)
=\omega_\theta(Q)^2
+\operatorname{Var}_{\omega_\theta}(Q),
$$

so

$$
\boxed{
1=\eta^2+G^{\mathrm{BKM}}_{\theta\theta}.}
$$

The state breaks the reflection symmetry when $\eta\ne0$, but the representation norm is unchanged. This is a precise conservation of normalized discernibility: resolved polarization grows as residual susceptibility shrinks. It is algebraic rather than a Noether charge, and it does not yet identify susceptibility with gravitational energy or spatial area.

If $\theta=\nu x$ on a chosen orientation, then

$$
\frac{\mathrm d\eta}{\mathrm dN}
=\nu G,
\qquad
\frac{\mathrm dG}{\mathrm dN}
=-2\nu\eta G,
\qquad
\frac{\mathrm d}{\mathrm dN}(\eta^2+G)=0.
$$

The normalized wall charge can also be written

$$
\mathcal Q_{\mathrm{wall}}
:=\frac12\int_{-\infty}^{+\infty}
\frac{\mathrm d\eta}{\mathrm dN}\,\mathrm dN
=1,
$$

provided the path reaches both asymptotic polarizations. This is a topological endpoint identity for the reduced path, not yet a locally conserved spacetime current.

## Intrinsic coordinate and finite length

Set

$$
\phi:=\operatorname{gd}(\theta)
=\arctan(\sinh\theta).
$$

Since $\mathrm d\phi=\operatorname{sech}\theta\,\mathrm d\theta$,

$$
\mathrm ds_{\mathrm{BKM}}^2
=\operatorname{sech}^2\theta\,\mathrm d\theta^2
=\mathrm d\phi^2.
$$

The complete binary line therefore has finite Fisher length

$$
\int_{-\infty}^{+\infty}\operatorname{sech}\theta\,\mathrm d\theta=\pi.
$$

At $\theta=0$, polarization vanishes and susceptibility is maximal. This is the binary self-dual point. Equality with an ordinary cosmological sector occurs there only after the amplitude principle takes its unit value.

## Relative entropy under reflection

The one-sided reflected divergence is

$$
S(\rho_\theta\Vert\rho_{-\theta})
=2\theta\tanh\theta.
$$

The symmetric Jeffreys divergence is therefore

$$
S(\rho_\theta\Vert\rho_{-\theta})
+S(\rho_{-\theta}\Vert\rho_\theta)
=4\theta\tanh\theta.
$$

Both are even under $\theta\mapsto-\theta$ and hence cannot select a direction of cosmological evolution. Orientation must come from the soldering convention and the selected expanding branch.
