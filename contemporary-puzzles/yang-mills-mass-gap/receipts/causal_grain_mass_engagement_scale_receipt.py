"""Conditional horizon check for the causal-grain mass-engagement hypothesis.

This receipt deliberately adds the unproved identification k_B T_g = E_g only to
test an instantaneous or passively stretched thermal-imprint reading.  It does
not identify the causal grain with a temperature, the QCD crossover, or the BAO
ruler, and it does not bound the sound distance accumulated after this epoch.
"""

from __future__ import annotations

from math import pi, sqrt


C_M_S = 299_792_458.0
MPC_M = 3.085_677_581_491_367e22
PC_M = MPC_M / 1.0e6
HBAR_GEV_S = 6.582_119_569e-25
UNREDUCED_PLANCK_MASS_GEV = 1.220_890e19
BOLTZMANN_EV_K = 8.617_333_262e-5
CMB_TEMPERATURE_K = 2.7255
ENTROPY_DOF_TODAY = 3.930_936_3

GRAIN_ENERGY_GEV = 46.274705e-3
PLANCK_BASE_LCDM_DRAG_RULER_MPC = 147.09

# Saikawa--Shirai Standard Model thermodynamics table near 46.28 MeV.
ENERGY_DOF_AT_GRAIN = 14.3149
ENTROPY_DOF_AT_GRAIN = 14.0125


def epoch_scales(
    temperature_gev: float,
    energy_dof: float,
    entropy_dof: float,
) -> tuple[float, float, float]:
    """Return (scale factor, H in s^-1, present comoving c/H in Mpc)."""

    # The coefficient 1.66 is paired with the unreduced Planck mass.
    hubble_gev = (
        1.66
        * sqrt(energy_dof)
        * temperature_gev**2
        / UNREDUCED_PLANCK_MASS_GEV
    )
    hubble_s = hubble_gev / HBAR_GEV_S
    temperature_today_gev = CMB_TEMPERATURE_K * BOLTZMANN_EV_K * 1.0e-9
    scale_factor = (
        temperature_today_gev
        / temperature_gev
        * (ENTROPY_DOF_TODAY / entropy_dof) ** (1.0 / 3.0)
    )
    physical_hubble_radius_m = C_M_S / hubble_s
    comoving_hubble_radius_mpc = physical_hubble_radius_m / scale_factor / MPC_M
    return scale_factor, hubble_s, comoving_hubble_radius_mpc


scale_factor, hubble_s, horizon_mpc = epoch_scales(
    GRAIN_ENERGY_GEV,
    ENERGY_DOF_AT_GRAIN,
    ENTROPY_DOF_AT_GRAIN,
)
horizon_pc = horizon_mpc * 1.0e6
separation = PLANCK_BASE_LCDM_DRAG_RULER_MPC / horizon_mpc
horizon_reentry_frequency_hz = scale_factor * hubble_s / (2.0 * pi)

assert 3.0e-12 < scale_factor < 3.7e-12
assert 1.5e3 < hubble_s < 1.9e3
assert 1.5 < horizon_pc < 2.0
assert 7.0e7 < separation < 1.0e8
assert 0.5e-9 < horizon_reentry_frequency_hz < 1.5e-9

print(f"central estimate a(T_g)={scale_factor:.4e}")
print(f"central estimate H(T_g)={hubble_s:.4e} s^-1")
print(f"central estimate present comoving Hubble radius={horizon_pc:.3f} pc")
print(f"central estimate Planck base-LCDM r_drag / Hubble radius={separation:.3e}")
print(
    "central estimate present horizon-reentry frequency="
    f"{horizon_reentry_frequency_hz:.3e} Hz"
)

print("thermal identification is diagnostic only: passed")
print("later drag-ruler comoving scale is super-Hubble at the diagnostic 46 MeV epoch: passed")
print("no claim is made against later sound-horizon accumulation: passed")
print("thermal branch points to a nanohertz spectral address: passed")
