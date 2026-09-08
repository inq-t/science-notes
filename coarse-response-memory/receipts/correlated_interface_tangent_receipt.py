"""Two-channel interface response, including a rational residual certificate.

The finite eigensolver proposes trials only. The certificate rationalizes
them, includes every omitted neighbor, and encloses square roots using the
existing exact interval arithmetic. It covers kappa=beta=1 on the supplied
seven-link system; it neither selects that Hamiltonian nor proves a field gap.
Run with Python -B to avoid creating import caches in the research modules.
"""

from __future__ import annotations

from fractions import Fraction as F
import math

import numpy as np

from ground_marginal_certificate import I, ZERO, interval_root, mixing, raising
import two_plaquette_vacuum_receipt as full


def labels(cutoff):
    return [(n, k) for n in range(cutoff + 1) for k in range(min(n, 1) + 1)]


def system(cutoff, beta):
    """kappa=1; exact m_y=1 sector, truncated only in n_x."""
    basis = labels(cutoff)
    index = {label: i for i, label in enumerate(basis)}
    kinetic = np.zeros((len(basis), len(basis)))
    magnetic = np.zeros_like(kinetic)
    for i, (n, k) in enumerate(basis):
        kinetic[i, i] = n * (n + 2) + 3 - k * (k + 1) / 2
        if n and k == 0:
            j = index[n, 1]
            kinetic[i, j] = kinetic[j, i] = -math.sqrt(n * (n + 2)) / 2
        if n < cutoff:
            j = index[n + 1, k]
            magnetic[i, j] = magnetic[j, i] = full.raising(n, k)
    return basis, kinetic + beta * (np.eye(len(basis)) - magnetic)


def propose(cutoff, beta):
    n = np.arange(cutoff + 1)
    radial = np.diag(n * (n + 2) + float(beta))
    radial += np.diag(np.full(cutoff, -beta / 2), 1)
    radial += np.diag(np.full(cutoff, -beta / 2), -1)
    energies, vectors = np.linalg.eigh(radial)
    p = vectors[:, 0] * np.sign(vectors[0, 0])
    basis, h = system(cutoff, beta)
    source = np.array([p[n] / 2 if k == 0 else 0 for n, k in basis])
    eta = np.linalg.solve(h - energies[0] * np.eye(len(basis)), source)
    susceptibility = source @ eta
    mismatch = np.linalg.norm(eta - 4 * susceptibility * source)
    angular = np.linalg.norm([eta[i] for i, (_, k) in enumerate(basis) if k])
    return p, float(energies[0]), eta, float(susceptibility), float(mismatch), float(angular)


def interval_norm(values):
    return interval_root(sum((v.square() for v in values), ZERO))


def exact_action(trial, cutoff, beta):
    """All m_y=1 output modes, including n=cutoff+1."""
    result = {label: ZERO for label in labels(cutoff + 1)}
    for (n, k), value in trial.items():
        result[n, k] += (n * (n + 2) + 3 - k * (k + 1) // 2 + beta) * value
        if n and k == 0:
            result[n, 1] += mixing(n, 1, 1) * value
        if k:
            result[n, 0] += mixing(n, 1, 1) * value
        result[n + 1, k] -= beta * raising(n, k) * value
        if n > k:
            result[n - 1, k] -= beta * raising(n - 1, k) * value
    return result


def decimal_enclosure(interval, digits=14):
    """Directed decimal rounding, with integer arithmetic."""
    interval = I.coerce(interval)
    scale = 10 ** digits
    low = (interval.lo * scale).__floor__()
    high = (interval.hi * scale).__ceil__()

    def show(integer):
        sign = '-' if integer < 0 else ''
        integer = abs(integer)
        return f'{sign}{integer // scale}.{integer % scale:0{digits}d}'

    return f'[{show(low)}, {show(high)}]'


def certificate(cutoff=12):
    beta = F(1)
    pf, _, etaf, _, _, _ = propose(cutoff, float(beta))
    # Rational trial; this does not assert the eigensolver was exact.
    p = [F(format(float(v / pf[0]), '.17g')) for v in pf]
    p[0] = F(1)
    norm2 = sum(v * v for v in p)
    hp = [F(0)] * (cutoff + 2)
    for n, value in enumerate(p):
        hp[n] += (n * (n + 2) + beta) * value
        hp[n + 1] -= beta * value / 2
        if n:
            hp[n - 1] -= beta * value / 2
    mu = sum(p[n] * hp[n] for n in range(cutoff + 1)) / norm2
    residual = [hp[n] - mu * (p[n] if n <= cutoff else 0) for n in range(cutoff + 2)]
    rho2 = sum(v * v for v in residual) / norm2
    # |U_n(a)| <= n+1 proves positivity and fixes the ground-state phase.
    positive_floor = p[0] - sum((n + 1) * abs(p[n]) for n in range(1, cutoff + 1))
    assert positive_floor > 0 and mu < 3
    energy_error = rho2 / (3 - mu)
    state_error = interval_root(2 * rho2 / (3 - mu) ** 2).hi
    normalized_p = [I.point(v) / interval_root(norm2) for v in p]
    trial = {label: F(format(float(v), '.17g')) for label, v in zip(labels(cutoff), etaf)}
    action = exact_action(trial, cutoff, beta)
    for label in action:
        n, k = label
        action[label] -= mu * trial.get(label, 0)
        if k == 0 and n <= cutoff:
            action[label] -= normalized_p[n] / 2
    residual_norm = interval_norm(action.values()).hi
    trial_norm = interval_root(sum(v * v for v in trial.values()))
    eta_error = F(4, 9) * (residual_norm + energy_error * trial_norm.hi + state_error / 2)
    approx_s = sum((normalized_p[n] * trial[n, 0] / 2 for n in range(cutoff + 1)), ZERO)
    s_error = eta_error / 2 + state_error * trial_norm.hi / 2
    susceptibility = approx_s + I(-s_error, s_error)
    eta_norm = I(max(F(0), trial_norm.lo - eta_error), trial_norm.hi + eta_error)
    mismatch2 = eta_norm.square() - 4 * susceptibility.square()
    assert mismatch2.lo > 0
    mismatch = interval_root(mismatch2)
    angular_trial = interval_root(sum(v * v for (n, k), v in trial.items() if k))
    angular = I(max(F(0), angular_trial.lo - eta_error), angular_trial.hi + eta_error)
    assert angular.lo > 0 and eta_error < F(1, 10 ** 12)
    print('CERTIFIED kappa=beta=1; exact rational trials and outward square-root enclosures:')
    print('  internal E0:', decimal_enclosure(I(mu - energy_error, mu)))
    print('  susceptibility <b,L^-1 b>:', decimal_enclosure(susceptibility))
    print('  ||eta||:', decimal_enclosure(eta_norm))
    print('  distance from every scalar multiple of b psi:', decimal_enclosure(mismatch))
    print('  angular k=1 norm:', decimal_enclosure(angular))
    print('  full tangent error < 1e-12; includes radial-vacuum error and omitted neighbor modes')
    return susceptibility, mismatch, angular


def diagnostics():
    # The reduced matrix must be the actual full invariant matrix restriction.
    basis, lookup, kinetic, _ = full.matrices(4)
    indices = [lookup[n, 1, k] for n, k in labels(4)]
    _, reduced = system(4, 0)
    full.close(reduced, kinetic[np.ix_(indices, indices)])
    haar = propose(8, 0)
    full.close(haar[3:], [1 / 12, 0, 0])
    for beta in (.1, .5, 1., 4., 10.):
        first, second = propose(14, beta), propose(20, beta)
        full.close(first[3:], second[3:], atol=2e-13, rtol=2e-10)
        print(f'DIAGNOSTIC beta={beta:g}: susceptibility={second[3]:.12g}, '
              f'q-only distance={second[4]:.12g}, angular norm={second[5]:.12g}')
    small = []
    for beta in (.04, .02):
        result = propose(12, beta)
        small.append(((result[3] - 1 / 12) / beta ** 2, result[4] / beta))
    target = np.array([1 / 8424, 7 / 1404])
    assert np.all(np.abs(np.array(small[1]) - target) < np.abs(np.array(small[0]) - target))
    full.close(small[1], target, atol=5e-7, rtol=1e-4)
    # Independently perturb the whole two-plaquette matrix with unequal couplings.
    # This check distinguishes the actual ground-vector derivative from a
    # response obtained by changing only a readout or a fitted scalar.
    cutoff = 6
    basis, lookup, kinetic, _ = full.matrices(cutoff)
    ma, mb = np.zeros_like(kinetic), np.zeros_like(kinetic)
    for i, (n, m, k) in enumerate(basis):
        for label, coefficient, operator in (((n + 1, m, k), full.raising(n, k), ma),
                                               ((n, m + 1, k), full.raising(m, k), mb)):
            if label in lookup:
                j = lookup[label]
                operator[i, j] = operator[j, i] = coefficient
    h = kinetic + np.eye(len(basis)) - ma
    step = 1e-4
    grounds = []
    for coupling in (-step, step):
        _, vectors = np.linalg.eigh(h - coupling * mb)
        grounds.append(vectors[:, 0] * np.sign(vectors[0, 0]))
    derivative = (grounds[1] - grounds[0]) / (2 * step)
    reference = np.zeros(len(basis))
    reduced_eta = propose(cutoff, 1.)[2]
    for label, value in zip(labels(cutoff), reduced_eta):
        n, k = label
        reference[lookup[n, 1, k]] = value
    full.close(derivative, reference, atol=2e-10, rtol=2e-7)
    print('PASS full-matrix derivative, exact sector restriction, Haar control, '
          'cutoff refinement and independent weak-coupling coefficients')


if __name__ == '__main__':
    diagnostics()
    certificate()
