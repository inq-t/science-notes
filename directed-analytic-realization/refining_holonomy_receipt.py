"""Stdlib, stdout-only arithmetic checks for refining Pauli holonomy.

Shared assertions and elementary matrix helpers come from the adjacent
context_transport_receipt, whose main guard prevents its checks from running.
No third-party libraries, network, file writes or numerical eigensolvers.

Integer-complex Pauli/source identities are exact binary arithmetic. Matrix
exponentials, sampled Fourier bounds, asymptotic remainders and variance
probes are floating-point checks, not interval certificates or limit proofs.
The Bloch-torus edge need not be attained on a finite periodic momentum grid.
The connection is fixed background data; no source-free interacting vacuum,
physical quantization unit, local Gauss constraint or Lorentz symmetry follows.
"""

from itertools import combinations, product
import cmath
import math

from context_transport_receipt import (
    I2, PAULI, close, equal, inner, mm, mv, norm_squared, plus_spinor, require,
)


def scale(c, a):
    return tuple(tuple(c*x for x in row) for row in a)


def add(a, b):
    return tuple(tuple(x+y for x, y in zip(row, other)) for row, other in zip(a, b))


def subtract(a, b):
    return add(a, scale(-1, b))


def adjoint(a):
    return tuple(tuple(complex(a[j][i]).conjugate() for j in range(len(a)))
                 for i in range(len(a[0])))


def conjugate(a):
    return tuple(tuple(complex(x).conjugate() for x in row) for row in a)


def matrix_norm_squared(a):
    return sum(complex(x).real**2+complex(x).imag**2 for row in a for x in row)


def commutator(a, b):
    return subtract(mm(a, b), mm(b, a))


def matrix_close(a, b, label, tolerance=2e-10):
    for row, other in zip(a, b):
        for x, y in zip(row, other):
            close(x, y, label, tolerance)


def pauli_vector(vector):
    out = scale(0, I2)
    for coefficient, sigma in zip(vector, PAULI):
        out = add(out, scale(coefficient, sigma))
    return out


def transport(theta, j):
    return add(scale(math.cos(theta), I2), scale(1j*math.sin(theta), PAULI[j]))


def symbol(a, g, momentum):
    theta = a*g
    scalar = 2*(len(momentum)-math.cos(theta)*sum(math.cos(k) for k in momentum))/(a*a)
    vector = tuple(-2*math.sin(theta)*math.sin(k)/(a*a) for k in momentum)
    return add(scale(scalar, I2), pauli_vector(vector))


def continuum_symbol(g, p):
    return add(scale(sum(x*x for x in p)+len(p)*g*g, I2), pauli_vector(tuple(-2*g*x for x in p)))


def exact_bloch_edge(a, theta, d):
    # Rationalization avoids cancellation when theta is small.
    radius = math.sqrt(d*d*math.cos(theta)**2+d*math.sin(theta)**2)
    return 2*d*(d-1)*(math.sin(theta)/a)**2/(d+radius)


def direct_symbols():
    cases = 0
    for d, g, a in product((2, 3), (-0.7, 0.0, 1.0, 1.4), (0.1, 0.4, 0.9)):
        for seed in range(6):
            k = tuple((seed+1)*(j+1)*0.37-1.1 for j in range(d))
            direct = scale(0, I2)
            for j in range(d):
                u = transport(a*g, j)
                matrix_close(mm(adjoint(u), u), I2, "refining transport is unitary")
                close(u[0][0]*u[1][1]-u[0][1]*u[1][0], 1, "refining transport has determinant one")
                edge = subtract(scale(cmath.exp(1j*k[j]), I2), u)
                direct = add(direct, scale(1/(a*a), mm(adjoint(edge), edge)))
            expected = symbol(a, g, k)
            matrix_close(direct, expected, "direct connection gradient equals stated symbol")
            v = tuple(math.sin(a*g)*math.sin(x) for x in k)
            z = plus_spinor(v)
            lower = (2/(a*a))*(d-math.cos(a*g)*sum(math.cos(x) for x in k)
                                    -math.sqrt(sum(x*x for x in v)))
            for actual, target in zip(mv(direct, z), (lower*x for x in z)):
                close(actual, target, "explicit lower-band spinor")
            require(lower >= -1e-9, "sampled connection symbol is nonnegative")
            cases += 1
    equal(cases, 144, "direct symbol count")
    print("PASS: 144 numerical SU(2) edge-gradient symbols agree with the Pauli Fourier formula and explicit lower-band spinors.")


def plaquette_orientations():
    cases = 0
    for mu, nu in combinations(range(3), 2):
        for g in (0.5, 1.0, -1.25):
            previous_error = math.inf
            for a in (1/8, 1/16, 1/32, 1/64):
                u, v = transport(a*g, mu), transport(a*g, nu)
                # Actual +mu,+nu,-mu,-nu path, with operators composed right to left.
                path = mm(mm(mm(adjoint(v), adjoint(u)), v), u)
                standard_product = mm(mm(mm(u, v), adjoint(u)), adjoint(v))
                leading = scale(g*g, commutator(PAULI[mu], PAULI[nu]))
                scaled_path = scale(1/(a*a), subtract(path, I2))
                scaled_standard = scale(1/(a*a), subtract(standard_product, I2))
                error = math.sqrt(matrix_norm_squared(subtract(scaled_path, leading)))
                require(error < previous_error, "oriented plaquette expansion converges")
                require(error <= 20*a*max(1, abs(g)**3), "sampled path cubic remainder")
                require(math.sqrt(matrix_norm_squared(add(scaled_standard, leading)))
                        <= 20*a*max(1, abs(g)**3), "opposite written product has opposite leading sign")
                previous_error = error
                defect = subtract(I2, path)
                matrix_close(mm(adjoint(defect), defect), scale(4*math.sin(a*g)**4, I2),
                             "exact SU(2) scalar square-defect formula")
                cases += 1
    equal(cases, 36, "plaquette refinement count")
    print("PASS: 36 numerical plaquettes check both orientation signs and (I-H)* (I-H)=4sin^4(ag) I.")


def edge_bounds_and_limits():
    bound_probes, saturators = 0, 0
    for d in (2, 3):
        for theta in (0.0, 0.2, -0.7, 1.4, math.pi/2, 2.4, math.pi):
            a = 0.4
            radius = math.sqrt(d*d*math.cos(theta)**2+d*math.sin(theta)**2)
            edge = exact_bloch_edge(a, theta, d)
            close(edge, 2*(d-radius)/(a*a), "rationalized Bloch edge")
            cosine = max(-1.0, min(1.0, d*math.cos(theta)/radius))
            star = math.acos(cosine)
            lower_at_star = 2*(d-d*math.cos(theta)*math.cos(star)
                               -abs(math.sin(theta))*math.sqrt(d)*abs(math.sin(star)))/(a*a)
            close(lower_at_star, edge, "continuous Bloch saturator")
            saturators += 1
            for indices in product(range(8), repeat=d):
                k = tuple(2*math.pi*n/8 for n in indices)
                lower = 2*(d-math.cos(theta)*sum(math.cos(x) for x in k)
                           -abs(math.sin(theta))*math.sqrt(sum(math.sin(x)**2 for x in k)))/(a*a)
                require(lower+2e-10 >= edge, "finite sampled momenta obey continuum-Bloch lower bound")
                bound_probes += 1
    equal(saturators, 14, "Bloch saturator count")
    equal(bound_probes, 4032, "sampled band lower-bound count")
    print("PASS: 14 numerical continuous-Bloch saturators and 4032 sampled momenta check the exact edge formula; no finite-grid attainment is presumed.")

    edge_cases, symbol_cases = 0, 0
    for d in (2, 3):
        for g in (0.5, 1.0, 1.7):
            last_edge_error = math.inf
            last_local_bound = math.inf
            for a in (1/4, 1/8, 1/16, 1/32, 1/64, 1/128):
                edge = exact_bloch_edge(a, a*g, d)
                target = (d-1)*g*g
                error = abs(edge-target)
                require(error < last_edge_error, "selected edge refinements approach continuum value")
                last_edge_error = error
                # HT5 with one square: defect=4 sin^4, congestion=8, physical edge factor a^-2.
                local_bound = math.sin(a*g)**4/(2*a*a)
                require(local_bound < last_local_bound, "single-square certificate decreases in this refinement")
                require(local_bound <= edge+1e-12, "local square certificate remains a valid lower bound")
                last_local_bound = local_bound
                edge_cases += 1
            require(last_edge_error/target < 1e-4, "last sampled edge near the continuum value")
            require(last_local_bound/target < 1e-4, "last sampled one-square certificate near zero")
            for seed in range(3):
                p = tuple((seed+1)*(j+1)/3-0.7 for j in range(d))
                target_matrix = continuum_symbol(g, p)
                last_error = math.inf
                for a in (1/4, 1/8, 1/16, 1/32, 1/64):
                    value = symbol(a, g, tuple(a*x for x in p))
                    error = math.sqrt(matrix_norm_squared(subtract(value, target_matrix)))
                    require(error < last_error, "selected symbols approach the differential symbol")
                    last_error = error
                    symbol_cases += 1
                require(last_error <= 0.001*max(1, math.sqrt(matrix_norm_squared(target_matrix))),
                        "last sampled differential symbol close to target")
    equal(edge_cases, 36, "edge refinement count")
    equal(symbol_cases, 90, "symbol refinement count")
    print("PASS: 36 edge and 90 symbol refinements approach the finite continuum response; the old single-square lower certificate instead tends to zero.")


def variance_identity():
    families = ((PAULI[0], PAULI[1]), PAULI,
                (((1, 0), (0, 2)), ((3, 0), (0, -1))),
                (add(PAULI[0], scale(2, PAULI[2])),
                 add(scale(0.5, I2), PAULI[1]),
                 add(scale(-1, I2), add(PAULI[0], PAULI[2]))))
    directions = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (3, 4, 0), (1, 2, 3))
    cases = 0
    for operators in families:
        for direction in directions:
            z = plus_spinor(direction)
            means = tuple(inner(z, mv(b, z)).real for b in operators)
            variance = sum(norm_squared(mv(b, z))-mean*mean for b, mean in zip(operators, means))
            require(variance >= -1e-12, "joint variance is nonnegative on probes")
            for seed in range(3):
                p = tuple((seed+1)*(j+1)*0.4-0.7 for j in range(len(operators)))
                direct = sum(norm_squared(tuple(momentum*x-y for x, y in zip(z, mv(b, z))))
                             for momentum, b in zip(p, operators))
                expected = variance+sum((momentum-mean)**2 for momentum, mean in zip(p, means))
                close(direct, expected, "variance plus squared displacement identity")
                at_means = sum(norm_squared(tuple(mean*x-y for x, y in zip(z, mv(b, z))))
                               for mean, b in zip(means, operators))
                close(at_means, variance, "momentum minimizer is the expectation vector")
                cases += 1
    equal(cases, 60, "joint variance identity probe count")
    for d in (2, 3):
        z = plus_spinor((1,)*d)
        variance = sum(norm_squared(mv(PAULI[j], z))-inner(z, mv(PAULI[j], z)).real**2
                       for j in range(d))
        close(variance, d-1, "Pauli joint variance attains continuum edge")

    # Noncommuting matrices can share an untouched eigenvector: noncommutation alone is insufficient.
    embedded = tuple(tuple(tuple(b[i][j] if i < 2 and j < 2 else 0 for j in range(3))
                           for i in range(3)) for b in PAULI)
    common = (0, 0, 1)
    for b in embedded:
        equal(mv(b, common), (0, 0, 0), "noncommuting family has a common zero eigenvector")
    require(matrix_norm_squared(commutator(embedded[0], embedded[1])) > 0,
            "embedded common-mode family really is noncommuting")
    print("PASS: 60 numerical joint-variance decompositions, two Pauli saturators, and an exact noncommuting/common-eigenvector witness are consistent.")


def source_equations():
    cases = 0
    for d in (2, 3):
        for g in (-2, -1, 1, 2):
            operators = tuple(scale(g, b) for b in PAULI[:d])
            total_pairing = 0
            commutator_cost = 0
            for j, bj in enumerate(operators):
                residual = scale(0, I2)
                for bi in operators:
                    residual = add(residual, commutator(bi, commutator(bi, bj)))
                    commutator_cost += matrix_norm_squared(commutator(bi, bj))
                equal(residual, scale(4*(d-1)*g**3, PAULI[j]), "Pauli source double commutator")
                product_matrix = mm(bj, residual)
                total_pairing += sum(product_matrix[i][i] for i in range(2))
            equal(total_pairing, commutator_cost, "source pairing is ordered commutator squared norm")
            equal(total_pairing, 8*d*(d-1)*g**4, "exact Pauli source cost")
            equal(complex(total_pairing).imag, 0, "source cost is exactly real")
            require(complex(total_pairing).real > 0, "Pauli background is not constant source-free Yang--Mills")
            for i, j in combinations(range(d), 2):
                ki = subtract(scale(i+2, I2), operators[i])
                kj = subtract(scale(j+2, I2), operators[j])
                equal(commutator(ki, kj), commutator(operators[i], operators[j]),
                      "covariant momentum components do not become commuting translations")
            cases += 1
    equal(cases, 8, "exact source family count")
    diagonal = (((1, 0), (0, 2)), ((-3, 0), (0, 5)), ((2, 0), (0, 7)))
    for b, c in product(diagonal, repeat=2):
        equal(commutator(b, c), ((0, 0), (0, 0)), "commuting source-free calibration")
    print("PASS: eight exact integer-Pauli source identities and nine commuting controls verify the source-free obstruction and noncommuting covariant momenta.")


def charged_and_neutral_translation_test():
    cases = 0
    for d, g, multiplier in product((2, 3), (0.5, 1.0, 2.0), (1, 2, 4, 8)):
        radius = multiplier*d*g
        p = tuple(radius/math.sqrt(d) for _ in range(d))
        energy_squared = radius*radius+d*g*g-2*g*radius
        energy = math.sqrt(energy_squared)
        particle_vector = plus_spinor(p)
        # Under conjugation, a vector of original momentum -p has physical antiparticle momentum +p.
        anti_vector = tuple(complex(x).conjugate() for x in plus_spinor(tuple(-x for x in p)))
        for matrix, vector in ((continuum_symbol(g, p), particle_vector),
                               (conjugate(continuum_symbol(g, tuple(-x for x in p))), anti_vector)):
            for actual, expected in zip(mv(matrix, vector), (energy_squared*x for x in vector)):
                close(actual, expected, "particle and antiparticle lower branches at equal physical momentum")
        charged_candidate = energy_squared-radius*radius
        pair_candidate = (2*energy)**2-(2*radius)**2
        close(charged_candidate, d*g*g-2*g*radius, "charged translation invariant candidate")
        close(pair_candidate, 4*(d*g*g-2*g*radius), "neutral pair translation invariant candidate")
        require(charged_candidate < 0 and pair_candidate < 0,
                "positive energies do not force a forward-cone translation spectrum")
        cases += 1
    equal(cases, 24, "charged/neutral translation probe count")
    print("PASS: 24 sampled charged and globally neutral equal-momentum pairs have positive energy but negative H^2-|P|^2.")


def main():
    direct_symbols()
    plaquette_orientations()
    edge_bounds_and_limits()
    variance_identity()
    source_equations()
    charged_and_neutral_translation_test()
    print("All seven check groups passed. Stdlib only; stdout only; no files written.")
    print("Sampled symbols and refinements are arithmetic checks, not proofs of a continuum quantum field theory.")
    print("The fixed background requires a source; global neutrality does not impose local Gauss law or restore Lorentz covariance.")


if __name__ == "__main__":
    main()
