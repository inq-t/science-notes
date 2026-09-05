# Linear-Tilted Sphere Coercivity

A linear external field does not destroy every uniform gradient bound on a sphere. On the unit \(S^{n-1}\), \(n\ge4\), the latitude measure supplies enough convexity to give a Poincare lower bound \(n-3\), independent of the field's magnitude or direction. For \(SU(2)\cong S^3\), this yields a coupling-independent single-link conditional bound even where a direct Bakry--Emery curvature test becomes negative.

**Status: [EXACT THEOREM] for every finite linear tilt and the unit round metric; [NOT AN OPTIMAL-CONSTANT CLAIM]; [NOT A MANY-BODY OR PHYSICAL MASS GAP].**

## The measure and the bound

Let \(\sigma\) be normalized round measure on \(S^{n-1}\subset\mathbb R^n\), with \(n\ge4\). For any \(a\in\mathbb R^n\), define
\[
dq_a(u)=Z(a)^{-1}e^{a\cdot u}\,d\sigma(u).
\tag{LT1}
\]
Then every function in the closed gradient-form domain satisfies
\[
\boxed{
(n-3)\operatorname{Var}_{q_a}F
\le\int|\nabla_{S^{n-1}}F|^2\,dq_a.}
\tag{LT2}
\]
For each finite \(a\), the density is smooth and strictly positive. Uniformity in \(a\) means the same constant works for every member; it does not identify the singular limit \(|a|=\infty\) with a smooth weighted sphere.

## A one-dimensional inequality with its boundary argument

For a strictly convex smooth potential \(V\) on a compact interval, let \(\nu\propto e^{-V}dx\). The one-dimensional variance inequality is
\[
\operatorname{Var}_\nu g\le\int\frac{|g'|^2}{V''}\,d\nu.
\tag{LT3}
\]
Here is a proof including the endpoint convention. Center \(g\) and solve
\(-\mathcal Gh=g\), where \(\mathcal Gh=h''-V'h'\), with reflecting conditions \(h'=0\) at both ends. Weighted integration by parts gives
\[
\int g^2\,d\nu=\int g'h'\,d\nu,\qquad
\int g^2\,d\nu=\int\big[(h'')^2+V''(h')^2\big]\,d\nu.
\]
The endpoint terms vanish. Cauchy--Schwarz with weights \(V''\), followed by the second identity, proves (LT3). This is the one-dimensional variance Brascamp--Lieb argument; the proof here does not rely on a log-convexity assertion for the spherical potential itself.

## The field disappears from the latitude curvature

Rotate \(a=\kappa e_0\), \(\kappa\ge0\), and write
\[
u=(x,\sqrt{1-x^2}\,\omega),\qquad
\omega\in S^{n-2}.
\]
The latitude \(x\) and angular direction \(\omega\) are independent under (LT1), with
\[
d\nu_\kappa(x)\propto
e^{\kappa x}(1-x^2)^{(n-3)/2}\,dx,\qquad -1<x<1.
\tag{LT4}
\]
Thus
\[
V_\kappa=-\kappa x-\frac{n-3}{2}\log(1-x^2),\qquad
V_\kappa''=(n-3)\frac{1+x^2}{(1-x^2)^2}
\ge\frac{n-3}{1-x^2}.
\tag{LT5}
\]
Apply (LT3) first on \([-1+\epsilon,1-\epsilon]\) with the normalized restricted measure, then let \(\epsilon\downarrow0\). For smooth spherical tests the resulting integrals converge, giving
\[
\operatorname{Var}_{\nu_\kappa}g
\le\frac1{n-3}\int(1-x^2)|g'|^2\,d\nu_\kappa.
\tag{LT6}
\]
The linear tilt has no second derivative in this coordinate. The required curvature comes from the sphere's induced latitude measure, which must not be omitted.

For a smooth sphere function \(F(x,\omega)\), total variance, Jensen and the round \(S^{n-2}\) gap \(n-2\) give
\[
\begin{aligned}
\operatorname{Var}_{q_a}F
&\le\frac1{n-3}\int(1-x^2)|\partial_xF|^2\,dq_a\\
&\quad+\frac1{n-2}\int|\nabla_\omega F|^2\,dq_a\\
&\le\frac1{n-3}\int\left[
(1-x^2)|\partial_xF|^2+
\frac{|\nabla_\omega F|^2}{1-x^2}\right]dq_a.
\end{aligned}
\tag{LT7}
\]
The last bracket is exactly the round spherical gradient norm. This proves (LT2) on smooth functions; density in the weighted \(H^1\) form domain proves the stated extension.

The proof does not apply as written to \(S^2\), where the latitude exponent vanishes, or to an arbitrary nonlinear potential. Its failure there is not a counterexample to any sharper theorem.

## The exact conditional scope

For \(SU(2)\) with metric \(g(X,Y)=-\operatorname{ReTr}(XY)/2\), a Wilson link appearing once in each incident plaquette has precisely the form (LT1). Therefore its conditional gradient gap is at least one, uniformly over all finite couplings and exterior configurations. At zero field the true Haar gap is three, so the estimate is conservative.

If a selected set of links shares no plaquette, their conditional law is a product of these tilted spheres. Tensorization gives
\[
\operatorname{Var}(F\mid R)
\le\mathbb E\!\left[\sum_{e\in H}|\nabla_eF|^2\,\middle|\,R\right]
\tag{LT8}
\]
without a factor proportional to the number of hidden links. [[rg-covariance-residue/su2-staple-elimination-and-response|Exact staple elimination]] specifies that law and its retained response.

This controls variations of hidden links with the exterior frozen. It does not control differentiation of the conditional law as the exterior changes, variance of the actual retained marginal, a whole temporal column, or physical transfer. In particular, [[rg-covariance-residue/frustrated-su3-conditional-wells|the \(SU(3)\) two-well conditional]] disproves the analogous all-coupling, all-boundary assertion for a different group.

[[rg-covariance-residue/receipts/staple_elimination_receipt.py|The finite receipt]] checks the spherical inequality on polynomial/angular test spaces, including strong tilts. The full-domain theorem is the proof above, not a numerical extrapolation of those tests.
