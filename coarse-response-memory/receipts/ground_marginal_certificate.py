"""Exact-arithmetic trial checks for the fixed kappa=lambda=1 marginal.

The floating solver ONLY proposes a vector. Decimal rationalization then
defines an exact trial with Haar coefficient one. All subsequent matrix,
residual, polynomial and Bernstein bounds use Fraction intervals; square
roots are enclosed by integer arithmetic. The residual includes omitted
cutoff+1 modes. The final transfer calculation states its analytic X2
bridge constants explicitly; arithmetic does not prove those constants.
This is the supplied seven-link system, not an infinite-volume gap claim.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import math

import two_plaquette_vacuum_receipt as proposal


ROOT_SCALE = 10**50


@dataclass(frozen=True)
class I:
    lo: F
    hi: F

    def __post_init__(self):
        assert isinstance(self.lo, F) and isinstance(self.hi, F)
        assert self.lo <= self.hi

    @staticmethod
    def point(value):
        assert isinstance(value, (int, str, F))
        value = F(value)
        return I(value, value)

    @staticmethod
    def coerce(value):
        return value if isinstance(value, I) else I.point(value)

    def __add__(self, other):
        other = I.coerce(other)
        return I(self.lo+other.lo, self.hi+other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self+-I.coerce(other)

    def __rsub__(self, other):
        return I.coerce(other)+-self

    def __mul__(self, other):
        other = I.coerce(other)
        products = (self.lo*other.lo, self.lo*other.hi,
                    self.hi*other.lo, self.hi*other.hi)
        return I(min(products), max(products))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = I.coerce(other)
        assert not other.lo <= 0 <= other.hi
        return self*I(1/other.hi, 1/other.lo)

    def square(self):
        lower = 0 if self.lo <= 0 <= self.hi else min(self.lo**2, self.hi**2)
        return I(F(lower), max(self.lo**2, self.hi**2))

    def abs_upper(self):
        return max(abs(self.lo), abs(self.hi))

    def is_zero(self):
        return self.lo == self.hi == 0


@lru_cache(maxsize=None)
def rational_root(value):
    """Enclose sqrt(value) on a fixed rational grid, using no float."""
    value = F(value)
    assert value >= 0
    scaled = value.numerator*ROOT_SCALE**2
    integer = math.isqrt(scaled//value.denominator)
    lo = F(integer, ROOT_SCALE)
    hi = lo if integer*integer*value.denominator == scaled else F(integer+1, ROOT_SCALE)
    assert lo*lo <= value <= hi*hi
    return I(lo, hi)


def interval_root(value):
    value = I.coerce(value)
    assert value.lo >= 0
    return I(rational_root(value.lo).lo, rational_root(value.hi).hi)


ZERO = I.point(0)


def trim(poly):
    while len(poly) > 1 and poly[-1].is_zero():
        poly.pop()
    return poly


def add(p, q):
    result = [ZERO]*max(len(p), len(q))
    for index, value in enumerate(p):
        result[index] = result[index]+value
    for index, value in enumerate(q):
        result[index] = result[index]+value
    return trim(result)


def scale(p, factor):
    return trim([value*factor for value in p])


def multiply(p, q):
    result = [ZERO]*(len(p)+len(q)-1)
    for i, first in enumerate(p):
        if first.is_zero():
            continue
        for j, second in enumerate(q):
            if not second.is_zero():
                result[i+j] = result[i+j]+first*second
    return trim(result)


def power(p, exponent):
    result = [I.point(1)]
    for _ in range(exponent):
        result = multiply(result, p)
    return result


def derivative(p):
    return [p[index]*index for index in range(1, len(p))] or [ZERO]


def bernstein(poly):
    """Interval coefficients in the Bernstein basis on the whole [-1,1]."""
    degree = len(poly)-1
    # Compose a=2x-1 with exact binomial coefficients.
    unit = [sum((poly[j]*(math.comb(j, k)*2**k*(-1)**(j-k))
                 for j in range(k, degree+1)), ZERO) for k in range(degree+1)]
    return [sum((unit[j]*F(math.comb(k, j), math.comb(degree, j))
                 for j in range(k+1)), ZERO) for k in range(degree+1)]


def envelope(poly):
    coefficients = bernstein(poly)
    return I(min(value.lo for value in coefficients),
             max(value.hi for value in coefficients))


def frozen_trial(cutoff):
    coefficients, energy, _, _ = proposal.ground_state(cutoff, 1.)
    coefficients = coefficients/coefficients[0]
    trial = {}
    for label, coefficient in zip(proposal.labels(cutoff), coefficients):
        # This is a new exact rational trial, not an interval assertion
        # about the eigensolver's unknown error. Its residual is checked.
        trial[label] = (F(0) if abs(coefficient) < 1e-16
                        else F(format(float(coefficient), '.16g')))
    trial[0, 0, 0] = F(1)
    energy = F(format(float(energy), '.16g'))
    record = '\n'.join(f'{n},{m},{k}:{value}' for (n, m, k), value in sorted(trial.items()))
    digest = hashlib.sha256((record+'\nE:'+str(energy)).encode('ascii')).hexdigest()
    return trial, energy, digest


@lru_cache(maxsize=None)
def raising(n, k):
    return rational_root(F((n-k+1)*(n+k+2), 4*(n+1)*(n+2)))


@lru_cache(maxsize=None)
def mixing(n, m, ell):
    radicand = F(ell*ell*((n+1)**2-ell*ell)*((m+1)**2-ell*ell),
                  4*(2*ell-1)*(2*ell+1))
    return -rational_root(radicand)


def physical_action(trial, cutoff):
    """Exact interval enclosure of (H0+2-a-b)p, including every halo mode."""
    result = {label: ZERO for label in proposal.labels(cutoff+1)}
    for (n, m, k), coefficient in trial.items():
        if not coefficient:
            continue
        diagonal = F(n*(n+2)+m*(m+2)+2)-F(k*(k+1), 2)
        result[n, m, k] = result[n, m, k]+diagonal*coefficient
        if k < min(n, m):
            result[n, m, k+1] = result[n, m, k+1]+mixing(n, m, k+1)*coefficient
        if k:
            result[n, m, k-1] = result[n, m, k-1]+mixing(n, m, k)*coefficient
        for label, value in (((n+1, m, k), raising(n, k)),
                             ((n, m+1, k), raising(m, k))):
            result[label] = result[label]-value*coefficient
        if n > k:
            result[n-1, m, k] = result[n-1, m, k]-raising(n-1, k)*coefficient
        if m > k:
            result[n, m-1, k] = result[n, m-1, k]-raising(m-1, k)*coefficient
    return result


def norm_l2(vector):
    return interval_root(sum((I.coerce(value).square() for value in vector.values()), ZERO))


def norm_x2(vector, remove_vacuum=False):
    """sum_(n,m) 2^(n+m) ||(c_nmk)_k||_2; Q removes only (0,0)."""
    blocks = {}
    for (n, m, k), value in vector.items():
        if remove_vacuum and n == m == 0:
            continue
        blocks[n, m] = blocks.get((n, m), ZERO)+I.coerce(value).square()
    return sum((interval_root(value)*2**(n+m)
                for (n, m), value in blocks.items()), ZERO)


def gegenbauer(degree, parameter):
    result = [[I.point(1)]]
    if degree:
        result.append([ZERO, I.point(2*parameter)])
    for n in range(1, degree):
        first = scale([ZERO]+result[n], F(2*(n+parameter), n+1))
        second = scale(result[n-1], -F(n+2*parameter-1, n+1))
        result.append(add(first, second))
    return result


def marginal_polynomial(trial, cutoff):
    """Enclose the exact Haar marginal of p^2, with p_000=1, not ||p||=1."""
    result = [ZERO]
    for k in range(cutoff+1):
        polynomials = gegenbauer(cutoff-k, k+1)
        normalized = []
        for degree, poly in enumerate(polynomials):
            norm = F(math.factorial(degree+2*k+1),
                     4**k*math.factorial(degree)*(degree+k+1)*math.factorial(k)**2)
            normalized.append([coefficient/rational_root(norm) for coefficient in poly])
        factor = power([I.point(1), ZERO, I.point(-1)], k)
        for m in range(k, cutoff+1):
            row = [ZERO]
            for n in range(k, cutoff+1):
                row = add(row, scale(normalized[n-k], trial[n, m, k]))
            result = add(result, multiply(factor, multiply(row, row)))
    return result


def display(name, value):
    value = I.coerce(value)
    # Decimal displays are informational. Assertions use exact Fractions.
    print(f'{name}: [{float(value.lo):.14g}, {float(value.hi):.14g}]', flush=True)


def representation_controls():
    """Small exact controls independent of the proposed ground vector."""
    root = rational_root(F(2))
    assert root.lo**2 < 2 < root.hi**2 and root.hi-root.lo == F(1, ROOT_SCALE)
    assert rational_root(F(4)) == I.point(2)
    negative, positive = I(F(-2), F(-1)), I(F(3), F(4))
    assert negative*positive == I(F(-8), F(-3))
    assert negative/positive == I(F(-2, 3), F(-1, 4))
    assert negative.square() == I(F(1), F(4))
    assert I(F(-1), F(2)).square() == I(F(0), F(4))
    assert bernstein([I.point(3)]) == [I.point(3)]
    assert bernstein([I.point(1), ZERO, I.point(-1)]) == [ZERO, I.point(2), ZERO]

    vacuum = {(0, 0, 0): F(1)}
    action = physical_action(vacuum, 0)
    assert action[0, 0, 0] == I.point(2)
    assert action[1, 0, 0] == action[0, 1, 0] == I.point(F(-1, 2))
    assert all(value.is_zero() for label, value in action.items()
               if label not in ((0, 0, 0), (1, 0, 0), (0, 1, 0)))
    test = {label: F(int(label == (1, 1, 1))) for label in proposal.labels(1)}
    rho = marginal_polynomial(test, 1)
    expected = (F(4, 3), F(0), F(-4, 3))
    assert len(rho) == 3
    assert all(value.lo <= target <= value.hi for value, target in zip(rho, expected))

    haar = marginal_polynomial(vacuum, 0)
    haar_numerator = add(multiply(derivative(haar), derivative(haar)),
                         scale(multiply(haar, derivative(derivative(haar))), -1))
    assert envelope(haar_numerator) == ZERO
    assert not envelope(haar_numerator).lo > 0
    print('PASS exact roots, signed interval arithmetic, Bernstein basis, vacuum '
          'action and the (1,1,1) marginal 4(1-a^2)/3. The Haar trial has zero '
          'curvature numerator and cannot pass the strict sign test; this is '
          'not a claim about the presence or absence of a free spectral gap.', flush=True)


def certify(cutoff=8):
    representation_controls()
    trial, energy, digest = frozen_trial(cutoff)
    print(f'Exact rational trial N={cutoff}; nonzero={sum(bool(c) for c in trial.values())}; '
          f'sha256={digest}', flush=True)
    action = physical_action(trial, cutoff)
    residual = {label: value-energy*trial.get(label, F(0)) for label, value in action.items()}
    norm = norm_l2(trial)
    residual_norm = norm_l2(residual)
    energy_error = residual_norm/norm
    norm_squared = sum((value*value for value in trial.values()), F(0))
    rayleigh = sum((action[label]*value for label, value in trial.items()), ZERO)/norm_squared
    halo = {label: value for label, value in residual.items()
            if label[0] > cutoff or label[1] > cutoff}
    assert trial[0, 0, 0] == 1 and norm.lo >= 1
    assert energy > 0 and energy+energy_error.hi < 3 and rayleigh.hi < 2
    display('trial energy', energy)
    display('Rayleigh quotient', rayleigh)
    display('L2 trial norm', norm)
    display('full L2 residual including halo', residual_norm)
    display('omitted-mode L2 residual', norm_l2(halo))
    display('delta_E bound', I.point(energy_error.hi))

    px, qpx, qrx = norm_x2(trial), norm_x2(trial, True), norm_x2(residual, True)
    display('||p||_X2', px)
    display('||Qp||_X2', qpx)
    display('||Qr||_X2 including halo', qrx)
    rho = marginal_polynomial(trial, cutoff)
    rho1, rho2 = derivative(rho), derivative(derivative(rho))
    numerator = add(multiply(rho1, rho1), scale(multiply(rho, rho2), -1))
    bounds = [envelope(poly) for poly in (rho, rho1, rho2)]
    numerator_bounds = envelope(numerator)
    numerator_slope = envelope(derivative(numerator))
    assert bounds[0].lo > 0 and numerator_bounds.lo > 0
    print(f'Exact marginal degrees R={len(rho)-1}, numerator={len(numerator)-1}', flush=True)
    for name, bound in zip(('R_p', "R_p'", "R_p''"), bounds):
        display(name+' Bernstein envelope', bound)
    display('N_p Bernstein envelope', numerator_bounds)
    display("N_p' Bernstein envelope", numerator_slope)

    # Analytic inputs, to be checked in the companion proof:
    # E0<=2, ||(H0+2-E0)^-1 Q||_X2<=1/3, ||a+b||_X2<=5/2,
    # hence the inverse norm is <=2. Both p and f have vacuum coefficient1.
    # The j=0,1,2 marginal bilinear norm bounds are (1,75/8,525/4).
    eta = 2*(energy_error.hi*qpx.hi+qrx.hi)
    assert qpx.hi+eta < F('.9')
    m0, m1, m2 = (bound.abs_upper() for bound in bounds)
    # Simple rational inequalities suitable for quotation in the proof.
    assert px.hi < F('1.9') and qpx.hi < F('.9')
    assert qrx.hi < F('1e-8') and energy_error.hi < F('1e-10')
    assert numerator_bounds.lo > F('.018') and bounds[0].lo > F('.5')
    assert m0 < F('1.91') and m1 < F('1.17') and m2 < F('.64')

    def transfer(name, vector_error):
        constants = (F(1), F(75, 8), F(525, 4))
        errors = [constant*(2*px.hi*vector_error+vector_error*vector_error)
                  for constant in constants]
        e0, e1, e2 = errors
        numerator_error = 2*m1*e1+e1*e1+m0*e2+m2*e0+e0*e2
        remaining = numerator_bounds.lo-numerator_error
        curvature_upper = -remaining/(2*(m0+e0)**2)
        display(name+' ||f-p||_X2 bound', I.point(vector_error))
        for index, error in enumerate(errors):
            display(name+f' marginal C{index} error', I.point(error))
        display(name+' numerator error', I.point(numerator_error))
        display(name+' remaining numerator margin', I.point(remaining))
        display(name+' latitude log-amplitude curvature upper bound', I.point(curvature_upper))
        assert bounds[0].lo > e0 and remaining > 0
        assert curvature_upper <= -F(1, 1000)

    transfer('ground bridge', eta)
    # Additional companion-proof input for the vacuum-aligned scalar
    # rescaling F_t=c^-2 exp(t E0) exp(-t H)1 of Haar preparation:
    # ||F_t-f_ground||_X2 <= 952*exp(-29) for every t>=30.
    # Its marginal log-curvature equals that of normalized preparation.
    # The Taylor partial sum is an exact LOWER bound on exp(29), so
    # dividing 952 by it gives an exact UPPER bound on the late tail.
    exp_lower = sum((F(29**k, math.factorial(k)) for k in range(101)), F(0))
    late_tail = F(952)/exp_lower
    display('rational late-time tail upper bound', I.point(late_tail))
    transfer('all t>=30 bridge', eta+late_tail)
    print('PASS exact interval residual and whole-interval Bernstein bounds. With '
          'the explicitly stated X2 inverse, marginal-derivative and late-preparation '
          'theorems, the arithmetic certifies v<=-1/1000 for the fixed-system '
          'ground marginal and every t>=30. The floating solver only selected '
          'the rational trial; no continuum Yang--Mills gap follows.', flush=True)
    return {'trial': trial, 'eta': eta, 'norm_q_upper': qpx.hi+eta,
            'rho_bounds': bounds, 'numerator_lower': numerator_bounds.lo,
            'trial_x_upper': px.hi}


if __name__ == '__main__':
    certify()
