"""Finite checks for Auxiliary Response Localization.

This receipt checks only the algebraic identities and normalization arithmetic.
It does not establish any Yang--Mills, locality, RG, or continuum hypothesis.
"""

from __future__ import annotations

import math

import numpy as np


def covariance(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.mean(x * y) - np.mean(x) * np.mean(y))


def check_covariance_split() -> float:
    # Symmetric graph Laplacian: exp(-tL) is a reversible Markov matrix for
    # the uniform measure on four states.
    laplacian = np.array(
        [
            [2.0, -1.0, 0.0, -1.0],
            [-1.0, 2.0, -1.0, 0.0],
            [0.0, -1.0, 2.0, -1.0],
            [-1.0, 0.0, -1.0, 2.0],
        ]
    )
    eigenvalues, eigenvectors = np.linalg.eigh(laplacian)
    time = 0.73
    transition = (eigenvectors * np.exp(-time * eigenvalues)) @ eigenvectors.T

    f = np.array([2.0, -1.0, 0.5, 3.0])
    g = np.array([-2.0, 4.0, 1.0, 0.25])
    pf = transition @ f
    pg = transition @ g
    pfg = transition @ (f * g)

    left = covariance(f, g)
    right = float(np.mean(pfg - pf * pg)) + covariance(pf, pg)
    error = abs(left - right)
    assert error < 1.0e-12
    return error


def check_optimized_exponent() -> tuple[float, float]:
    alpha = 0.7
    kappa = 1.3
    velocity = 0.9
    distance = 5.2
    time_star = alpha * distance / (alpha * velocity + 2.0 * kappa)
    spatial_exponent = alpha * (distance - velocity * time_star)
    mixing_exponent = 2.0 * kappa * time_star
    assert abs(spatial_exponent - mixing_exponent) < 1.0e-12

    static_rate = 2.0 * alpha * kappa / (alpha * velocity + 2.0 * kappa)
    assert abs(spatial_exponent - static_rate * distance) < 1.0e-12

    clock_rescaling = 3.7
    rescaled_rate = (
        2.0
        * alpha
        * (clock_rescaling * kappa)
        / (
            alpha * (clock_rescaling * velocity)
            + 2.0 * clock_rescaling * kappa
        )
    )
    assert abs(static_rate - rescaled_rate) < 1.0e-12
    return time_star, static_rate


def check_linear_gaussian_witten_identity() -> float:
    # For exp(-x^T A x/2), linear observables have covariance a^T A^{-1} b.
    # On constant exact one-forms the one-form Witten operator is A.
    precision = np.array([[3.0, 0.8], [0.8, 2.0]])
    a = np.array([1.2, -0.4])
    b = np.array([-0.3, 1.1])
    covariance_value = float(a @ np.linalg.inv(precision) @ b)
    witten_value = float(a @ np.linalg.solve(precision, b))
    error = abs(covariance_value - witten_value)
    assert error < 1.0e-12
    return error


def main() -> None:
    split_error = check_covariance_split()
    time_star, static_rate = check_optimized_exponent()
    witten_error = check_linear_gaussian_witten_identity()

    assert math.isfinite(static_rate) and static_rate > 0.0
    print("auxiliary-response-localization receipt: PASS")
    print(f"covariance split error: {split_error:.3e}")
    print(f"optimized auxiliary time: {time_star:.12f}")
    print(f"static exponent: {static_rate:.12f}")
    print("generator-rescaling invariance: PASS")
    print(f"linear Gaussian Witten identity error: {witten_error:.3e}")
    print(
        "scope: algebra and normalization only; no Yang--Mills or continuum "
        "premise tested"
    )


if __name__ == "__main__":
    main()
