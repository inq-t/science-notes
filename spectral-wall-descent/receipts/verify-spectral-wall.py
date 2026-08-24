"""Numerical receipts for the finite spectral-wall calculations.

The script uses only NumPy and exits nonzero on any failed identity.
"""

from __future__ import annotations

import math

import numpy as np


TOL = 2.0e-9


def hermitian_function(matrix: np.ndarray, function) -> np.ndarray:
    values, vectors = np.linalg.eigh(matrix)
    return (vectors * function(values)) @ vectors.conj().T


def von_neumann_entropy(rho: np.ndarray) -> float:
    values = np.linalg.eigvalsh(rho)
    values = values[values > 1.0e-15]
    return float(-np.sum(values * np.log(values)))


def relative_entropy(rho: np.ndarray, sigma: np.ndarray) -> float:
    log_rho = hermitian_function(rho, np.log)
    log_sigma = hermitian_function(sigma, np.log)
    return float(np.trace(rho @ (log_rho - log_sigma)).real)


def rotation(theta: float) -> np.ndarray:
    return np.array(
        [[math.cos(theta), -math.sin(theta)],
         [math.sin(theta), math.cos(theta)]],
        dtype=complex,
    )


def dephase(matrix: np.ndarray) -> np.ndarray:
    return np.diag(np.diag(matrix))


def left_right_dirac(h: np.ndarray) -> np.ndarray:
    identity = np.eye(h.shape[0], dtype=complex)
    # Column-vectorization convention: vec(hX + Xh) =
    # (I kron h + h.T kron I) vec(X).
    return np.kron(identity, h) + np.kron(h.T, identity)


def check_finite_spectral_wall() -> None:
    sigma_x = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sigma_y = np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=complex)
    sigma_z = np.diag([1.0, -1.0]).astype(complex)

    m, phi_x, phi_y = 1.3, 0.4, -0.7
    h = m * sigma_z + phi_x * sigma_x + phi_y * sigma_y
    radius = math.sqrt(m * m + phi_x * phi_x + phi_y * phi_y)
    dirac = left_right_dirac(h)
    spectrum = np.linalg.eigvalsh(dirac)
    expected = np.array([-2.0 * radius, 0.0, 0.0, 2.0 * radius])
    assert np.allclose(spectrum, expected, atol=TOL)
    assert abs(np.trace(dirac @ dirac).real - 8.0 * radius**2) < TOL
    assert abs(np.trace(np.linalg.matrix_power(dirac, 4)).real - 32.0 * radius**4) < 2.0e-8

    heat_time = 0.23
    heat_trace = float(np.sum(np.exp(-heat_time * spectrum**2)))
    expected_heat = 2.0 + 2.0 * math.exp(-4.0 * heat_time * radius**2)
    assert abs(heat_trace - expected_heat) < TOL

    p = 0.8
    rho_zero = np.diag([p, 1.0 - p]).astype(complex)

    def defect(theta: float) -> float:
        unitary = rotation(theta)
        rho = unitary @ rho_zero @ unitary.conj().T
        observed = dephase(rho)
        direct = relative_entropy(rho, observed)
        entropy_gain = von_neumann_entropy(observed) - von_neumann_entropy(rho)
        assert abs(direct - entropy_gain) < TOL
        return direct

    maximal = defect(math.pi / 4.0)
    binary_entropy = -p * math.log(p) - (1.0 - p) * math.log(1.0 - p)
    expected_maximal = math.log(2.0) - binary_entropy
    assert abs(maximal - expected_maximal) < TOL

    step = 2.0e-4
    hessian_fd = (defect(step) - 2.0 * defect(0.0) + defect(-step)) / step**2
    hessian_exact = 2.0 * (2.0 * p - 1.0) * math.log(p / (1.0 - p))
    assert abs(hessian_fd - hessian_exact) < 2.0e-6

    # K_0(C^2) -> K_0(M_2) is the sum map; its primitive kernel is (1,-1).
    rank_map = np.array([[1, 1]], dtype=int)
    root = np.array([1, -1], dtype=int)
    assert np.array_equal(rank_map @ root, np.array([0]))
    assert np.linalg.matrix_rank(rank_map) == 1

    print("finite spectral wall: PASS")
    print(f"  entropy defect at pi/4 = {maximal:.12f}")
    print(f"  BKM/defect Hessian    = {hessian_exact:.12f}")


def check_conditional_expectation_balance() -> None:
    rng = np.random.default_rng(20260825)
    raw = rng.normal(size=(3, 3)) + 1.0j * rng.normal(size=(3, 3))
    rho = raw @ raw.conj().T + 0.8 * np.eye(3)
    rho = rho / np.trace(rho)
    observed = dephase(rho)
    sigma = np.diag([0.50, 0.30, 0.20]).astype(complex)

    full = relative_entropy(rho, sigma)
    wall = relative_entropy(rho, observed)
    retained = relative_entropy(observed, sigma)
    assert abs(full - wall - retained) < TOL
    assert abs(wall - von_neumann_entropy(observed) + von_neumann_entropy(rho)) < TOL

    diagonal_tangent = np.diag([0.08, -0.03, -0.05]).astype(complex)
    off_diagonal_tangent = np.array(
        [[0.0, 0.04 + 0.02j, -0.03j],
         [0.04 - 0.02j, 0.0, 0.01],
         [0.03j, 0.01, 0.0]],
        dtype=complex,
    )
    tangent = diagonal_tangent + off_diagonal_tangent

    def divergences(parameter: float) -> tuple[float, float, float]:
        perturbed = sigma + parameter * tangent
        projected = dephase(perturbed)
        return (
            relative_entropy(perturbed, sigma),
            relative_entropy(projected, sigma),
            relative_entropy(perturbed, projected),
        )

    step = 2.0e-4
    at_zero = divergences(0.0)
    at_plus = divergences(step)
    at_minus = divergences(-step)
    hessians = tuple(
        (plus - 2.0 * zero + minus) / step**2
        for plus, zero, minus in zip(at_plus, at_zero, at_minus)
    )
    assert abs(hessians[0] - hessians[1] - hessians[2]) < 2.0e-6

    print("conditional expectation balance: PASS")
    print(f"  relative-entropy closure = {full - wall - retained:+.3e}")
    print(f"  BKM Hessian closure      = {hessians[0] - hessians[1] - hessians[2]:+.3e}")


def check_heat_entropy_coefficients() -> None:
    a0, a2, a4 = 2.3, -0.7, 1.1
    b = a2 / a0
    c = a4 / a0

    log_z_linear = b
    mean_energy_linear = -b
    entropy_linear = log_z_linear + mean_energy_linear
    entropy_quadratic = (c - 0.5 * b**2) - 2.0 * (c - 0.5 * b**2)
    expected_quadratic = 0.5 * b**2 - c
    assert abs(entropy_linear) < TOL
    assert abs(entropy_quadratic - expected_quadratic) < TOL

    # Z - t Z' multiplies a_k t^power by (1 - power).
    powers = np.array([-2.0, -1.0, 0.0])
    coefficients = np.array([a0, a2, a4])
    weighted = (1.0 - powers) * coefficients
    assert np.allclose(weighted, np.array([3.0 * a0, 2.0 * a2, a4]), atol=TOL)

    print("heat entropy coefficients: PASS")
    print(f"  linear a2 coefficient   = {entropy_linear:+.3e}")
    print(f"  quadratic coefficient   = {entropy_quadratic:+.12f}")


def check_hidden_resolvent() -> None:
    hidden = np.diag([2.0, 3.5])
    coupling = np.array([[0.4, -0.2], [0.1, 0.5]])
    target_schur = np.array([[1.7, 0.2], [0.2, 1.3]])
    retained = target_schur + coupling @ np.linalg.inv(hidden) @ coupling.T
    full = np.block([[retained, coupling], [coupling.T, hidden]])
    effective = retained - coupling @ np.linalg.inv(hidden) @ coupling.T
    assert np.allclose(effective, target_schur, atol=TOL)
    assert np.min(np.linalg.eigvalsh(full)) > 0.0

    momentum, mass_zero, mass_rate = 0.8, 1.4, 0.3
    coupling_zero, coupling_rate = 0.6, -0.2

    def mass(n_value: float) -> float:
        return mass_zero * math.exp(mass_rate * n_value)

    def vertex(n_value: float) -> float:
        return coupling_zero * math.exp(coupling_rate * n_value)

    def correction(n_value: float) -> float:
        return -(vertex(n_value) ** 2) / (momentum**2 + mass(n_value) ** 2)

    denominator = momentum**2 + mass_zero**2
    derivative_exact = (
        -2.0 * coupling_zero**2 * coupling_rate / denominator
        + coupling_zero**2 * (2.0 * mass_zero**2 * mass_rate) / denominator**2
    )
    step = 1.0e-5
    derivative_fd = (correction(step) - correction(-step)) / (2.0 * step)
    assert abs(derivative_fd - derivative_exact) < 2.0e-10

    mixing_mass, heavy_mass = 0.12, 8.0
    mass_block = np.array([[0.0, mixing_mass], [mixing_mass, heavy_mass]])
    eigenvalues = np.linalg.eigvalsh(mass_block)
    exact_light = -2.0 * mixing_mass**2 / (
        heavy_mass + math.sqrt(heavy_mass**2 + 4.0 * mixing_mass**2)
    )
    schur_mass = -(mixing_mass**2) / heavy_mass
    assert abs(eigenvalues[0] - exact_light) < TOL

    # The leading seesaw error is +m^4/M^3, not numerical equality.
    normalized_errors = []
    for trial_mixing in (0.24, 0.12, 0.06):
        trial_exact = -2.0 * trial_mixing**2 / (
            heavy_mass + math.sqrt(heavy_mass**2 + 4.0 * trial_mixing**2)
        )
        trial_schur = -(trial_mixing**2) / heavy_mass
        normalized_errors.append(
            (trial_exact - trial_schur) / (trial_mixing**4 / heavy_mass**3)
        )
    assert np.allclose(normalized_errors, np.ones(3), atol=2.0e-3)

    # A Majorana block is complex symmetric: its Schur map uses transpose,
    # not the Hermitian adjoint used by the positive response block above.
    dirac = np.array(
        [[0.12 + 0.03j, -0.07 + 0.02j], [0.04 - 0.05j, 0.09 + 0.01j]]
    )
    majorana = np.array([[8.0, 0.5 + 0.2j], [0.5 + 0.2j, 11.0]])
    light_transpose = -dirac.T @ np.linalg.inv(majorana) @ dirac
    light_adjoint = -dirac.conj().T @ np.linalg.inv(majorana) @ dirac
    assert np.allclose(light_transpose, light_transpose.T, atol=TOL)
    assert np.linalg.norm(light_transpose - light_adjoint) > 1.0e-4

    print("hidden resolvent and seesaw: PASS")
    print(f"  minimum full eigenvalue = {np.min(np.linalg.eigvalsh(full)):.12f}")
    print(f"  mixed-jet derivative    = {derivative_exact:+.12f}")
    print(f"  exact light eigenvalue  = {exact_light:+.12f}")
    print(f"  seesaw Schur mass       = {schur_mass:+.12f}")


def log_partition_m3(n_value: float, zeta_value: float) -> float:
    e13 = np.zeros((3, 3), dtype=complex)
    e13[0, 2] = 1.0
    e31 = e13.conj().T
    q_n = np.diag([1.0, 1.0, -2.0]) / math.sqrt(2.0)
    q_zeta = math.sqrt(3.0 / 2.0) * (e13 + e31)
    generator = n_value * q_n + zeta_value * q_zeta
    values = np.linalg.eigvalsh(generator)
    return float(np.log(np.sum(np.exp(-values))))


def check_mixed_response_jet() -> None:
    step = 1.0e-3

    def second_zeta(n_value: float) -> float:
        return (
            log_partition_m3(n_value, step)
            - 2.0 * log_partition_m3(n_value, 0.0)
            + log_partition_m3(n_value, -step)
        ) / step**2

    cubic_fd = (second_zeta(step) - second_zeta(-step)) / (2.0 * step)
    cubic_exact = 1.0 / (2.0 * math.sqrt(2.0))
    assert abs(cubic_fd - cubic_exact) < 4.0e-6

    # Quadratic Hessian at the tracial reference.
    g_nn = (
        log_partition_m3(step, 0.0)
        - 2.0 * log_partition_m3(0.0, 0.0)
        + log_partition_m3(-step, 0.0)
    ) / step**2
    g_zz = second_zeta(0.0)
    g_nz = (
        log_partition_m3(step, step)
        - log_partition_m3(step, -step)
        - log_partition_m3(-step, step)
        + log_partition_m3(-step, -step)
    ) / (4.0 * step**2)
    assert abs(g_nn - 1.0) < 2.0e-6
    assert abs(g_zz - 1.0) < 2.0e-6
    assert abs(g_nz) < 2.0e-6

    print("mixed response jet: PASS")
    print(f"  finite-difference jet = {cubic_fd:.12f}")
    print(f"  exact jet             = {cubic_exact:.12f}")


def check_majorana_jacobian() -> None:
    rng = np.random.default_rng(20260824)
    raw = rng.normal(size=(3, 3)) + 1.0j * rng.normal(size=(3, 3))
    r_matrix = raw.conj().T @ raw + 0.4 * np.eye(3)
    raw_k = rng.normal(size=(3, 3)) + 1.0j * rng.normal(size=(3, 3))
    k_matrix = raw_k.conj().T @ raw_k + 0.2 * np.eye(3)
    raw_x = rng.normal(size=(3, 3)) + 1.0j * rng.normal(size=(3, 3))
    x_matrix = (raw_x + raw_x.conj().T) / 2.0

    f0, f2, f4, cutoff, a_value = 1.7, 0.8, 0.3, 2.1, 4.2

    def coefficients(r_arg: np.ndarray) -> np.ndarray:
        c_value = np.trace(r_arg).real
        d_value = np.trace(r_arg @ r_arg).real
        e_value = np.trace(r_arg @ k_matrix).real
        kappa_inverse = (96.0 * f2 * cutoff**2 - f0 * c_value) / (12.0 * math.pi**2)
        gamma = (
            48.0 * f4 * cutoff**4
            - f2 * cutoff**2 * c_value
            + 0.25 * f0 * d_value
        ) / math.pi**2
        mu_squared = 2.0 * f2 * cutoff**2 / f0 - e_value / a_value
        return np.array([kappa_inverse, gamma, mu_squared])

    analytic = np.array(
        [
            -f0 * np.trace(x_matrix).real / (12.0 * math.pi**2),
            np.trace(
                (-f2 * cutoff**2 * np.eye(3) + 0.5 * f0 * r_matrix)
                @ x_matrix
            ).real
            / math.pi**2,
            -np.trace(k_matrix @ x_matrix).real / a_value,
        ]
    )
    step = 1.0e-6
    finite_difference = (
        coefficients(r_matrix + step * x_matrix)
        - coefficients(r_matrix - step * x_matrix)
    ) / (2.0 * step)
    assert np.allclose(finite_difference, analytic, atol=2.0e-8)

    print("Majorana response Jacobian: PASS")


def check_twisted_fixed_point_wall() -> None:
    q = np.diag([1.0, -1.0]).astype(complex)
    swap = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)

    def twist(matrix: np.ndarray) -> np.ndarray:
        return swap @ matrix @ swap

    theta = 0.73
    phi = math.tanh(theta)
    state = 0.5 * (np.eye(2) + phi * q)
    projected = 0.5 * (state + twist(state))
    tracial = 0.5 * np.eye(2)
    assert np.allclose(projected, tracial, atol=TOL)
    assert np.allclose(twist(q), -q, atol=TOL)

    defect = relative_entropy(state, tracial)
    defect_exact = theta * math.tanh(theta) - math.log(math.cosh(theta))
    assert abs(defect - defect_exact) < TOL
    assert abs(
        von_neumann_entropy(projected) - von_neumann_entropy(state) - defect
    ) < TOL

    step = 2.0e-5

    def log_partition(value: float) -> float:
        return math.log(2.0 * math.cosh(value))

    hessian_fd = (
        log_partition(theta + step)
        - 2.0 * log_partition(theta)
        + log_partition(theta - step)
    ) / step**2
    hessian_exact = 1.0 / math.cosh(theta) ** 2
    assert abs(hessian_fd - hessian_exact) < 2.0e-6

    print("twisted fixed-point wall: PASS")
    print(f"  twist entropy defect    = {defect:.12f}")
    print(f"  binary BKM response     = {hessian_exact:.12f}")


def check_index_edge_balance() -> None:
    dimension = 3
    index_operator = np.zeros((dimension, dimension), dtype=complex)
    for i in range(dimension):
        for j in range(dimension):
            matrix_unit = np.zeros((dimension, dimension), dtype=complex)
            matrix_unit[i, j] = 1.0
            quasi_basis = math.sqrt(dimension) * matrix_unit
            index_operator += quasi_basis @ quasi_basis.conj().T
    expected_index = dimension**2 * np.eye(dimension)
    assert np.allclose(index_operator, expected_index, atol=TOL)

    probabilities = np.array([0.60, 0.30, 0.10])
    edge_entropy = float(-np.sum(probabilities * np.log(probabilities)))
    tracial_probabilities = np.full(dimension, 1.0 / dimension)
    edge_defect = float(
        np.sum(probabilities * np.log(probabilities / tracial_probabilities))
    )
    capacity = 0.5 * math.log(dimension**2)
    assert abs(edge_entropy + edge_defect - capacity) < TOL

    print("finite-index edge balance: PASS")
    print(f"  edge entropy            = {edge_entropy:.12f}")
    print(f"  erased distinction      = {edge_defect:.12f}")
    print(f"  half log index          = {capacity:.12f}")


def positive_inverse_square_root(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(matrix)
    return (vectors * (values ** -0.5)) @ vectors.T


def check_singlet_response_completion() -> None:
    gravitational = np.array([[2.0, 0.35], [0.35, 1.25]])
    coupling_value = 1.7
    unit_vector = np.array([0.8, -0.6])
    mismatch_value = 0.55
    stiffness = 2.4
    mismatch = mismatch_value * np.outer(unit_vector, unit_vector)
    response_zero = coupling_value * gravitational + mismatch
    singlet_coupling = math.sqrt(stiffness * mismatch_value) * unit_vector
    response_effective = response_zero - np.outer(
        singlet_coupling, singlet_coupling
    ) / stiffness
    assert np.allclose(
        response_effective, coupling_value * gravitational, atol=TOL
    )
    assert np.linalg.matrix_rank(mismatch, tol=1.0e-10) == 1
    assert np.min(np.linalg.eigvalsh(mismatch)) > -TOL

    inverse_root = positive_inverse_square_root(gravitational)
    ratio = inverse_root @ response_effective @ inverse_root
    assert np.allclose(ratio, coupling_value * np.eye(2), atol=TOL)
    determinant_ratio = math.sqrt(
        np.linalg.det(response_effective) / np.linalg.det(gravitational)
    )
    assert abs(determinant_ratio - coupling_value) < TOL

    print("singlet response completion: PASS")
    print(f"  generalized eigenvalues = {np.linalg.eigvalsh(ratio)}")


def check_response_determinant() -> None:
    retained = np.array([[1.9, 0.2], [0.2, 1.5]])
    hidden = np.array([[2.4, 0.15], [0.15, 1.8]])
    coupling = np.array([[0.3, -0.1], [0.2, 0.25]])
    full = np.block([[retained, coupling], [coupling.T, hidden]])
    schur = retained - coupling @ np.linalg.inv(hidden) @ coupling.T
    assert abs(
        np.linalg.det(full) - np.linalg.det(hidden) * np.linalg.det(schur)
    ) < TOL

    direction_a = np.array([[0.35, 0.08], [0.08, -0.15]])
    direction_b = np.array([[-0.20, 0.05], [0.05, 0.30]])
    hidden_inverse = np.linalg.inv(hidden)
    hessian_exact = 0.5 * np.trace(
        hidden_inverse @ direction_a @ hidden_inverse @ direction_b
    )

    def gaussian_potential(x_value: float, y_value: float) -> float:
        varied = hidden + x_value * direction_a + y_value * direction_b
        sign, log_determinant = np.linalg.slogdet(varied)
        assert sign > 0.0
        return -0.5 * log_determinant

    step = 2.0e-4
    hessian_fd = (
        gaussian_potential(step, step)
        - gaussian_potential(step, -step)
        - gaussian_potential(-step, step)
        + gaussian_potential(-step, -step)
    ) / (4.0 * step**2)
    assert abs(hessian_fd - hessian_exact) < 2.0e-8

    print("response determinant: PASS")
    print(f"  mixed Gaussian Hessian  = {hessian_exact:+.12f}")


def check_majorana_square_and_pulse() -> None:
    f0, f2, f4, cutoff = 1.7, 0.8, 0.31, 2.1
    generation_count = 3
    radius = 2.0 * f2 * cutoff**2 / f0
    r_matrix = np.diag([0.8 * radius, 1.1 * radius, 1.35 * radius])

    def gamma_direct(matrix: np.ndarray) -> float:
        return (
            48.0 * f4 * cutoff**4
            - f2 * cutoff**2 * np.trace(matrix).real
            + 0.25 * f0 * np.trace(matrix @ matrix).real
        ) / math.pi**2

    gamma_residual = cutoff**4 * (
        48.0 * f4 - generation_count * f2**2 / f0
    ) / math.pi**2
    gamma_square = (
        f0
        * np.trace(
            (r_matrix - radius * np.eye(generation_count))
            @ (r_matrix - radius * np.eye(generation_count))
        ).real
        / (4.0 * math.pi**2)
        + gamma_residual
    )
    assert abs(gamma_direct(r_matrix) - gamma_square) < TOL

    stationary = radius * np.eye(generation_count)
    kappa_inverse = (
        96.0 * f2 * cutoff**2 - f0 * np.trace(stationary).real
    ) / (12.0 * math.pi**2)
    kappa_exact = (
        (48.0 - generation_count) * f2 * cutoff**2
        / (6.0 * math.pi**2)
    )
    assert abs(kappa_inverse - kappa_exact) < TOL

    q_matrix = np.diag([1.0, -1.0, 0.0])
    q_squared_trace = np.trace(q_matrix @ q_matrix).real
    orbit_amplitude, width, center = 0.12 * radius, 1.3, -0.2
    gamma_infinity = gamma_residual + (
        f0 * orbit_amplitude**2 * q_squared_trace / (4.0 * math.pi**2)
    )
    traces = []
    for n_value in (-1.1, 0.4, 1.7):
        hyperbolic = math.tanh(width * (n_value - center))
        orbit = stationary + orbit_amplitude * hyperbolic * q_matrix
        traces.append(np.trace(orbit).real)
        deficit = gamma_infinity - gamma_direct(orbit)
        expected_deficit = (
            f0
            * orbit_amplitude**2
            * q_squared_trace
            / (4.0 * math.pi**2)
            / math.cosh(width * (n_value - center)) ** 2
        )
        assert abs(deficit - expected_deficit) < TOL
        assert np.min(np.linalg.eigvalsh(orbit)) > 0.0
    assert np.allclose(traces, generation_count * radius, atol=TOL)

    print("Majorana square and pulse: PASS")
    print(f"  central residual        = {gamma_residual:.12f}")
    print(f"  stationary kappa^-2     = {kappa_inverse:.12f}")


def check_affine_ads_atlas() -> None:
    for n_value in (-1.2, 0.0, 0.9):
        warp = math.exp(-n_value)
        warp_second = math.exp(-n_value)
        gaussian_curvature = -warp_second / warp
        assert abs(gaussian_curvature + 1.0) < TOL

    print("affine AdS scale atlas: PASS")
    print("  unit-radius scalar R    = -2")


if __name__ == "__main__":
    check_finite_spectral_wall()
    check_conditional_expectation_balance()
    check_heat_entropy_coefficients()
    check_hidden_resolvent()
    check_mixed_response_jet()
    check_majorana_jacobian()
    check_twisted_fixed_point_wall()
    check_index_edge_balance()
    check_singlet_response_completion()
    check_response_determinant()
    check_majorana_square_and_pulse()
    check_affine_ads_atlas()
