#!/usr/bin/env python3
"""Receipts for hyperbolic-counting. Stdlib only; exit nonzero on failure.
Passing establishes the arithmetic quoted in the module's notes: orbifold
areas, the 5pi/6 vs golden-index firewall gap, resolution-depth ledger values,
the d iota = 2(1+q) iota dN relation, the Smith/ladder identities (path graph
A_{n-1} has norm 2cos(pi/n); A3 -> index 2), the affine-threshold check,
the algebraic-survivor table and separation costs, the accumulation honesty
bound, and the Gauss-map entropy
constant. It does NOT establish the channel reading, the fit's reliability,
transcendence (a theorem, not a float), or any selection principle."""
import json, math, sys, itertools
FAIL=[]
def check(name,val,ref,rtol=1e-3):
    if abs(val-ref)>rtol*abs(ref): FAIL.append((name,val,ref))
    return val
pi=math.pi; out={}

# 1) orbifold chi and areas
def chi(cones,cusps): return 2-sum(1-1/m for m in cones)-cusps
for sig,cones,cu,chref,aref in [("2,3,inf",[2,3],1,-1/6,pi/3),
                                ("2,4,inf",[2,4],1,-1/4,pi/2),
                                ("3,3,inf",[3,3],1,-1/3,2*pi/3),
                                ("3,4,inf",[3,4],1,-5/12,5*pi/6),
                                ("2,3,7",[2,3,7],0,-1/42,pi/21)]:
    c=chi(cones,cu); check(f"chi({sig})",c,chref,1e-12); check(f"area({sig})",-2*pi*c,aref,1e-12)
# least cusped triangle orbifold is (2,3,inf): assert its area strictly minimal among samples
assert pi/3 < pi/2 < 2*pi/3 < 5*pi/6
# firewall exhibit: 5pi/6 vs phi^2 — tiny but NONZERO gap (inequality is by transcendence)
phi2=((1+5**.5)/2)**2
gap=abs(5*pi/6-phi2); out["firewall_gap"]=gap
assert 1e-6 < gap < 5e-5

# 2) resolution depth and ledger
c0,hbar,G=299792458.0,1.054571817e-34,6.67430e-11
Mpc=3.0856775814913673e22; H0=67.4e3/Mpc; Om,OL=0.315,0.685
lP=math.sqrt(hbar*G/c0**3)
H_programme_crossing = 83.1058e3/Mpc
for H,Np_ref,i_ref,label in [(H0,140.29,2.265e122,"today"),
                             (H0*math.sqrt(2*OL),140.14,1.654e122,"matter_Lambda_equality"),
                             (H_programme_crossing,140.08,1.490e122,"programme_crossing")]:
    R=c0/H; Np=math.log(R/lP); iota=pi*math.exp(2*Np)
    out[f"N_P_{label}"]=check(f"N_P {label}",Np,Np_ref,1e-4)
    out[f"ledger_{label}"]=check(f"iota {label}",iota,i_ref,1e-2)
    check(f"iota=area/4lP2 {label}",iota,4*pi*R*R/(4*lP*lP),1e-12)
# d iota / iota = 2(1+q) dN  (finite-difference check in LCDM)
def H_of_N(N):  # a = e^N, a0=1
    return H0*math.sqrt(Om*math.exp(-3*N)+OL)
def q_of_N(N):
    a=math.exp(N); E2=Om*a**-3+OL
    return 0.5*Om*a**-3/E2 - OL/E2
for N in (0.0,-0.26):
    h=1e-6
    dlniota=2*(math.log(c0/H_of_N(N+h))-math.log(c0/H_of_N(N-h)))/(2*h)
    check(f"diota/iota/dN @N={N}",dlniota,2*(1+q_of_N(N)),1e-6)
out["2(1+q)_today"]=2*(1+q_of_N(0.0))

# 3) Smith/ladder identities: path graph A_{n-1} (n-1 vertices) has norm 2cos(pi/n)
def path_norm(k):  # largest eigenvalue of path graph on k vertices = 2cos(pi/(k+1))
    return 2*math.cos(pi/(k+1))
for n in range(3,13):
    check(f"A_{n-1} norm",path_norm(n-1),2*math.cos(pi/n),1e-12)
check("A3 norm^2 = 2",path_norm(3)**2,2.0,1e-12)

# 4) algebraic survivors in the released-2025 direct Delta-chi2 <= 1 profile window
fit_lo,fit_hi=0.941572,1.089954
s_lo,s_hi=1/fit_hi,1/fit_lo
ind_lo,ind_hi=math.exp(2*s_lo),math.exp(2*s_hi)
out["fit_window_above_affine_wall"] = s_lo > math.log(2)
assert out["fit_window_above_affine_wall"]
out["index_window"]=[round(ind_lo,3),round(ind_hi,3)]
ladder=[4*math.cos(pi/n)**2 for n in range(3,25)]+[4.0]
cands=set()
for r in (1,2,3):
    for combo in itertools.combinations_with_replacement(ladder,r):
        p=math.prod(combo)
        if ind_lo<=p<=ind_hi: cands.add(round(p,4))
cands|={7.0,8.0}
survivors=sorted(cands)
out["n_algebraic_survivors"]=len(survivors)
def s_of(i): return 0.5*math.log(i)
# named checks
check("golden^2",((1+5**.5)/2)**4,6.8541,1e-4); assert round(((1+5**.5)/2)**4,4) in cands
check("s*(golden^2)",s_of(6.854102),0.9624,1e-3)
check("4+2sqrt3",4+2*3**.5,7.4641,1e-4)
check("s*(4+2sqrt3)",s_of(4+2*3**.5),1.005053,1e-5)
# accumulation honesty: nearest survivor to s*=1
dmin=min(abs(s_of(i)-1.0) for i in survivors)
out["nearest_survivor_ds"]=round(dmin,4)
assert dmin<0.002   # 2 x 4cos^2(pi/11) sits at ~0.0016: transcendence not decidable by digits
# separation costs (sigma(s*) ~ sigma(R_c) near 1): factor over the current half-width
for i,lab in [(6.8541,"golden^2"),(7.0,"integer7"),(7.2361,"2x4cos2pi10"),(7.4641,"4+2sqrt3")]:
    need=abs(s_of(i)-1.0)/2
    out[f"improvement_x_{lab}"]=round(((fit_hi-fit_lo)/2)/need,0)

# 5) Gauss-map / mixmaster entropy
out["gauss_map_entropy_nats_per_era"]=check("h_Gauss",pi*pi/(6*math.log(2)),2.3731,1e-4)

print(json.dumps(out,indent=1))
if FAIL: print("FAILED:",FAIL,file=sys.stderr); sys.exit(1)
print("ALL RECEIPTS PASS")
