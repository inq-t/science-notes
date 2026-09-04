"""Finite checks for the triangle-presentation neutral adjoint frame."""

from cmath import exp, pi
from math import cos, sin

import numpy as np


def hs_inner(left: np.ndarray, right: np.ndarray) -> complex:
    return np.trace(left.conj().T @ right)


def cyclic_expectation(unitary: np.ndarray, order: int, matrix: np.ndarray) -> np.ndarray:
    result = np.zeros_like(matrix)
    power = np.eye(2, dtype=complex)
    for _ in range(order):
        result += power @ matrix @ power.conj().T
        power = power @ unitary
    return result / order


sigma_x = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
sigma_y = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
sigma_z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
basis = [sigma_x / np.sqrt(2), sigma_y / np.sqrt(2), sigma_z / np.sqrt(2)]


def superoperator_on_traceless(unitary: np.ndarray, order: int) -> np.ndarray:
    columns = []
    for vector in basis:
        image = cyclic_expectation(unitary, order, vector)
        columns.append([hs_inner(test, image).real for test in basis])
    return np.array(columns, dtype=float).T


def relative_entropy_to_trace(density: np.ndarray) -> float:
    """D(density || I/2) for a faithful two-level density matrix."""
    eigenvalues = np.linalg.eigvalsh(density).real
    assert np.all(eigenvalues > 0)
    return float(np.sum(eigenvalues * np.log(2 * eigenvalues)))


def entropy_half_hessian(tangent: np.ndarray, step: float = 1e-4) -> float:
    """Centered finite-difference check of (1/2) d^2 D/ds^2 at s=0."""
    identity = np.eye(2, dtype=complex)
    rho_plus = (identity + step * tangent) / 2
    rho_minus = (identity - step * tangent) / 2
    return (
        relative_entropy_to_trace(rho_plus)
        + relative_entropy_to_trace(rho_minus)
    ) / (2 * step**2)


omega = exp(2j * pi / 3)
a = np.diag([1.0, omega]).astype(complex)
assert np.allclose(np.linalg.matrix_power(a, 3), np.eye(2))

rows = []
for theta in (0.2, 0.4, pi / 4, 1.0):
    rotation = np.array(
        [[cos(theta), -sin(theta)], [sin(theta), cos(theta)]],
        dtype=complex,
    )
    b = rotation @ np.diag([1.0, 1j]) @ rotation.conj().T
    assert np.allclose(np.linalg.matrix_power(b, 4), np.eye(2))

    e_a = superoperator_on_traceless(a, 3)
    e_b = superoperator_on_traceless(b, 4)
    assert np.allclose(e_a @ e_a, e_a)
    assert np.allclose(e_b @ e_b, e_b)
    assert np.allclose(e_a, e_a.T)
    assert np.allclose(e_b, e_b.T)

    frame = 2 * np.eye(3) - e_a - e_b
    actual = np.linalg.eigvalsh(frame)
    c_f = abs(cos(2 * theta))
    expected = np.array(sorted([1 - c_f, 1 + c_f, 2.0]))
    assert np.allclose(actual, expected)

    orientation = (e_a @ e_b - e_b @ e_a) / (2j)
    actual_orientation = np.linalg.eigvalsh(orientation)
    signed = cos(2 * theta) * sin(2 * theta) / 2
    expected_orientation = np.array(sorted([-abs(signed), 0.0, abs(signed)]))
    assert np.allclose(actual_orientation, expected_orientation)

    tangent = 0.7 * basis[0] - 0.2 * basis[1] + 1.1 * basis[2]
    full_hessian = np.linalg.norm(tangent, "fro") ** 2 / 4
    loss_a = (
        np.linalg.norm(tangent, "fro") ** 2
        - np.linalg.norm(cyclic_expectation(a, 3, tangent), "fro") ** 2
    ) / 4
    loss_b = (
        np.linalg.norm(tangent, "fro") ** 2
        - np.linalg.norm(cyclic_expectation(b, 4, tangent), "fro") ** 2
    ) / 4
    frame_hessian = (
        hs_inner(tangent, tangent).real
        - hs_inner(tangent, cyclic_expectation(a, 3, tangent)).real / 2
        - hs_inner(tangent, cyclic_expectation(b, 4, tangent)).real / 2
    ) / 2
    assert np.isclose(loss_a + loss_b, frame_hessian)
    assert loss_a + loss_b + 1e-12 >= (1 - c_f) * full_hessian

    numeric_full = entropy_half_hessian(tangent)
    retained_a = cyclic_expectation(a, 3, tangent)
    retained_b = cyclic_expectation(b, 4, tangent)
    numeric_loss_a = numeric_full - entropy_half_hessian(retained_a)
    numeric_loss_b = numeric_full - entropy_half_hessian(retained_b)
    assert np.isclose(numeric_full, full_hessian, rtol=2e-5, atol=5e-8)
    assert np.isclose(numeric_loss_a, loss_a, rtol=2e-5, atol=5e-8)
    assert np.isclose(numeric_loss_b, loss_b, rtol=2e-5, atol=5e-8)

    rows.append((theta, actual[0], 1 - c_f))

print("TRIANGLE_RELATIONS_AND_EXPECTATIONS_PASSED")
for theta, actual_gap, expected_gap in rows:
    print(
        f"THETA={theta:.12f}; "
        f"FRAME_GAP={actual_gap:.12f}; "
        f"EXPECTED={expected_gap:.12f}"
    )
print("RELATIVE_ENTROPY_HESSIAN_IDENTITY_PASSED")
print("ORIENTATION_ODD_SPECTRUM_PASSED")
