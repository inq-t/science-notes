---
inq.module: "yang-mills-mass-gap"
inq.include:
  - "**/*.md"
inq.ambient:
  - "**/*.py"
  - "**/*.txt"
---
# Yang–Mills Existence and the Mass Gap

The research programme asks whether prior oriented geometry can determine both the local gauge description and a positive lower bound on its physical excitations. Its strongest kinematic result derives an exceptional stabilizer and a Wilson gauge carrier; its strongest analytic reductions identify the uniform response or correlation estimate that would force a gap. These are connected but different achievements. The interacting four-dimensional continuum construction and its regulator-uniform infrared bound remain open.

## The target is a spectral exclusion, not a spatial pixel

[[puzzle-as-posed|The Clay statement]] requires a nontrivial quantum Yang--Mills theory on \(\mathbb R^4\), for every compact simple gauge group, satisfying the required axioms and having
\[
H\Omega=0,\qquad
\sigma(H|_{\Omega^\perp})\subset[\Delta_E,\infty),
\qquad \Delta_E>0.
\]
The spectrum above the threshold may be continuous. A smallest mass in one theory is not a universal smallest quantity of matter, a discrete ladder of all masses, or a minimum spatial resolution. A one-channel glueball estimate also need not see the bottom of the complete physical spectrum.

[[register-audit|The genuine register correction]] is to distinguish a gauge-dependent gluon field from the gauge-invariant physical translation spectrum. The latter need not arise by adding a gluon mass term. This removes one misleading formulation of the puzzle; it does not show that the actual Clay problem is ill-typed. Likewise, [[spectral-gap-undecidability-firewall|general spectral-gap undecidability]] rules out a universal decision algorithm for a constructed family, not a Yang--Mills-specific proof.

An emergent-spacetime construction is admissible as a research route, but must recover the target observable theory. [[higgs-reduction-as-local-shadow/inq|Higgs reduction]] is a separate local presentation of stabilizer data; pure Yang--Mills must exhibit its gap without a Higgs input.

## Begin with the arrow, then derive its symmetry

The reversal in [[oriented-descent-angle-and-emergent-symmetry|oriented descent]] is precise: specify an oriented operation \(W\), then ask for the automorphisms preserving that operation. A symmetry group can consequently be a stabilizer of prior data, rather than the starting ontology.

[[order-three-orientation-and-the-exceptional-stabilizer|The order-three exceptional construction]] realizes this order of explanation. An oriented operation and pointed idempotent in the exceptional Jordan whole leave \(S(U(2)\times U(3))\). Averaging the cyclic operation forgets its orientation, while the odd residue retains a complex structure on the forgotten complement. This explains a mathematical stabilizer and an orientation-sensitive residue. It does not yet derive physical chirality, the matter spectrum, or a dynamics that selects those initial data.

The neighboring branches retain different information:

| Construction | What its operator acts on and establishes | What is not thereby established |
|---|---|---|
| [[oriented-descent-angle-and-emergent-symmetry|Opposed descents]] | Two state-compatible GNS projections; a lower frame determined by their angle modulo the common retained space | That the common space is only the physical vacuum, or that the angle stays open in a continuum limit |
| [[quantum-g2-categorical-rigidity-and-the-carrier-firewall|Quantum-\(G_2\) rigidity]] | A normalized fusion-averaging defect in an admissible categorical representation | A state-compatible action on the complete neutral Yang--Mills carrier |
| [[s6-descent-defect-and-the-chirality-firewall|\(S^6\) descent]] | Integral monodromy relations and topological residue cancellation; a separate character-bundle coercivity theorem | An identification with the octonionic almost-complex structure, physical chirality, or a physical energy bound |
| [[octonionic-clifford-completion-of-the-color-normal|Octonionic Clifford completion]] | A color-restricted representation, Clifford action, and exact trace ratios | A complete spectral cycle or an interacting field-state coercivity theorem |

This is not four competing numerical guesses. Each supplies a different part of a possible construction. Their meeting point must be an explicit map preserving the relevant state, norm, kernel, and action—not a shared numeral such as three, six, or eight.

## The exceptional normal has two legitimate uses

[[exceptional-wilson-same-carrier-factorization|The finite-graph holonomy-probe construction]] derives a color connection groupoid, a faithful probe, the Wilson plaquette function, and an invariant electric metric from the exceptional geometry. Product Haar measure and the electric/magnetic couplings are separately supplied; the construction does not select the interacting vacuum. It does **not** require a finite-dimensional normal space to become the QFT Hilbert space. The fields are connections; the normal representation probes their holonomy.

The exact representation-trace coefficient is accompanied by its reciprocal kinetic conversion. Thus the trace factor eight is structural, but does not multiply the predicted gap by eight. Once the Wilson carrier is identified, the remaining unknown is the interacting vacuum law and its normalized physical coercivity.

The [[octonionic-clifford-completion-of-the-color-normal|Clifford/spectral-cycle route]] makes a stronger, different proposal: turn that representation into a natural field-valued Clifford response, with operator, grading, real structure, and state. Those data remain to be constructed. Its unfinished status must not erase the holonomy route's existing carrier theorem; conversely, Wilson recovery does not complete the spectral-cycle route.

## A gap means uniform resistance to becoming invisible

A single distinction can be nonzero while a sequence of normalized distinctions becomes arbitrarily cheap. This is why an index, a discrete quotient, or injectivity alone does not prove a spectral gap.

The proposed response takes the form
\[
q[J\psi]\ge\kappa\|J\psi\|_{\mathcal K}^{2},
\qquad
\|J\psi\|_{\mathcal K}^{2}\ge b_J\|\psi\|_{\mathrm{phys}}^{2}.
\]
Here \(J\) analyzes physical states into a specified response carrier. The map, its complex form core, and the response kernel are part of the statement. [[measured-response-carriers/inq|Measured response carriers]] distinguishes algebra, GNS vectors, state tangents, parameter Hessians, and closed-form transport. [[program-core/response-registers|The response ledger]] prevents a Fisher Hessian, a representation trace, a spatial precision, and a Hamiltonian from silently changing types.

The geometric question is therefore whether the **joint observation map has a uniform lower frame** on the entire vacuum complement. [[regional-relative-entropy-frames|Regional entropy frames]] and [[causal-frame-coercivity|causal-frame coercivity]] make this question explicit. In finite dimensions its optimal coefficient is the square of a least singular value. In infinite dimensions, no hidden vector is weaker than no sequence of almost-hidden unit vectors.

The same distinction appears in [[distinction-grain-spectrum/inq|the grain spectrum]]: every tangent may cross a forgetting threshold at some finite scale while those crossing scales have no uniform ceiling. A gap needs uniform control. No spatial pixel is involved.

## One shared response-to-energy implication

[[measured-response-carriers/response-to-energy-comparison|The generic comparison theorem]] states the reusable step. On a complex form core of the physical vacuum complement, suppose
\[
\mathfrak h_{\mathrm{phys}}[\psi]
\ge \eta_{\mathrm{sol}}E_*q[J\psi],
\qquad
\eta_{\mathrm{sol}}>0,\quad E_*>0.
\]
Together with the two lower bounds above, this gives
\[
\boxed{\Delta_E\ge \eta_{\mathrm{sol}}E_*\kappa b_J.}
\]
The implication is elementary; constructing its premises is not. A response gap modulo its kernel requires a lower frame modulo that same kernel. A positive real Hessian must be extended correctly to the complex physical form core. The comparison and scale cannot be chosen by reading the desired gap backward into them.

[[joint-causal-generators-and-the-mass-casimir|The joint-causal Casimir theorem]] handles a further distinction: a boost-rescaled single causal generator can be gapless while a joint invariant of oppositely scaling generators is gapped. After positive-energy Poincare reconstruction, the physical mass invariant is not an arbitrary one of those generators. This is a genuine retyping of the question, not permission to omit the invariant's lower bound.

## Two physical certificates, with different strengths

[[collared-surface-response-to-the-clay-gap|The fixed-slab certificate]] asks for a uniform angle bound on the complete Perron-dressed physical vacuum complement. Under the stationary reversible Markov and OS realization hypotheses of [[past-future-angle-and-the-transfer-gap|the past--future theorem]], the angle at physical separation \(\ell\) obeys
\[
c_F(\ell)=e^{-\ell\Delta_E/(\hbar c)}.
\]
The dimensionless angle, inverse-length decay rate, energy, and invariant mass are successive presentations with specified conversion data. An adjacent-slice angle is expected to close as its spacing vanishes; a fixed physical slab is the appropriate uniform comparison.

[[auxiliary-response-localization/inq|The correlation certificate]] instead needs one common positive physical Euclidean decay exponent on an OS-total family of centered local states. An auxiliary sampler can help prove this static estimate without being physical time: its arbitrary clock cancels between forgetting and influence propagation. This route need not establish the stronger whole-surface angle.

[[rg-covariance-residue/inq|Covariance residues]] give a complementary exact decomposition into discarded-scale fluctuations and a retained infrared term. The Gaussian branch now has [[rg-covariance-residue/multilevel-local-gauge-completion|the actual multilevel conditional law]], [[rg-covariance-residue/accumulated-readout-noise|its exact accumulated noise]], and [[rg-covariance-residue/uniform-gaussian-conditional-locality|depth- and volume-uniform conditional locality]]. The apparent precision pole cancels by gradient compatibility, allowing weighted terminal inversion.

That result is not an infrared gap: the initial Maxwell law remains massless. The outstanding work is the full non-Abelian conditional estimate, renormalized source control, and a positive retained infrared exponent. [[strong-coupling-gap-and-continuum-crossover/inq|The strong-coupling crossover]] explains why an existing fixed-regulator gap does not by itself survive the weak-bare-coupling continuum limit.

## Geometry selects a quotient; a yardstick selects its presentation

[[hessian-response-geometry/relative-response-spectrum|A response spectrum is relative to a metric]]. The invariant is a pair \(q/g\), not the smallest eigenvalue of a coordinate Hessian. Coordinate changes preserve the pair; independent rescaling of the response or comparison metric changes the problem.

[[scale-torsor-and-the-global-local-gap-invariant|The scale-torsor construction]] packages the same distinction across dimensional presentations. A dimensionless rate or ratio can be invariant while a section supplies the displayed time, energy, and mass units. [[the-grain-of-causal-scale/relational-grain-construction|The grain method]] seeks that section by matching independently normalized ledgers on the relevant object. The cosmological \(46\)--\(47\,\mathrm{MeV}\) estimate is not a universal input or an observation pixel.

[[global-local-response-reconstruction/yang-mills-balanced-fisher-grain|The balanced-Fisher candidate]] applies this method to the full blocked Wilson law: recoverable and residual information of a declared scale score form complementary ledgers. A balance point might select a reference scale, but its existence, scheme covariance, and continuum stability remain open. Balance of one score does not replace a lower frame on all physical excitations.

Cosmology can enter through [[global-local-response-reconstruction/cosmological-reconvergence-contract|a reconvergence theorem]]: one upstream construction must yield both the vacuum Yang--Mills theory and a thermal cosmic history. [[global-local-response-reconstruction/trace-source-two-moment-solder|The scale-trace source]] supplies a typed candidate bridge between a thermal one-point response and a vacuum scalar spectral measure. It does not identify those states, determine the full spectrum, or remove the requirement to recover gravity-free pure Yang--Mills.

## The next decisive construction

The fresh task is to make a previously independent lower bound necessary from the same geometry that supplies the carrier.

For the exceptional holonomy route, that means constraining the whole-to-slice vacuum law so that the physical response cannot develop arbitrarily soft neutral directions along a tuned continuum trajectory. For the categorical or automorphic route, it first means constructing the admissible physical action and its vacuum-kernel identification. For the Clifford route, it first means completing the field-valued spectral data.

A successful construction must then carry one uniform physical bound through volume removal and a nontrivial local, positive-energy, Poincare-covariant Yang--Mills reconstruction. A solved \(SU(3)\) case would be major progress; the full Clay quantifier still asks for every compact simple group. The programme's Copernican promise is an economy of explanation that forces these ingredients together—not a relaxation of any one of them.
