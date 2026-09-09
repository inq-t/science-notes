# Auxiliary Boundary Sufficiency and the Wilson Source Algebra

The reflected determinant transfer averages spatial-link observables over an auxiliary boundary fiber, so its finite source compression is not multiplicative. That defect vanishes in the actual temporal vacuum along the many-copy return. The proof estimates the links from the boundary vectors, uniformly in the length of an even temporal cylinder, and then takes the cylinder to its transfer vacuum. It supplies an asymptotically sharp algebra of bounded invariant polynomial sources and their finite histories. It does not identify all auxiliary states with pure gauge states or control the lowest energy of every normalized excitation.

## Use the boundary and vacuum selected by reflection

Fix the open finite spatial graph \(\Lambda\), compact connected group \(G\), faithful representation \(\rho:G\to U(n)\), \(w=(2D)^{-1}\), and positive hopping \(0<r<1\) from [[reflection-sewing-and-the-auxiliary-boundary-carrier|RS1–14]]. The integer copy count is \(\nu\). Write
\[
\mathcal H_\nu=L^2(m_\nu(\Xi)d\Xi)^{G^\Lambda},
\qquad
\widetilde{\mathsf T}_\nu\varphi_\nu
=\lambda_{0,\nu}\varphi_\nu,
\qquad
\varphi_\nu>0,\quad \|\varphi_\nu\|=1.
\tag{AS1}
\]
The transfer is positive and trace class on this supported auxiliary carrier. Its highest eigenvalue is simple. These facts, including the actual slice weight \(m_\nu\), are consequences of the temporal amplitude factorization, not a separately supplied vacuum.

The spatial-link conditional expectation is
\[
(\Phi_\nu F)(\Xi)
=\frac{\int e^{-V_\nu(U,\Xi)}F(U)\,dU}{m_\nu(\Xi)},
\qquad
m_\nu(\Xi)=\int e^{-V_\nu(U,\Xi)}dU.
\tag{AS2}
\]
Here \(V_\nu\) is the slice action in RS2. This unital positive map preserves conjugation and is bounded by the sup norm. For neutral \(F\), its returned multiplication operator acts on \(\mathcal H_\nu\). At finite \(\nu\), \(\Phi_\nu(FG)\) need not equal \((\Phi_\nu F)(\Phi_\nu G)\).

Let \(\mathcal A_\rho\) be the algebra of gauge-invariant polynomials in the matrix entries of the spatial \(\rho(U_e)\) and their complex conjugates. It contains the usual Wilson polynomial sources, and permits the invariant tensors needed for general \(G\). Faithfulness, Stone–Weierstrass and gauge averaging make it dense in the continuous invariant functions on each finite spatial graph, as in [[prepared-readout-algebra-and-physical-source-completeness|the complete-source construction]]. The estimates below apply to each fixed polynomial and finite edge support; their constants are not uniform over the entire algebra.

## Estimate the spatial links without leaving the actual slice

For a spatial edge \(e=(x,y)\), form the matrix estimator from the boundary vectors alone:
\[
A_e(\Xi)=\frac1{\nu rw}
\sum_{a=1}^{\nu}\xi_x^{(a)}\xi_y^{(a)\dagger}.
\tag{AS3}
\]
It transforms in the same left/right gauge representation as \(\rho(U_e)\). It is not declared to be group valued.

Put the spatial graph on an even periodic temporal cylinder of length \(L\ge6\). Its adjacency is bipartite and has norm at most one, uniformly in \(L\). Conditional on all frame links, the auxiliary copies are independent centered complex Gaussians with covariance \((I-rP_U)^{-1}\). Therefore [[auxiliary-copy-refinement-and-the-exchange-clock|AC6–8's]] estimator calculation applies unchanged:
\[
\boxed{
\mathbb E_{\nu,L}\!\left[
\|A_e-\rho(U_e)\|_{\rm HS}^2\mid U
\right]
\le
\frac{n^2}{\nu r^2w^2(1-r)^2}
+\frac{nr^4}{w^2(1-r^2)^2}.}
\tag{AS4}
\]
The Gaussian covariance bound and the bipartite Neumann remainder have no temporal-volume factor. The constant is also independent of the spatial volume for a fixed edge, since its covariance block has fixed dimension \(n\). This is a direct uniform estimate; it does not use fixed-slab total-variation convergence to a Wilson law.

For a polynomial source, first project \(A_e\) onto the closed Hilbert–Schmidt ball of radius \(\sqrt n\):
\[
\widehat A_e
=A_e\min\{1,\sqrt n/\|A_e\|_{\rm HS}\},
\tag{AS5}
\]
with \(\widehat A_e=0\) when \(A_e=0\). Orthogonal projection onto this convex ball is nonexpansive and fixes every \(\rho(U_e)\), whose norm is \(\sqrt n\). It commutes with the relevant unitary gauge actions. Hence AS4 also bounds \(\widehat A_e-\rho(U_e)\).

Extend \(F\in\mathcal A_\rho\) by its defining matrix polynomial to this finite product of balls, using adjoints for inverse-link entries. The extension is bounded and Lipschitz there. Evaluating it on the \(\widehat A_e\) gives a bounded, slice-measurable estimator \(\widehat F(\Xi)\). If \(S_F\) is its finite edge support, a Lipschitz estimate and Cauchy–Schwarz give, for \(r\le r_0<1\),
\[
\mathbb E_{\nu,L}|F(U)-\widehat F(\Xi)|^2
\le C_F\left[\frac1{\nu r^2}+r^4\right].
\tag{AS6}
\]
The constant depends on the fixed polynomial, its support, \(n,w,r_0\), but not on the temporal cylinder length. Clipping prevents uncontrolled products of unbounded matrix estimators.

At fixed auxiliaries, each spatial link in the joint amplitude appears only in its own hopping factor. Its conditional Haar density therefore factorizes over spatial edges. In particular, the conditional law of \(U_t\) given all auxiliary slices is precisely \(e^{-V_\nu(U_t,\Xi_t)}dU_t/m_\nu(\Xi_t)\); it depends only on \(\Xi_t\). Integrating the other auxiliary slices does not change this conditional law. Thus AS2 is also the actual conditional expectation in the cylinder experiment, not a fresh boundary preparation.

Conditional expectation minimizes mean square error. Set
\[
D_{\nu,F}(\Xi)
=\Phi_\nu(|F|^2)(\Xi)-|\Phi_\nu F(\Xi)|^2.
\]
Then
\[
0\le D_{\nu,F}\le\|F\|_\infty^2,\qquad
\mathbb E_{\nu,L}D_{\nu,F}(\Xi_t)
\le C_F\left[\frac1{\nu r^2}+r^4\right].
\tag{AS7}
\]
All denominators and sources are those of the same cylinder law.

## The estimate passes to its actual temporal vacuum

Integrating the spatial links on the cylinder gives
\[
Z_{\nu,L}=\operatorname{Tr}\widetilde{\mathsf T}_\nu^L,
\qquad
\mathbb E_{\nu,L}B(\Xi_t)
=\frac{\operatorname{Tr}
(M_B\widetilde{\mathsf T}_\nu^L)}
{\operatorname{Tr}\widetilde{\mathsf T}_\nu^L}
\tag{AS8}
\]
for bounded invariant \(B\). The factors \(m_\nu\) occur once per slice. This is exactly the periodic version of RS4–5.

For each fixed \(\nu,r,\Lambda\), positivity, trace class and the simple top eigenvalue imply
\[
\frac{\widetilde{\mathsf T}_\nu^L}
{\operatorname{Tr}\widetilde{\mathsf T}_\nu^L}
\longrightarrow |\varphi_\nu\rangle\langle\varphi_\nu|
\quad\text{in trace norm as even }L\to\infty.
\tag{AS9}
\]
Indeed, divide all eigenvalues by \(\lambda_{0,\nu}\). Their \(L\)-th powers are dominated by their summable first powers, and every ratio except the top one is strictly below one. Dominated convergence gives AS9. No rate uniform in \(\nu\) or spatial size is used.

Apply this to the bounded multiplier \(D_{\nu,F}\) in AS7. The bound was already independent of \(L\), so it passes unchanged:
\[
\boxed{
\langle\varphi_\nu,M_{D_{\nu,F}}\varphi_\nu\rangle
\le C_F\left[\frac1{\nu r^2}+r^4\right].}
\tag{AS10}
\]
This is a statement in the selected reflected vacuum. It does not substitute the finite configuration density \(e^{-V_W}\) for a quantum vacuum, and it does not interchange the copy limit with a nonuniform temporal-vacuum limit.

## Coincident source products become sharp

For two fixed sources \(F,G\in\mathcal A_\rho\), define their compression defect
\[
B_{\nu;F,G}
=\Phi_\nu(FG)-(\Phi_\nu F)(\Phi_\nu G).
\tag{AS11}
\]
Pointwise conditional Cauchy–Schwarz gives
\[
|B_{\nu;F,G}|^2
\le D_{\nu,F}D_{\nu,G}
\le\|G\|_\infty^2D_{\nu,F}.
\]
Consequently
\[
\boxed{
\|M_{B_{\nu;F,G}}\varphi_\nu\|^2
\le C_F\|G\|_\infty^2
\left[\frac1{\nu r^2}+r^4\right].}
\tag{AS12}
\]
Complex sources are included: applying Cauchy–Schwarz to the centered product, with or without a conjugate, yields the same bound.

On the fixed-Wilson path \(r=r_\nu\to0\), \(2\nu r_\nu^4w^4\to b>0\), the bracket tends to zero and is \(O(q_\nu^{-1})\), where \(q_\nu=2\nu r_\nu^2w^2\). Thus \(\Phi_\nu\) becomes multiplicative in its actual vacuum seminorm for every fixed pair of invariant polynomial sources. Unitality and preservation of the adjoint are already exact. This resolves a concrete source-algebra defect of the finite reflected carrier; it is not an operator-norm convergence theorem.

The assertion also covers bounded source histories. Write
\[
d\pi_\nu(\Xi)=|\varphi_\nu(\Xi)|^2m_\nu(\Xi)d\Xi,
\qquad
(P_\nu h)(\Xi)
=\frac{\widetilde{\mathsf T}_\nu(\varphi_\nu h)(\Xi)}
{\lambda_{0,\nu}\varphi_\nu(\Xi)}.
\tag{AS13}
\]
This actual one-step ground-state transform is positive, unital and contractive in sup norm. A vector made by finitely many bounded source multipliers \(\Phi_\nu F_j\) and integer temporal transfers is \(\varphi_\nu h_\nu\), with
\(\|h_\nu\|_\infty\le\prod_j\|F_j\|_\infty\). Multiplying AS12's integrand by \(|h_\nu|^2\) proves the same vanishing defect on every such fixed bounded-source history vector. Arbitrarily long integer time separations do not enlarge that sup-norm bound. Coincident marks can therefore be replaced by products of their compressed operators with a controlled vanishing error on these vectors.

This does not silently renormalize a vanishing vector. If a history vector's norm tends to zero and it is divided by that norm, its sup-norm control can be lost. The constants also depend on polynomial degree and support. These estimates are not uniform over every normalized vector in the growing auxiliary Hilbert spaces.

## The remaining rigidity question is now on a selected source sector

At finite copy count, keep all coincident sources inside their original conditional integral. AS10–13 justify their asymptotic algebraic sharpness on the reflected vacuum and its fixed bounded-source histories. Together with [[reflection-sewing-and-the-auxiliary-boundary-carrier|RS18's]] fixed-slab reflected-source limit, this gives an explicit route from the auxiliary boundary to gauge observables without postulating an independent pure-gauge time-zero algebra.

The two results have different uniformities. RS18 compares complete finite-slab laws and carries the slab-volume remainder. AS10 is uniform in temporal length for a fixed local polynomial but does not itself prove convergence of the sequence of reflected vacua, transfer operators or energy spectra. Neither result excludes soft normalized states whose source support, degree or normalization changes with refinement.

[[oriented-source-lift-and-the-positive-comparison-obstruction|The four-face normal-form comparison]] supplies a useful distinction: its complete multiplier source lift has a sign-indefinite same-source product defect and therefore cannot be this positive conditional compression. Matching quadratic source vectors is insufficient to identify the maps. Their composite-source and retained-operator information must also agree.

The active algebraic rigidity conjecture must therefore act on the cyclic neutral sector generated by these actual source histories and its completed limiting representation. A finite positive certificate or bounded reconstruction must cover its normalized nonvacuum distinctions with constants surviving the physical limits. Gauge projection, bounded-source sufficiency and a simple finite-transfer vacuum do not supply that estimate. The [[global-local-response-reconstruction/quantitative-descent-and-the-shape-of-a-gap|quantitative-descent]] target remains open on this now explicit chronological construction.
