import numpy as np
from scipy.integrate import quad
c=2.99792458e8; G=6.67430e-11; Mpc=3.0856775814913673e22; kms=1e3/Mpc
Gly=9.4607e24  # m
H0,Om,OL=67.36,0.3153,0.6847; Or=4.15e-5/(H0/100)**2
H0s=H0*kms
E=lambda a: np.sqrt(Or*a**-4+Om*a**-3+OL)
Omx=lambda a: Om*a**-3/E(a)**2
P_pl=c**5/G

print("="*74); print("1.  IS ENERGY CONSERVED?   E = rho a^3  in a comoving box")
print("="*74)
print("  first law  dE = -p dV  =>  E ~ a^(-3w)")
for w,name in [(0,"matter   w=0"),(1/3,"radiation w=1/3"),(-1,"Lambda   w=-1")]:
    print(f"  {name:18s}  E ~ a^{-3*w:+.0f}   " +
          ("CONSTANT" if w==0 else "DECREASES -> energy simply gone" if w>0
           else "GROWS WITHOUT BOUND -> energy simply created"))
print("  => you are right: there is NO global energy conservation. Exact, standard GR.")
print("     No timelike Killing vector in FRW => no conserved Noether energy.")
print("     BUT: dE = -p dV is the REVERSIBLE first law. Comoving entropy is exactly")
print("     constant (perfect-fluid FRW is isentropic). Non-conservation != dissipation.\n")

print("="*74); print("2.  THE HUBBLE SPHERE IS NOT THE EDGE OF THE PAST LIGHT CONE")
print("="*74)
R_H=c/H0s
d_part=c*quad(lambda a: 1/(a**2*H0s*E(a)),1e-10,1)[0]     # particle horizon, proper now
d_evt =c*quad(lambda a: 1/(a**2*H0s*E(a)),1,np.inf)[0]     # event horizon, proper now
print(f"  Hubble radius     R_A = c/H0        = {R_H/Gly:7.2f} Gly   (v_rec = c HERE)")
print(f"  particle horizon  (all we ever saw) = {d_part/Gly:7.2f} Gly")
print(f"  event horizon     (all we ever will)= {d_evt/Gly:7.2f} Gly")
print(f"\n  recession speed of the CMB surface (z=1090): ", end="")
a_cmb=1/1091.
d_cmb=c*quad(lambda a: 1/(a**2*H0s*E(a)),a_cmb,1)[0]
print(f"v = H0*d = {H0s*d_cmb/c:.2f} c")
print("  We SEE it anyway. Superluminal recession is not an observational barrier;")
print("  the Hubble sphere grows and light crosses in. The past light cone has no leaky edge.")
print(f"\n  R_EH/R_A = {d_evt/R_H:.4f}   n = {E(1.0)/np.sqrt(OL):.4f}   (both -> 1 in de Sitter)")

print("\n"+"="*74); print("3.  BUT THERE *IS* AN EXACT ENERGY FLUX ACROSS THE APPARENT HORIZON")
print("="*74)
print("  Cai-Kim: put the Clausius relation  dQ = T dS  on the apparent horizon R_A=c/H,")
print("           with T = 1/(2 pi R_A) and S = A/4G.  Then")
print("           dQ = A (rho+p) H R_A dt   reproduces  Hdot = -4 pi G (rho+p)  EXACTLY.")
print("           The heat flux through the horizon IS the second Friedmann equation.\n")
print("  Evaluate it.  Only (rho+p) flows -- and rho_Lam + p_Lam = 0, so Lambda contributes")
print("  NOTHING.  The entire flux is matter:")
print("        dQ/dt = 4 pi R_A^3 H (rho+p) c^2 = (3/2) Omega_m * c^5/G\n")
for z in [0.0,0.3579,0.6313,2.0,10.0]:
    a=1/(1+z); Omz=Omx(a); H=H0s*E(a); RA=c/H
    rho=Omz*3*H**2/(8*np.pi*G)
    flux=4*np.pi*RA**3*H*rho*c**2
    n2=E(a)**2/OL
    print(f"   z={z:6.4f}  n^2={n2:9.4f}  Omega_m={Omz:.6f}  1-1/n^2={1-1/n2:.6f}"
          f"   flux={flux:.4e} W = {flux/P_pl:.6f} c^5/G")
print(f"\n  Planck power c^5/G = {P_pl:.4e} W")
print("  dQ/dt = (3/2)(1 - 1/n^2) * c^5/G     <-- THE LEAK IS EXACTLY THE DRAG")
print("  n -> 1  =>  flux -> 0 : de Sitter horizon is in equilibrium, nothing leaks.")
print(f"  at the grain crossing (n^2=2): flux = (3/2)(1/2) = 3/4 of a Planck power"
      f" = {0.75*P_pl:.3e} W")

print("\n"+"="*74); print("4.  SO IS IT FRICTION?")
print("="*74)
print("  friction: converts ordered energy to heat, produces entropy, irreversible.")
print("  this:     dE = -p dV, comoving entropy exactly constant, time-reversible.")
print("  => energy is NOT conserved, and the non-conservation is NOT dissipative.")
print("     It is reversible work against pressure with no reservoir on the other side.")
