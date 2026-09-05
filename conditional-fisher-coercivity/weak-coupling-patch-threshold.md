# Weak-Coupling Geometry Obstructs the Fixed Patch Threshold

Interior gauge reduction does not make every Wilson patch fluctuation fast. A weighted bundle of boundary-to-boundary paths survives that reduction and has a Gaussian refresh rate below the \(1/n\) projection threshold. Smooth compact-group observables carry this obstruction into the actual weak-coupling Wilson law: an interior-invariant path test rules out the sufficient certificate for fixed \(n\ge3\), and a globally invariant loop test rules out the same patch threshold on the global invariant carrier for fixed \(n\ge8\). These are failures of a particular certificate, not proofs of physical gaplessness.

**Status: exact Gaussian geometry and fixed-patch nonlinear Rayleigh-limit theorem.** The limit holds at fixed lattice geometry. It is not a continuum limit, a lower spectral estimate, or convergence of complete spectra.

## The actual boundary quadratic form

Take the vertex cube \(\{0,\ldots,n-1\}^d\), \(d\ge2\), \(n\ge2\), with all links whose endpoints are inside it. Freeze all exterior links to identity in a larger torus with side lengths exceeding \(2n\). Use every Wilson plaquette touching the patch. With Lie algebra metric
\[
\langle X,Y\rangle=-q^{-1}\operatorname{ReTr}(XY)
\]
for \(SU(q)\), \(q\ge2\), expansion at identity gives
\[
V_B(e^X;\mathbf1)=\tfrac12\|C_BX\|^2+O(\|X\|^3),\qquad
K=C_B^*C_B.
\tag{WP1}
\]
The same real link matrix \(K\) acts in each orthonormal color direction. No factor of the bare coupling is included in \(V_B\); the density is \(e^{-\beta V_B}\).

Every exterior plaquette touching the cube contains exactly one patch edge. Consequently
\[
K=C_{\rm in}^*C_{\rm in}+W,\qquad
W_{(x,\mu)}=\#\{\nu\ne\mu:x_\nu\in\{0,n-1\}\},
\qquad K_{ee}=d_0:=2(d-1).
\tag{WP2}
\]
This boundary term must not be replaced by free-boundary curl.

Internal curl-free fields are gradients of vertex potentials, by path independence on the cubical two-skeleton. The condition \(W^{1/2}X=0\) makes the potential constant along the connected boundary graph. Subtracting that constant proves
\[
\ker K=\operatorname{Ran}d_{\rm int},\qquad
\mathcal V=(\ker K)^\perp,
\tag{WP3}
\]
where \(d_{\rm int}\) differentiates potentials vanishing at boundary vertices. Thus \(K\) is positive on the interior-gauge quotient, but its lower edge still depends on patch geometry.

## A surviving path variation

Fix a direction \(\mu\), and assign
\[
v_\mu(x)=w(x_\perp):=
\prod_{\nu\ne\mu}\sin\frac{\pi(x_\nu+1)}{n+1},
\qquad v_\nu=0\quad(\nu\ne\mu).
\tag{WP4}
\]
The field is constant along each straight longitudinal path. Its divergence vanishes at every strictly interior vertex, so \(v\in\mathcal V\). Direct summation gives
\[
\|v\|^2=(n-1)\left(\frac{n+1}{2}\right)^{d-1},
\qquad
\frac{v^*Kv}{\|v\|^2}
=4(d-1)\sin^2\frac{\pi}{2(n+1)}.
\tag{WP5}
\]
The transverse sine is extended by zero beyond each face. Its endpoint differences account for precisely the exterior plaquettes in (WP2).

[[gaussian-refresh-projection-spectrum|The Gaussian refresh theorem]] gives the exact full Gaussian quotient gap \(\lambda_{\min}^+(K)/d_0\). More importantly for a nonlinear test, the fixed linear observable \(v^*X\) has Rayleigh quotient
\[
r(v):=\frac{\|v\|^2}{d_0\,v^*K^+v}
\le\frac{v^*Kv}{d_0\|v\|^2}
=1-\cos\frac{\pi}{n+1}=:b_n.
\tag{WP6}
\]
The inequality is Cauchy--Schwarz, not an assertion that the path field is an eigenvector.

For every \(n\ge3\),
\[
b_n<\frac{\pi^2}{2(n+1)^2}<\frac1n.
\tag{WP7}
\]
At \(n=2\), \(W=(d-1)I\), and internal-cube gradients attain \(K=d-1\). The Gaussian gap is exactly \(1/2\), equal to the threshold, not below it.

## A compact-group observable with that derivative

Let \(U_{\gamma_{x_\perp}}\) be the ordered product along the straight path from one \(\mu\)-face to the opposite face. For a fixed unit anti-Hermitian traceless \(T\), define the real smooth function
\[
f_T(U)=
-q^{-1}\operatorname{ReTr}
\left[T\sum_{x_\perp}w(x_\perp)U_{\gamma_{x_\perp}}\right].
\tag{WP8}
\]
It is invariant under all interior gauge transformations, vanishes on every zero-action configuration, and has derivative \(v\) in color direction \(T\). It is not invariant under arbitrary independent boundary transformations or under simultaneous conjugation with \(T\) held fixed. This is exactly the sufficient interior-invariant carrier of [[gauge-reduced-patch-coercivity|the reduced patch criterion]], not yet a globally neutral probe.

### The flat minimum is one smooth gauge orbit

At zero action, outward plaquettes force all boundary-tangential links to identity. Internal plaquette flatness gives \(U_{xy}=g_xg_y^{-1}\); connectedness of the boundary makes \(g\) constant there, and that constant can be set to identity. The entire minimum set is therefore one interior-gauge orbit.

Choose a forest connecting every interior vertex to a boundary root, with one boundary root per component. Fix its \(|V_{\rm int}|\) links to identity. The interior gauge action is free, this gives a global smooth quotient with the remaining compact-group coordinates, and product Haar disintegrates by successive left/right translations. The zero-action quotient point is unique. Equation (WP3) makes its Hessian nondegenerate.

Consequently, ordinary finite-dimensional Laplace scaling on this quotient applies. A nonorthogonal forest slice does not change the dual covariance of an interior-gauge-invariant derivative: it is \(v^*K^+v\). Taylor expansion, the substitution \(X=\beta^{-1/2}Z\), a positive quadratic bound near the minimum and a positive action separation outside that neighborhood give
\[
\beta\operatorname{Var}_{\beta,\mathbf1}(f_T)
\longrightarrow s:=v^*K^+v>0.
\tag{WP9}
\]
The estimates control polynomial moments, not just weak convergence.

### The conditional numerator needs its own argument

Near the projected flat orbit, an active-link conditional is, after an endpoint gauge rotation, a compact \(SU(q)\) linear tilt close to source \(d_0 I\). At that source its minimum is uniquely identity and its Hessian is \(d_0 I\). The implicit-function theorem and compactness give, uniformly on a fixed sufficiently small retained-context neighborhood, a unique nearby minimum, a positive conditional Hessian and a positive potential separation outside a fixed coordinate ball.

For each such retained context \(R\), one-link Laplace expansion gives
\[
\beta\operatorname{Var}_{e,\beta,R}(f_T)
=a_e(R)+o(1),
\]
uniformly there. The coefficient is the conditional derivative contracted with the inverse conditional Hessian at its minimum. Whole-law concentration sends this coefficient to
\(\|\partial_e f_T|_{\rm flat}\|^2/d_0\). Interior gauge invariance and the bi-invariant link metric make this value constant along the flat orbit.

The complementary retained-context set has exponentially small marginal probability: its inverse image stays away from the compact whole minimum orbit. Since conditional variance is bounded by a constant depending only on the fixed smooth \(f_T\), its contribution remains negligible after multiplication by \(\beta\). Thus
\[
\beta\sum_e
\mathbb E_{\beta,\mathbf1}\operatorname{Var}_{e,\beta,R}(f_T)
\longrightarrow\frac{\|v\|^2}{d_0}.
\tag{WP10}
\]
Global concentration alone would not imply (WP10); the uniform conditional minimum and moment argument are essential.

Combining (WP9)--(WP10) proves convergence of this one Rayleigh quotient to \(r(v)\). For each finite \(\beta\), its numerator and positive denominator are continuous in the exterior. The exterior marginal has full support. The same neighborhood argument as for the previous gauge-dependent witness therefore gives
\[
\boxed{
\limsup_{\beta\to\infty}\Gamma_n^{\rm int}(\beta)
\le r(v)\le b_n<1/n\qquad(n\ge3).}
\tag{WP11}
\]
This proves that the fixed-\(n\ge3\) sufficient interior-invariant patch condition eventually fails in the actual Wilson law. It does not merely suggest failure from its Hessian. For \(n=2\), the limiting upper bound equals \(1/2\); the sign of a finite-\(\beta\) correction is not determined here.

## The obstruction survives global gauge invariance

Complete each path in (WP8) through exterior links into a loop based at one common root. This can be done explicitly on the torus: continue in the positive \(\mu\) direction around the remaining periodic circle, and connect its starting vertex to the root through the exterior hyperplane \(x_\mu=L_\mu-1\). All added links lie outside \(B\). At identity exterior every added transport is identity, so the interior linear jets are unchanged.

Let \(W_p\) denote the resulting root-based holonomies, and use the real orthogonal projection
\[
\Pi_{\mathfrak{su}(q)}M
=\frac{M-M^*}{2}
-\frac{\operatorname{Tr}(M-M^*)}{2q}I.
\]
Define
\[
\Phi=\Pi_{\mathfrak{su}(q)}\sum_p w_pW_p,\qquad
F=\|\Phi\|^2.
\tag{WP12}
\]
All loop matrices transform by one root conjugation. Thus \(F\) is a smooth globally gauge-invariant function, without a fixed color vector or a boundary Gauss projection. At the flat orbit its first nonzero jet is
\[
P(X)=\sum_{A=1}^{m}\ell_A(X)^2,\qquad
\ell_A=v^*X^A,\qquad m=q^2-1.
\tag{WP13}
\]
The Gaussian colors are independent, each with variance \(s=v^*K^+v\).

### Quadratic jets require a conditional replica pair

For each refreshed edge \(e\), choose the boundary-rooted gauge forest to avoid \(e\). Such a forest exists: every cube edge lies on an internal plaquette, so deleting it leaves the graph connected; starting with all boundary vertices as roots gives the required forest. The gauge coordinates then depend only on the retained links. In this slice the actual \(e\)-refresh is an ordinary coordinate conditional refresh, and the positive quotient Hessian has active block \(d_0I\).

Draw \(U\) from the quotient law and \(U'\) by one stationary \(e\)-refresh. Write slice coordinates as \((x_e,y)\), with quotient Hessian blocks \(A_{ee}=d_0I,A_{ey},A_{yy}\). Conditional on \(\sqrt\beta\,y=z\), the scaled refreshed coordinate converges, uniformly on compact \(z\)-sets, to
\[
\sqrt\beta\,x'_e\ \Longrightarrow\
N(-d_0^{-1}A_{ey}z,\ d_0^{-1}I).
\]
The retained fluctuations must therefore be kept in the conditional mean. Together with the quotient Laplace limit this gives convergence of the scaled stationary pair to its Gaussian conditional replica pair. Both marginal laws equal the original quotient law. Their bounded scaled moments of every fixed order therefore give uniform integrability for the joint fourth-order expressions. This proves the variance limits below; convergence in distribution alone would not suffice.

Put \(a_e=v_e^2/d_0\). In each Gaussian color,
\[
\operatorname{Var}(\ell_A)=s,\qquad
\operatorname{Cov}(\ell_A,\ell'_A)=s-a_e.
\]
Using
\(\mathbb E\operatorname{Var}_eF=\tfrac12\mathbb E(F(U)-F(U'))^2\)
and the Gaussian fourth-moment identity yields
\[
\beta^2\operatorname{Var}_{\beta,\mathbf1}F\longrightarrow2ms^2,
\qquad
\beta^2\sum_e\mathbb E_{\beta,\mathbf1}\operatorname{Var}_eF
\longrightarrow\sum_e(4msa_e-2ma_e^2).
\tag{WP14}
\]
The derivative of \(F\) vanishes at the flat point, so a first-derivative-only conditional estimate would miss this leading term.

The exact limiting quotient is consequently
\[
\boxed{
R_{\rm neutral}
=2r(v)-\frac{\sum_e v_e^4}{d_0^2s^2}
\le2b_n<\frac1n\qquad(n\ge8).}
\tag{WP15}
\]
The color multiplicity cancels. The last strict inequality follows from
\(2b_n<\pi^2/(n+1)^2<1/n\) for \(n\ge8\).

### A genuine global-invariant patch countertest

For finite \(\beta\), let
\[
D(\eta)=\operatorname{Var}_{\beta,\eta}F,\qquad
N(\eta)=\sum_{e\in B}\mathbb E_{\beta,\eta}\operatorname{Var}_eF.
\]
These are continuous gauge-invariant exterior functions. For each fixed \(n\ge8\) and sufficiently large \(\beta\), (WP15) permits
\(N(\mathbf1)/D(\mathbf1)<c_*<1/n\). Set
\[
\chi(\eta)=(c_*D(\eta)-N(\eta))_+,\qquad
G(U,\eta)=\chi(\eta)(F-P_BF).
\tag{WP16}
\]
This bounded function is globally invariant, satisfies \(P_BG=0\), and is nonzero by full support and continuity. Since \(Q_eG=\chi Q_eF\),
\[
\langle G,h_BG\rangle
=\int\chi^2N
<c_*\int\chi^2D
=c_*\|G\|^2.
\tag{WP17}
\]
Thus \(h_B\ge(1/n)(I-P_B)\) fails even on the global invariant carrier. The cutoff need not be differentiable: the criterion uses bounded conditional projections, not a gradient form. Nothing here makes the full-lattice heat-bath energy small, since updates outside \(B\) also act on this test.

## Keep the slow information as retained data

The function (WP8) already factors through the tuple of boundary-to-boundary path products. Its response is therefore retained information for that readout, not a fluctuation inside a fiber conditioned on that readout. It may be moved to a coarse level, but must not be erased by calling it gauge redundancy.

[[rg-covariance-residue/endpoint-averages-and-quadratic-ultraviolet-control|The endpoint-average estimate]] supplies the existing linear model of this distinction: a hard zero-readout fiber can be coercive while its retained Maxwell field remains soft. [[rg-covariance-residue/soft-gaussian-gauge-blocking|Soft Gaussian blocking]] keeps both parts in an exact joint law. Neither conditional ultraviolet control nor a gauge choice proves a gap for the retained infrared response.

The next construction must therefore change something substantive: use a sharper finite-size comparison, a genuinely multiscale conditional geometry, or localization that pays for unfavorable boundary contexts. Simply repeating the fixed \(1/n\) all-context test on larger fixed cubes cannot overcome (WP11), and projecting further to global invariance does not overcome (WP17) for fixed \(n\ge8\). The nonlinear constants above are not uniform as \(n\) grows, so no growing-patch or continuum impossibility theorem has been proved.

[[tensor-local-refresh-and-inverse-square-patches|The inverse-square replacement]] implements the sharper-comparison branch on assigned plaquette-star patches. [[rg-covariance-residue/gaussian-harmonic-refresh-lifting|The harmonic-lift theorem]] implements the retained-data branch for the Gaussian law, with exact composition and a single comparison across a composite blocking scale. Neither proves the missing interacting retained response.

The [[receipts/weak_coupling_patch_receipt.py|finite receipt]] checks incidence, gauge kernels, path trials, Gaussian response and compact-group jets. The nonlinear asymptotic theorem rests on the stated finite-dimensional arguments, not on a numerical simulation or a complete spectral limit.
