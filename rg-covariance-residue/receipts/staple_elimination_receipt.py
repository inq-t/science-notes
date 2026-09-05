"""Finite conditional geometry checks; no full gauge or continuum gap claim."""

import itertools
import math

import numpy as np


RNG = np.random.default_rng(117)
INDEX = np.arange(1, 1025)
LATITUDE = np.cos(np.pi * INDEX / 1025)
HAAR_WEIGHT = 2 / 1025 * np.sin(np.pi * INDEX / 1025)**2


def sphere_moments(kappa):
    weights = HAAR_WEIGHT * np.exp(kappa * (LATITUDE - 1))
    total = weights.sum()
    weights /= total
    mean = weights @ LATITUDE
    second = weights @ (LATITUDE**2)
    return kappa + math.log(total), mean, second, weights


def response(a):
    radius = np.linalg.norm(a)
    logz, mean, second, _ = sphere_moments(radius)
    if radius < 1e-12:
        return logz, np.zeros(4), np.eye(4) / 4
    direction = a / radius
    projector = np.outer(direction, direction)
    covariance = (second - mean**2) * projector + (1 - second) / 3 * (np.eye(4) - projector)
    return logz, mean * direction, covariance


def qmul(a, b):
    return np.concatenate(((a[0] * b[0] - a[1:] @ b[1:],),
                           a[0] * b[1:] + b[0] * a[1:] - np.cross(a[1:], b[1:])))


def qexp(v, time):
    size = np.linalg.norm(v)
    if size == 0:
        return np.array((1.0, 0, 0, 0))
    return np.concatenate(((math.cos(time * size),), math.sin(time * size) * v / size))


def bessel_normalizer(kappa):
    term = total = 1.0
    for j in range(1, 1000):
        term *= (kappa * kappa / 4) / (j * (j + 1))
        total += term
        if term < total * 1e-16:
            return total
    raise AssertionError("Bessel series did not converge")


def sphere_checks():
    count = 0
    for kappa in (0.0, 0.1, 1, 5, 20, 100, 500):
        logz, mean, second, weights = sphere_moments(kappa)
        if kappa <= 100:
            assert abs(logz - math.log(bessel_normalizer(kappa))) < 2e-11
        if kappa:
            assert abs((1 - second) / 3 - mean / kappa) < 2e-11
            assert abs(second - mean**2 - (1 - mean**2 - 3 * mean / kappa)) < 2e-11
        x = LATITUDE
        for angular in range(4):
            p = []
            derivative = []
            for j in range(5):
                radial = (1 - x * x)**(angular / 2)
                pj = radial * x**j
                dp = np.zeros_like(x) if j == 0 else j * radial * x**(j - 1)
                if angular:
                    dp -= angular * x**(j + 1) * (1 - x * x)**(angular / 2 - 1)
                p.append(pj)
                derivative.append(dp)
            p = np.array(p)
            derivative = np.array(derivative)
            gram = (p * weights) @ p.T
            covariance = gram.copy()
            if angular == 0:
                averages = p @ weights
                covariance -= np.outer(averages, averages)
            energy = (derivative * (weights * (1 - x * x))) @ derivative.T
            energy += angular * (angular + 1) * (p * (weights / (1 - x * x))) @ p.T
            assert np.linalg.eigvalsh(energy - covariance).min() > -2e-10
            if angular == 0:
                bl_energy = (derivative * (weights * (1 - x*x)**2 / (1 + x*x))) @ derivative.T
                assert np.linalg.eigvalsh(bl_energy - covariance).min() > -2e-10
            count += 1
    return count


def staple_checks():
    count = 0
    for beta in (0.1, 1, 5, 25):
        for _ in range(6):
            staples = RNG.normal(size=(6, 4))
            staples /= np.linalg.norm(staples, axis=1, keepdims=True)
            left = RNG.normal(size=(6, 3))
            right = RNG.normal(size=(6, 3))
            a = beta * staples.sum(axis=0)
            da = np.zeros(4)
            dda = np.zeros(4)
            for u, x, y in zip(staples, left, right):
                qx, qy = np.r_[0.0, x], np.r_[0.0, y]
                da += beta * (qmul(qx, u) + qmul(u, qy))
                dda += beta * (-(x @ x + y @ y) * u + 2 * qmul(qmul(qx, u), qy))
            _, mean, covariance = response(a)
            exact = -da @ covariance @ da - mean @ dda
            step = 0.0005
            values = []
            for multiple in (-2, -1, 0, 1, 2):
                shifted = np.array([qmul(qmul(qexp(x, multiple * step), u),
                                         qexp(y, multiple * step))
                                    for u, x, y in zip(staples, left, right)])
                values.append(-response(beta * shifted.sum(axis=0))[0])
            fd = (-values[0] + 16*values[1] - 30*values[2] + 16*values[3] - values[4]) / (12*step**2)
            assert abs(fd - exact) < 4e-5
            # Common endpoint rotation leaves the integrated action unchanged.
            generator = np.r_[0.0, RNG.normal(size=3)]
            gauge_da = qmul(generator, a)
            gauge_dda = -(generator @ generator) * a
            assert abs(gauge_da @ covariance @ gauge_da + mean @ gauge_dda) < 2e-9
            count += 1
        for sign in (-1, 1):
            a = beta * np.array((1 + sign, 0, 0, 0), dtype=float)
            da = beta * np.array((0, sign, 0, 0), dtype=float)
            dda = beta * np.array((-sign, 0, 0, 0), dtype=float)
            _, mean, covariance = response(a)
            curvature = -da @ covariance @ da - mean @ dda
            expected = -beta**2 / 4 if sign == -1 else beta * sphere_moments(2 * beta)[1] / 2
            assert abs(curvature - expected) < 2e-10
            count += 1
    return count


def checkerboard_checks():
    dimension, size, orientation = 4, 4, 1
    sites = tuple(itertools.product(range(size), repeat=dimension))

    def step(site, axis):
        value = list(site)
        value[axis] = (value[axis] + 1) % size
        return tuple(value)

    def selected(site):
        return sum(site[j] for j in range(dimension) if j != orientation) % 2 == 0

    def selected_column(site):
        return sum(site[j] for j in range(1, dimension) if j != orientation) % 2 == 0

    count = 0
    temporal_pairs = 0
    for site in sites:
        for i in range(dimension):
            for j in range(i + 1, dimension):
                edges = ((site, i), (step(site, i), j), (step(site, j), i), (site, j))
                assert sum(axis == orientation and selected(base) for base, axis in edges) <= 1
                hits = [(base, axis) for base, axis in edges
                        if axis == orientation and selected_column(base)]
                if i != 0:
                    assert len(hits) <= 1
                if len(hits) == 2:
                    assert i == 0
                    assert hits[0][0][1:] == hits[1][0][1:]
                    temporal_pairs += 1
                count += 1
        site_reflected = ((-site[0]) % size,) + site[1:]
        link_reflected = ((1 - site[0]) % size,) + site[1:]
        assert selected(site_reflected) == selected(site)
        assert selected(link_reflected) != selected(site)
        assert selected_column(link_reflected) == selected_column(site)
    assert temporal_pairs > 0
    return count


def su3_checks():
    n = 384
    angle = 2 * np.pi * np.arange(n) / n
    alpha, beta = np.meshgrid(angle, angle, indexing="ij")
    angles = np.stack((alpha, beta, -alpha - beta))
    eigenvalues = np.exp(1j * angles)
    trace = eigenvalues.sum(axis=0)
    potential = trace.real
    assert potential.min() >= -1.5 - 1e-12
    z = np.exp(2j * np.pi / 3)
    assert np.allclose(3 * z * np.eye(3) + 3 * z.conjugate() * np.eye(3), -3 * np.eye(3))
    positive_source = (4 + z + z.conjugate()) * np.eye(3)
    negative_source = (3*z + 3*z.conjugate()) * np.eye(3)
    assert np.allclose(np.linalg.svd(positive_source, compute_uv=False),
                       np.linalg.svd(negative_source, compute_uv=False))
    assert np.allclose(np.linalg.det(positive_source), 27)
    assert np.allclose(np.linalg.det(negative_source), -27)
    assert abs((3*z).real + 1.5) < 1e-12
    weyl = np.ones_like(potential)
    for i in range(3):
        for j in range(i):
            weyl *= np.abs(eigenvalues[i] - eigenvalues[j])**2
    # C2 cutoff is sufficient for the numerical H1 Rayleigh test.
    coordinate = trace.imag
    clipped = np.clip(coordinate, -1, 1)
    test = (15*clipped - 10*clipped**3 + 3*clipped**5) / 8
    dh = 15 / 8 * (1 - clipped**2)**2
    cosines = np.cos(angles)
    mean_cosine = cosines.mean(axis=0)
    # Unit normalization g(X,Y)=-ReTr(XY)/3.
    gradient_squared = dh**2 * 3 * ((cosines - mean_cosine)**2).sum(axis=0)
    values = []
    for coupling in (4, 8, 16, 32, 64):
        weights = weyl * np.exp(-coupling * (potential + 1.5))
        weights /= weights.sum()
        mean = (weights * test).sum()
        variance = (weights * test**2).sum() - mean**2
        quotient = (weights * gradient_squared).sum() / variance
        assert abs(mean) < 1e-10
        assert variance > 0.1
        values.append(quotient)
    assert all(a > b for a, b in zip(values, values[1:]))
    assert values[-1] < 1e-5
    return values


def bad_context_checks():
    # Product contexts x hidden signs: rare does not mean operator-small.
    hidden_mean = np.full((2, 2), 0.5)
    projection = np.kron(np.eye(2), hidden_mean)
    bad_indicator = np.diag((1.0, 1.0, 0.0, 0.0))
    bad_response = bad_indicator @ (np.eye(4) - projection)
    assert np.allclose(bad_response @ bad_response, bad_response)
    assert np.allclose(bad_response.T, bad_response)
    assert np.isclose(np.linalg.norm(bad_response, ord=2), 1)
    for probability in (1e-2, 1e-4, 1e-8):
        weights = np.repeat((probability, 1-probability), 2) / 2
        test = np.array((1.0, -1.0, 0.0, 0.0)) / np.sqrt(probability)
        assert np.isclose(weights @ test, 0)
        assert np.isclose(weights @ test**2, 1)
        assert np.isclose(weights @ (bad_response @ test)**2, 1)
    return 3


if __name__ == "__main__":
    print("PASS tilted-sphere polynomial/angular form blocks:", sphere_checks())
    print("PASS exact staple Hessians and gauge cancellation:", staple_checks())
    print("PASS independent-link and whole-column plaquette checks:", checkerboard_checks())
    print("PASS SU(3) conditional trial Rayleigh quotients:", su3_checks())
    print("PASS rare-context norm-one projection checks:", bad_context_checks())
    print("Scope: finite conditional geometry, not a complete physical or continuum gap.")
