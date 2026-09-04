# Retract Corners and Local Unitarity

A noninvertible whole-to-local retraction can carry a perfectly invertible local symmetry without contradiction. If a local object \(L\) is a retract of a whole object \(W\), the split idempotent \(e=hq\) identifies \(\operatorname{End}(L)\) with the corner \(e\operatorname{End}(W)e\). A local unitary is a unit of that corner, whose identity is \(e\), even though its whole-carrier representative kills every direction forgotten by \(q\) and cannot be invertible in \(\operatorname{End}(W)\). This is an exact algebraic model of asymmetry preceding the observed grammar of symmetry; it does not by itself select a Hilbert metric, clock, factual event, or mass gap.

**Status: [EXACT] for the split-idempotent and corner-isomorphism theorems; [EXACT UNDER STATED METRIC HYPOTHESES] for the partial-unitary realization; [INTERPRETATION] for noninvertible descent preceding local symmetry; [OPEN] for the physical whole, local carrier, section, and clock action.**

## A local object as a retract

Work first in complex vector spaces. Let

$$
W\mathop{\longrightarrow}^{q}L
\mathop{\longrightarrow}^{h}W,
\qquad
qh=I_L.
\tag{RC1}
$$

Thus \(q\) is a split epimorphism, \(h\) is a section, and

$$
e:=hq\in\operatorname{End}(W)
\tag{RC2}
$$

is idempotent:

$$
e^2=h(qh)q=hq=e.
\tag{RC3}
$$

The decomposition is

$$
W=\operatorname{im}h\oplus\ker q,
\qquad
e|_{\operatorname{im}h}=I,
\qquad
e|_{\ker q}=0.
\tag{RC4}
$$

The word *whole* is only a role in this theorem. It does not mean a set of hidden particles, a global Hilbert space, or an environment. Likewise, the section \(h\) is extra structure. A quotient map does not canonically choose representatives.

## The corner theorem

The corner cut out by \(e\) is

$$
e\operatorname{End}(W)e
:=
\{A\in\operatorname{End}(W):eA=A=Ae\}.
\tag{RC5}
$$

It is an algebra whose multiplicative identity is \(e\), not \(I_W\). Define

$$
\Phi:\operatorname{End}(L)\longrightarrow e\operatorname{End}(W)e,
\qquad
\Phi(a)=haq,
\tag{RC6}
$$

and

$$
\Psi:e\operatorname{End}(W)e\longrightarrow\operatorname{End}(L),
\qquad
\Psi(A)=qAh.
\tag{RC7}
$$

Then

$$
\Psi\Phi(a)=qhaqh=a,
\qquad
\Phi\Psi(A)=hqAhq=eAe=A.
\tag{RC8}
$$

Both maps preserve composition. Hence

$$
\boxed{
\operatorname{End}(L)
\cong
e\operatorname{End}(W)e.}
\tag{RC9}
$$

This is the elementary split-idempotent, or Karoubi-corner, theorem. It applies in any category in which the corresponding endomorphism objects and split idempotent make sense; the vector-space proof displays all of the typing.

If \(u\in\operatorname{GL}(L)\), put

$$
\widetilde u:=huq.
\tag{RC10}
$$

Then

$$
\widetilde u\,\widetilde{u^{-1}}
=
\widetilde{u^{-1}}\,\widetilde u
=e.
\tag{RC11}
$$

Thus \(\widetilde u\) is invertible **in the corner**. If \(\ker q\neq0\), however,

$$
\ker q\subseteq\ker\widetilde u,
\tag{RC12}
$$

so \(\widetilde u\) is not invertible in \(\operatorname{End}(W)\). The apparent paradox comes only from silently changing the identity operator:

$$
\boxed{
\text{whole identity }I_W
\neq
\text{retained identity }e.}
\tag{RC13}
$$

An observed group of invertible transformations may therefore be derived after a prior asymmetric choice of retract. One should ask for the automorphisms of the retained object—or equivalently the units of its corner—rather than demand that the same maps be automorphisms of the whole object.

## Local unitaries are whole-carrier partial unitaries

Now let \(W\) and \(L\) be Hilbert spaces, let \(h:L\to W\) be an isometry, and take \(q=h^*\). Then \(qh=I_L\) and

$$
e=hh^*
\tag{RC14}
$$

is the orthogonal projection onto \(hL\). The corner is a \(C^*\)-corner, and (RC9) becomes a unital \(*\)-isomorphism when the corner's unit is understood to be \(e\):

$$
B(L)\cong eB(W)e.
\tag{RC15}
$$

For \(U\in\mathcal U(L)\),

$$
\widetilde U=hUh^*,
\qquad
\widetilde U^*\widetilde U
=
\widetilde U\widetilde U^*
=e.
\tag{RC16}
$$

Therefore \(\widetilde U\) is a unitary in \(eB(W)e\) and a partial unitary on \(W\). It is a whole-space unitary only when \(e=I_W\), equivalently when nothing is discarded.

This statement is stronger and cleaner than saying vaguely that “the whole is nonunitary.” Unitarity is always relative to an inner product, a carrier, and its identity. The exact statement is:

> The local clock may be unitary in the retained corner even though its canonical whole-carrier representative is noninvertible relative to the whole identity.

No claim has yet been made that \(U_t\) is physical time. A strongly continuous one-parameter group, an invariant physical state, and a clock calibration are still required.

## Harmonic sections make the idempotent a descent operator

[[trace-dirichlet-descent/inq|Trace Dirichlet descent]] owns the analytic
construction and its domain hypotheses. When its whole form admits a linear
harmonic section \(h\), the idempotent \(e=hq\) selects the least-cost
representative of each local class and gives the exact decomposition

$$
\mathcal E[w]
=
\check{\mathcal E}[qw]
+
\mathcal E[(I-e)w].
\tag{RC17}
$$

Consequently, if \(U\) preserves the local trace form, its corner
representative obeys

$$
\mathcal E[hUqw]
=
\check{\mathcal E}[qw]
\leq
\mathcal E[w].
\tag{RC18}
$$

The difference is the vertical term in (RC17), independent of \(U\), and
vanishes on the harmonic image. Thus

$$
\boxed{
\text{forget the vertical representative and retain its harmonic class}
\quad\Longrightarrow\quad
\text{act reversibly inside the retained corner}.}
\tag{RC19}
$$

The implication is structural, not causal. The idempotent makes the local group action well typed; it does not select which group or one-parameter subgroup nature uses.

When the pushed form is closed and Markovian in the appropriately ordered
carrier, the trace theorem additionally derives a local
Dirichlet-to-Neumann process. That process is not part of the elementary
corner theorem.

## What the theorem does not identify

Four arrows remain distinct:

$$
q:W\to L,
\qquad
e=hq:W\to W,
\qquad
U_t:L\to L,
\qquad
e^{-sD}:L\to L.
\tag{RC24}
$$

- \(q\) forgets which whole representative was present.
- \(e\) chooses the harmonic representative of a local class.
- \(U_t\) is an invertible local transformation and becomes clock evolution only after physical reconstruction.
- \(e^{-sD}\) is a contraction process generated by a positive response and need not be invertible as a positive process.

The corner theorem permits these arrows to coexist. It does not prove that the retraction actualizes an outcome, that the discarded directions are ontologically real, that \(D\) equals a Hamiltonian, or that a positive edge of \(D\) is a Yang--Mills mass gap. Those claims require the carrier, record, energy, continuum, and Poincare constructions stated elsewhere.
