"""Arithmetic checks for the joint-null Casimir witness.

This receipt does not prove spectral statements, modular reconstruction, the
Casimir solder, or the Yang--Mills mass gap. It checks only the displayed
rapidity formulas, reciprocal frame rescaling, and scalar AM--GM inequality.
"""

import numpy as np


mass = 1.7
theta = np.linspace(-12.0, 12.0, 24001)
p_plus = mass * np.exp(theta)
p_minus = mass * np.exp(-theta)
clock_energy = 0.5 * (p_plus + p_minus)

assert np.allclose(p_plus * p_minus, mass**2, rtol=2e-14, atol=2e-14)
assert np.isclose(clock_energy.min(), mass, rtol=1e-14, atol=1e-14)
assert np.all(clock_energy + 1e-14 >= np.sqrt(p_plus * p_minus))

boost = 2.3
boosted_plus = np.exp(boost) * p_plus
boosted_minus = np.exp(-boost) * p_minus
assert np.allclose(
    boosted_plus * boosted_minus,
    p_plus * p_minus,
    rtol=2e-14,
    atol=2e-14,
)

common_scale = 3.1
scaled_plus = common_scale * p_plus
scaled_minus = common_scale * p_minus
assert np.allclose(
    scaled_plus * scaled_minus,
    common_scale**2 * p_plus * p_minus,
    rtol=2e-14,
    atol=2e-14,
)

rng = np.random.default_rng(20260903)
x = np.exp(rng.normal(size=10000))
y = np.exp(rng.normal(size=10000))
assert np.all(0.5 * (x + y) + 1e-14 >= np.sqrt(x * y))

print("joint null product:", float((p_plus * p_minus)[0]))
print("clock lower edge:", float(clock_energy.min()))
print("reciprocal boost leaves Casimir invariant")
print("common scaling changes Casimir by the square of the yardstick")
print("all joint-null Casimir arithmetic receipts passed")
