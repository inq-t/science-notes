"""Exact, stdlib, stdout-only checks for a finite spectral transition return.

R=C^2, K=C^3, J e0=e0, J e1=(3e1+4e2)/5 and H=diag(0,1,2).
Positive rational q represents exp(-t), so q^H has rational entries.
The atom/source null quotient is distinct from a coefficient algebra
action; transition operators act on the completed preparation carrier.

Exact Gaussian-rational matrices, vectors and ranks reuse guarded local
receipts. No files, network, external dependencies, random sampling, eigensolvers
or transcendental approximations are used. This finite fixture supplies
neither physical locality, a relativistic net nor a new mass-gap theorem.
"""

from fractions import Fraction as F
from itertools import product

import positive_cone_process_receipt as pc
import vacuum_loss_receipt as vl
from context_transport_receipt import equal, require


J = pc.matrix(((1, 0), (0, F(3, 5)), (0, F(4, 5))))
H = pc.matrix(((0, 0, 0), (0, 1, 0), (0, 0, 2)))
EFFECTS = (pc.matrix(((1, 0), (0, 0))),
           pc.matrix(((0, 0), (0, F(9, 25)))),
           pc.matrix(((0, 0), (0, F(16, 25)))))


def vector(*values):
    return tuple(pc.C.cast(value) for value in values)


def basis(n, j):
    return tuple(pc.C(int(i == j)) for i in range(n))


def outer(u, v):
    return pc.matrix([[a*b.conjugate() for b in v] for a in u])


def heat(q):
    return pc.matrix(((1, 0, 0), (0, q, 0), (0, 0, q*q)))


def readout(q):
    return pc.matrix(((1, 0), (0, (9*q+16*q*q)/25)))


def prepare(q, xi):
    return vl.apply(heat(q), vl.apply(J, xi))


def source_probes():
    return (basis(2, 0), basis(2, 1), vector(1, pc.C(0, 1)),
            vector(pc.C(F(1, 2), F(1, 3)), pc.C(F(-2, 5), F(3, 7))))


def preparation_basis():
    records = ((F(1), basis(2, 0)), (F(1), basis(2, 1)), (F(1, 2), basis(2, 1)))
    return records, tuple(prepare(q, xi) for q, xi in records)


def spectral_readout_and_kernel():
    equal(pc.multiply(pc.adjoint(J), J), pc.I, "declared source embedding is isometric")
    projectors = tuple(vl.unit(3, i, i) for i in range(3))
    equal(vl.matrix_sum(projectors, 3), pc.identity(3), "whole spectral projectors resolve identity")
    for i, p in enumerate(projectors):
        equal(pc.multiply(pc.multiply(pc.adjoint(J), p), J), EFFECTS[i], "spectral compression has the stated exact effect")
        pc.positive_semidefinite(EFFECTS[i])
    equal(vl.matrix_sum(EFFECTS, 2), pc.I, "retained spectral measure is normalized")
    require(pc.multiply(EFFECTS[1], EFFECTS[1]) != EFFECTS[1], "nonzero-energy effect is not a projection")
    equal(vl.matrix_sum((pc.scale(p, i) for i, p in enumerate(projectors)), 3), H,
          "whole energy labels are the declared zero, one and two")
    parameters = (F(1), F(1, 2), F(2, 3))
    kernel_count = 0
    for q in parameters:
        equal(pc.multiply(pc.multiply(pc.adjoint(J), heat(q)), J), readout(q), "actual heat readout has coefficient (9q+16q^2)/25")
        for r in parameters:
            for xi, eta in product(source_probes(), repeat=2):
                equal(vl.inner(prepare(q, xi), prepare(r, eta)),
                      vl.inner(xi, vl.apply(readout(q*r), eta)),
                      "preparation Gram kernel is the readout at the product parameter")
                kernel_count += 1
    equal(kernel_count, 144, "complex preparation-kernel count")
    defect = pc.sub(readout(F(1, 4)), pc.multiply(readout(F(1, 2)), readout(F(1, 2))))
    equal(defect, pc.matrix(((0, 0), (0, F(9, 625)))), "readout alone is not a heat semigroup")
    print("PASS: the isometry and three spectral effects give 144 exact complex preparation-Gram identities; the compressed readout is not a semigroup.")


def atom_source_null_quotient():
    # Columns are [{0},e0], [{0},e1], [{1},e0], [{1},e1],
    # [{2},e0], [{2},e1]. They map to P_E J xi in the whole carrier.
    quotient = pc.matrix(((1, 0, 0, 0, 0, 0),
                          (0, 0, 0, F(3, 5), 0, 0),
                          (0, 0, 0, 0, 0, F(4, 5))))
    for atom, source_index in product(range(3), range(2)):
        equal(vl.apply(quotient, basis(6, 2*atom+source_index)),
              vl.apply(vl.unit(3, atom, atom), vl.apply(J, basis(2, source_index))),
              "each formal atom/source coordinate maps to its actual spectral preparation")
    gram = pc.multiply(pc.adjoint(quotient), quotient)
    equal(gram, pc.matrix([[value if i == j else 0 for j in range(6)]
                           for i, value in enumerate((1, 0, 0, F(9, 25), 0, F(16, 25)))]),
          "finite atom/source Gram exposes its null coordinates exactly")
    source_x, source_z = pc.PAULI[0], pc.PAULI[2]
    coefficient_x = vl.tensor(pc.identity(3), source_x)
    coefficient_z = vl.tensor(pc.identity(3), source_z)
    null_symbol = basis(6, 1)
    equal(vl.apply(quotient, null_symbol), vector(0, 0, 0), "[{0},e1] is a null spectral symbol")
    bad_image = vl.apply(quotient, vl.apply(coefficient_x, null_symbol))
    equal(bad_image, basis(3, 0), "coefficient flip sends a null symbol to the vacuum")
    equal(vl.inner(bad_image, bad_image), pc.C(1), "failed coefficient descent produces norm one")
    descended_z = pc.matrix(((1, 0, 0), (0, -1, 0), (0, 0, -1)))
    equal(pc.multiply(quotient, coefficient_z), pc.multiply(descended_z, quotient),
          "diagonal coefficient action has a well-defined full quotient intertwiner")
    equal(pc.multiply(descended_z, descended_z), pc.identity(3), "descended diagonal coefficient action is an involution")
    for i in (1, 2, 4):
        equal(vl.apply(quotient, vl.apply(coefficient_z, basis(6, i))), vector(0, 0, 0),
              "diagonal coefficient action preserves every null basis direction")
    print("PASS: the exact atom/source null quotient rejects the source flip but admits the diagonal coefficient action; preserving a source label is not automatic descent.")


def canonical_corner():
    def corner(a):
        return pc.multiply(pc.multiply(J, a), pc.adjoint(J))

    probes = vl.all_observables(2)
    product_count = 0
    for a in probes:
        equal(corner(pc.adjoint(a)), pc.adjoint(corner(a)), "canonical corner preserves adjoints")
        equal(pc.multiply(corner(a), J), pc.multiply(J, a), "corner action agrees on embedded source vectors")
        for b in probes:
            equal(corner(pc.multiply(a, b)), pc.multiply(corner(a), corner(b)), "canonical corner preserves all tested products")
            product_count += 1
    p = corner(pc.I)
    equal(p, pc.multiply(J, pc.adjoint(J)), "corner unit is exactly JJ*")
    equal(pc.multiply(p, p), p, "corner unit is a projection")
    equal(pc.real(pc.trace(p)), 2, "corner unit has rank two")
    require(p != pc.identity(3), "canonical M2 corner is nonunital in the full preparation algebra")
    require(pc.sub(pc.identity(3), p) != vl.zero(3), "preparation carrier has a direction outside the initial corner")
    equal(product_count, 36, "corner product count")
    print("PASS: 36 canonical corner products and their adjoints are preserved, but the returned unit is JJ*, not the identity on the three-dimensional preparation carrier.")


def transition_products_and_full_span():
    records, preparations = preparation_basis()
    columns = pc.matrix([[preparations[j][i] for j in range(3)] for i in range(3)])
    equal(pc.determinant(columns), pc.C(F(-3, 25)), "three preparation vectors are linearly independent")
    gram = pc.matrix([[vl.inner(u, v) for v in preparations] for u in preparations])
    for i, j in product(range(3), repeat=2):
        q, xi = records[i]
        r, eta = records[j]
        equal(gram[i][j], vl.inner(xi, vl.apply(readout(q*r), eta)), "transition coefficient is the same readout Gram kernel")
    transitions = {(i, j): outer(preparations[i], preparations[j]) for i, j in product(range(3), repeat=2)}
    for (i, j), theta in transitions.items():
        equal(pc.adjoint(theta), transitions[j, i], "transition adjoint reverses its preparation labels")
        for (k, l), other in transitions.items():
            equal(pc.multiply(theta, other), pc.scale(transitions[i, l], gram[j][k]),
                  "transition multiplication contracts the middle preparation labels by the readout Gram")
    flattened = {}
    for column, theta in enumerate(transitions.values()):
        for row, value in enumerate(value for line in theta for value in line):
            if value != pc.C():
                flattened[row, column] = pc.real(value)
    equal(vl.sparse_rank(flattened, 9), 9, "nine rank-one transitions span the complete complex M3 carrier")
    # Real matrix entries still constitute a complex basis after scalar
    # extension; exact rank nine proves there is no missing matrix direction.
    print("PASS: three preparation vectors have determinant -3/25; their nine transitions span M3 and satisfy all 81 exact Gram-contracted products and adjoint identities.")


def common_clock_on_transitions():
    _, preparations = preparation_basis()
    transitions = tuple(outer(u, v) for u, v in product(preparations, repeat=2))
    corner_unit = pc.multiply(J, pc.adjoint(J))
    for z in (pc.C(F(3, 5), F(4, 5)), pc.C(0, -1)):
        equal(z*z.conjugate(), pc.C(1), "Gaussian-rational phase has modulus one")
        clock = pc.matrix(((1, 0, 0), (0, z, 0), (0, 0, z*z)))
        equal(pc.multiply(clock, pc.adjoint(clock)), pc.identity(3), "common spectral clock is unitary")

        def evolve(a):
            return pc.multiply(pc.multiply(clock, a), pc.adjoint(clock))

        for u, v in product(preparations, repeat=2):
            theta = outer(u, v)
            evolved = evolve(theta)
            equal(evolved, outer(vl.apply(clock, u), vl.apply(clock, v)), "clock conjugation transports both preparation labels")
            equal(evolve(pc.adjoint(theta)), pc.adjoint(evolved), "clock conjugation preserves the transition adjoint")
            expected_norm2 = vl.inner(u, u)*vl.inner(v, v)
            equal(pc.trace(pc.multiply(pc.adjoint(theta), theta)), expected_norm2,
                  "rank-one Hilbert-Schmidt norm equals squared operator norm")
            equal(pc.trace(pc.multiply(pc.adjoint(evolved), evolved)), expected_norm2,
                  "common clock preserves the exact rank-one operator norm")
        for a, b in product(transitions, repeat=2):
            equal(evolve(pc.multiply(a, b)), pc.multiply(evolve(a), evolve(b)), "common clock preserves all transition products")
        require(evolve(corner_unit) != corner_unit, "initial source corner need not be invariant under the full common clock")
    print("PASS: two exact spectral phases preserve all transition products, adjoints and rank-one norms by unitary conjugation, while the initial source corner is not invariant.")


def locality_and_vacuum_column():
    omega, e1, e2 = basis(3, 0), basis(3, 1), basis(3, 2)
    a = pc.add(outer(e1, omega), outer(omega, e1))
    b = pc.add(outer(e2, omega), outer(omega, e2))
    equal(a, pc.adjoint(a), "first vacuum transition is Hermitian")
    equal(b, pc.adjoint(b), "second vacuum transition is Hermitian")
    equal(vl.inner(e1, e2), pc.C(), "created carrier vectors are orthogonal")
    actual = vl.commutator(a, b)
    expected = pc.sub(outer(e1, e2), outer(e2, e1))
    equal(actual, expected, "orthogonal vacuum transitions need not commute as operators")
    require(actual != vl.zero(3), "vacuum-transition commutator is genuinely nonzero")
    equal(vl.apply(actual, omega), vector(0, 0, 0), "the nonzero commutator nevertheless annihilates the vacuum")
    equal(vl.vacuum_expectation(omega, pc.multiply(a, b)), pc.C(), "one ordered vacuum two-point value vanishes")
    equal(vl.vacuum_expectation(omega, pc.multiply(b, a)), pc.C(), "the opposite ordered vacuum two-point value also vanishes")
    print("PASS: two Hermitian transitions create orthogonal vectors yet have a nonzero commutator that kills the vacuum; carrier orthogonality is not physical locality.")


def main():
    spectral_readout_and_kernel()
    atom_source_null_quotient()
    canonical_corner()
    transition_products_and_full_span()
    common_clock_on_transitions()
    locality_and_vacuum_column()
    print("All six check groups passed. Exact rational arithmetic; stdlib only; stdout only; no files written.")
    print("Finite spectral reconstruction and transition closure do not establish physical locality, a spacetime net, a selected clock scale, or a new mass-gap theorem.")


if __name__ == "__main__":
    main()
