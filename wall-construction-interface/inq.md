---
inq.module: "wall-construction-interface"
inq.include:
  - "**/*.md"
inq.ambient:
  - "**/*.py"
---
# The Wall-Construction Interface

Every programme that treats physical scale as displacement through quantum state space presupposes the same construction obligation: a family of causal-region algebras and states indexed by scale, carrying enough transport structure to make cross-scale comparison well typed. An exact core-spectral construction now supplies a continuous algebraic pre-wall with cuts, states, transport, readout, and nonzero Fisher--BKM response without measured gravity or a fitted history. It does not yet supply Lorentzian regions, a local causal net, renormalized sources, or area. This module states the full physical object once, records what the pre-wall closes, and fixes the tests its realization must pass.

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
\{(\mathcal B_{N,x},E_{N,x})\},\
\{J^{\rm TT}_N,\Delta_N\},\
\{\iota_{N_2:N_1}\},\
\Phi,\
\{u_{N_2:N_1}(s)\},\
\mathscr T=\{T_\alpha\}
\bigr),
$$

whose slots carry separate obligations:

| Slot | Object | Obligation |
|---|---|---|
| $D_N,\mathcal H_N,\Sigma_N$ | observer-accessible causal region, its horizon or boundary, and a selected codimension-two cut | construct the family; state what selects the cut; declare whether the region depends on a solved background |
| $\mathcal A_N(O)$ | local von Neumann algebra of a subregion | isotony, locality, covariance, an appropriate time-slice property |
| $\omega_N$ | faithful normal state | faithfulness, normality, and the declared standard form needed for modular theory; Hadamard or microlocal admissibility where renormalized local sources are used; a physical selection rule |
| $(\mathcal B_{N,x},E_{N,x})$ | observable context and conditional expectation, or a declared substitute instrument | construct the context family and prove state preservation and modular admissibility; do not infer an expectation from commutativity alone |
| $J^{\rm TT}_N,\Delta_N$ | Tomita conjugation and modular operator in a specified standard form | fix the standard form; do not conflate $J^{\rm TT}_N$ with a geometric reflection |
| $\iota_{N_2:N_1}$ | identification, embedding, or transport of observables between fibers | a composition law, and control of gauge and holonomy |
| $\Phi$ | the scale-to-state law $N\mapsto\omega_N$ | specified independently of the response it is meant to explain |
| $u_{N_2:N_1}(s)$ | relative modular data on a common algebra | defined only after transport; ratio dependence and regularity proved, not assumed |
| $\mathscr T=\{T_\alpha\}$ | renormalized source family, including the local Weyl-source direction and any TT source claimed by a tensor member | locality, covariance, scaling, source domains, and metric-variation ambiguities declared; a scalar-only realization need not supply a TT member |

The symbol W0 names one shared package, not one atomic theorem. Its slots fall into independently testable gates:

| Gate | Owned construction |
|---|---|
| W0a — carrier | regions, boundaries and cuts, local net, standard form, and modular data |
| W0b — state law | faithful regular states and a scale-to-state law selected independently of the target observable |
| W0c — transport | embeddings or correspondences, composition, and controlled holonomy |
| W0d — readout | contexts plus state-compatible expectations or declared instruments |
| W0e — source readiness | localized renormalized scalar sources and any independently claimed TT source, with domains and ambiguities |

The physical quotient is downstream programme-core data, not a hidden sixth W0 slot. A full response member must use it, but the wall package does not get to define physical nullity by itself.

**[OPEN CONSTRUCTION — PHYSICAL W0 WELD]** No dynamical FLRW instance of $\mathfrak W$ has been constructed. [[core-spectral-wall|The core spectral wall]] now constructs one continuous algebraic pre-wall from the canonical core of a type-$\mathrm{III}_1$ factor. Its capacity subpackage has exact nested spectral cuts and finite corners; its response subpackage has labelled whole-core fibers, one global faithful state, coherent dual-flow transport, state-preserving binary expectations, and a nonzero Fisher--BKM member. The binary context is not inside the finite corner, and the note keeps those carriers separate. The construction uses neither measured $G$ nor a fitted expansion history. Its projector $e_N$ is not a Lorentzian codimension-two cut $\Sigma_N$, neither core carrier is a local causal net, and its logistic density is a selected exact member rather than a uniqueness theorem. [[half-sided-modular-tunnel|The half-sided modular tunnel]] independently supplies positive orientation, while [[finite-cellular-markov-wall|the finite cellular Markov wall]] remains a useful finite source benchmark. The keystone remainder is now the realization of the algebraic pre-wall as causal geometry and local field theory, followed by W0e renormalized source readiness and the independent area weld.

## The algebraic pre-wall now exists

The exact constructed return is

$$
N
\longmapsto
\bigl(e_N,\mathcal A_N,\omega_N,
\mathcal K_N,\iota_{N_2:N_1},\mathcal B_N,E_N\bigr),
$$

where $\mathcal A_N=\mathcal C^{(N)}$ is the whole-core response fiber and $\mathcal K_N=e_N\mathcal C e_N$ is the finite capacity corner. The context $\mathcal B_N=W^*(e_N)$ lies in $\mathcal A_N$, not $\mathcal K_N$. With $\tau(e_N)=e^N$, an optional logistic readout has binary response $\nu^2\operatorname{sech}^2(\nu(N-N_c))$. This closes the former claim that no genuine cross-scale algebra--state--transport family had been constructed. It does **not** fill the geometric entries $D_N,\mathcal H_N,\Sigma_N$, the local-net dependence $O\mapsto\mathcal A_N(O)$, the physical state-selection rule, or the source family $\mathscr T$. The correct dependency is now

$$
\boxed{
\text{algebraic pre-wall}
\longrightarrow
\text{causal and local realization}
\longrightarrow
\text{source, area, gravity, and record welds}.}
$$

[[scale-character-solder|The scale-character solder]] gives an exact optional matching of core trace capacity, HSMI affine scale, and $A_2$ discriminant depth. Its physical naturality is part of the middle arrow, not a consequence of matching three formulas.

The new expectation slot is restrictive. A faithful state-preserving normal expectation onto a von Neumann subalgebra requires invariance under the state's modular automorphism group. A generic commutative context therefore need not admit the exact wall map. [[spectral-wall-descent/conditional-expectation-balance|The conditional-expectation balance]] gives the finite theorem, its BKM split, and the alternatives when this modular gate fails.

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

[[vertical-and-horizontal-motion|Vertical and horizontal motion]] fixes the recurring type distinction, while [[state-coordinate-types|the state-coordinate ledger]] separates a family label, a transported comparison coordinate, and a spacetime field. If Euclidean periodicity is proposed as a rate selector, [[euclidean-monodromy-and-rate|the monodromy conjecture]] states the additional transport theorem it would need.

### Correspondence upgrade

An embedding \(\iota_{N_2:N_1}\) is too restrictive when the algebra itself changes across scale. A microscopic member may instead supply a von Neumann correspondence

$$
{}_{\mathcal A_{N_2}(O)}X_{N_2:N_1}{}_{\mathcal A_{N_1}(O)}
$$

with coherent Connes fusion

$$
X_{N_3:N_2}
\boxtimes_{\mathcal A_{N_2}}
X_{N_2:N_1}
\simeq
X_{N_3:N_1}.
$$

The embedding slot should then be read as the representable special case of this correspondence transport. A finite-index candidate gravitational expectation can live at an intermediate noncommutative stage, while the final type-III-to-commutative factual descent remains generally infinite index. [[spectral-wall-descent/scale-correspondence-stack|The scale-correspondence prestack]] gives the present typing, and [[spectral-wall-descent/finite-index-area-weld|the finite-index area weld]] gives a scoped exact type-I product-cell model plus an open area weld.

This upgrade does not add a tenth independent return value to \(\mathfrak W\); it strengthens the transport slot. [[spectral-wall-descent/scale-correspondence-stack|The candidate correspondence prestack]] is denoted \(\mathfrak X_{\mathrm{corr}}\) and fills only the presentation and transport portion of this package. A candidate must still specify how regions, cuts, states, readouts, source tangents, and spectral data are induced across the correspondence before it realizes the full interface.

## One tangent space, two consumers

Write the scale variation of a positive scale section against a homogeneous reference as

$$
-\delta\ln\sigma(x)=\delta N+\zeta_{\rm wall}(x),
\qquad
\int_\Sigma\zeta_{\rm wall}=0 .
$$

The two summands are different directions in one presented scale tangent at $\bar\sigma$,

$$
T_{\bar\sigma}\mathfrak{Sc}(\Sigma)
\simeq\mathbb R\oplus C^\infty(\Sigma)/\mathbb R .
$$

The homogeneous response programme consumes the first summand; the primordial spectral programme consumes the second after the physical quotient and observational readout have been constructed. [[program-core/contextual-descent-from-homogeneity|Contextual descent]] sharpens the meaning of the second: it can be a nonconstant direction of observational differentiation rather than a lumpy direction in a fundamental spatial substrate. This is the structural reason the two programmes keep rewriting the same preamble: they are two consumers of one descent datum.

The design consequence is sharp. An interface built only for the homogeneous consumer may retain $\Sigma_N$ merely as an area — enough for an entropy normalization — and would then be unable to serve the spectral consumer at all. The shared package must therefore retain the field content on $\Sigma_N$, together with the quotient by constants that removes the homogeneous redundancy, even when the immediate caller integrates it away.

At a homogeneous and isotropic reference, invariance of the response form forces orthogonality when the global singlet and mean-zero observational sectors carry inequivalent representations. This is a **[CONDITIONAL THEOREM — UNDER THE REPRESENTATION HYPOTHESES]**, not a property of the direct-sum notation itself. A vanishing quadratic mixed block does not separate their origins: the first allowed common response may be the cubic tensor \(\nabla_NG_{\zeta\zeta}\). Mixed quadratic terms may also survive at boundaries, after pointing, away from the symmetric reference, or when the representation hypotheses fail.

What the shared construction must expose is one center-resolved response package

$$
\mathfrak G^Z_{\Sigma,N}
=
\left(
Z(\mathcal M_{\Sigma,N}),
\mathbf G^Z,
\omega^Z_N
\right),
$$

with correspondingly different blocks in the two tangent sectors:

$$
\text{homogeneous:}\quad
v_N\in H^{\mathrm{phys}}_{\Sigma,\mathrm{hom}},
\qquad
\mathbf G^Z_{NN};
$$

$$
\text{nonconstant observational:}\quad
H^{\mathrm{phys}}_{\Sigma,\mathrm{obs},0}
\equiv H^{\mathrm{phys}}_{\Sigma,\mathrm{inh}},
\qquad
\mathbf G^Z_{\zeta\zeta}
\quad\text{when the regular response exists.}
$$

The right-hand tangent symbol is retained as CWST's historical consumer notation; it must not be read as an assertion of microscopic spatial inhomogeneity. [[program-core/center-valued-response|Center-valued response and scalarization]] owns the central-score Fisher term and the available evaluation policies. A scalar \(G_{NN}\) or \(G_{\zeta\zeta}\) is returned only when the center is trivial or the member declares normal unconditioned evaluation, a conditional sector theorem, or a later factive instrument. The normal law \(\omega^Z_N:=\omega_N|_Z\) inherited from the faithful wall state gives an unconditioned average, not an outcome.

Both response blocks depend on the same nine interface slots and are undefined before cross-fiber transport, observational descent, and the physical quotient exist. [[program-core/common-response-form|The common-response construction]] owns their common positive form and mixed-jet gate; [[hessian-response-geometry/inq|Hessianity]] and [[spectral-wall-descent/hidden-resolvent-and-seesaw|hidden-mode reduction]] are separate downstream questions. A selected CST member independently supplies the scale-state rate, contracts the homogeneous block along its declared scale tangent, and applies [[program-core/ruble-equations#RE6 — Integrated reference matching|the RE6 reference matching ratio]]. CWST owns the conjectural BKM-to-spectral transfer and curvature realization. The interface returns neither a primordial precision nor a gauge-invariant cosmological mode.

## Two completion levels

A programme built on this interface may honestly stop at either level, provided it names the level it has reached.

**Interface completion.** Take established local quantum field theory as the fiber theory and construct a universal horizontal geometry over its admissible states. The primitive datum may then be a positive functional — a cut-integrated capacity ratio, or a precision kernel — postulated by an independent law rather than computed from a realized algebra. This level still owes an independent statement of that law and a demonstration that it couples consistently to gravity.

**Microscopic completion.** Construct a particular wall algebra and state family that *calculates* the return values above, and prove whatever continuation carries them to observables. This is strictly stronger, and it is not required merely to formulate an autonomous interface theory.

The distinction matters because the two levels have different burdens of proof and different falsifiers, and because a document that argues at the first level while phrasing its results in the vocabulary of the second will read as more complete than it is.

## An optional reduction that is assumed, not derived

The homogeneous CST member currently routes its response through a single binary generator associated with the two null-normal orientations of a codimension-two cut. The algebra that follows once that reduction is granted is exact and is kept in [[binary-information-geometry/inq|binary information geometry]]. What is *not* granted — that the two orientation sectors exhaust the selected image, that a large type-III local algebra reduces to this channel at all, that geometric reflection may be identified with Tomita conjugation, and that the reference weights are balanced — is collected in [[binary-channel|the binary channel obligation]]. [[a2-ternary-response/inq|The \(A_2\) ternary test]] supplies an exact neutral-sector countermodel to automatic exhaustivity. CWST requires a physical mean-zero observational response sector but does not require this binary reduction unless a particular CWST member explicitly adds it.

The word "rank one" is used across the archive for reductions that do not imply one another: one noncentral horizontal generator, one common material clock, and one spin-zero stress form factor. The first is an obligation only for a binary wall member. The other two are consumer-side assumptions and should be argued where they are used.

## What makes a construction explanatory

Two independent tests separate a construction that explains from one that redescribes. The first forbids obtaining the horizontal law by solving backward from the history or spectrum it is meant to predict. The second requires that adding the interface not disturb the local physics it claims to import. A candidate can pass either while failing the other, so they must be checked separately; both are stated in [[elimination-test|the elimination tests]].

Because the dynamical case makes every slot nontrivial at once, the credible route is incremental. [[construction-ladder|The construction ladder]] orders five settings by which slot first becomes hard, so that a failure localizes to an ingredient instead of to the programme.
