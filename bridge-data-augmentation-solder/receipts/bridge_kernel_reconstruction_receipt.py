"""Finite inverse-bridge reconstruction, with separate positivity firewalls.

All computations use complete finite midpoint and endpoint carriers. The
Wilson examples import the existing interacting gauge-quotient construction;
they do not construct a new model, a continuum limit, or a physical yardstick.
"""

import importlib.util
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np


def close(a, b, tol=3e-10):
    difference = float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
    assert difference < tol, difference


def perron(a):
    """Positive-entry matrix: Perron value and Euclidean-unit right vector."""
    assert np.min(a) > 0
    values, vectors = np.linalg.eig(a)
    index = int(np.argmax(values.real))
    assert abs(values[index].imag) < 1e-11
    assert np.max(np.abs(vectors[:, index].imag)) < 1e-11
    value = float(values[index].real)
    vector = vectors[:, index].real
    if vector.sum() < 0:
        vector = -vector
    assert vector.min() > 0
    vector /= np.linalg.norm(vector)
    close(a@vector, value*vector, 2e-9)
    assert np.max(np.abs(values)) <= value+1e-10
    return value, vector


def doob(a):
    value, vector = perron(a)
    p = a*vector[None, :]/(value*vector[:, None])
    close(p.sum(axis=1), 1.0)
    return p


def stationary(p):
    """Solve normalization and stationarity, not a supplied vacuum formula."""
    a = p.T-np.eye(len(p))
    a[-1] = 1
    rhs = np.zeros(len(p))
    rhs[-1] = 1
    w = np.linalg.solve(a, rhs)
    close(w@p, w)
    close(w.sum(), 1.0)
    assert w.min() > 0
    return w


def bridges(a):
    """b[x,z,y] is the middle y conditioned on the endpoint pair (x,z)."""
    assert np.min(a) > 0
    weight = np.einsum("xy,yz->xzy", a, a)
    b = weight/(a@a)[:, :, None]
    close(b.sum(axis=2), 1.0)
    return b


def anchored_kernel(b, anchor=0):
    assert np.min(b) > 0
    # This inverse consumes b alone; no original K, state or PF data enter.
    c = b[:, anchor, :]/b[:, anchor, anchor][:, None]
    close(c[:, anchor], 1.0)
    return c


def reversible_diagonal_inverse(d):
    close(d.sum(axis=1), 1.0)
    assert d.min() > 0
    w = stationary(d)
    edge = w[:, None]*d
    close(edge, edge.T)
    b = np.sqrt(edge)
    close(b, b.T)
    value, vacuum = perron(b)
    return b/value, vacuum**2, w


def full_from_diagonal(d):
    weight = np.sqrt(d[:, None, :]*d[None, :, :])
    return weight/weight.sum(axis=2, keepdims=True)


def positive_logarithmic_clock(transfer, vacuum):
    """H=-log(T/rho) requires Hilbert-positive T, not just positive entries."""
    close(transfer, transfer.T)
    eigenvalues, basis = np.linalg.eigh(transfer)
    assert eigenvalues.min() > 0
    normalized = transfer/eigenvalues[-1]
    hamiltonian = (basis*(-np.log(eigenvalues/eigenvalues[-1]))[None, :])@basis.T
    close(hamiltonian@vacuum, 0.0)
    energies, vectors = np.linalg.eigh(hamiltonian)
    assert energies.min() > -1e-11
    exponential = (vectors*np.exp(-energies)[None, :])@vectors.T
    close(exponential, normalized)
    return hamiltonian


def generic_inverse_checks():
    matrix_count, anchor_count = 0, 0
    nonreversible_count = 0
    for size in range(2, 9):
        for seed in (13, 82, 701):
            rng = np.random.default_rng(seed+size)
            a = rng.uniform(0.05, 2.0, size=(size, size))
            p = doob(a)
            pi = stationary(p)
            data = bridges(a)
            close(bridges(p), data)
            for anchor in range(size):
                c = anchored_kernel(data, anchor)
                close(bridges(c), data)
                close(doob(c), p)
                close(stationary(doob(c)), pi)
                # Independently identify the representative's gauge, after
                # recovering it from the conditional data alone.
                h = a[:, anchor]
                close(c, a*h[None, :]/(a[anchor, anchor]*h[:, None]))
                anchor_count += 1
            diagonal = np.exp(rng.uniform(-2.0, 2.0, size))
            equivalent = 3.1*a*diagonal[None, :]/diagonal[:, None]
            close(bridges(equivalent), data)
            close(doob(equivalent), p)
            if np.linalg.norm(pi[:, None]*p-pi[None, :]*p.T) > 1e-6:
                nonreversible_count += 1
            matrix_count += 1
    assert nonreversible_count > 0
    print(f"PASS {matrix_count} full-support kernel inversions, {anchor_count} anchors: "
          "same Doob clock and stationary law; positive diagonal/scalar gauges cancel")
    print(f"PASS {nonreversible_count} nonreversible examples retained by the general inverse")


def symmetric_inverse_checks():
    count, largest_state_difference = 0, 0.0
    for size in range(2, 9):
        for seed in (28, 517, 991):
            rng = np.random.default_rng(seed+size)
            factor = rng.uniform(0.05, 1.0, (size, size))
            a = factor@factor.T+np.diag(rng.uniform(0.1, 2.0, size))
            data = bridges(a)
            d = data[np.arange(size), np.arange(size)]
            recovered, nu, w = reversible_diagonal_inverse(d)
            value, vacuum = perron(a)
            close(recovered, a/value)
            close(nu, vacuum**2)
            close(full_from_diagonal(d), data)
            close(bridges(recovered), data)
            close(doob(recovered), doob(a))
            assert np.linalg.eigvalsh(recovered).min() > 0
            recovered_h = positive_logarithmic_clock(recovered, np.sqrt(nu))
            expected_h = positive_logarithmic_clock(a, vacuum)
            close(recovered_h, expected_h)
            # The reversible diagonal bridge's invariant law is not the
            # physical vacuum; compare each against its independent formula.
            row_square = np.sum(a*a, axis=1)
            close(w, row_square/row_square.sum())
            largest_state_difference = max(largest_state_difference, np.max(np.abs(w-nu)))
            count += 1
    assert largest_state_difference > 1e-3
    print(f"PASS {count} symmetric inversions: normalized transfer, full bridge compatibility "
          "and vacuum recovered from diagonal conditionals")
    print(f"PASS {count} positive logarithmic clocks: H=-log(T/rho), H*psi=0, exp(-H)=T/rho")
    print(f"PASS diagonal-bridge law differs from vacuum: largest coordinate difference="
          f"{largest_state_difference:.9f}")


def wilson_inverse_checks():
    root = Path(__file__).resolve().parents[2]
    source = root/"strong-coupling-gap-and-continuum-crossover"/"receipts"/"wilson_slab_fisher_receipt.py"
    spec = importlib.util.spec_from_file_location("existing_wilson_slab_receipt", source)
    module = importlib.util.module_from_spec(spec)
    previous_bytecode_setting = sys.dont_write_bytecode
    try:
        sys.dont_write_bytecode = True
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = previous_bytecode_setting
    count, depth_count = 0, 0
    maximum_log_error, minimum_clock_eigenvalue = 0.0, 1.0
    auxiliary_difference = None
    for extents in ((2, 1), (1, 1, 1)):
        _, cycles, fourier, lengths, bare_potential, _ = module.rectangular_cycle_carrier(extents)
        kinetic = (fourier*(0.73**lengths)[None, :])@fourier.T
        for beta in (0.2, 0.8):
            dressing = np.exp(-beta*bare_potential/2)
            transfer = dressing[:, None]*kinetic*dressing[None, :]
            assert np.linalg.norm(kinetic@np.diag(bare_potential)
                                  -np.diag(bare_potential)@kinetic) > 1e-3
            recovered_depths = {}
            for depth in (1, 3):
                normalized, psi, _ = module.perron_block(transfer, depth)
                # Only these conditional probabilities are supplied to the
                # inverses; the independently prepared Wilson state is withheld.
                data = bridges(normalized)
                reconstructed_p = doob(anchored_kernel(data))
                size = len(cycles)
                diagonal = data[np.arange(size), np.arange(size)]
                reconstructed_t, reconstructed_nu, _ = reversible_diagonal_inverse(diagonal)
                expected_p = normalized*psi[None, :]/psi[:, None]
                close(reconstructed_p, expected_p)
                close(reconstructed_t, normalized)
                close(reconstructed_nu, psi**2)
                close(stationary(reconstructed_p), psi**2)
                close(full_from_diagonal(diagonal), data)
                recovered_h = positive_logarithmic_clock(reconstructed_t, np.sqrt(reconstructed_nu))
                recovered_depths[depth] = (reconstructed_p, reconstructed_t, recovered_h)
                if extents == (2, 1) and beta == 0.8 and depth == 1:
                    # The posterior acts between DIFFERENT weighted carriers.
                    # Using product nu*nu instead of the true stationary
                    # endpoint law would compute a different adjoint/Gramian.
                    endpoint = reconstructed_nu[:, None]*(reconstructed_p@reconstructed_p)
                    flat_endpoint = endpoint.reshape(-1)
                    posterior = data.reshape(size*size, size)
                    close(flat_endpoint@posterior, reconstructed_nu)
                    psi_recovered = np.sqrt(reconstructed_nu)
                    analysis = np.sqrt(flat_endpoint)[:, None]*posterior/psi_recovered[None, :]
                    close(analysis@psi_recovered, np.sqrt(flat_endpoint))
                    close(analysis.T@np.sqrt(flat_endpoint), psi_recovered)
                    auxiliary_symmetric = analysis.T@analysis
                    auxiliary = auxiliary_symmetric*psi_recovered[None, :]/psi_recovered[:, None]
                    close(auxiliary.sum(axis=1), 1.0)
                    close(reconstructed_nu@auxiliary, reconstructed_nu)
                    assert np.linalg.eigvalsh(auxiliary_symmetric).min() > -1e-12
                    assert np.linalg.eigvalsh(auxiliary_symmetric).max() < 1+1e-12
                    auxiliary_difference = float(np.linalg.norm(auxiliary_symmetric-reconstructed_t, 2))
                    assert auxiliary_difference > 1e-3
                    assert np.linalg.norm(auxiliary-reconstructed_p, 2) > 1e-3
                count += 1
            p1, t1, h1 = recovered_depths[1]
            p3, t3, h3 = recovered_depths[3]
            close(p3, np.linalg.matrix_power(p1, 3))
            power_t = np.linalg.matrix_power(t1, 3)
            close(t3, power_t)
            # The beta=0.8 cube has lambda_min(T_3) about 1e-13. Retain
            # it, but expose the logarithm's conditioning instead of claiming
            # an absolute machine-precision H_3=3H_1 comparison. For SPD A,B,
            # ||log A-log B|| <= ||A-B||/min(lambda_min(A),lambda_min(B)).
            floor = min(np.linalg.eigvalsh(t3).min(), np.linalg.eigvalsh(power_t).min())
            matrix_error = float(np.linalg.norm(t3-power_t, 2))
            roundoff_allowance = 32*np.finfo(float).eps*len(t1)
            log_bound = (matrix_error+roundoff_allowance)/floor
            log_error = float(np.linalg.norm(h3-3*h1, 2))
            assert log_error <= log_bound+1e-9
            # Even the ill-conditioned case must discriminate a one-step
            # generator from the correctly tripled generator.
            log_tolerance = 2e-5 if floor < 1e-8 else 3e-9
            assert log_error < log_tolerance
            assert np.linalg.norm(h3-h1, 2) > 1
            maximum_log_error = max(maximum_log_error, log_error)
            minimum_clock_eigenvalue = min(minimum_clock_eigenvalue, floor)
            depth_count += 1
    print(f"PASS {count} existing interacting Wilson rectangle/cube inversions: "
          "complete 4/32-state carriers, state and normalized clock reconstructed from bridge data")
    print(f"PASS {depth_count} blocked-clock checks: P_3=P_1^3, H_3=3 H_1; "
          f"max log residual={maximum_log_error:.3e}, min clock eigenvalue={minimum_clock_eigenvalue:.3e}")
    assert auxiliary_difference is not None
    print(f"PASS Wilson clock differs from actual bridge K^*K: "
          f"weighted operator difference={auxiliary_difference:.9f}")


def incompatible_full_data():
    a = np.array([[4.0, 1.0, 2.0], [1.0, 3.0, 1.5], [2.0, 1.5, 5.0]])
    data = bridges(a)
    altered = data.copy()
    changed = data[0, 1]*np.array([1.2, 1.0, 0.8])
    changed /= changed.sum()
    altered[0, 1] = altered[1, 0] = changed
    close(altered.sum(axis=2), 1.0)
    assert altered.min() > 0
    close(altered, altered.transpose(1, 0, 2))
    index = np.arange(len(a))
    close(altered[index, index], data[index, index])
    # Endpoint symmetry, valid diagonal data and positive normalized rows
    # do not imply compatibility of the full conditional specification.
    assert np.max(np.abs(full_from_diagonal(altered[index, index])-altered)) > 0.01
    for anchor in range(len(a)):
        proposed = anchored_kernel(altered, anchor)
        assert np.max(np.abs(bridges(proposed)-altered)) > 0.01
    print("PASS incompatible full specification rejected: positive normalized "
          "endpoint-symmetric rows and unchanged reversible diagonals are insufficient")


def sparse_cycle_counterexample():
    f = Fraction
    r, p, q = f(1, 2), f(1, 3), f(1, 6)

    def transition(forward, backward):
        a = [[f(0) for _ in range(5)] for _ in range(5)]
        for x in range(5):
            a[x][x] = r
            a[x][(x+1) % 5] = forward
            a[x][(x-1) % 5] = backward
            assert sum(a[x]) == 1
        return a

    def exact_bridge(a):
        data = []
        for x in range(5):
            for z in range(5):
                weights = [a[x][y]*a[y][z] for y in range(5)]
                total = sum(weights)
                assert total > 0
                row = tuple(w/total for w in weights)
                assert sum(row) == 1
                data.extend(row)
        return tuple(data)

    forward, reverse = transition(p, q), transition(q, p)
    data = exact_bridge(forward)
    assert data == exact_bridge(reverse)
    assert forward != reverse
    assert any(value == 0 for row in forward for value in row)
    assert any(value == 0 for value in data)
    # Both chains are already Markov/Perron normalized with uniform stationary law.
    assert all(sum(row[col] for row in forward) == 1 for col in range(5))
    difference = max(abs(forward[x][z]-reverse[x][z]) for x in range(5) for z in range(5))
    assert difference == f(1, 6)
    print(f"PASS exact sparse C5 obstruction: all {len(data)} two-step bridge probabilities "
          f"agree, clocks differ by {difference}; full support is essential")


def positivity_firewalls():
    raw = np.array([[10.0, 8.0, 8.0], [8.0, 10.0, 1.0], [8.0, 1.0, 10.0]])
    d = raw**2/np.sum(raw**2, axis=1, keepdims=True)
    recovered, nu, w = reversible_diagonal_inverse(d)
    close(bridges(recovered)[np.arange(3), np.arange(3)], d)
    weighted_d = np.sqrt(w)[:, None]*d/np.sqrt(w)[None, :]
    close(weighted_d, weighted_d.T)
    dmin = float(np.linalg.eigvalsh(weighted_d).min())
    tmin = float(np.linalg.eigvalsh(recovered).min())
    assert dmin > 0 and tmin < 0
    assert recovered.min() > 0 and nu.min() > 0
    print(f"PASS positivity firewall: diagonal D is Hilbert-positive (min={dmin:.9f}) "
          f"but its reconstructed entry-positive clock is indefinite (min={tmin:.9f})")

    p = np.array([[43.0, 1.0, 16.0], [1.0, 43.0, 16.0], [16.0, 16.0, 28.0]])/60
    close(p.sum(axis=1), 1.0)
    values, vectors = np.linalg.eigh(p)
    close(values, [0.2, 0.7, 1.0])
    assert p.min() > 0 and values.min() > 0
    logp = (vectors*np.log(values)[None, :])@vectors.T
    exact_entry = np.log(0.2)/6-np.log(0.7)/2
    close(logp[0, 1], exact_entry)
    assert logp[0, 1] < 0
    fractional_clock = (vectors*(values**0.1)[None, :])@vectors.T
    close(fractional_clock.sum(axis=1), 1.0)
    assert fractional_clock[0, 1] < 0
    # A nonnegative self-adjoint Hamiltonian logarithm exists, but it does
    # not generate a positivity-preserving continuous interpolation P^t.
    assert np.linalg.eigvalsh(-logp).min() > -1e-12
    print(f"PASS interpolation firewall: spectrum(P)=(1,0.7,0.2), "
          f"log(P)[0,1]={logp[0, 1]:.9f}, P^0.1[0,1]={fractional_clock[0, 1]:.9f}")


if __name__ == "__main__":
    generic_inverse_checks()
    symmetric_inverse_checks()
    wilson_inverse_checks()
    incompatible_full_data()
    sparse_cycle_counterexample()
    positivity_firewalls()
    print("Finite deterministic inverse checks and exact sparse counterexample only; "
          "no full-group inverse, continuum carrier, generated scale or Yang-Mills return is certified.")
