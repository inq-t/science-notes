# Normal Chirality and Binary Information Geometry

A codimension-two spacelike cut has two null-normal rays, and their chirality supplies a natural binary score. Once the programme identifies the homogeneous $J$-odd response with this reduced quotient, the resulting information geometry is exact; the identification itself remains a physical structural choice.

## Fundamental normal reduction

Let

$$
N(\Sigma)=L_+\oplus L_-,
\qquad
Q=P_+-P_-.
$$

Then

$$
Q^2=1,
\qquad
J_{\mathrm{mod}}QJ_{\mathrm{mod}}=-Q.
$$

The narrow claim is that the homogeneous horizontal response factors through this chirality quotient. It is **not** a claim that the full type-III field theory has a two-level Hilbert space.

## Binary family and BKM metric

The reduced exponential family and log-partition potential are

$$
\omega_\theta=\frac{e^{\theta Q}}{2\cosh\theta},
\qquad
\Psi(\theta)=\ln(2\cosh\theta).
$$

Their dual coordinate and relative-entropy Hessian are

$$
\eta_Q:=\langle Q\rangle=\tanh\theta,
$$

$$
G^{\mathrm{BKM}}_{\theta\theta}
=\Psi''(\theta)
=\operatorname{sech}^2\theta.
$$

Because this reduced family is commuting and binary, the BKM covariance agrees here with the ordinary variance. The normalized moment identity is

$$
\eta_Q^2+G^{\mathrm{BKM}}_{\theta\theta}=1.
$$

The complete Fisher traversal has fixed length

$$
L_F=\int_{-\infty}^{\infty}\operatorname{sech}\theta\,\mathrm d\theta=\pi.
$$

## Self-duality

Normal reflection maps $\omega_\theta$ to $\omega_{-\theta}$. Their symmetrized relative entropy is

$$
\mathfrak S_J(\theta)=4\theta\tanh\theta,
$$

which is nonnegative and has its unique global minimum at $\theta=0$. This defines self-duality inside the reduced family; constructing the corresponding dynamical FLRW wall state remains open.

## Claim status

- **Structural identification:** reduction of the active homogeneous response to $Q$.
- **Exact after reduction:** the binary family, BKM shape, moment identity, Fisher length, and self-dual minimum.
- **Not implied:** a two-dimensional CFT, Cardy thermodynamics, or an entropy--capacity equality for the full wall.

## Dependencies and uses

This note refines [[modular-flow|horizontal state deformation]] and feeds [[scale-soldering|cocycle soldering]], [[scale-capacity|scale--capacity closure]], and [[witten-pair|the internal Witten pair]].

## Provenance

Distilled from [[Causal_Scale_Dynamics_Master_v7_0|Causal Scale Dynamics Master v7.0]]. $J_{\mathrm{mod}}$ and $\eta_Q$ are qualified here to avoid collisions with the Schouten trace and horizon rapidity.
