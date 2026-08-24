# Causal-Wall Spectral Receipts

This receipt suite checks the normalization algebra that remains valid in version 3. It is deliberately narrower than the historical v2.1 suite: a passing receipt verifies formulas inside their declared member, not the causal-wall state, the information-geometric weld, a microscopic spectral function, or agreement with observation.

Run the dependency-free receipt from the repository root:

```powershell
python causal-wall-spectral-theory/receipts/verify_v3_normalizations.py
```

The script uses only the Python standard library, writes [[verify_v3_normalizations.json|its machine-readable result]] beside itself, and exits nonzero exactly when a declared check fails or the receipt cannot be completed. The output omits a wall-clock timestamp so an unchanged verification does not dirty the repository merely because it was rerun.

The checks are separated by mathematical scope:

- the scalar and tensor normalization identities in [[vendor/holographic-cosmology/scalar-and-tensor-spectra|the holographic spectrum dictionary]], after the conditional representation has been selected;
- the leading [[vendor/holographic-cosmology/einstein-single-clock-member|Einstein single-clock member]] relations, not a derivation of that member from a wall;
- the factor of two in the symmetrized relative-entropy Hessian for a regular finite exponential family;
- the three-dimensional stress-projector trace contraction;
- the round-sphere eigenvalue formula for the conditional $P_3$ representative;
- the logarithmic-derivative identities of the constant-exponent member.

The historical receipts S9, S10, and S12 are excluded on purpose. Version 3 rejects the use of differences between Planck and ACT best-fit tilts as a running estimator, rejects a universal non-Gaussianity floor or $|f_{\mathrm{NL}}|\gtrsim1$ kill inferred from $c^{(0)}$, and rejects the unproved reading $N\sim\sqrt{c^{(0)}}$. The direct extended-model running constraint remains an observational input, not an algebra receipt.

The finite exponential-family check does not establish the open BKM-to-Euclidean-to-spatial map in [[causal-wall-spectral-theory/conjectures/state-response-is-spatial-precision|the state-to-spatial-precision conjecture]]. Likewise, reproducing a measured scalar amplitude after inserting it is calibration arithmetic rather than a prediction.
