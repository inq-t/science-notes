# The Wall-Scalar-to-Curvature Map

CWST conjectures that a physical mean-zero residue of observational scale descent can be represented first as the gauge-invariant equal-time curvature configuration whose correlations are observed, and then lifted into a Lorentzian physical field. The residue need not be an inhomogeneity of the sub-observable algebra. The equality is not a definition: it requires a configuration realization, gauge reduction, and canonical normalization, followed separately by a phase-space, state, evolution, and matching theorem.

W3 has an equal-time gate and a Lorentzian gate. The first maps the wall field to a reduced spatial configuration carrier; the second embeds that configuration in an imported or independently recovered \(3+1\) Lorentzian phase space. Neither gate derives ordinary dimension, Lorentzian signature, causal cones, or spacetime itself. [[algebra/real-forms-and-factive-spacetime|The real-form theorem]] supplies a candidate three-dimensional carrier under separate hypotheses and states the further history-functor obligation.

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
R_{\mathrm s}^{\mathrm{eq}}:
H^{\mathrm{phys}}_{\Sigma,\mathrm{inh}}
\longrightarrow
\mathcal Q^{\mathrm{scalar}}_{\mathrm{cos}}
$$

into a reduced equal-time scalar configuration or polarization carrier such that

$$
R_{\mathrm s}^{\mathrm{eq}}(\zeta_{\mathrm{wall}})
=\zeta_{\mathrm{ud}}
$$

or an explicitly related equal-time curvature variable. This is **[IDENTIFICATION — OPEN CONSTRUCTION]**. The symbol on the right must be the variable defined by a perturbed physical metric and slicing convention, not merely a dimensionless scalar with a similar transformation under spatial dilations. A further lift from \(\mathcal Q^{\mathrm{scalar}}_{\mathrm{cos}}\) to a Lorentzian phase space \(\mathcal P^{\mathrm{scalar}}_{\mathrm{cos}}\) must supply the conjugate variable, symplectic form, state, constraints, and clock evolution.

The equal-time map must specify:

- how the scale section enters the perturbed physical metric;
- the induced spatial gauge transformations and constraint reduction;
- the normalization of the surviving scalar configuration; and
- treatment of the homogeneous and other null modes.

The later Lorentzian lift must separately specify the surviving canonical pair and symplectic normalization, the relation between equal-time wall response and Lorentzian state data, lapse and shift constraints, and matching across any non-geometric or reheating transition.

[[compatible-with-existing-physics/primordial-observable-interface|The primordial observable interface]] owns the standard return type.

## Precision under the map

Let \(q_{\mathrm{wall}}\) be the closed positive form associated with \(\mathcal K_{\mathrm{wall}}\). If \(R_{\mathrm s}^{\mathrm{eq}}\) is a bounded Hilbert-space isomorphism with bounded inverse, define

$$
D(q_{\mathrm{cos}})
=R_{\mathrm s}^{\mathrm{eq}}D(q_{\mathrm{wall}}),
\qquad
q_{\mathrm{cos}}[R_{\mathrm s}^{\mathrm{eq}}\xi,R_{\mathrm s}^{\mathrm{eq}}\eta]
=q_{\mathrm{wall}}[\xi,\eta].
$$

Then the associated equal-time precision transforms as

$$
\mathcal K^{\mathrm{eq}}_{\zeta_{\mathrm{cos}}}
=\bigl(R_{\mathrm s}^{\mathrm{eq}}\bigr)^{-*}
\mathcal K_{\mathrm{wall}}
\bigl(R_{\mathrm s}^{\mathrm{eq}}\bigr)^{-1}.
$$

Thus even a successful scalar identification need not preserve the numerical kernel unchanged. A nontrivial field normalization or carrier map belongs in \(R_{\mathrm s}^{\mathrm{eq}}\). [[measured-response-carriers/inq|Measured response carriers]] owns this closed-form transport theorem and its domain hypotheses.

If \(R_{\mathrm s}^{\mathrm{eq}}\) has a kernel, first quotient by the declared null or gauge sector and prove that the induced map is an isomorphism onto a closed physical image. If the map remains genuinely projective, precision must be transported by an appropriate projected-covariance, constrained, or shorted-form construction; the displayed inverse formula is then not available on the unreduced carrier.

## Upgrade and failure conditions

The equal-time gate is upgraded by a covariant derivation of \(R_{\mathrm s}^{\mathrm{eq}}\), its form domain, and its normalization. Full W3 is upgraded only by a reduced action or equivalent constrained Hamiltonian construction that also derives the Lorentzian lift, state, clock evolution, and long-wavelength conserved mode. [[lorentzian-spectral-envelope/inq|The Lorentzian spectral envelope]] records why the static precision alone cannot supply that clock.

It fails if the wall residue is pure gauge, constrained away, nonpropagating when a physical mode is required, maps to an entropy rather than curvature mode, has unstable or acausal Lorentzian evolution, or cannot be matched into the observed growing mode. Failure leaves open the possibility that the wall response represents a different observable.
