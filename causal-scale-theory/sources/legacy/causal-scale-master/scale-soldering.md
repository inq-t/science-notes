# Connes-Cocycle Scale Soldering

The scale--state soldering argument derives a logarithmic functional form, not its coefficient. This module isolates the assumptions behind that conditional result so the physical choice $\varrho_\perp=1$ cannot be accidentally cited as a theorem.

## Assumptions

Assume that the reduced relative cocycle

1. depends on two positive scale sections only through $r=\sigma_2/\sigma_1$;
2. has one active noncentral generator $Q$; and
3. is measurable as a function of $r$.

The cocycle chain rule then reduces to

$$
\theta(r_1r_2)=\theta(r_1)+\theta(r_2).
$$

Measurable solutions of this multiplicative Cauchy equation are

$$
\theta(r)=-\varrho_\perp\ln r.
$$

With

$$
N:=\ln\frac{a}{a_0},
\qquad
N_c:=\ln\frac{a_c}{a_0},
$$

the soldering law is

$$
\theta=\varrho_\perp(N-N_c).
$$

## What fixes the slope?

The functional equation leaves every real $\varrho_\perp$ available. Causal Scale Dynamics selects

$$
\varrho_\perp=1
$$

by identifying the fundamental null-normal character with the fundamental scale/inverse-scale character. This is a physical representation choice.

## Claim status

- **Conditional theorem:** the affine logarithmic form, given the ratio, rank-one, cocycle, and measurability assumptions.
- **Physical choice:** unit slope.
- **Rejected derivation:** conformal density bundles admit real weights, so conformal geometry does not impose an integer spectrum that singles out one.
- **Open:** direct computation of this cocycle for an explicitly constructed scale-indexed FLRW causal-wall state family.

## Dependencies and uses

The construction combines [[causal-order|Weyl scale]], [[modular-flow|horizontal state comparison]], and [[binary-geometry|the chirality generator]].

## Provenance

Distilled from [[Causal_Scale_Dynamics_Master_v7_0|Causal Scale Dynamics Master v7.0]], including its audit of the rejected integrality argument.
