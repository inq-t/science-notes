"""Finite source-quadrature tests for a static SU(2) star with memory.

v has density exp(beta*v0)/Z(beta) relative to normalized Haar; h is
independent Haar, and the actual readout is x=v*h^{-1}.  Q=-2Tr and
T_a=-i*sigma_a/2, hence Q=4*g_round and -Delta_Q(v_mu)=3*v_mu/4.
The source generator is a1*(Delta_v+grad(log p).grad_v)+a0*Delta_h.
The code represents q by q0*I-i*q_vector.sigma (positive quaternion
cross product), whereas the accompanying note uses q0*I+i*q_vector.sigma.
Their vector coordinates have opposite signs. With the same T_a, the
code's left score is -beta*q_vector/2; the note's is +beta*q_vector/2.
This coordinate reversal changes neither the Fisher tensor nor energies.

Latitude quadrature is refined at three orders. Angular cubatures are
exact for the degrees occurring here: degree two on the v-direction S2
and degree two in h on S3. The code evaluates actual source functions
before averaging, independently checks their quaternion derivatives,
and compares with Bessel series. The final test uses two tilted profiles
and the fully endpoint-neutral character of v1*v2^{-1}; it checks an
actual reducing source projection and its low-spectral-weight bound.
It writes no files. Finite checks do
not prove a continuum field theory, a physical gap, or a spectral theorem.
"""

from __future__ import annotations

import math

import numpy as np


C = 0.75
PAULI = (
    np.array([[0, 1], [1, 0]], dtype=complex),
    np.array([[0, -1j], [1j, 0]], dtype=complex),
    np.array([[1, 0], [0, -1]], dtype=complex),
)
GENERATORS = tuple(-0.5j * s for s in PAULI)
H_POINTS = np.concatenate((np.eye(4), -np.eye(4)))
H_WEIGHTS = np.full(8, 1 / 8)
DIRECTIONS = np.concatenate((np.eye(3), -np.eye(3)))


def close(actual, expected, *, rtol=3e-12, atol=3e-13):
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
    return q[0] * np.eye(2) + sum(2 * q[a + 1] * GENERATORS[a] for a in range(3))


def turn(axis, step):
    value = np.zeros(4)
    value[0], value[axis + 1] = math.cos(step / 2), math.sin(step / 2)
    return value


def readout(v, h):
    return 2 * multiply(v, inverse(h))[..., 0]


def bessel(order, beta):
    term = (beta / 2) ** order / math.factorial(order)
    value = term
    for k in range(1, 1000):
        term *= beta * beta / (4 * k * (k + order))
        value += term
        if abs(term) <= 1e-17 * max(1, abs(value)):
            return value
    raise AssertionError("Bessel series did not converge")


def source_grid(beta, order):
    angles = np.pi * np.arange(1, order + 1) / (order + 1)
    latitude = np.cos(angles)
    haar = 2 * np.sin(angles) ** 2 / (order + 1)
    tilted = haar * np.exp(beta * latitude)
    normalizer = float(tilted.sum())
    weights = np.repeat(tilted / normalizer / len(DIRECTIONS), len(DIRECTIONS))
    points = np.concatenate((
        np.repeat(latitude, len(DIRECTIONS))[:, None],
        (np.sqrt(1 - latitude ** 2)[:, None, None] * DIRECTIONS).reshape(-1, 3),
    ), axis=1)
    close(np.sum(points * points, axis=1), 1)
    close(weights.sum(), 1)
    return points, weights, normalizer


def coordinate_generator(v, beta):
    """Actual L_v acting on the four coordinate functions, not on x."""
    radial = -v[..., 0, None] * v
    radial[..., 0] += 1
    return -C * v + (beta / 4) * radial


def derivative_checks():
    samples = (
        (np.array([.5, .5, .5, .5]), np.array([.8, 0, .6, 0])),
        (np.array([.6, 0, .8, 0]), np.array([0, .6, 0, .8])),
    )
    for a, generator in enumerate(GENERATORS):
        close(-2 * np.trace(generator @ generator), 1)
        close(matrix(turn(a, .37)), math.cos(.37 / 2) * np.eye(2)
              + 2 * math.sin(.37 / 2) * generator)
    for v, h in samples:
        close(matrix(multiply(v, inverse(h))), matrix(v) @ matrix(h).conj().T)
        x = multiply(v, inverse(h))
        value = readout(v, h)
        dv, dh = [], []
        lap_v = lap_h = 0.0
        for axis in range(3):
            step = 2e-4
            plus, minus = turn(axis, step), turn(axis, -step)
            vp, vm = multiply(plus, v), multiply(minus, v)
            hp, hm = multiply(plus, h), multiply(minus, h)
            dv.append((readout(vp, h) - readout(vm, h)) / (2 * step))
            dh.append((readout(v, hp) - readout(v, hm)) / (2 * step))
            lap_v += (readout(vp, h) - 2 * value + readout(vm, h)) / step ** 2
            lap_h += (readout(v, hp) - 2 * value + readout(v, hm)) / step ** 2
            beta = 1.7
            finite_score = beta * (vp[0] - vm[0]) / (2 * step)
            close(finite_score, -beta * v[axis + 1] / 2, rtol=3e-9)
        close(dv, -x[1:], rtol=3e-9)
        close(dh, x[1:], rtol=3e-9)
        close([lap_v, lap_h], [-C * value] * 2, atol=6e-8)
        direct = .6 * (lap_v + np.dot(-1.7 * v[1:] / 2, dv)) + .4 * lap_h
        coordinates = 2 * .6 * np.dot(coordinate_generator(v, 1.7), h) - .4 * C * value
        close(direct, coordinates, atol=6e-8)
    print("PASS actual quaternion source derivatives, Pauli products, Q=4*g_round, and source generator normalization")


def source_moments(beta, a1, a0, order):
    v, weight_v, normalizer = source_grid(beta, order)
    h = H_POINTS
    weights = weight_v[:, None] * H_WEIGHTS[None, :]
    x = multiply(v[:, None, :], inverse(h)[None, :, :])
    value = readout(v[:, None, :], h[None, :, :])
    close(value, 2 * np.einsum("vi,hi->vh", v, h))
    expectation = lambda array: np.einsum("vh,vh->", weights, array)
    close(expectation(value), 0)
    close(expectation(value * value), 1)
    close(np.einsum("vh,vhi,vhj->ij", weights, x, x), np.eye(4) / 4)

    score = -beta * v[:, 1:] / 2
    fisher = np.einsum("v,vi,vj->ij", weight_v, score, score)
    mean = float(weight_v @ v[:, 0])
    close(weight_v @ score, np.zeros(3))
    close(weight_v @ coordinate_generator(v, beta), np.zeros(4))
    mean_series = bessel(2, beta) / bessel(1, beta) if beta else 0.0
    z_series = 2 * bessel(1, beta) / beta if beta else 1.0
    close(normalizer, z_series)
    close(mean, mean_series)
    close(fisher, beta * mean_series * np.eye(3) / 4)

    gradient = -x[..., 1:]
    response = (a0 + a1) * expectation(np.sum(gradient * gradient, axis=-1))
    kappa = C * (a0 + a1)
    close(response, kappa)
    # Independently generate L_source(Jf) from all four v coordinates.
    source_lf = (2 * a1 * np.einsum("vi,hi->vh", coordinate_generator(v, beta), h)
                 - a0 * C * value)
    residual = source_lf + kappa * value
    direct_score_residual = a1 * np.einsum("vi,vhi->vh", score, gradient)
    close(residual, direct_score_residual)
    coefficient = float(expectation(residual * residual))
    expected_coefficient = 3 * a1 * a1 * beta * mean_series / 16
    close(coefficient, expected_coefficient)
    close(-expectation(value * source_lf), kappa)
    close(expectation(source_lf * source_lf) - kappa * kappa, coefficient)

    # Actual v-vacuum projection of Jf, integrated separately for every h.
    projected = weight_v @ value
    close(projected, 2 * mean_series * h[:, 0])
    atom = float(H_WEIGHTS @ (projected * projected))
    close(atom, mean_series ** 2)
    close(expectation((value - projected[None, :]) * projected[None, :]), 0)
    if beta == 0:
        close(source_lf, -kappa * value)
        close([atom, coefficient], [0, 0])
    else:
        assert atom > 0 and coefficient > 0
    return np.array([mean, coefficient, atom, response])


def memory_checks():
    print("Actual source quadrature: beta  t^2-defect coefficient  lowest-atom weight  retained first moment")
    for beta in (0.0, .2, 1.0, 3.0, 8.0):
        values = [source_moments(beta, .6, .4, n) for n in (24, 48, 96)]
        for value in values[:-1]:
            close(value, values[-1])
        mean, coefficient, atom, response = values[-1]
        print(f"{beta:4g}  {coefficient:.12g}  {atom:.12g}  {response:.12g}")
    print("PASS 24/48/96-point tilted latitude quadratures with exact angular degree-two cubatures; actual source score, generator moments, and vacuum projection agree")

    beta = 3.0
    previous = math.inf
    print("Fixed beta=3, a0=epsilon, a1=1-epsilon: visible atom location  weight  fixed first moment")
    for epsilon in (.5, .1, .02, .004):
        _, _, atom, first = source_moments(beta, 1 - epsilon, epsilon, 96)
        location = C * epsilon
        assert 0 < location < previous and atom > 0
        close(first, C)
        previous = location
        print(f"{location:.12g}  {atom:.12g}  {first:.12g}")
    print("PASS fixed instantaneous form with nonzero source vacuum-projection weight at a0*3/4; the exact visible-tail statement uses compact elliptic spectral theory, not a numerical diagonalization")


def coincident_profile_checks():
    """Differentiate the actual product profile before the shared Haar integral."""
    for m in (2, 4, 6):
        for beta in (.2, 1.0, 3.0):
            v, weights, _ = source_grid(m * beta, 96)
            score = -beta * v[:, 1] / 2
            second_log_factor = -beta * v[:, 0] / 4
            scalar_fisher = float(weights @ (score * score))
            mean = bessel(2, m * beta) / bessel(1, m * beta)
            close(scalar_fisher, beta * mean / (4 * m))
            for direction in (np.ones(m), np.arange(1, m + 1), (-1.) ** np.arange(m)):
                first_product = score * direction.sum()
                second_log_product = second_log_factor * (direction @ direction)
                hessian = -weights @ (second_log_product + first_product ** 2) + (weights @ first_product) ** 2
                expected = scalar_fisher * (m * (direction @ direction) - direction.sum() ** 2)
                close(hessian, expected)
    print("PASS nine actual exponential-profile coincident stars: integrated product jets, common-motion null direction, and Q-normalized Fisher coefficient")


def endpoint_neutral_moments(beta1, beta2, order):
    """Actual product-source projection; angular degree two in each factor.

    The v2-constant source subspace reduces the product generator. Its
    centered component g has spectral mass W and first moment a1*M.
    Markov's bound therefore puts at least W/2 of that component in
    (0, a1*R], R=2*M/W. The full character measure dominates this
    component. No eigenvalues are estimated by these quadratures.
    """
    v1, weight1, _ = source_grid(beta1, order)
    v2, weight2, _ = source_grid(beta2, order)
    weights = weight1[:, None] * weight2[None, :]
    expectation = lambda array: np.einsum("ij,ij->", weights, array)
    x = multiply(v1[:, None, :], inverse(v2)[None, :, :])
    raw = readout(v1[:, None, :], v2[None, :, :])
    close(raw, 2 * np.einsum("ik,jk->ij", v1, v2))
    # Both endpoint actions are invisible to the actual character readout.
    k = np.array([.5, .5, .5, .5])
    sample1, sample2 = v1[::max(1, len(v1) // 7)], v2[::max(1, len(v2) // 7)]
    base = readout(sample1[:, None, :], sample2[None, :, :])
    close(readout(multiply(k, sample1)[:, None, :], multiply(k, sample2)[None, :, :]), base)
    close(readout(multiply(sample1, k)[:, None, :], multiply(sample2, k)[None, :, :]), base)
    b1 = bessel(2, beta1) / bessel(1, beta1)
    b2 = bessel(2, beta2) / bessel(1, beta2)
    center = float(expectation(raw))
    close(center, 2 * b1 * b2)
    value = raw - center
    close(expectation(value), 0)

    # Source-coordinate differentiation before conditioning or scalarization.
    gradient1, gradient2 = -x[..., 1:], x[..., 1:]
    l1_value = 2 * np.einsum("ik,jk->ij", coordinate_generator(v1, beta1), v2)
    l2_value = 2 * np.einsum("ik,jk->ij", v1, coordinate_generator(v2, beta2))
    energy1 = float(expectation(np.sum(gradient1 ** 2, axis=-1)))
    energy2 = float(expectation(np.sum(gradient2 ** 2, axis=-1)))
    close(energy1, energy2)
    close(-expectation(value * l1_value), energy1)
    close(-expectation(value * l2_value), energy2)

    # Compute the actual v2-vacuum projection at each sampled v1.
    projected = value @ weight2
    projected_gradient = np.einsum("j,ijk->ik", weight2, gradient1)
    projected_l1 = l1_value @ weight2
    close(projected, 2 * b2 * (v1[:, 0] - b1))
    close(projected_gradient, -b2 * v1[:, 1:])
    close(l2_value @ weight2, np.zeros(len(v1)))
    close(weight1 @ projected, 0)
    complement = value - projected[:, None]
    close(expectation(complement * projected[:, None]), 0)
    close(expectation(complement * projected_l1[:, None]), 0)
    w = float(weight1 @ (projected ** 2))
    m = float(weight1 @ np.sum(projected_gradient ** 2, axis=-1))
    close(-weight1 @ (projected * projected_l1), m)

    # The Bessel derivative identity is independent of the projection integral.
    b1_prime = 1 - 3 * b1 / beta1 - b1 ** 2
    close(weight1 @ ((v1[:, 0] - b1) ** 2), b1_prime)
    close(w, 4 * b2 ** 2 * b1_prime)
    close(m, 3 * b2 ** 2 * b1 / beta1)
    r = 2 * m / w
    variance = float(expectation(value ** 2))
    assert 0 < w <= variance and m > 0 and r > 0
    close(m / r, w / 2)
    previous = math.inf
    for epsilon in (.5, .1, .02, .004):
        source_lf = epsilon * l1_value + (1 - epsilon) * l2_value
        close(-expectation(value * source_lf), energy1)
        close(source_lf @ weight2, epsilon * projected_l1)
        close(-weight1 @ (projected * (source_lf @ weight2)), epsilon * m)
        assert 0 < epsilon * r < previous
        previous = epsilon * r
    return np.array([w, m, r, variance, energy1])


def endpoint_neutral_checks():
    print("Endpoint-neutral two-profile source: beta1 beta2  R  weight floor W/2  fixed first moment")
    for beta1, beta2 in ((1.3, 2.1), (3.0, 3.0)):
        values = [endpoint_neutral_moments(beta1, beta2, n) for n in (24, 48, 96)]
        for value in values[:-1]:
            close(value, values[-1])
        w, m, r, variance, first = values[-1]
        print(f"{beta1:g} {beta2:g}  {r:.12g}  {w / 2:.12g}  {first:.12g}")
        print(f"  at epsilon=.004: interval (0, {.004 * r:.12g}], source variance {variance:.12g}, projected mass {w:.12g}")
    print("PASS actual two-profile product quadratures and projected gradients: fixed return state and first moment, with at least W/2 source spectral weight in (0, epsilon*R]; the spectral bound uses a reducing projection and positivity, not numerical diagonalization")


if __name__ == "__main__":
    derivative_checks()
    memory_checks()
    coincident_profile_checks()
    endpoint_neutral_checks()
    print("Finite source and profile diagnostics only. No physical mass gap, four-dimensional construction, or autonomous compressed semigroup is certified.")
