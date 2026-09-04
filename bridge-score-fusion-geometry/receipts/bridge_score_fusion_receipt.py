"""Finite checks for bridge-score fusion geometry.

This receipt checks conditional-projection, score, half-density, Doob, and
same-carrier operator identities in one two-state model. It does not prove a
volume-uniform bridge minorization, a continuum limit, OS reconstruction, or
a Yang--Mills mass gap.
"""

from __future__ import annotations

import math


TOL = 2.0e-11
FINITE_DIFFERENCE_STEP = 1.0e-6
STATES = range(2)


def transition(time: float) -> list[list[float]]:
    retained = math.exp(-time)
    return [
        [0.5 * (1.0 + retained), 0.5 * (1.0 - retained)],
        [0.5 * (1.0 - retained), 0.5 * (1.0 + retained)],
    ]


def transpose(matrix: list[list[float]]) -> list[list[float]]:
    return [list(column) for column in zip(*matrix, strict=True)]


def multiply(
    left: list[list[float]], right: list[list[float]]
) -> list[list[float]]:
    right_transpose = transpose(right)
    return [
        [
            sum(x * y for x, y in zip(row, column, strict=True))
            for column in right_transpose
        ]
        for row in left
    ]


def identity(size: int) -> list[list[float]]:
    return [
        [1.0 if row == column else 0.0 for column in range(size)]
        for row in range(size)
    ]


def subtract(
    left: list[list[float]], right: list[list[float]]
) -> list[list[float]]:
    return [
        [x - y for x, y in zip(left_row, right_row, strict=True)]
        for left_row, right_row in zip(left, right, strict=True)
    ]


def max_abs(values) -> float:
    return max(abs(value) for value in values)


def bridge(
    first: list[list[float]], second: list[list[float]]
) -> tuple[list[list[float]], list[list[list[float]]]]:
    composite = multiply(first, second)
    fibers = [
        [
            [
                first[initial][middle]
                * second[middle][final]
                / composite[initial][final]
                for middle in STATES
            ]
            for final in STATES
        ]
        for initial in STATES
    ]
    return composite, fibers


def endpoint_projection(
    path_function: list[list[list[float]]],
    fibers: list[list[list[float]]],
) -> list[list[list[float]]]:
    projected = [
        [
            sum(
                fibers[initial][final][middle]
                * path_function[initial][middle][final]
                for middle in STATES
            )
            for final in STATES
        ]
        for initial in STATES
    ]
    return [
        [
            [projected[initial][final] for final in STATES]
            for _middle in STATES
        ]
        for initial in STATES
    ]


def weighted_path_inner(
    left: list[list[list[float]]],
    right: list[list[list[float]]],
    stationary: list[float],
    first: list[list[float]],
    second: list[list[float]],
) -> float:
    return sum(
        stationary[initial]
        * first[initial][middle]
        * second[middle][final]
        * left[initial][middle][final]
        * right[initial][middle][final]
        for initial in STATES
        for middle in STATES
        for final in STATES
    )


def tilted_fiber(
    base: list[float], observable: list[float], theta: float
) -> list[float]:
    weights = [
        base[middle] * math.exp(theta * observable[middle])
        for middle in STATES
    ]
    normalization = sum(weights)
    return [weight / normalization for weight in weights]


def symmetric_two_by_two_eigenvalues(
    matrix: list[list[float]],
) -> tuple[float, float]:
    trace = matrix[0][0] + matrix[1][1]
    discriminant = math.sqrt(
        (matrix[0][0] - matrix[1][1]) ** 2
        + 4.0 * matrix[0][1] * matrix[1][0]
    )
    return 0.5 * (trace - discriminant), 0.5 * (trace + discriminant)


def perron_pair(matrix: list[list[float]]) -> tuple[float, list[float]]:
    low, high = symmetric_two_by_two_eigenvalues(matrix)
    del low
    vector = [matrix[0][1], high - matrix[0][0]]
    norm = math.sqrt(sum(entry * entry for entry in vector))
    return high, [entry / norm for entry in vector]


def main() -> None:
    half_time = 0.7
    stationary = [0.5, 0.5]
    first = transition(half_time)
    second = transition(half_time)
    composite, fibers = bridge(first, second)

    test = [
        [
            [0.3 + 1.1 * initial - 0.7 * middle + 0.2 * final for final in STATES]
            for middle in STATES
        ]
        for initial in STATES
    ]
    comparison = [
        [
            [-0.4 + 0.3 * initial + 0.9 * middle - 0.6 * final for final in STATES]
            for middle in STATES
        ]
        for initial in STATES
    ]
    projected = endpoint_projection(test, fibers)
    projected_twice = endpoint_projection(projected, fibers)
    projection_error = max_abs(
        projected_twice[i][j][k] - projected[i][j][k]
        for i in STATES
        for j in STATES
        for k in STATES
    )
    residue = [
        [
            [test[i][j][k] - projected[i][j][k] for k in STATES]
            for j in STATES
        ]
        for i in STATES
    ]
    projected_comparison = endpoint_projection(comparison, fibers)
    projection_orthogonality_error = abs(
        weighted_path_inner(
            residue,
            projected_comparison,
            stationary,
            first,
            second,
        )
    )

    observable = [1.0, -1.0]
    score = [
        [
            [
                observable[middle]
                - sum(
                    fibers[initial][final][other] * observable[other]
                    for other in STATES
                )
                for middle in STATES
            ]
            for final in STATES
        ]
        for initial in STATES
    ]
    score_mean_error = max_abs(
        sum(
            fibers[initial][final][middle] * score[initial][final][middle]
            for middle in STATES
        )
        for initial in STATES
        for final in STATES
    )

    score_difference_error = 0.0
    half_density_difference_error = 0.0
    half_density_gramian = 0.0
    fisher_gramian = 0.0
    for initial in STATES:
        for final in STATES:
            base = fibers[initial][final]
            plus = tilted_fiber(base, observable, FINITE_DIFFERENCE_STEP)
            minus = tilted_fiber(base, observable, -FINITE_DIFFERENCE_STEP)
            endpoint_weight = stationary[initial] * composite[initial][final]
            for middle in STATES:
                numerical_score = (
                    math.log(plus[middle]) - math.log(minus[middle])
                ) / (2.0 * FINITE_DIFFERENCE_STEP)
                score_difference_error = max(
                    score_difference_error,
                    abs(numerical_score - score[initial][final][middle]),
                )
                numerical_half_derivative = (
                    math.sqrt(plus[middle]) - math.sqrt(minus[middle])
                ) / (2.0 * FINITE_DIFFERENCE_STEP)
                expected_half_derivative = (
                    0.5
                    * score[initial][final][middle]
                    * math.sqrt(base[middle])
                )
                half_density_difference_error = max(
                    half_density_difference_error,
                    abs(numerical_half_derivative - expected_half_derivative),
                )
                half_density_gramian += (
                    endpoint_weight * numerical_half_derivative**2
                )
                fisher_gramian += (
                    endpoint_weight
                    * base[middle]
                    * score[initial][final][middle] ** 2
                )
    quarter_factor_error = abs(half_density_gramian - 0.25 * fisher_gramian)

    gram_form = [[0.0, 0.0], [0.0, 0.0]]
    for left_state in STATES:
        for right_state in STATES:
            gram_form[left_state][right_state] = sum(
                stationary[initial]
                * composite[initial][final]
                * sum(
                    fibers[initial][final][middle]
                    * (
                        (1.0 if middle == left_state else 0.0)
                        - fibers[initial][final][left_state]
                    )
                    * (
                        (1.0 if middle == right_state else 0.0)
                        - fibers[initial][final][right_state]
                    )
                    for middle in STATES
                )
                for initial in STATES
                for final in STATES
            )
    bridge_operator = [
        [gram_form[row][column] / stationary[row] for column in STATES]
        for row in STATES
    ]
    transfer_defect = subtract(identity(2), multiply(transpose(first), first))
    comparison_operator = subtract(transfer_defect, bridge_operator)
    comparison_eigenvalues = symmetric_two_by_two_eigenvalues(comparison_operator)
    bridge_eigenvalues = symmetric_two_by_two_eigenvalues(bridge_operator)

    kernel = [[1.4, 0.35], [0.35, 0.8]]
    action_weight = [1.25, 0.75]
    scalar = 0.63
    wilson = [
        [
            scalar
            * action_weight[initial]
            * kernel[initial][final]
            * action_weight[final]
            for final in STATES
        ]
        for initial in STATES
    ]
    perron_value, perron_vector = perron_pair(wilson)
    doob = [
        [
            wilson[initial][final]
            * perron_vector[final]
            / (perron_value * perron_vector[initial])
            for final in STATES
        ]
        for initial in STATES
    ]
    doob_row_error = max_abs(sum(row) - 1.0 for row in doob)
    doob_composite = multiply(doob, doob)
    wilson_bridge_error = 0.0
    for initial in STATES:
        for final in STATES:
            simplified_weights = [
                kernel[initial][middle]
                * action_weight[middle] ** 2
                * kernel[middle][final]
                for middle in STATES
            ]
            simplified_total = sum(simplified_weights)
            for middle in STATES:
                doob_bridge = (
                    doob[initial][middle]
                    * doob[middle][final]
                    / doob_composite[initial][final]
                )
                simplified_bridge = (
                    simplified_weights[middle] / simplified_total
                )
                wilson_bridge_error = max(
                    wilson_bridge_error,
                    abs(doob_bridge - simplified_bridge),
                )

    assert projection_error < TOL
    assert projection_orthogonality_error < TOL
    assert score_mean_error < TOL
    assert score_difference_error < 2.0e-9
    assert half_density_difference_error < 2.0e-9
    assert quarter_factor_error < 2.0e-9
    assert min(bridge_eigenvalues) > -TOL
    assert min(comparison_eigenvalues) > -TOL
    assert max(comparison_eigenvalues) > 1.0e-3
    assert doob_row_error < TOL
    assert wilson_bridge_error < TOL

    print("bridge-score fusion geometry: finite two-state receipt")
    print(f"conditional-projection error = {projection_error:.3e}")
    print(f"projection orthogonality error = {projection_orthogonality_error:.3e}")
    print(f"centered-score error = {score_mean_error:.3e}")
    print(f"score finite-difference error = {score_difference_error:.3e}")
    print(
        "half-density finite-difference error = "
        f"{half_density_difference_error:.3e}"
    )
    print(f"Fisher Gramian = {fisher_gramian:.12f}")
    print(f"half-density Gramian = {half_density_gramian:.12f}")
    print(f"one-quarter-factor error = {quarter_factor_error:.3e}")
    print(f"bridge-Gramian eigenvalues = {bridge_eigenvalues}")
    print(f"defect-minus-bridge eigenvalues = {comparison_eigenvalues}")
    print(f"Doob row-sum error = {doob_row_error:.3e}")
    print(f"Wilson/Doob bridge-cancellation error = {wilson_bridge_error:.3e}")
    print("PASS: bridge score is a centered fusion residue below transfer defect")


if __name__ == "__main__":
    main()
