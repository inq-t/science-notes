# The Interacting Vacuum Has Full Support at the Balanced Cut

The actual two-plaquette \(SU(2)\) vacuum occupies every admissible trivalent boundary sector at every positive magnetic coupling. Its magnetic multiplication operators have nonnegative matrix elements in a canonical theta spin-network basis, and character fusion connects every basis vector to the constant vacuum. At the balanced three-boundary cut, each sector has multiplicity one, so these strictly positive coefficients give faithful reduced densities on both charged regional carriers. This proves the finite-system support condition; it supplies neither a uniform Schmidt bound nor a continuum mass gap.

## Keep the actual Hamiltonian and its canonical basis

Use the three-path presentation of [[coarse-response-memory/two-plaquette-vacuum-and-relational-state|the interacting two-plaquette system]]. Orient the left outer path \(p\), shared path \(s\), and right outer path \(q\) from the same vertex \(u\) to \(v\). With normalized Haar measure, \(G=SU(2)\), \(Q=-2\operatorname{Tr}\), and \(\kappa>0\),
\[
\begin{aligned}
\mathcal H_{\rm phys}&=L^2(G^3)^{G_u\times G_v}
\cong L^2(G^2)^{\operatorname{Ad}G},\\
x&=ps^{-1},\qquad y=qs^{-1},\\
H_\lambda&=D+2\lambda-\frac{\lambda}{2}B,\qquad
D=\kappa(3D_p+D_s+3D_q),\\
B&=M_{ps}+M_{qs},\qquad
M_{ps}=M_{\chi_{1/2}(ps^{-1})},\quad
M_{qs}=M_{\chi_{1/2}(qs^{-1})}.
\end{aligned}
\tag{IS1}
\]
Here \(\chi_{1/2}=\operatorname{Tr}\), so the potential is exactly \(\lambda(2-a-b)\) with \(a=\operatorname{Tr}x/2\), \(b=\operatorname{Tr}y/2\). The three path weights retain the original seven-link kinetic operator; no independent loop clock has been substituted.

For a spin \(j\in\frac12\mathbb N_0\), put \(d_j=2j+1\), \(C_j=j(j+1)\). An admissible triple \(\mathbf j=(j_p,j_s,j_q)\) obeys the triangle inequalities and \(j_p+j_s+j_q\in\mathbb Z\). Its diagonal-\(G\) invariant tensor space is one-dimensional. Choose a unit vector \(t_{\mathbf j}\) in it and set
\[
\begin{aligned}
\mathfrak d_{\mathbf j}&=d_{j_p}d_{j_s}d_{j_q},\\
\Psi_{\mathbf j}(p,s,q)
&=\sqrt{\mathfrak d_{\mathbf j}}\,
\left\langle t_{\mathbf j},
\bigl(D^{j_p}(p)\otimes D^{j_s}(s)\otimes D^{j_q}(q)\bigr)
t_{\mathbf j}\right\rangle .
\end{aligned}
\tag{IS2}
\]
The phase of \(t_{\mathbf j}\) cancels. Product Peter--Weyl orthogonality gives a complete orthonormal basis, with \(\Psi_{\mathbf0}=1\) and
\[
D\Psi_{\mathbf j}
=\kappa(3C_{j_p}+C_{j_s}+3C_{j_q})\Psi_{\mathbf j}.
\tag{IS3}
\]
This is the [[gauge-cycle-innovation-filtration/loop-coordinates-and-the-induced-clock|full theta electric spectrum]]. The normalized singlet identity gives
\(\chi_{1/2}(ps^{-1})=\Psi_{(1/2,1/2,0)}\), and similarly for \(qs^{-1}\).

## The two-vertex amplitude removes the recoupling sign

Write \(\varphi_{\mathbf j}=\Psi_{\mathbf j}/\sqrt{\mathfrak d_{\mathbf j}}\). For the loop label \(\boldsymbol\ell=(1/2,1/2,0)\), \(\varphi_{\mathbf j}\varphi_{\boldsymbol\ell}\) is the matrix coefficient of the tensor representation at the unit invariant vector \(t_{\mathbf j}\otimes t_{\boldsymbol\ell}\).

Decompose that representation orthogonally under \(G^3\), using \(V_j\otimes V_{1/2}=V_{j+1/2}\oplus V_{j-1/2}\), with negative spins omitted. Each output triple occurs at most once. Its projected vector \(v_{\mathbf j'}\) is still diagonal-\(G\) invariant, hence is zero or a scalar multiple of \(t_{\mathbf j'}\). Orthogonality of the representation blocks therefore gives
\[
\boxed{\;
\langle\Psi_{\mathbf j'},M_{ps}\Psi_{\mathbf j}\rangle
=\sqrt{\frac{4\mathfrak d_{\mathbf j}}{\mathfrak d_{\mathbf j'}}}
\,\|v_{\mathbf j'}\|^2\ge0.
\;}
\tag{IS4}
\]
The same proof applies to \(M_{qs}\). Both matrices are symmetric, since the loop characters are real. Thus \(B\) is a bounded self-adjoint operator, \(\|B\|\le4\), with nonnegative entries. The two vertices supply a squared recoupling amplitude; no sign choice for an isolated recoupling symbol is assumed.

The resulting adjacency graph is connected. To prove this without inspecting individual recoupling coefficients, fix \(j_p,j_q\). Let \(P_{j_s}\) be the orthogonal projection onto \(V_{j_s}\subset V_{j_p}\otimes V_{j_q}\). At \(s=1\), the invariant tensor in (IS2) is the normalized coevaluation of this Clebsch subspace, giving
\[
\Psi_{(j_p,j_s,j_q)}(p,1,q)
=\sqrt{\frac{d_{j_p}d_{j_q}}{d_{j_s}}}\,
\operatorname{Tr}\!\left[
P_{j_s}\bigl(D^{j_p}(p)\otimes D^{j_q}(q)\bigr)\right].
\tag{IS5}
\]
Summing the projections and restoring \(s\) by gauge invariance yields
\[
\boxed{\;
\chi_{j_p}(ps^{-1})\chi_{j_q}(qs^{-1})
=\sum_{j_s=|j_p-j_q|}^{j_p+j_q}
\sqrt{\frac{d_{j_s}}{d_{j_p}d_{j_q}}}\,
\Psi_{(j_p,j_s,j_q)}.
\;}
\tag{IS6}
\]
The sum advances in integer steps. Fundamental fusion gives
\(\chi_{1/2}^{\,2j}=\chi_j+\sum_{\ell<j}m_\ell\chi_\ell\), with nonnegative integer multiplicities. Lower outer spins cannot contribute to a target with outer labels \(j_p,j_q\). Consequently
\[
\left\langle\Psi_{(j_p,j_s,j_q)},
M_{ps}^{\,2j_p}M_{qs}^{\,2j_q}\Psi_{\mathbf0}\right\rangle
=\sqrt{\frac{d_{j_s}}{d_{j_p}d_{j_q}}}>0.
\tag{IS7}
\]
By (IS4), this positive matrix-product entry contains a path of positive adjacency entries from \(\mathbf0\) to the target. Every admissible triple is reached. For example, \(j_p=j_q=1/2\) gives coefficients \(1/2,\sqrt3/2\) in the \(j_s=0,1\) sectors.

## All sectors occur in the actual interacting vacuum

**Theorem.** For every fixed \(\kappa>0,\lambda>0\), choose the actual normalized ground amplitude \(\psi_\lambda\) to be positive in configuration space. Then
\[
\boxed{\quad
\psi_\lambda=\sum_{\mathbf j\ {\rm admissible}}
c_{\mathbf j}(\lambda)\Psi_{\mathbf j},
\qquad c_{\mathbf j}(\lambda)>0\ \text{for every }\mathbf j.
\quad}
\tag{IS8}
\]

For the proof, expand \(e^{-tH_\lambda}\) by bounded perturbation of the diagonal operator \(D\). Every time-ordered term has nonnegative matrix entries: its factors are positive diagonal \(e^{-rD}\) and the nonnegative matrix \((\lambda/2)B\). The series converges in operator norm by the bound \((t\lambda\|B\|/2)^n/n!\), with the common scalar \(e^{-2\lambda t}\). A positive adjacency path contributes a strictly positive time integral. Hence
\[
\langle\Psi_{\mathbf i},e^{-tH_\lambda}\Psi_{\mathbf j}\rangle>0
\qquad(t>0,\ \mathbf i,\mathbf j\ {\rm admissible}).
\tag{IS9}
\]

The actual compact elliptic system has a unique smooth strictly positive ground amplitude, as in the two-plaquette owner. Put \(E_\lambda=\inf\sigma(H_\lambda)\). Its overlap \(c_{\mathbf0}=\int\psi_\lambda\) is positive, and compact resolvent gives
\[
e^{tE_\lambda}e^{-tH_\lambda}\Psi_{\mathbf0}
\longrightarrow c_{\mathbf0}\psi_\lambda
\quad\text{in }\mathcal H_{\rm phys}\quad(t\to\infty).
\tag{IS10}
\]
The coefficientwise nonnegative cone is closed, so all \(c_{\mathbf j}\ge0\). Applying (IS9) to the ground-vector identity then gives
\(c_{\mathbf j}\ge e^{tE_\lambda}
\langle\Psi_{\mathbf j},e^{-tH_\lambda}\Psi_{\mathbf0}\rangle c_{\mathbf0}>0\).
This proves (IS8) for the actual vacuum. At \(\lambda=0\), only \(c_{\mathbf0}=1\) remains; pointwise positivity alone would not establish the positive-coupling conclusion.

## Return the coefficients to the balanced charged regions

Use [[regional-preparation-algebras-and-vacuum-support|the balanced cut and its charged Schmidt criterion]]. Subdivide \(s=s_1s_2\) at \(m\); assign \(A=(p,s_1)\), \(B=(q,s_2)\), and retain \(K=G_u\times G_v\times G_m\) before boundary Gauss sewing. Both regional carriers are \(L^2(G^2)\), with matching admissible boundary triples and multiplicity one. Under pure subdivision,
\[
\Omega_\lambda(p,s_1;q,s_2)
=\psi_\lambda\bigl(p(s_1s_2)^{-1},q(s_1s_2)^{-1}\bigr).
\tag{IS11}
\]
This is an isometric transport of the old vector, not a reconstruction of its state from the new edge inventory.

The triple \((j_p,j_s,j_q)\) labels the boundary representation with spins \((j_q,j_p,j_s)\) at \((u,v,m)\), with orientation duals understood. Its dimension is \(\mathfrak d_{\mathbf j}\). The transported normalized theta vector is the unique normalized boundary coevaluation in that sector, up to phase. The general charged partial-trace formula therefore becomes
\[
\boxed{\quad
\rho_A\simeq\rho_B\simeq
\bigoplus_{\mathbf j\ {\rm admissible}}
\frac{|c_{\mathbf j}(\lambda)|^2}{\mathfrak d_{\mathbf j}}\,
I_{\mathfrak d_{\mathbf j}}.
\quad}
\tag{IS12}
\]
Each eigenvalue has multiplicity \(\mathfrak d_{\mathbf j}\), and the traces equal \(\sum_{\mathbf j}|c_{\mathbf j}|^2=1\). Equation (IS8) gives zero kernels on both complete regional carriers. Thus the actual transported vacuum is cyclic and separating for both proper charged factors \(B(\mathcal H_A)\otimes I\) and \(I\otimes B(\mathcal H_B)\).

This conclusion concerns the balanced cut; the asymmetric four-link/three-link cut still has the exact multiplicity obstruction proved in the regional owner. The full physical carrier is an invariant subspace of the charged tensor product. Charged operators need not individually preserve it, and the descended boundary-preserving algebras remain abelian in this multiplicity-one example.

## The same physical clock becomes a fusion-index Markov clock

Set \(h_{\mathbf j}=c_{\mathbf j}(\lambda)>0\), \(\pi_{\mathbf j}=h_{\mathbf j}^2\), and \(B_{\mathbf j\mathbf l}=\langle\Psi_{\mathbf j},B\Psi_{\mathbf l}\rangle\). The unitary
\[
\mathcal U:\ell^2(\pi)\longrightarrow\mathcal H_{\rm phys},
\qquad
\mathcal U f=\sum_{\mathbf j}h_{\mathbf j}f_{\mathbf j}\Psi_{\mathbf j}
\tag{IS13}
\]
sends \(1\) to the actual vacuum. Its centered positive generator and Dirichlet form are
\[
\begin{aligned}
(\mathcal L f)_{\mathbf j}
&=\bigl[\mathcal U^*(H_\lambda-E_\lambda)\mathcal U f\bigr]_{\mathbf j}\\
&=\frac{\lambda}{2}\sum_{\mathbf l}
B_{\mathbf j\mathbf l}\frac{h_{\mathbf l}}{h_{\mathbf j}}
(f_{\mathbf j}-f_{\mathbf l}),\\
\langle f,\mathcal Lf\rangle_{\pi}
&=\frac{\lambda}{4}\sum_{\mathbf j,\mathbf l}
B_{\mathbf j\mathbf l}h_{\mathbf j}h_{\mathbf l}
|f_{\mathbf j}-f_{\mathbf l}|^2 .
\end{aligned}
\tag{IS14}
\]
The ground equation gives the first identity; symmetry of \(B\) gives the second. Each row has finitely many neighbors. These formulas hold initially on finitely supported functions, an operator core because \(D\) is diagonal and \(B\) bounded; their closures specify the full operator and form.

More directly, its heat transition matrix is
\[
P_t(\mathbf j,\mathbf l)
=e^{tE_\lambda}\frac{h_{\mathbf l}}{h_{\mathbf j}}
\langle\Psi_{\mathbf j},e^{-tH_\lambda}\Psi_{\mathbf l}\rangle .
\tag{IS15}
\]
It is nonnegative, has row sums one by the ground-vector identity, and satisfies detailed balance with \(\pi\). Thus it is an exact conservative reversible Markov realization, unitarily equivalent to the same full centered TP Hamiltonian. In particular any gap estimate for this complete fusion-index clock is an estimate for that physical operator.

The configuration ground-transform state \(|\psi_\lambda(x,y)|^2dx\,dy\) and the coefficient state \(\pi_{\mathbf j}\) are different probability representations. A [[prepared-readout-algebra-and-physical-source-completeness|prepared physical multiplication source]] \(M_F\) must become \(\mathcal U^*M_F\mathcal U\); it is generally not diagonal in the fusion index. Replacing it by an arbitrary diagonal probe would change the experiment. At \(\lambda=0\), the coefficient vacuum has support only at \(\mathbf0\), and (IS13) no longer supplies a unitary on the full physical carrier.

Faithful trace-class densities in infinite dimension have eigenvalues approaching zero. Equation (IS12) gives no uniform lower Schmidt bound, estimate on modular logarithms, or [[physical-response-coercivity/conditional-vacuum-rigidity-and-the-physical-gap|uniform complete-source gap bound]]. Their type-I modular flow remains [[modular-recurrence-and-the-regional-limit|strongly recurrent]], so full support does not produce a proper exact half-sided modular inclusion at this regulator. The all-sector argument uses this \(SU(2)\) trivalent presentation and its two fundamental magnetic loops; extension to higher multiplicities, general graphs, other groups and a common continuum regional limit remains open.
