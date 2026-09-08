# Loop Coordinates and the Induced Clock

Closing gauge paths supplies physical coordinates, not an independent clock for each coordinate. On the theta graph, two fundamental loops share one edge, and the response of that edge becomes a mixed derivative between their holonomies. Keeping this term makes changes of spanning tree exactly covariant; dropping it changes observable decay rates. The construction gives a positive clock on the complete finite physical carrier, while exposing the graph and response weights that still have to be selected by a deeper theory.

**Status: [EXACT FINITE CONSTRUCTION] for the induced response, heat evolution, tree covariance and Haar spectrum; [OPEN] for selection of an interacting vacuum and a compatible four-dimensional continuum law.**

## Retain the response when changing the carrier

Let three oriented edges \(a,b,c\) join the same two vertices, and take a
nontrivial compact connected Lie group \(G\), normalized Haar measure,
and a fixed bi-invariant metric \(Q\). Put \(D=-\Delta_Q\). Start with
the supplied edge response
\[
H_\Gamma=\alpha_aD_a+\alpha_bD_b+\alpha_cD_c,
\qquad \alpha_a,\alpha_b,\alpha_c>0.
\tag{LC1}
\]
Its carrier is \(L^2(G^3)\), with the physical subspace fixed by both
vertex gauge groups. There is no magnetic potential in (LC1).

Choosing edge \(a\) as a spanning tree gives the based holonomies
\[
x=ba^{-1},\qquad y=ca^{-1},\qquad
(J_af)(a,b,c)=f(ba^{-1},ca^{-1}).
\tag{LC2}
\]
The coordinate change \((a,b,c)\leftrightarrow(a,x,y)\) preserves
product Haar. Thus \(J_a\) is an isometry onto the subspace invariant
under the gauge group at the other vertex. The remaining vertex acts
by simultaneous conjugation of \((x,y)\), so the complete physical
carrier is \(L^2(G^2)^{\operatorname{Ad}G}\), not a product of separate
one-loop class-function spaces. This is the
[[inq#Tree gauge displays what the filtration retains|existing tree-gauge reduction]].

For a \(Q\)-orthonormal basis \(X_A\), define
\(R_{x,A}f(x,y)=\left.\frac{d}{dt}\right|_0f(xe^{tX_A},y)\),
and similarly for \(y\). Varying \(a\) on its left moves both loops
on their right by \(e^{-tX_A}\). Consequently the reduced operator is
\[
\begin{aligned}
L_a&=\alpha_bD_x+\alpha_cD_y
       -\alpha_a\sum_A(R_{x,A}+R_{y,A})^2\\
   &=(\alpha_a+\alpha_b)D_x+(\alpha_a+\alpha_c)D_y
       -2\alpha_a\sum_AR_{x,A}R_{y,A},\\
H_\Gamma J_a&=J_aL_a.
\end{aligned}
\tag{LC3}
\]
These identities hold first on smooth functions and then on the
self-adjoint operators with their compact-manifold \(H^2\) domains.
The form domain is \(H^1(G^2)\), restricted to simultaneous invariants
for the physical theory. Its positive form is
\[
\mathcal E_a(f)=\int\sum_A\left[
\alpha_b|R_{x,A}f|^2+\alpha_c|R_{y,A}f|^2
+\alpha_a|R_{x,A}f+R_{y,A}f|^2\right],dx,dy.
\tag{LC4}
\]
In right-trivialized coordinates its cometric is
\[
C_a=
\begin{pmatrix}
\alpha_a+\alpha_b&\alpha_a\\
\alpha_a&\alpha_a+\alpha_c
\end{pmatrix}\otimes I_{\mathfrak g}.
\tag{LC5}
\]
Its determinant in each Lie-algebra direction is
\(\alpha_a\alpha_b+\alpha_a\alpha_c+\alpha_b\alpha_c>0\).
The coupling is imposed by the shared edge, not fitted to a spectrum.
Maximal-tree electric couplings are established machinery;
[[library/a-new-basis-for-hamiltonian-su-2-simulations/inq|Bauer and collaborators]]
provide the broader Hamiltonian context. Equations (LC2)–(LC5) derive
the particular response used here without assuming their general formulas.

## The finite clock is constructed, not merely named

Let \(q_s\), for \(s>0\), be the central heat density for \(e^{-sD}\). The three
Casimir terms in the first line of (LC3) commute, and the exact heat
evolution for \(t>0\) is
\[
\begin{split}
(e^{-tL_a}f)(x,y)=\int_{G^3}
&q_{\alpha_at}(u)q_{\alpha_bt}(v)q_{\alpha_ct}(w)\\
&\times f(xvu^{-1},ywu^{-1}),du,dv,dw.
\end{split}
\tag{LC6}
\]
This is a self-adjoint Markov semigroup and a Hilbert-positive
contraction, with the identity at \(t=0\) by strong continuity.
It preserves the physical subspace.
Ellipticity, compactness and connectedness give compact resolvent and
the unique zero mode \(1\). Both loops see the same integrated
variable \(u\); replacing it by independent variables changes the law.
The positive integral representation does not decide whether probability
is fundamental ontology.

For smooth positive simultaneous-conjugation-invariant density
\(w_0(x,y)\), the same differential response instead defines
\(\int\langle\nabla f,C_a\nabla f\rangle w_0\,dx,dy\).
Its generator is the corresponding weighted divergence operator;
its drift and spectrum generally differ from (LC3) and (LC6).
A changed state must be transported along with the cometric.
The Haar spectral statements below do not apply unchanged to that case.

## A change of tree transports the whole form

Using edge \(b\) as tree gives
\[
u=ab^{-1}=x^{-1},\qquad v=cb^{-1}=yx^{-1},\qquad
\Phi(x,y)=(x^{-1},yx^{-1}).
\tag{LC7}
\]
This is a Haar-preserving diffeomorphism equivariant for simultaneous
conjugation. For \(Uf=f\circ\Phi\),
\[
L_aU=UL_b,\qquad
L_b=\alpha_aD_u+\alpha_cD_v
       -\alpha_b\sum_A(R_{u,A}+R_{v,A})^2.
\tag{LC8}
\]
Indeed \(J_aU=J_b\); both sides of (LC8) are the same edge operator
written through different isometries. This proves full operator and
semigroup covariance, not only equality of a selected eigenvalue.

Three physical witnesses show why the mixed term is necessary. For any
nontrivial irreducible \(\lambda\), the normalized Haar characters
\(\chi_\lambda(x)\), \(\chi_\lambda(y)\), and
\(\chi_\lambda(yx^{-1})\) have respective eigenvalues
\[
C_2(\lambda)(\alpha_a+\alpha_b),\quad
C_2(\lambda)(\alpha_a+\alpha_c),\quad
C_2(\lambda)(\alpha_b+\alpha_c).
\tag{LC9}
\]
Matching the first two with an independent loop clock
\(\beta_xD_x+\beta_yD_y\) forces its third value to be
\(C_2(\lambda)(2\alpha_a+\alpha_b+\alpha_c)\), which is wrong.
The shared response cancels in the relative loop \(yx^{-1}\).

More generally, the free-loop reparametrization
\(N(x,y)=(x,xy)\) preserves Haar and simultaneous conjugation,
but not the reset product clock \(D_x+D_y\):
\(\chi_\lambda(y)\) has eigenvalue \(C_2(\lambda)\), while its
pullback \(\chi_\lambda(xy)\) has eigenvalue \(2C_2(\lambda)\).
Preserving an algebra and its state is not enough to preserve its clock.
Covariance means transforming the response tensor, not demanding the
same diagonal coefficients in every presentation.

[[gauge-boundary-frame-gluing/holonomy-refinement-and-clock-compatibility#Individually autonomous loop readouts can have a nonautonomous join|The adjacent-square specialization]]
also computes what happens when relative-loop information is forgotten:
the two separate character readouts are autonomous, but their joint
readout has an exact two-rate compression defect. Restoring the third
trace completes the isolated \(SU(2)\) pair's invariant carrier.

## The full spectral edge and its refinement obligation

The [[contemporary-puzzles/yang-mills-mass-gap/gauge-descent-flux-fisher-coercivity#Gauge invariance sharpens the constant to girth times Casimir|weighted girth--Casimir theorem]]
controls the entire physical carrier. With
\(\lambda_G=\min_{\lambda\ne1}C_2(\lambda)\), it gives
\[
\operatorname{gap}(L_a|_{\mathrm{GI}})
=\lambda_G\min\{
\alpha_a+\alpha_b,\alpha_a+\alpha_c,\alpha_b+\alpha_c\}.
\tag{LC10}
\]
For \(SU(2)\), the complete theta spin-network spectrum consists of
\(\alpha_aC_2(j_a)+\alpha_bC_2(j_b)+\alpha_cC_2(j_c)\):
the three half-integer spins satisfy the triangle inequalities and
\(j_a+j_b+j_c\in\mathbb Z\). Each admissible triple has one invariant
intertwiner at each vertex; accidental energy coincidences can still
give degeneracies. This is a full-carrier justification of (LC10),
not an inference from only the three probes in (LC9).

[[gauge-boundary-frame-gluing/holonomy-refinement-and-clock-compatibility|Holonomy refinement]]
requires the segment weights to add to the old edge weight under
same-clock subdivision. The mixed coefficient in (LC5) then retains
the total response of the shared path. Adding new cycles is a separate
operation: it can introduce new low-energy states even while every
old loop and its clock are exactly preserved.

The construction therefore does not select a mass by loop topology
alone. It selects a covariant response **given** the edge law, and
identifies the additional data a proposed whole-to-local law must fix.
The existing [[receipts/gauge_cycle_innovation_receipt.py|cycle receipt]]
checks this covariance on the complete finite \(S_3\) theta carrier,
using Haar-reset generators instead of Lie-group Laplacians. Its
integer matrix identities test the common-edge construction and the
failure of resetting loop dynamics; they do not approximate a
continuous-group or four-dimensional Yang--Mills gap.
