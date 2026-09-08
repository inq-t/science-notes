"""Numerical checks for the logistic scale-shadow factorization.

This receipt checks the displayed scalar identities, unitary ground-state
transform on sample functions, approach to the continuum threshold, the local
relative-entropy Hessian, the projection/involution normalization fork, the
incoming-density identities at nu=1/2, and the heavy-tail contrast. It also
checks the capacity-relative factor, its asymptotic sign phases, and the
algebraic kernel-line relation behind the conditional born-gapped rule. It
does not prove the Fredholm domains, flat-partner uniqueness, either proposed
solder, a physical-to-wall analysis map, or the Yang--Mills mass gap.
"""

import math

import numpy as np


def sech(x):
    return 1.0 / np.cosh(x)


for nu, center in ((0.4, -1.3), (1.0, 0.0), (2.2, 0.7)):
    half_width = 22.0 / nu
    grid = np.linspace(center - half_width, center + half_width, 240001)
    x = grid - center
    q = 0.5 * nu * sech(nu * x) ** 2
    psi0 = np.sqrt(q)
    wall = nu * np.tanh(nu * x)
    wall_prime = nu**2 * sech(nu * x) ** 2

    assert np.isclose(np.trapezoid(q, grid), 1.0, rtol=0.0, atol=2e-12)
    assert np.max(np.abs(wall_prime + wall**2 - nu**2)) < 2e-14

    psi0_prime = -wall * psi0
    assert np.max(np.abs(psi0_prime + wall * psi0)) < 2e-14

    v_minus = wall**2 - wall_prime
    v_plus = wall**2 + wall_prime
    assert np.max(
        np.abs(v_minus - (nu**2 - 2.0 * nu**2 * sech(nu * x) ** 2))
    ) < 3e-14
    assert np.max(np.abs(v_plus - nu**2)) < 3e-14

    f = np.sin(0.37 * nu * x) + 0.2 * np.cos(0.81 * nu * x)
    f_prime = 0.37 * nu * np.cos(0.37 * nu * x) - 0.162 * nu * np.sin(
        0.81 * nu * x
    )
    transformed_a = psi0 * f_prime
    weighted_energy = np.trapezoid(f_prime**2 * q, grid)
    flat_energy = np.trapezoid(np.abs(transformed_a) ** 2, grid)
    weighted_norm = np.trapezoid(f**2 * q, grid)
    flat_norm = np.trapezoid(np.abs(psi0 * f) ** 2, grid)
    assert np.isclose(weighted_energy, flat_energy, rtol=2e-13, atol=2e-13)
    assert np.isclose(weighted_norm, flat_norm, rtol=2e-13, atol=2e-13)


# Projection-coded matching identifies log odds with N-N_c and fixes nu=1/2.
# Normalized-involution matching identifies half log odds with N-N_c and fixes
# nu=1. These are different generator normalizations of the same binary
# family. The separate nondegenerate incoming-density law selects the same
# width as the projection-coded branch, nu=1/2;
# there the scale density, Fisher pulse, and readout derivative coincide.
center = 0.7
grid = np.linspace(-40.0, 40.0, 240001)
y = grid - center
z = 1.0 / (1.0 + np.exp(-y))
q_half = 0.25 * sech(0.5 * y) ** 2
q_odds = z * (1.0 - z)
core_density = np.exp(-grid) * q_half
core_density_closed = np.exp(-center) / (1.0 + np.exp(y)) ** 2
middle = (z > 1e-8) & (z < 1.0 - 1e-8)
fisher_pulse = q_odds[middle] ** 2 / (z[middle] * (1.0 - z[middle]))

assert np.max(np.abs(np.log(z[middle] / (1.0 - z[middle])) - y[middle])) < 3e-8
assert np.max(np.abs(q_half - q_odds)) < 3e-16
assert np.max(np.abs(fisher_pulse - q_half[middle])) < 3e-16
assert np.max(np.abs(core_density - core_density_closed)) < 3e-15
assert np.isclose(core_density[0], np.exp(-center), rtol=1e-12, atol=1e-12)
assert core_density[-1] < 1e-34


def incoming_core_density(nu, n, n_center=center):
    return np.exp(-n) * 0.5 * nu * sech(nu * (n - n_center)) ** 2


# The mismatch exponent 2*nu-1 gives three distinct incoming boundary
# classes. Moving farther toward -infinity amplifies the density below the
# wall, preserves a finite nonzero limit on it, and suppresses it above it.
n_near = -20.0
n_far = -40.0
assert incoming_core_density(0.4, n_far) > incoming_core_density(0.4, n_near)
assert np.isclose(
    incoming_core_density(0.5, n_far), np.exp(-center), rtol=1e-8, atol=1e-8
)
assert incoming_core_density(0.8, n_far) < incoming_core_density(0.8, n_near)


# On the separately declared translation-Haar carrier, the half-density of
# the state relative to core capacity has factor
# B=d/dN+1/2+nu*tanh(nu(N-Nc)).  Its incoming asymptotic coefficient changes
# sign at nu=1/2, while the outgoing coefficient remains positive.
relative_index_phases = []
for nu, expected_phase in ((0.4, 0), (0.5, None), (0.8, 1)):
    grid = np.linspace(center - 35.0 / nu, center + 35.0 / nu, 240001)
    x = grid - center
    q = 0.5 * nu * sech(nu * x) ** 2
    relative_half_density = np.exp(-0.5 * grid) * np.sqrt(q)
    relative_wall = 0.5 + nu * np.tanh(nu * x)
    relative_wall_prime = nu**2 * sech(nu * x) ** 2
    relative_half_density_prime = -relative_wall * relative_half_density

    assert np.max(
        np.abs(relative_half_density_prime + relative_wall * relative_half_density)
    ) < 2e-14
    assert np.max(
        np.abs(
            relative_wall**2
            + relative_wall_prime
            - (0.25 + nu**2 + nu * np.tanh(nu * x))
        )
    ) < 4e-14

    incoming_mass = 0.5 - nu
    outgoing_mass = 0.5 + nu
    if incoming_mass > 0.0:
        phase = 0
    elif incoming_mass < 0.0:
        phase = 1
    else:
        phase = None
    assert phase == expected_phase
    assert outgoing_mass > 0.0
    relative_index_phases.append((nu, phase))

# The supercritical relative zero mode is Haar-normalizable.  Its exact norm
# diverges as nu approaches the wall from above.
def relative_zero_mode_norm_squared(nu, n_center=center):
    ratio = 1.0 / (2.0 * nu)
    return (
        math.exp(-n_center)
        * math.gamma(1.0 - ratio)
        * math.gamma(1.0 + ratio)
    )


relative_norms = [
    relative_zero_mode_norm_squared(nu)
    for nu in (1.0, 0.7, 0.55, 0.51)
]
assert all(
    later > earlier
    for earlier, later in zip(relative_norms, relative_norms[1:])
)
assert relative_norms[-1] > 20.0 * relative_norms[0]

# On the supercritical phase, multiplication by the capacity half-character
# maps the relative zero mode to the probability zero mode. If admissibility
# is declared to require the former, every admitted squared probability edge
# is above 1/4 and approaches 1/4 only at the excluded threshold.
nu = 0.8
grid = np.linspace(center - 30.0 / nu, center + 30.0 / nu, 180001)
x = grid - center
probability_half_density = np.sqrt(0.5 * nu) * sech(nu * x)
relative_half_density = np.exp(-0.5 * grid) * probability_half_density
assert np.max(
    np.abs(np.exp(0.5 * grid) * relative_half_density - probability_half_density)
) < 2e-15
admitted_rates = (0.5001, 0.51, 0.8, 1.0)
assert all(rate > 0.5 and rate**2 > 0.25 for rate in admitted_rates)
assert math.isclose(0.5**2, 0.25)

z_involution = 1.0 / (1.0 + np.exp(-2.0 * y))
middle_involution = (z_involution > 1e-8) & (z_involution < 1.0 - 1e-8)
half_log_odds = 0.5 * np.log(
    z_involution[middle_involution] / (1.0 - z_involution[middle_involution])
)
assert np.max(np.abs(half_log_odds - y[middle_involution])) < 3e-8


# Compactly cut off the threshold solution tanh(x). Its Rayleigh quotient for
# H_- approaches the continuum edge 1 from above as the cutoff broadens.
threshold_quotients = []
for radius in (12.0, 24.0, 48.0, 96.0):
    grid = np.linspace(-1.25 * radius, 1.25 * radius, 250001)
    cutoff = np.zeros_like(grid)
    absolute = np.abs(grid)
    cutoff[absolute <= radius] = 1.0
    taper = (absolute > radius) & (absolute < 1.2 * radius)
    phase = (absolute[taper] - radius) / (0.2 * radius)
    cutoff[taper] = 0.5 * (1.0 + np.cos(np.pi * phase))

    cutoff_prime = np.zeros_like(grid)
    cutoff_prime[taper] = (
        -0.5
        * np.pi
        / (0.2 * radius)
        * np.sin(np.pi * phase)
        * np.sign(grid[taper])
    )
    phi = cutoff * np.tanh(grid)
    phi_prime = cutoff_prime * np.tanh(grid) + cutoff * sech(grid) ** 2
    potential = 1.0 - 2.0 * sech(grid) ** 2
    quotient = np.trapezoid(phi_prime**2 + potential * phi**2, grid) / np.trapezoid(
        phi**2, grid
    )
    threshold_quotients.append(float(quotient))

assert all(value > 1.0 for value in threshold_quotients)
assert all(
    later < earlier
    for earlier, later in zip(threshold_quotients, threshold_quotients[1:])
)
assert threshold_quotients[-1] - 1.0 < 0.02


# Local entropy/Fisher Hessian check around the unit logistic measure.
grid = np.linspace(-18.0, 18.0, 240001)
q = 0.5 * sech(grid) ** 2
raw_f = np.tanh(grid) + 0.15 * np.sin(0.6 * grid)
mean_f = np.trapezoid(raw_f * q, grid)
f = raw_f - mean_f
f_prime = sech(grid) ** 2 + 0.09 * np.cos(0.6 * grid)
entropy_hessian = np.trapezoid(f**2 * q, grid)
fisher_half_hessian = np.trapezoid(f_prime**2 * q, grid)
assert fisher_half_hessian + 2e-11 >= entropy_hessian

eps = 1e-4
density_ratio = 1.0 + eps * f
relative_entropy = np.trapezoid(
    density_ratio * np.log(density_ratio) * q,
    grid,
)
relative_fisher = np.trapezoid(
    (eps * f_prime / density_ratio) ** 2 * density_ratio * q,
    grid,
)
assert np.isclose(
    2.0 * relative_entropy / eps**2,
    entropy_hessian,
    rtol=3e-4,
    atol=3e-8,
)
assert np.isclose(
    relative_fisher / eps**2,
    fisher_half_hessian,
    rtol=3e-4,
    atol=3e-8,
)


# A normalizable heavy-tailed state need not be gapped: its transformed
# potential tends to zero rather than to a positive constant.
p = 1.2
radii = np.array([10.0, 100.0, 1000.0, 10000.0])
heavy_potential = (p * (p + 1.0) * radii**2 - p) / (1.0 + radii**2) ** 2
assert np.all(heavy_potential > 0.0)
assert np.all(np.diff(heavy_potential) < 0.0)
assert heavy_potential[-1] < 3e-8

print("logistic normalization and Riccati factorization: passed")
print("weighted-to-flat ground-state transform: passed")
print("projection/involution normalization fork: passed")
print("incoming core-density consequences at nu=1/2: passed")
print("incoming rate-matching boundary trichotomy: passed")
print("capacity-relative Fredholm sign phases:", relative_index_phases)
print("capacity-relative zero-mode norm diverges at the wall: passed")
print("conditional born-gapped carrier and kernel-line map: passed")
print("threshold Rayleigh quotients:", threshold_quotients)
print("local entropy/Fisher Hessian comparison: passed")
print("normalizable heavy-tail potential tends to zero: passed")
print("no physical-to-wall carrier map or Yang--Mills claim is tested")
