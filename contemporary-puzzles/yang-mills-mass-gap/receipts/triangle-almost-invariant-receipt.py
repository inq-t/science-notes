"""Finite checks for the almost-cusp-invariant C3 * C4 representation family."""

from cmath import exp, pi, sqrt
from math import cos, sin


def matmul(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def adjoint(a):
    return tuple(tuple(a[j][i].conjugate() for j in range(2)) for i in range(2))


def eye_error(a):
    return max(abs(a[i][j] - (1 if i == j else 0)) for i in range(2) for j in range(2))


def matrix_power(a, n):
    result = ((1 + 0j, 0j), (0j, 1 + 0j))
    for _ in range(n):
        result = matmul(result, a)
    return result


def min_singular_c_minus_one(theta):
    omega = exp(2j * pi / 3)
    a = ((1 + 0j, 0j), (0j, omega))
    r = ((cos(theta), -sin(theta)), (sin(theta), cos(theta)))
    d = ((1 + 0j, 0j), (0j, 1j))
    b = matmul(matmul(r, d), adjoint(r))
    c = adjoint(matmul(a, b))
    m = ((c[0][0] - 1, c[0][1]), (c[1][0], c[1][1] - 1))
    gram = matmul(adjoint(m), m)
    trace = (gram[0][0] + gram[1][1]).real
    determinant = (gram[0][0] * gram[1][1] - gram[0][1] * gram[1][0]).real
    discriminant = max(0.0, trace * trace - 4 * determinant)
    lambda_min = max(0.0, (trace - sqrt(discriminant).real) / 2)
    return eye_error(matrix_power(a, 3)), eye_error(matrix_power(b, 4)), sqrt(lambda_min).real


rows = []
for theta in (0.2, 0.1, 0.05, 0.02, 0.01):
    a3_error, b4_error, cusp_displacement = min_singular_c_minus_one(theta)
    assert a3_error < 1e-12
    assert b4_error < 1e-12
    rows.append((theta, cusp_displacement))

assert all(rows[i + 1][1] < rows[i][1] for i in range(len(rows) - 1))
assert rows[-1][1] < 0.02

print("C3_AND_C4_RELATIONS_PASSED")
for theta, displacement in rows:
    print(f"THETA={theta:.3f}; MIN_CUSP_DISPLACEMENT={displacement:.12f}")
print("ALMOST_CUSP_INVARIANT_LIMIT_CONFIRMED")
