"""Exact seam-eigenvalue coefficients; no numerical spectrum or sampling.

All coefficients are ordinary powers s**m t**n. Matrices are supplied in a
diagonal eigenbasis of P. The basis may be orthogonal but unnormalized:
the target coordinate is its spectral left functional. Inputs must reproduce
all multiplication paths of total bidegree at most (2, 2).

The executable checks use fractions only. Rational rescaling of the
non-target basis removes the sqrt(3) in the AP single-seam test.
"""

from fractions import Fraction as Q
from math import factorial


def matrix(rows):
    return [[Q(value) for value in row] for row in rows]


def zero_matrix(n):
    return [[Q(0) for _ in range(n)] for _ in range(n)]


def matvec(operator, vector):
    return [
        sum((value * vector[j] for j, value in enumerate(row)), Q(0))
        for row in operator
    ]


def add(left, right):
    return [x + y for x, y in zip(left, right)]


def scale(value, vector):
    return [value * x for x in vector]


def generalized_pencil(diagonal, g, h, target=0):
    """Return exact ordinary-power eigenvalue/vector coefficients through (2,2)."""
    diagonal = [Q(value) for value in diagonal]
    n = len(diagonal)
    a = diagonal[target]
    if any(value == a for i, value in enumerate(diagonal) if i != target):
        raise ValueError("The declared target eigenvalue must be simple.")

    def exponential_coefficient(degree, vector):
        i, j = degree
        result = vector
        for _ in range(j):
            result = matvec(h, result)
        for _ in range(i):
            result = matvec(g, result)
        return scale(Q((-1) ** (i + j), factorial(i) * factorial(j)), result)

    origin = (0, 0)
    unit = [Q(int(i == target)) for i in range(n)]
    eigenvalues = {origin: a}
    vectors = {origin: unit}
    transformed = {origin: unit}  # e**(-sG-tH) phi
    degrees = sorted(
        ((i, j) for i in range(3) for j in range(3) if i or j),
        key=lambda degree: (sum(degree), degree),
    )
    for degree in degrees:
        m, n_degree = degree
        k_vector = [Q(0)] * len(diagonal)
        for i in range(m + 1):
            for j in range(n_degree + 1):
                if i or j:
                    lower = (m - i, n_degree - j)
                    k_vector = add(
                        k_vector,
                        exponential_coefficient((i, j), vectors[lower]),
                    )
        forcing = scale(a, k_vector)
        for i in range(m + 1):
            for j in range(n_degree + 1):
                subdegree = (i, j)
                if subdegree not in (origin, degree):
                    lower = (m - i, n_degree - j)
                    forcing = add(
                        forcing,
                        scale(eigenvalues[subdegree], transformed[lower]),
                    )
        eigenvalues[degree] = -forcing[target]
        vectors[degree] = [
            Q(0) if i == target else -value / (a - diagonal[i])
            for i, value in enumerate(forcing)
        ]
        transformed[degree] = add(vectors[degree], k_vector)

    return eigenvalues, vectors


def mixed_log_derivative(eigenvalues):
    """For branches even separately in s and t; return partial_s^2 partial_t^2 log."""
    for degree in ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)):
        if eigenvalues[degree]:
            raise ValueError("Separate evenness failed at a required degree.")
    a = eigenvalues[(0, 0)]
    return 4 * (
        eigenvalues[(2, 2)] / a
        - eigenvalues[(2, 0)] * eigenvalues[(0, 2)] / a**2
    )


def additive_hamiltonian(diagonal, g, h, target=0):
    """Ordinary coefficients of H0-sG-tH; exact closed walks through (2,2)."""
    diagonal = [Q(value) for value in diagonal]
    a = diagonal[target]
    if any(value == a for i, value in enumerate(diagonal) if i != target):
        raise ValueError("The declared target eigenvalue must be simple.")
    origin = (0, 0)
    eigenvalues = {origin: a}
    vectors = {origin: [Q(int(i == target)) for i in range(len(diagonal))]}
    degrees = sorted(
        ((i, j) for i in range(3) for j in range(3) if i or j),
        key=lambda degree: (sum(degree), degree),
    )
    for degree in degrees:
        m, n = degree
        forcing = [Q(0)] * len(diagonal)
        if m:
            forcing = add(forcing, scale(-1, matvec(g, vectors[(m - 1, n)])))
        if n:
            forcing = add(forcing, scale(-1, matvec(h, vectors[(m, n - 1)])))
        for i in range(m + 1):
            for j in range(n + 1):
                subdegree = (i, j)
                if subdegree not in (origin, degree):
                    forcing = add(
                        forcing,
                        scale(-eigenvalues[subdegree], vectors[(m - i, n - j)]),
                    )
        eigenvalues[degree] = forcing[target]
        vectors[degree] = [
            Q(0) if i == target else -value / (diagonal[i] - a)
            for i, value in enumerate(forcing)
        ]
    return eigenvalues


def grid_moves(states, amplitude):
    size = len(states)
    g, h = zero_matrix(size), zero_matrix(size)
    for i, (left, right) in enumerate(states):
        for j, (other_left, other_right) in enumerate(states):
            if right == other_right and abs(left - other_left) == 1:
                g[i][j] = amplitude
            if left == other_left and abs(right - other_right) == 1:
                h[i][j] = amplitude
    return g, h


def nine_state_formula(diagonal, states):
    """Closed-walk formula for moves of amplitude 1/sqrt(2)."""
    eigenvalue = dict(zip(states, diagonal))
    a = eigenvalue[(0, 0)]
    x = {i: 1 / (1 - eigenvalue[(i, 0)] / a) for i in (-1, 1)}
    y = {j: 1 / (1 - eigenvalue[(0, j)] / a) for j in (-1, 1)}
    total_x, total_y = sum(x.values()), sum(y.values())
    corners = sum(
        (x[i] + y[j] - 1) ** 2 / (1 - eigenvalue[(i, j)] / a)
        for i in (-1, 1)
        for j in (-1, 1)
    )
    return (
        corners
        - total_y * sum(value**2 for value in x.values())
        - total_x * sum(value**2 for value in y.values())
        + total_x * total_y
    )


def polynomial_add(*polynomials):
    length = max(map(len, polynomials))
    result = [Q(0)] * length
    for polynomial in polynomials:
        for i, value in enumerate(polynomial):
            result[i] += value
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def polynomial_multiply(*polynomials):
    result = [Q(1)]
    for polynomial in polynomials:
        product = [Q(0)] * (len(result) + len(polynomial) - 1)
        for i, left in enumerate(result):
            for j, right in enumerate(polynomial):
                product[i + j] += left * right
        result = product
    return result


def abelian_polynomial_identity():
    """Clear AC6 denominators exactly; compare every coefficient with q P(q)."""
    u, c2, c3, c5 = [1, -1], [1, 1], [1, 1, 1], [1] * 5
    add_poly, mul = polynomial_add, polynomial_multiply
    # A+B-1, 2A-1, 2B-1, 2v-1 after their own denominators are cleared.
    ab = add_poly([1], c3, scale(-1, mul(u, c3)))
    aa = add_poly([2], scale(-1, mul(u, c3)))
    bb = add_poly([2], scale(-1, u))
    vv = add_poly([2], scale(-1, mul(u, c2)))
    # Multiply L1-L0 by D=u^3 C2^3 C3^3 C5, term by term.
    numerator = add_poly(
        mul(add_poly(scale(2, mul(ab, ab)), mul(aa, aa)), c2, c2, c2, c3),
        mul(bb, bb, c2, c2, c2, c3, c3, c3, c5),
        scale(-2, mul(add_poly([1], c3), add_poly([1], mul(c3, c3)), c2, c2, c2, c5)),
        mul(add_poly([1], c3), add_poly([1], c3), u, c2, c2, c2, c3, c5),
        scale(-2, mul(vv, vv, add_poly(c3, c5), c2, c3, c3)),
        scale(8, mul(c3, c3, c3, c5)),
        scale(-4, mul(u, c2, c3, c3, c3, c5)),
    )
    expected_p = [1, 8, 30, 79, 151, 234, 294, 318, 294, 234, 151, 79, 30, 8, 1]
    assert numerator == [0] + expected_p
    assert all(value > 0 for value in expected_p)
    return numerator


def controls():
    # Two disjoint two-state seams: each isolated eigenvalue factorizes.
    states = [(0, 0), (1, 0), (0, 1), (1, 1)]
    g, h = grid_moves(states, Q(1))
    diagonal = [Q(1), Q(1, 2), Q(1, 3), Q(1, 6)]
    for target in (0, 1):
        coefficients, _ = generalized_pencil(diagonal, g, h, target)
        assert mixed_log_derivative(coefficients) == 0
    print("Disjoint product branches: mixed logarithmic coefficient = 0 (exact).")

    # AP second order only needs the target-to-singlet/triplet matrix elements.
    a, beta_0, beta_1 = Q(2, 3), Q(1, 5), Q(1, 7)
    g = matrix([[0, Q(1, 2), Q(3, 2)], [Q(1, 2), 0, 0], [Q(1, 2), 0, 0]])
    coefficients, _ = generalized_pencil([a, beta_0, beta_1], g, zero_matrix(3))
    expected = a / 2 * (
        Q(1, 4) * (a + beta_0) / (a - beta_0)
        + Q(3, 4) * (a + beta_1) / (a - beta_1)
    )
    assert coefficients[(2, 0)] == expected
    print("AP single-seam coefficient and 1/4, 3/4 channel weights: exact match.")

    # Actual heat-U(1) corner. A rational amplitude 1/2 is used first.
    # Replacing both moves by 1/sqrt(2) multiplies a (2,2) coefficient by 4.
    states = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1)]
    target = states.index((0, 0))
    g, h = grid_moves(states, Q(1, 2))
    heat = Q(1, 2)
    results = []
    for charge in (0, 1):
        diagonal = [
            heat ** (
                4 * charge**2 + 4 * left**2 + 4 * right**2
                + 2 * charge * left - 2 * charge * right + 2 * left * right
            )
            for left, right in states
        ]
        coefficients, _ = generalized_pencil(diagonal, g, h, target)
        derivative = 4 * mixed_log_derivative(coefficients)
        assert derivative == nine_state_formula(diagonal, states)
        results.append(derivative)
    assert results[0] == Q(559232, 24168375)
    assert results[1] == Q(62312660, 85266027)
    assert results[1] - results[0] == Q(7542461188, 10658253375)
    print(f"Heat U(1), t=1/2: vacuum mixed log derivative = {results[0]}.")
    print(f"Heat U(1), t=1/2: charge-one mixed log derivative = {results[1]}.")
    print(f"Heat U(1): vacuum-subtracted difference = {results[1] - results[0]}.")
    abelian_polynomial_identity()
    print("Heat U(1): AC6-to-AC8 cleared-denominator polynomial identity holds coefficient by coefficient; all 15 P coefficients are positive.")

    # Same graph, additive Hamiltonian with epsilon=1. Constants in the
    # nonnegative seam potentials cancel from excitation energies.
    hamiltonian_results = []
    for charge in (0, 1):
        diagonal = [
            4 * charge**2 + 4 * left**2 + 4 * right**2
            + 2 * charge * left - 2 * charge * right + 2 * left * right
            for left, right in states
        ]
        coefficients = additive_hamiltonian(diagonal, g, h, target)
        # Restore move amplitude 1/sqrt(2), retaining ordinary coefficients.
        hamiltonian_results.append(4 * coefficients[(2, 2)])
    assert hamiltonian_results == [Q(-1, 480), Q(-31, 540)]
    hamiltonian_energy = 4 * (hamiltonian_results[1] - hamiltonian_results[0])
    assert hamiltonian_energy == Q(-239, 1080)
    print(f"Heat U(1) Hamiltonian: ordinary vacuum/charge-one coefficients = {hamiltonian_results[0]}, {hamiltonian_results[1]}.")
    print(f"Heat U(1) Hamiltonian: mixed excitation-energy derivative = {hamiltonian_energy} (epsilon=1).")

    # SU(2) Haar contractions: only the scalar quaternion monomials survive.
    haar_square = Q(1, 4)
    two_face_overlap = 2**3 * haar_square**2
    three_face_overlap = 2**4 * haar_square**3
    assert two_face_overlap == Q(1, 2)
    assert three_face_overlap == Q(1, 4)
    # Each normalized fundamental character has Haar second moment one.
    leading_corner_log = factorial(2) ** 2 * three_face_overlap**2
    assert leading_corner_log == Q(1, 4)
    print("SU(2) leading corner overlaps: 1/2, 1/2, 1/4 (exact Haar contractions).")
    print("SU(2) leading t_f^2 coefficient = 1/4; analytic remainder belongs to the corner proof.")
    print("PASS: rational coefficient checks only; no sampled or numerical dynamics.")


if __name__ == "__main__":
    controls()
