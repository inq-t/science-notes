# Regional Conditional Projections Follow the Actual Vacuum Score

The regional conditional projection has a first-order return in the actual compact vacuum, with its marginal normalizer retained. On each fixed finite polynomial source family, its derivative is the off-diagonal multiplication operator determined by the first vacuum amplitude score. Arbitrarily accurate compact quasimodes supply the weighted estimate needed to prove this derivative; Hellinger convergence alone would not suffice. Complete prepared face variables remain the regional access data throughout the comparison.

**Status: proved fixed-patch, fixed-group strong-source derivative.** [[vacuum-hellinger-return-and-regional-conditional-projections|VH]] supplies the fiber projection formula and its angle estimate. [[fixed-group-compact-vacuum-and-oriented-source-return|GV]] and [[compact-source-normalization-and-the-nonlinear-return|CS]] supply the actual-vacuum localization and quasimode method, extended below to any fixed finite open square patch. [[resonant-source-transport-and-fixed-regional-access|RG]] identifies why this actual projection must accompany a normal-form source comparison. No operator-norm derivative, uniform spatial estimate or complete marked-history limit is claimed.

## Keep the compact carrier and regional words exact

Fix a finite open \(L\times L\) patch, including \(L=5\), and a compact connected group \(G\) with simple Lie algebra of dimension \(d\). Keep the invariant metric \(Q\), faithful unitary representation \(\rho\), and positive preparation matrix \(A\) commuting with \(\rho(G)\). The weighted character and scale are those of [[weighted-character-scale-and-bounded-lie-sources|GM]]:
\[
H_{\kappa,g,A}=\kappa\sum_eC_{e,Q}
+g\sum_pW_A(P_p),\qquad
g_{\rm eff}=2I_Ag,\quad
h=(\kappa/g_{\rm eff})^{1/4},\quad
E_h=\kappa h^{-2}.
\tag{VP1}
\]
All vertices are gauged. Keep the prepared based-face words and comb connectors fixed. The exact triangular comb map gives the cover \(G^N\), \(N=L^2\), with product Haar measure and one simultaneous Gauss action. A region \(\mathcal A\) means a subset of these complete face variables. It does not mean an independently gauged or detached subsystem.

An exact common measurable chart can be built without assuming that a bounded Lie-valued mark separates group elements. Choose a small exponential chart at the identity and keep its logarithm coordinates unchanged on a smaller ball. Cover the complement by finitely many relatively compact smooth charts. Partition that complement into disjoint Borel pieces, each contained in its assigned chart, and translate and rescale their coordinate images into pairwise disjoint bounded boxes separated from the identity ball. Retain every piece and its inverse map. The resulting map
\[
\mathfrak c:G\longrightarrow D\subset\mathbb R^d
\]
is a bounded measurable bijection with measurable inverse, agrees with \(\log\) near the identity, and pushes Haar measure to a positive density \(j(x)\,dx\) on its measurable image, up to null sets. This follows chart by chart from the ordinary smooth change-of-variables formula. Boundaries can be assigned to any one of their chart pieces.

Use this same completed chart separately on each face. With
\(D_h=(D/h)^N\), the map
\[
(\mathcal U_hv)(X)
=h^{dN/2}\prod_pj(hX_p)^{1/2}
v\!\left((\mathfrak c^{-1}(hX_p))_{p=1}^N\right),
\quad X\in D_h,
\tag{VP2}
\]
extended by zero, is an isometry into the common Euclidean \(L^2\) space and a unitary onto its supported subspace. In particular,
\[
\sigma(X_p:p\in\mathcal A)
=\sigma(P_p:p\in\mathcal A)
\]
under this comparison. No complete face algebra is replaced by a noninjective local mark.

Outside the logarithm neighborhood, the Gauss action is the exactly transported compact action; it need not be the linear adjoint action in these auxiliary coordinates. Near the well the chart is equivariant. The local expansions below are therefore invariant, and the arbitrary-order tail bounds remove dependence of those expansions on the chosen chart completion. Conditioning is first performed on the framed cover, then restricted to physical invariant sources.

## Weighted vacuum accuracy follows at each fixed patch

The fixed-group argument of GV extends to this fixed \(L\). The horizontal chord rows are
\[
Z_{i,j,T}=-\mathcal R_{i,j,T}
+\mathbf1_{j<L}\mathcal L_{i,j+1,T}.
\]
Solving this triangular system from the top of each column, and using equality of left and right \(Q\)-norms, controls all face derivatives by the raw chord rows with a finite constant depending on \(L\). The complete cover operator is smooth and elliptic on the compact connected manifold \(G^N\).

Global faithfulness and \(A>0\) make the weighted potential vanish only when every face is the identity. Its local Hessian is positive. Equivariant single-well localization as in GV and CS gives the oscillator
\[
\mathcal O_0=-\partial^{\mathsf T}(A_L\otimes I_d)\partial
+\frac14|X|^2,\qquad A_L=4I-\operatorname{Adj}_L.
\]
Its full-cover vacuum is simple and separated, since every eigenvalue of \(A_L\) is positive at fixed \(L\). Thus the actual positive vacuum has arbitrarily accurate polynomial-Gaussian quasimodes. Resonances among excited oscillator levels do not obstruct the inverse off this vacuum.

Let \(\Omega>0\) be the normalized harmonic vacuum and let
\(\Phi_h=\mathcal U_h\psi_h\) be the actual normalized compact vacuum in the common carrier. Put \(K_0=\mathcal O_0-e_0\). The first correction is
\[
u=-\bigl(K_0|_{\Omega^\perp}\bigr)^{-1}V_1\Omega,\qquad
\langle\Omega,u\rangle=0,\qquad p=u/\Omega .
\tag{VP3}
\]
The actual comb/BCH first jet is odd, with no first density or magnetic term. Hence \(p\) is a real invariant polynomial; in this case it is a Cartan cubic. No choice among resonant source normal forms enters (VP3).

For every fixed integer \(s\ge0\), the stronger weighted statement is
\[
\boxed{
\|\langle X\rangle^s(\Phi_h-\Omega-hu)\|_2
\le C_s h^2.}
\tag{VP4}
\]
Here and below the constants may depend on the fixed \(L,G,Q,\rho,A\).

To prove (VP4), choose a compact vacuum approximation with unweighted norm error \(O(h^M)\), where \(M\ge s+2\), before truncating its polynomial series. On \(D_h\), boundedness of the completed chart gives
\(\langle X\rangle^s\le C_sh^{-s}\), so the weighted actual-to-quasimode error is \(O(h^{M-s})\). Every remaining Taylor coefficient is a fixed polynomial times \(\Omega\), and the terms beginning at order \(h^2\) have weighted norm \(O(h^2)\). The local cutoff equals one near the identity; its Gaussian tails, including the region outside \(D_h\), are smaller than every prescribed power of \(h\). This proves the assertion for each specified weight. A mere first-order unweighted vacuum approximation would not prove it.

## Differentiate the normalized fiber line

Write \(X=(a,z)\), where \(a=X_{\mathcal A}\) is retained and \(z=X_{\mathcal A^c}\) is exterior. Let \(P_{\mathcal A,h}\) be the orthogonal projection onto the closed space of vectors \(\Phi_h(a,z)b(a)\). It is the amplitude form of the actual conditional expectation for the complete regional face algebra:
\[
(P_{\mathcal A,h}v)(a,z)
=\frac{\Phi_h(a,z)}{m_h(a)}
\int\Phi_h(a,w)v(a,w)\,dw,\qquad
m_h(a)=\int\Phi_h(a,z)^2\,dz.
\tag{VP5}
\]
Use zero on zero fibers. Denote the harmonic projection by \(P_{\mathcal A}\), and write
\(\overline f=\mathbb E_0[f\mid a]\) for the harmonic Gaussian conditional expectation. Then
\(P_{\mathcal A}(\Omega f)=\Omega\overline f\).

The auxiliary line \(\phi_h=\Omega+hu\) has exact marginal
\[
m_{\phi_h}(a)=m_0(a)
\bigl(1+2h\overline p(a)+h^2\overline{p^2}(a)\bigr).
\]
Equation (VP4) gives the same first marginal coefficient for \(m_h\), with \(O(h^2)\) remainder in every fixed polynomially weighted \(L^1(da)\) norm. This follows by expanding the squared amplitudes and applying Cauchy–Schwarz; no pointwise inverse-density estimate is implied. Consequently the candidate derivative is
\[
\boxed{
\dot P_{\mathcal A}
=(I-P_{\mathcal A})M_pP_{\mathcal A}
+P_{\mathcal A}M_p(I-P_{\mathcal A}),}
\tag{VP6}
\]
on polynomial-Gaussian sources. Explicitly,
\[
\boxed{
\dot P_{\mathcal A}(\Omega f)
=\Omega\left[p\,\overline f+\overline{pf}
-2\overline p\,\overline f\right].}
\tag{VP7}
\]
The two copies of the marginal score cannot be omitted. One subtracts the parallel part of the moving output line, and the other subtracts it from the input contraction.

This expression maps polynomial Gaussians to polynomial Gaussians: conditioning a finite-dimensional Gaussian sends polynomials to polynomials. It is symmetric on that core and off-diagonal relative to the harmonic regional projection:
\[
P_{\mathcal A}\dot P_{\mathcal A}P_{\mathcal A}=0,\qquad
(I-P_{\mathcal A})\dot P_{\mathcal A}(I-P_{\mathcal A})=0.
\]
The multiplier \(M_p\) and the resulting derivative need not be bounded on the whole Hilbert space.

## The weighted estimate proves the derivative on sources

For every polynomial \(f\),
\[
\boxed{
\|(P_{\mathcal A,h}-P_{\mathcal A}
-h\dot P_{\mathcal A})(\Omega f)\|_2
\le C_{\mathcal A,f}h^2.}
\tag{VP8}
\]
This also holds uniformly on any specified finite-dimensional polynomial source space. The proof uses the exact fiber lines, rather than differentiating an uncontrolled inverse marginal density.

Let \(\phi_h=\Omega+hu\), and let \(P_{\phi_h}\) be its fiber-line projection. Positivity of this auxiliary amplitude is not needed. Set
\[
d_p(a)^2=\mathbb E_0[p^2\mid a],\qquad
q_f(a)^2=\mathbb E_0[|f|^2\mid a].
\]
Both are bounded by fixed polynomial weights in \(a\). On the region
\(|h|d_p(a)\le1/4\),
\[
\|\phi_h(a,\cdot)\|
\ge \tfrac34\|\Omega(a,\cdot)\|.
\]
The angle identity for two rank-one projections gives, independently of the size of the actual amplitude error,
\[
\|(P_{\mathcal A,h}-P_{\phi_h})(\Omega f)(a,\cdot)\|
\le \tfrac43q_f(a)
\|\Phi_h(a,\cdot)-\phi_h(a,\cdot)\|.
\]
Thus (VP4), with a sufficiently large fixed polynomial weight, bounds this part by \(O(h^2)\).

On the same region, the Taylor remainder of the normalized rank-one projection is bounded in fiber operator norm by
\(C h^2d_p(a)^2\). Its first derivative is exactly (VP6), and integration against \(m_0(a)q_f(a)^2\) gives another \(O(h^2)\) bound.

On the complementary region, \(d_p(a)>1/(4|h|)\). Since \(d_p\) grows at most polynomially and the regional marginal is a nondegenerate Gaussian, all weighted harmonic source tails there decay faster than any prescribed power of \(h\). Use the contraction bound for the projections and
\(\|\dot P_{\mathcal A}(a)\|\le 2d_p(a)\) for the derivative. These tails finish (VP8), including possible zero fibers of the actual projection. If \(d_p\) is bounded, this complementary region is empty for small enough \(h\).

The Hellinger estimate in VH gives useful continuity with much weaker hypotheses. The stronger derivative (VP8) follows from (VP4) and the polynomial-Gaussian structure; it has not been inferred from Hellinger convergence alone.

## Moving sources and overlapping conditional experiments

Suppose a specified actual compact source vector has a first expansion
\[
z_h=z_0+hz_1+O(h^2),\qquad
z_0=\Omega f_0,\quad z_1=\Omega f_1,
\]
with polynomial \(f_0,f_1\). Accurate vacuum multiplication as in CS and GV supplies this expansion for each fixed finite family of scaled smooth polynomial-jet marks, including their actual centering and variance normalization when the leading variance is positive. Then
\[
\boxed{
P_{\mathcal A,h}z_h
=P_{\mathcal A}z_0
+h\bigl(\dot P_{\mathcal A}z_0+P_{\mathcal A}z_1\bigr)
+O(h^2).}
\tag{VP9}
\]
This follows from (VP8) and projection contractivity. It retains both the moving vacuum and the moving source normalization.

The same argument iterates through any fixed finite word of regional projections, including overlapping regions. Every leading and first-order intermediate vector is still a polynomial Gaussian, while every actual projection is a contraction. The derivative of the word is the sum of its single derivative insertions, with an \(O(h^2)\) source-vector remainder. No commutation of overlapping projections is assumed.

For nested regions \(\mathcal A\subseteq\mathcal B\), their actual conditional tower is exact. Differentiation on these sources gives
\[
\boxed{
\dot P_{\mathcal A}P_{\mathcal B}
+P_{\mathcal A}\dot P_{\mathcal B}
=\dot P_{\mathcal A},}
\tag{VP10}
\]
and the adjoint identity. Thus the actual regional jets themselves satisfy the inherited nesting relation. This does not identify them with projections transported by a chosen kinetic normal form.

## What the score fixes and what it leaves open

For a regional polynomial \(f=f(a)\), (VP7) simplifies to
\[
\dot P_{\mathcal A}(\Omega f)
=\Omega(p-\overline p)f.
\tag{VP11}
\]
If the region is one complete face, \(\overline p=0\) for the Cartan-cubic vacuum score. Indeed the conditional means of all modes are scalar multiples of that face vector, and every conditional covariance is a scalar mode coefficient times the color identity. The triple of parallel means vanishes in the Cartan form; every covariance contraction vanishes by its alternation. The actual one-face derivative is therefore \(u f\).

The score \(p\), and hence the actual projection derivative, is fixed by the actual vacuum. Adding a resonant generator \(N\) with \(N\Omega=0\) to a source normal form cannot change it. Comparing (VP6) with the transport of a fixed source embedding is a separate operator calculation, as required by [[resonant-source-transport-and-fixed-regional-access|the regional-access test]]. In particular, no equality between those two routes has been declared by changing the regional algebra.

All conclusions concern fixed finite patches, groups and polynomial source families as \(h\to0\) with the declared physical scale. The chart completion retains the whole compact face algebra exactly, but its finite-source asymptotics do not assert a derivative on every regional \(L^2\) vector or in operator norm. No uniform spatial or continuum OI surplus follows.
