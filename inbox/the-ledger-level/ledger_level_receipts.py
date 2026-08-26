#!/usr/bin/env python3
"""Receipts for `the-ledger-level.md`. numpy; PASS/FAIL; nonzero exit on failure.
Imported constants CODATA/SI; imported H_c values flagged in the note."""
import sys, math
import numpy as np

fails = []
def chk(name, cond, detail=""):
    print(("PASS  " if cond else "FAIL  ") + name + (("  | " + detail) if detail else ""))
    if not cond: fails.append(name)

c, hbar, G, kB = 2.99792458e8, 1.054571817e-34, 6.67430e-11, 1.380649e-23
lP2 = G*hbar/c**3; tP = math.sqrt(hbar*G/c**5)
mP  = math.sqrt(hbar*c/G)
kms = 1000/3.0856775814913673e22
MeV = 1.602176634e-13/c**2          # kg per MeV/c^2
Hcep, Hcmb = 88.2608*kms, 82.64*kms # Cepheid-branch and CMB-branch crossing rates

# ---------- 1. the five presentations of one ledger ----------
iota  = lambda H: math.pi*c**5/(G*hbar*H**2)
alphaG= lambda H: G*hbar*H**2/c**5
L = c/Hcep
a = np.linspace(0, L, 400001)
Theta0 = (3*math.pi*c**3/(2*G*hbar))*np.trapezoid(a*np.sqrt(np.maximum(1-a**2/L**2,0)), a)
chk("normalization restored: Theta0 = (3 pi c^3/2G hbar) int a sqrt(1-a^2/L^2) da = pi L^2/(2 lP^2) = iota/2",
    abs(Theta0 - math.pi*L**2/(2*lP2)) < 1e-6*Theta0 and abs(2*Theta0 - iota(Hcep)) < 1e-5*iota(Hcep),
    f"2 Theta0 = {2*Theta0:.6e} vs iota = {iota(Hcep):.6e}")
TH = hbar*Hcep/(2*math.pi*kB); EH = c**5/(2*G*Hcep)
chk("five presentations: beta E_H = pi/alpha_G = iota_H (Boltzmann exponent = inverse coupling = ledger)",
    abs(EH/(kB*TH) - iota(Hcep)) < 1e-9*iota(Hcep) and abs(math.pi/alphaG(Hcep) - iota(Hcep)) < 1e-9*iota(Hcep))
chk("packet numbers: T_c = 3.4772e-30 K, iota_c = 1.3211e122, n_q = 1.9059e122, M_MS = 7.0568e52 kg",
    abs(TH-3.4772e-30)<1e-33 and abs(iota(Hcep)-1.3211e122)<1e118
    and abs(iota(Hcep)/math.log(2)-1.90595e122)<1e118 and abs(c**3/(2*G*Hcep)-7.05682e52)<1e48,
    f"T={TH:.4e} K, iota={iota(Hcep):.6e}, M_MS={c**3/(2*G*Hcep):.4e} kg")
epsP = c**7/(hbar*G**2); epscrit = 3*Hcep**2*c**2/(8*math.pi*G)
chk("vacuum catastrophe factor: eps_P/eps_crit = (8/3) iota  (inverse capacity, NOT the tunneling weight)",
    abs(epsP/epscrit - (8.0/3.0)*iota(Hcep)) < 1e-9*epsP/epscrit, f"= {epsP/epscrit:.5e}")

# ---------- 2. three different 'crossing ledgers', disambiguated ----------
OmL, H0L = 0.6847, 67.36*kms                      # LCDM bookkeeping [IMPORTED]
H_lcdm_cross = H0L*math.sqrt(2*OmL)
chk("disambiguation: 1.654e122 is the LCDM Lambda=matter bookkeeping crossing; CST branches give 1.507/1.321e122",
    abs(iota(H_lcdm_cross)-1.654e122) < 4e119 and abs(iota(Hcmb)-1.507e122) < 4e119 and abs(iota(Hcep)-1.321e122) < 4e119,
    f"LCDM {iota(H_lcdm_cross):.4g}; CMB-branch {iota(Hcmb):.4g}; Cepheid {iota(Hcep):.4g}")

# ---------- 3. the sixth-root bridge (fossil Weinberg <-> ledger level) ----------
def mstar(H, zeta): return (hbar**2*H/(4*zeta*c*G))**(1.0/3.0)
ok = True
for H in (Hcep, Hcmb):
    for z in (0.25, 1.0, 4.0):
        m = mstar(H, z)
        ok = ok and abs((math.pi/(16*z**2))*(mP/m)**6 - iota(H)) < 1e-9*iota(H)
chk("sixth-root bridge [EXACT]: G m*^3 = hbar^2 H/(4 zeta c)  <=>  iota_A = (pi/16 zeta^2)(m_P/m*)^6", ok)
m1 = mstar(Hcep,1.0)/MeV; m2 = mstar(Hcmb,1.0)/MeV
chk("carrier window: m*(zeta=1) = 41.2 MeV (Cepheid) / 40.3 MeV (CMB branch); 63 MeV needs zeta = 0.28",
    abs(m1-41.2)<0.5 and abs(m2-40.3)<0.5 and abs((m1/63.0)**3-0.28)<0.02,
    f"m* = {m1:.2f} / {m2:.2f} MeV")
m = mstar(Hcep,1.0)
chk("the level in nats: ln iota = 6 ln(m_P/m*) - ln(16 zeta^2/pi)  --  281.2 = 6 x 47.13 - 1.63",
    abs(math.log(iota(Hcep)) - (6*math.log(mP/m) - math.log(16/math.pi))) < 1e-9,
    f"ln iota = {math.log(iota(Hcep)):.2f}; ln(m_P/m*) = {math.log(mP/m):.2f}")
lam = hbar/(m*c)
chk("volume = age: (lambda*/l_P)^3 = 4 zeta / (H_c t_P) -- one carrier Compton volume = 4 zeta x the age in Planck ticks",
    abs((lam/math.sqrt(lP2))**3 - 4.0/(Hcep*tP)) < 1e-9*(lam**3/lP2**1.5),
    f"both = {(lam/math.sqrt(lP2))**3:.4e}")
Rc = c/Hcep
chk("bulk = area [EXACT in the closure]: iota_A = 4 pi zeta (R_H/lambda*)^3 -- the horizon count IS the bulk Compton-cell count",
    abs(4*math.pi*(Rc/lam)**3 - iota(Hcep)) < 1e-9*iota(Hcep),
    f"R_H/lambda* = {Rc/lam:.4e}; 4pi(.)^3 = {4*math.pi*(Rc/lam)**3:.4e}")

# ---------- 4. rulers-are-matter cross-checks; the factorization is ruler-independent ----------
mp_, me_ = 1.67262192369e-27, 9.1093837015e-31
ok = True; cells = []
for mr in (mp_, me_):
    lamr = hbar/(mr*c)
    per_cell = (lamr**2)/(4*lP2)                      # = (m_P/2m)^2
    Ncells   = 4*math.pi*Rc**2/lamr**2
    ok = ok and abs(per_cell - (mP/(2*mr))**2) < 1e-9*per_cell
    ok = ok and abs(Ncells*per_cell - iota(Hcep)) < 1e-9*iota(Hcep)
    cells.append(per_cell)
chk("rulers are matter: per-cell ledger = (m_P/2m)^2 -- proton 4.233e37, electron 1.427e44; N_cells x per-cell = iota for EVERY ruler",
    ok and abs(cells[0]-4.233e37)<2e34 and abs(cells[1]-1.427e44)<2e41,
    f"proton {cells[0]:.4g}, electron {cells[1]:.4g}")

# ---------- 5. consistency with the one-channel cut (note 5) ----------
chk("temporal reduction consistency: ln iota_A,c = 2 ln( sqrt(pi)/(H_c t_P) ) exactly",
    abs(math.log(iota(Hcep)) - 2*math.log(math.sqrt(math.pi)/(Hcep*tP))) < 1e-12)

print()
if fails:
    print("FAILURES: " + ", ".join(fails)); sys.exit(1)
print("ALL RECEIPTS PASS"); sys.exit(0)
