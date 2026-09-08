# Short-Loop Holonomy and Quantitative Gluing

Uniformly incompatible transports around short loops force a lower bound on the connection-gradient response, independent of the number of vertices. The proof constructs a bounded recovery map from edge discrepancies, rather than assuming a global inverse. Pauli transports give an explicit realization with no on-site mass term. Their passage to adjoint matrix observables then erases the central obstruction and restores diffusive modes. This is a constructive test of how a geometric gap can survive volume growth yet fail a change of carrier; no Yang–Mills realization is claimed.

## The response acts on sections, not on the connection

Let \(\Gamma=(V,E)\) be a finite graph or a locally finite graph of uniformly bounded degree. Give each vertex a finite-dimensional Hilbert space \(H_v\), with common dimension, and each oriented edge \(e:v\to w\) a unitary
\[
T_e:H_v\longrightarrow H_w,\qquad T_{\bar e}=T_e^*.
\]
Choose one orientation of each unoriented edge for counting. The section and edge carriers use counting measure and their given fiber norms. Define
\[
(D_Tx)_e=x_w-T_ex_v,\qquad
\mathcal E_T[x]=\sum_{e\in E}\|(D_Tx)_e\|^2,\qquad
L_T=D_T^*D_T.
\tag{HT1}
\]
Bounded degree makes \(D_T\) bounded on the Hilbert direct sums; on an infinite graph finitely supported sections are dense. The connection is an input to this operator. Its argument \(x\) is a section, not a function on the space of connections.

For a closed path \(\gamma=(v_0,\ldots,v_\ell=v_0)\), compose transport in path order:
\[
H_\gamma=T_{e_\ell}\cdots T_{e_1}:H_{v_0}\to H_{v_0}.
\tag{HT2}
\]
This is reversible holonomy. Neither ordering the factors nor finding \(H_\gamma\ne I\) constitutes irreversible historical loss.

## A local certificate gives a volume-independent bound

At each vertex \(v\), specify a finite family \(\mathcal C_v\) of rooted closed paths and nonnegative weights \(a_\gamma\). Define
\[
W_v=\sum_{\gamma\in\mathcal C_v}
a_\gamma(I-H_\gamma)^*(I-H_\gamma).
\tag{HT3}
\]
Assume the **fiber coverage** and **edge congestion** bounds
\[
W_v\ge\kappa I_{H_v}\quad\text{for every }v,\qquad \kappa>0,
\]
\[
B:=\sup_{e\in E}\sum_{v\in V}
\sum_{\gamma\in\mathcal C_v}
a_\gamma\,\ell(\gamma)\,m_e(\gamma)<\infty.
\tag{HT4}
\]
Here \(m_e(\gamma)\) counts all traversals of the unoriented edge, including repetitions. These constants are local transport and overlap data; they do not involve a chosen low eigenvector. Uniformly bounded loop length alone is insufficient without coverage and congestion.

Then
\[
\boxed{\mathcal E_T[x]\ge\frac{\kappa}{B}\|x\|^2.}
\tag{HT5}
\]

To prove it, propagate the edge discrepancies around a loop:
\[
(I-H_\gamma)x_v
=\sum_{j=1}^{\ell}
T_{e_\ell}\cdots T_{e_{j+1}}
\bigl(x_{v_j}-T_{e_j}x_{v_{j-1}}\bigr).
\tag{HT6}
\]
The empty product is the identity. A reversed edge has the same discrepancy norm as the chosen orientation. Cauchy–Schwarz and unitarity give
\[
\|(I-H_\gamma)x_v\|^2
\le\ell(\gamma)\sum_{e\in E}m_e(\gamma)\|(D_Tx)_e\|^2.
\]
Weighting and summing proves
\[
\kappa\sum_v\|x_v\|^2
\le\sum_v\langle x_v,W_vx_v\rangle
\le B\mathcal E_T[x].
\]
The bounded maps extend the proof from finite support to the full carrier.

The construction is frame-covariant. Changing fiber coordinates by unitaries \(G_v\) sends \(T_e\) to \(G_wT_eG_v^*\) and \(W_v\) to \(G_vW_vG_v^*\), preserving the constants. This covariance of section data must not be mistaken for a theorem on gauge-invariant functions of the connection.

## The gluing inverse is explicitly assembled

Let
\[
(Ax)_{v,\gamma}=\sqrt{a_\gamma}(I-H_\gamma)x_v.
\]
The transported sum in (HT6) defines an explicit edge-to-loop map \(K\). On arbitrary edge data, a reversed traversal uses \(-T_e^*y_e\); the same weighted Cauchy–Schwarz estimate gives \(\|Ky\|^2\le B\|y\|^2\), including on the infinite graph. Thus
\[
A=KD_T,\qquad \|K\|^2\le B,\qquad
A^*A=W=\bigoplus_vW_v\ge\kappa I.
\tag{HT7}
\]
Consequently
\[
\boxed{\mathcal R=W^{-1}A^*K,\qquad
\mathcal RD_T=I,\qquad
\|\mathcal R\|\le\sqrt{B/\kappa}.}
\tag{HT8}
\]
The bound uses \(\|W^{-1}A^*\|\le\kappa^{-1/2}\). Only the local matrices \(W_v\) are inverted, with the independently proved lower bound (HT4). No global inverse has been defined through the spectrum one hopes to bound.

This realizes the constructive branch of
[[global-local-response-reconstruction/quantitative-descent-and-the-shape-of-a-gap|quantitative gluing, QD7–QD8]],
with zero reconstruction error. It is distinct from
[[contemporary-puzzles/yang-mills-mass-gap/two-expectation-angle-process|the two-expectation process]]:
the present response compares transported sections along edges, not two conditional expectations on one observable algebra.

## Pauli transport supplies a concrete obstruction

Use \(\Gamma=(\mathbb Z/N\mathbb Z)^d\), with \(N\ge4\) even and \(d=2\) or \(3\), and \(H_v=\mathbb C^2\). Let the forward transport in direction \(j\) be the Pauli matrix \(\sigma_j\). These are unitary Hermitian reflections, with determinant \(-1\); they are not being called \(SU(2)\) matrices.

They satisfy
\[
\sigma_j^2=I,\qquad
\sigma_i\sigma_j=-\sigma_j\sigma_i\quad(i\ne j).
\tag{HT9}
\]
Every elementary square in two distinct directions therefore has holonomy \(-I\). Choose at each vertex just the positively rooted square in directions \(1,2\), with weight one. Then
\[
W_v=4I,\qquad \ell=4,\qquad B=8,
\]
because each edge in those two directions belongs to two chosen squares. Thus (HT5) gives \(L_T\ge\tfrac12I\), independently of \(N\); extra-direction energies are nonnegative.

The actual lower edge is sharper:
\[
\boxed{\inf\sigma(L_T)=2d-2\sqrt d>0.}
\tag{HT10}
\]
For commuting lattice shifts \(S_j\), put \(C_j=(S_j+S_j^*)/2\). Up to the harmless direction convention,
\[
L_T=2dI-2\mathsf B,\qquad
\mathsf B=\sum_{j=1}^dC_j\otimes\sigma_j,\qquad
\mathsf B^2=\sum_{j=1}^dC_j^2\otimes I\le dI.
\tag{HT11}
\]
Anticommutation cancels the mixed terms. A constant section with spinor in the \(+\sqrt d\) eigenspace of \(\sum_j\sigma_j\) attains (HT10). On \(\mathbb Z^d\), truncating that section to expanding boxes has only a boundary-to-volume error, so the same spectral infimum holds without a normalizable edge eigenvector.

Equivalently, the two Fourier bands are
\[
\lambda_\pm(k)=2d\pm2\sqrt{\sum_j\cos^2k_j}.
\tag{HT12}
\]
The gap is produced by incompatible parallel transport, not by an added term \(m^2\sum_v\|x_v\|^2\). The diagonal \(2dI\) in the expanded Laplacian is the ordinary edge-incidence contribution; with identity transports it cancels against the zero-momentum adjacency term.

The Pauli algebra is the associative envelope of
[[positive-cone-processes-and-the-complex-corner|the selected complex positive corner]].
Using it as transport is additional gluing data. Higher Clifford representations give related constructions in other dimensions; this example does not select three spatial dimensions or derive the graph.

## A completely positive observable process forgets this obstruction

On the finite even torus, pass instead to matrix-valued vertex observables
\(\mathcal M_\Gamma=\bigoplus_vM_2(\mathbb C)\), with the uniform vertex trace and normalized matrix trace. Replace each edge transport by conjugation.

For an edge \(e:v\to w\), the map exchanging its endpoint matrices through \(T_e\),
\[
(\mathscr S_eX)_v=T_e^*X_wT_e,\qquad
(\mathscr S_eX)_w=T_eX_vT_e^*,
\]
and fixing other vertices, is an involutive trace-preserving *-automorphism of \(\mathcal M_\Gamma\). Hence
\[
E_e=\tfrac12(I+\mathscr S_e)
\]
is a trace-preserving conditional expectation. The graph normalization is
\[
L_{\rm ad}=\sum_e(I-\mathscr S_e)=2\sum_e(I-E_e).
\tag{HT13}
\]
Its exponential is a UCP symmetric semigroup: each summand generates a convex mixture of \(I\) and \(\mathscr S_e\), and finite products converge to the summed semigroup. Writing \(\tau_2=\operatorname{Tr}/2\), its quadratic form is
\[
\langle X,L_{\rm ad}X\rangle
=\frac1{|V|}\sum_e\tau_2\!\left[
(X_w-T_eX_vT_e^*)^*(X_w-T_eX_vT_e^*)\right].
\]
This is an actual observable-algebra process, not merely the vector heat operator relabelled. The normalized vertex trace here is a finite-volume choice; no uniform probability measure on \(\mathbb Z^d\) has been assumed.

But \(\operatorname{Ad}(-I)=I\). The three automorphisms
\(\mathscr A_j=\operatorname{Ad}\sigma_j\) commute and square to the identity. On the even torus,
\[
G_v=\prod_j\mathscr A_j^{v_j}
\]
is a periodic fiber-coordinate transformation with
\(G_{v+\hat j}=\mathscr A_jG_v\). Writing \(X_v=G_vY_v\) therefore trivializes every adjoint edge. Consequently
\[
\boxed{L_{\rm ad}\simeq L_{\rm graph}\otimes I_{M_2},\qquad
\dim\ker L_{\rm ad}=4,\qquad
\operatorname{gap}(L_{\rm ad})=4\sin^2(\pi/N)\longrightarrow0.}
\tag{HT14}
\]
This gap is measured above the **entire** parallel kernel, not just the scalar unit. Already \(X_v=f(v)I\) supplies the ordinary slow scalar modes.

The change from vector to adjoint representation removes exactly the central loop discrepancy used by (HT3). This is the same kind of global-sensitivity distinction as
[[exceptional-gauge-realization/faithful-and-adjoint-holonomy-response|faithful versus adjoint holonomy]],
now with an explicit volume-uniform spectral consequence on one carrier and its failure on the other. It is not proof that a composite bound state is gapless: the adjoint heat process is not the two-particle Hamiltonian of the vector model.

[[positive-energy-pairs-and-the-neutral-gap|The positive-energy pair construction]] now makes this distinction constructive. The same response root \(A=\sqrt{L_T}\) yields a free charged Fock vacuum and a neutral pair threshold \(2\inf\sigma(A)\), transported by an explicit energy intertwiner. [[directed-analytic-realization/neutral-gaussian-return-of-holonomy-response|The Gaussian field return]] realizes that threshold in the vacuum carrier of a neutral local observable family. Global phase neutrality and a fixed-background free theory are not the Yang–Mills Gauss-law construction.

## What a causal-action construction must still supply

The positive lesson is precise: a local compositional obstruction can force a quantitative global bound without an on-site potential or a large enclosing box. The relevant invariant is the jointly visible holonomy defect together with bounded transport congestion, not bare topological nontriviality.

Three additional obligations cannot be omitted:

- **Realization:** prove that the physical nonvacuum carrier sees the obstruction. A section carrier with no zero mode is not yet a physical vacuum-plus-excitation space. Passing to a new representation, algebra, quotient or state must preserve an appropriate bound rather than merely preserve the word “holonomy.”
- **Selection and scale:** derive the transport law and its normalization. The graph result is uniform in volume at fixed edge convention. Assigning edge length \(a\) to a spatial discretization changes the Laplacian to \(a^{-2}L_T\). [[pauli-transport-and-the-continuum-scaling-obstruction|The exact scaling identity]] shows that even anisotropic positive reweighting cannot retain a finite clock gap and finite propagation in multiple shrinking-lattice directions. Fixed \(-I\) holonomy per shrinking plaquette is not a smooth finite-curvature continuum limit.
- **The field law:** a Yang–Mills connection is dynamical and includes near-flat configurations. This theorem fixes a connection; it does not estimate a measure over connections, prove its vacuum law, or identify a translation Casimir. [[contemporary-puzzles/yang-mills-mass-gap/twisted-holonomy-and-the-neutral-hessian|The neutral-holonomy audit]] owns the separate finite-box and interacting-theory comparison.

Likewise, the square holonomies and their squared defects do not pick a historical arrow. A full directed construction must still identify its irreversible operation and its record structure. The point of the example is to constrain what that construction has to preserve when it produces local observables.

[[directed-analytic-realization/context_transport_receipt.py|The context–transport receipt]]
checks finite Pauli holonomies, connection forms and sharp modes, alongside the separate Peirce averaging identities.
[[directed-analytic-realization/context-transport-receipt-output.txt|Its output]]
distinguishes exact finite algebra from numerical mode and form tests.
