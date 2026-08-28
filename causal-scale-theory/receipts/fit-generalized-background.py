#!/usr/bin/env python3
"""Branch-aware generalized CST-B2 late-time background profile.

This receipt reuses the data loaders, distance integrator, and nuisance-profile
conventions of fit-late-time-background.py.  It releases the CST-B2 rate nu
and canonical integrated reference ratio R_c without choosing the smallest
root at fixed parameters.  Instead, x_c itself labels a root-background pair;
the closure then returns R_c exactly.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

import numpy as np


sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
BASE_PATH = HERE / "fit-late-time-background.py"
BASE_SPEC = importlib.util.spec_from_file_location(
    "cst_late_time_background_receipt", BASE_PATH
)
if BASE_SPEC is None or BASE_SPEC.loader is None:
    raise ImportError(f"cannot load shared receipt from {BASE_PATH}")
BASE = importlib.util.module_from_spec(BASE_SPEC)
sys.modules[BASE_SPEC.name] = BASE
BASE_SPEC.loader.exec_module(BASE)


OMEGA_M_BOUNDS = (0.15, 0.50)
NU_BOUNDS = (0.001, 4.0)
A_POSITIVE_BOUNDS = (1.0e-8, 10.0)
NEGATIVE_AUDIT_NU_BOUNDS = (0.02, 4.0)
NEGATIVE_AUDIT_A_BOUNDS = (-10.0, -1.0e-8)


def log_cosh(value: float) -> float:
    absolute = abs(value)
    return absolute + math.log1p(math.exp(-2.0 * absolute)) - math.log(2.0)


def canonical_ratio(
    omega_m: float, nu: float, a_crossing: float, omega_r: float
) -> tuple[float, float, float]:
    """Return x_c, canonical R_c, and historical r_c=R_c/(2-R_c)."""

    x_crossing = a_crossing / nu
    complement = 1.0 - omega_m - omega_r
    if omega_r > 0.0:
        log_m = float(
            np.logaddexp(
                math.log(omega_m) + 3.0 * x_crossing,
                math.log(omega_r) + 4.0 * x_crossing,
            )
        )
    else:
        log_m = math.log(omega_m) + 3.0 * x_crossing
    log_f = log_m - 2.0 * log_cosh(a_crossing)
    log_historical = math.log(complement) - log_f
    if log_historical > 700.0:
        historical = math.inf
        canonical = 2.0
    elif log_historical < -700.0:
        historical = 0.0
        canonical = 0.0
    else:
        historical = math.exp(log_historical)
        canonical = 2.0 * historical / (1.0 + historical)
    return x_crossing, canonical, historical


def omega_m_from_canonical_ratio(
    canonical: float, nu: float, a_crossing: float, omega_r: float
) -> float:
    """Solve the present-flatness closure exactly for Omega_m."""

    historical = canonical / (2.0 - canonical)
    inverse_historical = 1.0 / historical
    x_crossing = a_crossing / nu
    log_profile = -2.0 * log_cosh(a_crossing)
    log_inverse_historical = math.log(inverse_historical)
    matter_ratio_log = 3.0 * x_crossing + log_profile - log_inverse_historical
    radiation_ratio_log = (
        4.0 * x_crossing + log_profile - log_inverse_historical
    )
    if radiation_ratio_log > 700.0:
        return -math.inf
    matter_ratio = (
        math.exp(matter_ratio_log) if matter_ratio_log < 700.0 else math.inf
    )
    radiation_ratio = math.exp(radiation_ratio_log)
    return (
        (1.0 - omega_r) - omega_r * radiation_ratio
    ) / (1.0 + matter_ratio)


def expansion_function(
    omega_m: float,
    nu: float,
    a_crossing: float,
    omega_r: float,
) -> Callable[[np.ndarray], np.ndarray]:
    complement = 1.0 - omega_m - omega_r
    normalizer = math.cosh(a_crossing)

    def expansion(redshift: np.ndarray) -> np.ndarray:
        one_plus = 1.0 + redshift
        response_ratio = (
            normalizer
            / np.cosh(a_crossing - nu * np.log1p(redshift))
        ) ** 2
        return np.sqrt(
            omega_m * one_plus**3
            + omega_r * one_plus**4
            + complement * response_ratio
        )

    return expansion


class Likelihood:
    def __init__(
        self,
        pantheon: BASE.PantheonLikelihood,
        bao: BASE.BaoLikelihood,
        omega_r: float,
    ) -> None:
        self.pantheon = pantheon
        self.bao = bao
        self.omega_r = omega_r
        self.cache: dict[tuple[float, float, float], dict[str, float]] = {}

    def evaluate(
        self, omega_m: float, nu: float, a_crossing: float
    ) -> dict[str, float]:
        key = (
            round(float(omega_m), 11),
            round(float(nu), 11),
            round(float(a_crossing), 11),
        )
        if key in self.cache:
            return self.cache[key]
        if not (
            OMEGA_M_BOUNDS[0] <= omega_m <= OMEGA_M_BOUNDS[1]
            and NU_BOUNDS[0] <= nu <= NU_BOUNDS[1]
            and -10.0 <= a_crossing <= 10.0
            and abs(a_crossing) >= 1.0e-10
        ):
            return {"chi_square": 1.0e50}

        expansion = expansion_function(omega_m, nu, a_crossing, self.omega_r)
        maximum_redshift = max(
            float(np.max(self.pantheon.z_hd)),
            float(np.max(self.bao.redshift)),
        )
        distance = BASE.comoving_distance_interpolator(
            expansion, maximum_redshift
        )

        luminosity_distance = (
            (1.0 + self.pantheon.z_hel) * distance(self.pantheon.z_hd)
        )
        residual_without_offset = self.pantheon.magnitude - 5.0 * np.log10(
            luminosity_distance
        )
        offset = float(
            self.pantheon.inverse_covariance_ones @ residual_without_offset
        ) / self.pantheon.ones_inverse_covariance_ones
        sn_residual = residual_without_offset - offset
        sn_chi = float(
            sn_residual @ self.pantheon.inverse_covariance @ sn_residual
        )

        e_value = expansion(self.bao.redshift)
        chi_value = distance(self.bao.redshift)
        shape = np.empty_like(self.bao.value)
        for index, quantity in enumerate(self.bao.quantity):
            if quantity == "DM_over_rs":
                shape[index] = chi_value[index]
            elif quantity == "DH_over_rs":
                shape[index] = 1.0 / e_value[index]
            elif quantity == "DV_over_rs":
                shape[index] = (
                    self.bao.redshift[index]
                    * chi_value[index] ** 2
                    / e_value[index]
                ) ** (1.0 / 3.0)
            else:
                raise ValueError(f"unknown BAO quantity: {quantity}")
        inverse = self.bao.inverse_covariance
        amplitude = float(shape @ inverse @ self.bao.value) / float(
            shape @ inverse @ shape
        )
        bao_residual = self.bao.value - amplitude * shape
        bao_chi = float(bao_residual @ inverse @ bao_residual)

        x_crossing, canonical, historical = canonical_ratio(
            omega_m, nu, a_crossing, self.omega_r
        )
        result = {
            "chi_square": sn_chi + bao_chi,
            "chi_square_pantheon_plus": sn_chi,
            "chi_square_desi_dr2_bao": bao_chi,
            "omega_m": omega_m,
            "nu": nu,
            "a_crossing_equals_nu_x_crossing": a_crossing,
            "x_crossing": x_crossing,
            "z_crossing": math.expm1(x_crossing) if x_crossing < 700.0 else math.inf,
            "canonical_R_c": canonical,
            "historical_r_c_equals_R_c_over_2_minus_R_c": historical,
            "profiled_sn_offset": offset,
            "bao_profile_amplitude_c_over_H0rd": amplitude,
            "profiled_rd_h_mpc": BASE.C_KM_S / (100.0 * amplitude),
        }
        self.cache[key] = result
        return result

    def chi(self, omega_m: float, nu: float, a_crossing: float) -> float:
        return float(self.evaluate(omega_m, nu, a_crossing)["chi_square"])


def bounded_nelder_mead(
    function: Callable[[np.ndarray], float],
    start: list[float] | np.ndarray,
    bounds: list[tuple[float, float]],
    maximum_iterations: int = 220,
) -> tuple[np.ndarray, float]:
    low = np.asarray([bound[0] for bound in bounds])
    high = np.asarray([bound[1] for bound in bounds])
    dimension = len(bounds)

    def transform(value: np.ndarray) -> np.ndarray:
        clipped = np.clip(value, -40.0, 40.0)
        return low + (high - low) / (1.0 + np.exp(-clipped))

    fraction = (np.asarray(start) - low) / (high - low)
    fraction = np.clip(fraction, 1.0e-12, 1.0 - 1.0e-12)
    origin = np.log(fraction / (1.0 - fraction))
    simplex = [origin]
    for index in range(dimension):
        vertex = origin.copy()
        vertex[index] += 0.20
        simplex.append(vertex)
    simplex_array = np.asarray(simplex)
    values = np.asarray([function(transform(vertex)) for vertex in simplex_array])

    for _ in range(maximum_iterations):
        order = np.argsort(values)
        simplex_array = simplex_array[order]
        values = values[order]
        if float(np.std(values)) < 2.0e-9:
            break
        centroid = np.mean(simplex_array[:-1], axis=0)
        reflected = 2.0 * centroid - simplex_array[-1]
        reflected_value = function(transform(reflected))
        if values[0] <= reflected_value < values[-2]:
            simplex_array[-1], values[-1] = reflected, reflected_value
            continue
        if reflected_value < values[0]:
            expanded = 3.0 * centroid - 2.0 * simplex_array[-1]
            expanded_value = function(transform(expanded))
            if expanded_value < reflected_value:
                simplex_array[-1], values[-1] = expanded, expanded_value
            else:
                simplex_array[-1], values[-1] = reflected, reflected_value
            continue
        contracted = centroid + 0.5 * (simplex_array[-1] - centroid)
        contracted_value = function(transform(contracted))
        if contracted_value < values[-1]:
            simplex_array[-1], values[-1] = contracted, contracted_value
            continue
        for index in range(1, dimension + 1):
            simplex_array[index] = simplex_array[0] + 0.5 * (
                simplex_array[index] - simplex_array[0]
            )
            values[index] = function(transform(simplex_array[index]))

    best = int(np.argmin(values))
    parameters = transform(simplex_array[best])
    return parameters, float(function(parameters))


def best_of_starts(
    function: Callable[[np.ndarray], float],
    starts: list[list[float]],
    bounds: list[tuple[float, float]],
) -> tuple[np.ndarray, float]:
    results = [bounded_nelder_mead(function, start, bounds) for start in starts]
    return min(results, key=lambda item: item[1])


def fit_general(likelihood: Likelihood) -> dict[str, float]:
    starts = [
        [0.318, 0.76, 0.229],
        [0.31, 0.20, 0.20],
        [0.32, 1.00, 0.25],
        [0.30, 0.05, 1.00],
        [0.33, 1.80, 1.00],
        [0.30, 0.50, 5.00],
    ]
    parameters, _ = best_of_starts(
        lambda value: likelihood.chi(*value),
        starts,
        [OMEGA_M_BOUNDS, NU_BOUNDS, A_POSITIVE_BOUNDS],
    )
    return likelihood.evaluate(*parameters)


def fit_fixed_canonical(
    likelihood: Likelihood, canonical: float
) -> dict[str, float]:
    def objective(value: np.ndarray) -> float:
        nu, a_crossing = value
        omega_m = omega_m_from_canonical_ratio(
            canonical, nu, a_crossing, likelihood.omega_r
        )
        return likelihood.chi(omega_m, nu, a_crossing)

    proposed_starts = [
        [0.76, 0.229],
        [0.20, 0.57],
        [0.30, 0.40],
        [0.45, 0.35],
        [1.00, 0.25],
        [1.80, 0.50],
        [0.05, 8.00],
    ]
    # At small R_c the feasible (nu,a_c) strip becomes narrow.  Seed it by
    # solving the algebraic closure for a_c at Omega_m=0.31 before running the
    # likelihood optimizer; otherwise a flat invalid simplex can masquerade as
    # a profile crossing.
    a_grid = np.geomspace(A_POSITIVE_BOUNDS[0], A_POSITIVE_BOUNDS[1], 120)
    for nu in np.geomspace(0.01, NU_BOUNDS[1], 18):
        previous_a = float(a_grid[0])
        previous_value = omega_m_from_canonical_ratio(
            canonical, float(nu), previous_a, likelihood.omega_r
        ) - 0.31
        for a_crossing in a_grid[1:]:
            current_a = float(a_crossing)
            current_value = omega_m_from_canonical_ratio(
                canonical, float(nu), current_a, likelihood.omega_r
            ) - 0.31
            if (
                math.isfinite(previous_value)
                and math.isfinite(current_value)
                and previous_value * current_value <= 0.0
            ):
                low_a, high_a = previous_a, current_a
                low_value = previous_value
                for _ in range(36):
                    middle_a = 0.5 * (low_a + high_a)
                    middle_value = omega_m_from_canonical_ratio(
                        canonical, float(nu), middle_a, likelihood.omega_r
                    ) - 0.31
                    if low_value * middle_value <= 0.0:
                        high_a = middle_a
                    else:
                        low_a, low_value = middle_a, middle_value
                proposed_starts.append(
                    [float(nu), 0.5 * (low_a + high_a)]
                )
            previous_a, previous_value = current_a, current_value

    feasible_starts = [
        start
        for start in proposed_starts
        if OMEGA_M_BOUNDS[0]
        <= omega_m_from_canonical_ratio(
            canonical, start[0], start[1], likelihood.omega_r
        )
        <= OMEGA_M_BOUNDS[1]
    ]
    unique_starts = {
        (round(start[0], 10), round(start[1], 10)): start
        for start in feasible_starts
    }
    starts = sorted(
        unique_starts.values(),
        key=lambda start: objective(np.asarray(start)),
    )[:8]
    if not starts:
        return {"chi_square": 1.0e50}
    parameters, _ = best_of_starts(
        objective, starts, [NU_BOUNDS, A_POSITIVE_BOUNDS]
    )
    nu, a_crossing = parameters
    omega_m = omega_m_from_canonical_ratio(
        canonical, nu, a_crossing, likelihood.omega_r
    )
    return likelihood.evaluate(omega_m, nu, a_crossing)


def fit_fixed_nu(likelihood: Likelihood, nu: float) -> dict[str, float]:
    starts = [
        [0.318, 0.229],
        [0.31, 0.02],
        [0.32, 0.40],
        [0.30, 2.00],
        [0.30, 8.00],
    ]
    parameters, _ = best_of_starts(
        lambda value: likelihood.chi(value[0], nu, value[1]),
        starts,
        [OMEGA_M_BOUNDS, A_POSITIVE_BOUNDS],
    )
    return likelihood.evaluate(parameters[0], nu, parameters[1])


def golden_minimum(
    function: Callable[[float], float], low: float, high: float
) -> tuple[float, float]:
    ratio = (math.sqrt(5.0) - 1.0) / 2.0
    left = high - ratio * (high - low)
    right = low + ratio * (high - low)
    f_left, f_right = function(left), function(right)
    for _ in range(55):
        if f_left < f_right:
            high, right, f_right = right, left, f_left
            left = high - ratio * (high - low)
            f_left = function(left)
        else:
            low, left, f_left = left, right, f_right
            right = low + ratio * (high - low)
            f_right = function(right)
    point = 0.5 * (low + high)
    return point, function(point)


def fit_fixed_pair(
    likelihood: Likelihood, canonical: float, nu: float
) -> dict[str, float]:
    grid = np.unique(
        np.concatenate(
            [
                np.geomspace(1.0e-8, 0.02, 24),
                np.geomspace(0.02, 0.30, 28),
                np.linspace(0.30, 2.0, 34),
                np.linspace(2.0, 10.0, 24),
            ]
        )
    )

    def objective(a_crossing: float) -> float:
        omega_m = omega_m_from_canonical_ratio(
            canonical, nu, a_crossing, likelihood.omega_r
        )
        return likelihood.chi(omega_m, nu, a_crossing)

    values = np.asarray([objective(float(value)) for value in grid])
    candidates: list[tuple[float, float]] = []
    for index in range(1, len(grid) - 1):
        if (
            values[index] <= values[index - 1]
            and values[index] <= values[index + 1]
            and values[index] < 1.0e40
        ):
            point, value = golden_minimum(
                objective, float(grid[index - 1]), float(grid[index + 1])
            )
            candidates.append((value, point))
    if not candidates:
        valid = np.flatnonzero(values < 1.0e40)
        if valid.size == 0:
            return {"chi_square": 1.0e50}
        index = int(valid[np.argmin(values[valid])])
        candidates.append((float(values[index]), float(grid[index])))
    _, a_crossing = min(candidates)
    omega_m = omega_m_from_canonical_ratio(
        canonical, nu, a_crossing, likelihood.omega_r
    )
    return likelihood.evaluate(omega_m, nu, a_crossing)


def profile_root(
    profile: Callable[[float], dict[str, float]],
    low: float,
    high: float,
    target: float,
    iterations: int = 12,
) -> float:
    low_value = float(profile(low)["chi_square"]) - target
    high_value = float(profile(high)["chi_square"]) - target
    if low_value * high_value > 0.0:
        raise ArithmeticError(
            f"profile target is not bracketed: {low}, {high}, "
            f"{low_value}, {high_value}"
        )
    for _ in range(iterations):
        middle = 0.5 * (low + high)
        middle_value = float(profile(middle)["chi_square"]) - target
        if low_value * middle_value <= 0.0:
            high, high_value = middle, middle_value
        else:
            low, low_value = middle, middle_value
    return 0.5 * (low + high)


def find_profile_bracket(
    profile: Callable[[float], dict[str, float]],
    best_parameter: float,
    target: float,
    domain: tuple[float, float],
    direction: int,
) -> tuple[float, float] | None:
    """Expand away from the profile minimum until a target is bracketed."""

    if direction not in (-1, 1):
        raise ValueError("profile-bracket direction must be -1 or +1")
    low, high = domain
    inside = min(max(best_parameter, low), high)
    inside_value = float(profile(inside)["chi_square"]) - target
    if inside_value > 1.0e-5:
        raise ArithmeticError(
            f"declared profile minimum lies above target: {inside_value}"
        )
    distance = max(1.0e-5, 0.01 * (high - low))
    for _ in range(40):
        outside = min(max(best_parameter + direction * distance, low), high)
        outside_value = float(profile(outside)["chi_square"]) - target
        if outside_value >= 0.0:
            return (
                (outside, inside) if direction < 0 else (inside, outside)
            )
        if outside == low or outside == high:
            return None
        inside, inside_value = outside, outside_value
        distance *= 1.6
    raise ArithmeticError("profile bracket expansion did not terminate")


def required_profile_endpoint(
    profile: Callable[[float], dict[str, float]],
    best_parameter: float,
    target: float,
    domain: tuple[float, float],
    direction: int,
) -> float:
    bracket = find_profile_bracket(
        profile, best_parameter, target, domain, direction
    )
    if bracket is None:
        side = "lower" if direction < 0 else "upper"
        raise ArithmeticError(
            f"required {side} profile endpoint is open on domain {domain}"
        )
    return profile_root(profile, bracket[0], bracket[1], target, iterations=16)


def constant_w_limit(likelihood: Likelihood) -> dict[str, float]:
    """R_c -> 0 positive-tail limit: rho_X/rho_X0=(1+z)^(2 nu)."""

    def evaluate(value: np.ndarray) -> float:
        omega_m, nu = value
        complement = 1.0 - omega_m - likelihood.omega_r

        def expansion(redshift: np.ndarray) -> np.ndarray:
            one_plus = 1.0 + redshift
            return np.sqrt(
                omega_m * one_plus**3
                + likelihood.omega_r * one_plus**4
                + complement * one_plus ** (2.0 * nu)
            )

        maximum_redshift = max(
            float(np.max(likelihood.pantheon.z_hd)),
            float(np.max(likelihood.bao.redshift)),
        )
        distance = BASE.comoving_distance_interpolator(expansion, maximum_redshift)
        residual = likelihood.pantheon.magnitude - 5.0 * np.log10(
            (1.0 + likelihood.pantheon.z_hel)
            * distance(likelihood.pantheon.z_hd)
        )
        offset = float(likelihood.pantheon.inverse_covariance_ones @ residual) / (
            likelihood.pantheon.ones_inverse_covariance_ones
        )
        residual -= offset
        sn_chi = float(
            residual @ likelihood.pantheon.inverse_covariance @ residual
        )
        e_value = expansion(likelihood.bao.redshift)
        chi_value = distance(likelihood.bao.redshift)
        shape = np.empty_like(likelihood.bao.value)
        for index, quantity in enumerate(likelihood.bao.quantity):
            if quantity == "DM_over_rs":
                shape[index] = chi_value[index]
            elif quantity == "DH_over_rs":
                shape[index] = 1.0 / e_value[index]
            else:
                shape[index] = (
                    likelihood.bao.redshift[index]
                    * chi_value[index] ** 2
                    / e_value[index]
                ) ** (1.0 / 3.0)
        inverse = likelihood.bao.inverse_covariance
        amplitude = float(shape @ inverse @ likelihood.bao.value) / float(
            shape @ inverse @ shape
        )
        bao_residual = likelihood.bao.value - amplitude * shape
        return sn_chi + float(bao_residual @ inverse @ bao_residual)

    parameters, chi_square = best_of_starts(
        evaluate,
        [[0.304, 0.10], [0.31, 0.02], [0.30, 0.30]],
        [OMEGA_M_BOUNDS, (0.001, 1.0)],
    )
    return {
        "chi_square": chi_square,
        "omega_m": float(parameters[0]),
        "nu": float(parameters[1]),
        "w_constant": -1.0 + 2.0 * float(parameters[1]) / 3.0,
        "meaning": "attainable limit as R_c tends to zero and a_crossing tends to positive infinity",
    }


def negative_reference_audit(likelihood: Likelihood) -> dict[str, float]:
    starts = [
        [0.306, 0.02, -1.0e-4],
        [0.31, 0.20, -0.20],
        [0.32, 1.00, -0.25],
        [0.30, 1.80, -1.00],
        [0.30, 0.10, -8.00],
    ]
    parameters, _ = best_of_starts(
        lambda value: likelihood.chi(*value),
        starts,
        [OMEGA_M_BOUNDS, NEGATIVE_AUDIT_NU_BOUNDS, NEGATIVE_AUDIT_A_BOUNDS],
    )
    return likelihood.evaluate(*parameters)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--bao-data-dir", type=Path, default=BASE.DEFAULT_BAO_DATA_DIR
    )
    parser.add_argument(
        "--pantheon-data-dir",
        type=Path,
        default=BASE.DEFAULT_PANTHEON_DATA_DIR,
    )
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--dataset",
        choices=("desi-dr2-bao-2025", "desi-dr2-lya-2026"),
        default="desi-dr2-lya-2026",
        help=(
            "released DESI DR2 BAO, or the provisional 2026 Ly-alpha "
            "published-Gaussian replacement used by the companion receipt"
        ),
    )
    parser.add_argument("--omega-r", type=float, default=9.15e-5)
    args = parser.parse_args()

    hashes = BASE.verify_sources(args.bao_data_dir, args.pantheon_data_dir)
    pantheon = BASE.load_pantheon(args.pantheon_data_dir)
    released_bao = BASE.load_bao(args.bao_data_dir)
    if args.dataset == "desi-dr2-bao-2025":
        bao = released_bao
        dataset_label = "2025 DESI DR2 BAO and Pantheon+"
        input_status = (
            "fully released DESI DR2 mean vector and covariance; "
            "released Pantheon+ data and covariance"
        )
    else:
        bao = BASE.with_2026_lya_full_shape(released_bao)
        dataset_label = (
            "2025 DESI DR2 galaxy BAO plus provisional 2026 Ly-alpha "
            "published-Gaussian replacement and Pantheon+"
        )
        input_status = (
            "released 2025 DESI galaxy BAO with its Ly-alpha block replaced "
            "by the transcribed 2026 Eq. 26 bivariate Gaussian; zero "
            "cross-covariance with the retained galaxy block is assumed"
        )
    likelihood = Likelihood(pantheon, bao, args.omega_r)

    unit_base = BASE.fit_model("cst-b2-unit", pantheon, bao, args.omega_r)["joint"]
    unit = likelihood.evaluate(
        float(unit_base["omega_m_best"]), 1.0, float(unit_base["x_crossing"])
    )
    fixed_canonical = fit_fixed_canonical(likelihood, 1.0)
    fixed_nu = fit_fixed_nu(likelihood, 1.0)
    general = fit_general(likelihood)

    fixed_pair_cache: dict[tuple[float, float], dict[str, float]] = {}
    fixed_nu_cache: dict[float, dict[str, float]] = {}
    fixed_canonical_cache: dict[float, dict[str, float]] = {}

    def fixed_pair_profile(canonical: float, nu: float) -> dict[str, float]:
        key = (round(canonical, 10), round(nu, 10))
        if key not in fixed_pair_cache:
            fixed_pair_cache[key] = fit_fixed_pair(likelihood, canonical, nu)
        return fixed_pair_cache[key]

    def nu_profile(nu: float) -> dict[str, float]:
        key = round(nu, 10)
        if key not in fixed_nu_cache:
            fixed_nu_cache[key] = fit_fixed_nu(likelihood, nu)
        return fixed_nu_cache[key]

    def canonical_profile(canonical: float) -> dict[str, float]:
        key = round(canonical, 10)
        if key not in fixed_canonical_cache:
            fixed_canonical_cache[key] = fit_fixed_canonical(likelihood, canonical)
        return fixed_canonical_cache[key]

    fixed_canonical_nu_profile = lambda nu: fixed_pair_profile(1.0, nu)
    fixed_nu_canonical_profile = lambda canonical: fixed_pair_profile(canonical, 1.0)

    canonical_domain = (1.0e-8, 2.0 - 1.0e-8)

    def required_interval(
        profile: Callable[[float], dict[str, float]],
        best_parameter: float,
        minimum_chi: float,
        delta_chi: float,
        domain: tuple[float, float],
    ) -> list[float]:
        target = minimum_chi + delta_chi
        return [
            required_profile_endpoint(
                profile, best_parameter, target, domain, -1
            ),
            required_profile_endpoint(
                profile, best_parameter, target, domain, 1
            ),
        ]

    nested_intervals = {
        "R_c_fixed_1_nu_profile": {
            "delta_chi2_1": required_interval(
                fixed_canonical_nu_profile,
                float(fixed_canonical["nu"]),
                float(fixed_canonical["chi_square"]),
                1.0,
                NU_BOUNDS,
            ),
            "delta_chi2_3_84": required_interval(
                fixed_canonical_nu_profile,
                float(fixed_canonical["nu"]),
                float(fixed_canonical["chi_square"]),
                3.84,
                NU_BOUNDS,
            ),
        },
        "nu_fixed_1_R_c_profile": {
            "delta_chi2_1": required_interval(
                fixed_nu_canonical_profile,
                float(fixed_nu["canonical_R_c"]),
                float(fixed_nu["chi_square"]),
                1.0,
                canonical_domain,
            ),
            "delta_chi2_3_84": required_interval(
                fixed_nu_canonical_profile,
                float(fixed_nu["canonical_R_c"]),
                float(fixed_nu["chi_square"]),
                3.84,
                canonical_domain,
            ),
        },
    }

    constant_limit = constant_w_limit(likelihood)
    general_minimum_chi = float(general["chi_square"])
    general_canonical_best = float(general["canonical_R_c"])

    def canonical_interval(delta_chi: float) -> dict[str, float | str | None]:
        target = general_minimum_chi + delta_chi
        lower_bracket = (
            None
            if float(constant_limit["chi_square"]) < target
            else find_profile_bracket(
                canonical_profile,
                general_canonical_best,
                target,
                canonical_domain,
                -1,
            )
        )
        lower = (
            None
            if lower_bracket is None
            else profile_root(
                canonical_profile,
                lower_bracket[0],
                lower_bracket[1],
                target,
                iterations=16,
            )
        )
        return {
            "lower": lower,
            "lower_status": (
                "open to R_c -> 0; the attainable constant-w tail remains "
                f"below the Delta-chi2={delta_chi:g} target"
                if lower is None
                else "finite profile crossing"
            ),
            "upper": required_profile_endpoint(
                canonical_profile,
                general_canonical_best,
                target,
                canonical_domain,
                1,
            ),
        }

    general_canonical_1_interval = canonical_interval(1.0)
    general_canonical_95_interval = canonical_interval(3.84)
    general_intervals = {
        "nu_profile": {
            "delta_chi2_1": required_interval(
                nu_profile,
                float(general["nu"]),
                general_minimum_chi,
                1.0,
                NU_BOUNDS,
            ),
            "delta_chi2_3_84": required_interval(
                nu_profile,
                float(general["nu"]),
                general_minimum_chi,
                3.84,
                NU_BOUNDS,
            ),
        },
        "R_c_profile": {
            "delta_chi2_1": general_canonical_1_interval,
            "delta_chi2_3_84": general_canonical_95_interval,
        },
    }

    negative = negative_reference_audit(likelihood)
    number_of_data = int(pantheon.z_hd.size + bao.value.size)
    unit_chi = float(unit["chi_square"])

    def comparison(entry: dict[str, float], added_parameters: int) -> dict[str, float]:
        chi_difference = float(entry["chi_square"]) - unit_chi
        return {
            "delta_chi2_from_unit": chi_difference,
            "delta_AIC_from_unit": chi_difference + 2.0 * added_parameters,
            "delta_BIC_from_unit": (
                chi_difference + math.log(number_of_data) * added_parameters
            ),
        }

    result = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "runtime": {
            "python": sys.version,
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
        "protocol": {
            "dataset_key": args.dataset,
            "dataset": dataset_label,
            "input_status": input_status,
            "pantheon_count": int(pantheon.z_hd.size),
            "desi_count": int(bao.value.size),
            "omega_r": args.omega_r,
            "profiled_nuisance": ["supernova offset", "c/(H0 r_d)"],
            "positive_branch_coordinates": ["Omega_m", "nu", "a_c=nu x_c > 0"],
            "domains": {
                "Omega_m": list(OMEGA_M_BOUNDS),
                "nu": list(NU_BOUNDS),
                "a_c_positive": list(A_POSITIVE_BOUNDS),
                "canonical_R_c": "derived without an artificial cutoff; 0 < R_c < 2",
                "negative_reference_audit_nu": list(NEGATIVE_AUDIT_NU_BOUNDS),
                "negative_reference_audit_a_c": list(NEGATIVE_AUDIT_A_BOUNDS),
            },
            "closure": (
                "[R_c/(2-R_c)] [Omega_m exp(3x_c)+Omega_r exp(4x_c)] "
                "sech^2(nu x_c) = 1-Omega_m-Omega_r"
            ),
            "root_parameterization": (
                "x_c labels root-background pairs exhaustively; R_c=2D/(D+F_nu(x_c))"
            ),
            "legacy_conversion": "historical r_c=R_c/(2-R_c); R_c=2r_c/(1+r_c)",
            "interval_meaning": (
                "one-dimensional Delta-chi-square profile-likelihood contours; "
                "not posterior credible intervals and not coverage-calibrated confidence intervals"
            ),
        },
        "source_sha256": hashes,
        "fits": {
            "frozen_unit": unit,
            "R_c_fixed_1_nu_free": fixed_canonical,
            "nu_fixed_1_R_c_free": fixed_nu,
            "nu_and_R_c_free": general,
        },
        "nested_profile_intervals": nested_intervals,
        "general_profile_intervals": general_intervals,
        "R_c_to_zero_attainable_limit": constant_limit,
        "negative_reference_audit": negative,
        "information_criteria_relative_to_frozen_unit": {
            "R_c_fixed_1_nu_free": comparison(fixed_canonical, 1),
            "nu_fixed_1_R_c_free": comparison(fixed_nu, 1),
            "nu_and_R_c_free": comparison(general, 2),
            "number_of_data_for_BIC": number_of_data,
        },
        "unity_profile_membership": {
            "R_c_fixed_1_nu_profile": {
                "inside_delta_chi2_1": (
                    nested_intervals["R_c_fixed_1_nu_profile"][
                        "delta_chi2_1"
                    ][0]
                    <= 1.0
                    <= nested_intervals["R_c_fixed_1_nu_profile"][
                        "delta_chi2_1"
                    ][1]
                ),
                "inside_delta_chi2_3_84": (
                    nested_intervals["R_c_fixed_1_nu_profile"][
                        "delta_chi2_3_84"
                    ][0]
                    <= 1.0
                    <= nested_intervals["R_c_fixed_1_nu_profile"][
                        "delta_chi2_3_84"
                    ][1]
                ),
            },
            "nu_fixed_1_R_c_profile": {
                "inside_delta_chi2_1": (
                    nested_intervals["nu_fixed_1_R_c_profile"][
                        "delta_chi2_1"
                    ][0]
                    <= 1.0
                    <= nested_intervals["nu_fixed_1_R_c_profile"][
                        "delta_chi2_1"
                    ][1]
                ),
                "inside_delta_chi2_3_84": (
                    nested_intervals["nu_fixed_1_R_c_profile"][
                        "delta_chi2_3_84"
                    ][0]
                    <= 1.0
                    <= nested_intervals["nu_fixed_1_R_c_profile"][
                        "delta_chi2_3_84"
                    ][1]
                ),
            },
            "joint_profile_nu_coordinate": {
                "inside_delta_chi2_1": (
                    general_intervals["nu_profile"]["delta_chi2_1"][0]
                    <= 1.0
                    <= general_intervals["nu_profile"]["delta_chi2_1"][1]
                ),
                "inside_delta_chi2_3_84": (
                    general_intervals["nu_profile"]["delta_chi2_3_84"][0]
                    <= 1.0
                    <= general_intervals["nu_profile"]["delta_chi2_3_84"][1]
                ),
            },
            "joint_profile_R_c_coordinate": {
                "inside_delta_chi2_1": (
                    (
                        general_canonical_1_interval["lower"] is None
                        or float(general_canonical_1_interval["lower"]) <= 1.0
                    )
                    and 1.0 <= float(general_canonical_1_interval["upper"])
                ),
                "inside_delta_chi2_3_84": (
                    (
                        general_canonical_95_interval["lower"] is None
                        or float(general_canonical_95_interval["lower"]) <= 1.0
                    )
                    and 1.0 <= float(general_canonical_95_interval["upper"])
                ),
            },
            "joint_two_parameter_point": {
                "delta_chi2_at_frozen_unit": unit_chi
                - float(general["chi_square"]),
                "inside_nominal_delta_chi2_2_30": (
                    unit_chi - float(general["chi_square"]) <= 2.30
                ),
                "inside_nominal_delta_chi2_5_99": (
                    unit_chi - float(general["chi_square"]) <= 5.99
                ),
            },
        },
        "branch_audit": {
            "exact_monotone_regime": (
                "for 0 < nu <= 3/2, F_nu is strictly increasing on x_c>0, "
                "so the positive closure root is unique when it exists"
            ),
            "confidence_region_branch_switch": False,
            "reason": (
                "all finite Delta-chi-square profile endpoints with material support "
                "have nu < 3/2"
            ),
            "negative_root_theorem": (
                "F_nu is strictly increasing on x_c<0; exactly one negative root "
                "exists iff R_c>2D"
            ),
        },
    }

    checks = {
        "unit_matches_base_receipt": abs(
            unit_chi - float(unit_base["chi_square"])
        ) < 1.0e-5,
        "nested_order": (
            float(general["chi_square"])
            <= float(fixed_canonical["chi_square"])
            <= unit_chi
            and float(general["chi_square"])
            <= float(fixed_nu["chi_square"])
            <= unit_chi
        ),
        "all_profile_intervals_ordered_around_their_minima": (
            nested_intervals["R_c_fixed_1_nu_profile"]["delta_chi2_1"][0]
            <= float(fixed_canonical["nu"])
            <= nested_intervals["R_c_fixed_1_nu_profile"]["delta_chi2_1"][1]
            and nested_intervals["nu_fixed_1_R_c_profile"]["delta_chi2_1"][0]
            <= float(fixed_nu["canonical_R_c"])
            <= nested_intervals["nu_fixed_1_R_c_profile"]["delta_chi2_1"][1]
            and general_intervals["nu_profile"]["delta_chi2_1"][0]
            <= float(general["nu"])
            <= general_intervals["nu_profile"]["delta_chi2_1"][1]
            and (
                general_canonical_1_interval["lower"] is None
                or float(general_canonical_1_interval["lower"])
                <= float(general["canonical_R_c"])
            )
            and float(general["canonical_R_c"])
            <= float(general_canonical_1_interval["upper"])
        ),
        "R_c_lower_profile_statuses_are_consistent": (
            (
                general_canonical_1_interval["lower"] is not None
                or float(constant_limit["chi_square"])
                < general_minimum_chi + 1.0
            )
            and (
                general_canonical_95_interval["lower"] is not None
                or float(constant_limit["chi_square"])
                < general_minimum_chi + 3.84
            )
        ),
        "negative_branch_not_competitive": (
            float(negative["chi_square"]) > unit_chi
        ),
        "all_finite_except_declared_open_or_tail_values": True,
    }
    if not all(checks.values()):
        raise AssertionError(f"generalized background checks failed: {checks}")
    result["checks"] = checks

    rendered = json.dumps(result, indent=2, allow_nan=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
