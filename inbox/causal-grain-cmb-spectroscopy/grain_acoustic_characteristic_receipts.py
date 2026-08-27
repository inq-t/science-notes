"""Arithmetic receipts for the proposed grain--acoustic characteristic.

The checks below verify unit cancellations, parse a bundled Planck best-fit
parameter file, and reproduce the displayed central values. They do not prove
the post-search characteristic, the chiral clause, or statistical significance.
"""

from __future__ import annotations

import math
import re
from pathlib import Path


MODULE = Path(__file__).resolve().parent
REPO = MODULE.parents[1]
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
PLANCK_100_THETA_SIGMA = 0.00030


def close(a: float, b: float, *, rel: float = 1e-11, abs_: float = 0.0) -> None:
    if not math.isclose(a, b, rel_tol=rel, abs_tol=abs_):
        raise AssertionError(f"{a:.16g} != {b:.16g}")


def read_planck_parameters(path: Path) -> dict[str, float]:
    wanted = {"rstar", "thetastar", "DAstar"}
    values: dict[str, float] = {}
    row = re.compile(r"^\s*\d+\s+([+-]?\d*\.?\d+(?:[Ee][+-]?\d+)?)\s+(\w+)\b")
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        match = row.match(line)
        if match and match.group(2) in wanted:
            values[match.group(2)] = float(match.group(1))
    missing = wanted.difference(values)
    if missing:
        raise ValueError(f"missing Planck parameters: {sorted(missing)}")
    return values


def positive_characteristic_root(scale_label: float, kappa: float = KAPPA) -> float:
    argument = 3.0 * math.sqrt(3.0) * scale_label**3 / (2.0 * kappa**1.5)
    return 2.0 * math.sqrt(kappa / 3.0) * math.sinh(math.asinh(argument) / 3.0)


def grain_from_hubble(hubble_km_s_mpc: float) -> dict[str, float]:
    hubble = hubble_km_s_mpc * 1_000.0 / MPC
    radius = C / hubble
    planck_length_sq = HBAR * G / C**3
    wavelength = (KAPPA * planck_length_sq * radius) ** (1.0 / 3.0)
    energy = HBAR * C / wavelength
    quality = radius / wavelength
    sigma = math.log(quality)
    beta = 2.0 * math.pi / (HBAR * hubble)
    alpha_h = G * HBAR * hubble**2 / C**5
    iota = math.pi / alpha_h

    close(quality, energy / (HBAR * hubble))
    close(quality, beta * energy / (2.0 * math.pi))
    close(quality**3, 3.0 * iota / (8.0 * math.pi))
    close(quality**3, 3.0 / (8.0 * alpha_h))
    close(sigma, -math.log(wavelength / radius))

    return {
        "hubble": hubble,
        "radius": radius,
        "wavelength": wavelength,
        "energy": energy,
        "quality": quality,
        "sigma": sigma,
        "iota": iota,
        "alpha_h": alpha_h,
    }


def central_planck_receipt() -> tuple[float, float]:
    params = read_planck_parameters(PLANCK_MINIMUM)
    theta = params["thetastar"] / 100.0
    q_observed = 1.0 / theta
    distance_ratio = params["DAstar"] * 1_000.0 / params["rstar"]
    close(distance_ratio, q_observed, rel=5e-5)

    grain = grain_from_hubble(83.1058)
    scale_label = 3.0 + grain["sigma"]
    q_predicted = positive_characteristic_root(scale_label)
    close(q_predicted * (q_predicted**2 + KAPPA), scale_label**3)
    theta_100_predicted = 100.0 / q_predicted
    kappa_central = (scale_label**3 - q_observed**3) / q_observed
    q_sigma = 100.0 * PLANCK_100_THETA_SIGMA / params["thetastar"] ** 2

    print("CMB-CONDITIONED CENTRAL RECEIPT")
    print(f"  100 theta_* bundled         = {params['thetastar']:.9f}")
    print(f"  q_*=1/theta_*               = {q_observed:.12f}")
    print(f"  ell_A=pi*q_*                = {math.pi * q_observed:.12f}")
    print(f"  lambda_*                    = {grain['wavelength'] * 1e15:.12f} fm")
    print(f"  Sigma_c                     = {grain['sigma']:.12f} nats")
    print(f"  q_*-Sigma_c                 = {q_observed - grain['sigma']:.12f}")
    print(f"  cubic q_*                   = {q_predicted:.12f}")
    print(f"  cubic 100 theta_*           = {theta_100_predicted:.12f}")
    print(f"  q residual                  = {q_predicted - q_observed:+.6e}")
    print(f"  central inferred kappa      = {kappa_central:.12f}")
    print(f"  kappa vs 8/3                = {100.0 * (kappa_central / KAPPA - 1.0):+.6f}%")
    print(f"  q sigma from Planck quote   = {q_sigma:.6f}")
    print("  scope: central-value reconstruction on a CMB-conditioned branch")

    return q_observed, params["thetastar"]


def chiral_cancellation_receipt() -> tuple[float, float]:
    f_pi_chiral_mev = 130.2 / math.sqrt(2.0)
    pion_energy_mev = 139.57039
    grain_energy_mev = math.sqrt(f_pi_chiral_mev * pion_energy_mev / 6.0)
    grain_energy = grain_energy_mev * 1e6 * EV

    hubble = 8.0 * G * grain_energy**3 / (3.0 * HBAR**2 * C**5)
    quality_from_grain = grain_energy / (HBAR * hubble)
    f_pi_chiral = f_pi_chiral_mev * 1e6 * EV
    pion_energy = pion_energy_mev * 1e6 * EV
    quality_cancelled = 9.0 * HBAR * C**5 / (
        4.0 * G * f_pi_chiral * pion_energy
    )
    close(quality_from_grain, quality_cancelled)

    scale_label = 3.0 + math.log(quality_cancelled)
    q_predicted = positive_characteristic_root(scale_label)
    theta_100_predicted = 100.0 / q_predicted
    hubble_km_s_mpc = hubble * MPC / 1_000.0

    print("FULLY CANCELLED CH3 ORACLE (POST-SEARCH)")
    print(f"  F_pi^chi                    = {f_pi_chiral_mev:.12f} MeV")
    print(f"  E_pi+/-                     = {pion_energy_mev:.12f} MeV")
    print(f"  E_*                         = {grain_energy_mev:.12f} MeV")
    print(f"  implied H_c                 = {hubble_km_s_mpc:.12f} km/s/Mpc")
    print(f"  cancelled Q_c               = {quality_cancelled:.12e}")
    print(f"  L_g=3+ln(Q_c)               = {scale_label:.12f}")
    print(f"  predicted q_*               = {q_predicted:.12f}")
    print(f"  predicted 100 theta_*       = {theta_100_predicted:.12f}")
    print("  scope: CH3 plus cubic weld; both are unproved post-search choices")

    return q_predicted, theta_100_predicted


def branch_receipts(observed_theta_100: float) -> None:
    branches = (
        ("CH0 theory", 81.8085),
        ("CMB-conditioned", 83.1058),
        ("Cepheid-calibrated", 88.2608),
    )
    print("BRANCH SENSITIVITY")
    for name, hubble in branches:
        sigma = grain_from_hubble(hubble)["sigma"]
        q_predicted = positive_characteristic_root(3.0 + sigma)
        theta_100 = 100.0 / q_predicted
        print(
            f"  {name:20s} H_c={hubble:9.4f}"
            f"  100 theta_*={theta_100:.12f}"
            f"  delta={theta_100 - observed_theta_100:+.6e}"
        )


def main() -> None:
    if not PLANCK_MINIMUM.is_file():
        raise FileNotFoundError(PLANCK_MINIMUM)

    _, observed_theta_100 = central_planck_receipt()
    print()
    chiral_cancellation_receipt()
    print()
    branch_receipts(observed_theta_100)
    print()
    print("ALL GRAIN--ACOUSTIC RECEIPTS PASS")
    print("Scope: arithmetic and local-file provenance, not a physics proof or fit.")


if __name__ == "__main__":
    main()
