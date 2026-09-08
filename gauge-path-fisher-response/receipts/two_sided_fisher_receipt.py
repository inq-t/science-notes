"""Finite tests for the specified two-sided path-shift Fisher construction.

These tests discriminate the joint response from either one-hand response,
check finite logarithmic-ramp entropy controls, and sample small-time
invariant trial quotients. They do not prove a continuum domain theorem,
an infinite-dimensional eigenvalue statement, or a physical mass gap.
The heat-factor additions test finite score projections, KL costs,
annular responses, an opposite-chaos kernel overlap, and Gaussian
moments of a fiber transformation that changes a source-chaos readout.
"""

from __future__ import annotations

import math
from decimal import Decimal, localcontext
from fractions import Fraction

import numpy as np


def joint_fisher_block_checks() -> None:
    """Build the adjoint heat matrix from Pauli commutators, then invert Fisher."""
    pauli = (
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    )
    generators = tuple(-0.5j*matrix for matrix in pauli)
    adjoint = []
    for a in range(3):
        matrix = np.zeros((3, 3))
        for b in range(3):
            bracket = generators[a]@generators[b]-generators[b]@generators[a]
            for c in range(3):
                coefficient = -2*np.trace(bracket@generators[c])
                assert abs(coefficient.imag) < 1e-14
                matrix[c, b] = coefficient.real
        assert np.array_equal(matrix.T, -matrix)
        adjoint.append(matrix)
    heat_generator = sum(matrix@matrix for matrix in adjoint)
    assert np.array_equal(heat_generator, -2*np.eye(3))
    eigenvalues, eigenvectors = np.linalg.eigh(heat_generator)
    swap = np.array([[0, 1], [1, 0]])
    test_left = np.array([0.2, -0.7, 0.4])
    test_right = np.array([-0.3, 0.1, 0.8])
    times = (0.001, 0.01, 0.3, 1.0, 3.0)
    for time in times:
        adjoint_mean = (eigenvectors*np.exp(time*eigenvalues))@eigenvectors.T
        rho = float(np.trace(adjoint_mean)/3)
        assert np.allclose(adjoint_mean, math.exp(-2*time)*np.eye(3), atol=2e-15)
        # Use velocity coordinates (h', -j'), paired with (p_L, p_R).
        # In the original (h', j') coordinates the Fisher off-diagonal
        # has the opposite sign and the observable covector is (p_L, -p_R).
        fisher = 0.5*np.array([[1, rho], [rho, 1]])
        inverse = np.linalg.inv(fisher)
        expected = (2/(1-rho*rho))*np.array([[1, -rho], [-rho, 1]])
        assert np.allclose(inverse, expected, rtol=2e-13, atol=2e-13)
        assert np.all(np.linalg.eigvalsh(fisher) > 0)
        assert np.all(np.linalg.eigvalsh(inverse) > 1)
        assert np.allclose(swap@inverse@swap, inverse, rtol=2e-13, atol=2e-13)
        for diagonal in (np.diag([2, 0]), np.diag([0, 2])):
            assert np.min(np.linalg.eigvalsh(inverse-diagonal)) > -5e-10
        gradients = np.array([test_left, test_right])
        contraction = float(np.einsum("ij,ia,ja->", inverse, gradients, gradients))
        split = (float(np.dot(test_left-test_right, test_left-test_right))/(1-rho)
                 + float(np.dot(test_left+test_right, test_left+test_right))/(1+rho))
        assert math.isclose(contraction, split, rel_tol=2e-13)
        excess = contraction-2*float(np.dot(test_left, test_left))
        square = 2*float(np.dot(test_right-rho*test_left,
                               test_right-rho*test_left))/(1-rho*rho)
        assert math.isclose(excess, square, rel_tol=2e-13)
        # Both excess-square equalities require p_R=r*p_L and
        # p_L=r*p_R. Their finite block has no nonzero solution.
        assert np.linalg.det(np.array([[-rho, 1], [1, -rho]])) < 0
    print("PASS Pauli-derived adjoint Casimir=2, five positive joint Fisher inversions, "
          "both one-hand domination tests and left/right exchange; finite equality block is nonsingular")


def class_trial_checks() -> None:
    """Stable SU(2) heat-law values, independently checked at 60 digits."""
    print("Joint neutral-character finite trial: heat-area t  b(t)  Rayleigh quotient")
    previous_quotient = math.inf
    for time in (1.0, 0.3, 0.1, 0.03, 0.01, 0.001, 0.00001):
        y = math.exp(-time/2)
        variance = math.expm1(-time/2)**2*(1+2*y+3*y*y)
        gradient = -0.75*math.expm1(-2*time)
        # cosh(t)=1+2*sinh(t/2)^2 avoids subtracting nearly equal
        # logarithms when t is small.
        b = 2*time+2*math.log1p(2*math.sinh(time/2)**2)
        quotient = b*gradient/variance
        with localcontext() as context:
            context.prec = 60
            t = Decimal(str(time))
            variance_d = 1+3*(-2*t).exp()-4*(-Decimal("1.5")*t).exp()
            gradient_d = Decimal("0.75")*(1-(-2*t).exp())
            b_d = 2*t+2*((t.exp()+(-t).exp())/2).ln()
            quotient_d = b_d*gradient_d/variance_d
        assert math.isclose(b, float(b_d), rel_tol=2e-14)
        assert math.isclose(quotient, float(quotient_d), rel_tol=2e-13)
        assert 2 < quotient < previous_quotient
        previous_quotient = quotient
        print(f"{time:9g}  {b:.10e}  {quotient:.10e}")
    print("PASS seven independent 60-digit joint character quotients; "
          "finite samples only, not a spectral-edge or eigenvalue proof")


def logarithmic_ramp_checks() -> None:
    """Integrate the entropy control with the actual 1-exp(-2s) weight.

    Let delta=1/2, epsilon=delta*exp(-L), and h'=xi/(s*L)
    on (epsilon,delta), with |xi|^2=1. The entropy control is
    (1/(2*L^2))*int (1-exp(-2s))/s^2 ds. In the variable
    u=log(s/epsilon) it has a smooth bounded integrand. The exact
    inequality 1-exp(-2s)<=2s proves the upper bound 1/L.
    Quadrature refinement is a finite accuracy test, not an error proof.
    """
    xi = (Fraction(3, 5), Fraction(4, 5), Fraction(0))
    assert sum(value*value for value in xi) == 1
    delta = 0.5
    grids = {order: np.polynomial.legendre.leggauss(order) for order in (64, 128, 256)}
    previous_entropy = math.inf
    print("Logarithmic-ramp finite entropy control: L  integrated value  analytic bound 1/L")
    for length in (2, 4, 8, 16, 32):
        values = []
        for nodes, weights in grids.values():
            u = (nodes+1)*length/2
            s = delta*np.exp(u-length)
            integrand = -np.expm1(-2*s)/s
            assert np.all(integrand > 0) and np.max(integrand) <= 2+2e-15
            values.append(float(np.dot(weights, integrand))/(4*length))
        assert max(abs(value-values[-1]) for value in values) < 2e-14
        bound = Fraction(1, length)
        assert 0 < values[-1] < float(bound)
        assert values[-1] < previous_entropy
        previous_entropy = values[-1]
        print(f"{length:2d}  {values[-1]:.10e}  {float(bound):.10e}")
    print("PASS five actual weighted logarithmic-ramp integrals with 64/128/256-point "
          "agreement; upper bound follows from 1-exp(-2s)<=2s, not extrapolation")


def weight_integrals(left: float, right: float):
    """Return integrals of 1/(1-r) and 1/(1+r), r=exp(-2s)."""
    assert 0 <= left < right
    plus = 0.5*(right-left
                + math.log1p(2*math.sinh(right/2)**2)
                - math.log1p(2*math.sinh(left/2)**2))
    minus = (0.5*(math.log(math.expm1(2*right))-math.log(math.expm1(2*left)))
             if left > 0 else math.inf)
    return minus, plus


def raw_coordinate_and_invariant_checks() -> None:
    """Actual quaternion gradients distinguish raw and invariant cylinders."""
    f = Fraction

    def cross(left, right):
        return (left[1]*right[2]-left[2]*right[1],
                left[2]*right[0]-left[0]*right[2],
                left[0]*right[1]-left[1]*right[0])

    def norm_squared(vector):
        return sum(value*value for value in vector)

    # For F(q)=v_3 at q=(0,e_1), grad_L=-e_2/2,
    # grad_R=e_2/2. Their difference is nonzero before its sole
    # positive readout time, unlike a conjugation-invariant cylinder.
    v = (f(1), f(0), f(0))
    covector = (f(0), f(0), f(1))
    rotation = cross(v, covector)
    left_gradient = tuple(value/2 for value in rotation)
    right_gradient = tuple(-value/2 for value in rotation)
    assert norm_squared(tuple(a-b for a, b in zip(left_gradient, right_gradient))) == 1
    assert norm_squared(tuple(a+b for a, b in zip(left_gradient, right_gradient))) == 0
    readout_time = 1.0
    # In the heat state E|p_L-p_R|^2=(1-exp(-2t))/2 and
    # E|p_L+p_R|^2=(1+3exp(-2t))/4, from f_fund=2w.
    mean_difference = -0.5*math.expm1(-2*readout_time)
    mean_sum = (1+3*math.exp(-2*readout_time))/4
    slope = mean_difference/2
    previous_value = -math.inf
    print("Raw-coordinate finite cutoff diagnostic: epsilon  pointwise response  heat-state response")
    for epsilon in (0.1, 0.001, 0.00001, 0.0000001):
        minus, plus = weight_integrals(epsilon, readout_time)
        average = mean_difference*minus+mean_sum*plus
        assert math.isfinite(minus) and average > previous_value
        previous_value = average
        # Its exact antiderivative already exposes the logarithm; these
        # finite values do not stand in for the non-domain proof.
        assert math.isclose(2*minus, math.log(math.expm1(2)/math.expm1(2*epsilon)),
                            rel_tol=2e-14)
        print(f"{epsilon:9g}  {minus:.10e}  {average:.10e}")

    scalar = (f(0), f(4, 5), f(0))
    vectors = ((f(1), f(0), f(0)), (f(0), f(3, 5), f(0)),
               (f(3, 5), f(0), f(4, 5)))
    assert all(w*w+norm_squared(v) == 1 for w, v in zip(scalar, vectors))
    cofactors = (cross(vectors[1], vectors[2]), cross(vectors[2], vectors[0]),
                 cross(vectors[0], vectors[1]))
    left, right = [], []
    for w, v, b in zip(scalar, vectors, cofactors):
        turn = cross(v, b)
        left.append(tuple((w*component+rotation)/2 for component, rotation in zip(b, turn)))
        right.append(tuple((w*component-rotation)/2 for component, rotation in zip(b, turn)))
    assert tuple(row[1] for row in left) == (f(9, 50), f(16, 50), -f(9, 50))
    assert tuple(row[1] for row in right) == (-f(9, 50), f(16, 50), f(9, 50))
    assert all(sum(row[a] for row in left) == sum(row[a] for row in right) for a in range(3))

    def joint_response(first, second):
        value = 0.0
        for interval in range(3):
            p = tuple(sum(row[a] for row in first[interval:]) for a in range(3))
            q = tuple(sum(row[a] for row in second[interval:]) for a in range(3))
            difference = norm_squared(tuple(a-b for a, b in zip(p, q)))
            together = norm_squared(tuple(a+b for a, b in zip(p, q)))
            minus, plus = weight_integrals(float(interval), float(interval+1))
            if interval == 0:
                assert difference == 0  # Do not numerically form 0*infinity.
            else:
                value += float(difference)*minus
            value += float(together)*plus
        return value

    joint = joint_response(left, right)
    assert math.isclose(joint, joint_response(right, left), rel_tol=2e-14)
    assert joint > float(f(481, 625)) > float(f(193, 625))
    print(f"PASS invariant quaternion determinant cancels the initial singular term: "
          f"joint response={joint:.10e}, above both one-hand values 193/625 and 481/625; "
          f"raw heat-state logarithmic coefficient={slope:.10e}")


def annular_restart_checks() -> dict[float, float]:
    """Test the actual increment readout and the joint clock's start dependence."""

    def multiply(left, right):
        scalar = left[0]*right[0]-float(np.dot(left[1:], right[1:]))
        vector = left[0]*right[1:]+right[0]*left[1:]+np.cross(left[1:], right[1:])
        return np.array([scalar, *vector])

    def inverse(value):
        return np.array([value[0], *(-value[1:])])

    def readout(x, y):
        return 2*multiply(inverse(x), y)[0]

    positions = tuple(np.array(value, dtype=float) for value in (
        (1, 0, 0, 0), (4/5, 0, 3/5, 0), (0, 3/5, 0, 4/5)))
    increments = tuple(np.array(value, dtype=float) for value in (
        (1, 0, 0, 0), (4/5, 3/5, 0, 0), (3/5, 0, 4/5, 0)))
    step = 1e-5
    different_frames = False
    for x in positions:
        assert math.isclose(float(x@x), 1)
        for z in increments:
            assert math.isclose(float(z@z), 1)
            y = multiply(x, z)
            # Q=-2Tr and T_a=-i*sigma_a/2: grad chi(z)=-vec(z).
            w = -z[1:]
            transported = multiply(multiply(x, np.array([0, *w])), inverse(x))
            assert abs(transported[0]) < 2e-14
            expected_left = np.array([-transported[1:], transported[1:]])
            expected_right = np.array([-w, w])
            assert np.array_equal(expected_left.sum(axis=0), np.zeros(3))
            assert np.array_equal(expected_right.sum(axis=0), np.zeros(3))
            assert math.isclose(float(w@w), 1-readout(x, y)**2/4, abs_tol=2e-14)
            finite_left, finite_right = np.zeros((2, 3)), np.zeros((2, 3))
            for axis in range(3):
                turn = np.zeros(4)
                turn[0], turn[axis+1] = math.cos(step/2), math.sin(step/2)
                back = inverse(turn)
                finite_left[0, axis] = (readout(multiply(turn, x), y)
                                        - readout(multiply(back, x), y))/(2*step)
                finite_left[1, axis] = (readout(x, multiply(turn, y))
                                        - readout(x, multiply(back, y)))/(2*step)
                finite_right[0, axis] = (readout(multiply(x, turn), y)
                                         - readout(multiply(x, back), y))/(2*step)
                finite_right[1, axis] = (readout(x, multiply(y, turn))
                                         - readout(x, multiply(y, back)))/(2*step)
            assert np.allclose(finite_left, expected_left, rtol=2e-10, atol=1e-10)
            assert np.allclose(finite_right, expected_right, rtol=2e-10, atol=1e-10)
            different_frames |= not np.allclose(expected_left, expected_right)
    assert different_frames

    # Before the first readout both cumulative gradients cancel. Inside
    # the annulus only the y derivatives remain: p_L=Ad_x*w, p_R=w.
    # Independence of x=X_s and z=X_s^-1 X_(s+t), and the adjoint
    # heat mean, give E<p_L,p_R>=exp(-2s)*J(t). Integrate the resulting
    # joint weight, rather than substitute the one-hand restart law.
    duration = 0.4
    j = -0.75*math.expm1(-2*duration)
    starts = (0.0, 0.2, 1.0, 5.0)
    grids = {order: np.polynomial.legendre.leggauss(order) for order in (64, 128, 256)}
    values = []
    for start in starts:
        quadratures = []
        for nodes, weights in grids.values():
            u = start+(nodes+1)*duration/2
            integrand = np.expm1(-2*(u+start))/np.expm1(-4*u)
            assert np.all(integrand > 0) and np.max(integrand) <= 1+2e-15
            quadratures.append(4*j*float(np.dot(weights, integrand))*duration/2)
        assert max(abs(value-quadratures[-1]) for value in quadratures) < 3e-14
        minus, plus = weight_integrals(start, start+duration)
        rho = math.exp(-2*start)
        # Independent partial fractions:
        # (1-rho*r)/(1-r^2)=(1-rho)/(2(1-r))+(1+rho)/(2(1+r)).
        primitive = plus if start == 0 else (1-rho)*minus/2+(1+rho)*plus/2
        assert math.isclose(quadratures[-1], 4*j*primitive, rel_tol=2e-13, abs_tol=3e-14)
        values.append(quadratures[-1])
    b = 2*duration+2*math.log1p(2*math.sinh(duration/2)**2)
    assert math.isclose(values[0], b*j, rel_tol=2e-13)
    assert all(left < right for left, right in zip(values, values[1:]))
    assert values[-1] < 4*duration*j
    print("Joint annular response at t=0.4: "
          + ", ".join(f"s={start:g}: {value:.10e}" for start, value in zip(starts, values))
          + f"; 4tJ comparison={4*duration*j:.10e}")
    print("PASS nine quaternion annular gradient transports and four 64/128/256-point "
          "integrals checked against analytic antiderivatives; same-clock restart fails "
          "in these finite samples, despite unchanged increment state laws")
    return dict(zip(starts, values))


def su2_adjoint_frames() -> tuple[np.ndarray, ...]:
    """Build actual group adjoints; the last four have zero adjoint mean.

    Giving the identity weight r and each remaining frame weight (1-r)/4
    reproduces E Ad_X=r I exactly. This finite cubature matches only that
    first adjoint moment; it is not a simulation of the path heat law.
    """
    pauli = (
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    )
    generators = tuple(-0.5j*matrix for matrix in pauli)
    identity = np.eye(2, dtype=complex)
    seed = (4/5)*identity+(6/5)*generators[0]
    group_elements = (identity, *(seed@q for q in
                                  (identity, *(2*t for t in generators))))
    frames = []
    for group in group_elements:
        assert np.allclose(group.conj().T@group, identity, atol=2e-15)
        assert abs(np.linalg.det(group)-1) < 2e-15
        adjoint = np.array([
            [-2*np.trace(group@b@group.conj().T@a) for b in generators]
            for a in generators
        ])
        assert np.max(np.abs(adjoint.imag)) < 2e-15
        frame = adjoint.real
        assert np.allclose(frame.T@frame, np.eye(3), atol=2e-15)
        frames.append(frame)
    assert np.allclose(sum(frames[1:]), np.zeros((3, 3)), atol=2e-15)
    assert any(not np.allclose(frame, frame.T) for frame in frames)
    return tuple(frames)


def heat_factor_fisher_checks() -> None:
    """Check the lift's source, observed, and discarded score covariances."""
    frames = su2_adjoint_frames()
    identity, zero = np.eye(3), np.zeros((3, 3))
    control = np.array([0.2, -0.7, 0.4, -0.3, 0.1, 0.8])
    times = (0.001, 0.01, 0.3, 1.0, 3.0)
    for alpha in (0.2, 0.5, 0.8):
        beta = 1-alpha
        source_map = np.block([[identity/math.sqrt(2*alpha), zero],
                               [zero, identity/math.sqrt(2*beta)]])
        source = 0.5*np.diag([1/alpha, 1/beta])
        observed_grams, missing_grams = [], []
        for frame in frames:
            rotation = np.block([
                [math.sqrt(alpha)*identity, -math.sqrt(beta)*frame],
                [math.sqrt(beta)*identity, math.sqrt(alpha)*frame],
            ])
            assert np.allclose(rotation@rotation.T, np.eye(6), atol=3e-15)
            assert np.allclose(rotation.T@rotation, np.eye(6), atol=3e-15)
            transformed = rotation@source_map
            observed_map, missing_map = transformed[:3], transformed[3:]
            assert np.allclose(observed_map, np.hstack((identity, -frame))/math.sqrt(2),
                               atol=3e-15)
            assert np.allclose(missing_map, np.hstack((math.sqrt(beta/alpha)*identity,
                                                      math.sqrt(alpha/beta)*frame))/math.sqrt(2),
                               atol=3e-15)
            # These are the projected and residual source-score vectors
            # in the original independent-noise coordinates. Their inner
            # product is their finite Gaussian score covariance.
            projected = rotation[:3].T@(observed_map@control)
            residual = rotation[3:].T@(missing_map@control)
            assert abs(float(projected@residual)) < 3e-15
            assert np.allclose(projected+residual, source_map@control, atol=3e-15)
            observed_grams.append(observed_map.T@observed_map)
            missing_grams.append(missing_map.T@missing_map)
        for time in times:
            rho = math.exp(-2*time)
            weights = (rho, *((1-rho)/4 for _ in range(4)))
            assert np.allclose(sum(w*frame for w, frame in zip(weights, frames)),
                               rho*identity, atol=3e-15)
            observed = sum(w*gram for w, gram in zip(weights, observed_grams))
            missing = sum(w*gram for w, gram in zip(weights, missing_grams))
            output_block = 0.5*np.array([[1, -rho], [-rho, 1]])
            missing_block = 0.5*np.array([[beta/alpha, rho], [rho, alpha/beta]])
            assert np.allclose(observed, np.kron(output_block, identity), atol=3e-15)
            assert np.allclose(missing, np.kron(missing_block, identity), atol=3e-15)
            assert np.allclose(observed+missing, np.kron(source, identity), atol=3e-15)
            assert np.allclose(source-output_block, missing_block, atol=3e-15)
            assert np.min(np.linalg.eigvalsh(output_block)) > 0
            assert np.min(np.linalg.eigvalsh(missing_block)) > 0
            assert math.isclose(np.linalg.det(missing_block), (1-rho*rho)/4,
                                rel_tol=3e-13, abs_tol=3e-15)
    print("PASS heat-factor alpha=0.2,0.5,0.8: 15 actual SU(2) 6x6 noise rotations "
          "and projected/residual score orthogonality; 15 source/output/missing "
          "Fisher blocks with positive discarded information")


def heat_factor_finite_kl_checks() -> None:
    """Integrate all three costs separately for K=L=exp(s T_3)."""
    terminal, casimir = 0.7, 2.0
    generator = np.diag([-0.5j, 0.5j])
    grids = {order: np.polynomial.legendre.leggauss(order) for order in (64, 128, 256)}
    for time in (0.0, 0.1, terminal):
        group = np.diag([np.exp(-0.5j*time), np.exp(0.5j*time)])
        derivative = generator@group
        body = group.conj().T@derivative
        spatial = derivative@group.conj().T
        assert np.allclose(body, generator, atol=2e-15)
        assert np.allclose(spatial, generator, atol=2e-15)
        assert abs(-2*np.trace(body@body)-1) < 2e-15
    results = []
    for alpha in (0.2, 0.5, 0.8):
        beta = 1-alpha
        integrals = []
        for nodes, weights in grids.values():
            times = (nodes+1)*terminal/2
            rho = np.exp(-casimir*times)
            source = np.full_like(times, (1/alpha+1/beta)/4)
            output = -0.5*np.expm1(-casimir*times)
            missing = (beta/alpha+alpha/beta+2*rho)/4
            integrals.append(np.array([np.dot(weights, row)*terminal/2
                                       for row in (source, output, missing)]))
        assert np.max(np.abs(np.array(integrals)-integrals[-1])) < 3e-14
        source, output, missing = integrals[-1]
        integrated_rho = -math.expm1(-casimir*terminal)/casimir
        expected = np.array([terminal*(1/alpha+1/beta)/4,
                             (terminal-integrated_rho)/2,
                             terminal*(beta/alpha+alpha/beta)/4+integrated_rho/2])
        assert np.allclose(integrals[-1], expected, rtol=3e-14, atol=3e-15)
        assert math.isclose(source, output+missing, rel_tol=3e-14)
        assert source > output > 0 and missing > 0
        results.append((alpha, source, output, missing))
    print("PASS finite KL K=L=exp(s T3), T=0.7, cA=2; alpha:(source,output,missing) "
          + "; ".join(f"{a:g}:({s:.10e},{o:.10e},{m:.10e})" for a, s, o, m in results)
          + "; separate 64/128/256-point integrals satisfy source=output+missing")


def lifted_annular_checks(prior_responses: dict[float, float]) -> None:
    """The pulled-back product form has no mixed left/right coefficient."""
    duration = 0.4
    gradient_mean = -0.75*math.expm1(-2*duration)
    expected = 2*duration*gradient_mean
    covector = np.array([0.2, -0.7, 0.4])
    frames = su2_adjoint_frames()
    values = []
    for alpha in (0.2, 0.5, 0.8):
        beta = 1-alpha
        inverse_source = 2*np.diag([alpha, beta])
        for frame in frames:
            gradients = np.array([frame@covector, -covector])
            contraction = float(np.einsum("ij,ia,ja->", inverse_source, gradients, gradients))
            assert math.isclose(contraction, 2*float(covector@covector), rel_tol=3e-14)
        for start, prior in prior_responses.items():
            # Both gradient tails vanish before s; on (s,s+t) their
            # squared norms have the same mean J(t), in different frames.
            value = 2*(alpha+beta)*duration*gradient_mean
            assert math.isclose(value, expected, rel_tol=3e-14)
            assert value < prior
            values.append(value)
    assert max(values)-min(values) < 2e-15
    print(f"PASS lifted annular response at t=0.4: 2tJ={expected:.10e} "
          "for s=0,0.2,1,5 and alpha=0.2,0.5,0.8; below each prior joint-Fisher "
          "response, despite the same output heat state")


def opposite_chaos_overlap_checks() -> None:
    """Check the normalized triangle integral, including cancellation-prone T.

    R(T)=2/T^2 int_0^T int_0^t exp(-cA*(t-s)) ds dt.
    This is a finite kernel overlap, not an independently computed
    infinite-dimensional chaos projection or spectral gap.
    """
    casimir = 2.0
    grids = {order: np.polynomial.legendre.leggauss(order) for order in (64, 128, 256)}
    results = []
    previous = 1.0
    for terminal in (1e-10, 1e-6, 0.001, 0.1, 0.7, 3.0):
        x = casimir*terminal
        if x < 0.01:
            term, ratio = 1.0, 1.0
            for order in range(1, 40):
                term *= -x/(order+2)
                ratio += term
                if abs(term) < 1e-18:
                    break
        else:
            ratio = 2*(x+math.expm1(-x))/(x*x)
        with localcontext() as context:
            context.prec = 80
            x_d = Decimal(str(casimir))*Decimal(str(terminal))
            ratio_d = 2*(x_d-1+(-x_d).exp())/(x_d*x_d)
        quadratures = []
        for nodes, weights in grids.values():
            unit, unit_weights = (nodes+1)/2, weights/2
            kernel = np.exp(-x*unit[:, None]*(1-unit[None, :]))
            quadratures.append(float(2*np.einsum("i,j,ij,i->", unit_weights,
                                                 unit_weights, kernel, unit)))
        assert math.isclose(ratio, float(ratio_d), rel_tol=3e-14, abs_tol=3e-15)
        assert max(abs(value-ratio) for value in quadratures) < 5e-14
        assert 0 < ratio < previous
        previous = ratio
        results.append(ratio)
    print("PASS opposite-chaos constant-triangle overlap: six 64/128/256-point "
          "double integrals and 80-digit closed forms; "
          f"R(1e-10)={results[0]:.12f}, R(0.7)={results[4]:.12f}, "
          f"R(3)={results[5]:.12f}; finite overlap checks only")


def heat_factor_fiber_chaos_checks() -> None:
    """Check the finite moments in the exact non-descent witness.

    This tests the Pauli tensor coefficient and a degree-four Gaussian
    integral independently. It does not approximate the conditional
    expectation onto the full path readout or prove semigroup non-descent.
    """
    terminal, casimir, speed = 0.7, 0.75, 1.2
    pauli = (
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    )
    generators = tuple(-0.5j*matrix for matrix in pauli)
    interaction = 2*sum(np.kron(g, g) for g in generators)
    eigenvalues, eigenvectors = np.linalg.eigh(interaction)
    chaos_norm = 1.5*terminal**2*math.exp(-2*casimir*terminal)
    tensor_coefficient = (terminal**2/2*math.exp(-2*casimir*terminal)
                          *np.trace(interaction@interaction).real)
    assert math.isclose(tensor_coefficient, chaos_norm, rel_tol=2e-14)
    for alpha in (0.2, 0.5, 0.8):
        beta = 1-alpha
        # Deterministic fiber shifts contribute identical drift terms
        # to sqrt(alpha) B_U and sqrt(beta) B_V, hence cancel.
        drift = math.sqrt(alpha)/math.sqrt(2*alpha)-math.sqrt(beta)/math.sqrt(2*beta)
        assert abs(drift) < 2e-15
        for rho in (0.0, 0.4, 1.0):
            rates = -2*casimir+rho*eigenvalues
            factor_u = (eigenvectors*np.exp(alpha*terminal*rates))@eigenvectors.conj().T
            factor_v = (eigenvectors*np.exp(beta*terminal*rates))@eigenvectors.conj().T
            moment = np.trace(factor_u@factor_v)
            target = math.exp(-1.5*terminal)*(math.exp(1.5*rho*terminal)
                                             +3*math.exp(-0.5*rho*terminal))
            assert abs(moment-target) < 4e-14

    angle = speed*terminal
    sine, cosine = math.sin(angle), math.cos(angle)
    integrated_rotation = np.array([
        [sine/speed, (1-cosine)/speed, 0],
        [(cosine-1)/speed, sine/speed, 0],
        [0, 0, terminal],
    ])
    for order in (16, 32, 64):
        nodes, weights = np.polynomial.legendre.leggauss(order)
        times = terminal*(nodes+1)/2
        rotations = np.zeros((order, 3, 3))
        rotations[:, 0, 0] = rotations[:, 1, 1] = np.cos(speed*times)
        rotations[:, 1, 0] = -np.sin(speed*times)
        rotations[:, 0, 1] = np.sin(speed*times)
        rotations[:, 2, 2] = 1
        integral = terminal/2*np.einsum("n,nij->ij", weights, rotations)
        assert np.allclose(integral, integrated_rotation, rtol=2e-14, atol=2e-15)

    # (Z,Z^k) is one six-dimensional Gaussian with this covariance.
    # Three-point Hermite quadrature in each coordinate integrates the
    # fourth-degree squared difference exactly, up to floating precision.
    covariance = np.block([
        [terminal*np.eye(3), integrated_rotation.T],
        [integrated_rotation, terminal*np.eye(3)],
    ])
    values, vectors = np.linalg.eigh(covariance)
    assert np.min(values) > -2e-14
    root = (vectors*np.sqrt(np.maximum(values, 0)))@vectors.T
    nodes, weights = np.polynomial.hermite.hermgauss(3)
    indices = np.indices((3,)*6).reshape(6, -1).T
    gaussian = math.sqrt(2)*nodes[indices]@root.T
    quadrature_weights = np.prod(weights[indices]/math.sqrt(math.pi), axis=1)
    squared = np.sum(gaussian[:, :3]**2, axis=1)
    rotated_squared = np.sum(gaussian[:, 3:]**2, axis=1)
    delta = rotated_squared-squared
    raw_variance = float(quadrature_weights@(delta*delta))
    target_variance = 4*(3*terminal**2-np.sum(integrated_rotation**2))
    assert np.isfinite(raw_variance) and raw_variance > 0
    assert math.isclose(raw_variance, target_variance, rel_tol=3e-13)
    assert abs(float(quadrature_weights@delta)) < 2e-14
    projected = -0.5*math.exp(-casimir*terminal)*(squared-3*terminal)
    assert math.isclose(float(quadrature_weights@(projected*projected)),
                        chaos_norm, rel_tol=3e-14)
    projected_variance = math.exp(-2*casimir*terminal)*raw_variance/4
    assert math.isclose(projected_variance,
                        math.exp(-2*casimir*terminal)
                        *(3*terminal**2-np.sum(integrated_rotation**2)),
                        rel_tol=3e-13)
    # A constant identity frame preserves the same squared norm.
    assert abs(4*(3*terminal**2-np.sum((terminal*np.eye(3))**2))) < 2e-15
    print("PASS heat-factor Pauli tensor moments and second-chaos norm; "
          "16/32/64-point smooth-frame integrals and 729-node Gaussian test: "
          f"raw squared-norm change variance={raw_variance:.12g}, "
          f"source-chaos change variance={projected_variance:.12g}. "
          "Finite moment checks; the path-fiber proof establishes non-descent.")


def charged_cut_twist_checks() -> None:
    """Differentiate the actual three-holonomy readout in both cut frames."""
    pauli = (
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    )
    generators = tuple(-0.5j*matrix for matrix in pauli)

    def group(w: float, v: np.ndarray) -> np.ndarray:
        # PF13 quaternion convention: g=w I-i v.sigma.
        return w*np.eye(2)-1j*sum(v[a]*pauli[a] for a in range(3))

    def vector(matrix: np.ndarray) -> np.ndarray:
        return np.array([(0.5j*np.trace(p@matrix)).real for p in pauli])

    whole = (
        group(0, np.array([1., 0., 0.])),
        group(4/5, np.array([0., 3/5, 0.])),
        group(0, np.array([3/5, 0., 4/5])),
    )
    vectors = tuple(vector(g) for g in whole)
    derivatives = (
        np.cross(vectors[1], vectors[2]),
        np.cross(vectors[2], vectors[0]),
        np.cross(vectors[0], vectors[1]),
    )

    def differential(changes: dict[int, np.ndarray]) -> float:
        return sum(float(derivatives[i]@vector(delta)) for i, delta in changes.items())

    left = np.array([[differential({i: h@g}) for h in generators]
                     for i, g in enumerate(whole)])
    right = np.array([[differential({i: g@h}) for h in generators]
                      for i, g in enumerate(whole)])
    assert np.allclose(left[:, 1], np.array([9, 16, -9])/50, atol=2e-15)
    assert np.allclose(right[:, 1], np.array([-9, 16, 9])/50, atol=2e-15)
    assert np.linalg.norm(np.sum(left-right, axis=0)) < 2e-15
    kernel = np.minimum.outer([1., 2., 3.], [1., 2., 3.])
    whole_l = float(2*np.einsum("ij,ia,ja->", kernel, left, left))
    whole_r = float(2*np.einsum("ij,ia,ja->", kernel, right, right))
    first, boundary, endpoint = whole
    future_left = boundary.conj().T@endpoint
    future_right = endpoint@boundary.conj().T
    assert np.allclose(boundary@future_left, future_right@boundary, atol=2e-15)

    # Differentiate F(A1,A2,A2 Y) directly, with Y held fixed
    # when A2 changes. This is the genuinely untwisted product frame.
    cut_left = np.array([
        [differential({0: h@first}) for h in generators],
        [differential({1: h@boundary, 2: h@endpoint}) for h in generators],
        [differential({2: boundary@h@future_left}) for h in generators],
    ])
    cut_right_naive = np.array([
        [differential({0: first@h}) for h in generators],
        [differential({1: boundary@h, 2: boundary@h@future_left}) for h in generators],
        [differential({2: endpoint@h}) for h in generators],
    ])
    # Now differentiate F(A1,A2,W A2), i.e. apply the actual twist
    # before the product right response. W, not Y, is held fixed.
    cut_right_twisted = np.array([
        [differential({0: first@h}) for h in generators],
        [differential({1: boundary@h, 2: endpoint@h}) for h in generators],
        [differential({2: future_right@h@boundary}) for h in generators],
    ])
    cut_kernel = np.array([[1., 1., 0.], [1., 2., 0.], [0., 0., 1.]])

    def cut_response(gradient: np.ndarray) -> float:
        return float(2*np.einsum("ij,ia,ja->", cut_kernel, gradient, gradient))

    assert math.isclose(whole_l, 193/625, rel_tol=3e-14)
    assert math.isclose(whole_r, 481/625, rel_tol=3e-14)
    assert math.isclose(cut_response(cut_left), whole_l, rel_tol=3e-14)
    assert math.isclose(cut_response(cut_right_twisted), whole_r, rel_tol=3e-14)
    naive = cut_response(cut_right_naive)
    assert math.isclose(naive, 67/625, rel_tol=3e-14)
    assert not math.isclose(naive, whole_r, rel_tol=1e-3)
    for alpha in (0.2, 0.5, 0.8):
        beta = 1-alpha
        actual = alpha*whole_l+beta*whole_r
        sewn = alpha*cut_response(cut_left)+beta*cut_response(cut_right_twisted)
        assert math.isclose(actual, sewn, rel_tol=3e-14)
        assert math.isclose(actual-(alpha*whole_l+beta*naive),
                            beta*414/625, rel_tol=3e-14)
    direct = (first@boundary)@endpoint@(first@boundary).conj().T
    nested = first@(boundary@endpoint@boundary.conj().T)@first.conj().T
    assert np.allclose(direct, nested, atol=2e-15)
    print("PASS charged cut via actual matrix derivatives: whole L=193/625, "
          "whole R=481/625, naive tensor R=67/625; boundary twist restores "
          "the full response for alpha=.2,.5,.8. Three-cut adjoint composition "
          "also checked; these finite witnesses do not prove the core-closure law.")


def conditional_boundary_frame_checks() -> None:
    """Finite conditional-block and charged-fiber witnesses; not a domain proof."""
    identity = np.eye(3)
    p = np.array([0.2, -0.7, 0.4])
    q = np.array([-0.3, 0.1, 0.8])
    largest_error = 0.0
    for frame in su2_adjoint_frames():
        for duration in (0.001, 0.1, 0.7):
            rho = math.exp(-2*duration)
            # Covector coordinates are (p_L,-p_R), as in JF6--JF9.
            conditional = 0.5*np.block([
                [identity, -rho*frame],
                [-rho*frame.T, identity],
            ])
            source_rotation = np.block([
                [frame, np.zeros((3, 3))],
                [np.zeros((3, 3)), identity],
            ])
            rooted = 0.5*np.kron(np.array([[1, -rho], [-rho, 1]]), identity)
            assert np.allclose(source_rotation.T@conditional@source_rotation, rooted, atol=3e-15)
            covector = np.r_[p, -q]
            returned = float(covector@np.linalg.solve(conditional, covector))
            expected = (np.linalg.norm(frame.T@p-q)**2/(1-rho)
                        + np.linalg.norm(frame.T@p+q)**2/(1+rho))
            error = abs(returned-expected)/max(1, abs(expected))
            largest_error = max(largest_error, error)
            assert error < 3e-13

    pauli = (
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    )
    generators = tuple(-0.5j*matrix for matrix in pauli)
    boundary, future = 1j*pauli[2], 1j*pauli[0]
    left = np.array([np.trace(boundary@generator@future).real for generator in generators])
    right = np.array([np.trace(boundary@future@generator).real for generator in generators])
    assert np.allclose(left, [0, 1, 0], atol=1e-15)
    assert np.allclose(right, [0, -1, 0], atol=1e-15)
    turn = (np.eye(2)+1j*pauli[1])/math.sqrt(2)
    whole = np.trace(boundary@future)
    joint_rotated = np.trace((turn@boundary@turn.conj().T)@(turn@future@turn.conj().T))
    assert abs(whole-joint_rotated) < 1e-14
    old_response = -math.inf
    print("Conditional future-fiber cutoff witness for globally neutral chi(BZ):")
    for epsilon in (0.1, 0.001, 0.00001, 0.0000001):
        minus, plus = weight_integrals(epsilon, 1.0)
        response = np.linalg.norm(left-right)**2*minus + np.linalg.norm(left+right)**2*plus
        assert response > old_response
        old_response = response
        print(f"  epsilon={epsilon:.7g} response={response:.10g}")
    print(f"PASS 15 conditional boundary-frame blocks; largest relative dual error={largest_error:.3g}. "
          "Pauli witness is jointly neutral but has nonzero future conjugation derivative. "
          "Finite cutoff growth illustrates, not proves, the domain exclusion.")


def gauge_vertex_source_checks() -> None:
    """Haar vertex variables plus independent heat-factor source actions.

    X_e=B_s U_e V_e^{-1} B_t^{-1}; U,V have heat speeds a*alpha,
    a*(1-alpha). Vertex left actions preserve their Haar source law.
    Their zero Fisher cost forces invariant observable derivatives to
    vanish. Edge endpoint covectors are dualized BEFORE any averaging.
    These pointwise samples are not samples from the heat path law.
    """
    pauli = (
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    )
    generators = np.array([-0.5j*p for p in pauli])
    identity = np.eye(2, dtype=complex)
    rng = np.random.default_rng(20260908)

    def close(actual, expected, *, rtol=3e-12, atol=3e-13):
        assert np.all(np.isfinite(actual)) and np.all(np.isfinite(expected))
        assert np.allclose(actual, expected, rtol=rtol, atol=atol), (actual, expected)

    def group():
        q = rng.normal(size=4)
        q /= np.linalg.norm(q)
        return q[0]*identity+2*sum(q[a+1]*generators[a] for a in range(3))

    def quaternion(u):
        return np.array([np.trace(u).real/2] + [-np.trace(t@u).real for t in generators])

    def adjoint(u):
        return np.array([[-2*np.trace(a@u@b@u.conj().T).real for b in generators]
                         for a in generators])

    pairs, determinants = ((0, 2), (0, 4)), ((0, 1, 2, 3), (0, 1, 3, 5))
    speeds = np.array([.35, .7, 1.1, 1.5, 2.3, .9])
    noninvariant_vertex_derivative = False
    for terminal in (.2, .7, 1.3):
        bs, bt = group(), group()
        us, vs = [group() for _ in range(6)], [group() for _ in range(6)]
        outputs = [bs@u@v.conj().T@bt.conj().T for u, v in zip(us, vs)]
        coordinates = np.array([quaternion(x) for x in outputs])

        def values(xs):
            qs = np.array([quaternion(x) for x in xs])
            return np.array([qs[i]@qs[j] for i, j in pairs]
                            + [np.linalg.det(qs[list(indices)]) for indices in determinants])

        def differential(changes):
            dq = {edge: quaternion(delta) for edge, delta in changes.items()}
            result = []
            for i, j in pairs:
                result.append((dq[i]@coordinates[j] if i in dq else 0)
                              + (coordinates[i]@dq[j] if j in dq else 0))
            for indices in determinants:
                value = 0.0
                for row, edge in enumerate(indices):
                    if edge in dq:
                        matrix = coordinates[list(indices)].copy()
                        matrix[row] = dq[edge]
                        value += np.linalg.det(matrix)
                result.append(value)
            return np.array(result)

        left, right, source_u, source_v = (np.zeros((4, 6, 3)) for _ in range(4))
        for edge, (u, v, x) in enumerate(zip(us, vs, outputs)):
            for axis, t in enumerate(generators):
                left[:, edge, axis] = differential({edge: t@x})
                right[:, edge, axis] = differential({edge: x@t})
                source_u[:, edge, axis] = differential({edge: bs@t@u@v.conj().T@bt.conj().T})
                source_v[:, edge, axis] = differential({edge: -bs@u@v.conj().T@t@bt.conj().T})
        close(source_u, np.einsum("pea,ab->peb", left, adjoint(bs)))
        close(source_v, -np.einsum("pea,ab->peb", right, adjoint(bt)))
        close(np.einsum("pea,qea->pqe", left, left), np.einsum("pea,qea->pqe", right, right))

        # Actual left actions on the two vertex source variables.
        for t in generators:
            close(differential({e: t@x for e, x in enumerate(outputs)}), np.zeros(4))
            close(differential({e: -x@t for e, x in enumerate(outputs)}), np.zeros(4))
            noninvariant_vertex_derivative |= abs(quaternion(t@outputs[0])[0]) > 1e-4
        step = 2e-4
        for edge in (0, 4):
            for axis, t in enumerate(generators):
                turn = math.cos(step/2)*identity+2*math.sin(step/2)*t
                for factor in ("u", "v"):
                    plus, minus = list(outputs), list(outputs)
                    u, v = us[edge], vs[edge]
                    if factor == "u":
                        plus[edge] = bs@turn@u@v.conj().T@bt.conj().T
                        minus[edge] = bs@turn.conj().T@u@v.conj().T@bt.conj().T
                        target = source_u[:, edge, axis]
                    else:
                        plus[edge] = bs@u@v.conj().T@turn.conj().T@bt.conj().T
                        minus[edge] = bs@u@v.conj().T@turn@bt.conj().T
                        target = source_v[:, edge, axis]
                    close((values(plus)-values(minus))/(2*step), target, rtol=5e-9, atol=3e-12)

        expected = 2*terminal*np.einsum("e,pea,qea->pq", speeds, left, left)
        for alphas in (np.full(6, .2), np.full(6, .8), rng.uniform(.1, .9, size=6)):
            response = np.zeros((4, 4))
            for edge, (a, alpha) in enumerate(zip(speeds, alphas)):
                # Minimum path Fisher cost for a prescribed endpoint tangent.
                fisher = np.diag(np.repeat([1/(2*a*terminal*alpha),
                                            1/(2*a*terminal*(1-alpha))], 3))
                covectors = np.concatenate((source_u[:, edge], source_v[:, edge]), axis=1)
                response += covectors@np.linalg.solve(fisher, covectors.T)
            close(response, expected)
            assert np.min(np.linalg.eigvalsh(response)) > -1e-12
        rate0 = 2*speeds[0]*terminal
        s02, s04 = coordinates[0]@coordinates[2], coordinates[0]@coordinates[4]
        close(expected[0, 1], rate0/4*(coordinates[2]@coordinates[4]-s02*s04))
        replaced = coordinates[list(determinants[0])].copy()
        replaced[0] = coordinates[4]
        close(expected[2, 1], rate0/4*(np.linalg.det(replaced)-values(outputs)[2]*s04))
        quotient = outputs[0]@outputs[1].conj().T
        actual_source_word = bs@us[0]@vs[0].conj().T@vs[1]@us[1].conj().T@bs.conj().T
        close(quotient, actual_source_word)
    assert noninvariant_vertex_derivative
    print("PASS Haar-vertex source: actual B_s/U/V/B_t chain rule for four invariant probes, "
          "both boundary adjoint frames, zero vertex derivatives and nonzero raw-coordinate witness; "
          "nine six-edge Fisher sweeps return rates 2*a_e*T and the pair/determinant cross-responses")

    # Independent finite representation moments of the two-edge source word.
    # Each heat factor contributes its own matrix exponential; inverse
    # factors give the same self-adjoint expectation. The tensor block
    # checks both singlet and triplet, not only the fundamental mean.
    tensor_generators = [np.kron(t, identity)+np.kron(identity, t) for t in generators]
    casimir = sum(t@t for t in generators)
    tensor_casimir = sum(t@t for t in tensor_generators)
    close(casimir, -.75*identity)
    fundamental_values, fundamental_vectors = np.linalg.eigh(casimir)
    eigenvalues, eigenvectors = np.linalg.eigh(tensor_casimir)
    close(eigenvalues, [-2, -2, -2, 0])
    for terminal in (.2, .7, 1.3):
        a1, a2 = .6, 1.4
        total_time = (a1+a2)*terminal
        for alpha1, alpha2 in ((.2, .8), (.5, .3), (.87, .61)):
            times = terminal*np.array([a1*alpha1, a1*(1-alpha1),
                                       a2*(1-alpha2), a2*alpha2])
            first, second = identity.copy(), np.eye(4, dtype=complex)
            for time in times:
                fundamental_mean = (fundamental_vectors*np.exp(time*fundamental_values))@fundamental_vectors.conj().T
                first = first@fundamental_mean
                tensor_mean = (eigenvectors*np.exp(time*eigenvalues))@eigenvectors.conj().T
                second = second@tensor_mean
            close(np.trace(first), 2*math.exp(-.75*total_time))
            close(np.trace(second), 1+3*math.exp(-2*total_time))
    print("PASS two-parallel-edge source heat moments at nine independent splits: "
          "quotient heat time=(a1+a2)*T, including fundamental mean and singlet/triplet tensor moment. "
          "Analytic convolution supplies the full density; no Wilson state or source-OU descent claimed.")


def tilted_self_loop_fisher_checks() -> None:
    """Finite heat-law and source-entropy checks for an actual tilted self-loop.

    Tilt the two-factor source by exp(lambda*q(U_T V_T^-1)), q=Tr/2.
    The source ramps are U_s -> exp(epsilon*s*xi/T) U_s and
    V_s -> exp(epsilon*s*eta/T) V_s, with t=a*T and factor split theta.
    Matrix quadrature tests the endpoint term in the exact path-entropy
    identity; it does not simulate path scores. Its baseline path cost
    and zero tilted stochastic-log mean require the analytic proof.
    The analytic arbitrary-path entropy identity makes the added Fisher
    term endpoint-only, so the bridge/ramp split identifies the full
    endpoint-control dual with this ramp inverse for this ONE self-loop.
    That proof is not replaced by the finite matrix checks below. The
    endpoint marginal experiment has a different Fisher metric.
    """
    pauli = np.array(([[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]))
    generators = -.5j*pauli
    identity = np.eye(2, dtype=complex)
    directions = np.r_[np.eye(3), -np.eye(3)]
    xi, eta = np.array([.2, -.7, .4]), np.array([-.3, .1, .8])
    assert np.linalg.norm(np.cross(xi, eta)) > .1

    def close(actual, expected, *, rtol=2e-11, atol=2e-13):
        assert np.all(np.isfinite(actual)) and np.all(np.isfinite(expected))
        assert np.allclose(actual, expected, rtol=rtol, atol=atol), (actual, expected)

    def turn(control, epsilon):
        length = np.linalg.norm(control)
        matrix = np.einsum("a,aij->ij", control, generators)
        result = math.cos(epsilon*length/2)*identity + 2*math.sin(epsilon*length/2)*matrix/length
        close(result.conj().T@result, identity)
        return result

    def heat_quadrature(time, order):
        angle = np.arange(1, order+1)*math.pi/(order+1)
        q = np.cos(angle)
        haar = 2*np.sin(angle)**2/(order+1)
        # SU(2) characters U_l(q) are generated rather than numerically
        # dividing sin((l+1)*angle) by sin(angle). The uniform heat-tail
        # bound uses |U_l|<=l+1 and the decreasing ratio of positive terms.
        cutoff = 32
        previous, current = np.ones(order), 2*q
        heat = previous + 2*math.exp(-.75*time)*current
        for ell in range(2, cutoff+1):
            following = 2*q*current-previous
            heat += (ell+1)*math.exp(-ell*(ell+2)*time/4)*following
            previous, current = current, following
        ell = cutoff+1
        first_tail = (ell+1)**2*math.exp(-ell*(ell+2)*time/4)
        ratio = ((ell+2)/(ell+1))**2*math.exp(-(2*ell+3)*time/4)
        assert ratio < 1 and first_tail/(1-ratio) < 1e-30
        assert np.min(heat) > -2e-13
        # No heat-density clipping or discarded quadrature nodes.
        return q, haar*heat

    response_derivatives = []
    moment_checks = entropy_checks = 0
    for time in (.3, .7, 1.3):
        grids = [heat_quadrature(time, order) for order in (48, 96, 192)]
        q, heat_weights = grids[-1]
        close(heat_weights.sum(), 1)
        mean0, second0 = math.exp(-.75*time), (1+3*math.exp(-2*time))/4
        close(heat_weights@q, mean0)
        close(heat_weights@(q*q), second0)
        variance0 = second0-mean0**2

        # Six angular directions integrate every linear or quadratic
        # quaternion expression used here. This is not a heat-path sample.
        vectors = np.sqrt(1-q*q)[:, None, None]*directions[None, :, :]
        groups = q[:, None, None, None]*identity + 2*np.einsum("nka,aij->nkij", vectors, generators)
        gradients = np.array([np.trace(t@groups, axis1=-2, axis2=-1).real/2
                              for t in generators]).transpose(1, 2, 0)
        close(gradients, -vectors/2)
        gradient_squared = np.sum(gradients**2, axis=-1)
        close(gradient_squared, np.broadcast_to((1-q*q)[:, None]/4, gradient_squared.shape))
        gradient_mean = float(heat_weights@gradient_squared.mean(axis=1))
        close(gradient_mean, 3*(1-math.exp(-2*time))/16)

        def tilted_mean(coupling):
            weights = heat_weights*np.exp(coupling*q)
            return float(weights@q/weights.sum())

        step = 2e-4
        mean_derivative = (tilted_mean(step)-tilted_mean(-step))/(2*step)
        close(mean_derivative, variance0, rtol=2e-8)
        for coupling in (0., .2, 1., 2.5):
            refined = []
            for nodes, weights in grids:
                tilted = weights*np.exp(coupling*nodes)
                refined.append(np.array([tilted.sum(), tilted@nodes/tilted.sum(),
                                         tilted@(nodes*nodes)/tilted.sum()]))
            close(refined, np.broadcast_to(refined[-1], (3, 3)))
            tilted = heat_weights*np.exp(coupling*q)
            tilted /= tilted.sum()
            mean = float(tilted@q)
            close(np.einsum("n,nkij->ij", tilted/6, groups), mean*identity)
            moment_checks += 1
            for theta in (.2, .5, .8):
                baseline = xi@xi/(2*time*theta)+eta@eta/(2*time*(1-theta))
                target_hessian = baseline+coupling*mean*np.linalg.norm(xi-eta)**2/4

                def entropy(epsilon):
                    left, right = turn(xi, epsilon), turn(eta, epsilon)
                    moved = left@groups@right.conj().T
                    delta_q = q[:, None]-np.trace(moved, axis1=-2, axis2=-1).real/2
                    endpoint_term = float(tilted@delta_q.mean(axis=1))
                    expected = mean*(1-np.trace(left@right.conj().T).real/2)
                    close(endpoint_term, expected, atol=7e-16)
                    return epsilon**2*baseline/2+coupling*endpoint_term

                for epsilon in (.15, .4, .7):
                    assert entropy(epsilon) > 0
                hessians = []
                for epsilon in (.002, .001):
                    hessians.append((entropy(epsilon)+entropy(-epsilon))/epsilon**2)
                richardson = (4*hessians[1]-hessians[0])/3
                close(richardson, target_hessian, rtol=3e-9, atol=3e-9)
                baseline_matrix = np.diag([1/(2*time*theta), 1/(2*time*(1-theta))])
                coupling_matrix = coupling*mean*np.array([[1., -1.], [-1., 1.]])/4
                fisher = np.kron(baseline_matrix+coupling_matrix, np.eye(3))
                assert np.min(np.linalg.eigvalsh(fisher)) > 0
                covectors = np.concatenate((gradients, -gradients), axis=-1)
                inverse = np.linalg.solve(fisher, np.eye(6))
                response = np.einsum("nka,ab,nkb->nk", covectors, inverse, covectors)
                rate = 2*time/(1+coupling*mean*time/2)
                close(response, rate*gradient_squared)
                entropy_checks += 1

        # Independently invert the 6x6 ramp block and differentiate its
        # contraction with actual Pauli observable gradients (w,-w).
        # The full endpoint representer is a ramp by the analytic
        # endpoint-only perturbation and orthogonal bridge/ramp split.
        # In this comparison keep the state fixed: its first derivative
        # cancels between actual and frozen-response energies at zero.
        derivative_values = []
        for theta in (.2, .5, .8):
            baseline = np.diag([1/(2*time*theta), 1/(2*time*(1-theta))])
            direction = np.array([[1., -1.], [-1., 1.]])
            covectors = np.concatenate((gradients, -gradients), axis=-1)
            energies = []
            for coupling in (-step, step):
                fisher = np.kron(baseline+coupling*tilted_mean(coupling)*direction/4, np.eye(3))
                assert np.min(np.linalg.eigvalsh(fisher)) > 0
                inverse = np.linalg.solve(fisher, np.eye(6))
                pointwise = np.einsum("nka,ab,nkb->nk", covectors, inverse, covectors)
                energies.append(float(heat_weights@pointwise.mean(axis=1)))
            derivative_values.append((energies[1]-energies[0])/(2*step))
        target = -time*time*mean0*gradient_mean
        close(derivative_values, np.full(3, target), rtol=3e-8, atol=3e-10)
        response_derivatives.append(target)
    print(f"PASS tilted self-loop: {moment_checks} 48/96/192-node heat-law moment tests, "
          "uniform omitted heat-series bound <1e-30, and m'(0)=Var(q); "
          f"{entropy_checks} nonparallel Pauli ramp entropy Hessians and full endpoint-control "
          "block inversions match the cross term and rate 2t/(1+lambda*m_lambda*t/2)")
    print("PASS actual-minus-frozen response energy derivative for q at t=.3,.7,1.3: "
          + ", ".join(f"{value:.12g}" for value in response_derivatives)
          + "; three ramp splits agree. Finite quadrature/matrix diagnostics only: "
          "the arbitrary-path entropy and bridge/ramp proof supply the full endpoint dual "
          "for this one self-loop, not the endpoint marginal Fisher experiment or a physical gap.")

    # Subdivision keeps the same tilted product readout state, but not
    # its source-derived response. Only the derivative at zero coupling
    # is used below: the fine finite-coupling Fisher is not supplied by
    # simply retaining this unperturbed, linearized Hessian.
    q1, q2 = np.array([4/5, 3/5, 0., 0.]), np.array([3/5, 0., 4/5, 0.])
    y1 = q1[0]*identity+2*np.einsum("a,aij->ij", q1[1:], generators)
    y2 = q2[0]*identity+2*np.einsum("a,aij->ij", q2[1:], generators)
    product = y1@y2
    w = np.array([np.trace(t@product).real/2 for t in generators])
    z = np.array([np.trace(y1@t@y2).real/2 for t in generators])
    expected_rows = np.array([w, -z, z, -w])

    def fine_readout(controls):
        factors = [turn(row, 1.) if np.linalg.norm(row) else identity for row in controls]
        return np.trace(factors[0]@y1@factors[1].conj().T
                        @factors[2]@y2@factors[3].conj().T).real/2

    actual_rows = np.zeros((4, 3))
    step = 1e-5
    for row in range(4):
        for axis in range(3):
            control = np.zeros((4, 3))
            control[row, axis] = step
            actual_rows[row, axis] = (fine_readout(control)-fine_readout(-control))/(2*step)
    close(actual_rows, expected_rows, rtol=3e-10, atol=2e-11)
    close(np.linalg.norm(w-z)**2, np.linalg.norm(np.cross(q1[1:], q2[1:]))**2)
    assert np.linalg.norm(w-z) > .1

    # Independently differentiate the Pauli word left after averaging
    # independent unperturbed Y1,Y2. Its Hessian is the rank-three sum
    # of all four signed source directions, including off-diagonal blocks.
    signs = np.array([1., -1., 1., -1.])
    unit_hessian = np.kron(np.outer(signs, signs)/4, np.eye(3))

    def averaged_word_potential(control):
        word = identity
        for sign, row in zip(signs, control.reshape(4, 3)):
            if np.linalg.norm(row):
                word = word@turn(row, sign)
        return 1-np.trace(word).real/2

    basis, epsilon = np.eye(12), .001
    measured_hessian = np.zeros((12, 12))
    for i in range(12):
        for j in range(12):
            measured_hessian[i, j] = sum(
                si*sj*averaged_word_potential(epsilon*(si*basis[i]+sj*basis[j]))
                for si in (-1., 1.) for sj in (-1., 1.)
            )/(4*epsilon**2)
    close(measured_hessian, unit_hessian, rtol=4e-7, atol=3e-10)
    symmetric_values = []
    for time1, time2 in ((.3, .7), (.7, 1.3), (.3, 1.3)):
        total, mean = time1+time2, math.exp(-.75*(time1+time2))
        moments = []
        for time in (time1, time2):
            refined = []
            for order in (48, 96):
                nodes, weights = heat_quadrature(time, order)
                vectors = np.sqrt(1-nodes*nodes)[:, None, None]*directions[None, :, :]
                refined.append(np.einsum("n,nka,nkb->ab", weights/6, vectors, vectors))
            close(refined[0], refined[1])
            moments.append(refined[-1])
        # E|v1 x v2|^2 from independently integrated orientation tensors;
        # this contraction uses independence, not a substituted radial law.
        cross_mean = np.trace(moments[0])*np.trace(moments[1])-np.trace(moments[0]@moments[1])
        close(cross_mean, 3*(1-math.exp(-2*time1))*(1-math.exp(-2*time2))/8)
        for theta1, theta2 in ((.2, .8), (.5, .5), (.87, .61)):
            times = np.array([time1*theta1, time1*(1-theta1),
                              time2*theta2, time2*(1-theta2)])
            inverse0 = np.diag(np.repeat(2*times, 3))
            fisher0, hessian = np.linalg.inv(inverse0), mean*unit_hessian
            inverse_derivative = -inverse0@hessian@inverse0
            delta = 1e-4
            finite_derivative = (np.linalg.inv(fisher0+delta*hessian)
                                 -np.linalg.inv(fisher0-delta*hessian))/(2*delta)
            close(finite_derivative, inverse_derivative, rtol=3e-8, atol=3e-11)
            covector = actual_rows.ravel()
            fine_derivative = float(covector@inverse_derivative@covector)
            coarse_split = .37
            coarse_inverse = np.diag(np.repeat([2*total*coarse_split,
                                                2*total*(1-coarse_split)], 3))
            coarse_hessian = mean*np.kron(np.array([[1., -1.], [-1., 1.]])/4, np.eye(3))
            coarse_covector = np.r_[w, -w]
            coarse_derivative = float(-coarse_covector@coarse_inverse@coarse_hessian
                                      @coarse_inverse@coarse_covector)
            a, b = times[0]+times[3], times[1]+times[2]
            close(fine_derivative, -mean*np.linalg.norm(a*w+b*z)**2, rtol=3e-10)
            close(coarse_derivative, -mean*total*total*(w@w))
            close(fine_derivative-coarse_derivative, mean*a*b*np.linalg.norm(w-z)**2, rtol=5e-10)
            integrated = mean*a*b*cross_mean
            assert integrated > 0
            if theta1 == theta2 == .5:
                symmetric_values.append(integrated)
    print("PASS two-edge subdivision: actual noncommuting Pauli product gradients, "
          "full 12x12 endpoint Hessian and nine fine/coarse inverse derivatives; "
          "independent 48/96-node heat/orientation moments give positive integrated "
          "obstruction even at theta1=theta2=1/2: "
          + ", ".join(f"{value:.12g}" for value in symmetric_values)
          + ". Finite first-order checks; the analytic source proof supplies the subdivision verdict.")


def ordered_source_transport_checks() -> None:
    """Actual source-cut intertwining and a distinct ordering obstruction.

    These finite matrix identities test the specified bijective path
    presentation and its transported action, not a path-law or domain
    theorem. Associativity of ordered cuts does not grant invariance
    under changing the order assigned to otherwise unordered loops.
    """
    pauli = np.array(([[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]))
    generators, identity = -.5j*pauli, np.eye(2, dtype=complex)

    def close(actual, expected, *, rtol=2e-11, atol=2e-13):
        assert np.all(np.isfinite(actual)) and np.all(np.isfinite(expected))
        assert np.allclose(actual, expected, rtol=rtol, atol=atol), (actual, expected)

    def inverse(group):
        return group.conj().T

    def turn(vector):
        length = np.linalg.norm(vector)
        if length == 0:
            return identity.copy()
        return (math.cos(length/2)*identity
                + 2*math.sin(length/2)/length*np.einsum("a,aij->ij", vector, generators))

    def adjoint(group, value):
        return group@value@inverse(group)

    us = [turn(v) for v in ([.3, -.7, .4], [.8, .2, -.1], [-.2, .5, .9])]
    vs = [turn(v) for v in ([-.4, .2, .8], [.1, .9, -.3], [.7, -.6, .2])]
    u1, u2, v1, v2 = us[0], us[1], vs[0], vs[1]
    whole_u, whole_v = u1@u2, v1@v2
    tilde_u, tilde_v = adjoint(v1, u2), adjoint(v1, v2)
    y1, future = u1@inverse(v1), tilde_u@inverse(tilde_v)
    close(u1@inverse(v1)@tilde_u@v1, whole_u)
    close(tilde_v@v1, whole_v)
    close(y1@future, whole_u@inverse(whole_v))
    assert np.linalg.norm(y1@future-future@y1) > .01

    k1, l1, k_end, l_end = [turn(v) for v in
                            ([.2, .8, -.4], [.7, -.1, .5], [-.6, .2, .1], [.3, -.7, .6])]
    k_increment, l_increment = inverse(k1)@k_end, inverse(l1)@l_end
    moved_u1, moved_v1 = k1@u1, l1@v1
    moved_whole_u, moved_whole_v = k_end@whole_u, l_end@whole_v
    # Recut the actually transformed source, independently of the
    # explicit formula for the transported fine action.
    recut_u = adjoint(moved_v1, inverse(moved_u1)@moved_whole_u)
    recut_v = adjoint(moved_v1, inverse(moved_v1)@moved_whole_v)
    transported_u = l1@inverse(y1)@k_increment@y1@tilde_u@inverse(l1)
    transported_v = l1@l_increment@tilde_v@inverse(l1)
    close(recut_u, transported_u)
    close(recut_v, transported_v)
    moved_readout = (moved_u1@inverse(moved_v1))@transported_u@inverse(transported_v)
    close(moved_readout, k_end@(y1@future)@inverse(l_end))

    # Both binary parenthesizations of the three-cut presentation.
    raw_readouts = [u@inverse(v) for u, v in zip(us, vs)]
    cut_readouts, v_prefix = [], identity.copy()
    for u, v in zip(us, vs):
        cut_readouts.append(adjoint(v_prefix, u@inverse(v)))
        v_prefix = v_prefix@v
    direct = cut_readouts[0]@cut_readouts[1]@cut_readouts[2]
    left_grouped = (us[0]@us[1]@inverse(vs[0]@vs[1]))@adjoint(vs[0]@vs[1], raw_readouts[2])
    right_grouped = raw_readouts[0]@adjoint(vs[0], us[1]@us[2]@inverse(vs[1]@vs[2]))
    whole = us[0]@us[1]@us[2]@inverse(vs[0]@vs[1]@vs[2])
    for value in (left_grouped, right_grouped, whole):
        close(direct, value)
    for factor in (us[2], vs[2]):
        close(adjoint(vs[0]@vs[1], factor), adjoint(vs[0], adjoint(vs[1], factor)))

    # Differentiate the transported action, not an independently reset
    # future action. Coordinates are (prefix U, prefix V, future U, future V).
    def transported_q(controls):
        kp, lp, ki, li = [turn(row) for row in controls]
        first = kp@y1@inverse(lp)
        second_u = lp@inverse(y1)@ki@y1@tilde_u@inverse(lp)
        second_v = lp@li@tilde_v@inverse(lp)
        return np.trace(first@second_u@inverse(second_v)).real/2

    w = np.array([np.trace(t@y1@future).real/2 for t in generators])
    rows, step = np.zeros((4, 3)), 1e-5
    for row in range(4):
        for axis in range(3):
            control = np.zeros((4, 3))
            control[row, axis] = step
            rows[row, axis] = (transported_q(control)-transported_q(-control))/(2*step)
    close(rows, np.array([w, -w, w, -w]), rtol=2e-9, atol=3e-11)
    print("PASS ordered source cut: noncommuting Phi/inverse and readout identities, "
          "actual recut-versus-transported action, both three-cut parenthesizations, "
          "and all 12 endpoint q-control derivatives (w,-w,w,-w)")

    # Assign three independent loops two different traversal orders.
    # In order ABC, F=q(AC)=q(X1 X2^-1 X3); in order ACB it is q(X2).
    # Both are the same complete loop observable, not a renamed function.
    a, b, c = us
    abc, acb = (a, a@b, a@b@c), (a, a@c, a@c@b)

    def value(xs, ordering):
        return np.trace(xs[0]@inverse(xs[1])@xs[2] if ordering == "ABC" else xs[1]).real/2

    def differential(xs, changes, ordering):
        if ordering == "ACB":
            return np.trace(changes.get(1, np.zeros((2, 2)))).real/2
        x1, x2, x3 = xs
        dx1, dx2, dx3 = [changes.get(i, np.zeros((2, 2))) for i in range(3)]
        x2i = inverse(x2)
        return np.trace(dx1@x2i@x3-x1@x2i@dx2@x2i@x3+x1@x2i@dx3).real/2

    close(value(abc, "ABC"), value(acb, "ACB"))
    gradients = {}
    for ordering, xs in (("ABC", abc), ("ACB", acb)):
        for handedness in ("L", "R"):
            gradient = np.array([[differential(xs, {i: t@x if handedness == "L" else x@t}, ordering)
                                  for t in generators] for i, x in enumerate(xs)])
            for i in range(3):
                for axis in range(3):
                    epsilon = np.eye(3)[axis]*step
                    plus, minus = list(xs), list(xs)
                    if handedness == "L":
                        plus[i], minus[i] = turn(epsilon)@xs[i], turn(-epsilon)@xs[i]
                    else:
                        plus[i], minus[i] = xs[i]@turn(epsilon), xs[i]@turn(-epsilon)
                    close((value(plus, ordering)-value(minus, ordering))/(2*step),
                          gradient[i, axis], rtol=2e-8, atol=4e-11)
            gradients[ordering, handedness] = gradient
    va = np.array([-np.trace(t@a).real for t in generators])
    vc = np.array([-np.trace(t@c).real for t in generators])
    cross_squared = np.linalg.norm(np.cross(va, vc))**2
    assert cross_squared > .001

    tensor_generators = [np.kron(t, identity)+np.kron(identity, t) for t in generators]
    tensor_casimir = sum(t@t for t in tensor_generators)
    eigenvalues, eigenvectors = np.linalg.eigh(tensor_casimir)
    close(eigenvalues, [-2, -2, -2, 0])

    def heat_vector_moment(time):
        mean_tensor = (eigenvectors*np.exp(time*eigenvalues))@eigenvectors.conj().T
        moment = np.array([[np.trace(np.kron(ta, tb)@mean_tensor).real
                            for tb in generators] for ta in generators])
        close(moment, (1-math.exp(-2*time))*np.eye(3)/4)
        return moment

    integrated_values = []
    for ta, tb, tc in ((.3, .7, 1.1), (.7, .2, .4), (.1, .5, .3)):
        responses = {}
        for ordering, intervals in (("ABC", [ta, tb, tc]), ("ACB", [ta, tc, tb])):
            for handedness in ("L", "R"):
                gradient = gradients[ordering, handedness]
                cumulative = np.cumsum(gradient[::-1], axis=0)[::-1]
                responses[ordering, handedness] = 2*np.dot(intervals, np.sum(cumulative*cumulative, axis=1))
        close(responses["ABC", "L"], responses["ACB", "L"])
        close(responses["ABC", "R"]-responses["ACB", "R"], 2*tb*cross_squared)
        ma, mc = heat_vector_moment(ta), heat_vector_moment(tc)
        cross_moment = np.trace(ma)*np.trace(mc)-np.trace(ma@mc)
        for beta in (.2, .5, .8):
            difference = ((1-beta)*(responses["ABC", "L"]-responses["ACB", "L"])
                          + beta*(responses["ABC", "R"]-responses["ACB", "R"]))
            close(difference, 2*beta*tb*cross_squared)
            integrated = 2*beta*tb*cross_moment
            close(integrated, 3*beta*tb*(1-math.exp(-2*ta))*(1-math.exp(-2*tc))/4)
            assert integrated > 0
            if beta == .5:
                integrated_values.append(integrated)
    print("PASS order ABC versus ACB for the same q(AC): actual cumulative-holonomy "
          "gradient channels give 2*beta*tB*|vA cross vC|^2; independent Pauli tensor "
          "heat moments give positive integrated differences at beta=1/2: "
          + ", ".join(f"{x:.12g}" for x in integrated_values)
          + ". Ordered-cut coherence therefore does not establish order-independent graph response.")

    # A chain of three bigons realizes the ordered rows as the reduction
    # of a specified raw edge metric. Its V-tree frame is retained.
    def tree_loops(raw_u, raw_v):
        loops, frames, prefix = [], [], identity.copy()
        for u, v in zip(raw_u, raw_v):
            frames.append(prefix)
            loops.append(adjoint(prefix, u@inverse(v)))
            prefix = prefix@v
        return loops, frames

    def probes(loops):
        za, zb, zc = loops
        return np.array([np.trace(za@zc).real/2, np.trace(za@zb@zc).real/2,
                         np.trace(za@zb@zc-za@zc@zb).real/2])

    loops, frames = tree_loops(us, vs)
    left, right, raw_u_rows, raw_v_rows = (np.zeros((3, 3, 3)) for _ in range(4))
    for edge in range(3):
        for axis in range(3):
            forward, backward = turn(step*np.eye(3)[axis]), turn(-step*np.eye(3)[axis])
            for handedness, target in (("L", left), ("R", right)):
                plus, minus = list(loops), list(loops)
                if handedness == "L":
                    plus[edge], minus[edge] = forward@loops[edge], backward@loops[edge]
                else:
                    plus[edge], minus[edge] = loops[edge]@forward, loops[edge]@backward
                target[:, edge, axis] = (probes(plus)-probes(minus))/(2*step)
            for raw, other, target, channel in ((us, vs, raw_u_rows, "U"),
                                               (vs, us, raw_v_rows, "V")):
                plus, minus = list(raw), list(raw)
                plus[edge], minus[edge] = forward@raw[edge], backward@raw[edge]
                plus_loops = tree_loops(plus, other)[0] if channel == "U" else tree_loops(other, plus)[0]
                minus_loops = tree_loops(minus, other)[0] if channel == "U" else tree_loops(other, minus)[0]
                target[:, edge, axis] = (probes(plus_loops)-probes(minus_loops))/(2*step)
    ordered_right = right.copy()
    for edge in range(3):
        ordered_right[:, edge] += np.sum(right[:, edge+1:]-left[:, edge+1:], axis=1)
        frame = np.array([[-2*np.trace(ta@frames[edge]@tb@inverse(frames[edge])).real
                           for tb in generators] for ta in generators])
        close(raw_u_rows[:, edge], left[:, edge]@frame, rtol=2e-8, atol=5e-11)
        close(raw_v_rows[:, edge], -ordered_right[:, edge]@frame, rtol=2e-8, atol=5e-11)
    close(np.sum(left-right, axis=1), np.zeros((3, 3)), rtol=2e-8, atol=5e-11)
    for durations in ([.3, .7, 1.1], [.7, .2, .4], [.1, .5, .3]):
        for alpha in (.2, .5, .8):
            raw_response = 2*(alpha*np.einsum("e,pea,qea->pq", durations, raw_u_rows, raw_u_rows)
                              +(1-alpha)*np.einsum("e,pea,qea->pq", durations, raw_v_rows, raw_v_rows))
            reduced = 2*(alpha*np.einsum("e,pea,qea->pq", durations, left, left)
                         +(1-alpha)*np.einsum("e,pea,qea->pq", durations, ordered_right, ordered_right))
            close(raw_response, reduced, rtol=3e-8, atol=2e-10)
    gauges = [turn(v) for v in ([.2, .4, -.1], [-.7, .2, .5], [.6, -.3, .2], [-.1, .8, .3])]
    gauged_u = [gauges[j]@u@inverse(gauges[j+1]) for j, u in enumerate(us)]
    gauged_v = [gauges[j]@v@inverse(gauges[j+1]) for j, v in enumerate(vs)]
    gauged_loops, _ = tree_loops(gauged_u, gauged_v)
    for original, gauged in zip(loops, gauged_loops):
        close(gauged, adjoint(gauges[0], original))
    close(probes(gauged_loops), probes(loops))
    print("PASS three-bigon parent: all raw U/V Pauli derivatives for q(AC), q(ABC), "
          "and the alternating trace difference reproduce the boundary-corrected ordered rows; "
          "nine full 3x3 response comparisons and independent vertex-frame invariance pass. "
          "Changing loop placements along this metrized chain is not an equivalent graph "
          "reparametrization. No interacting source/action law at nonzero coupling established.")

    # Actual independent raw-edge actions need not reproduce the source
    # action transported from a single coarse loop after an interaction.
    raw_edges = [us[0], us[1], vs[0], vs[1]]  # U1,U2,V1,V2
    signs = np.array([1., 1., -1., -1.])
    outer = raw_edges[0]@raw_edges[1]@inverse(raw_edges[3])@inverse(raw_edges[2])
    w = np.array([np.trace(t@outer).real/2 for t in generators])

    def outer_q(control):
        moved = [turn(row)@edge for row, edge in zip(control.reshape(4, 3), raw_edges)]
        return np.trace(moved[0]@moved[1]@inverse(moved[3])@inverse(moved[2])).real/2

    p = np.zeros((4, 3))
    for edge in range(4):
        for axis in range(3):
            control = np.zeros((4, 3))
            control[edge, axis] = step
            p[edge, axis] = (outer_q(control)-outer_q(-control))/(2*step)
    r = signs[:, None]*p
    close(r[0], w, rtol=2e-9, atol=3e-11)
    close(np.sum(r*r, axis=1), np.full(4, w@w), rtol=3e-9, atol=3e-11)
    fundamental_casimir = sum(t@t for t in generators)
    eig, vec = np.linalg.eigh(fundamental_casimir)
    close(fundamental_casimir, -.75*identity)
    unit_hessian = np.kron(np.outer(signs, signs)/4, np.eye(3))
    pointwise_defects = []
    for alpha in (.2, .5, .8):
        t1, t2 = .3, .7
        lengths = np.array([alpha*t1, alpha*t2, (1-alpha)*t1, (1-alpha)*t2])
        total, mean = t1+t2, math.exp(-.75*(t1+t2))
        heat_means = [(vec*np.exp(length*eig))@vec.conj().T for length in lengths]

        def averaged_potential(control):
            k1, k2, l1, l2 = [turn(row) for row in control.reshape(4, 3)]
            word = k1@heat_means[0]@k2@heat_means[1]@heat_means[3]@inverse(l2)@heat_means[2]@inverse(l1)
            return mean-np.trace(word).real/2

        basis, delta = np.eye(12), .001
        measured = np.zeros((12, 12))
        for i in range(12):
            for j in range(12):
                measured[i, j] = sum(si*sj*averaged_potential(delta*(si*basis[i]+sj*basis[j]))
                                     for si in (-1., 1.) for sj in (-1., 1.))/(4*delta*delta)
        hessian = mean*unit_hessian
        close(measured, hessian, rtol=5e-7, atol=4e-10)
        d0 = np.diag(np.repeat(2*lengths, 3))
        fisher0, delta = np.linalg.inv(d0), 1e-4
        inverse_derivative = -d0@hessian@d0
        finite = (np.linalg.inv(fisher0+delta*hessian)-np.linalg.inv(fisher0-delta*hessian))/(2*delta)
        close(finite, inverse_derivative, rtol=3e-8, atol=3e-11)
        fine = float(p.ravel()@inverse_derivative@p.ravel())
        coarse = -mean*total*total*(w@w)
        defect = mean*sum(lengths[i]*lengths[j]*np.linalg.norm(r[i]-r[j])**2
                          for i in range(4) for j in range(i+1, 4))
        close(fine, -mean*np.linalg.norm(lengths@r)**2)
        close(fine-coarse, defect, rtol=3e-8, atol=3e-11)
        assert defect > 0
        pointwise_defects.append(defect)
    print("PASS two-bigon outer-loop tilt: actual raw-edge q gradients, Pauli-derived "
          "averaged heat-word Hessian and full 12x12 inverse derivatives give positive "
          "fine-minus-coarse first-order response defects at alpha=.2,.5,.8: "
          + ", ".join(f"{x:.12g}" for x in pointwise_defects)
          + ". This tests the independent raw-edge source action, not the transported "
          "coarse action; no interacting equality follows from the unweighted graph realization.")


def random_frame_quadratic_variation_checks() -> None:
    """Finite Pauli Jacobians test obstructions detected by path variation.

    No Brownian simulation or Fisher matrix for the singular family is
    attempted. The analytic path argument, not these finite samples,
    proves mutual singularity when covariance differs on a time interval.
    """
    pauli = np.array(([[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]]))
    generators, identity = -.5j*pauli, np.eye(2, dtype=complex)

    def close(actual, expected, *, rtol=3e-8, atol=5e-10):
        assert np.all(np.isfinite(actual)) and np.all(np.isfinite(expected))
        assert np.allclose(actual, expected, rtol=rtol, atol=atol), (actual, expected)

    def inverse(g):
        return g.conj().T

    def turn(v):
        length = np.linalg.norm(v)
        return (math.cos(length/2)*identity
                + 2*math.sin(length/2)/length*np.einsum("a,aij->ij", v, generators))

    def adjoint(g):
        return np.array([[-2*np.trace(ta@g@tb@inverse(g)).real for tb in generators]
                         for ta in generators])

    def noise_jacobian(readout, inputs, handedness="R"):
        outputs, step = readout(inputs), 1e-5
        result = np.zeros((3*len(outputs), 3*len(inputs)))
        for edge, group in enumerate(inputs):
            for axis in range(3):
                forward, backward = turn(step*np.eye(3)[axis]), turn(-step*np.eye(3)[axis])
                plus, minus = list(inputs), list(inputs)
                if handedness == "R":
                    plus[edge], minus[edge] = forward@group, backward@group
                else:
                    plus[edge], minus[edge] = group@forward, group@backward
                changes = [(p-m)/(2*step) for p, m in zip(readout(plus), readout(minus))]
                for slot, (output, change) in enumerate(zip(outputs, changes)):
                    log_change = change@inverse(output) if handedness == "R" else inverse(output)@change
                    result[3*slot:3*slot+3, 3*edge+axis] = [
                        -2*np.trace(t@log_change).real for t in generators]
        return result

    a, b, c, k = [turn(np.array(v)) for v in
                  ([.3, -.7, .4], [.8, .2, -.1], [.7, -.6, .2], [-.2, .5, .9])]
    ca, cb, cc = .3, .7, 1.1
    q = inverse(a)@k@a

    def random_frame(inputs):
        first, second = inputs
        return first, second@inverse(first)@k@first

    close(random_frame([a, b])[1]@inverse(a), b@inverse(a)@k)
    m = adjoint(b@inverse(a))@(adjoint(k)-np.eye(3))
    n, rotation = np.eye(3)-adjoint(q).T, adjoint(q).T
    base = 2*np.diag([ca]*3+[cb]*3)
    for handedness, expected in (
            ("R", np.block([[np.eye(3), np.zeros((3, 3))], [m, np.eye(3)]])),
            ("L", np.block([[np.eye(3), np.zeros((3, 3))], [n, rotation]]))):
        jacobian = noise_jacobian(random_frame, [a, b], handedness)
        close(jacobian, expected)
        covariance = jacobian@base@jacobian.T
        close(covariance, expected@base@expected.T)
        assert np.linalg.norm(covariance[:3, 3:]) > .1
        close(np.trace(covariance[3:, 3:])-6*cb, 2*ca*np.linalg.norm(adjoint(k)-np.eye(3))**2)
    print("PASS random-frame lift b'=b*a^-1*k*a: actual Pauli noise Jacobians in "
          "both logarithmic frames acquire nonzero cross covariance and the predicted "
          "extra quadratic variation, although x'=x*k at the output")

    p, left_y, right_x, incompatible = [turn(np.array(v)) for v in
                                       ([.2, .8, -.4], [.7, -.1, .5], [-.6, .2, .1], [.3, -.7, .6])]
    x, y = b@inverse(a), c@inverse(a)
    source_covariance = 2*np.diag([ca]*3+[cb]*3+[cc]*3)
    extra_values = []
    for right_y in (right_x, -right_x, incompatible):
        def transformed(inputs):
            first, second, third = inputs
            xp = p@second@inverse(first)@inverse(right_x)
            yp = left_y@third@inverse(first)@inverse(right_y)
            return xp, yp, xp@inverse(yp)

        xp, yp, _ = transformed([a, b, c])
        jacobian = noise_jacobian(transformed, [a, b, c])
        covariance = jacobian@source_covariance@jacobian.T
        actual_cross = 2*ca*adjoint(p@x@inverse(y)@inverse(left_y))
        model_cross = 2*ca*adjoint(xp@inverse(yp))
        close(covariance[:3, 3:6], actual_cross)
        mismatch = np.eye(3)-adjoint(inverse(right_x)@right_y)
        extra = 2*ca*np.linalg.norm(mismatch)**2
        close(np.trace(covariance[6:, 6:])-6*(cb+cc), extra)
        if extra < 1e-12:
            close(actual_cross, model_cross)
        else:
            assert np.linalg.norm(actual_cross-model_cross) > .1
        extra_values.append(extra)
    assert extra_values[-1] > .1
    print("PASS theta output covariance: shared and pointwise-central right frames "
          "match the native covariance; an incompatible frame fails and adds relative-loop "
          f"quadratic-variation trace {extra_values[-1]:.12g}. Based smooth SU(2) "
          "paths cannot differ by a nontrivial continuous central path from the identity.")

    terminal, speed = .7, 1.2
    expected = 8*ca*(terminal-math.sin(speed*terminal)/speed)
    integrals = []
    for order in (16, 32, 64):
        nodes, weights = np.polynomial.legendre.leggauss(order)
        times = terminal*(nodes+1)/2
        values = [2*ca*np.linalg.norm(np.eye(3)-adjoint(turn(np.array([0., 0., speed*s]))))**2
                  for s in times]
        integrals.append(terminal*np.dot(weights, values)/2)
    close(integrals, np.full(3, expected), rtol=3e-13, atol=3e-14)
    print(f"PASS 16/32/64-point actual-adjoint integral for k_s=exp(omega*s*T3): "
          f"extra quadratic variation={expected:.12g}. Finite witnesses only; the "
          "pathwise covariance obstruction forbids using this bad lift as a finite-Fisher source family.")


def main() -> None:
    print("two-sided Fisher receipt: finite construction discrimination")
    joint_fisher_block_checks()
    class_trial_checks()
    logarithmic_ramp_checks()
    raw_coordinate_and_invariant_checks()
    print("Finite matrix, gradient, integral and trial checks only. "
          "No continuum domain theorem, spectral-edge/eigenvalue theorem, "
          "four-dimensional construction or physical mass gap certified.")
    prior_annular_responses = annular_restart_checks()
    heat_factor_fisher_checks()
    heat_factor_finite_kl_checks()
    lifted_annular_checks(prior_annular_responses)
    opposite_chaos_overlap_checks()
    heat_factor_fiber_chaos_checks()
    charged_cut_twist_checks()
    conditional_boundary_frame_checks()
    gauge_vertex_source_checks()
    tilted_self_loop_fisher_checks()
    ordered_source_transport_checks()
    random_frame_quadratic_variation_checks()


if __name__ == "__main__":
    main()
