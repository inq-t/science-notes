#!/usr/bin/env python3
"""Boltzmann's ledger: verification of the wall's thermodynamic dictionary.
Planck units throughout (hats); kB = conversion, entropy in nats.
Conventions: C = A/4lP^2, Z = tP^2 H^2, master equation Z = pi/C."""
import sympy as sp, math

print("=== A. Exact wall identities [all symbolic] ===")
C = sp.symbols('C', positive=True)
Z = sp.pi/C; That = sp.sqrt(Z)/(2*sp.pi); S = C; rA = 1/sp.sqrt(Z); E = rA/2  # Misner-Sharp
checks = [
 ("kB T-hat = 1/(2 sqrt(pi C))            ", sp.simplify(That-1/(2*sp.sqrt(sp.pi*C)))==0),
 ("E_MS = T S                     (Euler) ", sp.simplify(E-That*S)==0),
 ("4 pi S T^2 = 1          (master, FRW)  ", sp.simplify(4*sp.pi*S*That**2)==1),
 ("Z = (2 pi T)^2                          ", sp.simplify(Z-(2*sp.pi*That)**2)==0),
 ("Z = 1/sqrt(V4),  V4=(c/H)^4  (Poisson) ", sp.simplify(Z-1/sp.sqrt(rA**4))==0)]
M = sp.symbols('M', positive=True)
checks += [
 ("Schwarzschild Smarr M = 2 T S           ", sp.simplify(M-2*(1/(8*sp.pi*M))*(4*sp.pi*M**2))==0),
 ("Schwarzschild 4 pi S T^2 = 1/4          ", sp.simplify(4*sp.pi*4*sp.pi*M**2/(8*sp.pi*M)**2)==sp.Rational(1,4))]
for name, ok in checks: print(f"  {name}: {ok}")

print("\n=== B. Descent calorimetry and Fermi-Dirac [symbolic] ===")
N,l1,l2,m1,m2 = sp.symbols('N lambda1 lambda2 mu1 mu2', positive=True)
Zp = m1*sp.exp(-l1*N)+m2*sp.exp(-l2*N); p = m1*sp.exp(-l1*N)/Zp; g = l2-l1
Nc = sp.log(m2/m1)/g
for name, ok in [
 ("Var(lambda) = g^2 p(1-p)   (Schottky)  ", sp.simplify(sp.diff(sp.log(Zp),(N,2))-g**2*p*(1-p))==0),
 ("d<lambda>/dN = -Var        (cooling)   ", sp.simplify(sp.diff(-sp.diff(sp.log(Zp),N),N)+sp.diff(sp.log(Zp),(N,2)))==0),
 ("p = 1/(1+e^{-g(N-Nc)})  (Fermi-Dirac)  ", sp.simplify(p-1/(1+sp.exp(-g*(N-Nc))))==0),
 ("Dp = g p(1-p)         (broadening)     ", sp.simplify(sp.diff(p,N)-g*p*(1-p))==0)]:
    print(f"  {name}: {ok}")
print(f"  widths (g=2): sech^2 FWHM = 2 arccosh(sqrt2) = {2*math.log(1+math.sqrt(2)):.3f} e-folds;"
      f"  FD 10-90 = ln(81)/... = 2 ln9/g = {math.log(81)/2:.3f} e-folds")

print("\n=== C. Crossing-capacity theorem [B4': symbolic, then numeric] ===")
rho_s, Cc = sp.symbols('rho_* C_c', positive=True)
# master: C(Nc) = pi/Z(Nc), Z = (8pi/3) rho_tot; B4': rho_tot(Nc) = 2 rho_*
Cc_expr = sp.pi/((8*sp.pi/3)*2*rho_s)
kap = 4*rho_s
print("  kappa * C(Nc) =", sp.simplify(kap*Cc_expr), "  [EXACT under B4': kappa = 3/(4 C_c)]")
print("  rho_* * C(Nc) =", sp.simplify(rho_s*Cc_expr), " [= 3/16]")
EX_peak = rho_s*(4*sp.pi/3)*((8*sp.pi/3)*2*rho_s)**sp.Rational(-3,2)  # rho_* V3(Nc)
print("  E_X(peak)/sqrt(C_c) =", sp.simplify(EX_peak/sp.sqrt(Cc_expr)), " [= 1/(4 sqrt(pi)) ~ 0.141 modular sigma]")
# numeric anchor
Om,h,Ncf = 0.3128, 0.6808, -0.2899
Z0 = (5.391247e-44*h*3.240779e-18)**2; C0 = math.pi/Z0
rhoc = 3*Z0/(8*math.pi); OX = 1-Om
rs = OX/(1/math.cosh(Ncf)**2)*rhoc; kapn = 4*rs
print(f"  numbers: C0 = {C0:.3e}; C_c = 3/(4 kappa) = {3/(4*kapn):.3e}; kappa = {kapn:.3e}")
print(f"  kappa*C0 = {kapn*C0:.3f} = (3/2) Om (1+z_c)^3 [Om-dependent; ~9/8 is coincidence -- declined]")
print(f"  E_X(today)/sqrt(C0) = {OX/(2*math.sqrt(math.pi)):.3f} = Omega_X/(2 sqrt pi)")
print(f"  wall temperature today: T = hbar H0/(2 pi kB) = {1.0545718e-34*h*3.240779e-18/(2*math.pi*1.380649e-23):.2e} K")

print("\n=== D. Endpoints (third-law fork) ===")
mu0 = sp.symbols('mu0', positive=True)
print("  Branch A: 4 pi S_inf T_inf^2 =", sp.simplify(4*sp.pi*(sp.pi/mu0)*(sp.sqrt(mu0)/(2*sp.pi))**2),
      " (fixed point obeys the same law; mu0 C_inf = pi)")
print("  Branch B: T -> 0 like 1/a, S -> inf like a^2: II_infinity, temperature floor absent")
