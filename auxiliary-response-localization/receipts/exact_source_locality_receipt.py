"""Finite exact-source locality diagnostic; not a uniform physical-gap proof."""

import numpy as np


def check_cycle(n):
    d = np.zeros((n, n))
    for e in range(n):
        d[e, e] = -1
        d[e, (e + 1) % n] = 1
    k = d @ d.T
    vals, vecs = np.linalg.eigh(k)
    rho = float(vals[1])
    assert abs(vals[0]) < 1e-12
    assert abs(rho - 4 * np.sin(np.pi / n) ** 2) < 1e-12
    q = d[:, 0]
    support = np.flatnonzero(q)
    dist = np.minimum(
        (np.arange(n)[:, None] - support[None, :]) % n,
        (support[None, :] - np.arange(n)[:, None]) % n,
    ).min(axis=1)
    theta = 0.35
    w = np.exp(theta * dist)
    perturbation = w[:, None] * k / w[None, :] - k
    moment = 2 * np.expm1(theta)
    assert np.linalg.norm(perturbation, 2) <= moment + 1e-12
    # A spatial weight can send an exact vector into the harmonic sector.
    other_exact = d[:, 2]
    assert abs(np.sum(w * other_exact)) > 1e-6
    inverse = (vecs[:, 1:] / vals[1:]) @ vecs[:, 1:].T
    response = inverse @ q
    qnorm = np.linalg.norm(q)
    exponent = theta * dist * rho / (rho + moment)
    bound = ((1 / rho + 1 / moment) * np.exp(-exponent)
             - np.exp(-theta * dist) / moment) * qnorm
    assert np.all(np.abs(response) <= bound + 1e-11)
    worst_heat_ratio = 0.0
    for t in np.r_[0.0, np.geomspace(1e-3, 20 / rho, 60)]:
        # Omit the zero-mode component, known to vanish exactly for q.
        heat = vecs[:, 1:] @ (
            np.exp(-t * vals[1:]) * (vecs[:, 1:].T @ q)
        )
        local_bound = np.minimum(
            np.exp(-rho * t),
            np.exp(np.minimum(700, -theta * dist + moment * t)),
        ) * qnorm
        assert np.all(np.abs(heat) <= local_bound + 2e-12)
        worst_heat_ratio = max(
            worst_heat_ratio, float(np.max(np.abs(heat) / local_bound))
        )
    rng = np.random.default_rng(n)
    f, g = rng.normal(size=(2, n))
    f -= f.mean()
    g -= g.mean()
    # Uniform vertex law gives covariance f.g/n and edge form norm /n.
    assert abs(f @ g / n - (d @ f) @ inverse @ (d @ g) / n) < 1e-11
    print(f"cycle={n}: harmonic kernel; exact rho={rho:.8g}; "
          f"maximum heat/bound={worst_heat_ratio:.6f}; PASS")


if __name__ == "__main__":
    for size in (8, 16, 32):
        check_cycle(size)
    print("PASS: exact-source split and covariance identity; rho is not uniform in size.")
