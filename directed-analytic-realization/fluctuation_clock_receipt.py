"""Exact finite checks for purification fluctuations and their clock.

All evaluated quantities are rational or Gaussian rational. Sphere moments
are checked independently by permutation cycles of noncommuting Pauli
matrices. Sparse polynomial helpers and exact matrix arithmetic are reused
from guarded local receipts; none of their numerical checks are called.

Degree-four matrix, polynomial resolvent and Gaussian ladder checks are
finite certificates, not proofs of completeness, a full-space resolvent
limit, a process limit, locality, physical clock calibration or a Yang--Mills
gap. Ladder operations retain every generated degree, without truncation.
The script uses stdlib/local helpers, prints to stdout and writes no files.
"""

from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations, product
from math import factorial, isqrt, prod

import positive_cone_process_receipt as pc
import sphere_ball_descent_receipt as sb


DIMENSIONS = (8, 24, 48)
SHIFTS = (F(1, 2), F(1), F(3))
ZERO = (0, 0, 0)
ONE = sb.monomial(ZERO)
BASIS = sb.basis(3, 4)
equal, require = pc.equal, pc.require


def odd_double_factorial(n):
    return prod(range(1, n + 1, 2))


@lru_cache(None)
def moment(exponent, dimension):
    """The declared radial formula; None denotes the Gaussian limit."""
    if any(power % 2 for power in exponent):
        return F(0)
    half_degree = sum(exponent) // 2
    gaussian = prod(odd_double_factorial(power - 1) for power in exponent)
    correction = (F(1) if dimension is None else
                  prod(F(dimension + 1, dimension + 1 + 2*j)
                       for j in range(half_degree)))
    return gaussian * correction


def expectation(polynomial, dimension):
    return sum((coefficient * moment(exponent, dimension)
                for exponent, coefficient in polynomial.items()), F(0))


def pairing(p, q, dimension):
    return expectation(sb.pmul(p, q), dimension)


@lru_cache(None)
def permutation_cycles(length):
    result = []
    for permutation in permutations(range(length)):
        visited, cycles = set(), []
        for start in range(length):
            if start in visited:
                continue
            cycle, current = [], start
            while current not in visited:
                visited.add(current)
                cycle.append(current)
                current = permutation[current]
            cycles.append(tuple(cycle))
        result.append(tuple(cycles))
    return tuple(result)


@lru_cache(None)
def pauli_word_trace(word):
    matrix = pc.I
    for label in word:
        matrix = pc.multiply(matrix, pc.PAULI[label])
    return pc.trace(matrix)


@lru_cache(None)
def cycle_trace_coefficients(word):
    """Coefficients of K^number_of_cycles, before the sphere denominator."""
    result = {}
    for cycles in permutation_cycles(len(word)):
        value = pc.C(1)
        for cycle in cycles:
            value *= pauli_word_trace(tuple(word[j] for j in cycle))
            if value == pc.C(0):
                break
        power = len(cycles)
        result[power] = result.get(power, pc.C(0)) + value
    return result


def sphere_permutation_moment(word, dimension):
    environment = dimension // 2
    root = isqrt(dimension + 1)
    equal(root * root, dimension + 1, "rational fluctuation coordinate")
    numerator = sum((coefficient * environment**power
                     for power, coefficient in
                     cycle_trace_coefficients(word).items()), pc.C(0))
    denominator = prod(dimension + j for j in range(len(word)))
    return pc.real(numerator * root**len(word) / denominator)


def independent_moment_checks():
    # All orders through three, plus all monomial types at orders four-six.
    words = {word for length in range(4)
             for word in product(range(3), repeat=length)}
    words.update(tuple(label for label, power in enumerate(exponent)
                       for _ in range(power))
                 for exponent in sb.basis(3, 6)
                 if 4 <= sum(exponent) <= 6)
    words.update(((0, 1, 0, 1), (1, 0, 1, 0),
                  (0, 1, 2, 0, 1, 2), (2, 1, 0, 2, 1, 0),
                  (0, 1, 0, 2, 1, 2), (1, 2, 1, 0, 2, 0)))
    count = 0
    for dimension in DIMENSIONS:
        for word in sorted(words, key=lambda w: (len(w), w)):
            exponent = tuple(word.count(j) for j in range(3))
            equal(sphere_permutation_moment(word, dimension),
                  moment(exponent, dimension),
                  "permutation-cycle moment equals radial formula")
            count += 1
    equal(pauli_word_trace((0, 1, 0, 1)), pc.C(-2),
          "ordered alternating Pauli word")
    equal(pauli_word_trace((0, 0, 1, 1)), pc.C(2),
          "grouping Pauli factors changes the cycle trace")
    equal(pauli_word_trace((0, 1, 2)), pc.C(0, 2),
          "odd noncommuting cycle trace is not discarded prematurely")
    print(f"PASS: {count} exact sphere-permutation moments match the radial "
          "formula at D=8,24,48, through order six; noncommuting cycle "
          "traces and their imaginary cancellations are retained.")


def eigenvalue(degree, dimension):
    return F(degree) if dimension is None else (
        F(degree) + F(degree * (degree - 1), dimension))


def generator(polynomial, dimension):
    """Exact sparse monomial generator; no degree truncation."""
    diffusion = F(1) if dimension is None else F(dimension + 1, dimension)
    out = {}
    for exponent, coefficient in polynomial.items():
        out = sb.padd(out, sb.monomial(
            exponent, -eigenvalue(sum(exponent), dimension) * coefficient))
        for j, power in enumerate(exponent):
            if power < 2:
                continue
            target = list(exponent)
            target[j] -= 2
            out = sb.padd(out, sb.monomial(
                target, diffusion * power * (power - 1) * coefficient))
    return out


def coordinate_generator(polynomial, dimension):
    """Independent differentiation of the co-metric, not its diagonal."""
    diffusion = F(1) if dimension is None else F(dimension + 1, dimension)
    out = sb.pscale(diffusion, sb.laplacian(polynomial, 3))
    for i in range(3):
        xi = sb.coordinate(3, i)
        out = sb.padd(out, sb.pscale(
            -1, sb.pmul(xi, sb.derivative(polynomial, i))))
        if dimension is not None:
            for j in range(3):
                xj = sb.coordinate(3, j)
                second = sb.derivative(sb.derivative(polynomial, i), j)
                out = sb.padd(out, sb.pscale(
                    F(-1, dimension), sb.pmul(sb.pmul(xi, xj), second)))
    return out


def orthogonal_polynomials(dimension):
    polynomials, norms = [], []
    for exponent in BASIS:
        p = sb.monomial(exponent)
        for q, norm in zip(polynomials, norms):
            p = sb.padd(p, sb.pscale(-pairing(p, q, dimension) / norm, q))
        norm = pairing(p, p, dimension)
        require(norm > 0, "strict positive moment Gram pivot")
        equal(p.get(exponent), F(1), "monic degree-ordered polynomial")
        for q in polynomials:
            equal(pairing(p, q, dimension), F(0),
                  "exact Gram-Schmidt orthogonality")
        polynomials.append(p)
        norms.append(norm)
    return polynomials, norms


def polynomial_clock_checks():
    symmetry_count = mode_count = 0
    for dimension in DIMENSIONS + (None,):
        monomials = [sb.monomial(exponent) for exponent in BASIS]
        images = [generator(p, dimension) for p in monomials]
        for p, image in zip(monomials, images):
            equal(image, coordinate_generator(p, dimension),
                  "monomial and co-metric generator implementations agree")
            equal(expectation(image, dimension), F(0), "stationary moments")
        for i, p in enumerate(monomials):
            for j, q in enumerate(monomials):
                equal(pairing(p, images[j], dimension),
                      pairing(images[i], q, dimension),
                      "moment-Gram generator symmetry")
                symmetry_count += 1
        orthogonal, norms = orthogonal_polynomials(dimension)
        for exponent, p, norm in zip(BASIS, orthogonal, norms):
            rate = eigenvalue(sum(exponent), dimension)
            equal(generator(p, dimension), sb.pscale(-rate, p),
                  "full finite-degree orthogonal mode")
            equal(-pairing(p, generator(p, dimension), dimension),
                  rate * norm, "nonnegative generator quadratic form")
            require(rate >= 1 if sum(exponent) else rate == 0,
                    "centered finite-degree gap one")
            mode_count += 1
        equal(generator(ONE, dimension), {}, "constant mode")
        for j in range(3):
            x = sb.coordinate(3, j)
            centered_square = sb.padd(sb.pmul(x, x), sb.pscale(-1, ONE))
            equal(generator(x, dimension), sb.pscale(-1, x), "linear rate")
            equal(generator(centered_square, dimension),
                  sb.pscale(-eigenvalue(2, dimension), centered_square),
                  "centered square rate")
        if dimension is not None:
            # Dropping the finite-D diffusion correction destroys stationarity.
            wrong = sb.padd(generator(sb.coordinate(3, 0, 2), dimension),
                            sb.pscale(F(-2, dimension), ONE))
            equal(expectation(wrong, dimension), F(-2, dimension),
                  "negative control detects the missing diffusion correction")
    print(f"PASS: {symmetry_count} exact moment-Gram symmetry entries and "
          f"{mode_count} degree-ordered orthogonal modes on 35 monomials "
          "verify positivity, unique constant ground and finite-degree gap "
          "one; finite quadratic rate is 2+2/D, not 2.")


def shifted_operator(polynomial, dimension, shift, scale):
    return sb.padd(sb.pscale(shift, polynomial),
                   sb.pscale(-scale, generator(polynomial, dimension)))


def resolvent(polynomial, dimension, shift, scale):
    """Solve (shift I - scale A_D)q=p by descending degree."""
    require(shift > 0 and scale > 0, "positive resolvent parameters")
    residual, solution = dict(polynomial), {}
    degree = max((sum(exponent) for exponent in polynomial), default=0)
    for exponent in reversed(sb.basis(3, degree)):
        coefficient = residual.get(exponent, F(0))
        if not coefficient:
            continue
        term = sb.monomial(
            exponent, coefficient / (shift + scale * eigenvalue(
                sum(exponent), dimension)))
        solution = sb.padd(solution, term)
        residual = sb.padd(
            residual, sb.pscale(-1, shifted_operator(
                term, dimension, shift, scale)))
    equal(residual, {}, "triangular resolvent leaves no residual")
    return solution


def resolvent_checks():
    inverse_count = bound_count = 0
    for dimension in DIMENSIONS:
        for z in SHIFTS:
            # Keep the two resolvent conventions separate.
            for shift, scale in ((z, F(1)), (F(1), z)):
                for exponent in BASIS:
                    p = sb.monomial(exponent)
                    equal(shifted_operator(resolvent(
                        p, dimension, shift, scale), dimension, shift, scale),
                        p, "left finite polynomial inverse")
                    equal(resolvent(shifted_operator(
                        p, dimension, shift, scale), dimension, shift, scale),
                        p, "right finite polynomial inverse")
                    inverse_count += 2
            for degree in range(31):
                rate = eigenvalue(degree, dimension)
                difference = F(1, 1) / (z + degree) - F(1, 1) / (z + rate)
                equal(difference, (rate - degree) /
                      ((z + degree) * (z + rate)),
                      "shifted scalar resolvent difference")
                require(0 <= difference <= F(1, dimension),
                        "sampled shifted-resolvent bound 1/D")
                scaled = F(1, 1) / (1 + z * degree) - F(1, 1) / (1 + z * rate)
                require(0 <= scaled <= F(1, dimension) / z,
                        "sampled scaled-resolvent bound 1/(zD)")
                bound_count += 1
    print(f"PASS: {inverse_count} two-sided rational polynomial resolvent "
          f"identities and {bound_count} scalar degree checks (n=0..30, "
          "z=1/2,1,3); shifted bound 1/D and scaled bound 1/(zD) "
          "are distinguished.")


def annihilate(p, j):
    return sb.derivative(p, j)


def create(p, j):
    return sb.padd(sb.pmul(sb.coordinate(3, j), p),
                   sb.pscale(-1, sb.derivative(p, j)))


def gaussian_ladder_checks():
    finite_count = 0
    for dimension in DIMENSIONS:
        def cometric(i, j):
            radial = sb.pmul(sb.coordinate(3, i), sb.coordinate(3, j))
            diagonal = sb.pscale(
                F(dimension + 1, dimension) * int(i == j), ONE)
            return sb.padd(diagonal, sb.pscale(F(-1, dimension), radial))

        def velocity(p, j):
            # V_j=[H,Q_j], with H=-A_D; the self-adjoint candidate is i V_j.
            out = sb.pmul(sb.coordinate(3, j), p)
            for i in range(3):
                out = sb.padd(out, sb.pscale(
                    -2, sb.pmul(cometric(i, j), sb.derivative(p, i))))
            return out

        for exponent in sb.basis(3, 3):
            p = sb.monomial(exponent)
            for j in range(3):
                xj = sb.coordinate(3, j)
                direct = sb.padd(
                    sb.pscale(-1, generator(sb.pmul(xj, p), dimension)),
                    sb.pmul(xj, generator(p, dimension)))
                equal(direct, velocity(p, j),
                      "finite commutator velocity equals differential expression")
                for i in range(3):
                    xi = sb.coordinate(3, i)
                    commutator = sb.padd(
                        sb.pmul(xi, velocity(p, j)),
                        sb.pscale(-1, velocity(sb.pmul(xi, p), j)))
                    equal(commutator, sb.pscale(2, sb.pmul(cometric(i, j), p)),
                          "finite [Q_i,V_j] equals multiplication by 2 a_ij")
                    finite_count += 1
    commutator_count = adjoint_count = 0
    for exponent in BASIS:
        p = sb.monomial(exponent)
        number = {}
        for i in range(3):
            number = sb.padd(number, create(annihilate(p, i), i))
            for j in range(3):
                mixed = sb.padd(annihilate(create(p, j), i),
                               sb.pscale(-1, create(annihilate(p, i), j)))
                equal(mixed, p if i == j else {}, "Gaussian CCR")
                equal(annihilate(annihilate(p, j), i),
                      annihilate(annihilate(p, i), j),
                      "annihilators commute")
                equal(create(create(p, j), i), create(create(p, i), j),
                      "creators commute without degree truncation")
                commutator_count += 3
        equal(number, sb.pscale(-1, generator(p, None)),
              "number operator equals negative OU generator")
    for exponent in sb.basis(3, 3):
        p = sb.monomial(exponent)
        for other in BASIS:
            q = sb.monomial(other)
            for j in range(3):
                equal(pairing(annihilate(p, j), q, None),
                      pairing(p, create(q, j), None),
                      "creation is the Gaussian polynomial adjoint")
                adjoint_count += 1
    hermites = []
    for exponent in BASIS:
        h = ONE
        for j, power in enumerate(exponent):
            for _ in range(power):
                h = create(h, j)
        equal(generator(h, None), sb.pscale(-sum(exponent), h),
              "Hermite number eigenvalue")
        equal(pairing(h, h, None), F(prod(factorial(n) for n in exponent)),
              "Hermite factorial norm")
        for previous in hermites:
            equal(pairing(h, previous, None), F(0), "Hermite orthogonality")
        hermites.append(h)
    print(f"PASS: {commutator_count} exact Gaussian ladder commutators, "
          f"{adjoint_count} Gaussian adjoint pairings and 35 Hermite modes "
          "verify H=sum(a* a)=-A_infinity with every generated degree retained.")
    print(f"PASS: {finite_count} finite-core commutators [Q_i,V_j]=2 a_ij "
          "on degree-at-most-three monomials at D=8,24,48 retain the "
          "noncentral co-metric; no operator-domain or physical CCR claim.")


def main():
    independent_moment_checks()
    polynomial_clock_checks()
    resolvent_checks()
    gaussian_ladder_checks()
    print("All four finite exact check groups passed; stdout only; no files written.")
    print("No floating arithmetic, sampling, numerical integration or eigensolver is used.")
    print("Finite checks do not prove full-space spectral completeness, norm-resolvent "
          "convergence, a field limit, physical time or a Yang--Mills gap.")


if __name__ == "__main__":
    main()
