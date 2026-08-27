"""Nested acoustic-angle tests for the frozen CH0 causal-grain candidate.

This script uses archived public MCMC chains.  It computes a Gaussian profile
likelihood surrogate for fixing the *physical* acoustic angle ``100 theta_*``
to the CH0 prediction.  It does not pretend that posterior-chain arithmetic is
a fresh likelihood optimization.

The Planck chains contain frequency weights in column zero, minus log
likelihood in column one, and parameters in the order given by ``.paramnames``.
The ACT/Cobaya chains name every column in their first comment line.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np

from acoustic_receipts import acoustic_from_quality, minimal_chiral_quality


MODULE = Path(__file__).resolve().parent
REPO = MODULE.parent

PLANCK_ROOT = (
    REPO
    / "causal-wall-spectral-theory"
    / "sources"
    / "data"
    / "planck-2018"
    / "base-plikHM-TTTEEE-lowl-lowE"
    / "base"
)
ACT_ROOT = (
    REPO
    / "causal-wall-spectral-theory"
    / "sources"
    / "data"
    / "act-dr6"
)

F_PI_CHARGED_MEV = 130.2
F_PI_CHARGED_SIGMA_MEV = 1.2


@dataclass(frozen=True)
class Chain:
    label: str
    source_model: str
    files: tuple[Path, ...]
    names: tuple[str, ...]
    values: np.ndarray
    weights: np.ndarray
    minus_loglike: np.ndarray
    theta_name: str
    theta_mc_name: str
    theta_mc_factor: float
    convergence_note: str

    def column(self, name: str) -> np.ndarray:
        return self.values[:, self.names.index(name)]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def relative(path: Path) -> str:
    return path.relative_to(REPO).as_posix()


def weighted_mean(values: np.ndarray, weights: np.ndarray) -> float:
    return float(np.average(values, weights=weights))


def weighted_variance(values: np.ndarray, weights: np.ndarray) -> float:
    mean = weighted_mean(values, weights)
    return float(np.average((values - mean) ** 2, weights=weights))


def weighted_std(values: np.ndarray, weights: np.ndarray) -> float:
    return math.sqrt(weighted_variance(values, weights))


def weighted_quantile(
    values: np.ndarray, weights: np.ndarray, quantiles: Iterable[float]
) -> list[float]:
    order = np.argsort(values)
    sorted_values = values[order]
    sorted_weights = weights[order]
    cumulative = np.cumsum(sorted_weights) - 0.5 * sorted_weights
    cumulative /= np.sum(sorted_weights)
    return [
        float(np.interp(quantile, cumulative, sorted_values))
        for quantile in quantiles
    ]


def effective_sample_size(weights: np.ndarray) -> float:
    return float(np.sum(weights) ** 2 / np.sum(weights**2))


def load_planck_chain(directory_name: str, label: str) -> Chain:
    directory = PLANCK_ROOT / directory_name
    stem = f"base_{directory_name}"
    paramnames = directory / f"{stem}.paramnames"
    names = tuple(
        line.split()[0] for line in paramnames.read_text(encoding="utf-8").splitlines()
    )
    files = tuple(directory / f"{stem}_{index}.txt" for index in range(1, 5))
    arrays = [np.loadtxt(path) for path in files]
    data = np.vstack(arrays)
    if data.shape[1] != 2 + len(names):
        raise ValueError(f"column mismatch for {directory}")
    return Chain(
        label=label,
        source_model="six-parameter flat LambdaCDM plus Planck nuisance parameters",
        files=(paramnames, *files),
        names=names,
        values=data[:, 2:],
        weights=data[:, 0],
        minus_loglike=data[:, 1],
        theta_name="thetastar*",
        theta_mc_name="theta",
        theta_mc_factor=1.0,
        convergence_note="Official Planck chain; properties.ini declares burn_removed=T.",
    )


def load_cobaya_chain(directory_name: str, stem: str, label: str) -> Chain:
    directory = ACT_ROOT / directory_name / stem
    files = tuple(directory / f"{stem}.{index}.txt" for index in range(1, 5))
    header = files[0].open("r", encoding="utf-8").readline().lstrip("#").split()
    arrays = [np.loadtxt(path) for path in files]
    data = np.vstack(arrays)
    if data.shape[1] != len(header):
        raise ValueError(f"column mismatch for {directory}")
    sampled_start = header.index("ombh2")
    names = tuple(header[sampled_start:])
    return Chain(
        label=label,
        source_model=(
            "flat LambdaCDM plus running nrun and the nuisance parameters named "
            "in the archived Cobaya chain"
        ),
        files=files,
        names=names,
        values=data[:, sampled_start:],
        weights=data[:, header.index("weight")],
        minus_loglike=data[:, header.index("minuslogpost")],
        theta_name="thetastar",
        theta_mc_name="cosmomc_theta",
        theta_mc_factor=100.0,
        convergence_note=(
            "Secondary check only: archived ACT checkpoint is marked converged=false; "
            "this is also an nrun extension rather than the six-parameter baseline."
        ),
    )


def ch0_prediction() -> dict[str, float]:
    central_quality = minimal_chiral_quality(F_PI_CHARGED_MEV)
    q_central, theta_central = acoustic_from_quality(central_quality)
    _, theta_low = acoustic_from_quality(
        minimal_chiral_quality(F_PI_CHARGED_MEV - F_PI_CHARGED_SIGMA_MEV)
    )
    _, theta_high = acoustic_from_quality(
        minimal_chiral_quality(F_PI_CHARGED_MEV + F_PI_CHARGED_SIGMA_MEV)
    )
    return {
        "f_pi_charged_MeV": F_PI_CHARGED_MEV,
        "f_pi_charged_sigma_MeV": F_PI_CHARGED_SIGMA_MEV,
        "q_star": q_central,
        "theta_star": theta_central / 100.0,
        "theta_star_100": theta_central,
        "theta_star_100_input_sigma": (theta_high - theta_low) / 2.0,
        "theta_star_100_input_interval": [theta_low, theta_high],
    }


def gaussian_conditionals(
    chain: Chain, target: float, requested: Iterable[str]
) -> dict[str, dict[str, float]]:
    theta = chain.column(chain.theta_name)
    theta_mean = weighted_mean(theta, chain.weights)
    theta_var = weighted_variance(theta, chain.weights)
    result: dict[str, dict[str, float]] = {}
    for name in requested:
        if name not in chain.names or name == chain.theta_name:
            continue
        values = chain.column(name)
        mean = weighted_mean(values, chain.weights)
        std = weighted_std(values, chain.weights)
        covariance = float(
            np.average((values - mean) * (theta - theta_mean), weights=chain.weights)
        )
        conditional = mean + covariance / theta_var * (target - theta_mean)
        result[name] = {
            "unconstrained_mean": mean,
            "unconstrained_sigma": std,
            "conditional_mean": conditional,
            "shift_in_marginal_sigma": (conditional - mean) / std,
            "correlation_with_theta_star": covariance / (std * math.sqrt(theta_var)),
        }
    return result


def summarize(chain: Chain, prediction: dict[str, float]) -> dict[str, object]:
    target = prediction["theta_star_100"]
    input_sigma = prediction["theta_star_100_input_sigma"]
    theta = chain.column(chain.theta_name)
    theta_mc = chain.theta_mc_factor * chain.column(chain.theta_mc_name)
    mean = weighted_mean(theta, chain.weights)
    sigma = weighted_std(theta, chain.weights)
    residual = target - mean
    z_fixed = residual / sigma
    delta_chi2 = z_fixed**2

    log_theory_weight = -0.5 * ((theta - target) / input_sigma) ** 2
    log_theory_weight -= float(np.max(log_theory_weight))
    joint_weights = chain.weights * np.exp(log_theory_weight)

    if chain.theta_name.endswith("*"):
        conditional_names = (
            "omegabh2",
            "omegach2",
            "theta",
            "tau",
            "logA",
            "ns",
            "H0*",
        )
    else:
        conditional_names = (
            "ombh2",
            "omch2",
            "cosmomc_theta",
            "tau",
            "logA",
            "ns",
            "nrun",
            "H0",
        )

    return {
        "label": chain.label,
        "source_model": chain.source_model,
        "convergence_note": chain.convergence_note,
        "source_files": [
            {"path": relative(path), "sha256": sha256(path)} for path in chain.files
        ],
        "rows": int(len(theta)),
        "sum_frequency_weights": float(np.sum(chain.weights)),
        "kish_effective_sample_size": effective_sample_size(chain.weights),
        "theta_star_100": {
            "weighted_mean": mean,
            "weighted_sigma": sigma,
            "weighted_quantiles_2p5_16_50_84_97p5": weighted_quantile(
                theta, chain.weights, (0.025, 0.16, 0.5, 0.84, 0.975)
            ),
            "ch0_minus_mean": residual,
            "ch0_z_fixed": z_fixed,
            "gaussian_profile_delta_chi2": delta_chi2,
            "delta_aic_if_one_parameter_is_removed": delta_chi2 - 2.0,
        },
        "theta_definition_guard": {
            "theta_star_100_minus_theta_mc_100_mean": weighted_mean(
                theta - theta_mc, chain.weights
            ),
            "theta_star_100_minus_theta_mc_100_sigma": weighted_std(
                theta - theta_mc, chain.weights
            ),
        },
        "ch0_with_laboratory_input_uncertainty": {
            "combined_residual_z": residual / math.sqrt(sigma**2 + input_sigma**2),
            "importance_reweighted_theta_star_100_mean": weighted_mean(
                theta, joint_weights
            ),
            "importance_reweighted_theta_star_100_sigma": weighted_std(
                theta, joint_weights
            ),
            "importance_reweighted_kish_ess": effective_sample_size(joint_weights),
        },
        "gaussian_conditional_parameter_shifts": gaussian_conditionals(
            chain, target, conditional_names
        ),
        "method_boundary": (
            "The delta-chi2 is the local multivariate-Gaussian profile penalty "
            "inferred from a posterior chain. It is not a fresh constrained "
            "likelihood minimization, a Bayes factor, or evidence that accounts "
            "for the post-search construction of the CH0-selected acoustic package."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    prediction = ch0_prediction()
    chains = (
        load_planck_chain(
            "plikHM_TTTEEE_lowl_lowE",
            "Planck PR3 TT,TE,EE+lowl+lowE",
        ),
        load_planck_chain(
            "plikHM_TTTEEE_lowl_lowE_lensing",
            "Planck PR3 TT,TE,EE+lowl+lowE+lensing",
        ),
        load_cobaya_chain(
            "actlite_nrun_camb",
            "actlite_nrun_camb",
            "ACT DR6 TT,TE,EE+Planck lowE, nrun extension",
        ),
        load_cobaya_chain(
            "p-actlite_nrun_camb",
            "p-actlite_nrun_camb",
            "Planck high-l cut+ACT DR6+Planck lowT/lowE, nrun extension",
        ),
        load_cobaya_chain(
            "p-actlite-l-b_nrun_camb",
            "p-actlite-l-b_nrun_camb",
            "Planck+ACT DR6+lensing+DESI BAO, nrun extension",
        ),
    )
    result = {
        "schema_version": 1,
        "test": "CH0-selected package fixed physical acoustic angle chain test",
        "prediction": prediction,
        "parameterization": {
            "fixed_quantity": "physical CAMB theta_star = r_s(z_tau=1)/D_M(z_tau=1)",
            "constrained_coordinate": prediction["theta_star"],
            "archived_chain_coordinate": (
                "theta_MC/cosmomc_theta was sampled; physical theta_star was "
                "derived and is the coordinate conditioned here"
            ),
            "method": (
                "local Gaussian profile surrogate in derived physical theta_star; "
                "not an exact-theta rerun of the archived likelihood"
            ),
            "base_planck_reduction_interpreted": (
                "six to five cosmological coordinates, with H0 re-solved in a "
                "future exact constrained run"
            ),
            "act_extension_warning": (
                "the archived ACT diagnostics include nrun and therefore do not "
                "instantiate the base six-to-five comparison"
            ),
        },
        "datasets": [summarize(chain, prediction) for chain in chains],
    }

    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
