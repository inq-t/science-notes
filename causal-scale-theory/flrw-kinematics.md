# FLRW Scale-Section Kinematics

On a spatially flat FLRW background, the inverse scale factor is a scale section whose conformal-time derivatives encode the Hubble and deceleration parameters. The resulting horizon identities are exact kinematics and do not depend on CST's information-geometric closure.

Let

$$
\mathrm ds^2=-c^2\mathrm dt^2+a(t)^2\mathrm d\mathbf x^2,
\qquad
\mathrm d\eta=\frac{\mathrm dt}{a},
\qquad
\sigma:=a^{-1}.
$$

Using a dot for cosmic time and a prime $\partial_\eta$ only in this note,

$$
H:=\frac{\dot a}{a},
\qquad
q:=-\frac{a\ddot a}{\dot a^2},
\qquad
\sigma'=-H.
$$

The comoving apparent-horizon radius is

$$
\mathcal R:=\frac{c}{aH}.
$$

With $\eta$ measured in time units as defined above, differentiation gives

$$
\mathcal R'=cq.
$$

Equivalently, for the length-valued conformal coordinate $\eta_\ell:=c\eta$, one has $\mathrm d\mathcal R/\mathrm d\eta_\ell=q$. The older masters use the geometric-unit form $c=1$.

Thus acceleration is scale-section convexity:

$$
q
=-1+\frac{\sigma\sigma''}{(\sigma')^2}
=\frac{(\ln\sigma)''}{\bigl((\ln\sigma)'\bigr)^2}.
$$

These are identities, not equations of motion.

When the Einstein--FLRW equations are additionally imposed,

$$
\dot H=-\frac{4\pi G}{c^2}(\rho+p),
$$

and $\sigma''=-a\dot H$. Therefore

$$
\boxed{
\rho+p\ge0
\quad\Longleftrightarrow\quad
\sigma''\ge0.}
$$

This null-energy/scale-convexity equivalence is dynamical, not pure scale-section kinematics. It also depends on the flat Einstein--FLRW setting and the energy-density convention used here.

## Tractor norm and the signed horizon index

For the flat FLRW scale tractor in the conventions of [[causal-scale-theory/scale-tractor]],

$$
I^2=-\frac12(1-q)\frac{H^2}{c^2}.
$$

Define the signed index

$$
\widehat\mu_A:=\frac{1-q}{2}=-\frac{c^2I^2}{H^2}.
$$

The sign is part of the geometry. Thermodynamic temperature uses the magnitude

$$
\mu_A:=|\widehat\mu_A|,
$$

so signed transport identities and non-negative temperatures must not use the same symbol silently.

## E-fold form

With

$$
N:=\ln a,
$$

and now using $\mathrm d/\mathrm dN$ explicitly,

$$
q=-1-\frac{\mathrm d\ln H}{\mathrm dN}.
$$

For the physical apparent-horizon radius $R_A=c/H$,

$$
\frac{\mathrm d\ln R_A}{\mathrm dN}=1+q.
$$

Since the Bekenstein--Hawking entropy is proportional to $R_A^2$,

$$
\frac{\mathrm d\ln S_A}{\mathrm dN}
=2(1+q)
=4(1-\widehat\mu_A).
$$

Integrating this identity gives [[causal-scale-theory/horizon-clock|the horizon-clock allocation]]. None of these equations selects a response density or a state family; those belong later in [[causal-scale-theory/closure-stack]].

## Scope

- Spatial curvature changes the apparent-horizon radius and the simplest formulas above.
- A background identity does not supply perturbations.
- The scale-section interpretation is covariant in its proper tractor formulation; the displayed $a(t)$ formulas are the homogeneous specialization.
