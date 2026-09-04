"""Finite checks for the bridge data-augmentation solder.

The receipt checks a reversible binary half-transfer, its middle--boundary
conditional transport, the positive data-augmentation marginal chain,
physical defect domination, product maximal-correlation tensorization, and
restriction to the parity observable of a three-link Z2 gauge cycle. It is
not evidence for an interacting Wilson continuum bound.
"""

from __future__ import annotations

import itertools

import numpy as np


TOL = 2.0e-12
COPIES = 3


def main() -> None:
    half_transfer = np.array([[0.8, 0.2], [0.2, 0.8]], dtype=float)
    stationary = np.array([0.5, 0.5], dtype=float)

    # R[y, x, z] is the stationary law of middle Y and boundary pair (X, Z).
    joint = np.empty((2, 2, 2), dtype=float)
    for middle, left, right in itertools.product(range(2), repeat=3):
        joint[middle, left, right] = (
            stationary[middle]
            * half_transfer[middle, left]
            * half_transfer[middle, right]
        )

    flat_joint = joint.reshape(2, 4)
    boundary = flat_joint.sum(axis=0)
    normalized_transport = (
        flat_joint.T
        / np.sqrt(boundary[:, None] * stationary[None, :])
    )
    singular_values = np.linalg.svd(
        normalized_transport, compute_uv=False
    )
    rho = float(singular_values[1])

    boundary_given_middle = flat_joint / stationary[:, None]
    middle_given_boundary = flat_joint / boundary[None, :]
    augmentation = boundary_given_middle @ middle_given_boundary.T
    normalized_augmentation = (
        np.sqrt(stationary)[:, None]
        * augmentation
        / np.sqrt(stationary)[None, :]
    )

    augmentation_eigenvalues = np.linalg.eigvalsh(
        normalized_augmentation
    )
    augmentation_centered = float(augmentation_eigenvalues[-2])
    bridge_floor = 1.0 - augmentation_centered
    half_transfer_centered = float(
        half_transfer[0, 0] - half_transfer[0, 1]
    )
    parity_bridge_formula = (
        (1.0 - half_transfer_centered**2)
        / (1.0 + half_transfer_centered**2)
    )
    parity_formula_error = abs(bridge_floor - parity_bridge_formula)

    physical_round_trip = half_transfer @ half_transfer
    domination_eigenvalues = np.linalg.eigvalsh(
        normalized_augmentation - physical_round_trip
    )

    product_augmentation = normalized_augmentation.copy()
    for _ in range(COPIES - 1):
        product_augmentation = np.kron(
            product_augmentation, normalized_augmentation
        )
    product_eigenvalues = np.linalg.eigvalsh(product_augmentation)
    product_centered = float(product_eigenvalues[-2])
    product_floor = 1.0 - product_centered

    local_bridge_density_ratio = float(
        np.min(middle_given_boundary / stationary[:, None])
    )
    direct_product_minorization = (
        local_bridge_density_ratio**COPIES
    )

    signs = np.array([1.0, -1.0])
    gauge_cycle = signs.copy()
    for _ in range(COPIES - 1):
        gauge_cycle = np.kron(gauge_cycle, signs)
    gauge_cycle /= np.linalg.norm(gauge_cycle)
    gauge_cycle_eigenvalue = float(
        gauge_cycle @ product_augmentation @ gauge_cycle
    )
    gauge_cycle_floor = 1.0 - gauge_cycle_eigenvalue

    row_sum_error = float(
        np.max(np.abs(augmentation.sum(axis=1) - 1.0))
    )
    detailed_balance_error = float(
        np.max(
            np.abs(
                stationary[:, None] * augmentation
                - stationary[None, :] * augmentation.T
            )
        )
    )
    square_correlation_error = abs(augmentation_centered - rho**2)
    product_tensorization_error = abs(product_centered - rho**2)
    gauge_cycle_error = abs(
        gauge_cycle_eigenvalue - augmentation_centered**COPIES
    )

    assert row_sum_error < TOL
    assert detailed_balance_error < TOL
    assert min(augmentation_eigenvalues) > -TOL
    assert square_correlation_error < TOL
    assert parity_formula_error < TOL
    assert min(domination_eigenvalues) > -TOL
    assert product_tensorization_error < TOL
    assert gauge_cycle_error < TOL
    assert direct_product_minorization < local_bridge_density_ratio
    assert gauge_cycle_floor > product_floor

    print("bridge data-augmentation solder: finite binary receipt")
    print(f"middle-boundary maximal correlation = {rho:.12f}")
    print(
        "data-augmentation centered eigenvalue = "
        f"{augmentation_centered:.12f}"
    )
    print(f"bridge lower-frame constant = {bridge_floor:.12f}")
    print(f"parity bridge-formula error = {parity_formula_error:.3e}")
    print(
        "minimum eigenvalue of S-P^2 = "
        f"{min(domination_eigenvalues):.12f}"
    )
    print(
        f"{COPIES}-factor product centered eigenvalue = "
        f"{product_centered:.12f}"
    )
    print(f"{COPIES}-factor product bridge floor = {product_floor:.12f}")
    print(
        "one-factor / direct-product minorization = "
        f"{local_bridge_density_ratio:.12f} / "
        f"{direct_product_minorization:.12f}"
    )
    print(
        f"{COPIES}-link Z2 gauge-cycle eigenvalue = "
        f"{gauge_cycle_eigenvalue:.12f}"
    )
    print(f"{COPIES}-link Z2 gauge-cycle floor = {gauge_cycle_floor:.12f}")
    print(f"row-sum error = {row_sum_error:.3e}")
    print(f"detailed-balance error = {detailed_balance_error:.3e}")
    print(f"squared-correlation error = {square_correlation_error:.3e}")
    print(f"product-tensorization error = {product_tensorization_error:.3e}")
    print(f"gauge-cycle eigenvalue error = {gauge_cycle_error:.3e}")
    print(
        "PASS: canonical bridge augmentation tensorizes without a "
        "volume-product loss"
    )


if __name__ == "__main__":
    main()
