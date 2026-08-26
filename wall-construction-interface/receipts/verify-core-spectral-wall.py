"""Scalar checks for the core spectral wall and its character solder.

This receipt verifies the displayed trace, logistic, Fisher, and discriminant
identities only. It does not verify the operator-algebraic hypotheses, select a
physical state, or construct a Lorentzian causal wall.
"""

from __future__ import annotations

import math


def q_logistic(x: float, nu: float, center: float) -> float:
    return 0.5 * nu / math.cosh(nu * (x - center)) ** 2


def cut_probability(x: float, nu: float, center: float) -> float:
    return 0.5 * (1.0 + math.tanh(nu * (x - center)))


def simpson(function, left: float, right: float, intervals: int = 20000) -> float:
    if intervals % 2:
        raise ValueError("Simpson integration requires an even interval count")
    step = (right - left) / intervals
    total = function(left) + function(right)
    total += 4.0 * sum(function(left + step * index) for index in range(1, intervals, 2))
    total += 2.0 * sum(function(left + step * index) for index in range(2, intervals, 2))
    return total * step / 3.0


def main() -> None:
    nu = 1.3
    center = -0.4
    point = 0.7
    step = 1.0e-5

    # tau(e_N)=exp(N), with multiplicative composition under additive scale.
    first = 0.8
    second = -0.3
    assert math.isclose(
        math.exp(first + second),
        math.exp(first) * math.exp(second),
        rel_tol=0.0,
        abs_tol=1.0e-15,
    )

    # The logistic spectral density is normalized on the trace measure.
    normalization = simpson(
        lambda x: q_logistic(x, nu, center),
        center - 20.0 / nu,
        center + 20.0 / nu,
    )
    assert math.isclose(normalization, 1.0, rel_tol=0.0, abs_tol=1.0e-12)

    # Its cumulative probability differentiates back to the spectral density.
    derivative = (
        cut_probability(point + step, nu, center)
        - cut_probability(point - step, nu, center)
    ) / (2.0 * step)
    density = q_logistic(point, nu, center)
    assert math.isclose(derivative, density, rel_tol=1.0e-9)

    # Binary Fisher equals the claimed sech-squared pulse.
    probability = cut_probability(point, nu, center)
    binary_fisher = density**2 / (probability * (1.0 - probability))
    pulse = nu**2 / math.cosh(nu * (point - center)) ** 2
    assert math.isclose(binary_fisher, pulse, rel_tol=1.0e-14)

    # The full commuting location family has constant Fisher metric 4 nu^2/3.
    full_fisher = simpson(
        lambda x: q_logistic(x, nu, center)
        * (-2.0 * nu * math.tanh(nu * (x - center))) ** 2,
        center - 20.0 / nu,
        center + 20.0 / nu,
    )
    assert math.isclose(full_fisher, 4.0 * nu**2 / 3.0, abs_tol=1.0e-12)

    # The binary readout obeys monotonicity at every sampled cut.
    for index in range(-100, 101):
        sample = center + index / (10.0 * nu)
        probability = cut_probability(sample, nu, center)
        density = q_logistic(sample, nu, center)
        observed = density**2 / (probability * (1.0 - probability))
        assert observed <= full_fisher + 1.0e-12

    # On t=t_* exp(-N), the cubic discriminant is Delta=-4 t^6.
    scale = 1.7
    t_star = 2.4
    t_now = t_star * math.exp(-scale)
    delta_star = -4.0 * t_star**6
    delta_now = -4.0 * t_now**6
    a2_character = (abs(delta_star) / abs(delta_now)) ** (1.0 / 6.0)
    assert math.isclose(a2_character, math.exp(scale), rel_tol=1.0e-14)

    # The sixth-power trace/discriminant character balance is exact.
    trace_character = math.exp(scale)
    balance = trace_character**6 * abs(delta_now) / abs(delta_star)
    assert math.isclose(balance, 1.0, rel_tol=1.0e-14)

    print("core spectral wall receipt: 8/8 checks passed")
    print(f"binary Fisher at sample = {binary_fisher:.12f}")
    print(f"full location Fisher    = {full_fisher:.12f}")


if __name__ == "__main__":
    main()
