# Joint Fisher Response of Normalized Gauge Blocking

A normalized gauge readout determines two distinct conditional score tensors, one in each direction. The forward tensor and the fine marginal Poincare inequality already bound the complete prediction defect in both directions, because the two prediction maps are adjoints. A separate reverse-conditional estimate controls posterior geometry and the curvature of the actual coarse marginal. These are quantitative statements about one joint gauge law, not a physical mass gap inferred from a smoothed coarse distribution.

**Status: [EXACT FINITE-CARRIER IDENTITIES AND CONDITIONAL BOUNDS]; [EXPLICIT STRONG-COUPLING APPLICATION]; [OPEN] for continuum transport and physical reconstruction.**

## The whole path-incidence operator

Use the \(SU(r)\) metrics, Wilson fine law \(p_\beta(U)dU\), path averages \(Z_b(U)\), and normalized product kernel \(q_\kappa(V\mid U)\) of [[nonlinear-conditional-gauge-response|the nonlinear conditional gauge calculation]]. Define the nonnegative matrix
\[
\mathsf P_{be}:=p_{b,e}=\sum_iw_{bi}n_{bi,e},\qquad
s:=\|\mathsf P\|_{2\to2}.
\tag{JF1}
\]
The letter \(\mathsf P\) here denotes path incidence, not a conditional expectation or a spectral projection. For a full fine tangent \(\xi=(\xi_e)\),
\[
\|dZ_b[\xi]\|_{\rm HS,norm}
\le\sum_e p_{b,e}\|\xi_e\|_g.
\]
Consequently all tangent components can be bounded jointly using \(s\), instead of summing a separate bound for each coarse link. The Schur test gives
\[
s^2\le
\left(\max_b\sum_ep_{b,e}\right)
\left(\max_e\sum_bp_{b,e}\right).
\tag{JF2}
\]
Uniformity requires both path-length and reuse control. Duplicating a readout arbitrarily many times increases this norm and cannot be treated as free information.

## Forward scores give a bidirectional bounded response

For the actual joint law \(\mu(dU,dV)=p_\beta(U)q_\kappa(V\mid U)dU\,dV\), its normalized forward score is
\[
s^{\to}_U[\xi]
=\kappa\sum_b\left[
\phi(V_b,dZ_b[\xi])
-\mathbb E_{q_\kappa(\cdot\mid Z_b)}\phi(V_b,dZ_b[\xi])
\right].
\tag{JF3}
\]
The second term is the derivative of the fine-dependent log normalizer. Conditional independence of the \(V_b\) and bounded normalized matrix pairings give
\[
\boxed{I_U^{\to}(\xi,\xi)
=\mathbb E_{V\mid U}|s_U^{\to}[\xi]|^2
\le C_{\to}\|\xi\|^2,\qquad C_{\to}:=\kappa^2s^2.}
\tag{JF4}
\]
No posterior Poincare constant and no smallness of \(\kappa\) is needed for this estimate.

Suppose the actual fine marginal \(p_\beta\) has Poincare constant \(\sigma>0\). Applying [[conditional-fisher-coercivity/inq|conditional Fisher coercivity]] with context \(U\) and hidden variable \(V\) gives
\[
\mathbb E\operatorname{Var}(f(V)\mid U)
\ge\frac{\sigma}{\sigma+C_{\to}}\operatorname{Var}(f(V)).
\tag{JF5}
\]
On the centered marginal carriers let \(T f(U)=\mathbb E[f(V)\mid U]\). Its adjoint is \(T^*F(V)=\mathbb E[F(U)\mid V]\). Since \(\|T\|=\|T^*\|\), (JF5) also proves
\[
\boxed{\mathbb E\operatorname{Var}(F(U)\mid V)
\ge\frac{\sigma}{\sigma+C_{\to}}\operatorname{Var}(F(U))}
\tag{JF6}
\]
for every fine \(L^2\) observable. Thus the two complete conditional-variance floors agree as optimal constants, even when the two conditional gradient-form gaps do not.

This distinction matters: a bound for posterior conditional variance averaged over \(V\) is not a uniform gradient Poincare inequality for each \(U\mid V\). It is also not yet the two-boundary physical slab bridge. The readout must be identified with the relevant preparation and boundary data before that interpretation is available.

For the elementary hypercubic Wilson convention, one sufficient choice is
\[
\sigma=\frac{r^2}{2}-8\beta(d-1)>0.
\tag{JF7}
\]
Equations (JF4)--(JF7) give a volume-uniform response for each fixed finite \(\kappa\), provided \(s\) is uniformly bounded. Allowing \(\kappa\) to diverge with volume or depth can destroy that uniformity. The restriction is strong bare coupling; the estimate does not continue automatically to the four-dimensional continuum.

## A coarse marginal estimate that uses its actual prior

Each conditional factor \(V_b\mid U\) has potential \(-\kappa\phi(V_b,Z_b)\) and
\[
\operatorname{Ric}+\operatorname{Hess}[-\kappa\phi]
\ge a g,\qquad a:=r^2/2-\kappa.
\]
If \(a>0\), the product conditional law has Poincare constant at least \(a\). Differentiating (JF3) with respect to all coarse variables also gives
\[
\|d_Vs^{\to}_U[\xi]\|_2\le\kappa s\|\xi\|.
\]
Conditional Poincare therefore permits the better of the two proved Fisher bounds:
\[
C_{\to}:=\kappa^2s^2\min\{1,a^{-1}\}.
\tag{JF8}
\]
Here all metrics have the fixed dimensionless normalization already declared.

For a coarse observable \(f(V)\), total variance and the same score bound show
\[
\operatorname{Var}_{\bar\mu}f
\le\left(1+\frac{C_{\to}}{\sigma}\right)
\mathbb E\operatorname{Var}(f(V)\mid U)
\le\frac{\sigma+C_{\to}}{a\sigma}\int|d_Vf|^2\,d\bar\mu.
\]
Hence the **actual coarse marginal** \(\bar\mu(dV)=\int\mu(dU,dV)\) obeys
\[
\boxed{\lambda_{\bar\mu}\ge\frac{a\sigma}{\sigma+C_{\to}}>0.}
\tag{JF9}
\]
This bound requires no separately assumed coarse effective potential. For a general observable \(F(U,V)\), [[contemporary-puzzles/yang-mills-mass-gap/two-scale-rg-descent-and-the-crossover-lemma|the two-scale Fisher--Poincare theorem]] instead gives the joint gradient-form constant \(T_F(a,\sigma,C_{\to})\). The marginal-only bound (JF9) can be stronger; the two conclusions concern different carriers.

## Reverse Fisher information and the exact effective Hessian

For a full coarse tangent \(X=(X_b)\), write
\[
\ell_X(U)=\frac{\kappa}{r}\sum_b\operatorname{ReTr}(X_bV_b^*Z_b(U)).
\]
The normalized reverse score is \(-\ell_X+\nu_V\ell_X\), so
\[
I_V^{\leftarrow}(X,X)=\operatorname{Var}_{\nu_V}(\ell_X),\qquad
\|d_U\ell_X\|_2\le\kappa s\|X\|.
\tag{JF10}
\]
If the **actual reverse conditional law** \(\nu_V\) has uniform Poincare constant \(\rho>0\), then
\[
\boxed{I_V^{\leftarrow}\le C_{\leftarrow}g_V,\qquad
C_{\leftarrow}:=\kappa^2s^2/\rho.}
\tag{JF11}
\]
The nonlinear conditional note supplies one sufficient \(\rho=r^2/2-\|D\|>0\). Neither (JF9) nor the joint gradient gap by itself supplies such a uniform posterior constant.

Let \(W(V)=-\log\int e^{-A_V(U)}dU\), up to a constant, be the actual coarse potential. Its product-geodesic Hessian is
\[
\boxed{\operatorname{Hess}W[X,X]
=-\frac{\kappa}{r}\mathbb E_{\nu_V}
\sum_b\operatorname{ReTr}(X_b^2V_b^*Z_b)
-I_V^{\leftarrow}(X,X).}
\tag{JF12}
\]
The reverse Fisher tensor is subtracted, not added. The fine-dependent normalizer remains inside \(\nu_V\) even though it has no \(V\)-derivative. The first term is bounded below by \(-\kappa\|X\|^2\); therefore
\[
\gamma:=r^2/2-\kappa-C_{\leftarrow}>0
\quad\Longrightarrow\quad \lambda_{\bar\mu}\ge\gamma.
\tag{JF13}
\]
One may use the better applicable bound from (JF9) and (JF13). Equations (JF11) and conditional Fisher coercivity then give another complete fine-response certificate \(\lambda_{\bar\mu}/(\lambda_{\bar\mu}+C_{\leftarrow})\). This is independent of, and need not improve, the forward-adjoint certificate (JF6).

## What the compact calibration excludes

[[conditional-fisher-coercivity/compact-su2-fisher-calibration|The exact Haar \(SU(2)\) pair]] has an unchanged coarse marginal for every \(\kappa\), yet its complete response floor tends to zero as the readout becomes sharp. Its reverse Fisher tensor grows and cancels the averaged coarse potential Hessian exactly. Thus coarse marginal smoothness, compactness and an unchanged marginal gradient gap do not establish a uniform response.

The coefficients here belong to one actual normalized joint law. They do not by themselves estimate predictors omitted by replacing a physical fine boundary with this readout. [[regional-gauge-readouts-and-conditional-lifting|Regional gauge lifting]] uses these forward scores, quantitative Fisher contraction and an unchanged opposite conditional to verify both relative-leakage obligations on an enlarged regional law. Iterated effective actions, induced metrics, uniform total loss and physical reconstruction remain to be constructed.

[[conditional-fisher-coercivity/receipts/relative_leakage_and_compact_gauge_receipt.py|The compact and incidence receipt]] checks the exact calibration, joint score bounds and coefficient arithmetic. These checks do not establish weak-bare-coupling Yang--Mills estimates.
