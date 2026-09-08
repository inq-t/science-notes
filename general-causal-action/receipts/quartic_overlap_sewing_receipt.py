"""Exact linearized-balance and quartic sewing checks.

The derivative is conditional on the weighted differentiability hypotheses
in quartic-overlap-sewing-tangent.md. This receipt integrates conditional
Gaussian polynomial moments; it does not establish a nonlinear Sinkhorn
branch or its differentiability. Shared Hermite and Gaussian moment
routines are reused from the preceding Gaussian balancing receipt.
It also checks the separate interacting-refinement perturbation matrix
and its leading Gaussian conditional-memory coefficient.
"""

from fractions import Fraction as F
from math import factorial
from gaussian_overlap_balancing_receipt import (
    conditional_polynomial,
    hermite_polynomials,
)


H = hermite_polynomials(12)


def add(left, right):
    return [(left[i] if i < len(left) else F(0))
            + (right[i] if i < len(right) else F(0))
            for i in range(max(len(left), len(right)))]


def scale(value, polynomial):
    return [value * coefficient for coefficient in polynomial]


def multiply(left, right):
    result = [F(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def same(left, right):
    return not any(add(left, scale(F(-1), right)))


def gaussian_integral(polynomial):
    result = F(0)
    moment = 1
    for i in range(0, len(polynomial), 2):
        if i:
            moment *= i - 1
        result += moment * polynomial[i]
    return result


def inner(left, right):
    return gaussian_integral(multiply(left, right))


def q_action(r, polynomial):
    # Actual moments of y | x ~ N(r*x, 1-r^2), not a spectral substitution.
    return conditional_polynomial(polynomial, r, 1 - r * r)


def number_action(polynomial):
    # N=-d^2/dx^2 + x*d/dx on polynomial coefficients.
    result = [F(i) * value for i, value in enumerate(polynomial)]
    for i in range(2, len(polynomial)):
        result[i - 2] -= i * (i - 1) * polynomial[i]
    return result


def potential(components):
    result = [F(0)]
    for degree, coefficient in components.items():
        result = add(result, scale(coefficient, H[degree]))
    return result


def endpoint_derivative(r, components):
    # Solve (I+Q)b=Q V on the given finite Hermite support, then d=b-V/2.
    b = [F(0)]
    for degree, coefficient in components.items():
        b = add(b, scale(coefficient * r ** degree / (1 + r ** degree), H[degree]))
    v = potential(components)
    assert same(add(b, q_action(r, b)), q_action(r, v))
    d = add(b, scale(F(-1, 2), v))
    assert same(
        add(d, q_action(r, d)),
        scale(F(-1, 2), add(v, scale(F(-1), q_action(r, v)))),
    )
    return d


def derivative_action(r, components, polynomial):
    d = endpoint_derivative(r, components)
    return add(multiply(d, q_action(r, polynomial)),
               q_action(r, multiply(d, polynomial)))


def defect_action(r, s, components, polynomial):
    return add(
        derivative_action(r * s, components, polynomial),
        scale(F(-1), add(
            derivative_action(r, components, q_action(s, polynomial)),
            q_action(r, derivative_action(s, components, polynomial)),
        )),
    )


def factor(r, s, left_degree, right_degree, potential_degree):
    # Separate closed formula, compared with direct polynomial integration.
    h = lambda u: (1 - u ** potential_degree) / (1 + u ** potential_degree)
    m, n = left_degree, right_degree
    return -F(1, 2) * (
        h(r * s) * ((r * s) ** m + (r * s) ** n)
        - h(r) * (r ** m + r ** n) * s ** n
        - h(s) * r ** m * (s ** m + s ** n)
    )


def basic_checks():
    components = {4: F(1)}
    v = potential(components)
    assert gaussian_integral(v) == 0
    assert gaussian_integral(multiply([F(0), F(0), F(1)], v)) == 0
    for r in (F(1, 2), F(2, 3), F(1, 4)):
        dot_vacuum = derivative_action(r, components, H[0])
        # dot Q 1 + Q dot(vacuum) = dot(vacuum), including its changing state.
        state_derivative = scale(F(-1, 2), v)
        assert same(add(dot_vacuum, q_action(r, state_derivative)), state_derivative)

    for r, s in ((F(1, 2), F(1, 2)), (F(1, 2), F(2, 3))):
        for m, n in ((1, 3), (0, 4), (2, 2), (1, 5)):
            actual = inner(H[m], defect_action(r, s, components, H[n]))
            coefficient = inner(H[m], multiply(H[4], H[n]))
            assert actual == coefficient * factor(r, s, m, n, 4)

    r = F(1, 2)
    off_diagonal = inner(H[1], defect_action(r, r, components, H[3]))
    assert inner(H[1], multiply(H[4], H[3])) == 24
    assert factor(r, r, 1, 3, 4) == F(2835, 69904)
    assert off_diagonal == F(8505, 8738)
    assert inner(H[0], defect_action(r, r, components, H[4])) == 0
    assert inner(H[1], defect_action(r, r, components, H[5])) == 0
    assert inner(H[2], defect_action(r, r, components, H[2])) == F(10125, 8738)
    width = lambda u: (1 - u * u) / (2 * u)
    assert width(r) == F(3, 4) and width(r * r) == F(15, 8)
    print('EXACT H4: moving vacuum and variance controls; '
          '<H1, defect H3>=8505/8738 at widths 3/4 and 15/8')
    print('EXACT zero controls: <H0, defect H4>=0 and <H1, defect H5>=0; '
          'direct Gaussian moment integration agrees with the closed matrix formula')


def clock_correction_checks():
    r = F(1, 2)
    components = {4: F(1)}
    alpha_t, alpha_2t = F(2, 7), F(5, 11)

    def corrected_derivative(multiplier, alpha, polynomial):
        return add(derivative_action(multiplier, components, polynomial),
                   scale(-alpha, number_action(q_action(multiplier, polynomial))))

    for n in (1, 3):
        corrected = add(
            corrected_derivative(r * r, alpha_2t, H[n]),
            scale(F(-1), add(
                corrected_derivative(r, alpha_t, q_action(r, H[n])),
                q_action(r, corrected_derivative(r, alpha_t, H[n])),
            )),
        )
        uncorrected = defect_action(r, r, components, H[n])
        change = scale(-(alpha_2t - 2 * alpha_t),
                       number_action(q_action(r * r, H[n])))
        assert same(corrected, add(uncorrected, change))
        if n == 3:
            assert inner(H[1], corrected) == F(8505, 8738)
    print('EXACT arbitrary tested scalar-clock correction contributes only '
          '-(alpha_2t-2*alpha_t) N Q_2t; off-diagonal witness unchanged')


def other_potential_checks():
    r = F(1, 2)
    assert inner(H[1], defect_action(r, r, {2: F(1)}, H[3])) == 0
    quartic = {4: F(1, 4), 2: F(3, 2)}
    assert same(potential(quartic), [F(-3, 4), F(0), F(0), F(0), F(1, 4)])
    assert inner(H[1], defect_action(r, r, quartic, H[3])) == F(8505, 34952)

    # Two independent Gaussian integrals for V=H2(x)H2(y), left mode H1(x),
    # right mode H1(x)H2(y). Total Hermite degrees are 1 and 3.
    joint_coefficient = inner(H[1], multiply(H[2], H[1])) * inner(H[0], multiply(H[2], H[2]))
    assert joint_coefficient == 4
    assert joint_coefficient * factor(r, r, 1, 3, 4) == F(2835, 17476)
    # Every covariance derivative vanishes by an odd or centered factor.
    assert gaussian_integral(H[2]) == 0
    assert inner(H[1], H[2]) == 0
    print('EXACT x^4/4 defect=8505/34952; joint H2(x)H2(y) defect=2835/17476, '
          'with zero first covariance variation')


def interacting_refinement_checks():
    # IC13-14 uses normalized flat Hermites phi_n = sqrt(gamma) H_n/sqrt(n!).
    # Gaussian integration of H_m B H_n therefore computes the SAME flat
    # matrix element after division by sqrt(m! n!). No perturbed measure or
    # nonlinear balancing factors are used in this independent check.
    b = [F(0), F(0), F(-3, 2), F(0), F(1, 2)]
    entries = 0
    for n in range(9):
        for m in range(13):
            actual = inner(H[m], multiply(b, H[n]))
            low, high = min(m, n), max(m, n)
            separation = high - low
            if separation == 0:
                expected = F(3 * n * n * factorial(n))
            elif separation == 2:
                expected = F(4 * low + 3, 2) * factorial(high)
            elif separation == 4:
                expected = F(factorial(high), 2)
            else:
                expected = F(0)
            assert actual == expected
            entries += 1

        diagonal = inner(H[n], multiply(b, H[n])) / factorial(n)
        assert diagonal == 3 * n * n
        for jump, target_squared in (
            (2, F((4 * n + 3) ** 2 * (n + 1) * (n + 2), 4)),
            (4, F((n + 1) * (n + 2) * (n + 3) * (n + 4), 4)),
        ):
            m = n + jump
            actual = inner(H[m], multiply(b, H[n]))
            # Positive sign and exact square determine the normalized entry
            # without introducing rounded square roots of factorials.
            assert actual > 0
            assert actual * actual / (factorial(m) * factorial(n)) == target_squared

    # IC20: integrate the leading hidden response x(y^2-E[y^2]) using
    # independent one-dimensional Gaussian moments, not an assigned norm.
    coordinate_squared = [F(0), F(0), F(1)]
    conditional_mean = gaussian_integral(coordinate_squared)
    hidden_y = add(coordinate_squared, [F(-conditional_mean)])
    assert conditional_mean == 1 and gaussian_integral(hidden_y) == 0
    memory_coefficient = (
        gaussian_integral(coordinate_squared)
        * gaussian_integral(multiply(hidden_y, hidden_y))
    )
    assert memory_coefficient == 2
    print(f'EXACT IC14: {entries} unnormalized Hermite matrix entries, '
          'all normalized diagonals and positive off-diagonal squares for n=0..8')
    print('EXACT IC20 Gaussian leading coefficient: E[x^2 (y^2-1)^2]=2; '
          'this checks no non-Gaussian conditional-moment limit')


if __name__ == '__main__':
    basic_checks()
    clock_correction_checks()
    other_potential_checks()
    interacting_refinement_checks()
    print('PASS exact linearized-balance coefficients and composition tests. '
          'Interacting Hermite entries and the Gaussian memory coefficient also pass. '
          'No nonlinear balancing-branch existence, differentiability, '
          'or non-Gaussian moment limit is asserted.')
