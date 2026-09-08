"""Finite-dimensional receipts for the carrier-first reversal.

The checks establish semigroup/form reconstruction, a Poincare quotient,
and the dependence of Markov geometry on a chosen positive cone. They make
no claim about continuum Yang--Mills.
"""

from fractions import Fraction
from math import exp, isclose, log


def mat_vec(matrix, vector):
    return [
        sum(matrix[i][j] * vector[j] for j in range(len(vector)))
        for i in range(len(matrix))
    ]


def uniform_inner(left, right):
    return sum(x * y for x, y in zip(left, right, strict=True)) / len(left)


def trace(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))


def trace_square(matrix):
    size = len(matrix)
    return sum(
        matrix[i][j] * matrix[j][i]
        for i in range(size)
        for j in range(size)
    )


def has_markov_off_diagonals(matrix):
    return all(
        matrix[i][j] <= 0
        for i in range(len(matrix))
        for j in range(len(matrix))
        if i != j
    )


# Positive two-state generator L=2P_perp with spectrum {0, 2}.
two_state_l = (
    (Fraction(1), Fraction(-1)),
    (Fraction(-1), Fraction(1)),
)
vacuum = (Fraction(1), Fraction(1))
mean_zero = (Fraction(1), Fraction(-1))

assert mat_vec(two_state_l, vacuum) == [0, 0]
assert mat_vec(two_state_l, mean_zero) == [2, -2]

norm_squared = uniform_inner(mean_zero, mean_zero)
energy = uniform_inner(mean_zero, mat_vec(two_state_l, mean_zero))
gap = energy / norm_squared
assert gap == 2

# For P_t=P_0+exp(-2t)P_perp, spectral calculus recovers
# -t^{-1}log(P_t)=2P_perp=L.
t = 0.37
q = exp(-2 * t)
recovered_nonzero_eigenvalue = -log(q) / t
assert isclose(recovered_nonzero_eigenvalue, 2.0, rel_tol=1e-12)

# The positive-generator carré du champ is
# Gamma(f)=1/2(2 f Lf-L(f^2)).
f_squared = tuple(value * value for value in mean_zero)
l_f = mat_vec(two_state_l, mean_zero)
l_f_squared = mat_vec(two_state_l, f_squared)
gamma = tuple(
    (2 * mean_zero[i] * l_f[i] - l_f_squared[i]) / 2
    for i in range(2)
)
assert gamma == (2, 2)
assert uniform_inner(vacuum, gamma) == energy

# These symmetric three-state matrices share the vacuum vector and spectrum
# {0, 1, 10}. The first is a Markov graph Laplacian in the standard cone;
# the second has a positive off-diagonal entry and is not.
markov_l = (
    (Fraction(2, 3), Fraction(-1, 3), Fraction(-1, 3)),
    (Fraction(-1, 3), Fraction(31, 6), Fraction(-29, 6)),
    (Fraction(-1, 3), Fraction(-29, 6), Fraction(31, 6)),
)
non_markov_l = (
    (Fraction(13, 6), Fraction(-10, 3), Fraction(7, 6)),
    (Fraction(-10, 3), Fraction(20, 3), Fraction(-10, 3)),
    (Fraction(7, 6), Fraction(-10, 3), Fraction(13, 6)),
)

for matrix in (markov_l, non_markov_l):
    assert all(sum(row) == 0 for row in matrix)
    assert trace(matrix) == 11
    assert trace_square(matrix) == 101
    # With one zero eigenvalue, the other two have sum 11 and product 10.
    nonzero_product = (trace(matrix) ** 2 - trace_square(matrix)) / 2
    assert nonzero_product == 10

assert has_markov_off_diagonals(markov_l)
assert not has_markov_off_diagonals(non_markov_l)

print("two-state reconstructed nonzero generator eigenvalue:", recovered_nonzero_eigenvalue)
print("two-state Poincare gap:", gap)
print("two-state integrated carre du champ:", uniform_inner(vacuum, gamma))
print("three-state shared spectral invariants: trace=11 trace(L^2)=101 product=10")
print("first three-state presentation is Markov:", has_markov_off_diagonals(markov_l))
print("second three-state presentation is Markov:", has_markov_off_diagonals(non_markov_l))
print("all carrier-first reversal receipts passed")
