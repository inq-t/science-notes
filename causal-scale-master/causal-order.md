# Causal Order and Metric Scale

Under standard causality and regularity hypotheses, causal order determines a Lorentzian spacetime only up to conformal scale. Causal Scale Dynamics treats the missing scale calibration as a distinct physical register, but that interpretive step goes beyond the underlying reconstruction theorems.

## Conformal structure plus scale

A conformal class identifies metrics related by

$$
g_{ab}\sim\Omega^2g_{ab}.
$$

A positive conformal density

$$
\sigma\in\Gamma(\mathcal E[1])
$$

selects the physical representative

$$
g_{\mathrm{phys}}=\sigma^{-2}\boldsymbol g.
$$

The pair $([g],\sigma)$ therefore contains the same kinematic information as a metric: $[g]$ supplies the null cones and $\sigma$ supplies local calibration.

For cosmological use, define an uncentered e-fold coordinate and its crossing value by

$$
N:=\ln\frac{a}{a_0},
\qquad
N_c:=\ln\frac{a_c}{a_0}.
$$

The centered Weyl displacement is then

$$
x:=N-N_c
=\ln\frac{a}{a_c}
=-\ln\frac{\sigma}{\sigma_c}.
$$

This convention keeps $N=0$ today and $x=0$ at the distinguished crossing. The horizontal state coordinate is a separate quantity, $\theta=\varrho_\perp x$, until the unit-slope branch is chosen.

## Claim status

- **Standard:** the causal-to-conformal reconstruction, subject to its causality and regularity hypotheses.
- **Definition:** a positive scale section chooses a metric representative.
- **Framework interpretation:** causal geometry and metric calibration may have distinct dynamical sourcing.
- **Not established here:** that the scale register is sourced by modular information geometry or that it produces a cosmological response.

## Dependencies and uses

This is the geometric input to [[scale-tractor|scale-tractor transport]], [[scale-soldering|scale--state soldering]], and [[flrw-kinematics|FLRW scale kinematics]].

## Provenance

Distilled from [[Causal_Scale_Dynamics_Master_v7_0|Causal Scale Dynamics Master v7.0]]. The notation above resolves an inconsistency in the source by reserving $N-N_c$, rather than $N$, for displacement from the crossing.
