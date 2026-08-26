#!/usr/bin/env python3
"""Direct DESI DR2 BAO + Pantheon+ background comparison.

This receipt compares flat LambdaCDM with the frozen unit CST-B2 expansion
history.  Both models fit the same ordinary-sector parameter, Omega_m.  The
BAO scale c/(H0 r_d) and the supernova magnitude/H0 offset are profiled out
analytically, so neither H0, r_d, nor an absolute supernova calibration is
imported into the shape comparison.

The four late-time source files and the optional Planck chain archive are
unmodified public-release products. Pass their directories with --data-dir
and, for the acoustic stress tests, --planck-chain-dir. The expected late-time
filenames are listed in SOURCES.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

import numpy as np


C_KM_S = 299_792.458

SOURCES = {
    "desi_dr2_bao_mean.txt": {
        "url": "https://raw.githubusercontent.com/CobayaSampler/bao_data/master/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_mean.txt",
        "sha256": "9ac154ab583ce759c0f7eef3c978c7c70a6ead2d18774caceadf1a350a640585",
    },
    "desi_dr2_bao_cov.txt": {
        "url": "https://raw.githubusercontent.com/CobayaSampler/bao_data/master/desi_bao_dr2/desi_gaussian_bao_ALL_GCcomb_cov.txt",
        "sha256": "252a143274c8a07c78694c119617d36594f6d7965d00319ca611c6ffb886e509",
    },
    "Pantheon+SH0ES.dat": {
        "url": "https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/Pantheon%2BSH0ES.dat",
        "sha256": "1cb0fc379ef066afdc2ffd1857681cc478024570d8a3eba284fb645775198cf8",
    },
    "Pantheon+SH0ES_STAT+SYS.cov": {
        "url": "https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/Pantheon%2BSH0ES_STAT%2BSYS.cov",
        "sha256": "abf806d966485e64afdb359c87bffc0ecc00d05eff0a31ced66f247385df0fdc",
    },
}

PLANCK_ARCHIVE = {
    "filename": "COM_CosmoParams_base-plikHM-TTTEEE-lowl-lowE_R3.00.zip",
    "url": (
        "https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/"
        "cosmoparams/COM_CosmoParams_base-plikHM-TTTEEE-lowl-lowE_R3.00.zip"
    ),
    "sha256": "52cf6793f14e250ffc1436ce7f6fe6d92f6a066c433ec9efc66e4178f3d45a1f",
}


@dataclass
class PantheonLikelihood:
    z_hd: np.ndarray
    z_hel: np.ndarray
    magnitude: np.ndarray
    inverse_covariance: np.ndarray
    covariance_cholesky: np.ndarray
    inverse_covariance_ones: np.ndarray
    ones_inverse_covariance_ones: float


@dataclass
class BaoLikelihood:
    redshift: np.ndarray
    value: np.ndarray
    quantity: tuple[str, ...]
    inverse_covariance: np.ndarray
    covariance_cholesky: np.ndarray


def derive_planck_acoustic_compression(chain_dir: Path) -> dict[str, object]:
    """Derive a one-dimensional acoustic-distance compression from PR3 chains.

    This posterior is conditional on the Planck base-LambdaCDM carrier. It is
    retained as a stress test, not treated as a model-neutral CMB likelihood.
    """

    stem = "base_plikHM_TTTEEE_lowl_lowE"
    parameter_path = chain_dir / f"{stem}.paramnames"
    chain_paths = [chain_dir / f"{stem}_{index}.txt" for index in range(1, 5)]
    for path in (parameter_path, *chain_paths):
        if not path.exists():
            raise FileNotFoundError(f"missing Planck chain product: {path}")

    names = [
        line.split()[0].rstrip("*")
        for line in parameter_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    required = ("DAstar", "rdrag", "zstar")
    if any(name not in names for name in required):
        raise ValueError(f"Planck chain lacks one of the required columns: {required}")

    samples = np.vstack([np.loadtxt(path) for path in chain_paths])
    if samples.shape[1] != len(names) + 2:
        raise ValueError("Planck chain and parameter-name dimensions do not agree")
    weight = samples[:, 0]
    if np.any(weight <= 0.0):
        raise ValueError("Planck chain contains non-positive sample weights")

    def column(name: str) -> np.ndarray:
        return samples[:, 2 + names.index(name)]

    ratio = 1000.0 * column("DAstar") / column("rdrag")
    redshift = column("zstar")

    def weighted_mean_and_sigma(values: np.ndarray) -> tuple[float, float]:
        mean = float(np.average(values, weights=weight))
        sigma = float(np.sqrt(np.average((values - mean) ** 2, weights=weight)))
        return mean, sigma

    ratio_mean, ratio_sigma = weighted_mean_and_sigma(ratio)
    redshift_mean, redshift_sigma = weighted_mean_and_sigma(redshift)

    archive_path = chain_dir.parents[2] / PLANCK_ARCHIVE["filename"]
    if not archive_path.exists():
        raise FileNotFoundError(f"missing Planck source archive: {archive_path}")
    archive_hash = sha256(archive_path)
    if archive_hash != PLANCK_ARCHIVE["sha256"]:
        raise ValueError(
            f"SHA-256 mismatch for {archive_path}: "
            f"{archive_hash} != {PLANCK_ARCHIVE['sha256']}"
        )

    return {
        "quantity": "DM(z_star)/r_d = 1000 DAstar[Gpc]/rdrag[Mpc]",
        "mean": ratio_mean,
        "sigma": ratio_sigma,
        "z_star_weighted_mean": redshift_mean,
        "z_star_weighted_sigma": redshift_sigma,
        "chain_rows": int(samples.shape[0]),
        "sum_of_chain_weights": float(np.sum(weight)),
        "carrier": "Planck PR3 base LambdaCDM",
        "qualification": (
            "model-conditional posterior compression; not a model-neutral "
            "alternate-cosmology likelihood"
        ),
        "source_archive": {
            "path": str(archive_path),
            "url": PLANCK_ARCHIVE["url"],
            "sha256": archive_hash,
        },
        "chain_file_sha256": {
            path.name: sha256(path) for path in (parameter_path, *chain_paths)
        },
    }


def with_acoustic_distance_anchor(
    likelihood: BaoLikelihood,
    *,
    redshift: float,
    value: float,
    sigma: float,
) -> BaoLikelihood:
    """Append an independent DM(z*)/r_d datum sharing the BAO amplitude."""

    covariance = np.linalg.inv(likelihood.inverse_covariance)
    dimension = len(likelihood.value)
    extended_covariance = np.zeros((dimension + 1, dimension + 1))
    extended_covariance[:dimension, :dimension] = covariance
    extended_covariance[dimension, dimension] = sigma**2
    return BaoLikelihood(
        redshift=np.append(likelihood.redshift, redshift),
        value=np.append(likelihood.value, value),
        quantity=likelihood.quantity + ("DM_over_rs",),
        inverse_covariance=np.linalg.inv(extended_covariance),
        covariance_cholesky=np.linalg.cholesky(extended_covariance),
    )


def with_2026_lya_full_shape(likelihood: BaoLikelihood) -> BaoLikelihood:
    """Replace the 2025 Ly-alpha BAO pair by the 2026 joint BAO+AP pair.

    DESI DR2 Results IV, Eq. (26), reports at z=2.33
    DM/rd = 39.32 +/- 0.33, DH/rd = 8.600 +/- 0.066, rho = 0.225.
    This is a replacement because the full-shape result contains the BAO
    information from the same Ly-alpha forest sample.
    """

    covariance = np.linalg.inv(likelihood.inverse_covariance)
    value = likelihood.value.copy()
    lya = np.flatnonzero(np.isclose(likelihood.redshift, 2.33))
    if len(lya) != 2:
        raise ValueError("expected exactly two z=2.33 DESI entries")
    dh = next(index for index in lya if likelihood.quantity[index] == "DH_over_rs")
    dm = next(index for index in lya if likelihood.quantity[index] == "DM_over_rs")
    value[dh], value[dm] = 8.600, 39.32
    covariance[lya, :] = 0.0
    covariance[:, lya] = 0.0
    covariance[dh, dh] = 0.066**2
    covariance[dm, dm] = 0.33**2
    covariance[dh, dm] = covariance[dm, dh] = 0.225 * 0.066 * 0.33
    return BaoLikelihood(
        redshift=likelihood.redshift.copy(),
        value=value,
        quantity=likelihood.quantity,
        inverse_covariance=np.linalg.inv(covariance),
        covariance_cholesky=np.linalg.cholesky(covariance),
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_sources(data_dir: Path) -> dict[str, str]:
    hashes: dict[str, str] = {}
    for filename, metadata in SOURCES.items():
        path = data_dir / filename
        if not path.exists():
            raise FileNotFoundError(
                f"missing {path}; obtain the unmodified file from {metadata['url']}"
            )
        actual = sha256(path)
        expected = metadata["sha256"]
        if actual != expected:
            raise ValueError(f"SHA-256 mismatch for {path}: {actual} != {expected}")
        hashes[filename] = actual
    return hashes


def load_pantheon(data_dir: Path) -> PantheonLikelihood:
    table = np.genfromtxt(
        data_dir / "Pantheon+SH0ES.dat",
        names=True,
        dtype=None,
        encoding="utf-8",
    )
    z_hd_all = np.asarray(table["zHD"], dtype=float)
    z_hel_all = np.asarray(table["zHEL"], dtype=float)
    magnitude_all = np.asarray(table["m_b_corr"], dtype=float)
    calibrator_all = np.asarray(table["IS_CALIBRATOR"], dtype=int)
    keep = (z_hd_all > 0.01) & (calibrator_all == 0)

    flat_covariance = np.loadtxt(data_dir / "Pantheon+SH0ES_STAT+SYS.cov")
    dimension = int(flat_covariance[0])
    values = flat_covariance[1:]
    if dimension != len(table) or values.size != dimension * dimension:
        raise ValueError("Pantheon+ table and covariance dimensions do not agree")
    covariance = values.reshape(dimension, dimension)[np.ix_(keep, keep)]
    covariance = 0.5 * (covariance + covariance.T)
    covariance_cholesky = np.linalg.cholesky(covariance)
    inverse = np.linalg.inv(covariance)
    ones = np.ones(int(np.sum(keep)))
    inverse_ones = inverse @ ones
    return PantheonLikelihood(
        z_hd=z_hd_all[keep],
        z_hel=z_hel_all[keep],
        magnitude=magnitude_all[keep],
        inverse_covariance=inverse,
        covariance_cholesky=covariance_cholesky,
        inverse_covariance_ones=inverse_ones,
        ones_inverse_covariance_ones=float(ones @ inverse_ones),
    )


def load_bao(data_dir: Path) -> BaoLikelihood:
    rows: list[tuple[float, float, str]] = []
    with (data_dir / "desi_dr2_bao_mean.txt").open(encoding="utf-8") as handle:
        for line in handle:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            z_text, value_text, quantity = stripped.split()
            rows.append((float(z_text), float(value_text), quantity))
    covariance = np.loadtxt(data_dir / "desi_dr2_bao_cov.txt")
    if covariance.shape != (len(rows), len(rows)):
        raise ValueError("DESI mean vector and covariance dimensions do not agree")
    covariance = 0.5 * (covariance + covariance.T)
    return BaoLikelihood(
        redshift=np.asarray([row[0] for row in rows]),
        value=np.asarray([row[1] for row in rows]),
        quantity=tuple(row[2] for row in rows),
        inverse_covariance=np.linalg.inv(covariance),
        covariance_cholesky=np.linalg.cholesky(covariance),
    )


def sech_squared(value: np.ndarray | float) -> np.ndarray | float:
    return 1.0 / np.cosh(value) ** 2


def crossing_offset(omega_m: float, omega_r: float = 0.0) -> float:
    omega_x = 1.0 - omega_m - omega_r
    if not (0.0 < omega_m < 1.0 and 0.0 <= omega_r < omega_x):
        raise ValueError("invalid density fractions")

    def residual(x_value: float) -> float:
        ordinary = omega_m * math.exp(3.0 * x_value)
        ordinary += omega_r * math.exp(4.0 * x_value)
        return ordinary / math.cosh(x_value) ** 2 - omega_x

    low, high = 0.0, 1.0
    while residual(high) < 0.0:
        high *= 2.0
    for _ in range(100):
        middle = 0.5 * (low + high)
        if residual(middle) < 0.0:
            low = middle
        else:
            high = middle
    return 0.5 * (low + high)


def expansion_function(
    model: str, omega_m: float, omega_r: float = 0.0
) -> Callable[[np.ndarray], np.ndarray]:
    omega_x = 1.0 - omega_m - omega_r
    if model == "lcdm":
        return lambda z: np.sqrt(
            omega_m * (1.0 + z) ** 3
            + omega_r * (1.0 + z) ** 4
            + omega_x
        )
    if model == "cst-b2-unit":
        x_crossing = crossing_offset(omega_m, omega_r)
        normalizer = float(sech_squared(x_crossing))
        return lambda z: np.sqrt(
            omega_m * (1.0 + z) ** 3
            + omega_r * (1.0 + z) ** 4
            + omega_x
            * sech_squared(x_crossing - np.log1p(z))
            / normalizer
        )
    raise ValueError(f"unknown model: {model}")


def comoving_distance_interpolator(
    expansion: Callable[[np.ndarray], np.ndarray],
    maximum_redshift: float,
    refinement: int = 1,
) -> Callable[[np.ndarray], np.ndarray]:
    if refinement < 1:
        raise ValueError("refinement must be a positive integer")
    if maximum_redshift <= 5.0:
        grid_size = max(
            40_001 * refinement,
            int(math.ceil(maximum_redshift * 20_000 * refinement)) + 1,
        )
        grid = np.linspace(0.0, maximum_redshift * 1.000001, grid_size)
        reciprocal = 1.0 / expansion(grid)
        increments = 0.5 * (reciprocal[1:] + reciprocal[:-1]) * np.diff(grid)
        integral = np.empty_like(grid)
        integral[0] = 0.0
        integral[1:] = np.cumsum(increments)
        return lambda z: np.interp(z, grid, integral)

    # A logarithmic grid resolves both the low-redshift regime and the long,
    # smooth integral to last scattering. With y = log(1+z), dz = exp(y) dy.
    maximum_y = math.log1p(maximum_redshift * 1.000001)
    grid_size = max(
        200_001 * refinement,
        int(math.ceil(maximum_y * 30_000 * refinement)) + 1,
    )
    y_grid = np.linspace(0.0, maximum_y, grid_size)
    z_grid = np.expm1(y_grid)
    transformed = np.exp(y_grid) / expansion(z_grid)
    increments = 0.5 * (transformed[1:] + transformed[:-1]) * np.diff(y_grid)
    integral = np.empty_like(y_grid)
    integral[0] = 0.0
    integral[1:] = np.cumsum(increments)
    return lambda z: np.interp(np.log1p(z), y_grid, integral)


def supernova_chi_square(
    likelihood: PantheonLikelihood,
    model: str,
    omega_m: float,
    omega_r: float,
) -> tuple[float, float]:
    expansion = expansion_function(model, omega_m, omega_r)
    distance = comoving_distance_interpolator(expansion, float(np.max(likelihood.z_hd)))
    dimensionless_luminosity_distance = (
        (1.0 + likelihood.z_hel) * distance(likelihood.z_hd)
    )
    base_magnitude = 5.0 * np.log10(dimensionless_luminosity_distance)
    residual_without_offset = likelihood.magnitude - base_magnitude
    numerator = float(likelihood.inverse_covariance_ones @ residual_without_offset)
    offset = numerator / likelihood.ones_inverse_covariance_ones
    residual = residual_without_offset - offset
    chi_square = float(residual @ likelihood.inverse_covariance @ residual)
    return chi_square, offset


def bao_shape_vector(
    likelihood: BaoLikelihood,
    model: str,
    omega_m: float,
    omega_r: float,
) -> np.ndarray:
    expansion = expansion_function(model, omega_m, omega_r)
    distance = comoving_distance_interpolator(expansion, float(np.max(likelihood.redshift)))
    e_value = expansion(likelihood.redshift)
    chi_value = distance(likelihood.redshift)
    shape = np.empty_like(likelihood.value)
    for index, quantity in enumerate(likelihood.quantity):
        if quantity == "DM_over_rs":
            shape[index] = chi_value[index]
        elif quantity == "DH_over_rs":
            shape[index] = 1.0 / e_value[index]
        elif quantity == "DV_over_rs":
            shape[index] = (
                likelihood.redshift[index]
                * chi_value[index] ** 2
                / e_value[index]
            ) ** (1.0 / 3.0)
        else:
            raise ValueError(f"unknown BAO quantity: {quantity}")
    return shape


def bao_chi_square(
    likelihood: BaoLikelihood,
    model: str,
    omega_m: float,
    omega_r: float,
) -> tuple[float, float, float]:
    shape = bao_shape_vector(likelihood, model, omega_m, omega_r)
    inverse = likelihood.inverse_covariance
    amplitude = float(shape @ inverse @ likelihood.value) / float(shape @ inverse @ shape)
    residual = likelihood.value - amplitude * shape
    chi_square = float(residual @ inverse @ residual)
    h0_rd_over_100 = C_KM_S / (100.0 * amplitude)
    return chi_square, amplitude, h0_rd_over_100


def joint_goodness_diagnostics(
    pantheon: PantheonLikelihood,
    bao: BaoLikelihood,
    model: str,
    omega_m: float,
    omega_r: float,
) -> dict[str, object]:
    """Return nominal rank/dof and Cholesky-whitened residual diagnostics.

    These are conventional Gaussian diagnostics for the released compressed
    likelihood. They are not a coverage calibration for systematics or a
    substitute for comparing against the collaboration's reference carrier.
    """

    expansion = expansion_function(model, omega_m, omega_r)
    maximum_redshift = max(
        float(np.max(pantheon.z_hd)), float(np.max(bao.redshift))
    )
    distance = comoving_distance_interpolator(expansion, maximum_redshift)

    luminosity_distance = (1.0 + pantheon.z_hel) * distance(pantheon.z_hd)
    sn_base = 5.0 * np.log10(luminosity_distance)
    sn_without_offset = pantheon.magnitude - sn_base
    offset = float(pantheon.inverse_covariance_ones @ sn_without_offset)
    offset /= pantheon.ones_inverse_covariance_ones
    sn_residual = sn_without_offset - offset
    sn_whitened = np.linalg.solve(pantheon.covariance_cholesky, sn_residual)

    shape = bao_shape_vector(bao, model, omega_m, omega_r)
    inverse = bao.inverse_covariance
    amplitude = float(shape @ inverse @ bao.value) / float(shape @ inverse @ shape)
    bao_residual = bao.value - amplitude * shape
    bao_whitened = np.linalg.solve(bao.covariance_cholesky, bao_residual)

    whitened = np.concatenate((sn_whitened, bao_whitened))
    chi_square = float(whitened @ whitened)
    data_rank = int(whitened.size)
    fitted_parameter_count = 3  # Omega_m, SN offset, and c/(H0 r_d)
    nominal_dof = data_rank - fitted_parameter_count
    return {
        "data_vector_length_and_covariance_rank": data_rank,
        "fitted_parameter_count": fitted_parameter_count,
        "nominal_degrees_of_freedom": nominal_dof,
        "chi_square_from_whitened_residuals": chi_square,
        "nominal_reduced_chi_square": chi_square / nominal_dof,
        "whitened_residual_rms_per_nominal_dof": math.sqrt(
            chi_square / nominal_dof
        ),
        "maximum_absolute_cholesky_whitened_residual": float(
            np.max(np.abs(whitened))
        ),
        "covariance_positive_definite": True,
        "qualification": (
            "nominal Gaussian diagnostic for the released compressed data; "
            "not a systematics coverage calibration"
        ),
    }


def golden_minimum(
    function: Callable[[float], float],
    low: float = 0.15,
    high: float = 0.50,
    tolerance: float = 2.0e-8,
) -> tuple[float, float]:
    ratio = (math.sqrt(5.0) - 1.0) / 2.0
    left = high - ratio * (high - low)
    right = low + ratio * (high - low)
    f_left = function(left)
    f_right = function(right)
    while high - low > tolerance:
        if f_left < f_right:
            high, right, f_right = right, left, f_left
            left = high - ratio * (high - low)
            f_left = function(left)
        else:
            low, left, f_left = left, right, f_right
            right = low + ratio * (high - low)
            f_right = function(right)
    minimum = 0.5 * (low + high)
    return minimum, function(minimum)


def delta_one_interval(
    function: Callable[[float], float],
    minimum: float,
    minimum_value: float,
    low_bound: float = 0.15,
    high_bound: float = 0.50,
) -> tuple[float, float]:
    target = minimum_value + 1.0

    def root(low: float, high: float) -> float:
        low_value = function(low) - target
        high_value = function(high) - target
        if low_value * high_value > 0.0:
            raise ArithmeticError("Delta-chi-square root is not bracketed")
        for _ in range(70):
            middle = 0.5 * (low + high)
            middle_value = function(middle) - target
            if low_value * middle_value <= 0.0:
                high, high_value = middle, middle_value
            else:
                low, low_value = middle, middle_value
        return 0.5 * (low + high)

    return root(low_bound, minimum), root(minimum, high_bound)


def fit_model(
    model: str,
    pantheon: PantheonLikelihood,
    bao: BaoLikelihood,
    omega_r: float,
) -> dict[str, object]:
    sn_cache: dict[float, tuple[float, float]] = {}
    bao_cache: dict[float, tuple[float, float, float]] = {}

    def sn(omega_m: float) -> tuple[float, float]:
        key = round(float(omega_m), 12)
        if key not in sn_cache:
            sn_cache[key] = supernova_chi_square(
                pantheon, model, float(omega_m), omega_r
            )
        return sn_cache[key]

    def bao_only(omega_m: float) -> tuple[float, float, float]:
        key = round(float(omega_m), 12)
        if key not in bao_cache:
            bao_cache[key] = bao_chi_square(bao, model, float(omega_m), omega_r)
        return bao_cache[key]

    objectives = {
        "pantheon_plus": lambda omega: sn(omega)[0],
        "desi_dr2_bao": lambda omega: bao_only(omega)[0],
        "joint": lambda omega: sn(omega)[0] + bao_only(omega)[0],
    }
    result: dict[str, object] = {}
    for name, objective in objectives.items():
        omega_best, chi_best = golden_minimum(objective)
        interval = delta_one_interval(objective, omega_best, chi_best)
        entry: dict[str, object] = {
            "omega_m_best": omega_best,
            "omega_m_delta_chi2_1": list(interval),
            "chi_square": chi_best,
        }
        if name in ("desi_dr2_bao", "joint"):
            bao_result = bao_only(omega_best)
            entry["bao_profile_amplitude_c_over_H0rd"] = bao_result[1]
            entry["profiled_rd_h_mpc"] = bao_result[2]
            if float(np.max(bao.redshift)) > 100.0:
                anchor_index = int(np.argmax(bao.redshift))
                anchor_shape = bao_shape_vector(
                    bao, model, omega_best, omega_r
                )[anchor_index]
                anchor_prediction = bao_result[1] * anchor_shape
                covariance = np.linalg.inv(bao.inverse_covariance)
                anchor_sigma = math.sqrt(float(covariance[anchor_index, anchor_index]))
                anchor_residual = float(bao.value[anchor_index] - anchor_prediction)
                entry["acoustic_anchor"] = {
                    "redshift": float(bao.redshift[anchor_index]),
                    "observed": float(bao.value[anchor_index]),
                    "sigma": anchor_sigma,
                    "predicted": float(anchor_prediction),
                    "chi_square_contribution": (anchor_residual / anchor_sigma) ** 2,
                }
        if name in ("pantheon_plus", "joint"):
            entry["profiled_sn_offset"] = sn(omega_best)[1]
        if name == "joint":
            entry["chi_square_pantheon_plus"] = sn(omega_best)[0]
            entry["chi_square_desi_dr2_bao"] = bao_only(omega_best)[0]
            goodness = joint_goodness_diagnostics(
                pantheon, bao, model, omega_best, omega_r
            )
            if abs(
                float(goodness["chi_square_from_whitened_residuals"])
                - chi_best
            ) > 1.0e-5:
                raise ArithmeticError(
                    "whitened residual norm does not reproduce joint chi-square"
                )
            entry["goodness_of_fit"] = goodness
            if model == "cst-b2-unit":
                x_crossing = crossing_offset(omega_best, omega_r)
                entry["x_crossing"] = x_crossing
                entry["z_crossing"] = math.exp(x_crossing) - 1.0
        result[name] = entry
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", required=True, type=Path)
    parser.add_argument("--planck-chain-dir", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--omega-r", type=float, default=9.15e-5)
    args = parser.parse_args()

    hashes = verify_sources(args.data_dir)
    pantheon = load_pantheon(args.data_dir)
    bao_2025 = load_bao(args.data_dir)
    bao_2026 = with_2026_lya_full_shape(bao_2025)
    planck_acoustic: dict[str, object] | None = None
    acoustic_redshift = 1089.92
    comparison_inputs = [
        (
            "desi-dr2-bao-2025",
            bao_2025,
            "direct released BAO and supernova likelihood",
        ),
        (
            "desi-dr2-galaxy-bao-plus-lya-full-shape-2026",
            bao_2026,
            (
                "provisional Gaussian reconstruction of the published 2026 "
                "Ly-alpha pair; lower-redshift cross-covariances assumed zero"
            ),
        ),
    ]
    acoustic_protocol: dict[str, object] = {"included": False}
    acoustic_integration_relative_change: float | None = None
    if args.planck_chain_dir is not None:
        planck_acoustic = derive_planck_acoustic_compression(args.planck_chain_dir)
        bao_2025_historical_anchor = with_acoustic_distance_anchor(
            bao_2025,
            redshift=acoustic_redshift,
            value=94.32,
            sigma=0.28,
        )
        bao_2025_tight_anchor = with_acoustic_distance_anchor(
            bao_2025,
            redshift=acoustic_redshift,
            value=float(planck_acoustic["mean"]),
            sigma=float(planck_acoustic["sigma"]),
        )
        convergence_expansion = expansion_function(
            "cst-b2-unit", 0.32, args.omega_r
        )
        convergence_coarse = comoving_distance_interpolator(
            convergence_expansion, acoustic_redshift
        )(np.asarray([acoustic_redshift]))[0]
        convergence_fine = comoving_distance_interpolator(
            convergence_expansion, acoustic_redshift, refinement=2
        )(np.asarray([acoustic_redshift]))[0]
        acoustic_integration_relative_change = float(
            abs(convergence_fine - convergence_coarse) / convergence_fine
        )
        comparison_inputs.extend(
            [
                (
                    "desi-dr2-2025-plus-historical-project-acoustic-anchor",
                    bao_2025_historical_anchor,
                    (
                        "released 2025 DESI BAO plus a historical project acoustic "
                        "compression with undocumented uncertainty construction; "
                        "conditional sensitivity test, not a Planck-published datum"
                    ),
                ),
                (
                    "desi-dr2-2025-plus-base-lcdm-chain-acoustic-compression",
                    bao_2025_tight_anchor,
                    (
                        "released 2025 DESI BAO plus a Planck base-LambdaCDM "
                        "posterior compression; deliberately inadmissible as a "
                        "model-neutral likelihood and used only as a stringent "
                        "stress test"
                    ),
                ),
            ]
        )
        acoustic_protocol = {
            "included": True,
            "redshift": acoustic_redshift,
            "historical_project_compression": {
                "value": 94.32,
                "sigma": 0.28,
                "provenance": (
                    "scale-as-modular-observable/chats/03/outputs/"
                    "P1_shape_invariant_result.md"
                ),
                "qualification": (
                    "historical project sensitivity anchor with undocumented "
                    "uncertainty construction; not directly published by Planck"
                ),
            },
            "official_chain_derived_compression": planck_acoustic,
            "integration_convergence": {
                "test_model": "unit CST-B2 at Omega_m=0.32",
                "coarse_to_double_grid_relative_change": (
                    acoustic_integration_relative_change
                ),
            },
        }
    comparisons: dict[str, object] = {}
    for dataset_name, bao, qualification in comparison_inputs:
        models = {
            model: fit_model(model, pantheon, bao, args.omega_r)
            for model in ("lcdm", "cst-b2-unit")
        }
        benchmark_omega_m = 0.310598
        benchmark: dict[str, object] = {}
        for model in models:
            sn_chi, _ = supernova_chi_square(
                pantheon, model, benchmark_omega_m, args.omega_r
            )
            bao_chi, _, _ = bao_chi_square(
                bao, model, benchmark_omega_m, args.omega_r
            )
            joint_chi = sn_chi + bao_chi
            benchmark[model] = {
                "omega_m": benchmark_omega_m,
                "chi_square": joint_chi,
                "delta_chi_square_from_own_best_fit": (
                    joint_chi - models[model]["joint"]["chi_square"]
                ),
            }
        comparisons[dataset_name] = {
            "qualification": qualification,
            "models": models,
            "frozen_benchmark": benchmark,
            "joint_delta_chi_square_cst_minus_lcdm": (
                models["cst-b2-unit"]["joint"]["chi_square"]
                - models["lcdm"]["joint"]["chi_square"]
            ),
            "equal_parameter_count": True,
        }
    baseline_models = comparisons["desi-dr2-bao-2025"]["models"]
    latest_models = comparisons[
        "desi-dr2-galaxy-bao-plus-lya-full-shape-2026"
    ]["models"]
    result = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "runtime": {
            "python": sys.version,
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
        "protocol": {
            "models": ["flat LambdaCDM", "frozen unit CST-B2"],
            "fitted_shape_parameter_each": "Omega_m",
            "omega_r": args.omega_r,
            "pantheon_filter": "zHD > 0.01 and IS_CALIBRATOR == 0",
            "pantheon_count": int(pantheon.z_hd.size),
            "desi_bao_count": int(bao_2025.redshift.size),
            "profiled_nuisance": ["supernova offset", "c/(H0 r_d)"],
            "latest_update": (
                "DESI DR2 Results IV Eq. (26) replaces the z=2.33 Ly-alpha "
                "BAO pair by a reconstructed Gaussian for the joint BAO plus "
                "full-shape AP pair; the full released likelihood is pending"
            ),
            "latest_update_values": {
                "z": 2.33,
                "DM_over_rd": 39.32,
                "DM_over_rd_sigma": 0.33,
                "DH_over_rd": 8.600,
                "DH_over_rd_sigma": 0.066,
                "correlation": 0.225,
                "cross_covariance_assumption": (
                    "zero with lower-redshift DESI blocks pending a full release"
                ),
                "primary_source": "https://arxiv.org/abs/2607.27410v3",
            },
            "acoustic_distance_stress_tests": acoustic_protocol,
        },
        "source_sha256": hashes,
        "comparisons": comparisons,
        "checks": {
            "pantheon_count_is_1580": pantheon.z_hd.size == 1580,
            "bao_count_is_13": bao_2025.redshift.size == 13,
            "all_covariances_positive_definite": bool(
                np.all(np.diag(pantheon.covariance_cholesky) > 0.0)
                and all(
                    np.all(np.diag(bao.covariance_cholesky) > 0.0)
                    for _, bao, _ in comparison_inputs
                )
            ),
            "all_joint_whitened_residual_norms_reproduce_chi_square": all(
                abs(
                    float(
                        comparisons[comparison]["models"][model]["joint"]
                        ["goodness_of_fit"]
                        ["chi_square_from_whitened_residuals"]
                    )
                    - float(
                        comparisons[comparison]["models"][model]["joint"]
                        ["chi_square"]
                    )
                )
                < 1.0e-5
                for comparison in comparisons
                for model in comparisons[comparison]["models"]
            ),
            "planck_chain_not_requested_or_row_count_is_24497": (
                planck_acoustic is None or planck_acoustic["chain_rows"] == 24_497
            ),
            "planck_acoustic_not_requested_or_compression_reproduced": (
                planck_acoustic is None
                or (
                    abs(float(planck_acoustic["mean"]) - 94.31404) < 0.00002
                    and abs(float(planck_acoustic["sigma"]) - 0.03458) < 0.00002
                )
            ),
            "acoustic_integration_not_requested_or_converged": (
                acoustic_integration_relative_change is None
                or acoustic_integration_relative_change < 2.0e-9
            ),
            "published_lcdm_pantheon_omega_m_reproduced": abs(
                baseline_models["lcdm"]["pantheon_plus"]["omega_m_best"] - 0.334
            ) < 0.003,
            "published_lcdm_bao_omega_m_reproduced": abs(
                baseline_models["lcdm"]["desi_dr2_bao"]["omega_m_best"] - 0.2975
            ) < 0.002,
            "published_2026_lcdm_joint_desi_omega_m_reproduced": abs(
                latest_models["lcdm"]["desi_dr2_bao"]["omega_m_best"] - 0.3012
            ) < 0.002,
            "all_finite": bool(
                np.isfinite(
                    [
                        comparisons[comparison]["models"][model][dataset]["chi_square"]
                        for comparison in comparisons
                        for model in comparisons[comparison]["models"]
                        for dataset in ("pantheon_plus", "desi_dr2_bao", "joint")
                    ]
                ).all()
            ),
        },
    }
    if not all(result["checks"].values()):
        raise ArithmeticError(f"one or more validation checks failed: {result['checks']}")
    rendered = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
