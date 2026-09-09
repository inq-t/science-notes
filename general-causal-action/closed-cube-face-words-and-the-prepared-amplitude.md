# Closed Cube Face Words and the Prepared Amplitude

A cube has five independent graph cycles but six plaquette comparisons. An explicit tree gauge preserves product Haar measure on five loop coordinates and makes the sixth face a dependent non-Abelian word. The resulting sourced magnetic factor retains this relation exactly. It supplies a finite closed-cell sewing test without identifying a magnetic likelihood with the physical vacuum or replacing the raw-edge kinetic operator.

**Status: exact finite graph, Haar and marked-amplitude identities; proposed next closed-cell composition test.** The weighted character cost is the declared input of [[weighted-character-scale-and-bounded-lie-sources|GM]]. This closed boundary differs from the selected three faces of [[three-face-corner-and-joint-seam-response|CJ]], which do not enclose a cell.

## Fix the graph, tree and common root

Label the vertices by \(ijk\in\{0,1\}^3\), with root \(000\). Orient every edge in the positive coordinate direction. Name the bottom horizontal edges
\[
a:000\to100,\quad b:100\to110,\quad
c:010\to110,\quad p:000\to010,
\]
the vertical edges \(t_{ij}:ij0\to ij1\), and the top edges
\[
A:001\to101,\quad B:101\to111,\quad
C:011\to111,\quad D:001\to011.
\tag{CW1}
\]
The seven edges \(a,b,c,t_{00},t_{10},t_{01},t_{11}\) form a spanning tree. Thus \(12-8+1=5\) chords remain.

Path products are written in traversal order. Let \(T_z\) be the tree path from the root to \(z\). Under \(U_e\mapsto g_{\mathrm s(e)}U_eg_{\mathrm t(e)}^{-1}\), the based chord and face words are
\[
T_{\mathrm s(e)}U_eT_{\mathrm t(e)}^{-1},
\qquad T_zF_zT_z^{-1}.
\tag{CW2}
\]
They transform by the single root conjugation. Setting \(g_z=T_z\) gauges the tree edges to the identity. Below, chord letters denote their resulting based values. In particular the back-face connector is \(T_{010}=abc^{-1}\), not the chord \(p\).

The six faces use positive coordinate orientations; they are not all outward-oriented boundary faces. Their raw paths and tree-gauge values are:

| Face and base | Raw path | Based value |
|---|---|---|
| bottom \(xy\), \(000\) | \(abc^{-1}p^{-1}\) | \(p^{-1}\) |
| front \(xz\), \(000\) | \(at_{10}A^{-1}t_{00}^{-1}\) | \(A^{-1}\) |
| right \(yz\), \(100\) | \(bt_{11}B^{-1}t_{10}^{-1}\) | \(B^{-1}\) |
| back \(xz\), \(010\) | \(ct_{11}C^{-1}t_{01}^{-1}\) | \(C^{-1}\) |
| left \(yz\), \(000\) | \(pt_{01}D^{-1}t_{00}^{-1}\) | \(pD^{-1}\) |
| top \(xy\), \(001\) | \(ABC^{-1}D^{-1}\) | \(ABC^{-1}D^{-1}\) |

Each raw path is first transported using CW2. Consequently, on defining
\[
u=p^{-1},\quad v=A^{-1},\quad w=B^{-1},\quad
x=C^{-1},\quad y=pD^{-1},
\]
\[
\boxed{(F_1,\ldots,F_6)=(u,v,w,x,y,v^{-1}w^{-1}xuy).}
\tag{CW3}
\]
Direct substitution proves the ordered closure identity
\[
w\,v\,F_6\,y^{-1}u^{-1}x^{-1}=e.
\tag{CW4}
\]
Commuting the factors would change this identity.

## Preserve the Haar carrier and every mark

For compact \(G\), normalized product Haar on the twelve raw edges becomes product Haar on the seven tree variables and five based chords. This follows successively from left and right Haar invariance along the tree; integrating the tree variables contributes one. Inversion preserves Haar, and, conditional on \(p\), \(D\mapsto pD^{-1}\) preserves Haar. Hence
\[
d p\,dA\,dB\,dC\,dD=du\,dv\,dw\,dx\,dy.
\tag{CW5}
\]
The physical carrier is therefore \(L^2(G^5,d\mathrm{Haar}^5)^{\operatorname{Ad}G}\), without assuming a smooth orbit quotient.

A bounded joint mark \(M:G^6\to\mathbb C\) becomes exactly
\[
\widetilde M(u,v,w,x,y)
=M(u,v,w,x,y,v^{-1}w^{-1}xuy).
\tag{CW6}
\]
Physical scalar marks are invariant under simultaneous conjugation. Covariant boundary marks retain their common root index or its explicitly supplied closure. Changing connectors requires transporting the original marked words too; central face costs alone cannot record that change.

## Keep cost, magnetic factor and chronology distinct

For GM's faithful representation and positive commuting weight, retain
\[
W_A(U)=\operatorname{Re}\operatorname{Tr}[A(I-\rho(U))],
\qquad
H=\kappa\sum_{e=1}^{12}\mathsf C_{e,Q}
+g\sum_{j=1}^{6}W_A(F_j).
\tag{CW7}
\]
Here \(Q\) is the fixed Ad-invariant metric and \(\mathsf C_{e,Q}\) is the original nonnegative edge Casimir, with the sum restricted to the Gauss-invariant carrier. The common \(g\) is declared. \(W_A\), and UW's normalized \(w_\varepsilon=W_{A_\varepsilon}/15\), are costs. At a supplied magnetic duration \(s\ge0\), the positive central factor is instead
\[
\mathcal F_{A,s}(U)=e^{-sgW_A(U)}.
\]
The exact sourced magnetic integral is
\[
\boxed{\mathcal Z_s[M]=\int_{G^5}
\widetilde M\,
\prod_{z\in\{u,v,w,x,y\}}\mathcal F_{A,s}(z)\,
\mathcal F_{A,s}(v^{-1}w^{-1}xuy)\,d\mathrm{Haar}^5.}
\tag{CW8}
\]
Its source-free normalization is positive. Dividing by it defines a magnetic likelihood, not the actual ground-state density. The full transfer still requires kinetic sewing. In these coordinates the raw Casimirs in CW7 induce coupled derivatives; five independent loop Casimirs cannot be substituted.

Boundedness on the compact carrier proves Fubini consistency for every joint \(M\), including partially retained integrals. Both elimination orders must retain the dependent factor and the same normalization. This is exact integration, not a selection theorem.

## The kinetic and marked consequences

The proposed closed-cell operation retains all six original comparisons with one common coupling, the actual boundary marks and the raw-edge kinetic action. It introduces neither an independent sixth loop nor a tunable cell potential. [[closed-cube-raw-edge-kinetic-sewing|CK]] now derives every original edge derivative in this chart. The coupled kinetic matrix and dependent-face Hessian give harmonic frequencies \(2,2,2,\sqrt6,\sqrt6\).

[[closed-cube-dependent-face-and-oriented-source-jet|CD]] extracts the cubic magnetic word term and a bounded joint bracket mark with both positive and negative pairwise coefficients. [[closed-cube-bracket-source-and-the-actual-vacuum-return|CQ]] returns those coefficients and the marked chronology in the actual compact vacuum. Its centered bracket mark reaches the existing lowest neutral harmonic energy four. The signed source relation has been computed; no additional mass contribution follows from its positive aggregate.

## A closed boundary does not distinguish an ambient bulk

The cube graph itself is planar, and CW4 is also the sphere's face relation. More precisely, give a spherical cellulation the same oriented graph, six attaching words, edge metric and coefficients, prepared face factors and original marks. The raw Haar carrier and Hamiltonian CW7 are then identical, as is the Gauss action. Tree reduction gives the same unitary realization and every marked chronological amplitude. No calculation using only these data can distinguish the two ambient interpretations.

[[two-cube-shared-face-and-the-original-kinetic-law|TC]] now carries out the first shared-cell test with two cubes sharing one face. There are \(16-4=12\) vertices, \(24-4=20\) edges, \(12-1=11\) distinct plaquettes and \(20-12+1=9\) independent graph cycles. Its two ordered cell relations retain the compatible upper-cell connector transports. The ten exterior faces form a sphere, while the shared plaquette supplies an additional incidence: each of its four edges belongs to three distinct plaquettes. That incidence is absent from the single boundary surface.

[[two-cube-temporal-sewing-and-the-actual-joint-source|TJ]] sews the shared face and its four electric histories once, retaining the actual global vacuum caps and joint marks through either integration order. Adding two complete single-cell Hamiltonians would double those terms. The control omits only the shared magnetic cost, retaining the same word mark and all twenty electric edges.

[[two-cube-interior-cost-and-the-joint-bracket-response|TI's fixed cross-cell bracket source]] has a decreasing expectation as the interior cost is attached. TJ proves this decrease in the actual compact vacuum, although the fully attached endpoint has a larger full gap. The harmonic gap change is already an Abelian incidence effect. At full attachment the leading bracket mark misses the lowest physical modes; its possible nonlinear overlap with them is the next source-support test. Elimination-order agreement alone remains integration consistency.

[[reciprocal-coefficients-and-the-field-gap-test|FG]] already shows that linear incidence constraints alone permit soft modes. Full-amplitude integration, as in [[holonomy-state-refinement/overlap-kernels-and-face-refinement|OF15–18]], does not select the group, preparation or clock. Any shared-cell gap test must retain [[two-slice-innovation-geometry/regional-innovation-and-exterior-information-balance|RI's inherited exterior response]] and [[spatial-block-sewing-and-the-vacuum-cap-response|SB's temporal vacuum caps]], rather than infer coercivity from the closure identity.
