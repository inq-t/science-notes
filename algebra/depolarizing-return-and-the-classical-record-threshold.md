# Depolarizing Return and the Classical Record Threshold

The qubit return forced by invariant context averaging in a rank-two octonionic corner lies exactly at the entanglement-breaking threshold. It admits an explicit factorization through a classical outcome distribution, although that readout remains informationally complete and does not select an obtained outcome. This provides a precise connection between context geometry and a possible measurement realization, not an identification of measurement, mass gap and irreversible history.

## The local channel and its classical factorization

On \(M_2(\mathbb C)\), let \(\tau=\operatorname{Tr}/2\) and define the depolarizing channel
\[
\Phi_\lambda(A)=\lambda A+(1-\lambda)\tau(A)I,\qquad 0\le\lambda\le1.
\tag{CR1}
\]
Its trace-adjoint action on density matrices has the same form. For
\(\rho=(I+r\cdot\sigma)/2\), it returns \((I+\lambda r\cdot\sigma)/2\).

Let \(dn\) be normalized area measure on \(S^2\) and
\[
P_n=\frac{I+n\cdot\sigma}{2}.
\]
These are rank-one projections. The positive operator-valued measure \(2P_n\,dn\) is normalized because \(\int P_n\,dn=I/2\). Its declared Born-rule probability density and a preparation map give
\[
(\mathsf M\rho)(n)=2\operatorname{Tr}(P_n\rho)=1+n\cdot r,\qquad
\mathsf P(p)=\int p(n)P_n\,dn.
\tag{CR2}
\]
The sphere moments \(\int n\,dn=0\) and \(\int n_in_j\,dn=\delta_{ij}/3\) imply
\[
\boxed{\mathsf P\mathsf M(\rho)
=\frac12\left(I+\frac13r\cdot\sigma\right)
=\Phi_{1/3}(\rho).}
\tag{CR3}
\]
Thus the channel factors, on states, as
\[
\text{qubit density matrix}
\;\xrightarrow{\mathsf M}\;
\text{classical probability density}
\;\xrightarrow{\mathsf P}\;
\text{qubit density matrix}.
\]
This is an explicit realization through a commutative outcome algebra. The averaging parameter is not asserted to be ontologically random.

A finite factorization is also available. Choose the six directions \(n=\pm e_j\), \(j=1,2,3\), with effects \(P_n/3\). They sum to \(I\), and
\[
p_n=\frac13\operatorname{Tr}(P_n\rho),\qquad
\sum_np_nP_n=\Phi_{1/3}(\rho).
\tag{CR4}
\]
The chosen six-point frame is additional measurement data; the resulting channel is rotation covariant. Six is not being derived as a fundamental count of facts.

## Why this return breaks entanglement

A channel is entanglement-breaking when its application to one part of every finite bipartite state produces a separable state. For a density matrix \(R\) on a qubit and any finite ancilla, (CR3) gives
\[
(\Phi_{1/3}\otimes\operatorname{id})(R)
=\int P_n\otimes
2\operatorname{Tr}_{\rm q}\!\left[
(P_n\otimes I)R(P_n\otimes I)
\right]dn.
\tag{CR5}
\]
Each second factor is positive. The trace weights integrate to one, so this is a mixture of product states, with zero-weight terms omitted. The formula proves entanglement breaking directly, without a general classification theorem.

The threshold is sharp within (CR1). With
\(\Omega=(|00\rangle+|11\rangle)/\sqrt2\), the normalized Choi state is
\[
C_\lambda
=\lambda|\Omega\rangle\langle\Omega|
+\frac{1-\lambda}{4}I_4.
\tag{CR6}
\]
Partial transpose sends \(|\Omega\rangle\langle\Omega|\) to half the swap. The swap has eigenvalue \(+1\) on the three-dimensional symmetric subspace and \(-1\) on the antisymmetric line. Hence
\[
\sigma(C_\lambda^{\,\Gamma})
=\left\{\frac{1+\lambda}{4}\;(\times3),\;
\frac{1-3\lambda}{4}\;(\times1)\right\}.
\tag{CR7}
\]
A separable state has positive partial transpose, since transpose preserves positivity on each product factor. Thus \(\lambda>1/3\) cannot be entanglement-breaking. For \(0\le\lambda\le1/3\),
\[
\Phi_\lambda=3\lambda\Phi_{1/3}+(1-3\lambda)\Phi_0
\]
is a convex combination of the explicit measure-and-prepare return and complete depolarization. Both are entanglement-breaking. Therefore
\[
\boxed{\Phi_\lambda\text{ is entanglement-breaking}
\quad\Longleftrightarrow\quad 0\le\lambda\le\frac13}
\tag{CR8}
\]
within the specified nonnegative channel family. No claim about other channel families is needed.

## The octonionic context ratio lands at this threshold

[[exceptional-state-comparison/peirce-context-averaging-and-the-emergent-qubit-process|Peirce context averaging]]
fixes a rank-two octonionic corner
\(\mathbb Rp\oplus\mathbb R^9\), marks a complex subcorner
\(\mathbb Rp\oplus\mathbb R^3\), and compares its rotated three-planes with invariant weight. The projection rank divided by the ambient trace-free dimension gives the return coefficient
\[
\lambda=\frac39=\frac13.
\tag{CR9}
\]
The same declared geometric return is consequently the channel in (CR3), exactly on the boundary (CR8). Complete positivity and the classical factorization have been proved for its local complex realization, not imposed on every positive Jordan comparison.

More generally, invariant rank-three projection averaging in a spin factor \(\mathbb Rp\oplus\mathbb R^n\), \(n\ge3\), gives \(\lambda=3/n\). The same calculation therefore yields the exact comparator
\[
\boxed{\text{classical measure-and-prepare return}
\quad\Longleftrightarrow\quad n\ge9.}
\tag{CR10}
\]
Here “return” means the isotropic qubit channel just constructed. The trace-free dimensions of rank-two complex, quaternionic and octonionic Hermitian corners are respectively
\[
n=3,\quad5,\quad9,
\qquad
\lambda=1,\quad\frac35,\quad\frac13.
\]
The quaternionic return is CP but fails the entanglement-breaking test; the octonionic one reaches its boundary. These dimensions follow from one diagonal difference plus the real dimension of the off-diagonal division algebra.

This is a meaningful geometric coincidence with an exact proof and an explicitly fixed family. It does not select octonions among all possible algebras, force invariant context sampling, or identify \(n\) with the dimension of spacetime. General spin factors also exist beyond these division-algebra examples. The comparison must not be promoted into uniqueness of ontology.

The boundary is sensitive to the context law. Mixing normalized Haar comparison with weight \(\varepsilon>0\) on the marked context gives
\[
\Phi_\varepsilon=(1-\varepsilon)\Phi_{1/3}+\varepsilon I,
\qquad \lambda_\varepsilon=\frac{1+2\varepsilon}{3}.
\tag{CR10a}
\]
For \(0<\varepsilon<1\) this is still UCP and its unit-rate Poisson generator still has a positive centered gap \(2(1-\varepsilon)/3\), but it is not entanglement-breaking. Exact isotropy is load-bearing for the critical classical factorization; a nonzero transfer gap alone does not force it.

## A classical distribution is not an obtained fact

The readout in (CR2) retains the entire Bloch vector:
\[
r=3\int n\,(\mathsf M\rho)(n)\,dn.
\tag{CR11}
\]
Likewise \(r=3\sum_nnp_n\) in (CR4). The map from a density matrix to its full distribution is injective. It does not discard the input merely by representing it in a commutative language.

Preparation is not its inverse: it returns \(r/3\), not \(r\). Although \(\Phi_{1/3}\) is invertible as a linear map, its inverse is not positive on all output states. For example, it sends \((I+\sigma_3)/2\ge0\) to \((I+3\sigma_3)/2\), which has a negative eigenvalue. Thus physical reversal by a positive channel on arbitrary states is unavailable. Linear recoverability, entanglement breaking, and an admissible positive inverse are different predicates.

An outcome \(n\) obtained in one run is also different from the distribution over all outcomes. Neither (CR3) nor the factorization explains why one result obtains, constructs a persistent historical record, or proves deterministic or stochastic ontology. The Born weights in (CR2) belong to a declared measurement realization; this theorem does not derive the Born rule from the Albert algebra.

This supplies a controlled way to compare the user's measurement clue with the mass-gap inquiry: one context-derived operator has a spectral contraction and a classical factorization, but the theorems concern different properties of that operator. Neither property is by itself a relativistic mass Casimir or an explanation of actualization.

## Finite process thresholds, without a physical time claim

For the normalized processes in the Peirce construction,
\[
T_s^{\rm P}=P_\tau+e^{-2s/3}(I-P_\tau),\qquad
T_s^{\log}=P_\tau+3^{-s}(I-P_\tau),
\]
equation (CR8) gives
\[
T_s^{\rm P}\text{ entanglement-breaking}
\Longleftrightarrow s\ge\frac32\log3,
\qquad
T_s^{\log}\text{ entanglement-breaking}
\Longleftrightarrow s\ge1.
\tag{CR12}
\]
Every finite-time map remains linearly injective. Crossing this threshold changes the channel's ability to preserve entanglement with an ancilla, not the rank of its linear map. Its centered Hilbert generator is already gapped before the threshold is crossed; the two notions of gap do not coincide.

The process parameter, context averaging and clock interpolation are specified inputs. Equation (CR12) is not a cosmological epoch, a causal-grain duration, or the time at which mass switches on.

[[directed-analytic-realization/context_transport_receipt.py|The shared receipt]]
checks the finite six-direction moments, preparation return and threshold arithmetic separately from the continuum sphere proof.
[[directed-analytic-realization/context-transport-receipt-output.txt|Its output]]
also retains the distinction between these matrix-state calculations and the transport-section spectral tests.
