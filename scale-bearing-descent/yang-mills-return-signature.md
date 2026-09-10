# The Missing Signature of a Yang–Mills Return

A backwards solution needs three compatible interfaces: a local positive realization of the master law, a renormalized identification of its fields as Yang–Mills, and a quantitative comparison carrying upstream stability into the returned chronology. Clay fixes the observable target while leaving the construction language open. This inventory specifies what the missing maps must do, without attempting to construct them. Its strongest conjecture is that one realization satisfies all three interfaces; the master and physical carriers need not be identical.

## The target and the route have different logical force

[[contemporary-puzzles/yang-mills-mass-gap/clay-contract-and-scale-assumptions|The source-assumption audit]] and [[contemporary-puzzles/yang-mills-mass-gap/puzzle-as-posed|the precise target]] unpack [[library/quantum-yang-mills-theory/inq|Jaffe–Witten, §§3–4]]. The construction may begin with comparison, directed composition, a category, an algebra or another language. The returned theory must have the stipulated axiomatic strength and Yang–Mills field content.

Let \(\mathsf{QFT}_4\) denote theories with the required four-dimensional local quantum-field structure, before asserting Yang–Mills identity or a gap. The abstract target is
\[
\forall G\in\mathsf{CompactSimple},\quad
\exists\mathcal W_G\in\mathsf{QFT}_4:
\quad
\mathsf{YMId}_G(\mathcal W_G)
\ \wedge\
0<m_G<\infty.
\tag{YS1}
\]
Here \(\mathsf{CompactSimple}\) denotes the gauge Lie groups meant by the Clay statement: simplicity of the Lie algebra permits a finite group center. The number \(m_G\) is the lower edge of the nonvacuum Hamiltonian spectrum. Nontriviality is part of the target, including nonzero physical distinctions and the nontrivial Yang–Mills correspondence.

The quantifiers permit a family indexed by \(G\), group-dependent constants and a choice of admissible branch. They do not demand one numerical lower bound for every group, a unique realization across all possible phases, or one exceptional finite algebra containing every group.

For our proposed route, assume the [[scale-bearing-descent/pointed-comparison-and-the-yang-mills-return|stable-facticity axiom]] supplies the upstream requirement. The missing signature is then
\[
\begin{aligned}
\mathsf{Loc}_G &: (\mathfrak U,\sigma_G)\rightsquigarrow\mathcal W_G,\\
\mathsf{YMId}_G &: \mathcal W_G\rightsquigarrow
 \text{the stipulated renormalized Yang--Mills correspondence},\\
\mathsf{Comp}_{G,\ell} &: (\mathfrak U,\sigma_G,\mathcal W_G)
 \rightsquigarrow\text{a physical response domination}.
\end{aligned}
\tag{YS2}
\]
The branch \(\sigma_G\) includes whichever pointing, sector and relative calibration the doctrine permits. The arrows specify unknown relations or realizations; they are not claimed to be functors until their morphisms and composition laws are defined. The same \(\mathcal W_G\) must occur in all three lines.

These are sufficient interfaces for this programme. A theorem solving Clay by another method need not contain our master object, repair operator or comparison form. Conversely, simply defining the set of successful triples does not establish that it is inhabited. The conjecture may posit inhabitation while leaving its construction open.

## Interface I: a local positive realization

A standard Wightman presentation of the first output is
\[
\mathcal W_G=
\bigl(
\mathcal H_G,\mathcal D_G,\Omega_G,
U_G,\{\mathcal O_{\alpha,G}\}
\bigr).
\tag{YS3}
\]
An alternative axiomatic presentation is admissible if its demonstrated strength reaches the required target. A bare local net or a positive transfer alone does not establish that equivalence.

| Output slot | Exact work it must perform | Meaning before familiar physical nouns |
|---|---|---|
| \(\mathcal H_G,\Omega_G\) | A positive complex Hilbert space and normalized vacuum; finite products of returned fields on the vacuum have dense span | Comparisons have a common positive norm and generate the intended factual carrier |
| \(\mathcal D_G\) | A common dense domain containing the vacuum, invariant under the fields and \(U_G\), with the required adjoint and product operations | Successive comparisons remain mathematically meaningful on one domain |
| \(\mathcal O_{\alpha,G}\) | Local operator-valued tempered distributions, smeared with the appropriate test functions and satisfying covariance | A localized comparison is a continuous response to a probe, not a primitive value at a point |
| \(U_G\) | A strongly continuous unitary representation of the proper orthochronous Poincaré group or its cover, with \(U_G(g)\Omega_G=\Omega_G\) | The returned norm admits a coherent family of reversible frame comparisons |
| \(P_{\mu,G}\) | Joint translation spectrum in the closed forward cone; \(H_G=P_{0,G}\ge0\) fixes the vacuum | The clock has an orientation and compatible spatial translations, rather than merely a self-adjoint generator |
| Locality | Gauge-invariant bosonic fields commute at spacelike separated supports on their common domain | The observable product forgets the order of causally independent comparisons |
| Vacuum and nontriviality | The stipulated vacuum uniqueness in the chosen representation and a nonzero nonvacuum carrier | A common reference exists without reducing every comparison to that reference |

The four-dimensional arena belongs to the output type. An upstream derivation can return its region order, cone and translation action from prior relations. A Clay solution can instead use this arena as target geometry. Explaining why no other dimension is possible is a stronger selection theorem.

Several hidden dependencies become visible in this signature.

**Positivity does not yet give locality or a clock.** A positive kernel supplies a quotient norm. One still needs operations that preserve the appropriate null spaces, local field domains and the specified translation action. [[directed-analytic-realization/preparation-overlaps-and-the-transition-algebra|Preparation transitions]] already return a noncommutative product but leave the local commuting subalgebras unselected.

**Unitarity does not yet give positive energy.** [[algebra/quotient-unitarity-and-kernel-stabilization|Quotient unitarity]] allows irreversible upstream operations to induce reversible observable evolution. Strong continuity gives a self-adjoint generator; the forward-cone condition remains a distinct predicate. Record precedence, Euclidean attenuation and Lorentzian clock transport therefore require comparison maps, not one shared name for time.

**Locality is a condition on every source context.** In an associative Wightman source presentation, write \(q(c)=c\Omega_G\) for its represented vacuum vector. This is a vector quotient, not an algebra quotient. A sufficient realization of spacelike commutation is
\[
q\bigl((ab-ba)c\bigr)=0
\quad\text{for every domain-generating source word }c,
\tag{YS4}
\]
when \(a,b\) have spacelike separated returned supports. Annihilating only the vacuum vector is weaker. The master may retain order-sensitive operations that the returned observable product identifies. Its returned product must nevertheless be associative and well defined; coherence or nonassociativity upstream does not supply this automatically.

Equation (YS4) is a Wightman domain statement. A centered Osterwalder–Schrader null subspace is generally only a vector subspace, not an algebra ideal. One must not obtain local field multiplication by casually multiplying its Hilbert equivalence classes. [[global-local-response-reconstruction/causal-patch-boundary-and-two-times|The locality and temporal audit]] and the full reconstruction theorem supply the relevant distinctions.

## One compact way to package the local return

An admissible Euclidean implementation can return a complete source functional,
\[
\mathsf{SrcReal}_G:
(\mathfrak U,\sigma_G)
\rightsquigarrow
(\mathscr B_G,S_G,\Theta_G,\alpha_G).
\tag{YS5}
\]
Here \(\mathscr B_G\) contains finite expressions in smeared, renormalized local sources, including their joint products and support assignment. The latter defines its positive-time subspace \(\mathscr B_{G,+}\). The normalized linear functional \(S_G\) evaluates these expressions; \(\Theta_G\) is the antilinear reflected adjoint; and \(\alpha_G\) supplies Euclidean covariance and the positive-time translations used in reconstruction.

This package owes the full correlation hierarchy and the regularity, reflection positivity, covariance, symmetry and vacuum conditions needed by an applicable reconstruction theorem. It need not arise from an ordinary positive probability measure on classical connections. Its reflection is also not a postulate of physical time-reversal symmetry.

The important compatibility is that one evaluation supplies the marks, reflected norm, vacuum subtraction and all translated products. For a construction through approximations, a possible interface is
\[
S_G(F)=
\lim_r
\frac{\mathcal Z(D_{G,r};R_{G,r}F)}
     {\mathcal Z(D_{G,r};1)}.
\tag{YS6}
\]
The denominator must be admissible and nonzero. The maps \(R_{G,r}\) realize complete source expressions, with their renormalization terms and mixed products. The limit must exist in a topology sufficient for the required distributions and operations. Formula (YS6) declares the interface without selecting the diagrams, maps, measure or limiting technique. Its index \(r\) labels the declared return family; it need not mean that every upstream microscopic structure is disposable.

[[scale-bearing-descent/constitutive-resolution-and-the-yang-mills-return|Constitutive resolution]] sharpens the distinction using [[factive-cosmos/causal-fermion-systems-and-the-action-of-the-whole|Finster's causal fermion systems]]. Auxiliary approximation data must disappear from, or be proved immaterial to, the exact output. Constitutive microscopic data may belong to the master object; the return must specify which of their distinctions survive as scale or other parameters. An exact local sector, quotient or limit is a possible interface. A finite-resolution approximation alone does not supply the full target.

For the limiting route, full Poincaré covariance belongs to the return; a lattice approximation need not possess it exactly. A direct local-functional or Lorentzian realization may avoid auxiliary regulators altogether. Conversely, a retained microscopic parameter upstream need not appear as a locality defect downstairs. That separation requires a theorem about the complete sources, their state, products and chronology. The [[global-local-response-reconstruction/qft-recovery-contract|QFT recovery contract]] gives several stronger implementation choices; they must not all be imposed simultaneously as necessary conditions.

In a universality construction, the admissible basin must be specified by upstream data and declared renormalization conditions. The conjecture is that its presentation choices return the same complete functional after parameter matching, not that every microscopic state or phase must give the same theory. Fixed returned scale can coexist with a vanishing gap in cutoff units: \(a m_G\to0\) while \(m_G>0\). The duration needed by the comparison interface is a surviving relational scale, not automatically the microscopic step \(a\).

## Interface II: identify this theory as Yang–Mills

This is the most easily understated missing piece. It is not discharged by constructing \(F^2\), a compact stabilizer, a Wilson-like interaction, or some non-Gaussian correlations.

For each engineering-dimension cutoff \(d\), let \(\mathscr P^{\mathrm{inv}}_{G,\le d}\) denote the relevant space of gauge-invariant differential polynomials in curvature and covariant derivatives, with its algebraic identities. The identification must relate this power-counting filtration to the returned local operator spaces:
\[
\mathsf{Id}^{\mathrm{ren}}_{G,\le d}:
\mathscr P^{\mathrm{inv}}_{G,\le d}
\rightsquigarrow
\mathscr O^{\mathrm{loc}}_{G,\le d}.
\tag{YS7}
\]
This is a renormalization-aware correspondence, including operator mixing and relations; anomalous and logarithmic scaling belongs to its short-distance comparison. Clay's footnote explicitly warns against a natural one-to-one assignment of individual classical polynomials to quantum operators. A strict multiplicative map from pointwise classical products is therefore the wrong type.

The correspondence must include the required short-distance agreement with asymptotic freedom and perturbative renormalization, including a stress tensor and operator products with the prescribed local singularities. Its comparison data include a normalization convention, allowed changes of operator basis and the meaning of the asymptotic estimates. They must describe the same fields and state as Interface I.

There is a remaining specification task even before construction: choose a precise mathematical formulation of those short-distance estimates that faithfully implements the target. Merely writing “correct UV behavior” leaves a slot untyped. Schematically an OPE comparison concerns
\[
\mathcal O_\alpha(x)\mathcal O_\beta(y)
\sim\sum_\gamma C_{\alpha\beta}^{\ \gamma}(x-y;\mu)
\mathcal O_\gamma(y)
\tag{YS8}
\]
inside suitably smeared correlations with the allowed spectator insertions, in a specified short-distance limit and remainder topology. Equation (YS8) is not an assertion that an operator series converges in norm. The required coefficients, logarithmic behavior, mixing and remainder statements are part of the identification interface.

This formulation leaves substantial latitude. Exact equality with a particular Wilson lattice law is a sufficient candidate route, not the definition of the target. A local gauge potential need not act on the positive physical Hilbert space if the required gauge-invariant fields are supplied directly. Auxiliary variables may remain upstream, but the returned pure-gauge theory must not retain extra independent propagating matter or a necessary cosmic cutoff.

[[general-causal-action/prepared-readout-algebra-and-physical-source-completeness|Finite prepared sources]], [[general-causal-action/local-incidence-preparations-and-the-gauge-transfer|finite gauge transfers]] and [[general-causal-action/cofinal-determinant-and-wilson-source-equivalence|complete determinant-to-Wilson comparisons]] provide partial precedents. Their type limitations identify this missing interface: renormalized local fields, their complete correlations and the stipulated short-distance structure.

## Interface III: the returned clock must detect the stable comparisons

Grant the upstream stability axiom for the chosen branch. The weakest useful interface in the current fixed-duration route can be stated entirely with forms.

For every finite complex linear combination \(F\) of positive-time sources, let
\[
\begin{aligned}
K^c_G(F_1,F_2;t)
&=\langle Q_\Omega[F_1],e^{-tH_G}Q_\Omega[F_2]\rangle,\\
N_G(F)&=K^c_G(F,F;0),\\
D_{G,\ell}(F)&=N_G(F)-K^c_G(F,F;2\ell).
\end{aligned}
\tag{YS9}
\]
The duration \(\ell>0\) uses the inherited length convention, with \(H_G\) in inverse-length units. The centered positive-time source vectors must have dense span in \(Q_\Omega\mathcal H_G\). These are pairings of the theory returned by Interface I, not a separate classical prediction norm.

The unknown map must supply an actual positive Hermitian source-response form \(R_G\) with
\[
\boxed{
b_GN_G(F)\le R_G(F,F)
\le L_G^2D_{G,\ell}(F)+\eta_GN_G(F),
\qquad b_G>\eta_G\ge0,\quad L_G>0.}
\tag{YS10}
\]

The left inequality means **every physical distinction reaches the stable source comparison**. The right means **a source distinction cannot evade the returned chronology**. Their common margin gives, for any
\(0<\kappa_G<\min\{1,(b_G-\eta_G)/L_G^2\}\),
\[
H_G\ge-\frac{\log(1-\kappa_G)}{2\ell}Q_\Omega.
\tag{YS11}
\]
[[measured-response-carriers/response-to-energy-comparison#A reflected comparison needs only a form sandwich|The response domination contract]] gives this exact conditional deduction.

An equality between the master and physical Hilbert spaces is unnecessary. A comparison map \(J\) can instead detect the physical vacuum complement inside a larger source space: \(\|Q_sJx\|\ge a\|x\|\). A source floor \(q_s\ge cQ_s\) then supplies \(b_G=ca^2\), provided its pullback is bounded above by the physical chronological response as in (YS10). Only the centered image must retain the physical norm. Global faithfulness or invertibility across a forgetting map would impose an unnecessary and sometimes incompatible demand.

The upper inequality also makes \(R_G\) vanish on the centered physical null subspace \(\{F:Q_\Omega[F]=0\}\) and extend continuously; those conditions need not be separately postulated. Exact response intertwiners, bounded repairs, ordered-partner identities and cyclic Gram estimates are possible implementations. They are not additional required slots once the form interface is supplied.

For a limiting construction, the margin must survive the same return as the local fields, with \(\ell_r\to\ell>0\). [[positive-semigroup-decay/source-pairing-limit-and-the-mass-gap|The source-pairing limit theorem]] needs convergence only of the relevant reflected pairings and means; the maps, response forms and repairs need not converge. Normalizing a microscopic measure or minimizing a nonnegative action does not by itself supply this margin; [[scale-bearing-descent/causal-action-normalization-and-coercivity|the causal-action calculation]] makes the missing positive-form comparison explicit. A direct Lorentzian route can instead use [[measured-response-carriers/response-to-energy-comparison|the energy-form comparison]] on a physical form core.

## Minimal inventory of what remains unknown

| Missing item | What may be posited now | What would close its type |
|---|---|---|
| Admissible branch for each \(G\) | A realization branch exists in the stable master doctrine | One member for every compact simple group, with compatible pointing and relative calibration |
| Local positive realization | Complete sourced evaluation has a local quantum return | The full package (YS3), or reconstruction data proven to have that strength |
| Yang–Mills identification | The returned operator filtration has Yang–Mills short-distance structure | The mixing-aware dictionary and asymptotic comparison specified in (YS7)–(YS8) |
| Quantitative physical comparison | Stable source response detects and is detected by physical chronology | The complete-source domination (YS10), or another sufficient energy comparison |
| Limit closure, when used | All three interfaces survive one declared limiting family | Source convergence, surviving nontriviality, the required symmetries and one positive physical margin |

The last row is conditional on choosing a limiting construction. It is not an extra obstruction in a direct continuum definition. Vacuum uniqueness and finiteness of the positive edge can follow within the completed return: the complete centered contraction excludes extra zero-energy vectors, and a nonzero nonvacuum carrier with strongly continuous positive evolution has finite-energy spectral support. They must be established somewhere, but need not be independently built twice.

Several claims can therefore be removed from the minimal Clay signature while retained in the wider programme: selecting one preferred gauge group; proving that only \(3+1\) dimensions are possible; constructing record acquisition; classifying every theta sector or anomaly; deriving \(c,G,\hbar\); recovering cosmic acceleration or Higgs matter; proving confinement, an isolated glueball pole or a fully discrete spectrum; and choosing a mass in external units. Split properties, regional tensor factorizations and autonomous clocks for every intermediate readout are also not automatic requirements of the cited Wightman target.

Scale does require care, but no numerical ruler. The [[mass-scale-calibration/scale-torsor-and-the-global-local-gap-invariant|scale-family signature]] lets duration and inverse-duration transform together while the margin in (YS10) stays dimensionless. Exact dilation symmetry inside one fixed vacuum representation is a different condition and need not return.

## The minimal conjectural leap

**Conjecture — a local realization that detects complete comparison.** For every compact simple \(G\), a stable branch of the master marked law admits a nontrivial local realization with the required renormalized Yang–Mills correspondence. On its complete physical source space, the inherited comparison form satisfies (YS10) in the same chronology. Where limits or microscopic presentation choices occur, all these properties belong to one common exact return with a surviving comparison scale.

This posits exactly what is missing without pretending to construct it. Conditional on a valid local Yang–Mills realization, the remaining gap bridge is the quantitative comparison. Conditional on stable upstream comparison, the remaining theory bridge is the local and renormalized realization. Neither can substitute for the other.

The transcendental deduction is consequently a deduction of **required relations**: positivity must be compatible with products; localization with covariance; chronology with the positive cone; the field dictionary with renormalization; and stable comparison with the complete physical norm. The conjectural necessity is that one master law can realize these relations together. Its local action and its mass threshold would then be two returns of the same algebra.
