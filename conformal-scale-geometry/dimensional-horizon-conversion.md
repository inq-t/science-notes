# The Dimensional Horizon Conversion

In \(D=d+1\) Einstein--FLRW dimensions, the canonical apparent-horizon heat per horizon volume equals \(2/(d-1)\) times the flat Friedmann critical energy density. The familiar equality without an extra coefficient is therefore special to three spatial dimensions within these assumptions.

Let \(d>1\) be the number of spatial dimensions and let \(\omega_{d-1}\) be the area of the unit \((d-1)\)-sphere. For the flat apparent horizon

$$
R_A:=\frac cH,
$$

define

$$
A_A
:=\omega_{d-1}R_A^{d-1},
\qquad
V_A
:=\frac{\omega_{d-1}}{d}R_A^d.
$$

Adopt the \(D\)-dimensional Einstein entropy and canonical temperature scale

$$
\frac{S_A}{k_B}
:=\frac{c^3A_A}{4G_D\hbar},
\qquad
k_BT_A^{\mathrm{can}}
:=\frac{\hbar c}{2\pi R_A}.
$$

Their product per horizon volume is

$$
\begin{aligned}
\frac{k_BT_A^{\mathrm{can}}(S_A/k_B)}
{V_A}
&=
\frac{\hbar c}{2\pi R_A}
\frac{c^3\omega_{d-1}R_A^{d-1}}
{4G_D\hbar}
\frac{d}{\omega_{d-1}R_A^d}\\
&=
\frac{dc^4}{8\pi G_DR_A^2}.
\end{aligned}
$$

The spatially flat \(D\)-dimensional Friedmann critical energy density is

$$
\rho_{\mathrm{crit}}
:=
\frac{d(d-1)c^2H^2}
{16\pi G_D}.
$$

Using \(R_A=c/H\),

$$
\frac{dc^4}{8\pi G_DR_A^2}
=\frac{dc^2H^2}{8\pi G_D}
=\frac{2}{d-1}\rho_{\mathrm{crit}}.
$$

Hence

$$
\boxed{
\frac{k_BT_A^{\mathrm{can}}(S_A/k_B)}
{V_A}
=\frac{2}{d-1}\rho_{\mathrm{crit}}.}
$$

Equivalently,

$$
\boxed{
k_BT_A^{\mathrm{can}}\frac{S_A}{k_B}
=\frac{2}{d-1}
\rho_{\mathrm{crit}}V_A.}
$$

For \(d=3\), the coefficient is one and the result reduces to [[conformal-scale-geometry/hawking-friedmann-identity|the Hawking--Friedmann identity]].

## Boundary of the theorem

The result is a conversion identity inside a \(d\)-dimensional Einstein--FLRW model. It neither selects \(d=3\) nor supplies a dimensional-selection argument. A response fraction, equal-partition statement, state-capacity matching law, or cosmological crossing relation would require additional constitutive premises and therefore does not belong to this identity.

Higher-curvature gravity can replace Einstein area entropy by a Wald-type functional, and spatial curvature changes the apparent-horizon geometry. In either case the displayed coefficient must be rederived rather than assumed universal.
