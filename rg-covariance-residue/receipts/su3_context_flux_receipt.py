"""Wilson source-path and finite Weyl checks for the cut-flux obstruction."""

import numpy as np


def close(actual, expected, tolerance=1e-9):
    assert np.max(np.abs(np.asarray(actual) - expected)) < tolerance


def staples(alpha):
    diagonal = np.exp(1j * alpha * np.array((1.0, 1.0, -2.0)))
    return tuple(np.diag(np.roll(diagonal, j)) for j in range(3) for _ in range(2))


def source_path_checks():
    identity = np.eye(3)
    for alpha in (0.4, 2 * np.pi / 3, np.pi, 4 * np.pi / 3):
        matrices = staples(alpha)
        for matrix in matrices:
            close(matrix.conj().T @ matrix, identity)
            close(np.linalg.det(matrix), 1)
        close(sum(matrices), 2 * (2 * np.exp(1j * alpha) + np.exp(-2j * alpha)) * identity)
    close(sum(staples(np.pi)), -2 * identity)
    epsilon = 1e-5
    derivative = (sum(staples(np.pi + epsilon)) - sum(staples(np.pi - epsilon))) / (
        2 * epsilon
    )
    close(derivative, -8j * identity, 2e-9)
    close(np.imag(np.trace(np.linalg.solve(-2 * identity, derivative))), 12, 3e-9)
    generator = 1j * np.diag((1.0, 1.0, -2.0))
    speed_squared = 6 * (-np.real(np.trace(generator @ generator)) / 3)
    close(speed_squared, 12)
    theta = np.linspace(2 * np.pi / 3, 4 * np.pi / 3, 1001)
    potential = 2 * np.cos(theta) + np.cos(2 * theta)
    close(np.max(potential), -1)
    close(potential[0], -1.5)
    close(potential[-1], -1.5)
    close(potential, 2 * (np.cos(theta) + 0.5) ** 2 - 1.5)
    print("SU(3) staple sum, tangent, speed, determinant phase and barrier passed")


def edge_key(start, end):
    start, end = tuple(start), tuple(end)
    difference = np.asarray(end) - np.asarray(start)
    assert np.count_nonzero(difference) == 1 and np.sum(np.abs(difference)) == 1
    return tuple(sorted((start, end)))


def reference_path_check():
    origin = np.zeros(4, dtype=int)
    mu, nu = np.eye(4, dtype=int)[:2]
    active = edge_key(origin, mu)
    outer = set()
    paths = []
    for direction in np.eye(4, dtype=int)[1:]:
        for sign in (-1, 1):
            offset = sign * direction
            outer.add(edge_key(offset, offset + mu))
            paths.append((origin, offset, offset + mu, mu))
    reference = (origin, nu, 2 * nu, 2 * nu + mu, nu + mu, mu)
    reference_edges = {
        edge_key(reference[j], reference[j + 1]) for j in range(len(reference) - 1)
    }
    assert len(outer) == 6
    assert active not in reference_edges and outer.isdisjoint(reference_edges)
    # Each staple path traverses its own outer parallel edge forward.
    for path in paths:
        assert edge_key(path[1], path[2]) in outer
    print("actual star and five-link reference incidences passed")


def smooth_plateau(values, width=0.30):
    # C2 compact-gradient cutoff. The theorem uses a C-infinity cutoff;
    # these finite integral checks require only this explicitly stated C2 one.
    x = values / width
    clipped = np.clip(x, -1, 1)
    value = (15 * clipped - 10 * clipped**3 + 3 * clipped**5) / 8
    derivative = np.where(np.abs(x) < 1, 15 * (1 - x**2) ** 2 / (8 * width), 0)
    return value, derivative


def weyl_checks(points=384):
    angles = 2 * np.pi * np.arange(points) / points
    t1, t2 = np.meshgrid(angles, angles, indexing="ij")
    theta = np.stack((t1, t2, -t1 - t2), axis=-1)
    eigenvalues = np.exp(1j * theta)
    vandermonde = np.ones(t1.shape)
    for i, j in ((0, 1), (0, 2), (1, 2)):
        vandermonde *= np.abs(eigenvalues[..., i] - eigenvalues[..., j]) ** 2
    trace = np.sum(eigenvalues, axis=-1)
    potential, w = trace.real, trace.imag
    test, derivative = smooth_plateau(w)
    cosine = np.cos(theta)
    gradient_w = np.sqrt(
        3 * np.sum((cosine - cosine.mean(axis=-1, keepdims=True)) ** 2, axis=-1)
    )
    gradient_test = np.abs(derivative) * gradient_w
    expected = 4 * np.sqrt(3)
    ratios = []
    demands = []
    for kappa in (1.0, 4.0, 8.0, 16.0, 32.0):
        beta = 1.5 * kappa
        weight = vandermonde * np.exp(-kappa * (potential + 1.5))
        probability = weight / weight.sum()
        score = -(8 * beta / 3) * w
        mean = lambda array: np.sum(probability * array)
        demand_per_beta = abs(mean(score * test)) / beta
        denominator = mean(gradient_test)
        ratio = abs(mean(score * test)) / denominator
        fisher_full = mean(score**2)
        # Symmetric continuous partition has probability one half;
        # use 1/2 on the zero set in the quadrature to preserve symmetry.
        label_plus = np.where(w > 1e-12, 1, np.where(w < -1e-12, 0, 0.5))
        probability_plus = mean(label_plus)
        pi_prime = mean(score * label_plus)
        fisher_label = pi_prime**2 / (probability_plus * (1 - probability_plus))
        close(mean(score), 0, 1e-10)
        close(probability_plus, 0.5, 1e-10)
        assert 0 <= fisher_label <= fisher_full + 1e-8
        ratios.append(ratio)
        demands.append(demand_per_beta)
        print(
            f"kappa={kappa:4.0f}: demand/beta={demand_per_beta:.8f}, "
            f"flux lower test={ratio:.6g}, "
            f"label/full Fisher={fisher_label / fisher_full:.8f}"
        )
    assert all(a < b for a, b in zip(ratios, ratios[1:]))
    assert abs(demands[-1] - expected) < abs(demands[0] - expected)
    print("Weyl samples show increasing obstruction and concentration toward wells")


if __name__ == "__main__":
    source_path_checks()
    reference_path_check()
    weyl_checks()
    print("PASS: finite diagnostics, not an asymptotic or physical-gap proof")
