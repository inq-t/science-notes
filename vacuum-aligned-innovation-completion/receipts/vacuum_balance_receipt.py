"""Finite receipt for the vacuum-balance completion theorem.

The effective physical carrier of two Z2 links has basis {1, z}, where z is
the charged-pair/global-loop character.  A correlated state with
r(z) = 1 + kappa*z has uniform regional marginals, but its half-density
sqrt(r) has components in both blocks.  Since both blocks are one
dimensional, internal centering sees nothing; their relative vacuum balance
is the entire physical vacuum complement.
"""

from __future__ import annotations

import numpy as np


def matrix_rank(operator: np.ndarray) -> int:
    return int(np.linalg.matrix_rank(operator, tol=1e-12))


def op_norm(operator: np.ndarray) -> float:
    return float(np.linalg.svd(operator, compute_uv=False)[0])


def main() -> None:
    kappa = 0.60
    transfer_eigenvalue = 0.73

    z = np.array([-1.0, 1.0])
    stationary = 0.5 * (1.0 + kappa * z)
    correlation_density = 2.0 * stationary

    trivial = np.ones(2) / np.sqrt(2.0)
    charged_pair = z / np.sqrt(2.0)
    e_trivial = np.outer(trivial, trivial)
    e_charged = np.outer(charged_pair, charged_pair)

    vacuum = np.sqrt(stationary)
    vacuum_trivial = e_trivial @ vacuum
    vacuum_charged = e_charged @ vacuum
    p_trivial = float(vacuum_trivial @ vacuum_trivial)
    p_charged = float(vacuum_charged @ vacuum_charged)

    q_trivial_internal = (
        e_trivial
        - np.outer(vacuum_trivial, vacuum_trivial) / p_trivial
    )
    q_charged_internal = (
        e_charged
        - np.outer(vacuum_charged, vacuum_charged) / p_charged
    )
    p_vacuum = np.outer(vacuum, vacuum)
    q_balance = e_trivial + e_charged - p_vacuum
    naive_centered = q_trivial_internal + q_charged_internal

    markov = (
        transfer_eigenvalue * np.eye(2)
        + (1.0 - transfer_eigenvalue)
        * np.tile(stationary, (2, 1))
    )
    symmetric_transfer = (
        np.diag(np.sqrt(stationary))
        @ markov
        @ np.diag(1.0 / np.sqrt(stationary))
    )

    assert np.all(correlation_density > 0.0)
    assert np.allclose(stationary.sum(), 1.0)
    assert np.allclose(p_trivial + p_charged, 1.0)
    assert np.allclose(symmetric_transfer, symmetric_transfer.T)
    assert np.allclose(symmetric_transfer @ vacuum, vacuum)
    assert matrix_rank(q_trivial_internal) == 0
    assert matrix_rank(q_charged_internal) == 0
    assert matrix_rank(naive_centered) == 0
    assert matrix_rank(q_balance) == 1
    assert np.allclose(
        naive_centered + q_balance,
        np.eye(2) - p_vacuum,
    )

    balance_transfer_norm = op_norm(
        q_balance @ symmetric_transfer @ q_balance
    )
    assert np.isclose(balance_transfer_norm, transfer_eigenvalue)

    print("vacuum balance receipt: PASS")
    print(f"correlation kappa = {kappa:.9f}")
    print(
        "half-density block weights = "
        f"[{p_trivial:.9f}, {p_charged:.9f}]"
    )
    print(f"naive internal-centered rank = {matrix_rank(naive_centered)}")
    print(f"vacuum-balance rank = {matrix_rank(q_balance)}")
    print(f"physical centered rank = {matrix_rank(np.eye(2) - p_vacuum)}")
    print(f"transfer eigenvalue = {transfer_eigenvalue:.9f}")
    print(f"balance transfer norm = {balance_transfer_norm:.9f}")


if __name__ == "__main__":
    main()
