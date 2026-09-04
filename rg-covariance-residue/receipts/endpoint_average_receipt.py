"""Checks linear gauge averages and Gaussian variational pushforward, not Yang--Mills."""

import itertools
import numpy as np


def gradient(phi, spacing):
    return np.array([(np.roll(phi, -1, mu) - phi) / spacing for mu in range(phi.ndim)])


def curl(field, spacing):
    dim = len(field)
    return np.array([
        ((np.roll(field[nu], -1, mu) - field[nu])
         - (np.roll(field[mu], -1, nu) - field[mu])) / spacing
        for mu in range(dim) for nu in range(mu+1, dim)
    ])


def form(field, spacing):
    return spacing**len(field) * np.sum(curl(field, spacing)**2)


def average(field, n):
    dim, side = len(field), field.shape[1]
    size = side // n
    result = []
    for mu in range(dim):
        path_mean = sum(np.roll(field[mu], -j, mu) for j in range(n)) / n
        cell_mean = path_mean.reshape((size, n)*dim).mean(axis=tuple(range(1, 2*dim, 2)))
        result.append(cell_mean)
    return np.array(result)


def connector(field, origin, offset):
    point, value = list(origin), 0.0
    for mu, length in enumerate(offset):
        for _ in range(length):
            value += field[(mu, *point)]
            point[mu] += 1
    return value


def endpoint_average(field, n, spacing):
    dim, side = len(field), field.shape[1]
    size = side // n
    output = np.zeros((dim,) + (size,)*dim)
    s = np.zeros((size,)*dim)
    for cell in itertools.product(range(size), repeat=dim):
        origin = tuple(n*c for c in cell)
        for offset in itertools.product(range(n), repeat=dim):
            start = tuple(o+t for o, t in zip(origin, offset))
            first = connector(field, origin, offset)
            s[cell] += spacing * first / n**dim
            for mu in range(dim):
                destination = list(origin)
                destination[mu] = (destination[mu] + n) % side
                last = connector(field, destination, offset)
                point = list(start)
                parallel = 0.0
                for _ in range(n):
                    parallel += field[(mu, *point)]
                    point[mu] = (point[mu] + 1) % side
                output[(mu, *cell)] += (first + parallel - last) / n**(dim+1)
    return output, s


rng = np.random.default_rng(4096)
for dim in (2, 3, 4):
    side, n, spacing = 8, 2, 0.25
    field = rng.normal(size=(dim,) + (side,)*dim)
    phi = rng.normal(size=(side,)*dim)
    q = average(field, n)
    m, s = endpoint_average(field, n, spacing)
    assert np.max(np.abs(m - q + gradient(s, n*spacing))) < 1e-12
    transformed, _ = endpoint_average(field-gradient(phi, spacing), n, spacing)
    samples = phi[(slice(None, None, n),)*dim]
    assert np.max(np.abs(transformed - m + gradient(samples, n*spacing))) < 1e-12
    assert form(q, n*spacing) <= form(field, spacing) + 1e-10
    assert np.max(np.abs(curl(m, n*spacing)-curl(q, n*spacing))) < 1e-12
    assert np.max(np.abs(average(average(field, 2), 2)-average(field, 4))) < 1e-12
print("PASS: endpoint/volume identity, gauge covariance, curvature contraction, composition in d=2,3,4.")


def patch_constant(n, dim):
    shape = (2*n,) + (n,)*(dim-1)
    vertices = list(itertools.product(*(range(k) for k in shape)))
    edges = [(x, mu) for x in vertices for mu in range(dim) if x[mu]+1 < shape[mu]]
    indices = {edge: index for index, edge in enumerate(edges)}
    curls = []
    for x in vertices:
        for mu in range(dim):
            for nu in range(mu+1, dim):
                if x[mu]+1 >= shape[mu] or x[nu]+1 >= shape[nu]:
                    continue
                xm, xn = list(x), list(x)
                xm[mu] += 1
                xn[nu] += 1
                row = np.zeros(len(edges))
                for edge, sign in (((x, mu), 1), ((tuple(xm), nu), 1),
                                   ((tuple(xn), mu), -1), ((x, nu), -1)):
                    row[indices[edge]] += sign
                curls.append(row)
    constraints = []
    for block in (0, 1):
        origin = (block*n,) + (0,)*(dim-1)
        for offset in itertools.product(range(n), repeat=dim):
            if not any(offset):
                continue
            point = list(origin)
            row = np.zeros(len(edges))
            for mu, length in enumerate(offset):
                for _ in range(length):
                    row[indices[(tuple(point), mu)]] += 1
                    point[mu] += 1
            constraints.append(row)
    constraint = np.array(constraints)
    _, singular, vt = np.linalg.svd(constraint, full_matrices=True)
    basis = vt[np.count_nonzero(singular > 1e-10):].T
    q = np.zeros(len(edges))
    for x in itertools.product(range(n), repeat=dim):
        point = list(x)
        for _ in range(n):
            q[indices[(tuple(point), 0)]] += n**(-dim-1)
            point[0] += 1
    d = np.array(curls)
    hessian = d.T @ d + np.outer(q, q)
    minimum = np.linalg.eigvalsh(basis.T @ hessian @ basis)[0]
    assert minimum > 1e-8
    return minimum


for dim, n in ((2, 2), (2, 3), (3, 2), (4, 2)):
    print(f"PASS: two-block axial floor d={dim}, n={n}: c={patch_constant(n, dim):.9g}")


def periodic_matrices(side, dim, n):
    shape = (dim,) + (side,)*dim
    count = dim * side**dim
    basis = np.eye(count).reshape((count,) + shape)
    d = np.column_stack([curl(field, 1).ravel() for field in basis])
    q = np.column_stack([average(field, n).ravel() for field in basis])
    return d, q


for dim in (2, 3):
    side, n, a, b = 4, 2, 0.5, 1.0
    fine_d, q = periodic_matrices(side, dim, n)
    coarse_d, _ = periodic_matrices(side//n, dim, 1)
    fine_h = a**(dim-2) * fine_d.T @ fine_d
    coarse_h = b**(dim-2) * coarse_d.T @ coarse_d
    fine_e, fine_v = np.linalg.eigh(fine_h)
    coarse_e, coarse_v = np.linalg.eigh(coarse_h)
    fine_keep, coarse_keep = fine_e > 1e-8, coarse_e > 1e-8
    # Positive curl-form subspaces remove gradients and harmonic modes.
    induced = coarse_v[:, coarse_keep].T @ q @ fine_v[:, fine_keep]
    covariance = (induced / fine_e[fine_keep]) @ induced.T
    effective = np.linalg.inv(covariance)
    lower = np.diag(coarse_e[coarse_keep])
    assert np.linalg.eigvalsh(effective-lower)[0] > -1e-9
    print(f"PASS: exact Gaussian quotient pushforward dominates coarse Maxwell form in d={dim}.")

def quotient_basis(side, dim, spacing):
    raw_d, _ = periodic_matrices(side, dim, 1)
    eigenvalues, vectors = np.linalg.eigh(raw_d.T @ raw_d)
    keep = eigenvalues > 1e-8
    return eigenvalues[keep] / spacing**2, vectors[:, keep]


for dim, sides in ((2, [24, 12, 6, 3]), (3, [6, 3])):
    n, eta = 2, 0.07
    meshes = [2.0**(j-len(sides)+1) for j in range(len(sides))]
    data = [quotient_basis(side, dim, mesh) for side, mesh in zip(sides, meshes)]
    gamma = 1 + 4*dim*eta/(1-n**-2)
    c = patch_constant(n, dim)
    soft_constant = min(c*n*n/(2*dim*gamma), c*n**dim/eta)
    covariance_now = np.diag(1/data[0][0])
    for j in range(len(sides)-1):
        fine_e, fine_v = data[j]
        coarse_e, coarse_v = data[j+1]
        _, raw_q = periodic_matrices(sides[j], dim, n)
        # Orthonormal physical-L2 coordinates, not raw bond coefficients.
        q = n**(dim/2) * coarse_v.T @ raw_q @ fine_v
        assert np.linalg.eigvalsh(q @ q.T)[-1] <= 1+1e-9
        energy_map = np.sqrt(coarse_e)[:, None]*q/np.sqrt(fine_e)[None, :]
        assert np.linalg.eigvalsh(energy_map @ energy_map.T)[-1] <= 1+1e-9
        b_next = meshes[j+1]
        observation = (
            2*dim*meshes[j]**2*np.diag(fine_e)
            + n**-dim*q.T@q
        )
        assert np.linalg.eigvalsh(observation)[0] >= c-1e-8
        precision_now = np.linalg.inv(covariance_now)
        reverse = precision_now + q.T@q/(eta*b_next*b_next)
        assert np.linalg.eigvalsh(reverse)[0]*b_next*b_next >= soft_constant-1e-8
        covariance_now = q@covariance_now@q.T + eta*b_next*b_next*np.eye(len(coarse_e))
        energy_covariance = (
            np.sqrt(coarse_e)[:, None]*covariance_now*np.sqrt(coarse_e)[None, :]
        )
        assert np.linalg.eigvalsh(energy_covariance)[-1] <= gamma+1e-8
        assert coarse_e.max()*b_next*b_next <= 4*dim+1e-8
    print(f"PASS: physical quotient observation, soft covariance, and reverse floors in d={dim}, depth={len(sides)-1}.")


for epsilon in (0.1, 0.01, 0.001):
    fine_k = np.diag([1.0, epsilon**2])
    q = np.array([[0.0, epsilon]])
    assert np.linalg.eigvalsh(fine_k-q.T@q)[0] >= 0
    reverse = fine_k + 2*q.T@q
    assert abs(np.linalg.eigvalsh(reverse)[0]-3*epsilon**2) < 1e-12
print("PASS: hard-kernel coercivity alone fails the soft-observation test.")


def scalar_matrices(side, dim, n, spacing):
    count, coarse_side = side**dim, side//n
    basis = np.eye(count).reshape((count,) + (side,)*dim)
    derivative = np.column_stack([gradient(phi, spacing).ravel() for phi in basis])
    q0 = np.column_stack([
        phi.reshape((coarse_side, n)*dim).mean(axis=tuple(range(1, 2*dim, 2))).ravel()
        for phi in basis
    ])
    # Both scalar spaces are in orthonormal physical-L2 coordinates.
    return derivative, n**(dim/2)*q0


for dim, side, n in ((2, 12, 2), (2, 9, 3), (3, 6, 2)):
    a, eta = 0.37, 0.21
    b = n*a
    curl_raw, q_raw = periodic_matrices(side, dim, n)
    curl_op = curl_raw/a
    q_full = n**(dim/2)*q_raw
    derivative, q0 = scalar_matrices(side, dim, n, a)
    coarse_derivative, _ = scalar_matrices(side//n, dim, 1, b)
    block_zero = np.eye(q0.shape[1])-q0.T@q0
    assert np.allclose(q0@q0.T, np.eye(q0.shape[0]))
    assert np.allclose(q_full@derivative, coarse_derivative@q0)
    lift_gradient = derivative@q0.T
    assert np.allclose(
        lift_gradient.T@lift_gradient,
        n*coarse_derivative.T@coarse_derivative,
    )
    block_e, block_v = np.linalg.eigh(block_zero)
    block_v = block_v[:, block_e > 0.5]
    restricted_laplacian = block_v.T@derivative.T@derivative@block_v
    assert np.linalg.eigvalsh(restricted_laplacian)[0] >= 4/b**2-1e-8

    fine_e, fine_v = quotient_basis(side, dim, a)
    _, coarse_v = quotient_basis(side//n, dim, b)
    q_physical = coarse_v.T@q_full@fine_v
    weight = 1/(eta*b*b)
    conditional_precision = np.diag(fine_e)+weight*q_physical.T@q_physical
    quotient_covariance = fine_v@np.linalg.inv(conditional_precision)@fine_v.T
    quotient_curl_covariance = curl_op@quotient_covariance@curl_op.T
    quotient_mean_response = (
        weight*curl_op@quotient_covariance@q_full.T@coarse_v@coarse_v.T
    )
    c_patch = patch_constant(n, dim)
    first = 6*dim*(1+2*np.sqrt(n))**2/(c_patch*n*n)
    second = 3*(1+2*np.sqrt(n))**2/(c_patch*n**dim)+12*n
    previous_curl_covariance = None
    for alpha in (0.3, 1.0, 2.7):
        completed = (
            curl_op.T@curl_op
            + alpha*derivative@block_zero@derivative.T
            + weight*q_full.T@q_full
        )
        beta = min(1/first, 1/(eta*second), 4*alpha/3)
        upper = 4*dim*(1+alpha)*n*n+1/eta
        spectrum = np.linalg.eigvalsh(completed)
        assert spectrum[0]*b*b >= beta-1e-8
        assert spectrum[-1]*b*b <= upper+1e-8
        inverse = np.linalg.inv(completed)
        completed_curl_covariance = curl_op@inverse@curl_op.T
        assert np.allclose(completed_curl_covariance, quotient_curl_covariance, atol=1e-9)
        mean_response = weight*curl_op@inverse@q_full.T
        assert np.allclose(mean_response, quotient_mean_response, atol=1e-9)
        assert np.max(np.abs(mean_response@coarse_derivative)) < 1e-9
        if previous_curl_covariance is not None:
            assert np.allclose(completed_curl_covariance, previous_curl_covariance)
        previous_curl_covariance = completed_curl_covariance

        # Nonlinear observable F=(one plaquette curvature)^2.
        coarse_value = coarse_v@rng.normal(size=coarse_v.shape[1])
        h = np.zeros(q_full.shape[0])
        h[0] = 1
        current = curl_op[0]
        mean = weight*inverse@q_full.T@coarse_value
        change = weight*inverse@q_full.T@h
        epsilon = 1e-4
        finite_difference = (
            (current@(mean+epsilon*change))**2
            - (current@(mean-epsilon*change))**2
        )/(2*epsilon)
        score_derivative = 2*weight*(current@mean)*(current@inverse@q_full.T@h)
        assert np.isclose(finite_difference, score_derivative, atol=1e-8)

        if dim == 2 and n == 2 and alpha == 1:
            # Finite-range powers on the actual lattice, not a fitted decay curve.
            coords = list(itertools.product(range(side), repeat=dim))
            positions = []
            for mu in range(dim):
                for coord in coords:
                    midpoint = np.array(coord, dtype=float)
                    midpoint[mu] += 0.5
                    positions.append(a*midpoint)
            positions = np.array(positions)
            displacement = np.abs(positions[:, None, :]-positions[None, :, :])
            distance = np.minimum(displacement, side*a-displacement).sum(axis=2)
            support = np.abs(completed) > 1e-10
            actual_range = distance[support].max()
            assert actual_range <= (dim+4)*b
            step = np.eye(len(completed))-b*b*completed/upper
            power = np.eye(len(completed))
            for order in range(1, 4):
                power = power@step
                forbidden = distance > order*actual_range+1e-10
                if forbidden.any():
                    assert np.max(np.abs(power[forbidden])) < 1e-11
            far = np.unravel_index(np.argmax(distance), distance.shape)
            tail_bound = b*b/beta*(1-beta/upper)**np.ceil(distance[far]/actual_range)
            assert abs(inverse[far]) <= tail_bound
    print(f"PASS: local completion, quotient curl law, source response, and explicit bounds in d={dim}, n={n}.")

# An unrestricted gauge penalty changes even a finite cochain observable law.
naive = np.array([[3.0, 1.0], [1.0, 2.0]])
assert np.isclose(np.linalg.inv(naive)[0, 0], 2/5)
assert not np.isclose(np.linalg.inv(naive)[0, 0], 1/2)
print("PASS: finite-range inverse expansion and naive gauge-completion counterexample.")
print("Not tested: accumulated-step localization, nonlinear Wilson law, infrared gap, or continuum existence.")
