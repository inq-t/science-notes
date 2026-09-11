# A Universal Oriented Lift from the Four-Face Normal Form

The actual first odd kinetic jet on the four-face patch admits one explicit odd polynomial normal form. Its coefficients are fixed by all twelve raw edges, including angular terms invisible to the original soft probe. The resulting vacuum-evaluated commutator lifts every quadratic comparison into the four oriented cubic channels and recovers the previously constructed gap-following probe. One constant third-derivative term remains; it is essential when products of sources are considered.

**Status: exact operator identity on the polynomial-Gaussian core and complete first-order quadratic lift.** [[comb-face-transport-and-the-first-nonlinear-jet|FJ]] supplies the raw rows, and [[four-face-cubic-response-and-source-leakage|FC]] fixes the normal modes and correctors. No anti-selfadjoint closure or unitary exponential of the polynomial normal form is asserted.

[[all-group-oriented-kinetic-jet-and-source-lift|AJ1–13]] derives the same complete first jet and quadratic lift from the actual group words for every compact connected simple group. Its color tensor is \(Q(X,[Y,Z])\), and [[weighted-character-scale-and-bounded-lie-sources|the weighted character Hessian]] fixes the comparison scale. This generalization does not transfer the higher-order \(SU(2)\) spectral coefficient.

## Keep the full oscillator core and the specified modes

Use the fixed twelve-edge \(2\times2\) patch with complete Gauss law and the comb connectors of FJ. In the Hadamard normal modes of FC1, write
\[
\lambda=(2,4,4,6),\qquad
\omega_i=\sqrt{\lambda_i},\qquad
K_0=\sum_{i=0}^3\left(-\lambda_i\Delta_i+\frac{|Y_i|^2}{4}
-\frac{3\omega_i}{2}\right).
\]
Its normalized vacuum has
\[
\Omega(Y)=C\exp\!\left[-\sum_i\frac{|Y_i|^2}{4\omega_i}\right],
\qquad \partial_{i,a}\Omega=-\sigma_iY_{i,a}\Omega,\quad
\sigma_i=(2\omega_i)^{-1}.
\tag{UL1}
\]
Work on the algebraic core
\(\mathscr P=\mathbb C[Y]\Omega\), or its simultaneous-\(SO(3)\)-invariant subcore for physical states. Multiplication and all differential operators below preserve \(\mathscr P\). A computation on finitely many polynomial degrees uses a sufficiently large degree buffer; it does not replace this algebra by a compressed spectral subspace.

FJ12 gives the actual scaled operator
\[
\widehat H_h=\mathcal O+hV_1+O(h^2),\qquad
V_1=-\sum_{e,a}(D_0D_1+D_1D_0)_{e,a},
\]
where \(h=(\kappa/g)^{1/4}\). Its first density and magnetic corrections vanish. With the mode-transformed raw arrays
\[
D_{0,e,t}=\sum_\nu \bar s_{e\nu}\,t\cdot\partial_\nu,\qquad
D_{1,e,t}=\sum_{\mu,\ell}\bar z_{e\mu\ell}
(Y_\ell\times t)\cdot\partial_\mu ,
\]
the complete differential operator is
\[
\boxed{
V_1=\sum_{\ell=0}^3\sum_{j<k}
v_{\ell;jk}\,Y_\ell\cdot(\partial_j\times\partial_k),\qquad
v_{\ell;jk}=2\sum_e
\left(\bar s_{ek}\bar z_{ej\ell}-\bar s_{ej}\bar z_{ek\ell}\right).}
\tag{UL2}
\]
The sum uses every raw edge once. Differentiating the linear row coefficient in \(D_0D_1\) gives a contraction containing \(t\times t\), hence zero. There is no omitted lower-order term in (UL2).

## Distinct and repeated mode labels both contribute

For \(i<j<k\), use cyclic notation
\[
\begin{aligned}
T_{ijk}&=Y_i\cdot(Y_j\times Y_k),\\
D_i&=Y_i\cdot(\partial_j\times\partial_k),&
U_i&=(Y_j\times Y_k)\cdot\partial_i,\\
P_{ijk}&=\partial_i\cdot(\partial_j\times\partial_k).
\end{aligned}
\]
The definitions of \(D_j,D_k,U_j,U_k\) follow by cyclic permutation. The raw distinct-sector coefficients and their normal-form solution are:

| \(ijk\) | \((v_i,v_j,v_k)\) in \(V_1\) | \((u_i,u_j,u_k)\) in \(S_1\) | \(p_{ijk}\) in \(S_1\) |
| --- | --- | --- | --- |
| \(012\) | \((0,-1,0)\) | \((-1/28,1/7,-3/28)\) | \(-4/7\) |
| \(013\) | \((3,-3,-1)\) | \((-1/4,1/4,0)\) | \(0\) |
| \(023\) | \((-1,1,-1)\) | \((0,-1/4,1/4)\) | \(0\) |
| \(123\) | \((-1,2,-2)\) | \((0,-1/4,1/4)\) | \(0\) |

In this table,
\[
V_1^{ijk}=v_iD_i+v_jD_j+v_kD_k,\qquad
S_1^{ijk}=u_iU_i+u_jU_j+u_kU_k+p_{ijk}P_{ijk}.
\tag{UL3}
\]

Repeated mode labels are not zero merely because a multiplication triple would vanish. For \(i<j\), define
\[
\widetilde D_i=Y_i\cdot(\partial_i\times\partial_j),\quad
\widetilde D_j=Y_j\cdot(\partial_i\times\partial_j),
\]
\[
\widetilde U_i=(Y_i\times Y_j)\cdot\partial_i,\qquad
\widetilde U_j=(Y_i\times Y_j)\cdot\partial_j .
\]
Their complete coefficients are:

| \(ij\) | \((c_i,c_j)\) in \(V_1\) | \((\alpha_i,\alpha_j)\) in \(S_1\) |
| --- | --- | --- |
| \(01\) | \((-3,1)\) | \((3/8,-1/4)\) |
| \(02\) | \((1,0)\) | \((-1/8,0)\) |
| \(03\) | \((0,0)\) | \((0,0)\) |
| \(12\) | \((1,1)\) | \((-1/8,-1/8)\) |
| \(13\) | \((-1,1)\) | \((1/12,-1/8)\) |
| \(23\) | \((-2,1)\) | \((1/6,-1/8)\) |

Thus
\[
V_1^{ij}=c_i\widetilde D_i+c_j\widetilde D_j,\qquad
S_1^{ij}=\alpha_i\widetilde U_i+\alpha_j\widetilde U_j,\qquad
\alpha_i=-\frac{c_i}{2\lambda_j},\quad
\alpha_j=-\frac{c_j}{2\lambda_i}.
\tag{UL4}
\]
No repeated-mode term is discarded by invoking Gauss law. These terms annihilate the oscillator vacuum and the original soft radial source, but they can act on other quadratic comparisons.

## The commutator is an exact polynomial identity

Direct differentiation gives
\[
[K_0,U_i]=-\frac12T_{ijk}-2\lambda_jD_k-2\lambda_kD_j,\qquad
[K_0,P_{ijk}]=-\frac12(D_i+D_j+D_k).
\]
Consequently the distinct-sector equation
\([K_0,S_1^{ijk}]=-V_1^{ijk}\) is exactly the rational system
\[
u_i+u_j+u_k=0,\qquad
v_i=2\lambda_k u_j+2\lambda_j u_k+\frac{p_{ijk}}2,
\quad\text{and cyclic permutations}.
\tag{UL5}
\]
Every row of (UL3) solves it. For repeated modes,
\[
[K_0,\widetilde U_i]=2\lambda_j\widetilde D_i,\qquad
[K_0,\widetilde U_j]=2\lambda_i\widetilde D_j,
\]
so (UL4) supplies the remaining terms. The full result is
\[
\boxed{
S_1=\sum_{i<j<k}S_1^{ijk}+\sum_{i<j}S_1^{ij}
=\mathbf v(Y)\cdot\nabla-\frac47P_{012},\qquad
[K_0,S_1]=-V_1.}
\tag{UL6}
\]
Here \(\mathbf v\) is the homogeneous quadratic vector field specified completely by the tables.

Every vector field in \(S_1\) has zero Euclidean divergence; \(P_{012}\) is a constant product of three derivatives. Integration by parts on \(\mathscr P\) therefore gives
\[
\langle u,S_1v\rangle=-\langle S_1u,v\rangle .
\]
Thus \(S_1\) is formally skew-adjoint on this common core. It is real, invariant under simultaneous proper color rotations, and odd under \(Y\mapsto-Y\). The commutator identity holds before restricting to Gauss-invariant states.

The absence of an odd resonant ambiguity can also be checked without a matrix truncation. Oscillator energies are
\[
\sqrt2\,n_0+2(n_1+n_2)+\sqrt6\,n_3.
\]
Rational independence of \(1,\sqrt2,\sqrt6\) implies that equal energies have the same \(n_0,n_3,n_1+n_2\), and hence the same total-number parity. An odd operator has no matrix elements within such an equal-energy block. Requiring an odd solution therefore removes any commuting addition on the polynomial core. Equivalently, the finitely many nonzero ladder-frequency components of \(V_1\) may be divided by their energy differences. The explicit differential solution (UL3)–(UL6) needs no infinite small-denominator estimate.

Formal skew-adjointness is not a proof of an anti-selfadjoint closure. No global operator \(e^{hS_1}\), its domain, or an exact compact unitary is used here.

## The vacuum-evaluated lift is universal on quadratics

For any polynomial multiplication source \(F\), define
\[
\boxed{\mathcal D(F)=\Omega^{-1}[S_1,M_F]\Omega .}
\tag{UL7}
\]
The result is a polynomial. Constants map to zero. This is a linear source lift obtained from the already specified raw kinetic jet and harmonic vacuum.

For an invariant quadratic \(F\), its mixed Hessians are scalar color tensors:
\(\partial_{i,a}\partial_{j,b}F\) is proportional to \(\delta_{ab}\).
They vanish when contracted with the alternating tensor in \(P_{012}\). The remaining formula is
\[
\boxed{
\mathcal D(F)=\sum_{i=0}^3\mathbf d_i(Y)\cdot\nabla_iF,}
\]
\[
\begin{aligned}
\mathbf d_0&=\mathbf v_0-\frac1{28}Y_1\times Y_2,\\
\mathbf d_1&=\mathbf v_1-\frac{\sqrt2}{28}Y_2\times Y_0,\\
\mathbf d_2&=\mathbf v_2-\frac{\sqrt2}{28}Y_0\times Y_1,\qquad
\mathbf d_3=\mathbf v_3 .
\end{aligned}
\tag{UL8}
\]
For example, the coefficient added to \(\mathbf v_i\) is
\(p_{012}\sigma_j\sigma_k\), because two of the derivatives act on \(\Omega\).
Equation (UL8) is asserted on invariant quadratics. It is not a replacement of the full map (UL7) on their products by a vector-field derivation.

Let \(F_{ij}=Y_i\cdot Y_j\), \(i\le j\). The coefficients of
\(\mathcal D(F_{ij})\), in the ordered basis
\((T_{012},T_{013},T_{023},T_{123})\), are:

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

This evaluates the complete ten-dimensional linear map, with the same mode orientations as FC. For a symmetric matrix convention \(F=\sum_{i,j}B_{ij}Y_i\cdot Y_j\), the off-diagonal rows receive coefficient \(2B_{ij}\).

## The old oriented probe is recovered, with the vacuum kept

Let \(u\) be the first vacuum correction and \(\eta_1\) the first correction to the normalized soft excitation
\[
\phi=\frac{|Y_0|^2/\sqrt2-3}{\sqrt6}\Omega,\qquad
K_0\phi=2\sqrt2\,\phi .
\]
Equation (UL6), oddness and the corresponding nonresonant inverse imply
\[
S_1\Omega=u,\qquad S_1\phi=\eta_1 .
\]
Since the unnormalized soft-source variance is \(12\),
\[
[S_1,|Y_0|^2]\Omega
=\sqrt{12}\left(\eta_1-\frac{\phi}{\Omega}u\right)
=-\sqrt{12}\,\ell .
\]
Thus
\[
\boxed{\mathcal D(|Y_0|^2)
=-\frac17T_{012}-\frac12T_{013},}
\tag{UL9}
\]
exactly the linear jet of [[four-face-oriented-source-and-the-gap-following-probe|OS's fixed probe]]. The common normal form produces this result without defining \(S_1\) from that source or its first-excitation projector.

More generally, at the level of first-order vectors,
\[
(F+h\mathcal D(F))(\Omega+hS_1\Omega)
=F\Omega+hS_1(F\Omega)+O(h^2).
\tag{UL10}
\]
Skew symmetry makes the first correction to the actual mean vanish. Subtracting the common mean and normalizing its variance gives the same identity for the centered source vector; its first variance correction also vanishes. This statement does not make a generic quadratic into a single eigenmode. It transports its whole leading oscillator source vector.

## All quadratic lifts have fixed bounded compact representatives

Write a quadratic as \(F=\sum_{i\le j}b_{ij}F_{ij}\), and let
\(\mathcal D(F)=\sum_I d_I(F)T_I\) be the linear combination given above.
Using the fixed common-root quaternion modes \(\mathbf Q_i\) of OS1, set
\[
\boxed{
\mathcal Q_F^\uparrow
=\sum_{i\le j}b_{ij}\mathbf Q_i\cdot\mathbf Q_j
+2\sum_{I=(i,j,k)}d_I(F)\,
\mathbf Q_i\cdot(\mathbf Q_j\times\mathbf Q_k).}
\tag{UL11}
\]
This is a real bounded gauge-invariant observable whenever \(F\) is real. All coefficients and paths are fixed independently of \(h\). Since
\(\mathbf Q_i=hY_i/2+O(h^3)\),
\[
4\mathcal Q_F^\uparrow/h^2
=F+h\mathcal D(F)+O(h^2)
\]
in the same local source expansion. For \(F=F_{00}\), (UL11) is precisely
\(|\mathbf Q_0|^2-\frac27\mathbf Q_0\cdot(\mathbf Q_1\times\mathbf Q_2)
-\mathbf Q_0\cdot(\mathbf Q_1\times\mathbf Q_3)\).

[[oriented-source-products-and-the-compact-contact-return|The compact contact return]] applies CS's higher-accuracy vacuum construction to these fixed bounded marks. It realizes (UL10) in the actual compact theory, retaining source centering and the appropriate scaling. Products require their own contact terms: the formula for quadratics cannot be silently extended by Leibniz. [[four-face-source-products-and-the-oriented-contact|The product calculation]] evaluates that distinction from the third-derivative term in (UL6).

The [[general-causal-action/receipts/four_face_normal_form_receipt.py|exact normal-form receipt]] reconstructs the twelve raw rows, solves every rational coefficient system, and independently checks the commutator against the original Hermite row operator on the vacuum, colored linear states and all ten quadratics. It also verifies the complete lift table and both known eigenvector correctors. The general operator identity itself follows from (UL2)–(UL6), not from those finite checks. This is a fixed-patch first-order source construction; it asserts no spatially uniform normal form or continuum Yang–Mills gap.
