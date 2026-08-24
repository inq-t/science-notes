# Unrestricted Response Is Not Predictive

If a scalar response coefficient is allowed to be an arbitrary positive function of momentum, then it can represent every positive scalar two-point spectrum on the same domain. The response language remains a useful typing or representation, but the scalar spectrum cannot falsify the unrestricted class; prediction begins only after independent restrictions are imposed.

## Surjectivity onto positive spectra

Let \(\Delta_{\mathrm{target}}^2(k)>0\) be any positive scalar dimensionless power on an interval \(I\subset(0,\infty)\). Define

$$
C_{\mathrm{target}}(k)
:=\frac{1}{2\pi^2\Delta_{\mathrm{target}}^2(k)}.
$$

Then

$$
\mathcal K_\zeta(k)
=C_{\mathrm{target}}(k)|k|^3
$$

and [[basic-concepts/hessians/fourier-covariance-and-precision|Fourier inversion]] reproduce the target exactly:

$$
\Delta_\zeta^2(k)
=\Delta_{\mathrm{target}}^2(k).
$$

Likewise, in the normalization often used for a continued scalar stress response,

$$
\Delta_\zeta^2(k)
=\frac{4}{\pi^4c^{(0)}(k)},
$$

the choice

$$
c^{(0)}_{\mathrm{target}}(k)
=\frac{4}{\pi^4\Delta_{\mathrm{target}}^2(k)}
$$

fits the same arbitrary positive target.

Therefore:

> **[NO-GO]** An unrestricted positive scalar response function cannot be falsified by the shape or normalization of one positive scalar two-point spectrum, because the response may be defined pointwise from that spectrum.

## What the no-go does and does not say

The statement concerns explanatory and empirical freedom. It does not say that a response representation is mathematically false or physically useless. Such a representation can expose positivity, scaling, analyticity, tensor decomposition, or a route to microscopic calculation.

It also does not apply after independent structure restricts the function. Predictive content can enter through:

- a microscopic calculation of \(C(k)\) or \(c^{(0)}(k)\);
- a finite-dimensional family fixed before examining the target data;
- a flow equation with independently fixed boundary data;
- analyticity, locality, unitarity, or Ward-identity constraints that exclude spectra;
- relations to tensor and higher-point response from the same theory; or
- a joint relation to background, matter, or other observables.

## Member-level falsification

The exact critical member \(C(k)=C_*\) predicts a scale-invariant two-point shape. The constant-exponent member predicts zero running by [[tilt-and-running-identities|its defining assumption]]. A specified microscopic member may predict features, tensor ratios, or higher-point shapes. Those narrower classes can fail even though the unrestricted positive-function class survives by redefinition.

## Anti-circularity

If the response function is reconstructed from the measured spectrum and is then cited as an explanation of that spectrum, the construction has changed variables rather than supplied an independent law. This is the spectral instance of [[wall-construction-interface/elimination-test|the wall independence test]] and [[program-core/explanatory-economy|the programme's explanatory-economy rule]].
