# Why There Is an Action

Composition can partly ground the form of an action without presupposing stationarity. Nonzero complex scalar weights that multiply under concatenation have additive logarithms modulo their branch ambiguity; phase-only weights give a circle-valued action. Absolute continuity can supply a density along each history, but not a finite-jet local Lagrangian. Stationary phase additionally needs a defined integration problem and controlled asymptotics. A separate exact route reconstructs a stationary state action from a quotient clock.

## The composition argument

Histories concatenate. If $\gamma_1$ runs from $a$ to $b$ and $\gamma_2$ from $b$ to $c$, there is a history $\gamma_2\circ\gamma_1$ from $a$ to $c$. Suppose each history carries a nonzero complex scalar weight $W(\gamma)\in\mathbb C^\times$ and require

$$
W(\gamma_2\circ\gamma_1)=W(\gamma_2)\,W(\gamma_1).
$$

Then $A:=\log W$ is additive over concatenation modulo $2\pi i\mathbb Z$:

$$
A(\gamma_2\circ\gamma_1)=A(\gamma_2)+A(\gamma_1)
\pmod{2\pi i\mathbb Z}.
$$

An arbitrary abelian group need not possess such a logarithm; the target group is part of the hypothesis. Noncommuting transport in general requires an operator-valued or path-ordered description rather than this scalar identity. For positive real weights the real logarithm is unambiguous; phase-only weights retain the lift issue below.

Along a parametrized history, choose a compatible additive lift where one exists. An additive interval function need not be an integral—a singular measure or a crossing count is additive too. If the lifted increment defines an absolutely continuous finite-variation measure on each finite interval, Radon–Nikodym gives an integrable density along that history:

$$
A(\gamma)=\int_\gamma\mathcal L .
$$

This does not prove that $\mathcal L$ depends only on position, a field and finitely many derivatives. Finite-jet locality and compatibility among histories are additional requirements. Nor has the history parameter thereby become physical clock time.

Adding $|W|=1$ makes $\mathcal L$ imaginary and yields

$$
\boxed{
W(\gamma)=e^{\,iS[\gamma]/\hbar},
\qquad
S=-i\hbar\log W .
}
$$

Unimodularity is a further postulate and not a consequence of unitarity, which constrains the evolution operator rather than the weight of an individual history: Euclidean weights $e^{-S_E}$ obey the same composition law without it. Nothing in the argument asserts that anything is minimized, and it never mentions stationarity.

## The action is circle-valued

On $U(1)$ the logarithm is multivalued, so additivity holds modulo $2\pi i$ and the reconstruction produces an $\mathbb R/2\pi\hbar\mathbb Z$-valued functional. Lifting it to a genuine $S:\mathcal H\to\mathbb R$ is an extra hypothesis, and the obstruction is not an artifact — it is the same ambiguity that makes theta angles, Wess--Zumino terms, and Dirac quantization meaningful, and it is why [[what-the-axiom-asserts]] records that the quantum weight is sensitive to the action only modulo $2\pi\hbar$.

## Stationarity as a shadow

Stationarity can then arrive as an asymptotic statement rather than a postulate, but only after an oscillatory integral and an asymptotic family are defined. For a smooth finite-dimensional phase and compactly supported amplitude away from critical points, integration by parts suppresses the nonstationary contribution as the phase parameter grows. Nondegenerate critical points admit the corresponding stationary-phase expansion. A functional-integral or regulator limit requires further control; a multiplicative weight alone supplies neither that integral nor its measure. [[quantum-action]] owns the physical interpretation and its qualifications.

The possible inversion is precise: a composition law can precede the action, and a controlled stationary-phase theorem can explain a classical stationary description. This is not a universal derivation of physical dynamics from composition.

## What the argument grounds

| Grounded, given the hypotheses named above | Not grounded here |
|---|---|
| that the weight is exponential in an additive functional | the multiplicative composition law itself |
| that a compatible lifted increment has an integral density along a history | absolute continuity, finite-jet locality and compatibility among histories |
| that the density is imaginary, given $\vert W\vert=1$ | unimodularity |
| stationary-phase asymptotics for an integral satisfying its hypotheses | the integration problem, measure, limiting control, specific Lagrangian, field content and couplings |
| | the lift from a circle-valued to a real-valued action, and the existence and value of $\hbar$ |

The composition law assumes factorization through segments on the declared history category. It need not imply a finite-memory evolution on a smaller state space. Within a separately established local variational class, symmetry and field content can constrain a Lagrangian; [[philosophy/symmetry-principle/inq|the invariance axiom]] and [[symmetry-groups-select/inq|symmetry selection]] own that different selection question.

## An exact state-action return from a directed process

[[algebra/quotient-clock-and-stationary-action|The quotient-action theorem]]
does not start with scalar history weights. It begins with a one-sided
linear process and a complex semidefinite realization. When the process
induces a continuous unitary quotient, the quotient form supplies a
symplectic state space and the derivative of that same process supplies its
Hamiltonian. The resulting Schrödinger state action is exact, not a
stationary-phase limit. [[directed-analytic-realization/inq|An explicit
analytic-tail member]] calculates the form and generator from future
translation and a mean pairing. It still imports the analytic tail class
and process parameter, and does not supply a spacetime-local action.

[[algebra/cauchy-response-and-local-action|Opposed Cauchy response]]
now gives a stronger special case. Two boundary graphs supply a positive
pair norm and Green form; their common normal-response rate supplies the
clock. The same state action becomes
\(p\dot q-\tfrac12(p^2+qA^2q)\) after an endpoint correction. When the
geometrically derived \(A^2\) is a local Laplacian, eliminating \(p\)
returns a local wave-action integral. The boundary geometry and
clock-realization rule remain declared inputs; a gapped but nonlocal
\(A^2\) fails this return, as the
[[directed-analytic-realization/three-dimensional-boundary-test|finite-cap test]]
demonstrates.

## The shape of answer this project wants

The argument replaces a teleological-sounding principle with a structural one: not that nature optimizes, but that an arena in which histories compose multiplicatively carries an additive functional along them. That is the pattern [[cosmodynamics/inq|cosmodynamics]] asks for, and a candidate instance of the demand in [[sufficient-reason/inq|Sufficing and Necessitating Reason]] that a structure be shown necessary rather than exhibited. It remains a reconstruction: until the composition law, absolute continuity, and unimodularity are themselves grounded, the variational axiom has been moved rather than eliminated.
