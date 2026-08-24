# Background Receipt Contract

The background receipt independently recomputes the unit crossing and cosmography, samples the generalized branch topology, verifies the two historical fold anchors as regression checks, and demonstrates amplitude-dependent roots at and above $\nu=2$. It tests formulas and arithmetic only; no receipt validates the wall construction, constitutive source, unit principles, or observational fit.

Run locally with

```powershell
python causal-scale-theory/receipts/background.py
```

The script uses only the Python standard library and writes [[background.json|the machine-readable receipt]] beside itself. It exits nonzero if any declared check fails.

Every check carries one of two kinds:

- `independent`: the value is found from the equations by root solving or direct differentiation rather than inserted as the expected output;
- `regression`: the script evaluates a historical quoted anchor and checks that its residual is small.

The receipt covers:

- the unit-amplitude, unit-width present-flatness root;
- $z_c,w_0,w_a,q_0,j_0$, acceleration entry, and future exit;
- representative one-root, three-root, high-root-only, and no-root regimes for the inherited benchmark;
- the two historical double-root anchors;
- positive-root counterexamples for $\mathfrak R_c=1.9$ at $\nu=2$ and $\nu=2.2$.

Sign-change scans do not discover exact double roots, so folds are checked separately through the closure residual and its $x$ derivative. The scan interval and resolution are recorded in the JSON output.
