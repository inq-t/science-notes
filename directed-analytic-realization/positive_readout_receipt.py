"""Exact finite checks for positive readout of preparation transitions.

The chosen density matrix and the trace pairing are explicit input data.
Projectors and transition vectors are not themselves the same type of
object as a state. The fixture and exact Gaussian-rational helpers are
reused from spectral_transition_receipt.py and its guarded dependencies.

All arithmetic is exact. No files, network, random sampling, eigensolvers,
external dependencies or numerical integration are used. Finite checks
do not prove the infinite-dimensional trace-class representation theorem,
select a density matrix, derive an empirical probability law, or supply a
measurement outcome, physical locality or a mass-gap theorem.
"""

from fractions import Fraction as F
from itertools import product

import positive_cone_process_receipt as pc
import spectral_transition_receipt as st
import vacuum_loss_receipt as vl
from context_transport_receipt import equal, require


def functional(rho, a):
    return pc.trace(pc.multiply(rho, a))


def weight(rho, effect):
    return pc.real(functional(rho, effect))


def norm2(v):
    return pc.real(vl.inner(v, v))


def absolute_square(z):
    return pc.real(z.conjugate()*z)


def rank_one_projector(v):
    squared_norm = norm2(v)
    require(squared_norm > 0, "projective readout requires a nonzero vector")
    return pc.scale(st.outer(v, v), 1/squared_norm)


def normalized_density_checks(rho):
    pc.positive_semidefinite(rho)
    equal(pc.trace(rho), pc.C(1), "chosen positive density has trace one")


def finite_trace_pairing():
    rho2 = pc.scale(pc.hermitian(1, (F(1, 3), F(1, 4), F(1, 5))), F(1, 2))
    b = pc.matrix(((1, pc.C(F(1, 3), F(1, 4)), F(1, 5)),
                   (0, F(2, 3), pc.C(0, F(1, 2))),
                   (0, 0, F(3, 4))))
    gram = pc.multiply(b, pc.adjoint(b))
    rho3 = pc.scale(gram, 1/pc.real(pc.trace(gram)))
    reconstruction_count, positivity_count = 0, 0
    for rho in (rho2, rho3):
        n = len(rho)
        normalized_density_checks(rho)
        require(pc.real(pc.determinant(rho)) > 0, "these two calibration densities are faithful")
        equal(functional(rho, pc.identity(n)), pc.C(1), "positive trace functional is normalized on the identity")
        reconstructed = pc.matrix([[functional(rho, vl.unit(n, j, i)) for j in range(n)] for i in range(n)])
        equal(reconstructed, rho, "all matrix entries are recovered from the functional on reversed matrix units")
        reconstruction_count += n*n
        probes = vl.all_observables(n)
        for a in probes:
            positive = pc.multiply(pc.adjoint(a), a)
            require(weight(rho, positive) >= 0, "trace pairing is nonnegative on every tested A* A")
            equal(functional(rho, pc.adjoint(a)), functional(rho, a).conjugate(), "positive trace functional respects adjoints")
            positivity_count += 1
        a, c = probes[-1], probes[0]
        alpha, beta = pc.C(F(2, 3), F(1, 5)), pc.C(F(-3, 7), F(1, 2))
        equal(functional(rho, pc.add(pc.scale(a, alpha), pc.scale(c, beta))),
              alpha*functional(rho, a)+beta*functional(rho, c), "trace functional is complex-linear")
        diagonal_weights = tuple(weight(rho, vl.unit(n, i, i)) for i in range(n))
        require(all(0 <= p <= 1 for p in diagonal_weights), "orthogonal basis readout weights are normalized nonnegative numbers")
        equal(sum(diagonal_weights), 1, "complete orthogonal basis readout sums to one")
    equal((reconstruction_count, positivity_count), (13, 17), "finite trace reconstruction and positivity check counts")
    print("PASS: two faithful densities define normalized positive trace pairings; 13 matrix-unit values reconstruct them exactly and 17 A* A probes are nonnegative.")


def pure_and_mixed_readout():
    vectors = (st.basis(3, 0), st.vector(0, F(3, 5), F(4, 5)),
               st.vector(1, pc.C(0, 1), F(1, 2)))
    projections = tuple(rank_one_projector(v) for v in vectors)
    for p in projections:
        normalized_density_checks(p)
        equal(pc.multiply(p, p), p, "normalized vector readout is a rank-one projector")
    for u, v in product(vectors, repeat=2):
        rho, projection = rank_one_projector(u), rank_one_projector(v)
        expected = absolute_square(vl.inner(v, u))/(norm2(u)*norm2(v))
        actual = weight(rho, projection)
        equal(actual, expected, "pure-state projective weight is the normalized squared overlap")
        require(0 <= actual <= 1, "pure-state overlap weight lies in the unit interval")
        complement = pc.sub(pc.identity(3), projection)
        pc.positive_semidefinite(complement)
        equal(actual+weight(rho, complement), 1, "projection and complement exhaust the normalized readout")
    mixed = pc.add(pc.scale(projections[0], F(1, 3)), pc.scale(projections[1], F(2, 3)))
    normalized_density_checks(mixed)
    equal(weight(mixed, mixed), F(5, 9), "the declared orthogonal mixture is genuinely mixed")
    equal(weight(mixed, projections[0]), F(1, 3), "first orthogonal mixture weight")
    equal(weight(mixed, projections[1]), F(2, 3), "second orthogonal mixture weight")
    coherent_vector = tuple(a+b for a, b in zip(vectors[0], vectors[1]))
    coherent_projection = rank_one_projector(coherent_vector)
    equal(weight(mixed, coherent_projection), F(1, 2), "mixed-state trace readout agrees with its convex component weights")
    equal(weight(mixed, coherent_projection),
          F(1, 3)*weight(projections[0], coherent_projection)+F(2, 3)*weight(projections[1], coherent_projection),
          "readout is affine in the chosen density")
    frame = (st.basis(3, 1), st.basis(3, 2), vectors[1],
             st.vector(0, F(-4, 5), F(3, 5)))
    raw_rays = tuple(rank_one_projector(z) for z in frame)
    support = pc.sub(pc.identity(3), projections[0])
    frame_operator = vl.matrix_sum(raw_rays, 3)
    equal(frame_operator, pc.scale(support, 2), "two orthonormal bases give a redundant tight frame with S=2 P_F")
    require(vl.inner(frame[0], frame[2]) != pc.C(), "the combined frame is not pairwise orthogonal")
    require(frame_operator != support, "naively summing normalized rays double-counts the frame support")
    # S^(-1/2)=P_F/sqrt(2) on F; each rank-one effect thus has the rational factor 1/2.
    effects = (projections[0],)+tuple(pc.scale(ray, F(1, 2)) for ray in raw_rays)
    for effect in effects:
        pc.positive_semidefinite(effect)
        pc.positive_semidefinite(pc.sub(pc.identity(3), effect))
    equal(vl.matrix_sum(effects, 3), pc.identity(3), "canonical frame effects plus the complementary projection form a normalized readout")
    frame_weights = tuple(weight(mixed, effect) for effect in effects)
    equal(frame_weights, (F(1, 3), F(3, 25), F(16, 75), F(1, 3), F(0)),
          "the existing mixed density gives exact nonnegative canonical-frame weights")
    equal(sum(frame_weights), 1, "the normalized redundant-frame readout sums to one")
    equal(weight(mixed, frame_operator), F(4, 3), "the uncorrected unit-ray sum is not a probability readout")
    print("PASS: nine pure weights equal squared overlaps; the mixed state has purity 5/9, and a redundant nonorthogonal tight frame gives positive normalized effects while its naive ray sum is 2 P_F.")


def prepared_overlap_calibration():
    source = st.basis(2, 1)
    x, y = st.prepare(F(1), source), st.prepare(F(1, 2), source)
    equal(norm2(x), 1, "unfiltered embedded preparation has unit norm")
    equal(norm2(y), F(13, 100), "filtered preparation squared norm")
    equal(vl.inner(x, y), pc.C(F(17, 50)), "exact common-carrier preparation overlap")
    rho, projection = rank_one_projector(x), rank_one_projector(y)
    actual = weight(rho, projection)
    complement = weight(rho, pc.sub(pc.identity(3), projection))
    equal(actual, F(289, 325), "normalized preparation projection weight")
    equal(complement, F(36, 325), "normalized preparation complement weight")
    equal(actual+complement, 1, "two-outcome preparation readout is normalized")
    numerator = absolute_square(vl.inner(source, vl.apply(st.readout(F(1, 2)), source)))
    denominator = (pc.real(vl.inner(source, vl.apply(st.readout(F(1)), source)))
                   *pc.real(vl.inner(source, vl.apply(st.readout(F(1, 4)), source))))
    equal(numerator/denominator, actual, "the same normalized weight is computed entirely from the compressed readout kernel")
    phases = (pc.C(1), pc.C(F(3, 5), F(4, 5)), pc.C(0, -1))
    for alpha, beta in product(phases, repeat=2):
        equal(alpha.conjugate()*alpha, pc.C(1), "first endpoint phase has unit norm")
        equal(beta.conjugate()*beta, pc.C(1), "second endpoint phase has unit norm")
        phased_x, phased_y = tuple(alpha*a for a in x), tuple(beta*b for b in y)
        equal(rank_one_projector(phased_x), rho, "source endpoint phase leaves its positive state unchanged")
        equal(rank_one_projector(phased_y), projection, "probe endpoint phase leaves its projection unchanged")
        equal(absolute_square(vl.inner(phased_x, phased_y))/(norm2(phased_x)*norm2(phased_y)), actual,
              "independent complex endpoint phases preserve the normalized overlap weight")
    print("PASS: the shared three-dimensional preparation fixture gives weights 289/325 and 36/325; the compressed-kernel formula and nine independent endpoint-phase checks agree.")


def coherent_state_distinction():
    e0, e1 = st.basis(2, 0), st.basis(2, 1)
    diagonal_probes = (rank_one_projector(e0), rank_one_projector(e1))
    coherent_vectors = (st.vector(1, 1), st.vector(1, pc.C(0, 1)))
    coherent_probes = tuple(rank_one_projector(v) for v in coherent_vectors)
    for index, sigma in enumerate((pc.PAULI[0], pc.PAULI[1])):
        plus = pc.add(pc.scale(pc.I, F(1, 2)), pc.scale(sigma, F(1, 4)))
        minus = pc.sub(pc.scale(pc.I, F(1, 2)), pc.scale(sigma, F(1, 4)))
        normalized_density_checks(plus)
        normalized_density_checks(minus)
        require(plus != minus, "opposite coherent states are genuinely distinct")
        for probe in diagonal_probes:
            equal(weight(plus, probe), F(1, 2), "basis readout for first state")
            equal(weight(minus, probe), F(1, 2), "same basis readout for distinct second state")
        probe = coherent_probes[index]
        complement = pc.sub(pc.I, probe)
        equal(weight(plus, probe), F(3, 4), "matching coherent projection distinguishes the first state")
        equal(weight(minus, probe), F(1, 4), "matching coherent projection distinguishes the second state")
        equal(weight(plus, complement), F(1, 4), "coherent complement completes the first readout")
        equal(weight(minus, complement), F(3, 4), "coherent complement completes the second readout")
        # A single selected coherent phase is not complete tomography either.
        other = coherent_probes[1-index]
        equal(weight(plus, other), weight(minus, other), "the orthogonal coherent quadrature is blind to this state difference")
    print("PASS: real and imaginary off-diagonal state differences are invisible to basis diagonal tests but yield coherent projective weights 3/4 versus 1/4.")


def main():
    finite_trace_pairing()
    pure_and_mixed_readout()
    prepared_overlap_calibration()
    coherent_state_distinction()
    print("All four check groups passed. Exact rational arithmetic; stdlib only; stdout only; no files written.")
    print("Finite positive readout checks do not prove the trace-class representation theorem or select a state, measurement outcome, physical locality, or mass gap.")


if __name__ == "__main__":
    main()
