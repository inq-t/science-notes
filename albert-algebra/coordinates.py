"""Exact coordinates for the compact Albert algebra h_3(O).

The ordered basis contains three real diagonals followed by the eight
octonion components of entries (0, 1), (0, 2), and (1, 2).  Lower entries
are conjugates.  jordan_product_twice computes xy + yx in this integral
basis; its trace Gram matrix is diag(1, 1, 1, 2, ..., 2).  The binary
octonionic matrix products do not assert matrix associativity.

This module supplies coordinates only: it selects no context, invariant
measure, constraint Jacobian, physical carrier, or clock.
"""

from __future__ import annotations

OCTONION_DIMENSION = 8
JORDAN_DIMENSION = 27

FANO_TRIPLES = (
    (1, 2, 3),
    (1, 4, 5),
    (1, 7, 6),
    (2, 4, 6),
    (2, 5, 7),
    (3, 4, 7),
    (3, 6, 5),
)

OFF_DIAGONAL_PAIRS = ((0, 1), (0, 2), (1, 2))


def octonion_table() -> list[list[tuple[int, int]]]:
    table = [[(0, 0) for _ in range(OCTONION_DIMENSION)] for _ in range(OCTONION_DIMENSION)]
    for index in range(OCTONION_DIMENSION):
        table[0][index] = (1, index)
        table[index][0] = (1, index)
    for index in range(1, OCTONION_DIMENSION):
        table[index][index] = (-1, 0)
    for first, second, third in FANO_TRIPLES:
        cyclic = ((first, second, third), (second, third, first), (third, first, second))
        for left, right, result in cyclic:
            table[left][right] = (1, result)
            table[right][left] = (-1, result)
    assert all(sign != 0 for row in table for sign, _ in row)
    return table


OCTONION_TABLE = octonion_table()


def octonion_zero() -> list[int]:
    return [0] * OCTONION_DIMENSION


def octonion_add(left: list[int], right: list[int]) -> list[int]:
    return [a + b for a, b in zip(left, right)]


def octonion_conjugate(value: list[int]) -> list[int]:
    return [value[0], *(-entry for entry in value[1:])]


def octonion_multiply(left: list[int], right: list[int]) -> list[int]:
    result = octonion_zero()
    for left_index, left_value in enumerate(left):
        if left_value == 0:
            continue
        for right_index, right_value in enumerate(right):
            if right_value == 0:
                continue
            sign, output_index = OCTONION_TABLE[left_index][right_index]
            result[output_index] += sign * left_value * right_value
    return result


def matrix_zero() -> list[list[list[int]]]:
    return [[octonion_zero() for _ in range(3)] for _ in range(3)]


def matrix_add(
    left: list[list[list[int]]], right: list[list[list[int]]]
) -> list[list[list[int]]]:
    result = matrix_zero()
    for row in range(3):
        for column in range(3):
            result[row][column] = octonion_add(left[row][column], right[row][column])
    return result


def matrix_multiply(
    left: list[list[list[int]]], right: list[list[list[int]]]
) -> list[list[list[int]]]:
    result = matrix_zero()
    for row in range(3):
        for column in range(3):
            entry = octonion_zero()
            for middle in range(3):
                entry = octonion_add(
                    entry,
                    octonion_multiply(left[row][middle], right[middle][column]),
                )
            result[row][column] = entry
    return result


def coordinate_basis(index: int) -> list[int]:
    vector = [0] * JORDAN_DIMENSION
    vector[index] = 1
    return vector


def vector_to_hermitian(vector: list[int]) -> list[list[list[int]]]:
    matrix = matrix_zero()
    for diagonal in range(3):
        matrix[diagonal][diagonal][0] = vector[diagonal]
    for pair_index, (row, column) in enumerate(OFF_DIAGONAL_PAIRS):
        start = 3 + OCTONION_DIMENSION * pair_index
        value = vector[start : start + OCTONION_DIMENSION]
        matrix[row][column] = value.copy()
        matrix[column][row] = octonion_conjugate(value)
    return matrix


def hermitian_to_vector(matrix: list[list[list[int]]]) -> list[int]:
    vector = [0] * JORDAN_DIMENSION
    for diagonal in range(3):
        assert matrix[diagonal][diagonal][1:] == [0] * 7
        vector[diagonal] = matrix[diagonal][diagonal][0]
    for pair_index, (row, column) in enumerate(OFF_DIAGONAL_PAIRS):
        assert matrix[column][row] == octonion_conjugate(matrix[row][column])
        start = 3 + OCTONION_DIMENSION * pair_index
        vector[start : start + OCTONION_DIMENSION] = matrix[row][column]
    return vector


def jordan_product_twice(left: list[int], right: list[int]) -> list[int]:
    left_matrix = vector_to_hermitian(left)
    right_matrix = vector_to_hermitian(right)
    product_twice = matrix_add(
        matrix_multiply(left_matrix, right_matrix),
        matrix_multiply(right_matrix, left_matrix),
    )
    return hermitian_to_vector(product_twice)


FULL_BASIS = [coordinate_basis(index) for index in range(JORDAN_DIMENSION)]
