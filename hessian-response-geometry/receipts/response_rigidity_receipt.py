"""Stdout-only checks for response rigidity, fixed profiles and soft modes."""

import itertools
import numpy as np


def binary_channel(epsilon):
    points = np.array(tuple(itertools.product((-1.0, 1.0), repeat=3)))
    squares = np.array((0.5, 1.0 - epsilon, epsilon / (2.0 - epsilon)))
    k = np.sqrt(squares)
    kernel = np.prod(
        (1.0 + points[:, None, :] * points[None, :, :] * k) / 2.0, axis=2
    )
    return points, k, kernel


def entropy(law):
    return np.sum(law * np.log(8.0 * law))


def binary_entropy_response(mean):
    return 0.5 * (
        (1.0 + mean) * np.log1p(mean)
        + (1.0 - mean) * np.log1p(-mean)
    )


def channel_checks():
    count = 0
    profile_error = 0.0
    for epsilon in (0.5, 0.2, 0.03, 1.0e-4, 1.0e-7):
        points, k, kernel = binary_channel(epsilon)
        response = np.eye(8) - kernel.T @ kernel
        assert np.min(kernel) > 0.0
        np.testing.assert_allclose(kernel.sum(axis=1), 1.0, atol=1e-14)
        np.testing.assert_allclose(kernel, kernel.T, atol=1e-14)
        assert np.linalg.eigvalsh(kernel).min() > 0.0
        eigenvalues = np.linalg.eigvalsh(response)
        np.testing.assert_allclose(eigenvalues[0], 0.0, atol=2e-14)
        np.testing.assert_allclose(eigenvalues[1], epsilon, atol=2e-14)
        np.testing.assert_allclose(np.trace(response), 5.0, atol=2e-14)
        tangent = points[:, 0]
        np.testing.assert_allclose(tangent @ response @ tangent / 8, 0.5)
        np.testing.assert_allclose(np.linalg.norm(kernel @ tangent) ** 2 / 8, 0.5)
        for flags in itertools.product((False, True), repeat=3):
            subset = np.flatnonzero(flags)
            character = np.prod(points[:, subset], axis=1)
            multiplier = np.prod(k[subset])
            np.testing.assert_allclose(
                kernel @ character, multiplier * character, atol=2e-14
            )
        for theta in (-3.0, -1.0, -0.1, 0.0, 0.4, 2.5):
            mean = np.tanh(theta)
            law = np.exp(theta * points[:, 0]) / (8.0 * np.cosh(theta))
            output = kernel.T @ law
            expected = (1.0 + k[0] * mean * points[:, 0]) / 8.0
            np.testing.assert_allclose(output, expected, atol=2e-14)
            profile_error = max(profile_error, np.max(np.abs(output - expected)))
            np.testing.assert_allclose(
                entropy(law), binary_entropy_response(mean), atol=2e-14
            )
            np.testing.assert_allclose(
                entropy(output), binary_entropy_response(k[0] * mean), atol=2e-14
            )
            derivative = law * (points[:, 0] - mean)
            output_derivative = kernel.T @ derivative
            np.testing.assert_allclose(
                np.sum(derivative**2 / law), 1.0 - mean**2, atol=2e-14
            )
            np.testing.assert_allclose(
                np.sum(output_derivative**2 / output),
                k[0] ** 2 * (1.0 - mean**2) ** 2 / (1.0 - k[0] ** 2 * mean**2),
                atol=2e-14,
            )
            count += 1
        # Exact average over all permutations of the full eight-point carrier.
        averaged = np.zeros_like(response)
        for permutation in itertools.permutations(range(8)):
            order = np.array(permutation)
            averaged += response[np.ix_(order, order)]
        averaged /= 40320
        q = np.eye(8) - np.ones((8, 8)) / 8
        np.testing.assert_allclose(averaged, (5.0 / 7) * q, atol=2e-12)
        assert np.linalg.norm(response - averaged, 2) >= 5.0 / 7 - epsilon - 2e-12
    return count, profile_error


def rigidity_checks():
    rng = np.random.default_rng(121)
    for dimension in (3, 5, 8):
        unitary, _ = np.linalg.qr(rng.normal(size=(dimension, dimension)))
        eigenvalues = rng.uniform(0.15, 0.85, dimension)
        response = (unitary * eigenvalues) @ unitary.T
        # Sign conjugations erase off-diagonals; permutations equate diagonals.
        twirl = np.zeros_like(response)
        for signs in itertools.product((-1.0, 1.0), repeat=dimension):
            signs = np.array(signs)
            twirl += signs[:, None] * response * signs[None, :]
        twirl /= 2**dimension
        averaged = sum(
            np.roll(np.roll(twirl, shift, axis=0), shift, axis=1)
            for shift in range(dimension)
        ) / dimension
        scalar = np.trace(response) / dimension
        np.testing.assert_allclose(averaged, scalar * np.eye(dimension), atol=2e-14)
        eta = np.linalg.norm(response - averaged, 2)
        assert np.min(eigenvalues) >= scalar - eta - 2e-14
        assert np.min(eigenvalues) >= response[0, 0] - 2 * eta - 2e-14
        weights = rng.uniform(0.1, 1.0, dimension)
        weights /= weights.sum()
        delta = 1.0 - np.trace(np.diag(weights) @ response)
        assert np.min(eigenvalues) >= 1.0 - delta / weights.min() - 2e-14
    response = np.diag((0.99, 0.98, 0.97))
    weights = np.array((0.2, 0.3, 0.5))
    delta = 1.0 - weights @ np.diag(response)
    assert 0.0 < 1.0 - delta / weights.min() <= np.min(np.diag(response))
    internal = np.array((0.0, -1.0, 1.0, 0.0)).reshape(2, 2)
    multiplicity = np.diag(1.0 / np.arange(1, 13))
    response = np.kron(np.eye(2), multiplicity)
    action = np.kron(internal, np.eye(12))
    np.testing.assert_allclose(action @ response, response @ action)
    np.testing.assert_allclose(np.linalg.eigvalsh(response)[0], 1.0 / 12.0)


if __name__ == "__main__":
    count, error = channel_checks()
    rigidity_checks()
    print(f"PASS: 5 complete eight-state channels; {count} entropy/Fisher profiles")
    print("PASS: fixed trace 5, balanced tangent 1/2, full nonconstant edge epsilon")
    print(f"Maximum output-profile discrepancy: {error:.3g}")
    print("PASS: full-carrier twirl, scalar calibration, saturation and multiplicity")
