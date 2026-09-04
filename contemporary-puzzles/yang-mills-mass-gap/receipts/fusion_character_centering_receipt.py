"""Finite checks for the fusion-character centering identities.

This receipt checks algebra and normalization only. It does not establish
tube admissibility, a Yang--Mills carrier action, or a continuum mass gap.
"""

from __future__ import annotations

import math


def delta(eta: float) -> float:
    return (
        1.0
        + 2.0 * math.cosh(2.0 * eta)
        + 2.0 * math.cosh(8.0 * eta)
        + 2.0 * math.cosh(10.0 * eta)
    )


def wilson_character(t: float) -> float:
    # U_t = diag(exp(it), exp(-it), 1) in SU(3), and
    # X|SU(3) = 1 + 3 + conjugate(3).
    return 3.0 + 4.0 * math.cos(t)


def wilson_cost(t: float) -> float:
    return (2.0 / 3.0) * (1.0 - math.cos(t))


def normalize(values: list[float]) -> list[float]:
    total = sum(values)
    return [value / total for value in values]


def max_error(xs: list[float], ys: list[float]) -> float:
    return max(abs(x - y) for x, y in zip(xs, ys, strict=True))


def main() -> None:
    tol = 2.0e-13
    etas = [0.0, 0.02, -0.02, math.log(1.1)]
    ts = [0.0, 0.2, 0.5, 0.9]

    print("fusion-character centering receipt")
    print("delta(0) =", f"{delta(0.0):.12f}")
    assert abs(delta(0.0) - 7.0) < tol
    assert all(delta(eta) > 7.0 for eta in etas if eta != 0.0)
    assert abs(delta(0.02) - delta(-0.02)) < tol

    largest_identity_error = 0.0
    for eta in etas:
        d_q = delta(eta)
        for t in ts:
            direct = 1.0 - wilson_character(t) / d_q
            decomposed = (d_q - 7.0) / d_q + 6.0 * wilson_cost(t) / d_q
            largest_identity_error = max(
                largest_identity_error, abs(direct - decomposed)
            )
    print("max CW16 identity error =", f"{largest_identity_error:.3e}")
    assert largest_identity_error < tol

    # The classical centered cost approaches zero quadratically at flat
    # holonomy; it has no positive multiplication floor.
    for t in [1.0e-2, 1.0e-3, 1.0e-4]:
        classical_cost = 1.0 - wilson_character(t) / 7.0
        quadratic_limit = (2.0 / 7.0) * t * t
        ratio = classical_cost / quadratic_limit
        print(f"classical near-flat ratio at t={t:.0e}: {ratio:.12f}")
        assert abs(ratio - 1.0) < 1.0e-4

    eta = 0.02
    d_q = delta(eta)
    beta = 1.7
    fusion_costs = [1.0 - wilson_character(t) / d_q for t in ts]
    wilson_costs = [wilson_cost(t) for t in ts]
    p_fusion = normalize([math.exp(-beta * x) for x in fusion_costs])
    p_wilson = normalize(
        [math.exp(-(6.0 * beta / d_q) * x) for x in wilson_costs]
    )
    gibbs_error = max_error(p_fusion, p_wilson)
    print("normalized Gibbs cancellation error =", f"{gibbs_error:.3e}")
    assert gibbs_error < tol

    scalar_offset = (d_q - 7.0) / d_q
    base_spectrum = [0.13, 0.41, 1.07, 2.2]
    shifted_spectrum = [x + scalar_offset for x in base_spectrum]
    base_gaps = [x - base_spectrum[0] for x in base_spectrum]
    shifted_gaps = [x - shifted_spectrum[0] for x in shifted_spectrum]
    spectral_error = max_error(base_gaps, shifted_gaps)
    print("spectral-difference centering error =", f"{spectral_error:.3e}")
    assert spectral_error < tol

    print("PASS: scalar quantum-dimension floor cancels after normalization")


if __name__ == "__main__":
    main()
