"""Exact quaternion-polynomial calculation on the nine-link SU(2) corner.

Fractions only: no sampling, numerical eigensolver, or package dependency.
Hamiltonian normalization is epsilon=1. Physical polynomials use three unit
quaternions U,V,W, with Haar second moments delta_ij/4. The raw paths have
lengths (a,b,c;p,q,r)=(1,1,1;2,2,2).
"""

from fractions import Fraction as Q
from itertools import permutations


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for monomial, value in polynomial.items():
            result[monomial] = result.get(monomial, Q(0)) + value
    return {monomial: value for monomial, value in result.items() if value}


def scale(value, polynomial):
    return {m: value * c for m, c in polynomial.items() if value * c}


def multiply(left, right):
    result = {}
    for m, c in left.items():
        for n, d in right.items():
            exponent = tuple(a + b for a, b in zip(m, n))
            result[exponent] = result.get(exponent, Q(0)) + c * d
    return {m: c for m, c in result.items() if c}


def monomial(*variables):
    exponent = [0] * 12
    for variable in variables:
        exponent[variable] += 1
    return {tuple(exponent): Q(1)}


def epsilon(i, j, k):
    if len({i, j, k}) < 3:
        return 0
    return 1 if (i, j, k) in ((1, 2, 3), (2, 3, 1), (3, 1, 2)) else -1


def field(group, axis, left=True):
    """h q or q h, h=exp(theta e_axis/2), on Hamilton quaternions."""
    offset = 4 * group
    result = [(offset + axis, offset, Q(-1, 2)),
              (offset, offset + axis, Q(1, 2))]
    for row in range(1, 4):
        for column in range(1, 4):
            value = epsilon(row, axis, column) * (1 if left else -1)
            if value:
                result.append((offset + column, offset + row, Q(value, 2)))
    return result


def negate(operator):
    return [(to, source, -value) for to, source, value in operator]


def derivative(polynomial, operator):
    """Linear vector field sum c*x_to*d/dx_source on ambient polynomials."""
    result = {}
    for exponent, value in polynomial.items():
        for to, source, coefficient in operator:
            if exponent[source]:
                target = list(exponent)
                target[source] -= 1
                target[to] += 1
                target = tuple(target)
                result[target] = result.get(target, Q(0)) + (
                    value * coefficient * exponent[source]
                )
    return {m: c for m, c in result.items() if c}


def hamiltonian(polynomial, shared_edge=True):
    """(4/3) sum of the nine raw-link Casimirs, after exact tree gauge fixing."""
    result = {}
    for axis in range(1, 4):
        left = [field(group, axis) for group in range(3)]
        right = [field(group, axis, left=False) for group in range(3)]
        # Each exterior two-link path contributes twice its loop Casimir.
        for operator in left:
            result = add(result, scale(Q(-8, 3), derivative(
                derivative(polynomial, operator), operator)))
        # The three original axis-link rows preserve their actual incidence.
        axes = [left[0] + left[1], negate(right[0]) + left[2]]
        axes += ([right[1] + right[2]] if shared_edge else [right[1], right[2]])
        for operator in axes:
            result = add(result, scale(Q(-4, 3), derivative(
                derivative(polynomial, operator), operator)))
    return result


def coefficients(polynomial, basis, pivots):
    result = [polynomial.get(next(iter(monomial(*pivot))), Q(0)) for pivot in pivots]
    assert add(*(scale(c, p) for c, p in zip(result, basis))) == polynomial
    return result


def action_matrix(basis, pivots, shared_edge=True):
    columns = [coefficients(hamiltonian(p, shared_edge), basis, pivots) for p in basis]
    return [list(row) for row in zip(*columns)]


def matvec(matrix, vector):
    return [sum((a * b for a, b in zip(row, vector)), Q(0)) for row in matrix]


def shift(matrix, scalar):
    return [[value - (scalar if i == j else 0) for j, value in enumerate(row)]
            for i, row in enumerate(matrix)]


def solve(matrix, vector):
    rows = [list(row) + [value] for row, value in zip(matrix, vector)]
    size = len(vector)
    for i in range(size):
        pivot = next(j for j in range(i, size) if rows[j][i])
        rows[i], rows[pivot] = rows[pivot], rows[i]
        value = rows[i][i]
        rows[i] = [entry / value for entry in rows[i]]
        for j in range(size):
            if j != i:
                value = rows[j][i]
                rows[j] = [a - value * b for a, b in zip(rows[j], rows[i])]
    return [row[-1] for row in rows]


def inner(left, right, gram):
    return sum((a * b * weight for a, b, weight in zip(left, right, gram)), Q(0))


def verify_self_adjoint(matrix, gram):
    assert all(gram[i] * matrix[i][j] == gram[j] * matrix[j][i]
               for i in range(len(gram)) for j in range(len(gram)))


def dot_pair(first, second):
    return add(*(monomial(4 * first + i, 4 * second + i) for i in range(1, 4)))


def controls():
    f, g, h = [scale(2, monomial(4 * group)) for group in range(3)]
    for source in (f, g, h):
        assert hamiltonian(source) == scale(4, source)

    pair_basis = [monomial(0, 4), dot_pair(0, 1)]
    pair_matrix = action_matrix(pair_basis, [(0, 4), (1, 5)])
    assert pair_matrix == [[Q(8), Q(-2)], [Q(-2, 3), Q(20, 3)]]
    pair_gram = [Q(1, 16), Q(3, 16)]
    verify_self_adjoint(pair_matrix, pair_gram)
    first = solve(shift(pair_matrix, 4), [Q(4), Q(0)])
    assert first == [Q(8, 7), Q(2, 7)]
    first_polynomial = add(*(scale(c, p) for c, p in zip(first, pair_basis)))
    a = inner([Q(4), Q(0)], first, pair_gram)
    b = inner(first, first, pair_gram)
    assert (a, b) == (Q(2, 7), Q(19, 196))

    other_basis = [monomial(0, 8), dot_pair(0, 2)]
    other_matrix = action_matrix(other_basis, [(0, 8), (1, 9)])
    assert other_matrix == [[Q(8), Q(2)], [Q(2, 3), Q(20, 3)]]
    other_first = solve(shift(other_matrix, 4), [Q(4), Q(0)])
    assert other_first == [Q(8, 7), Q(-2, 7)]
    other_polynomial = add(*(scale(c, p) for c, p in zip(other_first, other_basis)))

    basis = [monomial(0, 4, 8),
             multiply(monomial(0), dot_pair(1, 2)),
             multiply(monomial(4), dot_pair(0, 2)),
             multiply(monomial(8), dot_pair(0, 1)),
             add(*(scale(epsilon(i, j, k), monomial(i, 4 + j, 8 + k))
                   for i, j, k in permutations((1, 2, 3))))]
    pivots = [(0, 4, 8), (0, 5, 9), (1, 4, 9), (1, 5, 8), (1, 6, 11)]
    matrix = action_matrix(basis, pivots)
    gram = [Q(value, 64) for value in (1, 3, 3, 3, 6)]
    verify_self_adjoint(matrix, gram)
    w_polynomial = add(multiply(h, first_polynomial), multiply(g, other_polynomial))
    w = coefficients(w_polynomial, basis, pivots)
    assert w == [Q(value, 7) for value in (32, 0, -4, 4, 0)]
    returned = solve(shift(matrix, 4), w)
    assert returned == [Q(value, 385) for value in (292, 76, -106, 106, -64)]
    quadratic = inner(w, returned, gram)
    assert quadratic == Q(743, 10780)

    # Independent exact spectral-projector check of all five middle channels.
    energies = [Q(6), Q(34, 3), Q(14)]
    spectral_weights = []
    projector_sum = [Q(0)] * 5
    for energy in energies:
        vector = list(w)
        for other in energies:
            if other != energy:
                vector = [value / (energy - other)
                          for value in matvec(shift(matrix, other), vector)]
        assert matvec(matrix, vector) == [energy * value for value in vector]
        projector_sum = [a + b for a, b in zip(projector_sum, vector)]
        spectral_weights.append(inner(w, vector, gram))
    assert projector_sum == w
    assert spectral_weights == [Q(1, 16), Q(177, 784), Q(27, 392)]
    assert sum(weight / (energy - 4) for weight, energy in
               zip(spectral_weights, energies)) == quadratic

    # Actual vacuum: R G=G/4, R H=H/4, so its middle vector is GH/2.
    vacuum_basis = [monomial(4, 8), dot_pair(1, 2)]
    vacuum_matrix = action_matrix(vacuum_basis, [(4, 8), (5, 9)])
    assert vacuum_matrix == pair_matrix
    vacuum_w = [Q(2), Q(0)]
    vacuum_returned = solve(vacuum_matrix, vacuum_w)
    assert vacuum_returned == [Q(10, 39), Q(1, 39)]
    vacuum_quadratic = inner(vacuum_w, vacuum_returned, pair_gram)
    assert vacuum_quadratic == Q(5, 156)

    # The remaining mixed pairing is exactly zero by conditional Haar
    # projection, proved in the companion note, not by a small coefficient.
    odd_ordinary = -quadratic + 2 * a * b
    vacuum_ordinary = -vacuum_quadratic + Q(1, 32)
    energy_derivative = 4 * (odd_ordinary - vacuum_ordinary)
    assert odd_ordinary == Q(-1021, 75460)
    assert vacuum_ordinary == Q(-1, 1248)
    assert energy_derivative == Q(-299687, 5885880)
    ratio = energy_derivative / Q(-239, 1080)
    assert ratio == Q(2697183, 11722711)

    # Different graph: split the common c edge and its exterior endpoint.
    # Fundamental one-face energies and first-leg resolvents are unchanged.
    split_matrix = action_matrix(basis, pivots, shared_edge=False)
    verify_self_adjoint(split_matrix, gram)
    split_returned = solve(shift(split_matrix, 4), w)
    assert split_returned == [Q(value, 49) for value in (32, 2, -8, 8, -2)]
    split_quadratic = inner(w, split_returned, gram)
    assert split_quadratic == 2 * a * b == Q(19, 343)
    split_vacuum_matrix = action_matrix(vacuum_basis, [(4, 8), (5, 9)], shared_edge=False)
    assert split_vacuum_matrix == [[Q(8), Q(0)], [Q(0), Q(8)]]
    split_vacuum_returned = solve(split_vacuum_matrix, vacuum_w)
    split_vacuum_quadratic = inner(vacuum_w, split_vacuum_returned, pair_gram)
    assert split_vacuum_quadratic == Q(1, 32)
    split_derivative = 4 * (-split_quadratic + 2 * a * b
                            + split_vacuum_quadratic - Q(1, 32))
    assert split_derivative == 0

    print('Raw-edge Casimir matrix in (A,B,C,D,E):')
    for row in matrix:
        print('  ' + ', '.join(map(str, row)))
    print('Haar Gram: ' + ', '.join(map(str, gram)))
    print('Middle spectral weights: ' + ', '.join(map(str, spectral_weights)))
    print(f'Odd first-leg moments: a={a}, b={b}.')
    print('Returned mixed vector: ' + ', '.join(map(str, returned)))
    print(f'Odd/vacuum mixed resolvent forms: {quadratic}, {vacuum_quadratic}.')
    print(f'Ordinary odd/vacuum quartic coefficients: {odd_ordinary}, {vacuum_ordinary}.')
    print(f'Complete excitation-energy mixed derivative: {energy_derivative}.')
    print(f'Ratio to calibrated Abelian coefficient: {ratio}.')
    print(f'Split-edge odd/vacuum forms: {split_quadratic}, {split_vacuum_quadratic}; connected energy derivative exactly zero.')
    print('PASS: exact polynomial actions, Haar Gram, rational solves and normalization contacts; no sampling.')


if __name__ == '__main__':
    controls()
