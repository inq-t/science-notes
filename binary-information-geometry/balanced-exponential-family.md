# The Balanced Binary Exponential Family

A faithful reference state with equal total weight in the two eigenspaces of a normalized involution generates a centered exponential family with polarization \(\tanh\theta\) and binary BKM metric \(\operatorname{sech}^2\theta\). The result is exact after the balanced binary reduction has been granted.

Let \(\mathcal H\) be finite dimensional, let \(\rho_0\) be a faithful density operator on \(\mathcal H\), and let

$$
Q=Q^*,
\qquad
Q^2=\mathbf1,
\qquad
P_\pm:=\frac{\mathbf1\pm Q}{2}.
$$

Assume

$$
[\rho_0,Q]=0
$$

and the balanced-weight condition

$$
\operatorname{Tr}(\rho_0P_+)
=\operatorname{Tr}(\rho_0P_-)
=\frac12.
$$

For \(\theta\in\mathbb R\), define

$$
\rho_\theta
:=
\frac{
e^{\theta Q/2}\rho_0e^{\theta Q/2}}
{Z_{\rho_0}(\theta)},
\qquad
Z_{\rho_0}(\theta)
:=\operatorname{Tr}(\rho_0e^{\theta Q}),
\qquad
\psi(\theta):=\ln Z_{\rho_0}(\theta).
$$

## Partition function

Involutivity gives

$$
e^{\theta Q}
=e^\theta P_++e^{-\theta}P_-
=\cosh\theta\,\mathbf1+\sinh\theta\,Q.
$$

The balanced weights imply

$$
\operatorname{Tr}(\rho_0Q)=0,
$$

and hence

$$
\boxed{
Z_{\rho_0}(\theta)=\cosh\theta,
\qquad
\psi(\theta)=\ln\cosh\theta.}
$$

## Mean and metric

Define the binary polarization

$$
m(\theta):=\operatorname{Tr}(\rho_\theta Q).
$$

Differentiating the log partition function gives

$$
\boxed{
m(\theta)
=\psi'(\theta)
=\tanh\theta.}
$$

Because this is a commuting exponential family, its BKM metric in the exponential coordinate is the variance of \(Q\):

$$
\boxed{
g^{\mathrm{bin}}_{\theta\theta}
:=\psi''(\theta)
=\operatorname{Var}_{\rho_\theta}(Q)
=\operatorname{sech}^2\theta.}
$$

Combining this with [[involutive-casimir|the involutive Casimir identity]] yields

$$
\boxed{
m(\theta)^2
+g^{\mathrm{bin}}_{\theta\theta}
=1.}
$$

These statements are **[EXACT — AFTER BALANCED BINARY REDUCTION]**.

## What balance contributes

For unequal positive weights

$$
w_\pm:=\operatorname{Tr}(\rho_0P_\pm),
\qquad
w_++w_-=1,
$$

set

$$
\theta_0:=\frac12\ln\frac{w_+}{w_-}.
$$

The same calculation gives

$$
m(\theta)=\tanh(\theta+\theta_0),
\qquad
g^{\mathrm{bin}}_{\theta\theta}
=\operatorname{sech}^2(\theta+\theta_0).
$$

Thus involutivity still gives a binary Casimir identity, but the zero-polarization and maximum-susceptibility point is \(\theta=-\theta_0\), not \(\theta=0\). Balance selects the centered origin; it is not derived from \(Q^2=\mathbf1\).

## Boundary of the theorem

The theorem does not establish that a larger algebra has a preferred binary quotient, that a reflection enforces balance, or that the normalized metric has any particular extensive multiplicity. If \([\rho_0,Q]\neq0\), the simple commuting covariance calculation does not apply in this form. Infinite-dimensional and type-III extensions require their own domain, faithfulness, and finiteness or renormalization hypotheses.

