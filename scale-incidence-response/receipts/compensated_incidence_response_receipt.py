"""Finite arithmetic illustrations for compensated incidence response.

These samples test diagonal arithmetic and one kernel witness only. They do not
prove an unbounded-support theorem or independently select D=4, and they do not
construct a boundary response, entropy Hessian, Yang--Mills continuum limit,
Poincare representation, Casimir solder, or dimensional mass scale.
"""

from __future__ import annotations

import math

import numpy as np


def assert_close(left: np.ndarray | float, right: np.ndarray | float) -> None:
    if not np.allclose(left, right, rtol=1e-12, atol=1e-12):
        raise AssertionError(f"mismatch:\n{left}\n!=\n{right}")


def finite_exact_compensation_sample() -> None:
    addresses = np.arange(-8.0, 9.0)
    presentation_squared = np.exp(-2.0 * addresses)
    response = np.exp(2.0 * addresses)
    pulled_back_coefficients = response * presentation_squared
    assert_close(pulled_back_coefficients, np.ones_like(addresses))
    print("finite sample: exact cancellation on one two-sided shell window: passed")


def finite_bounded_response_trend_sample() -> None:
    floors = []
    bounded_response = 7.0
    for radius in (2, 4, 8, 16):
        addresses = np.arange(-radius, radius + 1, dtype=float)
        coefficients = bounded_response * np.exp(-2.0 * addresses)
        floors.append(float(coefficients.min()))
    if not all(left > right for left, right in zip(floors, floors[1:])):
        raise AssertionError(floors)
    if floors[-1] >= 1e-10:
        raise AssertionError(floors)
    print("finite samples: decreasing floors for R=7I on radii 2,4,8,16: passed")


def finite_dimension_character_sample() -> None:
    floors: dict[int, list[float]] = {3: [], 4: [], 5: []}
    for radius in (2, 4, 8, 16):
        addresses = np.arange(-radius, radius + 1, dtype=float)
        for spacetime_dimension in floors:
            coefficients = np.exp((spacetime_dimension - 4.0) * addresses)
            floors[spacetime_dimension].append(float(coefficients.min()))
    assert_close(np.array(floors[4]), np.ones(4))
    for spacetime_dimension in (3, 5):
        values = floors[spacetime_dimension]
        if not all(left > right for left, right in zip(values, values[1:])):
            raise AssertionError((spacetime_dimension, values))
    print("finite samples: D=3,4,5 character arithmetic under q=D-2 and p=1: passed")


def finite_terminal_kernel_witness() -> None:
    presentation = np.diag([0.0, math.exp(-2.0), math.exp(1.0)])
    response = np.diag([1e12, math.exp(4.0), math.exp(-2.0)])
    composed = np.diag(np.sqrt(np.diag(response))) @ presentation
    if not np.allclose(composed[:, 0], 0.0):
        raise AssertionError(composed)
    assert_close(composed[1:, 1:], np.eye(2))
    print("finite witness: one selected terminal kernel survives compensation: passed")


if __name__ == "__main__":
    finite_exact_compensation_sample()
    finite_bounded_response_trend_sample()
    finite_dimension_character_sample()
    finite_terminal_kernel_witness()
    print(
        "scope: no unbounded-support theorem, D=4 selection theorem, physical "
        "boundary response, entropy Hessian, Casimir solder, or Yang--Mills gap is tested"
    )
