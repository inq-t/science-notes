"""Finite witnesses for background fibres and shorted response.

This receipt checks the classical conditional KL decomposition and bounded
positive-block Schur identities. It does not construct a fact, a Type-III
carrier, a physical Hamiltonian, or a Yang--Mills mass gap.
"""

from __future__ import annotations

import numpy as np


def relative_entropy(p: np.ndarray, r: np.ndarray) -> float:
    return float(np.sum(p * np.log(p / r)))


def main() -> None:
    rng = np.random.default_rng(20260903)

    # A deterministic readout with three nontrivial antecedent fibres.
    fibres = (
        np.array([0, 1, 2]),
        np.array([3, 4]),
        np.array([5, 6, 7, 8]),
    )
    maximum_kl_error = 0.0
    minimum_kl_residue = np.inf
    for _ in range(1000):
        p = rng.random(9) + 0.1
        r = rng.random(9) + 0.1
        p /= p.sum()
        r /= r.sum()

        p_visible = np.array([p[fibre].sum() for fibre in fibres])
        r_visible = np.array([r[fibre].sum() for fibre in fibres])
        conditional_residue = 0.0
        for index, fibre in enumerate(fibres):
            p_conditional = p[fibre] / p_visible[index]
            r_conditional = r[fibre] / r_visible[index]
            conditional_residue += p_visible[index] * relative_entropy(
                p_conditional, r_conditional
            )

        residue = relative_entropy(p, r) - relative_entropy(
            p_visible, r_visible
        )
        error = abs(residue - conditional_residue)
        maximum_kl_error = max(maximum_kl_error, error)
        minimum_kl_residue = min(minimum_kl_residue, residue)
        assert residue >= -2e-14
        assert error <= 2e-14

    maximum_square_error = 0.0
    minimum_short_edge = np.inf
    maximum_order_error = 0.0
    for _ in range(1000):
        hidden_seed = rng.normal(size=(3, 3))
        hidden = hidden_seed.T @ hidden_seed + 0.5 * np.eye(3)
        coupling = rng.normal(size=(2, 3))
        retained_seed = rng.normal(size=(2, 2))
        short = retained_seed.T @ retained_seed + 0.2 * np.eye(2)
        retained = short + coupling @ np.linalg.solve(hidden, coupling.T)
        whole = np.block(
            [[retained, coupling], [coupling.T, hidden]]
        )

        whole_spectrum = np.linalg.eigvalsh(whole)
        recovered_short = retained - coupling @ np.linalg.solve(
            hidden, coupling.T
        )
        assert whole_spectrum[0] >= -2e-12
        assert np.allclose(recovered_short, short, atol=2e-12)

        x = rng.normal(size=2)
        z = rng.normal(size=3)
        minimizing_z = -np.linalg.solve(hidden, coupling.T @ x)
        vector = np.concatenate((x, z))
        left = float(vector @ whole @ vector)
        completed = z - minimizing_z
        right = float(
            completed @ hidden @ completed + x @ recovered_short @ x
        )
        minimum = float(
            np.concatenate((x, minimizing_z))
            @ whole
            @ np.concatenate((x, minimizing_z))
        )
        maximum_square_error = max(maximum_square_error, abs(left - right))
        assert abs(left - right) <= 2e-10
        assert abs(minimum - float(x @ recovered_short @ x)) <= 2e-10

        minimum_short_edge = min(
            minimum_short_edge, float(np.linalg.eigvalsh(recovered_short)[0])
        )
        order_spectrum = np.linalg.eigvalsh(retained - recovered_short)
        maximum_order_error = max(
            maximum_order_error, max(0.0, float(-order_spectrum[0]))
        )
        assert order_spectrum[0] >= -2e-12

        # The raw forgetting projection is zero on every retained vector.
        retained_vector = np.concatenate((x, np.zeros(3)))
        forgetting_projection = np.diag([0.0, 0.0, 1.0, 1.0, 1.0])
        assert np.allclose(forgetting_projection @ retained_vector, 0.0)

    print("pointed-background receipt: 1000 KL and 1000 Schur witnesses passed")
    print("KL residue equals expected conditional fibre divergence")
    print("shorted response equals the least whole cost over hidden extensions")
    print("raw forgetting projection vanishes on the retained carrier")
    print(f"minimum sampled KL residue: {minimum_kl_residue:.12e}")
    print(f"maximum KL allocation error: {maximum_kl_error:.12e}")
    print(f"minimum sampled short edge: {minimum_short_edge:.12e}")
    print(f"maximum completed-square error: {maximum_square_error:.12e}")
    print(f"maximum order-cone error: {maximum_order_error:.12e}")
    print("scope: finite classical/block identities only; no mass-gap theorem")


if __name__ == "__main__":
    main()
