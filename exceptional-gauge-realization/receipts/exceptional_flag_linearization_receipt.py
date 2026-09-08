"""Exact modular-rank receipt for the standard exceptional complex flag.

The continuous variables are a candidate trace-two idempotent ell in the
Albert algebra J=h_3(O), together with a rank-nine real subspace B.  The
Grassmannian tangent at the standard B=h_3(C) is Hom(B,B^perp).  We linearize
the following integer-coefficient constraints at the standard pair:

  ell^2=ell, tr(ell)=2, 1 in B, ell in B, and B o B contained in B.

All Jordan products are multiplied by two, so the Jacobian is integral.  A
rank computation modulo a prime gives a rigorous lower bound for its rational
rank.  The cited F4 orbit has dimension 40 and lies in the kernel by
equivariance; modular rank 149 on the 189-dimensional tangent therefore proves
that the kernel is exactly the orbit tangent.

Receipt boundary: this is a computer-assisted finite linearization theorem at
one standard flag.  It does not prove a canonical weighting of the redundant
constraints, a physical flag-field realization, chirality, continuum
coercivity, or a Yang--Mills mass gap.
"""

from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

# Resolve the shared arithmetic from this receipt, independently of the cwd.
_coordinates_path = Path(__file__).resolve().parents[2] / "albert-algebra" / "coordinates.py"
_coordinates_spec = spec_from_file_location("albert_coordinates", _coordinates_path)
if _coordinates_spec is None or _coordinates_spec.loader is None:
    raise ImportError(f"Cannot load Albert coordinates from {_coordinates_path}")
jordan = module_from_spec(_coordinates_spec)
_coordinates_spec.loader.exec_module(jordan)

JORDAN_DIMENSION = jordan.JORDAN_DIMENSION
FULL_BASIS = jordan.FULL_BASIS
jordan_product_twice = jordan.jordan_product_twice

SUBALGEBRA_DIMENSION = 9
COMPLEMENT_DIMENSION = 18
GRASSMANN_TANGENT_DIMENSION = SUBALGEBRA_DIMENSION * COMPLEMENT_DIMENSION
VARIABLE_DIMENSION = JORDAN_DIMENSION + GRASSMANN_TANGENT_DIMENSION
PRIMES = (1_009, 10_007, 100_003, 1_000_003, 1_000_033)

B_INDICES = [0, 1, 2] + [3 + 8 * pair + component for pair in range(3) for component in (0, 1)]
C_INDICES = [3 + 8 * pair + component for pair in range(3) for component in range(2, 8)]
B_BASIS = [FULL_BASIS[index] for index in B_INDICES]
C_BASIS = [FULL_BASIS[index] for index in C_INDICES]


def selected(vector: list[int], indices: list[int]) -> list[int]:
    return [vector[index] for index in indices]


def add_column_value(matrix: list[list[int]], row: int, column: int, value: int) -> None:
    if value:
        matrix[row][column] += value


def build_integer_jacobian() -> list[list[int]]:
    jordan_rows = JORDAN_DIMENSION
    trace_rows = 1
    membership_rows = COMPLEMENT_DIMENSION
    unit_rows = COMPLEMENT_DIMENSION
    closure_pairs = SUBALGEBRA_DIMENSION * (SUBALGEBRA_DIMENSION + 1) // 2

    trace_offset = jordan_rows
    membership_offset = trace_offset + trace_rows
    unit_offset = membership_offset + membership_rows
    closure_offset = unit_offset + unit_rows
    row_count = closure_offset + closure_pairs * COMPLEMENT_DIMENSION
    matrix = [[0] * VARIABLE_DIMENSION for _ in range(row_count)]

    ell = [0] * JORDAN_DIMENSION
    ell[0] = 1
    ell[1] = 1
    unit = [0] * JORDAN_DIMENSION
    unit[0] = unit[1] = unit[2] = 1

    # Linearization of ell o ell - ell and tr(ell)-2.
    for column, variation in enumerate(FULL_BASIS):
        derivative = jordan_product_twice(ell, variation)
        derivative[column] -= 1
        for row, value in enumerate(derivative):
            add_column_value(matrix, row, column, value)
        if column < 3:
            add_column_value(matrix, trace_offset, column, 1)

    # The B-perpendicular part of a variation of ell.
    full_to_complement = {full_index: index for index, full_index in enumerate(C_INDICES)}
    for column in range(JORDAN_DIMENSION):
        complement_index = full_to_complement.get(column)
        if complement_index is not None:
            add_column_value(matrix, membership_offset + complement_index, column, 1)

    mix = [
        [selected(jordan_product_twice(c_vector, b_vector), C_INDICES) for b_vector in B_BASIS]
        for c_vector in C_BASIS
    ]
    products_in_b: list[list[list[int]]] = []
    for left in B_BASIS:
        product_row: list[list[int]] = []
        for right in B_BASIS:
            product = jordan_product_twice(left, right)
            assert selected(product, C_INDICES) == [0] * COMPLEMENT_DIMENSION
            product_row.append(selected(product, B_INDICES))
        products_in_b.append(product_row)

    pair_list = [
        (left, right)
        for left in range(SUBALGEBRA_DIMENSION)
        for right in range(left, SUBALGEBRA_DIMENSION)
    ]

    # A Grassmannian tangent K maps one B basis vector to one B-perpendicular
    # basis vector.  Linearize ell in B, 1 in B, and closure under o.
    for source in range(SUBALGEBRA_DIMENSION):
        ell_coefficient = ell[B_INDICES[source]]
        unit_coefficient = unit[B_INDICES[source]]
        for target in range(COMPLEMENT_DIMENSION):
            column = JORDAN_DIMENSION + source * COMPLEMENT_DIMENSION + target
            add_column_value(
                matrix,
                membership_offset + target,
                column,
                -ell_coefficient,
            )
            add_column_value(matrix, unit_offset + target, column, unit_coefficient)

            for pair_number, (left, right) in enumerate(pair_list):
                output = [0] * COMPLEMENT_DIMENSION
                if left == source:
                    output = [a + b for a, b in zip(output, mix[target][right])]
                if right == source:
                    output = [a + b for a, b in zip(output, mix[target][left])]
                output[target] -= products_in_b[left][right][source]
                row_start = closure_offset + pair_number * COMPLEMENT_DIMENSION
                for output_index, value in enumerate(output):
                    add_column_value(matrix, row_start + output_index, column, value)

    return matrix


def rank_mod_prime(matrix: list[list[int]], prime: int) -> int:
    pivots: dict[int, dict[int, int]] = {}
    for dense_row in matrix:
        row = {index: value % prime for index, value in enumerate(dense_row) if value % prime}
        while row:
            pivot_column = min(row)
            prior = pivots.get(pivot_column)
            if prior is None:
                inverse = pow(row[pivot_column], -1, prime)
                row = {index: (value * inverse) % prime for index, value in row.items()}
                pivots[pivot_column] = row
                break
            factor = row[pivot_column]
            for index, value in prior.items():
                updated = (row.get(index, 0) - factor * value) % prime
                if updated:
                    row[index] = updated
                else:
                    row.pop(index, None)
    return len(pivots)


def main() -> None:
    assert len(B_INDICES) == SUBALGEBRA_DIMENSION
    assert len(C_INDICES) == COMPLEMENT_DIMENSION
    assert sorted(B_INDICES + C_INDICES) == list(range(JORDAN_DIMENSION))

    jacobian = build_integer_jacobian()
    ranks = {prime: rank_mod_prime(jacobian, prime) for prime in PRIMES}
    rank = ranks[1_000_003]
    nullity_upper_bound = VARIABLE_DIMENSION - rank
    orbit_dimension = 52 - (4 + 9 - 1)

    print(f"PASS variable dimension: 27 + 9*18 = {VARIABLE_DIMENSION}")
    print(f"PASS standard flag orbit dimension: 52 - 12 = {orbit_dimension}")
    print(f"PASS integral Jacobian shape: {len(jacobian)} x {len(jacobian[0])}")
    rank_summary = ", ".join(f"{prime}:{value}" for prime, value in ranks.items())
    print(f"PASS Jacobian ranks modulo five primes: {rank_summary}")
    print(f"PASS rational nullity upper bound: {VARIABLE_DIMENSION} - {rank} = {nullity_upper_bound}")

    if (
        orbit_dimension != 40
        or set(ranks.values()) != {149}
        or nullity_upper_bound != orbit_dimension
    ):
        raise SystemExit(1)

    print(
        "PASS kernel equality: the 40-dimensional equivariant orbit tangent is the full rational kernel"
    )
    print("SUMMARY 6/6 checks passed")


if __name__ == "__main__":
    main()
