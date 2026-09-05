"""Finite checks for Fisher transport and same-law bridge lifting.

Analytic proofs live in the linked Markdown notes. No continuum or novelty
claim follows from these checks. This script does not write files.
"""

from math import exp, prod, sqrt

import numpy as np


RNG = np.random.default_rng(107)


def assert_close(left, right, tol=2e-11):
    assert np.max(np.abs(np.asarray(left) - np.asarray(right))) < tol


def centered_basis(prob):
    root = np.sqrt(prob)
    full, _ = np.linalg.qr(np.column_stack((root, np.eye(len(prob))[:, 1:])))
    return full[:, 1:]


def predictor(joint):
    py, pz = joint.sum(axis=1), joint.sum(axis=0)
    return joint.T / np.sqrt(pz[:, None] * py[None, :])


def bridge_gap(joint):
    joint = joint / joint.sum()
    k = predictor(joint)
    basis = centered_basis(joint.sum(axis=1))
    return np.linalg.eigvalsh(basis.T @ (np.eye(k.shape[1]) - k.T @ k) @ basis)[0]


def pullback(prob, labels):
    coarse = np.bincount(labels, weights=prob)
    result = np.zeros((len(prob), len(coarse)))
    result[np.arange(len(prob)), labels] = np.sqrt(prob / coarse[labels])
    return result, coarse


def check_projection_lemma():
    for a in (0.03, 0.2, 0.8, 1.0):
        for b in (0.02, 0.4, 0.9, 1.0):
            cross = sqrt(a * (1 - a) * (1 - b))
            mat = np.array([[a, cross], [cross, 1 - a + a * b]])
            assert_close(np.linalg.eigvalsh(mat), [a * b, 1])
            assert np.linalg.eigvalsh(mat - np.diag([0, b]))[0] > -2e-12
    for dimension in (3, 5, 9):
        for _ in range(20):
            raw = RNG.normal(size=(dimension, dimension)) + 1j * RNG.normal(
                size=(dimension, dimension)
            )
            unitary, _ = np.linalg.qr(raw)
            eigs = RNG.uniform(0.002, 1, size=dimension)
            mat = (unitary * eigs) @ unitary.conj().T
            rank = dimension // 2
            a = np.linalg.eigvalsh(mat[:rank, :rank])[0]
            b = 1 / np.linalg.eigvalsh(np.linalg.inv(mat)[rank:, rank:])[-1]
            q = np.diag([0] * rank + [1] * (dimension - rank))
            assert np.linalg.eigvalsh(mat - b * q)[0] > -2e-11
            assert np.linalg.eigvalsh(mat)[0] >= a * b - 2e-11
    diag_only = np.ones((2, 2)) / 2
    assert_close(np.linalg.eigvalsh(diag_only), [0, 1])


def inspect_joint(joint, x_labels, w_labels):
    joint = joint / joint.sum()
    py, pz = joint.sum(axis=1), joint.sum(axis=0)
    jx, px = pullback(py, x_labels)
    jw, _ = pullback(pz, w_labels)
    k = predictor(joint)
    bmat = np.eye(len(py)) - k.T @ k
    coarse_k = jw.T @ k @ jx
    coarse_b = np.eye(len(px)) - coarse_k.T @ coarse_k
    leakage = (np.eye(len(pz)) - jw @ jw.T) @ k @ jx
    assert_close(jx.T @ bmat @ jx, coarse_b - leakage.T @ leakage)
    x_basis = centered_basis(px)
    kappa_c = np.linalg.eigvalsh(x_basis.T @ coarse_b @ x_basis)[0]
    eta_sq = np.linalg.norm(leakage @ x_basis, ord=2) ** 2
    conditional_b = min(
        bridge_gap(joint[x_labels == label, :]) for label in range(len(px))
    )
    q = np.eye(len(py)) - jx @ jx.T
    assert np.linalg.eigvalsh(bmat - conditional_b * q)[0] > -2e-11
    lower = conditional_b * (kappa_c - eta_sq)
    fine = bridge_gap(joint)
    assert fine >= lower - 2e-11
    return fine, kappa_c, eta_sq, conditional_b, lower


def check_bridge_lifting():
    signs = np.array([-1, 1])
    states = np.array([(x, u) for x in signs for u in signs])
    for r in (0.1, 0.8, 0.9999):
        joint = 1 + r * states[:, 0, None] * states[None, :, 0]
        result = inspect_joint(joint, np.array([0, 0, 1, 1]), np.array([0, 1, 0, 1]))
        assert_close(result, [1 - r * r, 1, r * r, 1, 1 - r * r])
    for _ in range(40):
        joint = np.exp(0.7 * RNG.normal(size=(8, 6)))
        inspect_joint(joint, np.repeat(np.arange(4), 2), np.repeat(np.arange(3), 2))


def softmax(values, axis=-1):
    weights = np.exp(values - np.max(values, axis=axis, keepdims=True))
    return weights / weights.sum(axis=axis, keepdims=True)


def check_fisher_transport():
    input_features = RNG.normal(size=(7, 2))
    channel_features = RNG.normal(size=(7, 4, 2))
    input_base = RNG.normal(size=7)
    channel_base = RNG.normal(size=(7, 4))
    for moving in (False, True):
        features = channel_features if moving else np.zeros_like(channel_features)

        def law(z):
            py = softmax(input_base + input_features @ z)
            kernel = softmax(channel_base + np.einsum("yxp,p->yx", features, z))
            return py, kernel, py @ kernel

        z = np.array([0.2, -0.15])
        py, kernel, px = law(z)
        joint = py[:, None] * kernel
        score_y = input_features - py @ input_features
        score_q = features - np.einsum("yx,yxp->yp", kernel, features)[:, None, :]
        total = score_y[:, None, :] + score_q
        score_x = np.einsum("yx,yxp->xp", joint, total) / px[:, None]
        iy = np.einsum("y,yp,yq->pq", py, score_y, score_y)
        iq = np.einsum("yx,yxp,yxq->pq", joint, score_q, score_q)
        ix = np.einsum("x,xp,xq->pq", px, score_x, score_x)
        residual = total - score_x[None, :, :]
        missing = np.einsum("yx,yxp,yxq->pq", joint, residual, residual)
        assert_close(iy + iq - ix, missing)
        assert np.linalg.eigvalsh(missing)[0] > -2e-12
        if not moving:
            assert np.linalg.eigvalsh(np.linalg.inv(ix) - np.linalg.inv(iy))[0] >= -2e-11
        for coordinate in range(2):
            direction = np.eye(2)[coordinate] * 1e-5
            numerical = (np.log(law(z + direction)[2]) - np.log(law(z - direction)[2])) / 2e-5
            assert_close(numerical, score_x[:, coordinate], 2e-9)
    assert np.linalg.eigvalsh(np.linalg.pinv(np.diag([1.0, 0.0])) - np.eye(2))[0] == -1
    v, sigma_sq, noise_sq = 2.0, 0.001, 0.4
    fine = sigma_sq / (v + sigma_sq)
    retained = (sigma_sq + noise_sq) / (v + sigma_sq + noise_sq)
    assert retained > fine
    assert (1 + 30) ** 2 / (sigma_sq + noise_sq) > 1 / sigma_sq


def fisher_two_scale(rho, lam, c):
    trace = rho + lam + c
    return 2 * rho * lam / (trace + sqrt(trace * trace - 4 * rho * lam))


def recursive_two_scale(rhos, cs, metric_factors, terminal):
    current = terminal
    for rho, c, metric in reversed(list(zip(rhos, cs, metric_factors))):
        if rho <= current:
            raise ValueError("The simplified product bound needs rho > its recursive certificate")
        current = metric * current / (1 + c / (rho - current))
    return current


def check_two_scale_and_budget():
    for rho, lam, alpha in ((3.0, 1.0, 0.0), (3.0, 1.0, 2.0), (0.7, 4.0, -1.2)):
        c = rho * alpha * alpha
        precision = np.array([[rho, -rho * alpha], [-rho * alpha, lam + c]])
        assert_close(fisher_two_scale(rho, lam, c), np.linalg.eigvalsh(precision)[0])
        t = 0.6 * min(rho, lam)
        threshold = (rho - t) * (lam - t) / t
        for multiplier in (0.8, 1.0, 1.2):
            gap = fisher_two_scale(rho, lam, threshold * multiplier)
            assert (gap >= t - 1e-12) == (multiplier <= 1)
        if rho > lam:
            assert fisher_two_scale(rho, lam, c) >= lam / (1 + c / (rho - lam)) - 1e-12

    # Independent certificates 0.01 and 1 cannot be telescoped across gaps
    # 0.1, 100, 1. The recursive hypothesis must reject the simplified bound.
    try:
        recursive_two_scale([0.1, 100], [0, 0], [1, 1], 1)
    except ValueError:
        pass
    else:
        raise AssertionError("Invalid independent-certificate product was accepted")
    assert_close(fisher_two_scale(0.1, 1, 0), 0.1)

    rho0, rho1, alpha0, alpha1, terminal = 4.0, 3.0, 0.3, 0.4, 1.0
    gaussian_precision = np.array([
        [rho0, -rho0 * alpha0, 0],
        [-rho0 * alpha0, rho1 + rho0 * alpha0**2, -rho1 * alpha1],
        [0, -rho1 * alpha1, terminal + rho1 * alpha1**2],
    ])
    recursive = recursive_two_scale(
        [rho0, rho1], [rho0 * alpha0**2, rho1 * alpha1**2], [1, 1], terminal
    )
    assert np.linalg.eigvalsh(gaussian_precision)[0] >= recursive - 1e-12

    terminal, amplitude, leakage_amplitude = 0.7, 0.2, 0.01
    certified = exp(-amplitude) * terminal - leakage_amplitude / 3
    results = []
    for depth in (1, 3, 10, 100, 500):
        cs = [amplitude * 2.0 ** (j - depth) for j in range(depth)]
        leaks = [leakage_amplitude * 2.0 ** (2 * (j - depth)) for j in range(depth)]
        floors = [1 / (1 + c) for c in cs]
        recursive = terminal
        for j in reversed(range(depth)):
            recursive = floors[j] * (recursive - leaks[j])
        prefix, loss = 1.0, 0.0
        for b, eta_sq in zip(floors, leaks):
            prefix *= b
            loss += prefix * eta_sq
        assert_close(recursive, prefix * terminal - loss)
        assert recursive >= certified - 1e-12
        results.append((depth, recursive))
    assert prod([0.95] * 500) < 1e-10
    return results


if __name__ == "__main__":
    check_projection_lemma()
    print("PASS sharp projection-conditioned product and 60 complex operator checks")
    check_bridge_lifting()
    print("PASS boundary leakage identity, conditional full-space bound, and 40 joint-law lifts")
    check_fisher_transport()
    print("PASS fixed/moving normalized Fisher ledgers, score derivatives, and rank-loss warning")
    budget_results = check_two_scale_and_budget()
    print("PASS Gaussian two-scale constant, target budget, and depth-independent summable losses")
    print("CERTIFICATE ARITHMETIC:", budget_results)
    print("SCOPE: finite identities and sufficient bounds, not a Yang--Mills continuum construction")
