# The Puzzle as Posed

The Yang–Mills existence and mass-gap problem, as the Clay Mathematics Institute states it in the description by Jaffe and Witten, is four separable clauses, and the contemporary presentation runs them together. This note states each in the literature's own terms and cites nothing from the vault, so that a reader who rejects every reclassification downstream can still use the statement.

## Clause 1 — existence

Prove that for any compact simple gauge group \(G\), a nontrivial quantum Yang–Mills theory exists on \(\mathbb R^4\) and satisfies the Wightman axioms: a Hilbert space carrying a unitary positive-energy representation of the Poincaré group, a unique invariant vacuum, and local operator-valued distributions with the correct covariance and locality. Equivalently, by Osterwalder–Schrader reconstruction, a Euclidean measure on connections modulo gauge satisfying reflection positivity, Euclidean invariance, regularity, and clustering, whose reconstruction yields the Wightman theory.

No nontrivial interacting quantum field theory has been constructed in four dimensions. The constructive programme (Glimm–Jaffe, Balaban, and successors) controlled two- and three-dimensional scalar models and made deep partial progress on the ultraviolet problem for four-dimensional gauge theory without completing it. Existence, not the gap, is where the field's effort has gone.

## Clause 2 — the gap

Prove that the Hamiltonian of that theory has spectrum \(\{0\}\cup[\Delta,\infty)\) with \(\Delta>0\): the vacuum is isolated and the lightest excitation is massive. Under OS reconstruction this is equivalent to exponential clustering of the Euclidean correlations with rate \(\Delta\).

## Clause 3 — nontriviality

A free massive field has a mass gap and satisfies the Wightman axioms. The problem excludes it by requiring the theory be nontrivial: the S-matrix is not the identity, or equivalently the theory is not a generalized free field. The gap alone is easy; the gap together with interaction is the problem.

## Clause 4 — what is already known and measured

On a lattice, Wilson's action is reflection positive at every coupling (Osterwalder–Seiler, 1978) and has a mass gap at strong coupling by convergent cluster expansion. The lattice theory is therefore a gapped, reflection-positive statistical system at every finite spacing. The difficulty is entirely the continuum limit: that the gap survive \(a\to0\) at fixed physical scale, with the coupling running to zero as asymptotic freedom requires.

Numerically, pure \(\mathrm{SU}(3)\) lattice gauge theory has a \(0^{++}\) glueball at \(m_{0^{++}}\approx1.65\)–\(1.73\,\mathrm{GeV}\) and a \(2^{++}\) at \(\approx2.39\,\mathrm{GeV}\) when the scale is set by \(r_0\); the phenomenological string tension is \(\sqrt\sigma\approx440\,\mathrm{MeV}\); the pure-gauge \(\Lambda_{\overline{\mathrm{MS}}}\) is \(\approx260\,\mathrm{MeV}\). The theory's actual predictions are the dimensionless ratios computed within one scale-setting: \(m_{0^{++}}/\sqrt\sigma\approx3.5\)–\(3.6\) in the continuum (Lucini–Teper), \(m_{2^{++}}/m_{0^{++}}\approx1.4\), and \(m_{0^{++}}/\Lambda_{\overline{\mathrm{MS}}}\approx7\) via \(r_0m_{0^{++}}\approx4.2\) and \(r_0\Lambda\approx0.6\). Dividing a glueball mass in MeV by a string tension in MeV from a different convention gives \(\approx3.9\) and is the kind of cross-convention arithmetic these notes exist to forbid. The overall scale is one input, fixed by matching to any single dimensionful observable.

## What the statement does not say

It does not say that a continuum theory cannot have a discrete spectrum; a free massive field does. It does not say that the vacuum is empty; in the Wightman framework the vacuum is a cyclic, separating state on the local algebras (Reeh–Schlieder), the least empty object in the theory. It does not ask why the gap has the value it has; the value is one input. And it does not treat the gap as surprising: asymptotic freedom, the trace anomaly, and dimensional transmutation have been the accepted physical account since the 1970s. What it asks for is a proof.

## Distinct logical forms

The clauses have different forms: existence is a construction; the gap is a spectral inequality; nontriviality is a negation; and the measured facts are numbers with error bars. No argument that addresses one of them addresses the others, and the habit of demanding one insight that settles all four is the first symptom of the confusion that [[register-audit]] diagnoses.
