#!/usr/bin/env python3
"""Reviewed standard-library receipt for the generalized FLRW background.

This checks mathematics internal to the declared background closure. It does
not test the wall-state construction, the unit principles, the constitutive
source law, or any observational likelihood.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import asdict, dataclass
from typing import Callable


OM = 0.310598
OR = 9.15e-5
D = 1.0 - OM - OR


def log_cosh(value: float) -> float:
    """Stable log(cosh(value))."""
    absolute = abs(value)
    return absolute + math.log1p(math.exp(-2.0 * absolute)) - math.log(2.0)


def sech2(value: float) -> float:
    return math.exp(-2.0 * log_cosh(value))


def matter_sum(x: float, omega_m: float = OM, omega_r: float = OR) -> float:
    return omega_m * math.exp(3.0 * x) + omega_r * math.exp(4.0 * x)


def closure_residual(
    x: float,
    nu: float,
    ruble: float = 1.0,
    omega_m: float = OM,
    omega_r: float = OR,
    target_d: float | None = None,
) -> float:
    """Present-flatness residual for the generalized response."""
    if not 0.0 < ruble < 2.0:
        raise ValueError("ruble must lie in (0, 2) for the 3+1 positive-density branch")
    if target_d is None:
        target_d = 1.0 - omega_m - omega_r
    amplitude = ruble / (2.0 - ruble)
    return amplitude * matter_sum(x, omega_m, omega_r) * sech2(nu * x) - target_d


def bisect(function: Callable[[float], float], left: float, right: float) -> float:
    f_left = function(left)
    f_right = function(right)
    if f_left == 0.0:
        return left
    if f_right == 0.0:
        return right
    if f_left * f_right > 0.0:
        raise ValueError("interval does not bracket a root")
    for _ in range(160):
        middle = 0.5 * (left + right)
        f_middle = function(middle)
        if abs(f_middle) < 1e-13 or abs(right - left) < 1e-12:
            return middle
        if f_left * f_middle <= 0.0:
            right = middle
            f_right = f_middle
        else:
            left = middle
            f_left = f_middle
    return 0.5 * (left + right)


def enumerate_roots(
    function: Callable[[float], float],
    lower: float,
    upper: float,
    step: float = 0.002,
) -> list[float]:
    """Enumerate simple roots by sign changes; fold roots are solved separately."""
    roots: list[float] = []
    left = lower
    f_left = function(left)
    while left < upper:
        right = min(left + step, upper)
        f_right = function(right)
        if f_left == 0.0:
            candidate = left
        elif f_left * f_right < 0.0:
            candidate = bisect(function, left, right)
        else:
            candidate = None
        if candidate is not None and (not roots or abs(candidate - roots[-1]) > 1e-7):
            roots.append(candidate)
        left = right
        f_left = f_right
    return roots


def fold_equations(
    x: float,
    nu: float,
    omega_m: float,
    omega_r_in_shape: float,
    target_d: float,
) -> tuple[float, float, float, float, float, float]:
    matter = omega_m * math.exp(3.0 * x)
    radiation = omega_r_in_shape * math.exp(4.0 * x)
    total = matter + radiation
    radiation_fraction = radiation / total
    mean_power = 3.0 + radiation_fraction
    z = nu * x
    tangent = math.tanh(z)
    metric = sech2(z)

    value = math.log(total) - 2.0 * log_cosh(z) - math.log(target_d)
    stationary = mean_power - 2.0 * nu * tangent

    value_x = stationary
    value_nu = -2.0 * x * tangent
    stationary_x = radiation_fraction * (1.0 - radiation_fraction) - 2.0 * nu * nu * metric
    stationary_nu = -2.0 * tangent - 2.0 * nu * x * metric
    return value, stationary, value_x, value_nu, stationary_x, stationary_nu


def solve_fold(
    seed_nu: float,
    seed_x: float,
    omega_m: float = OM,
    omega_r_in_shape: float = OR,
    target_d: float = D,
) -> tuple[float, float]:
    """Newton solve of closure plus stationarity; returns (nu, x)."""
    nu = seed_nu
    x = seed_x
    for _ in range(40):
        value, stationary, value_x, value_nu, stationary_x, stationary_nu = fold_equations(
            x, nu, omega_m, omega_r_in_shape, target_d
        )
        determinant = value_x * stationary_nu - value_nu * stationary_x
        if abs(determinant) < 1e-16:
            raise ArithmeticError("singular fold Jacobian")
        delta_x = (-value * stationary_nu + value_nu * stationary) / determinant
        delta_nu = (-value_x * stationary + stationary_x * value) / determinant
        x += delta_x
        nu += delta_nu
        if max(abs(delta_x), abs(delta_nu), abs(value), abs(stationary)) < 2e-14:
            return nu, x
    raise ArithmeticError("fold solver did not converge")


@dataclass
class Check:
    name: str
    got: float
    want: float
    tolerance: float
    passed: bool


checks: list[Check] = []


def check(name: str, got: float, want: float, tolerance: float) -> None:
    checks.append(Check(name, got, want, tolerance, abs(got - want) <= tolerance))


def run_receipt() -> dict[str, object]:
    unit_roots = enumerate_roots(lambda x: closure_residual(x, 1.0), 0.0, 2.0)
    if len(unit_roots) != 1:
        raise AssertionError(f"expected one unit-width root, found {unit_roots}")
    unit_x = unit_roots[0]
    check("unit late root x_c", unit_x, 0.2940066, 2e-7)
    check("unit crossing redshift", math.exp(unit_x) - 1.0, 0.3417927, 2e-7)

    radiation_fold = solve_fold(1.56, 6.1)
    late_fold = solve_fold(1.815, 0.65)
    check("radiation fold nu", radiation_fold[0], 1.558402308, 2e-9)
    check("radiation fold x", radiation_fold[1], 6.106871592, 2e-9)
    check("late fold nu", late_fold[0], 1.814657203, 2e-9)
    check("late fold x", late_fold[1], 0.649049974, 2e-9)

    strict_dust_fold = solve_fold(1.814, 0.65, omega_r_in_shape=0.0, target_d=1.0 - OM)
    hybrid_fold = solve_fold(1.814, 0.65, omega_r_in_shape=0.0, target_d=D)
    check("strict dust fold nu", strict_dust_fold[0], 1.81400853, 2e-8)
    check("hybrid receipt fold nu", hybrid_fold[0], 1.81413212, 2e-8)

    atlas_cases = {
        "nu_1_0": (1.0, [0.2940066]),
        "nu_1_8": (1.8, [0.5466053, 0.8024096, 18.8519793]),
        "nu_1_9": (1.9, [37.7040688]),
        "nu_2_0": (2.0, []),
    }
    atlas_output: dict[str, list[float]] = {}
    for name, (nu, expected) in atlas_cases.items():
        roots = enumerate_roots(lambda x, width=nu: closure_residual(x, width), 0.0, 80.0)
        atlas_output[name] = roots
        if len(roots) != len(expected):
            checks.append(Check(f"{name} root count", float(len(roots)), float(len(expected)), 0.0, False))
            continue
        check(f"{name} root count", float(len(roots)), float(len(expected)), 0.0)
        for index, (got, want) in enumerate(zip(roots, expected), start=1):
            check(f"{name} root {index}", got, want, 2e-7)

    threshold_ruble = 2.0 * D
    check(
        "past/future threshold residual at x=0",
        closure_residual(0.0, 1.0, ruble=threshold_ruble),
        0.0,
        2e-14,
    )

    amplitude_output: dict[str, float] = {}
    for ruble in (0.8, 1.2, 1.5):
        roots = enumerate_roots(
            lambda x, amplitude=ruble: closure_residual(x, 1.0, ruble=amplitude),
            -5.0,
            5.0,
        )
        check(f"ruble_{ruble} root count", float(len(roots)), 1.0, 0.0)
        if len(roots) == 1:
            root = roots[0]
            amplitude_output[str(ruble)] = root
            check(
                f"ruble_{ruble} closure residual",
                closure_residual(root, 1.0, ruble=ruble),
                0.0,
                2e-12,
            )
            expected_sign = 1.0 if ruble < threshold_ruble else -1.0
            actual_sign = 1.0 if root > 0.0 else -1.0
            check(f"ruble_{ruble} crossing sign", actual_sign, expected_sign, 0.0)

    passed = all(item.passed for item in checks)
    return {
        "status": "PASS" if passed else "FAIL",
        "scope": "generalized homogeneous background arithmetic only",
        "inputs": {"omega_m0": OM, "omega_r0": OR, "D": D},
        "folds": {
            "radiation": {"nu": radiation_fold[0], "x": radiation_fold[1]},
            "late": {"nu": late_fold[0], "x": late_fold[1]},
            "strict_dust": {"nu": strict_dust_fold[0], "x": strict_dust_fold[1]},
            "hybrid_receipt": {"nu": hybrid_fold[0], "x": hybrid_fold[1]},
        },
        "root_atlas": atlas_output,
        "generalized_amplitude_roots": amplitude_output,
        "checks": [asdict(item) for item in checks],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    arguments = parser.parse_args()
    result = run_receipt()
    if arguments.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        for item in result["checks"]:
            label = "PASS" if item["passed"] else "FAIL"
            print(
                f"{label:4s}  {item['name']}: got={item['got']:.10g} "
                f"want={item['want']:.10g} tol={item['tolerance']:.2g}"
            )
        print(result["status"])
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
