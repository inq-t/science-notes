"""Finite checks for harmonic geometry and the exact Hardy defect.

The polynomial Hankel matrix implements the actual one-sided Hardy cut.
A separate negative control exposes the extra boundary from finite sections.
No files are written; no physical realization or infinite-limit gap is tested.
"""

from __future__ import annotations

import cmath
import math


def close(label, actual, expected, tol=1e-8):
    if abs(actual - expected) > tol:
        raise AssertionError(f"{label}: {actual!r} != {expected!r}")


def inner(f, g):
    return sum(z.conjugate() * g.get(n, 0j) for n, z in f.items())


def combine(f, g, scale):
    return {n: f.get(n, 0j) + scale * g.get(n, 0j)
            for n in f.keys() | g.keys()}


def conjugate_symbol(f):
    return {-n: z.conjugate() for n, z in f.items()}


def real_symbol(positive):
    f = dict(positive)
    f.update({-n: z.conjugate() for n, z in positive.items() if n > 0})
    return f


def j_operator(f):
    return {n: -1j * (1 if n > 0 else -1) * z
            for n, z in f.items() if n}


def phi(f):
    jf = j_operator(f)
    return {n: (z - 1j * jf.get(n, 0j)) / math.sqrt(2)
            for n, z in f.items() if n}


def harmonic_energy_integral(f, radius):
    # Integrate actual radial and angular derivatives, not a spectral sum.
    angles, radial_steps = 32, 400
    step = radius / radial_steps
    total = 0.0
    for j in range(radial_steps + 1):
        r = j * step
        angular_mean = 0.0
        for k in range(angles):
            theta = 2 * math.pi * k / angles
            dr, tangent = 0j, 0j
            for n, z in f.items():
                if not n:
                    continue
                common = z * r ** (abs(n) - 1) / radius ** abs(n)
                common *= cmath.exp(1j * n * theta)
                dr += abs(n) * common
                tangent += 1j * n * common
            angular_mean += (abs(dr) ** 2 + abs(tangent) ** 2) / angles
        weight = 1 if j in (0, radial_steps) else (4 if j % 2 else 2)
        total += weight * r * angular_mean
    return total * step / (3 * radius)


def hankel_trace(f):
    degree = max((n for n in f if n > 0), default=0)
    return sum(abs(f.get(k + n, 0j)) ** 2
               for k in range(1, degree + 1) for n in range(degree))


def convolution(f, g, index):
    return sum(z * g.get(index - n, 0j) for n, z in f.items())


def toeplitz_product(f, g, row, column, halo):
    return sum(f.get(j - row, 0j) * g.get(column - j, 0j)
               for j in range(halo))


def main():
    radius = 1.7
    f = real_symbol({1: 0.3 + 0.2j, 2: -0.1 + 0.4j, 3: 0.2 - 0.1j})
    g = real_symbol({1: -0.2 + 0.1j, 2: 0.3 - 0.2j, 3: 0.07j})
    jf, jg = j_operator(f), j_operator(g)
    for n, z in f.items():
        close("J squared", j_operator(jf)[n], -z)
        close("D equals minus JA",
              1j * n / radius * z, -abs(n) / radius * jf[n])
    close("real-to-complex Hermitian isometry",
          inner(phi(f), phi(g)), inner(f, g).real + 1j * inner(jf, g).real)
    for n, z in phi(f).items():
        close("complex linearity", phi(jf)[n], 1j * z)
    close("norm preservation", inner(phi(f), phi(f)), inner(f, f))
    print("PASS: real polar structure and Hardy isometry")

    s, depth = 0.31, 0.47
    radial_ratio = math.exp(-depth / radius)
    for n, z in f.items():
        close("harmonic depth parameter",
              radial_ratio ** abs(n) * z,
              math.exp(-depth * abs(n) / radius) * z)
        value = math.exp(-depth * abs(n) / radius) * cmath.exp(1j * n * s / radius) * z
        ds = 1j * n / radius * value
        dtau = -abs(n) / radius * value
        close("two-parameter relation", ds,
              -1j * (1 if n > 0 else -1) * dtau)
    print("PASS: logarithmic radial smoothing and tangential relation")

    energy = sum(abs(n) / radius * abs(z) ** 2 for n, z in f.items())
    trace = hankel_trace(f)
    close("bulk integration vs boundary form",
          harmonic_energy_integral(f, radius), energy)
    close("exact Hankel trace", trace,
          sum(n * abs(z) ** 2 for n, z in f.items() if n > 0))
    close("compression trace vs clock form", 2 * trace / radius, energy)
    psi = phi(f)
    close("clock state form", energy,
          sum(-n / radius * abs(z) ** 2 for n, z in psi.items() if n < 0))
    print("PASS: independently integrated bulk, compression and clock responses")

    degree = 3
    for row in range(degree + 2):
        for column in range(degree + 2):
            defect = convolution(f, f, column - row) - toeplitz_product(
                f, f, row, column, 2 * degree + 5)
            hankel_gram = sum(f.get(k + row, 0j).conjugate()
                             * f.get(k + column, 0j)
                             for k in range(1, degree + 1))
            close("full Hardy product defect", defect, hankel_gram)
    analytic = {-1: 1 + 0j}
    close("analytic symbol has no outgoing defect", hankel_trace(analytic), 0)
    close("two-sided complex-symbol response",
          (hankel_trace(analytic) + hankel_trace(conjugate_symbol(analytic))) / radius,
          1 / radius)
    print("PASS: product defect and real-symbol scope")

    cosine = {-1: 0.5 + 0j, 1: 0.5 + 0j}
    sine = {-1: 0.5j, 1: -0.5j}
    for row in range(5):
        for column in range(5):
            commutator = toeplitz_product(cosine, sine, row, column, 8)
            commutator -= toeplitz_product(sine, cosine, row, column, 8)
            close("cosine-sine corner commutator", commutator,
                  0.5j if row == column == 0 else 0j)
    # Smooth separated nonnegative bumps, integrated only away from the kernel pole.
    half_width, samples = 0.16, 120
    integral = 0.0
    step = 2 * half_width / samples
    for j in range(samples):
        theta = -half_width + (j + 0.5) * step
        a = math.exp(-1 / (1 - (theta / half_width) ** 2))
        for k in range(samples):
            offset = -half_width + (k + 0.5) * step
            phi_angle = math.pi / 2 + offset
            b = math.exp(-1 / (1 - (offset / half_width) ** 2))
            integral += a * b / math.tan((theta - phi_angle) / 2)
    integral *= (step / (2 * math.pi)) ** 2
    if integral >= -1e-5:
        raise AssertionError("Separated-support Hardy commutator did not have strict sign")
    print("PASS: exact corner and separated-support noncommutation")

    section_size = 12
    finite_trace = sum(
        convolution(f, f, 0) - toeplitz_product(f, f, n, n, section_size)
        for n in range(section_size)
    )
    close("second boundary in finite-section trace", finite_trace, 2 * trace)
    multiplier = 5
    covered = {multiplier * n: z for n, z in f.items()}
    close("cover changes unnormalized trace", hankel_trace(covered), multiplier * trace)
    close("cover preserves old clock response",
          2 * hankel_trace(covered) / (multiplier * radius), energy)
    print("PASS: cutoff-boundary and period-cover negative controls")

    def kappa(symbol):
        return {n: math.sqrt(n) * symbol.get(-n, 0j)
                for n in range(1, max(abs(k) for k in symbol) + 1)}

    kf, kg = kappa(f), kappa(g)
    sigma = 2 * inner(kf, kg).imag
    derivative_pair = sum(f.get(-n, 0j) * 1j * n * z
                          for n, z in g.items())
    close("central form vs local derivative", sigma, derivative_pair)
    central_trace = sum(
        toeplitz_product(f, g, n, n, 2 * degree + 5)
        - toeplitz_product(g, f, n, n, 2 * degree + 5)
        for n in range(degree + 2)
    )
    close("traced commutator", central_trace, 1j * sigma)
    close("response becomes one-particle norm", inner(kf, kf).real, trace)
    coherent_energy = sum(n / radius * abs(z) ** 2 for n, z in kf.items())
    close("extra generator in coherent energy", coherent_energy,
          sum(n * n / radius * abs(z) ** 2
              for n, z in f.items() if n > 0))
    # Coherent-vector kernels avoid a finite Fock cutoff, which cannot obey exact CCR.
    v = {1: 0.17 + 0.09j, 2: -0.21j, 3: 0.13}

    def displacement_coefficient(u, w):
        return cmath.exp(-inner(u, u).real / 2 - inner(u, w))

    left = displacement_coefficient(kg, v)
    left *= displacement_coefficient(kf, combine(v, kg, 1))
    right = cmath.exp(-0.5j * sigma)
    right *= displacement_coefficient(combine(kf, kg, 1), v)
    close("Weyl composition on coherent vectors", left, right)
    shifted_f = {n: cmath.exp(1j * n * s / radius) * z for n, z in f.items()}
    for n, z in kappa(shifted_f).items():
        close("inherited Weyl clock", z, cmath.exp(-1j * n * s / radius) * kf[n])
    normalized_cover = {n: z / math.sqrt(multiplier) for n, z in covered.items()}
    close("response-normalized source cover",
          hankel_trace(normalized_cover), trace)
    print("PASS: central derivative form, coherent Weyl law and inherited clock")
    print("Scope: finite harmonic and compression identities; no four-dimensional QFT certified")


if __name__ == "__main__":
    main()
