# A Fractional-Susceptibility Ansatz Does Not Preserve the CST Crossing

Replacing the anchored density pulse by an instantaneous fractional law $\Omega_X=\lambda\operatorname{sech}^2(\nu x)$ can define an effective cosmology on a restricted parameter interval, but its susceptibility maximum is generically not a density maximum and has $w_X\ne-1$. It therefore does not preserve the CST crossing identities or shape invariant.

Consider the alternative ansatz

$$
\Omega_X(N)
:=\frac{\rho_X}{\rho_{\mathrm{crit}}}
=\lambda\operatorname{sech}^2\!\bigl(\nu(N-N_c)\bigr)
$$

in a spatially flat, zero-residual matter-plus-radiation background. Writing

$$
B(N):=\rho_m(N)+\rho_r(N),
$$

flatness gives

$$
\rho_{\mathrm{crit}}(N)
=\frac{B(N)}{1-\Omega_X(N)},
\qquad
\rho_X(N)
=\frac{\Omega_X(N)}{1-\Omega_X(N)}B(N).
$$

Matching the present response fraction $D$ requires $\lambda\ge D$, because the profile never exceeds $\lambda$. Regularity at its peak requires $\lambda<1$; $\lambda=1$ makes the denominator vanish there. Thus even background existence restricts the ansatz to

$$
D\le\lambda<1.
$$

At the susceptibility peak $N=N_c$, one has $\Omega_X'=0$. Nevertheless,

$$
\left.\frac{\mathrm d\ln\rho_X}{\mathrm dN}\right|_{N_c}
=-\frac{3\rho_{m,c}+4\rho_{r,c}}
{\rho_{m,c}+\rho_{r,c}}.
$$

If the effective response is separately conserved, then

$$
\boxed{
w_{X,c}
=-1-\frac13
\left.\frac{\mathrm d\ln\rho_X}{\mathrm dN}\right|_{N_c}
=\frac{\rho_{r,c}}
{3(\rho_{m,c}+\rho_{r,c})}.}
$$

It is approximately dustlike, not vacuumlike, and is exactly nonnegative for nonnegative matter and radiation. The peak of the fractional susceptibility is therefore not the peak of $\rho_X$. The binary density conic and the CST differential invariant also fail because the instantaneous critical density contributes an additional scale dependence.

The scoped conclusion is

$$
\boxed{
\Omega_X\propto\operatorname{sech}^2(\nu x)
\not\Longrightarrow
\text{the anchored CST density response}.}
$$

This does not rule out fractional dark-energy models. It rules out using this particular dimensionless shortcut while retaining CST's self-dual density maximum, $w=-1$ crossing, and rigid shape law. A dimensionful conversion datum such as $T_cS_c/V_c$ is load-bearing in [[causal-scale-theory/free-energy-source|the anchored source law]].

