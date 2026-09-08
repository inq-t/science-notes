"""Numerical checks for the finite descent-loss and quotient-metric identities."""

from __future__ import annotations

import numpy as np


def close(left: float | np.ndarray, right: float | np.ndarray) -> None:
    assert np.allclose(left, right, rtol=1e-12, atol=1e-12), (left, right)


g_v = np.diag([2.0, 5.0, 7.0])
a = np.array([[0.30, 0.10, 0.00], [0.00, 0.20, 0.25]])
g_w = np.diag([1.0, 1.5])

contraction_defect = g_v - a.T @ g_w @ a
assert np.linalg.eigvalsh(contraction_defect).min() > 0.0

quotient_matrix = np.linalg.inv(a @ np.linalg.inv(g_v) @ a.T)
transgression_matrix = quotient_matrix - g_w
assert np.linalg.eigvalsh(transgression_matrix).min() > 0.0

y = np.array([0.17, -0.11])
minimal_lift = (
    np.linalg.inv(g_v)
    @ a.T
    @ quotient_matrix
    @ y
)
close(a @ minimal_lift, y)
close(minimal_lift @ g_v @ minimal_lift, y @ quotient_matrix @ y)
close(
    minimal_lift @ contraction_defect @ minimal_lift,
    y @ transgression_matrix @ y,
)

# The carrier split adds an arbitrary vertical component without changing the
# output.  Its extra defect is exactly its input norm.
_, _, v_h = np.linalg.svd(a)
vertical = 0.13 * v_h[-1]
close(a @ vertical, np.zeros(2))
x = minimal_lift + vertical
close(
    x @ contraction_defect @ x,
    y @ transgression_matrix @ y + vertical @ g_v @ vertical,
)

# A second surjective contraction checks the general infimal composition law.
b = np.array([[0.40, -0.20]])
g_z = np.array([[1.0]])
assert np.linalg.eigvalsh(g_w - b.T @ g_z @ b).min() > 0.0
composite = b @ a
composite_quotient = np.linalg.inv(composite @ np.linalg.inv(g_v) @ composite.T)
z = np.array([0.07])
min_intermediate = (
    np.linalg.inv(quotient_matrix)
    @ b.T
    @ composite_quotient
    @ z
)
close(b @ min_intermediate, z)
close(
    z @ composite_quotient @ z,
    min_intermediate @ quotient_matrix @ min_intermediate,
)
close(
    z @ (composite_quotient - g_z) @ z,
    min_intermediate @ transgression_matrix @ min_intermediate
    + min_intermediate @ g_w @ min_intermediate
    - z @ g_z @ z,
)

lambda_1 = 0.73
lambda_2 = 0.61
tangent = 0.09
output_tangent = 0.04


def loss(lam: float, value: float) -> float:
    return 4.0 * (1.0 - lam**2) * value**2


def transgression(lam: float, value: float) -> float:
    return 4.0 * (lam**-2 - 1.0) * value**2


close(
    loss(lambda_2 * lambda_1, tangent),
    loss(lambda_1, tangent) + loss(lambda_2, lambda_1 * tangent),
)
close(
    transgression(lambda_2 * lambda_1, output_tangent),
    transgression(lambda_1, output_tangent / lambda_2)
    + loss(lambda_2, output_tangent / lambda_2),
)

print("descent-loss cocycle: passed")
print("vertical carrier split: passed")
print("minimal-lift quotient metric: passed")
print("general infimal composition: passed")
print("binary transgression composition: passed")
