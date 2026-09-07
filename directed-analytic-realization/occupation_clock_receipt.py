"""Exact finite checks for occupation-dependent clocks.

The input is the declared scalar spectrum h_D(m)=m+m(m-1)/D on integer
occupations. Rational spectral entries, finite differences and derivatives
at zero are tested, not numerically fitted. Complex phase derivatives are
pairs of rational numbers, never Python floating complex numbers.

These checks do not prove full-operator convergence, a physical occupation
law, spatial locality, a selected clock or a Yang--Mills mass gap.
The script uses only the standard library, prints to stdout and writes no
files. It does not modify the earlier fluctuation receipt.
"""

from fractions import Fraction as F


DIMENSIONS = (8, 24, 48)
CUTOFFS = (1, 2, 4, 8)
SHIFTS = (F(1, 2), F(1), F(3))
TEST_OCCUPATIONS = (0, 1, 2, 5, 12)


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def equal(actual, expected, label):
    require(actual == expected, f"{label}: {actual!r} != {expected!r}")


def h(dimension, occupation):
    require(dimension > 0 and occupation >= 0, "positive dimension and occupation")
    return F(occupation) + F(occupation * (occupation - 1), dimension)


def backgrounds(dimension):
    return (0, 1, dimension // 2, dimension, 3 * dimension)


def local_rate(dimension, background):
    return F(1) + F(2 * background, dimension)


def bounded_energy_and_differences():
    cutoff_count = energy_count = difference_count = rare_tail_count = 0
    for dimension in DIMENSIONS:
        for cutoff in CUTOFFS:
            bound = F(cutoff * (cutoff - 1), dimension)
            residuals = []
            for occupation in range(cutoff + 1):
                residual = h(dimension, occupation) - occupation
                equal(residual, F(occupation * (occupation - 1), dimension),
                      "bounded-occupation residual")
                require(0 <= residual <= bound, "residual bound on m <= cutoff")
                residuals.append(residual)
                cutoff_count += 1
                if h(dimension, occupation) <= cutoff:
                    require(occupation <= cutoff, "energy bound controls occupation")
                    require(residual <= bound, "same bound on h_D(m) <= cutoff")
                    energy_count += 1
            equal(max(residuals), bound, "sharp number-cutoff residual norm")
        for occupation in range(13):
            first = h(dimension, occupation + 1) - h(dimension, occupation)
            second = (h(dimension, occupation + 2)
                      - 2 * h(dimension, occupation + 1)
                      + h(dimension, occupation))
            equal(first, F(1) + F(2 * occupation, dimension),
                  "unit occupation difference")
            equal(second, F(2, dimension), "constant second finite difference")
            difference_count += 1
        vacuum_weight, tail_weight = 1 - F(1, dimension), F(1, dimension)
        equal(vacuum_weight + tail_weight, F(1), "rare-tail normalized law")
        mean_energy = vacuum_weight * h(dimension, 0) + tail_weight * h(dimension, dimension)
        mean_number = tail_weight * dimension
        mean_residual = tail_weight * (h(dimension, dimension) - dimension)
        equal(mean_energy, 2 - F(1, dimension), "rare-tail mean energy")
        equal(mean_number, F(1), "rare-tail mean occupation")
        equal(mean_residual, 1 - F(1, dimension), "rare-tail mean nonlinear residual")
        require(mean_energy < 2 and mean_residual >= F(7, 8),
                "bounded mean energy does not make the nonlinear expectation small")
        rare_tail_count += 1
    print(f"PASS: {cutoff_count} bounded-occupation residual checks, "
          f"{energy_count} energy-cutoff checks and {difference_count} first/second "
          "differences; residual <= E(E-1)/D on m<=E for tested integer "
          "cutoffs E>=1, and second difference=2/D.")
    print(f"PASS: {rare_tail_count} exact vacuum/m=D mixtures with tail weight 1/D "
          "give E[H]=2-1/D, E[N]=1 and E[H-N]=1-1/D; bounded mean energy "
          "alone does not justify convergence of these unbounded expectations.")


def sector_subtraction():
    count = wrong_coefficient_count = 0
    for dimension in DIMENSIONS:
        for background in backgrounds(dimension):
            rate = local_rate(dimension, background)
            require(rate >= 1, "sector linear rate is at least one")
            for increment in range(9):
                actual = h(dimension, background + increment) - h(dimension, background)
                expected = (rate * increment
                            + F(increment * (increment - 1), dimension))
                equal(actual, expected, "exact background-sector subtraction")
                count += 1
                if background and increment:
                    wrong = ((1 + F(background, dimension)) * increment
                             + F(increment * (increment - 1), dimension))
                    equal(actual - wrong, F(background * increment, dimension),
                          "wrong n/D coefficient leaves a nonzero defect")
                    require(actual != wrong, "negative control rejects missing factor two")
                    wrong_coefficient_count += 1
    print(f"PASS: {count} sector-subtraction identities give "
          "(1+2n/D)k+k(k-1)/D; "
          f"{wrong_coefficient_count} negative controls reject the coefficient n/D.")


def mixed_mode_differences():
    count = missing_term_count = 0
    for dimension in DIMENSIONS:
        for background in backgrounds(dimension):
            for first in range(4):
                for second in range(4):
                    mixed = (h(dimension, background + first + second)
                             - h(dimension, background + first)
                             - h(dimension, background + second)
                             + h(dimension, background))
                    equal(mixed, F(2 * first * second, dimension),
                          "two-mode mixed energy difference")
                    count += 1
                    if first and second:
                        require(mixed > 0, "negative control rejects mode additivity")
                        missing_term_count += 1
    print(f"PASS: {count} two-mode differences equal 2ab/D; "
          f"{missing_term_count} nonzero mixed terms reject an additive independent-mode clock.")


def shifted_resolvents():
    count = 0
    for dimension in DIMENSIONS:
        for background in backgrounds(dimension):
            rate = local_rate(dimension, background)
            for shift in SHIFTS:
                for occupation in TEST_OCCUPATIONS:
                    actual_energy = (h(dimension, background + occupation)
                                     - h(dimension, background))
                    linear_energy = rate * occupation
                    difference = (1 / (shift + linear_energy)
                                  - 1 / (shift + actual_energy))
                    residual = F(occupation * (occupation - 1), dimension)
                    equal(difference, residual /
                          ((shift + linear_energy) * (shift + actual_energy)),
                          "positive shifted resolvent difference")
                    require(0 <= difference <= 1 / (dimension * rate**2),
                            "sampled stronger shifted-resolvent bound 1/(D a_D^2)")
                    require(difference <= F(1, dimension),
                            "sampled shifted-resolvent bound 1/D")
                    if occupation in (0, 1):
                        equal(difference, F(0), "ground and first-mode resolvents agree")
                    else:
                        require(difference > 0, "higher-mode comparison is nonvacuous")
                    count += 1
    print(f"PASS: {count} positive shifted-resolvent differences to a_D N "
          "satisfy 0<=difference<=1/(D a_D^2)<=1/D at the declared rational probes.")


def complex_pair(real=0, imag=0):
    return (F(real), F(imag))


def complex_product(left, right):
    a, b = left
    c, d = right
    return (a*c - b*d, a*d + b*c)


def complex_difference(left, right):
    return tuple(a-b for a, b in zip(left, right))


def weighted_pairs(weights, values):
    return tuple(sum((weight * value[j]
                      for weight, value in zip(weights, values)), F(0))
                 for j in range(2))


def mixed_clock_derivatives():
    # These are derivatives at zero, not Taylor coefficients divided by k!.
    rates, weights = (F(1), F(3)), (F(1, 2), F(1, 2))
    mean = sum(weight * rate for weight, rate in zip(weights, rates))
    second_moment = sum(weight * rate**2 for weight, rate in zip(weights, rates))
    variance = second_moment - mean**2
    equal((mean, second_moment, variance), (F(2), F(5), F(1)),
          "two-rate exact first and second moments")

    first = weighted_pairs(weights, [complex_pair(0, rate) for rate in rates])
    second = weighted_pairs(weights, [complex_pair(-rate**2) for rate in rates])
    first_squared = complex_product(first, first)
    equal(first, complex_pair(0, 2), "phase first derivative is 2i")
    equal(second, complex_pair(-5), "phase second derivative is -5")
    equal(first_squared, complex_pair(-4), "unitary candidate second derivative is -4")
    equal(complex_difference(second, first_squared), complex_pair(-variance),
          "phase second-derivative defect is minus rate variance")
    require(second != first_squared, "mixture fails the scalar group law at second order")
    # |c(t)|^2 has second derivative 2 Re c''(0)+2 |c'(0)|^2.
    modulus_second = 2 * second[0] + 2 * (first[0]**2 + first[1]**2)
    equal(modulus_second, F(-2), "phase mixture is not a unit-modulus clock")

    heat_first = sum(-weight * rate for weight, rate in zip(weights, rates))
    heat_second = second_moment
    equal(heat_first, F(-2), "heat first derivative")
    equal(heat_second, F(5), "heat second derivative")
    equal(heat_second - heat_first**2, variance,
          "heat second-derivative defect is plus rate variance")
    require(heat_second != heat_first**2,
            "heat mixture fails the scalar semigroup law at second order")
    print("PASS: the equal rate-1/rate-3 mixture on |1><0| has phase derivatives "
          "2i,-5 rather than 2i,-4 (defect -1), and heat derivatives -2,5 "
          "rather than -2,4 (defect +1); rate variance is exactly one.")


def minimal_carrier_and_observable_leak():
    # Order: (reservoir 1, level 0/1), then (reservoir 3, level 0/1).
    def matrix(rows):
        return tuple(tuple(F(x) for x in row) for row in rows)

    def multiply(a, b):
        return tuple(tuple(sum((x*y for x, y in zip(row, column)), F(0))
                           for column in zip(*b)) for row in a)

    def act(a, vector):
        return tuple(sum((x*y for x, y in zip(row, vector)), F(0)) for row in a)

    identity = matrix([[int(i == j) for j in range(4)] for i in range(4)])
    hamiltonian = matrix(((0, 0, 0, 0), (0, 1, 0, 0),
                          (0, 0, 0, 0), (0, 0, 0, 3)))
    projection = matrix(((F(1, 2), 0, F(1, 2), 0), (0, 1, 0, 0),
                         (F(1, 2), 0, F(1, 2), 0), (0, 0, 0, 1)))
    complement = tuple(tuple(x-y for x, y in zip(row, other))
                       for row, other in zip(identity, projection))
    # J=J0/sqrt(2) is the isometry. Range identities use rational J0.
    j0 = matrix(((1, 0), (0, 1), (1, 0), (0, 1)))
    equal(multiply(tuple(zip(*j0)), j0), matrix(((2, 0), (0, 2))),
          "J0/sqrt(2) is an isometry")
    equal(multiply(projection, projection), projection, "minimal projector is idempotent")
    equal(tuple(zip(*projection)), projection, "minimal projector is self-adjoint")
    equal(sum(projection[i][i] for i in range(4)), F(3), "minimal carrier has rank three")
    equal(multiply(projection, hamiltonian), multiply(hamiltonian, projection),
          "minimal carrier reduces the clock")
    equal(multiply(projection, j0), j0, "minimal carrier contains the initial readout")

    symmetric_excitation = (F(0), F(1), F(0), F(1))
    its_image = act(hamiltonian, symmetric_excitation)
    # These identities show both excited eigenvectors belong to the cyclic span.
    equal(tuple((3*x-y)/2 for x, y in zip(symmetric_excitation, its_image)),
          (F(0), F(1), F(0), F(0)), "first excited vector is generated")
    equal(tuple((y-x)/2 for x, y in zip(symmetric_excitation, its_image)),
          (F(0), F(0), F(0), F(1)), "second excited vector is generated")
    vacuum_projection = matrix(((1, 0, 0, 0), (0, 0, 0, 0),
                                (0, 0, 1, 0), (0, 0, 0, 0)))
    retained_vacuum = multiply(projection, vacuum_projection)
    equal(multiply(retained_vacuum, retained_vacuum), retained_vacuum,
          "retained vacuum projector")
    equal(sum(retained_vacuum[i][i] for i in range(4)), F(1),
          "minimal clock has a one-dimensional vacuum")
    anti_vacuum = (F(1), F(0), F(-1), F(0))
    anti_excitation = (F(0), F(1), F(0), F(-1))
    equal(act(hamiltonian, anti_vacuum), (F(0),)*4, "excluded vector has zero energy")
    equal(act(projection, anti_vacuum), (F(0),)*4, "antisymmetric vacuum is excluded")
    equal(act(projection, anti_excitation), anti_excitation,
          "antisymmetric excitation is retained")
    lowering = matrix(((0, 1, 0, 0), (0, 0, 0, 0),
                       (0, 0, 0, 1), (0, 0, 0, 0)))
    leak = multiply(multiply(complement, lowering), projection)
    equal(act(leak, anti_excitation), anti_vacuum,
          "the original I tensor |0><1| observable leaves the minimal carrier")
    require(any(entry for row in leak for entry in row),
            "observable leakage is nonzero")
    print("PASS: the exact rank-three spectral cyclic projector retains one vacuum "
          "and both excited levels, commutes with H and contains J; the original "
          "lowering operator sends a retained antisymmetric excitation to the excluded vacuum.")


def main():
    bounded_energy_and_differences()
    sector_subtraction()
    mixed_mode_differences()
    shifted_resolvents()
    mixed_clock_derivatives()
    minimal_carrier_and_observable_leak()
    print("All six exact finite check groups passed; stdlib only; stdout only; no files written.")
    print("No floating arithmetic, numerical exponential, sampling or spectral fitting is used.")
    print("Finite checks do not prove full-space convergence, an occupation-selection law, "
          "physical clock calibration, spatial locality or a Yang--Mills gap.")


if __name__ == "__main__":
    main()
