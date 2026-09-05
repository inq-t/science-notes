"""Exact finite-state gauge-spectrum tests and compact SU(3) identities.

Stdout only. The Z2 model is a separate finite witness, not a discretization
of SU(3). Floating-point tests supplement the proofs in the canonical note.
"""

from itertools import product
from pathlib import Path
import sys
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]
                       / "rg-covariance-residue" / "receipts"))
from joint_context_escape_receipt import haar_su3


def finite_plaquette_checks():
    labels = np.arange(16)
    spins = np.array(tuple(tuple(1 if label & (1 << i) else -1
                                for i in range(4)) for label in labels))
    holonomy = np.prod(spins, axis=1)
    identity = np.eye(16)
    averages = []
    for vertex in range(4):
        # Vertex v acts on the entering and leaving links of the cycle.
        mask = (1 << vertex) | (1 << ((vertex - 1) % 4))
        permutation = identity[labels ^ mask]
        averages.append((identity + permutation) / 2)
    invariant = identity.copy()
    for average in averages:
        invariant = invariant @ average
        assert np.allclose(average @ average, average)
    assert np.isclose(np.trace(invariant), 2)
    orbit = sum(identity - average for average in averages)
    assert np.linalg.eigvalsh(orbit - 2 * (identity - invariant)).min() > -1e-12
    worst, cases = 0.0, 0
    for beta in (0.0, 0.5, 2.0, 6.0):
        probability = np.exp(beta * (holonomy - 1))
        probability /= probability.sum()
        root = np.sqrt(probability)
        t = np.tanh(beta)
        innovations = []
        for edge in range(4):
            flipped = labels ^ (1 << edge)
            total = probability + probability[flipped]
            conditional = np.zeros((16, 16))
            conditional[labels, labels] = probability / total
            conditional[labels, flipped] = np.sqrt(
                probability * probability[flipped]) / total
            assert np.allclose(conditional @ conditional, conditional)
            innovations.append(identity - conditional)
        parent = sum(innovations)
        expected = 2 - np.sqrt(1 + 3 * t * t)
        spectrum = np.linalg.eigvalsh(parent)
        assert abs(spectrum[0]) < 1e-12
        assert spectrum[1] > 0
        worst = max(worst, abs(spectrum[1] - expected))
        assert np.isclose(spectrum[1], expected, atol=1e-12)
        assert np.allclose(parent @ invariant, invariant @ parent)
        for average in averages:
            assert np.allclose(parent @ average, average @ parent)
        centered = root * (holonomy - t) / np.sqrt(1 - t * t)
        assert abs(root @ centered) < 1e-10
        assert np.isclose(centered @ centered, 1, atol=1e-10)
        assert np.allclose(parent @ centered, 4 * centered, atol=1e-10)
        for edge in range(4):
            witness = root * spins[:, edge]
            response = witness @ parent @ witness
            assert np.isclose(response, 1 - t * t, atol=1e-12)
            assert response <= 2 * (1 - t) + 1e-12
            assert np.linalg.norm(invariant @ witness) < 1e-12
        for rate in (0.25, 2.0):
            completed = parent + rate * orbit
            assert np.allclose(completed @ invariant, parent @ invariant)
            completed_gap = np.linalg.eigvalsh(completed)[1]
            prediction = min(4, 2 * rate + expected)
            assert np.isclose(completed_gap, prediction, atol=1e-12)
            cases += 1
        # Full complementary-character spectrum, not just the least mode.
        for subset in range(1, 15):
            character = np.prod(spins[:, tuple(i for i in range(4)
                                               if subset & (1 << i))], axis=1)
            complement = character * holonomy
            weight = subset.bit_count()
            assert np.allclose(parent @ (root * character),
                               weight * root * (character - t * complement))
        print("  beta", beta, "full gap", spectrum[1],
              "invariant gap", 4, "completed gap at rate 2", 4)
    return cases, worst


def compact_path_checks():
    rng = np.random.default_rng(1231)
    largest, cases = 0.0, 0
    for _ in range(32):
        u = tuple(haar_su3(rng) for _ in range(4))
        plaquette = u[0] @ u[1] @ u[2].conj().T @ u[3].conj().T
        expected = 6 * (1 - np.trace(plaquette).real / 3)
        predictors = (u[3] @ u[2] @ u[1].conj().T,
                      u[0].conj().T @ u[3] @ u[2],
                      u[3].conj().T @ u[0] @ u[1],
                      u[0] @ u[1] @ u[2].conj().T)
        for active, predictor in zip(u, predictors):
            error = abs(np.linalg.norm(active - predictor, "fro") ** 2 - expected)
            largest = max(largest, error)
            assert error < 2e-13
            cases += 1
    # Whole-link cubes have an interior gauge star exactly when n >= 3.
    for dimension in (2, 3, 4):
        for side in (2, 3, 4):
            links = set()
            for vertex in product(range(side), repeat=dimension):
                for axis in range(dimension):
                    if vertex[axis] + 1 < side:
                        links.add(vertex + (axis,))
            count = 0
            for vertex in product(range(side), repeat=dimension):
                star = {vertex + (axis,) for axis in range(dimension)}
                for axis in range(dimension):
                    before = list(vertex)
                    before[axis] -= 1
                    star.add(tuple(before) + (axis,))
                count += star.issubset(links)
            assert count == (side - 2) ** dimension
    return cases, largest


if __name__ == "__main__":
    cases, error = finite_plaquette_checks()
    print("PASS complete Z2 spectra and gauge completion cases:", cases)
    print("Largest full-spectrum edge discrepancy:", error)
    path_cases, path_error = compact_path_checks()
    print("PASS SU(3) complementary-path identities:", path_cases,
          "max discrepancy:", path_error)
    print("PASS nine whole-link-cube interior-star counts")
    print("Scope: finite identities; no SU(3) quotient gap or physical mass computed.")
