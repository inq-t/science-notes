# Multiplication-Sensitive Cycle Preparations

Comparing left and right multiplication of one shared Gaussian preparation gives a nonconstant frame interaction at positive comparison strength, together with its complete conditional state. On tracial \(M_2(\mathbb C)\), both are explicit; sharing the preparation between two frames additionally couples their axes. The construction uses multiplication information absent from \(\mu\mu^\dagger\). It is a finite joint comparison law with declared preparation, frame measure and comparison strength. Turning these comparisons into graph holonomy cycles, selecting a physical clock and obtaining a four-dimensional gap remain separate tasks.

## One preparation supplies both comparison branches

Take \(V=M_2(\mathbb C)\), its ordinary multiplication \(\mu\), involution \(X\mapsto X^\dagger\), and the normalized trace pairing
\[
h(X,Y)=\tfrac12\operatorname{Tr}(X^\dagger Y).
\tag{MP1}
\]
Choose the compact frame group \(\mathcal U=U(2)\) with normalized Haar measure \(dU\). This is the full unitary group of this algebra; using it as a frame variable with a Haar prior is a declared rule. Choose a positive covariance \(G\) on the complex Hilbert space \(V\), and \(\beta\ge0\). The centered circular complex Gaussian preparation has
\[
dP_G(\xi)=\frac{e^{-\langle\xi,G^{-1}\xi\rangle}}{\det G}
\prod_{a=1}^4\frac{d^2\xi_a}{\pi},
\qquad \mathbb E_G[\xi\xi^\dagger]=G,
\tag{MP2}
\]
in any \(h\)-orthonormal coordinates. Covariances act on the four-dimensional amplitude space; they are not density matrices on the defining two-dimensional representation.

Both branches read the same \(\xi\):
\[
L_U\xi=\mu(U\otimes\xi)=U\xi,
\qquad R_U\xi=\mu(\xi\otimes U)=\xi U,
\qquad C_U=L_U-R_U.
\tag{MP3}
\]
The positive joint law is
\[
dP_\beta(U,\xi)=\mathcal Z_\beta^{-1}
e^{-\beta\|C_U\xi\|_h^2}\,dU\,dP_G(\xi).
\tag{MP4}
\]
Its normalization is finite and positive. Integration over the preparation and conditioning on the frame give, respectively,
\[
\boxed{
w_\beta(U)=\det(I+\beta C_UGC_U^\dagger)^{-1},
\qquad G_U=(G^{-1}+\beta C_U^\dagger C_U)^{-1}.}
\tag{MP5}
\]
Thus the frame marginal is \(\mathcal Z_\beta^{-1}w_\beta(U)dU\), where \(\mathcal Z_\beta=\int w_\beta(U)dU\); its conditional preparation is \(\mathcal N_{\mathbb C}(0,G_U)\). Completing the Gaussian square proves both formulas. Equivalently,
\[
G_U=G-\beta GC_U^\dagger
(I+\beta C_UGC_U^\dagger)^{-1}C_UG.
\tag{MP6}
\]
For \(\nu\) conditionally independent preparations sharing the same frame, the weight is \(w_\beta(U)^\nu\), with covariance \(G_U\) for each conditional copy.

The branch correlation is part of the law. With \(M_U=[L_U;R_U]\),
\[
\operatorname{Cov}\!\left(\binom{L_U\xi}{R_U\xi}\,\middle|\,U\right)
=M_UG_UM_U^\dagger.
\tag{MP7}
\]
Before tilting, replace \(G_U\) by \(G\). For \(G=I\), the prior block covariance is \(\left(\begin{smallmatrix}I&\operatorname{Ad}_U\\\operatorname{Ad}_{U^\dagger}&I\end{smallmatrix}\right)\), not a product of branch marginals. After integrating frames, the covariance is the frame-marginal average of (MP7); the resulting mixture need not be Gaussian.

## The tracial two-by-two member is explicit

The Pauli basis \(I,\sigma_1,\sigma_2,\sigma_3\) is orthonormal for (MP1). Write \(P_0\) and \(P_1\) for the scalar and traceless projections. A conjugation-invariant covariance has the form
\[
G=g_0P_0+gP_1,\qquad g_0,g>0.
\tag{MP8}
\]
Up to a central phase and conjugation, a unitary frame is \(U=\operatorname{diag}(e^{i\theta},e^{-i\theta})\). On matrix units, \(C_U E_{ij}=(U_{ii}-U_{jj})E_{ij}\). Therefore
\[
C_U^\dagger C_U
=4\sin^2\theta\,P_\perp,
\qquad P_\perp=P_{\operatorname{span}\{\sigma_1,\sigma_2\}},
\tag{MP9}
\]
and
\[
\boxed{
w_\beta(U)=(1+4\beta g\sin^2\theta)^{-2},
\quad
G_U=g_0P_0+gP_{\sigma_3}
+\frac{g}{1+4\beta g\sin^2\theta}P_\perp.}
\tag{MP10}
\]
The induced action \(-\log w_\beta\) has curvature \(16\beta g\) at \(\theta=0\). This is restoring curvature of the declared frame weight, not an excitation energy.

The formula is invariant under pairing-preserving \(*\)-automorphisms. Indeed, these send \(U\) to \(WUW^\dagger\), conjugate \(C_U\) on the amplitude carrier, preserve \(G\) in (MP8), and preserve Haar measure. The posterior transforms covariantly as well.

## Two frames interact through their shared preparation

Use independent Haar priors for \(U,V\), but the same \(\xi\), and tilt by \(\beta(\|C_U\xi\|^2+\|C_V\xi\|^2)\). The posterior precision is \(G^{-1}+\beta(C_U^\dagger C_U+C_V^\dagger C_V)\). Write their SU(2) representatives as
\[
U=\cos\theta\,I+i\sin\theta\,\mathbf n\cdot\boldsymbol\sigma,
\quad V=\cos\phi\,I+i\sin\phi\,\mathbf m\cdot\boldsymbol\sigma,
\]
and put \(p=4\beta g\sin^2\theta\), \(q=4\beta g\sin^2\phi\), \(c=\mathbf n\cdot\mathbf m\). The joint frame weight is
\[
\boxed{
w_\beta(U,V)
=\left[(1+p+q)\{1+p+q+pq(1-c^2)\}\right]^{-1}.}
\tag{MP11}
\]
To verify it, the traceless precision factor is \(sI-p\mathbf n\mathbf n^T-q\mathbf m\mathbf m^T\), with \(s=1+p+q\). The orthogonal direction has eigenvalue \(s\); the determinant on the remaining plane is \(s+pq(1-c^2)\). Continuity covers collinear axes.

For fixed noncentral frame angles and \(\beta>0\), the weight favors collinear axes. Independent preparations would instead give the product \((1+p)^{-2}(1+q)^{-2}\), with no relative-axis dependence. Nonparallel noncentral frames have no common traceless commutator kernel, although the scalar line remains untouched. These are properties of the actual two-frame joint law, not a graph or continuum rigidity theorem.

## A multiplication-dependent covariance is possible but not forced

For an \(h\)-orthonormal algebra basis \(\{e_a\}\), consider the constitutive rule
\[
K_{\rm ad}=\sum_a\operatorname{ad}(e_a)^\dagger\operatorname{ad}(e_a),
\qquad G_{\rm ad}=(I+K_{\rm ad})^{-1}.
\tag{MP12}
\]
Unitary changes of the orthonormal basis leave the sum unchanged; pairing-preserving algebra automorphisms transport it covariantly. The Pauli commutators \([\sigma_i,\sigma_j]=2i\epsilon_{ijk}\sigma_k\) give
\[
K_{\rm ad}=8P_1,
\qquad G_{\rm ad}=P_0+\tfrac19P_1
\quad\text{on tracial }M_2.
\tag{MP13}
\]
The coefficient uses \(h=\operatorname{Tr}/2\); with unnormalized Hilbert–Schmidt pairing it would be \(4\). Equation (MP10) then has \(g=1/9\). Symmetry alone allows every pair \(g_0,g>0\) in (MP8), so neither the chosen function \((I+K)^{-1}\) nor its scale is uniquely forced.

The full multiplication matters. Compare \(M_2\) above with \(\mathbb C^4\), coordinatewise multiplication and \(h(x,y)=\tfrac14\sum_i\bar x_i y_i\). Both have complex dimension four, \(\|1\|=1\), and
\[
\mu\mu^\dagger=4I.
\tag{MP14}
\]
For \(M_2\), use the basis \(\sqrt2 E_{ij}\); for \(\mathbb C^4\), use twice the coordinate idempotents. Their multiplication coefficients give (MP14) directly. But \(K_{\rm ad}=0\) and every commutator weight is one in \(\mathbb C^4\), whose full unitary group is \(U(1)^4\). Thus (MP5) and (MP12) distinguish multiplication tensors that their simple multiplication squares do not.

## Marks, presentation identities and the remaining physical return

For a specified readout insertion \(J:F\to V\), the readout is \(J^\dagger\xi\). Attach a Hermitian quadratic source \(T\) on \(F\) small enough to preserve positive precision. At fixed frame,
\[
w_U(T)=\mathbb E_G e^{-\beta\|C_U\xi\|^2-\langle\xi,JTJ^\dagger\xi\rangle},
\qquad
\boxed{\frac{w_U(T)}{w_U(0)}
=\det(I+T J^\dagger G_UJ)^{-1}.}
\tag{MP15}
\]
The same formula holds for the summed two-frame precision. [[closed-normalization-and-cosmic-response|Closed normalization and cosmic response]] owns the mixed-source consequence: differentiating this marked normalization recovers the entire response and its homogeneous variation, with the readout transport retained. If the prior covariance varies with that source, its normalization in (MP2) must also be differentiated; the expectation is relative to that preparation.

For two presentations of a fixed whole preparation, equal linear readout maps agree on every \(\xi\). Unit and reassociation relations can therefore give \(C=0\), weight one and unchanged preparation exactly. This supplies no new independent Gaussian variable. [[multiplication-reassociation-and-the-process-metric|The process-metric analysis]] explains why resetting an enlarged carrier's state or composing independent noisy transitions is a different requirement. Compatibility of the reference measures on genuinely different diagrams still needs proof.

The nonzero row \([U,\xi]\) compares two multiplication orders; commutativity is not an algebraic identity of \(M_2\). Calling it a cycle comparison does not construct a graph holonomy. Its relation to [[cycle-determinants-and-the-pure-gauge-return|the adjacency-based cycle law]] remains to be derived.

Every scalar preparation direction lies in the commutator kernel. Multiplying a frame by any central phase leaves its weight unchanged, so this law cannot distinguish the global frame group from its adjoint image through these comparisons alone. [[commutator-preparation-transfer-and-marked-gluing|The Gram transfer]] constructs its actual discrete path law and complete marked gluing. [[commutator-overlap-nullspace-and-angular-coverage|Its exact feature quotient]] also forgets inversion and fails to respect multiplication. Such unseen directions cannot simply be declared a physical quotient.

[[relative-multiplication-transfer-and-the-rotor-limit|Relative multiplication]] repairs the lost frame sectors. [[preparation-compression-and-the-returned-potential|Normalized preparation compression]] combines that repair with the commutator response and returns a specific potential and vacuum. Its independent preparation roles, covariance rule and duration remain declared inputs; a single-preparation alternative has a different unresolved refinement law. Neither construction yet supplies a four-dimensional Yang–Mills gap or a physical cosmological source.
