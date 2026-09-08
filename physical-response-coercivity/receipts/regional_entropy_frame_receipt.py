"""Finite regional relative-entropy frame receipt.

The checks verify the two-qubit calculations in regional-relative-entropy-frames:
local faithful marginals see the amplitude tangent but miss the phase tangent,
while one nonlocal binary channel closes that two-dimensional encoded tangent.
They make no claim about Yang--Mills, continuum limits, or physical energy.
"""

import numpy as np


def partial_trace_two_qubits(matrix: np.ndarray, keep: int) -> np.ndarray:
    tensor = matrix.reshape(2, 2, 2, 2)
    if keep == 0:
        return np.trace(tensor, axis1=1, axis2=3)
    if keep == 1:
        return np.trace(tensor, axis1=0, axis2=2)
    raise ValueError("keep must be 0 or 1")


def density_tangent(psi: np.ndarray, vacuum: np.ndarray) -> np.ndarray:
    return np.outer(psi, vacuum.conj()) + np.outer(vacuum, psi.conj())


def bkm_at_half_identity(tangent: np.ndarray) -> float:
    # Omega_{I/2}(X)=X/2, hence g_BKM(X,X)=2 Tr(X^2).
    return float(np.real(2 * np.trace(tangent @ tangent)))


zero_zero = np.array([1.0, 0.0, 0.0, 0.0], dtype=complex)
one_one = np.array([0.0, 0.0, 0.0, 1.0], dtype=complex)

phi_plus = (zero_zero + one_one) / np.sqrt(2)
phi_minus = (zero_zero - one_one) / np.sqrt(2)
phase_tangent = 1j * phi_minus

assert np.isclose(np.vdot(phi_plus, phi_minus), 0.0)
assert np.isclose(np.vdot(phi_plus, phase_tangent), 0.0)

vacuum_density = np.outer(phi_plus, phi_plus.conj())
half_identity = np.eye(2) / 2
assert np.allclose(partial_trace_two_qubits(vacuum_density, 0), half_identity)
assert np.allclose(partial_trace_two_qubits(vacuum_density, 1), half_identity)

z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
amp_global = density_tangent(phi_minus, phi_plus)
phase_global = density_tangent(phase_tangent, phi_plus)

for keep in (0, 1):
    assert np.allclose(partial_trace_two_qubits(amp_global, keep), z)
    assert np.allclose(partial_trace_two_qubits(phase_global, keep), 0.0)

one_local_amp_cost = bkm_at_half_identity(z)
local_amp_cost = 2 * one_local_amp_cost
local_phase_cost = 0.0
assert np.isclose(one_local_amp_cost, 4.0)
assert np.isclose(local_amp_cost, 8.0)

x = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
y = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
observable = np.kron(x, y)


def expectation_derivative(global_tangent: np.ndarray) -> float:
    return float(np.real(np.trace(global_tangent @ observable)))


amp_expectation_derivative = expectation_derivative(amp_global)
phase_expectation_derivative = expectation_derivative(phase_global)
assert np.isclose(amp_expectation_derivative, 0.0)
assert np.isclose(abs(phase_expectation_derivative), 2.0)

# p_+ = (1+<O>)/2 and p_- = (1-<O>)/2.  At p_+=p_-=1/2,
# a phase derivative of magnitude 2 gives probability derivatives +/-1.
nonlocal_phase_cost = 2 * (phase_expectation_derivative / 2) ** 2 / 0.5
assert np.isclose(nonlocal_phase_cost, 4.0)

# On Psi(a,b)=a Phi_- + b i Phi_-, d=8a^2+4b^2 and ||Psi||^2=a^2+b^2.
for a, b in ((1.0, 0.0), (0.0, 1.0), (2.0, -3.0), (0.25, 0.75)):
    distinction = local_amp_cost * a * a + nonlocal_phase_cost * b * b
    norm_squared = a * a + b * b
    assert distinction >= 4.0 * norm_squared - 1e-12

print("one-local amplitude BKM cost:", one_local_amp_cost)
print("two-local amplitude cost:", local_amp_cost)
print("two-local phase cost:", local_phase_cost)
print("nonlocal phase Fisher cost:", nonlocal_phase_cost)
print("encoded-tangent lower frame constant:", 4.0)
print("all regional relative-entropy frame receipts passed")
