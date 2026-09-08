# Response Factorization and the Vacuum

An independently constructed exact response can determine a positive quantum Hamiltonian and its vacuum together, once a configuration metric, reference measure and factorization rule are specified. The resulting potential contains a divergence correction absent from the classical squared response. A nonlinear one-coordinate example proves that a vanishing response derivative at the classical minimum need not mean a vanishing quantum gap. This is a finite-dimensional realization theorem, not a derivation of a physical quantization unit or a continuum gauge theory.

## Specify the response before the state

Let \(Q\) be connected, with a positive Riemannian metric \(g\) and a smooth positive reference measure \(dm=\rho\,d\mathrm{vol}_g\). A sufficient scope for the construction below is Euclidean \(\mathbb R^d\), or a compact manifold without boundary. Let \(W\) be a smooth real function and suppose the independently specified response is the globally exact one-form

\[
N=dW.
\tag{RV1}
\]

Its metric dual is the vector field \(N^\sharp=\nabla W\). This distinction fixes where the metric enters: a covector becomes a gradient vector only after \(g\) is given. Global exactness also matters. A merely locally exact response with nonzero periods need not admit a single-valued scalar vacuum of the form below.

Choose \(\epsilon>0\), an abstract quantization parameter, and assume

\[
0<Z_\epsilon:=\int_Q e^{-2W/\epsilon}\,dm<\infty.
\tag{RV2}
\]

No identification \(\epsilon=\hbar\) is made. The coefficient \(1/2\) used below fixes a kinetic normalization relative to the declared metric. Physical energy, clock and action units would require a further calibration.

On complex scalar functions, define

\[
\mathcal D_\epsilon u=\epsilon\,du+uN,
\qquad
\mathcal D_\epsilon:L^2(Q,m)\longrightarrow L^2(T^*Q,m).
\tag{RV3}
\]

Start on \(C_c^\infty\), or \(C^\infty\) on compact \(Q\), and take the closure. The smooth coefficients make this operator closable. Define the realization by its closed nonnegative form,

\[
\mathfrak h_\epsilon[u]
=\frac12\|\mathcal D_\epsilon u\|^2,
\qquad
H_\epsilon=\frac12\mathcal D_\epsilon^*\mathcal D_\epsilon.
\tag{RV4}
\]

The adjoint uses the same metric and reference measure. On a domain with boundary, one must choose a compatible closed-form boundary condition; ordinary Dirichlet conditions generally exclude the proposed positive vacuum. Such domains are not implicit in (RV4).

## The correction and vacuum are forced by this realization

Write \(\Delta_m=\operatorname{div}_m\nabla\), so that \(-\Delta_m\) is nonnegative. Expansion on the smooth core gives

\[
\boxed{
H_\epsilon
=-\frac{\epsilon^2}{2}\Delta_m
+\frac12|N|_g^2
-\frac\epsilon2\operatorname{div}_mN^\sharp.}
\tag{RV5}
\]

The first-derivative cross terms cancel. The remaining divergence depends on the reference measure as well as the metric; dropping a density or orbit-volume factor changes the operator.

The normalized vector

\[
\boxed{\psi_\epsilon=Z_\epsilon^{-1/2}e^{-W/\epsilon}}
\tag{RV6}
\]

satisfies \(\mathcal D_\epsilon\psi_\epsilon=0\). On Euclidean space it belongs to the closed domain: multiply it by smooth cutoffs \(\chi_R\to1\) with \(\|d\chi_R\|_\infty\to0\), and use
\(\mathcal D_\epsilon(\chi_R\psi_\epsilon)=\epsilon\psi_\epsilon d\chi_R\).
On compact \(Q\), it is already smooth. Conversely, every weak zero mode has \(d(e^{W/\epsilon}u)=0\), hence is proportional to \(\psi_\epsilon\) by connectedness. Therefore

\[
\ker H_\epsilon=\mathbb C\psi_\epsilon.
\tag{RV7}
\]

A unique normalizable zero mode does not alone establish a positive gap above it.

This is the constructive direction of the [[strong-coupling-gap-and-continuum-crossover/gauge-descent-flux-fisher-coercivity#Exact ground-state-transform theorem|ground-state transform]]. With \(d\mu_\epsilon=\psi_\epsilon^2dm\), multiplication \(U_\epsilon f=\psi_\epsilon f\) is unitary and

\[
\mathfrak h_\epsilon[U_\epsilon f]
=\frac{\epsilon^2}{2}\int_Q|df|_g^2\,d\mu_\epsilon.
\tag{RV8}
\]

The corresponding spectral gap is \(\epsilon^2/2\) times the complete weighted Poincare constant, not a Hessian evaluated at one configuration. The [[binary-information-geometry/witten-darboux|binary Witten–Darboux pair]] owns a different exact response with an explicitly solvable partner and weighted gap.

## Classical squared response is a different potential

The classical prescription

\[
V_{\mathrm{cl}}=\frac12|dW|_g^2
\]

does not contain the final term of (RV5). The selected factored quantum realization instead satisfies the real quantum Hamilton–Jacobi identity

\[
V_\epsilon
=\frac12|dW|_g^2-\frac\epsilon2\Delta_mW,
\qquad H_\epsilon\psi_\epsilon=0.
\tag{RV9}
\]

For nonlinear \(W\), this is generally a configuration-dependent correction, not an additive choice of vacuum energy. It is fixed by the stated factorization prescription, not by classical stationary action alone. Conversely, setting \(W=-\epsilon\log\psi\) after obtaining an unknown Hamiltonian's exact vacuum merely rewrites that Hamiltonian; it does not independently construct its response.

The linear calibration is transparent. On Euclidean \(Q\), let \(W(q)=q^TAq/2\) with \(A=A^T>0\). Then

\[
H_\epsilon
=-\frac{\epsilon^2}{2}\Delta
+\frac12q^TA^2q-\frac\epsilon2\operatorname{Tr}A,
\qquad
\operatorname{gap}H_\epsilon=\epsilon\lambda_{\min}(A).
\tag{RV10}
\]

Thus the finite Gaussian member recovers the frequencies of the [[algebra/cauchy-response-and-local-action|opposed-response construction]], with this explicit quantization convention. If the clock equation is chosen as \(i\epsilon\partial_t\Psi=H_\epsilon\Psi\), its rate generator is \(H_\epsilon/\epsilon\), not \(H_\epsilon\). The choice and calibration of \(t\) remain distinct from the configuration coordinates.

## A nonlinear response with no classical linear stiffness

Take the fixed Euclidean line, Lebesgue measure, and

\[
W(q)=\frac{q^4}{4},
\qquad N(q)=q^3\,dq.
\tag{RV11}
\]

Both \(N'(0)\) and \(V_{\mathrm{cl}}''(0)\), for \(V_{\mathrm{cl}}=q^6/2\), vanish. Nevertheless, with
\(D_\epsilon=\epsilon\partial_q+q^3\), the factored operator and its partner are

\[
H_-=\frac12D_\epsilon^*D_\epsilon
=\frac12\left[-\epsilon^2\partial_q^2+q^6-3\epsilon q^2\right],
\]
\[
H_+=\frac12D_\epsilon D_\epsilon^*
=\frac12\left[-\epsilon^2\partial_q^2+q^6+3\epsilon q^2\right].
\tag{RV12}
\]

Here the closed first-order operators have domain
\(\{u\in H^1(\mathbb R):q^3u\in L^2\}\).
The quadratic term is bounded relative to the sixth-power form with arbitrarily small relative bound, so these are the standard closed factorizations of the displayed Schrödinger operators. Both potentials tend to \(+\infty\); compactness on bounded intervals and control of the tails give compact resolvent.

Only \(H_-\) has a zero mode:

\[
\psi_\epsilon(q)=Z_\epsilon^{-1/2}e^{-q^4/(4\epsilon)},
\qquad
Z_\epsilon=\frac{(2\epsilon)^{1/4}}2\Gamma(1/4).
\tag{RV13}
\]

The adjoint zero-mode equation instead gives \(e^{q^4/(4\epsilon)}\), which is not square integrable. The maps \(D_\epsilon\) and \(D_\epsilon^*\), or their polar decomposition, identify the partners' nonzero spectra. Moreover,

\[
H_+\geq\frac12[-\epsilon^2\partial_q^2+3\epsilon q^2]
\geq\frac{\sqrt3}{2}\epsilon^{3/2}I.
\tag{RV14}
\]

The final inequality is the elementary harmonic-oscillator lower bound. Consequently it bounds the first nonzero eigenvalue of \(H_-\).

For the opposite bound, \(q\psi_\epsilon\) is orthogonal to the even vacuum and
\(D_\epsilon(q\psi_\epsilon)=\epsilon\psi_\epsilon\). Its Rayleigh quotient uses

\[
\int q^2\,d\mu_\epsilon
=(2\epsilon)^{1/2}\frac{\Gamma(3/4)}{\Gamma(1/4)}.
\]

Hence

\[
\boxed{
\frac{\sqrt3}{2}\epsilon^{3/2}
\leq\operatorname{gap}H_-
\leq
\frac{\Gamma(1/4)}{2\sqrt2\,\Gamma(3/4)}\epsilon^{3/2}.}
\tag{RV15}
\]

The two coefficients are approximately \(0.8660254\) and \(1.0460496\). The unitary dilation
\((V_\epsilon u)(x)=\epsilon^{1/8}u(\epsilon^{1/4}x)\)
gives \(V_\epsilon H_-(\epsilon)V_\epsilon^{-1}=\epsilon^{3/2}H_-(1)\). Thus the exact gap is \(c\epsilon^{3/2}\), with one fixed \(c\) lying in (RV15). No measured gap was inserted into the response. Nor was \(c\) identified with the zero classical Hessian.

## What a field realization still requires

The construction is useful when an independent global–local law actually supplies \(N\): the same response then controls the selected vacuum and quantum potential, rather than leaving them unrelated. The nonlinear example establishes this mechanism on a specified configuration line; it does not derive that line or its quartic response from a cosmological or gauge construction.

At a finite compact gauge regulator, an invariant metric, measure and \(W\) make the form invariant and permit restriction to the gauge-invariant carrier. In the field limit, however, \(\operatorname{div}N\) becomes a functional trace. Its existence, subtraction scheme and compatibility with the vacuum cannot be presumed. A nonlinear boundary response may also be spatially nonlocal; squaring it does not automatically return a local field Hamiltonian.

The remaining obligations are therefore concrete: construct the response independently, control its quantum divergence on the actual regulator family, recover the intended local observable dynamics, and retain a complete positive spectral edge in calibrated physical limits. Factorization and a normalizable vacuum supply a realization, not those limits by themselves.
