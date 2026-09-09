# Conditional Commutator Activity and the Neutral Tail

The actual spatial-link conditional law supplies a positive non-Abelian commutator block, but that block cannot by itself supply the oriented transport remainder. On a one-copy \(SU(2)\) square its strength is an explicit spin-two multiplier. Neutral plaquette sources can concentrate where this strength vanishes. Their normalized innovations have almost maximal chronological surplus, so this is a high-energy failure of an activity-only reconstruction, not a soft-mode counterexample. A viable remainder must retain a channel beyond these local commutator amplitudes.

## Test a concrete block in the selected vacuum

Use the reflected transfer of [[reflection-sewing-and-the-auxiliary-boundary-carrier|RS1–18]] for \(SU(2)\) in the defining representation, one auxiliary copy, and a spatial square. The square fits the declared hypercubic slicing for \(D\ge3\). Fix \(0<r<1\), \(w=(2D)^{-1}\), and \(\kappa=rw\). The supported temporal vacuum is the actual positive vector \(\varphi\), with
\[
d\pi(\Xi)=\varphi(\Xi)^2m(\Xi)d\Xi.
\tag{NC1}
\]
All calculations use this vacuum. No independent Gaussian approximation to \(\pi\) is made. The ground-transformed transfer \(P\), and \(A=P^k\) for any fixed positive integer \(k\), are compact on the gauge-invariant supported carrier. Their unique fixed line is the constants.

Write \(S_v=\|\xi_v\|^2\) and introduce the normalized color projector
\[
\Pi_v=\frac{\xi_v\xi_v^\dagger}{S_v}
\quad(S_v>0).
\tag{NC2}
\]
Set it to zero on the measure-zero set \(S_v=0\). For an oriented spatial edge \(e=(v,w)\), take the actual multiplication block
\[
\mathfrak c_e(U,\Xi)
=\|[\Pi_v,U_{vw}\Pi_wU_{vw}^\dagger]\|_{\rm HS}^2.
\tag{NC3}
\]
It is bounded and gauge invariant. The commutator itself transforms by conjugation at \(v\), so its Hilbert–Schmidt norm is an actual neutral quantity. This is not a gauge transformation acting on a neutral source.

Given \(\Xi\), spatial links have the original independent conditional densities obtained from \(b(U,\Xi)^2/m(\Xi)\). Define
\[
c_e(\Xi)=\mathbb E[\mathfrak c_e(U,\Xi)\mid\Xi],
\qquad C(\Xi)=\sum_{e\in E_\square}c_e(\Xi).
\tag{NC4}
\]
The vacuum factor \(\varphi(\Xi)^2\) does not change this conditional link law. A source insertion never recomputes its normalizer.

## The commutator block is exactly a spin-two response

Choose \(g_v\in SU(2)\) with \(\xi_v=\sqrt{S_v}\,g_ve_1\). In aligned coordinates \(V=g_v^\dagger U_{vw}g_w\), put
\[
t=2\kappa\sqrt{S_vS_w},\qquad
V=u_0I+i\sum_{j=1}^3u_j\sigma_j.
\]
The conditional Haar density is
\[
\frac{e^{tu_0}}{z(t)},\qquad
z(t)=\frac{2I_1(t)}t,
\qquad
m_1(t):=\mathbb E_tu_0=\frac{I_2(t)}{I_1(t)}.
\tag{NC5}
\]
The values at zero are defined by continuity. These are the exact conditional character factors in [[feature-number-grading-and-compact-reconstruction|FN6–7]].

For \(P_0=e_1e_1^\dagger\), let \(n\) be the Bloch unit vector of \(VP_0V^\dagger\). Then
\(\|[P_0,VP_0V^\dagger]\|_{\rm HS}^2=(1-n_3^2)/2\).
The identity \(n_3^2=[1+2P_2(n_3)]/3\), together with the spin-two matrix element \(P_2(n_3)\), gives
\[
\boxed{
c_e(\Xi)=c(t)=\frac13\left[1-\frac{I_5(t)}{I_1(t)}\right].}
\tag{NC6}
\]
Indeed a central conditional density has spin-\(j\) matrix mean \([I_{2j+1}(t)/I_1(t)]I\). This derives the nontrivial representation block from the existing link law; no new comparison rate has been attached to it.

A direct quaternion calculation also gives
\[
c(t)=\frac4{15}\mathbb E_t[(1-u_0^2)(1+4u_0^2)]
\le\frac83[1-m_1(t)].
\tag{NC7}
\]
For the equality, condition on \(u_0\): the other three coordinates are uniform on a two-sphere, so their squared coordinate has first two moments \((1-u_0^2)/3\) and \((1-u_0^2)^2/5\). For the inequality use \(1+4u_0^2\le5\) and \(1-u_0^2\le2(1-u_0)\).

The block is strictly positive for every finite \(t\), has \(c(0)=1/3\), and tends to zero as \(t\to\infty\). More precisely \(c(t)=4/t+O(t^{-2})\): in the large-\(t\) conditional law the three coordinates tangent to \(u_0=1\) have leading variance \(1/t\), which applied to NC7 gives the coefficient four. Positivity of each finite block therefore does not provide a uniform lower bound across actual preparation values.

## An actual plaquette source selects the small-activity region

Let \(F(U)=\operatorname{Tr}(U_\square)/2\). Its exact returned neutral source is
\[
a(\Xi):=\mathbb E[F(U)\mid\Xi]
=\prod_{e\in E_\square}m_1(t_e).
\tag{NC8}
\]
Conditional independence of the links and telescoping of the aligned endpoint rotations prove the formula. At every finite preparation, \(0\le a<1\). Taking all \(S_v\) large makes \(a\to1\). Since \(a\le m_1(t_e)\) for every edge, NC7 gives the exact useful bound
\[
\boxed{0\le C(\Xi)\le\frac{32}{3}[1-a(\Xi)],
\qquad C(\Xi)\le\frac43.}
\tag{NC9}
\]

For \(0<\epsilon<1\), let \(E_\epsilon=\{a>1-\epsilon\}\), with probability \(p_\epsilon=\pi(E_\epsilon)\). The actual vacuum density is strictly positive, and a sufficiently large open region of radial preparations belongs to \(E_\epsilon\), so \(p_\epsilon>0\). Since \(a<1\) almost everywhere, \(p_\epsilon\to0\). Define
\[
f_\epsilon=
\frac{1_{E_\epsilon}-p_\epsilon}
{\sqrt{p_\epsilon(1-p_\epsilon)}}.
\tag{NC10}
\]
These are centered unit vectors in the cyclic sector generated by the returned frame-source multipliers. In particular, bounded functions of \(a\) lie in the closure of polynomials in its multiplier. The tests can be replaced, to arbitrary required norm accuracy at each \(\epsilon\), by finite polynomials in \(a\), followed by centering and normalization. This uses the declared returned source algebra; it does not equate a product of conditional averages with the conditional average of coincident original frame marks.

The vectors converge weakly to zero: for any \(g\in L^2(\pi)\), Cauchy–Schwarz bounds the contribution of \(1_{E_\epsilon}/\sqrt{p_\epsilon}\) by \((\int_{E_\epsilon}|g|^2d\pi)^{1/2}\), while the subtracted constant has coefficient tending to zero. Their activity satisfies
\[
\boxed{
\int C|f_\epsilon|^2d\pi
\le\frac{(32/3)\epsilon+(4/3)p_\epsilon}{1-p_\epsilon}
\longrightarrow0.}
\tag{NC11}
\]
The centering term is retained in this bound. Thus the activity fails to frame the complete centered source space even at one fixed positive \(\kappa\), in its actual temporal vacuum.

## The same test reaches the actual innovation carrier

Use the pair law \(\mu_1(dX,dY)=\pi(dX)A(X,dY)\) and innovation \(\delta_+f=f(Y)-(Af)(X)\) of [[two-slice-innovation-geometry/oriented-innovation-and-finite-temporal-repair|OI19–28]]. Add the original conditional spatial-link draw at the middle boundary \(Y\). On this unchanged sourced extension, define the Hilbert–Schmidt-valued activity maps
\[
(\mathfrak D_eh)(X,Y,U)
=[\Pi_v(Y),U_{vw}\Pi_w(Y)U_{vw}^\dagger]h(X,Y),
\qquad \mathfrak D=(\mathfrak D_e)_e.
\tag{NC12}
\]
Their target norm uses \(\mu_1(dX,dY)\,p_{\rm sp}(dU\mid Y)\), including the actual conditional link normalizer. Consequently
\[
\|\mathfrak D h\|^2
=\int C(Y)|h(X,Y)|^2d\mu_1,
\qquad \|\mathfrak D\|\le\sqrt{4/3}.
\tag{NC13}
\]
Gauge covariance of the matrix output preserves this norm; the input remains a neutral innovation.

Compactness of the actual \(A\) and weak convergence in NC10 give \(\|Af_\epsilon\|\to0\). Hence
\[
\|\delta_+f_\epsilon\|^2=1-\|Af_\epsilon\|^2\longrightarrow1,
\qquad
h_\epsilon:=\frac{\delta_+f_\epsilon}{\|\delta_+f_\epsilon\|}
\in\mathscr K_0.
\]
Equations NC11–13 and the triangle inequality give
\[
\boxed{
\|\mathfrak D h_\epsilon\|\longrightarrow0,
\qquad
\|\mathcal K_\parallel h_\epsilon\|
=\frac{\|\delta_+Af_\epsilon\|}{\|\delta_+f_\epsilon\|}
\longrightarrow0.}
\tag{NC14}
\]
For the first limit, \(\|\mathfrak D J_0f_\epsilon\|^2\) is NC11 and
\(\|\mathfrak D J_-Af_\epsilon\|\le\sqrt{4/3}\|Af_\epsilon\|\).
For the second use \(\|\delta_+\|\le1\) and the exact OI intertwining. In particular, the actual variance surplus is
\[
V_Q(h_\epsilon)-C_{\rm lag}(h_\epsilon)
=1-\|\mathcal K_\parallel h_\epsilon\|^2
\longrightarrow1.
\tag{NC15}
\]
The local commutator activity disappears on a family where the chronological surplus is almost maximal. These sources escape toward strongly attenuated, high-energy directions, not toward the energy edge.

## The activity-only remainder law is rejected

One elementary proposed non-Abelian law would factor the positive remainder of OI25 entirely through the actual blocks NC12:
\[
\eta^2I-\mathcal K_\parallel^*\mathcal K_\parallel
=\sum_{j=1}^{M}\mathcal F_j^*\mathcal F_j,
\qquad
\mathcal F_j=B_j\mathfrak D,
\qquad 0<\eta<1,
\tag{NC16}
\]
where \(M<\infty\) and each \(B_j\) is a bounded synthesis map from the activity output. This defines a concrete class of candidate remainder words: every branch first measures these normalized transported-projector commutators, then applies bounded output operations. No arbitrary gap projector or inverse enters their definition.

NC14 disproves NC16. Its left quadratic form on \(h_\epsilon\) tends to \(\eta^2>0\); the right side is at most
\(\sum_j\|B_j\|^2\|\mathfrak D h_\epsilon\|^2\to0\). The corresponding positive lower-frame claim \(\|\mathfrak D h\|^2\ge c\|h\|^2\), \(c>0\), fails as well. This excludes this activity-only factorization at each fixed member of the square family, regardless of what uniform physical limits might later be attempted.

For an Abelian one-dimensional color representation the commutators are identically zero. In the non-Abelian example they also vanish on aligned preparations with \(U_{vw}=g_vg_w^\dagger\), a compatible flat connection. The positive conditional block distinguishes generic non-Abelian orientations, but the exact plaquette source can select increasingly aligned conditional laws. The unbounded preparation range makes this obstruction present at fixed regulator. [[commutator-word-comparisons-and-neutral-soft-escape|The commutator-word escape]] and [[categorical-gauge-response/categorical-action-on-the-neutral-wilson-carrier|the neutral carrier audit]] concern different failures; neither replaces the actual-vacuum calculation above.

No conclusion here rules out OI25, a sum with an additional direct chronological or Gaussian innovation channel, or input operations that do not factor through \(\mathfrak D\) as in NC16. Raw unnormalized color commutators are a different unbounded proposal with separate domain and scaling obligations. The useful next comparison is to keep the existing transport defect while asking whether non-Abelian multiplication controls its persistent source directions. Discarding that defect in favor of a commutator-only explanation would already lose the fully computed family NC14–15.
