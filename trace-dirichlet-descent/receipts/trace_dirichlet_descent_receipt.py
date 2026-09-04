#!/usr/bin/env python3
"""Finite checks and one finite no-go for trace Dirichlet descent.

The model is a weighted three-vertex graph. Vertices 0 and 1 are retained,
vertex 2 is hidden, edge (0, 1) has conductance one, and the dangling edge
(0, 2) has conductance epsilon. Eliminating vertex 2 leaves the retained
Laplacian unchanged even though the whole spectral gap tends to zero.
The final check uses a six-vertex tree to show that infimizing a classical
Dirichlet form through block conditional expectation need not preserve the
Markov contraction property.

This receipt checks finite matrix identities only. It is not a proof of the
closed-form, complete-Dirichlet, Type-III, continuum, or Yang--Mills claims.
Only the Python standard library is required.
"""

from __future__ import annotations

import math


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def sub(a, b):
    return [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def max_abs(a):
    return max(abs(x) for row in a for x in row)


def matvec(a, x):
    return [sum(v * w for v, w in zip(row, x)) for row in a]


def quad(a, x):
    return sum(x[i] * a[i][j] * x[j] for i in range(len(x)) for j in range(len(x)))


checks = []


def check(name, condition, detail):
    checks.append(bool(condition))
    print(("PASS" if condition else "FAIL") + f"  {name}: {detail}")


boundary_laplacian = [[1.0, -1.0], [-1.0, 1.0]]
worst_schur_error = 0.0
smallest_whole_gap = math.inf

for epsilon in (1.0, 0.1, 0.01, 0.001):
    whole = [
        [1.0 + epsilon, -1.0, -epsilon],
        [-1.0, 1.0, 0.0],
        [-epsilon, 0.0, epsilon],
    ]

    # C is the 1x1 hidden block. The Schur complement is exact here.
    g = [[whole[i][j] for j in (0, 1)] for i in (0, 1)]
    b = [[whole[i][2]] for i in (0, 1)]
    correction = [[b[i][0] * b[j][0] / epsilon for j in range(2)] for i in range(2)]
    short = sub(g, correction)
    worst_schur_error = max(worst_schur_error, max_abs(sub(short, boundary_laplacian)))

    # The two nonzero whole eigenvalues follow from trace and matrix-tree data.
    whole_gap = 1.0 + epsilon - math.sqrt(1.0 - epsilon + epsilon * epsilon)
    smallest_whole_gap = min(smallest_whole_gap, whole_gap)

check(
    "dangling-bulk Schur complement",
    worst_schur_error < 1e-12,
    f"max |short(A_epsilon)-L_boundary| = {worst_schur_error:.3e}",
)
check(
    "gapless-whole/gapped-trace family",
    smallest_whole_gap < 0.0016,
    f"epsilon=0.001 whole gap = {smallest_whole_gap:.6e}; trace gap = 2",
)

# TD19 with kappa=2 is the exact matrix identity
# A - 2 q^*(I-P0)q = epsilon vv^*, v=(1,0,-1).
epsilon = 0.037
whole = [
    [1.0 + epsilon, -1.0, -epsilon],
    [-1.0, 1.0, 0.0],
    [-epsilon, 0.0, epsilon],
]
lift_rhs = [
    [1.0, -1.0, 0.0],
    [-1.0, 1.0, 0.0],
    [0.0, 0.0, 0.0],
]
residue_matrix = [
    [epsilon, 0.0, -epsilon],
    [0.0, 0.0, 0.0],
    [-epsilon, 0.0, epsilon],
]
lift_identity_error = max_abs(sub(sub(whole, lift_rhs), residue_matrix))

check(
    "whole-to-local lift inequality",
    lift_identity_error < 1e-12,
    f"max |A-2q*(I-P0)q-epsilon vv*| = {lift_identity_error:.3e}",
)

# q keeps the first two coordinates; h(x0,x1)=(x0,x1,x0).
q = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]]
h = [[1.0, 0.0], [0.0, 1.0], [1.0, 0.0]]
e = matmul(h, q)
identity_3 = [[1.0 if i == j else 0.0 for j in range(3)] for i in range(3)]
vertical = sub(identity_3, e)
harmonic_form = matmul(matmul(transpose(e), whole), e)
vertical_form = matmul(matmul(transpose(vertical), whole), vertical)
pythagorean_error = max_abs(sub(sub(whole, harmonic_form), vertical_form))

check(
    "harmonic Pythagorean residue",
    pythagorean_error < 1e-12,
    f"max |A-e*Ae-(I-e)*A(I-e)| = {pythagorean_error:.3e}",
)

swap = [[0.0, 1.0], [1.0, 0.0]]
lifted_swap = matmul(matmul(h, swap), q)
corner_product = matmul(lifted_swap, lifted_swap)
hidden_image = matvec(lifted_swap, [0.0, 0.0, 1.0])

check(
    "split idempotent",
    max_abs(sub(matmul(e, e), e)) < 1e-12,
    f"max |e^2-e| = {max_abs(sub(matmul(e, e), e)):.3e}",
)
check(
    "local inverse uses the corner identity",
    max_abs(sub(corner_product, e)) < 1e-12,
    f"max |tilde(U)^2-e| = {max_abs(sub(corner_product, e)):.3e}",
)
check(
    "whole representative is noninvertible",
    max(abs(x) for x in hidden_image) < 1e-12,
    f"tilde(U)(0,0,1) = {hidden_image}",
)

# A conditional-expectation quotient of a classical Dirichlet form need not
# remain Markovian. Take the unit-conductance tree with edges
# 01, 04, 05, 12, 13 and retain the averages on blocks 01, 23, 45.
tree = [
    [3.0, -1.0, 0.0, 0.0, -1.0, -1.0],
    [-1.0, 3.0, -1.0, -1.0, 0.0, 0.0],
    [0.0, -1.0, 1.0, 0.0, 0.0, 0.0],
    [0.0, -1.0, 0.0, 1.0, 0.0, 0.0],
    [-1.0, 0.0, 0.0, 0.0, 1.0, 0.0],
    [-1.0, 0.0, 0.0, 0.0, 0.0, 1.0],
]
block_constant = [
    [1.0, 0.0, 0.0],
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0],
    [0.0, 0.0, 1.0],
]
within_block = [
    [1.0, 0.0, 0.0],
    [-1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, -1.0, 0.0],
    [0.0, 0.0, 1.0],
    [0.0, 0.0, -1.0],
]
g_block = matmul(matmul(transpose(block_constant), tree), block_constant)
b_block = matmul(matmul(transpose(block_constant), tree), within_block)
c_block_inverse = [[0.125, 0.0, 0.0], [0.0, 0.5, 0.0], [0.0, 0.0, 0.5]]
trace_form = sub(
    g_block,
    matmul(matmul(b_block, c_block_inverse), transpose(b_block)),
)
expected_trace_form = [
    [4.0, -2.0, -2.0],
    [-2.0, 1.5, 0.5],
    [-2.0, 0.5, 1.5],
]
# The pushed measure gives every block weight two, so this is the local
# generator relative to its L2 inner product.
trace_generator = [[0.5 * x for x in row] for row in trace_form]
signed = [0.0, -3.0, 1.0]
contracted = [abs(x) for x in signed]
signed_energy = quad(trace_generator, signed)
contracted_energy = quad(trace_generator, contracted)
trace_formula_error = max_abs(sub(trace_form, expected_trace_form))

check(
    "conditional-expectation trace is not automatically Markov",
    trace_formula_error < 1e-12
    and trace_generator[1][2] > 0.0
    and contracted_energy > signed_energy,
    (
        f"offdiag(1,2) = {trace_generator[1][2]:.2f}; "
        f"E(|f|) = {contracted_energy:.1f} > E(f) = {signed_energy:.1f}"
    ),
)

if not all(checks):
    raise SystemExit(1)

print(f"SUMMARY  {sum(checks)}/{len(checks)} checks passed")
