"""Finite witness for disjoint adhesion and collared bridge compression.

The receipt enumerates a stationary two-state Markov path. It checks that the
full disjoint three-block resampling edge is bounded by the adjacent-slice
transfer defect, and that overlapping boundary collars compress exactly to
the midpoint bridge Gramian. It also checks the large-x SU(2) Wilson Bessel
asymptotic. It makes no continuum or Yang--Mills proof claim.
"""

from __future__ import annotations

import itertools
import math

import numpy as np


P = np.array([[0.9, 0.1], [0.1, 0.9]], dtype=float)
PI = np.array([0.5, 0.5], dtype=float)
STATE_COUNT = 2
HALF_DEPTH = 3
PATH_LENGTH = 2 * HALF_DEPTH + 1


def bessel_i(order: int, x: float) -> float:
    """Return I_order(x) from its positive power series."""
    term = (0.5 * x) ** order / math.factorial(order)
    total = term
    for k in range(1, 10000):
        term *= (0.25 * x * x) / (k * (order + k))
        updated = total + term
        if abs(updated - total) <= 2.0e-16 * abs(updated):
            return updated
        total = updated
    raise RuntimeError("Bessel series did not converge")


def path_carrier() -> tuple[list[tuple[int, ...]], np.ndarray]:
    configs = list(itertools.product(range(STATE_COUNT), repeat=PATH_LENGTH))
    weights = np.empty(len(configs), dtype=float)
    for row, config in enumerate(configs):
        weight = PI[config[0]]
        for k in range(PATH_LENGTH - 1):
            weight *= P[config[k], config[k + 1]]
        weights[row] = weight
    assert math.isclose(float(weights.sum()), 1.0, abs_tol=1e-13)
    return configs, weights


def conditional_projection(
    configs: list[tuple[int, ...]],
    weights: np.ndarray,
    resampled_coordinates: set[int],
) -> np.ndarray:
    """Orthogonal projection onto functions of the complementary coordinates."""
    complement = tuple(k for k in range(PATH_LENGTH) if k not in resampled_coordinates)
    groups: dict[tuple[int, ...], list[int]] = {}
    for row, config in enumerate(configs):
        key = tuple(config[k] for k in complement)
        groups.setdefault(key, []).append(row)

    basis = np.zeros((len(configs), len(groups)), dtype=float)
    for column, rows in enumerate(groups.values()):
        group_weight = float(weights[rows].sum())
        basis[rows, column] = np.sqrt(weights[rows] / group_weight)
    assert np.allclose(basis.T @ basis, np.eye(len(groups)), atol=2e-13)
    return basis @ basis.T


def slice_embedding(
    configs: list[tuple[int, ...]],
    weights: np.ndarray,
    time_index: int,
) -> np.ndarray:
    embedding = np.zeros((len(configs), STATE_COUNT), dtype=float)
    for row, config in enumerate(configs):
        state = config[time_index]
        embedding[row, state] = math.sqrt(weights[row] / PI[state])
    assert np.allclose(embedding.T @ embedding, np.eye(STATE_COUNT), atol=2e-13)
    return embedding


def centered_floor(operator: np.ndarray, constant: np.ndarray) -> float:
    q = np.eye(operator.shape[0]) - np.outer(constant, constant)
    spectrum = np.linalg.eigvalsh(q @ operator @ q)
    positive = spectrum[spectrum > 1e-10]
    return float(positive[0])


def main() -> None:
    configs, weights = path_carrier()
    identity = np.eye(len(configs))
    constant = np.sqrt(weights)
    assert math.isclose(float(constant @ constant), 1.0, abs_tol=2e-13)

    initial = {0}
    interior = set(range(1, PATH_LENGTH - 1))
    final = {PATH_LENGTH - 1}
    disjoint_blocks = (initial, interior, final)
    l_disjoint = sum(
        (identity - conditional_projection(configs, weights, block))
        for block in disjoint_blocks
    )
    disjoint_floor = centered_floor(l_disjoint, constant)

    centered_state = np.sqrt(PI) * np.array([1.0, -1.0])
    assert math.isclose(float(centered_state @ centered_state), 1.0)
    j_one = slice_embedding(configs, weights, 1)
    boundary_trial = j_one @ centered_state
    trial_energy = float(boundary_trial @ l_disjoint @ boundary_trial)
    transfer_eigenvalue = 0.8
    adjacent_defect = 1.0 - transfer_eigenvalue**2
    assert trial_energy <= adjacent_defect + 2e-13
    assert disjoint_floor <= trial_energy + 2e-13

    collar_width = 1
    left_collar = set(range(0, collar_width + 1))
    right_collar = set(range(PATH_LENGTH - collar_width - 1, PATH_LENGTH))
    collared_blocks = (left_collar, interior, right_collar)
    l_collared = sum(
        (identity - conditional_projection(configs, weights, block))
        for block in collared_blocks
    )

    j_middle = slice_embedding(configs, weights, HALF_DEPTH)
    endpoint_projection = conditional_projection(configs, weights, interior)
    bridge = j_middle.T @ (identity - endpoint_projection) @ j_middle
    compressed_collared = j_middle.T @ l_collared @ j_middle
    compression_error = float(np.linalg.norm(compressed_collared - bridge, ord=2))
    assert compression_error < 3e-13

    bridge_spectrum = np.linalg.eigvalsh(bridge)
    bridge_floor = float(bridge_spectrum[-1])
    assert bridge_spectrum[0] > -2e-13
    assert bridge_floor > 0.0

    girth = 4
    bessel_rows: list[tuple[float, float, float, float]] = []
    for x in (20.0, 50.0, 100.0):
        ratio = bessel_i(2, x) / bessel_i(1, x)
        exact_lower_bound = 1.0 / (1.0 - ratio ** (2 * girth))
        leading = x / (3.0 * girth)
        relative_error = abs(exact_lower_bound / leading - 1.0)
        bessel_rows.append((x, exact_lower_bound, leading, relative_error))
    assert bessel_rows[-1][-1] < 0.08
    assert bessel_rows[0][-1] > bessel_rows[-1][-1]

    print("collared block factorization: finite stationary-path receipt")
    print(f"path states = {len(configs)}")
    print(f"adjacent transfer eigenvalue = {transfer_eigenvalue:.12f}")
    print(f"1-p^2 = {adjacent_defect:.12f}")
    print(f"boundary-adjacent trial energy = {trial_energy:.12f}")
    print(f"disjoint full-carrier floor = {disjoint_floor:.12f}")
    print(f"collared-to-bridge compression error = {compression_error:.3e}")
    print(f"midpoint bridge floor = {bridge_floor:.12f}")
    print("SU(2) disjoint-constant lower bound versus x/(3g), g=4")
    print("x       exact_bound      leading          relative_error")
    for x, exact_lower_bound, leading, relative_error in bessel_rows:
        print(
            f"{x:5.1f}   {exact_lower_bound:.9f}   "
            f"{leading:.9f}   {relative_error:.9f}"
        )
    print("PASS: collars preserve the bridge while removing the adhesion test")
    print("scope: finite Markov and Bessel identities only; no continuum claim")


if __name__ == "__main__":
    main()
