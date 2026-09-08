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

## Conjecture: one joint normalization has cosmic and local returns

**Conjecture.** A unit-compatible algebraic evaluation selects the marked joint determinant–Schur datum, including its physical closed normalization. Its local return reconstructs the complete gauge-invariant vacuum response, while its homogeneous return reconstructs central scale response and state geometry. Their transported mixed variations obey the common-source identities before and after the required limits.

The joint datum is essential: the Schur response alone omits the mode in (CN6), while the unmarked determinant omits how modes couple to local observables. The conjecture extends [[determinant-response-sewing-and-relational-rigidity|determinant–response sewing]] beyond a proposed identification with one Schur derivative. It does not identify the determinant action Hessian, the Gaussian Fisher metric and the harmonic-lift norm without a derived comparison.

A cosmic vacuum or gravitational coefficient would require a constructed homogeneous source, its physical state and observable return, and control of the closed normalization through refinement. A local mass statement requires the complete physical spectral measure and the translation/Poincaré return. No Hubble parameter is inserted to create its edge. The finite formulas establish a common generating mechanism; selection of its algebraic law and both physical returns remains open.
