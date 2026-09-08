"""Finite checks for oriented projection cycles; no field-theory gap is computed.

Requires NumPy. The note owns the finite-dimensional proofs and limiting claims.
This receipt compares ambient projection products with independent formulas,
checks sharp matrix inequalities, and distinguishes raw from polar composition.
"""

from math import ceil, cos, log2, pi, sin, sqrt, tan

import numpy as np


def adj(a):
    return a.conj().T


def norm(a):
    return float(np.linalg.norm(a, 2))


def check_close(a, b, tol=2e-11):
    error = norm(np.asarray(a) - np.asarray(b))
    assert error <= tol, (error, tol)
    return error


def expm(a):
    """Scaling/squaring Taylor evaluation, independent of eigenvector inversion."""
    scale = max(0, ceil(log2(max(1.0, 2 * norm(a)))))
    z = a / (2**scale)
    value = np.eye(a.shape[0], dtype=complex)
    term = value.copy()
    for k in range(1, 41):
        term = term @ z / k
        value = value + term
    for _ in range(scale):
        value = value @ value
    return value


def polar(a):
    u, singular, vh = np.linalg.svd(a)
    assert singular.min() > 1e-12
    return u @ vh


def graph_projection(a, epsilon):
    rank = a.shape[1]
    graph = np.vstack((np.eye(rank), epsilon * a))
    return graph @ np.linalg.solve(adj(graph) @ graph, adj(graph))


def compressed_cycle(vertices, epsilon):
    rank = vertices[0].shape[1]
    ambient = rank + vertices[0].shape[0]
    p0 = np.zeros((ambient, ambient), dtype=complex)
    p0[:rank, :rank] = np.eye(rank)
    product = p0.copy()
    for vertex in vertices[1:-1]:
        p = graph_projection(vertex, epsilon)
        check_close(p, adj(p))
        check_close(p @ p, p)
        product = p @ product
    product = p0 @ product
    return product[:rank, :rank]


def residue_row(vertices, epsilon):
    """Keep every discarded ambient component, without using the defect formula."""
    rank = vertices[0].shape[1]
    ambient = rank + vertices[0].shape[0]
    current = np.vstack((np.eye(rank), np.zeros((ambient - rank, rank))))
    rows = []
    for vertex in vertices[1:]:
        projection = graph_projection(vertex, epsilon)
        rows.append((np.eye(ambient) - projection) @ current)
        current = projection @ current
    return np.vstack(rows)


def positive_sqrt(a):
    values, vectors = np.linalg.eigh(a)
    assert values.min() >= -1e-12
    return (vectors * np.sqrt(np.maximum(values, 0))) @ adj(vectors)


def coefficients(vertices):
    rank = vertices[0].shape[1]
    k = np.zeros((rank, rank), dtype=complex)
    for j in range(1, len(vertices) - 1):
        k += adj(vertices[j]) @ (vertices[j] - vertices[j - 1])
    s = (k + adj(k)) / 2
    h = (k - adj(k)) / (2j)
    edge = sum(
        adj(right - left) @ (right - left) / 2
        for left, right in zip(vertices[:-1], vertices[1:])
    )
    check_close(s, edge)
    return s, h, k


def semigroup_checks(vertices, label):
    s, h, k = coefficients(vertices)
    t = 0.5
    target = expm(-t * k)
    unitary_target = expm(-1j * t * h)
    old_raw = old_polar = float("inf")
    print(f"\n{label}: repeated shrinking cycles, t={t}")
    for epsilon in (1 / 8, 1 / 16, 1 / 32, 1 / 64):
        steps = round(t / epsilon**2)
        cycle = compressed_cycle(vertices, epsilon)
        assert norm(cycle) <= 1 + 2e-12
        raw_error = norm(np.linalg.matrix_power(cycle, steps) - target)
        polar_error = norm(np.linalg.matrix_power(polar(cycle), steps) - unitary_target)
        assert raw_error < old_raw and polar_error < old_polar
        old_raw, old_polar = raw_error, polar_error
        print(f"  eps={epsilon:.7f} steps={steps:5d} raw={raw_error:.9g} polar={polar_error:.9g}")
    return s, h, k


def smooth_vertices(edges):
    b = np.array([[1, 0.5], [0, 0]], dtype=complex)
    d = np.array([[0, 0], [1, 1]], dtype=complex)
    vertices = [
        (np.exp(2j * pi * j / edges) - 1) * b
        + (np.exp(4j * pi * j / edges) - 1) * d
        for j in range(edges)
    ]
    vertices.append(np.zeros_like(b))
    # Fourier orthogonality supplies a target independent of the projection product.
    exact_k = edges * (
        (1 - np.exp(-2j * pi / edges)) * adj(b) @ b
        + (1 - np.exp(-4j * pi / edges)) * adj(d) @ d
    )
    h_infinity = 2 * pi * (adj(b) @ b + 2 * adj(d) @ d)
    assert norm((adj(b) @ b) @ (adj(d) @ d) - (adj(d) @ d) @ (adj(b) @ b)) > 0.1
    return vertices, exact_k, h_infinity


def uniform_remainder_checks():
    worst_ratio = 0.0
    for edges in (8, 32, 128):
        vertices, exact_k, _ = smooth_vertices(edges)
        _, _, k = coefficients(vertices)
        check_close(k, exact_k)
        maximum = max(norm(vertex) for vertex in vertices)
        variation = sum(norm(right - left) for left, right in zip(vertices[:-1], vertices[1:]))
        for epsilon in (0.1, 0.05, 0.025):
            cycle = compressed_cycle(vertices, epsilon)
            residual = norm(cycle - np.eye(2) + epsilon**2 * k)
            bound = epsilon**4 * (
                maximum**3 * variation
                + maximum**2 * variation**2 * np.exp(epsilon**2 * maximum * variation) / 2
            )
            assert residual <= bound + 2e-12
            worst_ratio = max(worst_ratio, residual / bound)
    print(f"Uniform PC8 remainder controls: largest actual/bound ratio={worst_ratio:.9g}")


def simultaneous_refinement_checks():
    t = 0.37
    for label, schedule in (("sqrt(n)", lambda n: round(sqrt(n))), ("n/8", lambda n: n // 8)):
        print(f"\nNoncommuting simultaneous refinement, m={label}, t={t}:")
        previous = float("inf")
        for steps in (256, 1024, 4096, 16384):
            edges = schedule(steps)
            epsilon = sqrt(t / steps)
            vertices, _, h_infinity = smooth_vertices(edges)
            cycle = compressed_cycle(vertices, epsilon)
            evolved = np.linalg.matrix_power(cycle, steps)
            target = expm(-1j * t * h_infinity)
            error = norm(evolved - target)
            defect = norm(np.eye(2) - adj(evolved) @ evolved)
            assert error < previous
            previous = error
            print(f"  steps={steps:5d} edges={edges:4d} eps={epsilon:.7f} error={error:.9g} defect={defect:.9g}")


def unbounded_spectral_diagnostics():
    """Quadrature for one vector, never an operator-norm substitute."""
    spectral, weights = np.polynomial.laguerre.laggauss(64)
    assert abs(weights.sum() - 1) < 1e-12
    assert abs(weights @ spectral - 1) < 1e-12
    t = 0.5
    previous_raw = previous_polar = float("inf")
    previous_loss = 0.0
    print("\nUnbounded multiplication carrier: vector with spectral density exp(-lambda)")
    for delta in (1 / 8, 1 / 32, 1 / 128, 1 / 512):
        steps = round(t / delta)
        x = delta * spectral
        raw = np.exp(steps * (np.log1p(-1j * x) - 2 * np.log1p(x)))
        phase = np.exp(-1j * steps * np.arctan(x))
        raw_error = sqrt(float(weights @ np.abs(raw - np.exp(-(2 + 1j) * t * spectral)) ** 2))
        polar_error = sqrt(float(weights @ np.abs(phase - np.exp(-1j * t * spectral)) ** 2))
        g = (4 + 5 * x + 4 * x**2 + x**3) / (1 + x) ** 4
        loss = float(weights @ (spectral * g))
        assert raw_error < previous_raw and polar_error < previous_polar
        assert previous_loss < loss < 4
        previous_raw, previous_polar, previous_loss = raw_error, polar_error, loss
        # Independently locate a spectral neighborhood witnessing polar norm error 2.
        low, high = 0.0, (pi + steps * pi / 2) / t + 1
        for _ in range(80):
            middle = (low + high) / 2
            if t * middle - steps * np.arctan(delta * middle) < pi:
                low = middle
            else:
                high = middle
        witness = (low + high) / 2
        phase_difference = abs(
            np.exp(-1j * steps * np.arctan(delta * witness)) - np.exp(-1j * t * witness)
        )
        assert abs(phase_difference - 2) < 1e-12
        print(
            f"  delta={delta:.7f} vector_raw={raw_error:.9g} vector_polar={polar_error:.9g}"
            f" loss_form={loss:.9g} norm_witness_lambda={witness:.9g} witness_error={phase_difference:.9g}"
        )
    print("The spectral integral is a finite quadrature diagnostic; the note proves the strong limit and norm obstruction.")


def main():
    print("Oriented projection-cycle finite receipt")
    print("NumPy", np.__version__)
    zero = np.zeros((1, 1), dtype=complex)
    triangle = [zero, np.ones((1, 1)), 1j * np.ones((1, 1)), zero]
    s, h, k = coefficients(triangle)
    check_close(s, np.array([[2.0]]))
    check_close(h, np.array([[1.0]]))
    for epsilon in (0.5, 0.25, 0.125):
        exact = np.array([[(1 - 1j * epsilon**2) / (1 + epsilon**2) ** 2]])
        check_close(compressed_cycle(triangle, epsilon), exact)
    print("Scalar triangle: ambient product equals (1-i eps^2)/(1+eps^2)^2; S=2, H=1.")
    semigroup_checks(triangle, "Scalar triangle")

    zero2 = np.zeros((2, 2), dtype=complex)
    a = np.eye(2, dtype=complex)
    b = 1j * np.array([[1, 1], [0, 1]], dtype=complex)
    noncommuting = [zero2, a, b, zero2]
    s, h, k = semigroup_checks(noncommuting, "Noncommuting triangle")
    check_close(s, np.array([[2, 1 - 0.5j], [1 + 0.5j, 3]]))
    check_close(h, np.array([[1, 0.5], [0.5, 1]]))
    assert np.linalg.eigvalsh(h).min() > 0
    assert norm(s @ h - h @ s) > 0.1
    late_polar = polar(expm(-0.5 * k))
    whole_polar_error = norm(late_polar - expm(-0.5j * h))
    group_error = norm(polar(expm(-k)) - late_polar @ late_polar)
    assert whole_polar_error > 1e-4 and group_error > 1e-4
    print(f"Polar after whole evolution differs from microscopic polar limit: {whole_polar_error:.9g}")
    print(f"Polar after whole evolution fails group composition: {group_error:.9g}")

    rng = np.random.default_rng(20260908)
    worst_expansion = 0.0
    worst_residue = 0.0
    least_bound = float("inf")
    for edges in range(3, 10):
        vertices = [np.zeros((3, 2), dtype=complex)]
        for _ in range(edges - 1):
            vertices.append((rng.normal(size=(3, 2)) + 1j * rng.normal(size=(3, 2))) / 4)
        vertices.append(vertices[0])
        s, h, k = coefficients(vertices)
        coefficient = 1 / tan(pi / edges)
        for sign in (-1, 1):
            least_bound = min(least_bound, float(np.linalg.eigvalsh(coefficient * s + sign * h).min()))
        epsilon = 1e-3
        approximation = (np.eye(2) - compressed_cycle(vertices, epsilon)) / epsilon**2
        worst_expansion = max(worst_expansion, norm(approximation - k))
        reversed_cycle = compressed_cycle(list(reversed(vertices)), epsilon)
        check_close(reversed_cycle, adj(compressed_cycle(vertices, epsilon)))
        cycle = compressed_cycle(vertices, 0.2)
        residue = residue_row(vertices, 0.2)
        worst_residue = max(worst_residue, check_close(adj(residue) @ residue, np.eye(2) - adj(cycle) @ cycle))
    assert least_bound > -1e-10 and worst_expansion < 3e-5
    print(f"Random rectangular polygon controls: min bound eigenvalue={least_bound:.9g}")
    print(f"Worst finite-epsilon coefficient error={worst_expansion:.9g}")
    print(f"Exact residue-row identity: worst error={worst_residue:.9g}")

    worst_converse = 0.0
    for _ in range(10):
        factors = [rng.normal(size=(3, 2)) + 1j * rng.normal(size=(3, 2)) for _ in range(2)]
        plus, minus = [adj(factor) @ factor for factor in factors]
        prescribed_s = (plus + minus) / 2
        prescribed_h = (plus - minus) / (2 * sqrt(3))
        c_plus, c_minus = positive_sqrt(plus), positive_sqrt(minus)
        b = (c_minus - c_plus) / (1j * sqrt(3))
        a = c_plus + np.exp(1j * pi / 3) * b
        s, h, _ = coefficients([zero2, a, b, zero2])
        worst_converse = max(
            worst_converse, check_close(s, prescribed_s), check_close(h, prescribed_h)
        )
    print(f"Sectorial-cone converse: worst reconstruction error={worst_converse:.9g}")

    print("\nSharp regular polygons (fixed infinitesimal geometry scale):")
    for edges in (3, 4, 8, 32, 128):
        vertices = [np.array([[np.exp(2j * pi * j / edges) - 1]]) for j in range(edges)]
        vertices.append(zero)
        s, h, k = coefficients(vertices)
        expected_s = edges * (1 - cos(2 * pi / edges))
        expected_h = edges * sin(2 * pi / edges)
        check_close(s, np.array([[expected_s]]))
        check_close(h, np.array([[expected_h]]))
        check_close(h, s / tan(pi / edges), tol=8e-11)
        print(f"  edges={edges:3d} S={s[0,0].real:.9f} H={h[0,0].real:.9f} H/S={(h[0,0]/s[0,0]).real:.9f}")

    uniform_remainder_checks()
    simultaneous_refinement_checks()
    unbounded_spectral_diagnostics()
    print("\nPASS: selected finite identities, inequalities and convergence diagnostics.")
    print("Finite diagnostics do not replace the analytic uniform-limit proof or establish novelty or a Yang-Mills mass gap.")


if __name__ == "__main__":
    main()
