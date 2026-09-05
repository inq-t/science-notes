"""Read-only checks: exact heat bounds, fusion envelopes and gauge quotients.

Fraction arithmetic certifies the displayed SU(2) heat lower bounds. Finite
matrices test quotient identities. No interacting continuum gap is asserted.
"""
import sys
sys.dont_write_bytecode = True

from fractions import Fraction as F
import importlib.util
import itertools
import math
from pathlib import Path
import numpy as np

spec = importlib.util.spec_from_file_location(
    "two_boundary_receipt", Path(__file__).with_name("two_boundary_prediction_receipt.py"))
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
close = helper.close


def negative_exp_upper(x, degree=70):
    """Rational upper bound for e^-x from a positive Taylor lower sum."""
    if x < 0:
        raise ValueError("x must be nonnegative")
    term = total = F(1)
    for k in range(1, degree+1):
        term *= x/k
        total += term
    return 1/total


def certified_heat_bound(t):
    q_upper = F(9, 4)*negative_exp_upper(F(5, 4)*t)
    if q_upper >= 1:
        raise ValueError("Geometric tail certificate unavailable at this time")
    return 4*negative_exp_upper(F(3, 4)*t)/(1-q_upper)


def log_fusion_series(j_twice, time, stop=80):
    """Log of the positive truncated fusion sum, without high-spin underflow.

    This is a numerical check, not a certificate for the infinite series.
    The note separately proves its envelope and the rational heat bounds.
    """
    j = j_twice/2
    log_terms = []
    for n in range(stop):
        r = j+n+1
        for m_index in range(j_twice+1):
            m = -j+m_index
            log_terms.append(time-time*(r*r+m*m)
                             + math.log(r*r-m*m)-math.log(j_twice+1))
    peak = max(log_terms)
    return peak+math.log(math.fsum(math.exp(value-peak) for value in log_terms))


def heat_and_envelope():
    assert certified_heat_bound(F(3)) < F(9, 20)
    assert certified_heat_bound(F(6)) < F(1, 20)
    epsilon = F(121, 420)
    b_lower = F(3, 2)*epsilon/(epsilon+F(2, 19))
    assert b_lower == F(6897, 6278) and b_lower > 1
    u = -math.log1p(-float(epsilon))
    a = 21/19
    b = 1.5*u/(u+math.log(a))
    assert b > float(b_lower)
    direct_checks = 0
    for t in [3.0, 4.0, 6.0]:
        for j2 in range(1, 61):
            c = (j2/2)*(j2/2+1)
            log_numerator = log_fusion_series(j2, t)
            assert math.isfinite(log_numerator)
            log_upper = min(math.log1p(-float(epsilon)),
                            log_numerator-math.log(19/20))
            if log_upper > -c+1e-10:
                raise AssertionError("Fusion envelope calibration failed")
            direct = helper.fusion_series(j2, t)
            if direct > 1e-250:
                assert abs(log_numerator-math.log(direct)) < 1e-10
                direct_checks += 1
    assert direct_checks > 0
    print("PASS rational heat certificates T3<9/20, T6<1/20; b>=6897/6278>1")
    print("PASS 180 log-domain finite-spin checks (2j=1..60; 80 series terms)")
    print(f"PASS {direct_checks} log-sum agreements with non-underflow direct sums")


def permutations_s3():
    elements = list(itertools.permutations(range(3)))
    identity = (0, 1, 2)
    classes = []
    for g in elements:
        fixed = sum(g[i] == i for i in range(3))
        classes.append(0 if g == identity else 1 if fixed == 1 else 2)
    return elements, np.array(classes)


def pullback(probability, labels):
    groups = np.unique(labels)
    marg = np.array([probability[labels == g].sum() for g in groups])
    j = np.zeros((len(probability), len(groups)))
    for k, g in enumerate(groups):
        selected = labels == g
        j[selected, k] = np.sqrt(probability[selected]/marg[k])
    return j, marg


def quotient_check(p, labels):
    n = len(p)
    nu = np.full(n, 1/n)
    j0, pi = pullback(nu, labels)
    coarse_white = j0.T @ p @ j0
    coarse_p = coarse_white*np.sqrt(pi[None, :])/np.sqrt(pi[:, None])
    k, endpoints = helper.bridge(p, nu)
    kb, endpoints_b = helper.bridge(coarse_p, pi)
    endpoint_labels = (3*labels[:, None]+labels[None, :]).reshape(-1)
    je, marginal = pullback(endpoints, endpoint_labels)
    close(marginal, endpoints_b, "quotient endpoint marginal")
    close(kb, je.T @ k @ j0, "quotient bridge conditional expectation")
    loss = k@j0-je@(je.T@k@j0)
    raw_restriction = j0.T@k.T@k@j0
    close(raw_restriction-kb.T@kb, loss.T@loss, "exact quotient loss square")
    if np.linalg.eigvalsh(raw_restriction-kb.T@kb).min() < -1e-10:
        raise AssertionError("Quotient prediction order failed")
    if np.linalg.eigvalsh(kb.T@kb-coarse_white.T@coarse_white).min() < -1e-10:
        raise AssertionError("Physical one-boundary domination failed")
    return k, kb, pi, coarse_p, j0


def finite_group_quotients():
    elements, labels = permutations_s3()
    n = 6
    p = 0.5*np.eye(n)+np.full((n, n), 0.5/n)
    k, kb, pi, _, _ = quotient_check(p, labels)
    transpositions = np.flatnonzero(labels == 1)
    f = (labels == 1).astype(float)-0.5
    endpoints = helper.bridge(p, np.full(n, 1/n))[1]
    prediction = (k @ (f/math.sqrt(n)))/np.sqrt(endpoints)
    x, z = transpositions[:2]
    close(prediction[n*x+x], 4/9, "identical transpositions")
    close(prediction[n*x+z], 1/3, "distinct transpositions")

    # Generator by direct permutation composition, not the quoted class matrix.
    transition = np.zeros((n, n))
    lookup = {g: i for i, g in enumerate(elements)}
    for i, g in enumerate(elements):
        for tau_idx in transpositions:
            tau = elements[tau_idx]
            composed = tuple(tau[g[k]] for k in range(3))
            transition[i, lookup[composed]] += 1/3
    laplacian = np.eye(n)-transition
    eig, vec = np.linalg.eigh(laplacian)
    t = math.log(2)
    p = (vec*np.exp(-t*eig))@vec.T
    k, kb, pi, coarse_p, j0 = quotient_check(p, labels)
    density = coarse_p/pi[None, :]
    close(density, np.array([[13, 3, 1], [3, 5, 3], [1, 3, 7]])/4,
          "quotient density at log 2")
    close(coarse_p@coarse_p/pi[None, :],
          np.array([[33, 15, 9], [15, 17, 15], [9, 15, 21]])/16,
          "quotient density at twice log 2")
    signs = np.sqrt(pi)*np.array([1., -1., 1.])
    standard = np.sqrt(pi)*np.array([2., 0., -1.])
    s = kb.T@kb
    close(signs@s@standard, 5/693, "quotient noncommuting cross element")
    quotient_l = j0.T@laplacian@j0
    assert np.linalg.norm(s@quotient_l-quotient_l@s) > 1e-4

    # Check envelope and its product/quotient orders directly on this finite group.
    h = p*6
    h2 = (p@p)*6
    epsilon = min(0.5, h.min()**2/h2.max())
    u = -math.log1p(-epsilon)
    amplitude = np.sum(p[0]**2)*6/h2.min()
    b = (t/2)*u/(u+math.log(amplitude))
    heat = (vec*np.exp(-b*eig))@vec.T
    s_raw = k.T@k
    assert np.linalg.eigvalsh(heat-s_raw).min() > -1e-10
    assert np.linalg.eigvalsh(j0.T@heat@j0-s).min() > -1e-10
    prod_s, prod_h = np.array([[1.0]]), np.array([[1.0]])
    for _ in range(3):
        prod_s = np.kron(prod_s, s_raw)
        prod_h = np.kron(prod_h, heat)
        assert np.linalg.eigvalsh(prod_h-prod_s).min() > -2e-10
    print("PASS both S3 quotients, loss squares, one-boundary order and cross term 5/693")
    print("PASS finite-group unit-prefactor product and quotient orders through 3 factors")


if __name__ == "__main__":
    heat_and_envelope()
    finite_group_quotients()
    print("No interacting law or continuum gap is certified.")
