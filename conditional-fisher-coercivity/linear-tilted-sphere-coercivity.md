# Linear-Tilted Sphere Coercivity

A linear external field does not destroy every uniform gradient bound on a sphere. On the unit \(S^{n-1}\), \(n\ge4\), the latitude measure supplies enough convexity to give a Poincare lower bound \(n-3\), independent of the field's magnitude or direction. The same bound holds for every smooth positive amplitude whose logarithm is concave in latitude. For \(SU(2)\cong S^3\), this gives coercivity even where an angular curvature test becomes negative.

**Status: [EXACT THEOREM] for finite linear tilts and the stated log-concave radial amplitudes, with the unit round metric; [NOT AN OPTIMAL-CONSTANT CLAIM]; [NOT A MANY-BODY OR PHYSICAL MASS GAP].**

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

## Concave radial amplitudes retain the same bound

The linear tilt is not essential to the estimate. Let
\(f\in C^\infty([-1,1])\) be strictly positive, with
\((\log f)''\le0\), and replace (LT1) by
\(dq\propto f(x)^2d\sigma\). Its latitude potential satisfies
\[
V_f''=-2(\log f)''+(n-3)\frac{1+x^2}{(1-x^2)^2}
\ge\frac{n-3}{1-x^2}.
\tag{LT9}
\]
The interval argument (LT3)--(LT6), followed by the same
independent angular decomposition, proves (LT2) with the
unchanged constant \(n-3\). In particular, on the radial
\(S^3\) carrier with electric coefficient \(\kappa\),
\[
\boxed{
\operatorname{Var}_{\nu_f}F
\le\int_{-1}^1(1-x^2)|F'(x)|^2d\nu_f,
\qquad d\nu_f\propto f(x)^2\sqrt{1-x^2}\,dx.
}
\tag{LT10}
\]
Thus the inherited form \(\kappa\int(1-x^2)|F'|^2d\nu_f\)
has gap at least \(\kappa\). The concavity condition is on
the logarithm of the amplitude in the latitude coordinate,
not on the density in angular distance. These are different
tests. [[algebra/partial-bochner-and-ground-state-score#A latitude estimate is uniform in magnetic coupling|The single-plaquette heat construction]]
proves this condition for its actual reference vacuum at
every finite magnetic coupling. A many-plaquette marginal
must satisfy it by a separate argument.

## Averaging a fixed transverse tilt preserves latitude concavity

On \(S^3\), split a fixed field into an axial component
\(\eta\in\mathbb R\) and transverse magnitude \(b\ge0\).
Average the transverse direction over \(S^2\), keeping
the latitude \(a\) fixed. With \(h=1-a^2\), the resulting
unnormalized density relative to round measure is
\[
k_{\eta,b}(a)=e^{\eta a}
\frac{\sinh(b\sqrt h)}{b\sqrt h}.
\tag{LT11}
\]
The ratio is one at zero. This is a rotation average of
one fixed linear tilt, not an arbitrary mixture of fields.
The same \(S^2\) integration appears in
[[gauge-path-fisher-response/path-shift-fisher-geometry-before-gauge-projection#The first retained change is explicitly quadratic|the path-source orbit average]].

The classical [hyperbolic-sine product](https://dlmf.nist.gov/4.36.E1)
gives
\[
\log\frac{\sinh(b\sqrt h)}{b\sqrt h}
=\sum_{n\ge1}\log\left(1+\frac{b^2h}{\pi^2n^2}\right).
\]
Define
\[
A_b(h)=\sum_{n\ge1}\frac{b^2}{\pi^2n^2+b^2h},
\qquad
B_b(h)=\sum_{n\ge1}\frac{b^4}{(\pi^2n^2+b^2h)^2}.
\tag{LT12}
\]
The series and the required derivatives converge uniformly
for bounded \(b\), \(0\le h\le1\). Differentiation proves
\[
\boxed{
(\log k_{\eta,b})'=\eta-2aA_b(h),\qquad
(\log k_{\eta,b})''=-2A_b(h)-4a^2B_b(h)\le0.
}
\tag{LT13}
\]
The second inequality is strict for \(b>0\), including
both endpoints. In particular,
\[
A_b(0)=b^2/6,\qquad B_b(0)=b^4/90.
\tag{LT14}
\]
There is no pole singularity in these expressions.
The amplitude \(\sqrt{k_{\eta,b}}\) therefore satisfies
(LT9), giving the same lower bound for each normalized
rotation-averaged component.

Arbitrary positive mixing does not preserve this conclusion.
Mix \((\eta,b)=(1,1),(-1,1)\) with equal weights. Both
components are strictly log-concave, but their sum is
proportional to
\[
K(a)=\cosh(a)\frac{\sinh\sqrt{1-a^2}}{\sqrt{1-a^2}},
\qquad
(\log K)''(0)=1-2A_1(1)\ge2/3>0,
\tag{LT15}
\]
since \(A_1(1)\le\sum_{n\ge1}(\pi^2n^2)^{-1}=1/6\).
The two component normalizers agree by \(a\mapsto-a\),
so this also describes their equally weighted normalized
mixture. This disproves mixture preservation of the
sufficient concavity condition, not the existence of a
Poincare bound for that particular smooth mixture.

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
