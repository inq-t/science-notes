"""Finite matrix flat-partner and unpointed-channel checks.

A two-by-two Hermitian Riccati wall has a constant nonscalar partner and
noncommuting initial data. Broad Gaussian trial states give decreasing
energies in the free channel. These finite checks do not establish a
physical mass gap. No files are written.
"""

from __future__ import annotations

import numpy as np


def check_close(label, actual, expected, atol=2e-10):
    error = float(np.max(np.abs(np.asarray(actual) - np.asarray(expected))))
    if error > atol:
        raise AssertionError(f"{label}: error {error:.6g} exceeds {atol}")
    return error


def main():
    # A nonscalar constant partner admits noncommuting Hermitian W.
    d = np.diag([1.0, 2.0])
    w0 = 0.4 * np.array([[0.0, 1.0], [1.0, 0.0]])

    def matrix_wall(n):
        cosh = np.diag(np.cosh(np.array([1.0, 2.0]) * n))
        sinh = np.diag(np.sinh(np.array([1.0, 2.0]) * n))
        f = cosh + np.linalg.solve(d, sinh) @ w0
        fp = d @ sinh + cosh @ w0
        return np.linalg.solve(f.T, fp.T).T

    max_riccati = 0.0
    step = 1e-5
    for n in np.linspace(-4, 4, 25):
        wn = matrix_wall(n)
        check_close("Hermitian matrix wall", wn, wn.T, 1e-9)
        derivative = (matrix_wall(n + step) - matrix_wall(n - step)) / (2 * step)
        max_riccati = max(max_riccati, check_close(
            "matrix Riccati", derivative, d @ d - wn @ wn, 3e-8))
    commutator = w0 @ (d @ d) - (d @ d) @ w0
    if np.linalg.norm(commutator) < 1:
        raise AssertionError("noncommutation witness missing")
    check_close("positive asymptotic", matrix_wall(10), d, 2e-8)
    check_close("negative asymptotic", matrix_wall(-10), -d, 2e-8)
    print(f"PASS noncommuting flat partner; max Riccati error {max_riccati:.3g}")

    # Normalized broad Gaussians in the unpointed channel have vanishing form.
    widths = np.array([1.0, 2.0, 4.0, 8.0, 16.0])
    free_energies = 1 / (2 * widths**2)
    if not np.all(np.diff(free_energies) < 0) or free_energies[-1] >= 0.002:
        raise AssertionError("free-channel closing sequence failed")
    print("PASS free-channel trial energies:", free_energies.tolist())


if __name__ == "__main__":
    main()
