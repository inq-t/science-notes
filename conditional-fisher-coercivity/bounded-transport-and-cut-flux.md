# Bounded Transport Is a Cut-Flux Condition

A conditional state can be transported at bounded speed exactly when its required probability transfer across every cut fits the cut's weighted capacity. This is a source-dependent geometric quotient, not a Fisher norm or a spectral gap. For several context directions, one linear transport operator requires a stronger, matrix-valued dual test. Both criteria have smooth near-optimal realizations on a fixed compact smooth family, so they test the connection actually needed for the horizontal form comparison.

## The scalar quotient

Let \(Y\) be a closed connected positive-dimensional Riemannian manifold, \(m\) its normalized volume, and \(d\beta=b\,dm\), with smooth \(b>0\) and \(\int b\,dm=1\). Let \(s\) be a smooth real score with \(\beta(s)=0\). The continuity equation and its minimum speed are
\[
\operatorname{div}(bv)=-bs,\qquad
B_*(s;b)=\inf_v\|v\|_{L^\infty}.
\tag{BF1}
\]
The first infimum is over essentially bounded vector fields satisfying the equation distributionally. Smooth solutions exist by the weighted Poisson construction in [[measure-preserving-horizontal-lifts|horizontal lifts]].

For a smooth proper domain \(A\), define the weighted perimeter
\(\operatorname{Per}_b(A)=\int_{\partial A}b\,d\Sigma_m\), where surface and volume use the same normalization. Then
\[
\boxed{
B_*(s;b)
=\sup_{df\ne0}\frac{|\beta(sf)|}{\beta(|df|)}
=\sup_A\frac{|\int_A s\,d\beta|}{\operatorname{Per}_b(A)}.}
\tag{BF2}
\]
Tests \(f\) are smooth and real. Cuts with zero perimeter are omitted. The weak minimum is attained.

**Proof.** The weak equation is
\(\beta(sf)=\beta[df(v)]\), which proves the lower bound on every admissible speed. Conversely the functional
\[
df\longmapsto\beta(sf)
\]
on the smooth-gradient subspace of \(L^1(T^*Y,\beta)\) is well defined: equal gradients differ by a constant, annihilated by the mean-zero score. Its norm is the middle expression of (BF2). Hahn--Banach extends it without changing that norm. The \(L^1\)-dual representation gives an \(L^\infty\) vector field attaining the bound and satisfying the weak equation.

To pass from cuts to tests, subtract the minimum of \(f\), use layer cake for \(\beta(sf)\), and apply the cut bound to the regular superlevel domains. Coarea gives
\(\int\operatorname{Per}_b(\{f>t\})\,dt=\beta(|df|)\). Smooth collar approximations of each domain's indicator give the converse inequality. Thus the geometry of all cuts, not merely a chosen bottleneck, determines the scalar optimum.

The classical continuous-flow precedent is [[library/max-flow-min-cut-in-anisotropic-networks/inq|Nozawa's anisotropic max-flow/min-cut theorem]], especially Theorems 4.4 and 4.9 and Remark 4.11. The closed-manifold formulation above has its own proof; no boundary-domain theorem or smooth attainment is silently imported.

For the weighted Cheeger constant
\[
h_b=\inf_A\frac{\operatorname{Per}_b(A)}
{\min(\beta(A),\beta(A^c))},
\]
mean-zero cancellation immediately gives
\[
B_*(s;b)\le \|s\|_\infty/h_b.
\tag{BF3}
\]
The exact source-dependent quotient can be much smaller. A Poincare lower bound alone does not yield a lower bound on \(h_b\) by reversing Cheeger's inequality.

## One operator for all context directions

Take \(k\) real mean-zero scores \(s_i\). A connection must supply one linear map \(V(y):\mathbb R^k\to T_yY\), not independently selected nonlinear choices for every direction. Require \(\operatorname{div}(bV_i)=-bs_i\) columnwise. Write
\[
B_{\rm joint}=\inf_V\|V\|_{L^\infty,\mathrm{op}}.
\]
For \(F=(f_1,\ldots,f_k)\), regard \(dF\) as the matrix of gradient columns and let \(\|\cdot\|_*\) be its nuclear norm. Then
\[
\boxed{
B_{\rm joint}
=\sup_{dF\ne0}
\frac{|\sum_i\beta(s_i f_i)|}
{\int\|dF\|_*\,d\beta}.}
\tag{BF4}
\]
The same Hahn--Banach argument now uses the finite-rank bundle-valued \(L^1\) nuclear norm, whose dual is the pointwise operator norm. It also attains a weak minimum.

Scalar directional tests give only
\[
\begin{aligned}
B_{\rm dir}
&:=\sup_{\|h\|=1} B_*\!\left(\sum_i h_i s_i;b\right)
=\sup_A\frac{\|\int_A s\,d\beta\|_2}{\operatorname{Per}_b(A)},\\
B_{\rm dir}&\le B_{\rm joint}\le\sqrt{k}\,B_{\rm dir}.
\end{aligned}
\tag{BF5}
\]
The upper bound assembles optimal columns; it does not say that the scalar certificate has the same constant as the joint one.

This distinction already occurs on a smooth circle. Let \(b=1\), and choose a smooth periodic \(F:S^1\to\mathbb R^2\) whose image is the boundary of an equilateral triangle of circumradius one. A parametrization flat at the three vertices makes the polygonal image compatible with smooth \(F\). Put \(s=-F'\). Every joint velocity is \(V=F+c\). Its smallest uniform norm is the enclosing-circle radius, namely one. In a fixed direction \(h\), the scalar optimum is half the oscillation of \(h\cdot F\). Maximizing over unit \(h\) gives half the triangle's diameter:
\[
B_{\rm dir}=\sqrt3/2<1=B_{\rm joint}.
\tag{BF6}
\]
These scores are genuine tangents of the positive normalized family \(b_z=1+z\cdot s\) for sufficiently small \(z\). The example disproves equality, not every possible dimension-independent comparison.

## Smooth realization without changing the infimum

Weak bounded flux alone does not define a smooth flow. Here the compact smooth hypotheses close that gap with any strictly positive tolerance.

Identify \(u=bv\) with a one-form, put \(f=bs\), and let \(\Delta_1,\Delta_0\) be the nonnegative Hodge Laplacians on one-forms and functions; \(\Delta_0=-\operatorname{div}\nabla\). Define
\[
u_t=e^{-t\Delta_1}u+
\nabla\Delta_0^{-1}(f-e^{-t\Delta_0}f).
\tag{BF7}
\]
The inverse acts on mean-zero functions. Hodge commutation with divergence proves \(\operatorname{div}u_t=-f\) exactly. Since \(f\) is smooth, the correction tends to zero smoothly.

A Ricci lower bound on the fixed compact manifold gives heat domination:
\[
|e^{-t\Delta_1}u|
\le e^{Ct}e^{-t\Delta_0}|u|
\le B e^{Ct}e^{-t\Delta_0}b.
\]
After division by \(b\), the final factor tends uniformly to one. Consequently \(v_t=u_t/b\) is smooth, solves the same equation, and has norm at most \(B+o(1)\). Therefore smooth and weak infima agree; smooth attainment at the exact infimum is not asserted.

For (BF4), apply the construction columnwise. Heat domination applied to \(u h\) for every unit \(h\), with the same scalar bound, controls the operator norm without adding a \(\sqrt{k}\) factor.

Now let \(Z\) also be a compact smooth Riemannian manifold and \(b_z\) a smooth positive conditional family. Suppose its tangent-linear score satisfies
\[
\sup_{z\in Z} B_{\rm joint}(z)\le B_0.
\tag{BF8}
\]
For every \(\varepsilon>0\), there is a globally smooth tangent-linear connection with exact continuity and \(\sup_z\|V_z\|_\infty\le B_0+\varepsilon\).

To see this, choose smooth near-optimal columns at \(z_0\) with a strict margin, and a local orthonormal tangent frame. Write
\(A_z=-b_z^{-1}\operatorname{div}(b_z\nabla)\). Extend the columns locally by
\[
v_i(z)=\frac{b_{z_0}}{b_z}v_i(z_0)
+\nabla A_z^{-1}
\left(s_i(z)-\frac{b_{z_0}}{b_z}s_i(z_0)\right).
\tag{BF9}
\]
The correction's source has exactly zero \(\beta_z\)-mean, vanishes at \(z_0\), and depends smoothly on \(z\). Elliptic inversion on the mean-zero subspace gives a smooth correction tending to zero. The continuity equation remains exact. A finite cover and a partition of unity depending only on \(z\) glue these local bundle maps. Convexity preserves the bound, and no vertical divergence differentiates the partition.

No flatness, global tangent frame, or equality of fibers' pointwise presentations is required. The construction gives the norm certificate consumed by [[measure-preserving-horizontal-lifts|the curved horizontal form theorem]]. It does not give regulator-uniform derivative estimates, spatial locality of the connection, or a spectral lower bound without the separate vertical and retained estimates.

## The exact circle optimum

On \(S^1\), choose a periodic flux primitive \(F'=-bs\). All scalar velocities are \(v=(F+c)/b\), so
\[
\boxed{
B_*=\min_c\sup_y\frac{|F(y)+c|}{b(y)}
=\sup_{y,t}\frac{|F(y)-F(t)|}{b(y)+b(t)}.}
\tag{BF10}
\]
Indeed, speed at most \(B\) is equivalent to the simultaneous intervals
\(-Bb(y)-F(y)\le c\le Bb(y)-F(y)\). Their pairwise intersection condition is precisely the last bound; compactness gives a common point.

For a rotating density \(b(y-z)\), take \(F=b\). Its extrema give
\[
B_*=\frac{b_{\max}-b_{\min}}{b_{\max}+b_{\min}},
\qquad
c_*=-\frac{2b_{\max}b_{\min}}{b_{\max}+b_{\min}}.
\tag{BF11}
\]
In the von Mises family from [[transport-cost-and-uniform-distortion|the transport-cost counterexample]], this becomes
\[
\boxed{
B_*=\tanh K,\qquad
v_\infty(y,z)=1-\frac{e^{-K\cos(y-z)}}{\cosh K}.}
\tag{BF12}
\]
It is a smooth exact optimizer. Rigid rotation has uniformly bounded speed but is not optimal; the minimum-\(L^2\) gradient transport has diverging maximum speed. Three distinct optimization problems have now been separated on the same law.

The hyperbolic tangent in (BF12) is an extremal density contrast. It is not an identification with the state-response rate or gravity matching in [[program-core/ruble-equations|Ruble's equations]].

## What the quotient operates on

Here the input is a *specified state tangent* \(s_h\), and the output is a vertical vector field carrying that tangent while preserving normalization. The quotient in (BF2) has units of fiber distance per base-parameter unit once those metrics are declared. It measures the largest required probability transfer divided by the available weighted boundary area. It is not yet a mass, a causal speed, or an area--entropy conversion.

This fills a quantitative part of [[wall-construction-interface/cross-fiber-transport|cross-fiber transport]] for compact commutative conditional fibers. It does not construct the type-III correspondence, local causal net, physical cut, or unit calibration required by that interface. Nor does transporting a probability law select an outcome or orient an irreversible record.

[[rg-covariance-residue/su3-context-flux-obstruction|The Wilson example]] shows why this distinction matters: a source can require order-one transfer across an exponentially depleted cut, forcing every single-link lift to become large. The repair must then alter the retained information or the active carrier, rather than just optimize the same Poisson solver.

The [[receipts/cut_flux_transport_receipt.py|finite receipt]] checks circle optima, interval feasibility, and a strict joint-versus-directional three-cycle witness. Hahn--Banach, coarea, smoothing and the parameter-selection proof are analytic statements, not consequences of those finite checks.
