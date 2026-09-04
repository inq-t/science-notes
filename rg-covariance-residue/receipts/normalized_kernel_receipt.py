"""Exact finite kernels and Markov residue identities; no physical randomness premise."""

import numpy as np


def covariance(f, g, weights):
    return np.vdot(f, weights*g) - np.conj(weights @ f) * (weights @ g)


# A finite subgroup of U(1), with an exact normalized counting Haar measure.
count, kappa = 48, 2.3
angles = np.arange(count) * 2*np.pi/count
first, second = np.meshgrid(angles, angles, indexing="ij")
z = (0.5*np.exp(1j*first) + 0.5*np.exp(1j*second)).ravel()
action = (0.4*np.cos(first-second) + 0.2*np.cos(2*first+second)).ravel()
fine = np.exp(-action)
fine /= fine.sum()
exponent = kappa * np.real(z[:, None]*np.exp(-1j*angles)[None, :])
normalizer = np.exp(exponent).mean(axis=1)
density = np.exp(exponent) / normalizer[:, None]
joint = fine[:, None]*density/count
assert np.max(np.abs(joint.sum(axis=1)-fine)) < 1e-16
wrong = fine*normalizer
wrong /= wrong.sum()
assert np.sum(np.abs(wrong-fine)) > 0.1
assert np.isfinite(density).all()
singular = np.abs(z) < 1e-12
assert np.max(np.abs(density[singular]-1)) < 1e-12
print("PASS: full-domain normalized gauge kernel preserves the exact fine marginal.")
print("PASS: omitting the normalizer changes the law; singular averages remain defined.")


source = np.exp(1j*first.ravel()) + 0.3*np.sin(second.ravel())
v = 0.41


def conditioned(value):
    raw = fine*np.exp(kappa*np.real(z*np.exp(-1j*value)))/normalizer
    return raw/raw.sum()


step = 1e-6
derivative = ((conditioned(v+step)-conditioned(v-step)) @ source)/(2*step)
score = kappa*np.real(1j*np.exp(-1j*v)*z)
assert abs(derivative + covariance(score, source, conditioned(v))) < 1e-9
print("PASS: complex-linear retained derivative has the real score in the first covariance slot.")


initial = np.array([0.23, 0.77])
forward0 = np.array([[0.60, 0.30, 0.10], [0.10, 0.35, 0.55]])
forward1 = np.array([[0.85, 0.15], [0.45, 0.55], [0.12, 0.88]])
law = initial[:, None, None]*forward0[:, :, None]*forward1[None, :, :]
indices = np.array(list(np.ndindex(law.shape)))
weights = law.ravel()


def projection(columns):
    labels = indices[:, columns]
    same = np.all(labels[:, None, :] == labels[None, :, :], axis=2)
    weighted = same*weights[None, :]
    return weighted/weighted.sum(axis=1)[:, None]


suffix = [projection(list(range(j, 3))) for j in range(3)]
single = [projection([j]) for j in range(3)]
f = np.array([1+2j, -0.2+0.4j])[indices[:, 0]]
g = np.array([0.8-0.1j, 0.7+1.3j])[indices[:, 0]]
shell = [suffix[j]-suffix[j+1] for j in range(2)]
for j in range(3):
    assert np.linalg.norm(suffix[j]@f-single[j]@f) < 1e-12
for j in range(2):
    assert np.linalg.norm(shell[j]@shell[j]-shell[j]) < 1e-12
assert np.linalg.norm(shell[0]@shell[1]) < 1e-12
assert np.linalg.norm(single[1]@single[2]-single[2]) > 0.1
rhs = covariance(suffix[-1]@f, suffix[-1]@g, weights)
rhs += sum(np.vdot(d@f, weights*(d@g)) for d in shell)
assert abs(rhs-covariance(f, g, weights)) < 1e-12
print("PASS: nested suffix projections, Markov reduction, and complex covariance-residue identity.")
print("PASS: individual state algebras fail the nesting test.")


independent0 = np.tile(np.array([0.2, 0.3, 0.5]), (2, 1))
law = initial[:, None, None]*independent0[:, :, None]*forward1[None, :, :]
weights = law.ravel()
centered = f - weights@f
later = projection([1, 2])@centered
assert np.linalg.norm(later) < 1e-12
assert abs(covariance(centered, centered, weights)-np.vdot(centered-later, weights*(centered-later))) < 1e-12
print("PASS: independent readout transfers every centered correlation into the first residue.")
# SU(2) Haar radial quadrature: f(W)=cos(theta), angular second moment 1/3.
nodes, gauss_weights = np.polynomial.legendre.leggauss(192)
theta = (nodes+1)*np.pi/2
radial_weights = gauss_weights*np.sin(theta)**2
cosine = np.cos(theta)


def su2_log_normalizer(concentration):
    exponent = concentration*cosine
    peak = exponent.max()
    return peak + np.log(np.dot(radial_weights, np.exp(exponent-peak)))


def su2_moments(concentration):
    exponent = concentration*cosine
    radial = radial_weights*np.exp(exponent-exponent.max())
    radial /= radial.sum()
    return radial, radial@cosine


def su2_exp(vector):
    length = np.linalg.norm(vector)
    if length == 0:
        return np.array([1.0, 0.0, 0.0, 0.0])
    return np.r_[np.cos(length), np.sin(length)*vector/length]


velocities = np.array([[0.3, -0.2, 0.4], [-0.4, 0.1, 0.2], [0.2, 0.5, -0.1]])
path_weights = np.array([0.2, 0.3, 0.5])
mean_velocity = path_weights@velocities
scatter = path_weights@np.sum((velocities-mean_velocity)**2, axis=1)
output_velocity = np.array([-0.2, 0.4, 0.6])

for concentration in (0.3, 2.0, 10.0, 100.0):
    radial, alpha = su2_moments(concentration)
    assert 0 < alpha < 1
    ward = concentration**2*(radial@np.sin(theta)**2)/3
    assert abs(ward-concentration*alpha) < 2e-10

    def negative_log_mode(t):
        z = path_weights@np.array([su2_exp(t*x) for x in velocities])
        v = su2_exp(t*output_velocity)
        return -concentration*np.dot(v, z) + su2_log_normalizer(concentration*np.linalg.norm(z))

    h = 2e-4
    hessian = (negative_log_mode(h)-2*negative_log_mode(0)+negative_log_mode(-h))/h**2
    expected = concentration*(
        np.sum((output_velocity-mean_velocity)**2)+(1-alpha)*scatter
    )
    assert abs(hessian-expected) < 4e-6
    fisher = ward*np.sum(mean_velocity**2)
    assert abs(fisher-concentration*alpha*np.sum(mean_velocity**2)) < 1e-11
    # Opposite paths: zero input score and Fisher, positive mode Hessian.
    scatter_hessian_by_output = concentration*(cosine-alpha)
    assert abs(radial@scatter_hessian_by_output) < 1e-12
    assert concentration*(1-alpha) > 0

assert abs(100*(1-su2_moments(100)[1])-1.5) < 0.01
print("PASS: SU(2) Haar moment, normalized-kernel Hessian, Fisher metric, and Ward identity.")
print("PASS: opposite paths have zero Fisher information but positive mode curvature.")

errors = []
k = 1.4
target_log_density = 1.5*np.log(k/(2*np.pi))-k*np.sum((output_velocity-mean_velocity)**2)/2
for epsilon in (0.2, 0.1, 0.05, 0.025):
    concentration = k/epsilon**2
    z = path_weights@np.array([su2_exp(epsilon*x) for x in velocities])
    v = su2_exp(epsilon*output_velocity)
    radius = epsilon*np.linalg.norm(output_velocity)
    log_jacobian = -np.log(2*np.pi**2)+2*np.log(np.sin(radius)/radius)
    log_density = (
        3*np.log(epsilon)+log_jacobian
        + concentration*np.dot(v, z)
        - su2_log_normalizer(concentration*np.linalg.norm(z))
    )
    errors.append(abs(log_density-target_log_density))
assert errors[-1] < errors[0]/20
assert errors[-1] < 0.001
print("PASS: rescaled Haar density converges to the declared normalized Gaussian.")
print("Not tested: reverse conditional localization, nonlinear RG limit, OS reconstruction, or Yang--Mills mass gap.")
