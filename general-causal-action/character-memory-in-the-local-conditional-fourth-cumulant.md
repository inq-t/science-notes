# Local Conditional Fourth Cumulants Retain the Character Preparation

The higher-character deformation whose gap coefficient follows the spatial soft frequency remains detectable in a fixed local conditional source. Its fourth-cumulant coefficient has a strictly positive bulk limit when the containing patch grows. Both results use the inherited vacuum covariance and the same bounded face mark. This separates the shrinking absolute gap response from erasure of the preparation data; it does not contradict a common leading harmonic limit or establish a four-dimensional universality class.

**Status: proved fixed-patch actual parameter contrast and sequential bulk coefficient limit.** [[equal-character-hessians-and-the-nonlinear-source-discriminator|EH]] fixes the preparation and source; [[weighted-character-gap-coefficient-and-the-spatial-soft-mode|WS]] owns the gap comparison. The argument below extends EH's conditional contrast without calculating the common second kinetic or vacuum coefficient. No uniform remainder for the growing compact conditional law is asserted.

## The parameter difference cancels the common vacuum terms

Use EH's fixed \(SU(2)\) representation and positive preparation family
\[
\rho=\rho_{1/2}\oplus\rho_1\oplus\rho_{3/2},\qquad
A_\varepsilon=(1+14\varepsilon)I_2
\oplus(1-16\varepsilon)I_3
\oplus(1+5\varepsilon)I_4,
\quad -1/14<\varepsilon<1/16.
\]
On an open \(L\times L\) face patch \(\Lambda\), keep every vertex Gauss constraint, the actual comb face words and
\[
h=(\kappa/(15g))^{1/4},\qquad E=\kappa/h^2,\qquad
C_\Lambda=\sqrt{4I-\operatorname{Adj}_\Lambda}.
\tag{LCM1}
\]
These scales and the electric operator are common to the family. The harmonic probability law is \(\mu_{0,\Lambda}=\Omega_\Lambda^2\,dX\), with covariance \(C_\Lambda\otimes I_3\).

In flat Haar-density coordinates write the normalized vacuum coefficients as
\[
\Phi_{\varepsilon,h}
=\Omega_\Lambda\{1+h\alpha_\Lambda+h^2a_{2,\varepsilon}+O(h^3)\},
\qquad b_\varepsilon=a_{2,\varepsilon}-\tfrac12\alpha_\Lambda^2.
\]
The remainder here is available with every fixed polynomial weight. The metric, first operator and first vacuum coefficient do not vary with \(\varepsilon\). EH's character calculation gives
\(\partial_\varepsilon V_2=-7\sum_p|X_p|^4/120\).
Subtracting the two logarithmic vacuum equations, as derived in [[logarithmic-vacuum-curvature-and-conditional-cumulants|LCV4–5]], therefore gives
\[
\boxed{
\mathcal L_{0,\Lambda}\,\partial_\varepsilon b_\varepsilon
=\frac7{120}\left\{\sum_p|X_p|^4-
\mathbb E_0\sum_p|X_p|^4\right\},\qquad
\mathbb E_0\partial_\varepsilon b_\varepsilon=0,}
\tag{LCM2}
\]
where
\(\mathcal L_{0,\Lambda}=-\partial^{\mathsf T}C_\Lambda^2\partial
+(C_\Lambda X)\cdot\partial\) is the positive Gaussian generator. Its inverse on this centered polynomial is unambiguous at each fixed patch.

The corresponding Ornstein–Uhlenbeck semigroup has conditional mean \(e^{-sC_\Lambda}X\). Its degree-four part consequently gives
\[
\boxed{
(\partial_\varepsilon b_\varepsilon)_4(X)
=\frac7{120}\int_0^\infty
\sum_{p\in\Lambda}|(e^{-sC_\Lambda}X)_p|^4\,ds.}
\tag{LCM3}
\]
The full solution also has degree-two and constant terms. They affect lower conditional moments but not the fourth cumulant. No assumption that the separate common kinetic terms vanish is needed.

For completeness, the actual fixed-\(L\) vacuum argument has the same smooth cover as [[fixed-group-compact-vacuum-and-oriented-source-return|GV]]: the chord rows are triangular, so solving the finite system gives ellipticity on \(SU(2)^{L^2}\), with an \(L\)-dependent constant. The positive weighted cost has a unique identity well. Equivariant localization and the separated harmonic vacuum then give arbitrarily accurate polynomial-Gaussian quasimodes. The fiber argument of [[regional-conditional-projection-and-the-vacuum-score|VP]] applies to the complete retained face coordinates. These are fixed-dimensional arguments; none supplies an \(L\)-uniform conditional remainder.

## Keep the original source and its conditional products

Fix a face \(r\), retain every other complete face \(S=\Lambda\setminus\{r\}\), and set
\[
\sigma_{\Lambda,r}=\bigl((C_\Lambda^{-1})_{rr}\bigr)^{-1},
\qquad
J_{\Lambda,r}=\int_0^\infty\sum_{p\in\Lambda}
\bigl(e^{-sC_\Lambda}\bigr)_{pr}^{\,4}\,ds.
\tag{LCM4}
\]
The harmonic conditional law is \(X_r=m_r(X_S)+\eta_r\), where \(\eta_r\) is independent of \(X_S\) with covariance \(\sigma_{\Lambda,r}I_3\). It is inherited from the containing patch.

Use the fixed unweighted representation mark from EH and [[weighted-character-scale-and-bounded-lie-sources|GM]]:
\[
\widehat X_{r,h}=\frac2h q_\rho(P_r),\qquad
\frac2h q_\rho(e^{hX})
=X-\frac{11}{40}h^2|X|^2X+O(h^4).
\tag{LCM5}
\]
The mark is bounded before the displayed scaling and is identical for all \(\varepsilon\). In each actual vacuum define
\[
Z_r=\widehat X_{r,h}-\mathbb E_{\varepsilon,h}
 [\widehat X_{r,h}\mid P_S],\qquad
V_r=\mathbb E_{\varepsilon,h}[Z_r\otimes Z_r\mid P_S],
\]
\[
\mathcal K_{\varepsilon,L,r}(h)
=\mathbb E_{\varepsilon,h}[|Z_r|^4\mid P_S]
-(\operatorname{Tr}V_r)^2-2\operatorname{Tr}(V_r^2).
\tag{LCM6}
\]
This double trace of the conditional fourth-cumulant tensor is invariant under simultaneous conjugation. Conditioning is on complete faces, not only their scalar characters or their projected marks.

The probability log-score contributes \(2h^2b_\varepsilon\). Four missing-face derivatives of LCM3 give the directional parameter contrast
\[
\frac{14}{5}(\varepsilon_2-\varepsilon_1)
h^2\sigma_{\Lambda,r}^4J_{\Lambda,r}|H|^4
\tag{LCM7}
\]
for the fourth cumulant of \(Q(H,\widehat X_{r,h})\). The factor is \(2\cdot4!\cdot7/120\). Lower-degree terms cancel from a fourth cumulant, and the cubic mark correction in LCM5 is common to both preparations. The isotropic double trace in three colors multiplies LCM7 by five. Thus, for fixed \(L,r,\varepsilon_1,\varepsilon_2\),
\[
\boxed{
\mathbb E_{\varepsilon_2,h}\mathcal K_{\varepsilon_2,L,r}(h)
-\mathbb E_{\varepsilon_1,h}\mathcal K_{\varepsilon_1,L,r}(h)
=14(\varepsilon_2-\varepsilon_1)
h^2\sigma_{\Lambda,r}^4J_{\Lambda,r}+O(h^3).}
\tag{LCM8}
\]
The coefficient of the difference is independent of retained face values; the common individual coefficients need not be. The two expectations use their respective actual retained marginals.

The source and its fourth products grow as powers of \(h^{-1}\), so vacuum quasimodes are taken to sufficiently high order before multiplication. VP's polynomial-weighted fiber estimates, conditional Jensen bounds and finite Hölder products then give the integrated \(O(h^3)\) remainder in LCM8, exactly as for LCV's conditional cumulants. This argument does not divide by a small actual conditional variance. The constants may depend on the fixed patch and parameters.

## The local coefficient has a positive bulk limit

Translate \(r\) to the origin and let its distance to the boundary tend to infinity. Define the unrestricted lattice kernel
\[
a_s(x)=(e^{-sC_\infty})_{x0},\qquad
C_\infty=\sqrt{4I-\operatorname{Adj}_{\mathbb Z^2}},
\]
\[
\omega(k)=\sqrt{4-2\cos k_1-2\cos k_2}.
\]
[[lattice-poisson-tails-and-collar-localization|LP1–7]] proves positivity, killed-kernel comparison and the diagonal estimate
\[
0\le a_s^\Lambda(x,r)\le a_s(x-r),\qquad
a_s(0)\le \frac{C}{(1+s)^2}.
\tag{LCM9}
\]
For each fixed \(s,x\), the killed kernel tends to the unrestricted one. Indeed the continuous-time random walk has a finite Poisson number of jumps on every fixed heat interval, so the probability of reaching a receding boundary vanishes. Subordination and dominated convergence pass this to the Poisson kernel. Nested boxes are not required.

The spectral identity \(C_\Lambda^{-1}=\int_0^\infty e^{-sC_\Lambda}\,ds\), applied to its diagonal, and LCM9 give
\[
\boxed{
\sigma_{\Lambda,r}\longrightarrow
\sigma_\infty=
\left\{\int_0^\infty a_s(0)\,ds\right\}^{-1}
=\left\{\int_{[-\pi,\pi]^2}
\frac{d^2k}{(2\pi)^2\,\omega(k)}\right\}^{-1}>0.}
\tag{LCM10}
\]
The integral is finite: \(\omega(k)\ge2|k|/\pi\) near the only zero, and \(1/|k|\) is locally integrable in two dimensions. The diagonal integral is also strictly positive.

Positive definiteness gives
\[
a_s(x)\le a_s(0),\qquad
\sum_x a_s(x)^2=a_{2s}(0).
\]
Consequently
\[
\sum_xa_s(x)^4\le a_s(0)^2a_{2s}(0)
\le\frac{C}{(1+s)^6}.
\]
Pointwise killed-kernel convergence and domination on
\(\mathbb Z^2\times(0,\infty)\) therefore prove
\[
\boxed{
J_{\Lambda,r}\longrightarrow
J_\infty=\int_0^\infty\sum_{x\in\mathbb Z^2}a_s(x)^4\,ds,
\qquad 0<J_\infty<\infty.}
\tag{LCM11}
\]
Strict positivity already follows from the origin term near \(s=0\), where it tends to one. These estimates use the same containing lattice covariance throughout.

## A source-sensitive test of the reduction

For fixed \(\varepsilon_2\ne\varepsilon_1\), LCM8–11 yield
\[
\boxed{
\lim_{\operatorname{dist}(r,\partial\Lambda)\to\infty}
\lim_{h\to0}
\frac{\mathbb E_{\varepsilon_2,h}\mathcal K_{\varepsilon_2,L,r}
-\mathbb E_{\varepsilon_1,h}\mathcal K_{\varepsilon_1,L,r}}
 {(\varepsilon_2-\varepsilon_1)h^2}
=14\sigma_\infty^4J_\infty>0.}
\tag{LCM12}
\]
Dividing instead by the additional common harmonic variance square
\(\sigma_{\Lambda,r}^2\) gives the positive limit
\(14\sigma_\infty^2J_\infty\). This is a specified coefficient normalization, not an inverse bound on the actual conditional variance.

WS's absolute gap coefficient tends to zero with the lowest spatial frequency; the conditional fourth-cumulant coefficient does not. The complete first-order inventory therefore remains insufficient for this higher-order local source law even as the patch grows. A positive rescaled coefficient is compatible with convergence of the unrescaled statistic to its common harmonic value as \(h\to0\). It proves neither different continuum universality classes nor failure of an explicitly defined coarse-graining limit.

The next analytic upgrade would control LCM8 uniformly along a stated compact growing-patch trajectory. The uniform gap and vacuum-energy estimates alone do not supply that conditional theorem. Any stronger claim that the character input disappears under refinement must specify its retained source algebra and complete sourced boundary map, as in [[holonomy-state-refinement/overlap-kernels-and-face-refinement|OF15–18]], rather than infer erasure from one soft eigenvalue.
