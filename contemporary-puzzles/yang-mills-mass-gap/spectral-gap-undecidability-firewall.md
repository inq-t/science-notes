# Spectral-Gap Undecidability Is Not a Yang--Mills No-Go

The undecidability theorem of Cubitt, Perez-Garcia, and Wolf blocks a universal algorithm for deciding the thermodynamic spectral phase of every Hamiltonian in a specially constructed two-dimensional spin-system family. It neither proves that four-dimensional pure Yang--Mills is undecidable nor rules out a model-specific analytic, geometric, or constructive proof. Its useful Copernican lesson is narrower and stronger: complete local interaction data do not, in unrestricted families, make the global infinite-system spectral phase uniformly computable.

**Status: [EXACT] for the cited undecidability theorem and the quantifier separation below; [METHODOLOGICAL] for its relevance to carrier-first Yang--Mills; [OPEN] for the decidability or independence of the particular Clay problem.**

## The theorem's actual input class

[[library/undecidability-of-the-spectral-gap/inq|Cubitt, Perez-Garcia, and Wolf]] construct a fixed finite local dimension (d) and a computably parameterized family (n\mapsto H(n)) of translationally invariant, nearest-neighbor Hamiltonians on a two-dimensional square lattice. The family has a strong alternative tied to a universal Turing machine:

$$
\begin{array}{ll}
\text{halting branch:} & H(n)\text{ is strongly gapped with a uniform positive lower bound},\\[2mm]
\text{nonhalting branch:} & H(n)\text{ is strongly gapless in the thermodynamic limit}.
\end{array}
\tag{U1}
$$

If an algorithm decided which branch held for every (n), it would decide the halting problem. No such algorithm exists. The full proof also gives, relative to suitable consistent recursively axiomatized formal systems, specially constructed Hamiltonians whose gappedness or gaplessness is independent of that system.

This is a theorem about a **family-decision problem**. It is not a theorem that the spectral predicate lacks a truth value for each member, that physical ontology is stochastic, or that no particular member can be solved.

## The quantifiers do not specialize to Yang--Mills

The invalid inference has the form

$$
\neg\exists\mathsf{Alg}\;\forall H\in\mathcal C:
\mathsf{Alg}(H)=\operatorname{Gap}(H)
\quad\Longrightarrow\quad
\neg\exists\text{ proof of }\operatorname{Gap}(H_{\mathrm{YM}}).
\tag{U2}
$$

The conclusion does not follow. An undecidable predicate on a broad class can be decidable on a distinguished subclass or provable for one distinguished member. A Yang--Mills consequence would require an explicit computable reduction sending arbitrary Turing-machine inputs to four-dimensional pure Yang--Mills theories while preserving the gapped/gapless alternative and the axioms in the Clay target. No such reduction is supplied by the theorem or by [[library/the-unsolvable-problem/inq|the authors' Scientific American account]].

The constructed systems are two-dimensional quantum spin lattices. The Clay target instead asks, for every compact simple gauge group, for a nontrivial continuum Yang--Mills theory on \(\mathbb R^4\) satisfying axioms at least as strong as the Wightman or Osterwalder--Schrader frameworks and having

$$
\sigma(H_{\mathrm{YM}})\cap(0,\Delta)=\varnothing
\quad\text{for some }\Delta>0.
\tag{U3}
$$

[[puzzle-as-posed]] owns that exact target. “No closed-form proof can exist” is therefore not a consequence of undecidability; *closed form* is not the decision predicate proved impossible.

## The genuine global--local lesson

The theorem does expose a structural failure in an unrestricted “shut up and calculate” aspiration:

$$
\boxed{
\text{explicit uniform local rule}
\not\Longrightarrow_{\text{one universal algorithm}}
\text{global thermodynamic spectral phase}.}
\tag{U4}
$$

This does not refute local QFT. It says that the carrier and limit are part of the problem. A finite Hamiltonian matrix is always algorithmically diagonalizable to arbitrary fixed precision; the undecidable property concerns the behavior of a computably specified sequence as system size tends to infinity. Likewise, the Yang--Mills gap belongs to the reconstructed infinite-volume vacuum representation, not to the classical density \(\operatorname{Tr}F^2\), a finite lattice Hessian, or a list of local couplings by itself.

The constructive response is not to abandon rigor but to seek a Yang--Mills-specific global certificate: reflection-positive reconstruction, complete physical-carrier coverage, and a volume- and cutoff-uniform coercive estimate. [[carrier-first-reversal]] states that proof architecture.

## Stopping rule

The undecidability claim may enter a Yang--Mills theorem only after one of two return values exists:

1. a genuine computable reduction proving undecidability for the precise Yang--Mills class; or
2. a model-specific global certificate proving the requested Yang--Mills construction and gap.

At present neither has been supplied by the undecidability literature. The Scientific American headline is therefore a warning about universal algorithms, not evidence that the Millennium problem is doomed or must be replaced.

