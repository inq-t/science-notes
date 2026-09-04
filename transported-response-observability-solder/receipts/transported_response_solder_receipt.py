"""Finite checks for the transported response-observability solder."""

from __future__ import annotations

import numpy as np


def minimum_eigenvalue(operator: np.ndarray) -> float:
    return float(np.linalg.eigvalsh(operator)[0])


def operator_norm(operator: np.ndarray) -> float:
    return float(np.linalg.svd(operator, compute_uv=False)[0])


def main() -> None:
    angle = 0.43
    joint_minus = np.array(
        [
            [np.cos(angle), 0.0],
            [0.0, 1.0],
            [np.sin(angle), 0.0],
        ]
    )
    joint_plus = np.array(
        [
            [1.0, 0.0],
            [0.0, 1.0],
            [0.0, 0.0],
        ]
    )
    assert np.allclose(joint_minus.T @ joint_minus, np.eye(2))
    assert np.allclose(joint_plus.T @ joint_plus, np.eye(2))
    correspondence_transfer = joint_plus.T @ joint_minus
    correspondence_residual = (
        np.eye(3) - joint_plus @ joint_plus.T
    ) @ joint_minus
    correspondence_defect = (
        np.eye(2)
        - correspondence_transfer.T @ correspondence_transfer
    )
    assert np.allclose(
        correspondence_defect,
        correspondence_residual.T @ correspondence_residual,
    )

    retained = 0.61
    response_depth = 0.70
    response_edge = 1.0 - np.exp(-response_depth)
    solder = (1.0 - retained) / response_edge

    first_transfer = np.diag([1.0, retained])
    second_transfer = np.diag([retained, 1.0])
    first_generator = np.diag([0.0, 1.0])
    second_generator = np.diag([1.0, 0.0])
    first_response = np.diag([0.0, response_edge])
    second_response = np.diag([response_edge, 0.0])

    identity = np.eye(2)
    first_kernel_solder = identity - first_transfer - solder * first_response
    second_kernel_solder = identity - second_transfer - solder * second_response
    assert minimum_eigenvalue(first_kernel_solder) >= -1e-12
    assert minimum_eigenvalue(second_kernel_solder) >= -1e-12

    first_defect = identity - first_transfer.T @ first_transfer
    second_defect = identity - second_transfer.T @ second_transfer
    first_analysis_square = solder * first_response
    second_analysis_square = solder * second_response
    first_residual = first_defect - first_analysis_square
    second_residual = second_defect - second_analysis_square
    assert minimum_eigenvalue(first_residual) >= -1e-12
    assert minimum_eigenvalue(second_residual) >= -1e-12

    initial_to_first = identity
    initial_to_second = first_transfer
    product = second_transfer @ first_transfer
    response_gramian = (
        initial_to_first.T @ first_analysis_square @ initial_to_first
        + initial_to_second.T @ second_analysis_square @ initial_to_second
    )
    transported_residual = (
        initial_to_first.T @ first_residual @ initial_to_first
        + initial_to_second.T @ second_residual @ initial_to_second
    )
    product_defect = identity - product.T @ product

    assert np.allclose(response_gramian, (1.0 - retained) * identity)
    assert np.allclose(
        transported_residual,
        retained * (1.0 - retained) * identity,
    )
    assert np.allclose(
        product_defect,
        response_gramian + transported_residual,
    )
    assert np.linalg.matrix_rank(first_generator) == 1
    assert np.linalg.matrix_rank(second_generator) == 1
    assert minimum_eigenvalue(response_gramian) > 0.0

    response_floor = minimum_eigenvalue(response_gramian)
    certified_product_bound = np.sqrt(1.0 - response_floor)
    exact_product_norm = operator_norm(product)
    certified_rate = -np.log(certified_product_bound)
    exact_rate = -np.log(exact_product_norm)
    assert exact_product_norm <= certified_product_bound + 1e-12

    test_vector = np.array([0.37, -0.91])
    left_side = float(test_vector @ test_vector)
    survival = float((product @ test_vector) @ (product @ test_vector))
    witnessed = float(test_vector @ response_gramian @ test_vector)
    residual = float(test_vector @ transported_residual @ test_vector)
    assert np.isclose(left_side, survival + witnessed + residual)

    print("transported response solder receipt: PASS")
    print(
        "joint-correspondence residual identity error = "
        f"{operator_norm(correspondence_defect - correspondence_residual.T @ correspondence_residual):.9f}"
    )
    print(f"bounded response edge = {response_edge:.9f}")
    print(f"same-carrier solder coefficient = {solder:.9f}")
    print(
        "individual transfer norms / product norm = "
        f"{operator_norm(first_transfer):.9f}, "
        f"{operator_norm(second_transfer):.9f} / "
        f"{exact_product_norm:.9f}"
    )
    print(
        "individual response ranks / joint floor = "
        f"{np.linalg.matrix_rank(first_generator)}, "
        f"{np.linalg.matrix_rank(second_generator)} / "
        f"{response_floor:.9f}"
    )
    print(
        "certified / exact product norm = "
        f"{certified_product_bound:.9f} / {exact_product_norm:.9f}"
    )
    print(
        "transported residual / total defect floors = "
        f"{minimum_eigenvalue(transported_residual):.9f} / "
        f"{minimum_eigenvalue(product_defect):.9f}"
    )
    print(
        "certified / exact inverse-slab rates = "
        f"{certified_rate:.9f} / {exact_rate:.9f}"
    )
    print(
        "ledger survival + response + residual = "
        f"{survival:.9f} + {witnessed:.9f} + {residual:.9f} "
        f"= {left_side:.9f}"
    )


if __name__ == "__main__":
    main()
