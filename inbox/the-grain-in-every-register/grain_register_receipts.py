#!/usr/bin/env python3
"""Receipts for `the-grain-in-every-register.md` [EXPLORATORY -- SIREN COUNTRY].

Audits: (A) the register table; (B) the three structural identities
(holographic cell, saturation, mixing line) to 1e-12; (C) Zel'dovich made
exact + the pion overshoot; (D) the 2/3 signature and the rank-meter;
(E) the siren census with measured density and bit pricing, kappa_d from PDG
masses, the H0 oracle with Planck gate, and the m_s(mu) deflation;
(F) the BBN kill of naive running (both directions); (G) the H3 area-law
motif. numpy; PASS/FAIL; nonzero exit on failure.
"""
import sys, math
import numpy as np

fails = []
def chk(name, cond, detail=""):
    print(("PASS  " if cond else "FAIL  ") + name + (("  | " + detail) if detail else ""))
    if not cond: fails.append(name)

# ---------------- constants and anchors (as committed) ----------------
c    = 2.99792458e8
hbar = 1.054571817e-34
G    = 6.67430e-11
kB   = 1.380649e-23
Mpc  = 3.0856775814913673e22
kms  = 1000.0/Mpc
MeVkg= 1.602176634e-13/c**2
hbarc= 197.3269804                      # MeV fm
mP   = math.sqrt(hbar*c/G)
lP2  = hbar*G/c**3
Hcmb = 82.64*kms                        # CMB-branch crossing rate
Hcep = 88.2608*kms                      # Cepheid branch
zeta, sstar, gamma = 2.0/3.0, 1.0, 2.0
E_fix = 82.64/67.84                     # committed branch composition (FLAGGED in owners)

def mstar(H): return (hbar**2*H/(4*zeta*c*G))**(1.0/3.0)
def iota(H):  return math.pi*c**5/(G*hbar*H**2)
m_cmb = mstar(Hcmb); mMeV = m_cmb/MeVkg
m_cep = mstar(Hcep)

# ================================================== A. the register table
lam = hbar/(m_cmb*c); tau = hbar/(m_cmb*c**2); Tst = m_cmb*c**2/kB
ast = c**2/lam; alg = G*m_cmb**2/(hbar*c)
cell_eps = mMeV/ (lam/1e-15)**3                      # MeV / fm^3
bond_MeV = alg*mMeV
chk("registers: m* = 46.19 MeV; lambda* = 4.272 fm; tau* = 1.425e-23 s; T* = 5.36e11 K",
    abs(mMeV-46.19) < 0.05 and abs(lam*1e15-4.272) < 0.005 and abs(tau-1.425e-23) < 5e-26 and abs(Tst-5.36e11) < 5e9,
    f"m* = {mMeV:.2f} MeV, lambda* = {lam*1e15:.3f} fm, tau* = {tau:.3e} s, T* = {Tst:.3e} K")
chk("registers: a* = c^2/lambda* = 2.10e31 m/s^2; cell density 0.592 MeV/fm^3; pair bond 6.6e-40 MeV",
    abs(ast-2.104e31)/2.104e31 < 0.01 and abs(cell_eps-0.592) < 0.006 and abs(bond_MeV-6.61e-40)/6.61e-40 < 0.02,
    f"a* = {ast:.3e}, eps_cell = {cell_eps:.4f} MeV/fm^3, bond = {bond_MeV:.2e} MeV")

# ================================================== B. structural identities (exact)
for tag, H, m_ in (("CMB", Hcmb, m_cmb), ("Cepheid", Hcep, m_cep)):
    lam_ = hbar/(m_*c); RH = c/H
    chk(f"holographic cell ({tag}): lambda*^3 = 4 zeta l_P^2 R_H  (Planck-area column of Hubble depth)",
        abs(lam_**3 - 4*zeta*lP2*RH)/lam_**3 < 1e-12,
        f"lambda*^3 = {lam_**3:.4e} m^3 = (8/3) x {lP2:.3e} m^2 x {RH:.3e} m")
    N = (4*math.pi/3)*RH**3/lam_**3
    chk(f"SATURATION ({tag}): iota = gamma s* N_cells -- wall channel count = bulk cell census, exactly",
        abs(iota(H) - gamma*sstar*N)/iota(H) < 1e-12,
        f"N_cells = {N:.4e}; gamma s* N = {gamma*sstar*N:.4e} = iota = {iota(H):.4e}")
mH = hbar*Hcmb/c**2
chk("mixing line: m* = (m_P^2 m_H / (4 zeta))^{1/3} -- the grain sits at a = gamma/3 = 2/3 on m_P^a m_H^{1-a}",
    abs((mP**2*mH/(4*zeta))**(1.0/3.0) - m_cmb)/m_cmb < 1e-12,
    f"m_H = {mH/MeVkg*1e6:.3e} eV; (m_P^2 m_H)^(1/3) = {((mP*mP*mH)**(1.0/3.0))/MeVkg:.1f} MeV before (4zeta)^(-1/3)")
a_half = math.sqrt(mP*mH)/MeVkg*1e6                  # eV
H0_SI = Hcmb/E_fix
epsX0 = (1-0.310711-9.15e-5)*3*H0_SI**2*c**2/(8*math.pi*G)
epsX0_eV4 = epsX0*(1.9732698e-7)**3/1.602176634e-19
de_quantum = epsX0_eV4**0.25
chk("the a = 1/2 point is the dark-energy quantum, to order unity [FLAGGED band, not exact]",
    4.5e-3 < a_half < 4.8e-3 and 2.0e-3 < de_quantum < 2.5e-3 and 1.5 < a_half/de_quantum < 3.0,
    f"sqrt(m_P m_H) = {a_half:.2e} eV vs eps_X0^(1/4) = {de_quantum:.2e} eV (ratio {a_half/de_quantum:.2f})")

# ================================================== C. Zel'dovich made exact
eps_crit_c = 3*Hcmb**2*c**2/(8*math.pi*G)
zeld = (8.0/(3*math.pi))*G*m_cmb**2/lam**4
zeld2 = (8.0/(3*math.pi))*G*c**4*m_cmb**6/hbar**4
chk("Zel'dovich EXACT: eps_crit,c = (8/3pi) G m*^2/lambda*^4 = (8/3pi) G c^4 m*^6/hbar^4",
    abs(zeld-eps_crit_c)/eps_crit_c < 1e-12 and abs(zeld2-eps_crit_c)/eps_crit_c < 1e-12,
    f"one grain-pair bond per cell: {eps_crit_c:.4e} J/m^3")
pion_factor = (139.570/mMeV)**6
rho_ratio = pion_factor*E_fix**2/(1-0.310711-9.15e-5)
chk("Zel'dovich's 1967 pion version = this identity with the wrong grain: overshoots rho_Lambda by ~1.6e3",
    700 < pion_factor < 830 and 1.3e3 < rho_ratio < 2.0e3,
    f"(m_pi/m*)^6 = {pion_factor:.0f}; vs rho_Lambda,0: x{rho_ratio:.0f}")

# ================================================== D. the 2/3 signature and the rank-meter
u = np.linspace(-30, 30, 200001)
w = -1 + (gamma/3.0)*np.tanh(u)
chk("rapidity register: max|1+w| = gamma/3 = 2/3 exactly -- the pulse's boost saturation",
    abs(float(np.max(np.abs(1+w))) - 2.0/3.0) < 1e-9)
def rank_meter(w0, wa):
    A, B = 1.0+w0, -wa
    return 1.5*(B + math.sqrt(B*B + 4*A*A))
ok = True
for g_true in (1.0, 2.0, 3.0):
    for t in (0.1, 0.294, 0.6):
        w0 = -1 + (g_true/3)*t; wa = -(g_true/3)*(1-t*t)
        ok = ok and abs(rank_meter(w0, wa) - g_true) < 1e-12
chk("rank-meter inversion: gamma = (3/2)[-wa + sqrt(wa^2 + 4(1+w0)^2)] recovers gamma exactly on the family", ok)
g_bench = rank_meter(-0.8094545, -0.6122053)
chk("the sky reads the rank: benchmark (w0, wa) returns gamma = 2.000000",
    abs(g_bench - 2.0) < 3e-6, f"gamma = {g_bench:.7f}")
desi = {"DESI+CMB+Pantheon+": (-0.838, -0.62), "DESI+CMB+DESY5": (-0.752, -0.86), "DESI+CMB+Union3": (-0.667, -1.09)}
gvals = {k: rank_meter(*v) for k, v in desi.items()}
chk("DESI DR2 combos [CITED -- verify at intake]: rank-meter reads 1.98 / 2.78 / 3.55 -- rank 2 comfortable, rank 3 open",
    abs(gvals["DESI+CMB+Pantheon+"] - 1.98) < 0.05 and 2.6 < gvals["DESI+CMB+DESY5"] < 3.0 and 3.3 < gvals["DESI+CMB+Union3"] < 3.8,
    "; ".join(f"{k.split('+')[-1]}: {v:.2f}" for k, v in gvals.items()))

# ================================================== E. the siren census
bases = {
    "m_e": 0.51100, "m_mu": 105.658, "m_pi0": 134.977, "m_pi+-": 139.570,
    "m_K+-": 493.677, "m_K0": 497.611, "m_eta": 547.862, "m_rho": 775.26,
    "m_omega": 782.66, "m_p": 938.272, "m_n": 939.565, "dm_np": 1.29333,
    "m_deuteron": 1875.61, "B_d": 2.224566, "f_pi": 130.2/math.sqrt(2.0),
    "f_K": 110.1, "Lam_QCD_nf3": 332.0, "Lam_QCD_nf5": 210.0,
    "m_u(2GeV)": 2.16, "m_d(2GeV)": 4.67, "m_s(2GeV)": 93.4,
    "sqrt(me*mmu)": math.sqrt(0.511*105.658), "sqrt(me*mp)": math.sqrt(0.511*938.272),
}
mp_, mn_, Bd_ = 938.27209, 939.56542, 2.224566
mu_np = mp_*mn_/(mp_+mn_)
kappa_d = math.sqrt(2*mu_np*Bd_)
bases["kappa_d"] = kappa_d
chk("kappa_d from PDG masses: sqrt(2 mu_np B_d) = 45.70 MeV; 1/kappa_d = 4.318 fm (the np halo scale)",
    abs(kappa_d - 45.70) < 0.01 and abs(hbarc/kappa_d - 4.318) < 0.005,
    f"kappa_d = {kappa_d:.4f} MeV; 1/kappa_d = {hbarc/kappa_d:.4f} fm; |kappa_d - m*|/m* = {abs(kappa_d-mMeV)/mMeV*100:.2f}%")
mult_rat = [0.25, 1.0/3, 0.5, 2.0/3, 0.75, 1.0, 4.0/3, 1.5, 2.0, 3.0, 4.0]
mult_irr = [math.sqrt(2), 1/math.sqrt(2), math.pi, 1/math.pi, 2*math.pi, 1/(2*math.pi), math.pi/2, 2/math.pi]
def census(mults):
    vals = []
    for bname, b in bases.items():
        for m_ in mults:
            v = b*m_
            if mMeV/math.sqrt(2) < v < mMeV*math.sqrt(2):
                vals.append((v, f"{bname} x {m_:.4g}"))
    seen, out = set(), []
    for v, n in sorted(vals):
        key = round(math.log(v)/0.002)
        if key not in seen: seen.add(key); out.append((v, n))
    return out
c_rat = census(mult_rat); c_full = census(mult_rat + mult_irr)
D_rat, D_full = len(c_rat)/math.log(2), len(c_full)/math.log(2)
near = sorted(c_full, key=lambda t: abs(math.log(t[0]/mMeV)))[:5]
print("      census top-5 nearest to the grain: " + "; ".join(f"{n} = {v:.2f} ({abs(v/mMeV-1)*100:.2f}%)" for v, n in near))
chk("the census: sub-percent rhymes are CHEAP here -- density > 40/nat (full), > 20/nat (rational-only); nearest < 1%",
    D_full > 40 and D_rat > 20 and abs(near[0][0]/mMeV - 1) < 0.01,
    f"density = {D_full:.0f}/nat (full), {D_rat:.0f}/nat (rational); {len(c_full)} candidates in the octave")
f_hit = abs((130.2/math.sqrt(2)/2)/mMeV - 1)
p_null = min(1.0, 2*f_hit*D_full)
chk("pricing: the sharpest siren (f_pi/2, 0.3%) is a ~coin-flip under the census null -- worth ~1-2 bits, NO promotion",
    0.15 < p_null < 0.9, f"P_null(<= {f_hit*100:.2f}%) = {p_null:.2f} => {-math.log2(p_null):.1f} bits")
mirage = math.sqrt(0.511*105.658)*2*math.pi
lam_mir = 2*abs(mirage/mMeV - 1)*D_full
chk("the census's own object lesson: nearest hit is the mirage sqrt(m_e m_mu)*2pi at 0.04% -- no mechanism register, order-statistic ~3% null event, set-choice look-elsewhere shrinks it further",
    abs(mirage - 46.17) < 0.02 and abs(mirage/mMeV - 1) < 1e-3 and 0.01 < lam_mir < 0.10,
    f"sqrt(m_e m_mu)*2pi = {mirage:.3f} MeV ({abs(mirage/mMeV-1)*100:.3f}%); E[hits <= this] = {lam_mir:.3f} => ~{-math.log2(lam_mir):.0f} bits ceiling")
# the H0 oracle: every candidate grain names its own Hubble constant
def H0_of(m_MeV):
    H = 4*zeta*G*c*(m_MeV*MeVkg)**3/hbar**2
    return H/kms/E_fix
chk("H0 oracle round trip: H0(m* = 46.19) = 67.84", abs(H0_of(mMeV) - 67.84) < 1e-9)
oracle = {"kappa_d": H0_of(kappa_d), "f_pi/2": H0_of(130.2/math.sqrt(2)/2),
          "m_s(2GeV)/2": H0_of(93.4/2), "m_mu/2": H0_of(105.658/2), "m_pi+-/2": H0_of(139.570/2),
          "mirage": H0_of(mirage)}
print("      oracle H0 per candidate: " + "; ".join(f"{k}: {v:.2f}" for k, v in oracle.items()))
chk("oracle gates: kappa_d -> 65.7 (3.0 sigma BELOW Planck 67.36+-0.54: disfavored); f_pi/2 -> 67.2 (inside branch, survives)",
    abs(oracle["kappa_d"] - 65.71) < 0.05 and (67.36 - oracle["kappa_d"])/0.54 > 2.5
    and abs(oracle["f_pi/2"] - 67.15) < 0.05 and 66.5 < oracle["f_pi/2"] < 68.5,
    f"Planck gate on kappa_d: {(67.36-oracle['kappa_d'])/0.54:.1f} sigma")
chk("oracle gates: m_s/2 -> 70.1 (splits the fork); m_mu/2 -> 101.5 and m_pi/2 -> 234 (dead, existing kills)",
    abs(oracle["m_s(2GeV)/2"] - 70.11) < 0.1 and abs(oracle["m_mu/2"] - 101.5) < 0.3 and abs(oracle["m_pi+-/2"] - 234) < 2)
# m_s(mu) deflation: 1-loop running sweeps m_s/2 across the whole window
def alpha_s(mu, Lam=0.29, nf=4):
    b0 = 11 - 2*nf/3.0
    return 4*math.pi/(b0*math.log(mu**2/Lam**2))
ms2 = 93.4
ms = lambda mu: ms2*(alpha_s(mu)/alpha_s(2.0))**(12.0/25.0)
chk("m_s/2 deflated: 1-loop m_s(mu) sweeps by >1.8x over mu = 1-91 GeV, so m_s(mu)/2 hits ANY target near 46 -- scheme shopping",
    ms(1.0)/ms(91.0) > 1.8 and ms(91.0)/2 < mMeV < ms(1.0)/2,
    f"m_s/2 sweeps [{ms(91.0)/2:.1f}, {ms(1.0)/2:.1f}] MeV as mu runs 91 -> 1 GeV")

# ================================================== F. the running question (kills)
gstar, T_MeV, mP_MeV = 10.75, 1.0, mP/MeVkg
H_BBN = 1.66*math.sqrt(gstar)*T_MeV**2/mP_MeV * (1.602176634e-13/hbar)
chk("KILL naive running G ~ H: G_BBN/G_0 = H_BBN/H_0 ~ 3e17 vs BBN bound |dG|/G < 0.2 -- dead by 18 orders",
    H_BBN/H0_SI > 1e17, f"H_BBN = {H_BBN:.2f} s^-1; H_BBN/H_0 = {H_BBN/H0_SI:.2e}")
m_run = mMeV*(H_BBN/Hcmb)**(1.0/3.0)
chk("KILL the dual escape: a co-running grain (m*^3 ~ H) would weigh ~29 TeV at BBN -- 'fixed matter scale' dies instead",
    2.5e7 < m_run < 3.3e7, f"m*(BBN) = {m_run/1e6:.1f} TeV; the freeze is the statement that NEITHER runs (crossing-evaluated)")

# ================================================== G. the hyperbolic motif
chk("H3 area law: d ln A/dr -> 2/L -- the coasting mint of 2 nats/e-fold is the hyperbolic capacity exponent [MOTIF, firewalled]",
    abs(2.0/math.tanh(12.0) - 2.0) < 1e-9, f"2 coth(12) - 2 = {2/math.tanh(12.0)-2:.1e}")

print()
if fails:
    print("FAILURES: " + ", ".join(fails)); sys.exit(1)
print("ALL RECEIPTS PASS"); sys.exit(0)
