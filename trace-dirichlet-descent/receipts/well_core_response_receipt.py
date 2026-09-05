"""Finite harmonic-core, inherited-metric and source-capacity checks."""

import numpy as np


def close(actual, expected, tolerance=1e-10):
    assert np.max(np.abs(np.asarray(actual) - expected)) < tolerance


def laplacian(size, edges):
    operator = np.zeros((size, size))
    for i, j, conductance in edges:
        operator[i, i] += conductance
        operator[j, j] += conductance
        operator[i, j] -= conductance
        operator[j, i] -= conductance
    return operator


def harmonic_data(operator, probability, retained):
    total = len(probability)
    lift = np.zeros((total, retained))
    lift[:retained] = np.eye(retained)
    lift[retained:] = -np.linalg.solve(
        operator[retained:, retained:], operator[retained:, :retained]
    )
    energy = lift.T @ operator @ lift
    metric = lift.T @ (probability[:, None] * lift)
    weights = probability @ lift
    return lift, energy, metric, weights


def four_vertex_check():
    operator = laplacian(4, ((0, 3, 2), (1, 3, 1), (2, 3, 1), (0, 1, 6)))
    probability = np.full(4, 0.25)
    lift, energy, metric, weights = harmonic_data(operator, probability, 3)
    close(lift[3], np.array((0.5, 0.25, 0.25)))
    expected_metric = np.array(((20, 2, 2), (2, 17, 1), (2, 1, 17))) / 64
    expected_energy = np.array(((28, -26, -2), (-26, 27, -1), (-2, -1, 3))) / 4
    close(metric, expected_metric)
    close(energy, expected_energy)
    inherited = np.linalg.solve(metric, energy)
    close(inherited[2, 1], 2 / 11)
    assert -inherited[2, 1] < 0
    diagonal_operator = energy / weights[:, None]
    assert np.max(diagonal_operator - np.diag(np.diag(diagonal_operator))) <= 1e-10
    print("PASS exact four-vertex non-Markov inherited operator witness")


def graph_checks():
    rng = np.random.default_rng(128)
    for retained in (2, 3, 4):
        for _ in range(8):
            total = retained + 3
            edges = tuple(
                (i, j, rng.uniform(0.2, 2))
                for i in range(total) for j in range(i + 1, total)
            )
            operator = laplacian(total, edges)
            probability = rng.uniform(0.2, 2, total)
            probability /= probability.sum()
            lift, energy, metric, weights = harmonic_data(operator, probability, retained)
            close(lift.sum(axis=1), 1)
            assert np.min(lift) > -1e-12
            close(energy.sum(axis=1), 0)
            assert np.max(energy - np.diag(np.diag(energy))) <= 1e-10
            diagonal = np.diag(weights)
            ambiguity = sum(
                probability[j] * (np.diag(lift[j]) - np.outer(lift[j], lift[j]))
                for j in range(total)
            )
            close(diagonal - metric, ambiguity)
            assert np.linalg.eigvalsh(ambiguity).min() > -1e-10
            assert np.linalg.eigvalsh(metric - np.diag(probability[:retained])).min() > -1e-10
            perturbation = np.zeros(total)
            perturbation[retained:] = rng.normal(size=total - retained)
            close(lift.T @ operator @ perturbation, 0)
            score = rng.normal(size=total)
            score -= probability @ score
            demand = probability * score
            retained_demand = lift.T @ demand
            full_cost = demand @ np.linalg.pinv(operator) @ demand
            lower_cost = retained_demand @ np.linalg.pinv(energy) @ retained_demand
            assert lower_cost <= full_cost + 1e-10
            if retained == 2:
                h = lift[:, 0]
                p = probability @ h
                variance = probability @ (h - p) ** 2
                capacity = energy[0, 0]
                source = demand @ h
                close(p * (1 - p) - variance, probability @ (h * (1 - h)))
                exact_rate = capacity / variance
                lumped_rate = capacity / (p * (1 - p))
                close((source**2 / variance) / exact_rate, source**2 / capacity)
                close((source**2 / (p * (1 - p))) / lumped_rate, lower_cost)
                spectrum = np.linalg.eigvals(np.linalg.solve(metric, energy))
                close(np.max(spectrum.real), exact_rate)
                assert exact_rate >= lumped_rate - 1e-10
    print("PASS 24 harmonic-core graphs: energy, Gram ambiguity, source-capacity bounds")
    print("PASS eight binary inherited/lumped rate and invariant-quotient checks")


if __name__ == "__main__":
    four_vertex_check()
    graph_checks()
    print("Scope: finite analogues, not proofs of Sobolev domains or physical mass gaps")
