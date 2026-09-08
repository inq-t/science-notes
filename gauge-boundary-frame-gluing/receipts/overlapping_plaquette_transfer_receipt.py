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


def orientation_carrier_checks():
    """Three loops: pairwise closure is exact but misses an odd physical mode.

    Pairwise traces determine the O(3) Gram orbit, whereas physical gauge
    conjugation acts by SO(3). Simultaneous inversion supplies the missing
    reflection. The analytic reducing-subspace proof uses equality of
    common left/right Casimirs on simultaneous-conjugation invariants;
    the derivative tests below check that identity on actual readouts.
    """
    triples = np.array(list(itertools.product(HAAR, repeat=3)))
    vectors = triples[..., 1:]
    tau = np.einsum("ni,ni->n", vectors[:, 0], np.cross(vectors[:, 1], vectors[:, 2]))
    close(np.mean(tau), 0)
    close(np.mean(tau ** 2), 3 / 32)
    reflected = inverse(triples)
    reflected_tau = np.linalg.det(reflected[..., 1:])
    close(reflected_tau, -tau)
    for i, j in itertools.combinations(range(3), 2):
        pair = 2 * multiply(triples[:, i], inverse(triples[:, j]))[:, 0]
        reflected_pair = 2 * multiply(reflected[:, i], inverse(reflected[:, j]))[:, 0]
        close(pair, reflected_pair)
        close(np.mean(tau * pair), 0)
        close(np.mean(tau * pair ** 2), 0)
    close(triples[..., 0], reflected[..., 0])

    def quaternion(u):
        return np.array([np.trace(u).real / 2] + [-np.trace(t @ u).real for t in TA])

    def readouts(links):
        q = np.array([quaternion(u) for u in links])
        x = multiply(q[1:], inverse(q[0]))
        orientation = float(np.linalg.det(x[:, 1:]))
        close(orientation, np.linalg.det(q))
        singles = 2 * x[:, 0]
        pair01 = 2 * multiply(x[0], inverse(x[1]))[0]
        pair12 = 2 * multiply(x[1], inverse(x[2]))[0]
        even = singles.prod() + .3 * pair01 * pair12
        odd = orientation * (1 + .2 * singles[0])
        return np.array([orientation, even, odd])

    samples = (
        np.eye(4),
        np.array([[.5, .5, .5, .5], [.8, .6, 0, 0],
                  [.6, 0, .8, 0], [.6, 0, 0, .8]]),
    )
    alpha = np.array([.7, 1.1, 1.4, .9])
    step = 2e-4

    def physical_derivatives(links):
        values = readouts(links)
        edge_laplacians = np.zeros((4, len(values)))
        for edge in range(4):
            for axis in range(3):
                turn = math.cos(step / 2) * np.eye(2) + 2 * math.sin(step / 2) * TA[axis]
                plus, minus = list(links), list(links)
                plus[edge], minus[edge] = turn @ links[edge], turn.conj().T @ links[edge]
                edge_laplacians[edge] += (readouts(plus) - 2 * values + readouts(minus)) / step ** 2
        close(edge_laplacians[:, 0], np.full(4, -.75 * values[0]), atol=2e-7)
        return -(alpha @ edge_laplacians)

    for q in samples:
        links = [matrix(value) for value in q]
        values = readouts(links)
        physical = physical_derivatives(links)
        close(physical[0], .75 * alpha.sum() * values[0], atol=7e-7)
        # OG15: the determinant ground transform returns drift five,
        # not the drift three of a bare quaternion Gram coordinate.
        odd_edge = .75 * alpha.sum()
        odd_pair_edge = odd_edge + 1.25 * (alpha[0] + alpha[1])
        close(physical[2], odd_edge * values[0]
              + .4 * odd_pair_edge * values[0] * (q[0] @ q[1]), atol=2e-6)
        # Gauge to a=1, then reflect the three actual loop holonomies.
        x = multiply(q[1:], inverse(q[0]))
        direct_links = [np.eye(2)] + [matrix(value) for value in x]
        inverse_links = [np.eye(2)] + [matrix(value) for value in inverse(x)]
        direct_values, inverse_values = readouts(direct_links), readouts(inverse_links)
        parity = np.array([-1, 1, -1])
        close(inverse_values, parity * direct_values)
        close(physical_derivatives(inverse_links), parity * physical_derivatives(direct_links), atol=2e-6)

        # Independent common-left/common-right Casimir check, not a
        # replacement by independently reset loop generators.
        common_laplacians = []
        for handedness in ("left", "right"):
            laplacian = np.zeros(3)
            for axis in range(3):
                turn = math.cos(step / 2) * np.eye(2) + 2 * math.sin(step / 2) * TA[axis]
                if handedness == "left":
                    plus = [np.eye(2)] + [turn @ u for u in direct_links[1:]]
                    minus = [np.eye(2)] + [turn.conj().T @ u for u in direct_links[1:]]
                else:
                    plus = [np.eye(2)] + [u @ turn for u in direct_links[1:]]
                    minus = [np.eye(2)] + [u @ turn.conj().T for u in direct_links[1:]]
                laplacian += (readouts(plus) - 2 * direct_values + readouts(minus)) / step ** 2
            common_laplacians.append(laplacian)
        close(common_laplacians[0], common_laplacians[1], atol=8e-7)
    print("PASS three-loop orientation: pairwise traces forget tau, ||tau||^2=3/32, four-link energy=(3/4)*sum(alpha)")
    print("PASS actual four-link derivatives and common left/right Casimirs: pairwise parity closure does not cover the odd physical carrier")
    print("PASS determinant-weighted linear Gram mode: inherited coefficient drift is five")


def context_gluing_checks():
    """Complete local invariant data can still omit a relative boundary frame.

    Three independent shared quaternions fix the frame after orientation
    is retained. Two shared quaternions leave an SO(2) gluing fibre.
    Rank-deficient cubature nodes are never discarded: the residual
    polynomial moment identities extend to those nodes continuously.
    """
    alpha0 = 1.7

    def pair_gradient(links, i, j):
        gradient = np.zeros((len(links), 3))
        product = links[i] @ links[j].conj().T
        for axis, t in enumerate(TA):
            gradient[i, axis] = .5 * np.trace(t @ product).real
            gradient[j, axis] = -.5 * np.trace(product @ t).real
        return gradient

    def qfrom(u):
        return np.array([np.trace(u).real / 2] + [-np.trace(t @ u).real for t in TA])

    sample = np.array([[.5, .5, .5, .5], [.8, .6, 0, 0],
                       [.6, 0, .8, 0], [.6, 0, 0, .8],
                       [0, .6, 0, .8], [.5, -.5, .5, -.5]])
    links = [matrix(q) for q in sample]
    gf, gg = pair_gradient(links, 0, 2), pair_gradient(links, 0, 4)
    actual_gamma = alpha0 * float(gf[0] @ gg[0])
    expected_gamma = alpha0 / 4 * (sample[2] @ sample[4]
                                    - (sample[0] @ sample[2]) * (sample[0] @ sample[4]))
    close(actual_gamma, expected_gamma)
    step = 2e-4
    for target, gradient in ((2, gf), (4, gg)):
        for edge in (0, target):
            for axis, t in enumerate(TA):
                turn = math.cos(step / 2) * np.eye(2) + 2 * math.sin(step / 2) * t
                plus, minus = list(links), list(links)
                plus[edge], minus[edge] = turn @ links[edge], turn.conj().T @ links[edge]
                fp = .5 * np.trace(plus[0] @ plus[target].conj().T).real
                fm = .5 * np.trace(minus[0] @ minus[target].conj().T).real
                close((fp - fm) / (2 * step), gradient[edge, axis], rtol=4e-9, atol=2e-12)

    # Ordered determinant replacement is checked from actual Pauli tangents.
    invariant = (0, 1, 2, 3)
    tau = float(np.linalg.det(sample[list(invariant)]))
    for a in invariant:
        j = 4
        determinant_gradient = np.zeros(3)
        for axis, t in enumerate(TA):
            differentiated = sample[list(invariant)].copy()
            differentiated[invariant.index(a)] = qfrom(t @ links[a])
            determinant_gradient[axis] = np.linalg.det(differentiated)
        replaced = sample[list(invariant)].copy()
        replaced[invariant.index(a)] = sample[j]
        actual = alpha0 * determinant_gradient @ pair_gradient(links, a, j)[a]
        expected = alpha0 / 4 * (np.linalg.det(replaced) - tau * (sample[a] @ sample[j]))
        close(actual, expected)

    def adjugate3(a):
        return np.array([[(-1) ** (i + j) * np.linalg.det(np.delete(np.delete(a, j, 0), i, 1))
                          for j in range(3)] for i in range(3)])

    def gluing_identity(shared, u3, u4):
        a = shared @ shared.T
        b3, b4 = shared @ u3, shared @ u4
        tau3 = np.linalg.det(np.vstack((shared, u3)))
        tau4 = np.linalg.det(np.vstack((shared, u4)))
        determinant = np.linalg.det(a)
        adjugate = adjugate3(a)
        close(a @ adjugate, determinant * np.eye(3))
        close(determinant * (u3 @ u4), b3 @ adjugate @ b4 + tau3 * tau4)
        if determinant > 1e-7:
            rebuilt = b3 @ np.linalg.solve(a, b4) + tau3 * tau4 / determinant
            close(rebuilt, u3 @ u4, rtol=3e-10, atol=3e-10)
        return determinant, tau3, tau4

    gluing_identity(sample[:3], sample[3], sample[4])
    e = np.eye(4)
    previous = math.inf
    for epsilon in (.5, .2, .05, .01, .002):
        shared = np.array([e[0], e[1], math.sqrt(1 - epsilon ** 2) * e[0] + epsilon * e[2]])
        for sign in (1, -1):
            determinant, tau3, tau4 = gluing_identity(shared, e[3], sign * e[3])
            close([determinant, tau3, tau4], [epsilon ** 2, epsilon, sign * epsilon])
            actual = alpha0 * (pair_gradient([matrix(q) for q in (*shared, e[3], sign * e[3])], 0, 3)[0]
                               @ pair_gradient([matrix(q) for q in (*shared, e[3], sign * e[3])], 0, 4)[0])
            close(actual, sign * alpha0 / 4)
        # The only differing local oriented invariant is tau4: its
        # difference vanishes, while cross pairing and response do not.
        assert 2 * epsilon < previous
        previous = 2 * epsilon
    gluing_identity(np.array([e[0], e[1], e[0]]), e[2], e[3])
    print("PASS rank-three oriented gluing identity, polynomial rank-wall extension, and nonuniform epsilon reconstruction")

    # Both four-link contexts have full rank; the shared pair has rank two.
    for order in (16, 32, 64):
        theta = 2 * np.pi * np.arange(order) / order
        responses = []
        for angle in theta:
            right4 = math.cos(angle) * e[2] + math.sin(angle) * e[3]
            right5 = -math.sin(angle) * e[2] + math.cos(angle) * e[3]
            q = np.array([e[0], e[1], e[2], e[3], right4, right5])
            for indices in ((0, 1, 2, 3), (0, 1, 4, 5)):
                context = q[list(indices)]
                close(context @ context.T, np.eye(4))
                close(np.linalg.det(context), 1)
            links = [matrix(value) for value in q]
            response = alpha0 * pair_gradient(links, 0, 2)[0] @ pair_gradient(links, 0, 4)[0]
            close(response, alpha0 * math.cos(angle) / 4)
            responses.append(response)
        close(np.mean(responses), 0)
        close(np.var(responses), alpha0 ** 2 / 32)

    # Rotational invariance fixes the shared span, not a conditionally
    # sampled pair of possibly degenerate cubature vectors. The actual
    # six-link Haar integral of residual moments is independent of its
    # Gram angle. All u2/u4 cubature nodes, including rank walls, remain.
    matrices2 = np.array([matrix(q) for q in HAAR])
    derivatives2 = .5 * np.einsum("aij,nji->na", np.array(TA), matrices2.conj().transpose(0, 2, 1)).real
    final_variance = None
    for order in (16, 32, 64):
        theta = 2 * np.pi * np.arange(order) / order
        rotated = np.repeat(HAAR[:, None, :], order, axis=1)
        rotated[..., 2] = HAAR[:, 2, None] * np.cos(theta) - HAAR[:, 3, None] * np.sin(theta)
        rotated[..., 3] = HAAR[:, 2, None] * np.sin(theta) + HAAR[:, 3, None] * np.cos(theta)
        matrices4 = np.array([[matrix(q) for q in row] for row in rotated])
        derivatives4 = .5 * np.einsum("aij,ntji->nta", np.array(TA), matrices4.conj().transpose(0, 1, 3, 2)).real
        responses = alpha0 * np.einsum("ia,jta->ijt", derivatives2, derivatives4)
        means = responses.mean(axis=2)
        conditional_variance = np.mean((responses - means[..., None]) ** 2, axis=2)
        residual_norms = np.sum(HAAR[:, 2:] ** 2, axis=1)
        close(conditional_variance, alpha0 ** 2 / 32 * residual_norms[:, None] * residual_norms[None, :])
        final_variance = float(HW @ conditional_variance @ HW)
        close(final_variance, alpha0 ** 2 / 128)
    norm_fg = float(HW @ ((HAAR[:, 0, None] * HAAR[None, :, 0]) ** 2) @ HW)
    close(norm_fg, 1 / 16)
    hidden_h_fg = 4 * final_variance
    close(hidden_h_fg, alpha0 ** 2 / 32)
    close(hidden_h_fg / norm_fg, alpha0 ** 2 / 2)
    print("PASS actual pair/determinant Pauli response identities and complete-local-context SO(2) gluing freedom")
    print("PASS independent angle/Haar moments: hidden Gamma norm^2=alpha0^2/128, hidden H(FG) norm^2=alpha0^2/32, normalized 4FG defect=alpha0^2/2")


if __name__ == "__main__":
    haar_and_link_checks()
    data = physical_pair_checks()
    wilson_convolution_checks(*data)
    box_incidence_checks()
    orientation_carrier_checks()
    context_gluing_checks()
    print("Finite physical-graph identities and leading magnetic perturbation checks only; no interacting continuum mass gap or finite-lambda spectral diagonalization.")
