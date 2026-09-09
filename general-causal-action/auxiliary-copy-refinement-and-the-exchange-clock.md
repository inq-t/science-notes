# Auxiliary Copy Refinement and the Exchange Clock

The determinant's many-copy Wilson return does not preserve its conditional-exchange clock. The frame interaction stays finite when \(\nu r^4\) stays finite, while the auxiliaries learn individual links with information of order \(\nu r^2\). A neutral plaquette source consequently has exchange response \(O(r^2)\), even on one fixed graph whose frame law approaches a nontrivial Wilson law. Its actual joint-boundary recovery defect also loses a uniform floor at fixed exchange duration. This is a discriminator for the declared cut protocol and clock convention, not a statement about the physical Yang–Mills spectrum.

## Keep the complete joint law and the actual link cut

Use [[determinant-response-sewing-and-relational-rigidity|DS3 and DS10a–c]] on a fixed finite open hypercubic graph of dimension \(D\ge2\) containing a plaquette. Let \(N=d_\rho\), take a faithful unitary representation \(\rho:G\to U(N)\), and use constant edge weights
\[
w=(2D)^{-1},\qquad Q_U=I-rP_U,\quad 0<r<1.
\tag{AC1}
\]
The graph is bipartite. In the block convention of DS3,
\((P_U)_{xy}=w\rho(U_{xy})\), with \(U_{yx}=U_{xy}^{-1}\).
The normalized joint probability is
\[
d\widehat\mu_{\nu,r}(U,\Xi)
=\widehat Z_{\nu,r}^{-1}
\exp\!\left[-\sum_{a=1}^{\nu}\xi^{(a)\dagger}Q_U\xi^{(a)}\right]
\prod_e dU_e\prod_{a,v}\frac{d^{2N}\xi_v^{(a)}}{\pi^N}.
\tag{AC2}
\]
Its frame marginal is
\(\mu_{\nu,r}(dU)\propto(\det Q_U)^{-\nu}\prod_e dU_e\).
Conditional on the incoming frame configuration,
\[
\xi^{(a)}\mid U\ \stackrel{\mathrm{iid}}{\sim}\
\operatorname{CN}(0,C_U),\qquad C_U=Q_U^{-1}.
\tag{AC3}
\]
In particular the conditional Gaussian density has normalization
\((\det Q_U)^\nu\). The copies share \(U\); they are independent only conditional on it.

For one primitive link cut \(e=\{x,y\}\), take the retained readout
\[
\eta_e=(U_{e^c},\Xi).
\]
It retains the outside frames and the full auxiliary preparation. Only the endpoint auxiliary values are needed by the estimator below. Let
\[
C_ef=\mathbb E[f(U)\mid\eta_e],\qquad
T_e=C_e^*C_e,\qquad L_{\nu,r}=\sum_e(I-T_e).
\tag{AC4}
\]
The sum assigns one rate to each physical link cut, as prescribed by DS10b; it is not divided by the number of links.

The conditional resampling is explicit. With
\[
J_e=\sum_{a=1}^{\nu}\xi_y^{(a)}\xi_x^{(a)\dagger},
\]
the outgoing link has Haar density
\[
\boxed{\quad
h_e(V\mid\Xi)
=\frac{\exp[\,2rw\operatorname{Re}\operatorname{Tr}(\rho(V)J_e)\,]}
{\displaystyle\int_G\exp[\,2rw\operatorname{Re}\operatorname{Tr}(\rho(W)J_e)\,]\,dW}.
\quad}
\tag{AC5}
\]
Both orientations of the edge supply the factor two. The other link values do not appear explicitly after all auxiliary values have been fixed. They still affect the first draw (AC3). The denominator in (AC5) is retained, not replaced by a Gaussian or by the determinant normalization.

One exchange draws a fresh full \(\Xi\) by (AC3), retains it during the cut resampling, and then averages it out. Successive exchanges repeat that procedure. Retaining the same auxiliary samples permanently would define a different process; the result below already holds with fresh conditional preparations.

## The auxiliaries estimate a link before its cycle action survives

Define the matrix-valued readout
\[
\widehat A_e
=\frac1{\nu rw}\sum_{a=1}^{\nu}
\xi_x^{(a)}\xi_y^{(a)\dagger}
=\frac{J_e^\dagger}{\nu rw}.
\tag{AC6}
\]
It is measurable from the actual endpoint preparation data. Conditional on \(U\),
\(\mathbb E\widehat A_e=(C_U)_{xy}/(rw)\).
Bipartiteness removes every even power from this off-diagonal block of the Neumann series. Since \(\|P_U\|\le1\),
\[
(C_U)_{xy}=rw\rho(U_{xy})+\sum_{m\ge1}r^{2m+1}(P_U^{2m+1})_{xy},
\]
\[
\left\|\mathbb E[\widehat A_e\mid U]-\rho(U_{xy})\right\|_{\rm HS}^2
\le\frac{Nr^4}{w^2(1-r^2)^2}.
\tag{AC7}
\]
This is a uniform configuration bound on the bias.

Complex Gaussian Wick contraction gives the exact one-copy identity
\[
\mathbb E\left[
\|\xi_x\xi_y^\dagger-(C_U)_{xy}\|_{\rm HS}^2\mid U\right]
=\operatorname{Tr}(C_U)_{xx}\operatorname{Tr}(C_U)_{yy}.
\]
Indeed, in each entry the connected fourth moment is
\((C_U)_{xx,ii}(C_U)_{yy,jj}\). Independence of the copies and
\(\|C_U\|\le(1-r)^{-1}\) therefore give
\[
\mathbb E\left[
\|\widehat A_e-\mathbb E[\widehat A_e\mid U]\|_{\rm HS}^2\mid U\right]
\le\frac{N^2}{\nu r^2w^2(1-r)^2}.
\]
Variance and squared bias add without a cross term:
\[
\boxed{\quad
\mathbb E\left[\|\widehat A_e-\rho(U_{xy})\|_{\rm HS}^2\mid U\right]
\le
\frac{N^2}{\nu r^2w^2(1-r)^2}
+\frac{Nr^4}{w^2(1-r^2)^2}.
\quad}
\tag{AC8}
\]
The leading information scale is \(\nu r^2w^2\), not the plaquette scale \(\nu r^4w^4\). No estimate of the physical Hamiltonian enters this statement.

The estimator has the correct boundary covariance:
\(\widehat A_{xy}\mapsto\rho(g_x)\widehat A_{xy}\rho(g_y)^\dagger\).
It need not lie in \(\rho(G)\). No projection onto that group is required for the following linear Wilson source.

## A complete neutral source has vanishing exchange response

For a plaquette \(p\), use the bounded neutral source
\[
F(U)=\frac1N\operatorname{Re}\chi_\rho(U_p).
\tag{AC9}
\]
Every link occurs once in this word. For an edge \(e\in p\), cyclicity of trace writes
\[
F(U)=\frac1N\operatorname{Re}\operatorname{Tr}
[\rho(U_e)W_e(U_{e^c})],
\]
where \(W_e\) is unitary; if the orientation is reversed, use
\(\rho(U_e)^\dagger\) instead. Replace that one factor by \(\widehat A_e\), or its adjoint, to obtain an estimator \(\widehat F_e(\eta_e)\). It is square integrable by (AC8). Hilbert–Schmidt Cauchy–Schwarz gives
\[
|F-\widehat F_e|^2
\le N^{-1}\|\rho(U_e)-\widehat A_e\|_{\rm HS}^2 .
\]
Conditional expectation is the best square-integrable estimator. Hence the exact DS response satisfies
\[
\boxed{\quad
\mathbb E\operatorname{Var}(F\mid\eta_e)
\le\mathbb E|F-\widehat F_e|^2
\le B_{\nu,r}:=
\frac{N}{\nu r^2w^2(1-r)^2}
+\frac{r^4}{w^2(1-r^2)^2}.
\quad}
\tag{AC10}
\]
Keeping additional data can only decrease this conditional variance. The same upper bound therefore holds for any cut readout containing the outside frames and these endpoint copies. It is not asserted for a protocol that discards those copies before resampling.

If \(e\notin p\), the readout \(U_{e^c}\) already contains \(F\), so its conditional variance is zero. Summing the four active cuts yields
\[
\langle F,L_{\nu,r}F\rangle_{\mu_{\nu,r}}
\le4B_{\nu,r}.
\tag{AC11}
\]
This tests a neutral configuration observable on the selected frame carrier. It is neither a color-vector test nor an auxiliary-only score.

At every finite \(\nu,r\), the full invariant space of (AC4) is exactly the constants. To see this, the density (AC5) has full support on \(G\) for every finite preparation. Zero conditional variance forces a frame function to be independent of \(U_e\) at fixed outside frames. The strictly positive joint density and Fubini make this an almost-everywhere statement for product Haar. Repeating it for every edge leaves only constants. Thus
\[
\ker L_{\nu,r}=\mathbb C1
\tag{AC12}
\]
on the complete frame carrier and on its neutral restriction. This kernel argument does not provide a uniform positive lower bound.

## The Wilson state remains nontrivial while the clock freezes

Choose the fixed-positive-coupling path in [[cycle-determinants-and-the-pure-gauge-return|CY6–8]]:
\[
r=r_\nu\longrightarrow0,\qquad
b_\nu=2\nu r_\nu^4w^4\longrightarrow b\in(0,\infty).
\tag{AC13}
\]
On this fixed graph, the determinant's longer-walk remainder is
\(O(\nu r_\nu^6)=O(r_\nu^2)\). Consequently
\[
\mu_{\nu,r_\nu}\longrightarrow
\mu_{W,b}:=Z_{W,b}^{-1}
e^{-b\sum_p[N-\operatorname{Re}\chi_\rho(U_p)]}\prod_e dU_e
\quad\text{in total variation}.
\tag{AC14}
\]
No physical time direction or quantum vacuum has been supplied by this convergence.

Faithfulness and the existence of the tested plaquette make \(F\) nonconstant. The limiting finite Wilson density is strictly positive, so
\[
v_\nu:=\operatorname{Var}_{\mu_{\nu,r_\nu}}F
\longrightarrow v_b:=\operatorname{Var}_{\mu_{W,b}}F>0.
\]
Define the complete neutral unit vector
\[
f_\nu=\frac{F-\mu_{\nu,r_\nu}F}{\sqrt{v_\nu}}.
\tag{AC15}
\]
Its definition is a centered source test, not a spectral definition of the comparison operator.

The exact coupling relation rewrites the first term in (AC10) as
\[
\frac{N}{\nu r_\nu^2w^2(1-r_\nu)^2}
=\frac{2Nr_\nu^2w^2}{b_\nu(1-r_\nu)^2}.
\]
Therefore
\[
\boxed{\quad
\langle f_\nu,L_{\nu,r_\nu}f_\nu\rangle
\le\frac4{v_\nu}
\left[
\frac{2Nr_\nu^2w^2}{b_\nu(1-r_\nu)^2}
+\frac{r_\nu^4}{w^2(1-r_\nu^2)^2}
\right]
=O(r_\nu^2)\longrightarrow0 .
\quad}
\tag{AC16}
\]
Together with (AC12), this excludes a regulator-uniform vacuum-complement floor for the equal-rate comparison clock along this admitted copy refinement. Its lower edge above the entire invariant space is at most the displayed Rayleigh quotient. A fixed positive finite-word certificate implying that edge cannot survive unchanged.

The mechanism is specific to the selected joint law: many weak auxiliary comparisons preserve a finite cycle interaction, but jointly retain an increasingly accurate record of each incoming link. Conditional exchange has little uncertainty left to resample. Increasing auxiliary multiplicity is not merely another representation of the same processed experiment, even when the frame marginal has the same limit.

## Fixed-slab recovery and the clock calibration

Take the stationary reversible process generated by \(L_{\nu,r_\nu}\), with a fresh conditional preparation at every cut occurrence. At fixed slab half-width \(\ell>0\), define its actual QD boundary defect
\[
R_{\nu,\ell}=J_\nu^*(I-P_{\partial,\nu})J_\nu,
\qquad J_\nu f=f(U_0),
\]
where \(P_{\partial,\nu}\) conditions on the joint frames at times
\(-\ell,+\ell\). The one-boundary comparison used in [[commutator-word-comparisons-and-neutral-soft-escape|NW11–13]] gives
\[
0\le R_{\nu,\ell}\le I-e^{-2\ell L_{\nu,r_\nu}}
\le2\ell L_{\nu,r_\nu}.
\]
In particular
\[
\boxed{\langle f_\nu,R_{\nu,\ell}f_\nu\rangle
=O(\ell r_\nu^2)\longrightarrow0
\quad\text{for fixed }\ell.}
\tag{AC17}
\]
This uses the actual selected exchange process, not the unrelated slab law of a pre-existing lattice Hamiltonian.

The frame probability \(\mu_{\nu,r}\) is not thereby the old interacting quantum vacuum. Its conditional-exchange generator is not automatically Yang–Mills time translation. Equation (AC14) identifies finite configuration laws; it identifies neither quantum ground vectors nor clocks.

If a common physical duration \(\tau_\nu\) per exchange is introduced, the rescaled candidate is \(L_{\nu,r_\nu}/\tau_\nu\). Equation (AC16) forces \(\tau_\nu=O(r_\nu^2)\) as a necessary condition for a nonclosing positive bound on this particular normalized source. A duration bounded below cannot work. This is only a necessary calibration constraint: accelerating by order \(\nu r_\nu^2\) does not itself prove a limiting diffusion, its coefficient, ultraviolet behavior or a physical energy interpretation.

The same diverging information scale is visible in the complete auxiliary score. Differentiate the conditional Gaussian law (AC3) in a left edge direction \(U_e(t)=e^{tX}U_e\), holding the actual auxiliary coordinates fixed. Define \(Q_\rho(X,Y)=-\operatorname{Re}\operatorname{Tr}[d\rho(X)d\rho(Y)]\), with its induced norm, and put \(Q_X=\partial_XQ_U\). Then
\[
\mathscr S_X=\nu\operatorname{Tr}(C_UQ_X)
-\sum_a\xi^{(a)\dagger}Q_X\xi^{(a)},\qquad
\mathcal I_e(X,Y)=\mathbb E[\mathscr S_X\mathscr S_Y\mid U]
=\nu\operatorname{Tr}(C_UQ_XC_UQ_Y).
\tag{AC18}
\]
There is no extra real-Gaussian factor of two in this complex Gaussian covariance formula. The two orientations of the differentiated edge instead give
\(\operatorname{Tr}(Q_XQ_Y)=2r^2w^2Q_\rho(X,Y)\).
In the Neumann expansion of (AC18), odd total powers of \(P_U\) have zero trace by bipartiteness. Hilbert–Schmidt Cauchy–Schwarz bounds the remaining terms and yields
\[
\boxed{\quad
\mathcal I_e(X,Y)=2\nu r^2w^2Q_\rho(X,Y)+\mathcal R_e(X,Y),\qquad
|\mathcal R_e(X,Y)|
\le
\frac{2\nu r^4w^2(3-r^2)}{(1-r^2)^2}
\|X\|_{Q_\rho}\|Y\|_{Q_\rho}.
\quad}
\tag{AC19}
\]
Indeed, \(\|Q_X\|_{\rm HS}^2=2r^2w^2\|X\|_{Q_\rho}^2\), and the relevant sum is
\(\sum_{j\ge1}(2j+1)r^{2j}=r^2(3-r^2)/(1-r^2)^2\).
Thus along (AC13) the auxiliary Fisher information diverges while the induced Wilson interaction remains finite. Equivalently, an acceleration \(a_\nu\) with \(a_\nu/(\nu r_\nu^2)\to0\) still has vanishing response on (AC15). A fixed positive physical floor would require \(a_\nu\gtrsim\nu r_\nu^2\); this necessary rate constraint is not a sufficiency theorem.

The estimator argument also applies to compact Abelian representations. It does not establish a Maxwell continuum law or require an Abelian finite regulator to be gapless. It shows that this copy-induced freezing is not a specifically non-Abelian rigidity mechanism.

The active proposal must now decide whether its primitive evaluation and cut rule select a duration scaling, discard or coarsen part of this auxiliary record, or exclude this copy-refinement path for a stated reason. Each choice changes a precise constitutive datum. A Wilson marginal alone cannot justify treating the induced state and the exchange mobility as independently fixed outputs.
