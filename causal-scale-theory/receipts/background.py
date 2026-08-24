"""Arithmetic receipts for the causal-scale homogeneous background.

This script intentionally uses only the Python standard library. It validates
formula implementation and benchmark arithmetic; it does not validate any
physical premise of Causal Scale Theory.
"""

from __future__ import annotations

import json
import math
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable


OMEGA_M0 = 0.310598
OMEGA_R0 = 9.15e-5
DARK0 = 1.0 - OMEGA_M0 - OMEGA_R0


def sech2(value: float) -> float:
    """Stable sech(value)^2 for the ranges used by this receipt."""

    magnitude = abs(value)
    if magnitude < 350.0:
        cosine = math.cosh(value)
        return 1.0 / (cosine * cosine)
    return 4.0 * math.exp(-2.0 * magnitude)


def matter_function(x: float) -> float:
    return OMEGA_M0 * math.exp(3.0 * x) + OMEGA_R0 * math.exp(4.0 * x)


def closure_residual(x: float, nu: float, ruble: float) -> float:
    if not 0.0 < ruble < 2.0:
        raise ValueError("ruble must lie in (0, 2)")
    ratio = ruble / (2.0 - ruble)
    return ratio * matter_function(x) * sech2(nu * x) - DARK0


def closure_dx(x: float, nu: float, ruble: float) -> float:
    ratio = ruble / (2.0 - ruble)
    exp3 = OMEGA_M0 * math.exp(3.0 * x)
    exp4 = OMEGA_R0 * math.exp(4.0 * x)
    profile = sech2(nu * x)
    return ratio * profile * (
        3.0 * exp3 + 4.0 * exp4
        - 2.0 * nu * math.tanh(nu * x) * (exp3 + exp4)
    )


def bisect(
    function: Callable[[float], float],
    left: float,
    right: float,
    *,
    tolerance: float = 1e-13,
    iterations: int = 300,
) -> float:
    f_left = function(left)
    f_right = function(right)
    if f_left == 0.0:
        return left
    if f_right == 0.0:
        return right
    if f_left * f_right > 0.0:
        raise ValueError("bisection interval does not bracket a root")
    for _ in range(iterations):
        middle = 0.5 * (left + right)
        f_middle = function(middle)
        if abs(f_middle) < tolerance or abs(right - left) < tolerance:
            return middle
        if f_left * f_middle <= 0.0:
            right = middle
            f_right = f_middle
        else:
            left = middle
            f_left = f_middle
    return 0.5 * (left + right)


def sign_change_roots(
    function: Callable[[float], float],
    left: float,
    right: float,
    *,
    step: float,
) -> list[float]:
    """Find simple roots; exact even-multiplicity roots are checked separately."""

    roots: list[float] = []
    x_left = left
    f_left = function(x_left)
    count = int(math.ceil((right - left) / step))
    for index in range(1, count + 1):
        x_right = min(right, left + index * step)
        f_right = function(x_right)
        if f_left * f_right < 0.0:
            root = bisect(function, x_left, x_right)
            if not roots or abs(root - roots[-1]) > 10.0 * step:
                roots.append(root)
        x_left = x_right
        f_left = f_right
    return roots


def e2_unit_derivatives(n_value: float, x_crossing: float) -> tuple[float, float, float]:
    centered = n_value + x_crossing
    profile = sech2(centered)
    tangent = math.tanh(centered)
    profile_prime = -2.0 * tangent * profile
    profile_second = 4.0 * tangent * tangent * profile - 2.0 * profile * profile
    normalizer = sech2(x_crossing)

    matter = OMEGA_M0 * math.exp(-3.0 * n_value)
    radiation = OMEGA_R0 * math.exp(-4.0 * n_value)
    response = DARK0 * profile / normalizer

    value = matter + radiation + response
    first = -3.0 * matter - 4.0 * radiation + DARK0 * profile_prime / normalizer
    second = 9.0 * matter + 16.0 * radiation + DARK0 * profile_second / normalizer
    return value, first, second


def deceleration(n_value: float, x_crossing: float) -> float:
    value, first, _ = e2_unit_derivatives(n_value, x_crossing)
    return -1.0 - 0.5 * first / value


def jerk(n_value: float, x_crossing: float) -> float:
    value, first, second = e2_unit_derivatives(n_value, x_crossing)
    q_value = -1.0 - 0.5 * first / value
    dq_dn = -0.5 * (second / value - (first / value) ** 2)
    return q_value * (2.0 * q_value + 1.0) - dq_dn


def close(actual: float, expected: float, tolerance: float) -> bool:
    return abs(actual - expected) <= tolerance


def check(
    identifier: str,
    kind: str,
    passed: bool,
    value: object,
    expected: object,
    tolerance: object,
) -> dict[str, object]:
    return {
        "id": identifier,
        "kind": kind,
        "pass": bool(passed),
        "value": value,
        "expected": expected,
        "tolerance": tolerance,
    }


def main() -> int:
    checks: list[dict[str, object]] = []

    x_crossing = bisect(lambda x: closure_residual(x, 1.0, 1.0), 0.0, 1.0)
    z_crossing = math.exp(x_crossing) - 1.0
    w0 = -1.0 + (2.0 / 3.0) * math.tanh(x_crossing)
    wa = -(2.0 / 3.0) * sech2(x_crossing)
    q0 = deceleration(0.0, x_crossing)
    j0 = jerk(0.0, x_crossing)

    entry_n = bisect(lambda n: deceleration(n, x_crossing), -2.0, 0.0)
    exit_n = bisect(lambda n: deceleration(n, x_crossing), 0.0, 5.0)
    entry_z = math.exp(-entry_n) - 1.0
    exit_a = math.exp(exit_n)

    unit_expectations = {
        "unit_x_crossing": (x_crossing, 0.2940066, 2e-7),
        "unit_z_crossing": (z_crossing, 0.3417927, 2e-7),
        "unit_w0": (w0, -0.8094545, 2e-7),
        "unit_wa": (wa, -0.6122053, 2e-7),
        "unit_q0": (q0, -0.3369025, 2e-7),
        "unit_j0": (j0, -0.1112465, 3e-7),
        "unit_acceleration_entry_z": (entry_z, 0.7856935, 3e-7),
        "unit_acceleration_exit_a": (exit_a, 11.7865, 3e-4),
    }
    for identifier, (value, expected, tolerance) in unit_expectations.items():
        checks.append(
            check(identifier, "independent", close(value, expected, tolerance), value, expected, tolerance)
        )

    scan_left = 1e-8
    scan_right = 60.0
    scan_step = 0.002
    atlas_cases = {
        "atlas_one_root": (1.4, 1),
        "atlas_three_roots": (1.7, 3),
        "atlas_high_root_only": (1.9, 1),
        "atlas_no_root_at_two": (2.0, 0),
    }
    atlas_roots: dict[str, list[float]] = {}
    for identifier, (nu, expected_count) in atlas_cases.items():
        roots = sign_change_roots(
            lambda x, width=nu: closure_residual(x, width, 1.0),
            scan_left,
            scan_right,
            step=scan_step,
        )
        atlas_roots[identifier] = roots
        checks.append(
            check(identifier, "independent", len(roots) == expected_count, len(roots), expected_count, 0)
        )

    fold_anchors = {
        "radiation_fold": (1.558402308, 6.10687),
        "late_fold": (1.814657, 0.64905),
    }
    fold_results: dict[str, dict[str, float]] = {}
    for identifier, (nu, x_value) in fold_anchors.items():
        residual = closure_residual(x_value, nu, 1.0)
        derivative = closure_dx(x_value, nu, 1.0)
        fold_results[identifier] = {"closure_residual": residual, "dx_residual": derivative}
        checks.append(
            check(
                identifier,
                "regression",
                abs(residual) < 2e-5 and abs(derivative) < 2e-5,
                fold_results[identifier],
                {"closure_residual": 0.0, "dx_residual": 0.0},
                2e-5,
            )
        )

    amplitude_counterexamples: dict[str, list[float]] = {}
    for nu in (2.0, 2.2):
        identifier = f"amplitude_root_nu_{nu:.1f}"
        roots = sign_change_roots(
            lambda x, width=nu: closure_residual(x, width, 1.9),
            scan_left,
            20.0,
            step=0.001,
        )
        amplitude_counterexamples[identifier] = roots
        checks.append(check(identifier, "independent", len(roots) > 0, roots, "at least one root", None))

    output = {
        "receipt": "causal-scale-theory homogeneous background",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "runtime": {
            "python": sys.version,
            "platform": platform.platform(),
        },
        "parameters": {
            "omega_m0": OMEGA_M0,
            "omega_r0": OMEGA_R0,
            "dark0": DARK0,
            "scan": {"left": scan_left, "right": scan_right, "step": scan_step},
        },
        "unit_branch": {
            "x_crossing": x_crossing,
            "z_crossing": z_crossing,
            "w0": w0,
            "wa": wa,
            "q0": q0,
            "j0": j0,
            "acceleration_entry_n": entry_n,
            "acceleration_entry_z": entry_z,
            "acceleration_exit_n": exit_n,
            "acceleration_exit_a": exit_a,
        },
        "atlas_roots": atlas_roots,
        "fold_anchors": fold_results,
        "amplitude_counterexamples": amplitude_counterexamples,
        "checks": checks,
        "all_pass": all(item["pass"] for item in checks),
        "scope": "arithmetic and formula implementation only",
    }

    output_path = Path(__file__).with_name("background.json")
    output_path.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if output["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
