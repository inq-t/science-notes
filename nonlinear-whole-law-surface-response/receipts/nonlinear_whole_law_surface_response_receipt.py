"""Finite checks for the Hessian soft mode and likelihood-frame identities."""

from __future__ import annotations

import math

import numpy as np


def soft_mode(L: float, spacing: float, half_depth: float) -> tuple[float, ...]:
    lattice_size = int(round(L / spacing))
    time_steps = int(round(half_depth / spacing))
    lam = 4.0 * math.sin(math.pi / lattice_size) ** 2
    omega = math.acosh(1.0 + lam / 2.0)
    omega_closed = 2.0 * math.asinh(math.sin(math.pi / lattice_size))
    kappa_one = math.tanh(time_steps * omega)
    kappa_singlet = 2.0 * kappa_one - kappa_one**2
    asymptotic = 4.0 * math.pi * half_depth / L
    assert math.isclose(omega, omega_closed, rel_tol=1e-13, abs_tol=1e-13)
    return lam, omega, kappa_one, kappa_singlet, asymptotic


def likelihood_frame() -> dict[str, float]:
    action = np.array(
        [
            [0.2, 1.1, 0.6, 1.8],
            [1.4, 0.1, 1.2, 0.5],
            [0.8, 1.6, 0.3, 0.9],
        ]
    )
    prior_boundary = np.array([0.25, 0.45, 0.30])
    prior_midpoint = np.array([0.10, 0.20, 0.30, 0.40])
    joint = (
        np.exp(-action)
        * prior_boundary[:, None]
        * prior_midpoint[None, :]
    )
    joint /= joint.sum()

    boundary = joint.sum(axis=1)
    midpoint = joint.sum(axis=0)
    conditional = joint / boundary[:, None]
    likelihood = conditional / midpoint[None, :]

    root_boundary = np.sqrt(boundary)
    root_midpoint = np.sqrt(midpoint)
    weighted_k = (
        root_boundary[:, None]
        * likelihood
        * root_midpoint[None, :]
    )
    weighted_a = (
        root_boundary[:, None]
        * (likelihood - 1.0)
        * root_midpoint[None, :]
    )

    constant_midpoint = root_midpoint
    constant_boundary = root_boundary
    assert np.allclose(weighted_k @ constant_midpoint, constant_boundary)
    assert np.allclose(weighted_a @ constant_midpoint, 0.0)

    q = np.eye(len(midpoint)) - np.outer(root_midpoint, root_midpoint)
    bridge = q @ (np.eye(len(midpoint)) - weighted_k.T @ weighted_k) @ q
    frame_bridge = q @ (np.eye(len(midpoint)) - weighted_a.T @ weighted_a) @ q
    assert np.allclose(bridge, frame_bridge)

    singular_values = np.linalg.svd(weighted_a, compute_uv=False)
    cosine = float(singular_values[0])
    centered_eigenvalues = np.linalg.eigvalsh(
        bridge + np.outer(root_midpoint, root_midpoint)
    )
    bridge_floor = float(centered_eigenvalues[0])
    assert np.isclose(bridge_floor, 1.0 - cosine**2)

    raw_f = np.array([-1.2, 0.3, 0.8, 1.4])
    raw_f -= np.dot(midpoint, raw_f)
    normalized_f = root_midpoint * raw_f
    form_value = float(normalized_f @ bridge @ normalized_f)
    conditional_mean = conditional @ raw_f
    conditional_second = conditional @ (raw_f**2)
    integrated_variance = float(
        np.dot(boundary, conditional_second - conditional_mean**2)
    )
    assert np.isclose(form_value, integrated_variance)

    ratios_10 = likelihood[1] / likelihood[0]
    ratios_21 = likelihood[2] / likelihood[1]
    ratios_20 = likelihood[2] / likelihood[0]
    assert np.allclose(ratios_21 * ratios_10, ratios_20)

    gram = weighted_a @ weighted_a.T
    nonzero_frame = np.linalg.eigvalsh(weighted_a.T @ weighted_a)
    nonzero_gram = np.linalg.eigvalsh(gram)
    frame_positive = nonzero_frame[nonzero_frame > 1e-12]
    gram_positive = nonzero_gram[nonzero_gram > 1e-12]
    assert np.allclose(frame_positive, gram_positive)

    return {
        "cosine": cosine,
        "bridge_floor": bridge_floor,
        "form_value": form_value,
        "integrated_variance": integrated_variance,
        "cocycle_error": float(
            np.max(np.abs(ratios_21 * ratios_10 - ratios_20))
        ),
    }


print("nonlinear whole-law surface-response receipt")
print("soft transverse Hessian mode at fixed a=0.01 and ell=1")
for physical_size in (20.0, 40.0, 80.0, 160.0):
    _, omega_value, _, singlet_value, asymptotic_value = soft_mode(
        physical_size, 0.01, 1.0
    )
    print(
        f"L={physical_size:6.1f}  omega={omega_value:.12e}  "
        f"kappa_sing={singlet_value:.12e}  "
        f"4*pi*ell/L={asymptotic_value:.12e}  "
        f"ratio={singlet_value / asymptotic_value:.8f}"
    )

frame = likelihood_frame()
print(f"likelihood maximal correlation: {frame['cosine']:.12f}")
print(f"bridge floor: {frame['bridge_floor']:.12f}")
print(f"1 - correlation^2: {1.0 - frame['cosine'] ** 2:.12f}")
print(f"bridge quadratic form: {frame['form_value']:.12f}")
print(f"integrated conditional variance: {frame['integrated_variance']:.12f}")
print(f"pairwise cocycle chain error: {frame['cocycle_error']:.3e}")
print("all checks passed")
