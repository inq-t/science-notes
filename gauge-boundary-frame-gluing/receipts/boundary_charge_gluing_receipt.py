"""Finite receipt for dual boundary-charge gluing.

Two Z2 link variables x_A and x_B share an effective boundary gauge action
(x_A, x_B) -> (-x_A, -x_B).  Each regional link carrier decomposes into the
trivial basis vector 1 and the charged basis vector x.  The diagonal global
invariants contain 1 tensor 1 and x tensor x, while independently averaging
each region keeps only 1 tensor 1.
"""

from __future__ import annotations

import itertools

import numpy as np


def main() -> None:
    states = list(itertools.product((-1, 1), repeat=2))
    index = {state: i for i, state in enumerate(states)}

    identity = np.eye(4)
    diagonal_flip = np.zeros((4, 4))
    flip_a = np.zeros((4, 4))
    flip_b = np.zeros((4, 4))

    for i, (x_a, x_b) in enumerate(states):
        diagonal_flip[index[(-x_a, -x_b)], i] = 1.0
        flip_a[index[(-x_a, x_b)], i] = 1.0
        flip_b[index[(x_a, -x_b)], i] = 1.0

    global_gauss = 0.5 * (identity + diagonal_flip)
    close_a = 0.5 * (identity + flip_a)
    close_b = 0.5 * (identity + flip_b)
    separately_closed = close_a @ close_b

    one_one = np.ones(4) / 2.0
    charged_pair = np.array([x_a * x_b for x_a, x_b in states]) / 2.0

    assert np.allclose(global_gauss @ global_gauss, global_gauss)
    assert np.allclose(separately_closed @ separately_closed, separately_closed)
    assert np.linalg.matrix_rank(global_gauss) == 2
    assert np.linalg.matrix_rank(separately_closed) == 1
    assert np.allclose(global_gauss @ one_one, one_one)
    assert np.allclose(global_gauss @ charged_pair, charged_pair)
    assert np.allclose(separately_closed @ one_one, one_one)
    assert np.allclose(separately_closed @ charged_pair, 0.0)
    assert np.allclose(global_gauss @ separately_closed, separately_closed)

    print("boundary charge gluing receipt: PASS")
    print(f"extended regional dimensions = 2 x 2")
    print(f"diagonally glued physical dimension = {np.linalg.matrix_rank(global_gauss)}")
    print(f"separately closed dimension = {np.linalg.matrix_rank(separately_closed)}")
    print("retained global sectors = trivial-trivial, charged-charged")
    print("premature regional closure erases = charged-charged")


if __name__ == "__main__":
    main()
