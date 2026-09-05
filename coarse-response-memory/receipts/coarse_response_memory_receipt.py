"""Exact finite calibrations of coarse response; no continuum or fit claims."""

import math

import numpy as np


RNG = np.random.default_rng(116)


def positive(a, tol=2e-10):
    return np.linalg.eigvalsh((a + a.T) / 2).min() >= -tol


def exp_minus(a, time):
    values, vectors = np.linalg.eigh(a)
    return (vectors * np.exp(-time * values)) @ vectors.T


def gap_bound(s, c, k):
    total = s + c + c * k * k
    # Stable evaluation of the smaller quadratic root.
    return 2 * s * c / (total + math.sqrt(total * total - 4 * s * c))


def block_checks():
    count = 0
    nodes, weights = np.polynomial.legendre.leggauss(80)
    for nr, nh in ((1, 1), (2, 3), (3, 2), (4, 5)):
        for _ in range(3):
            raw = RNG.normal(size=(nh, nh))
            cmat = raw.T @ raw + 0.3 * np.eye(nh)
            raw = RNG.normal(size=(nr, nr))
            smat = raw.T @ raw + 0.2 * np.eye(nr)
            b = RNG.normal(size=(nh, nr))
            cinv = np.linalg.inv(cmat)
            d = cinv @ b
            a = smat + b.T @ d
            whole = np.zeros((nr + nh, nr + nh))
            whole[:nr, :nr] = a
            whole[:nr, nr:] = b.T
            whole[nr:, :nr] = b
            whole[nr:, nr:] = cmat
            c = np.linalg.eigvalsh(cmat).min()
            s = np.linalg.eigvalsh(smat).min()
            k = np.linalg.norm(d, 2)
            delta = gap_bound(s, c, k)
            assert positive(whole - delta * np.eye(nr + nh))
            metric_excess = d.T @ d
            harmonic_lift = np.vstack((np.eye(nr), -d))
            assert np.allclose(harmonic_lift.T @ whole @ harmonic_lift, smat, atol=2e-11)
            assert np.allclose(harmonic_lift.T @ harmonic_lift, np.eye(nr) + metric_excess)
            assert abs(gap_bound(7 * s, 7 * c, k) / (7 * c) - delta / c) < 1e-12
            for z in (0.01, 0.4, 3.0):
                sigma = b.T @ np.linalg.solve(cmat + z * np.eye(nh), b)
                denominator = z * np.eye(nr) + a - sigma
                actual = np.linalg.inv(whole + z * np.eye(nr + nh))[:nr, :nr]
                assert np.allclose(actual, np.linalg.inv(denominator), atol=2e-11)
                remainder = sigma - b.T @ d + z * metric_excess
                assert positive(remainder)
                assert positive(z * z / (c + z) * metric_excess - remainder)
                lower = np.linalg.inv(smat + (1 + k * k) * z * np.eye(nr))
                static = np.linalg.inv(smat + z * np.eye(nr))
                assert positive(actual - lower)
                assert positive(static - actual)
                assert np.linalg.norm(actual - static, 2) <= z * k * k / (z + s)**2 + 1e-10
                count += 1
            for time in (0.08, 0.7):
                full = exp_minus(whole, time)
                retained = full[:nr, :nr]
                derivative = (-whole @ full)[:nr, :nr]
                convolution = np.zeros((nr, nr))
                for node, weight in zip(nodes, weights):
                    u = time * (node + 1) / 2
                    memory = b.T @ exp_minus(cmat, time - u) @ b
                    convolution += weight * memory @ exp_minus(whole, u)[:nr, :nr] * time / 2
                assert np.allclose(derivative, -a @ retained + convolution, atol=3e-10)
                count += 1
    return count


def chain_checks():
    f = np.array((2.0, -1.0, -1.0)) / math.sqrt(6)
    hidden = np.array((0.0, 1.0, -1.0)) / math.sqrt(2)
    # Isometry representing the complete two-cell conditional readout.
    j = np.zeros((3, 2))
    j[0, 0] = 1
    j[1:, 1] = 1 / math.sqrt(2)
    centered = np.column_stack((f, hidden))
    count = 0
    for eps in (1.0, 0.2, 0.03, 1e-3, 1e-5):
        whole = np.zeros((3, 3))
        for left, right, rate in ((0, 1, 1.0), (1, 2, eps)):
            whole[left, left] += rate
            whole[right, right] += rate
            whole[left, right] -= rate
            whole[right, left] -= rate
        block = centered.T @ whole @ centered
        a, b, c = 1.5, -math.sqrt(3) / 2, 0.5 + 2 * eps
        expected = np.array(((a, b), (b, c)))
        assert np.allclose(block, expected)
        s = 6 * eps / (1 + 4 * eps)
        radius = math.sqrt(1 - eps + eps * eps)
        upper = 1 + eps + radius
        lower = 3 * eps / upper
        alpha = (upper - a) / (upper - lower)
        assert abs(gap_bound(s, c, abs(b / c)) - lower) < 1e-11
        assert np.allclose(np.linalg.eigvalsh(whole), (0, lower, upper), atol=2e-12)
        for time in (0.2, 1.0, 1 / lower):
            semigroup = exp_minus(whole, time)
            r = alpha * math.exp(-lower * time) + (1 - alpha) * math.exp(-upper * time)
            assert abs(f @ semigroup @ f - r) < 2e-10
            coarse = j.T @ semigroup @ j
            assert np.all(coarse >= -1e-12)
            constant = np.array((1, math.sqrt(2)))
            assert np.allclose(coarse @ constant, constant, atol=2e-10)
            defect = j.T @ exp_minus(whole, 2 * time) @ j - coarse @ coarse
            assert positive(defect)
            r2 = alpha * math.exp(-2 * lower * time) + (1 - alpha) * math.exp(-2 * upper * time)
            predicted_defect = alpha * (1 - alpha) * (math.exp(-lower * time) - math.exp(-upper * time))**2
            assert abs(r2 - r * r - predicted_defect) < 2e-12
            count += 1
        # A genuine physical transfer can be handled through its bounded defect.
        tau = 0.7
        transfer = exp_minus(block, tau)
        defect = np.eye(2) - transfer
        cdef = defect[1, 1]
        bdef = defect[1, 0]
        sdef = defect[0, 0] - bdef * bdef / cdef
        dgap = gap_bound(sdef, cdef, abs(bdef / cdef))
        returned_energy = -math.log1p(-dgap) / tau
        assert abs(returned_energy - lower) < 3e-10
    for s, c in ((0.2, 1), (2, 0.1), (1, 1)):
        assert abs(gap_bound(s, c, 0) - min(s, c)) < 1e-12
    return count


if __name__ == "__main__":
    print("PASS block resolvent, memory quadrature, remainder and gap:", block_checks())
    print("PASS full reversible readout, slow tail and physical defect:", chain_checks())
    print("Scope: finite exact-algebra calibrations, not Yang--Mills or cosmological closure.")
