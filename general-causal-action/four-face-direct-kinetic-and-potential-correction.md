# Four-Face Direct Kinetic and Potential Correction

The complete direct second-order jet on the four-face patch raises the soft scalar excitation relative to the oscillator vacuum by \(-5/32+11\sqrt2/8+\sqrt3/16\). This positive direct contribution is not the gap correction: the cubic virtual transitions must also be included. The Haar half-density term is exactly \(-4\) in both normalized states. The remaining electric and magnetic terms below are evaluated separately from the inherited raw-edge rows, with no face-Casimir reset.

**Status: exact finite Gaussian evaluation of the specified differential jet.** [[comb-face-transport-and-the-first-nonlinear-jet|FJ]] fixes the comb connectors, full Gauss carrier and row coefficients. [[compact-source-normalization-and-the-nonlinear-return|CS]] realizes their fixed-patch spectral expansion; [[nonlinear-scalar-source-and-the-vacuum-response-coefficient|NV]] specifies the vacuum and source normalization. The complementary virtual terms are evaluated in [[four-face-cubic-response-and-source-leakage|FC]]. None of these fixed-patch coefficients is an estimate uniform in spatial size.

## The normalized states and the inherited row form

Put \(h=(\kappa/g)^{1/4}\), and use energy units \(\sqrt{\kappa g}\). Write FJ12 as
\[
\widetilde H_h=\mathcal O_2+hV_1+h^2V_2+\cdots,\qquad
\mathcal O_2=-\partial^{\mathsf T}(A_2\otimes I_3)\partial
+\frac14\sum_p|x_p|^2,\quad A_2=4I-\operatorname{Adj}_2.
\tag{FD1}
\]
Order the faces \(a=(1,1),b=(2,1),c=(1,2),d=(2,2)\), and set
\[
C=A_2^{1/2},\qquad S=\tfrac12A_2^{-1/2},\qquad
\Omega(x)=Z^{-1/2}e^{-\frac12\sum_{p,q}S_{pq}x_p\cdot x_q}.
\tag{FD2}
\]
Thus the three color components are independent under \(\Omega^2dx\), each with face covariance \(C\). The Hadamard modes in FC1 have component variances
\((\sqrt2,2,2,\sqrt6)\). In particular
\[
Y_0=\tfrac12(x_a+x_b+x_c+x_d),\qquad
f=\frac{|Y_0|^2/\sqrt2-3}{\sqrt6},\qquad
\phi=f\Omega,\quad \|\Omega\|=\|\phi\|=1.
\tag{FD3}
\]
Both vectors are in the simultaneous-color invariant carrier. The excitation satisfies
\((\mathcal O_2-E_0)\phi=2\sqrt2\,\phi\).

For each raw edge \(e\) and orthonormal color direction \(t\), use the FJ rows
\[
D_{0,e,t}=\sum_p s_{ep}\,t\cdot\partial_p,\qquad
E_{2,e,t}=D_{2,e,t}+m_{e,t},\qquad
m_{e,t}=\frac1{12}\sum_p s_{ep}\,t\cdot x_p .
\]
The flat-measure rows \(D_0,D_1,E_2\) are skew-adjoint on the polynomial-Gaussian core. Consequently
\[
\begin{aligned}
\langle\psi,V_2\psi\rangle={}&
\underbrace{\sum_{e,t}\bigl(\|D_1\psi\|^2
+2\operatorname{Re}\langle D_0\psi,D_2\psi\rangle\bigr)}
_{\mathcal K(\psi)}\\
&+\underbrace{2\sum_{e,t}\operatorname{Re}
\langle D_0\psi,m_{e,t}\psi\rangle}_{\mathcal J(\psi)}
+\underbrace{\left(-\frac1{192}\sum_p\langle\psi,|x_p|^4\psi\rangle\right)}
_{\mathcal M(\psi)} .
\end{aligned}
\tag{FD4}
\]
Here \(\mathcal M\) denotes the signed, negative magnetic contribution. This form follows before expanding any derivative products, so it keeps the density correction and its sign.

## The density and magnetic contractions

For any normalized real Schwartz vector, integration by parts gives
\[
\mathcal J(\psi)
=-\sum_{e,t}\langle\psi,(D_{0,e,t}m_{e,t})\psi\rangle
=-\frac14\sum_{e,p}s_{ep}^2
=-\frac14\operatorname{tr}A_L=-L^2 .
\tag{FD5}
\]
Thus the density contribution is \(-4\) for both four-face states. It cancels from their difference, while remaining in the individual direct vacuum and excitation energies.

Let
\[
c_0=C_{pp}=\frac{\sqrt2+4+\sqrt6}{4}.
\]
The centered three-color Gaussian identity
\(\mathbb E|x_p|^4=15c_0^2\) gives
\[
\mathcal M(\Omega)=-\frac5{16}c_0^2
=-\frac{15}{32}-\frac{5\sqrt2}{32}
-\frac{5\sqrt3}{64}-\frac{5\sqrt6}{32}.
\tag{FD6}
\]
For the excitation, write \(x_p=Y_0/2+Z_p\); \(Z_p\) is independent of \(Y_0\), with component variance \(c_0-\sqrt2/4\). Under the normalized weight \(f^2\), the soft radial moments change from
\[
\mathbb E|Y_0|^2=3\sqrt2,\quad
\mathbb E|Y_0|^4=30
\quad\text{to}\quad
\mathbb E_f|Y_0|^2=7\sqrt2,\quad
\mathbb E_f|Y_0|^4=150.
\]
Using
\(\mathbb E_Z|vY+Z|^4=v^4|Y|^4+10b v^2|Y|^2+15b^2\), with \(b\) the component variance of \(Z\), yields
\[
\begin{aligned}
\mathcal M(\phi)
&=-\frac58-\frac{35\sqrt2}{96}
-\frac{35\sqrt3}{192}-\frac{5\sqrt6}{32},\\
\mathcal M(\phi)-\mathcal M(\Omega)
&=-\frac5{32}-\frac{5\sqrt2}{24}-\frac{5\sqrt3}{48}.
\end{aligned}
\tag{FD7}
\]

## The electric metric contraction retains all twelve edges

For \(\psi=P\Omega\), with \(P=1\) or \(f\), put
\[
a_p=\partial_pP-\Bigl(\sum_qS_{pq}x_q\Bigr)P .
\]
If
\[
D_{1,e,t}=\sum_p(z_{ep}\times t)\cdot\partial_p,\qquad
D_{2,e,t}=\sum_p(M_{ep}(x)t)\cdot\partial_p,
\]
then the integrands in \(\mathcal K\) are obtained from
\[
\frac{D_0\psi}{\Omega}=\sum_p s_{ep}t\cdot a_p,\quad
\frac{D_1\psi}{\Omega}=\sum_p(z_{ep}\times t)\cdot a_p,\quad
\frac{D_2\psi}{\Omega}=\sum_p(M_{ep}t)\cdot a_p .
\tag{FD8}
\]
The \(z,M\) are exactly FJ3–8, including the ordered vertical prefix and the conjugation tails. For \(L=2\), each nonempty prefix contains only one face. Its extra second-order matrix is
\(\tfrac12\operatorname{ad}_s^2+\tfrac12\operatorname{ad}_{x_p}\operatorname{ad}_s\).

All remaining integrations are finite Wick contractions. If \(W(e)=\mathbb E\prod_p x_p^{e_p}\) for one color and \(e_i>0\), they satisfy
\[
W(e)=\sum_j(e_j-\delta_{ij})C_{ij}\,
W(e-\mathbf e_i-\mathbf e_j),\qquad W(0)=1;
\tag{FD9}
\]
terms with zero coefficient are omitted. Different colors factor. Rotational invariance allows one fixed \(t\), followed by multiplication by three. Applying (FD8)–(FD9) to the twelve rows gives
\[
\begin{array}{c|cc}
&\Omega&\phi\\ \hline
\sum\|D_1\psi\|^2&
-\frac{63}{16}+\frac{9\sqrt2}{4}+\frac{9\sqrt3}{16}+\frac{9\sqrt6}{8}&
-\frac{63}{16}+\frac{21\sqrt2}{4}+\frac{21\sqrt3}{16}+\frac{9\sqrt6}{8}\\[2pt]
2\sum\langle D_0\psi,D_2\psi\rangle&
\frac{25}{16}-\frac{17\sqrt2}{16}-\frac{7\sqrt3}{16}-\frac{11\sqrt6}{16}&
\frac{25}{16}-\frac{119\sqrt2}{48}-\frac{49\sqrt3}{48}-\frac{11\sqrt6}{16}
\end{array}
\tag{FD10}
\]
Their sums are
\[
\begin{aligned}
\mathcal K(\Omega)&=-\frac{19}{8}+\frac{19\sqrt2}{16}
+\frac{\sqrt3}{8}+\frac{7\sqrt6}{16},\\
\mathcal K(\phi)&=-\frac{19}{8}+\frac{133\sqrt2}{48}
+\frac{7\sqrt3}{24}+\frac{7\sqrt6}{16},\\
\mathcal K(\phi)-\mathcal K(\Omega)&=\frac{19\sqrt2}{12}+\frac{\sqrt3}{6}.
\end{aligned}
\tag{FD11}
\]
The exact arithmetic receipt [[receipts/four_face_direct_receipt.py]] constructs these original-coordinate rows and performs (FD9) over \(\mathbb Q(\sqrt2,\sqrt3)\). It also checks the covariance-precision identity, the incidence Gram matrix, state norms and independent magnetic identities. It uses no random samples or numerical spectral approximation.

## The direct difference and the one-face control

Combining the three contributions gives
\[
\begin{aligned}
\langle\Omega,V_2\Omega\rangle
&=-\frac{219}{32}+\frac{33\sqrt2}{32}
+\frac{3\sqrt3}{64}+\frac{9\sqrt6}{32},\\
\langle\phi,V_2\phi\rangle
&=-7+\frac{77\sqrt2}{32}
+\frac{7\sqrt3}{64}+\frac{9\sqrt6}{32},\\
D_{\rm direct}
&=\boxed{-\frac5{32}+\frac{11\sqrt2}{8}+\frac{\sqrt3}{16}}.
\end{aligned}
\tag{FD12}
\]
For \(L=1\), the radial vectors make both electric metric terms zero, the density term is \(-1\), and the magnetic terms are \(-5/16,-25/16\). The individual direct energies are \(-21/16,-41/16\), with difference \(-5/4\), exactly the first correction in [[one-plaquette-nonlinear-source-response|OP]].

At four faces, \(V_1\Omega\) and \(V_1\phi\) are nonzero. The full gap coefficient is therefore
\[
d_2=D_{\rm direct}
+\langle V_1\Omega,RV_1\Omega\rangle
-\langle V_1\phi,R_\phi V_1\phi\rangle ,
\tag{FD13}
\]
with the actual reduced oscillator inverses specified in NV. The direct split depends on the fixed coordinate and density convention; only the complete expression is the spectral coefficient. FC supplies the two virtual terms, and the compact-source susceptibility additionally requires its source-leakage term.
