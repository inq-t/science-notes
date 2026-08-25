# Receipt Contract

The receipt suite separates reduced algebra from homogeneous-background arithmetic. It tests formula implementation only; no receipt validates the wall construction, constitutive source, unit principles, dimensional applicability, or observational fit.

Run locally with

```powershell
python causal-scale-theory/receipts/algebra.py
python causal-scale-theory/receipts/background.py
```

Any current Python 3 interpreter can run the scripts. Both use only the standard library, write [[algebra.json|algebra]] and [[background.json|background]] outputs beside themselves, and exit nonzero if any declared check fails.

The `kind` field records how a check was performed. Exact rational substitutions, numerical quadrature, direct differentiation, root solving, and historical regression values remain distinguishable in the machine-readable output.

The algebra receipt covers:

- binary Casimir balance and its derivative identity;
- the density conic, logarithmic curvature, Riccati equation, and equation-of-state invariant;
- Witten factorization, zero-mode normalization, the explicit scattering-state Schrödinger residual, and unit transmission modulus;
- the dimensional crossing and equal-partition laws, the conditional unit selection of $d=3$, and the $3+1$ Hawking--Friedmann coefficients;
- normalized Gibbs invariance and explicit first/second-moment invariance of variance under an additive central shift;
- Fisher length and reflected relative entropy.

The background receipt covers:

- the weak-unit-matching, unit-rate present-flatness root;
- $z_c,w_0,w_a,q_0,j_0$, acceleration entry, and future exit;
- crossing density, response-to-matter ratio, exact response-to-matter-plus-radiation equality, radiation fraction, crossing deceleration, and horizon index;
- representative one-root, three-root, high-root-only, and no-root regimes for the inherited benchmark;
- the two historical double-root anchors;
- positive-root counterexamples for $\mathfrak R_c=1.9$ at $\nu=2$ and $\nu=2.2$.

Sign-change scans do not discover exact double roots, so folds are solved separately from the closure and stationarity equations. The scan interval and resolution are recorded in the JSON output. These checks establish algebra and arithmetic consequences of declared premises, not the truth of those premises.

The receipt schema uses **crossing_ratio** for the integrated crossing parameter \(\mathfrak R_c\). “Ruble” is reserved for the named equation system rather than used as a code-level constant or scalar type.
