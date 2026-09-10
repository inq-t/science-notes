"""Bounded finite checks of cyclic Gram claims and their counterexamples.

The Markdown notes contain the proofs. This script does not integrate a
Yang--Mills law, construct physical history lifts, or certify a mass gap.
Received Claude files remain unchanged in the module's inbox archive.
"""

import numpy as np


def gram(vectors):
    vectors = np.asarray(vectors, dtype=complex)
    return vectors.conj() @ vectors.T


def cyclic(g):
    return g[..., 0, 1] * g[..., 1, 2] * g[..., 2, 0]


def from_cyclic(a, b, c):
    return np.array(
        [[1, a, np.conj(c)], [np.conj(a), 1, b], [c, np.conj(b), 1]],
        dtype=complex,
    )


def close(a, b, tolerance=1e-11):
    np.testing.assert_allclose(a, b, rtol=tolerance, atol=tolerance)


def explicit_controls():
    omega = np.exp(2j * np.pi / 3)
    u = np.diag([1, omega])
    f = np.ones(2) / np.sqrt(2)
    g = gram([f, u @ f, u @ u @ f])
    close(cyclic(g), -1 / 8)
    close(g[0, 1], (1 + omega) / 2)

    rotation = np.array([[-0.5, -np.sqrt(3) / 2],
                         [np.sqrt(3) / 2, -0.5]])
    lifts = [np.eye(2), rotation, rotation @ rotation]
    close(sum(lifts), np.zeros((2, 2)))
    analysis = np.vstack([lifts[0] - lifts[1],
                          lifts[1] - lifts[2], lifts[2] - lifts[0]])
    close(analysis.conj().T @ analysis, 9 * np.eye(2))
    for real_f in (np.array([1., 0.]), np.array([2., -3.]) / np.sqrt(13)):
        close(cyclic(gram([v @ real_f for v in lifts])), -1 / 8)
    _, eigenvectors = np.linalg.eig(rotation.astype(complex))
    eigen_f = eigenvectors[:, 0]
    close(cyclic(gram([v @ eigen_f for v in lifts])), 1)
    # A commuting action on the larger target can meet the all-source premise.
    source = np.array([1, 2j, -3, 0.5]) / np.sqrt(14.25)
    close(cyclic(gram([np.kron(source, v[:, 0]) for v in lifts])), -1 / 8)

    permutation = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    centered = np.array([1, 1j, -1 - 1j]) / 2
    close(centered.sum(), 0)
    close(np.linalg.norm(centered), 1)
    g = gram([centered, permutation @ centered,
              permutation @ permutation @ centered])
    close(g[0, 1], -0.5 - 0.75j)
    close(cyclic(g), 23 / 32 - 9j / 64)

    unequal = from_cyclic(0.9, 0.1, -0.1)
    assert np.linalg.eigvalsh(unequal).min() > 0
    close(np.linalg.det(unequal), 0.152)
    assert abs(unequal[0, 1]) > 0.5

    g_spectral = from_cyclic(*(3 * [1j / np.sqrt(3)]))
    close(np.linalg.eigvalsh(g_spectral), [0, 1, 2])
    close(9 - g_spectral.sum().real, 6)
    g_comparison = from_cyclic(*(3 * [0.5 + 1j / (2 * np.sqrt(3))]))
    close(np.linalg.eigvalsh(g_comparison), [0, 1, 2])
    close(cyclic(g_comparison).real, 0)
    close(9 - g_comparison.sum().real, 3)
    g_upper = from_cyclic(-0.5, -0.5, -0.5)
    close(9 - g_upper.sum().real, 9)
    print("PASS explicit commuting, real-core, reality, unequal-modulus, and sharpness controls")


def finite_gram_checks():
    rng = np.random.default_rng(20260909)
    count = 20000
    z = rng.normal(size=(count, 3)) + 1j * rng.normal(size=(count, 3))
    g = np.broadcast_to(np.eye(3), (count, 3, 3)).astype(complex).copy()
    g[:, 0, 1], g[:, 1, 2], g[:, 2, 0] = z.T
    g[:, 1, 0], g[:, 2, 1], g[:, 0, 2] = z.conj().T
    residual = np.linalg.det(2 * np.eye(3) - g) - (
        np.linalg.det(g) - 4 * cyclic(g).real)
    assert np.max(np.abs(residual)) < 1e-10

    vectors = rng.normal(size=(count, 3, 3)) + 1j * rng.normal(size=(count, 3, 3))
    vectors /= np.linalg.norm(vectors, axis=2, keepdims=True)
    correlations = np.einsum("bik,bjk->bij", vectors.conj(), vectors)
    products = cyclic(correlations).real
    accepted = correlations[products <= 0]
    assert len(accepted) > 100
    assert np.linalg.eigvalsh(accepted).max() <= 2 + 1e-10
    response = 9 - accepted.sum(axis=(1, 2)).real
    assert response.min() >= 3 - 1e-10
    assert response.max() <= 9 + 1e-10
    print(f"PASS {count} determinant checks; {len(accepted)} exact-premise Gram checks")

    epsilon = 0.12
    for eta in (0.0, 0.01, 0.2, 0.8):
        selected = correlations[products <= eta]
        squared_norms = rng.uniform(1 - epsilon, 1 + epsilon,
                                   size=(len(selected), 3))
        weights = np.sqrt(squared_norms)
        response = 3 * squared_norms.sum(axis=1) - np.einsum(
            "bi,bij,bj->b", weights, selected, weights).real
        s = (np.sqrt(1 + 8 * eta) - 1) / 2
        lower = 3 * (1 - epsilon) * (1 - s)
        upper = 9 * (1 + epsilon)
        assert np.linalg.eigvalsh(selected).max() <= 2 + s + 1e-10
        assert response.min() >= lower - 1e-10
        assert response.max() <= upper + 1e-10
        print(f"PASS perturbed Gram checks: epsilon={epsilon}, eta={eta}, samples={len(selected)}")


if __name__ == "__main__":
    explicit_controls()
    finite_gram_checks()
    print("Scope: finite matrix diagnostics; no Yang--Mills realization or continuum certificate")
