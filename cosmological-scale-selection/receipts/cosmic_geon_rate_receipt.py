"""Arithmetic witnesses for the cosmic-geon rate ledger.

This receipt checks only the displayed FLRW algebra, the comoving-radiation
logarithmic rate, and the additive relative-entropy residue for finite
classical channels. It does not prove the Einstein equations, horizon
thermodynamics, a cosmic-geon ontology, a Type-III descent theorem, or a
Yang--Mills mass gap.
"""

from __future__ import annotations

import math

import numpy as np


def relative_entropy(p: np.ndarray, q: np.ndarray) -> float:
    """Classical finite relative entropy for strictly positive vectors."""
    return float(np.sum(p * np.log(p / q)))


def normalize_rows(matrix: np.ndarray) -> np.ndarray:
    return matrix / matrix.sum(axis=1, keepdims=True)


def main() -> None:
    rng = np.random.default_rng(20260903)

    # Arbitrary positive unit representatives; all tested identities are
    # homogeneous and do not depend on their numerical choice.
    c = 2.7
    newton_g = 0.43
    hbar = 1.9

    deceleration_samples = np.concatenate(
        (
            np.array([-1.3, -1.0, -0.9, 0.0, 1.0, 2.0]),
            rng.uniform(-1.5, 2.0, 994),
        )
    )
    for deceleration in deceleration_samples:
        hubble = float(np.exp(rng.normal()))
        deceleration = float(deceleration)
        hubble_dot = -(1.0 + deceleration) * hubble**2

        radius = c / hubble
        critical_density = 3.0 * c**2 * hubble**2 / (
            8.0 * math.pi * newton_g
        )
        horizon_volume = 4.0 * math.pi * radius**3 / 3.0
        misner_sharp_energy = c**4 * radius / (2.0 * newton_g)
        energy = c**5 / (2.0 * newton_g * hubble)
        mass = energy / c**2
        theta = hbar * hubble / (2.0 * math.pi)
        capacity = math.pi * c**5 / (newton_g * hbar * hubble**2)
        power = (1.0 + deceleration) * c**5 / newton_g

        energy_dot = -c**5 * hubble_dot / (
            2.0 * newton_g * hubble**2
        )
        capacity_dot = -2.0 * capacity * hubble_dot / hubble
        theta_dot = theta * hubble_dot / hubble

        assert math.isclose(energy, theta * capacity, rel_tol=2e-14)
        assert math.isclose(
            energy, critical_density * horizon_volume, rel_tol=2e-14
        )
        assert math.isclose(energy, misner_sharp_energy, rel_tol=2e-14)
        assert math.isclose(
            2.0 * newton_g * mass / (radius * c**2), 1.0, rel_tol=2e-14
        )
        assert math.isclose(
            power / energy,
            capacity_dot / capacity,
            rel_tol=2e-14,
        )
        assert math.isclose(
            power / energy,
            2.0 * hubble * (1.0 + deceleration),
            rel_tol=2e-14,
        )
        assert math.isclose(energy_dot, power / 2.0, rel_tol=2e-14)
        assert math.isclose(theta * capacity_dot, power, rel_tol=2e-14)
        assert math.isclose(capacity * theta_dot, -power / 2.0, rel_tol=2e-14)

        # For E_gamma = E_0/a and a_dot = H*a, -E_dot/E = H.
        scale_factor = float(np.exp(rng.normal()))
        radiation_energy = 3.1 / scale_factor
        radiation_energy_dot = -radiation_energy * hubble
        assert math.isclose(
            -radiation_energy_dot / radiation_energy, hubble, rel_tol=2e-14
        )

    minimum_residue = math.inf
    maximum_allocation_error = 0.0
    for _ in range(1000):
        p = rng.random(4) + 0.1
        q = rng.random(4) + 0.1
        p /= p.sum()
        q /= q.sum()
        first = normalize_rows(rng.random((4, 3)) + 0.1)
        second = normalize_rows(rng.random((3, 2)) + 0.1)

        p_first = p @ first
        q_first = q @ first
        p_second = p_first @ second
        q_second = q_first @ second

        residue_first = relative_entropy(p, q) - relative_entropy(
            p_first, q_first
        )
        residue_second = relative_entropy(
            p_first, q_first
        ) - relative_entropy(p_second, q_second)
        residue_composite = relative_entropy(p, q) - relative_entropy(
            p_second, q_second
        )

        minimum_residue = min(
            minimum_residue, residue_first, residue_second, residue_composite
        )
        allocation_error = abs(
            residue_composite - residue_first - residue_second
        )
        maximum_allocation_error = max(
            maximum_allocation_error, allocation_error
        )

        assert residue_first >= -2e-14
        assert residue_second >= -2e-14
        assert residue_composite >= -2e-14
        assert allocation_error <= 2e-14

    print("cosmic-geon rate ledger: 1000 random arithmetic witnesses passed")
    print("critical compactness and E = temperature * capacity passed")
    print("P/E = d log(capacity)/dt = 2 H (1+q) passed")
    print("E_dot = P/2 and temperature/capacity allocation passed")
    print("comoving radiation: -d log(E_gamma)/dt = H passed")
    print(
        "channel descent: nonnegative, composition-additive KL residue passed"
    )
    print(f"minimum sampled residue: {minimum_residue:.12e}")
    print(f"maximum allocation error: {maximum_allocation_error:.12e}")
    print(
        "scope: arithmetic/classical-channel checks only; no cosmic-geon or "
        "mass-gap theorem"
    )


if __name__ == "__main__":
    main()
