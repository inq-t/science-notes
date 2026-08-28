---
inq.module: "noether-conservation"
inq.include:
  - "**/*.md"
---
# The Noether Synthesis

The third principle is not an axiom but a theorem, and it is what the first two are for. Given an action and a continuous group with finitely many parameters that leaves that action invariant up to a boundary term, every generator yields a current conserved along solutions. The two hypotheses enter at two different places in one identity, so neither can be dropped and neither substitutes for the other. The synthesis needs more than the plain conjunction of the axioms as ordinarily stated, because the invariance must be of the action rather than of the laws — an upgrade that famous symmetries fail.

## The identity

For a local action $S[\phi]=\int\mathcal L\,\mathrm d^dx$ with Euler--Lagrange expressions $E_a$, the variational axiom supplies an off-shell pointwise decomposition of any variation, and the invariance axiom makes the symmetry variation of $\mathcal L$ a pure divergence. With $\xi^\mu_k$ the coordinate part of the $k$-th generator and $Q^a_k$ its characteristic,

$$
\boxed{
j^\mu_k=\Theta^\mu[Q_k]+\mathcal L\,\xi^\mu_k-K^\mu_k ,
\qquad
\partial_\mu j^\mu_k=-E_a\,Q^a_k
\;\xrightarrow{\ \text{on shell}\ }\;0 .
}
$$

[[what-the-synthesis-requires]] derives this and fixes the hypotheses. Three are easy to lose: the invariance must hold locally rather than for the integral over one fixed region; the transport term $\mathcal L\xi^\mu_k$ is required for any symmetry that moves the coordinates, so dropping it costs the energy; and a current becomes a number only with boundary control, the complete form being the flux-inclusive balance of [[conservation-of-causal-charge/diagonal-charge-balance|Diagonal Charge Balance]].

## The synthesis is not a plain conjunction

The invariance axiom is naturally stated about laws; the theorem needs it about the action. Kepler's rescaling maps solutions to solutions and rescales the action, so it is a symmetry of the laws and yields nothing; the general nesting, its strictness, and the re-typing this forces are established in [[philosophy/symmetry-principle/invariance-of-what|invariance of what]].

## The converse, and why it matters more than the theorem

[[variational-versus-dynamical-symmetry]] gives the direction usually omitted. For a variational system that is normal and totally nondegenerate there is a one-to-one correspondence between equivalence classes of conservation laws and equivalence classes of variational symmetries. Conservation therefore has no brute instances: every conserved quantity has a symmetry as its reason, which is a rare case of the demand in [[sufficient-reason/inq|Sufficing and Necessitating Reason]] being met by a theorem rather than by a programme.

The correspondence needs *symmetry* read broadly. The Runge--Lenz vector is conserved and is the charge of no point symmetry; admitting generalized symmetries, whose generators depend on velocities, restores the bijection.

## Where it stops

[[second-theorem-and-gauge]] handles the case that matters most here. A symmetry parameterized by arbitrary functions falls under the second theorem, whose output is one off-shell identity per gauge parameter among the equations of motion rather than new conserved quantities. Physical charges relocate to boundaries and belong to the transformations acting nontrivially there: energy in general relativity is not a bulk Noether charge, is the ADM surface charge where boundary conditions supply an asymptotic time translation, and becomes a conserved volume integral only with further structure such as a timelike Killing vector.

Under-determinacy is the common cause: a gauge system cannot be put in Cauchy--Kovalevskaya form, so it fails the normality the converse requires, in exactly the theories where the first theorem was already the wrong instrument.

[[where-the-synthesis-fails]] collects the register — no action, symmetry of the equations only, discrete symmetry, one-sided semigroup, gauge symmetry, no time-translation symmetry of the action, non-invariant measure, boundary failure, degeneracy. Nearly every entry is live in the setting this project works in, so the default is that there is no conservation law until each has been answered.

## Relation to the programme ledger

The programme's application of the theorem is owned elsewhere. [[program-core/symmetry-conservation-and-action|Symmetry, conservation, and action]] keeps Casimir, capacity, charge, and action apart as four types and lists six requirements whose joint output is the flux-inclusive charge balance $Q_\xi[\Sigma_2]-Q_\xi[\Sigma_1]+\mathcal F_\xi[W]=0$. The Lagrangian identity above delivers strictly less than that — a conserved current, which discharges the first of those requirements. A normalized generator, a moment map, boundary conditions, and flux accounting are still owed before a charge exists.

[[program-core/axioms-and-principles|The axiom and principle ledger]] records the commitment as construction axiom CA7: a continuous group action together with a presymplectic/Hamiltonian or Lagrangian structure, a normalized generator, a moment map or Noether current, and a boundary-flux law. The register in [[where-the-synthesis-fails]] is the general reason that list has the entries it does.

## Claim levels

| Status | Content |
|---|---|
| **[EXACT]** | the off-shell pointwise decomposition $\delta\mathcal L=E_a\delta\phi^a+\partial_\mu\Theta^\mu$; the current $j^\mu_k=\Theta^\mu[Q_k]+\mathcal L\xi^\mu_k-K^\mu_k$ and the identity $\partial_\mu j^\mu_k=-E_aQ^a_k$ |
| **[STANDARD]** | Noether's first theorem for a finitely-parameterized Lie group of variational symmetries; the second theorem's off-shell identities for function-parameterized groups; $\nabla^\mu G_{\mu\nu}\equiv0$ as the diffeomorphism Noether identity; the Runge--Lenz vector as the charge of a generalized symmetry; ADM energy as a boundary charge for an asymptotic time translation |
| **[CONDITIONAL THEOREM]** | the converse correspondence between conservation laws and variational symmetries, for normal and totally nondegenerate systems with generalized symmetries admitted and trivial classes quotiented; conservation of a charge given flux control; a conserved volume energy given a timelike Killing vector |
| **[NO-GO]** | a symmetry of the equations alone yields no current, witnessed by Kepler rescaling; a gauge symmetry yields on-shell-trivial currents rather than physical charges |
| Not delivered | which group; which action; the value of any charge; actuality of an outcome; any conservation law in a theory whose action has not been constructed |
| **[OPEN CONSTRUCTION]** | whether the causal-wall sector admits an action at all; whether its candidate symmetries are continuous, discrete, or one-sided; the boundary accounting for a causal horizon |

The project-specific construction target belongs to [[conservation-of-causal-charge/theorem-programme|the causal-charge theorem programme]].
