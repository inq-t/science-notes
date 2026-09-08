"""Actual charged-link spectral moments for a finite SU(2) Wilson plaquette.

The supplied RAW Hamiltonian is kappa*sum_e(-Delta_e)+lambda*(1-q_hol)
on four links with distinct endpoints, Q=-2Tr and q_hol=Tr(Hol)/2.
Its invariant positive ground is approximated in the complete character
basis; the probes are charged single-link representation coefficients,
not invariant plaquette characters. No charged spectrum is truncated.

The Chebyshev recurrence and omitted-mode residual follow the existing
prepared_vacuum_subdivision_receipt.py, with its class kinetic coefficient
set to 4*kappa. Matrix generators, full four-link derivatives, and Haar
entry moments are evaluated independently below. Floating-point cutoff
and quadrature checks are finite diagnostics, not interval certificates,
an infinite-volume gap, or a four-dimensional Yang--Mills construction.
"""

from __future__ import annotations

import math

import numpy as np


PAULI = np.array(([[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]))
TA = -0.5j*PAULI
ID2 = np.eye(2, dtype=complex)


def close(actual, expected, *, atol=2e-11, rtol=2e-10):
    assert np.all(np.isfinite(actual)) and np.all(np.isfinite(expected))
    assert np.allclose(actual, expected, atol=atol, rtol=rtol), (actual, expected)


def characters(coefficients, q):
    """Polynomial U_n evaluation and its analytic radial derivative."""
    q = np.asarray(q, dtype=float)
    prev, curr = np.ones_like(q), 2*q
    dprev, dcurr = np.zeros_like(q), 2*np.ones_like(q)
    value, slope = coefficients[0]*prev, np.zeros_like(q)
    if len(coefficients) > 1:
        value, slope = value+coefficients[1]*curr, coefficients[1]*dcurr
    for coefficient in coefficients[2:]:
        nxt, dnxt = 2*q*curr-prev, 2*curr+2*q*dcurr-dprev
        value, slope = value+coefficient*nxt, slope+coefficient*dnxt
        prev, curr, dprev, dcurr = curr, nxt, dcurr, dnxt
    return value, slope


def haar_radial(order):
    angles = math.pi*np.arange(1, order+1)/(order+1)
    return np.cos(angles), 2*np.sin(angles)**2/(order+1)


def ground(cutoff, kappa, coupling):
    n = np.arange(cutoff+1)
    diagonal = kappa*n*(n+2)+coupling
    off = np.full(cutoff, -coupling/2)
    matrix = np.diag(diagonal)+np.diag(off, 1)+np.diag(off, -1)
    energies, vectors = np.linalg.eigh(matrix)
    coefficients = vectors[:, 0]*np.sign(vectors[0, 0])
    residual_inside = matrix@coefficients-energies[0]*coefficients
    # H psi_N has exactly this one omitted character coefficient.
    residual = np.linalg.norm(np.r_[residual_inside, -coupling*coefficients[-1]/2])
    return coefficients, float(energies[0]), float(residual)


def radial_moments(coefficients, order):
    a, weight = haar_radial(order)
    psi, slope = characters(coefficients, a)
    assert psi.min() > 0
    density = weight*psi**2
    # Raw one-link score: grad_e log psi=(psi'/psi)*grad_e a.
    fisher = float(weight@((1-a*a)*slope*slope)/4)
    return float(density.sum()), float(density@a), fisher


def spin_generators(twice_spin):
    j, d = twice_spin/2, twice_spin+1
    m = j-np.arange(d)
    plus = np.zeros((d, d), complex)
    for column in range(1, d):
        plus[column-1, column] = math.sqrt((j-m[column])*(j+m[column]+1))
    minus = plus.conj().T
    angular = np.array([(plus+minus)/2, (plus-minus)/(2j), np.diag(m)])
    generators = -1j*angular
    casimir = -sum(t@t for t in generators)
    close(casimir, j*(j+1)*np.eye(d))
    close(generators[0]@generators[1]-generators[1]@generators[0], generators[2])
    return generators, angular


def exp_antihermitian(matrix):
    values, vectors = np.linalg.eigh(1j*matrix)
    return (vectors*np.exp(-1j*values))@vectors.conj().T


def represented(rotation_vector, generators):
    return exp_antihermitian(np.einsum('a,aij->ij', rotation_vector, generators))


def product(matrices):
    result = np.eye(matrices[0].shape[0], dtype=complex)
    for matrix in matrices:
        result = result@matrix
    return result


def haar_entry_tensors(generators, angular, azimuths, latitudes):
    """Actual Euler-matrix quadrature; no Schur identity is substituted.

    alpha in [0,2pi), gamma in [0,4pi), and cos(beta) uniform give SU(2)
    Haar. These orders integrate all displayed finite-spin moments.
    """
    d = len(angular[0])
    alpha = 2*math.pi*np.arange(azimuths)/azimuths
    gamma = 4*math.pi*np.arange(azimuths)/azimuths
    z, wz = np.polynomial.legendre.leggauss(latitudes)
    m = np.diag(angular[2]).real
    left = np.exp(-1j*alpha[:, None]*m)
    right = np.exp(-1j*gamma[:, None]*m)
    norm = np.zeros((d, d))
    cross = np.zeros((3, d, d), complex)
    gradient = np.zeros((3, 3, d, d), complex)
    for zz, weight in zip(z, wz/2):
        middle = exp_antihermitian(math.acos(zz)*generators[1])
        group = (left[:, None, :, None]*middle[None, None, :, :]
                 *right[None, :, None, :]).reshape(-1, d, d)
        derivatives = np.einsum('aik,skj->saij', generators, group)
        # Each matrix coefficient is normalized as sqrt(d)*D_mn.
        norm += d*weight*np.mean(abs(group)**2, axis=0)
        cross += d*weight*np.mean(group.conj()[:, None]*derivatives, axis=0)
        gradient += d*weight*np.einsum('saij,sbij->abij', derivatives.conj(), derivatives)/len(group)
    close(norm, np.ones_like(norm))
    close(np.einsum('aaij->ij', gradient).real, -np.trace(sum(t@t for t in generators)).real/d)
    return norm, cross, gradient


def actual_score_moments(coefficients, order):
    """Differentiate actual holonomy Pauli matrices before isotropic averaging."""
    a, weight = haar_radial(order)
    psi, slope = characters(coefficients, a)
    mean, covariance = np.zeros(3), np.zeros((3, 3))
    samples = []
    for aa, ww, pp, dd in zip(a, weight, psi, slope):
        for direction in np.r_[np.eye(3), -np.eye(3)]:
            holonomy = aa*ID2+2*math.sqrt(1-aa*aa)*np.einsum('a,aij->ij', direction, TA)
            da = np.array([np.trace(t@holonomy).real/2 for t in TA])
            score, mass = (dd/pp)*da, ww*pp*pp/6
            mean += mass*score
            covariance += mass*np.outer(score, score)
            samples.append((mass, score))
    close(mean, np.zeros(3))
    return mean, covariance, samples


def raw_hamiltonian_check(coefficients, energy, kappa, coupling, generators):
    """Full four-link finite differences on psi(Hol)*D_j(U_0)."""
    rotations = np.array([[.7, -.2, .4], [-.3, .8, .1], [.2, .4, -.5], [.6, .1, -.7]])
    edges = [represented(v, TA) for v in rotations]
    feature = represented(rotations[0], generators)
    holonomy = product(edges)
    a = np.trace(holonomy).real/2
    psi, slope = characters(coefficients, a)
    da = np.array([np.trace(t@holonomy).real/2 for t in TA])
    score = (slope/psi)*da
    c = -np.trace(sum(t@t for t in generators)).real/len(feature)
    target = kappa*c*feature-2*kappa*np.einsum('a,aij,jk->ik', score, generators, feature)
    base, laplacian, step = psi*feature, np.zeros_like(feature), 8e-4
    for edge in range(4):
        for axis in range(3):
            shifted = []
            for multiple in (-2, -1, 1, 2):
                h = multiple*step
                values = edges.copy()
                values[edge] = exp_antihermitian(h*TA[axis])@values[edge]
                q = np.trace(product(values)).real/2
                matrix = exp_antihermitian(h*generators[axis])@feature if edge == 0 else feature
                shifted.append(characters(coefficients, q)[0]*matrix)
            laplacian += (-shifted[3]+16*shifted[2]-30*base+16*shifted[1]-shifted[0])/(12*step**2)
    actual = (-kappa*laplacian+coupling*(1-a)*base-energy*base)/psi
    close(actual, target, atol=2e-7, rtol=2e-7)
    return float(np.max(abs(actual-target)))


def charged_moments(coefficients, kappa, twice_spin, radial_order, azimuths, latitudes):
    generators, angular = spin_generators(twice_spin)
    c = twice_spin*(twice_spin+2)/4
    mean_score, covariance, samples = actual_score_moments(coefficients, radial_order)
    norm, cross, gradient = haar_entry_tensors(generators, angular, azimuths, latitudes)
    first = kappa*c*norm-2*kappa*np.einsum('a,aij->ij', mean_score, cross)
    variance = 4*kappa*kappa*np.einsum('ab,abij->ij', covariance, gradient).real
    radial_fisher = radial_moments(coefficients, radial_order)[2]
    expected = 4*kappa*kappa*c*radial_fisher/3
    close(first, kappa*c*np.ones_like(first))
    close(variance, expected*np.ones_like(variance))
    # Independently apply the actual differential L to the whole feature
    # D_j(U)/sqrt(d), at a noncommuting U, and integrate its norms directly.
    unitary = represented(np.array([.31, -.72, .49]), generators)
    d = len(unitary)
    direct_first, direct_variance, direct_second = 0j, 0., 0.
    for mass, score in samples:
        drift = -2*kappa*np.einsum('a,aij,jk->ik', score, generators, unitary)
        applied = kappa*c*unitary+drift
        direct_first += mass*np.vdot(unitary, applied)/d
        direct_variance += mass*np.vdot(drift, drift).real/d
        direct_second += mass*np.vdot(applied, applied).real/d
    close(direct_first, kappa*c)
    close(direct_variance, expected)
    close(direct_second, (kappa*c)**2+expected)
    close(covariance, radial_fisher*np.eye(3)/3)
    assert expected > 0
    return float(first.real.mean()), float(variance.mean()), float(direct_second)


def main():
    kappa, coupling = 1., 1.
    print('Charged probe spectral-width receipt: actual finite four-link Wilson plaquette')
    rows = []
    for cutoff in (4, 8, 16):
        coefficients, energy, residual = ground(cutoff, kappa, coupling)
        values = [radial_moments(coefficients, order) for order in (48, 96)]
        close(values[0], values[1])
        norm, mean_a, fisher = values[-1]
        close(norm, 1.)
        close(fisher, (energy-coupling*(1-mean_a))/(4*kappa))
        assert 0 < fisher < (coupling/kappa)**2
        rows.append((energy, fisher, residual))
        print(f'  cutoff {cutoff:2d}: E0={energy:.12g}, I_e={fisher:.12g}, omitted-mode residual={residual:.3e}')
    close(rows[1][:2], rows[2][:2])
    assert rows[0][2] > 1e5*rows[-1][2] and rows[-1][2] < 1e-12
    print('PASS independent radial score integral equals the kinetic part of actual vacuum energy.')
    for twice_spin in (1, 2, 4, 8):
        low = charged_moments(coefficients, kappa, twice_spin, 48, 11, 10)
        high = charged_moments(coefficients, kappa, twice_spin, 96, 19, 14)
        close(low, high)
        generators = spin_generators(twice_spin)[0]
        derivative_error = raw_hamiltonian_check(coefficients, energy, kappa, coupling, generators)
        print(f'  spin {twice_spin/2:g}: first={high[0]:.12g}, variance={high[1]:.12g}, '
              f'second={high[2]:.12g}, raw-link differential error={derivative_error:.3e}')
    print('PASS actual matrix-entry Haar moments and direct L feature norms for all displayed spins; '
          'radial and Euler quadrature refinements agree.')
    print('PASS full four-link Hamiltonian finite differences include the charged link and all vacuum derivatives.')
    print('Finite diagnostics only: no charged-spectrum truncation, spectral tail simulation, '
          'mass-gap lower bound, continuum limit, or volume-uniform product theorem is claimed.')


if __name__ == '__main__':
    main()
