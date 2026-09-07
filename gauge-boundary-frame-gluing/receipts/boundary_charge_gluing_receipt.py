"""Receipts for boundary-charge gluing and exact kernel contractions.

Two Z2 link variables x_A and x_B share an effective boundary gauge action
(x_A, x_B) -> (-x_A, -x_B).  Each regional link carrier decomposes into the
trivial basis vector 1 and the charged basis vector x.  The diagonal global
invariants contain 1 tensor 1 and x tensor x, while independently averaging
each region keeps only 1 tensor 1.
"""

from __future__ import annotations

import itertools
import math
from decimal import Decimal, localcontext
from fractions import Fraction

import numpy as np


def su2_overlap_clock_checks() -> None:
    """Compute all Peter--Weyl blocks, including the omitted infinite tail.

    On SU(2), chi_1=2*z and kappa=(4+chi_1)/6.  Expanding
    (4+chi_1)^k gives integer coefficients a_l by the character product
    chi_1*chi_l=chi_(l+1)+chi_(l-1), with chi_(-1)=0.  Haar normalization
    is a_0/6^k; convolution on the full degree-l matrix-coefficient block
    is b_l=a_l/((l+1)*a_0), not merely the normalized character coefficient.

    Q_R=2*g_round, so -(3*r/2)*Delta_Q=-(3/2)*Delta_round has eigenvalue
    (3/2)*l*(l+2).  Coefficient and positivity checks below are exact;
    scalar error values use floating point and are not convergence proofs.
    """
    print("SU(2) overlap clock: exact character coefficients, full-carrier error readouts")
    print("N  heat-power error  Poisson-resolvent error  outside-support resolvent supremum")
    for n in (1, 2, 4, 8, 16, 32):
        power = n*n
        coefficients = [1]
        for _ in range(power):
            previous = coefficients
            coefficients = [4*previous[ell]
                            + (previous[ell-1] if ell else 0)
                            + (previous[ell+1] if ell+1 < len(previous) else 0)
                            for ell in range(len(previous))]
            coefficients.append(previous[-1])
        normalizer = coefficients[0]
        assert normalizer > 0 and len(coefficients) == power+1
        assert sum((ell+1)*value for ell, value in enumerate(coefficients)) == 6**power
        assert all(0 <= value <= (ell+1)*normalizer
                   for ell, value in enumerate(coefficients))
        assert Fraction(coefficients[0], normalizer) == 1
        if n == 1:
            assert coefficients == [4, 1]
            # p_1=1+chi_1/4, whose degree-one convolution eigenvalue is 1/8.
            assert Fraction(coefficients[1], 2*normalizer) == Fraction(1, 8)

        # For ell>power, B_N is exactly zero.  The heat-tail maximum is
        # its first block, exp[-3*(power+1)*(power+3)/2].  Its float can
        # underflow, but the tail formula is analytic, not a cutoff guess.
        heat_tail_exponent = Fraction(3*(power+1)*(power+3), 2)
        heat_error = math.exp(-float(heat_tail_exponent))
        # On the same infinite complement, (1+power*(I-B_N))^-1 is
        # 1/(1+power), whereas the target resolvent tends to zero.  The
        # supremum is this limiting value, not any last sampled block.
        assert Fraction(3*(power+1)*(power+3), 2) > power
        resolvent_tail = Fraction(1, 1+power)
        resolvent_error = resolvent_tail
        for ell, value in enumerate(coefficients):
            denominator = (ell+1)*normalizer
            eigenvalue = value/denominator
            target_generator = Fraction(3*ell*(ell+2), 2)
            heat_error = max(heat_error,
                             abs(eigenvalue**power-math.exp(-float(target_generator))))
            # Exact subtraction before floating conversion avoids loss of
            # low-mode precision when b_l approaches one under refinement.
            poisson_generator = Fraction(power*(denominator-value), denominator)
            resolvent_difference = abs(1/(1+poisson_generator)-1/(1+target_generator))
            resolvent_error = max(resolvent_error, resolvent_difference)
        print(f"{n:2d}  {heat_error:.10e}  {float(resolvent_error):.10e}  {float(resolvent_tail):.10e}")
    print("PASS exact normalization and 0<=b_l<=1 on every nonzero harmonic block; "
          "both infinite tails included analytically.")
    print("Floating-point norm readouts at six refinements only; "
          "no four-dimensional field limit or physical mass gap is certified.")


def su2_star_hessian_checks() -> None:
    """Differentiate the full star integrand before taking exact Haar moments.

    For X=i*sigma3/sqrt(2), Q(X,X)=-ReTr(X^2)=1. Working first with
    theta=t/sqrt(2) keeps all jet coefficients rational. The scalar part of
    exp(-theta*z_i*i*sigma3)u is u0*cos(theta*z_i)+u3*sin(theta*z_i).
    The constant 3^(-km) in the complete kernel product cancels in log jets.
    """
    f = Fraction

    def add(left, right):
        result = dict(left)
        for exponent, value in right.items():
            result[exponent] = result.get(exponent, f(0))+value
        return {exponent: value for exponent, value in result.items() if value}

    def multiply(left, right):
        result = {}
        for (a, b), value in left.items():
            for (c, d), other in right.items():
                exponent = (a+c, b+d)
                result[exponent] = result.get(exponent, f(0))+value*other
        return {exponent: value for exponent, value in result.items() if value}

    def jet_product(left, right):
        result = [{}, {}, {}]
        for degree in range(3):
            for index in range(degree+1):
                result[degree] = add(result[degree], multiply(left[index], right[degree-index]))
        return result

    def haar_moment(a, b):
        if a % 2 or b % 2:
            return f(0)
        numerator = math.prod(range(1, a, 2))*math.prod(range(1, b, 2))
        denominator = math.prod(range(4, a+b+4, 2))
        return f(numerator, denominator)

    def integrate(polynomial):
        return sum(value*haar_moment(*exponent) for exponent, value in polynomial.items())

    def star_jet(k, direction):
        total = [{(0, 0): f(1)}, {}, {}]
        for value in direction:
            factor = [{(0, 0): f(2), (1, 0): f(1)},
                      {(0, 1): f(value)}, {(1, 0): -f(value*value, 2)}]
            for _ in range(k):
                total = jet_product(total, factor)
        a0, a1, a2 = (integrate(polynomial) for polynomial in total)
        assert a0 > 0 and a1 == 0
        # Convert the angular second log derivative to Q-unit parameter t.
        return a0, -a2/a0+a1*a1/(2*a0*a0)

    def scalar_moment(power):
        # Independent one-variable Catalan expression for the coefficient
        # comparison, rather than reusing the jet's mixed-moment formula.
        if power % 2:
            return f(0)
        degree = power//2
        catalan = math.comb(2*degree, degree)//(degree+1)
        return f(catalan, 4**degree)

    def radial_integral(power, displacement=False):
        return sum(math.comb(power, j)*2**(power-j)
                   * (scalar_moment(j)-scalar_moment(j+2) if displacement else scalar_moment(j))
                   for j in range(power+1))

    cases, first_coefficients = 0, {}
    for m, k in itertools.product((2, 4, 6), (1, 2, 4, 8)):
        power = k*m
        normalization = radial_integral(power)
        coefficient = f(k*k, 6)*radial_integral(power-2, True)/normalization
        assert coefficient > 0
        units = [tuple(int(i == j) for i in range(m)) for j in range(m)]
        hessian = [[f(0) for _ in range(m)] for _ in range(m)]
        for i, direction in enumerate(units):
            a0, value = star_jet(k, direction)
            assert a0 == normalization
            hessian[i][i] = value
        for i, j in itertools.combinations(range(m), 2):
            plus = tuple(units[i][r]+units[j][r] for r in range(m))
            minus = tuple(units[i][r]-units[j][r] for r in range(m))
            _, plus_value = star_jet(k, plus)
            _, minus_value = star_jet(k, minus)
            entry = (plus_value-hessian[i][i]-hessian[j][j])/2
            hessian[i][j] = hessian[j][i] = entry
            assert minus_value == hessian[i][i]+hessian[j][j]-2*entry
        assert all(hessian[i][j] == coefficient*(m*int(i == j)-1)
                   for i, j in itertools.product(range(m), repeat=2))
        # A direct common-motion jet, not just multiplication by a matrix
        # whose zero row sums have been imposed as the expected answer.
        _, common = star_jet(k, (1,)*m)
        assert common == 0
        direction = tuple((-1)**i*(i+1) for i in range(m))
        _, mixed = star_jet(k, direction)
        expected = coefficient*(m*sum(value*value for value in direction)-sum(direction)**2)
        assert mixed == expected > 0
        if k == 1:
            first_coefficients[m] = coefficient
        cases += 1
    assert tuple(first_coefficients[m] for m in (2, 4, 6)) == (f(1, 34), f(25, 1062), f(107, 5614))
    print(f"PASS {cases} exact SU(2) star Hessians from integrated full-product jets: "
          "diagonal, mixed and common-gauge directions")
    print("Q-normalized c at k=1, m=2,4,6: "
          + ", ".join(str(first_coefficients[m]) for m in (2, 4, 6)))
    print("Coincident-star response checks only; no global coercivity or physical spectral-gap conclusion.")


def s3_shared_edge_checks() -> None:
    """Exact non-Abelian finite-group gluing, not a compact-Lie heat limit."""
    f = Fraction
    permutations = tuple(itertools.permutations(range(3)))
    indices = {g: i for i, g in enumerate(permutations)}
    identity = indices[(0, 1, 2)]
    elements = range(len(permutations))
    multiply = tuple(tuple(indices[tuple(g[h[j]] for j in range(3))]
                           for h in permutations) for g in permutations)
    inverse = tuple(indices[tuple(g.index(j) for j in range(3))] for g in permutations)
    character = tuple(sum(g[j] == j for j in range(3))-1 for g in permutations)
    anchored = tuple(f(4+value, 6) for value in character)
    assert anchored[identity] == 1
    for g in elements:
        assert multiply[g][inverse[g]] == identity
        assert anchored[inverse[g]] == anchored[g]
        assert anchored[g] == {2: f(1), 0: f(2, 3), -1: f(1, 2)}[character[g]]

    powers = (1, 2, 4)
    kernels = {}
    for k in powers:
        normalizer = sum(value**k for value in anchored)/6
        kernels[k] = tuple(value**k/normalizer for value in anchored)
        assert sum(kernels[k])/6 == 1

    def convolution(left, right):
        return tuple(sum(left[v]*right[multiply[inverse[v]][h]] for v in elements)/6
                     for h in elements)

    boundary_count, law_count, covariances = 0, 0, {}
    for k, ell in itertools.product(powers, repeat=2):
        left, right = kernels[k], kernels[ell]
        combined = convolution(left, right)
        assert sum(combined)/6 == 1
        # This is the actual density relative to product Haar on (A,u,B),
        # divided by 6^3 below to obtain exact point probabilities.
        joint = {}
        for a, b in itertools.product(elements, repeat=2):
            integral = sum(left[multiply[a][inverse[u]]]*right[multiply[u][b]]
                           for u in elements)/6
            assert integral == combined[multiply[a][b]]
            boundary_count += 1
            for u in elements:
                joint[(a, u, b)] = left[multiply[a][inverse[u]]]*right[multiply[u][b]]/216
        assert sum(joint.values()) == 1
        marginals = [[f(0) for _ in elements] for _ in range(3)]
        boundary = [[f(0) for _ in elements] for _ in elements]
        face_pair = [[f(0) for _ in elements] for _ in elements]
        for (a, u, b), value in joint.items():
            for coordinate, state in enumerate((a, u, b)):
                marginals[coordinate][state] += value
            boundary[a][b] += value
            face_pair[multiply[a][inverse[u]]][multiply[u][b]] += value
        assert all(value == f(1, 6) for marginal in marginals for value in marginal)
        covariance = boundary[identity][identity]-f(1, 36)
        assert covariance == (combined[identity]-1)/36
        assert covariance > 0
        assert any(value != marginals[0][a]*marginals[1][u]*marginals[2][b]
                   for (a, u, b), value in joint.items())
        # Framed boundary variables are correlated, but independent face
        # increments are possible after this exact change of variables.
        assert all(face_pair[a][b] == left[a]*right[b]/36
                   for a, b in itertools.product(elements, repeat=2))
        if k == ell:
            covariances[k] = covariance
        law_count += 1
    assert covariances[1] == f(1, 576)
    # Multiplication of feature powers is not operator/face convolution.
    convolved_identity = convolution(kernels[1], kernels[1])[identity]
    assert convolved_identity == f(17, 16)
    assert kernels[2][identity] == f(36, 17)
    assert convolved_identity != kernels[2][identity]
    print("S3 anchored trace kernel: exact values (identity, transposition, 3-cycle) = (1, 2/3, 1/2)")
    print(f"PASS {boundary_count} exact two-face boundary integrals and {law_count} normalized shared-edge joint laws")
    print("Framed boundary indicator covariances for equal k=1,2,4: "
          + ", ".join(str(covariances[k]) for k in powers))
    print("PASS raw/boundary nonfactorization and independent face-increment coordinates; "
          "p1*p1(identity)=17/16 differs from p2(identity)=36/17")

    # Standard representation on span(e1-e3,e2-e3). This rational basis is
    # not orthonormal: G=[[2,1],[1,2]] is its inherited invariant metric.
    basis = np.array([[1, 0], [0, 1], [-1, -1]], dtype=np.int64)
    metric = basis.T@basis
    representations = []
    for g in permutations:
        moved = np.zeros_like(basis)
        for source in range(3):
            moved[g[source]] = basis[source]
        representation = moved[:2]
        assert np.array_equal(basis@representation, moved)
        assert np.array_equal(representation.T@metric@representation, metric)
        representations.append(representation)
    for g, h in itertools.product(elements, repeat=2):
        assert np.array_equal(representations[g]@representations[h], representations[multiply[g][h]])
    assert tuple(int(np.trace(r)) for r in representations) == character

    def tensor_power(matrix, degree):
        result = np.ones((1, 1), dtype=np.int64)
        for _ in range(degree):
            result = np.kron(result, matrix)
        return result

    dimensions = []
    for degree, expected in ((2, 1), (4, 3), (6, 11)):
        tensors = [tensor_power(r, degree) for r in representations]
        # The Haar projector is S/6. Integer products avoid floating-point
        # rank decisions and verify its exact projector identities.
        total = sum(tensors)
        tensor_metric = tensor_power(metric, degree)
        assert np.array_equal(total@total, 6*total)
        assert np.array_equal(total.T@tensor_metric, tensor_metric@total)
        assert all(np.array_equal(r@total, total) for r in tensors)
        dimension = sum(f(value)**degree for value in character)/6
        assert dimension == f(int(np.trace(total)), 6) == expected
        dimensions.append(int(dimension))
    print("PASS exact S3 Haar projectors on V^2,V^4,V^6: invariant dimensions = "
          + ", ".join(map(str, dimensions)))
    print("Finite-group gluing and channel-multiplicity checks only; "
          "no compact-Lie heat limit, spatial continuum theory or mass gap is certified.")


def su2_heat_state_and_nested_loop_checks() -> None:
    """Check actual heat-law moments and disjoint nested-loop responses.

    Here D has C_j=j(j+1): Q=-2*Tr=4*g_round, twice the overlap
    metric Q_R above. The state q_t is the density of exp(-t*D) at e.
    Its parameter t is face area times sigma, not a physical clock.

    For f=chi_(1/2), f^2=1+chi_1 and Gamma(f)=1-f^2/4.
    Nested planar heat holonomies have the Brownian character moment
    M(s,t)=exp(-3*abs(t-s)/4)*(1+3*exp(-2*min(s,t))).
    Pairwise disjoint loop boundaries instead have zero off-diagonal
    ORIGINAL edge-gradient response, despite their correlated moments.
    The ensuing finite checks illustrate the separate analytic
    nonclosability argument; they are not an infinite-limit proof.
    """
    # Exact coefficient multiplication, independent of floating exponentials.
    left, right = (1, -2, 1), (1, 2, 3)
    product = [0]*5
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            product[i+j] += a*b
    assert product == [1, 0, 0, -4, 3]

    sampled_times = (0.001, 0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 20.0, 100.0)
    for t in sampled_times:
        y = math.exp(-t/2)
        one_minus_y = -math.expm1(-t/2)
        variance = one_minus_y**2*(1+2*y+3*y*y)
        response = -0.75*math.expm1(-2*t)
        trial = response/variance
        lower = -0.5/math.expm1(-t)
        assert variance > 0 and 0 < lower <= trial
        # Independently evaluate the unfactored character moments with
        # enough precision to retain their small-time cancellation.
        with localcontext() as context:
            context.prec = 60
            td = Decimal(str(t))
            variance_d = (Decimal(1)+3*(-2*td).exp()
                          -4*(-Decimal("1.5")*td).exp())
            response_d = Decimal("0.75")*(1-(-2*td).exp())
        assert math.isclose(variance, float(variance_d), rel_tol=2e-13)
        assert math.isclose(response, float(response_d), rel_tol=2e-13)
    assert abs(sampled_times[0] * (
        -0.75*math.expm1(-2*sampled_times[0]) /
        ((-math.expm1(-sampled_times[0]/2))**2 *
         (1+2*math.exp(-sampled_times[0]/2)+3*math.exp(-sampled_times[0])))) - 1) < 0.001
    print("PASS SU(2) heat-state variance factorization and nine full-loop Bochner/trial bounds; "
          "independent 60-digit character-moment checks")

    sizes = (8, 32, 128, 512)
    count = 2*max(sizes)
    times = np.array([1.0]+[1+1/k for k in range(1, count+1)])
    smaller = np.minimum(times[:, None], times[None, :])
    moments = np.exp(-0.75*np.abs(times[:, None]-times[None, :])) * (
        1+3*np.exp(-2*smaller))
    means = 2*np.exp(-0.75*times)

    # Verify the complete moment matrix via a second, positive covariance
    # representation, not an eigenvalue sample. Write d(t)=exp(-3t/4),
    # v(t)=exp(3t/2)+3*exp(-t/2)-4. Then Cov(s,t)=d(s)d(t)v(min(s,t)).
    # v(0)=0 and v'(t)=(3/2)(exp(3t/2)-exp(-t/2))>0 for t>0.
    # Ordered positive increments of v give a sum of rank-one PSD forms
    # on EVERY finite set of these times, without a spectral cutoff.
    covariance = np.outer(means/2, means/2) * (
        np.exp(1.5*smaller)+3*np.exp(-0.5*smaller)-4)
    assert np.array_equal(moments, moments.T)
    assert np.allclose(moments, np.outer(means, means)+covariance,
                       rtol=2e-14, atol=2e-14)
    ordered = np.sort(times)
    v_ordered = np.exp(1.5*ordered)+3*np.exp(-0.5*ordered)-4
    assert v_ordered[0] > 0 and np.all(np.diff(v_ordered) > 0)

    # These are square-loop perimeters B_k=4*sqrt(t_k), kappa=sigma=1.
    # They form the diagonal of the response Gram, not its moment Gram.
    energies = -3*np.sqrt(times)*np.expm1(-2*times)
    energy_zero = float(energies[0])

    def decimal_difference_norm(size: int) -> Decimal:
        """Independent ordered Markov summation of c^T M c, in O(N)."""
        with localcontext() as context:
            context.prec = 60
            coefficients = [Decimal(1)]+[-Decimal(1)/size]*size
            ordered_times = [Decimal(1)]+[
                Decimal(1)+Decimal(1)/k for k in range(size, 0, -1)]
            prefix, total = Decimal(0), Decimal(0)
            for coefficient, time in zip(coefficients, ordered_times):
                decay = (-Decimal("0.75")*time).exp()
                diagonal = Decimal(1)+3*(-2*time).exp()
                total += coefficient**2*diagonal+2*coefficient*decay*prefix
                prefix += coefficient*diagonal/decay
            return +total

    print("Nested-loop finite diagnostic: N  ||g_N||^2  E(g_N)  E(F_N)  E(F_N-F_2N); "
          f"E(f_0)={energy_zero:.10e}")
    previous_norm = previous_average_energy = previous_difference_energy = math.inf
    for size in sizes:
        # F_N=N^-1 sum_{k=1}^N f_k, g_N=f_0-F_N, without centering.
        # Every entry of the finite raw moment Gram contributes here.
        norm_squared = math.fsum((
            float(moments[0, 0]),
            math.fsum(-2*float(value)/size for value in moments[0, 1:size+1]),
            math.fsum(float(value)/(size*size)
                      for value in moments[1:size+1, 1:size+1].flat)))
        assert math.isclose(norm_squared, float(decimal_difference_norm(size)),
                            rel_tol=2e-10, abs_tol=2e-13)
        jensen_bound = math.fsum(float(moments[0, 0]+moments[k, k]-2*moments[0, k])
                                for k in range(1, size+1))/size
        assert 0 < norm_squared <= jensen_bound+2e-13
        average_energy = math.fsum(float(value) for value in energies[1:size+1])/size**2
        difference_energy = math.fsum(float(value) for value in energies[1:2*size+1])/(4*size**2)
        g_energy = energy_zero+average_energy
        # F_N-F_2N has coefficients +/-1/(2N) on the first 2N loops.
        # No off-diagonal response is substituted from the moment Gram.
        assert average_energy <= float(max(energies[1:size+1]))/size
        assert difference_energy <= float(max(energies[1:2*size+1]))/(2*size)
        assert norm_squared < previous_norm
        assert 0 < average_energy < previous_average_energy
        assert 0 < difference_energy < previous_difference_energy
        assert g_energy > energy_zero
        previous_norm = norm_squared
        previous_average_energy = average_energy
        previous_difference_energy = difference_energy
        print(f"{size:4d}  {norm_squared:.10e}  {g_energy:.10e}  "
              f"{average_energy:.10e}  {difference_energy:.10e}")
    print(f"PASS complete {count+1}-loop moment Gram identities and positive covariance decomposition; "
          "four 60-digit average-norm checks; disjoint-boundary response used separately")
    print("Finite state/response diagnostics only; the analytic nonclosability proof, "
          "not these samples, decides the limiting form; no Yang--Mills clock or mass gap certified.")


def su2_shared_driver_clock_checks() -> None:
    """Check the specified Wiener clock, not an inferred physical generator.

    With standard Brownian B and dX=sqrt(2)*X*T_a o dB_a, Q=-2*Tr,
    the shared Malliavin derivative yields response
    R(s,t)=2*min(s,t)*exp(-3*abs(s-t)/4)*J(min(s,t)).  This is a
    different response law from the preceding perimeter-diagonal form.
    The Mehler clock duration tau is separate from Brownian heat-area t.
    Its correlations are verified below using the actual 4x4 Pauli
    tensor generator, not by substituting a state covariance as response.
    """
    sizes = (8, 32, 128, 512)
    times = np.array([1.0]+[1+1/k for k in range(1, max(sizes)+1)])
    smaller = np.minimum(times[:, None], times[None, :])
    response = (-1.5*smaller*np.exp(-0.75*np.abs(times[:, None]-times[None, :]))
                * np.expm1(-2*smaller))
    assert np.array_equal(response, response.T)

    # Independent positive-increment factorization of the entire Gram:
    # R(s,t)=d(s)d(t)v(min(s,t)), d=exp(-3t/4),
    # v(t)=(3t/2)*(exp(3t/2)-exp(-t/2)).  Here v(0)=0, v'>0.
    decay = np.exp(-0.75*times)
    v = 1.5*smaller*(np.exp(1.5*smaller)-np.exp(-0.5*smaller))
    assert np.allclose(response, np.outer(decay, decay)*v,
                       rtol=2e-14, atol=2e-14)
    ordered = np.sort(times)
    ordered_v = 1.5*ordered*(np.exp(1.5*ordered)-np.exp(-0.5*ordered))
    assert ordered_v[0] > 0 and np.all(np.diff(ordered_v) > 0)

    def decimal_difference_energy(size: int) -> Decimal:
        """O(N) ordered Markov-kernel summation, independent of the dense Gram."""
        with localcontext() as context:
            context.prec = 60
            coefficients = [Decimal(1)]+[-Decimal(1)/size]*size
            ordered_times = [Decimal(1)]+[
                Decimal(1)+Decimal(1)/k for k in range(size, 0, -1)]
            prefix, total = Decimal(0), Decimal(0)
            for coefficient, time in zip(coefficients, ordered_times):
                factor = (-Decimal("0.75")*time).exp()
                diagonal = Decimal("1.5")*time*(1-(-2*time).exp())
                total += coefficient**2*diagonal+2*coefficient*factor*prefix
                prefix += coefficient*diagonal/factor
            return +total

    energy_zero = float(response[0, 0])
    old_energies = -3*np.sqrt(times)*np.expm1(-2*times)
    print("Shared-driver finite diagnostic: N  E_new(g_N)  E_new(F_N)  "
          "off-diagonal average  diagonal average  E_old(g_N); "
          f"E_new(f_0)={energy_zero:.10e}")
    previous_energy = math.inf
    for size in sizes:
        block = response[1:size+1, 1:size+1]
        diagonal_average = math.fsum(float(value) for value in block.diagonal())/size**2
        average = math.fsum(float(value) for value in block.flat)/size**2
        cross = math.fsum(float(value) for value in response[0, 1:size+1])/size
        g_energy = math.fsum((energy_zero, average, -2*cross))
        assert math.isclose(g_energy, float(decimal_difference_energy(size)),
                            rel_tol=2e-10, abs_tol=2e-13)
        off_diagonal = average-diagonal_average
        assert 0 < g_energy < previous_energy
        assert 0 < diagonal_average < average
        assert diagonal_average <= float(max(block.diagonal()))/size
        # The old response remains diagonal, even though the same state
        # and the same observables are used for this contrasting readout.
        old_g_energy = float(old_energies[0])+math.fsum(
            float(value) for value in old_energies[1:size+1])/size**2
        assert old_g_energy > float(old_energies[0]) > energy_zero
        previous_energy = g_energy
        print(f"{size:4d}  {g_energy:.10e}  {average:.10e}  {off_diagonal:.10e}  "
              f"{diagonal_average:.10e}  {old_g_energy:.10e}")
    print(f"PASS complete {len(times)}-loop shared-response Gram and four independent "
          "60-digit difference-energy checks; mixed response retained")

    pauli = (
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    )
    generators = tuple(0.5j*matrix for matrix in pauli)
    identity2, identity4 = np.eye(2), np.eye(4)
    for a, b in itertools.product(range(3), repeat=2):
        assert np.allclose(-2*np.trace(generators[a]@generators[b]), int(a == b))
    assert all(np.array_equal(matrix.conj().T, -matrix) for matrix in generators)
    single_casimir = -sum(matrix@matrix for matrix in generators)
    assert np.array_equal(single_casimir, 0.75*identity2)
    interaction = sum(np.kron(matrix, matrix) for matrix in generators)
    total_generators = tuple(np.kron(matrix, identity2)+np.kron(identity2, matrix)
                             for matrix in generators)
    total_casimir = -sum(matrix@matrix for matrix in total_generators)
    singlet = np.array([0, 1, -1, 0], dtype=complex)/math.sqrt(2)
    assert all(np.allclose(matrix@singlet, 0) for matrix in total_generators)
    assert np.allclose(np.linalg.eigvalsh(total_casimir), (0, 2, 2, 2))
    assert np.allclose(np.linalg.eigvalsh(interaction), (-0.25, -0.25, -0.25, 0.75))

    def tensor_exponential(rho: float, heat_time: float):
        # Compute exp(t*K) from the explicit matrix, before comparison
        # with the independently supplied singlet/triplet trace formula.
        kernel = -1.5*identity4+2*rho*interaction
        assert np.allclose(kernel, kernel.conj().T)
        eigenvalues, eigenvectors = np.linalg.eigh(kernel)
        expected = sorted((-1.5+1.5*rho,)+(-1.5-0.5*rho,)*3)
        assert np.allclose(eigenvalues, expected, rtol=2e-14, atol=2e-14)
        return (eigenvectors*np.exp(heat_time*eigenvalues))@eigenvectors.conj().T

    durations = (0.0, 0.2, 1.0, 3.0)
    heat_pairs = ((0.1, 0.1), (0.5, 1.0), (1.0, 1.5), (1.0, 1.0), (2.0, 3.0))
    traces = {}
    for s, t in heat_pairs:
        future_decay = math.exp(-0.75*(t-s))
        mean_product = 4*math.exp(-0.75*(s+t))
        for duration in durations:
            rho = math.exp(-duration)
            matrix = tensor_exponential(rho, s)
            centered = future_decay*float(np.trace(matrix).real)-mean_product
            formula = math.exp(-0.75*(s+t))*(
                math.exp(1.5*rho*s)+3*math.exp(-0.5*rho*s)-4)
            assert centered > 0
            assert math.isclose(centered, formula, rel_tol=2e-9, abs_tol=2e-14)
            if (s, t) == (1.0, 1.5):
                traces[duration] = centered
        # -d/dtau exp[s*K(exp(-tau))] at tau=0: K commutes with
        # its derivative -2*interaction, so this is an exact matrix
        # derivative, not a finite difference of the closed formula.
        matrix = tensor_exponential(1.0, s)
        response_from_clock = future_decay*float(np.trace(matrix@(2*s*interaction)).real)
        response_from_gradient = -1.5*s*future_decay*math.expm1(-2*s)
        assert math.isclose(response_from_clock, response_from_gradient,
                            rel_tol=2e-13, abs_tol=2e-14)
    print("Pauli-tensor centered Mehler readout at heat-areas (1,1.5): "
          + ", ".join(f"tau={duration:g}: {traces[duration]:.10e}" for duration in durations))
    print("PASS explicit 4x4 Pauli Casimir singlet/triplet spectra, 20 clock pairings "
          "and five matrix-derivative/shared-gradient identities")

    # Same Gaussian state, different duration generator dGamma(M_a).
    # For T>0 and h_n=sqrt(n/T)*1_(0,T/n), the three first-chaos
    # variables are independent standard normals. Their centered radial
    # square F=sum_a I(h_n e_a)^2-3 has variance 6 and gradient norm
    # expectation 12*h_n^2. Thus its Rayleigh quotient is
    # 2*integral a*h_n^2: 2 for a=1, but 1/n for a(s)=s/T.
    # Positive a almost everywhere preserves the constant kernel; the
    # all-n proof of gaplessness is analytic, not these four samples.
    horizon = Fraction(7, 3)
    variance = 3*Fraction(3)+6*Fraction(1)-18+9
    assert variance == 6
    weighted_quotients = []
    for n in sizes:
        squared_height = n/horizon
        support_length = horizon/n
        assert squared_height*support_length == 1
        unit_energy = 12*squared_height*support_length
        weighted_energy = 12*squared_height*support_length**2/(2*horizon)
        assert unit_energy/variance == 2
        quotient = weighted_energy/variance
        assert quotient == Fraction(1, n) > 0
        weighted_quotients.append(quotient)
    print("PASS exact quadratic-singlet rate-selection quotients: unit clock=2; "
          "a(s)=s/T at n=8,32,128,512 gives "
          + ", ".join(map(str, weighted_quotients))
          + "; Gaussian state unchanged")
    print("Finite diagnostics of the specified shared-driver and variable-rate clocks only; "
          "no four-dimensional construction or physical mass gap certified.")

    def su2_exponential(vector):
        angle = math.sqrt(sum(value*value for value in vector))
        if angle == 0:
            return np.eye(2, dtype=complex)
        tangent = sum(value*matrix for value, matrix in zip(vector, generators))
        return math.cos(angle/2)*identity2+(2*math.sin(angle/2)/angle)*tangent

    # Actual two-holonomy readout f(x,y)=Tr(x^-1*y). Left-moving x
    # and y gives opposite derivatives, so their common pre-annulus
    # driver cancels. Finite differences independently test those matrix
    # derivatives before the weighted 2x2 response is contracted.
    positions = ((0.0, 0.0, 0.0), (0.2, -0.4, 0.1), (0.7, 0.3, -0.5))
    increments = ((0.0, 0.0, 0.0), (0.4, 0.2, -0.1), (-1.0, 0.7, 0.3))
    annuli = ((Fraction(0), Fraction(1, 4)),
              (Fraction(1, 5), Fraction(2, 5)),
              (Fraction(2, 3), Fraction(1, 3)),
              (Fraction(1), Fraction(1, 2)))
    intensity = Fraction(3, 5)
    derivative_step = 1e-5
    annular_cases = 0
    for start, duration in annuli:
        assert start+duration <= horizon
        # These restart defects use exact rationals, independent of any
        # matrix calculations or fitted limiting rate.
        constant = lambda value: intensity*value
        quadratic = lambda value: value*value/(2*horizon)
        assert constant(start+duration)-constant(start)-constant(duration) == 0
        assert (quadratic(start+duration)-quadratic(start)-quadratic(duration)
                == start*duration/horizon)
        exponential = lambda value: -math.expm1(-float(value))
        assert math.isclose(exponential(start+duration)-exponential(start),
                            math.exp(-float(start))*exponential(duration),
                            rel_tol=2e-14, abs_tol=2e-14)
        for position in (positions[:1] if start == 0 else positions):
            x = su2_exponential(position)
            assert np.allclose(x.conj().T@x, identity2)
            assert np.allclose(np.linalg.det(x), 1)
            for increment in increments:
                y = x@su2_exponential(increment)
                character = float(np.trace(x.conj().T@y).real)
                gradients = np.zeros((2, 3))
                for axis, matrix in enumerate(generators):
                    derivative = np.trace(x.conj().T@matrix@y)
                    assert abs(derivative.imag) < 2e-14
                    gradients[:, axis] = (-derivative.real, derivative.real)
                    step_vector = tuple(derivative_step*int(a == axis) for a in range(3))
                    plus = su2_exponential(step_vector)
                    minus = plus.conj().T
                    finite_x = float((np.trace((plus@x).conj().T@y)
                                      - np.trace((minus@x).conj().T@y)).real)/(2*derivative_step)
                    finite_y = float((np.trace(x.conj().T@plus@y)
                                      - np.trace(x.conj().T@minus@y)).real)/(2*derivative_step)
                    assert math.isclose(finite_x, gradients[0, axis], abs_tol=8e-11)
                    assert math.isclose(finite_y, gradients[1, axis], abs_tol=8e-11)
                assert np.array_equal(gradients.sum(axis=0), np.zeros(3))
                norm_squared = float(gradients[1]@gradients[1])
                assert math.isclose(norm_squared, 1-character*character/4,
                                    rel_tol=2e-13, abs_tol=2e-14)
                for primitive in (constant, quadratic, exponential):
                    a0, a1 = float(primitive(start)), float(primitive(start+duration))
                    kernel = 2*np.array([[a0, a0], [a0, a1]])
                    if start == 0:
                        assert np.array_equal(kernel[0], np.zeros(2))
                    contracted = float(np.einsum("ij,ia,ja->", kernel, gradients, gradients))
                    annular = 2*(a1-a0)*(1-character*character/4)
                    assert math.isclose(contracted, annular, rel_tol=3e-13, abs_tol=3e-14)
                annular_cases += 1
    assert annular_cases == 30
    print("PASS 30 explicit SU(2) annular left-gradient/cross-response checks including s=0; "
          "exact constant/quadratic restart and exponential retiming tests; finite diagnostics only.")


def main() -> None:
    states = list(itertools.product((-1, 1), repeat=2))
    index = {state: i for i, state in enumerate(states)}

    identity = np.eye(4)
    diagonal_flip = np.zeros((4, 4))
    flip_a = np.zeros((4, 4))
    flip_b = np.zeros((4, 4))

    for i, (x_a, x_b) in enumerate(states):
        diagonal_flip[index[(-x_a, -x_b)], i] = 1.0
        flip_a[index[(-x_a, x_b)], i] = 1.0
        flip_b[index[(x_a, -x_b)], i] = 1.0

    global_gauss = 0.5 * (identity + diagonal_flip)
    close_a = 0.5 * (identity + flip_a)
    close_b = 0.5 * (identity + flip_b)
    separately_closed = close_a @ close_b

    one_one = np.ones(4) / 2.0
    charged_pair = np.array([x_a * x_b for x_a, x_b in states]) / 2.0

    assert np.allclose(global_gauss @ global_gauss, global_gauss)
    assert np.allclose(separately_closed @ separately_closed, separately_closed)
    assert np.linalg.matrix_rank(global_gauss) == 2
    assert np.linalg.matrix_rank(separately_closed) == 1
    assert np.allclose(global_gauss @ one_one, one_one)
    assert np.allclose(global_gauss @ charged_pair, charged_pair)
    assert np.allclose(separately_closed @ one_one, one_one)
    assert np.allclose(separately_closed @ charged_pair, 0.0)
    assert np.allclose(global_gauss @ separately_closed, separately_closed)

    print("boundary charge gluing receipt: PASS")
    print(f"extended regional dimensions = 2 x 2")
    print(f"diagonally glued physical dimension = {np.linalg.matrix_rank(global_gauss)}")
    print(f"separately closed dimension = {np.linalg.matrix_rank(separately_closed)}")
    print("retained global sectors = trivial-trivial, charged-charged")
    print("premature regional closure erases = charged-charged")
    s3_shared_edge_checks()
    su2_star_hessian_checks()
    su2_overlap_clock_checks()
    su2_heat_state_and_nested_loop_checks()
    su2_shared_driver_clock_checks()


if __name__ == "__main__":
    main()
