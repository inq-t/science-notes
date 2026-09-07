# Determinant Cone Preparation and the Gapless Return

An admissible determinant kernel on the complex rank-two cone fixes a Hilbert pairing, positive preparation semigroup and Lorentz-covariant translation representation on one carrier. Its parameter threshold is nevertheless not a mass gap: the same homogeneous geometry retains arbitrarily soft normalized preparations. At the first positive exponent the joint spectrum is lightlike; above it the spectrum enters the timelike cone but still approaches its null boundary. This constructs and tests a common arena-and-clock candidate rather than appending a Hamiltonian to a positive Hessian.

## The determinant fixes the pairing and its dual carrier

Use \(\Omega=\operatorname{Herm}_2(\mathbb C)_{++}\) and
\(\beta\in[1,\infty)\), as classified in
[[algebra/determinant-preparation-positivity-and-the-rank-threshold|the determinant-kernel theorem]].
Let \(\mu_\beta\) be the positive measure on \(\overline\Omega\)
characterized by
\[
\int e^{-\operatorname{Tr}(AX)}\,d\mu_\beta(X)
=\det(A)^{-\beta},\qquad A>0.
\tag{DC1}
\]
The theorem's explicit constructions are the pushforward of
\(\pi^{-2}d^4z\) under \(z\mapsto zz^*\) at \(\beta=1\), and
\[
d\mu_\beta(X)
=\frac{(\det X)^{\beta-2}}{\pi\Gamma(\beta)\Gamma(\beta-1)}\,dX,
\quad X>0,\quad\beta>1,
\tag{DC2}
\]
with coordinate Lebesgue measure as specified there. These are not
probability measures; the exponential preparations are square-integrable.
Laplace-transform uniqueness fixes the measure from the kernel.

Set
\[
\mathcal H_\beta=L^2(\overline\Omega,\mu_\beta),\qquad
\phi_A(X)=e^{-\operatorname{Tr}(AX)}.
\tag{DC3}
\]
Then
\[
\boxed{\langle\phi_A,\phi_B\rangle=\det(A+B)^{-\beta}.}
\tag{DC4}
\]
Thus the formal span of preparation labels, quotiented by the null space
of this pairing and completed, has a concrete realization.

It is all of \(\mathcal H_\beta\). If \(f\) is orthogonal to every
\(\phi_A\), fix \(A_0>0\). The complex measure
\(\overline f(X)e^{-\operatorname{Tr}(A_0X)}d\mu_\beta(X)\) is finite
by Cauchy--Schwarz. Its Laplace transform vanishes for every positive
argument, because \(A_0+B>0\). Uniqueness makes this measure zero,
and its exponential factor never vanishes. Hence \(f=0\).

The variable \(A\) labels preparations; \(X\) labels their joint
spectral response. Neither is being declared a spacetime position.
Unlike an arbitrary density assigned after constructing a carrier,
the measure and its pairing here come from the selected determinant law.
The cone type and exponent remain primitive choices.

## Order, positive preparation and phase translation share one carrier

For \(C\in\overline\Omega\), define on the dense preparation span
\[
T_C\phi_A=\phi_{A+C}.
\tag{DC5}
\]
In (DC3) this is multiplication by \(e^{-\operatorname{Tr}(CX)}\).
Self-duality of the positive matrix cone implies
\[
0\le T_C\le I,\qquad T_CT_D=T_{C+D}.
\tag{DC6}
\]
These strongly continuous commuting positive contractions operate on
preparation classes. They are injective, and their inverses generally
are unbounded. Their admissible cone order is one-sided; finite-depth
attenuation is not literal identification of different vectors.

For a Hermitian \(B\), the same spectral variable gives
\[
(U_Bf)(X)=e^{-i\operatorname{Tr}(BX)}f(X),\qquad
U_BU_D=U_{B+D}.
\tag{DC7}
\]
These form a strongly continuous unitary group. For a specified
\(u>0\), its positive generator is
\[
H_uf(X)=\operatorname{Tr}(uX)f(X),\qquad
\operatorname{Dom}H_u
=\{f:\operatorname{Tr}(uX)f\in L^2(\mu_\beta)\}.
\tag{DC8}
\]
It is self-adjoint as a real multiplication operator, and
\(T_{su}=e^{-sH_u}\), \(U_{tu}=e^{-itH_u}\).
No second spectral generator is selected for the reversible action.
The choice of \(u\) specifies a positive direction, not a duration unit.

Equations (DC4)--(DC8) implement the
[[algebra/wick-real-forms-and-positive-preparation|positive-preparation relationship]]
from explicit geometry. They do not identify the family parameter
\(\beta\) with the preparation depth \(s\). The forbidden kernel powers
below \(\beta=1\) do not obstruct the continuous semigroup (DC6).

## The determinant supplies a Lorentz-covariant joint spectrum

Write
\[
X=p_0I+\mathbf p\cdot\sigma,\qquad
\det X=p_0^2-|\mathbf p|^2,\qquad p_0\ge|\mathbf p|.
\tag{DC9}
\]
The cone and its signature belong to
[[algebra/positive-cone-processes-and-the-complex-corner|the selected complex rank-two geometry]].
For \(S\in SL(2,\mathbb C)\), congruence \(X\mapsto SXS^*\)
preserves both determinant and \(\mu_\beta\). For (DC2), its real
Jacobian is \(|\det S|^4=1\); at \(\beta=1\), use the complex-linear
change \(z\mapsto Sz\) in the pushforward construction.

Consequently
\[
(V_Sf)(X)=f(S^{-1}XS^{-*})
\tag{DC10}
\]
is unitary. The central element \(-I\) acts trivially, so this action
descends to the proper orthochronous Lorentz group. It is strongly
continuous, first on compactly supported continuous functions and then
by density in the Radon-measure carrier.

To display translations, put
\(B(a)=(a_0I-\mathbf a\cdot\sigma)/2\). Then
\(\operatorname{Tr}(B(a)X)=a_0p_0-\mathbf a\cdot\mathbf p\).
Together (DC7) and (DC10) give
\[
V_SU_{B(a)}V_S^*=U_{B(\Lambda(S)a)},
\tag{DC11}
\]
an explicit positive-energy Poincare representation. Its time
translation generator in these coordinates is
\(P_0=H_{I/2}\), not \(H_I\); the factor two follows from the trace
pairing. Units such as \(c\) have not been calibrated.

The quadratic translation invariant is multiplication by
\[
\boxed{P_0^2-\mathbf P^2=\det X.}
\tag{DC12}
\]
The expression is defined by joint spectral functional calculus, on
\(\{f:\det(X)f\in L^2(\mu_\beta)\}\). It is the closed multiplication
operator, not merely the difference of squared generators on their
smaller common domain. This is a genuine joint Casimir in the returned representation, not an
identification of a determinant Hessian with energy. A physical local
observable net and Yang--Mills dynamics still have not been constructed.

## The first positive admissible exponent is lightlike, not massive

At \(\beta=1\), the pushforward \(X=zz^*\) has rank one almost
everywhere. Thus (DC12) is zero on the whole carrier, while \(P_0\)
is nonzero. At \(\beta>1\), (DC2) has positive density throughout
the open cone. Then \(\det X>0\) almost everywhere, but every interval
\(0<\det X<\epsilon\) has nonzero spectral weight. The Casimir's
spectrum reaches zero; there is no strictly positive invariant mass
threshold.

The same conclusion is visible without relying on a qualitative support
description. Normalize the radial preparations by
\[
e_a=\det(2aI)^{\beta/2}\phi_{aI},\qquad a>0.
\tag{DC13}
\]
Direct differentiation of (DC1) gives
\[
\begin{aligned}
\langle e_a,e^{-sH_I}e_a\rangle
&=\left(\frac{2a}{2a+s}\right)^{2\beta},\\
\langle H_I\rangle_{e_a}&=\frac\beta a,\qquad
\operatorname{Var}_{e_a}(H_I)=\frac\beta{2a^2}.
\end{aligned}
\tag{DC14}
\]
These vectors have all finite energy moments. As \(a\to\infty\),
their mean energy tends to zero while their norm remains one.
Even one fixed preparation has algebraic, not exponential, long-depth
decay in (DC14). The positive exponent threshold therefore does not
bound the returned clock from below.

There is no zero-energy eigenvector in this carrier: \(H_u=0\) on
the cone only at \(X=0\), which has zero \(\mu_\beta\)-mass for
\(\beta>0\). One may append a trivial line
\(\mathbb C\Omega\oplus\mathcal H_\beta\), equivalently add an atom
at the origin. This produces a unique invariant vacuum but leaves
(DC14) on its orthogonal complement unchanged. The vacuum addition is
extra data, not a gap-producing step.

The reason is exact scale covariance, not the absence of a numerical
estimate. For \(r>0\), both constructions of the measure satisfy
\(\mu_\beta(rE)=r^{2\beta}\mu_\beta(E)\). Hence
\[
(D_rf)(X)=r^\beta f(rX),\qquad
D_rH_uD_r^{-1}=rH_u,\qquad
D_r(\det X)D_r^{-1}=r^2\det X.
\]
Here \(D_r\) is unitary, and the last identity is between multiplication
operators on their corresponding domains. A nonzero positive spectral
value can therefore be transported arbitrarily close to zero. The
construction supplies a covariant family of scales but selects no
positive lower edge. This supplements the explicit soft preparations,
which satisfy
\(\|H_Ie_a\|^2=\beta(2\beta+1)/(2a^2)\to0\).

## The returned algebra and readout are now available, not local by decree

Since the \(\phi_A\) span densely, their rank-one transitions obey
\[
|\phi_A\rangle\langle\phi_B|\,
|\phi_C\rangle\langle\phi_D|
=\det(B+C)^{-\beta}|\phi_A\rangle\langle\phi_D|.
\tag{DC15}
\]
The completion argument in
[[preparation-overlaps-and-the-transition-algebra|the transition-algebra theorem]]
returns the compact operators. Positive linear evaluation then has the
[[positive-readout-and-the-born-weight|trace form]], and two normalized
preparations give the real readout weight \(k_\beta(A,B)^2\).
These are consequences on the same carrier. Admitting all transitions,
choosing a physical state and selecting local subalgebras remain distinct
obligations; compact transitions must not be assigned spacelike
commutation merely because their preparation labels differ.

This candidate forces a relationship among determinant response,
positive overlaps, allowable exponents and a covariant clock. It also
pinpoints its failure for the full goal: exact homogeneous spectral
support retains all scales. Multiplying (DC2) by a strictly positive
weight cannot open a Casimir gap because it leaves its support unchanged.
A gap-producing modification must change the support or the physical
realization, and that change must follow from a further structural law,
not from inserting a desired cutoff.

The [[algebra/determinant-preparation-positivity-and-the-rank-threshold|fixed-trace exception]]
also prevents calling this exponent restriction a universal grain of
observation. Retaining only normalized qubit states loses precisely the
scale variation involved in the full-cone obstruction. A lawful relation
between those carriers is a sharper target than equating the parameter
threshold, the determinant rank wall and the physical mass gap.

[[determinant_kernel_receipt.py|The determinant-kernel receipt]] and
[[determinant-kernel-receipt-output.txt|its output]] check finite algebra,
the negative Gram witness and radial identities. They do not certify a
local field theory or replace the density and spectral arguments above.
