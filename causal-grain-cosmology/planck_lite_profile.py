"""Paired Planck Plik-lite spectrum-profile test of the CH0 constraint.

This is a transparent Python port of the archived ``plik_cmbonly.f90``
Gaussian TT/TE/EE likelihood.  Plik-lite has already marginalized the full
high-ell foreground nuisance model into its 613-bin covariance.  Both arms use
CAMB's physical ``thetastar`` coordinate; CH0 removes only that coordinate.

A Gaussian tau proxy stands in for lowE, and neither Commander low-l TT nor
Planck lensing is included here.  The official full-likelihood chains are
tested separately by ``cmb_nested_test.py``.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import math
import struct
from pathlib import Path

import numpy as np

from acoustic_receipts import acoustic_from_quality, minimal_chiral_quality


MODULE = Path(__file__).resolve().parent
REPO = MODULE.parent
EXTERNAL = (
    REPO
    / "causal-wall-spectral-theory"
    / "sources"
    / "data"
    / "planck-2018"
    / "clik-data-baseline-r3"
    / "baseline"
    / "plc_3.0"
    / "hi_l"
    / "plik_lite"
    / "plik_lite_v22_TTTEEE.clik"
    / "clik"
    / "lkl_0"
    / "_external"
)
FORTRAN_SOURCE = (
    REPO
    / "causal-wall-spectral-theory"
    / "sources"
    / "data"
    / "planck-2018"
    / "clik-code-v3"
    / "code"
    / "plc_3.0"
    / "plc-3.01"
    / "src"
    / "cmbonly"
    / "plik_cmbonly.f90"
)

LIKE_DATA = EXTERNAL / "cl_cmb_plik_v22.dat"
COVARIANCE = EXTERNAL / "c_matrix_plik_v22.dat"
BIN_MIN = EXTERNAL / "blmin.dat"
BIN_MAX = EXTERNAL / "blmax.dat"
BIN_WEIGHT = EXTERNAL / "bweight.dat"
CHECK_PARAM = EXTERNAL.parent.parent / "check_param"
CHECK_METADATA = EXTERNAL.parent.parent / "_mdb"

CH0_THETA = acoustic_from_quality(minimal_chiral_quality(130.2))[1] / 100.0
PLMIN = 30
NBIN_TT = 215
NBIN_TE = 199
NBIN_EE = 199
NBIN = NBIN_TT + NBIN_TE + NBIN_EE
LMAX_THEORY = 3000
TAU_PRIOR_MEAN = 0.0544
TAU_PRIOR_SIGMA = 0.0073
CAL_PRIOR_MEAN = 1.0
CAL_PRIOR_SIGMA = 0.0025

BASE_NAMES = (
    "ombh2",
    "omch2",
    "thetastar",
    "logA",
    "ns",
    "tau",
    "calPlanck",
)
FIXED_NAMES = tuple(name for name in BASE_NAMES if name != "thetastar")
LOWER = np.array([0.017, 0.09, 0.0103, 2.6, 0.9, 0.0, 0.9])
UPPER = np.array([0.027, 0.15, 0.0105, 3.5, 1.1, 0.1, 1.1])
SCALE = np.array([1.5e-4, 1.3e-3, 3.0e-6, 0.016, 0.005, 0.008, 0.0025])
DIFFERENCE_STEP = np.array([2e-5, 2e-4, 3e-7, 2e-3, 8e-4, 1.5e-3, 4e-4])
START = np.array(
    [
        0.0223445482,
        0.1206136762,
        0.01041048417,
        3.0548826113,
        0.9631161915,
        0.0586953475,
        1.0005019093,
    ]
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_fortran_covariance(path: Path) -> np.ndarray:
    raw = path.read_bytes()
    record_size = NBIN * NBIN * 8
    if len(raw) != record_size + 8:
        raise ValueError(f"unexpected covariance byte count: {len(raw)}")
    if struct.unpack("<i", raw[:4])[0] != record_size:
        raise ValueError("invalid leading Fortran record marker")
    if struct.unpack("<i", raw[-4:])[0] != record_size:
        raise ValueError("invalid trailing Fortran record marker")
    upper = np.frombuffer(raw[4:-4], dtype="<f8").reshape(
        (NBIN, NBIN), order="F"
    ).copy()
    lower_indices = np.tril_indices(NBIN, -1)
    upper[lower_indices] = upper.T[lower_indices]
    return upper


class PlikLiteProfile:
    def __init__(self) -> None:
        from scipy.linalg import solve_triangular

        self.solve_triangular = solve_triangular
        table = np.loadtxt(LIKE_DATA)
        if table.shape != (NBIN, 3):
            raise ValueError(f"unexpected likelihood table shape: {table.shape}")
        self.data = table[:, 1]
        self.bin_min = np.loadtxt(BIN_MIN).astype(int)[:NBIN_TT]
        self.bin_max = np.loadtxt(BIN_MAX).astype(int)[:NBIN_TT]
        # The v22 file carries additional blocks; the archived Fortran reader
        # consumes exactly the first 0:plmax block for this CMB-only likelihood.
        self.bin_weight = np.loadtxt(BIN_WEIGHT)[:2509]
        self.cholesky = np.linalg.cholesky(load_fortran_covariance(COVARIANCE))
        self.port_validation = self.validate_embedded_checkpoint()
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
        ell = np.arange(len(total), dtype=float)
        factor = np.ones_like(ell)
        factor[2:] = 2.0 * math.pi / (ell[2:] * (ell[2:] + 1.0))
        self.last_cls = {
            "tt": total[:, 0] * factor,
            "ee": total[:, 1] * factor,
            "te": total[:, 3] * factor,
        }
        self.last_cosmology = cosmology
        self.last_h0 = float(pars.H0)
        self.last_theta_100 = float(results.get_derived_params()["thetastar"])
        self.camb_calls += 1
        return self.last_cls

    def binned(self, spectrum: np.ndarray, count: int) -> np.ndarray:
        result = np.empty(count)
        for index in range(count):
            lo = int(self.bin_min[index])
            hi = int(self.bin_max[index])
            result[index] = np.sum(
                spectrum[PLMIN + lo : PLMIN + hi + 1]
                * self.bin_weight[lo : hi + 1]
            )
        return result

    def validate_embedded_checkpoint(self) -> dict[str, float]:
        """Reproduce the likelihood value embedded in the official clik file."""
        raw = CHECK_PARAM.read_bytes()
        # This specific clik checkpoint is a simple primary FITS image with one
        # 2880-byte header block and 7528 big-endian float64 values.
        check = np.frombuffer(raw, dtype=">f8", count=7528, offset=2880)
        tt = check[0:2509]
        ee = check[2509:5018]
        te = check[5018:7527]
        calibration = float(check[-1])
        model = np.concatenate(
            (
                self.binned(tt, NBIN_TT),
                self.binned(te, NBIN_TE),
                self.binned(ee, NBIN_EE),
            )
        ) / calibration**2
        residual = self.solve_triangular(
            self.cholesky, self.data - model, lower=True, check_finite=False
        )
        calculated = -0.5 * float(residual @ residual)
        metadata = CHECK_METADATA.read_text(encoding="ascii")
        expected = float(metadata.split("check_value float ", 1)[1].splitlines()[0])
        difference = calculated - expected
        if abs(difference) > 1.0e-7:
            raise AssertionError(
                f"Plik-lite port misses embedded check value by {difference}"
            )
        return {
            "expected_loglike": expected,
            "calculated_loglike": calculated,
            "difference": difference,
        }

    def model_vector(self, parameters: dict[str, float]) -> np.ndarray:
        spectra = self.spectra(parameters)
        calibration = parameters["calPlanck"] ** 2
        return np.concatenate(
            (
                self.binned(spectra["tt"], NBIN_TT),
                self.binned(spectra["te"], NBIN_TE),
                self.binned(spectra["ee"], NBIN_EE),
            )
        ) / calibration

    def residuals(self, names: tuple[str, ...], values: np.ndarray) -> np.ndarray:
        parameters = self.unpack(names, values)
        delta = self.data - self.model_vector(parameters)
        spectral = self.solve_triangular(
            self.cholesky, delta, lower=True, check_finite=False
        )
        priors = np.array(
            [
                (parameters["tau"] - TAU_PRIOR_MEAN) / TAU_PRIOR_SIGMA,
                (parameters["calPlanck"] - CAL_PRIOR_MEAN) / CAL_PRIOR_SIGMA,
            ]
        )
        return np.concatenate((spectral, priors))

    def jacobian(self, names: tuple[str, ...], values: np.ndarray) -> np.ndarray:
        lower, upper, _ = bounds_for(names)
        base_indices = [BASE_NAMES.index(name) for name in names]
        steps = DIFFERENCE_STEP[base_indices]
        base = self.residuals(names, values)
        jacobian = np.empty((len(base), len(values)))
        order = sorted(
            range(len(names)), key=lambda index: names[index] != "calPlanck"
        )
        for index in order:
            plus = values.copy()
            minus = values.copy()
            plus[index] = min(values[index] + steps[index], upper[index])
            minus[index] = max(values[index] - steps[index], lower[index])
            numerator = self.residuals(names, plus) - self.residuals(names, minus)
            jacobian[:, index] = numerator / (plus[index] - minus[index])
        return jacobian

    def describe(self, names: tuple[str, ...], values: np.ndarray) -> dict[str, object]:
        parameters = self.unpack(names, values)
        residuals = self.residuals(names, values)
        spectral = residuals[:-2]
        prior = residuals[-2:]
        self.spectra(parameters)
        return {
            "parameters": parameters,
            "derived_H0_km_s_Mpc": self.last_h0,
            "returned_theta_star_100": self.last_theta_100,
            "theta_solver_residual_100": self.last_theta_100
            - 100.0 * parameters["thetastar"],
            "chi2_plik_lite": float(spectral @ spectral),
            "chi2_tau_proxy": float(prior[0] ** 2),
            "chi2_calPlanck_prior": float(prior[1] ** 2),
            "chi2_total": float(residuals @ residuals),
        }


def bounds_for(names: tuple[str, ...]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    indices = np.array([BASE_NAMES.index(name) for name in names], dtype=int)
    return LOWER[indices], UPPER[indices], SCALE[indices]


def fit(
    profile: PlikLiteProfile,
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
    parser.add_argument("--max-nfev", type=int, default=40)
    args = parser.parse_args()

    profile = PlikLiteProfile()
    baseline_result, baseline = fit(profile, BASE_NAMES, START, args.max_nfev)
    fixed_start = np.array(
        [baseline_result.x[BASE_NAMES.index(name)] for name in FIXED_NAMES]
    )
    _, fixed = fit(profile, FIXED_NAMES, fixed_start, args.max_nfev)
    delta_chi2 = fixed["chi2_total"] - baseline["chi2_total"]
    theta_displacement_100 = 100.0 * (
        fixed["parameters"]["thetastar"]
        - baseline["parameters"]["thetastar"]
    )

    input_files = (
        LIKE_DATA,
        COVARIANCE,
        BIN_MIN,
        BIN_MAX,
        BIN_WEIGHT,
        CHECK_PARAM,
        CHECK_METADATA,
    )
    result = {
        "schema_version": 1,
        "test": "paired Planck Plik-lite TTTEEE CH0 profile transfer",
        "status": (
            "fresh paired marginalized-high-l likelihood transfer; not the full "
            "Plik nuisance likelihood, low-l likelihoods, or lensing"
        ),
        "data": {
            "bins": NBIN,
            "spectra": ["TT", "TE", "EE"],
            "input_files": [
                {
                    "path": path.relative_to(REPO).as_posix(),
                    "sha256": sha256(path),
                }
                for path in input_files
            ],
            "ported_likelihood_source": {
                "path": FORTRAN_SOURCE.relative_to(REPO).as_posix(),
                "sha256": sha256(FORTRAN_SOURCE),
            },
            "port_validation": profile.port_validation,
        },
        "software": {
            name: importlib.metadata.version(name)
            for name in ("camb", "scipy", "numpy")
        },
        "theory_and_likelihood": {
            "theta_coordinate": "physical CAMB thetastar",
            "theta_star_fixed": CH0_THETA,
            "theta_solver": (
                "external Brent root of full CAMB physical thetastar in H0; "
                "xtol=1e-10 km/s/Mpc, rtol=1e-12"
            ),
            "high_l_likelihood": "Planck PR3 Plik-lite v22 TTTEEE",
            "foreground_treatment": "already marginalized into Plik-lite covariance",
            "spatial_curvature": 0.0,
            "nnu": 3.044,
            "mnu_eV": 0.06,
            "num_massive_neutrinos": 1,
            "neutrino_hierarchy": "degenerate",
            "tau_block": {
                "kind": "Gaussian proxy for Planck lowE",
                "mean": TAU_PRIOR_MEAN,
                "sigma": TAU_PRIOR_SIGMA,
            },
            "calibration_prior": {
                "parameter": "calPlanck",
                "mean": CAL_PRIOR_MEAN,
                "sigma": CAL_PRIOR_SIGMA,
            },
            "recombination": "stock CAMB 1.6.6 default",
            "camb_lmax": LMAX_THEORY,
            "kmax": 10.0,
            "lens_potential_accuracy": 1,
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
            "The paired result tests the acoustic constraint against all 613 "
            "marginalized Planck high-l bins. The official full-chain surrogate "
            "remains the result that includes low-l, explicit Plik nuisance "
            "parameters, and lensing. Neither result corrects the post-search "
            "selection of CH0."
        ),
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
