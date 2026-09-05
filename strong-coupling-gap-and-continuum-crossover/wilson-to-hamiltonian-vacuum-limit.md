# The Wilson-to-Hamiltonian Vacuum Limit

At each fixed finite spatial lattice, anisotropic Wilson transfer powers converge in operator norm to the compact-rotor Hamiltonian semigroup. Their normalized positive vacuum vectors consequently converge, so a vacuum Poincare constant proved uniformly before taking the limit passes to the Hamiltonian vacuum with the same constant. This direction does not require volume-uniform convergence of the vectors and does not imply a converse uniform estimate for the finite-step Wilson spectrum.

**Status: [EXACT] for the finite compact carrier, nonnegative bounded smooth potential and normalization below.** Spatial regulator removal and infinite-volume representations require separate constructions.

## The time convention is part of the theorem

On a fixed finite set \(E\) of \(SU(2)\) links, use \(L|_l=l(l+2)\), the unit-\(S^3\) Laplacian. Set
\[
x=1/\varepsilon,\quad
K_\varepsilon=P_x^{\otimes E},\quad
f_\varepsilon=e^{-\varepsilon gW/2},\quad
T_\varepsilon=M_{f_\varepsilon}K_\varepsilon M_{f_\varepsilon},
\qquad g\ge0,\ W\ge0.
\tag{WH1}
\]
Here \(W\) is bounded and smooth at this fixed volume, and \(P_x\) is the normalized Wilson convolution. Define
\[
H_g=\tfrac12\sum_eL_e+gW.
\tag{WH2}
\]
Then, for integers \(n(\varepsilon)\) with \(n\varepsilon\to t>0\),
\[
\boxed{\|T_\varepsilon^{n(\varepsilon)}-e^{-tH_g}\|\longrightarrow0.}
\tag{WH3}
\]
The alternative convention \(a=1/(2x)\) gives kinetic coefficient one, not one half. No convention is changed inside (WH1)--(WH3).

## Resolve the entire representation tail

Put \(A_{0,\varepsilon}=(I-K_\varepsilon)/\varepsilon\). Fixed character labels converge by
\[
p_l(1/\varepsilon)
=1-\tfrac12 l(l+2)\varepsilon+O_l(\varepsilon^2).
\]
This is not by itself norm-resolvent convergence. If some edge label is at least \(M\), the [[bridge-score-fusion-geometry/wilson-bridge-envelopes-under-temporal-blocking|Näsell product bound]] gives
\[
\prod_ep_{l_e}(1/\varepsilon)
\le r_M(\varepsilon):=\prod_{\nu=1}^M(1+\nu\varepsilon)^{-1}.
\tag{WH4}
\]
For \(z>0\), the resolvent tail is bounded by
\[
\left[z+\frac{1-r_M(\varepsilon)}{\varepsilon}\right]^{-1},
\]
whose limit is \([z+M(M+1)/2]^{-1}\). Finite label sets have finite dimension at fixed \(E\). Taking their limit first and then \(M\to\infty\) proves
\[
(A_{0,\varepsilon}+z)^{-1}
\longrightarrow(\tfrac12\sum_eL_e+z)^{-1}
\quad\hbox{in norm}.
\tag{WH5}
\]

Let \(D_\varepsilon=(I-M_{f_\varepsilon})/\varepsilon\). Exactly,
\[
\frac{I-T_\varepsilon}{\varepsilon}
=A_{0,\varepsilon}+B_\varepsilon,\qquad
B_\varepsilon
=D_\varepsilon K_\varepsilon+K_\varepsilon D_\varepsilon
-\varepsilon D_\varepsilon K_\varepsilon D_\varepsilon.
\tag{WH6}
\]
At fixed volume, \(B_\varepsilon\) is uniformly bounded and converges strongly to multiplication by \(gW\). The limiting free resolvent in (WH5) is compact. A uniformly bounded strongly convergent sequence multiplied on the right by that compact resolvent converges in norm. Together with (WH5), this gives \(B_\varepsilon(A_{0,\varepsilon}+z)^{-1}\to gW(\tfrac12\sum L_e+z)^{-1}\) in norm. For \(z\) larger than the uniform perturbation norm, invert the bounded factors in the resolvent identity. Thus \((I-T_\varepsilon)/\varepsilon\) converges in norm resolvent to \(H_g\).

Positive-contraction functional calculus completes the proof. For \(0\le s\le1\),
\[
0\le e^{-n(1-s)}-s^n\le1/n.
\tag{WH7}
\]
To check the bound, write \(u=1-s\). For \(u\le1/2\), \(-\log(1-u)-u\le u^2\), so the difference is at most \(nu^2e^{-nu}\le4e^{-2}/n\). For \(u\ge1/2\), it is at most \(e^{-n/2}\le2/(en)\). Norm-resolvent convergence of nonnegative self-adjoint operators gives norm convergence of their positive-time exponential functions: approximate the exponential uniformly on \([0,\infty]\) by polynomials in a fixed resolvent. Applying (WH7), with \(n\varepsilon\to t\), proves (WH3).

## Pass the vacuum inequality in the safe direction

The limiting semigroup is compact and positivity improving. Its top eigenvalue is simple and isolated at every fixed finite volume. Norm convergence in (WH3) therefore gives norm convergence of the corresponding spectral projections. Choose normalized positive Perron vectors:
\[
\|\psi_{\varepsilon,\Lambda}-\psi_\Lambda\|_{L^2(dU)}\to0,
\qquad
\|\psi_{\varepsilon,\Lambda}^2-\psi_\Lambda^2\|_{L^1(dU)}
\le2\|\psi_{\varepsilon,\Lambda}-\psi_\Lambda\|_2\to0.
\tag{WH8}
\]
The top vectors of \(T_\varepsilon^n\) and \(T_\varepsilon\) agree because \(T_\varepsilon\) is Hilbert-positive.

Suppose an independently proved \(\lambda_*>0\), uniform in \(\varepsilon\) and \(\Lambda\), satisfies
\[
\lambda_*\operatorname{Var}_{\psi_{\varepsilon,\Lambda}^2dU}F
\le\int\sum_e|\nabla_eF|^2\psi_{\varepsilon,\Lambda}^2\,dU.
\tag{WH9}
\]
For each smooth \(F\), both integrands needed for the variance and Dirichlet form are bounded. Hence (WH8) passes (WH9) to the limiting vacuum at every \(\Lambda\), with the same \(\lambda_*\). Form closure extends it to its natural energy domain.

Integration by parts and \(H_g\psi_\Lambda=E_\Lambda\psi_\Lambda\) give the exact physical identity
\[
\langle\psi_\Lambda F,(H_g-E_\Lambda)\psi_\Lambda F\rangle
=\tfrac12\int\sum_e|\nabla_eF|^2\psi_\Lambda^2\,dU.
\tag{WH10}
\]
Consequently
\[
\boxed{H_g-E_\Lambda\ge
\tfrac12\lambda_*(I-|\psi_\Lambda\rangle\langle\psi_\Lambda|).}
\tag{WH11}
\]
If \(W\) is gauge invariant, as for the Wilson plaquette potential, gauge transformations preserve the positive unique vacuum and commute with \(H_g\), so restriction to the invariant subspace retains the estimate.

[[wilson-temporal-column-coercivity|Temporal-column coercivity]] supplies the independent input (WH9) in an explicit strong-coupling window. [[hamiltonian-product-vacuum-stability|Product-vacuum stability]] supplies a separate published route to interacting thermodynamic Hamiltonian vacua at sufficiently small magnetic/electric ratio.

The convergence constants and refinement thresholds used in proving (WH3) may depend on spatial volume; \(W\)'s norm is extensive. This is harmless for the passage of an already uniform inequality in (WH9), but it forbids using convergence alone to transfer a limiting Hamiltonian gap backward into a volume-uniform finite-\(\varepsilon\) Wilson gap. Neither direction by itself supplies a complete midpoint bridge bound.
