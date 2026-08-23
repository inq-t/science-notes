# Lineages and Scope

“Entropic gravity” names several logically different programmes rather than one theory. Jacobson derives gravitational field equations conditionally from local horizon or entanglement equilibrium; Verlinde reconstructs familiar force laws from holographic thermodynamic assignments and later proposes a distinct de Sitter elastic response. Their common vocabulary does not make their primitives, arguments, or empirical burdens interchangeable.

## Four meanings of entropy in gravity

The label hides four different mathematical uses of entropy.

1. In an **entropic force**, a mechanical force is represented by

   $$
   F_i=T\nabla_iS.
   $$

   The entropy gradient acts on a body or collective coordinate. This is the mechanism proposed in [[verlinde-entropic-force]].

2. In **local horizon thermodynamics**, matter boost energy is heat and horizon-area change is entropy change. Requiring

   $$
   \delta Q=T\,\delta S
   $$

   for every local causal horizon constrains the spacetime field equation. This is [[jacobson-local-horizon-thermodynamics]], not a force on a test particle.

3. In **entanglement equilibrium**, the first variation of total entropy—an ultraviolet area term plus infrared matter entanglement—in a small ball vanishes at fixed volume. After the area coefficient is identified with \(1/(4\hbar G)\), this has the Bekenstein generalized-entropy form. The field equation is encoded in a stationarity condition, not in entropy production or motion toward larger entropy. This is [[jacobson-entanglement-equilibrium]].

4. In **de Sitter entropy displacement**, matter is proposed to remove part of a volume-law entropy and the residual medium is represented by linear elasticity. Its strain is then translated into an apparent gravitational source. This is [[verlinde-emergent-gravity]].

These are not equivalent forms of one master equation. In particular,

$$
F=T\nabla S,
\qquad
\delta Q=T\,\delta S,
\qquad
\delta S_{\mathrm{tot}}|_V=0,
\qquad
\int_{\mathcal B}\varepsilon^2\,dV\leq V_M(\mathcal B)
$$

have different domains, variables, and logical roles.

## The two principal lineages

### Jacobson

The Jacobson sequence is cumulative but not one unchanged proof.

- In 1995, an equilibrium Clausius relation on all local Rindler horizons yields the Einstein equation as an equation of state; the same paper already suggests vacuum entanglement as a possible origin of horizon entropy.
- In 2006, curvature-dependent entropy density forces a non-equilibrium balance law with internal entropy production; the naïve equilibrium extension fails.
- In 2012, the vacuum-entanglement interpretation is developed and gravitational self-regulation of its ultraviolet divergence is proposed, still heuristically.
- In 2015–2016, a different small-causal-diamond argument relates first-order fixed-volume stationarity of the total ultraviolet-plus-infrared entropy to the semiclassical Einstein equation.

Jacobson does not posit holographic screens, equipartition of screen bits, or a literal entropic force on matter.

### Verlinde

The two principal Verlinde papers also describe distinct constructions.

- The 2011 paper assigns entropy gradients, Unruh temperature, area-proportional screen degrees of freedom, and equipartition so as to reproduce inertia, Newtonian gravity, Poisson’s equation, the Komar integral, and the static Einstein equation.
- The 2016 paper proposes long-range de Sitter entanglement, entropy displacement by matter, glassy memory, and an elastic dark-energy medium. Its restricted spherical response mimics part of the phenomenology ordinarily assigned to dark matter.

The later vector-field models in [[covariant-completions]] are independent attempts to complete the second construction. They are not uniquely forced by Verlinde’s paper.

## Claim map

| Construction | Principal physical inputs | Controlled consequence | What it does not supply |
|---|---|---|---|
| Jacobson 1995 | local Lorentz horizon, Unruh temperature, universal area entropy density, Clausius relation, stress conservation | Einstein equation with an undetermined cosmological constant | microstates, area coefficient, matter theory, quantum gravity |
| Eling–Guedens–Jacobson 2006 | curvature-dependent entropy functional and entropy-balance law | metric \(f(R)\) equation with a required production term | microscopic viscosity or arbitrary higher-curvature theory |
| Jacobson 2015–2016 | finite UV area density, entanglement first law, small-ball stationarity, local CFT modular Hamiltonian | first-order semiclassical Einstein equation in the stated small-ball regime | generic nonconformal QFT, finite perturbations, independent microscopic or numerical value of \(G\), or value of \(\Lambda\) |
| Verlinde 2011 | screen entropy gradient, Unruh normalization, area bit density, equipartition | reconstruction of Newton/Poisson/Komar/Einstein forms in quasi-static settings | microscopic screen theory, generic dynamics, independent new prediction |
| Verlinde 2016 | de Sitter volume-law entropy, matter-induced entropy deficit, elastic dictionary, saturation and symmetry assumptions | apparent-mass relation for isolated, static, approximately spherical systems | covariant field equations, cosmological perturbations, general lensing or structure formation |

The word *derivation* is therefore always qualified in this module. An algebraic result can follow exactly from premises that remain conjectural as physics.

## Scope of this vendor module

This module vendors the Jacobson and Verlinde lineages and the immediate papers needed to understand their claim boundaries and tests. It does not attempt to cover every thermodynamic-gravity programme, such as Sakharov induced gravity, Padmanabhan’s horizon thermodynamics, black-hole microstate counting, tensor-network reconstruction, or every MOND theory. Those are adjacent theories with their own primitives and should be vendored separately.
