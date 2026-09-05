"""Finite checks of conditional Fisher response and frozen-boundary heat.

Checks algebraic identities, Gaussian formulas, a smooth non-Gaussian
conditional family, and Wilson incidence constants. It neither samples a
four-dimensional interacting vacuum nor proves a continuum spectral bound.
No files are written.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations, product
import math

import numpy as np


def close(label, actual, expected, atol=1e-10):
    error = float(np.max(np.abs(np.asarray(actual) - np.asarray(expected))))
    if error > atol:
        raise AssertionError(f"{label}: {error:.6g} > {atol}")


def score_projection():
    rng = np.random.default_rng(106)
    features = rng.normal(size=(9, 3))
    f = rng.normal(size=9) + 1j * rng.normal(size=9)

    def family(z):
        logits = features @ z
        weights = np.exp(logits - np.max(logits))
        return weights / weights.sum()

    for _ in range(12):
        z = rng.normal(size=3)
        probabilities = family(z)
        scores = features - probabilities @ features
        centered = f - probabilities @ f
        fisher = scores.T @ (probabilities[:, None] * scores)
        derivative = scores.T @ (probabilities * f)
        whitened_scores = np.sqrt(probabilities)[:, None] * scores
        projection = whitened_scores @ np.linalg.solve(fisher, whitened_scores.T)
        close("score projection idempotence", projection @ projection, projection)
        left = np.vdot(derivative, np.linalg.solve(fisher, derivative)).real
        right = np.sum(probabilities * np.abs(centered)**2)
        close("score projection identity", left,
              np.linalg.norm(projection @ (np.sqrt(probabilities) * centered))**2)
        if left > right + 1e-10:
            raise AssertionError("dimension-free Bessel bound failed")
        h = rng.normal(size=3)
        step = 1e-5
        numerical = ((family(z + step*h) @ f) - (family(z - step*h) @ f)) / (2*step)
        close("normalized conditional derivative", numerical, h @ derivative, 2e-8)
    print("PASS complex score projection and normalized conditional derivatives")


def gaussian_checks():
    depth = 0.7
    rows = []
    for kappa in (0.8, 0.2, 0.01, 0.0001):
        r = 1 - kappa + kappa * math.exp(-depth/kappa)
        response = kappa * (-math.expm1(-depth/kappa))
        close("first Hermite response", 1-r, response)
        fisher_gap = kappa/(1-kappa)
        close("sharp Fisher calibration", fisher_gap/(1+fisher_gap), kappa)
        hermite_responses = 1 - r**np.arange(1, 17)
        close("finite Hermite minimum", hermite_responses.min(), response)
        if not 0 < response <= kappa:
            raise AssertionError("conditional heat comparison failed")
        r_half = 1-kappa+kappa*math.exp(-depth/(2*kappa))
        if abs(r_half*r_half-r) < 1e-10:
            raise AssertionError("expected compression semigroup defect absent")
        infinitesimal_step = kappa*1e-5
        derivative = kappa*(-math.expm1(-infinitesimal_step/kappa))/infinitesimal_step
        close("compressed infinitesimal unit gap", derivative, 1, 6e-6)
        rows.append((kappa, 1/kappa, response))
    kappas = np.array([0.03, 0.2, 0.4, 0.8])
    product_fisher_gap = np.min(kappas/(1-kappas))
    close("product Fisher minimum", product_fisher_gap/(1+product_fisher_gap),
          kappas.min())
    print("PASS Gaussian sharpness, product minimum, and non-semigroup checks")
    print("GAUSSIAN kappa, conditional gap, finite response:", rows)


def circle_checks():
    # Smooth non-Gaussian conditional law exp(beta cos(y-z)), uniform z.
    # Periodic quadrature checks finitely many Fourier observables only.
    angles = 2*np.pi*np.arange(2048)/2048
    for beta in (0.1, 0.8, 3.0, 8.0):
        weights = np.exp(beta*(np.cos(angles)-1))
        probabilities = weights/weights.sum()
        mean_cos = probabilities @ np.cos(angles)
        fisher = beta**2*(probabilities @ np.sin(angles)**2)
        close("circle Fisher integration by parts", fisher, beta*mean_cos)
        bound = 1/(1+fisher)
        for mode in range(1, 9):
            coefficient = probabilities @ np.cos(mode*angles)
            residue = 1-coefficient**2
            if residue + 1e-10 < bound:
                raise AssertionError("circle Fisher floor failed")
    print("PASS non-Gaussian circle Fisher bound for eight Fourier modes")


def frozen_bit_checks():
    labels = (-1, 1)
    states = list(product(labels, repeat=2))  # boundary z, midpoint y
    for correlation in (0.3, 0.9, 0.999):
        probabilities = np.array([(1+correlation*z*y)/4 for z, y in states])
        jy = np.zeros((4, 2))
        jz = np.zeros((4, 2))
        for i, (z, y) in enumerate(states):
            jy[i, labels.index(y)] = np.sqrt(2*probabilities[i])
            jz[i, labels.index(z)] = np.sqrt(2*probabilities[i])
        close("midpoint isometry", jy.T @ jy, np.eye(2))
        close("boundary isometry", jz.T @ jz, np.eye(2))
        boundary_projection = jz @ jz.T
        generator = np.eye(4)-boundary_projection
        centered = np.array([-1.0, 1.0])/np.sqrt(2)
        midpoint_vector = jy @ centered
        boundary_vector = jz @ centered
        bridge = float(midpoint_vector @ generator @ midpoint_vector)
        close("bit bridge", bridge, 1-correlation**2)
        response = (1-math.exp(-0.7))*bridge
        if not 0 < response <= bridge:
            raise AssertionError("bit conditional heat comparison failed")
        zero_cost_lift = boundary_vector/correlation
        close("hidden extension projects to midpoint",
              midpoint_vector @ zero_cost_lift, 1)
        close("hidden extension has zero cost", generator @ zero_cost_lift, 0)
    print("PASS frozen-bit heat and zero-short/positive-compression witness")


def wilson_incidence_checks():
    # Periodic lattice sizes >=3: no elementary plaquette repeats an edge.
    for dimension, side in ((2, 3), (3, 3), (4, 3), (4, 4)):
        sites = list(product(range(side), repeat=dimension))
        index = {(x, axis): i for i, (x, axis) in enumerate(
            (x, axis) for x in sites for axis in range(dimension))}
        pair_counts = defaultdict(int)

        def shift(x, axis):
            y = list(x)
            y[axis] = (y[axis]+1) % side
            return tuple(y)

        for x in sites:
            for a, b in combinations(range(dimension), 2):
                plaquette = (index[x, a], index[shift(x, a), b],
                             index[shift(x, b), a], index[x, b])
                if len(set(plaquette)) != 4:
                    raise AssertionError("repeated elementary edge")
                for e in plaquette:
                    for f in plaquette:
                        pair_counts[e, f] += 1
        row_sums = np.zeros(len(index), dtype=int)
        off_sums = np.zeros(len(index), dtype=int)
        for (e, f), count in pair_counts.items():
            row_sums[e] += count
            if e != f:
                off_sums[e] += count
        close("full incidence row sum", row_sums, 8*(dimension-1))
        close("mixed incidence row sum", off_sums, 6*(dimension-1))
        # Symmetry supplies the same column bound, independently of volume.
        if any(count != pair_counts[f, e] for (e, f), count in pair_counts.items()):
            raise AssertionError("incidence comparison not symmetric")
    print("PASS Wilson full/mixed incidence constants on four finite lattices")
    rank, beta, dimension, theta = 3, 0.03, 4, 0.7
    rho = rank**2/2-8*beta*(dimension-1)
    mixed = 6*beta*(dimension-1)
    weight_defect = mixed*math.expm1(theta)
    exponent = theta*rho/(rho+weight_defect)
    floors = []
    for distance in (0, 1, 3, 6):
        effective = mixed**2*(1/rho+1/weight_defect)*math.exp(-exponent*distance)
        best = min(mixed, effective)
        floors.append(rho**2/(rho**2+best**2))
    if not all(0 < value <= 1 for value in floors):
        raise AssertionError("invalid collar bound")
    if any(a > b for a, b in zip(floors, floors[1:])):
        raise AssertionError("collar bound not monotone")
    print("PASS collar-bound arithmetic (not a measured spectrum):", floors)


if __name__ == "__main__":
    score_projection()
    gaussian_checks()
    circle_checks()
    frozen_bit_checks()
    wilson_incidence_checks()
    print("SCOPE finite identities and incidence only; no continuum mass-gap claim")
