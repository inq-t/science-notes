# Compatible Spectral Readouts and a Positive Clock

Reflected boundary pairings at every integer duration can construct a positive transfer operator through a positive-kernel quotient; a separate endpoint test decides whether it has a full-carrier Hamiltonian logarithm. Their compatible spectral readouts can then be assembled into one global clock without assuming autonomous clocks in every local context. These are moment and spectral-dilation constructions, not new mass-gap theorems: they preserve a common vacuum and floor when the boundary data establish them, but do not derive the field algebras or Yang–Mills dynamics from compatibility alone.

## Reflected boundary moments can precede the spectrum

One need not supply the spectral measures as the first input. Let
\(\mathcal R\) be a retained boundary Hilbert space and let
\(R_n\in B(\mathcal R)\), \(n\ge0\), be self-adjoint all-duration boundary
pairings, with \(R_0=I\). For finite sequences \(f=(\xi_i)\), \(g=(\eta_j)\),
define
\[
q_a(f,g)=\sum_{i,j\ge0}\langle\xi_i,R_{i+j+a}\eta_j\rangle,
\qquad a=0,1.
\tag{HM1}
\]
Require, for every finite sequence of arbitrary length,
\[
\boxed{q_0\ge0,\qquad 0\le q_1\le q_0.}
\tag{HM2}
\]
The sum \(i+j\) has a boundary meaning: preparation of depth \(i\) is
reflected and sewn to preparation of depth \(j\). The shifted form inserts
one further layer. Positivity of each \(R_n\) separately is insufficient.
The upper bound is a contraction condition in a specified normalization,
not reflection positivity alone and not a spectral gap.

Here is the positive-kernel moment reconstruction, a standard
Hausdorff/GNS-type construction with its proof included; the general
operator-moment setting is treated by
[[library/operator-moment-dilations-as-block-operators/inq|Bhat, Ghatak and Pamula]].
Complete the finite sequences modulo the nullspace of \(q_0\), obtaining
\(\mathcal K_{\rm mom}\). Since
\[
|q_1(f,g)|^2\le q_1(f,f)q_1(g,g)\le q_0(f,f)q_0(g,g),
\]
\(q_1\) descends to a bounded positive form and represents a unique
operator \(0\le T\le I\). The symbolic shift \(S[i,\xi]=[i+1,\xi]\) obeys
\(q_0(Sf,g)=q_1(f,g)\). Thus
\[
[Sf]=T[f].
\]
This also proves that the shift respects the null quotient; no unproved
domain invariance or extra second-shift estimate was assumed.

The degree-zero inclusion \(J\xi=[0,\xi]\) is isometric, and
\[
\boxed{R_n=J^*T^nJ,\qquad
\mathcal K_{\rm mom}
=\overline{\operatorname{span}\{T^nJ\xi:n\ge0,\ \xi\in\mathcal R\}}.}
\tag{HM3}
\]
Conversely any positive contraction with such an isometric readout obeys
(HM2): the two forms are respectively
\(\|\sum_iT^iJ\xi_i\|^2\) and the expectation of \(T\) on that vector.
Two minimal realizations are unitarily equivalent by mapping their power
symbols to one another. Their inner products agree by (HM1).

The spectral measure of \(T\) now gives a normalized POVM
\(\mathsf N\) on \([0,1]\), with
\[
R_n=\int_0^1x^n\,d\mathsf N(x).
\tag{HM4}
\]
It is unique: equality of all moments gives equality on polynomials,
then on continuous functions by uniform approximation, and then of the
scalar measures and their polarized operator matrix elements.
Compatible boundary isometries preserving **every** \(R_n\) consequently
preserve every spectral effect of \(\mathsf N\). This is an upstream source
for the compatible spectral data below, not an extra independently fitted
POVM.

### A positive transfer is not yet a full-carrier clock

A nonnegative self-adjoint Hamiltonian logarithm on the whole minimal
carrier exists precisely when \(\ker T=0\). Under this condition it is
\[
H=-\log T,\qquad
D(H)=\left\{\psi:\int_{(0,1]}|\log x|^2
\,d\langle\psi,E_T(x)\psi\rangle<\infty\right\}
\tag{HM5}
\]
with a dense domain in the **whole** minimal carrier. The operator
\(H\) may be unbounded; no infinite eigenvalue is assigned.
Zero may remain in the continuous spectrum of
\(T\). If a zero eigenspace exists, \(T^s\) as \(s\downarrow0\) converges
strongly to \(I-P_{\ker T}\), not \(I\), so it is not the heat semigroup
of a full-carrier self-adjoint Hamiltonian.

This injectivity condition can be tested directly in the input moments:
\[
D_k:=\sum_{j=0}^k(-1)^j\binom{k}{j}R_j
=J^*(I-T)^kJ
\ \xrightarrow[k\to\infty]{\rm strong}\
J^*P_{\ker T}J.
\tag{HM6}
\]
The positive operators decrease in order. Their strong limit vanishes
if and only if \(\ker T=0\), using the minimal power-symbol span in (HM3).
Norm convergence is not required; imposing it would exclude legitimate
unbounded-energy clocks.

When this test passes, push \(\mathsf N\) forward by \(x\mapsto-\log x\)
to obtain the measure on \([0,\infty)\) used in (CR1)–(CR10).
The vacuum is the \(T=1\), or \(H=0\), sector—not the \(T=0\) sector.
A unique vacuum and a positive mass threshold remain separate conditions.

The distinction applies directly to
[[gauge-boundary-frame-gluing/overlap-kernels-and-face-refinement|finite overlap kernels]]:
their finite-rank convolution operators have exact zero modes. Restricting
to their supported range changes the degree-zero carrier and is not a
harmless logarithm convention. A Poissonized generator such as \(I-B_N\)
defines a different finite-step semigroup; its continuum comparison must
be proved rather than identified with the exact powers \(B_N^n\).

### What survives spatial readout and limiting operations

For an isometry \(V:\mathcal R'\to\mathcal R\), the compressed sequence
\(R'_n=V^*R_nV\) preserves (HM2) by substitution. For an actual normalized
gauge transfer \(\widehat T\), sewing and spatial readout give
\[
R_n=J^*\widehat T^{\,n}J,\qquad
R_2-R_1^2=J^*\widehat T(I-JJ^*)\widehat TJ\ge0.
\tag{HM7}
\]
Replacing this sequence by \(R_1^n\) removes hidden return.
[[coarse-response-memory/spectral-readout-and-the-visible-gap|Spectral readout]]
owns the complete memory and coverage distinctions.

Weak operator limits of every \(R_n\), on a fixed retained carrier or
through specified common embeddings, preserve (HM2): each test is a finite
sum. They need not preserve (HM6), vacuum uniqueness, or a gap.
For example \(R_n^{(k)}=e^{-kn}I\) has an injective transfer for every
\(k\), whereas its moment limit is \(R_0=I,\ R_n=0\) for \(n\ge1\).
A limiting clock needs an additional exclusion of this zero-transfer atom.

The theorem therefore identifies what the many-boundary amplitude law
must supply: consistently normalized pairings for all depths, the
reflected inequalities on all finite preparations, and the endpoint
conditions needed for the logarithm and vacuum. It does not prove those
conditions for repeated four-dimensional coarse graining.
[[gauge-boundary-frame-gluing/overlap-kernels-and-face-refinement#Temporal sewing needs a separate refinement law|Temporal sewing of the overlap law]]
constructs these pairings on a fixed spatial graph under a declared
anisotropic refinement. Its same-weight alternative instead realizes
the zero-transfer-atom failure even after Perron normalization; the
endpoint test is a genuine constraint on that law, not just an abstract
possibility.
[[temporal-column-response/spatial-elimination-and-self-return|Whole-column elimination]]
already preserves reflection positivity under its stated geometric
hypotheses while producing time-nonlocal amplitudes. Their actual
all-duration pairings must be retained, not reset to a one-step action.


## The input is a composable response, not a list of local Hamiltonians

For clarity use a countable nested family of Hilbert spaces \(\mathcal R_n\) and isometries
\[
v_{mn}:\mathcal R_n\longrightarrow\mathcal R_m,\qquad
v_{\ell m}v_{mn}=v_{\ell n},\qquad m\ge n.
\tag{CR1}
\]
The index is a refinement or context label, not clock time. The same argument works for a directed family by using a common upper context.

On \(X=[0,\infty)\), let \(\mathsf M_n\) be normalized positive operator-valued measures satisfying
\[
\boxed{\mathsf M_n(B)=v_{mn}^*\mathsf M_m(B)v_{mn}}
\quad\text{for every Borel }B\subseteq X.
\tag{CR2}
\]
Countable additivity is in the weak operator sense. No primitive global Hamiltonian is part of these data.

[[coarse-response-memory/spectral-readout-and-the-visible-gap|Spectral readout]]
shows why (CR2) is the appropriate compatibility rather than merely
matching first response moments. It holds for compressions of one whole
spectral measure even when their heat readouts have memory and their
unitary readouts are not unitary.

If every \(\mathsf M_n\) were projection-valued, (CR2) would force the smaller embedded carrier to reduce the larger spectral measure. Starting with sharp autonomous clocks at every level therefore reinstates precisely that extra hypothesis. Positive operator-valued readouts allow a more general relation.

## Assemble a positive measure before constructing the whole clock

Take the Hilbert inductive limit \(\mathcal R\), with canonical isometries \(j_n\), so \(j_m v_{mn}=j_n\) and \(\bigcup_n j_n\mathcal R_n\) is dense. For vectors from two stages and a common \(m\ge n,k\), define
\[
b_B(j_n\xi,j_k\eta)
=\langle v_{mn}\xi,\mathsf M_m(B)v_{mk}\eta\rangle.
\tag{CR3}
\]
Equation (CR2) makes this independent of the common stage and of representatives. Since \(0\le\mathsf M_m(B)\le I\), it is a bounded positive sesquilinear form:
\[
0\le b_B(x,x)\le\|x\|^2,\qquad
|b_B(x,y)|\le\|x\|\|y\|.
\]
It therefore extends uniquely to a positive contraction \(\mathsf M(B)\) on \(\mathcal R\), with
\[
j_n^*\mathsf M(B)j_n=\mathsf M_n(B),\qquad
\mathsf M(X)=I.
\tag{CR4}
\]

For disjoint \(B_r\), countable additivity holds on each finite-stage vector by that of \(\mathsf M_n\). It extends to arbitrary vectors by approximation: the positive difference between the measure of the union and any finite partial sum is bounded by \(I\), uniformly in that partial sum. Quadratic forms therefore pass to the limit; polarization gives the mixed matrix elements. Thus \(\mathsf M\) is a normalized positive operator-valued measure, not merely a finitely additive set function.

No new normalization or state was fitted between stages. Compatibility was used on all spectral sets, not only on finitely many sampled moments.

## A positive kernel creates the dilation carrier

Form finite sums of symbols \([B,\xi]\), with Borel \(B\subseteq X\) and \(\xi\in\mathcal R\), linear in \(\xi\), and declare
\[
\boxed{\langle[B,\xi],[C,\eta]\rangle
=\langle\xi,\mathsf M(B\cap C)\eta\rangle.}
\tag{CR5}
\]
The resulting form is positive semidefinite. To see this for a finite sum, refine its sets into finitely many disjoint Boolean atoms \(F\). Its squared norm becomes
\[
\sum_F\left\langle
\sum_{i:F\subseteq B_i}\xi_i,\,
\mathsf M(F)\sum_{i:F\subseteq B_i}\xi_i
\right\rangle\ge0.
\tag{CR6}
\]
Quotient by the null space and complete, obtaining \(\mathcal K\). These are spectral-response symbols; their equivalence classes are not assumed spacetime points or actualized outcomes.

Define
\[
E(B)[C,\eta]=[B\cap C,\eta],
\qquad
J\xi=[X,\xi].
\tag{CR7}
\]
The intersection rule gives self-adjoint projections with \(E(B)E(C)=E(B\cap C)\). Their norm bound follows from the orthogonal decomposition into \(B\) and its complement, so they descend through the null quotient. Countable additivity is strong on the dense simple-symbol space by the scalar measure identity, and extends by boundedness. Hence \(E\) is a projection-valued measure, with \(E(X)=I_{\mathcal K}\).

Normalization gives
\[
\boxed{J^*J=I,\qquad \mathsf M(B)=J^*E(B)J.}
\tag{CR8}
\]
Moreover \(\operatorname{span}\{E(B)J\xi\}\) is dense by construction. This is the minimal spectral dilation. If another dilation has this same minimality, the map \(E(B)J\xi\mapsto E'(B)J'\xi\) preserves (CR5), extends to a unitary, and intertwines the measures and embeddings. The output is therefore unique up to the stated unitary equivalence, not up to arbitrary identification of observable algebras.

## The positive clock and its domain are returned together

The spectral measure gives the nonnegative self-adjoint operator
\[
\boxed{H=\int_X\lambda\,dE(\lambda),\qquad
\operatorname{Dom}H=
\left\{\zeta:\int_X\lambda^2\,d\langle\zeta,E(\lambda)\zeta\rangle<\infty\right\}.}
\tag{CR9}
\]
The bounded-spectral-interval vectors form a dense domain. Its unitary group and heat semigroup satisfy, with \(J_n=Jj_n\),
\[
\begin{aligned}
J_n^*e^{-sH}J_n&=\int e^{-s\lambda}\,d\mathsf M_n(\lambda),\\
J_n^*e^{-itH}J_n&=\int e^{-it\lambda}\,d\mathsf M_n(\lambda).
\end{aligned}
\tag{CR10}
\]
Thus one positive generator realizes all the compatible readouts. The global unitaries are obtained through this positive-kernel completion; they were not imposed separately at each context.

The spectral variable \(\lambda\) already had an agreed normalization in (CR2). The theorem does not select a physical duration unit. Pushing every spectral measure forward by the same map \(\lambda\mapsto a\lambda\), \(a>0\), returns \(aH\) on the canonically identified minimal carrier.

## A common vacuum and floor survive the minimal dilation

Assume compatible unit vectors \(\Omega_n\), with
\[
v_{mn}\Omega_n=\Omega_m,\qquad
\mathsf M_n(\{0\})=P_{\Omega_n}.
\tag{CR11}
\]
They define a unit vector \(\Omega\in\mathcal R\). Equation (CR3), tested on finite-stage vectors, gives \(\mathsf M(\{0\})=P_\Omega\).

The projection \(E(\{0\})\) fixes \(J\Omega\), because its expectation there is one. For \(\xi\perp\Omega\),
\[
\|E(\{0\})J\xi\|^2
=\langle\xi,\mathsf M(\{0\})\xi\rangle=0.
\]
Applying \(E(\{0\})\) to the dense minimal symbols \(E(B)J\xi\) therefore gives either zero or a multiple of \(J\Omega\). Consequently
\[
\boxed{\ker H=\mathbb C J\Omega.}
\tag{CR12}
\]
Without minimality an arbitrary invisible zero-energy sector could have been appended, so that hypothesis is essential to this conclusion.

If, in addition, one \(\delta>0\) satisfies
\[
\mathsf M_n((0,\delta))=0\qquad\text{for every }n,
\tag{CR13}
\]
then \(\mathsf M((0,\delta))=0\). Hence \(E((0,\delta))J=0\), and minimality forces \(E((0,\delta))=0\) on all of \(\mathcal K\). Thus
\[
\boxed{H\ge\delta(I-P_{J\Omega}).}
\tag{CR14}
\]
Equation (CR14) is a quadratic-form lower bound when \(H\) is unbounded. It preserves a proved common lower bound; it does not create one or assert that \(\delta\) is the sharp edge. Separate floors \(\delta_n\downarrow0\), or convergence of finitely many moments, do not establish (CR13).

## What this assembly does not reconstruct

The dilated projection-valued measure \(E\) gives a \(*\)-representation of the commutative bounded spectral-function algebra on \(\mathcal K\). Its compressed positive map in (CR8) need not be multiplicative. Neither construction automatically extends every given local observable algebra on \(\mathcal R_n\) to a compatible unital representation on \(\mathcal K\). [[algebra/spectral-coefficient-lifts-and-the-frozen-clock|The coefficient-lift theorem]] makes the simplest attempted rule precise: keeping \(B\) fixed and replacing \([B,\xi]\) by \([B,a\xi]\) gives a \(*\)-representation exactly when the spectral effects commute with the supplied coefficient algebra. These lifts preserve energy sectors and cannot create positive-energy excitations from a zero-energy vacuum.

There is a constructive whole-algebra return.
[[directed-analytic-realization/preparation-overlaps-and-the-transition-algebra|Preparation overlaps]]
fix the product of transitions between the completed preparation classes.
Their norm completion is the compact-operator algebra on \(\mathcal K\),
with the same clock; its ultraweak completion is \(B(\mathcal K)\).
This is not yet the specified local algebra. Even the canonical corner
\(a\mapsto JaJ^*\) changes the unit to \(JJ^*\), and a three-dimensional
minimal-dilation example has no unital representation of the supplied
\(M_2\) at all. What remains is selection and compatible realization
of the physical local algebras, not merely construction of some
noncommutative operators.

[[algebra/occupation-conditioned-clocks-and-the-vacuum-boundary#A minimal spectral carrier need not retain the visible algebra|The two-rate oscillator test]]
exhibits the problem on an infinite-dimensional carrier. Minimal spectral
completion removes an invisible antisymmetric vacuum, while an original
visible lowering operator sends a retained excitation to that removed
vector. Minimality of the clock realization is not reduction for the
observable algebra, even when the resulting clock has a unique vacuum
and a positive gap.

That missing operator realization is a substantive part of the full target, not an optional interpretation. One must supply:

- a law producing the local positive kernels and their full compatibility from the directed relational data;
- compatible realizations of the gauge-invariant observable algebras, including their localization and covariance;
- a physical vacuum/translation interpretation and proof of a common spectral exclusion on the complete intended carrier.

[[algebra/modular-mirror-response-and-the-analytic-domain|Modular mirror response]]
provides a possible source of relational forms, while
[[algebra/expected-inclusions-and-mirror-clock-consistency|the inclusion test]]
shows why those forms alone do not supply (CR2). A correlated whole may
give exactly matching first moments and different spectral readouts.
The hidden-return response, or an equivalent complete spectral kernel,
must remain in the construction.

The gain is an exact intermediate type for the master-object programme: a coherent family of positive spectral kernels can create a common carrier and clock without demanding autonomous clocks in every local context. This still falls short of the interacting four-dimensional Yang--Mills return and does not lower that obligation.
