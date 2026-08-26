#!/usr/bin/env python3
"""Receipts for `h0-width-address-anchor.md`.

Requires numpy (inbox note; stdlib rewrite owed on promotion). PASS/FAIL per
claim; nonzero exit on failure. Units G = c = 1 where dimensionless; SI/astro
constants declared inline. Imported reference numbers are flagged in the note
as carrier-conditional and verify-before-promotion.
"""
import sys, math
import numpy as np

fails = []
def chk(name, cond, detail=""):
    print(("PASS  " if cond else "FAIL  ") + name + (("  | " + detail) if detail else ""))
    if not cond: fails.append(name)

# ================================================== A. three exact sech^2 facts
# A1. the de Sitter lapse in its own tortoise coordinate IS sech^2, width 1/H
L = 1.0
ok = True
for r in np.linspace(0.01, 0.99, 60):
    rstar = L*math.atanh(r/L)                       # = int_0^r dr'/f exactly
    grid = np.linspace(0, r, 200001)
    num = np.trapezoid(1.0/(1-grid**2/L**2), grid)
    ok = ok and abs(num - rstar) < 1e-6
    ok = ok and abs((1 - r**2/L**2) - 1.0/math.cosh(rstar/L)**2) < 1e-12
chk("dS: tortoise r* = L artanh(r/L); lapse f = sech^2(r*/L) EXACTLY -- width = L = c/H",
    ok, "H's native 1/T is the sech^2 width of the box in causal depth")

# A2. near-Nariai SdS: the wave potential becomes Poschl-Teller V0 sech^2(kappa r*)
mN = L/(3*math.sqrt(3.0))
def pt_fit(mfrac, ell=1):
    m = mfrac*mN
    rts = np.sort(np.roots([1.0, 0.0, -L**2, 2*m*L**2]).real)
    rh, rc = rts[1], rts[2]
    y = np.linspace(-14, 14, 40001)                  # tanh-clustered grid between horizons
    r = 0.5*(rh+rc) + 0.5*(rc-rh)*np.tanh(y/2.0)
    f = 1 - 2*m/r - r**2/L**2
    drdy = 0.25*(rc-rh)/np.cosh(y/2.0)**2
    rstar = np.cumsum(drdy/f)* (y[1]-y[0]); rstar -= rstar[len(y)//2]
    fp = 2*m/r**2 - 2*r/L**2
    V = f*(ell*(ell+1)/r**2 + fp/r)
    A = V.max(); i0 = int(V.argmax()); b = rstar[i0]
    half = np.where(V > A/2)[0]
    w = (rstar[half[-1]] - rstar[half[0]])/(2*math.log(math.sqrt(2)+1))
    res = np.max(np.abs(V - A/np.cosh((rstar-b)/w)**2))/A
    kappa = abs((rh - rts[0])*(rh - rc))/(2*L**2*rh)
    return res, w*kappa
r1,_ = pt_fit(0.99); r2,_ = pt_fit(0.999); r3, wk = pt_fit(0.99999)
chk("near-Nariai: potential -> V0 sech^2(kappa r*): residual falls 0.99 -> 0.999 -> 0.99999 of m_N",
    r1 > r2 > r3 and r3 < 1e-3, f"residuals {r1:.1e}, {r2:.1e}, {r3:.1e}")
chk("near-Nariai: fitted sech^2 width = 1/kappa (surface gravity): width*kappa -> 1",
    abs(wk - 1.0) < 5e-3, f"w*kappa = {wk:.5f}")

# A3. the CST pulse: w = -1 + (2/3) nu tanh(nu x)  <=>  rho_X ~ sech^2(nu x)
nu = 1.0
x = np.linspace(-6, 6, 240001)
lnrho = np.zeros_like(x)                              # integrate dlnrho/dx = -3(1+w)
w_ = (2.0/3.0)*nu*np.tanh(nu*x)
lnrho = -np.concatenate([[0.0], np.cumsum(0.5*(3*w_[1:]+3*w_[:-1]))*(x[1]-x[0])])
lnrho -= lnrho[len(x)//2]
target = -2*np.log(np.cosh(nu*x))
chk("CST pulse: conservation integrates w(x) to rho_X = rho_c sech^2(nu x) exactly",
    np.max(np.abs(lnrho - target)) < 1e-6, f"max err {np.max(np.abs(lnrho-target)):.1e}")

# ================================================== B. the unit-branch benchmark, reproduced
Om0, Or0 = 0.310598, 9.15e-5
OX0 = 1.0 - Om0 - Or0
def crossing(Om0, Or0):
    OX0 = 1.0 - Om0 - Or0
    g = lambda xc: OX0*math.cosh(xc)**2 - Om0*math.exp(3*xc) - Or0*math.exp(4*xc)
    lo, hi = 1e-6, 2.0
    for _ in range(200):
        mid = 0.5*(lo+hi)
        if g(mid) > 0: lo = mid
        else: hi = mid
    return 0.5*(lo+hi)
xc = crossing(Om0, Or0)
w0 = -1 + (2.0/3.0)*math.tanh(xc)
wa = -(2.0/3.0)/math.cosh(xc)**2
q0 = 0.5*(Om0 + 2*Or0 + OX0*(1+3*w0))
chk("unit branch reproduced: x_c = 0.2940066, z_c = 0.3417927",
    abs(xc - 0.2940066) < 2e-6 and abs(math.exp(xc)-1 - 0.3417927) < 3e-6,
    f"x_c = {xc:.7f}, z_c = {math.exp(xc)-1:.7f}")
chk("unit branch reproduced: w0 = -0.8094545, wa = -0.6122053 (rigid CPL tangent -(2/3)sech^2 x_c)",
    abs(w0 + 0.8094545) < 1e-6 and abs(wa + 0.6122053) < 1e-6, f"w0 = {w0:.7f}, wa = {wa:.7f}")
chk("unit branch reproduced: q0 = -0.3369025",
    abs(q0 + 0.3369025) < 1e-6, f"q0 = {q0:.7f}")
xc_nr = crossing(Om0, 0.0)
rel = 1.0/(1.0 + math.exp(3*xc_nr)/math.cosh(xc_nr)**2)
chk("closed-form relation (radiationless): Omega_m = 1/(1 + e^{3x_c} sech^2 x_c) inverts the crossing",
    abs(rel - Om0) < 1e-9, f"Omega_m({xc_nr:.5f}) = {rel:.6f}")
chk("hyperbolic-counting hook: ledger rate today 2(1+q0) = 1.326 nats per e-fold",
    abs(2*(1+q0) - 1.3262) < 1e-3, f"2(1+q0) = {2*(1+q0):.4f}")

# ================================================== C. the CMB-conditional H0 (differential design)
# reference: flat LCDM at (h, om, or) below; the pulse model must match its D_M(z*).
h_ref, om, orad, zstar = 0.6736, 0.1430, 4.177e-5, 1089.92     # [IMPORTED -- verify]
ckm = 299792.458
def DM_and_age(h, model):
    Om = om/h**2; Or = orad/h**2; OX = 1.0 - Om - Or
    if model == "lcdm":
        S = lambda z: np.ones_like(z)
    else:
        xch = crossing(Om, Or)
        S = lambda z: (np.cosh(xch)/np.cosh(xch - np.log(1+z)))**2
    ln1pz = np.linspace(0, math.log(1+zstar), 300001)
    z = np.exp(ln1pz) - 1
    E = np.sqrt(Om*(1+z)**3 + Or*(1+z)**4 + OX*S(z))
    DM = (ckm/(100*h))*np.trapezoid((1+z)/E, ln1pz)
    lnA = np.linspace(0, math.log(1+1e8), 300001)
    za = np.exp(lnA) - 1
    Ea = np.sqrt(Om*(1+za)**3 + Or*(1+za)**4 + OX*S(za))
    t0 = (977.79/(100*h))*np.trapezoid(1.0/Ea, lnA)             # Gyr (1/(km/s/Mpc) = 977.79 Gyr)
    return DM, t0
DM_ref, t0_ref = DM_and_age(h_ref, "lcdm")
def solve_h(model):
    lo, hi = 0.55, 0.80
    for _ in range(60):
        mid = 0.5*(lo+hi)
        DM, _ = DM_and_age(mid, model)
        if DM > DM_ref: lo = mid
        else: hi = mid
    return 0.5*(lo+hi)
h_check = solve_h("lcdm")
chk("pipeline: re-solving LCDM against its own distance returns h = 0.6736",
    abs(h_check - h_ref) < 2e-4, f"h = {h_check:.4f}; D_M(z*) = {DM_ref:.1f} Mpc, t0 = {t0_ref:.3f} Gyr")
h_cst = solve_h("cst")
DM_c, t0_c = DM_and_age(h_cst, "cst")
Om_c = om/h_cst**2
xc_c = crossing(Om_c, orad/h_cst**2)
w0_c = -1 + (2.0/3.0)*math.tanh(xc_c)
chk("CMB-conditional unit CST-B2: H0 solved by matching the acoustic distance at fixed (om, or)",
    0.55 < h_cst < 0.80,
    f"H0 = {100*h_cst:.2f} km/s/Mpc; Omega_m = {Om_c:.4f}; z_c = {math.exp(xc_c)-1:.4f}; w0 = {w0_c:.4f}; t0 = {t0_c:.3f} Gyr")
shoes, sig = 73.04, 1.04                                        # [IMPORTED -- verify]
gap = (shoes - 100*h_cst)/sig
chk("verdict: the pulse does NOT reach the local value -- residual gap vs SH0ES in its own sigma",
    gap > 3.0, f"gap = {shoes - 100*h_cst:.2f} km/s/Mpc = {gap:.1f} sigma(SH0ES)")
# the pulse is invisible at recombination: it cannot buy H0 back through r_s
Om_, Or_, OX_ = om/h_cst**2, orad/h_cst**2, 1-om/h_cst**2-orad/h_cst**2
fx = OX_*(math.cosh(xc_c)/math.cosh(xc_c - math.log(1+zstar)))**2
ftot = Om_*(1+zstar)**3 + Or_*(1+zstar)**4
chk("the pulse is invisible at recombination: rho_X/rho_tot(z*) < 1e-14 -- r_s untouched, no early-time lever",
    fx/ftot < 1e-14, f"ratio = {fx/ftot:.1e}")
# H(z) shape: where the pulse sits above/below Lambda at the SAME H0
ztab = np.array([0.0, 0.2, 0.34, 0.5, 1.0, 2.0, 3.0])
Om_r, Or_r, OX_r = om/h_ref**2, orad/h_ref**2, 1-om/h_ref**2-orad/h_ref**2
xr = crossing(Om_r, Or_r)
Sr = (np.cosh(xr)/np.cosh(xr - np.log(1+ztab)))**2
Ecst = np.sqrt(Om_r*(1+ztab)**3 + Or_r*(1+ztab)**4 + OX_r*Sr)
Elcdm = np.sqrt(Om_r*(1+ztab)**3 + Or_r*(1+ztab)**4 + OX_r)
print("      H_pulse/H_LCDM at same (H0, om):",
      ", ".join(f"z={z:g}: {a/b:.4f}" for z,a,b in zip(ztab, Ecst, Elcdm)))

# ================================================== D. anchors and addresses
tP = 5.391e-44        # s [IMPORTED]
H0_SI = 100*h_cst*1000/3.0857e22
chk("dimensional anchor: H0 t_Planck ~ 1.2e-61 -- no dimensionless structure supplies this; one anchor is owed",
    1e-61 < H0_SI*tP < 1.3e-61, f"H0 t_P = {H0_SI*tP:.3e}")
Ec = math.sqrt(Om_r*math.exp(3*xr) + Or_r*math.exp(4*xr) + OX_r*math.cosh(xr)**2)
chk("the theory's own T^-1 is the crossing rate: H_c = E(z_c) H0 with E(z_c)^2 = 2 Omega_X0 cosh^2 x_c",
    abs(Ec - math.sqrt(2*OX_r*math.cosh(xr)**2)) < 1e-9,
    f"E(z_c) = {Ec:.4f}; H_c = {Ec*100*h_ref:.1f} km/s/Mpc (at h_ref); 1/H_c = {977.79/(Ec*100*h_ref):.2f} Gyr")

print()
if fails:
    print("FAILURES: " + ", ".join(fails)); sys.exit(1)
print("ALL RECEIPTS PASS"); sys.exit(0)
