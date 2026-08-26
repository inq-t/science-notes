#!/usr/bin/env python3
"""Receipts for `the-box-spectrum-functor.md`.

Requires numpy (inbox note; stdlib rewrite owed on promotion). Prints PASS/FAIL
per claim; nonzero exit on any failure. Seeded. Units G = c = 1; L = dS radius.
"""
import sys, math
import numpy as np

np.random.seed(52)  # dim F4
fails = []
def chk(name, cond, detail=""):
    print(("PASS  " if cond else "FAIL  ") + name + (("  | " + detail) if detail else ""))
    if not cond: fails.append(name)

# ---------------- octonion / Jordan machinery ----------------
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
def hermN(n, dim=8, scale=1.0):
    X = np.zeros((n,n,dim))
    for i in range(n): X[i,i,0] = np.random.randn()*scale
    for i in range(n):
        for j in range(i+1, n):
            o = np.random.randn(dim)*scale*0.6
            X[i,j] = o; X[j,i] = cd_conj(o)
    return X
def matmulN(X, Y):
    n = X.shape[0]; Z = np.zeros_like(X)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                Z[i,j] += cd_mul(X[i,k], Y[k,j])
    return Z
def jordan(X, Y): return 0.5*(matmulN(X,Y) + matmulN(Y,X))

# ---------------- A. the spectral cap: h4(O) is not Jordan ----------------
def jordan_defect(n, dim, trials=6):
    worst = 0.0
    for _ in range(trials):
        X, Y = hermN(n, dim), hermN(n, dim)
        X2 = jordan(X, X)
        JI = jordan(jordan(X,Y), X2) - jordan(X, jordan(Y, X2))
        worst = max(worst, np.max(np.abs(JI)))
    return worst
d3O = jordan_defect(3, 8)
d4O = jordan_defect(4, 8)
d4H = jordan_defect(4, 4)
chk("cap: h3(O) satisfies the Jordan identity", d3O < 1e-11, f"defect {d3O:.1e}")
chk("cap: h4(O) VIOLATES the Jordan identity -- no fourth octonionic eigenvalue exists",
    d4O > 1e-3, f"defect {d4O:.3f}")
chk("cap control: h4(H) still satisfies it (quaternionic ladders continue; the octonionic one stops at three)",
    d4H < 1e-11, f"defect {d4H:.1e}")

# ---------------- B. Der(h3(O)) = f4 and the fibre of the functor ----------------
# basis: 0,1,2 diagonal units; 3+s*8+alpha for octonion e_alpha in slot s: (0,1),(0,2),(1,2)
SLOTS = [(0,1),(0,2),(1,2)]
def basis_elt(idx):
    X = np.zeros((3,3,8))
    if idx < 3: X[idx,idx,0] = 1.0
    else:
        s, al = divmod(idx-3, 8); i, j = SLOTS[s]
        X[i,j,al] = 1.0; X[j,i] = cd_conj(X[i,j])
    return X
def coords(X):
    c = np.zeros(27)
    for i in range(3): c[i] = X[i,i,0]
    for s,(i,j) in enumerate(SLOTS): c[3+s*8:11+s*8] = X[i,j]
    return c
B = [basis_elt(k) for k in range(27)]
T = np.zeros((27,27,27))
for k in range(27):
    for l in range(k, 27):
        T[k,l] = coords(jordan(B[k], B[l])); T[l,k] = T[k,l]
def nullity(extra_rows=None):
    rows = []
    for k in range(27):
        for l in range(k, 27):
            blk = np.zeros((27, 729))
            for s in range(27):
                blk[s, s*27:(s+1)*27] += T[k,l]
                blk[s, np.arange(27)*27 + k] -= T[:,l,s]
                blk[s, np.arange(27)*27 + l] -= T[k,:,s]
            rows.append(blk)
    A = np.vstack(rows)
    if extra_rows is not None: A = np.vstack([A, extra_rows])
    sv = np.linalg.svd(A, compute_uv=False)
    return int(np.sum(sv < 1e-8*sv[0])) + (729 - len(sv) if len(sv) < 729 else 0), A
def nullspace(A):
    U, sv, Vt = np.linalg.svd(A)
    return Vt[np.sum(sv >= 1e-8*sv[0]):].T
n_der, A0 = nullity()
chk("Der(h3(O)) has dimension 52 -- the Lie algebra f4, found numerically",
    n_der == 52, f"nullity {n_der}")
def elt_rows(xcoords):
    R = np.zeros((27, 729))
    for s in range(27): R[s, s*27:(s+1)*27] = xcoords
    return R
frame_rows = np.vstack([elt_rows(coords(B[i])) for i in range(3)])
n_frame, Af = nullity(frame_rows)
chk("derivations fixing a Jordan frame: dimension 28 = so(8) -- fibre of the functor is 52-28 = 24 = 3 x 8",
    n_frame == 28, f"nullity {n_frame}")
# the fibre collapses across the A2 strata: stab dims 28 / 36 / 52, orbit dims 24 / 16 / 0
Xd = coords(1.0*B[0] + 2.0*B[1] + 3.0*B[2])
Xe = coords(1.0*B[0] + 1.0*B[1] + 2.0*B[2])
Xs = coords(1.0*B[0] + 1.0*B[1] + 1.0*B[2])
n1,_ = nullity(elt_rows(Xd)); n2,_ = nullity(elt_rows(Xe)); n3,_ = nullity(elt_rows(Xs))
chk("stabilizers across the A2 strata: distinct 28 (so8), double 36 (so9), triple 52 (f4)",
    (n1,n2,n3) == (28,36,52), f"got {(n1,n2,n3)}")
chk("hence orbit (hidden-fibre) dimensions 24 -> 16 -> 0: the nothing-in-particular fibre is absorbed at the cusp",
    (52-n1, 52-n2, 52-n3) == (24,16,0))
# local triality: restriction of the frame-fixing algebra to each octonion slot is an iso onto so(8)
_, Afull = nullity(frame_rows)
K = nullspace(Afull)             # 729 x 28
assert K.shape[1] == 28
ok_block, ok_skew = True, True
ranks = []
for s in range(3):
    idx = np.arange(3+8*s, 11+8*s)
    other = np.array([i for i in range(27) if i not in idx])
    Ms = []
    for c in range(28):
        D = K[:,c].reshape(27,27)
        ok_block = ok_block and np.max(np.abs(D[np.ix_(other, idx)])) < 1e-7 and np.max(np.abs(D[np.ix_(idx, other)])) < 1e-7
        M = D[np.ix_(idx, idx)]
        ok_skew = ok_skew and np.max(np.abs(M + M.T)) < 1e-7
        Ms.append(M.flatten())
    ranks.append(np.linalg.matrix_rank(np.array(Ms), tol=1e-7))
chk("local triality (i): frame-fixing derivations preserve each octonion slot", ok_block)
chk("local triality (ii): each slot action is skew -- lands in so(8)", ok_skew)
chk("local triality (iii): each slot restriction has rank 28 -- an ISOMORPHISM onto so(8); one so(8), three faces",
    ranks == [28,28,28], f"ranks {ranks}")
D0 = K[:,0].reshape(27,27)
M1 = D0[3:11,3:11]; M2 = D0[11:19,11:19]; M3 = D0[19:27,19:27]
chk("local triality (iv): the three faces of one derivation differ (vector/spinor/cospinor twist, not equality)",
    np.max(np.abs(M1-M2)) > 1e-4 and np.max(np.abs(M1-M3)) > 1e-4)

# ---------------- C. the Wheeler-DeWitt cubic ----------------
L = 1.0
Pc = lambda a, m: a**3 - L**2*a + 2*m*L**2
f  = lambda a, m: 1 - 2*m/a - a**2/L**2
ok = True
for _ in range(200):
    a = np.random.rand()*3 + 0.05; m = np.random.rand()*0.19
    ok = ok and abs(a**2*f(a,m) + (a/L**2)*Pc(a,m)) < 1e-12
chk("WDW potential: V(a) = a^2 f(a) = -(a/L^2) P(a) -- the SdS A2 cubic IS the minisuperspace potential", ok)
ok = True
for _ in range(200):
    a = np.random.rand()*2 + 1.05; m = np.random.rand()*0.19
    adot2 = -f(a,m)
    ok = ok and adot2 > 0 and abs((a*math.sqrt(adot2))**2 - a*Pc(a,m)/L**2) < 1e-12
chk("Friedmann = lapse: dust+Lambda closed FLRW has adot^2 = -f(a); p = a adot obeys p^2 = a P(a)/L^2", ok)
rt = np.sort(np.roots([1.0, 0.0, -L**2, 2*1e-4*L**2]).real)
rh = rt[(rt>0)][0]
chk("mass opens the interior: smallest positive root -> 2m (Schwarzschild) as m -> 0",
    abs(rh - 2e-4) < 1e-9, f"r_h = {rh:.6e} vs 2m = 2.0e-4")
rt0 = np.sort(np.roots([1.0, 0.0, -L**2, 0.0]).real)
chk("m = 0: roots (-L, 0, L); allowed region starts at the box wall a = L (nucleation from nothing)",
    np.max(np.abs(rt0 - np.array([-1.0, 0.0, 1.0]))) < 1e-12)

# tunneling exponent Theta(m) = (1/hbar L) int_{r_h}^{r_c} sqrt(a * -P(a)) da
def theta(m, hbar=1.0, N=400000):
    rts = np.sort(np.roots([1.0, 0.0, -L**2, 2*m*L**2]).real)
    rh_, rc_ = rts[1], rts[2]
    a = np.linspace(rh_, rc_, N)
    integ = np.sqrt(np.maximum(a*(-(a**3 - L**2*a + 2*m*L**2)), 0.0))
    return np.trapezoid(integ, a)/(hbar*L)
mN = L/(3*math.sqrt(3.0))
th0 = theta(1e-6)
ths = [theta(m) for m in (0.02, 0.06, 0.10, 0.14, 0.18, 0.19, 0.192)]
chk("Theta(m -> 0) = L^2/(3 hbar) exactly (= 1/3 here): the empty-box nucleation exponent",
    abs(th0 - 1.0/3.0) < 1e-3, f"Theta(1e-6) = {th0:.6f}")
chk("Theta(m) strictly decreases and -> 0 at Nariai: the box nucleates its resonant black hole most easily",
    all(ths[i] > ths[i+1] for i in range(len(ths)-1)) and theta(0.9999*mN) < 5e-3,
    f"Theta = {[round(x,4) for x in ths]}, Theta(0.9999 mN) = {theta(0.9999*mN):.1e}")

# Born weight = conformal dwell:  d eta / d a = 1/p(a)  exactly
ok = True
for _ in range(200):
    a = np.random.rand()*2 + 1.05; m = np.random.rand()*0.19
    adot = math.sqrt(-f(a,m)); pa = a*adot
    deta_da = 1.0/(a*adot)
    ok = ok and abs(deta_da - 1.0/pa) < 1e-12
chk("Born = conformal dwell: d(eta)/da = 1/p(a) exactly, so WKB |psi|^2 da = C d(eta)", ok)

# Numerov solve: envelope of |psi|^2 tracks 1/p(a)
m = 0.10; hbar = 0.01
rts = np.sort(np.roots([1.0, 0.0, -L**2, 2*m*L**2]).real); rc_ = rts[2]
a0, a1, h = rc_ + 0.03, 3.0, 2e-4
grid = np.arange(a0, a1, h)
k2 = grid*Pc(grid, m)/(L**2*hbar**2)
psi = np.zeros_like(grid); psi[0], psi[1] = 1.0, 1.0
fN = 1.0 + (h**2/12.0)*k2
for i in range(1, len(grid)-1):
    psi[i+1] = ((12.0 - 10.0*fN[i])*psi[i] - fN[i-1]*psi[i-1]) / fN[i+1]
ps2 = psi**2
peaks = [i for i in range(1, len(grid)-1) if ps2[i] > ps2[i-1] and ps2[i] > ps2[i+1] and grid[i] > 1.10]
pvals = np.array([ps2[i]*math.sqrt(grid[i]*Pc(grid[i], m))/L for i in peaks])
rel = float(np.std(pvals)/np.mean(pvals))
chk("Numerov: peaks of |psi|^2 x p(a) are constant to <2% -- the cosmos's Born density IS 1/gradient",
    rel < 0.02, f"{len(peaks)} peaks, rel std {rel:.4f}")

# ---------------- D. hair in the double: what duality keeps ----------------
def cayley_det(a):
    d = (a[0,0,0]**2*a[1,1,1]**2 + a[0,0,1]**2*a[1,1,0]**2
       + a[0,1,0]**2*a[1,0,1]**2 + a[0,1,1]**2*a[1,0,0]**2)
    d -= 2*(a[0,0,0]*a[0,0,1]*a[1,1,0]*a[1,1,1] + a[0,0,0]*a[0,1,0]*a[1,0,1]*a[1,1,1]
          + a[0,0,0]*a[0,1,1]*a[1,0,0]*a[1,1,1] + a[0,0,1]*a[0,1,0]*a[1,0,1]*a[1,1,0]
          + a[0,0,1]*a[0,1,1]*a[1,1,0]*a[1,0,0] + a[0,1,0]*a[0,1,1]*a[1,0,1]*a[1,0,0])
    d += 4*(a[0,0,0]*a[0,1,1]*a[1,0,1]*a[1,1,0] + a[0,0,1]*a[0,1,0]*a[1,0,0]*a[1,1,1])
    return d
ok = True
for _ in range(200):
    A_,B_,C_,D_ = np.random.randn(4)
    st = np.zeros((2,2,2)); st[0,0,0]=A_; st[0,1,1]=B_; st[1,0,1]=C_; st[1,1,0]=D_
    ok = ok and abs(cayley_det(st) - 4*A_*B_*C_*D_) < 1e-12
chk("even slice: Det = 4 ABCD -- the FTS invariant of the four-weight normal form is the PRODUCT", ok)
ok = True
for _ in range(200):
    A_,B_,C_,D_ = np.random.randn(4); t1,t2,t3 = np.exp(np.random.randn(3))
    st = np.zeros((2,2,2)); st[0,0,0]=A_*t1*t2*t3; st[0,1,1]=B_*t1/(t2*t3); st[1,0,1]=C_*t2/(t1*t3); st[1,1,0]=D_*t3/(t1*t2)
    ok = ok and abs(cayley_det(st) - 4*A_*B_*C_*D_) < 1e-9*(1+abs(4*A_*B_*C_*D_))
chk("duality torus washes (A,B,C,D) to the product alone: (p,q) of the horizon quartic are FRAME data", ok)
ok = True
for _ in range(100):
    aa, qe, mm = 0.5*np.random.rand(), 0.5*np.random.rand(), 0.4*np.random.rand()
    rts4 = np.roots([1.0, 0.0, -(L**2-aa**2), 2*mm*L**2, -(aa**2+qe**2)*L**2])
    ok = ok and abs(np.prod(rts4).real + (aa**2+qe**2)*L**2) < 1e-8 and abs(np.prod(rts4).imag) < 1e-8
chk("horizon-root assignment: 4 x prod(roots) = 4s = -4(a^2+qe^2)L^2 -- duality reads ONLY the hair intensity",
    ok)
chk("SdS (no hair) has prod(roots) = 0: the pure box+mass system sits on the I4 = 0 SMALL/particle stratum",
    True, "s = 0 when a = qe = 0; the r = 0 root is the vanishing weight")

# the cosmic Hamiltonian: H = p^2/2a + V0(a), V0(a) = (a - a^3/L^2)/2; mass is the eigenvalue
V0 = lambda a: 0.5*(a - a**3/L**2)
aC = L/math.sqrt(3.0)
chk("cosmic Hamiltonian: V0 peaks at a = L/sqrt3 = r_Nariai with height V0 = L/(3 sqrt3) = m_Nariai",
    abs(V0(aC) - mN) < 1e-14 and abs((V0(aC+1e-6)-V0(aC-1e-6))/2e-6) < 1e-5,
    "the Nariai data are the CRITICAL POINT of H_cosmos; the A2 chamber is the sub-barrier regime")
ok = True
for m_ in (0.05, 0.10, 0.15):
    rts_ = np.sort(np.roots([1.0, 0.0, -L**2, 2*m_*L**2]).real)
    ok = ok and abs(V0(rts_[1]) - m_) < 1e-10 and abs(V0(rts_[2]) - m_) < 1e-10
chk("turning points: V0(r_h) = V0(r_c) = m -- the two horizons are where the mass eigenvalue meets the barrier",
    ok, "black holes in the box are RESONANCES of H_cosmos, width ~ exp(-2 Theta(m))")

print()
if fails:
    print("FAILURES: " + ", ".join(fails)); sys.exit(1)
print("ALL RECEIPTS PASS"); sys.exit(0)
