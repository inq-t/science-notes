# Pure-Vacuum Loss and the Returned Clock

A finite family of operators annihilating one vacuum vector determines both a unital completely positive process and a positive generator on that vacuum's state quotient. When its common kernel is a line, the row also selects that state up to an irrelevant vector phase. The stationary Schwarz deficit measures exactly the quadratic response of the returned generator. Its Hilbert analytic continuation acts by automorphisms of the faithfully represented full matrix algebra, unlike the earlier tracial clock return. This is an exact finite construction, not a derivation of the row from octonionic purification, a physical entropy law or a local quantum field theory.

## A loss row determines the positive response

Let \(\mathcal H\) be a finite-dimensional complex Hilbert space of dimension at least two, with unit vector \(\Omega\). Choose finitely many operators \(L_a\in B(\mathcal H)\) satisfying
\[
L_a\Omega=0.
\]
Their row map, quadratic response and vacuum state are
\[
\mathsf L:\mathcal H\longrightarrow\mathbb C^r\otimes\mathcal H,
\qquad \mathsf L\psi=\sum_a e_a\otimes L_a\psi,
\]
\[
\boxed{K=\frac12\mathsf L^*\mathsf L
=\frac12\sum_aL_a^*L_a,\qquad
\omega(A)=\langle\Omega,A\Omega\rangle.}
\tag{PV1}
\]
Thus \(K\ge0\) and \(K\Omega=0\). All operators are bounded; there are no hidden domain or closure hypotheses in this finite theorem.

Define a Heisenberg generator on the supplied algebra \(B(\mathcal H)\):
\[
\boxed{\mathcal L(A)=\sum_aL_a^*AL_a-KA-AK.}
\tag{PV2}
\]
No independent Hamiltonian commutator has been appended. If its parameter has a declared duration unit, \(K\) has inverse-duration units and \(\mathsf L\) inverse-square-root-duration units. Neither that duration nor its eventual physical calibration is selected by writing (PV1).

## The whole process is completely positive and stationary

Put \(\mathcal J(A)=\sum_aL_a^*AL_a\) and
\(\mathcal N_t(A)=e^{-tK}Ae^{-tK}\). Both are completely positive. The norm-convergent finite-dimensional Dyson series for
\[
\mathcal T_t=e^{t\mathcal L}
\]
is a sum of ordered integrals of compositions
\[
\mathcal N_{t-s_n}\mathcal J\mathcal N_{s_n-s_{n-1}}
\cdots\mathcal J\mathcal N_{s_1},
\quad 0<s_1<\cdots<s_n<t,
\]
including the \(n=0\) term \(\mathcal N_t\). Each term is completely positive; its norm is bounded by
\(\|\mathcal J\|^nt^n/n!\). Hence \(\mathcal T_t\) is completely positive. Since \(\mathcal L(I)=0\), the finite matrix ODE gives \(\mathcal T_t(I)=I\).

The decisive vector identity is
\[
\boxed{\mathcal L(A)\Omega=-KA\Omega.}
\tag{PV3}
\]
The jump term vanishes because every \(L_a\Omega=0\), and \(AK\Omega=0\). Iterating (PV3) and exponentiating gives
\[
\boxed{\mathcal T_t(A)\Omega=e^{-tK}A\Omega,\qquad
\omega\mathcal T_t=\omega.}
\tag{PV4}
\]
The pure vacuum state is stationary for the whole UCP process. This does not yet say that it is the process's only stationary state.

## A nonfaithful state quotient returns a faithful operator action

Set
\[
\mathcal Z_\omega=\{A:\omega(A^*A)=0\}
=\{A:A\Omega=0\}.
\]
This is a left ideal, generally not a two-sided ideal. Therefore
\(B(\mathcal H)/\mathcal Z_\omega\) is here a Hilbert-space quotient, not a quotient algebra. With inner product
\(\langle[A],[B]\rangle=\omega(A^*B)\), its realization is
\[
\boxed{q(A)=A\Omega,\qquad
B(\mathcal H)/\mathcal Z_\omega\cong\mathcal H.}
\tag{PV5}
\]
Surjectivity follows from \(q(|v\rangle\langle\Omega|)=v\). Left multiplication is well defined on the quotient and gives
\[
\pi(B)q(A)=q(BA)=Bq(A).
\]
Thus \(\pi\) is precisely the faithful defining representation of \(B(\mathcal H)\), with cyclic vector \(\Omega\). The state is nonfaithful, but the representation is faithful: a nonzero positive operator can annihilate \(\Omega\) without annihilating every vector.

Equation (PV3) preserves \(\mathcal Z_\omega\), and the exact quotient dynamics is
\[
\boxed{q\mathcal T_t=e^{-tK}q.}
\tag{PV6}
\]
The noninjective arrow is \(q\). In finite dimension \(\mathcal T_t=e^{t\mathcal L}\) remains invertible as a linear map at finite \(t\); its inverse need not be positive. A dissipative positive-process arrow and a literal many-to-one quotient remain different operations.

## Schwarz loss measures the same generator

For \(A,B\in B(\mathcal H)\), expansion of (PV2) gives
\[
\Gamma(A,B):=\frac12\{\mathcal L(A^*B)
-\mathcal L(A^*)B-A^*\mathcal L(B)\}
=\frac12\sum_a[L_a,A]^*[L_a,B].
\]
Since \([L_a,A]\Omega=L_aA\Omega\),
\[
\boxed{\omega\Gamma(A,B)
=\langle A\Omega,KB\Omega\rangle.}
\tag{PV7}
\]
This response acts on the realized vectors \(A\Omega\), not on all matrix entries independently.

UCP Schwarz positivity and stationarity give the finite-time identity
\[
\begin{aligned}
&\omega\!\left(\mathcal T_t(A^*A)
-\mathcal T_t(A)^*\mathcal T_t(A)\right)\\
&\qquad=\|A\Omega\|^2-\|e^{-tK}A\Omega\|^2\\
&\qquad=\int_0^t\|\mathsf L e^{-sK}A\Omega\|^2\,ds.
\end{aligned}
\tag{PV8}
\]
The last equality differentiates the squared norm. Thus the positive operator \(K\) is not unrelated to the loss: it is exactly its infinitesimal vacuum quadratic response. This is a Schwarz deficit, not automatically entropy, energy emitted to an environment or a count of obtained facts.

## Analytic continuation now preserves the actual algebra

The returned self-adjoint \(K\) gives
\[
U_t=e^{-itK},\qquad
\boxed{\alpha_t(A)=U_t^*AU_t=e^{itK}Ae^{-itK}.}
\tag{PV9}
\]
These are genuine \(*\)-automorphisms of the represented \(B(\mathcal H)\), and \(\omega\alpha_t=\omega\). With this Heisenberg convention,
\[
q(\alpha_t(A))=e^{itK}q(A).
\]
The sign is opposite to the Schrödinger vector unitary \(U_t\). Analytic continuation applies to the returned Hilbert semigroup \(e^{-sK}\); it does not assert that \(\mathcal T_s\), or the superoperator \(e^{it\mathcal L}\), is this automorphism group.

This avoids the specific obstruction in [[algebra/matrix-symbol-realization-and-the-clock-algebra|the tracial symbol realization]]. There the tracial Hilbert space has dimension \(d^2\), and represented left multiplication is a proper subalgebra of its full operator algebra; the returned phase clock need not normalize it. Here the nonfaithful pure-state quotient has dimension \(d\), and its represented algebra is already all of \(B(\mathcal H)\).

[[algebra/faithful-stationary-states-and-the-positive-clock|Faithful-state clock rigidity]]
gives the general theorem behind that distinction: on a faithful
stationary cyclic–separating implementation, an algebra-normalizing
generator has both spectral signs. The pure state here is deliberately
not faithful on the invariant whole algebra.

Nor does this contradict [[algebra/faithful-descent-rigidity-and-noiseless-unitarity|faithful-descent rigidity]]: \(q\) is not a faithful conditional expectation, its real-parameter return is a contraction rather than a unitary compression, and the automorphism arises through a distinct analytic clock arrow. This is a different state and construction, not the earlier depolarizing process reinterpreted in the same representation.

## The row must still control every nonvacuum direction

The complete ground kernel is
\[
\ker K=\bigcap_a\ker L_a.
\tag{PV10}
\]
If this is \(\mathbb C\Omega\), the finite returned generator has a positive centered gap. Its exact quantitative condition is
\[
\boxed{
K\ge\delta(I-P_\Omega)
\quad\Longleftrightarrow\quad
\sum_a\|L_a\psi\|^2\ge2\delta\|\psi\|^2
\quad(\psi\perp\Omega).
}
\tag{PV11}
\]
A family needs the same \(\delta>0\) uniformly; nonzero response in each individual member is insufficient. For example, on \(\mathbb C^3\),
\[
L_1=\sqrt2\,|0\rangle\langle1|,\qquad
L_2=\sqrt{2\varepsilon}\,|0\rangle\langle2|
\]
give \(K=\operatorname{diag}(0,1,\varepsilon)\). The vacuum is unique for \(\varepsilon>0\), one rate stays fixed, and the gap tends to zero.

If the row is primitive data and has a unique common null line, it determines the vacuum up to phase as well as \(K\). But any chosen positive \(K\) annihilating \(\Omega\) can conversely be factored by \(L=\sqrt{2K}\). A substantive application must restrict the allowed rows; positivity and factorization alone do not select a mass.

## One two-level row, and what its factorization does not fix

Take \(\Omega=|0\rangle\), \(\gamma>0\), and
\[
L=\sqrt\gamma\,|0\rangle\langle1|,\qquad
K=\frac\gamma2|1\rangle\langle1|.
\]
For \(A=\begin{pmatrix}a&b\\c&d\end{pmatrix}\), the full process is
\[
\boxed{
\mathcal T_t(A)=
\begin{pmatrix}
a&e^{-\gamma t/2}b\\
e^{-\gamma t/2}c&e^{-\gamma t}d+(1-e^{-\gamma t})a
\end{pmatrix}.
}
\tag{PV12}
\]
It is amplitude damping, with returned Hilbert gap \(\gamma/2\). Its inverse sends
\(|0\rangle\langle0|\) to
\(|0\rangle\langle0|-(e^{\gamma t}-1)|1\rangle\langle1|\), which is not positive for \(t>0\).

Replace \(L\) by \(L'=\sqrt\gamma\,|1\rangle\langle1|\). The same \(K\), vacuum quotient, Schwarz response and Hilbert clock remain, but the whole process is dephasing and fixes every diagonal matrix. Therefore uniqueness of the ground of \(K\) does not imply uniqueness of the stationary state of \(\mathcal T_t\).

More generally, a unitary \(V\) on the row's output space sends
\(\mathsf L\mapsto V\mathsf L\) without changing \(K\). It preserves the whole jump map only when the relevant conjugation leaves
\(\mathsf L^*(I_r\otimes A)\mathsf L\) unchanged. In particular, a unitary mixing only the channel labels, \(V=v\otimes I\), leaves \(\mathcal L\) unchanged; a general output rotation need not. The two-level rows above are related by an output Pauli flip. The quadratic response does not uniquely specify the full jump law.

Even for amplitude damping, irreversible UCP evolution does not force monotone von Neumann entropy. Starting its dual process at \(|1\rangle\langle1|\) gives eigenvalues \(e^{-\gamma t}\) and \(1-e^{-\gamma t}\). Their binary entropy rises from zero to \(\log2\), then falls back to zero. This state functional is not the stationary Schwarz loss in (PV8).

## A row stabilizer preserves both the process and the vacuum

Let a compact connected semisimple Lie group \(G\) have a continuous unitary representation \(U(g)\) on \(\mathcal H\). Suppose conjugation preserves the loss row up to unitary mixing of its channel labels:
\[
\boxed{U(g)^*L_aU(g)=\sum_bv_{ab}(g)L_b,\qquad v(g)\in U(r).}
\tag{PV13}
\]
No independent group law for a chosen mixing matrix \(v(g)\) is needed for the following pointwise identities. Unitarity of each \(v(g)\) gives
\[
U(g)^*KU(g)=K,\qquad
\mathcal L\bigl(U(g)AU(g)^*\bigr)
=U(g)\mathcal L(A)U(g)^*.
\tag{PV14}
\]
Thus the group preserves the entire UCP law, the positive response and its clock, not just an accidentally symmetric \(K\).

If \(\bigcap_a\ker L_a=\mathbb C\Omega\), then (PV13) preserves that line. Consequently \(U(g)\Omega=\chi(g)\Omega\) for a continuous character \(\chi:G\to U(1)\). Its derivative vanishes because a semisimple Lie algebra equals its commutator algebra, whereas the Lie algebra of \(U(1)\) is abelian. Connectedness then forces \(\chi=1\). The selected vacuum vector is therefore \(G\)-invariant. Without those group hypotheses only preservation of the vacuum line is guaranteed by this argument.

Here symmetry is a stabilizer of the supplied row, with its channel metric, before taking the quadratic response. The group and covariance hypothesis have not been derived automatically, and no particular \(SU(2)\) or \(SU(3)\) choice is required. An interpretation of this action as gauge symmetry still needs the physical representation and local algebra.

[[algebra/modular-mirror-response-and-the-analytic-domain|Bounded modular mirror rows]]
extend the process construction to arbitrary Hilbert dimension: a finite
bounded row still gives a norm-convergent completely positive Dyson
series on \(B(\mathcal H)\), the quotient intertwiner and the same
Schwarz-response identity. This removes the finite-dimensional carrier
restriction for that bounded-row argument, not the domain and
conservativity obligations for unbounded field rows.

## What locality and a physical return would additionally require

On a declared finite tensor product, if each \(L_a\) has support \(X_a\), then \(L_a^*L_a/2\) has the same support and \(K\) is a sum of support-local positive terms. A common annihilated vacuum and a uniform bound (PV11) remain separate requirements. Tensor supports, a graph, a metric and a physical time unit have not been derived; finite-range interactions also do not automatically give strict relativistic propagation.

[[algebra/local-vacuum-faithfulness-and-the-loss-carrier|The local-faithfulness theorem]]
places a necessary restriction on that interpretation. A nonzero bounded
local observable cannot annihilate a separating vacuum. The same holds
for a closed affiliated operator when the vacuum belongs to its domain.
Consequently the row in a relativistic return cannot simply be identified
with such local annihilating observables everywhere the local vacuum is
faithful. The shared note constructs a finite opposed-factor alternative:
a state-dependent mirror makes the difference between two local actions
annihilate their entangled whole vacuum. Its positive squared response
acts on their relation, not on either local algebra alone.

[[local-loss-rows-and-the-uniform-gap|The local row constructions]] prove this distinction on complete finite tensor carriers: independent loss has a uniform gap, anchored neighboring differences have the same unique vacuum but a closing gap, and a star-supported entangling conjugation retains the uniform gap while making each one-site vacuum restriction faithful. These are actual examples for (PV11), not assumptions that every local row satisfies it.

The construction makes the [[general-causal-action/directed-realization-and-foundational-restart|joint-return question]] concrete: one declared loss row supplies a UCP law, state quotient, quadratic response, positive preparation generator and algebra-preserving analytic clock. It does not construct an obtained outcome, irreversible record order, the origin of a spatial arena, or a four-dimensional Yang–Mills theory. Those are further return obligations on the same proposed physical family, not consequences of calling \(L_a\) a loss.

[[vacuum_loss_receipt.py|The exact finite receipt]] and
[[vacuum-loss-receipt-output.txt|its output]] check the quotient,
Schwarz normalization, actual damping channels, distinct same-response
processes, clock products, channel mixing and local row examples.
The all-size statements and complete-positivity construction have their
proofs in the notes, not merely in these finite tests.
