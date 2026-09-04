---
inq.module: "distinction-grain-spectrum"
inq.include:
  - "**/*.md"
---
# The Distinction-Grain Spectrum

A grain belongs first to a declared distinction, not to reality in the abstract. Along a nested whole-to-part channel, every square-integrable state tangent has a monotone Fisher ledger measuring how much of that distinction remains recoverable and how much has become inaccessible to the retained presentation. A single tangent may therefore have a finite half-information grain even in a gapless theory; a mass gap is the much stronger statement that the entire nonvacuum grain spectrum has a finite uniform ceiling at fixed physical scale. This converts the grain method into an exact operator criterion without identifying information loss, stochastic ontology, clock energy, or mass.

**Status: [EXACT] for the score-pushforward identity, Fisher decomposition, nested-channel monotonicity, local strong-data-processing coefficient, transfer-semigroup grain theorem, and gapless counterexample; [EXACT CONDITIONAL] for the exterior-collar implication under stationary Markov and positive-transfer hypotheses; [CONSTRUCTION TARGET] for a regulator-uniform Wilson realization; [OPEN] for four-dimensional continuum Yang--Mills and the Type-III/BKM lift.**

## Two grain questions must remain distinct

[[the-grain-of-causal-scale/relational-grain-construction|A matched-ledger grain]] solves an independently normalized equation \(\mathsf C_X=\mathsf B_X(\ell_X)\) and may select a physical ruler appropriate to the object \(X\). The distinction grain defined below asks a different question: given a nested response family and a tangent \(f\), at what scale has a fixed fraction of that tangent ceased to be recoverable? The first can supply an explanatory yardstick; the second measures persistence relative to a supplied yardstick.

For an exact transfer semigroup, the uniform distinction grain is equivalent to the spectral edge. It is therefore a clean characterization and stopping condition, but not by itself a noncircular reason that the edge is positive. The intended Yang--Mills construction needs both arrows, independently:

$$
\boxed{
\text{carrier-relative ledger match selects }\ell_*
\quad+\quad
\eta_F(C_{\ell_*})<1
\text{ on every nonvacuum direction}.}
\tag{DG0}
$$

Using the unknown gap or its measured correlation length to choose \(\ell_*\) would collapse these arrows and make the explanation circular.

## One distinction through one channel

Let \((X,\nu)\) be a standard-Borel probability carrier and let

$$
C:X\leadsto Z
\tag{DG1}
$$

be a parameter-independent Markov kernel between standard-Borel spaces. Its joint law has input marginal \(\nu\), output marginal \(\pi=C_*\nu\), and a regular conditional input law \(\beta_z=\operatorname{Law}(X\mid Z=z)\). The conditional-prediction contraction is

$$
K_C:L^2(\nu)\longrightarrow L^2(\pi),
\qquad
(K_Cf)(z):=\mathbb E_\nu[f(X)\mid Z=z].
\tag{DG2}
$$

Take a bounded real \(f\in L^2_0(\nu)\) and the regular local state path

$$
\mathrm d\nu_\varepsilon
=
(1+\varepsilon f)\,\mathrm d\nu
\tag{DG3}
$$

for sufficiently small \(\varepsilon\). The input score is \(f\). Direct pushforward of (DG3) gives

$$
\frac{\mathrm d(C_*\nu_\varepsilon)}
{\mathrm d(C_*\nu)}
=
1+\varepsilon K_Cf,
\tag{DG4}
$$

so the output score is exactly \(K_Cf\). This is the elementary score form of the missing-information identity and the local form of Fisher monotonicity under statistical reduction; [[library/a-note-on-insufficiency-and-the-preservation-of-fisher-information/inq|Pollard's DQM pushforward theorem]], [[library/finding-the-observed-information-matrix-when-using-the-em-algorithm/inq|Louis's observed-information construction]], and [[library/information-geometry-and-sufficient-statistics/inq|Ay--Jost--Lê--Schwachhöfer's Markov-morphism theorem]] supply primary precedents.

The three Fisher ledgers are therefore

$$
\begin{aligned}
\mathcal I_{\mathrm{in}}(f)
&:=\|f\|_\nu^2,\\
\mathcal I_{\mathrm{rec}}(C;f)
&:=\|K_Cf\|_\pi^2,\\
\mathcal I_{\mathrm{res}}(C;f)
&:=\mathcal I_{\mathrm{in}}(f)-\mathcal I_{\mathrm{rec}}(C;f).
\end{aligned}
\tag{DG5}
$$

Conditional expectation is an orthogonal projection inside the joint \(L^2\) space and gives

$$
\boxed{
\mathcal I_{\mathrm{in}}
=
\mathcal I_{\mathrm{rec}}
+
\mathcal I_{\mathrm{res}},
\qquad
\mathcal I_{\mathrm{res}}(C;f)
=
\int\operatorname{Var}_{\beta_z}(f)\,\pi(\mathrm dz)
=
\langle f,(I-K_C^*K_C)f\rangle.}
\tag{DG6}
$$

All three terms concern the same tangent on the same joint law. On the input carrier, \(K_C^*K_C\) is generally a positive contraction, not a projection; it becomes a projection for an appropriate deterministic statistic. Bounded centered scores are dense in \(L^2_0(\nu)\), so the quadratic identities extend continuously to every centered square-integrable tangent. The result does not say that information is a substance, that the channel chooses an outcome, or that the probability representation is ontologically stochastic.

The phrase *parameter-independent* is load-bearing. If a differentiable family has input density \(p_t(x)\) and channel density \(c_t(z\mid x)\), write

$$
f_t(x):=\partial_t\log p_t(x),
\qquad
u_t(x,z):=\partial_t\log c_t(z\mid x).
\tag{DG6a}
$$

Differentiating the joint density and then marginalizing gives the actual output score

$$
\boxed{
s_t^Z(z)
=
\mathbb E_t\!\left[
f_t(X)+u_t(X,Z)
\mid Z=z
\right].}
\tag{DG6b}
$$

Thus \(K_{C_t}f_t\) is the pushed-forward score only when the channel is fixed, or when the conditional projection of its channel-score term vanishes. A scale-dependent blocking, field redefinition, or carrier identification must carry this connection term explicitly. Fixed-carrier Fisher covariance does not license its omission.

## Nested descent makes the ledger monotone

Let \(C_s:X\leadsto Z_s\) be a family ordered by \(s\geq0\). Assume that for \(t\geq s\) there is another parameter-independent Markov kernel \(R_{t,s}\) with

$$
C_t=R_{t,s}\circ C_s.
\tag{DG7}
$$

The later presentation is therefore obtained from the earlier one by additional forgetting. The score-pushforward identity and the \(L^2\) contraction of conditional expectation give

$$
\mathcal I_{\mathrm{rec}}(C_t;f)
\leq
\mathcal I_{\mathrm{rec}}(C_s;f),
\qquad
\mathcal I_{\mathrm{res}}(C_t;f)
\geq
\mathcal I_{\mathrm{res}}(C_s;f).
\tag{DG8}
$$

Blackwell factorization (DG7) proves the norm monotonicity (DG8), but not by itself the orthogonality of successive losses. For deterministic statistics, or on a dilation in which the retained data form genuinely decreasing sigma-algebras, the contractions are conditional-expectation projections and successive differences form an orthogonal reverse-martingale ledger. [[reverse-prediction-residue-archive/inq|The reverse-prediction archive]] gives that exact transfer realization. One-time endpoint algebras need not be nested. The correct two-sided object is the full exterior algebra outside a widening collar; under the two-sided Markov property, the two endpoint variables are sufficient for predicting the interior from that exterior.

Where \(\mathcal I_{\mathrm{in}}(f)>0\), define the recoverable fraction

$$
r_f(s)
:=
\frac{\mathcal I_{\mathrm{rec}}(C_s;f)}
{\mathcal I_{\mathrm{in}}(f)}
\tag{DG9}
$$

and, for \(0<\alpha<1\), the distinction grain

$$
\boxed{
\ell_\alpha(f)
:=
\inf\left\{
s\geq0:
r_f(s)\leq1-\alpha
\right\}.}
\tag{DG10}
$$

Here \(\inf\varnothing:=+\infty\). The half-information grain is \(\ell_{1/2}(f)\). It is the first scale at which the recoverable and residual ledgers are balanced. With discrete blocking it is a first-crossing scale and equality need not occur. If the output carriers have been placed in one common Hilbert realization, \(s\mapsto K_{C_s}f\) is norm-continuous, \(r_f(0)>1-\alpha\), and \(\lim_{s\to\infty}r_f(s)<1-\alpha\), equality at the first crossing follows from the intermediate-value theorem. Strict decrease is a separate uniqueness condition.

The recoverable fraction is invariant under a regular reparameterization of the auxiliary statistical path that produces \(f\), because \(f\) and every Fisher ledger acquire the same squared tangent factor. Reparameterizing the descent coordinate \(s\mapsto\phi(s)\) instead carries the physical crossing locus covariantly and changes its coordinate value to \(\phi(\ell_\alpha)\). Changing the carrier, tangent, or descent channel defines a different question and may legitimately return a different grain.

## One tangent is not the complete response

For a fixed channel, let \(Q\) be one fixed orthogonal projection with \(QL^2(\nu)\subseteq L^2_0(\nu)\), removing its declared fixed or vacuum directions. The maximal local Fisher retention is

$$
\boxed{
\eta_F(C\mid\nu)
:=
\sup_{\substack{f\in QL^2(\nu)\\f\neq0}}
\frac{\mathcal I_{\mathrm{rec}}(C;f)}
{\mathcal I_{\mathrm{in}}(f)}
=
\|K_CQ\|^2.}
\tag{DG11}
$$

When \(Q=I-P_{\mathbf1}\), this is the fixed-input chi-squared strong-data-processing coefficient and the square of Hirschfeld--Gebelein--Rényi maximal correlation. If further vacuum or fixed directions are removed, it is the corresponding restricted maximal-correlation coefficient. [[library/strong-data-processing-inequalities-and-phi-sobolev-inequalities-for-discrete-channels/inq|Raginsky]] gives the variational identification, while [[library/on-maximal-correlation-hypercontractivity-and-the-data-processing-inequality-studied-by-erkip-and-cover/inq|Anantharam--Gohari--Kamath--Nair]] identifies the same number as a local information-Hessian threshold and warns that it need not be the global relative-entropy contraction coefficient.

Consequently,

$$
\boxed{
Q(I-K_C^*K_C)Q\geq\kappa Q
\quad\Longleftrightarrow\quad
\eta_F(C\mid\nu)\leq1-\kappa.}
\tag{DG12}
$$

Equation (DG12) is a quadratic-form statement on \(QL^2(\nu)\) and quantifies all infinitesimal distinctions in the claimed carrier. Equation (DG10) concerns one selected distinction. A declared tangent can select a useful reference scale, but only the supremum in (DG11) tests the complete nonvacuum response.

## The grain spectrum and its uniform ceiling

For a nested family define the extended-real uniform \(\alpha\)-grain

$$
\boxed{
\ell_\alpha^{\mathrm{unif}}
:=
\inf\left\{
s\geq0:
\eta_F(C_s\mid\nu)\leq1-\alpha
\right\}.}
\tag{DG13}
$$

Under the monotonicity hypotheses and with the same fixed \(Q\), this is exactly the upper envelope of the individual first-crossing grains in \([0,+\infty]\):

$$
\boxed{
\ell_\alpha^{\mathrm{unif}}
=
\sup_{0\neq f\in QL^2(\nu)}
\ell_\alpha(f).}
\tag{DG13a}
$$

The **distinction-grain spectrum** is the collection

$$
\mathscr G_\alpha
:=
\left\{
\ell_\alpha(f):
0\neq f\in QL^2(\nu)
\right\}.
\tag{DG14}
$$

The existence of many finite members of \(\mathscr G_\alpha\) says only that those particular distinctions are eventually forgotten. The boundedness of the entire spectrum is a uniform coercivity statement:

$$
\ell_\alpha^{\mathrm{unif}}<\infty
\quad\Longleftrightarrow\quad
\exists\,s<\infty:
Q(I-K_{C_s}^*K_{C_s})Q\geq\alpha Q.
\tag{DG15}
$$

Thus the gap-like predicate is not “there is a grain.” It is “no normalized nonvacuum distinction has an arbitrarily large persistence grain.”

## Exact transfer-semigroup theorem

Let \(A\geq0\) be self-adjoint on a Hilbert space, let \(Q=I-P_{\ker A}\), and let

$$
P_s=e^{-sA}.
\tag{DG16}
$$

In a stationary positive reversible Markov dilation, \(P_s\) is the one-sided future-prediction contraction. For \(0\neq f\in Q\mathcal H\), its recoverable fraction is

$$
r_f(s)
=
\frac{\|e^{-sA}f\|^2}{\|f\|^2}
=
\frac{1}{\|f\|^2}
\int_{(0,\infty)}
e^{-2s\lambda}\,
\mathrm d\mu_f^A(\lambda).
\tag{DG17}
$$

Every fixed \(f\) has \(r_f(s)\to0\) by dominated convergence, even when positive spectrum accumulates at zero. But if

$$
\delta
:=
\inf\sigma(A|_{Q\mathcal H}),
\tag{DG18}
$$

then spectral calculus gives

$$
\eta_F(P_s)=\|e^{-sA}Q\|^2=e^{-2s\delta}.
\tag{DG19}
$$

Therefore

$$
\boxed{
\ell_\alpha^{\mathrm{unif}}
=
\begin{cases}
\displaystyle
\frac{-\log(1-\alpha)}{2\delta},
&\delta>0,\\[1.1ex]
+\infty,
&\delta=0.
\end{cases}}
\tag{DG20}
$$

At the balanced value \(\alpha=1/2\),

$$
\boxed{
\delta
=
\frac{\log2}{2\ell_{1/2}^{\mathrm{unif}}}.}
\tag{DG21}
$$

This is an exact re-expression of a positive spectral edge, not a derivation of one. It becomes explanatory only if upstream geometry proves a finite uniform grain without consulting \(A\)'s low spectrum.

## Every distinction may have a grain while the theory is gapless

On \(\ell^2(\mathbb N)\), define

$$
Ae_n=\frac1n e_n.
\tag{DG22}
$$

Then \(A\) is positive, injective, and gapless. For every fixed nonzero \(f\),

$$
\|e^{-sA}f\|\longrightarrow0,
\tag{DG23}
$$

so every \(f\) has a finite half-information grain. For the basis distinction \(e_n\),

$$
\ell_{1/2}(e_n)=\frac{n\log2}{2}.
\tag{DG24}
$$

Hence

$$
\sup_n\ell_{1/2}(e_n)=+\infty,
\qquad
\|e^{-sA}\|=1
\quad(s<\infty).
\tag{DG25}
$$

This counterexample is the exact logical boundary needed by the grain programme: per-object finiteness is compatible with arbitrarily soft directions. [[distinction-grain-spectrum/receipts/distinction_grain_spectrum_receipt.py|The distinction-grain receipt]] checks both the semigroup formulas and an infinite-product Markov channel in which one declared tangent is exactly balanced while the complete response remains gapless; [[distinction-grain-spectrum/receipts/distinction-grain-spectrum-receipt-output.txt|its recorded output]] preserves the numerical witness.

## Clock, energy, and mass are downstream presentations

Suppose Osterwalder--Schrader reconstruction identifies

$$
A
=
\frac{H-E_0}{\hbar c}
\tag{DG26}
$$

when \(s\) is physical Euclidean length. Then (DG20) becomes

$$
\boxed{
\Delta_E
=
\frac{\hbar c}{2\ell_\alpha^{\mathrm{unif}}}
\bigl[-\log(1-\alpha)\bigr].}
\tag{DG27}
$$

For the half-information convention,

$$
\Delta_E
=
\frac{\hbar c\log2}
{2\ell_{1/2}^{\mathrm{unif}}},
\qquad
\Delta_M
=
\frac{\hbar\log2}
{2c\,\ell_{1/2}^{\mathrm{unif}}}.
\tag{DG28}
$$

If the semigroup parameter is Euclidean time \(\tau\), the corresponding relation is \(A=(H-E_0)/\hbar\); for Euclidean length \(s=c\tau\), it is (DG26). A dimensionless blocking depth cannot be inserted into (DG27) until a physical temporal lattice spacing or continuum length map has been constructed.

The logarithm comes from converting multiplicative retention into additive attenuation. The number \(1/2\) chooses a balanced reporting convention; any prospective \(0<\alpha<1\) returns the same generator edge through (DG27). Neither \(\hbar\) nor \(c\) creates the grain. They solder a reconstructed clock-length rate to energy units. The quotient \(\Delta_E/c^2\) becomes a physical invariant-mass gap only after OS/Poincare reconstruction and restriction to the zero-spatial-momentum sector; before that step it is merely an energy gap written in mass units.

## The collared whole--local version

For a two-sided stationary Markov path, let \(\mathcal F_s^{\mathrm{ext}}\) be the information outside a widening collar around the midpoint. These algebras decrease with \(s\), so

$$
K_s^{\mathrm{ext}}f
:=
\mathbb E[f(X_0)\mid\mathcal F_s^{\mathrm{ext}}]
\tag{DG29}
$$

has the monotone ledger (DG8). Under the Markov property the collar endpoints are sufficient for the exterior's prediction of the midpoint. Reversibility and positivity give the data-augmentation comparison

$$
Qe^{-2sA}Q
\leq
Q(K_s^{\mathrm{ext}})^*K_s^{\mathrm{ext}}Q.
\tag{DG30}
$$

Thus the independently proved whole--local half-grain bound

$$
\|(K_{\ell_*}^{\mathrm{ext}})Q\|^2
\leq\frac12
\tag{DG31}
$$

implies

$$
\Delta_E
\geq
\frac{\hbar c\log2}{2\ell_*}.
\tag{DG32}
$$

Unlike the one-sided semigroup theorem, this collared criterion is presented only as a sufficient implication: the two-sided boundary can retain more predictive information than either one boundary. [[contemporary-puzzles/yang-mills-mass-gap/collared-surface-response-to-the-clay-gap|The collared-surface theorem]] owns the finite-regulator proof and continuum obligations.

## Yang--Mills interpretation

At finite regulator, assume the Wilson transfer operator is self-adjoint and positivity-preserving, admits a strictly positive Perron ground state, and descends to the complete gauge-invariant slice carrier. Its ground-state transform then defines a stationary reversible Doob path. Each bounded physical tangent \(f\) has a collar grain whenever its recoverable fraction reaches the chosen threshold. The candidate Copernican statement is:

> A glueball mass is not a little substance inserted into a local field. It is the Poincare presentation of a regulator-stable upper bound on how far any nonvacuum physical distinction can remain recoverable through the whole Euclidean law.

That sentence has an exact finite-regulator operator meaning, but the Yang--Mills theorem still requires:

1. an independently selected physical collar scale, such as a successful carrier-relative matched-ledger construction;
2. a proof of (DG31) on the complete Perron-dressed Wilson carrier, uniform in volume, cutoff, and the allowed regulator and boundary data for one fixed gauge group, global form, vacuum sector, and topological angle;
3. survival of the response, scale, vacuum, and forms through the asymptotically free continuum trajectory; and
4. OS/Poincare reconstruction identifying the limit as nontrivial Yang--Mills.

[[global-local-response-reconstruction/yang-mills-balanced-fisher-grain|The balanced-Fisher proposal]] currently supplies only a candidate for clause 1. Its moving-family one-score balance is analogous to one member of \(\mathscr G_{1/2}\), but it belongs literally to that spectrum only after a common transport fixes the input carrier, tangent, and \(Q\) and the transported channels Blackwell-factorize. In either form it cannot establish clause 2. [[global-local-response-reconstruction/inq|Global--Local Response Reconstruction]] keeps the scale selector, complete response, and clock solder as three different arrows.

## Type III and cocycle extension

The commutative theorem uses ordinary scores and conditional expectation. A Type-III version should replace them by:

- a faithful normal reference state or weight;
- a declared monotone state-tangent metric, such as a BKM/Araki relative-entropy Hessian;
- state-preserving completely positive descent maps with a well-defined tangent pushforward;
- a common standard-form or canonical-core comparison carrier; and
- a strict contraction coefficient after the common fixed algebra is removed.

Monotonicity of relative entropy supplies nonexpansion, and Connes cocycles can compare faithful state charts. Neither supplies a strict coefficient, a physical collar, or a clock generator. Equality and recoverability results can identify sufficient directions; the mass-gap task is the quantitative opposite—prove that every nonvacuum physical direction is uniformly nonsufficient at one fixed physical collar. [[contemporary-puzzles/yang-mills-mass-gap/descent-loss-cocycle-and-recovery-fork|The descent-loss cocycle]] proves the Type-III-compatible zero set and its carrier fork, while [[contemporary-puzzles/yang-mills-mass-gap/regional-relative-entropy-frames|regional relative-entropy frames]] state the additional complete-frame obligation. A Type-III grain spectrum remains a construction target until its tangent carrier is mapped to the OS vacuum complement.

## Stopping condition

The new framework has a sharp hierarchy:

1. **Individual grain:** prove one selected \(f\) reaches a prospective Fisher balance.
2. **Grain spectrum:** construct the same nested response for a complete physical tangent carrier.
3. **Uniform ceiling:** derive \(\eta_F(C_{\ell_*})<1\) at an independently selected fixed physical scale.
4. **Mass presentation:** reconstruct the clock and Poincare translations, then apply the logarithmic solder.

The first item can occur in a gapless theory. The third is the dimensionless analytic heart of the gap. The fourth is what makes the word “mass” well typed.
