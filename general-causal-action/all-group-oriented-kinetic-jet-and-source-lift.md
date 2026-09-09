# The Oriented Kinetic Jet and Source Lift for Every Compact Simple Group

The four-face odd normal form is a consequence of the actual edge words, the Lie bracket and an invariant metric. After calibrating the magnetic Hessian, every compact connected group with simple Lie algebra has the same rational first-order coefficient tables. This includes the repeated-mode angular terms and the complete ten-dimensional quadratic source lift. The result does not use quaternion multiplication, a Clifford identity or a choice of global form invisible to the declared faithful representation.

**Status: exact general-group first kinetic jet, polynomial-core normal form and quadratic-source lift.** [[weighted-character-scale-and-bounded-lie-sources|The scale and bounded-source construction]] fixes the representation, actual weighted character cost and Lie-valued marks. [[comb-face-transport-and-the-first-nonlinear-jet|FJ]] supplies the four-face graph and connector convention; the derivation below starts from those group words. [[fixed-group-compact-vacuum-and-oriented-source-return|The fixed-group compact return]] realizes the resulting source jets in the actual vacuum.

## Fix the group, metric and inherited cost

Let \(G\) be compact and connected, with simple Lie algebra \(\mathfrak g\) of dimension \(d\), and let \(Q\) be a positive \(\operatorname{Ad}G\)-invariant inner product. Fix a faithful unitary representation \(\rho\) and a positive Hermitian matrix \(A\) commuting with \(\rho(G)\). Keep the cost
\[
W_A(U)=\operatorname{Re}\operatorname{Tr}[A(I-\rho(U))],
\qquad
-\operatorname{Re}\operatorname{Tr}[A\,d\rho(X)d\rho(Y)]
=I_AQ(X,Y).
\]
The positive scalar \(I_A\) is determined by the declared data. In particular \(A\) need not be the identity or a scalar on a reducible representation.

For
\[
H=\kappa\mathsf C_{\rm raw,Q}+g\sum_pW_A(P_p),
\]
use the derived normalization
\[
g_{\rm eff}=2I_Ag,\qquad
h=(\kappa/g_{\rm eff})^{1/4},\qquad
E=\sqrt{\kappa g_{\rm eff}} .
\tag{AJ1}
\]
The kinetic coefficient in \(H/E\) is then \(h^2\), and the normalized magnetic Hessian in logarithmic coordinates is \(Q(X,X)/4\). These are the parameters of the same Hamiltonian, not a new choice of physical clock.

For a \(Q\)-orthonormal basis \(e_a\), set
\[
f_{abc}=Q(e_a,[e_b,e_c]),\qquad
T_G(X,Y,Z)=Q(X,[Y,Z])
=\sum_{a,b,c}f_{abc}X_aY_bZ_c .
\tag{AJ2}
\]
Invariance of \(Q\) makes \(f_{abc}\) fully alternating. All gradients and Laplacians below use this metric. The color tensor need not be a three-dimensional cross product.

## The raw edge and connector rows are group identities

Use the open \(2\times2\) square patch, with all twelve edges and Gauss law at all nine vertices. Orient edges positively and choose every vertical edge and the bottom horizontal row as a tree. If \(H_{i,j}\) are the four remaining horizontal chords and \(H_{i,0}=I\), the based face variables obey
\[
P_{i,j}=H_{i,j-1}H_{i,j}^{-1},\qquad
H_{i,j}=P_{i,j}^{-1}\cdots P_{i,1}^{-1}.
\]
Successive left translation and inversion of normalized Haar measure in each column give product face Haar for every \(G\). The complete gauge-invariant carrier is consequently
\[
L^2(G^4,dP)^{\operatorname{Ad}G}.
\]
A nontrivial center has not been quotiented out of the four group variables.

Let \(\mathcal L_{p,T}\), \(\mathcal R_{p,T}\) differentiate
\(P_p\mapsto e^{tT}P_p\) and \(P_p\mapsto P_pe^{tT}\), and put
\(\mathcal C_{p,T}=\mathcal L_{p,T}-\mathcal R_{p,T}\). Varying each original edge and restoring tree gauge gives
\[
\begin{aligned}
Z^{\rm hor}_{i,j,T}
&=-\mathcal R_{i,j,T}+\mathbf1_{j<2}\mathcal L_{i,j+1,T},\\
Z^{\rm bot}_{i,T}
&=\mathcal L_{i,1,T}+\sum_{a>i}\sum_{k=1}^2\mathcal C_{a,k,T},\\
Z^{\rm ver}_{c,j,T}
&=\mathbf1_{c\ge1}\mathcal L_{c,j,\operatorname{Ad}_{H_{c,j-1}}T}
+\mathbf1_{c<2}\left[-\mathcal R_{c+1,j,T}
+\sum_{k>j}\mathcal C_{c+1,k,T}\right].
\end{aligned}
\tag{AJ3}
\]
The index ranges are \(1\le i,j\le2\) and \(0\le c\le2\). These are four horizontal, two bottom and six vertical rows. The adjoint prefix is the original ordered chord word. Its lower-column variables are left fixed by that row, so the variable coefficient introduces no Haar divergence. Every row is divergence-free, and
\(\mathsf C_{\rm raw,Q}=-\sum_{e,a}Z_{e,e_a}^2\).

Now put \(P_p=\exp(hx_p)\). The BCH expansion gives
\[
\begin{aligned}
h\mathcal L_{p,T}
&=\left(T-\frac h2[x_p,T]\right)\cdot\nabla_p+O(h^2),\\
h\mathcal R_{p,T}
&=\left(T+\frac h2[x_p,T]\right)\cdot\nabla_p+O(h^2),\\
h\mathcal C_{p,T}
&=-h[x_p,T]\cdot\nabla_p,\\
\operatorname{Ad}_{H_{c,j-1}}T
&=T-h\left[\sum_{k<j}x_{c,k},T\right]+O(h^2).
\end{aligned}
\tag{AJ4}
\]
Dots in this display denote \(Q\)-contraction. The conjugation-row identity is exact. The last line follows by multiplying the actual factors
\(\exp(-h\,\operatorname{ad}_{x_{c,j-1}})\cdots
\exp(-h\,\operatorname{ad}_{x_{c,1}})\).
Thus the coefficient arrays in
\[
hZ_{e,T}=D_{0,e,T}+hD_{1,e,T}+O(h^2),\qquad
D_{0,e,T}=\sum_p s_{ep}Q(T,\nabla_p),\quad
D_{1,e,T}=\sum_{p,q}z_{epq}Q([x_q,T],\nabla_p)
\]
are the same rational face arrays as in FJ. Their equality follows from the words and BCH coefficients, before any group-specific matrix identity.

The local Haar Jacobian has no linear term: the linear coefficient of its logarithm is proportional to \(\operatorname{tr}(\operatorname{ad}_x)=0\). Its half-density therefore changes the kinetic operator first at order \(h^2\). Also
\(W_A(e^{hX})=W_A(e^{-hX})\), so its Taylor expansion has no odd powers. The leading magnetic term after (AJ1) is \(\sum_pQ(x_p,x_p)/4\), with no order-\(h\) contribution.

## The first operator uses only the Cartan three-form

Order the faces as \((1,1),(2,1),(1,2),(2,2)\), and set
\[
x=OY,\qquad
O=\frac12\begin{pmatrix}
1&1&1&1\\
1&-1&1&-1\\
1&1&-1&-1\\
1&-1&-1&1
\end{pmatrix}.
\]
This acts identically on each Lie-algebra component. The incidence metric becomes
\(\lambda=(2,4,4,6)\), with \(\omega_i=\sqrt{\lambda_i}\). The vacuum-subtracted oscillator and its vacuum are
\[
K_0=\sum_{i=0}^3\left(-\lambda_i\Delta_i+
\frac{Q(Y_i,Y_i)}4-\frac{d\omega_i}{2}\right),\qquad
\Omega_G=C\exp\!\left[-\sum_i\frac{Q(Y_i,Y_i)}{4\omega_i}\right].
\tag{AJ5}
\]

Transform the raw arrays by \(\bar s_e=O^{\mathsf T}s_e\) and
\(\bar z_e=O^{\mathsf T}z_eO\). The first odd jet of the actual density-transformed operator is
\[
\boxed{
V_{1,G}=\sum_{\ell=0}^3\sum_{j<k}
v_{\ell;jk}\,T_G(Y_\ell,\nabla_j,\nabla_k),\qquad
v_{\ell;jk}=2\sum_e
(\bar s_{ek}\bar z_{ej\ell}-\bar s_{ej}\bar z_{ek\ell}).}
\tag{AJ6}
\]
To obtain it, expand
\(-\sum_{e,a}(D_0D_1+D_1D_0)_{e,e_a}\).
The derivative of the linear bracket coefficient contains \([T,T]=0\).
The remaining contraction uses \(Q\)-invariance to put \(Y_\ell\) first in \(T_G\). No contraction of two structure tensors occurs. Hence neither dimension nor an adjoint-Casimir factor multiplies (AJ6).

For \(i<j<k\), define cyclicly
\[
D_i=T_G(Y_i,\nabla_j,\nabla_k),\qquad
U_i=Q([Y_j,Y_k],\nabla_i),\qquad
P_{ijk}=T_G(\nabla_i,\nabla_j,\nabla_k).
\]
The complete distinct-mode contribution is
\(V_{1,G}^{ijk}=\sum_{\rm cyc}v_iD_i\), and define
\(S_{1,G}^{ijk}=\sum_{\rm cyc}u_iU_i+p_{ijk}P_{ijk}\).
The rational word calculation is:

| \(ijk\) | \((v_i,v_j,v_k)\) | \((u_i,u_j,u_k)\) | \(p_{ijk}\) |
| --- | --- | --- | --- |
| \(012\) | \((0,-1,0)\) | \((-1/28,1/7,-3/28)\) | \(-4/7\) |
| \(013\) | \((3,-3,-1)\) | \((-1/4,1/4,0)\) | \(0\) |
| \(023\) | \((-1,1,-1)\) | \((0,-1/4,1/4)\) | \(0\) |
| \(123\) | \((-1,2,-2)\) | \((0,-1/4,1/4)\) | \(0\) |

Repeated modes also remain. For \(i<j\), put
\[
\widetilde D_i=T_G(Y_i,\nabla_i,\nabla_j),\quad
\widetilde D_j=T_G(Y_j,\nabla_i,\nabla_j),\qquad
\widetilde U_r=Q([Y_i,Y_j],\nabla_r)\quad(r=i,j).
\]
The coefficients of
\(V_{1,G}^{ij}=c_i\widetilde D_i+c_j\widetilde D_j\) and
\(S_{1,G}^{ij}=\alpha_i\widetilde U_i+\alpha_j\widetilde U_j\) are:

| \(ij\) | \((c_i,c_j)\) | \((\alpha_i,\alpha_j)\) |
| --- | --- | --- |
| \(01\) | \((-3,1)\) | \((3/8,-1/4)\) |
| \(02\) | \((1,0)\) | \((-1/8,0)\) |
| \(03\) | \((0,0)\) | \((0,0)\) |
| \(12\) | \((1,1)\) | \((-1/8,-1/8)\) |
| \(13\) | \((-1,1)\) | \((1/12,-1/8)\) |
| \(23\) | \((-2,1)\) | \((1/6,-1/8)\) |

The table includes all terms of (AJ6), even those whose vacuum action vanishes. The finite rational extraction already displayed in [[four-face-oriented-normal-form-and-the-universal-source-lift|UL2–4]] is valid here because the arrays in (AJ4) and the alternating contraction in (AJ6) have been derived for the general group.

## The normal form is an identity on the polynomial core

Direct coordinate commutators give
\[
[K_0,U_i]=-\frac12T_G(Y_i,Y_j,Y_k)
-2\lambda_jD_k-2\lambda_kD_j,\qquad
[K_0,P_{ijk}]=-\frac12(D_i+D_j+D_k).
\]
The distinct-sector equation therefore requires precisely
\[
u_i+u_j+u_k=0,\qquad
v_i=2\lambda_k u_j+2\lambda_j u_k+\frac12p_{ijk},
\quad\text{and cyclic permutations}.
\tag{AJ7}
\]
For repeated modes,
\[
[K_0,\widetilde U_i]=2\lambda_j\widetilde D_i,\qquad
[K_0,\widetilde U_j]=2\lambda_i\widetilde D_j .
\]
All these identities use only the constant alternating tensor \(f_{abc}\).
The tables solve them, yielding the complete operator
\[
\boxed{
S_{1,G}=\sum_{i<j<k}S_{1,G}^{ijk}+\sum_{i<j}S_{1,G}^{ij}
=\mathbf v_G(Y)\cdot\nabla-\frac47T_G(\nabla_0,\nabla_1,\nabla_2),
\qquad [K_0,S_{1,G}]=-V_{1,G}.}
\tag{AJ8}
\]

The domain is
\(\mathscr P_G=\mathbb C[\mathfrak g^4]\Omega_G\);
restriction to its simultaneous-\(\operatorname{Ad}G\)-invariant part gives the physical core. The identity holds before that restriction. The vector field is homogeneous quadratic and divergence-free by alternation of \(f_{abc}\); the constant third derivative is formally skew. Consequently
\[
\langle u,S_{1,G}v\rangle=-\langle S_{1,G}u,v\rangle
\qquad(u,v\in\mathscr P_G).
\]
The operator is real, \(\operatorname{Ad}G\)-invariant and odd under \(Y\mapsto-Y\).

Odd nonresonance is independent of the number of color components. If \(n_i\) denotes the total number of quanta in mode \(i\), the energies are
\(\sqrt2\,n_0+2(n_1+n_2)+\sqrt6\,n_3\).
Rational independence of \(1,\sqrt2,\sqrt6\) implies that equal energies have the same total-number parity. Thus an odd operator commuting with \(K_0\) vanishes on this core. This fixes the odd normal form without a resonant freedom. The finitely many ladder-frequency differences needed by its cubic polynomial are nonzero.

These statements neither compress the core to a finite matrix algebra nor prove an anti-selfadjoint closure. No exponential of \(S_{1,G}\) or exact global coordinate transformation is constructed.

## The complete quadratic source space still has ten dimensions

For a compact simple Lie algebra, every invariant real bilinear form is proportional to \(Q\). Here is a way to retain possible cross-mode forms rather than assuming symmetry. Write a bilinear form as \(Q(BX,Y)\). Invariance makes \(B\) commute with every \(\operatorname{ad}_X\). The eigenspaces of its self-adjoint part are ideals, so simplicity makes that part scalar. Its skew part \(J\) also commutes with the adjoint action and obeys
\(J[X,Y]=[JX,Y]=[X,JY]\). Invariance of \(Q\) and skew symmetry give
\[
Q(J[X,Y],Z)=-Q(J[X,Y],Z);
\]
therefore \(J\) vanishes on all brackets, and hence on the perfect algebra \(\mathfrak g\).

There are no invariant linear sources. Modulo constants, all real invariant quadratics on four copies are consequently
\[
F_B(Y)=\sum_{i,j=0}^3B_{ij}Q(Y_i,Y_j),\qquad B=B^{\mathsf T}.
\tag{AJ9}
\]
This is a ten-dimensional space for every group in the stated class.

Define the polynomial lift
\[
\mathcal D_G(F)=\Omega_G^{-1}[S_{1,G},M_F]\Omega_G.
\]
For (AJ9), its mixed Hessians are \(2B_{ij}\delta_{ab}\).
Their contractions with \(f_{abc}\) vanish, and
\(\nabla_i\Omega_G=-Y_i\Omega_G/(2\omega_i)\).
Thus the complete quadratic formula is
\[
\boxed{\mathcal D_G(F)=\sum_iQ(\mathbf d_i,\nabla_iF),}
\]
\[
\begin{aligned}
\mathbf d_0&=\mathbf v_{G,0}-\frac1{28}[Y_1,Y_2],\\
\mathbf d_1&=\mathbf v_{G,1}-\frac{\sqrt2}{28}[Y_2,Y_0],\\
\mathbf d_2&=\mathbf v_{G,2}-\frac{\sqrt2}{28}[Y_0,Y_1],\qquad
\mathbf d_3=\mathbf v_{G,3}.
\end{aligned}
\tag{AJ10}
\]
No color trace remains to introduce a dimension factor.

Let \(F_{ij}=Q(Y_i,Y_j)\) and \(T_{ijk}=T_G(Y_i,Y_j,Y_k)\).
The coefficients of \(\mathcal D_G(F_{ij})\) are:

| \(ij\) | \(T_{012}\) | \(T_{013}\) | \(T_{023}\) | \(T_{123}\) |
| --- | --- | --- | --- | --- |
| \(00\) | \(-1/7\) | \(-1/2\) | \(0\) | \(0\) |
| \(01\) | \(0\) | \(1/12\) | \(0\) | \(0\) |
| \(02\) | \(1/4\) | \(1/4\) | \(1/6\) | \(1/4\) |
| \(03\) | \(1/4\) | \(1/4\) | \(-1/4\) | \(-1/14\) |
| \(11\) | \(2/7-\sqrt2/14\) | \(1/2\) | \(0\) | \(0\) |
| \(12\) | \(-1/4\) | \(-1/4\) | \(1/4\) | \(1/12\) |
| \(13\) | \(-1/4\) | \(-1/4\) | \(-1/7+\sqrt2/28\) | \(-1/4\) |
| \(22\) | \(-(3+\sqrt2)/14\) | \(0\) | \(-1/2\) | \(-1/2\) |
| \(23\) | \(0\) | \(-(3+\sqrt2)/28\) | \(0\) | \(0\) |
| \(33\) | \(0\) | \(0\) | \(1/2\) | \(1/2\) |

For the symmetric-matrix convention in (AJ9), off-diagonal rows are multiplied by \(2B_{ij}\). The table follows by inserting the already derived vector fields into (AJ10), using cyclic invariance of \(T_G\). In particular
\[
\boxed{\mathcal D_G(Q(Y_0,Y_0))=-T_{012}/7-T_{013}/2.}
\tag{AJ11}
\]
The Cartan form is nonzero for a non-Abelian simple Lie algebra. Its four displayed mode channels are independent, since setting the unused mode to zero isolates each triple.

## The source lift keeps the vacuum and its limits of scope

The oscillator means and variances now depend on dimension:
\[
\mathbb E_{\Omega_G^2}F_{ii}=d\omega_i,\qquad
\operatorname{Var}_{\Omega_G^2}F_{ii}=2d\omega_i^2.
\tag{AJ12}
\]
Their change does not alter the unnormalized coefficients in (AJ10)–(AJ11). With \(u_G=S_{1,G}\Omega_G\), the formal first-order marked identity is
\[
(F+h\mathcal D_G(F))(\Omega_G+hu_G)
=(I+hS_{1,G})(F\Omega_G)+O(h^2).
\tag{AJ13}
\]
Formal skew symmetry preserves the first mean and Gram coefficients, so the same identity holds after appropriate centering and variance normalization.

The bounded Lie-valued mark in [[weighted-character-scale-and-bounded-lie-sources|the representation construction]] has the local jet \(q_\rho(e^{hX})=hX/2+O(h^3)\), with no quaternion assumption. Combining its fixed modes with the coefficients above gives bounded fixed quadratic-plus-cubic compact observables. [[fixed-group-compact-vacuum-and-oriented-source-return|The fixed-group analytic return]] controls their multiplication in the actual compact vacuum. [[lie-bracket-source-contact-and-the-positive-comparison-test|The contact calculation]] retains the additional term required for products; (AJ10) is not a derivation on that larger algebra.

Some groups admit symmetric invariant cubic tensors as well. Those are legitimate sources in the complete physical algebra and have not been removed. They do not enter this first kinetic jet: (AJ6) is linear in the alternating Lie-bracket tensor, while the actual weighted real character and Haar density contribute no first odd term. The four Cartan channels are the image of the particular quadratic lift, not a classification of all invariant cubic observables.

At the next operator order, representation-dependent quartic character tensors, the Haar density and contractions of structure constants do contribute. Neither the numerical \(SU(2)\) nonlinear gap correction nor its normalized cubic moments follow from (AJ8). The conclusion is an all-global-form first-order law for the fixed four-face geometry, with a fixed metric and inherited cost. It supplies no estimate uniform over groups, spatial size or a continuum Yang–Mills limit.
