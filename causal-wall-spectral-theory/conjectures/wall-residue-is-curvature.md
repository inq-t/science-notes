# The Wall Residue Is Curvature

CWST conjectures that a physical mean-zero residue of observational scale descent can be represented as the gauge-invariant curvature perturbation whose correlations are observed. The residue need not be an inhomogeneity of the sub-observable algebra. The equality is not a definition: it requires a spacetime realization, gauge reduction, constraint solution, canonical normalization, and matching theorem.

## Candidate residue

Near a homogeneous scale section, write

$$
-\delta\ln\sigma(x)
=\delta N+\zeta_{\mathrm{wall}}(x).
$$

Removing the constant mode gives a kinematic representative in \(C^\infty(\Sigma)/\mathbb R\). The physical object is instead an equivalence class in the inhomogeneous part of [[program-core/physical-quotient|the physical horizontal quotient]], after gauge, constraints, boundary identifications, central normalization, and genuine information-metric null directions have been handled.

## Conjectured realization

There should exist a map

$$
R:
H^{\mathrm{phys}}_{\Sigma,\mathrm{inh}}
\longrightarrow
\mathcal P^{\mathrm{scalar}}_{\mathrm{cos}}
$$

into the reduced Lorentzian scalar phase space such that

$$
R(\zeta_{\mathrm{wall}})
=\zeta_{\mathrm{ud}}
$$

or an explicitly related conserved curvature variable. This is **[IDENTIFICATION — OPEN CONSTRUCTION]**. The symbol on the right must be the variable defined by a perturbed physical metric and slicing convention, not merely a dimensionless scalar with a similar transformation under spatial dilations.

The map must specify:

- how the scale section enters the perturbed physical metric;
- the action of spacetime gauge transformations;
- lapse, shift, matter, and gravitational constraints;
- the surviving scalar canonical pair and symplectic normalization;
- the relation between equal-time wall response and Lorentzian state data;
- treatment of the homogeneous and other null modes; and
- matching across any non-geometric or reheating transition.

[[compatible-with-existing-physics/primordial-observable-interface|The primordial observable interface]] owns the standard return type.

## Precision under the map

If the linearized realization is invertible on its image and

$$
\zeta_{\mathrm{cos}}=R\zeta_{\mathrm{wall}},
$$

then the quadratic precision transforms as

$$
\mathcal K_{\zeta_{\mathrm{cos}}}
=R^{-*}\mathcal K_{\mathrm{wall}}R^{-1}.
$$

Thus even a successful scalar identification need not preserve the numerical kernel unchanged. A nontrivial field normalization, projection, or carrier map belongs in \(R\).

## Upgrade and failure conditions

The conjecture is upgraded by a covariant reduced action or equivalent constrained Hamiltonian construction that derives \(R\), its normalization, and its long-wavelength conserved mode.

It fails if the wall residue is pure gauge, constrained away, nonpropagating when a physical mode is required, maps to an entropy rather than curvature mode, has unstable or acausal Lorentzian evolution, or cannot be matched into the observed growing mode. Failure leaves open the possibility that the wall response represents a different observable.
