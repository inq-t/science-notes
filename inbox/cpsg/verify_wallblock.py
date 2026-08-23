"""The algebra/state split, computed exactly on a lattice field.
Claim under test (user's thesis, precisified):
  - the COMMUTATOR (algebra structure) has a sharp causal front -- the wall,
    with an emergent speed c_eff: 'relativity' lives here;
  - the CORRELATIONS (state structure) are nonzero EVERYWHERE at equal time --
    'the photon is everywhere': the block is not confined by the cone.
Exact free-field lattice: N coupled oscillators, everything by normal modes."""
import numpy as np

N, m = 201, 0.05                      # sites, small mass
j0 = N//2
k = np.arange(N)
K = 2*np.pi*k/N
om = np.sqrt(m**2 + 4*np.sin(K/2)**2)  # dispersion
V = np.exp(2j*np.pi*np.outer(np.arange(N), k)/N)/np.sqrt(N)  # Fourier modes

def commutator_phi_pi(t):
    # [phi_j(t), pi_{j0}(0)] = i * sum_k cos(om t) e^{ik(j-j0)} / N   (exact)
    return np.real(V @ (np.cos(om*t) * np.conj(V[j0])))

def correlator_phi_phi():
    # <0| phi_j phi_{j0} |0> = sum_k e^{ik(j-j0)} / (2 om N)          (exact)
    return np.real(V @ (1/(2*om) * np.conj(V[j0])))

c_group = np.max(np.gradient(om, K[1]-K[0])[:N//2])   # max group velocity
print(f"emergent maximum signal speed (max group velocity): c_eff = {c_group:.4f}")

t = 60.0
C = commutator_phi_pi(t); G = correlator_phi_phi()
front = c_group*t
inside  = [j for j in range(N) if abs(j-j0) < 0.8*front]
outside = [j for j in range(N) if 1.3*front < abs(j-j0) < N//2]
print(f"\nat t={t}: causal front at |j-j0| = c_eff*t = {front:.1f} sites")
print(f"  commutator INSIDE the cone  (mean |C|): {np.mean(np.abs(C)[inside]):.3e}")
print(f"  commutator OUTSIDE the cone (mean |C|): {np.mean(np.abs(C)[outside]):.3e}")
print(f"  suppression factor: {np.mean(np.abs(C)[inside])/np.mean(np.abs(C)[outside]):.1e}")
print(f"\n  equal-time correlations at the SAME outside sites (mean |G|): "
      f"{np.mean(np.abs(G)[outside]):.3e}")
print(f"  correlations at the far edge |j-j0|={N//2}: {abs(G[0]):.3e}  (nonzero)")
print("\n=> THE SPLIT, exact on the lattice:")
print("   algebra (commutators): sharp front, emergent c -- THE WALL.")
print("   state   (correlations): everywhere nonzero at t=0 -- THE BLOCK.")
print("   'c' is a structural property of the observable algebra's front,")
print("   not a fence on the state. [Continuum pins: microcausality;")
print("   Reeh-Schlieder; W(x,y) != 0 spacelike while [phi,phi] = 0 spacelike.]")
