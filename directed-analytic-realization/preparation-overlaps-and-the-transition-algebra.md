# Preparation Overlaps and the Transition Algebra

A compatible spectral readout determines not only a positive clock but a concrete algebra of transitions between preparation states. The overlap kernel fixes the product and adjoint of these transitions; quotienting null preparations and completing returns the compact operators on the minimal spectral carrier. The same clock acts on that algebra. This is a whole-algebra construction, not yet a selection of commuting local field algebras, a spatial dimension or a positive mass threshold.

## Directed preparation labels have a positive overlap kernel

Use the normalized positive operator-valued measure \(\mathsf M\) on
\(\mathcal R\) assembled in
[[global-local-response-reconstruction/compatible-spectral-readouts-and-positive-clock|the compatible-readout theorem]].
Its minimal dilation is
\[
\mathsf M(B)=J^*E(B)J,\qquad
J^*J=I,\qquad
H=\int_0^\infty\lambda\,dE(\lambda)\ge0
\quad\text{on }\mathcal K.
\tag{PT1}
\]
The construction of \(\mathcal K,E,J,H\) belongs to that theorem. Define
\[
R_s=\int e^{-s\lambda}\,d\mathsf M(\lambda),\qquad
x_{s,\xi}=e^{-sH}J\xi,\qquad s\ge0,\quad \xi\in\mathcal R.
\tag{PT2}
\]
The label \(s\) initially means preparation depth. No spacetime position,
clock unit or irreversible record is assigned to it.
The compressed \(R_s\) need not be a semigroup.

For formal preparation symbols \([s,\xi]\), linear in \(\xi\), set
\[
\boxed{
\langle[s,\xi],[t,\eta]\rangle_{\mathrm{prep}}
=\langle\xi,R_{s+t}\eta\rangle
=\langle x_{s,\xi},x_{t,\eta}\rangle_{\mathcal K}.
}
\tag{PT3}
\]
This is a positive semidefinite kernel, conjugate-linear in the first
variable. Quotient its null space and complete. The displayed map
\([s,\xi]\mapsto x_{s,\xi}\) is an isometry onto a closed subspace of
\(\mathcal K\).

It is onto. In fact, for any fixed \(\tau>0\), the vectors
\[
\{e^{-n\tau H}J\xi:n=0,1,\ldots,\ \xi\in\mathcal R\}
\tag{PT4}
\]
already have dense span. If \(\zeta\) is orthogonal to them, the finite
complex measure
\(\nu_\xi(B)=\langle\zeta,E(B)J\xi\rangle\) has all moments
\(\int e^{-n\tau\lambda}\,d\nu_\xi(\lambda)=0\).
Its total variation is at most \(\|\zeta\|\|\xi\|\), by
Cauchy--Schwarz over disjoint spectral projections.
Push it forward by \(q=e^{-\tau\lambda}\), and extend by zero at \(q=0\).
It is a finite measure on \([0,1]\) annihilating every polynomial.
Polynomial density in \(C([0,1])\) makes that measure zero.
The map to \(q\in(0,1]\) is a Borel bijection, so \(\nu_\xi=0\).
Minimality of (PT1) now gives \(\zeta=0\).

Thus directed preparations alone recover the entire minimal carrier;
two-sided real clock labels are not required for this density statement.
The arbitrary sampling step \(\tau\) selects no physical duration unit.

The delay rule \([s,\xi]\mapsto[s+a,\xi]\) descends to the contraction
\(e^{-aH}\), \(a\ge0\), on the completed carrier. This is the
[[algebra/wick-real-forms-and-positive-preparation|positive-preparation method]]
with a bounded normalized overlap kernel. Unlike that owner's
\((2A)^{-1}\)-weighted test-function kernel, (PT3) also retains the zero
spectral sector without an inverse-generator factor.

## Overlaps fix an actual noncommutative product

For two preparations define the rank-one transition
\[
\Theta_{s,t}(\xi,\eta)
=|x_{s,\xi}\rangle\langle x_{t,\eta}|
\quad\text{on }\mathcal K.
\tag{PT5}
\]
It sends a vector \(z\) to
\(x_{s,\xi}\langle x_{t,\eta},z\rangle\). Hence it operates on preparation
classes, not on spectral numbers or spacetime points. Its product is
\[
\boxed{
\Theta_{s,t}(\xi,\eta)\Theta_{u,v}(\zeta,\theta)
=\langle\eta,R_{t+u}\zeta\rangle\,
  \Theta_{s,v}(\xi,\theta).
}
\tag{PT6}
\]
The middle contraction is supplied by the same readout, not a separately
chosen multiplication table. The adjoint and norm are
\[
\boxed{
\Theta_{s,t}(\xi,\eta)^*=\Theta_{t,s}(\eta,\xi),\qquad
\|\Theta_{s,t}(\xi,\eta)\|
=\|x_{s,\xi}\|\|x_{t,\eta}\|.
}
\tag{PT7}
\]
If a preparation is null, every transition having it as either endpoint
vanishes. The product therefore respects the preparation quotient.
Associativity follows directly from contracting the two independent
middle overlaps in a threefold product, or from its explicit operator
realization. When \(\dim\mathcal K\ge2\), this transition algebra is
noncommutative even though the spectral-function algebra in (PT1) was
commutative. The one-dimensional case remains commutative.

The linear span of (PT5) is a \(*\)-algebra. By (PT4), its operator-norm
closure is
\[
\boxed{\mathfrak T=\mathcal K(\mathcal K),}
\tag{PT8}
\]
the compact operators on the carrier. Indeed finite linear combinations
of preparation vectors approximate arbitrary endpoint vectors, and
\[
\||x\rangle\langle y|-|x'\rangle\langle y'|\|
\le\|x-x'\|\|y\|+\|x'\|\|y-y'\|.
\]
Its ultraweak closure is \(B(\mathcal K)\). In infinite dimension
\(\mathfrak T\) itself has no unit; its multiplier algebra is
\(B(\mathcal K)\). These are different completions, not an implicit
replacement of a local observable algebra by all bounded operators.

This is canonical given the choice to admit all preparation transitions:
a unitary intertwining two minimal dilations transports every (PT5) to
its counterpart. The spectral data do not require nature to allow every
such transition as an independently local operation.

[[positive-readout-and-the-born-weight|Positive evaluation on this algebra]]
has the density-operator trace form. In particular, a prepared ray and a
tested ray give a squared-overlap readout computable from (PT3).
This is a subsequent state-and-test pairing, not a probability ontology
or a consequence of noncommutativity alone.

## An observable must be allowed to connect two spectral labels

For a zero-depth transition \(X_{\xi,\eta}=\Theta_{0,0}(\xi,\eta)\), its
two-spectral-set kernel is
\[
\boxed{
J^*E(B)X_{\xi,\eta}E(C)J
=\mathsf M(B)|\xi\rangle\langle\eta|\mathsf M(C).
}
\tag{PT9}
\]
There is no requirement that \(B=C\) or that the two sets overlap.
For general (PT5), replace \(\mathsf M(B)\) and \(\mathsf M(C)\) by
\(\int_B e^{-s\lambda}\,d\mathsf M(\lambda)\) and
\(\int_C e^{-t\lambda}\,d\mathsf M(\lambda)\).
These are operator-valued transition kernels, not scalar probability laws.

[[algebra/spectral-coefficient-lifts-and-the-frozen-clock|The coefficient-lift theorem]]
shows why this matters. A \(*\)-action merely changing
\([B,\xi]\) to \([B,a\xi]\) must commute with the spectral effects and
therefore with the returned clock. It cannot create a positive-energy
excitation from a zero-energy vacuum. Equation (PT9) supplies a different,
off-diagonal action rather than contradicting that theorem.

For a supplied \(a\in B(\mathcal R)\), the corner map is always available:
\[
\pi_J(a)=JaJ^*,\qquad
\pi_J(ab)=\pi_J(a)\pi_J(b),\qquad
\pi_J(a)^*=\pi_J(a^*),\qquad
\|\pi_J(a)\|=\|a\|.
\tag{PT10}
\]
But \(\pi_J(I)=JJ^*\), not \(I_{\mathcal K}\) unless \(J\) is onto.
It is a faithful corner representation, not automatically a unital
representation on the whole carrier. It also differs from the
coefficient rule: \(\pi_J(a)[C,\eta]=J a\mathsf M(C)\eta\).

This unit issue can be unavoidable, not merely a poor choice of extension.
Take
\[
\mathcal R=\mathbb C^2,\quad \mathcal K=\mathbb C^3,\quad
Je_0=e_0,\quad Je_1=(3e_1+4e_2)/5,\quad
H=\operatorname{diag}(0,1,2).
\tag{PT11}
\]
The readout effects are
\[
\mathsf M(\{0\})=\operatorname{diag}(1,0),\quad
\mathsf M(\{1\})=\operatorname{diag}(0,9/25),\quad
\mathsf M(\{2\})=\operatorname{diag}(0,16/25).
\]
This dilation is minimal and has a unique zero-energy vector.
The corner returns \(M_2\) with a rank-two unit. There is no unital
\(*\)-representation \(M_2\to M_3\): its two diagonal matrix units would
be orthogonal equivalent projections with equal ranks summing to three.
Nevertheless (PT8) returns the whole \(M_3\). Returning a noncommutative
whole algebra is not the same as recovering a specified local algebra
with its original unit.

## Preparation and clock act differently on the same algebra

On \(\mathfrak T\), the directed preparation operation
\[
\mathcal P_a(X)=e^{-aH}Xe^{-aH}
\tag{PT12}
\]
is completely positive and contractive, with
\[
\mathcal P_a\Theta_{s,t}(\xi,\eta)=\Theta_{s+a,t+a}(\xi,\eta).
\]
It extends normally to \(B(\mathcal K)\), but is subunital rather than
unital unless \(H=0\): \(\mathcal P_a(I)=e^{-2aH}\) for \(a>0\).
It is not generally multiplicative. Nor does its injective attenuation
at finite \(a\) represent literal many-to-one forgetting; the null
preparation quotient is the distinct source of that identification.

The same positive generator gives \(U_t=e^{-itH}\) and
\[
\boxed{\alpha_t(X)=U_tXU_t^*.}
\tag{PT13}
\]
This chosen conjugation convention fixes all phase signs; reversing it
gives the usual opposite Heisenberg convention.
The \(\alpha_t\) are \(*\)-automorphisms of \(\mathfrak T\) and
\(B(\mathcal K)\). They are point-norm continuous on the compact
algebra, even for unbounded \(H\), by strong continuity on rank-one
endpoints and finite-rank approximation. The preparation and clock
operations commute, but are not the same operation.

Assume the vacuum condition from (PT1)'s owner, and put
\(\Omega=J\Omega_{\mathcal R}\). Then \(H\Omega=0\), and the vector
state on \(B(\mathcal K)\) is pure, stationary and cyclic, but
nonfaithful when \(\dim\mathcal K>1\). This is compatible with
[[algebra/faithful-stationary-states-and-the-positive-clock|faithful-state clock rigidity]].
No faithful state on the whole algebra has been silently substituted.

In this vacuum case the time orbit of the zero-depth rank-one transitions,
or equivalently the compact corner \(J\mathcal K(\mathcal R)J^*\),
also generates all of \(\mathfrak T\). Its products include
\[
\alpha_t(X_{\xi,\Omega_{\mathcal R}})
\alpha_u(X_{\Omega_{\mathcal R},\eta})
=|U_tJ\xi\rangle\langle U_uJ\eta|.
\tag{PT14}
\]
The orbit vectors have dense span: a vector orthogonal to all of them
defines finite scalar spectral measures with identically zero Fourier
transforms, hence zero measures; minimality then applies.
This is an additional clock-covariance result, not an assumption that
each zero-depth corner is clock-invariant.

The full bounded corner \(JB(\mathcal R)J^*\) in (PT10) can contain
noncompact operators when \(\mathcal R\) is infinite dimensional.
Its orbit algebra therefore need not equal \(\mathfrak T\).
Exact compact generation above uses the rank-one or compact corner.

## The returned transitions have a complete vacuum-response family

For centered vectors \(x,y\perp\Omega\), let
\(C_x=|x\rangle\langle\Omega|\). These are compact operators with
\(\omega_\Omega(C_x)=0\) and
\[
\boxed{
\omega_\Omega(C_x^*e^{-aH}C_y)=\langle x,e^{-aH}y\rangle,
\qquad a\ge0.
}
\tag{PT14a}
\]
For centered preparation endpoints
\(x=(I-P_\Omega)x_{s,\xi}\), \(y=(I-P_\Omega)x_{t,\eta}\), this is
\[
\langle\xi,R_{s+a+t}\eta\rangle
-\langle\xi,\Omega_{\mathcal R}\rangle
 \langle\Omega_{\mathcal R},\eta\rangle.
\tag{PT14b}
\]
Their linear span is dense in \(\Omega^\perp\), by (PT4).
The [[coarse-response-memory/spectral-readout-and-the-visible-gap|spectral-coverage theorem]]
therefore applies to actual operators on this returned carrier:
a common exponential bound on all their normalized vacuum responses is
equivalent to the corresponding whole-generator gap. It does not supply
that bound. These transitions are globally total by construction, not
certified physical local observables.

## Whole transitions do not select a local arena

Orthogonality of two distinctions is insufficient for their transition
algebras to commute. For orthonormal \(\Omega,\psi,\phi\), set
\[
A=|\psi\rangle\langle\Omega|+|\Omega\rangle\langle\psi|,\qquad
B=|\phi\rangle\langle\Omega|+|\Omega\rangle\langle\phi|.
\]
Then
\[
\boxed{[A,B]=|\psi\rangle\langle\phi|-|\phi\rangle\langle\psi|\ne0,
\qquad [A,B]\Omega=0.}
\tag{PT15}
\]
Even the vacuum-vector commutator test alone misses this failure of
operator commutation. Assigning these vacuum-sharing corners to
spacelike-separated regions would not establish locality.

The [[harmonic-boundary-realization|harmonic boundary example]] provides
a concrete comparison: Toeplitz readouts generate compact matrix units
and a compatible clock, yet a separate
[[local-weyl-realization|Weyl realization]] is needed for its commuting
local net. Likewise the [[pointed-cp-fusion-residue/inq|pointed CP kernel]]
already includes noncommutative algebra labels and preserves their
specified action; it is a different input from allowing every rank-one
transition between spectral preparations.

The exact gain is that a preparation-overlap law fixes an associative
noncommutative whole algebra and its clock on the same returned carrier.
What it has not fixed is which subalgebras represent local observations,
their causal arrangement and spatial covariance, the interacting
Yang--Mills law, or a uniform lower spectral edge. The compact transition
algebra exists for gapped and gapless readouts alike.
Mass interpretation still requires the physical translation structure,
not only a positive abstract preparation generator.

[[spectral_transition_receipt.py|The spectral-transition receipt]] and
[[spectral-transition-receipt-output.txt|its output]] check finite overlap
products, the null-space obstruction, the corner unit, complete transition
span, clock conjugation and the noncommuting vacuum-sharing example.
The density and completion arguments above are not conclusions of finite
sampling.
