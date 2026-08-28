# Receipt Contract

This receipt suite separates reduced binary algebra from CST-B2 homogeneous-background arithmetic. It tests formula implementation for that member only; it does not validate the wall construction, select CST-B2 from [[causal-scale-theory/response-family-interface|the wider response family]], promote the $A_2$ audit to a cosmology, or establish the constitutive source, unit principles, or dimensional applicability. The separately scoped [[causal-scale-theory/receipts/fit-late-time-background|late-time likelihood receipt]] owns the frozen-member comparison, whose canonical primary row uses fully released 2025 DESI DR2 and Pantheon+ products. [[causal-scale-theory/receipts/fit-des-dovekie-background|The DES-Dovekie robustness receipt]] substitutes the released alternate supernova reduction without treating the overlapping compilation as independent evidence. [[causal-scale-theory/receipts/fit-generalized-background|The generalized profile receipt]] releases \((\nu,\mathfrak R_c)\) and audits branches, parameter compatibility, and information-criterion cost. [[causal-scale-theory/receipts/fit-calibrated-background|The Cepheid-calibrated receipt]] retains the absolute-distance anchors and tests the implied \(H_0\), sound horizon, and extrapolated age; it reuses the shape-only Hubble-flow and DESI rows, so only the added Cepheid calibration is new information. None lends empirical credit back to the microscopic premises.

Run locally with

```powershell
python causal-scale-theory/receipts/algebra.py
python causal-scale-theory/receipts/background.py
```

Any current Python 3 interpreter can run the scripts. Both use only the standard library, write [[algebra.json|algebra]] and [[background.json|background]] outputs beside themselves, and exit nonzero if any declared check fails.

The data receipts additionally require NumPy and the tracked products documented by [[data/desi-dr2-bao-gaussian-likelihood/inq|DESI DR2 BAO]], [[data/pantheon-plus-shoes-distance-likelihood/inq|Pantheon+SH0ES]], and [[data/des-dovekie-distance-likelihood/inq|DES-Dovekie]]. They write [[causal-scale-theory/receipts/late-time-background-fit.json|the frozen Pantheon+ ledger]], [[causal-scale-theory/receipts/des-dovekie-background-fit.json|the DES-Dovekie ledger]], [[causal-scale-theory/receipts/generalized-background-fit-2025.json|the released-data generalized ledger]], [[causal-scale-theory/receipts/generalized-background-fit.json|the provisional-update generalized ledger]], and [[causal-scale-theory/receipts/calibrated-background-fit.json|the calibrated absolute-scale ledger]]. The specialized receipts import the base expansion and distance implementation rather than duplicating it.

Each data ledger preserves the type of its input. The 2025 DESI rows use released likelihood products and own the canonical generalized profile. The 2026 Ly\(\alpha\) rows reconstruct the published bivariate Gaussian block and assume zero cross-covariance with the retained lower-redshift distances; they are **[PROVISIONAL PUBLISHED-GAUSSIAN UPDATES]** until a full collaboration likelihood is released. Reproducible optimization does not promote that supplemental input into a released 2026 likelihood result.

The `kind` field records how a check was performed. Exact rational substitutions, numerical quadrature, direct differentiation, root solving, and historical regression values remain distinguishable in the machine-readable output.

The algebra receipt covers the exact binary and CST-B2 reductions:

- binary Casimir balance and its derivative identity;
- the density conic, logarithmic curvature, Riccati equation, and equation-of-state invariant;
- Witten factorization, zero-mode normalization, the explicit scattering-state Schrödinger residual, and unit transmission modulus;
- the dimensional crossing and equal-partition laws, the conditional unit selection of $d=3$, and the $3+1$ Hawking--Friedmann coefficients;
- normalized Gibbs invariance and explicit first/second-moment invariance of variance under an additive central shift;
- Fisher length and reflected relative entropy.

The background receipt covers the CST-B2 background:

- the weak-unit-matching, unit-rate present-flatness root;
- $z_c,w_0,w_a,q_0,j_0$, acceleration entry, and future exit;
- crossing density, response-to-matter ratio, exact response-to-matter-plus-radiation equality, radiation fraction, crossing deceleration, and horizon index;
- representative one-root, three-root, high-root-only, and no-root regimes for the inherited benchmark;
- the two historical double-root anchors;
- positive-root counterexamples for $\mathfrak R_c=1.9$ at $\nu=2$ and $\nu=2.2$.

Sign-change scans do not discover exact double roots, so folds are solved separately from the closure and stationarity equations. The scan interval and resolution are recorded in the JSON output. These checks establish algebra and arithmetic consequences of declared premises, not the truth of those premises.

The legacy receipt schema uses **crossing_ratio** for the integrated reference parameter \(\mathfrak R_c\). The code label does not prove that the reference cut is a physical crossing. “Ruble” is reserved for the named equation system rather than used as a code-level constant or scalar type.
