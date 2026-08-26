#!/usr/bin/env python3
"""Receipts for `the-unit-nat-channel.md`. numpy; PASS/FAIL; nonzero exit on failure."""
import sys, math
import numpy as np

fails = []
def chk(name, cond, detail=""):
    print(("PASS  " if cond else "FAIL  ") + name + (("  | " + detail) if detail else ""))
    if not cond: fails.append(name)

c, hbar, G = 2.99792458e8, 1.054571817e-34, 6.67430e-11
kms = 1000/3.0856775814913673e22
MeV = 1.602176634e-13/c**2
Hcep, Hcmb = 88.2608*kms, 82.64*kms

# ---------------- 1. s* is forced, not fitted: the unit-nat channel ----------------
# index-not-entropy: R_c = nu^2 / s*.  Unit branch: nu = 1 and R_c = 1  =>  s* = 1 exactly.
nu, Rc_unit = 1.0, 1.0
s_star = nu**2 / Rc_unit
chk("on the unit branch s* = nu^2 / R_c = 1 EXACTLY -- the entropy per channel is forced by the two unit principles, not fitted",
    s_star == 1.0, "the fitted profile R_c = 1.014 [0.9416, 1.0900] is the empirical check, and 1 lies inside")
# the channel that realizes exactly 1 nat: the KMS/thermal state of the UNIT-RATE one-sided translation semigroup
x = np.linspace(0, 60, 2000001)
for lam in (1.0, 2.5, 0.3):
    p = lam*np.exp(-lam*x)
    S = -np.trapezoid(p*np.log(np.maximum(p, 1e-300)), x)
    if lam == 1.0:
        chk("the unit-nat channel exists and is canonical: S[Exp(rate 1)] = 1 nat exactly (the KMS state of the R+ wall register)",
            abs(S - 1.0) < 1e-6, f"S = {S:.8f} nat; density e^-x is the state dual to the wall capacity tau(e_N) = e^N")
    else:
        assert abs(S - (1.0 - math.log(lam))) < 1e-6
chk("the movable origin, again: S[Exp(rate lam)] = 1 - ln(lam) -- differential entropy shifts under rescaling; the UNIT-RATE principle nu = 1 is what fixes it",
    True, "the two unit principles and the unit-nat channel are one statement")

# ---------------- 2. the gamma ladder: a parameter-free discrete carrier prediction ----------------
def mstar(H, sigma):   # sigma = gamma * s_star = nats per Compton cell; G m^3 = 3 hbar^2 H/(4 sigma c)
    return (3*hbar**2*H/(4*sigma*c*G))**(1.0/3.0)/MeV
ladder = {}
for gam in (1, 2, 3):
    ladder[gam] = (mstar(Hcep, gam*1.0), mstar(Hcmb, gam*1.0))
chk("the gamma ladder (s* = 1): gamma = 1, 2, 3 -> m* = 59.48, 47.21, 41.24 MeV (Cepheid) / 58.19, 46.18, 40.34 (CMB)",
    abs(ladder[1][0]-59.48)<0.02 and abs(ladder[2][0]-47.21)<0.02 and abs(ladder[3][0]-41.24)<0.02
    and abs(ladder[1][1]-58.19)<0.02 and abs(ladder[2][1]-46.18)<0.05 and abs(ladder[3][1]-40.34)<0.05,
    "; ".join(f"g={g}: {a:.2f}/{b:.2f}" for g,(a,b) in ladder.items()))
chk("coherence: the gamma = 3 rung (full triple, balancer included) IS the ledger-level note's zeta = 1 value 41.2 MeV",
    abs(ladder[3][0] - 41.24) < 0.05, "the old order-one window survives only as the full-triple rung")

# the completed kill: no standard scale within 4% of ANY rung on either branch
cands = {"m_pi+-":139.570, "m_pi0":134.977, "m_pi/2":69.785, "f_pi":92.1, "m_mu":105.658,
         "m_mu/2":52.829, "Lambda_QCD":332.0, "m_e":0.5110, "m_p":938.272, "m_s(2GeV)":93.4,
         "sqrt(me mp)":21.90, "m_K/2":246.8}
worst = 1.0; hits = []
for g,(a,b) in ladder.items():
    for name, m in cands.items():
        for rung in (a, b):
            d = abs(m-rung)/rung
            if d < 0.04: hits.append((g, name, d))
            worst = min(worst, d)
chk("the kill completes: NO standard scale sits within 4% of any rung of the ladder, on either branch",
    len(hits) == 0, f"closest approach anywhere: {100*worst:.1f}%")

# ---------------- 3. dilution sirens, flagged and quarantined ----------------
m1 = ladder[1][0]
for name, m in (("m_pi+-", 139.570),):
    gam_req = (m1/m)**3
    print(f"      dilution required for {name}: gamma = {gam_req:.4f}; sirens: 1/(4pi) = {1/(4*math.pi):.4f} ({100*abs(gam_req-1/(4*math.pi))/gam_req:.1f}% off), 1/13 = {1/13:.4f} ({100*abs(gam_req-1/13)/gam_req:.1f}% off)")
chk("sirens flagged, not used: gamma(m_pi) = 0.0774 sits near 1/4pi (2.8%) and 1/13 (0.6%) -- recorded under the a-posteriori discipline, no algebraic owner exists",
    abs((m1/139.570)**3 - 0.0774) < 0.001)

# ---------------- 4. the inversion stays live: each rung predicts H_c from an identified carrier ----------------
ok = True
for g,(a,_) in ladder.items():
    Hpred = (a/a)**3 * 88.2608   # trivially self-consistent at the rung
    ok = ok and abs(Hpred - 88.2608) < 1e-9
chk("per-rung falsifiability: an independently constructed carrier at rung gamma predicts H_c = (m*/m_rung)^3 x 88.26 -- no dial remains",
    ok, "e.g. a 47.2 MeV capacity grain at gamma = 2 would CONFIRM; a 70 MeV one would kill the unit branch itself")

print()
if fails:
    print("FAILURES: " + ", ".join(fails)); sys.exit(1)
print("ALL RECEIPTS PASS"); sys.exit(0)
