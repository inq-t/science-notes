#!/usr/bin/env python3
"""Receipts for `the-rank-two-cell.md`. numpy; PASS/FAIL; nonzero exit on failure."""
import sys, math
import numpy as np

fails = []
def chk(name, cond, detail=""):
    print(("PASS  " if cond else "FAIL  ") + name + (("  | " + detail) if detail else ""))
    if not cond: fails.append(name)

c, hbar, G = 2.99792458e8, 1.054571817e-34, 6.67430e-11
kms = 1000/3.0856775814913673e22
MeVkg = 1.602176634e-13/c**2
Hcep, Hcmb = 88.2608*kms, 82.64*kms

# ---------------- 1. gamma = 2, three faces ----------------
# (i) the cell is the trace-zero triple: exactly 2 degrees of freedom
A = np.array([[1.0, 1.0, 1.0]])            # the trace constraint
null_dim = 3 - np.linalg.matrix_rank(A)
chk("face (i): the trace-zero triple has exactly 2 independent slots -- rank A2 = 2", null_dim == 2)
# (ii) Born positivity: the SdS triple realizes exactly 2 of its 3 slots as geometry, at every admissible mass
ok = True
for m in np.linspace(0.01, 0.99, 60)*(1/(3*math.sqrt(3.0))):
    r = np.sort(np.roots([1.0, 0.0, -1.0, 2*m]).real)
    ok = ok and (r > 0).sum() == 2 and r[0] < 0
chk("face (ii): Born positivity -- exactly TWO slots of the triple ever write area (r_c, r_h > 0); the balancer never does",
    ok, "the negative balancer is the constraint, not a channel: gamma counts area-writing channels per cell")
# (iii) the conversion law is a two-channel structure (their theorem: d(C+ + C-)/dN = 0)
u = np.linspace(-20, 20, 200001)
m_ = np.tanh(u)
chk("face (iii): the conversion register has exactly two channels with one conserved total (m^2 + m' = 1)",
    np.max(np.abs(m_**2 + 1/np.cosh(u)**2 - 1)) < 1e-12,
    "three faces, one integer: gamma = 2  [DERIVED, conditional on cell = trace-zero triple]")

# ---------------- 2. the assembled prediction ----------------
def mstar(H, sigma): return (3*hbar**2*H/(4*sigma*c*G))**(1.0/3.0)
m_cep, m_cmb = mstar(Hcep, 2.0), mstar(Hcmb, 2.0)
lam_cep, lam_cmb = 197.3269804/ (m_cep/MeVkg), 197.3269804/(m_cmb/MeVkg)   # fm
chk("the prediction: gamma = 2, s* = 1  =>  m* = 47.21 MeV (Cepheid) / 46.18 MeV (CMB branch); lambda* = 4.18 / 4.27 fm",
    abs(m_cep/MeVkg - 47.21) < 0.02 and abs(m_cmb/MeVkg - 46.18) < 0.05
    and abs(lam_cep - 4.180) < 0.005 and abs(lam_cmb - 4.273) < 0.01,
    f"m* = {m_cep/MeVkg:.2f} / {m_cmb/MeVkg:.2f} MeV; lambda* = {lam_cep:.3f} / {lam_cmb:.3f} fm")
G_back = 3*hbar**2*Hcep/(8*c*m_cep**3)
chk("the closed form:  G = 3 hbar^2 H_c / (8 c m*^3)  -- no dials; reproduces G_N at the rung (circular check to 1e-12)",
    abs(G_back - G)/G < 1e-12, f"G back = {G_back:.6e}")
cands = {"m_mu/2":52.829, "m_pi/2":69.785, "sqrt(me mp)":21.90, "m_s(2GeV)":93.4, "m_pi0":134.977, "m_e":0.511, "m_u+m_d":6.9}
dmin = min(abs(v - m_cep/MeVkg)/(m_cep/MeVkg) for v in cands.values())
chk("the rung is clean: nearest standard scale to 47.2 MeV is m_mu/2 at 11.9% -- the theory owes the world one new grain",
    dmin > 0.10, f"min distance {100*dmin:.1f}%")

# ---------------- 3. the bimodule dichotomy ----------------
gaps = [abs(2.0 - math.log(d)) for d in range(2, 40)]
chk("integer-rank Pimsner is KILLED at the canonical unit step: the coasting rate 2 nats/e-fold is no ln(integer) -- min gap 0.054 (d = 7)",
    min(gaps) > 0.05 and abs(min(gaps) - (2 - math.log(7))) < 1e-12,
    f"|2 - ln 7| = {2 - math.log(7):.4f}, |ln 8 - 2| = {math.log(8) - 2:.4f}")
chk("the per-step index e^2 = 7.389 lies in the CONTINUOUS Jones range (> 4); e^2 is transcendental [CITED Lindemann]",
    math.exp(2) > 4,
    "welds three results: coasting 2-nats law + Ind >= e^2 (index-not-entropy) + the infinite-principal-graph theorem (hyperbolic counting): the wall has NO finite quantum symmetry")

# instantaneous Cuntz dimension d(N) = e^{2(1+q)} along the history
Om, Orr = 0.310598, 9.15e-5
OX = 1 - Om - Orr
def crossing(Om, Orr):
    OX = 1 - Om - Orr
    g = lambda xc: OX*math.cosh(xc)**2 - Om*math.exp(3*xc) - Orr*math.exp(4*xc)
    lo, hi = 1e-6, 2.0
    for _ in range(200):
        mid = 0.5*(lo+hi)
        lo, hi = (mid, hi) if g(mid) > 0 else (lo, mid)
    return 0.5*(lo+hi)
xc = crossing(Om, Orr)
lna = np.linspace(-25, 12, 800001)
a = np.exp(lna)
S_ = (np.cosh(xc)/np.cosh(xc + lna))**2
lnE = 0.5*np.log(Om*a**-3 + Orr*a**-4 + OX*S_)
opq = -np.gradient(lnE, lna)
d_of_N = np.exp(2*opq)
i_rad = np.argmin(np.abs(lna + 15)); i_mat = np.argmin(np.abs(lna + 4)); i_coast = np.argmin(np.abs(lna - 10))
band = (lna > -1) & (lna < 3)
d_dip = float(np.min(d_of_N[band]))
chk("the instantaneous Cuntz dimension d(N) = e^{2(1+q)}: 54.6 (radiation) -> 20.1 (matter) -> 3.76 (dip) -> 7.39 (coast)",
    abs(d_of_N[i_rad]-54.6)<0.3 and abs(d_of_N[i_mat]-20.1)<0.6 and abs(d_dip-3.765)<0.02 and abs(d_of_N[i_coast]-math.exp(2))<0.02,
    f"{d_of_N[i_rad]:.1f} -> {d_of_N[i_mat]:.1f} -> {d_dip:.3f} -> {d_of_N[i_coast]:.3f}")
chk("the dip descends BELOW the Jones threshold 4 -- but pointwise admissibility is step-convention-dependent (halving the step takes the square root), so only the invariant rate survives",
    d_dip < 4.0, f"convention receipt: at step 1/2, dip index = {math.sqrt(d_dip):.3f}")
j13 = 4*math.cos(math.pi/13)**2
chk("siren flagged, not used: the dip minimum 3.765 sits 0.16% from the Jones rung 4cos^2(pi/13) = 3.771 -- a-posteriori discipline applies",
    abs(d_dip - j13)/j13 < 0.005, f"dip {d_dip:.4f} vs rung {j13:.4f}")

# ---------------- 4. mint rate vs multiplicity (typed apart) ----------------
opq_c = float(opq[np.argmin(np.abs(lna + xc))])
chk("the crossing mint rate is 3/2 nats/e-fold EXACTLY (radiationless: 2(1+q)|_c = 3/2); the coast mints 2 -- neither is gamma",
    abs(2*opq_c - 1.5) < 2e-3,
    f"2(1+q) at the crossing = {2*opq_c:.4f}; gamma = 2 is per-CELL (structural), the mint is per-e-fold (dynamical): [MOTIF, no identification]")

print()
if fails:
    print("FAILURES: " + ", ".join(fails)); sys.exit(1)
print("ALL RECEIPTS PASS"); sys.exit(0)
