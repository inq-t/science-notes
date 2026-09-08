"""Finite diagnostics for conditional-score shorting; no QFT or continuum claim.

Run with Python and NumPy.  This script reads/writes no workspace files.
The Gaussian quadrature and finite Hermite carrier are numerical checks;
the note, not finite sampling, supplies the all-observable proofs.
"""
from itertools import product
from math import factorial, sqrt
import numpy as np
from numpy.polynomial.hermite import hermgauss

TOL = 3e-10
DEGREE = 5


def close(actual, expected, tolerance=TOL):
    error = float(np.max(np.abs(np.asarray(actual) - np.asarray(expected))))
    if not np.isfinite(error) or error > tolerance:
        raise AssertionError(f"error {error:.6g} exceeds {tolerance:.6g}")
    return error


def gaussian_quadrature(order):
    x, weight = hermgauss(order)
    return sqrt(2.0) * x, weight / sqrt(np.pi)


def probability(value, mean):
    return (1.0 + value * mean) / 2.0


def cells_for(means):
    cells = list(product((1, -1), repeat=len(means)))
    weights = np.array([
        np.prod([probability(z, m) for z, m in zip(cell, means)])
        for cell in cells
    ])
    return cells, weights


def range_cost(matrix, covector):
    inverse = np.linalg.pinv(matrix, rcond=1e-12)
    if np.linalg.norm(matrix @ inverse @ covector - covector) > TOL:
        return np.inf
    return float(covector @ inverse @ covector)


def frame(cell):
    return np.array([1.0, float(np.prod(cell))])


def hermite_basis(w, degree):
    raw = [np.ones_like(w), w.copy()]
    for n in range(1, degree):
        raw.append(w * raw[n] - n * raw[n - 1])
    values = np.array([raw[n] / sqrt(factorial(n)) for n in range(degree + 1)])
    derivative = np.zeros_like(values)
    for n in range(1, degree + 1):
        derivative[n] = sqrt(n) * values[n - 1]
    return values, derivative


def main():
    a, b = 0.5, 1.0 / 3.0
    cells, weights = cells_for((a, b))
    ell = np.array([frame(cell) for cell in cells])
    finest = np.array([np.outer(row, row) for row in ell])
    whole = np.einsum("i,ijk->jk", weights, finest)
    close(whole, [[1, a * b], [a * b, 1]])

    theta = np.array([0.2, -0.4])
    target_entropy = 0.5 * theta @ whole @ theta
    quadrature_results = []
    for order in (24, 48):
        w, gw = gaussian_quadrature(order)
        entropy = 0.0
        fisher = np.zeros((2, 2))
        normalization_error = 0.0
        for p, row in zip(weights, ell):
            shift = row @ theta
            log_density = shift * w - shift * shift / 2.0
            density = np.exp(log_density)
            normalization_error = max(normalization_error, close(gw @ density, 1.0))
            entropy += p * (gw @ (density * log_density))
            score = w[:, None] * row[None, :]
            fisher += p * np.einsum("i,ij,ik->jk", gw, score, score)
        close(entropy, target_entropy)
        close(fisher, whole)
        quadrature_results.append(entropy)
        print(f"PASS Gaussian likelihood order={order}: KL={entropy:.12g}, "
              f"normalization_error={normalization_error:.3g}")
    close(*quadrature_results)

    boundary = {}
    for B in (1, -1):
        ix = [i for i, cell in enumerate(cells) if cell[0] == B]
        boundary[B] = sum(weights[i] * finest[i] for i in ix) / sum(weights[ix])
        close(boundary[B], [[1, B * b], [B * b, 1]])
        transport = np.diag([1.0, B])
        close(transport @ boundary[B] @ transport, [[1, b], [b, 1]])
    for matrix, row in zip(finest, ell):
        close(np.linalg.pinv(matrix), matrix / 4.0)
        close(row @ np.linalg.pinv(matrix) @ row, 1.0)
    assert np.isinf(range_cost(finest[0], np.array([1.0, -1.0])))
    assert np.isinf(range_cost(np.zeros((2, 2)), np.array([1.0, 0.0])))
    close(range_cost(np.zeros((2, 2)), np.zeros(2)), 0.0)
    print("PASS conditional Gramians, frame transport, rank-one ranges and zero-range gate")

    u = np.array([1.0, 0.0])
    v = np.linalg.solve(whole, u)
    coefficient = ell @ v
    gradient = ell * coefficient[:, None]
    close(v, np.array([36.0, -6.0]) / 35.0)
    close(coefficient, [6.0 / 7, 6.0 / 5, 6.0 / 5, 6.0 / 7])
    close(weights @ gradient, u)
    cost = weights @ (coefficient ** 2)
    close(cost, 36.0 / 35.0)
    coarser = {}
    for B in (1, -1):
        ix = [i for i, cell in enumerate(cells) if cell[0] == B]
        coarser[B] = sum(weights[i] * gradient[i] for i in ix) / sum(weights[ix])
        close(coarser[B], boundary[B] @ v)
    close(coarser[1], np.array([34.0, 6.0]) / 35.0)
    close(coarser[-1], np.array([38.0, -18.0]) / 35.0)
    # A conditional mean is not itself the pointwise gradient at every R.
    wrong_range = np.linalg.norm((np.eye(2) - finest[0] / 2) @ coarser[1])
    assert wrong_range > 0.1
    beta = np.array([B - 9 * R / 16 - 5 / 16 for B, R in cells])
    close(weights @ (ell * beta[:, None]), np.zeros(2))
    perturbed = gradient + ell * beta[:, None]
    perturbed_cost = sum(p * range_cost(I, eta)
                         for p, I, eta in zip(weights, finest, perturbed))
    close(weights @ beta ** 2, 33.0 / 32)
    close(perturbed_cost - cost, 33.0 / 32)
    print(f"PASS actual observable gradient: variance={cost:.12g}, "
          f"nonminimal lift residue={perturbed_cost-cost:.12g}")

    # Solve independently over all cellwise Hermite observables through degree 5.
    # The basis 1_cell He_n/sqrt(p_cell n!) is orthonormal in the actual law.
    w, gw = gaussian_quadrature(48)
    hermite, derivative = hermite_basis(w, DEGREE)
    close((hermite * gw) @ hermite.T, np.eye(DEGREE + 1))
    response = np.zeros((2, len(cells) * (DEGREE + 1)))
    score_response = np.zeros_like(response)
    for i, (p, row) in enumerate(zip(weights, ell)):
        for n in range(DEGREE + 1):
            column = i * (DEGREE + 1) + n
            response[:, column] = sqrt(p) * row * (gw @ derivative[n])
            score_response[:, column] = sqrt(p) * row * (gw @ (w * hermite[n]))
    close(response, score_response)
    close(response @ response.T, whole)
    minimizer = response.T @ np.linalg.solve(response @ response.T, u)
    expected = np.zeros_like(minimizer)
    for i, p in enumerate(weights):
        expected[i * (DEGREE + 1) + 1] = sqrt(p) * coefficient[i]
    close(minimizer, expected)
    close(response @ minimizer, u)
    close(minimizer @ minimizer, cost)
    q_kernel = gw @ (w * (w*w - 1))
    q_product = gw @ (w * ((w*w - 1)*w))
    close(q_kernel, 0.0)
    close(q_product, 2.0)
    print(f"PASS full {len(minimizer)}-dimensional Hermite test: least variance is "
          "score-linear; response kernel is not a multiplication ideal")

    # A genuinely nested three-bit cut, ending at singular rank-one fibers.
    nested_cells, nested_weights = cells_for((0.5, 1.0/3, -0.25))
    nested_ell = np.array([frame(cell) for cell in nested_cells])
    nested_finest = np.array([np.outer(row, row) for row in nested_ell])
    levels = []
    for depth in range(4):
        level = {}
        for key in sorted({cell[:depth] for cell in nested_cells}):
            ix = [i for i, cell in enumerate(nested_cells) if cell[:depth] == key]
            mass = sum(nested_weights[ix])
            matrix = sum(nested_weights[i] * nested_finest[i] for i in ix) / mass
            level[key] = (mass, matrix)
        levels.append(level)
    target = np.array([2.0/3, -0.2])
    reference_v = np.linalg.solve(levels[0][()][1], target)
    current = {(): target}
    reference_cost = target @ reference_v
    for depth, level in enumerate(levels):
        if depth:
            following = {}
            for key, (_, matrix) in level.items():
                parent = key[:-1]
                parent_matrix = levels[depth-1][parent][1]
                following[key] = matrix @ np.linalg.pinv(parent_matrix) @ current[parent]
                close(following[key], matrix @ reference_v)
            current = following
        staged_cost = sum(mass * range_cost(matrix, current[key])
                          for key, (mass, matrix) in level.items())
        close(staged_cost, reference_cost)
        for cell, row in zip(nested_cells, nested_ell):
            key = cell[:depth]
            realized = row @ np.linalg.pinv(level[key][1]) @ current[key]
            close(realized, row @ reference_v)
    print(f"PASS four nested contexts: associative lifts and identical observables, "
          f"cost={reference_cost:.12g}")

    # Pseudoinverse matrices themselves are chart-dependent; admissible costs are not.
    transform = np.array([[2.0, 0.25], [0.5, 1.5]])
    transformed_whole = transform.T @ whole @ transform
    transformed_u = transform.T @ u
    transformed_v = np.linalg.solve(transformed_whole, transformed_u)
    for matrix, eta in zip(finest, gradient):
        changed = transform.T @ matrix @ transform
        changed_eta = transform.T @ eta
        close(range_cost(changed, changed_eta), range_cost(matrix, eta))
        close(changed @ transformed_v, changed_eta)
    print("PASS invertible source-coordinate change: singular dual costs and lifts invariant")

    # Independent pointwise dual computations determine all three closed OU clocks.
    rates = [[], [], []]
    for cell, row, matrix in zip(cells, ell, finest):
        rates[0].append(row @ np.linalg.inv(whole) @ row)
        rates[1].append(row @ np.linalg.inv(boundary[cell[0]]) @ row)
        rates[2].append(row @ np.linalg.pinv(matrix) @ row)
    rates = np.asarray(rates)
    close(rates[0], [2 / (1 + a*b*B*R) for B, R in cells])
    close(rates[1], [2 / (1 + b*R) for B, R in cells])
    close(rates[2], np.ones(4))
    close(rates @ weights, [2, 2, 1])
    energies = []
    for R in (1, -1):
        indicator = np.array([float(cell[1] == R) for cell in cells])
        energies.append(rates @ (weights * indicator))
    close(energies[0], [44.0/35, 1, 2.0/3])
    close(energies[1], [26.0/35, 1, 1.0/3])
    print("PASS three clocks: F+ energies=(44/35,1,2/3), "
          "F- energies=(26/35,1,1/3); whole and boundary forms not ordered")

    # At a=0 every policy intertwines the complete finite Hermite annular carrier.
    # Normalized sector restriction is a stronger test than this intertwining.
    a0, b0 = 0.0, 0.5
    c0, p0 = cells_for((a0, b0))
    d = DEGREE + 1
    inclusion = np.zeros((4*d, 2*d))
    for i, (B, R) in enumerate(c0):
        r_index = 0 if R == 1 else 1
        for n in range(d):
            inclusion[i*d+n, r_index*d+n] = sqrt(probability(B, a0))
    close(inclusion.T @ inclusion, np.eye(2*d))
    e0 = np.array([frame(cell) for cell in c0])
    atom_grams = np.array([np.outer(row, row) for row in e0])
    root_gram = np.einsum("i,ijk->jk", p0, atom_grams)
    conditional_grams = {}
    for B in (1, -1):
        ix = [i for i, cell in enumerate(c0) if cell[0] == B]
        conditional_grams[B] = (
            sum(p0[i] * atom_grams[i] for i in ix) / sum(p0[ix])
        )
    full_rates = [
        np.array([row @ np.linalg.pinv(root_gram) @ row for row in e0]),
        np.array([row @ np.linalg.pinv(conditional_grams[cell[0]]) @ row
                  for cell, row in zip(c0, e0)]),
        np.array([row @ np.linalg.pinv(matrix) @ row
                  for row, matrix in zip(e0, atom_grams)]),
    ]
    annular_rates = []
    for rates_here in full_rates:
        close(rates_here[:2], rates_here[2:])
        annular_rates.append(rates_here[:2])
    correlations = []
    for full_rate, annular_rate in zip(full_rates, annular_rates):
        full_diag = np.concatenate([rate * np.arange(d) for rate in full_rate])
        annular_diag = np.concatenate([rate * np.arange(d) for rate in annular_rate])
        close(full_diag[:, None] * inclusion, inclusion * annular_diag[None, :])
        assert np.count_nonzero(full_diag == 0) == 4
        for time in (0.2, 0.7, 1.3):
            close(np.exp(-time*full_diag)[:, None]*inclusion,
                  inclusion*np.exp(-time*annular_diag)[None, :])
        correlations.append(0.75 * np.exp(-0.7 * annular_rate[0]))
    assert max(correlations) - min(correlations) > 0.1
    # Reconstruct the clocks from the actual normalized conditional source laws.
    # Merely selecting a block of the old clock does not perform reconstruction.
    boundary_failure, finer_failure = 0.0, 0.0
    for i, ((B, R), row) in enumerate(zip(c0, e0)):
        rebuilt_B = row @ np.linalg.pinv(conditional_grams[B]) @ row
        rebuilt_BR = row @ np.linalg.pinv(atom_grams[i]) @ row
        boundary_failure = max(boundary_failure, abs(full_rates[0][i] - rebuilt_B))
        finer_failure = max(finer_failure, abs(full_rates[1][i] - rebuilt_BR))
        close(full_rates[1][i], rebuilt_B)
        close(full_rates[2][i], rebuilt_BR)
    close(boundary_failure, 2.0)
    close(finer_failure, 3.0)
    print("PASS all-time annular intertwining selects none; conditional source "
          "reconstruction exposes normalized-restriction rate discrepancies 2 and 3")
    print("DIAGNOSTIC F+ correlations at t=.7: " +
          ", ".join(f"{x:.12g}" for x in correlations))

    # Actual marginalization uses a mixture likelihood, not average Fisher matrices.
    w, gw = gaussian_quadrature(48)
    step = 1e-5
    marginal_fisher = np.zeros((2, 2))
    for R in (1, -1):
        scores = []
        for axis in range(2):
            probe = np.eye(2)[axis] * step
            likelihoods = []
            for sign in (1, -1):
                density = np.zeros_like(w)
                for B in (1, -1):
                    shift = sign * (probe[0] + B*R*probe[1])
                    density += probability(B, a) * np.exp(shift*w - shift*shift/2)
                likelihoods.append(density)
            scores.append((np.log(likelihoods[0])-np.log(likelihoods[1]))/(2*step))
        scores = np.asarray(scores)
        marginal_fisher += probability(R, b) * (scores * gw) @ scores.T
    marginal_target = np.array([[1, a*b], [a*b, a*a]])
    close(marginal_fisher, marginal_target, tolerance=2e-8)
    assert np.linalg.norm(whole - marginal_target) > 0.5
    print("PASS marginalized mixture likelihood: Fisher=[[1,ab],[ab,a^2]], "
          "distinct from scalarization")
    print("Finite Gaussian and matrix diagnostics only; no physical clock, "
          "record-selection law or four-dimensional Yang--Mills proof.")


if __name__ == "__main__":
    main()
