# Two Cube Temporal Sewing and the Actual Joint Source

The shared face can be attached with one original electric history and one magnetic factor, retaining the global vacuum caps and every joint mark. In this actual compact family, increasing its magnetic weight strictly decreases a fixed cross-cell bracket expectation for sufficiently strong confinement, even though the full gap is larger at the fully attached endpoint. The bracket source's harmonic spectral support also changes when a coefficient vanishes; actual soft spectral weight must be tested separately.

**Status: exact finite temporal sewing and parameter-response identity; proved fixed-complex compact source return, uniform in the shared-cost parameter.** [[two-cube-shared-face-and-the-original-kinetic-law|TC]] owns the common-root words and twenty-edge operator. [[two-cube-interior-cost-and-the-joint-bracket-response|TI]] owns the derived harmonic spectrum and joint-source contractions. Group, preparation, graph and physical clock remain declared.

## Sew the shared history once

Let \(E_L,E_R\) be the eight edges belonging exclusively to each cell, and \(E_S\) the four shared-face edges. On the full raw carrier \(G^{20}\), retain
\[
H_\tau=\kappa\sum_{e\in E_L\cup E_S\cup E_R}\mathsf C_{e,Q}
+g\left(\sum_{f\in\mathrm{ext}}W_A(F_f)+\tau W_A(P_1)\right),
\qquad 0\le\tau\le1.
\tag{TJ1}
\]
There are ten exterior costs. The control \(\tau=0\) keeps the same graph, based word \(P_1\), source marks and twenty electric edges.

Here is an exact chronological realization of the allocation. For physical duration \(t>0\), set \(\delta=t/N\), let \(T_{\rm el}=\kappa\sum_e\mathsf C_{e,Q}\), and denote the magnetic multiplier in TJ1 by \(V_\tau^{\rm phys}\). Then
\[
e^{-tH_\tau}
=\operatorname{s-lim}_{N\to\infty}
\left(e^{-\delta V_\tau^{\rm phys}/2}
e^{-\delta T_{\rm el}}
e^{-\delta V_\tau^{\rm phys}/2}\right)^N.
\tag{TJ2}
\]
For each fixed coupling the potential is bounded on the compact raw carrier. Bounded-perturbation Duhamel expansion gives this product limit; the symmetric factors merely place half spatial weights at the two outer slices.

Each finite product has the positive electric density
\[
\prod_{m=1}^N\prod_{e=1}^{20}
k_{\kappa\delta,Q}\!\left(U_{e,m-1}^{-1}U_{e,m}\right)
\]
and magnetic weight
\[
\exp\left[-\delta g\sum_{m=0}^N\eta_m
\left(\sum_{f\in\mathrm{ext}}W_A(F_f(U_m))
+\tau W_A(P_1(U_m))\right)\right],
\quad
\eta_0=\eta_N=\tfrac12,\quad \eta_m=1\ (0<m<N).
\tag{TJ3}
\]
The heat kernel is that of the original nonnegative \(Q\)-Casimir. Every shared edge contributes one heat kernel per time step, and every shared plaquette contributes one cost per weighted slice.

Separate the histories into \(A,S,B\) on \(E_L,E_S,E_R\). The weight factors as \(w_L(A;S)w_S(S)w_R(B;S)\): \(w_L,w_R\) carry their eight electric histories and five exterior costs, and \(w_S\) carries the four shared electric histories and the shared cost. For a bounded joint mark \(M\), the actual-vacuum capped integral is
\[
Z_N[M]=\int
v_\tau(U_0)v_\tau(U_N)\,
M(A,S,B)\,w_L(A;S)w_S(S)w_R(B;S)\,dA\,dS\,dB.
\tag{TJ4}
\]
Here \(v_\tau\) is the normalized global vacuum of TJ1. The cap and the mark remain inside both integrations; common-root connectors can themselves use edges from both blocks. Although the local action factors conditional on \(S\), neither the capped law nor a general joint mark is asserted to factor.

For the chronological limit, let \(M\) be a product, or finite linear combination of products, of bounded joint time-slice marks at prescribed insertion times. Apply TJ2 separately between successive insertion times; no common equally spaced grid is required. Strong convergence and bounded multiplication then give the normalized history as the limit of \(Z_N[M]/Z_N[1]\). Fubini agrees at every finite subdivision and preserves that limit and normalization. This does not assert convergence for every bounded path functional. Keep framed variables until the single global Gauss projection; independent regional quotients would change the available boundary channels. This is [[spatial-block-sewing-and-the-vacuum-cap-response|SB's cap-preserving spatial sewing]] for the explicit two-cell complex.

The formula explains why adding two complete single-cell Hamiltonians is incorrect here: it doubles the four shared kinetic terms and the shared cost. It does not derive \(\kappa,g,A\) or a physical clock from incidence alone.

## Use a mark involving both cells and their shared face

Write \(q=q_\rho\) for the original bounded GM source. The three horizontal faces are the fixed common-root words \(P_0,P_1,P_2\) of TC. Define
\[
A_q=2(q(P_0)-q(P_1)),\qquad
B_q=2(q(P_2)-q(P_1)),\qquad
M=|[A_q,B_q]|_Q^2,\qquad F_h=h^{-4}M,
\tag{TJ5}
\]
where
\[
h=\left(\frac{\kappa}{2I_Ag}\right)^{1/4},\qquad E=\kappa h^{-2}.
\]
The original nonnegative scalar mark \(M\) is bounded, gauge invariant and independent of \(\tau\); it vanishes identically after Abelianization. The scale \(E\) also stays fixed when \(\tau\) varies.

Let \(H_j\) be the leading scaled logarithm of \(P_j\). In the Gaussian well,
\[
E_{\rm v}=\frac{H_0+H_2-2H_1}{\sqrt2},\qquad
O_{\rm v}=\frac{H_0-H_2}{\sqrt2},\qquad
F_h\longrightarrow P=|[E_{\rm v},O_{\rm v}]|_Q^2.
\tag{TJ6}
\]
The sign of the unsquared bracket is immaterial in TJ6. Both combinations and the shared word are retained under the control.

## The compact return is uniform over the shared-cost interval

Put \(\widehat H_{\tau,h}=H_\tau/E\), let \(v_{\tau,h}\) be its positive vacuum, and write \(K_{\tau,h}=\widehat H_{\tau,h}-\lambda_0(\tau,h)\). TC's nine independent face costs all occur among the exterior costs. They give a unique nondegenerate identity well even at \(\tau=0\). The chord rows ensure uniform ellipticity on the smooth \(G^9\) cover. TI's smallest squared frequency satisfies
\[
\lambda_-(\tau)
=\frac{7+4\tau-\sqrt{17-24\tau+16\tau^2}}2
\ge\frac{7-\sqrt{17}}2>0.
\tag{TJ7}
\]
All local coefficients, the harmonic vacuum and its reduced inverse vary smoothly with \(\tau\). Their bounds are uniform on \([0,1]\); the excited-state crossing at \(\tau=\tfrac12\) does not close the vacuum gap.

Apply the equivariant localization and polynomial-Gaussian vacuum recursion of [[closed-cube-bracket-source-and-the-actual-vacuum-return|CQ]] in dimension \(9d\). Uniform relative form errors give uniform low eigenvalue return. A normalized fifth-order vacuum quasimode has residual and vacuum norm error \(O(h^6)\), uniformly in \(\tau\). This pays both the globally \(O(h^{-4})\) source and the \(O(h^{-2})\) parameter insertion before taking their local Taylor limits.

Let
\[
\begin{aligned}
f_h&=(F_h-\mathbb E_{\tau,h}F_h)v_{\tau,h},\\
D_h&=\partial_\tau\widehat H_{\tau,h}
=h^{-2}\frac{W_A(P_1)}{2I_A},\qquad
b_h=(D_h-\mathbb E_{\tau,h}D_h)v_{\tau,h},\\
f_0&=(P-\mathbb E_{\tau,0}P)\Omega_\tau,\qquad
b_0=\left(\frac{|H_1|_Q^2}4-\mathbb E_{\tau,0}\frac{|H_1|_Q^2}4\right)\Omega_\tau .
\end{aligned}
\tag{TJ8}
\]
With the actual centered cutoff embedding \(I_h=Q_h\mathcal J_hQ_0\), Gaussian moments and the preceding residual accuracy give
\[
\|f_h-I_hf_0\|+\|b_h-I_hb_0\|\le Ch,\qquad
\|f_h\|+\|b_h\|\le C.
\tag{TJ9}
\]
The full local kinetic and magnetic jets are retained. No product vacuum or separately normalized magnetic density is used.

On every fixed Hermite-degree family the centered generator defect is \(O(h)\), uniformly in \(\tau\). Both centered generators have a common positive lower bound. The decaying Duhamel estimate of [[centered-compact-chronology-and-integrable-source-return|CC]] therefore gives, for the diagonal and mixed profiles,
\[
\begin{aligned}
d_h(s)&=\langle f_h,e^{-sK_{\tau,h}}f_h\rangle,&
d_0(s)&=\langle f_0,e^{-sK_{\tau,0}}f_0\rangle,\\
k_h(s)&=\langle f_h,e^{-sK_{\tau,h}}b_h\rangle,&
k_0(s)&=\langle f_0,e^{-sK_{\tau,0}}b_0\rangle,\\
|d_h(s)-d_0(s)|+|k_h(s)-k_0(s)|
&\le Ch(1+s)e^{-cs}\qquad(s\ge0).
\end{aligned}
\tag{TJ10}
\]
The absolute time-integral errors are also \(O(h)\). These are specified two-point histories, not a claim about all normalized source families.

## The shared attachment suppresses the actual bracket mean

TI's horizontal covariance is \(4L_\tau^{-1/2}\), where
\[
L_\tau=\begin{pmatrix}
5&-1&0\\-1&2+4\tau&-1\\0&-1&5
\end{pmatrix}.
\]
Put \(w=(1,-2,1)^{\mathsf T}/\sqrt2\), \(e_{\rm mid}=(0,1,0)^{\mathsf T}\), and
\[
c_\tau(s)=4w^{\mathsf T}L_\tau^{-1/2}e^{-s\sqrt{L_\tau}}e_{\rm mid},
\qquad
v_O=\frac4{\sqrt5},\qquad
F_Q=d\,C_{\rm ad}=\sum_{abc}Q(e_a,[e_b,e_c])^2.
\tag{TJ11}
\]
The odd spatial mode \(O_{\rm v}\) is independent of the whole even sector and has component variance \(v_O\). Integrating it first gives
\(\mathbb E_O P=C_{\rm ad}v_O|E_{\rm v}|^2\). Wick's two remaining pairings yield
\[
\boxed{\quad k_0(s)=\frac{F_Qv_O}{2}\,c_\tau(s)^2\ge0.\quad}
\tag{TJ12}
\]
The parameter response is exact before approximation. Differentiating the simple normalized vacuum at fixed \(h\), or using its reduced resolvent, gives
\[
\boxed{\quad
\partial_\tau\mathbb E_{\tau,h}F_h
=-2\langle f_h,K_{\tau,h}^{-1}b_h\rangle
=-2\int_0^\infty k_h(s)\,ds.\quad}
\tag{TJ13}
\]
There is no source derivative: TJ5 and the clock are \(\tau\)-independent. The changing vacuum caps and centering are included.

TI writes \(\mathbb E_{\tau,0}P=F_QD(\tau)\), with
\[
D(\tau)=\frac{16}{\sqrt5}
\frac{8+4\tau+3\sqrt{8+20\tau}}
{\sqrt{8+20\tau}\sqrt{7+4\tau+2\sqrt{8+20\tau}}}.
\]
Its resolvent integral proves the uniform margin \(D'(\tau)\le-64/(7\sqrt{35})<0\). TJ10 and TJ13 now give the stronger actual statement
\[
\boxed{\quad
\partial_\tau\mathbb E_{\tau,h}F_h=F_QD'(\tau)+O(h)<0
\quad(0\le\tau\le1,\ h<h_0).\quad}
\tag{TJ14}
\]
The final inequality is uniform by the stated margin. It follows from the exact mixed response and its integral error, not from differentiating an \(O(h)\) expectation remainder. Pointwise positivity of the actual mixed profile is not claimed.

The actual full physical gaps, in the same scaled units, satisfy uniformly
\[
\Delta_h(\tau)\longrightarrow
2\sqrt{\min\{\lambda_-(\tau),3\}}.
\tag{TJ15}
\]
Thus \(\Delta_h(1)>\Delta_h(0)\) for sufficiently small \(h\), while the bracket mean decreases throughout the attachment. The endpoint increase is already an Abelian incidence effect in the even scalar sector. TJ15 does not prove monotonicity of the actual gap at every intermediate \(\tau\), especially on the harmonic plateau.

## Small spectral weight remains a separate obligation

TI proves the harmonic cyclic edge of \(f_0\):
\[
\lambda_{f_0}(\tau)=
\begin{cases}
2\sqrt{\lambda_-(\tau)},&0\le\tau<1,\\
2\sqrt5,&\tau=1.
\end{cases}
\tag{TJ16}
\]
The lowest radial spectral weight tends to zero as \((1-\tau)^4\). At full attachment the horizontal difference cancels the harmonic frequency-two mode. Meanwhile the full physical harmonic edge remains \(2\sqrt3\). A continuous two-point profile can therefore have a discontinuous cyclic edge.

For fixed \(0\le\tau\le\tfrac12\), harmonic source support reaches the full physical minimum. TJ9, cluster return and TJ15 then sandwich the actual source edge:
\[
\lambda_{f_h}(\tau)\longrightarrow2\sqrt{\lambda_-(\tau)}.
\tag{TJ17}
\]
For the rest of the interval, the proved conclusions are only
\[
2\sqrt3\le\liminf_{h\downarrow0}\lambda_{f_h}(\tau)
\le\limsup_{h\downarrow0}\lambda_{f_h}(\tau)
\le
\begin{cases}
2\sqrt{\lambda_-(\tau)},&\tfrac12<\tau<1,\\
2\sqrt5,&\tau=1.
\end{cases}
\tag{TJ18}
\]
The upper bounds follow from nonzero returned weight in a fixed harmonic cluster. The lower bound is the full physical gap. When the limiting source misses that minimum, an \(O(h)\) vector return cannot exclude smaller actual spectral weight there.

The two frequency-\(\sqrt3\) modes admit a radial sum of squared color norms. It is gauge invariant and invariant under graph symmetries preserving this harmonic mode space, so these symmetries permit a scalar channel at the lowest energy. No exact transformation law of the fixed connector-dependent source has been supplied that excludes overlap with that channel. Harmonic horizontal decoupling has not been promoted to an exact invariant sector.

The next decisive nonlinear test is the actual bracket source's projection onto this lowest physical cluster at \(\tau=1\), retaining the perturbed source, vacuum, cluster and full prepared character. A nonzero coefficient would expose chronological soft support hidden by the leading bracket profile; an exact zero would require a constructional invariant, beyond the displayed symmetry. This tests the same OI source-sewing proposal rather than adding a fitted local mass term.

All times \(s\) above are scaled times; physical duration is \(s/E\). The complex is fixed. Neither its nonzero finite gap nor its signed attachment response proves an infinite-volume or continuum Yang–Mills gap, and the same-amplitude cosmological return remains open.
