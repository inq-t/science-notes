"""Finite checks of opposed-response complex completions and clock geometry.

The pair carrier and canonical Green form are declared inputs. These checks
do not construct an interacting quantum field theory or a physical clock.
No files are written; matrix checks use floats, polynomial checks Fractions.
"""

from fractions import Fraction as F
import math


def mm(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def tr(a):
    return [list(row) for row in zip(*a)]


def add(*terms):
    first = terms[0][1]
    return [[sum(s*a[i][j] for s, a in terms)
             for j in range(len(first[0]))] for i in range(len(first))]


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def block(a, b, c, d):
    return [x+y for x, y in zip(a, b)]+[x+y for x, y in zip(c, d)]


def inv2(a):
    det = a[0][0]*a[1][1]-a[0][1]*a[1][0]
    assert det > 0
    return [[a[1][1]/det, -a[0][1]/det],
            [-a[1][0]/det, a[0][0]/det]]


def sqrt2(a):
    det = a[0][0]*a[1][1]-a[0][1]*a[1][0]
    assert det > 0 and a[0][0] > 0
    root = math.sqrt(det)
    scale = math.sqrt(a[0][0]+a[1][1]+2*root)
    return add((1/scale, a), (root/scale, eye(2)))


def close(name, a, b, tol=1e-10):
    if isinstance(a, list):
        assert len(a) == len(b), name
        for x, y in zip(a, b):
            close(name, x, y, tol)
    elif abs(a-b) > tol*(1+abs(a)+abs(b)):
        raise AssertionError((name, a, b))


def matrix_checks():
    p = [[2.0, 1.0], [1.0, 3.0]]
    m = [[4.0, -0.5], [-0.5, 1.5]]
    c = add((1, p), (1, m))
    z = [[0.0]*2 for _ in range(2)]
    ident = eye(2)
    df = block(ident, ident, p, add((-1, m)))
    sigma = block(z, ident, add((-1, ident)), z)
    omega = block(z, add((-1, c)), c, z)
    close("opposed Green pullback", mm(mm(tr(df), sigma), df), omega)
    g = block(p, z, z, m)
    raw = block(z, add((0.5, mm(inv2(p), c))),
                add((-0.5, mm(inv2(m), c))), z)
    close("raw skew pairing", add((2, mm(tr(raw), g))), omega)
    defect = add((1, mm(raw, raw)), (1, eye(4)))
    assert max(abs(v) for row in defect for v in row) > 0.01

    root = sqrt2(p)
    iroot = inv2(root)
    a = mm(mm(root, sqrt2(mm(mm(iroot, m), iroot))), root)
    ai = inv2(a)
    r = inv2(add((1, inv2(p)), (1, inv2(m))))
    close("geometric mean Riccati", mm(mm(a, inv2(p)), a), m)
    close("geometric mean parallel sum", mm(mm(a, inv2(c)), a), r)
    close("pair metric in response coordinates",
          mm(mm(tr(df), block(r, z, z, inv2(c))), df), g)
    jp = block(z, add((-1, ai)), a, z)
    gp = block(add((0.5, a)), z, z, add((0.5, ai)))
    close("polar complex square", mm(jp, jp), add((-1, eye(4))))
    close("polar corrected Green metric",
          add((2, mm(tr(jp), gp))), sigma)
    j0 = block(z, ident, add((-1, ident)), z)
    g0 = block(add((0.5, c)), z, z, add((0.5, c)))
    close("exchange corrected Green metric",
          add((2, mm(tr(j0), g0))), omega)
    print("PASS noncommuting Hessian pullback, polar mean and exchange completion")
    print("PASS unequal-response raw compatibility fails")


def scalar_checks():
    # Curvature is independently evaluated in original x,y coordinates.
    # At x=y, first derivatives of log(nu) vanish, so d_X^2=b^-1 d_x^2.
    slope = 0.7
    for at in [-0.2, 0.0, 0.4]:
        b = 1+slope*at
        def log_nu(x, y):
            bx, by = 1+slope*x, 1+slope*y
            return math.log((bx+by)/(2*math.sqrt(bx*by)))
        step = 0.001
        def lap(h):
            return (log_nu(at+h, at)+log_nu(at-h, at)
                    +log_nu(at, at+h)+log_nu(at, at-h)
                    -4*log_nu(at, at))/(h*h*b)
        curvature = -(4*lap(step/2)-lap(step))/6
        close("polar diagonal curvature", curvature,
              -slope*slope/(4*b**3), 1e-8)
    alpha = F(4)
    n_at_two, dn_at_two, ddn_at_two = F(10), F(13), F(12)
    fprime = dn_at_two**2+n_at_two*ddn_at_two
    assert (alpha-fprime/alpha)/2 == -F(273, 8)
    print("PASS curved polar geometry and prescribed nonlinear clock failure")


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def mv(a, x):
    return [dot(row, x) for row in a]


def outer(x, y):
    return [[a*b for b in y] for a in x]


def vec(*terms):
    return [sum(c*x[i] for c, x in terms) for i in range(len(terms[0][1]))]


def quartic_circle():
    a = [[F(2), F(1)], [F(1), F(3)]]
    c = [[F(1), F(0)], [F(0), F(2)]]
    def w4(v):
        return dot(v, mv(c, v))**2/4
    def b4(v):
        cv = mv(c, v)
        return add((dot(v, cv), c), (2, outer(cv, cv)))
    def s(x, y):
        return add((2, a), (1, b4(x)), (1, b4(y)))
    def energy(x, y):
        return (dot(x, mv(a, x))+dot(y, mv(a, y))
                +3*w4(x)+3*w4(y)+dot(x, mv(b4(y), x))/2)
    x, y = [F(1, 3), F(-2, 5)], [F(3, 7), F(4, 9)]
    xr = vec((F(3, 5), x), (-F(4, 5), y))
    yr = vec((F(4, 5), x), (F(3, 5), y))
    assert s(xr, yr) == s(x, y)
    assert energy(xr, yr) == energy(x, y) > 0

    # Exact derivative of a degree-four polynomial by two central evaluations.
    pair = x+y
    def h(v):
        return energy(v[:2], v[2:])
    gradient = []
    for i in range(4):
        def central(step):
            e = [F(0)]*4
            e[i] = step
            return (h(vec((1, pair), (1, e)))
                    -h(vec((1, pair), (-1, e))))/(2*step)
        gradient.append((4*central(F(1, 2))-central(F(1)))/3)
    assert gradient == mv(s(x, y), x)+mv(s(x, y), y)
    print("PASS nonradial quartic exchange geometry has an exact positive circle clock")
    print("PASS clock moment map follows the same opposed Green form")


def scalar_darboux():
    for a, lam in [(F(1), F(0)), (F(2, 3), F(3, 4)), (F(2), F(5, 3))]:
        for x, y in [(F(0), F(0)), (F(1, 3), F(-2, 5)), (F(2), F(1))]:
            r2 = x*x+y*y
            f2 = 2*a+F(3, 2)*lam*r2
            # Q=f x, P=-f y. Its determinant is -(f^2+r f f'),
            # with r f f'=3 lambda r^2/2; no finite differencing is used.
            determinant = -f2-F(3, 2)*lam*r2
            assert determinant == -2*(a+F(3, 2)*lam*r2)
            assert f2*r2/2 == a*r2+F(3, 4)*lam*r2*r2
    print("PASS scalar circle clock is canonically a harmonic oscillator")


if __name__ == "__main__":
    matrix_checks()
    scalar_checks()
    quartic_circle()
    scalar_darboux()
    print("Finite geometry checks only; no unique physical clock or quantum field gap.")
