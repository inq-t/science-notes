# Register Audit

The audit finds one genuine category mistake and two construction cautions. The mistake is to demand that a gauge-invariant Hamiltonian gap appear as a mass term or pole of a gauge-dependent connection. The cautions are that the interacting observable vacuum is not supplied by the perturbative Fock representation, and that Euclidean decay is not yet a Lorentzian spectrum without a reconstruction theorem. Correcting these registers dissolves the popular paradox; it does not dissolve the Clay problem.

## Category error — the register of the fields

The Yang--Mills Lagrangian is written in terms of a connection \(A\). Perturbation theory produces a massless gauge-fixed gluon propagator, but \(A\) is not a gauge-invariant observable. The physical mass-gap target belongs to the vacuum representation of the gauge-invariant observable algebra, or to an equivalent constrained or BRST construction. It is not determined by the absence of an \(A^2\) term or by the pole of a gauge-dependent two-point function. **[STANDARD]**

This removes the demand that a physical gap must look like a generated gluon mass. It does not remove the dynamical problem. Gauge reduction itself is not a gap mechanism: free Maxwell theory can be quantized on gauge-equivalence classes, with the gauge-invariant field strength generating the observable algebra, and it remains massless. [[program-core/physical-quotient|The physical quotient]] removes redundancy; a state and Hamiltonian on the reduced carrier must still produce the spectral bound.

**[CONJECTURE -- external scenario]** The Gribov--Zwanziger scenario restricts a gauge-fixed configuration space and modifies the gauge-dependent gluon propagator, typically with reflection-positivity violation. This can be evidence against an asymptotic one-gluon state. It is not a gauge-invariant mass-gap theorem, and its propagator parameter must not be identified with the physical gap.

## Caution — the register of the vacuum

Haag's theorem obstructs the ordinary interaction-picture identification of an interacting positive-metric Wightman theory with a free theory in one Fock representation. **[CONDITIONAL THEOREM]** For Yang--Mills the application is conditional twice over: the positive-metric interacting theory is the object whose existence is at issue, and gauge-fixed perturbation theory uses an indefinite-metric auxiliary space outside Haag's hypotheses. The theorem therefore does not directly govern the perturbative gauge-fixed formalism.

The safe warning is that the physical gap belongs to the interacting observable GNS representation; free-Fock poles do not determine it. This is analogous to the programme's warning that a symmetric model may not capture its proposed ground, but Haag's theorem is not a rigorous form of that broader metaphysical claim. Nor does representation inequivalence explain the gap: the interacting state and dynamics still have to be constructed.

## Caution — the Euclidean-to-Lorentzian bridge

A mass gap is a property of a Hamiltonian in a positive-energy representation. In a Euclidean construction, reflection positivity is the indispensable part of the Osterwalder--Schrader bridge: the positive-time algebra is quotiented by the null space of \(\langle\theta F,F\rangle\), and the remaining OS hypotheses reconstruct a Hilbert carrier and positive-energy semigroup. A direct canonical or Hamiltonian construction need not pass through reflection positivity. **[STANDARD]**

Once reconstructed, \(T_a=e^{-aH}\) is injective, although its inverse is generally unbounded. The gap is the logarithmic contraction rate on the vacuum complement,

$$
\Delta_a=-\frac1a\ln\left\|\widetilde T_a(1-P_0)\right\|,
$$

not a residue of noninvertibility. [[lorentzian-spectral-envelope/inq|The envelope module]] distinguishes the OS quotient, a conditional expectation, and the transfer semigroup. The register error would be to infer a physical Hamiltonian spectrum from Euclidean data without reconstruction, not to state the target in Lorentzian terms. Along a continuum trajectory the physical \(\Delta_a\) must remain positive even though the raw per-slice deficit behaves as \(1-e^{-a\Delta}\sim a\Delta\to0\).

## Where the audit places causal scale theory

The programme has one exact but scoped theorem here. For the positive translation generator \(P\) of a dilation-covariant half-sided modular inclusion, \(P=0\) or \(\sigma(P)=[0,\infty)\) ([[the-grain-of-causal-scale/causal-spectrum|the HSMI no-gap theorem]]). A gap in that same generator requires failure of the covariance hypothesis or passage to a different constructed carrier and generator. It does not follow that every pre-wall spectrum is gapless or that a wall automatically creates a gap.

The proposed identification between “residue of descent” and mass gap is therefore not yet correctly typed as an identity. The OS quotient can be noninjective; a conditional expectation is idempotent; the transfer operator is injective and its strict contraction measures the gap. A wall construction may eventually relate them, but it owes an explicit carrier map and intertwining theorem. That obligation, rather than the analogy, is the programme's possible contribution.

## The condition under which the charge reverses

The charge reverses against the programme if it treats gauge reduction as dynamics, equates its conditional expectation with a transfer semigroup, or calls a fixed-cutoff estimate the continuum theorem. A grain mechanism must first prove a regulator-level gap, then volume uniformity and persistence along a controlled continuum trajectory; a physical grain left in place describes a different target from a theory on \(\mathbb R^4\). Likewise, dimensionless algebra can at most predict dimensionless spectral ratios until an independent scale is supplied, by [[deriving-value-of-g/obstructions-to-an-unconditional-proof|the dimensional obstruction]]. Finally, a Euclidean wall construction still owes OS reconstruction, while a direct Lorentzian construction owes the corresponding Hamiltonian axioms. [[mass-gap-no-gos]] states these obligations and their failure conditions.
