# Entropy-Normalized Scale Capacity

The scale-capacity ratio is the dimensionless, coordinate-invariant peak norm of the horizontal scale tangent. It separates a normalized binary susceptibility from the extensive number and renormalization of physical wall channels. Its unit value is a distinct proposed law.

Let $G^\perp_{NN}(N)$ be the renormalized squared BKM norm of the reflection-odd horizontal tangent, and let $S_c$ be the declared horizon or wall entropy at the crossing. Define

$$
\boxed{
\mathfrak R_c
:=\frac{k_B}{S_c}G^\perp_{NN}(N_c).}
$$

Both numerator and $S_c/k_B$ are dimensionless, so $\mathfrak R_c$ is dimensionless.

Under a reparameterization $\widetilde\theta=f(\theta)$,

$$
G^\perp_{NN}
=G^\perp_{\theta\theta}\left(\frac{\mathrm d\theta}{\mathrm dN}\right)^2
=G^\perp_{\widetilde\theta\widetilde\theta}
\left(\frac{\mathrm d\widetilde\theta}{\mathrm dN}\right)^2,
$$

so $\mathfrak R_c$ is invariant even though the coordinate components and slope separately change.

## Normalized shape versus extensive norm

The binary algebra fixes

$$
g_{\theta\theta}^{\mathrm{bin}}
=\operatorname{sech}^2\theta.
$$

A physical wall can carry an extensive prefactor $C_\perp(N)$:

$$
G^\perp_{NN}(N)
=C_\perp(N)\nu^2\operatorname{sech}^2(\nu x).
$$

The rigid CST profile assumes

$$
C_\perp(N)=C_{\perp,c}
$$

over the homogeneous path. With that explicit assumption,

$$
G^\perp_{NN}(N)
=\frac{S_c}{k_B}\mathfrak R_c
\operatorname{sech}^2(\nu x).
$$

A microscopic wall may instead return a scale-dependent channel density. That would be a physical correction to the pulse, not a violation of the normalized binary identity.

## Cosmological meaning is downstream

Information geometry alone imposes no interval $0<\mathfrak R_c<2$. After [[causal-scale-theory/free-energy-source|the source law]] and [[causal-scale-theory/hawking-friedmann|the horizon conversion]] are adopted in $3+1$ dimensions,

$$
\Omega_{X,c}=\frac{\mathfrak R_c}{2}.
$$

If the background is spatially flat and the total complementary density is positive, then

$$
\frac{\rho_{X,c}}{\rho_{\mathrm{non-}X,c}}
=\frac{\mathfrak R_c}{2-\mathfrak R_c},
\qquad
0<\mathfrak R_c<2.
$$

Identifying the non-$X$ complement specifically with ordinary matter plus radiation additionally requires the zero-residual sector and no other crossing component. At $\mathfrak R_c=1$, response equals the total non-$X$ complement in the flat background, and equals ordinary matter plus radiation under those further premises. That equality is not the same statement as binary self-duality; it coincides with self-duality only on the unit-amplitude cosmological branch.

The proposed unit value and its falsification conditions are isolated in [[unit-amplitude-principle]].
