# Closed Cube Raw-Edge Kinetic Sewing

The twelve edge Casimirs of a cube induce a coupled sum of squares on its five independent based loops. Keeping the tree transports gives the exact operator in both chord and face coordinates. Its harmonic kinetic matrix and the dependent sixth-face potential together have frequencies \(2,2,2,\sqrt6,\sqrt6\); neither matrix can be replaced by five independently prepared face oscillators.

**Status: exact compact graph operator and exact harmonic calculation.** Use the graph, tree, face words and Haar unitary of [[closed-cube-face-words-and-the-prepared-amplitude|CW]], and the fixed compact connected simple group, metric, faithful representation and positive commuting cost weight of [[weighted-character-scale-and-bounded-lie-sources|GM]]. The harmonic statements below concern this fixed closed boundary, not a growing three-dimensional lattice or a continuum gap.

## Differentiate the original edges before eliminating the tree

For a Lie algebra vector \(X\), define the multiplication-side fields on a coordinate \(z\) by
\[
L_z(X)f=\left.\frac d{dt}f(\ldots,e^{tX}z,\ldots)\right|_{t=0},
\qquad
R_z(X)f=\left.\frac d{dt}f(\ldots,ze^{tX},\ldots)\right|_{t=0}.
\tag{CK1}
\]
Both are skew-adjoint for product Haar. The notation specifies multiplication side, independently of conventions for naming invariant vector fields.

The root paths to the bottom vertices are \(1,a,ab,abc^{-1}\); the four top paths append \(t_{00},t_{10},t_{11},t_{01}\), respectively. If a tree edge \(e\) is changed from the identity to \(e^{tX}\) on the tree-gauge slice, let \(\epsilon_e(z)\in\{-1,0,1\}\) record its oriented occurrence in the root path to \(z\). Every based chord then changes exactly as
\[
z_j(t)=e^{t\epsilon_e(\mathrm s_j)X}\,z_j\,
e^{-t\epsilon_e(\mathrm t_j)X},
\qquad
\mathcal D_e(X)=
\sum_j\bigl(\epsilon_e(\mathrm s_j)L_j(X)
-\epsilon_e(\mathrm t_j)R_j(X)\bigr).
\tag{CK2}
\]
The subtree reached through \(c\) contains \(010,011\) and has sign \(-1\), since the root path traverses \(c^{-1}\). This fixes the backward-edge signs.

In chord order \((p,A,B,C,D)\), the complete table is as follows. Every field in a row has the same argument \(X\).

| Raw edge | Induced field \(\mathcal D_e(X)\) |
|---|---|
| \(p,A,B,C,D\) | \(L_p,L_A,L_B,L_C,L_D\), respectively |
| \(a\) | \(-R_p-R_A+(L_B-R_B)+(L_C-R_C)-R_D\) |
| \(b\) | \(-R_p-R_B+(L_C-R_C)-R_D\) |
| \(c\) | \(R_p-L_C+R_D\) |
| \(t_{00}\) | \(L_A+L_D\) |
| \(t_{10}\) | \(-R_A+L_B\) |
| \(t_{01}\) | \(L_C-R_D\) |
| \(t_{11}\) | \(-R_B-R_C\) |

For a \(Q\)-orthonormal basis \((e_\alpha)_{\alpha=1}^d\), the exact reduced Casimir and form are
\[
\boxed{\mathsf C_{\mathrm{cube},Q}
=-\sum_{e=1}^{12}\sum_{\alpha=1}^d\mathcal D_e(e_\alpha)^2,}
\qquad
\mathfrak c(f)=\sum_{e,\alpha}\|\mathcal D_e(e_\alpha)f\|_2^2.
\tag{CK3}
\]
Their physical restriction is to \(L^2(G^5)^{\operatorname{Ad}G}\). Indeed, CW's Haar unitary identifies this space with the full raw Gauss-invariant carrier. CK2 describes the entire raw one-parameter curve, so its second derivative is \(\mathcal D_e(X)^2\), not merely the square of a principal symbol. At another tree representative the color basis is adjoint-rotated; summing in \(Q\) leaves CK3 unchanged. Thus no connection or ordering term has been discarded.

The simultaneous root generator \(\sum_j(L_j-R_j)\) annihilates physical functions, but no such simplification was used in the table. The five chord rows already span every tangent direction on \(G^5\); CK3 is a smooth elliptic sum of squares on this compact cover. Its nonnegative self-adjoint closure, restricted to root invariants, is the original electric operator.

## Transport the full vector fields to face coordinates

Use
\[
u=p^{-1},\quad v=A^{-1},\quad w=B^{-1},\quad
x=C^{-1},\quad y=pD^{-1}.
\tag{CK4}
\]
For example,
\[
L_p\mapsto-R_u+L_y,\qquad
R_p(X)\mapsto-L_u(X)+L_y(\operatorname{Ad}_{u^{-1}}X),
\]
\[
L_D\mapsto-R_y,\qquad
R_D(X)\mapsto-L_y(\operatorname{Ad}_{u^{-1}}X).
\tag{CK5}
\]
Inversion sends \(L_A\mapsto-R_v\) and \(R_A\mapsto-L_v\), and likewise for \(B,w\) and \(C,x\). Consequently the exact face-coordinate table is:

| Raw edge | Induced field |
|---|---|
| \(p\) | \(-R_u+L_y\) |
| \(A\) | \(-R_v\) |
| \(B\) | \(-R_w\) |
| \(C\) | \(-R_x\) |
| \(D\) | \(-R_y\) |
| \(a\) | \(L_u+L_v+(L_w-R_w)+(L_x-R_x)\) |
| \(b\) | \(L_u+L_w+(L_x-R_x)\) |
| \(c\) | \(-L_u+R_x\) |
| \(t_{00}\) | \(-R_v-R_y\) |
| \(t_{10}\) | \(L_v-R_w\) |
| \(t_{01}\) | \(-R_x(X)+L_y(\operatorname{Ad}_{u^{-1}}X)\) |
| \(t_{11}\) | \(L_w+L_x\) |

The only displayed transported coefficient is in \(t_{01}\). That row leaves \(u\) fixed, so its own differentiation of this coefficient is zero. More generally CK3 always squares the whole transported vector field. CW5 preserves product Haar, hence the displayed fields remain divergence-free and yield the same form.

## The incidence and dependent-face quadratic forms

Write \((u,v,w,x,y)=(e^{hU},e^{hV},e^{hW},e^{hX},e^{hY})\) and \(\xi=(U,V,W,X,Y)\). At the identity the twelve rows, in the order used above, are the following integer incidence matrix:
\[
S=\begin{pmatrix}
-1&0&0&0&1\\
0&-1&0&0&0\\
0&0&-1&0&0\\
0&0&0&-1&0\\
0&0&0&0&-1\\
1&1&0&0&0\\
1&0&1&0&0\\
-1&0&0&1&0\\
0&-1&0&0&-1\\
0&1&-1&0&0\\
0&0&0&-1&1\\
0&0&1&1&0
\end{pmatrix},
\qquad
\boxed{\mathsf A=S^\top S=
\begin{pmatrix}
4&1&1&-1&-1\\
1&4&-1&0&1\\
1&-1&4&1&0\\
-1&0&1&4&-1\\
-1&1&0&-1&4
\end{pmatrix}.}
\tag{CK6}
\]
The sixth face has linear logarithm \(\ell^\top\xi\), where
\[
\ell=(1,-1,-1,1,1)^\top,\qquad
\mathsf B=I+\ell\ell^\top,\qquad
\mathsf B^{-1}=I-\frac{\ell\ell^\top}{6}.
\tag{CK7}
\]
The symbol \(\mathsf B\) denotes the magnetic Hessian, not the chord \(B\) or GM's preparation weight \(A\). With GM's \(g_{\rm eff}=2I_Ag\), \(h=(\kappa/g_{\rm eff})^{1/4}\) and \(E=\kappa/h^2\), the leading scaled Hamiltonian is
\[
\boxed{\mathcal O_{\mathrm{cube}}
=-\sum_{i,j}\mathsf A_{ij}Q(\nabla_i,\nabla_j)
+\frac14\sum_{i,j}\mathsf B_{ij}Q(\xi_i,\xi_j).}
\tag{CK8}
\]
The extra \(\ell\ell^\top\) is the retained sixth comparison. The kinetic off-diagonal entries come from the original shared edges.

Direct multiplication gives
\[
\mathsf A\mathsf B=
\begin{pmatrix}
4&1&1&-1&-1\\
0&5&0&-1&0\\
0&0&5&0&-1\\
0&-1&0&5&0\\
0&0&-1&0&5
\end{pmatrix},
\qquad
(\mathsf A\mathsf B-4I)(\mathsf A\mathsf B-6I)=0.
\tag{CK9}
\]
Its eigenvalues are \(4\) three times and \(6\) twice. Equivalently, put \(N=(I_5,\ell)^\top\) and \(\mathsf A_6=N\mathsf A N^\top\). Its null vector is \((-\ell,1)\). Conjugating by the diagonal matrix of this vector's signs turns \(\mathsf A_6\) into the octahedral graph Laplacian \(4I-\operatorname{Adj}\), with opposite pairs \((1,6),(2,4),(3,5)\). This is the cube boundary's face-incidence identity.

## The inherited Gaussian and its physical harmonic level

Let \(\Sigma\) be the component covariance in the square of the normalized harmonic ground state: \(\mathbb E[\xi_i^\alpha\xi_j^\beta]=\Sigma_{ij}\delta_{\alpha\beta}\). The positive solution of \(\Sigma\mathsf B\Sigma=\mathsf A\) is
\[
\boxed{\Sigma=(6-2\sqrt6)\mathsf B^{-1}
+\frac{\sqrt6-2}{2}\mathsf A.}
\tag{CK10}
\]
To verify this, use CK9 to get
\(\mathsf A\mathsf B\mathsf A=10\mathsf A-24\mathsf B^{-1}\).
Equivalently,
\[
\Sigma=\mathsf B^{-1/2}
\bigl(\mathsf B^{1/2}\mathsf A\mathsf B^{1/2}\bigr)^{1/2}
\mathsf B^{-1/2}.
\]
The projectors
\[
P_4=\frac{6I-\mathsf A\mathsf B}{2},\qquad
P_6=\frac{\mathsf A\mathsf B-4I}{2},\qquad
\Sigma\mathsf B=2P_4+\sqrt6P_6
\tag{CK11}
\]
are orthogonal in the \(\mathsf B\) inner product; conjugation by \(\mathsf B^{1/2}\) gives Euclidean orthogonal projectors. No nonsymmetric matrix is treated as Euclidean self-adjoint.

For direct use in the dependent word, reorder and sign the variables as \(Z=(-V,-W,X,U,Y)\). Their covariance has diagonal \(1+\sqrt6/3\), ordinary off-diagonal entries \(-\sqrt6/6\), and the two exceptional off-diagonal pairs \((1,3),(2,5)\) equal \(-1+\sqrt6/3\). In particular, this is an inherited correlated Gaussian law.

An orthogonal diagonalization after \(\xi\mapsto\mathsf B^{1/2}\xi\) gives five mode frequencies
\[
(\omega_1,\ldots,\omega_5)=(2,2,2,\sqrt6,\sqrt6),\qquad
e_{\Omega}=d(3+\sqrt6),\qquad
\boxed{\Delta_{\mathrm{harm,phys}}=4.}
\tag{CK12}
\]
For a simple Lie algebra the one-quantum adjoint representation has no invariant vector. Two quanta in any lowest mode have the invariant quadratic \(Q(Y,Y)\), so the first physical excitation has energy \(2\cdot2=4\). There are six such scalar states from the symmetric pairings of the three lowest modes. The raw common-root Gauss action is retained throughout.

CK3 supplies the actual compact kinetic operator; CK8–12 identify its harmonic well. The passage to actual compact vacuum, source and chronological limits is the separate [[closed-cube-bracket-source-and-the-actual-vacuum-return|fixed-cube localization and source-return argument]]. A fixed-cube return does not establish uniformity over shared cells or a three-dimensional bulk construction. The ordered sixth-face word and the actual twelve-edge operator must both survive any such extension.
