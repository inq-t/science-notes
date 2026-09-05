# A Quotient Clock Carries a Stationary State Action

A complex positive realization can acquire a symplectic state space and a stationary-action description without imposing either on the whole process as a nondegenerate structure. Once a one-sided process induces a strongly continuous unitary quotient, the quotient form supplies the symplectic structure and the process derivative supplies the Hamiltonian in its state action. This is an exact representation theorem, not a derivation of spacetime locality, positive energy or a Yang–Mills action.

## The process data and their return

Use the hypotheses of [[algebra/quotient-unitarity-and-kernel-stabilization|quotient unitarity]]: a complex vector space \(\mathcal K\), a positive semidefinite Hermitian form \(g\), its radical \(N\), and a linear semigroup \(T_s\), \(s\geq0\), satisfying

\[
g(T_su,T_sv)=g(u,v),\qquad
T_s\mathcal K+N=\mathcal K,\qquad
g(T_su-u,T_su-u)\longrightarrow0.
\]

The last limit is as \(s\downarrow0\). Let \(q:\mathcal K\to\mathcal H_g\) map into the completion of \(\mathcal K/N\). The induced unitary semigroup extends to a strongly continuous group \(U_s\), \(s\in\mathbb R\), with

\[
qT_s=U_sq\quad(s\geq0),\qquad U_s=e^{-isK}.
\tag{QA1}
\]

Here \(K\) is the self-adjoint generator of this very group. It is not independently supplied after realization. The spectral sign of \(K\) is unrestricted by these hypotheses. The parameter \(s\) is the process parameter returned in this representation, not yet a calibrated physical duration.

All inner products below are conjugate-linear in the first argument.

## Symplectic form on the realized state space

On the underlying real Hilbert space of \(\mathcal H_g\), put

\[
\omega(u,v):=2\operatorname{Im}\langle u,v\rangle.
\tag{QA2}
\]

This constant bilinear form is closed and nondegenerate. Indeed, for \(u\neq0\),

\[
\omega(u,iu)=2\|u\|^2>0.
\]

The quotient clock preserves it because it preserves the Hermitian inner product. Before quotienting, \(2\operatorname{Im}g\) is degenerate precisely along \(N\) as a real form: testing against \(iv\) recovers the real part of \(g(u,v)\). Thus the symplectic state space is the reduction of a degenerate form, not an assumed nondegenerate geometry of the whole.

The complex structure and positive form are real inputs to this theorem. A real positive quotient alone need not be symplectic; a one-dimensional real quotient is an immediate counterexample. This theorem derives the symplectic description from complex positive realization, not complex positivity from nothing.

## The Hamiltonian is extracted from the process

For \(\psi\in\operatorname{Dom}K\), define

\[
\mathcal E(\psi):=\langle\psi,K\psi\rangle,\qquad
X(\psi):=-iK\psi.
\tag{QA3}
\]

For variations \(v\in\operatorname{Dom}K\),

\[
d\mathcal E_\psi[v]
=2\operatorname{Re}\langle v,K\psi\rangle
=\omega(X(\psi),v).
\tag{QA4}
\]

This fixes the Hamiltonian-vector-field convention. The quadratic functional is a consequence of the selected generator and norm. Calling \(\mathcal E\) physical energy requires a physical clock and normalization; positivity requires \(K\geq0\), separately.

## Exact stationarity, not a semiclassical approximation

For an interval \(I=[a,b]\), take paths

\[
\psi\in C^1(I;\mathcal H_g)
\cap C(I;\operatorname{Dom}K),
\]

where continuity into \(\operatorname{Dom}K\) uses the graph norm. Define the real state functional

\[
\mathcal S_I[\psi]
=\int_a^b
\left[
\frac{i}{2}
\bigl(\langle\psi,\dot\psi\rangle
-\langle\dot\psi,\psi\rangle\bigr)
-\langle\psi,K\psi\rangle
\right]\,ds.
\tag{QA5}
\]

For variations of the same regularity vanishing at both endpoints, integration by parts gives

\[
\delta\mathcal S_I[\psi;v]
=2\operatorname{Re}\int_a^b
\langle v,i\dot\psi-K\psi\rangle\,ds.
\tag{QA6}
\]

Consequently

\[
\boxed{\delta\mathcal S_I=0
\quad\Longleftrightarrow\quad
i\dot\psi=K\psi}
\tag{QA7}
\]

on this domain. To obtain the converse direction rigorously, use \(v(s)=f(s)w\) with smooth compactly supported \(f\) and \(w\in\operatorname{Dom}K\), then density and continuity. These are variations in the full linear state space. Imposing a unit-sphere constraint changes the statement by a scalar phase multiplier.

The action is additive under subdivision of its parameter interval. This theorem alone uses the one-dimensional parameter already present in (QA1); it has not produced a four-dimensional integration domain or a spatially local Lagrangian density. [[algebra/cauchy-response-and-local-action|The opposed-boundary specialization]] supplies a spatial carrier and proves that this very action becomes the local scalar wave action up to an endpoint term. Multiplication by a constant action unit leaves (QA7) unchanged. For a later calibration \(s=\nu t\), comparison with conventional notation gives \(H_{\rm phys}=\hbar\nu K\).

## The action factors through realization

For an admissible presented path \(u(s)\) whose image \(\psi(s)=q u(s)\) has the regularity above, define \(\widetilde{\mathcal S}[u]=\mathcal S[qu]\). Every change \(u(s)\mapsto u(s)+n(s)\) with \(n(s)\in N\) leaves this functional unchanged.

The local action therefore governs the realized path without governing the discarded directions. Its stationarity is not an upstream variational principle in disguise: the lift is blind to radical variations and supplies no equation selecting their history.

This is the relevant special-case relation. One process law has a variational representation on its quotient; it need not select the whole process by extremizing that representation.

## What has and has not been selected

If \(g\) and \(T_s\) were chosen independently to reproduce a desired \(K\), the theorem would only repackage the choice. [[directed-analytic-realization/inq|The directed analytic-tail member]] instead specifies a single translation law and a long-interval pairing. Its radical, analytic Hilbert carrier, positive generator and state action are then calculated from those data.

That tail member imports an analytic polarization, averaging prescription and process parameter. Its [[directed-analytic-realization/harmonic-boundary-realization|harmonic extension]] now selects the polarization relative to an oriented metric disk and computes the clock form from a compression residue. A further [[directed-analytic-realization/local-weyl-realization|Weyl realization]] returns local circle algebras and a Fock clock from the same response, with explicit bosonic and vacuum choices. None of these constructions supplies records, three spatial dimensions, an interacting Poincaré-covariant gauge theory or a physical mass scale. The full recovery obligations in [[contemporary-puzzles/yang-mills-mass-gap/clay-contract-and-scale-assumptions|the Clay contract]] remain in force.

[[philosophy/principle-of-least-action/why-an-action-at-all|Multiplicative history phases]] describe another route to action. Their semiclassical stationarity requires an oscillatory integration problem. Equations (QA5)–(QA7) instead give an exact state-space variational representation of an already reconstructed process; the two meanings of stationarity should not be exchanged.
