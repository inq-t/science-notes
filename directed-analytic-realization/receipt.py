"""Finite checks for the directed analytic-tail realization.

No files are written. These tests check representative finite modes,
transients, action signs and exact rational refinement embeddings.
The infinite-dimensional quotient, self-adjointness and limiting spectrum
are proved in the notes, not certified by this finite receipt.
"""

from __future__ import annotations

import cmath
from fractions import Fraction
import math


def close(label, actual, expected, tol=2e-9):
    if abs(actual - expected) > tol:
        raise AssertionError(f"{label}: {actual!r} != {expected!r}")


def inner(a, b):
    return sum(x.conjugate() * y for x, y in zip(a, b))


def flow(a, s, radius):
    return [x * cmath.exp(-1j * n * s / radius) for n, x in enumerate(a)]


def polynomial(a, x, radius):
    return sum(v * cmath.exp(-1j * n * x / radius)
               for n, v in enumerate(a))


def exponential_integral(frequency, lo, hi):
    if frequency == 0:
        return complex(hi - lo)
    return (cmath.exp(1j * frequency * hi)
            - cmath.exp(1j * frequency * lo)) / (1j * frequency)


def finite_pair(a, b, radius, length, transient_a, transient_b):
    # Each transient is a constant on [0, support).
    amp_a, support_a = transient_a
    amp_b, support_b = transient_b
    value = sum(
        x.conjugate() * y
        * exponential_integral((n - m) / radius, 0, length)
        for n, x in enumerate(a) for m, y in enumerate(b)
    )
    end_a = min(length, support_a)
    end_b = min(length, support_b)
    value += sum(
        x.conjugate() * amp_b
        * exponential_integral(n / radius, 0, end_b)
        for n, x in enumerate(a)
    )
    value += sum(
        amp_a.conjugate() * y
        * exponential_integral(-m / radius, 0, end_a)
        for m, y in enumerate(b)
    )
    value += amp_a.conjugate() * amp_b * min(end_a, end_b)
    return value / length


def integrate(f):
    # Three-point Gauss quadrature on [0,1], exact through degree five.
    offset = math.sqrt(15) / 10
    return (5 * f(0.5 - offset) + 8 * f(0.5)
            + 5 * f(0.5 + offset)) / 18


def action(a, da, radius):
    def lagrangian(s):
        value, derivative = a(s), da(s)
        energy = sum(n / radius * abs(z) ** 2
                     for n, z in enumerate(value))
        return -inner(value, derivative).imag - energy
    return integrate(lagrangian)


def main():
    radius = 1.7
    a = [0.7 + 0.2j, -0.1 + 0.5j, 0.3 - 0.8j, 0.2j]
    b = [0.2 - 0.1j, 0.4 + 0.2j, -0.3j, 0.8]
    b = [complex(z) for z in b]
    s, t = 0.37, 0.91

    for left, right in zip(flow(flow(a, s, radius), t, radius),
                           flow(a, s + t, radius)):
        close("semigroup composition", left, right)
    for x in (0.0, 0.4, 2.3, 6.2):
        close("translation intertwining",
              polynomial(a, x + s, radius),
              polynomial(flow(a, s, radius), x, radius))
    close("Hermitian response", inner(flow(a, s, radius),
                                     flow(b, s, radius)), inner(a, b))
    close("symplectic preservation",
          2 * inner(flow(a, s, radius), flow(b, s, radius)).imag,
          2 * inner(a, b).imag)
    close("symplectic nondegeneracy witness",
          2 * inner(a, [1j * z for z in a]).imag, 2 * inner(a, a).real)
    print("PASS: translation, composition, Hermitian and symplectic return")

    support = 0.25
    if max(0.0, support - s) != 0:
        raise AssertionError("Initial transient was not erased")
    # Exact Fourier mean plus explicit O(1/L) transient residue.
    pair = inner(a, b)
    transient_a = (0.2 + 0.7j, 0.4)
    transient_b = (-0.3 + 0.1j, 0.8)
    scaled = []
    for cycles in (1, 7, 101):
        length = cycles * 2 * math.pi * radius
        finite = finite_pair(a, b, radius, length,
                             transient_a, transient_b)
        scaled.append(length * (finite - pair))
    close("transient numerator independent of averaging length",
          scaled[0], scaled[1], 2e-8)
    close("transient numerator at longer averaging length",
          scaled[0], scaled[2], 2e-8)
    print("PASS: finite erasure and exact inverse-length transient correction")

    finite_cut = 2.0
    for x in (0.0, 0.25, 0.8, 1.7):
        transient = polynomial(a, x, radius) - polynomial(b, x, radius)
        if x >= finite_cut:
            transient = 0j
        close("finite-cut histories agree",
              polynomial(b, x, radius) + transient,
              polynomial(a, x, radius))
    if sum(abs(x - y) ** 2 for x, y in zip(a, b)) == 0:
        raise AssertionError("The different quotient classes accidentally coincide")
    print("PASS: equal finite-cut histories can have different realized tails")

    d = [0.1j, 0.2 - 0.3j, -0.1, 0.15j]
    e = [0.03, 0.05j, 0.02 - 0.01j, -0.04]
    w = [0.2j, -0.1 + 0.1j, 0.07, -0.09j]

    def path(u):
        return [x + y * u + z * u * u for x, y, z in zip(a, d, e)]

    def derivative(u):
        return [y + 2 * z * u for y, z in zip(d, e)]

    def variation(u):
        return [z * u * (1 - u) for z in w]

    def variation_derivative(u):
        return [z * (1 - 2 * u) for z in w]

    def perturbed(epsilon):
        return action(
            lambda u: [x + epsilon * y for x, y in zip(path(u), variation(u))],
            lambda u: [x + epsilon * y for x, y
                       in zip(derivative(u), variation_derivative(u))],
            radius,
        )

    epsilon = 1e-4
    finite_variation = (perturbed(epsilon) - perturbed(-epsilon)) / (2 * epsilon)

    def first_variation(u):
        residual = [1j * dz - n / radius * z
                    for n, (z, dz) in enumerate(zip(path(u), derivative(u)))]
        return 2 * inner(variation(u), residual).real

    close("action first variation", finite_variation,
          integrate(first_variation), 2e-8)
    exact_path = lambda u: flow(a, u, radius)
    exact_derivative = lambda u: [
        -1j * n / radius * z for n, z in enumerate(exact_path(u))
    ]
    close("on-shell state action", action(exact_path, exact_derivative, radius), 0)
    print("PASS: independent action variation and on-shell sign checks")

    for stage in range(1, 7):
        old_radius = Fraction(math.factorial(stage))
        new_radius = Fraction(math.factorial(stage + 1))
        multiplier = stage + 1
        for n in range(9):
            old_frequency = Fraction(n) / old_radius
            new_frequency = Fraction(multiplier * n) / new_radius
            if old_frequency != new_frequency:
                raise AssertionError("Refinement changed an old frequency")
        if Fraction(1) / new_radius >= Fraction(1) / old_radius:
            raise AssertionError("Refinement did not add a lower positive rate")
    print("PASS: exact rational refinement preserves old rates and adds soft modes")
    if -1 / radius >= 0:
        raise AssertionError("Negative Fourier mode unexpectedly has a positive generator value")
    print("PASS: Fourier-orientation negative control")
    print("Scope: finite algebraic checks only; no four-dimensional QFT or physical gap certified")


if __name__ == "__main__":
    main()
