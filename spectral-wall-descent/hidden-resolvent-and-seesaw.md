# One Schur Grammar, Three Possible Observable Effects

Eliminating a hidden block produces the same typed algebraic operation in three settings: a shift of homogeneous response, a scale-dependent kernel for nonconstant observational modes, and a small effective mass through a finite internal seesaw. The response operator is positive Hermitian, whereas the Majorana mass block is complex symmetric and need not be positive. What is common is therefore a Schur-complement grammar, not one already-constructed operator and not a derivation of dark energy, dark matter, or neutrino mass.

## The quadratic hidden-block theorem

Let \(x\) denote retained coordinates and \(h\) hidden coordinates. Consider the positive quadratic cost

$$
\mathscr I(x,h)
=\frac12
\begin{pmatrix}x\\h\end{pmatrix}^{\!*}
\begin{pmatrix}
G_{xx}&B\\
B^*&L
\end{pmatrix}
\begin{pmatrix}x\\h\end{pmatrix},
$$

where \(L>0\). The stationary hidden coordinate is

$$
h_*=-L^{-1}B^*x.
$$

Substitution gives the **[EXACT SCHUR-COMPLEMENT IDENTITY]**

$$
\boxed{
G_{xx}^{\mathrm{eff}}
=G_{xx}-BL^{-1}B^*.}
$$

The full form is positive if and only if \(L>0\) and \(G_{xx}^{\mathrm{eff}}\geq0\). Thus a healthy eliminated mode lowers the retained precision by a positive semidefinite term. Equivalently, it increases retained covariance where the inverse exists. This sign is fixed by positivity rather than chosen phenomenologically.

If \(L\) has null directions, the formula requires a pseudoinverse on a declared complement and the compatibility condition \(B\ker L=0\). A gauge zero mode must be quotiented rather than treated as a heavy physical mode.

## One homogeneous field, separated by representation

Let a hidden field \(h\) have a translation-invariant positive operator

$$
L(k;N)>0.
$$

This model already assumes a translation group, a Fourier carrier, and nonzero spatial modes; it does not derive those structures from the homogeneous algebra. For real-space fields impose

$$
h_{-k}=\overline{h_k},\qquad
\zeta_{-k}=\overline{\zeta_k},
$$

$$
L(-k)=L(k),\qquad
G_{\zeta\zeta}(-k)=G_{\zeta\zeta}(k),\qquad
v(-k)=\overline{v(k)}.
$$

Take \(N,h_0,u\) real. The integral below is over all nonzero momenta with the displayed factor \(1/2\); equivalently, one may choose one representative from each pair \(\{k,-k\}\) and remove the duplicate counting.

Its zero mode may couple to the homogeneous scale coordinate \(N\), while its nonzero modes couple to mean-zero observational coordinates \(\zeta_k\):

$$
\mathscr I
=\frac12G_{NN}N^2
+\frac12L(0)|h_0|^2
+uNh_0
$$

$$
\qquad
+\frac12\int_{k\neq0}
\left[
G_{\zeta\zeta}(k)|\zeta_k|^2
+L(k)|h_k|^2
+2\operatorname{Re}
\bigl(v(k)\zeta_{-k}h_k\bigr)
\right]\mathrm dk.
$$

Momentum conservation forbids a quadratic \(N\zeta_k\) term at the homogeneous reference even though both sectors couple to the same hidden field. Eliminating \(h\) gives

$$
\boxed{
G_{NN}^{\mathrm{eff}}
=G_{NN}-\frac{|u|^2}{L(0)},}
$$

$$
\boxed{
G_{\zeta\zeta}^{\mathrm{eff}}(k)
=G_{\zeta\zeta}(k)
-\frac{|v(k)|^2}{L(k)}.}
$$

The same resolvent \(L^{-1}\) changes the global and nonconstant blocks without making the hidden substrate a classical lumpy space.

Positivity of \(L\) alone is insufficient for stability. In the scalar blocks the full Schur conditions are

$$
G_{NN}\geq\frac{|u|^2}{L(0)},\qquad
G_{\zeta\zeta}(k)\geq\frac{|v(k)|^2}{L(k)}.
$$

Thus the construction explains how eliminating hidden coordinates can modify a pre-existing scale spectrum. It does not yet explain why the observable carrier possesses spatial modes in the first place.

## The mixed jet comes from scale dependence of the resolvent

Suppose \(L\), \(v\), and the bare observational kernel depend on \(N\). Differentiation gives

$$
\boxed{
\begin{aligned}
\partial_NG_{\zeta\zeta}^{\mathrm{eff}}(k)
={}&\partial_NG_{\zeta\zeta}(k)
-\frac{2\operatorname{Re}
(\overline v\,\partial_Nv)}{L}\\
&+\frac{|v|^2\partial_NL}{L^2}.
\end{aligned}}
$$

This is a calculated mechanism for a nonzero derivative of the effective precision kernel when the quadratic mixed block vanishes. It equals the earlier \(\mathcal C_{N\zeta\zeta}\) only when \(G^{\mathrm{eff}}\) is the Hessian of one effective potential in the declared affine coordinates. Without that Hessian weld it is a response-kernel derivative, not automatically the BKM cubic tensor. A change of global scale can alter the cost of hidden mediation and thereby change the spectrum of observable distinctions.

For the local prototype

$$
L(k;N)=k^2+M(N)^2,
$$

the correction is a Yukawa resolvent,

$$
-\frac{|v(k)|^2}{k^2+M(N)^2}.
$$

For constant \(v\), its magnitude is largest at long wavelength. More generally, bounded \(v(k)\) proves only ultraviolet decay of order \(k^{-2}\); a long-wavelength maximum requires additional nonvanishing and monotonicity hypotheses on the vertex. This differentiation of an existing scale spectrum is produced by algebraic elimination, not assigned as primordial lumpiness. [[lorentzian-spectral-envelope/entry|The Cauchy spectral-envelope module]] derives a similar positive resolvent from heat-scale mixing and states exactly why averaging, Schur elimination, and covariance inversion remain different operations.

## The determinant companion

The Schur complement is only the noncentral output of eliminating \(h\). For an invertible hidden block,

$$
\det
\begin{pmatrix}
G&B\\
B^*&L
\end{pmatrix}
=\det L\,\det(G-BL^{-1}B^*).
$$

For a constant finite real bosonic block, Gaussian integration contributes the retained response correction while \(\tfrac12\log\det L\) is only an additive normalization. If \(L=L[\bar x,g,\ldots]\) depends on retained backgrounds, its regulated determinant can instead generate cosmological, Einstein, and higher-curvature coefficients. For an affine classical positive Gaussian family, the negative log partition term has Hessian

$$
\partial_I\partial_J
\left[-\frac12\log\det L\right]
=\frac12\operatorname{Tr}
\left(
L^{-1}\partial_IL
L^{-1}\partial_JL
\right),
$$

the classical Fisher metric, equivalently commutative BKM. The real bosonic effective action contains \(+\tfrac12\log\det L\), whose affine Hessian has the opposite sign. [[spectral-wall-descent/response-determinant|The response--determinant note]] develops this finite same-operator bridge and the unresolved regulator normalization.

## The same grammar is the seesaw

For one light and one heavy internal mode, take the symmetric mass block

$$
\mathcal M
=\begin{pmatrix}
0&m\\
m&M
\end{pmatrix},
\qquad |M|\gg|m|.
$$

Eliminating the heavy component at leading order gives

$$
\boxed{
\mathcal M_{\mathrm{light}}^{\mathrm{eff}}
=-mM^{-1}m,}
$$

so \(|m_{\mathrm{light}}|\sim |m|^2/|M|\). In several generations, declare the block convention

$$
\mathcal M
=\begin{pmatrix}
0&M_D^T\\
M_D&M_R
\end{pmatrix}.
$$

Its light Schur block is

$$
M_{\mathrm{light}}^{\mathrm{eff}}
=-M_D^TM_R^{-1}M_D,
$$

when \(M_R\) is invertible. With the opposite placement of \(M_D\), the same calculation reads \(-M_DM_R^{-1}M_D^T\). [[spectral-wall-descent/majorana-response-jacobian|The Majorana response Jacobian]] shows separately that the same \(M_R\) enters observable gravitational, cosmological, and Higgs coefficients through \(R=M_R^*M_R\).

The fermionic mass bilinear is not a positive response matrix, so the positivity and covariance-order conclusions of the first theorem do not transfer to it. What is shared is the algebraic Schur operation and its inverse heavy block, not the physical type of the quadratic form.

## What the three interpretations would require

The exact commonality is only

$$
\boxed{
\text{observable correction}
=-B L^{-1}C.}
$$

The terminal map is sector-dependent: \(C=B^\dagger\) for a Hermitian response form, while \(C=B^T\) for the declared complex-symmetric Majorana bilinear. Suppressing that distinction would falsely identify two different quadratic types.

Three physical readings are then possible but unproved:

- A zero-mode correction to \(G_{NN}\) could participate in a homogeneous dark-energy response only after the CST source and covariant gravitational weld are derived. A lowered positive precision is not by itself accelerated expansion.
- A long-wavelength correction to \(G_{\zeta\zeta}(k)\) could enhance observable covariance and imitate an additional clustering channel only after the CWST precision-to-cosmology map is constructed. It is not particle dark matter and need not reproduce lensing or structure growth.
- An internal finite block can produce a small neutrino mass by the established seesaw grammar, but the upstream wall must still explain the scale and orientation of \(M_R\).

The proposal becomes genuinely common only if one independently constructed hidden spectral sector supplies the zero mode, propagating modes, and finite internal block, with their couplings constrained by one algebra or correspondence. Reusing the symbol \(M\) in three fitted models would not satisfy that requirement.

## Verification and failure conditions

[[spectral-wall-descent/receipts/verify-spectral-wall.py|The finite receipt]] verifies the Schur-complement identity, its positivity criterion in a positive example, and the derivative of a scale-dependent Yukawa resolvent.

- If \(L\) is not positive on the physical hidden sector, elimination can introduce an instability rather than a dark response.
- If \(L^{-1}\) is nonlocal, a causal Lorentzian realization must control support, poles, and boundary conditions.
- If symmetry permits \(N\zeta\) directly, the vanishing mixed block cannot be attributed to momentum separation alone.
- If the hidden sector is selected by fitting the desired background, spectrum, or neutrino mass, the construction is circular.
- If the three effects require unrelated carriers or independently chosen couplings, the shared Schur grammar is analogy rather than one common source.
