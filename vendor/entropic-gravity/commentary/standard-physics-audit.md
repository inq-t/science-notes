# Standard-Physics Audit

The strongest part of the vendored literature is Jacobson’s conditional universality argument; the weakest overstatement is to treat any of these works as a completed microscopic theory of gravity. Verlinde 2011 reconstructs known laws from thermodynamic assignments, Verlinde 2016 obtains a restricted phenomenological equality only after saturating an inequality, and the best-known covariant completion introduces new fields whose stability remains problematic.

This is commentary on the vendored theory, not part of its own presentation.

## Overall classification

| Programme | Best-supported classification |
|---|---|
| Jacobson 1995 | conditional derivation of Einstein’s equation of state from universal local-horizon thermodynamics |
| Eling–Guedens–Jacobson 2006 | conditional non-equilibrium construction of metric \(f(R)\) dynamics |
| Jacobson 2015–2016 | first-order entanglement-equilibrium characterization of the semiclassical Einstein equation, cleanest for conformal matter |
| Verlinde 2011 | thermodynamic reconstruction and reinterpretation of Newton/Poisson/Komar/Einstein relations |
| Verlinde 2016 | conjectural de Sitter microphysics plus a restricted elastic constitutive model |
| Covariant vector models | independent Verlinde-inspired effective theories, not unique completions |

None of these classifications is dismissive. It identifies the exact level at which each construction is rigorous.

## Coefficients are often matched rather than predicted

In [[vendor/entropic-gravity/jacobson-local-horizon-thermodynamics]], the area density \(\eta\) is assumed and then identified through

$$
\eta=\frac{1}{4\hbar G}
$$

in natural units. This explains why a universal area density entails a universal gravitational coupling, but it does not calculate \(G\) without gravitational input.

In [[vendor/entropic-gravity/verlinde-entropic-force]], \(G\) enters through

$$
N=\frac{Ac^3}{G\hbar}.
$$

The inverse-square law follows after this bit density, equipartition, and the Bekenstein–Unruh normalization are imposed. The construction reverses familiar gravitational thermodynamic relations; it does not obtain their coefficient from an independently specified microstate count.

In [[vendor/entropic-gravity/verlinde-emergent-gravity]], the elastic modulus is

$$
\mu=\frac{a_0^2}{16\pi G}.
$$

Thus neither \(G\) nor the de Sitter acceleration scale is predicted by the elastic medium. They normalize it.

## Conservative entropic forces are underdetermined

[[library/conservative-entropic-forces/inq|Visser]] studies a conservative one-body force written as

$$
-\nabla\Phi=T\nabla S.
$$

The general aligned solution can be parametrized by a monotone function \(f\):

$$
S=k_Bf\!\left(-\frac{\Phi}{E_*}\right),
\qquad
T=\frac{T_*}{f'\!\left(-\Phi/E_*\right)},
\qquad
E_*=k_BT_*.
$$

Equipotential, isoentropy, and isothermal surfaces must align. Verlinde’s more specific assignment \(T\propto|\nabla\Phi|\) can therefore be globally integrable only where iso-acceleration surfaces also align appropriately with equipotentials. Generic many-body configurations require still more structure.

The lesson is not that emergent forces are impossible. It is that a known conservative force admits many formal \(T,S\) representations; writing one does not select a microphysics. This objection does not directly apply to Jacobson, whose argument constrains a local tensor equation through horizon heat balance and does not posit a particle force.

## The screen–particle quantum objection is not decisive

[[library/gravity-is-not-an-entropic-force/inq|Kobakhidze]] argues that a literal screen-state implementation of the entropy postulate conflicts with coherent neutron bound states. [[library/entropic-gravity-entropy-postulate-screens-quantum-mechanics/inq|Chaichian, Oksanen, and Tureanu]] reply that the argument identifies the screen density matrix with the particle state too strongly and that the entropy postulate need not imply the claimed decoherence.

The dispute reveals a missing map:

$$
\text{screen macrostate}
\longleftrightarrow
\text{particle quantum state}.
$$

Because Verlinde’s paper does not specify that map, neither treatment is a definitive microscopic test of the proposal as written. The absence of the map is itself a real incompleteness.

## The 2016 equality is the principal internal vulnerability

The general elastic result is

$$
\int_{\mathcal B}\varepsilon^2\,dV
\leq V_M(\mathcal B).
$$

The first promotion to approximate equality requires saturation of the principal-strain bound—equivalently, equal transverse principal strains—and a negligible exterior strain-energy tail. A second step uses a gradient displacement and an aligned equipotential boundary to translate that elastic equality into gravitational variables. Isolation, equilibrium, four dimensions, and approximate spherical symmetry delimit the later radial apparent-mass formula used in observations.

This matters because the equality is not merely a convenient reformulation. It converts a one-sided bound into a definite source profile. Whenever an empirical paper applies the profile to disks, cluster outskirts, stacked environments, or non-equilibrium systems, it adds an extrapolation beyond the theorem-shaped elastic result.

## Covariance is not a cosmetic omission

A complete gravity theory must say how all matter and light couple, how constraints propagate, what initial data are admissible, and whether the Hamiltonian is stable. [[vendor/entropic-gravity/covariant-completions]] shows that one plausible completion:

- adds a timelike vector field and direct matter coupling;
- makes massive bodies follow an effective metric;
- requires independent choices for light coupling; and
- faces de Sitter-instability and unbounded-Hamiltonian objections.

Those failures do not refute every possible emergent theory. They demonstrate that the missing covariant structure can change the physical content and cannot be inferred uniquely from the static force law.

## Empirical reading

[[vendor/entropic-gravity/empirical-status]] supports a balanced conclusion.

- The baryonic Tully–Fisher and radial-acceleration regularities are real targets which any galaxy theory should explain.
- Verlinde’s point-mass asymptote lands on the correct kind of low-acceleration scaling.
- A 2026 dwarf-spheroidal comparison reports favorable relative performance for a later Yoon quadrature prescription against the tested MOND prescription; it is not a direct likelihood test of Verlinde’s original linear acceleration rule. Finite-galaxy residuals, the direct Solar-System exterior test, galaxy-type dependence, and cluster profiles expose tensions or new required structure.
- Existing lensing tests translate apparent mass through GR and standard cosmological distances because the vendored proposal lacks a native lensing sector.

The programme is therefore not flagrantly incompatible with known physics in its carefully stated restricted regimes. It is also not a complete alternative to GR plus dark matter. The gap between those statements is exactly where further theory is required.
