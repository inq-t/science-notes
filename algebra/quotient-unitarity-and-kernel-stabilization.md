# Quotient Unitarity and Kernel Stabilization

A nonfaithful realization can coexist exactly with reversible unitary dynamics on its retained quotient. The transformations that descend are those preserving the realization kernel, and those that preserve the descended positive form become isometries of the quotient completion. Thus an observed symmetry group may arise as the image of a kernel stabilizer even when no nondegenerate upstream Hilbert norm, and hence no upstream notion of unitarity, has been supplied. This proves compatibility, not causation: the kernel does not by itself select the local dynamics, Hamiltonian, or mass gap.

**Status: [EXACT] for the quotient-flow and semidefinite-form propositions; [INTERPRETATION] for observed symmetry as the grammar of a retained presentation; [OPEN] for deriving the physical quotient, local Poincare action, clock, Hamiltonian, and Yang--Mills coercivity from one upstream construction.**

## Automorphisms descend through an invariant kernel

Let \(\mathcal A\) be a unital \(C^*\)-algebra, let \(I\) be a proper closed
two-sided \(*\)-ideal, and let

\[
q:\mathcal A\twoheadrightarrow\mathcal A/I
\tag{KU1}
\]

be the quotient map. Suppose
\(\alpha:\mathbb R\to\operatorname{Aut}(\mathcal A)\) is a one-parameter
automorphism group. The following conditions are equivalent:

1. \(\alpha_t(I)=I\) for every \(t\in\mathbb R\);
2. there is a unique one-parameter automorphism group
   \(\bar\alpha:\mathbb R\to\operatorname{Aut}(\mathcal A/I)\) satisfying

   \[
   q\alpha_t=\bar\alpha_tq.
   \tag{KU2}
   \]

Indeed, kernel invariance makes

\[
\bar\alpha_t(q(a)):=q(\alpha_t(a))
\tag{KU3}
\]

well defined, and \(\alpha_{-t}\) supplies its inverse. Conversely, (KU2)
implies \(q(\alpha_t(a))=0\) whenever \(a\in I\), so
\(\alpha_t(I)\subseteq I\); applying the same argument to \(-t\) gives
equality.

The subgroup

\[
\operatorname{Stab}(I)
:=
\{\beta\in\operatorname{Aut}(\mathcal A):\beta(I)=I\}
\tag{KU4}
\]

therefore acts on the quotient. If

\[
\operatorname{Null}(q)
:=
\{\beta\in\operatorname{Stab}(I):q\beta=q\},
\]

then the lifted observable symmetry is described exactly by

\[
1\longrightarrow\operatorname{Null}(q)
\longrightarrow\operatorname{Stab}(I)
\longrightarrow
\operatorname{Im}\!\left(
\operatorname{Stab}(I)\to\operatorname{Aut}(\mathcal A/I)
\right)
\longrightarrow1.
\tag{KU5}
\]

The last group need not be all of \(\operatorname{Aut}(\mathcal A/I)\): a
local symmetry need not lift. What is exact is that every lifted local
symmetry comes from the stabilizer of the forgotten ideal, modulo upstream
transformations that have become observationally trivial.

If only \(\alpha_t(I)\subseteq I\) for \(t\geq0\) is known for a one-sided
endomorphism semigroup, the same formula gives a quotient semigroup. The
inverse and the word *unitary* do not follow.

## The quotient flow can be unitary although the quotient map is not

Let \(\bar\omega\) be an invariant state on \(\mathcal A/I\), and let

\[
(\pi_{\bar\omega},\mathcal H_{\bar\omega},\Omega_{\bar\omega})
\]

be its GNS representation. Then

\[
U_t\pi_{\bar\omega}(b)\Omega_{\bar\omega}
:=
\pi_{\bar\omega}(\bar\alpha_t(b))\Omega_{\bar\omega}
\tag{KU6}
\]

extends to a unitary group. If the action is strongly continuous in the GNS
norm, Stone's theorem supplies a self-adjoint generator \(K\) with

\[
U_t=e^{-itK}.
\tag{KU7}
\]

Point-norm continuity of \(\bar\alpha_t\) is a sufficient condition for this
GNS continuity. Only after \(t\) has been identified and normalized as a
physical clock parameter may one define a clock Hamiltonian \(H=\hbar K\).

For \(I\neq0\), the map \(q\) remains noninjective and is not a
\(*\)-isomorphism. After faithful Hilbert-space representations it therefore
cannot be implemented as a unitary equivalence. There is no contradiction:

\[
\boxed{
\text{noninvertible realization }q
\quad\text{and}\quad
\text{reversible unitary quotient flow }U_t
\text{ are different arrows}.}
\tag{KU8}
\]

Nor does the existence of \(q\) produce \(\bar\alpha_t\). The upstream
transformation must preserve the kernel, and an invariant positive state is
needed for this vacuum-preserving GNS implementation. GNS strong continuity
is the additional hypothesis required for a Stone generator. These are the
exact missing steps behind the phrase that nonunitary whole-to-local
realization occurs “so that” local unitarity can appear.

If \(\bar\omega\) is not faithful, its GNS representation can impose a second,
state-dependent null quotient. Thus (KU5) describes the quotient-algebra
symmetry exactly, while the finally represented observable symmetry may be a
further image. Faithfulness removes that additional algebra kernel.

## A semidefinite response selects the same stabilizer structure

The result does not require an algebra ideal. Let \(\mathcal K\) be a complex
vector space with a positive semidefinite Hermitian form \(g\), and put

\[
N:=\operatorname{rad}g
=
\{\xi\in\mathcal K:g(\xi,\eta)=0
\text{ for every }\eta\in\mathcal K\}.
\tag{KU9}
\]

The quotient \(\mathcal K/N\) is a pre-Hilbert space with

\[
\langle[\xi],[\eta]\rangle_g:=g(\xi,\eta).
\tag{KU10}
\]

Let \(\mathcal H_g\) be its completion. If a linear map
\(T:\mathcal K\to\mathcal K\) preserves the form,

\[
g(T\xi,T\eta)=g(\xi,\eta),
\tag{KU11}
\]

then \(T(N)\subseteq N\) and

\[
\bar T[\xi]:=[T\xi]
\tag{KU12}
\]

extends to an isometry of \(\mathcal H_g\). If \(T\) has a form-preserving
inverse, \(\bar T\) is unitary. Hence a form-preserving group on the
prequotient induces a unitary group on the quotient completion even if the
prequotient has no nondegenerate inner product with respect to which that
group could be called unitary.

An upstream inverse is stronger than necessary. Equation (KU11) implies

\[
\{\xi\in\mathcal K:T\xi\in N\}=N,
\qquad
\ker\bar T=0,
\qquad
\operatorname{Ran}\bar T
=
\frac{T(\mathcal K)+N}{N}.
\tag{KU12q}
\]

Indeed, \(T\xi\in N\) gives
\(0=g(T\xi,T\xi)=g(\xi,\xi)\), hence \(\xi\in N\). Consequently the purely
quotient-level condition

\[
\boxed{T(\mathcal K)+N=\mathcal K}
\tag{KU12u}
\]

makes \(\bar T\) a surjective isometry and therefore a unitary on
\(\mathcal H_g\). The original \(T\) may still have a nonzero kernel inside
\(N\) and may fail to be surjective on \(\mathcal K\); all such failure is
invisible after realization. More generally, let \((T_t)_{t\geq0}\) be a
form-preserving semigroup satisfying (KU12u) and the intrinsic
\(g\)-strong-continuity condition

\[
g(T_t\xi-\xi,T_t\xi-\xi)\longrightarrow0
\qquad(t\to0^+,\ \xi\in\mathcal K).
\tag{KU12c}
\]

Its quotient is a strongly continuous unitary semigroup on
\(\mathcal H_g\), which extends to negative parameters by the quotient
inverses even when no upstream inverse exists. This is the exact sense in
which directed prequotient processing can present itself as reversible local
clock transport.

This quotient mechanism is categorically different from
[[directed-isometric-residue-completion/inq|isometric residue completion]]:

\[
\boxed{
\text{quotient: invisible directions are removed},
\qquad
\text{defect completion: missing norm is retained in an added coordinate}.}
\tag{KU12d}
\]

The quotient can support a unitary after its radical is divided out. The
defect column is an isometry before any division and is proper exactly when
the declared transfer is not a coisometry. Neither construction implies a
physical measurement or record. Descent, quotienting, and dilation are
therefore three separate operations even when one programme uses all three.

More generally, the estimate

\[
g(T\xi,T\xi)\leq C^2g(\xi,\xi),
\qquad C\geq0,
\tag{KU12a}
\]

also forces \(T(N)\subseteq N\) and makes \(\bar T\) a bounded quotient
operator with \(\|\bar T\|\leq C\). The case \(C\leq1\) gives a contraction,
not a unitary. This is the appropriate branch for a measured or forgetting
operation whose defect is intended to be nonzero.

More precisely, put

\[
G_g:=\{T\in GL(\mathcal K):g(T\xi,T\eta)=g(\xi,\eta)\},
\qquad
G_g^0:=\{T\in G_g:(T-I)\mathcal K\subseteq N\}.
\]

Then the induced quotient representation has the exact sequence

\[
1\longrightarrow G_g^0
\longrightarrow G_g
\longrightarrow
\operatorname{Im}\!\left(G_g\to U(\mathcal H_g)\right)
\longrightarrow1.
\tag{KU12b}
\]

Thus the linear observable group is literally a stabilizer image modulo
transformations that differ from the identity only along response-null
directions.

For a complex-linear map \(J:\mathcal K\to\mathcal Y\) into a Hilbert space
\(\mathcal Y\), consider the measured response

\[
g(\xi,\eta)
=
\langle J\xi,J\eta\rangle_{\mathcal Y},
\tag{KU13}
\]

one has \(N=\ker J\). The locally visible unitary symmetry that lifts from
the prequotient is therefore the image of the group preserving the response
and its invisible directions. This is the linear carrier version of (KU5).
It also explains why the radical calculation in
[[measured-response-carriers/inq|measured-response carriers]] precedes any
claim about an operator spectrum.

## What this changes in the mass-gap programme

The theorem supplies a rigorous Copernican reversal:

\[
\boxed{
\text{derive the observational kernel and retained form first;}
\quad
\text{then calculate their symmetry stabilizer}.}
\tag{KU14}
\]

This theorem exactly realizes one mathematical sense in which symmetry can be
a grammar of presentation rather than the primitive ontology. It is not yet a
mechanism for positive mass.

The same quotient theorem also describes removal of mere gauge redundancy.
It cannot decide whether a kernel contains physically real upstream
distinctions that become inaccessible, or only multiple names for one object.
That ontological difference requires an independently specified doctrine of
objects and probes; it is not encoded by noninjectivity alone.

- A quotient inner product constructs a carrier but does not select a
  Hamiltonian or make its generator positive.
- Directions in the radical are absent from the retained quotient. A form
  supported only on those discarded directions does not thereby define a
  positive mass-gap form on the retained carrier; another transfer is needed.
- Kernel preservation proves well-defined local dynamics, not locality,
  Poincare covariance, the spectrum condition, or a positive gap.
- A vacuum-only kernel removes exact zero-cost directions. A physical gap
  requires a lower bound relative to a separately declared physical Hilbert
  norm. For bounded \(J\), this is equivalent to closed range and
  bounded-below coverage on the vacuum complement; closable or unbounded maps
  require a form-domain version.

For the current Yang--Mills route, a transformation that fixes one region
must preserve that region's response kernel to act on its quotient. A
Poincare transformation generally moves the region and must instead satisfy
the covariant relation \(U(g)N_B=N_{gB}\); only the region stabilizer preserves
one fixed \(N_B\). The reconstructed global clock action must be unitary on
the completed physical carrier. The categorical measured action has a
different job: it
must preserve that kernel well enough to induce bounded contractions on the
quotient, whose non-scalar defect is then compared with physical energy.
[[contemporary-puzzles/yang-mills-mass-gap/localized-relative-entropy-and-the-energy-solder#The local-unitary bridge has a centralizer kernel|The
local-unitary centralizer theorem]] gives the first falsification test:
regional centralizer and purification directions invisible to the response
must also be null for the categorical defect. Only after that compatibility,
uniform coercivity, OS or direct clock reconstruction, and Poincare recovery
may the physical quotient Hamiltonian carry a mass gap.

[[algebra/nonfaithful-realization|Nonfaithful realization]] owns the
categorical no-equivalence theorem. [[conservation-of-causal-charge/unitarity-and-ontological-time|Unitarity
and ontological time]] owns the distinction between wall loss, local charges,
and directed record extension. Strict [[basic-concepts/descent/inq|descent]]
owns gluing and effectivity; the nonfaithful quotient is an additional
operation, not a consequence of the descent cocycle alone.
