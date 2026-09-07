"""Read-only finite calibrations and SU(2) differential checks of the slab.

These enumerate finite path laws, covariance/influence and complete bridges.
Quaternion differences and Haar quadrature additionally test the ramp score.
The compact SU(2) gradient theorem is proved in the note, not by these samples.
"""
import itertools
import math
from fractions import Fraction
import numpy as np


def close(a, b, tol=3e-10):
    assert np.max(np.abs(np.asarray(a)-np.asarray(b))) < tol


def psd(a, tol=3e-10):
    assert np.linalg.eigvalsh((a+a.T)/2)[0] > -tol


def spin_states(n):
    # Coordinate i corresponds to binary bit i.
    idx = np.arange(2**n)
    return 2*((idx[:, None] >> np.arange(n)) & 1)-1


def slabs():
    count = 0
    rng = np.random.default_rng(3114)
    for x, beta in itertools.product([0.05, 0.15, 0.25], [0.01, 0.03]):
        q = 2*math.tanh(x)+6*math.tanh(beta)  # d_s=2 regular-lattice majorant
        assert q < 1
        for depth in [1, 2, 3]:
            states = spin_states(4*depth)
            history = states.reshape(-1, depth, 4)
            idx = np.arange(len(states))
            c = np.zeros((4*depth, 4*depth))
            for i in range(4*depth):
                for j in range(4*depth):
                    ti, ei = divmod(i, 4)
                    tj, ej = divmod(j, 4)
                    if ti == tj and ei != ej:
                        c[i, j] = math.tanh(beta)
                    if ei == ej and abs(ti-tj) == 1:
                        c[i, j] = math.tanh(x)
            resolvent = np.linalg.inv(np.eye(len(c))-c)
            for fixed in [np.ones(4), np.array([1, -1, 1, 1])]:
                logw = x*(history[:, 0]@fixed)
                if depth > 1:
                    logw += x*np.sum(history[:, :-1]*history[:, 1:], axis=(1, 2))
                    logw += beta*np.sum(np.prod(history[:, :-1], axis=2), axis=1)
                logw += beta*np.prod(history[:, -1], axis=1)/2
                law = np.exp(logw-logw.max())
                law /= law.sum()
                means = law@states
                cov = states.T@(law[:, None]*states)-np.outer(means, means)
                assert np.max(np.abs(cov)-resolvent) < 3e-10
                # Fisher response to the real external source u in exp(x*u.Y_1):
                # I(u)=x^2 Cov(Y_1), not a tangent derivative on discrete Z2.
                psd(np.eye(4)/(1-q)-cov[:4, :4])
                pplus = []
                for i in range(4*depth):
                    plus = idx | (1 << i)
                    minus = idx & ~(1 << i)
                    pplus.append(law[plus]/(law[plus]+law[minus]))
                for i in range(4*depth):
                    for j in range(4*depth):
                        actual = np.max(np.abs(pplus[i]-pplus[i][idx ^ (1 << j)]))
                        assert actual <= c[i, j]+2e-12
                # Nonlinear cylinder functions, with exact per-site oscillations.
                f = states[:, 0]*states[:, min(5, states.shape[1]-1)]
                g = np.tanh(states@rng.normal(size=states.shape[1]))
                df = np.array([np.max(np.abs(f-f[idx ^ (1 << i)])) for i in range(states.shape[1])])
                dg = np.array([np.max(np.abs(g-g[idx ^ (1 << i)])) for i in range(states.shape[1])])
                covariance = law@(f*g)-(law@f)*(law@g)
                assert abs(covariance) <= df@resolvent@dg/4+2e-12
                count += 1
    print(f"PASS {count} exact finite slabs: conditional TV, covariance resolvent and joint-score bounds")


def bridges():
    states = spin_states(4)
    parity = (np.prod(states, axis=1)+1)//2
    count = 0
    for x, beta in itertools.product([0.05, 0.15, 0.25], [0.01, 0.03]):
        k = np.exp(x*states@states.T)/(2*math.cosh(x))**4
        a = np.exp(beta*np.prod(states, axis=1)/2)
        t = a[:, None]*k*a[None, :]
        w, v = np.linalg.eigh(t)
        psi = v[:, -1]
        if psi.sum() < 0:
            psi = -psi
        assert psi.min() > 0 and w.min() > 0
        nu = psi**2
        p = t*psi[None, :]/(w[-1]*psi[:, None])
        close(nu@p, nu)
        endpoint = nu[:, None]*(p@p)
        joint_given_mid = p[:, :, None]*p[:, None, :]
        analysis = (np.sqrt(nu)[:, None, None]*joint_given_mid/np.sqrt(endpoint)[None, :, :]).reshape(16, 256).T
        s = analysis.T@analysis
        ph = np.sqrt(nu)[:, None]*p/np.sqrt(nu)[None, :]
        psd(s-ph@ph)
        psd(np.eye(16)-s)
        close(s@psi, psi)
        orbitlaw = np.bincount(parity, weights=nu, minlength=2)
        jmid = np.zeros((16, 2))
        jmid[np.arange(16), parity] = np.sqrt(nu/orbitlaw[parity])
        endpoint_parity = (2*parity[:, None]+parity[None, :]).reshape(-1)
        endflat = endpoint.reshape(-1)
        end_orbitlaw = np.bincount(endpoint_parity, weights=endflat, minlength=4)
        jend = np.zeros((256, 4))
        jend[np.arange(256), endpoint_parity] = np.sqrt(endflat/end_orbitlaw[endpoint_parity])
        abar = jend.T@analysis@jmid
        sbar = abar.T@abar
        pbar = jmid.T@ph@jmid
        psd(sbar-pbar@pbar)
        psd(jmid.T@s@jmid-sbar)
        raw_return = np.linalg.eigvalsh(s-np.outer(psi, psi))[-1]
        vbar = np.sqrt(orbitlaw)
        quotient_return = np.linalg.eigvalsh(sbar-np.outer(vbar, vbar))[-1]
        assert quotient_return <= raw_return+2e-12 < 1
        if x == 0.25 and beta == 0.03:
            assert np.ptp(psi) > 1e-3
            assert quotient_return > 1e-6
            assert np.linalg.norm(jmid.T@s@jmid-sbar) > 1e-6
            assert np.linalg.norm(sbar-pbar@pbar) > 1e-6
        count += 1
    print(f"PASS {count} complete interacting bridge and separate endpoint gauge-quotient matrices")


def su2_constants():
    count = 0
    for ds, x, beta in itertools.product([2, 3, 4], [0.01, 0.1, 0.2], [0.001, 0.005, 0.01]):
        q = 2*math.tanh(x)+6*(ds-1)*math.tanh(beta)
        assert q < 1
        d0 = 4*beta*(ds-1)+4*x
        lam = 3*math.exp(-d0)*(1-q)
        fisher = 2*x*x/(1-q)
        kappa = lam/(lam+fisher)
        close(kappa, 3*math.exp(-d0)*(1-q)**2/(3*math.exp(-d0)*(1-q)**2+2*x*x))
        assert 0 < kappa < 1
        rate = -math.log1p(-kappa)/2
        assert rate > 0 and abs(math.exp(-2*rate)-(1-kappa)) < 1e-12
        count += 1
    # The sufficient condition fails during temporal refinement even at beta=0.
    assert 2*math.tanh(10) > 1
    print(f"PASS {count} SU(2) certificate arithmetic cases and the temporal-refinement failure check")


def quaternion_product(a, b):
    """Hamilton product, with arbitrary broadcasting before the last axis."""
    a, b = np.asarray(a), np.asarray(b)
    scalar = a[..., :1]*b[..., :1]-np.sum(a[..., 1:]*b[..., 1:], axis=-1, keepdims=True)
    vector = (a[..., :1]*b[..., 1:]+b[..., :1]*a[..., 1:]
              + np.cross(a[..., 1:], b[..., 1:]))
    return np.concatenate((scalar, vector), axis=-1)


def quaternion_inverse(a):
    # Only unit quaternions enter this inverse; Lie tangents are not inverted.
    return np.asarray(a)*np.array([1.0, -1.0, -1.0, -1.0])


def quaternion_exponential(vector):
    angle = np.linalg.norm(vector, axis=-1, keepdims=True)
    return np.concatenate((np.cos(angle), np.sinc(angle/math.pi)*vector), axis=-1)


def oriented_box_faces(extents):
    """Actual oriented plaquettes, retaining shared-link incidence."""
    vertices = list(itertools.product(*(range(n+1) for n in extents)))
    edges = {(v, axis): ei for ei, (v, axis) in enumerate(
        (v, axis) for v in vertices for axis, n in enumerate(extents) if v[axis] < n)}
    faces = []
    for v in vertices:
        for a in range(len(extents)):
            for b in range(a+1, len(extents)):
                if v[a] >= extents[a] or v[b] >= extents[b]:
                    continue
                va, vb = list(v), list(v)
                va[a] += 1
                vb[b] += 1
                faces.append(((edges[(v, a)], 1), (edges[(tuple(va), b)], 1),
                              (edges[(tuple(vb), a)], -1), (edges[(v, b)], -1)))
    incidence = np.zeros((len(edges), len(edges)), dtype=int)
    for face in faces:
        indices = [edge for edge, _ in face]
        assert len(set(indices)) == 4
        incidence[np.ix_(indices, indices)] += 1
    assert np.max(incidence.sum(axis=1)) <= 8*(len(extents)-1)
    close(incidence, incidence.T)
    return len(edges), faces, incidence


def wilson_potential_and_derivative(links, tangents, faces):
    """Differentiate each oriented factor, including all neighboring tangents.

    tangents[e] is the actual ambient derivative dU_e, not its Lie coordinate.
    Inverse edges use d(U^-1)=-U^-1(dU)U^-1. No commuting-link simplification
    and no gauge fixing are made in this calculation.
    """
    shape = links.shape[:-2]
    potential, derivative = np.zeros(shape), np.zeros(shape)
    for face in faces:
        product = np.zeros(shape+(4,))
        product[..., 0] = 1
        differential = np.zeros_like(product)
        for edge, sign in face:
            factor, dfactor = links[..., edge, :], tangents[..., edge, :]
            if sign < 0:
                factor = quaternion_inverse(factor)
                dfactor = -quaternion_product(quaternion_product(factor, dfactor), factor)
            differential = (quaternion_product(differential, factor)
                            + quaternion_product(product, dfactor))
            product = quaternion_product(product, factor)
        potential += 1-product[..., 0]
        derivative -= differential[..., 0]
    return potential, derivative


def su2_ramp_differentiation():
    """Deterministic noncommuting histories; not samples of a Wilson law."""
    cases, mixed_cases = 0, 0
    max_difference = 0.0
    for seed, extents, m in itertools.product(
            (821, 7331), ((2, 1), (1, 1, 1), (2, 1, 1)), (1, 2, 4, 7)):
        rng = np.random.default_rng(seed+13*m)
        edge_count, faces, incidence = oriented_box_faces(extents)
        n, final = 2*m, 2*m+2
        links = rng.normal(size=(final+1, edge_count, 4))
        links /= np.linalg.norm(links, axis=-1, keepdims=True)
        v = rng.normal(size=(edge_count, 3))
        v /= np.linalg.norm(v, axis=-1, keepdims=True)
        v *= rng.uniform(0.2, 1.7, size=(edge_count, 1))
        v[0] = 0
        algebra_v = np.concatenate((np.zeros((edge_count, 1)), v), axis=-1)
        square = quaternion_product(algebra_v, algebra_v)
        close(square[:, 0], -np.sum(v*v, axis=1))
        close(square[:, 1:], 0.0)
        h = np.maximum(1-np.arange(final+1)/m, 0.0)
        close(2*np.sum(h[1:m]), m-1)
        tangent = h[:, None, None]*quaternion_product(algebra_v, links)
        # Replacing the declared left multiplication by right multiplication
        # must differ on these noncommuting histories.
        assert np.max(np.abs(tangent-h[:, None, None]*quaternion_product(links, algebra_v))) > 0.2
        x, beta = 1.3+0.7*m, 0.017
        temporal = quaternion_product(links[:-1], quaternion_inverse(links[1:]))
        b_score = (x/m)*np.sum(quaternion_product(algebra_v, temporal[:m])[..., 0])
        potential, dpotential = wilson_potential_and_derivative(links, tangent, faces)
        d_score = -beta*np.sum(dpotential[1:m])
        step = 2e-4

        def transformed(s):
            rotation = quaternion_exponential(s*h[:, None, None]*v)
            changed = quaternion_product(rotation, links)
            close(np.sum(changed*changed, axis=-1), 1.0)
            close(changed[n:], links[n:])
            close(changed[0], quaternion_product(quaternion_exponential(s*v), links[0]))
            return changed

        def log_terms(s):
            changed = transformed(s)
            z = quaternion_product(changed[:-1], quaternion_inverse(changed[1:]))
            w, _ = wilson_potential_and_derivative(changed, np.zeros_like(changed), faces)
            # The initial half-potential is deterministic in the conditioned
            # history and cancels in the normalized score. Keep all others.
            return np.array([x*np.sum(z[..., 0]), -beta*(np.sum(w[1:-1])+w[-1]/2)])

        finite_difference = (-log_terms(2*step)+8*log_terms(step)
                             - 8*log_terms(-step)+log_terms(-2*step))/(12*step)
        expected = np.array([b_score, d_score])
        error = float(np.max(np.abs(finite_difference-expected)))
        max_difference = max(max_difference, error)
        close(finite_difference, expected, 2e-8)
        # Initial half-potential removal itself has the stated derivative.
        d_initial = -beta*dpotential[0]/2
        initial_fd = []
        for s in (step, -step):
            w, _ = wilson_potential_and_derivative(transformed(s), np.zeros_like(links), faces)
            initial_fd.append(-beta*w[0]/2)
        close((initial_fd[0]-initial_fd[1])/(2*step), d_initial, 2e-7)
        cases += 1
        if m == 1:
            close(d_score, 0.0)
            continue
        # Resample a column whose own tangent is ZERO. Exterior tangents on
        # shared plaquettes still contribute to its score oscillation.
        e = int(np.argmax(incidence.sum(axis=1)))
        v[e] = 0
        algebra_v[e] = 0
        original_tangent = h[:, None, None]*quaternion_product(algebra_v, links)
        _, original_d = wilson_potential_and_derivative(links, original_tangent, faces)
        changed = links.copy()
        replacement = rng.normal(size=(m-1, 4))
        replacement /= np.linalg.norm(replacement, axis=-1, keepdims=True)
        changed[1:m, e] = replacement
        changed_tangent = h[:, None, None]*quaternion_product(algebra_v, changed)
        _, changed_d = wilson_potential_and_derivative(changed, changed_tangent, faces)
        difference = beta*abs(np.sum(changed_d[1:m]-original_d[1:m]))
        bound = beta*(m-1)*(incidence[e]@np.linalg.norm(v, axis=1))
        assert 1e-7 < difference <= bound+1e-12
        # A row that retained only the tangent on e would claim zero here.
        assert np.linalg.norm(v[e]) == 0 and bound > 0
        mixed_cases += 1
    print(f"PASS {cases} noncommuting SU(2) ramp log-weight derivatives: "
          f"kinetic, all magnetic factors and fixed endpoints; max error={max_difference:.3e}")
    print(f"PASS {mixed_cases} mixed-neighbor score tests with zero self tangent "
          "and actual oriented plaquette incidence")


def su2_haar_fisher():
    """S^3 angular quadrature; the six S^2 axes integrate degree two exactly."""
    node, weight = np.polynomial.legendre.leggauss(256)
    theta = (node+1)*math.pi/2
    weight *= math.pi/2
    axes = np.vstack((np.eye(3), -np.eye(3)))
    z = np.zeros((len(theta), len(axes), 4))
    z[..., 0] = np.cos(theta)[:, None]
    z[..., 1:] = np.sin(theta)[:, None, None]*axes
    direction = np.array([0.2, -0.8, 1.1])
    direction /= np.linalg.norm(direction)
    cases, residual = 0, 0.0
    for x, length in itertools.product((0.05, 0.5, 1, 3, 10, 50, 100), (0.4, 1.0, 2.3)):
        density = weight*np.sin(theta)**2*np.exp(x*(np.cos(theta)-1))
        density /= density.sum()
        v = np.r_[0.0, length*direction]
        first = quaternion_product(v, z)[..., 0]
        second = quaternion_product(v, quaternion_product(v, z))[..., 0]
        close(second, -length**2*z[..., 0])
        mean_first = density@np.mean(first, axis=1)
        mean_phi = density@np.cos(theta)
        second_moment = density@np.mean(first**2, axis=1)
        close(mean_first, 0.0)
        fisher = x*x*second_moment
        expected = x*length**2*mean_phi
        residual = max(residual, abs(fisher-expected))
        close(fisher, expected, 2e-10)
        assert 0 <= fisher <= x*length**2+1e-12
        cases += 1
    print(f"PASS {cases} SU(2) Haar Fisher quadratures: "
          f"x^2 E[(d_v phi)^2]=x |v|^2 E[phi] <= x |v|^2; max residual={residual:.3e}")


def su2_ramp_constants():
    """WC17 exact expressions evaluated numerically, not rounded as inputs."""
    ratio = Fraction(22, 13)
    lam = float(Fraction(33, 20)*Fraction(13, 22)**2)*math.exp(-float(Fraction(11, 50)))
    cstar = (math.sqrt(float(ratio))*math.exp(float(Fraction(1, 10)))/2
             + float(Fraction(1, 10)))**2/float(Fraction(11, 20))
    kstar = lam/(lam+2*cstar)
    close([lam, cstar, kstar], [0.4623602620, 1.2191229068, 0.1594012596], 6e-11)
    count = 0
    for ds, x, zeta in itertools.product(
            (2, 3, 4), (1, 1.001, 1.2499, 1.25, 1.2501, 2.13, 7, 100, 10000),
            (0.0, 0.001, 0.005)):
        beta = zeta/((ds-1)*x)
        m = math.ceil(4*x)
        b = 4*(ds-1)*beta
        tau = math.tanh((math.log(float(ratio))+m*b)/2)
        susceptibility = 2*m/(1-tau)-1
        q = 6*(ds-1)*beta*susceptibility
        assert m*b <= 0.1+1e-14 and tau <= 1/3 and q <= 0.45
        actual_lam = 3*math.exp(-b-2*m*b-2*math.log(float(ratio)))*(1-q)
        a = float(ratio)*math.exp(2*m*b)*x/m
        cf = (math.sqrt(a)+m*b)**2/(1-q)
        kappa = actual_lam/(actual_lam+2*cf)
        assert actual_lam >= lam-1e-14 and cf <= cstar+1e-14
        assert kappa >= kstar-1e-14 and 0 < kappa < 1
        count += 1
    limiting_rate = -math.log1p(-kstar)/16
    for epsilon in (1.0, 0.7, 0.3, 0.11, 0.023, 0.0041, 0.000013):
        n = 2*math.ceil(4/epsilon)
        half_slab = n*epsilon
        assert 8-1e-12 <= half_slab < 8+2*epsilon+1e-12
        rate = -math.log1p(-kstar)/(2*half_slab)
        assert 0 < rate <= limiting_rate+1e-14
        assert limiting_rate-rate <= limiting_rate*epsilon/4+1e-14
        close(math.exp(-2*half_slab*rate), 1-kstar)
    close(limiting_rate, 0.0108525534, 6e-11)
    print(f"PASS {count} WC17 ramp certificate cases: "
          f"lambda_*={lam:.12f}, C_*={cstar:.12f}, kappa_*={kstar:.12f}")
    print(f"PASS 7 temporal-rounding and rate checks: n*epsilon -> 8; "
          f"bridge rate={limiting_rate:.12f}, separate gradient rate={lam/2:.12f}")


def rectangular_cycle_carrier(extents):
    """Complete Z2 gauge quotient of an open rectangular spatial cell complex.

    A maximal tree is fixed to +1.  The remaining chord signs freely label
    every orbit; fundamental cycles furnish their dual character basis.
    Spatial faces need not be independent: the cube has six faces but only
    five chords, and its face dependence is retained.
    """
    vertices = list(itertools.product(*(range(n+1) for n in extents)))
    vertex_index = {v: i for i, v in enumerate(vertices)}
    edges = []
    edge_index = {}
    for v in vertices:
        for axis, n in enumerate(extents):
            if v[axis] < n:
                w = list(v)
                w[axis] += 1
                w = tuple(w)
                edge_index[(v, axis)] = len(edges)
                edges.append((vertex_index[v], vertex_index[w]))
    component = list(range(len(vertices)))

    def root(v):
        while component[v] != v:
            component[v] = component[component[v]]
            v = component[v]
        return v

    tree = [[] for _ in vertices]
    chords = []
    for ei, (u, v) in enumerate(edges):
        ru, rv = root(u), root(v)
        if ru == rv:
            chords.append(ei)
        else:
            component[ru] = rv
            tree[u].append((v, ei))
            tree[v].append((u, ei))

    def tree_path(u, v):
        todo = [(u, -1, 0)]
        while todo:
            point, parent, mask = todo.pop()
            if point == v:
                return mask
            todo.extend((q, point, mask ^ (1 << ei))
                        for q, ei in tree[point] if q != parent)
        raise AssertionError("Disconnected spanning tree")

    cycles = [(1 << ei) ^ tree_path(*edges[ei]) for ei in chords]
    rank = len(cycles)
    assert rank == len(edges)-len(vertices)+1
    cycle_masks = []
    for subset in range(1 << rank):
        mask = 0
        for ci, cycle in enumerate(cycles):
            if (subset >> ci) & 1:
                mask ^= cycle
        cycle_masks.append(mask)
        # Every retained character is exactly gauge invariant at every vertex.
        incidence = [0]*len(vertices)
        for ei, (u, v) in enumerate(edges):
            if (mask >> ei) & 1:
                incidence[u] ^= 1
                incidence[v] ^= 1
        assert not any(incidence)
    assert len(set(cycle_masks)) == 1 << rank
    face_masks = []
    face_characters = []
    for v in vertices:
        for axis in range(len(extents)):
            for other in range(axis+1, len(extents)):
                if v[axis] >= extents[axis] or v[other] >= extents[other]:
                    continue
                va, vb = list(v), list(v)
                va[axis] += 1
                vb[other] += 1
                mask = ((1 << edge_index[(v, axis)])
                        ^ (1 << edge_index[(tuple(va), other)])
                        ^ (1 << edge_index[(v, other)])
                        ^ (1 << edge_index[(tuple(vb), axis)]))
                coefficient = sum(((mask >> ei) & 1) << ci
                                  for ci, ei in enumerate(chords))
                assert cycle_masks[coefficient] == mask
                face_masks.append(mask)
                face_characters.append(coefficient)
    dimension = 1 << rank
    fourier = np.array([[(-1.0)**((x & y).bit_count())
                         for y in range(dimension)]
                        for x in range(dimension)])/math.sqrt(dimension)
    close(fourier.T@fourier, np.eye(dimension))
    lengths = np.array([mask.bit_count() for mask in cycle_masks], dtype=float)
    potential = np.array([sum(1-(-1)**((z & face).bit_count())
                              for face in face_characters)
                          for z in range(dimension)], dtype=float)
    if extents == (1, 1, 1):
        assert len(face_masks) == 6 and rank == 5
        xor_faces = 0
        for mask in face_masks:
            xor_faces ^= mask
        assert xor_faces == 0
    return edges, cycle_masks, fourier, lengths, potential, len(face_masks)


def complete_perron_bridge(blocked, psi, tolerance=3e-10):
    """Full middle-to-both-endpoints bridge for one normalized physical block.

    The endpoint reference is nu(x) P^2(x,z), not nu(x)nu(z).  Matrices use
    counting-measure Euclidean coordinates after stationary square-root
    weighting.  All midpoint functions, not only plaquette probes, are kept.
    """
    size = len(psi)
    nu = psi**2
    p = blocked*psi[None, :]/psi[:, None]
    close(p.sum(axis=1), np.ones(size), tolerance)
    close(nu@p, nu, tolerance)
    close(nu[:, None]*p, nu[None, :]*p.T, tolerance)
    assert p.min() > 0
    endpoint = nu[:, None]*(p@p)
    close(endpoint.sum(), 1.0, tolerance)
    joint_given_mid = p[:, :, None]*p[:, None, :]
    analysis = (psi[:, None, None]*joint_given_mid
                / np.sqrt(endpoint)[None, :, :]).reshape(size, size*size).T
    close(analysis@psi, np.sqrt(endpoint).reshape(-1), tolerance)
    s = analysis.T@analysis
    close(s@psi, psi, tolerance)
    psd(np.eye(size)-s, tolerance)
    psd(s-blocked@blocked, tolerance)
    centered = s-np.outer(psi, psi)
    eigenvalues, eigenvectors = np.linalg.eigh(centered)
    close(centered@eigenvectors, eigenvectors*eigenvalues[None, :], tolerance)
    kappa = 1-float(eigenvalues[-1])
    assert 0 < kappa < 1
    return kappa, s


def perron_block(transfer, depth):
    eigenvalues, eigenvectors = np.linalg.eigh(transfer)
    close(transfer@eigenvectors, eigenvectors*eigenvalues[None, :])
    assert eigenvalues.min() > 0
    psi = eigenvectors[:, -1]
    if psi.sum() < 0:
        psi = -psi
    assert psi.min() > 0
    ratios = eigenvalues/eigenvalues[-1]
    blocked = (eigenvectors*(ratios**depth)[None, :])@eigenvectors.T
    close(blocked@psi, psi)
    return blocked, psi, -math.log(float(ratios[-2]))


def raw_rectangle_projection():
    """Independent raw-link Wilson restriction for two adjacent plaquettes."""
    edges, cycles, fourier, lengths, bare_potential, _ = rectangular_cycle_carrier((2, 1))
    edge_count = len(edges)
    assert edge_count == 7 and len(cycles) == 4
    raw_size, quotient_size = 1 << edge_count, len(cycles)
    r = 0.63
    raw = np.ones((raw_size, raw_size))
    for i in range(raw_size):
        for j in range(raw_size):
            for ei in range(edge_count):
                raw[i, j] *= (1+r*(-1)**(((i ^ j) >> ei) & 1))/2
    embedding = np.zeros((raw_size, quotient_size))
    fundamental = [cycles[1 << ci] for ci in range(2)]
    orbit_size = raw_size//quotient_size
    for bits in range(raw_size):
        orbit = sum(((bits & mask).bit_count() % 2) << ci
                    for ci, mask in enumerate(fundamental))
        embedding[bits, orbit] = 1/math.sqrt(orbit_size)
    close(embedding.T@embedding, np.eye(quotient_size))
    kinetic = (fourier*(r**lengths)[None, :])@fourier.T
    close(embedding.T@raw@embedding, kinetic)
    close(raw@embedding, embedding@kinetic)
    # Independently construct actual geometric face products on raw links.
    # Do not recover them from the previously derived quotient potential.
    vertices = list(itertools.product(range(3), range(2)))
    vertex_index = {v: i for i, v in enumerate(vertices)}
    edge_index = {tuple(sorted(edge)): ei for ei, edge in enumerate(edges)}
    face_masks = []
    for left in range(2):
        corners = ((left, 0), (left+1, 0), (left+1, 1), (left, 1))
        mask = 0
        for v, w in zip(corners, corners[1:]+corners[:1]):
            pair = tuple(sorted((vertex_index[v], vertex_index[w])))
            mask ^= 1 << edge_index[pair]
        face_masks.append(mask)
    raw_potential = np.array([sum(1-(-1)**((bits & face).bit_count())
                                 for face in face_masks)
                              for bits in range(raw_size)], dtype=float)
    orbit_indicator = embedding*math.sqrt(orbit_size)
    close(raw_potential, orbit_indicator@bare_potential)
    beta = 0.37
    raw_dressing = np.exp(-beta*raw_potential/2)
    quotient_dressing = np.exp(-beta*bare_potential/2)
    raw_transfer = raw_dressing[:, None]*raw*raw_dressing[None, :]
    quotient_transfer = quotient_dressing[:, None]*kinetic*quotient_dressing[None, :]
    close(raw_transfer@embedding, embedding@quotient_transfer)
    close(embedding.T@raw_transfer@embedding, quotient_transfer)
    raw_block, raw_psi, _ = perron_block(raw_transfer, 1)
    quotient_block, quotient_psi, _ = perron_block(quotient_transfer, 1)
    close(raw_psi, embedding@quotient_psi)
    raw_doob = raw_block*raw_psi[None, :]/raw_psi[:, None]
    quotient_doob = quotient_block*quotient_psi[None, :]/quotient_psi[:, None]
    close(raw_doob@orbit_indicator, orbit_indicator@quotient_doob)
    close((raw_psi**2)@orbit_indicator, quotient_psi**2)
    print("PASS 128 raw Wilson link states -> 4 complete gauge orbits: kinetic/magnetic restriction, Perron law and Doob lumpability")


def exact_biased_plaquette_bridge():
    """Rational same-law counterexample to importing the Gaussian gap formula."""
    f = Fraction
    pi = (f(3, 4), f(1, 4))
    transition = ((f(7, 8), f(1, 8)), (f(3, 8), f(5, 8)))
    endpoint = tuple(tuple(sum(pi[y]*transition[y][x]*transition[y][z]
                               for y in range(2))
                           for z in range(2)) for x in range(2))
    assert endpoint == ((f(39, 64), f(9, 64)), (f(9, 64), f(7, 64)))
    # For the binary indicator, average conditional variance divided by
    # pi[0]*pi[1] spans the entire one-dimensional centered carrier.
    kappa = sum(transition[0][x]*transition[0][z]
                * transition[1][x]*transition[1][z]/endpoint[x][z]
                for x in range(2) for z in range(2))
    gaussian_value = f(3, 5)  # (1-r^2)/(1+r^2), r=1/2.
    assert kappa == f(163, 273)
    assert kappa-gaussian_value == -f(4, 1365)
    # Identify the rational law with the same fixed-space one-plaquette
    # Hamiltonian family used above, not with an unrelated Markov sampler.
    coupling = 1/math.sqrt(3)
    ell = math.sqrt(3)*math.log(2)/4
    hamiltonian = np.array([[1.0, -1.0], [-1.0, 1+2*coupling]])
    energies, vectors = np.linalg.eigh(hamiltonian)
    close(energies[1]-energies[0], 4/math.sqrt(3))
    psi = vectors[:, 0]
    if psi.sum() < 0:
        psi = -psi
    block = (vectors*np.exp(-ell*(energies-energies[0]))[None, :])@vectors.T
    close(psi**2, np.array(pi, dtype=float))
    close(block*psi[None, :]/psi[:, None], np.array(transition, dtype=float))
    numeric_kappa, _ = complete_perron_bridge(block, psi)
    close(numeric_kappa, float(kappa))
    close(math.tanh(ell*(energies[1]-energies[0])), float(gaussian_value))
    print(f"PASS exact interacting one-plaquette bridge: kappa={kappa}, "
          f"tanh(ell*gap)={gaussian_value}, difference={kappa-gaussian_value}")


def rectangular_temporal_refinement():
    """Finite interacting Wilson bridges at a fixed physical half-slab.

    gamma, coupling and ell are supplied calibration inputs.  The Z2 Wilson
    path is tanh(x_epsilon)=exp(-epsilon*gamma), beta=epsilon*coupling.
    It is not the compact-SU(2) asymptotic x_epsilon~1/epsilon.  Only time
    spacing is refined; every spatial graph and its finite carrier stay fixed.
    """
    raw_rectangle_projection()
    gamma, ell = 0.5, 0.5
    depths = (1, 2, 4, 8, 16, 32)
    count = 0
    print("Fixed-space temporal refinement: supplied gamma=0.5, ell=0.5; beta=epsilon*g")
    print("graph cycles states g kappa_H gap_H rate_bound kappa_H-tanh(ell*gap_H) commutator")
    for extents in ((1, 1), (2, 1), (2, 2), (1, 1, 1)):
        edges, cycles, fourier, lengths, bare_potential, faces = rectangular_cycle_carrier(extents)
        size = len(cycles)
        electric = (fourier*(gamma*lengths)[None, :])@fourier.T
        for coupling in (0.0, 0.2, 0.8):
            potential = coupling*bare_potential
            hamiltonian = electric+np.diag(potential)
            energies, vectors = np.linalg.eigh(hamiltonian)
            close(hamiltonian@vectors, vectors*energies[None, :])
            psi_h = vectors[:, 0]
            if psi_h.sum() < 0:
                psi_h = -psi_h
            assert psi_h.min() > 0
            gap_h = float(energies[1]-energies[0])
            assert gap_h > 0
            block_h = (vectors*np.exp(-ell*(energies-energies[0]))[None, :])@vectors.T
            kappa_h, s_h = complete_perron_bridge(block_h, psi_h)
            rate_h = -math.log1p(-kappa_h)/(2*ell)
            assert rate_h <= gap_h+3e-10
            commutator = float(np.linalg.norm(s_h@block_h-block_h@s_h, ord=2))
            errors, bridge_errors, refined = [], [], []
            for depth in depths:
                epsilon = ell/depth
                r = math.exp(-epsilon*gamma)
                x = math.atanh(r)
                close(math.tanh(x), r)
                beta = epsilon*coupling
                kinetic = (fourier*np.exp(-epsilon*gamma*lengths)[None, :])@fourier.T
                close(kinetic.sum(axis=1), np.ones(size))
                assert kinetic.min() > 0
                dressing = np.exp(-beta*bare_potential/2)
                transfer = dressing[:, None]*kinetic*dressing[None, :]
                block, psi, step_gap = perron_block(transfer, depth)
                kappa, s = complete_perron_bridge(block, psi)
                physical_gap = step_gap/epsilon
                lower_rate = -math.log1p(-kappa)/(2*ell)
                assert lower_rate <= physical_gap+3e-10
                errors.append(float(np.linalg.norm(block-block_h, ord=2)))
                bridge_errors.append(abs(kappa-kappa_h))
                refined.append((kappa, physical_gap, lower_rate))
                count += 1
            if coupling == 0:
                assert max(errors+bridge_errors) < 3e-10
                close(commutator, 0.0)
            else:
                # Genuine electric/magnetic noncommutation and O(epsilon^2)
                # fixed-time Strang convergence, not a single endpoint tilt.
                assert np.linalg.norm(electric@np.diag(potential)-np.diag(potential)@electric) > 1e-3
                assert errors[0] > 1e-5
                assert errors[-1] < errors[0]/100
                assert errors[-1] < errors[-2]*0.35
                assert bridge_errors[-1] < max(bridge_errors[0]/50, 1e-10)
                kinetic_total = (fourier*np.exp(-ell*gamma*lengths)[None, :])@fourier.T
                once = np.exp(-ell*potential/2)
                naive = once[:, None]*kinetic_total*once[None, :]
                naive_block, _, _ = perron_block(naive, 1)
                assert np.linalg.norm(naive_block-block, ord=2) > 1e-5
                assert np.linalg.norm(kinetic_total-block, ord=2) > 1e-5
            label = "x".join(map(str, extents))
            print(f"{label} {int(math.log2(size))} {size} {coupling:.1f} "
                  f"{kappa_h:.9f} {gap_h:.9f} {rate_h:.9f} "
                  f"{kappa_h-math.tanh(ell*gap_h):+.9f} {commutator:.3e}")
            print(f"  n=1->32 block error {errors[0]:.3e}->{errors[-1]:.3e}; "
                  f"bridge error {bridge_errors[0]:.3e}->{bridge_errors[-1]:.3e}; "
                  f"n=32 kappa={refined[-1][0]:.9f} gap={refined[-1][1]:.9f}")
            if extents == (1, 1, 1):
                assert faces == 6 and size == 32
    print(f"PASS {count} same-law complete Wilson bridges through fixed-space temporal refinement")
    print("Finite floating-point spectra are calibrations, not certified lower bounds; "
          "no spatial thermodynamic/continuum limit, compact-simple group, or generated physical mass is established.")


if __name__ == "__main__":
    slabs()
    bridges()
    su2_constants()
    rectangular_temporal_refinement()
    exact_biased_plaquette_bridge()
    su2_ramp_differentiation()
    su2_haar_fisher()
    su2_ramp_constants()
    print("SU(2) differential, quadrature and constant checks are deterministic numerical "
          "evidence, not a proof of the full-group inequalities or any limiting construction.")
    print("No compact-group discretization limit or four-dimensional continuum gap is certified.")
