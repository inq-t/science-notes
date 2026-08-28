#!/usr/bin/env python3
"""DES-Dovekie robustness fit for the frozen unit CST-B2 background.

The script reuses the expansion, distance, DESI, profiling, and optimizer
implementation in fit-late-time-background.py.  It adds only the independently
recalibrated DES-Dovekie supernova vector and its released inverse covariance.
"""

from __future__ import annotations

import argparse
import hashlib
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
BASE_RECEIPT_PATH = HERE / "fit-late-time-background.py"
BASE_SPEC = importlib.util.spec_from_file_location(
    "cst_late_time_background_receipt", BASE_RECEIPT_PATH
)
if BASE_SPEC is None or BASE_SPEC.loader is None:
    raise ImportError(f"cannot load shared receipt from {BASE_RECEIPT_PATH}")
BASE = importlib.util.module_from_spec(BASE_SPEC)
sys.modules[BASE_SPEC.name] = BASE
BASE_SPEC.loader.exec_module(BASE)

WORKSPACE_ROOT = HERE.parents[1]
DEFAULT_DOVEKIE_DATA_DIR = (
    WORKSPACE_ROOT / "data/des-dovekie-distance-likelihood/local"
)

SOURCES = {
    "desi_dr2_bao_mean.txt": BASE.SOURCES["desi_dr2_bao_mean.txt"],
    "desi_dr2_bao_cov.txt": BASE.SOURCES["desi_dr2_bao_cov.txt"],
    "DES-Dovekie_HD.csv": {
        "url": (
            "https://raw.githubusercontent.com/des-science/DES-SN5YR/"
            "main/4_DISTANCES_COVMAT/DES-Dovekie_HD.csv"
        ),
        "sha256": "2f57019d783eaa976df80a41b0054171a2d994ee9808d715ce850c2df5720aaf",
    },
    "DES-Dovekie_STAT+SYS.npz": {
        "url": (
            "https://raw.githubusercontent.com/des-science/DES-SN5YR/"
            "main/4_DISTANCES_COVMAT/STAT%2BSYS.npz"
        ),
        "sha256": "ffd3124b32148b1372bd95fda9299269f0352a9f8eee02d416c610e38495463b",
    },
}

BAO_FILENAMES = (
    "desi_dr2_bao_mean.txt",
    "desi_dr2_bao_cov.txt",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_sources(bao_data_dir: Path, dovekie_data_dir: Path) -> dict[str, str]:
    hashes: dict[str, str] = {}
    for filename, metadata in SOURCES.items():
        data_dir = bao_data_dir if filename in BAO_FILENAMES else dovekie_data_dir
        path = data_dir / filename
        if not path.exists():
            raise FileNotFoundError(
                f"missing {path}; obtain the unmodified file from {metadata['url']}"
            )
        actual = sha256(path)
        if actual != metadata["sha256"]:
            raise ValueError(
                f"SHA-256 mismatch for {path}: {actual} != {metadata['sha256']}"
            )
        hashes[filename] = actual
    return hashes


def load_dovekie(data_dir: Path) -> tuple[BASE.PantheonLikelihood, dict[str, object]]:
    rows: list[tuple[float, float, float, float, float]] = []
    with (data_dir / "DES-Dovekie_HD.csv").open(encoding="utf-8") as handle:
        for line in handle:
            if not line.startswith("SN:"):
                continue
            fields = line.split()
            rows.append(
                (
                    float(fields[3]),
                    float(fields[4]),
                    float(fields[5]),
                    float(fields[6]),
                    float(fields[8]),
                )
            )
    if not rows:
        raise ValueError("DES-Dovekie Hubble diagram contains no SN rows")

    values = np.asarray(rows)
    z_hd_all, z_hel_all, magnitude_all = values[:, 0], values[:, 1], values[:, 2]
    mu_error, mu_error_systematic = values[:, 3], values[:, 4]
    keep = z_hd_all > 0.0

    packed = np.load(data_dir / "DES-Dovekie_STAT+SYS.npz")
    if tuple(packed.files[:2]) != ("nsn", "cov"):
        raise ValueError(f"unexpected DES-Dovekie archive fields: {packed.files}")
    dimension = int(packed["nsn"][0])
    if dimension != len(rows):
        raise ValueError("DES-Dovekie vector and covariance dimensions do not agree")
    inverse_all = np.zeros((dimension, dimension))
    inverse_all[np.triu_indices(dimension)] = packed["cov"]
    lower = np.tril_indices(dimension, -1)
    inverse_all[lower] = inverse_all.T[lower]
    if not bool(np.all(keep)):
        raise ValueError(
            "the reusable compact receipt requires every released row to pass; "
            "subsetting a precision matrix would require covariance marginalization"
        )
    inverse = inverse_all
    ones = np.ones(int(np.sum(keep)))
    inverse_ones = inverse @ ones

    # The released diagonal diagnostics are not added here.  Inverting the
    # released precision matrix reproduces sqrt(MUERR^2 + MUERR_SYS^2), so
    # adding either column again would double count uncertainty.
    covariance = np.linalg.inv(inverse)
    covariance_cholesky = np.linalg.cholesky(covariance)
    released_diagonal = np.sqrt(np.diag(covariance))
    diagnostic_diagonal = np.sqrt(mu_error[keep] ** 2 + mu_error_systematic[keep] ** 2)
    diagonal_maximum_difference = float(
        np.max(np.abs(released_diagonal - diagnostic_diagonal))
    )

    likelihood = BASE.PantheonLikelihood(
        z_hd=z_hd_all[keep],
        z_hel=z_hel_all[keep],
        magnitude=magnitude_all[keep],
        inverse_covariance=inverse,
        covariance_cholesky=covariance_cholesky,
        inverse_covariance_ones=inverse_ones,
        ones_inverse_covariance_ones=float(ones @ inverse_ones),
    )
    metadata = {
        "row_count": int(np.sum(keep)),
        "released_row_count": len(rows),
        "redshift_cut_in_likelihood": "zHD > 0.0; every released row passes",
        "minimum_zHD": float(np.min(likelihood.z_hd)),
        "maximum_zHD": float(np.max(likelihood.z_hd)),
        "inverse_covariance_packing": "upper triangle, reflected to lower triangle",
        "ones_precision_ones": likelihood.ones_inverse_covariance_ones,
        "marginalization_constant_ln_C_over_2pi": math.log(
            likelihood.ones_inverse_covariance_ones / (2.0 * math.pi)
        ),
        "maximum_covariance_diagonal_difference_from_release_diagnostics": (
            diagonal_maximum_difference
        ),
    }
    return likelihood, metadata


def fit_model(
    model: str,
    supernova: BASE.PantheonLikelihood,
    bao: BASE.BaoLikelihood,
    omega_r: float,
) -> dict[str, object]:
    sn_cache: dict[float, tuple[float, float]] = {}
    bao_cache: dict[float, tuple[float, float, float]] = {}

    def sn(omega_m: float) -> tuple[float, float]:
        key = round(float(omega_m), 12)
        if key not in sn_cache:
            sn_cache[key] = BASE.supernova_chi_square(
                supernova, model, float(omega_m), omega_r
            )
        return sn_cache[key]

    def bao_only(omega_m: float) -> tuple[float, float, float]:
        key = round(float(omega_m), 12)
        if key not in bao_cache:
            bao_cache[key] = BASE.bao_chi_square(
                bao, model, float(omega_m), omega_r
            )
        return bao_cache[key]

    objectives: dict[str, Callable[[float], float]] = {
        "des_dovekie": lambda omega: sn(omega)[0],
        "joint": lambda omega: sn(omega)[0] + bao_only(omega)[0],
    }
    marginalization_constant = math.log(
        supernova.ones_inverse_covariance_ones / (2.0 * math.pi)
    )
    result: dict[str, object] = {}
    for name, objective in objectives.items():
        omega_best, chi_best = BASE.golden_minimum(objective)
        interval = BASE.delta_one_interval(objective, omega_best, chi_best)
        entry: dict[str, object] = {
            "omega_m_best": omega_best,
            "omega_m_delta_chi2_1": list(interval),
            "profile_chi_square": chi_best,
            "des_reported_convention_chi_square": chi_best
            + marginalization_constant,
            "profiled_sn_offset": sn(omega_best)[1],
        }
        if name == "joint":
            bao_result = bao_only(omega_best)
            goodness = BASE.joint_goodness_diagnostics(
                supernova, bao, model, omega_best, omega_r
            )
            if abs(
                float(goodness["chi_square_from_whitened_residuals"])
                - chi_best
            ) > 1.0e-5:
                raise ArithmeticError(
                    "whitened residual norm does not reproduce joint chi-square"
                )
            entry.update(
                {
                    "profile_chi_square_des_dovekie": sn(omega_best)[0],
                    "profile_chi_square_desi_dr2": bao_result[0],
                    "bao_profile_amplitude_c_over_H0rd": bao_result[1],
                    "profiled_rd_h_mpc": bao_result[2],
                    "goodness_of_fit": goodness,
                }
            )
            if model == "cst-b2-unit":
                crossing = BASE.crossing_offset(omega_best, omega_r)
                entry["x_crossing"] = crossing
                entry["z_crossing"] = math.exp(crossing) - 1.0
        result[name] = entry
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--bao-data-dir", type=Path, default=BASE.DEFAULT_BAO_DATA_DIR
    )
    parser.add_argument(
        "--dovekie-data-dir", type=Path, default=DEFAULT_DOVEKIE_DATA_DIR
    )
    parser.add_argument("--output", type=Path)
    parser.add_argument("--omega-r", type=float, default=9.15e-5)
    args = parser.parse_args()

    hashes = verify_sources(args.bao_data_dir, args.dovekie_data_dir)
    dovekie, dovekie_metadata = load_dovekie(args.dovekie_data_dir)
    bao_2025 = BASE.load_bao(args.bao_data_dir)
    bao_2026 = BASE.with_2026_lya_full_shape(bao_2025)

    # Popovic et al. neglect radiation for the SN-only fit.  This separate
    # validation uses their carrier before the common late-time comparison.
    official_lcdm_omega, official_lcdm_profile = BASE.golden_minimum(
        lambda omega: BASE.supernova_chi_square(
            dovekie, "lcdm", omega, 0.0
        )[0]
    )
    marginalization_constant = float(
        dovekie_metadata["marginalization_constant_ln_C_over_2pi"]
    )
    official_lcdm_reported = official_lcdm_profile + marginalization_constant

    comparison_inputs = {
        "released_2025_bao_plus_dovekie": (
            bao_2025,
            "fully released DESI DR2 BAO likelihood plus released DES-Dovekie",
        ),
        "provisional_2026_bao_plus_dovekie": (
            bao_2026,
            (
                "published bivariate Gaussian reconstruction for the 2026 "
                "Ly-alpha pair; lower-redshift cross-covariances assumed zero"
            ),
        ),
    }
    comparisons: dict[str, object] = {}
    for name, (bao, qualification) in comparison_inputs.items():
        models = {
            model: fit_model(model, dovekie, bao, args.omega_r)
            for model in ("lcdm", "cst-b2-unit")
        }
        delta = (
            models["cst-b2-unit"]["joint"]["profile_chi_square"]
            - models["lcdm"]["joint"]["profile_chi_square"]
        )
        comparisons[name] = {
            "qualification": qualification,
            "models": models,
            "joint_delta_chi_square_cst_minus_lcdm": delta,
            "equal_parameter_count": True,
            "normalization_note": (
                "ln(C/2pi) is constant for the shared Dovekie mask and "
                "covariance, so it cancels exactly in every model delta"
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
            "role": "alternate corrected-supernova robustness test",
            "models": ["flat LambdaCDM", "frozen unit CST-B2"],
            "fitted_shape_parameter_each": "Omega_m",
            "omega_r_for_joint_comparison": args.omega_r,
            "profiled_nuisance": ["supernova offset", "c/(H0 r_d)"],
            "supernova_theory_distance": "(1 + zHEL) chi(zHD)",
            "desi_update": (
                "the separate provisional row reconstructs the DESI DR2 "
                "Results IV Eq. (26) Ly-alpha Gaussian while its full release "
                "is pending"
            ),
            "dovekie": dovekie_metadata,
        },
        "source_sha256": hashes,
        "official_lcdm_validation": {
            "assumption": "radiation neglected, following Popovic et al. SN fit",
            "omega_m_best": official_lcdm_omega,
            "profile_chi_square_A_minus_B2_over_C": official_lcdm_profile,
            "marginalization_constant_ln_C_over_2pi": marginalization_constant,
            "reported_chi_square": official_lcdm_reported,
            "paper_table_10": {"omega_m": "0.330 +/- 0.015", "chi_square": 1640.3},
        },
        "comparisons": comparisons,
        "checks": {
            "dovekie_count_is_1820": dovekie.z_hd.size == 1820,
            "all_released_rows_pass_mask": (
                dovekie_metadata["released_row_count"] == dovekie_metadata["row_count"]
            ),
            "release_already_obeys_zmin_0p025": float(np.min(dovekie.z_hd)) > 0.025,
            "full_covariance_matches_diagonal_diagnostics": (
                dovekie_metadata[
                    "maximum_covariance_diagonal_difference_from_release_diagnostics"
                ]
                < 1.0e-5
            ),
            "dovekie_covariance_positive_definite": bool(
                np.all(np.diag(dovekie.covariance_cholesky) > 0.0)
            ),
            "joint_whitened_residual_norms_reproduce_chi_square": all(
                abs(
                    float(
                        comparisons[comparison]["models"][model]["joint"]
                        ["goodness_of_fit"]
                        ["chi_square_from_whitened_residuals"]
                    )
                    - float(
                        comparisons[comparison]["models"][model]["joint"]
                        ["profile_chi_square"]
                    )
                )
                < 1.0e-5
                for comparison in comparisons
                for model in comparisons[comparison]["models"]
            ),
            "published_lcdm_omega_m_reproduced": abs(official_lcdm_omega - 0.330) < 0.001,
            "published_lcdm_chi_square_reproduced": abs(
                official_lcdm_reported - 1640.3
            )
            < 0.05,
            "all_finite": bool(
                np.isfinite(
                    [
                        comparisons[comparison]["models"][model][dataset]
                        ["profile_chi_square"]
                        for comparison in comparisons
                        for model in comparisons[comparison]["models"]
                        for dataset in ("des_dovekie", "joint")
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
