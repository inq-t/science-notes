# Positive-Energy Pairs and the Neutral Gap

Opposite charges cancel without cancelling their positive excitation energies. A one-particle operator with lower edge \(m_0>0\) induces a doubled bosonic Fock theory whose unique vacuum is separated from its charge-zero excitations by exactly \(2m_0\). The pair carrier is a tensor product with an energy sum, not the adjoint carrier with an energy difference. This gives an explicit bound-preserving realization of a neutral sector, conditional on the chosen free bosonic construction; it does not construct interactions, a gauge constraint or a relativistic mass invariant.

## The pair operator and its domain

Let \(\mathfrak h\ne\{0\}\) be a complex Hilbert space and let \(A\) be a self-adjoint operator with
\[
A\ge mI,\qquad m>0,\qquad m_0:=\inf\sigma(A)\ge m.
\tag{PN1}
\]
The lower bound \(m\) may be a certificate rather than the sharp edge \(m_0\). No discreteness or eigenvector at the spectral edge is assumed.

Write \(\overline{\mathfrak h}\) for the conjugate Hilbert space and
\(\overline A\,\overline f=\overline{Af}\). On
\[
\mathcal H_{\mathrm{pair}}=\mathfrak h\otimes\overline{\mathfrak h},
\]
the two nonnegative operators \(A\otimes I\) and \(I\otimes\overline A\) strongly commute. Their joint spectral calculus defines
\[
\boxed{H_+=A\otimes I+I\otimes\overline A.}
\tag{PN2}
\]
Its closed energy form is
\[
\begin{aligned}
q_+[\psi]
&=\|(A^{1/2}\otimes I)\psi\|^2
+\|(I\otimes\overline A^{1/2})\psi\|^2,\\
\operatorname{Dom}q_+
&=\operatorname{Dom}(A^{1/2}\otimes I)
\cap\operatorname{Dom}(I\otimes\overline A^{1/2}).
\end{aligned}
\tag{PN3}
\]
The operator domain is
\(\operatorname{Dom}(A\otimes I)\cap\operatorname{Dom}(I\otimes\overline A)\): for nonnegative spectral values, integrability of \((a+b)^2\) is equivalent to integrability of both \(a^2\) and \(b^2\). In particular,
\[
q_+[\psi]\ge2m_0\|\psi\|^2\ge2m\|\psi\|^2.
\tag{PN4}
\]
These are form inequalities, so unbounded \(A\) causes no implicit all-vector domain assumption.

## A Hilbert–Schmidt presentation does not turn a pair into a density matrix

Use the unitary identification
\[
\mathcal J:\mathfrak h\otimes\overline{\mathfrak h}
\longrightarrow\operatorname{HS}(\mathfrak h),\qquad
f\otimes\overline g\longmapsto |f\rangle\langle g|.
\tag{PN5}
\]
Here \(|f\rangle\langle g|\) sends \(z\) to \(f\langle g,z\rangle\); the inner product is linear in its second argument. The target is a Hilbert space of amplitudes. A general \(T\in\operatorname{HS}(\mathfrak h)\) need not be positive, self-adjoint or trace-normalized. It is not being designated a density matrix.

On finite-rank operators with vectors in \(\operatorname{Dom}A\), (PN2) becomes
\[
\boxed{\mathcal JH_+\mathcal J^{-1}T=AT+TA.}
\tag{PN6}
\]
The closed form is
\[
q_+[T]=\|A^{1/2}T\|_{\mathrm{HS}}^2+
\|TA^{1/2}\|_{\mathrm{HS}}^2.
\tag{PN7}
\]
For an unbounded factor, the right product is initially defined on its natural dense domain and must have a Hilbert–Schmidt extension. Equivalently, (PN7) is the closure of the finite-rank form through (PN5). The corresponding evolutions are
\[
e^{-sH_+}T=e^{-sA}Te^{-sA},\qquad s\ge0,
\]
\[
e^{-itH_+}T=e^{-itA}Te^{-itA},\qquad t\in\mathbb R.
\tag{PN8}
\]
The second formula has the same clock sign on both sides. It is unitary on the Hilbert–Schmidt carrier, but is not an observable-algebra automorphism or a density-matrix conjugation.

For comparison, the joint spectral difference
\[
H_-=A\otimes I-I\otimes\overline A
\tag{PN9}
\]
acts on the common finite-rank core as \(AT-TA\), and its unitary group acts as
\[
e^{-itH_-}T=e^{-itA}Te^{itA}.
\]
This is the commutator generator for conjugation of one-particle operators. Its spectral values are differences, not positive pair energies. An eigenvector \(Af=af\) makes \(|f\rangle\langle f|\) a zero vector of that generator. Even without eigenvectors, normalized spectral packets in an interval of width \(\varepsilon\) give pair amplitudes on which the norm of \(H_-\) is at most \(\varepsilon\). Positive one-particle energy therefore does not exclude arbitrarily slow conjugation.

The [[short-loop-holonomy-and-quantitative-gluing|adjoint connection Laplacian]] is a third operator: it compares matrix fields at adjacent vertices by conjugating their fibers. It is neither (PN2) nor automatically the square of (PN9). A cancellation of central holonomy in that transport representation is not a cancellation of the sum in (PN2).

## The free charged Fock realization

Choose the bosonic CCR realization on
\[
\mathcal F=\mathcal F_s(\mathfrak h\oplus\overline{\mathfrak h})
\cong
\bigoplus_{r,s\ge0}
\operatorname{Sym}^r\mathfrak h\otimes
\operatorname{Sym}^s\overline{\mathfrak h}.
\tag{PN10}
\]
The first and second summands carry opposite unit charges. This choice of species, statistics and charge is explicit. The [[directed-analytic-realization/local-weyl-realization|coherent-vector Weyl construction]] supplies the Gaussian vacuum representation; it is not inferred from the lower bound alone.

Let \(\Omega\) be the degree-zero unit vector and define
\[
H=d\Gamma(A\oplus\overline A),\qquad
N=N_++N_-,\qquad Q=N_+-N_-.
\tag{PN11}
\]
On the \((r,s)\) sector,
\[
H_{r,s}
=\sum_{j=1}^{r}A_j+\sum_{k=1}^{s}\overline A_k,\qquad
N=r+s,\qquad Q=r-s.
\tag{PN12}
\]
The sums are defined by their nonnegative joint spectral calculus on the symmetric tensor sectors. The Fock operator is their self-adjoint direct sum:
\[
\operatorname{Dom}H
=\left\{\Psi:
\Psi_{r,s}\in\operatorname{Dom}H_{r,s},\quad
\sum_{r,s}\|H_{r,s}\Psi_{r,s}\|^2<\infty\right\}.
\]
Its form domain is
\[
\operatorname{Dom}H^{1/2}
=\left\{\Psi:
\Psi_{r,s}\in\operatorname{Dom}H_{r,s}^{1/2},\quad
\sum_{r,s}q_{r,s}[\Psi_{r,s}]<\infty\right\}.
\]
Thus
\[
\boxed{H\ge m_0N\ge mN,\qquad
\ker H=\mathbb C\Omega.}
\tag{PN13}
\]
The first inequality holds as an energy-form inequality. Each nonzero particle sector has positive energy, while \(H\Omega=0\), proving uniqueness of the vacuum. Normal ordering of this free Hamiltonian fixes the vacuum energy to zero; it does not remove the excitation sums in (PN12).

The number, charge and energy operators strongly commute. In particular \(e^{i\theta Q}\) implements a global \(U(1)\) symmetry commuting with the clock. Its invariant Hilbert sector is
\[
\mathcal F_0:=\ker Q
=\mathbb C\Omega\ \oplus
\bigoplus_{k\ge1}
\operatorname{Sym}^k\mathfrak h\otimes
\operatorname{Sym}^k\overline{\mathfrak h}.
\tag{PN14}
\]
Charge zero means equal particle and antiparticle numbers. It does not mean zero particle number.

## The exact neutral edge

On \(\mathcal F_0\ominus\mathbb C\Omega\), one has \(N\ge2\). Consequently
\[
\boxed{
H|_{\mathcal F_0}
\ge2m_0(I-P_\Omega)\ge2m(I-P_\Omega).
}
\tag{PN15}
\]
The coefficient \(2m_0\) is sharp, including when \(m_0\) is not an eigenvalue.

To prove sharpness, for every \(\varepsilon>0\) choose a unit vector
\[
f_\varepsilon\in
\operatorname{Ran}\mathbf1_{[m_0,m_0+\varepsilon]}(A).
\]
That spectral subspace is nonzero by the definition of the spectral bottom. Its vectors have bounded spectral support and therefore belong to \(\operatorname{Dom}A\). The opposite-charge pair
\[
\Psi_\varepsilon
=a_+^*(f_\varepsilon)
a_-^*(\overline{f_\varepsilon})\Omega
\tag{PN16}
\]
has unit norm, charge zero and is orthogonal to \(\Omega\). Since the species are distinct, no identical-species factor of \(\sqrt2\) occurs. Its energy satisfies
\[
\langle\Psi_\varepsilon,H\Psi_\varepsilon\rangle
=2\langle f_\varepsilon,Af_\varepsilon\rangle
\le2(m_0+\varepsilon).
\]
Together with (PN15), this proves
\[
\boxed{
\inf\sigma\!\left(H|_{\mathcal F_0\ominus\mathbb C\Omega}\right)
=2\,\inf\sigma(A).
}
\tag{PN17}
\]
This is a spectral infimum, not an assertion of a neutral bound-state eigenvector at threshold.

The carrier map making the inheritance explicit is the isometry
\[
\mathcal I_{\mathrm{pair}}:
f\otimes\overline g\longmapsto
a_+^*(f)a_-^*(\overline g)\Omega.
\tag{PN18}
\]
Its range is precisely the \((1,1)\) sector, and
\[
H\mathcal I_{\mathrm{pair}}
=\mathcal I_{\mathrm{pair}}H_+
\]
on the operator domain and equivalently on the closed forms. Thus the neutral threshold is transported by a specified energy intertwiner, not by identifying all uses of the word “neutral.”

## Vacuum response and observable energy differences

A normally ordered neutral quadratic field polynomial may contain a pair-creation term, a pair-annihilation term and number-conserving terms. Only its pair-creation term acts nontrivially on \(\Omega\). If centered neutral operators \(B,C\) satisfy
\[
B\Omega=\mathcal I_{\mathrm{pair}}\psi_B,\qquad
C\Omega=\mathcal I_{\mathrm{pair}}\psi_C,
\]
then for \(s\ge0\) their vacuum Euclidean two-point function obeys
\[
\langle B\Omega,e^{-sH}C\Omega\rangle
=\langle\psi_B,e^{-sH_+}\psi_C\rangle,\qquad
\left|\langle B\Omega,e^{-sH}C\Omega\rangle\right|
\le e^{-2m_0s}\|\psi_B\|\,\|\psi_C\|.
\tag{PN19}
\]
This assumes the displayed vacuum vectors exist; local unbounded field products need an actual domain and, in a continuum, a renormalized definition.

In contrast, a normally ordered number-conserving operator \(a^*(f)a(g)\) annihilates the vacuum. Its transition frequencies between occupied states can involve differences of one-particle energies. Those differences do not create low-energy vacuum excitations. The Heisenberg commutator on the full observable algebra and the positive energy acting on vectors created from the vacuum therefore answer different questions, even in the same free theory.

## What a geometric section bound now supplies

Suppose the input is the bounded-degree connection Laplacian from
[[short-loop-holonomy-and-quantitative-gluing]], with
\[
L_T\ge\frac{\kappa}{B}I.
\]
Choose its positive response root \(A=\sqrt{L_T}\). The [[cauchy-response-and-local-action|opposed-response clock prescription]] relates that root to the wave operator whose spatial part is \(L_T\). Combining this prescribed clock realization with the Fock construction gives
\[
\boxed{
H|_{\mathcal F_0}
\ge2\sqrt{\kappa/B}\,(I-P_\Omega).
}
\tag{PN20}
\]
This bound survives graph-volume growth whenever the original coverage and congestion constants do. For the Pauli example with sharp section edge \(2d-2\sqrt d\), (PN17) gives the sharp free neutral edge
\(2\sqrt{2d-2\sqrt d}\) in the same declared lattice normalization.

This is a richer realization than an unadorned positive section operator: it has a vacuum, charged sectors, a neutral excitation space and an explicit energy-preserving pair map. It does not assert that every change of carrier preserves the gap. A coincident pair transported as one adjoint fiber follows different dynamics from two independently propagating charges; the coincident-position subspace need not be invariant under their energy sum.

The construction remains free and at a fixed connection. Global \(U(1)\) neutrality is not a nonabelian singlet condition or a local Gauss constraint. Further invariant subspaces retain the lower bound if their dynamics is the restriction of this same \(H\), but constructing an interacting constraint and its physical vacuum is a separate task. Interactions can change both the threshold and the vacuum; (PN15) cannot be transferred to them without a new comparison.

Finally, a graph clock edge is not a Poincaré mass Casimir. The graph, connection law, response-to-clock prescription, bosonic realization and dimensional normalization remain inputs. No continuum limit, relativistic propagation, dynamical gauge law or historical record is supplied by the tensor-energy theorem.

The [[directed-analytic-realization/neutral-gaussian-return-of-holonomy-response|lattice Gaussian realization]] constructs local charged fields, neutral Wick squares and the invariant observable family whose vacuum carrier is \(\mathcal F_0\). It also distinguishes the resulting graph-local action from exact relativistic propagation.

The [[directed-analytic-realization/neutral_transport_receipt.py|neutral-transport receipt]] and [[directed-analytic-realization/neutral-transport-receipt-output.txt|its output]] check finite occupation energies, pair sums and differences, and the Pauli normalization. The unbounded-domain and exact spectral-infimum statements above depend on their operator proofs, not a finite occupation cutoff.
