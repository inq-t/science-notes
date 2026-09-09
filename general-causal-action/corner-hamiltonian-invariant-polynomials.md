# The Corner Hamiltonian on Invariant Polynomials

The complete fourth-order corner response can be calculated without choosing Clebsch phases. Three unit quaternions give a five-dimensional invariant middle space, and the original nine edge Casimirs act there by an exact rational matrix. Haar moments supply its non-Euclidean Gram matrix. This independently reproduces the spin-channel calculation, including its vacuum subtraction. Splitting the shared seam edge makes the connected coefficient vanish through an exact cancellation.

**Status: exact finite-graph differential representation and rational coefficient receipt.** [[three-face-corner-and-joint-seam-response|CJ]] supplies the raw graph and physical carrier. [[corner-hamiltonian-and-the-complete-fusion-response|The complete fusion response]] owns the evaluated Hamiltonian result and its spin-channel proof. This note supplies an independent reusable calculation in invariant polynomials. No spectral or stochastic approximation is used.

## Preserve the raw edges in the differential operator

Use the actual based words \(U=apb^{-1}\), \(V=aqc^{-1}\), \(W=brc^{-1}\), where \(a,b,c\) have length one and \(p,q,r\) length two. After the axis-tree gauge fixing, identify each loop with its Hamilton quaternion
\[
U=u_0I-i\mathbf u\cdot\boldsymbol\sigma,
\qquad u_0^2+|\mathbf u|^2=1,
\]
and similarly for \(V,W\). The three quaternions have product Haar measure before simultaneous conjugation. The fundamental characters are
\[
F=2u_0,\qquad G=2v_0,\qquad H=2w_0.
\tag{IP1}
\]
Let \(\mathcal L_i,\mathcal R_i\) differentiate multiplication by \(\exp(-i\theta\sigma_i/2)\) on the left and right. On any one quaternion \(q\),
\[
\mathcal L_iq_0=\mathcal R_iq_0=-q_i/2,
\quad
\mathcal L_i\mathbf q=(q_0\mathbf e_i+\mathbf e_i\times\mathbf q)/2,
\quad
\mathcal R_i\mathbf q=(q_0\mathbf e_i+\mathbf q\times\mathbf e_i)/2.
\tag{IP2}
\]
Thus \(\mathcal C(X)=-\sum_iX_i^2\) gives the usual Casimir eigenvalue \(j(j+1)\) for a single left or right action.

The axis-link rows are \(\mathcal L_U+\mathcal L_V\), \(-\mathcal R_U+\mathcal L_W\), and \(-\mathcal R_V-\mathcal R_W\). Each exterior path contributes two copies of its loop Casimir. Consequently the actual kinetic Hamiltonian is
\[
\boxed{
H_0=\frac{4\epsilon}{3}\left[
2(\mathcal C_U+\mathcal C_V+\mathcal C_W)
+\mathcal C(\mathcal L_U+\mathcal L_V)
+\mathcal C(-\mathcal R_U+\mathcal L_W)
+\mathcal C(\mathcal R_V+\mathcal R_W)
\right].}
\tag{IP3}
\]
The opposite overall sign of the last row has no effect on its square. Equation (IP3) is the sum of the nine raw-link Casimirs, rather than a sum of independently chosen face Laplacians. It gives \(H_0F=4\epsilon F\).

Set \(\epsilon=1\) in the calculation below and restore dimensions at the end. The two nonnegative seam potentials are \(2-G\), \(2-H\). Their constant parts cancel in excitation energies; at fourth order the Hamiltonian is therefore evaluated as \(H_0-sG-tH\).

## The quartic recurrence only needs two middle pairings

For a normalized simple base eigenvector \(e\) of energy \(E_0\), let \(Q=I-|e\rangle\langle e|\) and let \(R=(H_0-E_0)^{-1}\) on \(e^\perp\), extended by zero on \(e\). The inverse is taken in the conserved seed sector: the full physical carrier for the vacuum, and the complete source-face odd sector for \(F\). In particular the other free energy-four face states do not belong to this odd-sector resolvent. Write
\[
u=RGe,\quad v=RHe,\quad
a=\langle Ge,u\rangle=\langle He,v\rangle,
\quad b=\|u\|^2=\|v\|^2.
\]
Separate seam parity removes the cross terms at second order. Grouping the six closed words with two insertions of each seam in the additive eigenvalue recurrence gives the **ordinary** \(s^2t^2\) coefficient
\[
\boxed{
e_{22}=-2\langle QGu,RQHv\rangle
-\langle Q(Hu+Gv),RQ(Hu+Gv)\rangle+2ab.}
\tag{IP4}
\]
The first two terms retain all connected resolvent words; \(2ab\) is the energy-dependent normalization contact. Four times the difference between odd and vacuum coefficients is the physical mixed derivative. [[quartic-seam-eigenvalues-and-the-generalized-pencil|The coefficient recurrence]] fixes this ordinary-power convention.

For the odd branch \(e=F\), the bilinear invariant basis \((u_0v_0,\mathbf u\cdot\mathbf v)\) has Haar Gram \(\operatorname{diag}(1,3)/16\). Direct application of (IP2)–(IP3) gives
\[
[H_0]_{UV}=\begin{pmatrix}8&-2\\-2/3&20/3\end{pmatrix},
\qquad
u=\frac87u_0v_0+\frac27\mathbf u\cdot\mathbf v,
\]
\[
v=\frac87u_0w_0-\frac27\mathbf u\cdot\mathbf w,
\qquad a=\frac27,\qquad b=\frac{19}{196}.
\tag{IP5}
\]
The reversed sign in the \(UW\) scalar-vector component is fixed by the raw \(b\)-edge orientation.

The first pairing in (IP4) vanishes exactly. Let \(\mathbb E_V\) integrate the complete \(V\) Haar variable. This orthogonal projection commutes with (IP3): integrals of left or right derivatives vanish, and every term containing a \(V\) derivative kills a \(V\)-independent function. It therefore commutes with \(Q\) and \(R\) for \(e=F\). Equation (IP5) gives \(\mathbb E_V(Gu)=aF\), hence \(QGu\in\ker\mathbb E_V\). In contrast \(QHv\) is \(V\)-independent. Their resolvent pairing is zero. The same argument applies to the vacuum branch. This removes the entire same-seam middle subspace by an exact orthogonality identity.

## The mixed middle space is five-dimensional

The remaining vector \(Hu+Gv\) is linear in each quaternion. Simultaneous conjugation rotates all three vector parts by the same \(SO(3)\) rotation. The complete invariant trilinear space has basis
\[
A=u_0v_0w_0,\quad B=u_0\mathbf v\cdot\mathbf w,
\quad C=v_0\mathbf u\cdot\mathbf w,
\quad D=w_0\mathbf u\cdot\mathbf v,
\quad E=\mathbf u\cdot(\mathbf v\times\mathbf w).
\tag{IP6}
\]
These exhaust the invariant scalar, pair-contraction and alternating three-vector tensors. The operator (IP3) preserves this space. Haar second moments \(\int q_iq_j=\delta_{ij}/4\), including \(i,j=0\), give the exact Gram matrix
\[
\Gamma=\frac1{64}\operatorname{diag}(1,3,3,3,6).
\tag{IP7}
\]
In the ordered basis (IP6), with columns denoting the images of basis vectors,
\[
\boxed{
\mathsf M=[H_0]=
\begin{pmatrix}
12&-2&2&-2&0\\
-2/3&32/3&2/3&-2/3&8/3\\
2/3&2/3&32/3&2/3&-8/3\\
-2/3&-2/3&2/3&32/3&8/3\\
0&4/3&-4/3&4/3&10
\end{pmatrix}.}
\tag{IP8}
\]
It obeys \(\Gamma\mathsf M=\mathsf M^{\mathsf T}\Gamma\), as required by the physical Haar inner product. The mixed vector and its exact resolvent are
\[
\mathsf w=\frac17(32,0,-4,4,0)^{\mathsf T},\qquad
(\mathsf M-4I)^{-1}\mathsf w
=\frac1{385}(292,76,-106,106,-64)^{\mathsf T}.
\]
Consequently
\[
\boxed{\langle Hu+Gv,R(Hu+Gv)\rangle=\frac{743}{10780}.}
\tag{IP9}
\]
No projection subtraction is needed for this mixed vector, because its seam parities are odd in both variables.

An independent spectral check within this same matrix gives energies \(6,34/3,14\), of multiplicities \(1,3,1\). The squared projection norms of \(\mathsf w\) are
\[
\frac1{16},\qquad \frac{177}{784},\qquad \frac{27}{392},
\]
respectively. Dividing by \(2,22/3,10\) reproduces (IP9). These are the five complete spin channels combined by equal energy; the invariant calculation did not assume their recoupling coefficients.

## Keep the vacuum and compare a changed graph

For the actual vacuum seed \(e=1\), \(RGe=G/4\), \(RHe=H/4\), so the mixed vector is \(GH/2\). In the bilinear basis \((v_0w_0,\mathbf v\cdot\mathbf w)\), its coordinates are \((2,0)\), the Gram is \(\operatorname{diag}(1,3)/16\), and its kinetic matrix equals the matrix in (IP5). Thus
\[
H_0^{-1}(GH/2)\longleftrightarrow (10,1)/39,
\quad
\langle GH/2,H_0^{-1}GH/2\rangle=\frac5{156}.
\]
Its contact is \(2ab=1/32\). Equation (IP4) therefore yields
\[
e_{22}^{-}=\frac{19}{343}-\frac{743}{10780}
=-\frac{1021}{75460},\qquad
e_{22}^{\Omega}=\frac1{32}-\frac5{156}=-\frac1{1248}.
\]
The resulting validation value is
\[
\boxed{\epsilon^3\partial_{g_1}^2\partial_{g_2}^2
(E_--E_\Omega)\big|_0
=4(e_{22}^{-}-e_{22}^{\Omega})
=-\frac{299687}{5885880}.}
\tag{IP10}
\]
Here \(E_-\) and \(E_\Omega\) denote the un-subtracted eigenenergies of the odd branch and vacuum. The three resolvents in the fourth-order coefficient restore \(\epsilon^{-3}\). The primary fusion-response note states the comparison in excitation-energy notation.

There is a precise geometry control. Duplicate the seam-shared axis \(c\) into independent length-one paths and split its exterior endpoint, as in [[abelian-corner-and-the-joint-seam-energy|AC14]]. This is a different ten-edge graph. It replaces only \(\mathcal C(\mathcal R_V+\mathcal R_W)\) in (IP3) by \(\mathcal C(\mathcal R_V)+\mathcal C(\mathcal R_W)\). The single-seam vectors (IP5) and their contacts are unchanged. In the same middle basis the changed matrix gives
\[
(\mathsf M_{\rm split}-4I)^{-1}\mathsf w
=\frac1{49}(32,2,-8,8,-2)^{\mathsf T},
\quad
\langle\mathsf w,R_{\rm split}\mathsf w\rangle=\frac{19}{343}.
\tag{IP11}
\]
The vacuum bilinear matrix becomes \(8I\), giving middle form \(1/32\). Both ordinary quartic coefficients consequently vanish, and so does their difference. This is an exact fourth-order cancellation after the graph change; no all-order factorization is asserted here.

The [rational quaternion receipt](receipts/corner_hamiltonian_quaternion_receipt.py) constructs every displayed matrix by applying the raw-edge vector fields to ambient polynomials, verifies the invariant closure and Haar self-adjointness, solves the resolvents exactly, and checks both graph results. Its independent agreement with the spin-channel method checks orientation, normalization and omitted-channel errors. It does not establish a volume-uniform or continuum gap.
