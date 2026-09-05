# Local Perron Oscillation and Conditional Coercivity

The finite Wilson vacuum admits local conditional bounds without comparing its density globally to Haar. Its Perron equation controls how much the vacuum changes when one block changes, using only the incident potential and that block's kinetic kernels. The same equation identifies the remaining long-range dependence as a covariance of kinetic scores under the actual Doob transition. This supplies a concrete local estimate and a named correlation problem, not an interacting mass-gap proof.

**Status: [EXACT] on the declared finite compact product carrier with positive smooth kernels; [EXACT COUNTEREXAMPLE] to local conditional control implying a global floor; [OPEN] for a uniform interacting influence bound and its comparison to physical transfer.**

## Local comparison uses the actual Perron equation

Let \(X=\prod_{e\in E}G_e\) have product Haar probability, and let
\[
k(U,Y)=\prod_e k_e(U_e,Y_e)>0,\qquad
T=M_a K M_a,\qquad
a=e^{-V_{\rm sp}/2}>0.
\tag{LP1}
\]
Assume \(T\) is self-adjoint with positive Perron eigenfunction \(\psi\), normalized by \(\int\psi^2=1\), and \(T\psi=\lambda\psi\). The finite Wilson setting supplies such a product kinetic factor and gauge-invariant multiplication potential before restriction to the physical subspace; [[contemporary-puzzles/yang-mills-mass-gap/finite-spacing-transfer-and-bounded-flux-solder|the finite-transfer owner]] fixes its conventions. Write \(\nu=\psi^2\,dU\).

For configurations \(U,V\) agreeing outside a block \(I\),
\[
\frac{\psi(U)}{\psi(V)}
=\frac{a(U)}{a(V)}
\cdot
\frac{\int k(U,Y)a(Y)\psi(Y)\,dY}
{\int k(V,Y)a(Y)\psi(Y)\,dY}
\le\frac{a(U)}{a(V)}
\sup_{Y_I}\frac{k_I(U_I,Y_I)}{k_I(V_I,Y_I)}.
\tag{LP2}
\]
Positivity of the integrand proves the inequality; no density ratio over all configurations is taken.

Define \(\operatorname{osc}_I\) at fixed exterior and then take the supremum over exterior configurations. Let
\[
R_e:=\frac{\sup_{u,y}k_e(u,y)}{\inf_{u,y}k_e(u,y)}.
\]
Taking logarithms in (LP2) gives
\[
\operatorname{osc}_I\log\psi
\le\frac12\operatorname{osc}_I V_{\rm sp}
+\sum_{e\in I}\log R_e.
\]
The actual conditional density \(\nu(dU_I\mid U_{I^c})\), relative to block Haar, therefore has log-oscillation at most
\[
\boxed{D_I:=\operatorname{osc}_I V_{\rm sp}
+2\sum_{e\in I}\log R_e.}
\tag{LP3}
\]
For \(SU(2)\) Wilson factors \(k_e\propto e^{x_e\operatorname{ReTr}(u y^{-1})/2}\), \(R_e=e^{2x_e}\), so
\[
D_I\le\operatorname{osc}_I V_{\rm sp}+4\sum_{e\in I}x_e.
\tag{LP4}
\]
At fixed block and couplings, bounded plaquette incidence makes this independent of total volume. It can still deteriorate when the block grows or \(x_e\to\infty\).

## The conditional Poincare constant is now controlled

Let \(\lambda_{{\rm H},I}>0\) be the Poincare constant of block Haar for the declared product metric. A normalized density with \(\rho_{\max}/\rho_{\min}\le e^{D_I}\) satisfies
\[
\operatorname{Var}_{\rho\,dU_I}(f)
\le\frac{e^{D_I}}{\lambda_{{\rm H},I}}
\int|\nabla_I f|^2\rho\,dU_I.
\tag{LP5}
\]
Proof: minimize over constants in the variance, compare it from above with \(\rho_{\max}\) times Haar variance, apply the Haar inequality, and compare the gradient integral from below with \(\rho_{\min}\). The density comparison costs one oscillation, not its square.

Thus every conditional vacuum fiber has the explicit lower constant
\[
\boxed{\lambda_I^{\rm cond}\ge e^{-D_I}\lambda_{{\rm H},I}.}
\tag{LP6}
\]
This controls a conditional sampler or weighted gradient form on that fiber. It does not identify that form with the finite-spacing transfer logarithm.

## The missing mixed response is an actual transition covariance

Assume the factors and potential are \(C^2\); strict positivity and compactness allow differentiation under the integral. Put
\[
F(U):=\int k(U,Y)a(Y)\psi(Y)\,dY,\qquad
\eta_U(dY):=\frac{k(U,Y)a(Y)\psi(Y)}{F(U)}\,dY.
\tag{LP7}
\]
The Perron equation \(\lambda\psi(U)=a(U)F(U)\) shows that \(\eta_U\) is exactly the [[contemporary-puzzles/yang-mills-mass-gap/finite-spacing-transfer-and-bounded-flux-solder#The exact one-step form|physical one-step Doob kernel]] \(P_T(U,dY)\), not a newly selected state.

For a coordinate block \(I\), define the kinetic score covector
\[
s_I(U,Y):=d_I\log k_I(U_I,Y_I).
\]
Then
\[
d_I\log\psi=d_I\log a+\mathbb E_{\eta_U}s_I,\qquad
d_I\log\eta_U=s_I-\mathbb E_{\eta_U}s_I.
\tag{LP8}
\]
For disjoint blocks \(I,J\), the product connection and product kernel give
\[
\boxed{
\nabla_Jd_I\log\psi
=\nabla_Jd_I\log a
+\operatorname{Cov}_{\eta_U}(s_I,s_J).}
\tag{LP9}
\]
The covariance is a bilinear form on the two block tangent spaces. It is the cross block of the Fisher metric of the actual transition family \(U\mapsto\eta_U\). On diagonal blocks there is an additional \(\mathbb E_{\eta_U}\nabla_I d_I\log k_I\); (LP9) must not be applied there unchanged.

Let \(\mathcal V_\nu=-2\log\psi\). For individual factors \(i\ne j\),
\[
M_{ij}:=\sup_U\|\nabla_jd_i\mathcal V_\nu\|
\le
\sup_U\|\nabla_jd_iV_{\rm sp}\|
+2\sup_U\|\operatorname{Cov}_{\eta_U}(s_i,s_j)\|.
\tag{LP10}
\]
Locality of the multiplication potential removes its distant mixed blocks. It does not remove the transition covariance. This is where a genuinely whole-law estimate is still needed.

The relation to conditional influence is explicit. For an exterior-independent test \(f(U_i)\), differentiating the normalized conditional law \(\pi_i\) gives
\[
d_j\mathbb E_{\pi_i}f
=-\operatorname{Cov}_{\pi_i}(f,d_j\mathcal V_\nu).
\]
Applying (LP5) to both covariance factors yields, for \(1\)-Lipschitz \(f\),
\[
\|d_j\mathbb E_{\pi_i}f\|
\le\frac{M_{ij}}{\lambda_i^{\rm cond}}.
\tag{LP11}
\]
Integrating along a factor geodesic gives a Wasserstein sensitivity coefficient. Its type is propagation of a conditional readout under a change of exterior data, not mass or clock energy. The existing [[contemporary-puzzles/yang-mills-mass-gap/gauge-descent-flux-fisher-coercivity|raw-link Dobrushin assembly]] states one applicable global functional-inequality criterion. Its influence radius and conditional constants still need control along the regulator trajectory; a finite-spacing transfer-gap claim additionally needs the bounded same-carrier physical comparison.

All these estimates are on the raw product carrier. Gauge-invariant restriction is safe after the estimate is proved, because it only removes test functions. Gauge fixing before taking conditional derivatives changes the carrier and measure and requires a new calculation. The score blocks are equivariant cotangent tensors, not separately gauge-invariant scalar observables.

## Uniform local fibers do not imply a uniform whole-law floor

An exact finite-spin calibration shows why the additional influence estimate cannot be omitted. For odd \(N=2k+1\), take
\[
\nu_N(x)=\frac12\prod_{i=1}^N\frac{1+m x_i}{2}
+\frac12\prod_{i=1}^N\frac{1-m x_i}{2},
\qquad x_i\in\{-1,1\},\quad0<m<1.
\tag{LP12}
\]
Every one-spin conditional probability lies between \((1-m)/2\) and \((1+m)/2\), uniformly in \(N\). Nevertheless \(f(x)=\operatorname{sign}(\sum_i x_i)\) has mean zero and variance one, while
\[
\begin{aligned}
\sum_i\mathbb E_{\nu_N}\operatorname{Var}(f\mid x_{-i})
&=N\binom{2k}{k}\left(\frac{1-m^2}{4}\right)^k\\
&\le N(1-m^2)^k\longrightarrow0.
\end{aligned}
\tag{LP13}
\]
Only an exact tie among the other spins allows the conditional value of \(f\) to change. On that tie the two mixture components have equal posterior weight, giving conditional variance one. This proves (LP13).

Thus uniformly regular conditional fibers can coexist with an arbitrarily slow collective distinction. The example calibrates the logic of a sampler estimate; it is not a counterexample to the Wilson theory. [[bridge-data-augmentation-solder/predictive-sufficient-interfaces|Complete predictive interfaces]] and [[two-slice-innovation-geometry/inq|two-slice innovation geometry]] keep this collective obstruction visible.

[[boundary-action-fixed-points-and-physical-linearization|Finite-history boundary actions]] now make the local estimates uniform in preparation depth before the Perron limit. [[strong-coupling-gap-and-continuum-crossover/wilson-slab-conditional-fisher-certificate|The actual Wilson slab certificate]] additionally controls the covariance in (LP9), its spatial row sum and the complete midpoint response in an explicit small-parameter regime. The remaining question is whether this joint control survives fixed-physical-depth interacting blocking and the continuum trajectory. [[bridge-score-fusion-geometry/wilson-bridge-envelopes-under-temporal-blocking|The pure Wilson fusion bound]] does not answer that question by itself.

[[receipts/local_perron_response_receipt.py|The finite receipt]] checks local Perron ratios, conditional comparison, normalized scores, mixed covariance and the exact slow-mixture calibration.

For the separate gradient-form target, [[temporal-column-response/inq|whole temporal columns]] avoid the large one-link temporal influence. [[strong-coupling-gap-and-continuum-crossover/wilson-temporal-column-coercivity|The resulting Wilson theorem]] controls the actual vacuum through time refinement at small magnetic/electric ratio. Its midpoint density comparison is local after conditioning on the other complete columns, not a global Haar comparison or a bound on the full predictive bridge.
