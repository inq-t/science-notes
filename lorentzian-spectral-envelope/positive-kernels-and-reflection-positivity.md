# A Positive Kernel Need Not Be Reflection Positive

The stationary kernel \(\operatorname{sech}^2(\nu(t-s))\) has a positive Fourier transform, but its time-reflected kernel \(\operatorname{sech}^2(\nu(t+s))\) has a negative two-by-two determinant whenever the positive times differ. It therefore cannot directly serve as a reflection-positive Euclidean two-point function for that reflection. The same profile remains a valid probability density, Fisher response, and Witten potential: changing its role changes the positivity test.

## Two different pairings

For an even continuous function \(K:\mathbb R\to\mathbb R\), ordinary stationary positive definiteness asks for
\[
\sum_{i,j}\overline{c_i}c_j K(t_i-t_j)\ge0.
\tag{PR1}
\]
Bochner's theorem characterizes this by a positive Fourier measure. Reflection about zero instead asks, already on linear positive-time insertions, for
\[
\sum_{i,j}\overline{c_i}c_j K(t_i+t_j)\ge0,
\qquad t_i,t_j>0.
\tag{PR2}
\]
The signs inside the argument differ. [[library/reflection-positivity-and-spectral-theory/inq|The reflection-positive Hilbert construction]] requires the second pairing, together with the additional data needed for reconstruction. The first does not imply it.

## The exact sech counterexample

Take \(K(t)=\operatorname{sech}^2(\nu t)\), \(\nu>0\). In the convention \(\widehat K(k)=\int e^{-ikt}K(t)\,dt\),
\[
\widehat K(k)=\frac{\pi k}{\nu^2\sinh(\pi k/(2\nu))}>0,
\qquad \widehat K(0)=\frac2\nu.
\tag{PR3}
\]
Thus (PR1) holds. But
\[
\frac{d^2}{dt^2}\log K(t)=-2\nu^2\operatorname{sech}^2(\nu t)<0.
\]
Strict log concavity gives, for distinct \(s,t>0\),
\[
K(s+t)^2>K(2s)K(2t).
\]
Therefore the reflected Gram matrix
\[
\boxed{
\det\begin{pmatrix}
K(2s)&K(s+t)\\K(s+t)&K(2t)
\end{pmatrix}<0.}
\tag{PR4}
\]
One eigenvalue is negative. The failure also holds for sufficiently narrow smooth positive-time test functions approximating the two insertions, by continuity.

This corrects the Bochner-to-OS inference in the immutable
[[the-grain-of-causal-scale/inbox/the-carrier-and-zeta/the-carrier-and-zeta|carrier-and-zeta exploration]]. The Fourier-transform calculation there is compatible with (PR3); the inference to reflection positivity is not.

## A constructive positive-time alternative

Given a finite positive measure \(\mu\) on \([0,\infty)\), the kernel
\[
K_\mu(t)=\int e^{-E|t|}\,d\mu(E)
\tag{PR5}
\]
satisfies (PR2), since its reflected quadratic form is
\[
\int\left|\sum_j c_j e^{-Et_j}\right|^2d\mu(E)\ge0.
\]
It is also ordinarily positive definite. Under a reconstructed positive-energy semigroup, the spectral theorem supplies precisely this positive Laplace measure for the appropriate two-point channel. The variables in (PR5) are abstract; physical units require \(E t\) to be replaced by the correctly calibrated energy--time or energy--length ratio.

On the positive-time branch \(t>0\), every nonzero \(K_\mu(t)\) is log convex:
\[
(\log K_\mu)''(t)=\operatorname{Var}_{\mu_t}(E)\ge0,\qquad
d\mu_t=\frac{e^{-Et}d\mu(E)}{K_\mu(t)}.
\tag{PR6}
\]
This is the opposite curvature from the proposed stationary sech profile. Positive-time Laplace spectra, not a generic positive Fourier spectrum, are the relevant test here.

## The operator type determines the test

The density \(q(N)\propto\operatorname{sech}^2(\nu N)\) is still normalized and positive. The
[[binary-information-geometry/witten-darboux|Witten--Darboux operator]]
constructed from its half-density remains self-adjoint, nonnegative, and gapped on its declared complement. Its semigroup supplies reflection-positive kernels of the form
\[
\langle f,e^{-(s+t)H}f\rangle
=\langle e^{-sH}f,e^{-tH}f\rangle.
\]
Those kernels are not the assertion \(K(s+t)=\operatorname{sech}^2(\nu(s+t))\).

Likewise, a positive Hermitian metric on a complex manifold, the exceptional Jordan order cone, and a CP map each have their own positive pairing. A physical Euclidean theory must additionally pass the reflected test. No one of these notions is discredited by another having a different domain.

[[contemporary-puzzles/yang-mills-mass-gap/receipts/positivity_rigidity_audit_receipt.py|The audit receipt]] checks (PR4) directly against a positive Laplace-mixture comparison.
