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


def log_cosh(value: float) -> float:
    """Stable log(cosh(value))."""

    magnitude = abs(value)
    return magnitude + math.log1p(math.exp(-2.0 * magnitude)) - math.log(2.0)


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


def fold_equations(
    x: float,
    nu: float,
    *,
    omega_m: float = OMEGA_M0,
    omega_r_in_shape: float = OMEGA_R0,
    target_dark: float = DARK0,
    ruble: float = 1.0,
) -> tuple[float, float, float, float, float, float]:
    """Closure and stationarity equations with their Newton derivatives."""

    if not 0.0 < ruble < 2.0:
        raise ValueError("ruble must lie in (0, 2)")
    matter = omega_m * math.exp(3.0 * x)
    radiation = omega_r_in_shape * math.exp(4.0 * x)
    total = matter + radiation
    radiation_fraction = radiation / total
    mean_power = 3.0 + radiation_fraction
    z_value = nu * x
    tangent = math.tanh(z_value)
    metric = sech2(z_value)
    amplitude = ruble / (2.0 - ruble)

    value = math.log(amplitude) + math.log(total) - 2.0 * log_cosh(z_value) - math.log(target_dark)
    stationary = mean_power - 2.0 * nu * tangent

    value_x = stationary
    value_nu = -2.0 * x * tangent
    stationary_x = radiation_fraction * (1.0 - radiation_fraction) - 2.0 * nu * nu * metric
    stationary_nu = -2.0 * tangent - 2.0 * nu * x * metric
    return value, stationary, value_x, value_nu, stationary_x, stationary_nu


def solve_fold(
    seed_nu: float,
    seed_x: float,
    *,
    omega_m: float = OMEGA_M0,
    omega_r_in_shape: float = OMEGA_R0,
    target_dark: float = DARK0,
    ruble: float = 1.0,
) -> tuple[float, float]:
    """Solve closure plus stationarity; return (nu, x)."""

    nu = seed_nu
    x_value = seed_x
    for _ in range(40):
        value, stationary, value_x, value_nu, stationary_x, stationary_nu = fold_equations(
            x_value,
            nu,
            omega_m=omega_m,
            omega_r_in_shape=omega_r_in_shape,
            target_dark=target_dark,
            ruble=ruble,
        )
        determinant = value_x * stationary_nu - value_nu * stationary_x
        if abs(determinant) < 1e-16:
            raise ArithmeticError("singular fold Jacobian")
        delta_x = (-value * stationary_nu + value_nu * stationary) / determinant
        delta_nu = (-value_x * stationary + stationary_x * value) / determinant
        x_value += delta_x
        nu += delta_nu
        if max(abs(delta_x), abs(delta_nu), abs(value), abs(stationary)) < 2e-14:
            return nu, x_value
    raise ArithmeticError("fold solver did not converge")


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

    crossing_n = -x_crossing
    matter_crossing = OMEGA_M0 * math.exp(3.0 * x_crossing)
    radiation_crossing = OMEGA_R0 * math.exp(4.0 * x_crossing)
    response_crossing = DARK0 / sech2(x_crossing)
    ordinary_crossing = matter_crossing + radiation_crossing
    response_to_ordinary = response_crossing / ordinary_crossing
    total_crossing = ordinary_crossing + response_crossing
    q_crossing = deceleration(crossing_n, x_crossing)
    horizon_index_crossing = 0.5 * (1.0 - q_crossing)
    secondary_unit_expectations = {
        "unit_response_density_over_critical0": (response_crossing, 0.7506311, 2e-7),
        "unit_response_to_matter_at_crossing": (
            response_crossing / matter_crossing,
            1.0003953,
            2e-7,
        ),
        "unit_response_to_matter_plus_radiation_at_crossing": (
            response_to_ordinary,
            1.0,
            2e-13,
        ),
        "unit_radiation_fraction_at_crossing": (
            radiation_crossing / total_crossing,
            0.0001975633,
            2e-10,
        ),
        "unit_q_at_crossing": (q_crossing, -0.2499012, 2e-7),
        "unit_horizon_index_at_crossing": (horizon_index_crossing, 0.6249506, 2e-7),
    }
    for identifier, (value, expected, tolerance) in secondary_unit_expectations.items():
        checks.append(
            check(identifier, "independent", close(value, expected, tolerance), value, expected, tolerance)
        )

    radiation_fold = solve_fold(1.56, 6.1)
    late_fold = solve_fold(1.815, 0.65)
    strict_dust_fold = solve_fold(
        1.814,
        0.65,
        omega_r_in_shape=0.0,
        target_dark=1.0 - OMEGA_M0,
    )
    hybrid_fold = solve_fold(
        1.814,
        0.65,
        omega_r_in_shape=0.0,
        target_dark=DARK0,
    )
    fold_expectations = {
        "radiation_fold_nu": (radiation_fold[0], 1.558402308, 2e-9),
        "radiation_fold_x": (radiation_fold[1], 6.106871592, 2e-9),
        "late_fold_nu": (late_fold[0], 1.814657203, 2e-9),
        "late_fold_x": (late_fold[1], 0.649049974, 2e-9),
        "strict_dust_fold_nu": (strict_dust_fold[0], 1.81400853, 2e-8),
        "hybrid_fold_nu": (hybrid_fold[0], 1.81413212, 2e-8),
    }
    for identifier, (value, expected, tolerance) in fold_expectations.items():
        checks.append(
            check(identifier, "independent", close(value, expected, tolerance), value, expected, tolerance)
        )

    scan_left = 1e-8
    scan_right = 80.0
    scan_step = 0.002
    atlas_cases = {
        "nu_1_0": (1.0, [0.2940066]),
        "nu_1_8": (1.8, [0.5466053, 0.8024096, 18.8519793]),
        "nu_1_9": (1.9, [37.7040688]),
        "nu_2_0": (2.0, []),
    }
    atlas_roots: dict[str, list[float]] = {}
    for identifier, (nu, expected_roots) in atlas_cases.items():
        roots = sign_change_roots(
            lambda x, width=nu: closure_residual(x, width, 1.0),
            scan_left,
            scan_right,
            step=scan_step,
        )
        atlas_roots[identifier] = roots
        checks.append(
            check(
                f"{identifier}_root_count",
                "independent",
                len(roots) == len(expected_roots),
                len(roots),
                len(expected_roots),
                0,
            )
        )
        for index, (value, expected) in enumerate(zip(roots, expected_roots), start=1):
            checks.append(
                check(
                    f"{identifier}_root_{index}",
                    "independent",
                    close(value, expected, 2e-7),
                    value,
                    expected,
                    2e-7,
                )
            )

    threshold_ruble = 2.0 * DARK0
    threshold_residual = closure_residual(0.0, 1.0, threshold_ruble)
    checks.append(
        check(
            "past_future_crossing_threshold",
            "independent",
            close(threshold_residual, 0.0, 2e-14),
            threshold_residual,
            0.0,
            2e-14,
        )
    )

    generalized_amplitude_roots: dict[str, float] = {}
    for ruble in (0.8, 1.2, 1.5):
        roots = sign_change_roots(
            lambda x, amplitude=ruble: closure_residual(x, 1.0, amplitude),
            -5.0,
            5.0,
            step=0.002,
        )
        identifier = f"ruble_{ruble:.1f}"
        checks.append(
            check(f"{identifier}_root_count", "independent", len(roots) == 1, len(roots), 1, 0)
        )
        if len(roots) == 1:
            root = roots[0]
            generalized_amplitude_roots[f"{ruble:.1f}"] = root
            residual = closure_residual(root, 1.0, ruble)
            checks.append(
                check(
                    f"{identifier}_closure_residual",
                    "independent",
                    close(residual, 0.0, 2e-12),
                    residual,
                    0.0,
                    2e-12,
                )
            )
            expected_sign = 1 if ruble < threshold_ruble else -1
            actual_sign = 1 if root > 0.0 else -1
            checks.append(
                check(
                    f"{identifier}_crossing_sign",
                    "independent",
                    actual_sign == expected_sign,
                    actual_sign,
                    expected_sign,
                    0,
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
            "response_density_over_critical0_at_crossing": response_crossing,
            "response_to_matter_at_crossing": response_crossing / matter_crossing,
            "response_to_matter_plus_radiation_at_crossing": response_to_ordinary,
            "radiation_fraction_at_crossing": radiation_crossing / total_crossing,
            "q_at_crossing": q_crossing,
            "horizon_index_at_crossing": horizon_index_crossing,
        },
        "atlas_roots": atlas_roots,
        "folds": {
            "radiation": {"nu": radiation_fold[0], "x": radiation_fold[1]},
            "late": {"nu": late_fold[0], "x": late_fold[1]},
            "strict_dust": {"nu": strict_dust_fold[0], "x": strict_dust_fold[1]},
            "hybrid": {"nu": hybrid_fold[0], "x": hybrid_fold[1]},
        },
        "past_future_threshold_ruble": threshold_ruble,
        "generalized_amplitude_roots": generalized_amplitude_roots,
        "amplitude_counterexamples": amplitude_counterexamples,
        "checks": checks,
        "all_pass": all(item["pass"] for item in checks),
        "scope": "arithmetic and formula implementation only",
    }

    output_path = Path(__file__).with_name("background.json")
    output_path.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if output["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
