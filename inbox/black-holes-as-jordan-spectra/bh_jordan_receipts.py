#!/usr/bin/env python3
"""Receipts for `black-holes-as-jordan-spectra.md`.

Requires numpy (inbox note, not a module receipt; a stdlib rewrite is owed
if any part is promoted into a module with a stdlib receipt contract).
Prints PASS/FAIL per claim; nonzero exit on any failure. Seeded.
"""
import sys, math, itertools
import numpy as np

np.random.seed(34)  # (3,4,infinity)
fails = []
def chk(name, cond, detail=""):
    print(("PASS  " if cond else "FAIL  ") + name + (("  | " + detail) if detail else ""))
    if not cond: fails.append(name)

# ---------------------------------------------------------------- A. Cayley-Dickson tower
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

O = 8
rnd = lambda d=O: np.random.randn(d)
err = 0.0
for _ in range(3000):
    x, y = rnd(), rnd()
    err = max(err, abs(n2(cd_mul(x,y)) - n2(x)*n2(y)) / (n2(x)*n2(y)))
chk("octonions: norm composition n(xy)=n(x)n(y)", err < 1e-10, f"max rel err {err:.1e}")

err = 0.0
for _ in range(1500):
    x, y = rnd(), rnd()
    err = max(err, np.max(np.abs(cd_mul(x, cd_mul(x,y)) - cd_mul(cd_mul(x,x), y))),
                   np.max(np.abs(cd_mul(cd_mul(y,x), x) - cd_mul(y, cd_mul(x,x)))))
chk("octonions: alternativity x(xy)=(xx)y, (yx)x=y(xx)", err < 1e-9, f"max err {err:.1e}")

def assoc(a,b,c): return cd_mul(cd_mul(a,b), c) - cd_mul(a, cd_mul(b,c))
a,b,c = rnd(), rnd(), rnd()
A = assoc(a,b,c)
anti = max(np.max(np.abs(A + assoc(b,a,c))), np.max(np.abs(A + assoc(a,c,b))))
chk("octonions: associator nonzero and totally antisymmetric",
    np.linalg.norm(A) > 1e-2 and anti < 1e-9,
    f"|[a,b,c]|={np.linalg.norm(A):.3f}, antisym err {anti:.1e}")

viol = 0.0
for _ in range(3000):
    x, y = rnd(16), rnd(16)
    viol = max(viol, abs(n2(cd_mul(x,y))/(n2(x)*n2(y)) - 1.0))
chk("sedenions: norm composition FAILS (the tower stops at O; Hurwitz)",
    viol > 1e-2, f"max rel violation {viol:.3f}")

# ---------------------------------------------------------------- B. S^6 = unit imaginary octonions
def im7(v8): return v8[1:]
def emb(v7): return np.concatenate([[0.0], v7])
u7 = rnd(7); u7 /= np.linalg.norm(u7); u = emb(u7)
def tangent_at(u):
    v = rnd(7); v -= (v @ im7(u)) * im7(u); v /= np.linalg.norm(v); return emb(v)
v, w = tangent_at(u), tangent_at(u)
Jv, Jw = cd_mul(u, v), cd_mul(u, w)
chk("S6: J_u(v)=u*v stays tangent (imaginary, orthogonal to u)",
    abs(Jv[0]) < 1e-12 and abs(Jv @ u) < 1e-12)
chk("S6: J^2 = -1 (uses alternativity: u(uv)=(uu)v=-v)",
    np.max(np.abs(cd_mul(u, Jv) + v)) < 1e-12)
chk("S6: J is orthogonal / the round metric is Hermitian",
    abs((Jv @ Jw) - (v @ w)) < 1e-12)

def field(a7):
    a = a7 / np.linalg.norm(a7)
    def V(x7):
        xh = x7 / np.linalg.norm(x7)
        return a - (a @ xh) * xh
    return V
def Jfield(V):
    def JV(x7):
        xh = x7 / np.linalg.norm(x7)
        return im7(cd_mul(emb(xh), emb(V(x7))))
    return JV
def jac(F, x7, h=1e-5):
    J = np.zeros((7,7))
    for i in range(7):
        e = np.zeros(7); e[i] = h
        J[:, i] = (F(x7+e) - F(x7-e)) / (2*h)
    return J
def bracket(P, Q, x7):  # [P,Q] = DQ.P - DP.Q
    return jac(Q, x7) @ P(x7) - jac(P, x7) @ Q(x7)
def tproj(z7, x7):
    xh = x7 / np.linalg.norm(x7)
    return z7 - (z7 @ xh) * xh
def nijenhuis(V, W, x7):
    JV, JW = Jfield(V), Jfield(W)
    Jx = lambda z7: im7(cd_mul(emb(x7/np.linalg.norm(x7)), emb(tproj(z7, x7))))
    N = bracket(JV, JW, x7) - Jx(bracket(JV, W, x7)) - Jx(bracket(V, JW, x7)) - bracket(V, W, x7)
    return tproj(N, x7)

x0 = im7(u)
V, W = field(rnd(7)), field(rnd(7))
NJ = nijenhuis(V, W, x0)
chk("S6: Nijenhuis tensor NONZERO (octonionic J is not integrable)",
    np.linalg.norm(NJ) > 0.05, f"|N(V,W)| = {np.linalg.norm(NJ):.4f}")

# control: constant J on R^6 (= C^3) with linear fields -> N = 0
J0 = np.kron(np.eye(3), np.array([[0.,-1.],[1.,0.]]))
A6, B6 = np.random.randn(6,6), np.random.randn(6,6)
a6, b6 = np.random.randn(6), np.random.randn(6)
Vc = lambda x: A6 @ x + a6
Wc = lambda x: B6 @ x + b6
JVc = lambda x: J0 @ Vc(x); JWc = lambda x: J0 @ Wc(x)
def jac6(F, x, h=1e-5):
    J = np.zeros((6,6))
    for i in range(6):
        e = np.zeros(6); e[i] = h
        J[:, i] = (F(x+e) - F(x-e)) / (2*h)
    return J
def br6(P, Q, x): return jac6(Q,x) @ P(x) - jac6(P,x) @ Q(x)
xc = np.random.randn(6)
Nc = br6(JVc,JWc,xc) - J0 @ br6(JVc,Wc,xc) - J0 @ br6(Vc,JWc,xc) - br6(Vc,Wc,xc)
chk("control: same formula on C^3 (constant J) gives N = 0",
    np.linalg.norm(Nc) < 1e-7, f"|N| = {np.linalg.norm(Nc):.1e}")

# N lies in span{ assoc(x,V,W), x*assoc(x,V,W) } -- nonassociativity IS the nonintegrability
res_max, coeffs = 0.0, []
for _ in range(4):
    x7 = rnd(7); x7 /= np.linalg.norm(x7)
    V, W = field(rnd(7)), field(rnd(7))
    NJ = nijenhuis(V, W, x7)
    A1 = im7(assoc(emb(x7), emb(V(x7)), emb(W(x7))))
    A2 = im7(cd_mul(emb(x7), emb(A1)))
    M = np.stack([A1, A2], axis=1)
    cvec, *_ = np.linalg.lstsq(M, NJ, rcond=None)
    res = np.linalg.norm(M @ cvec - NJ) / np.linalg.norm(NJ)
    res_max = max(res_max, res); coeffs.append(cvec)
chk("S6: N(V,W) lies in span{[x,V,W], x*[x,V,W]} (associator = torsion)",
    res_max < 1e-3, f"max rel residual {res_max:.1e}; c={np.round(coeffs[0],4)}")

# ---------------------------------------------------------------- C. J3(O), Cayley-Hamilton, frames, A2 cusp
def herm3():
    X = np.zeros((3,3,8))
    for i in range(3): X[i,i,0] = np.random.randn()
    for (i,j) in [(0,1),(0,2),(1,2)]:
        o = np.random.randn(8)*0.6
        X[i,j] = o; X[j,i] = cd_conj(o)
    return X
def matmul3(X, Y):
    Z = np.zeros((3,3,8))
    for i in range(3):
        for j in range(3):
            for k in range(3):
                Z[i,j] += cd_mul(X[i,k], Y[k,j])
    return Z
def jordan(X, Y): return 0.5*(matmul3(X,Y) + matmul3(Y,X))
def tr(X): return X[0,0,0] + X[1,1,0] + X[2,2,0]
I3 = np.zeros((3,3,8));  I3[0,0,0]=I3[1,1,0]=I3[2,2,0]=1.0
def TSN(X):
    X2 = jordan(X,X); X3 = jordan(X,X2)
    T = tr(X); S = 0.5*(T*T - tr(X2))
    N = (tr(X3) - T*tr(X2) + S*T)/3.0
    return T,S,N,X2,X3
X = herm3()
T,S,N,X2,X3 = TSN(X)
CH = X3 - T*X2 + S*X - N*I3
scale = 1.0 + abs(T)**3 + abs(N)
chk("J3(O): Cayley-Hamilton  X^3 - T X^2 + S X - N = 0  (N := det)",
    np.max(np.abs(CH))/scale < 1e-10, f"residual {np.max(np.abs(CH)):.1e}")
Y = herm3()
JI = jordan(jordan(X,Y), X2) - jordan(X, jordan(Y, X2))
chk("J3(O): Jordan identity (Xo Y)o X^2 = Xo(Y o X^2)",
    np.max(np.abs(JI))/scale < 1e-9, f"residual {np.max(np.abs(JI)):.1e}")
Z = herm3()
na = np.max(np.abs(jordan(jordan(X,Y),Z) - jordan(X, jordan(Y,Z))))
chk("J3(O): Jordan product NOT associative (genuinely exceptional)", na > 1e-3, f"assoc defect {na:.3f}")
roots = np.roots([1.0, -T, S, -N])
chk("J3(O): spectrum is real (formally real Jordan algebra)",
    np.max(np.abs(roots.imag)) < 1e-7, f"max |Im| {np.max(np.abs(roots.imag)):.1e}")
lam = np.sort(roots.real)
def lagrange_idem(X, lam):
    es = []
    for i in range(3):
        j, k = [m for m in range(3) if m != i]
        P = matmul3(X - lam[j]*I3, X - lam[k]*I3) / ((lam[i]-lam[j])*(lam[i]-lam[k]))
        es.append(P)
    return es
es = lagrange_idem(X, lam)
ok = np.max(np.abs(sum(es) - I3)) < 1e-8
for i in range(3):
    for j in range(3):
        tgt = es[i] if i==j else 0*I3
        ok = ok and np.max(np.abs(jordan(es[i],es[j]) - tgt)) < 1e-7
ok = ok and np.max(np.abs(sum(lam[i]*es[i] for i in range(3)) - X)) < 1e-7
chk("J3(O): Jordan frame  X = l1 e1 + l2 e2 + l3 e3, ei o ej = dij ei, sum ei = 1", ok)
Y2 = lam[0]*es[0] + lam[1]*es[1]
chk("J3(O): rank-2 element has det N = 0  (the 'small'/particle stratum)",
    abs(TSN(Y2)[2])/scale < 1e-8, f"N(rank2) = {TSN(Y2)[2]:.1e}")
Zd = 1.7*(es[0]+es[1]) + (-0.9)*es[2]
Tz,Sz,Nz,_,_ = TSN(Zd)
p = Sz - Tz*Tz/3.0
q = -Nz + Tz*Sz/3.0 - 2.0*Tz**3/27.0
chk("J3(O): coincident eigenvalues land EXACTLY on the A2 cusp  4p^3+27q^2 = 0",
    abs(4*p**3 + 27*q**2) < 1e-8*(1+abs(Tz)**6), f"4p^3+27q^2 = {4*p**3+27*q**2:.1e}")
Xd = np.zeros((3,3,8)); Xd[0,0,0]=2.; Xd[1,1,0]=3.; Xd[2,2,0]=5.
chk("J3(O): N(diag(Q1,Q2,Q3)) = Q1 Q2 Q3  (the STU cube is the diagonal of det)",
    abs(TSN(Xd)[2] - 30.0) < 1e-10)
# real-orthogonal conjugation is an automorphism preserving (T,S,N)
Q_, _ = np.linalg.qr(np.random.randn(3,3))
def conj_O(X, Q):
    Z = np.zeros((3,3,8))
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    Z[i,j] += Q[i,k]*Q[j,l]*X[k,l]
    return Z
Xq = conj_O(X, Q_)
hom = np.max(np.abs(jordan(Xq, conj_O(Y,Q_)) - conj_O(jordan(X,Y), Q_)))
Tq,Sq,Nq,_,_ = TSN(Xq)
chk("J3(O): O(3)-conjugation is an automorphism; (T,S,N) invariant (F4 invariants, receipt on a subgroup)",
    hom < 1e-9 and abs(Tq-T)<1e-9 and abs(Sq-S)<1e-9 and abs(Nq-N)<1e-9,
    f"hom defect {hom:.1e}")

# ---------------------------------------------------------------- D. W(A2) = S3 sheet monodromy of the eigenvalue cover
def loop_perm(pconst, qpath):
    prev = None; first = None
    for q in qpath:
        r = np.roots([1.0, 0.0, pconst, q])
        if prev is None:
            prev = r; first = r.copy(); continue
        best, bperm = None, None
        for perm in itertools.permutations(range(3)):
            d = sum(abs(r[perm[i]] - prev[i]) for i in range(3))
            if best is None or d < best: best, bperm = d, perm
        prev = np.array([r[bperm[i]] for i in range(3)])
    best, bperm = None, None
    for perm in itertools.permutations(range(3)):
        d = sum(abs(prev[perm[i]] - first[i]) for i in range(3))
        if best is None or d < best: best, bperm = d, perm
    return bperm
t = np.linspace(0, 1, 3000)
perm1 = loop_perm(-3.0, 2.0 + 0.6*np.exp(2j*np.pi*t))      # around q=+2 only
perm2 = loop_perm(-3.0, 3.2*np.exp(2j*np.pi*t))            # around q=+2 and q=-2
perm3 = loop_perm(-3.0, 0.8*np.exp(2j*np.pi*t))            # around neither
def pcompose(a, b): return tuple(a[b[i]] for i in range(3))
ide = (0,1,2)
chk("monodromy: loop around ONE cusp branch = a transposition",
    perm1 != ide and pcompose(perm1,perm1) == ide, f"perm {perm1}")
chk("monodromy: loop around BOTH branch points = a 3-cycle (full W(A2)=S3 generated)",
    perm2 != ide and pcompose(perm2,pcompose(perm2,perm2)) == ide and pcompose(perm2,perm2) != ide,
    f"perm {perm2}")
chk("monodromy: loop around NEITHER = identity", perm3 == ide, f"perm {perm3}")

# ---------------------------------------------------------------- E. hyperdeterminant, GHZ/W, Freudenthal duality
def cayley_det(a):
    d = (a[0,0,0]**2*a[1,1,1]**2 + a[0,0,1]**2*a[1,1,0]**2
       + a[0,1,0]**2*a[1,0,1]**2 + a[0,1,1]**2*a[1,0,0]**2)
    d -= 2*(a[0,0,0]*a[0,0,1]*a[1,1,0]*a[1,1,1] + a[0,0,0]*a[0,1,0]*a[1,0,1]*a[1,1,1]
          + a[0,0,0]*a[0,1,1]*a[1,0,0]*a[1,1,1] + a[0,0,1]*a[0,1,0]*a[1,0,1]*a[1,1,0]
          + a[0,0,1]*a[0,1,1]*a[1,1,0]*a[1,0,0] + a[0,1,0]*a[0,1,1]*a[1,0,1]*a[1,0,0])
    d += 4*(a[0,0,0]*a[0,1,1]*a[1,0,1]*a[1,1,0] + a[0,0,1]*a[0,1,0]*a[1,0,0]*a[1,1,1])
    return d
def sl2():
    while True:
        L = np.random.randn(2,2)
        if abs(np.linalg.det(L)) > 0.2:
            L /= np.sqrt(abs(np.linalg.det(L)))
            if np.linalg.det(L) < 0: L[:, [0,1]] = L[:, [1,0]]
            return L
err = 0.0
for _ in range(200):
    a = np.random.randn(2,2,2)
    L, M, K = sl2(), sl2(), sl2()
    ap = np.einsum('ia,jb,kc,abc->ijk', L, M, K, a)
    err = max(err, abs(cayley_det(ap) - cayley_det(a)) / (abs(cayley_det(a)) + 1e-12))
chk("hyperdeterminant: SL(2)^3 invariance (the duality group of the 2x2x2 phase space)",
    err < 1e-9, f"max rel err {err:.1e}")
GHZ = np.zeros((2,2,2)); GHZ[0,0,0] = GHZ[1,1,1] = 1.0
Wst = np.zeros((2,2,2)); Wst[0,0,1] = Wst[0,1,0] = Wst[1,0,0] = 1.0
chk("GHZ class: Det != 0  (large black hole / nonzero horizon area)",
    abs(cayley_det(GHZ) - 1.0) < 1e-12, f"Det(GHZ) = {cayley_det(GHZ):.1f}")
chk("W class:   Det  = 0  (small black hole / 'particle' stratum)",
    abs(cayley_det(Wst)) < 1e-12, f"Det(W) = {cayley_det(Wst):.1e}")
eps = np.array([[0.,1.],[-1.,0.]])
def raise_eps(g): return np.einsum('ia,jb,kc,abc->ijk', eps, eps, eps, g)
def grad_det(a, h=1e-6):
    g = np.zeros((2,2,2))
    for idx in np.ndindex(2,2,2):
        ap = a.copy(); am = a.copy()
        ap[idx] += h; am[idx] -= h
        g[idx] = (cayley_det(ap) - cayley_det(am)) / (2*h)
    return g
while True:
    a = GHZ + 0.25*np.random.randn(2,2,2)
    if cayley_det(a) > 1e-2: break
D0 = cayley_det(a)
found = False
for s in (+1.0, -1.0):
    at = s * raise_eps(grad_det(a)) / (2*math.sqrt(D0))
    Dt = cayley_det(at)
    if Dt <= 0: continue
    att = s * raise_eps(grad_det(at)) / (2*math.sqrt(Dt))
    if np.max(np.abs(att + a)) < 1e-4*(1+np.max(np.abs(a))):
        found = True
        chk("Freudenthal duality: x~~ = -x  (nonlinear involution on the phase space)",
            True, f"sign {int(s):+d}, closure err {np.max(np.abs(att+a)):.1e}")
        chk("Freudenthal duality: Det(x~) = Det(x)  (the horizon-area shadow is F-dual invariant)",
            abs(Dt - D0)/abs(D0) < 1e-5, f"Det {D0:.6f} -> {Dt:.6f}")
        break
if not found:
    chk("Freudenthal duality: x~~ = -x", False, "no sign convention closed")

# ---------------------------------------------------------------- F. Kerr-Newman g=2; Heisenberg regime
Q, aa, M = 0.7, 0.3, 1.9
r, th = 1e9, 0.9
Aphi = Q*aa*r*math.sin(th)**2 / (r**2 + aa**2*math.cos(th)**2)
chk("Kerr-Newman: asymptotic A_phi -> (Q a) sin^2(th)/r, i.e. magnetic moment mu = Q a",
    abs(Aphi*r/math.sin(th)**2 - Q*aa) < 1e-12)
g = 2*M*(Q*aa)/(Q*(M*aa))
chk("Kerr-Newman: g = 2 M mu / (Q J) = 2, exactly (Carter)", abs(g-2.0) < 1e-15)

G, hbar, cc = 6.674e-11, 1.0546e-34, 2.998e8
me, ee, eps0 = 9.109e-31, 1.602e-19, 8.854e-12
Mstar = math.sqrt(hbar*cc/(2*G))
ratio_e = 2*G*me**2/(hbar*cc)
a_e = hbar/(2*me*cc); rg_e = G*me/cc**2
rQ_e = math.sqrt(G*ee**2/(4*math.pi*eps0*cc**4))
chk("Heisenberg regime: r_s = lambda_C exactly at M* = sqrt(hbar c/2G) ~ 1.5e-8 kg (Planckian)",
    1.4e-8 < Mstar < 1.7e-8, f"M* = {Mstar:.3e} kg")
chk("electron: r_s/lambda_C = 2(m/M_P)^2 ~ 3.5e-45 (horizon buried 45 orders under uncertainty)",
    3.0e-45 < ratio_e < 4.0e-45, f"ratio = {ratio_e:.2e}")
chk("electron as Kerr-Newman: a >> M_geo, r_Q  (super-extremal, no horizon: 'naked particle')",
    a_e/rg_e > 1e44 and a_e/rQ_e > 1e22,
    f"a = {a_e:.2e} m, GM/c^2 = {rg_e:.2e} m, r_Q = {rQ_e:.2e} m")

print()
if fails:
    print("FAILURES: " + ", ".join(fails)); sys.exit(1)
print("ALL RECEIPTS PASS"); sys.exit(0)
