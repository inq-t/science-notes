# Modular Free-Energy Source Law

Relative entropy gives an exact local free-energy curvature around a KMS reference state. Causal Scale Dynamics promotes that local curvature to an all-history homogeneous source density; this promotion is an independent constitutive input, not a consequence of the Scale--Capacity Equivalence Principle.

## Local Hessian

Let $\omega_c$ be the reference state at the crossing, with physical modular Hamiltonian $\mathcal H_c=k_BT_cK_c$. Nonequilibrium free energy obeys

$$
F_c(\rho)-F_c(\omega_c)
=k_BT_cS(\rho\Vert\omega_c).
$$

For a neighboring state in the scale-indexed family,

$$
S(\omega_{c+\delta N}\Vert\omega_c)
=\frac12G^{\perp}_{NN}(N_c)\delta N^2
+O(\delta N^3).
$$

Hence the quadratic free-energy curvature at coincidence is

$$
\left.
\frac{\mathrm d^2 F_c}{\mathrm dN^2}
\right|_{N_c}
=k_BT_cG^{\perp}_{NN}(N_c).
$$

The factor $1/2$ belongs to the Taylor expansion, so the quadratic free-energy increment is $\tfrac12k_BT_cG^{\perp}_{NN}\delta N^2$.

## Constitutive extension

The programme defines the homogeneous response over the whole state path by

$$
\rho_X(N)
:=\frac{k_BT_c}{2V_c}G^{\perp}_{NN}(N),
$$

using the crossing temperature $T_c$ and causal-wall volume $V_c$ as fixed conversion data.

## Claim status

- **Exact locally:** the free-energy/relative-entropy identity and the Hessian expansion at coincidence.
- **Constitutive definition:** distributing the collective free-energy curvature over $V_c$ and extending it over the whole history.
- **Not a scalar-field action:** $\theta$ is a collective state coordinate; no canonical local kinetic term, covariant stress tensor, or conservation law follows from this definition alone.
- **Not an amplitude law:** the source law does not set the peak value of $G^{\perp}_{NN}$.

## Dependencies and uses

The Hessian is supplied by [[binary-geometry|binary BKM geometry]], [[hawking-friedmann|the horizon conversion]] supplies physical units, and [[scale-capacity|the scale--capacity principle]] fixes the peak normalization. Their combination yields the conditional response history.

## Provenance

Distilled from [[Causal_Scale_Dynamics_Master_v7_0|Causal Scale Dynamics Master v7.0]].
