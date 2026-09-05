# Nonlinear Transport of the Actual Gauge Fibers

The normalized compact gauge readout admits smooth state-preserving transport of its actual reverse conditional laws at every finite regulator. In an explicit strong-coupling regime, a conditional heat-gradient estimate bounds the whole transport map pointwise, uniformly in volume under path-incidence control. This realizes the nonlinear retained/fiber interface and compares its gradient form with the unchanged fine Wilson law. It does not improve the known strong-coupling gap or extend it through the weak-coupling continuum trajectory.

## A global conditional carrier, including singular path averages

Use the \(SU(r)\) product metrics and normalized kernel of [[nonlinear-conditional-gauge-response|the nonlinear conditional calculation]]. The actual joint law is
\[
\mathbb P(dU,dV)=\mu_\beta(dU)q_\kappa(V\mid U)dV
=\bar\mu(dV)\nu_V(dU),
\tag{GT1}
\]
where \(\mu_\beta\) is the original fine Wilson law, and
\[
d\nu_V=\mathcal Z(V)^{-1}e^{-A_V}dU,\qquad
A_V=S_\beta-\kappa\sum_b\phi(V_b,Z_b(U))
+\sum_b\log N_\kappa(Z_b(U)).
\tag{GT2}
\]
The hidden manifold is the fixed compact connected \(SU(r)^E\), not a singular gauge quotient. All finite-parameter densities are positive and smooth, even where \(Z_b\) loses rank. Integrating \(V\) leaves \(\mu_\beta\) unchanged. Omitting the last normalizer in (GT2) would destroy that claim.

For a retained tangent \(X=(X_b)\), write
\[
\ell_X=d_VA_V[X],\qquad
\sigma_X=d_V\log\nu_V[X]=-\ell_X+\nu_V(\ell_X).
\tag{GT3}
\]
The conditional generator
\(L_V=-\Delta_U+\nabla_UA_V\cdot\nabla_U\)
has a unique mean-zero inverse on smooth centered scores. Define
\[
\phi_X=L_V^{-1}\sigma_X,\qquad v_X=\nabla_U\phi_X.
\tag{GT4}
\]
[[conditional-fisher-coercivity/measure-preserving-horizontal-lifts|The horizontal-lift theorem]] now applies: \(\nu_V\) is transported along every finite coarse path, and
\[
d_V(\nu_VF)[X]=\nu_V(d_VF[X]+d_UF[v_X]).
\tag{GT5}
\]
This constructs finite nonlinear transport at all finite couplings. It does not assert flatness or uniform bounds in the regulator.

The joint endpoint gauge actions preserve the product metrics and (GT2). Uniqueness of the mean-zero solution makes \(v\) equivariant under the corresponding actions on both tangent bundles. Thus the lifted form preserves the global gauge-invariant observable subspace without choosing orbit-space coordinates.

## A pointwise transport estimate from the actual conditional action

Let \(D\) be the nonnegative incidence matrix in (NG6), and let
\(\mathsf P_{be}=\sum_iw_{bi}n_{bi,e}\), \(s=\|\mathsf P\|_{2\to2}\).
Suppose
\[
\rho:=r^2/2-\|D\|_{2\to2}>0.
\tag{GT6}
\]
This is a full Bakry--Emery bound
\(\operatorname{Ric}+\operatorname{Hess}A_V\ge\rho g\),
not merely the conclusion of a scalar Poincare inequality.

For \(P_t^V=e^{-tL_V}\), the Bochner inequality and compact maximum principle give
\[
\|\nabla P_t^V f\|_\infty\le e^{-\rho t}\|\nabla f\|_\infty.
\]
Using the mean-zero Poisson representation,
\[
v_X=\int_0^\infty\nabla P_t^V\sigma_X\,dt,
\qquad
\|v_X\|_\infty\le\rho^{-1}\|d_U\ell_X\|_\infty.
\tag{GT7}
\]
There is no derivative of the coarse normalizing constant in \(d_U\sigma_X\). The hidden normalizer remains in \(L_V\).

Path differentiation gives a pointwise estimate on the whole retained tangent:
\[
\|d_U\ell_X(U)\|
\le\kappa\|\mathsf P^\top(|X_b|)_b\|_2
\le\kappa s\|X\|.
\]
Consequently
\[
\boxed{\sup_{U,V}\|X\mapsto v_X(U)\|\le B:=\kappa s/\rho.}
\tag{GT8}
\]
Both path lengths and path reuse enter \(s\). There is no additional factor counting all retained links. A uniform positive lower bound on \(\rho\) and a uniform upper bound on \(\kappa s\) supply volume uniformity at this one blocking step. In particular, a bound on path incidence alone does not control a diverging readout strength.

## Returning a bound to the unchanged fine marginal

The exact effective Hessian from [[joint-fisher-response-of-normalized-gauge-blocking|joint Fisher response]] is the conditional mean Hessian minus the reverse score covariance. Since
\(\operatorname{Hess}_V A_V\ge-\kappa g_V\) and
\(\operatorname{Var}_{\nu_V}\ell_X\le\kappa^2s^2\|X\|^2/\rho\),
the actual coarse marginal has the sufficient curvature bound
\[
\lambda_{\rm ret}:=r^2/2-\kappa-\frac{\kappa^2s^2}{\rho}>0.
\tag{GT9}
\]
The inequality, when positive, proves its Poincare gap is at least \(\lambda_{\rm ret}\). It is not a choice of an unrelated coarse prior.

Define on the joint law
\[
\mathcal E_{\rm conn}(F)
=\int\left(|d_UF|^2+
|d_VF+v^*d_UF|^2\right)d\mathbb P.
\tag{GT10}
\]
Conditional expectation reduces this operator, and (MH9) gives gap at least
\(\delta=\min\{\rho,\lambda_{\rm ret}\}\).
For an original fine observable \(F(U)\), (GT8) instead gives the restricted comparison
\[
\mathcal E_{\rm conn}(F)
\le(1+B^2)\mathcal E_{\mu_\beta}(F).
\]
Both its variance and the last gradient integral use the unchanged fine marginal. Therefore
\[
\boxed{\lambda_{\rm fine}\ge
\frac{\min\{\rho,\lambda_{\rm ret}\}}{1+(\kappa s/\rho)^2}.}
\tag{GT11}
\]
This is an actual-law nonlinear comparison, not an equality between auxiliary and physical clocks.

The point is the constructed interface, not a better strong-coupling constant. The sufficient condition (GT6) already implies an ordinary fine Wilson curvature bound, and (GT11) need not improve it. At \(\kappa=0\), retained data are independent Haar and all original difficulty remains in the hidden law. Neither a small readout strength nor the existence of a coarse gap can solve the fine theory by itself.

## What survives outside the curvature regime

Finite compactness still supplies (GT4)--(GT5) when (GT6) fails. If
\(\Delta_A=\sup_V\operatorname{osc}_UA_V\), a product-Haar Poincare constant \(\lambda_H\) gives a crude conditional gap \(\lambda_H e^{-\Delta_A}\). Hence
\[
\|v_X\|_{L^2(\nu_V)}^2
\le\lambda_H^{-1}e^{\Delta_A}
\|\sigma_X\|_{L^2(\nu_V)}^2.
\]
For the stated action, the safe finite bound
\(\Delta_A\le2\beta N_{\rm plaquette}+4\kappa N_{\rm readout}\)
already exposes its extensive deterioration. Smooth elliptic regularity gives finite higher norms at a fixed regulator, not uniform estimates as those counts grow.

[[conditional-fisher-coercivity/transport-cost-and-uniform-distortion|Minimum transport cost does not control uniform distortion]]. The connection may instead be adjusted by a conditionally divergence-free field, provided gauge covariance, metric domination and any claimed spatial localization are preserved. Such a correction is a concrete freedom to investigate, not an arbitrary mass insertion.

[[conditional-fisher-coercivity/bounded-transport-and-cut-flux|Cut-flux duality]] now gives an exact criterion for the bounded-transport part, including one joint tangent operator and smooth realization with a strict margin. [[su3-context-flux-obstruction|The one-link obstruction]] shows that circulation cannot always repair a bad comparison. Its conditioned carrier differs from this normalized soft posterior, so it neither proves nor refutes a uniform bound for (GT2).

Beyond one-step strong coupling the remaining obligations are explicit: use the actual generated actions, bound transport distortion or an adequate relative form, control the retained law, and preserve the physical source and reconstruction maps. Pointwise bounded transport need not be spatially short range, nor does it prove reflection positivity or a continuum quantum field theory.
