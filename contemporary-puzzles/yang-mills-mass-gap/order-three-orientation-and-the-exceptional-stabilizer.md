# Order-Three Orientation and the Exceptional Stabilizer

The exceptional flag admits a concrete asymmetry-first encoding. Yokota's order-three automorphism \(w\in F_4\) fixes \(\mathfrak h_3(\mathbb C)\), while its inverse \(w^2\) fixes the same subalgebra with the opposite hidden complex orientation. Cyclic averaging forgets that orientation, and adjoining a trace-two idempotent \(\ell\) leaves precisely \(S(U(2)\times U(3))\) as stabilizer. On the natural oriented-flag bundle, the idempotency defect has exact Hessian spectrum \(0^{(40)}\oplus1^{(4)}\). This derives symmetry, orientation, and a finite normal stiffness from one prior algebraic datum; it does not yet give the surviving gauge fields a Yang--Mills mass gap.

**Status: [EXACT CITED] for Yokota's automorphism and centralizer and for the exceptional-flag stabilizer; [EXACT] for the averaging, orientation-residue, projector, associated-bundle, and Hessian consequences; [CONSTRUCTION] for treating this flag as a field or holonomy probe; [OPEN] for physical chirality, Yang--Mills dynamics, OS reconstruction, continuum coercivity, and dimensional calibration.**

## The prior datum is an oriented automorphism

Choose a complex subalgebra \(\mathbb C\subset\mathbb O\). [[library/exceptional-lie-groups-yokota/inq|Yokota]] uses the real decomposition

$$
J:=\mathfrak h_3(\mathbb O)
\cong
\mathfrak h_3(\mathbb C)\oplus M_3(\mathbb C)
=:B\oplus B^\perp,
\tag{OT1}
$$

of dimensions \(9+18\), and constructs the real-linear Jordan automorphism

$$
w(X+M)=X+\omega M,
\qquad
\omega=-\frac12+\frac{\sqrt3}{2}i.
\tag{OT2}
$$

On the real space \(B^\perp\), multiplication by \(\omega\) means rotation through \(120^\circ\) in nine real two-planes. It is not scalar multiplication on all of the real Albert algebra. Yokota proves

$$
w^3=1,
\qquad
\operatorname{Fix}_J(w)=B,
\qquad
K:=C_{F_4}(w)
\cong
\frac{SU(3)\times SU(3)}{\mathbb Z_3}.
\tag{OT3}
$$

The centralizer \(K\) is connected. [[library/standard-model-from-exceptional-jordan-algebra/inq|Baez and Schwahn]] identify the same group as \(\operatorname{Stab}_{F_4}(B)_0\). Thus the connected symmetry of the complex subalgebra is already the centralizer of a prior oriented operation:

$$
\boxed{
\operatorname{Stab}_{F_4}(B)_0=C_{F_4}(w).}
\tag{OT4}
$$

This is stronger than attaching an abstract sign to \(B\). The orientation-bearing datum is an automorphism of the whole algebra.

## Averaging is the exact forgetting map

Since automorphisms preserve the trace metric, \(w^*=w^{-1}=w^2\). The orthogonal projection onto the fixed algebra is the cyclic average

$$
\boxed{
P_B=\frac{1+w+w^2}{3}.}
\tag{OT5}
$$

The part lost by this average still contains a signed first-order structure. Define

$$
q_B:=1-P_B,
\qquad
I_B:=\frac{w-w^2}{\sqrt3}.
\tag{OT6}
$$

Direct polynomial calculation gives

$$
I_B^*=-I_B,
\qquad
I_B^2=-q_B,
\qquad
P_BI_B=0.
\tag{OT7}
$$

Thus \(I_B\) is a canonical orthogonal complex structure on the forgotten real space \(B^\perp\). If \(\kappa\) belongs to the antiunitary component of \(\operatorname{Stab}(B)\), then

$$
\kappa w\kappa^{-1}=w^2,
\qquad
\kappa I_B\kappa^{-1}=-I_B,
\qquad
P_B(w^2)=P_B(w).
\tag{OT8}
$$

Consequently

$$
\boxed{
w\ \text{or}\ w^{-1}
\longmapsto
\frac{1+w+w^2}{3}=P_B}
\tag{OT9}
$$

is a literal two-to-one loss of orientation at fixed \(B\). The retained unoriented fixed-algebra datum does not contain enough information to reconstruct which cyclic direction supplied it.

There is also an honest orientation form. On \(B^\perp\), put

$$
\varpi_B(u,v):=\langle I_Bu,v\rangle,
\qquad
\Omega_{B^\perp}:=\frac1{9!}\varpi_B^{\wedge9}.
\tag{OT10}
$$

Because \((B^\perp,I_B)\) has complex dimension nine,

$$
\Omega_{B^\perp}(w^2)=-\Omega_{B^\perp}(w).
\tag{OT11}
$$

No preferred sheet follows from \(B\), the real Jordan product, and the trace metric alone: the antiunitary symmetry preserves those data and exchanges the two sheets. What is canonical is the orientation double cover and its odd residue, not the declaration that one sheet must be actual.

## The Standard Model group is the flag's isotropy

Choose

$$
\ell\in\operatorname{Fix}(w),
\qquad
\ell\circ\ell=\ell,
\qquad
\operatorname{tr}\ell=2.
\tag{OT12}
$$

The nested complex flag is recovered without another independent subspace variable:

$$
B=\operatorname{Fix}(w),
\qquad
X=E_1^B(\ell)
=\{x\in B:\ell\circ x=x\}.
\tag{OT13}
$$

The projections are polynomial in the prior data:

$$
\boxed{
P_B=\frac{1+w+w^2}{3},
\qquad
P_X=P_B\bigl(2L_\ell^2-L_\ell\bigr).}
\tag{OT14}
$$

Indeed, \(w\ell=\ell\) makes \(P_B\) commute with \(L_\ell\), while \(2L_\ell^2-L_\ell\) is the Peirce projector onto the eigenvalue-one space of \(L_\ell\).

The exact isotropy is

$$
\boxed{
\operatorname{Stab}_{F_4}(\ell,w)
=C_{F_4}(w)\cap\operatorname{Stab}_{F_4}(\ell)
\cong
S(U(2)\times U(3))
\cong
\frac{U(1)\times SU(2)\times SU(3)}{\mathbb Z_6}.}
\tag{OT15}
$$

This is the Copernican reversal in theorem form:

$$
\boxed{
\text{oriented operation }w
+\text{ pointed idempotent }\ell
\longrightarrow
\text{ observed gauge-group stabilizer}.}
\tag{OT16}
$$

The larger \(F_4\) is not being proposed as an ordinary gauge symmetry that must later be dynamically broken. It is the covariance of all presentations of the deeper datum; \(H:=S(U(2)\times U(3))\) is the automorphism group of one pointed presentation.

## The orientation lift is a connected double cover

The orbit of \(w\) is

$$
\mathcal O_w\cong F_4/K,
\qquad
\dim\mathcal O_w=52-16=36.
\tag{OT17}
$$

The full stabilizer of \(B\) has two components, with its second component exchanging \(w\) and \(w^2\). Therefore

$$
F_4/K
\longrightarrow
F_4/\operatorname{Stab}_{F_4}(B)
\tag{OT18}
$$

is the two-sheeted orientation cover of the complex-subalgebra orbit. The total cover is connected: the two orientations over one \(B\) are connected only by moving through other subalgebras, not by an element of the connected stabilizer of that fixed \(B\).

This topology is a precise replacement for the loose phrase “spontaneous choice of sign.” The sign is relative to the forgetful map (OT18).

## Chirality is retained by an orientation lift, not created by a torsor

The octonionic slice has a smaller exact model of the same two-sheeted grammar.
For a unit imaginary octonion \(u\),

$$
\mathbb C_u=\operatorname{span}_{\mathbb R}\{1,u\}
=\mathbb C_{-u},
\tag{OT18a}
$$

but \(u\) and \(-u\) give opposite complex orientations. Hence the space of
oriented slice directions and the space of unoriented complex subalgebras are
related by

$$
\boxed{
S^6\longrightarrow\mathbb RP^6,
\qquad
u\longmapsto\mathbb C_u,
\qquad
\{u,-u\}\longmapsto\mathbb C_u.}
\tag{OT18b}
$$

Put \(K_u:=\operatorname{Stab}_{G_2}(\{u,-u\})\). Since
\(\operatorname{Stab}_{G_2}(u)=\operatorname{Stab}_{G_2}(-u)=SU(3)\), there is an
exact sequence

$$
1\longrightarrow SU(3)\longrightarrow K_u
\longrightarrow\mathbb Z_2\longrightarrow1,
\tag{OT18c}
$$

and the cover (OT18b) is the homogeneous projection

$$
G_2/SU(3)\longrightarrow G_2/K_u.
\tag{OT18d}
$$

This locates the relevant forgetting precisely. A principal \(SU(3)\)-torsor
for a fixed oriented \(u\) forgets which local frame was chosen, but every allowed
frame change is complex-linear and preserves the orientation. Handedness is lost
only by the further functor that enlarges the structure group to \(K_u\), or
equivalently descends along (OT18b).

The associated obstruction has the usual descent form. For a principal
\(K_u\)-bundle \(Q\to X\), the quotient

$$
Q/SU(3)\longrightarrow X
\tag{OT18e}
$$

is a principal \(\mathbb Z_2\)-bundle. A reduction of \(Q\) to \(SU(3)\) is
equivalent to a section of this orientation cover. Local sections differ by a
\(\mathbb Z_2\)-valued Čech cocycle; on an ordinary paracompact base its class in
\(H^1(X;\mathbb Z_2)\) is the obstruction to choosing one handedness globally.
Thus a chiral orientation may be locally definite while failing global descent.
The cocycle records the obstruction; it does not choose which sheet is factual
when the obstruction vanishes.

[[octonionic-clifford-completion-of-the-color-normal]] shows that this cover acts
nontrivially on an exact operator carrier. On
\(\mathcal H_{\mathbb O}=\mathbb O\otimes_{\mathbb R}\mathbb C\), set

$$
\gamma_u=iL_u,
\qquad
P_\pm(u)=\frac{1\pm\gamma_u}{2}.
\tag{OT18f}
$$

Then

$$
\gamma_{-u}=-\gamma_u,
\qquad
P_\pm(-u)=P_\mp(u),
\qquad
J_0\gamma_u=-\gamma_uJ_0,
\tag{OT18g}
$$

and, up to the naming of the two signs,

$$
P_+(u)\mathcal H_{\mathbb O}\cong\mathbf1\oplus\mathbf3,
\qquad
P_-(u)\mathcal H_{\mathbb O}\cong\mathbf1\oplus\bar{\mathbf3}.
\tag{OT18h}
$$

The deck reversal therefore exchanges the two graded color modules, whereas the
unoriented quotient retains only their unordered pair. Even observables such as
the Hilbert--Schmidt Wilson response and the Killing trace form survive this
forgetting; the odd grading operator does not. At the Albert level, cyclic
averaging \(w\) and \(w^2\) to the common projector \(P_B\) has the same typed
effect: the fixed algebra survives while its sign-bearing complex orientation is
discarded.

The no-go is immediate. If an ordinary grading on the unoriented quotient pulled
back to \(\gamma_u\), deck invariance would require
\(\gamma_{-u}=\gamma_u\), while (OT18g) requires
\(\gamma_{-u}=-\gamma_u\). Since \(\gamma_u^2=1\), this is impossible. Before an
orientation lift is chosen, the grading can descend only as an endomorphism
valued in the associated sign line, not as a real-valued invariant of the coarse
quotient. Its square, its unordered eigenspace pair, and the even trace response
do descend.

This is an exact algebraic model of **chirality as a discernible relative to its
reversal**, but it is not yet the observed chiral matter spectrum. The two halves
in (OT18h) have equal dimension, and their
\(\mathbf3/\bar{\mathbf3}\) distinction is color conjugacy rather than the
Standard Model's left/right weak representation asymmetry. A physical theorem
still needs the finite algebra and bimodule, a complete real spectral cycle,
a justified representation-theoretic left/right asymmetry on the independent
fermions, anomaly cancellation, and a coupling to gauge-invariant observables.
A nonzero total Fredholm index is one possible imbalance witness, not a necessary
condition for a real-doubled chiral theory. Pure Yang--Mills contains no fermions
at all. Thus chirality, pointing, and the mass gap can share an
orientation/descent grammar without becoming the same operator or implying one
another.

## A canonical finite oriented-flag Hessian

Let

$$
B_2:=\{b\in B:\operatorname{tr}b=2\}
\tag{OT19}
$$

and form the associated affine bundle

$$
\mathcal E_{\mathrm{or}}
:=F_4\times_KB_2
\longrightarrow F_4/K.
\tag{OT20}
$$

Its dimension is \(36+8=44\). The Jordan product and trace metric define, without relative residual weights,

$$
V([g,b])
:=\frac12\lVert b\circ b-b\rVert^2.
\tag{OT21}
$$

The rank-two idempotents in \(B\cong\mathfrak h_3(\mathbb C)\) form \(\operatorname{Gr}_2(\mathbb C^3)\cong\mathbb CP^2\). Hence

$$
\boxed{
V^{-1}(0)
=F_4\times_K\operatorname{Idem}_2(B)
\cong F_4/H,}
\tag{OT22}
$$

of dimension \(36+4=40\).

At a zero represented by \(\ell\), the base directions contribute thirty-six zero modes. In the eight-dimensional vertical trace slice, the derivative \(2L_\ell-I\) vanishes on the four-dimensional Peirce space \(B_{1/2}(\ell)\), tangent to \(\mathbb CP^2\), and is an isometry on

$$
N_{\mathrm{int}}
=\bigl(B_1(\ell)\oplus B_0(\ell)\bigr)
\cap\ker\operatorname{tr},
\qquad
\dim_{\mathbb R}N_{\mathrm{int}}=4.
\tag{OT23}
$$

Therefore

$$
\boxed{
\operatorname{Spec}\bigl(\operatorname{Hess}V\bigr)
=\{0^{(40)},1^{(4)}\}.}
\tag{OT24}
$$

Unlike an arbitrary squared-distance potential, (OT21) is supplied by the Jordan multiplication itself. Unlike the larger redundant constraint package in [[jordan-idempotency-and-the-stabilizer-gap]], it also has a canonical nonzero spectrum once the trace metric is fixed.

There is an immediate limitation. Under

$$
H\cong
\frac{SU(2)\times U(1)\times SU(3)_{\mathrm c}}{\mathbb Z_6},
\tag{OT25}
$$

the complexified intrinsic normal is

$$
(N_{\mathrm{int}})_{\mathbb C}
\cong
(\mathbf3,\mathbf1)_0\oplus(\mathbf1,\mathbf1)_0.
\tag{OT26}
$$

The color and \(U(1)\) factors act trivially. The clean four-dimensional normal gap therefore cannot by itself supply a faithful response for the surviving gauge group.

## A flat constraint package exists, but its domain matters

The same datum can be described in the flat space \(J\oplus\operatorname{End}_{\mathbb R}(J)\) by the residuals

$$
\begin{aligned}
w\,m-m(w\otimes w)&=0,
&w^3-1&=0,
&\operatorname{Tr}_{\operatorname{End}J}w&=0,
\\
w\ell-\ell&=0,
&\ell\circ\ell-\ell&=0,
&\operatorname{tr}\ell-2&=0,
\end{aligned}
\tag{OT27}
$$

where \(m(x,y)=x\circ y\). For a real order-three operator on a twenty-seven-dimensional space, the trace-zero equation forces complexified multiplicities \(9,9,9\) for \(1,\omega,\bar\omega\). Globally, (OT27) should still be restricted to Yokota's conjugacy-class component until all other order-three automorphism classes satisfying the same equations have been excluded.

The reduced bundle (OT20) bakes precisely that conjugacy class into the domain. This is mathematically clean, but it is also a warning: a normal spectrum depends on which deformations have been admitted as meaningful. The zero locus alone does not determine its ambient response carrier.

## What has actually been explained

The construction proves three finite statements that the symmetry-first formulation leaves unrelated:

1. **Symmetry:** \(H\) is the stabilizer of \((\ell,w)\), not primordial input.
2. **Asymmetry:** \(I_B\) and \(\Omega_{B^\perp}\) are odd under the antiunitary exchange \(w\leftrightarrow w^2\).
3. **Positive response:** the even squared idempotency defect has the exact normal edge (OT24).

It does not identify those three structures. In particular,

$$
\boxed{
\text{oriented-flag normal edge}
\not\Rightarrow
\text{Yang--Mills mass edge}.}
\tag{OT28}
$$

The Hessian charges leaving the valid flag locus. A surviving \(H\)-connection can transport the flag while preserving it pointwise, so its curvature is invisible to the intrinsic four-dimensional normal (OT23). A physical construction must make the prior datum into a field, charge its holonomy or another faithful retained response, realize that form on the gauge-invariant OS carrier, and prove a regulator-uniform comparison with the Hamiltonian or Poincare Casimir. Only after that comparison may an independent dimensional yardstick turn the dimensionless response into mass.

[[contemporary-puzzles/yang-mills-mass-gap/receipts/exceptional_normal_holonomy_receipt.py|The shared exceptional-normal receipt]] verifies the dimension and multiplicity ledger behind (OT24). Yokota's automorphism and centralizer and Baez--Schwahn's stabilizer remain cited theorem inputs.
