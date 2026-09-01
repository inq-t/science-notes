# Acceleration Receipt

`acceleration.py` recomputes the unit-branch chronology from the generalized closure and, where it overlaps the reviewed background receipt in `causal-scale-theory/receipts/`, acts as a regression check on it rather than an independent implementation. It verifies the shape invariant and the CPL locus along the orbit, confirms the threshold at which the closure root leaves the canonically admitted domain, reproduces the benchmark fold atlas, and then performs the indicative comparison with published DESI DR2 `w0waCDM` fits that the module's receipts note tabulates.

It also carries the coincidence negative control: it computes the LambdaCDM matter-Lambda equality epoch alongside the causal-scale crossing at identical abundances, to establish that the logarithmic compression of that epoch is shared rather than distinctive.

Its added coverage is the cosmography — $q$ and $j$ by finite differences on $E^2(N)$, compared against the analytic tangent formulas — plus the branch, negative-control, and comparison blocks.

Run with any Python 3 interpreter, standard library only:

```text
python acceleration.py
python acceleration.py --json
```

Checks run in both output modes, so the exit status and the JSON `failures` list are meaningful either way; nonzero exit if any check fails. The published DESI values are hardcoded in `DESI_DR2` with their source cited in the module's receipts note; editing them changes the comparison and nothing else.

Scope. This checks arithmetic internal to the declared background closure and compares against published fitted parameters. It does not validate the wall-state construction, either unit principle, the constitutive source law, the horizontal-temperature identification, or any perturbation observable, and it is not a likelihood.

# Lambda-as-Inverse-Casimir Audit Receipt

`lambda_casimir_audit.py` accompanies `../lambda-as-inverse-casimir-audit.md`. It verifies the Vieta identities of the Schwarzschild–de Sitter cubic at five masses below Nariai (\(\sigma_1=0\), \(\sigma_2=-L^2\), \(\sum r_i^2=2L^2\), two positive roots), checks the recomputed numbers against the parallel note's stated values (\(\Lambda=1.0891\times10^{-52}\,\mathrm{m^{-2}}\), \(\lambda_\Lambda=4.872\,\mathrm{fm}\), \(E_\Lambda=40.51\,\mathrm{MeV}\), residual \(-1.1\times10^{-14}\)), runs the fake-\(\Lambda\) negative control showing the residual is floating-point noise, and checks that the crossing-to-horizon grain ratio is \((H_c/H_\Lambda)^{1/3}\), not \(^{2/3}\). Standard library only; `--json` supported; nonzero exit on failure. Output stored in `lambda-casimir-output.txt`.

Scope. This is a check of identities and a negative control. It establishes nothing about the value of \(\Lambda\), the grain, or any Casimir.
