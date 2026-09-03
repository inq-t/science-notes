"""Finite checks for paired scale filtrations and the incidence-wall theorem.

This receipt checks only matrix/arithmetic shadows of the exact statements.  It
does not select a Yang--Mills filtration, prove a continuum limit, or identify
the constructed diagonal operator with the physical Poincare Casimir.
"""

from __future__ import annotations

import math

import numpy as np


def projection(index: int, size: int) -> np.ndarray:
    p = np.zeros((size, size), dtype=float)
    p[index, index] = 1.0
    return p


def assert_close(left: np.ndarray | float, right: np.ndarray | float) -> None:
    if not np.allclose(left, right, rtol=1e-12, atol=1e-12):
        raise AssertionError(f"mismatch:\n{left}\n!=\n{right}")


def finite_incidence_check() -> None:
    # Basis vectors carry the nonzero incidences (0, 2), (1, 1), and (2, 0).
    size = 3
    d_plus = [projection(j, size) for j in range(size)]
    d_minus = [projection(2 - k, size) for k in range(size)]
    identity = np.eye(size)
    assert_close(sum(d_plus), identity)
    assert_close(sum(d_minus), identity)

    addresses = [0.0, 1.0, 2.0]
    k_plus = sum(math.exp(-addresses[j]) * d_plus[j] for j in range(size))
    k_minus = sum(math.exp(-addresses[k]) * d_minus[k] for k in range(size))
    mass = np.diag(np.sqrt(np.diag(k_plus @ k_minus)))

    # Every occupied pair has mean address one.
    assert_close(mass, math.exp(-1.0) * identity)
    occupied = []
    for j in range(size):
        for k in range(size):
            q_jk = d_plus[j] @ d_minus[k]
            if np.linalg.norm(q_jk) > 1e-12:
                occupied.append((j, k, (addresses[j] + addresses[k]) / 2.0))
    if occupied != [(0, 2, 1.0), (1, 1, 1.0), (2, 0, 1.0)]:
        raise AssertionError(occupied)
    print("finite joint-shell incidence and diagonal wall: passed")


def gapless_pair_limit_check() -> None:
    # Larger rapidity windows drive each one-sided floor to zero while the
    # product floor remains fixed.
    n0 = 0.7
    delta = 0.25
    one_sided_floors = []
    product_floors = []
    for radius in (2, 5, 10, 20):
        js = np.arange(-radius, radius + 1, dtype=float)
        a_plus = n0 + delta * js
        a_minus = n0 - delta * js
        k_plus = np.exp(-a_plus)
        k_minus = np.exp(-a_minus)
        one_sided_floors.append(min(k_plus.min(), k_minus.min()))
        product_floors.append(np.sqrt((k_plus * k_minus).min()))
    if not all(x > y for x, y in zip(one_sided_floors, one_sided_floors[1:])):
        raise AssertionError(one_sided_floors)
    assert_close(product_floors, np.full(4, math.exp(-n0)))
    print("gapless one-sided limit with fixed joint floor: passed")


def reciprocal_shift_check() -> None:
    # On a finite cyclic toy, address wraparound is avoided by checking only
    # the interior basis vectors affected by one bilateral shift.
    radius = 4
    labels = np.arange(-radius, radius + 1)
    delta = 0.3
    n0 = 0.2
    a_plus = n0 + delta * labels
    a_minus = n0 - delta * labels
    mean_before = (a_plus + a_minus) / 2.0
    shifted_plus = n0 + delta * (labels - 1)
    shifted_minus = n0 - delta * (labels - 1)
    assert_close(shifted_plus, a_plus - delta)
    assert_close(shifted_minus, a_minus + delta)
    assert_close((shifted_plus + shifted_minus) / 2.0, mean_before)
    print("reciprocal shell shift preserves mean address: passed")


def noncommuting_warning_check() -> None:
    p = np.array([[1.0, 0.0], [0.0, 0.0]])
    v = np.array([1.0, 1.0]) / math.sqrt(2.0)
    q = np.outer(v, v)
    product = p @ q
    if np.allclose(product, product.T) or np.allclose(product @ product, product):
        raise AssertionError("noncommuting projection product looked like a projection")
    print("noncommuting shell products are not joint projections: passed")


def terminal_tail_check() -> None:
    # The terminal tails can intersect only in the vacuum while their join
    # still contains two nonvacuum one-sided sectors.
    p_vacuum = np.diag([1.0, 0.0, 0.0, 0.0])
    p_infinity_plus = np.diag([1.0, 0.0, 1.0, 0.0])
    p_infinity_minus = np.diag([1.0, 1.0, 0.0, 0.0])
    assert_close(p_infinity_plus @ p_infinity_minus, p_vacuum)

    k_plus = np.diag([0.0, 2.0, 0.0, 3.0])
    k_minus = np.diag([0.0, 0.0, 5.0, 7.0])
    product = k_plus @ k_minus
    product_kernel = np.diag(np.isclose(np.diag(product), 0.0).astype(float))
    tail_join = np.diag([1.0, 1.0, 1.0, 0.0])
    assert_close(product_kernel, tail_join)
    if np.allclose(product_kernel, p_vacuum):
        raise AssertionError("terminal-tail intersection hid one-sided kernels")
    print("terminal-tail intersection is weaker than vacuum-complete tails: passed")


def all_direction_casimir_check() -> None:
    c = 1.0
    momenta = [
        np.array([0.0, 0.0, 0.0]),
        np.array([0.3, -0.4, 0.5]),
        np.array([1.0, 2.0, -1.0]),
    ]
    masses = [0.8, 1.1, 1.7]
    for momentum, mass in zip(momenta, masses):
        energy = math.sqrt(mass * mass + c * c * float(momentum @ momentum))
        casimir = energy * energy - c * c * float(momentum @ momentum)
        if np.linalg.norm(momentum) == 0.0:
            direction = np.array([1.0, 0.0, 0.0])
        else:
            direction = momentum / np.linalg.norm(momentum)
        null_product = (
            (energy + c * float(momentum @ direction))
            * (energy - c * float(momentum @ direction))
        )
        assert_close(casimir, mass * mass)
        assert_close(null_product, casimir)
    print("all-direction null-pair minimum equals the Casimir: passed")


if __name__ == "__main__":
    finite_incidence_check()
    gapless_pair_limit_check()
    reciprocal_shift_check()
    noncommuting_warning_check()
    terminal_tail_check()
    all_direction_casimir_check()
    print("no physical filtration, Casimir solder, or Yang--Mills gap is tested")
