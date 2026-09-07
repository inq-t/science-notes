"""Stdlib, stdout-only checks for the neutral free return of transport response.

Exact integer/Fraction tests cover matrix-unit energy sums versus differences,
declared normalized occupation basis energies, rational weight identities,
and a finite Gaussian/Hermite calibration. Radical/Fourier/refinement and
Taylor checks use floating-point arithmetic and are labelled accordingly.

The occupation cutoff only selects states of the full free model; it does not
assert exact canonical commutators on a truncated oscillator Hilbert space.
Neutrality here means the chosen global charge N_plus-N_minus, not a local
Yang--Mills Gauss constraint. No interacting or continuum gap is certified.
No files, network, external dependencies, local imports or eigensolvers are used.
"""

from fractions import Fraction as F
from itertools import product
import math


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def equal(actual, expected, label):
    require(actual == expected, f"{label}: {actual!r} != {expected!r}")


def close(actual, expected, label, tolerance=2e-11):
    require(abs(actual-expected) <= tolerance*max(1.0, abs(actual), abs(expected)),
            f"{label}: {actual!r} != {expected!r}")


def mm(a, b):
    return tuple(tuple(sum(x*y for x, y in zip(row, column))
                       for column in zip(*b)) for row in a)


def matrix_units_and_occupations():
    energies = (1, 2, 3)
    a = tuple(tuple(energies[i]*int(i == j) for j in range(3)) for i in range(3))
    sums, differences = [], []
    for i, j in product(range(3), repeat=2):
        unit = tuple(tuple(int(k == i and l == j) for l in range(3)) for k in range(3))
        left, right = mm(a, unit), mm(unit, a)
        for k, l in product(range(3), repeat=2):
            equal(left[k][l]+right[k][l], (energies[i]+energies[j])*unit[k][l],
                  "pair energy acts by sum on matrix units")
            equal(left[k][l]-right[k][l], (energies[i]-energies[j])*unit[k][l],
                  "Liouville commutator acts by difference on matrix units")
        sums.append(energies[i]+energies[j])
        differences.append(energies[i]-energies[j])
    equal(min(sums), 2, "positive pair edge")
    equal(differences.count(0), 3, "commutator has three diagonal zero modes")
    equal(sorted(set(differences)), [-2, -1, 0, 1, 2], "signed difference spectrum")

    # These are labels in the normalized occupation basis, not coherent amplitudes.
    # Keep total occupation <=4, so both the first and second neutral pair sectors appear.
    labels = tuple(n for n in product(range(5), repeat=6) if sum(n) <= 4)
    neutral, positive, zero = [], [], []
    for occupation in labels:
        n_plus, n_minus = occupation[:3], occupation[3:]
        charge = sum(n_plus)-sum(n_minus)
        energy = sum(w*(p+m) for w, p, m in zip(energies, n_plus, n_minus))
        if charge == 0:
            neutral.append((occupation, energy))
        if energy > 0:
            positive.append(energy)
        else:
            zero.append(occupation)
    equal(len(labels), 210, "total-cutoff occupation count")
    equal(len(neutral), 46, "neutral occupation count")
    equal(zero, [(0,)*6], "unique scalar vacuum in tested sectors")
    equal(min(positive), 1, "charged one-particle edge")
    equal(min(energy for _, energy in neutral if energy), 2, "neutral excitation edge")
    print("PASS: nine matrix units distinguish pair sums from Liouville differences; 210 occupation states include 46 neutral states with edge 2.")


def pauli_bands_and_neutral_pairs():
    cases = 0
    for d in (2, 3):
        gamma = 2*d-2*math.sqrt(d)
        charged_edge = math.sqrt(gamma)
        for length in (4, 6, 8):
            frequencies = []
            for momenta in product(range(length), repeat=d):
                radius = math.sqrt(sum(math.cos(2*math.pi*p/length)**2 for p in momenta))
                frequencies.extend((math.sqrt(2*d-2*radius), math.sqrt(2*d+2*radius)))
            close(min(frequencies), charged_edge, "actual Pauli-band frequency edge")
            # Two independent species give every ordered pair of frequencies.
            # The minimum of this product set equals the sum of its minima.
            neutral_edge = min(frequencies)+min(frequencies)
            close(neutral_edge, 2*charged_edge, "neutral free-pair edge")
            adjoint_edge = 2-2*math.cos(2*math.pi/length)
            require(adjoint_edge > 0, "adjoint graph edge above its whole parallel kernel")
            require(abs(adjoint_edge-neutral_edge) > 0.1,
                    "adjoint diffusion is not the free pair Hamiltonian")
            cases += 1
    equal(cases, 6, "finite Pauli-band family count")
    print("PASS: six finite Pauli spectra give charged edge sqrt(gamma) and free neutral edge 2sqrt(gamma), distinct from adjoint diffusion.")


def weighted_identity_and_refinement():
    rational_cases = 0
    for weights in ((F(1), F(2)), (F(2, 3), F(5, 4)),
                    (F(1), F(1), F(1)), (F(1, 2), F(2), F(7, 3))):
        for a in (F(1), F(1, 2), F(1, 5)):
            q2 = sum(w*w for w in weights)
            # Treat Q=sqrt(q2) formally. b_j=c_j Q, with c_j rational.
            coefficients = tuple(a*a*w*w/q2 for w in weights)
            equal(sum(coefficients), a*a, "exact coefficient of sum b_j = a^2 Q")
            for w, coefficient in zip(weights, coefficients):
                # (sum b_j)*b_j=(a^2 w_j)^2, positive, so its positive root is a^2 w_j.
                equal(a*a*coefficient*q2, a**4*w*w, "exact radical-elimination identity")
            # Both sides have the same formal coefficients of 1 and Q.
            lhs_coefficients = (2*a*a*sum(weights), -2*a*a)
            rhs_coefficients = (2*sum(a*a*w for w in weights), -2*sum(coefficients))
            equal(lhs_coefficients, rhs_coefficients, "exact coefficient identity for a^2 gamma")
            q = math.sqrt(float(q2))
            b = tuple(float(coefficient)*q for coefficient in coefficients)
            gamma = 2*(float(sum(weights))-q)
            close(float(a*a)*gamma,
                  2*(math.sqrt(sum(b))*sum(math.sqrt(x) for x in b)-sum(b)),
                  "numerical radical value of exact weighted identity")
            rational_cases += 1
    equal(rational_cases, 12, "rational weighted identity count")
    print("PASS: 12 rational weighted models verify the exact identity a^2 gamma=2(sqrt(sum b)sum sqrt(b)-sum b), plus numerical radical values.")

    isotropic_cases = 0
    for d in (2, 3):
        for v in (F(1), F(3, 2)):
            invariant = None
            for a in (F(1), F(1, 2), F(1, 4), F(1, 8)):
                af, vf = float(a), float(v)
                w = vf*vf*math.sqrt(d)/(af*af)
                q = math.sqrt(d)*w
                b = af*af*w*w/q
                gamma = 2*(d*w-q)
                close(b, vf*vf, "fixed isotropic physical quadratic velocity")
                close(af*af*gamma, 2*d*vf*vf*(math.sqrt(d)-1),
                      "isotropic inverse-square edge scaling")
                if invariant is not None:
                    close(af*af*gamma, invariant, "refinement preserves scaled isotropic edge")
                invariant = af*af*gamma
                isotropic_cases += 1
    equal(isotropic_cases, 16, "isotropic refinement count")

    anisotropic_cases = 0
    for velocities in ((F(3, 5), F(4, 5)), (F(3), F(4)),
                       (F(1, 3), F(2, 3), F(2, 3)), (F(1), F(2), F(2))):
        v2 = sum(v*v for v in velocities)
        # Chosen Pythagorean examples make the norm rational, so this part is exact.
        root = F(math.isqrt(v2.numerator), math.isqrt(v2.denominator))
        equal(root*root, v2, "exact velocity norm")
        for a in (F(1), F(1, 2), F(1, 4)):
            weights = tuple(root*v/(a*a) for v in velocities)
            q = v2/(a*a)
            equal(q*q, sum(w*w for w in weights), "exact norm of anisotropic weights")
            b = tuple(a*a*w*w/q for w in weights)
            equal(b, tuple(v*v for v in velocities), "exact prescribed anisotropic quadratic velocities")
            equal(a*a*2*(sum(weights)-q), 2*(root*sum(velocities)-v2),
                  "anisotropic inverse-square edge scaling")
            require(sum(weights) > q, "positive nondegenerate multidirectional edge")
            anisotropic_cases += 1
    equal(anisotropic_cases, 12, "anisotropic refinement count")
    print("PASS: 16 numerical isotropic and 12 exact anisotropic refinements keep nonzero velocities while gamma scales as a^-2.")

    last_error = math.inf
    for denominator in (1, 2, 4, 8, 16, 32, 64):
        a = 1/denominator
        root = math.sqrt(1+2*a**4)
        # w=(a^-2,1,1); use a stable rationalized expression for gamma.
        gamma = 4-4*a*a/(root+1)
        b1, b2, b3 = 1/root, a**4/root, a**4/root
        close(gamma, 2*(a**-2+2-math.sqrt(a**-4+2)),
              "degenerate scaling agrees with weighted edge", 1e-9)
        close(b1, a*a*a**-4/math.sqrt(a**-4+2), "first degenerate quadratic coefficient")
        close(b2, a*a/math.sqrt(a**-4+2), "second degenerate quadratic coefficient")
        equal(b2, b3, "transverse symmetry")
        error = abs(gamma-4)+abs(b1-1)+b2+b3
        require(error < last_error, "selected refinements approach gamma=4 and b=(1,0,0)")
        last_error = error
    require(last_error < 0.001, "last selected degenerate refinement is close to the stated limit")
    print("PASS: seven degenerate refinements approach finite gamma=4 only while the two transverse quadratic velocities vanish.")


def isotropic_quartic_expansion():
    cases = 0
    for d in (2, 3):
        root_d = math.sqrt(d)
        for direction in ((1,)+(0,)*(d-1), (1,)*d):
            u2 = sum(x*x for x in direction)
            u4 = sum(x**4 for x in direction)
            u6 = sum(x**6 for x in direction)
            sixth_coefficient = (2*u6/(45*root_d)-u2*u4/(6*d**1.5)
                                 +u2**3/(8*d**2.5))
            require(abs(sixth_coefficient) > 0.001, "tested direction has a visible sixth-order term")
            for t in (1/8, 1/16, 1/32, 1/64):
                momenta = tuple(t*x for x in direction)
                sin2 = sum(math.sin(k)**2 for k in momenta)
                q = math.sqrt(sum(math.cos(k)**2 for k in momenta))
                # Stable lambda(k)-gamma = 2(d-sum cos^2)/(sqrt(d)+sqrt(sum cos^2)).
                exact_increment = 2*sin2/(root_d+q)
                s2, s4 = sum(k*k for k in momenta), sum(k**4 for k in momenta)
                quartic_increment = s2/root_d-s4/(3*root_d)+s2*s2/(4*d**1.5)
                scaled_remainder = (exact_increment-quartic_increment)/t**6
                require(abs(scaled_remainder-sixth_coefficient)
                        <= 0.025*abs(sixth_coefficient)+2e-7,
                        "sampled quartic remainder follows its explicit sixth-order coefficient")
                cases += 1
    equal(cases, 16, "quartic expansion probe count")
    print("PASS: 16 axis/diagonal small-momentum probes check the isotropic quartic formula and sampled sixth-order remainder.")


def polynomial_derivative(p):
    return tuple(F(i)*p[i] for i in range(1, len(p))) or (F(0),)


def polynomial_trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


def gaussian_response_calibration():
    modes = 0
    for frequency in (F(1, 2), F(1), F(3)):
        for epsilon in (F(1, 3), F(1), F(2)):
            variance = epsilon/(2*frequency)
            # Gaussian moments follow integration by parts for exp(-q^2/(2 variance)).
            moments = {0: F(1)}
            for n in range(1, 13):
                moments[n] = F(0) if n % 2 else (n-1)*variance*moments[n-2]
            equal(moments[2], epsilon/(2*frequency), "finite Gaussian position covariance")
            for q in (F(-2), F(0), F(3, 5)):
                log_derivative = -frequency*q/epsilon
                psi_second_over_psi = log_derivative**2-frequency/epsilon
                h_over_psi = (-epsilon**2*psi_second_over_psi/2
                              +frequency**2*q*q/2-epsilon*frequency/2)
                equal(h_over_psi, 0, "actual Gaussian vacuum solves factored Hamiltonian")
            polynomials = [(F(1),), (F(0), F(1))]
            for n in range(1, 5):
                current, previous = polynomials[n], polynomials[n-1]
                nxt = [F(0)]+list(current)
                for j, coefficient in enumerate(previous):
                    nxt[j] -= n*variance*coefficient
                polynomials.append(polynomial_trim(nxt))
            for n, p in enumerate(polynomials):
                first = polynomial_derivative(p)
                second = polynomial_derivative(first)
                result = [F(0)]*max(len(p), len(first)+1)
                for j, coefficient in enumerate(first):
                    result[j+1] += epsilon*frequency*coefficient
                for j, coefficient in enumerate(second):
                    result[j] -= epsilon**2*coefficient/2
                equal(polynomial_trim(result), polynomial_trim(tuple(n*epsilon*frequency*c for c in p)),
                      "exact Hermite eigenmode under the ground-state transform")
                norm = sum(x*y*moments[i+j] for i, x in enumerate(p) for j, y in enumerate(p))
                equal(norm, math.factorial(n)*variance**n, "Gaussian polynomial norm")
                equal(n*epsilon*frequency/epsilon, n*frequency, "clock rate is energy divided by epsilon")
                modes += 1
    equal(modes, 54, "finite Gaussian mode count")
    print("PASS: 54 exact finite Gaussian/Hermite modes verify the vacuum subtraction, covariance epsilon/(2A), and energy-versus-rate normalization.")


def main():
    matrix_units_and_occupations()
    pauli_bands_and_neutral_pairs()
    weighted_identity_and_refinement()
    isotropic_quartic_expansion()
    gaussian_response_calibration()
    print("All seven check groups passed. Stdlib only; stdout only; no files written.")
    print("Finite identities and selected numerical refinements do not prove an interacting or continuum limit.")
    print("Global charge neutrality, adjoint diffusion, and local gauge invariance are distinct constructions.")


if __name__ == "__main__":
    main()
