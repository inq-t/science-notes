"""Finite checks of cut-flux identities, not proofs of smooth duality."""

import itertools
import numpy as np


def close(actual, expected, tolerance=1e-10):
    assert np.max(np.abs(np.asarray(actual) - expected)) < tolerance


def circle_checks():
    theta = 2 * np.pi * np.arange(2048) / 2048
    for k in (0.0, 0.2, 1.0, 3.0, 8.0, 20.0):
        density = np.exp(k * np.cos(theta)) / np.i0(k)
        velocity = 1 - np.exp(-k * np.cos(theta)) / np.cosh(k)
        bound = np.tanh(k)
        close(np.max(np.abs(velocity)), bound)
        # Exact periodic flux has derivative b'; the added flux is constant.
        flux_shift = density * (velocity - 1)
        close(flux_shift, -1 / (np.i0(k) * np.cosh(k)))
        lower = np.max(-bound * density - density)
        upper = np.min(bound * density - density)
        close(lower, upper)
        cost_min_velocity = 1 - np.exp(-k * np.cos(theta)) / np.i0(k)
        close(np.mean(density * cost_min_velocity**2), 1 - np.i0(k) ** -2)
        print(
            f"circle K={k:4.1f}: optimal max={bound:.9f}, "
            f"least-L2 max={np.max(np.abs(cost_min_velocity)):.9f}"
        )


def weighted_interval_checks():
    rng = np.random.default_rng(127)
    for _ in range(30):
        density = np.exp(rng.uniform(-2, 2, 17))
        primitive = rng.normal(size=17)
        denominator = density[:, None] + density[None, :]
        quotient = np.abs(primitive[:, None] - primitive[None, :]) / denominator
        bound = np.max(quotient)
        lower = np.max(-bound * density - primitive)
        upper = np.min(bound * density - primitive)
        assert lower <= upper + 1e-12
        shift = (lower + upper) / 2
        close(np.max(np.abs(primitive + shift) / density), bound)
        too_small = bound * (1 - 1e-5)
        assert np.max(-too_small * density - primitive) > np.min(
            too_small * density - primitive
        )
    print("30 weighted circle-sample interval minimax checks passed")


def joint_cycle_check():
    # Node demands sum to zero. Edges are 1->2, 2->3, 3->1.
    a = np.array((1.0, 0.0))
    b = np.array((-0.5, np.sqrt(3) / 2))
    c = -a - b
    demands = np.array((a, b, c))
    offsets = np.array((np.zeros(2), b, -a))
    shift = -np.mean(offsets, axis=0)
    flows = offsets + shift
    close(flows - np.roll(flows, 1, axis=0), demands)
    joint = 1 / np.sqrt(3)
    close(np.linalg.norm(flows, axis=1), joint)
    # Every nontrivial cut has two unit-capacity boundary edges.
    cuts = []
    for bits in itertools.product((False, True), repeat=3):
        if not any(bits) or all(bits):
            continue
        demand = demands[np.asarray(bits)].sum(axis=0)
        capacity = sum(bits[i] != bits[(i + 1) % 3] for i in range(3))
        cuts.append(np.linalg.norm(demand) / capacity)
    close(cuts, 0.5)
    # Vector dual test attains the joint optimum.
    potentials = demands
    numerator = np.sum(demands * potentials)
    denominator = np.linalg.norm(
        potentials - np.roll(potentials, -1, axis=0), axis=1
    ).sum()
    close(numerator / denominator, joint)
    assert joint > max(cuts)
    print(f"three-cycle: scalar cuts=0.5 < joint={joint:.12f}; dual attained")


if __name__ == "__main__":
    circle_checks()
    weighted_interval_checks()
    joint_cycle_check()
    print("PASS: finite algebraic receipts only; no continuum-gap conclusion")
