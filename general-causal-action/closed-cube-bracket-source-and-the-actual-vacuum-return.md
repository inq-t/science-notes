# Closed Cube Bracket Sources in the Actual Vacuum

The ordered sixth face leaves a signed joint response in the cube's actual ground state, with coefficients fixed by the original edge kinetics. A bounded bracket mark has a strictly positive leading mean, but its centered chronological carrier reaches the ordinary lowest neutral oscillator level. The first closed-cell bracket signal therefore supplies an observable relation; it does not create an additional spectral floor.

**Status: proved fixed-cube compact source and chronological return, with a harmonic source-support calculation.** The group, preparation, graph, coupling and clock are fixed inputs. [[closed-cube-raw-edge-kinetic-sewing|CK]] owns the exact kinetic operator and oscillator, and [[closed-cube-dependent-face-and-oriented-source-jet|CD]] owns the word expansion and Gaussian contractions. The argument extends the local-well method of [[fixed-group-compact-vacuum-and-oriented-source-return|GV]] to this dependent-face potential; it does not use the magnetic likelihood as a vacuum.

## Retain the original Hamiltonian and marked words

Use [[weighted-character-scale-and-bounded-lie-sources|GM's]] fixed compact connected \(G\) with simple Lie algebra, invariant metric \(Q\), faithful representation \(\rho\), and positive commuting weight \(A\). Write \(d=\dim\mathfrak g\), and retain all twelve raw edges and six CW faces:
\[
\widehat H_h=H/E
=h^2\mathsf C_{\rm raw,Q}+h^{-2}V,\qquad
V=\sum_{j=1}^6\frac{W_A(F_j)}{2I_A},\qquad
h=\left(\frac{\kappa}{2I_Ag}\right)^{1/4},\quad
E=\kappa h^{-2}.
\tag{CQ1}
\]
The cover is \(G^5\) with product Haar; the physical carrier is its simultaneous conjugation-invariant subspace.

For the actual based words \(F_6=v^{-1}w^{-1}xuy\), put
\[
\begin{aligned}
(\zeta_1,\ldots,\zeta_5)
&=(-q_\rho(v),-q_\rho(w),q_\rho(x),q_\rho(u),q_\rho(y)),\\
R&=2q_\rho(F_6)-2\sum_i\zeta_i,\\
M_{ij}&=Q(R,4[\zeta_i,\zeta_j])\quad(i<j),\\
M_*&=Q\left(R,2\sum_{i<j}[\zeta_i,\zeta_j]\right)
=\frac12\sum_{i<j}M_{ij}.
\end{aligned}
\tag{CQ2}
\]
The \(M_{ij}\) and \(M_*\) are bounded, real, gauge-invariant scalar marks. They vanish identically after Abelianization because their second factor is a Lie bracket. The closure defect \(R\) alone need not vanish on a compact Abelian group: GM's nonlinear \(q_\rho\) is not an additive logarithm.

In the scaled chart \((u,v,w,x,y)=\exp(h(U,V_1,W,X,Y))\), define
\[
(Z_1,\ldots,Z_5)=(-V_1,-W,X,U,Y),\qquad
B_{\rm br}(Z)=\frac12\sum_{i<j}[Z_i,Z_j].
\]
CD's exact Taylor calculation gives
\[
\frac{R}{h^2}\longrightarrow B_{\rm br},\qquad
\frac{M_{ij}}{h^4}\longrightarrow
P_{ij}=Q(B_{\rm br},[Z_i,Z_j]),\qquad
\frac{M_*}{h^4}\longrightarrow P=|B_{\rm br}|_Q^2.
\tag{CQ3}
\]
The factor two in \(R\) is essential for these normalizations. The marks were fixed before taking the limit.

## The finite compact vacuum supplies the Gaussian law

Let \(A_5\) be CK's raw incidence matrix and
\[
l=(1,-1,-1,1,1)^{\mathsf T},\qquad G_5=I+ll^{\mathsf T}.
\]
The leading operator on \(\mathfrak g^5\) is
\[
\mathcal O=-\partial^{\mathsf T}(A_5\otimes I_d)\partial
+\frac14 X_{\rm f}^{\mathsf T}(G_5\otimes I_d)X_{\rm f},
\qquad X_{\rm f}=(U,V_1,W,X,Y).
\tag{CQ4}
\]
Choose an orthogonal \(O\) diagonalizing
\(G_5^{1/2}A_5G_5^{1/2}\), and set \(X_{\rm f}=G_5^{-1/2}O\,Y_{\rm m}\).
The five independent color-vector modes have
\[
\omega=(2,2,2,\sqrt6,\sqrt6),\qquad
\Omega=C\exp\left[-\sum_r\frac{|Y_{{\rm m},r}|_Q^2}{4\omega_r}\right],
\qquad e_0=d(3+\sqrt6).
\tag{CQ5}
\]
Their probability covariances are \(\omega_r Q^{-1}\). Equivalently the face covariance \(\Sigma\) satisfies
\(\Sigma G_5\Sigma=A_5\). A product of five independently chosen rotors would give a different law.

Here the fixed-cube compact return can be proved directly. The five chord Casimirs already control every chord derivative; their smooth Haar-preserving change to face variables preserves uniform cover ellipticity. The other seven raw-edge forms are nonnegative. The cost \(V\) has its unique zero at the identity tuple, since the first five faithful face costs already do, and CQ4 has a positive Hessian. Positivity on the connected compact cover gives a simple positive vacuum \(v_h\), which is automatically gauge invariant.

Use invariant localization cutoffs at radius \(\delta_h=h^\alpha\), \(0<\alpha<1\). Their kinetic cost is \(O(h^2/\delta_h^2)=o(1)\), while the exterior potential is at least \(c\delta_h^2/h^2\to\infty\). Inside, coefficient and potential form errors relative to CQ4 tend to zero. The min–max argument with cutoff oscillator states therefore returns every fixed low eigenvalue and spectral cluster, including multiplicities. The cutoffs and charts commute with conjugation, so the argument also holds on the full physical invariant carrier.

In particular, for \(K_h=\widehat H_h-\lambda_0(h)\) and \(K_0=\mathcal O-e_0\),
\[
\lambda_0(h)\to e_0,\qquad
\operatorname{gap}(K_h|_{\rm phys})\to4.
\tag{CQ6}
\]
There is no invariant one-quantum vector for a simple Lie algebra. A radial quadratic in any frequency-two mode is invariant and has energy four. This proves the harmonic physical gap used in CQ6; no separate class-function restriction is imposed.

The energy-four cluster has rank six, from the symmetric pairings of the three slow modes. The next physical level is \(2+\sqrt6>4\). Cluster return retains that degeneracy; it does not require a simple first excited eigenvalue.

## Source multiplication is justified before chronology

Let \(\mathcal J_h\) be the equivariant cutoff dilation with the actual Haar half-density, now in dimension \(5d\). For each fixed polynomial Gaussian, the full operator has arbitrarily long differential Taylor expansions on this chart. The sixth-face cost can have an odd cubic term: it is retained among those coefficients, together with the raw kinetic jets. No even-potential simplification from the planar chart is used.

The vacuum recursion is algebraic on polynomial Gaussians: invert \(K_0\) off its simple vacuum and normalize at each order. Every input polynomial has finite Hermite expansion. A normalized fifth-order quasimode \(q_h\) has residual \(O(h^6)\); the fixed cover gap and positive overlap give
\[
\|v_h-q_h\|=O(h^6),\qquad
q_h=\mathcal J_h\left(\Omega+\sum_{j=1}^5h^j\psi_j\right)
+O(h^6)
\tag{CQ7}
\]
with normalization understood in the second expression. Each \(\psi_j\) is a fixed polynomial Gaussian. Constants may depend on all fixed group and preparation data.

Every original \(M_{ij}\) and \(M_*\) is globally bounded. Thus multiplying CQ7's error by its normalized source \(h^{-4}M\) costs at most \(Ch^{-4}\), leaving \(O(h^2)\). On the quasimode, Taylor expansion in CQ3 and Gaussian moments give the sharper leading vector comparison
\[
\left\|h^{-4}M_*v_h-\mathcal J_h(P\Omega)\right\|=O(h),
\qquad
\left\|h^{-4}M_{ij}v_h-\mathcal J_h(P_{ij}\Omega)\right\|=O(h).
\tag{CQ8}
\]
Chart-exterior and cutoff errors are smaller than any fixed power. This pays for the growing source normalization using actual-vacuum accuracy, not an assumed limiting probability density.

Set
\[
F_Q=\sum_{a,b,c}Q(e_a,[e_b,e_c])^2=d\,C_{\rm ad}>0.
\]
CD's Wick contractions with CK's covariance now become actual expectations:
\[
\boxed{\quad
h^{-4}\mathbb E_{v_h^2}M_*
=F_Q\left(2+\frac{2\sqrt6}{3}\right)+O(h).\quad}
\tag{CQ9}
\]
For example the pairwise channels have opposite signs,
\[
h^{-4}\mathbb E M_{12}
=F_Q\left(1+\frac{\sqrt6}{6}\right)+O(h),\qquad
h^{-4}\mathbb E M_{15}
=F_Q\left(-1+\frac{\sqrt6}{6}\right)+O(h).
\tag{CQ10}
\]
All ten coefficients are owned by CD. These are signed joint source expectations, not second derivatives of an energy or positive contributions to a Hamiltonian. They are unchanged by a coordinate change that faithfully transports the original words, marks and dynamics.

## The centered bracket mark reaches the lowest neutral level

Let \(J_{ij}=1\) for \(i<j\), \(J_{ij}=-1\) for \(i>j\), and \(J_{ii}=0\). The invertible real change \(Z=L Y_{\rm m}\) gives
\[
b=L^{\mathsf T}JL,\qquad
B_{\rm br}=\frac12\sum_{r<s}b_{rs}[Y_{{\rm m},r},Y_{{\rm m},s}].
\tag{CQ11}
\]
The antisymmetric \(5\times5\) matrix \(J\) has rank four: its leading \(4\times4\) Pfaffian is \(1-1+1=1\), and every odd-dimensional antisymmetric matrix is singular. Hence \(\dim\ker b=1\).

Write \(Y_r=Y_{{\rm m},r}\) in the following Wick identity. The degree-two Hermite part of \(P=|B_{\rm br}|^2\) is
\[
P^{[2]}
=\frac{C_{\rm ad}}4\sum_{r,t}
\left(\sum_s b_{rs}b_{ts}\omega_s\right)
\left(Q(Y_r,Y_t)-\delta_{rt}d\omega_r\right).
\tag{CQ12}
\]
This follows by contracting one pair of color vectors in the two brackets and using
\(\sum_{a,c}f_{abc}f_{ab'c}=C_{\rm ad}\delta_{bb'}\).
The constant part is the mean and the remaining part has Hermite degree four.

For a slow mode \(r\le3\), the coefficient of
\(|Y_r|^2-d\omega_r\) is
\[
a_r=\frac{C_{\rm ad}}4\sum_s b_{rs}^2\omega_s\ge0.
\]
They cannot all vanish: that would place a three-dimensional slow space inside the one-dimensional kernel of \(b\). Thus
\[
\boxed{\quad
\mathbf1_{\{4\}}(K_0)(P-\mathbb E_\Omega P)\Omega\ne0.\quad}
\tag{CQ13}
\]
The centered mark has both degree-two and degree-four content; subtracting its mean does not Wick-order it to pure degree four. Since no physical energy lies in \((0,4)\), its exact harmonic cyclic spectral edge is four.

## Return the centered two-point chronology in the original clock

Put
\[
f_h=(h^{-4}M_*-\mathbb E h^{-4}M_*)v_h,\qquad
f_0=(P-\mathbb E_\Omega P)\Omega.
\]
The vector comparison CQ8 returns \(f_h\) to \(f_0\). For completeness, let
\(I_h=Q_h\mathcal J_hQ_0\), with \(Q_h,Q_0\) the actual and harmonic vacuum-complement projections. On any fixed Hermite-degree space,
\[
\|(K_hI_h-I_hK_0)u\|\le Ch\|u\|,\qquad
\|f_h-I_hf_0\|\le Ch.
\tag{CQ14}
\]
The first bound follows from the full local jet and
\(|\lambda_0(h)-e_0|=O(h)\); the latter follows already from the leading vacuum quasimode and its separated cluster. Both centered generators have a fixed positive lower bound for small \(h\). Applying the two-sided decaying Duhamel argument of [[centered-compact-chronology-and-integrable-source-return|CC]] therefore gives
\[
\boxed{\quad
\left|\langle f_h,e^{-sK_h}f_h\rangle
-\langle f_0,e^{-sK_0}f_0\rangle\right|
\le Ch(1+s)e^{-cs},\qquad s\ge0.\quad}
\tag{CQ15}
\]
It also gives an \(O(h)\) absolute time-integral error. The limiting profile is a finite positive sum of exponentials from the degree-two and degree-four Hermite sectors, with strictly positive weight at energy four. It is the actual marked transfer limit.

CQ13, first-cluster convergence and CQ8 imply that the actual source has nonzero weight in \((4-\epsilon,4+\epsilon)\) for every fixed \(\epsilon>0\) and sufficiently small \(h\). CQ6 bounds its support below. Consequently its actual cyclic edge \(\lambda_{f_h}\) tends to four. Using [[two-slice-innovation-geometry/chronological-cyclic-sources-and-the-innovation-floor|CS's cyclic identity]],
\[
\inf_{0\ne u\in\mathscr C_{f_h}}
\frac{\langle u,(1-e^{-2aK_h})^2u\rangle}
{\langle u,(1-e^{-2aK_h})u\rangle}
=1-e^{-2a\lambda_{f_h}}
\longrightarrow1-e^{-8a}.
\tag{CQ16}
\]
This includes the complete chronological carrier, not only the original mark. It does not assert an exact finite-\(h\) eigenvalue or a gap correction coefficient.

After Abelianization the bracket mark itself is zero, so its normalized cyclic quotient is undefined. The full Abelian Gauss carrier also admits one-quantum states; its even radial sector supplies a separate spectral comparison. Neither change is an extra mass mechanism.

The parameter \(a\) is scaled duration. Physical duration is \(a/E\); at a fixed physical duration the generator is \(E K_h\). All conclusions here concern one fixed cube as confinement grows. They do not determine a continuum trajectory or a uniform bound on growing complexes.

The test therefore forces a non-Abelian marked relation and decides its finite chronological support. The positive aggregate in CQ9 reaches an already present neutral level. A claim of additional rigidity requires shared-cell composition with the inherited exterior and actual vacuum caps retained. The cube boundary itself can also be a spherical cellulation with the identical Hamiltonian and every identical sourced history; ambient bulk dimension has not been supplied by this calculation.
