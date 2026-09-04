from math import exp, isclose, log, pi


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


print("GENERALIZED_RATE_EDGE_BENCHMARK_PASSED")
print("CATEGORICAL_DEPTH_LADDER_IDENTITIES_PASSED")
print("INDEPENDENT_AGE_CALIBRATION_IDENTITY_PASSED")
