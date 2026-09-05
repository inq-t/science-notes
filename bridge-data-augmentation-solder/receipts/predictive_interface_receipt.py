"""Checks exact/approximate predictive interfaces and physical carrier selection.

NumPy-only finite checks, not an interacting continuum existence/gap proof.
No files are written. Gaussian complete-spectrum statements additionally
use the analytic Hermite argument in the canonical notes.
"""

import importlib.util
import itertools
from math import log, tanh
from pathlib import Path
import sys

sys.dont_write_bytecode = True
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "regional_helpers", ROOT / "bridge-data-augmentation-solder/receipts/regional_randomization_receipt.py"
)
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
H = R.H
RNG = np.random.default_rng(110)


def close(a, b, tol=5e-10):
    assert np.max(np.abs(np.asarray(a) - np.asarray(b))) < tol


def mutual_information(joint):
    joint = joint / joint.sum()
    product = joint.sum(axis=1)[:, None] * joint.sum(axis=0)[None, :]
    positive = joint > 0
    return np.sum(joint[positive] * np.log(joint[positive] / product[positive]))


def deterministic_data(joint, x_labels, w_labels):
    """Positive marginals, nontrivial retained carrier, invertible retained response."""
    joint = joint / joint.sum()
    py, pz = joint.sum(axis=1), joint.sum(axis=0)
    jx, px = H.pullback(py, x_labels)
    jw, _ = H.pullback(pz, w_labels)
    k = H.predictor(joint)
    q = np.eye(len(py)) - jx @ jx.T
    kc = jw.T @ k @ jx
    bf = np.eye(len(py)) - k.T @ k
    bc = np.eye(len(px)) - kc.T @ kc
    basis = H.centered_basis(px)
    a = basis.T @ jx.T @ bf @ jx @ basis
    leakage = (np.eye(len(pz)) - jw @ jw.T) @ k @ jx @ basis
    ai = R.invsqrt(a)
    relative = max(0.0, np.linalg.eigvalsh(ai @ leakage.T @ leakage @ ai)[-1])
    delta = np.linalg.norm(k @ q, 2) ** 2
    kappa_c = np.linalg.eigvalsh(basis.T @ bc @ basis)[0]
    floor = R.normalized_gap(joint)
    assert floor >= kappa_c / (1 + relative) - delta - 5e-10
    # Product-reference density residual, not joint conditional expectation.
    density = joint / (py[:, None] * pz[None, :])
    reduced = np.zeros_like(density)
    for x in np.unique(x_labels):
        rows = x_labels == x
        reduced[rows] = (py[rows] @ density[rows]) / py[rows].sum()
    residual = density - reduced
    hs_sq = np.sum(py[:, None] * pz[None, :] * residual**2)
    assert delta <= hs_sq + 5e-10
    # Conditional mutual information equals the projected-density KL residual.
    positive = joint > 0
    cmi = np.sum(joint[positive] * np.log(density[positive] / reduced[positive]))
    assert hs_sq <= 2 * np.max(density) * cmi + 5e-10
    return k, kc, jx, jw, bf, bc, floor, delta, relative, hs_sq, cmi


def check_exact_and_approximate():
    # Exact identities also cover a constant sufficient statistic and zero gap;
    # these cases do not require the invertible-response comparison helper.
    for joint, labels in (
        (np.outer([0.3, 0.7], [0.4, 0.6]), np.zeros(2, dtype=int)),
        (np.diag([0.3, 0.7]), np.arange(2)),
    ):
        k = H.predictor(joint)
        jx, _ = H.pullback(joint.sum(axis=1), labels)
        jw, _ = H.pullback(joint.sum(axis=0), labels)
        kc = jw.T @ k @ jx
        close(k, jw @ kc @ jx.T)
        bf = np.eye(2) - k.T @ k
        bc = np.eye(kc.shape[1]) - kc.T @ kc
        close(bf, jx @ bc @ jx.T + np.eye(2) - jx @ jx.T)
        close(R.normalized_gap(joint), 1 if len(np.unique(labels)) == 1 else 0)
    for _ in range(30):
        eta = np.exp(RNG.normal(size=(3, 2)))
        eta /= eta.sum()
        q = R.kernel(3, 2)
        r = R.kernel(2, 3)
        joint = (eta[:, None, :, None] * q[:, :, None, None] * r[None, None, :, :]).reshape(6, 6)
        data = deterministic_data(joint, np.repeat(np.arange(3), 2), np.repeat(np.arange(2), 3))
        k, kc, jx, jw, bf, bc, floor, delta, relative, _, _ = data
        close(k, jw @ kc @ jx.T)
        close(bf, jx @ bc @ jx.T + np.eye(6) - jx @ jx.T)
        close(floor, R.normalized_gap(eta))
        close([delta, relative], [0, 0])
        # Complete conditional distributions are identical inside each fiber.
        zy = joint / joint.sum(axis=1, keepdims=True)
        for t in range(3):
            close(zy[2 * t], zy[2 * t + 1])
    for _ in range(50):
        joint = np.exp(RNG.normal(size=(6, 4)))
        deterministic_data(joint, np.repeat(np.arange(3), 2), np.repeat(np.arange(2), 2))


def check_rare_sectors():
    states = np.array(list(itertools.product((0, 1), (-1, 1))))
    for eps, rho in itertools.product((0.2, 0.02, 0.002), (0.1, 0.9, 0.9999, 1.0)):
        weights = np.where(states[:, 0] == 1, eps, 1 - eps)
        joint = weights[:, None] * (
            1 + rho * states[:, 0, None] * states[:, 1, None] * np.array([-1, 1])
        ) / 4
        data = deterministic_data(joint, states[:, 0], np.array([0, 1]))
        floor, delta, relative, hs_sq, cmi = data[6:]
        close([floor, delta, relative, hs_sq], [1 - eps * rho**2, eps * rho**2, 0, eps * rho**2])
        j = 0.5 * ((1 + rho) * log(1 + rho) + ((1 - rho) * log(1 - rho) if rho < 1 else 0))
        close(cmi, eps * j)
        conditional = min(R.normalized_gap(joint[states[:, 0] == s]) for s in (0, 1))
        close(conditional, 1 - rho**2)
    for eps in (0.2, 0.02, 0.002, 0.0002):
        eta = eps**2 * (1 - eps)
        joint = np.array([[1 - eps - eta, eta], [eta, eps - eta]])
        assert np.all(joint > 0)
        close(R.normalized_gap(joint), 2 * eps - eps**2)
        entropy = -eps * log(eps) - (1 - eps) * log(1 - eps)
        assert mutual_information(joint) <= entropy + 1e-12


def check_likelihood_tilts():
    for _ in range(50):
        joint = np.exp(RNG.normal(size=(4, 3)))
        joint /= joint.sum()
        weights = np.exp(RNG.normal(size=4))
        ratio = weights.max() / weights.min()
        before = R.normalized_gap(joint)
        after = R.normalized_gap(joint * weights[:, None])
        assert before / ratio - 5e-11 <= after <= min(1, ratio * before) + 5e-11
    independent = np.full((3, 2), 1 / 6)
    for q in (R.kernel(3, 2), R.kernel(3, 4)):
        close([R.normalized_gap(independent * q[:, x, None]) for x in range(q.shape[1])], 1)


def check_wilson_interfaces():
    states = np.array(list(itertools.product((-1, 1), repeat=3)))
    t_labels = np.repeat(np.arange(4), 2)
    y, z = states[:, None, :], states[None, :, :]
    sy = -0.3 * states[:, 0] * states[:, 2] - 0.2 * states[:, 1] * states[:, 2]
    sz = -0.4 * states[:, 0] * states[:, 2] + 0.1 * states[:, 1] * states[:, 2]
    for beta in (0.05, 0.7, 2.0):
        cross = -beta * (y[:, :, 0] * z[:, :, 0] + y[:, :, 0] * y[:, :, 1] * z[:, :, 0] * z[:, :, 1])
        joint = np.exp(-sy[:, None] - sz[None, :] - cross)
        data = deterministic_data(joint, t_labels, t_labels)
        k, kc, jx, jw, bf, bc, floor, delta, relative, _, _ = data
        close(k, jw @ kc @ jx.T)
        close(bf, jx @ bc @ jx.T + np.eye(8) - jx @ jx.T)
        close([delta, relative], 0)
        # Independent calculation of the induced interface self-weights.
        my = np.exp(-sy).reshape(4, 2).sum(axis=1)
        mz = np.exp(-sz).reshape(4, 2).sum(axis=1)
        eta = my[:, None] * mz[None, :] * np.exp(-cross[::2, ::2])
        close(floor, R.normalized_gap(eta))
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sz_matrix = np.diag([1, -1]).astype(complex)
    a, b = 1j * sx, 1j * sz_matrix
    close(a @ a.conj().T, np.eye(2))
    close(b @ b.conj().T, np.eye(2))
    close(a @ b @ a.conj().T @ b.conj().T, -np.eye(2))
    close(np.eye(2) @ b @ np.eye(2) @ b.conj().T, np.eye(2))


def symmetric_root(a):
    values, vectors = np.linalg.eigh(a)
    assert values[0] > 0
    return (vectors * np.sqrt(values)) @ vectors.T


def gaussian_floor(sy, sz, cross):
    t = R.invsqrt(sy) @ cross @ R.invsqrt(sz)
    return 1 - np.linalg.norm(t, 2) ** 2


def check_gaussian_rank():
    for n, m, rank in ((4, 3, 1), (4, 3, 2), (3, 3, 3)):
        for _ in range(10):
            raw_a, raw_d = RNG.normal(size=(n, n)), RNG.normal(size=(m, m))
            a, d = np.eye(n) + raw_a @ raw_a.T, np.eye(m) + raw_d @ raw_d.T
            u, _ = np.linalg.qr(RNG.normal(size=(n, n)))
            v, _ = np.linalg.qr(RNG.normal(size=(m, m)))
            singular = np.linspace(0.15, 0.8, rank)
            t = (u[:, :rank] * singular) @ v[:, :rank].T
            c = symmetric_root(a) @ t @ symmetric_root(d)
            precision = np.block([[a, c], [c.T, d]])
            covariance = np.linalg.inv(precision)
            sy, sz, cross = covariance[:n, :n], covariance[n:, n:], covariance[:n, n:]
            exact = 1 - max(singular) ** 2
            close(gaussian_floor(sy, sz, cross), exact)
            # Independent rank-r coordinate maps on the actual marginal covariance.
            uc, sc, vc_t = np.linalg.svd(c, full_matrices=False)
            ly, lz = uc[:, :rank].T, vc_t[:rank]
            close(gaussian_floor(ly @ sy @ ly.T, lz @ sz @ lz.T, ly @ cross @ lz.T), exact)
            fisher_gap = np.min((1 - singular**2) / singular**2)
            close(fisher_gap / (1 + fisher_gap), exact)
            # Conditional precision with a genuinely noisy linear readout.
            readout = RNG.normal(size=(2, n))
            ax = a + readout.T @ readout
            posterior = np.linalg.inv(np.block([[ax, c], [c.T, d]]))
            bx = 1 - np.linalg.norm(R.invsqrt(ax) @ c @ R.invsqrt(d), 2) ** 2
            close(gaussian_floor(posterior[:n, :n], posterior[n:, n:], posterior[:n, n:]), bx)
            assert bx < 1
    for eps in (0.01, 0.1, 0.4, 0.65):
        n = 4
        eye, zero = np.eye(n), np.zeros((n, n))
        precision = np.block([[eye, eps * eye, zero], [eps * eye, eye, eps * eye], [zero, eps * eye, eye]])
        covariance = np.linalg.inv(precision)
        keep = list(range(n)) + list(range(2 * n, 3 * n))
        effective = np.linalg.inv(covariance[np.ix_(keep, keep)])
        close(effective[:n, :n], (1 - eps**2) * eye)
        close(effective[:n, n:], -eps**2 * eye)
        assert np.linalg.matrix_rank(effective[:n, n:]) == n
        close(gaussian_floor(covariance[:n, :n], covariance[2*n:, 2*n:], covariance[:n, 2*n:]), 1 - eps**4 / (1 - eps**2)**2)


def check_physical_separation():
    for omega, ell in itertools.product((0.2, 0.9, 2.0), (0.5, 1.2)):
        previous = 1.0
        for n in (2, 4, 8, 16, 32):
            a = ell / n
            times = np.linspace(-ell, ell, 2 * n + 1)
            covariance = np.exp(-omega * np.abs(times[:, None] - times[None, :]))
            sy, sz = covariance[1:-1, 1:-1], covariance[np.ix_([0, 2*n], [0, 2*n])]
            cross = covariance[1:-1][:, [0, 2*n]]
            whole = gaussian_floor(sy, sz, cross)
            interface = gaussian_floor(sy[np.ix_([0, 2*n-2], [0, 2*n-2])], sz, cross[[0, 2*n-2]])
            expected = -np.expm1(-2 * omega * a) / (1 + np.exp(-2 * omega * ell))
            close([whole, interface], expected)
            mid = gaussian_floor(np.ones((1, 1)), sz, covariance[n:n+1, [0, 2*n]])
            close(mid, tanh(omega * ell))
            assert whole < previous and whole < mid
            previous = whole


def check_additive_budget():
    for depth in (1, 3, 10, 100):
        rs = 0.05 * 0.5 ** np.arange(depth)
        ds = 0.005 * 0.5 ** np.arange(depth)
        terminal = 0.7
        recursive = terminal
        for r, delta in reversed(list(zip(rs, ds))):
            recursive = recursive / (1 + r) - delta
        prefix, cost = 1.0, 0.0
        for r, delta in zip(rs, ds):
            cost += prefix * delta
            prefix /= 1 + r
        close(recursive, prefix * terminal - cost)
        assert recursive >= np.exp(-0.1) * terminal - 0.01


if __name__ == "__main__":
    check_exact_and_approximate()
    print("PASS two degenerate and 30 positive exact reductions; 50 prediction/entropy bounds")
    check_rare_sectors()
    print("PASS 12 sharp rare conditional sectors and four positive rare-atom KL controls")
    check_likelihood_tilts()
    print("PASS 50 bounded likelihood-tilt comparisons")
    check_wilson_interfaces()
    print("PASS three nonlinear finite-subgroup interfaces and SU(2) transport-order witness")
    check_gaussian_rank()
    print("PASS 30 Gaussian rank/Fisher/noisy-posterior checks and four full-rank collars")
    check_physical_separation()
    print("PASS 30 full-covariance slab refinements, interface equality, and fixed midpoint floor")
    check_additive_budget()
    print("PASS additive loss-budget indices through depth 100")
    print("SCOPE: finite mathematics only; no Yang--Mills continuum or mass prediction")
