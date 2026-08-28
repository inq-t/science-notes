#!/usr/bin/env python3
"""Receipts for `the-constants-of-nature.md` [SYNTHESIS -- ALL CONDITIONALS GRANTED].

One script, no imports from other notes: recomputes the assembled chain from
CODATA/SI constants plus the two address readings (SH0ES ladder; Planck
acoustic anchor). Every identity in the note's SS3-SS4 is audited here.
Granted premises G1-G8 are ASSUMED, exactly as the note states; what this
script proves is that, under the grants, the arithmetic closes end to end.
numpy; PASS/FAIL per claim; nonzero exit on failure.
"""
import sys, math
import numpy as np

fails = []
def chk(name, cond, detail=""):
    print(("PASS  " if cond else "FAIL  ") + name + (("  | " + detail) if detail else ""))
    if not cond: fails.append(name)

# ---------------- constants (CODATA/SI) and the two addresses ----------------
c    = 2.99792458e8
hbar = 1.054571817e-34
G    = 6.67430e-11
kB   = 1.380649e-23
Mpc  = 3.0856775814913673e22
kms  = 1000.0/Mpc
MeVkg= 1.602176634e-13/c**2
hbarc_MeVfm = 197.3269804
mP   = math.sqrt(hbar*c/G)
tP   = math.sqrt(hbar*G/c**5)
Hcep = 88.2608*kms          # Cepheid-branch crossing rate [IMPORTED anchor: E(z_c)*73.04]
Hcmb = 82.64*kms            # CMB-branch crossing rate     [E(z_c)*67.84, reference abundances]
zeta, sstar, gamma = 2.0/3.0, 1.0, 2.0   # G2, G3 granted: zeta = gamma*sstar/3

def iota(H):   return math.pi*c**5/(G*hbar*H**2)
def alphaG(H): return G*hbar*H**2/c**5

# ================================================== A. the ledger identities
for tag, H in (("CMB", Hcmb), ("Cepheid", Hcep)):
    chk(f"iota*alpha_G = pi exactly ({tag} branch)",
        abs(iota(H)*alphaG(H)/math.pi - 1) < 1e-14, f"iota = {iota(H):.4e}")
chk("iota = pi/(H t_P)^2 -- the ledger is the clock, squared",
    abs(iota(Hcmb) - math.pi/(Hcmb*tP)**2)/iota(Hcmb) < 1e-14,
    f"H_c t_P = {Hcmb*tP:.3e}")
lncmb, lncep = math.log(iota(Hcmb)), math.log(iota(Hcep))
chk("ln iota = 281.3 nats of clock since the cut (branch spread)",
    abs(lncmb - 281.33) < 0.02 and abs(lncep - 281.19) < 0.02,
    f"ln iota = {lncmb:.2f} (CMB) / {lncep:.2f} (Cepheid)")
chk("the tension is 0.13 nats of ledger: Delta ln iota = 2 ln(H_cep/H_cmb)",
    abs(2*math.log(Hcep/Hcmb) - 0.1316) < 1e-3 and abs((lncmb - lncep) - 2*math.log(Hcep/Hcmb)) < 1e-12,
    f"Delta = {2*math.log(Hcep/Hcmb):.4f} nats")
# horizon thermodynamics: beta E_H = iota; F_H == 0
for tag, H in (("CMB", Hcmb), ("Cepheid", Hcep)):
    T_H = hbar*H/(2*math.pi*kB)
    S_H = math.pi*kB*c**5/(hbar*G*H**2)
    E_H = c**5/(2*G*H)
    chk(f"2Theta_0 = beta E_H = pi/alpha_G = iota ({tag})",
        abs(E_H/(kB*T_H) - iota(H))/iota(H) < 1e-14, f"beta E_H = {E_H/(kB*T_H):.4e}")
    chk(f"F_H = E_H - T_H S_H == 0 -- the books balance exactly ({tag})",
        abs(E_H - T_H*S_H)/E_H < 1e-14, f"E_H = T_H S_H = {E_H:.4e} J")
epsP = c**7/(hbar*G**2)
epsc = 3*Hcmb**2*c**2/(8*math.pi*G)
chk("vacuum 'catastrophe' is an identity: eps_P/eps_crit = (8/3) iota",
    abs(epsP/epsc - (8.0/3.0)*iota(Hcmb))/(epsP/epsc) < 1e-14,
    f"ratio = {epsP/epsc:.4e} = (8/3)*{iota(Hcmb):.4e}")

# ================================================== B. the shape (unit branch)
Om0, Or0 = 0.310598, 9.15e-5
def crossing(Om, Orr):
    OX = 1.0 - Om - Orr
    g = lambda xc: OX*math.cosh(xc)**2 - Om*math.exp(3*xc) - Orr*math.exp(4*xc)
    lo, hi = 1e-6, 2.0
    for _ in range(200):
        mid = 0.5*(lo+hi)
        lo, hi = (mid, hi) if g(mid) > 0 else (lo, mid)
    return 0.5*(lo+hi)
xc = crossing(Om0, Or0)
OX0 = 1 - Om0 - Or0
w0 = -1 + (2.0/3.0)*math.tanh(xc)
wa = -(2.0/3.0)/math.cosh(xc)**2
q0 = 0.5*(Om0 + 2*Or0 + OX0*(1+3*w0))
chk("benchmark reproduced: x_c = 0.2940066, z_c = 0.3417927",
    abs(xc - 0.2940066) < 2e-6 and abs(math.exp(xc)-1-0.3417927) < 3e-6,
    f"x_c = {xc:.7f}")
chk("rigid outputs: w0 = -0.8094545, wa = -(2/3)sech^2 x_c = -0.6122053, q0 = -0.3369025",
    abs(w0+0.8094545) < 1e-6 and abs(wa+0.6122053) < 1e-6 and abs(q0+0.3369025) < 1e-6,
    f"w0 = {w0:.7f}, wa = {wa:.7f}, q0 = {q0:.7f}")
chk("x_c = artanh(3(1+w0)/2) inverts -- one address fixes the family",
    abs(math.atanh(1.5*(1+w0)) - xc) < 1e-12)
xc_nr = crossing(Om0, 0.0)
chk("closed form: Omega_m = 1/(1 + e^{3x_c} sech^2 x_c) -- the matter fraction is an address function",
    abs(1.0/(1.0 + math.exp(3*xc_nr)/math.cosh(xc_nr)**2) - Om0) < 1e-9,
    f"Omega_m({xc_nr:.5f}) = {1.0/(1.0+math.exp(3*xc_nr)/math.cosh(xc_nr)**2):.6f}")
# H^2/H_c^2 = (1/2)(e^{-3u} + sech^2 u) exactly (radiationless, crossing + flatness)
Om_nr = 1.0/(1.0 + math.exp(3*xc_nr)/math.cosh(xc_nr)**2); OX_nr = 1 - Om_nr
u = np.linspace(-3, 3, 20001)
x = xc_nr - u
E2   = Om_nr*np.exp(3*x) + OX_nr*(math.cosh(xc_nr)/np.cosh(u))**2
E2c  = 2*OX_nr*math.cosh(xc_nr)**2
half = 0.5*(np.exp(-3*u) + 1/np.cosh(u)**2)
chk("H^2(u)/H_c^2 = (1/2)(e^{-3u} + sech^2 u) EXACTLY on the family",
    float(np.max(np.abs(E2/E2c - half))) < 1e-10,
    f"max dev {float(np.max(np.abs(E2/E2c-half))):.1e}")
chk("E(z_c)^2 = 2 Omega_X0 cosh^2 x_c -- the native rate in today's units",
    abs(math.sqrt(E2c) - math.sqrt(2*OX_nr)*math.cosh(xc_nr)) < 1e-12,
    f"E(z_c) = {math.sqrt(E2c):.4f}")
# the freeze: conservation integrates the w-profile to the sech^2 pulse (Casimir), zero net heat
ug = np.linspace(-30, 30, 600001)
w_ = -1 + (2.0/3.0)*np.tanh(ug)
lnrho = -np.concatenate([[0.0], np.cumsum(0.5*(3*(1+w_[1:]) + 3*(1+w_[:-1])))*(ug[1]-ug[0])])
lnrho -= lnrho[len(ug)//2]
chk("G1 freeze: d ln rho/dN = -3(1+w) integrates to rho_X = rho_c sech^2 u; rho cosh^2 u is the Casimir",
    float(np.max(np.abs(lnrho + 2*np.log(np.cosh(ug))))) < 1e-6)
heat = float(np.trapezoid(3*(1+w_)/np.cosh(ug)**2, ug))
chk("zero net pulse heat: integral of 3(1+w) rho_X dN = 0 (odd integrand)",
    abs(heat) < 1e-12, f"integral = {heat:.1e}")
chk("two channels, one Casimir: m^2 + m' = 1 on the whole line (m = tanh)",
    float(np.max(np.abs(np.tanh(ug)**2 + 1/np.cosh(ug)**2 - 1))) < 1e-12)
# production profile: 2(1+q) = 4 -> 3 -> 3/2 (crossing, exact radiationless) -> 1.326 (today) -> 2 (coast)
lna = np.linspace(-25, 12, 400001)
S_ = (math.cosh(xc)/np.cosh(xc + lna))**2
lnE = 0.5*np.log(Om0*np.exp(-3*lna) + Or0*np.exp(-4*lna) + OX0*S_)
mint = -2*np.gradient(lnE, lna)
i_r = int(np.argmin(np.abs(lna+15))); i_m = int(np.argmin(np.abs(lna+4)))
i_0 = int(np.argmin(np.abs(lna)));    i_c = int(np.argmin(np.abs(lna-10)))
chk("mint profile 2(1+q): radiation 4 -> matter 3 -> today 1.326 -> coast 2 nats/e-fold",
    abs(mint[i_r]-4) < 1e-2 and abs(mint[i_m]-3) < 0.03 and abs(mint[i_0]-1.3262) < 2e-3 and abs(mint[i_c]-2) < 1e-3,
    f"{mint[i_r]:.3f} -> {mint[i_m]:.3f} -> {mint[i_0]:.4f} -> {mint[i_c]:.4f}")
lna2 = np.linspace(-2, 2, 200001)
S2 = (math.cosh(xc_nr)/np.cosh(xc_nr + lna2))**2
lnE2 = 0.5*np.log(Om_nr*np.exp(-3*lna2) + OX_nr*S2)
mint2 = -2*np.gradient(lnE2, lna2)
mc = float(mint2[int(np.argmin(np.abs(lna2 + xc_nr)))])
chk("the crossing mints 3/2 nats/e-fold EXACTLY (radiationless 2(1+q)|_c)",
    abs(mc - 1.5) < 2e-3, f"2(1+q)|_c = {mc:.4f}")
d_prof = np.exp(mint)
chk("Cuntz-dimension form d(N)=e^{2(1+q)}: 54.6 -> 20.1 -> dip 3.765 -> coast e^2 = 7.389 (transcendental; > Jones 4)",
    abs(d_prof[i_r]-54.6) < 0.4 and abs(d_prof[i_m]-20.1) < 0.6
    and abs(float(np.min(d_prof[(lna > -1) & (lna < 3)])) - 3.765) < 0.02
    and abs(d_prof[i_c]-math.exp(2)) < 0.01 and math.exp(2) > 4,
    f"dip = {float(np.min(d_prof[(lna > -1) & (lna < 3)])):.3f}")
gaps = [abs(2.0 - math.log(d)) for d in range(2, 40)]
chk("no finite quantum symmetry feeds the wall: 2 nats/e-fold is no ln(integer), min gap |2 - ln 7| = 0.054",
    min(gaps) > 0.05 and abs(min(gaps) - (2 - math.log(7))) < 1e-12)

# ================================================== C. the CMB-conditional H0 (distance-matched)
h_ref, om, orad, zstar = 0.6736, 0.1430, 4.177e-5, 1089.92     # [IMPORTED -- verify]
ckm = 299792.458
def DM(h, model):
    Om = om/h**2; Orr = orad/h**2; OX = 1.0 - Om - Orr
    if model == "lcdm":
        S = lambda z: np.ones_like(z)
    else:
        xch = crossing(Om, Orr)
        S = lambda z: (np.cosh(xch)/np.cosh(xch - np.log(1+z)))**2
    ln1pz = np.linspace(0, math.log(1+zstar), 250001)
    z = np.exp(ln1pz) - 1
    E = np.sqrt(Om*(1+z)**3 + Orr*(1+z)**4 + OX*S(z))
    return (ckm/(100*h))*np.trapezoid((1+z)/E, ln1pz)
DM_ref = DM(h_ref, "lcdm")
def solve_h(model):
    lo, hi = 0.55, 0.80
    for _ in range(55):
        mid = 0.5*(lo+hi)
        lo, hi = (mid, hi) if DM(mid, model) > DM_ref else (lo, mid)
    return 0.5*(lo+hi)
chk("pipeline closes: re-solving LCDM against its own D_M(z*) returns h_ref",
    abs(solve_h("lcdm") - h_ref) < 2e-4, f"D_M(z*) = {DM_ref:.1f} Mpc")
h_cst = solve_h("cst")
chk("H0^(CST|CMB) = 67.84 km/s/Mpc -- the acoustic address read through the pulse",
    abs(100*h_cst - 67.84) < 0.05, f"H0 = {100*h_cst:.2f} km/s/Mpc; Omega_m = {om/h_cst**2:.4f}")
shoes, sig = 73.04, 1.04                                        # [IMPORTED -- verify]
chk("the fork is real: pulse does not reach the ladder; gap ~5 sigma(SH0ES)",
    (shoes - 100*h_cst)/sig > 3.0, f"gap = {shoes-100*h_cst:.2f} km/s/Mpc = {(shoes-100*h_cst)/sig:.1f} sigma")
Om_r, Or_r = om/h_ref**2, orad/h_ref**2
xr = crossing(Om_r, Or_r); OX_r = 1 - Om_r - Or_r
Ec = math.sqrt(2*OX_r*math.cosh(xr)**2)
chk("branch anchor composition: H_c(CMB) = E(z_c)*H0^(CST|CMB) = 82.64 km/s/Mpc",
    abs(Ec*100*h_cst - 82.64) < 0.05, f"E(z_c) = {Ec:.4f}; H_c = {Ec*100*h_cst:.2f} km/s/Mpc")
xr2 = crossing(om/h_cst**2, orad/h_cst**2)
Ec2 = math.sqrt(2*(1-om/h_cst**2-orad/h_cst**2)*math.cosh(xr2)**2)
band = sorted([Ec*100*h_cst, Ec2*100*h_cst])
chk("composition ambiguity FLAGGED, carried as a band: H_c(CMB) in [82.0, 83.2] (abundance choice in E)",
    82.0 < band[0] < band[1] < 83.2, f"band = [{band[0]:.2f}, {band[1]:.2f}] km/s/Mpc")

# ================================================== D. the carrier and the closed form for G
def mstar(H): return (hbar**2*H/(4*zeta*c*G))**(1.0/3.0)
m_cmb, m_cep = mstar(Hcmb), mstar(Hcep)
chk("zeta = gamma s*/3 = 2/3 exactly under G2+G3; 1/(4 zeta) = 3/8 is counting, not fitting",
    abs(zeta - 2.0/3.0) < 1e-15 and abs(1/(4*zeta) - 0.375) < 1e-15)
chk("the grain, predicted: m* = 46.18 MeV (CMB) / 47.21 MeV (Cepheid)",
    abs(m_cmb/MeVkg - 46.18) < 0.05 and abs(m_cep/MeVkg - 47.21) < 0.02,
    f"m* = {m_cmb/MeVkg:.2f} / {m_cep/MeVkg:.2f} MeV")
lam_cmb, lam_cep = hbarc_MeVfm/(m_cmb/MeVkg), hbarc_MeVfm/(m_cep/MeVkg)
chk("its Compton cell: lambda* = 4.273 / 4.180 fm",
    abs(lam_cmb - 4.273) < 0.01 and abs(lam_cep - 4.180) < 0.005,
    f"lambda* = {lam_cmb:.3f} / {lam_cep:.3f} fm")
chk("the closed form G = 3 hbar^2 H_c/(8 c m*^3) reproduces G_N (round trip 1e-13)",
    abs(3*hbar**2*Hcmb/(8*c*m_cmb**3) - G)/G < 1e-13 and abs(3*hbar**2*Hcep/(8*c*m_cep**3) - G)/G < 1e-13)
# the three exact presentations of the ledger through the grain
for tag, H, m_ in (("CMB", Hcmb, m_cmb), ("Cepheid", Hcep, m_cep)):
    p1 = (math.pi/(16*zeta**2))*(mP/m_)**6
    p2 = 4*math.pi*zeta*((c/H)/(hbar/(m_*c)))**3
    chk(f"presentations agree ({tag}): iota = (9pi/64)(m_P/m*)^6 = (8pi/3)(R_H/lambda*)^3",
        abs(p1 - iota(H))/iota(H) < 1e-12 and abs(p2 - iota(H))/iota(H) < 1e-12,
        f"m_P/m* = {mP/m_:.3e}")
chk("hierarchy = sixth root of the age: m_P/m* = (16 zeta^2 iota/pi)^{1/6} = 2.64e20 (CMB)",
    abs((16*zeta**2*iota(Hcmb)/math.pi)**(1.0/6.0) - mP/m_cmb)/(mP/m_cmb) < 1e-12
    and abs(mP/m_cmb - 2.64e20)/2.64e20 < 0.005,
    f"m_P/m* = {mP/m_cmb:.3e}")
alg = G*m_cmb**2/(hbar*c)
chk("gravity is weak because the clock is slow: alpha_g(m*) = G m*^2/(hbar c) = hbar H_c/(4 zeta m* c^2) ~ 1.4e-41",
    abs(alg - hbar*Hcmb/(4*zeta*m_cmb*c**2))/alg < 1e-12 and 1.3e-41 < alg < 1.6e-41,
    f"alpha_g = {alg:.3e}")
cands = {"m_mu/2": 52.829, "m_pi/2": 69.785, "sqrt(me mp)": 21.90, "m_s(2GeV)": 93.4, "m_pi0": 134.977, "m_e": 0.511, "m_u+m_d": 6.9}
dmin = min(abs(v - m_cep/MeVkg)/(m_cep/MeVkg) for v in cands.values())
chk("the blank is clean: nearest standard scale is 11.9% away (m_mu/2) -- the theory owes the world one new grain",
    dmin > 0.10, f"min distance {100*dmin:.1f}%")
lo_s, hi_s = 0.9175, 1.0621     # empirical CI on s* if G2 is de-granted
mband = sorted([m_cmb/MeVkg*(1.0/s)**(1.0/3.0) for s in (lo_s, hi_s)])
chk("de-granting G2 degrades gracefully: s* CI maps to m*(CMB) in [45.3, 47.5] MeV (m* ~ s*^{-1/3})",
    45.2 < mband[0] < mband[1] < 47.6, f"band = [{mband[0]:.2f}, {mband[1]:.2f}] MeV")

# ================================================== E. positivity, the unit nat, the spine
kk = np.array([0.5, 1.0, 2.0, 4.0, 8.0])
uu = np.linspace(0, 60, 400001)
sech2 = 1/np.cosh(uu)**2
ft = np.array([2*np.trapezoid(sech2*np.cos(k*uu), uu) for k in kk])
closed = math.pi*kk/np.sinh(math.pi*kk/2)
chk("G6 Born positivity certificate: FT[sech^2](k) = pi k/sinh(pi k/2) > 0 (Bochner)",
    float(np.max(np.abs(ft - closed))) < 1e-8 and np.all(closed > 0),
    f"max dev {float(np.max(np.abs(ft-closed))):.1e}")
xg = np.linspace(0, 60, 400001)
p = np.exp(-xg)
Sexp = float(np.trapezoid(np.where(p > 0, -p*np.log(p), 0.0), xg))
chk("G2 unit nat: S[Exp(1)] = 1 exactly -- the register's KMS state carries one nat",
    abs(Sexp - 1.0) < 1e-6, f"S = {Sexp:.7f}")
mN = 1.0/(3*math.sqrt(3.0))
r = np.sort(np.roots([1.0, 0.0, -1.0, 2*mN]).real)
chk("G7 spine: Nariai is the A2 fold -- SdS cubic acquires the double root r = 1/sqrt(3) at m_N = L/(3 sqrt(3))",
    abs(r[1]-r[2]) < 1e-7 and abs(r[1]-1/math.sqrt(3)) < 1e-7 and abs(r[0]+2/math.sqrt(3)) < 1e-7)
ok = True
for m_ in np.linspace(0.01, 0.99, 40)*mN:
    rr = np.sort(np.roots([1.0, 0.0, -1.0, 2*m_]).real)
    ok = ok and rr[0] < 0 and rr[1] > 0 and rr[2] > 0 and abs(rr.sum()) < 1e-10
chk("G3 face (ii): exactly TWO slots write area at every admissible mass; the balancer r3 = -(r_c+r_h) never does",
    ok, "gamma counts area-writing channels per trace-zero cell")

print()
if fails:
    print("FAILURES: " + ", ".join(fails)); sys.exit(1)
print("ALL RECEIPTS PASS"); sys.exit(0)
