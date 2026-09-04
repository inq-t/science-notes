"""Finite checks for the reverse-prediction residue archive.

This receipt verifies identities only.  It does not establish a regulator-uniform
innovation floor or any continuum Yang-Mills claim.
"""

from itertools import product

import numpy as np


TOL = 2.0e-13


def weighted_inner(left, right, weights):
    return np.vdot(left, weights * right)


def stationary_paths(transition, horizon):
    """Enumerate a uniform-stationary finite path of length horizon + 1."""
    dimension = transition.shape[0]
    paths = np.asarray(list(product(range(dimension), repeat=horizon + 1)))
    weights = np.full(len(paths), 1.0 / dimension)
    for time in range(horizon):
        weights *= transition[paths[:, time], paths[:, time + 1]]
    assert abs(weights.sum() - 1.0) < TOL
    return paths, weights


def predictor_vectors(transition, observable, horizon, paths):
    """M_k = (P*)^k f(X_k) for a uniform invariant distribution."""
    backward = transition.T
    predictors = []
    for depth in range(horizon + 1):
        predicted_observable = np.linalg.matrix_power(backward, depth) @ observable
        predictors.append(predicted_observable[paths[:, depth]])
    return predictors


def direct_suffix_conditionals(observable, paths, weights, depth):
    """Compute E[f(X_0) | X_depth,...,X_horizon] by grouping suffixes."""
    numerators = {}
    denominators = {}
    for path, weight in zip(paths, weights):
        suffix = tuple(path[depth:])
        numerators[suffix] = numerators.get(suffix, 0.0) + weight * observable[path[0]]
        denominators[suffix] = denominators.get(suffix, 0.0) + weight
    return np.asarray(
        [numerators[tuple(path[depth:])] / denominators[tuple(path[depth:])] for path in paths]
    )


def path_ledger(transition, observable, horizon):
    paths, weights = stationary_paths(transition, horizon)
    predictors = predictor_vectors(transition, observable, horizon, paths)
    increments = [predictors[k] - predictors[k + 1] for k in range(horizon)]

    conditional_error = max(
        np.max(
            np.abs(
                predictors[k]
                - direct_suffix_conditionals(observable, paths, weights, k)
            )
        )
        for k in range(horizon + 1)
    )

    pieces = increments + [predictors[-1]]
    gram = np.asarray(
        [[weighted_inner(left, right, weights) for right in pieces] for left in pieces]
    )
    off_diagonal = gram - np.diag(np.diag(gram))
    orthogonality_error = np.max(np.abs(off_diagonal))

    initial_norm_squared = np.mean(np.abs(observable) ** 2)
    ledger_sum = float(np.real(np.trace(gram)))
    ledger_error = abs(initial_norm_squared - ledger_sum)

    backward = transition.T
    defect = np.eye(len(observable)) - backward.T @ backward
    telescope = np.zeros_like(transition)
    for depth in range(horizon):
        power = np.linalg.matrix_power(backward, depth)
        telescope += power.T @ defect @ power
    survivor = np.linalg.matrix_power(backward, horizon)
    telescope_target = np.eye(len(observable)) - survivor.T @ survivor
    telescope_error = np.linalg.norm(telescope - telescope_target, ord=2)

    assert conditional_error < TOL
    assert orthogonality_error < TOL
    assert ledger_error < TOL
    assert telescope_error < TOL
    return conditional_error, orthogonality_error, ledger_error, telescope_error


def main():
    horizon = 3
    observable = np.asarray([1.0, -1.0, 0.0])

    # P = 0.4 I + 0.6 Pi_constants: reversible and Hilbert-positive.
    reversible = np.full((3, 3), 0.2)
    np.fill_diagonal(reversible, 0.6)
    rev_errors = path_ledger(reversible, observable, horizon)

    centered_projection = np.eye(3) - np.ones((3, 3)) / 3.0
    centered_power = np.linalg.matrix_power(reversible, horizon) @ centered_projection
    centered_norm = np.linalg.norm(centered_power, ord=2)
    optimal_floor = 1.0 - centered_norm**2
    assert abs(centered_norm - 0.4**horizon) < TOL
    assert abs(optimal_floor - (1.0 - 0.4 ** (2 * horizon))) < TOL

    # Uniform-stationary but nonreversible: the archive must follow P*.
    nonreversible = np.asarray(
        [
            [0.5, 0.4, 0.1],
            [0.1, 0.5, 0.4],
            [0.4, 0.1, 0.5],
        ]
    )
    assert np.linalg.norm(nonreversible - nonreversible.T) > 0.1
    nonrev_errors = path_ledger(nonreversible, observable, horizon)

    # Reversible Markov does not imply Hilbert positivity: the -1 mode is
    # invisible to I-P^2 even though it is not fixed by P.
    period_two = np.asarray([[0.0, 1.0], [1.0, 0.0]])
    alternating = np.asarray([1.0, -1.0])
    reverse_defect = np.eye(2) - period_two @ period_two
    dirichlet_response = (np.eye(2) - period_two) @ alternating
    assert np.linalg.norm(reverse_defect @ alternating) < TOL
    assert abs(np.linalg.norm(dirichlet_response) - 2.0 * np.linalg.norm(alternating)) < TOL

    print("reverse prediction residue receipt: PASS")
    print(f"reversible spectrum: {np.linalg.eigvalsh(reversible)}")
    print(f"fixed slab depth: {horizon}")
    print(f"centered survivor norm: {centered_norm:.12f}")
    print(f"optimal innovation floor: {optimal_floor:.12f}")
    print(f"reversible max conditional error: {rev_errors[0]:.3e}")
    print(f"reversible max orthogonality error: {rev_errors[1]:.3e}")
    print(f"reversible norm-ledger error: {rev_errors[2]:.3e}")
    print(f"reversible operator-telescope error: {rev_errors[3]:.3e}")
    print(f"nonreversible max conditional error: {nonrev_errors[0]:.3e}")
    print(f"nonreversible max orthogonality error: {nonrev_errors[1]:.3e}")
    print(f"nonreversible norm-ledger error: {nonrev_errors[2]:.3e}")
    print(f"nonreversible operator-telescope error: {nonrev_errors[3]:.3e}")
    print(f"period-two innovation-defect norm: {np.linalg.norm(reverse_defect):.3e}")
    print(f"period-two Dirichlet-response norm: {np.linalg.norm(dirichlet_response):.12f}")


if __name__ == "__main__":
    main()
