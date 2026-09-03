# The Octonionic Slice Groupoid and the Chiral Origin

The ordinary orbit set of octonionic complex directions is a point, but the corresponding quotient stack is not: for (S^6=G_2/SU(3)), the transitive action groupoid presents ([S^6/G_2]simeq BSU(3)). This is the precise category in which a selected complex direction is an origin for relational symmetry rather than a location in a prior space. The stack retains the stabilizer, all twisted (SU(3))-torsors, and the universal associated color carrier (W=(mathbb C^3)_{mathbb R}), while a connection remains additional data. Passing from oriented directions (S^6) to unoriented complex subalgebras (mathbb RP^6) extends the stabilizer by a reversal (mathbb Z_2); an (SU(3))-reduction is then exactly a choice of handed origin in the resulting double-cover torsor. The Clifford grading changes sign under this reversal, whereas the Wilson and Killing responses descend because they are even. This derives a rigorous common grammar for origin, torsor, chirality, and color, but it does not yet derive chiral matter, a connection, a physical scale, or a Yang--Mills mass gap.

**Status: [EXACT] for the transitive-groupoid equivalence, torsor classification, associated tangent and Clifford carriers, orientation-reduction obstruction, and Wilson character; [EXACT CITED] for the (G_2	o S^6) principal bundle and its clutching class; [PROPOSED INTERPRETATION] for a selected orientation as the structural origin of an observed symmetry; [OPEN] for a dynamically selected reduction, a connection and state, the Standard Model chiral bimodule, anomaly cancellation, interacting-vacuum coercivity, continuum reconstruction, and dimensional calibration.**

## The coarse quotient commits the category error

Fix a unit imaginary octonion (u_0), and put

\[
H:=\operatorname{Aut}(\mathbb O;u_0)\cong SU(3).
\tag{SG1}
\]

The (G_2=\operatorname{Aut}(\mathbb O)) action on unit imaginary octonions is
transitive, so

\[
S^6\cong G_2/H.
\tag{SG2}
\]

If one takes only the coarse orbit set, then

\[
S^6/G_2=\{*\}.
\tag{SG3}
\]

That point has forgotten the very symmetry the construction is meant to explain.
The action groupoid retains it:

\[
G_2\ltimes S^6
=
\bigl(G_2\times S^6\rightrightarrows S^6\bigr).
\tag{SG4}
\]

The full subgroupoid on the one object (u_0) has arrow group exactly (H).
Its inclusion into (SG4) is fully faithful, and it is essentially surjective
because every (u\in S^6) is (g(u_0)) for some (g\in G_2). Therefore the
two Lie groupoids are Morita equivalent, and their differentiable quotient
stacks obey

\[
\boxed{
[S^6/G_2]
\simeq
BH
=
BSU(3).}
\tag{SG5}
\]

This is not the numerical observation that (SU(3)) happens to stabilize one
octonion. It is an equivalence of moduli problems. The left side presents a
covariant whole of complex directions and comparison arrows; the right side
presents color torsors.

In the language of [[basic-concepts/groupoids/inq|groupoids]] and
[[basic-concepts/stacks/inq|stacks]], the Copernican correction is

\[
\boxed{
\text{coarse quotient }S^6/G_2=*
\quad\rightsquigarrow\quad
\text{structural quotient }[S^6/G_2]\simeq BSU(3).}
\tag{SG6}
\]

The coarse quotient remembers only that every presentation is equivalent. The
stack remembers the arrows, their composition, and the automorphisms of each
presentation. Symmetry is precisely that retained isotropy.

## A point of the stack is a color torsor

For a test manifold or suitable base (X), (SG5) gives an equivalence of
groupoids

\[
\boxed{
\operatorname{Map}\bigl(X,[S^6/G_2]\bigr)
\simeq
\operatorname{Bun}_{SU(3)}(X).}
\tag{SG7}
\]

A map to the quotient stack may be described as a principal (G_2)-bundle
together with a (G_2)-equivariant map to (S^6), equivalently a reduction of
that bundle to (H). Under (SG5), this is simply an arbitrary principal
(SU(3))-bundle. Local complex directions and their comparison arrows are not
extra decoration on the torsor; they are another presentation of the same
descent datum.

This resolves an important false no-go. A literal global field

\[
s:X\longrightarrow S^6
\tag{SG8}
\]

inside one fixed trivial (G_2)-background produces only the special pullback
(s^*G_2\to X). If (X) is a four-dimensional CW complex, (s) is
null-homotopic because (S^6) is five-connected, so this pullback is trivial.
That narrow model cannot recover nonzero instanton bundles on (S^4).

The stack-valued field in (SG7) is larger. It permits local slice presentations
whose transition arrows form nontrivial descent data, and it is equivalent to
the groupoid of **all** (SU(3))-torsors, including nonzero second-Chern-class
sectors. The global map and the stack map are different types:

\[
\boxed{
X\to S^6
\quad\text{is a chosen global presentation, whereas}\quad
X\to[S^6/G_2]
\quad\text{is a possibly twisted color object}.}
\tag{SG9}
\]

[Gyenge's transition-function calculation](https://sigma-journal.com/2019/078/)
shows that the particular bundle (G_2\to S^6) has clutching function generating
(pi_5(SU(3))). Equation (SG7) does not claim that this one bundle is universal;
it says the *quotient stack of its transitive presentation* is the classifying
stack because twisting and descent have been retained.

## The symmetry group has an origin but the torsor does not

For (x\in X), the fibre (P_x) of a principal (H)-bundle is an
[[basic-concepts/torsors/inq|(H)-torsor]]. It has a canonical difference map

\[
\delta:P_x\times P_x\longrightarrow H,
\qquad
p\,\delta(p,q)=q,
\tag{SG10}
\]

but no preferred point that could play the role of the identity. Choosing
(p\in P_x) identifies the fibre with (H) by (h\mapsto ph); changing (p)
changes that coordinate identification while leaving every relational
difference intact.

There is a second, structural meaning of origin. Before (u_0) is selected,
there is a family of conjugate stabilizers

\[
H_u:=\operatorname{Aut}(\mathbb O;u),
\qquad
u\in S^6,
\tag{SG11}
\]

and arrows (g:u\to v) identify them only by conjugation. Selecting an object
(u) chooses the presentation about which its automorphisms are measured:

\[
H_u=\operatorname{Aut}_{G_2\ltimes S^6}(u).
\tag{SG12}
\]

Thus the selected direction is an **origin of the observed symmetry structure**,
not an absolute point of prior physical space. The symmetry group is the loop
group at that object. Forgetting the object but retaining the groupoid preserves
that statement up to equivalence; collapsing the groupoid to its orbit set does
not.

## The universal tangent carrier is the fundamental color carrier

The isotropy representation of (H) on the tangent at (u_0) is

\[
W:=T_{u_0}S^6
\cong
(\mathbb C^3)_{\mathbb R},
\qquad
\chi_W(U)=2\operatorname{Re}\operatorname{tr}_{\mathbf3}U.
\tag{SG13}
\]

Equivariantly,

\[
TS^6\cong G_2\times_H W.
\tag{SG14}
\]

Under (SG5), this tangent bundle corresponds to the universal associated real
color bundle. For a color torsor (P\to X), the carrier is therefore

\[
E_W:=P\times_H W.
\tag{SG15}
\]

This statement survives every topological sector. It does not require (E_W)
to be the pullback of (TS^6) along one global map (X\to S^6).

The Clifford operator globalizes on the homogeneous presentation as well. For
(u\in S^6) and (w\in T_uS^6\subset\operatorname{Im}\mathbb O), define

\[
c_u(w):=L_w\in\operatorname{End}_{\mathbb R}(\mathbb O).
\tag{SG16}
\]

Alternativity gives

\[
c_u(w)c_u(z)+c_u(z)c_u(w)
=-2\langle w,z\rangle I,
\tag{SG17}
\]

and hence the smooth (G_2)-equivariant fibrewise isomorphism

\[
\boxed{
\mathrm{Cl}_0(TS^6)
\cong
S^6\times\operatorname{End}_{\mathbb R}(\mathbb O).}
\tag{SG18}
\]

The associated octonion bundle is trivial because the (H)-representation on
(mathbb O) extends to (G_2):

\[
G_2\times_H\mathbb O
\xrightarrow{\ \cong\ }
S^6\times\mathbb O,
\qquad
[g,x]\longmapsto(g u_0,gx).
\tag{SG19}
\]

For (U\in H), the Clifford and holonomy actions obey the exact covariance
square

\[
\rho_{\mathbb O}(U)c(w)\rho_{\mathbb O}(U)^{-1}
=
c\bigl(\rho_W(U)w\bigr),
\qquad
\rho_{\mathbb O}=\mathbf1_{\mathbb R^2}\oplus\rho_W.
\tag{SG20}
\]

Thus Clifford multiplication and color holonomy are compatible operations on
one carrier. Neither is being inferred from a matching dimension.

## A connection is additional, but its minimal response is exactly Wilson

The classifying stack (BH) classifies torsors, not connections. A gauge field
requires a connection on (P), equivalently a lift to a differential
classifying object such as (B_\nabla H). Once a connection supplies plaquette
holonomies (U_p\), the invariant metric on (W) gives

\[
\begin{aligned}
Q_W^{\mathrm{car}}(U)
&:=
\sum_p\|\rho_W(U_p)-I\|_{\mathrm{HS}}^2\\
&=
\sum_p2\bigl(6-\chi_W(U_p)\bigr)\\
&=
12\sum_p\left(1-\frac13
\operatorname{Re}\operatorname{tr}_{\mathbf3}U_p\right).
\end{aligned}
\tag{SG21}
\]

Therefore

\[
\boxed{
Q_W^{\mathrm{car}}=12Q_W^{\mathrm{Wilson}}.}
\tag{SG22}
\]

The same formula holds on the octonion carrier because its two extra real
directions are color singlets. [[octonionic-clifford-completion-of-the-color-normal]]
places this minimal response in the exact ladder

\[
Q_{T_{\mathrm{fr}}}
=3Q_W^{\mathrm{car}},
\qquad
Q_N
=24Q_W^{\mathrm{car}}
=8Q_{T_{\mathrm{fr}}}.
\tag{SG23}
\]

The groupoid construction therefore recovers the ordinary fundamental Wilson
regulator on every color torsor once a connection and coupling are supplied. It
derives the group, the carrier, and the permitted twisting; it does not derive
the connection, the bare coupling, or the vacuum measure.

## Handedness is a reduction of the unoriented torsor

The complex subalgebra depends only on the unoriented line:

\[
\mathbb C_u=\mathbb C_{-u}.
\tag{SG24}
\]

Let

\[
K:=\operatorname{Stab}_{G_2}(\{u_0,-u_0\}).
\tag{SG25}
\]

Then (H\) is the identity component that fixes (u_0), and

\[
1\longrightarrow H\longrightarrow K
\longrightarrow\mathbb Z_2\longrightarrow1.
\tag{SG26}
\]

The oriented and unoriented homogeneous spaces form the double cover

\[
S^6=G_2/H
\longrightarrow
G_2/K\cong\mathbb RP^6.
\tag{SG27}
\]

At the structural quotient level this becomes

\[
\boxed{
[S^6/G_2]\simeq BH
\longrightarrow
[\mathbb RP^6/G_2]\simeq BK.}
\tag{SG28}
\]

The map is extension of structure group along (H\hookrightarrow K). It forgets
which orientation-preserving reduction was chosen. For a (K)-torsor (Q\to X),

\[
Q/H\longrightarrow X
\tag{SG29}
\]

is the associated (mathbb Z_2)-torsor of handed origins. An (H)-reduction is
equivalent to a section of (SG29). Its Čech class in (H^1(X;\mathbb Z_2)) is
the obstruction to a global choice.

This makes “handedness as preferred origin” exact. The preference is not a
marked spatial location. It is a reduction from transformations that may reverse
the complex axis to transformations that preserve one chosen axis. If the
(mathbb Z_2)-torsor is nontrivial, local handed choices cannot be glued. If it
is trivial, a sheet may be chosen, but neither the torsor nor the vanishing of
the obstruction says which sheet becomes factual.

## Chirality is an odd structural observable

On the complexified octonion carrier, with an external scalar copy
(mathbb C_{\mathrm{ext}}), define

\[
\mathcal H_{\mathbb O}
:=
\mathbb O\otimes_{\mathbb R}\mathbb C_{\mathrm{ext}},
\qquad
\gamma_u:=i_{\mathrm{ext}}L_u,
\qquad
P_\pm(u):=\frac{1\pm\gamma_u}{2}.
\tag{SG30}
\]

Then

\[
\gamma_{-u}=-\gamma_u,
\qquad
P_\pm(-u)=P_\mp(u),
\tag{SG31}
\]

and, up to which sign is named positive,

\[
P_+(u)\mathcal H_{\mathbb O}\cong\mathbf1\oplus\mathbf3,
\qquad
P_-(u)\mathcal H_{\mathbb O}\cong\mathbf1\oplus\bar{\mathbf3}.
\tag{SG32}
\]

Chirality is therefore not a real-valued function on the unoriented quotient.
It is naturally a section of the sign object associated to the orientation
torsor. Choosing an (H)-reduction trivializes that sign object and turns the
relative distinction into the labels (+/-). Reversal exchanges them.

The even descendants

\[
\gamma_u^2,
\qquad
\|\rho_W(U)-I\|_{\mathrm{HS}}^2,
\qquad
b_W(X,Y)
=
\operatorname{Tr}_W\bigl(\mathrm d\rho(X)^*\mathrm d\rho(Y)\bigr)
\tag{SG33}
\]

survive the quotient because they are invariant under that reversal. This is
the exact sense in which an observable can be a quotient **with retained
structure**: the stack remembers isotropy, the associated bundle remembers what
the symmetry acts on, and the invariant metric supplies a dimensionless scale
of relational difference. Passing all the way to the coarse orbit set destroys
those data.

The physical yardstick remains separate. Multiplying the invariant metric by a
positive constant changes the Casimir normalization and is compensated by the
kinetic coefficient. A dimensionless quotient metric does not yet define clock
energy or invariant mass.

## What this changes in the mass-gap programme

The construction closes three category errors at once:

1. the observed (SU(3)) is the automorphism group of a selected complex
   presentation, not a primordial symmetry waiting to be broken;
2. the quotient stack, unlike the orbit set or a single global slice field,
   retains every color torsor and its topological sectors; and
3. chirality is a reduction/section problem for an orientation torsor, while
   the Wilson response is its orientation-even metric shadow.

It does not identify these three outputs with a mass gap. The partial carrier in
(SG32) is balanced and has no supplied odd Fredholm operator; its
(mathbf3/\bar{\mathbf3}) split is color conjugacy, not the observed weak
left/right matter asymmetry. Pure Yang--Mills has no fermionic matter. A physical
chiral construction still needs a finite algebra and bimodule, a complete real
spectral cycle, a nonzero index or another declared imbalance, anomaly
cancellation, and gauge-invariant experimental channels.

Likewise, (SG22) recovers the Wilson regulator rather than solving it. The mass
gap still requires the interacting vacuum state, a regulator-uniform Poincare or
equivalent coercivity estimate on its complete gauge-invariant complement,
Osterwalder--Schrader continuum reconstruction, the Poincare Casimir, and an
independently normalized dimensional scale. The groupoid supplies the right
carrier category. It does not supply the missing positive lower edge.
