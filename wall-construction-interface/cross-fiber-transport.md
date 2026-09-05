# Cross-Fiber Transport and State Selection

Comparing states attached to different scales requires two things that are usually assumed: a transport placing them on a common algebra, and a rule selecting the state at each scale in the first place. Both are substantive and neither implies the other. Half-sided-modular transport, functorial core maps, and one exact core-spectral pre-wall show that continuous transport and nonzero state response are mathematically attainable together. Their realization as a local Lorentzian wall and their physical state-selection rule remain additional constructions.

## The transport problem

Let $N\mapsto(\mathcal A_N,\omega_N)$ be the intended family. Relative entropy and the Connes cocycle are defined for two states on one von Neumann algebra, so before any cross-scale quantity is written, one of the following must be supplied:

- **embeddings** $\iota_{N_2N_1}:\mathcal A_{N_1}\to\mathcal A_{N_2}$, with a composition law $\iota_{N_3N_2}\circ\iota_{N_2N_1}=\iota_{N_3N_1}$;
- a **common ambient algebra** into which every $\mathcal A_N$ embeds;
- a **crossed-product or core construction** on which the relevant states become comparable;
- a **modular Berry connection** or parallel transport, with its gauge dependence and holonomy controlled.

These are not equivalent. An inclusion of regions gives isotony for free but changes which observables exist; a common ambient algebra buys comparability at the cost of specifying that ambient object; a crossed product changes the algebra type and introduces its own dressed observables; a connection defines transport only up to holonomy, which must then be shown negligible or accounted for.

## A compact commutative benchmark

[[conditional-fisher-coercivity/measure-preserving-horizontal-lifts|A smooth conditional family]] admits an exact connection with \(dP=PD\), even when that connection has curvature. [[conditional-fisher-coercivity/bounded-transport-and-cut-flux|Cut-flux duality]] determines whether the required law-preserving transport is bounded in the declared metrics. This is a concrete commutative transport instance, not a type-III or Lorentzian wall construction.

The connection transports the conditional law to itself while moving the probes. A score in a fixed presentation can therefore be nonzero even though the law is constant under that transport. Neither this score nor its cut quotient is automatically the physical horizontal BKM tangent selected by RE1--RE2. State selection, choice of connection, response interpretation and physical realization remain distinct.

## Exact transport constructors

The first exact constructor is a reconstructed half-sided-modular tunnel. Given one half-sided modular inclusion, [[half-sided-modular-tunnel|the tunnel theorem]] defines

$$
\mathcal A_r=\operatorname{Ad}U(r)(\mathcal M),
\qquad
\iota_{r_2:r_1}
=\operatorname{Ad}U(r_2-r_1)|_{\mathcal A_{r_1}},
$$

and proves that the maps are onto their stated fibers and compose exactly. This closes W0c for that reconstructed family. It does not prove that an independently proposed cosmological family is the same tunnel, and the invariant reference state supplied with the inclusion is horizontally constant after transport.

The second constructor applies when the fibers are carried to their canonical cores. A normal unital $*$-homomorphism

$$
\nu:\mathcal N\longrightarrow\mathcal M
$$

is **tempered** when there exists a normal faithful semifinite operator-valued weight from \(\mathcal M\) onto \(\nu(\mathcal N)\). Such arrows compose. [[library/functoriality-of-connes-takesaki-flow-of-weights/inq|Elliott's functoriality theorem]] then gives a canonical compatible morphism of Falcone--Takesaki cores, and the core map for a composite equals the composite of the core maps. Conversely, a compatible extension of an inclusion to the noncommutative flows implies tempering under the theorem's hypotheses.

Thus functorial core transport along a chain is **[STANDARD ON THE TEMPERED SUBCATEGORY]**. A wall candidate still has to construct its physical arrows and prove that they are tempered. The theorem does not choose states, establish a BKM tangent, prove effective descent over covers, or extend center-valued flow functoriality to arbitrary arrows; the center is functorial only on further proper subcategories. A bare phrase such as “pass to the core” therefore does not discharge W0c.

The third constructor keeps every scale inside one canonical core but has two distinct carriers. [[core-spectral-wall|The core spectral wall]] takes spectral cuts $e_N$ of the logarithmic core density and finite capacity corners $\mathcal K_N=e_N\mathcal C e_N$, with

$$
\kappa_{N_2:N_1}
=
\left.\beta_{N_2-N_1}\right|_{\mathcal K_{N_1}}.
$$

For response, it instead uses labelled whole-core fibers $\mathcal A_N=\mathcal C^{(N)}$, transport $\iota_{N_2:N_1}=\beta_{N_2-N_1}$, one global normal state, and binary contexts $\mathcal B_N=W^*(e_N)\subset\mathcal A_N$. The corner unit is $e_N$, so $\mathcal B_N\not\subset\mathcal K_N$; the Bernoulli readout is not a corner readout. Both transport laws compose exactly, and the ambient-core expectation returns nonzero Fisher--BKM response. This closes the abstract algebra--state--transport--readout problem on the whole-core carrier while separately constructing finite capacity. It does not show that the spectral cuts are causal cuts, that either carrier is a local spacetime net, that the ambient readout is the physical one, or that the chosen global density is physically selected.

[[finite-cellular-markov-wall|The finite cellular Markov wall]] gives a complementary exact benchmark using labelled carrier isomorphisms and a separate completely positive state-selection semigroup. Its point is typological: the reversible comparison arrow and the irreversible state-production arrow should not be denoted or interpreted as one map.

Locally covariant relative Cauchy evolution is a plausible way to define metric response on controlled backgrounds; the standard functorial framework is [[library/the-generally-covariant-locality-principle-a-new-paradigm-for-local-quantum-physics/inq|Brunetti, Fredenhagen, and Verch]]. A renormalized stress response additionally inherits the locality, covariance, scaling, and metric-variation ambiguities treated by [[library/microlocal-analysis-and-interacting-qft/inq|Brunetti and Fredenhagen]] and [[library/local-wick-polynomials-and-time-ordered-products/inq|Hollands and Wald]]. None of these implements a global homogeneous Weyl change or identifies changing cosmological regions, so they are candidate components rather than a finished transport.

For the algebraic exponential perturbation that a scale-deformed family would need, [[library/relative-hamiltonian-for-faithful-normal-states/inq|Araki's relative-Hamiltonian construction]] is the natural starting point, with relative entropy on von Neumann algebras and its support qualifications in [[library/relative-entropy-of-states-of-von-neumann-algebras/inq|Part I]] and [[library/relative-entropy-for-states-of-von-neumann-algebras-ii/inq|Part II]]. Local relativistic algebras are generally type III and admit neither density matrices nor an ordinary trace, so any finite-dimensional display of these constructions is an analogy and not the statement to be proved.

## Which part of the comparison is load-bearing

After transport, the logarithmic change of modular data separates into three terms of different type,

$$
\delta K
=\delta K_{\rm vertical\ gauge}
+\delta K_{\rm horizontal\ noncentral}
+\delta\alpha\,\mathbf 1 .
$$

The vertical term is modular-frame gauge. The central term shifts a normalization or a scalar lift and has **zero** information length, since relative entropy and every monotone metric are insensitive to a common central offset. Only the middle term can carry the response.

The obligation is therefore not merely to exhibit this decomposition but to show that its middle term is nonzero, is independent of the chosen frame, and does not depend arbitrarily on which transport was selected. This remains an **[OPEN PHYSICAL CONSTRUCTION]**, not an absence of mathematical examples. The half-sided-modular invariant family realizes the zero case exactly; the cellular Markov family realizes a nonzero finite case; and the core spectral wall realizes a nonzero continuous binary readout from one normal state on an infinite core. The missing theorem must preserve a nonzero horizontal sector while realizing a causal local carrier and physical quotient. If that tangent becomes pure vertical gauge or pure central shift under realization, the physical programme still has no response. [[vertical-and-horizontal-motion|Vertical and horizontal motion]] owns the type distinction.

## What a binary member additionally must show

After transport to a common algebra, let

$$
u_{21}(s):=(D\omega_{N_2}:D\omega_{N_1})_s
$$

be the relative modular cocycle. For a member that selects [[binary-channel|the optional binary channel]], the additional desired result is that its noncentral component takes the form

$$
u_{21}^{\perp}(s)
\sim
\exp\!\left[is\bigl(\theta(N_2)-\theta(N_1)\bigr)Q\right]
$$

up to a controlled central phase and vertical gauge. If in addition it depends on the two scales only through their ratio, cocycle composition gives the multiplicative Cauchy equation

$$
f(r_1r_2)=f(r_1)+f(r_2),
$$

whose measurable solutions are $f(r)=\varrho_\perp\ln r$, hence

$$
\theta=\varrho_\perp x,
\qquad
x:=N-N_c .
$$

**[CONDITIONAL THEOREM — BINARY MEMBER]** This derives logarithmic affinity. It does not derive the value $|\varrho_\perp|=1$, and no functional equation can, since every real slope solves it. Reversing the names of the two null orientations sends $Q\mapsto-Q$ and $\varrho_\perp\mapsto-\varrho_\perp$, so the orientation-independent quantity is the scale-state rate $\nu:=|\varrho_\perp|>0$. It is an inverse-width parameter only after a profile has been selected. The generic interface requires transport and a nonzero physical tangent, not this rank-one form; CWST does not consume it unless a particular spectral member says so.

### Two registrations that must accompany the statement

*The ratio convention.* Both existing derivations reach $\theta=\varrho_\perp x$ using **opposite** ratio conventions with compensating signs: one takes $r=\sigma_2/\sigma_1$ with $f(r)=-\varrho_\perp\ln r$, the other takes $r=\sigma_1/\sigma_2=a_2/a_1$ with $f(r)=+\varrho_\perp\ln r$. Since $\sigma\propto a^{-1}$, both land on the same soldering law. The conventions are consistent, but the sign of $\varrho_\perp$ is meaningful only relative to a declared ratio orientation, and any note that quotes the slope should register which it uses.

*Measurability is not continuity in $s$.* The regularity hypothesis needed is measurability of $f$ as a function of the external scale ratio $r$. Sigma-weak continuity of $u_t$ in the cocycle parameter $t$ is a different statement and does not supply it. This must be derived or assumed explicitly; without some regularity, pathological additive solutions are available.

## Failure modes of the binary-affine specialization

| Failure | Consequence |
|---|---|
| several noncommuting noncentral generators survive | a higher-rank path, not one scalar $\theta$; the binary channel obligation fails upstream |
| nontrivial holonomy | the comparison is path dependent; $\theta(N)$ is not a function of scale |
| state-dependent generator or non-affine transport | $\theta(N)$ nonlinear; the affine soldering law is lost while transport survives |
| scale-dependent channel | the binary normalization drifts, so a quoted slope has no fixed meaning |
| geometric modular flow fails | the horizon interpretation is lost, without invalidating abstract relative modular theory |

The last row is worth separating from the others: abstract relative modular theory can remain perfectly well defined while the *geometric* reading that motivated the construction evaporates. That would leave a mathematically sound comparison with no reason to call it a horizon response.

## State selection is a substantive law

The family $\{\omega_N\}$ cannot be treated as functorially automatic. [[library/dynamical-locality-and-covariance/inq|Fewster and Verch]] show that a covariantly preferred state is unavailable under broad dynamical-locality hypotheses. A candidate family must therefore state a physical selection rule and say which background structures or symmetries make it available — exact KMS behaviour, a horizon-equilibrium approximation, an adiabatic vacuum, or another declared condition.

There is a controlled precedent for the shape such a rule can take rather than for the rule itself: [[library/cosmological-horizons-and-reconstruction-of-quantum-field-theories/inq|Dappiaggi, Moretti, and Pinamonti]] map the algebra of a linear Klein–Gordon field into a cosmological-horizon algebra and induce a preferred bulk state on a selected class of expanding spacetimes. That is an existence result in a restricted class, with a linear field and a specific asymptotic structure; it is not the scale-indexed selection law required here.

The exact benchmarks give precise boundary conditions on this problem. The invariant reference state supplied as part of a half-sided modular inclusion is BKM-null after transport. The core spectral construction proves that no normal state on the whole trace-scaling core can be invariant under the full dual flow; one chosen global density therefore produces a nonconstant orbit, and its logistic member gives the exact balanced pulse after binary readout. This is a non-circular state **construction**, but not a unique physical **selection** of that density or its width. The finite Markov semigroup supplies the analogous separation in a finite carrier. A proposed cosmological law still has to explain why its causal realization selects one admissible state without reading the desired history backward.

**Success.** The family is defined without reference to the observable it is meant to explain, is regular enough for relative modular theory, and admits controlled renormalized stress responses.

**Failure.** The state is fixed only by matching a target history or spectrum, is non-faithful on the algebra where modular theory is used, or has unacceptable ultraviolet behaviour.

## Interface position

This note owns the generic horizontal problem: selecting states across fibers and comparing them. Its binary-affine subsection is one replaceable specialization. The exactness of the reduced algebra reached *after* that channel is granted belongs to [[binary-information-geometry/inq|binary information geometry]]; the justification of the channel belongs to [[binary-channel|the binary channel obligation]]; the affine theorem is kept in [[basic-concepts/soldering/affine-scale-state|affine scale--state soldering]]. Whether a completed transport explains anything is decided by [[elimination-test|the elimination tests]].
