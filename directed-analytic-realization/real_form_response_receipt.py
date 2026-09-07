"""Finite real-form and directed-response checks; standard library, stdout only.

Mathematical owners:
  algebra/wick-real-forms-and-positive-preparation.md
  algebra/directed-response-and-lorentzian-signature.md

Wick matrices have small Gaussian-integer entries, represented exactly by
Python complex arithmetic for these operations. Metric calculations use
Fractions throughout. Only exponential-kernel checks use toleranced floats.
No claim about a continuum theory, a physical time calibration, or a gap
follows from this receipt.
"""

from fractions import Fraction as F
from math import exp, isclose, sqrt


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def scale(c, a):
    return [[c * value for value in row] for row in a]


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def mm(a, b):
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(ar, bc)) for bc in bt] for ar in a]


def mv(a, v):
    return [sum(x * y for x, y in zip(row, v)) for row in a]


def dot(u, v):
    return sum(x * y for x, y in zip(u, v))


def outer(u, v):
    return [[x * y for y in v] for x in u]


def inverse(a):
    """Exact Gauss-Jordan inverse for the nonsingular rational test matrices."""
    n = len(a)
    rows = [
        [F(value) for value in row] + [F(i == j) for j in range(n)]
        for i, row in enumerate(a)
    ]
    for j in range(n):
        k = next(k for k in range(j, n) if rows[k][j])
        rows[j], rows[k] = rows[k], rows[j]
        pivot = rows[j][j]
        rows[j] = [value / pivot for value in rows[j]]
        for i in range(n):
            if i != j:
                factor = rows[i][j]
                rows[i] = [
                    value - factor * reference
                    for value, reference in zip(rows[i], rows[j])
                ]
    return [row[n:] for row in rows]


def det3(a):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def block(a, b, c, d):
    return [ar + br for ar, br in zip(a, b)] + [
        cr + dr for cr, dr in zip(c, d)
    ]


def close(a, b):
    assert isclose(a, b, rel_tol=1e-11, abs_tol=1e-12), (a, b)


def check_wick():
    a = [[2, 1], [1, 2]]
    a2 = mm(a, a)
    identity = eye(2)
    zero = [[0, 0], [0, 0]]
    be = block(zero, identity, a2, zero)
    bl = block(zero, identity, scale(-1, a2), zero)
    c = block(identity, zero, zero, scale(-1j, identity))
    ci = block(identity, zero, zero, scale(1j, identity))
    sigma = block(zero, identity, scale(-1, identity), zero)
    assert mm(ci, c) == eye(4)
    assert mm(mm(ci, be), c) == scale(-1j, bl)
    assert mm(mm(transpose(c), sigma), c) == scale(-1j, sigma)
    print("PASS exact Wick generator sign and complex symplectic scaling")

    q = [1, -2]
    aq = mv(a, q)
    pe = [-value for value in aq]
    pl = [-1j * value for value in aq]
    assert mv(c, q + pl) == q + pe
    assert mv(ci, q + pe) == q + pl
    evolved_q = pl
    expected = evolved_q + [-1j * value for value in mv(a, evolved_q)]
    assert mv(bl, q + pl) == expected

    # tau = i t, q_tau = -i q_dot, and d tau = i dt.
    # These are analytic bilinear squares, not Hermitian absolute squares.
    velocity = [2, 1]
    potential = dot(q, mv(a2, q)) / 2
    lorentz_density = dot(velocity, velocity) / 2 - potential
    euclidean_velocity = [-1j * value for value in velocity]
    euclidean_density = (
        dot(euclidean_velocity, euclidean_velocity) / 2 + potential
    )
    assert 1j * euclidean_density == -1j * lorentz_density
    print("PASS stable Euclidean graph gives positive frequency and action sign")


def reflection_data(h, theta, beta=F(2)):
    sharp = mv(inverse(h), theta)
    norm2 = dot(theta, sharp)
    assert norm2 > 0
    projection = scale(1 / norm2, outer(sharp, theta))
    reflection = add(eye(len(h)), scale(-beta, projection))
    metric = add(h, scale(-beta / norm2, outer(theta, theta)))
    assert metric == mm(h, reflection)
    return sharp, norm2, projection, reflection, metric


def check_record_reflection():
    h = [[F(2), F(1), F(0)], [F(1), F(2), F(0)], [F(0), F(0), F(3)]]
    theta = [F(1), F(0), F(1)]
    sharp, norm2, projection, reflection, metric = reflection_data(h, theta)
    assert h[0][0] > 0
    assert h[0][0] * h[1][1] - h[0][1] * h[1][0] > 0
    assert det3(h) == 9
    assert norm2 == 1  # The chosen sharp is already h-unit.
    assert mm(projection, projection) == projection
    assert sum(projection[i][i] for i in range(3)) == 1
    assert mm(transpose(reflection), h) == mm(h, reflection)
    assert mm(reflection, reflection) == eye(3)

    w1, w2 = [F(0), F(1), F(0)], [F(1), F(0), F(-1)]
    assert dot(theta, w1) == dot(theta, w2) == 0
    adapted = transpose([sharp, w1, w2])
    adapted_metric = mm(mm(transpose(adapted), metric), adapted)
    assert adapted_metric == [[-1, 0, 0], [0, 2, 1], [0, 1, 5]]
    # The spatial block has positive first pivot and determinant 9.
    # Together with the -1 block this proves signature (2 positive, 1 negative).
    assert det3(metric) == -9
    print("PASS rational non-diagonal response gives one negative record direction")

    for factor in (F(3, 2), F(7, 5), F(4)):
        changed_theta = [factor * value for value in theta]
        _, _, changed_projection, changed_reflection, changed_metric = (
            reflection_data(h, changed_theta)
        )
        assert changed_projection == projection
        assert changed_reflection == reflection
        assert changed_metric == metric
        assert dot(changed_theta, sharp) > 0
    _, _, _, _, reversed_metric = reflection_data(h, [-v for v in theta])
    assert reversed_metric == metric
    assert dot([-v for v in theta], sharp) < 0
    conformal = F(5, 2)
    _, _, scaled_projection, scaled_reflection, scaled_metric = (
        reflection_data(scale(conformal, h), theta)
    )
    assert scaled_projection == projection
    assert scaled_reflection == reflection
    assert scaled_metric == scale(conformal, metric)
    print("PASS record reparametrization and positive conformal covariance")

    # Pi^2 = Pi makes the full polynomial identity
    # (I-beta Pi)^2-I = beta(beta-2)Pi exact, not a numerical fit.
    for beta in (F(0), F(1, 2), F(1), F(3, 2), F(2), F(3)):
        _, _, _, rb, _ = reflection_data(h, theta, beta)
        assert add(mm(rb, rb), scale(-1, eye(3))) == scale(
            beta * (beta - 2), projection
        )
        if beta > 1:
            assert (mm(rb, rb) == eye(3)) == (beta == 2)
    _, _, _, r3, g3 = reflection_data(h, theta, F(3))
    assert mm(mm(transpose(adapted), g3), adapted) == [
        [-2, 0, 0], [0, 2, 1], [0, 1, 5]
    ]
    assert mm(r3, r3) != eye(3)
    assert det3(g3) == -18
    print("PASS beta=3 stays Lorentzian but only beta=2 is a reflection")

    forward_spacelike = [a + 2 * b for a, b in zip(sharp, w1)]
    assert dot(theta, forward_spacelike) == 1
    assert dot(forward_spacelike, mv(metric, forward_spacelike)) == 7
    forward_timelike = [a + b / 2 for a, b in zip(sharp, w1)]
    assert dot(theta, forward_timelike) == 1
    assert dot(forward_timelike, mv(metric, forward_timelike)) == F(-1, 2)
    print("PASS increasing record alone does not imply the causal cone bound")


def check_reflected_kernel():
    rates = (1.0, 2.0, 3.0)
    times = (0.0, 0.2, 0.7, 1.1)
    features = [
        [exp(-a * t) / sqrt(2 * a) for t in times] for a in rates
    ]
    gram = mm(transpose(features), features)
    kernel = [
        [sum(exp(-a * (s + t)) / (2 * a) for a in rates) for t in times]
        for s in times
    ]
    for row_a, row_b in zip(gram, kernel):
        for a, b in zip(row_a, row_b):
            close(a, b)
    for coefficients in (
        (1.0, -2.0, 3.0, -0.5),
        (0.0, 1.0, -1.0, 0.0),
        (1.0, 1.0, 1.0, 1.0),
    ):
        direct = dot(coefficients, mv(kernel, coefficients))
        prepared = mv(features, coefficients)
        squared_norm = dot(prepared, prepared)
        close(direct, squared_norm)
        assert direct >= -1e-12

    # Independent vector-valued probe of diag(exp(-(s+t)A)/(2A)).
    probe = ((1.0, -2.0, 0.5), (-0.7, 1.2, 2.0), (2.0, 0.1, -1.0), (0.3, -1.0, 0.4))
    direct = sum(
        probe[i][k] * probe[j][k] * exp(-a * (s + t)) / (2 * a)
        for i, s in enumerate(times)
        for j, t in enumerate(times)
        for k, a in enumerate(rates)
    )
    prepared = [
        sum(exp(-a * t) * probe[i][k] for i, t in enumerate(times))
        / sqrt(2 * a)
        for k, a in enumerate(rates)
    ]
    close(direct, dot(prepared, prepared))
    assert direct > 0
    print("PASS finite reflection-positive kernel equals its feature Gram form")

    s, t = 0.3, 0.8
    vector = (1.0, -2.0, 3.0)
    factors = [exp(-a * t) for a in rates]
    assert all(0 < value < 1 for value in factors)
    smoothed = [factor * value for factor, value in zip(factors, vector)]
    assert dot(smoothed, smoothed) < dot(vector, vector)
    for a, before, after in zip(rates, vector, smoothed):
        close(exp(a * t) * after, before)
        close(exp(-a * s) * exp(-a * t), exp(-a * (s + t)))
    assert factors[0] * factors[1] * factors[2] > 0
    print("PASS finite positive attenuation is contractive but not information erasure")


def main():
    check_wick()
    check_record_reflection()
    check_reflected_kernel()
    print("Finite algebra only; no continuum construction, time calibration or mass gap certified.")


if __name__ == "__main__":
    main()
