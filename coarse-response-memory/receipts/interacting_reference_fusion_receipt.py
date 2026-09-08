"""Controls for interacting-reference-and-spectral-product-control.md.

Exact Fraction Fourier arithmetic checks the first variation of a forbidden
Haar product channel and the columns of the proposed drift preconditioner.
The numerical branch diagonalizes the actual ground-state Schrodinger
operator H_eps = -d^2 - eps*cos(theta) + eps^2*sin(theta)^2 in two parity
Galerkin bases. Its positive ground is exp(eps*cos(theta)); the corresponding
Doob operator is L_eps = -d^2 + 2*eps*sin(theta)*d.

The cutoff comparisons are floating-point diagnostics, not certified tails.
They do not prove analytic perturbation, an interacting gap theorem, or a
continuum limit. The companion note supplies the analytic argument.
"""

from fractions import Fraction as F
import math

import numpy as np


ZERO = (F(0), F(0))


def cmul(a, b):
    return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def put(poly, mode, value):
    old = poly.get(mode, ZERO)
    new = (old[0]+value[0], old[1]+value[1])
    if new == ZERO:
        poly.pop(mode, None)
    else:
        poly[mode] = new


def scale(poly, factor):
    return {n: (factor*c[0], factor*c[1]) for n, c in poly.items()
            if factor and c != ZERO}


def add(*polys):
    result = {}
    for poly in polys:
        for n, c in poly.items():
            put(result, n, c)
    return result


def multiply(*polys):
    result = {0: (F(1), F(0))}
    for poly in polys:
        next_poly = {}
        for n, c in result.items():
            for m, d in poly.items():
                put(next_poly, n+m, cmul(c, d))
        result = next_poly
    return result


def cosine(n):
    assert n > 0
    return {n: (F(1, 2), F(0)), -n: (F(1, 2), F(0))}


def sine(n):
    assert n > 0
    return {n: (F(0), F(-1, 2)), -n: (F(0), F(1, 2))}


def derivative(poly):
    return {n: (-n*c[1], n*c[0]) for n, c in poly.items() if n}


def kinetic(poly):
    return {n: (n*n*c[0], n*n*c[1]) for n, c in poly.items() if n}


def mean(poly):
    real, imaginary = poly.get(0, ZERO)
    assert imaginary == 0
    return real


def exact_first_variation():
    f0 = sine(1)
    f1 = scale(sine(2), F(-1, 3))
    g0 = cosine(3)
    g1 = add(scale(cosine(2), F(-3, 5)),
             scale(cosine(4), F(-3, 7)))

    def perturbation(poly):
        return scale(multiply(sine(1), derivative(poly)), F(2))

    assert add(kinetic(f1), scale(f1, F(-1)), perturbation(f0)) == {}
    assert add(kinetic(g1), scale(g1, F(-9)), perturbation(g0)) == {}
    assert mean(multiply(f0, perturbation(f0))) == 0
    assert mean(multiply(g0, perturbation(g0))) == 0
    assert mean(multiply(f0, f0, g0)) == 0
    assert mean(multiply(f0, f0)) == F(1, 2)
    assert mean(multiply(g0, g0)) == F(1, 2)
    terms = (
        mean(scale(multiply(f0, f1, g0), F(2))),
        mean(multiply(f0, f0, g1)),
        mean(scale(multiply(cosine(1), f0, f0, g0), F(2))),
    )
    assert terms == (F(1, 6), F(3, 20), F(-1, 4))
    assert sum(terms) == F(1, 15)
    print('Exact unnormalized overlap derivative: '
          + ' + '.join(map(str, terms)) + ' = 1/15')
    print('Weighted unit-norm derivative: 2*sqrt(2)/15 = '
          f'{2*math.sqrt(2)/15:.12f}')


def exact_drift_columns():
    # D = 2*K^{-1}*Q_Haar*Gamma(cos(theta), .), at eps=1.
    # The norm is sum_{n != 0} n^2*|fhat_n|; remove constants first.
    w = cosine(1)
    ratios = []
    for n in range(-20, 21):
        if not n:
            continue
        mode = {n: (F(1), F(0))}
        gamma = scale(multiply(derivative(w), derivative(mode)), F(2))
        inverse = {m: (c[0]/(m*m), c[1]/(m*m))
                   for m, c in gamma.items() if m}
        assert all(c[1] == 0 for c in inverse.values())
        ratio = sum(m*m*abs(c[0]) for m, c in inverse.items())/(n*n)
        expected = F(1) if abs(n) == 1 else F(2, abs(n))
        assert ratio == expected
        ratios.append(ratio)
    assert max(ratios) == 1
    print('Exact drift-column controls n=+/-1,...,+/-20: '
          'ratios 1 for |n|=1 and 2/|n| otherwise; maximum 1.')
    print('The all-mode norm formula and the sufficient |eps|<1 '
          'Neumann condition require the companion proof.')


def parity_basis(theta, cutoff, odd):
    modes = np.arange(1 if odd else 0, cutoff+1)
    angles = modes[:, None]*theta[None, :]
    if odd:
        basis = math.sqrt(2)*np.sin(angles)
        prime = math.sqrt(2)*modes[:, None]*np.cos(angles)
    else:
        basis = math.sqrt(2)*np.cos(angles)
        prime = -math.sqrt(2)*modes[:, None]*np.sin(angles)
        basis[0] = 1
    return modes, basis, prime


def spectral_control(eps, cutoff, grid_size=4096):
    theta = 2*np.pi*np.arange(grid_size)/grid_size
    # All matrix integrands have degree <= 2*cutoff+2. The trapezoidal
    # rule is therefore exact for this finite trigonometric matrix in
    # exact arithmetic. Subsequent weighted readouts remain numerical.
    assert grid_size > 2*cutoff+2
    potential = -eps*np.cos(theta)+eps*eps*np.sin(theta)**2
    rho = np.exp(2*eps*np.cos(theta))
    rho /= np.mean(rho)
    ground = np.sqrt(rho)
    states = []
    for odd, target in ((True, 1), (False, 3)):
        modes, basis, prime = parity_basis(theta, cutoff, odd)
        matrix = np.diag(modes.astype(float)**2)
        matrix += (basis*potential) @ basis.T/grid_size
        eigenvalues, vectors = np.linalg.eigh(matrix)
        row = int(np.flatnonzero(modes == target)[0])
        branch = int(np.argmax(np.abs(vectors[row])))
        vector = vectors[:, branch]
        if vector[row] < 0:
            vector = -vector
        phi = vector @ basis
        phi_prime = vector @ prime
        f = phi/ground
        f_prime = (phi_prime+eps*np.sin(theta)*phi)/ground
        assert abs(np.mean(rho*f*f)-1) < 2e-12
        assert np.linalg.norm(matrix @ vector-eigenvalues[branch]*vector) < 2e-11
        states.append((eigenvalues[branch], f, f_prime, phi))
    ef, f, f_prime, phi_f = states[0]
    eg, g, _, phi_g = states[1]
    overlap = np.mean(rho*f*f*g)
    assert abs(overlap-np.mean(phi_f*phi_f*phi_g/ground)) < 2e-14
    gamma_channel = np.mean(rho*g*f_prime*f_prime)
    assert abs(gamma_channel-(ef-eg/2)*overlap) < 2e-10
    triangle = math.sqrt(eg)-2*math.sqrt(ef)
    cross_excess = abs(ef-eg/2)-ef
    if eps == 0:
        assert abs(overlap) < 2e-13
        assert abs(ef-1) < 2e-12 and abs(eg-9) < 2e-12
    else:
        assert overlap > 0 and triangle > .9 and cross_excess > 2
    return ef, eg, overlap, triangle


def main():
    exact_first_variation()
    exact_drift_columns()
    print('\nFloating-point actual-operator controls (not tail certificates)')
    print('cutoff   eps           E_f             E_g       overlap/eps'
          '     sqrt(E_g)-2sqrt(E_f)')
    results = {}
    for cutoff in (12, 20):
        for eps in (0., .05, .02, .01):
            result = spectral_control(eps, cutoff)
            results[cutoff, eps] = result
            ef, eg, overlap, triangle = result
            ratio = overlap/eps if eps else 0.
            print(f'{cutoff:6d} {eps:6.3f} {ef:15.10f} {eg:15.10f} '
                  f'{ratio:17.10f} {triangle:22.10f}')
    for eps in (0., .05, .02, .01):
        assert max(abs(a-b) for a, b in
                   zip(results[12, eps], results[20, eps])) < 2e-10
    target = 2*math.sqrt(2)/15
    errors = [abs(results[20, eps][2]/eps-target) for eps in (.05, .02, .01)]
    assert errors[0] > errors[1] > errors[2]
    assert errors[-1] < 1e-4
    print('\nPASS: exact first variation, drift columns, zero-coupling control, '
          'weighted normalization, and two-cutoff diagnostics.')
    print('Finite cutoffs do not certify tails. The analytic obstruction '
          'does not assert a Yang-Mills gap or a continuum construction.')


if __name__ == '__main__':
    main()
