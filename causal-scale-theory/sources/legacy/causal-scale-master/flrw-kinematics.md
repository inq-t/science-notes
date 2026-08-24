# FLRW Scale-Section Kinematics

In the flat conformal representative of FLRW spacetime, cosmic expansion can be expressed directly through the scale section $\sigma=1/a$. The resulting identities make acceleration a statement about log-concavity of scale and relate the tractor norm to the deceleration parameter.

## Scale dictionary

Let conformal time be $\eta$, let overdots denote proper-time derivatives, and write conformal-time derivatives explicitly. Then

$$
\sigma=\frac1a,
\qquad
N=\ln\frac{a}{a_0}=-\ln\frac{\sigma}{\sigma_0},
$$

$$
\frac{\mathrm d\sigma}{\mathrm d\eta}=-H,
\qquad
\mathcal R=\frac1{aH}
=-\frac{\sigma}{\mathrm d\sigma/\mathrm d\eta},
$$

$$
\frac{\mathrm d\mathcal R}{\mathrm d\eta}=q,
$$

$$
q=-1+
\frac{\sigma\,\mathrm d^2\sigma/\mathrm d\eta^2}
{(\mathrm d\sigma/\mathrm d\eta)^2}
=
\frac{\mathrm d^2(\ln\sigma)/\mathrm d\eta^2}
{[\mathrm d(\ln\sigma)/\mathrm d\eta]^2}.
$$

Therefore

$$
\ddot a>0
\quad\Longleftrightarrow\quad
q<0
\quad\Longleftrightarrow\quad
\frac{\mathrm d^2\ln\sigma}{\mathrm d\eta^2}<0.
$$

When the Einstein-FLRW equations are also imposed,

$$
\rho+p\ge0
\quad\Longleftrightarrow\quad
\frac{\mathrm d^2\sigma}{\mathrm d\eta^2}\ge0.
$$

The last equivalence is dynamical, not pure kinematics.

## Tractor norm and signed horizon index

The homogeneous tractor norm is

$$
I^2
=\frac12\sigma\frac{\mathrm d^2\sigma}{\mathrm d\eta^2}
-\left(\frac{\mathrm d\sigma}{\mathrm d\eta}\right)^2
=-\frac12(1-q)H^2.
$$

It is useful to define the signed index

$$
\widehat\mu_A:=\frac{1-q}{2}=-\frac{I^2}{H^2}.
$$

Then

$$
\ddot a>0
\quad\Longleftrightarrow\quad
\widehat\mu_A>\frac12.
$$

The usual magnitude definition $\mu_A:=|\kappa_A|R_A/c^2$ gives $\mu_A=|1-q|/2$. It coincides with $\widehat\mu_A$ only on branches with $q\le1$, including the v7 matter/radiation/response history.

## Claim status

- **Exact kinematics:** the scale, Hubble-radius, deceleration, acceleration, and tractor-norm identities in the chosen flat conformal representative.
- **Einstein-FLRW consequence:** null-energy-condition convexity.
- **Definition with a domain caveat:** the signed index versus the nonnegative surface-gravity magnitude.
- **Not a response-model prediction:** these relations hold independently of the proposed scale-capacity source.

## Dependencies and uses

This module uses [[causal-order|the conformal scale]] and [[scale-tractor|the tractor norm]], and it supplies kinematics to [[self-dual-response|the homogeneous response]]. The horizon information split is isolated in [[horizon-clock|Horizon Clock Allocation]].

## Provenance

Distilled from [[Causal_Scale_Dynamics_Master_v7_0|Causal Scale Dynamics Master v7.0]] with the signed-versus-magnitude distinction made explicit.
