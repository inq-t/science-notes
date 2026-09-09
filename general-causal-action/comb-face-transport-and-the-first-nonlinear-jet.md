# Comb Face Transport and the First Nonlinear Jet

A specified comb tree makes the planar face Haar law a product exactly, while retaining nonlocal electric rows through connector transport. Their logarithmic expansion has a cubic order-\(h\) operator. It kills bare scalar quadratic polynomials but does not kill the correlated oscillator vacuum or the soft scalar excitation: a \(2\times2\) patch supplies an explicit nonzero coefficient. The first nonlinear response must therefore retain the virtual cubic term, together with the Haar, kinetic, potential and source terms of order \(h^2\).

**Status: exact finite-patch differential representation and Taylor coefficients, with an evaluated nonzero \(L=2\) control.** The Hamiltonian, normalization and full Gauss carrier are those of [[planar-patch-confinement-and-the-spatial-soft-mode|PP]]. The transported-row principle is the one in [[gauge-cycle-innovation-filtration/loop-coordinates-and-the-induced-clock|LC]]. All jets below are for fixed \(L\); their use in a uniform spatial limit requires additional estimates.

## Fix the connector paths before expanding the source

Orient horizontal and vertical edges in their positive coordinate directions. Write a horizontal edge from \((i-1,j)\) to \((i,j)\) as \(H_{i,j}\). Choose as tree every vertical edge and the bottom horizontal row. A vertex connector runs along the bottom row and then vertically to that vertex. In tree gauge, all those links are \(I\), and the chords are \(H_{i,j}\), \(1\le i,j\le L\). Put \(H_{i,0}=I\).

Base each counterclockwise face at its bottom-left vertex and transport it to the root by the specified connector. Its tree-gauge word is
\[
X_{i,j}=H_{i,j-1}H_{i,j}^{-1},\qquad
H_{i,j}=X_{i,j}^{-1}X_{i,j-1}^{-1}\cdots X_{i,1}^{-1}.
\tag{FJ1}
\]
Successive Haar invariance along each column proves that (FJ1) is a global product-Haar-preserving change of coordinates. Consequently the complete physical carrier in this particular presentation is
\[
\mathcal H_{\rm phys}
=L^2\left(SU(2)^{L^2},\prod_{i,j}dX_{i,j}\right)^{\operatorname{Ad}SU(2)}.
\tag{FJ2}
\]
This proves a special choice with product face Haar; it does not assert that arbitrary based-face connectors preserve that product measure. No facewise Gauss quotient is taken.

Let \(\mathcal L_{p,T}\) and \(\mathcal R_{p,T}\) differentiate \(X_p\mapsto e^{tT}X_p\) and \(X_p\mapsto X_pe^{tT}\), respectively, with \(T_a=-i\sigma_a/2\) orthonormal. Set \(\mathcal C_{p,T}=\mathcal L_{p,T}-\mathcal R_{p,T}\). Each raw edge has one row \(Z_{e,T}\).

For a horizontal chord and a bottom tree edge these rows are
\[
\begin{aligned}
Z^{\rm hor}_{i,j,T}
&=-\mathcal R_{i,j,T}
 +{\bf1}_{j<L}\mathcal L_{i,j+1,T},\\
Z^{\rm bot}_{i,T}
&=\mathcal L_{i,1,T}
 +\sum_{a>i}\sum_{k=1}^L\mathcal C_{a,k,T}.
\end{aligned}
\tag{FJ3}
\]
For the vertical edge at column \(c\), from height \(j-1\) to \(j\), put
\(P_{c,j-1}=H_{c,j-1}\) when \(c\ge1\). Then
\[
\begin{aligned}
Z^{\rm ver}_{c,j,T}
={}&{\bf1}_{c\ge1}\,
\mathcal L_{c,j,\operatorname{Ad}_{P_{c,j-1}}T}\\
&+{\bf1}_{c<L}\left[
-\mathcal R_{c+1,j,T}
+\sum_{k>j}\mathcal C_{c+1,k,T}\right],
\qquad 0\le c\le L .
\end{aligned}
\tag{FJ4}
\]
Terms outside the grid are absent. The first line contains the actual parallel transport, not an independently adjustable coefficient.

To derive the tree rows, vary a tree edge on the left by \(e^{tT}\), then restore tree gauge. Every vertex in its descendant subtree receives the same compensating gauge element \(e^{tT}\). A chord with its source in that subtree acquires left multiplication, and one with its target there acquires inverse right multiplication. For a vertical edge, the affected chord columns are \(c\) and \(c+1\), at all heights \(k\ge j\). In column \(c\), their common inverse right motion cancels in every face above \(j\), while the face at \(j\) acquires \(\operatorname{Ad}_{H_{c,j-1}}T\) on its left. In column \(c+1\), the face at \(j\) acquires inverse right motion and all faces above it are conjugated. This gives (FJ4), including both the prefix transport and the conjugation tail.

Each row preserves product Haar. In (FJ4), the coefficient depends only on faces below \(j\) in column \(c\), which that row leaves fixed. Thus every row is divergence-free, and the exact kinetic form and operator on smooth invariant functions are
\[
\mathcal E_{\rm el}(f)=\kappa\int\sum_{e,a}|Z_{e,T_a}f|^2\,dX,
\qquad
\mathsf H_{\rm el}=-\kappa\sum_{e,a}Z_{e,T_a}^2 .
\tag{FJ5}
\]
The \(2L(L+1)\) rows count all raw edges once. Their closed form is the inherited Hamiltonian, not a reset collection of face Casimirs.

## Expand the rows and the measure together

Write \(X_p=\exp(-ih\,x_p\cdot\sigma/2)\), \(h=(\kappa/g)^{1/4}\), and identify the Lie bracket with the vector cross product. In this section \(x_p\) denotes the scaled Euclidean coordinate. Let \(\operatorname{ad}_x t=x\times t\). The single-face logarithmic rows satisfy
\[
\begin{aligned}
h\mathcal L_{p,t}
&=\left[t-\frac h2\operatorname{ad}_{x_p}t
+\frac{h^2}{12}\operatorname{ad}_{x_p}^2t\right]\cdot\partial_p
+O(h^4),\\
h\mathcal R_{p,t}
&=\left[t+\frac h2\operatorname{ad}_{x_p}t
+\frac{h^2}{12}\operatorname{ad}_{x_p}^2t\right]\cdot\partial_p
+O(h^4),\\
h\mathcal C_{p,t}
&=-h(\operatorname{ad}_{x_p}t)\cdot\partial_p .
\end{aligned}
\tag{FJ6}
\]
The remainders are coefficient Taylor remainders on fixed compact coordinate sets. For the ordered prefix in (FJ4), define
\[
s_{c,j}=\sum_{k<j}x_{c,k},\qquad
B_{c,j}=\frac12\sum_{k<j}\operatorname{ad}_{x_{c,k}}^2
+\sum_{j>a>b\ge1}\operatorname{ad}_{x_{c,a}}\operatorname{ad}_{x_{c,b}} .
\]
Its exact product order in (FJ1) gives
\[
\operatorname{Ad}_{P_{c,j-1}}
=I-h\operatorname{ad}_{s_{c,j}}+h^2B_{c,j}+O_L(h^3).
\tag{FJ7}
\]
In particular its transported left row is
\[
\begin{aligned}
h\mathcal L_{c,j,\operatorname{Ad}_{P}t}
=\bigg[t
&-h\left(\operatorname{ad}_{s_{c,j}}+
\frac12\operatorname{ad}_{x_{c,j}}\right)t\\
&+h^2\left(B_{c,j}
+\frac12\operatorname{ad}_{x_{c,j}}\operatorname{ad}_{s_{c,j}}
+\frac1{12}\operatorname{ad}_{x_{c,j}}^2\right)t
\bigg]\cdot\partial_{c,j}+O_L(h^3).
\end{aligned}
\tag{FJ8}
\]
Equations (FJ3), (FJ4), (FJ6) and (FJ8) specify every coefficient through order \(h^2\).

Write their sum for each edge as
\[
hZ_{e,t}=D_{0,e,t}+hD_{1,e,t}+h^2D_{2,e,t}+O_L(h^3).
\]
At order zero the row signs are the oriented face-edge incidence matrix. Hence
\[
-\sum_{e,a}D_{0,e,T_a}^2
=-\partial^{\mathsf T}(A_L\otimes I_3)\partial,\qquad
A_L=4I-\operatorname{Adj}_L .
\tag{FJ9}
\]
The conjugation tails vanish at order zero but not at order one.

Apart from a constant removed by normalization, the scaled product Haar density is
\[
\rho_h(x)=\prod_p
\left(\frac{\sin(h|x_p|/2)}{h|x_p|/2}\right)^2,\qquad
\log\rho_h=-\frac{h^2}{12}\sum_p|x_p|^2+O_L(h^4).
\tag{FJ10}
\]
Conjugate to Lebesgue measure by multiplication by \(\rho_h^{1/2}\). If
\(D_{0,e,t}=\sum_p s_{ep}\,t\cdot\partial_p\), the transformed row is
\[
\widetilde D_{e,t}
=D_{0,e,t}+hD_{1,e,t}+h^2E_{2,e,t}+O_L(h^3),\qquad
E_{2,e,t}=D_{2,e,t}
+\frac1{12}\sum_p s_{ep}\,t\cdot x_p .
\tag{FJ11}
\]
The last term is multiplication. It is the density-unitary correction, not an independently supplied potential.

In units of \(\sqrt{\kappa g}\), the resulting differential Taylor coefficients are
\[
\begin{aligned}
\widetilde{\mathsf H}_h&=\mathcal O_L+h\mathcal H_1+h^2\mathcal H_2+O_L(h^3),\\
\mathcal H_1&=-\sum_{e,a}(D_0D_1+D_1D_0)_{e,a},\\
\mathcal H_2&=-\sum_{e,a}(D_1^2+D_0E_2+E_2D_0)_{e,a}
-\frac1{192}\sum_p|x_p|^4 .
\end{aligned}
\tag{FJ12}
\]
Here \(\mathcal O_L\) is PP6. The last term follows from
\(2-\chi_{1/2}(e^{-ihx\cdot\sigma/2})
=h^2|x|^2/4-h^4|x|^4/192+O(h^6)\).
These are exact local Taylor jets. An actual spectral or normalized-source expansion must also justify localization, remainders and vacuum perturbation; a coefficient identity alone does not supply an estimate uniform in \(L\).

## The cubic row term is not killed by scalarity

For an explicit evaluation it is enough to write
\[
D_{0,e,t}=\sum_p s_{ep}\,t\cdot\partial_p,\qquad
D_{1,e,t}=\sum_p(z_{ep}(x)\times t)\cdot\partial_p .
\tag{FJ13}
\]
Every \(z_{ep}\) is linear in the face vectors. For a horizontal row its two nonzero values are \(-x_{i,j}/2\) and \(-x_{i,j+1}/2\), with signs \(s=-1,+1\). For a bottom row, \(s_{i,1}=1\), \(z_{i,1}=-x_{i,1}/2\), and \(z_{a,k}=-x_{a,k}\) for every \(a>i\). For a vertical row, its left face has
\(s=1,\ z=-s_{c,j}-x_{c,j}/2\); its right face has
\(s=-1,\ z=-x_{c+1,j}/2\); every face above that right face has
\(s=0,\ z=-x_{c+1,k}\).

Let
\[
S=\frac12A_L^{-1/2},\qquad
\Omega(x)=C\exp\left(-\frac12\sum_{p,q}S_{pq}x_p\cdot x_q\right),
\quad
g_p=\sum_qS_{pq}x_q,\quad
G_e=\sum_p s_{ep}g_p,\quad
F_e=\sum_p g_p\times z_{ep}.
\]
Then \(D_0\Omega=-(t\cdot G_e)\Omega\) and
\(D_1\Omega=-(t\cdot F_e)\Omega\). Differentiating a row's linear coefficient along its order-zero direction only produces \(t\times t=0\); the remaining Hessian trace also vanishes by antisymmetry. Therefore
\[
\boxed{\frac{\mathcal H_1\Omega}{\Omega}
=-2\sum_eG_e\cdot F_e .}
\tag{FJ14}
\]
This is a cubic simultaneous-color scalar, formed from alternating products of three face vectors. Scalarity under \(SO(3)\) does not exclude it. Global inversion \(x\mapsto-x\) makes \(\mathcal H_1\) odd, so its expectation in an even oscillator state is zero. That parity statement does not imply (FJ14) vanishes.

For \(L=2\), order the faces as
\(a=(1,1), b=(2,1), c=(1,2), d=(2,2)\).
Write the diagonal, nearest-neighbor and opposite-corner entries of \(S\) as \(d_0,u_0,v_0\). Put
\[
\alpha=\frac1{2\sqrt2},\qquad \beta=\frac14,\qquad
\gamma=\frac1{2\sqrt6}.
\]
The sine-mode diagonalization gives
\[
d_0=\frac{\alpha+2\beta+\gamma}{4},\qquad
u_0=\frac{\alpha-\gamma}{4},\qquad
v_0=\frac{\alpha-2\beta+\gamma}{4}.
\tag{FJ15}
\]
Substituting the finite row list (FJ13) into (FJ14), the coefficient of
\(x_a\cdot(x_c\times x_d)\) is
\[
\begin{aligned}
\mathfrak c
&=2d_0^2+6d_0u_0-4u_0^2-6u_0v_0+2v_0^2\\
&=\alpha\gamma+\beta^2+\frac{3\beta}{2}(\alpha-\gamma)>0 .
\end{aligned}
\tag{FJ16}
\]
For example, the six contributing rows are the horizontal rows \((1,1),(2,1)\), the bottom row \(1\), and the vertical rows \((0,1),(1,1),(1,2)\). Their respective contributions are
\[
\begin{gathered}
-u_0v_0+d_0v_0-u_0^2+d_0u_0,\qquad -u_0^2+v_0^2,\\
-2u_0v_0+2d_0u_0,\qquad -2u_0v_0+2d_0u_0,\\
-2u_0v_0+v_0^2-u_0^2+2d_0u_0,\qquad
-u_0^2+u_0v_0-d_0u_0+2d_0^2-d_0v_0 .
\end{gathered}
\]
All other rows give zero for this coefficient. The four possible distinct-face triple polynomials are linearly independent: set the unused face vector to zero to isolate any one. Thus
\(\mathcal H_1\Omega\ne0\), without a fitted coefficient or numerical approximation.

## The soft source also requires virtual transitions

Let \(f\) be the normalized scalar polynomial in PP9, with
\(Y=\sum_pv_{11}(p)x_p\) and \(\lambda=\lambda_{\min}\).
More generally, \(\mathcal H_1 f=0\) for every scalar quadratic polynomial
\(f=\sum_{p,q}b_{pq}x_p\cdot x_q+\text{constant}\).
Its constant Hessian contracts \(t\) with \(z\times t\), and the coefficient derivative vanishes as above.

This does not apply to the physical vector \(f\Omega\). Define
\[
r_p=\partial_pf,\qquad B_e=\sum_ps_{ep}r_p,\qquad
C_e=\sum_pr_p\times z_{ep}.
\]
The exact product rule gives
\[
\boxed{\mathcal H_1(f\Omega)
=\left[f\,\frac{\mathcal H_1\Omega}{\Omega}
+2\sum_e(B_e\cdot F_e+C_e\cdot G_e)\right]\Omega .}
\tag{FJ17}
\]
The second term is cubic. At \(L=2\), the first term has the nonzero quintic part \(f_{\rm quadratic}(\mathcal H_1\Omega/\Omega)\), so the result cannot vanish. In oscillator modes, the cubic vacuum vector has exactly three quanta: repeated mode indices in an alternating triple cancel. Equation (FJ17) has only three- and five-quantum scalar components. These finite spaces suffice for its virtual resolvent matrix elements at fixed \(L\); discarding them would change the order-\(h^2\) response.

In particular, with \(R=(\mathcal O_L-\omega_0)^{-1}\) on the vacuum complement, the vacuum second-order coefficient includes
\[
\langle\Omega,\mathcal H_2\Omega\rangle
-\langle\mathcal H_1\Omega,R\mathcal H_1\Omega\rangle .
\tag{FJ18}
\]
The second term is strictly negative at \(L=2\). Its separation from the first term depends on the chosen chart; their properly transported sum is the spectral quantity.

For the actual compact source PP12, use these same comb-based face words. If
\(X_p=q_{0,p}I-i\mathbf q_p\cdot\sigma\), then
\[
\begin{aligned}
\mathcal B_L&=\left|\sum_pv_{11}(p)\mathbf q_p\right|^2,\\
\frac{\mathcal B_L}{h^2}
&=\frac14|Y|^2
-\frac{h^2}{48}\,
Y\cdot\sum_pv_{11}(p)|x_p|^2x_p+O_L(h^4).
\end{aligned}
\tag{FJ19}
\]
There is no order-\(h\) source coefficient. The actual source still must be centered and normalized in the perturbed vacuum; its zeroth-order scalar form does not remove the odd vacuum and excited-state correctors in (FJ17).

The prefix in a vertical row contains up to \(L-1\) face factors, and a bottom row can conjugate order \(L^2\) faces. The explicit finite sums above determine that dependence instead of assuming a size-independent coefficient. The inverse oscillator denominators also depend on the spatial frequencies, whose smallest physical value is \(c_L\sim2\sqrt2\pi/(L+1)\). [[compact-source-normalization-and-the-nonlinear-return|CS11–14]] gives a conservative polynomial envelope for the first coefficients from this word counting. It supplies no uniform bound on the full nonlinear remainder.

A change of rooted presentation transports the full operator, measure and fixed physical source. Its local coordinate unitary generally has an order-\(h\) term, which changes \(\mathcal H_1\) by a commutator with \(\mathcal O_L\). Therefore \(\mathcal H_1\Omega\) alone need not obey a lattice symmetry acting only by linear permutation of oscillator coordinates. Moreover, changing the actual connector paths in (FJ19) can change that physical source, even when its harmonic quadratic jet agrees. Neither discarding the connector rows nor replacing the probe by a different connector comparison is a harmless simplification of the specified nonlinear experiment.
