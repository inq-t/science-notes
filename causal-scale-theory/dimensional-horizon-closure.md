# The Dimensional Horizon Closure

In $d$ spatial dimensions, flat Einstein--FLRW horizon algebra fixes the conversion between canonical horizon heat and critical energy. Combined with the CST source law, it gives $\Omega_{X,c}=\mathfrak R_c/(d-1)$. Equal partition requires $\mathfrak R_c=(d-1)/2$; the further unit-amplitude law makes that condition special to three spatial dimensions, but it does not derive dimensionality.

Let $D=d+1$ be the spacetime dimension, with $d>1$. For the flat apparent horizon $R_A=c/H$, write

$$
A_A=\omega_{d-1}R_A^{d-1},
\qquad
V_A=\frac{\omega_{d-1}}{d}R_A^d,
$$

where $\omega_{d-1}$ is the area of the unit $(d-1)$-sphere. Adopt the Einstein entropy and canonical horizon temperature

$$
\frac{S_A}{k_B}
=\frac{c^3A_A}{4G_D\hbar},
\qquad
k_BT_{\mathrm{hor}}
=\frac{\hbar c}{2\pi R_A}.
$$

Their product per horizon volume is

$$
\frac{k_BT_{\mathrm{hor}}(S_A/k_B)}{V_A}
=\frac{d c^4}{8\pi G_D R_A^2}.
$$

The $D$-dimensional flat-Friedmann critical energy density is

$$
\rho_{\mathrm{crit}}
=\frac{d(d-1)c^2H^2}{16\pi G_D}.
$$

Using $R_A=c/H$ therefore gives the **[EXACT — GIVEN THE HORIZON DEFINITIONS]** identity

$$
\boxed{
\frac{k_BT_{\mathrm{hor}}(S_A/k_B)}{V_A}
=\frac{2}{d-1}\rho_{\mathrm{crit}}.}
$$

For $d=3$, this reduces to [[causal-scale-theory/hawking-friedmann|the Hawking--Friedmann conversion]]. It is not the stationary black-hole Smarr relation; [[conservation-of-causal-charge/black-hole-saturation-boundary|black-hole saturation]] owns that distinct comparison.

## Crossing fraction

At the crossing, [[causal-scale-theory/free-energy-source|the CST source law]] and [[causal-scale-theory/scale-capacity|the capacity ratio]] give

$$
\rho_{X,c}
=\frac12\mathfrak R_c
\frac{k_BT_c(S_c/k_B)}{V_c}.
$$

After the open identification $T_c=T_{\mathrm{hor},c}$ is granted,

$$
\boxed{
\Omega_{X,c}
:=\frac{\rho_{X,c}}{\rho_{\mathrm{crit},c}}
=\frac{\mathfrak R_c}{d-1}.}
$$

For a spatially flat crossing with positive total non-$X$ complement,

$$
\frac{\rho_{X,c}}{\rho_{\mathrm{non-}X,c}}
=\frac{\mathfrak R_c}{d-1-\mathfrak R_c},
\qquad
0<\mathfrak R_c<d-1.
$$

Identifying the complement with ordinary matter plus radiation still requires the zero-residual sector and absence of another crossing component.

Equal response and non-$X$ densities mean $\Omega_{X,c}=1/2$. Within the same flat, positive-complement premises,

$$
\boxed{
\rho_{X,c}=\rho_{\mathrm{non-}X,c}
\quad\Longleftrightarrow\quad
\mathfrak R_c=\frac{d-1}{2}.}
$$

Thus equal partition alone does not select a dimension: for each admissible $d$, it selects a corresponding amplitude ratio. A dimension-specific statement arises only after an independent amplitude law is imposed.

## The unit-amplitude dimensional statement

If $\mathfrak R_c=1$ and $d>2$, then

$$
\Omega_{X,c}=\frac1{d-1},
\qquad
\frac{\rho_{X,c}}{\rho_{\mathrm{non-}X,c}}
=\frac1{d-2}.
$$

Consequently, combining the general equal-partition condition with the separate unit-amplitude law gives

$$
\boxed{
\mathfrak R_c=1
\quad\Longrightarrow\quad
\left(
\rho_{X,c}=\rho_{\mathrm{non-}X,c}
\quad\Longleftrightarrow\quad
d=3
\right).}
$$

This is a structural compatibility statement. It does not show that CST selects $d=3$, because the argument already assumes a $d$-dimensional Einstein horizon and separately imposes the unit-amplitude law. A dimensional-selection theorem would have to derive the admissible dimension before using the observed background.
