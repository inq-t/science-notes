import numpy as np
from scipy.optimize import brentq
print("="*72)
print("IS THE FRIEDMANN CONSTRAINT LITERALLY THE SdS HORIZON EQUATION?")
print("="*72)
print("  flat FRW, matter+Lambda:   Omega_m + Omega_L = 1")
print("  with  Omega_m = r_s/R_A   and   Omega_L = Lam R_A^2/3 :")
print("       r_s/R_A + Lam R_A^2/3 = 1")
print("   <=> 1 - 2GM/R_A - Lam R_A^2/3 = 0   ==   f(R_A) = 0   <-- SdS lapse")
print("  So R_A is a root of the A_2 cubic at EVERY instant, with M = mass inside.\n")

# enclosed mass in Nariai units:  2GM sqrt(Lam) = sqrt3 (n^2-1)/n^3
f = lambda n: np.sqrt(3)*(n**2-1)/n**3
ns = np.linspace(1.0001, 12, 400000)
i  = np.argmax(f(ns))
print("="*72); print("DOES THE ENCLOSED MASS EVER EXCEED THE NARIAI BOUND?")
print("="*72)
print(f"  2GM*sqrt(Lam) = sqrt3 (n^2-1)/n^3 ,   n = H/H_Lambda")
print(f"  numerical max at n  = {ns[i]:.6f}      sqrt(3) = {np.sqrt(3):.6f}")
print(f"  numerical max value = {f(ns[i]):.8f}   2/3     = {2/3:.8f}")
print(f"  analytic:  d/dn[(n^2-1)/n^3] = (3-n^2)/n^4  ->  n^2 = 3 exactly")
print(f"             value there = sqrt3*2/3^(3/2) = 2/3 = the Nariai mass exactly\n")
for n2 in [1e6, 100, 9, 4, 3, 2, 1.5, 1.0001]:
    n=np.sqrt(n2)
    print(f"   n^2={n2:10.4f}  Omega_m={1-1/n2:.4f}  2GM sqrt(Lam)={f(n):.6f}"
          f"  {'  <-- NARIAI SATURATED (q=0)' if abs(n2-3)<1e-9 else ''}")
print("\n  => M(t) rises, touches the Nariai bound EXACTLY at q=0, then falls forever.")
print("     FRW+Lambda saturates the SdS cubic's degenerate point once and never crosses it.")

print("\n"+"="*72); print("WHERE THE GRAIN CROSSING SITS RELATIVE TO IT")
print("="*72)
nc2, err = 2.1535, 0.1191
print(f"  grain crossing n_c^2 = {nc2} +- {err}")
print(f"     vs Nariai n^2=3 :  {abs(nc2-3)/err:.2f} sigma  -> EXCLUDED")
print(f"     vs halfway n^2=2 :  {abs(nc2-2)/err:.2f} sigma  -> allowed")
print("  The cubic supplies 3.  It does not supply 2.")
