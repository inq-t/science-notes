# Smoothed Endpoint Response

A change of initial context can be distributed over several internal layers while leaving the observed endpoint fixed. For central compact-group kernels this gives an exact normalized endpoint score. A buffer of unchanged layers bounds its conditional second moment, and whole-column variance factorization controls the interacting response without counting spatial volume. The resulting Fisher bound concerns the actual prepared history; it does not replace that history by independent kinetic steps.

**Status: [EXACT CONDITIONAL THEOREM] for the finite smooth compact-group laws below.** The [[strong-coupling-gap-and-continuum-crossover/wilson-temporal-column-coercivity|Wilson construction]] calculates its inputs in a temporally refinement-uniform small magnetic/electric-ratio regime. The theorem does not select the group, state law, spatial graph or physical clock.

## The operator differentiates an endpoint law

Let \(G\) be a compact connected Lie group with a declared bi-invariant metric and normalized Haar measure. Let \(k:G\to(0,\infty)\) be a smooth central probability density. Write
\[
s_v(z)=\left.\frac{d}{ds}\log k(e^{sv}z)\right|_{s=0},
\qquad
\mathbb E_k s_v=0,\qquad
\mathbb E_k s_v^2\le j\|v\|^2.
\tag{SR1}
\]
The zero mean follows from Haar invariance. The Fisher bound \(j\) is an input to be calculated for the kernel; it is not the square of a pointwise score bound unless that weaker estimate is all that is available.

On a finite set of spatial indices \(E\), take histories \(U_0,\ldots,U_N\in G^E\), with fixed \(U_0=U\), product kinetic bonds \(k(U_{t,e}U_{t+1,e}^{-1})\), and smooth time-slice potentials \(V_t(U_t)\). Take smooth positive preparation factors of the separated form \(w_0(U_0)w_N(U_N)\). The kernel, all \(V_t\), and \(w_N\) have no additional dependence on the varying parameter \(U\). Assume the following bounds hold uniformly in the initial value and preparation depth:

- The history law satisfies [[inq#A local insertion has a finite whole-column cost|whole-column variance factorization (TC11)]] with coefficient \(1-q>0\).
- Conditional on the other whole columns and on \(U_{2m,e}\), the segment \(0,\ldots,2m\) of column \(e\) differs from its kinetic bridge by a potential of oscillation at most \(D_m\). The remaining history couples to this segment only through its endpoints. Time-slice interactions have this property; arbitrary temporally nonlocal insertions need not.
- The score \(D_v\) of the steered slice potentials, defined below, obeys \(\frac12\|\delta D_v\|_{\ell^2(E)}\le L_m\|v\|_{\ell^2(E)}\), where \(\delta_e\) is oscillation under resampling the whole column \(e\).

Here \(m\ge1\), \(N\ge2m\), and all conditional factorization hypotheses include the chosen preparation. Arbitrary extra spatially coupled end weights cannot be added without rechecking them. Define
\[
R_m=\frac{\max k^{*m}}{\min k^{*(2m)}},\qquad
A_m=e^{D_m}R_m\frac jm.
\tag{SR2}
\]
Positivity and compactness make this ratio finite at fixed parameters; useful uniformity requires quantitative kernel bounds.

Let \(\eta_U\) be the actual marginal law of \(U_{2m}\). The score operator and its Gramian have types
\[
\mathcal J_U:T_UG^E\longrightarrow L^2_0(\eta_U),\qquad
\mathcal J_Uv=\partial_v\log\eta_U,\qquad
I_U=\mathcal J_U^*\mathcal J_U.
\tag{SR3}
\]
All derivatives keep the endpoint coordinates fixed. The theorem is
\[
\boxed{I_U\le C_m g_{G^E},\qquad
C_m=\frac{(\sqrt{A_m}+L_m)^2}{1-q}.}
\tag{SR4}
\]

## A ramp and an unchanged buffer

Write tangent directions through left multiplication and put
\[
h_t=(1-t/m)_+,\qquad U_{t,e}\mapsto e^{s h_tv_e}U_{t,e}.
\tag{SR5}
\]
This changes the initial configuration, preserves each integrated Haar measure, and leaves the endpoint and all layers \(t\ge m\) unchanged. For \(Z_{t,e}=U_{t,e}U_{t+1,e}^{-1}\), centrality gives
\[
k(e^{sh_tv_e}Z_{t,e}e^{-sh_{t+1}v_e})
=k(e^{s(h_t-h_{t+1})v_e}Z_{t,e}).
\]
Differentiating the transformed history weight therefore gives
\[
F_v=\sum_e B_e+D_v,\qquad
B_e=\frac1m\sum_{t<m}s_{v_e}(Z_{t,e}),\qquad
D_v=-\sum_{t=1}^{m-1}h_t\,dV_t(U_t)[v].
\tag{SR6}
\]
An initial potential contributes a deterministic term and cancels in the normalized score. The parameter-independent end factor at \(N\ge2m\) is unchanged. Differentiation of the normalized marginal gives exactly
\[
\mathcal J_Uv=\mathbb E[F_v\mid U_{2m}]-\mathbb E F_v,
\qquad
\|\mathcal J_Uv\|_2^2\le\operatorname{Var}F_v.
\tag{SR7}
\]

Under the reference kinetic path, increments are independent and centered scores are orthogonal, so \(\mathbb E B_e^2\le(j/m)\|v_e\|^2\). Fixing the endpoint after \(2m\) steps weights the first \(m\) increments by the density of the remaining \(m\) increments, divided by \(k^{*(2m)}\) at the complete displacement. This likelihood ratio is bounded by \(R_m\). The conditional potential comparison then gives
\[
\mathbb E[B_e^2\mid\text{exterior columns},U_{2m,e}]
\le A_m\|v_e\|^2.
\tag{SR8}
\]
It holds uniformly in the fixed endpoint, so mixing that endpoint with the actual future weight preserves it. This is a one-column conditional comparison, not an extensive comparison with product Haar.

Under resampling column \(e\), every \(B_f\), \(f\ne e\), is fixed. Conditional standard deviations satisfy
\[
\sqrt{\operatorname{Var}_e F_v}
\le\sqrt{A_m}\|v_e\|+\tfrac12\delta_eD_v.
\]
Take the \(\ell^2(E)\) norm, apply the assumed bound for \(D_v\), and then (TC11). Together with (SR7), this proves (SR4). In particular, mixed derivatives of potentials containing neighboring tangent components must enter \(\delta_eD_v\), even when \(v_e=0\).

## From endpoint response to complete recovery loss

Suppose the preparation limit is an actual reversible stationary Markov law with midpoint marginal \(\nu\), whose \(2m\)-step transition is \(\eta_U\) and whose endpoint score satisfies (SR4). Passing that score estimate needs a fixed-carrier regularity argument; finite-preparation weak convergence alone does not pass derivatives. Assume also the independently proved midpoint gradient inequality
\[
\underline\lambda_\nu\operatorname{Var}_\nu f
\le\int|df|^2\,d\nu,\qquad\underline\lambda_\nu>0.
\tag{SR9}
\]
The two endpoints are conditionally independent given the midpoint; their joint forward Fisher bound is \(2C_mg\). Apply [[conditional-fisher-coercivity/inq#A background-metric certificate that permits singular Fisher information|CF9]] from endpoint observables to midpoint conditional means. The reverse predictor is its Hilbert adjoint. Equality of centered operator norms gives, on the complete midpoint carrier,
\[
\boxed{I-S_{\rm bridge}\ge
\frac{\underline\lambda_\nu}{\underline\lambda_\nu+2C_m}Q_0.}
\tag{SR10}
\]
Thus finite-dimensional parameter derivatives can control every square-integrable observable through a proved score inequality; no truncation to parameter tangents is involved. Reversibility alone does not imply conditional independence of the two endpoints: the Markov property is essential here.

The preparation restriction is also substantive. On one \(U(1)\) column with \(k\equiv1\), a factor \(e^{a\cos(\theta_0-\theta_{2m})}\), \(a\ne0\), directly conveys initial-context information to the endpoint. Although the kinetic score and all internal potential scores vanish, the endpoint Fisher tensor does not. Such a correlated preparation has an extra derivative term and lies outside (SR6).

For temporal refinement, the useful quantities are \(j/m\), \(D_m\), \(L_m\), \(R_m\), and the margins \(1-q\), \(\underline\lambda_\nu\). A score that diverges at one step can still have bounded cost across a fixed positive depth. The unchanged buffer, not a minimum temporal pixel, makes the conditional estimate possible. Once the complete floor is proved, [[bridge-data-augmentation-solder/bridge-floor-under-joint-limits|joint-law convergence]] can preserve it without preserving the Fisher tensor. Existence, nontriviality and physical interpretation of that limiting law remain separate obligations.
