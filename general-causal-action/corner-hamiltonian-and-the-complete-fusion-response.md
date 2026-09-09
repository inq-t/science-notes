# The Corner Hamiltonian and Its Complete Fusion Response

The exact joint seam response on the nine-link \(SU(2)\) corner remains negative after taking the temporal Hamiltonian limit. Complete Gauss recoupling gives \(\epsilon^3\partial_{g_1}^2\partial_{g_2}^2E_-=-299687/5885880\), including the interacting vacuum subtraction and disconnected perturbation terms. Five middle spin channels suffice for this coefficient. Its absolute magnitude is smaller than the calibrated Abelian result, but the reduction does not multiply independently across the two seams.

**Status: exact finite-graph Hamiltonian coefficient and changed-graph control.** This evaluates [[three-face-corner-and-the-leading-joint-energy|JL18]], using the complete carrier and raw incidences of [[three-face-corner-and-joint-seam-response|CJ1–5]]. It does not identify the chosen odd-sector energy with the global gap at nonzero seams or establish spatially uniform rigidity.

## The physical strength and carrier remain fixed

Retain the oriented words
\[
U=apb^{-1},\qquad V=aqc^{-1},\qquad W=brc^{-1},
\qquad F=\chi_{1/2}(U),\quad G=\chi_{1/2}(V),\quad H=\chi_{1/2}(W).
\tag{CH1}
\]
The axes \(a,b,c\) have one raw link each; \(p,q,r\) have two each. Haar probability and joint Gauss projection give \(L^2(SU(2)^3)^{\mathrm{Ad}SU(2)}\). In particular, \(\|F\|=\|G\|=\|H\|=1\); no separate class-function projection is made.

With the fundamental kinetic rate \(\epsilon>0\) held fixed, the Hamiltonian is
\[
\mathsf H(\mathbf g)=\mathsf H_0+g_1(2-G)+g_2(2-H),\qquad
\mathsf H_0=\frac{4\epsilon}{3}
\left(C_a+C_b+C_c+2C_p+2C_q+2C_r\right).
\tag{CH2}
\]
This is [[strong-coupling-gap-and-continuum-crossover/wilson-to-hamiltonian-vacuum-limit|the Wilson weak-step return]] under \(t=e^{-\epsilon a_t}\), \(s_i=a_tg_i\), not a newly fitted clock. The free vacuum is \(1\). In the complete sector odd under a center flip on a \(p\)-link, the lowest energy is \(4\epsilon\), simple, with vector \(F\): the shortest half-integer cycle through that link is uniquely its four-link face, and every extra or higher label raises the Casimir sum. The free operator has compact resolvent and the character potentials are bounded. Thus both isolated eigenbranches are analytic near \(\mathbf g=0\); their difference is the actual vacuum-subtracted sector energy \(E_-(\mathbf g)\).

Separate \(q\)- and \(r\)-link center flips make this excitation energy even in each strength. Put \(\epsilon=1\) during the calculation. Each fourth-order energy coefficient scales back as \(\epsilon^{-3}\). The scalar \(2(g_1+g_2)\) shifts both branches equally and has no quartic derivative.

## The complete fourth-order expression

For seed \(f=1\) or \(F\), let \(e_0=0\) or \(4\), and define, within its conserved sector,
\[
Q=I-|f\rangle\langle f|,\qquad
R=Q(\mathsf H_0-e_0)^{-1}Q,\qquad
u=RGf,\quad v=RHf,\quad
a=\langle Gf,u\rangle,\quad b=\|u\|^2.
\tag{CH3}
\]
The inverse here is the ordinary reduced resolvent used to evaluate an isolated perturbation coefficient; it is not a proposed bounded reconstruction of the physical gap. Seam exchange gives the same \(a,b\) for \(H\). Parity kills the mixed second-order terms. If \(e_{22}\) denotes the ordinary coefficient of \(g_1^2g_2^2\) in this branch's eigenenergy, then
\[
\boxed{
e_{22}=-2\langle QGu,RQHv\rangle
-\langle w,Rw\rangle+2ab,\qquad
w=Q(Hu+Gv).}
\tag{CH4}
\]
Indeed the fourth-order chain is minus the squared \(R^{1/2}\)-norm of \(Q(g_1G+g_2H)R(g_1G+g_2H)f\). Its mixed coefficient gives the first two terms. The product of the second-order resolvent and squared-resolvent expectations contributes \(2ab\). Equivalently, [[quartic-seam-eigenvalues-and-the-generalized-pencil|the normalized eigenvector recurrence]] produces (CH4). The derivative is \(2!2!e_{22}=4e_{22}\).

For both seeds the first term is exactly zero. After \(G\) is applied twice, the \(q\)-spin is \(0\) or \(1\), while the \(r\)-spin remains zero. The zero-\(q\) component is only the seed, by the trivalent Gauss conditions, so \(QGu\) has \(q=1,r=0\). Similarly \(QHv\) has \(q=0,r=1\). The diagonal free resolvent preserves these orthogonal labels.

## The odd branch returns five middle channels

Write
\[
L_G=\chi_{1/2}(UV^{-1}),\qquad L_H=\chi_{1/2}(UW).
\]
The single-seam fusion weights are \(1/4,3/4\), with gaps \(2,14/3\) above \(F\). They give
\[
u=\frac{3}{14}FG+\frac17L_G,\qquad
v=\frac{3}{14}FH+\frac17L_H,\qquad
a=\frac27,\quad b=\frac{19}{196},\quad 2ab=\frac{19}{343}.
\tag{CH5}
\]
These are the Hamiltonian versions of [[adjacent-wilson-plaquette-and-the-chronological-surplus|the complete adjacent-face fusion]], with the same unit-norm character convention.

Set
\[
T=FGH,\quad A=HL_G,\quad B=GL_H,\quad
C=F\chi_{1/2}(VW^{-1}),\quad
D=\chi_{1/2}(UWV^{-1}).
\tag{CH6}
\]
The word \(D\) is the exterior six-link triangle: the axis matrices cancel without commuting any group elements. All five vectors have norm one. Independent Haar integration of \(U,V,W\), using fundamental matrix orthogonality, gives
\[
\langle D,T\rangle=\frac14,\qquad
\langle D,A\rangle=\langle D,B\rangle=\langle D,C\rangle=\frac12,
\]
\[
\langle A,T\rangle=\langle B,T\rangle=\langle C,T\rangle=\frac12.
\tag{CH7}
\]
For example, integrating \(\chi(U)\chi(UV^{-1})\) over \(U\) gives \(\chi(V)/2\); a second such contraction gives the \(1/4\) exterior-triangle coefficient. These are normalized Schur contractions, with their existing [[interacting-vacuum-support-at-the-balanced-cut|intertwiner interpretation]].

After one insertion of each seam, \(p,q,r\) all have spin \(1/2\); each axis has spin \(0\) or \(1\). Joint Gauss invariance permits exactly
\[
(j_a,j_b,j_c)=(0,0,0),(0,1,1),(1,0,1),(1,1,0),(1,1,1).
\tag{CH8}
\]
There is one normalized spin network per triple. Choose their phases so that \(D=\psi_{000}\) and
\[
A=\frac12D+\frac{\sqrt3}{2}\psi_{011},\quad
B=\frac12D+\frac{\sqrt3}{2}\psi_{101},\quad
C=\frac12D+\frac{\sqrt3}{2}\psi_{110}.
\]
Each identity follows from the corresponding axis cancellation and (CH7). The remaining projection and \(\|T\|=1\) then give
\[
T=\frac14D+\frac{\sqrt3}{4}
(\psi_{011}+\psi_{101}+\psi_{110})
+\frac{\sqrt6}{4}\psi_{111}.
\tag{CH9}
\]
Thus this computation retains the spin-one and relative-orientation channels omitted by a three-character carrier.

Equation (CH5) yields \(w=(3T+A+B)/7\). The complete middle spectral data are

| Axis spins | Squared coefficient of \(w\) | Gap above \(F\) |
| --- | ---: | ---: |
| \(000\) | \(49/784\) | \(2\) |
| \(011\) | \(75/784\) | \(22/3\) |
| \(101\) | \(75/784\) | \(22/3\) |
| \(110\) | \(27/784\) | \(22/3\) |
| \(111\) | \(54/784\) | \(10\) |

The weights sum to \(5/14=\|w\|^2\). The exterior paths contribute free energy \(6\); the axis Casimirs supply the remaining entries. Consequently
\[
\langle w,Rw\rangle
=\frac1{32}+\frac{531}{17248}+\frac{27}{3920}
=\frac{743}{10780},
\]
\[
\boxed{e_{-,22}=\frac{19}{343}-\frac{743}{10780}
=-\frac{1021}{75460}.}
\tag{CH10}
\]
No omitted spin can contribute to this coefficient: every four-insertion chain is contained in (CH4), its same-seam cross term vanishes exactly, and its mixed middle vector is exhausted by (CH8). The first and last steps use precisely (CH5). This is the coefficient of the full analytic branch, not a numerical truncation.

## Vacuum and disconnected terms change the answer

For the true vacuum seed, \(u=G/4,\ v=H/4\), so
\[
a_\Omega=\frac14,\qquad b_\Omega=\frac1{16},\qquad
w_\Omega=\frac12GH.
\]
The product \(GH\) has singlet/triplet weights \(1/4,3/4\) on the shared axis, with energies \(6,26/3\). Therefore
\[
\langle w_\Omega,R_\Omega w_\Omega\rangle
=\frac14\left(\frac{1/4}{6}+\frac{3/4}{26/3}\right)
=\frac5{156},\qquad
e_{\Omega,22}=\frac1{32}-\frac5{156}=-\frac1{1248}.
\tag{CH11}
\]
Restoring the physical kinetic rate gives the evaluated target
\[
\boxed{
\mathcal J_{SU(2)}
=\epsilon^3\partial_{g_1}^2\partial_{g_2}^2E_-(0,0)
=4\left(-\frac{1021}{75460}+\frac1{1248}\right)
=-\frac{299687}{5885880}.}
\tag{CH12}
\]
Both the vacuum and the disconnected terms are indispensable. The corresponding single-seam excitation derivative is \(2(-2/7+1/4)/\epsilon=-1/(14\epsilon)\).

## Splitting the shared seam edge removes this coefficient

As a changed-graph control, split \(Z\) into two vertices, ending \(q\) at one and \(r\) at the other, and replace the common \(c\)-edge by their separate one-link connections to \(O\). Keep all other lengths and kinetic rates. The spin joining those two fundamentals at \(O\) remains a recoupling label, but its Casimir no longer replaces the sum of their two independent link Casimirs. The five middle weights in the table stay fixed; their gaps become
\[
\left(4,\frac{20}{3},\frac{20}{3},\frac{28}{3},\frac{28}{3}\right).
\]
Their weighted resolvent sum is \(19/343\), exactly cancelling the odd disconnected term. For the vacuum, the seam product now has energy \(8\), so \(\langle w_\Omega,R_\Omega w_\Omega\rangle=1/32\) cancels its disconnected term too:
\[
\boxed{\partial_{g_1}^2\partial_{g_2}^2E_-^{\rm split}(0,0)=0.}
\tag{CH13}
\]
This is a graph with ten raw links and two distinct seam edges; it is not a pure subdivision or a new gauge fixing of the nine-link corner. The calculation proves quartic cancellation, without asserting all-order factorization of the non-Abelian sector.

## What the calibrated comparison establishes

[[abelian-corner-and-the-joint-seam-energy|The Abelian Hamiltonian benchmark]] uses the same fundamental energy and unit-norm real seam sources, but its declared higher-charge heat law differs from the \(SU(2)\) Casimir law. Its value is \(-239/1080\), so the absolute response ratio is
\[
\frac{|\mathcal J_{SU(2)}|}{|\mathcal J_{U(1)}|}
=\frac{2697183}{11722711}<1.
\tag{CH14}
\]
Complete Hamiltonian recoupling preserves an absolute reduction of this negative response. It does not preserve a product rule for reductions assigned independently to the two seams: [[corner-response-and-the-failure-of-multiplicative-attenuation|the locally normalized connected comparison]] is strictly larger for \(SU(2)\). Thus neither a positive joint-energy law nor simple multiplicative attenuation survives this corner test.

The actual mixed response depends on shared incidence, full fusion and the vacuum normalization together. The active [[oriented-innovation-and-finite-temporal-repair|oriented-innovation inequality]] still requires a uniform estimate for complete physical sources and composition, not the sign or size of a single finite coefficient. The full discrete temporal-coupling function and the spatial continuum and infinite-volume problems remain open.

The exact companion [spin-network receipt](receipts/corner_hamiltonian_spin_receipt.py) computes the oriented Wigner–Clebsch matrix elements independently of the five-channel projection argument, checks symmetry and the single-seam controls, and reproduces (CH10–12) by a separate normalized eigenvector recurrence. [[corner-hamiltonian-invariant-polynomials|The independent invariant-polynomial method]] derives the raw Casimir action and the same coefficient without Clebsch phases. Both use exact arithmetic and do not approximate the spectrum numerically.
