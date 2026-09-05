"""Finite diagnostics for GL2--GL12; the uniform strip proof is in the note.

No finite sampling proves holomorphy or a cutoff-uniform decay theorem.
This receipt checks analytic conventions, the exact cancellation, and the
weighted-inverse argument on a declared finite positive terminal model.
"""

from itertools import product

import numpy as np


def aliases(n, dim):
    return np.array(list(product(range(-(n // 2), (n + 1) // 2), repeat=dim)))


def symbol_parts(z, n, eta=0.7, scale=2):
    dim = len(z)
    ell = aliases(n, dim)
    q = (z + 2 * np.pi * ell) / n
    # Holomorphic pairing d_n(q)d_n(-q), NOT a squared complex modulus.
    ratio = np.sinc(n * q / (2 * np.pi)) / np.sinc(q / (2 * np.pi))
    pair = ratio**2
    numerator = np.prod(pair, axis=1)[:, None] * pair
    h_alias = 4 * n**2 * np.sum(np.sin(q / 2)**2, axis=1)
    nonzero = np.any(ell != 0, axis=1)
    high = np.sum(numerator[nonzero] / h_alias[nonzero, None], axis=0)
    depth = round(np.log(n) / np.log(scale))
    assert scale**depth == n
    u = (1 - scale**(-2 * depth)) / (1 - scale**-2)
    v = (1 - scale**(-4 * depth)) / (1 - scale**-4)
    noise = eta * ((2 * u + v) / 3 + (u - v) * np.cos(z) / 3)
    r = np.sinc(z / (2 * np.pi)) / np.sinc(z / (2 * n * np.pi))
    g = np.prod(r**2)
    a = g * r**2
    h = 4 * n**2 * np.sum(np.sin(z / (2 * n))**2)
    return a, h, high + noise, g, ell[nonzero], h_alias[nonzero]


def cancelled(z, n):
    a, h, remainder, g, _, _ = symbol_parts(z, n)
    b = a + h * remainder
    v = np.expm1(1j * z)
    vm = np.expm1(-1j * z)
    w = 1 / g - np.sum(vm * v * remainder / (a * b))
    return h * np.diag(1 / b) - np.outer(v / b, vm / b) / w


def constrained(z, n):
    a, h, remainder, _, _, _ = symbol_parts(z, n)
    dinv = 1 / (a / h + remainder)
    v = np.expm1(1j * z)
    vm = np.expm1(-1j * z)
    return np.diag(dinv) - np.outer(dinv * v, vm * dinv) / np.sum(vm * dinv * v)


rng = np.random.default_rng(4106)
minimum_alias_ratio = np.inf
maximum_inverse_error = 0.0
for dim, n in product((2, 3, 4), (2, 4, 8)):
    delta = 1 / (10 * np.sqrt(dim))
    for _ in range(12):
        z = rng.uniform(-np.pi - delta, np.pi + delta, dim)
        z = z + 1j * rng.uniform(-delta, delta, dim)
        a, h, remainder, g, ell, hh = symbol_parts(z, n)
        alias_ratio = np.real(hh) / np.sum(ell**2, axis=1)
        minimum_alias_ratio = min(minimum_alias_ratio, float(alias_ratio.min()))
        assert alias_ratio.min() >= 0.25
        v, vm = np.expm1(1j * z), np.expm1(-1j * z)
        assert np.allclose(np.sum(vm * v / a), h / g, rtol=2e-11, atol=2e-11)
        error = np.linalg.norm(cancelled(z, n) - constrained(z, n))
        maximum_inverse_error = max(maximum_inverse_error, error)
        assert error < 2e-10
        real_symbol = cancelled(z.real, n)
        assert np.allclose(real_symbol, real_symbol.conj().T, rtol=0, atol=2e-12)
        assert np.linalg.eigvalsh(real_symbol).min() > -2e-12
        assert np.linalg.norm(real_symbol @ np.expm1(1j * z.real)) < 2e-11
        # Complete aliases, unlike the principal/high split, are periodic.
        shifted = z.copy()
        shifted[0] += 2 * np.pi
        # Outside the principal chart, use AN9 rather than the cancellation
        # chart GL8, whose intermediate principal ratios can be ill-conditioned.
        assert np.allclose(constrained(shifted, n), constrained(z, n), rtol=0, atol=2e-10)

# Nonzero complex points on the principal massless cone. GL8 stays finite.
for n in (2, 4, 8):
    t = 0.035
    z = np.array([t, 2 * n * np.arcsin(1j * np.sin(t / (2 * n)))])
    assert abs(symbol_parts(z, n)[1]) < 1e-15
    limit = cancelled(z, n)
    assert np.isfinite(limit).all()
    errors = []
    for epsilon in (1e-4, 1e-5, 1e-6):
        nearby = z + np.array([epsilon, 0])
        errors.append(np.linalg.norm(constrained(nearby, n) - limit))
    assert errors[2] < errors[1] < errors[0]
    assert errors[-1] < 2e-7
    assert np.linalg.norm(cancelled(np.zeros(2), n)) == 0

# A finite periodic transverse precision, completed by a local positive I.
# This tests the GL11--GL12 matrix lemma, not the actual gauge Schur identity
# (the latter is independently checked by endpoint_average_receipt.py).
side, dim, n = 5, 2, 4
sites = np.array(list(product(range(side), repeat=dim)))
momenta = 2 * np.pi * np.where(sites > side // 2, sites - side, sites) / side
fourier = np.exp(1j * sites @ momenta.T) / np.sqrt(len(sites))
blocks = np.array([cancelled(p, n) for p in momenta])
kernel = np.einsum("xp,pab,yp->xayb", fourier, blocks, fourier.conj())
size = len(sites) * dim
matrix = kernel.reshape(size, size) + np.eye(size)
assert np.allclose(matrix, matrix.conj().T, rtol=0, atol=3e-12)
assert np.linalg.eigvalsh(matrix).min() >= 1 - 3e-12
offset = np.abs(sites[:, None, :] - sites[None, :, :])
distance = np.minimum(offset, side - offset).sum(axis=2)
block_norm = np.linalg.norm(
    matrix.reshape(len(sites), dim, len(sites), dim).transpose(0, 2, 1, 3),
    ord=2, axis=(-2, -1),
)
theta = 1.0
while True:
    moment = block_norm * np.expm1(theta * distance)
    if max(moment.sum(axis=0).max(), moment.sum(axis=1).max()) <= 0.5:
        break
    theta /= 2
weight = np.repeat(np.exp(theta * distance[:, 0]), dim)
perturbation = weight[:, None] * matrix / weight[None, :] - matrix
assert np.linalg.norm(perturbation, ord=2) <= 0.5 + 1e-12
inverse = np.linalg.inv(matrix)
assert np.linalg.norm(weight[:, None] * inverse / weight[None, :], ord=2) <= 2
for target in range(len(sites)):
    block = inverse[dim * target:dim * (target + 1), :dim]
    assert np.linalg.norm(block, ord=2) <= 2 * np.exp(-theta * distance[target, 0])

print(f"HIGH_ALIAS_BOUND_PASSED minimum_ratio={minimum_alias_ratio:.6g}")
print(f"COCHAIN_POLE_CANCELLATION_PASSED max_error={maximum_inverse_error:.3g}")
print("COMPLEX_CONE_AND_HARMONIC_EXTENSION_PASSED")
print("COMPLETE_SYMBOL_PERIODICITY_AND_REAL_POSITIVITY_PASSED")
print(f"WEIGHTED_TERMINAL_MATRIX_LEMMA_PASSED theta={theta:g}")
print("SCOPE: finite diagnostics, not a numerical proof of the uniform strip or a mass gap")
