# Flatness Tails and Fold Conditions

The asymptotic behavior and double-root condition of the generalized CST flatness function follow analytically from its exponential matter, radiation, and \(\operatorname{sech}^2\) factors. They classify possible root geometry but do not determine the number of roots for arbitrary amplitudes and abundances.

For

$$
F_\nu(x)
=\left(\Omega_{m0}e^{3x}+\Omega_{r0}e^{4x}\right)
\operatorname{sech}^2(\nu x),
\qquad
\nu>0,
$$

suppose first that \(\Omega_{r0}>0\). Since

$$
\operatorname{sech}^2(\nu x)
\sim4e^{-2\nu x}
\qquad(x\to+\infty),
$$

the radiation term dominates and

$$
\boxed{
F_\nu(x)
\sim4\Omega_{r0}e^{(4-2\nu)x}.}
$$

Consequently,

$$
\begin{array}{c|c}
0<\nu<2 & F_\nu(x)\to+\infty,\\
\nu=2 & F_\nu(x)\to4\Omega_{r0},\\
\nu>2 & F_\nu(x)\to0.
\end{array}
$$

If \(\Omega_{r0}=0\) and \(\Omega_{m0}>0\), then instead

$$
F_\nu(x)
\sim4\Omega_{m0}e^{(3-2\nu)x},
$$

so the corresponding dust-tail threshold is \(\nu=3/2\).

These thresholds classify only the far tail. A finite graph can cross a given positive threshold zero, one, or several times depending on all parameters.

## Fold equation

A double root of

$$
F_\nu(x)=T_{\mathfrak R}
$$

must also obey \(F_\nu'(x)=0\). Where \(F_\nu>0\), this is equivalent to

$$
\boxed{
\frac{3\Omega_{m0}e^{3x}+4\Omega_{r0}e^{4x}}
{\Omega_{m0}e^{3x}+\Omega_{r0}e^{4x}}
-2\nu\tanh(\nu x)=0.}
$$

Solving the closure and fold equations together locates saddle-node points of the root equation. The root equation may have saddle-node bifurcations even though the separately conserved equation-of-state flow in [[causal-scale-theory/theorems/rigid-sech-response-identities|the rigid response theorem]] does not.

Benchmark fold locations belong to [[causal-scale-theory/receipts/README|the arithmetic receipts]]. They are not universal width bounds.
