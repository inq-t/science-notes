"""Finite controls for the connected kinetic majorant (KF2--KF17).

The rotor branch uses exact Fraction Fourier dictionaries, including
overlapping interaction labels. Its instantaneous local norm diverges
with the number of links; the actual nonconstant kinetic inverse stays
bounded. Scalar mode inequalities and source arithmetic are exact.

The SU(2) branch uses actual finite spin representations, Q=-2 Tr and
T_a=-i J_a. It checks cross-Casimir channels, multiplication/readout,
and trace-norm contraction for non-Hermitian matrices, including a
genuine multiplicity-two channel in three spin-one-half factors.
Those matrix tests are floating-point diagnostics. No finite sample
proves the infinite Fourier theorem, the time-projective completion,
an interacting mass gap, or a continuum limit.
"""

from fractions import Fraction as F
from itertools import product
import math

import numpy as np


def put(poly, key, value):
    poly[key] = poly.get(key, F(0))+value
    if not poly[key]:
        del poly[key]


def cosine(mode, scale=F(1)):
    return {mode: scale/2, tuple(-x for x in mode): scale/2}


def local_norm(family, weights, links):
    return max(sum(weights[label]*abs(k[e])*sum(map(abs, k))*abs(c)
                   for label, poly in family.items() for k, c in poly.items())
               for e in range(links))


def gamma(family, other):
    result = {}
    for left, poly in family.items():
        for right, second in other.items():
            out = result.setdefault(left | right, {})
            for p, a in poly.items():
                for q, b in second.items():
                    put(out, tuple(x+y for x, y in zip(p, q)),
                        -sum(x*y for x, y in zip(p, q))*a*b)
    return {label: poly for label, poly in result.items() if poly}


def inverse_nonconstant(family):
    """K=-Delta: remove the Haar constant BEFORE dividing by |k|_2^2."""
    return {label: {k: c/sum(x*x for x in k) for k, c in poly.items()
                    if any(k)} for label, poly in family.items()}


def rotor_counterexample():
    print('rotor N: instantaneous norm; kinetic-inverse norm')
    for n in (4, 8, 16, 32, 64):
        full = frozenset(range(n))
        # Cycle supports E(p_j)={j,j+1}; mu=log(2), diam(full)=n/2.
        weights = {frozenset((j,)): F(1) for j in range(n)}
        weights[full] = F(2**(n//2))
        u = {full: cosine((1,)*n, 1/(n*weights[full]))}
        v = {}
        for j in range(n):
            poly = {}
            for e in (j, (j+1) % n):
                mode = tuple(int(i == e) for i in range(n))
                for k, c in cosine(mode, F(1, 2)).items():
                    put(poly, k, c)
            v[frozenset((j,))] = poly
        assert local_norm(u, weights, n) == local_norm(v, weights, n) == 1
        joined = gamma(u, v)
        assert set(joined) == {full}
        raw = local_norm(joined, weights, n)
        damped = local_norm(inverse_nonconstant(joined), weights, n)
        assert raw == F(n*n+1, n)
        assert damped == F(n*n+2*n-1, n*(n+3)) < 1
        assert raw > n and raw > 4*damped
        print(f'  {n}: {raw}; {damped}')
    # The discarded constant really occurs in Gamma, rather than being
    # an empty case in inverse_nonconstant().
    one = {frozenset((0,)): cosine((1,))}
    square = gamma(one, one)
    assert square[frozenset((0,))][(0,)] == F(1, 2)
    assert (0,) not in inverse_nonconstant(square)[frozenset((0,))]
    print('PASS exact overlap counterexample, damping compensation, and zero-mode exclusion.')


def scalar_majorant_controls():
    modes = [k for k in product(range(-2, 3), repeat=3) if any(k)]
    checked, constant_outputs = 0, 0
    for p in modes:
        for q in modes:
            r = tuple(x+y for x, y in zip(p, q))
            energy = sum(x*x for x in r)
            if not energy:
                constant_outputs += 1
                continue
            cross = abs(sum(x*y for x, y in zip(p, q)))
            overlap = sum(abs(x*y) for x, y in zip(p, q))
            assert sum(map(abs, r)) <= energy
            for e in range(3):
                lhs = F(abs(r[e])*sum(map(abs, r))*cross, energy)
                rhs = (abs(p[e])+abs(q[e]))*overlap
                assert lhs <= rhs
                checked += 1
    assert constant_outputs == len(modes)
    # Without the spectral denominator the same inequality fails.
    assert 2*6*3 > (1+1)*3
    assert F(2*6*3, 12) <= (1+1)*3

    # Actual four-active-link cosine coefficients; shared incidence is two.
    supports = ((0, 1, 2, 3), (2, 3, 4, 5))
    coupling, kappa = F(1, 100), F(3, 2)
    source = {}
    for j, support in enumerate(supports):
        mode = tuple(int(e in support) for e in range(6))
        source[frozenset((j,))] = {
            k: coupling*c/(kappa*sum(x*x for x in k))
            for k, c in cosine(mode).items()}
    s = local_norm(source, {key: F(1) for key in source}, 6)
    assert s == coupling*2/kappa
    constant = F(4)  # 2 exp(mu), mu=log(2).
    assert 4*constant*s < 1 and s+constant*(2*s)**2 <= 2*s
    print(f'PASS {checked} exact anchored Fourier inequalities; source={s}, '
          f'Picard contraction bound={4*constant*s}.')


def close(actual, expected, tol=3e-11):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert np.all(np.isfinite(actual)) and np.all(np.isfinite(expected))
    error = float(np.max(np.abs(actual-expected)))
    assert error <= tol*(1+float(np.max(np.abs(expected)))), error


def nuclear(matrix):
    return float(np.linalg.svd(matrix, compute_uv=False).sum())


def spins(j):
    values = np.arange(j, -j-1, -1)
    raising = np.zeros((len(values), len(values)), dtype=complex)
    for col, m in enumerate(values):
        if col:
            raising[col-1, col] = math.sqrt((j-m)*(j+m+1))
    lowering = raising.conj().T
    hermitian = ((raising+lowering)/2, (raising-lowering)/(2j), np.diag(values))
    return tuple(-1j*x for x in hermitian)


def group_element(generators, axis=(2, -1, 3), angle=0.71):
    direction = np.asarray(axis, float)
    direction /= np.linalg.norm(direction)
    antihermitian = sum(x*t for x, t in zip(direction, generators))
    eigenvalues, vectors = np.linalg.eigh(1j*antihermitian)
    return (vectors*np.exp(-1j*angle*eigenvalues)) @ vectors.conj().T


def random_matrix(size, rng):
    matrix = rng.normal(size=(size, size))+1j*rng.normal(size=(size, size))
    assert np.linalg.norm(matrix-matrix.conj().T) > 0.1
    return matrix/nuclear(matrix)


def spin_pair_controls():
    rng = np.random.default_rng(48131)
    ratios, channel_count = [], 0
    for j, ell in product((0.5, 1.0, 1.5), repeat=2):
        tj, tl = spins(j), spins(ell)
        dj, dl = len(tj[0]), len(tl[0])
        cj, cl = j*(j+1), ell*(ell+1)
        close(-sum(t@t for t in tj), cj*np.eye(dj))
        close(-sum(t@t for t in tl), cl*np.eye(dl))
        total = tuple(np.kron(a, np.eye(dl))+np.kron(np.eye(dj), b)
                      for a, b in zip(tj, tl))
        casimir = -sum(t@t for t in total)
        cross = sum(np.kron(a, b) for a, b in zip(tj, tl))
        eigenvalues, vectors = np.linalg.eigh(casimir)
        close(cross, ((cj+cl)*np.eye(dj*dl)-casimir)/2)
        a, b = random_matrix(dj, rng), random_matrix(dl, rng)
        coefficient = np.kron(a, b)
        gj, gl = group_element(tj), group_element(tl)
        joint = np.kron(gj, gl)
        multiplication, response, channel_norm = 0j, 0j, 0.0
        for spin in np.arange(abs(j-ell), j+ell+1, 1):
            c = spin*(spin+1)
            block = vectors[:, np.abs(eigenvalues-c) < 1e-8]
            assert block.shape[1] == round(2*spin+1)
            channel = block.conj().T @ coefficient @ block
            representation = block.conj().T @ joint @ block
            gamma_value = (cj+cl-c)/2
            close(cross@block, gamma_value*block)
            assert abs(gamma_value) <= math.sqrt(cj*cl)+1e-12
            assert math.sqrt(c) <= math.sqrt(cj)+math.sqrt(cl)+1e-12
            if c:
                assert 1/math.sqrt(c) <= 1/math.sqrt(0.75)+1e-12
            multiplication += np.trace(channel@representation)
            response += gamma_value*np.trace(channel@representation)
            channel_norm += nuclear(channel)
            channel_count += 1
        close(multiplication, np.trace(a@gj)*np.trace(b@gl))
        direct = sum(np.trace(a@ta@gj)*np.trace(b@tb@gl)
                     for ta, tb in zip(tj, tl))
        close(response, direct)
        assert channel_norm <= nuclear(a)*nuclear(b)+1e-11
        ratios.append(channel_norm)
    assert min(ratios) < 0.95  # Pinching really discards some cross-channel data.
    print(f'PASS {channel_count} actual SU(2) channels: Casimirs, direct Lie '
          f'response and non-Hermitian trace pinching; ratios '
          f'{min(ratios):.6f}..{max(ratios):.6f}.')


def multiplicity_control():
    half = spins(0.5)
    ident = np.eye(2)
    embed = lambda t, site: np.kron(np.kron(t if site == 0 else ident,
                                          t if site == 1 else ident),
                                  t if site == 2 else ident)
    total = tuple(sum(embed(t, site) for site in range(3)) for t in half)
    pair = tuple(embed(t, 0)+embed(t, 1) for t in half)
    casimir = -sum(t@t for t in total)
    pair_casimir = -sum(t@t for t in pair)
    jz = 1j*total[2]
    # These three self-adjoint matrices commute; this separates both
    # spin-1/2 copies by the first pair's spin, then fixes a highest weight.
    _, vectors = np.linalg.eigh(casimir+10*jz+100*pair_casimir)
    jminus = 1j*total[0]+total[1]

    def copy(spin, pair_spin):
        selected = []
        for vector in vectors.T:
            if (abs(np.vdot(vector, casimir@vector)-spin*(spin+1)) < 1e-8
                    and abs(np.vdot(vector, jz@vector)-spin) < 1e-8
                    and abs(np.vdot(vector, pair_casimir@vector)
                            -pair_spin*(pair_spin+1)) < 1e-8):
                selected.append(vector)
        assert len(selected) == 1
        basis = [selected[0]]
        for m in np.arange(spin, -spin, -1):
            basis.append(jminus@basis[-1]/math.sqrt((spin+m)*(spin-m+1)))
        return np.column_stack(basis)

    first, second, high = copy(0.5, 0), copy(0.5, 1), copy(1.5, 1)
    low = np.column_stack([first[:, 0], second[:, 0], first[:, 1], second[:, 1]])
    unitary = np.column_stack([low, high])
    close(unitary.conj().T@unitary, np.eye(8))
    joint = np.kron(np.kron(group_element(half), group_element(half)), group_element(half))
    close(low.conj().T@joint@low, np.kron(group_element(half), np.eye(2)))
    close(high.conj().T@joint@high, group_element(spins(1.5)))
    matrix = random_matrix(8, np.random.default_rng(1147))
    raw_low = low.conj().T@matrix@low
    # Order is representation index tensor multiplicity index.
    traced = np.einsum('aibi->ab', raw_low.reshape(2, 2, 2, 2))
    upper = high.conj().T@matrix@high
    ratio = nuclear(traced)+nuclear(upper)
    assert ratio <= nuclear(matrix)+1e-11
    close(np.trace(matrix@joint), np.trace(traced@group_element(half))
          +np.trace(upper@group_element(spins(1.5))))
    # Replacing multiplicity trace by its normalized average is wrong.
    positive = np.eye(8)/8
    low_positive = low.conj().T@positive@low
    low_trace = np.einsum('aibi->ab', low_positive.reshape(2, 2, 2, 2))
    close(np.trace(low_trace)+np.trace(high.conj().T@positive@high), 1)
    assert abs(np.trace(low_trace/2)+np.trace(high.conj().T@positive@high)-1) > 0.2
    print(f'PASS actual three-spin multiplicity-two contraction/readout; '
          f'non-Hermitian ratio={ratio:.6f}; normalized-trace substitution rejected.')


if __name__ == '__main__':
    rotor_counterexample()
    scalar_majorant_controls()
    spin_pair_controls()
    multiplicity_control()
    print('PASS finite controls only: no numerical claim of an infinite-series '
          'theorem, projective time completion, physical gap or continuum limit.')
