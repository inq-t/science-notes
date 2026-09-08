from math import exp, isclose, log, pi

import numpy as np


def close(left, right, tolerance=2e-13):
    return isclose(left, right, rel_tol=tolerance, abs_tol=tolerance)


# Finite diagonal benchmark for the generalized Rayleigh-edge theorem.
hubble = 0.27
local_rates = (1.4, 0.83, 2.1)
q_rate = min(rate / hubble for rate in local_rates)
assert close(q_rate, 0.83 / hubble)

hbar = 1.7
solder = 0.61
energy_rates = tuple(solder * rate + extra for rate, extra in zip(local_rates, (0.2, 0.0, 0.5)))
energy_floor = hbar * min(energy_rates)
assert energy_floor + 1e-14 >= hbar * solder * hubble * q_rate


# Categorical-depth/cosmic-capacity ladder. The weld itself is a premise;
# these checks exercise only its exact downstream algebra.
for dimension, rung, capacity_birth, gamma, cell_weight in (
    (2.0, 7, 1.0, 2.0, 1.0),
    (1.37, 11, 3.2, 1.4, 0.8),
):
    categorical_index = dimension ** (2 * rung)
    capacity = capacity_birth * categorical_index
    depth = log(capacity / capacity_birth)
    assert close(depth, 2 * rung * log(dimension))

    hubble_birth = 0.73
    hubble_rung = hubble_birth * dimension ** (-rung)
    assert close(
        log(hubble_birth / hubble_rung),
        rung * log(dimension),
    )
    assert close(capacity / capacity_birth, (hubble_birth / hubble_rung) ** 2)

    q_birth = (3 * capacity_birth / (4 * pi * gamma * cell_weight)) ** (1 / 3)
    q_rung = (3 * capacity / (4 * pi * gamma * cell_weight)) ** (1 / 3)
    assert close(q_rung / q_birth, dimension ** (2 * rung / 3))

    omega_birth = hubble_birth * q_birth
    omega_rung = hubble_rung * q_rung
    assert close(omega_rung / omega_birth, dimension ** (-rung / 3))


# Constant-epsilon benchmark for the independent proper-age calibration.
epsilon = 0.72
delta_n = 4.1
integrated_depth = epsilon * delta_n
age_shape = (exp(integrated_depth) - 1) / epsilon
proper_duration = 9.3
hubble_birth = age_shape / proper_duration
hubble_cut = hubble_birth * exp(-integrated_depth)
assert close(proper_duration, age_shape / hubble_birth)
assert close(log(hubble_birth / hubble_cut), integrated_depth)


def relative_spectrum(response, metric):
    """Eigenvalues of a finite response relative to a positive metric."""
    factor = np.linalg.cholesky(metric)
    reduced = np.linalg.solve(factor, response) @ np.linalg.inv(factor.T)
    assert np.allclose(reduced, reduced.T)
    return np.linalg.eigvalsh(reduced)


# Dimensionless coordinate changes alter the raw Hessian spectrum.
response = np.diag([3.0, 8.0])
metric = np.eye(2)
chart = np.diag([2.0, 0.5])
pulled_response = chart.T @ response @ chart
pulled_metric = chart.T @ metric @ chart
assert np.allclose(np.linalg.eigvalsh(pulled_response), [2.0, 12.0])
assert np.allclose(relative_spectrum(pulled_response, pulled_metric), [3.0, 8.0])

rng = np.random.default_rng(731)
for _ in range(12):
    chart = np.eye(2) + 0.15 * rng.normal(size=(2, 2))
    assert abs(np.linalg.det(chart)) > 0.1
    assert np.allclose(
        relative_spectrum(chart.T @ response @ chart, chart.T @ metric @ chart),
        [3.0, 8.0],
    )
assert np.allclose(relative_spectrum(7 * response, 2 * metric), [10.5, 28.0])


# Coverage without norm control does not transfer an upstream unit floor.
epsilon = 0.013
physical_energy = np.diag([epsilon, 4.0])
carrier_map = np.diag([epsilon ** -0.5, 0.5])
upstream_response = np.eye(2)
physical_pullback = carrier_map.T @ carrier_map
assert np.allclose(carrier_map.T @ physical_energy @ carrier_map, upstream_response)
assert min(np.linalg.eigvalsh(physical_energy)) < min(np.linalg.eigvalsh(upstream_response))
assert np.allclose(
    relative_spectrum(upstream_response, physical_pullback),
    np.linalg.eigvalsh(physical_energy),
)


# Einstein area compliance and reduced-Compton reference area: pure identities.
for hbar, c, gravity, mass in ((1.7, 2.3, 0.41, 0.19), (0.73, 5.1, 1.4, 2.2)):
    area_compliance = 4 * hbar * gravity / c ** 3
    spectral_edge = mass * c / hbar
    compton_ledger = 1 / (spectral_edge ** 2 * area_compliance)
    gravity_ratio = gravity * mass ** 2 / (hbar * c)
    xi = area_compliance * spectral_edge ** 2
    assert close(xi, 4 * gravity_ratio)
    assert close(xi, 1 / compton_ledger)
    assert close(gravity_ratio, 1 / (4 * compton_ledger))
    assert area_compliance * (0.7 * spectral_edge) ** 2 < xi
    for length_scale, time_scale, mass_scale in ((2.0, 3.0, 5.0), (0.4, 1.7, 0.3)):
        c_new = c * length_scale / time_scale
        hbar_new = hbar * mass_scale * length_scale ** 2 / time_scale
        gravity_new = gravity * length_scale ** 3 / (mass_scale * time_scale ** 2)
        mass_new = mass * mass_scale
        area_new = 4 * hbar_new * gravity_new / c_new ** 3
        edge_new = mass_new * c_new / hbar_new
        assert close(area_new, length_scale ** 2 * area_compliance)
        assert close(edge_new, spectral_edge / length_scale)
        assert close(area_new * edge_new ** 2, xi)


print("GENERALIZED_RATE_EDGE_BENCHMARK_PASSED")
print("CATEGORICAL_DEPTH_LADDER_IDENTITIES_PASSED")
print("INDEPENDENT_AGE_CALIBRATION_IDENTITY_PASSED")
print("RELATIVE_RESPONSE_COORDINATE_AND_NORMALIZATION_TESTS_PASSED")
print("CARRIER_MAP_NORM_COUNTEREXAMPLE_AND_REPAIR_PASSED")
print("ENTROPY_COMPTON_FACTOR_FOUR_AND_UNIT_COVARIANCE_PASSED")
print("Not tested: a physical response weld, a derived yardstick, continuum existence, or Yang--Mills mass gap.")
