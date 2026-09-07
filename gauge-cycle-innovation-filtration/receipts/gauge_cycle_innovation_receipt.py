"""Finite checks for the gauge-cycle innovation theorem.

The graph has two vertices joined by three parallel Z2 links.  One link is a
spanning tree and the other two close the independent cycles

    z1 = x0*x1,  z2 = x0*x2.

The receipt checks gauge-equivariant coordinate expectations, the vanishing
tree innovation, the pure product-transfer girth exponent, and the abstract
innovation-matrix bound after an interacting magnetic sandwich and Perron
ground-state transform.

The appended S3 theta-graph check is a finite Haar-reset response, not a
compact-Lie diffusion.  Its matrix identities and spectral multiplicities
use exact integers and rational row reduction.  Normalized-orbit matrix
compressions and displayed eigenvalues also receive floating-point checks
with absolute tolerance 3e-12 and zero relative tolerance.  A separate
finite SU(2) label check tests, but does not prove, the stated Casimir floor.
"""

from __future__ import annotations

import itertools
from fractions import Fraction

import numpy as np


def conditional_expectation(states, probabilities, coordinates):
    """Matrix for E[f | selected coordinates] on a finite probability space."""

    n = len(states)
    out = np.zeros((n, n), dtype=float)
    groups = {}
    for i, state in enumerate(states):
        key = tuple(state[k] for k in coordinates)
        groups.setdefault(key, []).append(i)
    for i, state in enumerate(states):
        key = tuple(state[k] for k in coordinates)
        indices = groups[key]
        mass = sum(probabilities[j] for j in indices)
        for j in indices:
            out[i, j] = probabilities[j] / mass
    return out


def weighted_euclidean(operator, probabilities):
    root = np.sqrt(probabilities)
    return np.diag(root) @ operator @ np.diag(1.0 / root)


def op_norm(operator):
    return float(np.linalg.svd(operator, compute_uv=False)[0])


def exact_rank(matrix):
    """Rational Gaussian elimination, used only on 11-by-11 matrices."""

    rows = [[Fraction(int(entry)) for entry in row] for row in matrix]
    pivot_row = 0
    for column in range(len(rows[0])):
        pivot = next(
            (i for i in range(pivot_row, len(rows)) if rows[i][column]), None
        )
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        divisor = rows[pivot_row][column]
        rows[pivot_row] = [entry / divisor for entry in rows[pivot_row]]
        for i in range(pivot_row + 1, len(rows)):
            factor = rows[i][column]
            if factor:
                rows[i] = [
                    entry - factor * pivot_entry
                    for entry, pivot_entry in zip(rows[i], rows[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def theta_response_checks():
    """Check two tree charts of the complete neutral S3 theta carrier."""

    permutations = list(itertools.permutations(range(3)))
    group_index = {element: i for i, element in enumerate(permutations)}
    order = len(permutations)
    multiplication = np.array(
        [
            [group_index[tuple(p[q[k]] for k in range(3))] for q in permutations]
            for p in permutations
        ],
        dtype=np.int64,
    )
    inverse = [next(j for j in range(order) if multiplication[i, j] == 0)
               for i in range(order)]
    signs = np.array(
        [(-1) ** sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
         for p in permutations],
        dtype=np.int64,
    )

    pair_states = list(itertools.product(range(order), repeat=2))
    raw_states = list(itertools.product(range(order), repeat=3))
    pair_index = {state: i for i, state in enumerate(pair_states)}
    raw_index = {state: i for i, state in enumerate(raw_states)}

    def reset_counts(states, index, coordinate):
        # Each row sums to |G|; divide by |G| for the Haar expectation.
        counts = np.zeros((len(states), len(states)), dtype=np.int64)
        for i, state in enumerate(states):
            for h in range(order):
                target = list(state)
                target[coordinate] = h
                counts[i, index[tuple(target)]] += 1
        return counts

    ex = reset_counts(pair_states, pair_index, 0)
    ey = reset_counts(pair_states, pair_index, 1)
    diagonal = np.zeros_like(ex)
    for i, (x, y) in enumerate(pair_states):
        for h in range(order):
            diagonal[i, pair_index[(multiplication[x, h], multiplication[y, h])]] += 1
    pair_identity = np.eye(len(pair_states), dtype=np.int64)
    raw_identity = np.eye(len(raw_states), dtype=np.int64)
    alpha_a, alpha_b, alpha_c = 1, 2, 4
    # All response matrices with suffix _six are exactly 6 times L.
    raw_six = sum(
        alpha * (order * raw_identity - reset_counts(raw_states, raw_index, edge))
        for edge, alpha in enumerate((alpha_a, alpha_b, alpha_c))
    )
    tree_a_six = (
        alpha_b * (order * pair_identity - ex)
        + alpha_c * (order * pair_identity - ey)
        + alpha_a * (order * pair_identity - diagonal)
    )
    tree_b_six = (
        alpha_a * (order * pair_identity - ex)
        + alpha_c * (order * pair_identity - ey)
        + alpha_b * (order * pair_identity - diagonal)
    )

    # Tree a: x=b*a^-1, y=c*a^-1.  This first removes one vertex frame.
    pullback = np.zeros((len(raw_states), len(pair_states)), dtype=np.int64)
    for i, (a, b, c) in enumerate(raw_states):
        pullback[i, pair_index[(multiplication[b, inverse[a]],
                               multiplication[c, inverse[a]])]] = 1
    assert np.array_equal(pullback.T @ pullback, order * pair_identity)
    assert np.array_equal(raw_six @ pullback, pullback @ tree_a_six)

    # The remaining vertex acts by simultaneous conjugation on (x,y).
    orbit_labels = {}
    representatives = []
    state_orbit = []
    for x, y in pair_states:
        orbit = [
            (multiplication[multiplication[h, x], inverse[h]],
             multiplication[multiplication[h, y], inverse[h]])
            for h in range(order)
        ]
        label = min(orbit)
        if label not in orbit_labels:
            orbit_labels[label] = len(orbit_labels)
            representatives.append(pair_index[label])
        state_orbit.append(orbit_labels[label])
    dimension = len(orbit_labels)
    assert dimension == 11
    indicators = np.zeros((len(pair_states), dimension), dtype=np.int64)
    indicators[np.arange(len(pair_states)), state_orbit] = 1
    orbit_sizes = indicators.sum(axis=0)

    # Independently construct the two-vertex gauge projector on all 216 states.
    gauge_counts = np.zeros_like(raw_six)
    for i, state in enumerate(raw_states):
        for left, right in itertools.product(range(order), repeat=2):
            target = tuple(
                multiplication[multiplication[left, g], inverse[right]] for g in state
            )
            gauge_counts[i, raw_index[target]] += 1
    assert np.array_equal(gauge_counts, gauge_counts.T)
    assert np.array_equal(gauge_counts @ gauge_counts, order**2 * gauge_counts)
    assert np.trace(gauge_counts) == order**2 * dimension
    assert np.array_equal(gauge_counts @ raw_six, raw_six @ gauge_counts)
    raw_indicators = pullback @ indicators
    assert np.array_equal(gauge_counts @ raw_indicators, order**2 * raw_indicators)
    assert np.array_equal(raw_indicators.sum(axis=0), order * orbit_sizes)

    # Integer indicator coordinates certify the complete invariant restriction.
    invariant_a_six = tree_a_six[representatives, :] @ indicators
    invariant_b_six = tree_b_six[representatives, :] @ indicators
    assert np.array_equal(tree_a_six @ indicators, indicators @ invariant_a_six)
    assert np.array_equal(tree_b_six @ indicators, indicators @ invariant_b_six)

    # Tree b: u=a*b^-1=x^-1, v=c*b^-1=y*x^-1.
    change = np.zeros_like(ex)
    for i, (x, y) in enumerate(pair_states):
        change[i, pair_index[(inverse[x], multiplication[y, inverse[x]])]] = 1
    assert np.array_equal(change.T @ change, pair_identity)
    assert np.array_equal(tree_a_six @ change, change @ tree_b_six)
    invariant_change = change[representatives, :] @ indicators
    assert np.array_equal(change @ indicators, indicators @ invariant_change)
    assert np.array_equal(invariant_a_six @ invariant_change,
                          invariant_change @ invariant_b_six)
    assert np.array_equal(invariant_change.T @ invariant_change,
                          np.eye(dimension, dtype=np.int64))

    # Exact nullities exhaust this 11-dimensional carrier, hence certify spectrum.
    spectral_multiplicities = {0: 1, 3: 2, 5: 2, 6: 2, 7: 4}
    invariant_identity = np.eye(dimension, dtype=np.int64)
    for eigenvalue, multiplicity in spectral_multiplicities.items():
        for matrix in (invariant_a_six, invariant_b_six):
            assert dimension - exact_rank(matrix - order * eigenvalue * invariant_identity) == multiplicity
    assert sum(spectral_multiplicities.values()) == dimension

    # These normalized indicator bases use counting-space coordinates; the common
    # uniform Haar factors are absorbed into the equivalent Euclidean carriers.
    pair_basis = indicators / np.sqrt(orbit_sizes)[None, :]
    raw_basis = raw_indicators / np.sqrt(order * orbit_sizes)[None, :]
    normalized_a = pair_basis.T @ (tree_a_six / order) @ pair_basis
    normalized_b = pair_basis.T @ (tree_b_six / order) @ pair_basis
    normalized_raw = raw_basis.T @ (raw_six / order) @ raw_basis
    tolerance = 3e-12
    assert np.allclose(normalized_raw, normalized_a, rtol=0, atol=tolerance)
    assert np.allclose(normalized_a, normalized_a.T, rtol=0, atol=tolerance)
    expected_spectrum = np.array(
        [value for value, multiplicity in spectral_multiplicities.items()
         for _ in range(multiplicity)]
    )
    for matrix in (normalized_a, normalized_b):
        assert np.allclose(np.linalg.eigvalsh(matrix), expected_spectrum,
                           rtol=0, atol=tolerance)

    # Resetting independent cycle coordinates equally in each chart is not the
    # same response.  The class function sign(v) has rate 1 before pullback but
    # sign(y*x^-1)=sign(y)*sign(x) has rate 2 after pullback.
    naive_six = 2 * order * pair_identity - ex - ey
    sign_v = np.array([signs[y] for _, y in pair_states], dtype=np.int64)
    pulled_sign_v = change @ sign_v
    assert np.array_equal(naive_six @ sign_v, order * sign_v)
    assert np.array_equal(naive_six @ pulled_sign_v, 2 * order * pulled_sign_v)
    assert not np.array_equal(naive_six @ change @ indicators,
                              change @ naive_six @ indicators)

    print("S3 theta Haar-reset response: PASS (not Lie diffusion)")
    print(f"S3 theta raw/neutral dimensions = {len(raw_states)}/{dimension}")
    print("S3 theta weights (a,b,c) = (1,2,4); exact gauge and tree intertwinings: PASS")
    print(f"S3 theta exact eigenvalue:multiplicity = {spectral_multiplicities}")
    print("naive independent cycle resets: sign(v) rate 1 becomes rate 2 (exact failure)")
    print(f"normalized full-carrier compression/eigenvalue checks: atol={tolerance:g}, rtol=0")

    # Independent Lie-theory check: j_e=n_e/2 and C_2(j)=j(j+1).
    # Trivalent SU(2) labels have integral sum and satisfy the triangle bounds.
    # This finite enumeration is not a proof for all labels or a continuum gap.
    maximum_twice_spin = 12
    nonvacuum_energies_four = []
    for labels in itertools.product(range(maximum_twice_spin + 1), repeat=3):
        if sum(labels) % 2 or 2 * max(labels) > sum(labels) or not any(labels):
            continue
        energy_four = sum(
            alpha * n * (n + 2) for alpha, n in zip((alpha_a, alpha_b, alpha_c), labels)
        )
        nonvacuum_energies_four.append(energy_four)
    floor_four = 3 * min(alpha_a + alpha_b, alpha_a + alpha_c, alpha_b + alpha_c)
    assert min(nonvacuum_energies_four) == floor_four
    print(f"SU2 Casimir normalization C2(j)=j(j+1): theta floor = {Fraction(floor_four, 4)}")
    print(f"SU2 admissible nonvacuum labels checked = {len(nonvacuum_energies_four)}, 2j <= {maximum_twice_spin}; finite check only")


def main():
    z_states = list(itertools.product((-1, 1), repeat=2))
    z_index = {state: i for i, state in enumerate(z_states)}

    link_correlation = 0.62
    cycle_correlation = link_correlation**2

    kinetic = np.zeros((4, 4), dtype=float)
    for i, z in enumerate(z_states):
        for j, zp in enumerate(z_states):
            eta1 = z[0] * zp[0]
            eta2 = z[1] * zp[1]
            kinetic[i, j] = 0.25 * (
                1.0
                + cycle_correlation * eta1
                + cycle_correlation * eta2
                + cycle_correlation * eta1 * eta2
            )

    assert np.allclose(kinetic.sum(axis=1), 1.0)
    assert np.allclose(np.linalg.eigvalsh(kinetic), [cycle_correlation] * 3 + [1.0])

    beta = 0.37
    coupling = 0.55
    magnetic = np.array(
        [
            np.exp(
                0.5
                * beta
                * (z1 + 0.8 * z2 + coupling * z1 * z2)
            )
            for z1, z2 in z_states
        ]
    )
    transfer = np.diag(magnetic) @ kinetic @ np.diag(magnetic)
    eigenvalues, eigenvectors = np.linalg.eigh(transfer)
    lambda0 = float(eigenvalues[-1])
    psi = eigenvectors[:, -1]
    if psi.sum() < 0:
        psi = -psi
    assert np.all(psi > 0)

    stationary = psi**2
    stationary /= stationary.sum()
    doob = transfer * psi[np.newaxis, :] / (lambda0 * psi[:, np.newaxis])
    assert np.allclose(doob.sum(axis=1), 1.0)
    assert np.allclose(stationary[:, None] * doob, stationary[None, :] * doob.T)

    e0 = np.tile(stationary, (4, 1))
    e1 = conditional_expectation(z_states, stationary, (0,))
    identity = np.eye(4)
    d1 = e1 - e0
    d2 = identity - e1

    symmetric_doob = weighted_euclidean(doob, stationary)
    d1e = weighted_euclidean(d1, stationary)
    d2e = weighted_euclidean(d2, stationary)
    e0e = weighted_euclidean(e0, stationary)
    centered = identity - e0e

    assert np.allclose(symmetric_doob, symmetric_doob.T)
    assert np.allclose(d1e @ d2e, 0.0, atol=1e-12)
    assert np.allclose(d1e + d2e, centered)

    blocks = (d1e, d2e)
    innovation = np.array(
        [
            [op_norm(left @ symmetric_doob @ right) for right in blocks]
            for left in blocks
        ]
    )
    rho = op_norm(centered @ symmetric_doob @ centered)
    innovation_bound = op_norm(innovation)
    assert rho <= innovation_bound + 1e-12
    assert innovation_bound < 1.0

    raw_states = list(itertools.product((-1, 1), repeat=3))
    raw_probabilities = np.array(
        [stationary[z_index[(x0 * x1, x0 * x2)]] / 2.0 for x0, x1, x2 in raw_states]
    )
    raw_index = {state: i for i, state in enumerate(raw_states)}
    gauge = np.zeros((8, 8), dtype=float)
    for i, state in enumerate(raw_states):
        gauge[i, i] += 0.5
        gauge[i, raw_index[tuple(-x for x in state)]] += 0.5

    prefix_sets = ((), (0,), (0, 1), (0, 1, 2))
    prefix_expectations = [
        conditional_expectation(raw_states, raw_probabilities, coordinates)
        for coordinates in prefix_sets
    ]
    gauge_e = weighted_euclidean(gauge, raw_probabilities)
    physical_ranks = []
    for expectation in prefix_expectations:
        expectation_e = weighted_euclidean(expectation, raw_probabilities)
        assert np.allclose(expectation_e @ gauge_e, gauge_e @ expectation_e)
        physical_ranks.append(
            int(np.linalg.matrix_rank(gauge_e @ expectation_e @ gauge_e, tol=1e-10))
        )

    assert physical_ranks == [1, 1, 2, 4]

    print("gauge-cycle innovation receipt: PASS")
    print(f"tree/prefix physical ranks = {physical_ranks}")
    print(f"link correlation = {link_correlation:.9f}")
    print(f"pure physical contraction = r^2 = {cycle_correlation:.9f}")
    print(f"interacting physical rho = {rho:.9f}")
    print("interacting innovation matrix =")
    print(np.array2string(innovation, precision=9, suppress_small=False))
    print(f"innovation-matrix norm = {innovation_bound:.9f}")


if __name__ == "__main__":
    main()
    theta_response_checks()
