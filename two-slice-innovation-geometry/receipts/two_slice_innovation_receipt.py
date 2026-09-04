"""Finite checks for the two-slice innovation theorems.

The receipt verifies the Friedrichs/variance constant, an innovation-matrix
bound that is sharp for a product binary channel, and the hidden-parity
counterexample. It makes no continuum or Yang--Mills claim.
"""

from __future__ import annotations

import itertools
import math

import numpy as np


def uniform_projection(size: int) -> np.ndarray:
    return np.ones((size, size)) / size


def product_binary_channel(rates: tuple[float, ...]) -> tuple[np.ndarray, np.ndarray]:
    states = np.array(list(itertools.product((-1.0, 1.0), repeat=len(rates))))
    size = len(states)
    kernel = np.ones((size, size))
    for coordinate, rate in enumerate(rates):
        kernel *= 0.5 * (
            1.0 + rate * states[:, coordinate, None] * states[None, :, coordinate]
        )
    assert np.allclose(kernel.sum(axis=1), 1.0)
    assert np.allclose(kernel, kernel.T)
    return states, kernel


def projection_onto_columns(columns: np.ndarray) -> np.ndarray:
    q, _ = np.linalg.qr(columns)
    return q @ q.T


def check_innovation_matrix() -> tuple[float, float]:
    states, transition = product_binary_channel((0.3, 0.6))
    size = len(states)
    constant = np.ones((size, 1))
    first_coordinate = states[:, 0, None]
    pi = uniform_projection(size)
    e_first = projection_onto_columns(np.hstack((constant, first_coordinate)))
    d1 = e_first - pi
    d2 = np.eye(size) - e_first

    blocks = (d1, d2)
    scalar_majorant = np.array(
        [
            [np.linalg.norm(left @ transition @ right, ord=2) for right in blocks]
            for left in blocks
        ]
    )
    rho = float(np.linalg.norm(transition - pi, ord=2))
    matrix_bound = float(np.linalg.norm(scalar_majorant, ord=2))
    assert np.allclose(scalar_majorant, np.diag((0.3, 0.6)), atol=1e-12)
    assert math.isclose(rho, 0.6, abs_tol=1e-12)
    assert math.isclose(matrix_bound, rho, abs_tol=1e-12)
    return rho, matrix_bound


def check_pair_factorization() -> tuple[float, float, float]:
    _, transition = product_binary_channel((0.3, 0.6))
    size = transition.shape[0]
    joint = transition / size
    path_size = size * size
    x_basis = np.zeros((path_size, size))
    y_basis = np.zeros((path_size, size))
    constant = np.zeros(path_size)

    row = 0
    for x in range(size):
        for y in range(size):
            root = math.sqrt(joint[x, y])
            x_basis[row, x] = root * math.sqrt(size)
            y_basis[row, y] = root * math.sqrt(size)
            constant[row] = root
            row += 1

    e_x = x_basis @ x_basis.T
    e_y = y_basis @ y_basis.T
    common = np.outer(constant, constant)
    reduced_x = e_x - common
    reduced_y = e_y - common
    rho = float(np.linalg.norm(reduced_x @ reduced_y, ord=2))

    pair_form = 2.0 * np.eye(path_size) - e_x - e_y
    complement = np.eye(path_size) - common
    eigenvalues = np.linalg.eigvalsh(complement @ pair_form @ complement)
    positive = eigenvalues[eigenvalues > 1e-10]
    floor = float(positive[0])
    optimal_factor = 1.0 / floor

    assert math.isclose(rho, 0.6, abs_tol=1e-12)
    assert math.isclose(floor, 1.0 - rho, abs_tol=1e-12)
    assert math.isclose(optimal_factor, 1.0 / (1.0 - rho), abs_tol=1e-12)
    return rho, floor, optimal_factor


def check_hidden_parity(
    n: int = 5, epsilon: float = 0.03
) -> tuple[float, float, float, float]:
    states = np.array(list(itertools.product((-1.0, 1.0), repeat=n)))
    size = len(states)
    parity = np.prod(states, axis=1)
    pi = uniform_projection(size)
    transfer = pi + (1.0 - epsilon) * np.outer(parity, parity) / size

    assert np.allclose(transfer.sum(axis=1), 1.0)
    assert np.allclose(transfer, transfer.T)
    assert np.min(transfer) > 0.0
    assert np.min(np.linalg.eigvalsh(transfer)) > -1e-12

    rho = float(np.linalg.norm(transfer - pi, ord=2))
    assert math.isclose(rho, 1.0 - epsilon, abs_tol=1e-12)

    # Projection onto functions of a proper output block: the first n-1 spins.
    labels = [tuple(row[:-1]) for row in states]
    block_basis = np.zeros((size, 2 ** (n - 1)))
    label_to_column: dict[tuple[float, ...], int] = {}
    for row, label in enumerate(labels):
        column = label_to_column.setdefault(label, len(label_to_column))
        block_basis[row, column] = 1.0
    e_block = projection_onto_columns(block_basis)
    proper_block_correlation = float(
        np.linalg.norm((transfer - pi) @ (e_block - pi), ord=2)
    )
    assert proper_block_correlation < 1e-12

    rate = 0.4
    delta = 0.02
    _, noise = product_binary_channel((rate,) * n)
    injective = (1.0 - delta) * transfer + delta * noise
    assert np.min(np.linalg.eigvalsh(injective)) > 0.0
    injective_block_correlation = float(
        np.linalg.norm((injective - pi) @ (e_block - pi), ord=2)
    )
    assert injective_block_correlation <= delta * rate + 1e-12
    parity_eigenvalue = float(parity @ injective @ parity / size)
    expected_parity = (1.0 - delta) * (1.0 - epsilon) + delta * rate**n
    assert math.isclose(parity_eigenvalue, expected_parity, abs_tol=1e-12)
    return (
        rho,
        proper_block_correlation,
        injective_block_correlation,
        parity_eigenvalue,
    )


def main() -> None:
    rho_pair, floor, factor = check_pair_factorization()
    rho_innovation, matrix_bound = check_innovation_matrix()
    parity_rho, block_rho, injective_block_rho, injective_parity = (
        check_hidden_parity()
    )

    print("two-slice innovation geometry: finite identities")
    print(f"pair maximal correlation       = {rho_pair:.9f}")
    print(f"pair-form floor 1-rho         = {floor:.9f}")
    print(f"optimal variance factor       = {factor:.9f}")
    print(f"innovation-matrix bound       = {matrix_bound:.9f}")
    print(f"actual product-channel rho    = {rho_innovation:.9f}")
    print(f"hidden parity rho             = {parity_rho:.9f}")
    print(f"proper-block correlation      = {block_rho:.3e}")
    print(f"injective proper-block rho    = {injective_block_rho:.9f}")
    print(f"injective parity eigenvalue   = {injective_parity:.9f}")
    print("scope: finite operator checks only; no Yang--Mills claim")


if __name__ == "__main__":
    main()
