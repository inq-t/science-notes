# Bosonic SU(2) Yang–Mills Matrix Model

The standard bosonic \(SU(2)\) Yang–Mills matrix model has unbounded commuting valleys, but its quantum kinetic form penalizes transverse localization strongly enough to give compact resolvent. This note gives a self-contained version of that established confinement mechanism and connects it to the workspace's transgression-selected potential. Its unique positive ground state is gauge invariant, and the complete homogeneous invariant carrier has a positive excitation gap. The model is a quantum-mechanical truncation, not a new four-dimensional gauge theory; its gap scales with the supplied quantization and volume parameters.

The [[compact-lie-gauge-positive-realization|compact-Lie extension]] owns the general adjoint-trace proof for every compact semisimple algebra and \(d\geq2\). This note retains the explicit determinant member, its orientation loss, quantum response and pure-gauge cancellation test. The finite mechanism does not select \(SU(2)\) or three dimensions.

## The same potential on the actual matrix carrier

In the [[chern-simons-response-and-gauge-action|homogeneous transgression member]], the configuration is a real matrix with three Lie-algebra rows,

\[
Q=(a_1,a_2,a_3)\in(\mathbb R^3)^3,
\qquad [a_i,a_j]=a_i\times a_j.
\tag{HG1}
\]

The Lie metric is normalized so that these are ordinary Euclidean norms and the bracket is the displayed cross product. Initially set the supplied spatial volume to one. Then

\[
W_{\rm CS}(Q)=\det Q,
\qquad
\frac12|\nabla W_{\rm CS}|^2
=V(Q):=\frac12\sum_{i<j}|a_i\times a_j|^2.
\tag{HG2}
\]

This uses all nine coordinates, not a diagonal three-coordinate ansatz or a singular gauge quotient. The potential vanishes whenever all three vectors are parallel, including arbitrarily large configurations. Ordinary pointwise coercivity \(V(Q)\to\infty\) therefore fails.

Choose \(\epsilon>0\), still an abstract quantization parameter, and the canonical kinetic law on \(L^2(\mathbb R^9,dQ)\):

\[
K_\epsilon=-\frac{\epsilon^2}{2}\sum_{i=1}^3\Delta_{a_i},
\qquad H_\epsilon=K_\epsilon+V.
\tag{HG3}
\]

More precisely, begin with the nonnegative form
\(\mathfrak h_\epsilon[u]=\epsilon^2\|\nabla u\|_2^2/2+\|V^{1/2}u\|_2^2\).
Its domain is \(H^1(\mathbb R^9)\cap L^2(V\,dQ)\), it is closed, and \(C_c^\infty\) is a form core. The associated self-adjoint operator is the Friedrichs realization in (HG3). The metric, measure and kinetic coefficient are explicit inputs; the positive form and potential then fix this operator without supplying a vacuum separately.

## The valleys carry a transverse cost

On the form core, define three partial operators

\[
T_i=-\frac{\epsilon^2}{2}\sum_{j\ne i}\Delta_{a_j}
+\frac12\sum_{j\ne i}|a_i\times a_j|^2.
\tag{HG4}
\]

Fix \(a_i\), with \(r=|a_i|>0\). Decompose each other vector into two components perpendicular to \(a_i\) and one parallel component. Its contribution is a two-dimensional harmonic oscillator of frequency \(r\), plus a nonnegative free longitudinal kinetic term. Each perpendicular coordinate contributes ground energy \(\epsilon r/2\), so each of the two other vectors contributes at least \(\epsilon r\). At \(r=0\), the resulting inequality still holds by nonnegativity. Integration over the fixed vector proves the quadratic-form bound

\[
T_i\geq2\epsilon|a_i|.
\tag{HG5}
\]

This is a fiberwise inequality, not an approximation that freezes fluctuations in the actual state. No differentiable choice of the perpendicular frame is needed because \(T_i\) contains no derivatives in \(a_i\).

Every kinetic term and pair potential occurs twice in the sum, hence

\[
\sum_iT_i=2H_\epsilon,
\qquad
H_\epsilon\geq\epsilon\sum_i|a_i|.
\tag{HG6}
\]

Since also \(H_\epsilon\geq K_\epsilon\), averaging the two bounds gives

\[
\boxed{
H_\epsilon\geq\frac12K_\epsilon
+\frac\epsilon2\sum_i|a_i|.}
\tag{HG7}
\]

All inequalities extend from the core to the closed form domain. This is the confinement mechanism: a tube around a commuting valley can have small magnetic potential, but narrowing the transverse wavefunction costs kinetic energy. The transverse oscillator bound charges that combined cost without inserting a quadratic mass potential.

## Compactness, the vacuum and the gauge-invariant gap

The [[compact-lie-gauge-positive-realization#Compactness selects a genuine vacuum and centered gap|shared compactness argument]] applies to (HG7): the derivative bound and linear tail moment give compact embedding of the form domain, and the positive heat kernel gives a unique smooth positive normalized ground state \(\psi_0\). Thus \(H_\epsilon\) has compact resolvent and a simple lowest eigenvalue satisfying

\[
E_0(\epsilon)>0.
\tag{HG8}
\]

Indeed a zero eigenvector would have zero kinetic form, hence be constant on \(\mathbb R^9\), which is impossible for a nonzero \(L^2\) vector.

Global gauge transformations act by simultaneous \(SO(3)\) rotations of the three Lie-algebra vectors. This is the adjoint action of \(SU(2)\); its center acts trivially. The measure, kinetic form and potential are invariant, so the gauge-average projection commutes with \(H_\epsilon\). Uniqueness and positivity force \(\psi_0\) to be gauge invariant. Restriction to

\[
\mathcal H_{\rm inv}=L^2(\mathbb R^9)^{SO(3)}
\tag{HG9}
\]

therefore preserves the ground state and compact resolvent. This carrier is infinite dimensional: it contains arbitrarily many independent smooth radial functions. Its first eigenvalue above \(E_0\) consequently exists, and

\[
\boxed{
\Delta_{\rm inv}(\epsilon)
:=E_{1,\rm inv}(\epsilon)-E_0(\epsilon)>0.}
\tag{HG10}
\]

No numerical value of this gap is asserted. In particular, the coordinate-dependent bound (HG6) is not a numerical excitation gap after subtracting the vacuum energy. The nonnegative vacuum-normalized operator is \(H_\epsilon-E_0\), not the unshifted operator with an assumed zero-energy state.

A numerical reduction must preserve this carrier. The Gram matrix
\(G_{ij}=a_i\cdot a_j\) determines a full-rank triple only up to
\(O(3)\), whereas the gauge action in (HG9) is \(SO(3)\).
Triples related by an improper orthogonal transformation have the same
Gram matrix and opposite \(\det Q\). For example,
\((\det Q)e^{-\operatorname{Tr}G}\) is a square-integrable gauge-invariant
function that cannot be represented by a function of \(G\) alone.
A Gram-only computation therefore selects the orientation-even sector
unless it also retains the determinant branch, with
\((\det Q)^2=\det G\), and the induced measure and boundary conditions.
An absolute ground energy, a scalar-sector excitation and the full
gauge-invariant centered gap must not be compared as the same number.

Self-adjoint functional calculus then supplies the strongly continuous
unitary group \(e^{-it(H_\epsilon-E_0)/\epsilon}\) on the invariant carrier.
Its rate generator is \((H_\epsilon-E_0)/\epsilon\). This is a clock
realization under the declared quantization convention, not an
identification of \(t\) with the signed normal parameter or a derivation
of physical duration. The transverse bound is a statement about functions
and their derivative norms; it does not posit random kicks in a vacuum.

The [[algebra/response-factorization-and-the-vacuum|factored-response theorem]] explains the failed shortcut. Here \(\Delta_Q\det Q=0\), so the Chern–Simons exponential is a formal zero-mode solution. But it grows on an open cone and is not normalizable. It cannot be \(\psi_0\); (HG8) independently confirms that no normalizable zero mode exists. The actual positive state is selected by the closed operator. Its logarithm \(W_0=-\epsilon\log\psi_0\) satisfies

\[
V-E_0=\frac12|\nabla W_0|^2-\frac\epsilon2\Delta_QW_0,
\tag{HG11}
\]

but this is the quantum response of the constructed vacuum, not a claim that \(W_0=\det Q\) or that its Hessian equals the modulus of the transgression Hessian.

The [[quantum-response-regularity-at-the-gauge-origin|origin regularity theorem]] sharpens this distinction. No \(C^3\) classical squared-response function can have a minimum at this nonzero quartic origin, while the actual smooth \(W_0\) has \(\operatorname{Hess}W_0(0)=2E_0I_9/(9\epsilon)>0\) at unit volume and zero potential offset. This coefficient uses the ground energy above the potential minimum, not the excitation gap; it is local stiffness, not global convexity.

There is also an exact orientation loss. Set
\(\mathcal D_\pm=\epsilon d\pm dW_{\rm CS}\), acting from scalar functions to one-forms. Harmonicity of \(W_{\rm CS}\) cancels the divergence term for either sign, so

\[
\boxed{
\frac12\mathcal D_+^*\mathcal D_+
=\frac12\mathcal D_-^*\mathcal D_-
=H_\epsilon.}
\tag{HG11a}
\]

The equality holds first on the smooth core and then for the identical closed scalar forms. Neither formal exponential \(e^{\mp W_{\rm CS}/\epsilon}\) is normalizable: each grows on the opposite determinant cone. Thus both signs select the same actual positive ground state and gap. A positive realization need not first replace the signed Hessian by a positive one, but this squared-response realization has forgotten the sign; it has not selected physical chirality or a directed clock. With volume restored, \(g=\mathcal V I\), \(W_{\rm CS}=\mathcal V\det Q\), and \(\Delta_gW_{\rm CS}=0\), the same equality holds with the same metric in both adjoints.

## The scale and the truncation remain visible

Because \(V\) is homogeneous of degree four, the unitary dilation
\((\mathcal U_\epsilon u)(X)=\epsilon^{3/2}u(\epsilon^{1/3}X)\)
gives

\[
\mathcal U_\epsilon H_\epsilon\mathcal U_\epsilon^{-1}
=\epsilon^{4/3}H_1.
\tag{HG12}
\]

It commutes with gauge rotations, so all invariant eigenvalues, including the shifted excitation gap, scale by \(\epsilon^{4/3}\).

Restoring exactly the volume convention of the transgression member,

\[
H_{\epsilon,\mathcal V}
=-\frac{\epsilon^2}{2\mathcal V}\Delta_Q+\mathcal V V(Q)
=\mathcal V H_{\epsilon/\mathcal V,1},
\]
\[
\boxed{
\Delta_{\rm inv}(\epsilon,\mathcal V)
=\epsilon^{4/3}\mathcal V^{-1/3}\Delta_{\rm inv}(1,1).}
\tag{HG13}
\]

Thus this model's gap is positive at every fixed normalization but is not uniform as \(\mathcal V\to\infty\) with \(\epsilon\) fixed. The equation supplies a scaling law, not a predicted physical yardstick.

The construction quantizes a homogeneous mechanical truncation, not all spatial connections. Global rotations are its gauge redundancy; arbitrary spatially varying gauge transformations do not preserve the ansatz. Nor has its Hilbert space been proved to be a reducing sector of the interacting field Hamiltonian. Consequently neither its positive finite gap nor its volume scaling can be transferred to the full Yang–Mills theory without another theorem.

## Historical placement and the small-volume convention

[Barry Simon's 1983 paper](https://authors.library.caltech.edu/records/4ahvp-yy937)
is a general precedent for discrete quantum spectra despite classically
open escape directions. The proof here is an instance of that mechanism,
not a claim to have discovered quantum confinement of flat valleys.

The torus zero-mode problem belongs to
[Lüscher's 1983 small-volume analysis](https://doi.org/10.1016/0550-3213(83)90436-4)
and [Lüscher–Münster's 1984 weak-coupling calculation](https://doi.org/10.1016/0550-3213(84)90038-5).
[Van Baal's review, section 3](https://arxiv.org/html/hep-ph/0008206),
displays the corrected effective Hamiltonian in equation (9). Its leading
two terms, before the listed corrections, have the convention
\[
H_{\rm lead}=\frac1L\left[-\frac{g^2}{2}\Delta_c+
\frac{V(c)}{g^2}\right]
=\frac1{g^2L}H_{\epsilon=g^2,\mathcal V=1}
\simeq\frac{g^{2/3}}L H_1.
\tag{HG13a}
\]
The last relation is the unitary dilation already proved in (HG12).
Thus the fractional-power small-volume scaling is compatible with
(HG13); it is not a distinct prediction of the response interpretation.
The coupling runs with \(L\) in the field theory. Its effective
corrections and field-space boundary identifications are absent from
the bare matrix operator on \(\mathbb R^9\).

The same review explains that relevant winding-number tunnelling paths
can leave the zero-momentum sector. Its finite-volume programme therefore
supplies context and additional obligations, not an equivalence between
this truncation and all Yang–Mills dynamics or a theorem reducing Clay
to one sphaleron calculation. A literature number requires a separate
match of normalization, symmetry sector and vacuum subtraction before it
can be assigned to \(\Delta_{\rm inv}(1,1)\).

[De Wit, Lüscher and Nicolai (1989)](https://doi.org/10.1016/0550-3213(89)90214-9)
provide a distinct supersymmetric matrix-Hamiltonian comparison with
continuous spectrum. That is not the bosonic operator proved discrete
here; its result must not be used as though the carrier and Hamiltonian
were unchanged.

## Spatial derivatives can cancel the matrix potential

The oscillator estimate cannot simply be applied to an independent matrix triple at every spatial point. With the convention
\(F_{ij}=\partial_iA_j-\partial_jA_i+[A_i,A_j]\), derivatives and commutators can cancel exactly. On a flat three-torus, take smooth periodic real functions \(f(x),h(y)\), orthonormal generators \(T_1,T_2,T_3\) with \([T_1,T_2]=T_3\), and

\[
g(x,y)=e^{f(x)T_1}e^{h(y)T_2},\qquad A=g^{-1}dg.
\tag{HG14}
\]

For example, \(f(x)=\sin x\), \(h(y)=\sin y\) give a globally smooth periodic gauge transformation on the torus of period \(2\pi\). Its components are

\[
A_x=f'(x)\operatorname{Ad}_{e^{-h(y)T_2}}T_1,
\qquad A_y=h'(y)T_2,\qquad A_z=0.
\tag{HG15}
\]

Direct differentiation gives

\[
\partial_yA_x=[A_x,A_y],\qquad
F_{xy}=0,\qquad
|[A_x,A_y]|=|f'(x)h'(y)|.
\tag{HG16}
\]

All other curvature components also vanish. Nevertheless the commutator is nonzero on an open set in the displayed example. Thus no constant \(c>0\) can satisfy
\(\|F\|_{L^2}^2\geq c\int\sum_{i<j}|[A_i,A_j]|^2\)
on all smooth representatives. Every connection in this example is gauge equivalent to zero; the pointwise commutator is not itself a local gauge invariant.

This does not exclude a field-theoretic gap or a gauge-fixed conditional estimate. It identifies the missing structure in extending (HG4)–(HG7): the response and kinetic comparison must respect local gauge reduction and [[gauge-boundary-frame-gluing/inq|boundary-frame gluing]], rather than treat spatial points as independent homogeneous carriers. The full curvature potential does not contain the homogeneous commutator potential as a separately controlled positive contribution.

What has been gained is a genuine positive interacting matrix realization of the same selected magnetic potential, including an actual vacuum and a complete invariant excitation spectrum. Infinite spatial modes, local observable reconstruction, physical calibration and the required continuum-uniform mass gap remain separate obligations.

[[nonlinear_response_receipt.py|The finite receipt]] verifies oscillator
multiplicities, dilation factors and the pure-gauge cancellation. The form compactness, positivity and
spectral arguments above establish the infinite-dimensional matrix-state
claims; those claims are not inferred from numerical diagonalization.
