import numpy as np
hbar=1.054571817e-34; kB=1.380649e-23; cc=2.99792458e8; G=6.67430e-11
Mpc=3.0856775814913673e22; kms=1e3/Mpc
H0,Om,OL=67.36,0.3153,0.6847; HL=H0*np.sqrt(OL)

print("="*72); print("1.  IS THE DRAG A TEMPERATURE?   T_GH = hbar H / 2 pi k_B")
print("="*72)
T=lambda Hk: hbar*(Hk*kms)/(2*np.pi*kB)
print(f"  T(today)      = {T(H0):.4e} K      (H0 = {H0})")
print(f"  T(asymptotic) = {T(HL):.4e} K      (H_Lam = {HL:.3f})")
print(f"  T/T_Lam       = {T(H0)/T(HL):.6f}   n = H/H_Lam = {H0/HL:.6f}   IDENTICAL")
print("  => n IS the horizon-temperature ratio, exactly.  At the grain crossing T = sqrt2 T_Lam.")
a_dS=cc*(H0*kms)
print(f"\n  Unruh acceleration matching T(today): a = 2 pi c k_B T/hbar = c*H0 = {a_dS:.4e} m/s^2")
print(f"  c*H0/(2 pi) = {a_dS/(2*np.pi):.4e}   vs MOND a_0 ~ 1.2e-10   (known coincidence, NOT promoted)")

print("\n"+"="*72); print("2.  IF THE DRAG WERE LITERAL FRICTION (constant bulk viscosity zeta)")
print("="*72)
print("  rho_dot + 3H(rho + p_eff) = 0 ,  p_eff = -3 zeta H   ->   dv/dx = (3/2)(1-v), v=H/H_inf")
print("  EXACT SOLUTION:   n_visc = 1 + B a^(-3/2)")
print("  vs LCDM:          n_LCDM = sqrt(1 + K a^(-3))")
n0=1/np.sqrt(OL); K=n0**2-1; B=n0-1
print(f"\n  matched at today: n0 = {n0:.4f}  ->  K = {K:.4f},  B = {B:.4f}")
# acceleration onset
a_l=(2/K)**(-1/3.); z_l=1/a_l-1
a_v=(2/B)**(-1/1.5); z_v=1/a_v-1     # 1.5(n-1)/n = 1  ->  n = 3
print(f"  q=0 in LCDM   :  n^2 = 3  ->  z = {z_l:.4f}")
print(f"  q=0 in viscous:  n   = 3  ->  z = {z_v:.4f}    <-- excluded by supernovae by a mile")
print(f"\n  late-time approach to de Sitter:  LCDM  n-1 ~ a^-3 ;  viscous  n-1 ~ a^-1.5")
print("  => 'space has literal friction' is a DIFFERENT expansion history, and it is ruled out.")
for z in [0.0,0.3579,0.6313,1.0,3.0]:
    a=1/(1+z); print(f"    z={z:6.4f}   n_LCDM={np.sqrt(1+K*a**-3):.4f}   n_visc={1+B*a**-1.5:.4f}")

print("\n"+"="*72); print("3.  IS FRICTION EVEN ALLOWED?  (time-reversal test)")
print("="*72)
print("  Friedmann:  H^2 = (8 pi G/3) rho ,  rho_dot = -3H(rho+p)")
print("  Under t -> -t :  H -> -H , rho -> rho .  Both equations map to themselves.")
print("  A friction term (+ b H) would flip sign and BREAK the symmetry.")
print("  => the background evolution is time-reversible; there is no dissipation in it.")
print("     Whatever n is, it cannot be friction.")
