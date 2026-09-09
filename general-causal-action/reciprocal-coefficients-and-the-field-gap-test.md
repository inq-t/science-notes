# Reciprocal Coefficients and the Field Gap Test

Reciprocal electric and magnetic coefficients fix the propagation rate of the quadratic field, while leaving long-wavelength excitations arbitrarily soft as the spatial domain grows. The exact finite cochain calculation below identifies what the shared-preparation coefficient relation supplies and what a non-Abelian rigidity theorem must add. It tests the field limit of [[anchored-word-cost-and-the-interacting-return|the interacting return]], rather than treating a compact-frame exchange rate as a field mass.

**Status: exact for the specified quadratic gauge model; conditional as a diagnostic of the nonlinear return.** No estimate below replaces the full interacting vacuum by its quadratic approximation when making a Yang–Mills claim. [[holonomy-state-refinement/holonomy-refinement-and-clock-compatibility|The weighted-cycle theorem]] gives the separate electric-only refinement test.

## Retain the incidence maps and the gauge quotient

On a finite periodic cubic cell complex with \(L\ge3\) sites in each of three directions, let \(C^j\) be real \(j\)-cochains with their counting pairings. The incidence maps satisfy
\[
C^0\xrightarrow{d_0}C^1\xrightarrow{d_1}C^2,
\qquad d_1d_0=0.
\tag{FG1}
\]
The linear gauge change is \(A\mapsto A+d_0\phi\). Remove the longitudinal directions and, for this test, hold the harmonic zero modes fixed. The remaining transverse space is
\[
\mathcal T=(\operatorname{ran}d_0)^\perp
\cap(\ker d_1)^{\perp}.
\tag{FG2}
\]
Thus \(K=d_1^*d_1\) is strictly positive on this finite-dimensional space. The exclusion of harmonic modes is explicit; the result will exhibit soft excitations even after that exclusion.

Choose \(e_*,b_*>0\) and a common scale \(s>0\). On \(L^2(\mathcal T,dA)\), consider
\[
H_s=\frac12\left[\frac{e_*}{s}\,\|P\|^2
+b_*s\,\|d_1A\|^2\right],\qquad P=-i\nabla_A.
\tag{FG3}
\]
Its electric and magnetic coefficients have constant product \(e_*b_*\). They model the reciprocal scale dependence returned by one preparation; trace and metric conventions are absorbed into the declared constants. This is a noncompact quadratic configuration model, not the original compact-link Hamiltonian.

If \(K\) has orthonormal eigenvectors with positive eigenvalues \(\nu_j^2\), then (FG3) is a sum of independent oscillators with
\[
\omega_j=\sqrt{e_*b_*}\,\nu_j,
\qquad
H_s-E_0=\sum_j\omega_j N_j.
\tag{FG4}
\]
The unitary dilation \(B=\sqrt{s}\,A\) removes \(s\) from the entire operator. Changing the shared scale reshapes its Gaussian vacuum but cannot alter the excitation frequencies of this quadratic member.

## The returned invariant is a propagation coefficient

The paired Hamilton equations are
\[
\dot A=\frac{e_*}{s}P,\qquad
\dot P=-b_*sKA,
\qquad
\boxed{\ddot A=-e_*b_*KA.}
\tag{FG5}
\]
The same product that couples the two preparation moments therefore supplies the coefficient of the incidence wave equation. In this realization, the reciprocal relation determines how quickly a spatial distinction propagates. A mass would require an additional positive low-frequency spectral edge after the physical reconstruction.

This identifies a possible division of roles for the broader programme: an invariant product may help return the arena's propagation law, while a non-Abelian, state-dependent rigidity theorem supplies the mass. Equating that product directly with a gap would discard the spatial operator \(K\).

## The complete transverse dispersion has soft modes

For lattice momentum \(k_i=2\pi n_i/L\), put \(\delta_i=e^{ik_i}-1\). In Fourier coordinates,
\[
\widehat{d_0\phi}_i=\delta_i\widehat\phi,
\qquad
\widehat{d_1A}_{ij}=\delta_i\widehat A_j-\delta_j\widehat A_i.
\tag{FG6}
\]
The elementary Gram identity gives
\[
\sum_{i<j}|\delta_i A_j-\delta_j A_i|^2
=|\delta|^2|A|^2-|\delta^*A|^2.
\tag{FG7}
\]
Hence each nonzero momentum has two transverse polarizations with
\[
\nu(k)^2=\sum_i|e^{ik_i}-1|^2
=4\sum_i\sin^2(k_i/2),\qquad
\omega(k)=2\sqrt{e_*b_*}\sqrt{\sum_i\sin^2(k_i/2)}.
\tag{FG8}
\]
Real sine and cosine modes implement the same oscillator decomposition without complexifying the physical configuration space. The least nonzero excitation is therefore
\[
\boxed{\operatorname{gap}_{\rm quad}(L)
=2\sqrt{e_*b_*}\sin(\pi/L)\longrightarrow0.}
\tag{FG9}
\]
The conclusion is independent of \(s\). Even if the preparation scale varies with \(L\), the reciprocal family with fixed \(e_*b_*\) cannot eliminate this sequence.

If the spatial spacing is \(a\), and the physical normalization sets \(\sqrt{e_*b_*}=v/a\), then at fixed physical side \(\ell=La\), the edge tends to \(2\pi v/\ell\). It still vanishes when \(\ell\to\infty\). This distinguishes the spatial continuum limit from the infinite-volume test required by the [[contemporary-puzzles/yang-mills-mass-gap/clay-contract-and-scale-assumptions|Clay contract]].

## Neutrality does not remove the quadratic diagnostic

For a compact simple group, the quadratic expansion about a flat connection has one copy of this incidence operator per Lie-algebra component. Linearized Gauss removes longitudinal modes; the residual global group rotates the color index in the adjoint representation. A single colored oscillator need not survive a global singlet restriction.

Nevertheless, choose opposite nonzero momenta and one transverse polarization. In the quadratic Fock model, let \(a^\dagger_{k,r,A}\) create that oscillator with color \(A\), in an orthonormal invariant Lie-algebra pairing. Then
\[
\Psi_k=\frac1{\sqrt{\dim G}}
\sum_{A=1}^{\dim G}
a^\dagger_{k,r,A}a^\dagger_{-k,r,A}\Omega
\tag{FG10}
\]
is normalized, transverse, invariant under the global group, and has total momentum zero. Here \(k\ne-k\), as holds for a least momentum at \(L\ge3\). Its excitation energy is
\[
\langle\Psi_k,(H_s-E_0)\Psi_k\rangle=2\omega(k).
\tag{FG11}
\]
The Killing-pairing contraction proves invariance; orthogonality of the different color terms proves the normalization. Thus even the globally neutral quadratic sector has an edge bounded above by \(4\sqrt{e_*b_*}\sin(\pi/L)\), which tends to zero.

This vector is not asserted to satisfy the full nonlinear Gauss constraint or to be a trial vector above the interacting Yang–Mills vacuum. Its role is precise: color neutrality alone cannot repair a certificate that uses only the flat quadratic incidence operator. The vacuum and the comparison of quadratic with full response require their own construction.

## The additional rigidity must act on the full returned state

The exact finite interacting operator supplies its actual vacuum \(\psi_0\). Its centered observable form contains
\[
\mathcal E_{\psi_0}(F)=\sum_e\kappa_e
\int|\nabla_eF|^2\psi_0^2\,d\mu_{\rm Haar}.
\tag{FG12}
\]
[[strong-coupling-gap-and-continuum-crossover/gauge-descent-flux-fisher-coercivity|The gauge-response programme]] owns this ground-state form and its geometric and multiscale comparison options. Its measure is the returned interacting vacuum, not an independently chosen Gibbs weight.

The substantive next conjecture is that a source-compatible non-Abelian preparation law controls (FG12), or an equivalent full physical response, uniformly through the required spatial and coupling limits. The quadratic test tells us where that conjecture must add content: the preparation cannot merely enforce reciprocal scalar coefficients while leaving the physical long-wavelength cost equal to \(d_1^*d_1\).

A successful return must explain why the non-Abelian state and its complete response exclude the sequence of soft physical distinctions, while its Abelian or quadratic control retains the dispersion just calculated. This is a discriminating test for the proposed law, not an assertion that a positive mass can be obtained by adding a constant to the quadratic operator.
