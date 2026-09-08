"""Exact Gaussian checks for state-preserving overlap balancing.

Uses rational precision matrices and Gaussian moment integration, not
sampled paths. It checks a genuinely noncommuting covariance/cometric,
normalization constants, a common-clock sewing example, an anisotropic
failure of family closure, and the first nine Hermite responses.
The canonical note supplies the classification and infinite-carrier proof.
"""

from fractions import Fraction as F
from math import comb


def identity(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def multiply(a, b):
    return [[sum((a[i][j] * b[j][k] for j in range(len(b))), F(0))
             for k in range(len(b[0]))] for i in range(len(a))]


def add(a, b):
    return [[x + y for x, y in zip(row, other)] for row, other in zip(a, b)]


def scale(c, a):
    return [[c * value for value in row] for row in a]


def inverse(a):
    n = len(a)
    rows = [[F(value) for value in row] + unit
            for row, unit in zip(a, identity(n))]
    for j in range(n):
        pivot = next(i for i in range(j, n) if rows[i][j])
        rows[j], rows[pivot] = rows[pivot], rows[j]
        normalizer = rows[j][j]
        rows[j] = [value / normalizer for value in rows[j]]
        for i in range(n):
            if i != j:
                coefficient = rows[i][j]
                rows[i] = [x - coefficient * y for x, y in zip(rows[i], rows[j])]
    assert [row[:n] for row in rows] == identity(n)
    return [row[n:] for row in rows]


def determinant(a):
    rows = [[F(value) for value in row] for row in a]
    result = F(1)
    for j in range(len(rows)):
        pivot = next(i for i in range(j, len(rows)) if rows[i][j])
        if pivot != j:
            rows[j], rows[pivot] = rows[pivot], rows[j]
            result *= -1
        value = rows[j][j]
        result *= value
        for i in range(j + 1, len(rows)):
            coefficient = rows[i][j] / value
            rows[i] = [x - coefficient * y for x, y in zip(rows[i], rows[j])]
    return result


def congruence(a, b):
    return multiply(multiply(a, b), transpose(a))


def joint_precision(source_precision, increment_precision):
    """Read the quadratic form of exp(-zUz/2-z'Uz'/2-(z-z')D^-1(z-z')/2)."""
    diagonal = add(source_precision, increment_precision)
    negative = scale(F(-1), increment_precision)
    return [left + right for left, right in zip(diagonal, negative)] + [
        left + right for left, right in zip(negative, diagonal)
    ]


def top_block(a, n):
    return [row[:n] for row in a[:n]]


def noncommuting_matrix_checks():
    # z = A w, C = A A^T, Sigma = A diag(tau) A^T. This whitening
    # factor need not be the symmetric square root of C.
    a = [[F(1), F(1)], [F(0), F(2)]]
    tau = [F(4), F(9, 4)]
    r = [F(1, 2), F(1, 3)]
    epsilon = F(3)
    c = congruence(a, identity(2))
    sigma = congruence(a, [[tau[0], F(0)], [F(0), tau[1]]])
    assert multiply(c, sigma) != multiply(sigma, c)
    d = scale(2 * epsilon, c)
    si, di = inverse(sigma), inverse(d)

    # Raw row normalization: the marginal of the full four-dimensional
    # Gaussian precision matrix independently gives the stationary law.
    raw_joint_covariance = inverse(joint_precision(si, di))
    stationary = inverse(add(si, inverse(add(sigma, d))))
    assert top_block(raw_joint_covariance, 2) == stationary
    assert stationary != sigma
    raw_v = inverse(add(si, di))
    raw_m = multiply(raw_v, di)
    assert raw_m == multiply(sigma, inverse(add(sigma, d)))
    assert add(congruence(raw_m, stationary), raw_v) == stationary

    for t, mean in zip(tau, r):
        assert 1 - mean * mean == 2 * epsilon * mean / t
    source = congruence(a, [[tau[0] * (1 + r[0]), F(0)],
                            [F(0), tau[1] * (1 + r[1])]])
    u = inverse(source)
    endpoint_precision = add(si, scale(F(-1), u))
    assert endpoint_precision == inverse(add(source, d))
    conditional_v = inverse(add(u, di))
    conditional_m = multiply(conditional_v, di)
    expected_m = multiply(multiply(a, [[r[0], F(0)], [F(0), r[1]]]), inverse(a))
    expected_v = congruence(a, [[tau[0] * (1 - r[0] ** 2), F(0)],
                                [F(0), tau[1] * (1 - r[1] ** 2)]])
    assert conditional_m == expected_m and conditional_v == expected_v
    assert add(congruence(conditional_m, sigma), conditional_v) == sigma
    assert multiply(conditional_m, sigma) == multiply(sigma, transpose(conditional_m))

    # Directly invert the balanced joint precision rather than presuming its
    # marginal. This also checks every cross-covariance entry.
    balanced_precision = joint_precision(u, di)
    balanced_covariance = inverse(balanced_precision)
    assert top_block(balanced_covariance, 2) == sigma
    assert [row[2:] for row in balanced_covariance[:2]] == multiply(sigma, transpose(conditional_m))
    # The square of the scalar row-normalization condition and the square
    # of the whole Gaussian integral must both equal one. Here A^4 is rational.
    endpoint_scalar_fourth = F(1)
    for mean in r:
        endpoint_scalar_fourth /= 1 - mean * mean
    assert endpoint_scalar_fourth == determinant(sigma) * determinant(add(u, di))
    assert endpoint_scalar_fourth == determinant(sigma) ** 2 * determinant(balanced_precision)
    assert endpoint_scalar_fourth == F(3, 2)

    # Two copies at the SAME width have multipliers r_j^2. The widths
    # required to represent their composite disagree across directions.
    composite_widths = [t * (1 - mean ** 4) / (2 * mean * mean)
                        for t, mean in zip(tau, r)]
    assert composite_widths == [F(15, 2), F(10)]
    assert composite_widths[0] != composite_widths[1]
    print('EXACT noncommuting Sigma,C: raw state changes; balanced full marginal, '
          'cross covariance, detailed balance and Gaussian constants agree')
    print('EXACT anisotropic sewing obstruction: composing width 3 with itself '
          'requires incompatible widths 15/2 and 10')


def scalar_sewing_checks():
    # C=Sigma, so epsilon=(1-r^2)/(2r) and sqrt(1+epsilon^2)=(1+r^2)/(2r).
    r, s = F(1, 2), F(2, 3)
    width = lambda mean: (1 - mean * mean) / (2 * mean)
    root = lambda mean: (1 + mean * mean) / (2 * mean)
    assert width(r) == F(3, 4) and width(s) == F(5, 12)
    composed = width(r) * root(s) + width(s) * root(r)
    assert composed == width(r * s) == F(4, 3)
    # The variance follows by integrating two independent Gaussian steps,
    # not by assuming the composed kernel has the asserted form.
    assert s * s * (1 - r * r) + (1 - s * s) == 1 - (r * s) ** 2
    assert r * r * (1 - s * s) + (1 - r * r) == 1 - (r * s) ** 2
    for epsilon in (F(1, 2), F(1, 8), F(1, 32)):
        raw_stationary = (1 + 2 * epsilon) / (2 + 2 * epsilon)
        half_source_stationary = (2 + 2 * epsilon) / (2 + epsilon)
        assert raw_stationary - F(1, 2) == epsilon / (2 + 2 * epsilon)
        assert half_source_stationary - 1 == epsilon / (2 + epsilon)
    print('EXACT scalar-clock sewing: widths 3/4 and 5/12 compose to 4/3; '
          'raw and half-density finite-width state shifts checked')


def hermite_polynomials(max_degree):
    polynomials = [[F(1)], [F(0), F(1)]]
    for n in range(1, max_degree):
        following = [F(0)] + polynomials[n]
        for j, coefficient in enumerate(polynomials[n - 1]):
            following[j] -= n * coefficient
        polynomials.append(following)
    return polynomials[:max_degree + 1]


def conditional_polynomial(polynomial, mean, variance):
    # E[(mean*x + sqrt(variance)*xi)^n], using standard Gaussian moments.
    result = [F(0)] * len(polynomial)
    for n, coefficient in enumerate(polynomial):
        even_moment = 1
        for j in range(n // 2 + 1):
            if j:
                even_moment *= 2 * j - 1
            result[n - 2 * j] += (
                coefficient * comb(n, 2 * j) * mean ** (n - 2 * j)
                * variance ** j * even_moment
            )
    return result


def hermite_response_checks():
    polynomials = hermite_polynomials(8)
    checks = 0
    for mean in (F(1, 2), F(2, 3), F(1, 3)):
        for n, polynomial in enumerate(polynomials):
            actual = conditional_polynomial(polynomial, mean, 1 - mean * mean)
            assert actual == [mean ** n * coefficient for coefficient in polynomial]
            assert mean ** n > 0
            checks += 1
    print(f'EXACT {checks} Hermite responses from conditional Gaussian moments, '
          'including positive multipliers through degree eight')


if __name__ == '__main__':
    noncommuting_matrix_checks()
    scalar_sewing_checks()
    hermite_response_checks()
    print('PASS exact finite Gaussian checks. Infinite-carrier completeness, '
          'all-width classification and physical scope are stated in the canonical note.')
