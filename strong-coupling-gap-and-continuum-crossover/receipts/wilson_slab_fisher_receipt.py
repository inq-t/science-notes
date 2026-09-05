"""Read-only finite Z2 plaquette calibrations of the slab mechanism.

These enumerate finite path laws, covariance/influence and complete bridges.
The compact SU(2) gradient theorem is proved in the note, not by these samples.
"""
import itertools
import math
import numpy as np


def close(a, b, tol=3e-10):
    assert np.max(np.abs(np.asarray(a)-np.asarray(b))) < tol


def psd(a, tol=3e-10):
    assert np.linalg.eigvalsh((a+a.T)/2)[0] > -tol


def spin_states(n):
    # Coordinate i corresponds to binary bit i.
    idx = np.arange(2**n)
    return 2*((idx[:, None] >> np.arange(n)) & 1)-1


def slabs():
    count = 0
    rng = np.random.default_rng(3114)
    for x, beta in itertools.product([0.05, 0.15, 0.25], [0.01, 0.03]):
        q = 2*math.tanh(x)+6*math.tanh(beta)  # d_s=2 regular-lattice majorant
        assert q < 1
        for depth in [1, 2, 3]:
            states = spin_states(4*depth)
            history = states.reshape(-1, depth, 4)
            idx = np.arange(len(states))
            c = np.zeros((4*depth, 4*depth))
            for i in range(4*depth):
                for j in range(4*depth):
                    ti, ei = divmod(i, 4)
                    tj, ej = divmod(j, 4)
                    if ti == tj and ei != ej:
                        c[i, j] = math.tanh(beta)
                    if ei == ej and abs(ti-tj) == 1:
                        c[i, j] = math.tanh(x)
            resolvent = np.linalg.inv(np.eye(len(c))-c)
            for fixed in [np.ones(4), np.array([1, -1, 1, 1])]:
                logw = x*(history[:, 0]@fixed)
                if depth > 1:
                    logw += x*np.sum(history[:, :-1]*history[:, 1:], axis=(1, 2))
                    logw += beta*np.sum(np.prod(history[:, :-1], axis=2), axis=1)
                logw += beta*np.prod(history[:, -1], axis=1)/2
                law = np.exp(logw-logw.max())
                law /= law.sum()
                means = law@states
                cov = states.T@(law[:, None]*states)-np.outer(means, means)
                assert np.max(np.abs(cov)-resolvent) < 3e-10
                # Fisher response to the real external source u in exp(x*u.Y_1):
                # I(u)=x^2 Cov(Y_1), not a tangent derivative on discrete Z2.
                psd(np.eye(4)/(1-q)-cov[:4, :4])
                pplus = []
                for i in range(4*depth):
                    plus = idx | (1 << i)
                    minus = idx & ~(1 << i)
                    pplus.append(law[plus]/(law[plus]+law[minus]))
                for i in range(4*depth):
                    for j in range(4*depth):
                        actual = np.max(np.abs(pplus[i]-pplus[i][idx ^ (1 << j)]))
                        assert actual <= c[i, j]+2e-12
                # Nonlinear cylinder functions, with exact per-site oscillations.
                f = states[:, 0]*states[:, min(5, states.shape[1]-1)]
                g = np.tanh(states@rng.normal(size=states.shape[1]))
                df = np.array([np.max(np.abs(f-f[idx ^ (1 << i)])) for i in range(states.shape[1])])
                dg = np.array([np.max(np.abs(g-g[idx ^ (1 << i)])) for i in range(states.shape[1])])
                covariance = law@(f*g)-(law@f)*(law@g)
                assert abs(covariance) <= df@resolvent@dg/4+2e-12
                count += 1
    print(f"PASS {count} exact finite slabs: conditional TV, covariance resolvent and joint-score bounds")


def bridges():
    states = spin_states(4)
    parity = (np.prod(states, axis=1)+1)//2
    count = 0
    for x, beta in itertools.product([0.05, 0.15, 0.25], [0.01, 0.03]):
        k = np.exp(x*states@states.T)/(2*math.cosh(x))**4
        a = np.exp(beta*np.prod(states, axis=1)/2)
        t = a[:, None]*k*a[None, :]
        w, v = np.linalg.eigh(t)
        psi = v[:, -1]
        if psi.sum() < 0:
            psi = -psi
        assert psi.min() > 0 and w.min() > 0
        nu = psi**2
        p = t*psi[None, :]/(w[-1]*psi[:, None])
        close(nu@p, nu)
        endpoint = nu[:, None]*(p@p)
        joint_given_mid = p[:, :, None]*p[:, None, :]
        analysis = (np.sqrt(nu)[:, None, None]*joint_given_mid/np.sqrt(endpoint)[None, :, :]).reshape(16, 256).T
        s = analysis.T@analysis
        ph = np.sqrt(nu)[:, None]*p/np.sqrt(nu)[None, :]
        psd(s-ph@ph)
        psd(np.eye(16)-s)
        close(s@psi, psi)
        orbitlaw = np.bincount(parity, weights=nu, minlength=2)
        jmid = np.zeros((16, 2))
        jmid[np.arange(16), parity] = np.sqrt(nu/orbitlaw[parity])
        endpoint_parity = (2*parity[:, None]+parity[None, :]).reshape(-1)
        endflat = endpoint.reshape(-1)
        end_orbitlaw = np.bincount(endpoint_parity, weights=endflat, minlength=4)
        jend = np.zeros((256, 4))
        jend[np.arange(256), endpoint_parity] = np.sqrt(endflat/end_orbitlaw[endpoint_parity])
        abar = jend.T@analysis@jmid
        sbar = abar.T@abar
        pbar = jmid.T@ph@jmid
        psd(sbar-pbar@pbar)
        psd(jmid.T@s@jmid-sbar)
        raw_return = np.linalg.eigvalsh(s-np.outer(psi, psi))[-1]
        vbar = np.sqrt(orbitlaw)
        quotient_return = np.linalg.eigvalsh(sbar-np.outer(vbar, vbar))[-1]
        assert quotient_return <= raw_return+2e-12 < 1
        if x == 0.25 and beta == 0.03:
            assert np.ptp(psi) > 1e-3
            assert quotient_return > 1e-6
            assert np.linalg.norm(jmid.T@s@jmid-sbar) > 1e-6
            assert np.linalg.norm(sbar-pbar@pbar) > 1e-6
        count += 1
    print(f"PASS {count} complete interacting bridge and separate endpoint gauge-quotient matrices")


def su2_constants():
    count = 0
    for ds, x, beta in itertools.product([2, 3, 4], [0.01, 0.1, 0.2], [0.001, 0.005, 0.01]):
        q = 2*math.tanh(x)+6*(ds-1)*math.tanh(beta)
        assert q < 1
        d0 = 4*beta*(ds-1)+4*x
        lam = 3*math.exp(-d0)*(1-q)
        fisher = 2*x*x/(1-q)
        kappa = lam/(lam+fisher)
        close(kappa, 3*math.exp(-d0)*(1-q)**2/(3*math.exp(-d0)*(1-q)**2+2*x*x))
        assert 0 < kappa < 1
        rate = -math.log1p(-kappa)/2
        assert rate > 0 and abs(math.exp(-2*rate)-(1-kappa)) < 1e-12
        count += 1
    # The sufficient condition fails during temporal refinement even at beta=0.
    assert 2*math.tanh(10) > 1
    print(f"PASS {count} SU(2) certificate arithmetic cases and the temporal-refinement failure check")


if __name__ == "__main__":
    slabs()
    bridges()
    su2_constants()
    print("No compact-group discretization limit or four-dimensional continuum gap is certified.")
