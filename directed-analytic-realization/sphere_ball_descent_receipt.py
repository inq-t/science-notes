"""Stdlib, stdout-only finite checks for spherical readout and ball geometry.

Sparse multivariate polynomials, moments, matrix defects, Jordan covariance,
SLD identities and weighted-metric jets use exact rational arithmetic. Only
finite probability entropies and their finite differences use logarithms.
The probability calibration is not a simulation of spherical diffusion.

Elementary helpers are reused from earlier guarded receipts. There is no
explicit filesystem I/O, network access, Monte Carlo or eigensolver. These
finite tests do not establish global operator domains, a continuum spectral
theorem, a physical clock, a spacetime net, or a Yang--Mills mass gap.
"""

from fractions import Fraction as F
from itertools import combinations, product
import math

import moving_response_receipt as mr
import positive_cone_process_receipt as pc
from context_transport_receipt import close, equal, mm, require


def clean(p):
    return {a: F(c) for a, c in p.items() if c}


def pscale(c, p):
    return clean({a: c*v for a, v in p.items()})


def padd(p, q):
    out = dict(p)
    for a, c in q.items():
        out[a] = out.get(a, F(0))+c
    return clean(out)


def pmul(p, q):
    out = {}
    for a, c in p.items():
        for b, d in q.items():
            exponent = tuple(x+y for x, y in zip(a, b))
            out[exponent] = out.get(exponent, F(0))+c*d
    return clean(out)


def monomial(exponent, coefficient=1):
    return clean({tuple(exponent): F(coefficient)})


def coordinate(dimension, j, power=1):
    return monomial(tuple(power if i == j else 0 for i in range(dimension)))


def derivative(p, j):
    out = {}
    for exponent, coefficient in p.items():
        if exponent[j]:
            target = list(exponent)
            target[j] -= 1
            out[tuple(target)] = coefficient*exponent[j]
    return clean(out)


def laplacian(p, dimension):
    out = {}
    for j in range(dimension):
        out = padd(out, derivative(derivative(p, j), j))
    return out


def embed(p, dimension):
    return {exponent+(0,)*(dimension-len(exponent)): coefficient
            for exponent, coefficient in p.items()}


def rotation(p, i, j, dimension):
    return padd(pmul(coordinate(dimension, i), derivative(p, j)),
                pscale(-1, pmul(coordinate(dimension, j), derivative(p, i))))


def sphere_casimir(p, dimension):
    out = {}
    for i, j in combinations(range(dimension), 2):
        out = padd(out, rotation(rotation(p, i, j, dimension), i, j, dimension))
    return out


def ball_generator(p, n, k):
    out = laplacian(p, k)
    for i in range(k):
        xi = coordinate(k, i)
        out = padd(out, pscale(-(n-1), pmul(xi, derivative(p, i))))
        for j in range(k):
            term = pmul(pmul(xi, coordinate(k, j)), derivative(derivative(p, i), j))
            out = padd(out, pscale(-1, term))
    return out


def basis(k, degree):
    return tuple(sorted((a for a in product(range(degree+1), repeat=k) if sum(a) <= degree),
                        key=lambda a: (sum(a), a)))


def sphere_moment(exponent, n):
    if any(a % 2 for a in exponent):
        return F(0)
    order = sum(exponent)//2
    numerator = math.prod(math.prod(range(1, a, 2)) for a in exponent)
    denominator = math.prod(n+2*j for j in range(order))
    return F(numerator, denominator)


def expect(p, n):
    return sum(coefficient*sphere_moment(exponent, n) for exponent, coefficient in p.items())


def dirichlet_pair(p, q, k):
    out, radial_p, radial_q = {}, {}, {}
    for j in range(k):
        dp, dq = derivative(p, j), derivative(q, j)
        out = padd(out, pmul(dp, dq))
        radial_p = padd(radial_p, pmul(coordinate(k, j), dp))
        radial_q = padd(radial_q, pmul(coordinate(k, j), dq))
    return padd(out, pscale(-1, pmul(radial_p, radial_q)))


FAMILIES = ((4, 1), (5, 2), (9, 3), (12, 4))


def ambient_descent():
    count = 0
    for n, k in FAMILIES:
        relation = monomial((0,)*n, -1)
        for j in range(n):
            relation = padd(relation, coordinate(n, j, 2))
        for exponent in basis(k, 4):
            p = monomial(exponent)
            ambient = sphere_casimir(embed(p, n), n)
            predicted = embed(ball_generator(p, n, k), n)
            # Off the unit sphere, the difference is exactly this defining relation times Delta_x f.
            equal(padd(ambient, pscale(-1, predicted)), pmul(relation, embed(laplacian(p, k), n)),
                  "ambient rotations descend modulo |z|^2-1")
            image = ball_generator(p, n, k)
            degree = sum(exponent)
            equal(image.get(exponent, F(0)), -degree*(degree+n-2), "exact degree-triangular diagonal")
            require(all(sum(a) in (degree, degree-2) for a in image), "generator lowers degree only by two")
            count += 1
    equal(count, 125, "ambient polynomial count")
    print("PASS: 125 exact polynomial pullbacks match the ambient rotational Casimir modulo the sphere equation and its triangular degree spectrum.")


def polynomial_eigenfunctions():
    count = 0
    for n, k in FAMILIES:
        constant = monomial((0,)*k)
        eigenfunctions = [(constant, 0)]
        for j in range(k):
            x, x2, x3, x4 = (coordinate(k, j, m) for m in (1, 2, 3, 4))
            eigenfunctions.extend(((x, 1), (padd(x2, pscale(F(-1, n), constant)), 2),
                                   (padd(x3, pscale(F(-3, n+2), x)), 3),
                                   (padd(padd(x4, pscale(F(-6, n+4), x2)),
                                         pscale(F(3, (n+2)*(n+4)), constant)), 4)))
        for i, j in combinations(range(k), 2):
            eigenfunctions.append((pmul(coordinate(k, i), coordinate(k, j)), 2))
        for i, j in product(range(k), repeat=2):
            if i != j:
                eigenfunctions.append((padd(pmul(coordinate(k, i, 2), coordinate(k, j)),
                                            pscale(F(-1, n+2), coordinate(k, j))), 3))
        for indices in combinations(range(k), 3):
            eigenfunctions.append((monomial(tuple(int(j in indices) for j in range(k))), 3))
        for p, degree in eigenfunctions:
            eigenvalue = degree*(degree+n-2)
            equal(ball_generator(p, n, k), pscale(-eigenvalue, p), "explicit ball eigenpolynomial")
            require(expect(pmul(p, p), n) > 0, "eigenpolynomial has nonzero norm")
            if degree:
                equal(expect(p, n), 0, "nonconstant eigenpolynomial has zero mean")
                require(eigenvalue >= n-1, "tested positive degree edge")
            count += 1
        x = coordinate(k, 0)
        equal(expect(dirichlet_pair(x, x, k), n)/expect(pmul(x, x), n), n-1,
              "coordinate Rayleigh quotient equals n-1")
    equal(count, 79, "explicit eigenpolynomial count")
    print("PASS: 79 exact low-degree eigenpolynomials have eigenvalues ell(ell+n-2); the n=9 coordinate quotient attains 8.")


def moment_integration_by_parts():
    count = 0
    for n, k in FAMILIES:
        polynomials = tuple(monomial(a) for a in basis(k, 3))
        for p, q in product(polynomials, repeat=2):
            equal(-expect(pmul(p, ball_generator(q, n, k)), n),
                  expect(dirichlet_pair(p, q, k), n), "exact moment integration by parts")
            count += 1
    equal(count, 1741, "moment integration-by-parts count")
    print("PASS: 1741 exact moment pairings verify the weighted Dirichlet integration-by-parts identity on low polynomials.")


def radial_normalization():
    # 4pi times 105/(32pi), so pi cancels before the rational calculation.
    prefactor = F(105, 8)
    radial_integral = F(1, 3)-F(2, 5)+F(1, 7)
    equal(prefactor*radial_integral, 1, "105/(32pi) ball density normalizes exactly")
    count = 0
    for halves in basis(3, 4):
        exponent = tuple(2*a for a in halves)
        order = sum(halves)
        radial_moment = prefactor*(F(1, 2*order+3)-F(2, 2*order+5)+F(1, 2*order+7))
        angular_moment = sphere_moment(exponent, 3)
        equal(radial_moment*angular_moment, sphere_moment(exponent, 9),
              "independent beta radial and S2 angular moments give the S8 readout moment")
        count += 1
    equal(count, 35, "independent radial moment count")
    print("PASS: exact radial beta normalization gives 105/(32pi); 35 independent radial/angular moments match the n=9 sphere formula.")


def forgotten_rotation():
    n, k = 9, 3
    y1, y2 = coordinate(n, k), coordinate(n, k+1)
    equal(rotation(y1, k, k+1, n), pscale(-1, y2), "vertical rotation of first hidden coordinate")
    equal(rotation(y2, k, k+1, n), y1, "vertical rotation of second hidden coordinate")
    for exponent in basis(k, 4):
        equal(rotation(embed(monomial(exponent), n), k, k+1, n), {}, "vertical rotation kills every tested readout")
    for omega in (F(-2), F(1, 2), F(3)):
        l1 = padd(sphere_casimir(y1, n), pscale(omega, rotation(y1, k, k+1, n)))
        l2 = padd(sphere_casimir(y2, n), pscale(omega, rotation(y2, k, k+1, n)))
        equal(l1, padd(pscale(-8, y1), pscale(-omega, y2)), "hidden generator first column")
        equal(l2, padd(pscale(omega, y1), pscale(-8, y2)), "hidden generator second column")
        equal(expect(pmul(y1, l2), n)-expect(pmul(l1, y2), n), 2*omega/n,
              "whole generator is not symmetric on the hidden plane")
        matrix = mr.rational(((-8, omega), (-omega, -8)))
        equal(mr.determinant_polynomial(mr.scale(-1, matrix), mr.identity(2)),
              (64+omega*omega, F(16), F(1)), "exact hidden rotation characteristic polynomial")
        g = mr.scale(F(1, n), mr.identity(2))
        equal(mr.response(g, mr.scale(0, g), matrix), mr.scale(F(16, n), mr.identity(2)),
              "skew hidden drift does not change the symmetric response")
    print("PASS: three exact nonsymmetric hidden rotations change the whole generator but annihilate all 35 tested retained polynomials.")


def probabilities(weights):
    total = sum(weights)
    return tuple(F(w, total) for w in weights)


def conditional_map(mu, groups):
    coarse = tuple(sum(mu[i] for i in group) for group in groups)
    matrix = tuple(tuple(mu[i]/coarse[j] if i in group else F(0) for i in range(len(mu)))
                   for j, group in enumerate(groups))
    lift = tuple(tuple(F(int(i in group)) for group in groups) for i in range(len(mu)))
    return coarse, matrix, lift


def apply(a, x):
    return tuple(sum(c*v for c, v in zip(row, x)) for row in a)


def entropy_density(mu, h):
    require(all(v > 0 for v in h), "tested density is strictly positive")
    return sum(float(p*v)*math.log(float(v)) for p, v in zip(mu, h))


def finite_entropy_calibration():
    mu = probabilities((1, 2, 3, 4, 5, 6))
    groups = ((0, 1), (2, 3), (4, 5))
    mux, f, lift = conditional_map(mu, groups)
    muw, h, _ = conditional_map(mux, ((0, 1), (2,)))
    projection = mm(lift, f)
    equal(mm(projection, projection), projection, "conditional projection is exactly idempotent")
    g0, g1, g2 = mr.diagonal(mu), mr.diagonal(mux), mr.diagonal(muw)
    d01, d12 = mr.arrow_defect(g0, g1, f), mr.arrow_defect(g1, g2, h)
    d02 = mr.arrow_defect(g0, g2, mm(h, f))
    equal(d02, mr.add(d01, mr.congruence(d12, f)), "exact Hessian loss cocycle on a discrete calibration")
    for nu in (probabilities((6, 5, 4, 3, 2, 1)), probabilities((1, 1, 1, 1, 1, 1)),
               probabilities((2, 3, 5, 7, 11, 13))):
        density = tuple(p/q for p, q in zip(nu, mu))
        coarse, twice = apply(f, density), apply(mm(h, f), density)
        whole_entropy = entropy_density(mu, density)
        retained_entropy = entropy_density(mux, coarse)
        final_entropy = entropy_density(muw, twice)
        conditional_loss = 0.0
        for group, coarse_density in zip(groups, coarse):
            conditional_loss += sum(float(nu[i])*math.log(float(density[i]/coarse_density)) for i in group)
        close(whole_entropy-retained_entropy, conditional_loss, "finite conditional entropy chain rule")
        close(whole_entropy-final_entropy, conditional_loss+retained_entropy-final_entropy,
              "two-stage entropy decomposition")
        require(conditional_loss > 0, "first readout has strictly positive entropy loss")
        projected = apply(projection, density)
        equal(apply(projection, projected), projected, "second identical readout changes no density")
        close(entropy_density(mu, projected)-entropy_density(mu, apply(projection, projected)), 0,
              "repeating the same projection creates no second entropy loss")
    for raw in ((1, -2, 3, -4, 5, -6), (2, 0, -1, 4, 3, -2), (-2, 1, 0, 3, -4, 2)):
        mean = sum(p*x for p, x in zip(mu, raw))
        tangent = tuple(F(x)-mean for x in raw)
        equal(sum(p*x for p, x in zip(mu, tangent)), 0, "normalized density tangent")
        projected = apply(projection, tangent)
        norm_residual = sum(p*(x-y)**2 for p, x, y in zip(mu, tangent, projected))
        equal(mr.quadratic(d01, tangent), norm_residual, "exact complete conditional Hessian")
        require(norm_residual > 0, "nontrivial tangent residue")
        for epsilon in (F(1, 128), F(1, 256), F(1, 512)):
            symmetric_loss = 0.0
            for sign in (-1, 1):
                density = tuple(1+sign*epsilon*x for x in tangent)
                symmetric_loss += entropy_density(mu, density)-entropy_density(mux, apply(f, density))
            numerical_hessian = symmetric_loss/float(epsilon*epsilon)
            require(abs(numerical_hessian-float(norm_residual)) <= 0.001*float(norm_residual),
                    "selected central entropy differences approach the exact Hessian")
    print("PASS: three discrete probability chain rules, repeated-projection zero loss, and nine numerical Hessian probes agree with the exact finite loss form.")


def pseudodeterminant_angle_failure():
    p = mr.diagonal((1, 0))
    for c, s in ((F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(8, 17), F(15, 17))):
        equal(c*c+s*s, 1, "exact unit direction")
        q = mr.rational(((c*c, c*s), (c*s, s*s)))
        equal(mm(q, q), q, "second rank-one projection")
        composite_gram = mr.congruence(q, p)
        for gram in (p, q, composite_gram):
            equal(mr.determinant(gram), 0, "each tested full Gram is singular")
        # Rank one: its unique nonzero eigenvalue equals its trace, no eigensolver required.
        equal(sum(p[i][i] for i in range(2)), 1, "first pseudodeterminant")
        equal(sum(q[i][i] for i in range(2)), 1, "second pseudodeterminant")
        equal(sum(composite_gram[i][i] for i in range(2)), c*c, "composite pseudodeterminant retains angle")
        require(c*c < 1, "pseudodeterminants fail multiplication despite unchanged nonzero rank")
    print("PASS: three exact rank-one projection pairs show that deleting zero eigenvalues loses the compositional angle cost.")


def jordan_and_sld():
    states = ((F(0),)*3, (F(1, 2), F(0), F(0)),
              (F(1, 3), F(-1, 4), F(1, 5)), (F(-2, 7), F(3, 7), F(1, 7)))
    directions = ((F(1), F(0), F(0)), (F(0), F(1), F(0)), (F(0), F(0), F(1)),
                  (F(1, 3), F(2, 3), F(-1, 3)))
    covariance_count, sld_count = 0, 0
    for x in states:
        y2 = 1-sum(v*v for v in x)
        require(y2 > 0, "faithful Bloch state")
        rho = pc.scale(pc.hermitian(1, x), F(1, 2))
        a_metric = tuple(tuple(F(int(i == j))-x[i]*x[j] for j in range(3)) for i in range(3))
        g_metric = tuple(tuple(F(int(i == j))+x[i]*x[j]/y2 for j in range(3)) for i in range(3))
        equal(mm(a_metric, g_metric), mr.identity(3), "exact inverse covariance metric")
        for a, b in product(directions, repeat=2):
            aa, bb = pc.hermitian(0, a), pc.hermitian(0, b)
            jordan = pc.scale(pc.add(pc.multiply(aa, bb), pc.multiply(bb, aa)), F(1, 2))
            actual = (pc.real(pc.trace(pc.multiply(rho, jordan)))
                      -pc.real(pc.trace(pc.multiply(rho, aa)))*pc.real(pc.trace(pc.multiply(rho, bb))))
            expected = sum(u*v for u, v in zip(a, b))-sum(u*v for u, v in zip(a, x))*sum(u*v for u, v in zip(b, x))
            equal(actual, expected, "actual qubit Jordan covariance")
            covariance_count += 1
        for v in directions:
            dot = sum(u*w for u, w in zip(x, v))
            alpha = -dot/y2
            b = tuple(v[i]+dot*x[i]/y2 for i in range(3))
            sld = pc.hermitian(alpha, b)
            drho = pc.scale(pc.hermitian(0, v), F(1, 2))
            equal(pc.scale(pc.add(pc.multiply(rho, sld), pc.multiply(sld, rho)), F(1, 2)), drho,
                  "exact symmetric logarithmic derivative equation")
            equal(pc.real(pc.trace(pc.multiply(rho, pc.multiply(sld, sld)))), mr.quadratic(g_metric, v),
                  "SLD Fisher form equals the inverse Jordan covariance metric")
            sld_count += 1
    equal(covariance_count, 64, "Jordan covariance count")
    equal(sld_count, 16, "SLD count")

    # Complex-bilinear affine symbols: no conjugation enters either covariance
    # or the oriented cross product. These local helpers retain Gaussian
    # rational coefficients, unlike the rational polynomial helpers above.
    imaginary = pc.C(0, 1)
    zero_degree = (0, 0, 0)
    unit_degrees = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

    def cadd(p, q):
        result = dict(p)
        for exponent, coefficient in q.items():
            result[exponent] = result.get(exponent, pc.C())+coefficient
        return {exponent: coefficient for exponent, coefficient in result.items() if coefficient != pc.C()}

    def cscale(c, p):
        return cadd({}, {exponent: pc.C.cast(c)*coefficient for exponent, coefficient in p.items()})

    def cmultiply(p, q):
        result = {}
        for e, a in p.items():
            for f, b in q.items():
                exponent = tuple(u+v for u, v in zip(e, f))
                result = cadd(result, {exponent: a*b})
        return result

    def symbol(a):
        return cadd({}, dict(zip((zero_degree,)+unit_degrees, a)))

    def cross(a, b):
        return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])

    def affine_star(a, b):
        oriented = cross(a[1:], b[1:])
        return ((a[0]*b[0]+sum((a[i]*b[i] for i in range(1, 4)), pc.C()),)
                +tuple(a[0]*b[i+1]+b[0]*a[i+1]+imaginary*oriented[i] for i in range(3)))

    symbols = tuple(tuple(pc.C.cast(value) for value in values) for values in (
        (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1),
        (pc.C(F(1, 2), F(1, 3)), pc.C(1, -1), F(2, 3), pc.C(0, F(1, 2))),
        (pc.C(-1, F(2, 5)), F(-1, 4), pc.C(F(2, 7), -1), pc.C(1, 1)),
    ))
    pair_count, triple_count = 0, 0
    for a, b in product(symbols, repeat=2):
        ab = affine_star(a, b)
        aa, bb = pc.hermitian(a[0], a[1:]), pc.hermitian(b[0], b[1:])
        equal(pc.hermitian(ab[0], ab[1:]), pc.multiply(aa, bb),
              "complex affine star is actual Pauli matrix multiplication including scalar parts")
        linear_a, linear_b = symbol((pc.C(),)+a[1:]), symbol((pc.C(),)+b[1:])
        covariance = cadd({zero_degree: sum((a[i]*b[i] for i in range(1, 4)), pc.C())},
                          cscale(-1, cmultiply(linear_a, linear_b)))
        bracket = symbol((pc.C(),)+cross(a[1:], b[1:]))
        differential = cadd(cadd(cmultiply(symbol(a), symbol(b)), covariance), cscale(imaginary, bracket))
        equal(differential, symbol(ab), "differential star cancels all quadratic affine terms exactly")
        equal(tuple(value.conjugate() for value in ab),
              affine_star(tuple(value.conjugate() for value in b), tuple(value.conjugate() for value in a)),
              "symbol involution reverses the affine star product")
        pair_count += 1
    for a, b, c in product(symbols, repeat=3):
        equal(affine_star(affine_star(a, b), c), affine_star(a, affine_star(b, c)),
              "exact affine associativity")
        triple_count += 1
    equal((pair_count, triple_count), (36, 216), "affine product and associativity counts")

    # For functions of z=x1 alone the oriented bracket vanishes; applying the
    # same differential expression to all polynomials is not associative.
    one, z, z2 = monomial(zero_degree), coordinate(3, 0), coordinate(3, 0, 2)
    one_minus_z2 = padd(one, pscale(-1, z2))

    def star_z(p, q):
        return padd(pmul(p, q), pmul(one_minus_z2, pmul(derivative(p, 0), derivative(q, 0))))

    nonaffine_defect = padd(star_z(star_z(z, z), z2), pscale(-1, star_z(z, star_z(z, z2))))
    equal(nonaffine_defect, pscale(-2, pmul(one_minus_z2, one_minus_z2)),
          "nonaffine associator is exactly -2(1-z^2)^2")

    # Ordinary symbol supremum and transported matrix norm are different.
    # The exact decomposition 1-|x1+i*x2|^2=x3^2+(1-|x|^2)
    # bounds the first by one on the ball, attained at (1,0,0).
    witness = tuple(pc.C.cast(value) for value in (0, 1, imaginary, 0))
    matrix_witness = pc.hermitian(witness[0], witness[1:])
    equal(pc.multiply(pc.adjoint(matrix_witness), matrix_witness), pc.matrix(((0, 0), (0, 4))),
          "sigma1+i*sigma2 has squared matrix operator norm four")
    squared_symbol = padd(coordinate(3, 0, 2), coordinate(3, 1, 2))
    radius2 = padd(squared_symbol, coordinate(3, 2, 2))
    equal(padd(one, pscale(-1, squared_symbol)),
          padd(coordinate(3, 2, 2), padd(one, pscale(-1, radius2))),
          "ordinary symbol supremum is at most one on the closed ball")
    equal(1*1+0*0, 1, "ordinary symbol supremum is attained at the first unit vector")
    equal(affine_star(tuple(value.conjugate() for value in witness), witness),
          tuple(pc.C.cast(value) for value in (2, 0, 0, -2)),
          "star squared norm symbol is 2-2*x3, attaining four at x3=-1")
    print("PASS: 64 Jordan covariances, 16 SLD equations, 36 complex affine products and 216 associativity checks are exact; the nonaffine associator and distinct symbol/matrix norms delimit the construction.")


def weighted_hemisphere_geometry():
    cases = 0
    for n, k in ((5, 2), (9, 3), (12, 4)):
        q, effective_dimension = n-k-1, n-1
        require(q > 0, "finite-dimensional weighted Ricci subtraction is defined")
        for multiple in (0, 1, 2):
            x = tuple(F(multiple, j+4) for j in range(k))
            r2 = sum(v*v for v in x)
            y2 = 1-r2
            require(y2 > 0, "hemisphere chart point is interior")
            a = tuple(tuple(F(int(i == j))-x[i]*x[j] for j in range(k)) for i in range(k))
            g = tuple(tuple(F(int(i == j))+x[i]*x[j]/y2 for j in range(k)) for i in range(k))
            equal(mm(a, g), mr.identity(k), "hemisphere inverse metric")
            gradient_v = tuple(q*v/y2 for v in x)
            # In graph coordinates Gamma^l_ij=x_l g_ij; differentiate -q log(y) directly.
            hessian = tuple(tuple(q*F(int(i == j))/y2+2*q*x[i]*x[j]/(y2*y2)
                                   -sum(x[l]*g[i][j]*gradient_v[l] for l in range(k))
                                   for j in range(k)) for i in range(k))
            expected_hessian = tuple(tuple(q*g[i][j]+q*x[i]*x[j]/(y2*y2)
                                            for j in range(k)) for i in range(k))
            equal(hessian, expected_hessian, "covariant Hessian of entropy weight")
            ric_v = mr.add(mr.scale(k-1, g), hessian)
            correction = tuple(tuple(gradient_v[i]*gradient_v[j]/q for j in range(k)) for i in range(k))
            equal(mr.subtract(ric_v, correction), mr.scale(effective_dimension-1, g),
                  "finite-effective-dimension weighted Ricci cancellation")
            gradient_log_w = tuple(-(n-k-2)*v/y2 for v in x)
            drift = tuple(-(k+1)*x[i]+sum(a[i][j]*gradient_log_w[j] for j in range(k)) for i in range(k))
            equal(drift, tuple(-(n-1)*v for v in x), "Lebesgue divergence drift is the descended spherical drift")
            cases += 1
    equal(cases, 9, "weighted hemisphere jet count")
    print("PASS: nine exact hemisphere jets verify the entropy-weight Hessian, effective Ricci cancellation, and descended divergence drift.")


def rising_integer(value, length):
    return math.prod(range(value, value+length))


def beta_power_moment(order, a, b):
    return F(rising_integer(a, order), rising_integer(a+b, order))


def shifted_jacobi_coefficients(ell, a, b):
    """Integer coefficients of P_ell^(b-1,a-1)(2t-1), not normalized at 1.

    Expand sum_j C(ell+b-1,j) C(ell+a-1,ell-j)
    (t-1)^(ell-j) t^j directly, retaining all cancellation exactly.
    """
    coefficients = [0]*(ell+1)
    for j in range(ell+1):
        scale = math.comb(ell+b-1, j)*math.comb(ell+a-1, ell-j)
        for power in range(ell-j+1):
            coefficients[j+power] += scale*math.comb(ell-j, power)*(-1)**(ell-j-power)
    equal(sum(coefficients), math.comb(ell+b-1, ell), "Jacobi endpoint value")
    return coefficients


def integrated_overlap_multiplier(k, ell, a, b):
    coefficients = shifted_jacobi_coefficients(ell, a, b)
    integral = sum(F(value)*beta_power_moment(k+power, a, b)
                   for power, value in enumerate(coefficients))
    return integral/(beta_power_moment(k, a, b)*sum(coefficients))


def overlap_multiplier(k, ell, rho):
    # For ell>k the integer numerator contains a zero, exactly.
    return F(math.prod(range(k-ell+1, k+1)), rising_integer(k+rho, ell))


def overlap_refinement():
    """Exact zonal integrations and sampled refinement, not a full-carrier proof.

    The independent note must identify the zonal harmonic decomposition and
    control its entire tail. This receipt does not infer those facts from a
    finite polynomial fit or choose a Laplacian as the definition of B_k.
    """
    integration_count, integrated_tail_count, normalizations = 0, 0, 0
    families = (("S8", 4, 4), ("OP2", 4, 8))
    powers = (0, 1, 2, 4, 8, 16, 32, 64)
    for _, a, b in families:
        rho = a+b
        beta_normalizer = F(math.factorial(a-1)*math.factorial(b-1), math.factorial(rho-1))
        for k in powers:
            zk = beta_power_moment(k, a, b)
            # Independent integration of t^(a+k-1)(1-t)^(b-1), without
            # using the rising-factorial moment formula on this side.
            expanded = sum(F((-1)**j*math.comb(b-1, j), a+k+j) for j in range(b))
            equal(expanded/beta_normalizer, zk, "overlap kernel normalization")
            equal(2*(zk-beta_power_moment(k+1, a, b))/zk, F(2*b, k+rho),
                  "kernel mean squared overlap distance")
            normalizations += 1
            for ell in range(13):
                actual = integrated_overlap_multiplier(k, ell, a, b)
                expected = overlap_multiplier(k, ell, rho)
                equal(actual, expected, "exact integrated Jacobi multiplier")
                if ell > k:
                    equal(actual, 0, "integrated multiplier vanishes above polynomial degree")
                    equal(k*(1-actual), k, "sampled H_k tail is exactly k")
                    integrated_tail_count += 1
                integration_count += 1
            if k <= 16:
                actual = integrated_overlap_multiplier(k, max(13, k+1), a, b)
                equal(actual, 0, "additional exact integrated tail outside the preceding degree table")
                integration_count += 1
                integrated_tail_count += 1
            if k:
                head = tuple(k*(1-overlap_multiplier(k, ell, rho)) for ell in range(k+1))
                equal(head[0], 0, "normalized constant has zero response")
                require(all(x <= y for x, y in zip(head, head[1:])), "finite head is nondecreasing")
                edge = F(rho*k, k+rho)
                equal(head[1], edge, "exact degree-one response edge")
                require(all(value >= edge for value in head[1:]), "every computed finite-head degree respects edge")
                require(k >= edge, "constant tail formula cannot lower the edge")
    equal((integration_count, normalizations), (220, 16), "overlap exact-case totals")
    print(f"PASS: {integration_count} exact shifted-Jacobi/Beta integrations match falling(k,ell)/rising(k+rho,ell), including {integrated_tail_count} integrated zero tails.")
    print("PASS: 16 independent kernel normalizations and displacement moments give Z_k=(a)_k/(a+b)_k and E_k[2(1-t)]=2b/(k+a+b); finite-head edges equal rho*k/(k+rho).")
    print("Overlap refinement: H_k=k(I-B_k); displayed degrees ell=1,2,4, not a harmonic cutoff proof.")
    for label, a, b in families:
        rho = a+b
        degrees = (1, 2, 4)
        targets = tuple(ell*(ell+rho-1) for ell in degrees)
        print(f"{label}: rho={rho}, limiting eigenvalues={targets}")
        previous = (F(0),)*len(degrees)
        for k in (1, 4, 16, 64, 256, 1024):
            values = tuple(k*(1-overlap_multiplier(k, ell, rho)) for ell in degrees)
            require(all(old < value <= limit for old, value, limit in zip(previous, values, targets)),
                    "sampled refinement increases toward the stated limiting levels")
            equal(values[0], F(rho*k, k+rho), "refinement table retains exact degree-one edge")
            print(f"  k={k:4d}: " + ", ".join(f"{float(value):.9f}" for value in values))
            previous = values
    print("The full-harmonic spectrum and operator convergence require the shared decomposition/tail theorem; these exact finite integrations do not supply it.")


def main():
    ambient_descent()
    polynomial_eigenfunctions()
    moment_integration_by_parts()
    radial_normalization()
    forgotten_rotation()
    finite_entropy_calibration()
    pseudodeterminant_angle_failure()
    jordan_and_sld()
    weighted_hemisphere_geometry()
    overlap_refinement()
    print("All ten check groups passed. Stdlib only; stdout only; no files written.")
    print("Exact low-degree identities and finite entropy calibrations do not prove global domains or a continuum spectral theorem.")
    print("The three Bloch coordinates are not, by this calculation, three spatial coordinates or a spacetime observable net.")


if __name__ == "__main__":
    main()
