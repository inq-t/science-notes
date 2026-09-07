"""Stdlib, stdout-only checks for compact-lie-gauge-positive-realization.md.

Exact rational arithmetic checks the balanced oscillator coefficients,
paired adjoint frequencies, independent diagonal su(N) roots, and central
free-coordinate energy. Floating-point checks cover the dilation factors
and one-dimensional Gaussian normalization and moments.

The su(N) root tests use <X,Y> = -Tr(XY), B(X,Y) = 2N Tr(XY).
The separate SU(2) cross-product tests use b_g = 2, equivalently -2Tr
in the defining two-dimensional representation. These metrics differ.

No eigensolver, files, network, local imports, or Monte Carlo are used.
This is not a numerical proof of compact resolvent, vacuum uniqueness,
the centered gap, its value, or a continuum Yang--Mills statement.
"""

from fractions import Fraction as F
from itertools import combinations, product
import math


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def equal(actual, expected, label):
    require(actual == expected, f"{label}: {actual!r} != {expected!r}")


def close(actual, expected, label, tolerance=2e-12):
    require(math.isclose(actual, expected, rel_tol=tolerance,
                         abs_tol=tolerance),
            f"{label}: {actual!r} != {expected!r}")


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0])


def balanced_coefficients():
    profiles = ((F(1), F(1), F(1)),
                (F(3, 2), F(5, 3), F(-7, 4)),
                (F(2, 5), F(7), F(3, 2)))
    frequencies = (F(0), F(1, 3), F(1), F(3, 2), F(4))
    oscillator_cases = 0
    for d in range(2, 9):
        kinetic_counts = [0] * d
        pair_counts = {pair: 0 for pair in combinations(range(d), 2)}
        for i in range(d):
            for j in range(d):
                if j != i:
                    kinetic_counts[j] += 1
                    pair_counts[tuple(sorted((i, j)))] += 1
        equal(kinetic_counts, [d-1] * d, "kinetic multiplicities")
        require(all(value == 2 for value in pair_counts.values()),
                "pair multiplicities")
        for epsilon, volume, coupling in profiles:
            kinetic = epsilon**2 / (volume * (d-1))
            potential = volume * coupling**2 / 2
            equal((d-1)*kinetic, 2*(epsilon**2/(2*volume)),
                  "sum T_i kinetic coefficient = 2H")
            equal(2*potential, 2*(volume*coupling**2/2),
                  "sum T_i potential coefficient = 2H")
            for mu in frequencies:
                equal(kinetic * potential * mu**2,
                      epsilon**2 * coupling**2 * mu**2 / (2*(d-1)),
                      "one-coordinate ground coefficient squared")
                oscillator_cases += 1
            # All slopes are nonnegative: squared checks retain their sign.
            single_slope_squared = epsilon**2*coupling**2/(2*(d-1))
            fiber_slope_squared = (d-1)**2 * single_slope_squared
            equal(fiber_slope_squared,
                  epsilon**2*coupling**2*(d-1)/2, "CL10 coefficient")
            h_tau_squared = fiber_slope_squared/4
            equal(h_tau_squared, epsilon**2*coupling**2*(d-1)/8,
                  "CL11 tau coefficient")
            for killing_floor in (F(2), F(4), F(12)):
                equal(h_tau_squared*2*killing_floor,
                      epsilon**2*coupling**2*(d-1)*killing_floor/4,
                      "CL11 radial coefficient")
            require(h_tau_squared > 0, "positive coefficient already at d=2")
    equal(oscillator_cases, 105, "oscillator case count")
    print("PASS: d=2..8 balance; 105 exact oscillator coefficient cases.")


def paired_frequencies():
    values = (F(0), F(1, 3), F(1), F(5, 2))
    cases = 0
    equality_cases = 0
    for number_of_pairs in range(1, 5):
        for mu in product(values, repeat=number_of_pairs):
            tau = 2*sum(mu)
            minus_killing = 2*sum(value**2 for value in mu)
            surplus = tau**2 - 2*minus_killing
            equal(surplus, 8*sum(x*y for x, y in combinations(mu, 2)),
                  "paired-frequency surplus identity")
            require(surplus >= 0, "tau squared >= -2 Killing")
            if surplus == 0:
                equality_cases += 1
            cases += 1
    equal(cases, 340, "paired-frequency case count")
    equal(equality_cases, 34, "paired-frequency equality count")
    print(f"PASS: {cases} paired-frequency cases; "
          f"{equality_cases} sharp or zero equality cases.")


def diagonal_su_roots():
    cases = 0
    for n in range(2, 7):
        positive_roots = tuple(combinations(range(n), 2))
        equal((n-1) + 2*len(positive_roots), n*n-1,
              "Cartan plus real root-space dimension")
        for seed in product((-1, 0, 1), repeat=n-1):
            theta = tuple(F(value, n+1) for value in seed)
            theta += (-sum(theta),)
            equal(sum(theta), 0, "traceless diagonal")
            # On the real root plane (ij), ad has frequencies +/- i(theta_i-theta_j).
            root_frequencies = [abs(theta[i]-theta[j])
                                for i, j in positive_roots]
            metric_norm_squared = sum(value**2 for value in theta)
            minus_killing_from_roots = 2*sum(mu**2 for mu in root_frequencies)
            minus_killing_from_defining_trace = 2*n*metric_norm_squared
            equal(minus_killing_from_roots, minus_killing_from_defining_trace,
                  "independent su(N) root and defining-trace Killing forms")
            tau = 2*sum(root_frequencies)
            require(tau**2 >= 4*n*metric_norm_squared,
                    "su(N) bound with b_g=2N in the -Tr metric")
            cases += 1
    equal(cases, 363, "su(N) diagonal case count")
    print("PASS: 363 diagonal su(N) root cases, N=2..6; -Tr metric, b_g=2N.")


def su2_cross_product():
    vectors = list(product((-1, 0, 1), repeat=3))
    vectors += [(F(1, 3), F(2, 5), F(-7, 4)),
                (F(0), F(0), F(5, 2)), (F(-3, 7), F(4, 7), F(0))]
    for vector in vectors:
        x, y, z = vector
        ad = ((0, -z, y), (z, 0, -x), (-y, x, 0))
        squared = [[sum(ad[i][k]*ad[k][j] for k in range(3))
                    for j in range(3)] for i in range(3)]
        norm_squared = dot(vector, vector)
        for i in range(3):
            for j in range(3):
                equal(-squared[i][j],
                      (norm_squared if i == j else 0)-vector[i]*vector[j],
                      "cross-product transverse oscillator matrix")
        minus_killing = -sum(squared[i][i] for i in range(3))
        equal(minus_killing, 2*norm_squared, "cross-product b_g=2")
        # Eigenvalues of -ad^2 are |a|^2, |a|^2, 0 by the matrix identity.
        tau_squared = 4*norm_squared
        equal(tau_squared, 2*minus_killing, "SU(2) sharp paired bound")
        equal(F(3-1, 8)*tau_squared, norm_squared,
              "d=3, coupling=1: H >= epsilon sum |a_i|")
    # The same su(2) matrices have twice the norm squared under -2Tr versus -Tr.
    for theta in (F(1, 3), F(1), F(5, 2)):
        defining_norm_squared = 2*theta**2
        cross_norm_squared = 2*defining_norm_squared
        minus_killing = 8*theta**2
        equal(minus_killing, 4*defining_norm_squared, "su(2) -Tr normalization")
        equal(minus_killing, 2*cross_norm_squared, "su(2) -2Tr normalization")
        equal((4*theta)**2, 4*cross_norm_squared, "cross-product tau=2|a|")
    equal(len(vectors), 30, "SU(2) vector count")
    print("PASS: 30 SU(2) cross-product matrices; d=3 recovery and metric distinction.")


def dilation():
    profiles = ((1.0, 1.0, 1.0), (0.25, 2.0, -3.0),
                (1.7, 0.6, 2.3), (3.0, 5.0, -0.125))
    cases = 0
    for epsilon, volume, coupling in profiles:
        scale = (epsilon/(volume*abs(coupling)))**(1.0/3.0)
        factor = epsilon**(4.0/3.0)*abs(coupling)**(2.0/3.0)*volume**(-1.0/3.0)
        close(epsilon**2/(volume*scale**2), factor, "dilated kinetic coefficient")
        close(volume*coupling**2*scale**4, factor, "dilated quartic coefficient")
        for d in range(2, 9):
            for n in (3, 8, 15, 24, 35):
                dimension = n*d
                # The stated map sends an original state to its scaled-coordinate state.
                amplitude = scale**(dimension/2.0)
                close(amplitude**2 / scale**dimension, 1.0,
                      "unitary dilation Jacobian")
                cases += 1
    equal(cases, 140, "dilation case count")
    print("PASS: 140 carrier/parameter dilation cases; kinetic and quartic scales agree.")


def simpson(function, left, right, panels):
    require(panels > 0 and panels % 2 == 0, "even Simpson panel count")
    width = (right-left)/panels
    total = function(left) + function(right)
    for j in range(1, panels):
        total += (4 if j % 2 else 2)*function(left+j*width)
    return total*width/3.0


def central_free_factor():
    # phi_R(z)=(pi R^2)^(-m/4) exp(-|z|^2/(2R^2)).
    # Its squared density has each coordinate variance R^2/2. Thus
    # ||grad phi_R||^2=m/(2R^2), and kinetic excess=epsilon^2*m/(4 V R^2).
    density = lambda u: math.exp(-u*u)/math.sqrt(math.pi)
    close(simpson(density, -9.0, 9.0, 4096), 1.0, "unit Gaussian normalization")
    close(simpson(lambda u: u*u*density(u), -9.0, 9.0, 4096),
          0.5, "unit Gaussian coordinate variance")
    energy_cases = 0
    potential_cases = 0
    for d in range(2, 9):
        # Explicit z+su(2) bracket: the z-coordinate is absent from every cross product.
        semisimple = [tuple(F((i+1)*(j+2)-4, i+j+2) for j in range(3))
                      for i in range(d)]
        reference_potential = sum(dot(cross(a, b), cross(a, b))
                                  for a, b in combinations(semisimple, 2))/2
        for central_dimension in (1, 2, 3):
            m = central_dimension*d
            previous = None
            for radius in (F(1), F(2), F(4), F(8)):
                epsilon, volume = F(3, 2), F(5, 3)
                excess = epsilon**2*m/(4*volume*radius**2)
                equal(excess*radius**2, epsilon**2*m/(4*volume),
                      "exact central R^-2 kinetic excess")
                if previous is not None:
                    equal(excess, previous/4, "doubling width quarters excess")
                previous = excess
                energy_cases += 1
                coordinates = [(tuple(radius*F((i+1)*(j+1), j+2)
                                      for j in range(central_dimension)), a)
                               for i, a in enumerate(semisimple)]
                brackets = [(tuple(F(0) for _ in range(central_dimension)), cross(a, b))
                            for (_, a), (_, b) in combinations(coordinates, 2)]
                full_potential = sum(dot(z, z)+dot(a, a) for z, a in brackets)/2
                equal(full_potential, reference_potential,
                      "central displacement leaves the commutator potential unchanged")
                require(all(dot(z, z) == 0 for z, _ in brackets),
                        "commutator has no central component")
                potential_cases += 1
    equal(energy_cases, 84, "central packet case count")
    equal(potential_cases, 84, "central bracket case count")
    print("PASS: Gaussian normalization/moment; 84 exact R^-2 excess cases.")
    print("PASS: 84 reductive bracket cases; central displacement costs no potential.")


def main():
    balanced_coefficients()
    paired_frequencies()
    diagonal_su_roots()
    su2_cross_product()
    dilation()
    central_free_factor()
    print("All seven check groups passed. Stdlib only; stdout only; no files written.")
    print("Scope: coefficient, root, scaling and free-center checks; no spectral gap computed.")
    print("Compactness, vacuum uniqueness and a positive centered gap use the note's proofs.")
    print("No continuum, volume-uniform, physical-yardstick or group/dimension selection claim.")


if __name__ == "__main__":
    main()
