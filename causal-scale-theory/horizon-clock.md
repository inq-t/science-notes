# The FLRW Horizon Clock

In flat FLRW geometry, one e-fold of scale change splits exactly into a signed apparent-horizon rapidity increment and one quarter of the logarithmic horizon-entropy increment. This is a kinematic allocation identity, not yet a thermodynamic conservation law or an identification with the binary state coordinate.

Let

$$
R_A:=\frac cH,
\qquad
\frac{S_A}{k_B}:=\frac{A_Ac^3}{4G\hbar}
=\frac{\pi c^3R_A^2}{G\hbar},
$$

and define the signed apparent-horizon index

$$
\widehat\mu_A:=\frac{1-q}{2}.
$$

From [[causal-scale-theory/flrw-kinematics]],

$$
\frac{\mathrm d\ln S_A}{\mathrm dN}
=4(1-\widehat\mu_A).
$$

Define a signed horizon rapidity by

$$
\mathrm d\widehat\eta_A
:=\widehat\mu_A\,\mathrm dN.
$$

Then

$$
\boxed{
\mathrm dN
=\mathrm d\widehat\eta_A
+\frac14\mathrm d\ln S_A.}
$$

No field equation beyond the declared flat-FLRW relations is needed for this identity.

## What is being allocated

The equation is an exact decomposition of one differential scalar in terms of two other scalars reconstructed from the same $H(N)$. It can be read as

$$
\text{scale increment}
=\text{signed horizon motion}
+\text{area-growth increment}.
$$

That reading is geometrically suggestive, but it does not yet exhibit two independently measured stocks exchanging under a conservation law. In particular,

$$
\widehat\eta_A\ne\theta,
\qquad
\widehat\mu_A\ne\eta=\tanh\theta
$$

unless an additional theorem identifies them.

The magnitude

$$
\mu_A:=|\widehat\mu_A|
$$

enters the non-negative Kodama--Hayward temperature, while the signed quantity belongs in the differential identity. [[horizontal-temperature]] keeps those uses separate.

## Research interpretation

The identity is a plausible geometric shadow of a deeper allocation between reversible state transport and growth of observable capacity. To upgrade that interpretation, one would need a common state-space construction in which the BKM tangent, horizon entropy variation, and signed horizon generator arise as components of one closed geometric law. At present, [[causal-scale-theory/binary-geometry|the binary Casimir balance]] is the exact internal conservation statement and this horizon equation is an exact but independently reconstructed analogue.
