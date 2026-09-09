# Four-Face Diagonal Sources and the Relational Schur Defect

The four separate face quadratics have a strictly larger harmonic innovation quotient than the complete ten-dimensional quadratic comparison space. Their exact response splits into three symmetry sectors. At any threshold between the two minima, retaining the innovation form and eliminating the old source coefficients gives an explicit negative Schur direction supplied by mixed-face bilinears. The experiment changes through its source space; the vacuum, Hamiltonian and duration stay fixed.

**Status: exact harmonic source-extension calculation on the fixed four-face patch.** [[four-face-gap-shift-and-the-complete-source-response|FF2]] fixes the normal modes, [[additive-neutral-sources-and-the-pairing-range-test|AR1]] fixes all mixed Gaussian responses, and [[compact-quadratic-carrier-and-the-pairing-range-return|QK]] owns their actual compact return. No nonlinear coefficient is inferred from the harmonic calculation here.

## Keep the innovation and surplus as two forms

Order the four faces as \(a,b,c,d\) in FF. Let \(H\) have columns
\[
v_0=\tfrac12(1,1,1,1),\quad
v_1=\tfrac12(1,-1,1,-1),\quad
v_2=\tfrac12(1,1,-1,-1),\quad
v_3=\tfrac12(1,-1,-1,1).
\]
Write
\[
C=H\operatorname{diag}(\omega)H^{\mathsf T},\qquad
\omega=(\sqrt2,2,2,\sqrt6),\qquad
D_s=Ce^{-sC}.
\tag{DQ1}
\]
The three color vectors \(X_\alpha\) are independent centered Gaussians with covariance \(C\). Every neutral quadratic in the common based color frame is
\[
F_B=\sum_{\alpha=1}^3X_\alpha^{\mathsf T}BX_\alpha-3\operatorname{Tr}(BC),
\qquad B=B^{\mathsf T}\in\operatorname{Sym}_4(\mathbb R).
\]
For the full harmonic Markov transfer \(P_s\), Wick contraction gives
\[
\mathcal M_s(B,N)=\langle F_B,P_sF_N\rangle
=6\operatorname{Tr}(BD_sND_s).
\]
At a fixed \(t>0\), retain the two forms
\[
G_t=\mathcal M_0-\mathcal M_{2t},\qquad
N_t=\mathcal M_0-2\mathcal M_{2t}+\mathcal M_{4t},\qquad
q_t(B)=\frac{N_t(B,B)}{G_t(B,B)}.
\tag{DQ2}
\]
Here \(G_t(B,B)>0\) for every nonzero symmetric \(B\). These are the original full-predictor innovation and OI surplus, without a regional conditional reset.

Put \(r_\nu=1-e^{-2t\nu}\) and \(M=H^{\mathsf T}BH\). The ten independent matrix entries give
\[
\begin{aligned}
G_t(B,B)
&=\sum_i6\omega_i^2r_{2\omega_i}M_{ii}^2
 +\sum_{i<j}12\omega_i\omega_jr_{\omega_i+\omega_j}M_{ij}^2,\\
N_t(B,B)
&=\sum_i6\omega_i^2r_{2\omega_i}^{\,2}M_{ii}^2
 +\sum_{i<j}12\omega_i\omega_jr_{\omega_i+\omega_j}^{\,2}M_{ij}^2.
\end{aligned}
\tag{DQ3}
\]
Thus the generalized spectrum on the complete quadratic space is
\[
\begin{array}{c|rrrrrr}
\nu&2\sqrt2&\sqrt2+2&\sqrt2+\sqrt6&4&2+\sqrt6&2\sqrt6\\ \hline
\text{multiplicity of }r_\nu&1&2&1&3&2&1 .
\end{array}
\]
Its minimum is simple:
\[
q_{\mathrm{full}}(t)=r_{2\sqrt2}=1-e^{-4\sqrt2t},
\qquad B_*=v_0v_0^{\mathsf T}.
\tag{DQ4}
\]

## The four old sources have three exact response sectors

The old space is \(\mathcal V_{\mathrm{old}}=\{\operatorname{diag}(d):d\in\mathbb R^4\}\). Its covariance matrix in \(d\) is \(6(D_s\circ D_s)\). Identify face and mode indices with \(\mathbb Z_2^2\), using the characters \(2v_\alpha\). The Hadamard convolution identity diagonalizes this matrix in the same four character vectors:
\[
h_\alpha(s)=\tfrac14\sum_j
\omega_j\omega_{j\oplus\alpha}
e^{-s(\omega_j+\omega_{j\oplus\alpha})}.
\tag{DQ5}
\]
Explicitly,
\[
\begin{aligned}
h_0(s)&=\tfrac12e^{-2\sqrt2s}+2e^{-4s}+\tfrac32e^{-2\sqrt6s},\\
h_1(s)=h_2(s)&=\sqrt2e^{-(\sqrt2+2)s}+\sqrt6e^{-(2+\sqrt6)s},\\
h_3(s)&=\sqrt3e^{-(\sqrt2+\sqrt6)s}+2e^{-4s}.
\end{aligned}
\]
For the Euclidean-unit coefficient vector \(d=v_\alpha\), the exact innovation and surplus eigenvalues are
\[
g_\alpha=6[h_\alpha(0)-h_\alpha(2t)],\qquad
n_\alpha=6[h_\alpha(0)-2h_\alpha(2t)+h_\alpha(4t)].
\tag{DQ6}
\]
The three generalized eigenvalues, with the edge sector repeated twice, are
\[
\begin{aligned}
q_I&=\frac{2r_{2\sqrt2}^2+8r_4^2+6r_{2\sqrt6}^2}
{2r_{2\sqrt2}+8r_4+6r_{2\sqrt6}},\\
q_{\mathrm{edge}}&=
\frac{\sqrt2r_{\sqrt2+2}^2+\sqrt6r_{2+\sqrt6}^2}
{\sqrt2r_{\sqrt2+2}+\sqrt6r_{2+\sqrt6}},\\
q_{\mathrm{checker}}&=
\frac{\sqrt3r_{\sqrt2+\sqrt6}^2+2r_4^2}
{\sqrt3r_{\sqrt2+\sqrt6}+2r_4}.
\end{aligned}
\tag{DQ7}
\]
Each is a positive innovation-weighted average of its displayed \(r_\nu\). The identity sector contains higher energies with nonzero weights, while the other two sectors contain only energies above \(2\sqrt2\). Consequently
\[
\boxed{q_{\mathrm{old}}(t):=\min\{q_I,q_{\mathrm{edge}},q_{\mathrm{checker}}\}
>q_{\mathrm{full}}(t),\qquad t>0.}
\tag{DQ8}
\]
This exact minimum does not require ordering the three functions at every duration. The diagonal source space need not be invariant under the physical transfer; only its two restricted response forms were diagonalized.

## An explicit old/new Schur pencil

Choose and fix
\[
q_{\mathrm{full}}(t)<\gamma<q_{\mathrm{old}}(t),\qquad
Q_\gamma=N_t-\gamma G_t.
\tag{DQ9}
\]
For example, the midpoint of these two minima is admissible. Then the old block \(Q_{\mathrm{oo}}\) is positive definite. With the new space consisting of zero-diagonal face matrices, the exact extension criterion is the Schur form
\[
\mathcal S_\gamma=Q_{\mathrm{nn}}
-Q_{\mathrm{no}}Q_{\mathrm{oo}}^{-1}Q_{\mathrm{on}}.
\]
The inverse here is the finite positive old block of the retained pencil, not a spectral inverse chosen to construct a physical repair.

An economical complete specification has four independent sectors:
\[
\begin{array}{c|c|c}
\alpha&\text{mode-matrix coordinates}&(\dim\mathrm{old},\dim\mathrm{new})\\ \hline
0&(M_{00},M_{11},M_{22},M_{33})&(1,3)\\
1&(M_{01},M_{23})&(1,1)\\
2&(M_{02},M_{13})&(1,1)\\
3&(M_{03},M_{12})&(1,1).
\end{array}
\tag{DQ10}
\]
In each row the old character source spans the all-ones coordinate line \(\mathbb R\mathbf1\). A face matrix has zero diagonal precisely when its coordinates in every row sum to zero. This follows by inverse Hadamard transformation of \(B_{pp}\). Let \(V_\alpha\) be any matrix whose columns span that sum-zero subspace.

Assign to each coordinate \(ij\) its weight \(w_{ii}=6\omega_i^2\) or \(w_{ij}=12\omega_i\omega_j\) for \(i<j\). The diagonal sector matrices are
\[
\mathsf G_\alpha=\operatorname{diag}(w_{ij}r_{\omega_i+\omega_j}),\qquad
\mathsf N_\alpha=\operatorname{diag}(w_{ij}r_{\omega_i+\omega_j}^2),\qquad
\mathsf D_\alpha=\mathsf N_\alpha-\gamma\mathsf G_\alpha .
\]
Therefore the complete six-dimensional Schur pencil is the direct sum of
\[
\boxed{
V_\alpha^{\mathsf T}\mathsf D_\alpha V_\alpha
-\frac{(V_\alpha^{\mathsf T}\mathsf D_\alpha\mathbf1)
(\mathbf1^{\mathsf T}\mathsf D_\alpha V_\alpha)}
{\mathbf1^{\mathsf T}\mathsf D_\alpha\mathbf1}.}
\tag{DQ11}
\]
All four denominators are positive by (DQ8)–(DQ9). In particular the mixed innovation entries remain inside the elimination.

## One mixed-face source already makes the Schur form negative

Set
\[
k_i=r_{2\omega_i}(r_{2\omega_i}-\gamma),\qquad
T=\sum_i\omega_i^2k_i>0,\qquad k_0<0.
\]
Take the explicit new source matrix
\[
B_{\mathrm n}=B_*-\tfrac14I,\qquad
F_{B_{\mathrm n}}=\tfrac12\sum_{p<q}X_p\cdot X_q
-3\operatorname{Tr}(B_{\mathrm n}C).
\tag{DQ12}
\]
The vector notation in this source groups the three colors at each face. Its face diagonal vanishes. Its mode coordinates lie wholly in sector \(0\), so only the old identity source couples to it.

Because \(B_{\mathrm n}\) differs from \(B_*\) by an old matrix, its Schur value is equivalently the minimum over the affine line \(B_*+aI\). DQ3 gives
\[
Q_\gamma(B_*,B_*)=12k_0,\qquad
Q_\gamma(I,B_*)=12k_0,\qquad
Q_\gamma(I,I)=6T.
\]
The minimizing complete source and the resulting new-source defect are
\[
\boxed{
B_{\mathrm{opt}}=B_*-\frac{2k_0}{T}I,\qquad
\mathcal S_\gamma(B_{\mathrm n},B_{\mathrm n})
=12k_0-\frac{24k_0^2}{T}<0.}
\tag{DQ13}
\]
Thus the threshold accepted by every old combination is rejected by a concrete relational source after optimal old-source adjustment. This is an exact Gaussian source-completeness test, not a negative physical energy or a change in the dynamics.

[[four-face-optimal-quadratic-response-and-parity|The actual quadratic variational theorem]] determines how the full quadratic minimum changes beyond the harmonic limit. [[four-face-oriented-source-and-the-gap-following-probe|The oriented probe]] belongs to a further source extension because its leading correction is cubic. Neither the old-source floor nor the completed quadratic calculation substitutes for the complete physical source obligation of [[conditional-vacuum-rigidity-and-the-physical-gap|CV]].
