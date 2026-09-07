"""Finite checks for nonlinear response and the homogeneous gauge return.

No files are written. These checks do not establish a continuum quantum field
theory or a Yang--Mills mass gap. Domain, compactness and spectral arguments
are proved separately in the canonical notes.
"""

from __future__ import annotations

from fractions import Fraction as F
import math


def close(name, actual, expected, tol=1e-8):
    if abs(actual - expected) > tol:
        raise AssertionError(f"{name}: {actual!r} != {expected!r}")


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0]]


def det(q):
    return dot(q[0], cross(q[1], q[2]))


def cofactor(q):
    return [cross(q[1], q[2]), cross(q[2], q[0]), cross(q[0], q[1])]


def mm(a, b):
    return [[dot(row, col) for col in zip(*b)] for row in a]


def transpose(a):
    return [list(row) for row in zip(*a)]


def combine(*terms):
    return [[sum(c * a[i][j] for c, a in terms)
             for j in range(len(terms[0][1][0]))]
            for i in range(len(terms[0][1]))]


def matrix_close(name, a, b, tol=1e-8):
    for row, other in zip(a, b):
        for x, y in zip(row, other):
            close(name, x, y, tol)


def symmetric_modulus(matrix):
    """Small Jacobi diagonalization, independent of the Frechet formula."""
    n = len(matrix)
    a = [list(row) for row in matrix]
    vectors = [[float(i == j) for j in range(n)] for i in range(n)]
    for _ in range(100):
        p, q = max(((i, j) for i in range(n) for j in range(i+1, n)),
                   key=lambda ij: abs(a[ij[0]][ij[1]]))
        if abs(a[p][q]) < 1e-14:
            break
        angle = 0.5 * math.atan2(2*a[p][q], a[q][q]-a[p][p])
        c, s = math.cos(angle), math.sin(angle)
        rotation = [[float(i == j) for j in range(n)] for i in range(n)]
        rotation[p][p] = rotation[q][q] = c
        rotation[p][q], rotation[q][p] = s, -s
        a = mm(mm(transpose(rotation), a), rotation)
        vectors = mm(vectors, rotation)
    else:
        raise AssertionError("Jacobi diagonalization did not converge")
    diagonal = [[abs(a[i][i]) if i == j else 0.0 for j in range(n)]
                for i in range(n)]
    return mm(mm(vectors, diagonal), transpose(vectors))


def determinant_hessian(x, y, z):
    return [[0.0, z, y], [z, 0.0, x], [y, x, 0.0]]


def simpson(f, hi=4.0, steps=8000):
    step = hi / steps
    return step / 3 * sum(
        (1 if j in (0, steps) else 4 if j % 2 else 2) * f(j * step)
        for j in range(steps+1))


def check_nonlinear_graphs():
    a, lam = 0.7, 0.4
    for x in [-1.2, -0.3, 0.0, 0.8]:
        n = a*x + lam*x**3
        dn = a + 3*lam*x*x
        force = a*a*x + 4*a*lam*x**3 + 3*lam*lam*x**5
        close("squared-response derivative", force, dn*n)
        for sign in [-1, 1]:
            close("normal graph tangent", sign*dn*(sign*n), force)
        for t in [0.0, 0.2, 1.5]:
            flow = lambda s: x*math.exp(-a*s) / math.sqrt(
                1+(lam/a)*x*x*(1-math.exp(-2*a*s)))
            y = flow(t)
            dt = 1e-5
            close("nonlinear decay", (flow(t+dt)-flow(t-dt))/(2*dt),
                  -(a*y+lam*y**3), 1e-8)
    c2, c4, c6 = a*a/2, a*lam, lam*lam/2
    close("coefficient restriction", c4*c4, 4*c2*c6)
    # Frozen compatible metric is not a conserved clock metric.
    x, p = 0.8, 0.3
    dn, ddn = a+3*lam*x*x, 6*lam*x
    n = a*x+lam*x**3
    lie_metric = [[p*ddn, -ddn*n/dn], [-ddn*n/dn, -p*ddn/(dn*dn)]]
    if max(abs(v) for row in lie_metric for v in row) < 0.1:
        raise AssertionError("nonlinear metric negative control vanished")
    print("PASS nonlinear graphs, decay law, coupling relation, metric control")


def check_gauge_transgression():
    matrices = [
        [[0.2, -0.7, 0.4], [1.1, 0.3, -0.2], [0.5, 0.6, 0.9]],
        [[1.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, -0.5]],
    ]
    step = 1e-5
    for q in matrices:
        n = cofactor(q)
        magnetic = sum(dot(cross(q[i], q[j]), cross(q[i], q[j]))
                       for i in range(3) for j in range(i+1, 3)) / 2
        close("magnetic norm", sum(dot(row, row) for row in n)/2, magnetic)
        gauge_moment = [sum(cross(q[i], n[i])[j] for i in range(3))
                        for j in range(3)]
        for value in gauge_moment:
            close("response gauge horizontality", value, 0)
        for i in range(3):
            for j in range(3):
                plus, minus = [r[:] for r in q], [r[:] for r in q]
                plus[i][j] += step
                minus[i][j] -= step
                close("determinant gradient",
                      (det(plus)-det(minus))/(2*step), n[i][j])
                close("determinant diagonal second derivative",
                      (det(plus)-2*det(q)+det(minus))/(step*step), 0, 1e-5)
    # At q I the scalar, symmetric tracefree, and skew sectors have
    # response-Hessian eigenvalues 2q, -q, and q.
    q = 0.6
    base = [[q if i == j else 0.0 for j in range(3)] for i in range(3)]
    tests = [
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 2*q),
        ([[1, 0, 0], [0, -1, 0], [0, 0, 0]], -q),
        ([[0, 1, 0], [-1, 0, 0], [0, 0, 0]], q),
    ]
    for b, rate in tests:
        finite = combine((1/(2*step), cofactor(combine((1, base), (step, b)))),
                         (-1/(2*step), cofactor(combine((1, base), (-step, b)))))
        matrix_close("cofactor Hessian sector", finite, combine((rate, b)))
    print("PASS determinant transgression, magnetic potential, gauge horizontality")


def check_hessian_integrability():
    p = [[F(1, 3)]*3 for _ in range(3)]
    ex = [[0, 0, 0], [0, 0, 1], [0, 1, 0]]
    ey = [[0, 0, 1], [0, 0, 0], [1, 0, 0]]

    def frechet(e):
        return combine((-1, e), (F(4, 3), mm(p, e)),
                       (F(4, 3), mm(e, p)), (-F(2, 3), mm(mm(p, e), p)))

    dy, dx = frechet(ey)[0][0], frechet(ex)[0][1]
    assert dy == F(20, 27) and dx == F(8, 27)
    assert dy-dx == F(4, 9)
    for q in [0.4, 1.0, 2.3]:
        h = determinant_hessian(q, q, q)
        modulus = symmetric_modulus(h)
        matrix_close("spectral square", mm(modulus, modulus), mm(h, h))
        step = 1e-5
        dy_numeric = (
            symmetric_modulus(determinant_hessian(q, q+step, q))[0][0]
            - symmetric_modulus(determinant_hessian(q, q-step, q))[0][0]
        )/(2*step)
        dx_numeric = (
            symmetric_modulus(determinant_hessian(q+step, q, q))[0][1]
            - symmetric_modulus(determinant_hessian(q-step, q, q))[0][1]
        )/(2*step)
        close("spectral dy", dy_numeric, float(dy), 1e-7)
        close("spectral dx", dx_numeric, float(dx), 1e-7)
    print("PASS positive-Hessian incompatibility: 20/27 - 8/27 = 4/9")


def check_rotated_response():
    def rotated(x, y):
        r = math.sqrt(y*y+4*x*x)
        return [2*x*(y*y+x*x)/r, 3*x*x*y/r]

    for x, y in [(1.0, 1.0), (0.3, -0.7), (2.0, 0.4)]:
        n, rn = [2*x*y, x*x], rotated(x, y)
        close("rotated norm", dot(n, n), dot(rn, rn))
        step = 1e-5
        curl = ((rotated(x+step, y)[1]-rotated(x-step, y)[1])
                -(rotated(x, y+step)[0]-rotated(x, y-step)[0]))/(2*step)
        expected = 2*x*y*(2*y*y-x*x)/(y*y+4*x*x)**1.5
        close("rotated nonclosed response", curl, expected, 1e-8)
    print("PASS norm-preserving response rotation is not gradient-compatible")


def check_quantum_response():
    for eps in [0.3, 1.0, 2.0]:
        for q in [-1.1, -0.2, 0.0, 0.7]:
            n, dn = q**3, 3*q*q
            psi_second_over_psi = n*n/(eps*eps)-dn/eps
            classical = n*n/2
            corrected = classical-eps*dn/2
            close("factored vacuum residual",
                  -eps*eps*psi_second_over_psi/2+corrected, 0)
            x = q / eps**0.25
            close("quartic-response scaling",
                  q**6-3*eps*q*q,
                  eps**1.5*(x**6-3*x*x))
    i0 = 2*simpson(lambda x: math.exp(-x**4/2))
    i2 = 2*simpson(lambda x: x*x*math.exp(-x**4/2))
    close("quartic vacuum normalization", i0,
          2**0.25*math.gamma(0.25)/2, 1e-10)
    close("quartic vacuum second moment", i2,
          2**0.75*math.gamma(0.75)/2, 1e-10)
    lower = math.sqrt(3)/2
    upper = math.gamma(0.25)/(2*math.sqrt(2)*math.gamma(0.75))
    close("q psi trial bound", i0/(2*i2), upper, 1e-10)
    assert 0 < lower < upper
    print(f"PASS quartic-response quantum gap constants: {lower:.9f}, {upper:.9f}")


def check_homogeneous_confinement():
    # Each kinetic slot and each unordered magnetic pair occurs in two T_i.
    for j in range(3):
        assert sum(j != i for i in range(3)) == 2
    for j in range(3):
        for k in range(j+1, 3):
            assert sum(i in (j, k) for i in range(3)) == 2
    for eps, radius in [(0.3, 0.8), (1.0, 2.0), (2.1, 0.4)]:
        # One transverse coordinate has variance eps/(2r). Its kinetic
        # and potential expectations are both eps*r/4.
        variance = eps/(2*radius)
        one_coordinate = radius*radius*variance
        close("four transverse zero-point contributions",
              4*one_coordinate, 2*eps*radius)
        length = eps**(1/3)
        close("matrix kinetic dilation", eps*eps/(length*length), eps**(4/3))
        close("matrix quartic dilation", length**4, eps**(4/3))
        for volume in [0.5, 1.0, 3.0]:
            length = (eps/volume)**(1/3)
            energy_scale = eps**(4/3)*volume**(-1/3)
            close("volume kinetic dilation",
                  eps*eps/(volume*length*length), energy_scale)
            close("volume magnetic dilation", volume*length**4, energy_scale)
    print("PASS homogeneous gauge oscillator counting and epsilon^(4/3) scaling")


def check_pure_gauge_extension():
    for amplitude in [0.4, 1.0, 3.0]:
        x, y = 0.2, 0.4
        fp = amplitude*math.cos(x)
        h, hp = amplitude*math.sin(y), amplitude*math.cos(y)
        ax = [fp*math.cos(h), 0.0, fp*math.sin(h)]
        ay = [0.0, hp, 0.0]
        dy_ax = [-fp*hp*math.sin(h), 0.0, fp*hp*math.cos(h)]
        bracket = cross(ax, ay)
        for derivative, commutator in zip(dy_ax, bracket):
            close("pure gauge derivative cancellation", -derivative+commutator, 0)
        close("nonzero pure gauge commutator", dot(bracket, bracket), (fp*hp)**2)
        assert dot(bracket, bracket) > 0
    print("PASS flat local gauge connection has nonzero pointwise commutator")


if __name__ == "__main__":
    check_nonlinear_graphs()
    check_gauge_transgression()
    check_hessian_integrability()
    check_rotated_response()
    check_quantum_response()
    check_homogeneous_confinement()
    check_pure_gauge_extension()
    print("Finite checks only; continuum Yang--Mills existence and gap remain open.")
