# Two Cubes Share One Face and One Kinetic Law

Two vertically stacked cubes have nine independent graph cycles and eleven plaquette comparisons. A single tree chart retains both compatible non-Abelian cell relations, product Haar measure and all twenty original edge Casimirs. The shared horizontal comparison can then receive weight zero or one without changing the carrier, connector paths, source algebra or kinetic operator.

**Status: exact finite graph, word, Haar and kinetic identities, with the derived quadratic forms.** Use the group, metric and faithful weighted character cost of [[weighted-character-scale-and-bounded-lie-sources|GM]]. [[closed-cube-face-words-and-the-prepared-amplitude|CW]] fixes the single-cube conventions, and [[closed-cube-raw-edge-kinetic-sewing|CK]] proves the corresponding raw-edge differentiation rule.

## One tree for both cells

Let the vertices be \((i,j,k)\), with \(i,j\in\{0,1\}\) and \(k\in\{0,1,2\}\), rooted at \(000\). Keep CW's four bottom edges \(a,b,c,p\). At height \(k=1,2\), let
\[
A_k:00k\to10k,\quad B_k:10k\to11k,\quad
C_k:01k\to11k,\quad D_k:00k\to01k.
\]
Let \(t_{ij}^{(k)}:(i,j,k-1)\to(i,j,k)\) be the eight upward edges. Choose the eleven-edge tree
\[
\mathcal T=\{a,b,c\}\cup\{t_{ij}^{(k)}:i,j=0,1,\ k=1,2\}.
\tag{TC1}
\]
The graph has twelve vertices and twenty edges, so its cycle rank is \(20-12+1=9\). The chords are
\[
(p,A_1,B_1,C_1,D_1,A_2,B_2,C_2,D_2).
\tag{TC2}
\]
Write \(b_{00}=1,b_{10}=a,b_{11}=ab,b_{01}=abc^{-1}\). The root path to \((i,j,k)\) is
\(T_{ij,k}=b_{ij}t_{ij}^{(1)}\cdots t_{ij}^{(k)}\).
Every chord or face is first based by these original paths. Gauging the tree to the identity leaves only simultaneous conjugation at the root.

Below, letters denote the resulting based chord values. Put
\[
A_0=B_0=C_0=1,\qquad D_0=p,\qquad
u=p^{-1},
\]
\[
v_k=A_{k-1}A_k^{-1},\quad
w_k=B_{k-1}B_k^{-1},\quad
x_k=C_{k-1}C_k^{-1},\quad
y_k=D_{k-1}D_k^{-1}\quad(k=1,2).
\tag{TC3}
\]
These are the eight vertical plaquettes with their original global root connectors. For example, before tree gauge the front and back raw paths are
\[
A_{k-1}t_{10}^{(k)}A_k^{-1}(t_{00}^{(k)})^{-1},
\qquad
C_{k-1}t_{11}^{(k)}C_k^{-1}(t_{01}^{(k)})^{-1},
\]
based at \(00(k-1)\) and \(01(k-1)\), respectively. The right and left paths are
\[
B_{k-1}t_{11}^{(k)}B_k^{-1}(t_{10}^{(k)})^{-1},
\qquad
D_{k-1}t_{01}^{(k)}D_k^{-1}(t_{00}^{(k)})^{-1},
\]
based at \(10(k-1)\) and \(00(k-1)\). At height zero the symbols \(A_0,B_0,C_0,D_0\) in these raw paths mean \(a,b,c,p\); their displayed values in TC3 are after tree gauge.

The three horizontal comparisons are
\[
P_0=u,\qquad P_k=A_kB_kC_k^{-1}D_k^{-1}\quad(k=1,2),
\tag{TC4}
\]
each based through \(T_{00,k}\). In particular \(P_1\) is one shared face with one fixed orientation and root port.

## Two compatible ordered closures

The inverse of TC3 is triangular:
\[
\begin{aligned}
&A_1=v_1^{-1},&&A_2=v_2^{-1}v_1^{-1},\\
&B_1=w_1^{-1},&&B_2=w_2^{-1}w_1^{-1},\\
&C_1=x_1^{-1},&&C_2=x_2^{-1}x_1^{-1},\\
&D_1=y_1^{-1}u^{-1},&&D_2=y_2^{-1}y_1^{-1}u^{-1}.
\end{aligned}
\]
Consequently
\[
\boxed{\begin{aligned}
P_1&=v_1^{-1}w_1^{-1}x_1uy_1,\\
P_2&=v_2^{-1}v_1^{-1}w_2^{-1}w_1^{-1}
x_1x_2uy_1y_2.
\end{aligned}}
\tag{TC5}
\]
To express each cell in CW's local face order, the upper side ports must also be transported. Define
\[
\widehat w_k=\operatorname{Ad}_{A_{k-1}}w_k,\qquad
\widehat x_k=\operatorname{Ad}_{A_{k-1}B_{k-1}C_{k-1}^{-1}}x_k .
\]
Then both cells obey the exact same ordered form:
\[
\boxed{P_k=v_k^{-1}\widehat w_k^{-1}
\widehat x_kP_{k-1}y_k,\qquad
\widehat w_kv_kP_ky_k^{-1}P_{k-1}^{-1}\widehat x_k^{-1}=1.}
\tag{TC6}
\]
For the lower cell the hats do nothing. For the upper cell they are
\(\widehat w_2=\operatorname{Ad}_{v_1^{-1}}w_2\) and
\(\widehat x_2=\operatorname{Ad}_{v_1^{-1}w_1^{-1}x_1}x_2\).
To verify TC6 without commuting factors, substitute
\(A_k=v_k^{-1}A_{k-1}\), and similarly for \(B,C,D\), into TC4. The product becomes
\[
v_k^{-1}A_{k-1}w_k^{-1}B_{k-1}C_{k-1}^{-1}
x_kD_{k-1}^{-1}y_k,
\]
which is exactly the right side of TC6. Thus the two relations use the same \(P_1\); neither an independent shared face nor an untransported upper-cell relation has been introduced. Conjugation leaves the central character cost unchanged, but it must still be retained in joint source words.

The raw Haar reduction is the single-tree reduction, followed by TC3:
\[
dp\prod_{k=1}^2dA_k\,dB_k\,dC_k\,dD_k
=du\prod_{k=1}^2dv_k\,dw_k\,dx_k\,dy_k.
\tag{TC7}
\]
At each step, conditional on the lower-plane variables, inversion and multiplication preserve Haar. Hence this is a global measure identity, and the physical carrier is \(L^2(G^9)^{\operatorname{Ad}G}\). Every bounded joint mark of the eleven comparisons is pulled back using TC3–5, with the original root indices or their stated contraction retained.

## All twenty original edge derivatives

Use CK1's multiplication-side convention
\(L_z(X):z\mapsto e^{tX}z\), \(R_z(X):z\mapsto ze^{tX}\).
The nine chord rows are their nine \(L_z(X)\) fields. The remaining eleven rows are:

| Raw tree edge | Induced field, with common argument \(X\) |
|---|---|
| \(a\) | \(-R_p+\sum_{j=1}^2[-R_{A_j}+(L_{B_j}-R_{B_j})+(L_{C_j}-R_{C_j})-R_{D_j}]\) |
| \(b\) | \(-R_p+\sum_{j=1}^2[-R_{B_j}+(L_{C_j}-R_{C_j})-R_{D_j}]\) |
| \(c\) | \(R_p+\sum_{j=1}^2[-L_{C_j}+R_{D_j}]\) |
| \(t_{00}^{(k)}\), \(k=1,2\) | \(\sum_{j=k}^2(L_{A_j}+L_{D_j})\) |
| \(t_{10}^{(k)}\), \(k=1,2\) | \(\sum_{j=k}^2(-R_{A_j}+L_{B_j})\) |
| \(t_{01}^{(k)}\), \(k=1,2\) | \(\sum_{j=k}^2(L_{C_j}-R_{D_j})\) |
| \(t_{11}^{(k)}\), \(k=1,2\) | \(\sum_{j=k}^2(-R_{B_j}-R_{C_j})\) |

These follow directly from the root paths: varying \(t_{ij}^{(k)}\) changes every endpoint on its column at heights at least \(k\). The backward occurrence of \(c\) has sign \(-1\). More formally, each tree row is
\(\sum_z\epsilon(\mathrm s_z)L_z-\epsilon(\mathrm t_z)R_z\), where \(\epsilon\) is its signed root-path occurrence. As in CK2, the whole raw-edge curve is a product of these left and right flows, so this determines exact second derivatives as well.

For a \(Q\)-orthonormal color basis the reduced operator is therefore
\[
\boxed{\mathsf C_{\mathrm{two},Q}
=-\sum_{e=1}^{20}\sum_{\alpha=1}^{d}\mathcal D_e(e_\alpha)^2.}
\tag{TC8}
\]
Every row is skew-adjoint for product chord Haar. The nine chord rows alone span the tangent space, so this is a smooth elliptic compact-cover operator. Its nonnegative self-adjoint closure on root-invariant functions is unitarily the original twenty-edge Casimir. TC3 supplies an exact pushforward to face coordinates: substitute the inverse chart into each complete vector field before squaring, retaining every variable adjoint coefficient.

## The principal matrix on the common carrier

Use face-log order
\[
\xi=(U,V_1,W_1,X_1,Y_1,V_2,W_2,X_2,Y_2).
\]
The linear chart at the identity is
\[
U=-P,\quad
(V_1,W_1,X_1,Y_1)=(-\mathsf A_1,-\mathsf B_1,-\mathsf C_1,P-\mathsf D_1),
\]
\[
(V_2,W_2,X_2,Y_2)
=(\mathsf A_1-\mathsf A_2,\mathsf B_1-\mathsf B_2,
\mathsf C_1-\mathsf C_2,\mathsf D_1-\mathsf D_2).
\tag{TC9}
\]
Here the sans-serif letters are chord Lie coordinates. Applying TC9 to the twenty row symbols and summing their outer products gives
\[
\boxed{\mathsf A_9=
\begin{pmatrix}
4&1&1&-1&-1&0&0&0&0\\
1&4&-1&0&1&-1&0&0&0\\
1&-1&4&1&0&0&-1&0&0\\
-1&0&1&4&-1&0&0&-1&0\\
-1&1&0&-1&4&0&0&0&-1\\
0&-1&0&0&0&4&-1&0&1\\
0&0&-1&0&0&-1&4&1&0\\
0&0&0&-1&0&0&1&4&-1\\
0&0&0&0&-1&1&0&-1&4
\end{pmatrix}.}
\tag{TC10}
\]
The two horizontal linear forms are
\[
\ell_1=(1,-1,-1,1,1,0,0,0,0)^\top,\qquad
\ell_2=(1,-1,-1,1,1,-1,-1,1,1)^\top.
\]
Thus the eleven-face incidence Gram is \(N\mathsf A_9N^\top\), where
\(N=(I_9,\ell_1,\ell_2)^\top\). It has rank nine, diagonal entries four, and null vectors
\((-\ell_1,1,0)\), \((-\ell_2,0,1)\), the two linearized cell relations. This gives a check on the original-edge count as well as the connector signs.

## Vary one shared-face cost without resetting the law

The ten exterior faces are \(u\), the eight vertical faces, and \(P_2\). For \(0\le\tau\le1\), retain the actual family
\[
\boxed{
H_\tau=\kappa\mathsf C_{\mathrm{two},Q}
+g\left[
W_A(u)+\sum_{k=1}^2\{W_A(v_k)+W_A(w_k)+W_A(x_k)+W_A(y_k)\}
+W_A(P_2)+\tau W_A(P_1)\right].}
\tag{TC11}
\]
At \(\tau=1\) every distinct plaquette is counted once; at \(\tau=0\) only the shared-face cost is omitted. All twenty edge terms, both closure relations and every word mark remain. Summing two isolated cube Hamiltonians would count the four shared edges twice, as well as count the shared-face potential twice; it is not TC11.

The common scale remains GM's \(g_{\rm eff}=2I_Ag\), \(h=(\kappa/g_{\rm eff})^{1/4}\), \(E=\kappa/h^2\), since the exterior coefficients are fixed. The harmonic forms are
\[
\boxed{\mathsf B_\tau=I_9+\ell_2\ell_2^\top+\tau\ell_1\ell_1^\top,\qquad
\mathcal O_\tau=-\nabla^\top\mathsf A_9\nabla
+\frac14\xi^\top\mathsf B_\tau\xi,}
\tag{TC12}
\]
with \(Q\) contracting each color pair. The nine independent face costs already have a unique common identity well for every \(\tau\), by faithfulness and \(A>0\). This states a geometric input, not a compact spectral limit.

At a supplied magnetic duration \(s\), the corresponding sourced magnetic integral is the product-Haar integral of the pulled-back joint mark times the exponential of \(-sg\) times the entire bracketed cost in TC11. It retains one normalization and one shared-face factor. Its normalized likelihood is distinct from the interacting vacuum of \(H_\tau\).

TC8 and TC11 specify the exact finite comparison. [[two-cube-interior-cost-and-the-joint-bracket-response|The harmonic spectrum and fixed joint bracket response]] evaluate this declared family while retaining its common carrier and clock. [[two-cube-temporal-sewing-and-the-actual-joint-source|TJ]] supplies the shared temporal history, actual vacuum caps and the specified compact joint-source response. These results do not select the coupling, group or preparation. Uniform sewing of larger collections of cells and a three-dimensional bulk construction require further results.
