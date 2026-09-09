# Three Faces at a Corner and Their Joint Seam Response

Three orthogonal plaquette faces meeting at one cubic corner give a finite test of genuinely overlapping seam response. Each added face shares an edge with the source face, and the two added faces share a third edge. The first possible joint response is fourth order by exact center symmetries. Both the complete source-face odd-sector energy and a fixed source's normalized surplus can be differentiated in finitely many exact spin sectors, without replacing the shared-edge Gauss law or resetting a compressed path kernel. The linked calculation proves negative joint coefficients at small temporal coupling; their complete dependence on that coupling remains open.

**Status: exact finite graph, symmetry and perturbative closure; evaluated small-coupling joint response; open full coefficient and physical-limit estimate.** [[adjacent-wilson-plaquette-and-the-chronological-surplus|The adjacent-plaquette calculation]] shows that an improving source quotient can coexist with a decreasing physical gap. This test keeps the complete relevant sector alongside that quotient. [[three-face-corner-and-the-leading-joint-energy|The leading joint-energy calculation]] owns the controlled evaluation. Its three-dimensional spatial incidence differs from [[three-cell-incidence-and-shared-path-motion|the three-cell row]].

## The raw corner reduces to a tetrahedral graph

Use the seven vertices \(O,X,Y,Z,XY,XZ,YZ\), at the corresponding corners of three unit coordinate faces. There are nine raw links: the three axes \(OX,OY,OZ\), and the two exterior links on each of the \(xy,xz,yz\) faces. Orient the axes away from \(O\). The exterior two-link paths run from \(X\) to \(Y\), \(X\) to \(Z\), and \(Y\) to \(Z\):
\[
a:O\to X,\quad b:O\to Y,\quad c:O\to Z,\qquad
p:X\to Y,\quad q:X\to Z,\quad r:Y\to Z.
\tag{CJ1}
\]
The axis paths have length one; \(p,q,r\) each have length two. Eliminating only the three bivalent exterior vertices gives the graph \(K_4\) on \(O,X,Y,Z\). The raw cycle rank is \(9-7+1=3\). Its based face words are
\[
U=apb^{-1},\qquad V=aqc^{-1},\qquad W=brc^{-1}.
\tag{CJ2}
\]
Thus \(U,V\) share \(a\), \(U,W\) share \(b\), and the seams \(V,W\) share \(c\), which is absent from \(U\). The order and inverses in these words are retained.

Joint Gauss reduction using the three axis paths gives
\[
\mathcal H_{\rm phys}=L^2(SU(2)^3,dU\,dV\,dW)^{\operatorname{Ad}SU(2)}.
\tag{CJ3}
\]
Haar invariance proves the product measure before the remaining simultaneous conjugation. This is not a product of three class-function carriers. In particular, separate face characters omit physical relative orientations.

Fix the actual Wilson temporal coupling \(b_t>0\) and duration \(a_t>0\). Put
\[
\tau_j=\frac{I_{2j+1}(2b_t)}{I_1(2b_t)},\qquad t=\tau_{1/2},
\qquad 1=\tau_0>t>\tau_1>\cdots>0.
\]
The normalized free transfer is the CM product-link Wilson convolution followed by the joint Gauss projection. In the normalized tetrahedral spin-network basis it has eigenvalues
\[
\boxed{\theta_{\mathbf j}
=\tau_{j_a}\tau_{j_b}\tau_{j_c}
 \tau_{\ell_p}^{\,2}\tau_{\ell_q}^{\,2}\tau_{\ell_r}^{\,2}.}
\tag{CJ4}
\]
At the four retained vertices impose the admissible triples
\[
(j_a,j_b,j_c),\quad(j_a,\ell_p,\ell_q),\quad
(j_b,\ell_p,\ell_r),\quad(j_c,\ell_q,\ell_r).
\tag{CJ5}
\]
Every admissible \(SU(2)\) trivalent intertwiner is unique up to normalization. The integer-sum and triangle conditions are part of the carrier. The squares in (CJ4) come from composing the two original link kernels; they are not a newly chosen one-link Wilson kernel. [[interacting-vacuum-support-at-the-balanced-cut|The normalized intertwiner construction]] and [[library/spin-network-states-in-gauge-theory/inq|spin-network states]] supply the existing basis conventions.

## Two seams leave the fixed source norm unchanged

Take the fundamental source and the two nonnegative seam potentials
\[
F=\chi_{1/2}(U),\qquad
G_1=\chi_{1/2}(V),\quad G_2=\chi_{1/2}(W),\qquad
V_i=2-G_i.
\]
With \(P_0\) the transfer in (CJ4), define the same spatial sandwich as SV:
\[
T_{\mathbf s}
=e^{-(s_1V_1+s_2V_2)/2}P_0
 e^{-(s_1V_1+s_2V_2)/2},\qquad
T_{\mathbf s}\psi_{\mathbf s}=\lambda_{\mathbf s}\psi_{\mathbf s},
\]
\[
P_{\mathbf s}h=\frac{T_{\mathbf s}(\psi_{\mathbf s}h)}
 {\lambda_{\mathbf s}\psi_{\mathbf s}},\qquad
d\pi_{\mathbf s}=\psi_{\mathbf s}^2dU_{\rm raw},\qquad
\int\psi_{\mathbf s}^2=1.
\tag{CJ6}
\]
The original one-link scalar factors can be retained throughout; their common product cancels from normalized transitions and energy ratios. The factors from the constant part of \(V_i\) remain in \(\lambda_{\mathbf s}\). No clock changes with \(\mathbf s\).

Gauge-invariant functions of the seven-edge union of the two seam faces form an invariant subspace of both the free transfer and the seam multiplications. Its positive Perron vector lifts to a positive eigenvector of the full transfer, hence is the actual \(\psi_{\mathbf s}\). It is independent of the two \(xy\)-exclusive raw links in \(p\). Conditional Haar integration of their product therefore gives
\[
\boxed{\pi_{\mathbf s}F=0,\qquad \pi_{\mathbf s}(F^2)=1}
\tag{CJ7}
\]
for every finite real seam pair. This does not assert a product vacuum across the shared seam edge or a closed chronological source algebra.

## Center parity selects a fourth-order joint test

Let \(C_i\) multiply one exclusive exterior raw link of seam face \(i\) by \(-I\). Its action at every temporal slice preserves all free temporal plaquettes, fixes \(F\) and the other seam character, and sends \(G_i\) to \(-G_i\). Consequently
\[
C_iT_{(s_i,s_j)}C_i^{-1}
=e^{-4s_i}T_{(-s_i,s_j)}.
\tag{CJ8}
\]
The scalar cancels from the ground-state transition and excitation energies. Every fixed-\(F\) chronological moment, and its normalized innovation quotient, is therefore even in each seam variable separately.

For the spectral comparison, let \(C_0\) flip one \(xy\)-exclusive raw link. Both seam potentials commute with \(C_0\), the vacuum is even, and \(F\) is odd. Retain the entire gauge-invariant sector
\[
\mathcal H_-=\{h\in\mathcal H_{\rm phys}:C_0h=-h\}.
\]
Its largest free eigenvalue is \(\alpha=t^4\), simple, with eigenfunction \(F\). Indeed the half-integer edge support of an invariant spin network has even incidence at every vertex. A marked half-integer edge thus lies on a closed half-integer cycle. The unique length-four cycle containing either \(xy\)-exclusive edge is the \(xy\) face. Four fundamental labels on that cycle attain \(t^4\); any additional nontrivial edge or higher label decreases the multiplier. Compactness isolates this simple eigenvalue from the rest of \(\mathcal H_-\).

Let \(\lambda_-(\mathbf s)\) be its analytic continuation, which remains the largest eigenvalue on the complete odd sector near zero. Define
\[
E_-(\mathbf s)=-a_t^{-1}
 \log\frac{\lambda_-(\mathbf s)}{\lambda_{\mathbf s}}.
\tag{CJ9}
\]
It is separately even by (CJ8). This energy controls the infimum of the normalized \(k\)-slab innovation quotient on \(\mathcal H_-\):
\(1-e^{-2ka_tE_-(\mathbf s)}\). It is not asserted to equal the full physical gap outside that sector.

Separately, set
\[
C_n(\mathbf s)=\langle F,P_{\mathbf s}^nF\rangle_{\pi_{\mathbf s}},
\qquad
\mathfrak c_k(F;\mathbf s)=
\frac{1-2C_{2k}(\mathbf s)+C_{4k}(\mathbf s)}
     {1-C_{2k}(\mathbf s)}.
\tag{CJ10}
\]
For either \(R=E_-\) or \(R=\mathfrak c_k(F;\cdot)\), remove the two single-seam responses:
\[
R_{\rm joint}(s_1,s_2)
=R(s_1,s_2)-R(s_1,0)-R(0,s_2)+R(0,0).
\]
Analyticity and separate evenness give
\[
\boxed{
R_{\rm joint}(s_1,s_2)
=\frac{s_1^2s_2^2}{4}
 \left.\partial_{s_1}^2\partial_{s_2}^2R\right|_{\mathbf0}
+O\!\left(s_1^2s_2^2(s_1^2+s_2^2)\right).}
\tag{CJ11}
\]
Fourth order is the first permitted joint order. Symmetry alone permits a zero coefficient. [[three-face-corner-and-the-leading-joint-energy|JL13–17]] now proves nonzero negative coefficients for both quantities at sufficiently small temporal coupling, retaining the actual vacuum and the complete source-face odd sector.

## The coefficient closes in exact finite spin sectors

At the coefficient with two insertions of each seam, fundamental multiplication changes the spin on each visited edge by at most \(1/2\) per insertion. Starting from the odd eigenfunction \(F\), all required intermediate spin networks lie within
\[
j_a,j_b\le\frac32,\qquad j_c\le2,\qquad
\ell_p=\frac12,\qquad \ell_q,\ell_r\le1.
\tag{CJ12}
\]
For vacuum derivatives, the corresponding bounds are
\[
j_a,j_b\le1,\qquad j_c\le2,\qquad
\ell_p=0,\qquad \ell_q,\ell_r\le1.
\tag{CJ13}
\]
In both sets impose every Gauss condition in (CJ5). Seam multiplication never acts on \(p\), so its spin remains fixed.

Free powers and reduced resolvents preserve these labels. Vacuum perturbation uses the inverse of \(1-P_0\) off constants; odd-sector perturbation uses the inverse of \(\alpha-P_0\) off \(F\). Their entries on the finite sets are the explicit nonzero eigenvalue denominators from (CJ4). Matrix elements are finite \(SU(2)\) Clebsch or \(6j\) recouplings. Differentiating a fixed finite history and both vacuum caps to order \((2,2)\) uses the same bounds. These are exact perturbative closures of the full isolated branches, not spectral cutoffs used to approximate the undeformed infinite-dimensional theory.

The energy coefficient must remove disconnected and vacuum responses as well. Write
\[
B_{\mathbf s}=e^{(s_1G_1+s_2G_2)/2}P_0
e^{(s_1G_1+s_2G_2)/2},\qquad
T_{\mathbf s}=e^{-2(s_1+s_2)}B_{\mathbf s}.
\]
Let \(\Lambda_-,\Lambda_\Omega\) be the separately even odd-sector and vacuum eigenvalues of \(B_{\mathbf s}\), with values \(\alpha,1\) at zero. Denote their derivatives there by \(\Lambda_{\bullet,ij}=\partial_1^i\partial_2^j\Lambda_\bullet(0,0)\). Then
\[
\boxed{
\partial_1^2\partial_2^2E_-(0,0)
=-\frac1{a_t}\left[
\frac{\Lambda_{-,22}}{\alpha}
-\frac{\Lambda_{-,20}\Lambda_{-,02}}{\alpha^2}
-\Lambda_{\Omega,22}
+\Lambda_{\Omega,20}\Lambda_{\Omega,02}\right].}
\tag{CJ14}
\]
This follows from \(\partial_{22}\log\Lambda
=\Lambda_{22}/\Lambda(0)-\Lambda_{20}\Lambda_{02}/\Lambda(0)^2\), since the odd derivatives and \(\Lambda_{11}\) vanish. Omitting the vacuum branch or the product of the two second derivatives changes the joint energy coefficient.

[[three-face-corner-and-the-leading-joint-energy|The evaluated corner response]] gives
\[
\partial_1^2\partial_2^2E_-(0,0)
=-\frac{t^2}{4a_t}+O(t^4/a_t),
\qquad
\partial_1^2\partial_2^2\mathfrak c_k(F;0,0)
=-\frac{k}{2}t^{8k+2}+O(t^{8k+4}),
\]
where \(t=\tau_{1/2}\downarrow0\), and \(a_t,k\) are fixed. Its operator remainder controls every omitted spin, so this is a derivative of the full transfer. [[abelian-corner-and-the-joint-seam-energy|The calibrated Abelian control]] also has a negative joint energy; duplicating its shared seam edge removes that connected energy exactly. Nonzero joint response alone therefore detects shared incidence without selecting a non-Abelian mechanism.

The next coefficient calculation takes the matched temporal Hamiltonian limit, using the same raw-link kinetic normalization and physical seam strengths. [[quartic-seam-eigenvalues-and-the-generalized-pencil|The exact generalized-pencil recurrence]] retains all quartic normalization contacts. The \(SU(2)\) coefficient away from the small-\(t\) regime, including its Hamiltonian limit, remains open. No uniform spatial, continuum or mass-gap conclusion follows from the finite result.
