#!/usr/bin/env python3
"""
verify_causal_wall_spectral_v2_1.py
Receipts for: Causal-Wall Spectral Theory memo v2.0 (referee audit) + v2.1 completion.
No Monte Carlo. Exit code 0 iff all receipts pass.

Receipts
  S1  Spectral dictionary internal consistency [symbolic]:
      Delta^2_S = 4/(pi^4 c0) <=> Im B = (pi^2/64) c0 q^3;
      K = q^3/(2 pi^2 Delta^2) = 8 Im B = (pi^2/8) c0 q^3;  I = pi^4 c0/4;
      Delta^2_T = 32/(pi^4 c2) <=> Im A = (pi^2/16) c2 q^3;  r = 8 c0/c2
  S2  Calibration: c0(k*) = 4/(pi^4 A_s), I_zeta = 1/A_s, per-e-fold growth
  S3  Tensor slot arithmetic: c2/c0 > 8/r_max, c2 lower bound,
      per-mode precision ratio K_gamma/K_zeta = 2/r (register both ratios)
  S4  Geometric-member weld [symbolic + numeric]:
      c0 = 4 eps S_w/pi^4, c2 = 2 S_w/pi^4  =>  r = 16 eps;
      pi^4 c0/4 = eps S_w (concordance with memo v1.x);
      S_w bound via two independent routes agrees; H_mint bound
  S5  Exponential-family Hessian lemma [symbolic]:
      d^2/dz^2 [z psi'(z) - psi(z)]|_0 = psi''(0)  (Hess S_rel = Hess W even with <T> != 0)
  S6  Gauge-limit bookkeeping [symbolic]: eps * Delta^2 = 1/S_w finite as eps -> 0
  S7  Trace algebra [numeric]: delta.delta contraction of A*Pi + B*pi pi = 4B; delta.Pi = 0
  S8  P3 critical spectrum l(l+1)(l+2) via Gamma
  S9  Running class: Planck/ACT tilt tension; minimal-class bound |alpha_s| <~ delta^2;
      implied running band if the tilt difference is physical
  S10 Non-Gaussianity: Ward values, capacity floors, Planck f_NL headroom
  S11 Tilt identities [symbolic]: n_s - 1 = -d ln I/d ln k = -delta; alpha_s = 0 for constant delta
  S12 Informational: dual central-charge reading N ~ sqrt(c0)
"""

import json
import math
import sys

import mpmath as mp
import numpy as np
import sympy as sp

mp.mp.dps = 30
RESULTS = {}
FAIL = 0


def check(name, ok, detail):
    global FAIL
    RESULTS[name] = {"pass": bool(ok), "detail": detail}
    print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    if not ok:
        FAIL += 1


# ----------------------------------------------------------------------
# S1: dictionary internal consistency (symbolic)
# ----------------------------------------------------------------------
q, c0, c2, eps, Sw = sp.symbols('q c0 c2 epsilon S_w', positive=True)

D2S = 4 / (sp.pi ** 4 * c0)
ImB = sp.pi ** 2 / 64 * c0 * q ** 3
ok1a = sp.simplify(q ** 3 / (16 * sp.pi ** 2 * ImB) - D2S) == 0          # (3.6)<->(3.7) scalar
K = q ** 3 / (2 * sp.pi ** 2 * D2S)
ok1b = sp.simplify(K - 8 * ImB) == 0                                     # (3.8) K = 8 Im B
ok1c = sp.simplify(K - sp.pi ** 2 / 8 * c0 * q ** 3) == 0                # (3.8) K = (pi^2/8) c0 q^3
Izeta_sym = 2 * sp.pi ** 2 * K / q ** 3
ok1d = sp.simplify(Izeta_sym - sp.pi ** 4 * c0 / 4) == 0                 # (3.9)
ImA = sp.pi ** 2 / 16 * c2 * q ** 3                                      # registered c2 normalization
D2T = 2 * q ** 3 / (sp.pi ** 2 * ImA)
ok1e = sp.simplify(D2T - 32 / (sp.pi ** 4 * c2)) == 0                    # (3.7) tensor
ok1f = sp.simplify(D2T / D2S - 8 * c0 / c2) == 0                         # (8.1) r = 8 c0/c2
check("S1_dictionary_consistency", bool(ok1a and ok1b and ok1c and ok1d and ok1e and ok1f),
      "Delta^2_S=4/(pi^4 c0) <=> ImB=(pi^2/64)c0 q^3; K=8ImB=(pi^2/8)c0 q^3; I=pi^4 c0/4; "
      "Delta^2_T=32/(pi^4 c2) <=> ImA=(pi^2/16)c2 q^3 [REGISTERED c2 normalization]; r=8c0/c2 "
      "[all exact symbolic]")

# ----------------------------------------------------------------------
# S2: calibration numbers
# ----------------------------------------------------------------------
As = math.exp(3.044) * 1e-10
pi4 = math.pi ** 4
c0_num = 4 / (pi4 * As)
I_num = 1 / As
dP, sP = 0.0351, 0.0042            # Planck 2018
dA, sA = 0.0257, 0.0034            # P-ACT-LB: n_s = 0.9743 +- 0.0034 (registered combination)
perP = math.expm1(dP)
perA = math.expm1(0.026)           # memo's rounded value
ok2 = (abs(c0_num - 1.9564e7) / 1.9564e7 < 2e-4
       and abs(I_num - 4.7644e8) / 4.7644e8 < 2e-4
       and abs(perP - 0.0357) < 2e-4
       and abs(perA - 0.0263) < 2e-4)
check("S2_calibration", ok2,
      f"c0(k*)=4/(pi^4 A_s)={c0_num:.4e} (memo 1.9564e7); I_zeta={I_num:.4e}; "
      f"per-e-fold growth {100*perP:.2f}% (Planck), {100*perA:.2f}% (ACT rounded)")

# ----------------------------------------------------------------------
# S3: tensor slot arithmetic
# ----------------------------------------------------------------------
rmax = 0.036
c_ratio_min = 8 / rmax
c2_min = c_ratio_min * c0_num
Kratio_min = 2 / rmax                 # per-polarization precision ratio K_gamma/K_zeta = 2/r
ok3 = (abs(c_ratio_min - 222.22) < 0.01
       and abs(c2_min - 4.3475e9) / 4.3475e9 < 1e-3
       and abs(Kratio_min - 55.556) < 0.01)
check("S3_tensor_slot", ok3,
      f"c2/c0 > {c_ratio_min:.1f} ({math.log10(c_ratio_min):.2f} orders in spectral density); "
      f"c2(k*) > {c2_min:.3e} (memo 4.35e9); per-mode precision ratio K_g/K_z = 2/r > "
      f"{Kratio_min:.1f} ({math.log10(Kratio_min):.2f} orders) — register WHICH ratio is quoted")

# ----------------------------------------------------------------------
# S4: geometric-member weld
# ----------------------------------------------------------------------
c0_geom = 4 * eps * Sw / sp.pi ** 4
c2_geom = 2 * Sw / sp.pi ** 4
ok4a = sp.simplify(8 * c0_geom / c2_geom - 16 * eps) == 0                # r = 16 eps recovered
ok4b = sp.simplify(sp.pi ** 4 * c0_geom / 4 - eps * Sw) == 0             # I = eps*S_w concordance
# Delta^2_t = 32/(pi^4 c2_geom) = 16/S_w  (memo v1.1 R9 form)
ok4c = sp.simplify(32 / (sp.pi ** 4 * c2_geom) - 16 / Sw) == 0
eps_max = rmax / 16.0
Sw_route1 = I_num / eps_max                    # from I = eps*S_w
Sw_route2 = pi4 * c2_min / 2.0                 # from c2 = 2 S_w/pi^4 at the bound
agree = abs(Sw_route1 - Sw_route2) / Sw_route1
H_max = math.sqrt(8 * math.pi ** 2 / Sw_route1) * 2.435e18
ok4 = ok4a and ok4b and ok4c and agree < 1e-9 and abs(H_max - 4.70e13) / 4.70e13 < 5e-3
check("S4_geometric_member_weld", bool(ok4),
      f"c0=4 eps S_w/pi^4, c2=2 S_w/pi^4 => r=16 eps, Delta^2_t=16/S_w, pi^4 c0/4=eps*S_w "
      f"[symbolic]; S_w bound routes agree to {agree:.1e}: {Sw_route1:.3e} (memo 2.12e11); "
      f"eps<{eps_max:.2e}; H_mint<{H_max:.2e} GeV — all of v2.0 Sec. 8.4-8.6 recovered")

# ----------------------------------------------------------------------
# S5: exponential-family Hessian lemma
# ----------------------------------------------------------------------
z = sp.Symbol('zeta')
psi = sp.Function('psi')
expr = z * sp.diff(psi(z), z) - psi(z)          # S_rel(z) for the tilted family
d2 = sp.diff(expr, z, 2)
ok5 = sp.simplify(d2.subs(z, 0) - sp.diff(psi(z), z, 2).subs(z, 0)) == 0
check("S5_exponential_family_lemma", bool(ok5),
      "d^2/dz^2 [z psi' - psi]|_0 = psi''(0): Hess S_rel = Hess W at coincidence "
      "even though first variations differ (<T> = psi'(0) != 0) [symbolic]")

# ----------------------------------------------------------------------
# S6: gauge-limit bookkeeping
# ----------------------------------------------------------------------
ok6 = sp.simplify(eps * (1 / (eps * Sw)) - 1 / Sw) == 0
check("S6_gauge_limit", bool(ok6),
      "eps * Delta^2_zeta = 1/S_w: the coupling-weighted covariance stays capacity-bounded "
      "as eps -> 0 while Delta^2 itself diverges (zero-information-cost gauge direction)")

# ----------------------------------------------------------------------
# S7: trace algebra of the TT/transverse decomposition
# ----------------------------------------------------------------------
qv = np.array([0.3, -0.4, 0.5])
qv = qv / np.linalg.norm(qv)
d = np.eye(3)
piP = d - np.outer(qv, qv)
Pi = np.zeros((3, 3, 3, 3))
for i in range(3):
    for j in range(3):
        for kk in range(3):
            for l in range(3):
                Pi[i, j, kk, l] = 0.5 * (piP[i, kk] * piP[j, l] + piP[i, l] * piP[j, kk]) \
                    - 0.5 * piP[i, j] * piP[kk, l]
trace_Pi = np.einsum('ij,ijkl->kl', d, Pi)
tt = float(np.einsum('ij,ij->', d, piP) * np.einsum('kl,kl->', d, piP))
ok7 = float(np.max(np.abs(trace_Pi))) < 1e-12 and abs(tt - 4.0) < 1e-12
check("S7_trace_algebra", ok7,
      f"delta^ij Pi_ijkl = 0 (max {float(np.max(np.abs(trace_Pi))):.1e}); "
      f"delta.delta pi pi = {tt:.0f} => <TT> = 4B  [(3.5) exact]")

# ----------------------------------------------------------------------
# S8: P3 critical spectrum via Gamma
# ----------------------------------------------------------------------
maxerr = 0.0
for ell in range(1, 401):
    lam = mp.gamma(ell + 3) / mp.gamma(ell)
    target = ell * (ell + 1) * (ell + 2)
    maxerr = max(maxerr, float(abs(lam - target) / target))
check("S8_P3_spectrum", maxerr < 1e-20, f"Gamma(l+3)/Gamma(l)=l(l+1)(l+2), max rel err {maxerr:.2e}")

# ----------------------------------------------------------------------
# S9: running class — tension, class bound, implied running band
# ----------------------------------------------------------------------
tension = (dP - dA) / math.sqrt(sP ** 2 + sA ** 2)
bound_P = dP ** 2
bound_A = dA ** 2
alpha_band = [(dP - dA) / L for L in (3.0, 1.5)]     # implied alpha_s if tilt diff is physical
planck_alpha = (-0.0045, 0.0067)                     # Planck 2018 X reference
ok9 = (abs(tension - 1.74) < 0.05
       and abs(bound_P - 1.232e-3) / 1.232e-3 < 1e-2
       and alpha_band[0] > bound_P)                  # even the smallest implied alpha exceeds class bound
check("S9_running_class", ok9,
      f"Planck vs P-ACT-LB tilt: Delta delta = {dP-dA:.4f} => {tension:.2f} sigma [WATCH]; "
      f"minimal-class bound |alpha_s| <~ delta^2 = {bound_P:.1e} (P) / {bound_A:.1e} (ACT); "
      f"implied alpha if physical: {alpha_band[0]:.1e}..{alpha_band[1]:.1e} for Dlnk 1.5-3 "
      f"— EXCEEDS class bound; Planck 2018: alpha_s = {planck_alpha[0]}+-{planck_alpha[1]} (consistent w/ 0)")

# ----------------------------------------------------------------------
# S10: non-Gaussianity — Ward values, capacity floors, data headroom
# ----------------------------------------------------------------------
fP = 5 * dP / 12
fA = 5 * 0.026 / 12
floor_c = 1 / math.sqrt(c0_num)
floor_S = 1 / math.sqrt(Sw_route1)
planck_fnl = {"local": (-0.9, 5.1), "equilateral": (-26, 47), "orthogonal": (-38, 24)}
sig = {k2: abs(v[0]) / v[1] for k2, v in planck_fnl.items()}
ok10 = (abs(fP - 0.014625) < 1e-5 and abs(fA - 0.010833) < 1e-5
        and abs(floor_c - 2.26e-4) / 2.26e-4 < 1e-2
        and floor_S < 3e-6
        and all(s < 2.0 for s in sig.values()))
check("S10_non_gaussianity", ok10,
      f"Ward f_NL^sq = {fP:.4f} (P) / {fA:.4f} (ACT); capacity floor 1/sqrt(c0) = {floor_c:.2e}; "
      f"geometric-member intrinsic floor 1/sqrt(S_w) <= {floor_S:.2e}; Planck 2018 IX: "
      f"all shapes consistent with 0 within {max(sig.values()):.1f} sigma — kill |f_NL|>~1 has "
      f">= {min(1/v[1] for v in [(1,5.1)]):.2f}... headroom local sigma=5.1, eq=47, ort=24")

# ----------------------------------------------------------------------
# S11: tilt identities (symbolic)
# ----------------------------------------------------------------------
u = sp.Symbol('u')                                   # u = ln k
delta_s = sp.Symbol('delta', positive=True)
Istar = sp.Symbol('I_*', positive=True)
I_of_u = Istar * sp.exp(delta_s * u)
ns1 = -sp.diff(sp.log(I_of_u), u)
alpha = -sp.diff(sp.log(I_of_u), u, 2)
ok11 = sp.simplify(ns1 + delta_s) == 0 and sp.simplify(alpha) == 0
check("S11_tilt_identities", bool(ok11),
      "n_s - 1 = -d ln I/d ln k = -delta; alpha_s = 0 for constant delta [symbolic]")

# ----------------------------------------------------------------------
# S12: informational — dual central-charge reading
# ----------------------------------------------------------------------
N_dual = math.sqrt(c0_num)
check("S12_dual_N_reading", 4000 < N_dual < 5000,
      f"c0 ~ N^2 reading: N ~ {N_dual:.0f} (order-of-magnitude, normalization-dependent; "
      f"matches the 'perturbative large-N QFT' regime of the holographic fits)")

# ----------------------------------------------------------------------
# summary + JSON
# ----------------------------------------------------------------------
RESULTS["_summary"] = {
    "total": len([r for r in RESULTS if not r.startswith('_')]),
    "failed": FAIL,
    "constants": {
        "A_s": As, "c0_star": c0_num, "I_zeta": I_num,
        "delta_Planck": dP, "delta_PACTLB": dA, "tilt_tension_sigma": tension,
        "c2_over_c0_min": c_ratio_min, "c2_min": c2_min,
        "K_ratio_per_pol_min": Kratio_min,
        "eps_mint_max": eps_max, "Sw_mint_min": Sw_route1, "H_mint_max_GeV": H_max,
        "alpha_class_bound_P": bound_P, "alpha_implied_band": alpha_band,
        "fNL_ward_P": fP, "fNL_ward_ACT": fA,
        "NG_floor_capacity": floor_c, "NG_floor_geometric": floor_S,
        "N_dual_reading": N_dual,
    },
}
with open("/mnt/user-data/outputs/causal_wall_spectral_receipts_v2_1.json", "w") as f:
    json.dump(RESULTS, f, indent=2)

n_ok = RESULTS["_summary"]["total"] - FAIL
print(f"\n{n_ok}/{RESULTS['_summary']['total']} receipts pass.")
sys.exit(1 if FAIL else 0)
