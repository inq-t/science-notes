"""Full invariant two-plaquette vacuum and conditional local memory.

The supplied physical operator is H0+lambda(2-a-b), kappa=1,
H0=4(Dx+Dy)-2 sum R_x R_y, on L2(SU2^2)^Ad. Coordinates are
a=x0,b=y0,z=vec(x).vec(y), and u=z/sqrt((1-a^2)(1-b^2)).
The basis retains every simultaneous-invariant angular channel k, not
only products of separate characters. Finite cutoffs approximate the
actual vacuum; floating-point residuals and quadrature convergence are
diagnostics, not a proof of an infinite-volume or Yang--Mills mass gap.
"""

from __future__ import annotations

import math

import numpy as np


def close(actual, expected, *, rtol=3e-10, atol=3e-12):
    assert np.all(np.isfinite(actual)) and np.all(np.isfinite(expected))
    assert np.allclose(actual, expected, rtol=rtol, atol=atol), (actual, expected)


def labels(cutoff):
    return [(n, m, k) for n in range(cutoff+1) for m in range(cutoff+1)
            for k in range(min(n, m)+1)]


def raising(n, k):
    return .5*math.sqrt((n-k+1)*(n+k+2)/((n+1)*(n+2)))


def matrices(cutoff):
    basis = labels(cutoff)
    lookup = {label: index for index, label in enumerate(basis)}
    kinetic, multiplication = np.zeros((len(basis), len(basis))), np.zeros((len(basis), len(basis)))
    for index, (n, m, k) in enumerate(basis):
        kinetic[index, index] = n*(n+2)+m*(m+2)-k*(k+1)/2
        if k < min(n, m):
            ell = k+1
            coefficient = -.5*ell*math.sqrt((((n+1)**2-ell**2)*((m+1)**2-ell**2))
                                            /((2*ell-1)*(2*ell+1)))
            other = lookup[n, m, k+1]
            kinetic[index, other] = kinetic[other, index] = coefficient
        for other_label, coefficient in (((n+1, m, k), raising(n, k)),
                                          ((n, m+1, k), raising(m, k))):
            if other_label in lookup:
                other = lookup[other_label]
                multiplication[index, other] = multiplication[other, index] = coefficient
    # Independent total-right-spin spectrum, separately in every (n,m).
    for n in range(cutoff+1):
        for m in range(cutoff+1):
            indices = [lookup[n, m, k] for k in range(min(n, m)+1)]
            spins = np.arange(abs(n-m), n+m+1, 2)/2
            target = .75*(n*(n+2)+m*(m+2))+spins*(spins+1)
            close(np.linalg.eigvalsh(kinetic[np.ix_(indices, indices)]), target)
    return basis, lookup, kinetic, multiplication


def quadrature(order, angular):
    theta = np.arange(1, order+1)*math.pi/(order+1)
    q, w = np.cos(theta), 2*np.sin(theta)**2/(order+1)
    u, wu = np.polynomial.legendre.leggauss(angular)
    return q, w, u, wu/2


def radial_tables(cutoff, k, q):
    """Normalized (1-q^2)^(k/2) C_(n-k)^(k+1)(q) and derivative."""
    degree, parameter = cutoff-k, k+1
    values = [np.ones_like(q)]
    derivatives = [np.zeros_like(q)]
    if degree > 0:
        values.append(2*parameter*q)
        derivatives.append(np.full_like(q, 2*parameter))
    for p in range(1, degree):
        values.append((2*(p+parameter)*q*values[p]-(p+2*parameter-1)*values[p-1])/(p+1))
        derivatives.append((2*(p+parameter)*(values[p]+q*derivatives[p])
                            -(p+2*parameter-1)*derivatives[p-1])/(p+1))
    radius = np.sqrt(1-q*q)
    result, derivative = [], []
    for p, (value, slope) in enumerate(zip(values, derivatives)):
        norm = math.factorial(p+2*k+1)/(4**k*math.factorial(p)*(p+k+1)*math.factorial(k)**2)
        factor = radius**k/math.sqrt(norm)
        result.append(factor*value)
        derivative.append(factor*(slope-k*q*value/(1-q*q)))
    return np.array(result).T, np.array(derivative).T


def legendre_tables(cutoff, u):
    values, derivatives = [np.ones_like(u)], [np.zeros_like(u)]
    if cutoff:
        values.append(u.copy())
        derivatives.append(np.ones_like(u))
    for k in range(1, cutoff):
        values.append(((2*k+1)*u*values[k]-k*values[k-1])/(k+1))
        derivatives.append(((2*k+1)*(values[k]+u*derivatives[k])-k*derivatives[k-1])/(k+1))
    return values, derivatives


def evaluate(coefficients, cutoff, a, b, u):
    lookup = {label: index for index, label in enumerate(labels(cutoff))}
    p, dp = legendre_tables(cutoff, u)
    shape = (len(a), len(b), len(u))
    psi, da, db, du = (np.zeros(shape) for _ in range(4))
    for k in range(cutoff+1):
        ra, dra = radial_tables(cutoff, k, a)
        rb, drb = radial_tables(cutoff, k, b)
        block = np.array([[coefficients[lookup[n, m, k]] for m in range(k, cutoff+1)]
                          for n in range(k, cutoff+1)])
        scale = math.sqrt(2*k+1)
        value = scale*ra@block@rb.T
        psi += value[:, :, None]*p[k]
        da += (scale*dra@block@rb.T)[:, :, None]*p[k]
        db += (scale*ra@block@drb.T)[:, :, None]*p[k]
        du += value[:, :, None]*dp[k]
    return psi, da, db, du


def coordinate_metric(a, b, z):
    g = np.zeros((*np.broadcast_shapes(a.shape, b.shape, z.shape), 3, 3))
    g[..., 0, 0], g[..., 1, 1] = 1-a*a, 1-b*b
    g[..., 0, 1] = g[..., 1, 0] = z/4
    g[..., 0, 2] = g[..., 2, 0] = -a*z-b*(1-a*a)/4
    g[..., 1, 2] = g[..., 2, 1] = -b*z-a*(1-b*b)/4
    g[..., 2, 2] = 1.5-(a*a+b*b+a*a*b*b)/2-1.5*z*z+a*b*z/2
    return g


def basis_and_operator_checks():
    cutoff, order, angular = 3, 12, 12
    basis, _, kinetic, multiplication = matrices(cutoff)
    q, w, u, wu = quadrature(order, angular)
    a, b, angle = np.meshgrid(q, q, u, indexing="ij")
    rx, ry = np.sqrt(1-a*a), np.sqrt(1-b*b)
    z = rx*ry*angle
    weight = (w[:, None, None]*w[None, :, None]*wu).ravel()
    values, gradients = [], []
    for index in range(len(basis)):
        coefficient = np.eye(len(basis))[index]
        value, da, db, du = evaluate(coefficient, cutoff, q, q, u)
        values.append(value.ravel())
        gradients.append(np.stack((da+a*angle*du/(1-a*a), db+b*angle*du/(1-b*b),
                                   du/(rx*ry)), axis=-1).reshape(-1, 3))
    values, gradients = np.array(values), np.array(gradients)
    close((values*weight)@values.T, np.eye(len(basis)))
    metric = coordinate_metric(a, b, z).reshape(-1, 3, 3)
    integrated = np.einsum("pni,nij,qnj,n->pq", gradients, metric, gradients, weight, optimize=True)
    close(integrated, kinetic, atol=2e-11)
    close((values*(weight*(a+b).ravel()))@values.T, multiplication)
    # Explicit low channels, including the relational degree of freedom.
    normalized_z = basis.index((1, 1, 1))
    product_character = basis.index((1, 1, 0))
    close(kinetic[np.ix_([product_character, normalized_z], [product_character, normalized_z])],
          [[6, -math.sqrt(3)/2], [-math.sqrt(3)/2, 5]])
    print("PASS complete orthonormal invariant basis: 30-mode positive-Haar Gram, "
          "coordinate-cometric kinetic integrals, multiplication and relative-loop channel; "
          "all later free blocks are also checked against total-right-spin spectra")


def ground_state(cutoff, coupling):
    basis, lookup, kinetic, multiplication = matrices(cutoff)
    hamiltonian = kinetic+coupling*(2*np.eye(len(basis))-multiplication)
    energies, vectors = np.linalg.eigh(hamiltonian)
    coefficients, energy = vectors[:, 0], energies[0]
    if coefficients[0] < 0:
        coefficients = -coefficients
    close(coefficients@coefficients, 1)
    inside = hamiltonian@coefficients-energy*coefficients
    outside_squared = 0.
    for index, (n, m, k) in enumerate(basis):
        if n == cutoff:
            outside_squared += (coupling*raising(n, k)*coefficients[index])**2
        if m == cutoff:
            outside_squared += (coupling*raising(m, k)*coefficients[index])**2
        close(coefficients[index], coefficients[lookup[m, n, k]], atol=3e-12)
    residual = math.sqrt(float(inside@inside)+outside_squared)
    assert 0 < energy < 2*coupling
    return coefficients, energy, residual, coefficients[lookup[1, 1, 1]]*4/math.sqrt(3)


def memory(coefficients, cutoff, order, angular):
    a, wa, u, wu = quadrature(order, angular)
    b, wb = a, wa
    psi, da, db, du = evaluate(coefficients, cutoff, a, b, u)
    assert np.min(psi) > 0
    aa, bb, uu = a[:, None, None], b[None, :, None], u[None, None, :]
    rx, ry = np.sqrt(1-aa*aa), np.sqrt(1-bb*bb)
    # The derivatives above hold u fixed. Converting the exact abc
    # cometric gives this expression without a spurious fixed-z derivative.
    contraction = (1-aa*aa)*da+rx*ry*uu*db/4-bb*rx*(1-uu*uu)*du/(4*ry)
    generator_character = -6*aa+4*contraction/psi
    density = psi*psi
    conditional_weights = wb[None, :, None]*wu[None, None, :]
    marginal = np.sum(density*conditional_weights, axis=(1, 2))
    close(wa@marginal, 1)
    conditional_mean = np.sum(density*generator_character*conditional_weights, axis=(1, 2))/marginal
    marginal_derivative = np.sum(2*psi*da*conditional_weights, axis=(1, 2))
    close(conditional_mean, -6*a+2*(1-a*a)*marginal_derivative/marginal, atol=4e-10)
    centered = generator_character-conditional_mean[:, None, None]
    result = float(np.sum(wa[:, None, None]*conditional_weights*density*centered*centered))
    mean_character = float(wa@(2*a*marginal))
    return np.array([result, mean_character, float(psi.min())])


def fixed_time_defect(cutoff, coupling, times, order, angular):
    """Q exp(t L) chi via the supplied source Hamiltonian, not a reset clock.

    Finite Galerkin evolution also truncates multiplication by chi. Its
    omitted coefficient norm is checked explicitly below; comparing two
    cutoffs is a diagnostic, not a certified semigroup error estimate.
    """
    basis, lookup, kinetic, multiplication = matrices(cutoff)
    hamiltonian = kinetic+coupling*(2*np.eye(len(basis))-multiplication)
    energies, vectors = np.linalg.eigh(hamiltonian)
    coefficients = vectors[:, 0].copy()
    if coefficients[0] < 0:
        coefficients *= -1
    character = np.zeros_like(hamiltonian)
    omitted_squared = 0.
    for index, (n, m, k) in enumerate(basis):
        if n < cutoff:
            other = lookup[n+1, m, k]
            character[index, other] = character[other, index] = 2*raising(n, k)
        else:
            omitted_squared += (2*raising(n, k)*coefficients[index])**2
    assert math.sqrt(omitted_squared) < 2e-11
    raw_initial = character@coefficients
    spectral_initial = vectors.T@raw_initial
    q, weights, angle, angular_weights = quadrature(order, angular)
    psi = evaluate(coefficients, cutoff, q, q, angle)[0]
    conditional_weights = weights[None, :, None]*angular_weights[None, None, :]
    total_weights = weights[:, None, None]*conditional_weights
    marginal = np.sum(psi*psi*conditional_weights, axis=(1, 2))
    close(weights@marginal, 1)
    assert np.min(psi) > 0
    projected_initial = evaluate(raw_initial, cutoff, q, q, angle)[0]
    insertion_error = np.sum(total_weights*(projected_initial-2*q[:, None, None]*psi)**2)
    close(insertion_error, omitted_squared, rtol=1e-5, atol=1e-27)
    defects = []
    for time in times:
        evolved = vectors@(np.exp(-time*(energies-energies[0]))*spectral_initial)
        raw_evolved = evaluate(evolved, cutoff, q, q, angle)[0]
        conditional_mean = np.sum(psi*raw_evolved*conditional_weights, axis=(1, 2))/marginal
        hidden = raw_evolved-psi*conditional_mean[:, None, None]
        # This is the norm of the full conditional residual, with no
        # division by psi in the integrand and no finite readout basis.
        defects.append(float(np.sum(total_weights*hidden*hidden)))
    return np.array(defects), math.sqrt(omitted_squared)


def fixed_time_checks():
    times = np.array([.1, .4, 1.])
    predicted = ((np.exp(-3*times)-np.exp(-4.5*times))**2/144
                 +(np.exp(-3*times)-np.exp(-6.5*times))**2/2352)
    zero, _ = fixed_time_defect(6, 0., times, 20, 16)
    assert np.max(zero) < 1e-25
    ratios = []
    for coupling in (.02, .01):
        first, _ = fixed_time_defect(6, coupling, times, 24, 20)
        second, omitted = fixed_time_defect(8, coupling, times, 24, 20)
        refined, _ = fixed_time_defect(8, coupling, times, 36, 32)
        close(first, second, rtol=3e-7, atol=1e-17)
        close(second, refined, rtol=3e-7, atol=1e-17)
        ratios.append(refined/(coupling*coupling))
        print(f"fixed-time lambda={coupling:g}: omitted insertion norm={omitted:.3e}")
        for time, defect, ratio, target in zip(times, refined, ratios[-1], predicted):
            print(f"  t={time:g}: d={defect:.12g}, d/lambda^2={ratio:.12g}, "
                  f"leading coefficient={target:.12g}")
    assert np.all(np.abs(ratios[1]-predicted) < np.abs(ratios[0]-predicted))
    close(ratios[1], predicted, rtol=3e-4, atol=0.)
    print("PASS fixed-time source-semigroup conditional defect: full 140/285-mode "
          "spectral evolution, independent positive quadratures and zero-coupling control; "
          "lambda=.01 approaches the fixed-time perturbative coefficient more closely "
          "than lambda=.02. No projected-clock semigroup was substituted.")


def all_readout_diagnostic(cutoff, coupling, order, angular):
    coefficients = ground_state(cutoff, coupling)[0]
    a, wa, angle, wu = quadrature(order, angular)
    psi, da, db, du = evaluate(coefficients, cutoff, a, a, angle)
    assert np.min(psi) > 0
    aa, bb, uu = a[:, None, None], a[None, :, None], angle[None, None, :]
    rx, ry = np.sqrt(1-aa*aa), np.sqrt(1-bb*bb)
    density = psi*psi
    conditional_weights = wa[None, :, None]*wu[None, None, :]
    marginal = np.sum(density*conditional_weights, axis=(1, 2))

    def conditional(value):
        return np.sum(density*value*conditional_weights, axis=(1, 2))/marginal

    contraction = (1-aa*aa)*da+rx*ry*uu*db/4-bb*rx*(1-uu*uu)*du/(4*ry)
    score = contraction/psi
    drift = -6*aa+4*score
    centered_drift = drift-conditional(drift)[:, None, None]
    hidden_density = marginal*conditional(centered_drift**2)/4
    # C_n^1 for n=1,...,8 span an eight-dimensional space modulo constants.
    # Centering them in the actual vacuum does not change either derivative
    # Gram. Bf=f'(a) Q(L chi)/2, and the retained physical form has density
    # (1-a^2) m(a) relative to one-link Haar.
    slopes = radial_tables(8, 0, a)[1][:, 1:]
    retained = slopes.T@((wa*(1-a*a)*marginal)[:, None]*slopes)
    hidden = slopes.T@((wa*hidden_density)[:, None]*slopes)
    eigenvalues, eigenvectors = np.linalg.eigh(retained)
    assert eigenvalues[0] > 0
    whitening = eigenvectors/np.sqrt(eigenvalues)
    relative = whitening.T@hidden@whitening
    spectrum = np.linalg.eigvalsh((relative+relative.T)/2)
    assert spectrum[0] >= -1e-13 and spectrum[-1] <= 25*coupling*coupling
    sampled_score_ratio = float(np.max(np.abs(score)/(2.5*coupling*rx)))
    assert sampled_score_ratio <= 1

    # Relational F=ab+z, z=rx*ry*u. Differentiate the actual conditional
    # integral at fixed u, then independently use the FULL cometric
    # horizontal field X=Gamma(a,.)/(1-a^2), not the coordinate field d/da.
    z = rx*ry*uu
    function = aa*bb+z
    fixed_u_derivative = bb-aa*ry*uu/rx
    projected = conditional(function)
    marginal_slope = np.sum(2*psi*da*conditional_weights, axis=(1, 2))/marginal
    quotient_derivative = (conditional(fixed_u_derivative+2*function*da/psi)
                           -projected*marginal_slope)
    metric = coordinate_metric(aa, bb, z)
    horizontal_function = (metric[..., 0, 0]*bb+metric[..., 0, 1]*aa
                           +metric[..., 0, 2])/(1-aa*aa)
    horizontal_log_density = 2*score/(1-aa*aa)
    close(conditional(horizontal_log_density), marginal_slope, atol=4e-10)
    covariance = conditional((function-projected[:, None, None])
                             *(horizontal_log_density-marginal_slope[:, None, None]))
    coarea_derivative = conditional(horizontal_function)+covariance
    close(coarea_derivative, quotient_derivative, atol=4e-10)
    coarea_error = float(np.max(np.abs(coarea_derivative-quotient_derivative)))
    return retained, hidden, float(spectrum[-1]), sampled_score_ratio, coarea_error


def all_readout_checks():
    for coupling in (.5, 1.):
        runs = [all_readout_diagnostic(cutoff, coupling, order, angular)
                for cutoff, order, angular in ((6, 24, 20), (8, 24, 20), (8, 36, 32))]
        reference_eigenvalues, reference_eigenvectors = np.linalg.eigh(runs[-1][0])
        reference_whitening = reference_eigenvectors/np.sqrt(reference_eigenvalues)
        for earlier in runs[:-1]:
            # Compare bilinear forms in the retained energy norm, rather
            # than demand relative accuracy in nearly zero matrix entries.
            for component in (0, 1):
                difference = reference_whitening.T@(earlier[component]-runs[-1][component])@reference_whitening
                assert np.linalg.norm(difference, 2) < 3e-9
            close(earlier[2], runs[-1][2], rtol=2e-8, atol=3e-12)
        _, _, largest, sampled_ratio, coarea_error = runs[-1]
        print(f"readout-form lambda={coupling:g}: eight-mode max B*B/a={largest:.12g} "
              f"<= {25*coupling*coupling:.12g}; sampled score/bound={sampled_ratio:.12g}; "
              f"relational coarea error={coarea_error:.3e}")
    print("PASS retained/hidden form Grams on eight class-polynomial directions "
          "modulo constants, with full interacting vacuum and independent cutoff/quadrature "
          "refinements. The pointwise score check is sampled only; the all-readout bound "
          "requires the analytic Bochner/domain argument, not this finite battery.")


def neutral_shape_profile(coefficients, cutoff, retained, order, angular):
    """Sample 4 Var(G/sqrt(1-a^2)|a), kappa=1, at fixed interior a.

    G is the unweighted raw gradient contraction, not an independently
    chosen score. This profile is not a certified supremum or error bound.
    """
    assert np.all(np.abs(retained) < 1)
    b, wb, angle, wu = quadrature(order, angular)
    psi, da, db, du = evaluate(coefficients, cutoff, retained, b, angle)
    assert np.min(psi) > 0
    aa, bb, uu = retained[:, None, None], b[None, :, None], angle[None, None, :]
    ra, rb = np.sqrt(1-aa*aa), np.sqrt(1-bb*bb)
    # ra*da = -d_theta psi at fixed (b,u), a=cos(theta). Compute the
    # normalized contraction BEFORE its conditional variance, rather
    # than dividing a vanishing variance by 1-a^2 near the endpoints.
    normalized_score = (ra*da+rb*uu*db/4-bb*(1-uu*uu)*du/(4*rb))/psi
    density_weights = psi*psi*wb[None, :, None]*wu[None, None, :]
    marginal = np.sum(density_weights, axis=(1, 2))
    mean = np.sum(density_weights*normalized_score, axis=(1, 2))/marginal
    centered = normalized_score-mean[:, None, None]
    profile = 4*np.sum(density_weights*centered*centered, axis=(1, 2))/marginal
    assert np.all(np.isfinite(profile)) and np.all(profile >= 0)

    # Independent coordinate-cometric contraction away from the radial
    # wall; the fixed-u derivatives must first be converted to fixed z.
    regular = np.abs(retained) < .95
    if np.any(regular):
        ar, rr = aa[regular], ra[regular]
        z = rr*rb*uu
        gradient = np.stack((da[regular]+ar*uu*du[regular]/(rr*rr),
                             db[regular]+bb*uu*du[regular]/(rb*rb),
                             du[regular]/(rr*rb)), axis=-1)
        metric = coordinate_metric(ar, bb, z)
        independent = np.sum(metric[..., 0, :]*gradient, axis=-1)/(rr*psi[regular])
        close(normalized_score[regular], independent, atol=3e-12)
    return profile


def neutral_shape_endpoints(coefficients, cutoff, order):
    """Analytic endpoint limits for the Galerkin state, integrated in b.

    Only k=0 contributes psi and psi_b at x=+/-I; only k=1
    contributes psi_z. No division by the retained radial coordinate
    or extrapolation from the interior supplies this calculation.
    """
    assert cutoff >= 1
    lookup = {label: index for index, label in enumerate(labels(cutoff))}
    b, wb, _, _ = quadrature(order, 2)
    rb = np.sqrt(1-b*b)
    values, slopes = radial_tables(cutoff, 0, b)
    relative = radial_tables(cutoff, 1, b)[0]/rb[:, None]
    scalar_block = np.array([[coefficients[lookup[n, m, 0]] for m in range(cutoff+1)]
                             for n in range(cutoff+1)])
    relative_block = np.array([[coefficients[lookup[n, m, 1]] for m in range(1, cutoff+1)]
                               for n in range(1, cutoff+1)])
    degrees, charged_degrees = np.arange(cutoff+1), np.arange(1, cutoff+1)
    endpoints = []
    for sign in (-1., 1.):
        character = sign**degrees*(degrees+1)
        # lim R_n,1(s)/sqrt(1-s^2) at s=+/-1, including normalization.
        relative_endpoint = (sign**(charged_degrees-1)*(charged_degrees+1)
                             *np.sqrt(charged_degrees*(charged_degrees+2))/3)
        psi = character@scalar_block@values.T
        slope_b = character@scalar_block@slopes.T
        slope_z = math.sqrt(3)*relative_endpoint@relative_block@relative.T
        assert np.min(psi) > 0
        # E[u^2]=1/3 at the endpoint. The mean of the limiting normalized
        # score vanishes by E[u]=0; its numerator is evaluated without logs.
        numerator = -sign*slope_z+slope_b/4
        endpoints.append(float((4/3)*(wb@((1-b*b)*numerator*numerator))/(wb@(psi*psi))))
    return np.array(endpoints)


def neutral_shape_checks():
    grid = np.linspace(-1., 1., 257)
    retained = grid[1:-1]
    for coupling in (.5, 1.):
        runs = []
        for cutoff, order, angular in ((6, 24, 20), (8, 24, 20), (8, 36, 32)):
            coefficients = ground_state(cutoff, coupling)[0]
            interior = neutral_shape_profile(coefficients, cutoff, retained, order, angular)
            endpoints = neutral_shape_endpoints(coefficients, cutoff, order)
            runs.append(np.concatenate((endpoints[:1], interior, endpoints[1:])))
        for earlier in runs[:-1]:
            close(earlier, runs[-1], rtol=3e-8, atol=4e-12)
        profile = runs[-1]
        coefficients = ground_state(8, coupling)[0]
        endpoint_errors = []
        for distance in (1e-3, 1e-7):
            near = np.array([-1+distance, 1-distance])
            values = neutral_shape_profile(coefficients, 8, near, 36, 32)
            endpoint_errors.append(float(np.max(np.abs(values-profile[[0, -1]]))))
        assert endpoint_errors[-1] < endpoint_errors[0]+3e-12
        close(values, profile[[0, -1]], rtol=2e-7, atol=4e-12)
        finite_mode = all_readout_diagnostic(8, coupling, 36, 32)[2]
        peak = int(np.argmax(profile))
        sampled_max = float(profile[peak])
        # A numerical consistency check for THIS grid, not a theorem that
        # any sampled maximum bounds the continuous multiplier or its gap.
        assert finite_mode <= sampled_max+1e-8*coupling*coupling+4e-12
        print(f"neutral shape lambda={coupling:g}: 257-point grid/endpoint maximum="
              f"{sampled_max:.12g} at a={grid[peak]:.8g}; "
              f"endpoints=({profile[0]:.12g},{profile[-1]:.12g}); "
              f"eight-mode value={finite_mode:.12g}; "
              f"near-endpoint error={endpoint_errors[-1]:.3e}")
    leading_errors = []
    for coupling in (.02, .1):
        coefficients = ground_state(8, coupling)[0]
        interior = neutral_shape_profile(coefficients, 8, retained, 36, 32)
        endpoints = neutral_shape_endpoints(coefficients, 8, 36)
        ratios = np.concatenate((endpoints, interior))/(coupling*coupling)
        leading_errors.append(float(np.max(np.abs(ratios-1/144))))
        print(f"  neutral shape lambda={coupling:g}: sampled c/lambda^2 range="
              f"[{ratios.min():.12g},{ratios.max():.12g}], leading value=1/144")
    assert leading_errors[0] < leading_errors[1] and leading_errors[0] < 1e-4
    print("PASS direct neutral multiplier samples with fixed retained nodes, separate "
          "cutoff/hidden-quadrature refinements and analytic Galerkin endpoint limits. "
          "The all-neutral optimal constant is the continuous essential supremum; "
          "this sampled maximum is not a certified supremum or a spectral-gap estimate.")


def marginal_jet(coefficients, cutoff, retained):
    """Return rho_A and its first three a-derivatives, including a=+/-1.

    Real invariant coefficients c_nmk give rho_A=sum_mk (sum_n
    c_nmk R_nk(a))^2 by hidden radial/angular orthonormality. Writing
    R_nk=(1-a^2)^(k/2) times a normalized Gegenbauer polynomial makes
    each square polynomial. Differentiate those polynomials analytically,
    without finite differences, logarithms, or singular fixed-z jets.
    """
    retained = np.asarray(retained, dtype=float)
    assert retained.ndim == 1 and np.all(np.abs(retained) <= 1)
    assert np.isrealobj(coefficients) and len(coefficients) == len(labels(cutoff))
    lookup = {label: index for index, label in enumerate(labels(cutoff))}
    h = 1-retained*retained
    result = np.zeros((4, len(retained)))
    for k in range(cutoff+1):
        degree, parameter = cutoff-k, k+1
        table = np.zeros((4, len(retained), degree+1))
        table[0, :, 0] = 1
        for p in range(1, degree+1):
            for derivative in range(4):
                first = retained*table[derivative, :, p-1]
                if derivative:
                    first = first+derivative*table[derivative-1, :, p-1]
                previous = table[derivative, :, p-2] if p > 1 else 0.
                table[derivative, :, p] = (2*(p+parameter-1)*first
                                           -(p+2*parameter-2)*previous)/p
        norms = np.array([math.factorial(p+2*k+1)
                          /(4**k*math.factorial(p)*(p+k+1)*math.factorial(k)**2)
                          for p in range(degree+1)])
        block = np.array([[coefficients[lookup[n, m, k]] for m in range(k, cutoff+1)]
                          for n in range(k, cutoff+1)])/np.sqrt(norms)[:, None]
        value, first, second, third = (row@block for row in table)
        squares = np.array([np.sum(value*value, axis=1),
                            np.sum(2*value*first, axis=1),
                            np.sum(2*(first*first+value*second), axis=1),
                            np.sum(2*(3*first*second+value*third), axis=1)])
        powers = np.zeros((4, len(retained)))
        powers[0] = h**k
        if k >= 1:
            powers[1] = -2*k*retained*h**(k-1)
            powers[2] = -2*k*h**(k-1)
        if k >= 2:
            powers[2] += 4*k*(k-1)*retained*retained*h**(k-2)
            powers[3] = 12*k*(k-1)*retained*h**(k-2)
        if k >= 3:
            powers[3] -= 8*k*(k-1)*(k-2)*retained**3*h**(k-3)
        for derivative in range(4):
            result[derivative] += sum(math.comb(derivative, j)*powers[j]*squares[derivative-j]
                                      for j in range(derivative+1))
    assert np.all(np.isfinite(result))
    return result


def marginal_effective_profile(coefficients, cutoff, retained):
    """Sample stationary-reconstruction slope and angular curvature, kappa=1.

    chi=sqrt(rho_A), a=cos(theta), U_rec=(h chi''-3a chi')/chi.
    Only for a stationary vector is U_rec'=F'(a)-lambda. For an
    evolving amplitude the actual instantaneous potential slope is
    U_rec'-d_a d_t log(chi); the temporal correction must be retained.
    A negative a-derivative corresponds to a positive theta-derivative.
    The angular curvature is +infinity at the two radial endpoints.
    """
    retained = np.asarray(retained, dtype=float)
    h = 1-retained*retained
    rho, first, second, third = marginal_jet(coefficients, cutoff, retained)
    assert np.all(rho > 0)
    ratio = first/rho
    u1 = ratio/2
    u2 = (second/rho-ratio*ratio)/2
    u3 = (third/rho-3*ratio*second/rho+2*ratio**3)/2
    potential_derivative = (h*(u3+2*u1*u2)-2*retained*(u2+u1*u1)
                            -3*u1-3*retained*u2)
    curvature = np.full_like(retained, np.inf)
    interior = h > 0
    curvature[interior] = (2/h[interior]-2*h[interior]*u2[interior]
                           +2*retained[interior]*u1[interior])
    assert np.all(np.isfinite(potential_derivative))
    return rho, potential_derivative, curvature


def marginal_shape_checks(include_tail=False):
    # Independent polynomial jets test every Leibniz term, including the
    # k>0 channels whose radial square roots are singular coordinates.
    polynomial = np.polynomial.Polynomial
    variable = polynomial([0., 1.])
    h_polynomial = 1-variable*variable
    controls = [((0, 0, 0), polynomial([1.])),
                ((1, 1, 0), 4*variable**2),
                ((1, 1, 1), (4/3)*h_polynomial),
                ((2, 0, 0), (4*variable**2-1)**2),
                ((2, 2, 1), 8*variable**2*h_polynomial),
                ((2, 2, 2), (8/5)*h_polynomial**2)]
    test_nodes = np.linspace(-1., 1., 31)
    for label, target in controls:
        coefficients = np.zeros(len(labels(2)))
        coefficients[labels(2).index(label)] = 1
        actual = marginal_jet(coefficients, 2, test_nodes)
        close(actual, np.array([target.deriv(j)(test_nodes) for j in range(4)]), atol=2e-12)
    # The Haar control does not call ground_state at zero coupling, where
    # its strict positive-energy assertion is intentionally inapplicable.
    rho, derivative, curvature = marginal_effective_profile(np.ones(1), 0, test_nodes)
    close(rho, np.ones_like(test_nodes))
    close(derivative, np.zeros_like(test_nodes))
    close(curvature[1:-1], 2/(1-test_nodes[1:-1]**2))

    # Check the marginal and its first jet against the existing positive
    # b,u quadrature, not another use of the orthogonality sum-of-squares.
    coefficients = ground_state(8, 1.)[0]
    retained = np.linspace(-.93, .93, 19)
    b, wb, angle, wu = quadrature(24, 20)
    psi, da, _, _ = evaluate(coefficients, 8, retained, b, angle)
    assert np.min(psi) > 0
    hidden_weights = wb[None, :, None]*wu[None, None, :]
    direct = np.array([np.sum(psi*psi*hidden_weights, axis=(1, 2)),
                       np.sum(2*psi*da*hidden_weights, axis=(1, 2))])
    close(marginal_jet(coefficients, 8, retained)[:2], direct, atol=3e-12)
    q, weights, _, _ = quadrature(24, 2)
    close(weights@marginal_jet(coefficients, 8, q)[0], coefficients@coefficients)

    grid = np.linspace(-1., 1., 2001)
    regimes = [(.5, 8, 10), (1., 8, 10), (2., 10, 12), (4., 10, 12), (8., 12, 14)]
    if include_tail:
        regimes.append((16., 14, 16))
    for coupling, coarse_cutoff, fine_cutoff in regimes:
        runs = []
        residuals = []
        for cutoff in (coarse_cutoff, fine_cutoff):
            coefficients, _, residual, _ = ground_state(cutoff, coupling)
            runs.append(marginal_effective_profile(coefficients, cutoff, grid))
            residuals.append(residual)
        rho, derivative, curvature = runs[-1]
        relative_density_error = float(np.max(np.abs(runs[0][0]/rho-1)))
        derivative_error = float(np.max(np.abs(runs[0][1]-derivative)))
        curvature_error = float(np.max(np.abs(runs[0][2][1:-1]-curvature[1:-1])))
        assert relative_density_error < 1e-8 and derivative_error < 2e-6
        assert curvature_error < 2e-8
        assert np.max(derivative) < 0 and np.min(curvature[1:-1]) > 0
        peak, minimum = int(np.argmax(derivative)), int(np.argmin(curvature))
        print(f"marginal shape lambda={coupling:g}, cutoffs={coarse_cutoff}/{fine_cutoff}: "
              f"min rho={rho.min():.12g}, max dVeff/da={derivative[peak]:.12g} "
              f"at a={grid[peak]:.6g}, min neutral curvature={curvature[minimum]:.12g} "
              f"at a={grid[minimum]:.6g}")
        print(f"  cutoff changes: relative rho={relative_density_error:.3e}, "
              f"dVeff/da={derivative_error:.3e}, curvature={curvature_error:.3e}; "
              f"fine full residual={residuals[-1]:.3e}")
    # A separate exploratory lambda=32 scan showed spurious sign failures
    # at low cutoff in the tiny-density tail. Do not encode that artifact
    # as a portable assertion or accept energy convergence as jet control.
    print("PASS analytic marginal jets: polynomial/endpoint/Haar controls and "
          "independent hidden quadrature; sampled decreasing effective potential "
          "and positive neutral curvature in the stated converged cutoff tests. "
          "No certified continuous sign bound, all-coupling theorem or uniform "
          "Yang--Mills estimate follows from these finite samples.")


def holonomy_hessian_contraction(a, b, z):
    """H_ij=Hess(a)(grad x_i,grad x_j) for the full raw metric.

    x=(a,b,z). Differentiate the polynomial cometric, not a metric
    inverse on the singular orbit body. H_ij = (g_ki d_k g_aj
    +g_kj d_k g_ai-g_ak d_k g_ij)/2, with kappa excluded.
    """
    metric = coordinate_metric(a, b, z)
    jets = np.zeros((*metric.shape[:-2], 3, 3, 3))
    # Last three indices are derivative coordinate, row, column.
    jets[..., 0, 0, 0], jets[..., 1, 1, 1] = -2*a, -2*b
    jets[..., 2, 0, 1] = jets[..., 2, 1, 0] = .25
    for coordinate, values in enumerate(((-z+a*b/2, -(1-b*b)/4),
                                         (-(1-a*a)/4, -z+a*b/2),
                                         (-a, -b))):
        jets[..., coordinate, 0, 2] = jets[..., coordinate, 2, 0] = values[0]
        jets[..., coordinate, 1, 2] = jets[..., coordinate, 2, 1] = values[1]
    jets[..., 0, 2, 2] = -a-a*b*b+b*z/2
    jets[..., 1, 2, 2] = -b-a*a*b+a*z/2
    jets[..., 2, 2, 2] = -3*z+a*b/2
    first = np.einsum("...ki,...kj->...ij", metric, jets[..., :, 0, :])
    hessian = (first+np.swapaxes(first, -1, -2)
               -np.einsum("...k,...kij->...ij", metric[..., 0, :], jets))/2
    close(hessian[..., 0, 0], -a*(1-a*a))
    return hessian


def marginal_stress_diagnostic(cutoff, coupling, order, angular):
    """Weak MF21/TP30 checks, retaining orbit and radial stress, kappa=1."""
    coefficients = ground_state(cutoff, coupling)[0]
    a, wa, angle, wu = quadrature(order, angular)
    aa, bb, uu = a[:, None, None], a[None, :, None], angle[None, None, :]
    h, hb = 1-aa*aa, 1-bb*bb
    z = np.sqrt(h*hb)*uu
    psi, da, db, du = evaluate(coefficients, cutoff, a, a, angle)
    assert np.min(psi) > 0
    rho, first, _, _ = marginal_jet(coefficients, cutoff, a)
    _, potential_slope, _ = marginal_effective_profile(coefficients, cutoff, a)
    marginal_score = first/(2*rho)
    phi_gradient = np.stack(np.broadcast_arrays(
        da+aa*uu*du/h-psi*marginal_score[:, None, None],
        db+bb*uu*du/hb, du/np.sqrt(h*hb)), axis=-1)/np.sqrt(rho)[:, None, None, None]
    metric = coordinate_metric(aa, bb, z)
    hessian = holonomy_hessian_contraction(aa, bb, z)
    hidden_weights = wa[None, :, None]*wu[None, None, :]
    projected = np.einsum("...i,...i->...", metric[..., 0, :], phi_gradient)
    s = np.sum(hidden_weights*projected*projected, axis=(1, 2))
    tau = np.sum(hidden_weights*np.einsum("...i,...ij,...j->...",
                                         phi_gradient, hessian, phi_gradient), axis=(1, 2))
    mean_z = np.sum(hidden_weights*psi*psi*z, axis=(1, 2))/rho
    weights = wa*rho
    left, right, radial_only = [], [], []
    for degree in range(5):
        probe = a**degree
        slope = degree*a**(degree-1) if degree else np.zeros_like(a)
        left.append(weights@((1-a*a)*(potential_slope+coupling)*probe))
        right.append(weights@(-coupling*mean_z*probe/4-2*(tau*probe+s*slope)))
        # Hess(a) on the orbit-normal unit vector is -a. Keeping only
        # this block of M would replace tau by -a*s/h and is wrong.
        reduced_tau = -a*s/(1-a*a)
        radial_only.append(weights@(-coupling*mean_z*probe/4-2*(reduced_tau*probe+s*slope)))
    left, right, radial_only = np.array(left), np.array(right), np.array(radial_only)
    close(left, right, rtol=3e-7, atol=3e-10)
    assert np.max(np.abs(left-radial_only)) > 1e-5
    return np.array([np.max(np.abs(left-right)), np.max(np.abs(left-radial_only))])


def marginal_stress_checks():
    for coupling in (.5, 1., 4.):
        diagnostics = [marginal_stress_diagnostic(cutoff, coupling, order, angular)
                       for cutoff, order, angular in ((10, 28, 24), (12, 28, 24), (12, 36, 32))]
        close(np.array([row[1] for row in diagnostics]), np.full(3, diagnostics[-1][1]),
              rtol=2e-7, atol=2e-10)
        error, omitted = diagnostics[-1]
        print(f"marginal stress lambda={coupling:g}: weak identity error={error:.3e}, "
              f"error if orbit stress is omitted={omitted:.9g}")
    print("PASS actual conditional-amplitude stress balance against five polynomial "
          "vector-field tests, independent of differentiating M; cutoff/quadrature "
          "refinements retain the shared geometry. Omitting orbit stress fails. "
          "Finite tests do not prove a pointwise signed bound or a Yang--Mills gap.")
    # The one-sided stress-sign proposal fails even where the effective
    # potential is monotone. Compare with the analytically derived quartic
    # coefficient, not a rational coefficient fitted to these data.
    a = np.array([-.5, .5])
    b, wb, angle, wu = quadrature(32, 28)
    z = np.sqrt((1-a[:, None, None]**2)*(1-b[None, :, None]**2))*angle
    hidden_weights = wb[None, :, None]*wu
    target = 5561/63078912
    errors = []
    for coupling in (.1, .05):
        coefficients = ground_state(8, coupling)[0]
        psi = evaluate(coefficients, 8, a, b, angle)[0]
        rho, potential_slope, _ = marginal_effective_profile(coefficients, 8, a)
        mean_z = np.sum(hidden_weights*psi*psi*z, axis=(1, 2))/rho
        stress = ((1-a*a)*(potential_slope+coupling)+coupling*mean_z/4)/2
        ratios = stress/(coupling**4*a*(1-a*a))
        assert stress[0] < 0 < stress[1]
        assert np.max(np.abs(ratios-target)) < 4e-7
        errors.append(abs(float(ratios.mean())-target))
        print(f"quartic stress lambda={coupling:g}: signed values={stress}, "
              f"normalized ratios={ratios}, analytic coefficient={target:.12g}")
    assert errors[1] < errors[0]
    print("PASS finite quartic stress sign/scaling check. The actual-vacuum sign "
          "obstruction is proved by the normalized perturbative expansion, not "
          "these floating-point cancellations.")


def amplitude_evolution(cutoff, coupling, times, initial):
    """Normalized exp(-t H)initial and its time derivative, kappa=1.

    Keep every relational k channel in the supplied finite Galerkin
    carrier. Shifting all eigenvalues by E0 only prevents underflow;
    normalization does not replace the supplied H by a marginal clock.
    Rows are (coefficients, time_derivative, mean_energy, outside_norm).
    """
    basis, lookup, kinetic, multiplication = matrices(cutoff)
    hamiltonian = kinetic+coupling*(2*np.eye(len(basis))-multiplication)
    energies, vectors = np.linalg.eigh(hamiltonian)
    initial = np.asarray(initial, dtype=float)
    assert initial.shape == (len(basis),)
    close(initial@initial, 1.)
    source = vectors.T@initial
    result = []
    for duration in times:
        assert duration >= 0
        if duration == 0:
            coefficients = initial.copy()
        else:
            coefficients = vectors@(np.exp(-duration*(energies-energies[0]))*source)
            coefficients /= np.linalg.norm(coefficients)
        action = hamiltonian@coefficients
        mean_energy = float(coefficients@action)
        velocity = -action+mean_energy*coefficients
        close(coefficients@velocity, 0., atol=2e-12)
        close(2*velocity@action, -2*velocity@velocity, atol=2e-11)
        outside_squared = 0.
        for index, (n, m, k) in enumerate(basis):
            if n == cutoff:
                outside_squared += (coupling*raising(n, k)*coefficients[index])**2
            if m == cutoff:
                outside_squared += (coupling*raising(m, k)*coefficients[index])**2
        result.append((coefficients, velocity, mean_energy, math.sqrt(outside_squared)))
    return result


def haar_amplitude_evolution(cutoff, coupling, times):
    """The actual Haar input, distinguished from other positive preparations."""
    initial = np.zeros(len(labels(cutoff)))
    initial[labels(cutoff).index((0, 0, 0))] = 1.
    return amplitude_evolution(cutoff, coupling, times, initial)


def marginal_time_jet(coefficients, velocity, cutoff, retained):
    """Exact polarization of the quadratic marginal jet, not a time difference."""
    scale = 1/max(1., float(np.linalg.norm(velocity)))
    return (marginal_jet(coefficients+scale*velocity, cutoff, retained)
            -marginal_jet(coefficients-scale*velocity, cutoff, retained))/(2*scale)


def evolution_shape_checks():
    """Finite evolution controls, including actual conditional-force curvature.

    Stationary reconstruction alone is not the instantaneous potential.
    The final force-curvature test includes the time derivative and checks
    both cutoff and spatial-difference resolution; it is not a certified
    bound over time, coupling, or the whole continuum latitude interval.
    """
    grid = np.linspace(-1., 1., 1001)
    origin, velocity, _, _ = haar_amplitude_evolution(4, 2., [0.])[0]
    origin_time = marginal_time_jet(origin, velocity, 4, grid)
    close(origin_time[0], 4*grid)
    close(origin_time[1], np.full_like(grid, 4.))
    close(origin_time[2:], np.zeros_like(origin_time[2:]))
    selected_state = None
    force_control_state = None
    # The last short-time member disproves preservation of the angular
    # convexity cone, not a property of its final ground state or gap.
    for coupling, coarse_cutoff, fine_cutoff, times in (
            (2., 8, 10, (.02, .2, 1.)),
            (16., 14, 16, (.02, .2, 1.)),
            (64., 14, 16, (3/64, 4/64))):
        histories = []
        for cutoff in (coarse_cutoff, fine_cutoff):
            history = []
            for duration, state in zip(times, haar_amplitude_evolution(cutoff, coupling, times)):
                coefficients, velocity, mean_energy, outside = state
                rho, reconstructed, curvature = marginal_effective_profile(coefficients, cutoff, grid)
                jet = marginal_jet(coefficients, cutoff, grid)
                time_jet = marginal_time_jet(coefficients, velocity, cutoff, grid)
                log_second = (jet[2]/rho-(jet[1]/rho)**2)/2
                temporal_slope = (time_jet[1]/rho-time_jet[0]*jet[1]/rho**2)/2
                instantaneous = reconstructed-temporal_slope
                history.append((rho, reconstructed, curvature, log_second, instantaneous, outside))
                if coupling == 16 and duration == .2 and cutoff == fine_cutoff:
                    selected_state = (coefficients, velocity, mean_energy, cutoff)
                if coupling == 64 and duration == 3/64 and cutoff == fine_cutoff:
                    force_control_state = state
            histories.append(history)
        for duration, coarse, fine in zip(times, *histories):
            rho, reconstructed, curvature, log_second, instantaneous, outside = fine
            density_error = float(np.max(np.abs(coarse[0]/rho-1)))
            reconstructed_error = float(np.max(np.abs(coarse[1]-reconstructed)))
            curvature_error = float(np.max(np.abs(coarse[2][1:-1]-curvature[1:-1])))
            instantaneous_error = float(np.max(np.abs(coarse[4]-instantaneous)))
            assert density_error < 1e-6 and reconstructed_error < .02
            assert curvature_error < 1e-4 and instantaneous_error < .04
            assert np.max(log_second) < 0 and np.max(instantaneous) < 0
            if coupling == 16 and duration == .2:
                assert reconstructed[0] > 2 and np.min(curvature) > 0
            if coupling == 64:
                assert np.min(curvature) < 0
            print(f"Haar evolution lambda={coupling:g}, t={duration:.8g}, "
                  f"cutoffs={coarse_cutoff}/{fine_cutoff}: min rho={rho.min():.6g}, "
                  f"max reconstructed dV/da={reconstructed.max():.12g}, "
                  f"max actual instantaneous dV/da={instantaneous.max():.12g}, "
                  f"min angular curvature={curvature.min():.12g}, "
                  f"log-chi aa range=[{log_second.min():.12g},{log_second.max():.12g}]")
            print(f"  cutoff changes rho={density_error:.3e}, reconstructed={reconstructed_error:.3e}, "
                  f"curvature={curvature_error:.3e}, instantaneous={instantaneous_error:.3e}; "
                  f"outside H amplitude={outside:.3e}")

    coefficients, velocity, mean_energy, cutoff = selected_state
    splits = []
    for order, angular in ((24, 20), (36, 32)):
        a, wa, angle, wu = quadrature(order, angular)
        psi = evaluate(coefficients, cutoff, a, a, angle)[0]
        psi_time = evaluate(velocity, cutoff, a, a, angle)[0]
        assert np.min(psi) > 0
        rho = marginal_jet(coefficients, cutoff, a)[0]
        rho_time = marginal_time_jet(coefficients, velocity, cutoff, a)[0]
        log_chi_time = rho_time/(2*rho)
        retained_rate = float(wa@(rho*log_chi_time**2))
        relative_time = psi_time-psi*log_chi_time[:, None, None]
        joint_weights = wa[:, None, None]*wa[None, :, None]*wu[None, None, :]
        conditional_rate = float(np.sum(joint_weights*relative_time**2))
        close(retained_rate+conditional_rate, velocity@velocity, rtol=3e-9, atol=2e-11)
        splits.append(np.array([retained_rate, conditional_rate]))
    close(splits[0], splits[1], rtol=3e-9, atol=2e-11)

    # Check the time correction against a separately integrated F_t:
    # lambda(1-E[b|a])+E[Gamma(log psi)|a]-h(log chi)'^2.
    # This is a value check; all reported a-derivatives above use jets.
    retained = np.array([-.9, -.5, 0., .5, .9])
    b, wb, angle, wu = quadrature(36, 32)
    psi, da, db, du = evaluate(coefficients, cutoff, retained, b, angle)
    aa, bb, uu = retained[:, None, None], b[None, :, None], angle[None, None, :]
    ra, rb = np.sqrt(1-aa*aa), np.sqrt(1-bb*bb)
    z = ra*rb*uu
    gradient = np.stack((da+aa*uu*du/(ra*ra), db+bb*uu*du/(rb*rb), du/(ra*rb)), axis=-1)
    metric = coordinate_metric(aa, bb, z)
    kinetic_density = np.einsum("...i,...ij,...j->...", gradient, metric, gradient)
    hidden_weights = wb[None, :, None]*wu[None, None, :]
    jet = marginal_jet(coefficients, cutoff, retained)
    time_jet = marginal_time_jet(coefficients, velocity, cutoff, retained)
    rho = jet[0]
    first = jet[1]/(2*rho)
    second = (jet[2]/rho-(jet[1]/rho)**2)/2
    mean_b = np.sum(psi*psi*bb*hidden_weights, axis=(1, 2))/rho
    direct = 16*(1-mean_b)+np.sum(kinetic_density*hidden_weights, axis=(1, 2))/rho
    direct -= (1-retained*retained)*first*first
    reconstructed_value = (1-retained*retained)*(second+first*first)-3*retained*first
    dynamic = mean_energy-16*(1-retained)+reconstructed_value-time_jet[0]/(2*rho)
    close(direct, dynamic, rtol=3e-9, atol=2e-10)
    print(f"  lambda=16,t=.2 energy-loss split: ||chi_dot||^2={splits[-1][0]:.12g}, "
          f"integrated ||Phi_dot||^2={splits[-1][1]:.12g}, "
          f"-E_dot={2*float(velocity@velocity):.12g}; direct F_t/time-corrected values agree")

    # Differentiate the ACTUAL slope -lambda+F_t', not U_rec' alone.
    # Since lambda is constant, this is F_t''. A strict negative value
    # falsifies the stronger source condition F_t'' >= 0. The weaker
    # first-contact source F_t''+2*kappa*p^2 is a separate sampled test.
    force_grid = np.linspace(-1., 1., 4001)
    interior = np.abs(force_grid) <= .9
    for coupling, duration, coarse_cutoff, fine_cutoff, coarse_state in (
            (64., 3/64, 16, 18, force_control_state),
            (128., 4/128, 20, 22, None)):
        force_histories = []
        for cutoff in (coarse_cutoff, fine_cutoff):
            state = (coarse_state if cutoff == coarse_cutoff and coarse_state is not None
                     else haar_amplitude_evolution(cutoff, coupling, [duration])[0])
            coefficients, velocity, _, outside = state
            jet = marginal_jet(coefficients, cutoff, force_grid)
            time_jet = marginal_time_jet(coefficients, velocity, cutoff, force_grid)
            rho, reconstructed, _ = marginal_effective_profile(coefficients, cutoff, force_grid)
            p = jet[1]/(2*rho)
            temporal_slope = (time_jet[1]/rho-time_jet[0]*jet[1]/rho**2)/2
            actual_slope = reconstructed-temporal_slope
            force_second = np.gradient(actual_slope, force_grid, edge_order=2)
            half_grid = force_grid[::2]
            half_interior = np.abs(half_grid) <= .9
            half_second = np.gradient(actual_slope[::2], half_grid, edge_order=2)
            difference_error = float(np.max(np.abs(
                half_second[half_interior]-force_second[::2][half_interior])))
            force_histories.append((force_second, p, difference_error, outside))
        force_second, p, difference_error, outside = force_histories[-1]
        cutoff_error = float(np.max(np.abs(
            force_histories[0][0][interior]-force_second[interior])))
        weaker_source = force_second+2*p*p  # kappa=1 throughout this receipt.
        assert np.max(force_second[interior]) < -.004
        assert cutoff_error < 2e-5 and difference_error < 5e-7
        assert np.min(weaker_source[interior]) > 10.
        print(f"  actual force curvature lambda={coupling:g},t={duration:.8g}, |a|<=.9, "
              f"cutoffs={coarse_cutoff}/{fine_cutoff}, grids=2001/4001: "
              f"F_t'' range=[{force_second[interior].min():.12g},"
              f"{force_second[interior].max():.12g}], "
              f"min(F_t''+2*p^2)={weaker_source[interior].min():.12g}; "
              f"cutoff change={cutoff_error:.3e}, difference change={difference_error:.3e}, "
              f"outside H amplitude={outside:.3e}")
    print("PASS full relational Haar evolution and temporal correction: reconstructed "
          "stationary-potential monotonicity and angular convexity can fail transiently. "
          "The stronger actual-force condition F_t''>=0 also fails the refined finite "
          "controls; their positive weaker F_t''+2*p^2 values are evidence beyond the "
          "unspecified small-coupling theorem range, not an extension of that theorem. "
          "The actual instantaneous potential and latitude log-concavity pass only the "
          "stated sampled tests; these are not all-time, all-coupling or certified gap bounds.")


def weak_coupling_evolution_checks():
    """Check leading uniform-time coefficients, without estimating the theorem's r0.

    tau=kappa*t and r=lambda/kappa; here kappa=1. The exact leading
    coefficients come from perturbative evolution, not fitted state data.
    v=(log chi)'' is sampled including both analytic latitude endpoints;
    S=F_t''+2*kappa*p^2 uses the actual temporal correction and interior
    finite differences of its slope. This finite list does not verify a
    uniform analytic remainder or select a valid all-time r threshold.
    """
    grid = np.linspace(-1., 1., 2001)
    interior = np.abs(grid) <= .9
    times = (0., .03, .1, .5, 2., 8.)
    nodes, weights = np.polynomial.legendre.leggauss(64)
    leading = {}
    for duration in times:
        amplitude = -math.expm1(-3*duration)/3
        integration_nodes = duration*(nodes+1)/2
        amplitudes = -np.expm1(-3*integration_nodes)/3
        # Positive integral avoids cancellation of four nearly equal
        # terms in the closed formula when tau is small.
        decay = float(duration*(weights@(np.exp(-8*(duration-integration_nodes))*amplitudes**2)))
        explicit = (1/36-4*math.exp(-3*duration)/45
                    +math.exp(-6*duration)/9-math.exp(-8*duration)/20)
        close(decay, explicit, rtol=2e-12, atol=5e-16)
        if duration == 0:
            assert amplitude == decay == 0
        else:
            assert amplitude > 0 and decay > 0
        leading[duration] = amplitude, decay
    errors = []
    for coupling in (.05, .1, .2):
        histories = []
        for cutoff in (6, 8):
            history = []
            for duration, state in zip(times, haar_amplitude_evolution(cutoff, coupling, times)):
                coefficients, velocity, _, _ = state
                jet = marginal_jet(coefficients, cutoff, grid)
                time_jet = marginal_time_jet(coefficients, velocity, cutoff, grid)
                rho, reconstructed, _ = marginal_effective_profile(coefficients, cutoff, grid)
                p = jet[1]/(2*rho)
                v = (jet[2]/rho-(jet[1]/rho)**2)/2
                temporal_slope = (time_jet[1]/rho-time_jet[0]*jet[1]/rho**2)/2
                force_second = np.gradient(reconstructed-temporal_slope, grid, edge_order=2)
                source = force_second+2*p*p
                if duration == 0:
                    close(v, np.zeros_like(v))
                    close(source[interior], np.zeros_like(source[interior]), atol=2e-12)
                    continue
                amplitude, decay = leading[duration]
                v_ratio = v/(-coupling*coupling*decay)
                source_ratio = source[interior]/(2*coupling*coupling*amplitude*amplitude)
                assert np.min(v_ratio) > 0 and np.min(source_ratio) > 0
                history.append((v_ratio, source_ratio))
            histories.append(history)
        cutoff_changes = np.array([
            max(float(np.max(np.abs(old[k]-new[k]))) for old, new in zip(*histories))
            for k in (0, 1)])
        assert np.max(cutoff_changes) < 2e-6
        relative_errors = np.array([
            max(float(np.max(np.abs(row[k]-1))) for row in histories[-1]) for k in (0, 1)])
        errors.append(relative_errors)
        print(f"weak evolution r={coupling:g}, tau={times[1:]}, cutoffs=6/8: "
              f"max |v/(-r^2 D)-1|={relative_errors[0]:.12g}, "
              f"max |S/(2*r^2 A^2)-1|={relative_errors[1]:.12g}; "
              f"errors/r={relative_errors/coupling}, cutoff changes={cutoff_changes}")
    errors = np.array(errors)
    assert np.all(errors[0] < errors[1]) and np.all(errors[1] < errors[2])
    print(f"  error growth under doubling r: {errors[1]/errors[0]}, {errors[2]/errors[1]}")
    print("PASS weak-coupling time-dependent leading coefficients and decreasing relative "
          "errors as r falls. Zero time remains an exact separate control. The all-time "
          "small-r conclusion requires the analytic uniform remainders; this diagnostic "
          "does not estimate r0 or extend the conclusion to arbitrary couplings.")


def short_layer_coefficient_checks():
    """Fixed-s high-energy asymptotics, not a large-time or threshold test.

    epsilon=kappa/lambda, s=lambda*t, kappa=1. Compare actual full
    evolution with v=-(2/3)epsilon*s^3 and S/kappa=2*s^2. The ratios
    have O(epsilon) errors on bounded s intervals; no epsilon_* is
    estimated here. Keep endpoint v jets and the time-corrected source.
    """
    grid = np.linspace(-1., 1., 2001)
    interior = np.abs(grid) <= .9
    scaled_times = (.5, 1., 2.)
    errors = []
    for coupling in (32., 64., 128.):
        epsilon = 1/coupling
        times = [s/coupling for s in scaled_times]
        histories = []
        for cutoff in (16, 18):
            history = []
            for s, state in zip(scaled_times, haar_amplitude_evolution(cutoff, coupling, times)):
                coefficients, velocity, _, _ = state
                jet = marginal_jet(coefficients, cutoff, grid)
                time_jet = marginal_time_jet(coefficients, velocity, cutoff, grid)
                rho, reconstructed, _ = marginal_effective_profile(coefficients, cutoff, grid)
                p = jet[1]/(2*rho)
                v = (jet[2]/rho-(jet[1]/rho)**2)/2
                temporal_slope = (time_jet[1]/rho-time_jet[0]*jet[1]/rho**2)/2
                force_second = np.gradient(reconstructed-temporal_slope, grid, edge_order=2)
                source = force_second+2*p*p
                v_ratio = v/(-2*epsilon*s**3/3)
                source_ratio = source[interior]/(2*s*s)
                assert np.min(v_ratio) > 0 and np.min(source_ratio) > 0
                history.append((v_ratio, source_ratio))
            histories.append(history)
        cutoff_changes = np.array([
            max(float(np.max(np.abs(old[k]-new[k]))) for old, new in zip(*histories))
            for k in (0, 1)])
        assert np.max(cutoff_changes) < 2e-5
        relative_errors = np.array([
            max(float(np.max(np.abs(row[k]-1))) for row in histories[-1]) for k in (0, 1)])
        errors.append(relative_errors)
        print(f"short layer lambda={coupling:g}, s={scaled_times}, cutoffs=16/18: "
              f"max |v/(-(2/3)*epsilon*s^3)-1|={relative_errors[0]:.12g}, "
              f"max |S/(2*s^2)-1|={relative_errors[1]:.12g}; "
              f"errors/epsilon={relative_errors/epsilon}, cutoff changes={cutoff_changes}")
    errors = np.array(errors)
    assert np.all(errors[0] > errors[1]) and np.all(errors[1] > errors[2])
    print(f"  error contraction as epsilon halves: {errors[1]/errors[0]}, {errors[2]/errors[1]}")
    print("PASS independent bounded-s short-layer coefficients with decreasing relative "
          "errors as epsilon falls. These finite samples do not determine epsilon_* "
          "or extend a bounded-s asymptotic theorem to arbitrarily late clock time.")


def positive_kernel_initial_state_checks():
    """Same H, different positive Gram input: flat marginals need not stay concave.

    psi_in=(1+(d/3)*chi_2(x*y^-1))/sqrt(1+d^2/9), with 0<d<1.
    This kernel is strictly positive, PSD, exchange symmetric, and has
    nonnegative complete harmonic coefficients. Its integral-operator
    rank is ten, not the Haar preparation's rank one. This diagnostic
    does not assert a failure of the actual Haar trajectory.
    """
    d, coupling = .5, 1.
    alpha = d*(d+6)/(3*(d*d+9))
    normalization = math.sqrt(1+d*d/9)
    durations = (.01, .005, .0025)
    probe = np.linspace(-1., 1., 31)
    runs = []
    for cutoff in (6, 8):
        basis, lookup, kinetic, _ = matrices(cutoff)
        relative_character = np.zeros(len(basis))
        for k in range(3):
            relative_character[lookup[2, 2, k]] = math.sqrt(2*k+1)/3
        close(kinetic@relative_character, 12*relative_character)
        close(relative_character@relative_character, 1.)
        initial = (d/3)*relative_character
        initial[lookup[0, 0, 0]] = 1.
        initial /= normalization
        assert np.all(initial >= 0)
        close(initial@initial, 1.)
        # The operator block is C^(k)/sqrt(2k+1), with angular
        # multiplicity 2k+1. This checks PSD and the full rank-ten
        # kernel, not positivity of the scalar function alone.
        rank = 0
        for k in range(cutoff+1):
            block = np.array([[initial[lookup[n, m, k]] for m in range(k, cutoff+1)]
                              for n in range(k, cutoff+1)])/math.sqrt(2*k+1)
            eigenvalues = np.linalg.eigvalsh(block)
            assert eigenvalues.min() >= -1e-14
            rank += (2*k+1)*int(np.count_nonzero(eigenvalues > 1e-14))
        assert rank == 10
        marginal = marginal_jet(initial, cutoff, probe)
        close(marginal[0], np.ones_like(probe))
        close(marginal[1:], np.zeros_like(marginal[1:]))
        # Exchange symmetry gives the same flat full y marginal.
        for index, (n, m, k) in enumerate(basis):
            close(initial[index], initial[lookup[m, n, k]])
        a, _, u, _ = quadrature(8, 8)
        psi = evaluate(initial, cutoff, a, a, u)[0]
        aa, bb = a[:, None, None], a[None, :, None]
        c = aa*bb+np.sqrt((1-aa*aa)*(1-bb*bb))*u[None, None, :]
        close(psi, (1+(d/3)*(4*c*c-1))/normalization)
        assert np.min(psi) >= (1-d/3)/normalization-2e-12
        ratios = []
        for duration, state in zip(durations, amplitude_evolution(cutoff, coupling, durations, initial)):
            coefficients = state[0]
            jet = marginal_jet(coefficients, cutoff, np.array([0.]))
            v = float((jet[2]/jet[0]-(jet[1]/jet[0])**2)[0]/2)
            assert v > 0
            ratios.append(v/(2*coupling*coupling*alpha*duration*duration))
        runs.append(np.array(ratios))
    close(runs[0], runs[1], rtol=3e-8, atol=2e-8)
    errors = np.abs(runs[-1]-1)
    assert errors[2] < errors[1] < errors[0]
    print(f"positive Gram non-Haar input d={d:g}, lambda=1, cutoffs=6/8: "
          f"times={durations}, v(t,0)/(2*lambda^2*alpha*t^2)={runs[-1]}, "
          f"alpha={alpha:.12g}, cutoff change={np.max(np.abs(runs[0]-runs[1])):.3e}")
    print("PASS full relative-channel evolution: PSD rank-ten kernel with both flat "
          "initial marginals develops positive latitude log-Hessian. The exact "
          "counterexample coefficient is not inferred from this finite approximation; "
          "the actual Haar rank-one preparation remains a distinct input.")


def relative_replica_checks():
    """GLOBAL relative moments versus an ideal opposite-feature replica pair.

    The first part uses actual seven-link Haar heat states, including
    every relational channel. The second uses p(a) proportional to
    f_+(a)f_+(-a), not an actual Brownian-averaged state or a squared
    scalar amplitude. Its second ideal shared control starts at -1;
    approximation by based continuous controls belongs to the analytic
    argument and is not implemented or certified by this diagnostic.
    """
    for coupling, coarse_cutoff, fine_cutoff in ((.5, 8, 10), (16., 14, 16)):
        states = {cutoff: haar_amplitude_evolution(cutoff, coupling, [.2])[0][0]
                  for cutoff in (coarse_cutoff, fine_cutoff)}
        runs = []
        for cutoff, order, angular in ((coarse_cutoff, 24, 20),
                                       (fine_cutoff, 24, 20), (fine_cutoff, 36, 32)):
            a, wa, u, wu = quadrature(order, angular)
            psi = evaluate(states[cutoff], cutoff, a, a, u)[0]
            assert np.min(psi) > 0
            aa, bb = a[:, None, None], a[None, :, None]
            c = aa*bb+np.sqrt((1-aa*aa)*(1-bb*bb))*u[None, None, :]
            weights = wa[:, None, None]*wa[None, :, None]*wu[None, None, :]*psi*psi
            close(np.sum(weights), 1.)
            alpha1 = float(np.sum(weights*c))
            alpha2 = float(np.sum(weights*(4*c*c-1)/3))
            runs.append(np.array([alpha1, alpha2, alpha2-alpha1*alpha1]))
        for earlier in runs[:-1]:
            close(earlier, runs[-1], atol=5e-13)
        assert runs[-1][2] < 0
        print(f"GLOBAL actual relative moments lambda={coupling:g},t=.2, "
              f"cutoffs={coarse_cutoff}/{fine_cutoff}: alpha1={runs[-1][0]:.12g}, "
              f"alpha2={runs[-1][1]:.12g}, alpha2-alpha1^2={runs[-1][2]:.12g}")

    # D has eigenvalue n(n+2)/4 on U_n. The outer three-link
    # path therefore uses 3D, not the four-link radial coefficient.
    times = (.2, .1, .05)
    runs = []
    for cutoff, order in ((16, 32), (20, 32), (20, 48)):
        n = np.arange(cutoff+1)
        hamiltonian = np.diag(.75*n*(n+2)+1.)
        hamiltonian -= (np.diag(np.ones(cutoff), 1)+np.diag(np.ones(cutoff), -1))/2
        energies, vectors = np.linalg.eigh(hamiltonian)
        a, wa, _, _ = quadrature(order, 2)
        characters = character_jet(cutoff, a)[0]
        history = []
        for duration in times:
            coefficients = vectors@(np.exp(-duration*(energies-energies[0]))*vectors[0, :])
            plus = characters@coefficients
            minus = characters@(((-1.)**n)*coefficients)
            assert np.min(plus) > 0 and np.min(minus) > 0
            product = plus*minus
            close(product, product[::-1])
            density = product/float(wa@product)
            beta1 = float(wa@(density*a))
            beta2 = float(wa@(density*(4*a*a-1)/3))
            close(beta1, 0., atol=3e-15)
            assert beta2 < 0 and beta2*beta2 > beta1**4
            history.append(np.array([beta1, beta2, beta2/(-duration**3/24)]))
        runs.append(np.array(history))
    for earlier in runs[:-1]:
        close(earlier, runs[-1], rtol=3e-9, atol=2e-10)
    errors = np.abs(runs[-1][:, 2]-1)
    assert errors[2] < errors[1] < errors[0]
    print(f"opposite-feature outer-path scalar control kappa=lambda=1, cutoffs=16/20: "
          f"times={times}, beta2={runs[-1][:, 1]}, beta2/(-t^3/24)={runs[-1][:, 2]}, "
          f"relative alpha2=beta2^2={runs[-1][:, 1]**2}; alpha1=0 exactly by parity")
    print("PASS refined global moment samples and opposite-feature scalar product. "
          "The latter violates the relative-moment inequality within an ideal "
          "conditional replica law, not in the actual Brownian average. Neither "
          "global moment comparison is a local conditional-Hessian or mass-gap estimate.")


def endpoint_source_channels(cutoff, coupling, duration, steps):
    """Finite endpoint source moments from an off-sphere generating function.

    Use the full asymmetric operator H0-lambda*r*a-lambda*b on the
    Haar vector, WITHOUT amplitude normalization or constant potential
    terms. Its unnormalized marginal G(r,q) equals F(a,h) at
    r=sqrt(a^2+h), q=a/r. Radial derivatives use five-point finite
    differences; latitude derivatives use the independent polynomial
    marginal jets. No truncated positive source measure is constructed.
    """
    basis, lookup, kinetic, multiplication = matrices(cutoff)
    left = np.zeros_like(multiplication)
    for index, (n, m, k) in enumerate(basis):
        other_label = (n+1, m, k)
        if other_label in lookup:
            other = lookup[other_label]
            left[index, other] = left[other, index] = raising(n, k)
    right = multiplication-left
    swap = np.array([lookup[m, n, k] for n, m, k in basis])
    close(right, left[np.ix_(swap, swap)])
    endpoints = np.array([-1., 1.])
    radius_jets = {}

    def jet(offset):
        # Identical radii shared by the three stencils need one solve.
        offset = round(float(offset), 12)
        if offset not in radius_jets:
            radius = 1+offset
            assert radius > 0
            operator = kinetic-coupling*radius*left-coupling*right
            energies, vectors = np.linalg.eigh(operator)
            coefficients = vectors@(np.exp(-duration*energies)
                                    *vectors[lookup[0, 0, 0], :])
            radius_jets[offset] = marginal_jet(coefficients, cutoff, endpoints)
        return radius_jets[offset]

    base = jet(0.)
    value, latitude, latitude2 = base[:3]
    assert np.min(value) > 0
    physical_v = (latitude2/value-(latitude/value)**2)/2
    runs = []
    for step in steps:
        minus2, minus, plus, plus2 = (jet(j*step) for j in (-2, -1, 1, 2))
        radial = (minus2-8*minus+8*plus-plus2)/(12*step)
        radial2 = (-minus2+16*minus-30*base+16*plus-plus2)/(12*step*step)
        gr, grr, grq = radial[0], radial2[0], radial[1]
        # Chain rule at (a,h)=(s,0), s=+/-1. The independent variables
        # of F are a,h; they must not be replaced by a on-sphere jet.
        fa, faa = endpoints*gr, grr
        fh = (gr-endpoints*latitude)/2
        fah = endpoints*(grr-gr)/2-grq/2+latitude
        fhh = (grr-2*endpoints*grq+latitude2-gr+3*endpoints*latitude)/4
        mean_eta = fa/value
        mean_b2, mean_b4 = 6*fh/value, 60*fhh/value
        variance_eta = faa/value-mean_eta*mean_eta
        covariance = 6*(fah/value-fa*fh/(value*value))
        variance_b2 = mean_b4-mean_b2*mean_b2
        score_variance = (variance_eta+variance_b2/9
                          -2*endpoints*covariance/3)
        geometric = mean_b2/3+2*mean_b4/45
        reconstructed_v = (score_variance-geometric)/2
        # This equality checks the coordinate algebra. It is NOT an
        # independent proof of a curvature sign or source positivity.
        close(reconstructed_v, physical_v, rtol=2e-10, atol=2e-10)
        moments = np.column_stack((mean_eta, mean_b2, mean_b4,
                                   variance_eta, covariance, variance_b2))
        channels = np.column_stack((score_variance, geometric,
                                    score_variance/geometric))
        runs.append((moments, channels))
    return runs, physical_v, value


def endpoint_source_channel_checks():
    """Separate sampled source variance and geometric curvature, kappa=1.

    Finite-difference and harmonic-cutoff refinements are separate.
    Positivity checks concern these resolved finite numerical values;
    a Galerkin truncation is not asserted to define a positive source
    measure. Both endpoint channels come from the actual full path
    generating law, not an independently chosen marginal clock.
    """
    steps = (.004, .002, .001)
    for coupling, coarse, fine in ((2., 10, 12), (16., 14, 16)):
        reports = [endpoint_source_channels(cutoff, coupling, .2, steps)
                   for cutoff in (coarse, fine)]
        for runs, physical_v, values in reports:
            for moments, channels in runs:
                assert np.min(moments[:, 1:4]) > 0
                assert np.min(moments[:, 5]) > 0
                assert np.min(channels[:, :2]) > 0
                assert np.max(channels[:, 2]) < 1
                assert np.min(moments[:, 3]*moments[:, 5]-moments[:, 4]**2) > 0
                source_radius = 2*coupling*.2
                assert np.max(np.abs(moments[:, 0])) < source_radius
                assert np.max(moments[:, 0]**2+moments[:, 3]+moments[:, 1]) < source_radius**2
                assert np.max(moments[:, 2]) < source_radius**4
            # Refinements, not the algebraic reconstruction equality,
            # test extraction of the two individual source channels.
            for earlier in runs[:-1]:
                close(earlier[0], runs[-1][0], rtol=3e-5, atol=3e-7)
                close(earlier[1], runs[-1][1], rtol=3e-5, atol=3e-7)
        for first, second in zip(reports[0][0], reports[1][0]):
            close(first[0], second[0], rtol=3e-5, atol=3e-7)
            close(first[1], second[1], rtol=3e-5, atol=3e-7)
        close(reports[0][1], reports[1][1], rtol=3e-8, atol=3e-9)
        runs, physical_v, values = reports[-1]
        fd_change = max(float(np.max(np.abs(row[1]-runs[-1][1]))) for row in runs[:-1])
        cutoff_change = max(float(np.max(np.abs(first[1]-second[1])))
                            for first, second in zip(reports[0][0], reports[1][0]))
        print(f"endpoint source channels lambda={coupling:g},t=.2, "
              f"cutoffs={coarse}/{fine}, a=(-1,+1): variance={runs[-1][1][:, 0]}, "
              f"geometric={runs[-1][1][:, 1]}, ratio={runs[-1][1][:, 2]}, "
              f"physical v={physical_v}; finite-difference change={fd_change:.3e}, "
              f"cutoff change={cutoff_change:.3e}, minimum generating value={values.min():.3e}")
    print("PASS separate endpoint source-channel samples with unnormalized, "
          "asymmetric full-operator evolution and radial-step/cutoff refinements. "
          "The reconstruction equality checks algebra, not a bound; no certified "
          "positive truncated source law, all-latitude inequality or gap is inferred.")


def late_endpoint_source_checks():
    """Resolved late-time channel cancellation, not an all-time estimate."""
    coupling, times, steps = 2., (2., 8.), (.002, .001)
    ground = ground_state(12, coupling)[0]
    multiplication = matrices(12)[3]
    # Exchange symmetry of the actual equal-coupling ground vector gives
    # <a>=<a+b>/2. No source-channel sample fixes this slope coefficient.
    d = coupling*float(ground@multiplication@ground)/2
    target = 8*d*d/3
    ground_jet = marginal_jet(ground, 12, np.array([-1., 1.]))
    ground_v = (ground_jet[2]/ground_jet[0]-(ground_jet[1]/ground_jet[0])**2)/2
    ratios, shape_errors, coefficient_errors = [], [], []
    print(f"late endpoint source ground d=lambda<a>={d:.12g}, "
          f"predicted common t^2 coefficient={target:.12g}, ground v={ground_v}")
    for duration in times:
        reports = [endpoint_source_channels(cutoff, coupling, duration, steps)
                   for cutoff in (10, 12)]
        for runs, _, _ in reports:
            close(runs[0][1], runs[1][1], rtol=5e-9, atol=3e-7)
            assert np.min(runs[-1][1][:, :2]) > 0
            assert np.all((runs[-1][1][:, 2] > 0)&(runs[-1][1][:, 2] < 1))
        channels, v = reports[-1][0][-1][1], reports[-1][1]
        close(reports[0][0][-1][1], channels, rtol=5e-9, atol=3e-7)
        close(reports[0][1], v, rtol=3e-8, atol=3e-9)
        ratios.append(channels[:, 2])
        shape_errors.append(np.abs(v-ground_v))
        coefficient_errors.append(float(np.max(np.abs(channels[:, :2]/duration**2-target))))
        fd_change = max(float(np.max(np.abs(report[0][0][1]-report[0][1][1])))
                        for report in reports)
        cutoff_change = float(np.max(np.abs(reports[0][0][-1][1]-channels)))
        print(f"  lambda=2,t={duration:g}, cutoffs=10/12, a=(-1,+1): "
              f"variance/t^2={channels[:, 0]/duration**2}, "
              f"geometric/t^2={channels[:, 1]/duration**2}, ratio={channels[:, 2]}, "
              f"v={v}; step change={fd_change:.3e}, cutoff change={cutoff_change:.3e}")
    assert np.all(ratios[1] > ratios[0])
    assert np.all(shape_errors[1] < shape_errors[0])
    assert coefficient_errors[1] < coefficient_errors[0]
    print("PASS two resolved late-time samples: the source/geometric ratio moves "
          "toward one while the finite negative curvature approaches the actual "
          "ground value. These samples test the analytic asymptotic, not an "
          "all-time limit, a positive Galerkin source law, or a uniform gap.")


def invariant_amplitude_jet(coefficients, cutoff, a, b, z):
    """Polynomial partial_a^i partial_z^j psi, i<=2,j<=4, with b,z fixed.

    Expand each Legendre channel before differentiation: its term of
    degree k-2l in z carries (1-a^2)^l(1-b^2)^l. Thus no radius or its
    inverse occurs, including at a=+/-1. These are invariant-coordinate
    derivatives, not the fixed-hidden-disk derivatives in evaluate().
    """
    def polynomial_jet(degree, parameter, nodes):
        table = np.zeros((3, len(nodes), degree+1))
        table[0, :, 0] = 1
        for n in range(1, degree+1):
            for order in range(3):
                first = nodes*table[order, :, n-1]
                if order:
                    first = first+order*table[order-1, :, n-1]
                previous = table[order, :, n-2] if n > 1 else 0.
                table[order, :, n] = (2*(n+parameter-1)*first
                                      -(n+2*parameter-2)*previous)/n
        return table

    lookup = {label: index for index, label in enumerate(labels(cutoff))}
    ha, hb = 1-a*a, 1-b*b
    result = np.zeros((3, 5, *z.shape))
    for k in range(cutoff+1):
        degree = cutoff-k
        table_a = polynomial_jet(degree, k+1, a)
        table_b = polynomial_jet(degree, k+1, b)[0]
        norms = np.array([math.factorial(n+2*k+1)
                          /(4**k*math.factorial(n)*(n+k+1)*math.factorial(k)**2)
                          for n in range(degree+1)])
        block = np.array([[coefficients[lookup[n, m, k]] for m in range(k, cutoff+1)]
                          for n in range(k, cutoff+1)])
        block /= np.sqrt(norms[:, None]*norms[None, :])
        for ell in range(k//2+1):
            power = k-2*ell
            legendre_coefficient = ((-1)**ell*math.factorial(2*k-2*ell)
                                    /(2**k*math.factorial(ell)*math.factorial(k-ell)
                                      *math.factorial(power)))
            ha_jet = np.zeros((3, len(a)))
            ha_jet[0] = ha**ell
            if ell:
                ha_jet[1] = -2*ell*a*ha**(ell-1)
                ha_jet[2] = -2*ell*ha**(ell-1)
            if ell >= 2:
                ha_jet[2] += 4*ell*(ell-1)*a*a*ha**(ell-2)
            for order_a in range(3):
                retained = sum(math.comb(order_a, j)*ha_jet[j, :, None]*table_a[order_a-j]
                               for j in range(order_a+1))
                value = (math.sqrt(2*k+1)*legendre_coefficient
                         *(retained@block@table_b.T)*hb[None, :]**ell)
                for order_z in range(min(power, 4)+1):
                    factor = math.factorial(power)/math.factorial(power-order_z)
                    result[order_a, order_z] += value[:, :, None]*factor*z**(power-order_z)
    return result


def regular_disk_density_integrals(a, b, u, hidden_weights, density_jet):
    """R,R',R'' from hidden-disk integration by parts; no singular 1/h."""
    density, da, daa, dzz, dazz, dzzzz = density_jet
    aa = a[:, None, None]
    slack = (1-b*b)[None, :, None]*(1-u*u)[None, None, :]
    integrands = (density, da-aa*slack*dzz/2,
                  daa-aa*slack*dazz-slack*dzz/2+aa*aa*slack*slack*dzzzz/8)
    return np.array([np.sum(hidden_weights*row, axis=(1, 2)) for row in integrands])


def regular_conditional_hessian_checks():
    # F=1+epsilon*z^4 shares every invariant derivative through order
    # three at z=0 with the flat density. Its endpoint marginal log-
    # Hessian nevertheless equals epsilon/2, owing to the fourth jet.
    a = np.array([-1., -.5, 0., .5, .9, .9999, 1.])
    b, wb, u, wu = quadrature(36, 32)
    z = np.sqrt(1-a*a)[:, None, None]*np.sqrt(1-b*b)[None, :, None]*u[None, None, :]
    hidden_weights = wb[None, :, None]*wu[None, None, :]
    epsilon = .2
    zero = np.zeros_like(z)
    density_polynomial = np.polynomial.Polynomial([1., 0., 0., 0., epsilon])
    for derivative in range(4):
        close(density_polynomial.deriv(derivative)(0.), 1. if derivative == 0 else 0.)
    polynomial = regular_disk_density_integrals(a, b, u, hidden_weights,
        (density_polynomial(z), zero, zero, density_polynomial.deriv(2)(z),
         zero, density_polynomial.deriv(4)(z)))
    expected = np.array([1+epsilon*(1-a*a)**2/8,
                         -epsilon*a*(1-a*a)/2, epsilon*(3*a*a-1)/2])
    close(polynomial, expected)
    endpoint_log_second = (polynomial[2]/polynomial[0]
                           -(polynomial[1]/polynomial[0])**2)/2
    close(endpoint_log_second[[0, -1]], np.full(2, epsilon/2))

    # One actual full-carrier heat member, three independent cutoff /
    # hidden-quadrature combinations. Endpoint and nearby cancellation
    # checks use the same coefficients but different derivative paths.
    states = {cutoff: haar_amplitude_evolution(cutoff, 16., [.2])[0][0]
              for cutoff in (14, 16)}
    runs = []
    identity_errors = []
    cancellation_indices = np.array([4, 5])
    for cutoff, order, angular in ((14, 24, 20), (16, 24, 20), (16, 36, 32)):
        coefficients = states[cutoff]
        b, wb, u, wu = quadrature(order, angular)
        aa = a[:, None, None]
        h = 1-aa*aa
        eta = np.sqrt(1-b*b)[None, :, None]*u[None, None, :]
        z = np.sqrt(h)*eta
        hidden_weights = wb[None, :, None]*wu[None, None, :]
        jet = invariant_amplitude_jet(coefficients, cutoff, a, b, z)
        psi, pa, paa = jet[0, 0], jet[1, 0], jet[2, 0]
        pz, pzz, pzzz, pzzzz = (jet[0, j] for j in range(1, 5))
        paz, pazz = jet[1, 1], jet[1, 2]
        assert np.min(psi) > 0
        density_jet = (psi*psi, 2*psi*pa, 2*(pa*pa+psi*paa),
                       2*(pz*pz+psi*pzz), 4*pz*paz+2*pa*pzz+2*psi*pazz,
                       2*psi*pzzzz+8*pz*pzzz+6*pzz*pzz)
        regular = regular_disk_density_integrals(a, b, u, hidden_weights, density_jet)
        independent = marginal_jet(coefficients, cutoff, a)[:3]
        close(regular, independent, rtol=3e-10, atol=5e-11)
        identity_errors.append(float(np.max(np.abs(regular-independent))))
        idx = cancellation_indices
        ad, hd, ed = aa[idx], h[idx], np.broadcast_to(eta, z.shape)[idx]
        disk_first = pa[idx]-ad*ed*pz[idx]/np.sqrt(hd)
        disk_second = (paa[idx]-2*ad*ed*paz[idx]/np.sqrt(hd)
                       +ad*ad*ed*ed*pzz[idx]/hd-ed*pz[idx]/hd**1.5)
        # Independent original fixed-u radial derivatives check the
        # first derivative and the polynomial expansion itself.
        radial_psi, radial_da, _, _ = evaluate(coefficients, cutoff, a[idx], b, u)
        close(psi[idx], radial_psi)
        close(disk_first, radial_da, rtol=3e-10, atol=5e-11)
        score = disk_first/psi[idx]
        hessian = disk_second/psi[idx]-score*score
        weights = hidden_weights*psi[idx]**2/regular[0, idx, None, None]
        mean_score = np.sum(weights*score, axis=(1, 2))
        twice_variance = 2*np.sum(weights*(score-mean_score[:, None, None])**2, axis=(1, 2))
        mean_hessian = np.sum(weights*hessian, axis=(1, 2))
        marginal_v = (independent[2]/independent[0]
                      -(independent[1]/independent[0])**2)/2
        close(mean_hessian+twice_variance, marginal_v[idx], rtol=3e-9, atol=3e-10)
        assert np.all(np.max(hessian, axis=(1, 2)) > 0)
        runs.append((regular, mean_hessian, twice_variance, marginal_v[idx]))
    for old in runs[:-1]:
        for index in range(4):
            close(old[index], runs[-1][index], rtol=3e-9, atol=5e-10)
    _, mean_hessian, twice_variance, marginal_v = runs[-1]
    print(f"regular conditional Hessian lambda=16,t=.2 at a={a[cancellation_indices]}: "
          f"mean phi_aa={mean_hessian}, 2Var(phi_a)={twice_variance}, sum={marginal_v}")
    print(f"  regular R,R',R'' versus independent jets: max error={max(identity_errors):.3e}; "
          f"cutoff change={np.max(np.abs(runs[0][0]-runs[1][0])):.3e}, "
          f"hidden-quadrature change={np.max(np.abs(runs[1][0]-runs[2][0])):.3e}")
    print("PASS regular density jets against independent harmonic marginal jets, including "
          "both endpoints; resolved hidden-quadrature/cutoff cancellation despite positive "
          "pointwise log-Hessians. F=1+epsilon*z^4 has the same invariant jets through "
          "order three at z=0 as F=1 but endpoint v=epsilon/2. These are finite polynomial "
          "identities and prepared-state diagnostics, not a new sign or gap theorem.")


def joined_class_readout_checks():
    # P_ab retains EVERY k=0 label in this full invariant cutoff, not
    # just one product character. The omitted relative channels are k>0.
    basis, lookup, kinetic, _ = matrices(8)
    retained_indices = [index for index, (_, _, k) in enumerate(basis) if k == 0]
    hidden_indices = [index for index, (_, _, k) in enumerate(basis) if k > 0]
    retained = kinetic[np.ix_(retained_indices, retained_indices)]
    cross = kinetic[np.ix_(hidden_indices, retained_indices)]
    hidden_squared = cross.T@cross
    second_order_bound = retained@retained/48
    assert np.linalg.eigvalsh(second_order_bound-hidden_squared)[0] >= -2e-10
    ratios = []
    for n in (1, 2, 4, 8):
        index = retained_indices.index(lookup[n, n, 0])
        column = cross[:, index]
        actual = float(column@column/retained[index, index])
        close(actual, n*(n+2)/24)
        close(hidden_squared[index, index], second_order_bound[index, index])
        ratios.append(f"n={n}: {actual:.12g}")
    print("PASS Haar joined class algebra: all 81 k=0 modes versus 204 relative "
          "channels, B*B <= A_ab^2/48 with equality on diagonal n=m; "
          "||B F_n||^2/a[F_n] = " + ", ".join(ratios) + ". "
          "These finite checks support the second-order estimate; absence of an "
          "all-degree first-order form bound follows from the analytic n->infinity argument.")


def one_plaquette_ground(cutoff, coupling):
    degrees = np.arange(cutoff+1)
    hamiltonian = (np.diag(degrees*(degrees+2)+coupling)
                   -coupling*(np.diag(np.ones(cutoff), 1)
                              +np.diag(np.ones(cutoff), -1))/2)
    energies, vectors = np.linalg.eigh(hamiltonian)
    coefficients = vectors[:, 0].copy()
    if coefficients[0] < 0:
        coefficients *= -1
    return coefficients, float(energies[0])


def score_energy_diagnostic(cutoff, coupling, order):
    coefficients, _ = one_plaquette_ground(cutoff, coupling)
    q, weights, _, _ = quadrature(order, 2)
    values, slopes = radial_tables(cutoff, 0, q)
    degrees = np.arange(cutoff+1)
    h = 1-q*q
    # Character differential identity, NOT the ground-state equation:
    # (1-q^2) C_n'' - 3q C_n' + n(n+2) C_n = 0.
    curvatures = (3*q[:, None]*slopes-values*(degrees*(degrees+2)))/h[:, None]
    phi, slope, curvature = values@coefficients, slopes@coefficients, curvatures@coefficients
    assert np.min(phi) > 0
    density = phi*phi
    close(weights@density, 1.)
    first = slope/phi
    second = curvature/phi-first*first
    # Neutral quotient density in theta=arccos(q) is sin(theta)^2 phi^2.
    # This is NOT the raw weighted Ricci tensor tested above. Positivity
    # for the exact state is proved by the one-dimensional Riccati argument;
    # this finite Galerkin sample is only an independent diagnostic.
    quotient_curvature = 2/h+2*q*first-2*h*second
    assert np.all(quotient_curvature > 0)
    # Raw four-link energy of ONE charged endpoint score -u'(q)b_a/2.
    # Angular average b_a^2=(1-q^2)/3; each link contributes the same
    # SU2 gradient norm under the based-holonomy map. kappa=1 here.
    energy = float(weights@(density*((h*second-q*first)**2+2*first*first)))/12
    covariance = float(weights@(density*h*first*first))/12
    force_hessian = coupling*float(weights@(density*q))/8
    close(energy, force_hessian, rtol=2e-8, atol=3e-12)
    # Vertex degree two, adjoint Casimir two: a charged-sector lower
    # bound, not a bound on neutral physical excitations.
    assert covariance <= energy+3e-12
    return np.array([energy, covariance, force_hessian])


def score_energy_checks():
    for coupling in (.5, 1., 4.):
        runs = [score_energy_diagnostic(cutoff, coupling, order)
                for cutoff, order in ((12, 32), (16, 32), (16, 48))]
        for earlier in runs[:-1]:
            close(earlier, runs[-1], rtol=2e-8, atol=3e-12)
        energy, covariance, hessian = runs[-1]
        print(f"charged plaquette score lambda={coupling:g}: energy={energy:.12g}, "
              f"covariance={covariance:.12g}, lambda<q>/8={hessian:.12g}")
    print("PASS independent character-derivative energy and force-Hessian sum rule. "
          "The probe is gauge charged on the raw carrier; its control is not a neutral mass gap. "
          "The separate invariant-quotient curvature samples are positive.")


def character_jet(cutoff, retained):
    """U_n and its first two latitude derivatives, with regular endpoints."""
    retained = np.asarray(retained, dtype=float)
    jet = np.zeros((3, len(retained), cutoff+1))
    jet[0, :, 0] = 1
    for n in range(1, cutoff+1):
        for derivative in range(3):
            first = retained*jet[derivative, :, n-1]
            if derivative:
                first = first+derivative*jet[derivative-1, :, n-1]
            previous = jet[derivative, :, n-2] if n > 1 else 0.
            jet[derivative, :, n] = 2*first-previous
    return jet


def scalar_latitude_checks():
    """Single-plaquette reference only: QB5-QB7, not a coupled-marginal proof."""
    grid = np.linspace(-1., 1., 1001)
    times = (0., .01, .1, .5, 2.)
    for coupling in (0., .5, 4., 16.):
        runs = []
        for cutoff in (20, 28):
            degrees = np.arange(cutoff+1)
            matrix = (np.diag(degrees*(degrees+2)+coupling)
                      -coupling*(np.diag(np.ones(cutoff), 1)
                                 +np.diag(np.ones(cutoff), -1))/2)
            energies, vectors = np.linalg.eigh(matrix)
            jet = character_jet(cutoff, grid)
            # Exact endpoint character formulas independently check the
            # recurrence; no division by 1-a^2 produces these derivatives.
            endpoint = character_jet(cutoff, np.array([-1., 1.]))
            for index, sign in enumerate((-1., 1.)):
                close(endpoint[0, index], sign**degrees*(degrees+1))
                close(endpoint[1, index], sign**(degrees+1)*degrees*(degrees+1)*(degrees+2)/3)
                close(endpoint[2, index], sign**degrees*(degrees-1)*degrees*(degrees+1)
                      *(degrees+2)*(degrees+3)/15)
            ground = vectors[:, 0].copy()
            if ground[0] < 0:
                ground *= -1
            close(ground, one_plaquette_ground(cutoff, coupling)[0], atol=2e-12)
            states = []
            for duration in times:
                if duration == 0 or coupling == 0:
                    coefficients = np.zeros(cutoff+1)
                    coefficients[0] = 1
                else:
                    coefficients = vectors@(np.exp(-duration*(energies-energies[0]))*vectors[0])
                    coefficients /= np.linalg.norm(coefficients)
                states.append(coefficients)
            states.append(ground)
            values = np.array([jet@coefficients for coefficients in states])
            amplitude, first, second = values[:, 0], values[:, 1], values[:, 2]
            assert np.min(amplitude) > 0
            log_second = second/amplitude-(first/amplitude)**2
            assert np.max(log_second) <= 5e-9
            gap = float(energies[1]-energies[0])
            assert gap >= 1-3e-12
            runs.append((amplitude, log_second, gap))
        close(runs[0][0], runs[1][0], rtol=2e-8, atol=3e-12)
        close(runs[0][1], runs[1][1], rtol=2e-8, atol=2e-7)
        close(runs[0][2], runs[1][2], atol=2e-11)
        log_second, gap = runs[-1][1:]
        print(f"scalar latitude lambda={coupling:g}, cutoffs=20/28: "
              f"positive-time max(log f)aa={log_second[1:-1].max():.12g}, "
              f"ground range=[{log_second[-1].min():.12g},{log_second[-1].max():.12g}], "
              f"neutral eigenvalue difference={gap:.12g}; "
              f"max log-second cutoff change={np.max(np.abs(runs[0][1]-log_second)):.3e}")
    print("PASS scalar reference latitude jets for heat from one and the actual "
          "single-plaquette ground operator, including analytic endpoints and the "
          "Haar gap-three control. Sampled concavity and converged eigenvalue "
          "differences support QB5-QB7/LT9-LT10; the all-coupling gap-at-least-one "
          "statement is the analytic theorem, not a Galerkin certificate or a "
          "many-plaquette marginal conclusion.")


def cut_vacuum_diagnostic(cutoff, coupling, order, angular):
    """A=left four edges; B=right three outer edges, with no duplication.

    The decoupled raw vacuum is phi(a) times the constant tree vacuum,
    NOT phi(a)phi(b). B's raw tree marginal is Haar by gauge invariance;
    b itself is a loop involving A's shared edge and is not Haar-distributed.
    """
    coefficients, energy, _, _ = ground_state(cutoff, coupling)
    degrees = np.arange(cutoff+1)
    decoupled, decoupled_energy = one_plaquette_ground(cutoff, coupling)
    # Exact character endpoint formulas avoid taking a singular radial
    # coordinate limit numerically. Here the supplied kappa is one.
    signs = (-1.)**degrees
    endpoint_value = float(decoupled@(signs*(degrees+1)))
    endpoint_slope = float(decoupled@(-signs*degrees*(degrees+1)*(degrees+2)/3))
    assert endpoint_value > 0
    endpoint_ratio = endpoint_slope/endpoint_value
    close(endpoint_ratio, (2*coupling-decoupled_energy)/3, rtol=3e-8, atol=1e-11)
    # A coherent four-link UNIT product-metric tangent has q(t)=-cos(t).
    # Hence Hess log(phi)[v,v]=phi'(-1)/phi(-1), whereas raw Ric[v,v]=1/2.
    weighted_curvature = .5-2*endpoint_ratio
    if coupling == 1.:
        assert weighted_curvature < 0
    a, wa, angle, wu = quadrature(order, angular)
    characters, slopes = radial_tables(cutoff, 0, a)
    phi, phi_slope = characters@decoupled, slopes@decoupled
    assert np.min(phi) > 0
    close(wa@(phi*phi), 1)
    reference_score = phi_slope/phi
    psi, da, db, du = evaluate(coefficients, cutoff, a, a, angle)
    assert np.min(psi) > 0
    aa, bb, uu = a[:, None, None], a[None, :, None], angle[None, None, :]
    rx, ry = np.sqrt(1-aa*aa), np.sqrt(1-bb*bb)
    z = rx*ry*uu
    conditional_weights = wa[None, :, None]*wu[None, None, :]
    weights = wa[:, None, None]*conditional_weights
    density = psi*psi
    mean_b = float(np.sum(weights*density*bb))
    reference_mean_b = float(np.sum(weights*phi[:, None, None]**2*bb))
    close(reference_mean_b, 0.)
    relative_from_energy = energy-coupling+coupling*mean_b-decoupled_energy
    lowering = decoupled_energy+coupling-energy
    close(relative_from_energy+lowering, coupling*mean_b)
    assert 0 < relative_from_energy < coupling and 0 < lowering < coupling

    # Actual full seven-edge cometric on invariant coordinates (a,b,z).
    gradient = np.stack(np.broadcast_arrays(da+aa*uu*du/(1-aa*aa),
                                           db+bb*uu*du/(1-bb*bb), du/(rx*ry)), axis=-1)
    metric = coordinate_metric(aa, bb, z)
    relative_gradient = gradient.copy()
    relative_gradient[..., 0] -= psi*reference_score[:, None, None]

    def integrated_form(tangent, tensor):
        return float(np.sum(weights*np.einsum("...i,...ij,...j->...", tangent, tensor, tangent)))

    relative_integral = integrated_form(relative_gradient, metric)
    close(relative_integral, relative_from_energy, rtol=2e-8, atol=3e-12)
    # Independent finite-matrix H_dec expectation, retaining all k channels.
    basis, lookup, kinetic, _ = matrices(cutoff)
    multiplier_a = np.zeros_like(kinetic)
    for index, (n, m, k) in enumerate(basis):
        if n < cutoff:
            other = lookup[n+1, m, k]
            multiplier_a[index, other] = multiplier_a[other, index] = raising(n, k)
    decoupled_full = kinetic+coupling*(np.eye(len(basis))-multiplier_a)
    direct_energy = float(coefficients@decoupled_full@coefficients-decoupled_energy)
    close(direct_energy, relative_integral, rtol=2e-8, atol=3e-12)

    # B consists of three raw outer links, so its partial form is 3 D_y.
    partial_b = np.zeros_like(metric)
    partial_b[..., 1, 1] = 3*(1-bb*bb)/4
    partial_b[..., 1, 2] = partial_b[..., 2, 1] = -3*bb*z/4
    partial_b[..., 2, 2] = 3*((1-aa*aa)-z*z)/4
    information_b = integrated_form(gradient, partial_b)
    information_a_total = integrated_form(gradient, metric-partial_b)
    marginal_a = np.sum(density*conditional_weights, axis=(1, 2))
    marginal_slope = np.sum(2*psi*da*conditional_weights, axis=(1, 2))/marginal_a
    marginal_half_score = marginal_slope/2
    marginal_a_information = float(wa@((1-a*a)*marginal_half_score**2*marginal_a))
    mismatch_a = float(wa@((1-a*a)*(marginal_half_score-reference_score)**2*marginal_a))
    mismatch_b = 0.  # Exact raw-tree Haar marginal, not the b-loop marginal.
    information_a = information_a_total-marginal_a_information
    assert mismatch_a > 0 and information_a > 0 and information_b > 0
    close(relative_integral, mismatch_a+mismatch_b+information_a+information_b,
          rtol=2e-8, atol=3e-12)
    return np.array([decoupled_energy, relative_integral, lowering, coupling*mean_b,
                     mismatch_a, mismatch_b, information_a, information_b,
                     endpoint_ratio, weighted_curvature])


def cut_vacuum_checks():
    for coupling in (.5, 1.):
        runs = [cut_vacuum_diagnostic(cutoff, coupling, order, angular)
                for cutoff, order, angular in ((6, 24, 20), (8, 24, 20), (8, 36, 32))]
        for earlier in runs[:-1]:
            close(earlier, runs[-1], rtol=2e-8, atol=4e-12)
        energy, relative, lowering, budget, da, db, ja, jb, ratio, curvature = runs[-1]
        print(f"raw-edge cut lambda={coupling:g}: E_dec={energy:.12g}, "
              f"R={relative:.12g}, delta={lowering:.12g}, "
              f"lambda<q_cross>={budget:.12g}; "
              f"(D_A,D_B,J_A,J_B)=({da:.12g},{db:g},{ja:.12g},{jb:.12g})")
        print(f"  reference endpoint q=-1: phi'/phi={ratio:.12g}, "
              f"coherent four-link weighted Ricci={curvature:.12g}")
    print("PASS true raw-edge cut: full-state relative half-density Fisher integral "
          "matches both energy differences and the marginal/conditional score decomposition. "
          "No shared edge or boundary-charge sector was duplicated or discarded. "
          "Standard density Fisher is four times this half-density convention; "
          "positivity and numerical convergence here remain finite diagnostics.")


def main():
    print("two-plaquette vacuum receipt: specified physical kappa=1, full invariant carrier")
    basis_and_operator_checks()
    small_ratios = []
    for coupling in (.02, .1, .5, 1.):
        runs = []
        for cutoff in (2, 4, 6, 8):
            coefficients, energy, residual, z_coefficient = ground_state(cutoff, coupling)
            diagnostic = memory(coefficients, cutoff, 32, 28)
            runs.append((cutoff, coefficients, energy, residual, z_coefficient, diagnostic))
        final = runs[-1]
        close(runs[-2][2], final[2], atol=2e-12)
        close(runs[-2][5][:2], final[5][:2], rtol=2e-8, atol=3e-12)
        assert final[3] < 2e-11
        refined = [memory(final[1], final[0], order, angular)
                   for order, angular in ((20, 16), (28, 24), (40, 36))]
        close(np.array([row[:2] for row in refined]), np.broadcast_to(refined[-1][:2], (3, 2)),
              rtol=2e-8, atol=4e-12)
        d = refined[-1][0]
        print(f"lambda={coupling:g}:")
        for cutoff, _, energy, residual, _, diagnostic in runs:
            print(f"  cutoff={cutoff}, modes={len(labels(cutoff))}: E0={energy:.12g}, "
                  f"full residual={residual:.3e}, conditional memory={diagnostic[0]:.12g}")
        print(f"  D/lambda^2={d/(coupling*coupling):.12g}, <chi_x>={refined[-1][1]:.12g}, "
              f"z-harmonic polynomial coefficient/lambda^2={final[4]/(coupling*coupling):.12g}")
        if coupling <= .1:
            small_ratios.append((coupling, d/(coupling*coupling), final[4]/(coupling*coupling)))
    assert abs(small_ratios[0][1]-1/48) < abs(small_ratios[1][1]-1/48)
    assert abs(small_ratios[0][1]-1/48) < 5e-6
    assert abs(small_ratios[0][2]-4/351) < 5e-6
    print("PASS independently refined positive quadratures condition on the ENTIRE "
          "one-plaquette class variable a, integrating both b and relative angle; "
          "small coupling approaches D/lambda^2=1/48 and z coefficient=4/351. "
          "The lambda=.5,1 values use the computed joint vacuum, not that leading expansion.")
    fixed_time_checks()
    all_readout_checks()
    neutral_shape_checks()
    marginal_shape_checks()
    evolution_shape_checks()
    weak_coupling_evolution_checks()
    short_layer_coefficient_checks()
    positive_kernel_initial_state_checks()
    relative_replica_checks()
    endpoint_source_channel_checks()
    late_endpoint_source_checks()
    regular_conditional_hessian_checks()
    marginal_stress_checks()
    joined_class_readout_checks()
    cut_vacuum_checks()
    score_energy_checks()
    scalar_latitude_checks()
    print("Finite Galerkin residual and quadrature diagnostics only. No uniform remainder, "
          "infinite-volume vacuum, long-time decay bound or Yang--Mills gap certified.")


if __name__ == "__main__":
    main()
