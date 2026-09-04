"""Finite checks of a thin-skeleton Maxwell witness and block-average control.

These are geometric quadratic-form checks, not a Yang--Mills mass-gap test.
"""

import itertools
import math
import numpy as np


def skeleton_witness(n, m):
    side = n * m
    x2 = np.arange(side)[:, None, None]
    sine = np.broadcast_to(np.sin(2 * np.pi * x2 / side), (side,) * 3).copy()
    field = sine.copy()
    field[::n, ::n, ::n] = 0
    norm = np.sum(field**2)
    energy = sum(np.sum((np.roll(field, -1, axis) - field)**2) for axis in range(3))
    lam = 4 * math.sin(math.pi / side)**2
    expected_norm = (side**3 - m**3) / 2
    expected_energy = lam * side**3 / 2 + (6 - 2 * lam) * m**3 / 2
    assert abs(norm - expected_norm) < 1e-10 * expected_norm
    assert abs(energy - expected_energy) < 1e-10 * expected_energy
    assert abs(field.mean()) < 1e-12
    assert np.max(np.abs(n * field[::n, ::n, ::n])) == 0
    assert energy > 0
    # A_1 is independent of x_1, so the linearized divergence is identically
    # zero. All other components vanish. The 4D x_1 multiplicity cancels.
    for amplitude in (0.2, 0.8):
        coarse_phase = np.exp(1j * amplitude * n * field[::n, ::n, ::n])
        assert np.max(np.abs(coarse_phase - 1)) == 0
    return norm, energy


for n, m in ((3, 3), (3, 5), (4, 4), (8, 5)):
    skeleton_witness(n, m)
print("PASS: direct lattice norm, curl energy, zero mean, and exact skeleton blindness.")

# Evaluate the proven formula at increasing volume and decreasing cutoff.
previous = math.inf
for n in (4, 8, 16, 32, 64, 128, 256, 512, 1024):
    m, b, a = n, 1.0, 1.0 / n
    lam = 4 * math.sin(math.pi / (m * n))**2
    rayleigh = (lam + (6 - 2 * lam) / n**3) / (a**2 * (1 - n**-3))
    upper = 4 * math.pi**2 / (m * b)**2 + 6 * a / (b**3 * (1 - n**-3))
    assert rayleigh <= upper * (1 + 1e-12)
    assert rayleigh < previous
    previous = rayleigh
    print(f"n=M={n:4d}: b^2 R={b*b*rayleigh:.9f}; analytic upper={b*b*upper:.9f}")
print("PASS: physical Rayleigh quotient tends downward on the joint-limit sequence.")

# Exact 1D Neumann eigenvalue; the d-dimensional internal-block Laplacian
# is its tensor sum.
for n in (2, 3, 8, 32):
    matrix = np.zeros((n, n))
    for i in range(n - 1):
        matrix[i, i] += 1
        matrix[i + 1, i + 1] += 1
        matrix[i, i + 1] -= 1
        matrix[i + 1, i] -= 1
    eigenvalues = np.linalg.eigvalsh(matrix)
    expected = 4 * math.sin(math.pi / (2 * n))**2
    assert abs(eigenvalues[1] - expected) < 1e-12
    assert n*n*expected >= 4 - 1e-12
print("PASS: exact Neumann block eigenvalue and cutoff-uniform b^-2 lower bound.")

# Independent check on actual 4D cells; internal and cross-cell edges differ.
rng = np.random.default_rng(4094)
for n in (3, 5, 7):
    field = rng.normal(size=(2*n,) * 4)
    for block in itertools.product(range(2), repeat=4):
        slices = tuple(slice(k*n, (k+1)*n) for k in block)
        field[slices] -= field[slices].mean()
    norm = np.sum(field**2)
    energy = sum(np.sum((np.roll(field, -1, axis) - field)**2) for axis in range(4))
    lam = 4 * math.sin(math.pi / (2 * n))**2
    assert energy >= lam * norm
print("PASS: mean-zero block constraint controls random four-dimensional scalar fields.")
print("Not tested: interacting conditional Yang--Mills laws, OS spectrum, or continuum existence.")
