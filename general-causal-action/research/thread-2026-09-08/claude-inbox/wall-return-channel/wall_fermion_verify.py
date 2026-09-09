"""Brute-force verification of the one-particle return channel of a fermionic Gaussian wall.

Claim to test:  for Majorana Gaussian state with covariance Gamma (real antisymmetric, Gamma_jk = i*omega(c_j c_k)),
region R (algebra M) and subregion A (algebra N), the return channel D = E_omega o iota acts on Majoranas c_j (j in A) as
        D(c_j) = sum_l X_jl c_l ,      X = [sqrt(1+Gamma_R^2)]_AA  *  [sqrt(1+Gamma_AA^2)]^{-1}
exactly (no higher-order terms).  Model: transverse-field Ising / Kitaev Majorana chain, H = (i/4) c^T A c.
"""
import numpy as np, itertools
from numpy.linalg import eigh, inv
from scipy.linalg import sqrtm, expm

def majoranas(L):
    X=np.array([[0,1],[1,0]],complex); Y=np.array([[0,-1j],[1j,0]]); Z=np.array([[1,0],[0,-1]],complex); I=np.eye(2)
    def kron_list(ops):
        out=np.array([[1]],complex)
        for o in ops: out=np.kron(out,o)
        return out
    cs=[]
    for j in range(L):
        for P in (X,Y):
            cs.append(kron_list([Z]*j+[P]+[I]*(L-j-1)))
    return cs
def chain_A(L,h,J):
    A=np.zeros((2*L,2*L))
    for j in range(L):
        A[2*j,2*j+1]=2*h; A[2*j+1,2*j]=-2*h
        if j<L-1: A[2*j+1,2*j+2]=2*J; A[2*j+2,2*j+1]=-2*J
    return A
def gamma_ground(A):
    w,V=eigh(1j*A); return np.real(1j*(V@np.diag(np.sign(w))@V.conj().T))

L=5; h,J=1.3,1.0
cs=majoranas(L); dim=2**L
for a in range(2*L):
    for b in range(2*L):
        assert np.allclose(cs[a]@cs[b]+cs[b]@cs[a], 2*np.eye(dim)*(a==b))
A=chain_A(L,h,J)
H=sum((1j/4)*A[a,b]*cs[a]@cs[b] for a in range(2*L) for b in range(2*L))
assert np.allclose(H,H.conj().T)
w,V=eigh(H); psi=V[:,0]
tau=lambda M: np.trace(M)/dim
Gam_num=np.array([[np.real(1j*(psi.conj()@cs[a]@cs[b]@psi)) if a!=b else 0 for b in range(2*L)] for a in range(2*L)])
Gam_form=gamma_ground(A)
print("Gamma numeric vs i*sign(iA):  max diff =", np.abs(Gam_num-Gam_form).max())
Gam=Gam_num

def monomials(idx):
    mons=[]
    for k in range(len(idx)+1):
        for sub in itertools.combinations(idx,k):
            m=np.eye(dim,dtype=complex)
            for s in sub: m=m@cs[s]
            mons.append(m)
    return mons
def CE(x,idx):   # trace-preserving conditional expectation onto CAR(idx)
    return sum(tau(m.conj().T@x)*m for m in monomials(idx))

def brute_X(Rsites,Asites):
    Rm=[i for s in Rsites for i in (2*s,2*s+1)]; Am=[i for s in Asites for i in (2*s,2*s+1)]
    rho=dim*np.outer(psi,psi.conj())
    rhoR=CE(rho,Rm); rhoA=CE(rhoR,Am)
    sR=sqrtm(rhoR); sAi=inv(sqrtm(rhoA))
    Xb=np.zeros((len(Am),len(Am))); resid=0
    Dops=[]
    for r,j in enumerate(Am):
        Dc=sAi@CE(sR@cs[j]@sR,Am)@sAi
        Dops.append(Dc)
        for c,l in enumerate(Am): Xb[r,c]=np.real(tau(Dc@cs[l]))
        resid=max(resid,np.abs(Dc-sum(Xb[r,c]*cs[l] for c,l in enumerate(Am))).max())
    # formula
    GR=Gam[np.ix_(Rm,Rm)]; GA=Gam[np.ix_(Am,Am)]
    SR=np.real(sqrtm(np.eye(len(Rm))+GR@GR)); pos=[Rm.index(i) for i in Am]
    SAA=SR[np.ix_(pos,pos)]; SA=np.real(sqrtm(np.eye(len(Am))+GA@GA))
    Xf=SAA@inv(SA)
    # full spectrum of D on CAR(A)
    monsA=monomials(Am); nA=len(monsA)
    Dfull=np.zeros((nA,nA),complex)
    def Dmap(x): return sAi@CE(sR@x@sR,Am)@sAi
    for c,m in enumerate(monsA):
        Dm=Dmap(m)
        for r,m2 in enumerate(monsA): Dfull[r,c]=tau(m2.conj().T@Dm)
    return Xb,Xf,resid,np.sort(np.real(np.linalg.eigvals(Dfull)))[::-1],np.sort(np.real(np.linalg.eigvals(Xf)))[::-1]

for Rsites,Asites in [([1,2,3],[2]),([0,1,2,3],[1,2]),([1,2,3,4],[2,3]),([0,1,2,3,4],[1,2,3])]:
    Xb,Xf,resid,specD,specX=brute_X(Rsites,Asites)
    print(f"\nR={Rsites} A={Asites}: max|X_brute - X_formula| = {np.abs(Xb-Xf).max():.2e};  nonlinear residual of D(c_j) = {resid:.2e}")
    print("   spec X (one-particle):", np.round(specX,6))
    print("   spec D on full CAR(A):", np.round(specD,6))
