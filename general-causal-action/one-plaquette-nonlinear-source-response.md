# The One-Plaquette Source Separates Susceptibility from the Gap

For the actual one-plaquette \(SU(2)\) vacuum, the first nonlinear gap correction is \(-5\kappa/4\), below the leading \(4\sqrt{\kappa g}\). The normalized susceptibility of the compact scalar source \(B=\sin^2\theta\) agrees with the inverse gap through that first correction. At the next order they separate: the source acquires a positive weight in a higher physical excitation. Its normalized susceptibility becomes smaller than the inverse gap, while its innovation quotient becomes larger than the gap's own quotient. The calculation retains the changing vacuum, source mean and variance.

**Status: proved strong-confinement expansion on the complete one-plaquette class carrier.** This calibrates the nonlinear compact source of [[planar-patch-confinement-and-the-spatial-soft-mode|PP9–12]] at \(L=1\). [[conditional-vacuum-rigidity-and-the-physical-gap|The complete-source criterion]] distinguishes a resolvent response from a spectral edge; the difference below is computed within one supplied physical law.

## The exact radial carrier retains its curvature term

Write \(U=\cos\theta\,I-i\sin\theta\,\mathbf n\cdot\sigma\), \(0<\theta<\pi\). Haar probability on class functions is \((2/\pi)\sin^2\theta\,d\theta\). The four raw-link electric terms give
\[
H_g=4\kappa C+g(2-\chi_{1/2}(U))
=-\kappa(\partial_\theta^2+2\cot\theta\,\partial_\theta)
+2g(1-\cos\theta).
\tag{OP1}
\]
The unitary map \(f\mapsto\sqrt{2/\pi}\sin\theta\,f\) sends this operator to
\[
\widetilde H_g=-\kappa\partial_\theta^2-\kappa+2g(1-\cos\theta)
\quad\text{on }L^2(0,\pi),
\tag{OP2}
\]
with Dirichlet endpoints. This is the radial conversion already used in [[coarse-response-memory/radial-marginal-and-conditional-stress|the radial marginal equation]]. The constant curvature term \(-\kappa\) remains in the absolute vacuum energy.

Fix \(\kappa>0\), and put
\[
E=\sqrt{\kappa g},\qquad \delta=\sqrt{\kappa/g},\qquad
\theta=\sqrt\delta\,x.
\]
After unitary dilation, the exact scaled operator is
\[
\mathcal H_\delta=\widetilde H_g/E
=-\partial_x^2-\delta+\frac2\delta(1-\cos(\sqrt\delta\,x)),
\qquad 0<x<\pi/\sqrt\delta .
\]
Its expansion near the well is
\[
\mathcal H_\delta
=\mathcal H_0+\delta V_1+\delta^2V_2+\cdots,\qquad
\mathcal H_0=-\partial_x^2+x^2,\quad
V_1=-1-\frac{x^4}{12},\quad V_2=\frac{x^6}{360}.
\tag{OP3}
\]
The limiting half-line oscillator has normalized states \(|n\rangle\), \(n=1,3,5,\ldots\), of energies \(2n+1\). These are odd full-line Hermite states restricted and normalized on the half-line. Their odd labels encode the radial Dirichlet condition, not an additional center-parity restriction of the physical carrier.

## Controlled quasimodes justify the expansions

The single-well localization argument of [[corner-fast-vacuum-and-harmonic-separation|FH]] identifies every fixed scaled eigenvalue with its simple half-line oscillator limit. For higher coefficients, multiply the finite Hermite perturbation series by a fixed smooth cutoff in \(\theta\), equal to one near zero and supported before \(\pi\). The cutoff error on these Gaussian-polynomial states is smaller than every power of \(\delta\). Taylor's theorem for the cosine gives an \(O(\delta^{M+1})\) norm residual after solving the perturbation equations through order \(M\). Each equation is a finite Hermite calculation; the inverse of \(\mathcal H_0-(2n+1)\) is taken only off the selected state.

The uniformly separated nearby exact eigenvalue and its spectral projection then give the same eigenvalue and eigenvector expansion with \(O(\delta^{M+1})\) errors. This is an asymptotic construction, not an assertion that the unstable negative quartic polynomial alone defines the exact operator. For the source below, its rescaled multiplication norm is at most \(\delta^{-1}\). Constructing the eigenvector quasimodes to a sufficiently higher order therefore controls source-weighted errors as well. In particular the displayed first-order source vectors have \(O(\delta^2)\) remainders in norm, and their spectral weights have the errors used below.

## The full physical gap has a negative first correction

Even oscillator matrix elements are unchanged by restriction to the normalized odd half-line states. The usual creation-operator identity
\[
x^2|n\rangle
=\frac{\sqrt{n(n-1)}}2|n-2\rangle
+\left(n+\frac12\right)|n\rangle
+\frac{\sqrt{(n+1)(n+2)}}2|n+2\rangle
\]
determines every entry required here. The first two ordinary energy coefficients are
\[
e_n^{(1)}=\langle n,V_1n\rangle,\qquad
e_n^{(2)}=\langle n,V_2n\rangle
+\sum_{m\ne n}\frac{|\langle m,V_1n\rangle|^2}{2n-2m}.
\tag{OP4}
\]
Only the odd states within four levels of \(n\) enter that sum. They give

| Oscillator label | Leading energy | \(e_n^{(1)}\) | \(e_n^{(2)}\) |
| --- | ---: | ---: | ---: |
| \(n=1\), actual vacuum branch | \(3\) | \(-21/16\) | \(-9/256\) |
| \(n=3\), first physical excitation | \(7\) | \(-41/16\) | \(-91/256\) |

For example \(\langle1,x^4 1\rangle=15/4\), \(\langle3,x^4 3\rangle=75/4\), while their sixth moments are \(105/8\) and \(945/8\). Subtracting the two actual energies yields
\[
\boxed{
\frac{\Delta_g}{E}
=4-\frac54\delta-\frac{41}{128}\delta^2+O(\delta^3).}
\tag{OP5}
\]
Thus \(\Delta_g=4\sqrt{\kappa g}-5\kappa/4+O(\kappa\sqrt{\kappa/g})\). The curvature constant cancels from the gap but is retained in both energy entries above.

## The actual mean and covariance change with the vacuum

Let \(\psi_g\) be the normalized positive physical vacuum and set
\[
B(U)=|\mathbf q|^2=\sin^2\theta,\qquad
b_g=\langle B\rangle_g,\qquad
\sigma_g^2=\langle(B-b_g)^2\rangle_g .
\]
Its exact rescaled multiplication operator and first source correction are
\[
S_\delta=B/\delta
=\frac{\sin^2(\sqrt\delta\,x)}{\delta}
=x^2-\frac{\delta}{3}x^4+O(\delta^2x^6).
\tag{OP6}
\]
The quartic term here belongs to the observable; it is distinct from the quartic term of the magnetic potential.

Choose the oscillator phases by their standard Hermite polynomials. The actual scaled vacuum has the expansion
\[
|\Omega_\delta\rangle
=|1\rangle+\delta\left(\frac{5\sqrt6}{96}|3\rangle
+\frac{\sqrt{30}}{192}|5\rangle\right)+O(\delta^2).
\tag{OP7}
\]
Combining this vacuum correction with (OP6), rather than holding its measure fixed, gives
\[
\boxed{
b_g=\delta\left(\frac32-\frac{15}{16}\delta+O(\delta^2)\right),\qquad
\sigma_g^2=\delta^2\left(\frac32-\frac{135}{32}\delta+O(\delta^2)\right).}
\tag{OP8}
\]
For a direct covariance check, \(\langle S_\delta^2\rangle=15/4-(225/32)\delta+O(\delta^2)\). Subtracting \(\langle S_\delta\rangle^2\) produces the variance coefficient in (OP8).

## A higher excitation first appears at quadratic spectral weight

Let \(|n;\delta\rangle\) denote the exact eigenstate continued from \(|n\rangle\). Centering the source does not change its matrix elements between the vacuum and excited states. Differentiating both eigenvectors and the source yields
\[
\begin{aligned}
\langle3;\delta|S_\delta|\Omega_\delta\rangle
&=\frac{\sqrt6}{2}-\frac{45\sqrt6}{64}\delta+O(\delta^2),\\
\langle5;\delta|S_\delta|\Omega_\delta\rangle
&=-\frac{3\sqrt{30}}{16}\delta+O(\delta^2).
\end{aligned}
\tag{OP9}
\]
The first-order \(n=7\) amplitude cancels exactly; every remaining excited component starts at order \(\delta^2\) in norm. For verification, the amplitude derivative at any \(n\ne1\) is
\[
\langle n,S_1 1\rangle
+\sum_{m\ne1}\frac{\langle n,S_0m\rangle\langle m,V_1 1\rangle}{3-(2m+1)}
+\sum_{m\ne n}\frac{\langle n,V_1m\rangle\langle m,S_0 1\rangle}{(2n+1)-(2m+1)},
\]
where \(S_0=x^2\), \(S_1=-x^4/3\). This includes the actual excited-state change as well as the vacuum and observable changes.

The normalized centered physical source vector
\[
\xi_g=\frac{(B-b_g)\psi_g}{\sigma_g}
\]
therefore has weights
\[
w_3=1-\frac{45}{64}\delta^2+O(\delta^3),\qquad
w_5=\frac{45}{64}\delta^2+O(\delta^3),\qquad
\sum_{n\ge7}w_n=O(\delta^4).
\tag{OP10}
\]
The squared first-order amplitude in (OP9), divided by the leading variance \(3/2\), fixes \(45/64\). All spectral states in these expressions belong to the actual physical class carrier.

## Susceptibility equals inverse gap only to the first correction

Define the actual reduced-resolvent response
\[
\mathcal X_g=
\left\langle(B-b_g)\psi_g,
(H_g-E_0(g))^{-1}_{\perp}(B-b_g)\psi_g\right\rangle .
\tag{OP11}
\]
It is half the negative ground-energy Hessian for a linear perturbation \(-sB\). Equations (OP5), (OP8) and (OP10) give
\[
\mathcal X_g=\frac{\delta^2}{E}
\left(\frac38-\frac{15}{16}\delta+O(\delta^2)\right),\qquad
\frac{\mathcal X_g}{\sigma_g^2}
=\frac1E\left(\frac14+\frac5{64}\delta+O(\delta^2)\right).
\tag{OP12}
\]
The normalization in (OP8) is essential for the second formula. At this order it agrees with \(1/\Delta_g\), because the escaped spectral weight starts only at \(\delta^2\).

The next order separates them without requiring second-order observable amplitudes. The \(n=5\) excitation gap tends to \(8E\), whereas the first gap tends to \(4E\). Its weight in (OP10) therefore gives
\[
\boxed{
\frac{\mathcal X_g}{\sigma_g^2}-\frac1{\Delta_g}
=-\frac{45}{512E}\delta^2+O(\delta^3/E),}
\]
\[
\boxed{
\frac{\mathcal X_g}{\sigma_g^2}
=\frac1E\left(\frac14+\frac5{64}\delta
-\frac{89}{2048}\delta^2+O(\delta^3)\right).}
\tag{OP13}
\]
The exact spectral inequality \(\mathcal X_g/\sigma_g^2\le1/\Delta_g\) holds at every strength. Here the first strict asymptotic difference is calculated, rather than inferred from an assumed single-excitation source.

## The same leakage raises the fixed-source innovation quotient

Fix a scaled duration \(\tau>0\), so the physical duration is \(\tau/E\). Put
\[
A_{\tau,g}=e^{-\tau(H_g-E_0(g))/E},\qquad
R_{\tau,g}=I-A_{\tau,g}^2,\qquad
q_\tau(g)=\frac{\langle\xi_g,R_{\tau,g}^2\xi_g\rangle}
{\langle\xi_g,R_{\tau,g}\xi_g\rangle}.
\]
For \(d_g=\Delta_g/E\), the same weights imply
\[
\boxed{
q_\tau(g)
=1-e^{-2\tau d_g}
+\frac{45}{64}\delta^2 e^{-8\tau}(1-e^{-16\tau})
+O_\tau(\delta^3).}
\tag{OP14}
\]
To check the factor, the two leading response eigenvalues are
\(r_1=1-e^{-8\tau}\) and \(r_2=1-e^{-16\tau}\). A small second-channel weight \(w\) changes the quotient by \(w\,r_2(r_2-r_1)/r_1=w e^{-8\tau}(1-e^{-16\tau})\). The remainder is uniform when \(\tau\) stays in a fixed compact subset of \((0,\infty)\).

Thus the actual compact source has a smaller normalized susceptibility and a larger innovation quotient than their respective first-gap values at the first distinguishing order. This is spectral redistribution within one physical vacuum, not a change of clock or source normalization. The formulas are a one-plaquette calibration; they supply neither coefficients uniform in patch size nor an interchange of large-volume and strong-confinement limits.
