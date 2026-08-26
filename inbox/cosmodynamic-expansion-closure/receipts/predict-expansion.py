"""Receipt for the provisional cosmodynamic expansion closure.

This standard-library calculation verifies the frozen CST-B2 unit background,
its dimensionless age, and the rank-one apparent-horizon ledger. Passing checks
formula implementation and arithmetic only. It does not validate the wall,
the unity principles, the constitutive source, or the Einstein-FLRW bridge.
"""

from __future__ import annotations

import argparse
import json
import math
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable


C = 299_792_458.0
G = 6.67430e-11
HBAR = 1.054_571_817e-34
KB = 1.380_649e-23
MPC = 3.085_677_581_491_367_3e22
JULIAN_YEAR = 365.25 * 86_400.0
GYR = 1.0e9 * JULIAN_YEAR
GLY = C * GYR

DEFAULT_OMEGA_M0 = 0.310598
DEFAULT_OMEGA_R0 = 9.15e-5
DEFAULT_NU = 1.0
DEFAULT_MATCHING = 1.0
DEFAULT_H0_KM_S_MPC = 67.4
DEFAULT_AGE_CALIBRATION_GYR = 13.8


def sech2(value: float) -> float:
    magnitude = abs(value)
    if magnitude < 350.0:
        cosine = math.cosh(value)
        return 1.0 / (cosine * cosine)
    return 4.0 * math.exp(-2.0 * magnitude)


def bisect(
    function: Callable[[float], float],
    left: float,
    right: float,
    *,
    tolerance: float = 1e-14,
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
    roots: list[float] = []
    x_left = left
    f_left = function(x_left)
    count = int(math.ceil((right - left) / step))
    for index in range(1, count + 1):
        x_right = min(right, left + index * step)
        f_right = function(x_right)
        if f_left == 0.0 or f_left * f_right < 0.0:
            root = bisect(function, x_left, x_right)
            if not roots or abs(root - roots[-1]) > 10.0 * step:
                roots.append(root)
        x_left = x_right
        f_left = f_right
    return roots


def simpson(function: Callable[[float], float], left: float, right: float, panels: int) -> float:
    if panels <= 0:
        raise ValueError("panels must be positive")
    if panels % 2:
        panels += 1
    width = (right - left) / panels
    total = function(left) + function(right)
    total += 4.0 * sum(
        function(left + (2 * index - 1) * width)
        for index in range(1, panels // 2 + 1)
    )
    total += 2.0 * sum(
        function(left + 2 * index * width)
        for index in range(1, panels // 2)
    )
    return total * width / 3.0


def close(actual: float, expected: float, tolerance: float) -> bool:
    return abs(actual - expected) <= tolerance


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--omega-m0", type=float, default=DEFAULT_OMEGA_M0)
    parser.add_argument("--omega-r0", type=float, default=DEFAULT_OMEGA_R0)
    parser.add_argument("--nu", type=float, default=DEFAULT_NU)
    parser.add_argument("--matching", type=float, default=DEFAULT_MATCHING)
    parser.add_argument("--h0", type=float, default=DEFAULT_H0_KM_S_MPC)
    parser.add_argument(
        "--omega-m-provenance",
        default="repository benchmark; empirical input, not a prediction",
    )
    parser.add_argument(
        "--omega-m-status",
        default="BENCHMARK INPUT",
    )
    parser.add_argument(
        "--age-calibration-gyr",
        type=float,
        default=DEFAULT_AGE_CALIBRATION_GYR,
    )
    parser.add_argument("--output", type=Path)
    parser.add_argument("--no-write", action="store_true")
    args = parser.parse_args()

    omega_m0 = args.omega_m0
    omega_r0 = args.omega_r0
    dark0 = 1.0 - omega_m0 - omega_r0
    nu = args.nu
    matching = args.matching
    if min(omega_m0, omega_r0, dark0, nu) <= 0.0:
        raise ValueError("densities and nu must be positive")
    if not 0.0 < matching < 2.0:
        raise ValueError("matching must lie in (0, 2)")

    amplitude = matching / (2.0 - matching)

    def closure_residual(x_value: float) -> float:
        ordinary = (
            omega_m0 * math.exp(3.0 * x_value)
            + omega_r0 * math.exp(4.0 * x_value)
        )
        return amplitude * ordinary * sech2(nu * x_value) - dark0

    crossing_roots = sign_change_roots(
        closure_residual,
        1e-10,
        50.0,
        step=0.002,
    )
    if not crossing_roots:
        raise ArithmeticError("no positive closure root found in the declared scan")
    x_crossing = crossing_roots[0]

    response_normalizer = sech2(nu * x_crossing)

    def e2_derivatives(n_value: float) -> tuple[float, float, float]:
        matter = omega_m0 * math.exp(-3.0 * n_value)
        radiation = omega_r0 * math.exp(-4.0 * n_value)
        centered = nu * (n_value + x_crossing)
        profile = sech2(centered)
        polarization = math.tanh(centered)
        response = dark0 * profile / response_normalizer
        response_first = -2.0 * nu * polarization * response
        response_second = (
            4.0 * nu * nu * polarization * polarization * response
            - 2.0 * nu * nu * profile * response
        )
        value = matter + radiation + response
        first = -3.0 * matter - 4.0 * radiation + response_first
        second = 9.0 * matter + 16.0 * radiation + response_second
        return value, first, second

    def deceleration(n_value: float) -> float:
        value, first, _ = e2_derivatives(n_value)
        return -1.0 - 0.5 * first / value

    def jerk(n_value: float) -> float:
        value, first, second = e2_derivatives(n_value)
        q_value = -1.0 - 0.5 * first / value
        dq_dn = -0.5 * (second / value - (first / value) ** 2)
        return q_value * (2.0 * q_value + 1.0) - dq_dn

    def age_integrand(scale_factor: float) -> float:
        if scale_factor == 0.0:
            return 0.0
        n_value = math.log(scale_factor)
        return 1.0 / (scale_factor * math.sqrt(e2_derivatives(n_value)[0]))

    dimensionless_age_coarse = simpson(age_integrand, 0.0, 1.0, 50_000)
    dimensionless_age = simpson(age_integrand, 0.0, 1.0, 100_000)

    acceleration_roots = sign_change_roots(deceleration, -3.0, 5.0, step=0.002)
    past_acceleration_roots = [root for root in acceleration_roots if root < 0.0]
    future_acceleration_roots = [root for root in acceleration_roots if root > 0.0]
    acceleration_entry_n = (
        max(past_acceleration_roots) if past_acceleration_roots else None
    )
    acceleration_exit_n = (
        min(future_acceleration_roots) if future_acceleration_roots else None
    )

    crossing_n = -x_crossing
    crossing_e2 = e2_derivatives(crossing_n)[0]
    h_crossing_over_h0 = math.sqrt(crossing_e2)
    z_crossing = math.exp(x_crossing) - 1.0
    w0 = -1.0 + (2.0 * nu / 3.0) * math.tanh(nu * x_crossing)
    wa = -(2.0 * nu * nu / 3.0) * sech2(nu * x_crossing)
    q0 = deceleration(0.0)
    j0 = jerk(0.0)

    h0_si = args.h0 * 1_000.0 / MPC
    planck_time = math.sqrt(HBAR * G / C**5)
    planck_length = C * planck_time

    def horizon_ledger(hubble_si: float) -> dict[str, float]:
        radius = C / hubble_si
        mass = C**3 / (2.0 * G * hubble_si)
        energy = mass * C**2
        entropy_nats = math.pi / (hubble_si * planck_time) ** 2
        temperature = HBAR * hubble_si / (2.0 * math.pi * KB)
        resolution_depth = math.log(radius / planck_length)
        inferred_hubble = {
            "from_radius": C / radius,
            "from_mass": C**3 / (2.0 * G * mass),
            "from_energy": C**5 / (2.0 * G * energy),
            "from_entropy": math.sqrt(math.pi / entropy_nats) / planck_time,
            "from_temperature": 2.0 * math.pi * KB * temperature / HBAR,
        }
        return {
            "hubble_s_inverse": hubble_si,
            "radius_m": radius,
            "radius_gly": radius / GLY,
            "mass_kg": mass,
            "energy_j": energy,
            "entropy_over_kb_nats": entropy_nats,
            "temperature_k": temperature,
            "resolution_depth": resolution_depth,
            "horizon_identity_ratio": KB * temperature * entropy_nats / energy,
            "max_relative_hubble_reconstruction_error": max(
                abs(value / hubble_si - 1.0) for value in inferred_hubble.values()
            ),
        }

    present_ledger = horizon_ledger(h0_si)
    crossing_ledger = horizon_ledger(h0_si * h_crossing_over_h0)

    sample_redshifts = [0.0, 0.25, 0.5, 0.75, 1.0, 2.0]
    samples = []
    for redshift in sample_redshifts:
        n_value = -math.log1p(redshift)
        samples.append(
            {
                "z": redshift,
                "h_over_h0": math.sqrt(e2_derivatives(n_value)[0]),
                "q": deceleration(n_value),
            }
        )

    age_gyr = dimensionless_age / h0_si / GYR
    h0_from_age = (
        dimensionless_age / (args.age_calibration_gyr * GYR) * MPC / 1_000.0
    )

    checks = {
        "closure_residual": abs(closure_residual(x_crossing)) < 2e-13,
        "present_normalization": close(e2_derivatives(0.0)[0], 1.0, 2e-13),
        "age_quadrature_convergence": abs(dimensionless_age - dimensionless_age_coarse) < 2e-10,
        "present_horizon_identity": close(present_ledger["horizon_identity_ratio"], 1.0, 2e-13),
        "crossing_horizon_identity": close(crossing_ledger["horizon_identity_ratio"], 1.0, 2e-13),
        "present_rank_one_reconstruction": present_ledger["max_relative_hubble_reconstruction_error"] < 2e-15,
        "crossing_rank_one_reconstruction": crossing_ledger["max_relative_hubble_reconstruction_error"] < 2e-15,
    }

    default_run = all(
        close(actual, expected, 1e-15)
        for actual, expected in (
            (omega_m0, DEFAULT_OMEGA_M0),
            (omega_r0, DEFAULT_OMEGA_R0),
            (nu, DEFAULT_NU),
            (matching, DEFAULT_MATCHING),
            (args.h0, DEFAULT_H0_KM_S_MPC),
        )
    )
    if default_run:
        if acceleration_entry_n is None or acceleration_exit_n is None:
            raise ArithmeticError("the frozen unit branch must have two acceleration boundaries")
        regression = {
            "x_crossing": close(x_crossing, 0.2940065550582187, 3e-13),
            "dimensionless_age": close(dimensionless_age, 0.9518469555679118, 3e-11),
            "q0": close(q0, -0.3369024707078755, 3e-12),
            "j0": close(j0, -0.11124646428421958, 3e-12),
            "entry_z": close(math.exp(-acceleration_entry_n) - 1.0, 0.7856935256176354, 3e-10),
            "exit_a": close(math.exp(acceleration_exit_n), 11.78652452215664, 3e-9),
        }
        checks.update({f"regression_{key}": value for key, value in regression.items()})

    output = {
        "receipt": "provisional cosmodynamic expansion closure",
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "runtime": {"python": sys.version, "platform": platform.platform()},
        "inputs": {
            "omega_m0": omega_m0,
            "omega_m0_provenance": args.omega_m_provenance,
            "omega_m0_status": args.omega_m_status,
            "omega_r0": omega_r0,
            "omega_x0": dark0,
            "response_to_non_x_today": dark0 / (omega_m0 + omega_r0),
            "nu": nu,
            "matching_ratio": matching,
            "root_policy": "smallest positive root",
            "h0_km_s_mpc": args.h0,
            "age_calibration_gyr": args.age_calibration_gyr,
        },
        "shape_outputs": {
            "positive_closure_roots": crossing_roots,
            "x_crossing": x_crossing,
            "z_crossing": z_crossing,
            "h_crossing_over_h0": h_crossing_over_h0,
            "w0": w0,
            "wa_local_cpl": wa,
            "q0": q0,
            "j0": j0,
            "acceleration_boundary_roots_n": acceleration_roots,
            "acceleration_entry_n": acceleration_entry_n,
            "acceleration_entry_z": (
                math.exp(-acceleration_entry_n) - 1.0
                if acceleration_entry_n is not None
                else None
            ),
            "acceleration_exit_n": acceleration_exit_n,
            "acceleration_exit_a_over_a0": (
                math.exp(acceleration_exit_n)
                if acceleration_exit_n is not None
                else None
            ),
            "dimensionless_age_h0_t0": dimensionless_age,
            "samples": samples,
        },
        "absolute_calibration": {
            "proper_age_gyr_from_h0": age_gyr,
            "h0_km_s_mpc_from_declared_age": h0_from_age,
            "present_horizon": present_ledger,
            "crossing_horizon": crossing_ledger,
        },
        "checks": checks,
        "all_pass": all(checks.values()),
        "claim_scope": (
            "arithmetic, numerical integration, and horizon-identity verification only; "
            "not physical validation or a first-principles wall return"
        ),
    }

    if not args.no_write:
        output_path = args.output or Path(__file__).with_name("prediction.json")
        output_path.write_text(
            json.dumps(output, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if output["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
