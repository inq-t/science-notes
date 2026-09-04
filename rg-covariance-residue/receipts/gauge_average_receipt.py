"""Finite matrix checks; not a Yang--Mills law or spectral-gap calculation."""

import numpy as np


rng = np.random.default_rng(4095)


def algebra(r):
    raw = rng.normal(size=(r, r)) + 1j * rng.normal(size=(r, r))
    x = (raw - raw.conj().T) / 2
    return x - np.trace(x) * np.eye(r) / r


def exp_skew(x):
    values, vectors = np.linalg.eigh(-1j * x)
    return (vectors * np.exp(1j * values)) @ vectors.conj().T


def mean(transports, weights):
    r = transports.shape[-1]
    z = np.einsum("i,ijk->jk", weights, transports)
    c = transports[0].conj().T @ z
    d = c - np.eye(r)
    assert np.linalg.norm(d, 2) < 0.5
    log_c = np.zeros_like(c)
    power = np.eye(r, dtype=complex)
    for k in range(1, 90):
        power = power @ d
        log_c += (-1)**(k + 1) * power / k
    theta = np.trace(log_c).imag
    left, _, right = np.linalg.svd(z)
    p = left @ right
    return np.exp(-1j * theta / r) * p


weights = np.array([0.2, 0.3, 0.5])
for r in (2, 3, 4):
    base = exp_skew(algebra(r))
    transports = np.array([base @ exp_skew(0.04 * algebra(r)) for _ in weights])
    output = mean(transports, weights)
    assert np.linalg.norm(output.conj().T @ output - np.eye(r)) < 1e-12
    assert abs(np.linalg.det(output) - 1) < 1e-12
    g, h = exp_skew(algebra(r)), exp_skew(algebra(r))
    transformed = np.array([g @ w @ h.conj().T for w in transports])
    assert np.linalg.norm(mean(transformed, weights) - g @ output @ h.conj().T) < 1e-12

    tangent = np.array([algebra(r) for _ in weights])
    step = 2e-6
    plus = np.array([base @ exp_skew(step*x) for x in tangent])
    minus = np.array([base @ exp_skew(-step*x) for x in tangent])
    derivative = (mean(plus, weights) - mean(minus, weights)) / (2*step)
    expected = base @ np.einsum("i,ijk->jk", weights, tangent)
    assert np.linalg.norm(derivative - expected) < 1e-8

    plus = np.array([w @ exp_skew(step*x) for w, x in zip(transports, tangent)])
    minus = np.array([w @ exp_skew(-step*x) for w, x in zip(transports, tangent)])
    derivative = (mean(plus, weights) - mean(minus, weights)) / (2*step)
    z = np.einsum("i,ijk->jk", weights, transports)
    dz = sum(w * u @ x for w, u, x in zip(weights, transports, tangent))
    sigma = np.linalg.svd(z, compute_uv=False)[-1]
    assert np.linalg.norm(derivative) <= np.linalg.norm(dz) / sigma + 1e-8

    identity = np.eye(r)
    order_two = np.diag([-1, -1] + [1] * (r-2))
    assert np.array_equal(order_two @ order_two, identity)
    assert np.linalg.matrix_rank((identity + order_two) / 2) == r-2
    # Left multiplication swaps the pair. No group output can be fixed,
    # because its inverse would imply order_two == identity.
    assert np.linalg.norm(order_two @ output - output) > 1

print("PASS: SU(2), SU(3), SU(4) regular polar means are special unitary.")
print("PASS: independent endpoint gauge covariance and coincident-input derivative.")
print("PASS: local Frobenius derivative bound at regular sampled inputs.")
print("PASS: order-two symmetric inputs are singular and admit no fixed group output.")
r0, r1 = 0.15, 0.4


def cutoff(s):
    def eta(u):
        return np.exp(-1/u) if u > 0 else 0.0
    top = eta(r1*r1 - s)
    return top / (top + eta(s - r0*r0))


def anchored_mean(transports, weights):
    r = transports.shape[-1]
    identity = np.eye(r, dtype=complex)
    z = np.einsum("i,ijk->jk", weights, transports)
    d = transports[0].conj().T @ z - identity
    blend = cutoff(np.linalg.norm(d)**2)
    safe_d = blend * d
    assert np.linalg.norm(safe_d, 2) < r1 + 1e-12
    safe = identity + safe_d
    log_safe = np.zeros_like(safe)
    power = identity.copy()
    for k in range(1, 90):
        power = power @ safe_d
        log_safe += (-1)**(k + 1) * power / k
    left, _, right = np.linalg.svd(safe)
    q = transports[0] @ (left @ right)
    return np.exp(-1j * np.trace(log_safe).imag/r) * q, blend


assert cutoff(r0*r0) == 1.0
assert cutoff(r1*r1) == 0.0

for r in (2, 3, 4):
    identity = np.eye(r, dtype=complex)
    base = exp_skew(algebra(r))
    directions = [algebra(r) for _ in range(2)]
    near = np.array([base] + [
        base @ exp_skew(0.04*x/np.linalg.norm(x)) for x in directions
    ])
    order_two = np.diag([-1, -1] + [1]*(r-2)).astype(complex)
    far = np.array([identity, order_two])

    rho = np.sqrt((r0*r0 + r1*r1)/2)
    t = 2*np.arcsin(rho/np.sqrt(2))
    axis = np.diag([1j, -1j] + [0j]*(r-2))
    transition = np.array([identity, exp_skew(t*axis)])

    cases = [
        (near, np.array([0.2, 0.3, 0.5]), 1.0),
        (transition, np.array([0.5, 0.5]), 0.5),
        (far, np.array([0.5, 0.5]), 0.0),
    ]
    for transports, weights, expected_blend in cases:
        q, blend = anchored_mean(transports, weights)
        assert abs(blend - expected_blend) < 1e-11
        assert np.linalg.norm(q.conj().T @ q - identity) < 2e-12
        assert abs(np.linalg.det(q) - 1) < 2e-12
        if expected_blend == 1.0:
            assert np.linalg.norm(q - mean(transports, weights)) < 2e-12
        elif expected_blend == 0.0:
            assert np.linalg.norm(q - transports[0]) < 2e-12
        else:
            assert np.linalg.norm(q - transports[0]) > 1e-3
            assert np.linalg.norm(q - mean(transports, weights)) > 1e-3

        g, h = exp_skew(algebra(r)), exp_skew(algebra(r))
        transformed = np.array([g @ w @ h.conj().T for w in transports])
        transformed_q, _ = anchored_mean(transformed, weights)
        assert np.linalg.norm(transformed_q - g @ q @ h.conj().T) < 3e-12

        # Treat transports as nonpivot prefixes to check V = K(Y) U*.
        pivot, target = exp_skew(algebra(r)), exp_skew(algebra(r))
        v, _ = anchored_mean(np.array([a @ pivot for a in transports]), weights)
        assert np.linalg.norm(v - q @ pivot) < 3e-12
        assert np.linalg.norm(q.conj().T @ v - pivot) < 3e-12
        recovered = q.conj().T @ target
        returned, _ = anchored_mean(
            np.array([a @ recovered for a in transports]), weights
        )
        assert np.linalg.norm(returned - target) < 3e-12

print("PASS: global anchored continuation, cutoff branches, endpoint covariance, and common-pivot inverse.")
print("Not tested: spatial block coercivity, conditional laws, continuum limit, or mass gap.")
