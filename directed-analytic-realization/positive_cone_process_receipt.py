"""Stdlib, stdout-only checks for the positive-cone process notes.

Gaussian rational matrices give exact finite identities. The finite-difference,
semigroup exponential and hyperbolic quadrature comparisons are explicitly
numerical checks, not proofs. Matrix pinching and compression are actual CP
maps on associative matrix algebras; they do not simulate the full Albert
algebra. The isolated octonionic 13-entry check uses only norm composition.

No files, network, external dependencies, Monte Carlo or eigensolvers are used.
No physical mass, continuum gap or complete exceptional realization is computed.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations
import math


@dataclass(frozen=True)
class C:
    """An exact rational complex number, with no binary-float matrix arithmetic."""
    real: F = F(0)
    imag: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "real", F(self.real))
        object.__setattr__(self, "imag", F(self.imag))

    @staticmethod
    def cast(value):
        return value if isinstance(value, C) else C(value)

    def __add__(self, other):
        other = C.cast(other)
        return C(self.real+other.real, self.imag+other.imag)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.real, -self.imag)

    def __sub__(self, other):
        return self + (-C.cast(other))

    def __rsub__(self, other):
        return C.cast(other) + (-self)

    def __mul__(self, other):
        other = C.cast(other)
        return C(self.real*other.real-self.imag*other.imag,
                 self.real*other.imag+self.imag*other.real)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = C.cast(other)
        denominator = other.real**2+other.imag**2
        if denominator == 0:
            raise ZeroDivisionError("zero Gaussian rational")
        numerator = self*other.conjugate()
        return C(numerator.real/denominator, numerator.imag/denominator)

    def conjugate(self):
        return C(self.real, -self.imag)


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def equal(actual, expected, label):
    require(actual == expected, f"{label}: {actual!r} != {expected!r}")


def close(actual, expected, label, tolerance=2e-11):
    require(math.isclose(float(actual), float(expected), rel_tol=tolerance,
                         abs_tol=tolerance),
            f"{label}: {actual!r} != {expected!r}")


def matrix(rows):
    return [[C.cast(value) for value in row] for row in rows]


def identity(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def add(a, b):
    return [[x+y for x, y in zip(row, other)] for row, other in zip(a, b)]


def scale(a, value):
    return [[value*x for x in row] for row in a]


def sub(a, b):
    return add(a, scale(b, -1))


def adjoint(a):
    return [[value.conjugate() for value in row] for row in zip(*a)]


def multiply(a, b):
    return [[sum(x*y for x, y in zip(row, column)) for column in zip(*b)]
            for row in a]


def conjugate(a, s):
    return multiply(multiply(s, a), adjoint(s))


def real(value):
    equal(value.imag, 0, "real scalar identity")
    return value.real


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def determinant(a):
    if len(a) == 1:
        return a[0][0]
    return sum((-1)**j*a[0][j]*determinant(
        [[row[k] for k in range(len(a)) if k != j] for row in a[1:]])
        for j in range(len(a)))


def positive_semidefinite(a):
    equal(a, adjoint(a), "Hermitian PSD input")
    for size in range(1, len(a)+1):
        for indices in combinations(range(len(a)), size):
            minor = [[a[i][j] for j in indices] for i in indices]
            require(real(determinant(minor)) >= 0, "nonnegative principal minor")


def inverse2(a):
    return scale([[a[1][1], -a[0][1]], [-a[1][0], a[0][0]]],
                 C(1)/determinant(a))


I = identity(2)
PAULI = (matrix([[0, 1], [1, 0]]),
         matrix([[0, C(0, -1)], [C(0, 1), 0]]),
         matrix([[1, 0], [0, -1]]))


def hermitian(t, vector):
    out = scale(I, t)
    for coefficient, sigma in zip(vector, PAULI):
        out = add(out, scale(sigma, coefficient))
    return out


UNITS = (I, hermitian(2, (F(1, 2), F(1, 3), F(1, 4))),
         hermitian(3, (1, 1, 1)),
         hermitian(F(5, 2), (F(1, 3), F(-2, 3), F(1, 2))))
TANGENTS = (I,) + PAULI + (
    hermitian(2, (1, F(1, 2), F(-1, 3))),
    hermitian(-1, (2, 1, 0)),
    hermitian(0, (F(1, 3), F(-1, 2), F(3, 2))))
CONGRUENCES = (I, matrix([[1, C(1, 1)], [0, 1]]),
               matrix([[2, C(0, 1)], [C(1, -1), 1]]))


def theta(u, x):
    return real(trace(multiply(inverse2(u), x)))/2


def h(u, x, y):
    inv = inverse2(u)
    return real(trace(multiply(multiply(multiply(inv, x), inv), y)))/2


def det_polar(x, y):
    return real(determinant(add(x, y))-determinant(x)-determinant(y))/2


def solve(a, b):
    work = [list(row)+[value] for row, value in zip(a, b)]
    n = len(b)
    for j in range(n):
        pivot = next(i for i in range(j, n) if work[i][j] != 0)
        work[j], work[pivot] = work[pivot], work[j]
        divisor = work[j][j]
        work[j] = [x/divisor for x in work[j]]
        for i in range(n):
            if i != j:
                coefficient = work[i][j]
                work[i] = [x-coefficient*y for x, y in zip(work[i], work[j])]
    return [row[-1] for row in work]


def determinant_metric():
    pairs = 0
    congruence_cases = 0
    basis = (I,) + PAULI
    for u in UNITS:
        positive_semidefinite(u)
        detu = real(determinant(u))
        require(detu > 0, "strictly positive order unit")
        equal(h(u, u, u), 1, "normalized order unit")
        gram = [[h(u, x, y) for y in basis] for x in basis]
        covector = [theta(u, x) for x in basis]
        dual = solve(gram, covector)
        equal(sum(x*y for x, y in zip(covector, dual)), 1,
              "inverse-metric scale-covector norm")
        for size in range(1, 5):
            require(real(determinant(matrix([row[:size] for row in gram[:size]]))) > 0,
                    "positive Hessian Gram matrix")
        for x in TANGENTS:
            equal(h(u, u, x), theta(u, x), "scale line is the metric dual")
            for y in TANGENTS:
                equal(h(u, x, y)-2*theta(u, x)*theta(u, y),
                      -det_polar(x, y)/detu, "Lorentz determinant identity")
                pairs += 1
        for s in CONGRUENCES:
            transformed_u = conjugate(u, s)
            determinant_scale = real(determinant(s)*determinant(s).conjugate())
            require(determinant_scale > 0, "invertible congruence")
            equal(real(determinant(transformed_u)), determinant_scale*detu,
                  "congruence determinant scale")
            for x in TANGENTS:
                transformed_x = conjugate(x, s)
                equal(theta(transformed_u, transformed_x), theta(u, x),
                      "natural scale differential")
                equal(h(transformed_u, transformed_x, transformed_x), h(u, x, x),
                      "natural Hessian response")
                congruence_cases += 1
    equal(pairs, 196, "metric-pair count")
    equal(congruence_cases, 84, "congruence count")
    print("PASS: 196 exact metric/Lorentz pairs at four positive units (three non-diagonal).")
    print("PASS: inverse-metric scale normalization and 84 simultaneous congruence cases.")


def cone_ratio():
    vectors = ((C(1), C(0)), (C(0), C(1)), (C(1), C(1)),
               (C(1), C(0, 1)), (C(1, 1), C(2, -1)),
               (C(F(1, 3)), C(F(2, 5), F(1, 2))))
    small_values = (F(1), F(1, 2), F(1, 16), F(1, 256), F(1, 4096))
    count = 0
    for u in UNITS:
        equal(h(u, u, u)/theta(u, u)**2, 1, "radial ratio one")
        count += 1
        for vector in vectors:
            x = [[a*b.conjugate() for b in vector] for a in vector]
            positive_semidefinite(x)
            equal(real(determinant(x)), 0, "rank-one null determinant")
            require(theta(u, x) > 0, "positive future scale")
            equal(h(u, x, x)/theta(u, x)**2, 2, "rank-one cone saturation")
            count += 1
        for s in CONGRUENCES:
            for epsilon in small_values:
                x = conjugate(matrix([[1, 0], [0, epsilon]]), s)
                positive_semidefinite(x)
                require(real(determinant(x)) > 0, "rank-two positive determinant")
                ratio = h(u, x, x)/theta(u, x)**2
                require(1 <= ratio < 2, "rank-two cone ratio")
                count += 1
    previous = F(0)
    for epsilon in small_values:
        x = matrix([[1, 0], [0, epsilon]])
        ratio = h(I, x, x)/theta(I, x)**2
        equal(ratio, 2*(1+epsilon**2)/(1+epsilon)**2, "boundary-approach formula")
        require(ratio >= previous, "ratio tends upward as determinant decreases")
        previous = ratio
        equal(real(determinant(x)), epsilon, "rank two does not fix determinant floor")
    equal(count, 88, "cone case count")
    print("PASS: 88 exact PSD cone cases; ratios in [1,2], null saturation, soft rank-two boundary.")


def pinch(a, labels):
    return [[value if labels[i] == labels[j] else C()
             for j, value in enumerate(row)] for i, row in enumerate(a)]


def corner(a):
    return [row[:2] for row in a[:2]]


def square(a):
    return multiply(a, a)


def composite_variance():
    projection_complement = matrix([[0, 0, 0], [0, 0, 0], [0, 0, 1]])
    for seed in range(1, 13):
        a = matrix([[F(seed, 3), C(F(1, seed+1), F(seed, 5)), C(F(seed+1, 4), -1)],
                    [0, F(-seed, 2), C(F(2, seed+2), F(1, 3))],
                    [0, 0, F(seed-2, 7)]])
        for i in range(3):
            for j in range(i):
                a[i][j] = a[j][i].conjugate()
        phi = lambda value: pinch(value, (0, 1, 0))
        b = phi(a)
        y = sub(a, b)
        delta_phi = sub(phi(square(a)), square(b))
        delta_psi = sub(corner(square(b)), square(corner(b)))
        total = sub(corner(phi(square(a))), square(corner(b)))
        transported = corner(delta_phi)
        equal(total, add(transported, delta_psi), "composite CP variance balance")
        equal(transported, corner(phi(square(y))), "transported pinching variance")
        equal(delta_psi, corner(multiply(multiply(b, projection_complement), b)),
              "additional corner variance")
        for value in (delta_phi, transported, delta_psi, total):
            positive_semidefinite(value)
        require(real(trace(transported)) > 0 and real(trace(delta_psi)) > 0,
                "both variance contributions are genuinely present")
    print("PASS: 12 exact pinching/corner CP variance balances with both positive contributions.")


def quaternion_multiply(a, b):
    x, y, z, w = a
    r, s, t, u = b
    return (x*r-y*s-z*t-w*u, x*s+y*r+z*u-w*t,
            x*t-y*u+z*r+w*s, x*u+y*t-z*s+w*r)


def quaternion_conjugate(a):
    return (a[0], -a[1], -a[2], -a[3])


def octonion_multiply(a, b):
    p, q, r, s = a[:4], a[4:], b[:4], b[4:]
    first = tuple(x-y for x, y in zip(quaternion_multiply(p, r),
                                    quaternion_multiply(quaternion_conjugate(s), q)))
    second = tuple(x+y for x, y in zip(quaternion_multiply(s, p),
                                     quaternion_multiply(q, quaternion_conjugate(r))))
    return first+second


def isolated_octonionic_residue():
    # C is span(1,i); all six probes have only its orthogonal octonion coordinates.
    for j in range(2, 8):
        z = tuple(F((j+1) if k == j else 0, j+2) for k in range(8))
        conjugate_z = (z[0],) + tuple(-x for x in z[1:])
        norm_squared = sum(x*x for x in z)
        scalar = (norm_squared,)+(F(0),)*7
        equal(octonion_multiply(z, conjugate_z), scalar, "13-entry z times conjugate")
        equal(octonion_multiply(conjugate_z, z), scalar, "31-entry conjugate times z")
        # For the isolated 13/31 entries these are the only nonzero terms of a^2.
        squared_a = matrix([[norm_squared, 0, 0], [0, 0, 0], [0, 0, norm_squared]])
        residue = corner(squared_a)
        positive_semidefinite(residue)
        equal(real(determinant(residue)), 0, "nonzero corner residue is null")
        require(real(trace(residue)) > 0, "nonzero corner residue")
        equal(h(I, residue, residue)/theta(I, residue)**2, 2, "residue cone saturation")
    print("PASS: six isolated octonionic 13-entry norm products give nonzero rank-one residues.")


def logdet_derivatives():
    step = F(1, 4000)
    def potential(u):
        detu = real(determinant(u))
        require(detu > 0 and real(trace(u)) > 0, "finite-difference point stays in cone")
        return -0.5*math.log(float(detu))
    count = 0
    for u in UNITS:
        for x in TANGENTS:
            numerical_first = (potential(add(u, scale(x, step)))
                               - potential(sub(u, scale(x, step))))/(2*float(step))
            close(numerical_first, -theta(u, x), "numerical logdet first derivative", 4e-6)
            count += 1
            for y in TANGENTS:
                numerical_second = sum(sx*sy*potential(add(add(u, scale(x, sx*step)),
                                                          scale(y, sy*step)))
                                       for sx in (-1, 1) for sy in (-1, 1))
                numerical_second /= 4*float(step)**2
                close(numerical_second, h(u, x, y), "numerical mixed logdet Hessian", 8e-6)
                count += 1
    equal(count, 224, "finite-difference count")
    print("PASS: 224 numerical logdet derivative comparisons (finite differences, not proofs).")


def pauli_generator(x, weights):
    out = scale(x, 0)
    for weight, sigma in zip(weights, PAULI):
        out = add(out, scale(sub(x, conjugate(x, sigma)), weight))
    return out


def pauli_transfer(x, weights, lag):
    out = x
    for weight, sigma in zip(weights, PAULI):
        # The exponential is numerical; exact rational coefficients retain sum=1 and CP.
        decay = F(math.exp(-2*lag*float(weight)))
        out = add(scale(out, (1+decay)/2),
                  scale(conjugate(out, sigma), (1-decay)/2))
    return out


def qubit_contraction():
    epsilons = (F(1), F(1, 2), F(1, 4), F(1, 10), F(1, 100), F(1, 1000))
    directions = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0),
                  (0, 0, 1), (0, 0, -1), (F(1, 3), F(2, 3), F(2, 3)),
                  (F(-2, 3), F(1, 3), F(2, 3)), (0, 0, 0),
                  (F(1, 10), F(1, 5), F(3, 10)))
    cases = 0
    for epsilon in epsilons:
        weights = (epsilon/4, epsilon/4, (2-epsilon)/4)
        require(all(weight >= 0 for weight in weights), "positive Pauli jump weights")
        equal(pauli_generator(I, weights), scale(I, 0), "fixed order unit")
        for sigma, rate in zip(PAULI, (F(1), F(1), epsilon)):
            equal(pauli_generator(sigma, weights), scale(sigma, rate), "exact Pauli rate")
        for first in PAULI:
            for second in PAULI:
                for x in (I,)+PAULI:
                    equal(conjugate(conjugate(x, first), second),
                          conjugate(conjugate(x, second), first), "commuting jumps")
        for lag in (0.1, 0.5, 1.0, 3.0):
            operator_norm_squared = math.exp(-2*lag*float(epsilon))
            for direction in directions:
                b = hermitian(1, direction)
                positive_semidefinite(b)
                out = pauli_transfer(b, weights, lag)
                positive_semidefinite(out)
                equal(real(trace(out)), 2, "normalized positive base preserved")
                ratio = h(I, out, out)/theta(I, out)**2
                contracted = float(ratio-1)
                require(contracted <= operator_norm_squared+2e-12,
                        "complete diagonal norm bounds each tested direction")
                if direction == (0, 0, 1):
                    close(contracted, operator_norm_squared, "slow direction attains supremum")
                cases += 1
    # Zero is an endpoint control, not one of the primitive positive-rate cases.
    weights_zero = (F(0), F(0), F(1, 2))
    equal(pauli_generator(PAULI[2], weights_zero), scale(I, 0), "extra fixed endpoint mode")
    equal(pauli_transfer(add(I, PAULI[2]), weights_zero, 1.0), add(I, PAULI[2]),
          "endpoint has no strict interiorization")
    equal(cases, 240, "Pauli cone-probe count")
    print("PASS: six exact Pauli rate families (1,1,epsilon); unchanged cone and zero-rate endpoint.")
    print("PASS: 240 numerical CP cone probes; the slow boundary direction saturates exp(-2s epsilon).")


def simpson(function, left, right, panels=16384):
    width = (right-left)/panels
    total = function(left)+function(right)
    for j in range(1, panels):
        total += (4 if j % 2 else 2)*function(left+j*width)
    return total*width/3


def radial_hyperbolic_test():
    # f=z/sinh(r), z=sin(pi(r-1)/length), extended by zero.
    # These are compactly supported H^1 trials, not smooth at the two endpoints.
    # The common angular factor 4*pi cancels in the radial Rayleigh quotient.
    for length in (2.0, 4.0, 8.0, 16.0, 32.0):
        def z(r):
            return math.sin(math.pi*(r-1)/length)
        def dz(r):
            return math.pi/length*math.cos(math.pi*(r-1)/length)
        denominator = simpson(lambda r: z(r)**2, 1.0, 1.0+length)
        raw_energy = simpson(lambda r: (dz(r)-z(r)/math.tanh(r))**2,
                             1.0, 1.0+length)
        transformed_energy = simpson(lambda r: dz(r)**2+z(r)**2,
                                     1.0, 1.0+length)
        close(denominator, length/2, "radial trial norm", 2e-10)
        close(raw_energy, transformed_energy, "hyperbolic integration by parts", 2e-9)
        close(raw_energy/denominator, 1+math.pi**2/length**2,
              "unshifted hyperbolic trial quotient", 2e-9)
        close(raw_energy/denominator-1, math.pi**2/length**2,
              "conformal subtraction removes one", 2e-9)
    print("PASS: five numerical H^1 radial trials; quotient 1+pi^2/L^2 and shifted quotient pi^2/L^2.")


def main():
    determinant_metric()
    cone_ratio()
    composite_variance()
    isolated_octonionic_residue()
    logdet_derivatives()
    qubit_contraction()
    radial_hyperbolic_test()
    print("All nine check groups passed. Stdlib only; stdout only; no files written.")
    print("Exact finite matrix checks are separate from numerical derivatives and quadrature.")
    print("No full Albert CP map, causal history, physical mass or continuum spectral gap is certified.")


if __name__ == "__main__":
    main()
