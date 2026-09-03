"""Finite arithmetic checks for the Jordan idempotency-gap note.

Receipt boundary: this script checks Peirce multiplicities, homogeneous-space
dimension balances, and the explicit h_5(C) projector linearization.  It does
not prove the exceptional flag-stabilizer theorem, regularity of the proposed
flag constraint, chirality, a continuum limit, or a Yang--Mills mass gap.
"""

from __future__ import annotations

from math import sqrt


TOLERANCE = 1.0e-12


def zero_matrix(size: int) -> list[list[complex]]:
    return [[0j for _ in range(size)] for _ in range(size)]


def frobenius_norm(matrix: list[list[complex]]) -> float:
    return sqrt(sum(abs(entry) ** 2 for row in matrix for entry in row))


def projector_derivative(matrix: list[list[complex]], rank: int) -> list[list[complex]]:
    """Return p h + h p - h for p = diag(1_rank, 0)."""

    size = len(matrix)
    result = zero_matrix(size)
    for row in range(size):
        for column in range(size):
            p_row = 1 if row < rank else 0
            p_column = 1 if column < rank else 0
            result[row][column] = (p_row + p_column - 1) * matrix[row][column]
    return result


def hermitian_basis_on_pairs(size: int, pairs: list[tuple[int, int]]) -> list[list[list[complex]]]:
    basis: list[list[list[complex]]] = []
    for row, column in pairs:
        real = zero_matrix(size)
        real[row][column] = 1 / sqrt(2)
        real[column][row] = 1 / sqrt(2)
        basis.append(real)

        imaginary = zero_matrix(size)
        imaginary[row][column] = 1j / sqrt(2)
        imaginary[column][row] = -1j / sqrt(2)
        basis.append(imaginary)
    return basis


def diagonal_basis(size: int, indices: range) -> list[list[list[complex]]]:
    basis: list[list[list[complex]]] = []
    for index in indices:
        matrix = zero_matrix(size)
        matrix[index][index] = 1
        basis.append(matrix)
    return basis


def record(name: str, passed: bool, detail: str) -> bool:
    status = "PASS" if passed else "FAIL"
    print(f"{status} {name}: {detail}")
    return passed


def main() -> None:
    checks: list[bool] = []

    exceptional_peirce = (1, 16, 10)
    checks.append(
        record(
            "exceptional Peirce balance",
            sum(exceptional_peirce) == 27,
            "1 + 16 + 10 = 27",
        )
    )
    hessian_zero = exceptional_peirce[1]
    hessian_one = exceptional_peirce[0] + exceptional_peirce[2]
    checks.append(
        record(
            "exceptional Hessian multiplicities",
            (hessian_zero, hessian_one) == (16, 11),
            "spec((2L_e-I)^2) = {0^(16), 1^(11)}",
        )
    )
    checks.append(
        record(
            "Cayley-plane orbit balance",
            52 - 36 == hessian_zero,
            "dim(F4) - dim(Spin(9)) = 52 - 36 = 16",
        )
    )
    rank_two_peirce = (10, 16, 1)
    checks.append(
        record(
            "rank-two exceptional Peirce balance",
            sum(rank_two_peirce) == 27
            and (rank_two_peirce[1], rank_two_peirce[0] + rank_two_peirce[2]) == (16, 11),
            "10 + 16 + 1 = 27 and the Hessian multiplicities remain 0^(16), 1^(11)",
        )
    )
    checks.append(
        record(
            "Jordan-frame triality balance",
            52 - 28 == 8 + 8 + 8,
            "dim(F4/Spin(8)) = 24 = dim(8_v + 8_s + 8_c)",
        )
    )
    checks.append(
        record(
            "exceptional flag orbit balance",
            52 - (4 + 9 - 1) == 40,
            "dim(F4/S(U(2)xU(3))) = 52 - 12 = 40",
        )
    )
    checks.append(
        record(
            "flag fibration balance",
            (52 - 16) + (8 - 4) == 40,
            "dim h3(C)-subalgebra orbit 36 + dim Gr_2(C^3) 4 = 40",
        )
    )

    size = 5
    rank = 2
    cross_pairs = [(row, column) for row in range(rank) for column in range(rank, size)]
    tangent_basis = hermitian_basis_on_pairs(size, cross_pairs)

    top_pairs = [(row, column) for row in range(rank) for column in range(row + 1, rank)]
    bottom_pairs = [
        (row, column)
        for row in range(rank, size)
        for column in range(row + 1, size)
    ]
    normal_basis = (
        diagonal_basis(size, range(size))
        + hermitian_basis_on_pairs(size, top_pairs)
        + hermitian_basis_on_pairs(size, bottom_pairs)
    )

    tangent_error = max(frobenius_norm(projector_derivative(item, rank)) for item in tangent_basis)
    checks.append(
        record(
            "h5(C) tangent kernel",
            len(tangent_basis) == 12 and tangent_error < TOLERANCE,
            f"12 cross-block real directions; max ||DC_p(h)|| = {tangent_error:.3e}",
        )
    )

    normal_norm_error = max(
        abs(frobenius_norm(projector_derivative(item, rank)) - frobenius_norm(item))
        for item in normal_basis
    )
    checks.append(
        record(
            "h5(C) unit normal edge",
            len(normal_basis) == 13 and normal_norm_error < TOLERANCE,
            f"13 block-diagonal directions; max norm error = {normal_norm_error:.3e}",
        )
    )

    su5_dimension = size**2 - 1
    stabilizer_dimension = rank**2 + (size - rank) ** 2 - 1
    orbit_dimension = su5_dimension - stabilizer_dimension
    checks.append(
        record(
            "h5(C) stabilizer/orbit balance",
            (su5_dimension, stabilizer_dimension, orbit_dimension) == (24, 12, 12),
            "dim SU(5) = 24, dim S(U(2)xU(3)) = 12, orbit dim = 12",
        )
    )

    alpha = 7.0
    checks.append(
        record(
            "normalization firewall",
            alpha * 1.0 == 7.0,
            "V -> 7V sends the dimensionless Hessian edge 1 -> 7",
        )
    )

    passed = sum(checks)
    total = len(checks)
    print(f"SUMMARY {passed}/{total} checks passed")
    if passed != total:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
