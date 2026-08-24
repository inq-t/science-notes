# Cross-Fiber Transport and State Selection

Comparing states attached to different scales requires two things that are usually assumed: a transport placing them on a common algebra, and a rule selecting the state at each scale in the first place. Both are substantive. Without transport, the horizontal tangent is an undefined symbol rather than an uncomputed number; without a selection rule, a covariance argument shows no preferred family need exist at all.

## The transport problem

Let $N\mapsto(\mathcal A_N,\omega_N)$ be the intended family. Relative entropy and the Connes cocycle are defined for two states on one von Neumann algebra, so before any cross-scale quantity is written, one of the following must be supplied:

- **embeddings** $\iota_{N_2N_1}:\mathcal A_{N_1}\to\mathcal A_{N_2}$, with a composition law $\iota_{N_3N_2}\circ\iota_{N_2N_1}=\iota_{N_3N_1}$;
- a **common ambient algebra** into which every $\mathcal A_N$ embeds;
- a **crossed-product or core construction** on which the relevant states become comparable;
- a **modular Berry connection** or parallel transport, with its gauge dependence and holonomy controlled.

These are not equivalent. An inclusion of regions gives isotony for free but changes which observables exist; a common ambient algebra buys comparability at the cost of specifying that ambient object; a crossed product changes the algebra type and introduces its own dressed observables; a connection defines transport only up to holonomy, which must then be shown negligible or accounted for.

Locally covariant relative Cauchy evolution is a plausible way to define metric response on controlled backgrounds; the standard functorial framework is [[causal-wall-spectral-theory/sources/papers/0112041-brunetti-fredenhagen-verch-generally-covariant-locality.pdf|Brunetti, Fredenhagen, and Verch]]. A renormalized stress response additionally inherits the locality, covariance, scaling, and metric-variation ambiguities treated by [[causal-wall-spectral-theory/sources/papers/9903028-brunetti-fredenhagen-microlocal-renormalization-physical-backgrounds.pdf|Brunetti and Fredenhagen]] and [[causal-wall-spectral-theory/sources/papers/0103074-hollands-wald-local-wick-polynomials-time-ordered-products.pdf|Hollands and Wald]]. None of these implements a global homogeneous Weyl change or identifies changing cosmological regions, so they are candidate components rather than a finished transport.

For the algebraic exponential perturbation that a scale-deformed family would need, [[causal-wall-spectral-theory/sources/papers/1973-araki-relative-hamiltonian-faithful-normal-states.pdf|Araki's relative-Hamiltonian construction]] is the natural starting point, with relative entropy on von Neumann algebras and its support qualifications in [[causal-wall-spectral-theory/sources/papers/1976-araki-relative-entropy-von-neumann-algebras-i.pdf|Part I]] and [[causal-wall-spectral-theory/sources/papers/1977-araki-relative-entropy-von-neumann-algebras-ii.pdf|Part II]]. Local relativistic algebras are generally type III and admit neither density matrices nor an ordinary trace, so any finite-dimensional display of these constructions is an analogy and not the statement to be proved.

## Which part of the comparison is load-bearing

After transport, the logarithmic change of modular data separates into three terms of different type,

$$
\delta K
=\delta K_{\rm vertical\ gauge}
+\delta K_{\rm horizontal\ noncentral}
+\delta\alpha\,\mathbf 1 .
$$

The vertical term is modular-frame gauge. The central term shifts a normalization or a scalar lift and has **zero** information length, since relative entropy and every monotone metric are insensitive to a common central offset. Only the middle term can carry the response.

The obligation is therefore not merely to exhibit this decomposition but to show that its middle term is nonzero, is independent of the chosen frame, and does not depend arbitrarily on which transport was selected. **[OPEN CONSTRUCTION]** If the horizontal tangent turns out to be pure vertical gauge or pure central shift, the programme has no response at all — and this is a live possibility, not a formality, because the central direction is exactly where a vacuum-energy-like offset would sit. [[vertical-and-horizontal-motion|Vertical and horizontal motion]] owns the type distinction.

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

**[CONDITIONAL THEOREM — BINARY MEMBER]** This derives logarithmic affinity. It does not derive the value $|\varrho_\perp|=1$, and no functional equation can, since every real slope solves it. Reversing the names of the two null orientations sends $Q\mapsto-Q$ and $\varrho_\perp\mapsto-\varrho_\perp$, so the orientation-independent quantity is the width $\nu:=|\varrho_\perp|>0$. The generic interface requires transport and a nonzero physical tangent, not this rank-one form; CWST does not consume it unless a particular spectral member says so.

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

The family $\{\omega_N\}$ cannot be treated as functorially automatic. [[causal-wall-spectral-theory/sources/papers/1106.4785-fewster-verch-dynamical-locality-covariance.pdf|Fewster and Verch]] show that a covariantly preferred state is unavailable under broad dynamical-locality hypotheses. A candidate family must therefore state a physical selection rule and say which background structures or symmetries make it available — exact KMS behaviour, a horizon-equilibrium approximation, an adiabatic vacuum, or another declared condition.

There is a controlled precedent for the shape such a rule can take rather than for the rule itself: [[causal-wall-spectral-theory/sources/papers/0712.1770-dappiaggi-moretti-pinamonti-cosmological-horizons-qft.pdf|Dappiaggi, Moretti, and Pinamonti]] map the algebra of a linear Klein–Gordon field into a cosmological-horizon algebra and induce a preferred bulk state on a selected class of expanding spacetimes. That is an existence result in a restricted class, with a linear field and a specific asymptotic structure; it is not the scale-indexed selection law required here.

**Success.** The family is defined without reference to the observable it is meant to explain, is regular enough for relative modular theory, and admits controlled renormalized stress responses.

**Failure.** The state is fixed only by matching a target history or spectrum, is non-faithful on the algebra where modular theory is used, or has unacceptable ultraviolet behaviour.

## Interface position

This note owns the generic horizontal problem: selecting states across fibers and comparing them. Its binary-affine subsection is one replaceable specialization. The exactness of the reduced algebra reached *after* that channel is granted belongs to [[binary-information-geometry/entry|binary information geometry]]; the justification of the channel belongs to [[binary-channel|the binary channel obligation]]; the affine theorem is kept in [[basic-concepts/soldering/affine-scale-state|affine scale--state soldering]]. Whether a completed transport explains anything is decided by [[elimination-test|the elimination tests]].
