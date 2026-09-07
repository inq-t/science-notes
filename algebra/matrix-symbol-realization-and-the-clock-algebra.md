# Matrix-Symbol Realization and the Clock Algebra

Rescaled purification symbols give an exact Hilbert isometry that realizes a supplied matrix algebra as faithful positive operators, with its original norm and tracial state. These operators are not pointwise multiplication by the symbols. The same response returns a depolarizing heat evolution, but its associated unitary group neither preserves the represented matrix algebra nor respects a bounded-range interpretation across arbitrarily separated tensor factors. The result is a constructive finite operator return with an explicit remaining clock-algebra problem, not an obstruction to positive realization itself.

## The normalized symbols carry the tracial Hilbert geometry

Use [[purification-descent-and-the-matrix-response|matrix purification descent]] with \(K\ge d\ge2\), \(D=dK\), induced state law \(\nu_{d,K}\), and normalized generator \(\widehat L=L_{d,K}/D\). For \(A\in M_d(\mathbb C)\), put
\[
\tau(A)=\frac{\operatorname{Tr}A}{d},\qquad
A=a_0I+A_0,\qquad a_0=\tau(A),\quad \tau(A_0)=0.
\]
The affine symbol \(f_A(\rho)=\operatorname{Tr}(\rho A)\) is extended complex-linearly. The spherical fourth moment gives
\[
\nu(f_{A_0})=0,\qquad
\nu(\overline{f_{A_0}}f_{B_0})
=\frac{\tau(A_0^*B_0)}{D+1}.
\]
Define
\[
\boxed{J_K(A)=a_0+\sqrt{D+1}\,f_{A_0}.}
\tag{MS1}
\]
Then
\[
\boxed{
\langle J_K(A),J_K(B)\rangle_{L^2(\nu)}
=\bar a_0b_0+\tau(A_0^*B_0)=\tau(A^*B).
}
\tag{MS2}
\]
Thus \(J_K\) is a unital complex-linear Hilbert isometry from the tracial matrix Hilbert space into \(L^2(\nu)\). It also takes matrix adjoints to complex conjugates. Its image \(E_K\) is the full complex affine-symbol subspace, of dimension \(d^2\); the normalization, not this subspace as a vector space, depends on \(D\).

The exact affine evolution is
\[
\boxed{
e^{t\widehat L}J_K=J_K\Phi_t,\qquad
\Phi_t(A)=a_0I+e^{-t}A_0,\qquad t\ge0.
}
\tag{MS3}
\]
The map \(\Phi_t\) is the tracial depolarizing channel. This return remains nontrivial for every \(K\); concentration of the density-parameter law does not destroy its finite Hilbert carrier.

There is also exact partial-trace compatibility. If \(d=d_A d_B\), \(R(\rho)=\operatorname{Tr}_B\rho\), and \(K_A=d_BK\), regrouping the same purification gives \(d_AK_A=D\) and
\[
\boxed{J_{d,K}(A\otimes I_B)=R^*J_{d_A,K_A}(A).}
\tag{MS4}
\]
Indeed both the normalized trace of \(A\otimes I_B\) and the factor \(\sqrt{D+1}\) agree with those on the right. Its symbol is \(f_A\circ R\). The isometry and the channel therefore commute with these readouts without fitting a new duration.

## Positive operators are returned, not pointwise multiplication

Put \(\Omega=J_K(I)=1\) and define operators on \(E_K\) by
\[
\boxed{\pi_K(B)J_K(A)=J_K(BA).}
\tag{MS5}
\]
This transports left multiplication through the isometry. Consequently
\[
\pi_K(BC)=\pi_K(B)\pi_K(C),\qquad
\pi_K(B^*)=\pi_K(B)^*,\qquad
\pi_K(I)=I_{E_K},\qquad
\boxed{\|\pi_K(B)\|=\|B\|.}
\tag{MS6}
\]
For the norm equality, the upper bound is the Hilbert–Schmidt product inequality; a rank-one matrix whose range is a maximal right-singular-vector direction of \(B\) attains the lower bound. Faithfulness follows already from \(\pi_K(B)\Omega=J_K(B)\).

For \(B\ge0\),
\[
\langle J_K(A),\pi_K(B)J_K(A)\rangle
=\tau(A^*BA)\ge0.
\]
Thus \(\pi_K(B)\) is a positive Hilbert-space operator. The vector \(\Omega\) is cyclic, and its state on the represented algebra is
\[
\boxed{\langle\Omega,\pi_K(B)\Omega\rangle=\tau(B).}
\tag{MS7}
\]
These recover the supplied algebra's product, adjoint, norm, positivity and tracial state exactly on one carrier.

None of this makes the symbols themselves a pointwise copy of the matrix algebra. For a qubit,
\[
J_K(\sigma_3)^2=(D+1)x_3^2\ne J_K(I)=1.
\]
The unchanged [[jordan-covariance-and-the-entropy-weighted-ball|qubit affine \(\star\)-product]] gives
\(J_K(\sigma_3)\star J_K(\sigma_3)=D+1\), not one; using such a symbol product requires transporting it by \(J_K\).

Even positivity has to be assigned to the right object:
\[
I+\sigma_3\ge0,\qquad
J_K(I+\sigma_3)=1+\sqrt{D+1}\,x_3<0
\quad\text{for}\quad x_3<-1/\sqrt{D+1}.
\tag{MS8}
\]
This is an open set of positive reference measure. Nevertheless \(\pi_K(I+\sigma_3)\ge0\). The function in (MS8) is that positive operator applied to \(\Omega\); operator positivity does not require the resulting function to be pointwise nonnegative.

The construction therefore provides a genuine positive operator return. Its input is explicit: (MS5) uses the already supplied matrix multiplication \(BA\). This is not a derivation of a unique noncommutative algebra from a commutative ensemble with no further data.

## The positive response does not automatically preserve the clock algebra

On \(E_K\), let \(P_1\) project onto the constant vector. The inherited positive generator and its unitary group are
\[
\boxed{H_K=-\widehat L|_{E_K}=I-P_1,\qquad U_t=e^{-itH_K}.}
\tag{MS9}
\]
The Euclidean semigroup implements (MS3) on vectors \(J_K(A)\). The unitary group, however, satisfies the exact obstruction
\[
\boxed{
U_t\pi_K(M_d)U_t^*=\pi_K(M_d)
\quad\Longleftrightarrow\quad t\in2\pi\mathbb Z.
}
\tag{MS10}
\]
To prove necessity, normalization would define an automorphism \(\alpha_t\). Since \(U_t\Omega=\Omega\), applying the conjugation identity to \(\Omega\) forces
\[
\alpha_t(A)=\tau(A)I+z\bigl(A-\tau(A)I\bigr),\qquad z=e^{-it}.
\]
Multiplicativity on matrix units \(E_{12},E_{21}\) would require
\[
z^2E_{11}=zE_{11}+\frac{1-z}{d}I.
\]
Its \((2,2)\) entry forces \(z=1\) for every \(d\ge2\). Conversely \(z=1\) makes \(U_t=I\). A valid Hilbert unitary clock and a valid positive algebra representation have both been returned, but not an algebra-preserving clock dynamics on this chosen algebra.

[[faithful-stationary-states-and-the-positive-clock|The faithful-state theorem]]
identifies the general cause: this tracial vector is cyclic and separating,
and an algebra-normalizing group fixing such a vector has a generator
whose spectrum is symmetric about zero. It cannot have a nonzero
nonnegative generator. Changing the depolarizing coefficients alone
cannot remove that incompatibility while these hypotheses remain.
[[directed-analytic-realization/pure-vacuum-loss-and-the-returned-clock|The pure-vacuum return]]
uses a different state quotient and does construct a compatible positive
clock. It is a new process/state member, not an unproved continuation of
the present purification law.

## A tensor-factor test identifies the clock's nonlocal coupling

Suppose the supplied matrix algebra has distinct tensor factors. Take nonzero traceless observables \(A\) and \(B\) supported in two different factors, with identities in the others. Then
\([A,B]=0\), \(\tau(AB)=0\), and \(AB\ne0\). Define the Heisenberg translate with an explicit sign convention:
\[
\pi_K(A;t)=U_t^*\pi_K(A)U_t.
\]
Because \(A,B,AB\) are all traceless, direct use of (MS9) gives
\[
\pi_K(A;t)\pi_K(B)\Omega=J_K(AB),\qquad
\pi_K(B)\pi_K(A;t)\Omega=e^{it}J_K(AB).
\]
Therefore
\[
\boxed{
[\pi_K(A;t),\pi_K(B)]\Omega
=(1-e^{it})J_K(AB).
}
\tag{MS11}
\]
The equal-time algebras commute, while this chosen global clock produces unequal-time coupling. Its derivative at zero is already nonzero:
\[
[[H_K,\pi_K(A)],\pi_K(B)]\Omega=-J_K(AB).
\tag{MS12}
\]

If a graph and spatial supports are additionally assigned to many tensor factors, (MS12) rules out a generator built from terms of uniformly bounded range whenever these supports are farther apart than that range. Every term of such a generator touching the support of \(A\) would be disjoint from \(B\), so the double commutator would vanish. Under the tracial tensor identification, the actual generator is instead \(I-\bigotimes_v P_{1,v}\), which depends on all factors together.

The derivative test matters: a nonzero commutator at positive time alone would not rule out a finite-range lattice Hamiltonian, whose evolution can develop small tails. Here the first-order coupling itself reaches any pair of chosen factors, independently of their assigned separation.

Purification supplies no spatial metric or causal relation in the first place. The result is therefore a failure of this particular global clock under a proposed bounded-range spatial interpretation, not a prohibition of local operator realization. A further construction may use appropriate time-translated algebras or different compatible clock data; it must actually establish the intended locality and covariance. Neither the finite operator return nor its positive internal gap is already an interacting field theory or a Yang–Mills mass.

[[directed-analytic-realization/purification_descent_receipt.py|The purification receipt]] checks finite symbol moments, Hilbert isometries, representation products, positivity and clock-commutator identities. [[directed-analytic-realization/purification-descent-receipt-output.txt|Its output]] records the exact arithmetic checks. These corroborate selected finite identities; the arguments above establish their general scope, not a physical field limit.
