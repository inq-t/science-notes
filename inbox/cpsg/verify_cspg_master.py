"""verify_cspg_master.py -- self-contained certificate for Causal-Scale
Partition Geometry. Part A: symbolic identity tower. Part B: empirical
pipeline, four inputs -> full output table."""
import sympy as sp, numpy as np
from scipy.integrate import quad

print("="*74); print("PART A: THE IDENTITY TOWER (symbolic, exact)"); print("="*74)
ok = lambda l,c: print(f"  {l}: {bool(c)}")
N = sp.Symbol('N', real=True)
n1,n2,n3,O1,O2,O3 = sp.symbols('n1 n2 n3 O1 O2 O3', positive=True)
Z = O1*sp.exp(-n1*N)+O2*sp.exp(-n2*N)+O3*sp.exp(-n3*N)
X = -sp.Rational(1,2)*sp.log(Z)
p=[Oi*sp.exp(-ni*N)/Z for Oi,ni in [(O1,n1),(O2,n2),(O3,n3)]]; ns=[n1,n2,n3]
m1=sum(pi*ni for pi,ni in zip(p,ns)); m2=sum(pi*(ni-m1)**2 for pi,ni in zip(p,ns))
m3=sum(pi*(ni-m1)**3 for pi,ni in zip(p,ns))
ok("T1  X'   = <n>/2               (slope = mean)", sp.simplify(sp.diff(X,N)-m1/2)==0)
ok("T2  X''  = -Var(n)/2           (bend = -variance)", sp.simplify(sp.diff(X,N,2)+m2/2)==0)
ok("T3  X''' = +kappa3(n)/2        (jerk = skewness)", sp.simplify(sp.diff(X,N,3)-m3/2)==0)
ok("T10 d<n>/dN = -Var(n) <= 0     (H-theorem)", sp.simplify(sp.diff(m1,N)+m2)==0)
t=sp.Symbol('t',positive=True); a=sp.Function('a',positive=True)(t); H=sp.diff(a,t)/a
q_def=-sp.diff(a,t,2)*a/sp.diff(a,t)**2
ok("T4  q = X' - 1                 (deceleration = slope - coasting)",
   sp.simplify(q_def-((-sp.diff(sp.log(H),t)/H)-1))==0)
ok("T6  d ln|Omega_k|/dN = 2q      (curvature flow)",
   sp.simplify(sp.diff(sp.log(1/(a*H)**2),t)/H-2*q_def)==0)
G,c0,H0s,rho=sp.symbols('G c H_0 rho',positive=True)
M=sp.Rational(4,3)*sp.pi*rho*(c0/H0s)**3
ok("T8  2GM_H/(R_H c^2) = Omega_tot (compactness IS flatness)",
   sp.simplify(2*G*M/((c0/H0s)*c0**2)-rho/(3*H0s**2/(8*sp.pi*G)))==0)
w=sp.Symbol('w')
ok("A3  n = 3(1+w)                 (spectrum is kinematic)", sp.simplify(3*(1+w)-(3+3*w))==0)

print(); print("="*74); print("PART B: THE EMPIRICAL PIPELINE"); print("="*74)
c=2.99792458e8; Gc=6.6743e-11; hbar=1.054571817e-34; kB=1.380649e-23
Mpc=3.0856775814913673e22; Gyr=3.1557e16; Gly=9.4607304725808e24
# ---- EMPIRICAL INPUTS ----
H0=68.17; Om=0.3027; Tcmb=2.7255; Neff=3.044; Ok=0.0
print(f"  INPUTS: H0={H0} km/s/Mpc | Omega_m={Om} | T_CMB={Tcmb} K | N_eff={Neff} | Omega_k={Ok}")
H0si=H0*1e3/Mpc
rho_c=3*H0si**2/(8*np.pi*Gc)
a_rad=np.pi**2*kB**4/(15*hbar**3*c**3)
Og=a_rad*Tcmb**4/(rho_c*c**2)
Onu=Og*Neff*(7/8)*(4/11)**(4/3)
Orad=Og+Onu; OL=1-Om-Orad-Ok
print(f"  derived weights: O_gamma={Og:.3e}  O_nu={Onu:.3e}  O_r={Orad:.3e}  O_Lambda={OL:.4f}")

Zf=lambda Nv: OL+Om*np.exp(-3*Nv)+Orad*np.exp(-4*Nv)
mean_n=lambda Nv:(3*Om*np.exp(-3*Nv)+4*Orad*np.exp(-4*Nv))/Zf(Nv)
q0=0.5*mean_n(0)-1
zt=(2*OL/Om)**(1/3)-1
zeq=Om/Orad-1
zLm=(OL/Om)**(1/3)-1   # Lambda-matter equality: Om e^{-3N} = OL
H0t0=quad(lambda Nv:1/np.sqrt(Zf(Nv)),-30,0,limit=400)[0]
t0=H0t0/H0si/Gyr
eta_future=quad(lambda Nv:np.exp(-Nv)/np.sqrt(Zf(Nv)),0,60,limit=400)[0]  # in c/H0 units
RH=c/H0si; MH=c**3/(2*Gc*H0si)
lP=np.sqrt(hbar*Gc/c**3); XP=np.log(RH/lP); SH=np.pi*np.exp(2*XP); Nq=SH/np.log(2)
lam=3*OL*(H0si*np.sqrt(hbar*Gc/c**5))**2

rows=[("q_0 = <n>_0/2 - 1", f"{q0:+.4f}", "observed deceleration parameter ~ -0.55"),
 ("z_acc  (<n>=2 crossing)", f"{zt:.3f}", "SNe transition z ~ 0.6-0.7"),
 ("z_eq   (matter=radiation)", f"{zeq:.0f}", "CMB-inferred z_eq ~ 3400"),
 ("z_Lm   (Lambda=matter)", f"{zLm:.3f}", "onset of Lambda domination"),
 ("H0*t0  (age integral)", f"{H0t0:.4f}", "dimensionless age"),
 ("t0", f"{t0:.3f} Gyr", "stellar/CMB ages ~ 13.8 Gyr"),
 ("future conformal reach", f"{eta_future:.4f} c/H0", "event horizon exists (finite)"),
 ("R_H = c/H0", f"{RH/Gly:.2f} Gly", "Hubble radius"),
 ("M_H = c^3/2GH0", f"{MH:.3e} kg", "critical Hubble mass"),
 ("X_P = ln(R_H/l_P)", f"{XP:.3f}", "the height of the curve"),
 ("S_H/k_B = pi e^{2X_P}", f"{SH:.2e}", "horizon entropy"),
 ("N_qubit = S/ln2", f"{Nq:.2e}", "holographic capacity"),
 ("ln(1/Lambda l_P^2) = 2X_P - ln(3O_L)", f"{np.log(1/lam):.2f}", "the 'owed logarithm' ~280")]
print(f"\n  {'OUTPUT':34s} {'VALUE':>16s}   ANCHOR")
for r in rows: print(f"  {r[0]:34s} {r[1]:>16s}   {r[2]}")
print(f"\n  era slopes X' -> n/2: radiation 2, matter 3/2, vacuum 0 [tropical skeleton]")
print(f"  max deviation from skeleton: ln(2)/2 = {np.log(2)/2:.4f} nats per crossing")
