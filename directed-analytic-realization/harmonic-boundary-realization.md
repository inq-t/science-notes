# An Oriented Harmonic Boundary Selects Its Clock

An oriented metric disk relates two different operations on its boundary data: inward harmonic smoothing and reversible tangential translation. Its Dirichlet-to-Neumann response determines a positive generator, while the orientation determines the complex structure that turns tangential translation into Schrödinger evolution. The same quadratic response is the trace of a Hardy multiplication defect. This supplies a geometric origin for the analytic member's polarization and response-to-clock relation, relative to a specified disk; it does not derive that disk as physical spacetime.

## Begin with real boundary geometry

The primitive datum here is an oriented Euclidean disk \(B_R\), its metric boundary measure, and the law assigning a harmonic interior to real boundary data. The disk is a mathematical presentation domain, not a proposed spatial cross-section of the universe.

Write \(x=R\theta\), and equip real \(L^2(S^1_R)\) with

\[
(f,g)_R=\frac1{2\pi R}\int_{\partial B_R}fg\,dx.
\tag{HB1}
\]

On the mean-zero subspace \(\mathcal V_0\), define

\[
D=\partial_x,\qquad
A=(-D^2)^{1/2},\qquad
J=-DA^{-1}.
\tag{HB2}
\]

\(D\) is the skew-adjoint periodic derivative and \(A\) is positive self-adjoint, both with domain \(H^1\cap\mathcal V_0\). The mean-zero circle has \(A\geq R^{-1}\), so the displayed inverse is bounded here. On Fourier pairs,

\[
J\cos(n\theta)=\sin(n\theta),\qquad
J\sin(n\theta)=-\cos(n\theta).
\tag{HB3}
\]

It follows directly that

\[
J^*=-J,\qquad J^2=-1,\qquad D=-JA.
\tag{HB4}
\]

Thus orientation, positive modulus and complex structure are related, not three separately fitted operators. Reversing the boundary orientation sends \(D,J\) to \(-D,-J\), leaving \(A\) unchanged. The underlying unoriented metric does not choose a preferred sheet.

The same structural distinction appears in [[contemporary-puzzles/yang-mills-mass-gap/order-three-orientation-and-the-exceptional-stabilizer|the order-three exceptional construction]]: its oriented operation selects an odd complex structure while its even response survives reversal. The circle calculation does not identify its carrier or derivative with the exceptional automorphism.

The polar factorization itself does not prove a gap. For any densely defined real skew-adjoint \(D\), set \(A=|D|\) and define \(J(Au)=-Du\) on \(\operatorname{Ran}A\). The equality \(\|Au\|=\|Du\|\) extends this map to the same orthogonal complex structure on \(\ker(D)^\perp\), even when \(A^{-1}\) is unbounded. Thus positivity can be obtained by a choice of complex presentation for a general real skew flow. The additional content here is the independently computed identification of \(A\) with harmonic response and compression residue, not positivity by itself.

## Complex scalars describe the real oriented response

Let multiplication by \(i\) mean application of \(J\) on \(\mathcal V_0\). Define

\[
h_J(f,g)=(f,g)_R+i(Jf,g)_R.
\tag{HB5}
\]

This is a positive Hermitian inner product, conjugate-linear in the first variable; \(h_J(f,f)=\|f\|_R^2\). It turns the real space into a complex Hilbert space without independently choosing positive Fourier amplitudes.

To compare with conventional complex-valued boundary functions, use the real-linear formula

\[
\Phi f=\frac{f-iJf}{\sqrt2}
=\sqrt2 P_-f.
\tag{HB6}
\]

The second expression uses ordinary complexification and the negative-frequency projection. The zero Fourier coefficient is absent. By pairing conjugate real Fourier coefficients,

\[
\langle\Phi f,\Phi g\rangle=h_J(f,g),\qquad
\Phi(Jf)=i\Phi f.
\tag{HB7}
\]

Hence \(\Phi\) is a complex-linear isometry onto the mean-zero Hardy space, with the domain complex structure specified by \(J\).

Constants require separate attention. The polar construction is zero on \(\ker D\); one real constant direction does not canonically become a complex line. The full Hardy member uses the complexification of the constant sector to obtain its vacuum \(\mathbb C\Omega\). This is an explicit extension, not a consequence of (HB3) on a one-dimensional real space.

## The clock is the same boundary response

For harmonic extension \(u_f\), the outward normal derivative is

\[
\Lambda_R f:=\left.\partial_r u_f\right|_{r=R}
=Af.
\tag{HB8}
\]

Thus the positive modulus of the oriented tangent derivative equals the Dirichlet-to-Neumann operator for this disk. This equality is geometry-specific; it is not being assumed for an arbitrary manifold with boundary.

Tangential translation now satisfies

\[
U_sf(x)=f(x+s),\qquad
U_s=e^{sD}=e^{-JsA}.
\tag{HB9}
\]

In the complex structure (HB5), this is \(U_s=e^{-isA}\). Under \(\Phi\) it is precisely the nonconstant part of the clock in [[inq|the analytic-tail realization]], not a new Hamiltonian added to it.

The quadratic form has three independently calculated presentations:

\[
\boxed{
h_J(f,Af)
=\frac1{2\pi R}\int_{B_R}|\nabla u_f|^2\,dA
=\frac2R\operatorname{Tr}\Delta_f.}
\tag{HB10}
\]

Initially take \(f\) in the operator domain; the form identity extends to \(H^{1/2}\). The imaginary part on the left vanishes because \(J\) commutes with \(A\) and is skew-adjoint. The last equality is proved in [[algebra/hardy-compression-and-boundary-response|Hardy compression and boundary response]], with real \(f\) serving as the readout symbol.

The roles must remain typed: \(f\) labels a self-adjoint multiplication readout, \(\Phi f\) is a Hardy state vector, and \(\Delta_f\) is a positive operator associated with that readout. The equality transports the **trace form in the symbol label** to the clock's **state quadratic form**. It is not \(\Delta_f\) equal to \(A\), nor a physical identification of every observable with a state.

Consequently the [[algebra/quotient-clock-and-stationary-action|stationary state action]] has its symplectic form and Hamiltonian term fixed by this same realized structure. In this member, calling the response a clock cost has a precise theorem behind it. Calling it physical energy or mass still requires a physical realization and clock calibration.

## Two parameters related by harmonic extension

Let

\[
r=R e^{-\tau/R},\qquad \tau\geq0.
\tag{HB11}
\]

Restriction of the harmonic extension to this concentric circle, pulled back by the same angle, gives

\[
C_\tau f=e^{-\tau A}f.
\tag{HB12}
\]

The parameter \(\tau\) is logarithmic radial depth, not ordinary inward distance \(R-r\). Tangential displacement \(s\) and this depth obey

\[
C_\tau U_s=U_sC_\tau,\qquad
F(\tau,s)=e^{-\tau A}e^{-JsA}f,
\qquad
\partial_sF=J\partial_\tau F.
\tag{HB13}
\]

For positive \(\tau\), the derivatives are defined for every \(L^2\) boundary vector by smoothing; at zero, use the generator domain. This is the exact two-parameter relation: one response controls attenuation along depth and rotation along the oriented boundary.

These are not the same process arrow. For \(\tau>0\), \(C_\tau\) is a strict contraction on nonconstant modes, injective, with an unbounded inverse on its range. It does not literally erase a nonzero vector at finite depth. \(U_s\) is reversible. The compact-transient erasure in [[inq|the original member]] is a third, genuinely noninjective map.

No continuous Hilbert-space quotient intertwining the same parameter can turn \(e^{-\tau A}\) into this nontrivial unitary group merely by declaring the parameters equal. The relation is supplied by \(D=-JA\), not by confusing smoothing with translation. It sharpens the [[algebra/os-descent-naturality-and-clock-no-go|idempotent-clock distinction]] while allowing both processes to belong to one geometric object.

## What the geometry has selected

Relative to the disk, the negative Fourier orientation is no longer a free spectral choice: it follows from \(D\), positivity of its modulus, and \(J=-DA^{-1}\). The response-to-clock equality (HB10) is also forced, including its normalization.

The construction still supplies a metric disk, orientation, harmonic extension law and boundary measure. It has not shown why nature selects this presentation domain, why a particular \(R\) should be retained, or why a spatially three-dimensional field realization follows.

The boundary readouts \(P_-M_fP_-\) are legitimate compressed observables (effects when \(0\leq f\leq1\)) but fail commuting locality even on disjoint arcs, as the explicit counterexample in [[algebra/hardy-compression-and-boundary-response|the compression theorem]] shows. This is a construction constraint, not a reason to abandon the shared response.

They nevertheless generate a concrete clock-covariant algebra. Multiplication by \(e^{-i\theta}\) compresses to the unilateral shift \(S e_n=e_{n+1}\), and continuous-symbol readouts belong to \(C^*(S)\). Since \(1-SS^*=|\Omega\rangle\langle\Omega|\), the operators \(S^m(1-SS^*)(S^*)^n\) are its compact matrix units. The existing clock obeys

\[
U_sT_aU_s^*=T_{a(\,\cdot+s/R\,)}.
\tag{HB14}
\]

This supplies an observable algebra and its covariance without appending another Hamiltonian. It does not turn that algebra into a commuting local net.

[[local-weyl-realization|A different realization of the same response]] does construct commuting local circle algebras: the trace of the odd compression residue supplies the local derivative pairing, while the even trace supplies a positive one-particle norm. A stated bosonic Weyl/Fock construction then returns locality and clock covariance. It is an additional realization choice, not an identification of Weyl operators with Toeplitz readouts.

The compatible period refinement remains available and still closes the positive rate edge. Geometry has now removed two independent choices from the prototype; it has not supplied the interacting four-dimensional theory or the obstruction that would keep all its normalized excitations away from zero.
