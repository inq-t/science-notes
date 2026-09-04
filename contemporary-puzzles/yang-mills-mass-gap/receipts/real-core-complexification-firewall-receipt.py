"""A real-core lower bound need not control the complex spectral floor."""

import numpy as np


hamiltonian = np.diag([0.5, 1.5]).astype(complex)

# D_R = {(a+ib, a-ib): a,b real}.  These two real generators have complex
# span C^2, but the energy cross terms hidden by the real slice matter.
real_generators = np.array(
    [
        [1.0, 1.0],
        [1j, -1j],
    ],
    dtype=complex,
).T

assert np.linalg.matrix_rank(real_generators) == 2

for a, b in ((1.0, 0.0), (0.0, 1.0), (1.7, -0.4), (-0.2, 2.3)):
    vector = real_generators @ np.array([a, b], dtype=complex)
    norm = np.vdot(vector, vector).real
    energy = np.vdot(vector, hamiltonian @ vector).real
    assert np.isclose(energy, norm)

spectral_floor = np.linalg.eigvalsh(hamiltonian)[0]
assert np.isclose(spectral_floor, 0.5)
assert spectral_floor < 1.0

print("REAL_CORE_APPARENT_FLOOR=1.000000000000")
print(f"COMPLEX_SPECTRAL_FLOOR={spectral_floor:.12f}")
print("COMPLEXIFICATION_SPANS_FULL_SPACE=True")
print("REAL_TO_COMPLEX_GAP_INFERENCE_BLOCKED")
