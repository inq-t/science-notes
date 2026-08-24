# What Actually Fluctuates

Linearising about Minkowski and decomposing into scalar, vector and tensor sectors answers the question the construction leaves open: which parts of the metric are stochastic degrees of freedom, and where the indefiniteness of the deWitt kernel lives. The answer is favourable. The dynamical modes are a transverse-traceless spin-2 pair and one spin-0 scalar, each diffusing around its own wave equation, and their sectors are positive semidefinite. The indefinite sector is the vector, which carries the momentum constraint and does not propagate.

Source: [[library/stochastic-modes-in-postquantum-gravity/entry|Oppenheim and Sajjad]].

## Counting degrees of freedom in a stochastic theory

The counting procedure differs from the quantum one, and the difference is instructive. In Einstein--Hilbert or quadratic gravity one identifies constrained variables, substitutes the constraints back, and counts the surviving second time derivatives. Here the object being decomposed is not a Lagrangian but an Onsager--Machlup action, so one instead reads off the stochastic differential equations whose squares constitute it. Then:

- an equation of motion obtained from the OM action means a degree of freedom **diffusing around** that equation;
- a constraint equation means a mode **diffusing around its constraint**, which is not an independent degree of freedom.

## The modes

$$
\Box\psi=\xi,
\qquad
\Box h^{TT}_{ij}=\xi^{\prime TT}_{ij},
$$

with $\xi$ and $\xi'$ mean-zero noise. So the dynamical content is one scalar plus two tensor polarisations, each a stochastic wave equation. The tensor noise carries the transverse-traceless projector $P^{ij,kl}$.

The remaining metric functions are not independently stochastic. The Newtonian potential $\Phi$ is fixed by the Hamiltonian constraint once $\psi$ is given, and the vector $V_i$ satisfies the momentum constraint rather than an equation of motion.

**Three dynamical modes rather than general relativity's two.** The extra scalar is expected: stress-energy conservation no longer suffices to remove the additional modes on shell. This is a genuine physical difference from deterministic general relativity, not a gauge artifact, and it is what the scalar-sector bounds below constrain.

## Where the indefiniteness went

The vector sector is the one that is not positive semidefinite. It also carries fewer time derivatives, marking it as a constraint rather than a propagating mode. The conclusion the paper draws is precise and hedged twice over. It calls the indefiniteness *relatively* benign, and it holds only under an added prescription: the vector action is indefinite when the path integral sums over both continuous and non-continuous geometries, and ceases to be so when the sum is restricted to continuous geometries. The published paper is more guarded still, reporting the vector sector positive semidefinite *on shell* while the off-shell tachyonic modes are not yet fully understood. Subject to those,

$$
\boxed{
\text{the positive-semidefinite sectors are exactly the dynamical ones; the indefinite sector is a constraint.}
}
$$

This is the strongest available answer to the wound identified in [[cq-construction]] — that the Lorentzian deWitt metric has negative eigenvalues. The indefiniteness is not benign because it was miscounted, but because it sits where nothing propagates, once continuity of the geometries is imposed.

The paper does not claim the matter is closed. $V_i$ is not determined once and for all: at second order, vector--scalar mixing in the presence of matter gives it stochastic contributions through the momentum constraint, and it must, if the constraint is sourced by fields in superposition and covariance is to hold. How constraints are imposed in the path integral at higher order, where that coupling becomes dynamically relevant, is left open.

## Two procedures that do not commute

The most useful structural observation in the paper is a warning about method. One may reduce the gravitational phase space by solving the constraints classically and then introduce stochasticity on what survives; or one may let the stochastic dynamics act on the full metric and let the constraints emerge from the path integral. **These do not commute**, and the paper's Newtonian-limit results differ significantly from earlier weak-field treatments for exactly this reason.

The authors note the parallel with the long-standing quantum-gravity dispute between Dirac quantisation and reduced-phase-space quantisation, and observe that the classical-stochastic setting is a more tractable arena in which to study the inequivalence. That is a transferable methodological point, and it belongs with the ordering discipline recorded in [[vendor/entropic-gravity/commentary/methodological-lessons|the methodological lessons]]: quotient-then-deform and deform-then-quotient are different theories, and a programme that quotients redundant structure before introducing its dynamics has made a choice it must defend.

## Experimental handles

The decomposition sharpens the bounds by separating sectors. Fluctuations of the Newtonian potential give a power spectral density comparable with the excess noise reported by LISA Pathfinder, bounding one combination of the theory's two dimensionless couplings; bounds on the stochastic gravitational-wave energy density in an FLRW background constrain another. The effective action for matter distributions makes decoherence bounds depend on fluctuations in both $\Phi$ and the curvature perturbation $\psi$. The verdict is that the theory remains viable, with care needed over nonlinearities, non-Markovianity and scale invariance. One near-exclusion belongs with it: if the computed spectrum is assumed to hold throughout, the bound requires an ultraviolet cutoff $\ell\gtrsim10^2\,$m, far above the millimetre scale to which gravity has been probed, and with scale-independent couplings **this would rule the theory out**. The escape is the running of the coupling. [[vendor/postquantum-gravity/empirical-status|empirical status]] collects the numbers.

The paper also checks internal consistency of the formalism: the Onsager--Machlup action, the Martin-Siggia-Rose (Janssen--De Dominicis) form, and the stochastic differential equations agree.
