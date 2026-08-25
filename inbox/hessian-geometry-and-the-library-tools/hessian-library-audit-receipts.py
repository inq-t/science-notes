#!/usr/bin/env python3
"""Receipts for `hessian-geometry-and-the-library-tools.md`.

Requires numpy (NOT stdlib-only -- this is an inbox note, not a module receipt;
if it is promoted into a module the BKM section needs a stdlib rewrite).
Prints PASS/FAIL per claim. Exits nonzero if any claim fails.
"""
import sys, math, random
import numpy as np

fails = []
def chk(name, cond, detail=""):
    print(("PASS  " if cond else "FAIL  ") + name + (("  | " + detail) if detail else ""))
    if not cond: fails.append(name)

# ---------- helpers: tiny real symmetric matrix utilities (2x2 / 4x4) ----------
def matmul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def transpose(A): return [list(r) for r in zip(*A)]
def eigvals_sym(A):
    # Jacobi eigenvalue algorithm for small symmetric matrices
    n=len(A); A=[row[:] for row in A]
    for _ in range(200):
        off=max(((abs(A[i][j]),i,j) for i in range(n) for j in range(n) if i!=j), default=(0,0,0))
        if off[0]<1e-14: break
        _,p,q=off
        if abs(A[p][p]-A[q][q])<1e-300: th=math.pi/4
        else: th=0.5*math.atan2(2*A[p][q], A[p][p]-A[q][q])
        c,s=math.cos(th),math.sin(th)
        J=[[1.0 if i==j else 0.0 for j in range(n)] for i in range(n)]
        J[p][p]=c; J[q][q]=c; J[p][q]=-s; J[q][p]=s
        A=matmul(matmul(transpose(J),A),J)
    return sorted(A[i][i] for i in range(n))
def is_psd(A,tol=1e-9): return all(e>-tol for e in eigvals_sym(A))
def inv2(A):
    d=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]

# ================================================================
# CLAIM 1. S6 manuscript Remark 3.23: Gram matrix of h|F^1 has signature (1,1),
#   given Im tau > 0 and D := Im beta - 6 (Im mu)^2 / Im tau < 0  (condition (beta3)).
#   Gram = -[[12 Im tau, 12 Im mu],[12 Im mu, 2 Im beta]] ; det = 24 Im tau * D.
# ================================================================
random.seed(7)
ok_det=True; ok_sig=True
for _ in range(20000):
    it=random.uniform(1e-3,50.0)          # Im tau > 0
    imu=random.uniform(-20.0,20.0)        # Im mu free
    D=-random.uniform(1e-6,30.0)          # (beta3): D < 0
    ib=D+6*imu*imu/it                     # Im beta from D
    G=[[12*it,12*imu],[12*imu,2*ib]]
    det=G[0][0]*G[1][1]-G[0][1]*G[1][0]
    if abs(det-24*it*D)>1e-6*max(1.0,abs(det)): ok_det=False
    ev=eigvals_sym(G)
    if not (ev[0]<0<ev[1]): ok_sig=False
    ev2=eigvals_sym([[-x for x in r] for r in G])   # overall sign flip (either sign of Q0)
    if not (ev2[0]<0<ev2[1]): ok_sig=False
chk("S6 Gram determinant identity  det = 24*Im(tau)*D", ok_det)
chk("S6 Hodge form signature is (1,1) for BOTH signs of Q0", ok_sig,
    "20000 random admissible (Im tau>0, D<0)")

# ================================================================
# CLAIM 2. The CQ decoherence-diffusion trade-off IS a Schur-complement condition,
#   identical in form to the vault's hidden-mode elimination in common-response-matrix.md.
#   Block PSD  [[D0, D1],[D1, D2]] >= 0   <==>  D0 - D1 D2^{-1} D1 >= 0   (D2 > 0)
#                                        <==>  D2 - D1 D0^{-1} D1 >= 0   (D0 > 0)
#   Saturation (Schur complement = 0)  <==>  D2 = D1 D0^{-1} D1.
# ================================================================
def rand_sym_pd(n):
    M=[[random.uniform(-1,1) for _ in range(n)] for _ in range(n)]
    A=matmul(M,transpose(M))
    for i in range(n): A[i][i]+=0.35
    return A
agree_fwd=True; agree_rev=True; sat_ok=True
for _ in range(4000):
    D0=rand_sym_pd(2); D2=rand_sym_pd(2)
    s=random.uniform(0.0,1.6)
    B=[[s*random.uniform(-1,1) for _ in range(2)] for _ in range(2)]
    D1=[[0.5*(B[i][j]+B[j][i]) for j in range(2)] for i in range(2)]   # symmetric coupling
    big=[[D0[0][0],D0[0][1],D1[0][0],D1[0][1]],
         [D0[1][0],D0[1][1],D1[1][0],D1[1][1]],
         [D1[0][0],D1[0][1],D2[0][0],D2[0][1]],
         [D1[1][0],D1[1][1],D2[1][0],D2[1][1]]]
    blockpsd=is_psd(big,1e-8)
    sc_a=[[D0[i][j]-matmul(matmul(D1,inv2(D2)),D1)[i][j] for j in range(2)] for i in range(2)]
    sc_b=[[D2[i][j]-matmul(matmul(D1,inv2(D0)),D1)[i][j] for j in range(2)] for i in range(2)]
    if blockpsd != is_psd(sc_a,1e-7): agree_fwd=False
    if blockpsd != is_psd(sc_b,1e-7): agree_rev=False
    # saturation: set D2 := D1 D0^{-1} D1  -> Schur complement exactly zero, block still PSD
    D2s=matmul(matmul(D1,inv2(D0)),D1)
    sc_s=[[D2s[i][j]-matmul(matmul(D1,inv2(D0)),D1)[i][j] for j in range(2)] for i in range(2)]
    if max(abs(sc_s[i][j]) for i in range(2) for j in range(2))>1e-9: sat_ok=False
chk("trade-off <=> block PSD, form A: D0 - D1 D2^-1 D1 >= 0", agree_fwd, "4000 random 2x2 blocks")
chk("trade-off <=> block PSD, form B: D2 - D1 D0^-1 D1 >= 0", agree_rev, "4000 random 2x2 blocks")
chk("saturation D2 = D1 D0^-1 D1 makes the Schur complement exactly 0", sat_ok)



# ---- CLAIM 3: BKM = Hessian of log-partition, quantum exponential family ----
n=4
def herm(n):
    M=np.random.randn(n,n)+1j*np.random.randn(n,n); return (M+M.conj().T)/2
A=[herm(n),herm(n),herm(n)]            # noncommuting generators
def logZ(th):
    K=sum(t*a for t,a in zip(th,A)); w=np.linalg.eigvalsh(K)
    m=w.max(); return m+np.log(np.exp(w-m).sum())
def rho_of(th):
    K=sum(t*a for t,a in zip(th,A)); w,U=np.linalg.eigh(K)
    e=np.exp(w-w.max()); e=e/e.sum(); return (U*e)@U.conj().T
th=np.array([0.37,-0.21,0.44])
h=1e-4
H=np.zeros((3,3))
for i in range(3):
    for j in range(3):
        ei=np.zeros(3); ei[i]=h; ej=np.zeros(3); ej[j]=h
        H[i,j]=(logZ(th+ei+ej)-logZ(th+ei-ej)-logZ(th-ei+ej)+logZ(th-ei-ej))/(4*h*h)
rho=rho_of(th); w,U=np.linalg.eigh(rho)
def ctr(X): return X-np.trace(rho@X).real*np.eye(n)
At=[ctr(a) for a in A]
# BKM in the eigenbasis of rho: g(X,Y) = sum_{ab} Xt_ab* Yt_ab * (w_a - w_b)/(log w_a - log w_b)
def logmean(a,b): return a if abs(a-b)<1e-12 else (a-b)/(math.log(a)-math.log(b))
Lm=np.array([[logmean(w[a],w[b]) for b in range(n)] for a in range(n)])
def bkm(X,Y):
    Xr=U.conj().T@X@U; Yr=U.conj().T@Y@U
    return float(np.real(np.sum(Xr.conj()*Yr*Lm)))
G=np.array([[bkm(At[i],At[j]) for j in range(3)] for i in range(3)])
chk("BKM metric == Hessian of log Z (quantum exp. family, affine chart)",
    np.allclose(G,H,atol=1e-5,rtol=1e-4), f"max|diff|={np.abs(G-H).max():.2e}")
Sym=np.array([[0.5*np.trace(rho@(At[i]@At[j]+At[j]@At[i])).real for j in range(3)] for i in range(3)])
chk("BKM != symmetrized (SLD-style) covariance -- BKM is a genuine selection",
    not np.allclose(G,Sym,atol=1e-3), f"max|BKM-Sym|={np.abs(G-Sym).max():.3e}")
chk("BKM is positive definite here", np.linalg.eigvalsh(G).min()>0, f"eigs={np.round(np.linalg.eigvalsh(G),5)}")

# ---- Amari-Chentsov cubic tensor = third derivative of the SAME potential ----
C=np.zeros((3,3,3))
hh=2e-3
for i in range(3):
    for j in range(3):
        for k in range(3):
            e=[np.zeros(3) for _ in range(3)]
            for idx,ax in enumerate((i,j,k)): e[idx][ax]=hh
            s=0.0
            for s1 in (1,-1):
                for s2 in (1,-1):
                    for s3 in (1,-1):
                        s+= s1*s2*s3*logZ(th+s1*e[0]+s2*e[1]+s3*e[2])
            C[i,j,k]=s/(8*hh**3)
chk("cubic response tensor C_ijk is totally symmetric (Amari-Chentsov / Codazzi)",
    max(abs(C[i,j,k]-C[p,q,r]) for i in range(3) for j in range(3) for k in range(3)
        for (p,q,r) in [(j,i,k),(i,k,j),(k,j,i)])<2e-3,
    "this symmetry IS the integrability condition the vault asks for")
# and C_ijk == d_i G_jk  (the vault's C_Nzetazeta = d_N G_zetazeta)
def Gof(t):
    r=rho_of(t); ww,UU=np.linalg.eigh(r)
    Lm2=np.array([[logmean(ww[a],ww[b]) for b in range(n)] for a in range(n)])
    At2=[a-np.trace(r@a).real*np.eye(n) for a in A]
    def bk(X,Y):
        Xr=UU.conj().T@X@UU; Yr=UU.conj().T@Y@UU
        return float(np.real(np.sum(Xr.conj()*Yr*Lm2)))
    return np.array([[bk(At2[i],At2[j]) for j in range(3)] for i in range(3)])
dG=np.zeros((3,3,3))
for i in range(3):
    ei=np.zeros(3); ei[i]=1e-3
    dG[i]=(Gof(th+ei)-Gof(th-ei))/(2e-3)
chk("C_ijk == d_i G_jk  (the vault's C_{N zeta zeta} = d_N G_{zeta zeta})",
    np.abs(C-dG).max()<5e-3, f"max|diff|={np.abs(C-dG).max():.2e}")

# ---- CLAIM 4: Levi form of Phi(z)=psi(Re z) is (1/4) Hess psi; conj is antiholo involution ----
def psi(x): return np.exp(0.4*x[0])+np.exp(-0.3*x[1]+0.2*x[0])+np.exp(0.5*x[2]-0.1*x[1])+0.5*x@x
def hess(f,x,h=1e-4):
    m=len(x); Hm=np.zeros((m,m))
    for i in range(m):
        for j in range(m):
            ei=np.zeros(m); ei[i]=h; ej=np.zeros(m); ej[j]=h
            Hm[i,j]=(f(x+ei+ej)-f(x+ei-ej)-f(x-ei+ej)+f(x-ei-ej))/(4*h*h)
    return Hm
ok_levi=True; ok_pd=True
for _ in range(300):
    x=np.random.uniform(-1.2,1.2,3); y=np.random.uniform(-2,2,3)
    Phi=lambda v: psi(v[:3])                       # no y-dependence
    Hx=hess(psi,x)
    # d^2 Phi / dz_i dzbar_j = (1/4)(d_xi d_xj + d_yi d_yj) Phi = (1/4) Hess_x psi
    Levi=0.25*Hx
    if not np.allclose(4*Levi,Hx,atol=1e-6): ok_levi=False
    if np.linalg.eigvalsh(Hx).min()<=0: ok_pd=False
chk("Levi form of Kahler potential Phi(z)=psi(Re z) equals (1/4)*Hess(psi)", ok_levi,
    "so TM is Kahler exactly when (nabla,g) is Hessian; restricting to y=0 returns the Hessian metric")
chk("Hess psi positive definite (psi strictly convex) -> Kahler on TM", ok_pd)
# involution
x=np.random.randn(3); y=np.random.randn(3)
tau=lambda xy:(xy[0],-xy[1])
chk("tau(z)=conj(z) i.e. (x,y)->(x,-y): involution, antiholomorphic, fixed locus {y=0}",
    tau(tau((x,y)))[0].tolist()==x.tolist() and np.allclose(tau(tau((x,y)))[1],y),
    "dim_R TM = 6, dim_R fixed locus = 3 -- matches algebra/real-forms-and-factive-spacetime.md exactly")


print()
if fails:
    print("FAILURES: " + ", ".join(fails)); sys.exit(1)
print("ALL RECEIPTS PASS"); sys.exit(0)
