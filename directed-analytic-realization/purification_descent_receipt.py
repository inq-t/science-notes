"""Exact, stdlib, stdout-only checks for purification and octonionic descent.

Gaussian-rational matrices, sparse rational polynomials and exact spherical
moments are reused from guarded local receipts. The sphere generator is
one quarter of the rotational Casimir. The Cayley--Dickson convention is
the one in positive_cone_process_receipt.py. All equality checks are exact;
there is no sampling, eigensolver, numerical integration or spectral fit.

The listed rational points are finite algebraic probes, not Monte Carlo.
Finite moment and polynomial checks do not prove global operator domains,
disintegration, completeness of eigenfunctions, a physical clock, spatial
dimension selection, or a Yang--Mills mass gap. No files are written.
The fluctuation checks are finite identities, not a CLT or a process limit.
"""

from fractions import Fraction as F
from itertools import combinations, product

import positive_cone_process_receipt as pc
import sphere_ball_descent_receipt as sb
from context_transport_receipt import equal, mm, mv, require


FAMILIES = ((2, 2), (2, 4), (3, 3))


def identity(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def transpose(a):
    return tuple(zip(*a))


def add(a, b):
    return tuple(tuple(x+y for x, y in zip(row, other)) for row, other in zip(a, b))


def scale(c, a):
    return tuple(tuple(c*x for x in row) for row in a)


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def poly_sum(polynomials):
    result = {}
    for p in polynomials:
        result = sb.padd(result, p)
    return result


def squared_radius(n):
    return poly_sum(sb.coordinate(n, j, 2) for j in range(n))


def quadratic(a):
    n = len(a)
    return poly_sum(sb.pscale(a[i][j], sb.pmul(sb.coordinate(n, i), sb.coordinate(n, j)))
                    for i in range(n) for j in range(n) if a[i][j])


def evaluate(p, x):
    return sum(c*product_value(x[j]**power for j, power in enumerate(exponent))
               for exponent, c in p.items())


def product_value(values):
    result = F(1)
    for value in values:
        result *= value
    return result


def fast_sphere_casimir(p, n):
    # Exact ambient rotational identity: |z|^2 Delta - E(E+n-2).
    euler_part = {exponent: -sum(exponent)*(sum(exponent)+n-2)*c for exponent, c in p.items()}
    return sb.padd(sb.pmul(squared_radius(n), sb.laplacian(p, n)), sb.clean(euler_part))


def pullback(p, coordinates):
    n = len(next(iter(coordinates[0])))
    result = {}
    for exponent, coefficient in p.items():
        term = sb.monomial((0,)*n, coefficient)
        for q, degree in zip(coordinates, exponent):
            for _ in range(degree):
                term = sb.pmul(term, q)
        result = sb.padd(result, term)
    return result


def unit_points(n):
    points = [tuple(F(int(i == j)) for i in range(n)) for j in (0, n-1)]
    for seed in range(1, 5):
        u = tuple(F(((j+2)*seed) % 7-3, j+seed+3) for j in range(n-1))
        s = dot(u, u)
        points.append(((1-s)/(1+s),)+tuple(2*v/(1+s) for v in u))
    for point in points:
        equal(dot(point, point), 1, "rational stereographic unit point")
    return tuple(points)


def hermitian_probes(d):
    probes = []
    for i in range(d):
        probes.append(pc.matrix([[int(r == i and c == i) for c in range(d)] for r in range(d)]))
    for i, j in combinations(range(d), 2):
        for value in (pc.C(1), pc.C(0, 1)):
            a = pc.matrix([[0]*d for _ in range(d)])
            a[i][j], a[j][i] = value, value.conjugate()
            probes.append(a)
    mixed = pc.matrix([[0]*d for _ in range(d)])
    for i, a in enumerate(probes):
        mixed = pc.add(mixed, pc.scale(a, F((-1)**i*(i+1), i+2)))
    probes.append(mixed)
    for a in probes:
        equal(a, pc.adjoint(a), "Hermitian purification probe")
    return tuple(probes)


def realification(a, k):
    # Coordinates are row-major complex entries, each stored as (real,imag).
    d, n = len(a), 2*len(a)*k
    r = [[F(0)]*n for _ in range(n)]
    for i, j, column in product(range(d), range(d), range(k)):
        u, v = 2*(i*k+column), 2*(j*k+column)
        r[u][v], r[u][v+1] = a[i][j].real, -a[i][j].imag
        r[u+1][v], r[u+1][v+1] = a[i][j].imag, a[i][j].real
    return tuple(tuple(row) for row in r)


def purification(point, d, k):
    return [[pc.C(point[2*(i*k+j)], point[2*(i*k+j)+1]) for j in range(k)] for i in range(d)]


def purification_linear_response():
    count, point_count = 0, 0
    for d, k in FAMILIES:
        n = 2*d*k
        radius = squared_radius(n)
        one = sb.monomial((0,)*n)
        for a in hermitian_probes(d):
            r, trace_a = realification(a, k), pc.real(pc.trace(a))
            equal(r, transpose(r), "Hermitian realification is symmetric")
            f = quadratic(r)
            actual = sb.pscale(F(1, 4), fast_sphere_casimir(f, n))
            expected = sb.padd(sb.pscale(k*trace_a, one), sb.pscale(-d*k, f))
            equal(sb.padd(actual, sb.pscale(-1, expected)),
                  sb.pscale(k*trace_a, sb.padd(radius, sb.pscale(-1, one))),
                  "quarter-Casimir drift equals K Tr A-dK f_A modulo the sphere relation")
            for point in unit_points(n):
                psi = purification(point, d, k)
                q = pc.multiply(psi, pc.adjoint(psi))
                equal(pc.real(pc.trace(q)), 1, "purification output is trace one")
                equal(evaluate(f, point), pc.real(pc.trace(pc.multiply(q, a))),
                      "quadratic realification is the actual partial-trace observable")
                equal(evaluate(actual, point), k*trace_a-d*k*evaluate(f, point),
                      "actual unit-sphere affine drift")
                point_count += 1
            count += 1
    equal((count, point_count), (20, 120), "purification affine probe counts")
    print("PASS: 20 exact purification observables and 120 rational unit-point checks give Q=Psi Psi* and L f_A=K Tr A-dK f_A.")


def purification_covariance_and_moments():
    count = 0
    for d, k in FAMILIES:
        n = 2*d*k
        probes = hermitian_probes(d)
        polynomials = [quadratic(realification(a, k)) for a in probes]
        for a, fa in zip(probes, polynomials):
            equal(sb.expect(fa, n), pc.real(pc.trace(a))/d, "first purification moment")
            for b, fb in zip(probes, polynomials):
                jordan = pc.scale(pc.add(pc.multiply(a, b), pc.multiply(b, a)), F(1, 2))
                fj = quadratic(realification(jordan, k))
                gradient_pair = poly_sum(sb.pmul(sb.derivative(fa, j), sb.derivative(fb, j)) for j in range(n))
                equal(sb.pscale(F(1, 4), gradient_pair), fj, "ambient gradient produces the Jordan product")
                # On the unit sphere the tangential subtraction is f_A f_B.
                covariance = sb.padd(sb.pscale(F(1, 4), gradient_pair), sb.pscale(-1, sb.pmul(fa, fb)))
                equal(covariance, sb.padd(fj, sb.pscale(-1, sb.pmul(fa, fb))),
                      "quarter-sphere response is Jordan covariance, not a BKM claim")
                expected = (k*pc.real(pc.trace(a))*pc.real(pc.trace(b))+pc.real(pc.trace(pc.multiply(a, b)))) / (d*(d*k+1))
                equal(sb.expect(sb.pmul(fa, fb), n), expected, "exact spherical purification second moment")
                count += 1
    equal(count, 150, "purification covariance and second moment count")
    print("PASS: 150 exact Jordan covariance and spherical second-moment pairs match [K Tr A Tr B+Tr(AB)]/[d(dK+1)].")


def simplex_generator(p, d, k):
    # Independent diagonal entries q_1,...,q_(d-1); q_d=1-sum q_i.
    m = d-1
    result = {}
    one = sb.monomial((0,)*m)
    for i in range(m):
        xi = sb.coordinate(m, i)
        drift = sb.padd(sb.pscale(k, one), sb.pscale(-d*k, xi))
        result = sb.padd(result, sb.pmul(drift, sb.derivative(p, i)))
        for j in range(m):
            covariance = sb.pscale(-1, sb.pmul(xi, sb.coordinate(m, j)))
            if i == j:
                covariance = sb.padd(covariance, xi)
            result = sb.padd(result, sb.pmul(covariance, sb.derivative(sb.derivative(p, i), j)))
    return result


def purification_polynomial_descent():
    count, rotation_count = 0, 0
    for d, k in FAMILIES:
        n = 2*d*k
        readouts = [poly_sum(sb.coordinate(n, 2*(i*k+j)+part, 2) for j in range(k) for part in (0, 1)) for i in range(d-1)]
        relation = sb.padd(squared_radius(n), sb.monomial((0,)*n, -1))
        for exponent in sb.basis(d-1, 4):
            p = sb.monomial(exponent)
            image = simplex_generator(p, d, k)
            ell = sum(exponent)
            equal(image.get(exponent, F(0)), -ell*(ell+d*k-1), "degree-triangular purification eigenvalue")
            require(all(sum(a) in (ell, ell-1) for a in image), "generator lowers diagonal polynomial degree by at most one")
            fp = pullback(p, readouts)
            actual = sb.pscale(F(1, 4), fast_sphere_casimir(fp, n))
            equal(sb.padd(actual, sb.pscale(-1, pullback(image, readouts))),
                  sb.pscale(F(1, 4), sb.pmul(relation, sb.laplacian(fp, n))),
                  "complete diagonal polynomial pullback modulo the unit-sphere relation")
            if ell <= 1:
                equal(fast_sphere_casimir(fp, n), sb.sphere_casimir(fp, n),
                      "fast ambient identity independently matches explicit rotational fields")
                rotation_count += 1
            count += 1
    equal((count, rotation_count), (25, 7), "polynomial descent and rotational cross-check counts")
    print("PASS: 25 exact diagonal-polynomial pullbacks have upper-degree eigenvalue ell(ell+dK-1); seven checks use the explicit rotational fields.")


def octonion_conjugate(a):
    return (a[0],)+tuple(-x for x in a[1:])


def octonion_basis():
    return tuple(tuple(int(i == j) for i in range(8)) for j in range(8))


def clifford_system():
    basis = octonion_basis()
    left = [transpose(tuple(pc.octonion_multiply(c, b) for b in basis)) for c in basis]
    p0 = tuple(tuple((1 if i < 8 else -1)*int(i == j) for j in range(16)) for i in range(16))
    matrices = [p0]
    for l in left:
        p = [[0]*16 for _ in range(16)]
        for i, j in product(range(8), repeat=2):
            p[i][j+8], p[i+8][j] = l[i][j], l[j][i]
        matrices.append(tuple(tuple(row) for row in p))
    return tuple(matrices), tuple(left)


def hopf_clifford_and_norm():
    matrices, left = clifford_system()
    for p in matrices:
        equal(p, transpose(p), "real symmetric Clifford matrix")
        equal(sum(p[i][i] for i in range(16)), 0, "traceless Clifford matrix")
    for i, j in product(range(9), repeat=2):
        equal(add(mm(matrices[i], matrices[j]), mm(matrices[j], matrices[i])),
              scale(2*int(i == j), identity(16)), "exact real Clifford anticommutation")
    h = tuple(quadratic(p) for p in matrices)
    equal(poly_sum(sb.pmul(q, q) for q in h), sb.pmul(squared_radius(16), squared_radius(16)),
          "Hopf norm composition is an exact off-sphere polynomial identity")
    for point in unit_points(16):
        a, b = point[:8], point[8:]
        octonionic = (dot(a, a)-dot(b, b),)+tuple(2*x for x in pc.octonion_multiply(a, octonion_conjugate(b)))
        actual = tuple(evaluate(q, point) for q in h)
        equal(actual, octonionic, "Clifford quadratic map equals (|a|^2-|b|^2,2a conjugate(b))")
        equal(dot(actual, actual), 1, "rational unit point maps to the unit S8")
        for j, l in enumerate(left):
            equal(actual[j+1], 2*dot(a, mv(l, b)), "left-multiplication convention for each Hopf component")
    basis = octonion_basis()
    a = tuple(F(3, 5)*x for x in basis[1])
    b = tuple(F(4, 5)*x for x in basis[2])
    u = basis[4]
    au, bu = pc.octonion_multiply(a, u), pc.octonion_multiply(b, u)
    equal(dot(a, a)+dot(b, b), 1, "right-action counterexample starts on S15")
    equal(dot(au, au)+dot(bu, bu), 1, "right multiplication preserves the total norm")
    before = tuple(2*x for x in pc.octonion_multiply(a, octonion_conjugate(b)))
    after = tuple(2*x for x in pc.octonion_multiply(au, octonion_conjugate(bu)))
    equal(before, tuple(F(-24, 25)*x for x in basis[3]), "initial Hopf off-diagonal is -24/25 k")
    equal(after, tuple(F(24, 25)*x for x in basis[3]), "simultaneous octonionic right action changes the Hopf fiber")
    require(before != after, "unit octonions do not give this naive fiberwise group action")
    print("PASS: nine symmetric traceless 16x16 matrices satisfy all 81 Clifford relations; the exact Hopf norm and six probes pass, while a rational right-action counterexample changes the fiber.")


def hopf_response_and_moments():
    matrices, _ = clifford_system()
    h = tuple(quadratic(p) for p in matrices)
    radius4 = sb.pmul(squared_radius(16), squared_radius(16))
    for hi in h:
        equal(fast_sphere_casimir(hi, 16), sb.pscale(-32, hi), "Hopf harmonic quadratic has spherical Laplacian -32 h")
        equal(sb.expect(hi, 16), 0, "Hopf first spherical moment")
    parent_coordinate = sb.coordinate(16, 0)
    equal(sb.pscale(F(1, 4), fast_sphere_casimir(parent_coordinate, 16)),
          sb.pscale(F(-15, 4), parent_coordinate), "normalized parent linear mode has positive decay rate 15/4")
    equal(sb.pscale(F(1, 4), fast_sphere_casimir(h[0], 16)), sb.pscale(-8, h[0]),
          "visible quadratic mode has decay rate eight in the same normalization")
    require(F(15, 4) < 8, "positive parent linear rate is below the visible quadratic rate")
    for i, j in product(range(9), repeat=2):
        gradient_pair = poly_sum(sb.pmul(sb.derivative(h[i], k), sb.derivative(h[j], k)) for k in range(16))
        equal(gradient_pair, sb.pscale(4*int(i == j), squared_radius(16)), "ambient Clifford gradient covariance")
        rotational_pair = sb.padd(sb.pmul(squared_radius(16), gradient_pair), sb.pscale(-4, sb.pmul(h[i], h[j])))
        equal(rotational_pair, sb.pscale(4, sb.padd(sb.pscale(int(i == j), radius4), sb.pscale(-1, sb.pmul(h[i], h[j])))),
              "spherical gradient covariance is 4(delta-h h) on the unit sphere")
        equal(sb.expect(sb.pmul(h[i], h[j]), 16), F(int(i == j), 9), "Hopf second moments equal round S8 moments")
    fourth_count = 0
    for i in range(9):
        for j in range(i, 9):
            equal(sb.expect(sb.pmul(sb.pmul(h[i], h[i]), sb.pmul(h[j], h[j])), 16),
                  F(3 if i == j else 1, 9*11), "Hopf fourth moments equal round S8 moments")
            fourth_count += 1
    equal(fourth_count, 45, "Hopf fourth-moment count")
    print("PASS: nine Laplacian and 81 gradient-covariance identities give the quarter-Casimir return; 81 second and 45 fourth moments match S8, with parent linear rate 15/4 and visible quadratic rate 8.")


def complex_coordinates(a, left_e):
    # e=e1 and real C-basis representatives (1,e2,e4,e6).
    # The fourth imaginary partner may carry a Cayley--Dickson sign.
    basis = octonion_basis()
    return tuple(pc.C(dot(a, basis[j]), dot(a, mv(left_e, basis[j]))) for j in (0, 2, 4, 6))


def hopf_purification_composition():
    matrices, left = clifford_system()
    h = tuple(quadratic(p) for p in matrices)
    for exponent in sb.basis(9, 2):
        p = sb.monomial(exponent)
        equal(sb.pscale(F(1, 4), fast_sphere_casimir(pullback(p, h), 16)),
              pullback(fast_sphere_casimir(p, 9), h),
              "quarter S15 Casimir intertwines the full S8 Casimir through the Hopf map")
    # Exact signed orthonormal identification O=C^4, selected by L_e1.
    real_basis = octonion_basis()
    complex_frame = tuple(vector for j in (0, 2, 4, 6) for vector in (real_basis[j], mv(left[1], real_basis[j])))
    equal(mm(complex_frame, transpose(complex_frame)), identity(8), "selected complex frame is real orthonormal")
    frame16 = tuple(tuple(complex_frame[i][j] if block == half else 0 for half in range(2) for j in range(8))
                    for block in range(2) for i in range(8))
    # z_complex=frame16*z_octonion, so response quadratics pull back by congruence.
    for sigma, expected_h, sign in ((pc.PAULI[0], h[1], 1), (pc.PAULI[1], h[2], -1), (pc.PAULI[2], h[0], 1)):
        transported = mm(mm(transpose(frame16), realification(sigma, 4)), frame16)
        equal(quadratic(transported), sb.pscale(sign, expected_h), "complex-corner Pauli readout equals the signed Hopf projection as a polynomial")
    for point in unit_points(16):
        psi = [list(complex_coordinates(point[:8], left[1])), list(complex_coordinates(point[8:], left[1]))]
        q = pc.multiply(psi, pc.adjoint(psi))
        hh = tuple(evaluate(hi, point) for hi in h)
        expected = pc.scale(pc.matrix(((1+hh[0], pc.C(hh[1], hh[2])),
                                      (pc.C(hh[1], -hh[2]), 1-hh[0]))), F(1, 2))
        equal(q, expected, "Hopf complex corner equals actual C^(2x4) partial trace")
        bloch = tuple(pc.real(pc.trace(pc.multiply(q, sigma))) for sigma in pc.PAULI)
        equal(bloch, (hh[1], -hh[2], hh[0]), "standard Pauli y coordinate has the declared minus sign")
        equal(pc.real(pc.determinant(q)), (1-dot(bloch, bloch))/4, "corner determinant is the retained Bloch radial defect")
        require(dot(bloch, bloch) <= 1, "retained Hopf coordinates lie in the Bloch ball")
    # The parent is the normalized-amplitude sphere, not its complex
    # projectivization: a common selected-complex phase need not preserve h.
    a = tuple(F(3, 5)*x for x in real_basis[2])
    b = tuple(F(4, 5)*x for x in real_basis[4])
    ja, jb = mv(left[1], a), mv(left[1], b)
    j_ell = pc.octonion_multiply(real_basis[2], real_basis[4])
    before = tuple(2*x for x in pc.octonion_multiply(a, octonion_conjugate(b)))
    after = tuple(2*x for x in pc.octonion_multiply(ja, octonion_conjugate(jb)))
    equal(before, tuple(F(-24, 25)*x for x in j_ell), "selected-complex phase witness starts at -24/25 j*ell")
    equal(after, tuple(F(24, 25)*x for x in j_ell), "common left-i phase changes the full Hopf output")
    require(before != after, "Hopf map does not descend through this complex global phase")
    psi = [list(complex_coordinates(a, left[1])), list(complex_coordinates(b, left[1]))]
    phased_psi = [list(complex_coordinates(ja, left[1])), list(complex_coordinates(jb, left[1]))]
    equal(phased_psi, pc.scale(psi, pc.C(0, 1)), "left-i is the common complex phase in the selected frame")
    equal(pc.multiply(phased_psi, pc.adjoint(phased_psi)), pc.multiply(psi, pc.adjoint(psi)),
          "selected complex Gram matrix is unchanged by the common global phase")
    equal(dot(a, a)+dot(b, b), 1, "global-phase counterexample lies on the normalized-amplitude sphere")
    print("PASS: 55 Hopf intertwinings, three signed corner quadratics and six partial traces give Bloch=(h_Re,-h_e,h_diag); a common complex phase preserves the Gram matrix but changes the full Hopf output.")


def partial_trace_clock_and_fluctuations():
    def tensor_identity(a, db):
        da = len(a)
        return pc.matrix([[a[i//db][j//db]*int(i % db == j % db)
                           for j in range(da*db)] for i in range(da*db)])

    def partial_trace_b(rho, da, db):
        return pc.matrix([[sum(rho[i*db+b][j*db+b] for b in range(db))
                           for j in range(da)] for i in range(da)])

    def state_value(rho, a):
        return pc.real(pc.trace(pc.multiply(rho, a)))

    def jordan(a, b):
        return pc.scale(pc.add(pc.multiply(a, b), pc.multiply(b, a)), F(1, 2))

    def second_moment(a, b, d, k):
        return (k*pc.real(pc.trace(a))*pc.real(pc.trace(b))+pc.real(pc.trace(pc.multiply(a, b)))) / (d*(d*k+1))

    marginal_covariance_count, marginal_moment_count = 0, 0
    # Include both rank-constrained K=1 parents and full-rank families. No
    # determinant density on the full matrix interior is asserted at K=1.
    for da, db, k in ((2, 2, 1), (2, 2, 4), (2, 3, 1), (2, 3, 6)):
        d, ka = da*db, db*k
        total = d*k
        equal(da*ka, total, "partial trace preserves the total purification dimension and clock divisor")
        probes = hermitian_probes(da)
        lifted = [tensor_identity(a, db) for a in probes]
        for a, aa in zip(probes, lifted):
            equal(pc.real(pc.trace(aa)), db*pc.real(pc.trace(a)), "partial-trace affine constant is compatible")
            for b, bb in zip(probes, lifted):
                equal(jordan(aa, bb), tensor_identity(jordan(a, b), db), "Jordan products commute with the tensor-identity lift")
                equal(second_moment(aa, bb, d, k), second_moment(a, b, da, ka),
                      "parent and marginal exact second moments agree")
                marginal_moment_count += 1
        for point in unit_points(2*total)[2:4]:
            psi = purification(point, d, k)
            rho = pc.multiply(psi, pc.adjoint(psi))
            marginal = partial_trace_b(rho, da, db)
            regrouped = [[psi[i*db+b][column] for b in range(db) for column in range(k)] for i in range(da)]
            equal(marginal, pc.multiply(regrouped, pc.adjoint(regrouped)),
                  "actual partial trace is the Gram matrix of the same regrouped amplitude")
            for a, aa in zip(probes, lifted):
                fa, lifted_fa = state_value(marginal, a), state_value(rho, aa)
                equal(lifted_fa, fa, "actual affine values pull back through partial trace")
                parent_drift = k*pc.real(pc.trace(aa))-total*lifted_fa
                marginal_drift = ka*pc.real(pc.trace(a))-total*fa
                equal(parent_drift, marginal_drift, "unnormalized marginal clock agrees")
                equal(parent_drift/total, pc.real(pc.trace(a))/da-fa, "normalized marginal affine drift")
                for b, bb in zip(probes, lifted):
                    parent_gamma = state_value(rho, jordan(aa, bb))-lifted_fa*state_value(rho, bb)
                    marginal_gamma = state_value(marginal, jordan(a, b))-fa*state_value(marginal, b)
                    equal(parent_gamma, marginal_gamma, "actual parent and marginal covariances agree")
                    equal(parent_gamma/total, marginal_gamma/(da*ka), "normalized response preserves the same duration")
                    marginal_covariance_count += 1
    equal((marginal_moment_count, marginal_covariance_count), (100, 200), "marginal moment and state-covariance counts")

    def traceless_basis(d):
        if d == 2:
            return tuple(pc.PAULI)
        require(d == 3, "receipt has a declared two- and three-level traceless basis")
        diagonal1 = pc.matrix(((1, 0, 0), (0, -1, 0), (0, 0, 0)))
        diagonal2 = pc.matrix(((1, 0, 0), (0, 1, 0), (0, 0, -2)))
        return (diagonal1, diagonal2)+hermitian_probes(3)[3:9]

    variance_count, coefficient_count, drift_count = 0, 0, 0
    for d in (2, 3):
        basis = traceless_basis(d)
        require(all(pc.trace(a) == pc.C() for a in basis), "all fluctuation probes are traceless")
        norm2 = tuple(pc.real(pc.trace(pc.multiply(t, t))) for t in basis)
        for i, j in product(range(len(basis)), repeat=2):
            equal(pc.real(pc.trace(pc.multiply(basis[i], basis[j]))), norm2[i] if i == j else 0,
                  "declared traceless basis is trace-orthogonal")
        for t, tnorm2 in zip(basis, norm2):
            previous_variance = None
            for k in (1, 2, 4, 8, 32):
                total = d*k
                raw_variance = second_moment(t, t, d, k)
                equal(raw_variance, tnorm2/(d*(total+1)), "raw ensemble variance has the stated exact denominator")
                equal((total+1)*raw_variance, tnorm2/d, "squared fluctuation rescaling preserves nonzero variance exactly")
                require(raw_variance > 0, "every tested raw ensemble variance is positive")
                if previous_variance is not None:
                    require(raw_variance < previous_variance, "raw ensemble variance decreases as the environment grows")
                previous_variance = raw_variance
                variance_count += 1

        coefficients = {}
        for i, j in product(range(len(basis)), repeat=2):
            product_jordan = jordan(basis[i], basis[j])
            g = pc.real(pc.trace(product_jordan))/d
            c = tuple(pc.real(pc.trace(pc.multiply(product_jordan, t)))/tnorm2 for t, tnorm2 in zip(basis, norm2))
            reconstructed = pc.scale(pc.identity(d), g)
            for ck, t in zip(c, basis):
                reconstructed = pc.add(reconstructed, pc.scale(t, ck))
            equal(reconstructed, product_jordan, "exact scalar-plus-traceless Jordan decomposition")
            coefficients[i, j] = (g, c, product_jordan)
        if d == 3:
            require(any(any(c) for _, c, _ in coefficients.values()), "three-level checks include genuinely nonzero linear Jordan terms")

        # D+1 is a perfect square, so xi and every coefficient stay rational.
        # All these coefficient probes have K>=d; variance checks above also
        # deliberately cover valid low-rank purification supports.
        roots = (3, 5, 7) if d == 2 else (4, 5, 7)
        for root in roots:
            total, k = root*root-1, (root*root-1)//d
            equal(d*k, total, "rational fluctuation normalization has integer environment size")
            require(k >= d, "coefficient probe belongs to a full-rank purification family")
            for point in unit_points(2*total)[2:4]:
                psi = purification(point, d, k)
                rho = pc.multiply(psi, pc.adjoint(psi))
                values = tuple(state_value(rho, t) for t in basis)
                xi = tuple(root*v for v in values)
                for value, rescaled in zip(values, xi):
                    equal(F(root, total)*(-total*value), -rescaled, "normalized fluctuation drift is exactly minus xi")
                    drift_count += 1
                for (i, j), (g, c, product_jordan) in coefficients.items():
                    actual = F(total+1, total)*(state_value(rho, product_jordan)-values[i]*values[j])
                    expected = F(total+1, total)*g+F(root, total)*dot(c, xi)-xi[i]*xi[j]/total
                    equal(actual, expected, "finite fluctuation co-metric includes constant, linear and quadratic terms")
                    coefficient_count += 1
    equal((variance_count, coefficient_count, drift_count), (55, 438, 66), "finite fluctuation check counts")
    isometry_count = 0
    for d, k in FAMILIES:
        total = d*k
        for a, b in product(hermitian_probes(d), repeat=2):
            a0, b0 = pc.real(pc.trace(a))/d, pc.real(pc.trace(b))/d
            centered_a = pc.sub(a, pc.scale(pc.identity(d), a0))
            centered_b = pc.sub(b, pc.scale(pc.identity(d), b0))
            equal(pc.trace(centered_a), pc.C(), "first centered isometry probe has zero mean")
            equal(pc.trace(centered_b), pc.C(), "second centered isometry probe has zero mean")
            # On the real Hermitian carrier, cross terms with the constants
            # vanish. Only the squared rescaling D+1 is needed, not its root.
            ensemble_inner = a0*b0+(total+1)*second_moment(centered_a, centered_b, d, k)
            matrix_inner = pc.real(pc.trace(pc.multiply(a, b)))/d
            equal(ensemble_inner, matrix_inner, "fluctuation map is an exact Hilbert isometry on tested Hermitian symbols")
            isometry_count += 1
    equal(isometry_count, 150, "Hermitian fluctuation-isometry pair count")

    sigma3 = pc.PAULI[2]
    positive_a = pc.add(pc.I, sigma3)
    pc.positive_semidefinite(positive_a)
    equal(pc.real(pc.trace(pc.multiply(positive_a, positive_a)))/2, 2, "positive witness has normalized matrix squared norm two")
    equal(1+9*second_moment(sigma3, sigma3, 2, 4), 2, "its rescaled ensemble squared norm is also two")
    equal(1+3*F(-1), -2, "positive matrix maps to a negative boundary affine value")
    # A rational normalized amplitude gives an interior witness, so failure
    # is not confined to the measure-zero pure-state boundary.
    interior_psi = pc.matrix(((F(1, 2), 0, 0, 0), (0, F(1, 2), F(1, 2), F(1, 2))))
    interior_rho = pc.multiply(interior_psi, pc.adjoint(interior_psi))
    equal(interior_rho, pc.matrix(((F(1, 4), 0), (0, F(3, 4)))), "actual rational purification realizes a faithful interior witness")
    equal(pc.real(pc.trace(interior_rho)), 1, "interior positivity witness is normalized")
    require(pc.real(pc.determinant(interior_rho)) > 0, "interior positivity witness is strictly positive")
    equal(1+3*state_value(interior_rho, sigma3), F(-1, 2),
          "Hilbert isometry is not a positive symbol map even in the full-rank interior")

    # J_K transports the tracial Hilbert carrier, so it also transports an
    # actual faithful left *-representation. These matrices use its
    # orthonormal basis (I,sigma1,sigma2,sigma3), not pointwise multiplication
    # of the fluctuation symbols. A vector taking negative values is not a
    # failure of positivity for this operator representation.
    pauli_basis = (pc.I,)+tuple(pc.PAULI)

    def left_representation(b):
        return pc.matrix([[pc.trace(pc.multiply(pc.multiply(si, b), sj))/2
                           for sj in pauli_basis] for si in pauli_basis])

    def vacuum_column(a):
        return tuple(row[0] for row in a)

    representation_probes = pauli_basis+(positive_a, pc.hermitian(F(2, 3), (F(1, 2), F(-2, 5), F(3, 7))))
    equal(left_representation(pc.I), pc.identity(4), "tracial left representation is unital")
    representation_count = 0
    for b, c in product(representation_probes, repeat=2):
        bc = pc.multiply(b, c)
        represented = left_representation(bc)
        equal(represented, pc.multiply(left_representation(b), left_representation(c)),
              "actual left representation preserves all tested products")
        equal(left_representation(pc.adjoint(bc)), pc.adjoint(represented),
              "actual left representation preserves adjoints including non-Hermitian products")
        equal(represented[0][0], pc.trace(bc)/2, "constant vacuum returns the tracial quantum expectation")
        representation_count += 1
    equal(representation_count, 36, "quantum left-representation product count")

    represented_positive = left_representation(positive_a)
    equal(represented_positive, pc.adjoint(represented_positive), "positive witness returns a self-adjoint operator")
    equal(pc.multiply(represented_positive, represented_positive), pc.scale(represented_positive, 2),
          "represented I+sigma3 has spectrum contained in zero and two")
    pc.positive_semidefinite(represented_positive)
    equal(represented_positive[0][0], pc.C(1), "vacuum expectation of the represented positive witness is one")

    h = pc.matrix(((0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)))
    equal(pc.multiply(h, h), h, "normalized response generator is the centered projection")
    equal(vacuum_column(h), (pc.C(),)*4, "constant vacuum is the response kernel")
    equal(pc.trace(h), pc.C(3), "all three centered Pauli vectors have response eigenvalue one")
    for decay in (F(1, 2), F(1, 3), F(2, 5)):
        euclidean = pc.sub(pc.identity(4), pc.scale(h, 1-decay))
        for b in representation_probes:
            scalar = pc.trace(b)/2
            channel_b = pc.add(pc.scale(pc.I, scalar), pc.scale(pc.sub(b, pc.scale(pc.I, scalar)), decay))
            equal(vacuum_column(pc.multiply(euclidean, left_representation(b))),
                  vacuum_column(left_representation(channel_b)),
                  "Euclidean vector evolution is the exact tracial depolarizing channel")

    phase = pc.C(0, -1)
    unitary = pc.add(pc.sub(pc.identity(4), h), pc.scale(h, phase))
    equal(pc.multiply(unitary, pc.adjoint(unitary)), pc.identity(4), "chosen real-time phase is unitary")
    actual_evolution = pc.multiply(pc.multiply(unitary, represented_positive), pc.adjoint(unitary))
    naive_matrix_evolution = pc.add(pc.I, pc.scale(sigma3, phase))
    naive_representation = left_representation(naive_matrix_evolution)
    equal(actual_evolution, pc.adjoint(actual_evolution), "unitary conjugation retains operator self-adjointness")
    require(naive_representation != pc.adjoint(naive_representation),
            "multiplying the traceless matrix part by minus i does not preserve self-adjointness")
    require(actual_evolution != naive_representation, "unitary vector realization does not normalize the left observable algebra by this phase rule")
    equal(vacuum_column(actual_evolution), vacuum_column(naive_representation),
          "agreement on the vacuum vector is weaker than equality of represented operators")

    # A separate two-factor calculation fixes the opposite Heisenberg
    # orientation A(t)=U_z^* left(A) U_z. The positive representation is
    # intact; it is this global centered clock that fails the tested
    # unequal-time commutation requirement between disjoint factors.
    local_a = tensor_identity(sigma3, 2)
    local_b = pc.matrix(((1, 0, 0, 0), (0, -1, 0, 0), (0, 0, 1, 0), (0, 0, 0, -1)))
    local_ab = pc.multiply(local_a, local_b)
    equal(local_ab, pc.multiply(local_b, local_a), "separate tensor factors commute at equal time")
    require(all(pc.trace(x) == pc.C() for x in (local_a, local_b, local_ab)),
            "both disjoint-factor observables and their product have zero tracial mean")

    def phase_on_matrix(x, z):
        scalar_part = pc.scale(pc.identity(4), pc.trace(x)/4)
        return pc.add(scalar_part, pc.scale(pc.sub(x, scalar_part), z))

    for z in (pc.C(0, -1), pc.C(F(3, 5), F(4, 5)), pc.C(1)):
        equal(z*z.conjugate(), pc.C(1), "exact unit phase for global centered clock")

        def evolved_left_a(x):
            return phase_on_matrix(pc.multiply(local_a, phase_on_matrix(x, z)), z.conjugate())

        commutator_on_vacuum = pc.sub(evolved_left_a(local_b),
                                     pc.multiply(local_b, evolved_left_a(pc.identity(4))))
        equal(commutator_on_vacuum, pc.scale(local_ab, pc.C(1)-z.conjugate()),
              "disjoint-factor unequal-time commutator on the vacuum is (1-conjugate(z))*AB")
        if z != pc.C(1):
            require(any(value != pc.C() for row in commutator_on_vacuum for value in row),
                    "nontrivial tested global phases give a nonzero disjoint-factor commutator")
        else:
            equal(commutator_on_vacuum, pc.matrix([[0]*4 for _ in range(4)]),
                  "equal-time phase returns the vanishing commutator")
    print("PASS: four marginalizations, 55 variances, 438 co-metrics, 150 Hilbert-isometry pairs and 36 left-representation products pass; quantum positivity survives, but the global phase clock fails algebra normalization and disjoint-factor unequal-time commutation.")


def main():
    purification_linear_response()
    purification_covariance_and_moments()
    purification_polynomial_descent()
    hopf_clifford_and_norm()
    hopf_response_and_moments()
    hopf_purification_composition()
    partial_trace_clock_and_fluctuations()
    print("All seven check groups passed. Exact rational arithmetic; stdlib only; stdout only; no files written.")
    print("Finite polynomial and moment identities do not establish a global spectral theorem, physical scale, selected spatial dimension, or a Yang--Mills mass gap.")
    print("The finite fluctuation checks do not prove a central limit theorem, process convergence, or a physical field limit.")


if __name__ == "__main__":
    main()
