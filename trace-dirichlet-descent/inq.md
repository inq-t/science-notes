---
inq.module: "trace-dirichlet-descent"
inq.include:
  - "./"
inq.ambient:
  - "**"
---
# Trace Dirichlet Descent

A whole response reaches a local carrier by two opposite constructions. Pulling local observables into the whole gives a closed Dirichlet form and inherits every whole Poincare edge; minimizing over every forgotten whole representative of one conditional local presentation gives a smaller least-cost trace whose edge is exactly a whole-register lift inequality. A finite graph counterexample proves that the second construction is not automatically Markovian. A harmonic section simultaneously makes local reversible symmetries into units of a split-idempotent corner: state descent, observable pullback, nonfaithful least-cost elimination, local Markov decay, and unitary clock grammar are thereby related without being identified.

**Status: [EXACT] for the observable-pullback Dirichlet form, inherited Poincare edge, infimal pushforward, harmonic Pythagoras, corner compatibility, gap/lift equivalence, finite block formulas, and the conditional-expectation non-Markov counterexample under the stated hypotheses; [ESTABLISHED CLASSICAL THEORY] for trace Dirichlet forms and their boundary time-changed processes; [CONDITIONAL CONSTRUCTION] for a completely Dirichlet Type-III trace; [OPEN] for a net-natural Yang--Mills realization, regulator-uniform carrier coverage, physical clock-energy solder, and internal scale.**

## The missing arrow is an infimal pushforward

Let \(W\) be a complex vector space carrying a nonnegative Hermitian form \(\mathcal E_W\), let \(\mathcal H_L\) be a Hilbert space, and let

$$
q:D(\mathcal E_W)\longrightarrow\mathcal H_L
\tag{TD1}
$$

be a linear map with dense range. The fibre

$$
q^{-1}(\varphi)
=
\{w\in D(\mathcal E_W):qw=\varphi\}
\tag{TD2}
$$

contains all whole-register variations with the same local presentation. Define

$$
D(\check{\mathcal E})
:=
\left\{
\varphi\in\operatorname{ran}q:
\inf_{qw=\varphi}\mathcal E_W[w]<\infty
\right\},
\tag{TD3}
$$

and

$$
\boxed{
\check{\mathcal E}[\varphi]
:=
\inf_{qw=\varphi}\mathcal E_W[w].}
\tag{TD4}
$$

This is a quotient construction, not a restriction of \(\mathcal E_W\) to a preferred copy of \(\mathcal H_L\). The hidden fibre is quantified over before the local operator is formed. In the language of positive operators it is [[contemporary-puzzles/yang-mills-mass-gap/shorted-response-filtration-and-the-leak-cocycle|shorting]]; in boundary potential theory it is the trace form; in a finite block it is a Schur complement.

The operation is not automatically physical. The form \(\mathcal E_W\), the map \(q\), and the local Hilbert norm must be derived independently of the desired mass spectrum.

## Harmonic representatives and the exact residue

Suppose every fibre in (TD2) has a selected linear minimizer

$$
h:D(\check{\mathcal E})\longrightarrow D(\mathcal E_W),
\qquad
qh=I,
\tag{TD5}
$$

which is orthogonal to the vertical space in the \(\mathcal E_W\)-form:

$$
\mathcal E_W(h\varphi,n)=0
\qquad
(n\in\ker q).
\tag{TD6}
$$

Then \(h\varphi\) is the harmonic representative of \(\varphi\). Every \(w\) has the form

$$
w=hqw+n,
\qquad n\in\ker q,
\tag{TD7}
$$

and hence

$$
\boxed{
\mathcal E_W[w]
=
\check{\mathcal E}[qw]
+
\mathcal E_W[w-hqw].}
\tag{TD8}
$$

The nonnegative vertical residue is therefore

$$
\mathfrak R_q^{\mathcal E}(w)
:=
\mathcal E_W[w]-\check{\mathcal E}[qw]
=
\mathcal E_W[(I-hq)w].
\tag{TD9}
$$

This is a precise form-level sense in which a representative is forgotten. It is not automatically thermodynamic entropy, energy emitted to an exterior, state reduction, or production of a record. It measures the whole response that disappears when only the least-cost representative of the local class is retained.

When every downstream form is defined by the same infimal-pushforward rule, nested quotient maps compose by taking one joint infimum. This is the form version of transitivity of Anderson--Trapp shorting and gives a genuine descent law for successive eliminations.

## The finite block is a Dirichlet-to-Neumann operator

Let \(L\) and \(B\) be finite-dimensional Hilbert spaces,
\(W=L\oplus B\), and \(q(x,z)=x\). Let the whole response be represented by

$$
A=
\begin{pmatrix}
G&B_0\\
B_0^*&C
\end{pmatrix}
\geq0,
\qquad
C>0.
\tag{TD10}
$$

Here \(C>0\) means positive definite, hence boundedly invertible. The same
formula holds on infinite-dimensional block Hilbert spaces under the stronger
operator hypothesis \(C\geq cI\) for some \(c>0\).

Completing the square gives

$$
hx=
\begin{pmatrix}
x\\-C^{-1}B_0^*x
\end{pmatrix},
\qquad
\check A
=
G-B_0C^{-1}B_0^*\geq0,
\tag{TD11}
$$

and

$$
\check{\mathcal E}[x]
=
\langle x,\check A x\rangle.
\tag{TD12}
$$

If \(C\) is singular, the intrinsic shorted operator still exists for bounded \(A\); a Moore--Penrose formula requires the corresponding range condition and must not be inferred from notation alone.

For a finite electrical or Markov network, \(A\) is a graph Laplacian and \(\check A\) is the Kron-reduced boundary Laplacian. For an elliptic bulk form, \(\check A\) is the Dirichlet-to-Neumann operator: a boundary value is extended harmonically through the bulk, and the returned normal flux depends on the whole interior even though the operator acts only on boundary data. [[contemporary-puzzles/yang-mills-mass-gap/vacuum-boundary-gluing-and-wall-response|Vacuum boundary gluing]] contains the Gaussian field-theory member and its separate OS and physical-energy obligations.

This supplies a rigorous version of the reversal tactic:

$$
\boxed{
\text{do not place a mass operator inside the local space first;}
\quad
\text{derive a local response by eliminating whole-compatible lifts}.}
\tag{TD13}
$$

[[library/the-dirichlet-to-neumann-operator-on-rough-domains/inq|Arendt and ter Elst]] construct a positive self-adjoint Dirichlet-to-Neumann operator on rough boundaries by form methods and show that its negative generates a contractive \(C_0\)-semigroup. [[library/generalizing-dirichlet-to-neumann-operators/inq|Li]] identifies Dirichlet-to-Neumann operators of irreducible Dirichlet forms with trace Dirichlet forms and boundary time changes of the associated Markov processes.

## When the wall derives a local process

Assume that \(\check{\mathcal E}\) is densely defined, closed, symmetric, and
nonnegative on \(\mathcal H_L\). The representation theorem for closed forms
gives a unique positive self-adjoint operator \(D_q\) such that

$$
\check{\mathcal E}[\varphi]
=
\|D_q^{1/2}\varphi\|^2.
\tag{TD14}
$$

The word *Markovian* requires more than the bare Hilbert space. In the
classical case, assume \(\mathcal H_L=L^2(X,\mu)\) with its Hilbert-lattice
order and that \(\check{\mathcal E}\) is a Dirichlet form. Then

$$
P_s=e^{-sD_q},
\qquad s\geq0,
\tag{TD15}
$$

is a symmetric sub-Markov semigroup. It is conservative when the distinguished
constant is in the form kernel. In the noncommutative case, one must instead
supply a von Neumann algebra in standard form, its natural cone and order-unit
data; complete Dirichletness together with the corresponding conservativity
condition is the hypothesis that produces the \(L^2\) implementation of a
unital quantum Markov semigroup.

The logical order is

$$
(\mathcal E_W,q)
\longmapsto
\check{\mathcal E}
\longmapsto
D_q
\longmapsto
(P_s)_{s\geq0}.
\tag{TD16}
$$

The local Markov process is no longer an arbitrary extra operator. It is derived from the whole response and realization map. But the Markov property does not follow from positivity alone. Classical trace theorems supply it for suitable Dirichlet forms and boundary traces; a general positive Schur complement need not generate a positivity-preserving process, and a noncommutative Schur complement need not be a Lindblad generator.

## Conditional expectation alone does not preserve Markovianity

There is already a finite classical obstruction. Let \(A\) be the graph
Laplacian of the unit-conductance tree on vertices \(0,\ldots,5\) with edges

$$
01,\qquad04,\qquad05,\qquad12,\qquad13,
\tag{TD16a}
$$

and let \(q\) be conditional expectation for the uniform measure onto the
partition

$$
\{0,1\},\qquad\{2,3\},\qquad\{4,5\}.
\tag{TD16b}
$$

Writing the three block averages as \((a,b,c)\), direct minimization over the
three within-block differences gives

$$
\boxed{
\check{\mathcal E}(a,b,c)
=
2(a-b)^2+2(a-c)^2-\frac12(b-c)^2.}
\tag{TD16c}
$$

The form is nonnegative because it is a Schur complement of the graph
Dirichlet form. Nevertheless it is not a Dirichlet form. For
\(f=(0,-3,1)\), the normal contraction \(f\mapsto|f|\) gives

$$
\check{\mathcal E}(f)=12,
\qquad
\check{\mathcal E}(|f|)=18.
\tag{TD16d}
$$

Equivalently, relative to the pushed \(L^2\) measure, its generator is

$$
\begin{pmatrix}
2&-1&-1\\
-1&3/4&1/4\\
-1&1/4&3/4
\end{pmatrix},
\tag{TD16e}
$$

whose positive off-diagonal entry cannot be a Markov jump rate. Thus even an
ordinary state-preserving conditional expectation does not make the
infimal-pushforward form Markovian. Boundary traces in classical potential
theory have additional compatibility with pointwise normal contractions;
an arbitrary coarse conditional expectation does not.

This makes the noncommutative target sharper. One must derive a wall for
which the contraction property survives at every matrix amplification, or
identify another theorem that produces the local UCP semigroup. Positivity,
closedness, conditional expectation, and a lower spectral edge do not suffice.

## The variance-correct safe branch pulls observables back

The counterexample does not prevent a local Markov response; it distinguishes
two variances that are often conflated. Let
\(\pi:X\to Y\) be a measurable coarse map, let
\(\nu=\pi_*\mu\), and define the isometric observable pullback

$$
J:L^2(Y,\nu)\longrightarrow L^2(X,\mu),
\qquad
Jf=f\circ\pi.
\tag{TD16f}
$$

Its adjoint \(q=J^*\) is the local coordinate of conditional expectation and
\(qJ=I\). Besides the infimal quotient (TD4), the whole Dirichlet form
therefore defines the contravariant pullback form

$$
\mathcal E^\leftarrow[f]
:=
\mathcal E_W[Jf].
\tag{TD16g}
$$

This form has the Markov compatibility that the quotient may lack. For every
normal contraction \(C:\mathbb R\to\mathbb R\),

$$
J(C\circ f)=C\circ Jf
\quad\Longrightarrow\quad
\mathcal E^\leftarrow[C\circ f]
\leq
\mathcal E^\leftarrow[f].
\tag{TD16h}
$$

Because \(J L^2(Y,\nu)\) is a closed Hilbert subspace, the restriction of a
closed whole form to that pullback range is closed; density of its domain in
the local carrier remains a separate requirement. If the whole form is merely
closable and its pullback is closable, the closure retains the contraction
inequality. Thus the densely defined closed result is a classical Dirichlet
form. If the whole form satisfies

$$
\mathcal E_W[F]
\geq
\kappa\|F-\mu(F)\mathbf1\|_2^2,
\tag{TD16i}
$$

then the isometry and \(\mu(Jf)=\nu(f)\) give the inherited edge

$$
\boxed{
\mathcal E^\leftarrow[f]
\geq
\kappa\|f-\nu(f)\mathbf1\|_2^2.}
\tag{TD16j}
$$

The two local forms obey

$$
\check{\mathcal E}[f]
\leq
\mathcal E^\leftarrow[f],
\tag{TD16k}
$$

because \(Jf\) is one admissible lift of \(qF=f\). They answer different
questions:

- \(\check{\mathcal E}\) asks for the least whole response among all
  observables with the same conditional local presentation;
- \(\mathcal E^\leftarrow\) asks for the response of the actual local
  observable when viewed inside the whole algebra.

The first is an adjoint quotient through \(q\); the second is contravariant
transport through the multiplicative map \(J\). A marginal
state moves from whole to part while its observables move in the opposite
direction. This variance reversal is not notation: it is exactly why
functional calculus commutes with \(J\) but not with conditional expectation.

The compressed family \(q e^{-sD_W}J\) is a third construction and need not
obey the semigroup law without lumpability. Infimal quotient, observable
pullback, and semigroup compression must therefore remain separate.

At a finite Wilson regulator, the coordinate or cylinder form in
[[contemporary-puzzles/yang-mills-mass-gap/vacuum-boundary-gluing-and-wall-response#A direct route that does not require a local boundary action|the marginal-inheritance theorem]]
is precisely (TD16g). It is the safer Markov branch. The infimal trace remains
the sharper realization of least whole-compatible cost, but now carries a
genuine additional theorem obligation.

## The gap is exactly a whole-to-local lift inequality

Let
\(P_0=1_{\{0\}}(D_q)\) be the orthogonal projection onto the full local
zero-energy subspace, already identified physically with the vacuum sector.
For \(\kappa>0\), the following are equivalent as quadratic-form statements:

$$
D_q\geq\kappa(I-P_0),
\tag{TD17}
$$

$$
\check{\mathcal E}[\varphi]
\geq
\kappa\|(I-P_0)\varphi\|^2
\qquad
(\varphi\in D(\check{\mathcal E})),
\tag{TD18}
$$

and

$$
\boxed{
\mathcal E_W[w]
\geq
\kappa\|(I-P_0)qw\|^2
\qquad
(w\in D(\mathcal E_W)).}
\tag{TD19}
$$

Indeed, (TD18) and \(\check{\mathcal E}[qw]\leq\mathcal E_W[w]\) imply (TD19). Conversely, taking the infimum of (TD19) over every lift of a fixed \(\varphi\) gives (TD18).

Equation (TD19) is the exact Copernican stopping condition:

> Every whole variation that presents a nonvacuum local distinction must pay a uniform positive whole-response cost.

The whole form may still be globally gapless. Under (TD19), every sequence
\(w_n\) satisfying \(\mathcal E_W[w_n]\to0\) must obey

$$
(I-P_0)qw_n\longrightarrow0.
\tag{TD20}
$$

Thus the lift inequality is compatible with scale-free or soft whole
directions only when they disappear into the local vacuum presentation.
Vanishing local image does not by itself construct such directions; it only
removes this lower-bound obstruction. Merely proving that exact zero modes lie
in \(\ker q\) is insufficient; (TD19) forbids *almost* visible soft modes as
well.

When minimizers exist,

$$
\ker D_q=q(\ker\mathcal E_W).
\tag{TD21}
$$

Hence a unique local vacuum requires \(q(\ker\mathcal E_W)=\operatorname{ran}P_0\). In nonattained or nonclosed settings the corresponding closure statement must be proved rather than presumed.

For bounded \(A\geq0\) and bounded \(q\), (TD19) is

$$
A\geq\kappa q^*(I-P_0)q.
\tag{TD22}
$$

Equivalently, Douglas factorization gives
\(C\in\operatorname B(W,\mathcal H_L)\) with

$$
(I-P_0)q=CA^{1/2},
\qquad
\|C\|^2\leq\kappa^{-1}.
\tag{TD23}
$$

This exposes the true carrier question: the local distinction map must factor continuously through the square root of the whole response. A numerical eigenvalue on an unrelated carrier proves nothing.

## The local clock is a unit in the retained corner

The form-domain maps in (TD1) and (TD5) do not automatically act on the
completed Hilbert carriers. Suppose additionally, for this section, that
\(W\) is a Hilbert whole carrier and that \(q\) and \(h\) extend to bounded
maps

$$
q:W\longrightarrow\mathcal H_L,
\qquad
h:\mathcal H_L\longrightarrow W,
\qquad
qh=I_{\mathcal H_L},
\tag{TD24}
$$

whose restrictions retain the harmonic property on the form domains. Put

$$
e=hq.
\tag{TD25}
$$

Then \(e^2=e\), and [[algebra/retract-corners-and-local-unitarity|the retract-corner theorem]] gives

$$
\operatorname B(\mathcal H_L)
\cong
e\operatorname B(W)e,
\qquad
U\longmapsto hUq.
\tag{TD26}
$$

When \(U\in\operatorname{GL}(\mathcal H_L)\), its representative \(hUq\)
is invertible relative to the corner identity \(e\). If \(q\) is
noninjective, it cannot be invertible relative to \(I_W\). If, in addition,
\(h\) is an isometry and \(q=h^*\), then a local unitary \(U\) is represented
by the partial unitary \(hUh^*\) on the whole Hilbert carrier and is a unitary
inside the \(C^*\)-corner. Isometry of \(h\) alone is not enough: the adjoint
relation is what makes \(e=hh^*\) an orthogonal projection and the corner
isomorphism a \(*\)-isomorphism.

If \(U\) also preserves the trace form,

$$
\check{\mathcal E}[U\varphi]
=
\check{\mathcal E}[\varphi],
\tag{TD27}
$$

then

$$
\mathcal E_W[hUqw]
=
\check{\mathcal E}[qw]
\leq
\mathcal E_W[w].
\tag{TD28}
$$

The vertical excess is removed once, while the retained action is reversible. Form invariance also implies

$$
U^*D_qU=D_q.
\tag{TD29}
$$

For a strongly continuous group \(U_t=e^{-itK}\), \(K\) is the local clock generator. Even when (TD29) holds,

$$
\boxed{D_q\neq K\quad\text{without an additional theorem}.}
\tag{TD30}
$$

The first is a positive distinction or relaxation generator; the second generates reversible clock translations. Commutation is compatibility, not identity.

The three relevant arrows are therefore

$$
q:W\to\mathcal H_L,
\qquad
P_s=e^{-sD_q},
\qquad
U_t=e^{-itK}.
\tag{TD31}
$$

The first is nonfaithful formation, the second is one-sided local relaxation, and the third is reversible local clock grammar. This is the precise algebra beneath the poetic claim that ontological directedness can make a locally reversible clock possible.

## The Type-III pullback theorem is exact

[[trace-dirichlet-descent/standard-form-pullback-and-reducing-wall|The
standard-form pullback theorem]] closes the safe noncommutative arrow. Let
\(\iota:N\hookrightarrow M\) be a normal unital faithful inclusion, let
\(\varphi\) be a faithful normal whole state, and suppose \(N\) is invariant
under \(\sigma^\varphi\). By Takesaki's theorem this is equivalent to a
\(\varphi\)-preserving normal faithful expectation \(E:M\to N\). The
inclusion induces a standard-form isometry

$$
V:L^2(N,\varphi|_N)\longrightarrow L^2(M,\varphi)
\tag{TD31a}
$$

whose amplifications preserve the Markov intervals at every matrix level. If
\(\mathcal E_M\) is a closed completely Dirichlet form and

$$
\mathcal E_N[\eta]:=\mathcal E_M[V\eta]
\tag{TD31b}
$$

has dense domain, then \(\mathcal E_N\) is closed and completely Dirichlet.
Modularity and conservativity descend under the corresponding modular
intertwining and zero-energy-vacuum hypotheses. This theorem applies to
\(\sigma\)-finite Type-III factors without a trace-class density matrix.
Type III is therefore compatible with the safe pullback; it is not itself a
source of a positive floor.

The sharper infimal quotient remains conditional. It equals (TD31b) when the
standard-form projection \(p=VV^*\) reduces the whole form, equivalently when
it commutes with the self-adjoint \(L^2\) semigroup. In that case the hidden
and retained directions are form-orthogonal and pullback, invariant
restriction, infimal quotient, and semigroup compression agree. Without this
reducing condition the pullback remains completely Dirichlet, but the
infimal quotient may fail Markovianity and the compressed family may fail the
semigroup law.

Thus a Type-III least-cost realization must still supply:

1. a physically defined expected inclusion and standard-form carrier map;
2. a KMS-symmetric completely Dirichlet whole form derived before the desired spectrum;
3. either reduction of the retained subspace or a special theorem proving density, closedness, and complete Markovianity of the infimal pushforward;
4. covariance under the local net and relevant gauge action; and
5. the vacuum-kernel identity and uniform lift inequality (TD19).

Once a KMS-symmetric quantum Markov semigroup has been constructed, [[library/derivations-and-kms-symmetric-quantum-markov-semigroups/inq|Vernooij and Wirth]] show that its \(L^2\) generator can be represented as the square of a derivation into a Hilbert bimodule. [[library/the-differential-structure-of-generators-of-gns-symmetric-quantum-markov-semigroups/inq|Wirth's GNS-symmetric theorem]] gives a twisted product rule controlled by modular structure. These results explain what the derived local response operates through; they do not prove a nonreducing infimal pushforward completely Dirichlet.

## Yang--Mills specialization

At regulator \(r\), the desired data are

$$
\left(
D(\mathcal E_{W,r}),
\mathcal E_{W,r},
q_r,
\mathcal H_r,
P_{0,r}
\right),
\tag{TD32}
$$

with

$$
\check{\mathcal E}_r[\Psi]
=
\inf_{q_rw=\Psi}\mathcal E_{W,r}[w],
\qquad
\check{\mathcal E}_r[\Psi]
=
\|D_r^{1/2}\Psi\|^2.
\tag{TD33}
$$

The dimensionless gap is no longer posited as a free Markov step. It follows if one proves

$$
\mathcal E_{W,r}[w]
\geq
\kappa_r\|(I-P_{0,r})q_rw\|^2
\tag{TD34}
$$

on the complete physical lift domain. To solder it to local clock energy, one
still needs a same-carrier upper comparison on a common complex form core
\(\mathscr C_r\subset
D(D_r^{1/2})\cap D(H_r^{1/2})\), for example

$$
\check{\mathcal E}_r[\Psi]
\leq
\frac{2\pi R_r}{\hbar c}
\|H_r^{1/2}\Psi\|^2
\qquad(\Psi\in\mathscr C_r).
\tag{TD35}
$$

Then

$$
H_r
\geq
\frac{\hbar c}{2\pi R_r}\,
\kappa_r(I-P_{0,r}).
\tag{TD36}
$$

If comparison maps or normalization constants intervene, their operator norms enter exactly as in [[contemporary-puzzles/yang-mills-mass-gap/localized-relative-entropy-and-the-energy-solder|the localized energy solder]]. A continuum result requires the appropriately normalized version of

$$
\inf_r\frac{\kappa_r}{R_r}>0,
\tag{TD37}
$$

together with infinite-volume control, convergence of forms and vacuum projections, OS or direct positive-energy reconstruction, and Poincare covariance.

Equation (TD34), not a fitted glueball energy, is the immediate research
target for the least-cost branch. The safer pullback branch instead asks for
a regulator-uniform whole Poincare inequality on the pulled-back complete
neutral observable core. It permits fewer kinds of whole soft modes because
the lift is fixed to \(J_r\Psi\), whereas (TD34) controls every representative
of the same conditional local presentation. The dimensional yardstick remains
separate. In (TD35), \(\hbar\) belongs to the downstream clock-energy
calibration; it has not been used to define the pre-QFT response.

[[contemporary-puzzles/yang-mills-mass-gap/gauge-dirichlet-trace-carrier|The regulated gauge specialization]]
now verifies the first finite part of this programme without reading from the
transfer spectrum. A volume-uniform strong-coupling Poincare estimate for the
Wilson Euclidean Langevin form gives a closed Markov cylinder form on any
coordinate interface with the same constant; it also implies (TD34) for the
conditional-expectation trace. Conditional reflection-Markov factorization
can transport either interface operator to the OS Hilbert carrier. The
cylinder branch still requires full neutral-algebra coverage and a physical
energy comparison. The trace branch additionally requires closed complete
Dirichletness. Moreover, the known uniform estimate is confined to
fixed-lattice strong coupling and does not approach the four-dimensional
asymptotically free continuum limit. This is a worked carrier test, not a
continuum mass-gap theorem.

## What would falsify this route

- If \(\check{\mathcal E}\) is not closed, it need not define a self-adjoint local generator.
- If it is not Markovian or completely Dirichlet in the relevant setting, its semigroup is not the required classical or quantum process.
- If \(q\) only removes gauge naming redundancy, its noninjectivity does not establish ontological forgetting.
- If \(\mathcal E_W\) is copied from the Yang--Mills Hamiltonian whose gap is sought, the construction is circular.
- If soft whole sequences retain a normalized nonvacuum local image, (TD19) fails and the local edge closes.
- If \(D_q\) is called physical time merely because it generates a semigroup, the clock/relaxation distinction has been erased.
- If \(\kappa_r>0\) at each finite regulator but the calibrated uniform bound vanishes, no continuum mass gap follows.
- If the harmonic section is chosen arbitrarily, the corner theorem proves only compatibility with that choice, not a principle selecting nature's local algebra.

The present gain is specific. A multiplicative observable pullback gives a
safe bridge from whole response to local Markov form; the sharper least-cost
bridge is Markov only under extra wall compatibility, and its
global-gap/local-gap relation reduces to the lift inequality (TD19). Local
unitarity lives naturally in the corner created by the prior idempotent
descent. Complete Type-III realization, Yang--Mills carrier coverage, uniform
continuum comparison, and the physical yardstick remain the frontier.

[[trace-dirichlet-descent/receipts/trace_dirichlet_descent_receipt.py|The finite graph receipt]] and [[trace-dirichlet-descent/receipts/trace-dirichlet-descent-receipt-output.txt|its stored output]] verify the Schur complement, harmonic residue, lift inequality, gapless-whole/gapped-trace family, split idempotent, and corner inverse by exact matrix identities in one three-vertex model. The same receipt verifies (TD16c)--(TD16e) in the six-vertex counterexample. It does not test the infinite-dimensional, complete-Markov, Type-III, continuum, or physical claims.
