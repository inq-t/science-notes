# Compact Regional Sources Retain the Inherited Chronology

Fixed local quadratic sources in the actual compact planar vacuum return to the harmonic history inherited from the whole patch. Their mixed normalized covariance has an error uniform over all scaled times, and their reduced-resolvent susceptibility has a separate quantitative bound. In the bulk limit, finite local susceptibilities coexist with a vanishing full scaled gap. The regional response therefore cannot be inferred from an independently prepared block or used by itself as a complete-source gap bound.

**Status: proved return for each fixed finite profile family on the stated confinement window.** [[fixed-regional-sources-and-the-compact-vacuum-return|The regional source theorem]] supplies the actual vacuum, means and variances. [[compact-chronology-on-finite-hermite-sources|The chronology estimate]] supplies the generator comparison. [[inherited-planar-vacuum-and-the-regional-time-law|IR]] owns the inherited harmonic law. All sources use the same comb connectors and the complete simultaneous Gauss carrier.

## Fix the regional marks before taking the limit

Take finitely many nonzero real finitely supported profiles \(b_1,\ldots,b_r\), translated together into the open \(L\times L\) face patch. Their shapes, coefficients and relative placements remain fixed. Put
\[
n=L+1,\qquad h=(\kappa/g)^{1/4},\qquad
E=\sqrt{\kappa g},\qquad
0<\epsilon=hn^{10}\le\eta,\qquad
\theta=hn^{11/2}.
\tag{RC1}
\]
Let \(\psi_h\) be the actual normalized vacuum,
\(K_h=H_{L,g}/E-\widehat E_0\), and define
\[
B_{i,h}=\frac4{h^2}\left|\sum_p b_i(p)\mathbf q_p\right|^2,\quad
m_{i,h}=\langle\psi_h,B_{i,h}\psi_h\rangle,\quad
\sigma_{i,h}=\|(B_{i,h}-m_{i,h})\psi_h\|,\quad
\zeta_{i,h}=\frac{(B_{i,h}-m_{i,h})\psi_h}{\sigma_{i,h}}.
\tag{RC2}
\]
The common multiplier \(4/h^2\) cancels from normalized responses. The actual centered covariance and scaled susceptibility matrices are
\[
\Gamma^h_{ij}(t)=\langle\zeta_{i,h},e^{-tK_h}\zeta_{j,h}\rangle,\qquad
\Sigma^h_{ij}=\langle\zeta_{i,h},K_h^{-1}\zeta_{j,h}\rangle.
\tag{RC3}
\]
The inverse acts on the actual vacuum complement. No invertibility of the finite source covariance matrix is assumed.

Write \(A_L=4I-\operatorname{Adj}_L\), \(C_L=A_L^{1/2}\), and let \(\Omega_L\) be the oscillator vacuum. With \(c_{i,L}=b_i^{\mathsf T}C_Lb_i\),
\[
\zeta_{i,0}=
\frac{|b_i^{\mathsf T}X|^2-3c_{i,L}}{\sqrt6\,c_{i,L}}\Omega_L,\qquad
k_{ij,L}(t)=b_i^{\mathsf T}C_Le^{-tC_L}b_j.
\]
These are centered invariant vectors of Hermite degree two. Their exact harmonic responses are
\[
\Gamma^0_{ij,L}(t)=
\frac{k_{ij,L}(t)^2}{c_{i,L}c_{j,L}},\qquad
\Sigma^0_{ij,L}=\int_0^\infty\Gamma^0_{ij,L}(t)\,dt.
\tag{RC4}
\]
The fixed-profile energy bound gives \(c_{i,L}\ge c_i>0\), independently of placement and size. This replaces the shrinking variance of the lowest-mode profile used in the earlier marked-well test.

## The actual covariance returns uniformly in time

For sufficiently small size-independent \(\eta\), there is a constant depending on the fixed profile family but not on \(L,h,t\), such that
\[
\boxed{
\sup_{t\ge0}|\Gamma^h_{ij}(t)-\Gamma^0_{ij,L}(t)|
\le C\theta,\qquad
|\Sigma^h_{ij}-\Sigma^0_{ij,L}|\le Cn\theta.}
\tag{RC5}
\]
Use CQ's cutoff embedding \(\mathcal J_h\). The source theorem gives
\[
\|\zeta_{i,h}-\mathcal J_h\zeta_{i,0}\|\le C\theta.
\]
On a centered physical vector \(u\) of fixed Hermite degree, the chronology theorem gives
\[
\sup_{t\ge0}
\|e^{-tK_h}\mathcal J_hu-\mathcal J_he^{-tK_0}u\|
\le C\theta\|u\|,\qquad K_0=V_0-e_0.
\tag{RC6}
\]
Its Duhamel integral uses the harmonic decay \(e^{-c_Lt}\), with \(c_L\ge8/n\). It does not identify the full two operators in norm. Their cutoff inner products differ by \(O((hn^{3/2})^4)\) on these vectors. Contractivity and subtraction now give the covariance bound in (RC5), including both actual source normalizations.

## A Poisson residual controls the integrated response

Uniform absolute covariance error cannot be integrated over an infinite interval. Instead set \(y_{j,0}=K_0^{-1}\zeta_{j,0}\). Harmonic degree is preserved, and
\[
\|y_{j,0}\|\le Cn,\qquad K_0y_{j,0}=\zeta_{j,0}.
\]
The chronology theorem's actual generator defect is
\[
\|(K_h\mathcal J_h-\mathcal J_hK_0)u\|
\le Chn^{9/2}\|u\|.
\]
Applying it to \(y_{j,0}\), then retaining the actual source difference, gives
\[
\boxed{
\|K_h\mathcal J_hy_{j,0}-\zeta_{j,h}\|\le C\theta.}
\tag{RC7}
\]
UP supplies \(\|K_h^{-1}\|\le Cn\) on the physical vacuum complement. For its projection \(Q_h\),
\[
Q_h\mathcal J_hy_{j,0}-K_h^{-1}\zeta_{j,h}
=K_h^{-1}(K_h\mathcal J_hy_{j,0}-\zeta_{j,h}),
\]
so this vector error is \(O(n\theta)\). Pairing with the actual centered left source removes the vacuum component. Its own \(O(\theta)\) source error costs at most \(Cn\), and the cutoff inner-product error is smaller. This proves the susceptibility part of (RC5). The argument retains the whole Poisson vector; it does not replace susceptibility by the inverse first gap.

## The bulk limit keeps the full local response

Let the distance from the translated profile supports to the outer boundary tend to infinity. IR's functional calculus gives the limiting \(k_{ij,\infty}(t)\) and \(c_{i,\infty}>0\). On compact time intervals, convergence is uniform because \(|\partial_t k_{ij,L}|\le8\|b_i\|_2\|b_j\|_2\). For the remaining times,
\[
|k_{ij,L}(t)|\le
\frac{\|b_i\|_2\|b_j\|_2}{et},\qquad t>0,
\tag{RC8}
\]
follows from \(\sup_{\omega\ge0}\omega e^{-t\omega}=1/(et)\).
The positive lower bounds on \(c_{i,L}\) make the corresponding quadratic tails \(O(t^{-2})\), uniformly in \(L\).

Consequently the harmonic susceptibilities converge by dominated convergence. Alternatively their double spectral integral uses the continuous kernel
\(\sqrt\lambda\sqrt\mu/(\sqrt\lambda+\sqrt\mu)\), extended by zero at the origin, on \([0,8]^2\). For every sequence \(0<\epsilon_L\le\eta\), (RC5) then proves
\[
\boxed{
\sup_{t\ge0}|\Gamma^h_{ij}(t)-\Gamma^\infty_{ij}(t)|\longrightarrow0,\qquad
\Sigma^h_{ij}\longrightarrow\Sigma^\infty_{ij}.}
\tag{RC9}
\]
The compact-to-harmonic errors are respectively \(O(\epsilon_Ln^{-9/2})\) and \(O(\epsilon_Ln^{-7/2})\). No estimate uniform in a growing inventory of profiles is asserted.

For one profile with \(\sum_pb_p\ne0\), the limiting normalized covariance has the \(t^{-6}\) tail of IR9, and its susceptibility is finite. The actual full scaled gap nevertheless tends to zero by UN. The lowest-mode source that detects its inverse is spread over the growing patch and is outside the fixed-profile hypothesis.

The power law is a property of the limiting response; (RC9) is an absolute error statement and does not identify relative late-time tails at finite \(L,h\). Time remains scaled: physical duration is \(t/E\), and the physical normalized susceptibility is \(\Sigma^h/E\). No fixed-coupling thermodynamic limit or four-dimensional mass-gap theorem follows.

Covariance alone does not determine a regional Markov kernel. [[vacuum-hellinger-return-and-regional-conditional-projections|The conditional-projection theorem]] supplies the additional operator comparison that tests actual regional memory. Both tests retain the inherited whole vacuum, rather than prepare an independent block.
