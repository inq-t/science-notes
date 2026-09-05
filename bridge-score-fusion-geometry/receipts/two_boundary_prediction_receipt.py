"""Read-only numerical checks of two-boundary multiplication and prediction.

Uses the actual endpoint law throughout. Finite checks calibrate the analytic
proofs; they do not prove interacting continuum uniformity or a Yang--Mills gap.
"""

import sys
sys.dont_write_bytecode = True

import itertools
import math
import numpy as np


def close(actual, expected, label, atol=2e-10, rtol=2e-9):
    if not np.allclose(actual, expected, atol=atol, rtol=rtol):
        error = float(np.max(np.abs(np.asarray(actual) - expected)))
        raise AssertionError(f"{label}: maximum error {error}")


def bridge(transition, probability):
    """Whitened L2(nu) -> L2(actual joint endpoints) prediction matrix."""
    joint = np.einsum("y,yx,yz->yxz", probability, transition, transition)
    endpoints = joint.sum(axis=0).reshape(-1)
    if np.min(endpoints) <= 0 or np.min(probability) <= 0:
        raise ValueError("This finite helper requires strictly positive marginals.")
    prediction = joint.reshape(len(probability), -1).T
    prediction /= np.sqrt(endpoints[:, None] * probability[None, :])
    return prediction, endpoints


def discard(probability, labels):
    labels = np.asarray(labels)
    columns = []
    for label in np.unique(labels):
        mask = labels == label
        col = np.zeros_like(probability)
        col[mask] = np.sqrt(probability[mask] / probability[mask].sum())
        columns.append(col)
    retained = np.stack(columns, axis=1)
    return np.eye(len(probability)) - retained @ retained.T


def finite_certificates():
    rng = np.random.default_rng(111)
    count = 0
    for n in range(3, 8):
        for _ in range(6):
            raw = rng.uniform(0.15, 1.0, (n, n))
            weights = raw @ raw.T + 0.4 * np.eye(n)
            row = weights.sum(axis=1)
            nu = row / row.sum()
            p = weights / row[:, None]
            sw = np.sqrt(nu)
            transfer = sw[:, None] * p / sw[None, :]
            lam, vectors = np.linalg.eigh(transfer)
            phi = vectors / sw[:, None]
            q = discard(nu, np.arange(n) % 2)
            k, endpoint = bridge(p, nu)
            close(k @ sw, np.sqrt(endpoint), "constant preservation")
            delta = np.linalg.norm(k @ q, 2) ** 2

            products = np.einsum("ia,jb->ijab", phi, phi).reshape(n*n, n*n)
            gram = products.T @ (endpoint[:, None] * products)
            c = np.einsum("i,ia,ib,ik->abk", nu, phi, phi, phi)
            gram_formula = np.einsum("ack,k,bdk->abcd", c, lam**2, c)
            close(gram, gram_formula.reshape(n*n, n*n), "multiplication Gram")
            pp = p @ phi
            columns = np.einsum("ia,ib->iab", pp, pp).reshape(n, n*n)
            f = q @ (sw[:, None] * columns)
            close(f, q @ k.T @ (np.sqrt(endpoint)[:, None] * products),
                  "product adjoint")
            eig, eigvec = np.linalg.eigh(gram)
            if eig.min() <= 1e-10:
                raise AssertionError("Unexpected degenerate positive endpoint Gram")
            inverse_half = (eigvec / np.sqrt(eig)) @ eigvec.T
            close(np.linalg.norm(f @ inverse_half, 2)**2, delta,
                  "complete generalized Gram certificate")

            density_two = (p @ p) / nu[None, :]
            m = density_two.min()
            row_square = np.max(np.sum(p*p / nu[None, :], axis=1))
            epsilon = np.linalg.norm(q @ transfer, "fro") ** 2
            if delta > 4 * row_square * epsilon / m + 1e-10:
                raise AssertionError("Sufficient algebra smoothing bound failed")

            observable = rng.normal(size=n)
            density_one = p / nu[None, :]
            insert_density = (density_one * (nu*observable)[None, :]) @ density_one
            norm_density = np.sum(
                nu[:, None] * nu[None, :] * insert_density**2 / density_two)
            target = np.linalg.norm(k @ (sw * observable)) ** 2
            close(norm_density, target, "weighted density insertion")
            insert_perron = (transfer * observable[None, :]) @ transfer
            norm_perron = np.sum(
                sw[:, None] * sw[None, :] * insert_perron**2 / (transfer @ transfer))
            close(norm_perron, target, "Perron weighted insertion")
            count += 1

    # Exact measurable sufficiency: a positive two-class chain with private fibers.
    nu = np.array([0.12, 0.18, 0.28, 0.42])
    labels = np.array([0, 0, 1, 1])
    coarse = np.array([[0.65, 0.35], [0.15, 0.85]])
    coarse_nu = np.array([0.3, 0.7])
    p = np.array([[coarse[labels[i], labels[j]] * nu[j] / coarse_nu[labels[j]]
                   for j in range(4)] for i in range(4)])
    q = discard(nu, labels)
    transfer = np.sqrt(nu[:, None]) * p / np.sqrt(nu[None, :])
    k, _ = bridge(p, nu)
    close(transfer @ q, 0, "exact one-ended sufficiency")
    close(k @ q, 0, "exact two-ended sufficient algebra")
    print(f"PASS {count} finite product/Gram/smoothing/Perron checks; exact algebra closure")


def parity_examples():
    states = np.array(list(itertools.product([-1.0, 1.0], repeat=2)))
    chars = np.column_stack([np.ones(4), states[:, 0], states[:, 1],
                             states[:, 0] * states[:, 1]])
    for a, b in [(0.25, 0.25), (0.1, 0.4), (0.3, 0.2)]:
        for c in [0.0, 0.0001, 0.02]:
            p = (chars * np.array([1.0, a, b, c])) @ chars.T / 4
            k, _ = bridge(p, np.full(4, 0.25))
            f = chars[:, 3] / 2
            expected = ((c+a*b)**2 / (1+a*a+b*b+c*c)
                        + (c-a*b)**2 / (1-a*a-b*b+c*c))
            close(np.linalg.norm(k @ f)**2, expected, "four-state parity")
            close(np.linalg.norm(p @ f)**2, c*c, "one-ended parity")
            if c == 0:
                close(expected, 2*a*a*b*b/(1-(a*a+b*b)**2), "zero mode formula")
    print("PASS 9 positive-entry four-state parity calibrations")


def bit_cubes_and_gaussian_degrees():
    for alpha in [0.2, 0.55, 0.85]:
        beta = 2 * alpha**2 / (1 + alpha**2)
        one = np.array([[1+alpha, 1-alpha], [1-alpha, 1+alpha]]) / 2
        for d in range(1, 7):
            p = np.array([[1.0]])
            for _ in range(d):
                p = np.kron(p, one)
            n = len(p)
            k, _ = bridge(p, np.full(n, 1/n))
            s = k.T @ k
            if np.linalg.eigvalsh(s-p@p).min() < -1e-10:
                raise AssertionError("Lower half-smoothing sandwich failed")
            if np.linalg.eigvalsh(p-s).min() < -1e-10:
                raise AssertionError("Upper half-smoothing sandwich failed")
            spectrum = np.linalg.eigvalsh(s)
            close(1-spectrum[-2], 1-beta, "dimension-free complete bridge floor")
            f = np.zeros(n)
            f[0], f[-1] = 1/math.sqrt(2), -1/math.sqrt(2)
            x = alpha**2
            expected_one = ((1+x)**d - (1-x)**d) / 2**d
            expected_two = ((1+beta)**d - (1-beta)**d) / 2**d
            close(np.linalg.norm(p@f)**2, expected_one, "merged-state one-end")
            close(np.linalg.norm(k@f)**2, expected_two, "merged-state two-end")
            q = discard(np.full(n, 1/n), [0] + list(range(1, n-1)) + [0])
            close(q, np.outer(f, f), "genuine deterministic discarded projection")

    for ell in [0.1, 0.8, 2.0]:
        omega = np.array([0.03, 0.7, 3.0])
        alpha = np.exp(-omega*ell)
        beta = 2*alpha**2/(1+alpha**2)
        for degree in itertools.product(range(5), repeat=3):
            degree = np.array(degree)
            s_eigenvalue = np.prod(beta**degree)
            p_eigenvalue = np.exp(-ell*np.dot(omega, degree))
            if not p_eigenvalue**2-1e-12 <= s_eigenvalue <= p_eigenvalue+1e-12:
                raise AssertionError("Gaussian multidegree sandwich failed")
    print("PASS 18 complete bit-cube bridges and 375 Gaussian multidegree checks")


def character(twice_spin, theta):
    return np.sin((twice_spin+1)*theta) / np.sin(theta)


def heat(time, theta, max_twice=90):
    result = np.zeros_like(theta)
    for twice in range(max_twice+1):
        j = twice / 2
        result += (twice+1) * math.exp(-time*j*(j+1)) * character(twice, theta)
    return result


def fusion_direct(j_twice, time, max_twice=60):
    total = 0.0
    for a2 in range(max_twice+1):
        for b2 in range(max_twice+1):
            if (abs(a2-b2) <= j_twice <= a2+b2
                    and (a2+b2+j_twice) % 2 == 0):
                a, b = a2/2, b2/2
                total += (a2+1)*(b2+1)*math.exp(-2*time*(a*(a+1)+b*(b+1)))
    return total/(j_twice+1)


def fusion_series(j_twice, time, start=0, stop=80):
    j = j_twice/2
    total = 0.0
    for n in range(start, stop):
        r = j+n+1
        inner = sum((r*r-m*m)*math.exp(-time*m*m)
                    for m in np.arange(-j, j+1, 1.0))
        total += math.exp(time-time*r*r) * inner / (j_twice+1)
    return total


def tail_bound(time, r):
    if r < 1/math.sqrt(time):
        raise ValueError("The decreasing-summand tail bound requires r >= t^-1/2")
    return math.exp(time) * (
        (r*r + r/(2*time))*math.exp(-time*r*r)
        + math.sqrt(math.pi)/(4*time**1.5)*math.erfc(math.sqrt(time)*r))


def compact_fusion():
    # Deterministic Gauss-Legendre quadrature of the SU(2) class Haar measure.
    nodes, weights = np.polynomial.legendre.leggauss(480)
    theta = (nodes+1)*math.pi/2
    measure = weights*np.sin(theta)**2
    close(measure.sum(), 1.0, "class Haar normalization")
    checks = 0
    for time in [0.3, 0.8, 1.7]:
        h = heat(2*time, theta)
        for j2 in range(17):
            exact_series = fusion_series(j2, time)
            direct = fusion_direct(j2, time)
            integral = np.sum(measure*h*h*character(j2, theta))/(j2+1)
            close(exact_series, direct, "fusion enumeration", atol=1e-12)
            close(exact_series, integral, "character convolution numerator",
                  atol=2e-11, rtol=2e-7)
            for start in [3, 6]:
                bound = tail_bound(time, j2/2+start+1)
                if fusion_series(j2, time, start=start) > bound*(1+1e-12):
                    raise AssertionError("Fusion-series remainder exceeds analytic bound")
            checks += 1
        close(fusion_series(0, time),
              sum((k+1)**2*math.exp(-4*time*(k/2)*(k/2+1)) for k in range(91)),
              "C0 heat diagonal")
        # Independent class quadrature of the finite low-spin product.
        fundamental = character(1, theta)
        coefficients = np.array([
            np.sum(measure*fundamental**2*character(k, theta)) for k in range(10)])
        expected_coefficients = np.zeros(10)
        expected_coefficients[[0, 2]] = 1.0
        close(coefficients, expected_coefficients, "fundamental product coefficients")
        second = sum(coefficients[k]**2*math.exp(-2*time*(k/2)*(k/2+1))
                     for k in range(10))
        mean = math.exp(-1.5*time)*np.sum(measure*fundamental**2)
        close(mean, math.exp(-1.5*time), "low-spin endpoint mean")
        close(second, 1+math.exp(-4*time), "low-spin endpoint second moment")
        variance = second-mean*mean
        lower = mean*mean/variance
        if not math.exp(-4*time) <= lower <= 1:
            raise AssertionError("Low-spin prediction lower bound inconsistent")
        cutoff = max(2.0, math.ceil(2*(1/math.sqrt(time)-1.5))/2)
        uniform = tail_bound(time, cutoff+1.5)
        for j2 in range(int(2*cutoff)+1, int(2*cutoff)+30):
            if fusion_series(j2, time) > uniform*(1+1e-12):
                raise AssertionError("Uniform high-spin tail failed")
    print(f"PASS {checks} compact fusion sums/quadratures; fusion-numerator tail bounds")


if __name__ == "__main__":
    finite_certificates()
    parity_examples()
    bit_cubes_and_gaussian_degrees()
    compact_fusion()
    print("All two-boundary prediction receipts pass. No continuum gap is asserted.")
