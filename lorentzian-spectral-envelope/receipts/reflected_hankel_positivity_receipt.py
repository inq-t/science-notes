"""Finite reflected-Hankel positivity checks for two covariance kernels.

Nine two-time minors of sech-squared are negative, while positive
Laplace-mixture controls are positive. These finite witnesses distinguish
Fourier covariance positivity from reflection positivity; they do not
establish a reconstruction or a physical mass gap. No files are written.
"""

from __future__ import annotations

import math

import numpy as np


def main():
    # Positive Fourier covariance does not imply reflected Hankel positivity.
    for nu in (0.3, 1.0, 2.0):
        for s, t in ((0.1, 0.4), (0.2, 0.8), (1.0, 1.3)):
            def kernel(z):
                return 1 / math.cosh(nu * z) ** 2
            hankel = np.array([[kernel(2*s), kernel(s+t)],
                               [kernel(s+t), kernel(2*t)]])
            if not np.linalg.det(hankel) < 0:
                raise AssertionError("sech reflected determinant not negative")
            times = np.array([s, t])
            laplace = sum(weight * np.exp(-energy * (times[:, None] + times[None, :]))
                          for weight, energy in ((0.4, 1.0), (0.6, 3.0)))
            if np.linalg.eigvalsh(laplace).min() < -1e-13:
                raise AssertionError("positive Laplace mixture failed")
    print("PASS nine negative sech reflected minors and positive Laplace controls")


if __name__ == "__main__":
    main()
