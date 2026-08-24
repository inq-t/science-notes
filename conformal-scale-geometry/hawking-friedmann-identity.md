# The Hawking--Friedmann Identity

For the apparent horizon of a spatially flat \(3+1\)-dimensional Einstein--FLRW spacetime, canonical \(2\pi\) horizon heat times Einstein area entropy equals both the Misner--Sharp horizon energy and the Friedmann critical energy inside the horizon volume. This is exact algebra given the stated horizon and gravitational definitions.

Use the energy-density convention

$$
\rho_{\mathrm{crit}}
:=\frac{3c^2H^2}{8\pi G}.
$$

For the flat apparent horizon described by [[conformal-scale-geometry/flrw-scale-section-kinematics|FLRW scale-section kinematics]], define

$$
R_A:=\frac cH,
\qquad
A_A:=4\pi R_A^2,
\qquad
V_A:=\frac{4\pi}{3}R_A^3.
$$

The Einstein area entropy is

$$
\frac{S_A}{k_B}
:=\frac{A_Ac^3}{4G\hbar}
=\frac{\pi c^3R_A^2}{G\hbar}.
$$

Associate to the horizon radius the canonical \(2\pi\) temperature scale

$$
\boxed{
k_BT_A^{\mathrm{can}}
:=\frac{\hbar c}{2\pi R_A}.}
$$

Multiplication gives

$$
k_BT_A^{\mathrm{can}}\frac{S_A}{k_B}
=\frac{\hbar c}{2\pi R_A}
\frac{\pi c^3R_A^2}{G\hbar}
=\frac{c^4R_A}{2G}.
$$

The right-hand side is the Misner--Sharp energy evaluated at the apparent horizon:

$$
E_{\mathrm{MS},A}
=\frac{c^4R_A}{2G}.
$$

Independently,

$$
\begin{aligned}
\rho_{\mathrm{crit}}V_A
&=
\frac{3c^2H^2}{8\pi G}
\frac{4\pi}{3}R_A^3\\
&=
\frac{c^4R_A}{2G},
\end{aligned}
$$

where \(R_A=c/H\) was used. Therefore

$$
\boxed{
k_BT_A^{\mathrm{can}}\frac{S_A}{k_B}
=E_{\mathrm{MS},A}
=\rho_{\mathrm{crit}}V_A.}
$$

## Scope

The identity uses:

- a spatially flat FLRW apparent horizon;
- \(3+1\)-dimensional Einstein gravity;
- the Einstein area entropy;
- the canonical \(2\pi\) temperature scale; and
- the stated energy-density convention.

It does not determine \(G\): both the entropy and critical-density definitions already contain it. It also does not identify this canonical temperature with the temperature of an independent horizontal state deformation, construct a state-space source, or convert a response capacity into cosmological energy. Such steps are additional physical identifications.
