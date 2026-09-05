"""Finite calibrations, not an SU(2) discretization or continuum proof."""

import itertools
import math

import numpy as np


RNG = np.random.default_rng(115)


def states(q, length):
    return np.array(list(itertools.product(range(q), repeat=length)), dtype=int)


def log_diameter(a):
    # Exact finite cross-ratio diameter, without a four-index tensor.
    return max(np.ptp(np.log(a[i]) - np.log(a[j]))
               for i in range(len(a)) for j in range(len(a)))


def normalize(v):
    return v / v.sum()


def block_checks():
    count = 0
    for q in (2, 3, 4):
        base = RNG.uniform(0.05, 1, (q, q))
        base = (base + base.T) / 2
        # A symmetric Markov kernel via a lazy complete weighted graph.
        np.fill_diagonal(base, 0)
        base /= 2 * base.sum(axis=1).max()
        base += np.diag(1 - base.sum(axis=1))
        for n in (1, 2, 4):
            kn = np.linalg.matrix_power(base, n)
            ratio = kn.max() / kn.min()
            for b in (0.02, 0.2, 0.7):
                potentials = RNG.uniform(-b / 2, b / 2, (n, q))
                actual = np.eye(q)
                for v in potentials:
                    actual = actual @ base @ np.diag(np.exp(-v))
                assert np.all(actual >= math.exp(-n * b / 2) * kn - 1e-14)
                assert np.all(actual <= math.exp(n * b / 2) * kn + 1e-14)
                tau = math.tanh((math.log(ratio) + n * b) / 2)
                assert log_diameter(actual) <= 2 * math.log(ratio) + 2 * n * b + 1e-12
                message = np.exp(RNG.uniform(-8, 8, q))
                posterior = actual * message
                posterior /= posterior.sum(axis=1, keepdims=True)
                tv = max(np.abs(posterior[i] - posterior[j]).sum() / 2
                         for i in range(q) for j in range(q))
                assert tv <= tau + 1e-12
                # Potentials truly change the blocked transition.
                if n > 1:
                    assert np.linalg.norm(actual - kn) > 1e-6
                count += 1
    return count


def chain_checks():
    q, length, n = 3, 8, 2
    paths = states(q, length)
    kernel = np.full((q, q), 0.08)
    np.fill_diagonal(kernel, 0.84)
    kn = np.linalg.matrix_power(kernel, n)
    ratio = kn.max() / kn.min()
    count = 0
    for b in (0.1, 0.4):
        potentials = RNG.uniform(-b / 2, b / 2, (length, q))
        logw = sum(np.log(kernel[paths[:, t], paths[:, t + 1]])
                   for t in range(length - 1))
        logw -= sum(potentials[t, paths[:, t]] for t in range(length))
        # Separate, uneven endpoint messages remain in the actual law.
        logw += np.array([0.0, 2.0, -3.0])[paths[:, 0]]
        logw += np.array([-2.0, 0.0, 1.0])[paths[:, -1]]
        mu = normalize(np.exp(logw - logw.max()))
        tau = math.tanh((math.log(ratio) + n * b) / 2)
        for r in (0, 3, 7):
            h = np.array([-0.5, 0.3, 0.7])[paths[:, r]]
            for case in range(5):
                f = RNG.normal(size=len(paths))
                if case == 0:
                    f = np.prod(paths - 1, axis=1).astype(float)
                cube = f.reshape((q,) * length)
                delta = np.array([np.ptp(cube, axis=t).max()
                                  for t in range(length)])
                centered = f - mu @ f
                covariance = mu @ (centered * (h - mu @ h))
                bound = (np.ptp(h) / 4) * sum(
                    delta[t] * tau ** (abs(t - r) // n)
                    for t in range(length))
                assert abs(covariance) <= bound + 1e-12
                conditional = np.array([
                    mu[paths[:, r] == a] @ f[paths[:, r] == a]
                    / mu[paths[:, r] == a].sum() for a in range(q)])
                assert np.ptp(conditional) <= 4 * bound / np.ptp(h) + 1e-12
                eta = 1e-5
                plus = normalize(mu * np.exp(-eta * h))
                minus = normalize(mu * np.exp(eta * h))
                derivative = ((plus - minus) @ f) / (2 * eta)
                assert abs(derivative + covariance) < 2e-9
                count += 1
    return count


def coupled_column_checks():
    """Two interacting binary temporal columns, complete path spaces."""
    results = []
    for eps, n in ((1.0, 2), (0.75, 3), (0.5, 4)):
        length = 2 * n + 1
        paths = 2 * states(2, length) - 1
        p = math.exp(-eps)
        beta = 0.01 * eps
        weights = np.ones(length)
        weights[0] = weights[-1] = 0.5
        logfree = sum(np.log((1 + p * paths[:, t] * paths[:, t + 1]) / 2)
                      for t in range(length - 1))
        logjoint = logfree[:, None] + logfree[None, :]
        logjoint += beta * (paths * weights) @ paths.T
        joint = np.exp(logjoint - logjoint.max())
        joint /= joint.sum()
        marginal = joint.sum(axis=1)
        whitened = joint / np.sqrt(marginal[:, None] * marginal[None, :])
        singular = np.linalg.svd(whitened, compute_uv=False)
        assert abs(singular[0] - 1) < 2e-12
        rho = singular[1]
        ratio = (1 + p ** n) / (1 - p ** n)
        b = 2 * beta
        tau = math.tanh((math.log(ratio) + n * b) / 2)
        susceptibility = 2 * n / (1 - tau) - 1
        qcol = beta * susceptibility
        assert qcol < 1 and 0 < rho < qcol
        # For two conditional-expectation updates, the exact full L2
        # heat-bath gap is 1-rho, not a chosen finite observable gap.
        assert 1 - rho >= 1 - qcol - 1e-12
        dmid = b + 2 * n * b + 2 * math.log(ratio)
        plus = paths[:, n] == 1
        pplus = joint[plus].sum(axis=0) / marginal
        logodds = np.log(pplus / (1 - pplus))
        assert np.abs(logodds).max() <= dmid + 1e-12
        # Test the full-path variance factorization independently.
        for _ in range(3):
            f = RNG.normal(size=joint.shape)
            mean = np.sum(joint * f)
            var = np.sum(joint * (f - mean) ** 2)
            first = np.sum(joint * f, axis=0) / marginal
            second = np.sum(joint * f, axis=1) / marginal
            residual = (np.sum(joint * (f - first[None, :]) ** 2)
                        + np.sum(joint * (f - second[:, None]) ** 2))
            assert (1 - qcol) * var <= residual + 1e-12
        results.append((eps, rho, qcol))
    return results


def exponential(a, time):
    values, vectors = np.linalg.eigh(a)
    return (vectors * np.exp(-time * values)) @ vectors.T


def hamiltonian_checks():
    # Fixed finite carrier with noncommuting electric and magnetic terms.
    lap = np.array(((0.5, -0.5), (-0.5, 0.5)))
    kinetic = np.kron(lap, np.eye(2)) + np.kron(np.eye(2), lap)
    potential = 0.03 * np.diag([0.0, 2.0, 2.0, 0.0])
    h = kinetic + potential
    values, vectors = np.linalg.eigh(h)
    psi = abs(vectors[:, 0])
    errors, vacuum_errors = [], []
    for eps in (0.4, 0.2, 0.1, 0.05, 0.025):
        n = round(2 / eps)
        a = np.diag(np.exp(-eps * np.diag(potential) / 2))
        transfer = a @ exponential(kinetic, eps) @ a
        blocked = np.linalg.matrix_power(transfer, n)
        errors.append(np.linalg.norm(blocked - exponential(h, 2), 2))
        spectrum, basis = np.linalg.eigh(transfer)
        vacuum_errors.append(np.linalg.norm(abs(basis[:, -1]) - psi))
        euler = exponential(np.eye(4) - transfer, n)
        assert np.linalg.norm(blocked - euler, 2) <= 1 / n + 1e-12
        gap = -math.log(spectrum[-2] / spectrum[-1]) / eps
        assert abs(gap - (values[1] - values[0])) < 0.01
    assert all(y < x for x, y in zip(errors, errors[1:]))
    assert all(y < x for x, y in zip(vacuum_errors, vacuum_errors[1:]))
    for n in (1, 2, 5, 50, 500):
        s = np.linspace(0, 1, 20001)
        assert np.max(np.exp(-n * (1 - s)) - s ** n) <= 1 / n + 1e-14
    return errors, vacuum_errors


def su2_arithmetic():
    count = 0
    floor = (33 / 20) * (13 / 22) ** 2 * math.exp(-11 / 50)
    for ds in (2, 3, 4):
        for x in (1, 1.001, 2.1, 10.1, 100, 1000):
            for zeta in (0, 0.002, 0.005):
                beta = zeta / ((ds - 1) * x)
                n = math.ceil(4 * x)
                b = 4 * (ds - 1) * beta
                tau = math.tanh((math.log(22 / 13) + n * b) / 2)
                susceptibility = 2 * n / (1 - tau) - 1
                qcol = 6 * (ds - 1) * beta * susceptibility
                dmid = b + 2 * n * b + 2 * math.log(22 / 13)
                assert tau <= 1 / 3 and qcol <= 9 / 20
                assert 3 * math.exp(-dmid) * (1 - qcol) >= floor - 1e-14
                count += 1
    return count, floor


if __name__ == "__main__":
    print(f"PASS {block_checks()} inhomogeneous FK block and arbitrary-message bounds")
    print(f"PASS {chain_checks()} whole-path covariance, conditioning and score checks")
    for eps, rho, qcol in coupled_column_checks():
        print(f"PASS complete interacting columns eps={eps}: rho={rho:.6g} <= {qcol:.6g}")
    errors, vacuum_errors = hamiltonian_checks()
    print("PASS fixed-carrier transfer and vacuum convergence:", errors, vacuum_errors)
    count, floor = su2_arithmetic()
    print(f"PASS {count} SU(2) regime inequalities; vacuum PI floor={floor:.9g}")
    print("No SU(2) numerical discretization limit, finite-step physical bridge floor,"
          " or four-dimensional continuum gap is certified.")
