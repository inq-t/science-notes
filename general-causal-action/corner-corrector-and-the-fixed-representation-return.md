# A Vacuum Corrector Returns Each Fixed Corner Representation

A smooth local cube root of each seam holonomy gives an exactly normalized corrected embedding of the residual class-function rotor. Its first normal derivatives minimize the actual raw-edge kinetic form at the seam well. Concentration of the actual vacuum then proves that each fixed central-spin sector approaches energy \((10\kappa/3)j(j+1)\). The proof uses an exact ground-state form identity and the all-strength lower bound; it does not require an oscillator expansion of the vacuum wavefunction.

**Status: exact corrected isometry and proved fixed-representation bottom limit.** [[strong-seam-corner-and-the-residual-rotor|SR]] fixes the strong-seam family, with \(g_1=g_2=g\), \(\kappa=4\epsilon/3\), and the actual vacuum. [[magnetic-completion-and-the-corner-representation-tail|MT]] supplies the exact lower bound. The complete resolvent return also needs exclusion of additional slow states within each spin sector; the argument here supplies its variational correction and bottom-energy limit.

## The actual vacuum concentrates at the seam well

Write
\[
\mathsf K_g=\mathsf H_g-E_\Omega(g),\qquad
d\mu_g(V,W)=\psi_g(V,W)^2\,dV\,dW,
\quad \int d\mu_g=1.
\tag{CR1}
\]
The positive normalized vacuum \(\psi_g\) is exactly independent of \(U\). Its fast Hamiltonian is
\[
\mathsf H_{{\rm fast},g}
=\kappa\bigl[4(C_V+C_W)+2J_{R,V}\cdot J_{R,W}\bigr]
+g\mathcal V(V,W),
\qquad
\mathcal V=4-\chi_{1/2}(V)-\chi_{1/2}(W).
\]
Its kinetic form is positive and uniformly elliptic. Fix a bi-invariant metric on \(SU(2)\), and set
\[
r(V,W)^2=d(V,I)^2+d(W,I)^2,
\qquad h=(\kappa/g)^{1/4}.
\]
The unique zero of \(\mathcal V\) is \((I,I)\), and compactness together with its positive quadratic minimum gives
\[
c\,r^2\le\mathcal V\le C\,r^2.
\tag{CR2}
\]
For sufficiently small \(h\), a Gaussian of width \(h\) in a fixed logarithm chart, multiplied by a fixed smooth cutoff, has kinetic expectation at most \(C\kappa h^{-2}\) and potential expectation at most \(Cg h^2\). Haar density is smooth and positive there. The trial can be chosen invariant under joint conjugation, so it is admissible in the actual neutral fast carrier. Hence
\[
E_\Omega(g)\le C\sqrt{\kappa g}.
\]
Increasing the constant on a fixed bounded interval of \(g/\kappa\) extends this bound to \(g\ge\kappa\).
Positivity of the kinetic term and (CR2) imply the estimate for the **actual** vacuum
\[
\boxed{\int r^2\,d\mu_g\le C\sqrt{\kappa/g}=Ch^2.}
\tag{CR3}
\]
Thus \(\mu_g\) tends to point mass at \((I,I)\). The Gaussian is used only for a variational energy bound; no trial density replaces \(\mu_g\).

## A globally smooth corrected embedding preserves the Haar norm

Choose an adjoint-invariant smooth cutoff \(\rho\), equal to one near \(I\) and supported strictly inside a logarithm chart. Define
\[
T(V)=\exp\!\left(\frac{\rho(V)}3\log V\right)
\]
in that chart and set \(T(V)=I\) outside it. The cutoff vanishes on a collar of the chart boundary, so \(T\) is globally smooth. It is adjoint equivariant and equals the local cube root near the identity. No global cube-root choice is made.

For a class function \(f\), put
\[
(\mathcal Tf)(U,V,W)=f\!\left(T(V)^{-1}UT(W)\right),
\qquad
\widetilde J_gf=\psi_g(V,W)\mathcal Tf,
\]
\[
J_gf=\psi_g(V,W)f(U).
\tag{CR4}
\]
Equivariance of \(T\) and centrality of \(f\) make \(\mathcal Tf\) invariant under simultaneous conjugation. For fixed \(V,W\), left and right translation preserve \(U\)-Haar measure. Consequently
\[
\boxed{\widetilde J_g^*\widetilde J_g=I,
\qquad \widetilde J_g1=J_g1=\psi_g.}
\tag{CR5}
\]
This is an exact isometry for every \(g\). Both embeddings preserve the \(U\)-Casimir: translating a matrix coefficient leaves its spin unchanged. In particular \(\widetilde J_g\chi_j\) belongs to the complete physical spin-\(j\) block and has norm one.

For each smooth class function, global smoothness of \(T\) gives
\[
|\mathcal Tf(U,V,W)-f(U)|\le C_f r(V,W).
\]
Equation (CR3) therefore yields
\[
\boxed{\|\widetilde J_gf-J_gf\|\le C_fh.}
\tag{CR6}
\]
The constants can be chosen uniformly for unit vectors in any fixed finite span of class characters. No uniform bound over unbounded spin is needed here.

## Use the exact ground-state form before taking the limit

For a smooth physical multiplier \(F(U,V,W)\), the actual vacuum equation and integration by parts give
\[
\langle\psi_gF,\mathsf K_g\psi_gF\rangle
=\kappa\int dU\,d\mu_g\,\mathcal D(F),
\tag{CR7}
\]
where the raw-edge gradient density is
\[
\begin{aligned}
\mathcal D(F)={}&2\sum_i\bigl(
|\mathcal L_{U,i}F|^2+|\mathcal L_{V,i}F|^2
+|\mathcal L_{W,i}F|^2\bigr)\\
&+\sum_i|\mathcal L_{U,i}F+\mathcal L_{V,i}F|^2
+\sum_i|-\mathcal R_{U,i}F+\mathcal L_{W,i}F|^2\\
&+\sum_i|\mathcal R_{V,i}F+\mathcal R_{W,i}F|^2.
\end{aligned}
\tag{CR8}
\]
These are exactly [[corner-hamiltonian-invariant-polynomials|IP3]]'s three two-link paths and three original axes. The magnetic potential and every derivative of \(\psi_g\) cancel by the ground-state identity. This cancellation is exact before localization, so no bound on an approximate vacuum derivative is being assumed.

At \(V=W=I\), the corrected multiplier in (CR4) obeys
\[
\mathcal L_{U,i}\mathcal Tf=\mathcal L_if,
\quad \mathcal R_{U,i}\mathcal Tf=\mathcal R_if,
\]
\[
\mathcal L_{V,i}\mathcal Tf
=\mathcal R_{V,i}\mathcal Tf=-\frac13\mathcal L_if,
\quad
\mathcal L_{W,i}\mathcal Tf
=\mathcal R_{W,i}\mathcal Tf=\frac13\mathcal R_if.
\tag{CR9}
\]
For a class function \(\mathcal L_if=\mathcal R_if\). Substitution into the six rows in (CR8) gives
\[
\mathcal D(\mathcal Tf)(U,I,I)
=\left[2\left(1+\frac19+\frac19\right)
+\frac49+\frac49\right]\sum_i|\mathcal L_if|^2
=\frac{10}{3}\sum_i|\mathcal L_if|^2.
\tag{CR10}
\]
The last, shared-axis row vanishes at this optimized derivative choice. Thus the Schur coefficient is realized by an actual smooth physical multiplier.

The function
\(Q_f(V,W)=\int\mathcal D(\mathcal Tf)(U,V,W)\,dU\)
is smooth on the compact fast manifold. Its deviation from its value at the well is bounded by \(C_fr\). Equations (CR3), (CR7) and (CR10) now prove
\[
\left|
\langle\widetilde J_gf,\mathsf K_g\widetilde J_gf\rangle
-\frac{10\kappa}{3}\langle f,C_Uf\rangle
\right|\le C_f\kappa h.
\tag{CR11}
\]
Polarization gives the corresponding mixed-form limits on each finite character span. The proof is a compact-group argument with the actual vacuum and actual raw-edge form; a principal normal symbol alone would not establish (CR11).

## Each fixed representation reaches the exact lower bound

Let
\[
a_j=\frac{10\kappa}{3}j(j+1),\qquad
e_j(g)=\inf\operatorname{spec}(\mathsf K_g|_{\mathcal H_j}),
\]
where \(\mathcal H_j\) is the complete physical \(U\)-spin block, including all fast states. The exact magnetic-completion inequality MT9 gives \(\mathsf K_g|_{\mathcal H_j}\ge a_j\). Use the norm-one state \(\widetilde J_g\chi_j\) in the variational principle and apply (CR11):
\[
\boxed{
0\le e_j(g)-a_j\le C_j\kappa(\kappa/g)^{1/4},
\qquad g\ge\kappa,
\qquad
e_j(g)\longrightarrow\frac{10\kappa}{3}j(j+1)
\quad\text{for each fixed }j.}
\tag{CR12}
\]
The same bound holds for the excess Rayleigh energy of the corrected state. For \(j=0\), that state is the exact vacuum and the excess is identically zero. For \(j=1/2\), the limiting bottom is \(10\epsilon/3\).

The isometry and representation-tail bound do not by themselves prove that only one slow state survives in a fixed block. [[corner-fast-vacuum-and-harmonic-separation|The fast-excitation estimate]] shows that its second eigenvalue diverges. Equations (CR6) and (CR11) then identify its surviving eigenline with \(J_g\chi_j\): the squared norm of the corrected state's component above the lowest eigenline is bounded by its excess energy divided by the separating gap. [[strong-seam-resolvent-and-the-physical-rotor|The complete return theorem]] combines these conclusions with MT12's uniform representation tail. The fixed-representation result here does not supply a spatial-volume or continuum estimate.
