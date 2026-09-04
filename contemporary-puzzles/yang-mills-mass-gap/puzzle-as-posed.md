# The Puzzle as Posed

The Yang–Mills existence and mass-gap problem, as the Clay Mathematics Institute states it in [[library/quantum-yang-mills-theory/inq|the description by Jaffe and Witten]], can be audited as four separable clauses that contemporary shorthand often runs together. This note states each in the literature's own terms so that a reader who rejects every reclassification downstream can still use the target.

## Clause 1 — existence

Prove that for any compact simple gauge group \(G\), a nontrivial quantum Yang--Mills theory exists on \(\mathbb R^4\) and satisfies axioms at least as strong as the standard Wightman framework: a Hilbert space carrying a unitary positive-energy representation of the Poincaré group, a unique invariant vacuum, and local observables with the required covariance and locality. One admissible constructive route is Euclidean: construct suitable gauge-invariant Schwinger functions or a controlled Euclidean measure satisfying the Osterwalder--Schrader hypotheses, including reflection positivity, so that reconstruction yields the positive-energy theory. This is a route to the target, not a claim that every Hamiltonian construction must begin with a Euclidean measure on connections modulo gauge.

No nonperturbative interacting four-dimensional model satisfying the full standard axioms has been constructed. The constructive programme (Glimm--Jaffe, Balaban, and successors) controlled two- and three-dimensional scalar models and made deep partial progress on the ultraviolet problem for four-dimensional gauge theory without completing it. Existence, not only the gap estimate, is where the field's effort has gone.

## Clause 2 — the gap

Prove that the Hamiltonian of that theory has no spectrum immediately above the vacuum:

$$
\boxed{E_H((0,\Delta))=0\quad\text{for some }\Delta>0.}
$$

Equivalently, \(\sigma(H)\cap(0,\Delta)=\varnothing\). The spectrum may start continuously at its lower threshold; an isolated one-particle pole is an additional statement. Under OS reconstruction a gap yields exponential decay estimates for appropriate connected Euclidean correlations, generally with any rate strictly below the relevant spectral threshold. Conversely, a sufficiently uniform clustering estimate for a family of operators that sees the lowest sector can establish a gap; one channel's decay rate need not equal the global gap.

## Clause 3 — nontriviality

A free massive field has a mass gap and satisfies the Wightman axioms. The problem additionally requires a nontrivial Yang--Mills theory. Non-Gaussian truncated correlations, nontrivial operator products, and a nonidentity scattering matrix when scattering theory is available are distinct possible diagnostics of interaction; they are not blanket logical equivalents. The gap alone is easy to realize; constructing it together with a nontrivial four-dimensional gauge theory is the problem.

## Clause 4 — what is already known and computed

Wilson's lattice action is reflection positive at every coupling (Osterwalder--Seiler, 1978). At sufficiently strong coupling, convergent cluster expansions prove exponential decay and a mass gap uniformly in volume. Reflection positivity alone does not imply a gap, and finite lattice spacing alone is not a gap theorem. The continuum trajectory runs toward weak bare coupling as \(a\to0\); proving a nontrivial limit and a positive physical gap uniformly through that limit and the infinite-volume limit is unresolved.

Numerically, pure \(\mathrm{SU}(3)\) lattice gauge theory gives a \(0^{++}\) glueball near \(1.65\)–\(1.73\,\mathrm{GeV}\) and a \(2^{++}\) near \(2.39\,\mathrm{GeV}\) after a scale-setting convention is chosen; \(\sqrt\sigma\approx440\,\mathrm{MeV}\) is a commonly used phenomenological convention, and pure-gauge \(\Lambda_{\overline{\mathrm{MS}}}\) is scheme-dependent. The clean predictions are dimensionless ratios computed within one consistent scale-setting: \(m_{0^{++}}/\sqrt\sigma\approx3.5\)–\(3.6\) in the continuum (Lucini--Teper), \(m_{2^{++}}/m_{0^{++}}\approx1.4\), and a scheme-labelled ratio such as \(m_{0^{++}}/\Lambda_{\overline{\mathrm{MS}}}\). Dividing separately quoted MeV values from different conventions manufactures a ratio rather than computing one. An external dimensionful datum is needed to express the pure-number spectrum in MeV.

## What the statement does not say

It does not say that a continuum theory cannot have isolated spectral structure; a free massive field does. It does not say that the vacuum is empty; in the Wightman framework the vacuum is cyclic for local algebras, and under the usual locality hypotheses it is separating as well (Reeh--Schlieder). It does not ask for a value in MeV without a scale-setting convention. Nor does it make dimensional transmutation a proof of the gap: asymptotic freedom and the trace anomaly explain the origin of a scale, while the positive spectral bound remains a dynamical theorem. What the statement asks for is a construction and proof.

## Distinct logical forms

The clauses have different forms: existence is a construction; the gap is a spectral inequality; nontriviality excludes a degenerate solution; and numerical evidence consists of regulator-controlled estimates with uncertainties and scale conventions. No argument that addresses one clause automatically addresses the others. [[register-audit]] isolates the narrower register mistake that can make this theorem look paradoxical.

Nor does undecidability of the general spectral-gap decision problem add a fifth obstruction to this particular theorem. [[spectral-gap-undecidability-firewall]] records the quantifiers: no universal algorithm for one constructed family does not imply that Yang--Mills is undecidable, independent, or immune to a model-specific proof.
