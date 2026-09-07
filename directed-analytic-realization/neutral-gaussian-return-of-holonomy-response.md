# Neutral Gaussian Return of Holonomy Response

A gapped connection response can be realized as a Gaussian field with a unique vacuum and a neutral observable sector whose excitation threshold is twice the one-particle edge. This return preserves the Pauli transport bound that disappears in the adjoint diffusion construction: neutral pair amplitudes carry summed positive energies, not a commutator or a new conjugation Laplacian. The construction is an explicit continuous-time lattice theory in a fixed background. Its interaction, Gauss-law and relativistic continuum obligations remain open.

## Keep the response while changing its realization

Use the finite even Pauli torus or the infinite lattice from
[[algebra/short-loop-holonomy-and-quantitative-gluing|short-loop quantitative gluing]],
with complex section carrier
\[
\mathfrak h=\ell^2(V;\mathbb C^2),\qquad
L_T=D_T^*D_T,\qquad A=L_T^{1/2}.
\tag{NG1}
\]
For \(d=2,3\), the exact lower edges are
\[
\gamma_*=2d-2\sqrt d,\qquad
m_*=\inf\sigma(A)=\sqrt{\gamma_*}>0.
\tag{NG2}
\]
The same formulas hold on the infinite lattice as spectral infima. They are fixed-edge-normalization quantities, not physical masses.

Regard \(\mathfrak h\) as a real Hilbert space \(\mathfrak h_{\mathbb R}\), with inner product \(\operatorname{Re}\langle\cdot,\cdot\rangle\). Realification gives positive real operators \(L_{\mathbb R}\) and \(A_{\mathbb R}\). The original fiber multiplication by \(i\) commutes with both and defines a global phase symmetry.

The [[algebra/cauchy-response-and-local-action|opposed-response construction]]
and its stated clock prescription give
\[
\ddot q+L_{\mathbb R}q=0,\qquad
S[q]=\frac12\int
\left(\|\dot q\|^2-\|D_Tq\|^2\right)dt.
\tag{NG3}
\]
This is a local graph action: the second term compares nearest-neighbor transported values. The nonlocal square root \(A\) supplies the boundary response and positive frequency, while its local square supplies the field equation. No separate on-site mass potential has been inserted.

The graph, background transports, real pairing and response-to-clock prescription are still inputs. The two-component fiber is an internal field multiplet here, not a demonstrated spacetime spin representation.

## The Gaussian vacuum uses this same response

Choose the bosonic CCR realization with quantization convention one. On a finite graph, let \(n_{\mathbb R}=\dim_{\mathbb R}\mathfrak h_{\mathbb R}\). The existing
[[algebra/response-factorization-and-the-vacuum|quadratic response factorization, RV10]]
gives
\[
\widehat H
=-\frac12\Delta_q+\frac12(q,L_{\mathbb R}q)
-\frac12\operatorname{Tr}_{\mathbb R}A_{\mathbb R},
\]
\[
\psi_0(q)
=\det(A_{\mathbb R}/\pi)^{1/4}
\exp\!\left[-\frac12(q,A_{\mathbb R}q)\right].
\tag{NG4}
\]
The determinant is on the \(n_{\mathbb R}\)-dimensional real space. Direct Gaussian integration normalizes \(\psi_0\); oscillator factorization proves its uniqueness and zero energy. Its coordinate covariance is \((2A_{\mathbb R})^{-1}\).

The final scalar in \(\widehat H\) subtracts the vacuum energy only. It does not change the quadratic stiffness \(L_{\mathbb R}\) or any excitation difference. Subtracting a multiple of \(I\) from \(L_T\) instead would change the field potential by a multiple of \(\|q\|^2\); it is not this vacuum-energy convention.

The Euclidean covariance is
\[
K(\tau)=\frac{e^{-|\tau|A_{\mathbb R}}}{2A_{\mathbb R}}.
\tag{NG5}
\]
[[algebra/wick-real-forms-and-positive-preparation|Positive preparation]]
proves its reflected quadratic form is a squared norm of the half-history preparation map. The declared Gaussian realization inherits that positive preparation and the clock with frequencies \(A_{\mathbb R}\). This reuses the same response, rather than specifying an unrelated state and Hamiltonian.

On \(\mathbb Z^d\), an infinite determinant or an ordinary Lebesgue density on \(\ell^2\) is not available. Instead use the
[[local-weyl-realization|Weyl/Fock construction]] from the opposed Cauchy norm. Since \(A\) is bounded above and below, finite-support Cauchy data have finite covariance and dense one-particle image. The quasifree state and its Fock representation exist directly. No trace-class covariance on all of \(\ell^2\) is claimed.

## Global neutrality retains a positive excitation edge

Complexifying the real one-particle space splits its two phase charges:
\[
\mathfrak h_{\mathbb R}\otimes_{\mathbb R}\mathbb C
\simeq\mathfrak h\oplus\overline{\mathfrak h}.
\]
The Fock carrier, positive energy and phase charge are
\[
\mathcal F=\mathcal F_s(\mathfrak h\oplus\overline{\mathfrak h}),\qquad
H=d\Gamma(A\oplus\overline A),\qquad
Q=N_+-N_-.
\tag{NG6}
\]
The degree-zero vector \(\Omega\) is the unique vacuum. On every occupation sector, \(H\ge m_*(N_++N_-)\). A nonvacuum vector with \(Q=0\) has at least one quantum of each charge. The
[[algebra/positive-energy-pairs-and-the-neutral-gap|neutral-pair theorem]]
therefore gives
\[
\boxed{\ker H=\mathbb C\Omega,\qquad
\inf\sigma\!\left(H|_{\ker Q\ominus\mathbb C\Omega}\right)=2m_*.}
\tag{NG7}
\]
Conjugate low-energy spectral packets prove sharpness, including when \(m_*\) is not an eigenvalue. This threshold is uniform in lattice volume.

Here neutrality is under a **global \(U(1)\)**. It is not a local nonabelian Gauss-law condition, a proof of confinement, or an identification of these pairs with glueballs. The background connection remains fixed, not quantized.

## The neutral sector is the vacuum carrier of actual observables

For a finite vertex set \(O\), let \(\mathcal A(O)\) be the von Neumann algebra generated by the Weyl operators of real Cauchy data supported in \(O\). The local Green pairing makes \(\mathcal A(O_1)\) and \(\mathcal A(O_2)\) commute at equal time when \(O_1\cap O_2=\varnothing\).

The global phase action
\[
\alpha_\theta(B)=e^{i\theta Q}Be^{-i\theta Q}
\]
preserves these supports, commutes with \(H\), and fixes \(\Omega\). Define the invariant local algebra \(\mathcal A_0(O)=\mathcal A(O)^{U(1)}\). For every bounded \(B\in\mathcal A(O)\), compact averaging gives
\[
E_0(B)=\frac1{2\pi}\int_0^{2\pi}\alpha_\theta(B)\,d\theta
\in\mathcal A_0(O),
\qquad
E_0(B)\Omega=P_{\ker Q}B\Omega.
\tag{NG8}
\]
The integral can be taken ultraweakly. Finite-support Weyl coherent vectors are total in the original Fock space. Projecting their dense span by \(P_{\ker Q}\) proves
\[
\boxed{\overline{\operatorname{span}
\{B\Omega:B\in\mathcal A_0(O),\ O\text{ finite}\}}
=\ker Q.}
\tag{NG9}
\]
Thus (NG7) belongs to the vacuum representation of a specified neutral observable family; it is not merely a Hilbert subspace selected because it has a convenient gap. This is global cyclicity of the union, not a claim of relativistic local cyclicity.

The gauge-frame covariance of \(D_T\) relates different background presentations. It must not be substituted for the global-charge invariance used in (NG8), or for a dynamical gauge theory's physical-state constraint.

## A local quadratic observable carries the energy sum

Use the standard complex charged field associated with this realification, normalized as \(\varphi=(q_x+iq_y)/\sqrt2\) for the two real coordinates in (NG3)–(NG4). For a vertex-fiber basis vector \(e_i\), put
\[
f_i=(2A)^{-1/2}e_i,\qquad
\varphi_i=a(f_i)+b^\dagger(\overline{f_i}),
\tag{NG10}
\]
where \(a\) and \(b\) act on the two charge species, annihilation is antilinear in its vector argument, and creation is linear. Thus \(\varphi_i\) has charge \(-1\) under \(Q\). It is the local coordinate combination \((q(e_i)+iq(ie_i))/\sqrt2\); the nonlocal one-particle smear \(A^{-1/2}e_i\) does not change this equal-time localization. On the finite-particle core define the neutral local Wick square
\[
B_v=\sum_{i\text{ at }v}:\varphi_i^\dagger\varphi_i:.
\]
It has zero vacuum expectation and creates a genuine neutral pair:
\[
B_v\Omega
=\sum_{i\text{ at }v}
a^\dagger(f_i)b^\dagger(\overline{f_i})\Omega.
\tag{NG11}
\]
A number-density operator \(a^\dagger a\) alone would instead annihilate the vacuum. These are different observables.

Under \(\mathfrak h\otimes\overline{\mathfrak h}\simeq\operatorname{HS}(\mathfrak h)\), the vector in (NG11) corresponds to the finite-rank operator
\[
K_v=(2A)^{-1/2}P_v(2A)^{-1/2},
\tag{NG12}
\]
where \(P_v\) projects onto the two vertex components. The pair generator acts by
\[
H_+K=AK+KA.
\tag{NG13}
\]
Consequently its connected Euclidean two-point function is
\[
\langle B_v\Omega,e^{-tH}B_w\Omega\rangle
=\langle K_v,e^{-tH_+}K_w\rangle_{\rm HS},
\]
\[
\left|\langle B_v\Omega,e^{-tH}B_w\Omega\rangle\right|
\le e^{-2m_*t}\|K_v\|_{\rm HS}\|K_w\|_{\rm HS},
\qquad t\ge0.
\tag{NG14}
\]
All expressions are finite for a vertex on the infinite lattice because \(A^{-1/2}\) is bounded and \(P_v\) has finite rank. On a finite Pauli torus the lowest one-particle eigenspace has nonzero vertex evaluation, so \(P_{\min}K_vP_{\min}\ne0\); this Wick square has nonzero overlap with the exact pair edge.

There is no contradiction with the flat adjoint process. Conjugation of a matrix observable by \(e^{-itA}\) has generator \(K\mapsto AK-KA\). The separate transported adjoint graph Laplacian is yet another operator. Neither equals (NG13). The matrix \(K\) in (NG12) represents a pair amplitude, not a one-particle density matrix or a pointwise adjoint field.

## Local graph dynamics is not relativistic microcausality

Nearest-neighbor \(L_T\) does not imply exact finite-speed propagation in continuous lattice time. The Cauchy propagator contains
\[
\frac{\sin(t\sqrt{L_{\mathbb R}})}{\sqrt{L_{\mathbb R}}}
=\sum_{n=0}^\infty
\frac{(-1)^nt^{2n+1}L_{\mathbb R}^{\,n}}{(2n+1)!}.
\tag{NG15}
\]
If two vertices have graph distance \(r\), matrix entries vanish for \(n<r\), giving the bound
\[
\left\|P_v\frac{\sin(t\sqrt{L_{\mathbb R}})}
{\sqrt{L_{\mathbb R}}}P_w\right\|
\le\sum_{n\ge r}
\frac{|t|^{2n+1}\|L_{\mathbb R}\|^n}{(2n+1)!}.
\tag{NG16}
\]
This is a small-tail estimate, not exact vanishing outside a cone. On the infinite lattice, vertices separated by \(r\) steps along one axis have a unique shortest path; its nonzero Pauli product gives a nonzero leading \(t^{2r+1}\) coefficient. Arbitrarily distant commutators therefore have nonzero analytic tails.

The continuum wave-locality theorem in the Cauchy note used a differential Laplacian and cannot be copied to this graph. Moreover,
[[algebra/pauli-transport-and-the-continuum-scaling-obstruction|the scaling obstruction]]
shows that positive Pauli edge reweighting cannot preserve finite nonzero propagation in two or more continuum directions while keeping this gap finite. A vacuum-energy subtraction in (NG4) does not repair that response-level problem.

The construction therefore closes a specific missing return: a geometric section bound can survive as a neutral vacuum-excitation bound and as decay of actual Gaussian observables. It does not solve the interacting, local, Lorentz-covariant continuum problem. The next improvement must alter or derive the transport realization and its scale law, not relabel adjoint diffusion or a fixed lattice as Yang–Mills theory.

[[algebra/refining-holonomy-and-a-finite-continuum-threshold|The identity-approaching refinement]]
now alters that law and proves local-smear covariance convergence with a
finite positive edge. It restores exact continuum finite-speed propagation,
but its neutral pairs still fail the forward-cone translation test, and
the background is not source-free. This is a distinct diagnostic, not a
promotion of (NG7) to a physical mass theorem.

[[neutral_transport_receipt.py|The neutral-transport receipt]] checks finite occupation sectors, pair sums and differences, Pauli thresholds and the continuum-scaling arithmetic. [[neutral-transport-receipt-output.txt|Its output]] does not replace the Fock-domain, observable-cyclicity or infinite-lattice proofs.
