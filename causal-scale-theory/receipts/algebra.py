"""Dependency-free algebra receipts for Causal Scale Theory.

Exact checks are evaluated with rational arithmetic after writing the binary
identities in terms of polarization m = tanh(theta) and binary metric
g_bin = 1 - m**2. Numerical checks are limited to integrals or transcendental
representations. The script verifies formula implementation, not the physical
wall, source, or unit principles.
"""

from __future__ import annotations

import json
import math
import platform
import sys
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path


def record(
    identifier: str,
    kind: str,
    passed: bool,
    value: object,
    expected: object,
    tolerance: object = None,
) -> dict[str, object]:
    return {
        "id": identifier,
        "kind": kind,
        "pass": bool(passed),
        "value": value,
        "expected": expected,
        "tolerance": tolerance,
    }


def rational_zero_check(identifier: str, residuals: list[Fraction]) -> dict[str, object]:
    values = [str(value) for value in residuals]
    return record(identifier, "exact_rational", all(value == 0 for value in residuals), values, "all zero")


def simpson(function, left: float, right: float, intervals: int) -> float:
    if intervals % 2:
        raise ValueError("Simpson intervals must be even")
    step = (right - left) / intervals
    total = function(left) + function(right)
    for index in range(1, intervals):
        total += (4.0 if index % 2 else 2.0) * function(left + index * step)
    return total * step / 3.0


def main() -> int:
    checks: list[dict[str, object]] = []
    samples = [
        (Fraction(-2, 5), Fraction(1, 2)),
        (Fraction(0), Fraction(1)),
        (Fraction(1, 3), Fraction(3, 2)),
        (Fraction(4, 5), Fraction(7, 3)),
    ]

    balance_residuals: list[Fraction] = []
    casimir_derivative_residuals: list[Fraction] = []
    conic_residuals: list[Fraction] = []
    curvature_residuals: list[Fraction] = []
    shape_residuals: list[Fraction] = []
    riccati_residuals: list[Fraction] = []
    witten_residuals: list[Fraction] = []

    for polarization, nu in samples:
        binary_metric = 1 - polarization * polarization
        polarization_prime = nu * binary_metric
        binary_metric_prime = -2 * nu * polarization * binary_metric

        balance_residuals.append(polarization * polarization + binary_metric - 1)
        casimir_derivative_residuals.append(
            2 * polarization * polarization_prime + binary_metric_prime
        )

        log_density_prime = -2 * nu * polarization
        log_density_second = -2 * nu * nu * binary_metric
        conic_residuals.append(
            binary_metric + log_density_prime * log_density_prime / (4 * nu * nu) - 1
        )
        curvature_residuals.append(log_density_second + 2 * nu * nu * binary_metric)

        one_plus_w = 2 * nu * polarization / 3
        w_prime = 2 * nu * nu * binary_metric / 3
        shape_residuals.append(9 * one_plus_w * one_plus_w + 6 * w_prime - 4 * nu * nu)

        delta = 2 * nu * polarization
        delta_prime = 2 * nu * nu * binary_metric
        riccati_residuals.append(delta_prime - (2 * nu * nu - delta * delta / 2))

        potential_minus = polarization * polarization - binary_metric
        potential_plus = polarization * polarization + binary_metric
        zero_mode_density = binary_metric / 2
        zero_mode_derivative_coefficient = -polarization
        witten_residuals.extend(
            [
                potential_minus - (1 - 2 * binary_metric),
                potential_plus - 1,
                2 * zero_mode_density - binary_metric,
                zero_mode_derivative_coefficient + polarization,
            ]
        )

    checks.extend(
        [
            rational_zero_check("binary_casimir_balance", balance_residuals),
            rational_zero_check(
                "binary_casimir_derivative_identity",
                casimir_derivative_residuals,
            ),
            rational_zero_check("density_conic", conic_residuals),
            rational_zero_check("density_log_curvature", curvature_residuals),
            rational_zero_check("equation_of_state_invariant", shape_residuals),
            rational_zero_check("density_riccati", riccati_residuals),
            rational_zero_check("witten_factorization_and_zero_mode", witten_residuals),
        ]
    )

    dimension_residuals: list[Fraction] = []
    equal_partition_residuals: list[Fraction] = []
    for dimension in range(2, 8):
        for crossing_ratio in (Fraction(1, 2), Fraction(1), Fraction(4, 3)):
            if crossing_ratio >= dimension - 1:
                continue
            fraction = crossing_ratio / (dimension - 1)
            complement_ratio = fraction / (1 - fraction)
            dimension_residuals.append(
                complement_ratio
                - crossing_ratio / (dimension - 1 - crossing_ratio)
            )
            equal_partition_residuals.append(
                (complement_ratio - 1) * (dimension - 1 - crossing_ratio)
                - (2 * crossing_ratio - (dimension - 1))
            )
        equal_partition_crossing_ratio = Fraction(dimension - 1, 2)
        equal_partition_fraction = equal_partition_crossing_ratio / (dimension - 1)
        equal_partition_ratio = equal_partition_crossing_ratio / (
            dimension - 1 - equal_partition_crossing_ratio
        )
        equal_partition_residuals.extend(
            [
                equal_partition_fraction - Fraction(1, 2),
                equal_partition_ratio - 1,
            ]
        )
    dimension_residuals.append(Fraction(1, 3 - 1) - Fraction(1, 2))
    checks.append(rational_zero_check("dimensional_crossing_law", dimension_residuals))
    checks.append(rational_zero_check("dimensional_equal_partition_law", equal_partition_residuals))
    unit_equal_dimension = 2 * Fraction(1) + 1
    checks.append(
        record(
            "unit_equal_partition_selects_d3",
            "exact_rational",
            unit_equal_dimension == 3,
            str(unit_equal_dimension),
            "3",
        )
    )

    hawking_residuals: list[Fraction] = []
    for radius in (Fraction(2, 3), Fraction(1), Fraction(7, 4)):
        temperature_entropy = radius / 2
        misner_sharp_energy = radius / 2
        source_peak = temperature_entropy / 2
        half_critical_horizon_energy = misner_sharp_energy / 2
        hawking_residuals.extend(
            [
                temperature_entropy - misner_sharp_energy,
                source_peak - half_critical_horizon_energy,
            ]
        )
    checks.append(rational_zero_check("hawking_friedmann_coefficients", hawking_residuals))

    central_residuals: list[Fraction] = []
    for weight_one, weight_two, common_factor, value_one, value_two, shift in (
        (
            Fraction(2, 5),
            Fraction(3, 7),
            Fraction(11, 4),
            Fraction(-3, 2),
            Fraction(5, 3),
            Fraction(7, 4),
        ),
        (
            Fraction(5, 8),
            Fraction(7, 9),
            Fraction(13, 6),
            Fraction(4, 5),
            Fraction(11, 6),
            Fraction(-9, 7),
        ),
    ):
        probability_one = weight_one / (weight_one + weight_two)
        probability_two = weight_two / (weight_one + weight_two)
        shifted_normalizer = common_factor * weight_one + common_factor * weight_two
        shifted_probability_one = common_factor * weight_one / shifted_normalizer
        shifted_probability_two = common_factor * weight_two / shifted_normalizer
        central_residuals.extend(
            [
                shifted_probability_one - probability_one,
                shifted_probability_two - probability_two,
            ]
        )
        mean = probability_one * value_one + probability_two * value_two
        second = probability_one * value_one * value_one + probability_two * value_two * value_two
        variance = second - mean * mean
        shifted_mean = (
            shifted_probability_one * (value_one + shift)
            + shifted_probability_two * (value_two + shift)
        )
        shifted_second = (
            shifted_probability_one * (value_one + shift) * (value_one + shift)
            + shifted_probability_two * (value_two + shift) * (value_two + shift)
        )
        shifted_variance = shifted_second - shifted_mean * shifted_mean
        central_residuals.extend(
            [
                shifted_mean - (mean + shift),
                shifted_second - (second + 2 * shift * mean + shift * shift),
                shifted_variance - variance,
            ]
        )
    checks.append(rational_zero_check("central_normalization_and_shifted_moments", central_residuals))

    fisher_length = simpson(lambda value: 1.0 / math.cosh(value), -20.0, 20.0, 200_000)
    checks.append(
        record(
            "fisher_length",
            "independent_quadrature",
            abs(fisher_length - math.pi) < 2e-8,
            fisher_length,
            math.pi,
            2e-8,
        )
    )

    zero_mode_norm = simpson(
        lambda value: 0.5 / (math.cosh(value) ** 2),
        -20.0,
        20.0,
        200_000,
    )
    checks.append(
        record(
            "witten_zero_mode_norm",
            "independent_quadrature",
            abs(zero_mode_norm - 1.0) < 2e-12,
            zero_mode_norm,
            1.0,
            2e-12,
        )
    )

    reflected_residuals: list[float] = []
    for polarization in (-0.8, -0.3, 0.2, 0.7):
        theta = math.atanh(polarization)
        probability_plus = 0.5 * (1.0 + polarization)
        probability_minus = 0.5 * (1.0 - polarization)
        one_sided = (
            probability_plus * math.log(probability_plus / probability_minus)
            + probability_minus * math.log(probability_minus / probability_plus)
        )
        reflected_residuals.append(one_sided - 2.0 * theta * polarization)
    checks.append(
        record(
            "reflected_relative_entropy",
            "independent_numeric",
            max(abs(value) for value in reflected_residuals) < 2e-15,
            reflected_residuals,
            "all zero",
            2e-15,
        )
    )

    schrodinger_residuals: list[float] = []
    transmission_residuals: list[float] = []
    for polarization in (-0.6, 0.0, 0.75):
        binary_metric = 1.0 - polarization * polarization
        for momentum in (0.3, 1.0, 2.5):
            # psi_k(theta) = f(theta) exp(i k theta), with
            # f(theta) = tanh(theta) - i k. Reduce the eigenvalue equation
            # [H_- - (1 + k^2)] psi_k = 0 to the coefficient of exp(i k theta).
            factor = complex(polarization, -momentum)
            factor_prime = binary_metric
            factor_second = -2.0 * polarization * binary_metric
            psi_second_coefficient = (
                factor_second
                + 2.0j * momentum * factor_prime
                - momentum * momentum * factor
            )
            potential_minus = 1.0 - 2.0 * binary_metric
            eigen_residual = (
                -psi_second_coefficient
                + potential_minus * factor
                - (1.0 + momentum * momentum) * factor
            )
            schrodinger_residuals.append(abs(eigen_residual))
            transmission = complex(momentum, 1.0) / complex(momentum, -1.0)
            transmission_residuals.append(abs(abs(transmission) - 1.0))
    checks.extend(
        [
            record(
                "witten_scattering_schrodinger_residual",
                "analytic_numeric",
                max(schrodinger_residuals) < 3e-15,
                schrodinger_residuals,
                "all zero",
                3e-15,
            ),
            record(
                "witten_scattering_transmission_modulus",
                "analytic_numeric",
                max(transmission_residuals) < 2e-15,
                transmission_residuals,
                "all zero",
                2e-15,
            ),
        ]
    )

    output = {
        "receipt": "causal-scale-theory reduced algebra",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "runtime": {"python": sys.version, "platform": platform.platform()},
        "scope": "reduced algebra and formula implementation only",
        "checks": checks,
        "all_pass": all(item["pass"] for item in checks),
    }
    output_path = Path(__file__).with_name("algebra.json")
    output_path.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if output["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
