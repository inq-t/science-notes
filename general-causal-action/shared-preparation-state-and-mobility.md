# Shared Preparation: State and Mobility

Using one Gaussian preparation for both relative multiplication and commutator comparison returns a state-dependent mobility and a definite stationary measure. The local preparation after integrating the next frame is generally non-Gaussian. Exact degree normalization gives a conservative diffusion; a different, fixed endpoint normalization retains an additional potential. Both limits follow from the same finite positive kernel with controlled remainders, at each fixed finite comparison strength. They are compact-frame processes with declared normalization and duration, not a Yang–Mills or cosmological return.

## One preparation carries both comparisons

Use \(E=M_2(\mathbb C)\), \(h(X,Y)=\operatorname{Tr}(X^\dagger Y)/2\), normalized Haar measure on \(SU(2)\), and the round unit-\(S^3\) metric. Thus \(-\Delta\) has eigenvalues \(n(n+2)\). Let \(P_G\) be the centered circular complex Gaussian with covariance \(G>0\) on \(E\), and fix \(0\le\beta<\infty\). Put
\[
S=\|\xi\|^2,\quad C_U\xi=[U,\xi],\quad D_U=C_U^\dagger C_U,
\quad f_U(\xi)=e^{-\beta\langle\xi,D_U\xi\rangle/2}.
\tag{SP1}
\]
For \(\alpha>0\), define the shared-preparation kernel and its integrated operator by
\[
K_{\alpha,\beta}(U,V)=\mathbb E_G
\left[f_Ue^{-\alpha\|(U-V)\xi\|^2}f_V\right],
\qquad T_\alpha\psi(U)=\int K_{\alpha,\beta}(U,V)\psi(V)\,dV.
\tag{SP2}
\]
[[relative-multiplication-transfer-and-the-rotor-limit|The relative-multiplication construction, RT16]] proves positivity and injectivity on the full Haar carrier. This retains the frame distinctions lost by the commutator feature alone. No independent second preparation has been introduced.

The full source insertion \(e^{2\operatorname{Re}j^\dagger\xi-\xi^\dagger T\xi}\), with \(T=T^\dagger\) and \(G^{-1}+T>0\), gives exactly
\[
\begin{aligned}
Q_{U,V}^{\alpha,T}
&=G^{-1}+2\alpha\left(1-\tfrac12\operatorname{Re}\operatorname{Tr}(U^\dagger V)\right)I
+\tfrac\beta2(D_U+D_V)+T,\\
K_{\alpha,\beta}^{j,T}(U,V)
&=\frac{\exp\!\left[j^\dagger(Q_{U,V}^{\alpha,T})^{-1}j\right]}
{\det G\det Q_{U,V}^{\alpha,T}}.
\end{aligned}
\tag{SP3}
\]
The precision condition is uniform in the frames, and the positive preparation weight preserves kernel positivity. The source-free normalization factors below remain fixed when this experiment is differentiated. [[commutator-preparation-transfer-and-marked-gluing|Marked gluing]] owns the block-precision formula for marks coupling distinct edge preparations.

## The raw expansion retains its scalar correction

All expectations in the following coefficients use the same \(P_G\):
\[
M(U)=\mathbb E_G[f_U^2S^{-3/2}],\qquad
N(U)=\mathbb E_G[f_U^2S^{-5/2}],\qquad
J(U)=\mathbb E_G[S^{-5/2}|\nabla f_U|^2].
\tag{SP4}
\]
These are smooth, and \(M,N\) are strictly positive. Define
\[
v(U)=\frac18\Delta N-\frac14J-\frac3{16}N,
\qquad \mathcal A=\frac14\operatorname{div}(N\nabla)+v,
\qquad c=\frac1{2\sqrt\pi}.
\tag{SP5}
\]
Then for every smooth \(\psi\), in each fixed \(C^m\) norm,
\[
\boxed{T_\alpha\psi
=c\alpha^{-3/2}\left[M\psi+\alpha^{-1}\mathcal A\psi
+O_{\psi,\beta,G,m}(\alpha^{-2})\right].}
\tag{SP6}
\]
In particular, the actual row degree is
\(d_\alpha=T_\alpha1=c\alpha^{-3/2}[M+\alpha^{-1}v+O(\alpha^{-2})]\).

Here is a remainder proof that includes small preparations. For a fixed value of \(S\), let \(\mathcal C_t\) be convolution by \(e^{-2t(1-\cos\theta)}\). The exact chord coordinate \(r=2\sin(\theta/2)\) gives the Haar radial measure \((2/\pi)r^2\sqrt{1-r^2/4}\,dr\), \(0\le r\le2\). Radial Taylor expansion therefore gives
\[
\mathcal C_t h
=ct^{-3/2}\left[h+t^{-1}\left(\frac14\Delta h-\frac3{16}h\right)\right]
+O(t^{-7/2}\|h\|_{C^4}),\qquad t>0.
\tag{SP7}
\]
For \(t\ge1\), use \(\sqrt{1-r^2/4}=1-r^2/8+O(r^4)\), \(\theta^2=r^2+O(r^4)\), and the fourth-order spherical Taylor remainder. Extending radial integrals to infinity introduces an error bounded by the same sixth radial moment. For \(t\le1\), the displayed bound follows directly from the bounded row mass and the displayed terms. Thus its constant is independent of \(t\).

Now \(T_\alpha\psi=\mathbb E_G[f_U\mathcal C_{\alpha S}(f_\bullet\psi)(U)]\). At fixed \(\beta\), every frame derivative of \(f\) is bounded by a polynomial in \(S\). Full-rank complex dimension four implies \(\mathbb E[S^{-7/2}\operatorname{poly}(S)]<\infty\): couple \(S\ge\lambda_{\min}(G)Y\) with \(Y\sim\operatorname{Gamma}(4,1)\) for the negative moment, and use Gaussian positive moments. Integrating (SP7), also after frame differentiation, proves the raw \(O(\alpha^{-7/2})\) remainder. Finally,
\(\nabla N=2\mathbb E[S^{-5/2}f\nabla f]\) and
\(\Delta N=2\mathbb E[S^{-5/2}f\Delta f]+2J\)
give (SP5). The term \(-3N/16\) is the sphere correction; it has not been discarded as an unspecified constant.

## Exact degree normalization returns the state and diffusion

Define the row-normalized Markov operator and its symmetric Haar representative by
\[
P_\alpha=d_\alpha^{-1}T_\alpha,
\qquad F_\alpha=d_\alpha^{-1/2}T_\alpha d_\alpha^{-1/2}.
\tag{SP8}
\]
The exact stationary probability of \(P_\alpha\) is
\(d\pi_\alpha=d_\alpha\,dU/\int d_\alpha\,dU\).
Its multiplication unitary to Haar \(L^2\) identifies it with \(F_\alpha\), which is a positive injective contraction with vacuum proportional to \(\sqrt{d_\alpha}\). From (SP6),
\[
\boxed{
L=\frac1{4M}\operatorname{div}(N\nabla),\qquad
d\pi=\frac{M\,dU}{\int M\,dU},\qquad
D(U)=\frac{N}{4M}.}
\tag{SP9}
\]
The drift in the fixed round metric is \(\nabla N/(4M)=\nabla D+D\nabla\log M\). Thus the potential \(v\) cancels under exact row normalization, but the state and mobility both change. The symmetric limit is
\[
\boxed{H=-\sqrt M\,L\,M^{-1/2}
=-\frac1{4\sqrt M}\operatorname{div}\!\left(N\nabla\frac{\cdot}{\sqrt M}\right),
\qquad
\mathfrak h[\psi]=\frac14\int N\left|\nabla\frac\psi{\sqrt M}\right|^2dU.}
\tag{SP10}
\]
Its form domain is \(H^1(S^3)\), operator domain \(H^2(S^3)\), and normalized vacuum is \(\sqrt{M/\int M}\). For each fixed \(\beta\), smooth positive coefficients make it uniformly elliptic. Connectedness gives a simple vacuum and a positive centered gap at that fixed parameter, without any assertion of a uniform bound as \(\beta\) changes.

The remainders give actual product limits:
\[
\boxed{P_{n/t}^{\,n}\psi\longrightarrow e^{tL}\psi,
\qquad F_{n/t}^{\,n}\psi\longrightarrow e^{-tH}\psi.}
\tag{SP11}
\]
The first convergence holds uniformly for each \(\psi\in C(S^3)\), and strongly on the fixed \(L^2(\pi)\) carrier; the second is strong on Haar \(L^2\). Convergence is uniform on bounded nonnegative time intervals, interpreting time zero as the identity. On smooth functions the one-step errors are \(O(\alpha^{-2})\); smooth diffusion orbits have bounded required norms on compact time intervals, so telescoping proves the limits. Markov contractivity gives the extension on \(C(S^3)\). Since \(\pi_\alpha/\pi\to1\) uniformly, the powers are uniformly bounded on the fixed \(L^2(\pi)\) carrier, giving its extension by density. Haar contractivity handles \(F_\alpha\). No operator-norm product convergence or joint \(\alpha,\beta\) limit is claimed.

The preparation law conditioned on the outgoing frame after integrating the next infinitesimal step is
\[
\boxed{d\nu_U(\xi)=\frac{f_U^2S^{-3/2}}{M(U)}\,dP_G(\xi),
\qquad D(U)=\frac14\mathbb E_{\nu_U}S^{-1}.}
\tag{SP12}
\]
This differs from conditioning on exactly coincident frame labels: the latter has Gaussian covariance \(\Gamma_U=(G^{-1}+\beta D_U)^{-1}\) and normalization \(w_U=\mathbb E_Gf_U^2\). In particular,
\(M=w_U\mathbb E_{\Gamma_U}S^{-3/2}\) and
\(N=w_U\mathbb E_{\Gamma_U}S^{-5/2}\).
The extra \(S^{-3/2}\) in (SP12) comes from the volume of nearby relative frames. Its logarithm adds \(-\tfrac32\log S\) to the Gaussian log density, so this local preparation law is non-Gaussian. It remains centered and invariant under a common complex phase.

## The declared tracial covariance gives closed formulas

For \(G=G_{\rm ad}=P_0+P_1/9\), write
\(U=\cos\theta\,I+i\sin\theta\,\mathbf n\cdot\boldsymbol\sigma\),
\(q=4\beta\sin^2\theta\), and \(s=\sqrt{9+q}\). The exact Laplace transform is
\[
\mathbb E_G[f_U^2e^{-uS}]
=\frac{729}{(u+1)(u+9)(u+s^2)^2}.
\tag{SP13}
\]
Its Mellin integrals at orders \(3/2\) and \(5/2\) give
\[
\boxed{
M=\frac{729\sqrt\pi(s+2)}{2s(s+1)^2(s+3)^2},\qquad
N=\frac{243\sqrt\pi(2s+3)}{(s+1)^2(s+3)^2},\qquad
D=\frac{s(2s+3)}{6(s+2)}.}
\tag{SP14}
\]
To verify the integrals, substitute \(u=r^2\) and differentiate with respect to \(s^2\) the identities
\[
\int_0^\infty\frac{r^2\,dr}{(r^2+a^2)(r^2+b^2)(r^2+s^2)}
=\frac\pi{2(a+b)(a+s)(b+s)},
\]
\[
\int_0^\infty\frac{r^4\,dr}{(r^2+a^2)(r^2+b^2)(r^2+s^2)}
=\frac{\pi(ab+as+bs)}{2(a+b)(a+s)(b+s)}.
\]
Set \(a=1,b=3\); the negative derivative inserts the second factor \((r^2+s^2)^{-1}\).

At \(\beta=0\), \(M=135\sqrt\pi/128\), \(N=243\sqrt\pi/64\), and \(D=9/10\). Thus (SP9) returns the same rotor calibration as the relative-transfer owner. At large \(q\),
\[
M\sim\frac{729\sqrt\pi}{2}q^{-2},\qquad
N\sim486\sqrt\pi\,q^{-3/2},\qquad D\sim\frac{\sqrt q}{3}.
\tag{SP15}
\]
These are pointwise large-comparison asymptotics, not estimates uniform near \(U=\pm I\). Away from those frames, increasing \(\beta\) suppresses two complex transverse preparation coordinates. The limiting scalar-and-axis Gaussian has rank two: its \(S^{-3/2}\) moment stays finite, whereas its \(S^{-5/2}\) moment diverges. Different negative moments therefore explain why concentration of the state can coexist with increasing mobility. No strong-comparison spectral limit follows from (SP15) alone; [[shared-preparation-and-the-two-center-limit|the two-center limit]] separately establishes the spectral return after taking the fixed-\(\beta\) diffusion limit.

## A fixed endpoint normalization retains a different potential

Exact row division is not the only positive normalization. Holding its leading coefficient fixed gives
\[
\widehat F_\alpha=(c\alpha^{-3/2})^{-1}M^{-1/2}T_\alpha M^{-1/2},
\qquad
\varphi_U(\xi)=\frac{S^{-3/4}f_U(\xi)}{\sqrt{M(U)}},
\qquad (W\psi)(U,\xi)=\psi(U)\varphi_U(\xi).
\tag{SP16}
\]
Since \(\mathbb E_G\varphi_U^2=1\), \(W\) is an isometry. Let \(z_t=\int e^{-2t(1-\cos\theta)}dU\). The chord Jacobian gives the exact bound
\[
z_t\le\frac2\pi\int_0^\infty r^2e^{-tr^2}dr=ct^{-3/2}.
\tag{SP17}
\]
The positive radial convolution \(\mathcal C_t\) has norm \(z_t\). Consequently
\(\widehat F_\alpha=W^*\operatorname{diag}_\xi[\mathcal C_{\alpha S}/(c(\alpha S)^{-3/2})]W\)
is an exact positive contraction. Its generator and closed form are
\[
\boxed{\widehat H=-M^{-1/2}\mathcal A M^{-1/2}=H-\frac vM,}
\]
\[
\widehat{\mathfrak h}[\psi]
=\frac14\int\mathbb E_G\!\left[S^{-1}|\nabla(\varphi_U\psi)|^2\right]dU
+\frac3{16}\int\frac NM|\psi|^2dU.
\tag{SP18}
\]
The same smooth remainder and contraction proof give
\(\widehat F_{n/t}^{\,n}\to e^{-t\widehat H}\) strongly, uniformly on bounded time intervals. The weighted gradient form is nonnegative and includes its cross terms; it need not reduce to a constant mobility plus a bare Fisher potential. Its principal mobility is still \(N/(4M)\), but its simple positive ground vector generally differs from \(\sqrt M\). At \(\beta=0\), \(\widehat H=(9/10)(-\Delta+3/4)\); subtracting its vacuum value restores the rotor. For nonzero \(\beta\), the difference \(-v/M\) is generally frame-dependent, rather than merely a choice of energy origin.

[[preparation-compression-and-the-returned-potential|Independent-preparation compression]] instead holds a separately normalized relative transfer and preparation feature fixed. Its constant mobility and Fisher potential belong to that different processing law. Here sharing the preparation correlates its local scale, feature variation and normalization.

## Source insertions retain the unmarked degrees

For fixed \(j,T\) as in (SP3), put
\[
M_{j,T}(U)=\mathbb E_G\!\left[f_U^2S^{-3/2}
e^{2\operatorname{Re}j^\dagger\xi-\xi^\dagger T\xi}\right].
\]
Using the original unmarked \(d_\alpha\), the symmetrically normalized marked operator has the limit
\[
d_\alpha^{-1/2}T_\alpha^{j,T}d_\alpha^{-1/2}\psi
\longrightarrow \frac{M_{j,T}}M\psi
\quad\text{on smooth functions and strongly in Haar }L^2.
\tag{SP19}
\]
The marked precision condition gives the same smooth expansion with marked coefficients. Since \(d_\alpha^{j,T}/d_\alpha\) converges uniformly to \(M_{j,T}/M\), it is uniformly bounded for large \(\alpha\); the weighted Schur test with weight \(\sqrt{d_\alpha}\) bounds the marked symmetric operators by this row ratio. The smooth limit therefore extends strongly to Haar \(L^2\).

The limit is a source insertion, not an identity step. The same multiplication limit holds for row normalization and fixed leading endpoints. For Hermitian directions \(B,C\),
\[
-\left.\partial_s\log M_{0,sB}\right|_0
=\mathbb E_{\nu_U}(\xi^\dagger B\xi),\qquad
\left.\partial_s\partial_t\log M_{0,sB+tC}\right|_0
=\operatorname{Cov}_{\nu_U}(\xi^\dagger B\xi,\xi^\dagger C\xi).
\tag{SP20}
\]
Renormalizing the degrees after each source insertion changes the experiment and, for a repeated marked process, its limiting stationary law. An order-one insertion repeated at every increasingly short step is not the source-free product limit (SP11); a finite continuous source perturbation needs its own scaling.

Closed chains retain the normalization explicitly. For \(U_m=U_0\),
\(\operatorname{Tr}F_\alpha^m=\int\prod_{i=0}^{m-1}[K_{\alpha,\beta}(U_i,U_{i+1})/d_\alpha(U_i)]\prod_i dU_i\).
For \(\widehat F_\alpha\), replace each denominator by \(c\alpha^{-3/2}M(U_i)\). Marks replace the declared edge kernels while these unmarked denominators stay fixed. The complete raw source response is therefore not determined by the vacuum-centered spectrum alone, as in [[closed-normalization-and-cosmic-response|the closed-normalization identity]].

The comparison duration \(1/\alpha\), covariance rule, group and normalization protocol remain inputs. The state and mobility are consequences of those inputs, with full frame support. Their identification with physical time, local gauge translations or a common cosmological response remains a separate construction.
