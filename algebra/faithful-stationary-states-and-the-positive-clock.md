# Faithful Stationary States and the Positive Clock

A unitary group fixing a cyclic and separating vector and preserving its von Neumann algebra has a generator with spectrum symmetric about zero. If that same generator is nonnegative, it must vanish. This is an exact restriction on a particular state, algebra and implementation—not a prohibition of positive physical Hamiltonians. It explains why a positive response on a faithful matrix-symbol carrier cannot simply become an algebra-preserving clock, while leaving open positive-energy realizations with a nonfaithful global vacuum or time-translated local algebras.

## The algebra and the stationary vector must be specified together

Let \(M\subseteq B(\mathcal H)\) be a von Neumann algebra and let \(\Omega\) be a unit vector that is cyclic and separating for \(M\):
\[
\overline{M\Omega}=\mathcal H,\qquad
x\Omega=0,\ x\in M\ \Longrightarrow\ x=0.
\tag{FS1}
\]
Its vector state \(\varphi(x)=\langle\Omega,x\Omega\rangle\) is faithful and normal on \(M\). Conversely, the GNS realization of a faithful normal state on a von Neumann algebra supplies such a vector.

Suppose \(U_t=e^{-itH}\), \(t\in\mathbb R\), is a strongly continuous unitary group with
\[
U_t\Omega=\Omega,\qquad U_tMU_t^*=M
\quad\text{for every }t\in\mathbb R.
\tag{FS2}
\]
The second condition is equality with the same algebra for the whole group, not covariance among different region algebras or one-sided inclusion.

**Theorem.** If \(J\) is the modular conjugation of \((M,\Omega)\), then
\[
\boxed{
J\operatorname{Dom}H=\operatorname{Dom}H,\qquad
JHJ=-H.
}
\tag{FS3}
\]
In particular,
\[
\boxed{
\sigma(H)=-\sigma(H),\qquad
H\ge0\ \Longrightarrow\ H=0,\quad U_t=I.
}
\tag{FS4}
\]
Neither traciality, finite dimension, detailed balance nor identification of \(U_t\) with modular flow is assumed.

## Tomita's operator carries the proof

On the dense core \(M\Omega\), define the antilinear operator
\[
S_0(x\Omega)=x^*\Omega.
\tag{FS5}
\]
Cyclicity makes this core dense; separatingness makes the rule well-defined. The cyclic–separating hypotheses give its closed Tomita extension \(S=\overline{S_0}\), with polar decomposition
\[
S=J\Delta^{1/2}.
\tag{FS6}
\]
Here \(J\) is antiunitary, \(J^2=I\), and \(\Delta=S^*S\) is the positive modular operator. The [[library/the-standard-form-of-von-neumann-algebras/inq|standard-form source]] owns the surrounding representation framework; the intertwining needed here follows directly on the Tomita core.

Write \(\alpha_t(x)=U_txU_t^*\). Equation (FS2) gives
\[
U_t(x\Omega)=\alpha_t(x)\Omega,
\]
so \(U_t(M\Omega)=M\Omega\), and
\[
S_0U_t(x\Omega)
=\alpha_t(x)^*\Omega
=U_tx^*\Omega
=U_tS_0(x\Omega).
\tag{FS7}
\]

This identity extends with its domains, not merely formally. If \(\xi\in\operatorname{Dom}S\), take \(x_n\Omega\to\xi\) and \(x_n^*\Omega\to S\xi\). Applying \(U_t\) to this graph-approximating sequence and using (FS7) shows
\[
U_t\xi\in\operatorname{Dom}S,\qquad SU_t\xi=U_tS\xi.
\]
Applying the same argument to \(U_{-t}\) proves equality of domains. Thus
\[
U_tSU_t^*=S.
\tag{FS8}
\]
Taking adjoints yields the corresponding statement for \(S^*\). Consequently \(U_t\Delta U_t^*=\Delta\), including its domain, and uniqueness of the polar decomposition in (FS6) gives
\[
U_tJU_t^*=J,\qquad JU_tJ=U_t.
\tag{FS9}
\]

Antiunitarity changes the sign of \(i\). The spectral calculus therefore gives
\[
Je^{-itH}J=e^{+itJHJ}=e^{-itH}.
\]
Uniqueness of the Stone generator proves (FS3), including the domain equality. Equivalently, for every Borel set \(B\subseteq\mathbb R\),
\[
JE_H(B)J=E_H(-B),
\tag{FS10}
\]
where \(E_H\) is the spectral measure of \(H\). If \(H\ge0\), the negative spectral projection vanishes, so its positive partner vanishes as well. Only the zero spectral subspace remains, proving (FS4).

The antilinear relation does not assert a physical time-reversal symmetry. It follows from the adjoint operation and this faithful stationary implementation, whether or not a proposed physical model has a time-reversal symmetry.

## A faithful stationary density gives differences of energies

The finite example makes the carrier distinction explicit. Let \(M_d(\mathbb C)\) have faithful state
\[
\varphi(A)=\operatorname{Tr}(\rho A),\qquad \rho>0,\quad\operatorname{Tr}\rho=1.
\]
Represent it by left multiplication on the Hilbert–Schmidt space:
\[
\pi(A)T=AT,\qquad \Omega=\rho^{1/2},\qquad J(T)=T^*.
\tag{FS11}
\]
Since \(\rho\) is invertible, \(\Omega\) is cyclic and separating. Choose \(K=K^*\) with \([K,\rho]=0\). The automorphism
\[
\alpha_t(A)=e^{-itK}Ae^{itK}
\]
preserves \(\varphi\), and its \(\Omega\)-fixing GNS implementation is
\[
U_tT=e^{-itK}Te^{itK},\qquad
\boxed{HT=KT-TK.}
\tag{FS12}
\]
For eigenvectors of \(K\), the matrix unit \(|i\rangle\langle j|\) has eigenvalue \(k_i-k_j\). Exchanging \(i,j\) reverses that sign. Directly,
\[
JHJ(T)=(KT^*-T^*K)^*=TK-KT=-H(T).
\]
A nonconstant \(K\) therefore gives both positive and negative GNS energies.

There is no obstruction to \(K\ge0\) on the original space \(\mathbb C^d\). Shifting \(K\) by a scalar leaves (FS12) unchanged: the faithful-state implementation carries energy differences, not the one-sided spectrum of the original \(K\). The [[positive-energy-pairs-and-the-neutral-gap|positive-pair construction]] further distinguishes this commutator from the positive sum \(AT+TA\) on a Hilbert–Schmidt amplitude carrier.

Even on the Hilbert–Schmidt space, the alternative implementation
\[
\widetilde U_tT=e^{-itK}T
\]
has nonnegative generator \(T\mapsto KT\) when \(K\ge0\), and normalizes the same left matrix algebra. But it does not fix \(\rho^{1/2}\) unless \(K=0\). Invariance of the density state under the induced automorphism is not the same hypothesis as invariance of this implementing vector under this chosen unitary.

## The matrix-symbol clock is one instance, not the whole theorem

The [[matrix-symbol-realization-and-the-clock-algebra|matrix-symbol realization]] transports precisely the tracial left representation to its affine-symbol carrier. Its constant vector is therefore separating as well as cyclic. The positive response generator on that carrier is \(I-P_1\).

If the associated continuous group preserved that represented matrix algebra, (FS4) would force \(I-P_1=0\), which fails for \(d\ge2\). The earlier matrix-unit calculation gives the stronger pointwise statement that normalization occurs only at the isolated identity times. The present theorem explains why no nontrivial continuous positive clock can preserve that algebra with that faithful stationary vector, independently of the particular depolarizing formula.

This theorem is distinct from [[faithful-descent-rigidity-and-noiseless-unitarity|faithful descent rigidity]]. That result starts with a conditional expectation and a whole UCP process, and proves that an exactly automorphic expected return was already noiseless. The present result starts after an automorphism and its stationary implementation have been obtained, and restricts the sign of its generator. No expectation or noisy whole process is needed for (FS3).

## Exact boundaries and viable changes of architecture

**Cyclicity and separatingness do different work.** With a separating but noncyclic vector, the theorem applies on \(\mathcal H_0=\overline{M\Omega}\). That subspace reduces \(U_t\) under (FS2), and a positive generator vanishes there. It need not vanish on an unused orthogonal complement. With a cyclic but nonseparating vector, \(S_0(x\Omega)=x^*\Omega\) need not be well-defined, so the argument can fail on the actual generated carrier.

**The vacuum energy must be anchored.** If instead
\[
U_t\Omega=e^{-itE_0}\Omega,
\]
apply the theorem to \(e^{itE_0}U_t\). It gives symmetry of \(H-E_0I\) about zero. If \(\Omega\) is a ground vector, meaning \(H\ge E_0I\), then \(H=E_0I\). Mere invariance of the vector state, or a semibounded generator without a ground-state condition at \(\Omega\), does not supply this conclusion.

**An invariant global algebra can have a nonfaithful vacuum.** On \(\mathcal H=\mathbb C^2\), take
\[
M=B(\mathbb C^2),\qquad
\Omega=|0\rangle,\qquad
H=m|1\rangle\langle1|,\quad m>0.
\tag{FS13}
\]
The group \(e^{-itH}\) fixes \(\Omega\), normalizes \(M\), and has a genuine gap \(m\). The vector is cyclic but not separating: \(|1\rangle\langle1|\Omega=0\). Its normal state on \(M\) is not faithful. More generally a nontrivial pure vector vacuum on an irreducible global algebra \(B(\mathcal H)\) has this same failure of separatingness. Restricting (FS13) to the support corner \(|0\rangle\langle0|M|0\rangle\langle0|\) makes the state faithful only by discarding the excited carrier.

[[directed-analytic-realization/pure-vacuum-loss-and-the-returned-clock|Pure-vacuum loss]] gives a constructive version of this alternative. A row \(L_a\Omega=0\) returns \(K=\frac12\sum_aL_a^*L_a\) through the Hilbert quotient \(A\mapsto A\Omega\), with a faithful defining representation but nonfaithful vector state. The same \(K\) generates an algebra-preserving analytic clock. Its [[directed-analytic-realization/local-loss-rows-and-the-uniform-gap|local row examples]] distinguish a uniform gap from a unique vacuum with a closing gap; the changed state does not itself guarantee coercivity.

**Faithful local states need not live on invariant local algebras.** A covariant net may have a cyclic and separating vacuum for each bounded-region algebra while
\[
U_tM(\mathcal O)U_t^*=M(\mathcal O+t),
\tag{FS14}
\]
not \(M(\mathcal O)\). Such covariance does not satisfy (FS2) on one bounded region. Conversely, passing to an invariant global algebra does not preserve the separating property automatically. The theorem therefore cannot be applied by taking faithfulness from one algebra and time invariance from another.

**One-sided inclusion is not normalization.** A group can satisfy
\[
U_tMU_t^*\subsetneq M\qquad(t>0)
\]
without satisfying equality for all real \(t\). Then the core argument need not extend in both directions, and (FS8)--(FS9) do not follow. [[sufficient-reason/algebraic-arrow-of-time|Half-sided inclusion]] provides an existing algebraic architecture of this kind. Its independently supplied dilation covariance has [[the-grain-of-causal-scale/causal-spectrum|its own scoped spectral consequences]]; evading the present theorem is not by itself a proof of a positive gap.

The constructive lesson is to return the state, observable algebra and clock implementation together. A positive response form plus a faithful stationary algebra is not sufficient to identify its imaginary-time continuation with physical clock dynamics. The faithful implementation has a two-sided spectrum; a one-sided vacuum spectrum requires a different declared relationship among those objects.
