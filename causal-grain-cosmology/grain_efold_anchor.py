#!/usr/bin/env python3
"""
GRAIN-ANCHORED DARK ENERGY OVER E-FOLD TIME
Origin of the clock: the birth of mass (QCD crossover), NOT the big bang.
Free parameters: c, G, hbar  (+ the grain scale itself, from F_pi).
"""
import numpy as np

# ---------------------------------------------------------------- constants
c      = 2.99792458e8          # m/s
hbar_c = 197.3269804           # MeV fm
G      = 6.67430e-11
hbar   = 1.054571817e-34
l_P    = np.sqrt(hbar*G/c**3)  # m
l_P_fm = l_P*1e15
Mpc    = 3.0856775814913673e22  # m
kmsMpc = 1e3/Mpc                # s^-1 per (km/s/Mpc)

# ------------------------------------------------- the grain (chiral branch)
F_pi, dF_pi = 130.2, 1.2       # MeV  (PDG, f_pi convention sqrt2*92)
# E* on the chiral CH0 branch, calibrated in earlier sessions:
E_star  = 46.03                # MeV
dE_star = E_star*(dF_pi/F_pi)  # E* ~ F_pi  =>  fractional error carries over

def grain_chain(E):
    lam    = hbar_c/E                       # fm
    lam_m  = lam*1e-15
    R_c    = 3.0*lam_m**3/(8.0*l_P**2)      # m   <- lam^3 = (8/3) l_P^2 R_c
    H_c    = c/R_c                          # s^-1
    return lam, R_c, H_c

lam_star, R_c, H_c = grain_chain(E_star)
_,_,H_c_hi = grain_chain(E_star*(1-dF_pi/F_pi))   # E* down -> lam up -> H_c down
_,_,H_c_lo = grain_chain(E_star*(1+dF_pi/F_pi))
H_c_kms   = H_c/kmsMpc
dH_c_kms  = 0.5*abs(H_c_hi-H_c_lo)/kmsMpc

# ------------------------------------------------------------ LCDM backdrop
H0, Om, OL = 67.36, 0.3153, 0.6847
Or = 4.15e-5/(H0/100)**2
H0_s   = H0*kmsMpc
H_L    = H0*np.sqrt(OL)                    # km/s/Mpc, asymptotic de Sitter rate
H_L_s  = H_L*kmsMpc

n_c   = H_c_kms/H_L
dn_c  = dH_c_kms/H_L

print("="*74)
print("THE GRAIN CHAIN   lambda*^3 = (8/3) l_P^2 R_c ,  H_c = c/R_c")
print("="*74)
print(f"  E*        = {E_star:.2f} +- {dE_star:.2f} MeV      (from F_pi = {F_pi} +- {dF_pi})")
print(f"  lambda*   = {lam_star:.4f} fm")
print(f"  R_c       = {R_c:.4e} m  = {R_c/Mpc:.4e} Mpc")
print(f"  H_c       = {H_c_kms:.3f} +- {dH_c_kms:.3f} km/s/Mpc   (H_c ~ F_pi^3)")
print(f"  H_Lambda  = {H_L:.3f} km/s/Mpc                (= H0 sqrt(Omega_L))")
print()
print(f"  n_c   = H_c/H_Lambda = {n_c:.4f} +- {dn_c:.4f}     sqrt(2) = {np.sqrt(2):.4f}")
print(f"  n_c^2                = {n_c**2:.4f} +- {2*n_c*dn_c:.4f}     2       = 2")
print(f"  ->  {abs(n_c**2-2)/(2*n_c*dn_c):.2f} sigma from exactly 2   "
      f"({100*(n_c**2/2-1):+.1f}% in rho_Lambda, {100*(n_c/np.sqrt(2)-1):+.1f}% in H_Lambda)")

# -------------------------------------------- resolution depth, the monotone
def E_of_x(x):                       # x = ln a, a=1 today
    return np.sqrt(Or*np.exp(-4*x) + Om*np.exp(-3*x) + OL)
def N_P(x):                          # ln(R_A / l_P),  R_A = c/H
    return np.log(c/(H0_s*E_of_x(x)*l_P))
def one_plus_q(x):                   # dN_P/dx
    E = E_of_x(x)
    dlnH = 0.5*(-4*Or*np.exp(-4*x) - 3*Om*np.exp(-3*x))/E**2
    return -dlnH
def n_of_x(x):                       # H/H_Lambda = sqrt(1 + rho_m/rho_L)
    return E_of_x(x)/np.sqrt(OL)

NP_today = N_P(0.0)
NP_inf   = np.log(c/(H_L_s*l_P))
# grain prediction of the plateau, assuming n_c = sqrt(2)
H_L_pred   = H_c/np.sqrt(2)
NP_inf_pred= np.log(c/(H_L_pred*l_P))
NP_inf_alt = 3*np.log(lam_star*1e-15/l_P) + np.log(3*np.sqrt(2)/8)

print()
print("="*74)
print("THE SAME STATEMENT AS A RESOLUTION DEPTH   N_P = ln(R_A/l_P)")
print("="*74)
print(f"  N_P today            = {NP_today:.3f}")
print(f"  N_P asymptotic (obs) = {NP_inf:.3f}")
print(f"  N_P asymptotic (grain, n_c=sqrt2) = {NP_inf_pred:.3f}")
print(f"      closed form  3 ln(lambda*/l_P) + ln(3 sqrt2 / 8) = {NP_inf_alt:.3f}")
print(f"      3 ln(lambda*/l_P) = {3*np.log(lam_star*1e-15/l_P):.3f}"
      f"   ln(3sqrt2/8) = {np.log(3*np.sqrt(2)/8):.4f}")
print(f"  residual = {NP_inf_pred-NP_inf:+.4f} nats out of {NP_inf:.1f}"
      f"   ({100*(NP_inf_pred-NP_inf)/NP_inf:+.4f}%)")
print(f"  1-sigma band on the plateau from F_pi alone: +-{3*dF_pi/F_pi:.4f} nats")
print(f"  ->  {abs(NP_inf_pred-NP_inf)/(3*dF_pi/F_pi):.2f} sigma")

# ------------------------------------------------ the clock: birth of mass
T_QCD, g_QCD = 155.0, 17.25          # MeV, g_*s just below the crossover
T_0          = 2.7255*8.617333262e-11   # MeV
g_0          = 3.9384
a_ratio = (T_QCD/T_0)*(g_QCD/g_0)**(1/3.)
N_tot   = np.log(a_ratio)

def z_of_H(Htarget_kms):             # invert H(z) for the crossing redshift
    from scipy.optimize import brentq
    f = lambda x: H0*E_of_x(x) - Htarget_kms
    x = brentq(f, -3.0, 0.0)
    return np.exp(-x)-1, x

z_c,  x_c  = z_of_H(H_c_kms)
z_eq, x_eq = z_of_H(H_L*np.sqrt(2))          # rho_m = rho_L  (n = sqrt2)
z_acc,x_acc= z_of_H(H_L*np.sqrt(3))          # q = 0, acceleration onset (n=sqrt3)

print()
print("="*74)
print("E-FOLDS FROM THE BIRTH OF MASS")
print("="*74)
print(f"  T_QCD = {T_QCD} MeV -> T_0 = {T_0:.4e} MeV,  a_0/a_QCD = {a_ratio:.4e}")
print(f"  N_total (birth of mass -> now)      = {N_tot:.3f} e-folds")
for lbl, x, zz in [("acceleration onset  (n=sqrt3)", x_acc, z_acc),
                   ("matter-Lambda equality (n=sqrt2)", x_eq, z_eq),
                   ("GRAIN crossing H=H_c", x_c, z_c)]:
    print(f"  {lbl:34s} z={zz:6.4f}  N={N_tot+x:7.3f}  "
          f"({-x:.4f} e-folds ago)  N_P={N_P(x):.3f}")
print(f"  {'today':34s} z=0.0000  N={N_tot:7.3f}  (0.0000 e-folds ago)  N_P={NP_today:.3f}")

print()
print(f"  grain crossing vs matter-Lambda equality: {100*(H_c_kms/(H_L*np.sqrt(2))-1):+.2f}% in H,"
      f"  {abs(x_c-x_eq):.4f} e-folds apart")

np.savez("/home/claude/grain_efold.npz",
         N_tot=N_tot, x_c=x_c, x_eq=x_eq, x_acc=x_acc,
         H_c_kms=H_c_kms, dH_c_kms=dH_c_kms, H_L=H_L, n_c=n_c, dn_c=dn_c,
         NP_today=NP_today, NP_inf=NP_inf, NP_inf_pred=NP_inf_pred,
         lam_star=lam_star, E_star=E_star, H0=H0, Om=Om, OL=OL, Or=Or)
print("\nsaved -> grain_efold.npz")
