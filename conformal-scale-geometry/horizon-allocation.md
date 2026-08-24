# The FLRW Horizon-Allocation Identity

For a spatially flat \(3+1\)-dimensional FLRW apparent horizon with area-law entropy, one logarithmic scale increment decomposes exactly into a signed horizon-rapidity increment and one quarter of the logarithmic entropy increment. This is a kinematic identity among quantities reconstructed from one history, not by itself a thermodynamic exchange law.

Let

$$
R_A:=\frac cH,
\qquad
A_A:=4\pi R_A^2,
$$

and let \(S_A\) be any entropy proportional to \(A_A\) with a scale-independent proportionality coefficient. For Einstein gravity,

$$
\frac{S_A}{k_B}
=\frac{A_Ac^3}{4G\hbar}
=\frac{\pi c^3R_A^2}{G\hbar}.
$$

Define the signed apparent-horizon index

$$
\widehat\mu_A
:=\frac{1-q}{2}.
$$

From [[conformal-scale-geometry/flrw-scale-section-kinematics|FLRW scale-section kinematics]],

$$
\frac{\mathrm d\ln S_A}{\mathrm dN}
=4(1-\widehat\mu_A).
$$

Now define a signed horizon rapidity \(\widehat\zeta_A\), up to an additive constant, by

$$
\boxed{
\mathrm d\widehat\zeta_A
:=\widehat\mu_A\,\mathrm dN.}
$$

Then

$$
\boxed{
\mathrm dN
=\mathrm d\widehat\zeta_A
+\frac14\,\mathrm d\ln S_A.}
$$

Equivalently, over any interval on which the quantities are regular,

$$
N_2-N_1
=\widehat\zeta_A(N_2)-\widehat\zeta_A(N_1)
+\frac14\ln\frac{S_A(N_2)}{S_A(N_1)}.
$$

The symbol \(\widehat\zeta_A\) is deliberately distinct from conformal time \(\eta\) and from the gravitational areal modulus \(\eta_{\mathrm{grav}}\).

## What the identity establishes

The identity is an exact decomposition of the single scalar differential \(\mathrm dN\) into two terms calculated from the same FLRW function \(H(N)\). It may be read geometrically as

$$
\text{scale increment}
=
\text{signed horizon motion}
+
\text{area-growth increment}.
$$

The normalization of the area entropy cancels from \(\mathrm d\ln S_A\). The identity therefore depends on area scaling, not on using its coefficient to derive a gravitational coupling.

## What it does not establish

The two terms are not thereby independently measured stocks or conserved charges. A physical exchange interpretation would require a common state or phase space, a continuous symmetry, a moment map or current, and a flux law. Nor does the identity identify \(\widehat\zeta_A\) with modular time, a horizontal state coordinate, proper time, or conformal time.
