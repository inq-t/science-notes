# Local Incidence Preparations and the Gauge Transfer

One matrix preparation per declared link gives a positive transfer on any finite \(SU(2)\) graph. Each cell compares its holonomy with the identity using the preparations of its incident links, retaining the same variable wherever a link is shared. The continuum-time return is a gauge-invariant electric-plus-Wilson Hamiltonian with explicit coefficients. Localization remains a three-dimensional, rank-four calculation on each link as the graph grows. Graph incidence, preparation inventory, covariance, weights and duration remain inputs; the result supplies neither a refinement family nor a uniform continuum gap.

## Local preparations and actual cell words

Let \(\Lambda=(\mathcal V,\mathcal E,\mathcal C)\) be a finite oriented link graph with declared closed cell words. A configuration is \(g\in SU(2)^{\mathcal E}\), with normalized product Haar. The vertex action is \(g_e\mapsto h_{s(e)}g_eh_{t(e)}^{-1}\). For each cell \(c\), choose a base vertex \(v_c\), its actual word \(U_c(g)\), and
\[
V_c(g)=1-\tfrac12\operatorname{Tr}U_c(g)\ge0.
\tag{LI1}
\]
Give each link one independent circular complex Gaussian \(\Xi_e\in M_2(\mathbb C)\), with pairing \(\operatorname{Tr}(A^\dagger B)/2\), covariance \(\Gamma_e=\sigma_e^2I_4\), \(\sigma_e>0\), and \(S_e=\|\Xi_e\|^2\). Thus \(S_e\sim\operatorname{Gamma}(4,\sigma_e^2)\). The full preparation is \(\Xi\in\bigoplus_e M_2(\mathbb C)\), with block covariance \(\Gamma=\bigoplus_e\Gamma_e\) and the normalized complex Gaussian reference measure.

Choose \(w_{ce}\ge0\), supported on links occurring in cell \(c\), with \(\sum_e w_{ce}=1\), and strengths \(\beta_c\ge0\). These incidence weights are inputs. For each nonzero incidence choose a boundary path \(W_{ce}(g)\) from \(v_c\) to \(t(e)\). Its transported identity row is
\[
B_{ce}(g)\Xi_e=(U_c(g)-I)\operatorname{Ad}_{W_{ce}(g)}\Xi_e,
\qquad \|B_{ce}(g)\Xi_e\|^2=2V_c(g)S_e.
\tag{LI2}
\]
Transport \(\Xi_e\mapsto\operatorname{Ad}_{h_{t(e)}}\Xi_e\) under the vertex action. Then \(B_{ce}\Xi_e\) transforms by conjugation at \(v_c\), and \((g_e-g'_e)\Xi_e\) transforms by left multiplication at \(s(e)\) and inverse right multiplication at \(t(e)\). All norms and the isotropic prior are invariant. These are transformations of actual matrix readouts. The scalar in (LI2) is independent of the chosen transport path; marked readouts still retain that path and its transported sources.

Define the joint weak cell cost
\[
C(g,\Xi)=\sum_c\beta_cV_c(g)Y_c(\Xi),\qquad
Y_c=\sum_e w_{ce}S_e,
\qquad f_{\alpha,g}=e^{-C(g,\Xi)/(2\alpha)}.
\tag{LI3}
\]
In particular, two cells sharing link \(e\) use the same \(S_e\), and the same \(\Xi_e\) in their complete matrix rows. The cost equals \(\tfrac12\sum_{c,e}\beta_cw_{ce}\|B_{ce}\Xi_e\|^2\).

## Exact finite transfer and all Gaussian sources

Fix positive link comparison weights \(r_e\) and the duration \(1/\alpha\). Set
\[
d_e(g,g')^2=2\left[1-\tfrac12\operatorname{Tr}(g_e^{-1}g'_e)\right],
\]
\[
K_{\alpha,\beta}(g,g')=
\mathbb E\!\left[f_{\alpha,g}
\exp\!\left(-\alpha\sum_e r_e^{-1}S_ed_e(g,g')^2\right)
f_{\alpha,g'}\right].
\tag{LI4}
\]
The special \(SU(2)\) difference identity reduces every free edge comparison to \(S_ed_e^2\). Independence of the assigned link preparations gives
\[
K_{\alpha,\beta}(g,g')=
\prod_e(1+\sigma_e^2 h_e(g,g'))^{-4},
\quad
h_e=\frac\alpha{r_e}d_e^2+
\frac1{2\alpha}\sum_c\beta_cw_{ce}[V_c(g)+V_c(g')].
\tag{LI5}
\]
The cell words in \(h_e\) couple the link configurations. This product of preparation integrals is not a product of independent interacting cell laws.

For arbitrary joint linear source \(j\) and Hermitian quadratic source \(T\) on the whole preparation carrier, including off-diagonal link blocks, let
\[
A^{\alpha,T}_{g,g'}=\Gamma^{-1}+\bigoplus_e h_eI_4+T>0.
\]
Then
\[
\boxed{K_{\alpha,\beta}^{j,T}(g,g')=
\frac{\exp[j^\dagger(A^{\alpha,T}_{g,g'})^{-1}j]}
{\det\Gamma\,\det A^{\alpha,T}_{g,g'}}.}
\tag{LI6}
\]
The source insertion is \(e^{2\Re(j^\dagger\Xi)-\Xi^\dagger T\Xi}\). Sources on all transported cell rows, temporal difference rows and their joint outputs pull back to (LI6). The conditional covariance is \((A^{\alpha,T}_{g,g'})^{-1}\), with the corresponding pushed-forward cross blocks. The boundary paths are part of the marked readout prescription: only declared presentation equivalences with transported readout and source maps preserve that experiment. Scalar path independence in (LI2) does not justify an arbitrary path replacement. Source derivatives keep the source-free normalization below fixed; changing the preparation prescription itself also changes that normalization.

Let \(z_e(t)\) be the exact unmarked one-link row integral of \(\mathbb E e^{-tS_ed_e^2}\), and set
\[
Z_\alpha=\prod_e z_e(\alpha/r_e),\qquad
(F_{\alpha,\beta}\psi)(g)=Z_\alpha^{-1}\int K_{\alpha,\beta}(g,g')\psi(g')dg'.
\tag{LI7}
\]
Every \(F_{\alpha,\beta}\) is positive, self-adjoint, injective and contractive on the full Haar carrier. For positivity, condition on all preparations: the free factor is a Gaussian distance kernel on the embedding \(g\mapsto(r_e^{-1/2}g_e\Xi_e)_e\), multiplied by the positive endpoint functions. Almost surely all \(\Xi_e\) are invertible, so this embedding is injective; the Gaussian Fourier argument proves strict positive energy on every nonzero Haar-density measure. The inequality \(0<K_{\alpha,\beta}\le K_{\alpha,0}\), symmetry and the exact free row integral give contraction by the Schur test. Gauge covariance makes the operator commute with the full vertex action. Its restriction to \(L^2(SU(2)^{\mathcal E})^{SU(2)^{\mathcal V}}\) therefore retains the entire physical carrier, without a separate conjugation quotient on each link.

## The finite-graph continuum-time return

Let \(D_{Q,e}=-\Delta_{Q,e}\), with \(Q=-2\operatorname{Tr}\), so \(D_Q=-\Delta_{S^3}/4\). Define
\[
\rho_e=\frac{\mathbb E S_e^{-5/2}}{\mathbb E S_e^{-3/2}}
=\frac{2}{3\sigma_e^2},\qquad
\eta_e=\frac{\mathbb E S_e^{-1/2}}{\mathbb E S_e^{-3/2}}
=\frac52\sigma_e^2,
\]
\[
\boxed{\kappa_e=r_e\rho_e,\qquad
\lambda_c=\beta_c\sum_e w_{ce}\eta_e,\qquad
H_\Lambda=\sum_e\kappa_eD_{Q,e}+\sum_c\lambda_cV_c.}
\tag{LI8}
\]
For every fixed finite graph and fixed parameters,
\[
F_{\alpha,\beta}\psi=\psi-\alpha^{-1}H_\Lambda\psi+O_\psi(\alpha^{-2}),
\qquad
F_{n/t,\beta}^{\,n}\longrightarrow e^{-tH_\Lambda}
\quad\text{strongly}.
\tag{LI9}
\]
The first statement holds on smooth functions in the uniform norm. The free operator is the tensor product of the normalized [[relative-multiplication-transfer-and-the-rotor-limit|one-link relative transfers]] at parameters \(\alpha/r_e\); their expansions supply the electric sum. Integrating the neighboring configurations weights each preparation by \(S_e^{-3/2}\), independently at leading order. Expanding the weak endpoints consequently returns \(\sum_c\beta_cV_c\sum_e w_{ce}\eta_e\). The quadratic endpoint remainder uses finite positive moments of these weighted preparations. The free fourth-order remainder needs only \(\mathbb E S_e^{-7/2}<\infty\), satisfied by each rank-four Gaussian. The exact free normalization cancels its scalar geometric corrections. This is the local version of [[anchored-word-cost-and-the-interacting-return|the anchored-word return]].

On the compact smooth covering product, \(H_\Lambda\) is nonnegative and uniformly elliptic, with bounded smooth potential, form domain \(H^1\) and operator domain \(H^2\). Smooth functions form a core. Contractivity and telescoping give the strong limit on the full carrier and its gauge-invariant subspace, uniformly on bounded nonnegative time intervals. The positive scalar heat evolution gives a simple positive ground vector, which is gauge invariant; the interacting vacuum is returned by this operator. No estimate uniform over graph growth is asserted.

## The shared incidence has a measurable source covariance

The leading preparation law after integrating one nearby temporal boundary is
\[
d\nu(\Xi)=\prod_e\frac{S_e^{-3/2}d\gamma_e(\Xi_e)}{\mathbb E S_e^{-3/2}},
\qquad S_e\sim_\nu\operatorname{Gamma}(5/2,\sigma_e^2).
\tag{LI10}
\]
It is a localization preparation law, not the returned interacting frame vacuum. The weak features tend to one at this leading order. For the incidence variables in (LI3),
\[
\mathbb E_\nu e^{-\sum_ct_cY_c}
=\prod_e\left(1+\sigma_e^2\sum_cw_{ce}t_c\right)^{-5/2},
\]
\[
\boxed{\operatorname{Cov}_\nu(Y_c,Y_d)
=\frac52\sum_e w_{ce}w_{de}\sigma_e^4.}
\tag{LI11}
\]
Thus two cells with positive weights on a common link have a strictly positive mixed logarithmic source response. Under the original unweighted Gaussian prior, the factor is instead \(4\), not \(5/2\). At a fixed finite comparison the exact conditioned covariance is supplied by (LI6), rather than either universal prior coefficient. The source response must keep the preparation measure appropriate to its experiment.

## Attach a genuine cell while retaining the shared link

Start from one square. Attach an adjacent square along its existing edge \(p\), adding the three new outer links and their preparations. Keep the old \(\Xi_p\), covariance and incidence weights for the old cell; the new cell assigns its own normalized incidence weights and reuses \(\Xi_p\). At zero new cell strength the normalized raw transfer is exactly the old transfer tensored with the three new free link transfers. Hence the old observable embedding \(\psi\mapsto\psi\otimes1\) intertwines these finite-width transfers, including old preparation marks with no new insertions. It also respects the vertex gauge actions.

For positive new strength, the same shared variable participates in both costs and in their mixed response (LI11). With all \(\kappa_e=\kappa\), tree coordinates \(x=up^{-1}\), \(y=vp^{-1}\), where \(u,v\) are the two outer three-link paths, give
\[
H_{\rm two\ cells}=
4\kappa(D_{Q,x}+D_{Q,y})-2\kappa\sum_AR_{x,A}R_{y,A}
+\lambda_1(1-a)+\lambda_2(1-b).
\tag{LI12}
\]
The [[gauge-cycle-innovation-filtration/loop-coordinates-and-the-induced-clock|induced-clock identity]] proves this as a complete operator reduction. In particular, with \(z=\mathbf x\cdot\mathbf y\), its electric part sends \(ab\) to \(\kappa(6ab-z/2)\). The shared raw link produces the mixed kinetic term. The shared Gaussian cell weights additionally supply the joint source response; these are distinct consequences of the same incidence assignment.

Equation (LI12) is the operator of [[coarse-response-memory/two-plaquette-vacuum-and-relational-state|the two-plaquette benchmark]]. Keeping \(\lambda_1>0\) and varying \(\lambda_2=t\gamma\), with its additive scalar \(t\gamma\) retained, gives [[coarse-response-memory/correlated-interface-tangent|the complete crossing tangent]], including its signed angular channel. It also matches the return of [[spatial-word-comparison-and-mixed-motion|the word comparison]] and the anchored owner after matching the declared coefficients. For example, \(\sigma_e^2=1\), \(r_e=1/40\), and cell strength \(\beta_c=2\beta\) give \(\kappa=1/60\), \(\lambda_c=5\beta\). The finite preparation inventories and kernels remain different constructions.

Each localization still uses dimension three and complex rank four. Adding a genuine cell therefore does not impose the single globally shared norm of [[preparation-rank-and-locality|the rank obstruction]]. This observation does not grant refinement consistency: [[preparation-transport-through-spatial-subdivision|preparation transport through subdivision]] distinguishes a new cell from a pure bivalent subdivision, where the old preparation and its sources must be transported. Cutting a shared link duplicates its readouts, not its underlying variable or reference measure. Successive temporal edges use independent copies of the entire declared spatial preparation; correlations between temporal edges can be inserted by the full block-source law of [[commutator-preparation-transfer-and-marked-gluing|marked gluing]]. Closed amplitudes retain \(Z_\alpha^{-N}\) and all transported marks. Neither pure presentation moves nor source insertion authorize resetting those factors.

## The construction on a general compact simple group

The finite-graph return also holds for a declared compact connected group \(G\) with simple Lie algebra of dimension \(d\), using any faithful unitary representation \(\rho:G\to U(n)\). This paragraph uses the separate convention of [[general-group-preparation-and-the-casimir-return|the general-group preparation theorem]]: \(Q(X,Y)=-\operatorname{Re}\operatorname{Tr}[d\rho(X)d\rho(Y)]\), and the preparation norm is unnormalized Hilbert–Schmidt. Do not import the preceding \(M_2\) numerical constants into this convention.

Assign independent matrices \(\Xi_e\in\mathbb C^{n\times k_e}\) with independent circular complex entries of variance \(\sigma_e^2\), where
\[
k_e>n+\frac d2.
\tag{LI13}
\]
This sufficient finite inventory gives full row rank almost surely and the dominated localization proved by the general-group owner. Keep the same actual cell words, incidence weights and boundary paths. The terminal vertex action and cell rows are now
\[
\Xi_e\mapsto\rho(h_{t(e)})\Xi_e,\qquad
C_{ce}(g)=[\rho(U_c(g))-I_n]\rho(W_{ce}(g)),
\]
\[
\mathcal C(g,\Xi)=\frac12\sum_{c,e}\beta_cw_{ce}\|C_{ce}(g)\Xi_e\|_{\rm HS}^2,
\qquad f_{\alpha,g}=e^{-\mathcal C(g,\Xi)/(2\alpha)}.
\tag{LI14}
\]
These are left transports of rectangular preparations. Under a vertex action, each cell output gains left multiplication by \(\rho(h_{v_c})\), and each temporal output \([\rho(g_e)-\rho(g'_e)]\Xi_e\) gains left multiplication by \(\rho(h_{s(e)})\). The norms and isotropic preparation law are therefore gauge invariant.

Use these endpoint factors in the Gaussian comparison
\[
K_{\alpha,\beta}^{G}(g,g')=
\mathbb E\!\left[f_{\alpha,g}
e^{-\alpha\sum_e r_e^{-1}\|[\rho(g_e)-\rho(g'_e)]\Xi_e\|_{\rm HS}^2}
f_{\alpha,g'}\right].
\tag{LI15}
\]
For \(B_\rho(u)=2I_n-\rho(u)-\rho(u)^\dagger\), its complete marked precision, with columns stacked within each link, is
\[
\begin{aligned}
\mathcal Q^{\alpha,T}_{g,g'}
&=\bigoplus_e I_{k_e}\otimes\left[\sigma_e^{-2}I_n
+\frac\alpha{r_e}B_\rho(g_e^{-1}g'_e)\right.\\
&\hspace{34mm}\left.+\frac1{4\alpha}\sum_c\beta_cw_{ce}
\{C_{ce}(g)^\dagger C_{ce}(g)+C_{ce}(g')^\dagger C_{ce}(g')\}\right]+T.
\end{aligned}
\tag{LI16}
\]
For arbitrary joint \(j,T=T^\dagger\) with this precision positive, the marked kernel is exactly \(\exp[j^\dagger(\mathcal Q^{\alpha,T})^{-1}j]/[\det\Gamma\det\mathcal Q^{\alpha,T}]\), with \(\Gamma=\bigoplus_e\sigma_e^2I_{nk_e}\). This includes every cross-column, cross-link and transported row source. Unmarked preparations factor by link, but the matrix terms within each link need not commute.

Divide by \(Z_\alpha^G=\prod_ez_e^G(\alpha/r_e)\), the exact free row normalization from the general-group theorem. The resulting transfer is a positive injective contraction on the full Haar \(L^2(G^{\mathcal E})\), commuting with all vertex gauge actions. The proof is the same fixed-preparation embedding and domination argument as for (LI7), now using faithfulness and full row rank on every link.

For each link define its real tangent metric, localized preparation law and returned moments by
\[
g_{\Xi_e}(X,Y)=\operatorname{Re}\operatorname{Tr}[(d\rho(X)\Xi_e)^\dagger d\rho(Y)\Xi_e],
\qquad
d\nu_e=\frac{(\det_Q g_{\Xi_e})^{-1/2}dP_e}{\mathbb E(\det_Q g_{\Xi_e})^{-1/2}},
\]
\[
c_e=\frac1d\mathbb E_{\nu_e}\operatorname{tr}_Q g_{\Xi_e}^{-1},
\qquad \overline A_e=\mathbb E_{\nu_e}(\Xi_e\Xi_e^\dagger).
\tag{LI17}
\]
The local preparation laws are independent at leading order. The general-group theorem proves all these moments finite under (LI13), and that \(\overline A_e\) commutes with \(\rho(G)\). Hence \(\rho(W_{ce})\) drops from the leading expected cell cost, giving the exact finite-graph return
\[
\boxed{H_\Lambda^G=
\sum_e\frac{r_ec_e}{4}(-\Delta_{Q,e})
+\sum_c\beta_c\sum_e w_{ce}
\operatorname{Tr}[\overline A_e(I_n-\operatorname{Re}\rho(U_c))].}
\tag{LI18}
\]
Here \(\operatorname{Re}\rho=(\rho+\rho^\dagger)/2\). Under the stated sufficient inventory condition the normalized transfers satisfy \(F_\alpha^G\psi=\psi-\alpha^{-1}H_\Lambda^G\psi+o(\alpha^{-1})\) uniformly on bounded sets of the needed smooth norms; no \(O(\alpha^{-2})\) rate is asserted. Product localization on finitely many links and the polynomially weighted domination in the general-group owner control the weak cell cost. Contractivity then gives \((F_{N/t}^G)^N\to e^{-tH_\Lambda^G}\) strongly as the step count \(N\to\infty\) on the full carrier and its complete vertex-invariant subspace, uniformly on bounded nonnegative times. The operator has the inherited \(H^1\) form and \(H^2\) operator domains and a simple positive gauge-invariant ground vector.

If \(\rho\) is irreducible, its potential has the explicit coefficients
\[
\overline A_e=a_eI_n,\qquad
a_e=\frac{\sigma_e^2(nk_e-d/2)}n,
\qquad
V_\Lambda^G=\sum_c\beta_c\left(\sum_e w_{ce}a_e\right)
[n-\operatorname{Re}\chi_\rho(U_c)].
\tag{LI19}
\]
For a faithful reducible representation, (LI18) instead yields the positive weighted character sum determined by the block coefficients of \(\overline A_e\), as proved in the general-group owner. Faithful reducible choices preserve global forms that admit no faithful irreducible representation. The scalar Gamma formulas (LI10)–(LI11) belong to the earlier \(SU(2)\) preparation; (LI17) is the preparation law for this convention.

Independence of the leading potential from \(W_{ce}\) does not imply path independence of the finite kernel (LI16), where the free and cell matrices interact, or of its marked experiment. The paths and all source maps remain part of the declared law. Pure subdivisions still use the transported preparation construction; a genuinely enlarged cell diagram has its own declared inventory. Equations (LI13)–(LI19) complete the finite-graph construction for the stated compact simple groups, with gauge constraints, full sources and the interacting operator retained. They do not establish estimates uniform over growing graphs, a selected representation or inventory, or the four-dimensional physical return.
