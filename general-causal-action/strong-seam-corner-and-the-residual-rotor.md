# Strong Seams and the Residual Corner Rotor

The corner's two strongly confined seam holonomies leave a central rotor whose coefficient is fixed by the raw-edge incidence matrix. Direct compression into the actual vacuum misses a finite derivative-coupling correction. The complete quantum return, now proved in a separate module, retains that correction and gives the fundamental energy \(10\epsilon/3\).

**Status: exact finite-vacuum compression and Euclidean response identity; proved \(SU(2)\) strong-seam return.** [[corner-hamiltonian-and-the-complete-fusion-response|The Hamiltonian corner]] owns the fixed law. [[corner-response-and-the-failure-of-multiplicative-attenuation|The connected-gain test]] rejects multiplying its local suppression factors. This note owns the Schur calculation; [[strong-seam-resolvent-and-the-physical-rotor|the complete physical return]] owns the compact-group proof. The base test is a fixed spatial graph with zero central magnetic coupling.

## Keep the actual vacuum in the slow comparison

Set \(g_1=g_2=g>0\), \(\kappa=4\epsilon/3\), and write
\[
\mathsf K_g=\mathsf H_g-E_\Omega(g).
\]
The exact vacuum is independent of \(U\). Restricting the Hamiltonian to \(U\)-independent functions gives the actual adjacent two-plaquette problem on \(V,W\); its positive eigenvector is also a positive full-carrier eigenvector, hence the unique full vacuum. This is the Hamiltonian form of [[three-face-corner-and-joint-seam-response|CJ7]], with the vacuum construction in [[coarse-response-memory/two-plaquette-vacuum-and-relational-state|the interacting two-plaquette owner]].

Thus, for the actual normalized \(\psi_g(V,W)>0\),
\[
J_gf=f(U)\psi_g(V,W),\qquad
J_g:L^2(SU(2))^{\mathrm{Ad}}\longrightarrow\mathcal H_{\rm phys},
\qquad J_g^*J_g=I.
\tag{SR1}
\]
No density on \(U\) is fitted. In particular \(J_g1\) is the exact vacuum. In the raw differential operator of [[corner-hamiltonian-invariant-polynomials|IP3]], the \(U\)-fast cross terms have zero vacuum expectation, because each left or right derivative is skew-adjoint and \(\psi_g\) is real. Consequently, as a quadratic-form identity on smooth class functions,
\[
\boxed{J_g^*\mathsf K_gJ_g=4\kappa C_U.}
\tag{SR2}
\]
Compression alone leaves the free central coefficient unchanged. Any reduction must come from excursions outside this vacuum product subspace.

## A complete elimination includes the derivative coupling

Put \(\Pi_g=J_gJ_g^*\), \(Q_g=I-\Pi_g\). For \(z>0\), the exact block elimination of \(\mathsf K_g+z\) has slow Schur operator
\[
\mathsf S_g(z)=4\kappa C_U+z
-J_g^*\mathsf K_gQ_g
\bigl[Q_g(\mathsf K_g+z)Q_g\bigr]^{-1}
Q_g\mathsf K_gJ_g.
\tag{SR3}
\]
Use its closed-form interpretation if a product is unbounded. This is [[coarse-response-memory/inq|the inherited dynamical Schur response]], applied to the specified physical vacuum. It does not assume a physical gap.

Near \(V=W=I\), let \(p=(p_V,p_W)\) be the Euclidean normal momenta. With self-adjoint left and right \(U\)-momenta \(J_L,J_R\), the principal kinetic expression is
\[
\kappa\bigl[4C_U+p^{\mathsf T}Ap+2b^{\mathsf T}p\bigr],
\qquad
A=\begin{pmatrix}4&1\\1&4\end{pmatrix},
\quad b=\binom{J_L}{-J_R}.
\tag{SR4}
\]
Each entry carries three Lie-algebra components. This matrix retains the one shared seam edge. Its algebraic Schur expression is
\[
4C_U-b^{\mathsf T}A^{-1}b
=\frac{52}{15}C_U-\frac{2}{15}J_L\cdot J_R
=\frac{10}{3}C_U
\quad\text{on class functions}.
\tag{SR5}
\]
The last equality uses the conjugation constraint \(J_Lf=J_Rf\), not commutativity of group multiplication.

There is an exact quantum identity behind this calculation. For a Euclidean confined Hamiltonian
\(H_f=\kappa p^{\mathsf T}Ap+V(x)\), let \(\varphi\) be a real normalized simple isolated ground state with the coordinate and momentum vectors in the required operator/form domains. Let \(R_f=(H_f-E_f)^{-1}\) off its ground state. The commutator
\([H_f,x_b]=-2i\kappa\sum_aA_{ba}p_a\) and the ground-state form identity give
\[
\boxed{\langle p_a\varphi,R_fp_b\varphi\rangle
=\frac{(A^{-1})_{ab}}{4\kappa}.}
\tag{SR6}
\]
Indeed \(p_a\varphi=(i/2\kappa)\sum_b(A^{-1})_{ab}(H_f-E_f)x_b\varphi\), and
\(\langle x_a\varphi,(H_f-E_f)x_b\varphi\rangle=\kappa A_{ab}\).
Centering the coordinate vectors changes neither relation. This is a ground-state commutator sum rule, related to [[algebra/partial-bochner-and-ground-state-score|the existing score sum rules]], rather than a new spectral principle.

For the leading normal oscillator, (SR6) fixes the complete second-order derivative-coupling correction to be \(\kappa b^{\mathsf T}A^{-1}b\), independently of the oscillator's restoring matrix. A fast gap of order \(\sqrt{\epsilon g}\) does not make it vanish: the two momentum matrix elements each scale as \((g/\epsilon)^{1/4}\). This explains the candidate coefficient. The compact-group proof instead uses an exact ground-form corrector and lower bound, so it need not justify a termwise expansion of the Schur inverse.

## The complete return is now proved

At fixed \(\epsilon>0\), the full-carrier norm-resolvent theorem is
\[
\boxed{
\left\|(\mathsf K_g+z)^{-1}
-J_g\left(\frac{10\kappa}{3}C_U+z\right)^{-1}J_g^*
\right\|\longrightarrow0
\qquad(g/\epsilon\to\infty),\ z>0.}
\tag{SR7}
\]
[[strong-seam-resolvent-and-the-physical-rotor|PR1–15]] proves this statement and the return of bounded continuous source histories at positive durations. The complete finite-graph physical gap tends to \(10\epsilon/3\), since the first nonconstant class character has \(C_{1/2}=3/4\) and every additional fixed-representation mode escapes to high energy.

Three estimates supply the proof: [[magnetic-completion-and-the-corner-representation-tail|the completed magnetic form]] bounds every central representation at all strengths; [[corner-corrector-and-the-fixed-representation-return|the actual-vacuum corrector]] attains its limiting coefficient; and [[corner-fast-vacuum-and-harmonic-separation|equivariant harmonic separation]] excludes extra slow lines. Their combination controls the complete carrier. The exact isometry (SR1) fixes the Haar class-function measure and constant vacuum.

[[abelian-corner-and-the-strong-seam-return|The Abelian strong-seam theorem]] provides the matching flux-sector benchmark, with its torus twist retained. The agreement identifies a nonperturbative incidence-controlled remainder in this finite family. A central interaction of fixed strength also survives by PR16–18, but comparable confinement of all three faces is a different limit. Neither finite return supplies the spatial continuum or infinite-volume Yang–Mills estimate.
