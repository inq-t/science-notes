"""Finite tests of same-law conditional projections and patch overlap.

Stdout only. Integer geometry is exact. Matrix checks use floating point on
a finite Ising carrier, not an approximation of the SU(3) patch spectrum.
"""

from collections import Counter
from itertools import product
import numpy as np


def shifted(vertex, axis, amount=1):
    result = list(vertex)
    result[axis] += amount
    return tuple(result)


def cube_overlap_checks():
    cases = 0
    for dimension in (2, 3, 4):
        origin = (0,) * dimension
        active = origin + (0,)
        neighbors = set()
        for axis in range(1, dimension):
            for base in (origin, shifted(origin, axis, -1)):
                plaquette = (base + (0,), shifted(base, 0) + (axis,),
                             shifted(base, axis) + (0,), base + (axis,))
                neighbors.update(plaquette)
        neighbors.remove(active)
        assert len(neighbors) == 6 * (dimension - 1)
        for side in (2, 3, 4):
            ranges = (range(2 - side, 1),) + (range(1 - side, 1),) * (dimension - 1)
            counts = Counter()
            for anchor in product(*ranges):
                for local in product(range(side), repeat=dimension):
                    vertex = tuple(a + b for a, b in zip(anchor, local))
                    for axis in range(dimension):
                        if local[axis] < side - 1:
                            counts[vertex + (axis,)] += 1
            coverage = (side - 1) * side ** (dimension - 1)
            pair_overlap = (side - 1) ** 2 * side ** (dimension - 2)
            assert counts[active] == coverage
            assert all(counts[edge] == pair_overlap for edge in neighbors)
            assert all(count <= pair_overlap
                       for edge, count in counts.items() if edge != active)
            assert coverage * (side - 1) == pair_overlap * side
            cases += 1
    return cases


def conditional_projections(size, coupling):
    labels = np.arange(2 ** size)
    spins = np.array(tuple(tuple(1 if (label >> axis) & 1 else -1
                                for axis in range(size)) for label in labels))
    logarithm = coupling * np.sum(spins * np.roll(spins, -1, axis=1), axis=1)
    probability = np.exp(logarithm - logarithm.max())
    probability /= probability.sum()
    identity = np.eye(len(labels))
    innovations = []
    for axis in range(size):
        flipped = labels ^ (1 << axis)
        total = probability + probability[flipped]
        # Unitary density conjugation of the actual conditional expectation.
        projection = np.zeros_like(identity)
        projection[labels, labels] = probability / total
        projection[labels, flipped] = np.sqrt(probability * probability[flipped]) / total
        assert np.allclose(projection, projection.T, atol=1e-13)
        assert np.allclose(projection @ projection, projection, atol=1e-13)
        innovations.append(identity - projection)
    vacuum = np.sqrt(probability)
    assert all(np.linalg.norm(q @ vacuum) < 1e-13 for q in innovations)
    return innovations


def positive_edge(matrix, expected_kernel=None):
    spectrum = np.linalg.eigvalsh(matrix)
    assert spectrum.min() > -2e-12
    zero = abs(spectrum) < 2e-10
    if expected_kernel is not None:
        assert np.count_nonzero(zero) == expected_kernel
    return spectrum[~zero].min()


def same_law_matrix_checks():
    size, cases, worst = 7, 0, 0.0
    for coupling in (0.0, 0.2, 0.6):
        innovations = conditional_projections(size, coupling)
        parent = sum(innovations)
        parent_gap = positive_edge(parent, expected_kernel=1)
        for i in range(size):
            for j in range(i + 1, size):
                commutator = innovations[i] @ innovations[j] - innovations[j] @ innovations[i]
                if (j - i) not in (1, size - 1):
                    assert np.linalg.norm(commutator) < 1e-12
        for side in (2, 3):
            patches = tuple(sum(innovations[(start + offset) % size]
                                for offset in range(side)) for start in range(size))
            patch_gap = min(positive_edge(patch, expected_kernel=2 ** (size - side))
                            for patch in patches)
            squares = sum(patch @ patch for patch in patches)
            # The cyclic weighted-patch identity has rho=n, kappa=n-1.
            upper_defect = (side - 1) * (parent @ parent) + parent - squares
            lower_defect = squares - side * patch_gap * parent
            worst = min(worst, np.linalg.eigvalsh(upper_defect).min(),
                        np.linalg.eigvalsh(lower_defect).min())
            assert worst > -2e-11
            bound = (side * patch_gap - 1) / (side - 1)
            assert parent_gap >= bound - 2e-11
            if coupling == 0:
                assert np.isclose(parent_gap, 1)
                assert np.isclose(patch_gap, 1)
                assert np.isclose(bound, 1)
            print("  coupling", coupling, "patch size", side,
                  "conditional patch gap", patch_gap,
                  "global gap", parent_gap, "bound", bound)
            cases += 1
    return cases, worst


if __name__ == "__main__":
    print("PASS endpoint-contained cube overlap cases:", cube_overlap_checks())
    cases, worst = same_law_matrix_checks()
    print("PASS actual-law conditional projection matrix cases:", cases)
    print("Smallest tested positive-order defect eigenvalue:", worst)
    print("Scope: finite algebra checks; no SU(3) patch gap or physical mass derived.")
