"""Verify the fixed-index BKM Hessian counterexample.

The inclusion is M_2 x 1 inside M_2 x M_2 with the normalized partial-trace
expectation.  Its Jones index is four.  The reference states are not preserved
by that expectation when t is nonzero.
"""

from __future__ import annotations

import numpy as np


I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = (I, X, Y, Z)


def logarithmic_mean(a: float, b: float) -> float:
    if np.isclose(a, b, rtol=0.0, atol=1e-14):
        return 0.5 * (a + b)
    return (a - b) / (np.log(a) - np.log(b))


def bkm_metric(rho: np.ndarray, u: np.ndarray, v: np.ndarray) -> float:
    eigenvalues, eigenvectors = np.linalg.eigh(rho)
    u_eigen = eigenvectors.conj().T @ u @ eigenvectors
    v_eigen = eigenvectors.conj().T @ v @ eigenvectors
    total = 0.0j
    for i, left in enumerate(eigenvalues):
        for j, right in enumerate(eigenvalues):
            total += (
                np.conjugate(u_eigen[i, j])
                * v_eigen[i, j]
                / logarithmic_mean(float(left), float(right))
            )
    return float(np.real_if_close(total))


def partial_trace_second(a: np.ndarray) -> np.ndarray:
    reshaped = a.reshape(2, 2, 2, 2)
    return np.trace(reshaped, axis1=1, axis2=3)


def ratio_formula(t: float) -> float:
    sigma = (np.eye(4) + t * np.kron(X, X)) / 4.0
    xi = np.kron(Z, I) / 4.0
    reduced_sigma = partial_trace_second(sigma)
    reduced_xi = partial_trace_second(xi)
    upstairs = bkm_metric(sigma, xi, xi)
    downstairs = bkm_metric(reduced_sigma, reduced_xi, reduced_xi)
    expected_upstairs = np.arctanh(t) / t
    expected_ratio = 1.0 - t / np.arctanh(t)
    assert np.isclose(upstairs, expected_upstairs, rtol=1e-11, atol=1e-12)
    assert np.isclose(downstairs, 1.0, rtol=1e-11, atol=1e-12)
    assert np.isclose(
        (upstairs - downstairs) / upstairs,
        expected_ratio,
        rtol=1e-11,
        atol=1e-12,
    )
    return expected_ratio


def generalized_spectrum(t: float) -> np.ndarray:
    sigma = (np.eye(4) + t * np.kron(X, X)) / 4.0
    reduced_sigma = partial_trace_second(sigma)
    basis = [
        np.kron(left, right) / 4.0
        for left in PAULI
        for right in PAULI
        if not (np.array_equal(left, I) and np.array_equal(right, I))
    ]
    size = len(basis)
    upstairs = np.empty((size, size))
    downstairs = np.empty((size, size))
    for i, first in enumerate(basis):
        reduced_first = partial_trace_second(first)
        for j, second in enumerate(basis):
            upstairs[i, j] = bkm_metric(sigma, first, second)
            downstairs[i, j] = bkm_metric(
                reduced_sigma,
                reduced_first,
                partial_trace_second(second),
            )
    defect = upstairs - downstairs
    chol = np.linalg.cholesky(upstairs)
    inv_chol = np.linalg.inv(chol)
    normalized_defect = inv_chol @ defect @ inv_chol.T
    return np.linalg.eigvalsh(
        0.5 * (normalized_defect + normalized_defect.T)
    )


for parameter in (1e-4, 0.1, 0.5, 0.9):
    ratio = ratio_formula(parameter)
    spectrum = generalized_spectrum(parameter)
    expected = np.array(
        [0.0]
        + [ratio, ratio]
        + [1.0] * 12
    )
    assert np.allclose(spectrum, expected, rtol=1e-8, atol=1e-9), (
        parameter,
        spectrum,
        expected,
    )
    print(
        f"t={parameter:.4g}: "
        f"smallest_positive_ratio={ratio:.12g}"
    )

print("generalized spectrum at each t:")
print("  0 (multiplicity 1)")
print("  1 - t / artanh(t) (multiplicity 2)")
print("  1 (multiplicity 12)")
print("PASS: fixed index 4 does not bound the positive BKM loss edge.")
