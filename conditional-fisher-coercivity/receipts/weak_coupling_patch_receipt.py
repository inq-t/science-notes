"""Finite checks of the fixed-patch weak-coupling obstruction.

Stdout only. Incidence, Gaussian identities and compact SU(3) jets are checked.
The nonlinear Laplace theorem and continuum hypotheses are not numerical tests.
"""

from itertools import combinations, product
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]
                      / "rg-covariance-residue" / "receipts"))
from joint_context_escape_receipt import exp_anti, haar_su3, su3_basis


def shift(vertex, axis, step=1):
    result = list(vertex)
    result[axis] += step
    return tuple(result)


def cube(d, n):
    vertices = tuple(product(range(n), repeat=d))
    edges = tuple((x, mu) for x in vertices for mu in range(d)
                  if x[mu] < n - 1)
    index = {edge: i for i, edge in enumerate(edges)}
    plaquettes, rows = [], []
    for x in product(range(-1, n), repeat=d):
        for mu, nu in combinations(range(d), 2):
            p = (((x, mu), 1), ((shift(x, mu), nu), 1),
                 ((shift(x, nu), mu), -1), ((x, nu), -1))
            inside = tuple((edge, sign) for edge, sign in p if edge in index)
            if inside:
                assert len(inside) in (1, 4)
                row = np.zeros(len(edges))
                for edge, sign in inside:
                    row[index[edge]] = sign
                rows.append(row)
                plaquettes.append(p)
    curl = np.array(rows)
    internal = curl[np.count_nonzero(curl, axis=1) == 4]
    boundary = np.array(tuple(sum(x[nu] in (0, n - 1)
                                  for nu in range(d) if nu != mu)
                              for x, mu in edges))
    k = curl.T @ curl
    assert np.array_equal(k, internal.T @ internal + np.diag(boundary))
    assert np.array_equal(np.diag(k), np.full(len(edges), 2 * (d - 1)))
    inner_vertices = tuple(x for x in vertices
                           if all(0 < a < n - 1 for a in x))
    gradient = np.zeros((len(edges), len(inner_vertices)))
    inner_index = {x: i for i, x in enumerate(inner_vertices)}
    for i, (x, mu) in enumerate(edges):
        y = shift(x, mu)
        if x in inner_index:
            gradient[i, inner_index[x]] -= 1
        if y in inner_index:
            gradient[i, inner_index[y]] += 1
    assert np.allclose(curl @ gradient, 0)
    assert np.allclose(k @ gradient, 0)
    weights = {transverse: np.prod(np.sin(
        np.pi * (np.array(transverse) + 1) / (n + 1)))
        for transverse in product(range(n), repeat=d - 1)}
    v = np.array(tuple(weights[x[1:]] if mu == 0 else 0
                       for x, mu in edges))
    assert np.allclose(gradient.T @ v, 0)
    norm = float(v @ v)
    b = 1 - np.cos(np.pi / (n + 1))
    assert np.isclose(norm, (n - 1) * ((n + 1) / 2) ** (d - 1))
    assert np.isclose(v @ k @ v / norm, 2 * (d - 1) * b)
    return edges, plaquettes, k, v, weights, gradient


def geometry_checks():
    count = 0
    for d, n in product((2, 3, 4), (2, 3, 4)):
        edges, _, k, v, _, gradient = cube(d, n)
        values, vectors = np.linalg.eigh(k)
        positive = values > 1e-9
        assert np.count_nonzero(~positive) == (n - 2) ** d
        if gradient.shape[1]:
            assert np.linalg.matrix_rank(gradient) == gradient.shape[1]
        coefficients = vectors[:, positive].T @ v
        s = np.sum(coefficients**2 / values[positive])
        d0 = 2 * (d - 1)
        r = (v @ v) / (d0 * s)
        b = 1 - np.cos(np.pi / (n + 1))
        gaussian_gap = values[positive][0] / d0
        assert gaussian_gap <= r + 1e-12
        assert r <= b + 1e-12
        if n == 2:
            assert np.isclose(gaussian_gap, 0.5)
        else:
            assert b < 1 / n
        directions = (np.sqrt(values[positive])[:, None]
                      * vectors[:, positive].T / np.sqrt(d0))
        assert np.allclose(np.sum(directions**2, axis=0), 1)
        assert np.allclose(directions @ directions.T,
                           np.diag(values[positive] / d0))
        a = v**2 / d0
        quadratic_ratio = np.sum(4*s*a - 2*a*a) / (2*s*s)
        assert np.isclose(quadratic_ratio, 2*r - np.sum(a*a) / s**2)
        assert quadratic_ratio <= 2*r + 1e-12
        assert np.all(a <= s + 1e-12)
        print(f"PASS cube d={d} n={n}: edges={len(edges)}, "
              f"kernel={np.count_nonzero(~positive)}, "
              f"Gaussian gap={gaussian_gap:.10f}, "
              f"path rate={r:.10f}, neutral rate={quadratic_ratio:.10f}")
        count += 1
    for n in range(2, 33):
        b = 1 - np.cos(np.pi / (n + 1))
        if n >= 3:
            assert b < 1 / n
        if n >= 8:
            assert 2*b < 1 / n
    return count


def hermite_checks():
    rng = np.random.default_rng(124)
    count = 0
    for dimension in (2, 3, 4):
        directions = rng.normal(size=(dimension + 2, dimension))
        directions /= np.linalg.norm(directions, axis=1)[:, None]
        rates = rng.uniform(0.2, 2, size=len(directions))
        frame = sum(rate * np.outer(u, u)
                    for u, rate in zip(directions, rates))
        floor = np.linalg.eigvalsh(frame)[0]
        identity = np.eye(dimension)
        h2 = np.zeros((dimension**2, dimension**2))
        rhs = np.zeros_like(h2)
        for u, rate in zip(directions, rates):
            p = identity - np.outer(u, u)
            h2 += rate * (np.eye(dimension**2) - np.kron(p, p))
            rhs += rate * (np.kron(identity - p, identity)
                           + np.kron(identity, identity - p)) / 2
        assert np.linalg.eigvalsh(h2 - rhs).min() > -1e-12
        assert np.linalg.eigvalsh(h2).min() >= floor - 1e-12
        count += 1
    # Joint color refresh and separate color refresh are different processes.
    color_identity = np.eye(2)
    block_h2 = np.zeros((16, 16))
    scalar_h2 = np.zeros_like(block_h2)
    block_frame = np.zeros((4, 4))
    scalar_frame = np.zeros_like(block_frame)
    for u in (np.array((1.0, 0.0)), np.array((0.6, 0.8))):
        retained = np.kron(np.eye(2) - np.outer(u, u), color_identity)
        block_frame += np.eye(4) - retained
        block_h2 += np.eye(16) - np.kron(retained, retained)
        for color in color_identity:
            direction = np.kron(u, color)
            scalar_retained = np.eye(4) - np.outer(direction, direction)
            scalar_frame += np.eye(4) - scalar_retained
            scalar_h2 += (np.eye(16)
                          - np.kron(scalar_retained, scalar_retained))
    assert np.allclose(block_frame, scalar_frame)
    assert np.linalg.norm(block_h2 - scalar_h2) > 0.1
    assert np.linalg.eigvalsh(block_h2).min() >= (
        np.linalg.eigvalsh(block_frame).min() - 1e-12)
    count += 1
    return count


def action(plaquettes, field):
    total = 0.0
    identity = np.eye(3, dtype=complex)
    for p in plaquettes:
        value = identity
        for edge, orientation in p:
            u = field.get(edge, identity)
            value = value @ (u if orientation == 1 else u.conj().T)
        total += 1 - np.trace(value).real / 3
    return total


def path_sum(field, weights, n):
    result = np.zeros((3, 3), dtype=complex)
    for transverse, weight in weights.items():
        holonomy = np.eye(3, dtype=complex)
        for a in range(n - 1):
            holonomy = holonomy @ field[((a,) + transverse, 0)]
        result += weight * holonomy
    return result


def lie_projection(matrix):
    result = (matrix - matrix.conj().T) / 2
    return result - np.trace(result) * np.eye(3) / 3


def compact_checks():
    rng = np.random.default_rng(125)
    basis = su3_basis()
    count = 0
    for d, n in ((2, 3), (3, 3)):
        edges, plaquettes, k, v, weights, _ = cube(d, n)
        for _ in range(4):
            coefficients = rng.normal(size=(len(edges), len(basis)))
            directions = np.einsum("ea,aij->eij", coefficients, basis)
            step = 3e-4
            plus = {edge: exp_anti(step*x)
                    for edge, x in zip(edges, directions)}
            minus = {edge: exp_anti(-step*x)
                     for edge, x in zip(edges, directions)}
            expected_hessian = np.sum(coefficients * (k @ coefficients))
            observed_hessian = (action(plaquettes, plus)
                                + action(plaquettes, minus)) / step**2
            assert np.isclose(observed_hessian, expected_hessian,
                              rtol=5e-6, atol=1e-6)
            path_plus = path_sum(plus, weights, n)
            path_minus = path_sum(minus, weights, n)
            derivative = -np.trace(basis[0] @ (path_plus-path_minus)).real / (
                6*step)
            assert np.isclose(derivative, v @ coefficients[:, 0],
                              rtol=2e-5, atol=2e-6)
            phi_plus, phi_minus = (lie_projection(path_plus),
                                   lie_projection(path_minus))
            quadratic = (-np.trace(phi_plus @ phi_plus).real
                         - np.trace(phi_minus @ phi_minus).real) / (6*step**2)
            assert np.isclose(quadratic,
                              np.sum((v @ coefficients)**2), rtol=5e-6)
            gauge = {x: haar_su3(rng)
                     for x in product(range(n), repeat=d)
                     if all(0 < a < n-1 for a in x)}
            identity = np.eye(3, dtype=complex)
            moved = {edge: gauge.get(edge[0], identity) @ plus[edge]
                     @ gauge.get(shift(*edge), identity).conj().T
                     for edge in edges}
            assert np.allclose(path_sum(moved, weights, n), path_plus)
            assert np.isclose(action(plaquettes, moved),
                              action(plaquettes, plus), atol=1e-12)
            root_rotation = haar_su3(rng)
            conjugated = root_rotation @ path_plus @ root_rotation.conj().T
            rotated_phi = lie_projection(conjugated)
            assert np.allclose(rotated_phi,
                               root_rotation @ phi_plus @ root_rotation.conj().T)
            assert np.isclose(np.trace(rotated_phi @ rotated_phi),
                              np.trace(phi_plus @ phi_plus))
            count += 1
    return count


if __name__ == "__main__":
    print("PASS complete cube matrix cases:", geometry_checks())
    print("PASS second-tensor Hermite comparisons:", hermite_checks())
    print("PASS compact-group action, path and neutral jets:", compact_checks())
    print("Scope: finite geometry and identities, not a simulated "
          "nonlinear spectral limit or a physical mass gap.")
