"""Read-only checks for the vacuum-vector obstruction to Haar heat envelopes."""
import sys
sys.dont_write_bytecode = True

import math
import numpy as np


def rank_one_and_centering():
    rng = np.random.default_rng(112)
    for n in range(3, 10):
        for _ in range(5):
            # A common Haar constant vector, with an independently chosen vacuum.
            constant = np.ones(n)/math.sqrt(n)
            basis, _ = np.linalg.qr(np.column_stack([constant, rng.normal(size=(n, n-1))]))
            if np.dot(basis[:, 0], constant) < 0:
                basis[:, 0] *= -1
            rates = np.r_[0., rng.uniform(0.3, 2.0, n-1)]
            b = 0.7
            heat = (basis*np.exp(-b*rates))@basis.T
            psi = rng.uniform(0.3, 1.0, n)
            psi /= np.linalg.norm(psi)
            ray = np.outer(psi, psi)
            q = np.eye(n)-ray
            actual = ray+0.4*q
            assert np.linalg.eigvalsh(heat-actual).min() < -1e-8
            min_c = np.sum((basis.T@psi)**2*np.exp(b*rates))
            assert np.linalg.eigvalsh(min_c*heat-ray).min() > -1e-10
            assert np.linalg.eigvalsh((min_c-1e-5)*heat-ray).min() < -1e-9
            overlap = float(np.dot(constant, psi)**2)
            bound = 1-(1-math.exp(-b*rates[1:].min()))*overlap
            assert np.linalg.eigvalsh(q@heat@q).max() <= bound+1e-10
    print("PASS 35 finite rank-one prefactor, wrong-vacuum and centered-overlap checks")


def circle_checks():
    samples = 8192
    theta = np.arange(samples)*2*math.pi/samples
    for kappa in [0.3, 1.0, 2.0]:
        raw = np.exp(kappa*np.cos(theta))
        z = np.mean(raw*raw)
        psi = raw/math.sqrt(z)
        derivative = -kappa*np.sin(theta)*psi
        second = (-kappa*np.cos(theta)+kappa*kappa*np.sin(theta)**2)*psi
        potential = kappa*kappa*np.sin(theta)**2-kappa*np.cos(theta)
        assert np.max(np.abs(derivative+kappa*np.sin(theta)*psi)) < 1e-12
        assert np.max(np.abs(-second+potential*psi)) < 1e-12
        coeff = np.fft.fft(psi)/samples
        for n in range(9):
            series = sum((kappa/2)**(n+2*r) /
                         (math.factorial(n+r)*math.factorial(r)) for r in range(40))
            assert abs(coeff[n]-series/math.sqrt(z)) < 1e-12
        overlap = np.mean(psi)**2
        assert 0 < overlap < 1
        assert overlap**100 < overlap
        # These finite values illustrate the proved divergent lower bound.
        for b in [0.1, 0.4, 1.0]:
            log_bounds = [b*n*n + 2*n*math.log(kappa/2)
                          - 2*math.lgamma(n+1)-math.log(z)
                          for n in [300, 600, 1200]]
            assert log_bounds[2] > log_bounds[1] > log_bounds[0] > 0
    print("PASS 3 circle factorizations, 27 Fourier coefficients and overlap decay")
    print("PASS finite illustrations of the analytically proved heat-domain obstruction")


if __name__ == "__main__":
    rank_one_and_centering()
    circle_checks()
    print("The infinite no-go is a proof in the note, not inferred from these samples.")
