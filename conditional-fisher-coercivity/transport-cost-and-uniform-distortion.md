# Transport Cost Is Not Uniform Distortion

The velocity minimizing average transport cost need not be the best connection for an all-observable spectral comparison. A rotating circle density has minimum-gradient transport with bounded mean-square cost but unbounded pointwise distortion as it concentrates. The same family admits rigid rotational transport with uniformly bounded distortion. Thus a law-preserving circulation can be useful, and deleting it by a least-cost prescription can worsen the estimate one actually needs.

## The minimum depends on the norm being minimized

In [[measure-preserving-horizontal-lifts|the smooth conditional construction]], the gradient velocity \(v_h=\nabla A_z^{-1}s_h\) is the unique minimum of conditional \(L^2\) velocity norm. If \(u_h\) is another solution of the continuity equation, integration by parts gives
\[
\langle v_h,u_h-v_h\rangle_{\beta_z}=0,\qquad
\|u_h\|_{\beta_z}^2=\|v_h\|_{\beta_z}^2+\|u_h-v_h\|_{\beta_z}^2.
\tag{TC1}
\]
Its squared norm is
\[
\boxed{
\|v_h\|_{\beta_z}^2
=\langle s_h,A_z^{-1}s_h\rangle_{\beta_z}
\le\rho_z^{-1}\|s_h\|_{\beta_z}^2.}
\tag{TC2}
\]
The inverse-weighted score is a transport metric; the unweighted score norm is Fisher information. Neither is a pointwise bound on \(v_h\).

## An exact circle counterexample

Let \(Y=Z=S^1\), both with their ordinary angular metrics, and define a conditional density relative to normalized Haar:
\[
b_z(y)=\frac{\exp(K\cos(y-z))}{I_0(K)},\qquad
I_0(K)=\frac1{2\pi}\int_0^{2\pi}e^{K\cos\theta}\,d\theta,
\qquad K\ge0.
\tag{TC3}
\]
The law is smooth and strictly positive for every finite \(K\). Put \(\theta=y-z\).
The continuity equation is
\(\partial_zb+\partial_y(bv)=0\), so every velocity has
\(bv=b+c(z)\).

Rigid rotation \(v_{\rm rot}=1\) is therefore an exact transport with pointwise norm one at every \(K\). For the minimum-gradient velocity, periodicity of its potential requires \(\int v\,dy=0\). Since \(\int b^{-1}dm=I_0(K)^2\), this selects
\[
\boxed{
v_{\min}(\theta)
=1-\frac{e^{-K\cos\theta}}{I_0(K)}.}
\tag{TC4}
\]
Direct integration gives
\[
\int v_{\min}^2b\,dm=1-I_0(K)^{-2}\le1.
\tag{TC5}
\]
Yet
\[
|v_{\min}(\pi)|=\frac{e^K}{I_0(K)}-1
\sim\sqrt{2\pi K}\quad(K\to\infty).
\tag{TC6}
\]
The asymptotic follows by the one-dimensional Laplace expansion of the defining integral at its maximum. Hence no bound on the mean-square transport cost alone bounds its pointwise distortion. The omitted circulation \(v_{\rm rot}-v_{\min}\) has weighted divergence zero and weighted squared norm \(I_0(K)^{-2}\): its very small average cost hides its large effect in the low-density region.

Rigid rotation is not the minimum-\(L^\infty\) solution either. [[bounded-transport-and-cut-flux#The exact circle optimum|The cut-flux minimax theorem]] gives the exact optimum \(B_*=\tanh K\), attained by \(v_\infty=1-e^{-K\cos\theta}/\cosh K\). Thus the same family explicitly distinguishes minimum average cost, a simple uniformly bounded transport, and minimum maximum speed.

## Why rare regions still matter to the complete form

For the lifted derivative \(D=\partial_z+v\partial_y\), the form
\(\int(|\partial_y f|^2+|Df|^2)d\mu\) has principal quadratic symbol
\[
(\eta,\xi)\longmapsto |\eta|^2+|\xi+v\eta|^2.
\]
Its norm relative to \(|\eta|^2+|\xi|^2\) is \(C(|v|)\) from (MH11).
At each fixed finite \(K\), smooth wave packets supported near \(\theta=\pi\), with frequency sent to infinity after the support is fixed, recover that pointwise symbol in their Rayleigh ratios. Strictly positive density multiplies numerator and denominator equally. Therefore the optimal all-test form-comparison constants for \(v_{\min}\) diverge with \(K\).

Rigid rotation instead gives the uniform bound \(C(1)=(3+\sqrt5)/2\). This does not by itself prove a uniform conditional or physical gap: the retained and vertical forms still require their own bounds. It proves that minimizing Wasserstein tangent cost can select the wrong transport for the desired operator inequality.

The distinction is geometric. The angular one-form \(dy\) is closed but not exact on the circle. Gradient minimization removes that circulation; state preservation does not require its removal. No claim about spacetime knots or a physical mass follows from this example.

## Even a bounded Fisher-to-gap ratio does not force this comparison

There is a stronger smooth compact counterexample in hidden dimension \(d>2\). On a fixed flat torus, take a nonconstant smooth bump supported in a coordinate ball and put
\[
\phi_\varepsilon(y)=\varepsilon^{\,2-d/2}\phi(y/\varepsilon),
\qquad s_\varepsilon=-\Delta\phi_\varepsilon.
\tag{TC7}
\]
Subtracting the mean of \(\phi_\varepsilon\) does not change its derivatives. Scaling gives constant \(\|s_\varepsilon\|_2\), while
\(\|\nabla\phi_\varepsilon\|_\infty\asymp\varepsilon^{1-d/2}\to\infty\).
Choose an integer \(m_\varepsilon\ge2\|s_\varepsilon\|_\infty\) and, on \(Z=S^1\), let
\[
b_z(y)=1+\frac{\sin(m_\varepsilon z)}{m_\varepsilon}s_\varepsilon(y).
\tag{TC8}
\]
These normalized densities stay between \(1/2\) and \(3/2\). Their conditional gaps are at least one third of the Haar gap, and their Fisher coefficients are at most \(2\|s_\varepsilon\|_2^2\), uniformly. At \(z=0\), however, the minimum-gradient velocity is exactly \(\nabla\phi_\varepsilon\). Localized oscillatory tests again force diverging shear constants.

The joint density relative to product Haar also stays within those same bounds, so its original product-gradient gap stays uniformly positive. The failing estimate diagnoses this particular connection comparison, not the law's gap. Minimum average transport cost, Fisher control and uniform multiplication-form control are distinct requirements.

The [[receipts/measure_preserving_lift_receipt.py|finite receipt]] checks the circle continuity equations, costs and increasing distortion. The higher-dimensional example rests on exact bump scaling, not on a sampled torus calculation.
