"""Exact arithmetic receipts for the A2 Weyl-radial operator note.

The checks establish root, half-sum, dimension, and Casimir arithmetic only.
They do not identify a one-link class-function model with continuum Yang--Mills
or construct a bridge from complex S6 geometry.
"""

from fractions import Fraction


GRAM = (
    (Fraction(2, 3), Fraction(1, 3)),
    (Fraction(1, 3), Fraction(2, 3)),
)


def inner(left: tuple[int, int], right: tuple[int, int]) -> Fraction:
    return sum(
        Fraction(left[i]) * GRAM[i][j] * Fraction(right[j])
        for i in range(2)
        for j in range(2)
    )


def add(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    return left[0] + right[0], left[1] + right[1]


def casimir(p: int, q: int) -> Fraction:
    highest_weight = (p, q)
    return inner(highest_weight, (p + 2, q + 2)) / 2


def dimension(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


positive_roots = ((2, -1), (-1, 2), (1, 1))
rho = (
    sum(root[0] for root in positive_roots) // 2,
    sum(root[1] for root in positive_roots) // 2,
)

assert all(inner(root, root) == 2 for root in positive_roots)
assert rho == (1, 1)
assert inner(rho, rho) == 2

assert dimension(0, 0) == 1
assert all(
    dimension(p, q) > 1
    for p in range(8)
    for q in range(8)
    if (p, q) != (0, 0)
)

assert casimir(1, 0) == Fraction(4, 3)
assert casimir(0, 1) == Fraction(4, 3)
assert casimir(1, 1) == 3

for p in range(8):
    for q in range(8):
        lam = (p, q)
        radial_shift = inner(add(lam, rho), add(lam, rho)) - inner(rho, rho)
        assert radial_shift == 2 * casimir(p, q)

nonzero = [
    (casimir(p, q), p, q)
    for p in range(8)
    for q in range(8)
    if (p, q) != (0, 0)
]
first_casimir = min(value for value, _, _ in nonzero)
first_weights = sorted((p, q) for value, p, q in nonzero if value == first_casimir)

vandermonde_degree = len(positive_roots)
weyl_density_degree = 2 * vandermonde_degree
assert vandermonde_degree == 3
assert weyl_density_degree == 6
assert first_casimir == Fraction(4, 3)
assert first_weights == [(0, 1), (1, 0)]

print("A2 positive-root lengths squared:", [inner(root, root) for root in positive_roots])
print("rho in fundamental-weight coordinates:", rho)
print("rho squared:", inner(rho, rho))
print("Weyl amplitude degree:", vandermonde_degree)
print("Weyl density degree:", weyl_density_degree)
print(
    "root-length-two radial shifts (fundamental, adjoint):",
    2 * casimir(1, 0),
    2 * casimir(1, 1),
)
print("C2 fundamental:", casimir(1, 0))
print("C2 adjoint:", casimir(1, 1))
print("first nonzero class Casimir:", first_casimir, "at", first_weights)
print("nontrivial one-dimensional SU(3) representations in search:", 0)
print("all exact A2 radial receipts passed")
