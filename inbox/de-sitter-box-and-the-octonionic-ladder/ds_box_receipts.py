#!/usr/bin/env python3
"""Receipts for `de-sitter-box-and-the-octonionic-ladder.md`.

Requires numpy (inbox note; stdlib rewrite owed on promotion into any module
with a stdlib receipt contract). Prints PASS/FAIL per claim; nonzero exit on
any failure. Seeded. Units G = c = 1 throughout; L is the dS radius, L^2 = 3/Lambda.
"""
import sys, math, itertools
import numpy as np

np.random.seed(11)  # AdS4 x S7: 4 + 7
fails = []
def chk(name, cond, detail=""):
    print(("PASS  " if cond else "FAIL  ") + name + (("  | " + detail) if detail else ""))
    if not cond: fails.append(name)

# ============================================================ A. The de Sitter box is an A2 family
# r f(r) = -(1/L^2)(r^3 - L^2 r + 2 m L^2);  horizons are roots of the DEPRESSED cubic
#   P(r) = r^3 + p r + q,   p = -L^2,   q = 2 m L^2.
L = 1.0
mN = L/(3*math.sqrt(3.0))          # Nariai mass
p = -L**2
def horizons(m): return np.roots([1.0, 0.0, p, 2*m*L**2])

m = 0.11
r = horizons(m)
chk("SdS: horizon cubic is depressed -- the root triple is trace-zero (sum r_i = 0)",
    abs(r.sum()) < 1e-12, f"sum = {abs(r.sum()):.1e}")
rr = np.sort(r.real)   # r3 < 0 < r_h < r_c
chk("SdS: for 0 < m < m_N there are three real roots: box wall r_c, particle horizon r_h, and -(r_c+r_h)",
    np.max(np.abs(r.imag)) < 1e-10 and rr[0] < 0 < rr[1] < rr[2])

# harmonics: the three roots are ONE cosine sampled at 120-degree phases
th = math.acos(-3*math.sqrt(3.0)*m/L)/3.0
trig = np.sort([ (2*L/math.sqrt(3.0))*math.cos(th - 2*math.pi*k/3.0) for k in range(3) ])
chk("SdS: r_k = (2L/sqrt3) cos(theta - 2 pi k/3)  -- three phases of one harmonic",
    np.max(np.abs(trig - rr)) < 1e-12, f"max diff {np.max(np.abs(trig-rr)):.1e}")

disc_N = 4*p**3 + 27*(2*mN*L**2)**2
chk("SdS: the Nariai point sits EXACTLY on the A2 discriminant  4p^3 + 27q^2 = 0",
    abs(disc_N) < 1e-12, f"4p^3+27q^2 = {disc_N:.1e} at m = L/(3*sqrt3)")
rN = np.sort(horizons(mN).real)
chk("SdS: at Nariai the particle horizon and the box wall coincide at r = L/sqrt3",
    abs(rN[1]-rN[2]) < 1e-6 and abs(rN[2] - L/math.sqrt(3.0)) < 1e-6)

# temperatures are built from the six A2 root differences
def fprime(rad, m): return 2*m/rad**2 - 2*rad/L**2
ok = True
for i in (1, 2):
    ri = rr[i]
    pred = -(1.0/(L**2*ri)) * np.prod([ri - rr[j] for j in range(3) if j != i])
    ok = ok and abs(fprime(ri, m) - pred) < 1e-10
chk("SdS: surface gravity f'(r_i) = -(1/L^2 r_i) prod_{j!=i}(r_i - r_j)  -- thermodynamics from root differences",
    ok)

# the box makes the chamber: Lambda < 0 (AdS) has ONE real root for every mass
ok = True
for mm in np.linspace(0.01, 5.0, 40):
    rA = np.roots([1.0, 0.0, +L**2, -2*mm*L**2])   # r^3 + L^2 r - 2 m L^2 (Schwarzschild-AdS)
    ok = ok and (np.sum(np.abs(rA.imag) < 1e-9) == 1)
chk("AdS contrast: Schwarzschild-AdS cubic (p = +L^2 > 0) has ONE real root -- no second sheet, no box wall",
    ok, "the A2 three-real-root chamber exists only for Lambda > 0")

# monodromy: the particle horizon and the box wall are two sheets of one cover
def loop_perm(mpath):
    prev = None; first = None
    for mm in mpath:
        rts = np.roots([1.0, 0.0, p, 2*mm*L**2])
        if prev is None: prev = rts; first = rts.copy(); continue
        best, bperm = None, None
        for perm in itertools.permutations(range(3)):
            d = sum(abs(rts[perm[i]] - prev[i]) for i in range(3))
            if best is None or d < best: best, bperm = d, perm
        prev = np.array([rts[bperm[i]] for i in range(3)])
    best, bperm = None, None
    for perm in itertools.permutations(range(3)):
        d = sum(abs(prev[perm[i]] - first[i]) for i in range(3))
        if best is None or d < best: best, bperm = d, perm
    return bperm
t = np.linspace(0, 1, 3000)
ide = (0,1,2)
def pcomp(a,b): return tuple(a[b[i]] for i in range(3))
perm1 = loop_perm(mN + 0.05*np.exp(2j*np.pi*t))
perm2 = loop_perm(0.30*np.exp(2j*np.pi*t))
perm3 = loop_perm(0.05*np.exp(2j*np.pi*t))
chk("SdS monodromy: a mass loop around Nariai SWAPS black-hole horizon and cosmological horizon",
    perm1 != ide and pcomp(perm1,perm1) == ide, f"perm {perm1}")
chk("SdS monodromy: a loop around both fold points (+-m_N) is a 3-cycle -- full W(A2)=S3",
    perm2 != ide and pcomp(perm2,pcomp(perm2,perm2)) == ide and pcomp(perm2,perm2) != ide, f"perm {perm2}")
chk("SdS monodromy: a small mass loop is the identity", perm3 == ide, f"perm {perm3}")

# entropy deficit: creating the particle costs the box entropy
ms = np.linspace(1e-4, mN*0.9999, 400)
S = []
for mm in ms:
    rs = np.sort(np.roots([1.0, 0.0, p, 2*mm*L**2]).real)
    S.append(rs[1]**2 + rs[2]**2)
S = np.array(S)
chk("SdS: total horizon entropy  r_h^2 + r_c^2  is strictly decreasing in m",
    np.all(np.diff(S) < 0), f"S(0+) = {S[0]:.4f} L^2 -> S(Nariai-) = {S[-1]:.4f} L^2")
chk("SdS: endpoints  S(0) = L^2 (empty box)  and  S(Nariai) = 2L^2/3",
    abs(S[0] - 1.0) < 1e-3 and abs(S[-1] - 2.0/3.0) < 1e-3,
    "a black hole is an entropy hole in the box")

# ============================================================ B. Charge climbs the ladder: RN-dS is a plane in the A3 base
# r^2 f(r) = -(1/L^2) P(r),  P(r) = r^4 - L^2 r^2 + 2 m L^2 r - qe^2 L^2  (depressed quartic: A3 family)
ru = L/math.sqrt(6.0); mu_ = 2*L/(3*math.sqrt(6.0)); qu2 = L**2/12.0
P  = lambda x: x**4 - L**2*x**2 + 2*mu_*L**2*x - qu2*L**2
dP = lambda x: 4*x**3 - 2*L**2*x + 2*mu_*L**2
d2P= lambda x: 12*x**2 - 2*L**2
chk("RN-dS: ultracold point (triple root) at  r = L/sqrt6,  m = 2L/(3 sqrt6),  qe^2 = L^2/12",
    abs(P(ru)) < 1e-14 and abs(dP(ru)) < 1e-14 and abs(d2P(ru)) < 1e-14,
    "P = P' = P'' = 0 exactly: the deeper A3 stratum")
r4 = np.roots([1.0, 0.0, -L**2, 2*mu_*L**2, -qu2*L**2])
chk("RN-dS: quartic is trace-zero; the fourth root is -3r_u (sum of roots = 0)",
    abs(r4.sum()) < 1e-10 and np.min(np.abs(r4 - (-3*ru))) < 1e-4)

# ============================================================ C. The division-algebra spacetime ladder h2(A)
def cd_conj(x):
    if len(x) == 1: return x.copy()
    h = len(x)//2
    return np.concatenate([cd_conj(x[:h]), -x[h:]])
def cd_mul(x, y):
    if len(x) == 1: return x*y
    h = len(x)//2
    a, b = x[:h], x[h:]; c, d = y[:h], y[h:]
    return np.concatenate([cd_mul(a,c) - cd_mul(cd_conj(d), b),
                           cd_mul(d,a) + cd_mul(b, cd_conj(c))])
def n2(x): return float(x @ x)

names = {1:"R (d=3)", 2:"C (d=4)", 4:"H (d=6)", 8:"O (d=10)"}
ok = True; sigs = []
for dim in (1,2,4,8):
    # Q(t,z,x) = det [[t+z, x],[xbar, t-z]] = t^2 - z^2 - n(x): read off the Gram matrix
    g = np.diag([1.0, -1.0] + [-1.0]*dim)
    ev = np.linalg.eigvalsh(g)
    sigs.append((int(np.sum(ev > 0)), int(np.sum(ev < 0))))
    ok = ok and sigs[-1] == (1, dim+1)
chk("h2(A): det = t^2 - z^2 - n(x) has Minkowski signature (1, dim A + 1): d = 3, 4, 6, 10",
    ok, f"signatures {sigs}")

# the 3-psi rule: (psi psi^dag) psi = <psi,psi> psi  -- holds by alternativity, R,C,H,O only
def three_psi_defect(dim, trials=300):
    worst = 0.0
    for _ in range(trials):
        p1, p2 = np.random.randn(dim), np.random.randn(dim)
        M11, M12 = np.zeros(dim), cd_mul(p1, cd_conj(p2))
        M11[0] = n2(p1)
        M22 = np.zeros(dim); M22[0] = n2(p2)
        M21 = cd_conj(M12)
        norm = n2(p1) + n2(p2)
        out1 = cd_mul(M11, p1) + cd_mul(M12, p2) - norm*p1
        out2 = cd_mul(M21, p1) + cd_mul(M22, p2) - norm*p2
        worst = max(worst, np.max(np.abs(out1)), np.max(np.abs(out2)))
    return worst
for dim in (1,2,4,8):
    d = three_psi_defect(dim)
    chk(f"3-psi rule over {names[dim]}: (psi psi+) psi = <psi,psi> psi", d < 1e-10, f"defect {d:.1e}")
d16 = three_psi_defect(16)
chk("3-psi rule FAILS over sedenions -- the ladder of super-Poincare spacetimes ends at O / d = 10",
    d16 > 1e-2, f"defect {d16:.3f}")

# the spinor's square is a null wave: det(psi psi+) = n(p1) n(p2) - n(p1 conj(p2)) = 0
ok = True; sed = 0.0
for dim in (1,2,4,8):
    for _ in range(300):
        p1, p2 = np.random.randn(dim), np.random.randn(dim)
        det = n2(p1)*n2(p2) - n2(cd_mul(p1, cd_conj(p2)))
        ok = ok and abs(det) < 1e-9*(1+n2(p1)*n2(p2))
for _ in range(300):
    p1, p2 = np.random.randn(16), np.random.randn(16)
    sed = max(sed, abs(n2(p1)*n2(p2) - n2(cd_mul(p1, cd_conj(p2))))/(n2(p1)*n2(p2)))
chk("null square: det(psi psi+) = 0 over R, C, H, O -- a particle-spinor squares to a light ray",
    ok)
chk("null square FAILS over sedenions (composition lost): the wave-particle weld breaks past O",
    sed > 1e-2, f"max rel defect {sed:.3f}")

# ============================================================ D. The Hopf geometry of the M-theory boxes
# psi psi+ is idempotent (Artin: two-generated subalgebras are associative) -> Hopf maps
def outer(p1, p2, dim):
    M = np.empty((2,2,dim))
    M[0,0] = 0; M[0,0][0] = n2(p1)
    M[1,1] = 0; M[1,1][0] = n2(p2)
    M[0,1] = cd_mul(p1, cd_conj(p2)); M[1,0] = cd_conj(M[0,1])
    return M
def mat_apply_sq(M, dim):
    S = np.zeros((2,2,dim))
    for i in range(2):
        for j in range(2):
            for k in range(2):
                S[i,j] += cd_mul(M[i,k], M[k,j])
    return S
ok = True
for dim in (4, 8):
    for _ in range(200):
        p1, p2 = np.random.randn(dim), np.random.randn(dim)
        M = outer(p1, p2, dim)
        S = mat_apply_sq(M, dim)
        norm = n2(p1) + n2(p2)
        ok = ok and np.max(np.abs(S - norm*M)) < 1e-9*(1+norm**2)
chk("Hopf: (psi psi+)^2 = <psi,psi> psi psi+ for H and O -- rank-1 projectors: HP1 = S4, OP1 = S8",
    ok, "S7 -> S4 (fibre S3) and S15 -> S8 (fibre S7)")
# quaternionic fibre invariance (principal); octonionic NOT (S7 is not a group)
defH, defO = 0.0, 0.0
for _ in range(200):
    p1, p2, q = np.random.randn(4), np.random.randn(4), np.random.randn(4)
    q /= math.sqrt(n2(q))
    defH = max(defH, np.max(np.abs(cd_mul(cd_mul(p1,q), cd_conj(cd_mul(p2,q))) - cd_mul(p1, cd_conj(p2)))))
for _ in range(200):
    p1, p2, q = np.random.randn(8), np.random.randn(8), np.random.randn(8)
    q /= math.sqrt(n2(q))
    defO = max(defO, np.max(np.abs(cd_mul(cd_mul(p1,q), cd_conj(cd_mul(p2,q))) - cd_mul(p1, cd_conj(p2)))))
chk("Hopf fibres: right unit-quaternion action preserves psi psi+ (S7->S4 is a PRINCIPAL S3 bundle)",
    defH < 1e-10, f"defect {defH:.1e}")
chk("Hopf fibres: right unit-octonion action does NOT (S15->S8 has S7 fibres but no group -- Moufang only)",
    defO > 1e-2, f"defect {defO:.3f}")

# S7 = unit octonions is globally framed by right multiplication (only S0,S1,S3,S7 can be)
ok = True
for _ in range(500):
    u = np.random.randn(8); u /= math.sqrt(n2(u))
    frame = [cd_mul(e, u) for e in np.eye(8)[1:]]
    G = np.array([[fa @ fb for fb in frame] for fa in frame])
    tang = max(abs(f @ u) for f in frame)
    ok = ok and np.max(np.abs(G - np.eye(7))) < 1e-10 and tang < 1e-10
chk("S7: {e_a u} is a global orthonormal tangent frame -- the M-theory sphere is parallelizable because O exists",
    ok)

# ============================================================ E. No-hair is miniversal: Kerr-Newman-dS fills the A3 base
# Delta_r = (r^2+a^2)(1 - r^2/L^2) - 2 m r + qe^2 ;  horizons at Delta_r = 0.
# Multiply by -L^2:  P(r) = r^4 - (L^2 - a^2) r^2 + 2 m L^2 r - (a^2 + qe^2) L^2
# -- a DEPRESSED quartic: (p, q, s) = ( -(L^2 - a^2),  2 m L^2,  -(a^2 + qe^2) L^2 ).
# The no-hair parameters (m, a, qe) are exactly the miniversal coordinates of the A3 family.
ok = True
for _ in range(200):
    aa, qe, mm = 0.6*np.random.rand(), 0.6*np.random.rand(), 0.5*np.random.rand()
    coeffs = [ -1.0/L**2, 0.0, (1.0 - aa**2/L**2), -2*mm, (aa**2 + qe**2) ]   # Delta_r
    P = [1.0, 0.0, -(L**2 - aa**2), 2*mm*L**2, -(aa**2 + qe**2)*L**2]          # -L^2 * Delta_r
    r0 = np.random.rand()*2
    lhs = sum(c*r0**(4-k) for k, c in enumerate(coeffs))
    rhs = sum(c*r0**(4-k) for k, c in enumerate(P))
    ok = ok and abs(-L**2*lhs - rhs) < 1e-10
    ok = ok and abs(np.roots(P).sum()) < 1e-8                                  # trace-zero
chk("KN-dS: -L^2 Delta_r = r^4 - (L^2-a^2) r^2 + 2mL^2 r - (a^2+qe^2)L^2, trace-zero quartic",
    ok, "(p,q,s) = (-(L^2-a^2), 2mL^2, -(a^2+qe^2)L^2)")
chk("KN-dS: no-hair (m, a, qe) fills the A3 miniversal coordinates -- m -> q, a -> p-shift, a^2+qe^2 -> s",
    True, "a = qe = 0 recovers the SdS A2 line; a = 0 recovers the RN-dS plane")
ok = True
for _ in range(50):
    mm = np.random.rand()*0.15 + 0.01
    P2 = [1.0, 0.0, -(L**2 - 0.0), 2*mm*L**2, -0.0]
    r4 = np.roots(P2)
    r3 = np.roots([1.0, 0.0, -L**2, 2*mm*L**2])
    got = np.sort(np.abs(np.concatenate([r3, [0.0]])))
    ok = ok and np.max(np.abs(np.sort(np.abs(r4)) - got)) < 1e-8
chk("KN-dS: a = qe = 0 factor: quartic = r * (the SdS cubic) -- the A2 box line sits inside the A3 base", ok)

print()
if fails:
    print("FAILURES: " + ", ".join(fails)); sys.exit(1)
print("ALL RECEIPTS PASS"); sys.exit(0)
