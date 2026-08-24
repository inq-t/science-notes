# The Wall-Construction Interface

Every programme that treats physical scale as displacement through quantum state space presupposes the same unconstructed object: a family of causal-region algebras and states indexed by scale, carrying enough transport structure to make cross-scale comparison well typed. This module states that object once, enumerates what must be supplied before relative entropy, a Connes cocycle, or a BKM norm may be written at all, and fixes the tests a candidate construction must pass. It derives no cosmology and predicts no spectrum. Its purpose is to be the shared dependency of the homogeneous response programme and the primordial spectral programme rather than a third private copy of their common preamble.

Claim labels follow [[program-core/axioms-and-principles#Status vocabulary|the programme-wide claim-status vocabulary]].

## The interface is a dependency, not a theory

The module admits two kinds of import: standard operator-algebraic and conformal-geometric results, and the exact reduced algebra of an already-granted channel. It admits no import from either consumer. Concretely, no statement here may mention $\rho_X$, $w_X$, $\Delta_\zeta^2(k)$, $H(z)$, a benchmark abundance, or a fitted equation of state. Those belong to the programmes that call this interface, and a construction obligation stated in terms of them would silently be the circularity that [[elimination-test|the elimination tests]] exist to forbid.

The consequence for the graph is that arrows point one way:

$$
\begin{aligned}
\text{standard AQFT, modular theory, conformal geometry}
&\longrightarrow \mathfrak W\\
\mathfrak W &\longrightarrow \text{homogeneous response programme}\\
\mathfrak W &\longrightarrow \text{primordial spectral programme}
\end{aligned}
$$

A construction obligation that cannot be stated without naming a consumer's observable is misfiled and belongs in that consumer.

## The minimal package

A scale-indexed interface is the tuple

$$
\mathfrak W=
\bigl(
\{D_N,\mathcal H_N,\Sigma_N\},\
\{\mathcal A_N(O)\},\
\{\omega_N\},\
\{J^{\rm TT}_N,\Delta_N\},\
\{\iota_{N_2:N_1}\},\
\Phi,\
\{u_{N_2:N_1}(s)\},\
T
\bigr),
$$

whose slots carry separate obligations:

| Slot | Object | Obligation |
|---|---|---|
| $D_N,\mathcal H_N,\Sigma_N$ | observer-accessible causal region, its horizon or boundary, and a selected codimension-two cut | construct the family; state what selects the cut; declare whether the region depends on a solved background |
| $\mathcal A_N(O)$ | local von Neumann algebra of a subregion | isotony, locality, covariance, an appropriate time-slice property |
| $\omega_N$ | faithful normal state | microlocal or Hadamard regularity sufficient for modular theory; a physical selection rule |
| $J^{\rm TT}_N,\Delta_N$ | Tomita conjugation and modular operator in a specified standard form | fix the standard form; do not conflate $J^{\rm TT}_N$ with a geometric reflection |
| $\iota_{N_2:N_1}$ | identification, embedding, or transport of observables between fibers | a composition law, and control of gauge and holonomy |
| $\Phi$ | the scale-to-state law $N\mapsto\omega_N$ | specified independently of the response it is meant to explain |
| $u_{N_2:N_1}(s)$ | relative modular data on a common algebra | defined only after transport; ratio dependence and regularity proved, not assumed |
| $T$ | renormalized operator proposed to generate a local Weyl-source direction | locality, covariance, scaling, and metric-variation ambiguities declared |

**[OPEN CONSTRUCTION — WALL STRUCTURE]** No dynamical FLRW instance of $\mathfrak W$ has been constructed. This single gap is the common ancestor of the open problems recorded downstream in both programmes; it is not two independent gaps that happen to resemble each other.

## Why a derivative of the state family is not yet defined

Different $N$ generally means a different region and possibly a different algebra. The expression

$$
\partial_N\omega_N
$$

is therefore not yet a tangent vector but a difference between elements of distinct state spaces. Araki relative entropy and the Connes cocycle both compare two states on **one** von Neumann algebra, so the notation

$$
[D\omega_{N_2}:D\omega_{N_1}]_s
$$

presupposes that $\mathcal A_{N_1}$ and $\mathcal A_{N_2}$ have already been placed on common ground. Until $\iota_{N_2:N_1}$ is supplied, a horizontal BKM norm is not a small quantity awaiting calculation; it is an undefined symbol. The available transport strategies, the decomposition that isolates the physically load-bearing part of the comparison, and the failure modes of each are developed in [[cross-fiber-transport|cross-fiber transport and state selection]].

[[vertical-and-horizontal-motion|Vertical and horizontal motion]] fixes the recurring type distinction, while [[state-coordinate-types|the state-coordinate ledger]] separates a family label, a transported comparison coordinate, and a spacetime field. If Euclidean periodicity is proposed as a width selector, [[euclidean-monodromy-and-width|the monodromy conjecture]] states the additional transport theorem it would need.

## One tangent space, two consumers

Write the scale variation of a positive scale section against a homogeneous reference as

$$
-\delta\ln\sigma(x)=\delta N+\zeta_{\rm wall}(x),
\qquad
\int_\Sigma\zeta_{\rm wall}=0 .
$$

The two summands are different directions in one tangent space at $\bar\sigma$,

$$
T_{\bar\sigma}\mathfrak{Sc}(\Sigma)
\simeq\mathbb R\oplus C^\infty(\Sigma)/\mathbb R .
$$

The homogeneous response programme consumes the first summand; the primordial spectral programme consumes the second. This is the structural reason the two programmes keep rewriting the same preamble: they are the two halves of a single decomposition, and each has been carrying its own copy of the shared part.

The design consequence is sharp. An interface built only for the homogeneous consumer may retain $\Sigma_N$ merely as an area — enough for an entropy normalization — and would then be unable to serve the spectral consumer at all. The shared package must therefore retain the field content on $\Sigma_N$, together with the quotient by constants that removes the homogeneous redundancy, even when the immediate caller integrates it away.

At a homogeneous and isotropic reference, invariance of the response form under the reference symmetry can force orthogonality when the homogeneous and inhomogeneous sectors carry inequivalent representations. This is a **[CONDITIONAL THEOREM — UNDER THE REPRESENTATION HYPOTHESES]**, not a property of the direct-sum notation itself. Mixed terms may survive if those hypotheses fail, and they may return beyond quadratic order or on an inhomogeneous background.

What the shared construction must expose is correspondingly different in the two sectors:

$$
\text{homogeneous:}\quad
v_N\in H^{\mathrm{phys}}_{\Sigma,\mathrm{hom}},
\qquad
G^{\mathrm{BKM}}_{NN};
$$

$$
\text{inhomogeneous:}\quad
H^{\mathrm{phys}}_{\Sigma,\mathrm{inh}},
\qquad
G^{\mathrm{BKM}}_{\zeta\zeta}
\quad\text{when the regular response exists.}
$$

Both response blocks depend on the same eight interface slots and are undefined before cross-fiber transport and the physical quotient exist. The homogeneous consumer owns the further contraction into \(\nu\) and [[program-core/ruble-equations#RE6 — Integrated crossing capacity|the RE6 crossing capacity]]. CWST owns the conjectural BKM-to-spectral transfer and curvature realization. The interface returns neither a primordial precision nor a gauge-invariant cosmological mode.

## Two completion levels

A programme built on this interface may honestly stop at either level, provided it names the level it has reached.

**Interface completion.** Take established local quantum field theory as the fiber theory and construct a universal horizontal geometry over its admissible states. The primitive datum may then be a positive functional — a cut-integrated capacity ratio, or a precision kernel — postulated by an independent law rather than computed from a realized algebra. This level still owes an independent statement of that law and a demonstration that it couples consistently to gravity.

**Microscopic completion.** Construct a particular wall algebra and state family that *calculates* the return values above, and prove whatever continuation carries them to observables. This is strictly stronger, and it is not required merely to formulate an autonomous interface theory.

The distinction matters because the two levels have different burdens of proof and different falsifiers, and because a document that argues at the first level while phrasing its results in the vocabulary of the second will read as more complete than it is.

## An optional reduction that is assumed, not derived

The homogeneous CST member currently routes its response through a single binary generator obtained from the two null-normal orientations of a codimension-two cut. The algebra that follows once that reduction is granted is exact and is kept in [[binary-information-geometry/entry|binary information geometry]]. What is *not* granted — that a large type-III local algebra reduces to this channel at all, that geometric reflection may be identified with Tomita conjugation, and that the reference weights are balanced — is collected in [[binary-channel|the binary channel obligation]]. CWST requires a physical inhomogeneous response sector but does not require this binary reduction unless a particular CWST member explicitly adds it.

The word "rank one" is used across the archive for reductions that do not imply one another: one noncentral horizontal generator, one common material clock, and one spin-zero stress form factor. The first is an obligation only for a binary wall member. The other two are consumer-side assumptions and should be argued where they are used.

## What makes a construction explanatory

Two independent tests separate a construction that explains from one that redescribes. The first forbids obtaining the horizontal law by solving backward from the history or spectrum it is meant to predict. The second requires that adding the interface not disturb the local physics it claims to import. A candidate can pass either while failing the other, so they must be checked separately; both are stated in [[elimination-test|the elimination tests]].

Because the dynamical case makes every slot nontrivial at once, the credible route is incremental. [[construction-ladder|The construction ladder]] orders five settings by which slot first becomes hard, so that a failure localizes to an ingredient instead of to the programme.
