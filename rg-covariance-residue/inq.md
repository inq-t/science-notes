---
inq.module: "rg-covariance-residue"
inq.include:
  - "**/*.md"
inq.ambient:
  - "**/*.py"
  - "**/*.txt"
---
# RG Covariance Residue

Exact nested coarse-graining splits a correlation into its retained correlation and an orthogonal sum of conditional covariance residues. A cutoff-uniform exponential estimate on each discarded scale, together with a terminal estimate at one fixed physical scale, gives a common physical correlation exponent. This replaces an opaque source-transport assumption with explicit estimates on what is forgotten. It does not assume that coarse-graining is physical time, or that a probability law implies ontological randomness.

**Status: [EXACT IDENTITIES AND CONDITIONAL SUMMATION THEOREM]; [OPEN] source-localization and terminal estimates for the asymptotically free four-dimensional Yang--Mills law.**

## What the operators operate on

At each regulator \(a\), start with one probability law \(\mu_a\) and nested retained sigma algebras

$$
\mathcal B_{a,0}\supset\cdots\supset\mathcal B_{a,J(a)},
\qquad
E_{a,j}:L^2(\mu_a)\longrightarrow L^2(\mathcal B_{a,j},\mu_a),
\qquad E_{a,0}=I.
\tag{CR1}
$$

Here \(E_{a,j}\) is conditional expectation for the **same** law \(\mu_a\). Successive measurable block maps supply such a tower through composition. A gauge-invariant law and gauge-stable retained sigma algebras make these projections preserve gauge-invariant observables.

These are projections of source functions, not projections of spacetime points, quantum instruments selecting outcomes, or physical time translations. A tower of sigma algebras is an ordered loss of accessible distinctions. The law supplies their weights; the tower alone supplies neither probabilities nor energy.

Suppress \(a\), define

$$
D_j=E_j-E_{j+1},\qquad
\langle F,G\rangle_\mu=\mu(\overline F G),\qquad
\operatorname{Cov}_\mu(F,G)
=\mu(\overline F G)-\overline{\mu(F)}\mu(G).
\tag{CR2}
$$

The tower property and self-adjointness give

$$
D_iD_j=\delta_{ij}D_j,\qquad
E_JD_j=0,\qquad
I=E_J+\sum_{j<J}D_j.
\tag{CR3}
$$

Thus for all \(F,G\in L^2(\mu)\),

$$
\boxed{\operatorname{Cov}_\mu(F,G)
=\operatorname{Cov}_\mu(E_JF,E_JG)
+\sum_{j<J}\langle D_jF,D_jG\rangle_\mu.}
\tag{CR4}
$$

This is the sesquilinear counterpart of the [[contemporary-puzzles/yang-mills-mass-gap/gauge-descent-flux-fisher-coercivity|orthogonal variance-shell identity]]. Expanding (CR3) on centered functions proves it: every cross-shell term vanishes. No dynamics or gap hypothesis enters.

If \(\mu_j\) is the exact retained law at scale \(j\), let \(f_j,g_j\) represent \(E_jF,E_jG\), and disintegrate \(\mu_j\) over the next block variable \(y\) with conditional law \(\nu_{j,y}\). Then

$$
\boxed{\langle D_jF,D_jG\rangle_\mu
=\int\operatorname{Cov}_{\nu_{j,y}}(f_j,g_j)\,\mu_{j+1}(\mathrm dy).}
\tag{CR5}
$$

For \(F=G\), the residue is nonnegative. For two different sources it need not have a sign. Calling every covariance residue a positive energy cost would already mistype the identity.

## A uniform physical exponent from ultraviolet shells

Let \(L>1\), choose a fixed physical scale \(r_*>0\) independently of the unknown gap, and suppose the terminal scale and discarded scales are

$$
b_*(a)\in[r_*,Lr_*],\qquad
b_{a,j}=b_*(a)L^{j-J(a)}.
\tag{CR6}
$$

For fixed renormalized sources \(F,G\) and physical separation \(r\), assume

$$
\begin{aligned}
|\langle D_{a,j}F_a,D_{a,j}G_{a,r}\rangle_{\mu_a}|
&\le C_{F,G}\left(\frac{b_*(a)}{b_{a,j}}\right)^{p_{F,G}}
e^{-mr/b_{a,j}},\\
|\operatorname{Cov}_{\mu_a}
(E_{a,J}F_a,E_{a,J}G_{a,r})|
&\le C^T_{F,G}e^{-\sigma_T r},
\end{aligned}
\tag{CR7}
$$

with \(m,\sigma_T>0\) common to the source family, \(p_{F,G}\ge0\), and finite prefactors independent of cutoff, volume, admissible boundary data, and separation. The scale ratios and \(m\) are dimensionless; \(\sigma_T\) has inverse-length units. Translation need not commute with \(E_{a,j}\) for these written estimates, but the translated sources must be actual sources on the original law.

**Conditional theorem.** For \(r\ge Lr_*\), these hypotheses imply

$$
|\operatorname{Cov}_{\mu_a}(F_a,G_{a,r})|
\le\left(C_{F,G}A_{p_{F,G},m,L}+C^T_{F,G}\right)e^{-\sigma_0r},
\qquad
\sigma_0=\min\left\{\frac{m}{Lr_*},\sigma_T\right\}>0,
\tag{CR8}
$$

where

$$
A_{p,m,L}
=\sum_{n=1}^{\infty}L^{np}e^{-m(L^n-1)}<\infty.
\tag{CR9}
$$

**Proof.** Put \(n=J-j\ge1\), \(t=r/b_*\ge1\). Then

$$
\begin{aligned}
\sum_{j<J}(b_*/b_j)^p e^{-mr/b_j}
&=\sum_{n=1}^{J}L^{np}e^{-mtL^n}\\
&=e^{-mt}\sum_{n=1}^{J}L^{np}e^{-mt(L^n-1)}
\le e^{-mt}A_{p,m,L}.
\end{aligned}
\tag{CR10}
$$

The series converges because \(e^{-mL^n}\) dominates \(L^{np}\). Apply the triangle inequality to (CR4), then \(b_*\le Lr_*\). This proves (CR8) at the stated endpoint; no exponent loss is needed. Polynomial separation factors, if introduced by a different estimate, would require a small exponent loss.

Source-dependent powers and prefactors are allowed. Source-dependent exponents tending to zero across the family are not. More general weights \(w_{a,j}\) work whenever

$$
\sup_a\sum_{j<J(a)}w_{a,j}
\exp[-m(b_*(a)/b_{a,j}-1)]<\infty.
\tag{CR11}
$$

This is a sufficient absolute-summation criterion, not a necessary one if cancellations occur. A finite sum of separation-independent errors is insufficient.

The allowed polynomial is in \(b_*/b_j\), the remaining ratio to the fixed terminal scale. It is not an arbitrary cutoff divergence. [[conditioned-source-transport|Conditioned source transport]] shows that a bounded amplification \(M>1\) at each step instead yields \(M^j=(b_j/a)^{\log_LM}\), which can diverge at the terminal scale and does not establish (CR7).

## The actual analytic obligations

The first line of (CR7) is not supplied by nesting. One sufficient route starts with a conditional covariance kernel. In a declared block geometry with dimensionless distance \(d_j\), suppose

$$
|\operatorname{Cov}_{\nu_{j,y}}(f,g)|
\le K_j\sum_{x,z}e^{-m d_j(x,z)}
a_x(f;y)a_z(g;y),
\tag{CR12}
$$

where \(a_x\) are specified nonnegative local derivative or oscillation seminorms, and the sums converge. For original source supports \(A,B\), define

$$
S_{F,j}(y)=\sum_xe^{m d_j(x,A)}a_x(f_j;y),
\qquad
S_{G,j}(y)=\sum_ze^{m d_j(z,B)}a_z(g_j;y).
\tag{CR13}
$$

Assume \(d_j(A,B)\ge r/b_j\), with \(r\) the actual physical support separation. Only offsets bounded in block units, hence physical \(O(b_j)\), can be absorbed into regulator-uniform constants. A fixed physical offset \(\delta\) would introduce \(e^{m\delta/b_j}\); instead use actual support separation, or lower the common exponent and impose a source-dependent onset such as translation distance \(s\ge2\delta\). The metric triangle inequality and Cauchy--Schwarz in \(y\) give

$$
|\langle D_jF,D_jG\rangle|
\le K_j e^{-mr/b_j}
\|S_{F,j}\|_{L^2(\mu_{j+1})}
\|S_{G,j}\|_{L^2(\mu_{j+1})}.
\tag{CR14}
$$

A polynomial bound on the product on the right proves the first line of (CR7). Weighted source norms need to be finite: exponential tails at exactly rate \(m\), without further summability, do not ensure that.

The terminal line of (CR7) has its own source-localization obligation. A terminal mixing theorem stated only for strictly local functions does not automatically apply to \(E_JF\), which can be nonlocal. One must prove controlled localized representatives, extend the terminal kernel estimate to the weighted source class, or directly establish the displayed terminal covariance bound.

This separates two missing estimates that the phrase “exact blocking” obscures:

- conditional fluctuations forgotten at step \(j\) must be localized at scale \(b_j\); and
- the sources retained at each step must have uniformly controlled spatial tails.

[[conditioned-source-transport|The conditioned-source derivative]] identifies the relevant response exactly: direct source variation minus covariance with the retained perturbation's conditional score. [[wilson-path-product-fibers|Wilson path-product fibers]] realizes that score as a plaquette derivative on an explicit fixed-Haar fiber. This supplies the finite carrier and local score geometry, while leaving the susceptibility and renormalized-source estimates separate.

Uniform conditional Poincare or logarithmic-Sobolev inequalities plus influence estimates can prove such bounds. They are sufficient machinery, not necessary hypotheses of (CR4) or (CR8). Static source covariance can be controlled even when a chosen auxiliary sampler mixes slowly. Rescaling a sampler changes its rate without changing any of (CR1)--(CR14).

[[library/a-simple-method-for-finite-range-decomposition/inq|Bauerschmidt's Gaussian finite-range decomposition]] supplies a rigorous precedent for localized covariance scales. Its independent Gaussian summands are not automatically the conditional-expectation shells of a given deterministic block map, and a massless field also admits localized multiscale decompositions. The infrared remainder, not the existence of shells, is decisive.

## A local block can discard an infrared field

Take the product of independent massive and massless free Euclidean scalar fields in four dimensions. Let an ultralocal block retain the massive species and discard the massless species \(\phi\) entirely. The retained law is gapped.

Choose real nonnegative smooth compactly supported \(f\) with nonzero integral, set \(X=\phi(f)\), and use the bounded centered source \(F=\sin X\). Independence gives \(E_1F=0\), hence \(D_0F=F\). For a translate \(f_r\),

$$
\operatorname{Cov}(F,F_r)
=e^{-v}\sinh C(r),\qquad
v=\operatorname{Var}\phi(f),\quad
C(r)=\operatorname{Cov}(\phi(f),\phi(f_r))
\asymp r^{-2}.
\tag{CR15}
$$

The identity follows by expanding \(\sin X\sin Y\) into cosines and using the joint centered Gaussian characteristic function. The four-dimensional massless Green kernel is proportional to \(|x-y|^{-2}\), giving the stated large-distance behavior after smearing. Therefore the discarded shell violates every positive exponential bound.

Locality of a deterministic block map does **not** imply that its forgotten information is ultraviolet. If the discarded gapless field is visible in the intended physical source family, a proof must retain it or control it; it cannot certify only the massive marginal.

[[thin-skeleton-and-block-average-coercivity|Thin skeletons and block-average coercivity]] gives a same-field geometric test: the straight path-product block can also hide an extended Maxwell variation at vanishing stiffness cost. Componentwise cell means behave differently, imposing a uniform linear fluctuation floor on the constrained, co-closed carrier. Both results concern ultraviolet separation. The retained infrared covariance still decides whether a physical gap can follow.

[[regular-gauge-averages-and-the-selection-obstruction|Gauge averages and the selection obstruction]] constructs a regular nonlinear average and a smooth global continuation retaining a chosen anchor. A common-pivot architecture gives exact product-Haar fibers. [[normalized-gauge-kernels-and-markov-residues|Normalized gauge kernels]] instead return a probability measure on coarse group variables and need no determinant branch or pivot chart. Their auxiliary Markov tower realizes (CR4)--(CR5) through nested suffix algebras for initial physical sources; the fine marginal is unchanged.

[[endpoint-averages-and-quadratic-ultraviolet-control|Endpoint averaging]] proves that curvature and the retained average jointly control every linear gauge class, uniformly even in the blocking factor. [[soft-gaussian-gauge-blocking|Soft Gaussian blocking]] bounds reverse conditional precision in volume and completed depth. [[accumulated-readout-noise|The accumulated noise]] has an exact nearest-neighbor unprojected covariance, and [[multilevel-local-gauge-completion|the whole-chain completion]] preserves all joint curvature statistics. [[uniform-gaussian-conditional-locality|Uniform Gaussian conditional locality]] controls the inherited Maxwell term and transverse inverse: the principal pole cancels by gradient compatibility, high aliases admit a depth-uniform holomorphic bound, and weighted terminal inversion gives exponential covariance and coarse-source response. The full-stack coherent-mode obstruction remains true but no longer obstructs this terminal proof.

[[compact-gauge-kernel-tangent-response|The compact-kernel tangent calculation]] supplies the normalized near-identity match in four dimensions and separates a mode Hessian from the forward Fisher metric. The Gaussian precision bound is depth-uniform, but the compact approximation is only fixed-regulator; transferring the estimates through the full nonlinear law remains open.

## From residues to physical mass

Apply (CR8) at each regulator, including to reflected diagonal pairs from a fixed source family whose complex linear span reconstructs a dense vacuum-complement subspace. Compare support separation \(r\) with OS translation distance \(s\) explicitly. If \(r\ge s-\delta_F\) for a fixed source-dependent physical offset, the already summed estimate obeys \(e^{-\sigma_0r}\le e^{\sigma_0\delta_F}e^{-\sigma_0s}\). Unlike the individual-shell factor \(e^{m\delta_F/b_j}\), this prefactor is cutoff independent, so the exponent is preserved beyond a source-dependent onset. Pass the uniform bounds through a nontrivial reflection-positive continuum limit satisfying the full OS reconstruction hypotheses. [[auxiliary-response-localization/inq|The positive spectral-measure argument]] then gives

$$
H-E_0\ge\hbar c\,\sigma_0(I-P_0).
\tag{CR16}
$$

Here \(P_0\) is the zero-energy projection; uniqueness of the vacuum and the OS-totality requirement must be established, not inferred from centering alone. Positive-energy Poincare covariance and the usual forward-cone spectrum are additionally needed to read this as an invariant-mass floor \(M_{\mathrm{gap}}\ge\hbar\sigma_0/c\).

No common probability space across different cutoffs, or infinite reverse-martingale limit, was used. Each identity is finite-regulator; uniform estimates do the limiting work.

This gives a concrete static alternative to transporting full auxiliary coercivity in [[contemporary-puzzles/yang-mills-mass-gap/asymptotically-free-response-crossover-lemma|the Yang--Mills response-crossover lemma]]. What remains open there is proving (CR7), including source tails, for the full non-Abelian trajectory and constructing its Yang--Mills continuum limit. The result here is an exact decomposition and a conditional implication, not that missing construction.
