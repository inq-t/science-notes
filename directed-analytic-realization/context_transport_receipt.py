"""Stdlib, stdout-only checks for context averaging and Pauli graph transport.

The coordinate-projection average is a finite R^9 calibration, NOT a sample
of the actual Spin(9) Haar orbit. Its mean is a CP qubit map even though some
individual compressed projections are not CP. Exact Fraction arithmetic is
used for the averaging and Pauli weights. Pauli products have exact integer
complex entries; graph Fourier/probe checks use numerical complex arithmetic.
The six-record POVM uses exact Bloch moment arithmetic; its Choi partial
transpose is also checked as an explicit four-by-four Fraction matrix.

Edge transports are sigma_mu in U(2), not i*sigma_mu in SU(2). Energies sum
once over every positive graph edge; there is no degree or volume averaging.
The scalar-adjoint tests concern their specified neutral scalar sector;
additional exact sign-basis checks flatten the full adjoint carrier at L=4.

No files, network, dependencies, local imports or eigensolvers are used.
No continuum spectral-gap or physical state-selection claim is made.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
import cmath
import math


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def equal(actual, expected, label):
    require(actual == expected, f"{label}: {actual!r} != {expected!r}")


def close(actual, expected, label, tolerance=2e-10):
    require(abs(actual-expected) <= tolerance*max(1.0, abs(actual), abs(expected)),
            f"{label}: {actual!r} != {expected!r}")


I2 = ((1, 0), (0, 1))
PAULI = (((0, 1), (1, 0)), ((0, -1j), (1j, 0)), ((1, 0), (0, -1)))


def mm(a, b):
    return tuple(tuple(sum(x*y for x, y in zip(row, column))
                       for column in zip(*b)) for row in a)


def mv(a, v):
    return tuple(sum(x*y for x, y in zip(row, v)) for row in a)


def inner(a, b):
    return sum(complex(x).conjugate()*y for x, y in zip(a, b))


def norm_squared(v):
    return float(inner(v, v).real)


def subtract(a, b):
    return tuple(x-y for x, y in zip(a, b))


def pauli_weights(lambdas):
    x, y, z = lambdas
    return ((1+x+y+z)/4, (1+x-y-z)/4,
            (1-x+y-z)/4, (1-x-y+z)/4)


def coordinate_average():
    subsets = tuple(combinations(range(9), 3))
    total = [[0]*9 for _ in range(9)]
    for subset in subsets:
        for i in subset:
            total[i][i] += 1
    equal(len(subsets), 84, "rank-three coordinate projection count")
    average = [[F(value, len(subsets)) for value in row] for row in total]
    for i in range(9):
        for j in range(9):
            equal(average[i][j], F(1, 3) if i == j else F(0), "full R9 mean")
    compressed = [row[:3] for row in average[:3]]
    equal(compressed, [[F(int(i == j), 3) for j in range(3)] for i in range(3)],
          "retained R3 mean")
    lambdas = (F(1, 3),)*3
    weights = pauli_weights(lambdas)
    equal(weights, (F(1, 2), F(1, 6), F(1, 6), F(1, 6)), "depolarizer Pauli weights")
    equal(sum(weights), 1, "unital CP mixture normalization")
    signs = ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))
    for direction in range(3):
        returned = sum(weight*sign[direction] for weight, sign in zip(weights, signs))
        equal(returned, F(1, 3), "actual Pauli-mixture contraction")
        equal(1-returned, F(2, 3), "unit-rate centered generator gap")
    print("PASS: all 84 coordinate rank-three projections average to I9/3; compressed Bloch mean I3/3.")
    print("PASS: exact depolarizer weights (1/2,1/6,1/6,1/6) and unit-rate centered gap 2/3.")


def non_cp_projection():
    weights = pauli_weights((F(1), F(1), F(0)))
    equal(weights, (F(3, 4), F(1, 4), F(1, 4), F(-1, 4)), "non-CP Pauli weight")
    # diag(1,1,0) keeps off-diagonal entries and replaces both diagonals by half the trace.
    def channel(a):
        t = (a[0][0]+a[1][1])/2
        return ((t, a[0][1]), (a[1][0], t))
    choi = [[0j]*4 for _ in range(4)]
    for i in range(2):
        for j in range(2):
            unit = tuple(tuple(F(int(k == i and l == j)) for l in range(2))
                         for k in range(2))
            image = channel(unit)
            for k in range(2):
                for l in range(2):
                    choi[2*i+k][2*j+l] = image[k][l]/2
    bell_minus = (1, 0, 0, -1)
    # The entries and this unnormalized-vector quotient are exactly binary-representable.
    equal(inner(bell_minus, mv(choi, bell_minus))/norm_squared(bell_minus),
          -0.25, "negative normalized Choi expectation")
    print("PASS: Bloch diag(1,1,0) has weight -1/4 and a negative Choi witness.")


def classical_record_threshold():
    directions = tuple(tuple(F(sign if j == axis else 0) for j in range(3))
                       for axis in range(3) for sign in (-1, 1))
    # P_n=(I+n.sigma)/2; E_n=P_n/3. These are exact coefficient identities.
    equal(sum(F(1, 6) for _ in directions), 1, "POVM identity coefficient")
    for j in range(3):
        equal(sum(n[j]/6 for n in directions), 0, "POVM traceless coefficient")
        for k in range(3):
            equal(sum(n[j]*n[k] for n in directions),
                  2*int(j == k), "six-direction second moment")
    vectors = ((F(0), F(0), F(0)), (F(1), F(0), F(0)),
               (F(-1), F(0), F(0)), (F(0), F(3, 5), F(4, 5)),
               (F(1, 3), F(-2, 3), F(2, 3)),
               (F(1, 4), F(-1, 3), F(1, 2)),
               (F(-2, 7), F(3, 7), F(-1, 7)))
    for r in vectors:
        require(sum(x*x for x in r) <= 1, "input Bloch vector is a state")
        probabilities = tuple((1+sum(n[j]*r[j] for j in range(3)))/6
                              for n in directions)
        require(all(p >= 0 for p in probabilities), "record probabilities nonnegative")
        equal(sum(probabilities), 1, "record probability normalization")
        prepared = tuple(sum(p*n[j] for p, n in zip(probabilities, directions))
                         for j in range(3))
        equal(tuple(3*x for x in prepared), r, "full record reconstructs input Bloch vector")
        equal(prepared, tuple(x/3 for x in r), "measure-and-prepare returns r/3")
    print("PASS: seven exact Bloch states obey the six-record POVM, reconstruction, and r/3 preparation identities.")

    # J_lambda=lambda |Omega><Omega|+(1-lambda)I4/4, |Omega>=(00+11)/sqrt(2).
    # Its partial transpose is (1-lambda)I4/4+lambda SWAP/2.
    swap = tuple(tuple(F(int(i//2 == j % 2 and i % 2 == j//2))
                       for j in range(4)) for i in range(4))
    symmetric = ((1, 0, 0, 0), (0, 0, 0, 1), (0, 1, 1, 0))
    antisymmetric = (0, 1, -1, 0)
    lambdas = tuple(dict.fromkeys((F(0), F(1, 3), F(3, 5), F(1))
                                  + tuple(F(3, n) for n in (3, 5, 9, 12))))
    for lam in lambdas:
        partial_transpose = tuple(tuple((1-lam)*int(i == j)/4+lam*swap[i][j]/2
                                        for j in range(4)) for i in range(4))
        positive, possibly_negative = (1+lam)/4, (1-3*lam)/4
        equal(sum(partial_transpose[i][i] for i in range(4)), 1, "Choi PT trace")
        equal(3*positive+possibly_negative, 1, "Choi PT spectral trace")
        for vector in symmetric:
            equal(mv(partial_transpose, vector), tuple(positive*x for x in vector),
                  "exact triply degenerate symmetric PT eigenvalue")
        equal(mv(partial_transpose, antisymmetric),
              tuple(possibly_negative*x for x in antisymmetric),
              "exact antisymmetric PT eigenvalue")
        equal(possibly_negative >= 0, lam <= F(1, 3), "exact isotropic PPT threshold")
    equal((1-3*F(1, 3))/4, 0, "threshold eigenvalue vanishes")
    require((1-3*F(3, 5))/4 < 0 and (1-3*F(1))/4 < 0,
            "higher-contraction Choi matrices have a negative PT eigenvalue")
    for n in (3, 5, 9, 12):
        equal((1-3*F(3, n))/4 >= 0, n >= 9, "3/n partial-transpose threshold")
    # Numerical clock calibration only, not an exact transcendental arithmetic test.
    t_eb = 1.5*math.log(3)
    close(math.exp(-2*t_eb/3), 1/3, "Poisson clock reaches the exact record threshold")
    print("PASS: five exact isotropic Choi PT spectra verify the 1/3 and 3/n thresholds; Poisson time checked numerically.")


def shift(vertex, direction, amount, length):
    out = list(vertex)
    out[direction] = (out[direction]+amount) % length
    return tuple(out)


def connection_energy(field, d, length):
    return sum(norm_squared(subtract(field[shift(v, mu, 1, length)],
                                     mv(PAULI[mu], value)))
               for v, value in field.items() for mu in range(d))


def connection_laplacian(field, vertex, d, length):
    out = tuple(2*d*x for x in field[vertex])
    for mu in range(d):
        neighbors = tuple(field[shift(vertex, mu, 1, length)][j]
                          + field[shift(vertex, mu, -1, length)][j] for j in range(2))
        out = subtract(out, mv(PAULI[mu], neighbors))
    return out


def square_walk(vertex, length):
    current = vertex
    for mu, sign in ((0, 1), (1, 1), (0, -1), (1, -1)):
        following = shift(current, mu, sign, length)
        # A negative step uses the adjoint Pauli matrix, equal to itself.
        edge_tail = current if sign == 1 else following
        yield current, following, mu, (edge_tail, mu)
        current = following
    equal(current, vertex, "square loop closes")


def plus_spinor(vector):
    a, b = vector[:2]
    c = vector[2] if len(vector) == 3 else 0.0
    radius = math.sqrt(a*a+b*b+c*c)
    if radius < 1e-13:
        return (1.0+0j, 0j)
    if radius+c < 1e-13:
        return (0j, 1.0+0j)
    raw = (radius+c, a+1j*b)
    denominator = math.sqrt(norm_squared(raw))
    return tuple(x/denominator for x in raw)


def graph_transport():
    minus_identity = ((-1, 0), (0, -1))
    for mu, nu in combinations(range(3), 2):
        holonomy = mm(mm(mm(PAULI[nu], PAULI[mu]), PAULI[nu]), PAULI[mu])
        equal(holonomy, minus_identity, "exact Pauli plaquette holonomy")
    equal(F(4, 4*2), F(1, 2), "length-four, defect-four, overlap-two certificate")
    probe_count = 0
    band_count = 0
    for d, length in ((2, 4), (2, 6), (3, 4), (3, 6)):
        vertices = tuple(product(range(length), repeat=d))
        uses = Counter(edge for v in vertices for _, _, _, edge in square_walk(v, length))
        for vertex in vertices:
            for mu in range(d):
                equal(uses[(vertex, mu)], 2 if mu < 2 else 0, "actual loop-edge incidence")
        sharp_edge = 2*d-2*math.sqrt(d)
        spinor = plus_spinor((1.0,)*d)
        constant = {v: spinor for v in vertices}
        norm = sum(norm_squared(value) for value in constant.values())
        close(connection_energy(constant, d, length)/norm, sharp_edge,
              "constant aligned spinor saturates spectral edge")
        for v in vertices:
            close(norm_squared(subtract(connection_laplacian(constant, v, d, length),
                                          tuple(sharp_edge*x for x in spinor))),
                  0, "matrix-free constant eigenmode")
        for seed in range(1, 9):
            field = {v: (complex(math.sin(seed+sum((j+1)*x for j, x in enumerate(v))),
                                  math.cos(seed*0.3+sum(v))),
                         complex(math.cos(seed+sum((j+2)*x for j, x in enumerate(v))),
                                 math.sin(seed*0.7-sum(v)))) for v in vertices}
            norm = sum(norm_squared(value) for value in field.values())
            energy = connection_energy(field, d, length)
            laplacian_form = sum(inner(value, connection_laplacian(field, v, d, length))
                                 for v, value in field.items())
            close(laplacian_form, energy, "direct gradient equals Laplacian quadratic form")
            require(energy+1e-9 >= 0.5*norm, "loop-gluing lower certificate on probe")
            require(energy+1e-9 >= sharp_edge*norm, "sharp Fourier lower bound on probe")
            loop_energy = 0.0
            for v in vertices:
                local_cost = sum(norm_squared(subtract(field[following], mv(PAULI[mu], field[current])))
                                 for current, following, mu, _ in square_walk(v, length))
                require(4*norm_squared(field[v]) <= 4*local_cost+1e-9,
                        "individual loop telescoping Cauchy bound")
                loop_energy += local_cost
            first_two_energy = sum(norm_squared(subtract(field[shift(v, mu, 1, length)],
                                                          mv(PAULI[mu], value)))
                                   for v, value in field.items() for mu in range(2))
            close(loop_energy, 2*first_two_energy, "summed loop overlap")
            probe_count += 1
        bottom = math.inf
        for momenta in product(range(length), repeat=d):
            cosines = tuple(math.cos(2*math.pi*p/length) for p in momenta)
            radius = math.sqrt(sum(x*x for x in cosines))
            # These are the closed two-by-two Pauli eigenvalues, not a numerical eigensolver.
            lower, upper = 2*d-2*radius, 2*d+2*radius
            require(lower+1e-12 >= sharp_edge, "every Fourier band obeys the lower edge")
            require(upper >= lower, "ordered two-by-two bands")
            bottom = min(bottom, lower)
            band_count += 1
        close(bottom, sharp_edge, "finite Fourier minimum")
        # One nonconstant Fourier mode independently checks the matrix-free form.
        momenta = tuple((mu+1) % length for mu in range(d))
        cosines = tuple(math.cos(2*math.pi*p/length) for p in momenta)
        spinor_mode = plus_spinor(cosines)
        field = {v: tuple(cmath.exp(2j*math.pi*sum(p*x for p, x in zip(momenta, v))/length)*a
                          for a in spinor_mode) for v in vertices}
        eigenvalue = 2*d-2*math.sqrt(sum(x*x for x in cosines))
        norm = sum(norm_squared(value) for value in field.values())
        close(connection_energy(field, d, length)/norm, eigenvalue, "nonconstant Fourier gradient form")
    equal(probe_count, 32, "nonconstant graph probe count")
    equal(band_count, 332, "closed Fourier block count")
    print("PASS: exact plaquette holonomy -I; four graph families have length 4, defect 4, overlap 2.")
    print("PASS: 32 matrix-free probes satisfy the gluing bound 1/2; all 332 Fourier blocks checked.")
    print("PASS: constant aligned spinors attain 2d-2sqrt(d); nonconstant Fourier forms agree.")


def scalar_adjoint_transport():
    cases = 0
    for d in (2, 3):
        for length in (4, 8, 16):
            vertices = tuple(product(range(length), repeat=d))
            field = {v: math.cos(2*math.pi*v[0]/length) for v in vertices}
            close(sum(field.values()), 0, "mean-zero scalar field", 1e-9)
            norm = sum(value*value for value in field.values())
            ordinary_energy = 0.0
            adjoint_energy = 0.0
            for vertex, value in field.items():
                scalar_matrix = ((value, 0), (0, value))
                for mu in range(d):
                    transported = mm(mm(PAULI[mu], scalar_matrix), PAULI[mu])
                    equal(transported, scalar_matrix, "adjoint scalar is untouched by edge transport")
                    next_value = field[shift(vertex, mu, 1, length)]
                    ordinary_energy += (next_value-value)**2
                    target = ((next_value, 0), (0, next_value))
                    difference = tuple(tuple(x-y for x, y in zip(row, other))
                                       for row, other in zip(target, transported))
                    # Normalized trace HS norm: Tr(D*D)/2, so ||f I||_tau^2=|f|^2.
                    adjoint_energy += sum(abs(x)**2 for row in difference for x in row)/2
            close(adjoint_energy, ordinary_energy, "neutral scalar ordinary graph form")
            close(adjoint_energy/norm, 2-2*math.cos(2*math.pi/length),
                  "scalar mean-zero graph eigenvalue")
            cases += 1
    equal(cases, 6, "neutral scalar sector count")
    print("PASS: six adjoint scalar sectors reduce to graph gaps 2-2cos(2pi/L), L=4,8,16.")


def full_adjoint_flattening():
    basis = (I2,)+PAULI
    signs = tuple(tuple(1 if a == 0 or a == mu+1 else -1 for a in range(4))
                  for mu in range(3))
    for mu in range(3):
        for a, matrix in enumerate(basis):
            equal(mm(mm(PAULI[mu], matrix), PAULI[mu]),
                  tuple(tuple(signs[mu][a]*x for x in row) for row in matrix),
                  "actual adjoint action equals Pauli sign action")

    def from_coefficients(coefficients):
        return tuple(tuple(sum(coefficients[a]*basis[a][i][j] for a in range(4))
                           for j in range(2)) for i in range(2))

    parallel_count = 0
    for d in (2, 3):
        length = 4
        vertices = tuple(product(range(length), repeat=d))
        frames = {v: tuple(math.prod(signs[mu][a]**v[mu] for mu in range(d))
                           for a in range(4)) for v in vertices}
        for v in vertices:
            for mu in range(d):
                neighbor = shift(v, mu, 1, length)
                equal(frames[neighbor], tuple(signs[mu][a]*frames[v][a] for a in range(4)),
                      "periodic adjoint frame flattens every edge, including wraparound")
        for a in range(4):
            # The four fields G_v e_a are pointwise orthonormal for normalized trace.
            for v in vertices:
                coefficients = tuple(frames[v][j]*int(j == a) for j in range(4))
                matrix = from_coefficients(coefficients)
                for mu in range(d):
                    neighbor = shift(v, mu, 1, length)
                    target = from_coefficients(tuple(frames[neighbor][j]*int(j == a)
                                                     for j in range(4)))
                    equal(mm(mm(PAULI[mu], matrix), PAULI[mu]), target,
                          "actual matrix-valued field is parallel")
            parallel_count += 1
        # Integer-complex coefficients and Pauli entries make these binary-representable
        # operations exact. This probes the full complex carrier, not just Hermitian fields.
        fields = {v: tuple(complex((sum((a+j+1)*x for j, x in enumerate(v))+a) % 7-3,
                                    (sum((a+2*j+1)*x for j, x in enumerate(v))+2*a) % 5-2)
                           for a in range(4)) for v in vertices}
        ordinary_energy = 0
        adjoint_energy = 0
        for v in vertices:
            matrix = from_coefficients(tuple(frames[v][a]*fields[v][a] for a in range(4)))
            for mu in range(d):
                neighbor = shift(v, mu, 1, length)
                target = from_coefficients(tuple(frames[neighbor][a]*fields[neighbor][a]
                                                 for a in range(4)))
                transported = mm(mm(PAULI[mu], matrix), PAULI[mu])
                difference = tuple(target[i][j]-transported[i][j]
                                   for i in range(2) for j in range(2))
                adjoint_energy += sum((x.conjugate()*x).real for x in difference)/2
                ordinary_energy += sum((x.conjugate()*x).real
                                       for x in subtract(fields[neighbor], fields[v]))
        equal(adjoint_energy, ordinary_energy, "full actual adjoint matrix form equals four scalar forms")
    equal(parallel_count, 8, "four parallel fields on each of two graphs")
    print("PASS: exact L=4 adjoint sign frames flatten both d=2,3 graphs; eight parallel matrix fields and full forms checked.")


def main():
    coordinate_average()
    non_cp_projection()
    classical_record_threshold()
    graph_transport()
    scalar_adjoint_transport()
    full_adjoint_flattening()
    print("All ten check groups passed. Stdlib only; stdout only; no files written.")
    print("Coordinate averaging is not Spin(9) Haar sampling; graph probes are not a continuum proof.")
    print("U(2) spinor holonomy coercivity does not control the adjoint neutral scalar modes.")


if __name__ == "__main__":
    main()
