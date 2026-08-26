"""Arithmetic checks for the finite cellular Markov-wall formulas.

This receipt verifies only the finite semigroup, state law, and BKM identities.
It is not evidence for a Lorentzian carrier, continuum limit, or cosmological weld.
"""

from __future__ import annotations

import math


def polarization(r_star: float, scale_depth: float) -> float:
    return r_star * math.exp(-scale_depth)


def binary_relative_entropy(r_left: float, r_right: float) -> float:
    """D(r_left || r_right) for rho(r)=(1+r q)/2."""

    return (
        0.5 * (1.0 + r_left) * math.log((1.0 + r_left) / (1.0 + r_right))
        + 0.5 * (1.0 - r_left) * math.log((1.0 - r_left) / (1.0 - r_right))
    )


def main() -> None:
    r_star = 0.4
    scale_depth = 0.7
    cells = 5
    step = 1.0e-4
    first_time = 0.3
    second_time = 0.8

    # C_t=P_0+exp(-t)(id-P_0), so composition reduces to this coefficient.
    composed = math.exp(-first_time) * math.exp(-second_time)
    direct = math.exp(-(first_time + second_time))
    assert math.isclose(composed, direct, rel_tol=0.0, abs_tol=1.0e-15)

    r_now = polarization(r_star, scale_depth)
    r_later = polarization(r_star, scale_depth + first_time)
    assert math.isclose(r_later, math.exp(-first_time) * r_now, abs_tol=1.0e-15)

    r_plus = polarization(r_star, scale_depth + step)
    r_minus = polarization(r_star, scale_depth - step)
    finite_difference = cells * (
        binary_relative_entropy(r_plus, r_now)
        + binary_relative_entropy(r_minus, r_now)
    ) / step**2
    exact_bkm = cells * r_now**2 / (1.0 - r_now**2)
    assert math.isclose(finite_difference, exact_bkm, rel_tol=1.0e-6)

    mean_zero_score = (2.0, -1.0, -1.0, 0.5, -0.5)
    mixed_block = -r_now * sum(mean_zero_score)
    assert math.isclose(mixed_block, 0.0, abs_tol=1.0e-15)

    density = r_now**2 / (1.0 - r_now**2)
    assert math.isclose((2 + 3) * density, 2 * density + 3 * density)

    selected_profile = r_now**2 / (1.0 - r_now**2)
    balanced_binary_profile = 1.0 / math.cosh(scale_depth) ** 2
    assert not math.isclose(selected_profile, balanced_binary_profile, rel_tol=1.0e-3)

    print("finite cellular Markov-wall receipt: 6/6 checks passed")
    print(f"finite-difference BKM = {finite_difference:.12f}")
    print(f"closed-form BKM      = {exact_bkm:.12f}")


if __name__ == "__main__":
    main()
