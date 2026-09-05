"""Finite checks of compatible signed curvature and retained collective escape.

Stdout only. The full Wilson law is unchanged; no physical mass is computed.
"""

from itertools import product
import numpy as np
from joint_context_escape_receipt import exp_anti, haar_su3, phi, su3_basis


def build_patch(size=8):
    def shift(x, direction, step=1):
        y = list(x)
        y[direction] = (y[direction]+step) % size
        return tuple(y)

    plaquettes = []
    for x in product(range(size), repeat=4):
        for i in range(4):
            for j in range(i+1, 4):
                plaquettes.append(((x+(i,), 1), (shift(x, i)+(j,), 1),
                                   (shift(x, j)+(i,), -1), (x+(j,), -1)))
    active = (0, 0, 0, 0, 0)
    selected = tuple((1, a, b, c, 0) for a in (0, 1)
                     for b in range(6) for c in range(6))
    coefficients = {edge: np.sqrt(2)/7 * np.sin(np.pi*(edge[2]+1)/7)
                    * np.sin(np.pi*(edge[3]+1)/7) for edge in selected}
    assert np.isclose(sum(a*a for a in coefficients.values()), 1)
    selected_set = set(selected)
    touching = tuple(p for p in plaquettes
                     if any(e in selected_set for e, _ in p))
    active_plaquettes = tuple(p for p in plaquettes
                              if any(e == active for e, _ in p))
    assert len(touching) == 276 and len(selected) == 72
    assert all(not any(e == active for e, _ in p) for p in touching)
    assert all(sum(e in selected_set for e, _ in p) <= 2 for p in touching)
    root = (1, 0, 0, 0)
    paths = {}
    tree_edges = set()
    for edge in selected:
        x, path = edge[:4], []
        for direction in (3, 2, 1):
            while x[direction] > 0:
                parent = shift(x, direction, -1)
                tree_edge = parent+(direction,)
                path.append((tree_edge, -1))
                tree_edges.add(tree_edge)
                x = parent
        assert x == root
        paths[edge] = tuple(path)
    assert len(tree_edges) == 71 and not tree_edges.intersection(selected_set)
    assert active not in tree_edges
    assert all(not any(e in selected_set for e, _ in p) for p in active_plaquettes)

    def power(edge):
        return sum(int(edge[k] in (0, 1)) for k in (1, 2, 3)) if edge[4] == 0 else 0

    def plaquette_weight(p):
        exponent = sum(sign*power(edge) for edge, sign in p) % 3
        return 1 if exponent == 0 else -0.5

    diagonal = {}
    for p in plaquettes:
        for edge, _ in p:
            diagonal[edge] = diagonal.get(edge, 0) + plaquette_weight(p)
    assert min(v for e, v in diagonal.items() if e[4] == 0) == 1.5
    assert min(v for e, v in diagonal.items() if e[4] != 0) == 3
    q = sum(plaquette_weight(p)
            * sum(sign*coefficients.get(edge, 0) for edge, sign in p)**2
            for p in touching)
    margin = 0.5-8*np.sin(np.pi/14)**2
    assert margin > 0 and q <= -margin
    six_outer = tuple(shift(active[:4], direction, step)+(0,)
                      for direction in (1, 2, 3) for step in (1, -1))
    external = tuple(p for p in plaquettes if any(e in six_outer for e, _ in p)
                     and not any(e == active for e, _ in p))
    # At central links all first derivatives vanish. The previous adaptive
    # certificate has A=0 and is negative here.
    previous_certificate = -4*(6+sum(plaquette_weight(p) for p in external))
    assert previous_certificate < 0
    all_edges = {edge for p in touching+active_plaquettes for edge, _ in p}
    all_edges.update(tree_edges)
    z = np.exp(2j*np.pi/3)
    field = {edge: z**power(edge)*np.eye(3) for edge in all_edges}
    source = -3*z*np.eye(3)
    rng = np.random.default_rng(120)
    for _ in range(15):
        field[active] = haar_su3(rng)
        assert np.isclose(sum(phi(p, field) for p in active_plaquettes),
                          np.trace(field[active].conj().T @ source).real/3)
    field[active] = np.eye(3)
    return (size, active, selected, coefficients, touching, paths, field,
            q, margin, previous_certificate)


def transports(field, paths):
    result = {}
    for edge, path in paths.items():
        u = np.eye(3, dtype=complex)
        for tree_edge, sign in path:
            v = field[tree_edge]
            u = u @ (v if sign == 1 else v.conj().T)
        result[edge] = u
    return result


def collective_jets(field, touching, paths, coefficients, basis):
    """Exact first and second jets; the transport tree is frozen by this flow."""
    transport = transports(field, paths)
    first, second = np.zeros(8), np.zeros(8)
    for index, tangent in enumerate(basis):
        generators = {e: coefficients[e]*(p @ tangent @ p.conj().T)
                      for e, p in transport.items()}
        for plaquette in touching:
            value = np.eye(3, dtype=complex)
            derivative = np.zeros((3, 3), dtype=complex)
            acceleration = np.zeros((3, 3), dtype=complex)
            for edge, sign in plaquette:
                u = field[edge]
                generator = generators.get(edge, np.zeros((3, 3), dtype=complex))
                if sign == 1:
                    v, dv, ddv = u, generator @ u, generator @ generator @ u
                else:
                    v = u.conj().T
                    dv, ddv = -v @ generator, v @ generator @ generator
                acceleration = acceleration @ v + 2*derivative @ dv + value @ ddv
                derivative = derivative @ v + value @ dv
                value = value @ v
            first[index] -= np.trace(derivative).real/3
            second[index] -= np.trace(acceleration).real/3
    return first, second


def flow(field, paths, coefficients, tangent, time):
    result = dict(field)
    for edge, p in transports(field, paths).items():
        generator = coefficients[edge]*(p @ tangent @ p.conj().T)
        result[edge] = exp_anti(time*generator) @ field[edge]
    return result


def covariance_checks(patch):
    size, active, selected, weights, touching, paths, central, q, margin, _ = patch
    basis, rng = su3_basis(), np.random.default_rng(121)
    first, second = collective_jets(central, touching, paths, weights, basis)
    assert np.allclose(first, 0, atol=1e-12)
    assert np.allclose(second, q)
    assert -second.sum() >= 8*margin
    largest_error, cases = 0.0, 0
    for coupling in (0.25, 1, 4):
        field = {edge: u @ exp_anti(0.002*np.einsum(
            "a,aij->ij", rng.normal(size=8), basis)) for edge, u in central.items()}
        field[active] = haar_su3(rng)
        first, second = collective_jets(field, touching, paths, weights, basis)
        assert -second.sum() > 4*margin
        assert abs(second.sum()) <= 96
        step = 1e-3
        measured_potential = 0.0
        for k, tangent in enumerate(basis):
            plus = flow(field, paths, weights, tangent, step)
            minus = flow(field, paths, weights, tangent, -step)
            dp = coupling*sum(phi(p, field)-phi(p, plus) for p in touching)
            dm = coupling*sum(phi(p, field)-phi(p, minus) for p in touching)
            wp, wm = np.expm1(dp), np.expm1(dm)
            measured_potential -= ((wp+wm)/step**2
                                   - coupling*first[k]*(wp-wm)/(2*step))
        error = abs(measured_potential+coupling*second.sum())/(
            1+coupling*abs(second.sum()))
        largest_error = max(largest_error, error)
        assert error < 3e-5, (error, measured_potential, -second.sum())

        def endpoint(edge):
            target = list(edge[:4])
            target[edge[4]] = (target[edge[4]]+1) % size
            return tuple(target)

        vertices = {edge[:4] for edge in field} | {endpoint(edge) for edge in field}
        gauge = {vertex: haar_su3(rng) for vertex in vertices}
        gauged = {edge: gauge[edge[:4]] @ u @ gauge[endpoint(edge)].conj().T
                  for edge, u in field.items()}
        gauge_first, gauge_second = collective_jets(
            gauged, touching, paths, weights, basis)
        assert np.isclose(gauge_second.sum(), second.sum())
        assert np.isclose(gauge_first @ gauge_first, first @ first)
        # A scalar smooth probe with all selected-link derivatives represented.
        gradients = rng.normal(size=(len(selected), 8))
        collective = sum(weights[e]*gradients[k] for k, e in enumerate(selected))
        assert collective @ collective <= np.sum(gradients**2) + 1e-12
        cases += 1
    for _ in range(3):
        generic = {edge: haar_su3(rng) for edge in central}
        _, second = collective_jets(generic, touching, paths, weights, basis)
        assert abs(second.sum()) <= 96
    return cases, largest_error


def commuting_conditioning_checks(patch):
    """Check the exact incidence and a finite Haar-sample quadrature.

    The quadrature tests the derivative identity algebraically; it does not
    certify approximation error for the continuum conditional integral.
    """
    size, active, selected, weights, touching, paths, central, _, _, _ = patch
    origin = active[:4]

    def shift(vertex, axis, amount=1):
        result = list(vertex)
        result[axis] = (result[axis] + amount) % size
        return tuple(result)

    active_plaquettes = []
    for axis in (1, 2, 3):
        for base in (origin, shift(origin, axis, -1)):
            active_plaquettes.append(((base+(0,), 1), (shift(base, 0)+(axis,), 1),
                                      (shift(base, axis)+(0,), -1), (base+(axis,), -1)))
    assert len(active_plaquettes) == 6
    assert all(not any(edge in weights for edge, _ in p) for p in active_plaquettes)
    assert all(edge != active for path in paths.values() for edge, _ in path)
    rng, basis = np.random.default_rng(123), su3_basis()
    field = {edge: haar_su3(rng) for edge in central}
    samples = tuple(haar_su3(rng) for _ in range(48))
    probe_edge, probe_matrix = selected[15], haar_su3(rng)
    largest_error, cases = 0.0, 0

    def conditional_data(context, coupling):
        scores, probes = [], []
        for sample in samples:
            changed = dict(context)
            changed[active] = sample
            scores.append(coupling * sum(phi(p, changed) for p in active_plaquettes))
            probes.append(np.trace(sample @ changed[probe_edge] @ probe_matrix).real / 3)
        scores = np.array(scores)
        probabilities = np.exp(scores - scores.max())
        probabilities /= probabilities.sum()
        return probabilities, np.array(probes)

    for coupling in (0.25, 1.0, 4.0):
        probabilities, _ = conditional_data(field, coupling)
        for tangent in basis:
            step = 1e-4
            plus = flow(field, paths, weights, tangent, step)
            minus = flow(field, paths, weights, tangent, -step)
            pp, fp = conditional_data(plus, coupling)
            pm, fm = conditional_data(minus, coupling)
            assert np.array_equal(pp, probabilities)
            assert np.array_equal(pm, probabilities)
            derivative = (fp - fm) / (2 * step)
            lhs = (pp @ fp - pm @ fm) / (2 * step)
            rhs = probabilities @ derivative
            largest_error = max(largest_error, abs(lhs - rhs))
            assert abs(lhs - rhs) < 2e-11
            centered = derivative - rhs
            assert probabilities @ centered**2 <= probabilities @ derivative**2 + 1e-13
            cases += 1
    return cases, largest_error


def compatible_image_checks():
    rng = np.random.default_rng(122)
    cases = 0
    for rows, columns, rank in ((8, 6, 5), (12, 7, 6), (9, 9, 7)):
        d = rng.normal(size=(rows, rank)) @ rng.normal(size=(rank, columns))
        u, singular, _ = np.linalg.svd(d, full_matrices=False)
        image = u[:, singular > 1e-10]
        projection = image @ image.T
        assert np.allclose(projection, d @ np.linalg.pinv(d.T @ d) @ d.T)
        for _ in range(8):
            mask = np.diag(rng.integers(0, 2, size=rows))
            overlap = np.linalg.eigvalsh(mask @ projection @ mask).max()
            relative = np.eye(rank)-1.5*(image.T @ mask @ image)
            assert np.isclose(np.linalg.eigvalsh(relative).min(), 1-1.5*overlap)
            raw = d.T @ (np.eye(rows)-1.5*mask) @ d
            assert (np.linalg.eigvalsh(raw).min() < -1e-8) == (overlap > 2/3+1e-8)
            cases += 1
    # A negative target coefficient need not survive restriction to the image.
    d = np.ones((2, 1))
    assert np.isclose((d.T @ np.diag((1, -0.5)) @ d).item(), 0.5)
    return cases


if __name__ == "__main__":
    patch = build_patch()
    cases, error = covariance_checks(patch)
    print("PASS full 8^4 central configuration, positive single-link Hessians")
    print("PASS active two-well source and old certificate failure:", patch[-1])
    print("PASS normalized 72-link collective curvature:", patch[-3],
          "certified margin:", patch[-2])
    print("PASS transported gauge covariance and collective localizer:", cases,
          "max relative discrepancy:", error)
    print("PASS generic global jet bound and inherited form domination")
    commute_cases, commute_error = commuting_conditioning_checks(patch)
    print("PASS active conditional independence and commuting derivative quadrature:",
          commute_cases, "max discrepancy:", commute_error)
    print("PASS compatible-image spectral criterion:", compatible_image_checks())
    print("Scope: finite critical-context control; no global or physical mass gap.")
