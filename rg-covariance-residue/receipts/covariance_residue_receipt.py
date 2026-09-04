"""Finite checks of covariance shells and summation; not a Yang--Mills proof."""

import itertools
import math
import numpy as np


def conditional_projection(states, weights, retained):
    keys = [tuple(s[i] for i in retained) for s in states]
    result = np.zeros((len(states), len(states)))
    for i, key in enumerate(keys):
        mask = np.array([other == key for other in keys])
        result[i, mask] = weights[mask] / weights[mask].sum()
    return result


def covariance(f, g, weights):
    return np.vdot(f, weights * g) - np.conj(weights @ f) * (weights @ g)


states = np.array(list(itertools.product((-1, 1), repeat=4)))
weights = np.exp(
    0.47 * states[:, 0] * states[:, 1]
    + 0.31 * states[:, 1] * states[:, 2]
    - 0.23 * states[:, 2] * states[:, 3]
    + 0.17 * states[:, 0]
)
weights /= weights.sum()
projections = [
    conditional_projection(states, weights, keep)
    for keep in ((0, 1, 2, 3), (0, 1, 2), (0, 1), (0,))
]
shells = [a - b for a, b in zip(projections, projections[1:])]
f = states[:, 0] + 0.2j * states[:, 2] + states[:, 1] * states[:, 3]
g = states[:, 3] - 0.4j * states[:, 1] + states[:, 0] * states[:, 2]
fine = covariance(f, g, weights)
terminal = covariance(projections[-1] @ f, projections[-1] @ g, weights)
residues = sum(np.vdot(d @ f, weights * (d @ g)) for d in shells)
assert abs(fine - terminal - residues) < 1e-12
for i, di in enumerate(shells):
    for j, dj in enumerate(shells):
        assert np.linalg.norm(di @ dj - (di if i == j else 0)) < 1e-12
    assert np.vdot(di @ f, weights * (di @ f)).real >= -1e-12
print("PASS: complex covariance identity and weighted orthogonal shells.")

# A nonnested replacement fails: this is not a generic projection identity.
p = conditional_projection(states, weights, (0, 1))
q = conditional_projection(states, weights, (2, 3))
bad_shells = (np.eye(len(states)) - p, p - q)
bad = covariance(q @ f, q @ g, weights) + sum(
    np.vdot(d @ f, weights * (d @ g)) for d in bad_shells
)
assert abs(fine - bad) > 1e-4
print("PASS: nonnested-projection negative control fails the claimed identity.")

# Check each finite sum against its finite endpoint majorant. The infinite
# series convergence is analytic (CR9), not inferred from this truncation.
for dilation in (1.3, 2.0, 3.0):
    for power in (0.0, 1.0, 4.0):
        for rate in (0.2, 1.0):
            for depth in (1, 4, 12):
                for distance in (1.0, 2.5, 8.0):
                    scales = [dilation**n for n in range(1, depth + 1)]
                    lhs = sum(s**power * math.exp(-rate * distance * s) for s in scales)
                    rhs = math.exp(-rate * distance) * sum(
                        s**power * math.exp(-rate * (s - 1)) for s in scales
                    )
                    assert lhs <= rhs * (1 + 1e-12) + 1e-300
print("PASS: geometric-scale endpoint bound over parameter grid.")

# A retained independent variable loses a correlated hidden pair completely.
hidden = np.array(list(itertools.product((-1, 1), repeat=3)))
hidden_weights = np.exp(0.8 * hidden[:, 1] * hidden[:, 2])
hidden_weights /= hidden_weights.sum()
retain = conditional_projection(hidden, hidden_weights, (0,))
left, right = hidden[:, 1], hidden[:, 2]
assert np.max(np.abs(retain @ left)) < 1e-12
assert abs(covariance(left, right, hidden_weights) - math.tanh(0.8)) < 1e-12
assert abs(covariance(retain @ left, retain @ right, hidden_weights)) < 1e-12
print("PASS: discarded-correlated-fiber negative control.")

# For the analytic massless example, successive doubling has power-law ratio.
for radius in (10.0, 100.0):
    ratio = math.sinh(1 / (2 * radius)**2) / math.sinh(1 / radius**2)
    assert abs(ratio - 0.25) < 1e-5
print("PASS: Gaussian sine-source formula retains the massless power-law tail.")
