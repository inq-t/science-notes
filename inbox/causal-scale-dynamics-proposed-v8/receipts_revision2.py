"""
receipts_revision2.py — verifies every numerical claim that is NEW or
CORRECTED in Revision 2 of 'Scale as a Modular Observable'.
(All Revision-1 numbers are unchanged and remain covered by
receipts_closure.py, receipts_transparency_fold.py, and the P1/ package.)

Checks:
  R2-1  Benchmark closure (Appendix A.8): N_c, z_c, rho*/rc0, Om_X0, w0, wa, q0
  R2-2  Jerk correction (Appendix A.9): j0 = q+2q^2-q' by two independent routes;
        the Revision-1 sign error reproduces the superseded value
  R2-3  dq/dN corollary: +0.0013505; q-minimum at z = 0.0008
  R2-4  q0 pinning: spread < 0.004 over Om in [0.28, 0.33]; LCDM sweep for contrast
  R2-5  Acceleration chronology: entry z, exit a/a0, duration; exit-state checks
  R2-6  Density-history table (section 27.1), all ten rows
  R2-7  CPL locus (A.10) and DESI-implied crossings 0.354 / 0.405 / 0.440
  R2-8  Invariant 9(1+w)^2+6w' = 4 along the benchmark history
  R2-9  Existence ceiling value 1.8141 at benchmark Om (section 14 table row)
Requires numpy, scipy only.
"""
import numpy as np
from scipy.optimize import brentq, minimize_scalar

TOL = 2e-6
fails = []


def check(name, got, want, tol=TOL):
    ok = abs(got - want) <= tol
    print(f"{'PASS' if ok else 'FAIL'}  {name}: got {got:.7f}, want {want:.7f}")
    if not ok:
        fails.append(name)


Om, Or = 0.310598, 9.15e-5

# ---------- R2-1 benchmark closure ----------
f = lambda x: (Om*np.exp(3*x) + Or*np.exp(4*x))/np.cosh(x)**2 - (1 - Om - Or)
x = brentq(f, 0.01, 1.0)
Nc = -x
rhostar = Om*np.exp(3*x) + Or*np.exp(4*x)
OX0 = rhostar/np.cosh(x)**2
w0 = -1 + (2/3)*np.tanh(x)
wa = -(2/3)/np.cosh(x)**2
q0 = 0.5*(Om + 2*Or + OX0*(1 + 3*w0))
check("A.8 N_c", Nc, -0.2940066)
check("A.8 z_c", np.exp(x) - 1, 0.3417927)
check("A.8 rho*/rc0", rhostar, 0.7506311)
check("A.8 Om_X0", OX0, 0.6893105)
check("A.8 flatness", Om + Or + OX0, 1.0)
check("A.8 w0", w0, -0.8094545)
check("A.8 wa", wa, -0.6122053)
check("A.8 q0", q0, -0.3369025)

# ---------- shared machinery ----------
def q_of(N, Om=Om, Or=Or, Nc=Nc, rhostar=rhostar):
    th = N - Nc
    rX = rhostar/np.cosh(th)**2
    w = -1 + (2/3)*np.tanh(th)
    rm, rr = Om*np.exp(-3*N), Or*np.exp(-4*N)
    return 0.5*(rm + 2*rr + rX*(1 + 3*w))/(rm + rr + rX)

# ---------- R2-2 jerk ----------
h = 1e-5
dqdN0 = (q_of(h) - q_of(-h))/(2*h)
j0_route1 = q0 + 2*q0**2 - dqdN0                        # identity route
dw0 = (2/3)/np.cosh(x)**2
j0_route2 = 1 + 4.5*(OX0*w0*(1 + w0) + Or*(1/3)*(4/3)) - 1.5*OX0*dw0  # component route
check("A.9 j0 (identity route)", j0_route1, -0.1112465, tol=5e-6)
check("A.9 j0 (component route)", j0_route2, -0.1112465, tol=5e-6)
check("A.9 superseded Rev-1 value from sign error", q0 + 2*q0**2 + dqdN0, -0.1085454, tol=5e-6)

# ---------- R2-3 corollary ----------
check("sec.26 dq/dN|0", dqdN0, 0.0013505, tol=5e-6)
r = minimize_scalar(q_of, bounds=(-0.5, 0.5), method='bounded')
check("sec.26 q-min redshift", np.exp(-r.x) - 1, 0.0008, tol=2e-4)

# ---------- R2-4 q0 pinning ----------
def q0_of_Om(OM):
    ff = lambda xx: (OM*np.exp(3*xx) + Or*np.exp(4*xx))/np.cosh(xx)**2 - (1 - OM - Or)
    xx = brentq(ff, 0.005, 1.5)
    rs = OM*np.exp(3*xx) + Or*np.exp(4*xx)
    ox = rs/np.cosh(xx)**2
    ww = -1 + (2/3)*np.tanh(xx)
    return 0.5*(OM + 2*Or + ox*(1 + 3*ww))
qs = [q0_of_Om(OM) for OM in np.linspace(0.28, 0.33, 26)]
spread = max(qs) - min(qs)
print(f"{'PASS' if spread < 0.004 else 'FAIL'}  sec.26 q0 spread over Om in [0.28,0.33]: {spread:.5f} < 0.004")
if spread >= 0.004: fails.append("q0 pinning")
lcdm = [1.5*OM - 1 for OM in (0.28, 0.33)]
print(f"INFO  LCDM q0 sweep over same range: {lcdm[0]:.3f} to {lcdm[1]:.3f}")
check("sec.26 acceleration ratio q0/q0_LCDM", q0/(1.5*Om + 2*Or - 1), 0.631, tol=2e-3)

# ---------- R2-5 chronology ----------
z_entry = np.exp(-brentq(q_of, -1.5, -0.1)) - 1
a_exit = np.exp(brentq(q_of, 1.0, 4.0))
check("sec.20.1 entry z", z_entry, 0.7856935)
check("sec.20.1 exit a/a0", a_exit, 11.78652, tol=1e-4)
check("sec.20.1 duration e-folds", np.log(a_exit) + np.log(1 + z_entry), 3.047, tol=1e-3)
th_ex = np.log(a_exit) - Nc
check("sec.20.1 1+3w at exit", 1 + 3*(-1 + (2/3)*np.tanh(th_ex)), -1.59e-2, tol=2e-4)
mfrac = Om*a_exit**-3/(Om*a_exit**-3 + Or*a_exit**-4 + rhostar/np.cosh(th_ex)**2)
check("sec.20.1 matter fraction at exit", mfrac, 1.57e-2, tol=2e-4)

# ---------- R2-6 density history ----------
rows = {5: 0.198, 3: 0.396, 2: 0.605, 1: 0.932, 0.5: 1.076, 0.3417927: 1.089, 0: 1.000}
for z, want in rows.items():
    N = -np.log(1 + z)
    check(f"sec.27.1 ratio at z={z}", rhostar/np.cosh(N - Nc)**2/OX0, want, tol=1e-3)
for a, want in {2: 0.466, 4: 0.141, 11.78652: 0.017}.items():
    check(f"sec.27.1 ratio at a={a}", rhostar/np.cosh(np.log(a) - Nc)**2/OX0, want, tol=1e-3)

# ---------- R2-7 CPL locus + implied crossings ----------
check("A.10 locus at benchmark", 1.5*(1 + w0)**2 - 2/3, wa, tol=1e-9)
for lbl, (W0, Wa), want in [("PP", (-0.838, -0.62), 0.354),
                            ("D5", (-0.752, -0.86), 0.405),
                            ("U3", (-0.667, -1.09), 0.440)]:
    s = (1 + W0)/(-Wa)
    check(f"A.10 implied crossing {lbl}", s/(1 - s), want, tol=1e-3)

# ---------- R2-8 invariant ----------
Ns = np.linspace(-3, 3, 601)
th = Ns - Nc
wX = -1 + (2/3)*np.tanh(th)
inv = 9*(1 + wX)**2 + 6*(2/3)/np.cosh(th)**2
check("sec.19 invariant max|.-4|", float(np.max(np.abs(inv - 4))), 0.0, tol=1e-12)

# ---------- R2-9 ceiling ----------
Tm = (1 - Om - Or)/Om
g = lambda rp: (1 - 9/(4*rp**2))*np.exp((3/rp)*np.arctanh(3/(2*rp))) - Tm  # r_c = 1
check("sec.14 ceiling at benchmark", brentq(g, 1.51, 5.0), 1.8141, tol=1e-3)

print()
print("ALL PASS" if not fails else f"FAILURES: {fails}")
