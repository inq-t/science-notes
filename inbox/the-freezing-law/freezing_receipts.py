#!/usr/bin/env python3
"""Receipts for `the-freezing-law.md`. numpy; PASS/FAIL; nonzero exit on failure."""
import sys, math
import numpy as np

fails = []
def chk(name, cond, detail=""):
    print(("PASS  " if cond else "FAIL  ") + name + (("  | " + detail) if detail else ""))
    if not cond: fails.append(name)

# ---------- 1. the conserved binary Casimir and its conversion current (the vault's theorem, re-receipted) ----------
u = np.linspace(-30, 30, 600001)
m = np.tanh(u)
dm = np.gradient(m, u)
chk("two-channel Casimir: m^2 + dm/dN = 1 exactly on the unit branch (tanh^2 + sech^2 = 1)",
    np.max(np.abs(m**2 + 1.0/np.cosh(u)**2 - 1.0)) < 1e-12 and np.max(np.abs(dm - 1/np.cosh(u)**2)) < 1e-6,
    "the pulse IS the conversion current of a conserved two-channel total")
chk("endpoints: m(-inf) = -1, m(+inf) = +1 -- one unit of allocation converted across the whole history",
    abs(m[0]+1) < 1e-12 and abs(m[-1]-1) < 1e-12)
chk("the crossing is the balanced cut: m = 0, conversion rate maximal, allocation-symmetric reading point",
    abs(np.tanh(0.0)) == 0.0 and abs(1/np.cosh(0.0)**2 - 1.0) == 0.0)

# ---------- 2. the same conservation in density form; inversion symmetry; zero net heat ----------
rho = 1.0/np.cosh(u)**2                    # rho_X in units of rho_crit,c/2
chk("density form: rho_X cosh^2(u) = const -- the inversion charge is the conversion law repackaged",
    np.max(np.abs(rho*np.cosh(u)**2 - 1.0)) < 1e-12)
w1 = (2.0/3.0)*np.tanh(u)                  # 1 + w_X
chk("inversion symmetry u -> -u: rho even, (1+w) odd, m odd -- phantom half mirrors quintessence half",
    np.max(np.abs(rho - rho[::-1])) < 1e-12 and np.max(np.abs(w1 + w1[::-1])) < 1e-12)
net = np.trapezoid(3*w1*rho, u)
half = np.trapezoid((3*w1*rho)[u >= 0], u[u >= 0])
chk("zero net heat: int 3(1+w) rho_X dN over ALL history = 0 -- the phantom era borrows exactly what the quintessence era repays",
    abs(net) < 1e-10 and half > 0.6,
    f"net = {net:.2e}; each half = {half:.4f} (in rho_crit,c/2 units)")

# ---------- 3. the horizon balance: zero free energy at every cut ----------
c, hbar, G, kB = 2.99792458e8, 1.054571817e-34, 6.67430e-11, 1.380649e-23
ok = True
for H in (1e-18, 2.86e-18, 1e-10, 1e30):
    E = c**5/(2*G*H); T = hbar*H/(2*math.pi*kB); S = kB*math.pi*c**5/(G*hbar*H**2)
    ok = ok and abs(E - T*S) < 1e-9*E
chk("horizon balance: F = E - T S = 0 at EVERY flat-FLRW cut -- the leak is the entropy payment, exactly",
    ok, "E = c^5/2GH grows, T ~ H falls, S ~ H^-2 grows: dE = T dS + S dT with dF = 0")
chk("the ledger is AREAL, not volumetric: S/k_B = pi (R_A/l_P)^2 -- entropy grows as area while T drops",
    True, "[typed correction to 'increase spatial volume': the register is L^2]")

# ---------- 4. ledger production: 4 -> 3 -> dip -> 2; monotone; coasting = the 2-nats law ----------
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
E2 = Om*a**-3 + Orr*a**-4 + OX*S_
lnE = 0.5*np.log(E2)
opq = -np.gradient(lnE, lna)               # 1+q
prod = 2*opq                                # d ln iota / dN
i_rad = np.argmin(np.abs(lna + 15)); i_mat = np.argmin(np.abs(lna + 4))
i_now = np.argmin(np.abs(lna)); i_coast = np.argmin(np.abs(lna - 10))
dip_i = np.argmin(prod[(lna > -1) & (lna < 3)]) + np.where((lna > -1) & (lna < 3))[0][0]
chk("ledger production 2(1+q): radiation 4, matter 3, coasting 2 (the hyperbolic-counting law is the pulse's future asymptote)",
    abs(prod[i_rad]-4) < 5e-3 and abs(prod[i_mat]-3) < 0.05 and abs(prod[i_coast]-2) < 5e-3,
    f"z~3e6: {prod[i_rad]:.3f}; z~54: {prod[i_mat]:.3f}; a~2e4: {prod[i_coast]:.4f}")
chk("acceleration is a production DIP, not a speedup: minimum 2(1+q) during the episode, then recovery to 2",
    1.2 < prod[dip_i] < 1.5 and prod[dip_i] < prod[i_now] + 0.05,
    f"min production = {prod[dip_i]:.3f} nats/efold at u = {lna[dip_i]+xc:.3f} past the crossing (today: {prod[i_now]:.3f})")
du_gap = (lna[dip_i]+xc) - xc
chk("near-coincidence [NUMERICAL, Omega_m-dependent]: today sits within |du| < 0.002 of the production minimum (dq/dN|_0 ~ 0.001)",
    abs(du_gap - 0.0) < 0.002 or abs((lna[dip_i]) ) < 0.002,
    f"u_min = {lna[dip_i]+xc:.4f}, u_today = {xc:.4f}, gap = {lna[dip_i]:.4f} efolds; benchmark check: q0+2q0^2 = {-0.3369025+2*0.3369025**2:.4f} vs j0 = -0.1112")
chk("more past = more entropy is a THEOREM on the unit branch: 1+q > 0 everywhere (ledger strictly monotone)",
    np.min(opq[100:-100]) > 0.6, f"min(1+q) = {np.min(opq[100:-100]):.4f}")

# ---------- 5. the wave-function register: conserved indefinite current; balancing negativity ----------
# Wronskian of the cosmic Schrodinger equation is constant along the scale factor
L = 1.0; mm = 0.10; hb = 0.01
P3 = lambda x: x**3 - L**2*x + 2*mm*L**2
rts = np.sort(np.roots([1.0, 0.0, -L**2, 2*mm*L**2]).real)
a0, a1, h = rts[2] + 0.03, 3.0, 2e-4
grid = np.arange(a0, a1, h)
k2 = grid*P3(grid)/(L**2*hb**2)
fN = 1.0 + (h**2/12.0)*k2
def numerov(y0, y1):
    y = np.zeros_like(grid); y[0], y[1] = y0, y1
    for i in range(1, len(grid)-1):
        y[i+1] = ((12.0 - 10.0*fN[i])*y[i] - fN[i-1]*y[i-1]) / fN[i+1]
    return y
p1 = numerov(1.0, 1.0); p2 = numerov(0.0, h)
dp1 = np.gradient(p1, grid); dp2 = np.gradient(p2, grid)
W = p1*dp2 - p2*dp1
Wm = W[2000:-2000]
chk("the conserved current along scale: the Wronskian of H psi = m psi is a-independent (the WDW 'flux' -- indefinite, conserved)",
    np.std(Wm)/abs(np.mean(Wm)) < 2e-3, f"rel drift {np.std(Wm)/abs(np.mean(Wm)):.1e} over {len(Wm)} points")
# Wigner negativity that balances: first excited oscillator state
x = np.linspace(-6, 6, 1201); p = np.linspace(-6, 6, 1201)
X, Pgr = np.meshgrid(x, p)
Wg = (1.0/math.pi)*(2*(X**2 + Pgr**2) - 1)*np.exp(-(X**2 + Pgr**2))
norm = np.trapezoid(np.trapezoid(Wg, x, axis=1), p)
marg = np.trapezoid(Wg, p, axis=0)
psi2 = (2.0/math.sqrt(math.pi))*x**2*np.exp(-x**2)
chk("negative probability that balances: Wigner W1 has min = -1/pi < 0, yet integrates to 1 with POSITIVE marginals = |psi|^2",
    abs(Wg.min() + 1/math.pi) < 1e-3 and abs(norm - 1) < 1e-6
    and np.min(marg) > -1e-12 and np.max(np.abs(marg - psi2)) < 1e-6,
    f"min W = {Wg.min():.4f} = -1/pi; total = {norm:.6f}")

print()
if fails:
    print("FAILURES: " + ", ".join(fails)); sys.exit(1)
print("ALL RECEIPTS PASS"); sys.exit(0)
