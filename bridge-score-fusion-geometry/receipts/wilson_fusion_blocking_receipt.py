"""Read-only Wilson fusion, blocking and kernel-normalization checks.

All Bessel evaluations use positive power series in logarithms. Exact rational
arithmetic certifies the displayed factorial bounds. Finite samples do not
prove the Hartman--Watson representation or an interacting continuum gap.
"""
import importlib.util
from functools import lru_cache
from fractions import Fraction as F
import math
from pathlib import Path
import sys
sys.dont_write_bytecode = True
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "old_wilson", ROOT / "contemporary-puzzles/yang-mills-mass-gap/receipts/wilson_bounded_solder_receipt.py")
OLD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(OLD)


def logadd(a, b):
    high, low = max(a, b), min(a, b)
    return high+math.log1p(math.exp(low-high))


@lru_cache(maxsize=None)
def log_i(order, x):
    """Positive Bessel series, with a relative tail stopping test."""
    assert order >= 0 and x > 0
    term = order*math.log(x/2)-math.lgamma(order+1)
    total = term
    for k in range(1, 200000):
        term += 2*math.log(x/2)-math.log(k)-math.log(k+order)
        total = logadd(total, term)
        next_ratio = (x/2)**2/((k+1)*(k+1+order))
        if next_ratio < 1:
            log_tail = term+math.log(next_ratio)-math.log1p(-next_ratio)
            if log_tail-total < math.log(2e-16):
                return total
    raise AssertionError("Bessel series failed to converge")


def cost(label, x):
    if label == 0:
        return 0.0
    return log_i(1, x)-log_i(label+1, x)


def log_z(x):
    return 0.0 if x == 0 else math.log(2/x)+log_i(1, x)


def bessel_and_fusion():
    for x in [0.2, 1.0, 4.0, 20.0]:
        for order in range(25):
            assert abs(log_i(order, x)-math.log(OLD.bessel_i(order, x))) < 2e-12
    count = 0
    for x in [0.05, 0.2, 1., 4., 20., 100., 1000.]:
        weights = [cost(l, x) for l in range(61)]
        assert all(math.isfinite(w) for w in weights)
        assert all(a < b for a, b in zip(weights, weights[1:]))
        for m in range(31):
            for l in range(31):
                for r in range(abs(m-l), m+l+1, 2):
                    assert weights[r] <= 2*(weights[m]+weights[l])+3e-10
                    count += 1
        s_values = np.array([0., 0.1, 0.7, 2., 5., 12., 30., 80., 200.])
        f_values = np.array([log_i(1, x)-log_i(math.sqrt(1+s), x) for s in s_values])
        slopes = np.diff(f_values)/np.diff(s_values)
        assert min(slopes) > 0
        assert max(np.diff(slopes)) < 2e-9
    sharp = cost(40, 10000.)/(2*cost(20, 10000.))
    assert abs(sharp-42/22) < 2e-4
    print(f"PASS 100 independent Bessel checks, {count} fusion channels and 7 concavity grids")
    print(f"PASS sharp-constant calibration: ratio={sharp:.9f}, limit={42/22:.9f}")


def rational_certificate():
    fourth_tail = F(1, 4)/(1-F(1, 36))
    eighth_tail = F(1, 64)/(1-F(1, 2916))
    assert fourth_tail == F(9, 35)
    assert eighth_tail == F(729, 46640) and eighth_tail < F(1, 60)
    assert F(26, 35)**2/F(61, 60) > F(1, 2)
    theta = F(1, 2)*F(2, 3)/(F(2, 3)+F(2, 59))
    assert theta == F(59, 124)
    print("PASS exact factorial tails, epsilon=1/2 and theta=59/124")


def character(label, theta):
    # The endpoints are handled by their continuous values.
    answer = np.zeros_like(theta)
    for m in range(-label, label+1, 2):
        answer += np.cos(m*theta)
    return answer


def kernel_from_coefficients(coefficients, theta):
    return sum((l+1)*value*character(l, theta) for l, value in enumerate(coefficients))


def quaternion_convolution():
    # Parametrize S^3 by v0=a and one uniformly distributed coordinate z on S^2.
    t = np.arange(1, 193)*math.pi/193
    a = np.cos(t)
    wa = 2/193*np.sin(t)**2
    z, wz = np.polynomial.legendre.leggauss(100)
    wz = wz/2
    count = 0
    for x in [0.1, 1., 4., 12.]:
        for q0 in [-1., -0.7, 0., 0.4, 1.]:
            qdotv = q0*a[:, None]+math.sqrt(max(0., 1-q0*q0))*np.sin(t)[:, None]*z
            exponent = x*(a[:, None]+qdotv)-2*log_z(x)
            integral = np.sum(wa[:, None]*wz[None, :]*np.exp(exponent))
            exact = math.exp(log_z(x*math.sqrt(2+2*q0))-2*log_z(x))
            assert abs(integral/exact-1) < 2e-11
            count += 1
    print(f"PASS {count} independent S^3 quaternion-convolution quadratures")


def temporal_blocking():
    grid = np.linspace(0., math.pi, 601)
    theta_star = 59/124
    inequalities = 0
    for x in [1., 2.5, 10., 50., 200., 1000.]:
        n = math.ceil(4*x)
        logs = np.array([-n*cost(l, x) for l in range(41)])
        for l in range(1, 41):
            assert logs[l] <= -(n/x)*math.lgamma(l+2)+3e-9
            inequalities += 1
        coefficients = np.exp(logs)
        hn = kernel_from_coefficients(coefficients, grid)
        h2n = kernel_from_coefficients(coefficients**2, grid)
        assert hn.min() > 26/35 and hn.max() < 44/35
        assert h2n.min() > 59/60 and h2n.max() < 61/60
        # The global bounds are analytic; this samples the finite series only.
        # Fusion numerator: enumerate a+b=l+2*r, a-b=m; keep r=0..29.
        extended = np.array([-n*cost(l, x) for l in range(70)])
        for l in range(1, 11):
            terms = []
            for r in range(30):
                for delta in range(-l, l+1, 2):
                    a = (l+2*r+delta)//2
                    b = (l+2*r-delta)//2
                    terms.append(math.log((a+1)*(b+1)/(l+1))
                                 +2*extended[a]+2*extended[b])
            peak = max(terms)
            log_numerator = peak+math.log(math.fsum(math.exp(v-peak) for v in terms))
            log_bound = min(-math.log(2), log_numerator-math.log(59/60))
            assert math.isfinite(log_numerator)
            assert log_bound <= theta_star*logs[l]+2e-8
    errors = []
    heat = kernel_from_coefficients(
        np.exp(-np.arange(41)*(np.arange(41)+2)/2), grid)
    for x in [20., 80., 320., 1280.]:
        n = int(x)  # n/x=1: limiting heat time is 2.
        hn = kernel_from_coefficients(np.exp([-n*cost(l, x) for l in range(41)]), grid)
        errors.append(float(np.max(np.abs(hn-heat))))
    assert all(a > b > 0 for a, b in zip(errors, errors[1:]))
    assert errors[-1] < 0.002
    print(f"PASS {inequalities} all-order-bound samples and 60 log-domain bridge numerator checks")
    print("PASS sampled uniform-kernel convergence:", ", ".join(f"{e:.6g}" for e in errors))


if __name__ == "__main__":
    bessel_and_fusion()
    rational_certificate()
    quaternion_convolution()
    temporal_blocking()
    print("No interacting vacuum, SU(3) extension or four-dimensional continuum gap is certified.")
