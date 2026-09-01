#!/usr/bin/env python3
"""Receipts for the Lorentzian spectral envelope. Stdlib only; exit nonzero on failure.

What a pass establishes: three pieces of exact arithmetic behind the module's
dictionary between (i) a Cauchy/Lorentzian line in energy, (ii) two-sided
exponential correlation in time, and (iii) spectral contraction by a transfer
operator after reconstruction. It does NOT identify that operator with a
non-invertible descent or establish reflection positivity
for any interacting theory, the continuum limit of any gap, or any physical
identification of the wall.

Checks
  A. Fourier pair: C(t) = exp(-G|t|/2 - i E0 t)  <->  S(w) = G / ((w-E0)^2 + G^2/4).
  B. Euclidean clustering exp(-m|tau|) has spectral transform 2m/(w^2+m^2). The pole
     position is RECOVERED from the numerical transform: 1/hatC(w) is fitted to a w^2 + b at
     three frequencies and the fit must return b/a = m^2 (roots at +-i m) and a = 1/(2m).
  C. 1d Ising transfer matrix (a finite debugging model for transfer contraction and gap):
     the matrix must remain invertible throughout the tested positive-coupling sweep;
     the ring two-point function, computed by explicit matrix contraction, must equal
     (lambda1/lambda0)^n with the finite-ring correction, across a sweep of K; and the
     gap -ln(lambda1/lambda0) must decrease monotonically across the sweep and already be below
     1e-4 at K=5, sampling its analytic approach to zero as K -> infinity.
  D. Numbers only: the lattice-resolved 0++ gap-candidate length vs the causal grain, and the lattice-consistent
     pure ratios versus the convention-mixed ones.
"""
import json, math, sys, cmath

FAIL = []
def check(name, val, ref, rtol=1e-6, atol=0.0):
    ok = abs(val - ref) <= max(atol, rtol * abs(ref))
    if not ok: FAIL.append((name, val, ref))
    return val

out = {}

# ---- A. Cauchy line <-> two-sided exponential correlation ------------------
E0, G = 1.3, 0.4
def S_num(w, T=400.0, n=400001):
    # trapezoid over t in [-T, T] of C(t) e^{i w t}; C decays like e^{-G|t|/2}
    h = 2*T/(n-1); acc = 0.0
    for k in range(n):
        t = -T + k*h
        c = math.exp(-G*abs(t)/2) * cmath.exp(-1j*E0*t) * cmath.exp(1j*w*t)
        wgt = 0.5 if k in (0, n-1) else 1.0
        acc += wgt * c.real
    return acc*h
for w in (0.0, 1.0, 1.3, 1.5, 3.0):
    ref = G/((w-E0)**2 + G**2/4)
    out[f"A_S({w})"] = check(f"A_S({w})", S_num(w), ref, rtol=1e-4)
# half-maximum test: S(E0 +- G/2) must equal S(E0)/2, so the full width at half maximum is Gamma
S_peak = S_num(E0); S_half = S_num(E0 + G/2)
out["A_half_max_ratio"] = check("A_half_max", S_half/S_peak, 0.5, rtol=1e-4)

# ---- B. Euclidean clustering -> pole at +- i m -----------------------------
m = 0.7
def hatC(w, T=300.0, n=300001):
    h = 2*T/(n-1); acc = 0.0
    for k in range(n):
        tau = -T + k*h
        wgt = 0.5 if k in (0, n-1) else 1.0
        acc += wgt * math.exp(-m*abs(tau)) * math.cos(w*tau)
    return acc*h
ws = (0.0, 0.5, 2.0)
vals = [hatC(w) for w in ws]
for w, v in zip(ws, vals):
    out[f"B_hatC({w})"] = check(f"B_hatC({w})", v, 2*m/(w**2+m**2), rtol=1e-4)
# recover the pole from the numerics: least-squares fit of 1/hatC(w) = a w^2 + b
ys = [1.0/v for v in vals]; xs = [w*w for w in ws]
xb = sum(xs)/3; yb = sum(ys)/3
a_fit = sum((x-xb)*(y-yb) for x, y in zip(xs, ys)) / sum((x-xb)**2 for x in xs)
b_fit = yb - a_fit*xb
out["B_fit_a_vs_1/(2m)"] = check("B_fit_a", a_fit, 1.0/(2*m), rtol=1e-3)
out["B_fit_pole_m2_from_b/a"] = check("B_fit_pole", b_fit/a_fit, m*m, rtol=1e-3)

# ---- C. 1d Ising transfer matrix: invertibility, contraction, and gap -------
K = 0.8
lam0, lam1 = 2*math.cosh(K), 2*math.sinh(K)
# eigenvalues by hand from the 2x2 symmetric matrix
a, b = math.exp(K), math.exp(-K)
tr, det = 2*a, a*a - b*b
disc = math.sqrt(tr*tr - 4*det)
e_hi, e_lo = (tr+disc)/2, (tr-disc)/2
out["C_lambda0"] = check("C_lambda0", e_hi, lam0)
out["C_lambda1"] = check("C_lambda1", e_lo, lam1)
out["C_det_T(K=0.8)"] = check("C_det_T(K=0.8)", det, 2*math.sinh(2*K))
ratio = e_lo/e_hi
out["C_ratio(K=0.8)"] = ratio
# two-point function by explicit transfer-matrix contraction on a ring of N sites
def two_point_ring(Kk, n, N=60):
    # <s0 s_n> = Tr(S T^n S T^{N-n}) / Tr(T^N), S = diag(1,-1)
    aa, bb = math.exp(Kk), math.exp(-Kk)
    def mm(X, Y): return [[sum(X[i][k]*Y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    def mpow(X, p):
        R = [[1.0,0.0],[0.0,1.0]]
        for _ in range(p): R = mm(R, X)
        return R
    T = [[aa, bb],[bb, aa]]; Sg = [[1.0,0.0],[0.0,-1.0]]
    num = mm(mm(Sg, mpow(T, n)), mm(Sg, mpow(T, N-n)))
    den = mpow(T, N)
    return (num[0][0]+num[1][1])/(den[0][0]+den[1][1])
gaps = []
for Kk in (0.2, 0.8, 2.0, 5.0):
    r = math.tanh(Kk)          # lambda1/lambda0 = 2 sinh K / 2 cosh K
    det_k = math.exp(2*Kk) - math.exp(-2*Kk)
    out[f"C_det_positive_K{Kk}"] = check(f"C_det_positive_K{Kk}", float(det_k > 0), 1.0)
    for n in (1, 3, 7):
        ring = two_point_ring(Kk, n)
        exact = r**n * (1 + r**(60-2*n)) / (1 + r**60)   # finite-ring correction
        out[f"C_two_point_K{Kk}_n{n}"] = check(f"C_two_point_K{Kk}_n{n}", ring, exact, rtol=1e-9, atol=1e-14)
    gaps.append(-math.log(r))
out["C_gap_ma_by_K"] = dict(zip(("0.2","0.8","2.0","5.0"), [round(g, 6) for g in gaps]))
# the gap must shrink across the sweep and be small by K=5, sampling the analytic limit
for i in range(len(gaps)-1):
    check(f"C_gap_monotone_{i}", float(gaps[i] > gaps[i+1]), 1.0)
out["C_gap_at_K5_small"] = check("C_gap_K5", gaps[-1], 0.0, atol=1e-4)
out["C_inverse_xi(K=0.8)"] = check("C_inv_xi", -math.log(ratio), -math.log(math.tanh(K)))

# ---- D. Numbers: lattice 0++ gap candidate vs causal grain (report, plus range regression) ----
hbarc_MeVfm = 197.3269804
m0pp_range = (1653.0, 1730.0)          # SU(3) 0++ glueball, lattice determinations
grain_range = (46.27, 47.21)           # MeV, the two crossing branches
out["D_gap_candidate_length_fm_range"] = [round(hbarc_MeVfm/m0pp_range[1], 4), round(hbarc_MeVfm/m0pp_range[0], 4)]
out["D_grain_length_fm_range"] = [round(hbarc_MeVfm/grain_range[1], 4), round(hbarc_MeVfm/grain_range[0], 4)]
lo = (hbarc_MeVfm/grain_range[1])/(hbarc_MeVfm/m0pp_range[0]); hi = (hbarc_MeVfm/grain_range[0])/(hbarc_MeVfm/m0pp_range[1])
out["D_grain_over_gap_candidate_range"] = [round(lo, 1), round(hi, 1)]
check("D_ratio_range_matches_prose", float(34.5 < lo < hi < 38.0), 1.0)
out["D_pure_numbers"] = {"m0pp_over_sqrt_sigma_lattice_consistent_LuciniTeper": 3.55,
                         "m0pp_over_sqrt_sigma_convention_mixed_1730_over_440": round(1730.0/440.0, 2),
                         "m2pp_over_m0pp": round(2390.0/1730.0, 2)}

if "--json" in sys.argv:
    print(json.dumps({"results": out, "failures": FAIL}, indent=2, default=str))
else:
    for k, v in out.items(): print(f"{k:32s} {v}")
    print("FAILURES:", FAIL if FAIL else "none")
sys.exit(1 if FAIL else 0)
