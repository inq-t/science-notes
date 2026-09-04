"""Finite checks for the gauge-cycle innovation theorem.

The graph has two vertices joined by three parallel Z2 links.  One link is a
spanning tree and the other two close the independent cycles

    z1 = x0*x1,  z2 = x0*x2.

The receipt checks gauge-equivariant coordinate expectations, the vanishing
tree innovation, the pure product-transfer girth exponent, and the abstract
innovation-matrix bound after an interacting magnetic sandwich and Perron
ground-state transform.
"""

from __future__ import annotations

import itertools

import numpy as np


def conditional_expectation(states, probabilities, coordinates):
    """Matrix for E[f | selected coordinates] on a finite probability space."""

    n = len(states)
    out = np.zeros((n, n), dtype=float)
    groups = {}
    for i, state in enumerate(states):
        key = tuple(state[k] for k in coordinates)
        groups.setdefault(key, []).append(i)
    for i, state in enumerate(states):
        key = tuple(state[k] for k in coordinates)
        indices = groups[key]
        mass = sum(probabilities[j] for j in indices)
        for j in indices:
            out[i, j] = probabilities[j] / mass
    return out


def weighted_euclidean(operator, probabilities):
    root = np.sqrt(probabilities)
    return np.diag(root) @ operator @ np.diag(1.0 / root)


def op_norm(operator):
    return float(np.linalg.svd(operator, compute_uv=False)[0])


def main():
    z_states = list(itertools.product((-1, 1), repeat=2))
    z_index = {state: i for i, state in enumerate(z_states)}

    link_correlation = 0.62
    cycle_correlation = link_correlation**2

    kinetic = np.zeros((4, 4), dtype=float)
    for i, z in enumerate(z_states):
        for j, zp in enumerate(z_states):
            eta1 = z[0] * zp[0]
            eta2 = z[1] * zp[1]
            kinetic[i, j] = 0.25 * (
                1.0
                + cycle_correlation * eta1
                + cycle_correlation * eta2
                + cycle_correlation * eta1 * eta2
            )

    assert np.allclose(kinetic.sum(axis=1), 1.0)
    assert np.allclose(np.linalg.eigvalsh(kinetic), [cycle_correlation] * 3 + [1.0])

    beta = 0.37
    coupling = 0.55
    magnetic = np.array(
        [
            np.exp(
                0.5
                * beta
                * (z1 + 0.8 * z2 + coupling * z1 * z2)
            )
            for z1, z2 in z_states
        ]
    )
    transfer = np.diag(magnetic) @ kinetic @ np.diag(magnetic)
    eigenvalues, eigenvectors = np.linalg.eigh(transfer)
    lambda0 = float(eigenvalues[-1])
    psi = eigenvectors[:, -1]
    if psi.sum() < 0:
        psi = -psi
    assert np.all(psi > 0)

    stationary = psi**2
    stationary /= stationary.sum()
    doob = transfer * psi[np.newaxis, :] / (lambda0 * psi[:, np.newaxis])
    assert np.allclose(doob.sum(axis=1), 1.0)
    assert np.allclose(stationary[:, None] * doob, stationary[None, :] * doob.T)

    e0 = np.tile(stationary, (4, 1))
    e1 = conditional_expectation(z_states, stationary, (0,))
    identity = np.eye(4)
    d1 = e1 - e0
    d2 = identity - e1

    symmetric_doob = weighted_euclidean(doob, stationary)
    d1e = weighted_euclidean(d1, stationary)
    d2e = weighted_euclidean(d2, stationary)
    e0e = weighted_euclidean(e0, stationary)
    centered = identity - e0e

    assert np.allclose(symmetric_doob, symmetric_doob.T)
    assert np.allclose(d1e @ d2e, 0.0, atol=1e-12)
    assert np.allclose(d1e + d2e, centered)

    blocks = (d1e, d2e)
    innovation = np.array(
        [
            [op_norm(left @ symmetric_doob @ right) for right in blocks]
            for left in blocks
        ]
    )
    rho = op_norm(centered @ symmetric_doob @ centered)
    innovation_bound = op_norm(innovation)
    assert rho <= innovation_bound + 1e-12
    assert innovation_bound < 1.0

    raw_states = list(itertools.product((-1, 1), repeat=3))
    raw_probabilities = np.array(
        [stationary[z_index[(x0 * x1, x0 * x2)]] / 2.0 for x0, x1, x2 in raw_states]
    )
    raw_index = {state: i for i, state in enumerate(raw_states)}
    gauge = np.zeros((8, 8), dtype=float)
    for i, state in enumerate(raw_states):
        gauge[i, i] += 0.5
        gauge[i, raw_index[tuple(-x for x in state)]] += 0.5

    prefix_sets = ((), (0,), (0, 1), (0, 1, 2))
    prefix_expectations = [
        conditional_expectation(raw_states, raw_probabilities, coordinates)
        for coordinates in prefix_sets
    ]
    gauge_e = weighted_euclidean(gauge, raw_probabilities)
    physical_ranks = []
    for expectation in prefix_expectations:
        expectation_e = weighted_euclidean(expectation, raw_probabilities)
        assert np.allclose(expectation_e @ gauge_e, gauge_e @ expectation_e)
        physical_ranks.append(
            int(np.linalg.matrix_rank(gauge_e @ expectation_e @ gauge_e, tol=1e-10))
        )

    assert physical_ranks == [1, 1, 2, 4]

    print("gauge-cycle innovation receipt: PASS")
    print(f"tree/prefix physical ranks = {physical_ranks}")
    print(f"link correlation = {link_correlation:.9f}")
    print(f"pure physical contraction = r^2 = {cycle_correlation:.9f}")
    print(f"interacting physical rho = {rho:.9f}")
    print("interacting innovation matrix =")
    print(np.array2string(innovation, precision=9, suppress_small=False))
    print(f"innovation-matrix norm = {innovation_bound:.9f}")


if __name__ == "__main__":
    main()
