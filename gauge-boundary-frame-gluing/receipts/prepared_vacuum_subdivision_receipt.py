"""Actual one-plaquette vacuum and its prepared-source subdivision response.

The physical CLASS Hamiltonian is supplied: K D_Q+lambda(1-q), q=Tr/2,
Q=-2Tr. Character truncations approximate its vacuum, not a guessed tilt.
An N-edge cycle has physical coefficients K/N and heat ages L/N, so the
same physical class operator and vacuum are held fixed under subdivision.
The source-clock calibration E_star=K/(2L) is declared, not derived.
Floating-point residuals and finite quadratures do not certify a physical
mass gap, a four-dimensional limit, or an infinite-volume vacuum.
"""

from __future__ import annotations

import itertools
import math

import numpy as np


PAULI = np.array(([[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]))
GENERATORS, IDENTITY = -.5j*PAULI, np.eye(2, dtype=complex)


def close(actual, expected, *, rtol=2e-11, atol=4e-13):
    assert np.all(np.isfinite(actual)) and np.all(np.isfinite(expected))
    assert np.allclose(actual, expected, rtol=rtol, atol=atol), (actual, expected)


def character_values(coefficients, q):
    """Evaluate a sum of U_n(q) and its first two radial derivatives."""
    q = np.asarray(q)
    previous, current = np.ones_like(q), 2*q
    dp, dc, ddp, ddc = np.zeros_like(q), np.full_like(q, 2.), np.zeros_like(q), np.zeros_like(q)
    value, derivative, second = coefficients[0]*previous, np.zeros_like(q), np.zeros_like(q)
    if len(coefficients) > 1:
        value, derivative = value+coefficients[1]*current, coefficients[1]*dc
    for coefficient in coefficients[2:]:
        following, df = 2*q*current-previous, 2*current+2*q*dc-dp
        ddf = 4*dc+2*q*ddc-ddp
        value, derivative, second = value+coefficient*following, derivative+coefficient*df, second+coefficient*ddf
        previous, current, dp, dc, ddp, ddc = current, following, dc, df, ddc, ddf
    return value, derivative, second


def haar_quadrature(order):
    theta = np.arange(1, order+1)*math.pi/(order+1)
    return np.cos(theta), 2*np.sin(theta)**2/(order+1)


def vacuum_checks(kinetic, coupling):
    eigenvectors, rows = [], []
    for cutoff in (4, 8, 16, 32):
        indices = np.arange(cutoff+1)
        casimir = indices*(indices+2)/4
        off_diagonal = np.full(cutoff, -coupling/2)
        hamiltonian = (np.diag(kinetic*casimir+coupling)
                       + np.diag(off_diagonal, 1)+np.diag(off_diagonal, -1))
        energies, vectors = np.linalg.eigh(hamiltonian)
        energy, coefficients = energies[0], vectors[:, 0]
        if coefficients[0] < 0:
            coefficients = -coefficients
        close(coefficients@coefficients, 1)
        # This includes the ONLY omitted matrix component of H*psi_N.
        # It is an actual full character-space residual, evaluated in
        # floating point, not just the finite eigensolver's residual.
        inside = hamiltonian@coefficients-energy*coefficients
        omitted = -coupling*coefficients[-1]/2
        residual = math.sqrt(float(inside@inside)+omitted*omitted)
        assert 0 < energy <= coupling and energy < .75*kinetic
        q, weights = haar_quadrature(192)
        psi, derivative, second = character_values(coefficients, q)
        assert np.min(psi) > 0
        close(weights@(psi*psi), 1)
        radial_d = -(1-q*q)*second/4+3*q*derivative/4
        radial_residual = kinetic*radial_d+coupling*(1-q)*psi-energy*psi
        close(np.sqrt(weights@(radial_residual*radial_residual)), residual, atol=2e-13)
        fisher_scalar = float(weights@((1-q*q)*derivative*derivative)/3)
        close(fisher_scalar, 4*np.dot(casimir, coefficients*coefficients)/3)
        rows.append((cutoff, energy, residual, fisher_scalar, float(psi.min())))
        eigenvectors.append(coefficients)
    close(np.array([row[1] for row in rows[1:]]), rows[-1][1])
    close(np.array([row[3] for row in rows[1:]]), rows[-1][3])
    assert rows[0][2] > 1e5*rows[-1][2]
    assert rows[-1][2] < 1e-12
    coefficients = eigenvectors[-1]
    refined = []
    for order in (96, 192, 384):
        q, weights = haar_quadrature(order)
        psi, derivative, _ = character_values(coefficients, q)
        score_radial = 2*derivative/psi
        density = psi*psi
        score_norm = (1-q*q)*score_radial*score_radial/4
        refined.append(np.array([weights@density, weights@(density*score_norm)/3,
                                 weights@(density*(1-q*q)/4)]))
    close(refined, np.broadcast_to(refined[-1], (3, 3)))
    endpoints = character_values(coefficients, np.array([-1., 1.]))[0]
    assert endpoints.min() > 0
    print("Character cutoff: E0, full-space residual norm, s=E_w|grad log w|^2/3, sampled min psi")
    for cutoff, energy, residual, scalar, minimum in rows:
        print(f"  {cutoff:2d}: {energy:.12g}, {residual:.3e}, {scalar:.12g}, {minimum:.12g}")
    print("PASS character/Casimir and radial kinetic identities, positive sampled vacuum, "
          "96/192/384-point score quadratures; residual is a numerical finite-model "
          "check, not a mass-gap proof or a rigorous interval-arithmetic enclosure.")
    return coefficients, rows[-1][1], refined[-1][1], refined[-1][2]


def finite_gauge_frames():
    """Binary tetrahedral matrices integrate adjoint first/second moments."""
    quaternions = list(np.eye(4))+list(-np.eye(4))
    quaternions += [np.array(signs)/2 for signs in itertools.product((-1, 1), repeat=4)]
    groups, adjoints = [], []
    for q in quaternions:
        group = q[0]*IDENTITY+2*np.einsum("a,aij->ij", q[1:], GENERATORS)
        close(group.conj().T@group, IDENTITY)
        groups.append(group)
        adjoints.append(np.array([[-2*np.trace(ta@group@tb@group.conj().T).real
                                    for tb in GENERATORS] for ta in GENERATORS]))
    rotations = np.array(adjoints)
    close(rotations.mean(axis=0), np.zeros((3, 3)))
    close(np.einsum("rij,rkl->ijkl", rotations, rotations)/24,
          np.einsum("ik,jl->ijkl", np.eye(3), np.eye(3))/3)
    return groups, rotations


def cycle_cotangents(edges):
    prefixes, running = [], IDENTITY.copy()
    for edge in edges:
        prefixes.append(running)
        running = running@edge
    suffixes, tail = [None]*len(edges), IDENTITY.copy()
    for index in reversed(range(len(edges))):
        suffixes[index] = tail
        tail = edges[index]@tail
    cotangent = np.zeros((2*len(edges), 3))
    for edge, (prefix, value, suffix) in enumerate(zip(prefixes, edges, suffixes)):
        cotangent[2*edge] = [np.trace(prefix@t@value@suffix).real/2 for t in GENERATORS]
        cotangent[2*edge+1] = [-np.trace(prefix@value@t@suffix).real/2 for t in GENERATORS]
    return cotangent, np.trace(running).real/2


def subdivision_checks(coefficients, scalar, mean_q_gradient, kinetic, total_age):
    frames, rotations = finite_gauge_frames()
    holonomy = .6*IDENTITY+2*np.einsum("a,aij->ij", [.48, .64, 0.], GENERATORS)
    psi, derivative, _ = character_values(coefficients, np.array([.6]))
    score_multiplier = float(2*derivative[0]/psi[0])
    unit_direction = np.array([.36, .48, .8])
    close(unit_direction@unit_direction, 1)
    orbit = np.einsum("rij,j->ri", rotations, unit_direction)
    orbit_mean, orbit_second = orbit.mean(axis=0), orbit.T@orbit/24
    close(orbit_second, np.eye(3)/3)
    calibration = kinetic/(2*total_age)
    previous = 0.
    print(f"Fixed physical K={kinetic:g}, total heat age L={total_age:g}, declared E_star={calibration:g}")
    for count in (4, 8, 16):
        age = total_age/count
        edges = [holonomy]+[IDENTITY.copy() for _ in range(count-1)]
        p_q, q = cycle_cotangents(edges)
        close(q, .6)
        p_score = score_multiplier*p_q
        anchors = np.array([anchor for edge in range(count) for anchor in (edge, (edge+1) % count)])
        signs = np.tile([1., -1.], count)
        # Independently rotate each vertex. Same-anchor second moments
        # survive; distinct-anchor first moments multiply to zero.
        # Integrating the actual vacuum's radial score norm supplies 3s.
        fisher = np.zeros((6*count, 6*count))
        for i, anchor_i in enumerate(anchors):
            for j, anchor_j in enumerate(anchors):
                moment = orbit_second if anchor_i == anchor_j else np.outer(orbit_mean, orbit_mean)
                fisher[3*i:3*i+3, 3*j:3*j+3] = 3*scalar*signs[i]*signs[j]*moment
        for offset in (0, 7, 13):
            gauges = [frames[(5*vertex+offset) % len(frames)] for vertex in range(count)]
            gauged = [gauges[e]@edge@gauges[(e+1) % count].conj().T for e, edge in enumerate(edges)]
            gauged_p, gauged_q = cycle_cotangents(gauged)
            close(gauged_q, q)
            for slot, anchor in enumerate(anchors):
                frame = rotations[(5*anchor+offset) % len(frames)]
                close(score_multiplier*gauged_p[slot], frame@p_score[slot])
        # Each vertex has two slots with opposite covectors, the actual
        # Gauss identity rather than a hand-selected matrix eigenvector.
        for vertex in range(count):
            close(p_q[anchors == vertex].sum(axis=0), np.zeros(3))
        d0 = age*np.eye(6*count)  # theta=1/2 in every U,V slot.
        stiffness = np.linalg.inv(d0)+fisher
        inverse = np.linalg.solve(stiffness, np.eye(6*count))
        assert np.linalg.eigvalsh(stiffness).min() > 0
        actual = float(p_q.ravel()@inverse@p_q.ravel())
        radial_gradient = (1-q*q)/4
        coefficient = actual/radial_gradient
        expected = 2*total_age/(1+2*scalar*total_age/count)
        close(coefficient, expected)
        assert previous < coefficient < 2*total_age
        previous = coefficient
        # Fixed physical form and same vacuum norm throughout subdivision.
        physical_energy = kinetic*mean_q_gradient
        calibrated = calibration*coefficient*mean_q_gradient
        assert calibrated < physical_energy
        print(f"  N={count:2d}, full Fisher size={6*count}: response coefficient={coefficient:.12g}, "
              f"calibrated q energy={calibrated:.12g}, physical q energy={physical_energy:.12g}, "
              f"ratio={calibrated/physical_energy:.12g}")
    print("PASS full 24/48/96-dimensional Fisher inversions and actual cycle Pauli "
          "cotangents; independent vertex rotations verify the score covariance factors. "
          "The coefficient follows 2L/(1+2sL/N), not a fixed response under subdivision.")


def main():
    kinetic, coupling, total_age = 1., .7, 1.
    print("prepared vacuum subdivision receipt: one supplied finite physical Hamiltonian")
    coefficients, energy, scalar, gradient = vacuum_checks(kinetic, coupling)
    print(f"Converged finite-model E0={energy:.12g}, vacuum Fisher scalar s={scalar:.12g}")
    subdivision_checks(coefficients, scalar, gradient, kinetic, total_age)
    print("No physical vacuum construction in four dimensions, Poincare lower bound, "
          "Yang--Mills mass gap, or regulator-independent interacting source derived.")


if __name__ == "__main__":
    main()
