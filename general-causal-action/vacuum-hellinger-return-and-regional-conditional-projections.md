# Vacuum Return Preserves the Regional Conditional Defect

The actual compact planar theory retains a nonzero regional memory on its confinement window. The proof uses the returned vacuum amplitude and the complete evolved source vector to control the regional conditional projection. A fiberwise Hellinger estimate supplies the missing step: it transfers the harmonic one-face semigroup defect to the actual compact conditional kernels. Autocorrelation convergence alone would not justify that conclusion.

**Status: proved one-source regional conditional return and semigroup obstruction.** [[fixed-regional-sources-and-the-compact-vacuum-return|FR]] supplies the actual vacuum and normalized source; [[compact-chronology-on-finite-hermite-sources|HC]] supplies its full-vector chronology. [[inherited-planar-vacuum-and-the-regional-time-law|IR]] supplies the harmonic conditional law. All bounds retain the specified comb connectors, full Gauss carrier and window \(0<hn^{10}\le\eta\), where \(n=L+1\) and \(h=(\kappa/g)^{1/4}\).

## Conditional projection without an inverse-density estimate

Let \(\psi,\Omega\ge0\) be normalized amplitudes in
\(L^2(dx_B\,dx_E)\), and let \(\mathsf E_\psi\) project onto the closed subspace of vectors \(\psi(x_B,x_E)a(x_B)\). With
\(m_\psi(x_B)=\int\psi(x_B,x_E)^2dx_E\),
\[
(\mathsf E_\psi u)(x_B,x_E)
=\frac{\psi(x_B,x_E)}{m_\psi(x_B)}
 \int\psi(x_B,z)u(x_B,z)\,dz,
\tag{VH1}
\]
with zero on fibers where \(m_\psi=0\). Multiplication by \(\psi\) identifies this with conditional expectation in the probability law \(\psi^2dx\). No uniform lower bound on its marginal density is imposed.

Put \(\delta=\|\psi-\Omega\|_2\). For every bounded whole-configuration function \(g\),
\[
\boxed{\| (\mathsf E_\psi-\mathsf E_\Omega)(\Omega g)\|_2
\le\|g\|_\infty\delta.}
\tag{VH2}
\]
To prove it, fix \(x_B\). These are projections onto the two amplitude lines in the exterior fiber. Their difference has norm equal to the sine of their angle. Moreover,
\[
\|\Omega_{x_B}\|^2\sin^2\angle(\psi_{x_B},\Omega_{x_B})
=\operatorname{dist}(\Omega_{x_B},\operatorname{span}\psi_{x_B})^2
\le\|\Omega_{x_B}-\psi_{x_B}\|^2.
\]
Use \(\|\Omega_{x_B}g\|\le\|g\|_\infty\|\Omega_{x_B}\|\) and integrate. The zero-fiber cases satisfy the same inequality.

For \(g\in L^4(\Omega^2dx)\), clip its modulus at \(M\). Since a difference of orthogonal projections has norm at most one,
\[
\| (\mathsf E_\psi-\mathsf E_\Omega)(\Omega g)\|_2
\le M\delta+\frac{\|g\|_4^2}{M}
\le 2\|g\|_4\sqrt\delta
\tag{VH3}
\]
after choosing \(M=\|g\|_4/\sqrt\delta\); the zero cases follow by continuity. This controls a quadratic source without dividing by a small regional probability.

## Use an exact common framed chart

[[comb-face-transport-and-the-first-nonlinear-jet|FJ1–2]] gives comb face variables with product Haar measure globally. Each principal logarithm
\(P_p=\exp(-ihX_p\cdot\sigma/2)\), \(|X_p|<2\pi/h\), misses only the Haar-null antipode. If \(\rho_L(y)dy\) is the complete product Haar density, then
\[
(\mathcal U_hv)(X)
=h^{3L^2/2}\rho_L(hX)^{1/2}v(P(hX))
\quad(X\in D_h),
\qquad D_h=\prod_p B_{2\pi/h}(0),
\tag{VH4}
\]
extended by zero, is an isometry into the full Euclidean \(L^2\) space and unitary onto its supported subspace. It is distinct from CQ's cutoff map: \(\mathcal U_h\mathcal J_hu=\chi_hu\).

Let \(\Phi_h=\mathcal U_h\psi_h\), where \(\psi_h\) is the actual positive vacuum, and let \(\Omega_L\) be the harmonic vacuum. FR's sixth-order construction, actual branch selection and cutoff tails give
\[
\boxed{\|\Phi_h-\Omega_L\|_2\le C\theta,
\qquad \theta=hn^{11/2}.}
\tag{VH5}
\]
For example the actual-to-quasimode error is \(O(nh^7n^{75/2})=O(\theta^7)\), while the polynomial vacuum differs from \(\Omega_L\) by \(O(\theta)\). The global zero extension retains the omitted chart tail.

Retain one face \(p\). Define \(\mathsf E_h=\mathsf E_{\Phi_h}\) and \(\mathsf E_0=\mathsf E_{\Omega_L}\) with regional variable \(X_p\). Both commute with simultaneous color rotations. On invariant vectors their outputs are \(\Phi_h\) or \(\Omega_L\) times a radial function of that one face. Thus their restrictions are the actual conditional projections onto the one-face class-observable algebra. This uses a framed cover before invariants; it imposes no independent regional Gauss quotient or physical Hilbert-space factorization.

## Return the conditional action on the actual source

Use FR's scaled compact observable \(B_h=4|\mathbf q_p|^2/h^2\), its actual mean \(m_h\), variance \(\sigma_h^2\), and normalized regional function
\(f_h=(B_h-m_h)/\sigma_h\). Its flat source vector is
\(z_h=\Phi_hf_h\). Write
\[
c_{p,L}=(\sqrt{A_L})_{pp},\qquad
f_0=\frac{|X_p|^2-3c_{p,L}}{\sqrt6c_{p,L}},\qquad
z_0=\Omega_Lf_0.
\tag{VH6}
\]
Both source vectors have norm one. FR proves \(\|z_h-z_0\|\le C\theta\); in particular the compact normalization is not replaced by its harmonic value.

Let \(\widehat K_h\) be the actual vacuum-subtracted scaled Hamiltonian, \(K_0\) its harmonic counterpart, and
\(\mathsf T_h(t)=\mathcal U_he^{-t\widehat K_h}\mathcal U_h^*\).
HC7 and the source return imply
\[
\sup_{t\ge0}\|\mathsf T_h(t)z_h-e^{-tK_0}z_0\|
\le C\theta.
\tag{VH7}
\]
The harmonic vector is centered and degree two, so HC's full physical gap controls its integrated Duhamel error. The remaining cutoff tail is uniform in time because harmonic evolution preserves that degree.

Write \(e^{-tK_0}z_0=\Omega_Lg_t\). The harmonic ground transform is Markov, so \(\|g_t\|_4\le\|f_0\|_4\), with a universal bound from the normalized three-color Gaussian quadratic. Equations (VH3), (VH5) and (VH7), together with IR's exact conditional calculation, give
\[
\boxed{\sup_{t\ge0}
\|Q_h(t)f_h-r_L(t)f_h\|_{L^2(\pi_{h,p})}
\le C\sqrt\theta,\qquad
r_L(t)=\left[\frac{k_{p,L}(t)}{c_{p,L}}\right]^2,}
\tag{VH8}
\]
where \(k_{p,L}(t)=(\sqrt{A_L}e^{-t\sqrt{A_L}})_{pp}\).
Here \(\pi_{h,p}\) is the actual regional vacuum marginal and \(Q_h(t)\) its actual two-time conditional kernel. In flat amplitude form it is \(\mathsf E_h\mathsf T_h(t)\mathsf E_h\). It is a self-adjoint Markov contraction for each \(t\); no semigroup law has been assumed.

## A genuine compact regional semigroup obstruction

Contractivity and \(0\le r_L(t)\le1\) now yield
\[
\boxed{\sup_{t\ge0}
\left\|(Q_h(2t)-Q_h(t)^2)f_h
-d_L(t)f_h\right\|_{L^2(\pi_{h,p})}
\le C\sqrt\theta,\qquad
d_L(t)=r_L(2t)-r_L(t)^2.}
\tag{VH9}
\]
The two applications of \(Q_h(t)\) cost at most twice the error in (VH8). There is also an exact nonnegative identity:
\[
\langle f_h,(Q_h(2t)-Q_h(t)^2)f_h\rangle
=\|(I-\mathsf E_h)\mathsf T_h(t)z_h\|^2.
\tag{VH10}
\]
It measures information carried outside the retained regional algebra during the actual chronology.

For every nontrivial connected patch, IR's strict frequency-mixture inequality gives \(d_L(t)>0\) at each \(t>0\). Hence at fixed \(L>1,t>0\), sufficiently strong confinement makes the actual regional conditional kernels fail the semigroup law. For a bulk face with distance to the boundary tending to infinity, IR8 gives \(d_L(t)\to d_\infty(t)>0\): the infinite-lattice frequency measure is still nondegenerate. Along \(hn^{10}\le\eta\), \(\theta\le\eta n^{-9/2}\to0\), so the actual defect stays bounded away from zero at each fixed scaled time.

This conclusion uses (VH8), not just the autocorrelation. For example a stationary scalar Ornstein–Uhlenbeck process and a normalized mixture of its first two Hermite observables have
\(C(t)=(e^{-t}+e^{-2t})/2\), hence \(C(2t)>C(t)^2\), although their full transition kernels form a Markov semigroup.

The whole compact chronology remains Markov; its one-face restriction retains exterior memory. This is one conditional source-vector theorem, not operator-norm convergence of the whole regional kernel or convergence of every marked history. Time remains scaled by \(\sqrt{\kappa g}\). The complete mixed histories and lag/source-exchange terms required by [[spatial-block-sewing-and-the-vacuum-cap-response|SB]] and [[oriented-innovation-and-finite-temporal-repair|OI]] remain separate constraints; no uniform Yang–Mills gap follows.
