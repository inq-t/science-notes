"""Coordinate elimination of actual Ising laws and nonnegative majorants."""

import itertools
import math

import numpy as np


RNG = np.random.default_rng(11601)


def spectral_radius(a):
    return max(abs(np.linalg.eigvals(a)), default=0)


def eliminate(c, retained):
    hidden = tuple(i for i in range(len(c)) if i not in retained)
    rr = c[np.ix_(retained, retained)]
    rh = c[np.ix_(retained, hidden)]
    hr = c[np.ix_(hidden, retained)]
    hh = c[np.ix_(hidden, hidden)]
    effective = rr + rh @ np.linalg.solve(np.eye(len(hidden)) - hh, hr)
    diagonal = np.diag(effective)
    normalized = effective.copy()
    np.fill_diagonal(normalized, 0)
    normalized /= (1 - diagonal)[:, None]
    return effective, normalized, diagonal


def conditional_influences(states, weights):
    size = states.shape[1]
    tables = []
    for i in range(size):
        table = {}
        others = tuple(k for k in range(size) if k != i)
        for state, weight in zip(states, weights):
            key = tuple(state[k] for k in others)
            total, plus = table.get(key, (0.0, 0.0))
            table[key] = (total + weight, plus + (weight if state[i] == 1 else 0))
        tables.append({key: plus / total for key, (total, plus) in table.items()})
    result = np.zeros((size, size))
    for i in range(size):
        others = tuple(k for k in range(size) if k != i)
        for j in others:
            pos = others.index(j)
            for key, prob in tables[i].items():
                flipped = list(key)
                flipped[pos] *= -1
                result[i, j] = max(result[i, j], abs(prob - tables[i][tuple(flipped)]))
    return result


def ising_checks():
    count = 0
    for leaves in (2, 3):
        for coupling in (0.1, 0.4, math.log(3), 2.0):
            t = math.tanh(coupling)
            states = np.array(list(itertools.product((-1, 1), repeat=leaves + 1)))
            weights = np.exp(coupling * states[:, 0] * states[:, 1:].sum(axis=1))
            weights /= weights.sum()
            c = conditional_influences(states, weights)
            retained_states = np.array(list(itertools.product((-1, 1), repeat=leaves)))
            marg = np.zeros(len(retained_states))
            for idx, state in enumerate(retained_states):
                marg[idx] = weights[np.all(states[:, 1:] == state, axis=1)].sum()
            actual = conditional_influences(retained_states, marg)
            effective, normalized, diagonal = eliminate(c, tuple(range(1, leaves + 1)))
            assert np.all(actual <= normalized + 1e-12)
            if leaves == 2:
                assert np.allclose(c[0, 1:], t / (1 + t * t))
                assert np.allclose(effective, t * t / (1 + t * t))
                assert np.allclose(actual, normalized)
                assert abs(actual[0, 1] - t * t) < 1e-12
                assert effective[0, 1] < actual[0, 1]
            else:
                assert np.allclose(c[0, 1:], t)
                assert np.allclose(effective, t * t)
                assert abs(spectral_radius(c) - math.sqrt(3) * t) < 1e-12
                assert abs(spectral_radius(normalized) - 2 * t * t / (1 - t * t)) < 1e-10
                assert abs(spectral_radius(actual) - 2 * t * t / (1 + t * t)) < 1e-12
                if abs(coupling - math.log(3)) < 1e-12:
                    assert spectral_radius(c) > 1
                    assert spectral_radius(normalized) > 1
                    assert abs(spectral_radius(actual) - 32 / 41) < 1e-12
            count += 1
    return count


def matrix_checks():
    count = 0
    for size in (3, 5, 8):
        retained = tuple(range(0, size, 2))
        hidden = tuple(i for i in range(size) if i not in retained)
        for trial in range(40):
            c = RNG.uniform(0, 1, (size, size))
            np.fill_diagonal(c, 0)
            q = 0.2 + 0.75 * RNG.random()
            c *= q / c.sum(axis=1).max()
            effective, normalized, diagonal = eliminate(c, retained)
            assert np.all(diagonal < 1)
            assert effective.sum(axis=1).max() <= q + 1e-12
            assert normalized.sum(axis=1).max() <= q + 1e-12
            actual_resolvent = np.linalg.inv(np.eye(size) - c)[np.ix_(retained, retained)]
            returned = np.linalg.solve(np.eye(len(retained)) - normalized, np.diag(1 / (1 - diagonal)))
            assert np.allclose(actual_resolvent, returned, atol=2e-12)
            assert np.allclose(actual_resolvent, np.linalg.inv(np.eye(len(retained)) - effective))
            # Test both sides of the spectral threshold while the hidden block stays stable.
            unit = c / spectral_radius(c)
            for factor in (0.85, 1.15):
                candidate = factor * unit
                if spectral_radius(candidate[np.ix_(hidden, hidden)]) >= 1:
                    continue
                e, bar, diag = eliminate(candidate, retained)
                inside = spectral_radius(candidate) < 1
                assert inside == (spectral_radius(e) < 1)
                assert inside == (bool(np.all(diag < 1)) and spectral_radius(bar) < 1)
                count += 1
    # A two-site loop cannot be certified by erasing its induced diagonal.
    c = np.array(((0.0, 1.2), (1.2, 0.0)))
    e, _, diagonal = eliminate(c, (0,))
    assert diagonal[0] > 1 and spectral_radius(c) > 1
    assert abs(e[0, 0] - 1.44) < 1e-12
    return count


if __name__ == "__main__":
    print("PASS actual Ising conditional laws and marginal improvement:", ising_checks())
    print("PASS response resolvents, row preservation and spectral threshold:", matrix_checks())
    print("Scope: coordinate comparison, not nonlinear blocking or a physical mass-gap proof.")
