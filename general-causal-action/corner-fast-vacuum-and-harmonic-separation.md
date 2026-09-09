# The Corner's Fast Vacuum Has a Diverging Excitation Gap

The two strongly confined seam holonomies have one nondegenerate magnetic well. Localization and a direct min–max comparison with its six-dimensional oscillator prove that, in every fixed central-spin sector, exactly one state remains at the oscillator ground level. Every second state separates from the actual vacuum by order \(\sqrt{\kappa g}\). The calculation retains Gauss invariance on the smooth group cover; singular orbit coordinates introduce no extra angular zero modes. Its constants are not uniform in the central spin.

**Status: proved fixed-spin harmonic separation on the actual finite graph.** [[strong-seam-corner-and-the-residual-rotor|The residual-rotor target]] needs this fast separation in addition to its slow trial states and its control of large central spin. The raw differential operator is [[corner-hamiltonian-invariant-polynomials|IP3]]. This note proves the necessary spectral separation directly, without importing an adiabatic theorem.

## Fix the normalization before expanding the well

Put \(\kappa=4\epsilon/3>0\), and write self-adjoint right momenta as \(J_R=-i\mathcal R\). The \(U\)-independent fast operator on \(SU(2)^2\) is
\[
H_{f,g}
=\kappa K_f+g\mathcal V,\qquad
K_f=4(C_V+C_W)+2J_{R,V}\cdot J_{R,W},
\]
\[
\mathcal V=(2-\chi_{1/2}(V))+(2-\chi_{1/2}(W)).
\tag{FH1}
\]
Its quadratic form satisfies
\[
3(C_V+C_W)\ \le K_f\le\ 5(C_V+C_W)
\tag{FH2}
\]
in form order, by Cauchy–Schwarz on the cross term. It is uniformly elliptic on the compact smooth covering manifold. The real potential has a unique zero, \((V,W)=(I,I)\). The lowest eigenfunction is smooth, positive and unique. Its invariance under simultaneous conjugation follows from uniqueness.

Use exponential coordinates
\[
V=\exp(-ix\cdot\sigma/2),\qquad
W=\exp(-iy\cdot\sigma/2).
\]
At the well the principal kinetic matrix and potential are
\[
A_0=\begin{pmatrix}4&1\\1&4\end{pmatrix}\otimes I_3,\qquad
\mathcal V=\frac{|x|^2+|y|^2}{4}+O(|(x,y)|^4).
\tag{FH3}
\]
Set \(h=(\kappa/g)^{1/4}\). Dividing the operator by
\(\sqrt{\kappa g}=\kappa/h^2\), and rescaling \((x,y)=h(X,Y)\), gives the candidate oscillator
\[
\mathcal O=p^TA_0p+\frac{|X|^2+|Y|^2}{4}.
\tag{FH4}
\]
The proof of spectral convergence is given below.

In the orthogonal coordinates \(Z_\pm=(X\pm Y)/\sqrt2\), this is the sum of three oscillators with excitation frequency \(\sqrt5\) and three with frequency \(\sqrt3\). Its ground energy is
\[
\omega_0=\frac32(\sqrt5+\sqrt3).
\tag{FH5}
\]
Here “excitation frequency” means the difference between successive one-dimensional oscillator levels; the zero-point contribution is half that number.

## The fixed-spin carrier keeps the correct gauge multiplicity

Peter–Weyl decomposition in \(U\) preserves each \(j\)-block of the full corner Hamiltonian, because the seams do not involve \(U\). Represent that block by matrix-valued functions
\[
F(U,V,W)=\operatorname{Tr}(\rho_j(U)f(V,W)).
\]
Give \(\mathcal E_j=\operatorname{End}(V_j)\) the inner product
\(\langle B,C\rangle=\operatorname{Tr}(B^\dagger C)/(2j+1)\). Haar orthogonality makes this representation isometric. The physical block is
\[
\mathscr H_j=
\left\{f\in L^2(SU(2)^2;\mathcal E_j):
f(kVk^{-1},kWk^{-1})=\rho_j(k)f(V,W)\rho_j(k)^{-1}\right\}.
\tag{FH6}
\]
In this convention the constant matrix \(I\) has unit norm and corresponds to the character \(\chi_j(U)\).

For fixed \(j\), the \(U\) derivatives in IP3 become bounded matrices on \(\mathcal E_j\). Thus the actual block Hamiltonian differs from \(H_{f,g}\otimes I\) only by \(\kappa\) times fixed smooth first-order terms and bounded zeroth-order terms. Cauchy–Schwarz and (FH2) give, for every \(0<\eta<1\),
\[
\left|\kappa^{-1}q_{H_j-H_{f,g}}[f]\right|
\le \eta\,q_{K_f}[f]+C_j(1+\eta^{-1})\|f\|^2.
\tag{FH7}
\]
The same estimate holds for any fixed smooth finite-dimensional covariant connection with bounded coefficients. It need not hold uniformly when \(j\) grows.

After division by \(\sqrt{\kappa g}\), choose \(\eta=h\). The difference of the two scaled forms is bounded by \(h\) times the scaled fast kinetic form plus \(O_j(h)\|f\|^2\). Since the magnetic potential is nonnegative, their ordered eigenvalues have the same fixed-index limits. It therefore suffices to compare the scalar fast form, tensored with \(\mathcal E_j\) and restricted by (FH6), with its oscillator.

## Localization gives the harmonic limit by min–max

Here is the comparison for each fixed eigenvalue index. All cutoffs are invariant under simultaneous conjugation. Choose \(r=h^\alpha\), with any fixed \(0<\alpha<1\), and smooth real functions \(\chi_0,\chi_1\) satisfying
\[
\chi_0^2+\chi_1^2=1,\qquad
\chi_0=1\ \text{inside }B_r,\qquad
\chi_0=0\ \text{outside }B_{2r},\qquad
|d\chi_i|\le C/r.
\]
The balls are in the exponential chart around the well. The IMS identity for the uniformly elliptic form shows that the localization error in the scaled operator
\(h^2K_f+h^{-2}\mathcal V\) is at most
\[
C h^2/r^2=o(1).
\tag{FH8}
\]
Outside \(B_r\), compactness and the positive Hessian give
\(\mathcal V\ge c r^2\). The outside localized form is therefore bounded below by \(c(r/h)^2\), which tends to infinity.

Inside \(B_{2r}\), the principal coefficients equal \(A_0+O(r)\); the Haar density is its positive value at the origin times \(1+O(r^2)\). The potential differs from its positive quadratic part by a relative \(O(r^2)\). Dilation followed by multiplication by the square root of the Haar density gives an isometry to a ball of radius \(2r/h\) in \(\mathbb R^6\). It intertwines the conjugation action exactly, since the exponential chart and Haar density are equivariant. On supported functions the scaled inner form differs from the oscillator form by a relative \(O(r)\) and an additive \(O(h^2)\). The density derivative contributes only to that controlled error.

For a lower bound, the map \(f\mapsto(\chi_0f,\chi_1f)\) is an isometry into the direct sum of the two localized form spaces. Its Rayleigh form differs by at most (FH8). The outside block lies above any fixed oscillator level for small \(h\). The inside block has a Dirichlet boundary after extension by zero; its oscillator eigenvalues are no smaller than those on \(\mathbb R^6\). The min–max principle therefore bounds the lower limit of every fixed eigenvalue by the corresponding equivariant oscillator eigenvalue.

For an upper bound, take the first finitely many equivariant oscillator eigenfunctions, dilate them into the chart, and apply \(\chi_0\). Their Gaussian tails make the cutoff error vanish as \(r/h\to\infty\). The coefficient comparison just established makes their finite-dimensional Rayleigh matrices converge to the oscillator matrices. Min–max gives the matching upper limits.

Consequently, for every fixed \(j\) and eigenvalue index \(m\),
\[
\boxed{
\frac{\lambda_{m,j}(g)}{\sqrt{\kappa g}}
\longrightarrow \nu_{m,j},}
\tag{FH9}
\]
where \(\lambda_{m,j}\) are the ordered eigenvalues of the actual block Hamiltonian, and \(\nu_{m,j}\) those of \(\mathcal O\otimes I_{\mathcal E_j}\) on its equivariant subspace. Equation (FH7) transfers the comparison to the actual matrix-valued block without changing the limit.

## Exactly one physical state occupies the lowest oscillator band

The oscillator ground function is a rotational scalar in both \(Z_+,Z_-\). Its tensor product with the fiber is invariant only when the matrix lies in
\(\operatorname{End}(V_j)^{SU(2)}=\mathbb C I\). The lowest equivariant oscillator eigenspace is therefore one-dimensional for every \(j\).

Furthermore,
\[
\operatorname{End}(V_j)\cong\bigoplus_{\ell=0}^{2j}V_\ell.
\]
One quantum in \(Z_-\) transforms as the spin-one adjoint representation. For \(j\ge1/2\), it pairs with the unique spin-one fiber component to give a physical state of energy \(\omega_0+\sqrt3\). No oscillator state lies between it and the ground level. For \(j=0\), a single quantum cannot be invariant; the first invariant excitation is the scalar two-quantum state in \(Z_-\), at energy \(\omega_0+2\sqrt3\). Thus
\[
\nu_{0,j}=\omega_0,\qquad
\nu_{1,j}-\omega_0=
\begin{cases}
2\sqrt3,&j=0,\\
\sqrt3,&j\ge1/2.
\end{cases}
\tag{FH10}
\]
In particular the lowest eigenvalue of each fixed block is simple for sufficiently large \(g/\kappa\).

The actual full vacuum is the \(j=0\) fast ground state, with energy \(E_\Omega(g)=\lambda_{0,0}(g)\). Combining (FH9)–(FH10) proves
\[
\boxed{
\frac{\lambda_{1,j}(g)-E_\Omega(g)}{\sqrt{\kappa g}}
\longrightarrow
\begin{cases}
2\sqrt3,&j=0,\\
\sqrt3,&j\ge1/2.
\end{cases}}
\tag{FH11}
\]
Hence every fixed physical \(j\)-block has exactly one state below the diverging fast excitation scale. This statement alone does not determine that remaining state's finite energy or eigenvector; those require the slow-state construction.

The fixed point of conjugation at the magnetic well creates no zero-frequency angular direction: the Hessian in (FH3) is positive in all six covering coordinates. Gauss law is imposed by the equivariant subspace, as in (FH6), rather than by artificial boundary conditions at singular orbit strata. No choice of a particular \(U\) conjugacy orbit is used. The constants \(C_j\) in (FH7) grow with the fiber representation; [[strong-seam-resolvent-and-the-physical-rotor|the complete return theorem]] therefore combines this fixed-spin separation with an independent all-spin lower bound and an actual-vacuum slow-state corrector.
