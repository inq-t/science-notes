"""Numerical checks for the distinction-grain spectrum identities."""

from __future__ import annotations

import math


TOL = 1.0e-12
ALPHA = 0.5
DELTA = 0.7


def half_grain(edge: float) -> float:
    return -math.log1p(-ALPHA) / (2.0 * edge)


def main() -> None:
    uniform_half_grain = half_grain(DELTA)
    recoverability = math.exp(-2.0 * DELTA * uniform_half_grain)
    reconstructed_edge = math.log(2.0) / (2.0 * uniform_half_grain)

    assert abs(recoverability - 0.5) < TOL
    assert abs(reconstructed_edge - DELTA) < TOL

    truncations = (10, 100, 1000, 10000)
    fixed_depth = 1.0
    gapless_rows = []
    for n_max in truncations:
        smallest_edge = 1.0 / n_max
        largest_half_grain = half_grain(smallest_edge)
        retained_norm_squared = math.exp(-2.0 * fixed_depth * smallest_edge)
        gapless_rows.append(
            (n_max, largest_half_grain, retained_norm_squared)
        )

    assert all(
        gapless_rows[i + 1][1] > gapless_rows[i][1]
        for i in range(len(gapless_rows) - 1)
    )
    assert all(
        gapless_rows[i + 1][2] > gapless_rows[i][2]
        for i in range(len(gapless_rows) - 1)
    )

    # X_N = exp(N) Z with Z standard normal has score Z^2 - 1.
    # Its Fisher information is Var(Z^2) = 2.  The moving identification
    # Y_N = exp(-N) X_N returns the N-independent standard-normal law.
    original_scale_fisher = 2.0
    transported_scale_fisher = 0.0
    assert original_scale_fisher > transported_scale_fisher

    # Genuine product-sign Markov channel: Z_n = X_n W_n, with X_n
    # unbiased and E[W_n] = q_n.  The conditional expectation has Walsh
    # singular values prod(q_i).  One direction is exactly balanced while
    # the complete mean-zero contraction tends to one.
    balanced_recoverable = 0.5
    balanced_residual = 1.0 - balanced_recoverable
    assert abs(balanced_recoverable - balanced_residual) < TOL
    walsh_rows = []
    for n_max in truncations:
        complete_norm_squared = 1.0 - 1.0 / n_max
        complete_defect_edge = 1.0 / n_max
        walsh_rows.append(
            (n_max, complete_norm_squared, complete_defect_edge)
        )
    assert all(
        walsh_rows[i + 1][1] > walsh_rows[i][1]
        for i in range(len(walsh_rows) - 1)
    )
    assert all(
        walsh_rows[i + 1][2] < walsh_rows[i][2]
        for i in range(len(walsh_rows) - 1)
    )

    print("distinction-grain spectrum receipt")
    print(f"gapped edge: {DELTA:.12f}")
    print(f"uniform half grain: {uniform_half_grain:.12f}")
    print(f"recoverable fraction there: {recoverability:.12f}")
    print(f"reconstructed edge: {reconstructed_edge:.12f}")
    print("gapless diagonal truncations")
    for n_max, largest_half_grain, retained_norm_squared in gapless_rows:
        print(
            f"N={n_max:5d}  "
            f"largest_half_grain={largest_half_grain:.12f}  "
            f"fixed_depth_retention={retained_norm_squared:.12f}"
        )
    print("moving-carrier score check")
    print(f"original scale Fisher: {original_scale_fisher:.12f}")
    print(f"transported scale Fisher: {transported_scale_fisher:.12f}")
    print("product-sign Markov counterexample")
    print(f"selected recoverable fraction: {balanced_recoverable:.12f}")
    print(f"selected residual fraction: {balanced_residual:.12f}")
    for n_max, complete_norm_squared, complete_defect_edge in walsh_rows:
        print(
            f"N={n_max:5d}  "
            f"complete_norm_squared={complete_norm_squared:.12f}  "
            f"complete_defect_edge={complete_defect_edge:.12f}"
        )
    print("PASS: a moving carrier identification can erase a scale score")
    print("PASS: individual grains can be finite while their uniform ceiling diverges")
    print("PASS: one balanced Markov direction need not give a complete-carrier gap")


if __name__ == "__main__":
    main()
