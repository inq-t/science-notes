"""Exact, stdlib, stdout-only finite checks for a pure dark-vacuum response.

Heisenberg convention: L_a Omega=0, K=sum L_a*L_a/2, and
G(A)=sum L_a* A L_a-K A-A K. Gaussian-rational matrix helpers are reused
from positive_cone_process_receipt.py. Spin-chain and graph-cluster tests
use sparse rational matrices on the ACTUAL qubit tensor product, not just
matrices indexed by sites. Their one-excitation compression is checked
separately. The finite entangled vacuum is obtained by a declared global
unitary conjugation; that conjugation is not asserted to preserve locality.

All arithmetic is exact. There is no sampling, eigensolver, file output,
network, external dependency or numerical approximation. The finite tests
do not prove thermodynamic or continuum limits, a relativistic local net,
an emergent physical clock, or the Yang--Mills existence and mass gap.
"""

from fractions import Fraction as F
from functools import lru_cache
from itertools import product

import positive_cone_process_receipt as pc
from context_transport_receipt import equal, require


def zero(n):
    return pc.matrix([[0]*n for _ in range(n)])


def unit(n, i, j):
    return pc.matrix([[int(r == i and c == j) for c in range(n)] for r in range(n)])


def matrix_sum(matrices, n):
    result = zero(n)
    for a in matrices:
        result = pc.add(result, a)
    return result


def tensor(a, b):
    return pc.matrix([[a[i][j]*b[r][s] for j in range(len(a)) for s in range(len(b))]
                      for i in range(len(a)) for r in range(len(b))])


def apply(a, x):
    return tuple(sum(value*coordinate for value, coordinate in zip(row, x)) for row in a)


def inner(x, y):
    return sum(a.conjugate()*b for a, b in zip(x, y))


def projector(x):
    return pc.matrix([[a*b.conjugate() for b in x] for a in x])


def vacuum_expectation(omega, a):
    return inner(omega, apply(a, omega))


def response(jumps):
    n = len(jumps[0])
    return pc.scale(matrix_sum((pc.multiply(pc.adjoint(l), l) for l in jumps), n), F(1, 2))


def generator(jumps, k, a):
    return pc.sub(matrix_sum((pc.multiply(pc.multiply(pc.adjoint(l), a), l) for l in jumps), len(a)),
                  pc.add(pc.multiply(k, a), pc.multiply(a, k)))


def dual_generator(jumps, k, rho):
    return pc.sub(matrix_sum((pc.multiply(pc.multiply(l, rho), pc.adjoint(l)) for l in jumps), len(rho)),
                  pc.add(pc.multiply(k, rho), pc.multiply(rho, k)))


def commutator(a, b):
    return pc.sub(pc.multiply(a, b), pc.multiply(b, a))


def mixed_probe(n):
    return pc.matrix([[pc.C(F(i-j, n+1), F((i+1)*(j+2), n+3)) for j in range(n)] for i in range(n)])


def all_observables(n):
    return tuple(unit(n, i, j) for i, j in product(range(n), repeat=2))+(pc.identity(n), mixed_probe(n))


def schwarz_observables(n):
    return (pc.identity(n), unit(n, 0, 0), unit(n, 0, n-1),
            unit(n, n-1, 0), unit(n, n-1, n-1), mixed_probe(n))


@lru_cache(None)
def entangled_fixture():
    lowering = unit(2, 0, 1)
    original = (tensor(lowering, pc.I), tensor(pc.I, lowering))
    u = pc.matrix(((F(3, 5), 0, 0, F(-4, 5)), (0, 1, 0, 0),
                   (0, 0, 1, 0), (F(4, 5), 0, 0, F(3, 5))))
    jumps = tuple(pc.multiply(pc.multiply(u, l), pc.adjoint(u)) for l in original)
    omega = tuple(row[0] for row in u)
    return original, u, jumps, omega


def finite_fixtures():
    qubit = ((unit(2, 0, 1),), (pc.C(1), pc.C()))
    qutrit_jumps = (pc.matrix(((0, 1, 0), (0, 0, 1), (0, 0, 0))),
                   pc.matrix(((0, F(1, 3), pc.C(0, F(1, 2))),
                              (0, 0, F(1, 4)), (0, 0, 0))))
    _, _, entangled_jumps, entangled_omega = entangled_fixture()
    return (qubit, (qutrit_jumps, (pc.C(1), pc.C(), pc.C())),
            (entangled_jumps, entangled_omega))


def pure_dark_vacuum_identities():
    observable_count, defect_count, diagonal_count = 0, 0, 0
    for jumps, omega in finite_fixtures():
        n = len(omega)
        equal(inner(omega, omega), pc.C(1), "normalized pure dark vacuum")
        for l in jumps:
            equal(apply(l, omega), (pc.C(),)*n, "each jump annihilates the vacuum")
        k = response(jumps)
        equal(k, pc.adjoint(k), "positive loss response is self-adjoint")
        pc.positive_semidefinite(k)
        equal(apply(k, omega), (pc.C(),)*n, "response annihilates the dark vacuum")
        equal(generator(jumps, k, pc.identity(n)), zero(n), "Heisenberg generator is unital")
        equal(dual_generator(jumps, k, projector(omega)), zero(n), "pure vacuum state is stationary")
        for a in all_observables(n):
            ga = generator(jumps, k, a)
            equal(apply(ga, omega), tuple(-x for x in apply(k, apply(a, omega))),
                  "G(A)Omega=-K A Omega on the actual pure-state carrier")
            equal(vacuum_expectation(omega, ga), pc.C(), "stationary vacuum expectation")
            equal(generator(jumps, k, pc.adjoint(a)), pc.adjoint(ga), "generator preserves adjoints")
            observable_count += 1
        probes = schwarz_observables(n)
        for i, a in enumerate(probes):
            for j, b in enumerate(probes):
                astar = pc.adjoint(a)
                defect = pc.sub(generator(jumps, k, pc.multiply(astar, b)),
                                pc.add(pc.multiply(generator(jumps, k, astar), b),
                                       pc.multiply(astar, generator(jumps, k, b))))
                residual = matrix_sum((pc.multiply(pc.adjoint(commutator(l, a)), commutator(l, b)) for l in jumps), n)
                equal(defect, residual, "Schwarz infinitesimal defect is the exact commutator Gram form")
                equal(vacuum_expectation(omega, defect),
                      2*inner(apply(a, omega), apply(k, apply(b, omega))),
                      "vacuum Schwarz form has the factor 2K, while the vector generator is K")
                if i == j:
                    pc.positive_semidefinite(defect)
                    diagonal_count += 1
                defect_count += 1
    equal((observable_count, defect_count, diagonal_count), (35, 108, 18), "dark-vacuum identity counts")
    print("PASS: three pure dark vacua, 35 full matrix observables and 108 Schwarz defects give G(A)Omega=-K A Omega, stationarity, unitality and the vacuum form 2K.")


def amplitude_damping_return():
    jumps, omega = finite_fixtures()[0]
    k = response(jumps)
    equal(k, pc.matrix(((0, 0), (0, F(1, 2)))), "amplitude damping response normalization")
    triples = ((F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(8, 17), F(15, 17)))

    def explicit_channel(a, q):
        return pc.matrix(((a[0][0], q*a[0][1]),
                          (q*a[1][0], q*q*a[1][1]+(1-q*q)*a[0][0])))

    channel_count, composition_count = 0, 0
    for q, leaked_amplitude in triples:
        equal(q*q+leaked_amplitude*leaked_amplitude, 1, "rational damping amplitudes are normalized")
        kraus = (pc.matrix(((1, 0), (0, q))), pc.scale(unit(2, 0, 1), leaked_amplitude))
        equal(matrix_sum((pc.multiply(pc.adjoint(m), m) for m in kraus), 2), pc.I, "exact Kraus channel is unital and CP by construction")
        for a in all_observables(2):
            actual = matrix_sum((pc.multiply(pc.multiply(pc.adjoint(m), a), m) for m in kraus), 2)
            equal(actual, explicit_channel(a, q), "actual amplitude-damping Kraus formula")
            equal(apply(actual, omega), apply(pc.matrix(((1, 0), (0, q))), apply(a, omega)),
                  "channel implements the positive vacuum response semigroup with q=exp(-t/2)")
            equal(vacuum_expectation(omega, actual), vacuum_expectation(omega, a), "Kraus channel fixes the vacuum state")
            channel_count += 1
    for (q, _), (r, _) in product(triples, repeat=2):
        for a in all_observables(2):
            equal(explicit_channel(explicit_channel(a, q), r), explicit_channel(a, q*r),
                  "amplitude-damping composition multiplies the survival amplitude")
            composition_count += 1
    equal((channel_count, composition_count), (18, 54), "amplitude-damping check counts")

    p1 = unit(2, 1, 1)
    dephasing_jumps = (p1,)
    dephasing_k = response(dephasing_jumps)
    equal(dephasing_k, k, "amplitude damping and dephasing have the same positive vacuum response K")
    equal(apply(p1, omega), (pc.C(), pc.C()), "dephasing jump is dark on the same vacuum")
    equal(generator(jumps, k, p1), pc.scale(p1, -1), "damping changes the excited-state projection")
    equal(generator(dephasing_jumps, dephasing_k, p1), zero(2), "dephasing fixes the excited-state projection")
    for a in all_observables(2):
        equal(apply(generator(jumps, k, a), omega),
              apply(generator(dephasing_jumps, dephasing_k, a), omega),
              "different whole generators induce the same generator on the q(A)=A Omega carrier")
        for q, _ in triples:
            dephased = pc.matrix(((a[0][0], q*a[0][1]), (q*a[1][0], a[1][1])))
            equal(apply(dephased, omega), apply(explicit_channel(a, q), omega),
                  "dephasing and damping semigroups have the same vacuum-column return")
    for q, _ in triples:
        image = explicit_channel(p1, q)
        defect = pc.sub(explicit_channel(pc.multiply(p1, p1), q), pc.multiply(image, image))
        equal(defect, pc.scale(p1, q*q*(1-q*q)), "Kraus damping is not multiplicative on the excited-state projection")
        require(q*q*(1-q*q) > 0, "each tested damping multiplicative defect is genuinely nonzero")
        pc.positive_semidefinite(defect)

    clock_product_count = 0
    for phase in (pc.C(F(3, 5), F(4, 5)), pc.C(0, -1)):
        u = pc.matrix(((1, 0), (0, phase)))
        equal(pc.multiply(pc.adjoint(u), u), pc.I, "clock phase matrix is exactly unitary")
        equal(apply(u, omega), omega, "unitary clock fixes the vacuum")

        def alpha(a):
            return pc.multiply(pc.multiply(pc.adjoint(u), a), u)

        for a in all_observables(2):
            equal(alpha(pc.adjoint(a)), pc.adjoint(alpha(a)), "Heisenberg clock preserves adjoints")
            equal(apply(alpha(a), omega), apply(pc.adjoint(u), apply(a, omega)),
                  "q(alpha(A))=U* A Omega has the declared opposite Heisenberg sign")
            equal(vacuum_expectation(omega, alpha(a)), vacuum_expectation(omega, a), "clock automorphism preserves the vacuum state")
            for b in all_observables(2):
                equal(alpha(pc.multiply(a, b)), pc.multiply(alpha(a), alpha(b)),
                      "unitary Heisenberg clock is an algebra automorphism, unlike the damping channel")
                clock_product_count += 1
    equal(clock_product_count, 72, "exact clock product count")

    qutrit_jumps, qutrit_omega = finite_fixtures()[1]
    cosine, sine = F(3, 5), F(4, 5)
    equal(cosine*cosine+sine*sine, 1, "rational channel-label rotation is orthogonal")
    mixed_jumps = (pc.add(pc.scale(qutrit_jumps[0], cosine), pc.scale(qutrit_jumps[1], sine)),
                   pc.add(pc.scale(qutrit_jumps[0], -sine), pc.scale(qutrit_jumps[1], cosine)))
    require(mixed_jumps != qutrit_jumps, "channel-label rotation is nontrivial")
    qutrit_k = response(qutrit_jumps)
    equal(response(mixed_jumps), qutrit_k, "orthogonal channel-label mixing preserves K")
    for l in mixed_jumps:
        equal(apply(l, qutrit_omega), (pc.C(),)*3, "mixed jumps remain dark")
    for a in all_observables(3):
        equal(generator(mixed_jumps, qutrit_k, a), generator(qutrit_jumps, qutrit_k, a),
              "orthogonal mixing preserves the complete whole generator, not just its vacuum return")
    print("PASS: three Kraus channels and 54 compositions distinguish damping from same-K dephasing; 72 clock products are automorphic, and 11 qutrit probes preserve the whole generator under orthogonal label mixing.")


def entangled_dark_vacuum():
    original, u, jumps, omega = entangled_fixture()
    equal(pc.multiply(pc.adjoint(u), u), pc.identity(4), "declared two-qubit conjugation is unitary")
    rho = projector(omega)
    equal(pc.multiply(rho, rho), rho, "entangled dark state is pure")
    reduced = pc.matrix([[sum(rho[2*i+b][2*j+b] for b in range(2)) for j in range(2)] for i in range(2)])
    equal(reduced, pc.matrix(((F(9, 25), 0), (0, F(16, 25)))), "entangled dark vacuum has a strictly mixed one-qubit marginal")
    require(pc.real(pc.determinant(reduced)) > 0, "pure two-qubit dark vacuum is entangled")
    k0, k = response(original), response(jumps)
    equal(k0, pc.matrix(((0, 0, 0, 0), (0, F(1, 2), 0, 0),
                         (0, 0, F(1, 2), 0), (0, 0, 0, 1))), "product damping response has the declared finite spectrum")
    equal(k, pc.multiply(pc.multiply(u, k0), pc.adjoint(u)), "entangled response is unitarily conjugate to the product response")
    for a in all_observables(4):
        transported_a = pc.multiply(pc.multiply(u, a), pc.adjoint(u))
        equal(generator(jumps, k, transported_a),
              pc.multiply(pc.multiply(u, generator(original, k0, a)), pc.adjoint(u)),
              "entangled generator intertwines under the declared global conjugation")

    # These defects cross the two opposed tensor factors. They are not
    # nonzero dark operators belonging to one faithful local factor alone.
    schmidt_root = pc.matrix(((F(3, 5), 0), (0, F(4, 5))))
    inverse_root = pc.matrix(((F(5, 3), 0), (0, F(5, 4))))
    units = tuple(unit(2, i, j) for i, j in product(range(2), repeat=2))

    def plain_transpose(a):
        return [[a[j][i] for j in range(len(a))] for i in range(len(a))]

    def mirror(a):
        return pc.multiply(pc.multiply(schmidt_root, plain_transpose(a)), inverse_root)

    defects, local_vectors = [], []
    for a in units:
        defect = pc.sub(tensor(a, pc.I), tensor(pc.I, mirror(a)))
        equal(apply(defect, omega), (pc.C(),)*4, "Schmidt-mirror defect annihilates the entangled vacuum")
        defects.append(defect)
        local_vectors.append(apply(tensor(a, pc.I), omega))
    for a, b in product(units, repeat=2):
        equal(mirror(pc.multiply(a, b)), pc.multiply(mirror(b), mirror(a)),
              "Schmidt mirror reverses all 16 matrix-unit products")
    equal(mirror(pc.scale(unit(2, 0, 1), pc.C(0, 1))), pc.scale(mirror(unit(2, 0, 1)), pc.C(0, 1)),
          "Schmidt mirror uses complex-linear transpose, not conjugate transpose")
    equal(mirror(unit(2, 0, 1)), pc.scale(unit(2, 1, 0), F(4, 3)), "unequal-weight mirror factor")
    equal(mirror(unit(2, 1, 0)), pc.scale(unit(2, 0, 1), F(3, 4)), "oppositely weighted mirror factor")
    require(mirror(pc.adjoint(unit(2, 0, 1))) != pc.adjoint(mirror(unit(2, 0, 1))),
            "unequal-Schmidt mirror is not a star-preserving map")
    mirror_response = response(tuple(defects))
    pc.positive_semidefinite(mirror_response)
    equal(apply(mirror_response, omega), (pc.C(),)*4, "positive mirror response has the entangled vacuum in its kernel")
    sparse_mirror_response = {(i, j): pc.real(value) for i, row in enumerate(mirror_response)
                              for j, value in enumerate(row) if value != pc.C()}
    equal(sparse_rank(sparse_mirror_response, 4), 3, "four opposed-factor defects have exactly one common vacuum line")
    local_gram = pc.matrix([[inner(a, b) for b in local_vectors] for a in local_vectors])
    weights = (F(9, 25), F(16, 25))
    equal(local_gram, pc.matrix([[weights[i % 2] if i == j else 0 for j in range(4)] for i in range(4)]),
          "local matrix-unit vectors have strictly positive Schmidt-weight Gram matrix")
    require(pc.real(pc.determinant(local_gram)) > 0,
            "faithful marginal makes A -> (A tensor I)Omega injective on the full local matrix carrier")

    bell_vector = (pc.C(1), pc.C(), pc.C(), pc.C(1))
    bell_projector = pc.scale(projector(bell_vector), F(1, 2))
    equal(pc.multiply(bell_projector, bell_projector), bell_projector, "normalized Bell projector uses no irrational amplitude")
    uniform_defects = tuple(pc.sub(tensor(a, pc.I), tensor(pc.I, plain_transpose(a))) for a in units)
    for defect in uniform_defects:
        equal(apply(defect, bell_vector), (pc.C(),)*4, "uniform-Schmidt defect is dark on the Bell line")
    equal(response(uniform_defects), pc.scale(pc.sub(pc.identity(4), bell_projector), 2),
          "uniform four-defect response is exactly 2(I-P_Bell)")
    print("PASS: the entangled vacuum and 18 conjugated generators admit four opposed-factor Schmidt defects with rank-three response; 16 mirror products, local faithfulness and the uniform identity K=2(I-P_Bell) are exact.")


# Sparse rational operators below act on the full 2^N-dimensional tensor
# carrier; basis bit j records the state of qubit j.
def sparse_add(*operators):
    result = {}
    for operator in operators:
        for entry, value in operator.items():
            result[entry] = result.get(entry, F(0))+value
    return {entry: value for entry, value in result.items() if value}


def sparse_scale(c, operator):
    return {entry: F(c)*value for entry, value in operator.items() if c*value}


def sparse_adjoint(operator):
    return {(j, i): value for (i, j), value in operator.items()}


def sparse_multiply(a, b):
    rows_b = {}
    for (i, j), value in b.items():
        rows_b.setdefault(i, []).append((j, value))
    result = {}
    for (i, k), left in a.items():
        for j, right in rows_b.get(k, ()):
            result[i, j] = result.get((i, j), F(0))+left*right
    return {entry: value for entry, value in result.items() if value}


def sparse_identity(dimension):
    return {(j, j): F(1) for j in range(dimension)}


def sparse_apply(a, vector):
    result = [F(0)]*len(vector)
    for (i, j), value in a.items():
        result[i] += value*vector[j]
    return tuple(result)


def sparse_commutator(a, b):
    return sparse_add(sparse_multiply(a, b), sparse_scale(-1, sparse_multiply(b, a)))


def real_inner(a, b):
    return sum(x*y for x, y in zip(a, b))


def sparse_rank(a, dimension):
    rows = [[a.get((i, j), F(0)) for j in range(dimension)] for i in range(dimension)]
    rank = 0
    for column in range(dimension):
        pivot = next((i for i in range(rank, dimension) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale_factor = rows[rank][column]
        rows[rank] = [value/scale_factor for value in rows[rank]]
        for i in range(rank+1, dimension):
            if rows[i][column]:
                coefficient = rows[i][column]
                rows[i] = [x-coefficient*y for x, y in zip(rows[i], rows[rank])]
        rank += 1
    return rank


def site_operator(n, j, kind):
    dimension, mask = 1 << n, 1 << j
    if kind == "lower":
        return {(x ^ mask, x): F(1) for x in range(dimension) if x & mask}
    if kind == "X":
        return {(x ^ mask, x): F(1) for x in range(dimension)}
    if kind == "Z":
        return {(x, x): F(-1 if x & mask else 1) for x in range(dimension)}
    if kind == "plus_minus":
        result = {}
        for x in range(dimension):
            value = F(-1 if x & mask else 1, 2)
            for output_bit in (0, 1):
                result[(x & ~mask) | (output_bit << j), x] = value
        return result
    raise ValueError("unknown exact on-site operator")


@lru_cache(None)
def local_chain(n):
    annihilators = tuple(site_operator(n, j, "lower") for j in range(n))
    jumps = (annihilators[0],)+tuple(sparse_add(annihilators[j], sparse_scale(-1, annihilators[j+1])) for j in range(n-1))
    k = sparse_scale(F(1, 2), sparse_add(*(sparse_multiply(sparse_adjoint(l), l) for l in jumps)))
    return annihilators, jumps, k


def local_chain_kernel_and_support():
    support_count = 0
    for n in range(1, 6):
        dimension = 1 << n
        omega = (F(1),)+(F(0),)*(dimension-1)
        annihilators, jumps, k = local_chain(n)
        for index, l in enumerate(jumps):
            equal(sparse_apply(l, omega), (F(0),)*dimension, "actual tensor-local jumps annihilate the product vacuum")
            support = {0} if index == 0 else {index-1, index}
            for j in range(n):
                if j not in support:
                    for kind in ("X", "Z"):
                        equal(sparse_commutator(l, site_operator(n, j, kind)), {}, "declared local jump commutes with generators outside its tensor support")
                        support_count += 1
        # The coefficient recursion recovers every on-site lowering operator
        # from the anchor and differences. Their common kernel is the vacuum.
        recovered = jumps[0]
        equal(recovered, annihilators[0], "anchor lowering operator")
        for j in range(1, n):
            recovered = sparse_add(recovered, sparse_scale(-1, jumps[j]))
            equal(recovered, annihilators[j], "local differences recover the next on-site lowering operator")
        equal(k, sparse_adjoint(k), "full chain response is self-adjoint")
        equal(sparse_apply(k, omega), (F(0),)*dimension, "full chain vacuum is in the response kernel")
        equal(sparse_rank(k, dimension), dimension-1, "exact full-carrier rank leaves only the dark vacuum")
        require(all(i.bit_count() == j.bit_count() for i, j in k), "full response preserves total excitation count")
    equal(support_count, 60, "outside-support commutator count")
    print("PASS: five actual local spin chains have a unique dark-vacuum response kernel; K preserves excitation count, and the jumps satisfy 60 exact outside-support commutators.")


def one_excitation_trials():
    for n in range(1, 6):
        dimension = 1 << n
        _, _, k = local_chain(n)
        compressed = {(i, j): k.get((1 << i, 1 << j), F(0)) for i in range(n) for j in range(n)}
        expected = {}
        for i, j in product(range(n), repeat=2):
            expected[i, j] = F((1 if i == n-1 else 2) if i == j else (-1 if abs(i-j) == 1 else 0), 2)
        equal(compressed, expected, "one-excitation compression is the anchored Dirichlet-Neumann half Laplacian")
        uniform = tuple(F(int(x != 0 and x.bit_count() == 1)) for x in range(dimension))
        ramp_list = [F(0)]*dimension
        for j in range(n):
            ramp_list[1 << j] = F(j+1)
        ramp = tuple(ramp_list)
        equal(real_inner(uniform, sparse_apply(k, uniform))/real_inner(uniform, uniform), F(1, 2*n), "constant one-excitation trial quotient")
        quotient = real_inner(ramp, sparse_apply(k, ramp))/real_inner(ramp, ramp)
        equal(quotient, F(3, (n+1)*(2*n+1)), "ramp trial has the exact inverse-square-scale Rayleigh quotient")
        require(n*n*quotient < F(3, 2), "tested ramp quotients respect the uniform inverse-square upper envelope")
    print("PASS: five independent one-excitation compressions give constant quotient 1/(2N) and ramp quotient 3/((N+1)(2N+1)); these are variational upper bounds, not numerical eigenvalues.")


def jordan_wigner_identity():
    pair_count = 0
    for n in range(1, 6):
        dimension = 1 << n
        annihilators, _, k = local_chain(n)
        fermions = []
        prefix = sparse_identity(dimension)
        for j in range(n):
            fermions.append(sparse_multiply(prefix, annihilators[j]))
            prefix = sparse_multiply(prefix, site_operator(n, j, "Z"))
        for i, j in product(range(n), repeat=2):
            equal(sparse_add(sparse_multiply(fermions[i], sparse_adjoint(fermions[j])),
                             sparse_multiply(sparse_adjoint(fermions[j]), fermions[i])),
                  sparse_identity(dimension) if i == j else {}, "exact CAR with adjoints")
            equal(sparse_add(sparse_multiply(fermions[i], fermions[j]), sparse_multiply(fermions[j], fermions[i])),
                  {}, "exact CAR annihilator anticommutator")
            pair_count += 1
        reconstructed = {}
        for i, j in product(range(n), repeat=2):
            coefficient = k.get((1 << i, 1 << j), F(0))
            if coefficient:
                reconstructed = sparse_add(reconstructed, sparse_scale(coefficient, sparse_multiply(sparse_adjoint(fermions[i]), fermions[j])))
        equal(reconstructed, k, "full tensor-local response equals the CAR quadratic form of its one-particle compression")
    equal(pair_count, 55, "CAR index-pair count")
    print("PASS: 55 exact CAR index pairs and five full-carrier reconstructions identify the anchored spin response with its quadratic fermionic realization.")


def graph_cluster_family():
    eigenvector_count, marginal_count, support_count = 0, 0, 0
    for n in range(2, 5):
        dimension = 1 << n
        phases = tuple(F((-1)**sum(((x >> j) & 1)*((x >> (j+1)) & 1) for j in range(n-1))) for x in range(dimension))

        def cz_conjugate(operator):
            return {entry: phases[entry[0]]*value*phases[entry[1]] for entry, value in operator.items()}

        stabilizers, jumps = [], []
        for j in range(n):
            neighbors = {i for i in (j-1, j+1) if 0 <= i < n}
            s = site_operator(n, j, "X")
            for neighbor in neighbors:
                s = sparse_multiply(s, site_operator(n, neighbor, "Z"))
            stabilizers.append(s)
            equal(s, cz_conjugate(site_operator(n, j, "X")), "cluster stabilizer is the conjugated on-site X")
            equal(sparse_multiply(s, s), sparse_identity(dimension), "each cluster stabilizer squares to identity")
            l = cz_conjugate(site_operator(n, j, "plus_minus"))
            jumps.append(l)
            equal(sparse_apply(l, phases), (F(0),)*dimension, "local cluster jump annihilates the unnormalized entangled vacuum")
            for outside in set(range(n))-{j}-neighbors:
                for kind in ("X", "Z"):
                    equal(sparse_commutator(l, site_operator(n, outside, kind)), {}, "cluster jump has only closed-star support")
                    support_count += 1
        for s, t in product(stabilizers, repeat=2):
            equal(sparse_commutator(s, t), {}, "cluster stabilizers commute")
        k = sparse_scale(F(1, 2), sparse_add(*(sparse_multiply(sparse_adjoint(l), l) for l in jumps)))
        expected_k = sparse_scale(F(1, 4), sparse_add(sparse_scale(n, sparse_identity(dimension)), sparse_scale(-1, sparse_add(*stabilizers))))
        equal(k, expected_k, "cluster response is one quarter the sum of stabilizer defects")
        equal(real_inner(phases, phases), dimension, "unnormalized cluster vacuum has squared norm 2^N")
        eigenvectors = []
        for word in range(dimension):
            vector = tuple(phases[x]*((-1)**((word & x).bit_count())) for x in range(dimension))
            equal(sparse_apply(k, vector), tuple(F(word.bit_count(), 2)*value for value in vector),
                  "signed Walsh vectors have exact half-integer excitation energies")
            eigenvectors.append(vector)
            eigenvector_count += 1
        for i, j in product(range(dimension), repeat=2):
            equal(real_inner(eigenvectors[i], eigenvectors[j]), dimension if i == j else 0,
                  "complete exact orthogonal cluster eigenbasis")
        equal(sparse_rank(k, dimension), dimension-1, "cluster kernel is exactly the vacuum line")
        require(min(F(word.bit_count(), 2) for word in range(1, dimension)) == F(1, 2),
                "all tested cluster systems have the same gap one half")
        for j in range(n):
            marginal = [[F(0), F(0)], [F(0), F(0)]]
            mask = 1 << j
            for x in range(dimension):
                if x & mask:
                    continue
                for a, b in product((0, 1), repeat=2):
                    marginal[a][b] += phases[x | (a << j)]*phases[x | (b << j)]/dimension
            equal(marginal, [[F(1, 2), F(0)], [F(0), F(1, 2)]], "every non-isolated cluster site has maximally mixed marginal")
            marginal_count += 1
    equal((eigenvector_count, marginal_count, support_count), (28, 9, 16), "cluster basis, marginal and support counts")
    print("PASS: three actual path-cluster systems have commuting stabilizers, 28 complete eigenvectors, nine maximally mixed marginals and local jumps; each finite gap is exactly 1/2.")


def main():
    pure_dark_vacuum_identities()
    amplitude_damping_return()
    entangled_dark_vacuum()
    local_chain_kernel_and_support()
    one_excitation_trials()
    jordan_wigner_identity()
    graph_cluster_family()
    print("All seven check groups passed. Exact rational arithmetic; stdlib only; stdout only; no files written.")
    print("Finite identities and trial quotients do not establish a thermodynamic or continuum limit, a relativistic net, physical scale selection, or a Yang--Mills mass gap.")


if __name__ == "__main__":
    main()
