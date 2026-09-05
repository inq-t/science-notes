"""Check the intrinsic normalized SU(2) conditional Hessian on two loop edges.

Both edges are loops at one vertex, so every readout word has common endpoints.
The Haar normalizer of a real quaternion average is a one-dimensional S^3
integral, evaluated by Gauss-Chebyshev quadrature of the second kind.
This checks identities and bounds, not a functional inequality numerically.
"""

import numpy as np

I = np.eye(2, dtype=complex)
PAULI = np.array([
    [[0, 1], [1, 0]],
    [[0, -1j], [1j, 0]],
    [[1, 0], [0, -1]],
], dtype=complex)
BASIS = np.concatenate([I[None], 1j * PAULI])
WORDS = (((0, 1), (1, 1)), ((1, 1), (0, 1)),
         ((0, -1), (1, -1)))
WEIGHTS = np.array([0.2, 0.3, 0.5])
PLAQUETTE = ((0, 1), (1, 1), (0, -1), (1, -1))
QUAD_J = np.arange(1, 257)
QUAD_X = np.cos(np.pi * QUAD_J / 257)
QUAD_W = 2 / 257 * np.sin(np.pi * QUAD_J / 257)**2


def quaternion(a):
    return np.array([np.trace(b.conj().T @ a).real / 2 for b in BASIS])


def matrix(q):
    return np.einsum("j,jab->ab", q, BASIS)


def random_su(rng):
    q = rng.normal(size=4)
    return matrix(q / np.linalg.norm(q))


def exp_generator(v, t):
    size = np.linalg.norm(v)
    if size == 0:
        return I
    return np.cos(t * size) * I + np.sin(t * size) / size * (
        1j * np.einsum("j,jab->ab", v, PAULI)
    )


def multiply_jets(a, b):
    return (a[0] @ b[0],
            a[1] @ b[0] + a[0] @ b[1],
            a[2] @ b[0] + 2 * a[1] @ b[1] + a[0] @ b[2])


def word_jet(links, vectors, word):
    result = (I, np.zeros((2, 2), complex), np.zeros((2, 2), complex))
    for edge, sign in word:
        u = links[edge]
        x = 1j * np.einsum("j,jab->ab", vectors[edge], PAULI)
        if sign == 1:
            factor = (u, u @ x, u @ x @ x)
        else:
            inv = u.conj().T
            factor = (inv, -x @ inv, x @ x @ inv)
        result = multiply_jets(result, factor)
    return result


def jets(links, vectors):
    p = word_jet(links, vectors, PLAQUETTE)
    paths = [word_jet(links, vectors, word) for word in WORDS]
    z = tuple(sum(w * jet[k] for w, jet in zip(WEIGHTS, paths)) for k in range(3))
    return p, tuple(quaternion(a) for a in z)


def normalizer(z, kappa):
    radius = np.linalg.norm(z)
    if radius < 1e-14:
        return 0.0, np.zeros(4), np.eye(4) / 4
    axis = z / radius
    terms = QUAD_W * np.exp(kappa * radius * QUAD_X)
    norm = terms.sum()
    mean_x = terms @ QUAD_X / norm
    second_x = terms @ (QUAD_X**2) / norm
    projector = np.outer(axis, axis)
    covariance = ((second_x - mean_x**2) * projector
                  + (1 - second_x) / 3 * (np.eye(4) - projector))
    assert np.linalg.eigvalsh(covariance).min() >= -1e-13
    return np.log(norm), mean_x * axis, covariance


def potential(links, coarse, beta, kappa):
    p, (z, _, _) = jets(links, np.zeros((2, 3)))
    lognorm, _, _ = normalizer(z, kappa)
    return beta * (1 - np.trace(p[0]).real / 2) - kappa * coarse @ z + lognorm


def hessian(links, vectors, coarse, beta, kappa):
    p, (z, dz, ddz) = jets(links, vectors)
    _, mean, covariance = normalizer(z, kappa)
    return (-beta * np.trace(p[2]).real / 2
            - kappa * (coarse - mean) @ ddz
            + kappa**2 * dz @ covariance @ dz)


def run():
    rng = np.random.default_rng(102)
    worst_fd_error = 0.0
    worst_mixed_ratio = 0.0
    tests = 0
    for beta, kappa in ((0.01, 0.03), (0.08, 0.4), (0.3, 2.0)):
        n_p = np.array([2, 2])
        path_n = np.array([[1, 1]] * len(WORDS))
        mean_n = WEIGHTS @ path_n
        d = beta * np.outer(n_p, n_p)
        d += 2 * kappa * sum(w * np.outer(n, n) for w, n in zip(WEIGHTS, path_n))
        j = d + kappa**2 * np.outer(mean_n, mean_n)
        rho_bound = 2 - np.linalg.norm(d, 2)
        for _ in range(10):
            links = np.array([random_su(rng), random_su(rng)])
            coarse = quaternion(random_su(rng))
            vectors = rng.normal(size=(2, 3))
            vectors /= np.linalg.norm(vectors)
            exact = hessian(links, vectors, coarse, beta, kappa)
            sizes = np.linalg.norm(vectors, axis=1)
            assert exact >= -sizes @ d @ sizes - 2e-12
            step = 0.002
            values = []
            for multiple in (-2, -1, 0, 1, 2):
                shifted = np.array([
                    u @ exp_generator(v, multiple * step)
                    for u, v in zip(links, vectors)
                ])
                values.append(potential(shifted, coarse, beta, kappa))
            fd = (-values[0] + 16 * values[1] - 30 * values[2]
                  + 16 * values[3] - values[4]) / (12 * step**2)
            worst_fd_error = max(worst_fd_error, abs(fd - exact))
            assert abs(fd - exact) < 2e-6
            basis = np.eye(6).reshape(6, 2, 3)
            diagonal = [hessian(links, v, coarse, beta, kappa) for v in basis]
            mixed = np.zeros((3, 3))
            for e in range(3):
                for f in range(3):
                    combined = hessian(links, basis[e] + basis[3 + f],
                                       coarse, beta, kappa)
                    mixed[e, f] = (combined - diagonal[e] - diagonal[3 + f]) / 2
            mixed_ratio = np.linalg.norm(mixed, 2) / j[0, 1]
            assert mixed_ratio <= 1 + 1e-12
            worst_mixed_ratio = max(worst_mixed_ratio, mixed_ratio)
            tests += 1
        print(f"beta={beta}, kappa={kappa}: sufficient Ricci-Hessian "
              f"floor={rho_bound:.6g}; {'positive' if rho_bound > 0 else 'inconclusive'}")
    print(f"PASS: {tests} nonlinear normalized Hessians; "
          f"max finite-difference error={worst_fd_error:.3g}; "
          f"max mixed/bound={worst_mixed_ratio:.6f}.")
    print("No weak-coupling, RG-depth, or continuum-gap claim.")


if __name__ == "__main__":
    run()
