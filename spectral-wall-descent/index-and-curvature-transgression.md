# Index and Curvature Transgression Through the Wall

The most defensible invariant through observable symmetry breaking is a \(K\)-homology or cyclic fundamental class, not energy, entropy, or unitary information. Bounded inner fluctuations preserve the class while local Chern representatives change by transgression. Relative \(K\)-theory then records which contextual distinctions disappear in the homogeneous algebra, and a separate connection-and-soldering construction may turn their transgression into spacetime curvature.

## The class preserved by inner fluctuation

Let an even real spectral triple represent a fundamental class

$$
\mu_D
\in
KKO_n(
\mathcal A\widehat\otimes\mathcal A^{\mathrm{op}},
\mathbb R).
$$

For a norm-continuous family of bounded odd self-adjoint perturbations \(B_t\), put

$$
D_t=D+B_t.
$$

Under the usual regularity and Fredholm hypotheses, the bounded transforms

$$
F_t=D_t(1+D_t^2)^{-1/2}
$$

form an operator homotopy. Hence

$$
\boxed{[D_t]=[D]\text{ in }KKO.}
$$

For projections \(p_i,p_j\) representing \(K_0(\mathcal A)\), all intersection pairings

$$
Q_{ij}(D)
:=\operatorname{Index}
\left(
P_{ij}D^+P_{ij}
\right),
\qquad
P_{ij}=\pi(p_i)J\pi(p_j)J^{-1},
$$

are consequently constant along the perturbation. Connes' inner fluctuations are bounded because they are built from bounded commutators \(a[D,b]\). Gauge fields, Higgs representatives, masses, and the spectral action may change without changing these index pairings.

This is **[STANDARD OPERATOR \(K\)-THEORY UNDER THE STATED HYPOTHESES]**. Topology change, failure of Fredholmness, or a change of algebra or domain can invalidate the homotopy and permit a jump. A quantum anomaly may obstruct a gauge symmetry without changing this \(K\)-class and must be analyzed separately.

## Cyclic transgression

For a suitably summable differentiable family, the JLO Chern character satisfies schematically

$$
\boxed{
\frac{\mathrm d}{\mathrm dt}
\operatorname{Ch}_{\mathrm{JLO}}(D_t)
=(b+B_{\mathrm{cyc}})
\operatorname{CS}(D_t,\dot D_t).}
$$

Thus

$$
\operatorname{Ch}(D_1)-\operatorname{Ch}(D_0)
=(b+B_{\mathrm{cyc}})\operatorname{CS}(D_t).
$$

The local representative changes, but its cyclic-cohomology class and its pairing with closed cycles remain fixed. On a region with boundary, a specified relative cocycle or local-index realization can pair the transgression with the boundary through an appropriate Stokes theorem. The \((b+B)\)-coboundary does not become a physical wall term automatically. When the relative pairing is constructed, it gives a cohomological balance of local density and boundary contribution, not a scalar conservation of information.

[[library/quanta-of-geometry/inq|Quanta of Geometry]] supplies a close local precedent. Its two-sided relation gives

$$
\det(e)=\Omega_++\Omega_-,
$$

while the integrated volume is fixed by the degrees of \(Y_\pm\), equivalently an index pairing. For a smooth family,

$$
\frac{\mathrm d}{\mathrm dt}
Y_t^*\omega
=d\left(Y_t^*\iota_{\dot Y_t}\omega\right),
$$

so local volume density can flow through a boundary while the global degree remains fixed. The construction already assumes a manifold and Dirac operator; it is a grammar for the desired balance, not its pregeometric derivation.

## Relative \(K\)-theory of an observable context

Let \(i:\mathcal B\hookrightarrow\mathcal A\) be the inclusion of an observable subalgebra and define its mapping cone by

$$
C_i
:=\left\{
(b,f)\in\mathcal B\oplus C_0([0,1),\mathcal A)
:f(0)=i(b)
\right\}.
$$

It fits into \(0\to S\mathcal A\to C_i\to\mathcal B\to0\). Use the shifted convention

$$
K_j(\mathcal A,\mathcal B)
:=K_{j+1}(C_i),
$$

with indices modulo two. The long exact sequence then contains

$$
K_0(\mathcal B)
\xrightarrow{i_*}
K_0(\mathcal A)
\longrightarrow
K_0(\mathcal A,\mathcal B)
\longrightarrow
K_1(\mathcal B)
\longrightarrow
K_1(\mathcal A)
\longrightarrow
K_1(\mathcal A,\mathcal B).
$$

For the diagonal context

$$
\mathcal B=\mathbb C^n
\subset
\mathcal A=M_n(\mathbb C),
$$

one has

$$
K_0(\mathcal B)=\mathbb Z^n,
\qquad
K_0(\mathcal A)=\mathbb Z,
\qquad
i_*(k_1,\ldots,k_n)=\sum_i k_i,
$$

and both ordinary \(K_1\) groups vanish. Exactness therefore gives the **[EXACT FINITE CALCULATION]**

$$
\boxed{
K_0(\mathcal A,\mathcal B)=0,
\qquad
K_1(\mathcal A,\mathcal B)
\cong
\left\{k\in\mathbb Z^n:\sum_i k_i=0\right\}
\cong A_{n-1}.}
$$

All minimal projections of \(\mathcal B\) become Murray--von Neumann equivalent in the simple algebra \(M_n\). Their total rank survives, while their balanced differences form \(\ker\sum\cong\mathbb Z^{n-1}\). With the standard coordinate bilinear form this embedded lattice is the \(A_{n-1}\) root lattice. After tensoring with \(\mathbb R\),

$$
\mathbb R^n
=\mathbb R(1,\ldots,1)
\oplus
\left\{\zeta:\sum_i\zeta_i=0\right\}.
$$

This is an algebraic skeleton for the homogeneous and mean-zero observational sectors of the common response form. It does not provide their BKM metric, continuum carrier, or gravity map.

The expectation \(E:\mathcal A\to\mathcal B\) and the inclusion \(i:\mathcal B\hookrightarrow\mathcal A\) perform different jobs. The expectation supplies entropy and BKM loss. The inclusion supplies relative \(K\)-theory. A completely positive kernel is generally not an ideal, so it must not be inserted into a six-term exact sequence as though it came from a \(C^*\)-quotient.

## Symmetry reduction and curvature

Let a principal \(G\)-bundle \(P\to X\) admit a reduction to \(H\subset G\). Equivalently, under the standard hypotheses, the associated bundle \(P/H\to X\) has a section. The chosen reduction makes only \(H\) manifest, while the full \(G\)-bundle and its transition laws remain.

After pulling a \(G\)-connection back to the chosen \(H\)-reduction, a reductive splitting

$$
\mathfrak g=\mathfrak h\oplus\mathfrak m,
$$

a connection decomposes as

$$
\mathcal A=\omega+e,
$$

with curvature

$$
\boxed{
F_{\mathcal A}
=F_\omega
+D_\omega e
+\frac12[e,e].}
$$

In Cartan geometry, the \(\mathfrak m\)-valued component \(e\) becomes a genuine solder form only when it is horizontal, equivariant, nondegenerate, and identifies \(\mathfrak m\) with tangent directions. For de Sitter or anti-de Sitter model geometry this takes the convention-dependent schematic form

$$
\mathcal A=\omega+\ell^{-1}e,
\qquad
F_{\mathcal A}
=\left(R_\omega\mathbin{\pm}\ell^{-2}e\wedge e\right)
+\ell^{-1}T.
$$

This gives a concrete sense in which spacetime curvature may be the additional structure required to compare locally symmetry-broken observable frames while the larger equivariant geometry persists.

The connection part of this construction is expressed by the Atiyah sequence

$$
0
\longrightarrow
\operatorname{ad}P
\longrightarrow
\operatorname{At}(P)
\longrightarrow
T_X
\longrightarrow0.
$$

A connection is a splitting as vector bundles. Its curvature is the failure of that splitting to preserve Lie brackets. [[basic-concepts/soldering/inq|Strict soldering]] is still required before an internal curvature can be called spacetime gravity.

## The proposed wall diagram

The candidate construction now separates four typed statements:

$$
\begin{aligned}
K_*(\mathcal A,\mathcal B)
\times HP^*(\mathcal A,\mathcal B)
&\xrightarrow{\ \langle\cdot,\cdot\rangle_{\mathrm{rel}}\ }
\mathbb C,
\qquad &&\text{standard when the relative classes exist},\\
\text{relative cocycle representative}
&\dashrightarrow
\text{boundary curvature density},
&&\text{open transgression and soldering},\\
G^{\mathrm{ret}}
&\xrightarrow{\ \mathfrak S\ }
\mathcal E_{\mathrm{can}}^{\mathrm{grav}},
&&\text{calibrated in controlled AdS code sectors},\\
\mathcal L_\chi(U)
&\stackrel{?}{=}
\eta_*\mathcal A_D^Z(U),
&&\text{open central spectral-area weld}.
\end{aligned}
$$

The first line is topological and cohomological. The dashed arrow is not supplied by the Chern character alone. The retained-response line is continuous and metric, while the final line compares a central entropy operator with a dimensionful spectral assignment. [[spectral-wall-descent/finite-index-area-weld|The finite-index area weld]] shows only that, for a type-I product state compared with an auxiliary tracial expectation, edge entropy plus tracial defect equals half the Watatani log index. The code expectation selecting the fixed edge state is generally different, so no general index--area theorem follows.

A completed theory must show that these statements arise compatibly from one scale-indexed correspondence without identifying an integer index, its logarithm, edge entropy, BKM norm, and physical area. [[spectral-wall-descent/scale-correspondence-stack|The scale-correspondence prestack]] is the present typed container and effective descent remains open.

## Failure conditions

- A \(KK\)-equivalent inclusion has trivial relative \(K\)-groups and therefore no nonzero relative class of the proposed kind; this does not by itself make every metric or entropy defect vanish.
- Index invariance alone cannot determine a continuous mass, entropy, or Newton coefficient.
- With nontrivial centers, scalar minimal index is not functorially multiplicative; the matrix dimension or full correspondence must be retained.
- A conditional expectation is not a quotient homomorphism and has no automatic six-term sequence.
- A \(G\to H\) reduction is not gravity unless its coset component is genuinely soldered to \(TX\).
- Curvature of a context bundle is not automatically Lorentzian spacetime curvature.
- A local transgression becomes a physical wall balance only after boundary conditions and a carrier are specified.
- A topological jump is possible if the path leaves the Fredholm or fixed-algebra sector.
