---
inq.module: "complex-presentation-without-polarization"
inq.include:
  - "**/*.md"
---
# Complex Presentation Without Polarization

An integrable complex geometry can be an ontologically complete mode of presentation without being Kähler, polarized, probabilistic, or already spacetime. The geometric six-sphere construction reviewed here uses a torus family, monodromy, logarithmic twists, and a toric cusp filling; an inspected but not locally executed Lean source supplies a distinct formal presentation. Its lack of a compatible Kähler polarization does not erase the complex geometry; it shows that complex presentation, positive quantum-state geometry, real-form selection, factive descent, and Lorentzian realization must be constructed as distinct structures.

## The meaning of complex presentation

An almost-complex structure on a smooth real $2n$-manifold is a smooth endomorphism

$$
J:TX\longrightarrow TX,
\qquad
J^2=-\mathbf 1.
$$

The complexified tangent splitting

$$
T_{\mathbb C}X
=T^{1,0}X\oplus T^{0,1}X
$$

already exists for an almost-complex structure. Integrability is the stronger condition \(N_J=0\). The Newlander--Nirenberg theorem then supplies local complex coordinates with holomorphic transition maps; the extra bidegree components of \(\mathrm d\) vanish, so

$$
\mathrm d=\partial+\bar\partial,
\qquad
\bar\partial^2=0.
$$

The underlying smooth cycles do not change merely because \(J\) is integrable. Their analytic types, periods, and admissibility for holomorphic constructions can change, as do the allowable functions, differential operators, and gluing laws.

On the programme's mathematical realism, that complex structure is as real as a Lorentzian metric or an operator algebra. But reality does not abolish type. A complex atlas is not yet a Hilbert space of states, a positive information metric, a selected real locus, or a causal history.

## The new $S^6$ return value

The Alpöge-hosted manuscript audited in [[algebra/s6-manuscript-branch|the integrable $S^6$ branch]] constructs a compact complex threefold

$$
f:X\longrightarrow\mathbb P^1
$$

that is diffeomorphic to $S^6$. Its generic fibers are complex two-tori. The two exceptional fibers have multiplicities \(3\) and \(4\), with local monodromies of orders \(3\) and \(4\). At the cusp the manuscript uses unipotent monodromy, logarithmic transformations, and an \(A_2\)-triangulated toric degeneration. The resulting cusp fiber \(W\) is non-normal: its normalization is a degree-six del Pezzo surface whose opposite boundary curves are identified.

[[library/complex-structures-on-s6-engel/inq|Engel gives a shorter self-contained geometric proof]] of the same construction; this is not an unrelated geometric route. [[library/formalization-of-the-hopf-problem/inq|The separate public Lean source]] transports a complex atlas by a homeomorphism to the standard topological unit sphere. Compatibility with a preassigned standard smooth atlas is not the target of that formal snippet; the geometric recognition argument supplies the smooth existence conclusion. The displayed axiom list is a comment recording expected output, not an independently executed dependency report, and the comparator configuration is not an execution receipt. This workspace has statically audited but not locally rebuilt the artifact. Manuscript-specific Hodge, polarization, and automorphism computations remain source-specific claims unless separately verified. [[algebra/s6-manuscript-branch|The branch note]] owns this evidence boundary.

Its philosophical force is substantial. It exhibits one compact smooth object whose complex presentation is created globally by monodromy and singular gluing rather than by choosing a complex coordinate independently at every point. The geometry is simple locally and nontrivial in the way its local pieces continue around exceptional loci.

The arithmetic spine should not be mistaken for a second global symmetry group. The $GL_4(\mathbb Z)$ matrices act as monodromy on the first-homology lattice of the complex two-torus fibers; they need not act as automorphisms of the completed threefold. Nor is that lattice a microscopic spacetime lattice. The root object is mixed descent data: a varying holomorphic torus family, its integral local system, singular fillings, and compatibility maps. [[contemporary-puzzles/yang-mills-mass-gap/s6-descent-defect-and-the-chirality-firewall|The $S^6$ descent-defect audit]] isolates both the exact finite projection-and-quotient pattern and the automorphic-Casimir route by which a discrete global admissibility condition could constrain the spectrum of a smooth local operator.

## Why wave functions make this compelling

Quantum mechanics uses complex amplitudes essentially: relative phase affects interference even when absolute phase does not. In the Bargmann representation, ordinary oscillator states can be represented by holomorphic functions whose Hilbert norm is a real \(2n\)-dimensional integral over \(\mathbb C^n\), not a holomorphic period integral. More generally, geometric quantization represents states by sections of a complex line bundle after a polarization has selected the admissible directions. Because \(S^6\) admits no symplectic form, that conventional quantization cannot take the compact sphere itself as its symplectic phase space.

This makes a fundamental complex threefold more than numerology. It supplies the kinds of objects from which holomorphic sections, period integrals, analytic continuation, and monodromy representations can be built. [[holomorphic-wavefunctions|Holomorphic wave functions and complex integrals]] states this connection precisely.

The implication is nevertheless one-way:

$$
\boxed{
\text{integrable complex geometry}
\Longrightarrow
\text{holomorphic analytic machinery is available},}
$$

not

$$
\text{integrable complex geometry}
\Longrightarrow
\text{a quantum theory has been derived}.
$$

A wave function is normally a vector or ray in a complex Hilbert space, often realized as a section. A complex manifold by itself supplies neither the Hilbert norm nor the operator algebra, state, Hamiltonian or Dirac operator, Born rule, and observable representation needed to give that section quantum meaning.

## Holomorphic locality is not yet a QFT net

Integrability supplies the contravariant commutative sheaf

$$
U\longmapsto\mathcal O_X(U).
$$

A local quantum field theory instead supplies a covariant net or factorization structure of generally noncommutative operator algebras,

$$
O\longmapsto\mathcal A(O)\subset B(\mathcal H),
$$

together with adjoints, positivity, a state, causal locality, and physical dynamics. Holomorphic functions are not closed under complex conjugation, so $\mathcal O_X(U)$ is not even naturally the required $C^*$-algebra. On compact connected $X$, the global holomorphic functions are only constants.

The precise charitable reading is that an integrable $J$ may provide the *grammar of compatible local complex presentation*. A quantization or realization functor must still construct the local quantum algebras:

$$
\mathcal O_X
\dashrightarrow
\left(O\mapsto\mathcal A(O),\omega,\mathcal H,H\right).
$$

[[the-grain-of-causal-scale/inbox/causal-grain-and-the-yang-mills-gap/s6-complex-presentation-and-the-determinant-fork|The determinant-fork exploration]] asks what extra structure would be required for that grammar to contribute a physical spectral number.

## The absence of polarization is a type lesson

The manuscript computes an invariant Hodge form of signature \((1,1)\) on the rank-two Hodge bundle and concludes that the family has no monodromy-compatible polarization and no \(Q_0\)-polarized limiting mixed Hodge structure. The indefinite form therefore cannot directly serve as a positive BKM metric on that full bundle. The proposed equality is also ill-typed until a map from Hodge data to state tangents has been constructed. A separately selected positive subquotient is not ruled out, but its positivity and monodromy compatibility would be new obligations.

It does not show that the complex presentation is defective. Nor does it prevent the manifold from carrying ordinary positive Hermitian metrics. It shows that one form cannot do every job. [[polarization-and-positive-state-geometry|Polarization and positive state geometry]] separates the relevant objects:

$$
\begin{aligned}
(X,J,f,\rho_{\mathrm{mon}})
&\quad &&\text{complex presentation and monodromy},\\
(\mathcal A,\omega,g_{\mathrm{BKM}})
&\quad &&\text{positive state-space distinguishability},\\
(X,\tau,X^\tau)
&\quad &&\text{selected real form},\\
(\mathsf{LorHist}_3,g_{\mathrm L})
&\quad &&\text{factive Lorentzian histories}.
\end{aligned}
$$

No equality between these rows is licensed by their common dimensionality or by the word *geometry*. The programme needs realization maps relating them.

## $A_2$ is a motif, not yet one object

The manuscript's $A_2$ is a triangular root-lattice combinatorics used in its toric cusp filling. [[algebra/a2-inverse-cover|The $A_2$ inverse cover]] instead concerns the analytic cuspidal discriminant and a degree-three cover with $S_3=W(A_2)$ sheet monodromy. These are not already the same family.

Their common lesson is more abstract and more durable: locally simple branches can acquire global individuality through monodromy, degeneration, and nontrivial gluing. [[a2-ternary-response/inq|The $A_2$ ternary-response module]] asks what state geometry arises when three such branches are treated before a binary wall has selected two of them.

## Consequence for the larger programme

The useful ontological proposal is not that an \(S^6\) wave function collapses into spacetime. It is that several regimes can be equally mathematical and equally real while occupying different categorical levels:

$$
\boxed{
\text{atemporal complex presentation}
\xrightarrow{\ \mathfrak S\ }
\text{positive spectral/state geometry}
\xrightarrow{\ \mathfrak R\ }
\text{selected real form}
\xrightarrow{\ \mathfrak F\ }
\text{factive records}
\xrightarrow{\ \mathfrak L\ }
\text{Lorentzian history}.}
$$

Here \(\mathfrak S,\mathfrak R,\mathfrak F,\mathfrak L\) are construction targets, not decorative arrows. The first would associate an algebra, spectral family, and faithful states to the complex presentation. The second would select an antiholomorphic real form. The third would be a genuinely noninvertible fact-producing operation; a semilinear involution alone cannot do that. The fourth is the Lorentzian-history realization described in [[algebra/real-forms-and-factive-spacetime|real forms and factive spacetime]].

This architecture permits an atemporal internal regime. Complex integrals and spectral principles can compare or weight complete configurations without being evolution in a pre-existing time. Time may enter only when compatible records become composable Lorentzian histories. That is a **[PROJECT INTERPRETATION]**, not a consequence of complex integrability alone.

## Failure conditions

- If a manuscript-specific invariant fails separate audit, only the downstream claims using that invariant are affected directly. The geometric existence argument and the inspected, not locally executed, formal source require their own evidence assessment; agreement of presentations is not an independent execution receipt.
- If no algebra, spectral family, or faithful state bundle is constructed from $X$, the quantum reading remains analogy.
- If the state bundle is added arbitrarily, it explains no more than an independently postulated quantum model.
- If no antiholomorphic involution with a suitable fixed locus exists, complex dimension three does not yield physical three-space.
- If no fact-producing realization functor constructs causal composition, the complex geometry does not derive time or $3+1$ spacetime.
- If the manuscript's toric $A_2$ and the analytic $A_2$ inverse cover are identified without a map of families and monodromy, the synthesis is a homonym.

The sources and their exact roles are recorded in [[sources|the source ledger]].
