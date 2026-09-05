"""Read-only finite checks of the boundary-action recursion.

Circle quadratures are exactly specified finite models, not convergence
certificates for continuum gauge theory. Gaussian checks use explicit matrices.
"""
import itertools
import math
import numpy as np


def close(a, b, tol=2e-9):
    assert np.max(np.abs(np.asarray(a)-np.asarray(b))) < tol


def sqrtm(a):
    w, v = np.linalg.eigh(a)
    assert w.min() > 0
    return (v*np.sqrt(w))@v.T


def posterior(t, v):
    p = t*np.exp(-v/2)[None, :]
    return p/p.sum(axis=1, keepdims=True)


def action(t, v):
    return -2*np.log(t@np.exp(-v/2))


def finite_actions():
    rng = np.random.default_rng(114)
    count = 0
    for size in [4, 6]:
        angles = 2*math.pi*np.arange(size)/size
        states = np.array(list(itertools.product(angles, repeat=2)))
        for x in [0.1, 0.4, 0.8]:
            raw = np.exp(x*np.cos(angles[:, None]-angles[None, :]))
            one = raw/raw.sum(axis=1, keepdims=True)
            kinetic = np.kron(one, one)
            beta = 0.3
            vsp = beta*(1-np.cos(states[:, 0]-states[:, 1]))
            a = np.exp(-vsp/2)
            t = a[:, None]*kinetic*a[None, :]
            w, u = np.linalg.eigh(t)
            psi = u[:, -1]
            if psi.sum() < 0:
                psi = -psi
            assert psi.min() > 0 and w.min() > 0
            nu = psi**2
            vstar = -2*np.log(psi)
            p = t*psi[None, :]/(w[-1]*psi[:, None])
            close(p, posterior(t, vstar))
            close(nu@p, nu)
            close(action(t, vstar)-vstar, -2*np.log(w[-1]))
            logt = np.log(t)
            diameter = max(np.ptp(row-other) for row in logt for other in logt)
            close(diameter, 8*x)
            for _ in range(3):
                v = rng.normal(0, 0.3, len(states))
                h = rng.normal(size=len(states))
                z = rng.normal(size=len(states))
                eta = posterior(t, v)
                eps = 1e-5
                first = (action(t, v+eps*h)-action(t, v-eps*h))/(2*eps)
                close(first, eta@h, 2e-8)
                eps = 3e-4
                mixed = (action(t, v+eps*(h+z))-action(t, v+eps*(h-z))
                         -action(t, v+eps*(-h+z))+action(t, v-eps*(h+z)))/(4*eps**2)
                cov = eta@(h*z)-(eta@h)*(eta@z)
                close(mixed, -cov/2, 2e-6)
                rho = eta*np.exp(-h/2)[None, :]
                rho /= rho.sum(axis=1, keepdims=True)
                kl = np.sum(rho*np.log(rho/eta), axis=1)
                close(action(t, v+h)-action(t, v), rho@h+2*kl)
                assert np.ptp(action(t, v+h)-action(t, v)) <= math.tanh(diameter/4)*np.ptp(h)+1e-12
                centered = h-nu@h
                close(nu@(p@centered), 0)
                count += 1
            f = np.ones(len(states))
            errors = []
            for n in range(31):
                if n in [0, 5, 15, 30]:
                    errors.append(np.max(np.abs(posterior(t, -2*np.log(f))-p)))
                f = t@f
                f /= np.linalg.norm(f)
            assert errors[-1] < 2e-10 and errors[-1] < errors[0]
    print(f"PASS {count} action-derivative, entropy and projective cases; six finite Perron limits")


def gaussian():
    rng = np.random.default_rng(2114)
    count = 0
    for dim in [1, 2, 4]:
        for scale in [0.1, 0.7, 2.0]:
            b0 = rng.normal(size=(dim, dim))
            b = np.eye(dim)+b0@b0.T
            a0 = rng.normal(size=(dim, dim))
            a = scale*np.eye(dim)+a0@a0.T
            bs = sqrtm(b)
            bis = np.linalg.inv(bs)
            abar = bis@a@bis
            rstar = bs@sqrtm(abar@abar+4*abar)@bs
            def step(r):
                d = b+(a+r)/2
                return a+2*b-2*b@np.linalg.solve(d, b)
            close(step(rstar), rstar)
            r = np.zeros_like(a)
            for _ in range(1000):
                r = step(r)
            close(r, rstar, 1e-8)
            d = b+(a+rstar)/2
            h0 = rng.normal(size=(dim, dim))
            h = (h0+h0.T)/2
            eps = 1e-5
            close((step(rstar+eps*h)-step(rstar-eps*h))/(2*eps),
                  b@np.linalg.solve(d, h)@np.linalg.solve(d, b), 2e-8)
            mean = np.linalg.solve(d, b)
            stationary = np.linalg.inv(rstar)
            close(stationary, mean@stationary@mean.T+np.linalg.inv(d))
            vals = np.linalg.eigvalsh(abar)
            gs = 2/(2+vals+np.sqrt(vals**2+4*vals))
            close(np.sort(np.linalg.eigvals(mean).real), np.sort(gs))
            assert max(gs)**2 < max(gs) < 1
            count += 1
    print(f"PASS {count} noncommuting Gaussian Riccati and full-versus-quadratic rate calibrations")


if __name__ == "__main__":
    finite_actions()
    gaussian()
    print("No uniform interacting continuum stability or mass prediction is certified.")
