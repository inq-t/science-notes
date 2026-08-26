#!/usr/bin/env python3
"""Receipts for `the-movable-origin-and-the-one-channel-cut.md`.

Requires numpy (inbox note; stdlib rewrite owed on promotion). PASS/FAIL per
claim; nonzero exit on failure. Constants and branch values marked IMPORTED
are flagged for verification in the note.
"""
import sys, math
import numpy as np

fails = []
def chk(name, cond, detail=""):
    print(("PASS  " if cond else "FAIL  ") + name + (("  | " + detail) if detail else ""))
    if not cond: fails.append(name)

# constants [IMPORTED -- CODATA/SI]
c    = 2.99792458e8
hbar = 1.054571817e-34
GN   = 6.67430e-11
kmsMpc = 1000/3.0856775814913673e22
tP   = math.sqrt(hbar*GN/c**5)

# ---------------- 1. the identity chain and its circularity ----------------
def iota_A(H):  return math.pi/(H*tP)**2          # = S_A/k_B for A = 4 pi (c/H)^2
def alpha_G(H): return GN*hbar*H**2/c**5
H_c_planck  = 82.64*kmsMpc     # this vault's CMB-conditional branch (previous note)
H_c_cepheid = 88.26*kmsMpc     # ChatGPT-side Cepheid-calibrated fit [IMPORTED]
i_p, i_c = iota_A(H_c_planck), iota_A(H_c_cepheid)
chk("crossing ledgers: iota_A,c = pi/(H_c t_P)^2 for the two calibration branches",
    1.49e122 < i_p < 1.53e122 and 1.30e122 < i_c < 1.34e122,
    f"Planck-conditional {i_p:.4g}; Cepheid {i_c:.4g}")
chk("the invariant: iota_A(H) * alpha_G(H) = pi at EVERY cut (the ledger is the reciprocal coupling)",
    all(abs(iota_A(H)*alpha_G(H) - math.pi) < 1e-12 for H in (H_c_planck, H_c_cepheid, 1e-30, 1e30)))
G_back = math.pi*c**5/(hbar*i_c*H_c_cepheid**2)
chk("circularity display: G -> iota -> G returns G_N exactly (a reversed identity, not a derivation)",
    abs(G_back - GN)/GN < 1e-12, f"G back = {G_back:.6e}")
chk("the Hubble tension restated: the two branches differ by 0.13 nats of crossing ledger",
    abs(math.log(i_p/i_c) - 0.131) < 0.01, f"ln ratio = {math.log(i_p/i_c):.4f} nats")

# ---------------- 2. the movable origin (toy demo of the trace-scaling module) ----------------
# the core wall returns tau(e_N) = e^N; a trace rescaling tau -> lam*tau shifts ln iota by ln lam
N1, N2 = 3.7, 9.1
for lam in (1.0, 2.5, 1e6):
    d = (math.log(lam*math.exp(N2)) - math.log(lam*math.exp(N1)))
    assert abs(d - (N2-N1)) < 1e-12
chk("movable origin: trace rescaling shifts every ln iota by ln(lambda); DIFFERENCES are invariant, the absolute count is not",
    True, "the vault's own typed-cosmic-ledger line: relative capacity tau(e_N)=e^N, movable origin")

# ---------------- 3. the exact bookkeeping bridge ----------------
# d ln iota_A / dN = 2(1+q)  <=>  iota_A ~ H^-2  <=>  dlnH/dN = -(1+q): receipt on the composed background
h0 = 0.6784                                     # CMB-conditional unit CST-B2 (previous note)
om_m, om_r = 0.1430, 4.177e-5                   # [IMPORTED carrier]
Om, Or = om_m/h0**2, om_r/h0**2
OX = 1 - Om - Or
def crossing(Om, Or):
    OX = 1 - Om - Or
    g = lambda xc: OX*math.cosh(xc)**2 - Om*math.exp(3*xc) - Or*math.exp(4*xc)
    lo, hi = 1e-6, 2.0
    for _ in range(200):
        mid = 0.5*(lo+hi)
        lo, hi = (mid, hi) if g(mid) > 0 else (lo, mid)
    return 0.5*(lo+hi)
xc = crossing(Om, Or)
def E2_of_lna(lna):   # lna = ln a (a=1 today); pulse sech^2 in efolds about the crossing
    a = np.exp(lna)
    S = (np.cosh(xc)/np.cosh(xc + lna))**2      # x(a) = xc + ln a
    return Om*a**-3 + Or*a**-4 + OX*S
lna = np.linspace(-80, 0, 400001)
lnE = 0.5*np.log(E2_of_lna(lna))
q = -1 - np.gradient(lnE, lna)
resid = np.max(np.abs(np.gradient(np.log(1.0/np.exp(2*lnE)), lna) - 2*(1+q)))
chk("exact bookkeeping: d ln(iota_A)/dN = 2(1+q) is IDENTICALLY iota_A ~ H^-2 (numeric residual on the full history)",
    resid < 1e-6, f"max residual {resid:.1e}")

# ---------------- 4. the one-channel cut and the era breakdown of 10^122 ----------------
H0 = 100*h0*kmsMpc
H1ch = math.sqrt(math.pi)/tP                    # iota_A = 1  <=>  alpha_G = pi
E1 = H1ch/H0
lna1 = float(np.interp(-math.log(E1), -lnE, lna))          # solve lnE = ln E1
a_eq = Or/Om
Heq = H0*math.sqrt(E2_of_lna(math.log(a_eq)))
lnac = -xc                                       # a_c = e^{-x_c}
Hc = H0*math.sqrt(E2_of_lna(lnac))
ln_iota_c = 2*math.log(H1ch/Hc)                  # iota_birth = 1
chk("one-channel cut: with iota_birth = 1 the crossing ledger is EXACTLY exp(2 ln(H_1ch/H_c))",
    abs(ln_iota_c - math.log(iota_A(Hc))) < 1e-9,
    f"ln iota_A,c = {ln_iota_c:.4f} nats; iota_A,c = {math.exp(ln_iota_c):.4g}")
nats_rad = 2*math.log(H1ch/Heq)
nats_mat = 2*math.log(Heq/Hc)
efolds_rad = math.log(a_eq) - lna1
efolds_mat = lnac - math.log(a_eq)
chk("era breakdown: radiation + (matter+pulse) nats sum to the whole ledger",
    abs(nats_rad + nats_mat - ln_iota_c) < 1e-9,
    f"radiation {nats_rad:.1f} nats over {efolds_rad:.1f} efolds ({nats_rad/efolds_rad:.2f}/efold); "
    f"matter+pulse {nats_mat:.1f} nats over {efolds_mat:.1f} efolds ({nats_mat/efolds_mat:.2f}/efold)")
chk("the 10^122 is a clock reading: ~4 nats/efold (radiation) then ~3 (matter) since the one-channel cut",
    3.9 < nats_rad/efolds_rad < 4.05 and 2.7 < nats_mat/efolds_mat < 3.1,
    f"total e-folds since the first cut: {lnac - lna1:.2f}")
chk("equivalent birth statement: alpha_G(H_birth) = pi -- gravity is order-pi at the one-channel cut",
    abs(alpha_G(H1ch) - math.pi) < 1e-12)

# ---------------- 5. cross-checks of the pasted packet ----------------
Omb, Orb = 0.310598, 9.15e-5                     # unit-branch benchmark abundances
OXb = 1 - Omb - Orb
xcb = crossing(Omb, Orb)
lnab = np.linspace(-30, 0, 400001)
ab = np.exp(lnab)
Sb = (np.cosh(xcb)/np.cosh(xcb + lnab))**2
Eb = np.sqrt(Omb*ab**-3 + Orb*ab**-4 + OXb*Sb)
H0t0 = float(np.trapezoid(1.0/Eb, lnab))
chk("packet cross-check: H0 t0 = 0.9518469556 on the unit-branch benchmark",
    abs(H0t0 - 0.9518469556) < 5e-6, f"H0 t0 = {H0t0:.7f}")
Ec = math.sqrt(2*OXb*math.cosh(xcb)**2)
chk("packet cross-check: H_c/H0 = E(z_c) = sqrt(2 Omega_X0) cosh(x_c); benchmark abundances give 1.2253",
    abs(Ec - 1.22526) < 1e-4,
    f"E(z_c) = {Ec:.5f}; Omega_m-sensitive family: 1.207 (Cepheid-fit Om~0.33) to 1.225 (benchmark Om=0.3106)")

print()
if fails:
    print("FAILURES: " + ", ".join(fails)); sys.exit(1)
print("ALL RECEIPTS PASS"); sys.exit(0)
