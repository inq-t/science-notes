"""Finite checks of Wilson refresh locality and patch geometry, not a mass gap."""

import itertools as it
import numpy as np


def shift(x, mu, side):
    y = list(x)
    y[mu] = (y[mu] + 1) % side
    return tuple(y)


def finite_gibbs():
    vertices = list(it.product(range(2), range(3)))
    edges = [(x, mu) for x in vertices for mu in range(2)
             if x[mu] + 1 < (2, 3)[mu]]
    index = {e: j for j, e in enumerate(edges)}
    faces = []
    for y in range(2):
        faces.append([index[e] for e in (
            ((0, y), 0), ((1, y), 1), ((0, y + 1), 0), ((0, y), 1))])
    count, ne = 2**len(edges), len(edges)
    ids = np.arange(count)
    signs = 1 - 2 * ((ids[:, None] >> np.arange(ne)) & 1)
    plaquettes = np.column_stack([np.prod(signs[:, p], axis=1) for p in faces])
    # The full vertex gauge group, including its harmless global redundancy.
    masks = []
    for bits in it.product((0, 1), repeat=len(vertices)):
        assignment = dict(zip(vertices, bits))
        mask = 0
        for e, j in index.items():
            x, mu = e
            y = list(x)
            y[mu] += 1
            mask |= (assignment[x] ^ assignment[tuple(y)]) << j
        masks.append(mask)
    gauge = sum(np.eye(count)[ids ^ mask] for mask in masks) / len(masks)
    ev, vec = np.linalg.eigh(gauge)
    invariant = vec[:, ev > 0.5]
    assert invariant.shape[1] == 4
    for beta in (0.0, 0.2, 1.0, 3.0):
        w = np.exp(beta * plaquettes.sum(axis=1))
        w /= w.sum()
        root = np.sqrt(w)
        projections = []
        for e in range(ne):
            flipped = ids ^ (1 << e)
            probability = w / (w + w[flipped])
            p = np.zeros((count, count))
            p[ids, ids] = probability
            p[ids, flipped] = probability[flipped]
            transformed = root[:, None] * p / root[None, :]
            direct = np.diag(probability)
            direct[ids, flipped] = np.sqrt(probability * probability[flipped])
            assert np.max(abs(transformed - direct)) < 1e-12
            assert np.max(abs(direct @ direct - direct)) < 1e-12
            assert np.max(abs(direct @ root - root)) < 1e-12
            assert np.max(abs(direct @ gauge - gauge @ direct)) < 1e-12
            star = set().union(*(set(p) for p in faces if e in p))
            for remote in set(range(ne)) - star:
                assert np.max(abs(probability - probability[ids ^ (1 << remote)])) < 1e-12
            projections.append(direct)
        h = ne * np.eye(count) - sum(projections)
        restricted = invariant.T @ h @ invariant
        assert abs(np.linalg.eigvalsh(restricted)[0]) < 1e-10
        assert np.linalg.eigvalsh(restricted)[1] > 0
        for e, f in it.combinations(range(ne), 2):
            if not any(e in p and f in p for p in faces):
                assert np.max(abs(projections[e] @ projections[f]
                                  - projections[f] @ projections[e])) < 1e-12
    print("PASS: four actual Z2 Gibbs laws; density transform, gauge reduction, locality and commutation.")


def lattice_geometry(dim, side=6):
    vertices = list(it.product(range(side), repeat=dim))
    edges = [(x, mu) for x in vertices for mu in range(dim)]
    adjacent = {e: set() for e in edges}
    for x in vertices:
        for mu, nu in it.combinations(range(dim), 2):
            face = {(x, mu), (shift(x, mu, side), nu),
                    (shift(x, nu, side), mu), (x, nu)}
            for e in face:
                adjacent[e].update(face - {e})
    coarse_side = side // 2
    counts = {}
    active = 0
    region = set(it.product(range(2), repeat=dim))
    for e in edges:
        x, mu = e
        anchor = tuple(((x[nu] if nu == mu else x[nu] - 1) // 2) % coarse_side
                       for nu in range(dim))
        declared = {tuple((a + z) % coarse_side for a, z in zip(anchor, offset))
                    for offset in it.product((0, 1), repeat=dim)}
        actual = {tuple(v // 2 for v in origin)
                  for origin, _ in adjacent[e] | {e}}
        assert actual <= declared
        counts[anchor] = counts.get(anchor, 0) + 1
        if declared <= region:
            active += 1
        color = 2 * mu + sum(x[nu] for nu in range(dim) if nu != mu) % 2
        assert len(adjacent[e]) == 6 * (dim - 1)
        for y, direction in adjacent[e]:
            other = 2 * direction + sum(y[nu] for nu in range(dim) if nu != direction) % 2
            assert other != color
    assert set(counts.values()) == {dim * 2**dim}
    assert active == dim * 2**dim
    # Arithmetic only: these are not simulated large patches.
    g, layers = 6 * (dim - 1), 2 * dim
    threshold_constant = 200 * layers**2 * g**2 * 6**dim
    t = max(8 * layers**2, 64 * 4**dim * layers) + 1
    bound = min(g**2 / 16**dim, (1 - threshold_constant / t**2) / 6**dim)
    assert 0 < bound <= 1  # Independent Haar refresh has patch and full gap one.
    print(f"PASS: d={dim} even-torus supports, unique anchors, layers, counts; criterion arithmetic.")


def projection_converse():
    rng = np.random.default_rng(125)
    for size in (4, 11, 32):
        for _ in range(20):
            u, _ = np.linalg.qr(rng.normal(size=(size, size)))
            v, _ = np.linalg.qr(rng.normal(size=(size, size)))
            a = u[:, :size // 2] @ u[:, :size // 2].T
            b = v[:, :size // 3] @ v[:, :size // 3].T
            # I - A B A <= 3(2 I - A - B).
            defect = 3 * (2 * np.eye(size) - a - b) - (np.eye(size) - a @ b @ a)
            assert np.linalg.eigvalsh(defect)[0] > -1e-10
    print("PASS: 60 two-projection converse matrix checks.")


if __name__ == "__main__":
    finite_gibbs()
    for dimension in (2, 3, 4):
        lattice_geometry(dimension)
    projection_converse()
    print("Scope: finite algebra and incidence checks, not a nonlinear patch margin or physical gap.")
