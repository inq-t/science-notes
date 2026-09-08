"""Two interacting SU(2) heat loops: local scores, globally inverted response.

This is an actual finite retained-source calculation for the specified tilt
exp(lambda*q(Y1 Y2^-1)), q=Tr/2. It integrates the positive joint endpoint
law and the shifted Pauli words before constructing the Fisher matrix.
The path likelihood and endpoint-control reduction are analytic inputs
from loop-correlations-and-the-source-response.md, not numerical claims.
The final banded-matrix check is a separate generic linear-algebra control.
No physical gap, continuum construction, or infinite Gibbs simulation is
computed. Convention: g=q0 I-i vec(q).sigma, T_a=-i sigma_a/2, Q=-2Tr.
"""

from __future__ import annotations

import itertools
import math

import numpy as np


PAULI = np.array(([[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]))
GENERATORS = -.5j*PAULI
IDENTITY = np.eye(2, dtype=complex)


def close(actual, expected, *, rtol=2e-11, atol=3e-13):
    assert np.all(np.isfinite(actual)) and np.all(np.isfinite(expected))
    assert np.allclose(actual, expected, rtol=rtol, atol=atol), (actual, expected)


def turn(vector):
    length = np.linalg.norm(vector)
    if length == 0:
        return IDENTITY.copy()
    return (math.cos(length/2)*IDENTITY
            + 2*math.sin(length/2)/length*np.einsum("a,aij->ij", vector, GENERATORS))


def central_heat_quadrature(time, order):
    angles = np.arange(1, order+1)*math.pi/(order+1)
    nodes, haar = np.cos(angles), 2*np.sin(angles)**2/(order+1)
    previous, current = np.ones(order), 2*nodes
    density = previous+2*math.exp(-.75*time)*current
    cutoff = 32
    for ell in range(2, cutoff+1):
        following = 2*nodes*current-previous
        density += (ell+1)*math.exp(-ell*(ell+2)*time/4)*following
        previous, current = current, following
    ell = cutoff+1
    term = (ell+1)**2*math.exp(-ell*(ell+2)*time/4)
    ratio = ((ell+2)/(ell+1))**2*math.exp(-(2*ell+3)*time/4)
    tail = term/(1-ratio)  # |U_ell(q)|<=ell+1, decreasing term ratio.
    assert tail < 1e-70 and np.min(density) > 0
    weights = haar*density
    close(weights.sum(), 1)
    close(weights@nodes, math.exp(-.75*time))
    close(weights@(nodes*nodes), (1+3*math.exp(-2*time))/4)
    return nodes, weights, tail


def proper_cube_rotations():
    rotations = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = np.eye(3)[list(permutation)]*np.array(signs)[:, None]
            if np.linalg.det(matrix) > 0:
                rotations.append(matrix)
    rotations = np.array(rotations)
    assert len(rotations) == 24
    close(rotations.mean(axis=0), np.zeros((3, 3)))
    close(np.einsum("rij,rkl->ijkl", rotations, rotations)/24,
          np.einsum("ik,jl->ijkl", np.eye(3), np.eye(3))/3)
    return rotations


def coupled_quadrature(order, angle_order, couplings):
    q1, w1, tail1 = central_heat_quadrature(.7, order)
    q2, w2, tail2 = central_heat_quadrature(1.1, order)
    z, wz = np.polynomial.legendre.leggauss(angle_order)
    first, second, dot = [x.ravel() for x in np.meshgrid(q1, q2, z, indexing="ij")]
    base = (w1[:, None, None]*w2[None, :, None]*wz[None, None, :]/2).ravel()
    radius1, radius2 = np.sqrt(1-first*first), np.sqrt(1-second*second)
    vector_dot = radius1*radius2*dot
    word = first*second+vector_dot
    weights = np.exp(np.asarray(couplings)[:, None]*word)*base
    partitions = weights.sum(axis=1)
    weights /= partitions[:, None]
    moments = np.column_stack((partitions, weights@(first*second), weights@vector_dot,
                               weights@word, weights@(first*first)))
    # Fix the relative angle, then integrate its common spatial frame.
    # Every shifted matrix word is bilinear in Y1,Y2; these 24 proper
    # rotations integrate the required common-frame degree-two moments.
    v1 = np.column_stack((np.zeros_like(first), np.zeros_like(first), radius1))
    v2 = radius2[:, None]*np.column_stack((np.sqrt(1-dot*dot), np.zeros_like(dot), dot))
    tensor = np.zeros((len(couplings), 2, 2, 2, 2), dtype=complex)
    for rotation in proper_cube_rotations():
        a, b = v1@rotation.T, v2@rotation.T
        group1 = first[:, None, None]*IDENTITY+2*np.einsum("na,aij->nij", a, GENERATORS)
        inverse2 = second[:, None, None]*IDENTITY-2*np.einsum("na,aij->nij", b, GENERATORS)
        for index, probability in enumerate(weights):
            tensor[index] += np.einsum("n,nij,nkl->ijkl", probability, group1, inverse2,
                                      optimize=True)/24
    close(tensor[0], math.exp(-.75*1.8)*np.einsum("ij,kl->ijkl", IDENTITY, IDENTITY))
    close(moments[0, 0], 1)
    return moments, tensor, max(tail1, tail2)


def interacting_response_checks():
    couplings = (0., .4, 1.)
    runs = [coupled_quadrature(order, angular, couplings)
            for order, angular in ((24, 16), (32, 24), (48, 32))]
    for moments, tensors, _ in runs[:-1]:
        close(moments, runs[-1][0])
        close(tensors, runs[-1][1])
    moments, tensors, tail = runs[-1]
    word_nodes, word_weights, _ = central_heat_quadrature(1.8, 64)
    for index, coupling in enumerate(couplings):
        weighted = word_weights*np.exp(coupling*word_nodes)
        close(weighted.sum(), moments[index, 0])
        close(weighted@word_nodes/weighted.sum(), moments[index, 3])
    print("PASS positive coupled heat quadratures (24,16)/(32,24)/(48,32), "
          "24 proper rotation moments, exact unweighted heat moments and independent "
          f"relative-word convolution; heat-series tail < {tail:.3g}")

    # An actual local class observable, not an arbitrary cotangent:
    # f=q(Y1) at Y1=.6 I-i(.48 sigma1+.64 sigma2).
    group = .6*IDENTITY+2*np.einsum("a,aij->ij", [.48, .64, 0.], GENERATORS)
    close(group.conj().T@group, IDENTITY)
    w = np.array([np.trace(t@group).real/2 for t in GENERATORS])
    local_covector = np.r_[w, -w]
    step = 1e-5
    for slot in range(2):
        for axis in range(3):
            t = turn(step*np.eye(3)[axis])
            plus, minus = (t@group, t.conj().T@group) if slot == 0 else (group@t.conj().T, group@t)
            actual = np.trace(plus-minus).real/(4*step)
            close(actual, local_covector[3*slot+axis], rtol=2e-9, atol=3e-11)
    d0 = np.diag(np.repeat([2*.7*.3, 2*.7*.7, 2*1.1*.6, 2*1.1*.4], 3))
    source_to_difference = np.zeros((6, 12))
    source_to_difference[:3, :3] = source_to_difference[3:, 3:6] = np.eye(3)
    source_to_difference[:3, 6:9] = source_to_difference[3:, 9:] = -np.eye(3)
    unit_local = np.array([1., 0., 0., -1., 0., 0.])

    for index, coupling in enumerate(couplings[1:], start=1):
        partition, alpha, beta, mean, q1_squared = moments[index]
        chi = alpha-beta/3
        tensor = tensors[index]

        def word_average(left, middle):
            return np.einsum("ij,kl,jkli->", left, middle, tensor).real/2

        # Hessian from the integrated actual Pauli word, before using
        # the candidate alpha/beta coefficient formula.
        actual_six = np.zeros((6, 6))
        for a, ta in enumerate(GENERATORS):
            for b, tb in enumerate(GENERATORS):
                symmetric = (ta@tb+tb@ta)/2
                actual_six[a, b] = -word_average(symmetric, IDENTITY)
                actual_six[3+a, 3+b] = -word_average(IDENTITY, symmetric)
                actual_six[a, 3+b] = actual_six[3+b, a] = word_average(ta, tb)
        candidate = np.kron(np.array([[mean, -chi], [-chi, mean]])/4, np.eye(3))
        close(actual_six, candidate)
        hessian = source_to_difference.T@actual_six@source_to_difference

        def shifted_potential(control):
            u1, v1, u2, v2 = [turn(row) for row in control.reshape(4, 3)]
            return mean-word_average(u2.conj().T@u1, v1.conj().T@v2)

        basis, epsilon = np.eye(12), .001
        finite_hessian = np.zeros((12, 12))
        for a in range(12):
            for b in range(12):
                finite_hessian[a, b] = sum(
                    sa*sb*shifted_potential(epsilon*(sa*basis[a]+sb*basis[b]))
                    for sa in (-1., 1.) for sb in (-1., 1.))/(4*epsilon*epsilon)
        close(finite_hessian, hessian, rtol=5e-7, atol=4e-10)

        stiffness = np.linalg.inv(d0)+coupling*hessian
        assert np.linalg.eigvalsh(stiffness).min() > 0
        full_inverse = np.linalg.inv(stiffness)
        a, b, c = stiffness[:6, :6], stiffness[:6, 6:], stiffness[6:, 6:]
        shorted = a-b@np.linalg.solve(c, b.T)
        global_local, premature = full_inverse[:6, :6], np.linalg.inv(a)
        close(global_local, np.linalg.inv(shorted))
        difference = global_local-premature
        assert np.linalg.eigvalsh(difference).min() > -3e-14
        local_global = float(local_covector@global_local@local_covector)
        local_naive = float(local_covector@premature@local_covector)
        assert local_global-local_naive > 1e-5
        # The common source frame rotates every covector simultaneously;
        # isotropic 3x3 blocks make this contraction frame independent.
        mean_grad = (1-q1_squared)/4
        global_energy = float(unit_local@global_local@unit_local)*mean_grad
        naive_energy = float(unit_local@premature@unit_local)*mean_grad
        print(f"lambda={coupling:g}: Z_exp(lambda*q)={partition:.12g}, "
              f"alpha={alpha:.12g}, beta={beta:.12g}, m={mean:.12g}, chi={chi:.12g}")
        print(f"  local q cotangent: global inverse={local_global:.12g}, "
              f"premature local inverse={local_naive:.12g}, difference={local_global-local_naive:.12g}; "
              f"integrated q energies={global_energy:.12g} versus {naive_energy:.12g}")
    print("PASS actual coupled-state Pauli Hessians and all 12 shifted-source controls; "
          "global inversion followed by restriction differs strictly on a local observable "
          "from restriction followed by inversion. Finite retained-source evidence only.")


def generic_banded_controls():
    """Independent generic matrix check, not another interacting source model."""
    diagonal, coupling, size = 2., .3, 17
    adjacency = np.eye(size, k=1)+np.eye(size, k=-1)
    stiffness = diagonal*np.eye(size)-coupling*adjacency
    scaled = coupling*adjacency/diagonal
    norm_bound = 2*coupling/diagonal
    inverse = np.linalg.inv(stiffness)
    partial, power = np.zeros_like(stiffness), np.eye(size)
    for degree in range(13):
        partial += power/diagonal
        bound = norm_bound**(degree+1)/(diagonal*(1-norm_bound))
        assert np.linalg.norm(inverse-partial, 2) <= bound+3e-15
        if degree < 8:
            assert partial[0, 8] == 0
        power = power@scaled
    values = []
    for radius in (1, 2, 4, 8):
        section = stiffness[8-radius:9+radius, 8-radius:9+radius]
        values.append(np.linalg.inv(section)[radius, radius])
    assert all(a < b for a, b in zip(values[:-1], values[1:]))
    close(values[-1], inverse[8, 8])
    infinite_toeplitz_value = 1/math.sqrt(diagonal*diagonal-4*coupling*coupling)
    assert abs(values[-1]-infinite_toeplitz_value) < 1e-12
    print("PASS separate GENERIC banded-matrix control: 13 Neumann error bounds, "
          "finite propagation of polynomial terms and four finite sections. "
          "This is not an infinite-volume Gibbs calculation or a physical gap bound.")


def main():
    print("local interaction assembly receipt: actual coupled finite source")
    interacting_response_checks()
    generic_banded_controls()
    print("No continuum construction, infinite interacting limit, physical clock identification, "
          "or Yang--Mills mass gap certified.")


if __name__ == "__main__":
    main()
