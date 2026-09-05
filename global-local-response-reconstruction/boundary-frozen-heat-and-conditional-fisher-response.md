# Boundary-Frozen Heat and Conditional Fisher Response

An auxiliary field response can be placed below the actual slab-recovery defect without guessing a comparison constant: evolve the interior under its conditional law while keeping the boundary fixed. The resulting bounded heat response is always at most the irrecoverable midpoint variance. A separate conditional-Fisher estimate can then supply its lower bound. Fast mixing within each fiber alone is insufficient, because a sharply localized fiber may still have a center almost completely determined by the boundary.

**Status: [EXACT] for the operator comparison and counterexamples; [EXACT AT FINITE WILSON REGULATOR] for the conditional generator under the stated raw-link hypotheses; [CONDITIONAL] for the lower Fisher and physical-transfer bounds; [OPEN] for uniform continuum survival.**

## Freeze the data that are allowed to predict

On the whole slab carrier \(\mathcal H=L^2(\mu)\), let
\[
E_D=\mathbb E_\mu[\,\cdot\mid\mathcal F_D]
\tag{BH1}
\]
retain the boundary data. This convention differs from a block-resampling notation \(E_A=\mathbb E[\cdot\mid\mathcal F_{A^c}]\); the retained sigma-algebra is explicit here.

Disintegrate \(\mu(dz,dy)=\nu_D(dz)\beta_z(dy)\). Give each conditional fiber a conservative nonnegative self-adjoint Dirichlet generator \(L_z\), measurably in \(z\), and form
\[
L_v=\int_Z^\oplus L_z\,d\nu_D(z)=\delta_v^*\delta_v.
\tag{BH2}
\]
The differential \(\delta_v\) changes only the interior variables. Thus
\(\operatorname{Ran}E_D\subseteq\ker L_v\).

For a finite raw-link Wilson cylinder, \(L_z\) can be the full weighted elliptic link-gradient generator on every unfrozen interior link. Smooth strict positivity of the conditional density and connectedness of the compact product \(SU(r)^{E_{\rm int}}\) give
\(\ker L_v=\operatorname{Ran}E_D\). Gauge-orbit derivatives alone, omitted links, or disconnected sectors need not give this equality.

Let \(J_C:L^2(\nu_C)\to\mathcal H\) pull back a complete midpoint or core observable, and let \(Q_C=I-P_{\mathbf1}\) center that marginal \(L^2\) carrier. Put
\[
B_D=J_C^*(I-E_D)J_C,\qquad
R_s^{\,v}=J_C^*(I-e^{-sL_v})J_C.
\tag{BH3}
\]
Nonnegative spectral calculus and the fixed boundary subspace imply
\[
\boxed{0\le R_s^{\,v}\le B_D.}
\tag{BH4}
\]
No conditional Poincare inequality is needed for this upper comparison. If \(D\) includes more information than the two endpoint slices, conditioning order gives
\[
R_s^{\,v}\le B_D\le B_{\rm endpoints}.
\tag{BH5}
\]
Exact equality with the endpoint bridge requires the same sigma-algebra or a proved Markov-shielding reduction.

This is a new **boundary-frozen alternative** to the unfrozen whole-law response in
[[exceptional-context-analysis-of-gauge-gradients|the differentiated-context construction]]. It does not prove that earlier response's separate comparison inequality by changing its generator silently.

## The bounded analysis map is explicit

For \(s>0\), define
\[
h_s(\lambda)=
\begin{cases}
\sqrt{(1-e^{-s\lambda})/\lambda},&\lambda>0,\\
\sqrt s,&\lambda=0.
\end{cases}
\]
Then
\[
A_s=\delta_v h_s(L_v)J_C,\qquad
R_s^{\,v}=A_s^*A_s,
\tag{BH6}
\]
and equivalently
\[
\langle f,R_s^{\,v}f\rangle
=\int_0^s\|\delta_v e^{-tL_v/2}J_Cf\|^2\,dt.
\tag{BH7}
\]
These maps extend boundedly to every \(L^2\) core observable. The exceptional gradient frame factors \(\delta_v\) by using only interior links and the conditional measure; its normalization is the same \(9/13\) as before.

If \(\ker L_v=\operatorname{Ran}E_D\), then
\[
e^{-sL_v}\longrightarrow E_D\quad\text{strongly},\qquad
R_s^{\,v}\uparrow B_D.
\tag{BH8}
\]
Consequently \(J_C^*e^{-sL_v}J_C\) tends to the
[[bridge-data-augmentation-solder/inq|data-augmentation operator]] \(K_D^*K_D\). Finite compressed heat generally is not a semigroup.

If in addition \(L_v\ge\rho(I-E_D)\), with \(\rho>0\), then
\[
\boxed{(1-e^{-s\rho})B_D\le R_s^{\,v}\le B_D.}
\tag{BH9}
\]
Conditional mixing controls how closely finite heat approaches the bridge response. It does not create a lower bound on the bridge response itself. A full bound \(L_v\ge\rho(I-P_{\rm constants})\) is impossible when nonconstant boundary functions remain fixed.

## Conditional stiffness can increase while the response closes

In the [[gaussian-bridge-gap-calibration/inq|variance-one Gaussian bridge]], write
\[
X=m+\sqrt\kappa\,\varepsilon,\qquad
\operatorname{Var}m=1-\kappa,\qquad
\kappa=\tanh(\omega\ell),\quad0<\kappa<1,
\]
where \(m,\varepsilon\) are independent. Keep \(m\) frozen and use conditional diffusion
\[
L_m=-\partial_x^2+\frac{x-m}{\kappa}\partial_x.
\tag{BH10}
\]
Its conditional gap is \(1/\kappa\). At response depth \(s\), the stationary update is
\[
X_s=m+e^{-s/\kappa}\sqrt\kappa\,\varepsilon
+\sqrt{\kappa(1-e^{-2s/\kappa})}\,\eta,
\]
with independent standard Gaussian \(\eta\). Thus \(X\) and \(X_s\) are jointly standard Gaussian with correlation
\[
r_s=1-\kappa+\kappa e^{-s/\kappa}.
\tag{BH11}
\]
The compressed operator \(P_s=J_X^*e^{-sL_v}J_X\) acts on the normalized Hermites by \(P_sh_n=r_s^nh_n\). Hence
\[
\boxed{\operatorname{gap}(I-P_s)
=\kappa(1-e^{-s/\kappa})\le\kappa.}
\tag{BH12}
\]
The fiber gap diverges as \(\kappa\downarrow0\), while the midpoint response closes. A normalization issue, not absent conditional ellipticity, carries this failure.

There is also an infinitesimal trap. On the polynomial core,
\[
J_X^*L_vJ_X=-\partial_x^2+x\partial_x=:N,
\tag{BH13}
\]
independent of \(\kappa\), but \(P_s\ne e^{-sN}\). Indeed its first-chaos eigenvalue is \(r_s\), not \(e^{-s}\). Repeated compression at short steps satisfies
\((P_{s/n})^n\to e^{-sN}\); it refreshes the boundary conditional law between steps and describes a different process.

The whole-interior version is equally explicit for a jointly Gaussian interior and boundary law. If \(C\) is the conditional interior covariance, \(X=RY\) has unconditional covariance \(V\), and the interior diffusion matrix is the identity, the normalized one-particle response is
\[
V^{-1/2}RC(I-e^{-sC^{-1}})R^*V^{-1/2}
\le V^{-1/2}RCR^*V^{-1/2}.
\tag{BH14}
\]
Positive definite covariances and the Gaussian polynomial-core closures are understood. Heating additional interior variables does not remove the boundary-angle obstruction.

## Compression is not the least-cost short

Let \(C_s=I-e^{-sL_v}\), and let \(E\) be the centered midpoint subspace inside \(\mathcal H\). A positive operator short \(S_E(C_s)\ge\gamma I_E\) would imply \(C_s\ge\gamma P_E\). Applying this to boundary functions in \(\ker C_s\) forces
\[
P_E\operatorname{Ran}E_D=0.
\tag{BH15}
\]
Ordinary correlated midpoint and boundary data violate this condition.

For example, take two uniform signs \(Y,Z\) with \(\mathbb E[YZ]=a\), \(0<|a|<1\), and \(L_v=I-E_Z\). The centered midpoint compression is
\((1-e^{-s})(1-a^2)>0\). Its short is zero: the zero-cost vector \(Z/a\) has midpoint projection \(Y\), so a hidden extension cancels the cost. The unfrozen-whole-law short in
[[nonlinear-whole-law-surface-response/inq|the surface-response construction]] remains a different branch. Infimizing over hidden extensions here would also allow changes of the very boundary data being held fixed.

## An independent lower certificate

[[conditional-fisher-coercivity/inq|Conditional Fisher coercivity]] supplies the missing type of estimate. If the boundary marginal has Poincare constant \(\lambda_D>0\) in a declared metric and the conditional family has Fisher tensor at most \(C_F\) times that metric, then
\[
B_D\ge\frac{\lambda_D}{\lambda_D+C_F}Q_C.
\tag{BH16}
\]
With the additional conditional gap \(\rho\),
\[
\boxed{R_s^{\,v}\ge
(1-e^{-s\rho})\frac{\lambda_D}{\lambda_D+C_F}Q_C.}
\tag{BH17}
\]
This separates finite response depth, conditional coupling, and normalization by the actual boundary law. The proof does not posit the desired angle as a premise.

[[collared-quasi-factorization-and-surface-response/fisher-collar-bound-for-wilson-laws|The nonlinear Wilson collar bound]] derives all three coefficients in an explicit strong-coupling regime, with no transverse-area factor. Extending their control to the actual integrated laws on a continuum trajectory remains open. Only the stationary vacuum-prepared bridge-to-transfer comparison and subsequent reconstruction turn these dimensionless estimates into a mass statement.
