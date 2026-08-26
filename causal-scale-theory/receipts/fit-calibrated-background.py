#!/usr/bin/env python3
"""Cepheid-calibrated Pantheon+SH0ES background comparison.

This receipt reproduces the official Pantheon+SH0ES selection and calibrator
theory vector, then compares flat LambdaCDM with the frozen unit CST-B2
background on calibrated supernovae alone and on the fully released 2025 DESI
DR2 BAO plus calibrated-supernova likelihood.  It imports the shared expansion,
distance, BAO, source-verification, and one-dimensional optimization code from
fit-late-time-background.py rather than copying that implementation.

The supernova absolute magnitude is one common nuisance parameter across the
Cepheid-calibrator and Hubble-flow rows.  At fixed Omega_m its joint generalized
least-squares projection with the Hubble intercept yields H0.  DESI then yields
r_d through its separately profiled c/(H0 r_d) amplitude.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import platform
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

import numpy as np


sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
BASE_RECEIPT_PATH = HERE / "fit-late-time-background.py"
BASE_SPEC = importlib.util.spec_from_file_location(
    "cst_late_time_background_receipt_for_calibrated_fit", BASE_RECEIPT_PATH
)
if BASE_SPEC is None or BASE_SPEC.loader is None:
    raise ImportError(f"cannot load shared receipt from {BASE_RECEIPT_PATH}")
BASE = importlib.util.module_from_spec(BASE_SPEC)
sys.modules[BASE_SPEC.name] = BASE
BASE_SPEC.loader.exec_module(BASE)


MPC_IN_KM = 3.085_677_581_491_367e19
SECONDS_PER_GYR = 365.25 * 86_400.0 * 1.0e9
HUBBLE_TIME_GYR_AT_H0_ONE = MPC_IN_KM / SECONDS_PER_GYR
PROFILE_OMEGA_M_BOUNDS = (0.15, 0.50)
BROADER_SCAN_OMEGA_M_BOUNDS = (0.05, 0.80)
BROADER_SCAN_POINT_COUNT = 151

SOURCES = {
    filename: BASE.SOURCES[filename]
    for filename in (
        "desi_dr2_bao_mean.txt",
        "desi_dr2_bao_cov.txt",
        "Pantheon+SH0ES.dat",
        "Pantheon+SH0ES_STAT+SYS.cov",
    )
}

PRIMARY_SOURCES = {
    "official_likelihood_implementation": (
        "https://github.com/PantheonPlusSH0ES/DataRelease/blob/"
        "c447f0fea703fcd0fff57de5000947b5ca81286b/"
        "Pantheon%2B_Data/5_COSMOLOGY/cosmosis_likelihoods/"
        "Pantheon%2BSH0ES_cosmosis_likelihood.py"
    ),
    "official_likelihood_commit": "c447f0fea703fcd0fff57de5000947b5ca81286b",
    "official_likelihood_sha256": (
        "345fac3781a5cb930b95e91c1c07eb17dcf99b441703bb5e449477519240a59d"
    ),
    "pantheon_plus_cosmology": "https://doi.org/10.3847/1538-4357/ac8e04",
    "shoes_distance_ladder": "https://doi.org/10.3847/2041-8213/ac5c5b",
    "desi_dr2_results_ii": "https://doi.org/10.48550/arXiv.2503.14738",
    "planck_2018_parameters": "https://doi.org/10.1051/0004-6361/201833910",
    "valcin_globular_cluster_age": "https://arxiv.org/abs/2102.04486",
}


@dataclass
class CalibratedPantheonLikelihood:
    z_hd: np.ndarray
    z_hel: np.ndarray
    magnitude: np.ndarray
    is_calibrator: np.ndarray
    cepheid_distance_modulus: np.ndarray
    inverse_covariance: np.ndarray
    covariance_cholesky: np.ndarray


def verify_sources(data_dir: Path) -> dict[str, str]:
    hashes: dict[str, str] = {}
    for filename, metadata in SOURCES.items():
        path = data_dir / filename
        if not path.exists():
            raise FileNotFoundError(
                f"missing {path}; obtain the unmodified file from {metadata['url']}"
            )
        actual = BASE.sha256(path)
        expected = metadata["sha256"]
        if actual != expected:
            raise ValueError(f"SHA-256 mismatch for {path}: {actual} != {expected}")
        hashes[filename] = actual
    return hashes


def all_numeric_values_are_finite(value: object) -> bool:
    """Recursively reject non-finite real values before JSON serialization."""

    if isinstance(value, (float, np.floating)):
        return bool(np.isfinite(value))
    if isinstance(value, dict):
        return all(all_numeric_values_are_finite(item) for item in value.values())
    if isinstance(value, (list, tuple)):
        return all(all_numeric_values_are_finite(item) for item in value)
    return True


def load_calibrated_pantheon(
    data_dir: Path,
) -> tuple[CalibratedPantheonLikelihood, dict[str, object]]:
    table = np.genfromtxt(
        data_dir / "Pantheon+SH0ES.dat",
        names=True,
        dtype=None,
        encoding="utf-8",
    )
    z_hd_all = np.asarray(table["zHD"], dtype=float)
    z_hel_all = np.asarray(table["zHEL"], dtype=float)
    magnitude_all = np.asarray(table["m_b_corr"], dtype=float)
    calibrator_all = np.asarray(table["IS_CALIBRATOR"], dtype=bool)
    cepheid_all = np.asarray(table["CEPH_DIST"], dtype=float)

    # This is the OR selection in the collaboration likelihood, not the AND
    # selection used for the uncalibrated Hubble-diagram shape fit.
    keep = (z_hd_all > 0.01) | calibrator_all

    flat_covariance = np.loadtxt(data_dir / "Pantheon+SH0ES_STAT+SYS.cov")
    released_dimension = int(flat_covariance[0])
    values = flat_covariance[1:]
    if released_dimension != len(table) or values.size != released_dimension**2:
        raise ValueError("Pantheon+ table and covariance dimensions do not agree")
    covariance = values.reshape(released_dimension, released_dimension)
    covariance = covariance[np.ix_(keep, keep)]
    covariance = 0.5 * (covariance + covariance.T)
    covariance_cholesky = np.linalg.cholesky(covariance)
    inverse_covariance = np.linalg.inv(covariance)

    selected_calibrator = calibrator_all[keep]
    likelihood = CalibratedPantheonLikelihood(
        z_hd=z_hd_all[keep],
        z_hel=z_hel_all[keep],
        magnitude=magnitude_all[keep],
        is_calibrator=selected_calibrator,
        cepheid_distance_modulus=cepheid_all[keep],
        inverse_covariance=inverse_covariance,
        covariance_cholesky=covariance_cholesky,
    )
    metadata = {
        "released_row_count": int(len(table)),
        "selected_row_count": int(np.sum(keep)),
        "selected_calibrator_row_count": int(np.sum(selected_calibrator)),
        "selected_hubble_flow_row_count": int(np.sum(~selected_calibrator)),
        "excluded_low_redshift_noncalibrator_row_count": int(np.sum(~keep)),
        "selection": "(zHD > 0.01) OR bool(IS_CALIBRATOR)",
        "calibrator_theory": "CEPH_DIST distance modulus",
        "hubble_flow_theory": (
            "5 log10[(c/H0) (1+zHEL) chi(zHD)] + 25"
        ),
        "common_nuisance": (
            "one absolute magnitude M added to every selected row"
        ),
        "covariance": (
            "full selected statistical-plus-systematic covariance; "
            "symmetrized before Cholesky factorization"
        ),
    }
    return likelihood, metadata


def supernova_base_vector(
    likelihood: CalibratedPantheonLikelihood,
    model: str,
    omega_m: float,
    omega_r: float,
) -> np.ndarray:
    base = np.empty_like(likelihood.magnitude)
    base[likelihood.is_calibrator] = likelihood.cepheid_distance_modulus[
        likelihood.is_calibrator
    ]
    hubble = ~likelihood.is_calibrator
    expansion = BASE.expansion_function(model, omega_m, omega_r)
    distance = BASE.comoving_distance_interpolator(
        expansion, float(np.max(likelihood.z_hd[hubble]))
    )
    dimensionless_luminosity_distance = (
        (1.0 + likelihood.z_hel[hubble]) * distance(likelihood.z_hd[hubble])
    )
    base[hubble] = (
        5.0
        * np.log10(BASE.C_KM_S * dimensionless_luminosity_distance)
        + 25.0
    )
    return base


def profile_calibrated_supernova(
    likelihood: CalibratedPantheonLikelihood,
    model: str,
    omega_m: float,
    omega_r: float,
) -> dict[str, object]:
    """Profile the common M and Hubble intercept at fixed Omega_m.

    With base_i equal to CEPH_DIST for calibrators and to the Hubble-flow
    distance modulus before division by H0 otherwise,

        m_i - base_i = M + I_HF beta,   beta = -5 log10(H0).

    The two coefficients are therefore an exact generalized-least-squares
    projection.  The first coefficient is the one common magnitude nuisance;
    the second is re-expressed as the physical H0 parameter.
    """

    base = supernova_base_vector(likelihood, model, omega_m, omega_r)
    hubble_indicator = (~likelihood.is_calibrator).astype(float)
    design = np.column_stack((np.ones_like(hubble_indicator), hubble_indicator))
    inverse = likelihood.inverse_covariance
    normal = design.T @ inverse @ design
    right_hand_side = design.T @ inverse @ (likelihood.magnitude - base)
    magnitude, hubble_intercept = np.linalg.solve(normal, right_hand_side)
    h0 = 10.0 ** (-hubble_intercept / 5.0)
    residual = likelihood.magnitude - base - design @ np.asarray(
        [magnitude, hubble_intercept]
    )
    chi_square = float(residual @ inverse @ residual)
    nuisance_score = design.T @ inverse @ residual
    return {
        "chi_square": chi_square,
        "absolute_magnitude_M": float(magnitude),
        "hubble_intercept_minus_5_log10_H0": float(hubble_intercept),
        "H0_km_s_Mpc": float(h0),
        "profiled_nuisance_normal_equation_score": nuisance_score.tolist(),
        "maximum_absolute_profiled_nuisance_score": float(
            np.max(np.abs(nuisance_score))
        ),
        "residual": residual,
    }


def full_parameter_residuals(
    theta: np.ndarray,
    likelihood: CalibratedPantheonLikelihood,
    model: str,
    omega_r: float,
    bao: BASE.BaoLikelihood | None,
) -> tuple[np.ndarray, np.ndarray | None]:
    omega_m, log_h0, magnitude = map(float, theta[:3])
    h0 = math.exp(log_h0)
    expansion = BASE.expansion_function(model, omega_m, omega_r)

    sn_prediction = np.empty_like(likelihood.magnitude)
    calibrator = likelihood.is_calibrator
    sn_prediction[calibrator] = (
        likelihood.cepheid_distance_modulus[calibrator] + magnitude
    )
    hubble = ~calibrator
    distance = BASE.comoving_distance_interpolator(
        expansion,
        max(
            float(np.max(likelihood.z_hd[hubble])),
            0.0 if bao is None else float(np.max(bao.redshift)),
        ),
    )
    dimensionless_luminosity_distance = (
        (1.0 + likelihood.z_hel[hubble]) * distance(likelihood.z_hd[hubble])
    )
    sn_prediction[hubble] = (
        5.0
        * np.log10(
            BASE.C_KM_S * dimensionless_luminosity_distance / h0
        )
        + 25.0
        + magnitude
    )
    sn_residual = likelihood.magnitude - sn_prediction

    if bao is None:
        return sn_residual, None
    rd_mpc = math.exp(float(theta[3]))
    bao_shape = BASE.bao_shape_vector(bao, model, omega_m, omega_r)
    bao_amplitude = BASE.C_KM_S / (h0 * rd_mpc)
    bao_residual = bao.value - bao_amplitude * bao_shape
    return sn_residual, bao_residual


def full_parameter_half_chi_square(
    theta: np.ndarray,
    likelihood: CalibratedPantheonLikelihood,
    model: str,
    omega_r: float,
    bao: BASE.BaoLikelihood | None,
) -> float:
    sn_residual, bao_residual = full_parameter_residuals(
        theta, likelihood, model, omega_r, bao
    )
    chi_square = float(
        sn_residual @ likelihood.inverse_covariance @ sn_residual
    )
    if bao is not None and bao_residual is not None:
        chi_square += float(bao_residual @ bao.inverse_covariance @ bao_residual)
    return 0.5 * chi_square


def numerical_hessian(
    function: Callable[[np.ndarray], float],
    point: np.ndarray,
    steps: np.ndarray,
) -> np.ndarray:
    dimension = point.size
    hessian = np.empty((dimension, dimension))
    center = function(point)
    for i in range(dimension):
        delta = np.zeros(dimension)
        delta[i] = steps[i]
        hessian[i, i] = (
            function(point + delta) - 2.0 * center + function(point - delta)
        ) / steps[i] ** 2
        for j in range(i):
            delta_j = np.zeros(dimension)
            delta_j[j] = steps[j]
            mixed = (
                function(point + delta + delta_j)
                - function(point + delta - delta_j)
                - function(point - delta + delta_j)
                + function(point - delta - delta_j)
            ) / (4.0 * steps[i] * steps[j])
            hessian[i, j] = mixed
            hessian[j, i] = mixed
    return 0.5 * (hessian + hessian.T)


def dimensionless_age(model: str, omega_m: float, omega_r: float) -> float:
    """Return H0 t0 by a declared high-redshift extension of E(z).

    For CST-B2 this extrapolates the homogeneous ansatz far beyond the fitted
    z <= 2.33 domain.  The resulting age is therefore a conditional diagnostic,
    not a direct consequence of a constructed early-universe completion.
    """

    y = np.linspace(0.0, 35.0, 280_001)
    z = np.expm1(y)
    expansion = BASE.expansion_function(model, omega_m, omega_r)
    integrand = 1.0 / expansion(z)
    return float(
        np.sum(0.5 * (integrand[1:] + integrand[:-1]) * np.diff(y))
    )


def derived_quantities(
    theta: np.ndarray,
    model: str,
    omega_r: float,
    include_rd: bool,
) -> dict[str, float]:
    omega_m = float(theta[0])
    h0 = math.exp(float(theta[1]))
    h0_t0 = dimensionless_age(model, omega_m, omega_r)
    result = {
        "Omega_m": omega_m,
        "H0_km_s_Mpc": h0,
        "absolute_magnitude_M": float(theta[2]),
        "H0_t0": h0_t0,
        "age_Gyr": h0_t0 * HUBBLE_TIME_GYR_AT_H0_ONE / h0,
    }
    if include_rd:
        rd_mpc = math.exp(float(theta[3]))
        result["r_d_Mpc"] = rd_mpc
        result["r_d_h_Mpc"] = rd_mpc * h0 / 100.0
    return result


def scalar_gradient(
    function: Callable[[np.ndarray], float],
    point: np.ndarray,
    steps: np.ndarray,
) -> np.ndarray:
    gradient = np.empty_like(point)
    for index, step in enumerate(steps):
        delta = np.zeros_like(point)
        delta[index] = step
        gradient[index] = (
            function(point + delta) - function(point - delta)
        ) / (2.0 * step)
    return gradient


def propagated_scalar(
    name: str,
    function: Callable[[np.ndarray], float],
    point: np.ndarray,
    covariance: np.ndarray,
    steps: np.ndarray,
) -> dict[str, float | str]:
    gradient = scalar_gradient(function, point, steps)
    variance = float(gradient @ covariance @ gradient)
    if variance <= 0.0:
        raise ArithmeticError(f"non-positive propagated variance for {name}")
    return {
        "quantity": name,
        "value": float(function(point)),
        "local_hessian_sigma": math.sqrt(variance),
        "propagation": "gradient transpose times covariance times gradient",
    }


def local_hessian_summary(
    point: np.ndarray,
    likelihood: CalibratedPantheonLikelihood,
    model: str,
    omega_r: float,
    bao: BASE.BaoLikelihood | None,
) -> dict[str, object]:
    include_rd = bao is not None
    parameter_order = ["Omega_m", "ln_H0", "absolute_magnitude_M"]
    if include_rd:
        parameter_order.append("ln_r_d")
    steps = np.asarray([5.0e-4] * len(parameter_order))

    objective = lambda theta: full_parameter_half_chi_square(
        theta, likelihood, model, omega_r, bao
    )
    hessian = numerical_hessian(objective, point, steps)
    half_step_hessian = numerical_hessian(objective, point, 0.5 * steps)
    covariance = np.linalg.inv(hessian)
    half_step_covariance = np.linalg.inv(half_step_hessian)
    if np.any(np.linalg.eigvalsh(hessian) <= 0.0):
        raise ArithmeticError("local observed Hessian is not positive definite")
    sigma = np.sqrt(np.diag(covariance))
    half_step_sigma = np.sqrt(np.diag(half_step_covariance))
    relative_sigma_change = np.abs(half_step_sigma / sigma - 1.0)

    derived = derived_quantities(point, model, omega_r, include_rd)
    propagated: dict[str, object] = {
        "H0_km_s_Mpc": propagated_scalar(
            "H0 [km s^-1 Mpc^-1]",
            lambda theta: math.exp(float(theta[1])),
            point,
            covariance,
            steps,
        ),
        "age_Gyr": propagated_scalar(
            "t0 [Gyr]",
            lambda theta: derived_quantities(
                theta, model, omega_r, include_rd
            )["age_Gyr"],
            point,
            covariance,
            steps,
        ),
    }
    if include_rd:
        propagated["r_d_Mpc"] = propagated_scalar(
            "r_d [Mpc]",
            lambda theta: math.exp(float(theta[3])),
            point,
            covariance,
            steps,
        )
        propagated["r_d_h_Mpc"] = propagated_scalar(
            "r_d h [Mpc]",
            lambda theta: (
                math.exp(float(theta[1]) + float(theta[3])) / 100.0
            ),
            point,
            covariance,
            steps,
        )

    return {
        "method": (
            "inverse numerical Hessian of -ln L = chi_square/2 in the full "
            "parameter space, including the common magnitude nuisance"
        ),
        "parameter_order": parameter_order,
        "finite_difference_steps": steps.tolist(),
        "hessian": hessian.tolist(),
        "covariance": covariance.tolist(),
        "parameter_sigma_in_native_coordinates": sigma.tolist(),
        "maximum_relative_sigma_change_when_steps_halved": float(
            np.max(relative_sigma_change)
        ),
        "positive_definite": True,
        "derived_central_values": derived,
        "propagated": propagated,
        "qualification": (
            "local Gaussian/observed-Hessian approximation; not a posterior "
            "credible interval or coverage-calibrated confidence interval"
        ),
    }


def whitened_diagnostics(
    sn_residual: np.ndarray,
    sn_cholesky: np.ndarray,
    fitted_parameter_count: int,
    bao_residual: np.ndarray | None = None,
    bao_cholesky: np.ndarray | None = None,
) -> dict[str, object]:
    sn_whitened = np.linalg.solve(sn_cholesky, sn_residual)
    components = [sn_whitened]
    component_chi_square: dict[str, float] = {
        "calibrated_supernova": float(sn_whitened @ sn_whitened)
    }
    if bao_residual is not None:
        if bao_cholesky is None:
            raise ValueError("BAO residual supplied without a Cholesky factor")
        bao_whitened = np.linalg.solve(bao_cholesky, bao_residual)
        components.append(bao_whitened)
        component_chi_square["desi_dr2_bao"] = float(
            bao_whitened @ bao_whitened
        )
    whitened = np.concatenate(components)
    chi_square = float(whitened @ whitened)
    data_rank = int(whitened.size)
    nominal_dof = data_rank - fitted_parameter_count
    absolute = np.abs(whitened)
    return {
        "data_vector_length_and_covariance_rank": data_rank,
        "fitted_parameter_count": fitted_parameter_count,
        "nominal_degrees_of_freedom": nominal_dof,
        "chi_square_from_cholesky_whitened_residuals": chi_square,
        "component_chi_square": component_chi_square,
        "nominal_reduced_chi_square": chi_square / nominal_dof,
        "whitened_residual_rms_per_nominal_dof": math.sqrt(
            chi_square / nominal_dof
        ),
        "whitened_residual_mean": float(np.mean(whitened)),
        "whitened_residual_standard_deviation": float(np.std(whitened)),
        "maximum_absolute_cholesky_whitened_residual": float(np.max(absolute)),
        "absolute_whitened_residual_quantiles": {
            "p50": float(np.quantile(absolute, 0.50)),
            "p90": float(np.quantile(absolute, 0.90)),
            "p95": float(np.quantile(absolute, 0.95)),
            "p99": float(np.quantile(absolute, 0.99)),
        },
        "absolute_whitened_residual_counts": {
            "greater_than_2": int(np.sum(absolute > 2.0)),
            "greater_than_3": int(np.sum(absolute > 3.0)),
            "greater_than_4": int(np.sum(absolute > 4.0)),
        },
        "covariance_positive_definite": True,
        "qualification": (
            "nominal Gaussian diagnostic; individual Cholesky-whitened "
            "coordinates depend on the released row ordering, and the "
            "diagnostic is not a systematics coverage calibration"
        ),
    }


def fit_model(
    model: str,
    likelihood: CalibratedPantheonLikelihood,
    bao: BASE.BaoLikelihood,
    omega_r: float,
) -> dict[str, object]:
    sn_cache: dict[float, dict[str, object]] = {}
    bao_cache: dict[float, tuple[float, float, float]] = {}

    def supernova(omega_m: float) -> dict[str, object]:
        key = round(float(omega_m), 12)
        if key not in sn_cache:
            sn_cache[key] = profile_calibrated_supernova(
                likelihood, model, float(omega_m), omega_r
            )
        return sn_cache[key]

    def bao_only(omega_m: float) -> tuple[float, float, float]:
        key = round(float(omega_m), 12)
        if key not in bao_cache:
            bao_cache[key] = BASE.bao_chi_square(
                bao, model, float(omega_m), omega_r
            )
        return bao_cache[key]

    objectives = {
        "calibrated_supernova_only": lambda omega: float(
            supernova(omega)["chi_square"]
        ),
        "released_2025_desi_plus_calibrated_supernova": lambda omega: (
            float(supernova(omega)["chi_square"]) + bao_only(omega)[0]
        ),
    }
    result: dict[str, object] = {}
    for dataset, objective in objectives.items():
        omega_best, chi_square = BASE.golden_minimum(
            objective,
            low=PROFILE_OMEGA_M_BOUNDS[0],
            high=PROFILE_OMEGA_M_BOUNDS[1],
        )
        omega_interval = BASE.delta_one_interval(
            objective,
            omega_best,
            chi_square,
            low_bound=PROFILE_OMEGA_M_BOUNDS[0],
            high_bound=PROFILE_OMEGA_M_BOUNDS[1],
        )
        scan_omega = np.linspace(
            BROADER_SCAN_OMEGA_M_BOUNDS[0],
            BROADER_SCAN_OMEGA_M_BOUNDS[1],
            BROADER_SCAN_POINT_COUNT,
        )
        scan_chi_square = np.asarray(
            [objective(float(omega)) for omega in scan_omega]
        )
        scan_minimum_index = int(np.argmin(scan_chi_square))
        sn_result = supernova(omega_best)
        h0 = float(sn_result["H0_km_s_Mpc"])
        is_joint = dataset.startswith("released_2025")
        bao_result = bao_only(omega_best) if is_joint else None
        rd_mpc = None
        if bao_result is not None:
            rd_mpc = 100.0 * bao_result[2] / h0

        theta_values = [
            omega_best,
            math.log(h0),
            float(sn_result["absolute_magnitude_M"]),
        ]
        if rd_mpc is not None:
            theta_values.append(math.log(rd_mpc))
        theta = np.asarray(theta_values)

        sn_residual, bao_residual = full_parameter_residuals(
            theta,
            likelihood,
            model,
            omega_r,
            bao if is_joint else None,
        )
        hessian = local_hessian_summary(
            theta,
            likelihood,
            model,
            omega_r,
            bao if is_joint else None,
        )
        goodness = whitened_diagnostics(
            sn_residual,
            likelihood.covariance_cholesky,
            fitted_parameter_count=4 if is_joint else 3,
            bao_residual=bao_residual,
            bao_cholesky=bao.covariance_cholesky if is_joint else None,
        )
        if abs(
            float(goodness["chi_square_from_cholesky_whitened_residuals"])
            - chi_square
        ) > 1.0e-5:
            raise ArithmeticError(
                "whitened residual norm does not reproduce profiled chi-square"
            )

        entry: dict[str, object] = {
            "Omega_m_best": omega_best,
            "Omega_m_profile_delta_chi2_1": list(omega_interval),
            "H0_km_s_Mpc": h0,
            "absolute_magnitude_M": float(sn_result["absolute_magnitude_M"]),
            "chi_square": chi_square,
            "search_audit": {
                "optimizer_bounds_Omega_m": list(PROFILE_OMEGA_M_BOUNDS),
                "best_fit_is_strictly_interior": bool(
                    PROFILE_OMEGA_M_BOUNDS[0]
                    < omega_best
                    < PROFILE_OMEGA_M_BOUNDS[1]
                ),
                "broader_scan_bounds_Omega_m": list(
                    BROADER_SCAN_OMEGA_M_BOUNDS
                ),
                "broader_scan_point_count": BROADER_SCAN_POINT_COUNT,
                "broader_scan_minimum_Omega_m": float(
                    scan_omega[scan_minimum_index]
                ),
                "broader_scan_minimum_chi_square": float(
                    scan_chi_square[scan_minimum_index]
                ),
                "optimized_chi_square_not_above_any_broader_scan_point": bool(
                    chi_square <= float(np.min(scan_chi_square)) + 1.0e-7
                ),
                "qualification": (
                    "the scan is a nonconvexity/boundary check, not a proof "
                    "over the full physical parameter domain"
                ),
            },
            "maximum_absolute_profiled_sn_nuisance_score": float(
                sn_result["maximum_absolute_profiled_nuisance_score"]
            ),
            "local_hessian": hessian,
            "goodness_of_fit": goodness,
        }
        if bao_result is not None and rd_mpc is not None:
            bao_shape = BASE.bao_shape_vector(
                bao, model, omega_best, omega_r
            )
            bao_residual_at_profile = bao.value - bao_result[1] * bao_shape
            bao_amplitude_score = float(
                bao_shape @ bao.inverse_covariance @ bao_residual_at_profile
            )
            entry.update(
                {
                    "chi_square_calibrated_supernova": float(
                        sn_result["chi_square"]
                    ),
                    "chi_square_desi_dr2_bao": bao_result[0],
                    "bao_profile_amplitude_c_over_H0rd": bao_result[1],
                    "profiled_bao_amplitude_normal_equation_score": (
                        bao_amplitude_score
                    ),
                    "r_d_h_Mpc": bao_result[2],
                    "r_d_Mpc": rd_mpc,
                }
            )
        if model == "cst-b2-unit":
            x_crossing = BASE.crossing_offset(omega_best, omega_r)
            entry["x_crossing"] = x_crossing
            entry["z_crossing"] = math.exp(x_crossing) - 1.0
        result[dataset] = entry
    return result


def add_external_reference_comparisons(
    models: dict[str, dict[str, object]],
) -> dict[str, object]:
    planck_rd = 147.09
    planck_rd_sigma = 0.26
    valcin_age = 13.5
    valcin_age_sigma = 0.27
    result: dict[str, object] = {
        "references": {
            "planck_base_lcdm": {
                "r_d_Mpc": planck_rd,
                "sigma_Mpc": planck_rd_sigma,
                "source": PRIMARY_SOURCES["planck_2018_parameters"],
                "published_location": "Table 1",
                "likelihood_combination": (
                    "default Plik TT,TE,EE+lowE+lensing base-LambdaCDM"
                ),
                "statistic": "marginalized mean and 68 percent interval",
                "qualification": (
                    "Planck base-LambdaCDM posterior parameter, not a "
                    "model-neutral sound-horizon measurement"
                ),
            },
            "valcin_globular_cluster_chronometry": {
                "age_Gyr": valcin_age,
                "sigma_Gyr": valcin_age_sigma,
                "source": PRIMARY_SOURCES["valcin_globular_cluster_age"],
                "qualification": (
                    "stellar-evolution, distance, abundance, and cluster-formation "
                    "inference; comparatively cosmology-insensitive, not "
                    "assumption-free or strictly model-neutral"
                ),
            },
        },
        "models": {},
    }
    for model, datasets in models.items():
        model_result: dict[str, object] = {}
        for dataset, fit in datasets.items():
            propagated = fit["local_hessian"]["propagated"]
            age = float(propagated["age_Gyr"]["value"])
            age_sigma = float(propagated["age_Gyr"]["local_hessian_sigma"])
            age_difference = age - valcin_age
            dataset_result: dict[str, object] = {
                "globular_cluster_age_comparison": {
                    "fit_age_Gyr": age,
                    "fit_local_hessian_sigma_Gyr": age_sigma,
                    "difference_fit_minus_reference_Gyr": age_difference,
                    "combined_independent_Gaussian_sigma_Gyr": math.hypot(
                        age_sigma, valcin_age_sigma
                    ),
                    "absolute_difference_in_combined_sigma": abs(age_difference)
                    / math.hypot(age_sigma, valcin_age_sigma),
                    "qualification": (
                        "conditional local-Gaussian comparison treating the fit "
                        "and quoted stellar-age error as independent; the fitted "
                        "age also extrapolates the declared background E(z) to "
                        "y=35 at fixed Omega_r"
                    ),
                }
            }
            if "r_d_Mpc" in propagated:
                rd = float(propagated["r_d_Mpc"]["value"])
                rd_sigma = float(
                    propagated["r_d_Mpc"]["local_hessian_sigma"]
                )
                rd_difference = rd - planck_rd
                dataset_result["planck_sound_horizon_comparison"] = {
                    "fit_r_d_Mpc": rd,
                    "fit_local_hessian_sigma_Mpc": rd_sigma,
                    "difference_fit_minus_reference_Mpc": rd_difference,
                    "absolute_difference_in_fit_sigma": abs(rd_difference)
                    / rd_sigma,
                    "combined_independent_Gaussian_sigma_Mpc": math.hypot(
                        rd_sigma, planck_rd_sigma
                    ),
                    "absolute_difference_in_combined_sigma": abs(rd_difference)
                    / math.hypot(rd_sigma, planck_rd_sigma),
                    "qualification": (
                        "conditional comparison to an early-universe sound "
                        "horizon inferred inside Planck base-LambdaCDM; it is "
                        "not a model-neutral CST likelihood"
                    ),
                }
            model_result[dataset] = dataset_result
        result["models"][model] = model_result
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--omega-r", type=float, default=9.15e-5)
    args = parser.parse_args()

    source_hashes = verify_sources(args.data_dir)
    likelihood, likelihood_metadata = load_calibrated_pantheon(args.data_dir)
    bao = BASE.load_bao(args.data_dir)

    # The collaboration's low-redshift flat-LambdaCDM validation carrier does
    # not need the fixed radiation term used in the project's common late-time
    # comparison.  Keeping this as a separate parity fit makes the tiny
    # convention difference auditable rather than silently absorbing it.
    validation_omega_m, validation_chi_square = BASE.golden_minimum(
        lambda omega: float(
            profile_calibrated_supernova(
                likelihood, "lcdm", float(omega), 0.0
            )["chi_square"]
        )
    )
    validation_sn = profile_calibrated_supernova(
        likelihood, "lcdm", validation_omega_m, 0.0
    )

    models = {
        model: fit_model(model, likelihood, bao, args.omega_r)
        for model in ("lcdm", "cst-b2-unit")
    }

    sn_name = "calibrated_supernova_only"
    joint_name = "released_2025_desi_plus_calibrated_supernova"
    deltas = {
        "calibrated_supernova_only_delta_chi_square_cst_minus_lcdm": (
            models["cst-b2-unit"][sn_name]["chi_square"]
            - models["lcdm"][sn_name]["chi_square"]
        ),
        "released_2025_joint_delta_chi_square_cst_minus_lcdm": (
            models["cst-b2-unit"][joint_name]["chi_square"]
            - models["lcdm"][joint_name]["chi_square"]
        ),
        "equal_parameter_count_within_each_dataset": True,
    }

    lcdm_sn = models["lcdm"][sn_name]
    published = {
        "flat_LambdaCDM_Pantheon_plus_SH0ES": {
            "Omega_m": 0.334,
            "Omega_m_sigma": 0.018,
            "H0_km_s_Mpc": 73.6,
            "H0_sigma_km_s_Mpc": 1.1,
            "source": PRIMARY_SOURCES["pantheon_plus_cosmology"],
            "statistic_type": "published marginalized 68 percent constraints",
        },
        "receipt_maximum_likelihood": {
            "Omega_m": validation_omega_m,
            "H0_km_s_Mpc": validation_sn["H0_km_s_Mpc"],
            "absolute_magnitude_M": validation_sn["absolute_magnitude_M"],
            "chi_square": validation_chi_square,
            "omega_r": 0.0,
            "statistic_type": (
                "maximum-likelihood quadratic using the official compact "
                "selection and covariance"
            ),
        },
        "difference_in_published_sigma": {
            "Omega_m": (
                (validation_omega_m - 0.334) / 0.018
            ),
            "H0": (
                (float(validation_sn["H0_km_s_Mpc"]) - 73.6) / 1.1
            ),
        },
        "qualification": (
            "the paper quotes marginalized constraints, whereas the receipt "
            "reports a maximum-likelihood point; agreement is therefore tested "
            "against the quoted uncertainty rather than decimal identity; the "
            "paper does not tabulate an absolute chi-square for this row"
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
            "role": (
                "separately executable calibrated-supernova robustness test "
                "of the homogeneous background law; not statistically "
                "independent of the Pantheon+ shape receipt"
            ),
            "models": ["flat LambdaCDM", "frozen unit CST-B2"],
            "omega_r": args.omega_r,
            "datasets": [
                "official Pantheon+SH0ES calibrated likelihood",
                "fully released 2025 DESI DR2 Gaussian BAO likelihood",
            ],
            "selection_and_theory": likelihood_metadata,
            "fitted_parameters": {
                "calibrated_supernova_only": [
                    "Omega_m",
                    "H0",
                    "one common absolute magnitude M",
                ],
                "joint": [
                    "Omega_m",
                    "H0",
                    "one common absolute magnitude M",
                    "r_d (equivalently the BAO amplitude c/(H0 r_d))",
                ],
            },
            "likelihood_normalization": (
                "reported chi-square is the parameter-dependent quadratic only; "
                "the Gaussian log-determinant and 2pi constant are common to "
                "both models and cancel exactly in every delta chi-square"
            ),
            "Omega_m_search": {
                "optimizer_bounds": list(PROFILE_OMEGA_M_BOUNDS),
                "broader_scan_bounds": list(BROADER_SCAN_OMEGA_M_BOUNDS),
                "broader_scan_point_count": BROADER_SCAN_POINT_COUNT,
            },
            "age_extension": {
                "integration_variable": "y = ln(1+z)",
                "integration_bounds": [0.0, 35.0],
                "omega_r": args.omega_r,
                "qualification": (
                    "conditional extension of each homogeneous E(z) far beyond "
                    "the z <= 2.33 fit domain; for CST-B2 this is not an "
                    "early-universe construction"
                ),
            },
            "primary_sources": PRIMARY_SOURCES,
        },
        "source_sha256": source_hashes,
        "official_flat_lcdm_validation": published,
        "models": models,
        "comparisons": deltas,
        "external_reference_comparisons": add_external_reference_comparisons(
            models
        ),
    }

    all_goodness = [
        models[model][dataset]["goodness_of_fit"]
        for model in models
        for dataset in (sn_name, joint_name)
    ]
    all_hessians = [
        models[model][dataset]["local_hessian"]
        for model in models
        for dataset in (sn_name, joint_name)
    ]
    result["checks"] = {
        "selected_count_is_1657": likelihood.z_hd.size == 1657,
        "calibrator_count_is_77": int(np.sum(likelihood.is_calibrator)) == 77,
        "hubble_flow_count_is_1580": int(np.sum(~likelihood.is_calibrator))
        == 1580,
        "desi_bao_count_is_13": bao.redshift.size == 13,
        "all_covariances_positive_definite": bool(
            np.all(np.diag(likelihood.covariance_cholesky) > 0.0)
            and np.all(np.diag(bao.covariance_cholesky) > 0.0)
        ),
        "all_whitened_norms_reproduce_chi_square": all(
            abs(
                float(goodness["chi_square_from_cholesky_whitened_residuals"])
                - float(
                    models[model][dataset]["chi_square"]
                )
            )
            < 1.0e-5
            for goodness, (model, dataset) in zip(
                all_goodness,
                (
                    (model, dataset)
                    for model in models
                    for dataset in (sn_name, joint_name)
                ),
            )
        ),
        "all_local_hessians_positive_definite": all(
            bool(summary["positive_definite"]) for summary in all_hessians
        ),
        "all_local_hessian_sigmas_stable_to_step_halving": all(
            float(summary["maximum_relative_sigma_change_when_steps_halved"])
            < 0.03
            for summary in all_hessians
        ),
        "all_profiled_nuisance_scores_vanish": all(
            abs(
                float(
                    models[model][dataset][
                        "maximum_absolute_profiled_sn_nuisance_score"
                    ]
                )
            )
            < 1.0e-5
            and (
                dataset == sn_name
                or abs(
                    float(
                        models[model][dataset][
                            "profiled_bao_amplitude_normal_equation_score"
                        ]
                    )
                )
                < 1.0e-5
            )
            for model in models
            for dataset in (sn_name, joint_name)
        ),
        "all_profiled_minima_are_interior_and_pass_broader_scan": all(
            bool(
                models[model][dataset]["search_audit"][
                    "best_fit_is_strictly_interior"
                ]
            )
            and bool(
                models[model][dataset]["search_audit"][
                    "optimized_chi_square_not_above_any_broader_scan_point"
                ]
            )
            for model in models
            for dataset in (sn_name, joint_name)
        ),
        "published_lcdm_Omega_m_reproduced": abs(
            validation_omega_m - 0.334
        )
        < 0.003,
        "published_lcdm_H0_reproduced": abs(
            float(validation_sn["H0_km_s_Mpc"]) - 73.6
        )
        < 0.2,
        "displayed_chi_squares_are_finite": bool(
            np.isfinite(
                [
                    models[model][dataset]["chi_square"]
                    for model in models
                    for dataset in (sn_name, joint_name)
                ]
            ).all()
        ),
    }
    result["checks"]["all_numeric_ledger_values_are_finite"] = (
        all_numeric_values_are_finite(result)
    )
    if not all(result["checks"].values()):
        raise ArithmeticError(f"one or more validation checks failed: {result['checks']}")

    rendered = json.dumps(result, indent=2, allow_nan=False) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
