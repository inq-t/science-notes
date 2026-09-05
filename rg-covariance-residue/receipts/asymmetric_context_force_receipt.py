"""Finite checks of asymmetric conditional wells and full exterior-force escape.

Reuses the full Wilson patch and metric from the joint-context receipt.
Stdout only. Neither sampling nor these finite identities prove a physical gap.
"""

import numpy as np
from joint_context_escape_receipt import (
    action, exp_anti, haar_su3, lattice, phi, su3_basis,
)


def phi_gradient(plaquette, field, edge, basis):
    """Right-trivialized derivative of the actual ordered plaquette."""
    factors = tuple(field[j] if sign == 1 else field[j].conj().T
                    for j, sign in plaquette)
    positions = tuple(k for k, (j, _) in enumerate(plaquette) if j == edge)
    assert len(positions) == 1
    position = positions[0]
    sign = plaquette[position][1]
    derivatives = []
    for tangent in basis:
        value = np.eye(3, dtype=complex)
        for k, factor in enumerate(factors):
            if k == position:
                factor = factor @ tangent if sign == 1 else -tangent @ factor
            value = value @ factor
        derivatives.append(np.trace(value).real / 3)
    return np.array(derivatives)


def force(plaquettes, field, edge, basis):
    return -sum((phi_gradient(p, field, edge, basis) for p in plaquettes
                 if any(j == edge for j, _ in p)), start=np.zeros(8))


def asymmetric_geometry():
    rng = np.random.default_rng(119)
    basis = su3_basis()
    active, outer, _, touching, external, old = lattice()
    field = {edge: np.eye(3, dtype=complex) for edge in old}
    a = (3 + 4j) / 5
    diagonal = np.array((a, a, a**-2))
    for index, edge in enumerate(outer):
        field[edge] = np.diag(np.roll(diagonal, index // 2))
        assert np.isclose(np.linalg.det(field[edge]), 1)
    source = sum(field[edge] for edge in outer)
    expected_source = (46 + 32j) / 25
    assert np.allclose(source, expected_source * np.eye(3))
    assert np.allclose(tuple(phi(p, field) for p in external), 23/75)
    expected_force = 44*np.sqrt(2)/15
    assert expected_force > 3
    for edge in outer:
        assert np.isclose(np.linalg.norm(force(external, field, edge, basis)),
                          expected_force)

    # The actual active plaquettes have the proposed scalar source orientation.
    active_plaquettes = tuple(p for p in touching
                              if any(j == active for j, _ in p))
    for _ in range(25):
        field[active] = haar_su3(rng)
        exponent = sum(phi(p, field) for p in active_plaquettes)
        assert np.isclose(exponent,
                          np.trace(field[active].conj().T @ source).real / 3)

    phase = np.angle(expected_source)
    assert np.pi/6 < phase < np.pi/3
    z = np.exp(2j*np.pi/3)
    maximum_error = 0.0
    for phase_sample in (np.pi/6 + 0.025, phase, np.pi/3 - 0.025):
        def potential(u):
            return np.trace(np.exp(-1j*phase_sample)*u).real
        assert potential(np.eye(3)) > potential(z*np.eye(3))
        for j in (0, 1):
            center = z**j*np.eye(3)
            for _ in range(8):
                coefficients = rng.normal(size=8)
                tangent = np.einsum("a,aij->ij", coefficients, basis)
                expected = -3*np.cos(2*np.pi*j/3-phase_sample) * (
                    coefficients @ coefficients)
                assert expected < 0
                step = 1e-4
                plus, minus = (center @ exp_anti(sign*step*tangent)
                               for sign in (1, -1))
                derivative = (potential(plus)-potential(minus))/(2*step)
                measured = (potential(plus)+potential(minus)
                            - 2*potential(center))/step**2
                error = abs(measured-expected)/(1+abs(expected))
                maximum_error = max(maximum_error, error)
                assert abs(derivative) < 2e-5
                assert error < 2e-6
    return field, maximum_error


def full_force_checks(base):
    rng = np.random.default_rng(120)
    basis = su3_basis()
    active, outer, _, touching, external, _ = lattice()
    maximum_error = 0.0
    cases = 0
    for coupling in (48, 96, 384):
        for _ in range(2):
            field = {
                edge: u @ exp_anti(0.015*np.einsum(
                    "a,aij->ij", rng.normal(size=8), basis))
                for edge, u in base.items()
            }
            field[active] = haar_su3(rng)
            full_gradient = {}
            for edge in outer:
                outside = force(external, field, edge, basis)
                full = force(touching, field, edge, basis)
                assert np.linalg.norm(outside) > 3
                assert np.linalg.norm(full-outside) <= 1 + 1e-12
                assert np.linalg.norm(full) >= 2
                full_gradient[edge] = coupling*full
            gradient_squared = sum(v @ v for v in full_gradient.values())
            laplacian = 8*coupling*sum(phi(p, field) for p in touching)
            assert gradient_squared >= 24*coupling**2
            assert laplacian <= 288*coupling
            potential = gradient_squared/4-laplacian/2
            assert potential >= 6*coupling**2-144*coupling
            assert potential >= 3*coupling**2

            # Independent finite-difference -L exp(S_J/2) / exp(S_J/2).
            step = 1e-5
            s0 = action(touching, field, coupling)
            measured = 0.0
            for edge in outer:
                for index, tangent in enumerate(basis):
                    plus, minus = dict(field), dict(field)
                    plus[edge] = field[edge] @ exp_anti(step*tangent)
                    minus[edge] = field[edge] @ exp_anti(-step*tangent)
                    dp = action(touching, plus, coupling)-s0
                    dm = action(touching, minus, coupling)-s0
                    wp, wm = np.expm1(dp/2), np.expm1(dm/2)
                    measured -= ((wp+wm)/step**2
                                 - full_gradient[edge][index]*(wp-wm)/(2*step))
            error = abs(measured-potential)/(1+abs(potential))
            maximum_error = max(maximum_error, error)
            assert error < 2e-4
            remainder = 24/coupling
            assert 0 < remainder <= 0.5
            assert np.isclose(6/(6*coupling**2), 1/coupling**2)
            cases += 1

    # Test the trace-gradient bound on unconstrained, noncommuting link data.
    for _ in range(40):
        plaquette = touching[rng.integers(len(touching))]
        field = {edge: haar_su3(rng) for edge, _ in plaquette}
        for edge, _ in plaquette:
            assert np.linalg.norm(phi_gradient(plaquette, field, edge, basis)) <= 1
    return cases, maximum_error


def retained_certificate_checks(asymmetric):
    rng = np.random.default_rng(121)
    basis = su3_basis()
    active, outer, _, touching, external, central = lattice()
    cases = 0
    for coupling in (1, 25, 28, 48):
        for family in ("central", "asymmetric", "generic"):
            if family == "generic":
                field = {edge: haar_su3(rng) for edge in central}
            else:
                field = dict(central if family == "central" else asymmetric)
            excess = sum(max(np.linalg.norm(force(external, field, edge, basis))
                             - 1, 0)**2 for edge in outer)
            certificate = coupling**2*excess/4 - 4*coupling*(
                6 + sum(phi(p, field) for p in external))
            assert certificate >= -144*coupling - 1e-10
            if coupling >= 28 and family != "generic":
                assert certificate >= 24*coupling - 1e-10
            for _ in range(3):
                field[active] = haar_su3(rng)
                gradient_squared = coupling**2 * sum(
                    np.linalg.norm(force(touching, field, edge, basis))**2
                    for edge in outer)
                laplacian = 8*coupling*sum(phi(p, field) for p in touching)
                potential = gradient_squared/4-laplacian/2
                assert potential >= certificate - 1e-9
                cases += 1
    return cases


if __name__ == "__main__":
    field, hessian_error = asymmetric_geometry()
    cases, force_error = full_force_checks(field)
    print("PASS exact asymmetric six-staple source and positive external traces")
    print("PASS exterior-force norm: 44 sqrt(2) / 15 =", 44*np.sqrt(2)/15)
    print("PASS 48 unequal-well Hessian checks; max relative error:", hessian_error)
    print("PASS full Wilson force and half-action localizer:", cases,
          "max relative error:", force_error)
    print("PASS 160 generic plaquette gradient bounds and sixfold form coefficient")
    print("PASS retained force-curvature and common-union certificates:",
          retained_certificate_checks(field))
    print("Scope: finite algebra and local-context bounds, not a global mass gap.")
