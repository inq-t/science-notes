"""Finite checks for regional randomization, response lifting and Fisher contraction.

The analytic proofs belong to the linked notes. These checks do not construct
a continuum Yang--Mills theory, verify Lie-group curvature, or predict a mass.
Requires NumPy only; writes no files.
"""

import importlib.util
import itertools
from pathlib import Path
import sys

sys.dont_write_bytecode = True
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "bridge_helpers",
    ROOT / "conditional-fisher-coercivity/receipts/coarse_fisher_and_bridge_lifting_receipt.py",
)
H = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(H)
RNG = np.random.default_rng(109)


def close(a, b, tol=4e-11):
    assert np.max(np.abs(np.asarray(a) - np.asarray(b))) < tol


def psd(a, tol=4e-11):
    assert np.linalg.eigvalsh((a + a.T) / 2)[0] > -tol


def invsqrt(a):
    vals, vecs = np.linalg.eigh(a)
    assert vals[0] > 0
    return (vecs * (1 / np.sqrt(vals))) @ vecs.T


def kernel(n, m):
    raw = np.exp(RNG.normal(size=(n, m)))
    return raw / raw.sum(axis=1, keepdims=True)


def regional_step(joint, q, r):
    """Positive-atom lifting tests; degenerate carriers are checked separately."""
    joint = joint / joint.sum()
    ny, nz = joint.shape
    nx, nw = q.shape[1], r.shape[1]
    # Axes are original core, retained core, original boundary, retained boundary.
    tensor = joint[:, None, :, None] * q[:, :, None, None] * r[None, None, :, :]
    ext = tensor.reshape(ny * nx, nz * nw)
    close(tensor.sum(axis=(1, 3)), joint)
    pyx, pzw = ext.sum(axis=1), ext.sum(axis=0)
    jy, _ = H.pullback(pyx, np.repeat(np.arange(ny), nx))
    jz, _ = H.pullback(pzw, np.repeat(np.arange(nz), nw))
    jx, px = H.pullback(pyx, np.tile(np.arange(nx), ny))
    jw, _ = H.pullback(pzw, np.tile(np.arange(nw), nz))
    k, ke = H.predictor(joint), H.predictor(ext)
    bmat = np.eye(ny) - k.T @ k
    be = np.eye(ny * nx) - ke.T @ ke
    close(ke, jz @ k @ jy.T)
    close(be, jy @ bmat @ jy.T + np.eye(ny * nx) - jy @ jy.T)
    close(H.bridge_gap(ext), H.bridge_gap(joint))
    coarse = q.T @ joint @ r
    bc = np.eye(nx) - H.predictor(coarse).T @ H.predictor(coarse)
    amat = jx.T @ be @ jx
    leakage = (np.eye(nz * nw) - jw @ jw.T) @ ke @ jx
    close(bc, amat + leakage.T @ leakage)
    basis = H.centered_basis(px)
    ac = basis.T @ amat @ basis
    lc = basis.T @ leakage.T @ leakage @ basis
    ai = invsqrt(ac)
    relative = max(0.0, np.linalg.eigvalsh(ai @ lc @ ai)[-1])
    psd(relative * ac - lc)
    b = min(H.bridge_gap(joint * q[:, x, None]) for x in range(nx))
    psd(be - b * (np.eye(ny * nx) - jx @ jx.T))
    kc = H.bridge_gap(coarse)
    floor = H.bridge_gap(joint)
    lower = b * kc / (1 + relative)
    assert floor >= lower - 4e-11
    return floor, kc, b, relative, lower


def normalized_gap(joint):
    """Delete null atoms and normalize the floor on trivial centered carriers."""
    joint = joint[np.any(joint > 0, axis=1), :]
    joint = joint[:, np.any(joint > 0, axis=0)]
    joint = joint / joint.sum()
    by = H.centered_basis(joint.sum(axis=1))
    bz = H.centered_basis(joint.sum(axis=0))
    centered = bz.T @ H.predictor(joint) @ by
    return 1.0 if centered.size == 0 else 1 - np.linalg.norm(centered, 2) ** 2


def check_degenerate_carriers():
    for ny, nz in ((2, 2), (1, 2), (2, 1), (1, 1)):
        joint = np.exp(RNG.normal(size=(ny, nz)))
        joint /= joint.sum()
        for private_noise in (False, True):
            q = np.full((ny, 2), 0.5) if private_noise else np.eye(ny)
            r = np.full((nz, 2), 0.5) if private_noise else np.eye(nz)
            nx, nw = q.shape[1], r.shape[1]
            tensor = joint[:, None, :, None] * q[:, :, None, None] * r[None, None, :, :]
            ext = tensor.reshape(ny * nx, nz * nw)
            core_support, boundary_support = ext.sum(axis=1) > 0, ext.sum(axis=0) > 0
            ext = ext[core_support][:, boundary_support]
            jy, _ = H.pullback(
                ext.sum(axis=1), np.repeat(np.arange(ny), nx)[core_support]
            )
            jz, _ = H.pullback(
                ext.sum(axis=0), np.repeat(np.arange(nz), nw)[boundary_support]
            )
            k, ke = H.predictor(joint), H.predictor(ext)
            close(ke, jz @ k @ jy.T)
            close(
                np.eye(len(ext)) - ke.T @ ke,
                jy @ (np.eye(ny) - k.T @ k) @ jy.T + np.eye(len(ext)) - jy @ jy.T,
            )
            close(normalized_gap(ext), normalized_gap(joint))
            if min(ny, nz) == 1:
                close(normalized_gap(ext), 1)
    close(normalized_gap(np.array([[0.5, 0.5], [0.0, 0.0]])), 1)


def check_regional_lifting():
    for _ in range(50):
        joint = np.exp(RNG.normal(size=(4, 3)))
        regional_step(joint, kernel(4, 3), kernel(3, 2))
    joint = np.array([[0.4, 0.1], [0.1, 0.4]])
    erased = regional_step(joint, np.full((2, 3), 1 / 3), np.full((2, 2), 0.5))
    close(erased, [0.64, 1, 0.64, 0, 0.64])


def expected_conditional_variance(prob, values, labels):
    """Direct finite disintegration, including zero-probability atoms."""
    result = 0.0
    for label in np.unique(labels):
        selected = labels == label
        p, f = prob[selected], values[selected]
        mass = p.sum()
        if mass:
            result += np.dot(p, f * f) - np.dot(p, f) ** 2 / mass
    return result


def check_complete_quantifier():
    yz = np.array([[1 / 3, 0], [0, 1 / 3], [1 / 6, 1 / 6]])
    q = np.array([[0.5, 0.5], [0.5, 0.5], [0, 1]])
    joint = yz[:, None, :] * q[:, :, None]
    y, x, z = np.indices(joint.shape).reshape(3, -1)
    prob = joint.ravel()
    for _ in range(50):
        u, v, t = RNG.normal(size=3)
        f = np.array([u, v, t])[y]
        n = expected_conditional_variance(prob, f, 2 * x + z)
        d = expected_conditional_variance(prob, f, x)
        close(n, ((u - t) ** 2 + (v - t) ** 2) / 12)
        close(d, n + (u - v) ** 2 / 8)
        assert n >= d / 4 - 2e-12
    sharp = np.array([1.0, -1.0, 0])[y]
    close(
        expected_conditional_variance(prob, sharp, 2 * x + z)
        / expected_conditional_variance(prob, sharp, x),
        0.25,
    )
    witness = (x == 0) * ((y == 0).astype(float) - (y == 1))
    close(expected_conditional_variance(prob, witness, 2 * x + z), 0)
    close(expected_conditional_variance(prob, witness, x), 1 / 3)


def check_gaussian_cancellation():
    count = 0
    for t, u, v in itertools.product(
        (0.0, 0.2, -0.8, 0.999), (0.0, 0.01, 1.0, 100.0), (0.0, 0.03, 2.0, 100.0)
    ):
        d, a, c = 1 - t * t, 1 + u, 1 + v
        kc = 1 - t * t / (a * c)
        b = d * a / (u + d)
        relative = t * t * v / (c * (u + d))
        close(b * kc / (1 + relative), d)
        alpha, q0 = t * t / a, 1 / c
        for n in range(1, 51):
            rn = alpha**n * (1 - q0**n) / (1 - alpha**n)
            assert rn <= relative + 2e-11
        # Actual conditional correlation of Y,Z given X, not a marginal surrogate.
        if u:
            vy, vz, cyz = u / a, 1 - t * t / a, t * u / a
            close(1 - cyz * cyz / (vy * vz), b)
        else:
            close(b, 1)
        if u and v:
            sy = np.array([[1, 1], [1, a]])
            sz = np.array([[1, 1], [1, c]])
            cross = np.full((2, 2), t)
            correlation = invsqrt(sy) @ cross @ invsqrt(sz)
            close(1 - np.linalg.norm(correlation, 2) ** 2, d, 2e-10)
        count += 1
    return count


def check_shared_noise():
    # Independent Y,Z; correlated auxiliary signs R,S with correlation eta.
    states = np.array(list(itertools.product((-1, 1), repeat=2)))
    for eta in (0.0, 0.4, 0.99, 1.0):
        ext = (1 + eta * states[:, 1, None] * states[None, :, 1]) / 16
        close(H.bridge_gap(ext), 1 - eta * eta)
        jy, _ = H.pullback(ext.sum(axis=1), np.repeat(np.arange(2), 2))
        bmat = np.eye(4) - H.predictor(ext).T @ H.predictor(ext)
        basis = H.centered_basis(np.array([0.5, 0.5]))
        # Original centered source still has response one.
        close(basis.T @ jy.T @ bmat @ jy @ basis, [[1]])


def check_tower():
    joint = np.array([[0.43, 0.07], [0.07, 0.43]])
    qs, rs = [kernel(2, 2) for _ in range(3)], [kernel(2, 2) for _ in range(3)]
    pairs, factors = [joint], []
    for q, r in zip(qs, rs):
        _, _, b, relative, _ = regional_step(pairs[-1], q, r)
        factors.append(b / (1 + relative))
        pairs.append(q.T @ pairs[-1] @ r)
    assert H.bridge_gap(joint) >= H.bridge_gap(pairs[-1]) * np.prod(factors) - 4e-11
    # Suffix histories, unlike individual time-slice variables, are nested.
    for start in range(3):
        histories = list(itertools.product(range(2), repeat=4 - start))
        suffix = np.empty((len(histories), len(histories)))
        for iy, yh in enumerate(histories):
            for iz, zh in enumerate(histories):
                weight = pairs[start][yh[0], zh[0]]
                for k in range(3 - start):
                    weight *= qs[start + k][yh[k], yh[k + 1]]
                    weight *= rs[start + k][zh[k], zh[k + 1]]
                suffix[iy, iz] = weight
        close(suffix.sum(), 1)
        close(H.bridge_gap(suffix), H.bridge_gap(pairs[start]))


def check_fisher_tensor():
    for _ in range(50):
        py = RNG.uniform(0.1, 1, size=6)
        py /= py.sum()
        q = kernel(6, 4)
        joint, px = py[:, None] * q, py @ q
        features = RNG.normal(size=(6, 3))
        sy = features - py @ features
        sx = (joint.T @ sy) / px[:, None]
        iy, ix = sy.T @ (py[:, None] * sy), sx.T @ (px[:, None] * sx)
        tau = 1 - H.bridge_gap(joint)
        psd(tau * iy - ix)
        psd(iy - ix - (1 - tau) * iy)
    # Checks the operator contraction, not a continuous Poincare estimate.


def check_nonlinear_normalization():
    # Finite Z2 subgroup calibration, not a Lie-group curvature test.
    states = np.array(list(itertools.product((-1, 1), repeat=2)))
    for beta, kx, kw in itertools.product((0.02, 0.2, 0.8), (0.1, 1.2), (0.2, 2.0)):
        y1, y2 = states[:, 0, None], states[:, 1, None]
        z1, z2 = states[None, :, 0], states[None, :, 1]
        action = beta * (3 - y1 * z1 - y2 * z2 - y1 * y2 * z1 * z2)
        joint = np.exp(-action)
        joint /= joint.sum()
        averaged_paths = states.mean(axis=1)
        q = np.exp(kx * averaged_paths[:, None] * np.array([-1, 1]))
        r = np.exp(kw * averaged_paths[:, None] * np.array([-1, 1]))
        # The normalization depends on the fine configuration.
        assert np.ptp(q.sum(axis=1)) > 0
        q /= q.sum(axis=1, keepdims=True)
        r /= r.sum(axis=1, keepdims=True)
        regional_step(joint, q, r)
        for x in range(2):
            posterior = joint * q[:, x, None]
            unchanged = posterior / posterior.sum(axis=1, keepdims=True)
            close(unchanged, joint / joint.sum(axis=1, keepdims=True))


def check_sufficient_constants():
    for rho0, fraction, h, c in itertools.product(
        (0.1, 1.0, 4.5), (0.1, 0.5, 1.0), (0.0, 0.2, 3.0), (0.0, 0.5, 8.0)
    ):
        rhox = fraction * rho0
        b = rho0 * rhox / (rho0 * rhox + h * h)
        naive = rhox * rhox / (rhox * rhox + h * h)
        tau = c / (rho0 + c)
        relative = tau * h * h / rho0**2
        assert 0 < naive <= b + 1e-12 <= 1 + 1e-12
        assert 0 <= relative <= h * h / rho0**2 + 1e-12
        close(b / (1 + relative), b * rho0**2 / (rho0**2 + tau * h * h))
    # When X=Y the discarded-core inequality is vacuous. A normalized
    # certificate must be capped at one, not inferred from that inequality.
    independent = np.full((2, 2), 0.25)
    close(H.bridge_gap(independent), 1)
    assert 2 * H.bridge_gap(independent) > H.bridge_gap(independent)


if __name__ == "__main__":
    check_degenerate_carriers()
    print("PASS eight deterministic/private-noise degeneracies, trivial carriers, and null atoms")
    check_regional_lifting()
    print("PASS 50 regional joint-law factorizations, full floors, relative lifts, and erasure")
    check_complete_quantifier()
    print("PASS sharp 1/4 restricted-source bound with zero complete discarded-core floor")
    count = check_gaussian_cancellation()
    print(f"PASS {count} Gaussian noise choices, 50 Hermite degrees each, and exact cancellation")
    check_shared_noise()
    print("PASS shared-noise failure and preserved restricted original-source response")
    check_tower()
    print("PASS three-step Markov product and nested suffix-history response identities")
    check_fisher_tensor()
    print("PASS 50 complete Fisher tensor contractions")
    check_nonlinear_normalization()
    print("PASS 12 nonlinear finite-subgroup laws with fine-dependent readout normalizers")
    check_sufficient_constants()
    print("PASS 81 sufficient-constant combinations and vacuous-condition cap warning")
    print("SCOPE: finite identities and calibrations; no continuum or physical mass-gap claim")
