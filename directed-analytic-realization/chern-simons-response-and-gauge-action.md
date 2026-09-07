# Chern–Simons Response and the Gauge Action

Chern–Simons transgression on a supplied oriented three-dimensional geometry has gradient \(*F_A\). Its squared norm is precisely the interacting magnetic Yang–Mills potential. A declared canonical kinetic pairing and temporal gauge prescription then return the local classical \(3+1\)-dimensional action. This response is signed, however: its instanton relation is not positive vacuum preparation, and its exponential does not provide the required quantum ground state. The classical return is exact; quantum existence and a uniform physical mass gap remain separate construction problems.

## The three-dimensional response

Let \(\Sigma\) be a closed oriented Riemannian three-manifold, \(G\) a compact Lie group, and \(\langle\, ,\,\rangle\) a positive invariant inner product on its Lie algebra. Work with smooth connections in a fixed trivialization. The formula below is an ordinary real functional on this presentation space; descent under large gauge transformations requires separate care.

Use the form bracket convention

\[
F_A=dA+\frac12[A,A],\qquad d_A=d+[A,\,\cdot\,],
\qquad
W_{\rm CS}(A)
=\frac12\int_\Sigma\langle A\wedge dA\rangle
+\frac16\int_\Sigma\langle A\wedge[A,A]\rangle.
\tag{CG1}
\]

This normalization differs from the characteristic-number normalization in [[knotting-as-dimensional-presentation/inq|the three-to-four transgression discussion]]. The associated three-form has exterior derivative \(\frac12\langle F\wedge F\rangle\) on a four-dimensional extension.

On the closed three-manifold, integration by parts makes the two variations of the quadratic term equal. Invariance of the Lie pairing makes the three variations of the cubic term equal. Consequently

\[
dW_{\rm CS}(A)[a]
=\int_\Sigma\langle a\wedge F_A\rangle,
\qquad
N(A):=\operatorname{grad}_{L^2}W_{\rm CS}(A)=*F_A,
\tag{CG2}
\]

where \((a,b)=\int_\Sigma\langle a\wedge*b\rangle\). In particular,

\[
\boxed{\frac12\|N(A)\|^2=\frac12\|F_A\|^2.}
\tag{CG3}
\]

The bracket in \(F_A\) supplies the nonlinear interaction. No quadratic approximation has been taken. This is a gradient response on connection space, not yet the positive Dirichlet-to-Neumann map of a minimizing boundary problem.

For an infinitesimal gauge variation \(a=d_A\epsilon\), Bianchi gives

\[
dW_{\rm CS}[d_A\epsilon]=0,\qquad
d_A^*N=-*d_AF_A=0.
\tag{CG4}
\]

Thus the response is horizontal to gauge orbits. For finite gauge transformations it is equivariant, and its squared norm is invariant. The functional itself can change by a convention-dependent period under large gauge transformations; a real single-valued \(e^{-W_{\rm CS}/\epsilon}\) need not descend to the full gauge quotient, for any supplied \(\epsilon>0\).

## The canonical prescription returns the local gauge action

Introduce an independent momentum \(E\), a clock parameter \(t\), and a temporal connection \(A_0\). Use the same Lie pairing in the kinetic and magnetic terms:

\[
S_{\rm can}
=\int dt\left[
(E,\dot A-d_AA_0)
-\frac12\|E\|^2-\frac12\|N(A)\|^2
\right].
\tag{CG5}
\]

These are explicit realization inputs. The Chern–Simons functional alone does not supply a clock or the canonical kinetic pairing. An overall gauge coupling can be incorporated in the common inner product; it is not predicted here.

Variation of \(A_0\) and then \(E\) gives

\[
d_A^*E=0,\qquad E=\dot A-d_AA_0.
\tag{CG6}
\]

Gauge invariance of a Hamiltonian conserves its gauge moment map; it does not by itself choose the zero-charge constraint. Here that choice follows from treating time-dependent gauge transformations as redundancy through the multiplier \(A_0\). The [[gauge-boundary-frame-gluing/inq|Gauss-gluing construction]] likewise imposes the diagonal constraint only after retaining the charged regional presentations.

Eliminating \(E\) in (CG5) and using (CG3) gives

\[
\boxed{
S[A,A_0]=\frac12\int dt\left[
\|\dot A-d_AA_0\|^2-\|F_A\|^2
\right].}
\tag{CG7}
\]

This is the local classical Yang–Mills action for the product Lorentzian metric \(-dt^2+g_\Sigma\), in units with limiting speed one. The three-dimensional transgression determines its magnetic potential; the specified phase pairing determines its kinetic term. Unlike defining a boundary functional by first minimizing a chosen Yang–Mills action, this calculation starts with transgression. It nevertheless supplies the group, connection carrier, metric and canonical prescription rather than deriving them from necessity.

The [[algebra/cauchy-response-and-local-action|opposed-Cauchy construction]] returned a free local action from a squared linear response. The [[algebra/nonlinear-response-and-clock-realization|nonlinear response theorem]] separates this classical prescription from quantum realization. Equation (CG7) supplies its gauge counterpart at the classical-action level, not a construction of its quantum Hilbert space or vacuum.

## Signed instanton response is not a positive normal semigroup

For a smooth Euclidean path in temporal gauge, completing the square yields

\[
\frac12\int d\tau\left(\|\dot A\|^2+\|N(A)\|^2\right)
=\frac12\int d\tau\,\|\dot A\mp N(A)\|^2
\ \pm\left[W_{\rm CS}(A)\right]_{\rm endpoints}.
\tag{CG8}
\]

The endpoint difference is evaluated on the chosen path lift. With product orientation \(d\tau\wedge\operatorname{vol}_\Sigma\), the equations

\[
\partial_\tau A=\pm*F_A
\tag{CG9}
\]

are the self-dual and anti-self-dual conditions. They select special Euclidean trajectories, not all solutions of a boundary-value problem.

At the trivial flat connection,

\[
DN=*d.
\tag{CG10}
\]

On nonzero transverse Fourier modes of a flat three-torus, this curl operator has eigenvalues \(+|p|\) and \(-|p|\). Either sign in (CG9) therefore has arbitrarily rapidly growing linearized modes. It does not define a bounded forward semigroup on the usual Sobolev completion, much less a positive contractive preparation law.

After treating gauge and harmonic zero modes separately, the decaying free response is instead \(|\operatorname{curl}|\), with positive quadratic functional
\(\frac12(a,|\operatorname{curl}|a)\). Squaring that nonlocal linear response recovers the local magnetic form. Extending this replacement nonlinearly is a new integrability problem: [[algebra/absolute-hessian-and-response-integrability|the absolute-Hessian obstruction]] shows that even the homogeneous example below does not permit simply replacing its Hessian by its absolute value.

The [[cubic-gauge-boundary-response-and-gauss-completion|cubic boundary construction]] supplies an actual nonlinear extension of this positive free response on spatial Fourier-polynomial connections. It satisfies both the squared-response equation and the infinitesimal gauge identity. Gauss law forces longitudinal terms whose norm becomes a Coulomb energy at quartic order; harmonic modes prevent continuing the chosen cubic prescription by a frequency denominator alone. This is coefficient-level field progress, not a global positive vacuum construction.

## A finite homogeneous \(SU(2)\) test

Take a flat three-torus of volume \(\mathcal V\), with orthonormal generators obeying \([T_a,T_b]=\epsilon_{abc}T_c\), and constant connections

\[
A_i=\sum_aQ_{ia}T_a,\qquad Q\in M_3(\mathbb R).
\]

The induced \(L^2\) metric on these coordinates is
\(\mathcal V\operatorname{Tr}(dQ^T dQ)\). The six terms in the cubic three-form give

\[
W_{\rm CS}(Q)=\mathcal V\det Q,\qquad
N(Q)=\operatorname{cof}Q,\qquad
V_{\rm mag}(Q)=\frac{\mathcal V}{2}\|\operatorname{cof}Q\|_{\rm F}^2.
\tag{CG11}
\]

The cofactor is the gradient in this induced metric, not the unscaled Euclidean gradient of \(\mathcal V\det Q\). For \(Q=\operatorname{diag}(x,y,z)\), the formulas become \(W=\mathcal Vxyz\), \(N=\operatorname{diag}(yz,xz,xy)\), and
\[
V_{\rm mag}=\frac{\mathcal V}{2}
(x^2y^2+y^2z^2+z^2x^2).
\]

At \(Q=qI\),

\[
DN[B]=q\left(\operatorname{tr}B\,I-B^T\right).
\tag{CG12}
\]

Its eigenvalues are \(2q\) on scalar matrices, \(-q\) on symmetric tracefree matrices, and \(q\) on antisymmetric matrices. For \(q\ne0\), homogeneous gauge-horizontal variations satisfy \(\sum_i[A_i,B_i]=0\), equivalently \(B=B^T\). The Hessian remains indefinite on that horizontal space. This is a finite-dimensional restriction used to test the response, not an identification of the homogeneous coordinates with the complete physical gauge quotient.

## The quantum correction and the vacuum obstruction

For a finite-dimensional Riemannian configuration space, let \(\Delta=\operatorname{div}\nabla\), and suppose a differential Hamiltonian and a smooth real functional are specified:

\[
H=-\frac{\epsilon^2}{2}\Delta+V,\qquad
N=\nabla W,\qquad \psi=e^{-W/\epsilon}.
\]

The parameter \(\epsilon>0\) is an abstract quantization input, not derived from transgression. Any identification with physical Planck action requires a further calibration. The [[algebra/response-factorization-and-the-vacuum|response-factorization theorem]] specifies the corresponding domains, reference measure and vacuum conditions. Direct differentiation gives

\[
\frac{H\psi}{\psi}
=V-\frac12\|N\|^2+\frac{\epsilon}{2}\operatorname{div}N.
\tag{CG13}
\]

An actual ground state at energy \(E_0\) must therefore satisfy
\[
V-E_0=\frac12\|N\|^2-\frac{\epsilon}{2}\operatorname{div}N,
\]
together with positivity, the Hilbert-space domain and normalizability. The classical squared-response identity omits the divergence term.

For (CG11), \(\det Q\) is harmonic in its nine entries. Thus
\[
H_{\rm hom}
=-\frac{\epsilon^2}{2\mathcal V}\Delta_Q
+\frac{\mathcal V}{2}\|\operatorname{cof}Q\|_{\rm F}^2
\]
formally annihilates \(e^{-\mathcal V\det Q/\epsilon}\). But this function grows exponentially in cubic radius on an open cone where \(\det Q<0\), and is not in \(L^2(M_3(\mathbb R))\). The formal identity therefore identifies neither a ground state nor its energy, and says nothing by itself about the actual spectral gap.

Nevertheless, [[homogeneous-gauge-positive-realization|the separate positive homogeneous realization]] proves that this same canonical operator has compact resolvent, a unique positive gauge-invariant ground state and a positive complete invariant excitation gap. It uses the closed kinetic-plus-potential form, not the Chern–Simons exponential. Its gap scales as \(\epsilon^{4/3}\mathcal V^{-1/3}\), so it is not volume uniform; the homogeneous truncation is not an established reducing sector of the full field theory.

In [[vacuum-aligned-innovation-completion/boundary-action-fixed-points-and-physical-linearization|the existing boundary-action construction]], the dimensionless fixed action is \(V_*=-2\log\psi\), so the functional in (CG13) would be \(W=\epsilon V_*/2\). That construction starts with a specified positive transfer. Its finite-spacing logarithm is not automatically the differential Hamiltonian assumed in (CG13).

The classical interaction has now been returned from a three-dimensional response, and a positive quantum member exists at the homogeneous truncation. For the full spatial field, what remains is a positive, gauge-compatible quantum boundary law with the correct same-carrier physical dynamics, continuum existence and a uniform mass edge. Neither signed transgression nor the formal exponential has supplied those missing data.
