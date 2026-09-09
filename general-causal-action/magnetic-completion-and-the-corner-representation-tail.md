# Magnetic Completion Controls the Corner Representation Tail

The complete \(SU(2)\) corner Hamiltonian has an exact lower bound at every seam strength: after subtracting its actual vacuum, the sector of central spin \(j\) lies above \((10\kappa/3)j(j+1)\), where \(\kappa=4\epsilon/3\). Completing the mixed kinetic form produces a Hermitian matrix connection; taking the norm of its vector-valued section returns the actual scalar fast-vacuum problem. This controls every large representation uniformly and bounds the complete center-odd energy between \(10\epsilon/3\) and \(4\epsilon\). It does not yet control the excited \(j=0\) sector or prove the proposed strong-seam resolvent return.

**Status: exact all-strength finite-graph form inequality and uniform representation-tail estimate.** [[corner-hamiltonian-invariant-polynomials|IP3]] fixes the raw differential operator. [[strong-seam-corner-and-the-residual-rotor|SR1–7]] fixes the actual vacuum isometry and the strong-seam target. The argument uses the existing [[abelian-corner-and-the-strong-seam-return|diamagnetic norm principle]] with a finite matrix fiber; its connection need not be flat.

## Resolve the central representation before completing the square

The physical carrier remains
\[
\mathcal H_{\rm phys}
=L^2(SU(2)^3,dU\,dV\,dW)^{\mathrm{Ad}SU(2)}.
\]
Use self-adjoint left and right momenta \(J_L,J_R\), with Casimir \(C=\sum_aJ_{L,a}^2=\sum_aJ_{R,a}^2\). For \(g\ge0\), put
\[
\mathsf H_g=\kappa\left[
4C_U+4(C_V+C_W)+2J_{R,V}\!\cdot J_{R,W}
+2J_{L,U}\!\cdot J_{L,V}-2J_{R,U}\!\cdot J_{L,W}
\right]+g\mathcal V(V,W),
\]
\[
\mathcal V=4-\chi_{1/2}(V)-\chi_{1/2}(W),\qquad
\mathsf K_g=\mathsf H_g-E_\Omega(g).
\tag{MT1}
\]
These are exactly the nine-link Casimirs and two seam potentials. The \(U\)-Casimir commutes with this operator and with joint Gauss projection.

In its spin-\(j\) block, normalized Peter–Weyl expansion in \(U\) identifies a function with a vector \(\Psi(V,W)\) in the finite fiber
\[
\mathcal E_j=V_j\otimes V_j^*,\qquad
\|\Psi\|^2=\int_{SU(2)^2}\|\Psi(V,W)\|_{\mathcal E_j}^2.
\tag{MT2}
\]
The physical subspace imposes simultaneous-conjugation equivariance. On the full fiber, the two \(U\)-momenta are Hermitian matrices \(L_a,R_a\), with
\(\sum_aL_a^2=\sum_aR_a^2=C_jI\), \(C_j=j(j+1)\). The proof below holds before restricting to that equivariant subspace.

Use right-invariant normal momenta
\[
p=(J_{R,V},J_{R,W}),\qquad
A=\begin{pmatrix}4I_3&I_3\\I_3&4I_3\end{pmatrix},
\qquad 3I_6\le A\le5I_6.
\tag{MT3}
\]
Let the real adjoint rotations \(O(V),O(W)\) be defined by \(J_{L,V}=O(V)J_{R,V}\) and similarly for \(W\). The cross terms in the quadratic form are encoded by six Hermitian fiber matrices
\[
b(V,W)=\binom{O(V)^{\mathsf T}L}{-O(W)^{\mathsf T}R},
\qquad \sum_{\alpha=1}^6b_\alpha^2=2C_jI.
\tag{MT4}
\]
The metric \(A\) is globally constant in this frame. All nonconstant frame coefficients stay in \(b\); Haar probability remains the integration measure.

## The connection is unitary even when its components do not commute

Set \(c=A^{-1}b\) and \(D_\alpha=p_\alpha+c_\alpha\). Since \(A\) is real and \(b_\alpha\) is Hermitian, every \(c_\alpha\) is Hermitian. Direct completion of the quadratic form gives
\[
\begin{aligned}
q_{j,g}[\Psi]
={}&\kappa\int\sum_{\alpha,\beta}A_{\alpha\beta}
\langle D_\alpha\Psi,D_\beta\Psi\rangle\\
&+\kappa\int\left\langle\Psi,
\left(4C_jI-\sum_{\alpha,\beta}b_\alpha(A^{-1})_{\alpha\beta}b_\beta\right)
\Psi\right\rangle
+g\int\mathcal V\|\Psi\|^2.
\end{aligned}
\tag{MT5}
\]
This equality is stated on smooth sections and then closed. It does not commute a derivative through \(b\) or discard a coefficient derivative. Expanding the closed covariant form retains such terms automatically. No commutativity between distinct connection matrices is required.

Pointwise, \(A^{-1}\le I/3\) implies
\[
\sum_{\alpha,\beta}
\langle b_\alpha\Psi,(A^{-1})_{\alpha\beta}b_\beta\Psi\rangle
\le\frac13\sum_\alpha\|b_\alpha\Psi\|^2
=\frac23C_j\|\Psi\|^2.
\tag{MT6}
\]
Thus the scalar residual in (MT5) is bounded below by \(10C_j/3\).

For completeness, let \(r=\|\Psi\|_{\mathcal E_j}\), and write \(p_\alpha=-iX_\alpha\), where \(X_\alpha\) is a real right-invariant vector field. At \(r>0\),
\[
X_\alpha r
=\operatorname{Re}\left\langle\frac{\Psi}{r},iD_\alpha\Psi\right\rangle.
\]
The connection term drops from this real part because \(\langle\Psi,c_\alpha\Psi\rangle\) is real. Projection onto the real unit vector \(\Psi/r\), applied after \(A^{1/2}\) in the six derivative components, is contractive. Hence
\[
\sum_{\alpha,\beta}A_{\alpha\beta}(X_\alpha r)(X_\beta r)
\le\sum_{\alpha,\beta}A_{\alpha\beta}
\langle D_\alpha\Psi,D_\beta\Psi\rangle.
\tag{MT7}
\]
Regularizing \(r\) by \(\sqrt{\|\Psi\|^2+\delta^2}\) and taking \(\delta\downarrow0\) proves the form-domain version across zeros. For each fixed \(j\), all connection coefficients are smooth and bounded on the compact normal manifold, so smooth sections are a common form core.

## Taking the vector norm returns the actual vacuum

The scalar form on the left of (MT7), with the same potential, is precisely that of
\[
\mathsf H_{{\rm fast},g}
=\kappa\left[4(C_V+C_W)+2J_{R,V}\!\cdot J_{R,W}\right]
+g\mathcal V(V,W).
\tag{MT8}
\]
Its real uniformly elliptic operator on connected \(SU(2)^2\) has a unique positive ground state. Simultaneous-conjugation invariance makes that ground state neutral. Its lift, independent of \(U\), is the actual full vacuum \(\psi_g(V,W)\), as in SR1. Therefore its lowest energy is exactly \(E_\Omega(g)\), with the same normalization as (MT1).

Combining (MT5–8) gives, for every spin and seam strength,
\[
\boxed{\mathsf H_{j,g}-E_\Omega(g)\ge\frac{10\kappa}{3}C_jI,
\qquad
\mathsf K_g\ge\frac{10\kappa}{3}C_U.}
\tag{MT9}
\]
The second inequality is the direct sum of the first, restricted to the full physical carrier. It is a form inequality, not a comparison with an independently chosen fast density.

The exact vacuum isometry \(J_gf=f(U)\psi_g\) obeys
\(J_g^*\mathsf K_gJ_g=4\kappa C_U\). Testing with the normalized character \(\chi_j\) gives the complementary upper bound on each sector bottom:
\[
\boxed{
\frac{10\kappa}{3}C_j
\le \inf\operatorname{spec}(\mathsf K_g|_j)
\le4\kappa C_j.}
\tag{MT10}
\]
The center-odd carrier consists of all half-integer \(j\). Its complete bottom therefore satisfies
\[
\boxed{\frac{10}{3}\epsilon\le E_-(g,g)\le4\epsilon
\qquad(g\ge0).}
\tag{MT11}
\]
This bounds the total softening in this family without asserting monotonicity or summing perturbative coefficients. The \(j=0\) block contains the actual vacuum and its fast excitations, so (MT9) alone is not a lower bound for the full physical gap.

## The infinite representation tail is now controlled

Let \(\mathcal P_{\le J}\) retain \(U\)-spins \(j\le J\), with \(J\in\frac12\mathbb N_0\), and let \(z>0\). The commuting block decomposition and (MT9) imply
\[
\boxed{
\|(I-\mathcal P_{\le J})(\mathsf K_g+z)^{-1}\|
\le
\frac1{z+(10\kappa/3)(J+\frac12)(J+\frac32)}.}
\tag{MT12}
\]
The estimate is uniform in \(g\). The same bound holds for the discarded tail of the rotor comparison
\[
J_g\left((10\kappa/3)C_U+z\right)^{-1}J_g^*.
\]
Consequently the full norm-resolvent statement SR7 follows if its difference tends to zero on each fixed finite set of \(U\)-spins. The discarded part of the difference is at most twice the right side of (MT12).

Each retained spin block still has an infinite-dimensional fast carrier. [[strong-seam-resolvent-and-the-physical-rotor|The complete return theorem]] combines the actual-vacuum corrector and harmonic separation with (MT12), including the excited \(j=0\) block. The present estimate removes the representation-tail obligation without assuming those fixed-block limits, a spatial-volume estimate or a Yang–Mills mass gap.
