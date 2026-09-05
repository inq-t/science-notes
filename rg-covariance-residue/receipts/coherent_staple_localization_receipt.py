"""Finite checks of exact source support and a genuine small Wilson block."""

from itertools import product

import numpy as np

from joint_context_escape_receipt import exp_anti, haar_su3, phi, su3_basis


def close(actual, expected, tolerance=1e-9):
    assert np.max(np.abs(np.asarray(actual) - expected)) < tolerance


def source_bracket(matrix, count=8192):
    """Analytic grid-error bounds, evaluated in ordinary floating point."""
    left, sigma, right_star = np.linalg.svd(matrix)
    # The SVD extension also assigns a harmless phase for singular inputs.
    delta = np.angle(np.linalg.det(left @ right_star))
    grid = 2 * np.pi * np.arange(count) / count
    remaining = delta - grid
    radicand = (
        sigma[1] ** 2 + sigma[2] ** 2
        + 2 * sigma[1] * sigma[2] * np.cos(remaining)
    )
    objective = sigma[0] * np.cos(grid) + np.sqrt(np.maximum(radicand, 0))
    index = int(np.argmax(objective))
    first = grid[index]
    other_sum = delta - first
    second = np.angle(sigma[1] + sigma[2] * np.exp(1j * other_sum))
    phases = np.array((first, second, other_sum - second))
    optimizer = left @ np.diag(np.exp(-1j * phases)) @ right_star
    lower = objective[index] / 3
    upper = lower + (sigma[0] + min(sigma[1], sigma[2])) * np.pi / (3 * count)
    return lower, upper, optimizer


def source_checks():
    rng = np.random.default_rng(128)
    identity = np.eye(3)
    center = np.exp(2j * np.pi * np.arange(3) / 3)
    for scalar in (0, 1, -1, -2, -3, 3, 1 + 2j, -2 + 0.4j):
        lower, upper, optimizer = source_bracket(scalar * identity)
        exact = max(np.real(scalar * center.conj()))
        assert lower - 1e-10 <= exact <= upper + 1e-10
        close(np.linalg.det(optimizer), 1)
    for _ in range(18):
        matrix = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
        lower, upper, optimizer = source_bracket(matrix)
        close(optimizer.conj().T @ optimizer, identity)
        close(np.linalg.det(optimizer), 1)
        close(np.trace(optimizer.conj().T @ matrix).real / 3, lower, 1e-8)
        for _ in range(20):
            candidate = haar_su3(rng)
            assert np.trace(candidate.conj().T @ matrix).real / 3 <= upper + 1e-10
        g, h = haar_su3(rng), haar_su3(rng)
        transformed = source_bracket(g @ matrix @ h.conj().T)
        close(transformed[0], lower, 1e-8)
        close(transformed[1], upper, 1e-8)
    singular = np.diag((4.0, 2.0, 0.0))
    lower, upper, _ = source_bracket(singular)
    assert lower - 1e-10 <= 2 <= upper + 1e-10
    delta = 1.7
    matrix = np.diag((4 * np.exp(1j * delta), 2, 1))
    lower, _, _ = source_bracket(matrix)
    scalar_polar_correction = 7 * np.cos(delta / 3) / 3
    assert lower > scalar_polar_correction + 0.01
    print("PASS source support: scalar phases, 18 general sources, gauge tests, polar shortcut")


def patch():
    size = 7
    origin = (3, 3, 3, 3)

    def shift(point, direction, step=1):
        value = list(point)
        value[direction] = (value[direction] + step) % size
        return tuple(value)

    active = origin + (0,)
    outer = tuple(
        shift(origin, direction, step) + (0,)
        for direction in (1, 2, 3) for step in (1, -1)
    )
    powers = {active: 1}
    for direction in (1, 2, 3):
        for step, power in ((1, 1), (-1, 2)):
            powers[shift(origin, direction, step) + (0,)] = power
            powers[shift(origin, direction, 2 * step) + (0,)] = power
    diagonal = shift(shift(origin, 1), 2) + (0,)
    powers[diagonal] = 1
    plaquettes = []
    for point in product(range(size), repeat=4):
        for i in range(4):
            for j in range(i + 1, 4):
                plaquettes.append((
                    (point + (i,), 1),
                    (shift(point, i) + (j,), 1),
                    (shift(point, j) + (i,), -1),
                    (point + (j,), -1),
                ))
    touching = tuple(p for p in plaquettes if any(e in outer for e, _ in p))
    external = tuple(p for p in touching if all(e != active for e, _ in p))
    selected = outer[-2:]
    pair_touching = tuple(p for p in touching if any(e in selected for e, _ in p))
    pair_external = tuple(p for p in pair_touching if all(e != active for e, _ in p))
    local_edges = {e for p in touching for e, _ in p}
    z = np.exp(2j * np.pi / 3)
    field = {e: z ** powers.get(e, 0) * np.eye(3) for e in local_edges}
    assert len(touching) == 36 and len(external) == 30
    assert len(pair_touching) == 12 and len(pair_external) == 10
    assert all(sum(e in selected for e, _ in p) == 1 for p in pair_touching)
    overlap = {}
    for point in product(range(size), repeat=4):
        for direction in range(4):
            transverse = (direction + 3) % 4
            for step in (1, -1):
                edge = shift(point, transverse, step) + (direction,)
                overlap[edge] = overlap.get(edge, 0) + 1
    assert len(overlap) == 4 * size**4 and set(overlap.values()) == {2}
    return active, outer, selected, touching, external, pair_touching, pair_external, field


def staple_source(plaquettes, field, active):
    source = np.zeros((3, 3), dtype=complex)
    for plaquette in plaquettes:
        positions = tuple(i for i, (edge, _) in enumerate(plaquette) if edge == active)
        if not positions:
            continue
        index = positions[0]
        orientation = plaquette[index][1]
        complement = np.eye(3, dtype=complex)
        for offset in range(1, 4):
            edge, sign = plaquette[(index + offset) % 4]
            matrix = field[edge]
            complement = complement @ (matrix if sign == 1 else matrix.conj().T)
        source += complement.conj().T if orientation == 1 else complement
    return source


def lattice_checks():
    active, outer, selected, touching, external, pair_touching, pair_external, base = patch()
    values = np.array(tuple(phi(p, base) for p in external))
    close(np.sort(values), np.array((-0.5,) * 22 + (1.0,) * 8))
    close(values.sum(), -3)
    close(sum(phi(p, base) for p in pair_external), -2)
    close(sum(base[e] for e in outer), -3 * np.eye(3))
    close(sum(base[e] for e in selected), -np.eye(3))
    close(staple_source(pair_touching, base, active), -np.eye(3))
    old_chi_per_beta = -4 * (6 + values.sum())
    close(old_chi_per_beta, -12)
    support_cut = 0.5 + sum(phi(p, base) for p in pair_external)
    close(support_cut, -1.5)
    basis = su3_basis()
    epsilon = 2e-4
    rng = np.random.default_rng(128)
    gauges = {}
    transformed = {}
    for edge, matrix in base.items():
        start, direction = edge[:4], edge[4]
        endpoint = list(start)
        endpoint[direction] = (endpoint[direction] + 1) % 7
        end = tuple(endpoint)
        for site in (start, end):
            if site not in gauges:
                gauges[site] = haar_su3(rng)
        transformed[edge] = gauges[start] @ matrix @ gauges[end].conj().T
    close(
        np.array(tuple(phi(p, transformed) for p in touching)),
        np.array(tuple(phi(p, base) for p in touching)),
    )
    endpoint = list(active[:4])
    endpoint[active[4]] = (endpoint[active[4]] + 1) % 7
    source_in_new_frame = gauges[active[:4]] @ (-np.eye(3)) @ gauges[tuple(endpoint)].conj().T
    close(staple_source(pair_touching, transformed, active), source_in_new_frame)
    worst_laplacian_error = 0
    for _ in range(5):
        field = dict(base)
        field[active] = haar_su3(rng)
        baseline = sum(1 - phi(p, field) for p in pair_touching)
        laplacian = 0
        for edge in selected:
            for tangent in basis:
                positive, negative = dict(field), dict(field)
                positive[edge] = field[edge] @ exp_anti(epsilon * tangent)
                negative[edge] = field[edge] @ exp_anti(-epsilon * tangent)
                plus = sum(1 - phi(p, positive) for p in pair_touching)
                minus = sum(1 - phi(p, negative) for p in pair_touching)
                laplacian += (plus + minus - 2 * baseline) / epsilon**2
        exact = 8 * sum(phi(p, field) for p in pair_touching)
        worst_laplacian_error = max(worst_laplacian_error, abs(laplacian - exact))
        close(laplacian, exact, 5e-5)
        assert exact <= -12 + 1e-9
    for beta in (0.1, 1.0, 28.0, 100.0):
        delta, outside = 8 * beta, 96 * beta
        close(1 / (delta + outside), 1 / (104 * beta))
        close(outside / (delta + outside), 12 / 13)
    print(
        "PASS full Wilson patch: 8/22 exterior split, missed old cut, "
        "three-link remainder, twofold overlap"
    )
    print(f"PASS five nonlinear Casimir checks; max discrepancy {worst_laplacian_error:.3g}")


if __name__ == "__main__":
    source_checks()
    lattice_checks()
    print("Scope: finite diagnostics; no interval-arithmetic or continuum-gap certificate")
