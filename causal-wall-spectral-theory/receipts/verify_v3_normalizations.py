"""Dependency-free normalization receipts for Causal-Wall Spectral Theory v3.

The script checks algebraic consequences already isolated in the canonical
notes. It does not test the causal-wall construction, the BKM-to-spectral
weld, a microscopic response, a likelihood, or QFT/GR preservation.

Historical v2.1 claims S9, S10, and S12 are intentionally absent.
"""

from __future__ import annotations

import json
import platform
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path


def render_fraction(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def record(
    identifier: str,
    kind: str,
    passed: bool,
    value: object,
    expected: object,
    scope: str,
) -> dict[str, object]:
    return {
        "id": identifier,
        "kind": kind,
        "pass": bool(passed),
        "value": value,
        "expected": expected,
        "scope": scope,
    }


def exact_residual_check(
    identifier: str,
    residuals: list[Fraction],
    scope: str,
) -> dict[str, object]:
    return record(
        identifier,
        "exact_rational_substitution",
        all(residual == 0 for residual in residuals),
        [render_fraction(residual) for residual in residuals],
        "all zero",
        scope,
    )


@dataclass(frozen=True)
class Jet2:
    """Second-order Taylor jet with exact rational coefficients.

    The coefficient ``quadratic`` multiplies t**2 rather than t**2/2.
    Exponential and logarithm are needed only for jets with constant term zero
    and one respectively, which keeps every coefficient rational.
    """

    constant: Fraction
    linear: Fraction = Fraction(0)
    quadratic: Fraction = Fraction(0)

    @staticmethod
    def coerce(value: Jet2 | Fraction | int) -> Jet2:
        if isinstance(value, Jet2):
            return value
        return Jet2(Fraction(value))

    def __add__(self, other: Jet2 | Fraction | int) -> Jet2:
        right = self.coerce(other)
        return Jet2(
            self.constant + right.constant,
            self.linear + right.linear,
            self.quadratic + right.quadratic,
        )

    __radd__ = __add__

    def __neg__(self) -> Jet2:
        return Jet2(-self.constant, -self.linear, -self.quadratic)

    def __sub__(self, other: Jet2 | Fraction | int) -> Jet2:
        return self + (-self.coerce(other))

    def __rsub__(self, other: Jet2 | Fraction | int) -> Jet2:
        return self.coerce(other) - self

    def __mul__(self, other: Jet2 | Fraction | int) -> Jet2:
        right = self.coerce(other)
        return Jet2(
            self.constant * right.constant,
            self.constant * right.linear + self.linear * right.constant,
            self.constant * right.quadratic
            + self.linear * right.linear
            + self.quadratic * right.constant,
        )

    __rmul__ = __mul__

    def reciprocal(self) -> Jet2:
        if self.constant == 0:
            raise ZeroDivisionError("A jet with zero constant term is not invertible")
        return Jet2(
            1 / self.constant,
            -self.linear / self.constant**2,
            self.linear**2 / self.constant**3 - self.quadratic / self.constant**2,
        )

    def __truediv__(self, other: Jet2 | Fraction | int) -> Jet2:
        return self * self.coerce(other).reciprocal()

    def __rtruediv__(self, other: Jet2 | Fraction | int) -> Jet2:
        return self.coerce(other) * self.reciprocal()

    def exp_zero_constant(self) -> Jet2:
        if self.constant != 0:
            raise ValueError("Exact exp jet requires zero constant term")
        return Jet2(1, self.linear, self.quadratic + self.linear**2 / 2)

    def log_unit_constant(self) -> Jet2:
        if self.constant != 1:
            raise ValueError("Exact log jet requires unit constant term")
        return Jet2(0, self.linear, self.quadratic - self.linear**2 / 2)


def spectral_dictionary_checks() -> list[dict[str, object]]:
    scalar_residuals: list[Fraction] = []
    tensor_residuals: list[Fraction] = []
    samples = [
        (Fraction(2, 3), Fraction(5, 2), Fraction(7, 3)),
        (Fraction(1), Fraction(11, 4), Fraction(13, 5)),
        (Fraction(7, 5), Fraction(9, 2), Fraction(17, 6)),
    ]

    for momentum, spin_zero, spin_two in samples:
        momentum_cubed = momentum**3

        # Pi powers are scaled out exactly:
        # delta_s_pi4 = pi^4 Delta_S^2,
        # rho_b_pi2 = rho_B/pi^2,
        # kappa_pi2 = K_zeta/pi^2,
        # information_pi4 = I_zeta/pi^4.
        delta_s_pi4 = 4 / spin_zero
        rho_b_pi2 = spin_zero * momentum_cubed / 64
        kappa_pi2 = momentum_cubed / (2 * delta_s_pi4)
        information_pi4 = 2 * kappa_pi2 / momentum_cubed
        scalar_residuals.extend(
            [
                momentum_cubed / (16 * rho_b_pi2) - delta_s_pi4,
                kappa_pi2 - 8 * rho_b_pi2,
                kappa_pi2 - spin_zero * momentum_cubed / 8,
                information_pi4 - spin_zero / 4,
                4 * information_pi4 - spin_zero,
            ]
        )

        # delta_t_pi4 = pi^4 Delta_T^2 and rho_a_pi2 = rho_A/pi^2.
        delta_t_pi4 = 32 / spin_two
        rho_a_pi2 = spin_two * momentum_cubed / 16
        tensor_to_scalar = delta_t_pi4 / delta_s_pi4
        scalar_precision_pi2 = momentum_cubed / (2 * delta_s_pi4)
        one_polarization_precision_pi2 = momentum_cubed / delta_t_pi4
        tensor_residuals.extend(
            [
                2 * momentum_cubed / rho_a_pi2 - delta_t_pi4,
                tensor_to_scalar - 8 * spin_zero / spin_two,
                spin_two / spin_zero - 8 / tensor_to_scalar,
                one_polarization_precision_pi2 / scalar_precision_pi2
                - 2 / tensor_to_scalar,
            ]
        )

    return [
        exact_residual_check(
            "scalar_spectral_normalizations",
            scalar_residuals,
            "Exact normalization algebra inside the declared holographic spectral member.",
        ),
        exact_residual_check(
            "tensor_spectral_normalizations",
            tensor_residuals,
            "Exact tensor and per-polarization algebra inside the same declared member.",
        ),
    ]


def einstein_member_check() -> dict[str, object]:
    residuals: list[Fraction] = []
    samples = [
        (Fraction(1, 100), Fraction(10_000)),
        (Fraction(3, 200), Fraction(25_000, 3)),
        (Fraction(7, 500), Fraction(40_000, 7)),
    ]

    for epsilon, horizon_capacity in samples:
        scalar_spectrum = 1 / (epsilon * horizon_capacity)
        tensor_spectrum = 16 / horizon_capacity
        spin_zero_pi4 = 4 * epsilon * horizon_capacity
        spin_two_pi4 = 2 * horizon_capacity
        information = spin_zero_pi4 / 4
        tensor_ratio = tensor_spectrum / scalar_spectrum
        residuals.extend(
            [
                4 / spin_zero_pi4 - scalar_spectrum,
                32 / spin_two_pi4 - tensor_spectrum,
                information - epsilon * horizon_capacity,
                tensor_ratio - 16 * epsilon,
                8 * spin_zero_pi4 / spin_two_pi4 - 16 * epsilon,
            ]
        )

    return exact_residual_check(
        "einstein_single_clock_member",
        residuals,
        "Leading Einstein single-clock consistency relations; not a general CWST identity.",
    )


def symmetrized_hessian_check() -> dict[str, object]:
    residuals: list[Fraction] = []
    families = [
        ([Fraction(1, 3), Fraction(2, 3)], [Fraction(-1), Fraction(2)]),
        (
            [Fraction(1, 4), Fraction(1, 2), Fraction(1, 4)],
            [Fraction(-2), Fraction(0), Fraction(3)],
        ),
        (
            [Fraction(2, 7), Fraction(3, 7), Fraction(2, 7)],
            [Fraction(-3, 2), Fraction(1, 3), Fraction(5, 2)],
        ),
    ]

    for weights, scores in families:
        if sum(weights, Fraction(0)) != 1:
            raise ValueError("Reference weights must sum to one")
        mean = sum((weight * score for weight, score in zip(weights, scores)), Fraction(0))
        second_moment = sum(
            (weight * score * score for weight, score in zip(weights, scores)),
            Fraction(0),
        )
        bkm = second_moment - mean * mean

        parameter = Jet2(0, 1, 0)
        unnormalized = [
            weight * (parameter * score).exp_zero_constant()
            for weight, score in zip(weights, scores)
        ]
        partition = sum(unnormalized, Jet2(0))
        tilted = [term / partition for term in unnormalized]

        forward_divergence = sum(
            (
                probability
                * (probability / weight).log_unit_constant()
                for probability, weight in zip(tilted, weights)
            ),
            Jet2(0),
        )
        reverse_divergence = sum(
            (
                weight
                * (weight / probability).log_unit_constant()
                for weight, probability in zip(weights, tilted)
            ),
            Jet2(0),
        )

        forward_hessian = 2 * forward_divergence.quadratic
        reverse_hessian = 2 * reverse_divergence.quadratic
        symmetrized_hessian = forward_hessian + reverse_hessian
        residuals.extend(
            [
                forward_hessian - bkm,
                reverse_hessian - bkm,
                symmetrized_hessian - 2 * bkm,
            ]
        )

    return exact_residual_check(
        "symmetrized_relative_entropy_hessian",
        residuals,
        "Regular finite exponential families at coincidence; the continuum spectral weld remains open.",
    )


def stress_trace_check() -> dict[str, object]:
    dimension = 3
    delta = [
        [Fraction(1) if i == j else Fraction(0) for j in range(dimension)]
        for i in range(dimension)
    ]
    # Choose the momentum along the third axis. The transverse projector is
    # diag(1, 1, 0), so every contraction is exact rational arithmetic.
    transverse = [
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(0)],
    ]

    projector = [[[[Fraction(0) for _ in range(dimension)] for _ in range(dimension)]
                  for _ in range(dimension)] for _ in range(dimension)]
    for i in range(dimension):
        for j in range(dimension):
            for k in range(dimension):
                for ell in range(dimension):
                    projector[i][j][k][ell] = (
                        transverse[i][k] * transverse[j][ell]
                        + transverse[i][ell] * transverse[j][k]
                        - transverse[i][j] * transverse[k][ell]
                    ) / 2

    residuals: list[Fraction] = []
    for k in range(dimension):
        for ell in range(dimension):
            traced = sum(
                (delta[i][j] * projector[i][j][k][ell]
                 for i in range(dimension) for j in range(dimension)),
                Fraction(0),
            )
            residuals.append(traced)

    scalar_double_trace = sum(
        (
            delta[i][j]
            * delta[k][ell]
            * transverse[i][j]
            * transverse[k][ell]
            for i in range(dimension)
            for j in range(dimension)
            for k in range(dimension)
            for ell in range(dimension)
        ),
        Fraction(0),
    )
    residuals.append(scalar_double_trace - 4)

    return exact_residual_check(
        "three_dimensional_stress_trace_contraction",
        residuals,
        "For the registered three-dimensional transverse decomposition: delta.Pi=0 and <TT>=4B.",
    )


def p3_spectrum_check() -> dict[str, object]:
    residuals: list[int] = []
    for ell in range(1, 201):
        gamma_ratio = 1
        for factor in range(ell, ell + 3):
            gamma_ratio *= factor
        residuals.append(gamma_ratio - ell * (ell + 1) * (ell + 2))

    return record(
        "round_sphere_p3_spectrum",
        "exact_integer",
        all(residual == 0 for residual in residuals),
        {"ell_min": 1, "ell_max": 200, "max_absolute_residual": max(map(abs, residuals))},
        "Gamma(ell+3)/Gamma(ell) = ell(ell+1)(ell+2)",
        "Round-sphere eigenvalue formula for the conditional P3 representative.",
    )


def constant_exponent_check() -> dict[str, object]:
    residuals: list[Fraction] = []
    samples = [
        (Fraction(7, 3), Fraction(1, 25), Fraction(-2), Fraction(1, 3)),
        (Fraction(-4, 5), Fraction(7, 100), Fraction(5, 2), Fraction(2, 5)),
        (Fraction(11, 7), Fraction(3, 80), Fraction(1, 4), Fraction(3, 7)),
    ]

    for intercept, exponent, log_momentum, step in samples:
        def log_information(coordinate: Fraction) -> Fraction:
            return intercept + exponent * coordinate

        first_derivative = (
            log_information(log_momentum + step)
            - log_information(log_momentum - step)
        ) / (2 * step)
        second_derivative = (
            log_information(log_momentum + step)
            - 2 * log_information(log_momentum)
            + log_information(log_momentum - step)
        ) / (step * step)
        tilt = -first_derivative
        running = -second_derivative
        residuals.extend(
            [
                first_derivative - exponent,
                tilt + exponent,
                second_derivative,
                running,
            ]
        )

    return exact_residual_check(
        "constant_exponent_log_derivatives",
        residuals,
        "Inside the member ln(I)=constant+delta ln(k): n_s-1=-delta and alpha_s=0.",
    )


def main() -> int:
    checks: list[dict[str, object]] = []
    checks.extend(spectral_dictionary_checks())
    checks.append(einstein_member_check())
    checks.append(symmetrized_hessian_check())
    checks.append(stress_trace_check())
    checks.append(p3_spectrum_check())
    checks.append(constant_exponent_check())

    failed = sum(not check["pass"] for check in checks)
    payload = {
        "schema_version": 1,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(),
        "scope": (
            "Algebraic normalization checks only. No wall construction, "
            "BKM-to-spectral weld, microscopic response, likelihood, or recovery claim."
        ),
        "excluded_legacy_claims": {
            "S9": "No tilt-difference running estimator and no universal delta-squared running bound.",
            "S10": "No universal non-Gaussianity floor or order-one kill from c^(0).",
            "S12": "No rank or central-charge inference N approximately sqrt(c^(0)).",
        },
        "checks": checks,
        "summary": {
            "total": len(checks),
            "passed": len(checks) - failed,
            "failed": failed,
            "all_pass": failed == 0,
        },
    }

    output_path = Path(__file__).with_suffix(".json")
    output_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    for check in checks:
        label = "PASS" if check["pass"] else "FAIL"
        print(f"[{label}] {check['id']}")
    print(f"\n{len(checks) - failed}/{len(checks)} checks pass.")
    print(f"Wrote {output_path}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
