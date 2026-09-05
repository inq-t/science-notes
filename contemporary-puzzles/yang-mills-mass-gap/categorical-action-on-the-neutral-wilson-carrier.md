# Categorical Action on the Neutral Wilson Carrier

The first direct attempt to make quantum-\(G_2\) rigidity operate on Yang--Mills states can now be decided. On a finite Wilson carrier, insertion of the restricted fundamental character is exactly fusion by \(\mathbf1\oplus\mathbf3\oplus\bar{\mathbf3}\); at classical normalization there is no normalizable invariant GNS vector, only a formal distributional \(1\)-eigenstate or evaluation functional at the flat connection, and the vacuum-compressed edge is zero. Dividing instead by the quantum dimension \(\delta_q>7\) creates a positive floor, but that floor is only a scalar offset: it cancels from normalized Gibbs laws and from excitation-energy differences, while the remaining term is an ordinary Wilson coupling reparameterization. Canonical Type-III hypergroup actions fail in the opposite direction because their maps fix the entire smaller observable algebra pointwise. The same-carrier target surviving these audits is therefore a family of vacuum-ergodic, state-preserving UCP maps satisfying the normalized fusion law, whose GNS fusion representation is tube admissible, whose joint invariant space is exactly the physical vacuum, and whose selected non-scalar defect is dominated by a regional relative-entropy response. The stronger wall reading additionally asks that a genuine restriction-loss form dominate the same defect; that does not follow from data processing alone.

**Status: [EXACT] for the one-loop fusion/multiplication identity, classical no-edge theorem, quantum-normalization decomposition, Gibbs and Hamiltonian centering no-go, and the Type-III fixed-carrier firewall under their stated hypotheses; [STANDARD] for abstract annular and Type-III realizability of rigid \(C^*\)-tensor categories; [EXACT CONDITIONAL] for the normalized fusion-action theorem and its entropy--energy consequence; [OPEN] for constructing that action from Yang--Mills or the proposed global-to-local descent, proving tube admissibility and vacuum ergodicity, and carrying it uniformly through continuum and Poincare reconstruction.**

The distinction among the algebra action, its GNS contraction, and the BKM
state-tangent loss is developed once in
[[measured-response-carriers/inq|the measured-response carrier stack]]. This
note uses that stack rather than identifying categorical disagreement with
statistical forgetting or energy.

## The smallest honest carrier test

Take the one-cycle gauge carrier

\[
\mathcal H_{\mathrm{cyc}}
:=
L^2(SU(3),\mu_{\mathrm H})^{\operatorname{Ad}SU(3)}.
\tag{CW1}
\]

Its orthonormal Peter--Weyl basis consists of irreducible characters
\(\{\chi_\lambda\}_{\lambda\in\widehat{SU(3)}}\). If

\[
R:=\mathbf1\oplus\mathbf3\oplus\bar{\mathbf3},
\qquad
W(U):=\chi_R(U)
=1+2\operatorname{Re}\operatorname{tr}_{\mathbf3}U,
\tag{CW2}
\]

then

\[
M_W\chi_\lambda
=
\chi_R\chi_\lambda
=
\sum_\sigma N_{R\lambda}^{\ \ \sigma}\chi_\sigma.
\tag{CW3}
\]

Thus character multiplication is not merely analogous to fusion: on this
carrier it **is** the regular fusion adjacency operator for the restricted
object \(R\). On a general graph, multiplication by \(W\) of the holonomy
around a closed loop performs the same label fusion along that loop in the
spin-network basis.

At generic positive \(q\), the type-1 \(U_q(\mathfrak g_2)\) category has the
classical \(G_2\) based fusion ring. Choose the standard based-ring
identification \(K_0(\mathcal C_q)\cong R(G_2)\), compose it with classical
restriction \(R(G_2)\to R(SU(3))\), and then use the
character-multiplication representation. The fundamental class \(X\) maps
to \(R\), giving an algebraic fusion-\(*\)-representation with

\[
[X]\longmapsto M_W.
\tag{CW4}
\]

This ring-level statement does **not** show annular admissibility. By
[[library/annular-representation-theory-for-rigid-c-star-tensor-categories/inq|Ghosh and Jones]],
Popa--Vaes admissibility requires this fusion representation to be unitarily
equivalent to the weight-zero restriction of a nondegenerate representation
of a full annular algebra, generally acting on a larger graded Hilbert space.
No such extension has been constructed here.

## The Haar carrier has the wrong invariant

Since

\[
W(e)=7,
\qquad
W(U)\leq7,
\tag{CW5}
\]

the classical normalized fusion operator is

\[
A_1:=M_{W/7},
\qquad
L_1:=I-A_1\geq0.
\tag{CW6}
\]

It does not preserve the Haar vacuum:

\[
A_1\mathbf1=W/7\neq\mathbf1.
\tag{CW7}
\]

The formal invariant is instead evaluation at the identity. Distributionally,

\[
\delta_e
=
\sum_{\lambda\in\widehat{SU(3)}}
d_\lambda\chi_\lambda,
\qquad
A_1\delta_e=\delta_e.
\tag{CW8}
\]

But \(\delta_e\notin L^2(SU(3),\mu_{\mathrm H})\). Equivalently,
\(W(U)=7\) only at \(e\), a Haar-null set, so \(1\) is not an \(L^2\)
eigenvalue of \(A_1\). This is the flat or BF presentation of the vacuum,
not the ordinary continuous-Haar vacuum. The distinction is structural:
[[library/fusion-basis-for-lattice-gauge-theory-and-loop-quantum-gravity/inq|Delcamp, Dittrich, and Riello]]
note that for a Lie group the BF vacuum requires a discrete topology and
measure to have finite norm.

There is also no hidden edge after merely deleting any proposed vacuum line.

**Classical character-multiplication no-edge theorem.** Let
\(\Omega\in\mathcal H_{\mathrm{cyc}}\) be any unit vector. Then

\[
\boxed{
\inf_{\substack{f\perp\Omega\\\|f\|=1}}
\langle f,L_1f\rangle=0.}
\tag{CW9}
\]

**Proof.** For every \(\varepsilon>0\), continuity and (CW5) give a
conjugation-invariant neighborhood

\[
\mathcal U_\varepsilon
:=
\{U:1-W(U)/7<\varepsilon\}
\tag{CW10}
\]

of the identity with positive Haar measure. The class-function subspace
supported in \(\mathcal U_\varepsilon\) is infinite-dimensional, so it
contains a unit vector \(f_\varepsilon\perp\Omega\). Since \(L_1\) is
multiplication by \(1-W/7\),

\[
0\leq
\langle f_\varepsilon,L_1f_\varepsilon\rangle
<\varepsilon.
\]

Letting \(\varepsilon\downarrow0\) proves (CW9). \(\square\)

The same proof applies to a gauge-invariant loop coordinate on a finite graph
whenever the continuous-Haar quotient contains arbitrarily small positive-
measure neighborhoods of trivial loop holonomy. It is the character version
of the plaquette-multiplier no-go in
[[exceptional-wilson-same-carrier-factorization]].

## Quantum normalization opens only an absolute offset

For the fundamental quantum-\(G_2\) object,

\[
\delta_q
:=d_q(X)
=1+2\cosh(2\eta)+2\cosh(8\eta)+2\cosh(10\eta),
\qquad
\eta=\log q.
\tag{CW11}
\]

Hence

\[
\delta_q>7
\quad\Longleftrightarrow\quad
q\neq1.
\tag{CW12}
\]

If the categorical normalization is applied to the classical branching
operator (CW4), one obtains

\[
A_q:=\frac1{\delta_q}M_W,
\qquad
L_q^{\mathrm{br}}:=I-A_q.
\tag{CW13}
\]

Pointwise,

\[
L_q^{\mathrm{br}}
\geq
\left(1-\frac7{\delta_q}\right)I.
\tag{CW14}
\]

This looks like the desired dimensionless gap. The exact decomposition shows
what kind of number it is. With

\[
Q_W(U):=1-\frac13\operatorname{Re}\operatorname{tr}_{\mathbf3}U,
\tag{CW15}
\]

one has

\[
\boxed{
L_q^{\mathrm{br}}
=
\frac{\delta_q-7}{\delta_q}I
+
\frac6{\delta_q}M_{Q_W}
=
\frac{\delta_q-7}{\delta_q}I
+
\frac7{\delta_q}L_1.}
\tag{CW16}
\]

The entire new lower floor is the first, scalar term. Subtracting the spectral
bottom leaves

\[
L_q^{\mathrm{br}}
-
\frac{\delta_q-7}{\delta_q}I
=
\frac7{\delta_q}L_1,
\tag{CW17}
\]

whose lower edge is zero by (CW9).

This is not merely a choice of words about zero energy. Let \(N_p\) plaquettes
carry this multiplier and put

\[
F_q(U):=\sum_p
\left(1-\frac{W(U_p)}{\delta_q}\right).
\tag{CW18}
\]

Then

\[
F_q
=
N_p\frac{\delta_q-7}{\delta_q}
+
\frac6{\delta_q}Q_W^{\mathrm{tot}}.
\tag{CW19}
\]

For every finite regulator, the normalized Gibbs law therefore satisfies

\[
\frac{e^{-\beta F_q}\,\mathrm d\mu_{\mathrm H}}
{\int e^{-\beta F_q}\,\mathrm d\mu_{\mathrm H}}
=
\frac{e^{-(6\beta/\delta_q)Q_W^{\mathrm{tot}}}\,\mathrm d\mu_{\mathrm H}}
{\int e^{-(6\beta/\delta_q)Q_W^{\mathrm{tot}}}\,\mathrm d\mu_{\mathrm H}}.
\tag{CW20}
\]

The scalar floor cancels exactly. The remaining \(q\)-dependence is a
redefinition of the ordinary Wilson coupling.

Likewise, for any kinetic operator \(T\),

\[
H_q:=T+gF_q
=
\left(T+\frac{6g}{\delta_q}Q_W^{\mathrm{tot}}\right)
+gN_p\frac{\delta_q-7}{\delta_q}I.
\tag{CW21}
\]

The last term translates the entire spectrum and therefore cancels from every
excitation-energy difference. The first term has the same kinetic operator
plus the ordinary Wilson potential with coefficient \(6g/\delta_q\).
Whether that coefficient change is one standard Kogut--Susskind coupling
reparameterization depends on the kinetic normalization. Thus (CW14) is a
positive **absolute offset**, not a relative vacuum gap.

This resolves a subtle normalization fork:

- normalization by \(7\) respects the classical character maximum but gives
  the gapless operator (CW6);
- normalization by \(\delta_q\) matches the quantum categorical dimension but
  does not preserve the continuous-Haar vacuum and creates only the removable
  scalar in (CW16); and
- adjoining a separate trivial representation for the vacuum by hand makes a
  block-diagonal gap, but it inserts the physical vacuum projection instead of
  deriving it.

Quantum-\(G_2\) property \((T)\) remains a real theorem. What fails is the
claim that its Kazhdan projection has thereby been realized as the Yang--Mills
vacuum projection.

## The canonical Type-III action is blind in the opposite direction

There is a rigorous same-Hilbert-space construction close to the proposed
global/local picture. Let

\[
\mathcal N\subset\mathcal M
\tag{CW22}
\]

be an irreducible local discrete Type-III subfactor with a standard vector
\(\Omega\) whose state is invariant under the canonical expectation.
[[library/compact-hypergroups-from-discrete-subfactors/inq|Bischoff, Del Vecchio, and Giorgetti]]
construct a canonical compact hypergroup of normal \(\mathcal N\)-bimodular
unital completely positive maps \(\phi:\mathcal M\to\mathcal M\). Each map
has the actual standard-space implementation

\[
V_\phi(m\Omega):=\phi(m)\Omega,
\qquad
\|V_\phi\|\leq1.
\tag{CW23}
\]

Every map fixes \(\mathcal N\) pointwise, while the joint fixed-point algebra
of the full hypergroup action is \(\mathcal N\). Consequently

\[
V_\phi(n\Omega)=n\Omega
\quad
(n\in\mathcal N),
\tag{CW24}
\]

and the Haar-averaged implementation is the expectation projection onto
\(\overline{\mathcal N\Omega}\). Any defect assembled directly from these
maps therefore has

\[
\overline{\mathcal N\Omega}
\subseteq
\ker(I-V_\phi).
\tag{CW25}
\]

If \(\mathcal N\) is the neutral observable subnet, this retained subspace
contains its vacuum-sector excitations as well as \(\Omega\). The action is
on the correct ambient standard Hilbert space but is blind to the very neutral
directions that the mass-gap theorem must control.

This is the mirror image of the Wilson failure:

\[
\begin{array}{c|c|c}
\text{construction}&\text{carrier}&\text{fixed space}\\
\hline
\text{Wilson character multiplication}&\text{physical regulator carrier}
&\text{no nonzero }L^2\text{ fixed vector; formal }\delta_e\\
\text{Type-III fixed-point hypergroup}&\text{standard GNS carrier}
&\overline{\mathcal N\Omega},\text{ too large}\\
\text{categorical Kazhdan operator}&\text{annular/tube module}
&\text{correct abstract trivial presentation}
\end{array}
\tag{CW26}
\]

## Abstract Type-III realizability is not the missing identification

The categorical side itself has no Type-III obstruction.
[[library/realization-of-rigid-c-star-tensor-categories-via-tomita-bimodules/inq|Giorgetti and Yuan]]
prove that an arbitrary small rigid \(C^*\)-tensor category with simple unit
can be realized on Type II or Type \(\mathrm{III}_\lambda\) factors and, for
infinite spectrum, give a fully faithful unitary tensor functor

\[
\mathcal C
\hookrightarrow
\operatorname{End}_0(M_{\mathcal C})
\tag{CW27}
\]

into finite-index endomorphisms of a constructed factor
\(M_{\mathcal C}\). In particular, a quantum-\(G_2\) category can live on a
Type-III factor.

The construction uses a synthetic Fock/free-product factor, and its type is
tuned by auxiliary Tomita data. It does not produce the Yang--Mills local net,
vacuum state, translations, Wilson regulator, or regional restriction map.
An action on **some** Type-III factor is therefore an existence prototype,
not a physical realization theorem. The internal \(W^*\)-algebra, GNS, and
completely-positive-map language developed by
[[library/operator-algebras-in-rigid-c-star-tensor-categories/inq|Jones and Penneys]]
is the right grammar for formulating the missing object, but grammar alone
does not select it.

## The same-carrier construction surviving these audits

The arbitrary analysis map in
[[quantum-g2-categorical-rigidity-and-the-carrier-firewall]] can now be
replaced by a sharper target. Let \((\mathcal A_B,\omega_B)\) be a regional
gauge-invariant observable algebra with faithful standard GNS data
\((\mathcal H_B,\Omega_B)\). Assume that \(\omega_B\) is the restriction of
the physical Yang--Mills vacuum and that this GNS representation is
unitarily identified with the intended neutral physical vacuum carrier, with
\(\Omega_B\) its unique ground vector. All later energy inequalities are
understood on one declared complex core in
\(\operatorname{Dom}(H_{\mathrm{YM}}^{1/2})\), where
\(H_{\mathrm{YM}}\) means the vacuum-subtracted generator \(H-E_0\).

A **normalized fusion action by measured operations** of a rigid category
\(\mathcal C_q\) consists, at minimum, of normal unital completely positive
maps

\[
\Phi_\alpha:\mathcal A_B\to\mathcal A_B,
\qquad
\alpha\in\operatorname{Irr}(\mathcal C_q),
\tag{CW28}
\]

which preserve \(\omega_B\), admit \(\omega_B\)-adjoints, and obey

\[
\begin{aligned}
\Phi_{\mathbf1}&=\operatorname{id},\\
\Phi_{\bar\alpha}&=\Phi_\alpha^\sharp,\\
\Phi_\alpha\Phi_\beta
&=
\sum_\gamma
\frac{N_{\alpha\beta}^{\ \ \gamma}d_q(\gamma)}
{d_q(\alpha)d_q(\beta)}
\Phi_\gamma.
\end{aligned}
\tag{CW29}
\]

Here \(\sharp\) is the GNS adjoint condition

\[
\omega_B\!\left(a^*\Phi_\alpha(b)\right)
=
\omega_B\!\left(\Phi_{\bar\alpha}(a)^*b\right),
\tag{CW29a}
\]

so existence of the normal UCP adjoint is a substantive nontracial
hypothesis.

The coefficients in the last line are nonnegative and sum to one because
\(d_q\) is a fusion character. Let \(V_\alpha\) be the GNS contraction

\[
V_\alpha(a\Omega_B):=\Phi_\alpha(a)\Omega_B.
\tag{CW30}
\]

Then

\[
\Theta([\alpha]):=d_q(\alpha)V_\alpha
\tag{CW31}
\]

is an algebraic \(*\)-representation of the fusion algebra. The load-bearing
additional requirement is **tube admissibility**: \(\Theta\) must be
unitarily equivalent to the weight-zero restriction of a nondegenerate full
annular or tube-algebra representation, possibly on a larger graded Hilbert
space. This is not a consequence of (CW29).

Require also the Hilbert-space ergodicity condition

\[
\mathcal H_B^{\mathrm{inv}}
:=
\{\xi:V_\alpha\xi=\xi\ \text{for every }\alpha\}
=
\mathbb C\Omega_B.
\tag{CW32}
\]

This condition rules out both failures above: the invariant is normalizable,
and no nonvacuum neutral subspace is fixed pointwise.

**Same-carrier categorical-edge theorem.** Suppose (CW28)--(CW32) hold for
the quantum-\(G_2\) category at \(q>0,\ q\neq1\). Choose a finite symmetric
tensor-generating set
\(S\subset\operatorname{Irr}(\mathcal C_q)\setminus\{\mathbf1\}\) and
symmetric positive weights \(\nu\), let
\(h_{S,\nu}\) be the normalized categorical average defined in
[[quantum-g2-categorical-rigidity-and-the-carrier-firewall#The universal categorical averaging operator|the
categorical-rigidity theorem]], and put

\[
\begin{aligned}
\Phi_{\mathrm K}
&:=
\frac1{Z_{S,\nu}}
\sum_{\alpha\in S}\nu(\alpha)d_q(\alpha)\Phi_\alpha,\\
V_{\mathrm K}
&:=V_{\Phi_{\mathrm K}}=\Theta(h_{S,\nu}),
\qquad
\kappa_{q,S,\nu}:=\kappa_{S,\nu}>0.
\end{aligned}
\]

The coefficients in \(\Phi_{\mathrm K}\) are positive and sum to one, so it
is again a state-preserving UCP map. Symmetry of \(S\) and \(\nu\), together
with (CW29a), makes it GNS symmetric.

Then categorical property \((T)\) gives

\[
\boxed{
I-V_{\mathrm K}
\geq
\kappa_{q,S,\nu}(I-P_{\Omega_B}).}
\tag{CW33}
\]

**Proof.** Tube admissibility permits application of the universal
categorical Kazhdan estimate to the represented averaging element. Equation
(CW32) identifies the represented Kazhdan projection with
\(P_{\Omega_B}\). \(\square\)

For a self-conjugate fundamental generator \(X=\bar X\), (CW29)--(CW31) make
\(V_X\) self-adjoint. Replacing \(V_{\mathrm K}\) by \(V_X\) in (CW33) is
valid only after declaring \(S=\{X\}\) to be symmetric and tensor-generating
and invoking the corresponding universal estimate
\(\kappa_{q,\{X\},\nu}>0\). Property \((T)\) does not turn every arbitrarily
chosen fusion generator into the relevant Kazhdan average.

There is now an exact arbitrary-von-Neumann-algebra upgrade of this edge.
Poissonize the categorical average,

\[
\mathsf P_t
:=
e^{-t}\sum_{n=0}^{\infty}
\frac{t^n}{n!}\Phi_{\mathrm K}^{\,n}.
\tag{CW33p}
\]

It is a normal \(\omega_B\)-preserving quantum Markov semigroup whose GNS
implementation is \(e^{-t(I-V_{\mathrm K})}\). Hence (CW33) is a GNS
Markov gap. [[library/the-kms-and-gns-spectral-gap-of-quantum-markov-semigroups/inq|Wirth's operator-monotone gap theorem]]
then gives at least the same decay rate in every normalized
operator-monotone observable norm, including the observable BKM norm. This
removes an ad hoc GNS-to-observable-BKM comparison even in type III. It does
not prove (CW33c): the inverse BKM metric on state tangents is the dual
carrier and still requires the score intertwiner and physical range. Nor
does Poissonization turn the Markov parameter into clock time. The group
benchmark and its exact constants are isolated in
[[kazhdan-markov-process-carrier]].

The edge still has no clock built into it. Although \(V_{\mathrm K}\) is a
self-adjoint contraction, it need not be positive and therefore need not be
one Euclidean transfer step. Its canonical lazification

\[
\Lambda_{\mathrm K}:=\frac{\operatorname{id}+\Phi_{\mathrm K}}2,
\qquad
B_{\mathrm K}:=V_{\Lambda_{\mathrm K}}
=\frac{I+V_{\mathrm K}}2.
\]

does obey

\[
0\leq B_{\mathrm K}\leq I,
\qquad
I-B_{\mathrm K}
\geq
\frac{\kappa_{q,S,\nu}}{2}(I-P_{\Omega_B}).
\tag{CW33a}
\]

Only after an independent theorem identifies \(B_{\mathrm K}\) with a physical
Euclidean step of duration \(\tau\) may functional calculus define
\(H_\tau=-(\hbar/\tau)\log B_{\mathrm K}\), provided \(B_{\mathrm K}\) is
injective so that this is a densely defined self-adjoint operator. The
selected operation supplies the integer iteration \(B_{\mathrm K}^n\); it
does not supply \(\tau\), the relation \(t=n\tau\), or energy units. The
entropy--energy comparison below is therefore still essential.

Lazification nevertheless gives one exact candidate for that comparison.
Functional calculus yields

\[
\boxed{
\frac12(I-V_{\mathrm K})
\leq
I-B_{\mathrm K}^2
\leq
I-V_{\mathrm K}.}
\tag{CW33b}
\]

Suppose the regional BKM tangent class has a Hilbert completion
\(\mathcal T_B^{\mathrm{BKM}}\), the lazy channel induces the contraction
\(T_{\mathrm K}Y:=Y\circ\Lambda_{\mathrm K}\) there, and an isometric score map

\[
S_B:\mathcal T_B^{\mathrm{BKM}}\to\mathcal H_{B,\mathbb R}
\]

intertwines \(T_{\mathrm K}\) with \(B_{\mathrm K}\). In the half-Hessian
convention used by the localized entropy form, the channel loss is

\[
q_{\Lambda_{\mathrm K},\omega_B}^{\mathrm{half}}[Y]
=
\frac12
\langle S_BY,(I-B_{\mathrm K}^2)S_BY\rangle_{\mathbb R}
\geq
\frac14
\langle S_BY,(I-V_{\mathrm K})S_BY\rangle_{\mathbb R}.
\tag{CW33c}
\]

In finite faithful dimension, genuine GNS symmetry makes the channel commute
with the modular flow, and the Kubo--Mori coordinate map gives precisely such
an intertwiner. For a Type-III regional algebra the corresponding modular
maps are generally unbounded; a common Tomita core, strong modular
commutation, closability, invariant range, and coverage must therefore be
proved. [[measured-response-carriers/inq#A conditional BKM--GNS bridge|The
shared carrier theorem]] records the exact hypotheses.

If \(J_B\) maps the physical real core into this tangent space, write

\[
q_B[\psi]
:=
\frac12\|J_B\psi\|_{\mathrm{BKM}}^2.
\]

Equation (CW33c) becomes the desired physical comparison only after the
weighted range estimate

\[
\langle S_BJ_B\psi,(I-V_{\mathrm K})S_BJ_B\psi\rangle
\geq
b_D\langle\psi,(I-V_{\mathrm K})\psi\rangle,
\qquad b_D>0.
\tag{CW33d}
\]

Since the full regional half-Hessian dominates the half-Hessian lost under a
channel, (CW33c)--(CW33d) give on the declared **real** tangent core

\[
q_B[\psi]
\geq
q_{\Lambda_{\mathrm K},\omega_B}^{\mathrm{half}}[J_B\psi]
\geq
\frac{b_D}{4}
\langle\psi,(I-V_{\mathrm K})\psi\rangle.
\tag{CW33e}
\]

This is a concrete route from categorical defect to the full regional
relative-entropy response. It is not yet a comparison with a smaller descent
loss: data processing gives
\(0\leq q_{B\to\mathcal N}^{\mathrm{loss}}\leq q_B\), not the reverse
inequality. The stronger wall reading therefore requires the independent
hypothesis

\[
q_{B\to\mathcal N}^{\mathrm{loss}}[\psi]
\geq
b_{\mathrm{loss}}
\langle\psi,(I-V_{\mathrm K})\psi\rangle,
\qquad b_{\mathrm{loss}}>0.
\tag{CW33f}
\]

Neither route yet supplies a positive Hermitian extension from the real
tangent core to the complex energy-form core, nor gives \(B_{\mathrm K}\) a
clock interpretation.

For local-unitary tangents this coverage has an exact first obstruction.
[[localized-relative-entropy-and-the-energy-solder#The local-unitary bridge has a centralizer kernel|The
centralizer-kernel theorem]] identifies the kernel of the regional state
differential with centered vectors generated by the vacuum centralizer. Thus
(CW33d), when asserted for one region, requires every such invisible vector
to lie in \(\ker(I-V_{\mathrm K})\). If the categorical action fixes only the
vacuum, that regional class must have no nonzero centered centralizer
direction. A summed state or regional atlas is different: individual kernels
may remain large, but their pullbacks to one physical source carrier must
have the correct intersection and a uniform relative lower frame.
[[modular-cocycle-tomography/inq|The modular cocycle theorem]] computes the
same-algebra intersection exactly. Reeh--Schlieder density proves neither
the common-source construction nor its quantitative lower bound.

Here the operator finally acts on the intended object: normalizable
gauge-invariant state vectors, or their localized tangent core, rather than
on spacetime points, bare color indices, particle species, or a distributional
flat vacuum.

It is still not an energy operator. Let \(\widehat q_{\mathrm{cmp},B}\) denote
a positive Hermitian extension to a complex energy-form core of either the
full regional Hessian in (CW33e), or a genuine restriction-loss form after
the independent comparison (CW33f) has been proved. Suppose

\[
\widehat q_{\mathrm{cmp},B}[\psi]
\geq
b_{\mathrm{cat}}
\langle\psi,(I-V_{\mathrm K})\psi\rangle,
\qquad
b_{\mathrm{cat}}>0,
\tag{CW34}
\]

Assume additionally the localization, wedge-duality, positive-energy,
differentiability, and energy-form regularity hypotheses stated in
[[localized-relative-entropy-and-the-energy-solder]], and require the same
complex extension to satisfy

\[
\widehat q_{\mathrm{cmp},B}[\psi]
\leq
\frac{2\pi R_B}{\hbar c}
\langle\psi,H_{\mathrm{YM}}\psi\rangle,
\tag{CW35}
\]

then (CW33) implies

\[
\boxed{
H_{\mathrm{YM}}
\geq
\frac{\hbar c}{2\pi R_B}
b_{\mathrm{cat}}\kappa_{q,S,\nu}
(I-P_{\Omega_B})}
\tag{CW36}
\]

as a quadratic-form inequality.

For a regulator family, positivity of the continuum energy edge requires
the dimensional stopping condition

\[
\inf_r
\frac{b_{\mathrm{cat},r}\kappa_{q_r,S_r,\nu_r}}
{R_{B,r}}>0.
\tag{CW36a}
\]

A uniform dimensionless categorical edge can still collapse in energy units
if the selected localization width diverges.

Unlike the earlier \(J_q\)-theorem, this version removes the abstract
analysis-map loss on the chosen GNS carrier. Identification with, and
complete form-core coverage of, the physical neutral Yang--Mills carrier
remain explicit hypotheses. Its difficulty has not disappeared; it has been
concentrated into a falsifiable algebraic object.

## Construction signature and kill conditions

The last implication (CW34)--(CW36) is [[measured-response-carriers/response-to-energy-comparison|the generic response-to-energy comparison]] on the same carrier, with \(J=I\) and \(E_*=\hbar c/(2\pi R_B)\). The categorical averaging edge and the independently proved regional domination remain separate inputs; writing their product does not construct either.

A vacuum-only fixed subspace and a numerical edge are not, by themselves,
diagnostic of mass. Pairs of conditional-expectation projections can be
chosen whose ranges meet only on \(\mathbb C\Omega\) and whose summed defect
has an order-one floor even in systems with no relevant dynamics. Categorical
property \((T)\) makes the edge representation-uniform once the admissible
action has been constructed; it does not make an arbitrary action physical.
The selection of the maps and the comparison (CW34) carry the dynamical
content.

A successful global-to-local construction must now produce all of the
following without consulting the glueball spectrum:

1. the state-preserving fusion law (CW29), not bare multiplication by a Wilson
   class function;
2. extension to a full annular or tube-algebra representation;
3. the vacuum-only invariant condition (CW32) on the complete neutral carrier;
4. a non-scalar centered defect--anything reduced to (CW16) is physically
   absorbed by normalization and coupling conversion;
5. regional naturality and compatibility with gauge reduction, refinement,
   and the proposed whole-to-local descent;
6. the entropy comparison (CW34) on a positive Hermitian complex form core,
   either by extending the full regional response obtained through
   (CW33c)--(CW33e), or by separately proving the stronger restriction-loss
   comparison (CW33f);
7. the dimensional uniformity (CW36a), not merely a uniform product
   \(\kappa_{q,S,\nu} b_{\mathrm{cat}}>0\), together with continuum OS
   reconstruction and the full Poincare-Casimir interpretation; and
8. an internal selector for \(q\) and \(R_B\), with a controlled
   gravity-decoupled pure-Yang--Mills limit.

Five shortcuts are now ruled out:

- **Wilson shortcut:** \(M_{W/7}\) has no normalizable invariant GNS vector,
  only a formal distributional \(1\)-eigenstate or evaluation functional, and
  no positive vacuum-compressed edge.
- **dimension shortcut:** \(M_{W/\delta_q}\) has an apparent floor consisting
  only of a removable scalar plus a Wilson coupling conversion.
- **fixed-point shortcut:** an \(\mathcal N\)-bimodular Type-III action fixes
  \(\overline{\mathcal N\Omega}\), not only the vacuum.
- **vacuum-projection shortcut:** engineering maps whose fixed ranges meet
  only on the vacuum can create a cheap dimensionless floor without supplying
  Yang--Mills dynamics or an energy comparison.
- **clock shortcut:** fusion depth or categorical iteration is an integer
  order parameter, not a physical duration; lazification supplies positivity,
  not the missing \(\tau\).

The Copernican gain is a sharper question. We are no longer asking how the
known local Wilson potential mysteriously manufactures mass. We are asking
whether the global compositional category admits a **measured action on the
neutral observable presentation itself** whose only fully undifferentiated
normal state vector is the vacuum. Property \((T)\) would then make distinction
costly; the regional entropy theorem would convert that cost into local clock
energy; and only the separately derived cosmological or RG yardstick would
set its dimensional presentation.

[[contemporary-puzzles/yang-mills-mass-gap/receipts/fusion_character_centering_receipt.py|The finite receipt]]
and its
[[contemporary-puzzles/yang-mills-mass-gap/receipts/fusion-character-centering-receipt-output.txt|stored output]]
sample (CW16) on an exact one-parameter \(SU(3)\) subgroup and check
normalized-weight cancellation and scalar-shift cancellation. They do not
prove the full functional identities, tube admissibility, construct the
measured action, establish (CW34), or prove a Yang--Mills gap.
