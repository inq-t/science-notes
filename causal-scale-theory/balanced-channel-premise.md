# The Balanced-Channel Premise

The normalized generator $Q^2=\mathbf1$ fixes two outcomes but not their reference weights. The canonical $\tanh\theta$ response centered at the declared self-dual point requires a balanced reference channel, either derived from a valid reflection-invariant state or supplied as an explicit premise.

Let

$$
P_\pm:=\frac{\mathbf1\pm Q}{2},
\qquad
w_\pm:=\operatorname{Tr}(\rho_0P_\pm),
\qquad
w_++w_-=1.
$$

The balanced premise is

$$
\boxed{w_+=w_-=\frac12.}
$$

Then the exponential tilt has partition function

$$
Z_{\rho_0}(\theta)
=w_+e^\theta+w_-e^{-\theta}
=\cosh\theta,
$$

and [[causal-scale-theory/binary-geometry]] follows with its self-dual point at $\theta=0$.

## What happens without balance

For unequal positive weights, define

$$
\theta_0:=\frac12\ln\frac{w_+}{w_-}.
$$

The response becomes

$$
\eta(\theta)=\tanh(\theta+\theta_0),
\qquad
G_{\theta\theta}=\operatorname{sech}^2(\theta+\theta_0).
$$

Thus $Q^2=\mathbf1$ still gives a binary Casimir balance, but the maximum-susceptibility point is shifted. Declaring $\theta=0$ self-dual without establishing balance hides the bias inside the coordinate origin.

## Possible derivation from reflection

If a valid reflection exchanges $P_+$ and $P_-$ and the reference state is invariant under that reflection, then

$$
\omega_0(P_+)=\omega_0(P_-)
$$

follows. But [[open-questions/binary-reflection-realization|the full-algebra reflection]] is itself unconstructed. Balance is therefore **[ASSUMPTION — BINARY REFERENCE]** in the present closure, not a consequence of $Q^2=\mathbf1$ alone.

A microscopic wall returning stable unequal weights would not destroy binary geometry; it would replace the centered canonical pulse with its biased generalization and revise the crossing interpretation.
