"""Finite tests for the specified two-sided path-shift Fisher construction.

These tests discriminate the joint response from either one-hand response,
check finite logarithmic-ramp entropy controls, and sample small-time
invariant trial quotients. They do not prove a continuum domain theorem,
an infinite-dimensional eigenvalue statement, or a physical mass gap.
The heat-factor additions test finite score projections, KL costs,
annular responses, and an opposite-chaos kernel overlap.
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


if __name__ == "__main__":
    main()
