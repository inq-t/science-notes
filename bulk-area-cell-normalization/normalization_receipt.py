#!/usr/bin/env python3
"""Focused standard-library receipts for the bulk--area normalization."""

import math
import sys


C = 299_792_458.0
HBAR = 1.054_571_817e-34
G_NEWTON = 6.674_30e-11
MPC = 3.085_677_581_491_367_3e22
MEV_C2_KG = 1.602_176_634e-13 / C**2
H_CEPHEID = 88.2608 * 1000.0 / MPC
H_CMB = 82.64 * 1000.0 / MPC
S_INTERVAL = (0.9175, 1.0621)


failures = []


def check(name, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    print(f"{status}  {name}" + (f" | {detail}" if detail else ""))
    if not condition:
        failures.append(name)


def iota(H):
    return math.pi * C**5 / (G_NEWTON * HBAR * H**2)


def carrier_mass(H, gamma, s_star):
    return (
        3.0 * HBAR**2 * H
        / (4.0 * gamma * s_star * C * G_NEWTON)
    ) ** (1.0 / 3.0)


exact = True
for H in (H_CEPHEID, H_CMB):
    for s_star in (*S_INTERVAL, 0.9861, 1.0):
        mass = carrier_mass(H, 1.0, s_star)
        lam = HBAR / (mass * C)
        radius = C / H
        n_bulk = (4.0 * math.pi / 3.0) * (radius / lam) ** 3
        exact &= math.isclose(
            s_star * n_bulk,
            iota(H),
            rel_tol=1e-12,
        )

check(
    "zeta = s_star/3 reproduces iota = s_star (4pi/3)(R/lambda)^3",
    exact,
    "both branches, interval endpoints, and benchmark s_star values",
)

unit_values = [
    carrier_mass(H_CEPHEID, 1.0, 1.0) / MEV_C2_KG,
    carrier_mass(H_CMB, 1.0, 1.0) / MEV_C2_KG,
]
fit_values = [
    carrier_mass(H_CEPHEID, 1.0, 0.9861) / MEV_C2_KG,
    carrier_mass(H_CMB, 1.0, 0.9861) / MEV_C2_KG,
]
check(
    "carrier diagnostics reproduce the two branch values",
    abs(unit_values[0] - 59.48) < 0.02
    and abs(unit_values[1] - 58.19) < 0.02
    and abs(fit_values[0] - 59.76) < 0.02
    and abs(fit_values[1] - 58.47) < 0.02,
    (
        f"unit={unit_values[0]:.2f}/{unit_values[1]:.2f} MeV; "
        f"s_star=0.9861 gives {fit_values[0]:.2f}/{fit_values[1]:.2f} MeV"
    ),
)

window_low = carrier_mass(H_CMB, 1.0, S_INTERVAL[1]) / MEV_C2_KG
window_high = carrier_mass(H_CEPHEID, 1.0, S_INTERVAL[0]) / MEV_C2_KG
check(
    "two branches and fitted s_star interval give the sharpened window",
    57.03 < window_low < 57.05 and 61.21 < window_high < 61.23,
    f"[{window_low:.2f}, {window_high:.2f}] MeV",
)

if failures:
    print("FAILURES: " + ", ".join(failures))
    sys.exit(1)

print("ALL RECEIPTS PASS")
