# Height--Position--Shape Closure

The homogeneous prediction separates into an intrinsic crossing-centered curve, an empirical or independently constructed absolute height, and a present-position equation. This decomposition produces a complete \(H(N)\) once its premises are frozen, while making clear that the dimensionful constants calibrate the curve rather than determine its dimensionless shape.

## Intrinsic shape at the response cut

Let \(u=N-N_c\), and suppose the reference cut is realized as a spatially flat \(3+1\)-dimensional Einstein--FLRW slice containing noninteracting matter, radiation, and one separately conserved CST-B2 response, with no residual sector. The response law and reference partition give

$$
\Omega_{X,c}=\frac{\mathfrak R_c}{2},
\qquad
\Omega_{\mathrm{non-X},c}=1-\frac{\mathfrak R_c}{2}.
$$

If

$$
\epsilon_c:=\frac{\rho_{r,c}}{\rho_{m,c}+\rho_{r,c}},
$$

then ordinary dilution and the normalized binary response give the **[CONDITIONAL OUTPUT]**

$$
\boxed{
\frac{H^2(u)}{H_c^2}
=\left(1-\frac{\mathfrak R_c}{2}\right)
\left[(1-\epsilon_c)e^{-3u}+\epsilon_c e^{-4u}\right]
+\frac{\mathfrak R_c}{2}\operatorname{sech}^2(\nu u).}
$$

This is normalized automatically at \(u=0\). [[causal-scale-theory/theorems/dimensional-crossing-partition|The dimensional crossing theorem]] owns the factor \(\mathfrak R_c/2\); [[causal-scale-theory/future-asymptotics|the CST-B2 expansion history]] owns the returned background.

For the unit member and dust idealization,

$$
\boxed{
\frac{H^2(u)}{H_c^2}
=\frac12\left(e^{-3u}+\operatorname{sech}^2u\right).}
$$

Its interpretation is precise. The first summand is the ordinary dilution law on a three-dimensional spatial fiber. The second is the balanced-binary BKM response after affine scale--state soldering and the constitutive horizon conversion. Equality of the coefficients is weak integrated matching at the cut. No material dark-energy field is required by this equation, but the physical response-to-stress realization is still an open construction.

## Locating the present slice

Set the present scale coordinate to \(N=0\) and write \(x=N+x_c\), so \(x_c=-N_c>0\) places the response maximum in the past. Define

$$
D:=\Omega_{X0}=1-\Omega_{m0}-\Omega_{r0}.
$$

If the supplied present ratio is

$$
r_0:=\frac{\rho_{X0}}{\rho_{\mathrm{non-X},0}},
$$

then flatness and the declared zero-residual contents imply

$$
D=\frac{r_0}{1+r_0},
\qquad
\Omega_{\mathrm{non-X},0}=\frac1{1+r_0}.
$$

After \(\Omega_{r0}\) is specified, \(\Omega_{m0}=\Omega_{\mathrm{non-X},0}-\Omega_{r0}\). The present-position equation is

$$
\boxed{
\frac{\mathfrak R_c}{2-\mathfrak R_c}
\left(\Omega_{m0}e^{3x_c}+\Omega_{r0}e^{4x_c}\right)
\operatorname{sech}^2(\nu x_c)
=D.}
$$

This is [[causal-scale-theory/theorems/present-flatness-closure|the present-flatness closure]]. It dates the already selected response profile; it does not construct the microscopic event or prove that the reference cut is physical. When several roots exist, the branch index is extra member data. The unit benchmark has one root.

## The full present-centered expansion function

Once \(x_c\) is selected,

$$
\boxed{
\mathcal Z(N):=\frac{H^2(N)}{H_0^2}
=\Omega_{m0}e^{-3N}
+\Omega_{r0}e^{-4N}
+D\frac{\operatorname{sech}^2[\nu(N+x_c)]}
{\operatorname{sech}^2(\nu x_c)}.}
$$

The dimensionless function \(\mathcal Z\) is the complete homogeneous prediction. In the resolution-depth register it is the curve

$$
\boxed{
\Gamma(N):=X_P(N)
=X_{P0}-\frac12\ln\mathcal Z(N).}
$$

Consequently

$$
q(N)=\Gamma'(N)-1
=-1-\frac12\frac{\mathcal Z'(N)}{\mathcal Z(N)},
$$

and proper chronology is

$$
H_0[\tau(N_2)-\tau(N_1)]
=\int_{N_1}^{N_2}\frac{\mathrm dN}{\sqrt{\mathcal Z(N)}}.
$$

Separate conservation also gives

$$
w_X(N)
=-1+\frac{2\nu}{3}\tanh[\nu(N+x_c)]
$$

and the exact member signature

$$
9(1+w_X)^2+6w_X'=4\nu^2.
$$

[[causal-scale-theory/theorems/rigid-sech-response-identities|The rigid-response theorem]] owns these last statements.

## Two legitimate prediction protocols

**Forward calibration.** Supply \(H_0\), or one exactly equivalent horizon scalar, together with the present sector ratio and radiation content. The frozen member predicts \(H(z)\), \(q(z)\), the response crossing, the acceleration interval, \(H_0t_0\), proper age, and the evolution of every horizon-ledger presentation.

**Age calibration.** Supply an independently measured proper age \(t_0\) instead of \(H_0\). The predicted dimensionless age gives

$$
H_0=\frac{H_0t_0}{t_0}.
$$

The same age cannot be counted once as a calibration and again as a successful prediction. A CMB-inferred age obtained under a competing background is a useful comparison, but not a model-independent clock datum.

## The stronger absolute construction

The theory would cease to need a measured height if the wall returned an independently normalized \(\iota_c\). Then

$$
H_c=\frac1{t_P}\sqrt{\frac\pi{\iota_c}},
$$

and independently measured physical matter and radiation densities could determine \(x_c\) through

$$
\rho_{m0}e^{3x_c}+\rho_{r0}e^{4x_c}
=\left(1-\frac{\mathfrak R_c}{2}\right)
\rho_{\mathrm{crit},c}^{(E)}.
$$

The relative curve would then return \(H_0\), rather than being normalized by it. This is the cleanest remaining construction target: an absolute physical crossing capacity and cut realization obtained without \(H_0\), a fitted history, or \(G\)-defined area upstream. The [[wall-construction-interface/elimination-test|elimination test]] and [[causal-scale-theory/no-gos/background-reconstruction-is-not-wall-construction|background-reconstruction no-go]] forbid reversing that arrow.

## Why the unit rate is philosophically apt but not proved

For zero residual, the CST-B2 tail obeys \(\rho_X\sim a^{-2\nu}\). In the response-dominated range, unbounded future conformal reach requires \(\nu\geq1\), while an asymptotically nondecelerating expansion requires \(\nu\leq1\). Requiring both therefore selects

$$
\nu=1,
$$

with asymptotic coasting and a marginally absent event horizon. This suggests a cosmodynamic *open-arena principle*: the late cosmos remains causally unclosed without being forced into permanent deceleration.

The inequalities are theorems of the declared tail; the demand that both be satisfied is a proposed grounding reason, not a theorem of BKM geometry. Its value is empirical sharpness: once adopted before fitting, it fixes the future class and cannot be adjusted to rescue a failed curve.
