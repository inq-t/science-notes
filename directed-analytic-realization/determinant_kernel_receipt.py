"""Exact finite checks for determinant preparation kernels on Herm_2(C).

The six-point obstruction uses rational Hermitian matrices and certified
rational bounds on square roots. Its sign is never inferred from floats.
Positive integer samples use exact LDL congruence, not an eigensolver.
Fourth-order Taylor jets independently check the determinant differential
coefficient at finitely many rational parameters. Positive diagonal
congruence relates normalized and unnormalized Gram matrices.

The inherited Gaussian-rational helpers have a guarded main. No files,
network, random sampling, external dependencies or runtime writes are used.
These checks do not prove the global kernel classification, the integral
representations, spectral support, a physical clock, or a mass gap.
"""

from fractions import Fraction as F
from itertools import product

import positive_cone_process_receipt as pc


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def equal(actual, expected, label):
    require(actual == expected, f"{label}: {actual!r} != {expected!r}")


def det(a):
    return pc.real(pc.determinant(a))


def strict_positive(a):
    equal(a, pc.adjoint(a), "Hermitian cone input")
    require(pc.real(a[0][0]) > 0 and det(a) > 0,
            "positive first pivot and determinant")


def exact_psd(a):
    """PSD certificate by rational symmetric Schur/LDL congruences."""
    work = [list(map(F, row)) for row in a]
    n = len(work)
    equal(work, [list(row) for row in zip(*work)], "symmetric real Gram")
    rank = 0
    for j in range(n):
        pivot = work[j][j]
        require(pivot >= 0, "nonnegative LDL pivot")
        if pivot == 0:
            require(all(work[j][k] == 0 for k in range(j+1, n)),
                    "zero pivot has zero remaining row")
            continue
        rank += 1
        for r in range(j+1, n):
            for c in range(j+1, n):
                work[r][c] -= work[r][j]*work[j][c]/pivot
    return rank


def square_part(n):
    """Return q,r with n=q*q*r and r square-free, by integer division."""
    q, r, prime = 1, 1, 2
    while prime*prime <= n:
        power = 0
        while n % prime == 0:
            n //= prime
            power += 1
        q *= prime**(power//2)
        r *= prime**(power % 2)
        prime += 1
    return q, r*n


TETRAHEDRON = ((1, 1, 1), (1, -1, -1),
               (-1, 1, -1), (-1, -1, 1))
POINTS = (pc.scale(pc.I, F(5, 4)), pc.scale(pc.I, F(3, 4))) + tuple(
    pc.hermitian(1, tuple(F(v, 4) for v in vector))
    for vector in TETRAHEDRON)
COEFFICIENTS = (2, 2, -1, -1, -1, -1)


def six_point_gram_test():
    for a in POINTS:
        strict_positive(a)
    equal(sum(COEFFICIENTS), 0, "signed coefficients cancel constants")
    first_moment = pc.matrix(((0, 0), (0, 0)))
    for coefficient, a in zip(COEFFICIENTS, POINTS):
        first_moment = pc.add(first_moment, pc.scale(a, coefficient))
    equal(first_moment, pc.matrix(((0, 0), (0, 0))),
          "signed points cancel all affine matrix coordinates")
    determinants = [[det(pc.add(a, b)) for b in POINTS] for a in POINTS]
    grouped = {}
    for i, j in product(range(6), repeat=2):
        value = determinants[i][j]
        grouped[value] = grouped.get(value, 0)+COEFFICIENTS[i]*COEFFICIENTS[j]
    equal(grouped, {F(25, 4): 4, F(9, 4): 4, F(4): 8,
                    F(39, 8): -16, F(23, 8): -16,
                    F(13, 4): 4, F(15, 4): 12},
          "all 36 Gram entries reduce to seven determinant types")
    radicals = {}
    for value, coefficient in grouped.items():
        q, r = square_part(value.numerator*value.denominator)
        equal(q*q*r, value.numerator*value.denominator,
              "exact square-root factorization")
        radicals[r] = radicals.get(r, F(0))+F(coefficient*value.denominator, q)
    equal(radicals, {1: F(124, 15), 78: F(-64), 46: F(-64),
                     13: F(8), 15: F(24)}, "beta=1/2 exact radical expression")
    lower = {13: F(36055, 10000), 15: F(38729, 10000)}
    upper = {78: F(88318, 10000), 46: F(67824, 10000)}
    for n, bound in lower.items():
        require(bound > 0 and bound*bound < n, "certified lower root bound")
    for n, bound in upper.items():
        require(bound > 0 and bound*bound > n, "certified upper root bound")
    q_upper = radicals[1]+sum(radicals[n]/bound for n, bound in lower.items())
    q_upper += sum(radicals[n]/bound for n, bound in upper.items())
    equal(q_upper, F(-84420832374148, 261387268239424095),
          "exact strict upper bound on the signed Gram quadratic form")
    require(q_upper < 0, "six positive points refute beta=1/2 positivity")
    ranks = []
    for beta in (1, 2):
        gram = [[value**(-beta) for value in row] for row in determinants]
        ranks.append(exact_psd(gram))
        if beta == 2:
            diagonal = [det(pc.scale(a, 2)) for a in POINTS]
            normalized = [[diagonal[i]*gram[i][j]*diagonal[j]
                           for j in range(6)] for i in range(6)]
            equal([normalized[i][i] for i in range(6)], [F(1)]*6,
                  "beta=2 diagonal congruence normalizes every vector")
            equal(exact_psd(normalized), 6, "normalized beta=2 Gram stays positive")
    equal(ranks, [6, 6], "beta=1 and beta=2 sample Grams are positive definite")
    # For beta=-1 the scalar pair I,2I already violates normalized Cauchy--Schwarz.
    off_diagonal = F(8, 9)**(-1)
    require(1-off_diagonal**2 < 0, "negative exponent fails a two-point Gram")
    print("PASS: six rational positive points give beta=1/2 Gram quadratic Q < "
          "-84420832374148/261387268239424095 < 0; all radical bounds are squared rational checks.")
    print("PASS: beta=1 and beta=2 six-point Grams are positive definite by exact LDL; "
          "normalization is positive diagonal congruence, and beta=-1 fails a scalar two-point test.")


ZERO = (0, 0, 0, 0)


def poly_add(*polynomials):
    out = {}
    for polynomial in polynomials:
        for powers, value in polynomial.items():
            out[powers] = out.get(powers, F(0))+value
    return {powers: value for powers, value in out.items() if value}


def poly_scale(polynomial, coefficient):
    return {powers: coefficient*value for powers, value in polynomial.items()
            if coefficient*value}


def poly_multiply(a, b):
    out = {}
    for powers, x in a.items():
        for other, y in b.items():
            combined = tuple(p+q for p, q in zip(powers, other))
            if sum(combined) <= 4:
                out[combined] = out.get(combined, F(0))+x*y
    return {powers: value for powers, value in out.items() if value}


def derivative(polynomial, coordinate):
    out = {}
    for powers, value in polynomial.items():
        if powers[coordinate]:
            reduced = list(powers)
            reduced[coordinate] -= 1
            out[tuple(reduced)] = powers[coordinate]*value
    return out


def cayley(polynomial):
    return poly_add(derivative(derivative(polynomial, 0), 1),
                    poly_scale(derivative(derivative(polynomial, 2), 2), F(-1, 4)),
                    poly_scale(derivative(derivative(polynomial, 3), 3), F(-1, 4)))


def determinant_derivative_jets():
    cases = 0
    beta_values = tuple(map(F, (0, 1, 2, 3))) + (F(1, 4), F(1, 2), F(3, 4), F(3, 2))
    for a, b, x, y in ((F(2), F(2), F(0), F(0)),
                        (F(2), F(3), F(1, 2), F(-1, 4)),
                        (F(3, 2), F(5, 3), F(-2, 5), F(1, 3))):
        delta = a*b-x*x-y*y
        require(delta > 0 and a > 0, "Taylor center is in the open cone")
        increment = {(1, 0, 0, 0): b, (0, 1, 0, 0): a,
                     (0, 0, 1, 0): -2*x, (0, 0, 0, 1): -2*y,
                     (1, 1, 0, 0): F(1), (0, 0, 2, 0): F(-1),
                     (0, 0, 0, 2): F(-1)}
        q = poly_scale(increment, 1/delta)
        for beta in beta_values:
            # The exact degree-four jet of det(C+h)^(-beta)/det(C)^(-beta).
            jet, power, coefficient = {ZERO: F(1)}, {ZERO: F(1)}, F(1)
            for order in range(1, 5):
                power = poly_multiply(power, q)
                coefficient *= (-beta-order+1)/order
                jet = poly_add(jet, poly_scale(power, coefficient))
            first = cayley(jet).get(ZERO, F(0))
            second = cayley(cayley(jet)).get(ZERO, F(0))
            equal(first, beta*(beta-1)/delta, "first Cayley derivative from Taylor coefficients")
            equal(second, beta*beta*(beta*beta-1)/(delta*delta),
                  "fourth mixed derivative from independent determinant jet")
            if 0 < beta < 1:
                require(second < 0, "forbidden interval has a negative same-functional derivative")
            cases += 1
    equal(cases, 24, "rational Taylor-jet case count")
    print("PASS: 24 exact fourth-order determinant jets independently give "
          "D^2 det(C)^(-beta)/det(C)^(-beta) = beta^2(beta^2-1)/det(C)^2, "
          "including negative values throughout the three tested forbidden exponents.")


def normalized_squared(a, b, beta):
    return (det(pc.scale(a, 2))*det(pc.scale(b, 2)))**beta/det(pc.add(a, b))**(2*beta)


def block_sum(a, b):
    return pc.matrix([list(row)+[0]*len(b) for row in a]
                     + [[0]*len(a)+list(row) for row in b])


def normalized_covariance_and_cost():
    cases = 0
    pairs = ((POINTS[0], POINTS[2]), (POINTS[1], POINTS[3]),
             (POINTS[2], POINTS[5]))
    for a, b in pairs:
        for beta in (1, 2, 3):
            reference = normalized_squared(a, b, beta)
            require(0 < reference <= 1, "normalized squared pairing is bounded on these points")
            for transform in pc.CONGRUENCES:
                determinant_scale = pc.real(pc.determinant(transform)*pc.determinant(transform).conjugate())
                require(determinant_scale > 0, "congruence is invertible")
                transformed_a = pc.conjugate(a, transform)
                transformed_b = pc.conjugate(b, transform)
                equal(det(transformed_a), determinant_scale*det(a), "congruence determinant character")
                equal(normalized_squared(transformed_a, transformed_b, beta), reference,
                      "normalized determinant character cancels under simultaneous congruence")
                cases += 1
            for scale in (F(1, 3), F(2), F(7, 2)):
                equal(normalized_squared(pc.scale(a, scale), pc.scale(b, scale), beta), reference,
                      "common positive scale cancels")
                cases += 1
    product_cases = 0
    for (a, b), (c, d) in product(pairs, repeat=2):
        left, right = block_sum(a, c), block_sum(b, d)
        equal(det(left), det(a)*det(c), "direct-sum determinant factorization")
        equal(normalized_squared(left, right, 1),
              normalized_squared(a, b, 1)*normalized_squared(c, d, 1),
              "direct-sum normalized product; equivalently additive negative log cost")
        product_cases += 1
    equal((cases, product_cases), (54, 9), "normalization and direct-sum counts")
    print("PASS: 54 exact normalized congruence/scaling checks and nine direct-sum "
          "product identities; logarithmic cost additivity is tested in its equivalent multiplicative form.")


def radial_preparation_moments():
    curves = 0
    # The beta=1/2 case is only a radial restriction: its full-cone
    # kernel is inadmissible, as the independent Gram witness proves.
    for beta in (F(1, 2), F(1), F(3, 2), F(2), F(3)):
        power = int(2*beta)
        equal(power, 2*beta, "integer radial power permits rational samples")
        previous_mean = None
        for a in (F(1), F(2), F(4), F(8), F(16), F(32)):
            # Exact first two Taylor coefficients of (1+s/(2a))^(-power).
            first_coefficient = F(-power)/(2*a)
            second_coefficient = F(power*(power+1), 2)/(2*a)**2
            mean, second_moment = -first_coefficient, 2*second_coefficient
            equal(mean, beta/a, "radial first moment")
            equal(second_moment, beta*(2*beta+1)/(2*a*a), "radial second moment")
            equal(second_moment-mean*mean, beta/(2*a*a), "positive radial variance")
            if previous_mean is not None:
                equal(mean, previous_mean/2, "doubling preparation scale halves the mean")
            previous_mean = mean
            radial = lambda s: (2*a/(2*a+s))**power
            equal(radial(0), 1, "normalized preparation curve")
            for s in (F(1, 3), F(1), F(3)):
                require(radial(2*s) > radial(s)**2,
                        "radial attenuation is not a scalar exponential semigroup")
                require(radial(s) >= 1-mean*s,
                        "sampled convex tangent bound approaches one as the mean decreases")
                equal(radial(2*s)/radial(s)**2,
                      ((2*a+s)**2/(2*a*(2*a+2*s)))**power,
                      "exact nonexponential attenuation ratio")
            curves += 1
    equal(curves, 30, "radial curve count")
    print("PASS: 30 rational radial curves have mean beta/a and variance beta/(2a^2); "
          "doubling a halves the mean, and exact attenuation ratios differ from an exponential semigroup.")


def main():
    six_point_gram_test()
    determinant_derivative_jets()
    normalized_covariance_and_cost()
    radial_preparation_moments()
    print("All four check groups passed. Exact rational arithmetic; stdlib only; stdout only; no files written.")
    print("Scope: finite Gram, differential-jet, normalization and radial-moment checks. "
          "No global positivity classification, Gaussian integral or spectral-support theorem is numerically inferred.")
    print("The exponent obstruction is not an energy threshold; no physical clock, scale, locality or Yang--Mills mass gap is established.")


if __name__ == "__main__":
    main()
