#!/usr/bin/env python3
"""Standard-library receipts for minimal cosmodynamic closure.

The checks verify conditional algebra and reproduce two frozen numerical
protocols. They do not prove fixed extensivity, the unit wall correspondence,
the rank-two common-count identification, the operator-induced chiral solder,
the independent correlation-ruler identification, fossil transport, or the
optional spectral-width clause.
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path


C = 299_792_458.0
HBAR = 1.054_571_817e-34
G_NEWTON = 6.674_30e-11
MPC = 3.085_677_581_491_367_3e22
EV_J = 1.602_176_634e-19
MEV_J = 1.0e6 * EV_J
SECONDS_PER_GYR = 365.25 * 86_400.0 * 1.0e9

F_PI_PLUS_THEORY_PDG_MEV = 130.2
F_PI_PLUS_THEORY_SIGMA_PDG_MEV = 1.2
F_PI_PLUS_EXPERIMENTAL_PDG_MEV = 130.56

ROOT = Path(__file__).resolve().parents[1]
FIT_PATH = ROOT / "causal-scale-theory" / "receipts" / "late-time-background-fit.json"
SHAPE_PATH = ROOT / "causal-scale-theory" / "receipts" / "late-time-best-fit-prediction.json"
GENERALIZED_PATH = (
    ROOT / "causal-scale-theory" / "receipts" / "generalized-background-fit-2025.json"
)

failures: list[str] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    print(f"{status}  {name}" + (f" | {detail}" if detail else ""))
    if not condition:
        failures.append(name)


def close(left: float, right: float, tolerance: float = 1.0e-10) -> bool:
    return math.isclose(left, right, rel_tol=tolerance, abs_tol=0.0)


def within(value: float, target: float, tolerance: float) -> bool:
    return abs(value - target) <= tolerance


def sech2(value: float) -> float:
    return 1.0 / math.cosh(value) ** 2


def bisect(function, low: float, high: float, iterations: int = 120) -> float:
    f_low = function(low)
    f_high = function(high)
    if f_low == 0.0:
        return low
    if f_high == 0.0:
        return high
    if f_low * f_high > 0.0:
        raise ValueError("root is not bracketed")
    for _ in range(iterations):
        middle = 0.5 * (low + high)
        f_middle = function(middle)
        if f_low * f_middle <= 0.0:
            high = middle
            f_high = f_middle
        else:
            low = middle
            f_low = f_middle
    return 0.5 * (low + high)


def grain_energy_mev(f_pi_pdg_mev: float) -> float:
    """Return E_*=F_pi/2=f_pi/(2 sqrt(2))."""

    return f_pi_pdg_mev / (2.0 * math.sqrt(2.0))


def crossing_rate_si(f_pi_pdg_mev: float) -> float:
    energy = grain_energy_mev(f_pi_pdg_mev) * MEV_J
    mass = energy / C**2
    return 8.0 * C * G_NEWTON * mass**3 / (3.0 * HBAR**2)


def km_s_mpc(rate_si: float) -> float:
    return rate_si * MPC / 1000.0


def age_factor(
    Omega_m0: float,
    Omega_r0: float,
    x_crossing: float,
    lower: float = -30.0,
    intervals: int = 120_000,
) -> float:
    """Return H0*t0 by Simpson integration in present-centered N."""

    if intervals % 2:
        raise ValueError("Simpson intervals must be even")
    dark = 1.0 - Omega_m0 - Omega_r0
    normalizer = sech2(x_crossing)

    def inverse_e(n_value: float) -> float:
        e2 = (
            Omega_m0 * math.exp(-3.0 * n_value)
            + Omega_r0 * math.exp(-4.0 * n_value)
            + dark * sech2(n_value + x_crossing) / normalizer
        )
        return 1.0 / math.sqrt(e2)

    step = -lower / intervals
    total = inverse_e(lower) + inverse_e(0.0)
    for index in range(1, intervals):
        weight = 4.0 if index % 2 else 2.0
        total += weight * inverse_e(lower + index * step)
    return total * step / 3.0


def e2_derivatives(
    n_value: float,
    Omega_m0: float,
    Omega_r0: float,
    x_crossing: float,
) -> tuple[float, float, float]:
    """Return E^2 and its first two N derivatives."""

    dark = 1.0 - Omega_m0 - Omega_r0
    normalizer = sech2(x_crossing)
    response = sech2(n_value + x_crossing)
    tangent = math.tanh(n_value + x_crossing)
    e2 = (
        Omega_m0 * math.exp(-3.0 * n_value)
        + Omega_r0 * math.exp(-4.0 * n_value)
        + dark * response / normalizer
    )
    first = (
        -3.0 * Omega_m0 * math.exp(-3.0 * n_value)
        - 4.0 * Omega_r0 * math.exp(-4.0 * n_value)
        - 2.0 * dark * tangent * response / normalizer
    )
    second = (
        9.0 * Omega_m0 * math.exp(-3.0 * n_value)
        + 16.0 * Omega_r0 * math.exp(-4.0 * n_value)
        + dark * (4.0 * response - 6.0 * response**2) / normalizer
    )
    return e2, first, second


def deceleration(
    n_value: float,
    Omega_m0: float,
    Omega_r0: float,
    x_crossing: float,
) -> float:
    e2, first, _ = e2_derivatives(
        n_value,
        Omega_m0,
        Omega_r0,
        x_crossing,
    )
    return -1.0 - 0.5 * first / e2


with FIT_PATH.open(encoding="utf-8") as handle:
    fit = json.load(handle)
with SHAPE_PATH.open(encoding="utf-8") as handle:
    shape = json.load(handle)
with GENERALIZED_PATH.open(encoding="utf-8") as handle:
    generalized = json.load(handle)

released = fit["comparisons"]["desi-dr2-bao-2025"]["models"]["cst-b2-unit"]["joint"]
released_lcdm = fit["comparisons"]["desi-dr2-bao-2025"]["models"]["lcdm"]["joint"]
Omega_m0_fit = released["omega_m_best"]
Omega_r0_fit = shape["inputs"]["omega_r0"]
dark_fit = 1.0 - Omega_m0_fit - Omega_r0_fit
rd_h_fit = released["profiled_rd_h_mpc"]
x_fit_recorded = shape["shape_outputs"]["x_crossing"]
h_crossing_over_h0_recorded = shape["shape_outputs"]["h_crossing_over_h0"]
age_factor_recorded = shape["shape_outputs"]["dimensionless_age_h0_t0"]


def fit_closure(x_value: float) -> float:
    ordinary = (
        Omega_m0_fit * math.exp(3.0 * x_value)
        + Omega_r0_fit * math.exp(4.0 * x_value)
    )
    return ordinary * sech2(x_value) - dark_fit


x_fit = bisect(fit_closure, 0.0, 1.0)
h_crossing_over_h0 = math.sqrt(2.0 * dark_fit / sech2(x_fit))
w0 = -1.0 + (2.0 / 3.0) * math.tanh(x_fit)
wa = -(2.0 / 3.0) * sech2(x_fit)

check(
    "fit and shape receipts use the same fractional radiation abundance",
    close(float(fit["protocol"]["omega_r"]), Omega_r0_fit),
    f"Omega_r0={Omega_r0_fit:.8g}",
)

check(
    "released-2025 flatness root is reproduced",
    close(x_fit, x_fit_recorded, 2.0e-13),
    f"x_c={x_fit:.12f}",
)
check(
    "released-2025 crossing ratio is reproduced",
    close(h_crossing_over_h0, h_crossing_over_h0_recorded, 2.0e-13),
    f"H_c/H0={h_crossing_over_h0:.12f}",
)
check(
    "parameter-free CPL signature",
    close(wa, 1.5 * (1.0 + w0) ** 2 - 2.0 / 3.0),
    f"w0={w0:.9f}; wa={wa:.9f}",
)

e2_present, first_present, second_present = e2_derivatives(
    0.0,
    Omega_m0_fit,
    Omega_r0_fit,
    x_fit,
)
q0 = -1.0 - 0.5 * first_present / e2_present
j0 = 1.0 + 1.5 * first_present / e2_present + 0.5 * second_present / e2_present
n_acceleration_entry = bisect(
    lambda n_value: deceleration(
        n_value,
        Omega_m0_fit,
        Omega_r0_fit,
        x_fit,
    ),
    -1.0,
    0.0,
)
n_acceleration_exit = bisect(
    lambda n_value: deceleration(
        n_value,
        Omega_m0_fit,
        Omega_r0_fit,
        x_fit,
    ),
    0.0,
    4.0,
)
z_acceleration_entry = math.exp(-n_acceleration_entry) - 1.0
a_acceleration_exit = math.exp(n_acceleration_exit)

check(
    "released-2025 kinematic forecasts are independently reproduced",
    within(q0, shape["shape_outputs"]["q0"], 2.0e-12)
    and within(j0, shape["shape_outputs"]["j0"], 2.0e-12)
    and within(
        z_acceleration_entry,
        shape["shape_outputs"]["acceleration_entry_z"],
        2.0e-12,
    )
    and within(
        a_acceleration_exit,
        shape["shape_outputs"]["acceleration_exit_a_over_a0"],
        2.0e-11,
    ),
    (
        f"q0={q0:.9f}; j0={j0:.9f}; z_in={z_acceleration_entry:.9f}; "
        f"a_out/a0={a_acceleration_exit:.7f}"
    ),
)


def fractional_root_function(
    x_value: float,
    Omega_m0: float,
    Omega_r0: float,
) -> float:
    ordinary = (
        Omega_m0 * math.exp(3.0 * x_value)
        + Omega_r0 * math.exp(4.0 * x_value)
    )
    return ordinary * sech2(x_value) - (1.0 - Omega_m0 - Omega_r0)


x_half = bisect(
    lambda value: fractional_root_function(value, 0.5, 0.0),
    -0.5,
    0.5,
)
x_post = bisect(
    lambda value: fractional_root_function(value, 0.3, 0.0),
    0.0,
    1.0,
)
x_pre = bisect(
    lambda value: fractional_root_function(value, 0.6, 0.0),
    -1.0,
    0.0,
)
check(
    "fractional flatness root changes sign only at half ordinary content",
    abs(x_half) < 1.0e-12 and x_post > 0.0 and x_pre < 0.0,
    f"x(sum=.5)={x_half:.3e}; x(.3)={x_post:.6f}; x(.6)={x_pre:.6f}",
)

delta_chi_square = released["chi_square"] - released_lcdm["chi_square"]
general_improvement = (
    generalized["fits"]["frozen_unit"]["chi_square"]
    - generalized["fits"]["nu_and_R_c_free"]["chi_square"]
)
delta_aic = generalized["information_criteria_relative_to_frozen_unit"][
    "nu_and_R_c_free"
]["delta_AIC_from_unit"]
unit_inside_joint_68 = generalized["unity_profile_membership"][
    "joint_two_parameter_point"
]["inside_nominal_delta_chi2_2_30"]

check(
    "released likelihood and generalized-family comparison",
    within(delta_chi_square, -3.31391098, 5.0e-8)
    and within(general_improvement, 1.89749492, 5.0e-8)
    and within(delta_aic, 2.10250508, 5.0e-8)
    and unit_inside_joint_68,
    (
        f"Delta_chi2={delta_chi_square:.7f}; improvement={general_improvement:.7f}; "
        f"Delta_AIC={delta_aic:.7f}; unit_in_68={unit_inside_joint_68}"
    ),
)

h_c_theory_si = crossing_rate_si(F_PI_PLUS_THEORY_PDG_MEV)
h_c_theory = km_s_mpc(h_c_theory_si)
h_c_experimental = km_s_mpc(crossing_rate_si(F_PI_PLUS_EXPERIMENTAL_PDG_MEV))
energy_theory = grain_energy_mev(F_PI_PLUS_THEORY_PDG_MEV)
f_pi_chi_theory_j = F_PI_PLUS_THEORY_PDG_MEV * MEV_J / math.sqrt(2.0)
xi_chi = (
    G_NEWTON
    * f_pi_chi_theory_j**3
    / (HBAR**2 * C**5 * h_c_theory_si)
)
lambda_theory = HBAR * C / (energy_theory * MEV_J)
planck_length = math.sqrt(HBAR * G_NEWTON / C**3)
radius_theory = C / h_c_theory_si
iota_theory = math.pi * radius_theory**2 / planck_length**2
cells_theory = (4.0 * math.pi / 3.0) * (radius_theory / lambda_theory) ** 3

check(
    "chiral and common-count closure agree",
    close(lambda_theory**3, (8.0 / 3.0) * planck_length**2 * radius_theory)
    and close(iota_theory, 2.0 * cells_theory),
    f"E*={energy_theory:.6f} MeV; ln(iota)={math.log(iota_theory):.6f}",
)
check(
    "two declared pion-response prescriptions remain distinct",
    within(h_c_theory, 81.80848, 5.0e-5)
    and within(h_c_experimental, 82.48895, 5.0e-5),
    f"Hc(theory)={h_c_theory:.5f}; Hc(experimental)={h_c_experimental:.5f}",
)
check(
    "dimensionless chiral oracle coefficient",
    close(xi_chi, 3.0),
    f"Xi_chi={xi_chi:.12f}",
)
prior_acoustic_h_c = 83.1058
prior_offset_fraction = (prior_acoustic_h_c - h_c_theory) / prior_acoustic_h_c
theory_h_c_fractional_sigma = (
    3.0 * F_PI_PLUS_THEORY_SIGMA_PDG_MEV / F_PI_PLUS_THEORY_PDG_MEV
)
check(
    "chiral oracle is distinct from but compatible with the prior acoustic diagnostic",
    within(prior_offset_fraction, 0.01561, 2.0e-5)
    and within(theory_h_c_fractional_sigma, 0.02765, 2.0e-5),
    (
        f"offset={100.0 * prior_offset_fraction:.3f}%; "
        f"theory cubic sigma={100.0 * theory_h_c_fractional_sigma:.3f}%"
    ),
)

# Protocol A: hold the released late-time fractional-composition fit fixed.
h0_protocol_a = h_c_theory / h_crossing_over_h0
rd_protocol_a = rd_h_fit / (h0_protocol_a / 100.0)
age_factor_protocol_a = age_factor(Omega_m0_fit, Omega_r0_fit, x_fit)
age_protocol_a = (
    age_factor_protocol_a
    / (h0_protocol_a * 1000.0 / MPC)
    / SECONDS_PER_GYR
)
linewidth_ev = HBAR * h_c_theory_si / EV_J
quality = energy_theory * 1.0e6 / linewidth_ev

check(
    "protocol A recomputes the recorded dimensionless age",
    within(age_factor_protocol_a, age_factor_recorded, 2.0e-8),
    f"recomputed={age_factor_protocol_a:.9f}; recorded={age_factor_recorded:.9f}",
)
check(
    "protocol A absolute oracle",
    within(h0_protocol_a, 67.76137, 5.0e-5)
    and within(rd_protocol_a, 146.5787, 5.0e-4)
    and within(age_protocol_a, 13.61602, 5.0e-5),
    (
        f"H0={h0_protocol_a:.5f}; rd={rd_protocol_a:.4f} Mpc; "
        f"t0={age_protocol_a:.5f} Gyr"
    ),
)


def h0_at_fractional_matter(Omega_m0: float) -> float:
    dark = 1.0 - Omega_m0 - Omega_r0_fit

    def closure(x_value: float) -> float:
        ordinary = (
            Omega_m0 * math.exp(3.0 * x_value)
            + Omega_r0_fit * math.exp(4.0 * x_value)
        )
        return ordinary * sech2(x_value) - dark

    x_value = bisect(closure, 0.0, 1.0)
    crossing_ratio = math.sqrt(2.0 * dark / sech2(x_value))
    return h_c_theory / crossing_ratio


Omega_m0_interval = released["omega_m_delta_chi2_1"]
h0_composition_endpoints = sorted(
    h0_at_fractional_matter(value) for value in Omega_m0_interval
)
h0_theory_sigma_linear = (
    h0_protocol_a
    * 3.0
    * F_PI_PLUS_THEORY_SIGMA_PDG_MEV
    / F_PI_PLUS_THEORY_PDG_MEV
)

check(
    "protocol A composition interval and theoretical-input propagation",
    within(h0_composition_endpoints[0], 67.13, 0.01)
    and within(h0_composition_endpoints[1], 68.40, 0.01)
    and within(h0_theory_sigma_linear, 1.874, 0.002),
    (
        f"H0 range={h0_composition_endpoints[0]:.3f}--"
        f"{h0_composition_endpoints[1]:.3f}; sigma_Fpi={h0_theory_sigma_linear:.3f}"
    ),
)
check(
    "conditional causal-line diagnostics",
    1.73e-33 < linewidth_ev < 1.77e-33 and 2.62e40 < quality < 2.66e40,
    f"Gamma={linewidth_ev:.4e} eV; Q={quality:.4e}",
)

# Protocol B: hold physical ordinary densities fixed and predict h.
physical_omega_m = 0.1430
physical_omega_r = 4.18e-5
h_c_dimensionless = h_c_theory / 100.0


def physical_density_closure(x_value: float) -> float:
    return (
        physical_omega_m * math.exp(3.0 * x_value)
        + physical_omega_r * math.exp(4.0 * x_value)
        - 0.5 * h_c_dimensionless**2
    )


x_physical = bisect(physical_density_closure, 0.0, 1.0)
h_squared = (
    physical_omega_m
    + physical_omega_r
    + 0.5 * h_c_dimensionless**2 * sech2(x_physical)
)
h_physical = math.sqrt(h_squared)
h0_physical = 100.0 * h_physical
Omega_m0_protocol_b = physical_omega_m / h_squared
Omega_r0_protocol_b = physical_omega_r / h_squared
w0_physical = -1.0 + (2.0 / 3.0) * math.tanh(x_physical)
wa_physical = -(2.0 / 3.0) * sech2(x_physical)
age_factor_physical = age_factor(
    Omega_m0_protocol_b,
    Omega_r0_protocol_b,
    x_physical,
)
age_physical = (
    age_factor_physical
    / (h0_physical * 1000.0 / MPC)
    / SECONDS_PER_GYR
)
z_physical = math.exp(x_physical) - 1.0
dark_physical_fraction = 1.0 - Omega_m0_protocol_b - Omega_r0_protocol_b
fractional_flatness_residual = (
    (
        Omega_m0_protocol_b * math.exp(3.0 * x_physical)
        + Omega_r0_protocol_b * math.exp(4.0 * x_physical)
    )
    * sech2(x_physical)
    - dark_physical_fraction
)

check(
    "protocol B closes the absolute background without H0 input",
    physical_omega_m + physical_omega_r < 0.5 * h_c_dimensionless**2
    and within(x_physical, 0.283266, 5.0e-7)
    and within(z_physical, 0.327458, 5.0e-7)
    and within(h0_physical, 67.24553, 5.0e-5)
    and within(Omega_m0_protocol_b, 0.316234, 5.0e-7)
    and abs(fractional_flatness_residual) < 1.0e-13,
    (
        f"x_c={x_physical:.6f}; z_c={z_physical:.6f}; "
        f"H0={h0_physical:.5f}; Omega_m={Omega_m0_protocol_b:.6f}"
    ),
)
check(
    "protocol B equation-of-state and age outputs",
    within(w0_physical, -0.816050, 5.0e-7)
    and within(wa_physical, -0.615910, 5.0e-7)
    and within(age_factor_physical, 0.947877, 5.0e-7)
    and within(age_physical, 13.78272, 5.0e-5),
    (
        f"w0={w0_physical:.6f}; wa={wa_physical:.6f}; "
        f"H0*t0={age_factor_physical:.6f}; t0={age_physical:.5f} Gyr"
    ),
)


def protocol_b_h0(f_pi_pdg_mev: float) -> float:
    h_c_value = km_s_mpc(crossing_rate_si(f_pi_pdg_mev))
    h_c_value_dimensionless = h_c_value / 100.0

    def closure(x_value: float) -> float:
        return (
            physical_omega_m * math.exp(3.0 * x_value)
            + physical_omega_r * math.exp(4.0 * x_value)
            - 0.5 * h_c_value_dimensionless**2
        )

    x_value = bisect(closure, 0.0, 1.0)
    h_value_squared = (
        physical_omega_m
        + physical_omega_r
        + 0.5 * h_c_value_dimensionless**2 * sech2(x_value)
    )
    return 100.0 * math.sqrt(h_value_squared)


h0_protocol_b_low = protocol_b_h0(
    F_PI_PLUS_THEORY_PDG_MEV - F_PI_PLUS_THEORY_SIGMA_PDG_MEV
)
h0_protocol_b_high = protocol_b_h0(
    F_PI_PLUS_THEORY_PDG_MEV + F_PI_PLUS_THEORY_SIGMA_PDG_MEV
)
h0_protocol_b_sigma = 0.5 * (h0_protocol_b_high - h0_protocol_b_low)

physical_threshold = 2.0 * (physical_omega_m + physical_omega_r)
check(
    "protocol B root domain and theoretical-input propagation",
    abs(
        physical_omega_m
        + physical_omega_r
        - 0.5 * physical_threshold
    )
    < 1.0e-15
    and (
        physical_omega_m
        + physical_omega_r
        - 0.5 * (0.99 * physical_threshold)
    )
    > 0.0
    and within(h0_protocol_b_sigma, 1.04, 0.03),
    (
        f"equality_root=0; reversed_f(0)>0; "
        f"H0 endpoints={h0_protocol_b_low:.3f}--{h0_protocol_b_high:.3f}; "
        f"half-span={h0_protocol_b_sigma:.3f}"
    ),
)

if failures:
    print("FAILURES: " + ", ".join(failures))
    sys.exit(1)

print("ALL RECEIPTS PASS")
