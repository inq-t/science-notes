"""Finite calibrations of joint Wilson escape, localization, and moving fibers.

Stdout only. These checks do not establish a continuum or physical mass gap.
"""

from itertools import product
import numpy as np


def su3_basis():
    hermitian = []
    for i in range(3):
        for j in range(i + 1, 3):
            symmetric = np.zeros((3, 3), dtype=complex)
            symmetric[i, j] = symmetric[j, i] = 1
            antisymmetric = np.zeros((3, 3), dtype=complex)
            antisymmetric[i, j], antisymmetric[j, i] = -1j, 1j
            hermitian.extend((symmetric, antisymmetric))
    hermitian.extend((np.diag((1, -1, 0)),
                      np.diag((1, 1, -2)) / np.sqrt(3)))
    basis = np.array(hermitian) * (1j * np.sqrt(1.5))
    gram = np.array(tuple(tuple(-np.trace(a @ b).real / 3
                               for b in basis) for a in basis))
    assert np.allclose(gram, np.eye(8))
    assert np.allclose(sum(a @ a for a in basis), -8 * np.eye(3))
    return basis


def exp_anti(x):
    values, vectors = np.linalg.eigh(-1j * x)
    return (vectors * np.exp(1j * values)) @ vectors.conj().T


def haar_su3(rng):
    a = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
    q, r = np.linalg.qr(a)
    q = q * (np.diag(r) / np.abs(np.diag(r)))
    q[:, 0] /= np.linalg.det(q)
    return q


def lattice():
    size = 5

    def shift(x, direction, step=1):
        y = list(x)
        y[direction] = (y[direction] + step) % size
        return tuple(y)

    plaquettes = []
    for x in product(range(size), repeat=4):
        for i in range(4):
            for j in range(i + 1, 4):
                plaquettes.append(((x + (i,), 1),
                                   (shift(x, i) + (j,), 1),
                                   (shift(x, j) + (i,), -1),
                                   (x + (j,), -1)))
    origin = (2, 2, 2, 2)
    active = origin + (0,)
    outer = tuple(shift(origin, j, step) + (0,)
                  for j in (1, 2, 3) for step in (1, -1))
    powers = {active: 1}
    powers.update({edge: (1 if index % 2 == 0 else -1)
                   for index, edge in enumerate(outer)})
    touching = tuple(p for p in plaquettes
                     if any(edge in outer for edge, _ in p))
    external = tuple(p for p in touching
                     if not any(edge == active for edge, _ in p))
    assert len(plaquettes) == 3750
    assert len(touching) == 36 and len(external) == 30
    assert all(sum(edge in outer for edge, _ in p) == 1 for p in touching)
    assert all(sum(any(edge == j for edge, _ in p) for p in touching) == 6
               for j in outer)
    overlap = {}
    for x in product(range(size), repeat=4):
        for direction in range(4):
            for transverse in range(4):
                if transverse == direction:
                    continue
                for step in (1, -1):
                    edge = shift(x, transverse, step) + (direction,)
                    overlap[edge] = overlap.get(edge, 0) + 1
    assert len(overlap) == 2500 and set(overlap.values()) == {6}
    z = np.exp(2j * np.pi / 3)
    local_edges = {edge for p in touching for edge, _ in p}
    base = {edge: z**powers.get(edge, 0) * np.eye(3) for edge in local_edges}
    return active, outer, powers, touching, external, base


def phi(plaquette, field):
    value = np.eye(3, dtype=complex)
    for edge, orientation in plaquette:
        u = field[edge]
        value = value @ (u if orientation == 1 else u.conj().T)
    return np.trace(value).real / 3


def action(plaquettes, field, coupling=1.0):
    return coupling * sum(1 - phi(p, field) for p in plaquettes)


def wilson_checks():
    rng = np.random.default_rng(118)
    basis = su3_basis()
    active, outer, powers, touching, external, base = lattice()
    assert all(abs(phi(p, base) + 0.5) < 1e-12 for p in external)
    baseline = action(touching, base)
    finite_paths = 0
    rotation = 1j * np.diag((1, -1, 0))
    for edge in outer:
        coefficient = 1 if powers[edge] == 1 else 2
        for t in (0.05, 0.2, 0.7, 1.5, np.pi):
            moved = dict(base)
            moved[edge] = base[edge] @ exp_anti(t * rotation)
            difference = action(touching, moved) - baseline
            assert np.isclose(difference, coefficient * (np.cos(t) - 1),
                              atol=2e-12)
            finite_paths += 1

    hessian_tests = 0
    for _ in range(16):
        directions = {edge: np.einsum("a,aij->ij", rng.normal(size=8), basis)
                      for edge in (active,) + outer}
        expected = 0.0
        for p in touching:
            curvature = sum(sign * directions.get(edge, np.zeros((3, 3)))
                            for edge, sign in p)
            expected += phi(p, base) * (-np.trace(curvature @ curvature).real / 3)
        step = 1e-4
        plus, minus = dict(base), dict(base)
        for edge, direction in directions.items():
            plus[edge] = base[edge] @ exp_anti(step * direction)
            minus[edge] = base[edge] @ exp_anti(-step * direction)
        measured = (action(touching, plus) + action(touching, minus)
                    - 2 * baseline) / step**2
        assert abs(measured - expected) < 2e-4 * (1 + abs(expected))
        hessian_tests += 1
    # Negative coordinate restriction: no cross-plaquette term between outer links.
    diagonal = tuple(sum(phi(p, base) for p in touching
                         if any(edge == j for edge, _ in p)) for j in outer)
    assert np.allclose(diagonal, (-1.5, -3, -1.5, -3, -1.5, -3))

    laplace_tests = 0
    maximum_relative_error = 0.0
    for coupling in (0.1, 1.0, 5.0):
        for _ in range(2):
            field = {
                edge: u @ exp_anti(0.025 * np.einsum(
                    "a,aij->ij", rng.normal(size=8), basis))
                for edge, u in base.items()
            }
            field[active] = haar_su3(rng)
            assert all(phi(p, field) <= -0.4 for p in external)
            s0 = action(touching, field, coupling)
            expected = 8 * coupling * sum(phi(p, field) for p in touching)
            assert expected <= -48 * coupling
            step = 1e-4
            laplacian, generator_ratio = 0.0, 0.0
            for edge in outer:
                for direction in basis:
                    plus, minus = dict(field), dict(field)
                    plus[edge] = field[edge] @ exp_anti(step * direction)
                    minus[edge] = field[edge] @ exp_anti(-step * direction)
                    dp = action(touching, plus, coupling) - s0
                    dm = action(touching, minus, coupling) - s0
                    ds = (dp - dm) / (2 * step)
                    laplacian += (dp + dm) / step**2
                    wp, wm = np.expm1(dp), np.expm1(dm)
                    generator_ratio += ((wp + wm) / step**2
                                        - ds * (wp - wm) / (2 * step))
            error = max(abs(laplacian - expected),
                        abs(generator_ratio - expected)) / (1 + abs(expected))
            maximum_relative_error = max(maximum_relative_error, error)
            assert error < 2e-4
            laplace_tests += 1
    return finite_paths, hessian_tests, laplace_tests, maximum_relative_error


def lyapunov_checks():
    theta = 2 * np.pi * np.arange(4096) / 4096
    sine, cosine = np.sin(theta), np.cos(theta)
    cases = 0
    for coupling in (0.2, 1, 4, 16, 64):
        weights = np.exp(coupling * (cosine - 1))
        weights /= weights.sum()
        score_action = coupling * sine
        potential = -coupling * cosine  # -L exp(S)/exp(S) = -S''.
        localized = np.exp(0.5 * coupling * (1-cosine))
        trials = (
            (np.sin(2*theta), 2*np.cos(2*theta)),
            (1 + np.cos(3*theta), -3*np.sin(3*theta)),
            (localized * (1-cosine)**2,
             localized * (0.5*coupling*sine*(1-cosine)**2
                          + 2*(1-cosine)*sine)),
        )
        for f, df in trials:
            normalization = np.sqrt(weights @ f**2)
            f, df = f / normalization, df / normalization
            energy = weights @ df**2
            remainder = weights @ (df - f*score_action)**2
            left = weights @ (potential * f**2)
            assert abs(left - energy + remainder) < 2e-9 * (1 + energy)
            restricted = weights @ ((cosine <= -0.4) * f**2)
            assert restricted <= (energy + coupling) / (1.4*coupling) + 1e-12
            cases += 1
    return cases


def moving_fiber_checks():
    cases = 0
    for x in np.linspace(-3, 3, 31):
        p = (1 + np.tanh(x)) / 2
        dp = 2*p*(1-p)
        q = np.array((p, 1-p))
        score = np.array((dp/p, -dp/(1-p)))
        phi_x = np.array((np.sqrt((1-p)/p), -np.sqrt(p/(1-p))))
        derivative = -dp / (2*p*(1-p)) * np.array((phi_x[0], -phi_x[1]))
        c = np.tanh(x)
        kappa = 1 / np.cosh(x)
        assert np.isclose(q @ phi_x, 0)
        assert np.isclose(q @ phi_x**2, 1)
        assert np.allclose(derivative, -kappa + c*phi_x)
        assert np.isclose(q @ (phi_x * derivative), c)
        assert np.isclose(q @ (derivative - c*phi_x)**2, kappa**2)
        half_vacuum = np.sqrt(q)
        d_half_vacuum = 0.5 * score * half_vacuum
        assert np.allclose(d_half_vacuum - 0.5*score*half_vacuum, 0)
        assert np.isclose(np.sum(d_half_vacuum**2), kappa**2 / 4)

        a0, a1 = np.sin(2*x), np.cos(x)
        da0, da1 = 2*np.cos(2*x), -np.sin(x)
        direct = da0 + da1*phi_x + a1*derivative
        band_energy = (da0-kappa*a1)**2 + (da1+c*a1)**2
        assert np.isclose(q @ direct**2, band_energy)
        label_a1 = np.sqrt(p*(1-p))
        label_da1 = dp*(1-2*p)/(2*label_a1)
        assert np.isclose(dp - kappa*label_a1, 0)
        assert np.isclose(label_da1 + c*label_a1, 0)
        cases += 1
    return cases


def nested_context_checks():
    rng = np.random.default_rng(119)
    states = tuple(product(range(2), repeat=3))  # outside, active, outer
    cases = 0
    for _ in range(12):
        weights = rng.uniform(0.1, 1, size=8)
        weights /= weights.sum()

        def conditional_projection(coordinates):
            result = np.zeros((8, 8))
            for i, state in enumerate(states):
                matching = tuple(j for j, other in enumerate(states)
                                 if all(state[k] == other[k] for k in coordinates))
                mass = sum(weights[j] for j in matching)
                for j in matching:
                    result[i, j] = np.sqrt(weights[i]*weights[j]) / mass
            return result

        retained = conditional_projection((0, 2))
        outside = conditional_projection((0,))
        bad = np.diag(tuple(float(state[2] == 1) for state in states))
        q_active, q_block = np.eye(8)-retained, np.eye(8)-outside
        difference = q_block @ bad @ q_block - bad @ q_active
        assert np.allclose(difference,
                           (retained-outside) @ bad @ (retained-outside))
        assert np.linalg.eigvalsh(difference).min() > -1e-12
        cases += 1
    return cases


if __name__ == "__main__":
    paths, hessians, laplacians, error = wilson_checks()
    print("PASS full Wilson lattice incidence: 3750 plaquettes, 36 touching, 30 external")
    print("PASS exact finite context escapes:", paths)
    print("PASS signed full-action Hessians:", hessians)
    print("PASS nonlinear Laplacian and localizer checks:", laplacians,
          "max relative discrepancy:", error)
    print("PASS ground-state localization calibrations:", lyapunov_checks())
    print("PASS moving-fiber and binary cancellation checks:", moving_fiber_checks())
    print("PASS nested conditional projections and block-local remainder:",
          nested_context_checks())
    print("Scope: finite identities and local joint estimates; no full physical gap.")
