import numpy as np
from itertools import product
rng = np.random.default_rng(20260909)

def G_from(z12, z23, z31):
    return np.array([[1, z12, np.conj(z31)],
                     [np.conj(z12), 1, z23],
                     [z31, np.conj(z23), 1]], dtype=complex)

def delta3(G): return G[0,1]*G[1,2]*G[2,0]

def Anorm2(G):
    # ||A f||^2 / ||f||^2 = 6 - 2*Re(G12+G23+G31)
    return 6 - 2*np.real(G[0,1]+G[1,2]+G[2,0])

print("="*66)
print("R1  determinant identity  det(2I-G) = det G - 4 Re(G12 G23 G31)")
worst = 0.0
for _ in range(200000):
    z = (rng.normal(size=3) + 1j*rng.normal(size=3))*rng.uniform(0,1.5)
    G = G_from(*z)
    lhs = np.linalg.det(2*np.eye(3)-G)
    rhs = np.linalg.det(G) - 4*np.real(delta3(G))
    worst = max(worst, abs(lhs-rhs))
print(f"    200000 random Hermitian unit-diagonal matrices, max |LHS-RHS| = {worst:.3e}")

print("="*66)
print("R2  MA2 implication:  G>=0, unit diag, Re D3<=0  ==>  G<=2I  and  3<=A*A<=9")
n_tested = 0; viol_G = 0; viol_A = 0; lam_max = 0.0; a_lo = 9.0; a_hi = 0.0
while n_tested < 400000:
    # sample PSD unit-diagonal by random low/full-rank Gram
    r = rng.integers(1,4)
    V = rng.normal(size=(3,r)) + 1j*rng.normal(size=(3,r))
    V /= np.linalg.norm(V,axis=1,keepdims=True)
    G = V @ V.conj().T
    if np.real(delta3(G)) > 0: continue
    n_tested += 1
    lam = np.linalg.eigvalsh(G)[-1]; lam_max = max(lam_max, lam)
    if lam > 2 + 1e-9: viol_G += 1
    a = Anorm2(G); a_lo = min(a_lo,a); a_hi = max(a_hi,a)
    if a < 3 - 1e-9 or a > 9 + 1e-9: viol_A += 1
print(f"    {n_tested} samples satisfying the premise")
print(f"    violations of G<=2I : {viol_G}      max eigenvalue found : {lam_max:.6f}")
print(f"    violations of 3<=A*A<=9 : {viol_A}  range found : [{a_lo:.4f}, {a_hi:.4f}]")

print("="*66)
print("R3  sharpness: G12=G23=G31 = i/sqrt(3)")
Gs = G_from(1j/np.sqrt(3), 1j/np.sqrt(3), 1j/np.sqrt(3))
print("    spectrum =", np.round(np.linalg.eigvalsh(Gs),12))
print(f"    Re D3 = {np.real(delta3(Gs)):.3e}   A*A = {Anorm2(Gs):.6f}")

print("="*66)
print("R4  gamma_max = max modulus floor compatible with Re D3 <= 0 and G >= 0")
# equal-moduli analysis: det = 1 - 3g^2 + 2 g^3 cos(Phi),  need cos(Phi) <= 0
# REAL case: cos Phi = -1  ->  1 - 3g^2 - 2g^3 >= 0  ->  (2g-1)(g+1)^2 <= 0 -> g <= 1/2
# CPLX case: cos Phi = 0   ->  1 - 3g^2 >= 0        ->  g <= 1/sqrt(3)
best_r = 0.0; best_c = 0.0
for _ in range(4000000):
    rr = rng.uniform(0.3, 0.70, size=3)
    ph = rng.uniform(0, 2*np.pi, size=3)
    # real case: phases restricted to {0, pi}
    sgn = rng.integers(0,2,size=3)*2-1
    Gr = G_from(rr[0]*sgn[0], rr[1]*sgn[1], rr[2]*sgn[2])
    if np.real(delta3(Gr)) <= 0 and np.linalg.eigvalsh(Gr)[0] >= -1e-12:
        best_r = max(best_r, rr.min())
    Gc = G_from(rr[0]*np.exp(1j*ph[0]), rr[1]*np.exp(1j*ph[1]), rr[2]*np.exp(1j*ph[2]))
    if np.real(delta3(Gc)) <= 0 and np.linalg.eigvalsh(Gc)[0] >= -1e-12:
        best_c = max(best_c, rr.min())
print(f"    REAL  Gram (theta=0 Yang-Mills) : gamma_max found = {best_r:.6f}   exact = {0.5:.6f}")
print(f"    CPLX  Gram (phase available)    : gamma_max found = {best_c:.6f}   exact = {1/np.sqrt(3):.6f}")
Gopt = G_from(0.5, 0.5, -0.5)
print(f"    real optimum G=(+.5,+.5,-.5): spectrum = {np.round(np.linalg.eigvalsh(Gopt),12)}, A*A = {Anorm2(Gopt)}")
Gopt2 = G_from(np.exp(1j*np.pi/2)/np.sqrt(3),np.exp(1j*np.pi/2)/np.sqrt(3),np.exp(1j*np.pi/2)/np.sqrt(3))
print(f"    cplx optimum, all phases pi/2 : spectrum = {np.round(np.linalg.eigvalsh(Gopt2),9)}, Re D3 = {np.real(delta3(Gopt2)):.2e}")

print("="*66)
print("R5  strong coupling: three translates of a plaquette source, C(R) = K u^(4R)")
print("    triangle x1=0, x2=e1, x3=e2 : R12=R13=1, R23=2  (taxicab tube lengths)")
print(f"    {'u':>8} {'|G|~u^4':>12} {'Re D3 ~ u^16':>16} {'sign':>6} {'|G| >= 1/2 ?':>14}")
for u in [0.05,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.84,0.90]:
    g = u**4; d3 = u**16
    print(f"    {u:8.2f} {g:12.3e} {d3:16.3e} {'  +':>6} {str(g>=0.5):>14}")
print(f"    |G| = u^4 >= 1/2 requires u >= {0.5**0.25:.4f}  (weak-coupling end; expansion invalid)")
import numpy as np
rng = np.random.default_rng(20260909)

def spec_min(r, cosPhi):
    # G unit diagonal, |G_ij| = r_i, total phase Phi.  det = 1 - sum r^2 + 2 prod r cos Phi
    return 1 - (r**2).sum(axis=1) + 2*r.prod(axis=1)*cosPhi

print("="*70)
print("R4  gamma_max : largest modulus floor compatible with G>=0 and Re(D3)<=0")
N = 8_000_000
r  = rng.uniform(0.30, 0.75, size=(N,3))
mn = r.min(axis=1)

# --- REAL Gram (theta = 0 Yang-Mills): arg D3 in {0, pi}; premise forces cos Phi = -1
ok_r = (spec_min(r, -1.0) >= 0) & (r.max(axis=1) <= 1)
print(f"    REAL : gamma_max sampled = {mn[ok_r].max():.6f}    exact root of 2g^3+3g^2-1 = 1/2 = 0.500000")

# --- COMPLEX Gram: cos Phi may be 0 (the optimum, since larger cos Phi is forbidden)
ok_c = (spec_min(r, 0.0) >= 0) & (r.max(axis=1) <= 1)
print(f"    CPLX : gamma_max sampled = {mn[ok_c].max():.6f}    exact 1/sqrt(3)         = {1/np.sqrt(3):.6f}")

# --- full random check that no (r, Phi) with cos Phi <= 0 beats 1/sqrt(3)
Phi = rng.uniform(np.pi/2, 3*np.pi/2, size=N)
ok_f = (spec_min(r, np.cos(Phi)) >= 0)
print(f"    free-phase scan (cos Phi <= 0) : gamma_max = {mn[ok_f].max():.6f}   <= 1/sqrt(3) ? {mn[ok_f].max() <= 1/np.sqrt(3)+1e-6}")
print(f"    2g^3+3g^2-1 factors as (2g-1)(g+1)^2  ->  real root g = 1/2 exactly")

def G_from(a,b,c):
    return np.array([[1,a,np.conj(c)],[np.conj(a),1,b],[c,np.conj(b),1]],dtype=complex)
def A2(G): return 6-2*np.real(G[0,1]+G[1,2]+G[2,0])
Gr = G_from(.5,.5,-.5); Gc = G_from(*(3*[1j/np.sqrt(3)]))
print(f"    real optimum (+1/2,+1/2,-1/2): spectrum {np.round(np.linalg.eigvalsh(Gr),12)}  A*A = {A2(Gr):.4f}  D3 = {np.real(Gr[0,1]*Gr[1,2]*Gr[2,0]):+.4f}")
print(f"    cplx optimum (i/sqrt3 x3)    : spectrum {np.round(np.linalg.eigvalsh(Gc),12)}  A*A = {A2(Gc):.4f}  ReD3 = {np.real(Gc[0,1]*Gc[1,2]*Gc[2,0]):+.1e}")
print("    Fubini-Study angle floor: arccos(1/2) = 60.00 deg (real),  arccos(1/sqrt3) = 54.74 deg (complex)")

print("="*70)
print("R5  strong coupling, three translates of a plaquette source")
print("    leading character-expansion kernel  C(R) = K u^(4R),  K > 0,  u = c_f/c_0 -> 0")
print("    triangle x1=0, x2=e1, x3=e2  =>  R12 = R13 = 1, R23 = 2, total 4")
print(f"    {'u':>6}  {'|G_ij| ~ u^4':>14}  {'Re D3 ~ u^16':>14}  {'sign':>5}  {'|G| >= 1/2':>11}")
for u in [0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.84,0.9]:
    print(f"    {u:6.2f}  {u**4:14.4e}  {u**16:14.4e}  {'+':>5}  {str(u**4>=0.5):>11}")
print(f"    |G| = u^4 >= 1/2  requires  u >= {0.5**0.25:.4f}   (u -> 1 is the WEAK-coupling end)")
print(f"    Re D3 = K^3 u^16 > 0 strictly for every u in (0,1): premise violated at all strong couplings.")
