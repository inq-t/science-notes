"""Exact finite checks for modular mirrors, inclusions and spectral return.

The carrier is the matrix Hilbert space with unnormalized HS inner product.
D_A(T)=A T-T R^-1 A R, with R proportional to sqrt(rho). Common scalar
factors in R cancel. The canonical correlated state is diag(9,1,1,9)/20.
Its isometry is represented by an integer matrix W with W*W=10 I, so every
compressed Gram uses W*(.)W/10; no irrational square root is approximated.

The product control has R=diag(3,4,3,4), rho=R^2/50 and W*W=25 I.
The correlated fixture and product comparison are the ones documented in
algebra/expected-inclusions-and-mirror-clock-consistency.md (EI16--EI20).
Sparse rational operators and exact Gaussian-rational matrix helpers are
reused from guarded local receipts. Powers of rational q encode exact heat
values after the explicitly specified exponential parameterization.

No files, network, external dependencies, Monte Carlo, eigensolvers or
transcendental fits are used. Finite checks do not establish unbounded
domains, continuum/QFT realization, physical scale selection or a mass gap.
"""

from fractions import Fraction as F
from itertools import product

import positive_cone_process_receipt as pc
import vacuum_loss_receipt as vl
from context_transport_receipt import equal, require


def diagonal(values):
    return pc.matrix([[value if i == j else 0 for j in range(len(values))]
                      for i, value in enumerate(values)])


def hs_inner(a, b):
    return pc.trace(pc.multiply(pc.adjoint(a), b))


def mirror_action(a, t, root, inverse):
    twisted = pc.multiply(pc.multiply(inverse, a), root)
    return pc.sub(pc.multiply(a, t), pc.multiply(t, twisted))


def mirror_adjoint_action(a, t, root, inverse):
    astar = pc.adjoint(a)
    twisted = pc.multiply(pc.multiply(root, astar), inverse)
    return pc.sub(pc.multiply(astar, t), pc.multiply(t, twisted))


def matrix_units(n):
    return tuple(vl.unit(n, i, j) for i, j in product(range(n), repeat=2))


def finite_modular_mirror():
    action_count, adjoint_count = 0, 0
    for roots in ((F(3, 5), F(4, 5)), (F(1, 3), F(2, 3), F(2, 3))):
        n = len(roots)
        root, inverse = diagonal(roots), diagonal(tuple(1/r for r in roots))
        equal(pc.real(hs_inner(root, root)), 1, "finite root defines a faithful normalized state")
        units = matrix_units(n)
        probes = units+(vl.mixed_probe(n),)
        for a in probes:
            equal(mirror_action(a, root, root, inverse), vl.zero(n), "modular mirror defect kills the state vector")
            for b in probes:
                equal(mirror_action(a, pc.multiply(b, root), root, inverse),
                      pc.multiply(vl.commutator(a, b), root), "mirror on B sqrt(rho) is the ordinary commutator times sqrt(rho)")
                action_count += 1
            for t, s in product(units, repeat=2):
                equal(hs_inner(mirror_action(a, t, root, inverse), s),
                      hs_inner(t, mirror_adjoint_action(a, s, root, inverse)),
                      "HS adjoint uses R A* R^-1, not R^-1 A* R")
                adjoint_count += 1
        a, t = vl.unit(n, 0, 1), pc.identity(n)
        require(mirror_adjoint_action(a, t, root, inverse)
                != mirror_action(pc.adjoint(a), t, root, inverse),
                "nonuniform-state adjoint twist is genuinely different from just conjugating the source")
    equal((action_count, adjoint_count), (125, 890), "finite modular action and adjoint counts")
    print("PASS: two faithful matrix states satisfy 125 cyclic commutator identities and 890 exact HS-adjoint checks, including the nonuniform modular twist.")


# Real HS operators below are sparse matrices on row-major matrix units.
def real_mirror_operator(a, roots):
    n = len(roots)
    result = {}
    for i, j, k in product(range(n), repeat=3):
        left = pc.real(a[i][k])
        right = roots[j]*pc.real(a[k][j])/roots[k]
        if left:
            result = vl.sparse_add(result, {(i*n+j, k*n+j): left})
        if right:
            result = vl.sparse_add(result, {(i*n+j, i*n+k): -right})
    return result


def row_response(operators):
    return vl.sparse_scale(F(1, 2), vl.sparse_add(*(vl.sparse_multiply(vl.sparse_adjoint(d), d) for d in operators)))


def inclusion_data(roots):
    # Local rho_A=I/2, so local mirror ratios are one. The two local source
    # rows are E01 and E10, not the complete matrix-unit row.
    require(roots[0]*roots[0]+roots[1]*roots[1] == roots[2]*roots[2]+roots[3]*roots[3],
            "chosen diagonal state has the declared tracial A marginal")
    normalization = roots[0]*roots[0]+roots[1]*roots[1]
    w = {}
    for i, j, b in product(range(2), range(2), range(2)):
        row, column = (2*i+b)*4+(2*j+b), 2*i+j
        w[row, column] = roots[2*j+b]
    sources = (vl.unit(2, 0, 1), vl.unit(2, 1, 0))
    local_rows = tuple(real_mirror_operator(a, (F(1), F(1))) for a in sources)
    whole_rows = tuple(real_mirror_operator(vl.tensor(a, pc.I), roots) for a in sources)
    return normalization, w, local_rows, whole_rows, row_response(local_rows), row_response(whole_rows)


def compression(operator, w, normalization):
    return vl.sparse_scale(1/normalization, vl.sparse_multiply(vl.sparse_multiply(vl.sparse_adjoint(w), operator), w))


def dense_real(operator, dimension):
    return pc.matrix([[operator.get((i, j), F(0)) for j in range(dimension)] for i in range(dimension)])


def basis_vector(dimension, index):
    return tuple(F(int(j == index)) for j in range(dimension))


def rectangular_apply(operator, vector, target_dimension):
    result = [F(0)]*target_dimension
    for (i, j), value in operator.items():
        result[i] += value*vector[j]
    return tuple(result)


def normalize_squared_moment(operator, vector, norm2):
    return vl.real_inner(vector, vl.sparse_apply(operator, vector))/norm2


def spectral_projections(k, eigenvalues, dimension):
    identity = vl.sparse_identity(dimension)
    projections = []
    for value in eigenvalues:
        p = identity
        for other in eigenvalues:
            if other != value:
                factor = vl.sparse_add(k, vl.sparse_scale(-other, identity))
                p = vl.sparse_scale(1/(value-other), vl.sparse_multiply(p, factor))
        projections.append(p)
    equal(vl.sparse_add(*projections), identity, "Lagrange spectral projectors resolve the identity")
    equal(vl.sparse_add(*(vl.sparse_scale(value, p) for value, p in zip(eigenvalues, projections))), k,
          "exact spectral projectors reconstruct the self-adjoint response")
    for i, p in enumerate(projections):
        equal(vl.sparse_adjoint(p), p, "spectral projector is self-adjoint")
        for j, q in enumerate(projections):
            equal(vl.sparse_multiply(p, q), p if i == j else {}, "spectral projectors are mutually orthogonal")
    return tuple(projections)


def correlated_inclusion_and_second_moment():
    c, w, local_rows, whole_rows, local_k, whole_k = inclusion_data(tuple(map(F, (3, 1, 1, 3))))
    equal(c, 10, "canonical correlated isometry normalization")
    equal(vl.sparse_multiply(vl.sparse_adjoint(w), w), vl.sparse_scale(c, vl.sparse_identity(4)),
          "W/sqrt(10) is an exact HS isometry")

    def partial_trace_b(a):
        return pc.matrix([[sum(a[2*i+b][2*j+b] for b in range(2)) for j in range(2)] for i in range(2)])

    root = diagonal((3, 1, 1, 3))
    for s in matrix_units(4)+(vl.mixed_probe(4),):
        flat_s = tuple(value for row in s for value in row)
        actual = tuple(pc.C.cast(value) for value in rectangular_apply(vl.sparse_adjoint(w), flat_s, 4))
        expected = tuple(value for row in partial_trace_b(pc.multiply(s, root)) for value in row)
        equal(actual, expected, "scaled inclusion adjoint is Tr_B(S R), with the declared factor order")
    rho = pc.scale(pc.multiply(root, root), F(1, 20))
    x = vl.unit(4, 0, 2)
    projected_x = pc.scale(partial_trace_b(pc.multiply(x, rho)), 2)
    projected_xstar = pc.scale(partial_trace_b(pc.multiply(pc.adjoint(x), rho)), 2)
    equal(projected_x, pc.scale(vl.unit(2, 0, 1), F(1, 10)), "correlated GNS coefficient projection on E00,10")
    equal(projected_xstar, pc.scale(vl.unit(2, 1, 0), F(9, 10)), "GNS coefficient projection of the adjoint has a different weight")
    require(projected_xstar != pc.adjoint(projected_x), "correlated GNS coefficient projection is not a conditional expectation preserving adjoints")
    for local, whole in zip(local_rows, whole_rows):
        equal(vl.sparse_multiply(whole, w), vl.sparse_multiply(w, local), "mirror response rows intertwine under the state-preserving inclusion")
    equal(compression(whole_k, w, c), local_k, "first response moment is natural under inclusion")
    local_i = (F(1), F(0), F(0), F(1))
    equal(vl.sparse_apply(local_k, local_i), (F(0),)*4, "local response has the state vector in its kernel")
    equal(vl.sparse_apply(whole_k, rectangular_apply(w, local_i, 16)), (F(0),)*16, "included state vector remains dark")
    p = vl.sparse_scale(1/c, vl.sparse_multiply(w, vl.sparse_adjoint(w)))
    q = vl.sparse_add(vl.sparse_identity(16), vl.sparse_scale(-1, p))
    leak = vl.sparse_multiply(vl.sparse_multiply(q, whole_k), w)
    second = compression(vl.sparse_multiply(whole_k, whole_k), w, c)
    defect = vl.sparse_add(second, vl.sparse_scale(-1, vl.sparse_multiply(local_k, local_k)))
    equal(defect, vl.sparse_scale(1/c, vl.sparse_multiply(vl.sparse_adjoint(leak), leak)),
          "compressed second-moment defect is exactly the positive clock-leak Gram matrix")
    pc.positive_semidefinite(dense_real(defect, 4))
    e01 = basis_vector(4, 1)
    expected_leak = [F(0)]*16
    expected_leak[2], expected_leak[7] = F(4), F(-4, 3)
    equal(rectangular_apply(leak, e01, 16), tuple(expected_leak), "scaled coherence leak is 4 e0-(4/3)e1")
    equal(normalize_squared_moment(local_k, e01, 1), 1, "retained coherence first response moment")
    equal(normalize_squared_moment(second, e01, 1), F(25, 9), "retained coherence second moment")
    equal(normalize_squared_moment(defect, e01, 1), F(16, 9), "canonical coherence leakage variance")
    require(vl.sparse_multiply(whole_k, w) != vl.sparse_multiply(w, local_k),
            "matching first response forms does not make the smaller clock carrier invariant")
    require(any(vl.sparse_multiply(vl.sparse_adjoint(whole), w)
                != vl.sparse_multiply(w, vl.sparse_adjoint(local))
                for local, whole in zip(local_rows, whole_rows)),
            "row naturality does not extend to the adjoint rows in the correlated state")
    print("PASS: the correlated diagonal inclusion intertwines mirror rows and their first response form, but its exact coherence second-moment defect is 16/9.")


def correlated_spectral_return():
    c, w, _, _, local_k, whole_k = inclusion_data(tuple(map(F, (3, 1, 1, 3))))
    eigenvalues = tuple(map(F, (0,)))+(F(5, 9), F(5), F(50, 9))
    projectors = spectral_projections(whole_k, eigenvalues, 16)
    effects = tuple(compression(p, w, c) for p in projectors)
    equal(vl.sparse_add(*effects), vl.sparse_identity(4), "retained spectral effects form a normalized POVM")
    for effect in effects:
        pc.positive_semidefinite(dense_real(effect, 4))
    require(any(vl.sparse_multiply(effect, effect) != effect for effect in effects),
            "retained spectral effects are not a projection-valued measure")
    e01 = basis_vector(4, 1)
    equal(tuple(normalize_squared_moment(effect, e01, 1) for effect in effects),
          (F(0), F(9, 10), F(1, 10), F(0)), "coherence spectral weights occur at 5/9 and 5")
    z = (F(1), F(0), F(0), F(-1))
    equal(tuple(normalize_squared_moment(effect, z, 2) for effect in effects),
          (F(16, 25), F(0), F(0), F(9, 25)), "centered local Z has a genuine zero spectral atom in the whole clock")
    included_z = rectangular_apply(w, z, 16)
    z_b_root = (F(3), F(0), F(0), F(0), F(0), F(-1), F(0), F(0),
                F(0), F(0), F(1), F(0), F(0), F(0), F(0), F(-3))
    equal(vl.sparse_apply(projectors[0], included_z), tuple(F(4, 5)*x for x in z_b_root),
          "zero atom projects onto the correlated opposite-factor Z state")
    equal(normalize_squared_moment(local_k, z, 2), 2, "local Z first response moment remains two")

    def compressed_heat(q):
        # q=exp(-5t/9); the four exact spectral powers are 0,1,9,10.
        return vl.sparse_add(*(vl.sparse_scale(q**degree, effect)
                               for degree, effect in zip((0, 1, 9, 10), effects)))

    for q in (F(2, 3), F(3, 5)):
        heat = compressed_heat(q)
        failure = vl.sparse_add(compressed_heat(q*q), vl.sparse_scale(-1, vl.sparse_multiply(heat, heat)))
        pc.positive_semidefinite(dense_real(failure, 4))
        equal(normalize_squared_moment(failure, e01, 1), F(9, 100)*(q-q**9)**2,
              "coherence heat-compression semigroup defect is an exact positive variance")
        equal(normalize_squared_moment(failure, z, 2), F(144, 625)*(1-q**10)**2,
              "centered-Z heat-compression defect retains the zero spectral atom")
        require(failure != {}, "compressed heat return is not a semigroup")
    print("PASS: exact correlated spectral projectors compress to a nonprojective POVM; centered Z retains zero weight 16/25, and two rational heat returns fail the semigroup law.")


def product_inclusion_control():
    c, w, local_rows, whole_rows, local_k, whole_k = inclusion_data(tuple(map(F, (3, 4, 3, 4))))
    equal(c, 25, "product-state isometry normalization")
    equal(vl.sparse_multiply(vl.sparse_adjoint(w), w), vl.sparse_scale(c, vl.sparse_identity(4)), "product inclusion is isometric")
    for local, whole in zip(local_rows, whole_rows):
        equal(vl.sparse_multiply(whole, w), vl.sparse_multiply(w, local), "product mirror rows intertwine")
        equal(vl.sparse_multiply(vl.sparse_adjoint(whole), w), vl.sparse_multiply(w, vl.sparse_adjoint(local)),
              "product state also intertwines the adjoint rows")
    equal(vl.sparse_multiply(whole_k, w), vl.sparse_multiply(w, local_k), "product inclusion is a reducing clock carrier")
    equal(compression(vl.sparse_multiply(whole_k, whole_k), w, c), vl.sparse_multiply(local_k, local_k),
          "product-state second-moment defect vanishes")
    eigenvalues = (F(0), F(1), F(2))
    whole_projections = spectral_projections(whole_k, eigenvalues, 16)
    local_projections = spectral_projections(local_k, eigenvalues, 4)
    for whole, local in zip(whole_projections, local_projections):
        equal(compression(whole, w, c), local, "product spectral effects remain the local projections")
    for q, r in product((F(2, 3), F(3, 5)), repeat=2):
        hq = vl.sparse_add(*(vl.sparse_scale(q**j, p) for j, p in enumerate(local_projections)))
        hr = vl.sparse_add(*(vl.sparse_scale(r**j, p) for j, p in enumerate(local_projections)))
        hqr = vl.sparse_add(*(vl.sparse_scale((q*r)**j, p) for j, p in enumerate(local_projections)))
        equal(vl.sparse_multiply(hq, hr), hqr, "product-state heat compression obeys the exact semigroup law")
    print("PASS: the product-state control intertwines rows and adjoints, has zero second-moment leakage, and retains projection-valued spectra and an exact heat semigroup.")


def small_spectral_compressions():
    phase = pc.C(F(3, 5), F(4, 5))
    for index, (c, s) in enumerate(((F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(8, 17), F(15, 17)))):
        equal(c*c+s*s, 1, "rational spectral rotation")
        p0 = pc.matrix(((c*c, c*s), (c*s, s*s)))
        p1 = pc.sub(pc.I, p0)
        equal(pc.multiply(p0, p0), p0, "first two-level spectral projector")
        equal(pc.multiply(p1, p1), p1, "second two-level spectral projector")
        equal(pc.multiply(p0, p1), vl.zero(2), "two-level spectral projectors are orthogonal")
        low, high = F(index), F(index+3)
        k = pc.add(pc.scale(p0, low), pc.scale(p1, high))
        first = pc.real(k[0][0])
        second = pc.real(pc.multiply(k, k)[0][0])
        equal(second-first*first, c*c*s*s*(high-low)**2, "generic compressed second moment is the spectral variance")
        equal(second-first*first, pc.real(k[0][1]*k[1][0]), "generic spectral variance equals the orthogonal leakage Gram")
        require(0 < c*c < 1 and 0 < s*s < 1, "rank-one compressed spectral effects are not projections")
        for q in (F(1, 2), F(2, 3)):
            heat = c*c*q**int(low)+s*s*q**int(high)
            heat_twice = c*c*q**int(2*low)+s*s*q**int(2*high)
            equal(heat_twice-heat*heat, c*c*s*s*(q**int(low)-q**int(high))**2,
                  "generic finite heat compression fails multiplicativity by the exact spectral variance")
            require(heat_twice > heat*heat, "tested compressed heat family is not a semigroup")
        # z=exp(-it); integer eigenvalues permit exact Gaussian-rational phases.
        phases = [pc.C(1)]
        for _ in range(int(high)):
            phases.append(phases[-1]*phase)
        full_unitary = pc.add(pc.scale(p0, phases[int(low)]), pc.scale(p1, phases[int(high)]))
        equal(pc.multiply(full_unitary, pc.adjoint(full_unitary)), pc.I, "full finite spectral clock is unitary")
        compressed_phase = full_unitary[0][0]
        require(pc.real(compressed_phase.conjugate()*compressed_phase) < 1,
                "compression of the unitary clock is strictly contractive on the retained line")
    print("PASS: three rational two-level spectral compressions satisfy the exact positive second-moment identity; their effects are nonprojective and neither heat nor unitary compression is an autonomous clock.")


def main():
    finite_modular_mirror()
    correlated_inclusion_and_second_moment()
    correlated_spectral_return()
    product_inclusion_control()
    small_spectral_compressions()
    print("All five check groups passed. Exact rational arithmetic; stdlib only; stdout only; no files written.")
    print("Finite mirror and spectral-return identities do not establish unbounded domains, a physical clock or scale, a QFT limit, or a Yang--Mills mass gap.")


if __name__ == "__main__":
    main()
