# Equal Character Hessians Leave a Nonlinear Source Response Undetermined

Two positive preparations can have the same faithful representation, total weight, character Hessian, physical scale and complete first-order source chronology, yet different conditional fourth cumulants and different second-order physical gap coefficients. An explicit three-block family on \(SU(2)\) separates them using the same bounded Lie source and clock. This tests a reduction of the declared input to its metric and Lie bracket; the full preparation weight distinguishes the members and is not held fixed.

**Status: exact finite preparation family and actual fixed-patch second-order source and gap differences.** [[weighted-character-scale-and-bounded-lie-sources|GM]] fixes the weighted character cost and the bounded source. [[all-group-oriented-kinetic-jet-and-source-lift|AJ]] fixes the normalized first operator. [[logarithmic-vacuum-curvature-and-conditional-cumulants|LCV]] supplies the actual conditional fourth-cumulant return, including the source's coordinate correction. No claim about a continuum universality class follows from this finite-scale distinction.

## Hold the representation, trace and Hessian fixed

Use \(G=SU(2)\), \(Q(e_a,e_b)=\delta_{ab}\), and the fundamental generators \(d\rho_{1/2}(e_a)=-i\sigma_a/2\). Fix once and for all the faithful representation
\[
\rho=\rho_{1/2}\oplus\rho_1\oplus\rho_{3/2}.
\tag{EH1}
\]
The fundamental block makes the direct sum faithful. For the unit vector \(H=e_3\), its blocks have the following exact moments:

| Block | Dimension | \(-\operatorname{Tr}d\rho(H)^2\) | \(\operatorname{Tr}d\rho(H)^4\) |
| --- | --- | --- | --- |
| \(\rho_{1/2}\) | \(2\) | \(1/2\) | \(1/8\) |
| \(\rho_1\) | \(3\) | \(2\) | \(2\) |
| \(\rho_{3/2}\) | \(4\) | \(5\) | \(41/4\) |

These follow by summing the second and fourth powers of the weights \(\pm1/2\), \(0,\pm1\), and \(\pm1/2,\pm3/2\). The latter block is the symmetric cube of the fundamental representation. Adjoint invariance extends the table to every \(H\), with factors \(\|H\|_Q^2\) and \(\|H\|_Q^4\).

Set
\[
\boxed{
A_\varepsilon=(1+14\varepsilon)I_2
\oplus(1-16\varepsilon)I_3
\oplus(1+5\varepsilon)I_4,\qquad
-\frac1{14}<\varepsilon<\frac1{16}.}
\tag{EH2}
\]
Every block is strictly positive, and \(A_\varepsilon\) commutes with \(\rho(G)\). The identities
\[
28-48+20=0,\qquad 7-32+25=0
\]
give
\[
\boxed{
\operatorname{Tr}A_\varepsilon=9,\qquad
I_{A_\varepsilon}=\frac{15}{2}.}
\tag{EH3}
\]
In contrast, \(14/8-32+205/4=21\), so
\[
\boxed{
\operatorname{Tr}\!\left(A_\varepsilon d\rho(H)^4\right)
=\left(\frac{99}{8}+21\varepsilon\right)\|H\|_Q^4.}
\tag{EH4}
\]
Thus even fixing both the total weight and the quadratic index leaves a nonzero fourth-character variation.

For the actual cost \(W_{A_\varepsilon}\), every member still has a unique identity minimum by faithfulness and positivity. On the same four-face graph, keep \(\kappa,g>0\) fixed. Then all members have
\[
g_{\rm eff}=15g,\qquad
h=(\kappa/(15g))^{1/4},\qquad
E=\sqrt{15\kappa g}.
\tag{EH5}
\]
Their harmonic vacuum, covariance, raw normalized odd operator \(V_1\), first vacuum score \(\alpha\), normal form \(S\), and first chronological source jets agree. The graph, bracket, representation and source functions also agree. Their actual second operator differs through the quartic cost in EH4.

## Keep the original bounded source in the comparison

Because \(\rho\) is fixed, GM's unweighted projection source \(q_\rho\) is the same function in every member. Its unweighted index and fourth trace are
\[
I_\rho=\frac{15}{2},\qquad
J_{4,\rho}=\frac{99}{8}.
\]
On the \(SU(2)\) Lie algebra, equivariance and the one-dimensional stabilizer-fixed direction at \(X\ne0\) make the cubic projection radial. Contracting it with \(d\rho(X)\) in the real Hilbert–Schmidt inner product gives
\[
(d\rho)^{-1}\Pi_\rho(d\rho(X)^3)
=-\frac{J_{4,\rho}}{I_\rho}\|X\|_Q^2X
=-\frac{33}{20}\|X\|_Q^2X.
\]
Consequently the actual scaled mark has local expansion
\[
\boxed{
\widehat X_h=\frac2h q_\rho(e^{hX})
=X-\frac{11}{40}h^2\|X\|_Q^2X+O(h^4).}
\tag{EH6}
\]
The cubic source correction is independent of \(\varepsilon\). It must be retained when comparing fourth cumulants; replacing this source by a cutoff logarithm would be a different experiment.

Retain the three complete faces \(S=r^c\). Let
\[
C=\sqrt{A_2},\qquad
\sigma_r=((C^{-1})_{rr})^{-1},\qquad
\mathcal J_r=\int_0^\infty\sum_{p=1}^4
\bigl(e^{-sC}\bigr)_{pr}^{\,4}\,ds>0.
\tag{EH7}
\]
Here \(A_2\) is the inherited four-face incidence matrix. The integral is finite by the positive oscillator frequencies and positive since its \(p=r\) term starts at one.

LCV's fourth-cumulant theorem, including the cubic coordinate term in EH6, gives for every fixed \(H\)
\[
\boxed{
\begin{aligned}
\operatorname{cum}_{4,\varepsilon,h}
\bigl(Q(H,\widehat X_{r,h})\mid X_S\bigr)
={}&h^2\|H\|_Q^4
\left[
\left(\frac{33}{20}+\frac{14}{5}\varepsilon\right)
\sigma_r^4\mathcal J_r-\frac{33}{5}\sigma_r^3
\right]+O(h^3).
\end{aligned}}
\tag{EH8}
\]
The remainder is in each prescribed fixed \(L^p\) of the actual retained marginal, with fixed parameters and patch. The last term follows from
\(4\sigma_r^3\partial_H^3 Q(H,-11\|X\|^2X/40)
=-33\sigma_r^3\|H\|^4/5\).
Thus the positivity of the cutoff-log cumulant is not asserted for this different source. Its variation between members is unambiguous.

## A closed invariant statistic detects the difference

The directional tensor in EH8 is a framed presentation. Its double trace gives an invariant scalar diagnostic. In each actual law define
\[
Z_r=\widehat X_{r,h}
-\mathbb E_{\varepsilon,h}[\widehat X_{r,h}\mid X_S],
\qquad
V_r=\mathbb E_{\varepsilon,h}[Z_r\otimes Z_r\mid X_S],
\]
\[
\mathcal K_{\varepsilon,h}
=\mathbb E_{\varepsilon,h}[\|Z_r\|_Q^4\mid X_S]
-(\operatorname{Tr}V_r)^2-2\operatorname{Tr}(V_r^2).
\tag{EH9}
\]
All these operations use the same complete conditional law. The scalar is invariant under simultaneous conjugation because the centered vector and covariance transform covariantly.

For a rotationally invariant symmetric fourth tensor on three dimensions, the double trace is five times its value on a unit vector: if the tensor is \(c(\delta_{ab}\delta_{cd}+\delta_{ac}\delta_{bd}+\delta_{ad}\delta_{bc})\), those values are \(15c\) and \(3c\). EH8 therefore implies
\[
\boxed{
\mathbb E_{\varepsilon,h}\mathcal K_{\varepsilon,h}
=h^2\left[
\left(\frac{33}{4}+14\varepsilon\right)
\sigma_r^4\mathcal J_r-33\sigma_r^3
\right]+O(h^3).}
\tag{EH10}
\]
Only the leading fourth tensor needs rotational invariance; its coefficient is independent of the retained values. LCV's conditional moment bounds justify the products and subsequent integration.

For any fixed two parameters in EH2,
\[
\boxed{
\mathbb E_{\varepsilon_2,h}\mathcal K_{\varepsilon_2,h}
-\mathbb E_{\varepsilon_1,h}\mathcal K_{\varepsilon_1,h}
=14(\varepsilon_2-\varepsilon_1)
\sigma_r^4\mathcal J_r\,h^2+O(h^3).}
\tag{EH11}
\]
It is nonzero for sufficiently small positive \(h\) when \(\varepsilon_1\ne\varepsilon_2\). The common cubic source correction cancels. The difference cannot be removed by the common quadratic scale or an odd normal-form convention.

## The same deformation changes the actual finite physical gap

Write \(\widehat H_\varepsilon=H_{\kappa,g,A_\varepsilon}/E\), and let \(\Delta_\varepsilon(h)\) be its first positive gap above the vacuum on the simultaneous-Gauss physical carrier. The scale \(E\) is common to every member. The only changing term is the character cost. Its constant and quadratic variations vanish, and EH4 gives the local weighted jet
\[
\boxed{
\partial_\varepsilon\widehat H_\varepsilon
=-\frac7{120}h^2\sum_p\|X_p\|_Q^4+O(h^4).}
\tag{EH12}
\]

Put \(d=3\), \(\omega=\sqrt2\), \(c_0=C_{aa}\). The normalized lowest physical harmonic state is
\[
\phi=\frac{\|Y_0\|^2-d\omega}{\sqrt{2d}\,\omega}\Omega .
\]
There is no invariant one-quantum state, and the lowest-mode invariant quadratic is unique. Its energy \(2\sqrt2\) is simple and isolated from the other physical harmonic levels.

Let \(R=\|Y_0\|^2\). Gaussian radial moments give
\[
\langle R\rangle_\phi-\langle R\rangle_\Omega=4\omega,\qquad
\langle R^2\rangle_\phi-\langle R^2\rangle_\Omega
=12(d+2)\omega^2.
\]
For each face, \(X_p=Y_0/2+\eta_p\), where \(\eta_p\) is independent of \(Y_0\) with component variance \(c_0-\omega/4\). The residuals at different faces need not be independent. Conditional Gaussian contraction yields
\[
\boxed{
\left\langle\sum_p\|X_p\|^4\right\rangle_\phi
-\left\langle\sum_p\|X_p\|^4\right\rangle_\Omega
=(d+2)(8c_0\omega+\omega^2)
=5(8\sqrt2+6+4\sqrt3).}
\tag{EH13}
\]

These harmonic expectations determine an actual parameter derivative. On any compact interval \(I\) inside EH2's positivity interval, the character weights have a uniform positive lower bound and the same unique identity well. The fixed-level localization and equivariant quasimode proof of [[compact-source-normalization-and-the-nonlinear-return|CS]], used with this smooth weighted cost as in [[fixed-group-compact-vacuum-and-oriented-source-return|GV]], therefore has uniform constants on \(I\). It returns the actual simple vacuum and lowest physical branches to \(\Omega,\phi\). No coefficient of the original fundamental-representation second operator is imported.

At each sufficiently small fixed \(h\), the two simple branches are differentiable in \(\varepsilon\). Feynman–Hellmann subtracts their actual expectations of EH12. Take arbitrarily accurate eigenvector quasimodes before multiplying its globally \(O(h^{-2})\) compact operator; order five suffices for an \(O(h^3)\) error. The local quartic leading term and weighted localization then give
\[
\boxed{
\partial_\varepsilon\Delta_\varepsilon(h)
=-\frac7{24}(8\sqrt2+6+4\sqrt3)h^2+O_I(h^3).}
\tag{EH14}
\]
Integrating on \(I\) proves
\[
\boxed{
\Delta_{\varepsilon_2}(h)-\Delta_{\varepsilon_1}(h)
=-\frac7{24}(8\sqrt2+6+4\sqrt3)
(\varepsilon_2-\varepsilon_1)h^2
+O_I(|\varepsilon_2-\varepsilon_1|h^3).}
\tag{EH15}
\]
Increasing \(\varepsilon\) lowers the actual first physical gap for sufficiently small \(h\), while preserving the entire first-order inventory and scale. The unknown common second-order contribution cancels in the parameter difference. Multiplication by the common \(E\) restores physical units. This is a fixed four-face spectral result, without uniform spatial or continuum control.

## What this discriminator decides

The metric, Lie bracket, total weight and first-order source law do not determine the full finite prepared joint state or its nonlinear gap coefficient. EH11 and EH15 exhibit actual distinctions missed by that reduced inventory. A proposed law using only those inputs must either supply the remaining preparation data or prove that its intended return is insensitive to them in the required limit.

The complete declared weight \(A_\varepsilon\) changes in this family. This is not retuning with every primitive fixed, and it does not contradict the original determinant amplitude once its full preparation is specified. Nor does a different finite-scale cumulant imply a different continuum Yang–Mills universality class. The result identifies a concrete higher-order source channel that any claimed reduction must retain or control; it supplies neither an absolute scale nor a uniform physical-gap theorem.

[[weighted-character-gap-coefficient-and-the-spatial-soft-mode|The growing-patch coefficient]] and [[uniform-weighted-character-return-and-the-soft-gap|its actual uniform return]] now extend the spectral contrast: it follows the closing harmonic frequency throughout the quantified confinement window. [[character-response-and-the-bulk-vacuum-normalization|The same variation of the closed trace]] has an extensive vacuum coefficient and a fixed normalized relation to this soft-gap response. [[character-memory-in-the-local-conditional-fourth-cumulant|The local conditional contrast]] separately has a positive bulk coefficient; its actual return is fixed-patch, with a uniform conditional remainder still required.
