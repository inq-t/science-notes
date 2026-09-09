# Closed Normalization and Cosmic Response

A complete local response can miss a physical mode that never returns to its readout. The closed determinant can still detect that mode. A marked Gaussian determinant gives an exact finite witness: local response and its homogeneous variation are derivatives of the same normalization. The conjecture is that one algebraically selected sewing law fixes this joint datum and admits cosmic and local physical returns. Unit transparency constrains presentation auxiliaries, but does not by itself fix the normalization of genuine closed diagrams.

## One marked determinant generates an open response

Use a finite complex carrier with a fixed positive pairing and Gaussian reference measure. Let
\[
Q(z,N)=z\Gamma(N)+K(N)>0,\qquad z>0,
\tag{CN1}
\]
where \(\Gamma\ge0\), \(K=K^\dagger\), and the coefficients depend smoothly on a real source \(N\). The source is not physical time; the spectral meaning and units of \(z\) must be supplied independently. Put \(R=Q^{-1}\). Choose a readout insertion \(J:\mathbb C^m\to\mathbb C^n\), and a Hermitian matrix source \(T\) sufficiently small that \(Q+JTJ^\dagger>0\). For \(\nu\in\mathbb N_{>0}\) independent complex Gaussian copies, define
\[
\mathcal Z(z,N,T)=\det(Q+JTJ^\dagger)^{-\nu},
\qquad \mathcal I=-\log\mathcal Z.
\tag{CN2}
\]
The matrix determinant lemma gives
\[
\boxed{
\frac{\mathcal Z(z,N,T)}{\mathcal Z(z,N,0)}
=\det\!\left(I+T\mathcal R_{\rm loc}(z,N)\right)^{-\nu},
\qquad \mathcal R_{\rm loc}=J^\dagger Q^{-1}J.
}
\tag{CN3}
\]
Indeed, factor out \(Q\) and use \(\det(I+AB)=\det(I+BA)\). When \(J\) is supported on retained variables, block inversion makes \(\mathcal R_{\rm loc}\) the corresponding pullback of the inverse Schur complement. Thus arbitrary matrix marks determine the entire open response, including off-diagonal entries; an unmarked determinant determines much less.

For a Hermitian source direction \(S\), in a transport where \(J\) and its source coordinates are fixed,
\[
\begin{aligned}
D_T\mathcal I\big|_{T=0}[S]
&=\nu\operatorname{Tr}(S\mathcal R_{\rm loc}),\\
\partial_ND_T\mathcal I\big|_{T=0}[S]
&=-\nu\operatorname{Tr}\!\left(SJ^\dagger RQ_NR J\right)
=\nu\operatorname{Tr}(S\partial_N\mathcal R_{\rm loc}).
\end{aligned}
\tag{CN4}
\]
This is a finite common-source test at every \(z>0\). A moving \(J\) contributes the additional terms \(J_N^\dagger RJ+J^\dagger RJ_N\). Choosing \(J\) after seeing the desired response would not supply a physical readout construction. [[program-core/common-response-form|The common response form]] owns the independent state geometry and its mixed-response compatibility requirement.

The closed spectral derivative is
\[
\partial_z\mathcal I(z,N,0)
=\nu\operatorname{Tr}(Q^{-1}\Gamma).
\tag{CN5}
\]
If \(\Gamma>0\), this equals \(\nu\operatorname{Tr}(z+H)^{-1}\) for \(H=\Gamma^{-1/2}K\Gamma^{-1/2}\): it records every generalized eigenvalue, including multiplicities, but not its coupling to a chosen readout. A degenerate \(\Gamma\) requires auxiliary elimination and a justified carrier before an ordinary physical Hamiltonian is claimed, as [[transparent-units-and-hidden-determinants|the unit theorem]] illustrates.

## A hidden source changes normalization while the local response stays fixed

Consider
\[
Q(z,N)=
\begin{pmatrix}1+z&0\\0&1+c(N)z\end{pmatrix},
\qquad c(N)>0,\qquad J=\binom{1}{0}.
\tag{CN6}
\]
Eliminating the second variable returns
\[
\left((1+c(N)z)^{-\nu},\ 1+z\right),
\qquad \mathcal R_{\rm loc}(z,N)=\frac1{1+z}.
\tag{CN7}
\]
The hidden generalized rate is \(1/c(N)\). Its entire local response is invisible, although its closed contribution \(\mathcal I_{\rm hid}=\nu\log(1+c(N)z)\) has
\[
\partial_N\mathcal I_{\rm hid}
=\frac{\nu zc'}{1+cz},\qquad
\partial_N^2\mathcal I_{\rm hid}
=\nu\left[\frac{zc''}{1+cz}-\frac{z^2(c')^2}{(1+cz)^2}\right].
\tag{CN8}
\]
For fixed \(z>0\), its normalized Gaussian family has Fisher response \(g_{NN}^{\rm F}=\nu[z c'/(1+cz)]^2\). This is a comparison diagnostic, not a cosmic identification. The same hidden factor occurs in the unit theorem after changing to relative coordinates. It is excluded when the added variable is declared a pure presentation unit; a genuine hidden physical sector requires a separate justification and cannot be erased by that declaration.

[[spectral-wall-descent/response-determinant|Response and determinant from one hidden operator]] owns the sign distinction: bosonic elimination gives \(+\nu\log\det Q\) in the effective action, while the positive Gaussian Fisher metric is the affine Hessian of \(-\nu\log\det Q\). Nonlinear source paths add the contact term \(\nu\operatorname{Tr}(Q^{-1}Q_{NN})\) to the action Hessian. Positive statistical response is therefore not automatically a restoring potential. If retained frame variables are subsequently integrated, their full log-partition curvature also includes their fluctuations, as in [[global-local-response-reconstruction/cosmological-reconvergence-contract|the cosmological response contract]].

## Unit transparency leaves a possible closed scalar freedom

Suppose a diagram family admits a real scalar \(V(D,N)\) that is additive under its prescribed sewing and vanishes on presentation units:
\[
V(D_2\circ D_1,N)=V(D_2,N)+V(D_1,N),
\qquad V(1,N)=0.
\tag{CN9}
\]
Assume \(V\) is independent of integrated boundary variables and of the local matrix source \(T\). No geometric volume or nonzero such functional has been derived here. If one exists, then for a constant \(\Lambda\),
\[
\boxed{\widetilde{\mathcal Z}_D
=e^{-\Lambda V(D,N)}\mathcal Z_D}
\tag{CN10}
\]
preserves sewing, unit transparency, normalized boundary laws and (CN3)–(CN4). Yet it shifts \(\mathcal I_D\) by \(\Lambda V(D,N)\), and hence shifts its homogeneous variation whenever \(V_N\ne0\). Even the mixed-source identity does not fix this central freedom. A proposed primitive evaluation must select or exclude these scalar characters; their absence cannot be inferred from the unit test.

## Centering the transfer does not fix its gravitational source

The distinction has a direct spectral form. If \(H\) has vacuum energy \(E_0\), then adding a scalar \(cI\) changes the closed transfer but leaves its vacuum-centered generator unchanged:
\[
e^{-t(H+cI)}=e^{-tc}e^{-tH},\qquad
(H+cI)-(E_0+c)I=H-E_0I.
\tag{CN11}
\]
Thus no measurement of the centered gap alone can determine \(c\). The Perron normalization of [[commutator-preparation-transfer-and-marked-gluing|the finite path law]] retains exactly this distinction. [[preparation-compression-and-the-returned-potential|Preparation compression]] additionally shows that changing a nonconstant positive potential can lower the centered gap because the vacuum shifts too.

If a separate geometric return identifies an additive scalar with spacetime volume, the same freedom becomes a cosmological source. For a Lorentzian matter action with signature \((-+++)\), \(c=1\), and convention \(T_{\mu\nu}=-(2/\sqrt{-g})\,\delta S/\delta g^{\mu\nu}\), adding
\[
S_c=-\rho_c\int\sqrt{-g}\,d^4x
\quad\Longrightarrow\quad
\Delta T_{\mu\nu}=-\rho_c g_{\mu\nu}.
\tag{CN12}
\]
This follows from \(\delta\sqrt{-g}=-(1/2)\sqrt{-g}\,g_{\mu\nu}\delta g^{\mu\nu}\); the displayed sign uses the stated stress convention. A different action/sign convention must be transported consistently. Nothing in (CN9) has yet constructed this spacetime volume or source map.

The useful research connection is therefore a common **selection of absolute weight and relative excitation**, with distinct tests. A vacuum term shifts a gravitational source; a mass gap concerns the complete centered physical spectrum. A trace anomaly, a thermal horizon scale or a finite transfer gap cannot by itself identify these returns. The [[global-local-response-reconstruction/cosmological-reconvergence-contract|reconvergence contract]] requires the relevant states, sources and carriers to come from one constructed law.

## Fluctuating central weights carry shared memory

A possible extension replaces the scalar character by a law for a real central variable \(\lambda\). Let \(\pi\) have the exponential moments needed below, and define
\[
W(V)=\int e^{-\lambda V}d\pi(\lambda),\qquad
d\pi_V(\lambda)=W(V)^{-1}e^{-\lambda V}d\pi(\lambda).
\tag{CN13}
\]
If two pieces retain the same \(\lambda\), their weight is \(W(V_1+V_2)\). Independently averaging each piece instead gives \(W(V_1)W(V_2)\). These agree for every \(V_1,V_2\) near zero only when \(\pi\) is a point mass: multiplicativity makes \(\log W\) linear, whereas
\[
\boxed{
\partial_{V_1}\partial_{V_2}\log W(V_1+V_2)
=\operatorname{Var}_{\pi_{V_1+V_2}}(\lambda).}
\tag{CN14}
\]
The variance is strictly positive for a nondegenerate law. Thus averaging a fluctuating global coefficient does not preserve the scalar sewing character automatically. Sewing can instead retain \(\lambda\) and its conditional law until the final evaluation. Resampling it separately changes the theory, just as reusing or resampling the edge preparations changes [[commutator-preparation-transfer-and-marked-gluing|the marked path law]].

This is a concrete stochastic research option, not a derivation of a cosmological constant, a spacetime volume, or its fluctuation law. A proposed cosmic application must specify whether its central variable is shared, renewed or dynamically correlated and must retain its cross-region sources. A marginal fluctuation magnitude alone does not determine that law.

## A common preparation scale has an exact normalization response

[[local-incidence-preparations-and-the-gauge-transfer|The local incidence construction]] now gives a concrete finite common-source family. Use its general-group convention on a fixed finite graph, with \(d=\dim G\), independent \(n\times k_e\) preparations and the sufficient moment bounds of [[general-group-preparation-and-the-casimir-return|the general-group theorem]]. Give every Gaussian entry the same variance \(s>0\), and put \(u=\log s\). Hold the comparison pace, incidence, representation and anchored strengths fixed.

Let \(Z_\alpha(s)\) be the exact product of free temporal row normalizations. Before performing the Gaussian integral, its comparison exponent is independent of \(s\). In the normalized joint law of those free comparisons and preparations, denoted \(\Pi_{\alpha,s}\), define
\[
R=\sum_e nk_e,\qquad T=\frac1s\sum_e\|\Xi_e\|_{\rm HS}^2.
\]
The Gaussian prior has score \(T-R\), and its derivative with respect to \(u\) is \(-T\). Differentiation under the finite integrals therefore gives
\[
\boxed{
\partial_u\log Z_\alpha=\mathbb E_{\Pi_{\alpha,s}}T-R,\qquad
\partial_u^2\log Z_\alpha=
\operatorname{Var}_{\Pi_{\alpha,s}}T-\mathbb E_{\Pi_{\alpha,s}}T.
}
\tag{CN15}
\]
The normalized joint score is \(T-\mathbb ET\), so its Fisher response is \(\operatorname{Var}T\). The second term in (CN15) is the contact term for the logarithmic variance path. The raw logarithmic Hessian is not that Fisher response.

At fixed graph, temporal localization selects the determinant-weighted preparations. Their radial variables satisfy
\[
\frac{\|\Xi_e\|_{\rm HS}^2}{s}
\sim\operatorname{Gamma}(nk_e-d/2,1)
\quad\text{independently in the limiting preparation law}.
\tag{CN16}
\]
Polynomially weighted domination in the general-group theorem proves convergence of their first and second moments. Consequently
\[
\boxed{
\partial_u\log Z_\alpha\longrightarrow-\frac{d|\mathcal E|}{2},\qquad
\partial_u^2\log Z_\alpha\longrightarrow0,
\qquad
\operatorname{Var}_{\Pi_{\alpha,s}}T\longrightarrow R-\frac{d|\mathcal E|}{2}>0.
}
\tag{CN17}
\]
This proves the differentiated limits directly, rather than differentiating an uncontrolled leading asymptotic. \(|\mathcal E|\) counts the declared independent link comparisons in this family. Under [[preparation-transport-through-spatial-subdivision|pure preparation transport]], \(Z_\alpha\) and (CN15) stay exactly the same: one must use the original comparison rank, not the dimension of a larger redundant fine cover.

The calculation concerns one retained normalization factor. An interacting closed chain also contains the variation of its actual kernels; those terms must be differentiated together with \(Z_\alpha^{-N}\). Neither this count of comparison directions nor its constant logarithmic response has been identified with spacetime volume, gravitational stiffness or a cosmological constant.

Even a fully gauged tree has a trivial physical configuration carrier while these raw link comparisons retain their localization exponent. The count is therefore not a physical degree-of-freedom count obtained merely by naming it a volume.

## The same scale probes the interacting vacuum

On the fixed graph, the returned family has the exact form
\[
H_s=K_s+V_s=s^{-1}K+sV,\qquad
D_s:=\partial_uH_s=-K_s+V_s,\qquad
\partial_u^2H_s=H_s,
\tag{CN18}
\]
where \(K,V\) are fixed, and all normalization and metric conventions are those of the local incidence owner. This includes faithful reducible representations. The reciprocal coefficient relation leaves the propagation product unchanged while this homogeneous source changes the relative electric and magnetic response.

Let \(\psi_s\) be the normalized positive ground vector, \(E_s\) its eigenvalue, and \(R_s=(H_s-E_s)^{-1}\) on the vacuum complement. At every fixed \(s>0\), compact ellipticity gives an isolated simple ground, and the family is analytic on its common operator domain. Differentiating the eigenvalue equation in the normalization \(\langle\psi_s,\partial_u\psi_s\rangle=0\) yields
\[
J_s=(D_s-\langle D_s\rangle_{\psi_s})\psi_s,
\qquad \partial_u\psi_s=-R_sJ_s,
\]
\[
\boxed{
\partial_uE_s=\langle V_s-K_s\rangle_{\psi_s},\qquad
\partial_u^2E_s=E_s-2\langle J_s,R_sJ_s\rangle.
}
\tag{CN19}
\]
The source vector can be written using only bounded multiplication:
\(J_s=2(V_s-\langle V_s\rangle_{\psi_s})\psi_s\), hence
\(\|J_s\|^2=4\operatorname{Var}_{\psi_s}(V_s)\).
This follows from \(K_s\psi_s=(E_s-V_s)\psi_s\). The positive susceptibility in (CN19) is one matrix element of the actual interacting reduced resolvent. Its nonnegativity does not give a fixed sign for the total curvature, and a single source need not overlap the lowest excitation.

Thus one specified homogeneous preparation change supplies both a raw normalization response and a vacuum response on the same returned theory. It does not reconstruct the whole spectrum from one derivative, select \(s\), or prove a homogeneous restoring mode. [[reciprocal-coefficients-and-the-field-gap-test|The field-gap test]] shows separately why reciprocal coefficients alone retain soft quadratic modes in large volume. A cosmological application still needs the physical homogeneous map and its geometric normalization.

## Conjecture: one joint normalization has cosmic and local returns

**Conjecture.** A unit-compatible algebraic evaluation selects the marked joint determinant–Schur datum, including its physical closed normalization. Its local return reconstructs the complete gauge-invariant vacuum response, while its homogeneous return reconstructs central scale response and state geometry. Their transported mixed variations obey the common-source identities before and after the required limits.

The joint datum is essential: the Schur response alone omits the mode in (CN6), while the unmarked determinant omits how modes couple to local observables. The conjecture extends [[determinant-response-sewing-and-relational-rigidity|determinant–response sewing]] beyond a proposed identification with one Schur derivative. It does not identify the determinant action Hessian, the Gaussian Fisher metric and the harmonic-lift norm without a derived comparison.

A cosmic vacuum or gravitational coefficient would require a constructed homogeneous source, its physical state and observable return, and control of the closed normalization through refinement. A local mass statement requires the complete physical spectral measure and the translation/Poincaré return. No Hubble parameter is inserted to create its edge. The finite formulas establish a common generating mechanism; selection of its algebraic law and both physical returns remains open.
