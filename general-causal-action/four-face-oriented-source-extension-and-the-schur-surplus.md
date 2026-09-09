# Oriented Source Extension Removes the Apparent Surplus Gain

Adding two fixed oriented cubic observables to the four-face quadratic source carrier removes its leading positive leakage contribution. The Schur pencil subtracts exactly the two escaped spectral weights, and the optimal extended OI quotient follows the negative physical-gap correction at every fixed positive scaled duration. This is a concrete source-extension computation in the same compact theory. Generalized eigenvalue roots and inertia carry the invariant content; raw eigenvalues of an unnormalized Schur matrix do not.

**Status: proved first nonlinear source-extension response on the fixed four-face patch.** [[four-face-gap-shift-and-the-complete-source-response|FF]] supplies the actual gap and leakage coefficients, [[four-face-cubic-response-and-source-leakage|FC]] supplies the two escaped vectors, and [[four-face-oriented-source-and-the-gap-following-probe|OS]] supplies the fixed compact marks and their spectral estimate. [[four-face-optimal-quadratic-response-and-parity|OQ]] identifies the optimal quadratic correction. The old diagonal-to-quadratic extension and the further cubic extension are distinct source enlargements. All use the full Gauss carrier, common comb connectors, actual vacuum and unchanged time convention.

## The physical test is a generalized Gram pencil

Fix a scaled duration \(t>0\), let \(K_h\) be the actual vacuum-subtracted scaled Hamiltonian, and put \(R_h=I-e^{-2tK_h}\). For an independent finite set of actual centered source vectors \(z_{i,h}\), define
\[
G_{ij,h}=\langle z_{i,h},R_hz_{j,h}\rangle,\qquad
N_{ij,h}=\langle z_{i,h},R_h^2z_{j,h}\rangle,\qquad
Q_h(\lambda)=N_h-\lambda G_h.
\tag{OE1}
\]
At fixed sufficiently small \(h\), \(G_h>0\). The least source quotient is the lowest generalized eigenvalue of \((N_h,G_h)\). Individual source normalization is optional if both matrices are transformed together. No orthogonality of the source vectors is presumed.

For an old/new coefficient split, write
\[
Q=\begin{pmatrix}A&B\\B^*&D\end{pmatrix},\qquad
\mathcal S=D-B^*A^{-1}B,\qquad
\mathcal J_\lambda=\binom{-A^{-1}B}{I}.
\]
Whenever the old block \(A>0\),
\[
\boxed{
\operatorname{inertia}(Q)
=\operatorname{inertia}(A)+\operatorname{inertia}(\mathcal S),\qquad
Q\ge0\ \Longleftrightarrow\ \mathcal S\ge0.}
\tag{OE2}
\]
Completing the old coefficient square proves the identity. In particular a fixed threshold \(\gamma\) below the old quotient minimum tests source extension exactly through \(\mathcal S_h(\gamma)\).

The dependence on the test threshold has an important normalization:
\[
\boxed{
\partial_\lambda\mathcal S_h(\lambda)
=-\mathcal J_\lambda^*G_h\mathcal J_\lambda<0.}
\tag{OE3}
\]
Indeed \(Q\mathcal J_\lambda=(0,\mathcal S)^{\mathsf T}\), while the derivative of \(\mathcal J_\lambda\) has zero new component. Differentiating \(\mathcal S=\mathcal J_\lambda^*Q\mathcal J_\lambda\) therefore leaves only \(-\mathcal J_\lambda^*G_h\mathcal J_\lambda\). This remains the derivative whenever the eliminated block is invertible.

For example, if \(Q_h=Q_0+h^2Q_2+o(h^2)\) in a fixed source basis, then at fixed \(\lambda\)
\[
\mathcal S_2=
D_2-B_2^*A_0^{-1}B_0-B_0^*A_0^{-1}B_2
+B_0^*A_0^{-1}A_2A_0^{-1}B_0
=\mathcal J_0^*(N_2-\lambda G_2)\mathcal J_0.
\]
At a simple root \(\lambda_0\), with \(\mathcal S_0(\lambda_0)y=0\),
\[
\boxed{
\lambda_2=
\frac{y^*\mathcal S_2(\lambda_0)y}
     {y^*\mathcal J_0^*G_0\mathcal J_0y}.}
\tag{OE4}
\]
The denominator is part of the root shift. A fixed-threshold coefficient at \(\gamma\ne\lambda_0\) instead contains \(N_2-\gamma G_2\), the old-source response and the elimination terms displayed above.

## Two actual cubic marks supply the missing source directions

Use FF's fixed four-face normal modes and write
\[
c=2\sqrt2,\qquad
d=-\frac5{32}+\frac{3\sqrt2}{56}-\frac{5\sqrt3}{48}<0,
\qquad
c_h=c+h^2d+O(h^4).
\]
Here \(c_h\) is the actual physical gap divided by \(\sqrt{\kappa g}\). Let
\[
\mathcal B=|\mathbf Q_0|^2,\qquad
\mathcal T_1=\mathbf Q_0\cdot(\mathbf Q_1\times\mathbf Q_2),\qquad
\mathcal T_2=\mathbf Q_0\cdot(\mathbf Q_1\times\mathbf Q_3).
\tag{OE5}
\]
These are fixed bounded real invariant multiplication sources, with no dependence on \(h\), the vacuum or a spectral projector. Consider the span of all ten symmetric quadratic kernels together with \(\mathcal T_1,\mathcal T_2\), centering in the same actual vacuum.

The normalized leading vectors of the cubic sources are
\[
e_1=\frac{T_{012}\Omega}{\sqrt{24\sqrt2}},\qquad
e_2=\frac{T_{013}\Omega}{\sqrt{24\sqrt3}},
\]
of excitation energies
\[
\nu_1=4+\sqrt2,\qquad \nu_2=2+\sqrt2+\sqrt6.
\]
If \(z_{0,h}\) is the actual normalized source vector of \(\mathcal B\), and \(\phi_h\) is the normalized actual first excitation, FC gives in the common chart
\[
z_{0,h}=\phi_h+h\ell+O(h^2),\qquad
\ell=a_1e_1+a_2e_2,
\]
\[
\boxed{
a_1^2=w_1=\frac{2\sqrt2}{49},\qquad
a_2^2=w_2=\frac{\sqrt3}{2},\qquad a_i>0.}
\tag{OE6}
\]
The actual centered cubic source vectors satisfy \(z_{i,h}=e_i+O(h)\). The fixed smooth-source expansion of [[compact-source-normalization-and-the-nonlinear-return|CS]] applies after scaling each cubic by \(8/h^3\): its leading Gaussian variance is positive, and arbitrarily accurate vacuum quasimodes control multiplication by this rescaled observable. Their first corrections need not be discarded or specified to compute the following order.

## The Schur subtraction cancels the leakage exactly

Put
\[
r_\alpha=1-e^{-2t\alpha},\qquad
\lambda_0=r_c,\qquad
\mathcal A_i=r_{\nu_i}(r_{\nu_i}-r_c)>0.
\]
At this harmonic root the cubic block of the pencil is
\(\operatorname{diag}(\mathcal A_1,\mathcal A_2)\).
The root-to-cubic entries have the actual expansion
\[
\boxed{Q_{0i,h}(\lambda_0)=h\,a_i\mathcal A_i+O(h^2).}
\tag{OE7}
\]
To verify it, the operator represented by the pencil is
\(R_h(R_h-\lambda_0)\). Its eigenvalue on \(\phi_h\) is \(O(h^2)\), because \(r_{c_h}-r_c=O(h^2)\). Substituting (OE6) therefore leaves at first order only
\(h\langle\ell,R_0(R_0-r_c)e_i\rangle=h a_i\mathcal A_i\).
An \(O(h)\) change in the cubic source cannot contribute at this order through the harmonic root vector, on which the leading pencil vanishes.

FF11 supplies the original fixed-quadratic quotient:
\[
\mathfrak q_t(z_{0,h})
=r_c+h^2q_2(t)+o(h^2),\qquad
q_2(t)=2td\,e^{-2tc}
+\sum_{i=1}^2 w_i\frac{\mathcal A_i}{r_c}.
\tag{OE8}
\]
Since \(G_{00,0}=r_c\), its unnormalized pencil entry is
\[
Q_{00,h}(\lambda_0)
=h^2\left[r_c\,2td\,e^{-2tc}
+\sum_iw_i\mathcal A_i\right]+o(h^2).
\]
Eliminating the positive cubic block subtracts
\[
h^2(a_i\mathcal A_i)_i^*
\operatorname{diag}(\mathcal A_i^{-1})
(a_i\mathcal A_i)_i
=h^2\sum_iw_i\mathcal A_i .
\tag{OE9}
\]
Thus both escaped weights cancel, with their actual spectral denominators.

At the harmonic minimum, all other quadratic directions form a positive complementary pencil block. The mixed quadratic Gram matrices have zero first-order coefficient by graded parity: both source seeds are even, whereas the first operator and vacuum corrections are odd. Their couplings to the root begin at order \(h^2\). Their elimination therefore does not change (OE9) at second order, even though their first-order couplings to the cubic sector may be nonzero.

For a trial root \(\lambda=r_c+h^2\lambda_2\), the remaining scalar Schur entry is consequently
\[
h^2r_c\bigl(2td\,e^{-2tc}-\lambda_2\bigr)+o(h^2).
\]
Its threshold derivative at the harmonic root is \(-r_c\). Hence
\[
\boxed{\lambda_2^{\rm extended}(t)=2td\,e^{-2tc}<0,\qquad t>0.}
\tag{OE10}
\]
The calculation concerns the generalized eigenvalue root, rather than an eigenvalue of a raw Schur matrix.

## A fixed observable independently attains the root to this order

OS constructs the fixed compact observable
\[
\boxed{\mathcal B^\sharp=\mathcal B-\frac27\mathcal T_1-\mathcal T_2.}
\tag{OE11}
\]
Its normalized source vector has escaped weight \(O(h^4)\) outside the actual first excitation. It lies in the extended finite source span at every \(h\). The induced cubic coefficients in a normalized-source basis are \(-ha_i+O(h^2)\), exactly the first-order minimizing coefficients in (OE9). The \(h\) factors arise from the different variances of quadratic and cubic marks; the physical coefficients \(2/7\) and \(1\) remain fixed.

For any actual centered source, spectral positivity gives
\(\mathfrak q_t\ge1-e^{-2tc_h}\). OS's source gives the reverse upper estimate to order \(h^4\). If \(\lambda_{\rm ext}(h,t)\) is the minimum over all quadratic sources and these two cubic marks, then
\[
\boxed{
1-e^{-2tc_h}
\le\lambda_{\rm ext}(h,t)
\le1-e^{-2tc_h}+O_t(h^4).}
\tag{OE12}
\]
This proves the expansion in (OE10) independently of a choice of source coordinates. It also shows that no other direction in this finite extension can lower the coefficient further. The remainder is for fixed positive scaled duration, or uniformly on compact duration intervals inside \((0,\infty)\).

## What a fixed-threshold Schur coefficient can establish

For [[four-face-diagonal-sources-and-the-relational-schur-defect|the original diagonal-to-full-quadratic extension]], a threshold strictly between their harmonic minima gives a positive old block and an explicit negative Schur direction. Equations (OE2)–(OE4) specify its correct continuation. The present cubic calculation is a further source enlargement; it does not compute the entire fixed-threshold second-order matrix for that earlier split.

Once a source basis and threshold are fixed, its Schur coefficient is a definite algebraic quantity. Its raw spectrum, however, has no independent physical energy normalization. Even the harmless change of new coordinates \(y=(1+ah^2)\widetilde y\) changes
\(\mathcal S_2\) to \(\mathcal S_2+2a\mathcal S_0\), while preserving every root and inertia. At a simple root the extra term vanishes on the null vector, and (OE4) remains invariant. At a threshold away from a root, the derivative of the corresponding source quotient additionally differentiates its \(G_h\) norm.

The useful invariant result here is therefore the root shift and its explicit fixed-source realization: the positive leakage term available within the quadratic readout is removed by two admitted oriented directions, leaving the negative gap coefficient. This is not a retuning of the Hamiltonian or clock, and it proves no positive reinforcement under source extension. [[four-face-oriented-normal-form-and-the-universal-source-lift|One normal-form operator]] now produces all quadratic lifts. [[four-face-source-products-and-the-oriented-contact|Their product contact]] and [[oriented-source-products-and-the-compact-contact-return|its compact realization]] determine the additional information needed for composites. Complete-source, spatial-assembly and continuum bounds remain separate obligations.
