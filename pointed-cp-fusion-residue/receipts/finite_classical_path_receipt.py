"""Finite checks for the pointed CP fusion-residue construction.

This receipt verifies a two-state classical UCP semigroup and finite matrix
identities only. It does not construct a physical record, entropy, clock,
causal net, Yang--Mills transfer matrix, or mass gap.
"""

from __future__ import annotations

import math


TOL = 2.0e-12


def transition(time: float) -> list[list[float]]:
    retained = math.exp(-time)
    diagonal = 0.5 * (1.0 + retained)
    off_diagonal = 0.5 * (1.0 - retained)
    return [[diagonal, off_diagonal], [off_diagonal, diagonal]]


def zeros(rows: int, columns: int) -> list[list[float]]:
    return [[0.0 for _ in range(columns)] for _ in range(rows)]


def identity(size: int) -> list[list[float]]:
    result = zeros(size, size)
    for index in range(size):
        result[index][index] = 1.0
    return result


def transpose(matrix: list[list[float]]) -> list[list[float]]:
    return [list(column) for column in zip(*matrix, strict=True)]


def multiply(
    left: list[list[float]], right: list[list[float]]
) -> list[list[float]]:
    right_transpose = transpose(right)
    return [
        [sum(x * y for x, y in zip(row, column, strict=True)) for column in right_transpose]
        for row in left
    ]


def add(
    left: list[list[float]], right: list[list[float]]
) -> list[list[float]]:
    return [
        [x + y for x, y in zip(left_row, right_row, strict=True)]
        for left_row, right_row in zip(left, right, strict=True)
    ]


def subtract(
    left: list[list[float]], right: list[list[float]]
) -> list[list[float]]:
    return [
        [x - y for x, y in zip(left_row, right_row, strict=True)]
        for left_row, right_row in zip(left, right, strict=True)
    ]


def diagonal(entries: list[float]) -> list[list[float]]:
    result = zeros(len(entries), len(entries))
    for index, entry in enumerate(entries):
        result[index][index] = entry
    return result


def max_abs(matrix: list[list[float]]) -> float:
    return max(abs(entry) for row in matrix for entry in row)


def trace(matrix: list[list[float]]) -> float:
    return sum(matrix[index][index] for index in range(len(matrix)))


def inclusion(
    first: list[list[float]],
    second: list[list[float]],
    composite: list[list[float]],
) -> list[list[float]]:
    endpoints = [(initial, final) for initial in range(2) for final in range(2)]
    paths = [
        (initial, middle, final)
        for initial in range(2)
        for middle in range(2)
        for final in range(2)
    ]
    result = zeros(len(paths), len(endpoints))
    for row, (initial, middle, final) in enumerate(paths):
        for column, endpoint in enumerate(endpoints):
            if endpoint == (initial, final):
                result[row][column] = math.sqrt(
                    first[middle][initial]
                    * second[final][middle]
                    / composite[final][initial]
                )
    return result


def main() -> None:
    first_time = 0.3
    second_time = 0.7
    third_time = 1.1

    first = transition(first_time)
    second = transition(second_time)
    third = transition(third_time)
    first_second = transition(first_time + second_time)
    second_third = transition(second_time + third_time)
    total = transition(first_time + second_time + third_time)

    semigroup_error = max_abs(subtract(multiply(second, first), first_second))
    assert semigroup_error < TOL
    assert all(entry > 0.0 for row in first for entry in row)

    endpoint_dimension = sum(entry > 0.0 for row in first_second for entry in row)
    path_dimension = sum(
        first[middle][initial] * second[final][middle] > 0.0
        for initial in range(2)
        for middle in range(2)
        for final in range(2)
    )
    assert endpoint_dimension == 4
    assert path_dimension == 8

    inclusion_matrix = inclusion(first, second, first_second)
    endpoint_descent = transpose(inclusion_matrix)
    endpoint_identity_error = max_abs(
        subtract(multiply(endpoint_descent, inclusion_matrix), identity(4))
    )
    assert endpoint_identity_error < TOL

    retained_projection = multiply(inclusion_matrix, endpoint_descent)
    residue_projection = subtract(identity(8), retained_projection)
    retained_projection_error = max_abs(
        subtract(
            multiply(retained_projection, retained_projection), retained_projection
        )
    )
    residue_projection_error = max_abs(
        subtract(multiply(residue_projection, residue_projection), residue_projection)
    )
    assert retained_projection_error < TOL
    assert residue_projection_error < TOL
    assert abs(trace(retained_projection) - 4.0) < TOL
    assert abs(trace(residue_projection) - 4.0) < TOL

    associativity_error = 0.0
    for initial in range(2):
        for first_middle in range(2):
            for second_middle in range(2):
                for final in range(2):
                    left_parenthesized = math.sqrt(
                        first_second[second_middle][initial]
                        * third[final][second_middle]
                        / total[final][initial]
                    ) * math.sqrt(
                        first[first_middle][initial]
                        * second[second_middle][first_middle]
                        / first_second[second_middle][initial]
                    )
                    right_parenthesized = math.sqrt(
                        first[first_middle][initial]
                        * second_third[final][first_middle]
                        / total[final][initial]
                    ) * math.sqrt(
                        second[second_middle][first_middle]
                        * third[final][second_middle]
                        / second_third[final][first_middle]
                    )
                    associativity_error = max(
                        associativity_error,
                        abs(left_parenthesized - right_parenthesized),
                    )
    assert associativity_error < TOL

    endpoint_unitary = diagonal([1.0, -1.0, -1.0, 1.0])
    retained_corner_unitary = multiply(
        multiply(inclusion_matrix, endpoint_unitary), endpoint_descent
    )
    corner_unitary_error = max_abs(
        subtract(
            multiply(transpose(retained_corner_unitary), retained_corner_unitary),
            retained_projection,
        )
    )
    assert corner_unitary_error < TOL

    full_extension = add(retained_corner_unitary, residue_projection)
    full_extension_error = max_abs(
        subtract(multiply(transpose(full_extension), full_extension), identity(8))
    )
    descended = multiply(multiply(endpoint_descent, full_extension), inclusion_matrix)
    descent_error = max_abs(subtract(descended, endpoint_unitary))
    assert full_extension_error < TOL
    assert descent_error < TOL

    print("pointed CP fusion residue: finite classical-path receipt")
    print(f"semigroup composition error = {semigroup_error:.3e}")
    print(f"GNS endpoint dimension = {endpoint_dimension}")
    print(f"two-step fusion path dimension = {path_dimension}")
    print(f"retained projection trace = {trace(retained_projection):.12f}")
    print(f"fusion residue projection trace = {trace(residue_projection):.12f}")
    print(f"V*V identity error = {endpoint_identity_error:.3e}")
    print(f"retained projection error = {retained_projection_error:.3e}")
    print(f"residue projection error = {residue_projection_error:.3e}")
    print(f"three-step associativity error = {associativity_error:.3e}")
    print(f"retained-corner unitary error = {corner_unitary_error:.3e}")
    print(f"full-extension unitary error = {full_extension_error:.3e}")
    print(f"coisometric descent error = {descent_error:.3e}")
    print("PASS: pointwise GNS fusion is a proper cyclic inclusion")


if __name__ == "__main__":
    main()
