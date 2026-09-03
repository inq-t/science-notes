"""Reproduce selected Standard-Model trace-fossil diagnostics.

Central rows are transcribed from the Saikawa--Shirai machine-readable table:
https://member.ipmu.jp/satoshi.shirai/standardmodel2018.dat

Particle masses and the charged-pion lifetime use the 2025 PDG summary tables:
https://pdg.lbl.gov/2025/tables/contents_tables.html

This receipt checks arithmetic only.  It does not propagate the correlated
table uncertainties, establish global uniqueness of either stationary point,
model an interacting pion gas or collision spectrum, select a particle
species, or establish a causal-grain, mass-gap, or BAO map.
"""

from __future__ import annotations

from math import log, sqrt

import numpy as np


# Temperature [GeV]: (g_*rho, g_*s)
ROWS = {
    0.020054420: (11.326008, 11.238981),
    0.046283721: (14.314909, 14.012474),
    0.100324050: (17.766600, 17.352434),
    0.150038880: (27.171459, 25.450391),
    0.175512160: (35.664284, 32.879053),
    0.200013840: (41.095117, 38.108558),
    0.299129190: (52.346759, 49.875614),
}


def trace_fraction(temperature: float) -> float:
    g_rho, g_s = ROWS[temperature]
    return 4.0 * (1.0 - g_s / g_rho)


def adiabatic_residue(high_temperature: float, low_temperature: float) -> float:
    g_rho_high, g_s_high = ROWS[high_temperature]
    g_rho_low, g_s_low = ROWS[low_temperature]
    return (
        log(g_rho_low / g_rho_high)
        - (4.0 / 3.0) * log(g_s_low / g_s_high)
    )


# K_nu(z) = integral_0^infinity exp(-z cosh(t)) cosh(nu t) dt.
# Gauss--Legendre quadrature on [0, 12] is ample for the x >= 1 tests here.
_nodes, _weights = np.polynomial.legendre.leggauss(256)
_times = 6.0 * (_nodes + 1.0)
_time_weights = 6.0 * _weights


def bessel_k(nu: int, z: float) -> float:
    values = np.exp(-z * np.cosh(_times)) * np.cosh(nu * _times)
    return float(np.dot(_time_weights, values))


def bose_sums(x: float) -> tuple[float, float]:
    sum_k0 = 0.0
    sum_k1_over_n = 0.0
    for n in range(1, 65):
        k0 = bessel_k(0, n * x)
        k1_over_n = bessel_k(1, n * x) / n
        sum_k0 += k0
        sum_k1_over_n += k1_over_n
        if abs(k1_over_n) < 1e-15:
            break
    return sum_k0, sum_k1_over_n


def fermi_sums(x: float) -> tuple[float, float]:
    sum_k0 = 0.0
    sum_k1_over_n = 0.0
    for n in range(1, 65):
        sign = 1.0 if n % 2 == 1 else -1.0
        k0 = sign * bessel_k(0, n * x)
        k1_over_n = sign * bessel_k(1, n * x) / n
        sum_k0 += k0
        sum_k1_over_n += k1_over_n
        if abs(k1_over_n) < 1e-15:
            break
    return sum_k0, sum_k1_over_n


def bose_trace_shape(x: float) -> float:
    _, sum_k1_over_n = bose_sums(x)
    return x**3 * sum_k1_over_n


def bose_trace_derivative_sign(x: float) -> float:
    sum_k0, sum_k1_over_n = bose_sums(x)
    return 2.0 * sum_k1_over_n - x * sum_k0


def bose_trace_peak() -> float:
    lower = 1.0
    upper = 5.0
    assert bose_trace_derivative_sign(lower) > 0.0
    assert bose_trace_derivative_sign(upper) < 0.0
    for _ in range(60):
        midpoint = 0.5 * (lower + upper)
        if bose_trace_derivative_sign(midpoint) > 0.0:
            lower = midpoint
        else:
            upper = midpoint
    return 0.5 * (lower + upper)


def fermi_trace_shape(x: float) -> float:
    _, sum_k1_over_n = fermi_sums(x)
    return x**3 * sum_k1_over_n


def fermi_trace_derivative_sign(x: float) -> float:
    sum_k0, sum_k1_over_n = fermi_sums(x)
    return 2.0 * sum_k1_over_n - x * sum_k0


def fermi_trace_stationary_point() -> float:
    lower = 1.0
    upper = 5.0
    assert fermi_trace_derivative_sign(lower) > 0.0
    assert fermi_trace_derivative_sign(upper) < 0.0
    for _ in range(60):
        midpoint = 0.5 * (lower + upper)
        if fermi_trace_derivative_sign(midpoint) > 0.0:
            lower = midpoint
        else:
            upper = midpoint
    return 0.5 * (lower + upper)


for temperature in ROWS:
    print(
        f"T={1000.0 * temperature:.6f} MeV: "
        f"Theta/rho={trace_fraction(temperature):.9f}"
    )

print(
    "Xi(299.129190 -> 46.283721 MeV)="
    f"{adiabatic_residue(0.299129190, 0.046283721):.9f}"
)
print(
    "Xi(150.038880 -> 46.283721 MeV)="
    f"{adiabatic_residue(0.150038880, 0.046283721):.9f}"
)
print(
    "Xi(100.324050 -> 46.283721 MeV)="
    f"{adiabatic_residue(0.100324050, 0.046283721):.9f}"
)
print(
    "Xi(299.129190 -> 20.054420 MeV)="
    f"{adiabatic_residue(0.299129190, 0.020054420):.9f}"
)

charged_pion_mass_mev = 139.57039
charged_pion_lifetime_seconds = 2.6033e-8
muon_mass_mev = 105.6583755
grain_temperature_mev = 46.274705
bose_peak_x = bose_trace_peak()
grain_x = charged_pion_mass_mev / grain_temperature_mev
shape_ratio = bose_trace_shape(grain_x) / bose_trace_shape(bose_peak_x)
fermi_peak_x = fermi_trace_stationary_point()
muon_grain_x = muon_mass_mev / grain_temperature_mev
muon_shape_ratio = fermi_trace_shape(muon_grain_x) / fermi_trace_shape(fermi_peak_x)

# Standard radiation-dominated estimate H=1.66 sqrt(g_*rho) T^2/M_Pl.
planck_mass_gev = 1.220890e19
hbar_gev_seconds = 6.582119569e-25
grain_g_rho = ROWS[0.046283721][0]
grain_temperature_gev = grain_temperature_mev / 1000.0
hubble_per_second = (
    1.66
    * sqrt(grain_g_rho)
    * grain_temperature_gev**2
    / planck_mass_gev
    / hbar_gev_seconds
)
charged_pion_decay_over_hubble = (
    1.0 / charged_pion_lifetime_seconds / hubble_per_second
)

print(f"ideal Bose stationary point: x=m/T={bose_peak_x:.9f}")
print(
    "charged-pion stationary temperature="
    f"{charged_pion_mass_mev / bose_peak_x:.6f} MeV"
)
print(f"grain-temperature x=m_pi/T={grain_x:.9f}")
print(f"pion trace-shape ratio at grain temperature={shape_ratio:.9f}")
print(f"ideal Fermi stationary point: x=m/T={fermi_peak_x:.9f}")
print(
    "muon stationary temperature="
    f"{muon_mass_mev / fermi_peak_x:.6f} MeV"
)
print(f"muon trace-shape ratio at grain temperature={muon_shape_ratio:.9f}")
print(f"radiation-era H(T_g)={hubble_per_second:.6e} s^-1")
print(
    "charged-pion vacuum-decay rate/H(T_g)="
    f"{charged_pion_decay_over_hubble:.6e}"
)

assert trace_fraction(0.046283721) < 0.1
assert trace_fraction(0.175512160) > 0.3
assert trace_fraction(0.175512160) > trace_fraction(0.046283721)
assert abs(adiabatic_residue(0.299129190, 0.046283721) - 0.396190560) < 1e-9
assert abs(adiabatic_residue(0.150038880, 0.046283721) - 0.154845359) < 1e-9
assert abs(adiabatic_residue(0.100324050, 0.046283721) - 0.069027761) < 1e-9
assert abs(adiabatic_residue(0.299129190, 0.020054420) - 0.456070321) < 1e-9
assert abs(bose_peak_x - 2.302863424) < 1e-8
assert abs(charged_pion_mass_mev / bose_peak_x - 60.607324) < 1e-6
assert abs(shape_ratio - 0.918648952) < 1e-8
assert abs(fermi_peak_x - 2.453869) < 1e-6
assert muon_shape_ratio > 0.99
assert charged_pion_decay_over_hubble > 1e4

print("PASS: among the seven hard-coded central rows, 46 MeV does not maximize Theta/rho.")
print(
    "PASS: in the hard-coded charged-pion ideal-gas model, the normalized shape "
    f"at T_g is {shape_ratio:.9f} of its bracketed stationary maximum."
)
print("PASS: the muon negative control is even closer to its generic thermal shoulder.")
print("PASS: generic charged-pion decay is far faster than expansion at T_g.")
