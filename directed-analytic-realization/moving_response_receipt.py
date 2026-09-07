"""Stdlib, stdout-only checks for a moving response balance.

Rectangular cocycles, moving-frame jets, characteristic-polynomial ratios,
skew freedom, one-step Peirce defects and trace clocks use exact Fraction
arithmetic. Exponential yardsticks and interpolation times use numerical
arithmetic. Elementary multiplication/assertion helpers are reused from the
adjacent context_transport_receipt; importing it does not run its checks.

These checks verify finite identities on declared carriers, not selection of
a physical clock, irreversible records, spacetime or a quantum-field gap.
No explicit filesystem I/O, network calls, third-party dependencies or eigensolvers.
"""

from fractions import Fraction as F
from itertools import combinations, permutations
import math

from context_transport_receipt import close, equal, mm, require


def identity(n):
    return tuple(tuple(F(int(i == j)) for j in range(n)) for i in range(n))


def diagonal(values):
    return tuple(tuple(F(values[i])*int(i == j) for j in range(len(values)))
                 for i in range(len(values)))


def rational(a):
    return tuple(tuple(F(x) for x in row) for row in a)


def transpose(a):
    return tuple(zip(*a))


def scale(c, a):
    return tuple(tuple(c*x for x in row) for row in a)


def add(a, b):
    return tuple(tuple(x+y for x, y in zip(row, other)) for row, other in zip(a, b))


def subtract(a, b):
    return add(a, scale(-1, b))


def congruence(g, s):
    return mm(mm(transpose(s), g), s)


def inverse(a):
    n = len(a)
    rows = [list(row)+list(unit) for row, unit in zip(a, identity(n))]
    for column in range(n):
        pivot = next(i for i in range(column, n) if rows[i][column] != 0)
        rows[column], rows[pivot] = rows[pivot], rows[column]
        divisor = rows[column][column]
        rows[column] = [x/divisor for x in rows[column]]
        for i in range(n):
            if i != column:
                coefficient = rows[i][column]
                rows[i] = [x-coefficient*y for x, y in zip(rows[i], rows[column])]
    result = tuple(tuple(row[n:]) for row in rows)
    equal(mm(a, result), identity(n), "exact frame inverse")
    return result


def permutation_sign(p):
    return (-1)**sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p)))


def determinant(a):
    return sum(permutation_sign(p)*math.prod(a[i][p[i]] for i in range(len(a)))
               for p in permutations(range(len(a))))


def positive_semidefinite(a, label):
    equal(a, transpose(a), label+" is symmetric")
    # For real symmetric finite matrices, nonnegative ALL principal minors characterize PSD.
    for size in range(1, len(a)+1):
        for indices in combinations(range(len(a)), size):
            submatrix = tuple(tuple(a[i][j] for j in indices) for i in indices)
            require(determinant(submatrix) >= 0, label+" has nonnegative principal minors")


def quadratic(a, x):
    return sum(x[i]*a[i][j]*x[j] for i in range(len(x)) for j in range(len(x)))


def response(g, g_dot, k):
    return scale(-1, add(g_dot, add(mm(transpose(k), g), mm(g, k))))


def arrow_defect(source, target, arrow):
    return subtract(source, congruence(target, arrow))


def rectangular_cocycle():
    frames = (
        (diagonal((1, 2, 3)), diagonal((2, 1)), diagonal((1, 2, 1, 3))),
        (rational(((1, 1, 0), (0, 2, 1), (0, 0, 1))),
         rational(((2, 1), (0, 1))),
         rational(((1, 1, 0, 0), (0, 1, 1, 0), (0, 0, 2, 1), (0, 0, 0, 1))))
    )
    cases = 0
    for t0, t1, t2 in frames:
        g0, g1, g2 = (mm(transpose(t), t) for t in (t0, t1, t2))
        for c in (F(1), F(1, 2), F(2, 3)):
            a = scale(c, rational(((F(3, 5), 0, 0), (0, F(1, 2), 0))))
            b = rational(((F(1, 3), 0), (0, F(1, 4)), (F(1, 3), 0), (0, F(1, 4))))
            f = mm(mm(inverse(t1), a), t0)
            h = mm(mm(inverse(t2), b), t1)
            d01 = arrow_defect(g0, g1, f)
            d12 = arrow_defect(g1, g2, h)
            d02 = arrow_defect(g0, g2, mm(h, f))
            for defect in (d01, d12, d02):
                positive_semidefinite(defect, "rectangular contractive defect")
            equal(d02, add(d01, congruence(d12, f)), "exact pulled-back defect cocycle")
            for x in ((F(1), F(0), F(0)), (F(1, 3), F(-2), F(4, 5))):
                fx = tuple(sum(row[j]*x[j] for j in range(3)) for row in f)
                equal(quadratic(g0, x), quadratic(g1, fx)+quadratic(d01, x),
                      "incoming retained-plus-defect balance")
            # The erased third Euclidean component remains visible as an incoming defect.
            erased = tuple(row[2] for row in inverse(t0))
            equal(tuple(sum(row[j]*erased[j] for j in range(3)) for row in f), (0, 0),
                  "rectangular arrow really erases a nonzero direction")
            equal(quadratic(d01, erased), quadratic(g0, erased), "erased input is not an output tangent")
            cases += 1
    equal(cases, 6, "rectangular cocycle count")
    print("PASS: six exact 3-to-2-to-4 contraction chains verify positive defects, pulled-back cocycles, and erased incoming directions.")


def moving_frames():
    data = (
        (rational(((2, 1), (1, 3))), rational(((1, 2), (2, -1))),
         rational(((3, 1), (1, 2))), rational(((1, 1), (0, 2)))),
        (rational(((3, 1, 0), (1, 2, 1), (0, 1, 3))),
         rational(((1, 0, 2), (0, -1, 1), (2, 1, 0))),
         rational(((2, 0, 1), (0, 3, 1), (1, 1, 2))),
         rational(((1, 1, 0), (0, 2, 1), (0, 0, 1))))
    )
    returned = []
    for g, g_dot, r, s in data:
        n = len(g)
        positive_semidefinite(g, "reference response")
        positive_semidefinite(r, "chosen loss form")
        require(determinant(g) > 0, "response is positive definite")
        q = tuple(tuple(F(j-i) for j in range(n)) for i in range(n))
        k = mm(inverse(g), subtract(q, scale(F(1, 2), add(r, g_dot))))
        equal(response(g, g_dot, k), r, "original moving response jet")
        for alpha in (F(-1), F(1, 2), F(2)):
            s_dot = tuple(tuple(alpha*F(1+i+2*j) for j in range(n)) for i in range(n))
            g_new = congruence(g, s)
            g_dot_new = add(add(mm(mm(transpose(s_dot), g), s), congruence(g_dot, s)),
                            mm(mm(transpose(s), g), s_dot))
            k_new = subtract(mm(mm(inverse(s), k), s), mm(inverse(s), s_dot))
            r_new = response(g_new, g_dot_new, k_new)
            equal(r_new, congruence(r, s), "all moving-frame derivatives cancel in R")
            naive_k = mm(mm(inverse(s), k), s)
            require(response(g_new, g_dot_new, naive_k) != r_new,
                    "omitting the frame-velocity term changes the response")
            returned.append((r, g, s))
    equal(len(returned), 6, "moving-frame jet count")
    print("PASS: six exact moving-frame jets include S-dot and preserve R by congruence; omitting S-dot fails each test.")
    return returned


def polynomial_product(a, b):
    result = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return tuple(result)


def determinant_polynomial(a, b):
    # Coefficients of det(A+z B), computed exactly without eigenvalues.
    n = len(a)
    result = [F(0)]*(n+1)
    for permutation in permutations(range(n)):
        term = (F(permutation_sign(permutation)),)
        for i in range(n):
            j = permutation[i]
            term = polynomial_product(term, (a[i][j], b[i][j]))
        result = [x+y for x, y in zip(result, term)]
    return tuple(result)


def normalized_pencil_polynomial(r, c):
    # Coefficients of det(R-lambda C)/det(C), not an eigenvalue approximation.
    result = determinant_polynomial(r, scale(-1, c))
    divisor = determinant(c)
    require(divisor > 0, "comparison form determinant is positive")
    return tuple(x/divisor for x in result)


def pencil_invariance(data):
    cases = 0
    for r, c, s in data:
        polynomial = normalized_pencil_polynomial(r, c)
        r_new, c_new = congruence(r, s), congruence(c, s)
        equal(normalized_pencil_polynomial(r_new, c_new), polynomial,
              "generalized characteristic polynomial invariant under nonorthogonal congruence")
        for weight in (F(1, 3), F(2), F(7)):
            equal(normalized_pencil_polynomial(scale(weight, r_new), scale(weight, c_new)), polynomial,
                  "common process-density weight cancels from the pencil")
            # Weighting R but not C rescales generalized eigenvalues, rather than leaving them fixed.
            scaled = normalized_pencil_polynomial(scale(weight, r), c)
            equal(scaled, tuple(value*weight**(len(r)-degree)
                                for degree, value in enumerate(polynomial)),
                  "relative rate against a weight-zero form changes under reparameterization")
            cases += 1
    equal(cases, 18, "weighted pencil comparison count")
    print("PASS: 18 exact characteristic-polynomial ratios verify frame and common-clock-weight invariance, but not invariance of an uncalibrated rate.")


def determinant_process_clock(data):
    def ratio(g0, g1, f):
        return determinant(congruence(g1, f))/determinant(g0)

    cases = 0
    for n in (2, 3):
        t0 = tuple(tuple(F(2 if i == j else int(j == i+1)) for j in range(n)) for i in range(n))
        t1 = tuple(tuple(F(1 if i == j else int(j == i+1)) for j in range(n)) for i in range(n))
        t2 = diagonal(tuple(range(1, n+1)))
        g0, g1, g2 = (mm(transpose(t), t) for t in (t0, t1, t2))
        rotation = [list(row) for row in identity(n)]
        rotation[0][:2], rotation[1][:2] = [F(3, 5), F(-4, 5)], [F(4, 5), F(3, 5)]
        rotation = tuple(tuple(row) for row in rotation)
        equal(mm(transpose(rotation), rotation), identity(n), "exact mixing rotation")
        for c in (F(1), F(1, 2), F(2, 3)):
            a = scale(c, diagonal(tuple(F(j+1, j+2) for j in range(n))))
            b = mm(rotation, diagonal(tuple(F(1, j+2) for j in range(n))))
            f = mm(mm(inverse(t1), a), t0)
            h = mm(mm(inverse(t2), b), t1)
            for defect in (arrow_defect(g0, g1, f), arrow_defect(g1, g2, h)):
                positive_semidefinite(defect, "invertible determinant-clock contraction")
            q01, q12, q02 = ratio(g0, g1, f), ratio(g1, g2, h), ratio(g0, g2, mm(h, f))
            require(0 < q01 <= 1 and 0 < q12 <= 1 and 0 < q02 <= 1,
                    "response-volume determinant ratios are positive contractions")
            equal(q02, q01*q12, "exact determinant cocycle before logarithms")
            close(-math.log(float(q02))/n,
                  -math.log(float(q01))/n-math.log(float(q12))/n,
                  "numerical logarithmic process-clock additivity")
            # Change both endpoint frames independently; the determinant ratio is unchanged.
            s0, s1 = t1, t0
            f_new = mm(mm(inverse(s1), f), s0)
            equal(ratio(congruence(g0, s0), congruence(g1, s1), f_new), q01,
                  "exact endpoint-frame invariance of determinant cost")
            cases += 1
    equal(cases, 6, "determinant cocycle count")
    for r, g, _ in data:
        relative = mm(inverse(g), r)
        derivative = determinant_polynomial(identity(len(g)), scale(-1, relative))[1]
        ell = sum(relative[i][i] for i in range(len(g)))/len(g)
        equal(-derivative/len(g), ell, "exact Jacobi first-jet of normalized negative log determinant")
    integral_cases = 0
    for n in (2, 3):
        alphas = (1.0, -2.0, 3.0)[:n]
        ks = (-1.0, 0.0, -2.0)[:n]
        ell = -sum(alpha+2*k for alpha, k in zip(alphas, ks))/n
        for u0, u1 in ((-1.0, 0.0), (0.0, 0.25), (0.25, 1.0), (1.0, 2.0)):
            q = math.prod(math.exp(-alpha*u0)*math.exp(2*k*(u1-u0))*math.exp(alpha*u1)
                          for alpha, k in zip(alphas, ks))
            close(-math.log(q)/n, ell*(u1-u0), "integrated trace rate equals endpoint determinant cost")
            integral_cases += 1
    equal(integral_cases, 8, "integrated clock calibration count")
    singular = diagonal((1, 0))
    equal(ratio(identity(2), identity(2), singular), 0, "singular arrow has zero determinant, not a finite log cost")
    print("PASS: six exact determinant cocycles, six Jacobi jets, and eight numerical integrals verify the additive response-volume clock; singular arrows remain excluded.")


def changing_yardsticks():
    points = (-1.0, 0.0, 0.5, 1.0, 2.0)
    for u in points:
        g = math.exp(2*u)
        g_dot, k = 2*g, -1.0
        r = -g_dot-2*g*k
        close(r, 0, "growing yardstick exactly compensates shrinking coordinate")
        close(g*math.exp(-u)**2, 1, "moving response of actual transported vector")
        s = math.exp(-u)
        s_dot = -s
        close(s*s*g, 1, "normalized moving frame metric")
        close(k-s_dot/s, 0, "normalized moving frame generator")
        decreasing_g = math.exp(-2*u)
        decreasing_r = 2*decreasing_g
        close(decreasing_r/decreasing_g, 2, "stationary-coordinate moving-yardstick loss")
    for u0, u1 in zip(points, points[1:]):
        t = math.exp(-(u1-u0))
        close(math.exp(2*u0)-t*t*math.exp(2*u1), 0, "finite-step compensated defect")
        defect = math.exp(-2*u0)-math.exp(-2*u1)
        require(defect > 0, "decreasing response has positive finite-step defect")
        close(defect, 2*(math.exp(-2*u0)-math.exp(-2*u1))/2,
              "integrated decreasing-yardstick response")
    print("PASS: five numerical yardstick states and four intervals distinguish compensated coordinate decay from actual response loss.")


def skew_freedom():
    r = rational(((2, 1), (1, 3)))
    determinants = set()
    for alpha in (F(-3), F(0), F(1, 2), F(2)):
        q = rational(((0, alpha), (-alpha, 0)))
        k = subtract(q, scale(F(1, 2), r))
        equal(scale(-1, add(k, transpose(k))), r, "same response for arbitrary skew part")
        for x in ((F(1), F(2)), (F(-1, 2), F(3, 4))):
            equal(quadratic(k, x), -quadratic(r, x)/2, "skew part contributes no real norm loss")
        determinants.add(determinant(k))
    equal(len(determinants), 4, "different generator polynomials share the same loss form")
    print("PASS: four exact skew choices preserve the whole positive response while changing the generator's characteristic polynomial.")


def peirce_and_clock_normalization():
    g = identity(3)
    phi = scale(F(1, 3), g)
    equal(arrow_defect(g, g, phi), scale(F(8, 9), g), "exact one-step Peirce defect")
    k_poisson = scale(F(-2, 3), g)
    equal(response(g, scale(0, g), k_poisson), scale(F(4, 3), g), "exact Poisson infinitesimal response")
    t_poisson = 1.5*math.log(3)
    close(math.exp(-2*t_poisson/3), 1/3, "Poisson duration of the original channel")
    close(3**-1, 1/3, "logarithmic duration of the original channel")
    for s in (0.0, 0.25, 0.75, 1.0, t_poisson):
        poisson = math.exp(-2*s/3)
        logarithmic = math.exp(-s*math.log(3))
        poisson_defect = 1-poisson*poisson
        logarithmic_defect = 1-logarithmic*logarithmic
        close(poisson_defect, 1-math.exp(-4*s/3), "pulled-back Poisson rate integrates to its finite defect")
        close(logarithmic_defect, 1-math.exp(-2*s*math.log(3)), "pulled-back logarithmic rate integrates to its finite defect")
    close(1-math.exp(-4*t_poisson/3), 8/9, "Poisson channel duration returns exact step defect")
    close(1-math.exp(-2*math.log(3)), 8/9, "logarithmic unit duration returns exact step defect")
    step_determinant = determinant(congruence(g, phi))/determinant(g)
    equal(step_determinant, F(1, 729), "three-dimensional Peirce response-volume squared")
    close(-math.log(float(step_determinant))/3, 2*math.log(3), "intrinsic one-step determinant cost")
    close((4/3)*t_poisson, 2*math.log(3), "Poisson trace-clock cost at channel duration")
    require(abs(math.exp(-2/3)-1/3) > 0.1, "Poisson unit duration is not the original channel")
    require(abs(4/3-2*math.log(3)) > 0.5, "interpolation rates are genuinely different")
    print("PASS: exact Peirce defect 8/9 and distinct interpolation rates return the same intrinsic step cost 2log(3), at their different durations.")


def trace_clock_without_floor():
    for denominator in (2, 4, 8, 16, 64, 256, 4096):
        epsilon = F(1, denominator)
        r = diagonal((2-epsilon, epsilon))
        ell = sum(r[i][i] for i in range(2))/2
        equal(ell, 1, "trace-selected clock has constant unit mean")
        c = scale(ell, identity(2))
        equal(quadratic(r, (F(0), F(1)))/quadratic(c, (F(0), F(1))), epsilon,
              "normalized response retains arbitrarily slow direction")
        expected = polynomial_product((2-epsilon, -1), (epsilon, -1))
        equal(normalized_pencil_polynomial(r, c), expected, "exact complete pencil in trace-clock family")
    print("PASS: seven exact trace-clock models have mean rate one while their minimum remains epsilon tending to zero.")


def main():
    rectangular_cocycle()
    data = moving_frames()
    pencil_invariance(data)
    determinant_process_clock(data)
    changing_yardsticks()
    skew_freedom()
    peirce_and_clock_normalization()
    trace_clock_without_floor()
    print("All eight check groups passed. Stdlib only; stdout only; no files written.")
    print("Finite matrix identities and numerical exponentials do not select physical clocks, records, spacetime or a mass gap.")


if __name__ == "__main__":
    main()
