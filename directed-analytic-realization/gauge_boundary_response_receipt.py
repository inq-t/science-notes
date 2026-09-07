"""Finite polynomial checks for boundary response and its Gauss completion.

Fourier products retain every generated mode: this is not a Galerkin gauge
theory. No files are written. Analytic convergence, state existence and
continuum Yang--Mills require the proofs and qualifications in the notes.

Field pairings use normalized torus-average measure and integer momenta.
They check identities after removing the common volume factor, not the
L**3 normalization of the integrated field pairing in the canonical note.
"""

from __future__ import annotations

from fractions import Fraction as F
import math
import random
import sys

sys.dont_write_bytecode = True
from nonlinear_response_receipt import (  # noqa: E402
    close, combine, cross, dot, mm, simpson, transpose,
)


ZERO = (0, 0, 0)


def neg(k):
    return tuple(-x for x in k)


def plus(k, l):
    return tuple(x+y for x, y in zip(k, l))


def norm2(k):
    return sum(x*x for x in k)


def blank():
    return [[0j]*3 for _ in range(3)]


def field_add(*terms):
    out = {}
    for scale, field in terms:
        for k, matrix in field.items():
            dest = out.setdefault(k, blank())
            for i in range(3):
                for c in range(3):
                    dest[i][c] += scale*matrix[i][c]
    return out


def pair(a, b):
    value = 0j
    for k, matrix in a.items():
        if neg(k) in b:
            value += sum(dot(row, other)
                         for row, other in zip(matrix, b[neg(k)]))
    close("real field pairing", value.imag, 0, 1e-8)
    return value.real


def color_pair(a, b):
    value = sum(dot(v, b[neg(k)]) for k, v in a.items() if neg(k) in b)
    close("real color pairing", value.imag, 0, 1e-8)
    return value.real


def derivative(phi):
    return {k: [[1j*k[i]*v[c] for c in range(3)] for i in range(3)]
            for k, v in phi.items()}


def split_field(field):
    phi = {k: [-1j*sum(k[i]*matrix[i][c] for i in range(3))/norm2(k)
               for c in range(3)]
           for k, matrix in field.items() if k != ZERO}
    longitudinal = derivative(phi)
    return field_add((1, field), (-1, longitudinal)), phi, longitudinal


def response_k(field):
    transverse, _, _ = split_field(field)
    return {k: [[math.sqrt(norm2(k))*v for v in row] for row in matrix]
            for k, matrix in transverse.items()}


def bracket(field, phi):
    out = {}
    for k, matrix in field.items():
        for l, v in phi.items():
            dest = out.setdefault(plus(k, l), blank())
            for i in range(3):
                term = cross(matrix[i], v)
                for c in range(3):
                    dest[i][c] += term[c]
    return out


def magnetic_cubic(field):
    value = 0j
    for p, ap in field.items():
        for q, aq in field.items():
            r = neg(plus(p, q))
            if r not in field:
                continue
            ar = field[r]
            for i in range(3):
                for j in range(i+1, 3):
                    curl = [1j*(p[i]*ap[j][c]-p[j]*ap[i][c])
                            for c in range(3)]
                    value += dot(curl, cross(aq[i], ar[j]))
    close("real cubic potential", value.imag, 0, 1e-8)
    return value.real


def cubic_integral(field, retain_longitudinal):
    """Integrate the trilinear magnetic polynomial by exact mode rates."""
    a, _, longitudinal = split_field(field)
    value = 0j
    for p, ap in a.items():
        if p == ZERO:
            continue
        for q, aq in a.items():
            r = neg(plus(p, q))
            if r not in a:
                continue
            ar = a[r]
            q_choices = [(aq, math.sqrt(norm2(q)))]
            r_choices = [(ar, math.sqrt(norm2(r)))]
            if retain_longitudinal:
                q_choices.append((longitudinal.get(q, blank()), 0.0))
                r_choices.append((longitudinal.get(r, blank()), 0.0))
            for bq, rq in q_choices:
                for br, rr in r_choices:
                    rate = math.sqrt(norm2(p))+rq+rr
                    for i in range(3):
                        for j in range(i+1, 3):
                            curl = [1j*(p[i]*ap[j][c]-p[j]*ap[i][c])
                                    for c in range(3)]
                            value += dot(curl, cross(bq[i], br[j]))/rate
    close("real response integral", value.imag, 0, 1e-8)
    return value.real


def cubic_response(field):
    a, phi, longitudinal = split_field(field)
    correction = field_add((1, bracket(a, phi)),
                           (0.5, bracket(longitudinal, phi)))
    return cubic_integral(a, False)-pair(response_k(a), correction)


def cubic_directional(polynomial, field, direction):
    # Exact polarization for homogeneous cubics, not a small-step derivative.
    return ((polynomial(field_add((1, field), (1, direction)))
             - polynomial(field_add((1, field), (-1, direction))))/2
            - polynomial(direction))


def rho_current(a):
    ka = response_k(a)
    out = {}
    for k, matrix in a.items():
        for l, response in ka.items():
            dest = out.setdefault(plus(k, l), [0j]*3)
            for i in range(3):
                term = cross(matrix[i], response[i])
                for c in range(3):
                    dest[c] += term[c]
    return out


def test_field():
    rng = random.Random(431)
    out = {}
    for k in [(1, 0, 0), (0, 2, 0), (1, 2, 0)]:
        matrix = [[complex(rng.randint(-7, 7), rng.randint(-7, 7))/10
                   for _ in range(3)] for _ in range(3)]
        out[k] = matrix
        out[neg(k)] = [[v.conjugate() for v in row] for row in matrix]
    # Harmonic coordinates are retained, not silently projected out.
    out[ZERO] = [[0.1, 0.2, 0.0], [0.0, -0.3, 0.1], [0.2, 0.0, 0.4]]
    return out


def check_cubic_gauge_response():
    a_full = test_field()
    omega = {(1, 0, 0): [0.2+0.3j, -0.4+0.1j, 0.1-0.2j]}
    omega[(-1, 0, 0)] = [v.conjugate() for v in omega[(1, 0, 0)]]
    ka = response_k(a_full)
    close("full-flow and Coulomb-completed response",
          cubic_response(a_full), cubic_integral(a_full, True), 1e-8)
    close("cubic Hamilton-Jacobi",
          cubic_directional(cubic_response, a_full, ka),
          magnetic_cubic(a_full), 1e-8)
    ward_correction = pair(ka, bracket(a_full, omega))
    ward_linear = cubic_directional(cubic_response, a_full, derivative(omega))
    close("full cubic Ward identity", ward_linear+ward_correction, 0, 1e-8)
    bare_transverse = lambda a: cubic_integral(a, False)
    omitted = cubic_directional(bare_transverse, a_full, derivative(omega))
    close("transverse response ignores linear gauge direction", omitted, 0, 1e-8)
    if abs(ward_correction) < 1e-4:
        raise AssertionError("Ward negative control accidentally vanished")
    print("PASS full cubic boundary response satisfies Hamilton-Jacobi and Gauss")
    print("PASS transverse-only cubic response fails the nonabelian Ward test")

    a, _, _ = split_field(a_full)
    rho = rho_current(a)
    for value in rho.get(ZERO, [0j]*3):
        close("mean-zero Gauss current", abs(value), 0, 1e-8)
    inverse = {k: [v/norm2(k) for v in values]
               for k, values in rho.items() if k != ZERO}
    long_response = derivative(inverse)
    coulomb = color_pair(rho, inverse)
    close("longitudinal norm is Coulomb energy",
          pair(long_response, long_response), coulomb, 1e-8)
    if coulomb <= 0:
        raise AssertionError("Coulomb correction must be visible in this test")
    for k, matrix in long_response.items():
        for c in range(3):
            divergence = -1j*sum(k[i]*matrix[i][c] for i in range(3))
            close("longitudinal response solves Gauss", abs(divergence-rho[k][c]),
                  0, 1e-8)
    print("PASS quartic source requires the positive Coulomb completion energy")

    harmonic = {ZERO: [[1.0, 0, 0], [0, 1.0, 0], [0, 0, 1.0]]}
    close("harmonic cubic integral", cubic_response(harmonic), 0)
    quartic = sum(dot(cross(harmonic[ZERO][i], harmonic[ZERO][j]),
                      cross(harmonic[ZERO][i], harmonic[ZERO][j]))
                  for i in range(3) for j in range(i+1, 3))/2
    close("homogeneous quartic obstruction", quartic, 1.5)
    close("harmonic normal generator", pair(response_k(harmonic),
                                            response_k(harmonic)), 0)
    print("PASS zero-mode cubic prescription leaves a nonzero quartic obstruction")


def check_positive_branch():
    for g in [-0.7, 0.3, 1.2]:
        for x, y in [(0.2, -0.3), (0.5, 0.4), (-0.7, 0.1)]:
            q = [x, y]
            n3 = [2*g*x*y/3, g*x*x/3]
            n4 = [g*g*(4*x**3+8*x*y*y)/9, g*g*8*x*x*y/9]
            close("positive cubic branch", dot(q, n3), g*x*x*y)
            close("positive quartic branch", dot(q, n4)+dot(n3, n3)/2,
                  g*g*(x**4+4*x*x*y*y)/2)
    a, alpha = 0.8, 0.3
    for t in [0.2, 1.1]:
        kernel = lambda s: ((math.exp(-a*abs(t-s))-math.exp(-a*(t+s)))
                            /(2*a)*math.exp(-alpha*s))
        integral = simpson(kernel, hi=t, steps=2000)
        integral += simpson(lambda s: kernel(t+s), hi=80-t, steps=20000)
        expected = (math.exp(-alpha*t)-math.exp(-a*t))/(a*a-alpha*alpha)
        close("weighted half-line Green integral", integral, expected, 1e-10)
        assert math.exp(alpha*t)*integral <= 1/(a*a-alpha*alpha)
    print("PASS local positive branch jets and weighted Green contraction kernel")


def check_quantum_origin_jet():
    q = [[F(1, 3), F(2, 5), F(-1, 4)],
         [F(-2, 3), F(1, 2), F(1, 7)],
         [F(3, 4), F(-1, 5), F(2, 3)]]

    def s(matrix):
        return sum(dot(row, row) for row in matrix)

    def t(matrix):
        gram = mm(matrix, transpose(matrix))
        return sum(dot(row, row) for row in gram)

    def laplacian_quartic(poly):
        result = F(0)
        for i in range(3):
            for j in range(3):
                def central(step):
                    e = [[F(0)]*3 for _ in range(3)]
                    e[i][j] = step
                    return (poly(combine((1, q), (1, e)))-2*poly(q)
                            +poly(combine((1, q), (-1, e))))/(step*step)
                result += (4*central(F(1, 2))-central(F(1)))/3
        return result

    assert laplacian_quartic(lambda x: s(x)**2) == 44*s(q)
    assert laplacian_quartic(t) == 28*s(q)
    rotation = [[F(3, 5), F(-4, 5), 0],
                [F(4, 5), F(3, 5), 0], [0, 0, -1]]
    rotated = mm(mm(rotation, q), transpose(rotation))
    assert s(rotated) == s(q) and t(rotated) == t(q)
    for eps, volume, coupling, e_unit in [
        (0.4, 0.7, 0.3, 1.2), (1.0, 2.0, -0.8, 2.1)
    ]:
        # e_unit is a dummy positive energy for checking the identity/scaling,
        # not a numerical solution of the matrix ground-state problem.
        energy = eps**(4/3)*volume**(-1/3)*abs(coupling)**(2/3)*e_unit
        kappa = 2*volume*energy/(9*eps)
        close("origin quantum equation", eps*9*kappa/(2*volume), energy)
        length = (eps/(volume*abs(coupling)))**(1/3)
        close("generated slope dilation", eps/length**2*(2*e_unit/9), kappa)
    print("PASS invariant quantum-origin jet and 44 a + 28 b coefficient identity")


if __name__ == "__main__":
    check_cubic_gauge_response()
    check_positive_branch()
    check_quantum_origin_jet()
    print("Finite checks only; no full boundary vacuum or continuum mass gap certified.")
