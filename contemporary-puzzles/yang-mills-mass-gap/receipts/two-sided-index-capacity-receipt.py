"""Finite checks for the two-sided index-capacity/cosmic-weld note.

This receipt checks only finite-dimensional relative-entropy arithmetic and the
conditional ladder formulas. It does not test the Type-III theorem or any
physical Yang--Mills identification.
"""

from __future__ import annotations

import math

import numpy as np


TOL = 5.0e-12


def relative_entropy(rho: np.ndarray, sigma: np.ndarray) -> float:
    """Return Tr rho(log rho-log sigma) when supp(rho) is in supp(sigma)."""

    rho_values, rho_vectors = np.linalg.eigh(rho)
    sigma_values, sigma_vectors = np.linalg.eigh(sigma)
    positive_sigma = sigma_values > TOL
    null_vectors = sigma_vectors[:, ~positive_sigma]
    if null_vectors.size:
        outside_weight = float(np.trace(null_vectors.conj().T @ rho @ null_vectors).real)
        if outside_weight > TOL:
            return math.inf

    rho_log_rho = sum(
        value * math.log(value) for value in rho_values if value > TOL
    )
    supported_vectors = sigma_vectors[:, positive_sigma]
    log_sigma = (
        supported_vectors
        @ np.diag(np.log(sigma_values[positive_sigma]))
        @ supported_vectors.conj().T
    )
    rho_log_sigma = float(np.trace(rho @ log_sigma).real)
    return float(rho_log_rho - rho_log_sigma)


def pure_basis_state(dimension: int) -> np.ndarray:
    vector = np.zeros(dimension, dtype=complex)
    vector[0] = 1.0
    return np.outer(vector, vector.conj())


def maximally_entangled_state(dimension: int) -> np.ndarray:
    vector = np.zeros(dimension * dimension, dtype=complex)
    for index in range(dimension):
        vector[index * dimension + index] = 1.0 / math.sqrt(dimension)
    return np.outer(vector, vector.conj())


def rectangular_maximally_entangled_state(retained: int, edge: int) -> np.ndarray:
    rank = min(retained, edge)
    vector = np.zeros(retained * edge, dtype=complex)
    for index in range(rank):
        vector[index * edge + index] = 1.0 / math.sqrt(rank)
    return np.outer(vector, vector.conj())


def partial_trace_edge(rho: np.ndarray, retained: int, edge: int) -> np.ndarray:
    tensor = rho.reshape(retained, edge, retained, edge)
    return np.einsum("ibjb->ij", tensor)


def check_close(name: str, actual: float, expected: float) -> None:
    error = abs(actual - expected)
    if not math.isclose(actual, expected, rel_tol=1.0e-12, abs_tol=TOL):
        raise AssertionError(f"{name}: {actual} != {expected}; error={error}")
    print(f"PASS {name}: actual={actual:.12g}, expected={expected:.12g}")


def main() -> None:
    for dimension in (2, 3, 5):
        tau = np.eye(dimension) / dimension
        one_side = relative_entropy(pure_basis_state(dimension), tau)
        check_close(
            f"one-sided pure loss d={dimension}",
            one_side,
            math.log(dimension),
        )
        check_close(
            f"half categorical log-index d={dimension}",
            one_side,
            0.5 * math.log(dimension**2),
        )

        phi = maximally_entangled_state(dimension)
        tau_pair = np.eye(dimension**2) / dimension**2
        amplified = relative_entropy(phi, tau_pair)
        check_close(
            f"amplified full log-index d={dimension}",
            amplified,
            math.log(dimension**2),
        )

    edge = 4
    tau_edge = np.eye(edge) / edge
    for retained in (1, 2, 4, 8):
        state = rectangular_maximally_entangled_state(retained, edge)
        retained_state = partial_trace_edge(state, retained, edge)
        coarse_state = np.kron(retained_state, tau_edge)
        loss = relative_entropy(state, coarse_state)
        check_close(
            f"carrier-dependent capacity n={retained}, d={edge}",
            loss,
            math.log(edge * min(retained, edge)),
        )

    dimension = 3.0
    log_index_cell = 2.0 * math.log(dimension)
    base_iota = 100.0
    for rung in range(6):
        capacity = rung * log_index_cell
        iota_ratio = math.exp(capacity)
        hubble_ratio = math.exp(-0.5 * capacity)
        count_ratio = math.exp(capacity / 3.0)
        energy_ratio = hubble_ratio * count_ratio

        check_close(
            f"declared scalar fusion arithmetic n={rung}",
            capacity,
            2.0 * rung * math.log(dimension),
        )
        check_close(
            f"horizon capacity ratio n={rung}",
            iota_ratio,
            dimension ** (2 * rung),
        )
        check_close(
            f"Hubble ratio n={rung}",
            hubble_ratio,
            dimension ** (-rung),
        )
        check_close(
            f"common-count ratio n={rung}",
            count_ratio,
            dimension ** (2.0 * rung / 3.0),
        )
        check_close(
            f"yardstick-energy ratio n={rung}",
            energy_ratio,
            dimension ** (-rung / 3.0),
        )
        additive_hubble_ratio = math.sqrt(base_iota / (base_iota + capacity))
        check_close(
            f"additive-weld Hubble ratio n={rung}",
            additive_hubble_ratio,
            (1.0 + capacity / base_iota) ** -0.5,
        )
        if rung > 0 and math.isclose(
            additive_hubble_ratio, hubble_ratio, rel_tol=1.0e-12, abs_tol=TOL
        ):
            raise AssertionError("additive and multiplicative welds were conflated")

    print("PASS branch firewall: additive and multiplicative cosmic welds differ")

    mass_flow = 42.0
    hubble = 0.125
    epsilon = 0.2
    horizon_iota = 1.0e3
    horizon_mass = mass_flow / (2.0 * hubble)
    fractional_rate_mass = mass_flow / (2.0 * epsilon * hubble)
    additive_rate_mass = mass_flow / (2.0 * epsilon * hubble * horizon_iota)
    check_close(
        "fractional-ledger rate quotient",
        fractional_rate_mass,
        horizon_mass / epsilon,
    )
    check_close(
        "additive-nat rate quotient",
        additive_rate_mass,
        horizon_mass / (epsilon * horizon_iota),
    )
    if math.isclose(
        fractional_rate_mass, additive_rate_mass, rel_tol=1.0e-12, abs_tol=TOL
    ):
        raise AssertionError("fractional and additive ledger rates were conflated")
    print("PASS rate firewall: fractional-ledger and additive-nat quotients differ")
    print("PASS scope: finite arithmetic only; no Type-III or mass-gap claim tested")


if __name__ == "__main__":
    main()
