# Symmetry, Conservation, and Action

The programme distinguishes six mathematical orders that recurring language tends to merge: a homotopy or index class records structural persistence, categorical dimension values a composable correspondence, a Casimir is an invariant polynomial, capacity is a positive quadratic response, charge is linear in a symmetry generator, and an action is a functional on observable histories. A future unification must connect these types through explicit maps rather than call all of them “conservation.”

## Six orders

| Order | Typical object | Variance and sign | What it can establish |
|---|---|---|---|
| Structural class | \([D]\in K^*(\mathcal A)\), a \(KK\)-class, or cyclic class | locally constant under admissible homotopy | persistence of index pairings through changing representatives |
| Categorical valuation | dimension of a dualizable correspondence; matrix dimension with centers | multiplicative under fusion in the appropriate categorical form | compositional capacity across algebra-changing scale transport |
| Casimir | \(C_R\in Z(U\mathfrak g)\) or an invariant norm | fixed within a representation | algebraic sector and norm allocation |
| Capacity | \(g(v,v)\geq0\) | quadratic in the tangent | susceptibility, squared speed, canonical-energy candidate |
| Charge | \(\langle\boldsymbol\mu,\xi\rangle\) | linear in a normalized generator | Noether, Hamiltonian, or boundary balance |
| Action | \(I[\phi]\) | functional of a history or field | equations of motion and variational symmetry |

A structural class can persist while all local metric representatives change, but it is too coarse to determine a response coefficient. A signed charge can reverse under orientation. A squared norm cannot. A Casimir can remain fixed when a state ceases to be invariant. An action may be invariant without every field configuration being invariant.

Entropy, fact, and record are further types:

- entropy accounts for a state in a declared algebra and prescription;
- a fact is a contextual value or outcome; and
- a record is a stable physical encoding.

None is made a charge merely by entering an equation with one.

## The exact involutive Casimir allocation

The proof and its hypotheses live in the shared [[binary-information-geometry/inq|binary-information geometry]] module. Its reusable signature is

$$
Q^*=Q,
\qquad
Q^2=\mathbf1
\quad\Longrightarrow\quad
1=m_\omega^2+\operatorname{Var}_\omega(Q),
$$

where \(m_\omega:=\omega(Q)\). This is **[EXACT]** for every state and self-adjoint involution. Under the additional [[binary-information-geometry/balanced-exponential-family|balanced exponential-family]] hypotheses,

$$
m(\theta)=\tanh\theta,
\qquad
g^{\mathrm{bin}}_{\theta\theta}
=\operatorname{sech}^2\theta,
\qquad
1=m(\theta)^2+g^{\mathrm{bin}}_{\theta\theta}.
$$

The unit is the representation normalization \(Q^2=\mathbf1\). Balance selects the centered coordinate profile; it does not establish a gravitational interpretation.

It does not say that:

- susceptibility is gravitational area;
- polarization is an actual fact;
- the two terms are energies;
- the identity is a conserved spacetime current; or
- the full wall has only one binary channel.

Those are separate identifications and constructions.

## Indiscernibility does not cross the Noether gap

An observational quotient follows from a declared equivalence relation. Noether conservation additionally requires:

1. a continuous group or Lie-algebra action;
2. a phase space or covariant presymplectic structure;
3. a normalized generator \(\xi\);
4. an invariant action or Hamiltonian structure;
5. a moment map or current; and
6. boundary conditions and flux accounting.

Only then can one write a well-typed balance such as

$$
\boxed{
Q_\xi[\Sigma_2]
-Q_\xi[\Sigma_1]
+\mathcal F_\xi[W]=0.}
$$

Gauge symmetry may yield a constraint or boundary charge rather than a bulk Noether charge. A discrete reflection may yield a grading or selection rule but no ordinary infinitesimal current. A one-sided semigroup may encode record preservation without admitting an inverse. [[conservation-of-causal-charge/indiscernibility-and-the-noether-gap|The Noether-gap note]] develops these distinctions.

## The prospective common charge

If state, gravitational, material, and record sectors carry one common continuous action, their moment maps may be embedded in one dual Lie algebra. Taking the state sector to include matter, write

$$
\boxed{
\boldsymbol\mu^{\mathrm{causal}}_\Sigma
=\boldsymbol\mu^{\mathrm{state+matter}}_\Sigma
+\boldsymbol\mu^{\mathrm{grav}}_\Sigma
+\boldsymbol\mu^{\mathrm{record}}_\Sigma
\in\mathfrak g_c^*.}
$$

The charge associated with a normalized generator is

$$
Q_\xi[\Sigma]
:=\left\langle
\boldsymbol\mu^{\mathrm{causal}}_\Sigma,\xi
\right\rangle.
$$

These equations are **[CONJECTURE — CHARGE LEVEL]**. They presuppose compatible embeddings. If matter is instead assigned its own moment map, it must be removed from the state summand so that it is not counted twice. Gauge constraints may prevent a Cartesian factorization; a combined covariant presymplectic object is prior to any decomposition into addends.

The intended conservation statement is about the flux-inclusive whole, not a substance that migrates from “information” into “space.”

## How compositional capacity could meet response and charge

For dualizable factor correspondences,

$$
d(X_{32}\boxtimes X_{21})
=d(X_{32})d(X_{21}),
$$

so \(\log d\) is additive under fusion. This is the strongest current candidate for a quantity that remains exact through the wall: it is a monoidal valuation, not a time-conserved Noether charge. With centers, the functorial object is a matrix dimension or the full correspondence. [[spectral-wall-descent/finite-index-area-weld|The finite-index area weld]] shows, only for a type-I product state and an auxiliary tracial expectation on the same multiplicity factor, how a chosen input edge entropy and its tracial defect partition that factor's log-dimension.

The plausible bridge is a common variational structure:

$$
\text{relative-entropy Hessian}
\longleftrightarrow
\text{canonical energy}
\longleftrightarrow
\text{second variation of a charge or action}.
$$

More precisely, controlled AdS calibration seeks the retained-response equality

$$
g^{\mathrm{BKM}}_{\mathrm{ret}}(v,v)
=
\mathcal E^{(1)}_{\mathrm{can}}
(\mathfrak S v,\mathfrak S v).
$$

The coefficient is supplied separately by the central density equation

$$
\mathcal L_\chi(U)=\eta_*\mathcal A_D^Z(U).
$$

Together these can place categorical capacity, quadratic state response, and gravitational Noether structure in one theory without identifying any of them with the linear charge. The density \(\eta_*\) must remain symbolic until the correspondence and spectral area sides are independently calculated.

## Why this is not yet least action

A relative-entropy Hessian is a local second-order response at coincidence. It does not imply that physical histories minimize relative entropy, BKM length, or capacity. More fundamentally, the pre-observable wall need not be variational at all. A least-action claim on the descended observable carrier would require a history functional such as

$$
\mathcal S_{\mathrm{CI}}
[\text{state},\text{geometry},\text{records}]
$$

with a declared domain, boundary terms, admissible variations, and stationary equations yielding the descended gravitational response, observable constraints, matter dynamics, and any proposed record dynamics. No such common observable functional is currently defined, and its existence would not make the upstream wall variational.

Einstein--Hilbert gravity can be written in the areal-modulus basis as

$$
\frac{S_{\mathrm{EH}}}{\hbar}
=\frac{\eta_{\mathrm E}}{4\pi}
\int R\,\mathrm dV_g.
$$

This is an exact reparameterization after Einstein gravity and its normalization have been assumed. It neither makes the wall BKM metric an action nor derives \(\eta_{\mathrm E}\). [[spectral-wall-descent/observable-spectral-action|The observable spectral-action analysis]] places Connes' variational functional on the downstream side of the wall and proves that its bulk value cannot determine a context-dependent entropy defect. [[philosophy/principle-of-least-action/inq|The least-action module]] owns the general variational distinctions.

## The escort tangent is not the binary translation

For the literal two-state specialization

$$
\rho_0=\frac{\mathbf1}{2},
\qquad
\rho_\theta=\frac{e^{\theta Q}}{2\cosh\theta},
$$

one has

$$
K_\theta=-\ln\rho_\theta
=-\theta Q+\ln(2\cosh\theta)\mathbf1,
$$

so its entanglement capacity is

$$
C_E(\rho_\theta)
=\operatorname{Var}_{\rho_\theta}(K_\theta)
=\theta^2\operatorname{sech}^2\theta.
$$

At the self-dual point,

$$
g^{\mathrm{BKM}}_{\theta\theta}(0)=1,
\qquad
C_E(\rho_0)=0.
$$

Thus translation in the binary exponential coordinate is not temperature rescaling of the modular Hamiltonian of that same reduced state. A larger wall sector may still possess an escort tangent whose sufficient binary reduction preserves the physical norm, but that requires a reduction theorem. It cannot be supplied by terminology or multiplicity alone. [[binary-information-geometry/escort-tangent-no-go|The escort-tangent no-go]] is constitutional for the programme.

## Facthood is a further layer

Selection of a section, state, or polarization can reduce the manifest symmetry from \(G\) to the stabilizer subgroup of the selected object while the equivariant law remains \(G\)-symmetric. This supplies a precise model of “symmetry breaking without destruction of the underlying symmetry.” It still does not actualize an outcome.

A completed causal-conservation theory must therefore coordinate, without conflation:

$$
\text{persistent algebraic class},
\quad
\text{noninvertible wall},
\quad
\text{equivariant observable law},
\quad
\text{state response},
\quad
\text{linear charge},
\quad
\text{contextual fact},
\quad
\text{persistent record}.
$$

The last two are essential if the result is to describe a cosmos as a history rather than only a family of states.
