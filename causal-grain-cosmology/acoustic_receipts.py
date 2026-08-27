"""Arithmetic receipts for the causal-grain acoustic candidates.

These checks reproduce the dimensional cancellations and central values quoted
in the module. They do not prove the common-count law, either chiral clause, or
the post-search acoustic characteristic.
"""

from __future__ import annotations

import math
import re
from pathlib import Path


MODULE = Path(__file__).resolve().parent
REPO = MODULE.parent
PLANCK_MINIMUM = (
    REPO
    / "causal-wall-spectral-theory"
    / "sources"
    / "data"
    / "planck-2018"
    / "COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum_R3.01.txt"
)

C = 299_792_458.0
HBAR = 1.054_571_817e-34
G = 6.674_30e-11
EV = 1.602_176_634e-19
MPC = 3.085_677_581_491_367e22
KAPPA = 8.0 / 3.0
PLANCK_THETA_100_SIGMA = 0.00030


def close(a: float, b: float, *, rel: float = 1e-11) -> None:
    if not math.isclose(a, b, rel_tol=rel):
        raise AssertionError(f"{a:.16g} != {b:.16g}")


def positive_root(scale_label: float) -> float:
    argument = 3.0 * math.sqrt(3.0) * scale_label**3 / (2.0 * KAPPA**1.5)
    return 2.0 * math.sqrt(KAPPA / 3.0) * math.sinh(
        math.asinh(argument) / 3.0
    )


def planck_theta_100() -> float:
    row = re.compile(r"^\s*\d+\s+([+-]?\d*\.?\d+(?:[Ee][+-]?\d+)?)\s+thetastar\b")
    for line in PLANCK_MINIMUM.read_text(
        encoding="utf-8", errors="replace"
    ).splitlines():
        match = row.match(line)
        if match:
            return float(match.group(1))
    raise ValueError("thetastar missing from bundled Planck best-fit file")


def common_count_branch(hubble_km_s_mpc: float) -> tuple[float, float, float]:
    hubble = hubble_km_s_mpc * 1_000.0 / MPC
    radius = C / hubble
    planck_length_sq = HBAR * G / C**3
    wavelength = (KAPPA * planck_length_sq * radius) ** (1.0 / 3.0)
    quality = radius / wavelength
    energy = HBAR * C / wavelength
    close(quality, energy / (HBAR * hubble))
    return wavelength, quality, math.log(quality)


def acoustic_from_quality(quality: float) -> tuple[float, float]:
    q_value = positive_root(3.0 + math.log(quality))
    close(q_value * (q_value**2 + KAPPA), (3.0 + math.log(quality)) ** 3)
    return q_value, 100.0 / q_value


def minimal_chiral_quality(f_pi_input_mev: float) -> float:
    f_pi_chiral = f_pi_input_mev / math.sqrt(2.0) * 1e6 * EV
    grain_energy = f_pi_chiral / 2.0
    hubble = 8.0 * G * grain_energy**3 / (3.0 * HBAR**2 * C**5)
    quality_direct = grain_energy / (HBAR * hubble)
    quality_cancelled = 3.0 * HBAR * C**5 / (2.0 * G * f_pi_chiral**2)
    close(quality_direct, quality_cancelled)
    return quality_cancelled


def pion_midpoint_quality(
    f_pi_input_mev: float, pion_energy_mev: float
) -> float:
    f_pi_chiral = f_pi_input_mev / math.sqrt(2.0) * 1e6 * EV
    pion_energy = pion_energy_mev * 1e6 * EV
    grain_energy = math.sqrt(f_pi_chiral * pion_energy / 6.0)
    hubble = 8.0 * G * grain_energy**3 / (3.0 * HBAR**2 * C**5)
    quality_direct = grain_energy / (HBAR * hubble)
    quality_cancelled = 9.0 * HBAR * C**5 / (
        4.0 * G * f_pi_chiral * pion_energy
    )
    close(quality_direct, quality_cancelled)
    return quality_cancelled


def main() -> None:
    if not PLANCK_MINIMUM.is_file():
        raise FileNotFoundError(PLANCK_MINIMUM)

    theta_100_observed = planck_theta_100()
    q_observed = 100.0 / theta_100_observed

    wavelength, quality_conditioned, sigma_conditioned = common_count_branch(83.1058)
    q_conditioned, theta_100_conditioned = acoustic_from_quality(quality_conditioned)

    f_pi_input = 130.2
    f_pi_sigma = 1.2
    quality_minimal = minimal_chiral_quality(f_pi_input)
    q_minimal, theta_100_minimal = acoustic_from_quality(quality_minimal)
    theta_low = acoustic_from_quality(
        minimal_chiral_quality(f_pi_input - f_pi_sigma)
    )[1]
    theta_high = acoustic_from_quality(
        minimal_chiral_quality(f_pi_input + f_pi_sigma)
    )[1]
    theta_input_sigma = (theta_high - theta_low) / 2.0

    quality_midpoint = pion_midpoint_quality(f_pi_input, 139.57039)
    q_midpoint, theta_100_midpoint = acoustic_from_quality(quality_midpoint)

    print("CMB-CONDITIONED RECONSTRUCTION (IN-SAMPLE)")
    print(f"  bundled 100 theta_*         = {theta_100_observed:.12f}")
    print(f"  observed q_*                = {q_observed:.12f}")
    print(f"  lambda_*                    = {wavelength * 1e15:.12f} fm")
    print(f"  Sigma_c                     = {sigma_conditioned:.12f}")
    print(f"  q_*-Sigma_c                 = {q_observed - sigma_conditioned:.12f}")
    print(f"  cubic 100 theta_*           = {theta_100_conditioned:.12f}")
    print(f"  cubic q residual            = {q_conditioned - q_observed:+.6e}")
    print()
    print("MINIMAL CHIRAL ORACLE (POST-SEARCH)")
    print(f"  predicted q_*               = {q_minimal:.12f}")
    print(f"  predicted 100 theta_*       = {theta_100_minimal:.12f}")
    print(f"  residual / Planck sigma     = {(theta_100_minimal - theta_100_observed) / PLANCK_THETA_100_SIGMA:+.6f}")
    print(f"  propagated chiral sigma     = {theta_input_sigma:.12f}")
    print()
    print("CHARGED-PION MIDPOINT ORACLE (POST-SEARCH)")
    print(f"  predicted q_*               = {q_midpoint:.12f}")
    print(f"  predicted 100 theta_*       = {theta_100_midpoint:.12f}")
    print(f"  residual / Planck sigma     = {(theta_100_midpoint - theta_100_observed) / PLANCK_THETA_100_SIGMA:+.6f}")
    print()
    print("ALL CAUSAL-GRAIN COSMOLOGY RECEIPTS PASS")
    print("Scope: arithmetic and local provenance, not a physics proof or fit.")


if __name__ == "__main__":
    main()
