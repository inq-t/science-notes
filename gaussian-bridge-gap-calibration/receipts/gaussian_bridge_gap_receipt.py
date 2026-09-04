"""Finite checks for the exact Gaussian bridge-gap calibration.

The receipt verifies Gaussian regression, the tanh bridge floor, Hermite
spectra, product tensorization, optimal relative quasi-factorization, and
rate reconstruction for a finite family of independent modes. It is not
evidence for an interacting Yang--Mills bridge estimate.
"""

from __future__ import annotations

import math

import numpy as np


TOL = 2.0e-12
ELL = 1.2
FREQUENCIES = np.array([0.35, 0.9, 1.7], dtype=float)
HERMITE_DEPTH = 12


def mode_data(omega: float) -> dict[str, float]:
    r = math.exp(-omega * ELL)
    endpoint_covariance = np.array(
        [[1.0, r * r], [r * r, 1.0]], dtype=float
    )
    middle_endpoint_covariance = np.array([r, r], dtype=float)
    predictor_variance = float(
        middle_endpoint_covariance
        @ np.linalg.solve(
            endpoint_covariance, middle_endpoint_covariance
        )
    )
    residual = 1.0 - predictor_variance
    expected_residual = math.tanh(omega * ELL)

    q_squared = predictor_variance
    bridge_spectrum = np.array(
        [1.0 - q_squared**k for k in range(1, HERMITE_DEPTH + 1)]
    )
    transfer_defect = np.array(
        [1.0 - r ** (2 * k) for k in range(1, HERMITE_DEPTH + 1)]
    )
    relative_ratios = transfer_defect / bridge_spectrum
    optimal_quasi_factor = 1.0 + r * r
    reconstructed = math.atanh(residual) / ELL
    generic_lower_bound = -math.log(1.0 - residual) / (2.0 * ELL)

    return {
        "r": r,
        "q_squared": q_squared,
        "residual": residual,
        "tanh_error": abs(residual - expected_residual),
        "bridge_floor_error": abs(min(bridge_spectrum) - residual),
        "quasi_factor_error": abs(
            max(relative_ratios) - optimal_quasi_factor
        ),
        "reconstruction_error": abs(reconstructed - omega),
        "generic_lower_bound": generic_lower_bound,
    }


def main() -> None:
    modes = [mode_data(float(omega)) for omega in FREQUENCIES]
    local_floors = np.array([mode["residual"] for mode in modes])
    local_q_squared = np.array([mode["q_squared"] for mode in modes])

    product_floor = 1.0 - float(np.max(local_q_squared))
    expected_product_floor = math.tanh(
        float(np.min(FREQUENCIES)) * ELL
    )
    reconstructed_minimum = math.atanh(product_floor) / ELL

    for omega, mode in zip(FREQUENCIES, modes, strict=True):
        assert mode["tanh_error"] < TOL
        assert mode["bridge_floor_error"] < TOL
        assert mode["quasi_factor_error"] < TOL
        assert mode["reconstruction_error"] < TOL
        assert mode["generic_lower_bound"] <= float(omega) + TOL

    assert abs(product_floor - min(local_floors)) < TOL
    assert abs(product_floor - expected_product_floor) < TOL
    assert abs(reconstructed_minimum - min(FREQUENCIES)) < TOL

    print("Gaussian bridge-gap calibration: finite-mode receipt")
    print(f"half-slab length = {ELL:.6f}")
    for omega, mode in zip(FREQUENCIES, modes, strict=True):
        print(
            f"omega={omega:.6f}: r={mode['r']:.12f}, "
            f"q^2={mode['q_squared']:.12f}, "
            f"kappa={mode['residual']:.12f}, "
            f"generic-bound={mode['generic_lower_bound']:.12f}"
        )
    print(f"product bridge floor = {product_floor:.12f}")
    print(
        "reconstructed minimum frequency = "
        f"{reconstructed_minimum:.12f}"
    )
    print(
        "maximum tanh identity error = "
        f"{max(mode['tanh_error'] for mode in modes):.3e}"
    )
    print(
        "maximum Hermite-floor error = "
        f"{max(mode['bridge_floor_error'] for mode in modes):.3e}"
    )
    print(
        "maximum quasi-factorization error = "
        f"{max(mode['quasi_factor_error'] for mode in modes):.3e}"
    )
    print(
        "maximum rate-reconstruction error = "
        f"{max(mode['reconstruction_error'] for mode in modes):.3e}"
    )
    print(
        "PASS: dimensionless bridge geometry reconstructs the Gaussian "
        "inverse-length gap"
    )


if __name__ == "__main__":
    main()
