"""Finite receipts for opposed Cauchy response and the three-dimensional tests.

No files are written. Matrix and polynomial identities, independent quadratures,
and negative controls are tested here. Infinite-dimensional domains, locality,
and the physical return are proved or left open in the corresponding notes.
"""

from __future__ import annotations

import cmath
import math


def close(label, actual, expected, tol=1e-8):
    if abs(actual - expected) > tol:
        raise AssertionError(f"{label}: {actual!r} != {expected!r}")


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def hermitian(a, b):
    return sum(x.conjugate() * y for x, y in zip(a, b))


def kappa(q, p, rates):
    return [(math.sqrt(a) * x + 1j * y / math.sqrt(a)) / math.sqrt(2)
            for x, y, a in zip(q, p, rates)]


def mu(q, p, rates):
    return sum(a * x * x + y * y / a
               for x, y, a in zip(q, p, rates)) / 2


def flow(q, p, rates, t):
    q_out, p_out = [], []
    for x, y, a in zip(q, p, rates):
        c, s = math.cos(a * t), math.sin(a * t)
        q_out.append(c * x + s * y / a)
        p_out.append(-a * s * x + c * y)
    return q_out, p_out


def simpson(f, lo, hi, steps=2000):
    step = (hi - lo) / steps
    return step / 3 * sum(
        (1 if j in (0, steps) else 4 if j % 2 else 2) * f(lo + j * step)
        for j in range(steps + 1)
    )


def gauss(f):
    offset = math.sqrt(15) / 10
    return (5 * f(0.5 - offset) + 8 * f(0.5)
            + 5 * f(0.5 + offset)) / 18


def matmul(a, b):
    return [[sum(x * y for x, y in zip(row, column))
             for column in zip(*b)] for row in a]


def matadd(a, b, factor=1):
    return [[x + factor * y for x, y in zip(row, other)]
            for row, other in zip(a, b)]


def scale(a, factor):
    return [[factor * x for x in row] for row in a]


def kron(a, b):
    return [[a[i][j] * b[k][l]
             for j in range(len(a[0])) for l in range(len(b[0]))]
            for i in range(len(a)) for k in range(len(b))]


def matrix_close(label, a, b):
    for row, other in zip(a, b):
        for x, y in zip(row, other):
            close(label, x, y)


def main():
    rates = [0.3, 1.1, 2.0]
    q, p = [0.2, -0.3, 0.7], [0.5, 0.1, -0.2]
    vq, vp = [-0.1, 0.6, 0.2], [0.3, -0.4, 0.1]
    plus = [(x + y / a) / 2 for x, y, a in zip(q, p, rates)]
    minus = [(x - y / a) / 2 for x, y, a in zip(q, p, rates)]
    response = sum(a * (x * x + y * y)
                   for x, y, a in zip(plus, minus, rates))
    close("opposed graph response", response, mu(q, p, rates))
    pair = hermitian(kappa(q, p, rates), kappa(vq, vp, rates))
    close("Green pairing", 2 * pair.imag, dot(q, vp) - dot(p, vq))
    jq = [-y / a for y, a in zip(p, rates)]
    jp = [a * x for x, a in zip(q, rates)]
    for left, right in zip(kappa(jq, jp, rates), kappa(q, p, rates)):
        close("selected complex structure", left, 1j * right)
    t = 0.47
    tq, tp = flow(q, p, rates, t)
    for left, right, a in zip(kappa(tq, tp, rates), kappa(q, p, rates), rates):
        close("clock intertwining", left, cmath.exp(-1j * a * t) * right)
    close("clock preserves response", mu(tq, tp, rates), response)
    print("PASS: opposed graphs, Green form, complex structure and clock")

    def q_path(t):
        return [x + 0.2 * y * t + 0.1 * t * t
                for x, y in zip(q, p)]

    def dq_path(t):
        return [0.2 * y + 0.2 * t for y in p]

    def p_path(t):
        return [y + 0.3 * x * t for x, y in zip(q, p)]

    def dp_path(t):
        return [0.3 * x for x in q]

    def variation(values, t):
        return [x * t * (1 - t) for x in values]

    def dvariation(values, t):
        return [x * (1 - 2 * t) for x in values]

    def canonical(epsilon):
        def integrand(t):
            qt = [x + epsilon * dx for x, dx
                  in zip(q_path(t), variation(vq, t))]
            pt = [x + epsilon * dx for x, dx
                  in zip(p_path(t), variation(vp, t))]
            dqt = [x + epsilon * dx for x, dx
                   in zip(dq_path(t), dvariation(vq, t))]
            return dot(pt, dqt) - sum(y * y + a * a * x * x
                                     for x, y, a in zip(qt, pt, rates)) / 2
        return gauss(integrand)

    def first_variation(t):
        q_residue = [d + a * a * x
                     for d, a, x in zip(dp_path(t), rates, q_path(t))]
        p_residue = [d - y for d, y in zip(dq_path(t), p_path(t))]
        return (dot(variation(vp, t), p_residue)
                - dot(variation(vq, t), q_residue))

    epsilon = 1e-4
    close("canonical action variation",
          (canonical(epsilon) - canonical(-epsilon)) / (2 * epsilon),
          gauss(first_variation))
    endpoint = (dot(q_path(1), p_path(1)) - dot(q_path(0), p_path(0))) / 2

    def state_integrand(t):
        psi = kappa(q_path(t), p_path(t), rates)
        dpsi = kappa(dq_path(t), dp_path(t), rates)
        return (-hermitian(psi, dpsi).imag
                - sum(a * abs(z) ** 2 for a, z in zip(rates, psi)))

    close("state to canonical endpoint term",
          gauss(state_integrand) + endpoint, canonical(0))
    print("PASS: independent state-to-local-action and variation identities")

    length = 1.3
    for wave_number in (0.2, 1.0, 3.0):
        denominator = math.sinh(length * wave_number)

        def bulk_density(tau):
            value = math.sinh((length - tau) * wave_number) / denominator
            normal = -wave_number * math.cosh((length - tau) * wave_number) / denominator
            return normal * normal + wave_number * wave_number * value * value

        boundary = wave_number / math.tanh(length * wave_number)
        close("slab bulk response", simpson(bulk_density, 0, length), boundary)
        if boundary < 1 / length:
            raise AssertionError("Slab edge lower bound failed")
        invariant = wave_number ** 2 / math.sinh(length * wave_number) ** 2
        close("slab joint invariant", boundary ** 2 - wave_number ** 2, invariant)
    if (20 / math.sinh(20)) ** 2 >= 1e-12:
        raise AssertionError("Cap invariant did not soften at large momentum")

    def cap_kernel(distance):
        def radial(k):
            if k == 0:
                return 0.0
            b = k * k / math.sinh(length * k) ** 2
            z = k * distance
            sinc = 1.0 if z == 0 else math.sin(z) / z
            return k * k * b * sinc / (2 * math.pi * math.pi)
        return simpson(radial, 0, 35 / length, 6000)

    close("nonlocal cap kernel at origin",
          cap_kernel(0), math.pi ** 2 / (60 * length ** 5))
    for separation in (0.05 * length, 0.1 * length):
        if cap_kernel(separation) <= 0:
            raise AssertionError("Cap kernel lost the nearby nonlocal witness")
    print("PASS: capped bulk response, clock edge and nonlocality witness")

    def angular_numeric(t, a):
        steps = 20000
        return 2 / steps * sum(
            1 - (t + a * u) / math.sqrt(t * t + a * a + 2 * t * a * u)
            for u in (-1 + (j + 0.5) * 2 / steps for j in range(steps))
        )

    for t, a in ((0.2, 1.0), (0.7, 1.0), (1.5, 1.0), (4.0, 1.7)):
        exact = 2 - 4 * t / (3 * a) if t < a else 2 * a * a / (3 * t * t)
        close("weighted angular integral", angular_numeric(t, a), exact, 2e-7)
    spin_rank, scale_value = 4, 1.7
    near = simpson(lambda t: 2 - 4 * t / (3 * scale_value), 0, scale_value)
    # The inverse-radius variable turns the infinite tail into a finite integral.
    far = simpson(lambda u: 2 * scale_value * scale_value / 3, 0, 1 / scale_value)
    close("weighted full mode integral",
          spin_rank / 4 * 2 * math.pi * (near + far),
          spin_rank * math.pi * scale_value)
    print("PASS: three-dimensional Green-weighted compression integral")

    identity = [[1, 0], [0, 1]]
    x = [[0, 1], [1, 0]]
    z = [[1, 0], [0, -1]]
    e = matmul(x, z)
    i4 = kron(identity, identity)
    zero = scale(i4, 0)
    clifford = [kron(x, identity), kron(z, x), kron(z, z)]
    masses = [kron(e, identity), kron(z, e)]
    for j, c in enumerate(clifford):
        for k, d in enumerate(clifford):
            matrix_close("Clifford relation",
                         matadd(matmul(c, d), matmul(d, c)),
                         scale(i4, 2 if j == k else 0))
        for m in masses:
            matrix_close("mass anticommutation",
                         matadd(matmul(c, m), matmul(m, c)), zero)
    a, b = 0.4, -0.7
    mass = matadd(scale(masses[0], a), scale(masses[1], b))
    matrix_close("mass-plane radius", matmul(mass, mass), scale(i4, -(a * a + b * b)))
    product = matmul(matmul(clifford[0], clifford[1]), clifford[2])
    angle = 0.37
    rotation = matadd(scale(i4, math.cos(angle)), scale(product, math.sin(angle)))
    inverse = matadd(scale(i4, math.cos(angle)), scale(product, -math.sin(angle)))
    rotated = matmul(matmul(rotation, masses[0]), inverse)
    target = matadd(scale(masses[0], math.cos(2 * angle)),
                    scale(masses[1], math.sin(2 * angle)))
    matrix_close("commutant rotates mass direction", rotated, target)
    print("PASS: Clifford mass plane and its unfixed direction")
    print("Scope: finite identities and quadratures; no interacting Yang-Mills construction certified")


if __name__ == "__main__":
    main()
