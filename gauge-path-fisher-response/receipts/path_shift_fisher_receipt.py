"""Finite Fisher/projection and path-frame receipts, with explicit scope.

The radial Gaussian family is an exact invariant likelihood readout of a
chosen Gaussian logarithm. It does not identify right-logarithm Wiener
chaos with the earlier left-driver clock. Radial integrals below cover a
finite interval by deterministic quadrature and bound the entire omitted
tail analytically. Quadrature-order agreement is an accuracy check, not
a certified bound on quadrature error or a continuum construction proof.
"""

from __future__ import annotations

import math
from decimal import Decimal, localcontext
from fractions import Fraction

import numpy as np


def exact_projection_coefficients() -> None:
    """Use all relevant chi-square moments, without sampling a Gaussian."""
    f = Fraction

    def radial_square_moment(degree):
        return f(math.prod(3+2*j for j in range(degree)))

    def polynomial_expectation(coefficients):
        return sum(value*radial_square_moment(degree)
                   for degree, value in enumerate(coefficients))

    q = (-f(1, 2), f(1, 6))
    p = (f(1, 8), -f(1, 12), f(1, 120))
    assert radial_square_moment(1)/3 == 1  # E[Z_3^2] for the original shift score.

    def product(left, right):
        result = [f(0)]*(len(left)+len(right)-1)
        for i, value in enumerate(left):
            for j, other in enumerate(right):
                result[i+j] += value*other
        return result

    assert polynomial_expectation(q) == polynomial_expectation(p) == 0
    assert polynomial_expectation(product(q, q)) == f(1, 6)
    assert polynomial_expectation(product(q, p)) == 0
    assert polynomial_expectation(product(product(q, q), q)) == f(1, 9)
    assert polynomial_expectation(product(q, q))/2 == f(1, 12)
    # N=-Delta+z.grad sends (|z|^2-3)/6 to twice itself in the
    # reference Gaussian coordinates; no other logarithm is identified.
    assert (-f(1), f(1, 3)) == tuple(2*value for value in q)
    print("PASS exact Gaussian projection coefficients: epsilon-score=0, "
          "eta-score=(|Z|^2-3)/6, boundary eta-Fisher=1/6, KL coefficient=1/12; "
          "unprojected shift Fisher=1")


def polynomial_gaussian_tail(coefficients, lower: Fraction) -> Fraction:
    """Rigorous rational upper bound for sum c_k int_L^inf u^k e^-u2/2 du.

    Mills' bound gives I_0<=e^-L2/2/L, I_1=e^-L2/2, and integration
    by parts gives I_k=L^(k-1)e^-L2/2+(k-1)I_(k-2). Replacing the
    exponential by 2^-floor(L^2/2) is conservative because e>2.
    All coefficients here are nonnegative. No floating tail estimate is
    used in the assertion that the omitted contributions are small.
    """
    assert lower > 0 and all(value >= 0 for value in coefficients)
    powers = [1/lower, Fraction(1)]
    while len(powers) < len(coefficients):
        degree = len(powers)
        powers.append(lower**(degree-1)+(degree-1)*powers[degree-2])
    exponent = lower*lower/2
    exponential_bound = Fraction(1, 2**(exponent.numerator//exponent.denominator))
    return exponential_bound*sum(value*powers[degree]
                                 for degree, value in enumerate(coefficients))


def radial_tail_bounds(epsilon: Fraction, cutoff: Fraction):
    """Bound normalization, centered KL, chi-square and eta-Fisher tails.

    p_R(r)=sqrt(2/pi)*r^2*exp(-r^2/2),
    likelihood=exp(-a^2/2)*sinh(a*r)/(a*r), a=abs(epsilon)<=1.
    Use sqrt(2/pi)<1 and likelihood<=exp(a*r-a^2/2).
    For its square the completed square contributes exp(a^2)<3.
    For eta>0, |score_eta| <= (a+r)/(2*a), from 0<=coth(x)-1/x<=1.
    """
    a = abs(epsilon)
    assert a <= 1 and cutoff > 2*a
    base = polynomial_gaussian_tail((0, 0, 1), cutoff)
    normalization = polynomial_gaussian_tail((a*a, 2*a, 1), cutoff-a)
    if a == 0:
        fisher = polynomial_gaussian_tail(
            (0, 0, Fraction(1, 4), 0, Fraction(1, 6), 0, Fraction(1, 36)), cutoff)
        return normalization, Fraction(0), Fraction(0), fisher
    # |log likelihood| <= a^2/2+a*r. The KL integral is evaluated
    # as E[likelihood*log likelihood-likelihood+1] to avoid cancellation.
    log_tail = polynomial_gaussian_tail(
        (Fraction(3, 2)*a**4, 4*a**3, Fraction(7, 2)*a*a, a), cutoff-a)
    kl = log_tail+normalization+base
    second_moment = 3*polynomial_gaussian_tail((4*a*a, 4*a, 1), cutoff-2*a)
    chi_square = second_moment+2*normalization+base
    fisher = polynomial_gaussian_tail(
        (4*a**4, 12*a**3, 13*a*a, 6*a, 1), cutoff-a)/(4*a*a)
    return normalization, kl, chi_square, fisher


def radial_quadrature(epsilon: float, radii, weights):
    a = abs(epsilon)
    x = a*radii
    log_likelihood = np.zeros_like(radii)
    score_eta = (radii*radii-3)/6
    if a:
        small = x < 0.1
        z = x[small]**2
        log_sinhc = z*(1/6+z*(-1/180+z*(1/2835+z*(-1/37800+z/467775))))
        log_likelihood[small] = -a*a/2+log_sinhc
        log_likelihood[~small] = -a*a/2+np.log(np.sinh(x[~small])/x[~small])
        score_eta[small] = -0.5+radii[small]**2*(
            1/6+z*(-1/90+z*(1/945+z*(-1/9450+z/93555))))
        score_eta[~small] = -0.5+radii[~small]/(2*a)*(
            1/np.tanh(x[~small])-1/x[~small])
    likelihood = np.exp(log_likelihood)
    difference = np.expm1(log_likelihood)
    kl_density = likelihood*log_likelihood-difference
    # exp(l)*l-exp(l)+1 = sum_(n>=2) (n-1)*l^n/n!.
    small_log = np.abs(log_likelihood) < 0.05
    coefficients = [(n-1)/math.factorial(n) for n in range(2, 17)]
    kl_density[small_log] = log_likelihood[small_log]**2*np.polynomial.polynomial.polyval(
        log_likelihood[small_log], coefficients)
    radial_weight = weights*math.sqrt(2/math.pi)*radii*radii*np.exp(-radii*radii/2)
    return np.array([
        np.dot(radial_weight, likelihood),
        np.dot(radial_weight, kl_density),
        np.dot(radial_weight, difference*difference),
        np.dot(radial_weight, likelihood*score_eta*score_eta),
    ])


def gaussian_radial_checks() -> None:
    """Integrate the entire radial density up to explicitly bounded tails."""
    cutoff = Fraction(16)
    epsilons = (Fraction(0), Fraction(1, 32), Fraction(1, 16), Fraction(1, 8),
                Fraction(1, 4), Fraction(1, 2), Fraction(1))
    quadratures = {}
    for order in (128, 256, 512):
        nodes, weights = np.polynomial.legendre.leggauss(order)
        quadratures[order] = ((nodes+1)*float(cutoff)/2, weights*float(cutoff)/2)
    max_refinement_error = 0.0
    print("Full radial quadrature: epsilon  normalization error  KL/epsilon^4  "
          "eta-Fisher  chi-square identity error  rigorous tail bound")
    for epsilon in epsilons:
        values = {order: radial_quadrature(float(epsilon), *grid)
                  for order, grid in quadratures.items()}
        fine = values[512]
        refinement_error = max(float(np.max(np.abs(values[order]-fine)))
                               for order in (128, 256))
        assert refinement_error < 3e-13
        max_refinement_error = max(max_refinement_error, refinement_error)
        assert abs(fine[0]-1) < 4e-14
        tails = radial_tail_bounds(epsilon, cutoff)
        assert all(bound < Fraction(1, 10**24) for bound in tails)
        with localcontext() as context:
            context.prec = 70
            eta = Decimal(epsilon.numerator)**2/Decimal(epsilon.denominator)**2
            exact_chi_square = ((eta.exp()-(-eta).exp())/(2*eta)-1) if eta else Decimal(0)
        # Averaging two sphere directions gives E[r_epsilon^2]
        # =sinh(epsilon^2)/epsilon^2 exactly, independent of quadrature.
        chi_error = abs(fine[2]-float(exact_chi_square))
        assert chi_error < 3e-14
        if epsilon:
            ratio = fine[1]/float(epsilon**4)
            if epsilon <= Fraction(1, 4):
                assert abs(ratio-1/12) < 0.002
            ratio_text = f"{ratio:.10e}"
        else:
            assert fine[1] == fine[2] == 0
            assert math.isclose(fine[3], 1/6, rel_tol=3e-13)
            ratio_text = "boundary"
        print(f"{float(epsilon):7g}  {abs(fine[0]-1):.3e}  {ratio_text:>16}  "
              f"{fine[3]:.10e}  {chi_error:.3e}  {float(max(tails)):.3e}")
    print("PASS seven full radial likelihood integrals: 128/256/512-point quadrature "
          f"discrepancy <= {max_refinement_error:.3e}; all omitted tails bounded by exact "
          "rational estimates below 1e-24")


def inverse_fraction_matrix(matrix):
    size = len(matrix)
    augmented = [list(row)+[Fraction(int(i == j)) for j in range(size)]
                 for i, row in enumerate(matrix)]
    for column in range(size):
        pivot = next(i for i in range(column, size) if augmented[i][column])
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        denominator = augmented[column][column]
        augmented[column] = [value/denominator for value in augmented[column]]
        for row in range(size):
            if row != column:
                multiplier = augmented[row][column]
                augmented[row] = [left-multiplier*right
                                  for left, right in zip(augmented[row], augmented[column])]
    assert all(augmented[i][j] == int(i == j) for i in range(size) for j in range(size))
    return [row[size:] for row in augmented]


def path_fisher_precision_checks() -> None:
    """Exact discrete Cameron--Martin metric, not finite heat-law Fisher."""
    times = (Fraction(1, 7), Fraction(2, 5), Fraction(3, 4), Fraction(1), Fraction(3, 2))
    durations = tuple(t-s for s, t in zip((Fraction(0),)+times[:-1], times))
    size = len(times)

    def negative_log_quadratic(path):
        increments = (value-previous for previous, value in zip((Fraction(0),)+tuple(path[:-1]), path))
        return sum(increment*increment/(4*dt) for increment, dt in zip(increments, durations))

    units = [tuple(Fraction(int(i == j)) for i in range(size)) for j in range(size)]
    precision = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            # Exact finite difference Hessian of the increment action.
            together = tuple(a+b for a, b in zip(units[i], units[j]))
            precision[i][j] = (negative_log_quadratic(together)
                               - negative_log_quadratic(units[i])
                               - negative_log_quadratic(units[j]))
    inverse = inverse_fraction_matrix(precision)
    assert all(inverse[i][j] == 2*min(times[i], times[j])
               for i in range(size) for j in range(size))
    for axis in range(3):
        path = tuple(Fraction((i+1)*(axis+2)-axis*axis, 11) for i in range(size))
        norm = sum(path[i]*precision[i][j]*path[j] for i in range(size) for j in range(size))
        assert norm == 2*negative_log_quadratic(path) > 0
    print("PASS exact five-time increment-Hessian inversion: all 25 inverse entries "
          "equal 2*min(s,t); three-component Cameron--Martin norms agree")


def exact_frame_audit() -> None:
    """Expose pointwise frame dependence without comparing integrated energies."""
    f = Fraction

    def cross(left, right):
        return (left[1]*right[2]-left[2]*right[1],
                left[2]*right[0]-left[0]*right[2],
                left[0]*right[1]-left[1]*right[0])

    def dot(left, right):
        return sum(a*b for a, b in zip(left, right))

    scalar = (f(0), f(4, 5), f(0))
    vectors = ((f(1), f(0), f(0)), (f(0), f(3, 5), f(0)),
               (f(3, 5), f(0), f(4, 5)))
    assert all(w*w+dot(v, v) == 1 for w, v in zip(scalar, vectors))
    cofactors = (cross(vectors[1], vectors[2]), cross(vectors[2], vectors[0]),
                 cross(vectors[0], vectors[1]))
    left, right = [], []
    for w, v, b in zip(scalar, vectors, cofactors):
        rotation = cross(v, b)
        left.append(tuple((w*component+turn)/2 for component, turn in zip(b, rotation)))
        right.append(tuple((w*component-turn)/2 for component, turn in zip(b, rotation)))
    assert tuple(row[1] for row in left) == (f(9, 50), f(16, 50), -f(9, 50))
    assert tuple(row[1] for row in right) == (-f(9, 50), f(16, 50), f(9, 50))
    assert all(row[0] == row[2] == 0 for row in left+right)
    rotated = tuple((v[1], v[2], v[0]) for v in vectors)
    assert dot(vectors[0], cofactors[0]) == dot(rotated[0], cross(rotated[1], rotated[2]))
    times = (1, 2, 3)

    def response(gradients):
        return sum(2*min(times[i], times[j])*dot(gradients[i], gradients[j])
                   for i in range(3) for j in range(3))

    assert response(left) == f(193, 625)
    assert response(right) == f(481, 625)
    print("PASS exact quaternion frame audit: invariant determinant has pointwise "
          "Gamma_left=193/625 and Gamma_right=481/625; no integrated-energy inequality inferred")


def main() -> None:
    print("path-shift Fisher receipt: reference Gaussian driver and explicit frame distinctions")
    exact_projection_coefficients()
    gaussian_radial_checks()
    path_fisher_precision_checks()
    exact_frame_audit()
    print("Finite diagnostics and exact coefficient checks only; quadrature refinement is not "
          "a certified quadrature-error bound. No right/left clock identification, Born rule, "
          "four-dimensional construction or physical mass gap is certified.")


if __name__ == "__main__":
    main()
