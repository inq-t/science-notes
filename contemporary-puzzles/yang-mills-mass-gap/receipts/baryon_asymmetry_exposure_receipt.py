"""Check the ideal baryon-asymmetry exposure arithmetic.

The calculation is deliberately diagnostic.  It uses a Maxwell--Boltzmann
nucleon/antinucleon gas, an illustrative conserved baryon-to-entropy ratio,
and log-linear interpolation of three transcribed Saikawa--Shirai entropy
degree counts.  Its numerically precise interpolation root is not a
physically precise event temperature.  It does not model the full
hadron-resonance gas, solve a Boltzmann network, date the causal grain, or
derive a BAO observable.
"""

from __future__ import annotations

from math import asinh, exp, log, pi, sqrt

import numpy as np


M_N_MEV = 938.918
G_NUCLEON = 4.0  # proton/neutron spin states on one baryon-sign branch
Y_B = 8.7e-11  # illustrative conserved net-baryon-to-entropy ratio
T_GRAIN_MEV = 46.274705  # conditional thermal retyping, not an event date

# Central g_*s rows transcribed from:
# https://member.ipmu.jp/satoshi.shirai/standardmodel2018.dat
G_STAR_S_ROWS = (
    (20.054420, 11.238981),
    (46.283721, 14.012474),
    (100.324050, 17.352434),
)

# Gauss--Legendre representation of K_nu(z) on [0,12].
_nodes, _weights = np.polynomial.legendre.leggauss(256)
_times = 6.0 * (_nodes + 1.0)
_time_weights = 6.0 * _weights


def bessel_k(nu: int, z: float) -> float:
    values = np.exp(-z * np.cosh(_times)) * np.cosh(nu * _times)
    return float(np.dot(_time_weights, values))


def g_star_s(temperature_mev: float) -> float:
    """Piecewise log-linear diagnostic interpolation in temperature."""
    for (t0, g0), (t1, g1) in zip(G_STAR_S_ROWS, G_STAR_S_ROWS[1:]):
        if t0 <= temperature_mev <= t1:
            weight = log(temperature_mev / t0) / log(t1 / t0)
            return g0 + weight * (g1 - g0)
    raise ValueError("temperature outside the transcribed interpolation range")


def zero_potential_baryon_density_over_entropy(temperature_mev: float) -> float:
    """Return n_0/s for one baryon-sign branch in the ideal nucleon model."""
    x = M_N_MEV / temperature_mev
    n0_over_t3 = G_NUCLEON * x * x * bessel_k(2, x) / (2.0 * pi**2)
    entropy_over_t3 = (2.0 * pi**2 / 45.0) * g_star_s(temperature_mev)
    return n0_over_t3 / entropy_over_t3


def exposure_coordinates(temperature_mev: float) -> tuple[float, float, float, float]:
    """Return u=sinh(theta), pointing, complement, and anti/baryon ratio."""
    n0_over_s = zero_potential_baryon_density_over_entropy(temperature_mev)
    u = Y_B / (2.0 * n0_over_s)
    theta = asinh(u)
    pointing = u / sqrt(1.0 + u * u)
    complement = 1.0 / (1.0 + u * u)
    anti_to_baryon = exp(-2.0 * theta)
    return u, pointing, complement, anti_to_baryon


def balanced_temperature() -> float:
    """Solve u(T)=1, equivalently pointing^2=complement=1/2."""
    lower = 20.054420
    upper = 46.283721
    assert exposure_coordinates(lower)[0] > 1.0
    assert exposure_coordinates(upper)[0] < 1.0
    for _ in range(70):
        midpoint = 0.5 * (lower + upper)
        if exposure_coordinates(midpoint)[0] > 1.0:
            lower = midpoint
        else:
            upper = midpoint
    return 0.5 * (lower + upper)


grain_u, grain_pointing, grain_complement, grain_ratio = exposure_coordinates(
    T_GRAIN_MEV
)
balance_temperature = balanced_temperature()
balance_u, balance_pointing, balance_complement, balance_ratio = exposure_coordinates(
    balance_temperature
)

print(f"diagnostic Y_B={Y_B:.3e}")
print(f"at T_g={T_GRAIN_MEV:.6f} MeV: g_*s={g_star_s(T_GRAIN_MEV):.6f}")
print(f"at T_g: sinh(mu_B/T)={grain_u:.9f}")
print(f"at T_g: baryon pointing={grain_pointing:.9f}")
print(f"at T_g: binary complement={grain_complement:.9f}")
print(f"at T_g: n_antibaryon/n_baryon={grain_ratio:.9f}")
print(
    "balanced-exposure interpolation root="
    f"{balance_temperature:.6f} MeV (report only as about {balance_temperature:.1f} MeV)"
)
print(f"at balance: sinh(mu_B/T)={balance_u:.9f}")
print(f"at balance: baryon pointing={balance_pointing:.9f}")
print(f"at balance: binary complement={balance_complement:.9f}")
print(f"at balance: n_antibaryon/n_baryon={balance_ratio:.9f}")

assert abs(grain_pointing * grain_pointing + grain_complement - 1.0) < 1e-14
assert abs(grain_u - 0.006824909) < 5e-10
assert abs(grain_ratio - 0.986443024) < 5e-10
assert abs(balance_u - 1.0) < 1e-12
assert abs(balance_pointing - 1.0 / sqrt(2.0)) < 1e-12
assert abs(balance_complement - 0.5) < 1e-12
assert abs(balance_temperature - 36.578314) < 5e-6
assert balance_temperature < T_GRAIN_MEV

print("PASS: pair exposure obeys the exact binary complement identity.")
print(
    "PASS: in the declared ideal-nucleon/interpolation model, "
    "the u=1 balance temperature differs from the conditionally retyped grain temperature."
)
