"""Checks source-score transport and finite SU(2) path-block geometry."""

import math
import numpy as np


def cov(first, second, weights):
    return np.vdot(first, weights * second) - np.conj(weights @ first) * (weights @ second)


# Smooth circle fiber with a moving reference density.
z = np.arange(4096) * (2 * np.pi / 4096)
beta, field, y0 = 1.3, 0.4, 0.7


def circle(y):
    action = -beta * np.cos(y + z) - field * np.cos(z)
    log_reference = 0.3 * np.sin(y) * np.cos(2 * z)
    weights = np.exp(-action + log_reference)
    weights /= weights.sum()
    source = np.exp(1j * z) + 0.1 * np.exp(1j * y) * np.cos(2 * z)
    return weights, source


weights, source = circle(y0)
dy_source = 0.1j * np.exp(1j * y0) * np.cos(2 * z)
action_score = beta * np.sin(y0 + z)
mean_force = action_score - 0.3 * np.cos(y0) * np.cos(2 * z)
step = 1e-5
wp, fp = circle(y0 + step)
wm, fm = circle(y0 - step)
numerical = (wp @ fp - wm @ fm) / (2 * step)
exact_formula = weights @ dy_source - cov(mean_force, source, weights)
wrong_reference = weights @ dy_source - cov(action_score, source, weights)
wrong_conjugation = weights @ dy_source - cov(source, mean_force, weights)
assert abs(numerical - exact_formula) < 1e-8
assert abs(numerical - wrong_reference) > 1e-3
assert abs(numerical - wrong_conjugation) > 1e-2
print("PASS: complex-linear source derivative, moving-reference term, and negative controls.")

rng = np.random.default_rng(2304)
identity = np.eye(2, dtype=complex)
pauli = [
    np.array([[0, 1], [1, 0]], complex),
    np.array([[0, -1j], [1j, 0]], complex),
    np.array([[1, 0], [0, -1]], complex),
]
generators = [1j * p for p in pauli]


def su2():
    q = rng.normal(size=4)
    q /= np.linalg.norm(q)
    return q[0] * identity + sum(q[k + 1] * generators[k] for k in range(3))


def product(matrices):
    answer = identity.copy()
    for matrix in matrices:
        answer = answer @ matrix
    return answer


def exponential(t, generator):
    return math.cos(t) * identity + math.sin(t) * generator


def scalar(u):
    return np.trace(u).real / 2


for length in (2, 3, 5):
    edges = [su2() for _ in range(length)]
    retained = product(edges)
    hidden = product(edges[:-1])
    assert np.linalg.norm(hidden.conj().T @ retained - edges[-1]) < 1e-12
    gauges = [su2() for _ in range(length + 1)]
    transformed = [gauges[k] @ edges[k] @ gauges[k + 1].conj().T for k in range(length)]
    assert np.linalg.norm(product(transformed) - gauges[0] @ retained @ gauges[-1].conj().T) < 1e-12
    coarse_norm = 0.0
    fine_norm = 0.0
    for generator in generators:
        coarse_derivative = (
            scalar(retained @ exponential(step, generator))
            - scalar(retained @ exponential(-step, generator))
        ) / (2 * step)
        coarse_norm += coarse_derivative**2
        for k in range(length):
            plus, minus = list(edges), list(edges)
            plus[k] = edges[k] @ exponential(step, generator)
            minus[k] = edges[k] @ exponential(-step, generator)
            derivative = (scalar(product(plus)) - scalar(product(minus))) / (2 * step)
            fine_norm += derivative**2
    assert abs(fine_norm - length * coarse_norm) < 1e-7
print("PASS: non-Abelian path inversion, endpoint gauge covariance, and length-weighted mobility.")

# Two adjacent square plaquettes. Block the two bottom edges U0,U1 into V.
edges = [su2() for _ in range(7)]
retained = edges[0] @ edges[1]
generator = generators[1]


def rebuild(v, hidden_edges):
    all_edges = list(hidden_edges)
    all_edges[1] = all_edges[0].conj().T @ v
    return all_edges


def wilson(all_edges):
    u = all_edges
    p0 = u[0] @ u[5] @ u[2].conj().T @ u[4].conj().T
    p1 = u[1] @ u[6] @ u[3].conj().T @ u[5].conj().T
    return beta * (2 - scalar(p0) - scalar(p1))


def pivot_score(v, hidden_edges):
    u = rebuild(v, hidden_edges)
    return -beta * scalar(u[1] @ generator @ u[6] @ u[3].conj().T @ u[5].conj().T)


numerical_score = (
    wilson(rebuild(retained @ exponential(step, generator), edges))
    - wilson(rebuild(retained @ exponential(-step, generator), edges))
) / (2 * step)
assert abs(numerical_score - pivot_score(retained, edges)) < 1e-8
assert abs(numerical_score) <= beta + 1e-8
remote_changed = list(edges)
remote_changed[2] = su2()  # Top-left edge is outside the pivot plaquette star.
assert abs(pivot_score(retained, remote_changed) - pivot_score(retained, edges)) < 1e-12
print("PASS: exact Wilson pivot-score formula, local support, and beta bound.")

# Uniform per-step amplification is not a uniform terminal-source bound.
factor, dilation = 1.4, 2.0
terminal_norms = []
for depth in (4, 8, 16, 32):
    a = dilation ** (-depth)
    amplified = factor**depth
    expected = (1 / a) ** (math.log(factor) / math.log(dilation))
    assert abs(amplified / expected - 1) < 1e-12
    terminal_norms.append(amplified)
assert terminal_norms[-1] > 1000 * terminal_norms[0]
print("PASS: accumulated source growth diverges at fixed terminal scale.")
print("Scope: exact finite identities and illustrative bounds, not Yang--Mills mixing or continuum existence.")
