"""Finite arithmetic checks for the collared surface-response identities."""

from __future__ import annotations

from itertools import product

import numpy as np


def path_data(stay: float) -> tuple[np.ndarray, list[tuple[int, ...]]]:
    transition = np.array([[stay, 1.0 - stay], [1.0 - stay, stay]])
    states = list(product(range(2), repeat=5))
    weights = np.array(
        [
            0.5
            * np.prod(
                [transition[state[k], state[k + 1]] for k in range(4)]
            )
            for state in states
        ]
    )
    return weights, states


def conditional_projection(
    weights: np.ndarray,
    states: list[tuple[int, ...]],
    retained_coordinates: tuple[int, ...],
) -> np.ndarray:
    raw = np.zeros((len(states), len(states)))
    groups: dict[tuple[int, ...], list[int]] = {}
    for index, state in enumerate(states):
        key = tuple(state[k] for k in retained_coordinates)
        groups.setdefault(key, []).append(index)

    for indices in groups.values():
        mass = weights[indices].sum()
        for row in indices:
            raw[row, indices] = weights[indices] / mass

    root = np.sqrt(weights)
    return root[:, None] * raw / root[None, :]


def joint_middle_endpoints(
    weights: np.ndarray, states: list[tuple[int, ...]]
) -> np.ndarray:
    joint = np.zeros((2, 4))
    for weight, state in zip(weights, states):
        endpoint_index = 2 * state[0] + state[4]
        joint[state[2], endpoint_index] += weight
    return joint


def maximal_correlation(joint: np.ndarray) -> tuple[float, np.ndarray]:
    left = joint.sum(axis=1)
    right = joint.sum(axis=0)
    normalized = (
        joint
        / np.sqrt(left)[:, None]
        / np.sqrt(right)[None, :]
    )
    singular_values = np.linalg.svd(normalized, compute_uv=False)
    singular_values.sort()
    singular_values = singular_values[::-1]
    return float(singular_values[1]), singular_values


def local_check(stay: float) -> dict[str, float]:
    weights, states = path_data(stay)
    p_core = conditional_projection(weights, states, (2,))
    p_outer = conditional_projection(weights, states, (0, 4))
    constant = np.sqrt(weights)
    r_fixed = np.outer(constant, constant)

    reduced_product = (p_core - r_fixed) @ (p_outer - r_fixed)
    cosine = float(np.linalg.svd(reduced_product, compute_uv=False)[0])

    two_projection_form = 2.0 * np.eye(len(states)) - p_core - p_outer
    eigenvalues = np.linalg.eigvalsh(two_projection_form)
    positive_edge = float(eigenvalues[eigenvalues > 1e-11][0])

    joint = joint_middle_endpoints(weights, states)
    channel_cosine, _ = maximal_correlation(joint)
    bridge_floor = 1.0 - channel_cosine**2

    assert np.allclose(p_core @ p_core, p_core)
    assert np.allclose(p_outer @ p_outer, p_outer)
    assert np.allclose(p_core, p_core.T)
    assert np.allclose(p_outer, p_outer.T)
    assert np.isclose(cosine, channel_cosine)
    assert np.isclose(positive_edge, 1.0 - cosine)

    return {
        "cosine": cosine,
        "two_projection_edge": positive_edge,
        "bridge_floor": bridge_floor,
    }


first = local_check(0.82)
second = local_check(0.73)

weights_1, states_1 = path_data(0.82)
weights_2, states_2 = path_data(0.73)
joint_product = np.kron(
    joint_middle_endpoints(weights_1, states_1),
    joint_middle_endpoints(weights_2, states_2),
)
product_cosine, product_singular_values = maximal_correlation(joint_product)
expected_product_cosine = max(first["cosine"], second["cosine"])

assert np.isclose(product_cosine, expected_product_cosine)
assert np.isclose(first["bridge_floor"], 1.0 - first["cosine"] ** 2)

print("collared surface-response receipt")
print(f"local cosine 1: {first['cosine']:.12f}")
print(f"local cosine 2: {second['cosine']:.12f}")
print(f"two-projection edge 1: {first['two_projection_edge']:.12f}")
print(f"1 - cosine 1: {1.0 - first['cosine']:.12f}")
print(f"bridge floor 1: {first['bridge_floor']:.12f}")
print(f"1 - cosine 1^2: {1.0 - first['cosine'] ** 2:.12f}")
print(f"product cosine: {product_cosine:.12f}")
print(f"max local cosine: {expected_product_cosine:.12f}")
print(
    "leading product singular values: "
    + ", ".join(f"{value:.12f}" for value in product_singular_values[:4])
)
print("all checks passed")
