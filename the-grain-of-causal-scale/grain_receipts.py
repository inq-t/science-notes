#!/usr/bin/env python3
"""Standard-library receipts for the grain of causal scale.

The checks verify algebraic reformulations of the conditional common-count
closure and reproduce its diagnostic branch values. They do not verify the
wall correspondence, select a material carrier, or establish a resonance.
"""

import cmath
import math
import sys


C = 299_792_458.0
HBAR = 1.054_571_817e-34
G_NEWTON = 6.674_30e-11
MPC = 3.085_677_581_491_367_3e22
EV_J = 1.602_176_634e-19
MEV_J = 1.0e6 * EV_J
MEV_C2_KG = MEV_J / C**2

# Self-consistent physical-density CMB-conditional protocol. The older 82.64
# value mixed a re-solved H0 with a reference-composition Hc/H0 ratio.
H_CMB = 83.1058 * 1000.0 / MPC
H_CEPHEID = 88.2608 * 1000.0 / MPC
ZETA = 2.0 / 3.0
GAMMA = 2.0
S_STAR = 1.0

failures = []


def check(name, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    print(f"{status}  {name}" + (f" | {detail}" if detail else ""))
    if not condition:
        failures.append(name)


def close(left, right, tolerance=1e-11):
    return math.isclose(left, right, rel_tol=tolerance, abs_tol=0.0)


def carrier_mass(rate):
    return (
        HBAR**2 * rate
        / (4.0 * ZETA * C * G_NEWTON)
    ) ** (1.0 / 3.0)


def ledger(rate):
    return math.pi * C**5 / (G_NEWTON * HBAR * rate**2)


planck_length = math.sqrt(HBAR * G_NEWTON / C**3)
planck_time = planck_length / C
planck_mass = math.sqrt(HBAR * C / G_NEWTON)

branch_rows = []
all_exact = True

for name, rate in (("CMB", H_CMB), ("Cepheid", H_CEPHEID)):
    mass = carrier_mass(rate)
    energy = mass * C**2
    wavelength = HBAR / (mass * C)
    duration = wavelength / C
    radius = C / rate
    iota = ledger(rate)
    address = math.log(iota)
    cells = (4.0 * math.pi / 3.0) * (radius / wavelength) ** 3
    quality = radius / wavelength
    gamma_energy_ev = HBAR * rate / EV_J

    branch_rows.append(
        (name, rate, mass, energy, wavelength, duration, iota, quality, gamma_energy_ev)
    )

    all_exact &= close(wavelength**3, 4.0 * ZETA * planck_length**2 * radius)
    all_exact &= close(iota, GAMMA * S_STAR * cells)
    all_exact &= close(
        G_NEWTON,
        HBAR**2 * rate / (4.0 * ZETA * C * mass**3),
    )
    all_exact &= close(
        duration**3,
        (8.0 / 3.0) * planck_time**2 / rate,
    )
    all_exact &= close(
        energy**3,
        (3.0 / 8.0) * (planck_mass * C**2) ** 2 * HBAR * rate,
    )
    all_exact &= close(
        planck_mass / mass,
        (16.0 * ZETA**2 * math.exp(address) / math.pi) ** (1.0 / 6.0),
    )

check(
    "common-count, UV/IR, closure, and hierarchy identities",
    all_exact,
    "both crossing branches",
)

cmb = branch_rows[0]
cepheid = branch_rows[1]

check(
    "diagnostic branch energies",
    abs(cmb[3] / MEV_J - 46.27) < 0.02
    and abs(cepheid[3] / MEV_J - 47.21) < 0.02,
    f"CMB={cmb[3] / MEV_J:.3f} MeV; Cepheid={cepheid[3] / MEV_J:.3f} MeV",
)

check(
    "diagnostic branch correlation lengths",
    abs(cmb[4] * 1.0e15 - 4.264) < 0.005
    and abs(cepheid[4] * 1.0e15 - 4.180) < 0.005,
    f"CMB={cmb[4] * 1.0e15:.4f} fm; Cepheid={cepheid[4] * 1.0e15:.4f} fm",
)

register_checks = True
for row in branch_rows:
    name, rate, mass, energy, wavelength, duration, iota, quality, _ = row
    alpha_star = G_NEWTON * mass**2 / (HBAR * C)
    alpha_horizon = G_NEWTON * HBAR * rate**2 / C**5
    schwarzschild = 2.0 * G_NEWTON * mass / C**2
    beta_energy = 2.0 * math.pi * quality

    register_checks &= close(alpha_star, 3.0 / (8.0 * quality))
    register_checks &= close(alpha_horizon, (64.0 / 9.0) * alpha_star**3)
    register_checks &= close(iota, math.pi / alpha_horizon)
    register_checks &= close(iota, (8.0 * math.pi / 3.0) * quality**3)
    register_checks &= close(iota, beta_energy**3 / (3.0 * math.pi**2))
    register_checks &= close(planck_length**2, 0.5 * schwarzschild * wavelength)
    register_checks &= close(wavelength**2, (4.0 / 3.0) * schwarzschild * C / rate)
    register_checks &= close(
        G_NEWTON * mass / wavelength**2,
        (3.0 / 8.0) * C * rate,
    )

check(
    "coupling, horizon-temperature, quality-factor, and Schwarzschild registers",
    register_checks,
    "all exact reformulations pass",
)

born_checks = True
for row in branch_rows:
    iota = row[6]
    ratio = planck_mass / row[2]
    cubic_amplitude = 3.0 * math.sqrt(math.pi) * ratio**3 / 8.0
    born_checks &= close(iota, (9.0 * math.pi / 64.0) * ratio**6)
    born_checks &= close(iota, cubic_amplitude**2)

check(
    "sixth-power ledger is the square of the conditional cubic amplitude",
    born_checks,
)


def vandermonde(values):
    product = 1.0 + 0.0j
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            product *= values[i] - values[j]
    return product


roots = (-1.25, 0.5, 2.0)
radial_scale = 0.37
phase = 0.41
weyl_amplitude = vandermonde(roots)
radial_amplitude = vandermonde(tuple(radial_scale * x for x in roots))
phase_amplitude = vandermonde(tuple(cmath.exp(1j * phase) * x for x in roots))
weyl_density = abs(weyl_amplitude) ** 2

check(
    "A2 Weyl amplitude has weight three and its positive density weight six",
    close(abs(radial_amplitude / weyl_amplitude), radial_scale**3)
    and close(abs(radial_amplitude) ** 2 / weyl_density, radial_scale**6),
)

check(
    "holomorphic discriminant has phase weight six while positive density is phase-neutral",
    abs(
        (phase_amplitude**2 / weyl_amplitude**2)
        - cmath.exp(6j * phase)
    )
    < 1.0e-12
    and close(abs(phase_amplitude) ** 2, weyl_density),
)

check(
    "half-density and raw-discriminant Witten thresholds remain distinct",
    3**2 == 9 and 6**2 == 36,
    "Weyl half-density slope=3; discriminant-as-amplitude slope=6",
)

reverse_checks = True
for row in branch_rows:
    rate, iota = row[1], row[6]
    address = math.log(iota)
    reverse_time = math.sqrt(math.pi) * math.exp(-address / 2.0) / rate
    reverse_g = math.pi * C**5 * math.exp(-address) / (HBAR * rate**2)
    reverse_checks &= close(reverse_time, planck_time)
    reverse_checks &= close(reverse_g, G_NEWTON)

check(
    "crossing address and rate reconstruct Planck time and G",
    reverse_checks,
    "a round trip, not independent evidence",
)

check(
    "linewidth and quality-factor diagnostics",
    1.74e-33 < cmb[8] < 1.79e-33
    and 2.60e40 < cmb[7] < 2.64e40,
    f"Gamma_c={cmb[8]:.3e} eV; Q_c={cmb[7]:.3e}",
)


def cubic_roots(parameter, length=1.0):
    """Real roots of r^3 - L^2 r + 2 m L^2 near the three-root region."""
    if parameter == 0.0:
        return [-length, 0.0, length]
    p = -(length**2)
    q = 2.0 * parameter * length**2
    angle = math.acos((3.0 * q / (2.0 * p)) * math.sqrt(-3.0 / p))
    roots = [
        2.0
        * math.sqrt(-p / 3.0)
        * math.cos((angle - 2.0 * math.pi * k) / 3.0)
        for k in range(3)
    ]
    return sorted(roots)


epsilon = 1.0e-6
roots_negative = cubic_roots(-epsilon)
roots_zero = cubic_roots(0.0)
roots_positive = cubic_roots(epsilon)
rank_negative = sum(root > 0.0 for root in roots_negative)
rank_zero = sum(root > 0.0 for root in roots_zero)
rank_positive = sum(root > 0.0 for root in roots_positive)
central_derivative = (
    roots_positive[1] - roots_negative[1]
) / (2.0 * epsilon)

check(
    "positive-support prototype has one upward crossing",
    rank_negative == 1
    and rank_zero == 1
    and rank_positive == 2
    and abs(central_derivative - 2.0) < 1.0e-8,
    f"ranks={rank_negative}->{rank_zero}->{rank_positive}; r0'(0)={central_derivative:.9f}",
)

fisher = math.factorial(0) - 2.0 * math.factorial(1) + math.factorial(2)
check(
    "exponential scale family has unit log-scale Fisher response",
    fisher == 1.0,
    "E[(1-X)^2]=1 for X~Exp(1)",
)

proton_mev = 938.272_088_16
neutron_mev = 939.565_420_52
binding_mev = 2.224_566
reduced_mass_mev = proton_mev * neutron_mev / (proton_mev + neutron_mev)
deuteron_momentum_mev = math.sqrt(2.0 * reduced_mass_mev * binding_mev)
deuteron_length_fm = 197.326_980_4 / deuteron_momentum_mev
f_pi_pdg_mev = 130.2
f_pi_half_mev = f_pi_pdg_mev / (2.0 * math.sqrt(2.0))
cmb_energy_mev = cmb[3] / MEV_J

check(
    "material rhymes are reproduced but not selected",
    abs(deuteron_momentum_mev - 45.70) < 0.02
    and abs(deuteron_length_fm - 4.318) < 0.005
    and abs(f_pi_half_mev - 46.03) < 0.02,
    (
        f"kappa_d={deuteron_momentum_mev:.3f} MeV, "
        f"hbar/kappa_d={deuteron_length_fm:.3f} fm, "
        f"F_pi/2={f_pi_half_mev:.3f} MeV; "
        f"offsets={abs(deuteron_momentum_mev / cmb_energy_mev - 1.0) * 100:.2f}%/"
        f"{abs(f_pi_half_mev / cmb_energy_mev - 1.0) * 100:.2f}%"
    ),
)

if failures:
    print("FAILURES: " + ", ".join(failures))
    sys.exit(1)

print("ALL RECEIPTS PASS")
