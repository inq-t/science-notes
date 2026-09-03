"""Finite stationary-path witness for the past--future angle theorem.

The receipt constructs two conditional-expectation projections from a reversible
three-state Markov pair. It checks the Friedrichs cosine, the alternating
round trip, the two-projection frame edge, and the distinction between a
shrinking one-step separation and a fixed physical slab. It makes no
continuum or Yang--Mills claim.
"""

from __future__ import annotations

import math

import numpy as np


GENERATOR = np.array(
    [
        [1.0, -1.0, 0.0],
        [-1.0, 2.0, -1.0],
        [0.0, -1.0, 1.0],
    ]
)
STATE_COUNT = GENERATOR.shape[0]
PI = np.full(STATE_COUNT, 1.0 / STATE_COUNT)


def transfer(thickness: float) -> np.ndarray:
    """Return exp(-thickness * GENERATOR) by symmetric spectral calculus."""
    eigenvalues, eigenvectors = np.linalg.eigh(GENERATOR)
    matrix = (eigenvectors * np.exp(-thickness * eigenvalues)) @ eigenvectors.T
    assert np.allclose(matrix, matrix.T)
    assert np.allclose(matrix.sum(axis=1), 1.0)
    assert np.min(matrix) >= -1e-13
    return matrix


def projection_witness(step: float, separation_steps: int) -> tuple[float, float, float]:
    """Construct endpoint sigma-algebra projections on the weighted pair carrier."""
    thickness = step * separation_steps
    transition = transfer(thickness)
    joint = PI[:, None] * transition
    assert np.allclose(joint.sum(axis=1), PI)
    assert np.allclose(joint.sum(axis=0), PI)

    # Weighted-coordinate indicator isometries for sigma(X_0) and sigma(X_d).
    path_count = STATE_COUNT * STATE_COUNT
    past_basis = np.zeros((path_count, STATE_COUNT))
    future_basis = np.zeros((path_count, STATE_COUNT))
    constant = np.zeros(path_count)
    row = 0
    for past_state in range(STATE_COUNT):
        for future_state in range(STATE_COUNT):
            root_weight = math.sqrt(joint[past_state, future_state])
            past_basis[row, past_state] = root_weight / math.sqrt(PI[past_state])
            future_basis[row, future_state] = root_weight / math.sqrt(PI[future_state])
            constant[row] = root_weight
            row += 1

    identity_states = np.eye(STATE_COUNT)
    assert np.allclose(past_basis.T @ past_basis, identity_states)
    assert np.allclose(future_basis.T @ future_basis, identity_states)
    assert math.isclose(float(constant @ constant), 1.0, abs_tol=1e-12)

    e_past = past_basis @ past_basis.T
    e_future = future_basis @ future_basis.T
    p0 = np.outer(constant, constant)
    p = e_past - p0
    q = e_future - p0

    friedrichs_cosine = float(np.linalg.norm(p @ q, ord=2))
    expected_cosine = math.exp(-thickness)
    assert math.isclose(friedrichs_cosine, expected_cosine, abs_tol=2e-12)

    alternating_norm = float(np.linalg.norm(q @ p @ q, ord=2))
    assert math.isclose(alternating_norm, expected_cosine**2, abs_tol=2e-12)

    frame = 2.0 * np.eye(path_count) - e_past - e_future
    frame_spectrum = np.linalg.eigvalsh(frame)
    positive_spectrum = frame_spectrum[frame_spectrum > 1e-10]
    frame_floor = float(positive_spectrum[0])
    assert math.isclose(frame_floor, 1.0 - expected_cosine, abs_tol=2e-12)

    # Compression of the round trip to the centered future endpoint carrier.
    q_state = np.eye(STATE_COUNT) - np.ones((STATE_COUNT, STATE_COUNT)) / STATE_COUNT
    compressed = future_basis.T @ (q @ p @ q) @ future_basis
    expected_compressed = transfer(2.0 * thickness) - np.ones(
        (STATE_COUNT, STATE_COUNT)
    ) / STATE_COUNT
    assert np.allclose(compressed, expected_compressed, atol=2e-12)
    assert np.allclose(compressed @ q_state, compressed)

    recovered_gap = -math.log(friedrichs_cosine) / thickness
    assert math.isclose(recovered_gap, 1.0, abs_tol=2e-12)
    return friedrichs_cosine, frame_floor, alternating_norm


def main() -> None:
    eigenvalues, eigenvectors = np.linalg.eigh(GENERATOR)
    assert np.allclose(eigenvalues, (0.0, 1.0, 3.0))

    # In units hbar*c=1, integral_0^infinity exp(-2 ell H) d ell
    # is (1/2) H^{-1} on the vacuum complement. The zero below is its
    # zero extension to the vacuum; the unprojected integral diverges there.
    inverse_spectrum = np.zeros_like(eigenvalues)
    inverse_spectrum[eigenvalues > 1e-12] = 1.0 / eigenvalues[eigenvalues > 1e-12]
    dwell = 0.5 * (eigenvectors * inverse_spectrum) @ eigenvectors.T
    dwell_spectrum = np.linalg.eigvalsh(dwell)
    assert np.allclose(dwell_spectrum, (0.0, 1.0 / 6.0, 1.0 / 2.0))
    dwell_norm = float(np.linalg.norm(dwell, ord=2))
    recovered_gap_from_dwell = 1.0 / (2.0 * dwell_norm)
    assert math.isclose(recovered_gap_from_dwell, 1.0, abs_tol=2e-12)

    print("past--future angle: finite reversible three-state witness")
    print("separation exponent d (step = 0.2)")
    print("d    c_F           expected       round_trip")
    for separation_steps in (1, 2, 3, 5):
        cosine, _, round_trip = projection_witness(0.2, separation_steps)
        print(
            f"{separation_steps:1d}    {cosine:.9f}   "
            f"{math.exp(-0.2 * separation_steps):.9f}   {round_trip:.9f}"
        )

    print("adjacent slices: raw floor vanishes; logarithmic rate stays fixed")
    print("a          1-c_F         -log(c_F)/a")
    for step in (0.5, 0.25, 0.125, 0.0625):
        cosine, frame_floor, _ = projection_witness(step, 1)
        print(f"{step:.4f}     {frame_floor:.9f}    {-math.log(cosine) / step:.9f}")

    print("fixed physical thickness: raw angle stays fixed")
    print("a          d       c_F           1-c_F")
    for separation_steps in (1, 2, 4, 8):
        step = 1.0 / separation_steps
        cosine, frame_floor, _ = projection_witness(step, separation_steps)
        print(
            f"{step:.4f}     {separation_steps:1d}       "
            f"{cosine:.9f}   {frame_floor:.9f}"
        )

    print("Euclidean dwell (hbar*c = 1): gap is reciprocal persistence ceiling")
    print(
        "spectrum(D_E) = "
        f"[{dwell_spectrum[0]:.9f}, {dwell_spectrum[1]:.9f}, "
        f"{dwell_spectrum[2]:.9f}]"
    )
    print(f"1/(2 ||D_E||) = {recovered_gap_from_dwell:.9f}")

    print("scope: finite Markov identities only; no continuum or Yang--Mills claim")


if __name__ == "__main__":
    main()
