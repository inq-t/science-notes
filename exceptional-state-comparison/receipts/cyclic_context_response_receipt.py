"""Finite cyclic-context and regular-response checks on the Albert algebra.

The exact shared coordinates define a chosen order-three automorphism and
its rank-nine fixed context. Numerical checks cover covariance, Jordan
variance, matrix-state entropy curvature, and an invisible matrix direction.
Haar irreducibility is an analytic input, not a finite averaging result.
No files are written and no physical mass gap is tested.
"""

from __future__ import annotations

import math

import numpy as np

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

# Resolve the shared arithmetic from this receipt, independently of the cwd.
_coordinates_path = Path(__file__).resolve().parents[2] / "albert-algebra" / "coordinates.py"
_coordinates_spec = spec_from_file_location("albert_coordinates", _coordinates_path)
if _coordinates_spec is None or _coordinates_spec.loader is None:
    raise ImportError(f"Cannot load Albert coordinates from {_coordinates_path}")
jordan = module_from_spec(_coordinates_spec)
_coordinates_spec.loader.exec_module(jordan)

# One declared complex slice C = span(1, e1), not an intrinsic context choice.
B_INDICES = [0, 1, 2] + [3 + 8 * pair + component for pair in range(3) for component in (0, 1)]


def check_close(label, actual, expected, atol=2e-10):
    error = float(np.max(np.abs(np.asarray(actual) - np.asarray(expected))))
    if error > atol:
        raise AssertionError(f"{label}: error {error:.6g} exceeds {atol}")
    return error


def main():
    # Convert the integer-coordinate multiplication tensor to a trace-ON basis.
    scales = np.array([1.0] * 3 + [math.sqrt(2.0)] * 24)
    product = np.zeros((27, 27, 27))
    for i, left in enumerate(jordan.FULL_BASIS):
        for j, right in enumerate(jordan.FULL_BASIS):
            value = np.array(jordan.jordan_product_twice(left, right)) / 2
            product[:, i, j] = value * scales / (scales[i] * scales[j])

    def multiply(x, y):
        return np.einsum("aij,i,j->a", product, x, y)

    def regular(x):
        return np.einsum("aij,i->aj", product, x)

    unit = np.array([1.0] * 3 + [0.0] * 24)
    identity = np.eye(27)
    p_unit = np.outer(unit, unit) / 3
    keep = np.zeros(27)
    keep[B_INDICES] = 1
    expectation = np.diag(keep)
    loss = identity - expectation

    # Entrywise G2 automorphism: fix C=span(1,e1), rotate C-perp by 120 deg.
    w = np.eye(27)
    for block in range(3):
        start = 3 + 8 * block
        for j in range(2, 8):
            w[start + j, start + j] = -0.5
            sign, output = jordan.OCTONION_TABLE[1][j]
            w[start + output, start + j] += math.sqrt(3) * sign / 2
    check_close("w cubed", w @ w @ w, identity)
    check_close("orthogonal w", w.T @ w, identity)
    check_close("cyclic expectation", (identity + w + w @ w) / 3, expectation)
    check_close("regular covariance on all basis vectors",
                np.stack([w @ regular(e) @ w.T for e in identity]),
                np.stack([regular(w @ e) for e in identity]))
    check_close("Jordan unit", regular(unit), identity)

    def twirl(t):
        w2 = w @ w
        return (t + w @ t @ w.T + w2 @ t @ w2.T) / 3

    rng = np.random.default_rng(104)
    max_variance_error = 0.0
    max_entropy_error = 0.0
    for _ in range(12):
        x = rng.normal(size=27)
        x -= p_unit @ x
        x /= np.linalg.norm(x)
        b, y = expectation @ x, loss @ x
        residue = expectation @ multiply(x, x) - multiply(b, b)
        max_variance_error = max(max_variance_error, check_close(
            "Jordan variance", residue, expectation @ multiply(y, y)))
        check_close("trace residue", np.dot(unit, residue), np.dot(y, y))
        if np.linalg.eigvalsh(regular(residue)).min() < -2e-10:
            raise AssertionError("Jordan residue not positive")
        lx = regular(x)
        check_close("regular trace", np.trace(lx), 0)
        check_close("regular square trace", np.trace(lx @ lx), 3)
        check_close("CP intertwiner", twirl(lx), regular(b))

        def relative_to_uniform(t, eps):
            # Stable expansion of (1+z)log(1+z)-z, with exact linear cancellation.
            z = eps * np.linalg.eigvalsh(t)
            if np.min(1 + z) <= 0:
                raise AssertionError("state not faithful")
            return np.sum((1 + z) * np.log1p(z) - z) / 27

        eps = 0.002
        even_loss = sum(
            relative_to_uniform(lx, sign * eps)
            - relative_to_uniform(twirl(lx), sign * eps)
            for sign in (-1, 1)
        ) / (2 * eps * eps)
        max_entropy_error = max(max_entropy_error, check_close(
            "entropy Taylor coefficient", even_loss, np.dot(y, y) / 18, 1e-8))

    # Whole matrix carrier retains a nonzero traceless balance direction.
    balance = 27 * p_unit - identity
    check_close("balance trace", np.trace(balance), 0)
    check_close("balance fixed", twirl(balance), balance)
    check_close("frame rank ratio", np.trace(loss) / 26, 9 / 13)
    print(f"PASS Albert/CP identities; max variance error {max_variance_error:.3g}")
    print(f"PASS entropy half-Hessian; max coefficient error {max_entropy_error:.3g}")
    print("PASS explicit full-matrix invisible balance direction")
    print("SCOPE Haar-frame theorem uses cited irreducibility, not numerical averaging")


if __name__ == "__main__":
    main()
