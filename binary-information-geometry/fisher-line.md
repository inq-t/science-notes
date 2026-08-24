# The Binary Fisher Line

The balanced binary BKM metric is globally flattened by the Gudermannian, making the complete exponential family a finite open interval of length \(\pi\). This is an intrinsic statement about the normalized one-dimensional statistical manifold.

Under the hypotheses of [[balanced-exponential-family]], the line element is

$$
\mathrm ds_{\mathrm{bin}}^2
=g^{\mathrm{bin}}_{\theta\theta}\,\mathrm d\theta^2
=\operatorname{sech}^2\theta\,\mathrm d\theta^2.
$$

Define

$$
\phi
:=\operatorname{gd}(\theta)
:=\arctan(\sinh\theta).
$$

Since

$$
\frac{\mathrm d\phi}{\mathrm d\theta}
=\operatorname{sech}\theta,
$$

one obtains

$$
\boxed{
\mathrm ds_{\mathrm{bin}}^2=\mathrm d\phi^2.}
$$

Moreover,

$$
\lim_{\theta\to\pm\infty}\phi
=\pm\frac{\pi}{2}.
$$

Thus the map

$$
\theta\longmapsto\phi
$$

is an isometry from the binary exponential line onto the Euclidean interval

$$
\left(-\frac{\pi}{2},\frac{\pi}{2}\right).
$$

The distance between two finite parameters is

$$
\boxed{
d_{\mathrm{bin}}(\theta_1,\theta_2)
=
\left|
\operatorname{gd}(\theta_2)
-\operatorname{gd}(\theta_1)
\right|,}
$$

and the total end-to-end length is

$$
\boxed{
\int_{-\infty}^{+\infty}
\sqrt{g^{\mathrm{bin}}_{\theta\theta}}\,\mathrm d\theta
=\int_{-\infty}^{+\infty}
\operatorname{sech}\theta\,\mathrm d\theta
=\pi.}
$$

These are **[EXACT — AFTER BALANCED BINARY REDUCTION]**.

## Completion and boundary

The statistical manifold itself is the open interval. Its metric completion adds the two limiting distributions supported entirely in the \(Q=+1\) and \(Q=-1\) sectors. Those endpoints are not faithful, so formulas requiring faithful density operators apply only before completion or by a controlled limit.

Finite normalized Fisher length does not determine an extensive physical norm. Replicating the binary channel, changing its multiplicity, or attaching a scale-dependent prefactor leaves the intrinsic normalized line unchanged while changing any extensive capacity.

