"""Finite SU(N) faithful/adjoint identities; no physical spectrum is computed."""

import numpy as np


def random_su(n, rng):
    z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    u, r = np.linalg.qr(z)
    u = u @ np.diag(np.diag(r) / np.abs(np.diag(r)))
    u[:, 0] /= np.linalg.det(u)
    return u


def responses(u):
    n = len(u)
    t = np.trace(u) / n
    char_adjoint = abs(np.trace(u)) ** 2 - 1
    a = (n * n - 1) / (2 * n * n) * (1 - char_adjoint / (n * n - 1))
    return 1 - t.real, a, abs(1 - t) ** 2 / 2


def check(n):
    rng = np.random.default_rng(102 + n)
    for _ in range(40):
        u = random_su(n, rng)
        w, a, residue = responses(u)
        assert abs(w - a - residue) < 2e-14
        assert a >= -2e-14 and w >= a - 2e-14
        t = np.trace(u) / n
        assert abs(np.linalg.norm(u - t * np.eye(n)) ** 2 / (2 * n) - a) < 2e-14
    z = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    h = (z + z.conj().T) / 2
    h -= np.trace(h) * np.eye(n) / n
    h /= np.sqrt(np.trace(h @ h).real / n)
    eigenvalues, basis = np.linalg.eigh(h)

    def exp_x(s):
        return (basis * np.exp(1j * s * eigenvalues)) @ basis.conj().T

    step = 1e-3
    for j in range(n):
        center = np.exp(2j * np.pi * j / n)
        u = center * np.eye(n)
        w0, a0, _ = responses(u)
        assert abs(w0 - (1 - center.real)) < 2e-14
        assert abs(a0) < 2e-14
        wp, ap, _ = responses(center * exp_x(step))
        wm, am, _ = responses(center * exp_x(-step))
        assert abs((wp + wm - 2 * w0) / step**2 - center.real) < 2e-6
        assert abs((ap + am - 2 * a0) / step**2 - 1) < 2e-6
    ratios = []
    for s in (0.08, 0.04, 0.02):
        _, _, residue = responses(exp_x(s))
        ratios.append(residue / s**4)
    # g_N(X,X)=1 makes the leading quartic coefficient 1/8.
    assert abs(ratios[-1] - 0.125) < 1e-4
    assert abs(ratios[-1] - 0.125) < abs(ratios[0] - 0.125)
    print(f"SU({n}): exact decomposition, center Hessians, "
          f"quartic coefficient={ratios[-1]:.8f}; PASS")


if __name__ == "__main__":
    for rank in (2, 3, 4):
        check(rank)
    print("PASS: nonlinear probe identities only; no interacting or continuum gap.")
