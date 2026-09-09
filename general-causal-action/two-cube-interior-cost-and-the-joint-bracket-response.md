# The Interior Face Changes the Joint Bracket Response

Two cubes sharing a face have a harmonic law selected by twenty edge Casimirs and eleven face comparisons. Removing only the interior magnetic cost changes a three-mode block while preserving the original source words and electric operator. A fixed bounded bracket mark involving all three horizontal faces has a strictly larger leading expectation in that control. Its centered harmonic spectral edge also changes, with a disappearing low-energy weight that must be retained when interpreting compact source return.

**Status: exact harmonic spectrum, covariance and marked response for the supplied two-cube Hamiltonian.** [[two-cube-shared-face-and-the-original-kinetic-law|TC]] owns the graph, common-root words, product Haar chart and complete raw-edge operator. The group, metric, faithful representation, positive commuting preparation weight and bounded source are those of [[weighted-character-scale-and-bounded-lie-sources|GM]]. All conclusions below concern this fixed complex. The covariance is the oscillator vacuum covariance, not a magnetic likelihood.

## Change one cost while retaining every edge and word

Use TC's independent face coordinates
\[
(u,v_1,w_1,x_1,y_1,v_2,w_2,x_2,y_2)
=\exp h(U,V_1,W_1,X_1,Y_1,V_2,W_2,X_2,Y_2).
\]
The horizontal faces are \(P_0=u\), the shared face \(P_1\), and the upper face \(P_2\). Their exact words and connectors are TC5–6. In particular their linear logarithms are
\[
H_0=U,\qquad
H_1=U-V_1-W_1+X_1+Y_1,\qquad
H_2=H_1-V_2-W_2+X_2+Y_2.
\tag{TI1}
\]
Let \(0\le\tau\le1\) multiply only the cost of \(P_1\). All ten exterior costs have weight one. With the original GM scale,
\[
\widehat H_{\tau,h}
=h^2\mathsf C_{\mathrm{raw},Q}
+h^{-2}\left(\sum_{F\ {\rm exterior}}w_A(F)+\tau w_A(P_1)\right),
\quad
w_A=\frac{W_A}{2I_A},\quad
h=\left(\frac{\kappa}{2I_Ag}\right)^{1/4},\quad E=\kappa h^{-2}.
\tag{TI2}
\]
Every one of the twenty raw edge Casimirs occurs once. In particular, the four edges bounding \(P_1\) are neither deleted nor doubled. The \(\tau=0\) control retains \(P_1\) as the same original marked word.

## Reduce the inherited kinetic form by the square symmetry

For each slab put
\[
b_k=(-V_k,-W_k,X_k,Y_k),\qquad
e=\tfrac12(1,1,1,1)^{\mathsf T},\qquad c_k=e^{\mathsf T}b_k .
\]
In coordinates \((U,b_1,b_2)\), TC10's kinetic matrix has block form
\[
A_9=
\begin{pmatrix}
4&-\mathbf1^{\mathsf T}&0\\
-\mathbf1&D&-I_4\\
0&-I_4&D
\end{pmatrix},
\qquad
D=4I_4-\operatorname{Adj}(C_4).
\tag{TI3}
\]
Here the cyclic side order is front, right, back, left. The eigenvalues of \(D\) are \(2\) on \(e\), \(4\) on a two-dimensional space, and \(6\) on the alternating side vector. The only dependent-face linear forms use \(U,c_1,c_2\), so the other angular sectors have magnetic matrix \(I\).

For each angular eigenvalue \(d_a\in\{4,4,6\}\), the two-slab kinetic matrix and its vacuum covariance are
\[
A(d_a)=\begin{pmatrix}d_a&-1\\-1&d_a\end{pmatrix},
\qquad
\Sigma(d_a)=
\frac12
\begin{pmatrix}
\sqrt{d_a-1}+\sqrt{d_a+1}&\sqrt{d_a-1}-\sqrt{d_a+1}\\
\sqrt{d_a-1}-\sqrt{d_a+1}&\sqrt{d_a-1}+\sqrt{d_a+1}
\end{pmatrix}.
\tag{TI4}
\]
Thus these six modes have squared frequencies \(3,3,5,5,5,7\), independently of \(\tau\). These are probability covariances in the square of the oscillator vacuum.

The constant angular kinetic block on \((U,c_1,c_2)\) is
\[
\begin{pmatrix}4&-2&0\\-2&2&-1\\0&-1&2\end{pmatrix}.
\]
The invertible transformation to the three horizontal variables is
\[
(H_0,H_1,H_2)=(U,U+2c_1,U+2c_1+2c_2).
\]
It changes this kinetic matrix to \(4I_3\). The quadratic magnetic cost on this sector is
\[
H_0^2+\tau H_1^2+H_2^2
+\frac{(H_1-H_0)^2+(H_2-H_1)^2}{4},
\]
with \(Q\) understood in each color. Therefore
\[
\boxed{
\mathcal O_{\tau,\mathrm{hor}}
=-4\Delta_H+\frac1{16}H^{\mathsf T}L_\tau H,\qquad
L_\tau=
\begin{pmatrix}
5&-1&0\\
-1&2+4\tau&-1\\
0&-1&5
\end{pmatrix},\qquad
\operatorname{Cov}_0(H)=4L_\tau^{-1/2}.}
\tag{TI5}
\]
Together with TI4 and the inverse coordinate transformations, TI5 gives the entire nine-face vacuum covariance. It retains the interior comparison through \(L_\tau\); it is not the inverse of the magnetic Hessian.

## The complete harmonic spectrum

Set
\[
H_{\rm o}=\frac{H_0-H_2}{\sqrt2},\qquad
H_{\rm e}=\frac{H_0+H_2}{\sqrt2}.
\]
The odd outer combination has squared frequency \(5\). On \((H_{\rm e},H_1)\),
\[
M_\tau=
\begin{pmatrix}5&-\sqrt2\\-\sqrt2&2+4\tau\end{pmatrix},
\qquad
\lambda_\pm(\tau)
=\frac{7+4\tau\pm\sqrt{17-24\tau+16\tau^2}}2 .
\tag{TI6}
\]
The rank-one magnetic change is \(M_\tau=M_1-4(1-\tau)e_2e_2^{\mathsf T}\). The complete multiset of nine squared frequencies is
\[
\boxed{\{3^{[2]},\,5^{[4]},\,7,\,\lambda_-(\tau),\,\lambda_+(\tau)\}.}
\tag{TI7}
\]
In particular, at \(\tau=1\) it is
\(\{3^{[2]},4,5^{[4]},7^{[2]}\}\), and at \(\tau=0\) the distinguished pair is \((7\pm\sqrt{17})/2\).

Let \(d=\dim\mathfrak g\). The harmonic vacuum energy is
\[
e_0(\tau)=\frac d2\left(2\sqrt3+4\sqrt5+\sqrt7+
\sqrt{\lambda_-(\tau)}+\sqrt{\lambda_+(\tau)}\right).
\]
Each one-quantum color space is adjoint and has no invariant vector for a simple Lie algebra. An invariant radius of a lowest mode supplies a two-quantum state. Hence the full physical harmonic gap is
\[
\boxed{\Delta_{\rm harm,phys}(\tau)
=2\sqrt{\min\{3,\lambda_-(\tau)\}},\qquad
\lambda_-(1/2)=3.}
\tag{TI8}
\]
The incidence-dependent change in TI7–8 is already present for Abelian oscillators. The simple-group Gauss selection and the bracket mark below are separate facts. For an Abelian adjoint action, one-quantum states are themselves physical.

## One fixed joint source and its exact coefficient

Use the original bounded equivariant GM mark, without replacing it by a logarithm:
\[
\boxed{
\mathcal A=2\bigl(q_\rho(P_0)-q_\rho(P_1)\bigr),\qquad
\mathcal B=2\bigl(q_\rho(P_2)-q_\rho(P_1)\bigr),\qquad
\mathcal M=Q([\mathcal A,\mathcal B],[\mathcal A,\mathcal B]).}
\tag{TI9}
\]
All three based faces use the same root port. The mark is bounded, real, nonnegative and gauge invariant; it vanishes identically for an Abelian Lie algebra. The exact word of the shared face occurs at both values of \(\tau\).

GM's normalization \(2q_\rho(e^{hX})=hX+O(h^3)\), together with TC's dependent-word expansion, gives the local source limit
\[
h^{-4}\mathcal M\longrightarrow
P=Q([H_0-H_1,H_2-H_1],[H_0-H_1,H_2-H_1]).
\tag{TI10}
\]
The dependent horizontal words can have second-order logarithmic terms. They contribute only to subsequent source orders in TI10.

Put \(E_{\rm b}=(H_0+H_2-2H_1)/\sqrt2\) and \(O_{\rm b}=(H_0-H_2)/\sqrt2\). The two differences in TI10 have bracket \(-[E_{\rm b},O_{\rm b}]\). These two color vectors are independent in the harmonic vacuum, and
\[
v_O=\operatorname{Var}(O_{\rm b}^a)=\frac4{\sqrt5},\qquad
v_E=\operatorname{Var}(E_{\rm b}^a)=4s_\tau,\qquad
s_\tau=w^{\mathsf T}M_\tau^{-1/2}w,\quad w=(1,-\sqrt2)^{\mathsf T}.
\]
For \(r_\tau=\sqrt{8+20\tau}\), the two-dimensional inverse-square-root identity yields
\[
\boxed{
s_\tau=\frac{8+4\tau+3r_\tau}
{r_\tau\sqrt{7+4\tau+2r_\tau}},\qquad
\mathbb E_{0,\tau}P=\frac{16F_Q}{\sqrt5}s_\tau,\qquad
F_Q=\sum_{abc}Q(e_a,[e_b,e_c])^2.}
\tag{TI11}
\]
Indeed \(M^{-1/2}=((\operatorname{Tr}M+\sqrt{\det M})I-M)/
(\sqrt{\det M}\sqrt{\operatorname{Tr}M+2\sqrt{\det M}})\). The color contraction is
\(\mathbb E Q([E_{\rm b},O_{\rm b}],[E_{\rm b},O_{\rm b}])=F_Qv_Ev_O\).
Equivalently \(v_Ev_O\) is the determinant of the covariance of the two original differences.

The endpoints are explicit:
\[
\boxed{
\mathbb E_{0,1}P=\frac{48F_Q}{\sqrt{35}},\qquad
\mathbb E_{0,0}P=
\frac{16F_Q(3+2\sqrt2)}{\sqrt{5(7+4\sqrt2)}}.}
\tag{TI12}
\]
The second is strictly larger. In fact the harmonic response strictly decreases throughout the interval. The resolvent formula gives
\[
\frac{d s_\tau}{d\tau}
=-\frac4\pi\int_0^\infty
t^{-1/2}\left|e_2^{\mathsf T}(M_\tau+tI)^{-1}w\right|^2\,dt<0,
\]
because
\[
e_2^{\mathsf T}(M_\tau+tI)^{-1}w
=-\frac{\sqrt2(4+t)}{\det(M_\tau+tI)}\ne0.
\]
There is an explicit uniform margin. Write \(R_{\tau,t}=(M_\tau+tI)^{-1}\). Differentiating this finite positive-matrix resolvent once more gives
\[
s_\tau''=\frac{32}{\pi}\int_0^\infty
t^{-1/2}(e_2^{\mathsf T}R_{\tau,t}e_2)
\left|e_2^{\mathsf T}R_{\tau,t}w\right|^2\,dt>0.
\]
At \(\tau=1\), \(M_1w=7w\), so \(s_1'=-4/7^{3/2}\). Consequently, with \(D(\tau)=16s_\tau/\sqrt5\),
\[
\boxed{D'(\tau)\le D'(1)=-\frac{64}{7\sqrt{35}}<0
\qquad(0\le\tau\le1).}
\]
This is a response of the same bracket source under a changed interior cost. It is not a source insertion into an independently prepared product of cubes, nor an assertion about a correction to the full compact gap.

## The scalar source has a disappearing low-energy weight

Let \(C_{\rm ad}=F_Q/d\). Contracting one Gaussian pair in \(P=|[E_{\rm b},O_{\rm b}]|^2\) gives its exact degree-two Hermite part,
\[
P^{[2]}=C_{\rm ad}\left[
v_O\bigl(|E_{\rm b}|^2-dv_E\bigr)
+v_E\bigl(|O_{\rm b}|^2-dv_O\bigr)\right].
\tag{TI13}
\]
Its remaining centered part has degree four, with exactly two quanta from each of the independent even and odd sectors. Formula TI13 suffices to determine the lowest visible energy.

Let \(\Pi_-(\tau)\) be the Euclidean spectral projector of \(M_\tau\) onto \(\lambda_-(\tau)\). Then
\[
c_-(\tau)=\|\Pi_-(\tau)w\|^2
=\frac{3\lambda_+(\tau)-13-8\tau}{\lambda_+(\tau)-\lambda_-(\tau)}.
\tag{TI14}
\]
For \(0\le\tau<1\), \(c_-(\tau)>0\). To see the only possible zero, \(w\) would have to be an eigenvector of \(M_\tau\); direct multiplication forces \(\tau=1\), when its eigenvalue is \(7\). The weight of the primitive even vector in the slow oscillator is \(4c_-/\sqrt{\lambda_-}\), but the squared norm of the scalar source's projection onto energy \(2\sqrt{\lambda_-}\) is
\[
\boxed{
\left\|\mathbf1_{\{2\sqrt{\lambda_-}\}}(K_{0,\tau})
(P-\mathbb EP)\Omega_\tau\right\|^2
=2dC_{\rm ad}^2v_O^2
\left(\frac{4c_-(\tau)}{\sqrt{\lambda_-(\tau)}}\right)^2>0
\quad(0\le\tau<1).}
\tag{TI15}
\]
At isolated coincidences with another source energy this formula still gives the squared norm of the pure slow-radius component, and is a lower bound for the entire spectral projection.

Consequently the centered harmonic source's cyclic spectral edge is
\[
\boxed{\lambda_{P,\mathrm{harm}}(\tau)=
\begin{cases}
2\sqrt{\lambda_-(\tau)},&0\le\tau<1,\\
2\sqrt5,&\tau=1.
\end{cases}}
\tag{TI16}
\]
At \(\tau=1\), \(w\) is entirely in the frequency-\(\sqrt7\) sector, while \(O_{\rm b}\) has frequency \(\sqrt5\). The six remaining angular modes are absent from this horizontal source. Thus its harmonic edge exceeds the full physical gap \(2\sqrt3\).

The weight loss is quantitative:
\[
c_-(\tau)=\frac{32}{27}(1-\tau)^2+O((1-\tau)^3).
\]
The primitive covariance weight vanishes quadratically; the scalar low-radius weight in TI15 vanishes to fourth order. This distinguishes a disappearing spectral weight from a uniform positive gap estimate.

## Compact return must retain the distinction between a profile and its edge

TI10–12 are local source jets and their evaluated harmonic expectations. [[two-cube-temporal-sewing-and-the-actual-joint-source|TJ]] now supplies actual compact expectations, the mixed chronological profile and a strictly negative actual attachment derivative uniformly in \(\tau\), using TC's nine-coordinate kinetic operator and both dependent faces. The proof extends [[closed-cube-bracket-source-and-the-actual-vacuum-return|CQ's]] fixed-complex localization. The marks remain bounded before multiplication by \(h^{-4}\); their growing normalization is paid by higher-order vacuum accuracy.

Even actual vector and chronological-profile return does not by itself imply convergence to TI16's source edge when that edge lies above the full physical gap. Small additional actual spectral weight can occupy lower levels. For \(\tau\le1/2\), TI16 coincides with TI8, so a returned nonzero low component and the full-gap lower bound can provide a matching sandwich. For \(\tau>1/2\), such a source-edge conclusion requires further support control. [[chronological-cyclic-sources-and-the-innovation-floor|CS]] explains why this matters for the infimum over an entire chronological carrier.

The spectrum and the joint expectation both detect the retained interior incidence, but the bracket response is not the cause of the harmonic gap change. No group, preparation, clock, growing-complex coercivity or continuum dynamics has been selected by this fixed comparison.
