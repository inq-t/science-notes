"""Numerical checks for the resolvent--logistic scale transform.

This receipt checks only the displayed scalar identities and finite diagonal
examples. It does not prove the spectral theorem, construct the Yang--Mills
interface operator, establish continuum naturality, or prove a mass gap.
"""

import math

import numpy as np


def logistic_density(n, lam):
    x = np.exp(n) * lam
    return x / (1.0 + x) ** 2


# Every spectral value produces the same translated logistic profile.
for lam in (1e-5, 0.03, 1.0, 17.0, 1e4):
    center = -math.log(lam)
    grid = np.linspace(center - 35.0, center + 35.0, 350001)
    q = logistic_density(grid, lam)
    z = np.exp(grid) * lam / (1.0 + np.exp(grid) * lam)
    q_closed = 0.25 / np.cosh(0.5 * (grid - center)) ** 2

    assert np.max(np.abs(q - q_closed)) < 2e-15
    assert np.max(np.abs(q - z * (1.0 - z))) < 2e-16
    assert np.isclose(np.trapezoid(q, grid), 1.0, atol=2e-14, rtol=0.0)

    mean = np.trapezoid(grid * q, grid)
    variance = np.trapezoid((grid - mean) ** 2 * q, grid)
    entropy = -np.trapezoid(q * np.log(q), grid)
    location_score = np.tanh(0.5 * (grid - center))
    fisher = np.trapezoid(location_score**2 * q, grid)

    half_density = np.sqrt(q)
    half_density_prime = -0.5 * location_score * half_density
    half_density_energy = np.trapezoid(half_density_prime**2, grid)
    signed_detail = -2.0 * math.sqrt(3.0) * half_density_prime

    assert np.isclose(mean, center, atol=2e-12, rtol=0.0)
    assert np.isclose(variance, math.pi**2 / 3.0, atol=2e-10, rtol=0.0)
    assert np.isclose(entropy, 2.0, atol=2e-12, rtol=0.0)
    assert np.isclose(fisher, 1.0 / 3.0, atol=2e-12, rtol=0.0)
    assert np.isclose(half_density_energy, 1.0 / 12.0, atol=2e-12, rtol=0.0)
    assert np.isclose(np.trapezoid(signed_detail, grid), 0.0, atol=2e-14, rtol=0.0)
    assert np.isclose(np.trapezoid(signed_detail**2, grid), 1.0, atol=2e-12, rtol=0.0)


# Finite diagonal functional calculus: the scale transform is isometric on
# the positive subspace and kills exactly the zero eigenspace.
eigenvalues = np.array([0.0, 1e-4, 0.2, 3.0, 90.0])
vector = np.array([2.0 + 1.0j, -0.4 + 0.7j, 1.3 - 2.0j, 0.8j, -1.1])
grid = np.linspace(-35.0 - math.log(eigenvalues[-1]), 35.0 - math.log(eigenvalues[1]), 500001)
positive = eigenvalues > 0.0
x = np.exp(grid[:, None]) * eigenvalues[None, :]
q = np.zeros_like(x)
q[:, positive] = x[:, positive] / (1.0 + x[:, positive]) ** 2
transformed_norm_density = np.sum(q * np.abs(vector[None, :]) ** 2, axis=1)
transform_norm = np.trapezoid(transformed_norm_density, grid)
positive_norm = np.sum(np.abs(vector[positive]) ** 2)
assert np.isclose(transform_norm, positive_norm, atol=2e-11, rtol=0.0)


# A gapless family has the same profile width: only its centers run to +infinity.
gapless_values = np.exp(-np.array([1.0, 3.0, 8.0, 20.0]))
gapless_centers = -np.log(gapless_values)
assert np.allclose(gapless_centers, np.array([1.0, 3.0, 8.0, 20.0]))


# Reciprocal scaling moves individual centers but preserves their mean.
k_plus = 0.07
k_minus = 13.0
mean_center = -0.5 * math.log(k_plus * k_minus)
for boost in (-9.0, -1.7, 0.0, 2.3, 11.0):
    boosted_plus = math.exp(boost) * k_plus
    boosted_minus = math.exp(-boost) * k_minus
    plus_center = -math.log(boosted_plus)
    minus_center = -math.log(boosted_minus)
    assert math.isclose(0.5 * (plus_center + minus_center), mean_center, abs_tol=2e-14)


print("resolvent odds and forced logistic rate: passed")
print("scale normalization, moments, entropy, and Fisher constants: passed")
print("normalized signed scale-detail window: passed")
print("finite diagonal scale-frame isometry: passed")
print("gapless spectra translate centers without changing shape: passed")
print("reciprocal causal centers have invariant mean: passed")
print("no Yang--Mills operator selection, Casimir solder, or mass gap is tested")
