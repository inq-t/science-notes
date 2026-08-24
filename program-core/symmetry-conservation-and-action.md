# Symmetry, Conservation, and Action

The programme distinguishes four mathematical orders that recurring language tends to merge: a Casimir is an invariant polynomial, capacity is a positive quadratic response, charge is linear in a symmetry generator, and an action is a functional on histories. A future unification must connect these types through explicit maps rather than call all of them “conservation.”

## Four orders

| Order | Typical object | Variance and sign | What it can establish |
|---|---|---|---|
| Casimir | \(C_R\in Z(U\mathfrak g)\) or an invariant norm | fixed within a representation | algebraic sector and norm allocation |
| Capacity | \(g(v,v)\geq0\) | quadratic in the tangent | susceptibility, squared speed, canonical-energy candidate |
| Charge | \(\langle\boldsymbol\mu,\xi\rangle\) | linear in a normalized generator | Noether, Hamiltonian, or boundary balance |
| Action | \(I[\phi]\) | functional of a history or field | equations of motion and variational symmetry |

A signed charge can reverse under orientation. A squared norm cannot. A Casimir can remain fixed when a state ceases to be invariant. An action may be invariant without every field configuration being invariant.

Entropy, fact, and record are further types:

- entropy accounts for a state in a declared algebra and prescription;
- a fact is a contextual value or outcome; and
- a record is a stable physical encoding.

None is made a charge merely by entering an equation with one.

## The exact involutive Casimir allocation

Let \(\omega\) be any state and let \(Q\) be a self-adjoint involution:

$$
Q^*=Q,
\qquad
Q^2=\mathbf1.
$$

Writing \(m_\omega:=\omega(Q)\), one has

$$
\operatorname{Var}_\omega(Q)
=\omega(Q^2)-\omega(Q)^2
=1-m_\omega^2,
$$

and hence

$$
\boxed{
1=m_\omega^2+\operatorname{Var}_\omega(Q).}
$$

This identity is **[EXACT]** for every such state and involution. It is the second-moment Casimir allocation; it requires neither a balanced state nor an exponential family.

The familiar profile is more specialized. Let

$$
P_\pm=\frac{\mathbf1\pm Q}{2},
$$

and choose a reference state satisfying

$$
[\rho_0,Q]=0,
\qquad
\operatorname{Tr}(\rho_0P_+)
=\operatorname{Tr}(\rho_0P_-)
=\frac12.
$$

Define the normalized exponential family

$$
\rho_\theta
:=
\frac{e^{\theta Q/2}\rho_0e^{\theta Q/2}}
{\operatorname{Tr}(\rho_0e^{\theta Q})}.
$$

Then \(\operatorname{Tr}(\rho_0e^{\theta Q})=\cosh\theta\), and one has

$$
m(\theta):=\langle Q\rangle_{\rho_\theta}
=\tanh\theta,
\qquad
g^{\mathrm{BKM}}_{\theta\theta}
=\operatorname{Var}_{\rho_\theta}(Q)
=\operatorname{sech}^2\theta,
$$

so the general Casimir identity becomes

$$
\boxed{
1=m(\theta)^2+g^{\mathrm{BKM}}_{\theta\theta}.}
$$

The \(\tanh/\operatorname{sech}^2\) profile is **[EXACT — AFTER THE BALANCED EXPONENTIAL-FAMILY REDUCTION]**. The unit on the left remains the representation normalization \(\langle Q^2\rangle=1\); balance fixes the particular coordinate profile, not the underlying Casimir theorem.

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

## How capacity could meet charge

The plausible bridge is a common variational structure:

$$
\text{relative-entropy Hessian}
\longleftrightarrow
\text{canonical energy}
\longleftrightarrow
\text{second variation of a charge or action}.
$$

More precisely, the same-tangent conjecture seeks

$$
g^{\mathrm{BKM}}(v,v)
=Z_g\,
\mathcal E^{(1)}_{\mathrm{can}}
(\mathfrak S v,\mathfrak S v).
$$

This can place a quadratic state capacity and gravitational Noether structure in one theory without identifying capacity with the linear charge. The coefficient \(Z_g\) must remain symbolic until the state side is independently calculated.

## Why this is not yet least action

A relative-entropy Hessian is a local second-order response at coincidence. It does not imply that physical histories minimize relative entropy, BKM length, or capacity. A least-action claim would require a history functional such as

$$
\mathcal S_{\mathrm{CI}}
[\text{state},\text{geometry},\text{records}]
$$

with a declared domain, boundary terms, admissible variations, and stationary equations yielding the wall-state law, gravitational response, constraints, and factive or record dynamics. No such common functional is currently defined.

Einstein--Hilbert gravity can be written in the areal-modulus basis as

$$
\frac{S_{\mathrm{EH}}}{\hbar}
=\frac{\eta_{\mathrm E}}{4\pi}
\int R\,\mathrm dV_g.
$$

This is an exact reparameterization after Einstein gravity and its normalization have been assumed. It neither makes the wall BKM metric an action nor derives \(\eta_{\mathrm E}\). [[philosophy/principle-of-least-action/entry|The least-action module]] owns the general variational distinctions.

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

Thus translation in the binary exponential coordinate is not temperature rescaling of the modular Hamiltonian of that same reduced state. A larger wall sector may still possess an escort tangent whose sufficient binary reduction preserves the physical norm, but that requires a reduction theorem. It cannot be supplied by terminology or multiplicity alone. [[causal-scale-theory/no-gos/modular-rescaling-is-not-the-binary-tangent|The binary-tangent no-go]] is constitutional for the programme.

## Facthood is a further layer

Selection of a section, state, or polarization can reduce the manifest symmetry from \(G\) to the stabilizer subgroup of the selected object while the equivariant law remains \(G\)-symmetric. This supplies a precise model of “symmetry breaking without destruction of the underlying symmetry.” It still does not actualize an outcome.

A completed causal-conservation theory must therefore coordinate, without conflation:

$$
\text{equivariant law},
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
