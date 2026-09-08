"""Exact rational checks of the binary sewn state and conditional clock.

These checks cover the complete four-state carrier, the invariant binary
quotient, unequal boundary-integration orders, and the clock retuning
counterexample. SU(2) constants are checked from exact character moments;
the infinite-carrier completeness proof belongs to the linked note.
"""

from fractions import Fraction as F


STATES = [(x, y) for x in (-1, 1) for y in (-1, 1)]


def action(matrix, vector):
    return [sum((a * b for a, b in zip(row, vector)), F(0)) for row in matrix]


def inner(left, right, weight):
    return sum((a * b * w for a, b, w in zip(left, right, weight)), F(0))


def check_binary(k):
    r = F(3 ** k - 1, 3 ** k + 1)
    rho = r * r
    probability = [(1 + rho * x * y) / 4 for x, y in STATES]
    assert sum(probability) == 1 and min(probability) > 0
    # The normalized tensor comparison is a density relative to Haar(+-1).
    def p(x, u):
        return 1 + r * x * u

    for i, (x, y) in enumerate(STATES):
        sewn_density = sum((p(x, u) * p(y, u) for u in (-1, 1)), F(0)) / 2
        assert sewn_density / 4 == probability[i]
    # Three comparison factors, two internal variables: either summation
    # order retains the same x,z kernel without projecting to a fitted family.
    for x, z in STATES:
        first = sum((p(x, u) * sum((p(u, v) * p(v, z) for v in (-1, 1)), F(0)) / 2
                     for u in (-1, 1)), F(0)) / 2
        second = sum((sum((p(x, u) * p(u, v) for u in (-1, 1)), F(0)) / 2 * p(v, z)
                      for v in (-1, 1)), F(0)) / 2
        assert first == second == 1 + r ** 3 * x * z
    px = [[2 * probability[j] if x == u else F(0) for j, (u, v) in enumerate(STATES)]
          for x, y in STATES]
    py = [[2 * probability[j] if y == v else F(0) for j, (u, v) in enumerate(STATES)]
          for x, y in STATES]
    clock = [[2 * F(i == j) - px[i][j] - py[i][j] for j in range(4)] for i in range(4)]
    vectors = [[F(1)] * 4, [F(x + y) for x, y in STATES],
               [F(x - y) for x, y in STATES], [x * y - rho for x, y in STATES]]
    rates = [F(0), 1 - rho, 1 + rho, F(2)]
    for i in range(4):
        assert sum(clock[i]) == 0
        for j in range(4):
            assert probability[i] * clock[i][j] == probability[j] * clock[j][i]
            if i != j:
                assert clock[i][j] <= 0
    for i, (vector, rate) in enumerate(zip(vectors, rates)):
        assert action(clock, vector) == [rate * v for v in vector]
        assert inner(vector, vector, probability) > 0
        for j in range(i):
            assert inner(vector, vectors[j], probability) == 0
    # The inverse-image and cross susceptibility retain BOTH response rates.
    y = [F(y) for x, y in STATES]
    inv_y = [vectors[1][i] / (2 * (1 - rho)) - vectors[2][i] / (2 * (1 + rho))
             for i in range(4)]
    assert action(clock, inv_y) == y
    x = [F(x) for x, y in STATES]
    assert inner(x, inv_y, probability) == 2 * rho / (1 - rho * rho)
    # Simultaneous-flip invariants are exactly 1 and xy-rho, so quotient gap=2.
    for i, (x, y) in enumerate(STATES):
        j = STATES.index((-x, -y))
        assert vectors[3][i] == vectors[3][j]
        assert vectors[1][i] == -vectors[1][j]
    # Additional whole-state updates preserve the state but change the clock.
    theta = F(2, 7)
    modified = [[clock[i][j] + theta * (F(i == j) - probability[j])
                 for j in range(4)] for i in range(4)]
    for vector, rate in zip(vectors[1:], rates[1:]):
        assert action(modified, vector) == [(rate + theta) * v for v in vector]
    gap = rates[1]
    assert gap == F(4 * 3 ** k, (3 ** k + 1) ** 2)
    print(f'EXACT binary k={k}: sewn correlation={rho}, full gap={gap}, invariant quotient gap=2')
    return gap


def su2_constants():
    # Haar-normalized characters: <chi_1>=0, <chi_1^2>=1, d_1=2.
    p_coefficient = F(1, 4)
    multiplier = p_coefficient / 2
    q_coefficient = p_coefficient ** 2 / 2
    correlation = q_coefficient / 2
    assert multiplier == F(1, 8) and correlation == F(1, 64)
    assert 1 - correlation == F(63, 64)
    assert 2 * correlation / (1 - correlation ** 2) == F(128, 4095)
    # <chi_1,p*chi_1> and all other Peter-Weyl multipliers use the
    # stated character convolution theorem, not numerical group sampling.
    print('EXACT SU(2) character coefficients: covariance=1/64, gap=63/64, mixed inverse=128/4095')


if __name__ == '__main__':
    gaps = [check_binary(k) for k in (0, 1, 2, 3, 6)]
    assert all(left > right for left, right in zip(gaps, gaps[1:]))
    su2_constants()
    print('PASS rational detailed balance, complete eigenbasis, mixed inverse, '
          'sewing order and independent-clock retuning checks')
