"""Finite checks for directed isometric residue completion."""

from __future__ import annotations

import numpy as np


def positive_square_root(operator: np.ndarray) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(operator)
    assert np.all(eigenvalues >= -1e-12)
    return (eigenvectors * np.sqrt(np.maximum(eigenvalues, 0.0))) @ eigenvectors.T


def operator_norm(operator: np.ndarray) -> float:
    return float(np.linalg.svd(operator, compute_uv=False)[0])


def main() -> None:
    retained = 0.61
    identity = np.eye(2)
    first = np.diag([1.0, retained])
    second = np.diag([retained, 1.0])
    first_defect = identity - first.T @ first
    second_defect = identity - second.T @ second

    first_minimal_residue = np.array([[0.0, np.sqrt(1.0 - retained**2)]])
    first_column = np.vstack([first, first_minimal_residue])
    assert np.allclose(first_column.T @ first_column, identity)
    assert np.linalg.matrix_rank(first_column) == 2
    assert first_column.shape == (3, 2)

    coisometry = np.array([[1.0, 0.0]])
    coisometry_residue = np.array([[0.0, 1.0]])
    unitary_column = np.vstack([coisometry, coisometry_residue])
    assert np.allclose(unitary_column.T @ unitary_column, identity)
    assert np.allclose(unitary_column @ unitary_column.T, identity)

    angle = 0.37
    residue_embedding = np.array([[np.cos(angle)], [np.sin(angle)]])
    alternate_residue = residue_embedding @ first_minimal_residue
    alternate_column = np.vstack([first, alternate_residue])
    factored_column = np.vstack([first, residue_embedding @ first_minimal_residue])
    factorization_error = operator_norm(alternate_column - factored_column)
    assert np.allclose(alternate_column.T @ alternate_column, identity)
    assert np.isclose(factorization_error, 0.0)

    product = second @ first
    discrete_cascade = np.vstack(
        [
            product,
            positive_square_root(first_defect),
            positive_square_root(second_defect) @ first,
        ]
    )
    assert np.allclose(discrete_cascade.T @ discrete_cascade, identity)

    # The full chronological archive can contain a stage coordinate that no
    # initial input reaches even when the endpoint product is the identity.
    insertion = np.array([[1.0], [0.0]])
    deletion = np.array([[1.0, 0.0]])
    endpoint_identity = deletion @ insertion
    deletion_defect_root = np.array([[0.0, 1.0]])
    unreachable_residue = deletion_defect_root @ insertion
    chronological_column = np.vstack([endpoint_identity, unreachable_residue])
    assert np.allclose(endpoint_identity, np.eye(1))
    assert np.allclose(chronological_column.T @ chronological_column, np.eye(1))
    assert np.linalg.matrix_rank(chronological_column) == 1
    assert chronological_column.shape == (2, 1)

    # A finite truncation suffices to verify the compression-of-powers
    # identity on the original carrier through the displayed order.
    power_order = 4
    schaeffer = np.zeros((2 + power_order, 2 + power_order))
    schaeffer[:2, :2] = first
    schaeffer[2, :2] = first_minimal_residue
    for slot in range(power_order - 1):
        schaeffer[3 + slot, 2 + slot] = 1.0
    embedded_projection = np.zeros((2 + power_order, 2))
    embedded_projection[:2, :] = identity
    power_errors = []
    for exponent in range(power_order + 1):
        compressed_power = (
            embedded_projection.T
            @ np.linalg.matrix_power(schaeffer, exponent)
            @ embedded_projection
        )
        power_errors.append(operator_norm(compressed_power - np.linalg.matrix_power(first, exponent)))
    assert max(power_errors) < 1e-12

    response_depth = 0.70
    response_edge = 1.0 - np.exp(-response_depth)
    solder = (1.0 - retained) / response_edge
    first_response_square = solder * np.diag([0.0, response_edge])
    second_response_square = solder * np.diag([response_edge, 0.0])
    first_residual = first_defect - first_response_square
    second_residual = second_defect - second_response_square
    refined_cascade = np.vstack(
        [
            product,
            positive_square_root(first_response_square),
            positive_square_root(second_response_square) @ first,
            positive_square_root(first_residual),
            positive_square_root(second_residual) @ first,
        ]
    )
    assert np.allclose(refined_cascade.T @ refined_cascade, identity)

    generator = np.diag([0.40, 1.30])
    depth = 0.70
    transfer = np.diag(np.exp(-depth * np.diag(generator)))
    continuous_residue_square = identity - transfer.T @ transfer
    continuous_column = np.vstack(
        [transfer, positive_square_root(continuous_residue_square)]
    )
    assert np.allclose(continuous_column.T @ continuous_column, identity)
    residue_floor = float(np.linalg.eigvalsh(continuous_residue_square)[0])
    recovered_edge = -np.log(1.0 - residue_floor) / (2.0 * depth)
    assert np.isclose(recovered_edge, 0.40)

    partition = [0.0, 0.19, 0.43, depth]
    partitioned_residue_square = np.zeros_like(identity)
    for left, right in zip(partition[:-1], partition[1:]):
        incoming = np.diag(np.exp(-left * np.diag(generator)))
        stage = np.diag(np.exp(-(right - left) * np.diag(generator)))
        partitioned_residue_square += incoming.T @ (identity - stage.T @ stage) @ incoming
    partition_error = operator_norm(partitioned_residue_square - continuous_residue_square)
    assert partition_error < 1e-12

    clock_parameter = 0.31
    clock = np.diag(np.exp(-1j * clock_parameter * np.diag(generator)))
    enlarged_clock = np.block(
        [[clock, np.zeros_like(clock)], [np.zeros_like(clock), clock]]
    )
    intertwiner_error = operator_norm(
        continuous_column.astype(complex) @ clock
        - enlarged_clock @ continuous_column.astype(complex)
    )
    assert intertwiner_error < 1e-12

    print("directed isometric residue completion receipt: PASS")
    print(
        "proper positive column input/output rank = "
        f"{np.linalg.matrix_rank(first_column)} / {first_column.shape[0]}"
    )
    print(
        "coisometric column unitarity residues = "
        f"{operator_norm(unitary_column.T @ unitary_column - identity):.9f} / "
        f"{operator_norm(unitary_column @ unitary_column.T - identity):.9f}"
    )
    print(f"universal residual factorization error = {factorization_error:.9f}")
    print(
        "discrete cascade isometry residue = "
        f"{operator_norm(discrete_cascade.T @ discrete_cascade - identity):.9f}"
    )
    print(
        "endpoint-unitary chronological archive rank = "
        f"{np.linalg.matrix_rank(chronological_column)} / {chronological_column.shape[0]}"
    )
    print(f"Schaeffer compression-of-powers error = {max(power_errors):.9f}")
    print(
        "refined response-residual isometry residue = "
        f"{operator_norm(refined_cascade.T @ refined_cascade - identity):.9f}"
    )
    print(
        "continuous residue floor / recovered generator edge = "
        f"{residue_floor:.9f} / {recovered_edge:.9f}"
    )
    print(f"partitioned residue Gramian error = {partition_error:.9f}")
    print(f"residue-clock intertwiner error = {intertwiner_error:.9f}")


if __name__ == "__main__":
    main()
