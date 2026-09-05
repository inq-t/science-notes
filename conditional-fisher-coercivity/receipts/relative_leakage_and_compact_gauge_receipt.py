"""Finite checks for relative leakage and normalized compact gauge response.

Uses NumPy and the standard library only. It reads existing receipt helpers,
does not write files, and does not verify a Yang--Mills continuum limit.
"""

import importlib.util
import math
from pathlib import Path
import sys

import numpy as np


sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
RNG = np.random.default_rng(108)


def load_helper(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BL = load_helper(
    "bridge_checks",
    "conditional-fisher-coercivity/receipts/coarse_fisher_and_bridge_lifting_receipt.py",
)
NG = load_helper(
    "gauge_checks",
    "rg-covariance-residue/receipts/nonlinear_conditional_gauge_response_receipt.py",
)


def close(left, right, tol=2e-10):
    assert np.max(np.abs(np.asarray(left) - np.asarray(right))) < tol


def check_relative_joint_laws():
    x_labels = np.repeat(np.arange(3), 2)
    w_labels = np.tile(np.arange(2), 3)
    for _ in range(50):
        joint = np.exp(RNG.normal(size=(6, 6)))
        joint /= joint.sum()
        py, pz = joint.sum(axis=1), joint.sum(axis=0)
        jx, px = BL.pullback(py, x_labels)
        jw, _ = BL.pullback(pz, w_labels)
        k = BL.predictor(joint)
        bmat = np.eye(6) - k.T @ k
        a = jx.T @ bmat @ jx
        leak = (np.eye(6) - jw @ jw.T) @ k @ jx
        coarse_k = jw.T @ k @ jx
        coarse_b = np.eye(3) - coarse_k.T @ coarse_k
        close(coarse_b, a + leak.T @ leak)

        # Exact discrete conditional bridge constants certify the relative
        # inequality without claiming a differential Fisher form on this set.
        xz = np.zeros((3, 6))
        np.add.at(xz, x_labels, joint)
        fiber_floor = min(
            BL.bridge_gap(xz[:, w_labels == w]) for w in range(2)
        )
        relative = 1 / fiber_floor - 1
        xb = BL.centered_basis(px)
        assert np.linalg.eigvalsh(
            xb.T @ (relative * a - leak.T @ leak) @ xb
        )[0] > -2e-11
        discarded = min(
            BL.bridge_gap(joint[x_labels == x, :]) for x in range(3)
        )
        assert np.linalg.eigvalsh(
            bmat - discarded * (np.eye(6) - jx @ jx.T)
        )[0] > -2e-11
        coarse_floor = np.linalg.eigvalsh(xb.T @ coarse_b @ xb)[0]
        assert BL.bridge_gap(joint) >= (
            discarded * coarse_floor / (1 + relative) - 2e-11
        )
        # The centered prediction maps in the two directions are adjoints.
        close(BL.bridge_gap(joint), BL.bridge_gap(joint.T))
    print("PASS: 50 actual joint-law relative lifts and adjoint floors.")


def check_gaussian_and_budget():
    for a, v, noise in ((2.0, 3.0, 0.4), (0.1, 8.0, 0.001), (4, 0.2, 7)):
        total = a + v + noise
        relative = v / noise
        fine = noise / total
        coarse = (v + noise) / total
        close(fine, coarse / (1 + relative))
        for n in range(1, 30):
            fine_response = 1 - ((a + v) / total) ** n
            coarse_response = 1 - (a / total) ** n
            assert coarse_response <= (1 + relative) * fine_response + 2e-11

    terminal, amp_c, amp_r = 0.7, 0.4, 0.6
    certificate = terminal * math.exp(-(amp_c + amp_r / 2))
    for depth in (1, 3, 10, 100, 500):
        levels = np.arange(1, depth + 1, dtype=float)
        cs, rs = amp_c * 2.0 ** (-levels), amp_r * 3.0 ** (-levels)
        lifted = terminal * math.exp(-np.sum(np.log1p(cs) + np.log1p(rs)))
        assert lifted >= certificate
    assert terminal * (1.01 ** -500) < terminal * (1.01 ** -10)
    print("PASS: sharp Gaussian relative factor; summable budget to 500 levels.")


def scaled_bessel(order, x):
    """Independent positive power series for exp(-x) I_order(x), x > 0."""
    logs = [
        (2 * k + order) * math.log(x / 2)
        - math.lgamma(k + 1) - math.lgamma(k + order + 1) - x
        for k in range(math.ceil(x) + 100)
    ]
    top = max(logs)
    return math.exp(top) * math.fsum(math.exp(term - top) for term in logs)


def check_compact_haar():
    count = 2048
    theta = np.pi * np.arange(1, count + 1) / (count + 1)
    x = np.cos(theta)
    haar = 2 / (count + 1) * np.sin(theta) ** 2
    for kappa in (0.001, 0.1, 1, 10, 100, 1000):
        raw = haar * np.exp(kappa * (x - 1))
        norm = raw.sum()
        prob = raw / norm
        i1 = scaled_bessel(1, kappa)
        a = scaled_bessel(2, kappa) / i1
        assert abs(norm / (2 * i1 / kappa) - 1) < 3e-11
        close(prob @ x, a, 3e-11)
        fisher = kappa**2 * (prob @ (1 - x * x)) / 3
        close(fisher, kappa * a, 3e-8)
        # The actual coarse Hessian is zero: mean curvature cancels Fisher.
        close(kappa * (prob @ x) - fisher, 0, 3e-8)
        ratios = []
        for dimension in range(1, 13):
            char = np.sin(dimension * theta) / np.sin(theta)
            eigenvalue = scaled_bessel(dimension, kappa) / i1
            close(prob @ char / dimension, eigenvalue, 3e-11)
            ratios.append(eigenvalue)
        assert all(ratios[n] > ratios[n + 1] for n in range(11))
        true_floor = 1 - a * a
        fisher_floor = 3 / (3 + kappa * a)
        assert 0 < fisher_floor <= true_floor + 3e-11
        if kappa == 1000:
            assert abs(kappa * true_floor - 3) < 0.01
            assert abs(fisher_floor / true_floor - 1) < 0.002
        print(
            f"kappa={kappa:g}: exact compact response={true_floor:.8g}; "
            f"Fisher certificate={fisher_floor:.8g}"
        )
    print("PASS: Haar normalization, all tested character sectors, Fisher and Hessian cancellation.")


def check_joint_incidence():
    words = list(NG.WORDS) + [((0, 1), (0, 1), (1, -1))]
    weights = np.array([[0.2, 0.3, 0.4, 0.1], [0.1, 0.1, 0.3, 0.5],
                        [0.4, 0.2, 0.2, 0.2]])
    incidence = np.array([
        [sum(edge == e for edge, _ in word) for e in range(2)] for word in words
    ])
    pmat = weights @ incidence
    size = np.linalg.norm(pmat, 2)
    assert size**2 <= pmat.sum(axis=1).max() * pmat.sum(axis=0).max() + 1e-12
    basis = np.eye(6).reshape(6, 2, 3)
    for _ in range(30):
        links = np.array([NG.random_su(RNG), NG.random_su(RNG)])
        coarse = [NG.random_su(RNG) for _ in range(3)]
        values, derivatives = [], []
        for word in words:
            values.append(NG.word_jet(links, np.zeros((2, 3)), word)[0])
            derivatives.append([
                NG.word_jet(links, vec, word)[1] for vec in basis
            ])
        values, derivatives = np.array(values), np.array(derivatives)
        for kappa in (0.03, 0.7, 3):
            forward_fisher = np.zeros((6, 6))
            mixed = np.zeros((9, 6))
            for b, w in enumerate(weights):
                z = NG.quaternion(np.einsum("i,ijk->jk", w, values))
                dz_mat = np.einsum("i,iajk->ajk", w, derivatives)
                jac = np.array([NG.quaternion(mat) for mat in dz_mat]).T
                _, _, cov = NG.normalizer(z, kappa)
                forward_fisher += kappa**2 * jac.T @ cov @ jac
                for j in range(3):
                    for e in range(6):
                        mixed[3 * b + j, e] = kappa * np.trace(
                            (1j * NG.PAULI[j]) @ coarse[b].conj().T @ dz_mat[e]
                        ).real / 2
            assert np.linalg.eigvalsh(forward_fisher)[-1] <= kappa**2 * size**2 + 2e-10
            assert np.linalg.norm(mixed, 2) <= kappa * size + 2e-10
    print("PASS: 90 joint SU(2) score-tensor and reverse-gradient incidence checks.")


if __name__ == "__main__":
    check_relative_joint_laws()
    check_gaussian_and_budget()
    check_compact_haar()
    check_joint_incidence()
    print("Finite identities and certificates only; no continuum or physical-gap claim.")
