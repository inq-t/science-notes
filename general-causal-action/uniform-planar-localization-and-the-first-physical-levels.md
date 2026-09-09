# Uniform Localization of the First Physical Planar Levels

The complete compact planar theory has a uniform harmonic comparison for its vacuum and first two ordered physical excitations in an explicit growing-patch confinement window. A global magnetic cutoff controls the exterior and its localization cost; the comb metric controls the interior. The proof retains the extensive vacuum energy and dimension dependence of the trial states. Its actual low-level separation supplies the spectral input for the sharper nonlinear remainder estimates.

**Status: proved uniform coarse spectral return for the specified planar family.** Keep the Hamiltonian, full boundary Gauss constraints and comb coordinates of [[planar-patch-confinement-and-the-spatial-soft-mode|PP]] and [[comb-face-transport-and-the-first-nonlinear-jet|FJ]]. [[comb-chart-ellipticity-and-uniform-local-comparison|UC]] supplies the uniform local form comparison. [[planar-physical-cluster-separation-and-the-uniform-window|PS]] supplies the complete invariant harmonic levels. This is a quantitative part of the [[uniform-marked-well-return-and-the-growing-patch-test|growing-patch test]], not a four-dimensional continuum theorem.

## The actual spectral statement

Put
\[
n=L+1,\quad h=(\kappa/g)^{1/4},\quad
E=\sqrt{\kappa g}=\kappa h^{-2},\quad
\epsilon=hn^{10}.
\tag{UP1}
\]
Write \(\widehat E_{m,L}(h)=E_{m,L}(g)/E\) for the actual ordered physical eigenvalues, starting with the vacuum at \(m=0\). Write \(\omega_{m,L}\) for the ordered physical eigenvalues of the oscillator \(\mathcal O_L\), including its vacuum energy.

There are constants \(C,\eta>0\), independent of \(L,h\), such that
\[
\boxed{
|\widehat E_{m,L}(h)-\omega_{m,L}|
\le C\epsilon^{2/3}n^{-4},
\qquad m=0,1,2,\quad 0<\epsilon\le\eta.}
\tag{UP2}
\]
Consequently,
\[
\boxed{
\left|\frac{\Delta_L(g)}E-c_L\right|
\le2C\epsilon^{2/3}n^{-4},\qquad
c_L=4\sqrt2\sin\frac{\pi}{2n}.}
\tag{UP3}
\]
The fractional power measures a coarse localization error. It is not a new term in the fixed-patch Taylor expansion.

## A global magnetic cutoff has no volume factor in its localization cost

Let
\[
W=\sum_p W_p,\qquad W_p=2-\chi_{1/2}(P_p),
\qquad
\widehat H_h=h^2 C_{\rm raw}+h^{-2}W.
\]
Use the raw electric square-field form
\(\Gamma(F)=\sum_{e,a}|D_{e,a}F|^2\).
For one incidence of an edge in a plaquette, the squared trace-gradient norm is \(|\mathbf q_p|^2\), where \(P_p=q_{0,p}I-i\mathbf q_p\cdot\sigma\). Based connectors cancel from the class trace. Each edge belongs to at most two elementary faces, and each face has four edges. Therefore
\[
\boxed{
\Gamma(W)\le 2\sum_e\sum_{p\ni e}|\mathbf q_p|^2
=8\sum_p|\mathbf q_p|^2\le8W.}
\tag{UP4}
\]
The last inequality is \(1-q_{0,p}^2\le2(1-q_{0,p})\). It holds globally, independently of \(L\).

Choose a fixed smooth function \(\vartheta\) equal to zero on \((-\infty,1]\), equal to \(\pi/2\) on \([2,\infty)\), and valued in \([0,\pi/2]\). For \(\delta>0\), set
\[
\chi_0=\cos\vartheta(W/\delta^2),\qquad
\chi_1=\sin\vartheta(W/\delta^2).
\]
These are physical, gauge-invariant multipliers and \(\chi_0^2+\chi_1^2=1\). Equation (UP4) gives the exact IMS estimate
\[
q_h(u)\ge q_h(\chi_0u)+q_h(\chi_1u)
-C_\vartheta\frac{h^2}{\delta^2}\|u\|^2.
\tag{UP5}
\]
On the support of \(\chi_1\), the potential is at least \(\delta^2/h^2\). Thus the entire exterior block has this lower bound, not only selected trial states.

## The small magnetic region is a controlled face chart

In the principal face logarithms \(y_p\), with \(|y_p|\le2\pi\),
\[
W_p=4\sin^2(|y_p|/4),\qquad
\frac{|y|^2}{\pi^2}\le W\le\frac{|y|^2}{4}.
\tag{UP6}
\]
Hence \(\operatorname{supp}\chi_0\subset\{|y|\le\pi\sqrt2\,\delta\}\).
For sufficiently small \(\delta\), this is inside the product logarithm chart. The comb face variables have exactly product Haar measure. Relative to its density at the identity,
\(\rho(y)=\prod_p[\sin(|y_p|/2)/(|y_p|/2)]^2\).

Dilate \(y=hX\). UC proves, on this support, that the actual weighted Rayleigh form differs from that of
\[
\mathcal O_L=-\partial_X^{\mathsf T}(A_L\otimes I_3)\partial_X
+|X|^2/4
\]
by relative error at most
\[
\beta\le C\bigl(n^{3/2}\delta+\delta^2\bigr).
\tag{UP7}
\]
Here \(\|B(y)-B(0)\|\le6\sqrt L\,|y|\), while
\(\sigma_{\min}(B(0))=\sqrt{\lambda_{\min}}\ge2\sqrt2/n\).
The density ratio is between \(e^{-C\delta^2}\) and \(1\), and the magnetic quadratic error is \(O(\delta^2)\) relatively. Both numerator and denominator retain this density. No half-density derivative term is omitted: for this min–max comparison, equivalent weighted measures suffice without conjugating the operator.

Extend interior Dirichlet functions by zero into the invariant oscillator carrier. For \(\beta<1/2\), min–max and (UP5) give
\[
\widehat E_{m,L}(h)
\ge(1-\beta)\omega_{m,L}-C h^2/\delta^2
\tag{UP8}
\]
whenever the exterior threshold \(\delta^2/h^2\) lies above the oscillator levels in question. This is a full-carrier lower bound. It does not assume that all low exact eigenvectors already resemble Gaussians.

## The upper trial spaces have dimension-controlled tails

The first three ordered physical oscillator eigenvectors have total Hermite degree at most four. For \(L\ge2\), only degrees zero and two are needed; degree four covers the second radial excitation at \(L=1\). Their energies satisfy
\[
0<\omega_{m,L}\le Cn^2,\qquad m\le2.
\]
The \(O(n^2)\) includes the extensive vacuum energy \((3/2)\sum_{r,s}\sqrt{\lambda_{rs}}\).

Let \(P_{\le j,L}\) project onto total Hermite degree at most \(j\) on the full oscillator cover. Since every coordinate variance is at most \(\sqrt8\), the creation and annihilation formulas give
\(\|X_i^2P_{\le j,L}\|\le C_j\).
There are \(3L^2\) coordinates. Summing and applying this bound successively through degrees \(j,j+2,j+4\) yields
\[
\||X|^6P_{\le j,L}\|\le C_j n^6.
\tag{UP9}
\]
Thus every normalized vector \(u\) in one of the first three ordered trial spaces obeys
\[
\|\mathbf 1_{\{|X|\ge R\}}u\|\le C n^6R^{-6}.
\]
This deliberately loose moment estimate retains the dimension dependence and needs no fixed-dimensional tail constant.

Set \(R=\delta/h\). Pull \(\chi_0u\) into the compact chart. It vanishes near the chart boundary, so extending it by zero is smooth. If \(\chi_0\ne1\), then (UP6) implies \(|X|\ge2R\). The norm lost by cutting off the trial vector is therefore bounded by
\(t_R=C n^6R^{-6}\).
Also \(\Gamma_{\mathcal O}(\chi_0)\le C/R^2\), since \(\|A_L\|\le8\) and the Euclidean squared gradient of \(W\) is at most \(W\).

For a trial vector \(u\) in an oscillator spectral subspace through \(\omega_{m,L}\), integration by parts gives
\[
q_{\mathcal O}(\chi_0u)
=\operatorname{Re}\langle\chi_0^2u,\mathcal O_Lu\rangle
+\int\Gamma_{\mathcal O}(\chi_0)|u|^2
\le\omega_{m,L}(1+C t_R)+C/R^2.
\]
The weighted norm of this trial vector is at least
\(e^{-C\delta^2}(1-t_R^2)\).
The cutoff map is injective on these trial spaces when \(t_R<1\). UC and min–max consequently give
\[
\widehat E_{m,L}(h)
\le\omega_{m,L}
+C\bigl(\beta\omega_{m,L}+\omega_{m,L}t_R+R^{-2}\bigr).
\tag{UP10}
\]

## One radius proves the uniform window

Choose a sufficiently large fixed number \(A\), then a sufficiently small fixed \(\eta\), and put
\[
R=A n^2\epsilon^{-1/3},\qquad
\delta=hR=A\epsilon^{2/3}n^{-8}.
\tag{UP11}
\]
For every \(n\ge2\), \(0<\epsilon\le\eta\), the chart is valid and \(\beta<1/2\). The exterior threshold
\(R^2=A^2n^4\epsilon^{-2/3}\)
lies above twice the first three oscillator levels. The three error terms satisfy
\[
\begin{aligned}
\beta\omega_{m,L}&\le C\epsilon^{2/3}n^{-9/2},\\
\omega_{m,L}t_R&\le C\epsilon^2n^{-4},\\
R^{-2}&=A^{-2}\epsilon^{2/3}n^{-4}.
\end{aligned}
\]
The density error is smaller still. Equations (UP8) and (UP10) prove (UP2).

By PS's harmonic isolation, shrinking \(\eta\) once more makes the actual vacuum and first physical excitation simple, separated from the remaining spectrum by at least \(c/n\), with \(c>0\) independent of size. This supplies the low-cluster input for quasimode projection and the [[weighted-compact-source-return-on-growing-patches|exact weighted source-return estimate]]. It asserts no rank for a higher degenerate cluster from only three ordered eigenvalues.

## What this settles, and what remains nonlinear

Equation (UP3) proves
\[
\boxed{
\frac{\Delta_L(g)}{E c_L}
=1+O(\epsilon^{2/3}n^{-3}).}
\tag{UP12}
\]
In particular, along \(L\to\infty\) with any \(0<\epsilon_L\le\eta\), even without \(\epsilon_L\to0\),
\(\Delta_L(g)/E\sim2\sqrt2\pi/n\).
At fixed \(\kappa>0\), the absolute gap instead satisfies
\[
\Delta_L(g)\sim2\sqrt2\pi\kappa\,n^{19}/\epsilon_L^2
\longrightarrow\infty.
\]
The complete innovation floor tends to zero at fixed scaled duration and to one at fixed positive physical duration, as the exact spectral identity GW8 specifies. These particular window conclusions now follow from the actual compact theory, without assuming GW3–4.

[[uniform-nonlinear-planar-gap-and-marked-response|The nonlinear return theorem]] adds the actual operator and source calculation: it identifies the \(h^2\) coefficients uniformly and gives fourth-order remainders \(Ch^4n^{21}\) for the scaled gap and \(Ch^4n^{23}\) for the normalized susceptibility. The present coarse comparison selects the eigenbranches and bounds the physical reduced inverse used there. Neither theorem transports the isolated planar vacuum into a larger spatial region or supplies the four-dimensional continuum scaling.
