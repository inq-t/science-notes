#!/usr/bin/env python3
"""Receipts for dimensional-ladder. Stdlib only; exit nonzero on failure.
Passing establishes arithmetic only, never a mechanism or reading."""
import json, math, sys
FAIL=[]
def check(name,val,ref,rtol=1e-2):
    if abs(val-ref)>rtol*abs(ref): FAIL.append((name,val,ref))
    return val
c,hbar,G,kB=299792458.0,1.054571817e-34,6.67430e-11,1.380649e-23
eV=1.602176634e-19
out={}
# ladder
out["c2_G_kg_per_m"]=check("c2/G",c**2/G,1.347e27)
out["c3_G_kg_per_s"]=check("c3/G",c**3/G,4.037e35)
out["c4_G_N"]      =check("c4/G",c**4/G,1.210e44)
out["c5_G_W"]      =check("c5/G",c**5/G,3.628e52)
# G rho = 1/t^2 demos
for rho,ref_min,label in [(5514.0,84.34,"earth_density"),(1000.0,198.05,"water")]:
    T=math.sqrt(3*math.pi/(G*rho))/60.0
    out[f"surface_orbit_min_{label}"]=check(label,T,ref_min,1e-3)
# acceleration = c^2/d and a=cH
out["a_from_c2_over_d_1m"]=check("c2/d",c**2/1.0,8.988e16)
# Heisenberg edge
mP=math.sqrt(hbar*c/G)
mx=mP/math.sqrt(2)
out["crossover_GeV"]=check("m_x",mx*c**2/(1e9*eV),8.633e18)
# lambda_C(m_x) = r_s(m_x)
assert abs(hbar/(mx*c) - 2*G*mx/c**2) < 1e-40
# GUP minimum: dx(dp)=hbar/dp+G dp/c^3, min at dp=mP c, dx_min=2 lP
lP=math.sqrt(hbar*G/c**3); dp=mP*c
dx=lambda p: hbar/p + G*p/c**3
out["dx_min_over_lP"]=check("dxmin",dx(dp)/lP,2.0,1e-9)
assert dx(dp*1.01)>dx(dp) and dx(dp*0.99)>dx(dp)      # genuine minimum
assert dx(10*dp)>dx(dp)                                # UV/IR inversion branch rises
# GM vs G: recorded facts (not computable here): GM_sun ~ 1.32712440e20 m^3/s^2 (~1e-10 rel),
# CODATA G rel. uncertainty ~2.2e-5. Asserted only as ordering:
assert 1e-10 < 2.2e-5
print(json.dumps(out,indent=1))
if FAIL: print("FAILED:",FAIL,file=sys.stderr); sys.exit(1)
print("ALL RECEIPTS PASS")
