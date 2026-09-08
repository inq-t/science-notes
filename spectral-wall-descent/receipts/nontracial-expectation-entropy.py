"""A preserving expectation can raise or lower absolute entropy.

Checks the Heisenberg/Schrodinger adjoint relation and the relative-entropy
loss for one fixed nontracial qubit expectation. NumPy only; no file I/O.
"""

import numpy as np


def entropy(rho):
    values = np.linalg.eigvalsh(rho)
    return float(-np.sum(values * np.log(values)))


def log_matrix(rho):
    values, vectors = np.linalg.eigh(rho)
    return (vectors * np.log(values)) @ vectors.conj().T


def relative_entropy(rho, sigma):
    return float(np.trace(rho @ (log_matrix(rho) - log_matrix(sigma))).real)


sigma = np.diag([0.8, 0.2]).astype(complex)
identity = np.eye(2, dtype=complex)


def expectation(a):
    return np.trace(sigma @ a) * identity


def predual(rho):
    return np.trace(rho) * sigma


assert np.allclose(expectation(identity), identity)
assert np.allclose(predual(sigma), sigma)
observables = [identity, np.diag([1, -1]), np.array([[0, 1j], [-1j, 0]])]
states = [identity / 2, np.diag([0.99, 0.01]), np.array([[0.5, 0.2j], [-0.2j, 0.5]])]
changes = []
for rho in states:
    output = predual(rho)
    assert np.allclose(predual(output), output)
    for a in observables:
        assert np.allclose(expectation(expectation(a)), expectation(a))
        assert np.allclose(np.trace(sigma @ expectation(a)), np.trace(sigma @ a))
        assert np.allclose(np.trace(rho @ expectation(a)), np.trace(output @ a))
    loss = relative_entropy(rho, sigma) - relative_entropy(output, sigma)
    assert loss > 0
    changes.append(entropy(output) - entropy(rho))
assert changes[0] < 0 < changes[1]
assert not np.allclose(expectation(states[0]), predual(states[0]))
assert np.isclose(relative_entropy(states[0], sigma), np.log(1.25))
print("nontracial expectation: PASS")
print(f"  entropy change from maximally mixed input = {changes[0]:.12f}")
print(f"  entropy change from low-entropy input     = {changes[1]:.12f}")
print("  invariant state, idempotence, duality and positive relative-entropy loss: PASS")
