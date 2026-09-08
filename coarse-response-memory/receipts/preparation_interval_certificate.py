"""Validated compact-time preparation on the supplied two-plaquette system.

Floating spectral values propose rational Chebyshev curves with Haar
coefficient exactly one. Exact interval full-halo residuals, contractive
X2 comparison, and bivariate Bernstein bounds validate whole time/latitude
rectangles. The initial Taylor and ground certificates supply the two
ends. Analytic positivity, contraction and marginal derivative estimates
are the stated companion-proof inputs, not inferred from this arithmetic.
"""

from __future__ import annotations

from fractions import Fraction as F
from functools import lru_cache
import hashlib
import math

import numpy as np

import ground_marginal_certificate as exact
import initial_preparation_certificate as initial


I, ZERO = exact.I, exact.ZERO
VACUUM = (0, 0, 0)


def vector_sum(rows, weights):
    result = {}
    for row, weight in zip(rows, weights):
        for label, coefficient in row.items():
            result[label] = result.get(label, F(0))+weight*coefficient
    return {label: value for label, value in result.items() if value}


def endpoint(rows, side):
    return vector_sum(rows, [side**j for j in range(len(rows))])


def distance(first, second):
    labels = set(first)|set(second)
    delta = {label: I.coerce(first.get(label, F(0)))-I.coerce(second.get(label, F(0)))
             for label in labels}
    assert delta.get(VACUUM, ZERO).is_zero()
    return exact.norm_x2(delta, True).hi


def chebyshev_derivative(rows, width):
    result = [{} for _ in range(max(1, len(rows)-1))]
    for j in range(1, len(rows)):
        for index in range(j-1, -1, -2):
            factor = F(2, 1)/width*(j if index == 0 else 2*j)
            for label, value in rows[j].items():
                result[index][label] = result[index].get(label, F(0))+factor*value
    return result


def residual_bound(rows, width, cutoff):
    """Uniform X2 residual of p'+Hp-(Hp)_000*p, including halo modes."""
    degree = len(rows)-1
    result = [{} for _ in range(2*degree+1)]

    def put(index, label, value):
        result[index][label] = result[index].get(label, ZERO)+value

    actions = [exact.physical_action(row, cutoff) for row in rows]
    for j, row in enumerate(actions):
        for label, value in row.items():
            if not value.is_zero():
                put(j, label, value)
    for j, row in enumerate(chebyshev_derivative(rows, width)):
        for label, value in row.items():
            put(j, label, I.point(value))
    # T_i*T_j=(T_(i+j)+T_|i-j|)/2, also when i or j is zero.
    for i, action in enumerate(actions):
        scalar = action[VACUUM]
        if scalar.is_zero():
            continue
        for j, row in enumerate(rows):
            for label, coefficient in row.items():
                value = -scalar*coefficient/2
                put(i+j, label, value)
                put(abs(i-j), label, value)
    assert all(row.get(VACUUM, ZERO).is_zero() for row in result)
    return sum((exact.norm_x2(row, True).hi for row in result), F(0))


def proposal_factory(cutoff, degree):
    labels, _, kinetic, multiplication = exact.proposal.matrices(cutoff)
    energies, vectors = np.linalg.eigh(kinetic+2*np.eye(len(labels))-multiplication)
    source = vectors[0, :]
    angles = (np.arange(degree+1)+.5)*math.pi/(degree+1)
    nodes = np.cos(angles)
    transform = 2*np.cos(np.arange(degree+1)[:, None]*angles)/(degree+1)
    transform[0] /= 2

    def propose(start, end):
        times = float(start)+(nodes+1)*float(end-start)/2
        values = (vectors@(np.exp(-(energies-energies[0])[:, None]*times)
                           *source[:, None])).T
        values /= values[:, 0, None]
        coefficients = transform@values
        coefficients[:, 0] = 0
        coefficients[0, 0] = 1
        rows = []
        for row in coefficients:
            rows.append({label: F(format(float(value), '.17g'))
                         for label, value in zip(labels, row) if abs(value) >= 1e-18})
        rows[0][VACUUM] = F(1)
        for row in rows[1:]:
            row.pop(VACUUM, None)
        assert endpoint(rows, -1)[VACUUM] == endpoint(rows, 1)[VACUUM] == 1
        return rows

    return propose


@lru_cache(maxsize=None)
def shifted_chebyshev(degree):
    """Exact coefficients of T_j(2u-1), u in [0,1]."""
    result = [[F(1)]]
    if degree:
        result.append([F(-1), F(2)])
    for j in range(1, degree):
        value = [F(0)]*(j+2)
        for k, coefficient in enumerate(result[j]):
            value[k] -= 2*coefficient
            value[k+1] += 4*coefficient
        for k, coefficient in enumerate(result[j-1]):
            value[k] -= coefficient
        result.append(value)
    return result


def power_rows(rows):
    result = [{} for _ in rows]
    for row, polynomial in zip(rows, shifted_chebyshev(len(rows)-1)):
        for j, factor in enumerate(polynomial):
            for label, value in row.items():
                result[j][label] = result[j].get(label, F(0))+factor*value
    return result


def p_add(first, second, factor=1):
    result = dict(first)
    for key, value in second.items():
        result[key] = result.get(key, ZERO)+value*factor
        if result[key].is_zero():
            del result[key]
    return result


def p_multiply(first, second):
    result = {}
    for (i, j), value in first.items():
        for (k, ell), other in second.items():
            key = (i+k, j+ell)
            result[key] = result.get(key, ZERO)+value*other
    return {key: value for key, value in result.items() if not value.is_zero()}


def p_derivative(poly):
    return {(i, j-1): value*j for (i, j), value in poly.items() if j}


@lru_cache(maxsize=None)
def normalized_gegenbauer(cutoff, k):
    result = []
    for degree, poly in enumerate(exact.gegenbauer(cutoff-k, k+1)):
        norm = F(math.factorial(degree+2*k+1),
                 4**k*math.factorial(degree)*(degree+k+1)*math.factorial(k)**2)
        # Enclose sqrt(1/norm), avoiding coprime denominators produced
        # by inverting individually rounded square-root endpoints.
        factor = exact.rational_root(1/norm)
        result.append([coefficient*factor for coefficient in poly])
    return result


def marginal_polynomial(rows, cutoff):
    """Bivariate powers u^i a^j for the complete conditional marginal."""
    time = power_rows(rows)
    result = {}
    for k in range(cutoff+1):
        radial = normalized_gegenbauer(cutoff, k)
        for m in range(k, cutoff+1):
            row = {}
            for n in range(k, cutoff+1):
                for i, coefficients in enumerate(time):
                    value = coefficients.get((n, m, k), F(0))
                    if not value:
                        continue
                    for j, factor in enumerate(radial[n-k]):
                        if not factor.is_zero():
                            key = (i, j)
                            row[key] = row.get(key, ZERO)+value*factor
            square = p_multiply(row, row)
            # Multiply by (1-a^2)^k without changing the time variable.
            for j in range(k+1):
                factor = (-1)**j*math.comb(k, j)
                shifted = {(i, ell+2*j): value for (i, ell), value in square.items()}
                result = p_add(result, shifted, factor)
    return result


def rectangle_envelope(poly):
    """Exact bivariate Bernstein hull on u in [0,1], a in [-1,1]."""
    if not poly:
        return ZERO
    nt = max(i for i, _ in poly)
    na = max(j for _, j in poly)
    spatial = []
    for i in range(nt+1):
        spatial.append(exact.bernstein([poly.get((i, j), ZERO) for j in range(na+1)]))
    lower, upper = None, None
    for k in range(nt+1):
        factors = [F(math.comb(k, i), math.comb(nt, i)) for i in range(k+1)]
        for j in range(na+1):
            value = sum((spatial[i][j]*factors[i] for i in range(k+1)), ZERO)
            lower = value.lo if lower is None else min(lower, value.lo)
            upper = value.hi if upper is None else max(upper, value.hi)
    return I(lower, upper)


def transfer(bounds, numerator_lower, trial_norm, error):
    constants = (F(1), F(75, 8), F(525, 4))
    e0, e1, e2 = [constant*(2*trial_norm*error+error*error) for constant in constants]
    m0, m1, m2 = [bound.abs_upper() for bound in bounds]
    loss = 2*m1*e1+e1*e1+m0*e2+m2*e0+e0*e2
    margin = numerator_lower-loss
    assert bounds[0].lo > e0 and margin > 0
    return margin, -margin/(2*(m0+e0)**2)


def arithmetic_controls():
    assert shifted_chebyshev(2) == [[F(1)], [F(-1), F(2)], [F(1), F(-8), F(8)]]
    # The Bernstein hull of 1+u+a^2 is [0,3], not its exact range [1,3].
    control = {(0, 0): I.point(1), (1, 0): I.point(1), (0, 2): I.point(1)}
    assert rectangle_envelope(control) == I(F(0), F(3))
    # A constant Haar trial fails its ODE: Q residual is -M1, X norm2.
    assert residual_bound([{VACUUM: F(1)}], F(1, 4), 0) == 2
    print('PASS exact shifted-Chebyshev, rectangle-Bernstein and nonzero Haar '
          'residual controls.', flush=True)


def certify(cutoff=8, degree=12, width=F(1, 4), stop=F(4)):
    assert isinstance(width, (int, F)) and isinstance(stop, (int, F))
    assert width > 0 and stop >= initial.T0
    arithmetic_controls()
    initial.certify()
    data = initial.initial_normalized_data()
    propose = proposal_factory(cutoff, degree)
    current, previous = data['time'], data['coefficients']
    error = data['error_x']
    digest = hashlib.sha256()
    smallest_margin, largest_error, index = None, F(0), 0
    while current < stop:
        end = min(current+width, stop)
        rows = propose(current, end)
        for j, row in enumerate(rows):
            digest.update((f'{current},{end},{j}:'+str(sorted(row.items()))+'\n').encode('ascii'))
        jump = distance(endpoint(rows, -1), previous)
        entry_error = error+jump
        qnorm = sum((exact.norm_x2(row, True).hi for row in rows), F(0))
        assert qnorm < 1
        residual = residual_bound(rows, end-current, cutoff)
        # D+||g-y|| <= -||g-y||/4 + ||residual||. The maximum
        # of the entry error and 4*residual bounds the whole interval.
        error = max(entry_error, 4*residual)
        rho = marginal_polynomial(rows, cutoff)
        first, second = p_derivative(rho), p_derivative(p_derivative(rho))
        numerator = p_add(p_multiply(first, first), p_multiply(rho, second), -1)
        bounds = [rectangle_envelope(poly) for poly in (rho, first, second)]
        nbound = rectangle_envelope(numerator)
        margin, curvature = transfer(bounds, nbound.lo, 1+qnorm, error)
        smallest_margin = margin if smallest_margin is None else min(smallest_margin, margin)
        largest_error = max(largest_error, error)
        print(f'slab {index}: [{current},{end}], ||Qtrial||X<{float(qnorm):.12g}, '
              f'residualX<{float(residual):.5g}, jump<{float(jump):.5g}, '
              f'errorX<{float(error):.5g}, Bernstein N>{float(nbound.lo):.12g}, '
              f'remaining N>{float(margin):.12g}, v<{float(curvature):.12g}', flush=True)
        previous, current, index = endpoint(rows, 1), end, index+1
    print(f'Rational time-trial sha256={digest.hexdigest()}; slabs={index}; '
          f'maximum certified Xerror<{float(largest_error):.12g}', flush=True)

    ground = exact.certify(cutoff)
    endpoint_to_trial = distance(previous, ground['trial'])
    # Compare the exact heat trajectory to the exact ground, contract
    # in X2, then compare back to the certified ground trial. This uses
    # the separately proved ||Qground||X<.9 and actual s(g)>=0.
    assert ground['norm_q_upper'] < F('.9')
    ground_distance = error+endpoint_to_trial+ground['eta']
    future_error = ground_distance+ground['eta']
    margin, curvature = transfer(ground['rho_bounds'], ground['numerator_lower'],
                                 ground['trial_x_upper'], future_error)
    exact.display('terminal distance to exact ground', I.point(ground_distance))
    exact.display(f'all t>={stop} remaining numerator margin', I.point(margin))
    exact.display(f'all t>={stop} curvature upper bound', I.point(curvature))
    print('PASS exact arithmetic for all-latitude concavity on the compact '
          'preparation window and its contractive ground tail. Together with '
          'the certified initial layer and the companion positivity/contraction '
          'theorems, this covers every t>0 at kappa=lambda=1 on this fixed '
          'two-plaquette system. No continuum or full-field mass gap is claimed.', flush=True)


if __name__ == '__main__':
    certify()
