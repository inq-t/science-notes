# Predictive Rank and Physical Separation

A Gaussian pair admits an exact sufficient interface determined by the mixed precision matrix. Its response depends on normalized coupling strength, not on the number of retained coordinates. Exact compression nevertheless preserves the chosen carrier: an entire slab interior has a response floor that closes under refinement even when the fixed-distance midpoint response stays positive.

**Status: [EXACT FINITE-DIMENSIONAL GAUSSIAN CALIBRATIONS]; [OPEN] for their interacting gauge realization.** Precision matrices are positive definite. Gauge null directions require a separately justified quotient before applying these formulas.

## The mixed precision selects the interface

Let the centered Gaussian pair \((Y,Z)\) have precision
\[
\mathsf Q=\begin{pmatrix}A&C\\C^{\mathsf T}&D\end{pmatrix}>0,\qquad
\mathsf T=A^{-1/2}CD^{-1/2}.
\tag{GP1}
\]
Whitening with the conditional precisions and taking the singular value decomposition of \(\mathsf T\) gives independent paired precision blocks
\[
\begin{pmatrix}1&s_i\\s_i&1\end{pmatrix},\qquad 0<s_i<1,
\]
plus uncoupled coordinates. Their ordinary correlations are \(-s_i\). The complete Hermite expansion and product argument in [[inq|the Gaussian bridge calibration]] give
\[
\boxed{\kappa=1-\|\mathsf T\|^2.}
\tag{GP2}
\]
This is a complete observable statement, not merely the minimum among linear tests.

The statistics
\[
X=C^{\mathsf T}Y,\qquad W=CZ
\tag{GP3}
\]
are sufficient in both directions. Their actual supports have linear dimension \(\operatorname{rank}C\), and [[bridge-data-augmentation-solder/predictive-sufficient-interfaces|the response reduction]] is \(B\simeq B_{X,W}\oplus I\).

Any sufficient core statistic must determine
\(\mathbb E[Z\mid Y]=-D^{-1}C^{\mathsf T}Y\). This proves minimality of the predictive sigma algebra and identifies the minimal linear coordinates. It does not prove minimal dimension among arbitrary measurable encodings. Nor is \(K\) finite rank merely because \(C\) has finite rank: a single correlated Gaussian coordinate already has infinitely many nonzero Hermite modes.

## The identifiable Fisher quotient is sharp

In the paired coordinates, \(Y_i\mid Z_i=z_i\sim N(-s_i z_i,1)\). The boundary Fisher tensor is \(\operatorname{diag}(s_i^2)\), and the actual boundary marginal variances are \((1-s_i^2)^{-1}\). On this identifiable quotient,
\[
\lambda_F=\min_i\frac{1-s_i^2}{s_i^2},
\qquad
\boxed{\frac{\lambda_F}{1+\lambda_F}=1-\|\mathsf T\|^2.}
\tag{GP4}
\]
Thus [[conditional-fisher-coercivity/inq|conditional Fisher coercivity]] is exact in every finite dimension here, without summing a loss per coordinate. When \(C=0\), the pair is independent and \(\kappa=1\); there is no nontrivial identifiable Fisher quotient to invert.

## Small collar coupling need not mean small predictive rank

Let \(Y,H,Z\in\mathbb R^n\), and choose
\[
\mathsf Q_\varepsilon=
\begin{pmatrix}
I&\varepsilon I&0\\
\varepsilon I&I&\varepsilon I\\
0&\varepsilon I&I
\end{pmatrix},\qquad 0<\varepsilon<1/\sqrt2.
\tag{GP5}
\]
Integrating \(H\) gives the Schur complement
\[
A_{\rm eff}=D_{\rm eff}=(1-\varepsilon^2)I,\qquad
C_{\rm eff}=-\varepsilon^2I.
\tag{GP6}
\]
The mixed norm can be arbitrarily small, but the exact predictive rank remains \(n\). The full response is
\[
\kappa=1-\frac{\varepsilon^4}{(1-\varepsilon^2)^2}.
\tag{GP7}
\]
Conversely, with no direct \(Y,Z\) interaction and a genuinely \(h\)-dimensional hidden separator,
\[
C_{\rm eff}=-Q_{YH}Q_{HH}^{-1}Q_{HZ},
\qquad \operatorname{rank}C_{\rm eff}\le h.
\]
A rank bottleneck is additional structural information; [[collared-quasi-factorization-and-surface-response/fisher-collar-bound-for-wilson-laws|a collar norm estimate]] does not supply it.

## A whole-interior floor can close in a gapped model

Use the stationary Gaussian Markov process of [[inq|the parent calibration]],
\(\mathbb E[X_sX_t]=e^{-\omega|s-t|}\), with \(\omega>0\). Fix endpoints \(Z=(X_{-\ell},X_\ell)\). Let \(a=\ell/N\), \(N\ge2\), and let \(Y_a\) contain every interior lattice sample between them.

The adjacent interior pair
\[
T_a=(X_{-\ell+a},X_{\ell-a})
\]
is sufficient for predicting the endpoint pair from the whole interior. Put \(t=e^{-\omega a}\) and \(r=e^{-2\omega(\ell-a)}\). Its covariance matrices are
\[
\Sigma_T=\begin{pmatrix}1&r\\r&1\end{pmatrix},\quad
\Sigma_Z=\begin{pmatrix}1&t^2r\\t^2r&1\end{pmatrix},\quad
\Sigma_{TZ}=t\begin{pmatrix}1&r\\r&1\end{pmatrix}.
\tag{GP8}
\]
The symmetric and antisymmetric canonical correlations squared are
\[
\rho_\pm^2=\frac{t^2(1\pm r)}{1\pm t^2r}.
\]
The plus channel is maximal. Exact sufficiency therefore gives the complete all-interior floor
\[
\boxed{
\kappa_{\rm all}(a,\ell)=
\frac{1-e^{-2\omega a}}{1+e^{-2\omega\ell}}
\longrightarrow0\quad(a\downarrow0).}
\tag{GP9}
\]
Yet for the midpoint \(X_0\) and the same endpoints,
\[
\boxed{\kappa_{\rm mid}(\ell)=\tanh(\omega\ell)>0.}
\tag{GP10}
\]
The time-transfer spectrum has not changed. The all-interior carrier permits distinctions arbitrarily close to an observed endpoint, so it demands an increasingly strong prediction obstruction. Restricting a positive complete all-interior bound to the midpoint is legitimate; failure of a uniform all-interior bound does not imply midpoint gaplessness.

This identifies an avoidable strengthening in a proposed continuum proof. A cross-plaquette interface for the whole slab can be exact and still be the wrong object on which to demand a fixed positive floor. Preserve the specified physical separation before judging whether an interface reduction advances the mass-gap estimate.

[[bridge-data-augmentation-solder/receipts/predictive_interface_receipt.py|The receipt]] checks full Gaussian covariance matrices, exact rank reductions, Schur complements, and (GP9)--(GP10) independently of the formulas' symbolic derivation.
