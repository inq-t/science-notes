# A Local Gauge Completion of the Whole Gaussian Chain

Keeping all intermediate bond fields gives an exact local representation of the accumulated soft Gaussian chain, conditional on its terminal readout. Integrating auxiliary gauge and harmonic coordinates preserves the joint curvature law. Its terminal Schur precision contains the actual accumulated prior and has depth-uniform upper and lower norm bounds. The whole enlarged operator loses coercivity in the unweighted stack norm; the separate terminal-locality theorem bypasses that obstruction without assigning the full stack an artificial gap.

## The enlarged carrier and its law

Use [[soft-gaussian-gauge-blocking|the normalized chain]] at meshes \(b_i=L^ia\), \(i=0,\ldots,k+1\), with \(L\ge2\), \(\eta>0\), and the physical \(L^2\) metrics. Let \(D_i,\mathcal C_i\) be scalar gradient and curl; let \(Q_i,Q_i^0\) be the raw parallel-path and scalar averages from level \(i\) to \(i+1\). Set

$$
E_i=(Q_i^0)^*,\qquad Z_i=I-E_iQ_i^0.
\tag{MC1}
$$

Here \(Z_i\) projects scalar fields onto block-mean-zero fields. It is local; it is neither a Coulomb projection nor the accumulated precision \(P_i\).

Condition on \(X_{k+1}=B\in H_{k+1}\). Instead of using only harmonic-free Coulomb fields \(X_i\), integrate over all bond coordinates \(A_0,\ldots,A_k\) with density proportional to \(\exp[-\mathcal E_B/2]\), where

$$
\begin{aligned}
\mathcal E_B(A)
={}&\|\mathcal C_0A_0\|_{b_0}^2
+\sum_{i=1}^{k}\frac{\|A_i-Q_{i-1}A_{i-1}\|_{b_i}^2}{\eta b_i^2}\\
&+\frac{\|B-Q_kA_k\|_{b_{k+1}}^2}{\eta b_{k+1}^2}
+\sum_{i=0}^k\alpha_i\|Z_iD_i^*A_i\|_{b_i}^2,
\qquad\alpha_i>0.
\end{aligned}
\tag{MC2}
$$

Its precision \(\mathbb L_k\) is block tridiagonal in the level index. Each block has bounded spatial range at the corresponding block scale. The extra fields are coordinates of an equivalent Gaussian presentation, not additional physical matter.

## Why all gauge dimensions fit

Write a gauge orbit as \(A_i+D_i\phi_i\), with scalar \(\phi_i\) modulo global constants. Define independent relative gauge coordinates

$$
u_i=\phi_i-Q_{i-1}^0\phi_{i-1}\quad(1\le i\le k),
\qquad u_{k+1}=-Q_k^0\phi_k,
\tag{MC3}
$$

and

$$
z_i=Z_iD_i^*(A_i+D_i\phi_i),\quad0\le i\le k.
\tag{MC4}
$$

If \(s_i\) is the dimension of the scalar space modulo constants, their total dimension is
\(\sum_{i=1}^{k+1}s_i+\sum_{i=0}^k(s_i-s_{i+1})=\sum_{i=0}^ks_i\).
The coordinate map is an affine bijection, not merely a dimension count. Solve backward: \(u_{k+1}\) prescribes \(Q_k^0\phi_k\), and \(z_k\) determines its remaining block-zero part through
\(Z_kD_k^*D_kZ_k\). Continue with
\(Q_{i-1}^0\phi_{i-1}=\phi_i-u_i\).
The required restricted scalar Laplacian obeys

$$
Z_iD_i^*D_iZ_i\ge\frac4{b_{i+1}^2}I
\quad\hbox{on }\ker Q_i^0,
\tag{MC5}
$$

by the cell Poincare estimate of [[local-completion-of-soft-gauge-conditioning|the one-step theorem]]. The Jacobian is field-independent.

The \(i\)-th readout mismatch changes by \(D_i u_i\); the last changes by \(D_{k+1}u_{k+1}\). The gauge penalties become \(\alpha_i\|z_i\|^2\). Integrating \(z_i\), then the independent \(u_i\), projects each mismatch orthogonally off gradients. All resulting determinants are field-independent and cancel in normalized expectations.

Harmonic one-forms require one further step. They are not scalar gauge directions. Mean preservation separates them into a Gaussian chain anchored by the terminal readout. Integrating that chain rather than fixing all harmonics to zero does not affect any \(\mathcal C_iA_i\). Consequently every integrable joint curvature observable satisfies

$$
\boxed{
\mathbb E_{\mathcal E_B}
f(\mathcal C_0A_0,\ldots,\mathcal C_kA_k)
=
\mathbb E\!\left[
f(\mathcal C_0X_0,\ldots,\mathcal C_kX_k)
\mid X_{k+1}=B\right].}
\tag{MC6}
$$

The unprojected Gaussian is normalized at every finite depth and volume. In the homogeneous form \(\mathcal E_0\), zero energy forces a flat chain; its terminal readout kills the harmonic component, and (MC3)--(MC5) kill the remaining gauge motion backward through the levels. Thus its Hessian \(\mathbb L_k>0\), independently of \(B\). This statement alone contains no uniform lower constant.

## The terminal Schur operator is the actual one

Integrate levels \(0,\ldots,k-1\), retaining all of \(A_k\). Those earlier levels are exactly the preceding completed chain with terminal value \(A_k\). Their integral is a constant times
\(\exp[-\langle A_k,\widehat P_kA_k\rangle/2]\), where \(\widehat P_k\) extends the actual precision \(P_k=\operatorname{Cov}(X_k)^{-1}\) by zero on gradients and harmonics.

The extension is flat in harmonic directions because integrating a free initial harmonic chain with prescribed endpoint produces a constant independent of that endpoint. The centered prior supplies no new linear source. Therefore the terminal Schur precision and source are exactly

$$
\boxed{
S_k=\widehat P_k+\alpha_kD_kZ_kD_k^*
+\frac{Q_k^*Q_k}{\eta b_{k+1}^2},
\qquad j_B=\frac{Q_k^*B}{\eta b_{k+1}^2}.}
\tag{MC7}
$$

No fresh Maxwell action has been substituted for the accumulated law.

Let \(\Gamma=1+4d\eta/(1-L^{-2})\), so
\(\widehat P_k\ge\Gamma^{-1}\mathcal C_k^*\mathcal C_k\) by (SG6). Let \(A_1,A_2\) be the one-step full-carrier constants in (LC13), evaluated at \(n=L\). That estimate gives

$$
S_k\ge\frac{\beta_*}{b_{k+1}^2}I,\qquad
\beta_*=\min\left\{
\frac1{\Gamma A_1},\frac1{\eta A_2},\frac{4\alpha_k}{3}
\right\}>0.
\tag{MC8}
$$

For \(k\ge1\), the latest injected noise yields
\(P_k\le(\eta b_k^2)^{-1}I_{H_k}\). Hence

$$
S_k\le\frac{L^2(\eta^{-1}+4d\alpha_k)+\eta^{-1}}
{b_{k+1}^2}I.
\tag{MC9}
$$

With \(\alpha_k\) fixed positive, both bounds are depth- and volume-uniform. The \(k=0\) upper bound is (LC14). These are estimates relative to the terminal physical bond metric, not arbitrary coordinate eigenvalues; [[hessian-response-geometry/relative-response-spectrum|the relative-response spectrum]] explains that distinction.

## Why a local enlarged law is not yet a uniform localization theorem

Set \(B=0\) and \(A_i=h\) for one spatially constant nonzero bond field on every mesh. The physical volume is common to all levels. All curls, gauge penalties, and intermediate mismatches vanish, while

$$
\mathcal E_0(h,\ldots,h)=\frac{\|h\|^2}{\eta b_{k+1}^2},
\qquad
\sum_{i=0}^k\|h\|^2=(k+1)\|h\|^2.
\tag{MC10}
$$

Thus the smallest eigenvalue of \(\mathbb L_k\) in the unweighted product norm is at most \(1/[\eta(k+1)b_{k+1}^2]\). These duplicated auxiliary harmonic coordinates do not contradict (MC8), which concerns a different, terminal carrier. They do invalidate a depth-uniform finite-range inverse argument based on that full-stack norm.

Conversely, \(S_k\) is uniformly bounded above and below but need not have finite range: elimination puts the accumulated \(\widehat P_k\) into it. Its norm bounds cannot be inserted into the one-step finite-range proof without controlling those coefficients or a weighted terminal response.

[[accumulated-readout-noise|The exact accumulated-noise formula]] isolates a nearest-neighbor unprojected noise covariance. [[uniform-gaussian-conditional-locality|The terminal-locality theorem]] additionally controls the inherited Maxwell term and transverse inversion in a common holomorphic strip, then applies weighted inversion directly to \(S_k\). Thus the Gaussian spatial estimate no longer depends on uniform full-stack coercivity. Averaging these conditional laws over the actual terminal-readout distribution returns the original massless fine marginal; fixing a readout does change that marginal. Neither a conditional floor nor gauge completion has generated a physical mass, selected a dimensional yardstick, or solved the non-Abelian infrared problem.
