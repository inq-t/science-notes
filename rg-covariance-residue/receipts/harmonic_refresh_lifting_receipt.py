"""Independent finite Gaussian gauge-quotient checks, not nonlinear Yang--Mills."""

import itertools as it
import numpy as np


def curl_matrix(side, dim):
    sites = list(it.product(range(side), repeat=dim))
    edges = [(x, mu) for mu in range(dim) for x in sites]
    index = {e: i for i, e in enumerate(edges)}
    rows = []
    for x in sites:
        for mu, nu in it.combinations(range(dim), 2):
            xm, xn = list(x), list(x)
            xm[mu], xn[nu] = (xm[mu] + 1) % side, (xn[nu] + 1) % side
            row = np.zeros(len(edges))
            for edge, sign in (((x, mu), 1), ((tuple(xm), nu), 1),
                               ((tuple(xn), mu), -1), ((x, nu), -1)):
                row[index[edge]] += sign
            rows.append(row)
    return np.array(rows)


def quotient(side, dim, spacing):
    curl = curl_matrix(side, dim)
    values, vectors = np.linalg.eigh(curl.T @ curl)
    keep = values > 1e-8
    return vectors[:, keep], np.diag(values[keep] / spacing**2)


def average_matrix(side, dim, factor):
    shape = (dim,) + (side,)*dim
    coarse = side // factor
    result = []
    for flat in np.eye(dim * side**dim):
        field = flat.reshape(shape)
        averaged = []
        for mu in range(dim):
            paths = sum(np.roll(field[mu], -j, axis=mu) for j in range(factor)) / factor
            averaged.append(paths.reshape((coarse, factor)*dim)
                            .mean(axis=tuple(range(1, 2*dim, 2))))
        result.append(np.array(averaged).ravel())
    return np.column_stack(result)


def minimum(a):
    return np.linalg.eigvalsh((a + a.T) / 2)[0]


def split(kf, q):
    cf = np.linalg.inv(kf)
    cc = q @ cf @ q.T
    kc = np.linalg.inv(cc)
    m = cf @ q.T @ kc
    _, singular, vt = np.linalg.svd(q, full_matrices=True)
    assert singular[-1] > 1e-8
    v = vt[len(singular):].T
    kv = v.T @ kf @ v
    assert np.max(abs(q @ m - np.eye(len(kc)))) < 1e-9
    assert np.max(abs(v.T @ kf @ m)) < 1e-8
    assert np.max(abs(m.T @ kf @ m - kc)) < 1e-8
    residual = cf - m @ cc @ m.T
    assert np.max(abs(residual @ q.T)) < 1e-9
    assert np.max(abs(residual - v @ np.linalg.inv(kv) @ v.T)) < 1e-8
    # The lifted OU drift is similar to the independent product precision.
    t = np.column_stack((v, m))
    blocks = np.zeros_like(kf)
    blocks[:len(kv), :len(kv)] = kv
    blocks[len(kv):, len(kv):] = kc
    mobility = v @ v.T + m @ m.T
    assert np.max(abs(mobility @ kf @ t - t @ blocks)) < 1e-8
    return kc, m, kv, mobility


def maxwell_case(dim, coarse, factor):
    side, a, b = coarse * factor, 1 / factor, 1.0
    vf, kf = quotient(side, dim, a)
    vc, kb = quotient(coarse, dim, b)
    q = factor**(dim / 2) * vc.T @ average_matrix(side, dim, factor) @ vf
    kc, m, kv, mobility = split(kf, q)
    r = (np.pi / 2)**(dim + 1)
    c = 4 / (1 + r*r)
    cmax = np.pi**2 * r*r / 4
    assert np.linalg.norm(q, 2) <= 1 + 1e-9
    assert np.linalg.norm(m, 2) <= r + 1e-9
    assert minimum(kc - kb) > -1e-8
    assert minimum(cmax * kb - kc) > -1e-8
    assert minimum(kv) * b*b >= c - 1e-9
    assert minimum((1 + r*r) * np.eye(len(kf)) - mobility) > -1e-8
    assert minimum(kf) >= min(c / b**2, minimum(kc)) / (1 + r*r) - 1e-9
    print(f"PASS: d={dim}, n={factor}, coarse side={coarse}; split, lift, forms and Maxwell bounds.")
    return vf, kf, vc, kb, q, m


def composite():
    dim, side, a = 2, 12, 0.25
    bases, k = zip(*(quotient(s, dim, a * (side // s)) for s in (12, 6, 3)))
    q0 = 2 * bases[1].T @ average_matrix(12, 2, 2) @ bases[0]
    q1 = 2 * bases[2].T @ average_matrix(6, 2, 2) @ bases[1]
    direct = 4 * bases[2].T @ average_matrix(12, 2, 4) @ bases[0]
    assert np.max(abs(q1 @ q0 - direct)) < 1e-10
    c0 = np.linalg.inv(k[0])
    c1, c2 = q0 @ c0 @ q0.T, direct @ c0 @ direct.T
    m0, m1 = c0 @ q0.T @ np.linalg.inv(c1), c1 @ q1.T @ np.linalg.inv(c2)
    mdirect = c0 @ direct.T @ np.linalg.inv(c2)
    assert np.max(abs(m0 @ m1 - mdirect)) < 1e-9
    eta = 0.07
    soft = c2 + eta * (0.5**2 * q1 @ q1.T + np.eye(len(c2)))
    precision = np.linalg.inv(soft)
    gamma = 1 + 4 * dim * eta / (1 - 0.25)
    assert minimum(precision - k[2] / gamma) > -1e-8
    assert minimum(np.linalg.inv(c2) - precision) > -1e-8
    print("PASS: exact two-level/composite harmonic identity and actual accumulated soft-noise comparison.")


def fourier_checks():
    rng = np.random.default_rng(125)
    for dim in (2, 3, 4):
        for factor in (2, 3, 8, 31):
            for _ in range(20):
                p = rng.uniform(-np.pi, np.pi, size=dim)
                q = p / factor
                dn = np.array([np.mean(np.exp(1j * np.arange(factor) * x)) for x in q])
                omega = np.prod(dn) * dn
                assert min(abs(omega)) >= (2 / np.pi)**(dim + 1) - 1e-12
                principal = 4 * factor**2 * np.sum(np.sin(q / 2)**2)
                coarse = 4 * np.sum(np.sin(p / 2)**2)
                assert principal <= (np.pi**2 / 4) * coarse + 1e-10
                # Coordinatewise principal-alias minimality implies the sum bound.
                for coordinate in range(dim):
                    aliases = (p[coordinate] + 2*np.pi*np.arange(factor)) / factor
                    assert min(np.sin(aliases / 2)**2) >= np.sin(q[coordinate] / 2)**2 - 1e-12
    print("PASS: 240 Fourier samples, principal-alias invertibility and energy ordering in d=2,3,4.")


if __name__ == "__main__":
    rng = np.random.default_rng(321)
    matrix = rng.normal(size=(9, 9))
    split(matrix.T @ matrix + np.eye(9), rng.normal(size=(3, 9)))
    for case in ((2, 3, 2), (2, 3, 3), (2, 3, 4), (3, 3, 2)):
        maxwell_case(*case)
    composite()
    fourier_checks()
    print("Scope: exact finite Gaussian identities and sampled bounds; no nonlinear or physical mass-gap claim.")
