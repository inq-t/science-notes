"""Finite matrix witness for the oriented-descent angle and Weyl-pair claims."""

from __future__ import annotations

import math

import numpy as np


def projection_data(theta: float) -> tuple[float, float, float, float]:
    """Construct the two projections and verify their frame and order data."""
    c = math.cos(theta)
    s = math.sin(theta)

    p = np.array([[1.0, 0.0], [0.0, 0.0]])
    direction = np.array([c, s])
    q = np.outer(direction, direction)
    identity = np.eye(2)

    assert np.allclose(p @ p, p)
    assert np.allclose(q @ q, q)

    g_pair = 2.0 * identity - p - q
    eigenvalues = np.linalg.eigvalsh(g_pair)
    friedrichs_cosine = float(np.linalg.norm(p @ q, ord=2))
    alternating_norm = float(np.linalg.norm(q @ p @ q, ord=2))

    orientation = (p @ q - q @ p) / (2.0j)
    orientation_norm = float(np.linalg.norm(orientation, ord=2))

    lambda_min = float(eigenvalues[0])
    lambda_max = float(eigenvalues[-1])
    assert math.isclose(lambda_min, 1.0 - friedrichs_cosine, abs_tol=1e-12)
    assert math.isclose(lambda_max, 1.0 + friedrichs_cosine, abs_tol=1e-12)
    assert math.isclose(alternating_norm, friedrichs_cosine**2, abs_tol=1e-12)

    # Swapping the ordered pair preserves the positive form and flips orientation.
    reversed_g_pair = 2.0 * identity - q - p
    reversed_orientation = (q @ p - p @ q) / (2.0j)
    assert np.allclose(reversed_g_pair, g_pair)
    assert np.allclose(reversed_orientation, -orientation)

    return friedrichs_cosine, lambda_min, alternating_norm, orientation_norm


def weyl_floor(order: int) -> float:
    """Construct clock/shift matrices and verify the full commutator Laplacian."""
    omega = np.exp(2.0j * np.pi / order)
    u = np.diag(omega ** np.arange(order))
    v = np.zeros((order, order), dtype=complex)
    for column in range(order):
        v[(column + 1) % order, column] = 1.0

    assert np.allclose(u @ v, omega * v @ u)

    # Column-vectorization turns [A, X] into (I tensor A - A^T tensor I) vec(X).
    identity = np.eye(order, dtype=complex)
    commutator_u = np.kron(identity, u) - np.kron(u.T, identity)
    commutator_v = np.kron(identity, v) - np.kron(v.T, identity)
    laplacian = (
        commutator_u.conj().T @ commutator_u
        + commutator_v.conj().T @ commutator_v
    )
    spectrum = np.linalg.eigvalsh(laplacian)
    zero_count = int(np.count_nonzero(np.isclose(spectrum, 0.0, atol=1e-10)))
    assert zero_count == 1

    measured_coefficients: list[float] = []
    for a in range(order):
        for b in range(order):
            x = np.linalg.matrix_power(u, a) @ np.linalg.matrix_power(v, b)
            q_value = (
                np.linalg.norm(u @ x - x @ u, ord="fro") ** 2
                + np.linalg.norm(v @ x - x @ v, ord="fro") ** 2
            )
            measured = float(q_value / np.linalg.norm(x, ord="fro") ** 2)
            expected = 4.0 * (
                math.sin(math.pi * a / order) ** 2
                + math.sin(math.pi * b / order) ** 2
            )
            assert math.isclose(measured, expected, abs_tol=1e-10)

            if a == 0 and b == 0:
                assert math.isclose(measured, 0.0, abs_tol=1e-12)
                continue

            assert np.isclose(np.trace(x), 0.0, atol=1e-10)
            measured_coefficients.append(measured)

    floor = min(measured_coefficients)
    expected_floor = 4.0 * math.sin(math.pi / order) ** 2
    assert math.isclose(floor, expected_floor, abs_tol=1e-10)

    positive_spectrum = spectrum[spectrum > 1e-10]
    assert math.isclose(float(positive_spectrum[0]), expected_floor, abs_tol=1e-9)

    # Reversing generator order conjugates the Weyl phase and preserves q.
    assert np.allclose(v @ u, np.conjugate(omega) * u @ v)
    return floor


def main() -> None:
    print("oriented descent angle: finite principal-angle witnesses")
    print("degrees   c_F          frame_floor  alternating  orientation")
    for degrees in (15, 30, 60, 90):
        values = projection_data(math.radians(degrees))
        print(
            f"{degrees:7d}   "
            f"{values[0]:.9f}  "
            f"{values[1]:.9f}  "
            f"{values[2]:.9f}  "
            f"{values[3]:.9f}"
        )

    print("reversal: frame operator unchanged; orientation operator changes sign")

    print("weyl pair: finite traceless Hilbert--Schmidt floor")
    print("order     exact_floor")
    for order in (2, 3, 4, 6, 12):
        print(f"{order:5d}     {weyl_floor(order):.9f}")
    print("weyl reversal: phase conjugates; squared-commutator floor is unchanged")
    print("scope: finite matrix witnesses only; no type-III, Casimir, continuum, or Yang--Mills claim")


if __name__ == "__main__":
    main()
