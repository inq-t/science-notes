# Relative Entropy on the Balanced Binary Line

Relative entropy between two points of the balanced binary family is an exact Bregman divergence for \(\psi(\theta)=\ln\cosh\theta\). Its reflected specialization is even, while its coincidence Hessian recovers the binary BKM metric.

Under the hypotheses of [[balanced-exponential-family]], commutativity gives

$$
\ln\rho_\theta
=\ln\rho_0+\theta Q-\psi(\theta)\mathbf1.
$$

For \(\theta,\vartheta\in\mathbb R\), the Umegaki relative entropy is therefore

$$
\begin{aligned}
D(\rho_\theta\Vert\rho_\vartheta)
&:=\operatorname{Tr}
\rho_\theta
\left(\ln\rho_\theta-\ln\rho_\vartheta\right)\\
&=(\theta-\vartheta)m(\theta)
-\psi(\theta)+\psi(\vartheta).
\end{aligned}
$$

Hence

$$
\boxed{
D(\rho_\theta\Vert\rho_\vartheta)
=(\theta-\vartheta)\tanh\theta
-\ln\cosh\theta
+\ln\cosh\vartheta.}
$$

This is **[EXACT — AFTER BALANCED BINARY REDUCTION]**.

## Reflection

Because \(\psi\) is even and \(m\) is odd,

$$
\boxed{
D(\rho_\theta\Vert\rho_{-\theta})
=2\theta\tanh\theta.}
$$

The reverse divergence has the same value, so the Jeffreys divergence is

$$
\boxed{
D(\rho_\theta\Vert\rho_{-\theta})
+D(\rho_{-\theta}\Vert\rho_\theta)
=4\theta\tanh\theta.}
$$

Both expressions are even under \(\theta\mapsto-\theta\). They measure separation from the balanced reflection point but cannot choose an orientation of traversal.

## Fixed reference and coincidence

Taking \(\vartheta=0\) gives

$$
\boxed{
D(\rho_\theta\Vert\rho_0)
=\theta\tanh\theta-\ln\cosh\theta.}
$$

Its derivative is

$$
\frac{\mathrm d}{\mathrm d\theta}
D(\rho_\theta\Vert\rho_0)
=\theta\operatorname{sech}^2\theta,
$$

which is nonzero away from \(\theta=0\).

By contrast, for an infinitesimal neighboring state,

$$
\boxed{
D(\rho_{\theta+\delta\theta}\Vert\rho_\theta)
=\frac12
g^{\mathrm{bin}}_{\theta\theta}
(\delta\theta)^2
+O((\delta\theta)^3).}
$$

The fixed-reference divergence and the coincidence Hessian answer different questions. The second-order local metric cannot be substituted for the first quantity along a finite interval.

## Boundary of the result

The formula uses faithful commuting density operators from one common finite-dimensional carrier. Relative entropy can diverge at the nonfaithful endpoints of [[fisher-line|the metric completion]]. Noncommuting families retain a BKM coincidence Hessian under suitable regularity, but not this elementary scalar Bregman formula without further work.

