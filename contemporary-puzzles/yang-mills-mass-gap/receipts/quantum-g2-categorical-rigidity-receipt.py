"""Finite checks for the quantum-G2 categorical-rigidity note.

This receipt checks elementary scalar identities and inversion of the explicitly
conditional cosmic-depth equation. It does not prove categorical property (T),
compute a Kazhdan constant, or construct a physical Yang--Mills carrier.
"""

from __future__ import annotations

import math


TOL = 5.0e-12

C_LIGHT = 299_792_458.0
G_NEWTON = 6.67430e-11
HBAR = 1.054571817e-34
MPC_METRES = 3.085677581491367e22


def quantum_dimension(q_value: float) -> float:
    powers = (10, 8, 2, 0, -2, -8, -10)
    return sum(q_value**power for power in powers)


def quantum_dimension_eta(eta: float) -> float:
    return (
        1.0
        + 2.0 * math.cosh(2.0 * eta)
        + 2.0 * math.cosh(8.0 * eta)
        + 2.0 * math.cosh(10.0 * eta)
    )


def jones_certificate(q_value: float) -> float:
    return (q_value - 1.0 / q_value) ** 2 * (
        q_value**2 + 1.0 + q_value**-2
    )


def check_close(name: str, actual: float, expected: float) -> None:
    if not math.isclose(actual, expected, rel_tol=1.0e-11, abs_tol=TOL):
        raise AssertionError(f"{name}: {actual} != {expected}")
    print(f"PASS {name}: actual={actual:.12g}, expected={expected:.12g}")


def check_asymptotic(name: str, actual: float, expected: float) -> None:
    if not math.isclose(actual, expected, rel_tol=1.0e-6, abs_tol=1.0e-6):
        raise AssertionError(f"{name}: {actual} is not close to {expected}")
    print(f"PASS {name}: actual={actual:.12g}, limit={expected:.12g}")


def invert_dimension(target: float) -> float:
    if target < 7.0:
        raise ValueError("positive-real-q branch requires target dimension >= 7")
    if math.isclose(target, 7.0, abs_tol=TOL):
        return 0.0
    lower = 0.0
    upper = 1.0
    while quantum_dimension_eta(upper) < target:
        upper *= 2.0
    for _ in range(120):
        middle = 0.5 * (lower + upper)
        if quantum_dimension_eta(middle) < target:
            lower = middle
        else:
            upper = middle
    return 0.5 * (lower + upper)


def main() -> None:
    for q_value in (0.5, 0.8, 1.0, 1.25, 2.0):
        check_close(
            f"q-inversion dimension symmetry q={q_value}",
            quantum_dimension(q_value),
            quantum_dimension(1.0 / q_value),
        )
        check_close(
            f"eta presentation q={q_value}",
            quantum_dimension(q_value),
            quantum_dimension_eta(math.log(q_value)),
        )

    check_close("classical quantum dimension", quantum_dimension(1.0), 7.0)
    capacity_at_one = 2.0 * math.log(quantum_dimension(1.0))
    check_close("classical index capacity", capacity_at_one, 2.0 * math.log(7.0))
    check_close("Jones certificate at q=1", jones_certificate(1.0), 0.0)
    print("PASS firewall: positive 2 log(7) capacity coexists with zero Jones certificate")

    for q_value in (0.6, 0.9, 1.1, 1.7):
        certificate = jones_certificate(q_value)
        if certificate <= 0.0:
            raise AssertionError("Jones certificate must be positive away from q=1")
        check_close(
            f"certificate inversion symmetry q={q_value}",
            certificate,
            jones_certificate(1.0 / q_value),
        )

    eta_small = 1.0e-5
    dimension_quadratic = (quantum_dimension_eta(eta_small) - 7.0) / eta_small**2
    certificate_quadratic = jones_certificate(math.exp(eta_small)) / eta_small**2
    check_asymptotic("dimension small-eta coefficient", dimension_quadratic, 168.0)
    check_asymptotic("certificate small-eta coefficient", certificate_quadratic, 12.0)

    eta_true = 0.137
    fusion_depth = 6
    target_dimension = quantum_dimension_eta(eta_true)
    cosmic_depth = 2.0 * fusion_depth * math.log(target_dimension)
    eta_recovered = invert_dimension(math.exp(cosmic_depth / (2.0 * fusion_depth)))
    check_close("conditional cosmic-depth inversion", eta_recovered, eta_true)
    check_close(
        "twofold q presentation",
        quantum_dimension(math.exp(eta_recovered)),
        quantum_dimension(math.exp(-eta_recovered)),
    )

    impossible_target = math.exp((2.0 * fusion_depth * math.log(7.0) - 0.1) / (2.0 * fusion_depth))
    try:
        invert_dimension(impossible_target)
    except ValueError:
        print("PASS threshold: depth below 2 n log(7) has no positive-real-q solution")
    else:
        raise AssertionError("sub-threshold target was incorrectly accepted")

    # Post-search diagnostic only.  Combine the separately proposed one-channel
    # birth section iota_b=1 with the two existing crossing-rate branches.  The
    # result does not select fusion depth, identify direct-sum multiplicity with
    # tensor power, or validate the cosmic/index weld.
    birth_hubble = math.sqrt(math.pi * C_LIGHT**5 / (G_NEWTON * HBAR))
    for label, hubble_km_s_mpc in (
        ("CMB-conditioned", 83.1058),
        ("local-ladder", 88.2608),
    ):
        hubble = hubble_km_s_mpc * 1_000.0 / MPC_METRES
        ledger_depth = 2.0 * math.log(birth_hubble / hubble)
        maximum_depth = math.floor(ledger_depth / (2.0 * math.log(7.0)))
        if maximum_depth != 72:
            raise AssertionError(
                f"{label}: expected maximum admissible integer depth 72, "
                f"got {maximum_depth}"
            )
        residual = ledger_depth - 144.0 * math.log(7.0)
        eta_at_72 = invert_dimension(math.exp(ledger_depth / 144.0))
        print(
            "PASS post-search one-channel diagnostic "
            f"{label}: D={ledger_depth:.12g}, n_max={maximum_depth}, "
            f"D-144log(7)={residual:.12g}, "
            f"eta_72={eta_at_72:.12g}, q_72={math.exp(eta_at_72):.12g}"
        )

    print("PASS scope: scalar identities only; no property-(T) or mass-gap claim tested")


if __name__ == "__main__":
    main()
