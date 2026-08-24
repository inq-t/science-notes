# Scale Tractor and Local Vacuum Blindness

In four-dimensional conformal geometry, the scale tractor packages a scale section and its first two derivatives. Einstein's equation can then be split into a trace-free scale-transport equation and a separate scalar norm equation, making the local and scalar channels easy to distinguish.

## Scale tractor

With Schouten tensor and trace

$$
P_{ab}=\frac12\left(R_{ab}-\frac16R g_{ab}\right),
\qquad
J_{\mathrm{Sch}}:=P^a{}_a=\frac R6,
$$

the scale tractor is

$$
I_A=\frac14D_A\sigma
\simeq
\left(
\sigma,
\nabla_a\sigma,
-\frac14(\Delta\sigma+J_{\mathrm{Sch}}\sigma)
\right).
$$

Define the almost-Einstein operator

$$
\mathcal E_{ab}(\sigma)
:=\left(\nabla_a\nabla_b\sigma+P_{ab}\sigma\right)_0.
$$

On the open set where $\sigma\ne0$,

$$
\nabla_a^{T}I_B=0
\quad\Longleftrightarrow\quad
\mathcal E_{ab}(\sigma)=0
\quad\Longleftrightarrow\quad
g_\sigma\text{ is Einstein}.
$$

## Sourced transport and norm

The trace-free and trace parts of Einstein's equation become

$$
\mathcal E_{ab}(\sigma)
=\frac{4\pi G}{c^4}\,\sigma T^{\circ}_{ab},
$$

$$
I^2=\frac{2\pi G}{3c^4}T-\frac{\Lambda_g}{3}.
$$

Thus trace-free stress is an obstruction to parallel scale transport, while the stress trace and cosmological lift occupy the tractor-norm channel.

## Local vacuum blindness

A metric-proportional stress shift obeys

$$
T_{ab}\mapsto T_{ab}+\lambda g_{ab}
\quad\Longrightarrow\quad
T^{\circ}_{ab}\mapsto T^{\circ}_{ab}.
$$

The local trace-free equation is therefore blind to this central direction. This is a statement about the local equation only: it neither fixes $\Lambda_g$ nor proves radiative stability of the remaining scalar/global sector.

The modular analogue is that a constant Hamiltonian shift leaves a normalized Gibbs state unchanged:

$$
\frac{e^{-\beta(H+C\mathbf 1)}}
{\operatorname{tr}e^{-\beta(H+C\mathbf 1)}}
=
\frac{e^{-\beta H}}
{\operatorname{tr}e^{-\beta H}}.
$$

Likewise,

$$
\operatorname{Var}(K+\alpha\mathbf 1)
=\operatorname{Var}(K).
$$

These parallel quotient statements explain local blindness to an additive zero. They do not remove every metric-proportional term from a renormalized gravitational effective action.

## Claim status

- **Standard or exact:** the tractor identities and the rewriting of four-dimensional GR in the stated conventions.
- **Interpretive:** calling trace-free stress a transport defect and $\Lambda_g$ a global lift.
- **Not established:** a solution of the full cosmological-constant problem. Exact zero residual curvature remains a separate sector choice.

## Dependencies and uses

This note depends on [[causal-order|the conformal/scale split]] and feeds [[flrw-kinematics|the FLRW scale dictionary]].

## Provenance

Distilled from [[Causal_Scale_Dynamics_Master_v7_0|Causal Scale Dynamics Master v7.0]]. $J_{\mathrm{Sch}}$ is used here to avoid confusing the Schouten trace with modular conjugation.
