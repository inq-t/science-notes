"""Finite diagnostics for singular source fibers and a commuting Wilson escape.

The proofs are in the neighboring Markdown owners. No physical gap or
interval-arithmetic certificate is computed.
"""

from itertools import combinations, product

import numpy as np

from coherent_staple_localization_receipt import close, patch, staple_source
from joint_context_escape_receipt import exp_anti, haar_su3, phi, su3_basis


def shifted(point, direction, step=1, side=7):
    result = list(point)
    result[direction] = (result[direction] + step) % side
    return tuple(result)


def source_fiber_checks():
    basis = su3_basis()
    z = np.exp(2j * np.pi / 3)
    identity = np.eye(3)
    assignments = tuple(
        powers for powers in product((1, 2), repeat=6)
        if abs(sum(z ** power for power in powers) + 3) < 1e-10
    )
    assert len(assignments) == 20
    assert all(powers.count(1) == powers.count(2) == 3 for powers in assignments)
    columns = []
    for power in (1, 1, 1, 2, 2, 2):
        for tangent in basis:
            derivative = z ** power * tangent
            columns.append(np.concatenate((derivative.real.ravel(), derivative.imag.ravel())))
    jacobian = np.array(columns).T
    assert jacobian.shape == (18, 48)
    assert np.linalg.matrix_rank(jacobian, tol=1e-10) == 16
    rng = np.random.default_rng(129)
    epsilon = 2e-4
    worst = 0.0
    for _ in range(12):
        tangents = []
        for _ in range(2):
            a = np.einsum("a,aij->ij", rng.normal(size=8), basis)
            b = np.einsum("a,aij->ij", rng.normal(size=8), basis)
            tangents.extend((a, b, -a - b))
        squared_norm = sum(-np.trace(t @ t).real / 3 for t in tangents)
        tangents = tuple(t / np.sqrt(squared_norm) for t in tangents)
        powers = (1, 1, 1, 2, 2, 2)
        close(sum(z ** p * t for p, t in zip(powers, tangents)), np.zeros((3, 3)))
        plus = sum(z ** p * exp_anti(epsilon * t) for p, t in zip(powers, tangents))
        minus = sum(z ** p * exp_anti(-epsilon * t) for p, t in zip(powers, tangents))
        curvature = (np.trace(plus + minus).real + 18) / epsilon**2
        close(curvature, 1.5, 2e-5)
        worst = max(worst, abs(curvature - 1.5))
        assert np.trace(plus).real + 9 > 0
    span = []
    for _ in range(36):
        unitary = haar_su3(rng)
        span.append(np.concatenate((unitary.real.ravel(), unitary.imag.ravel())))
    assert np.linalg.matrix_rank(np.array(span), tol=1e-9) == 18
    print(f"PASS source fiber: 20 assignments, rank16/kernel32, 12 quadratic tests ({worst:.3g})")


def second_ring_checks():
    active, _, _, _, _, _, _, base = patch()
    points = tuple(product(range(7), repeat=4))
    field = {point + (axis,): np.eye(3, dtype=complex) for point in points for axis in range(4)}
    field.update(base)
    plaquettes = tuple(
        (
            (point + (i,), 1),
            (shifted(point, i) + (j,), 1),
            (shifted(point, j) + (i,), -1),
            (point + (j,), -1),
        )
        for point in points for i in range(4) for j in range(i + 1, 4)
    )
    selected = shifted(active[:4], 3, 2) + (0,)
    touching = tuple(p for p in plaquettes if any(edge == selected for edge, _ in p))
    active_terms = tuple(p for p in plaquettes if any(edge == active for edge, _ in p))
    assert len(touching) == len(active_terms) == 6
    assert len({edge for p in active_terms for edge, _ in p}) == 19
    assert all(all(edge != active for edge, _ in p) for p in touching)
    assert all(all(edge != selected for edge, _ in p) for p in active_terms)
    close(sorted(phi(p, field) for p in touching), np.array((-0.5,) * 5 + (1.0,)))
    source = staple_source(active_terms, field, active)
    close(source, -3 * np.eye(3))
    rng = np.random.default_rng(129)
    for _ in range(8):
        changed = dict(field)
        changed[selected] = haar_su3(rng)
        close(staple_source(active_terms, changed, active), source)
    basis = su3_basis()
    epsilon = 2e-4
    baseline = sum(1 - phi(p, field) for p in touching)
    second = []
    for tangent in basis:
        plus, minus = dict(field), dict(field)
        plus[selected] = exp_anti(epsilon * tangent) @ field[selected]
        minus[selected] = exp_anti(-epsilon * tangent) @ field[selected]
        second.append((sum(1 - phi(p, plus) for p in touching)
                       + sum(1 - phi(p, minus) for p in touching)
                       - 2 * baseline) / epsilon**2)
    close(np.array(second), -1.5 * np.ones(8), 2e-5)
    close(sum(second), -12, 8e-5)
    local_edges = {edge for p in touching + active_terms for edge, _ in p}
    gauges = {}
    transformed = {}
    for edge in local_edges:
        start = edge[:4]
        end = shifted(start, edge[4])
        for site in (start, end):
            if site not in gauges:
                gauges[site] = haar_su3(rng)
        transformed[edge] = gauges[start] @ field[edge] @ gauges[end].conj().T
    close(
        np.array(tuple(phi(p, transformed) for p in touching)),
        np.array(tuple(phi(p, field) for p in touching)),
    )
    close(
        staple_source(active_terms, transformed, active),
        gauges[active[:4]] @ source @ gauges[shifted(active[:4], active[4])].conj().T,
    )
    translated = tuple(
        shifted(point, (axis + 3) % 4, 2) + (axis,)
        for point in points for axis in range(4)
    )
    assert len(set(translated)) == len(translated) == 4 * 7**4
    for beta in (0.1, 1, 28, 100):
        delta, outside = 8 * beta, 48 * beta
        close(1 / (delta + outside), 1 / (56 * beta))
        close(outside / (delta + outside), 6 / 7)
    print("PASS full Wilson second ring: six plaquettes, source independence, gauge tests, overlap1")
    print(f"PASS eight nonlinear Hessians and Laplacian: {sum(second):.9g}")


def pair_incidence_checks():
    origin = (3, 3, 3, 3)
    cases = 0
    for transverse in product(*(tuple(j for j in range(4) if j != i) for i in range(4))):
        missed = tuple((i, j) for i, j in combinations(range(4), 2)
                       if transverse[i] != j and transverse[j] != i)
        assert len(missed) >= 2
        i, j = missed[0]
        plaquette = {origin + (i,), shifted(origin, i) + (j,),
                     shifted(origin, j) + (i,), origin + (j,)}
        centers = set()
        for edge in plaquette:
            axis = edge[4]
            for step in (-1, 0, 1):
                centers.add(shifted(edge[:4], transverse[axis], step) + (axis,))
        assert len(centers) == 12
        for center in centers:
            axis = center[4]
            block = {shifted(center[:4], transverse[axis], step) + (axis,)
                     for step in (-1, 0, 1)}
            assert len(block.intersection(plaquette)) == 1
        cases += 1
    assert cases == 81
    close(12 / (12 + 4.5), 8 / 11)
    assert 3 * 8 / 11 > 1
    print("PASS all81 transverse choices: neutral plaquette ratio3 and bC>=24/11")


if __name__ == "__main__":
    source_fiber_checks()
    second_ring_checks()
    pair_incidence_checks()
    print("Scope: exact finite incidence plus floating diagnostics; no continuum-gap certificate")
