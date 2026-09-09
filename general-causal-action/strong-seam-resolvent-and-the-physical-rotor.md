# Strong-Seam Return of the Complete Physical Rotor

The nine-edge \(SU(2)\) corner returns a complete physical rotor when its two seam strengths increase together. The returned coefficient is \(10\kappa/3\), fixed by the shared-edge kinetic form. This is convergence of the full vacuum-subtracted resolvent, not just selected eigenvalues or a compression. Every bounded continuous physical source has the corresponding positive-time vacuum-history return, and a central magnetic face of fixed strength survives as the same multiplication operator.

**Status: proved at the fixed corner and fixed \(\kappa=4\epsilon/3>0\).** The Hamiltonian and Gauss carrier are those of [[corner-hamiltonian-and-the-complete-fusion-response|the complete corner]]. [[strong-seam-corner-and-the-residual-rotor|SR1–7]] owns the exact compression and the Schur calculation that proposed this return. The argument below combines three independent estimates on the actual compact-group problem; it does not replace its vacuum by a Gaussian.

## The operator and its physical comparison

Write the gauge-fixed loops as \(U,V,W\). On
\(\mathcal H=L^2(SU(2)^3)^{\mathrm{Ad}}\), let
\[
\mathsf H_g=\kappa\sum_{\text{nine raw }e} C_e
+g\{(2-\chi_{1/2}(V))+(2-\chi_{1/2}(W))\},
\qquad
\mathsf K_g=\mathsf H_g-E_\Omega(g),\qquad g\ge0.
\tag{PR1}
\]
The kinetic form is the raw-edge form in [[corner-hamiltonian-invariant-polynomials|IP3]]. The central face initially has zero magnetic coupling. The unique normalized positive vacuum \(\psi_g(V,W)\) is independent of \(U\). Thus
\[
J_gf=f(U)\psi_g(V,W),\qquad
J_g:\mathcal H_{\mathrm{rot}}=L^2(SU(2))^{\mathrm{Ad}}\longrightarrow\mathcal H,
\qquad J_g^*J_g=I,\qquad J_g1=\psi_g.
\tag{PR2}
\]
The candidate returned operator is
\[
\mathsf H_{\mathrm{rot}}=\frac{10\kappa}{3}C_U,\qquad
a_j=\frac{10\kappa}{3}j(j+1),\qquad j=0,\tfrac12,1,\ldots .
\tag{PR3}
\]
Its orthonormal eigenbasis consists of the characters \(\chi_j\).

The central Casimir commutes with \(\mathsf H_g\) and simultaneous conjugation. Hence the complete physical carrier decomposes as \(\mathcal H=\bigoplus_j\mathcal H_j\), with no restriction on the remaining \(V,W\) representations. Denote the two lowest eigenvalues of \(\mathsf K_g|_{\mathcal H_j}\), counting multiplicity, by \(e_j(g)\) and \(b_j(g)\).

## Three estimates control different parts of the carrier

[[magnetic-completion-and-the-corner-representation-tail|MT9–12]] gives an all-strength, all-representation form bound:
\[
\mathsf K_g|_{\mathcal H_j}\ge a_j I .
\tag{PR4}
\]
This uses the completed matrix-valued kinetic square and the norm of the physical coefficient vector. The scalar comparison vacuum is exactly \(\psi_g\). It controls arbitrarily large \(j\), including representations growing with \(g\).

[[corner-corrector-and-the-fixed-representation-return|CR7–12]] supplies normalized physical vectors \(u_{j,g}\) for each fixed \(j\). With \(h=(\kappa/g)^{1/4}\), for \(g\ge\kappa\),
\[
\|u_{j,g}-J_g\chi_j\|\le C_j h,\qquad
a_j\le e_j(g)\le
\langle u_{j,g},\mathsf K_g u_{j,g}\rangle
\le a_j+C_j\kappa h.
\tag{PR5}
\]
The vector is built from the actual vacuum multiplied by a smooth corrected central holonomy. Its optimized first derivatives give the coefficient \(10/3\) through the exact vacuum ground-form identity.

[[corner-fast-vacuum-and-harmonic-separation|FH9–11]] controls the next eigenvalue for every fixed \(j\):
\[
\frac{b_j(g)}{\sqrt{\kappa g}}\longrightarrow
\begin{cases}
2\sqrt3,&j=0,\\
\sqrt3,&j>0.
\end{cases}
\tag{PR6}
\]
The unique fast well has precisely one lowest Gauss-invariant line in each fixed central representation. Its other modes leave every bounded physical energy interval. The proof retains the representation fiber and the Gauss constraint in localization and the oscillator comparison.

None of (PR5) or (PR6) asserts uniformity in \(j\). The separate bound (PR4) is what makes that unnecessary.

## Assemble the full norm-resolvent return

For a fixed \(j\), (PR5)–(PR6) make the lowest line simple for all sufficiently large \(g\). Let \(P_{j,g}\) be its orthogonal projection. The variational excess bounds its excited weight:
\[
\|(I-P_{j,g})u_{j,g}\|^2
\le
\frac{\langle u_{j,g},\mathsf K_g u_{j,g}\rangle-e_j(g)}
{b_j(g)-e_j(g)}
\le\frac{C_j\kappa h}{b_j(g)-e_j(g)}
\longrightarrow0.
\tag{PR7}
\]
Together with (PR5), this proves
\[
e_j(g)\longrightarrow a_j,\qquad
\left\|P_{j,g}
-|J_g\chi_j\rangle\langle J_g\chi_j|\right\|\longrightarrow0.
\tag{PR8}
\]
The resolvent on the orthogonal complement of \(P_{j,g}\) has norm at most \((b_j(g)+z)^{-1}\) for \(z>0\). Therefore
\[
\left\|(\mathsf K_g|_{\mathcal H_j}+z)^{-1}
-\frac{|J_g\chi_j\rangle\langle J_g\chi_j|}{a_j+z}\right\|
\longrightarrow0
\quad\text{for each fixed }j.
\tag{PR9}
\]

Let \(N\) run through nonnegative half-integers. The orthogonal sum over \(j\le N\) is finite, so (PR9) gives norm convergence there. On the entire remaining carrier, (PR4) gives
\[
\sup_g\left\|(\mathsf K_g+z)^{-1}
\big|_{\bigoplus_{j>N}\mathcal H_j}\right\|
\le\frac1{a_{N+1/2}+z}.
\tag{PR10}
\]
The returned rotor resolvent has the same tail bound. Consequently the limsup of the full difference is at most \(2/(a_{N+1/2}+z)\). Sending \(N\) to infinity proves
\[
\boxed{\left\|(\mathsf K_g+z)^{-1}
-J_g(\mathsf H_{\mathrm{rot}}+z)^{-1}J_g^*\right\|
\longrightarrow0,\qquad g\longrightarrow\infty,\quad z>0.}
\tag{PR11}
\]
The comparison kills the fast complement. The theorem concerns the complete physical Hilbert space even though the surviving carrier is smaller.

The complete physical gap also follows directly. Every \(j>0\) block lies above \(a_{1/2}\), the \(j=0\) excited bottom diverges, and \(e_{1/2}(g)\to a_{1/2}\). Thus
\[
\boxed{\Delta_{\mathrm{corner}}(g)\longrightarrow
\frac{10\kappa}{3}\frac34=\frac{10\epsilon}{3}.}
\tag{PR12}
\]
This includes all physical center-even and center-odd states.

## The same limit returns observable histories

For every fixed duration \(\ell>0\), continuous functional calculus applied to (PR11) gives
\[
\left\|e^{-\ell\mathsf K_g}
-J_g e^{-\ell\mathsf H_{\mathrm{rot}}}J_g^*\right\|\longrightarrow0.
\tag{PR13}
\]
Indeed \(x\mapsto e^{-\ell(1/x-z)}\), extended by zero at \(x=0\), is continuous on \([0,1/z]\). Its value at zero removes the fast complement of the embedded resolvent. This is the same functional-calculus mechanism used in [[strong-coupling-gap-and-continuum-crossover/wilson-to-hamiltonian-vacuum-limit|the temporal vacuum return]], with a different limit proved here.

Let \(B(U,V,W)\) be a bounded continuous simultaneous-conjugation-invariant source, and set \(b(U)=B(U,I,I)\). Then \(b\) is a class function. With \(d\mu_g=\psi_g^2\,dV\,dW\), CR's concentration estimate and uniform continuity on the compact configuration space give
\[
\begin{split}
\|M_BJ_g-J_gM_b\|^2
&\le\sup_U\int |B(U,V,W)-B(U,I,I)|^2\,d\mu_g(V,W)\\
&\longrightarrow0.
\end{split}
\tag{PR14}
\]
For any finite list of such sources and fixed positive time gaps, (PR13)–(PR14) and \(J_g1=\psi_g\) now imply, by telescoping bounded products,
\[
\begin{split}
&\langle\psi_g,M_{B_0}e^{-\ell_1\mathsf K_g}M_{B_1}
\cdots e^{-\ell_m\mathsf K_g}M_{B_m}\psi_g\rangle\\
&\hspace{1em}\longrightarrow
\langle1,M_{b_0}e^{-\ell_1\mathsf H_{\mathrm{rot}}}M_{b_1}
\cdots e^{-\ell_m\mathsf H_{\mathrm{rot}}}M_{b_m}1\rangle .
\end{split}
\tag{PR15}
\]
Coincident multiplication marks may first be combined. Operator-norm heat convergence is asserted at positive durations; at zero duration \(I-J_gJ_g^*\) has norm one.

## A central magnetic interaction of fixed strength survives

Set \(W(U)=2-\chi_{1/2}(U)\), so \(0\le W\le4\). For a fixed \(\lambda\ge0\), add the third-face interaction to the original Hamiltonian:
\[
\mathsf H_{g,\lambda}=\mathsf H_g+\lambda M_W,\qquad
\mathsf T_\lambda=\mathsf H_{\mathrm{rot}}+\lambda M_W
\quad\text{on }\mathcal H_{\mathrm{rot}}.
\tag{PR16}
\]
The central-spin decomposition is no longer preserved. Nevertheless, bounded perturbation of the already complete return is sufficient. Since \(M_WJ_g=J_gM_W\), a norm-convergent resolvent series at \(z>4\lambda\) applied to (PR11) proves
\[
\left\|(\mathsf K_g+\lambda M_W+z)^{-1}
-J_g(\mathsf T_\lambda+z)^{-1}J_g^*\right\|\longrightarrow0.
\tag{PR17}
\]
The resolvent identity extends this conclusion to every \(z>0\), since both operators are nonnegative. In particular the restored interaction has its original strength and source normalization.

The compact rotor has a unique positive vacuum \(v_\lambda\), of energy \(t_0(\lambda)\), and a strictly positive first gap. Spectral projections of the compact resolvents in (PR17) give
\[
E_\Omega(g,\lambda)-E_\Omega(g)\longrightarrow t_0(\lambda),
\qquad
\|\psi_{g,\lambda}-J_gv_\lambda\|\longrightarrow0,
\tag{PR18}
\]
with the positive normalized vacua fixing the phase. Subtracting these actual vacuum energies yields the corresponding heat and source-history return, with \(\mathsf T_\lambda-t_0(\lambda)\) and \(v_\lambda\). The complete finite-graph gap converges to that of this interacting rotor.

This corollary takes \(g\to\infty\) with \(\lambda\) fixed. It does not justify setting \(\lambda=g\) in the limit operator. Comparable confinement of all three faces changes the well and the surviving energy scale. Spatial assembly, volume-uniform innovation coercivity and the continuum Yang–Mills return remain separate requirements.
