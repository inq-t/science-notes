#!/usr/bin/env python3
"""Finite arithmetic checks for shorted-response filtration.

This receipt checks coordinate Schur complements for strictly positive matrices.
It illustrates the bounded theorems in the companion note; it is not a proof of
the infinite-dimensional shorting, Douglas, Type-III, or Yang--Mills claims.
Only the Python standard library is required.
"""

from __future__ import annotations

import math
import random


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def add(a, b):
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def sub(a, b):
    return [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def eye(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def inverse(a):
    n = len(a)
    aug = [row[:] + ident[:] for row, ident in zip(a, eye(n))]
    for col in range(n):
        pivot = max(range(col, n), key=lambda i: abs(aug[i][col]))
        if abs(aug[pivot][col]) < 1e-14:
            raise ValueError("singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for i in range(n):
            if i == col:
                continue
            factor = aug[i][col]
            aug[i] = [x - factor * y for x, y in zip(aug[i], aug[col])]
    return [row[n:] for row in aug]


def block(a, rows, cols):
    return [[a[i][j] for j in cols] for i in rows]


def schur_to_first(a, k):
    n = len(a)
    if k == n:
        return [row[:] for row in a]
    kept = list(range(k))
    hidden = list(range(k, n))
    g = block(a, kept, kept)
    b = block(a, kept, hidden)
    c = block(a, hidden, hidden)
    return sub(g, matmul(matmul(b, inverse(c)), transpose(b)))


def embed_top_left(a, n):
    out = [[0.0 for _ in range(n)] for _ in range(n)]
    for i, row in enumerate(a):
        for j, value in enumerate(row):
            out[i][j] = value
    return out


def max_abs(a):
    return max(abs(x) for row in a for x in row)


def quad(a, x):
    return sum(x[i] * a[i][j] * x[j] for i in range(len(x)) for j in range(len(x)))


def sampled_lower(a, samples=4000, seed=314159):
    rng = random.Random(seed)
    lower = math.inf
    for _ in range(samples):
        x = [rng.gauss(0.0, 1.0) for _ in a]
        norm = math.sqrt(sum(t * t for t in x))
        x = [t / norm for t in x]
        lower = min(lower, quad(a, x))
    return lower


checks = []


def check(name, condition, detail):
    checks.append(bool(condition))
    print(("PASS" if condition else "FAIL") + f"  {name}: {detail}")


m = [
    [2.0, 1.0, 0.0, 1.0],
    [0.0, 2.0, 1.0, 0.0],
    [1.0, 0.0, 2.0, 1.0],
    [0.0, 1.0, 0.0, 2.0],
]
a = matmul(transpose(m), m)
for i, shift in enumerate((0.5, 0.7, 0.9, 1.1)):
    a[i][i] += shift

# L = first two coordinates, T = first three.
s_t = schur_to_first(a, 3)
s_l_direct = schur_to_first(a, 2)
s_l_staged = schur_to_first(s_t, 2)
transitivity_error = max_abs(sub(s_l_direct, s_l_staged))
check(
    "nested shorting",
    transitivity_error < 1e-11,
    f"max |S_L(A)-S_L(S_T(A))| = {transitivity_error:.3e}",
)

# D_{T->L}=S_T-S_L, with S_L embedded in T.
d_tl = sub(s_t, embed_top_left(s_l_direct, 3))
d_lower = sampled_lower(d_tl)
check(
    "positive stage loss",
    d_lower > -1e-10,
    f"sampled min quadratic value = {d_lower:.6e}",
)

# Hard/relaxed residue and its nested identity.
g_l = block(a, [0, 1], [0, 1])
g_t = block(a, [0, 1, 2], [0, 1, 2])
r_l = sub(g_l, s_l_direct)
r_t = sub(g_t, s_t)
r_t_seen_l = block(r_t, [0, 1], [0, 1])
r_l_after_t = sub(block(s_t, [0, 1], [0, 1]), s_l_staged)
residue_error = max_abs(sub(r_l, add(r_t_seen_l, r_l_after_t)))
check(
    "nested hard/relaxed residue",
    residue_error < 1e-11,
    f"max balance error = {residue_error:.3e}",
)
check(
    "positive hard/relaxed residue",
    sampled_lower(r_l) > -1e-10 and sampled_lower(r_l_after_t) > -1e-10,
    f"sampled minima = {sampled_lower(r_l):.6e}, {sampled_lower(r_l_after_t):.6e}",
)

stage_projection_error = max_abs(sub(r_l_after_t, block(d_tl, [0, 1], [0, 1])))
check(
    "stage loss projects to added relaxation",
    stage_projection_error < 1e-11,
    f"max projection error = {stage_projection_error:.3e}",
)

# A positive frozen compression can be cancelled by one hidden adjustment.
a_cancel = [[1.0, 1.0], [1.0, 1.0]]
s_cancel = schur_to_first(a_cancel, 1)[0][0]
check(
    "hidden cancellation",
    abs(s_cancel) < 1e-12,
    f"frozen response = 1, shorted response = {s_cancel:.3e}",
)

# Finite truncations of I_E direct-sum diag(1,1/2,...,1/N).
worst_short_error = 0.0
last_global_floor = None
for n in (4, 16, 64, 256):
    diagonal = [1.0] + [1.0 / j for j in range(1, n + 1)]
    whole = [[diagonal[i] if i == j else 0.0 for j in range(n + 1)] for i in range(n + 1)]
    local_short = schur_to_first(whole, 1)[0][0]
    worst_short_error = max(worst_short_error, abs(local_short - 1.0))
    last_global_floor = min(diagonal)
check(
    "gapless-whole/gapped-quotient truncations",
    worst_short_error < 1e-12 and abs(last_global_floor - 1.0 / 256.0) < 1e-14,
    f"local floor = 1; N=256 whole floor = {last_global_floor:.6e}",
)

if not all(checks):
    raise SystemExit(1)

print(f"SUMMARY  {sum(checks)}/{len(checks)} checks passed")
