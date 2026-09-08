"""Exact initial-layer certificate for the supplied two-plaquette heat.

At kappa=lambda=1, use P(t)=exp[-t(K-a-b)]1. Removing the scalar
potential constant multiplies the amplitude only; no L2 or vacuum
normalization is used in the curvature certificate. A degree-seven
Taylor vector is checked twice: by the normalized harmonic matrix from
ground_marginal_certificate.py and by the exact coordinate operator
(TP3--TP4) on Fraction polynomials in (a,b,z). Conditional Haar moments
then produce the complete finite time polynomial, including relational
channels. No eigensolver or sampled latitude grid selects this vector.

Analytic inputs: ||exp[-t(K-a-b)]||_X <= exp(5t/2), the Taylor integral
remainder, and the marginal bilinear constants (1,75/8,525/4). The
companion proof must justify these operators and their common domain.
The arithmetic certifies v <= -t^3/12 for every latitude and
0 <= t <= 1/20 in this fixed compact system, not a continuum gap.
"""

from fractions import Fraction as F
from functools import lru_cache
import math

import ground_marginal_certificate as interval


I, ZERO = interval.I, interval.ZERO
T0 = F(1, 20)
DEGREE = 7
NORM_BOUNDS = (F(1), F(2), F(21, 4), F(12), F(26),
               F(55), F(119), F(260), F(576))
EXP_UPPER = F(8, 7)
RAW_ERROR = EXP_UPPER*NORM_BOUNDS[8]*T0**8


def add(p, q, factor=F(1)):
    result = dict(p)
    for key, value in q.items():
        result[key] = result.get(key, F(0))+factor*value
        if not result[key]:
            del result[key]
    return result


def multiply(p, q):
    result = {}
    for first, c in p.items():
        for second, d in q.items():
            key = tuple(i+j for i, j in zip(first, second))
            result[key] = result.get(key, F(0))+c*d
    return {key: value for key, value in result.items() if value}


def derivative(p, axis=0):
    result = {}
    for key, value in p.items():
        if key[axis]:
            lowered = list(key)
            lowered[axis] -= 1
            result[tuple(lowered)] = key[axis]*value
    return result


def term(key, value=1):
    return {key: F(value)}


ONE = term((0, 0, 0))
A, B, Z = term((1, 0, 0)), term((0, 1, 0)), term((0, 0, 1))
S = add(A, B)
HA, HB = add(ONE, multiply(A, A), -1), add(ONE, multiply(B, B), -1)


def coordinate_metric():
    """The exact TP4 cometric, including the shared electric row."""
    g = [[None]*3 for _ in range(3)]
    g[0][0], g[1][1] = HA, HB
    g[0][1] = g[1][0] = term((0, 0, 1), F(1, 4))
    g[0][2] = g[2][0] = add(
        {}, add(multiply(A, Z), multiply(B, HA), F(1, 4)), -1)
    g[1][2] = g[2][1] = add(
        {}, add(multiply(B, Z), multiply(A, HB), F(1, 4)), -1)
    squares = add(add(multiply(A, A), multiply(B, B)),
                  multiply(multiply(A, A), multiply(B, B)))
    g[2][2] = add(term((0, 0, 0), F(3, 2)), squares, -F(1, 2))
    g[2][2] = add(g[2][2], multiply(Z, Z), -F(3, 2))
    g[2][2] = add(g[2][2], multiply(multiply(A, B), Z), F(1, 2))
    return g


METRIC = coordinate_metric()
DRIFT = (term((1, 0, 0), 3), term((0, 1, 0), 3),
         add(term((0, 0, 1), 5), multiply(A, B), -F(3, 2)))


def generator(p):
    """Apply -K+a+b, not a reset marginal generator."""
    result = {}
    for i in range(3):
        result = add(result, multiply(DRIFT[i], derivative(p, i)), -1)
        for j in range(3):
            result = add(result, multiply(METRIC[i][j],
                                          derivative(derivative(p, i), j)))
    return add(result, multiply(S, p))


def conditional_haar(p):
    """Integrate b,z at fixed a; the result is an exact polynomial in a.

    I[b^(2m)z^(2j)] = (1-a^2)^j (2m)!(2j)! /
                      [4^(m+j)m!j!(m+j+1)!]. Odd hidden powers vanish.
    """
    result = {}
    for (i, j, k), value in p.items():
        if j % 2 or k % 2:
            continue
        m, ell = j//2, k//2
        moment = F(math.factorial(2*m)*math.factorial(2*ell),
                   4**(m+ell)*math.factorial(m)*math.factorial(ell)
                   *math.factorial(m+ell+1))
        for power in range(ell+1):
            key = (i+2*power,)
            result[key] = result.get(key, F(0)) + (
                value*moment*math.comb(ell, power)*(-1)**power)
    return {key: value for key, value in result.items() if value}


def full_haar(p):
    result = F(0)
    for (power,), value in conditional_haar(p).items():
        if power % 2 == 0:
            j = power//2
            result += value*F(math.factorial(2*j),
                              4**j*math.factorial(j)*math.factorial(j+1))
    return result


@lru_cache(maxsize=1)
def harmonic_taylor():
    """Interval rows (-A)^j1/j!, with every newly reached harmonic."""
    rows = [{(0, 0, 0): I.point(1)}]
    for j in range(1, 9):
        previous = rows[-1]
        physical = interval.physical_action(previous, j-1)
        # physical_action is K+2-a-b; restore the removed scalar 2.
        rows.append({key: (2*previous.get(key, ZERO)-value)/j
                     for key, value in physical.items()})
    for j, row in enumerate(rows):
        assert interval.norm_x2(row).hi <= NORM_BOUNDS[j]
    return rows


def coordinate_taylor():
    rows = [ONE]
    for j in range(1, DEGREE+1):
        rows.append({key: value/j for key, value in generator(rows[-1]).items()})
    return rows


def marginal_time_polynomials(rows):
    degree = len(rows)-1
    rho = [{} for _ in range(2*degree+1)]
    for i, first in enumerate(rows):
        for j, second in enumerate(rows):
            rho[i+j] = add(rho[i+j], conditional_haar(multiply(first, second)))
    numerator = [{} for _ in range(4*degree+1)]
    for i, first in enumerate(rho):
        for j, second in enumerate(rho):
            product = add(multiply(derivative(first), derivative(second)),
                          multiply(first, derivative(derivative(second))), -1)
            numerator[i+j] = add(numerator[i+j], product)
    return rho, numerator


def initial_normalized_data():
    """Data for a subsequent proof, not a silently normalized source.

    'coefficients' enclose P7(T0)/p000 with vacuum exactly one. The
    error is to the exact P(T0)/<1,P(T0)>, in the X norm. A caller
    replacing the intervals by rational points must add that X distance.
    The normalization estimate additionally uses <1,P(t)> >= 1,
    from Jensen/Feynman--Kac with stationary Haar initial law and the
    zero Haar mean of a+b. It is not inferred from a finite truncation.
    """
    rows = harmonic_taylor()
    raw = {key: ZERO for key in interval.proposal.labels(DEGREE)}
    for j in range(DEGREE+1):
        for key, value in rows[j].items():
            raw[key] = raw[key]+value*T0**j
    denominator = raw[0, 0, 0]
    raw_norm, qnorm = interval.norm_x2(raw), interval.norm_x2(raw, True)
    assert denominator.lo >= 1
    assert raw_norm.hi < F(9, 8) and qnorm.hi < F(1, 8)
    normalized = {key: value/denominator for key, value in raw.items()}
    normalized[0, 0, 0] = I.point(1)
    error = (1+qnorm.hi/denominator.lo)*RAW_ERROR
    return {'time': T0, 'coefficients': normalized, 'error_x': error,
            'raw_coefficients': raw, 'raw_error_x': RAW_ERROR,
            'denominator': denominator, 'raw_norm_x': raw_norm,
            'nonvacuum_norm_x': qnorm}


def certify():
    rows = coordinate_taylor()
    harmonic = harmonic_taylor()
    assert generator(ONE) == S
    assert rows[2] == {key: value/2 for key, value in
                       add(multiply(S, S), S, -3).items()}
    # Explicitly retain the relative channel created at third order.
    assert rows[3][0, 0, 1] == F(1, 6)
    for j, (poly, vector) in enumerate(zip(rows, harmonic)):
        exact_squared_norm = full_haar(multiply(poly, poly))
        enclosed = sum((value.square() for value in vector.values()), ZERO)
        assert enclosed.lo <= exact_squared_norm <= enclosed.hi
        interval.display(f'||A^{j} 1||_X/{j}! enclosure', interval.norm_x2(vector))
    interval.display('||A^8 1||_X/8! enclosure', interval.norm_x2(harmonic[8]))
    print('PASS independent exact coordinate/harmonic Taylor norms, including '
          'the third-order relative channel and all reached modes.', flush=True)

    rho, numerator = marginal_time_polynomials(rows)
    assert rho[0] == term((0,), 1) and rho[1] == term((1,), 2)
    assert numerator[:3] == [{}, {}, {}]
    assert numerator[3] == term((0,), F(4, 3))
    assert numerator[4] == {(0,): -F(17, 3), (1,): F(16, 3)}
    assert numerator[5] == {(0,): F(73, 5), (1,): -F(508, 15), (2,): F(32, 3)}
    v4 = add(numerator[4], multiply(rho[1], numerator[3]), -2)
    assert {key: -value/2 for key, value in v4.items()} == term((0,), F(17, 6))
    # All powers are nonnegative after dividing by t^3. Bounding |a|<=1
    # by coefficient absolute sums makes the worst bound occur at T0.
    higher = sum((sum(abs(v) for v in numerator[j].values())*T0**(j-3)
                  for j in range(5, len(numerator))), F(0))
    polynomial_floor = F(4, 3)-11*T0-higher
    assert polynomial_floor > F(59, 100)

    taylor_norm = sum((NORM_BOUNDS[j]*T0**j for j in range(8)), F(0))
    assert taylor_norm < F(9, 8)
    # exp(5T0/2)=exp(1/8) <= 1/(1-1/8)=8/7, by its positive series.
    p = F(9, 8)
    quartic_constant = F(75, 8)**2+F(525, 4)
    # With eta(t)=EXP_UPPER*576*t^8, the divided quartic loss has only
    # positive multiples of t^5,t^13,t^21,t^29, hence is largest at T0.
    loss_ratio = quartic_constant*((p+RAW_ERROR)**4-p**4)/T0**3
    assert loss_ratio < F(13, 50)
    assert polynomial_floor-loss_ratio > F(3, 10)
    v_coefficient = -F(3, 10)/(2*EXP_UPPER**4)
    assert v_coefficient <= -F(1, 12)
    interval.display('finite N7/t^3 lower bound', I.point(polynomial_floor))
    interval.display('raw Taylor error at t0', I.point(RAW_ERROR))
    interval.display('quartic transfer loss divided by t^3', I.point(loss_ratio))
    interval.display('full numerator coefficient lower bound', I.point(polynomial_floor-loss_ratio))
    interval.display('full v/t^3 upper bound', I.point(v_coefficient))

    initial = initial_normalized_data()
    interval.display('P7(t0) Haar coefficient', initial['denominator'])
    interval.display('P7(t0) nonvacuum X norm', initial['nonvacuum_norm_x'])
    interval.display('vacuum-normalized initial X error', I.point(initial['error_x']))
    assert initial['coefficients'][0, 0, 0] == I.point(1)
    print('PASS exact finite checks for the initial-layer theorem: with the '
          'stated X-semigroup, Taylor-remainder and marginal bridge, '
          'N>=3t^3/10 and v<=-t^3/12 at every latitude for 0<=t<=1/20. '
          'The separately supplied initial-data normalization bound uses '
          'the Haar/Jensen lower bound; no continuum mass gap is inferred.', flush=True)


if __name__ == '__main__':
    certify()
