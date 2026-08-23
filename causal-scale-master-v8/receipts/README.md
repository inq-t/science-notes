# Background Receipt

`background.py` is the reviewed, dependency-free receipt for the generalized homogeneous closure. It computes the two exact matter-plus-radiation folds, distinguishes strict dust from the supplied receipt's hybrid dust-form approximation, enumerates representative positive-root branches, checks past- and future-crossing generalized-amplitude cases, checks the unit benchmark, and exits nonzero if a comparison fails.

Run the human-readable receipt with a standard Python 3 interpreter:

```text
python background.py
```

Use `--json` for machine-readable output. The receipt checks internal background arithmetic only. It does not validate the binary wall reduction, either unit principle, the free-energy source law, the horizon-temperature identification, perturbations, or an observational likelihood.
