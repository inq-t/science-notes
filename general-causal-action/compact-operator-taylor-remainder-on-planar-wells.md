# Compact Operator Taylor Remainder on Planar Wells

The exact flat-density planar operator has a uniform Taylor remainder in norm on finite-degree oscillator vectors, after restricting to a quantified comb-chart ball. For remainder order \(r=M+1\), the bound is \(C_{m,M}h^r(L+1)^{3r/2+4}\). It includes derivatives of the electric coefficients and the Haar-density terms. Applied to the complete sixth-order formal eigenvector, it yields an interior residual at most \(Ch^7(L+1)^{75/2}\). Global cutoff errors remain a separate contribution.

**Status: proved uniform interior operator estimate and formal-vector residual bound.** [[comb-face-transport-and-the-first-nonlinear-jet|FJ]] fixes the exact comb rows. [[comb-chart-ellipticity-and-uniform-local-comparison|UC18–20]] owns the flat jets and normalized formal recursion. [[uniform-planar-localization-and-the-first-physical-levels|UP]] supplies actual low-level isolation, but the present interior estimate does not use or replace that spectral theorem.

## The exact differential operator includes the density divergence

Put \(n=L+1\), \(d=3L^2\), and write each face as
\(X_p=\exp(-ihx_p\cdot\sigma/2)\). Let \(\mathsf B_h(x)\) be UC's matrix of all scaled raw electric rows. Work on
\[
B_R=\{x:|x|<R\},\qquad
R\ge1,\quad 0<h\le1,\quad h\sqrt L\,R\le1.
\tag{OT1}
\]
The product Haar density is
\(\rho_h=\prod_p[\sin(h|x_p|/2)/(h|x_p|/2)]^2\).
Set
\[
\mathsf A_h=\mathsf B_h^{\mathsf T}\mathsf B_h,\qquad
\ell_h=\nabla_x\log\rho_h,\qquad
W_h=\frac2{h^2}\sum_p(1-\cos(h|x_p|/2)).
\]
Unlike UC12's weighted coefficient \(a_h\), \(\mathsf A_h\) contains no factor \(\rho_h\).

After conjugation by \(\rho_h^{1/2}\), the exact scaled kinetic form is
\(\|\mathsf B_h(\nabla-\ell_h/2)u\|^2\).
Integration by parts gives the exact local differential expression
\[
\boxed{
\mathscr H_h
=-\operatorname{div}(\mathsf A_h\nabla)
+U_h+W_h,\qquad
U_h=\tfrac12\operatorname{div}(\mathsf A_h\ell_h)
+\tfrac14\ell_h^{\mathsf T}\mathsf A_h\ell_h .}
\tag{OT2}
\]
The cross term in the form is
\(-\operatorname{Re}\int\nabla u^*\mathsf A_h\ell_h u\); it becomes the positive divergence term displayed in \(U_h\). In particular the density is not treated as a harmless constant when estimating the operator. At \(h=0\), \(\mathscr H_0=\mathcal O_L\), including its absolute oscillator vacuum energy.

## Mixed derivatives of the real comb rows remain controlled

Write \(\mathsf B_h(x)=\mathsf B(hx)\). In physical log coordinates \(y\), the exact Jacobian and orthogonal-prefix formulas in UC give, for each fixed \(k\ge1\),
\[
\|D_y^k\mathsf B(y)\|_{\mathrm{mult}}\le C_kL^{k/2}
\quad (|y|\le1),\qquad
\|\mathsf B(y)\|\le C
\quad (\sqrt L\,|y|\le1).
\tag{OT3}
\]
The multilinear norm takes unit Euclidean coordinate directions and the operator norm from face covectors to raw-row vectors.

To verify (OT3), differentiate the finite product of real orthogonal adjoint factors. In a given directional slot, the sum over factors is at most
\(\sum_{\rm prefix}|v_p|\le\sqrt L\,|v|\).
The multinomial product rule therefore costs \(L^{k/2}\). Each prefix still acts on only one face derivative, with every face occurring once in that family. Local Jacobian terms have bounded row and column incidence counts. The two conjugation-tail families are linear in \(y\), have first derivative bounded by \(C\sqrt L\), and have no higher derivatives. The single-face logarithmic Jacobians have uniformly bounded derivatives on \(|y_p|\le1\). These observations prove the estimate without an exponential factor in prefix length or in the number of faces.

Let \(\langle x\rangle=(1+|x|^2)^{1/2}\). For fixed integers \(r\ge0\) and \(0\le a\le2\), the mixed derivatives satisfy on (OT1)
\[
\boxed{
\|\partial_h^r D_x^a\mathsf B_h(x)\|
\le C_{r,a}L^{r/2}\langle x\rangle^r,\qquad
\|\partial_h^r D_x^a\ell_h(x)\|
\le C_{r,a}\langle x\rangle^r .}
\tag{OT4}
\]
For the first bound, differentiating
\(D_y^r\mathsf B(hx)[x,\ldots,x]\)
in \(x\) either replaces an \(x\)-slot by the differentiation direction or adds a derivative of \(\mathsf B\) with a factor \(h\). A term with \(k\) additional derivatives costs at most
\[
C_{r,a}L^{r/2}(h\sqrt L)^k
\langle x\rangle^r .
\]
Here \(h\sqrt L\le1\) follows from (OT1). This also covers \(r=0\); the undifferentiated row is bounded by (OT3).

For the second bound, put
\(\Phi(y)=\sum_p2\log[\sin(|y_p|/2)/(|y_p|/2)]\).
Its gradient has norm at most \(C|y|\), and every fixed derivative of order at least two has dimension-independent multilinear norm on \(|y|\le1\). The latter follows from the blockwise single-face derivative bounds and Hölder's inequality on the face index. Since
\(\ell_h=h\nabla_y\Phi(hx)\), the same product rule proves the second estimate in (OT4). Smooth values at the origin remove the apparent radial singularities.

## Taylor remainder before applying the operator

Let \(\mathcal T_M\) denote the Taylor polynomial in \(h\) through degree \(M\), and set \(r=M+1\). All derivatives are taken at fixed \(x\). Equations (OT3)–(OT4), the product rule and integral Taylor remainder give
\[
\begin{aligned}
\|\mathsf A_h-\mathcal T_M\mathsf A_h\|
&\le C_Mh^rL^{r/2}\langle x\rangle^r,\\
\left|\operatorname{div}
(\mathsf A_h-\mathcal T_M\mathsf A_h)\right|
&\le C_Md\,h^rL^{r/2}\langle x\rangle^r,\\
|U_h-\mathcal T_MU_h|
&\le C_Md\,h^rL^{r/2}\langle x\rangle^r,\\
|W_h-\mathcal T_MW_h|
&\le C_Mh^r\langle x\rangle^{r+2}.
\end{aligned}
\tag{OT5}
\]
The divergence is a Euclidean coordinate contraction. Bounding the sum of its \(d\) columns by the sum of their norms gives the displayed factor \(d\), explicitly retained. The same factor bounds the trace in \(\operatorname{div}(\mathsf A_h\ell_h)\). No further dimension factor enters the vector and matrix product estimates.

For the potential, the identity
\[
W_h=\frac12\sum_p|x_p|^2
\int_0^1(1-t)\cos(th|x_p|/2)\,dt
\]
makes every fixed real \(h\)-derivative bounded by
\(C_r\sum_p|x_p|^{r+2}\le C_r|x|^{r+2}\).
Thus the \(h^{-2}\) notation in \(W_h\) causes no negative power in its Taylor remainder.

Since Taylor differentiation commutes with the spatial derivatives, the coefficients of \(\mathscr H_h\) in (OT2) are precisely the flat-density jets \(V_j\) of UC, with \(V_0=\mathcal O_L\). From (OT5), pointwise on \(B_R\),
\[
\begin{aligned}
\left|\left(\mathscr H_h-\sum_{j=0}^Mh^jV_j\right)u\right|
\le C_Mh^r\big[&
L^{r/2}\langle x\rangle^r
\big(\sqrt d\,|\nabla^2u|_{\mathrm{HS}}
+d|\nabla u|+d|u|\big)\\
&+\langle x\rangle^{r+2}|u|\big].
\end{aligned}
\tag{OT6}
\]
The factor \(\sqrt d\) comes from
\(|\operatorname{tr}(A\nabla^2u)|
\le\sqrt d\,\|A\|\,|\nabla^2u|_{\mathrm{HS}}\).
This step estimates the actual differential remainder, rather than inferring an operator norm from its quadratic form.

## Finite Hermite degree converts this into an operator-norm estimate

Let \(P_{\le m,L}\) be the full oscillator total-degree projector. Creation and annihilation bounds, with the sine covariance retained, give for each fixed \(s,m\)
\[
\begin{aligned}
\|\langle x\rangle^su\|&\le C_{m,s}n^s\|u\|,\\
\|\langle x\rangle^s\nabla u\|&\le C_{m,s}n^{s+3/2}\|u\|,\\
\|\langle x\rangle^s\nabla^2u\|_{\mathrm{HS}}
&\le C_{m,s}n^{s+3}\|u\|,
\qquad u\in\operatorname{ran}P_{\le m,L}.
\end{aligned}
\tag{OT7}
\]
For example, each coordinate derivative on fixed degree has norm at most \(C_m\sqrt n\), and each pair at most \(C_mn\). Summing over \(d\) or \(d^2\) components gives the last two powers. Those derivative vectors have degree at most \(m+1\) or \(m+2\), so their weighted moments obey the first bound with the corresponding fixed degree. The constants are independent of the dimension; the explicit powers of \(n\) contain the coordinate count.

Combining (OT6)–(OT7), with \(L\le n\), proves
\[
\boxed{
\left\|\mathbf1_{B_R}
\left(\mathscr H_h-\sum_{j=0}^Mh^jV_j\right)
P_{\le m,L}\right\|
\le C_{m,M}h^{M+1}n^{3(M+1)/2+4}.}
\tag{OT8}
\]
The indicator restricts the output of the local differential expression. It is not differentiated. The input is the uncut oscillator vector, and no operator is assigned outside the chart. The estimate also holds after multiplication of that output by any cutoff of absolute value at most one supported in \(B_R\).

## The sixth-order interior residual meets the required scale

Take either normalized formal branch from UC20 and form
\[
\Psi^{[6]}=\sum_{j=0}^6h^j\psi_j,\qquad
e^{[6]}=\sum_{j=0}^6h^je_j .
\]
For \(hn^{11/2}\) in a sufficiently small fixed interval, \(\Psi^{[6]}\) has norm between \(1/2\) and \(2\), and degree at most twenty. Thus (OT8) at \(M=6\) applies to the whole vector, without multiplying its bound by the norm of an unweighted sixth corrector:
\[
\left\|\mathbf1_{B_R}
\left(\mathscr H_h-\sum_{j=0}^6h^jV_j\right)\Psi^{[6]}
\right\|\le Ch^7n^{29/2}.
\tag{OT9}
\]
The formal eigen-equation cancels every coefficient through order six. The remaining finite products have total order \(k=7,\ldots,12\). UC19–20 bound each by \(C_kh^kn^{11k/2-1}\); the scalar energy products obey the same envelope. Since \(hn^{11/2}\) is small, their sum is bounded by \(Ch^7n^{75/2}\). Consequently
\[
\boxed{
\|\mathbf1_{B_R}(\mathscr H_h-e^{[6]})\Psi^{[6]}\|
\le Ch^7n^{75/2}.}
\tag{OT10}
\]
The stricter window \(hn^{10}\le\eta\) satisfies the required smallness uniformly after fixing \(\eta\).

This is an actual interior residual. For a cutoff \(\chi\), the compact vector also has the term
\([\mathscr H_h,\chi]\Psi^{[6]}\), and its norm and normalization must be controlled with the same dimension dependence. Only after adding those errors and applying actual spectral isolation can (OT10) be used as a compact eigenvector estimate. It does not by itself prove the marked Poisson or susceptibility remainder.
