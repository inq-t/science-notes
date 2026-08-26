#!/usr/bin/env python3
"""Receipts for deriving-g-v2. Stdlib only. Exits nonzero on any failed assertion.

What a pass establishes: every number quoted in the module's notes follows from
the declared constants, cosmology, and formulas. What it does NOT establish:
the wall construction, the channel reading, the fossil law, or any closure's
truth in nature. The equal-partition crossing z_c is a CONSTRUCTION (rho_X =
rho_crit/2 is linear bookkeeping), not a discovery -- asserted here only as
internal consistency.
"""
import json, math, random, sys

FAIL = []
def check(name, val, ref, rtol=1e-2):
    ok = (abs(val - ref) <= rtol * abs(ref)) if ref != 0 else (abs(val) <= rtol)
    if not ok: FAIL.append((name, val, ref))
    return val

# constants (SI, CODATA 2018) and Planck-2018 flat LCDM baseline
c, hbar, G, kB = 299792458.0, 1.054571817e-34, 6.67430e-11, 1.380649e-23
eV, Mpc, yr = 1.602176634e-19, 3.0856775814913673e22, 3.15576e7
H0 = 67.4e3 / Mpc; Om, OL = 0.315, 0.685

out = {}
lP2 = hbar * G / c**3
etaE = out["etaE_nat_per_m2"] = check("etaE", 1/(4*lP2), 9.5702e68, 1e-3)

# crossing cut: rho_X = rho_crit/2  <=>  E^2 = 2*OL (construction, not discovery)
zc = out["z_c"] = check("z_c", (OL/Om)**(1/3) - 1, 0.296, 2e-2)
Hc = H0 * math.sqrt(2*OL); out["Hc_over_H0"] = check("Hc/H0", Hc/H0, 1.1705, 1e-3)
Rc = c / Hc; Ac = 4*math.pi*Rc**2
out["T_c_K"] = check("T_c", hbar*Hc/(2*math.pi*kB), 3.11e-30, 1e-2)
out["M_c_kg_CIRCULAR"] = c**3/(2*G*Hc)  # contains G: inadmissible input
assert abs(OL/(Om*(1+zc)**3 + OL) - 0.5) < 1e-12  # bookkeeping identity only

# Closure C: holographic acceptance number
out["ledger_at_crossing_nats"] = check("N_ledger", Ac*etaE, 1.654e122, 1e-2)

# Closure A: fossil Weinberg. lambda^3 = 4*zeta*lP2*Rc, m = hbar/(lambda c)
def mMeV(lam): return hbar/(lam*c) * c**2 / (1e6*eV)
mA = mMeV((4*1.00*lP2*Rc)**(1/3)); mB = mMeV((4*0.25*lP2*Rc)**(1/3))
out["weinberg_mass_MeV_zeta1"]  = check("m*(zeta=1)", mA, 39.7, 1e-2)
out["weinberg_mass_MeV_zeta14"] = check("m*(zeta=1/4)", mB, 63.1, 1e-2)

# Kill 1: live running vs LLR
q0 = Om/2 - OL; opq = 1 + q0; H0yr = H0*yr; LLR = 1.5e-13
r1 = out["running_a1_per_yr"] = check("run a=1", 1*opq*H0yr, 3.26e-11, 1e-2)
r2 = out["running_a2_per_yr"] = check("run a=2", 2*opq*H0yr, 6.51e-11, 1e-2)
lam1 = (4*lP2*Rc)**(1/3)
rlog = out["running_log_per_yr"] = check("run log", opq*H0yr/math.log(Rc/lam1), 3.50e-13, 1e-2)
assert r1/LLR > 200 and r2/LLR > 400 and rlog/LLR > 2   # the kills
out["surviving_exponent"] = check("a_max", LLR/(opq*H0yr), 4.6e-3, 2e-2)

# Kill 2: channel-entropy extraction from the reported fit (REPORTED-LIMITED input)
fit, lo, hi = 1.025, 0.941, 1.088
out["s_star_nat"] = [round(1/hi, 4), round(1/lo, 4)]
assert not (lo <= 1/math.log(2) <= hi)   # qubit excluded (1.4427)
assert not (lo <= 1/math.log(3) <= hi)   # maximal qutrit excluded (0.9102)
# Jones ladder: every rigid value sits at or below ln 2
for n in range(3, 61):
    s_n = math.log(2*math.cos(math.pi/n))
    assert s_n <= math.log(2) + 1e-12
out["index_at_s1"] = check("Ind(e2)", math.exp(2*1.0), 7.389056, 1e-6)
assert math.exp(2*1.0) > 4.0             # above the Jones wall: continuum regime

# Closure B: NCG spectral closure. (96 f2 L^2)/(24 pi^2) = etaE/(4 pi)
f2L2 = (etaE/(4*math.pi)) * 24*math.pi**2 / 96
E_GeV = math.sqrt(f2L2) * hbar * c / (1e9*eV)
out["sqrt_f2_Lambda_GeV"] = check("sqrt(f2)L", E_GeV, 2.705e18, 1e-2)
out["f2_at_unification"] = check("f2@1.1e17", (E_GeV/1.1e17)**2, 605, 2e-2)

# Closure D: a=2 cell vs measured dark-energy length
lam4 = (4*lP2*Rc**2)**0.25
out["a2_cell_um"] = check("a2 cell", lam4*1e6, 61.6, 1e-2)
rhoc0 = 3*H0**2/(8*math.pi*G); E_DE = (OL*rhoc0*c**2*(hbar*c)**3)**0.25
lamDE = hbar*c/E_DE
out["DE_length_um"] = check("DE length", lamDE*1e6, 88.1, 1e-2)
out["a2_C"] = check("C(a=2)", (lamDE/lam4)**4, 4.19, 2e-2)

# Rulers are matter: ledger per Compton cell; sqrt = m_P/(2m)
mP = math.sqrt(hbar*c/G)
for label, m_kg, ref in [("proton", 1.67262192369e-27, 4.233e37),
                         ("electron", 9.1093837015e-31, 1.427e44)]:
    lamC = hbar/(m_kg*c); iota = lamC**2 * etaE
    out[f"ledger_per_{label}_cell"] = check(f"iota {label}", iota, ref, 1e-2)
    assert abs(math.sqrt(iota) - mP/(2*m_kg)) / (mP/(2*m_kg)) < 1e-9

# Leak register: P = (-Hdot/H^2) c^5/G
LPl = out["c5_over_G_W"] = check("c5/G", c**5/G, 3.628e52, 1e-2)
out["leak_today_W"] = check("P0", 1.5*Om*LPl, 1.714e52, 1e-2)
Omc = Om*(1+zc)**3/(2*OL)
out["leak_crossing_W"] = check("Pc", 1.5*Omc*LPl, 2.723e52, 1e-2)

# Cell identity receipt: S(chi)+D(chi||tau_d) = (1/2) log Ind_W = log d, diagonal states
rng = random.Random(7)
for d in (2, 3, 5, 7):
    w = [rng.random() for _ in range(d)]; s = sum(w); w = [x/s for x in w]
    S = -sum(x*math.log(x) for x in w)
    D = math.log(d) - S
    assert abs((S + D) - 0.5*math.log(d**2)) < 1e-12

print(json.dumps(out, indent=1))
if FAIL:
    print("FAILED:", FAIL, file=sys.stderr); sys.exit(1)
print("ALL RECEIPTS PASS")
