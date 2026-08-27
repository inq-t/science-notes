"""Paired ACT DR6 spectrum-profile test of the CH0 acoustic constraint.

This is a direct fit to the archived scientific ACT DR6 foreground-marginalized
TT/TE/EE SACC data.  Both arms use CAMB's physical ``thetastar`` input.  The
baseline samples that coordinate; the CH0 arm fixes it and otherwise changes
nothing.  A Gaussian tau proxy stands in for the Planck lowE block, so this is
an internally paired transfer test rather than a reproduction of the archived
ACT+Planck likelihood.

Runtime dependencies: CAMB 1.6.6, SciPy, and SACC.  They are deliberately not
vendored in this repository.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from acoustic_receipts import acoustic_from_quality, minimal_chiral_quality


MODULE = Path(__file__).resolve().parent
REPO = MODULE.parent
DATA = (
    REPO
    / "causal-wall-spectral-theory"
    / "sources"
    / "data"
    / "act-dr6"
    / "dr6_data_cmbonly"
    / "v1.0"
    / "dr6_data_cmbonly.fits"
)
LIKELIHOOD_SOURCE = (
    REPO
    / "causal-wall-spectral-theory"
    / "sources"
    / "code"
    / "act-dr6-cmbonly-627aeafb"
    / "DR6-ACT-lite-627aeafb88ae5ad1aa66b406bea2d65cfa66a27d"
    / "act_dr6_cmbonly"
    / "act_dr6_cmbonly.py"
)
ANALYSIS_CONFIG = (
    REPO
    / "causal-wall-spectral-theory"
    / "sources"
    / "data"
    / "act-dr6"
    / "actlite_nrun_camb"
    / "actlite_nrun_camb"
    / "actlite_nrun_camb.updated.yaml"
)

CH0_THETA = acoustic_from_quality(minimal_chiral_quality(130.2))[1] / 100.0
LMIN = 600
LMAX = 8500
LMAX_THEORY = 9000
TAU_PRIOR_MEAN = 0.0544
TAU_PRIOR_SIGMA = 0.0073
A_ACT_PRIOR_MEAN = 1.0
A_ACT_PRIOR_SIGMA = 0.003

BASE_NAMES = (
    "ombh2",
    "omch2",
    "thetastar",
    "logA",
    "ns",
    "tau",
    "A_act",
    "P_act",
)
FIXED_NAMES = tuple(name for name in BASE_NAMES if name != "thetastar")

LOWER = np.array([0.017, 0.09, 0.0103, 2.6, 0.9, 0.0, 0.5, 0.9])
UPPER = np.array([0.027, 0.15, 0.0105, 3.5, 1.1, 0.1, 1.5, 1.1])
SCALE = np.array([2.0e-4, 2.0e-3, 4.0e-6, 0.02, 0.01, 0.008, 0.003, 0.003])
DIFFERENCE_STEP = np.array(
    [3.0e-5, 3.0e-4, 5.0e-7, 3.0e-3, 1.5e-3, 2.0e-3, 5.0e-4, 5.0e-4]
)

# Gaussian conditioning of the archived ACT+nrun chain to nrun=0 supplies only
# the optimizer start.  It does not enter the objective or the result.
START = np.array(
    [
        0.0225799258,
        0.1238546895,
        0.01040745894,
        3.0514063032,
        0.9665280912,
        0.0558285941,
        0.9996386148,
        0.9997540271,
    ]
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


@dataclass
class SpectrumBlock:
    pol: str
    indices: np.ndarray
    window_ells: np.ndarray
    window: np.ndarray


class ACTProfile:
    def __init__(self) -> None:
        import sacc
        from scipy.linalg import solve_triangular

        self.solve_triangular = solve_triangular
        archive = sacc.Sacc.load_fits(str(DATA))
        pol_types = {"tt": "cl_00", "te": "cl_0e", "ee": "cl_ee"}
        blocks: list[SpectrumBlock] = []
        selected: list[int] = []

        for pol, data_type in pol_types.items():
            for tracer1, tracer2 in archive.get_tracer_combinations(data_type):
                ells, _, indices = archive.get_ell_cl(
                    data_type, tracer1, tracer2, return_ind=True
                )
                mask = np.logical_and(ells >= LMIN, ells <= LMAX)
                kept = np.asarray(indices[mask], dtype=int)
                if len(kept) == 0:
                    continue
                windows = archive.get_bandpower_windows(kept)
                blocks.append(
                    SpectrumBlock(
                        pol=pol,
                        indices=kept,
                        window_ells=np.asarray(windows.values, dtype=int),
                        window=np.asarray(windows.weight.T),
                    )
                )
                selected.extend(int(index) for index in kept)

        self.blocks = blocks
        self.selected = np.asarray(sorted(selected), dtype=int)
        self.position = {
            int(index): position for position, index in enumerate(self.selected)
        }
        self.data = np.asarray(archive.mean)[self.selected]
        covariance = archive.covariance.covmat[np.ix_(self.selected, self.selected)]
        self.cholesky = np.linalg.cholesky(covariance)
        self.last_cosmology: tuple[float, ...] | None = None
        self.last_cls: dict[str, np.ndarray] | None = None
        self.camb_calls = 0
        self.theta_background_calls = 0

    @staticmethod
    def unpack(names: tuple[str, ...], values: np.ndarray) -> dict[str, float]:
        result = dict(zip(names, (float(value) for value in values), strict=True))
        result.setdefault("thetastar", CH0_THETA)
        return result

    def spectra(self, parameters: dict[str, float]) -> dict[str, np.ndarray]:
        import camb
        from scipy.optimize import brentq

        cosmology = tuple(parameters[name] for name in BASE_NAMES[:6])
        if cosmology == self.last_cosmology and self.last_cls is not None:
            return self.last_cls

        common = dict(
            ombh2=parameters["ombh2"],
            omch2=parameters["omch2"],
            omk=0.0,
            As=1.0e-10 * math.exp(parameters["logA"]),
            ns=parameters["ns"],
            tau=parameters["tau"],
            mnu=0.06,
            nnu=3.044,
            num_massive_neutrinos=1,
            neutrino_hierarchy="degenerate",
            lmax=LMAX_THEORY,
            kmax=10.0,
            lens_potential_accuracy=1,
            nonlinear=True,
        )
        approximate = camb.set_params(
            thetastar=parameters["thetastar"], **common
        )
        approximate_h0 = float(approximate.H0)

        def theta_residual(h0: float) -> float:
            trial = camb.set_params(H0=h0, **common)
            background = camb.get_background(trial)
            self.theta_background_calls += 1
            return (
                float(background.get_derived_params()["thetastar"]) / 100.0
                - parameters["thetastar"]
            )

        h0 = brentq(
            theta_residual,
            max(10.0, approximate_h0 - 1.0),
            min(100.0, approximate_h0 + 1.0),
            xtol=1.0e-10,
            rtol=1.0e-12,
        )
        pars = camb.set_params(H0=h0, **common)
        results = camb.get_results(pars)
        total = results.get_cmb_power_spectra(
            pars, CMB_unit="muK", raw_cl=False
        )["total"]
        self.last_h0 = float(pars.H0)
        self.last_theta_100 = float(results.get_derived_params()["thetastar"])
        self.last_cls = {
            "tt": total[:, 0],
            "ee": total[:, 1],
            "te": total[:, 3],
        }
        self.last_cosmology = cosmology
        self.camb_calls += 1
        return self.last_cls

    def model_vector(self, parameters: dict[str, float]) -> np.ndarray:
        cls = self.spectra(parameters)
        model = np.zeros_like(self.data)
        for block in self.blocks:
            values = cls[block.pol][block.window_ells] / parameters["A_act"] ** 2
            if "e" in block.pol:
                values /= parameters["P_act"]
            if block.pol == "ee":
                values /= parameters["P_act"]
            projected = block.window @ values
            positions = [self.position[int(index)] for index in block.indices]
            model[positions] = projected
        return model

    def residuals(self, names: tuple[str, ...], values: np.ndarray) -> np.ndarray:
        parameters = self.unpack(names, values)
        delta = self.data - self.model_vector(parameters)
        spectral = self.solve_triangular(
            self.cholesky, delta, lower=True, check_finite=False
        )
        priors = np.array(
            [
                (parameters["tau"] - TAU_PRIOR_MEAN) / TAU_PRIOR_SIGMA,
                (parameters["A_act"] - A_ACT_PRIOR_MEAN) / A_ACT_PRIOR_SIGMA,
            ]
        )
        return np.concatenate((spectral, priors))

    def jacobian(self, names: tuple[str, ...], values: np.ndarray) -> np.ndarray:
        """Central finite differences with steps larger than CAMB's noise floor."""
        lower, upper, _ = bounds_for(names)
        base_indices = [BASE_NAMES.index(name) for name in names]
        steps = DIFFERENCE_STEP[base_indices]
        base = self.residuals(names, values)
        jacobian = np.empty((len(base), len(values)))

        # Do the two calibration directions first; the cached spectrum is then
        # reused for all four nuisance-only residual calls.
        order = sorted(
            range(len(names)), key=lambda index: names[index] not in {"A_act", "P_act"}
        )
        for index in order:
            step = steps[index]
            plus = values.copy()
            minus = values.copy()
            plus[index] = min(values[index] + step, upper[index])
            minus[index] = max(values[index] - step, lower[index])
            numerator = self.residuals(names, plus) - self.residuals(names, minus)
            jacobian[:, index] = numerator / (plus[index] - minus[index])
        return jacobian

    def describe(self, names: tuple[str, ...], values: np.ndarray) -> dict[str, object]:
        parameters = self.unpack(names, values)
        residuals = self.residuals(names, values)
        spectral = residuals[:-2]
        prior = residuals[-2:]
        # Ensure cached derived values correspond to the reported point.
        self.spectra(parameters)
        return {
            "parameters": parameters,
            "derived_H0_km_s_Mpc": self.last_h0,
            "returned_theta_star_100": self.last_theta_100,
            "theta_solver_residual_100": self.last_theta_100
            - 100.0 * parameters["thetastar"],
            "chi2_spectra": float(spectral @ spectral),
            "chi2_tau_proxy": float(prior[0] ** 2),
            "chi2_A_act_prior": float(prior[1] ** 2),
            "chi2_total": float(residuals @ residuals),
        }


def bounds_for(names: tuple[str, ...]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    indices = np.array([BASE_NAMES.index(name) for name in names], dtype=int)
    return LOWER[indices], UPPER[indices], SCALE[indices]


def fit(
    profile: ACTProfile,
    names: tuple[str, ...],
    start: np.ndarray,
    max_nfev: int,
) -> tuple[object, dict[str, object]]:
    from scipy.optimize import least_squares

    lower, upper, scale = bounds_for(names)
    result = least_squares(
        lambda values: profile.residuals(names, values),
        start,
        bounds=(lower, upper),
        x_scale=scale,
        jac=lambda values: profile.jacobian(names, values),
        ftol=1.0e-9,
        xtol=1.0e-9,
        gtol=1.0e-5,
        max_nfev=max_nfev,
        verbose=1,
    )
    description = profile.describe(names, result.x)
    description.update(
        {
            "success": bool(result.success),
            "message": str(result.message),
            "optimizer_function_evaluations": int(result.nfev),
            "optimizer_jacobian_evaluations": int(result.njev or 0),
            "optimality": float(result.optimality),
        }
    )
    return result, description


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--max-nfev", type=int, default=80)
    args = parser.parse_args()

    profile = ACTProfile()
    baseline_result, baseline = fit(profile, BASE_NAMES, START, args.max_nfev)

    fixed_start = np.array(
        [baseline_result.x[BASE_NAMES.index(name)] for name in FIXED_NAMES]
    )
    fixed_result, fixed = fit(profile, FIXED_NAMES, fixed_start, args.max_nfev)

    delta_chi2 = fixed["chi2_total"] - baseline["chi2_total"]
    theta_displacement_100 = 100.0 * (
        fixed["parameters"]["thetastar"]
        - baseline["parameters"]["thetastar"]
    )
    result = {
        "schema_version": 1,
        "test": "paired ACT DR6 full-spectrum CH0 profile transfer",
        "status": (
            "fresh paired likelihood transfer; not a Planck-clik or archived "
            "ACT+Planck lowE reproduction"
        ),
        "data": {
            "path": DATA.relative_to(REPO).as_posix(),
            "sha256": sha256(DATA),
            "likelihood_source": {
                "path": LIKELIHOOD_SOURCE.relative_to(REPO).as_posix(),
                "sha256": sha256(LIKELIHOOD_SOURCE),
            },
            "analysis_config_with_ell_8500_override": {
                "path": ANALYSIS_CONFIG.relative_to(REPO).as_posix(),
                "sha256": sha256(ANALYSIS_CONFIG),
            },
            "selected_bandpowers": int(len(profile.data)),
            "spectra": ["TT", "TE", "EE"],
            "ell_range": [LMIN, LMAX],
        },
        "software": {
            name: importlib.metadata.version(name)
            for name in ("camb", "scipy", "sacc", "numpy")
        },
        "theory_and_likelihood": {
            "background": "flat six-parameter LambdaCDM transfer",
            "spatial_curvature": 0.0,
            "nnu": 3.044,
            "mnu_eV": 0.06,
            "recombination": "stock CAMB 1.6.6 default, not archived CosmoRec",
            "theta_coordinate": "physical CAMB thetastar",
            "theta_star_fixed": CH0_THETA,
            "theta_solver": (
                "external Brent root of full CAMB physical thetastar in H0; "
                "xtol=1e-10 km/s/Mpc, rtol=1e-12"
            ),
            "num_massive_neutrinos": 1,
            "neutrino_hierarchy": "degenerate",
            "tau_block": {
                "kind": "Gaussian proxy for Planck lowE",
                "mean": TAU_PRIOR_MEAN,
                "sigma": TAU_PRIOR_SIGMA,
            },
            "calibration_prior": {
                "parameter": "A_act",
                "mean": A_ACT_PRIOR_MEAN,
                "sigma": A_ACT_PRIOR_SIGMA,
            },
            "camb_lmax": LMAX_THEORY,
            "lens_potential_accuracy": 1,
            "kmax": 10.0,
            "nonlinear_lensing": True,
        },
        "baseline": baseline,
        "ch0_fixed": fixed,
        "comparison": {
            "delta_chi2_fixed_minus_baseline": delta_chi2,
            "delta_aic_for_one_fewer_parameter": delta_chi2 - 2.0,
            "theta_star_100_displacement": theta_displacement_100,
            "implied_local_profile_sigma_theta_star_100": abs(
                theta_displacement_100
            )
            / math.sqrt(delta_chi2),
            "camb_spectrum_calls": profile.camb_calls,
            "camb_theta_background_calls": profile.theta_background_calls,
        },
        "interpretive_boundary": (
            "This tests whether fixing the physical acoustic angle damages an "
            "ACT TT/TE/EE spectrum fit under an economical LambdaCDM transfer. "
            "It does not test the unconstructed cosmodynamic perturbation law, "
            "supply a look-elsewhere correction, or make CH0 prospective."
        ),
    }

    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
