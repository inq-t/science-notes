"""Q*-type test: fixed small region A (one site), growing large region R = A ± R sites, infinite TFI/Kitaev chain.
Return-channel one-particle eigenvalues lam(R); compare decay rate with the inverse correlation length ln(h/J)."""
import numpy as np, mpmath as mp, time
from numpy.linalg import eigh
mp.mp.dps=45
def chain_A(L,h,J):
    A=np.zeros((2*L,2*L))
    for j in range(L):
        A[2*j,2*j+1]=2*h; A[2*j+1,2*j]=-2*h
        if j<L-1: A[2*j+1,2*j+2]=2*J; A[2*j+2,2*j+1]=-2*J
    return A
def gamma_ground(A):
    w,V=eigh(1j*A); return np.real(1j*(V@np.diag(np.sign(w))@V.conj().T))
# --- infinite-chain Majorana correlator g_n = Gamma_{a_0, b_n}, from the Bloch formula; verify against finite chain
def g_inf(n,h,J,prec=False):
    f=lambda k: -(h-J*mp.e**(-1j*k))/abs(h-J*mp.e**(-1j*k))*mp.e**(-1j*k*n)
    val=mp.quad(f,[0,mp.pi,2*mp.pi])/(2*mp.pi)
    return val
L=401; c=L//2; J=1.0
for h in [1.5]:
    Gam=gamma_ground(chain_A(L,h,J))
    print(f"convention check h={h}: finite-chain Gamma[a_c,b_{{c+n}}] vs Bloch integral")
    for n in [-2,-1,0,1,2,3]:
        fin=Gam[2*c,2*(c+n)+1]; inf=complex(g_inf(n,h,J))
        print(f"   n={n:2d}: finite={fin:+.10f}  bloch={inf.real:+.10f} (im {inf.imag:.1e})")
    print("   aa / bb correlations (should vanish):", abs(Gam[2*c,2*(c+1)]), abs(Gam[2*c+1,2*(c+1)+1]))

def Gamma_block_mp(h,J,sites):
    # Majorana ordering: site s -> indices (2s: a, 2s+1: b); Gamma antisymmetric, Gamma[a_s,b_t]=g_{t-s}, Gamma[b_t,a_s]=-g_{t-s}
    n=len(sites); gcache={}
    def g(m):
        if m not in gcache: gcache[m]=mp.re(g_inf(m,h,J))
        return gcache[m]
    G=mp.zeros(2*n,2*n)
    for i,s in enumerate(sites):
        for j,t in enumerate(sites):
            v=g(t-s); G[2*i,2*j+1]=v; G[2*j+1,2*i]=-v
    return G
def psd_sqrt_mp(M):
    E,Q=mp.eigsy(M); n=M.rows
    D=mp.diag([mp.sqrt(max(E[i],mp.mpf(0))) for i in range(n)])
    return Q*D*Q.T
def lam_return(h,J,R):
    sites=list(range(-R,R+1)); GR=Gamma_block_mp(h,J,sites); n=GR.rows
    SR=psd_sqrt_mp(mp.eye(n)+GR*GR)
    pos=[2*R,2*R+1]                       # the central site's two Majoranas
    SAA=mp.matrix([[SR[pos[i],pos[j]] for j in range(2)] for i in range(2)])
    GA=mp.matrix([[GR[pos[i],pos[j]] for j in range(2)] for i in range(2)])
    SA=psd_sqrt_mp(mp.eye(2)+GA*GA)
    SAi=mp.inverse(psd_sqrt_mp(SA))     # S_A^{-1/2}
    Mx=SAi*SAA*SAi
    E,_=mp.eigsy((Mx+Mx.T)/2)
    return sorted([float(E[i]) for i in range(2)],reverse=True), float(SA[0,0])
print("\nReturn-channel recoverability of one central site inside R = ±R sites (exact infinite chain, 45 digits)")
Rs=[1,2,3,4,6,8,12,16]
results={}
for h in [1.0,1.2,1.5,2.0]:
    xi_inv = 0.0 if h==J else float(mp.log(h/J))
    print(f"\n h/J={h}:  1/xi = ln(h/J) = {xi_inv:.4f}")
    print("   R    lam_1           lam_2           -ln(lam_1)   S_A(site)")
    t0=time.time()
    for R in Rs:
        (l1,l2),sa=lam_return(h,J,R); results[(h,R)]=(l1,l2)
        print(f"  {R:3d}  {l1:.6e}   {l2:.6e}   {-np.log(l1) if l1>0 else float('inf'):9.4f}   {sa:.4f}")
    print(f"   ({time.time()-t0:.0f}s)")
print("\nLocal decay rate  -[ln lam_1(R2) - ln lam_1(R1)]/(R2-R1)   vs   ln(h/J)  and  2 ln(h/J)")
for h in [1.2,1.5,2.0]:
    li=float(mp.log(h/J)); line=f" h={h}: "
    for R1,R2 in [(4,6),(6,8),(8,12),(12,16)]:
        r=-(np.log(results[(h,R2)][0])-np.log(results[(h,R1)][0]))/(R2-R1); line+=f" [{R1}->{R2}] {r:.4f}"
    print(line+f"    | ln(h/J)={li:.4f}  2ln(h/J)={2*li:.4f}")
print("\nCritical h=J: local power-law exponent  -d ln lam_1 / d ln R")
for R1,R2 in [(2,4),(4,8),(8,16)]:
    p=-(np.log(results[(1.0,R2)][0])-np.log(results[(1.0,R1)][0]))/(np.log(R2)-np.log(R1)); print(f"  [{R1}->{R2}] exponent {p:.3f}")
