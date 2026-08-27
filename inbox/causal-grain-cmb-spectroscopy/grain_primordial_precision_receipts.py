"""Receipts for the conditional grain rewrite of primordial precision.

The script parses bundled Planck best-fit targets and checks algebraic
equivalence to the leading Einstein single-clock formulas. It does not derive
the live-cut common-count law, a wall state, or primordial dynamics.
"""

from __future__ import annotations

import math
import re
from pathlib import Path


MODULE = Path(__file__).resolve().parent
REPO = MODULE.parents[1]
PLANCK_MINIMUM = (
    REPO
    / "causal-wall-spectral-theory"
    / "sources"
    / "data"
    / "planck-2018"
    / "COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum_R3.01.txt"
)
BK18_ENTRY = (
    REPO
    / "library"
    / "bicep-keck-2018-primordial-gravitational-waves"
    / "entry.md"
)

KAPPA = 8.0 / 3.0
ARCHIVED_R_BOUND_95 = 0.036


def close(a: float, b: float, *, rel: float = 1e-12, abs_: float = 0.0) -> None:
    if not math.isclose(a, b, rel_tol=rel, abs_tol=abs_):
        raise AssertionError(f"{a:.16g} != {b:.16g}")


def read_parameters(path: Path) -> dict[str, float]:
    wanted = {"A", "ns"}
    values: dict[str, float] = {}
    row = re.compile(r"^\s*\d+\s+([+-]?\d*\.?\d+(?:[Ee][+-]?\d+)?)\s+(\w+)\b")
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        match = row.match(line)
        if match and match.group(2) in wanted:
            values[match.group(2)] = float(match.group(1))
    missing = wanted.difference(values)
    if missing:
        raise ValueError(f"missing Planck parameters: {sorted(missing)}")
    return values


def algebra_receipt() -> None:
    epsilon = 0.0017
    hubble_planck = 2.9e-6
    grain_ratio_cubed = KAPPA * hubble_planck**2
    iota = math.pi / hubble_planck**2

    scalar_from_horizon = 1.0 / (epsilon * iota)
    scalar_from_grain = 3.0 * grain_ratio_cubed / (8.0 * math.pi * epsilon)
    tensor_from_horizon = 16.0 / iota
    tensor_from_grain = 6.0 * grain_ratio_cubed / math.pi

    close(scalar_from_horizon, scalar_from_grain)
    close(tensor_from_horizon, tensor_from_grain)
    close(tensor_from_grain / scalar_from_grain, 16.0 * epsilon)

    sigma = -math.log(grain_ratio_cubed) / 3.0
    log_precision = -math.log(scalar_from_grain)
    log_ledger = 3.0 * sigma + math.log(8.0 * math.pi / 3.0) + math.log(epsilon)
    close(log_precision, log_ledger)

    print("CONDITIONAL EINSTEIN / LIVE-CUT IDENTITIES")
    print(f"  trial epsilon_H             = {epsilon:.9f}")
    print(f"  trial H*t_P                 = {hubble_planck:.9e}")
    print(f"  grain ratio g               = {grain_ratio_cubed ** (1.0 / 3.0):.12e}")
    print(f"  scalar power                = {scalar_from_grain:.12e}")
    print(f"  tensor power                = {tensor_from_grain:.12e}")
    print(f"  tensor/scalar               = {tensor_from_grain / scalar_from_grain:.12e}")
    print("  horizon and grain presentations agree")


def planck_target_receipt() -> None:
    params = read_parameters(PLANCK_MINIMUM)
    scalar_amplitude = params["A"] * 1e-9
    scalar_tilt = params["ns"]
    grain_cubed_per_epsilon = 8.0 * math.pi * scalar_amplitude / 3.0
    inverse_precision = 1.0 / scalar_amplitude

    epsilon_max = ARCHIVED_R_BOUND_95 / 16.0
    grain_ratio_max = (grain_cubed_per_epsilon * epsilon_max) ** (1.0 / 3.0)
    sigma_min = -math.log(grain_ratio_max)
    hubble_planck_max = math.sqrt(math.pi * epsilon_max * scalar_amplitude)

    constant_epsilon = (1.0 - scalar_tilt) / (3.0 - scalar_tilt)
    constant_epsilon_r = 16.0 * constant_epsilon
    epsilon_2_at_bound = (
        (1.0 - scalar_tilt) * (1.0 - epsilon_max) - 2.0 * epsilon_max
    )

    close(
        3.0 * grain_cubed_per_epsilon / (8.0 * math.pi),
        scalar_amplitude,
    )
    close(
        -2.0 * constant_epsilon / (1.0 - constant_epsilon),
        scalar_tilt - 1.0,
    )

    print("BUNDLED PLANCK CALIBRATION TARGET")
    print(f"  A_s                          = {scalar_amplitude:.12e}")
    print(f"  n_s                          = {scalar_tilt:.9f}")
    print(f"  I_zeta=1/A_s                 = {inverse_precision:.12e}")
    print(f"  g_*^3/epsilon_*              = {grain_cubed_per_epsilon:.12e}")
    print(f"  BK18 r_0.05 (95% CL)         < {ARCHIVED_R_BOUND_95:.6f}")
    print(f"  Einstein epsilon upper bound < {epsilon_max:.12e}")
    print(f"  Einstein grain upper bound   < {grain_ratio_max:.12e}")
    print(f"  Einstein Sigma lower bound   > {sigma_min:.12f} nats")
    print(f"  Einstein H*t_P upper bound   < {hubble_planck_max:.12e}")
    print(f"  constant-epsilon solution    = {constant_epsilon:.12e}")
    print(f"  constant-epsilon r           = {constant_epsilon_r:.12e}")
    print(f"  epsilon_2 at r-bound edge    = {epsilon_2_at_bound:.12e}")
    print("  scope: calibration under the imported Einstein single-clock member")


def main() -> None:
    if not PLANCK_MINIMUM.is_file():
        raise FileNotFoundError(PLANCK_MINIMUM)
    if not BK18_ENTRY.is_file():
        raise FileNotFoundError(BK18_ENTRY)
    if "r_{0.05}<0.036" not in BK18_ENTRY.read_text(encoding="utf-8"):
        raise AssertionError("archived BK18 entry does not contain the declared 95% bound")
    algebra_receipt()
    print()
    planck_target_receipt()
    print()
    print("ALL GRAIN--PRIMORDIAL-PRECISION RECEIPTS PASS")
    print("Scope: conditional identities and local targets, not a causal-wall derivation.")


if __name__ == "__main__":
    main()
