# Compact Gauge-Kernel Tangent Response

The normalized compact gauge readout has two different quadratic responses: its negative-log density at the most likely output penalizes both averaged mismatch and path scatter, while its Fisher metric detects only the averaged input velocity. A controlled near-identity scaling returns a normalized Gaussian readout; the scatter term cancels at leading order. This separates a conditional mode Hessian, statistical information, and the Gaussian approximation instead of treating them as one mass-producing cost.

## One kernel and its intrinsic moment

Use one factor of [[normalized-gauge-kernels-and-markov-residues|the normalized gauge kernel]], with \(G=SU(r)\), \(r\ge2\), and the real Lie-algebra norm

$$
\langle X,Y\rangle=-\operatorname{ReTr}(XY)/r,\qquad
f(W)=\operatorname{ReTr}W/r.
\tag{GK1}
$$

Let \(\mu_\kappa(dW)=e^{\kappa f(W)}dW/N_\kappa(I)\) and
\(\alpha_\kappa=\mu_\kappa(f)\). Irreducibility and conjugation invariance imply \(\mu_\kappa(W)\) is scalar; invariance under \(W\mapsto W^{-1}\) makes it real. Thus

$$
\mu_\kappa(W)=\alpha_\kappa I,\qquad
\alpha_0=0,\quad
\alpha_\kappa'=\operatorname{Var}_{\mu_\kappa}(f)>0,\quad
0<\alpha_\kappa<1\quad(\kappa>0).
\tag{GK2}
$$

The final strict inequality follows from full support and \(f(W)\le1\), with equality only at \(I\). The concentration parameter \(\kappa\) is still a freely chosen blocking parameter. Its moment \(\alpha_\kappa\) does not determine a physical mass.

Take \(W_i(t)=e^{tX_i}\), \(V(t)=e^{tY}\), and fixed weights \(w_i\). Write

$$
\overline X=\sum_iw_iX_i,\qquad
\mathscr D=\sum_iw_i\|X_i-\overline X\|^2.
\tag{GK3}
$$

Haar invariance makes \(N_\kappa(e^{tX})\) constant. Differentiating its logarithm twice gives the useful Ward identity

$$
\boxed{
\kappa^2\operatorname{Var}_{\mu_\kappa}
\left(\frac1r\operatorname{ReTr}(W^*X)\right)
=\kappa\alpha_\kappa\|X\|^2.}
\tag{GK4}
$$

The mean of this real score vanishes.

## The mode Hessian includes a scatter term

Put \(Z(t)=\sum_iw_i e^{tX_i}\). Direct differentiation of the numerator and then (GK4) give

$$
\begin{aligned}
\left[-\kappa\phi(V(t),Z(t))\right]''_0
 &=\kappa\bigl(\|Y-\overline X\|^2+\mathscr D\bigr),\\
\left[\log N_\kappa(Z(t))\right]''_0
 &=-\kappa\alpha_\kappa\mathscr D.
\end{aligned}
\tag{GK5}
$$

Consequently the exact Hessian of the negative-log density **relative to Haar**, at coincident inputs and output, is

$$
\boxed{
\left[-\log q_\kappa(V(t)\mid W_i(t))\right]''_0
=\kappa\|Y-\overline X\|^2
+\kappa(1-\alpha_\kappa)\mathscr D.}
\tag{GK6}
$$

The quadratic Taylor term is one half this expression. Multiple output links add their factors. Common motion \(X_i=Y\) is null, as required by endpoint covariance.

The formula also applies to smooth path products through the identity. Their second derivatives have the form \(X_i^2+A_i\), \(A_i\in\mathfrak{su}(r)\). The extra skew-adjoint terms have zero real trace and do not contribute. Equivalently, the negative-log kernel is stationary there, so its pullback Hessian depends only on the transport velocities.

This is not a global convexity statement on a compact group. Exponential-coordinate Lebesgue densities additionally contain the Haar Jacobian. For hidden fine-link coordinates those are the actual fine-link Jacobians, not independent Jacobians for overlapping path outputs.

## The Fisher metric has a larger kernel

Hold the sampled output \(V\) fixed and differentiate with respect to the input path:

$$
s(V)=\left.\partial_t\log q_\kappa(V\mid W_i(t))\right|_0
=\frac{\kappa}{r}\operatorname{ReTr}(V^*\overline X).
$$

Its variance is

$$
\boxed{
\mathcal J_\kappa((X_i))
=\mu_\kappa(s^2)
=\kappa\alpha_\kappa\|\overline X\|^2.}
\tag{GK7}
$$

This is also the expectation of the input negative-log Hessian under \(\mu_\kappa\), by differentiating the normalized fixed-Haar integral. It is not that Hessian evaluated only at \(V=I\). Every scatter direction with \(\overline X=0\) has zero Fisher information, despite the positive scatter term in (GK6).

An exact \(SU(2)\) witness makes the distinction visible without a limit. Take \(X=i\sigma_3\), equally weighted paths \(e^{tX},e^{-tX}\), and \(Z(t)=\cos t\,I\). Then

$$
q_t(V)=
\frac{e^{\kappa\cos t\,f(V)}}{N_{\kappa\cos t}(I)},\qquad
\left[-\log q_t(V)\right]''_0
=\kappa(f(V)-\alpha_\kappa).
\tag{GK8}
$$

The score is identically zero at \(t=0\). At \(V=I\) the Hessian is positive; its expectation is zero. Treating the mode curvature as a Fisher, entropy-loss, or physical-energy response would be a type error.

The Fisher calculation concerns this forward statistical readout on path data. Gauge-invariant observable statistics, reverse conditional susceptibility, and a physical vacuum Hilbert-space form require their own carrier maps.

## A normalized Gaussian limit, with the scale declared

For fixed group rank let \(m=r^2-1\). The unique maximum of \(f\) at \(I\) satisfies
\(f(e^X)=1-\|X\|^2/2+O(\|X\|^4)\).
Local Laplace expansion gives

$$
1-\alpha_\kappa=\frac{m}{2\kappa}+O(\kappa^{-2}).
\tag{GK9}
$$

Thus the fixed-coordinate scatter coefficient \(\kappa(1-\alpha_\kappa)\) tends to \(m/2\), not zero. This does not contradict the following diffusive limit.

Set \(\kappa=k/\varepsilon^2\), \(k>0\), \(W_i=e^{\varepsilon X_i}\), \(V=e^{\varepsilon Y}\). At bounded \(X_i,Y\),

$$
\kappa\phi(V,Z)
=\frac{k}{\varepsilon^2}
-\frac{k}{2}\|Y-\overline X\|^2
-\frac{k}{2}\mathscr D+O(\varepsilon).
$$

The same factor \(e^{-k\mathscr D/2}\) multiplies the normalizer. In orthonormal exponential coordinates \(dV=\varepsilon^m J(\varepsilon Y)dY\), the smooth Haar density has \(J(0)>0\). The unique nondegenerate nearby maximum and exponentially suppressed contributions outside a fixed identity neighborhood justify Laplace normalization. The rescaled probability law converges to

$$
\boxed{
\left(\frac{k}{2\pi}\right)^{m/2}
\exp\!\left[-\frac{k}{2}\|Y-\overline X\|^2\right]dY.}
\tag{GK10}
$$

This is weak convergence with convergence of the rescaled density on bounded coordinate sets, for fixed finite path data. It uses a scaled Laplace argument, not an unjustified uniform-in-\(\kappa\) remainder in (GK6). The scatter factor and Haar normalization cancel at leading order.

Now select the compatible endpoint-volume path family and weights in [[endpoint-averages-and-quadratic-ultraviolet-control|the endpoint-average theorem]]. For physical link fields, put \(U_e=e^{\varepsilon a A_e}\) and \(V_b=e^{\varepsilon b B_b}\). Then \(Y=bB\), \(\overline X=bM_nA\), and the product Gaussian exponent is

$$
-\frac{k}{2}b^{\,2-d}\|B-M_nA\|_b^2.
\tag{GK11}
$$

After orthogonal projection onto the harmonic-free gauge carrier \(H_j\), the covariance in \(d=4\) is \(b^2/k\) times its physical-metric identity. This is precisely the noise normalization \(\eta=1/k\) in [[soft-gaussian-gauge-blocking|soft Gaussian blocking]]. Ordinary gauge reduction alone would still retain harmonic constants. A fixed-coefficient choice in other dimensions needs a different mesh scaling to retain that same \(\eta b^2\) convention.

The normalized compact block and its classical quadratic mismatch have precedent in [[library/the-classically-perfect-fixed-point-action-for-su3-gauge-theory/inq|DeGrand et al.]], equations (4)--(7) and (15)--(16). Their full exponent includes the action coefficient \(\beta\); the parameter here denotes the entire concentration. The finite-\(\kappa\) Hessian and Fisher separation above are proved directly, not attributed to their saddle approximation.

This matches a conditional readout at fixed regulator and bounded near-identity input. It does not prove that the full Wilson measure concentrates there, control flat holonomy sectors, justify a gauge-fixed global Gaussian limit, or give estimates uniform in blocking depth. Those are the remaining steps before transferring the Gaussian ultraviolet theorem to the nonlinear law.

[[receipts/normalized_kernel_receipt.py|The verification receipt]] checks the compact \(SU(2)\) moment, Ward identity, mode/Fisher discrepancy, and rescaled density limit with deterministic Haar quadrature. None is a computation of a physical mass.
