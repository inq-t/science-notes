# Four-Face Cubic Response and Source Leakage

The actual comb kinetic jet sends the four-face vacuum and soft scalar excitation into finite odd oscillator sectors. Their virtual energy contributions are exactly computable, and every five-quantum component cancels from the normalized source leakage. Two cubic channels remain. Their squared norm is \(2\sqrt2/49+\sqrt3/2\); their contribution to normalized susceptibility is strictly negative. These are fixed-patch coefficients of the specified compact source, not a claim about their spatial accumulation.

**Status: exact finite oscillator calculation with rational radical arithmetic.** [[comb-face-transport-and-the-first-nonlinear-jet|FJ]] fixes the raw edge rows, comb connectors and density convention. [[nonlinear-scalar-source-and-the-vacuum-response-coefficient|NV]] defines the vacuum, excitation and source correctors. [[compact-source-normalization-and-the-nonlinear-return|CS]] proves that these coefficients belong to the actual compact problem at fixed patch size. This note evaluates the cubic and leakage terms at \(L=2\); the direct second-order jet is a separate contribution.

## Fix the mode orientation and the physical source

Order the faces as \(a=(1,1),b=(2,1),c=(1,2),d=(2,2)\). Use the orthogonal mode matrix
\[
\begin{pmatrix}x_a\\x_b\\x_c\\x_d\end{pmatrix}
=O\begin{pmatrix}Y_0\\Y_1\\Y_2\\Y_3\end{pmatrix},
\qquad
O=\frac12
\begin{pmatrix}
1&1&1&1\\
1&-1&1&-1\\
1&1&-1&-1\\
1&-1&-1&1
\end{pmatrix}.
\tag{FC1}
\]
Each entry acts identically on the three color components. The excitation frequencies and vacuum component variances are
\[
(\omega_0,\omega_1,\omega_2,\omega_3)=(\sqrt2,2,2,\sqrt6).
\]
Let \(\Omega\) be the normalized oscillator vacuum and \(K=\mathcal O_2-E_0\). The physical scalar source and its leading vector are
\[
f=\frac{|Y_0|^2/\sqrt2-3}{\sqrt6},\qquad
\phi=f\Omega,\qquad
\|\phi\|=1,\qquad K\phi=c\phi,\quad c=2\sqrt2 .
\tag{FC2}
\]
This is the harmonic normalization of the fixed comb-based compact probe in FJ19 and CS2. All energies in this note are in the scaled units \(\sqrt{\kappa g}\).

For \(I=(i,j,k)\), \(i<j<k\), define
\[
T_I=Y_i\cdot(Y_j\times Y_k),\qquad
E_I=\omega_i+\omega_j+\omega_k,\qquad
N_I=\|T_I\Omega\|^2=6\omega_i\omega_j\omega_k .
\tag{FC3}
\]
The four triples \(012,013,023,123\) give mutually orthogonal physical scalar states of exactly three quanta. Their energies are \(4+\sqrt2\), \(2+\sqrt2+\sqrt6\), \(2+\sqrt2+\sqrt6\), \(4+\sqrt6\); their norms squared are \(24\sqrt2,24\sqrt3,24\sqrt3,24\sqrt6\).

## Contract the original rows before taking resolvents

Write the FJ13 row coefficients in face coordinates as
\[
D_{0,e,t}=\sum_p s_{ep}\,t\cdot\partial_{x_p},\qquad
D_{1,e,t}=\sum_{p,q}z_{epq}(x_q\times t)\cdot\partial_{x_p}.
\]
Their normal-mode coefficients are \(\bar s_e=O^{\mathsf T}s_e\) and
\(\bar z_e=O^{\mathsf T}z_eO\). Put \(\sigma_\mu=(2\omega_\mu)^{-1}\). The coefficient of \(T_I\) in \(V_1\Omega/\Omega\) is the finite contraction
\[
a_I=-2\sum_e\sum_{(\nu,\mu,\lambda)\in{\rm Perm}(I)}
\operatorname{sgn}(\nu,\mu,\lambda)\,
\bar s_{e\nu}\sigma_\nu\sigma_\mu\bar z_{e\mu\lambda}.
\tag{FC4}
\]
Here the sign is relative to the increasing order of \(I\). The cubic product-rule term in FJ17 is determined by the same rows. With
\(r=2/(\sqrt6\,\omega_0)\), its coefficient is zero for \(I=123\); for \(I=(0,i,j)\),
\[
b_I=2r\sum_e\left[
\bar s_{e0}\sum_{(\mu,\lambda)\in{\rm Perm}(i,j)}
\sigma_\mu\bar z_{e\mu\lambda}\operatorname{sgn}(0,\mu,\lambda)
+
\sum_{(\nu,\lambda)\in{\rm Perm}(i,j)}
\bar z_{e0\lambda}\bar s_{e\nu}\sigma_\nu
\operatorname{sgn}(\nu,0,\lambda)\right].
\tag{FC5}
\]
All twelve raw edge rows are used once. Equations (FC4)–(FC5) give the complete vectors
\[
\boxed{
V_1\Omega=\sum_Ia_I T_I\Omega,\qquad
V_1\phi=\sum_I(a_I fT_I+b_I T_I)\Omega .}
\tag{FC6}
\]
Their evaluated coefficients are:

| \(I\) | \(a_I\) | \(b_I\) |
|---|---|---|
| \(012\) | \(-\sqrt2/16\) | \(\sqrt3/12\) |
| \(013\) | \(-\sqrt2/16-\sqrt3/8+\sqrt6/16\) | \(\sqrt2/4+\sqrt3/12\) |
| \(023\) | \(-\sqrt2/16+\sqrt3/24-\sqrt6/48\) | \(-\sqrt2/12+\sqrt3/12\) |
| \(123\) | \(-1/8+\sqrt6/48\) | \(0\) |

The alternating channels include connector-dependent cubic terms. A linear lattice symmetry of the harmonic matrix alone does not license deleting them in this comb presentation.

## The five-quantum part cancels from leakage

Define
\[
\ell_I^{\,0}=\begin{cases}2/\sqrt6,&0\in I,\\0,&0\notin I,\end{cases}
\qquad
Q_I=fT_I-\ell_I^{\,0}T_I .
\tag{FC7}
\]
If \(0\in I\), this is
\(Q_I=(|Y_0|^2-5\omega_0)T_I/(\sqrt6\,\omega_0)\).
It is the pure degree-five Hermite part: the projection of
\(|Y_0|^2Y_{0,a}\) onto \(Y_{0,a}\) has coefficient \(5\omega_0\).
If \(0\notin I\), the independent degree-two source factor already makes \(fT_I\) pure degree five. Therefore
\[
KQ_I\Omega=(E_I+c)Q_I\Omega,\qquad
\langle T_I\Omega,Q_I\Omega\rangle=0,\qquad
\|Q_I\Omega\|^2=\gamma_I N_I,
\quad
\gamma_I=\begin{cases}5/3,&0\in I,\\1,&0\notin I.\end{cases}
\tag{FC8}
\]
The factor \(5/3\) follows from
\(\mathbb E[(|Y_0|^2-5\omega_0)^2Y_{0,a}^2]=10\omega_0^3\).
Different \(I\) remain orthogonal by their distinct mode parities. Thus (FC7)–(FC8) give a complete finite orthogonal resolution of (FC6).

Let \(R=K^{-1}\) on the vacuum complement and
\(R_\phi=(K-c)^{-1}\) on the physical complement of \(\phi\).
The odd states appearing here all have energy greater than \(c\), so both inverses are positive on their supports. The actual first correctors are
\[
\begin{aligned}
u&=-RV_1\Omega=-\sum_I\frac{a_I}{E_I}T_I\Omega,\\
\eta_1&=-R_\phi V_1\phi
=-\sum_I\left[
\frac{a_I\ell_I^{\,0}+b_I}{E_I-c}T_I
+\frac{a_I}{E_I}Q_I\right]\Omega .
\end{aligned}
\tag{FC9}
\]
The vacuum-weighted centered-source correction is \(fu\), as in NV12. Its degree-five term equals the one in \(\eta_1\) exactly: the degree-five excitation denominator is \((E_I+c)-c=E_I\). Hence
\[
\begin{aligned}
\ell=fu-\eta_1
&=\sum_I\left[
\frac{a_I\ell_I^{\,0}+b_I}{E_I-c}
-\frac{a_I\ell_I^{\,0}}{E_I}\right]T_I\Omega\\
&=\boxed{\left(\frac{\sqrt3}{42}T_{012}
+\frac{\sqrt3}{12}T_{013}\right)\Omega .}
\end{aligned}
\tag{FC10}
\]
There is no degree-five leakage. The \(023\) cubic coefficient cancels as well, while the \(123\) channel has neither a cubic source term nor a surviving leakage term.

Using (FC3), the exact squared leakage and its normalized susceptibility contribution are
\[
\boxed{\|\ell\|^2=\frac{2\sqrt2}{49}+\frac{\sqrt3}{2}>0,}
\tag{FC11}
\]
\[
\begin{aligned}
\langle\ell,(R-c^{-1}I)\ell\rangle
&=\frac{2\sqrt2}{49}
\left(\frac1{4+\sqrt2}-\frac1{2\sqrt2}\right)
+\frac{\sqrt3}{2}
\left(\frac1{2+\sqrt2+\sqrt6}-\frac1{2\sqrt2}\right)\\
&=\boxed{-\frac{1101}{2744}+\frac{4\sqrt2}{343}
+\frac{\sqrt3}{8}<0 .}
\end{aligned}
\tag{FC12}
\]
Both differences in the first expression are strictly negative, proving the sign without decimal evaluation. The actual normalized compact-source vector therefore leaves its moving first-excitation line with squared norm \(h^2\|\ell\|^2+O(h^4)\), using CS's fixed-patch expansion and parity. It cannot be replaced by a permanently pure first-mode insertion.

## The two virtual energy terms remain part of the gap coefficient

The same orthogonal resolution evaluates
\[
\begin{aligned}
W_\Omega
&=\langle V_1\Omega,RV_1\Omega\rangle
=\sum_I\frac{N_Ia_I^2}{E_I}\\
&=\boxed{-\frac{117}{56}
+\frac{111\sqrt2}{112}+\frac{\sqrt3}{8}
+\frac{5\sqrt6}{16}},\\
W_\phi
&=\langle V_1\phi,R_\phi V_1\phi\rangle\\
&=\sum_I N_I\left[
\frac{(a_I\ell_I^{\,0}+b_I)^2}{E_I-c}
+\frac{\gamma_Ia_I^2}{E_I}\right]\\
&=\boxed{-\frac{117}{56}
+\frac{37\sqrt2}{16}+\frac{7\sqrt3}{24}
+\frac{5\sqrt6}{16}} .
\end{aligned}
\tag{FC13}
\]
The sum formulas make their positivity explicit. With the actual vacuum subtraction, their contribution to the first excitation gap coefficient is
\[
\boxed{W_\Omega-W_\phi
=-\frac{37\sqrt2}{28}-\frac{\sqrt3}{6}.}
\tag{FC14}
\]
This must be added to
\(\langle\phi,V_2\phi\rangle-\langle\Omega,V_2\Omega\rangle\);
it is not the complete gap correction. Likewise NV13 requires both
\(-d_2/c^2\) and (FC12) in the normalized susceptibility coefficient.
The cancellation of degree-five leakage removes redundant response components, not the virtual energy terms themselves.

The [exact cubic receipt](receipts/four_face_cubic_response_receipt.py) constructs the twelve FJ rows, checks their full incidence spectrum, performs (FC4)–(FC5) in \(\mathbb Q(\sqrt2,\sqrt3)\), and evaluates every displayed resolvent and norm. It uses the established exact radical arithmetic from the corner spin receipt. No sampled path, numerical diagonalization or spectral cutoff enters this calculation. The finite three- and five-quantum spaces are the complete sectors reached by this perturbative order.
