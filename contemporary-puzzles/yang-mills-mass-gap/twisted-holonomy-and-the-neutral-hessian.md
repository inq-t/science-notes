# Twisted Holonomy and the Neutral Hessian

A global gauge twist can remove zero modes of charged constituents while leaving gauge-invariant local observables in the trivial character sector. On a compact twisted torus this gives a positive neutral two-constituent threshold, but it scales as inverse box size and vanishes in the infinite-volume limit. Center-stabilized Yang--Mills supplies the more instructive two-stage mechanism: holonomy organizes and gaps charged modes, whereas a nonperturbative monopole-induced potential creates the positive Hessian on the remaining neutral modes. The residue-bearing operator is therefore a dynamical Hessian after quotienting gauge zero modes, not the twist character by itself.

**Status: [STANDARD] for one-form center charges, twisted-torus momentum sectors, and the semiclassical deformed-theory mass mechanism; [EXACT] for the equivariant-map and neutral-character obstructions; [OPEN] for a deformation-removal, decompactification, and continuum comparison to ordinary finite-\(N\) Yang--Mills on \(\mathbb R^4\).**

## A center twist does not charge a glueball

The center symmetry of pure \(SU(N)\) Yang--Mills is a one-form symmetry. Its charged observables are Wilson lines, not point-local gauge-invariant fields such as \(\operatorname{Tr}F^2\). Consequently the glueball carrier

\[
\mathcal H_{\mathrm{gl}}
=
\overline{\{(O-\langle O\rangle)\Omega:
O\in\mathcal A_{\mathrm{loc}}^{\mathrm{inv}}\}}
\]

is center-neutral when the vacuum is center invariant. [[library/generalized-global-symmetries/inq]] fixes this categorical degree: the background for a one-form symmetry is a two-form gauge field, while the triangle construction uses an ordinary flat line bundle acting on pointwise sections.

The direct transfer obstruction is elementary. If \(\mathcal K_\chi\) carries a nontrivial center character and

\[
J:\mathcal H_{\mathrm{gl}}\to\mathcal K_\chi
\]

is equivariant, then for a center element \(z\) with \(\chi(z)\ne1\),

\[
J=J U_{\mathrm{gl}}(z)
=U_\chi(z)J
=\chi(z)J,
\]

so \(J=0\). A nontrivial-character line cannot be the direct image of the neutral local carrier.

The same issue appears for constituents. A representation and its conjugate always contain a neutral channel,

\[
\mathbf1\subset R\otimes R^*,
\]

and line phases cancel as \(\chi\bar\chi=1\). Positive constituent energies may survive that cancellation, but only a separate composite or interacting estimate can prove it.

## What a twisted finite box proves

For irreducible 't Hooft twist on a spatial two-torus,

\[
\Gamma_1\Gamma_2
=e^{2\pi i k/N}\Gamma_2\Gamma_1,
\]

adjoint color-momentum is quantized in units

\[
p_{\min}=\frac{2\pi}{NL}.
\]

The single lowest constituent carries nonzero electric flux. In the zero-flux sector, the first perturbative excitation is an opposite-flux pair with

\[
E_{0}^{(0)}
=2p_{\min}
=\frac{4\pi}{NL}.
\]

This is a real gauge-invariant neutral finite-volume threshold, not merely a color-vector eigenvalue. But

\[
\lim_{L\to\infty}E_0^{(0)}=0
\]

at fixed \(N\). [[library/spatial-volume-dependence-for-2-1-dimensional-su-n-yang-mills-theory/inq]] derives the twisted momentum organization, while [[library/the-spectrum-of-2-1-dimensional-yang-mills-theory-on-a-twisted-spatial-torus/inq]] distinguishes the small-volume torelon--antitorelon level from the large-volume glueball. A box gap caused by excluding zero momentum is not the Clay gap.

There is also a topological limit. Center backgrounds lie in \(H^2(M,\mathbb Z_N)\). They can be nontrivial on a torus, but \(H^2(\mathbb R^4,\mathbb Z_N)=0\). Keeping a flux on \(\mathbb R^4\) requires a defect or asymptotic datum and changes the sector being studied.

## The positive two-stage precedent

[[library/center-stabilized-yang-mills-theory-confinement-and-large-n-volume-independence/inq]] studies a double-trace-deformed theory on \(\mathbb R^3\times S^1_L\). A center-symmetric Wilson-line background gives off-diagonal \(W\)-bosons the kinematic scales

\[
m_{W,k}=\frac{2\pi k}{NL}.
\]

The \(N-1\) Cartan photons remain massless to every perturbative order. Monopole-instantons then generate the dual action

\[
S_{\mathrm{dual}}
=
\int_{\mathbb R^3}
\left[
\frac1{2L}\left(\frac g{2\pi}\right)^2
(\nabla\sigma)^2
-\zeta\sum_{i=1}^{N}\cos(\alpha_i\cdot\sigma)
\right].
\]

At a minimum, its Hessian has the cycle-graph form

\[
\delta^2V
=
m_\gamma^2
\sum_{i=1}^{N}(\sigma_{i+1}-\sigma_i)^2,
\]

with physical Fourier masses

\[
m_p=m_\gamma\sin\frac{\pi p}{N},
\qquad
p=1,\ldots,N-1.
\]

The constant \(p=0\) direction is the decoupled overall \(U(1)\), not a physical \(SU(N)\) mode. Thus the neutral physical Hessian is positive.

This precisely separates the roles:

\[
\text{global holonomy}
\longrightarrow
\text{controlled carrier and saddles},
\]

\[
\text{monopole fugacity }\zeta
\longrightarrow
\text{positive neutral Hessian}.
\]

The twist does not do the second job by itself. It makes a nonperturbative residue calculable.

## The remaining firewall

The controlled regime is \(N\Lambda L\ll1\), and the action contains a center-stabilizing deformation. Control is lost near \(N\Lambda L\sim1\). The absence of a known order parameter between regimes supports an adiabatic-continuity conjecture but is not a proof of a uniform gap during deformation removal and \(L\to\infty\).

The strongest reusable target is therefore:

\[
\boxed{
\begin{array}{c}
\text{global descent organizes the gauge-orbit carrier}\
\Downarrow\\
\text{nonperturbative effective form on neutral directions}\
\Downarrow\\
\text{positive Hessian after gauge zero-mode quotient}\
\Downarrow\\
\text{uniform OS/Hamiltonian comparison}.
\end{array}}
\]

[[localized-relative-entropy-and-the-energy-solder]] now supplies a rigorous candidate for the last comparison on localized state tangents. What remains is to derive a neutral descent-loss Hessian whose lower constant survives decompactification, deformation removal, and the asymptotically free continuum limit.

