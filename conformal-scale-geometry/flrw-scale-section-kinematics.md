# FLRW Scale-Section Kinematics

On a spatially flat FLRW spacetime, the inverse scale factor is a conformal scale section whose derivatives encode the Hubble and deceleration parameters. Apparent-horizon motion and the horizon-area rate then follow as exact kinematics; Einstein dynamics enters only when stress-energy is related to scale convexity.

Let

$$
\mathrm ds^2
=-c^2\mathrm dt^2
+a(t)^2\mathrm d\mathbf x^2,
\qquad
\mathrm d\eta
=\frac{\mathrm dt}{a},
\qquad
\sigma:=a^{-1}.
$$

Here \(\eta\) is conformal time. Use a dot for \(\mathrm d/\mathrm dt\) and a prime for \(\mathrm d/\mathrm d\eta\) in this note. Define

$$
H:=\frac{\dot a}{a},
\qquad
q:=-\frac{a\ddot a}{\dot a^2}.
$$

Direct differentiation gives

$$
\boxed{\sigma'=-H,}
$$

and

$$
\sigma''=-a\dot H.
$$

Consequently,

$$
\boxed{
q
=-1+\frac{\sigma\sigma''}{(\sigma')^2}
=\frac{(\ln\sigma)''}
{\bigl((\ln\sigma)'\bigr)^2}.}
$$

Thus accelerated expansion is equivalently a statement about the conformal-time curvature of the logarithmic scale section. No field equation is used in these identities.

## Comoving apparent-horizon motion

The comoving apparent-horizon radius is

$$
\mathcal R_A
:=\frac{c}{aH}.
$$

Its conformal-time derivative is

$$
\boxed{\mathcal R_A'=cq.}
$$

If the length-valued conformal coordinate \(\eta_\ell:=c\eta\) is used instead, then

$$
\frac{\mathrm d\mathcal R_A}{\mathrm d\eta_\ell}
=q.
$$

## Einstein energy condition and scale convexity

If the flat Einstein--FLRW equations are additionally imposed using the energy-density convention in which \(\rho\) and \(p\) have the same units,

$$
\dot H
=-\frac{4\pi G}{c^2}(\rho+p).
$$

Because \(\sigma''=-a\dot H\),

$$
\boxed{
\rho+p\geq0
\quad\Longleftrightarrow\quad
\sigma''\geq0.}
$$

This equivalence is dynamical and specific to the declared Einstein--FLRW setting. It is not pure conformal kinematics.

## Tractor norm and signed horizon index

For the flat FLRW scale tractor in the conventions of [[conformal-scale-geometry/scale-tractor-transport|scale-tractor transport]],

$$
I^2
=-\frac12(1-q)\frac{H^2}{c^2}.
$$

Define the signed apparent-horizon index

$$
\boxed{
\widehat\mu_A
:=\frac{1-q}{2}
=-\frac{c^2I^2}{H^2}.}
$$

The sign belongs to the geometric relation. A nonnegative temperature constructed from a surface-gravity magnitude would use \(\lvert\widehat\mu_A\rvert\), not silently discard the sign in a transport identity.

## E-fold and physical-horizon form

Let

$$
N:=\ln\frac{a}{a_*}.
$$

Then

$$
q
=-1-\frac{\mathrm d\ln H}{\mathrm dN}.
$$

For the physical apparent-horizon radius

$$
R_A:=\frac cH,
$$

one obtains

$$
\boxed{
\frac{\mathrm d\ln R_A}{\mathrm dN}
=1+q.}
$$

In \(3+1\) dimensions any area-law entropy satisfies \(S_A\propto R_A^2\), so

$$
\boxed{
\frac{\mathrm d\ln S_A}{\mathrm dN}
=2(1+q)
=4(1-\widehat\mu_A).}
$$
