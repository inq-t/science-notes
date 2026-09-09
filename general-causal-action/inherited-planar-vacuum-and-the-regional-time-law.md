# The Inherited Planar Vacuum Has a Regional Memory

A finite region inherited from the full planar harmonic vacuum has a different state and chronological law from an independently prepared block. Its complete Gaussian history is obtained by compressing the full covariance at every time separation. That compression generally fails the semigroup law, even on a neutral one-face quadratic source. In the bulk infinite-lattice limit, a fixed local source has an algebraic temporal tail where the independently prepared finite block has exponential decay. This gives an exact acceptance test for spatial sewing.

**Status: exact harmonic regional law and bulk asymptotics.** [[planar-patch-confinement-and-the-spatial-soft-mode|PP6]] fixes the oscillator and Gauss convention. [[spatial-block-sewing-and-the-vacuum-cap-response|SB]] explains why an inherited history retains its vacuum caps and differs from a reset regional transfer. No actual compact regional-return theorem is assumed here.

## Compress the complete history, not only its equal-time state

On a finite connected planar face grid \(\Lambda\), put
\[
A_\Lambda=4I-\operatorname{Adj}_\Lambda,\qquad
\Omega_\Lambda=A_\Lambda^{1/2},\qquad
\mathcal O_\Lambda=p^{\mathsf T}(A_\Lambda\otimes I_3)p+|X|^2/4.
\tag{IR1}
\]
The ground-state probability has independent colors, each of covariance \(\Omega_\Lambda\). Its stationary chronological Gaussian process satisfies
\[
\mathbb E[X_a(0)X_b(t)^{\mathsf T}]
=\delta_{ab}\,\Omega_\Lambda e^{-|t|\Omega_\Lambda}.
\tag{IR2}
\]
Thus a region \(B\subset\Lambda\) inherits
\[
\boxed{C_B=(\Omega_\Lambda)_{BB},\qquad
D_B(t)=(\Omega_\Lambda e^{-|t|\Omega_\Lambda})_{BB}.}
\tag{IR3}
\]
For arbitrary regional linear marks \(J_i\) at finitely many times, the generating function is
\(\exp[\frac12\sum_{i,j,a}J_{i,a}^{\mathsf T}D_B(t_i-t_j)J_{j,a}]\).
This determines the entire Gaussian history and all its mixed polynomial responses.

The calculation uses the common framed Gaussian cover before simultaneous color averaging. Neutral sources below are already invariant. The equal-time marginal is a probability density, not the full quantum reduced density operator or a claim that the physical Hilbert space factors across the cut.

For real vectors \(b,c\) supported in \(B\), write
\[
k_{bc}(t)=b^{\mathsf T}\Omega_\Lambda e^{-|t|\Omega_\Lambda}c,\qquad
F_b=|b^{\mathsf T}X|^2-3k_{bb}(0).
\]
Wick contraction gives the exact mixed marked response
\[
\boxed{
\mathbb E[F_b(0)F_c(t)]=6k_{bc}(t)^2,\qquad
\mathcal C_b(t)=
\frac{\mathbb E[F_b(0)F_b(t)]}{\operatorname{Var}F_b}
=\left[\frac{k_{bb}(t)}{k_{bb}(0)}\right]^2.}
\tag{IR4}
\]
Here \(\operatorname{Var}F_b=6k_{bb}(0)^2\); no independent source normalization is substituted.

The full time-Fourier covariance is
\[
\widehat D_B(\xi)=
\left[2A_\Lambda(\xi^2+A_\Lambda)^{-1}\right]_{BB}.
\tag{IR5}
\]
Its inverse is the Schur complement, across the spatial cut, of the full history precision
\(\frac12(I+\xi^2A_\Lambda^{-1})\).
It generally depends on frequency through the eliminated exterior.

## One retained face already detects the reset

For a single face \(p\) in a nontrivial connected grid, let
\(c=(\Omega_\Lambda)_{pp}\). Then \(c<2\): Cauchy–Schwarz gives
\(c^2\le(\Omega_\Lambda^2)_{pp}=4\), and equality would make \(e_p\) an eigenvector of \(A_\Lambda\), contrary to its neighboring entries.

Let \(Q_t\) be conditional expectation between the two inherited regional time slices. Its Gaussian conditional mean is \(D_B(t)C_B^{-1}X_B\). Generally the Markov identity would require
\[
D_B(t+s)=D_B(t)C_B^{-1}D_B(s),
\tag{IR6}
\]
which fails. For the single face, \(k(t)=\sum_j a_j\omega_j e^{-t\omega_j}\), with \(a_j\ge0\), and at least two distinct frequencies have positive weight. Strict Cauchy–Schwarz gives
\[
c\,k(2t)>k(t)^2,\qquad t>0.
\]
For its normalized neutral quadratic \(f=F_{e_p}/(\sqrt6c)\),
\[
\boxed{
(Q_{2t}-Q_t^2)f
=\left[\left(\frac{k(2t)}c\right)^2
-\left(\frac{k(t)}c\right)^4\right]f\ne0.}
\tag{IR7}
\]
The complete process remains Markov; discarding the exterior creates regional memory.

Moreover, \(k'(0+)=-4\) and \(c\,k''(0+)>16\), by strict Cauchy–Schwarz on the same frequency weights. Even a scalar Gaussian Markov clock fitted to the inherited variance and initial slope, \(k_{\mathrm{fit}}(t)=c e^{-4t/c}\), misses the second derivative.

An independently prepared one-face oscillator instead has \(A_B=4\), variance \(2\), and \(\mathcal C_b(t)=e^{-4t}\). More generally, independent preparation uses \(\sqrt{A_B}\), not \((\sqrt{A_\Lambda})_{BB}\), with \(A_B=4I-\operatorname{Adj}_B\). Its fixed-source covariance is a finite sum of exponentials, asymptotically decaying at twice its lowest frequency with nonzero source overlap.

## The bulk limit makes the difference algebraic

Embed a fixed nonzero finitely supported real \(b\) in boxes whose boundary distance from its support tends to infinity. For each fixed \(t\), continuous functional calculus gives
\[
\boxed{
k_b(t)\longrightarrow
\int_{[-\pi,\pi]^2}
|\widehat b(k)|^2\omega(k)e^{-t\omega(k)}
\frac{d^2k}{(2\pi)^2},\quad
\omega(k)=\sqrt{4-2\cos k_1-2\cos k_2},}
\tag{IR8}
\]
where \(\widehat b(k)=\sum_p b_pe^{-ik\cdot p}\).
Indeed polynomial matrix elements stabilize once the boundary is sufficiently far away; uniform polynomial approximation applies to \(\sqrt a\,e^{-t\sqrt a}\) on \([0,8]\).

Use \(k_b\) for this limiting function and \(c_b=k_b(0)>0\). If \(B_0=\sum_pb_p\ne0\), then
\[
\boxed{
k_b(t)\sim\frac{B_0^2}{\pi t^3},\qquad
\mathcal C_b(t)\sim
\frac{B_0^4}{\pi^2c_b^2}\,t^{-6}.}
\tag{IR9}
\]
If \(\sum_pb_p=0\), but \(m=\sum_pb_pp\ne0\), then
\[
\boxed{
k_b(t)\sim\frac{6|m|^2}{\pi t^5},\qquad
\mathcal C_b(t)\sim
\frac{36|m|^4}{\pi^2c_b^2}\,t^{-10}.}
\tag{IR10}
\]
For proof, \(\omega(k)=|k|+O(|k|^3)\). Rescale \(k=u/t\), while the torus away from zero contributes exponentially little. The angular integrals are \(2\pi B_0^2\) and \(\pi|m|^2\); the radial integrals are \(\Gamma(3)=2\) and \(\Gamma(5)=24\). Higher moment cancellations give faster powers, rather than a spectral gap: a nonzero finite-support trigonometric polynomial has finite vanishing order at \(k=0\).

Nevertheless the fixed local source has finite integrated normalized susceptibility:
\[
\frac1{2\sqrt8}\le
\mathcal S_b:=\int_0^\infty\mathcal C_b(t)\,dt
\le\frac{\|b\|_2^2}{2c_b}<\infty.
\]
Indeed, with probability weight \(d\mu_b=|\widehat b(k)|^2\omega(k)d^2k/[(2\pi)^2c_b]\), its integral is \(\iint(\omega+\omega')^{-1}d\mu_b d\mu_b'\); use \((a+b)^{-1}\le(a^{-1}+b^{-1})/4\). Its spectral support still reaches zero. A favorable response of this one source therefore supplies no complete-source uniform bound of the kind required by [[conditional-vacuum-rigidity-and-the-physical-gap|CV]].

These tails require the bulk limit before the long-duration limit. Every finite box still has discrete exponential tails; keeping the source near an exterior boundary instead gives a different limit. Time here is PP's scaled time, with physical duration \(t/\sqrt{\kappa g}\). No joint fixed-physical-time or interacting infinite-volume limit follows.

The acceptance test is to return (IR3)–(IR5), including mixed sources, when eliminating an exterior. Replacing them by an independent block misses both its inherited vacuum and its memory. Extending this test to the actual compact law requires compatible connector/source transport and the full regional marked return, beyond the currently proved soft-source estimate.
