# Planar Confinement Has a Spatially Soft Physical Mode

On an isolated open \(L\times L\) square patch with every vertex gauged, the complete strong-confinement gap has leading coefficient \(2\sqrt{4-4\cos(\pi/(L+1))}\) in units of \(\sqrt{\kappa g}\). That coefficient tends to zero as the patch grows. The lowest allowed oscillator excitation is a neutral pair in the softest spatial mode, with an explicit normalized scalar source. This disproves a positive size-independent harmonic coefficient for this family; it does not establish a vanishing absolute gap at fixed coupling.

**Status: exact incidence spectrum and proved fixed-patch physical gap asymptotic.** [[gauge-cycle-innovation-filtration/inq|The gauge-cycle construction]] fixes the complete tree-gauge carrier and the role of boundary Gauss constraints. [[gauge-cycle-innovation-filtration/loop-coordinates-and-the-induced-clock|The induced-clock analysis]] requires preserving the shared-edge kinetic terms. [[corner-fast-vacuum-and-harmonic-separation|FH]] and [[three-face-confinement-and-the-coupling-path|CP]] supply the equivariant single-well comparison used below. This is an isolated planar spatial family, with its own specified vacuum.

## The patch has one magnetic minimum after full Gauss reduction

Let \(\Gamma_L\) have vertices \(\{0,\ldots,L\}^2\), horizontal and vertical nearest-neighbor links, and its \(N=L^2\) elementary square faces. The counts are
\[
|V_L|=(L+1)^2,\qquad |E_L|=2L(L+1),\qquad
|E_L|-|V_L|+1=L^2=N.
\tag{PP1}
\]
Choose an orientation for each raw edge and orient every face counterclockwise. Impose the full \(SU(2)\) gauge group at **every** vertex, including the open boundary. There are no external charges, fixed boundary links or retained boundary frames. The physical Hamiltonian is
\[
\mathsf H_{L,g}
=\kappa\sum_{e\in E_L}C_e
+g\sum_{p\in F_L}(2-\chi_{1/2}(P_p)),
\qquad \kappa>0,\quad g>0,
\tag{PP2}
\]
on \(L^2(SU(2)^{E_L})^{SU(2)^{V_L}}\). Here \(P_p\) is the actual oriented plaquette holonomy and \(C_e\) has eigenvalue \(j(j+1)\). No edge clock is reassigned after changing coordinates.

A rooted spanning tree removes all vertex frames except the root. Its \(N\) chord holonomies have product Haar measure, giving
\[
\mathcal H_{L,\rm phys}\cong L^2(SU(2)^N)^{\operatorname{Ad}SU(2)}.
\tag{PP3}
\]
This is one residual simultaneous conjugation, not a product of separate one-plaquette class carriers. Ungauging boundary vertices would change (PP3) and the mode selection below.

The square patch, including its filled faces, is simply connected. If every plaquette has holonomy \(I\), parallel transport is path independent and the connection is pure gauge. The rooted tree presentation therefore has exactly one zero of the magnetic potential, the identity chord tuple. Since \(2-\chi_{1/2}(U)\) vanishes only at \(U=I\), no additional center-valued magnetic minimum occurs.

Base each face loop at the root using tree connectors. Near the flat tuple, its logarithm \(x_p\in\mathfrak{su}(2)\cong\mathbb R^3\) defines a local face chart. To see invertibility, the integral elementary face boundaries form a basis of the graph's cycle lattice: the filled planar cell complex has zero first and second homology. Relative to the fundamental chord cycles their change-of-basis matrix is unimodular. This is the derivative of the based-face map at the identity; the inverse function theorem supplies the local chart. The global chord carrier remains the one in (PP3).

The pushed Haar measure in this local face chart has a smooth positive density. It need not be product Haar in the face variables. The chart and its density are equivariant under simultaneous conjugation; all localization below is performed on this smooth cover before taking invariants.

## The edge form gives a Dirichlet face matrix

Let \(B_L\) be the oriented face-edge incidence matrix, with entries \(+1,-1,0\). At the flat connection, differentiating the based plaquette cancels the two connector contributions and gives the linear curvature
\[
x_p=\sum_e(B_L)_{pe}a_e+O(|a|^2),
\]
where \(a_e\) is the raw edge logarithm. Thus the principal kinetic matrix in the face chart is
\[
\boxed{A_L=B_LB_L^{\mathsf T}
=4I-\operatorname{Adj}_L.}
\tag{PP4}
\]
Here \(\operatorname{Adj}_L\) is the nearest-neighbor adjacency matrix on the \(L\times L\) face grid. Adjacent counterclockwise faces traverse their common edge oppositely, giving the entry \(-1\). Every face still has four raw edges, including at the boundary, so every diagonal entry is four. This is the Dirichlet matrix with zero exterior face values, not the grid degree Laplacian.

For \(1\le r,s\le L\), its orthonormal sine modes and eigenvalues are
\[
v_{rs}(i,j)=\frac2{L+1}
\sin\frac{r\pi i}{L+1}\sin\frac{s\pi j}{L+1},
\]
\[
\boxed{\lambda_{rs}
=4-2\cos\frac{r\pi}{L+1}-2\cos\frac{s\pi}{L+1},
\qquad
\lambda_{\min}=4-4\cos\frac{\pi}{L+1}>0.}
\tag{PP5}
\]
The smallest spatial mode, \((r,s)=(1,1)\), is simple. Changing face orientations conjugates (PP4) by a diagonal sign matrix and does not change its spectrum.

## Harmonic localization retains the complete physical spectrum

Write \(P_p=\exp(-ix_p\cdot\sigma/2)\) in the local face chart. The magnetic potential is
\[
\sum_p(2-\chi_{1/2}(P_p))
=\frac14\sum_p|x_p|^2+O_L(|x|^4).
\]
Set \(h=(\kappa/g)^{1/4}\), dilate \(x=hX\), and divide energies by \(\sqrt{\kappa g}=\kappa/h^2\). The limiting oscillator on \(\mathbb R^{3N}\) is
\[
\boxed{\mathcal O_L
=p^{\mathsf T}(A_L\otimes I_3)p+\frac14|X|^2
=\sum_{r,s}\left(\lambda_{rs}|p_{rs}|^2+\frac14|Y_{rs}|^2\right),}
\tag{PP6}
\]
where \(Y_{rs}=\sum_pv_{rs}(p)X_p\). These normal-coordinate changes act on face labels and commute with the common adjoint rotation of the three color components.

For each fixed \(L\), the harmonic comparison is a full-carrier min–max argument. The rooted-tree kinetic operator is a smooth real uniformly elliptic operator on the compact chord cover: the chord-edge Casimirs already control all chord derivatives, and the remaining edge contributions are positive forms. Its magnetic potential has the unique nondegenerate well identified above.

Choose adjoint-invariant IMS cutoffs at chart radius \(\delta_h=h^\alpha\), \(0<\alpha<1\). In the scaled operator the localization error is \(O_L(h^2/\delta_h^2)=o(1)\). Outside the inner ball, the potential is at least \(c_L\delta_h^2\), so its scaled contribution diverges like \((\delta_h/h)^2\). Inside, the principal coefficients approach \(A_L\otimes I_3\), the potential has its positive quadratic approximation, and the Haar density remains smooth and positive. Dilation and multiplication by its square root give an equivariant local isometry. The resulting inner form differs from (PP6) by a vanishing relative and additive error.

The lower min–max bound follows from the localized direct sum: its outside block escapes, while extending the inside Dirichlet functions by zero compares them to the invariant oscillator on all of \(\mathbb R^{3N}\). For the upper bound, pull back a fixed finite set of invariant oscillator eigenfunctions and cut off their Gaussian tails. Their Rayleigh matrices converge. All constants may depend on \(L\), and no uniform ellipticity bound as \(L\to\infty\) is asserted in this comparison.

If \(E_{m,L}(g)\) are the ordered physical eigenvalues and \(\omega_{m,L}^{\rm inv}\) the ordered simultaneous-rotation-invariant oscillator eigenvalues, this proves
\[
\boxed{\frac{E_{m,L}(g)}{\sqrt{\kappa g}}
\longrightarrow\omega_{m,L}^{\rm inv}
\quad\text{for every fixed }L,m.}
\tag{PP7}
\]
In particular the vacuum energy is that of the actual interacting operator. No singular quotient coordinates or extra boundary conditions at the flat orbit are introduced.

Each spatial normal mode has three oscillator components with excitation frequency \(\sqrt{\lambda_{rs}}\). The ground Gaussian is a rotational scalar. Every one-quantum state transforms as spin one under the residual Gauss group and is excluded from the physical carrier. Two quanta in the lowest spatial mode contain the scalar \(\sum_a(a_{11,a}^{\dagger})^2\Omega_L\); no state with two or more quanta has a smaller excitation energy. Therefore the complete physical gap satisfies
\[
\boxed{\Delta_L(g)
=2\sqrt{\kappa g}\sqrt{4-4\cos\frac{\pi}{L+1}}
+o_L(\sqrt{\kappa g}),
\qquad g/\kappa\to\infty,\quad L\text{ fixed}.}
\tag{PP8}
\]
For one plaquette this gives \(4\sqrt{\kappa g}\), including the scalar-sector factor two. There is no external representation fiber that could pair with a single adjoint quantum.

## A normalized neutral source sees the soft mode

Let \(Y=Y_{11}\), \(\lambda=\lambda_{\min}\), and let \(d\nu_L=|\Omega_L|^2dX\) be the normalized oscillator vacuum measure. Each component of \(Y\) has variance \(\sqrt\lambda\). The scalar multiplication source
\[
\boxed{f_L(X)=\frac{|Y|^2/\sqrt\lambda-3}{\sqrt6}}
\tag{PP9}
\]
has \(\nu_L(f_L)=0\), \(\nu_L(f_L^2)=1\). The vector \(f_L\Omega_L\) is precisely the normalized scalar two-quantum state. With \(K_L^{\rm osc}=\mathcal O_L-\omega_{0,L}\),
\[
K_L^{\rm osc}f_L\Omega_L=2\sqrt\lambda\,f_L\Omega_L,
\qquad
\langle f_L\Omega_L,(K_L^{\rm osc})^{-1}f_L\Omega_L\rangle
=\frac1{2\sqrt\lambda}.
\tag{PP10}
\]
This is the normalized resolvent susceptibility; the negative ground-energy Hessian for a perturbation \(-sf_L\) is twice that quantity. It is a response in the scaled oscillator energy units.

At scaled duration \(\tau>0\), let \(A_\tau=e^{-\tau K_L^{\rm osc}}\) and \(R_\tau=I-A_\tau^2\). The same normalized state has the exact innovation-surplus quotient
\[
\boxed{
\frac{\|R_\tau f_L\Omega_L\|^2}
{\langle f_L\Omega_L,R_\tau f_L\Omega_L\rangle}
=1-e^{-4\tau\sqrt\lambda}.}
\tag{PP11}
\]
Thus the loss of a uniform harmonic coefficient is visible in a neutral scalar response, not only in an eigenvalue list. [[conditional-vacuum-rigidity-and-the-physical-gap|The complete physical-source criterion]] supplies the corresponding source and susceptibility distinctions.

There is an actual bounded compact multiplication probe with this quadratic jet. Write each based face holonomy as \(P_p=q_{0,p}I-i\mathbf q_p\cdot\sigma\), and define
\[
\mathcal B_L=\left|\sum_pv_{11}(p)\mathbf q_p\right|^2.
\tag{PP12}
\]
All \(\mathbf q_p\) rotate together, so this is gauge invariant. Near the well,
\(\mathcal B_L=\frac14|\sum_pv_{11}(p)x_p|^2+O_L(|x|^4)\).
It supplies a concrete physical source for the nonlinear calculation. Equations (PP9)–(PP11) describe the limiting oscillator source. [[compact-source-normalization-and-the-nonlinear-return|The compact-source theorem]] now proves its fixed-patch covariance and susceptibility expansion with the actual vacuum and normalization; [[nonlinear-scalar-source-and-the-vacuum-response-coefficient|the first coefficient]] separates the gap shift from source leakage. A remainder uniform in spatial size is still required for a joint limit.

## The coefficient cannot be bounded below uniformly in patch size

The proved coefficient is
\[
c_L=2\sqrt{\lambda_{\min}}
=4\sqrt2\sin\frac{\pi}{2(L+1)}
=\frac{2\sqrt2\pi}{L+1}+O((L+1)^{-3})
\longrightarrow0.
\tag{PP13}
\]
Accordingly the susceptibility in (PP10) diverges like \((L+1)/(2\sqrt2\pi)\), and the fixed-\(\tau\) quotient in (PP11) tends to zero. These are exact statements about the harmonic response family.

There cannot be a constant \(c>0\), independent of \(L\), such that \(\Delta_L(g)\ge c\sqrt{\kappa g}\) on every patch at all sufficiently strong confinement. Even allowing the onset threshold to depend on \(L\) does not help: take the fixed-\(L\) limit first in (PP8), then choose \(L\) with \(c_L<c\). One can also choose a diagonal sequence \(g_L/\kappa\to\infty\) large enough to realize the fixed-patch asymptotic and obtain \(\Delta_L(g_L)/\sqrt{\kappa g_L}\to0\).

This does not show that \(\Delta_L(g_L)\) itself vanishes, or determine \(\lim_{L\to\infty}\Delta_L(g)\) at fixed \(g\). The comparison proved here has size-dependent constants. [[uniform-planar-localization-and-the-first-physical-levels|Uniform planar localization]] now supplies a quantified joint growing-patch window: its scaled gap follows \(c_L\), while its absolute gap grows. Nor is this isolated planar law automatically the induced vacuum of a region inside a three-dimensional lattice. A positive coefficient proportional to \(\sqrt{\kappa g}\) is refuted for the stated family; an absolute physical-gap bound, the three-dimensional spatial theory and the continuum Yang–Mills target are separate questions.
