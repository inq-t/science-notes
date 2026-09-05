"""Read-only finite checks for local Perron and transition-score identities.

The smooth checks use an exactly specified finite quadrature model on a circle
product, not a continuum eigenfunction approximation certificate. Spin-mixture
checks calibrate why conditional regularity alone does not prove a global gap.
"""
import itertools
import math
import numpy as np


def close(a, b, tol=2e-10):
    assert np.max(np.abs(np.asarray(a)-np.asarray(b))) < tol


def psd(a, tol=3e-10):
    assert np.linalg.eigvalsh((a+a.T)/2)[0] > -tol


def finite_perron():
    count = 0
    for size in [5, 7, 9]:
        angles = 2*math.pi*np.arange(size)/size
        states = np.array(list(itertools.product(angles, repeat=2)))
        labels = np.array(list(itertools.product(range(size), repeat=2)))
        x = np.array([0.7, 1.3])
        one = []
        for coupling in x:
            raw = np.exp(coupling*np.cos(angles[:, None]-angles[None, :]))
            one.append(raw/raw.sum(axis=1, keepdims=True))
        kinetic = np.kron(*one)
        for beta in [0.1, 0.7, 1.5]:
            def loga(u):
                return -beta*(1-math.cos(u[0]-u[1]))/2

            a = np.exp([loga(u) for u in states])
            transfer = a[:, None]*kinetic*a[None, :]
            vals, vecs = np.linalg.eigh(transfer)
            eigenvalue = vals[-1]
            psi = vecs[:, -1]
            if psi.sum() < 0:
                psi = -psi
            assert psi.min() > 0
            nu = psi**2
            doob = transfer*psi[None, :]/(eigenvalue*psi[:, None])
            close(doob.sum(axis=1), 1)
            close(nu[:, None]*doob, nu[None, :]*doob.T)
            posterior = kinetic*a[None, :]*psi[None, :]
            posterior /= posterior.sum(axis=1, keepdims=True)
            close(posterior, doob)
            for direction in range(2):
                other = 1-direction
                log_ratio = math.log(one[direction].max()/one[direction].min())
                for exterior in range(size):
                    idx = np.flatnonzero(labels[:, other] == exterior)
                    conditional = nu[idx]/nu[idx].sum()
                    osc_v = float(np.ptp(-2*np.log(a[idx])))
                    d_bound = osc_v+2*log_ratio
                    assert np.ptp(np.log(conditional)) <= d_bound+2e-12
                    for i in idx:
                        for j in idx:
                            ratios = kinetic[i]/kinetic[j]
                            assert psi[i]/psi[j] <= a[i]/a[j]*ratios.max()+2e-10
                    # Discrete-cycle Poincare analogue of the density comparison.
                    gradient = np.roll(np.eye(size), -1, axis=1)-np.eye(size)
                    energy = gradient.T@np.diag(conditional)@gradient
                    variance = np.diag(conditional)-np.outer(conditional, conditional)
                    haar_gap = 4*math.sin(math.pi/size)**2
                    psd(energy-math.exp(-d_bound)*haar_gap*variance)

            def extended_logpsi(u):
                # The fixed positive quadrature weights define the exact extension.
                terms = np.exp(np.cos(u-states)@x)*a*psi
                return loga(u)+math.log(terms.sum())

            for u in states[::max(1, len(states)//7)]:
                terms = np.exp(np.cos(u-states)@x)*a*psi
                eta = terms/terms.sum()
                scores = -np.sin(u-states)*x
                means = eta@scores
                covariance = (scores-means).T@(eta[:, None]*(scores-means))
                grad_a = np.array([-1., 1.])*beta*math.sin(u[0]-u[1])/2
                gradient = grad_a+means
                mixed = beta*math.cos(u[0]-u[1])/2+covariance[0, 1]
                h = 2e-4
                e0, e1 = np.array([h, 0]), np.array([0, h])
                grad_fd = np.array([
                    (extended_logpsi(u+e)-extended_logpsi(u-e))/(2*h)
                    for e in [e0, e1]])
                mixed_fd = (
                    extended_logpsi(u+e0+e1)-extended_logpsi(u+e0-e1)
                    -extended_logpsi(u-e0+e1)+extended_logpsi(u-e0-e1))/(4*h*h)
                close(gradient, grad_fd, 2e-7)
                close(mixed, mixed_fd, 2e-7)
                # Normalized posterior score removes the mean, not the raw score.
                def posterior_at(v):
                    q = np.exp(np.cos(v-states)@x)*a*psi
                    return q/q.sum()
                score_fd = (np.log(posterior_at(u+e0))-np.log(posterior_at(u-e0)))/(2*h)
                close(score_fd, scores[:, 0]-means[0], 2e-7)
                count += 1
    print(f"PASS 9 actual finite Perron vacua, local ratios and conditional form comparisons")
    print(f"PASS {count} normalized-score, gradient and cross-Fisher derivative checks")


def slow_mixture():
    checks = 0
    for m in [0.4, 0.6, 0.8]:
        for n in [3, 5, 7, 9]:
            states = np.array(list(itertools.product([-1, 1], repeat=n)))
            nu = (np.prod((1+m*states)/2, axis=1)
                  +np.prod((1-m*states)/2, axis=1))/2
            f = np.sign(states.sum(axis=1))
            close(nu.sum(), 1)
            close(nu@f, 0)
            close(nu@(f*f), 1)
            energy = 0.0
            for i in range(n):
                others = [j for j in range(n) if j != i]
                for values in itertools.product([-1, 1], repeat=n-1):
                    idx = np.all(states[:, others] == values, axis=1)
                    conditional = nu[idx]/nu[idx].sum()
                    assert conditional.min() >= (1-m)/2-2e-14
                    assert conditional.max() <= (1+m)/2+2e-14
                    energy += nu[idx].sum()*(conditional@(f[idx]**2)-(conditional@f[idx])**2)
            k = (n-1)//2
            exact = n*math.comb(2*k, k)*((1-m*m)/4)**k
            close(energy, exact)
            assert exact <= n*(1-m*m)**k+2e-14
            checks += 1
    m, n = 0.6, 151
    log_bound = math.log(n)+(n-1)/2*math.log1p(-m*m)
    assert log_bound < -28
    print(f"PASS {checks} enumerated slow-mixture laws and positive uniform conditional bounds")
    print(f"PASS analytic collective upper-bound illustration at N=151: log bound={log_bound:.6f}")


if __name__ == "__main__":
    finite_perron()
    slow_mixture()
    print("No continuum vacuum, global influence bound or physical mass gap is certified.")
