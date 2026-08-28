# The Optional Holographic Spectral Adapter

The holographic spectral adapter is an optional factorization of selected CWST response arrows through a continued three-dimensional stress-tensor theory. It is available only after a wall member constructs the source, state, carrier pairing, and response that enter the adapter. It neither defines the general W2 map nor constructs the W3 Lorentzian scalar or tensor field.

## Eligibility datum

A candidate member declares an admitted sector set \(\mathcal S_{\mathfrak H}\subseteq\{0,2\}\), which may be scalar-only, tensor-only, or both. For every \(s\in\mathcal S_{\mathfrak H}\), it must provide an explicit pairing from that sector's wall source data to a renormalized three-dimensional Euclidean QFT datum,

$$
(\mathcal A_{\mathrm{wall}}^s,\omega_{\mathrm{wall}}^s,J_{\mathrm{wall}}^s,
\Pi_{\mathrm{wall}}^s)
\xrightarrow{\ \mathfrak H_s\ }
(\mathrm{QFT}_3,\omega_3,T_s^{(3)},c^{(s)}),
$$

on the sector's physical effective image. This is **[CONJECTURE — OPEN CONSTRUCTION]**. Each arrow must state which source directions are paired, how their measures and normalizations change, and whether it factors that sector's W2 source transform or begins from an already constructed spatial precision. Possessing \(\mathfrak H_0\) does not imply \(\mathfrak H_2\), or conversely.

[[vendor/holographic-cosmology/inq|The vendored holographic framework]] owns the domain-wall/cosmology representation. [[vendor/holographic-cosmology/scalar-and-tensor-spectra|Its spectrum dictionary]] is the sole owner of the response decomposition and numerical conversion factors. CWST's additional burden is to prove that its wall datum lies in that domain; the shared vocabulary of scale or stress does not establish eligibility.

## Operators that must remain distinct

At least three source operators occur in candidate constructions:

- a four-dimensional renormalized Weyl-source trace \(T^{(4)}\);
- a horizon or cut generator \(K_\Sigma\), related to modular flow only in declared settings; and
- a three-dimensional Euclidean stress trace \(T^{(3)}\).

They are not one bare \(T\). A member must construct

$$
T^{(4)}
\dashrightarrow K_\Sigma
\dashrightarrow T^{(3)}
$$

or provide a different typed route. The adapter fails if the paired operators do not act on the declared sources or if their Ward identities and normalizations are incompatible.

## Continuation, state, and branch data

The QFT, state, regulator, subtraction prescription, momentum variables, theory parameters, and response coefficients must be analytically continued together. The member must state the branch orientation and reality/positivity condition of the continued kernel. Continuing only a final coefficient while leaving its state or regulator implicit does not define an adapter.

A modular or KMS kernel can make the wall-to-Euclidean relation frequency dependent. [[causal-wall-spectral-theory/open-questions/bkm-source-kernel-comparison|The same-source comparison]] owns the experiment that distinguishes a scalar normalization from such a transform.

## Contact and analytic qualifications

Local polynomial counterterms have zero discontinuity across a registered spectral cut in the vendor's analytic setting. This removes one class of scheme ambiguity. The converse requires dispersion, growth, and analyticity hypotheses: zero discontinuity alone does not prove that a contribution is a removable local contact. Boundaries, defects, anomalies, parity-odd structures, and semilocal terms require separate treatment.

## Calculated and inferred responses

A member predicts only when it computes \(c_{\mathrm{calc}}^{(0)}(k)\) or \(c_{\mathrm{calc}}^{(2)}(k)\) from the wall construction without using the target spectrum as input. Inverting measured correlations to define \(c_{\mathrm{inf}}^{(s)}\) is a useful normalization audit, not a microscopic return. [[causal-wall-spectral-theory/empirical-targets|The empirical-target ledger]] owns the inferred targets and conventions.

## Boundary and failure

The adapter is upgraded when \(\mathfrak H\), the paired operators, simultaneous continuation, state, branch, regulator, contacts, and physical effective image are all constructed. It fails for a member if the wall datum is outside the vendor's domain, the source pairing is absent, continuation is inconsistent, or the continued response cannot define the claimed positive spatial probability kernel.

Failure of [[causal-wall-spectral-theory/conjectures/wall-scalar-to-cosmological-curvature|scalar W3]], [[causal-wall-spectral-theory/conjectures/wall-tensor-to-cosmological-graviton|tensor W3]], or an observational fit is downstream and is not failure of this adapter. Conversely, a successful adapter cannot discharge either W3 field-identification problem.
