# Prepared Readout Algebra and Physical Source Completeness

Quadratic cross marks on an actual transported preparation recover every matrix entry of the declared faithful group representation. Their generated multiplication algebra is dense on a finite link graph; joint gauge averaging then gives a dense physical source algebra. The reconstruction is exact with the free finite-width row posterior and survives temporal localization. This closes the finite-graph source-completeness step in the susceptibility criterion, while leaving the source response bounds, compatible growing preparation law and continuum return open.

## The exact row posterior supplies an invertible calibration

Use one link of [[local-incidence-preparations-and-the-gauge-transfer|the general-group incidence construction]], with normalized Haar measure. Let \(\rho:G\to U(n)\) be faithful, \(\Xi\in E=\mathbb C^{n\times k}\) have independent circular complex entries of variance \(\sigma^2>0\), and use unnormalized Hilbert–Schmidt norm. Fix \(r,\alpha>0\). Write
\[
B_\rho(h)=2I-\rho(h)-\rho(h)^\dagger,\qquad
\zeta_\alpha(\Xi)=
\int_G e^{-(\alpha/r)\|[I-\rho(h)]\Xi\|^2}\,dh,
\]
\[
z_\alpha=\mathbb E\zeta_\alpha,\qquad
dP_\alpha(\Xi)=\frac{\zeta_\alpha(\Xi)}{z_\alpha}\,dP(\Xi),
\qquad A_\alpha=\mathbb E_{P_\alpha}\Xi\Xi^\dagger.
\tag{RA1}
\]
This is the actual free preparation law after integrating the neighboring temporal frame. It is independent of the retained \(g\): in the comparison with \(g'\), substitute \(h=g^{-1}g'\). \(P_\alpha\) is generally not Gaussian.

At fixed \(h\), the conditional columns are Gaussian with covariance
\((\sigma^{-2}I+(\alpha/r)B_\rho(h))^{-1}\).
The normalized \(h\)-mixture therefore gives
\[
\frac{k}{\sigma^{-2}+4\alpha/r}I
\le A_\alpha\le k\sigma^2I,\qquad A_\alpha>0.
\tag{RA2}
\]
Here \(0\le B_\rho(h)\le4I\). Conjugating \(h\) and left-translating \(\Xi\) show that \(P_\alpha\) is invariant under \(\Xi\mapsto\rho(a)\Xi\). Consequently \(A_\alpha\) commutes with \(\rho(G)\). These bounds are finite-width statements; their displayed lower bound is not uniform in \(\alpha\).

Under the sufficient inventory \(k>n+\dim G/2\), the polynomially weighted localization proof of [[general-group-preparation-and-the-casimir-return|the general-group owner]] gives
\[
P_\alpha\longrightarrow P_\infty,\qquad
dP_\infty=\frac{(\det_Qg_\Xi)^{-1/2}dP}
{\mathbb E(\det_Qg_\Xi)^{-1/2}},\qquad
A_\alpha\longrightarrow\overline A
:=\mathbb E_{P_\infty}\Xi\Xi^\dagger>0.
\tag{RA3}
\]
The first convergence holds against bounded continuous tests, and also against the required quadratic tests. Full row rank almost surely and the positive weight prove strict positivity of \(\overline A\); the moment theorem proves finiteness. It commutes with \(\rho(G)\), including for faithful reducible representations. In the irreducible case it is the explicit scalar \(\sigma^2(nk-\dim G/2)I/n\).

## Actual cross marks return the faithful matrix entries

Keep the terminal preparation and its transported row together:
\[
Y_1=\rho(g)\Xi,\qquad Y_0=\Xi,\qquad
q_C(g,\Xi)=\operatorname{Re}\operatorname{Tr}(C^\dagger Y_1Y_0^\dagger),
\quad C\in M_n(\mathbb C).
\tag{RA4}
\]
This is a permitted Hermitian quadratic mark on the pair \(E\oplus E\). With columns stacked, its source matrix is
\[
\mathcal T_C=\frac12
\begin{pmatrix}0&I_k\otimes C\\I_k\otimes C^\dagger&0\end{pmatrix},
\qquad
q_C=\langle(Y_1,Y_0),\mathcal T_C(Y_1,Y_0)\rangle.
\tag{RA5}
\]
Indeed the two off-diagonal terms are conjugates. Thus real and imaginary matrix components are available using real Hermitian source directions; no non-Hermitian probability weight is required.

Normalize by the original unmarked \(z_\alpha\) and set
\[
\mathcal Z_{\alpha,C}(g,t)=\mathbb E_{P_\alpha}e^{-tq_C(g,\Xi)}.
\]
This is the row-integrated marked Gaussian amplitude. More explicitly, with
\(H_C(g)=[\rho(g)^\dagger C+C^\dagger\rho(g)]/2\),
\[
\mathcal Z_{\alpha,C}(g,t)=\frac1{z_\alpha}
\int_G\det\!\left[I+\sigma^2\{(\alpha/r)B_\rho(h)+tH_C(g)\}\right]^{-k}dh.
\tag{RA6}
\]
For real \(t\) in a neighborhood of zero, the precision is uniformly positive because \(\|H_C(g)\|\le\|C\|\). Differentiating at zero is justified by Gaussian moments. Since \(\mathcal Z_{\alpha,C}(g,0)=1\),
\[
-\left.\partial_t\log\mathcal Z_{\alpha,C}(g,t)\right|_0
=\mathbb E_{P_\alpha}q_C
=\operatorname{Re}\operatorname{Tr}[C^\dagger\rho(g)A_\alpha].
\tag{RA7}
\]
Equivalently, the matrix of these first cross-source jets is
\[
\boxed{M_\alpha(g)=\mathbb E_{P_\alpha}(Y_1Y_0^\dagger)
=\rho(g)A_\alpha,\qquad
M_\alpha(g)A_\alpha^{-1}=\rho(g).}
\tag{RA8}
\]
For matrix units \(E_{ij}\), choosing \(C=E_{ij}A_\alpha^{-1}\) gives \(\operatorname{Re}\rho(g)_{ij}\); choosing \(C=iE_{ij}A_\alpha^{-1}\) gives \(\operatorname{Im}\rho(g)_{ij}\). This is an exact source calibration, not a fit to a desired vacuum or spectral gap. Replacing \(A_\alpha,P_\alpha\) by \(\overline A,P_\infty\) gives the same reconstruction after localization.

The rows retain their two ports. Under \(g\mapsto h_sgh_t^{-1}\) and \(\Xi\mapsto\rho(h_t)\Xi\), they transform as \(Y_1\mapsto\rho(h_s)Y_1\), \(Y_0\mapsto\rho(h_t)Y_0\). Transport \(C\mapsto\rho(h_s)C\rho(h_t)^\dagger\); its pairing stays unchanged. Commutation of \(A_\alpha\) with the terminal representation makes (RA8) transform exactly as the original link matrix. Averaging either charged row separately before pairing it with other rows would change this experiment.

## Multiply the returned functions and then impose the whole Gauss law

For a finite link set \(\mathcal E\), let \(\mathscr P\) be the unital complex algebra generated pointwise by all returned entries \(\rho(g_e)_{ij}\) and their complex conjugates. It is closed under conjugation and separates points of \(G^{\mathcal E}\), since \(\rho\) is faithful. The complex Stone–Weierstrass theorem therefore gives
\[
\overline{\mathscr P}^{\,\|\cdot\|_\infty}=C(G^{\mathcal E}).
\tag{RA9}
\]
This uses the stated finite representation to realize the familiar matrix-coefficient density theorem; it is not a new approximation theorem.

Let \(\mathcal G=G^{\mathcal V}\) be the actual vertex gauge group and average jointly:
\[
(\mathsf Gp)(g)=\int_{\mathcal G}p(h\cdot g)\,dh,\qquad
\mathscr P_{\rm phys}=\mathsf G\mathscr P=\mathscr P^{\mathcal G}.
\tag{RA10}
\]
The average remains a polynomial: the gauge orbit of any fixed-degree matrix-coefficient polynomial lies in a finite-dimensional coefficient space. If \(F\) is continuous and invariant, approximate it uniformly by \(p\); then
\(\|\mathsf Gp-F\|_\infty\le\|p-F\|_\infty\).
Hence
\[
\boxed{\overline{\mathscr P_{\rm phys}}^{\,\|\cdot\|_\infty}
=C(G^{\mathcal E})^{\mathcal G}.}
\tag{RA11}
\]
Products of invariant polynomials remain invariant polynomials. All shared vertex actions are imposed together, preserving the boundary-charge pairing of [[gauge-boundary-frame-gluing/inq|finite Gauss gluing]]. The real self-adjoint part is dense in the real continuous physical functions and thus in the actual vacuum \(L^2\) carrier. The latter statement uses the returned \(\psi_0^2d\mu_{\rm Haar}\), not the preparation posterior \(P_\alpha\).

Multiplication in \(\mathscr P\) is multiplication of the returned frame functions. Gaussian averaging has not become multiplicative:
\[
\mathbb E_{P_\alpha}(q_Cq_D)
=\mathbb E_{P_\alpha}q_C\,\mathbb E_{P_\alpha}q_D
+\operatorname{Cov}_{P_\alpha}(q_C,q_D).
\tag{RA12}
\]
At \(g=e\), \(C=D=I\), the covariance is the strictly positive variance of \(\|\Xi\|^2\). Thus higher same-preparation source jets retain additional correlations; they are not automatically products in the physical multiplication algebra.

## Insert those physical sources into the returned evolution

Let \(F_\alpha\) be the interacting transfers of the incidence owner, with their original free normalization and strong product return \(e^{-tH}\). Every real \(F\in\mathscr P_{\rm phys}\) is smooth and bounded. Define the physical multiplication insertion
\[
G_{\alpha,\theta}
=M_{\exp[\theta F/(2\alpha)]}\,
F_\alpha\,
M_{\exp[\theta F/(2\alpha)]},
\qquad \theta\in\mathbb R.
\tag{RA13}
\]
Keep the original scalar normalizations. The resulting operator is positive and self-adjoint, with
\(\|G_{\alpha,\theta}\|\le e^{|\theta|\|F\|_\infty/\alpha}\).
The existing smooth-core expansion, uniform on bounded smooth sets, gives
\[
\boxed{G_{\alpha,\theta}f
=f-\alpha^{-1}(H-\theta F)f+o_f(\alpha^{-1}),
\qquad
G_{N/t,\theta}^{\,N}\longrightarrow e^{-t(H-\theta F)}
\ \text{strongly}.}
\tag{RA14}
\]
The expansion is a smooth-core statement. Quasi-contractivity and telescoping along smooth semigroup orbits prove the product limit, uniformly on bounded nonnegative times at fixed graph and source. Finite real linear combinations of these \(F\)'s give the multi-source family in [[physical-response-coercivity/conditional-vacuum-rigidity-and-the-physical-gap|the complete-source susceptibility criterion]]. Constant source pieces retain their amplitude factors.

This constructs the physical source family after the preparation has returned its carrier and operator. It does not identify a fixed order-one Gaussian quadratic mark inside one integral with \(e^{-t(H-\theta F)}\). The first jets supply the algebra generators; pointwise closure supplies the bounded physical functions; (RA13) supplies their temporal insertion. These are distinct, specified steps.

Pure word subdivision preserves the actual returned functions under ordered multiplication and the source transport of [[preparation-transport-through-spatial-subdivision|the subdivision theorem]]. It creates no independent physical link-entry algebra on redundant fibers. At new access, the path pair \(A=U\), \(B=LU\) in [[conditional-preparation-sewing/conditional-preparation-extension-at-new-access|the conditional extension]] separates its complete internal-vertex quotient. Its joint row posterior has positive moment matrices for both \(\Xi\) and \(\Eta\); applying (RA8) to each row pair recovers \(\rho(A)\) and \(\rho(B)\), even when the preparations are correlated. The same density and joint gauge-averaging argument therefore applies there. A word inventory that does not separate its declared physical carrier would not meet this criterion.

The finite-graph source algebra is consequently constructed from these prepared readouts. What remains open is uniform control of all its mixed susceptibility blocks, compatible calibration and source transport through growing access diagrams, and the nontrivial continuum physical return. Finite algebraic density supplies no uniform approximation degree, response norm, or mass-gap constant.
