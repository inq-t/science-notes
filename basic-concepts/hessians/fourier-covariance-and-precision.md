# Fourier Covariance and Precision

For a translation-invariant scalar field, precision is the inverse of the covariance operator on a declared physical subspace; in Fourier space this becomes reciprocal multiplication mode by mode. The identity is exact after zero modes, gauge directions, domains, and Fourier conventions are fixed, but it supplies neither a probability ontology nor a dynamical field equation.

## Fourier convention

Let \(\zeta(x)\) be a real dimensionless scalar on \(\mathbb R^3\), with

$$
\zeta(x)
=\int\frac{\mathrm d^3k}{(2\pi)^3}
e^{i\mathbf k\cdot\mathbf x}\zeta_{\mathbf k}.
$$

Translation invariance gives

$$
\langle\zeta_{\mathbf k}\zeta_{\mathbf k'}\rangle_c
=(2\pi)^3\delta^{(3)}(\mathbf k+\mathbf k')P_\zeta(k).
$$

The conventional dimensionless power is

$$
\Delta_\zeta^2(k)
:=\frac{k^3}{2\pi^2}P_\zeta(k).
$$

Suppose the covariance operator is positive and invertible after constants, gauge directions, constraints, and any further null directions have been removed. Its inverse is the precision operator. In the translation-invariant Fourier chart,

$$
\boxed{
\mathcal K_\zeta(k)
:=P_\zeta(k)^{-1}
=\frac{k^3}{2\pi^2\Delta_\zeta^2(k)}.}
$$

This is **[DEFINITION + EXACT OPERATOR IDENTITY]** on the stated physical subspace.

With this convention,

$$
[P_\zeta]=L^3,
\qquad
[\mathcal K_\zeta]=L^{-3}.
$$

The precision is therefore a three-dimensional spectral density. It is not the \(L^{-2}\) areal descent modulus of [[program-core/descent-response-geometry|the programme core]]. Relating the two requires an explicit boundary, integration, or soldering map.

## Gaussian weight and general effective action

For a centered Gaussian measure, the same operator appears in

$$
-\log\mathbb P[\zeta]
=\frac12
\int\frac{\mathrm d^3k}{(2\pi)^3}
\mathcal K_\zeta(k)
|\zeta_{\mathbf k}|^2
+\text{constant}.
$$

Outside a Gaussian theory, the raw quadratic coefficient of \(-\log\mathbb P\) need not be the exact inverse connected covariance. The exact general relation uses the Legendre effective action. If

$$
W[J]=\log Z[J],
\qquad
\bar\zeta=\frac{\delta W}{\delta J},
\qquad
\Gamma[\bar\zeta]
=\sup_J\bigl(J\cdot\bar\zeta-W[J]\bigr),
$$

then, under the differentiability, convexity, gauge-reduction, and invertibility hypotheses,

$$
\boxed{
\Gamma^{(2)}[\bar\zeta]
=\bigl(W^{(2)}[J]\bigr)^{-1}
=\mathcal C_\zeta^{-1}.}
$$

This is **[EXACT]** as a Legendre-duality statement. Lorentzian theories additionally require a state and a causal prescription; Euclidean, in-in, retarded, and time-ordered kernels are not interchangeable.

## Domains and zero modes

The reciprocal formula is shorthand for an inverse operator. It fails on a null direction. Removing the constant Fourier mode is justified when constants are a declared redundancy or constrained sector; a vanishing eigenvalue is not automatically gauge merely because inversion is inconvenient. The physical quotient must be established independently, as required by [[program-core/physical-quotient|the programme's quotient construction]].

On compact or curved spaces, Fourier momentum may be replaced by a self-adjoint spectral resolution. Positivity, domain, boundary conditions, and the treatment of the kernel remain part of the definition.

## Claim boundary

Knowing \(\mathcal K_\zeta\) fixes a two-point covariance on its domain. It does not by itself provide:

- a Lorentzian kinetic term or symplectic form;
- gauge constraints or a physical slicing;
- hyperbolicity, causal propagation, or stability;
- higher-point vertices;
- a state-selection or outcome law; or
- an identification of \(\zeta\) with cosmological curvature.

Those are additional representation and dynamics problems rather than consequences of operator inversion.
