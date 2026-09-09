import numpy as np, mpmath as mp, time
mp.mp.dps=45
J=1.0
def g_inf(n,h): 
    f=lambda k: -(h-J*mp.e**(-1j*k))/abs(h-J*mp.e**(-1j*k))*mp.e**(-1j*k*n)
    return mp.re(mp.quad(f,[0,mp.pi,2*mp.pi])/(2*mp.pi))
def Gamma_block(h,sites,cache):
    n=len(sites); G=mp.zeros(2*n,2*n)
    for i,s in enumerate(sites):
        for j,t in enumerate(sites):
            m=t-s
            if m not in cache: cache[m]=g_inf(m,h)
            G[2*i,2*j+1]=cache[m]; G[2*j+1,2*i]=-cache[m]
    return G
def psd_sqrt(M):
    E,Q=mp.eigsy(M); return Q*mp.diag([mp.sqrt(max(E[i],mp.mpf(0))) for i in range(M.rows)])*Q.T
def lams(h,R,Asites,cache):
    sites=list(range(-R,R+1)); GR=Gamma_block(h,sites,cache); n=GR.rows
    SR=psd_sqrt(mp.eye(n)+GR*GR)
    pos=[i for s in Asites for i in (2*(s+R),2*(s+R)+1)]
    SAA=mp.matrix([[SR[p,q] for q in pos] for p in pos]); GA=mp.matrix([[GR[p,q] for q in pos] for p in pos])
    SAi=mp.inverse(psd_sqrt(psd_sqrt(mp.eye(len(pos))+GA*GA)))
    Mx=SAi*SAA*SAi; E,_=mp.eigsy((Mx+Mx.T)/2)
    return sorted([float(E[i]) for i in range(len(pos))],reverse=True)
# Extrapolation of the massive rates from the previous run (rate(R) = r_inf + c/R, using R_avg pairs (7,14))
prev={1.2:(0.4385,0.4008),1.5:(0.8806,0.8474),2.0:(1.4571,1.4224)}
print("Richardson extrapolation of local rate (R_avg=7,14):")
for h,(r7,r14) in prev.items():
    rinf=(14*r14-7*r7)/7; c=(r7-rinf)*7
    print(f"  h={h}: r_inf={rinf:.4f}  vs 2ln(h/J)={2*np.log(h):.4f}   (diff {rinf-2*np.log(h):+.4f});  prefactor exponent c={c:.3f}")
# Control 1: two-site small region, h=1.5
print("\nControl 1: A = two central sites, h/J=1.5; expect same rate 2 ln(1.5)=0.8109 for the top eigenvalue")
cache={}; res={}
t0=time.time()
for R in [3,4,6,8,12]:
    l=lams(1.5,R,[0,1],cache); res[R]=l
    print(f"  R={R:3d}: lam = {l[0]:.4e} {l[1]:.4e} {l[2]:.4e} {l[3]:.4e}")
for R1,R2 in [(4,6),(6,8),(8,12)]:
    print(f"  rate[{R1}->{R2}] top: {-(np.log(res[R2][0])-np.log(res[R1][0]))/(R2-R1):.4f}   second: {-(np.log(res[R2][1])-np.log(res[R1][1]))/(R2-R1):.4f}")
print(f"  ({time.time()-t0:.0f}s)")
# Control 2: critical exponent at larger R
print("\nControl 2: critical h=J, one site, larger R; expect lam_1 ~ R^-1")
cache={}; res={}
t0=time.time()
for R in [16,24,32]:
    l=lams(1.0,R,[0],cache); res[R]=l; print(f"  R={R:3d}: lam_1={l[0]:.6e}   R*lam_1={R*l[0]:.4f}")
for R1,R2 in [(16,24),(24,32)]:
    print(f"  exponent[{R1}->{R2}] = {-(np.log(res[R2][0])-np.log(res[R1][0]))/(np.log(R2)-np.log(R1)):.4f}")
print(f"  ({time.time()-t0:.0f}s)")
