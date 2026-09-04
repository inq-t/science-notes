"""Finite checks for vacuum-balance Fisher and transfer geometry."""

from __future__ import annotations

import numpy as np


def op_norm(operator: np.ndarray) -> float:
    return float(np.linalg.svd(operator, compute_uv=False)[0])


def main() -> None:
    weights = np.array([0.9, 0.1])
    amplitude_score = np.array(
        [
            np.sqrt(weights[1] / weights[0]),
            -np.sqrt(weights[0] / weights[1]),
        ]
    )

    assert np.isclose(weights @ amplitude_score, 0.0)
    amplitude_norm_sq = float(
        np.sum(weights * amplitude_score**2)
    )
    probability_score = 2.0 * amplitude_score
    fisher_speed_sq = float(
        np.sum(weights * probability_score**2)
    )
    assert np.isclose(amplitude_norm_sq, 1.0)
    assert np.isclose(fisher_speed_sq, 4.0 * amplitude_norm_sq)

    phase_weight_velocity = 2.0 * np.real(
        np.sqrt(weights)
        * np.conjugate(1j * amplitude_score * np.sqrt(weights))
    )
    assert np.allclose(phase_weight_velocity, 0.0)

    balance_norm = 0.73
    internal_norm = 0.55
    cross_norm = 0.12
    centered_transfer = np.array(
        [
            [balance_norm, cross_norm],
            [cross_norm, internal_norm],
        ]
    )
    eigenvalues = np.linalg.eigvalsh(centered_transfer)
    scalar_majorant = 0.5 * (
        balance_norm
        + internal_norm
        + np.sqrt(
            (balance_norm - internal_norm) ** 2
            + 4.0 * cross_norm**2
        )
    )
    shorted_balance_defect = (
        1.0
        - balance_norm
        - cross_norm**2 / (1.0 - internal_norm)
    )
    leave_and_return = cross_norm**2

    assert eigenvalues[0] > 0.0
    assert np.isclose(op_norm(centered_transfer), scalar_majorant)
    assert scalar_majorant < 1.0
    assert cross_norm**2 < (
        (1.0 - balance_norm) * (1.0 - internal_norm)
    )
    assert shorted_balance_defect > 0.0
    assert np.isclose(
        (centered_transfer @ centered_transfer)[0, 0],
        balance_norm**2 + leave_and_return,
    )

    print("vacuum-balance Fisher receipt: PASS")
    print(f"block weights = {weights.tolist()}")
    print(f"amplitude tangent norm^2 = {amplitude_norm_sq:.9f}")
    print(f"Fisher speed^2 = {fisher_speed_sq:.9f}")
    print(
        "phase block-weight velocity norm = "
        f"{np.linalg.norm(phase_weight_velocity):.9f}"
    )
    print(f"complete transfer norm = {scalar_majorant:.9f}")
    print(
        "shorted balance defect = "
        f"{shorted_balance_defect:.9f}"
    )
    print(f"leave-and-return correction = {leave_and_return:.9f}")


if __name__ == "__main__":
    main()
