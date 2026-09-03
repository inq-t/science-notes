# Register Audit

The popular Yang--Mills paradox is not one mistake but a stack of type errors: a gauge-fixed presentation is substituted for the observable theory, a formal expansion for the nonperturbative function, an ultraviolet limiting law for a fixed quantum member, and a Lagrangian coefficient for a spectral property. Removing those substitutions explains why massless perturbative gluons do not contradict a positive physical gap. It does not solve the Clay problem, whose hard content is to construct the observable carrier and prove a positive dimensionless infrared ratio uniformly through infinite volume and continuum removal.

**Status: [STANDARD TYPE DISTINCTIONS; SCOPED TOPOLOGICAL OBSTRUCTION; OPEN CONTINUUM COERCIVITY PROBLEM].** The audit dissolves an apparent contradiction, not the existence-and-gap theorem.

## Presentation is not the presented object

The Yang--Mills connection \(A\) is a coordinate-bearing presentation of gauge data. A gauge-fixed gluon propagator belongs to that presentation; the physical gap belongs to the vacuum representation of the gauge-invariant observable algebra, or to an equivalent constrained or BRST construction after its physical quotient has been justified. The absence of an \(A^2\) term and a massless gauge-dependent perturbative pole therefore do not decide the physical Hamiltonian spectrum. **[STANDARD]**

This is a genuine category correction, but gauge reduction is not a gap mechanism. Free Maxwell theory also has a gauge quotient and gauge-invariant field strengths, yet remains massless. [[program-core/physical-quotient|The physical quotient]] removes redundancy; the physical state and dynamics must still yield coercivity.

Gauge fixing also need not be one global chart. [[library/some-remarks-on-the-gribov-ambiguity/inq|Singer's obstruction]] proves, for the compact-base nonabelian configuration classes treated there, that no continuous global choice of one connection representative exists. The safe lesson is atlas-like: local gauge sections require transition data, while gauge-invariant observables live on the quotient. It would be an overreach to turn that scoped obstruction into a claim that every gauge choice fails locally, or that chart topology itself creates a spectral gap.

**[CONJECTURE -- external scenario]** The Gribov--Zwanziger construction restricts a gauge-fixed configuration region and modifies the gauge-dependent gluon propagator, often with reflection-positivity violation. This may diagnose the absence of an asymptotic one-gluon state. It is neither a gauge-invariant mass-gap theorem nor a license to identify its propagator parameter with the physical gap.

## A formal series is not the nonperturbative function

Perturbation theory expands around \(g=0\). A transmutation scale has schematic weak-coupling behavior

$$
\Lambda_{\mathsf s}
\sim
\mu\,
\exp\!\left[-\frac{1}{2\beta_0g^2(\mu)}\right]
\times
\text{powers of }g,
$$

with convention and scheme dependence suppressed. The exponential is flat at \(g=0\): its Taylor coefficients there vanish even though it is nonzero for \(g>0\). Consequently, a massless result at every finite perturbative order does not imply that the completed observable theory has zero gap. **[STANDARD ASYMPTOTIC-FREEDOM INTERPRETATION]**

The converse is equally important. Failure of ordinary perturbation theory to see \(\Lambda_{\mathsf s}\) does not prove that \(\Delta_E>0\), and expected renormalon, transseries, or non-Borel phenomena in four-dimensional Yang--Mills are not substitutes for a constructive theorem. They diagnose why one representation is incomplete, not what the completed spectrum must be.

## An ultraviolet limit is not the whole trajectory

Asymptotic freedom says, perturbatively, that the running coupling tends toward the Gaussian ultraviolet fixed point. It does not say that a fixed interacting quantum theory at nonzero \(\Lambda_{\mathsf s}\) is exactly dilation invariant at all scales. Nor is a rigorously constructed free ultraviolet scaling limit of four-dimensional pure Yang--Mills currently available to be silently assumed as part of the Clay solution.

The correct positive statement is about a one-scale *family*. With the convention that a dilation enlarges lengths by \(e^s\), one may seek comparison maps of the form

$$
\mathfrak D_s:
\mathfrak T_\Lambda
\longrightarrow
\mathfrak T_{e^{-s}\Lambda}.
\tag{R1}
$$

Family covariance (R1) is compatible with every fixed member \(\mathfrak T_\Lambda\), \(\Lambda>0\), failing to possess an internal dilation symmetry. If its physical gap obeys

$$
\Delta_E(\Lambda)=\kappa\Lambda,
\tag{R2}
$$

then covariance fixes the homogeneity of the gap but not the strict positivity of the dimensionless coefficient \(\kappa\). Proving \(\kappa>0\) is the mass-gap problem after the scale register has been corrected. [[mass-as-casimir-and-realization#A fixed member may be gapped while the family is scale covariant|The fixed-member/family distinction]] makes the torsor statement precise.

## A coefficient is not a spectral property

A mass parameter in a quadratic Lagrangian is one sufficient way for a free field to acquire a gapped one-particle dispersion relation. It is not the definition of mass in an interacting relativistic theory. The physical invariant is the joint translation spectrum:

$$
\operatorname{sp}(P)
\subseteq
\{0\}
\cup
\left\{
p\in\overline V_+:
p^\mu p_\mu\geq m_*^2c^2
\right\}.
\tag{R3}
$$

Thus one must not infer “no gap” from a missing bare mass coefficient, nor infer the observable gap from a pole or parameter belonging to a gauge-dependent two-point function. [[joint-causal-generators-and-the-mass-casimir]] gives the sharper reversal: individually gapless null-translation generators can possess a strictly positive joint Poincare Casimir.

## A number is not yet a physical quantity

Geometry or algebra may determine a dimensionless constant \(\kappa\). An energy gap requires a separately normalized quantity \(E_*\):

$$
\Delta_E=\kappa E_*.
\tag{R4}
$$

In pure four-dimensional Yang--Mills the native candidate is a renormalization-group scale \(\Lambda_{\mathrm{YM}}^{(\mathsf s)}\), after a scheme and renormalization condition are declared. A scheme change rescales \(\Lambda_{\mathrm{YM}}^{(\mathsf s)}\) and the reported coefficient reciprocally; the physical product is invariant. A dimensionless octonionic, cusp, flux, or entropy invariant cannot become MeV merely by multiplication with \(G\), a fitted cosmic rate, or a chosen Unruh acceleration unless an independent same-carrier theorem explains why that quantity is the Yang--Mills yardstick.

The family \(\{\mathfrak T_\Lambda\}_{\Lambda>0}\) is scale-torsor-like: ratios between members are meaningful before one member is assigned a numerical unit. Coupling to a metrological or external sector may point the torsor and express the gap in joules, but the pure-theory theorem must first show the scale-free statement \(\Delta_E/\Lambda_{\mathrm{YM}}^{(\mathsf s)}>0\).

## Finite cutoff is not continuum, and confinement is not the gap

A positive spectral estimate at finite lattice spacing and finite volume is not the target theorem. The physical statement requires a bound in renormalized units that survives both infinite volume and the tuned weak-bare-coupling continuum trajectory. A per-link or raw-transfer deficit may tend to zero while the physical gap stays fixed; the conversion factor is part of the theorem.

This also explains why a strong-coupling cluster or Dobrushin estimate is a precedent rather than an answer. The continuum trajectory approaches weak bare coupling. A useful block inequality must be proved after ultraviolet modes are integrated to an independently fixed physical block scale and must remain uniform as the number of microscopic links per block diverges. [[gauge-descent-flux-fisher-coercivity#The renormalization-group crossover is the bridge|The block route]] is therefore the ultraviolet-to-infrared crossover problem in quantitative form, not a way around renormalization.

Confinement is also not synonymous with a mass gap. An area law, absence of colored asymptotic states, positivity of the lowest glueball energy, and a uniform vacuum-complement spectral lower bound are different statements. Any implication among them needs hypotheses and a proof.

## The interacting vacuum is not the free Fock vacuum

Haag's theorem obstructs the ordinary interaction-picture identification of an interacting positive-metric Wightman theory with a free theory in one Fock representation. **[CONDITIONAL THEOREM]** Its direct use for Yang--Mills is conditional twice over: the positive-metric interacting theory is the object whose existence is at issue, while covariant gauge-fixed perturbation theory uses an indefinite-metric auxiliary space outside Haag's hypotheses.

The safe conclusion is that the physical gap belongs to the interacting observable GNS representation; free-Fock poles do not determine it. Representation inequivalence still does not explain the gap. The interacting state, carrier, and dynamics must be constructed.

## Euclidean decay is not yet Lorentzian spectrum

A mass gap is a property of a positive-energy representation. In a Euclidean route, reflection positivity is one indispensable part of the Osterwalder--Schrader bridge: the positive-time algebra is quotiented by the null space of \(\langle\theta F,F\rangle\), and the remaining OS hypotheses reconstruct a Hilbert carrier and positive-energy semigroup. A direct Hamiltonian construction may instead establish the Lorentzian axioms without OS reconstruction. **[STANDARD]**

Once reconstructed, \(T_a=e^{-aH/(\hbar c)}\) is injective, although its inverse is generally unbounded. The gap is the logarithmic contraction rate on the vacuum complement,

$$
\Delta_E
=
-\frac{\hbar c}{a}
\ln\left\|\widetilde T_a(1-P_0)\right\|,
$$

not a residue of noninvertibility. [[lorentzian-spectral-envelope/inq|The envelope module]] distinguishes the OS quotient, a conditional expectation, and the transfer semigroup. A wall construction may relate them only through explicit carrier maps and intertwiners.

## Where the theorem now lives

After the category errors are removed, the surviving problem is remarkably concentrated:

1. construct a gauge-invariant continuum carrier, vacuum, observable net, and Poincare translations;
2. find a presentation or dual carrier on which the infrared distinction form is structurally positive;
3. prove a quantitative comparison between that form and the physical Poincare Casimir without defining either from the desired spectrum;
4. transport the bound across the ultraviolet-to-infrared RG crossover, uniformly in volume and regulator removal; and
5. prove that the resulting dimensionless coefficient \(\kappa=\Delta_E/\Lambda_{\mathrm{YM}}^{(\mathsf s)}\) is positive.

The Copernican reversal is therefore legitimate but demanding: seek a carrier on which the gap is a geometric coercivity theorem rather than a mysterious mass term, then prove that this carrier reconstructs the same Yang--Mills theory. A merely suggestive duality, a fixed-cutoff estimate, or a scale fitted from the answer has changed the presentation without reaching the theorem.
