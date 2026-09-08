"""Actual finite SU(2) overlapping-plaquette transfer and response checks.

Q=-2Tr, T_a=-i*sigma_a/2 and q=q0*I-i*q_vector.sigma, so the
fundamental Casimir is 3/4. Two adjacent squares have seven links;
their shared path has one link and each outside path has three.
The magnetic convention is lambda*sum_p(1-chi_p/2).

The 24-point S3 cubature is exact through degree four (in fact five).
Wilson integrals use refined latitude quadrature and exact degree-two
angular cubature, and are compared with independent Bessel series.
No Galerkin diagonalization, physical continuum limit, or finite-lambda
vacuum approximation is claimed. The magnetic coefficient is the
leading perturbative coefficient established by the analytic proof.
"""

from __future__ import annotations

import itertools
import math

import numpy as np


PAULI = (
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.array([[1, 0], [0, -1]], dtype=complex),
)
TA = tuple(-.5j * p for p in PAULI)
HAAR = np.concatenate((np.eye(4), -np.eye(4),
                       np.array(list(itertools.product((-.5, .5), repeat=4)))))
HW = np.full(len(HAAR), 1 / len(HAAR))
DIRECTIONS = np.concatenate((np.eye(3), -np.eye(3)))
X_WORD = ((1, 1), (2, 1), (3, 1), (0, -1))
Y_WORD = ((4, 1), (5, 1), (6, 1), (0, -1))


def close(actual, expected, *, rtol=3e-12, atol=4e-13):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert np.all(np.isfinite(actual)) and np.all(np.isfinite(expected))
    assert np.allclose(actual, expected, rtol=rtol, atol=atol), (actual, expected)


def multiply(left, right):
    left, right = np.asarray(left), np.asarray(right)
    scalar = left[..., 0] * right[..., 0] - np.sum(left[..., 1:] * right[..., 1:], axis=-1)
    vector = (left[..., 0, None] * right[..., 1:]
              + right[..., 0, None] * left[..., 1:]
              + np.cross(left[..., 1:], right[..., 1:]))
    return np.concatenate((scalar[..., None], vector), axis=-1)


def inverse(q):
    return np.asarray(q) * np.array([1, -1, -1, -1])


def matrix(q):
    return q[0] * np.eye(2) + sum(2 * q[a + 1] * TA[a] for a in range(3))


def word_matrix(links, word, derivative=None):
    value = np.eye(2, dtype=complex)
    for edge, sign in word:
        u = links[edge]
        factor = u if sign == 1 else u.conj().T
        if derivative is not None and derivative[0] == edge:
            factor = TA[derivative[1]] @ u if sign == 1 else -u.conj().T @ TA[derivative[1]]
        value = value @ factor
    return value


def word_jet(links, word):
    value = float(np.trace(word_matrix(links, word)).real)
    gradient = np.zeros((len(links), 3))
    for edge, _ in word:
        for axis in range(3):
            gradient[edge, axis] = np.trace(word_matrix(links, word, (edge, axis))).real
    # Each word uses each link once: T_a^2=-I/4 fixes each second derivative.
    laplacian = -.75 * len(word) * value
    return value, gradient, laplacian


def haar_and_link_checks():
    close(np.sum(HAAR ** 2, axis=1), 1)
    for degrees in itertools.product(range(5), repeat=4):
        total = sum(degrees)
        if total > 4:
            continue
        actual = HW @ np.prod(HAAR ** np.array(degrees), axis=1)
        if any(k % 2 for k in degrees):
            expected = 0.0
        else:
            expected = math.gamma(2) / math.gamma(2 + total / 2)
            for k in degrees:
                expected *= math.gamma((k + 1) / 2) / math.gamma(.5)
        close(actual, expected)
    for t in TA:
        close(-2 * np.trace(t @ t), 1)

    samples = [np.array([.5, .5, .5, .5]), np.array([.8, 0, .6, 0]),
               np.array([0, .6, 0, .8]), np.array([.6, .8, 0, 0])]
    links = [matrix(samples[i % len(samples)]) for i in range(7)]
    step = 2e-4
    for word in (X_WORD, Y_WORD):
        value, gradient, laplacian = word_jet(links, word)
        finite_laplacian = 0.0
        for edge in range(7):
            for axis in range(3):
                turn = math.cos(step / 2) * np.eye(2) + 2 * math.sin(step / 2) * TA[axis]
                plus, minus = list(links), list(links)
                plus[edge], minus[edge] = turn @ links[edge], turn.conj().T @ links[edge]
                fp = np.trace(word_matrix(plus, word)).real
                fm = np.trace(word_matrix(minus, word)).real
                close((fp - fm) / (2 * step), gradient[edge, axis], rtol=4e-9, atol=2e-12)
                finite_laplacian += (fp - 2 * value + fm) / step ** 2
        close(finite_laplacian, laplacian, atol=3e-7)
    print("PASS degree-four S3 Haar moments and actual seven-link Pauli first/second derivatives")


def physical_pair_checks():
    weights = HW[:, None] * HW[None, :]
    f, phi0, gamma, h0_f = (np.zeros((len(HAAR), len(HAAR))) for _ in range(4))
    for i, x in enumerate(HAAR):
        for j, y in enumerate(HAAR):
            links = [np.eye(2, dtype=complex) for _ in range(7)]
            links[1], links[4] = matrix(x), matrix(y)
            cx, gx, lx = word_jet(links, X_WORD)
            cy, gy, ly = word_jet(links, Y_WORD)
            cross = float(np.sum(gx * gy))
            close(cross, np.dot(x[1:], y[1:]))
            close(np.sum(gx ** 2), 4 * (1 - cx * cx / 4))
            close(np.sum(gy ** 2), 4 * (1 - cy * cy / 4))
            close(np.sum(gx[1:] * gy[1:]), 0)
            f[i, j] = cx * cy
            phi0[i, j] = np.trace(word_matrix(links, Y_WORD) @ word_matrix(links, X_WORD).conj().T).real
            gamma[i, j] = cross
            h0_f[i, j] = -(cy * lx + cx * ly + 2 * cross)
    inner = lambda u, v: float(np.sum(weights * u * v))
    phi1 = f - phi0 / 2
    close([inner(f, f), inner(phi0, phi0), inner(phi1, phi1)], [1, 1, .75])
    close([inner(phi0, phi1), inner(phi0, f)], [0, .5])
    close(gamma, (2 * phi0 - f) / 4)
    close(gamma @ HW, np.zeros(len(HAAR)))
    close(inner(gamma, gamma), 3 / 16)
    # Condition on BOTH complete class coordinates, not just one vector.
    # Each latitude block retains exact quadratic angular Haar moments.
    for x0 in np.unique(HAAR[:, 0]):
        for y0 in np.unique(HAAR[:, 0]):
            block = ((HAAR[:, 0] == x0)[:, None]
                     & (HAAR[:, 0] == y0)[None, :])
            conditional_weights = weights[block] / weights[block].sum()
            close(conditional_weights @ gamma[block], 0)
            close(conditional_weights @ phi0[block], 2 * x0 * y0)
            for duration in (0.0, .1, .7):
                actual = conditional_weights @ (
                    .5 * np.exp(-4.5 * duration) * phi0[block]
                    + np.exp(-6.5 * duration) * phi1[block])
                rate_mix = (.25 * np.exp(-4.5 * duration)
                            + .75 * np.exp(-6.5 * duration))
                close(actual, rate_mix * 4 * x0 * y0)
    # Kappa=1: outer six-link loop energy 9/2; shared adjoint adds 2.
    close(h0_f, 6.5 * f - phi0)
    close(h0_f - .5 * 4.5 * phi0, 6.5 * phi1)
    for kappa in (.4, 1.0, 2.0):
        e_y = 3 * kappa
        hidden_first = -kappa * gamma / e_y
        close(inner(hidden_first, hidden_first), 1 / 48)
        close(kappa * h0_f, .5 * (4.5 * kappa) * phi0 + (6.5 * kappa) * phi1)
    print("PASS actual shared-edge response: ||Gamma/kappa||^2=3/16, magnetic lambda^2 coefficient=1/48")
    print("PASS orthogonal character channels: norms 1 and 3/4, overlap 1/2, physical energies 9*kappa/2 and 13*kappa/2")
    print("PASS complete joint-character conditioning on every cubature latitude block, including the identity at t=0")
    return f, phi0, phi1, weights


def bessel(order, beta):
    term = (beta / 2) ** order / math.factorial(order)
    result = term
    for k in range(1, 1000):
        term *= beta * beta / (4 * k * (k + order))
        result += term
        if abs(term) < 1e-17 * max(1, abs(result)):
            return result
    raise AssertionError("Bessel series did not converge")


def wilson_grid(beta, order):
    angle = np.pi * np.arange(1, order + 1) / (order + 1)
    latitude = np.cos(angle)
    unnormalized = 2 * np.sin(angle) ** 2 * np.exp(beta * latitude) / (order + 1)
    z = float(unnormalized.sum())
    close(z, 2 * bessel(1, beta) / beta)
    weights = np.repeat(unnormalized / z / 6, 6)
    points = np.concatenate((np.repeat(latitude, 6)[:, None],
                             (np.sin(angle)[:, None, None] * DIRECTIONS).reshape(-1, 3)), axis=1)
    return points, weights


def wilson_convolution_checks(f, phi0, phi1, weights):
    inner = lambda u, v: float(np.sum(weights * u * v))
    basis = (phi0, phi1)
    gram = np.diag([1.0, .75])
    initial = np.array([.5, 1.0])
    print("Finite Wilson convolution: beta  first return  two-step nonsemigroup defect")
    for beta in (.4, 1.0, 4.0, 16.0):
        p1, p2 = (bessel(ell + 1, beta) / bessel(1, beta) for ell in (1, 2))
        actions = []
        for order in (32, 64):
            u, wu = wilson_grid(beta, order)
            matrix_mean = sum(w * matrix(q) for w, q in zip(wu, u))
            close(matrix_mean, p1 * np.eye(2))
            # The adjoint character is measured independently from actual U.
            close(wu @ (4 * u[:, 0] ** 2 - 1) / 3, p2)
            transformed_chars = 2 * multiply(HAAR[:, None, :], inverse(u)[None, :, :])[..., 0]
            shared_f = (transformed_chars * wu[None, :]) @ transformed_chars.T
            close(shared_f, .5 * phi0 + p2 * phi1)
            # Common right convolution fixes phi0 exactly, before integration.
            for q in u[::max(1, len(u) // 11)]:
                moved = multiply(HAAR, inverse(q))
                close(2 * multiply(moved[None, :, :], inverse(moved)[:, None, :])[..., 0], phi0)
            transformed_basis = (phi0, shared_f - .5 * phi0)
            action = np.linalg.solve(gram, np.array([
                [inner(left, right) for right in transformed_basis] for left in basis]))
            # Six independent outside fundamental-link convolutions.
            outside = np.linalg.matrix_power(matrix_mean, 6)[0, 0].real
            action *= outside
            close(action, np.diag([p1 ** 6, p1 ** 6 * p2]))
            actions.append(action)
        close(actions[0], actions[1])
        measured = {}
        for n in (0, 1, 2, 5, 11):
            measured[n] = float(initial @ gram @ np.linalg.matrix_power(actions[-1], n) @ initial)
            close(measured[n], .25 * p1 ** (6 * n) + .75 * (p1 ** 6 * p2) ** n)
        defect = measured[2] - measured[1] ** 2
        assert defect > 0
        print(f"{beta:g}  {measured[1]:.12g}  {defect:.12g}")
    print("PASS actual shared-link Wilson convolution and representation weights; scalar returns are a two-rate mixture, not a semigroup")


def box_plaquettes(size):
    result = {}
    for base in itertools.product(range(size + 1), repeat=3):
        for i, j in itertools.combinations(range(3), 2):
            if base[i] == size or base[j] == size:
                continue
            vi, vj = list(base), list(base)
            vi[i] += 1
            vj[j] += 1
            # An edge is its lower endpoint and positive coordinate direction.
            result[(base, i, j)] = (((base, i), 1), ((tuple(vi), j), 1),
                                     ((tuple(vj), i), -1), ((base, j), -1))
    return result


def box_incidence_checks():
    for size in (1, 2, 4):
        plaquettes = box_plaquettes(size)
        assert len(plaquettes) == 3 * size * size * (size + 1)
        edge_sets = {key: {edge for edge, _ in word} for key, word in plaquettes.items()}
        for word in plaquettes.values():
            boundary = {}
            for (base, axis), sign in word:
                end = list(base)
                end[axis] += 1
                for vertex, coefficient in ((base, -sign), (tuple(end), sign)):
                    boundary[vertex] = boundary.get(vertex, 0) + coefficient
            assert all(coefficient == 0 for coefficient in boundary.values())
        if size == 1:
            assert all(sum(bool(edges & other) for key2, other in edge_sets.items() if key2 != key) == 4
                       for key, edges in edge_sets.items())
        if size != 4:
            continue
        target = ((2, 2, 2), 0, 1)
        target_edges = edge_sets[target]
        neighbors = [key for key, edges in edge_sets.items() if key != target and edges & target_edges]
        assert len(neighbors) == 12
        assert all(sum(edge in edge_sets[key] for key in neighbors) == 3 for edge in target_edges)
        for key in neighbors:
            assert len(edge_sets[key] & target_edges) == 1
            assert edge_sets[key] - target_edges
        for first, second in itertools.combinations(neighbors, 2):
            # Flip this private link by -I. Gamma(p,first) changes sign,
            # Gamma(p,second) and the retained plaquette stay unchanged.
            witnesses = edge_sets[first] - target_edges - edge_sets[second]
            assert witnesses
            witness = sorted(witnesses)[0]
            parity_first = int(witness in target_edges) + int(witness in edge_sets[first])
            parity_second = int(witness in target_edges) + int(witness in edge_sets[second])
            assert parity_first % 2 == 1 and parity_second % 2 == 0
        coefficient = len(neighbors) / 48
        close(coefficient, .25)
        print(f"PASS open 3D box: {len(plaquettes)} oriented plaquettes, {len(neighbors)} bulk neighbors, 66 private-edge parity witnesses, coefficient {coefficient:g}")


if __name__ == "__main__":
    haar_and_link_checks()
    data = physical_pair_checks()
    wilson_convolution_checks(*data)
    box_incidence_checks()
    print("Finite physical-graph identities and leading magnetic perturbation checks only; no interacting continuum mass gap or finite-lambda spectral diagonalization.")
