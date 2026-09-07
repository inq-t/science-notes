# Expected Inclusions and Mirror-Clock Consistency

A faithful bipartite state makes the observable inclusion into the whole a Hilbert isometry. Mirror commutators intertwine through this map and their positive forms pull back exactly, even for correlated states. Their adjoints and clocks need not intertwine. For an included frame with scalar commutant, an autonomous reducing mirror-clock return is equivalent to a product state; a correlated two-qubit example instead has leakage and a visible zero-frequency atom. This classifies one specific autonomous return, not the legitimacy of correlated local observations or memory-bearing dynamics.

## The inclusion has a canonical state-dependent isometry

Let \(N=M_{d_A}(\mathbb C)\), \(M=M_{d_A d_B}(\mathbb C)\), and
\[
\iota(A)=A\otimes I_B,\qquad
\rho=\rho_{AB}>0,\qquad \operatorname{Tr}\rho=1,\qquad
\rho_A=\operatorname{Tr}_B\rho.
\]
The standard carriers are Hilbert–Schmidt spaces
\(\mathcal H_N=\operatorname{HS}_{d_A}\),
\(\mathcal H_M=\operatorname{HS}_{d_A d_B}\), with cyclic vectors
\(\Omega_N=\sqrt{\rho_A}\), \(\Omega_M=\sqrt\rho\). Define
\[
\boxed{
V(X\sqrt{\rho_A})=(X\otimes I_B)\sqrt\rho,\qquad
V(T)=(T\rho_A^{-1/2}\otimes I_B)\sqrt\rho.
}
\tag{EI1}
\]
Every \(T\) has the displayed form because \(\rho_A>0\). Moreover
\[
\|V(X\sqrt{\rho_A})\|_{\mathrm{HS}}^2
=\operatorname{Tr}\rho_A X^*X
=\|X\sqrt{\rho_A}\|_{\mathrm{HS}}^2.
\]
Thus \(V\) is an isometry without any product-state assumption. Direct Hilbert–Schmidt pairing fixes its adjoint:
\[
\boxed{V^*(S)=\operatorname{Tr}_B(S\sqrt\rho)\rho_A^{-1/2}.}
\tag{EI2}
\]
The order of the factors matters. This is always a GNS inclusion isometry; it is not automatically an intertwiner of the standard-form conjugations or natural cones for a correlated state.

Use the [[modular-mirror-response-and-the-analytic-domain|finite modular mirror]]
\[
D_A^\theta(T)=AT-T\theta^{-1/2}A\theta^{1/2},
\qquad \theta>0.
\tag{EI3}
\]
It satisfies \(D_A^\theta(X\sqrt\theta)=[A,X]\sqrt\theta\). Therefore
\[
\boxed{D_{\iota(A)}^\rho V=V D_A^{\rho_A}}
\tag{EI4}
\]
for every \(A\in N\), irrespective of correlations.

## The same frame has exact form compression, not automatic clock restriction

Choose a finite frame \(A_1,\ldots,A_r\in N\), with any fixed positive weights absorbed into its members. Define
\[
K_N=\frac12\sum_a(D_{A_a}^{\rho_A})^*D_{A_a}^{\rho_A},
\qquad
K_M=\frac12\sum_a(D_{\iota(A_a)}^\rho)^*D_{\iota(A_a)}^\rho.
\tag{EI5}
\]
The whole operator here uses precisely the **included \(N\)-frame**. It is not an independently chosen complete frame of \(M\). Additional whole rows would contribute additional pullback terms.

Equation (EI4) and the isometry give
\[
\boxed{V^*K_MV=K_N.}
\tag{EI6}
\]
These are positive Hilbert forms on the stated carriers. The bounded mirror-row construction realizes a UCP process on \(B(\mathcal H_M)\); it does not automatically give a completely Dirichlet process on the original left-represented \(M\).

Put \(P=VV^*\). An actual reducing return requires the stronger condition
\[
\boxed{K_MV=VK_N.}
\tag{EI7}
\]
Since \(K_M\) is self-adjoint, this is equivalent to \(\operatorname{ran}V\) reducing \(K_M\), and to both
\[
e^{-sK_M}V=Ve^{-sK_N},\qquad
e^{-itK_M}V=Ve^{-itK_N}
\]
for all \(s\ge0\), \(t\in\mathbb R\). Form compression fixes the first moment; it does not imply these identities. The general distinction between pullback and reduction is owned by [[trace-dirichlet-descent/standard-form-pullback-and-reducing-wall|the reducing-wall theorem]], while [[coarse-response-memory/inq|coarse response memory]] owns the resulting nonautonomous compressed evolution.

## Product states are exactly the expected tensor-factor inclusions

A conditional expectation onto \(N\otimes I_B\) must, by bimodularity, have the form
\[
E(X\otimes Y)=X\,\phi_B(Y)\otimes I_B
\tag{EI8}
\]
for a state \(\phi_B\): \(E(I\otimes Y)\) commutes with every element of \(N\), hence is scalar there. It preserves the faithful state \(\rho\) exactly when
\[
\operatorname{Tr}\rho(X\otimes Y)
=\operatorname{Tr}\rho_A X\,\phi_B(Y)
\]
for all \(X,Y\), which is equivalent to
\[
\boxed{\rho=\rho_A\otimes\rho_B,\qquad
\phi_B(Y)=\operatorname{Tr}\rho_B Y.}
\tag{EI9}
\]
Faithfulness of \(\rho\) makes both marginals faithful.

The linked expected-inclusion theorem also identifies this with modular invariance of the tensor factor. In finite matrices, invariance of
\(\rho^{it}(N\otimes I)\rho^{-it}\) makes the restricted derivation
\([\log\rho,\,\cdot\,]\) inner on \(N\). Subtracting its \(N\)-implementer leaves an operator commuting with \(N\), so
\(\log\rho=H_A\otimes I+I\otimes H_B\), up to a scalar. Exponentiation gives the product form. This is the finite tensor-factor specialization, not a replacement for the general standard-form theorem.

Ordinary partial trace of a density matrix always gives \(\rho_A\); it does **not** prove that a \(\rho\)-preserving conditional expectation exists. The coefficient map obtained from (EI2) is instead
\[
V^*(X\sqrt\rho)
=E_{\mathrm{GNS}}(X)\sqrt{\rho_A},\qquad
E_{\mathrm{GNS}}(X)=\operatorname{Tr}_B(X\rho)\rho_A^{-1}.
\tag{EI10}
\]
For correlated states this linear projection need not even preserve adjoints. It cannot silently be substituted for (EI8).

## The mirror-adjoint and irreducible-frame criteria are sharp

On vectors \(X\sqrt\theta\), the Hilbert adjoint of the mirror derivative is
\[
(D_A^\theta)^*(X\sqrt\theta)
=\bigl(A^*X-X\theta A^*\theta^{-1}\bigr)\sqrt\theta.
\tag{EI11}
\]
Consequently adjoint intertwining for every \(A\in N\) is equivalent to
\[
\rho(A\otimes I)\rho^{-1}
=(\rho_AA\rho_A^{-1})\otimes I.
\tag{EI12}
\]
Necessity follows by applying the adjoint identity to \(\Omega_N\), then replacing \(A^*\) by \(A\); sufficiency follows from (EI11) for every \(X\). Equation (EI12) says
\((\rho_A^{-1}\otimes I)\rho\) commutes with \(N\otimes I\), and therefore gives precisely (EI9). Thus all mirror adjoints intertwine if and only if the state is product.

There is a stronger statement for a fixed frame. Assume
\[
\{A_1,\ldots,A_r\}'=\mathbb C I
\quad\text{inside }N.
\tag{EI13}
\]
Then
\[
\ker K_N=\mathbb C\sqrt{\rho_A},\qquad
\ker K_M=(I_A\otimes M_{d_B})\sqrt\rho.
\tag{EI14}
\]
Indeed the kernel of a sum of derivative squares is the common commutator kernel; expand any whole coefficient matrix in a basis of the \(B\)-factor.

If (EI7) holds, the whole kernel projection preserves \(\operatorname{ran}V\), whose intersection with that kernel is only \(\mathbb C\Omega_M\). Hence every centered local vector
\((X\otimes I)\sqrt\rho\), with \(\operatorname{Tr}\rho_A X=0\), is orthogonal to every \((I\otimes Y)\sqrt\rho\). This says
\[
\operatorname{Tr}\rho(X^*\otimes Y)=0
\]
for every such \(X\) and every \(Y\). Subtracting the mean from arbitrary \(X\) proves factorization of all tensor correlations, hence (EI9).

Conversely, for a product state the natural Hilbert–Schmidt tensor identification gives
\[
V(T)=T\otimes\sqrt{\rho_B},\qquad
D_{\iota(A)}^\rho=D_A^{\rho_A}\otimes I_{\mathcal H_B},
\qquad K_M=K_N\otimes I_{\mathcal H_B}.
\tag{EI15}
\]
Thus (EI7) holds. Under (EI13), product state is therefore necessary and sufficient for this specified autonomous reducing mirror-row return. Without the irreducibility assumption, an incomplete frame can reduce accidentally; the zero row is an immediate counterexample to unrestricted necessity.

Even (EI15) is an intertwining of Hilbert clocks. It does not assert that the positive clock normalizes the original left-represented factor \(N\). The algebra acted upon by the joined-carrier clock remains a separate part of the realization.

## A correlated faithful example has a positive local form and a leaking clock

Take two qubits in the ordered basis \(00,01,10,11\):
\[
\rho=\frac1{20}\operatorname{diag}(9,1,1,9),\qquad
\rho_A=\rho_B=I/2,\qquad
A_1=E_{01},\quad A_2=E_{10}.
\tag{EI16}
\]
This frame satisfies (EI13). Set
\[
e_0=|00\rangle\langle10|,\qquad
e_1=|01\rangle\langle11|,\qquad
v=V(E_{01})=\frac{e_0+3e_1}{\sqrt{10}}.
\]
These Hilbert–Schmidt matrix units are orthonormal. Direct evaluation of (EI3)–(EI5) gives
\[
K_NE_{01}=E_{01},\qquad
K_Me_0=5e_0,\qquad K_Me_1=\frac59e_1.
\]
Thus (EI6) holds on this coherence, but
\[
\boxed{
K_Mv-VK_NE_{01}
=\frac{4e_0-\frac43e_1}{\sqrt{10}}
\perp\operatorname{ran}V,\qquad
\left\|K_Mv-VK_NE_{01}\right\|^2=\frac{16}{9}.
}
\tag{EI17}
\]
Its first spectral moment is one, while its second is \(25/9\), not one. The actual retained coherence has
\[
\boxed{
V^*e^{-tK_M}V(E_{01})
=\left(\frac1{10}e^{-5t}+\frac9{10}e^{-5t/9}\right)E_{01},
}
\tag{EI18}
\]
not \(e^{-t}E_{01}\). This is an exact readout with two spectral frequencies, not an invalid observation.

The adjoint-map distinction is visible without exponentiation. For
\(X=|00\rangle\langle10|\), (EI10) gives
\[
E_{\mathrm{GNS}}(X)=\frac1{10}E_{01},\qquad
E_{\mathrm{GNS}}(X^*)=\frac9{10}E_{10}.
\]
So \(E_{\mathrm{GNS}}(X^*)\ne E_{\mathrm{GNS}}(X)^*\).

## A local centered distinction can retain a whole zero-frequency atom

Let \(Z=\operatorname{diag}(1,-1)\) and
\[
z_A=(Z\otimes I)\sqrt\rho,\qquad
z_B=(I\otimes Z)\sqrt\rho.
\]
Both have norm one and are orthogonal to \(\Omega_M\). Their inner product is \(4/5\). The whole kernel in (EI14) has orthonormal Pauli coordinates from the \(B\)-factor, and the other centered coordinates pair to zero with \(z_A\). Therefore
\[
\boxed{P_{\ker K_M}z_A=\frac45z_B.}
\tag{EI19}
\]
The zero-frequency weight is \(16/25\). The remaining vector
\(z_A-\frac45z_B\) has squared norm \(9/25\) and eigenvalue \(50/9\): in either fixed-\(B\) diagonal block, the two mirror rows have eigenvalues zero and
\(\frac12(2+9+1/9)=50/9\). Consequently
\[
\boxed{
V^*e^{-tK_M}V(Z/\sqrt2)
=\left(\frac{16}{25}+\frac9{25}e^{-50t/9}\right)Z/\sqrt2,
}
\tag{EI20}
\]
although \(K_N(Z/\sqrt2)=2Z/\sqrt2\). The first moment still agrees:
\((9/25)(50/9)=2\). Centering against \(\Omega_M\) alone did not remove the entire ground sector of this whole operator.

The cause is explicit: the whole row contains only the included \(N\)-frame and leaves its \(B\)-commutant as a kernel. This is not a claim that correlated nature, a complete global mirror frame, or Yang–Mills theory is gapless.

The useful return requirement is consequently precise. Product-state expectedness characterizes autonomous reduction for this irreducible tensor-factor mirror row. It is not necessary for local observations, spatial covariance, or a physical QFT; a correlated subsystem may correctly retain a frequency-dependent response and memory. [[coarse-response-memory/spectral-readout-and-the-visible-gap|The spectral-readout construction]] keeps that whole response while allowing nonautonomous local clocks. The full problem is to select and control the actual row, state, observable family and spectral readout through the required physical limits, not to replace every correlated inclusion by an autonomous product model.

[[directed-analytic-realization/mirror_inclusion_receipt.py|The exact mirror-inclusion receipt]] checks the inclusion adjoint, row and form intertwiners, the correlated spectral atoms and the product-state control. [[directed-analytic-realization/mirror-inclusion-receipt-output.txt|Its output]] records finite rational identities; the necessity and sufficiency arguments above are not inferred from sampled states.
