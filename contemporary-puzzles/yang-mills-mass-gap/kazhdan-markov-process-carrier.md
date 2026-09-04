# The Kazhdan--Markov Process Carrier

The reversible automorphisms of a local observable algebra need not exhaust its physically meaningful arrows. Given a state-preserving action of a property-\((T)\) group whose only invariant GNS vectors are the vacuum line, a symmetric Kazhdan average has an exact dimensionless Dirichlet edge on that algebra's own GNS carrier, even when the algebra is type III. This is a conditional same-carrier benchmark for local distinction decay, not yet the whole-to-local wall or a fact-producing collapse. It becomes a Yang--Mills mass gap only after a selected net action, a theorem relating that endoprocess to the realization wall, modular-response coverage, a same-core entropy--energy comparison, regulator-uniformity, and Poincare reconstruction are proved.

**Status: [EXACT, CONDITIONAL ON THE DECLARED ACTION] for the property-\((T)\) Markov construction and its GNS edge; [PRIMARY-SOURCE THEOREM, RECENT PREPRINT] for the GNS-to-observable-BKM gap transfer; [ESTABLISHED PRECEDENT] for coherent UCP operations on chiral conformal nets; [CONDITIONAL] for the response-to-energy implication; [OPEN] for a natural four-dimensional Yang--Mills realization, its relation to a whole-to-local wall, a dimensional selector, and the continuum limit.**

## Enlarge the arrows, not the local predictions

For a von Neumann algebra \(M\), automorphisms form the reversible core of a
larger category of normal unital completely positive maps:

\[
\operatorname{Aut}(M)
\subset
\operatorname{UCP}_{\mathrm n}(M,M).
\tag{KM1}
\]

The distinction is structural. An automorphism preserves products and has an
inverse. A general UCP map need do neither. It may represent a nonselective
measurement, an accessible coarse-graining, a conditional transfer, or a
one-sided process. Which interpretation is physical requires additional
data, but failure to admit an inverse in the UCP process category is already
a precise algebraic predicate.

Let \(\omega\) be a faithful normal state. If \(\Phi\) preserves it, then

\[
V_\Phi(x\Omega_\omega):=\Phi(x)\Omega_\omega
\tag{KM2}
\]

extends to a contraction on \(L^2(M,\omega)\). This is the first reversal:
the contraction carrier of an algebraic process can be constructed before a
physical Hamiltonian is named. A positive Dirichlet defect requires the
additional GNS symmetry imposed below; it must not be obtained by setting
\(V_\Phi=e^{-\tau H/\hbar}\), since that would import the spectrum the
construction is meant to explain.

There is no contradiction in also having a strongly continuous clock group

\[
\alpha_s\in\operatorname{Aut}(M),
\qquad
U_s=e^{-isH/\hbar}
\tag{KM3}
\]

unitarily implemented in the physical representation. Equations (KM2) and
(KM3) describe different arrows. If both belong to one covariant theory, an
intertwining or covariance law must state how they coexist. The phrase “the
whole is not unitary while the local clock is unitary” is meaningful in this
typed sense; unitarity is not a predicate of an unrepresented whole.

Three arrows must therefore remain distinct:

\[
\mathcal C_{\mathrm{whole}}
\xrightarrow{\ \Pi\ }
\mathcal C_{\mathrm{local}},
\qquad
\mathsf P_t^O:\mathcal A(O)\longrightarrow\mathcal A(O),
\qquad
\alpha_s^O\in\operatorname{Aut}(\mathcal A(O)).
\tag{KM3a}
\]

The realization \(\Pi\) changes registers and is nonfaithful if it genuinely
forgets a distinction. The Markov map \(\mathsf P_t^O\) is an endoprocess on
an already declared local algebra. The automorphism \(\alpha_s^O\) is the
candidate reversible clock flow. Before the Markov defect can be called the
wall cost, one must construct \(\Pi\) and prove that its response or residue
factors through the Dirichlet form of \(\mathsf P_t^O\). Merely placing all
three arrows in one diagram does not identify them.

## Exact property-\((T)\) benchmark

Let a discrete group \(\Gamma\) act by \(\omega\)-preserving automorphisms,

\[
\alpha:\Gamma\longrightarrow\operatorname{Aut}(M),
\qquad
\omega\circ\alpha_g=\omega.
\tag{KM4}
\]

Its GNS implementation is the unitary representation

\[
U_g(x\Omega_\omega)=\alpha_g(x)\Omega_\omega.
\tag{KM5}
\]

Choose a finite symmetric generating set \(S=S^{-1}\), a symmetric
probability \(\mu\) with \(\mu(s)>0\) for \(s\in S\), and define

\[
\mathsf T_\mu
:=
\sum_{s\in S}\mu(s)\alpha_s,
\qquad
V_\mu
:=
\sum_{s\in S}\mu(s)U_s.
\tag{KM6}
\]

Then \(\mathsf T_\mu\) is normal, UCP, and \(\omega\)-preserving, while
\(V_\mu\) is a self-adjoint GNS contraction. Put

\[
L_\mu:=I-V_\mu.
\tag{KM7}
\]

The exact Dirichlet identity is

\[
\boxed{
\langle\xi,L_\mu\xi\rangle
=
\frac12\sum_{s\in S}\mu(s)
\|U_s\xi-\xi\|^2.}
\tag{KM8}
\]

Let \((S,\kappa)\) be a Kazhdan pair in the convention

\[
\max_{s\in S}\|U_s\xi-\xi\|
\geq
\kappa\|\xi\|
\qquad
(\xi\perp\mathcal H^\Gamma).
\tag{KM9}
\]

If \(\mu_{\min}:=\min_{s\in S}\mu(s)\), equations (KM8)--(KM9) give

\[
\boxed{
L_\mu
\geq
\lambda_\mu(I-P_\Gamma),
\qquad
\lambda_\mu:=\frac{\mu_{\min}\kappa^2}{2}>0,}
\tag{KM10}
\]

where \(P_\Gamma\) projects onto the invariant GNS vectors. If

\[
\mathcal H^\Gamma=\mathbb C\Omega_\omega,
\tag{KM11}
\]

then (KM10) is a vacuum-only, same-carrier, dimensionless spectral edge.

Poissonization produces an actual quantum Markov semigroup,

\[
\mathsf P_t
:=
e^{-t}
\sum_{n=0}^\infty\frac{t^n}{n!}\mathsf T_\mu^n,
\tag{KM12}
\]

whose GNS implementation is \(e^{-tL_\mu}\). Every \(\mathsf P_t\) is
normal, UCP, and \(\omega\)-preserving. Under (KM10)--(KM11), every
\(t>0\) map is a strict GNS contraction on the vacuum complement and hence
cannot be an automorphism represented unitarily. It is a one-sided semigroup
in the UCP process category, not a unitary group.

There is a precise caveat. Since \(\mathsf T_\mu-I\) is a bounded linear
operator, every finite-\(t\) map

\[
\mathsf P_t=e^{t(\mathsf T_\mu-I)}
\]

has the bounded linear inverse \(e^{-t(\mathsf T_\mu-I)}\). That inverse is
generally not UCP, contractive, or physically admissible. The orientation is
therefore exact inside the positive-process category and in asymptotic
distinction decay; it is not yet noninjective forgetting, outcome selection,
or a factive record. Those stronger meanings require a quotient,
expectation, instrument, asymptotic limit, or separate record map.

Nothing in the proof used a trace or density matrix. The theorem therefore
applies unchanged to a type-III algebra once the state-preserving action is
given. This is a conditional benchmark for the *kind* of carrier being
sought, not an unconditional existence theorem and not a theorem that
Yang--Mills selects \(\Gamma\), \(\alpha\), or \(\mu\).

## The BKM gain, and its exact limit

[[library/the-kms-and-gns-spectral-gap-of-quantum-markov-semigroups/inq|Wirth's 2026 theorem]]
applies to quantum Markov semigroups with a faithful normal invariant state
on arbitrary von Neumann algebras. If such a semigroup has GNS spectral gap
\(\lambda\), then it has \(f\)-spectral gap at least \(\lambda\) for every
normalized operator-monotone function \(f\). In particular this includes

\[
f_{\mathrm{BKM}}(t)
=
\frac{t-1}{\log t},
\qquad f_{\mathrm{BKM}}(1)=1.
\tag{KM13}
\]

For a nontrivial fixed algebra \(N\), the statement holds on the kernel of
the \(\omega\)-preserving expectation \(E:M\to N\). For the present
symmetric-average semigroup, the GNS implementation of \(E\) is
\(P_\Gamma\), so

\[
\mathcal H^\Gamma=\overline{N\Omega_\omega}.
\]

Thus the complement used in (KM10) is the GNS completion of \(\ker E\).
Applied to (KM12), Wirth's theorem gives the same exponential lower rate in
the observable BKM Hilbert norm. Under (KM11), this reduces to the centered
scalar-fixed case.

This is a real strengthening of the carrier programme: a separately proved
GNS Kazhdan edge no longer needs an ad hoc comparison constant merely to
reach the *observable* BKM norm. It does not identify that norm with the
inverse BKM metric on state-density tangents. The two are Legendre-dual
carriers. A score map, predual dualization, or detailed-balance intertwiner
with its domain and range is still required before one may claim a
relative-entropy Hessian bound. [[measured-response-carriers/inq#Third carrier: faithful state tangents|Measured response carriers]]
owns this distinction.

Nor is \(L_\mu\) the physical Hamiltonian. Rescaling
\(t\mapsto at\) replaces it by \(aL_\mu\) without changing the invariant
state or fixed algebra. The group, Kazhdan set, probability normalization,
and physical meaning of one Markov step must be selected internally before
\(\lambda_\mu\) can be more than a dimensionless rigidity coefficient.

## The centralizer is the first physical coverage test

For a local-unitary state path generated by \(A=A^*\), the regional state
differential is

\[
d_\omega A(x)=i\omega([x,A]).
\tag{KM14}
\]

Its kernel is the state centralizer. If (KM11) holds but
\(M_\omega\neq\mathbb C\mathbf1\), then the Kazhdan defect charges some
nonvacuum GNS directions that the one-state response does not see. No
positive comparison

\[
q_\omega\geq b\langle\cdot,L_\mu\cdot\rangle,
\qquad b>0,
\tag{KM15}
\]

can hold on a core containing such a direction.

[[modular-cocycle-tomography/inq|Modular cocycle tomography]] gives two
ways to state the obstruction exactly. A single faithful state works if its
centralizer is scalar. More generally, a state atlas works algebraically if
its centralizers meet only in the scalars; relative to one reference state,
this is the cocycle-commutant condition

\[
M_{\omega_0}
\cap
\{[D\omega_i:D\omega_0]_t:i,t\}'
=
\mathbb C\mathbf1.
\tag{KM16}
\]

Marrakchi and Vaes prove that a type-III\(_1\) factor with separable predual
admits a dense \(G_\delta\) family of faithful normal states whose individual
centralizer is scalar. This clears the abstract existence obstruction. It
does not show that the physical vacuum restriction is one of those states,
and algebraic injectivity still permits approximate-null sequences.

There are therefore two different comparison regimes:

1. A **per-region** inequality such as (KM15) requires that region's
   response kernel to lie in \(\ker L_\mu\). If the latter is only the
   vacuum, the declared regional class must have no nonzero centered
   centralizer direction.
2. A **summed atlas** inequality may let individual regions or states retain
   large kernels. What matters is the intersection of their pullback kernels
   on one common physical source carrier, followed by a uniform lower-frame
   theorem.

Centralizers belonging to different regional algebras cannot be intersected
directly. Cross-region transport and the common physical source map are
part of the theorem.

## Net coherence is the compatibility condition

For a local net \(O\mapsto\mathcal A(O)\), a process family must satisfy at
least

\[
\mathsf P_t^{O_2}|_{\mathcal A(O_1)}
=
\mathsf P_t^{O_1}
\qquad(O_1\subset O_2),
\tag{KM17}
\]

vacuum preservation, and spacetime covariance

\[
\beta_g\mathsf P_t^O
=
\mathsf P_t^{gO}\beta_g.
\tag{KM18}
\]

If a clock automorphism preserves \(O\), its relation with the process must
also be declared, for example

\[
\alpha_s\mathsf P_t^O
=
\mathsf P_t^O\alpha_s.
\tag{KM19}
\]

These conditions are not empty formal wishes.
[[library/quantum-operations-on-conformal-nets/inq|Bischoff, Del Vecchio, and Giorgetti]]
construct compatible, vacuum-preserving, covariant UCP operation families on
chiral conformal nets and obtain compact or finite hypergroups for discrete
subnet inclusions. Their result is an exact precedent for the process-net
type. It does not construct a four-dimensional Yang--Mills operation, a
property-\((T)\) edge, or the physical energy comparison.

Adding such operations as new structural maps need not change any local QFT
prediction: the local algebra, vacuum, Poincare action, and clock Hamiltonian
can be retained exactly. If the operations are asserted to be actual time
evolution or laboratory channels, however, their observable effects must be
included and tested. “Compatibility” here means a coherent enrichment of
the local net, not automatic derivation of that net.

## The Copernican mass-gap chain

The reversal now has a precise theorem shape. At each regulator \(r\), one
must construct without consulting the Hamiltonian spectrum:

1. a net-natural group, hypergroup, or rigid-category action by
   state-preserving UCP maps on the complete neutral observable carrier;
2. a normalized same-carrier defect \(D_r\) with

   \[
   D_r\geq\kappa_{D,r}(I-P_{0,r}),
   \qquad \inf_r\kappa_{D,r}>0;
   \tag{KM20}
   \]

3. a physical Hilbert carrier \(\mathcal H_r\), a response Hilbert carrier
   \(\mathcal K_r\), a common complex energy-form core
   \(\mathscr C_r\subset\mathcal H_r\), and a physically selected modular or
   regional analysis map

   \[
   T_r:\mathscr C_r\longrightarrow\mathcal K_r;
   \]

   together with a bounded map
   \(C_r:\overline{T_r\mathscr C_r}\to\mathcal H_r\) satisfying the
   regulator-uniform core factorization

   \[
   D_r^{1/2}\Psi=C_rT_r\Psi
   \quad(\Psi\in\mathscr C_r),
   \qquad
   \sup_r\|C_r\|<\infty;
   \tag{KM21}
   \]

4. a local entropy--energy upper comparison on the same core; and
5. a controlled continuum and Poincare reconstruction.

For the finite-width relative-entropy solder, write

\[
q_r[\Psi]:=\|T_r\Psi\|^2.
\]

Equations (KM20)--(KM21) give

\[
q_r[\Psi]
\geq
\frac{\kappa_{D,r}}{\|C_r\|^2}
\|(I-P_{0,r})\Psi\|^2.
\tag{KM22}
\]

If the positive Hermitian extension of this response also obeys

\[
q_r[\Psi]
\leq
\frac{2\pi R_r}{\hbar c}
\langle\Psi,H_r\Psi\rangle,
\tag{KM23}
\]

then

\[
\boxed{
H_r
\geq
\frac{\hbar c}{2\pi R_r}
\frac{\kappa_{D,r}}{\|C_r\|^2}
(I-P_{0,r}).}
\tag{KM24}
\]

Here (KM24) is a quadratic-form inequality on \(\mathscr C_r\), extended by
closure on the declared \(H_r^{1/2}\)-form domain. A strictly positive
continuum lower bound requires the complete dimensional condition

\[
\boxed{
\inf_r
\frac{\kappa_{D,r}}{R_r\|C_r\|^2}>0.}
\tag{KM25}
\]

Uniform rigidity and uniform factorization alone do not suffice if the
selected physical width \(R_r\) diverges.

This is the desired upside-down calculation. The Hamiltonian did not define
the distinction operator; the independently constructed distinction edge
lower-bounds the Hamiltonian through a theorem about localized states.
Planck's constant appears only in the downstream conversion between the
dimensionless local-QFT distinction and clock energy. It is not used to
construct the pre-clock edge.

Equation (KM24) is still an energy gap. A Yang--Mills *mass* gap additionally
requires the physical vacuum representation, spectrum condition, full
translation representation, and Poincare-Casimir conclusion described in
[[mass-as-casimir-and-realization]]. The scale \(R_r\) must be selected
without fitting the glueball mass, and any cosmological selection must admit
a controlled \(G\to0\) pure-Yang--Mills limit.

## What the theorem changes

The candidate “operator” is no longer mysterious. Within an already
descended observable register, it operates first on the algebra as a UCP
endoprocess, then on the algebra's own GNS carrier as a positive Dirichlet
defect. Property \((T)\) can make its non-scalar edge
representation-uniform, and modular tomography states exactly when a local
state atlas sees the same directions. The remaining work is not to invent a
mass term. It is to derive the realization wall and operation family, prove
their relation, select the normalization and net-natural action, and obtain
the bounded core factorization (KM21).

The symmetric average used in (KM6) does not assert that ontology is
fundamentally symmetric. It extracts a positive coercive part from a process
family. Orientation, chirality, and record production cannot be inferred from
that symmetric average; they require additional data such as a grading,
ordered correspondence, antisymmetric component, instrument, or record map.
Symmetry is the grammar needed to represent the descended local sector; it
is not thereby made the primitive source of the process.

The categorical construction in
[[categorical-action-on-the-neutral-wilson-carrier]] is the non-group version
of this benchmark. There the load-bearing hypotheses are a normalized fusion
action by measured operations, annular or tube admissibility, and a
vacuum-only invariant vector. Categorical property \((T)\) then provides
(KM20). The present theorem shows exactly how that proposal belongs in a
larger process category and identifies the new 2026 BKM transfer that can be
used once the physical action exists.
