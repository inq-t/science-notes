"""Smooth-circle and finite-symbol checks; no nonlinear continuum claim."""

import numpy as np


def derivative(values):
    n = len(values)
    modes = np.fft.fftfreq(n, 1 / n)
    return np.fft.ifft(1j * modes * np.fft.fft(values)).real


def velocities(a, b, y):
    density = 1 + a * np.cos(y) + b * np.sin(y)
    invmean = np.mean(1 / density)
    ca = np.mean(np.sin(y) / density) / invmean
    cb = -np.mean(np.cos(y) / density) / invmean
    va = (-np.sin(y) + ca) / density
    vb = (np.cos(y) + cb) / density
    return density, va, vb


def conditional_derivative_and_curvature():
    y = 2 * np.pi * np.arange(1024) / 1024
    for a, b in ((0, 0), (0.2, -0.3), (-0.4, 0.15), (0.55, 0.2)):
        density, va, vb = velocities(a, b, y)
        assert max(abs(derivative(density * va) + np.cos(y))) < 1e-10
        assert max(abs(derivative(density * vb) + np.sin(y))) < 1e-10
        assert abs(np.mean(va)) < 1e-12
        assert abs(np.mean(vb)) < 1e-12
        f = np.cos(y) + a * np.sin(2*y) + b * np.cos(3*y) + a*b
        fy = -np.sin(y) + 2*a*np.cos(2*y) - 3*b*np.sin(3*y)
        fa, fb = np.sin(2*y) + b, np.cos(3*y) + a
        da, db = fa + va*fy, fb + vb*fy
        mean_a = np.mean(density*fa + np.cos(y)*f)
        mean_b = np.mean(density*fb + np.sin(y)*f)
        assert abs(mean_a - np.mean(density*da)) < 1e-12
        assert abs(mean_b - np.mean(density*db)) < 1e-12
        # Centered conditional residual has zero expected horizontal derivative.
        dha, dhb = da - mean_a, db - mean_b
        assert abs(np.mean(density * dha)) < 1e-12
        assert abs(np.mean(density * dhb)) < 1e-12
        # Its horizontal cross form with any retained gradient vanishes.
        assert abs(np.mean(density * ((2*a + 1)*dha + (b - 2)*dhb))) < 1e-12
    step = 1e-5
    _, va, vb = velocities(0, 0, y)
    partial_a_vb = (velocities(step, 0, y)[2] - velocities(-step, 0, y)[2]) / (2*step)
    partial_b_va = (velocities(0, step, y)[1] - velocities(0, -step, y)[1]) / (2*step)
    curvature = partial_a_vb - partial_b_va + va*derivative(vb) - vb*derivative(va)
    assert max(abs(curvature - 1)) < 1e-8
    print("PASS: four conditional families, horizontal expectation/reduction identities, nonzero curvature.")


def rotating_circle():
    y = 2 * np.pi * np.arange(8192) / 8192
    previous = -1
    for concentration in (0, 0.5, 2, 8, 32, 128):
        normalizer = np.i0(concentration)
        density = np.exp(concentration*np.cos(y)) / normalizer
        velocity = 1 - np.exp(-concentration*np.cos(y)) / normalizer
        score = concentration*np.sin(y)
        assert abs(np.mean(density) - 1) < 1e-12
        assert abs(np.mean(velocity)) < 1e-12
        assert max(abs(derivative(density*velocity) + density*score)) < 1e-8
        assert max(abs(derivative(density) + density*score)) < 1e-8
        cost = np.mean(density*velocity**2)
        assert abs(cost - (1 - normalizer**-2)) < 1e-12
        circulation = 1 - velocity
        assert abs(np.mean(density*circulation**2) - normalizer**-2) < 1e-12
        assert abs(np.mean(density*circulation*velocity)) < 1e-12
        distortion = np.max(abs(velocity))
        assert abs(distortion - (np.exp(concentration)/normalizer - 1)) < 1e-12
        assert distortion >= previous
        previous = distortion
        print(f"PASS rotating circle K={concentration:g}: minimal cost={cost:.8g}, maximum speed={distortion:.8g}.")
    # A localized oscillatory packet approaches the local high-distortion symbol.
    concentration = 32
    density = np.exp(concentration*np.cos(y)) / np.i0(concentration)
    velocity = 1 - np.exp(-concentration*np.cos(y)) / np.i0(concentration)
    envelope = np.exp(-150 * (1 + np.cos(y)))
    wave = envelope * np.sin(300*y)
    dy = derivative(wave)
    quotient = np.mean(density*(1 + velocity**2)*dy**2) / np.mean(density*dy**2)
    assert quotient > 80
    print(f"PASS: rare-region derivative test has comparison ratio {quotient:.6g}; density does not erase distortion.")


def shear_checks():
    rng = np.random.default_rng(126)
    for hidden, retained in ((1, 1), (3, 2), (2, 5), (7, 4)):
        for scale in (0, 0.2, 1, 7):
            v = scale * rng.normal(size=(hidden, retained))
            bound = np.linalg.norm(v, 2)
            shear = np.eye(hidden + retained)
            shear[hidden:, :hidden] = v.T
            actual = np.linalg.eigvalsh(shear.T @ shear)[-1]
            expected = (2 + bound**2 + bound*np.sqrt(bound**2 + 4)) / 2
            assert abs(actual - expected) < 1e-9
    print("PASS: 16 full tangent-operator sharp shear constants.")


if __name__ == "__main__":
    conditional_derivative_and_curvature()
    rotating_circle()
    shear_checks()
    print("Scope: finite quadrature and symbol checks, not a uniform Wilson transport or physical gap proof.")
