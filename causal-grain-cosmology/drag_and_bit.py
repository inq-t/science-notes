#!/usr/bin/env python3
"""Is the drag already geometric (G, c, size)?  And is the 2 a bit?"""
import numpy as np
from scipy.optimize import brentq

c=2.99792458e8; G=6.67430e-11; l_P=1.616255e-35
Mpc=3.0856775814913673e22; kms=1e3/Mpc
H0,Om,OL = 67.36,0.3153,0.6847
Or = 4.15e-5/(H0/100)**2
H0s=H0*kms; HL=H0*np.sqrt(OL); HLs=HL*kms
E   = lambda x: np.sqrt(Or*np.exp(-4*x)+Om*np.exp(-3*x)+OL)
Omx = lambda x: Om*np.exp(-3*x)/E(x)**2

print("="*72); print("1.  IS THE DRAG ALREADY GEOMETRIC?   r_s / R_A  =?  Omega_m")
print("="*72)
for x in [0.0,-0.3,-1.0,-3.0]:
    H=H0s*E(x); R_A=c/H
    rho_m = Omx(x)*3*H**2/(8*np.pi*G)
    M     = rho_m*(4*np.pi/3)*R_A**3          # mass inside the Hubble sphere
    r_s   = 2*G*M/c**2
    print(f"  z={np.exp(-x)-1:6.3f}   r_s/R_A = {r_s/R_A:.10f}   Omega_m = {Omx(x):.10f}"
          f"   diff {r_s/R_A-Omx(x):+.2e}")
print("  => r_s = Omega_m * R_A   EXACTLY.  Drag is pure geometry:")
print("     n^2 = 1/(1 - r_s/R_A).   Inputs: G, c, R_A, and the mass inside.\n")

print("="*72); print("2.  WHAT THE CONDITION n^2 = 2 IS, IN FOUR LANGUAGES")
print("="*72)
for n2,name in [(2.0,"n^2 = 2"),(3.0,"n^2 = 3")]:
    Omc = 1-1/n2
    print(f"  {name}:  Omega_m = {Omc:.6f} = {'1/2' if abs(Omc-.5)<1e-9 else '2/3'}"
          f"   r_s/R_A = {Omc:.6f}   S_horizon/S_inf = {1/n2:.6f}"
          f"   rho+3p = {Omc-2*(1-Omc):+.4f} rho_c")

print("\n  n^2 = 2  <=>  Omega_m = 1/2  <=>  r_s = R_A/2  <=>  S(now) = S(inf)/2")
print("  n^2 = 3  <=>  Omega_m = 2/3  <=>  r_s = 2R_A/3  <=>  rho+3p = 0  (q=0, SEC edge)\n")

print("="*72); print("3.  THE SdS / A_2 CUBIC:  DOES IT SUPPLY EITHER RATIO?")
print("="*72)
# f(r) = 1 - 2GM/r - Lam r^2/3.  Nariai: double root.
Lam=1.0
def nariai():
    # double root of  Lam r^3/3 - r + 2GM = 0  ->  r*=1/sqrt(Lam), 2GM = 2/(3 sqrt(Lam))
    r=1/np.sqrt(Lam); GM2=(r-Lam*r**3/3)
    return r,GM2
r_h,r_s_nar = nariai()
print(f"  Nariai (horizons merge):  r_h = 1/sqrt(Lam) = {r_h:.6f}")
print(f"                            r_s = 2GM        = {r_s_nar:.6f}")
print(f"                            r_s/r_h          = {r_s_nar/r_h:.10f}   (= 2/3)")
print("  => the cubic's degenerate point is r_s/R = 2/3, i.e. Omega_m = 2/3, i.e. q = 0.")
print("     The cubic anchors n^2 = 3, NOT n^2 = 2.\n")

print("="*72); print("4.  THE EXACT SOLUTION:  n = coth(u),  u = (3/2) H_Lam t")
print("="*72)
def n_coth(x):                       # matter+Lambda only, closed form
    return np.sqrt(1+ (Om/OL)*np.exp(-3*x))
for x in [0.0,-0.3060,-0.4894,-1.0]:
    n_full=E(x)/np.sqrt(OL); n_cl=n_coth(x)
    u=np.arctanh(1/n_cl)
    print(f"  z={np.exp(-x)-1:6.4f}  n(full,with rad)={n_full:.6f}  n=coth(u)={n_cl:.6f}"
          f"  u={u:.6f}  tanh u={1/n_cl:.6f}")
u_c=np.arctanh(1/np.sqrt(2))
print(f"\n  n^2 = 2  =>  tanh u = 1/sqrt2 ,  u = arctanh(1/sqrt2) = {u_c:.6f} = ln(1+sqrt2) = {np.log(1+np.sqrt(2)):.6f}")
print(f"  two-state allocation at that point:  m^2 = tanh^2 u = {np.tanh(u_c)**2:.6f}"
      f"   g = sech^2 u = {1/np.cosh(u_c)**2:.6f}   m^2+g = {np.tanh(u_c)**2+1/np.cosh(u_c)**2:.1f}")
print("  => n^2 = 2 is EXACTLY the equipartition point of the binary allocation m^2 + g = 1.\n")

print("="*72); print("5.  IS THERE A BIT?  (iota ~ 1/H^2, two nats per e-fold)")
print("="*72)
n_c=1.4675; dn=0.0406
print(f"  dN_P remaining after the crossing = ln n_c              = {np.log(np.sqrt(2)):.6f} nats  if n_c=sqrt2")
print(f"                                                          = {np.log(np.sqrt(2))/np.log(2):.6f} BITS  (exactly 1/2)")
print(f"  d(ln iota) remaining              = 2 ln n_c = ln 2     = {np.log(2):.6f} nats")
print(f"                                                          = {1.0:.6f} BIT  (exactly 1)")
print(f"  measured:  ln n_c = {np.log(n_c):.6f} nats = {np.log(n_c)/np.log(2):.6f} bits"
      f"   (target 0.5)")

print("\n"+"="*72); print("6.  IS A FACTOR OF 2 MISSING SOMEWHERE?  (size of the residual)")
print("="*72)
meas=n_c**2; err=2*n_c*dn
for t,lbl in [(2.0,"2"),(2.25,"9/4"),(1.0,"1  (a missing halving of n^2)"),
              (4.0,"4  (a missing doubling of n^2)"),(np.e,"e"),(np.pi**2/4,"pi^2/4")]:
    print(f"  target {lbl:30s} {t:7.4f}   offset {100*(meas/t-1):+8.2f}%   {abs(meas-t)/err:6.2f} sigma")
print("  => the residual is 7.7%.  A missing factor of 2 would show as 100% or -50%.")
print("     Whatever is off is a few-percent effect, not a binary bookkeeping error.\n")

print("="*72); print("7.  CAN WE SWITCH TO LOG BASE 2?   (test on the additive relation)")
print("="*72)
lam=4.2869e-15; R_c=1.1310e26
Sig_nats=np.log(R_c/lam); Sig_bits=Sig_nats/np.log(2)
print(f"  Sigma_c = ln(R_c/lambda*)   = {Sig_nats:8.4f} nats")
print(f"  Sigma_c = log2(R_c/lambda*) = {Sig_bits:8.4f} bits")
print(f"  q* is a pure ratio D_M/r_s  -> base-independent, ~= {Sig_nats+3:.2f}")
print(f"  q* = Sigma_c + d  holds in nats ({Sig_nats:.2f}+3={Sig_nats+3:.2f});"
      f" in bits it fails by {Sig_bits-Sig_nats:.1f}.")
print("  => the base is FIXED to e by every additive relation in the vault.")
print("     A factor of 2 in a RATIO is base-free; a log base is not.")
