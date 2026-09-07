"""Finite checks for the exact Gaussian bridge-gap calibration.

The receipt verifies Gaussian regression, the tanh bridge floor, Hermite
spectra, product tensorization, optimal relative quasi-factorization, and
rate reconstruction for a finite family of independent modes. It is not
evidence for an interacting Yang--Mills bridge estimate.

The added lattice checks use continuous Euclidean time and an actual dense
spatial covariance Schur complement. Massless zero modes are removed by an
orthonormal zero-mean quotient, never by a small-mass regularization. The
larger infrared and thickness scans evaluate Fourier formulas only.
"""

from __future__ import annotations

import math

import numpy as np


TOL = 2.0e-12
ELL = 1.2
FREQUENCIES = np.array([0.35, 0.9, 1.7], dtype=float)
HERMITE_DEPTH = 12
LATTICE_TOL = 2.0e-10
SOLVE_TOL = 2.0e-12


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


def lattice_frequencies(spatial_dimension: int, size: int, mass: float) -> np.ndarray:
    """Periodic nearest-neighbor spatial lattice, spacing a=1."""
    axes = np.indices((size,) * spatial_dimension, dtype=float)
    return np.sqrt(mass * mass + 4.0 * np.sum(np.sin(np.pi * axes / size) ** 2, axis=0))


def covariance_weights(frequencies: np.ndarray, time: float) -> np.ndarray:
    weights = np.zeros_like(frequencies)
    positive = frequencies > 0.0
    weights[positive] = np.exp(-abs(time) * frequencies[positive]) / (
        2.0 * frequencies[positive]
    )
    return weights


def covariance_from_weights(weights: np.ndarray) -> np.ndarray:
    """Real inverse DFT, then the full position-space circulant matrix."""
    kernel = np.fft.ifftn(weights)
    assert np.max(np.abs(kernel.imag)) < LATTICE_TOL
    shape = weights.shape
    positions = np.array(list(np.ndindex(shape)), dtype=int)
    differences = (positions[:, None, :] - positions[None, :, :]) % np.array(shape)
    indices = tuple(differences[:, :, axis] for axis in range(weights.ndim))
    covariance = kernel.real[indices]
    assert np.linalg.norm(covariance - covariance.T) < LATTICE_TOL
    return covariance


def zero_mean_basis(size: int) -> np.ndarray:
    """Helmert contrasts: columns orthonormal and orthogonal to constants."""
    basis = np.zeros((size, size - 1))
    for j in range(1, size):
        normalization = math.sqrt(j * (j + 1))
        basis[:j, j - 1] = 1.0 / normalization
        basis[j, j - 1] = -j / normalization
    assert np.linalg.norm(basis.T @ basis - np.eye(size - 1)) < LATTICE_TOL
    assert np.linalg.norm(basis.T @ np.ones(size)) < LATTICE_TOL
    return basis


def modal_lattice_data(
    spatial_dimension: int, size: int, mass: float, ell: float
) -> tuple[float, float, int]:
    frequencies = lattice_frequencies(spatial_dimension, size, mass)
    positive = frequencies[frequencies > 0.0]
    weights = 1.0 / (2.0 * positive)
    residues = np.tanh(ell * positive)
    floor = float(np.min(residues))
    single_point = float(np.sum(weights * residues) / np.sum(weights))
    return floor, single_point, len(positive)


def dense_lattice_data(
    spatial_dimension: int, size: int, mass: float, ell: float
) -> tuple[float, float, int]:
    frequencies = lattice_frequencies(spatial_dimension, size, mass)
    full_covariances = [
        covariance_from_weights(covariance_weights(frequencies, time))
        for time in (0.0, ell, 2.0 * ell)
    ]
    sites = size**spatial_dimension
    if mass == 0.0:
        assert np.count_nonzero(frequencies == 0.0) == 1
        basis = zero_mean_basis(sites)
        for covariance in full_covariances:
            assert np.linalg.norm(covariance @ np.ones(sites)) < LATTICE_TOL
    else:
        assert np.all(frequencies > 0.0)
        basis = np.eye(sites)

    covariance, propagated, twice_propagated = [
        basis.T @ item @ basis for item in full_covariances
    ]
    boundary = np.block(
        [[covariance, twice_propagated], [twice_propagated, covariance]]
    )
    cross = np.hstack((propagated, propagated))
    assert np.linalg.norm(boundary - boundary.T) < LATTICE_TOL
    np.linalg.cholesky(boundary)
    solution = np.linalg.solve(boundary, cross.T)
    relative_residual = np.linalg.norm(boundary @ solution - cross.T) / np.linalg.norm(cross)
    assert relative_residual < SOLVE_TOL
    schur = covariance - cross @ solution
    assert np.linalg.norm(schur - schur.T) < LATTICE_TOL
    schur = (schur + schur.T) / 2.0
    np.linalg.cholesky(schur)

    # Congruence by the Cholesky inverse has the normalized Schur spectrum.
    # It is orthogonally equivalent to whitening by covariance**(-1/2).
    cholesky = np.linalg.cholesky(covariance)
    left_whitened = np.linalg.solve(cholesky, schur)
    normalized = np.linalg.solve(cholesky, left_whitened.T).T
    assert np.linalg.norm(normalized - normalized.T) < LATTICE_TOL
    eigenvalues = np.linalg.eigvalsh((normalized + normalized.T) / 2.0)
    assert 0.0 < float(eigenvalues[0]) <= float(eigenvalues[-1]) < 1.0

    # Independent modal prediction tests the entire Schur matrix and spectrum,
    # not just the lowest eigenvalue subsequently printed.
    expected_weights = covariance_weights(frequencies, 0.0) * np.tanh(ell * frequencies)
    expected_full = covariance_from_weights(expected_weights)
    expected_schur = basis.T @ expected_full @ basis
    assert np.linalg.norm(schur - expected_schur) / np.linalg.norm(schur) < LATTICE_TOL
    positive = frequencies[frequencies > 0.0]
    expected_spectrum = np.sort(np.tanh(ell * positive))
    assert np.max(np.abs(eigenvalues - expected_spectrum)) < LATTICE_TOL

    # This is one midpoint site's prediction error against the FULL boundary
    # slices. It is a test-vector quotient, not the complete L2 response floor.
    full_schur = basis @ schur @ basis.T
    point_ratios = np.diag(full_schur) / np.diag(full_covariances[0])
    single_point = float(point_ratios[0])
    assert np.max(np.abs(point_ratios - single_point)) < LATTICE_TOL
    modal_floor, modal_point, retained_modes = modal_lattice_data(
        spatial_dimension, size, mass, ell
    )
    floor = float(eigenvalues[0])
    assert abs(floor - modal_floor) < LATTICE_TOL
    assert abs(single_point - modal_point) < LATTICE_TOL
    assert single_point > floor + 1.0e-8
    return floor, single_point, retained_modes


def lattice_receipt() -> None:
    print()
    print("Finite spatial lattice: continuous Euclidean time, a=1, ell=1")
    print("Dense covariance Schur solves; full midpoint and two full boundary slices")
    print("m=0: exact constant mode removed by orthonormal zero-mean contrasts")
    dense_cases = [(1, size) for size in (8, 16, 32)] + [(3, size) for size in (4, 6)]
    for spatial_dimension, size in dense_cases:
        for mass in (0.0, 0.3):
            floor, point, retained_modes = dense_lattice_data(
                spatial_dimension, size, mass, 1.0
            )
            print(
                f"dense s={spatial_dimension}, N={size:2d}, m={mass:.1f}, "
                f"modes={retained_modes:3d}: floor={floor:.12f}, "
                f"single-point/full-boundary={point:.12f}"
            )
    print(
        "PASS: 10 dense Schur solves, positivity, full spectra, zero-mode quotients, "
        "and single-point checks"
    )
    print("Solver relative residual < 2e-12; matrix/spectrum tolerance = 2e-10")
    print()
    print("Fourier-only infrared scan: ell=1 (not additional dense Schur solves)")
    for spatial_dimension in (1, 3):
        for mass in (0.0, 0.3):
            previous_floor = 1.0
            for size in (8, 16, 32, 64):
                floor, point, _ = modal_lattice_data(spatial_dimension, size, mass, 1.0)
                if mass == 0.0:
                    assert floor < previous_floor
                else:
                    assert abs(floor - math.tanh(mass)) < TOL
                previous_floor = floor
                print(
                    f"modal s={spatial_dimension}, N={size:2d}, m={mass:.1f}: "
                    f"floor={floor:.12f}, single-point/full-boundary={point:.12f}"
                )
    print()
    print("Fourier-only thickness scan: N=16 (not additional dense Schur solves)")
    for spatial_dimension in (1, 3):
        for mass in (0.0, 0.3):
            previous_floor = previous_point = 0.0
            for ell in (0.25, 1.0, 4.0):
                floor, point, _ = modal_lattice_data(spatial_dimension, 16, mass, ell)
                assert floor > previous_floor and point > previous_point
                previous_floor, previous_point = floor, point
                print(
                    f"modal s={spatial_dimension}, N=16, m={mass:.1f}, ell={ell:.2f}: "
                    f"floor={floor:.12f}, single-point/full-boundary={point:.12f}"
                )
    print("PASS: 16 modal infrared evaluations and 12 modal thickness evaluations")
    print("The full L2 floor uses the proved Gaussian Hermite extension, not a finite-chaos test.")
    print("Finite Gaussian calibration only: no interacting or continuum Yang--Mills gap is proved.")


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
    lattice_receipt()


if __name__ == "__main__":
    main()
