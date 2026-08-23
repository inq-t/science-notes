# Classical Action

Classical action is the most direct form of the stationary-action principle. A classical system is assigned a functional $S$ of its possible histories, and its physical histories are those for which the first variation vanishes under the permitted variations.

## Hamilton's principle

For generalized coordinates $q^i(t)$,

$$
S[q]=\int_{t_1}^{t_2}L(q,\dot q,t)\,\mathrm dt.
$$

Hamilton's principle holds the endpoint configurations and endpoint times fixed and requires

$$
\delta S=0.
$$

Varying $q^i$, integrating the $\delta\dot q^i$ term by parts, and setting the endpoint variations to zero gives

$$
\frac{\mathrm d}{\mathrm dt}
\frac{\partial L}{\partial\dot q^i}
-\frac{\partial L}{\partial q^i}=0.
$$

These Euler--Lagrange equations are the local equations of motion. For a particle in a potential,

$$
L=\frac12m\dot{\boldsymbol x}^{\,2}-V(\boldsymbol x),
$$

they give

$$
m\ddot{\boldsymbol x}=-\boldsymbol\nabla V.
$$

Hamilton's principle and Newtonian evolution are therefore alternative formulations of the same dynamics when the Lagrangian is regular and the boundary-value problem is well posed.

## Stationary is not necessarily least

The first variation tests only whether the action changes to first order. Classification requires the second variation:

$$
S[q+\varepsilon\eta]
=S[q]
+\varepsilon\,\delta S[q;\eta]
+\frac{\varepsilon^2}{2}\,\delta^2S[q;\eta]
+\cdots.
$$

At a stationary history the linear term vanishes. If $\delta^2S$ is positive for all permitted nonzero variations, the history is a local minimum; if it has both signs, the history is a saddle. Conjugate points, long time intervals, gauge directions, and indefinite kinetic terms commonly prevent a true minimum.

The free particle between fixed endpoints is a simple genuine minimum. By contrast, classical systems such as the harmonic oscillator can have stationary trajectories that cease to minimize the action once the time interval is long enough.

## Equivalent Lagrangians

The same bulk equations can come from more than one Lagrangian. In particular,

$$
L'(q,\dot q,t)
=L(q,\dot q,t)
+\frac{\mathrm d}{\mathrm dt}F(q,t)
$$

changes the action only by endpoint values of $F$. With fixed endpoints, it leaves the Euler--Lagrange equations unchanged. Multiplying the entire action by a nonzero constant also leaves the classical stationarity equation unchanged, although normalization becomes consequential when the action enters the quantum phase $e^{iS/\hbar}$ or when it is coupled to other sectors.

The action is thus not unique as a formula. Its equivalence class, boundary conditions, symplectic structure, and couplings carry the physical information.

## From particles to fields

For fields $\phi^a(x)$ on spacetime,

$$
S[\phi]=\int_\mathcal M
\mathcal L(\phi^a,\partial_\mu\phi^a,x)\,\mathrm d^dx.
$$

The field Euler--Lagrange equations are

$$
\frac{\partial\mathcal L}{\partial\phi^a}
-\partial_\mu
\left(
\frac{\partial\mathcal L}{\partial(\partial_\mu\phi^a)}
\right)=0.
$$

For a real scalar field with

$$
\mathcal L
=-\frac12\partial_\mu\phi\,\partial^\mu\phi
-V(\phi),
$$

the result is the nonlinear Klein--Gordon equation, up to the chosen metric-sign convention:

$$
\Box\phi-V'(\phi)=0.
$$

Boundary terms again determine which field data can consistently be fixed. In gauge theories some variations are physically redundant, and the resulting degeneracy is expressed through constraints and Noether identities.

The [[einstein-hilbert-action]] is the corresponding field-action construction when spacetime geometry itself becomes dynamical.

## Symmetry and Noether's theorem

If a continuous transformation changes the Lagrangian by at most a total derivative, the equations possess a conserved quantity. Common examples are:

| Action symmetry | Conserved quantity |
|---|---|
| Time translations | Energy |
| Spatial translations | Linear momentum |
| Spatial rotations | Angular momentum |
| Global internal phase | Charge |

Noether's theorem is one reason actions are more than an elegant repackaging of differential equations: they expose which conservation laws follow structurally from symmetry.

## Constraints and endpoint data

The phrase “vary the path” hides choices that matter.

- Holonomic constraints can be built into generalized coordinates or imposed with Lagrange multipliers.
- Nonholonomic constraints need extra care and do not always follow by naively restricting variations.
- Fixing endpoint positions leads to Hamilton's usual principle; fixing other boundary data generally requires adding or subtracting boundary terms.
- Singular Lagrangians, especially gauge theories, produce constraints rather than an invertible relation between velocities and canonical momenta.

The canonical momentum and Hamiltonian are

$$
p_i:=\frac{\partial L}{\partial\dot q^i},
\qquad
H:=p_i\dot q^i-L.
$$

When the Legendre transform is regular, the same dynamics can be written in first-order form,

$$
S[q,p]=\int_{t_1}^{t_2}
\left(p_i\dot q^i-H(q,p,t)\right)\mathrm dt.
$$

Variation with appropriate endpoint data gives Hamilton's equations.

## Nearby variational principles

Several historical principles are related but use different constraints:

- **Maupertuis' abbreviated action:** at fixed energy, the physical orbit in configuration space makes $\int p_i\,\mathrm dq^i$ stationary. Its parametrization in time is not the primary variable.
- **Jacobi's principle:** conservative mechanics at fixed energy becomes a geodesic problem for a configuration-space metric.
- **Fermat's principle:** optical rays make travel time, or equivalently optical path length under standard conditions, stationary.
- **D'Alembert's principle:** virtual work vanishes for permitted virtual displacements; it is closely related to Lagrangian mechanics but is not itself an integral-over-history statement.

These are not interchangeable without translating their fixed data and admissible variations.
