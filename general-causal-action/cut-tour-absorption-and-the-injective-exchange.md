# Cut Tour Absorption and the Injective Exchange

A finite composition relation can supply an explicit bounded repair without inserting a vacuum projector. If a prescribed bounded-depth tour of positive cut exchanges is idempotent, its telescoping defect reconstructs every distinction outside the common fixed space with a uniform constant. The actual determinant auxiliary exchanges fail this proposed relation: once enough faithful auxiliary columns are retained, each exchange is injective, so a nontrivial finite tour cannot be idempotent. This tests a specific algebraic source of rigidity rather than assuming an inverse gap.

## A finite word can select its own fixed-space projection

Let \(T_p\) be positive self-adjoint contractions on one Hilbert carrier, with explicitly supplied comparison maps
\[
\delta_p^*\delta_p=I-T_p,\qquad
\delta f=(\delta_pf)_p,\qquad
R=\delta^*\delta=\sum_p(I-T_p).
\tag{CT1}
\]
For [[determinant-response-sewing-and-relational-rigidity#Conditional boundary exchange and its clock test|DS conditional exchanges]], take \(\delta_p=(I-E_{\eta_p})J\), where \(J\) pulls frame observables into the complete joint law and \(E_{\eta_p}\) is its actual conditional-expectation projection. Then (CT1) is exactly DS10c.

Partition the finite primitive-cut list into \(m\) layers \(\mathcal L_a\), assuming the \(T_p\) commute within each layer. Form
\[
S_a=\prod_{p\in\mathcal L_a}T_p,\qquad
W=S_m\cdots S_1.
\tag{CT2}
\]
The additional candidate relation is
\[
\boxed{W^2=W.}
\tag{CT3}
\]
It says that repeating this prescribed completed tour adds no further processing. It does not follow from associative integration of a fixed amplitude. Layer commutation and the tour itself are also data to prove or postulate; geometrically disjoint raw links need not commute after a shared auxiliary preparation has been integrated.

A contractive idempotent on a Hilbert space is an orthogonal projection. If \(Wv=v\), the contraction inequalities along every factor in the tour are equalities. For a positive contraction \(T\), \(\|Tv\|=\|v\|\) implies \(Tv=v\), by positivity of \(I-T^2\). Applying this successively shows
\[
\operatorname{Ran}W=\bigcap_p\operatorname{Fix}T_p=\ker R.
\tag{CT4}
\]
The common fixed space is an output of the word relation, not a supplied projector. Its identification with a physical vacuum is a further test.

## The repair is assembled from the actual comparisons

Order the cuts within layer \(a\) and let \(A_p\) be the product of factors preceding \(p\), with the empty product equal to \(I\). Define
\[
B_a(\zeta_p)_{p\in\mathcal L_a}
=\sum_{p\in\mathcal L_a}A_p\delta_p^*\zeta_p.
\tag{CT5}
\]
Commutation within the layer makes the prefixes positive contractions and gives
\[
B_a\delta_{\mathcal L_a}=I-S_a,
\]
\[
B_aB_a^*
=\sum_p A_p^2(I-T_p)
\le\sum_p A_p(I-T_p)=I-S_a\le I.
\tag{CT6}
\]
Thus the norm of each layer repair is at most one, independent of its number of cuts. On the direct sum of all layer discrepancy spaces, put
\[
B(\zeta_a)_{a=1}^m
=\sum_{a=1}^m S_m\cdots S_{a+1}B_a\zeta_a.
\tag{CT7}
\]
Telescoping and Cauchy–Schwarz prove
\[
B\delta=I-W,\qquad \|B\|\le\sqrt m.
\]
Under (CT3)–(CT4), this yields the exact conditional theorem
\[
\boxed{R\ge\frac1m(I-W).}
\tag{CT8}
\]
The bound survives a growing cut count if the number of layers stays bounded and the same comparison norms and primitive-cut weighting are retained. No inverse of \(R\), spectral square root of a desired certificate, or vacuum projector defines \(B\). This is a concrete instance of [[global-local-response-reconstruction/quantitative-descent-and-the-shape-of-a-gap|QD7–8's bounded repair]]. The substantive new premise is the independently testable finite-word relation (CT3).

## The sharpening family rejects the word relation

In [[global-local-response-reconstruction/quantitative-descent-and-the-shape-of-a-gap|QD6a–c]], use the two conditional projections \(P_x,P_y\), with fundamental overlap multiplier \(b_k\in(0,1)\). The neutral source \(\chi_1(y)\) has norm one and satisfies
\[
P_yP_x\chi_1(y)=b_k^4\chi_1(y),
\]
\[
\langle\chi_1(y),(W-W^2)\chi_1(y)\rangle
=b_k^4(1-b_k^4)>0,
\qquad W=P_yP_x.
\tag{CT9}
\]
Thus this particular tour is not idempotent at any finite positive sharpening parameter. As \(k\to\infty\), the displayed idempotence defect tends to zero while the comparison gap also closes. Small idempotence error by itself cannot distinguish a direction nearly erased by \(W\) from an extra direction nearly fixed by \(W\). The exact relation cannot be replaced by an unqualified approximate one.

The [[commutator-word-comparisons-and-neutral-soft-escape|neutral flat-bump construction]] is another control. Every fixed finite tour of its small word moves or fixed-time positive averages nearly fixes those centered bumps. An idempotent tour whose range were only the vacuum would annihilate them. The two claims cannot hold together for that law.

## The actual Gaussian exchange is injective

Consider the raw-link DS preparation on a finite graph. Let \(\rho:G\to U(n)\) be faithful, \(0<r<1\), and let the tested link \(e:v\to w\) have distinct endpoints and \(w_e>0\). Retain all other links and all auxiliary endpoint vectors, with \(\nu\ge n\) copies. The selected exchange resamples only \(U_e\).

At fixed retained data, its conditional link density is
\[
\frac{\exp\{2rw_e\operatorname{Re}\operatorname{Tr}[\rho(h)J_e]\}}{z_e(J_e)}\,dh,
\qquad
J_e=\sum_{a=1}^{\nu}\xi_w^{(a)}\xi_v^{(a)*},
\tag{CT10}
\]
where \(z_e\) is the actual positive Haar row integral. This follows directly from the two oriented off-diagonal blocks of \(Q_U=I-rP_U\); it is also the explicit link law in [[conditional-exchange-through-cuts-and-retained-marks|the sourced cut calculation]]. Other Gaussian and frame factors cancel from this conditional density, rather than being reset.

**Injectivity theorem.** On the full frame \(L^2(\mu_D)\) carrier, and hence on its invariant subspace, the conditional map \(C_e\) is injective. Consequently \(T_e=C_e^*C_e\) is injective.

Fix almost every outside configuration for which the disintegrated frame function \(f(h)\) is integrable. The determinant marginal is continuous and strictly positive on the compact frame product, so this follows for every \(f\in L^2(\mu_D)\). If \(C_ef=0\), multiplying its conditional expectation by \(z_e(J_e)>0\) gives
\[
\int_G f(h)
\exp\{2rw_e\operatorname{Re}\operatorname{Tr}[\rho(h)J_e]\}\,dh=0
\tag{CT11}
\]
for almost every auxiliary tuple. Its conditional density is positive everywhere because the joint Gaussian precision is strictly positive. The left side is continuous, indeed real analytic, in the endpoint variables, so it vanishes for all endpoint tuples.

With \(\nu\ge n\), \(J_e\) ranges over all \(M_n(\mathbb C)\): the first \(n\) columns at \(v\) can be the identity and the corresponding columns at \(w\) any chosen matrix, with other columns zero. Therefore (CT11) holds for every complex matrix parameter. Differentiating at zero gives the integral of \(f\) against every polynomial in the real and imaginary parts of the matrix entries of \(\rho(h)\). These polynomials contain constants, are closed under conjugation, and separate points because \(\rho\) is faithful. The same [[prepared-readout-algebra-and-physical-source-completeness|Stone–Weierstrass source argument]] used by RA makes them dense in \(C(G)\). The finite measure \(f(h)dh\) is therefore zero. Applying this on almost every outside fiber proves \(C_ef=0\Rightarrow f=0\).

The proof keeps the entire endpoint preparation. Coarsening that data can create a kernel and is a different comparison law. At zero hopping the conditional density is Haar and injectivity generally fails; for a self-loop the endpoint matrices cannot vary independently. Neither case is covered by this theorem. The sufficient copy count is not claimed optimal. The many-copy Wilson return lies within its scope.

## Exact absorption is incompatible with nontrivial DS exchanges

A finite product of injective operators is injective. An injective idempotent \(W\) obeys \(W(W-I)=0\), hence \(W=I\). If a finite product of positive contractions equals \(I\), the same norm-equality argument forces every factor to be \(I\).

But a DS link exchange is not the identity when the tested neutral source is nonconstant on the resampled link fiber. On a simple detected cycle containing \(e\), its Wilson character supplies such a source: the conditional density (CT10) has full support, so its conditional variance is strictly positive. Thus a tour containing these nontrivial cycle-link exchanges cannot satisfy (CT3), on the actual neutral carrier as well as on the full frame carrier.

The finite-tour absorption conjecture is therefore rejected for this version of the selected determinant law. No calibration of its pace repairs this exact algebraic failure. This does not refute every finite-word certificate, every bounded repair, or the existence of a gap for a particular finite DS generator. It identifies an additional relation that the actual comparison maps do not satisfy, even though the same relation would have supplied the desired constructive repair if true.
