#!/usr/bin/env python3
"""Finite arithmetic checks for the paired-wall short and Cayley response.

The receipt uses finite orthogonal projections in Halmos form. It verifies the
weighted shorting formula, its common kernel, the single-wall no-go, and the
equal-weight tanh identity for a supplied transfer spectrum. It proves no
infinite-dimensional, Markov, Type-III, continuum, or Yang--Mills claim.
"""

from __future__ import annotations

import math

import numpy as np


TOLERANCE = 2e-12
checks: list[bool] = []


def check(name: str, condition: bool, detail: str) -> None:
    checks.append(bool(condition))
    print(("PASS" if condition else "FAIL") + f"  {name}: {detail}")


def projection_pair(cosines: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return projections P,Q with principal cosines given by ``cosines``."""
    cosine = np.diag(cosines)
    sine = np.diag(np.sqrt(1.0 - cosines**2))
    size = len(cosines)
    zero = np.zeros((size, size))
    identity = np.eye(size)
    p = np.block([[identity, zero], [zero, zero]])
    q = np.block(
        [
            [cosine @ cosine, cosine @ sine],
            [cosine @ sine, sine @ sine],
        ]
    )
    return p, q


def short_to_first_block(matrix: np.ndarray, kept: int) -> np.ndarray:
    """Schur-short a positive matrix to its first ``kept`` coordinates."""
    retained = matrix[:kept, :kept]
    coupling = matrix[:kept, kept:]
    hidden = matrix[kept:, kept:]
    return retained - coupling @ np.linalg.solve(hidden, coupling.T)


def main() -> None:
    # Include one common direction (cosine 1) and two reduced directions.
    cosines = np.array([1.0, 0.8, 0.35])
    p, q = projection_pair(cosines)
    identity = np.eye(p.shape[0])
    size = len(cosines)

    projection_error = max(
        float(np.max(np.abs(p @ p - p))),
        float(np.max(np.abs(q @ q - q))),
        float(np.max(np.abs(p.T - p))),
        float(np.max(np.abs(q.T - q))),
    )
    check(
        "orthogonal projections",
        projection_error < TOLERANCE,
        f"max projection error = {projection_error:.3e}",
    )

    alpha = 0.7
    beta = 1.3
    whole = alpha * (identity - p) + beta * (identity - q)
    short = short_to_first_block(whole, size)
    compression = (p @ q @ p)[:size, :size]
    expected = (
        alpha
        * beta
        * (np.eye(size) - compression)
        @ np.linalg.inv(alpha * np.eye(size) + beta * compression)
    )
    formula_error = float(np.max(np.abs(short - expected)))
    check(
        "weighted paired-wall formula",
        formula_error < TOLERANCE,
        f"max formula error = {formula_error:.3e}",
    )

    expected_floor = alpha * beta * (1.0 - 0.8**2) / (alpha + beta * 0.8**2)
    eigenvalues = np.linalg.eigvalsh(short)
    positive_eigenvalues = eigenvalues[eigenvalues > TOLERANCE]
    check(
        "common kernel and sharp reduced floor",
        abs(float(eigenvalues[0])) < TOLERANCE
        and math.isclose(float(positive_eigenvalues[0]), expected_floor, abs_tol=TOLERANCE),
        f"spectrum = {np.array2string(eigenvalues, precision=9)}",
    )

    single_wall = alpha * (identity - p)
    single_short = short_to_first_block(single_wall, size)
    single_norm = float(np.linalg.norm(single_short, ord=2))
    check(
        "single-wall retained-carrier no-go",
        single_norm < TOLERANCE,
        f"short norm = {single_norm:.3e}",
    )

    # A transfer T=exp(-aH) gives principal cosines T^d. Its return is T^(2d),
    # and the equal-weight short is the Cayley transform tanh(d a H).
    energies = np.array([0.4, 1.1, 2.0])
    step = 0.17
    separation = 3
    slab = step * separation
    transfer_cosines = np.exp(-slab * energies)
    p_transfer, q_transfer = projection_pair(transfer_cosines)
    transfer_identity = np.eye(p_transfer.shape[0])
    paired_transfer = (transfer_identity - p_transfer) + (
        transfer_identity - q_transfer
    )
    transfer_short = short_to_first_block(paired_transfer, len(energies))
    round_trip = (p_transfer @ q_transfer @ p_transfer)[: len(energies), : len(energies)]
    expected_return = np.diag(np.exp(-2.0 * slab * energies))
    return_error = float(np.max(np.abs(round_trip - expected_return)))
    check(
        "finite projection return",
        return_error < TOLERANCE,
        f"max |PQP-exp(-2 d a H)| = {return_error:.3e}",
    )

    expected_tanh = np.diag(np.tanh(slab * energies))
    tanh_error = float(np.max(np.abs(transfer_short - expected_tanh)))
    check(
        "Cayley/tanh relation",
        tanh_error < TOLERANCE,
        f"max |short-tanh(d a H)| = {tanh_error:.3e}",
    )

    computed_edge = float(np.linalg.eigvalsh(transfer_short)[0])
    expected_edge = math.tanh(slab * float(np.min(energies)))
    check(
        "tanh edge",
        math.isclose(computed_edge, expected_edge, abs_tol=TOLERANCE),
        f"computed = {computed_edge:.9f}, expected = {expected_edge:.9f}",
    )

    if not all(checks):
        raise SystemExit(1)

    print(f"SUMMARY  {sum(checks)}/{len(checks)} checks passed")
    print("scope: finite projection arithmetic only; no continuum or Yang--Mills claim")


if __name__ == "__main__":
    main()
