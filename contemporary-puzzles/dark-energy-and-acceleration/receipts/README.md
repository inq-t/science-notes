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
