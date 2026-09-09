# Spatial Word Comparison and Mixed Motion

Comparing three actual words of a declared two-cell graph gives a positive transfer on its complete two-loop carrier. The composite word retains the signed relative orientation and produces a mixed kinetic term. Two Gaussian matrix copies provide enough inverse moments for an ordinary diffusion limit. The comparison metric is proportional to the endpoint Schur metric of the seven-link graph, and the limit is exactly the electric operator of the existing two-plaquette benchmark. The graph, elementary link metric, nonlinear comparison, replication and duration remain inputs. No magnetic vacuum or four-dimensional return is obtained here.

## Three words on one spatial diagram

Take three oriented paths \(p,u,v\) between two vertices, with \(p\) the common path of two cells. Multiplication and inversion give
\[
x=up^{-1},\qquad y=vp^{-1},\qquad r=xy^{-1}=uv^{-1}.
\tag{SW1}
\]
For adjacent squares, \(p\) has one link and each outer path has three. Tree reduction leaves the complete carrier \(L^2(SU(2)^2,dx\,dy)^{\operatorname{Ad}SU(2)}\), with normalized product Haar and simultaneous conjugation. The [[gauge-cycle-innovation-filtration/loop-coordinates-and-the-induced-clock|induced-clock construction]] owns this reduction and the transport under a change of tree.

Let \(V=M_2(\mathbb C)\), \(h(A,B)=\operatorname{Tr}(A^\dagger B)/2\), and \(E=V\oplus V\). Use one circular complex Gaussian \(\Xi=(\xi_1,\xi_2)\in E\) per transfer edge, with positive covariance \(\Gamma\). In orthonormal complex coordinates,
\[
d\gamma_\Gamma(\Xi)=\frac{e^{-\Xi^\dagger\Gamma^{-1}\Xi}}{\det\Gamma}
\prod_{j=1}^{8}\frac{d\Re\Xi_j\,d\Im\Xi_j}{\pi},
\qquad S=\|\Xi\|^2.
\tag{SW2}
\]
The main example is \(\Gamma=I_E\), hence \(S\sim\operatorname{Gamma}(8,1)\). Both copies are shared across all three words within the edge. Their use is a declared preparation choice. Simultaneous conjugation of the complete marked law also transports \(\Xi\) and its sources; a fixed prior invariant under that action includes \(\Gamma=I_E\).

Write \(L_g\) for left multiplication on both copies. For \(q=(x,y)\), define
\[
\Phi_q\Xi=(\sqrt3 L_x\Xi,\sqrt3 L_y\Xi,L_{xy^{-1}}\Xi),
\qquad
K_\alpha(q,q')=\mathbb E_\Gamma e^{-\alpha\|(\Phi_q-\Phi_{q'})\Xi\|^2}.
\tag{SW3}
\]
The finite comparison (SW3) is a prescription. Its coefficient ratio \(3,3,1\) has the conditional tangent derivation below from the declared elementary link metric; the nonlinear extension and overall scale are not thereby selected. Using actual products makes (SW1) an identity on the same preparation, without replacing the words by commutator features or adding fresh variables when a word is reassociated.

For \(c(g)=\operatorname{Tr}(g)/2\), the special \(SU(2)\) identity \((g-h)^\dagger(g-h)=2[1-c(g^{-1}h)]I_2\) gives
\[
\begin{aligned}
\|(\Phi_q-\Phi_{q'})\Xi\|^2&=d(q,q')^2S,\\
d(q,q')^2&=2\{3[1-c(x^{-1}x')]+3[1-c(y^{-1}y')]
+[1-c((xy^{-1})^{-1}x'y'^{-1})]\},\\
K_\alpha(q,q')&=\det(I_E+\alpha d(q,q')^2\Gamma)^{-1}.
\end{aligned}
\tag{SW4}
\]
In particular \(K_\alpha=(1+\alpha d^2)^{-8}\) for the main example.

## Invariance, coverage and the full Gaussian marks

Independent left translations \((x,y)\mapsto(hx,ky)\) send the third word to \(hxy^{-1}k^{-1}\). Its chord distance is unchanged, as are the first two distances. Thus the unmarked kernel is left invariant on \(SU(2)^2\). More explicitly, setting \(x'=xa\), \(y'=yb\), gives
\[
d(q,q')^2=\delta(a,b)^2
=2\{3[1-c(a)]+3[1-c(b)]+[1-c(ab^{-1})]\}.
\tag{SW5}
\]
This uses conjugation invariance of the trace; it does not assert that the matrix words themselves are unchanged. The relative kernel is invariant under joint conjugation and under \((a,b)\mapsto(a^{-1},b^{-1})\).

For each preparation with invertible \(\xi_1\), \(q\mapsto\Phi_q\Xi\) is an injective compact embedding because its first two components already determine \(x,y\). Almost every \(\xi_1\) is invertible. The Gaussian distance kernel on the ambient real vector space has strictly positive energy on every nonzero finite complex measure, by its strictly positive Fourier density. Pushing forward a nonzero Haar-density measure and then averaging proves that \(K_\alpha\) is Hilbert positive and injective on the full \(L^2(SU(2)^2)\). This is the same argument as [[relative-multiplication-transfer-and-the-rotor-limit|relative multiplication]], now with actual spatial words. No sector is removed by a commutator quotient.

Arbitrary joint linear and quadratic Gaussian marks remain explicit. For \(j\in E\), \(T=T^\dagger\) and \(A=\Gamma^{-1}+\alpha d^2I_E+T>0\),
\[
K_\alpha(q,q';j,T)
=\int e^{-\alpha d^2S+2\Re(j^\dagger\Xi)-\Xi^\dagger T\Xi}d\gamma_\Gamma
=\frac{e^{j^\dagger A^{-1}j}}{\det\Gamma\,\det A}.
\tag{SW6}
\]
Sources on the two complete readouts \((\Phi_q\Xi,\Phi_{q'}\Xi)\) pull back to this formula, including arbitrary off-diagonal quadratic source blocks. The conditional covariance is \(A^{-1}\), and the cross covariance of these readouts is \(\Phi_q A^{-1}\Phi_{q'}^\dagger\); it is not a product of independently prepared word states. Source transformations must accompany changes of presentation, as in [[marked-gaussian-constraints-and-sewing-measures|marked Gaussian sewing]].

## The inherited mixed kinetic operator

Set \(z_\alpha=\int K_\alpha(q,q')dq'\), independent of \(q\), and let \(P_\alpha\) have kernel \(K_\alpha/z_\alpha\). It is a self-adjoint Markov contraction, Hilbert positive and injective. Use the declared duration \(\epsilon=1/\alpha\).

To fix all metric factors, let \(X_A=-i\sigma_A/2\) be orthonormal for \(Q=-2\operatorname{Tr}\), and define the right-multiplication derivatives
\[
R_{x,A}f=\left.\frac d{dt}\right|_0f(xe^{tX_A},y),
\qquad D_{Q,x}=-\sum_AR_{x,A}^2,
\tag{SW7}
\]
with the analogous definitions for \(y\). These fields commute with left translations. The unit-round-\(S^3\) derivatives are \(2R_{x,A}\), so \(D_{S^3,x}=4D_{Q,x}\).

In round coordinates \(a=e^{-i s\cdot\sigma}\), \(b=e^{-i t\cdot\sigma}\),
\[
\delta(a,b)^2
=4|s|^2+4|t|^2-2s\cdot t+O(|(s,t)|^4),
\quad
M=\begin{pmatrix}4&-1\\-1&4\end{pmatrix}\otimes I_3,
\quad
M^{-1}=\frac1{15}\begin{pmatrix}4&1\\1&4\end{pmatrix}\otimes I_3.
\tag{SW8}
\]
This ratio has an exact endpoint origin. Give each of the seven links the same quadratic tangent cost in a common transported frame. Minimizing the three constituent increments of each outer path gives the path cost \(|A|^2+|B|^2/3+|C|^2/3\), with \(A,B,C\) the increments of \(p,u,v\). At the tree representative \(p=I\), the loop increments are \(X=B-A\), \(Y=C-A\), and
\[
\min_A\left\{|A|^2+\frac{|A+X|^2}{3}+\frac{|A+Y|^2}{3}\right\}
=\frac{4|X|^2+4|Y|^2-2X\cdot Y}{15},
\qquad A_*=-\frac{X+Y}{5}.
\tag{SW8a}
\]
Thus (SW8) is fifteen times the induced Schur metric. Equivalently, \(\Phi/\sqrt{15}\) realizes that metric exactly at tangent order. Bi-invariance transports the calculation to other tree representatives. The eliminated common increment is the other-endpoint gauge freedom \((p,u,v)\mapsto(ph^{-1},uh^{-1},vh^{-1})\), which fixes \(x,y\); it is not the remaining simultaneous conjugation of the two loops. [[marked-gaussian-constraints-and-sewing-measures|Gaussian disintegration]] supplies the corresponding determinant and source factors if this minimization is implemented by integration. This conditional metric derivation does not uniquely extend the tangent law to (SW3).

The positive off-diagonal mobility comes from the inverse of the metric contributed by the composite word. Sharing only a scalar Gaussian amplitude across separate word comparisons would not supply this mixed quadratic term.

Define
\[
\rho_\Gamma=\frac{\mathbb E_\Gamma S^{-4}}{\mathbb E_\Gamma S^{-3}},
\qquad \kappa=\frac{\rho_\Gamma}{15}.
\tag{SW9}
\]
All inverse moments through order five are finite for positive \(\Gamma\) on complex dimension eight: couple \(S\ge\lambda_{\min}(\Gamma)T_8\) with \(T_8\sim\operatorname{Gamma}(8,1)\). Gaussian localization in the six round coordinates therefore gives, uniformly for \(C^4\) functions,
\[
\begin{aligned}
z_\alpha&=\frac{\mathbb E S^{-3}}{4\pi\,15^{3/2}}\alpha^{-3}[1+O(\alpha^{-1})],\\
P_\alpha f&=f-\alpha^{-1}Hf+O_f(\alpha^{-2}),\\
H&=\kappa\left[4(D_{Q,x}+D_{Q,y})-2\sum_AR_{x,A}R_{y,A}\right].
\end{aligned}
\tag{SW10}
\]
For the expansion, condition on \(S\). The leading Gaussian has quadratic form \(\alpha S M\), integral proportional to \((\alpha S)^{-3}\), and covariance \((2\alpha S)^{-1}M^{-1}\). Its fourth moment and the quartic geometric corrections are controlled after averaging by \(\mathbb E S^{-5}\). The region \(\alpha S<1\) contributes only \(O(\alpha^{-8})\) before normalization. Inversion symmetry cancels odd terms. This proves both the coefficient and the stated remainder. For \(\Gamma=I_E\), \(\rho_\Gamma=1/4\) and \(\kappa=1/60\).

The positive form of \(H\) is
\[
\kappa\int\sum_A\left[3|R_{x,A}f|^2+3|R_{y,A}f|^2
+|R_{x,A}f+R_{y,A}f|^2\right]dx\,dy.
\tag{SW11}
\]
It is uniformly elliptic on the compact product, with form domain \(H^1\), operator domain \(H^2\), and smooth core. Its restriction to simultaneous invariants is the corresponding closed physical operator. The contraction product theorem applied to (SW10) gives \(P_\alpha^{\lfloor\alpha t\rfloor}\to e^{-tH}\) strongly on the entire carrier for each \(t\ge0\). This is the electric operator of [[coarse-response-memory/two-plaquette-vacuum-and-relational-state|the two-plaquette construction]], in the declared units. No operator-norm convergence claim is required here.

One matrix copy has \(S\sim\operatorname{Gamma}(4,1)\) at identity covariance, so \(\mathbb E S^{-4}\) diverges. It does not satisfy this ordinary diffusion theorem. [[preparation-rank-and-locality|Preparation rank and locality]] separates the required configuration dimension and inverse moments from any spacetime-dimensional claim.

## A signed first-order crossing witness

Write \(x=aI-i\mathbf x\cdot\sigma\), \(y=bI-i\mathbf y\cdot\sigma\), and \(z=\mathbf x\cdot\mathbf y\). The three retained word traces \((w_1,w_2,w_3)=(a,b,ab+z)\) separate simultaneous-conjugation orbits. Their anchored source partition function is \(Z(\lambda)=\det[I_E+2\sum_i\lambda_i(1-w_i)\Gamma]^{-1}\), so \(-\partial_{\lambda_i}\log Z|_0=2\operatorname{Tr}_E(\Gamma)(1-w_i)\). Thus independent sources recover all three traces; no sign of \(z\) is identified with its opposite.

More strongly, the full kinetic response obeys
\[
Ha=3\kappa a,\qquad Hb=3\kappa b,\qquad
H(ab)=\kappa(6ab-z/2).
\tag{SW12}
\]
Indeed \(R_xa=-\mathbf x/2\), \(R_yb=-\mathbf y/2\). For \(P_t=e^{-tH}\),
\[
P_t(ab)-(P_ta)(P_tb)=\frac{\kappa t}{2}z+O(t^2).
\tag{SW13}
\]
Thus the first mixed motion already carries the signed angular channel. It is absent from two independently reset loop diffusions. Recovering the internally interacting vacuum and its two radial tangent channels remains the further test in [[coarse-response-memory/correlated-interface-tangent|the correlated-interface benchmark]]; equations (SW12)–(SW13) do not claim that return.

Successive transfer edges use independent copies of the entire preparation (SW2), while every word within one edge uses the same preparation. Ordinary gluing integrates the intermediate full loop pair and transports all marks in (SW6). The raw normalization remains \(K_\alpha^m=z_\alpha^mP_\alpha^m\). Reusing one \(\Xi\) over several successive edges instead gives a different, generally non-Markov boundary law and must retain that shared variable. This finite spatial construction supplies a mixed response and its complete source measure; it does not select graph incidence, the elementary link metric, the nonlinear comparison, replication, physical duration or a Yang–Mills continuum limit.
