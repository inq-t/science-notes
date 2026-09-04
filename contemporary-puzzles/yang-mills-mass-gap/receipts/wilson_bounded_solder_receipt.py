"""Finite checks for the SU(2) pure product-Wilson bounded solder.

This receipt checks Bessel arithmetic, tensor eigenvalues, and the
tree-level temporal scaling. The analytic proof uses Peter--Weyl
diagonalization, Bessel order monotonicity, and closed spin-network support.
It does not test the interacting magnetic sandwich or a continuum mass gap.
"""

from __future__ import annotations

import math


def bessel_i(n: int, x: float) -> float:
    """Return I_n(x) from its positive power series for n >= 0 and x > 0."""

    term = (0.5 * x) ** n / math.factorial(n)
    total = term
    for k in range(1, 10000):
        term *= (0.25 * x * x) / (k * (n + k))
        updated = total + term
        if abs(updated - total) <= 2.0e-16 * abs(updated):
            return updated
        total = updated
    raise RuntimeError("Bessel series did not converge")


def p(j_twice: int, x: float) -> float:
    """Wilson convolution eigenvalue for spin j=j_twice/2."""

    return bessel_i(j_twice + 1, x) / bessel_i(1, x)


def main() -> None:
    print("SU(2) Wilson bounded-solder receipt")

    for x in [0.2, 1.0, 4.0, 20.0]:
        eigenvalues = [p(j_twice, x) for j_twice in range(0, 25)]
        assert abs(eigenvalues[0] - 1.0) < 2.0e-14
        assert all(
            left > right > 0.0
            for left, right in zip(eigenvalues, eigenvalues[1:])
        )
        gamma = 1.0 - eigenvalues[1]
        smallest_sampled_defect = min(1.0 - value for value in eigenvalues[1:])
        assert abs(gamma - smallest_sampled_defect) < 2.0e-14
        assert gamma > 1.0 / (x + 1.0)
        print(
            f"x={x:4.1f}: p_half={eigenvalues[1]:.12f}, "
            f"sharp edge={gamma:.12f}, "
            f"elementary floor={1.0 / (x + 1.0):.12f}"
        )

    x = 5.0
    p_half = p(1, x)
    girth = 4
    sharp_gauge_edge = 1.0 - p_half**girth
    elementary_gauge_floor = 1.0 - (x / (x + 1.0)) ** girth
    sampled_labels = [
        [1, 1, 1, 1],
        [2, 2, 2, 2],
        [1, 1, 1, 1, 1, 1],
        [1, 2, 1, 2],
    ]
    sampled_products = [
        math.prod(p(label, x) for label in labels)
        for labels in sampled_labels
    ]
    assert abs(sampled_products[0] - p_half**girth) < 2.0e-14
    assert all(value <= p_half**girth + 2.0e-14 for value in sampled_products)
    assert sharp_gauge_edge > elementary_gauge_floor
    print(
        f"square-girth contraction={p_half**girth:.12f}, "
        f"defect edge={sharp_gauge_edge:.12f}, "
        f"elementary floor={elementary_gauge_floor:.12f}"
    )

    for x in [25.0, 50.0, 100.0]:
        ratio = p(1, x)
        scaled_defect = x * (1.0 - ratio)
        scaled_log_edge = x * math.log(1.0 / ratio)
        assert abs(scaled_defect - 1.5) < 0.05
        assert abs(scaled_log_edge - 1.5) < 0.07
        print(
            f"x={x:5.1f}: x(1-p_half)={scaled_defect:.9f}, "
            f"x log(1/p_half)={scaled_log_edge:.9f}"
        )

    spatial_spacing = 0.7
    bare_coupling = 0.8
    target = (
        girth
        * 3.0
        * bare_coupling**2
        / (8.0 * spatial_spacing)
    )
    for temporal_spacing in [0.04, 0.02, 0.01]:
        beta_t = (
            4.0
            * spatial_spacing
            / (bare_coupling**2 * temporal_spacing)
        )
        physical_edge = (
            girth
            * math.log(1.0 / p(1, beta_t))
            / temporal_spacing
        )
        ratio = physical_edge / target
        assert abs(ratio - 1.0) < 0.01
        print(
            f"a_tau={temporal_spacing:.3f}: "
            f"edge/electric-Casimir={ratio:.9f}"
        )

    print("PASS: pure product-Wilson edge and temporal scaling agree")


if __name__ == "__main__":
    main()
