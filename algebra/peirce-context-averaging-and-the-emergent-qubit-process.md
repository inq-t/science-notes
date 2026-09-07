# Peirce Context Averaging and the Emergent Qubit Process

Fixing a rank-two idempotent in the Albert algebra leaves a nine-dimensional family of trace-free corner directions. Comparing all compatible complex rank-two contexts with invariant weight returns an exact qubit depolarizer with centered eigenvalue \(1/3\). Its unit-rate Poisson process has gap \(2/3\) and a calculable positive-cone interior margin. Individual context comparisons need only be positive Jordan maps; complete positivity is proved for the averaged local return. The process shape is therefore constrained by a specified whole–context comparison, although the invariant context law, physical clock and field realization remain additional choices.

## Fix the Peirce corner, not the complete flag

Let \(J=\mathfrak h_3(\mathbb O)\) be the compact Euclidean Albert algebra with unit \(\mathbf1\) and canonical trace. Use a selected order-three automorphism \(w\), its complex fixed context \(B\), and its positive retraction

\[
E=\frac{I+w+w^2}{3},\qquad
B=\operatorname{Fix}(w)\cong\mathfrak h_3(\mathbb C).
\tag{PA1}
\]

The [[exceptional-context-response|exceptional retraction theorem]] supplies positivity, trace preservation, orthogonal projection and the \(B\)-module identity for \(E\).

Choose a trace-two idempotent \(p\in B\). Its complement \(e=\mathbf1-p\) is primitive. The Peirce corner and marked complex corner are

\[
\mathcal P=J_1(p)=J_0(e)\cong\mathfrak h_2(\mathbb O),
\qquad
X_0=B\cap\mathcal P\cong\mathfrak h_2(\mathbb C).
\tag{PA2}
\]

The unit of both corners is \(p\), not the Albert unit \(\mathbf1\). The [[contemporary-puzzles/yang-mills-mass-gap/jordan-idempotency-and-the-stabilizer-gap|primitive Peirce dimensions and stabilizer]] give
\(\dim\mathcal P=10\) and
\[
G_p=\operatorname{Stab}_{F_4}(p)
=\operatorname{Stab}_{F_4}(e)\cong\operatorname{Spin}(9).
\tag{PA3}
\]

The marked flag \((p,w)\) has a smaller stabilizer. The construction below keeps \(p\) fixed while allowing \(w\) and \(B\) to move; it is not an average over symmetries fixing the entire flag.

With \(\tau_{\mathcal P}=\operatorname{tr}_J/2\), the rank-two corner is the spin factor

\[
\mathcal P=\mathbb Rp\oplus V,\qquad \dim V=9,
\]
\[
(t,v)\circ(s,z)=(ts+\langle v,z\rangle,\;tz+sv),
\qquad
\tau_{\mathcal P}(t,v)=t.
\tag{PA4}
\]

Its positive cone is \(t\geq\|v\|\). The marked corner has the form
\(X_0=\mathbb Rp\oplus V_0\), where \(V_0\subset V\) has dimension three. Every three-plane \(W\subset V\) gives a spin-factor Jordan subalgebra \(\mathbb Rp\oplus W\cong\mathfrak h_2(\mathbb C)\).

## The stabilizer supplies every rotation of the nine directions

The required action can be checked without identifying a group solely by its dimension. For pure vectors \(a,b\in V\), viewed as elements of \(\mathcal P\), the [[primitive-peirce-response|Jordan inner derivation]]
\(\mathcal D_{a,b}=[L_a,L_b]\) fixes \(p\). On the spin factor,

\[
\mathcal D_{a,b}(t,v)
=\bigl(0,\;a\langle b,v\rangle-b\langle a,v\rangle\bigr).
\tag{PA5}
\]

These elementary skew operators span \(\mathfrak{so}(V)\). Their exponentials are Albert automorphisms fixing \(p\), so the induced \(G_p\)-action contains \(SO(V)\). Conversely it preserves the spin-factor product, unit and positive trace metric; its connected action on \(V\) lies in \(SO(V)\). Therefore it acts on \(V\) through the full vector rotation group \(SO(9)\).

In particular this action is irreducible and moves \(V_0\) through all three-planes. The nine directions are directions of the rank-two Jordan corner, not nine asserted spatial dimensions.

## Context retractions become three-plane projections

For \(g\in G_p\), set

\[
E_g=gEg^{-1},\qquad
\mathsf E_g=E_g|_{\mathcal P},\qquad
V_g=gV_0.
\tag{PA6}
\]

Since \(p\in B\), the module identity makes \(E\) commute with \(L_p\); hence it preserves \(\mathcal P\). The same holds for \(E_g\) because \(gp=p\). Thus \(\mathsf E_g\) is a positive, unital, trace-preserving orthogonal Jordan retraction onto
\(\mathbb Rp\oplus V_g\). In the spin-factor coordinates,

\[
\mathsf E_g(t,v)=(t,P_gv),
\tag{PA7}
\]

where \(P_g\) is the Euclidean projection onto \(V_g\).

Compare the marked context with the moving context and return:

\[
\Phi_g
=\mathsf E_0\mathsf E_g\mathsf E_0|_{X_0},
\qquad
\Phi_g(t,v)=(t,P_0P_gP_0v),\quad v\in V_0.
\tag{PA8}
\]

Here \(\mathsf E_0=E|_{\mathcal P}\) and \(P_0\) projects onto \(V_0\). The subscript zero marks the original context, not the zero map. Each comparison is positive, unital and trace-preserving on the real Hermitian corner. Its trace-Hilbert implementation is a positive self-adjoint contraction.

Unlike the [[contemporary-puzzles/yang-mills-mass-gap/two-expectation-angle-process|associative two-expectation theorem]], these maps have not been granted a common completely positive associative realization. That distinction matters below.

## Invariant comparison fixes the local channel

Declare normalized Haar measure \(dg\) on \(G_p\), and define
\[
\overline\Phi=\int_{G_p}\Phi_g\,dg.
\tag{PA9}
\]

This is an invariant geometric comparison law. It does not assert that ontology samples contexts stochastically, and the marked flag by itself does not force this law.

The average \(\int P_g\,dg\) commutes with every rotation of \(V\), so irreducibility makes it scalar. Its trace is three on a nine-dimensional carrier. Hence

\[
\int_{G_p}P_g\,dg=\frac13I_V,
\qquad
\boxed{\overline\Phi(t,v)=(t,v/3).}
\tag{PA10}
\]

This is a different ratio from the full \(F_4\) context-frame coefficient \(9/13\). Here the carrier is the nine-dimensional trace-free Peirce corner and the retained projection has rank three. Neither coefficient may be transferred to the other's carrier.

Identify \(X_0\) with the Hermitian part of \(M_2(\mathbb C)\), with \(p=I_2\) and \(\tau=\operatorname{Tr}/2\). Its complex-linear extension is

\[
\overline\Phi(A)
=\tau(A)I_2+\frac13\bigl(A-\tau(A)I_2\bigr)
=\frac12A+\frac16\sum_{j=1}^3\sigma_jA\sigma_j.
\tag{PA11}
\]

The final formula is an explicit convex combination of unitary conjugations. It proves that the averaged local return is UCP, trace-preserving and trace-symmetric. Complete positivity has been established at this target, not assumed for every upstream Jordan comparison.

[[depolarizing-return-and-the-classical-record-threshold|The classical-record factorization]] proves a further property of this exact return: centered contraction \(1/3\) is precisely the qubit entanglement-breaking boundary. The channel factors through a declared classical outcome distribution and a preparation map. The readout remains informationally complete, and neither the factorization nor the averaged channel selects an obtained outcome. The octonionic \(3/9\) ratio reaches this boundary only for the stipulated invariant context law.

## A positive comparison can fail complete positivity

Choose an orthonormal frame of \(V\) with
\[
V_0=\operatorname{span}(e_1,e_2,e_3),\qquad
V_g=\operatorname{span}(e_1,e_2,e_4).
\]

A rotation in the \(e_3,e_4\) plane realizes this \(V_g\), and (PA5) lifts the needed rotation to the \(p\)-stabilizer. The corresponding comparison has Bloch matrix

\[
P_0P_gP_0|_{V_0}=\operatorname{diag}(1,1,0).
\tag{PA12}
\]

It contracts the Bloch ball and is therefore positive. But its complex-linear extension has normalized Choi eigenvalues
\[
\frac34,\quad \frac14,\quad \frac14,\quad-\frac14.
\tag{PA13}
\]

These follow by applying the Pauli-diagonal map to one factor of the normalized maximally entangled two-qubit state. The negative eigenvalue rules out complete positivity. The witness is geometrically present in the actual context orbit, not an arbitrary unrelated positive map.

The averaged channel (PA11) avoids this failure by its explicitly computed form. Positivity of an individual Jordan projection is not sufficient to invoke associative quantum-channel theorems.

## Two normalized process constructions

Let \(P_\tau A=\tau(A)I_2\). Unit-rate Poissonization of the derived channel gives

\[
T_s=\exp\bigl[s(\overline\Phi-I)\bigr],\qquad
L_{\rm P}=I-\overline\Phi=\frac23(I-P_\tau),
\]
\[
\boxed{
T_s=P_\tau+e^{-2s/3}(I-P_\tau),\qquad
\delta_{\rm P}=\frac23.}
\tag{PA14}
\]

The Poisson series is a convex combination of powers of \(\overline\Phi\), so \(T_s\) is UCP. Equivalently the displayed depolarizing formula proves it directly. Its only fixed vectors are the scalar matrices.

For the normalized positive base \(\mathcal B=\{B\geq0:\tau(B)=1\}\), write \(\mathscr Q(B)=\tau(B^2)/\tau(B)^2\). The [[qubit-cone-interiorization-and-the-clock-gap|same-carrier interiorization theorem]] now gives

\[
\boxed{
\sup_{B\in\mathcal B}\bigl[\mathscr Q(T_sB)-1\bigr]
=e^{-4s/3},\qquad
\inf_{B\in\mathcal B}\det(T_sB)=1-e^{-4s/3}.}
\tag{PA15}
\]

This no longer begins with freely chosen Pauli jump rates: the selected Peirce corner and the declared invariant context family determine the normalized channel and its full centered spectrum.

A discrete step has a different exact rate convention:

\[
L_{\log}=-\log\overline\Phi
=(\log3)(I-P_\tau),\qquad
e^{-sL_{\log}}=P_\tau+3^{-s}(I-P_\tau).
\tag{PA16}
\]

In this case the interpolation is UCP by its explicit depolarizing form; logarithms of arbitrary UCP maps do not automatically generate UCP semigroups. At integer \(s=n\), (PA16) is \(\overline\Phi^{\,n}\), whereas one unit of Poisson time in (PA14) averages over numbers of channel steps. The constants \(2/3\) and \(\log3\) describe these distinct normalizations. They are not two physical predictions. Either positive self-adjoint generator also supplies the corresponding finite Hilbert clock \(e^{-itL}\), subject to the algebra-automorphism distinction in the interiorization theorem.

Strict contraction is not exact erasure of the input. The averaged return has nonzero eigenvalues \(1\) and \(1/3\), so it is linearly invertible, as are both semigroups at every finite \(s\). Its inverse is not positive: it sends the positive matrix \(I_2+\sigma_3\) to \(I_2+3\sigma_3\), which has a negative eigenvalue. For positive time the semigroup inverses fail positivity in the same way. Thus inverse evolution is unavailable within positive, and hence within completely positive, maps on the full corner; it remains available as a linear map on the range. Individual context projections have genuine kernels, and the infinite-time limit \(P_\tau\) does too, but their average and its finite-time process do not. No stochastic ontology, outcome selection or literal loss of all reconstructible input information follows from (PA14).

## Why fixed-flag averaging is not this construction

For \(h\in H=\operatorname{Stab}_{F_4}(p,w)\), one has
\[
E_h=E,\qquad
\Phi_h|_{X_0}=I_{X_0}.
\tag{PA17}
\]

Averaging retractions over the fixed flag stabilizer therefore supplies no decay of retained distinctions. It only repeats the original context. Averaging the stabilizer's conjugation action on \(X_0\) is a different operation: its usual \(SU(2)\) corner action can depolarize noninvariant qubit directions, but gauge-invariant observables are fixed by gauge averaging.

The process in (PA9) instead compares inequivalent complex contexts while fixing their common Peirce unit. It deliberately leaves the smaller flag stabilizer. This is why it can detect marked-context distinctions that a single retraction, or its stabilizer orbit, leaves untouched.

The distinction persists for fields. Every fiberwise unital extension fixes \(f(U)I_2\) for arbitrary scalar configuration functions \(f\); it does not control gauge-invariant Wilson observables merely by having a finite matrix gap. [[global-local-response-reconstruction/exceptional-context-analysis-of-gauge-gradients|Differentiated context analysis]] owns the existing field-sensitive bridge and its actual-law coercivity problem.

## What is constrained, and what remains to construct

The exact new relation is between a specified orbit of positive Jordan context comparisons and a completely positive local process with a fixed normalized spectral shape. The full orbit and its invariant weighting are load-bearing: a context law concentrated at the marked corner gives \(\Phi=I\), not (PA10). If a probability law dominates \(\alpha\,dg\), then its averaged positive Hilbert return has a Poisson-form lower bound at least \(2\alpha/3\) on the centered corner, but complete positivity of that differently averaged map must still be checked.

Replacing \(s\) by \(\kappa s\) changes the clock rate. Neither an overall physical normalization, an actually obtained fact, a persistent record nor the observed context distribution is fixed by the finite theorem. The orientation \(w\leftrightarrow w^{-1}\) is also invisible to (PA1)'s even retraction; it cannot be recovered from the averaged rate.

A further theory must select and transport these context comparisons, identify the relevant state and field carrier, and establish a common dynamics across local realizations. The qubit determinant margin in (PA15) is a transfer statement on matrix observables, not a Lorentz-invariant mass bound or a four-dimensional Yang–Mills continuum result.

[[directed-analytic-realization/context_transport_receipt.py|The context–transport receipt]] checks the coordinate-projection mean, CP and non-CP Pauli weights, and the classical-factorization arithmetic. [[directed-analytic-realization/context-transport-receipt-output.txt|Its output]] does not treat a finite coordinate average as numerical verification of the continuous exceptional orbit; (PA5) and the invariant trace argument prove that step.
